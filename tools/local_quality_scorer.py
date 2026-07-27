#!/usr/bin/env python3
"""
本地LLM质量评分器 (v1.0)
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
"""

import json
import os
import sys
import re
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
    max_chars = 8000
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


# ============ CLI入口 ============


def main():
    if len(sys.argv) < 2:
        print("用法: python local_quality_scorer.py <skill_dir_or_path> [--json]")
        print("      python local_quality_scorer.py --test")
        sys.exit(1)

    if sys.argv[1] == "--test":
        _self_test()
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
