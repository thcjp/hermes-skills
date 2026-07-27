#!/usr/bin/env python3
"""
SKILL深度重写工具 (v1.0)
========================
基于评分反馈，精准识别SKILL.md的缺陷维度，
使用LLM生成针对性增强内容，补齐缺失部分。

核心策略:
  1. 评分 → 分析反馈 → 识别缺陷维度
  2. 针对每个缺陷维度生成具体增强内容（非泛泛而谈）
  3. 将增强内容插入SKILL.md的合适位置
  4. 重新评分验证提升效果

Usage:
  python skill_deep_rewrite.py <skill_dir>              # 增强单个skill
  python skill_deep_rewrite.py <skill_dir> --dry-run     # 只预览不修改
  python skill_deep_rewrite.py --batch <db_query>        # 批量处理
  python skill_deep_rewrite.py --batch-range 4.0 4.5     # 按分数范围批量
"""

import json
import os
import sys
import re
import time
import shutil
import sqlite3
from pathlib import Path
from datetime import datetime

import requests

# 项目根目录
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_DB_PATH = str(_PROJECT_ROOT / "skill-registry.db")
_CONFIG_PATH = _PROJECT_ROOT / "data" / "config" / "quality_scoring_config.json"
_BACKUP_DIR = _PROJECT_ROOT / "data" / "backups" / "skill-rewrites"
_BACKUP_DIR.mkdir(parents=True, exist_ok=True)

# 导入评分器
sys.path.insert(0, str(_PROJECT_ROOT / "tools"))
from local_quality_scorer import score_skill, _load_config, _get_api_key


def _call_llm(prompt, config=None, api_key=None, max_retries=2):
    """调用LLM API"""
    if config is None:
        config = _load_config()
    if api_key is None:
        api_key = _get_api_key(config)
    
    if not api_key:
        return {"error": "未找到API密钥"}
    
    llm_config = config.get("llm", {})
    endpoint = llm_config.get("api_endpoint", "https://api.siliconflow.cn/v1/chat/completions")
    model = llm_config.get("model", "deepseek-ai/DeepSeek-V3")
    max_tokens = llm_config.get("max_tokens", 3000)
    temperature = llm_config.get("temperature", 0.4)
    timeout = llm_config.get("timeout", 120)
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是一位专业的SKILL.md技术文档工程师，擅长根据评测反馈精准补齐文档缺陷。"},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    
    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(endpoint, headers=headers, json=payload, timeout=timeout)
            resp.raise_for_status()
            data = resp.json()
            content = data["choices"][0]["message"]["content"]
            return {"content": content}
        except requests.exceptions.Timeout:
            if attempt < max_retries:
                time.sleep(2)
                continue
            return {"error": f"LLM API请求超时({timeout}s)"}
        except Exception as e:
            if attempt < max_retries:
                time.sleep(2)
                continue
            return {"error": f"LLM API调用异常: {e}"}
    
    return {"error": "LLM API调用失败，已重试"}


def _analyze_gaps(score_result):
    """分析评分结果，识别需要改进的维度和具体缺陷"""
    gaps = []
    dimensions = score_result.get("dimensions", {})
    
    dim_names = {
        "completeness": "功能完整性",
        "accuracy": "准确性",
        "usability": "易用性",
        "security": "安全性",
        "innovation": "创新性",
    }
    
    for dim_key, dim_data in dimensions.items():
        score = dim_data.get("score", 0.0)
        reason = dim_data.get("reason", "")
        
        if score < 0.9:
            # 提取具体缺陷关键词
            specific_issues = _extract_specific_issues(dim_key, reason)
            gaps.append({
                "dimension": dim_key,
                "dimension_name": dim_names.get(dim_key, dim_key),
                "current_score": score,
                "reason": reason,
                "specific_issues": specific_issues,
            })
    
    # 按分数升序排列（最差的先处理）
    gaps.sort(key=lambda g: g["current_score"])
    return gaps


