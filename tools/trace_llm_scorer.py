#!/usr/bin/env python3
"""
LLM驱动的TRACE评分脚本 v2.0
===========================
增强功能：
1. 静态评分（T+C维度）- 全自动
2. LLM评分（R+A+E维度）- 批量生成评估内容，LLM评估后导入
3. 批量评估 - 支持大批量skill的高效评分
4. 评分报告 - 生成详细的TRACE评分报告

Usage:
    python trace_llm_scorer.py static                    # 全部skill静态评分
    python trace_llm_scorer.py static --packaged         # 仅60个packaged skill静态评分
    python trace_llm_scorer.py export --packaged         # 导出60个skill供LLM评估
    python trace_llm_scorer.py export --limit 100        # 导出100个skill供LLM评估
    python trace_llm_scorer.py import <results.json>     # 导入LLM评估结果
    python trace_llm_scorer.py report                    # 生成评分报告
    python trace_llm_scorer.py report --packaged         # 仅60个packaged skill报告
"""

import sqlite3
import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional

# 导入统一配置（修复U-21硬编码路径、U-23阈值不一致）
import os as _os
_sys_path = _os.path.dirname(_os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)
from config import (
    DB_PATH, EXPORT_DIR, TRACE_PASS_THRESHOLD, TRACE_FIELD_MAPPING,
    PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, SCORE_TYPE_TRACE_LLM,
    L2_PASS_THRESHOLD, L2_EXCELLENT_THRESHOLD, L2_MANUAL_REVIEW_THRESHOLD,
    create_backup
)

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# TRACE评估Prompt模板（用于LLM评估）
TRACE_EVAL_PROMPT = """请按照SkillHub TRACE评测体系评估以下Skill。

## TRACE五维度
- T (Trust 可信任度): 安全性、国内可用性、中文支持
- R (Reliability 可靠性): 异常处理、边界输入、失败反馈
- A (Adaptability 适用性): description精准、能力边界清晰、触发条件明确
- C (Convention 规范性): 信息架构、文档充分性、章节完整性
- E (Effectiveness 有效性): 解决问题、输出可用、额外价值

## 评分标准(每维度0-10分)
- 9-10: 卓越，行业标杆
- 7-8: 良好，满足要求
- 5-6: 及格，有改进空间
- 3-4: 不足，需要修复
- 0-2: 严重缺失

## 待评估SKILL.md
{skill_content}

## 输出格式(严格JSON)
{{
  "trace_scores": {{
    "trust": {{"score": 0, "reason": "", "suggestion": ""}},
    "reliability": {{"score": 0, "reason": "", "suggestion": ""}},
    "adaptability": {{"score": 0, "reason": "", "suggestion": ""}},
    "convention": {{"score": 0, "reason": "", "suggestion": ""}},
    "effectiveness": {{"score": 0, "reason": "", "suggestion": ""}}
  }},
  "total_score": 0,
  "top_3_issues": ["", "", ""],
  "quality_grade": "A|B|C|D"
}}

等级: A(45-50) B(40-44) C(30-39) D(<30)
"""

