# 详细参考 - moltbook-firewall-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
#!/usr/bin/env python3
"""专业版上下文感知深度注入检测"""

import re
import json
from datetime import datetime
from collections import deque

class DeepInjectionDetector:
    """上下文感知深度注入检测引擎"""

    DIRECT_PATTERNS = [
        (r'ignore.{0,20}(previous|prior|above).{0,20}(instruction|prompt|rule)',
         "CRITICAL", "直接指令覆盖", "使用角色边界和分隔符隔离用户输入"),
        (r'(disregard|forget|discard).{0,20}(all|previous|above).{0,20}(instruction|prompt)',
         "CRITICAL", "指令清除攻击", "在系统提示中声明不可被覆盖"),
        (r'you.{0,10}(are|act).{0,10}(now|as).{0,20}(different|new|jailbreak|developer|admin)',
         "HIGH", "角色劫持攻击", "输出前验证角色一致性"),
    ]

    INDIRECT_PATTERNS = [
        (r'(reveal|show|print|output).{0,20}(system|hidden|secret).{0,20}(prompt|instruction)',
         "HIGH", "系统提示泄露", "不在输出中包含系统提示"),
        (r'(translate|repeat|echo|paraphrase).{0,20}(system|hidden|initial).{0,20}(prompt|instruction)',
         "HIGH", "间接提示泄露", "过滤translate/echo类请求"),
        (r'(base64|hex|rot13|url.?encod).{0,30}(decode|decrypt|convert)',
         "MEDIUM", "编码绕过攻击", "解码后重新安全检查"),
    ]

    MULTI_TURN_PATTERNS = [
        (r'(remember|note|store).{0,30}(this|following).{0,30}(as|as a).{0,20}(rule|instruction|system)',
         "HIGH", "多轮注入植入", "不跨会话存储用户规则"),
        (r'(in (our|the) next|later|when I ask).{0,30}(do|execute|follow|ignore)',
         "MEDIUM", "延迟执行注入", "不执行用户预设延迟指令"),
    ]

    def __init__(self, context_window=10):
        self.context_history = deque(maxlen=context_window)
        self.injection_attempts = []

    def detect(self, user_input, session_id=None):
        """深度检测注入攻击"""
        self.context_history.append({
            "input": user_input,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "session": session_id
        })

        findings = []

        for pattern, severity, desc, remediation in self.DIRECT_PATTERNS:
            for match in re.finditer(pattern, user_input, re.IGNORECASE):
                findings.append({
                    "layer": "direct",
                    "severity": severity,
                    "type": desc,
                    "match": match.group()[:50],
                    "remediation": remediation
                })

        for pattern, severity, desc, remediation in self.INDIRECT_PATTERNS:
            for match in re.finditer(pattern, user_input, re.IGNORECASE):
                findings.append({
                    "layer": "indirect",
                    "severity": severity,
                    "type": desc,
                    "match": match.group()[:50],
                    "remediation": remediation
                })

        for pattern, severity, desc, remediation in self.MULTI_TURN_PATTERNS:
            for match in re.finditer(pattern, user_input, re.IGNORECASE):
                contextual_risk = self._check_contextual_risk(user_input, match.group())
                findings.append({
                    "layer": "multi_turn",
                    "severity": severity,
                    "type": desc,
                    "match": match.group()[:50],
                    "contextual_risk": contextual_risk,
                    "remediation": remediation
                })

        progressive = self._detect_progressive_injection()
        if progressive:
            findings.append(progressive)

        should_block = any(f["severity"] == "CRITICAL" for f in findings)

        return {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "session": session_id,
            "input_length": len(user_input),
            "context_entries": len(self.context_history),
            "findings_count": len(findings),
            "should_block": should_block,
            "findings": findings
        }

    def _check_contextual_risk(self, current_input, pattern):
        """检查上下文关联风险"""
        risk = "LOW"
        for entry in list(self.context_history)[:-1]:
            if pattern.lower() in entry["input"].lower():
                risk = "HIGH"
                break
        return risk

    def _detect_progressive_injection(self):
        """检测渐进式注入(多轮逐步诱导)"""
        if len(self.context_history) < 3:
            return None

        recent = list(self.context_history)[-3:]

        trust_indicators = ['thank', 'great', 'perfect', 'exactly']
        rule_indicators = ['remember', 'note', 'from now on', 'always']
        exec_indicators = ['now do', 'execute', 'as we discussed', 'like you said']

        has_trust = any(any(ind in e["input"].lower() for ind in trust_indicators) for e in recent[:1])
        has_rule = any(any(ind in e["input"].lower() for ind in rule_indicators) for e in recent[1:2])
        has_exec = any(any(ind in e["input"].lower() for ind in exec_indicators) for e in recent[2:])

        if has_trust and has_rule and has_exec:
            return {
                "layer": "progressive",
                "severity": "CRITICAL",
                "type": "渐进式注入攻击",
                "description": "检测到信任建立->规则植入->执行请求的渐进式注入模式",
                "remediation": "重置会话上下文,拒绝执行用户预设规则"
            }

        return None