def _extract_specific_issues(dim_key, reason):
    """从评分理由中提取具体缺陷"""
    issues = []
    
    # 通用缺陷检测
    issue_patterns = {
        "FAQ": ["FAQ", "常见问题", "troubleshooting"],
        "示例不足": ["示例不够", "示例不足", "缺少示例", "示例略少", "示例可以更丰富"],
        "参数描述": ["参数", "默认值", "参数描述"],
        "错误处理": ["错误处理", "错误码", "异常处理"],
        "边界条件": ["边界", "边缘", "corner case"],
        "安全细节": ["安全", "密钥", "加密", "审计"],
        "依赖说明": ["依赖", "depend", "requirement"],
        "文档结构": ["文档结构", "结构清晰", "导航"],
        "差异化": ["差异化", "独特", "创新", "亮点"],
        "场景不足": ["场景", "使用场景", "应用场景"],
        "frontmatter": ["frontmatter", "元数据"],
        "代码示例": ["代码", "code example", "可运行"],
        "实现细节": ["实现细节", "具体实现", "detail"],
    }
    
    for issue_name, keywords in issue_patterns.items():
        for kw in keywords:
            if kw.lower() in reason.lower():
                issues.append(issue_name)
                break
    
    return issues


def _build_enhancement_prompt(skill_content, gaps, slug):
    """构建增强内容生成prompt"""
    
    # 构建缺陷描述
    gap_descriptions = []
    for gap in gaps:
        issues_str = ", ".join(gap["specific_issues"]) if gap["specific_issues"] else "综合提升"
        gap_descriptions.append(
            f"### {gap['dimension_name']} (当前: {gap['current_score']:.1f}, 目标: 0.9)\n"
            f"评测反馈: {gap['reason']}\n"
            f"需补齐: {issues_str}"
        )
    
    gaps_text = "\n\n".join(gap_descriptions)
    
    prompt = f"""请基于以下评测反馈，为SKILL.md生成针对性的增强内容。

## 当前SKILL.md内容
{skill_content[:20000]}

## 评测发现的缺陷
{gaps_text}

## 增强内容生成要求

请为每个缺陷维度生成具体的增强内容，遵循以下原则：

1. **内容必须具体且与技能主题相关** — 不要泛泛而谈，要结合技能的实际功能
2. **内容必须实质且详尽** — 每个增强部分至少200字，包含具体的技术细节
3. **内容必须与现有内容互补** — 不要重复已有内容，只补齐缺失部分
4. **格式为Markdown** — 使用合适的标题层级和格式

### 各维度增强模板

**功能完整性 (completeness)**:
- 补充详细的功能列表（含边界条件处理）
- 补充输入输出参数说明（含默认值、类型、取值范围）
- 补充错误码定义和处理方案

**准确性 (accuracy)**:
- 补充可运行的技术示例（含完整上下文）
- 修正不准确的描述
- 补充依赖版本和兼容性说明

**易用性 (usability)**:
- 补充FAQ部分（至少5个常见问题及解答）
- 补充Troubleshooting故障排查指南
- 补充更多使用场景示例

**安全性 (security)**:
- 补充安全架构说明
- 补充API密钥安全存储和处理机制
- 补充数据保护和隐私说明
- 补充安全审计清单

**创新性 (innovation)**:
- 补充技术亮点与差异化优势分析
- 补充与同类方案的对比
- 补充解决的真实验证痛点
- 补充技术或方法创新点

## 输出格式

请按以下JSON格式返回（不要包含其他内容）：
```json
{{
  "enhancements": [
    {{
      "dimension": "维度名",
      "section_title": "增强内容标题",
      "content": "增强内容（Markdown格式，至少200字）",
      "insert_after": "插入位置（SKILL.md中的标题或'append'表示追加到末尾）"
    }}
  ]
}}
```

请确保每个缺陷维度都有对应的增强内容。"""

    return prompt


def _parse_enhancement_response(content):
    """解析LLM返回的增强内容"""
    # 尝试从markdown代码块中提取JSON
    json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", content, re.DOTALL)
    if json_match:
        content = json_match.group(1)
    
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        start = content.find("{")
        end = content.rfind("}")
        if start != -1 and end != -1:
            try:
                data = json.loads(content[start:end+1])
            except json.JSONDecodeError as e:
                return {"error": f"无法解析增强内容JSON: {e}"}
        else:
            return {"error": "LLM返回中未找到JSON结构"}
    
    return {"enhancements": data.get("enhancements", [])}


