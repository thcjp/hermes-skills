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

阈值: LOCAL_QUALITY_PASS_THRESHOLD (project_config统一配置, 当前=4.5)

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
import os  # [V130 A2] 保留: 需要os.environ
import sys
import re
import time
from pathlib import Path
from datetime import datetime

import requests

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import PROJECT_ROOT, TOOLS_DIR, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, DATA_DIR, DEFAULT_DEEPSEEK_ENDPOINT, LOCAL_QUALITY_PASS_THRESHOLD, LOCAL_QUALITY_GRADE_B, LOCAL_QUALITY_GRADE_C  # V124 W2: 移除unused _DB_PATH; V147 R3.1: 新增LOCAL_QUALITY_PASS_THRESHOLD; V153 R11: 新增等级阈值
if str(TOOLS_DIR) not in _sys.path:
    _sys.path.insert(0, str(TOOLS_DIR))  # V125 W2: 模块级设置TOOLS_DIR(替代函数级sys.path.insert)
# === End Phase 1 ===

# ============ 配置加载 ============

CONFIG_PATH = DATA_DIR / "config" / "quality_scoring_config.json"  # V117 W5: 标准化(替换Path(__file__).resolve().parent.parent)

# V147 R3.1: 统一从project_config导入阈值(消除本地硬编码4.5)
SCORE_THRESHOLD = LOCAL_QUALITY_PASS_THRESHOLD


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


