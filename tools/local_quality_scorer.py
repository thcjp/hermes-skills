#!/usr/bin/env python3
"""
本地LLM质量评分器 (v1.1)
========================
5维度评测SKILL.md质量，产出0.0-5.0分数。

评测维度（对齐SkillHub平台AI评测维度）:
  1. 功能完整性 (completeness)
  2. 准确性 (accuracy)
  3. 易用性 (usability)
  4. 安全性 (security)
  5. 创新性 (innovation)

阈值: 4.5（与 quality_gate.py 的 RATING_GATE_THRESHOLD 一致）

Usage:
  python local_quality_scorer.py <skill_dir_or_path>     # 评分单个skill
  python local_quality_scorer.py <skill_dir> --json       # JSON输出
  python local_quality_scorer.py --test                   # 自检
  python local_quality_scorer.py scan-all                 # 批量扫描全部skill
  python local_quality_scorer.py scan-all --dir <path>    # 扫描指定目录
  python local_quality_scorer.py scan-all --force         # 强制重新扫描
  python local_quality_scorer.py scan-all --limit 50      # 限制扫描数量
"""

import json
import os
import sys
import re
import time
import sqlite3
from pathlib import Path
from datetime import datetime

import requests

# ============ 配置加载 ============

CONFIG_PATH = Path(__file__).resolve().parent.parent / "data" / "config" / "quality_scoring_config.json"

SCORE_THRESHOLD = 4.5  # 与 quality_gate.py RATING_GATE_THRESHOLD 一致


def _load_config():
    """加载评分器配置"""
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"评分器配置文件不存在: {CONFIG_PATH}")
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _get_api_key(config):
    """从环境变量获取API密钥"""
    env_var = config.get("llm", {}).get("api_key_env", "DEEPSEEK_API_KEY")
    api_key = os.environ.get(env_var, "")
    if not api_key:
        # 尝试备选环境变量
        for fallback_env in ["SILICONFLOW_API_KEY", "ZHIPU_API_KEY", "OPENAI_API_KEY"]:
            api_key = os.environ.get(fallback_env, "")
            if api_key:
                return api_key
    return api_key


# ============ 核心评分逻辑 ============


def score_skill(skill_input):
    """
    对SKILL.md评分。

    参数:
        skill_input: SKILL.md文件路径(Path/str) 或 目录路径 或 文件内容字符串

    返回:
        {
            "total_score": float,       # 0.0-5.0
            "dimensions": {             # 每维度详情
                "completeness": {"score": float, "reason": str},
                "accuracy": {"score": float, "reason": str},
                "usability": {"score": float, "reason": str},
                "security": {"score": float, "reason": str},
                "innovation": {"score": float, "reason": str},
            },
            "feedback": str,            # 改进建议汇总
            "passed": bool,             # total_score >= 4.5
            "scored_at": str,           # ISO时间戳
        }
    """
    # 1. 读取SKILL.md内容
    skill_content, skill_path = _resolve_skill_input(skill_input)
    if not skill_content:
        return _error_result("无法读取SKILL.md内容")

    # 2. 截断过长的内容（避免超出LLM token限制）
    # GLM-4-Flash支持128K上下文,30000字符约15000tokens,足够覆盖完整SKILL.md(含代码示例和架构分析)
    max_chars = 30000
    if len(skill_content) > max_chars:
        skill_content = skill_content[:max_chars] + "\n... (内容已截断)"

    # 3. 加载配置
    try:
        config = _load_config()
    except FileNotFoundError as e:
        return _error_result(str(e))

    # 4. 获取API密钥
    api_key = _get_api_key(config)
    if not api_key:
        return _error_result(
            "未找到LLM API密钥，请设置环境变量 DEEPSEEK_API_KEY / SILICONFLOW_API_KEY / ZHIPU_API_KEY"
        )

    # 5. 构造评测prompt
    prompt = _build_eval_prompt(skill_content, config)

    # 6. 调用LLM API
    llm_response = _call_llm(prompt, config, api_key)
    if "error" in llm_response:
        return _error_result(llm_response["error"])

    # 7. 解析LLM返回
    parsed = _parse_llm_response(llm_response["content"])
    if "error" in parsed:
        return _error_result(parsed["error"])

    # 8. 构造标准结果
    dimensions = parsed["dimensions"]
    total_score = round(sum(d["score"] for d in dimensions.values()), 2)
    suggestions = parsed.get("suggestions", [])

    feedback_parts = []
    for dim_key, dim_val in dimensions.items():
        if dim_val["score"] < 0.9:
            feedback_parts.append(f"[{dim_key}] {dim_val['reason']}")
    if suggestions:
        feedback_parts.append("改进建议: " + "; ".join(suggestions))

    return {
        "total_score": total_score,
        "dimensions": dimensions,
        "feedback": " | ".join(feedback_parts) if feedback_parts else "各维度均达标",
        "passed": total_score >= SCORE_THRESHOLD,
        "skill_path": skill_path,
        "scored_at": datetime.now().isoformat(),
    }