def _apply_enhancements(original_content, enhancements):
    """将增强内容应用到SKILL.md"""
    lines = original_content.split("\n")
    modified_content = original_content
    
    for enh in enhancements:
        section_title = enh.get("section_title", "")
        content = enh.get("content", "")
        insert_after = enh.get("insert_after", "append")
        
        if not content.strip():
            continue
        
        # 构建增强块
        enhancement_block = f"\n\n## {section_title}\n\n{content}\n"
        
        if insert_after == "append" or not insert_after:
            # 追加到末尾
            modified_content += enhancement_block
        else:
            # 尝试在指定标题后插入
            # 查找标题位置（支持 ## 和 ### 前缀）
            patterns = [
                f"\n## {insert_after}\n",
                f"\n## {insert_after}",
                f"\n### {insert_after}\n",
                f"\n### {insert_after}",
                f"\n# {insert_after}\n",
                f"\n# {insert_after}",
            ]
            
            inserted = False
            for pattern in patterns:
                idx = modified_content.find(pattern)
                if idx != -1:
                    # 找到该section的末尾（下一个##或文件末尾）
                    section_start = idx + len(pattern)
                    next_section = modified_content.find("\n## ", section_start)
                    if next_section == -1:
                        next_section = modified_content.find("\n### ", section_start)
                    if next_section == -1:
                        next_section = len(modified_content)
                    
                    # 在该section末尾插入增强内容
                    modified_content = (
                        modified_content[:next_section] + 
                        enhancement_block + 
                        modified_content[next_section:]
                    )
                    inserted = True
                    break
            
            if not inserted:
                # 找不到插入位置，追加到末尾
                modified_content += enhancement_block
    
    return modified_content


def _backup_skill(skill_path):
    """备份原始SKILL.md"""
    skill_md = Path(skill_path) / "SKILL.md"
    if not skill_md.exists():
        return None
    
    slug = Path(skill_path).name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = _BACKUP_DIR / f"{slug}_{timestamp}.md"
    shutil.copy2(skill_md, backup_path)
    return str(backup_path)