def get_all_skills(limit=None, specific_slugs=None, packaged_only=False):
    """获取待评估的skill列表
    
    修复U-26：使用参数化查询替代f-string拼接LIMIT
    修复U-21：使用config中的路径常量替代硬编码
    """
    conn = get_db()
    c = conn.cursor()
    
    if packaged_only:
        # 获取60个packaged skills
        skills = []
        # JueJin 20个（使用config路径）
        if PACKAGED_SKILLS_DIR.exists():
            for d in sorted(PACKAGED_SKILLS_DIR.iterdir()):
                if d.is_dir() and (d / "SKILL.md").exists():
                    c.execute("SELECT id, slug, current_display_name, local_path, source, edition FROM skills WHERE slug = ?", (d.name,))
                    row = c.fetchone()
                    if row:
                        skills.append(dict(row))
        # Open Source 40个（使用config路径）
        if OPENSOURCE_SKILLS_DIR.exists():
            for d in sorted(OPENSOURCE_SKILLS_DIR.iterdir()):
                if d.is_dir() and (d / "SKILL.md").exists():
                    c.execute("SELECT id, slug, current_display_name, local_path, source, edition FROM skills WHERE slug = ?", (d.name,))
                    row = c.fetchone()
                    if row:
                        skills.append(dict(row))
        conn.close()
        return skills
    
    if specific_slugs:
        placeholders = ','.join('?' * len(specific_slugs))
        c.execute(f"""
            SELECT id, slug, current_display_name, local_path, source, edition
            FROM skills
            WHERE slug IN ({placeholders})
              AND workflow_state != 'deprecated'
            ORDER BY slug
        """, specific_slugs)
    else:
        query = """
            SELECT id, slug, current_display_name, local_path, source, edition
            FROM skills
            WHERE workflow_state != 'deprecated'
            ORDER BY slug
        """
        if limit:
            query += " LIMIT ?"
            c.execute(query, (limit,))
        else:
            c.execute(query)
    
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return results

def read_skill_md(local_path):
    """读取SKILL.md内容"""
    if not local_path:
        return ""
    skill_md_path = Path(local_path) / "SKILL.md"
    if not skill_md_path.exists():
        skill_md_path = Path(local_path)
        if not skill_md_path.exists():
            return ""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    return content