def _resolve_skill_input(skill_input):
    """解析输入，返回(content, path)"""
    if isinstance(skill_input, Path):
        skill_input = str(skill_input)

    if isinstance(skill_input, str):
        # 判断是路径还是内容
        if "\n" in skill_input or len(skill_input) > 500:
            # 多行或长文本 → 当作内容
            return skill_input, None

        # 尝试当作路径
        p = Path(skill_input)
        if p.is_dir():
            skill_md = p / "SKILL.md"
            if skill_md.exists():
                return skill_md.read_text(encoding="utf-8"), str(skill_md)
            return None, None
        if p.is_file():
            return p.read_text(encoding="utf-8"), str(p)

    return None, None


def _build_eval_prompt(skill_content, config):
    """构造评测prompt"""
    template = config.get("prompt_template", "")
    dims = config.get("dimensions", [])

    replacements = {"skill_content": skill_content}
    for d in dims:
        replacements[f"{d['key']}_desc"] = d.get("description", "")

    # 安全替换（避免 KeyError）
    prompt = template
    for key, val in replacements.items():
        prompt = prompt.replace("{" + key + "}", val)

    return prompt


def _call_llm(prompt, config, api_key):
    """调用LLM API（OpenAI兼容格式）"""
    llm_config = config.get("llm", {})
    endpoint = llm_config.get("api_endpoint", "https://api.deepseek.com/v1/chat/completions")
    model = llm_config.get("model", "deepseek-chat")
    max_tokens = llm_config.get("max_tokens", 2000)
    temperature = llm_config.get("temperature", 0.3)
    timeout = llm_config.get("timeout", 30)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是一个专业的SKILL质量评测专家，请严格按照JSON格式返回评测结果。"},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

    try:
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        return {"content": content}
    except requests.exceptions.Timeout:
        return {"error": f"LLM API请求超时({timeout}s)"}
    except requests.exceptions.ConnectionError as e:
        return {"error": f"LLM API连接失败: {e}"}
    except requests.exceptions.HTTPError as e:
        return {"error": f"LLM API HTTP错误: {e}"}
    except (KeyError, IndexError) as e:
        return {"error": f"LLM API返回格式异常: {e}"}
    except Exception as e:
        return {"error": f"LLM API调用异常: {e}"}