def enhance_skill(skill_path, dry_run=False, skip_if_passing=True):
    """
    增强单个skill
    
    参数:
        skill_path: skill目录路径
        dry_run: 只预览不修改
        skip_if_passing: 如果已通过(>=4.5)则跳过
    
    返回:
        {
            "slug": str,
            "original_score": float,
            "new_score": float,
            "improvement": float,
            "gaps_addressed": list,
            "backup_path": str,
            "dry_run": bool,
            "status": str,  # success/skip/error
        }
    """
    skill_path = Path(skill_path)
    skill_md = skill_path / "SKILL.md"
    slug = skill_path.name
    
    if not skill_md.exists():
        return {"slug": slug, "status": "error", "error": "SKILL.md不存在"}
    
    # 读取原始内容
    original_content = skill_md.read_text(encoding="utf-8")
    
    # 1. 评分
    print(f"  [{slug}] 评分中...", flush=True)
    score_result = score_skill(skill_path)
    
    if score_result.get("error"):
        return {"slug": slug, "status": "error", "error": f"评分失败: {score_result['error']}"}
    
    original_score = score_result["total_score"]
    print(f"  [{slug}] 原始分数: {original_score:.2f}", flush=True)
    
    # 检查是否需要增强
    if skip_if_passing and original_score >= 4.5:
        return {
            "slug": slug,
            "status": "skip",
            "reason": "已通过(>=4.5)",
            "original_score": original_score,
        }
    
    # 2. 分析缺陷
    gaps = _analyze_gaps(score_result)
    if not gaps:
        return {
            "slug": slug,
            "status": "skip",
            "reason": "无缺陷维度",
            "original_score": original_score,
        }
    
    gap_dims = [g["dimension"] for g in gaps]
    print(f"  [{slug}] 缺陷维度: {gap_dims}", flush=True)
    
    # 3. 生成增强内容
    prompt = _build_enhancement_prompt(original_content, gaps, slug)
    print(f"  [{slug}] 生成增强内容...", flush=True)
    
    llm_result = _call_llm(prompt)
    if llm_result.get("error"):
        return {"slug": slug, "status": "error", "error": f"LLM生成失败: {llm_result['error']}"}
    
    parsed = _parse_enhancement_response(llm_result["content"])
    if parsed.get("error"):
        return {"slug": slug, "status": "error", "error": parsed["error"]}
    
    enhancements = parsed.get("enhancements", [])
    if not enhancements:
        return {"slug": slug, "status": "error", "error": "LLM未返回增强内容"}
    
    print(f"  [{slug}] 生成 {len(enhancements)} 个增强块", flush=True)
    
    # 4. 应用增强
    new_content = _apply_enhancements(original_content, enhancements)
    
    if dry_run:
        total_enhancement_chars = sum(len(e.get("content", "")) for e in enhancements)
        return {
            "slug": slug,
            "status": "dry_run",
            "original_score": original_score,
            "gaps_addressed": gap_dims,
            "enhancement_count": len(enhancements),
            "enhancement_chars": total_enhancement_chars,
            "original_length": len(original_content),
            "new_length": len(new_content),
            "enhancement_preview": enhancements[0].get("content", "")[:200] if enhancements else "",
        }
    
    # 5. 备份
    backup_path = _backup_skill(skill_path)
    
    # 6. 写入新内容
    skill_md.write_text(new_content, encoding="utf-8")
    print(f"  [{slug}] 已写入增强内容 (原始: {len(original_content)}字 → 新: {len(new_content)}字)", flush=True)
    
    # 7. 重新评分
    print(f"  [{slug}] 重新评分...", flush=True)
    time.sleep(1)  # 避免API速率限制
    new_score_result = score_skill(skill_path)
    
    if new_score_result.get("error"):
        return {
            "slug": slug,
            "status": "error",
            "error": f"重新评分失败: {new_score_result['error']}",
            "original_score": original_score,
            "backup_path": backup_path,
        }
    
    new_score = new_score_result["total_score"]
    improvement = new_score - original_score
    print(f"  [{slug}] 新分数: {new_score:.2f} (提升: {improvement:+.2f})", flush=True)
    
    # 8. 更新DB中的评分
    try:
        conn = sqlite3.connect(_DB_PATH)
        c = conn.cursor()
        now = datetime.now().isoformat()
        feedback = new_score_result.get("feedback", "")[:500]
        dims_json = json.dumps(new_score_result.get("dimensions", {}), ensure_ascii=False)
        c.execute("""
            UPDATE skills 
            SET local_quality_score = ?,
                local_score_feedback = ?,
                local_score_at = ?,
                updated_at = ?
            WHERE slug = ?
        """, (new_score, feedback, now, now, slug))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"  [{slug}] DB更新警告: {e}", flush=True)
    
    return {
        "slug": slug,
        "status": "success" if improvement > 0 else "no_improvement",
        "original_score": round(original_score, 2),
        "new_score": round(new_score, 2),
        "improvement": round(improvement, 2),
        "passed": new_score >= 4.5,
        "gaps_addressed": gap_dims,
        "backup_path": backup_path,
        "enhancement_count": len(enhancements),
    }