def score_skill(skill_input, persist: bool = True):
    """
    对SKILL.md评分。

    参数:
        skill_input: SKILL.md文件路径(Path/str) 或 目录路径 或 文件内容字符串
        persist: 是否将评分持久化到DB(skills表+scores表)。默认True。
                 scan_all等批量场景应设为False(由调用方自行持久化)。

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

    # V161审计修复: 检测模板化评分(所有维度分数完全相同)并告警
    # 防御性监控: 不同维度反映技能不同方面, 质量必然存在差异;
    # 若5个维度分数全部相同, 说明LLM可能未执行真实差异化评估
    dim_scores = [d["score"] for d in dimensions.values()]
    if len(dim_scores) == 5 and len(set(dim_scores)) == 1:
        print(f"[WARN] 检测到模板化评分: 5个维度分数均为{dim_scores[0]}, "
              f"总分={total_score}, 可能是LLM未执行差异化评估(检查prompt模板)")

    suggestions = parsed.get("suggestions", [])

    feedback_parts = []
    for dim_key, dim_val in dimensions.items():
        if dim_val["score"] < 0.9:
            feedback_parts.append(f"[{dim_key}] {dim_val['reason']}")
    if suggestions:
        feedback_parts.append("改进建议: " + "; ".join(suggestions))

    # V153 R1: 计算等级(0-5标度, 对齐TRACE等级体系)
    # A(>=4.5) B(>=4.0) C(>=3.5) D(<3.5)
    # V153 R11: 使用project_config统一配置阈值
    if total_score >= SCORE_THRESHOLD:
        grade = 'A'
    elif total_score >= LOCAL_QUALITY_GRADE_B:
        grade = 'B'
    elif total_score >= LOCAL_QUALITY_GRADE_C:
        grade = 'C'
    else:
        grade = 'D'

    feedback = " | ".join(feedback_parts) if feedback_parts else "各维度均达标"

    # V157: 持久化评分到DB (修复 score_skill 不写库导致 upload_gate 查不到 TRACE 评分)
    if persist:
        try:
            # a. 从SKILL.md内容中提取slug(正则从frontmatter提取)
            slug_match = re.search(r'^slug:\s*(.+)$', skill_content, re.MULTILINE)
            if slug_match:
                slug = slug_match.group(1).strip()
                # b. 获取数据库连接
                conn = db_module.get_db()
                c = conn.cursor()
                now = datetime.now().isoformat()
                # c. 查询 skills 表获取 skill_id
                c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
                row = c.fetchone()
                if row:
                    skill_id = row[0]
                else:
                    # d. skill不存在则插入 (V157修复: status→current_status, 补充NOT NULL字段)
                    c.execute(
                        "INSERT INTO skills (slug, current_version, source, local_path, created_at, updated_at, current_status) VALUES (?, ?, 'local', ?, ?, ?, 'active')",
                        (slug, '0.1.0', str(skill_path) if skill_path else '', now, now)
                    )
                    skill_id = c.lastrowid
                # e. 更新 skills 表(评分/反馈/等级)
                _write_score_to_db(conn, slug, total_score, feedback, dimensions, grade)
                # g. 提交事务并关闭连接(必须在save_score之前关闭,避免database locked)
                conn.commit()
                conn.close()
                # f. 写入 scores 表 (save_score内部自建连接, 避免连接冲突)
                db_module.save_score(
                    skill_id=skill_id,
                    score_type='local_quality',
                    total_score=total_score,
                    reviewer='local_quality_scorer',
                    notes=feedback[:500] if feedback else "",
                    is_pass=1 if total_score >= SCORE_THRESHOLD else 0,
                    pass_threshold=int(SCORE_THRESHOLD * 10),
                    grade=grade,
                )
        except Exception as e:
            # i. DB操作失败时记录警告但不阻断(评分结果仍返回)
            print(f"[WARN] score_skill持久化失败: {e}")
            try:
                if 'conn' in dir() and conn:
                    conn.close()
            except Exception as close_err:
                print(f"[WARN] conn.close失败(可忽略): {close_err}")

    return {
        "total_score": total_score,
        "grade": grade,
        "dimensions": dimensions,
        "feedback": feedback,
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


# V130 A3: 与skill_deep_rewrite._call_llm不是重复定义。
# 差异: 本函数签名(prompt,config,api_key)无重试, 用DEFAULT_DEEPSEEK_ENDPOINT+glm-5.2,
#       max_tokens=2000/temp=0.3/timeout=30, system角色为"质量评测专家"; skill_deep_rewrite版
#       签名含max_retries且有重试循环, 用DEFAULT_SILICONFLOW_ENDPOINT+glm-5.2,
#       max_tokens=3000/temp=0.4/timeout=120, system角色为"技术文档工程师"。
# V165: 统一主模型为glm-5.2,429余额不足时降级到glm-4-flash
def _call_llm(prompt, config, api_key):
    """调用LLM API（OpenAI兼容格式）— V165: 主模型glm-5.2,429时降级到glm-4-flash"""
    llm_config = config.get("llm", {})
    endpoint = llm_config.get("api_endpoint", DEFAULT_DEEPSEEK_ENDPOINT)
    model = llm_config.get("model", "glm-5.2")  # V165: 主模型GLM-5.2
    fallback_model = llm_config.get("fallback_model", "glm-4-flash")  # V165: 429降级模型
    max_tokens = llm_config.get("max_tokens", 2000)
    temperature = llm_config.get("temperature", 0.3)
    timeout = llm_config.get("timeout", 30)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # V165: 模型降级列表 — 主模型429时尝试降级模型
    models_to_try = [model]
    if fallback_model and fallback_model != model:
        models_to_try.append(fallback_model)

    for current_model in models_to_try:
        payload = {
            "model": current_model,
            "messages": [
                {"role": "system", "content": "你是一个专业的SKILL质量评测专家，请严格按照JSON格式返回评测结果。"},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        try:
            resp = requests.post(endpoint, headers=headers, json=payload, timeout=timeout)
            if resp.status_code == 429 and current_model != models_to_try[-1]:
                continue  # 余额不足,尝试降级模型
            resp.raise_for_status()
            data = resp.json()
            content = data["choices"][0]["message"]["content"]
            return {"content": content}
        except requests.exceptions.Timeout:
            if current_model != models_to_try[-1]:
                continue  # 超时也尝试降级模型
            return {"error": f"LLM API请求超时({timeout}s)"}
        except requests.exceptions.ConnectionError as e:
            if current_model != models_to_try[-1]:
                continue
            return {"error": f"LLM API连接失败: {e}"}
        except requests.exceptions.HTTPError as e:
            if resp.status_code == 429 and current_model != models_to_try[-1]:
                continue  # 尝试降级模型
            return {"error": f"LLM API HTTP错误: {e}"}
        except (KeyError, IndexError) as e:
            return {"error": f"LLM API返回格式异常: {e}"}
        except Exception as e:  # [V131 B2] 宽泛捕获: 异常时返回错误/默认值
            return {"error": f"LLM API调用异常: {e}"}

    return {"error": "LLM API调用失败，已尝试所有模型"}


def _sanitize_json_string(s):
    """清理JSON字符串中的非法控制字符"""
    s = s.replace("\x00", "\\u0000").replace("\x01", "\\u0001").replace("\x02", "\\u0002")
    s = s.replace("\x03", "\\u0003").replace("\x04", "\\u0004").replace("\x05", "\\u0005")
    s = s.replace("\x06", "\\u0006").replace("\x07", "\\u0007").replace("\x08", "\\b")
    s = s.replace("\x0b", "\\u000b").replace("\x0c", "\\f").replace("\x0e", "\\u000e")
    s = s.replace("\x0f", "\\u000f").replace("\x10", "\\u0010").replace("\x11", "\\u0011")
    s = s.replace("\x12", "\\u0012").replace("\x13", "\\u0013").replace("\x14", "\\u0014")
    s = s.replace("\x15", "\\u0015").replace("\x16", "\\u0016").replace("\x17", "\\u0017")
    s = s.replace("\x18", "\\u0018").replace("\x19", "\\u0019").replace("\x1a", "\\u001a")
    s = s.replace("\x1b", "\\u001b").replace("\x1c", "\\u001c").replace("\x1d", "\\u001d")
    s = s.replace("\x1e", "\\u001e").replace("\x1f", "\\u001f")
    return s


def _parse_llm_response(content):
    """解析LLM返回的JSON（健壮版，支持malformed JSON）"""
    # 尝试从markdown代码块中提取JSON
    json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", content, re.DOTALL)
    if json_match:
        content = json_match.group(1)

    # 清理控制字符
    sanitized = _sanitize_json_string(content)

    # 尝试直接解析JSON
    data = None
    try:
        data = json.loads(sanitized, strict=False)
    except json.JSONDecodeError as e:  # [V132 C2] 有意降级: JSON解析失败,尝试提取JSON部分  V144: 添加警告日志
        print(f"[WARN] JSON解析失败,尝试提取JSON部分: {e}")

    if data is None:
        # 尝试提取JSON部分
        start = sanitized.find("{")
        end = sanitized.rfind("}")
        if start != -1 and end != -1:
            json_str = sanitized[start : end + 1]
            try:
                data = json.loads(json_str, strict=False)
            except json.JSONDecodeError:
                # 修复未转义的换行符
                fixed = re.sub(r'(?<=": ")(.*?)(?="[,\n\r}])', lambda m: m.group(1).replace("\n", "\\n"), json_str, flags=re.DOTALL)
                try:
                    data = json.loads(fixed, strict=False)
                except json.JSONDecodeError as e:  # [V132 C2] 有意降级: 修复后仍解析失败,回退到正则提取  V144: 添加警告日志
                    print(f"[WARN] 修复后仍解析失败,回退到正则提取: {e}")

    if data is None:
        # 最终回退：用正则提取各维度分数
        dims = {}
        for dim_key in ["completeness", "accuracy", "usability", "security", "innovation"]:
            score_match = re.search(
                rf'"{dim_key}"\s*:\s*\{{\s*"score"\s*:\s*([0-9.]+)',
                sanitized,
                re.IGNORECASE
            )
            reason_match = re.search(
                rf'"{dim_key}"\s*:\s*\{{\s*"score"\s*:\s*[0-9.]+\s*,\s*"reason"\s*:\s*"(.*?)"',
                sanitized,
                re.DOTALL
            )
            if score_match:
                score = max(0.0, min(1.0, float(score_match.group(1))))
                reason = reason_match.group(1).replace("\\n", "\n") if reason_match else ""
                dims[dim_key] = {"score": round(score, 2), "reason": reason}

        if dims:
            return {"dimensions": dims, "suggestions": []}

        return {"error": "无法解析LLM返回为JSON（已尝试多种修复策略）"}

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
        "grade": "D",
        "dimensions": {},
        "feedback": f"评分失败: {error_msg}",
        "passed": False,
        "error": error_msg,
        "scored_at": datetime.now().isoformat(),
    }


# ============ 批量扫描 (T1-005) ============

# V127 X5: 移除冗余sys.path设置(模块级Phase 1已覆盖, TD-194)
# V127 X10: 统一db别名(原带下划线前缀→db_module, TD-199)
from skill_core import db as db_module  # V116 W1: 统一db入口(替代import db)
# V111 W2: 统一从project_config导入PROJECT_ROOT (TD-107, 原: Path(__file__).resolve().parent.parent)
# 默认扫描目录
_DEFAULT_SCAN_DIRS = [
    PROJECT_ROOT / "packaged-skills" / "skillhub",
    PROJECT_ROOT / "packaged-skills" / "plugs",  # V164: 新增plugs扫描(与skill_deep_rewrite对齐)
    PROJECT_ROOT / "opensource-skills" / "packaged",
    PROJECT_ROOT / "differentiated-skills",
    PROJECT_ROOT / "hermes-skills",  # V164: 新增hermes-skills扫描
    PROJECT_ROOT / "enterprise-upload",
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
    except Exception as e:
        print(f"[WARN] 从SKILL.md提取slug失败,返回None: {e}")
    return None


def _get_scored_slugs(conn):
    """获取已有本地评分的slug集合（断点续扫）"""
    c = conn.cursor()
    c.execute("SELECT slug FROM skills WHERE local_quality_score > 0")
    return {row["slug"] for row in c.fetchall()}


def _write_score_to_db(conn, slug, score, feedback, dimensions, grade=None):
    """将评分写入DB (v1.3: 返回skill_id供调用方调用save_score统一持久化)

    V153 R1修复: 增加grade字段持久化(在score_skill中计算但未写入DB)。
    自动检查skills表是否有grade列, 缺失则ALTER TABLE添加(fail-safe)。
    V174修复: 如果skill不存在,自动注册(避免评分丢失)。

    返回: (written: bool, skill_id: int|None)
    """
    c = conn.cursor()
    now = datetime.now().isoformat()

    # 检查skills表是否有grade列, 没有则添加(幂等, fail-safe)
    c.execute("PRAGMA table_info(skills)")
    existing_columns = [row[1] for row in c.fetchall()]
    if 'grade' not in existing_columns:
        c.execute("ALTER TABLE skills ADD COLUMN grade TEXT")

    # 构造feedback摘要（截断到500字符避免DB字段过长）
    feedback_short = feedback[:500] if feedback else ""

    # 构造dimensions JSON
    dims_json = json.dumps(dimensions, ensure_ascii=False) if dimensions else "{}"

    # V174: 先尝试UPDATE
    c.execute("""
        UPDATE skills
        SET local_quality_score = ?,
            local_score_feedback = ?,
            local_score_at = ?,
            grade = ?,
            updated_at = ?
        WHERE slug = ?
    """, (score, feedback_short, now, grade, now, slug))

    written = c.rowcount > 0
    skill_id = None
    
    if not written:
        # V174: skill不存在,自动注册后再UPDATE
        c.execute("""
            INSERT OR IGNORE INTO skills 
            (slug, current_display_name, current_version, source, local_path,
             created_at, updated_at, current_status, workflow_state, source_license)
            VALUES (?, '', '1.0.0', 'auto-registered', '', ?, ?, 'active', 'packaged', 'MIT')
        """, (slug, now, now))
        
        if c.rowcount > 0:
            # 注册成功,再次UPDATE评分
            c.execute("""
                UPDATE skills
                SET local_quality_score = ?,
                    local_score_feedback = ?,
                    local_score_at = ?,
                    grade = ?,
                    updated_at = ?
                WHERE slug = ?
            """, (score, feedback_short, now, grade, now, slug))
            written = c.rowcount > 0
    
    if written:
        c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
        row = c.fetchone()
        if row:
            skill_id = row[0]

    return written, skill_id


def _generate_scan_report(conn, scan_results):
    """生成全量质量评分报告 (T1-007)"""
    report_dir = PROJECT_ROOT / "data" / "reports"
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
        result = score_skill(skill_md_path, persist=False)
        if result.get("error"):
            return {"slug": slug, "error": result["error"]}
        return {
            "slug": slug,
            "score": result["total_score"],
            "grade": result.get("grade", "D"),
            "feedback": result.get("feedback", ""),
            "dimensions": result.get("dimensions", {}),
            "passed": result.get("passed", False),
        }
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常时返回错误/默认值
        return {"slug": slug, "error": str(e)}


# [V131 B5: 与multi_source_discover.scan_all不同(本版是函数, 对方是方法; 扫描逻辑不同)]
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
    conn = db_module.get_db()  # V126 W8: 直接调用(替代_get_db_connection wrapper, TD-188)

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
    except Exception:  # [V130 A1] 宽泛捕获: 配置加载可能因文件缺失/JSON格式/键不存在等多种原因失败
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
            except Exception as e:  # [V131 B2] 宽泛捕获: 异常更新状态/计数继续
                result = {"slug": slug, "error": str(e)}

            if result.get("error"):
                scan_results.append(result)
                error_count += 1
                print(f"  [{completed_count}/{len(to_scan)}] ERROR {slug}: {result['error']}", flush=True)
            else:
                score = result["score"]
                grade = result.get("grade", "D")
                feedback = result.get("feedback", "")
                dimensions = result.get("dimensions", {})

                # 线程安全地写DB
                with db_lock:
                    written, skill_id = _write_score_to_db(conn, slug, score, feedback, dimensions, grade)
                    conn.commit()

                # v1.3: 统一持久化到scores表 (commit后调用save_score, 避免连接冲突)
                if written and skill_id:
                    try:
                        db_module.save_score(
                            skill_id=skill_id,
                            score_type='local_quality',
                            total_score=score,
                            reviewer='local_quality_scorer',
                            notes=(feedback[:500] if feedback else ""),
                            is_pass=1 if score >= SCORE_THRESHOLD else 0,
                            pass_threshold=SCORE_THRESHOLD,
                            grade=grade,
                        )
                    except Exception as e:
                        # [V129 Z6] 记录异常而非静默pass
                        print(f"  [WARN] save_score持久化失败({slug}): {e}")

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
                    dir_path = PROJECT_ROOT / dir_val
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
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
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
        PACKAGED_SKILLS_DIR / "skillhub",  # V117 W5: 标准化(替换Path(__file__).resolve().parent.parent)
        OPENSOURCE_SKILLS_DIR / "packaged",  # V117 W5: 标准化
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


# ============ E13: TRAE Work AI代理适配 ============

def score_skill_with_agent(skill_input) -> dict:
    """E13: 使用LLM评分skill — 双路径(Trae AI代理/外部API)

    V138 A2: 修复断点 — 从"只返回prompt+fallback字符串"改为"调用llm_bridge执行+返回结果"。
    LLM不可用时走score_skill()规则评分降级(真实降级, 非mock)。
    """
    from llm_bridge import get_bridge
    bridge = get_bridge()
    skill_content, skill_path = _resolve_skill_input(skill_input)
    if not skill_content:
        return _error_result("无法读取SKILL.md内容")
    slug = Path(skill_path).parent.name if skill_path else 'unknown'
    skill_data = {'slug': slug, 'skill_content': skill_content}
    result = bridge.execute('score', skill_data)
    if result.get('status') == 'success':
        return {'result': result['result'], 'source': result.get('task_id', '')}
    # fallback: 走规则评分降级(真实降级, 非mock)
    return score_skill(skill_input)


# ============ E2: 基线对比测试 ============

def run_baseline_comparison(
    skill_input,
    priority: str = 'P0',
    max_baseline_tests: int = 10,
    _test_count: int = 0,
):
    """E2: 基线对比测试 — With-skill vs Without-skill效果对比

    限P0 Skill执行, max_baseline_tests=10 (F-09修正)。
    通过对比"有skill内容"与"无skill内容(仅骨架)"的评分差异,
    量化skill内容的实际价值增量。

    参数:
        skill_input: SKILL.md文件路径(Path/str) 或 目录路径 或 文件内容字符串
        priority: Skill优先级, 仅'P0'时执行对比(默认'P0')
        max_baseline_tests: 最大基线测试数量(默认10, F-09)
        _test_count: 已执行的基线测试计数(内部递增, 防超限)

    返回:
        {
            'baseline_score': float,     # 无skill内容时的基线分数(0-5)
            'enhanced_score': float,     # 有skill内容时的增强分数(0-5)
            'improvement': float,         # 提升幅度(enhanced - baseline)
            'improvement_pct': float,     # 提升百分比
            'baseline_summary': str,      # 基线内容摘要
            'enhanced_summary': str,       # 增强内容摘要
            'comparison_report': str,     # 对比报告文本
            'priority': str,              # 使用的优先级
            'tested_at': str,             # 测试时间(ISO)
            'skipped': bool,              # 是否跳过
            'skip_reason': str,           # 跳过原因
        }
    """
    # F-09: 仅对P0优先级Skill执行基线对比
    if priority != 'P0':
        return {
            'baseline_score': 0.0,
            'enhanced_score': 0.0,
            'improvement': 0.0,
            'improvement_pct': 0.0,
            'baseline_summary': '',
            'enhanced_summary': '',
            'comparison_report': '',
            'priority': priority,
            'tested_at': datetime.now().isoformat(),
            'skipped': True,
            'skip_reason': f'非P0优先级(priority={priority}), 跳过基线对比',
        }

    # F-09: 超过max_baseline_tests则跳过
    if _test_count >= max_baseline_tests:
        return {
            'baseline_score': 0.0,
            'enhanced_score': 0.0,
            'improvement': 0.0,
            'improvement_pct': 0.0,
            'baseline_summary': '',
            'enhanced_summary': '',
            'comparison_report': '',
            'priority': priority,
            'tested_at': datetime.now().isoformat(),
            'skipped': True,
            'skip_reason': f'已达最大基线测试数量({max_baseline_tests})',
        }

    # 1. 读取实际SKILL.md内容(增强版)
    enhanced_content, skill_path = _resolve_skill_input(skill_input)
    if not enhanced_content:
        return _error_result('E2基线对比: 无法读取SKILL.md内容')

    # 2. 构造基线内容(无skill能力版): 保留frontmatter + 最小骨架正文
    baseline_content = _create_baseline_content(enhanced_content)

    # 3. 评分增强版(有skill)
    enhanced_result = score_skill(enhanced_content)
    enhanced_score = enhanced_result.get('total_score', 0.0)

    # 4. 评分基线版(无skill)
    baseline_result = score_skill(baseline_content)
    baseline_score = baseline_result.get('total_score', 0.0)

    # 5. 计算提升
    improvement = round(enhanced_score - baseline_score, 2)
    improvement_pct = round(
        (improvement / baseline_score * 100) if baseline_score > 0 else 0.0, 1
    )

    # 6. 生成对比报告
    report_lines = [
        f'基线对比报告 (E2)',
        f'  基线分数(无skill): {baseline_score:.2f} / 5.0',
        f'  增强分数(有skill): {enhanced_score:.2f} / 5.0',
        f'  提升幅度: +{improvement:.2f} ({improvement_pct:+.1f}%)',
        f'  基线内容: frontmatter + 最小骨架(无核心能力)',
        f'  增强内容: 完整SKILL.md(含核心能力+输入输出+依赖)',
    ]

    # 各维度对比
    enhanced_dims = enhanced_result.get('dimensions', {})
    baseline_dims = baseline_result.get('dimensions', {})
    if enhanced_dims and baseline_dims:
        report_lines.append('  维度对比:')
        for dim_key in ['completeness', 'accuracy', 'usability', 'security', 'innovation']:
            e_score = enhanced_dims.get(dim_key, {}).get('score', 0.0)
            b_score = baseline_dims.get(dim_key, {}).get('score', 0.0)
            diff = e_score - b_score
            report_lines.append(
                f'    {dim_key:15s}: {b_score:.2f} → {e_score:.2f} ({diff:+.2f})'
            )

    return {
        'baseline_score': baseline_score,
        'enhanced_score': enhanced_score,
        'improvement': improvement,
        'improvement_pct': improvement_pct,
        'baseline_summary': f'基线内容{len(baseline_content)}字符, 分数{baseline_score:.2f}',
        'enhanced_summary': f'增强内容{len(enhanced_content)}字符, 分数{enhanced_score:.2f}',
        'comparison_report': '\n'.join(report_lines),
        'priority': priority,
        'tested_at': datetime.now().isoformat(),
        'skipped': False,
        'skip_reason': '',
    }


def _create_baseline_content(skill_content: str) -> str:
    """从完整SKILL.md构造基线内容(无skill能力版)

    保留frontmatter(保持slug/name等元信息), 替换正文为最小骨架:
    - 仅保留标题行
    - 移除核心能力、输入输出格式、依赖说明等实质内容
    - 用占位文本替代, 模拟"没有skill"的场景

    参数:
        skill_content: 完整SKILL.md内容

    返回:
        基线SKILL.md内容字符串
    """
    # 提取frontmatter
    if skill_content.startswith('---'):
        parts = re.split(r'^---\s*$', skill_content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            frontmatter = parts[1]
            # 提取displayName用于标题
            display_match = re.search(
                r'^displayName:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE
            )
            display_name = display_match.group(1) if display_match else 'Skill'
            slug_match = re.search(
                r'^slug:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE
            )
            slug = slug_match.group(1) if slug_match else 'unknown'
        else:
            frontmatter = ''
            display_name = 'Skill'
            slug = 'unknown'
    else:
        frontmatter = ''
        display_name = 'Skill'
        slug = 'unknown'

    # 构造基线内容: frontmatter + 最小骨架正文(无实质内容)
    baseline = f"""---
{frontmatter.strip()}
---

# {display_name}

## 核心功能

本skill的核心功能待补充。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| input | string | 是 | 输入内容 |

## 输出格式

```json
{{
  "success": true,
  "data": {{
    "result": "待实现"
  }}
}}
```

## 依赖说明

### 运行环境
- 待补充
"""
    return baseline


if __name__ == "__main__":
    main()