def _parse_llm_response(content):
    """解析LLM返回的JSON"""
    # 尝试从markdown代码块中提取JSON
    json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", content, re.DOTALL)
    if json_match:
        content = json_match.group(1)

    # 尝试直接解析JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        # 尝试找到第一个{和最后一个}
        start = content.find("{")
        end = content.rfind("}")
        if start != -1 and end != -1:
            try:
                data = json.loads(content[start : end + 1])
            except json.JSONDecodeError as e:
                return {"error": f"无法解析LLM返回为JSON: {e}"}
        else:
            return {"error": "LLM返回中未找到JSON结构"}

    # 验证结构
    dimensions = data.get("dimensions", {})
    required_dims = ["completeness", "accuracy", "usability", "security", "innovation"]

    normalized_dims = {}
    for dim_key in required_dims:
        dim_data = dimensions.get(dim_key, {})
        if isinstance(dim_data, dict):
            score = float(dim_data.get("score", 0.0))
            score = max(0.0, min(1.0, score))  # 限制在0-1范围
            reason = dim_data.get("reason", "")
        elif isinstance(dim_data, (int, float)):
            score = max(0.0, min(1.0, float(dim_data)))
            reason = ""
        else:
            score = 0.0
            reason = ""
        normalized_dims[dim_key] = {"score": round(score, 2), "reason": reason}

    suggestions = data.get("suggestions", [])
    if not isinstance(suggestions, list):
        suggestions = [str(suggestions)]

    return {"dimensions": normalized_dims, "suggestions": suggestions}


def _error_result(error_msg):
    """构造错误返回（非mock，报告真实错误）"""
    return {
        "total_score": 0.0,
        "dimensions": {},
        "feedback": f"评分失败: {error_msg}",
        "passed": False,
        "error": error_msg,
        "scored_at": datetime.now().isoformat(),
    }


# ============ 批量扫描 (T1-005) ============

# 项目根目录
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_DB_PATH = str(_PROJECT_ROOT / "skill-registry.db")

# 默认扫描目录
_DEFAULT_SCAN_DIRS = [
    _PROJECT_ROOT / "packaged-skills" / "skillhub",
    _PROJECT_ROOT / "opensource-skills" / "packaged",
    _PROJECT_ROOT / "differentiated-skills",
    _PROJECT_ROOT / "clawhub-skills",
    _PROJECT_ROOT / "enterprise-upload",
]


def _extract_slug_from_skill_md(skill_md_path):
    """从SKILL.md的frontmatter中提取slug"""
    try:
        content = skill_md_path.read_text(encoding="utf-8")
        if content.startswith("\ufeff"):
            content = content[1:]
        if content.startswith("---"):
            parts = re.split(r"^---\s*$", content, maxsplit=2, flags=re.MULTILINE)
            if len(parts) >= 3:
                fm = parts[1]
                m = re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
                if m:
                    return m.group(1).strip()
    except Exception:
        pass
    return None