def batch_enhance(score_range=None, limit=None, dry_run=False, force=False):
    """
    批量增强skill
    
    参数:
        score_range: (min_score, max_score) 元组，指定分数范围
        limit: 限制处理数量
        dry_run: 只预览不修改
        force: 即使已通过也处理
    """
    conn = sqlite3.connect(_DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # 构建查询
    query = """
        SELECT slug, local_path, local_quality_score
        FROM skills
        WHERE local_quality_score > 0
    """
    params = []
    
    if score_range:
        query += " AND local_quality_score >= ? AND local_quality_score < ?"
        params.extend(score_range)
    
    if not force:
        query += " AND local_quality_score < 4.5"
    
    query += " ORDER BY local_quality_score DESC"
    
    if limit:
        query += " LIMIT ?"
        params.append(limit)
    
    c.execute(query, params)
    skills = c.fetchall()
    conn.close()
    
    print(f"待处理skill数: {len(skills)}", flush=True)
    if score_range:
        print(f"分数范围: {score_range[0]}-{score_range[1]}", flush=True)
    
    results = []
    success_count = 0
    error_count = 0
    skip_count = 0
    total_improvement = 0.0
    
    for i, skill in enumerate(skills):
        slug = skill["slug"]
        local_path = skill["local_path"]
        current_score = skill["local_quality_score"]
        
        if not local_path or not Path(local_path).exists():
            # 尝试根据slug查找路径
            possible_paths = [
                _PROJECT_ROOT / "packaged-skills" / "skillhub" / slug,
                _PROJECT_ROOT / "opensource-skills" / "packaged" / slug,
                _PROJECT_ROOT / "differentiated-skills" / slug,
                _PROJECT_ROOT / "clawhub-skills" / slug,
                _PROJECT_ROOT / "enterprise-upload" / slug,
            ]
            skill_path = None
            for p in possible_paths:
                if p.exists() and (p / "SKILL.md").exists():
                    skill_path = p
                    break
            
            if not skill_path:
                print(f"  [{i+1}/{len(skills)}] SKIP {slug}: 路径不存在", flush=True)
                skip_count += 1
                continue
        else:
            skill_path = Path(local_path)
            if not skill_path.exists():
                # local_path可能是文件路径，取父目录
                skill_path = skill_path.parent
        
        if not (skill_path / "SKILL.md").exists():
            print(f"  [{i+1}/{len(skills)}] SKIP {slug}: SKILL.md不存在", flush=True)
            skip_count += 1
            continue
        
        print(f"\n[{i+1}/{len(skills)}] 处理: {slug} (当前: {current_score:.2f})", flush=True)
        
        result = enhance_skill(skill_path, dry_run=dry_run, skip_if_passing=not force)
        results.append(result)
        
        if result["status"] == "success":
            success_count += 1
            total_improvement += result["improvement"]
        elif result["status"] == "skip":
            skip_count += 1
        else:
            error_count += 1
        
        # API速率限制
        time.sleep(1.5)
    
    # 生成报告
    report = {
        "timestamp": datetime.now().isoformat(),
        "total": len(skills),
        "success": success_count,
        "skip": skip_count,
        "error": error_count,
        "avg_improvement": round(total_improvement / success_count, 2) if success_count > 0 else 0,
        "results": results,
    }
    
    report_path = _PROJECT_ROOT / "data" / "reports" / "deep_rewrite_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*60}", flush=True)
    print(f"批量处理完成:", flush=True)
    print(f"  总数: {len(skills)}", flush=True)
    print(f"  成功: {success_count}", flush=True)
    print(f"  跳过: {skip_count}", flush=True)
    print(f"  错误: {error_count}", flush=True)
    print(f"  平均提升: {report['avg_improvement']:+.2f}", flush=True)
    print(f"  报告: {report_path}", flush=True)
    
    return report


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    if sys.argv[1] == "--batch-range":
        # 按分数范围批量处理
        if len(sys.argv) < 4:
            print("用法: python skill_deep_rewrite.py --batch-range <min> <max> [--limit N] [--dry-run]")
            sys.exit(1)
        
        min_score = float(sys.argv[2])
        max_score = float(sys.argv[3])
        limit = None
        dry_run = "--dry-run" in sys.argv
        
        if "--limit" in sys.argv:
            idx = sys.argv.index("--limit")
            if idx + 1 < len(sys.argv):
                limit = int(sys.argv[idx + 1])
        
        batch_enhance(score_range=(min_score, max_score), limit=limit, dry_run=dry_run)
        return
    
    if sys.argv[1] == "--batch":
        # 批量处理所有未通过的
        limit = None
        dry_run = "--dry-run" in sys.argv
        
        if "--limit" in sys.argv:
            idx = sys.argv.index("--limit")
            if idx + 1 < len(sys.argv):
                limit = int(sys.argv[idx + 1])
        
        batch_enhance(limit=limit, dry_run=dry_run)
        return
    
    # 单个skill处理
    skill_path = sys.argv[1]
    dry_run = "--dry-run" in sys.argv
    
    result = enhance_skill(skill_path, dry_run=dry_run)
    print(f"\n{'='*60}")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
