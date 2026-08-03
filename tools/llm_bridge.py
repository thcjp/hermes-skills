#!/usr/bin/env python3
"""
LLM执行桥接层 (E13 Bridge)
=========================
将E13断点(只生成prompt不执行)改为双路径执行:
  路径1: Trae AI代理(交互模式) — 写入pending文件供Trae AI执行,结果回写
  路径2: 外部API(批处理模式) — 调用skill_deep_rewrite._call_llm (SiliconFlow API)

设计原则:
  - 优先Trae AI代理(在Trae环境中运行时)
  - 外部API作为批处理fallback(无人值守时)
  - 两者均不可用时返回no_llm_available,由调用方走真实降级(非mock)

依赖说明:
  - LLM/API Key: 可选(有API Key时走外部API路径)
  - 运行环境: Trae Work(交互模式)或独立运行(批处理模式)
  - 无外部依赖(标准库 + 项目内部模块)
"""

import json
import time
import hashlib
import os
from pathlib import Path
from datetime import datetime

# === Phase 1: 统一配置导入 ===
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
from project_config import DATA_DIR
# === End Phase 1 ===

# 路径配置
PENDING_DIR = DATA_DIR / "pending_llm_tasks"
RESULT_DIR = DATA_DIR / "llm_results"


class LLMBridge:
    """LLM执行桥接 — 双路径自动选择

    路径1 (Trae AI代理): 写入pending JSON文件,Trae AI代理读取执行,结果回写
    路径2 (外部API): 直接调用SiliconFlow API(复用skill_deep_rewrite._call_llm)

    选择逻辑:
      - prefer_trae_agent=True(默认) → 路径1
      - prefer_trae_agent=False 或路径1无结果 → 路径2(如有API Key)
      - 两者均不可用 → 返回no_llm_available
    """

    def __init__(self, prefer_trae_agent=True):
        """初始化LLM桥接

        V147 R4增强: 优先策略调整 — 当外部API可用时优先使用API(同步可靠),
        仅当API不可用时才使用Trae代理路径(异步文件消息)。
        原逻辑: 总是先尝试Trae代理(返回pending)再降级到API,导致不必要的文件写入和延迟。
        """
        self.prefer_trae_agent = prefer_trae_agent
        self.api_key = os.environ.get('SILICONFLOW_API_KEY', '')
        # V147 R4: 检测是否在Trae环境中运行(有TRAE特定的环境变量)
        self._in_trae_env = bool(os.environ.get('TRAE_WORKSPACE_ID') or
                                  os.environ.get('TRAE_SESSION_ID') or
                                  os.environ.get('TRAE_AGENT_MODE'))

    def execute(self, task_type: str, skill_data: dict, context: dict = None) -> dict:
        """执行LLM任务 — 自动选择路径

        V165增强路径选择逻辑:
          1. generate/rewrite任务 + Trae环境 → 优先Trae代理路径(使用GLM-5.2)
          2. score/analyze/evaluate任务 → 直接使用外部API(glm-5.2→glm-4-flash降级)
          3. Trae代理不可用 → 降级到外部API
          4. 两者均不可用 → 返回no_llm_available

        Args:
            task_type: 任务类型 (generate|score|rewrite|analyze)
            skill_data: skill内容数据(必须包含slug)
            context: 额外上下文(可选)

        Returns:
            dict:
              status: success | pending | error | no_llm_available
              result: LLM执行结果文本(status=success时)
              task_id: 唯一任务标识
              prompt: 生成的prompt(status!=success时供调试)
        """
        from llm_validator import generate_agent_prompt
        prompt = generate_agent_prompt(task_type, skill_data, context)
        task_id = self._gen_task_id(task_type, skill_data)

        # V165: 增强类任务(generate/rewrite)优先使用Trae代理(GLM-5.2)
        # 评分类任务(score/analyze/evaluate)使用外部API(glm-5.2→glm-4-flash)
        is_enhancement_task = task_type in ('generate', 'rewrite')
        
        if is_enhancement_task and self.prefer_trae_agent:
            result = self._execute_with_trae_agent(prompt, task_id)
            if result.get('status') == 'success':
                return result
            # Trae代理无结果,降级到外部API
            if self.api_key:
                return self._execute_with_external_api(prompt, task_id)
            return result

        # 评分类任务或非Trae环境: 直接使用外部API(已支持429降级)
        if self.api_key:
            return self._execute_with_external_api(prompt, task_id)

        # 无API Key时: Trae代理路径(异步,适合交互式Trae Work会话)
        if self.prefer_trae_agent:
            result = self._execute_with_trae_agent(prompt, task_id)
            if result.get('status') == 'success':
                return result
            # Trae代理也无结果,返回pending状态(调用方可决定是否等待或降级)
            return result

        # 两者均不可用
        return {
            'status': 'no_llm_available',
            'prompt': prompt,
            'task_id': task_id,
            'detail': '无SILICONFLOW_API_KEY且Trae代理无结果' + (' (当前在Trae环境)' if self._in_trae_env else ' (不在Trae环境)'),
        }

    def _execute_with_trae_agent(self, prompt: str, task_id: str) -> dict:
        """路径1: 写入pending文件供Trae AI代理执行

        Trae AI代理会:
        1. 扫描PENDING_DIR中的JSON文件
        2. 读取prompt并执行
        3. 将结果写入RESULT_DIR/{task_id}.json
        """
        PENDING_DIR.mkdir(parents=True, exist_ok=True)
        task_file = PENDING_DIR / f"{task_id}.json"
        task_file.write_text(json.dumps({
            'task_id': task_id,
            'prompt': prompt,
            'created_at': datetime.now().isoformat(),
            'status': 'pending',
        }, ensure_ascii=False, indent=2), encoding='utf-8')

        # 检查是否已有执行结果(可能是同步执行或之前的结果)
        result = self._read_result(task_id)
        if result:
            return result

        # 无结果,返回pending状态
        return {
            'status': 'pending',
            'task_id': task_id,
            'prompt': prompt,
        }

    def _execute_with_external_api(self, prompt: str, task_id: str) -> dict:
        """路径2: 调用SiliconFlow API(复用skill_deep_rewrite._call_llm)"""
        try:
            from skill_deep_rewrite import _call_llm
            result_text = _call_llm(prompt)
            self._write_result(task_id, result_text, 'external_api')
            return {
                'status': 'success',
                'result': result_text,
                'task_id': task_id,
            }
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'task_id': task_id,
                'prompt': prompt,
            }

    def _read_result(self, task_id: str) -> dict:
        """读取已执行的LLM结果"""
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        result_file = RESULT_DIR / f"{task_id}.json"
        if result_file.exists():
            data = json.loads(result_file.read_text(encoding='utf-8'))
            return {
                'status': 'success',
                'result': data.get('result', ''),
                'task_id': task_id,
            }
        return None

    def _write_result(self, task_id: str, result: str, source: str):
        """写入LLM执行结果"""
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        result_file = RESULT_DIR / f"{task_id}.json"
        result_file.write_text(json.dumps({
            'task_id': task_id,
            'result': result,
            'source': source,
            'completed_at': datetime.now().isoformat(),
        }, ensure_ascii=False, indent=2), encoding='utf-8')

    def _gen_task_id(self, task_type: str, skill_data: dict) -> str:
        """生成唯一task_id"""
        slug = skill_data.get('slug', 'unknown')
        ts = str(int(time.time()))
        return f"{task_type}_{slug}_{ts}"