def _get_db_connection():
    """获取DB连接"""
    conn = sqlite3.connect(_DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _get_scored_slugs(conn):
    """获取已有本地评分的slug集合（断点续扫）"""
    c = conn.cursor()
    c.execute("SELECT slug FROM skills WHERE local_quality_score > 0")
    return {row["slug"] for row in c.fetchall()}


def _write_score_to_db(conn, slug, score, feedback, dimensions):
    """将评分写入DB"""
    c = conn.cursor()
    now = datetime.now().isoformat()

    # 构造feedback摘要（截断到500字符避免DB字段过长）
    feedback_short = feedback[:500] if feedback else ""

    # 构造dimensions JSON
    dims_json = json.dumps(dimensions, ensure_ascii=False) if dimensions else "{}"

    c.execute("""
        UPDATE skills
        SET local_quality_score = ?,
            local_score_feedback = ?,
            local_score_at = ?,
            updated_at = ?
        WHERE slug = ?
    """, (score, feedback_short, now, now, slug))

    return c.rowcount > 0


def _generate_scan_report(conn, scan_results):
    """生成全量质量评分报告 (T1-007)"""
    report_dir = _PROJECT_ROOT / "data" / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / "local_quality_scan.json"

    # 从DB读取全部评分数据
    c = conn.cursor()
    c.execute("""
        SELECT slug, local_quality_score, local_score_feedback, local_score_at
        FROM skills
        WHERE local_quality_score > 0
        ORDER BY local_quality_score ASC
    """)
    db_rows = c.fetchall()

    if not db_rows:
        print("[WARN] DB中无评分数据，跳过报告生成")
        return None

    scores = [row["local_quality_score"] for row in db_rows]
    avg_score = sum(scores) / len(scores) if scores else 0

    # 评分分布
    dist = {"0.0-2.0": 0, "2.0-3.0": 0, "3.0-3.5": 0, "3.5-4.0": 0, "4.0-4.5": 0, "4.5-5.0": 0}
    for s in scores:
        if s < 2.0:
            dist["0.0-2.0"] += 1
        elif s < 3.0:
            dist["2.0-3.0"] += 1
        elif s < 3.5:
            dist["3.0-3.5"] += 1
        elif s < 4.0:
            dist["3.5-4.0"] += 1
        elif s < 4.5:
            dist["4.0-4.5"] += 1
        else:
            dist["4.5-5.0"] += 1

    low_score_skills = []
    for row in db_rows:
        if row["local_quality_score"] <= SCORE_THRESHOLD:
            # 从feedback中提取最弱维度
            feedback = row["local_score_feedback"] or ""
            weakest = ""
            for dim in ["innovation", "usability", "completeness", "security", "accuracy"]:
                if f"[{dim}]" in feedback:
                    weakest = dim
                    break
            low_score_skills.append({
                "slug": row["slug"],
                "score": round(row["local_quality_score"], 2),
                "weakest_dim": weakest,
                "feedback": feedback[:200],
            })

    report = {
        "scan_at": datetime.now().isoformat(),
        "total_scored": len(db_rows),
        "score_distribution": dist,
        "low_score_count": len(low_score_skills),
        "passed_count": len(db_rows) - len(low_score_skills),
        "avg_score": round(avg_score, 2),
        "low_score_skills": low_score_skills,
        "scan_errors": [r for r in scan_results if r.get("error")],
    }

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\n报告已生成: {report_path}")
    print(f"  总评分数: {len(db_rows)}")
    print(f"  通过(>4.5): {len(db_rows) - len(low_score_skills)}")
    print(f"  未通过(<=4.5): {len(low_score_skills)}")
    print(f"  平均分: {avg_score:.2f}")
    print(f"  评分分布: {dist}")

    return report_path


def _score_one_skill(args):
    """线程池worker: 评分单个skill，返回结果dict（不写DB）"""
    slug, skill_md_path = args
    try:
        result = score_skill(skill_md_path)
        if result.get("error"):
            return {"slug": slug, "error": result["error"]}
        return {
            "slug": slug,
            "score": result["total_score"],
            "feedback": result.get("feedback", ""),
            "dimensions": result.get("dimensions", {}),
            "passed": result.get("passed", False),
        }
    except Exception as e:
        return {"slug": slug, "error": str(e)}


def scan_all(dirs=None, force=False, limit=None):
    """
    批量扫描所有skill，评分并写入DB（并行版，5线程）。

    参数:
        dirs: 要扫描的目录列表（默认packaged-skills/skillhub + opensource-skills/packaged）
        force: 强制重新扫描（不跳过已评分的）
        limit: 限制扫描数量
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading

    scan_dirs = [Path(d) for d in (dirs or _DEFAULT_SCAN_DIRS)]

    # 收集所有SKILL.md文件
    all_skills = []
    for scan_dir in scan_dirs:
        if not scan_dir.exists():
            print(f"[SKIP] 目录不存在: {scan_dir}")
            continue
        # 递归查找所有SKILL.md文件（支持多级嵌套目录）
        for skill_md in sorted(scan_dir.rglob("SKILL.md")):
            all_skills.append(skill_md)

    print(f"发现 {len(all_skills)} 个SKILL.md文件", flush=True)

    # 连接DB
    conn = _get_db_connection()

    # 获取已评分的slug（断点续扫）
    if not force:
        scored_slugs = _get_scored_slugs(conn)
        print(f"DB中已评分: {len(scored_slugs)} 个（将跳过）", flush=True)
    else:
        scored_slugs = set()
        print("强制重新扫描模式", flush=True)

    # 筛选需要扫描的skill
    to_scan = []
    for skill_md in all_skills:
        slug = _extract_slug_from_skill_md(skill_md)
        if not slug:
            slug = skill_md.parent.name
        if slug in scored_slugs and not force:
            continue
        to_scan.append((slug, skill_md))

    if limit:
        to_scan = to_scan[:limit]

    print(f"待扫描: {len(to_scan)} 个", flush=True)
    if not to_scan:
        print("无待扫描skill，生成报告...", flush=True)
        _generate_scan_report(conn, [])
        conn.close()
        return

    # 加载并行配置
    try:
        config = _load_config()
        max_workers = config.get("scan", {}).get("max_workers", 5)
    except Exception:
        max_workers = 5

    print(f"并行线程数: {max_workers}", flush=True)

    # 并行扫描
    scan_results = []
    success_count = 0
    error_count = 0
    completed_count = 0
    db_lock = threading.Lock()
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务
        future_to_slug = {
            executor.submit(_score_one_skill, item): item[0] for item in to_scan
        }

        for future in as_completed(future_to_slug):
            slug = future_to_slug[future]
            completed_count += 1

            try:
                result = future.result()
            except Exception as e:
                result = {"slug": slug, "error": str(e)}

            if result.get("error"):
                scan_results.append(result)
                error_count += 1
                print(f"  [{completed_count}/{len(to_scan)}] ERROR {slug}: {result['error']}", flush=True)
            else:
                score = result["score"]
                feedback = result.get("feedback", "")
                dimensions = result.get("dimensions", {})

                # 线程安全地写DB
                with db_lock:
                    written = _write_score_to_db(conn, slug, score, feedback, dimensions)
                    conn.commit()

                if written:
                    scan_results.append({"slug": slug, "score": score, "passed": result.get("passed", False)})
                    success_count += 1
                else:
                    scan_results.append({"slug": slug, "error": "DB中无此slug记录"})
                    error_count += 1

                status = "PASS" if result.get("passed") else "FAIL"
                print(f"  [{completed_count}/{len(to_scan)}] {status} {slug}: {score:.2f}", flush=True)

            # 每10个打印进度
            if completed_count % 10 == 0:
                elapsed = time.time() - start_time
                rate = completed_count / elapsed if elapsed > 0 else 0
                remaining = (len(to_scan) - completed_count) / rate if rate > 0 else 0
                print(f"  --- 进度: {completed_count}/{len(to_scan)} ({completed_count/len(to_scan)*100:.1f}%) "
                      f"成功={success_count} 错误={error_count} "
                      f"速率={rate:.1f}/s 预计剩余={remaining:.0f}s ---", flush=True)

    elapsed_total = time.time() - start_time
    print(f"\n{'='*60}", flush=True)
    print(f"扫描完成: {len(to_scan)} 个", flush=True)
    print(f"  成功: {success_count}", flush=True)
    print(f"  错误: {error_count}", flush=True)
    print(f"  耗时: {elapsed_total:.0f}秒 ({elapsed_total/60:.1f}分钟)", flush=True)

    # 生成报告 (T1-007)
    _generate_scan_report(conn, scan_results)

    conn.close()


# ============ CLI入口 ============


def main():
    if len(sys.argv) < 2:
        print("用法: python local_quality_scorer.py <skill_dir_or_path> [--json]")
        print("      python local_quality_scorer.py --test")
        print("      python local_quality_scorer.py scan-all [--dir <path>] [--force] [--limit N]")
        sys.exit(1)

    if sys.argv[1] == "--test":
        _self_test()
        return

    # T1-005: 批量扫描命令
    if sys.argv[1] == "scan-all":
        force = "--force" in sys.argv
        limit = None
        custom_dirs = None

        # 解析 --dir 参数
        if "--dir" in sys.argv:
            idx = sys.argv.index("--dir")
            if idx + 1 < len(sys.argv):
                dir_val = sys.argv[idx + 1]
                # 支持相对路径（相对于项目根目录）
                dir_path = Path(dir_val)
                if not dir_path.is_absolute():
                    dir_path = _PROJECT_ROOT / dir_val
                custom_dirs = [dir_path]

        # 解析 --limit 参数
        if "--limit" in sys.argv:
            idx = sys.argv.index("--limit")
            if idx + 1 < len(sys.argv):
                try:
                    limit = int(sys.argv[idx + 1])
                except ValueError:
                    print(f"错误: --limit 参数需要整数, 得到: {sys.argv[idx + 1]}")
                    sys.exit(1)

        scan_all(dirs=custom_dirs, force=force, limit=limit)
        return

    skill_input = sys.argv[1]
    output_json = "--json" in sys.argv

    result = score_skill(skill_input)

    if output_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        _print_result(result)

    sys.exit(0 if result.get("passed") else 1)


def _print_result(result):
    """人类可读输出"""
    print(f"\n{'='*60}")
    print(f"SKILL质量评分报告")
    print(f"{'='*60}")
    print(f"总分: {result.get('total_score', 0.0):.2f} / 5.0")
    print(f"通过: {'是' if result.get('passed') else '否'} (阈值: {SCORE_THRESHOLD})")

    if result.get("error"):
        print(f"错误: {result['error']}")
        return

    dims = result.get("dimensions", {})
    dim_names = {
        "completeness": "功能完整性",
        "accuracy": "准确性",
        "usability": "易用性",
        "security": "安全性",
        "innovation": "创新性",
    }
    print(f"\n维度详情:")
    for key, name in dim_names.items():
        d = dims.get(key, {})
        score = d.get("score", 0.0)
        reason = d.get("reason", "")
        bar = "█" * int(score * 10) + "░" * (10 - int(score * 10))
        print(f"  {name:8s} [{bar}] {score:.1f}  {reason}")

    print(f"\n改进建议:")
    print(f"  {result.get('feedback', '无')}")
    print(f"{'='*60}")


def _self_test():
    """自检：验证配置加载和API可用性"""
    print("=== 本地质量评分器自检 ===\n")

    # 1. 配置加载
    try:
        config = _load_config()
        print(f"[OK] 配置加载成功: {CONFIG_PATH}")
        print(f"     LLM端点: {config['llm']['api_endpoint']}")
        print(f"     模型: {config['llm']['model']}")
    except Exception as e:
        print(f"[FAIL] 配置加载失败: {e}")
        sys.exit(1)

    # 2. API密钥
    api_key = _get_api_key(config)
    if api_key:
        print(f"[OK] API密钥可用 (来源: {config['llm'].get('api_key_env', 'DEEPSEEK_API_KEY')})")
    else:
        print("[WARN] 未找到API密钥，请设置环境变量 DEEPSEEK_API_KEY")
        sys.exit(1)

    # 3. 查找示例skill
    test_skills = [
        Path(__file__).resolve().parent.parent / "packaged-skills" / "skillhub",
        Path(__file__).resolve().parent.parent / "opensource-skills" / "packaged",
    ]
    test_skill_dir = None
    for d in test_skills:
        if d.exists():
            for sub in d.iterdir():
                if sub.is_dir() and (sub / "SKILL.md").exists():
                    test_skill_dir = sub
                    break
            if test_skill_dir:
                break

    if not test_skill_dir:
        print("[WARN] 未找到测试用skill，跳过评分测试")
        return

    print(f"[OK] 测试skill: {test_skill_dir.name}")

    # 4. 执行评分
    print("\n执行评分中...")
    result = score_skill(test_skill_dir)

    if result.get("error"):
        print(f"[FAIL] 评分失败: {result['error']}")
        sys.exit(1)

    print(f"[OK] 评分成功:")
    print(f"     总分: {result['total_score']:.2f} / 5.0")
    print(f"     通过: {'是' if result['passed'] else '否'}")
    for key, val in result.get("dimensions", {}).items():
        print(f"     {key}: {val['score']:.1f}")

    print("\n=== 自检完成 ===")


if __name__ == "__main__":
    main()