def static_check(skill_content):
    """静态检查（T和C维度的静态部分）"""
    checks = {
        'has_frontmatter': False,
        'has_displayName': False,
        'has_summary': False,
        'has_description': False,
        'has_license': False,
        'has_tools': False,
        'has_core_capability': False,
        'has_use_cases': False,
        'has_workflow': False,
        'has_examples': False,
        'has_error_handling': False,
        'has_dependencies': False,
        'has_faq': False,
        'has_limitations': False,
        'frontmatter_valid': False,
        'description_length': 0,
        'body_line_count': 0,
        'has_hardcoded_keys': False,
        'has_exaggeration': False,
        'has_reserved_words': False,
        'issues': []
    }
    
    if not skill_content:
        checks['issues'].append('SKILL.md内容为空')
        return checks
    
    # 解析frontmatter
    if skill_content.startswith('---'):
        parts = re.split(r'^---\s*$', skill_content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2]
            checks['has_frontmatter'] = True
            checks['frontmatter_valid'] = True
            
            checks['has_displayName'] = bool(re.search(r'^displayName:', fm, re.MULTILINE))
            checks['has_summary'] = bool(re.search(r'^summary:', fm, re.MULTILINE))
            checks['has_license'] = bool(re.search(r'^license:', fm, re.MULTILINE))
            checks['has_tools'] = bool(re.search(r'^tools:', fm, re.MULTILINE))
            
            # description长度
            desc_match = re.search(r'description:\s*\|-\s*\n((?:\s+.+\n?)+)', fm)
            if desc_match:
                desc_text = desc_match.group(1).strip()
                checks['description_length'] = len(desc_text)
                checks['has_description'] = True
            else:
                desc_match = re.search(r'description:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
                if desc_match:
                    checks['description_length'] = len(desc_match.group(1).strip())
                    checks['has_description'] = True
            
            # 检查硬编码凭证（排除代码块）
            fm_no_code = re.sub(r'```[\s\S]*?```', '', fm)
            key_patterns = [
                r'sk-[a-zA-Z0-9]{20,}',
                r'AKIA[A-Z0-9]{16}',
                r'ghp_[a-zA-Z0-9]{36}',
            ]
            for pattern in key_patterns:
                if re.search(pattern, fm_no_code):
                    checks['has_hardcoded_keys'] = True
                    checks['issues'].append('frontmatter含硬编码凭证')
                    break
            
            # 检查保留词
            for field in ['displayName', 'summary']:
                match = re.search(rf'^{field}:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
                if match:
                    value = match.group(1).lower()
                    for word in ['claude', 'anthropic', 'openai', 'chatgpt']:
                        if re.search(rf'\b{word}\b', value):
                            checks['has_reserved_words'] = True
                            checks['issues'].append(f'{field}含保留词{word}')
                            break
            
            # 检查夸大词
            for field in ['displayName', 'summary']:
                match = re.search(rf'^{field}:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
                if match:
                    for word in ['万能', '超级', '最强', '最好', '最佳', '终极', '完美', '第一', '顶级', '极致']:
                        if word in match.group(1):
                            checks['has_exaggeration'] = True
                            checks['issues'].append(f'{field}含夸大词{word}')
                            break
        else:
            checks['issues'].append('frontmatter格式错误')
    else:
        body = skill_content
        checks['issues'].append('缺少frontmatter')
    
    # 检查正文章节
    checks['has_core_capability'] = any(kw in body for kw in ['核心能力', '核心功能', '## 功能'])
    checks['has_use_cases'] = any(kw in body for kw in ['适用场景', '使用场景', '## 场景'])
    checks['has_workflow'] = any(kw in body for kw in ['使用流程', '工作流程', '## Step', '### Step', '## 步骤', '快速开始', '快速上手'])
    checks['has_examples'] = any(kw in body for kw in ['示例', 'Example', '## 示例', '输入', '输出'])
    checks['has_error_handling'] = any(kw in body for kw in ['错误处理', '异常处理', 'Error Handling', '故障排查', '错误码'])
    checks['has_dependencies'] = any(kw in body for kw in ['依赖说明', '## 依赖', 'Dependencies', 'API Key', 'LLM'])
    checks['has_faq'] = any(kw in body for kw in ['常见问题', 'FAQ', 'Q:', 'A:'])
    checks['has_limitations'] = any(kw in body for kw in ['已知限制', '限制说明', 'Limitations', '不适用'])
    
    checks['body_line_count'] = len([l for l in body.split('\n') if l.strip()])
    
    # 缺失章节
    missing = []
    if not checks['has_core_capability']: missing.append('核心能力')
    if not checks['has_use_cases']: missing.append('适用场景')
    if not checks['has_workflow']: missing.append('使用流程')
    if not checks['has_examples']: missing.append('示例')
    if not checks['has_error_handling']: missing.append('错误处理')
    if not checks['has_dependencies']: missing.append('依赖说明')
    if not checks['has_faq']: missing.append('常见问题')
    if missing:
        checks['issues'].append(f'缺失章节: {", ".join(missing)}')
    
    return checks

def calculate_static_scores(checks):
    """根据静态检查计算T和C维度的基础分"""
    # Trust基础分 (0-10)
    trust = 0
    if checks['has_frontmatter']: trust += 1.5
    if checks['frontmatter_valid']: trust += 1.5
    if checks['has_license']: trust += 1.5
    if checks['has_tools']: trust += 1.5
    if not checks['has_hardcoded_keys']: trust += 1.5
    if not checks['has_reserved_words']: trust += 1.5
    if not checks['has_exaggeration']: trust += 1.0
    trust = min(10, trust)
    
    # Convention基础分 (0-10)
    section_count = sum([
        checks['has_core_capability'], checks['has_use_cases'],
        checks['has_workflow'], checks['has_examples'],
        checks['has_error_handling'], checks['has_dependencies'],
        checks['has_faq'], checks['has_limitations']
    ])
    convention = min(8, section_count * 1.0)  # 8个章节满分8
    if checks['has_displayName']: convention += 0.5
    if checks['has_summary']: convention += 0.5
    if checks['has_description']: convention += 0.5
    if 50 <= checks['description_length'] <= 300: convention += 0.5
    convention = min(10, convention)
    
    return {
        'trust_static': round(trust, 1),
        'convention_static': round(convention, 1)
    }

def save_trace_score(skill_id, checks, static_scores, llm_result=None):
    """保存TRACE评分到数据库
    
    修复U-01：使用TRACE_FIELD_MAPPING保证字段语义正确
    修复U-23：使用TRACE_PASS_THRESHOLD统一阈值（原为硬编码40）
    
    字段映射说明（scores表字段名与TRACE维度名不一致）：
    - trust → debranding_score
    - reliability → quality_score
    - adaptability → practicality_score
    - convention → simplicity_score
    - effectiveness → performance_score
    - differentiation_score: 存effectiveness副本（差异化维度）
    - compliance_score: 存trust副本（合规维度）
    """
    conn = get_db()
    c = conn.cursor()
    now = datetime.now().isoformat()
    
    if llm_result:
        # 合并静态分和LLM分
        trace = llm_result.get('trace_scores', {})
        trust_score = max(static_scores['trust_static'], trace.get('trust', {}).get('score', 0))
        reliability_score = trace.get('reliability', {}).get('score', 0)
        adaptability_score = trace.get('adaptability', {}).get('score', 0)
        convention_score = max(static_scores['convention_static'], trace.get('convention', {}).get('score', 0))
        effectiveness_score = trace.get('effectiveness', {}).get('score', 0)
        total = round(trust_score + reliability_score + adaptability_score + convention_score + effectiveness_score, 1)
        grade = llm_result.get('quality_grade', 'D')
        notes = json.dumps({
            'issues': checks['issues'],
            'top_3': llm_result.get('top_3_issues', []),
            'suggestions': {k: v.get('suggestion', '') for k, v in trace.items()},
            'static_scores': static_scores,
            'llm_scores': {k: v.get('score', 0) for k, v in trace.items()},
            'evaluated_at': now,
            'field_mapping': TRACE_FIELD_MAPPING,
        }, ensure_ascii=False)
        is_pass = 1 if total >= TRACE_PASS_THRESHOLD else 0
    else:
        # 仅静态评分
        trust_score = static_scores['trust_static']
        reliability_score = 0
        adaptability_score = 0
        convention_score = static_scores['convention_static']
        effectiveness_score = 0
        total = round(trust_score + convention_score, 1)
        grade = 'D'
        notes = json.dumps({
            'issues': checks['issues'],
            'static_only': True,
            'static_scores': static_scores,
            'message': 'R/A/E维度需要LLM评估',
            'field_mapping': TRACE_FIELD_MAPPING,
        }, ensure_ascii=False)
        is_pass = 0
    
    # 使用映射常量写入，语义清晰可追溯
    # differentiation_score 存 effectiveness 副本，compliance_score 存 trust 副本
    differentiation_val = effectiveness_score
    compliance_val = trust_score
    
    # 检查是否已有trace评分
    c.execute(f"SELECT id FROM scores WHERE skill_id = ? AND score_type = '{SCORE_TYPE_TRACE_LLM}'", (skill_id,))
    existing = c.fetchone()
    
    if existing:
        c.execute("""
            UPDATE scores SET
                total_score = ?, quality_score = ?, practicality_score = ?,
                simplicity_score = ?, performance_score = ?, debranding_score = ?,
                differentiation_score = ?, compliance_score = ?, cost_score = 0,
                scored_at = ?, reviewer = ?, notes = ?, is_pass = ?
            WHERE id = ?
        """, (total, reliability_score, adaptability_score,
              convention_score, effectiveness_score, trust_score,
              differentiation_val, compliance_val,
              now, 'trace_llm_scorer_v2', notes, is_pass, existing['id']))
    else:
        c.execute(f"""
            INSERT INTO scores (skill_id, score_type, total_score,
                quality_score, practicality_score, simplicity_score,
                performance_score, debranding_score, differentiation_score,
                compliance_score, cost_score, scored_at, reviewer, notes, is_pass, pass_threshold)
            VALUES (?, '{SCORE_TYPE_TRACE_LLM}', ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?, ?, ?, ?)
        """, (skill_id, total, reliability_score, adaptability_score,
              convention_score, effectiveness_score, trust_score,
              differentiation_val, compliance_val,
              now, 'trace_llm_scorer_v2', notes, is_pass, TRACE_PASS_THRESHOLD))
    
    conn.commit()
    conn.close()
    
    return {
        'total': total, 'grade': grade,
        'trust': trust_score, 'reliability': reliability_score,
        'adaptability': adaptability_score, 'convention': convention_score,
        'effectiveness': effectiveness_score,
        'is_llm_evaluated': llm_result is not None
    }


# ============================================================
# L2低分标注机制 (Round 09 Step 5.4优化项3)
# ============================================================

def annotate_low_score_skills(limit: int = None) -> List[Dict[str, Any]]:
    """
    扫描L2评分低于L2_MANUAL_REVIEW_THRESHOLD的skill, 标注需AI手动优化的章节。

    标注规则:
    - 总分 < L2_PASS_THRESHOLD(35): 标记为"需重新生成"
    - 总分 < L2_MANUAL_REVIEW_THRESHOLD(40): 标记为"需AI手动优化"
    - 总分 >= L2_EXCELLENT_THRESHOLD(45): 标记为"优秀, 可跳过优化"

    对需优化的skill, 基于TRACE维度得分识别薄弱章节:
    - T < 7: 依赖说明/frontmatter需优化
    - R < 7: 异常处理章节需优化
    - A < 7: 适用场景/description需优化
    - C < 7: 章节完整性需优化
    - E < 7: 案例展示/输出格式需优化

    参数:
    - limit: 最多处理多少个skill (None=全部)

    返回: 标注结果列表
    """
    conn = get_db()
    c = conn.cursor()

    # 查询低于L2_MANUAL_REVIEW_THRESHOLD的skill
    query = """
        SELECT s.id, s.slug, s.local_path,
               sc.total_score, sc.quality_score, sc.practicality_score,
               sc.simplicity_score, sc.performance_score, sc.debranding_score,
               sc.notes
        FROM scores sc
        JOIN skills s ON sc.skill_id = s.id
        WHERE sc.score_type = 'trace_llm'
          AND sc.total_score < ?
        ORDER BY sc.total_score ASC
    """
    params = (L2_MANUAL_REVIEW_THRESHOLD,)
    if limit:
        query += " LIMIT ?"
        params = (L2_MANUAL_REVIEW_THRESHOLD, limit)

    c.execute(query, params)
    rows = c.fetchall()

    annotations = []
    for row in rows:
        slug = row['slug']
        total = row['total_score']

        # 确定优化级别
        if total < L2_PASS_THRESHOLD:
            action = 'regenerate'
            action_label = '需重新生成'
        else:
            action = 'manual_optimize'
            action_label = '需AI手动优化'

        # 识别薄弱维度和对应章节
        weak_chapters = []
        dimension_chapter_map = {
            'T': ('debranding_score', '依赖说明/frontmatter', '检查frontmatter完整性和依赖配置'),
            'R': ('quality_score', '异常处理', '补充边界输入处理和错误恢复方案'),
            'A': ('practicality_score', '适用场景/description', '优化description精准度和场景描述'),
            'C': ('simplicity_score', '章节完整性', '补全缺失的标准8章节'),
            'E': ('performance_score', '案例展示/输出格式', '增加真实可用的示例和输出模板'),
        }

        for dim, (field, chapter, suggestion) in dimension_chapter_map.items():
            score = row[field]
            if score is not None and score < 7:
                weak_chapters.append({
                    'dimension': dim,
                    'score': score,
                    'chapter': chapter,
                    'suggestion': suggestion,
                })

        annotation = {
            'slug': slug,
            'skill_id': row['id'],
            'l2_total': total,
            'action': action,
            'action_label': action_label,
            'weak_chapters': weak_chapters,
            'scores': {
                'T': row['debranding_score'],
                'R': row['quality_score'],
                'A': row['practicality_score'],
                'C': row['simplicity_score'],
                'E': row['performance_score'],
            }
        }
        annotations.append(annotation)

    conn.close()
    return annotations


def print_low_score_annotations(annotations: List[Dict[str, Any]]):
    """打印低分标注报告"""
    if not annotations:
        print("  ✓ 无需优化的skill (所有skill L2评分≥{})".format(L2_MANUAL_REVIEW_THRESHOLD))
        return

    print(f"  发现 {len(annotations)} 个需优化的skill:")
    print(f"  {'slug':40s} | L2分 | 操作       | 薄弱章节")
    print(f"  " + "-" * 85)

    for a in annotations:
        weak_str = ', '.join(f"{w['dimension']}({w['score']}):{w['chapter']}" for w in a['weak_chapters'])
        if not weak_str:
            weak_str = '-'
        print(f"  {a['slug']:40s} | {a['l2_total']:4.1f} | {a['action_label']:10s} | {weak_str}")


def cmd_static(args):
    """静态评分（全部skill或packaged）"""
    packaged = '--packaged' in args
    limit = None
    for i, a in enumerate(args):
        if a == '--limit' and i+1 < len(args):
            limit = int(args[i+1])
    
    skills = get_all_skills(limit=limit, packaged_only=packaged)
    print(f"待评估skill数: {len(skills)}")
    
    results = []
    for i, skill in enumerate(skills):
        content = read_skill_md(skill.get('local_path'))
        checks = static_check(content)
        static_scores = calculate_static_scores(checks)
        result = save_trace_score(skill['id'], checks, static_scores)
        result['slug'] = skill['slug']
        results.append(result)
        
        if (i + 1) % 200 == 0:
            print(f"  已评估 {i+1}/{len(skills)}")
    
    # 汇总
    graded = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for r in results:
        graded[r['grade']] = graded.get(r['grade'], 0) + 1
    
    avg = sum(r['total'] for r in results) / len(results) if results else 0
    print(f"\n静态评分完成:")
    print(f"  A: {graded.get('A', 0)}, B: {graded.get('B', 0)}, C: {graded.get('C', 0)}, D: {graded.get('D', 0)}")
    print(f"  平均分: {avg:.1f}/50 (仅T+C维度)")

def cmd_export(args):
    """导出skill供LLM评估"""
    packaged = '--packaged' in args
    limit = None
    for i, a in enumerate(args):
        if a == '--limit' and i+1 < len(args):
            limit = int(args[i+1])
    
    skills = get_all_skills(limit=limit, packaged_only=packaged)
    print(f"导出 {len(skills)} 个skill供LLM评估...")
    
    export_data = []
    for skill in skills:
        content = read_skill_md(skill.get('local_path'))
        if content:
            # 截取前2500字符避免过长
            truncated = content[:2500] + ('...(截断)' if len(content) > 2500 else '')
            checks = static_check(content)
            static_scores = calculate_static_scores(checks)
            
            export_data.append({
                'id': skill['id'],
                'slug': skill['slug'],
                'display_name': skill.get('current_display_name', ''),
                'source': skill.get('source', ''),
                'edition': skill.get('edition', ''),
                'content': truncated,
                'static_scores': static_scores,
                'static_issues': checks['issues']
            })
    
    # 按批次保存（每批20个）
    batch_size = 20
    for i in range(0, len(export_data), batch_size):
        batch = export_data[i:i+batch_size]
        batch_num = i // batch_size + 1
        output_path = EXPORT_DIR / f"trace_eval_batch_{batch_num}.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(batch, f, ensure_ascii=False, indent=2)
        print(f"  批次 {batch_num}: {len(batch)} skills → {output_path}")
    
    # 保存汇总文件
    summary_path = EXPORT_DIR / "trace_eval_summary.json"
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump({
            'total_skills': len(export_data),
            'total_batches': (len(export_data) + batch_size - 1) // batch_size,
            'batch_size': batch_size,
            'exported_at': datetime.now().isoformat()
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n共导出 {len(export_data)} skills, {(len(export_data)+batch_size-1)//batch_size} 个批次")

def cmd_import(args):
    """导入LLM评估结果"""
    if not args:
        print("用法: python trace_llm_scorer.py import <results.json>")
        return
    
    results_file = Path(args[0])
    if not results_file.exists():
        print(f"文件不存在: {results_file}")
        return
    
    with open(results_file, 'r', encoding='utf-8') as f:
        results = json.load(f)
    
    # 支持单个结果或结果列表
    if isinstance(results, dict):
        results = [results]
    
    print(f"导入 {len(results)} 个LLM评估结果...")
    
    conn = get_db()
    c = conn.cursor()
    
    imported = 0
    for result in results:
        slug = result.get('slug')
        if not slug:
            continue
        
        # 查找skill
        c.execute("SELECT id, local_path FROM skills WHERE slug = ? AND workflow_state != 'deprecated'", (slug,))
        row = c.fetchone()
        if not row:
            print(f"  [SKIP] {slug}: skill不存在")
            continue
        
        skill_id = row['id']
        
        # 读取内容进行静态检查
        content = read_skill_md(row['local_path'])
        checks = static_check(content)
        static_scores = calculate_static_scores(checks)
        
        # 保存合并评分
        save_trace_score(skill_id, checks, static_scores, result)
        imported += 1
        print(f"  [OK] {slug}: {result.get('total_score', 0)}/50 ({result.get('quality_grade', 'D')})")
    
    conn.close()
    print(f"\n导入完成: {imported}/{len(results)}")

def cmd_report(args):
    """生成评分报告"""
    packaged = '--packaged' in args
    
    conn = get_db()
    c = conn.cursor()
    
    if packaged:
        # 获取60个packaged skill的评分
        packaged_slugs = []
        skillhub_dir = Path(r"d:\skills\packaged-skills\skillhub")
        if skillhub_dir.exists():
            for d in sorted(skillhub_dir.iterdir()):
                if d.is_dir():
                    packaged_slugs.append(d.name)
        opensource_dir = Path(r"d:\skills\opensource-skills\packaged")
        if opensource_dir.exists():
            for d in sorted(opensource_dir.iterdir()):
                if d.is_dir():
                    packaged_slugs.append(d.name)
        
        placeholders = ','.join('?' * len(packaged_slugs))
        c.execute(f"""
            SELECT s.slug, s.current_display_name, s.source, s.edition,
                   sc.total_score, sc.debranding_score AS trust,
                   sc.quality_score AS reliability, sc.practicality_score AS adaptability,
                   sc.simplicity_score AS convention, sc.performance_score AS effectiveness,
                   sc.is_pass, sc.notes
            FROM skills s
            LEFT JOIN scores sc ON s.id = sc.skill_id AND sc.score_type = 'trace_llm'
            WHERE s.slug IN ({placeholders})
            ORDER BY CASE WHEN sc.total_score IS NULL THEN 1 ELSE 0 END, sc.total_score DESC
        """, packaged_slugs)
    else:
        c.execute("""
            SELECT s.slug, s.current_display_name, s.source, s.edition,
                   sc.total_score, sc.debranding_score AS trust,
                   sc.quality_score AS reliability, sc.practicality_score AS adaptability,
                   sc.simplicity_score AS convention, sc.performance_score AS effectiveness,
                   sc.is_pass, sc.notes
            FROM skills s
            LEFT JOIN scores sc ON s.id = sc.skill_id AND sc.score_type = 'trace_llm'
            WHERE s.workflow_state != 'deprecated'
            ORDER BY CASE WHEN sc.total_score IS NULL THEN 1 ELSE 0 END, sc.total_score DESC
        """)
    
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    
    scope = "Packaged Skills" if packaged else "全部Skills"
    print(f"\n{'='*90}")
    print(f"TRACE评分报告 - {scope}")
    print(f"{'='*90}")
    print(f"总计: {len(results)}个skill")
    
    graded = [r for r in results if r['total_score'] is not None]
    not_graded = [r for r in results if r['total_score'] is None]
    
    if graded:
        avg = sum(r['total_score'] for r in graded) / len(graded)
        llm_evaluated = sum(1 for r in graded if r['reliability'] and r['reliability'] > 0)
        static_only = len(graded) - llm_evaluated
        
        print(f"\n已评分: {len(graded)}/{len(results)}")
        print(f"  LLM评估: {llm_evaluated}个")
        print(f"  仅静态: {static_only}个")
        print(f"  未评分: {len(not_graded)}个")
        print(f"  平均分: {avg:.1f}/50")
        
        # 等级分布
        grades = {'A (45-50)': 0, 'B (40-44)': 0, 'C (30-39)': 0, 'D (<30)': 0}
        for r in graded:
            score = r['total_score']
            if score >= 45: grades['A (45-50)'] += 1
            elif score >= 40: grades['B (40-44)'] += 1
            elif score >= 30: grades['C (30-39)'] += 1
            else: grades['D (<30)'] += 1
        
        print(f"\n等级分布:")
        for grade, count in grades.items():
            pct = count/len(graded)*100 if graded else 0
            bar = '█' * int(pct/2)
            print(f"  {grade}: {count:>4} ({pct:.1f}%) {bar}")
        
        # 五维度均分
        if llm_evaluated > 0:
            llm_graded = [r for r in graded if r['reliability'] and r['reliability'] > 0]
            dims = {
                'T (Trust)': sum(r['trust'] or 0 for r in llm_graded) / len(llm_graded),
                'R (Reliability)': sum(r['reliability'] or 0 for r in llm_graded) / len(llm_graded),
                'A (Adaptability)': sum(r['adaptability'] or 0 for r in llm_graded) / len(llm_graded),
                'C (Convention)': sum(r['convention'] or 0 for r in llm_graded) / len(llm_graded),
                'E (Effectiveness)': sum(r['effectiveness'] or 0 for r in llm_graded) / len(llm_graded),
            }
            print(f"\n五维度均分(LLM评估的{llm_evaluated}个):")
            for dim, score in dims.items():
                bar = '█' * int(score)
                print(f"  {dim:<25} {score:.1f}/10 {bar}")
        
        # Top 15
        print(f"\nTop 15:")
        for r in graded[:15]:
            llm_tag = " [LLM]" if r['reliability'] and r['reliability'] > 0 else " [静态]"
            print(f"  {r['slug']:<40} {r['total_score']:>5.1f}/50{llm_tag}  {r['current_display_name'] or ''}")
        
        # Bottom 15
        if len(graded) > 15:
            print(f"\nBottom 15:")
            for r in graded[-15:]:
                llm_tag = " [LLM]" if r['reliability'] and r['reliability'] > 0 else " [静态]"
                print(f"  {r['slug']:<40} {r['total_score']:>5.1f}/50{llm_tag}  {r['current_display_name'] or ''}")
    
    # 保存报告到JSON
    report_path = DATA_DIR / "reports" / "trace_evaluation_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'scope': scope,
            'total': len(results),
            'graded': len(graded),
            'not_graded': len(not_graded),
            'results': [{k: v for k, v in r.items() if v is not None} for r in results]
        }, f, ensure_ascii=False, indent=2)
    print(f"\n报告保存到: {report_path}")

def cmd_annotate(args):
    """低分标注 - 扫描L2低分skill并标注需优化的章节"""
    import argparse
    parser = argparse.ArgumentParser(description='L2低分标注')
    parser.add_argument('--limit', type=int, help='最多处理数量')
    parser.add_argument('--json', action='store_true', help='JSON格式输出')
    parsed = parser.parse_args(args)

    annotations = annotate_low_score_skills(limit=parsed.limit)

    if parsed.json:
        print(json.dumps(annotations, ensure_ascii=False, indent=2))
    else:
        print(f"\n{'='*70}")
        print(f"L2低分标注报告 (阈值<{L2_MANUAL_REVIEW_THRESHOLD})")
        print(f"{'='*70}")
        print_low_score_annotations(annotations)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    cmd = sys.argv[1]
    args = sys.argv[2:]
    
    if cmd == 'static':
        cmd_static(args)
    elif cmd == 'export':
        cmd_export(args)
    elif cmd == 'import':
        cmd_import(args)
    elif cmd == 'report':
        cmd_report(args)
    elif cmd == 'annotate':
        cmd_annotate(args)
    else:
        print(f"未知命令: {cmd}")
        print(__doc__)

if __name__ == '__main__':
    main()