# ============ 单例便捷API ============

_bridge = None


def get_bridge() -> LLMBridge:
    """获取全局LLMBridge单例"""
    global _bridge
    if _bridge is None:
        _bridge = LLMBridge()
    return _bridge


def execute_llm(task_type: str, skill_data: dict, context: dict = None) -> dict:
    """便捷函数: 执行LLM任务"""
    return get_bridge().execute(task_type, skill_data, context)


if __name__ == '__main__':
    # 自检
    print("=== LLM执行桥接层(E13 Bridge)自检 ===\n")

    bridge = LLMBridge()
    print(f"路径配置:")
    print(f"  PENDING_DIR: {PENDING_DIR}")
    print(f"  RESULT_DIR: {RESULT_DIR}")
    print(f"  prefer_trae_agent: {bridge.prefer_trae_agent}")
    print(f"  api_key配置: {'有' if bridge.api_key else '无'}")

    # 测试task_id生成
    task_id = bridge._gen_task_id('analyze', {'slug': 'test-skill'})
    print(f"\n测试task_id生成: {task_id}")

    # 测试execute(no_llm_available场景)
    print("\n测试execute(无LLM可用时)...")
    result = bridge.execute('analyze', {'slug': 'test-skill', 'skill_content': 'test'})
    print(f"  status: {result.get('status')}")
    print(f"  task_id: {result.get('task_id')}")
    print(f"  prompt长度: {len(result.get('prompt', ''))}")

    print("\n=== 自检完成 ===")