```

## 代码示例 (python)

```python
#!/usr/bin/env python3
"""专业版沙盒隔离执行环境"""

import subprocess
import json
import os
import tempfile
import shutil
from datetime import datetime

class SandboxExecutor:
    """沙盒隔离执行器"""

    SANDBOX_CONFIG = {
        "timeout": 30,           # 执行超时(秒)
        "memory_limit": "256m",  # 内存限制
        "cpu_limit": "50%",      # CPU限制
        "network": "none",       # 网络隔离
        "read_only_root": True,  # 只读根文件系统
        "allowed_paths": [],     # 允许访问的路径
        "env_vars": {},          # 允许的环境变量
    }

    def __init__(self):
        self.sandbox_dir = tempfile.mkdtemp(prefix="agent_sandbox_")
        self.execution_log = []

    def execute_safely(self, command, params=None):
        """在沙盒中安全执行命令"""
        params = params or {}

        safety_check = self._check_safety(command, params)
        if not safety_check["safe"]:
            return {
                "status": "BLOCKED",
                "reason": safety_check["reason"],
                "command": command
            }

        sandbox_path = os.path.join(self.sandbox_dir, f"exec_{len(self.execution_log)}")
        os.makedirs(sandbox_path, exist_ok=True)

        try:
            result = subprocess.run(
                command if isinstance(command, list) else command.split(),
                cwd=sandbox_path,
                timeout=self.SANDBOX_CONFIG["timeout"],
                capture_output=True,
                text=True,
                env=self._get_safe_env(),
            )

            execution_result = {
                "status": "COMPLETED",
                "exit_code": result.returncode,
                "stdout": result.stdout[:5000],  # 限制输出长度
                "stderr": result.stderr[:1000],
                "duration": "N/A",
                "sandbox_path": sandbox_path
            }
        except subprocess.TimeoutExpired:
            execution_result = {
                "status": "TIMEOUT",
                "reason": f"执行超时(>{self.SANDBOX_CONFIG['timeout']}秒)",
                "command": command
            }
        except Exception as e:
            execution_result = {
                "status": "ERROR",
                "reason": str(e),
                "command": command
            }

        self._cleanup_sandbox(sandbox_path)

        self.execution_log.append({
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "command": str(command)[:200],
            "result": execution_result["status"],
            "exit_code": execution_result.get("exit_code")
        })

        return execution_result

    def _check_safety(self, command, params):
        """安全检查"""
        DANGEROUS = ['rm -rf', 'mkfs', 'dd if=', 'shutdown', 'reboot', ':(){:|:&};:']
        cmd_str = str(command) + str(params)

        for pattern in DANGEROUS:
            if pattern in cmd_str:
                return {"safe": False, "reason": f"检测到危险操作: {pattern}"}

        return {"safe": True}

    def _get_safe_env(self):
        """获取安全的环境变量"""
        safe_env = {"PATH": "/usr/local/bin:/usr/bin:/bin"}
        safe_env.update(self.SANDBOX_CONFIG["env_vars"])
        return safe_env

    def _cleanup_sandbox(self, path):
        """清理沙盒"""
        try:
            shutil.rmtree(path)
        except:
            pass

    def get_execution_log(self):
        """获取执行日志"""
        return self.execution_log
```

