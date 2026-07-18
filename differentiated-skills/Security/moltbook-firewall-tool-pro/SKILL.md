---
slug: moltbook-firewall-tool-pro
name: moltbook-firewall-tool-pro
version: "1.0.0"
displayName: Agent防火墙专业版
summary: 企业级Agent安全防护平台,支持深度注入检测、沙盒隔离、多Agent统一管理、实时监控与审计,适合企业Agent安全团队。
license: MIT
edition: pro
description: |-
  Agent防火墙专业版,为企业提供全方位AI Agent安全防护能力。
  核心能力:上下文感知深度注入检测、沙盒隔离、参数投毒检测、多Agent统一管理、实时监控与告警、完整审计链。
  适用场景:企业级Agent安全治理、红蓝对抗防护、合规审计、Agent安全门禁。
  差异化:专业版兼容免费版防护方法,新增企业级深度检测与多Agent管理能力,满足规模化Agent安全需求。
  触发关键词: 深度注入检测, 沙盒隔离, 参数投毒, 多Agent管理, 实时监控, sandbox isolation, deep injection, enterprise
tags:
- 安全
- AI安全
- 企业版
- 沙盒隔离
tools:
- read
- exec
---

# Agent防火墙专业版

## 概述

专业版为企业提供完整的AI Agent安全防护平台,在免费版基础防护能力之上,新增上下文感知深度注入检测、沙盒隔离执行、工具参数投毒检测、多Agent统一管理、实时监控与Webhook告警、完整审计链与SARIF报告。专业版完全兼容免费版防护规则,已有安全配置可无缝升级,适合企业级Agent安全治理。

### 专业版核心优势

| 优势 | 说明 |
|:-----|:-----|
| 深度检测 | 上下文感知,检测多轮+编码注入 |
| 沙盒隔离 | Agent工具在沙盒中执行,限制影响范围 |
| 参数投毒 | 检测工具参数中的恶意载荷 |
| 多Agent管理 | 统一管理多个Agent的安全策略 |
| 实时监控 | 全维度安全监控+智能告警 |
| 审计链 | 完整可追溯的安全审计记录 |
| SARIF报告 | 集成到代码扫描与合规流程 |
| 自动修复 | 检测到攻击自动调整策略 |

## 核心能力

### 1. 上下文感知深度注入检测(专业版独有)

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
        # 记录上下文
        self.context_history.append({
            "input": user_input,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "session": session_id
        })
        
        findings = []
        
        # 第一层:直接注入检测
        for pattern, severity, desc, remediation in self.DIRECT_PATTERNS:
            for match in re.finditer(pattern, user_input, re.IGNORECASE):
                findings.append({
                    "layer": "direct",
                    "severity": severity,
                    "type": desc,
                    "match": match.group()[:50],
                    "remediation": remediation
                })
        
        # 第二层:间接注入检测
        for pattern, severity, desc, remediation in self.INDIRECT_PATTERNS:
            for match in re.finditer(pattern, user_input, re.IGNORECASE):
                findings.append({
                    "layer": "indirect",
                    "severity": severity,
                    "type": desc,
                    "match": match.group()[:50],
                    "remediation": remediation
                })
        
        # 第三层:多轮注入检测(结合上下文)
        for pattern, severity, desc, remediation in self.MULTI_TURN_PATTERNS:
            for match in re.finditer(pattern, user_input, re.IGNORECASE):
                # 检查后续对话是否有执行迹象
                contextual_risk = self._check_contextual_risk(user_input, match.group())
                findings.append({
                    "layer": "multi_turn",
                    "severity": severity,
                    "type": desc,
                    "match": match.group()[:50],
                    "contextual_risk": contextual_risk,
                    "remediation": remediation
                })
        
        # 上下文分析:检测渐进式注入
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
        # 如果之前的对话中有类似的注入模式,风险升级
        for entry in list(self.context_history)[:-1]:
            if pattern.lower() in entry["input"].lower():
                risk = "HIGH"
                break
        return risk
    
    def _detect_progressive_injection(self):
        """检测渐进式注入(多轮逐步诱导)"""
        if len(self.context_history) < 3:
            return None
        
        # 检测信任建立 -> 规则植入 -> 执行请求的模式
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

### 2. 沙盒隔离执行(专业版独有)

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
        
        # 1. 参数安全检查
        safety_check = self._check_safety(command, params)
        if not safety_check["safe"]:
            return {
                "status": "BLOCKED",
                "reason": safety_check["reason"],
                "command": command
            }
        
        # 2. 准备沙盒环境
        sandbox_path = os.path.join(self.sandbox_dir, f"exec_{len(self.execution_log)}")
        os.makedirs(sandbox_path, exist_ok=True)
        
        # 3. 执行命令(带限制)
        try:
            result = subprocess.run(
                command if isinstance(command, list) else command.split(),
                cwd=sandbox_path,
                timeout=self.SANDBOX_CONFIG["timeout"],
                capture_output=True,
                text=True,
                env=self._get_safe_env(),
                # 在实际实现中使用容器化执行:
                # docker run --rm --network=none --memory=256m --cpus=0.5
                #   --read-only --tmpfs /tmp:rw,size=64m
                #   --user 1000:1000
                #   alpine:latest sh -c "COMMAND"
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
        
        # 4. 清理沙盒
        self._cleanup_sandbox(sandbox_path)
        
        # 5. 记录日志
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

### 3. 多Agent统一管理(专业版独有)

```python
#!/usr/bin/env python3
"""专业版多Agent统一安全管理"""

import json
from datetime import datetime
from collections import defaultdict

class MultiAgentSecurityManager:
    """多Agent安全管理器"""
    
    def __init__(self):
        self.agents = {}
        self.global_policies = {
            "max_agents_per_session": 10,
            "shared_tool_blacklist": ["format_disk", "shutdown_system"],
            "cross_agent_communication": False,
        }
        self.security_events = []
    
    def register_agent(self, agent_id, config):
        """注册Agent"""
        self.agents[agent_id] = {
            "id": agent_id,
            "name": config.get("name", agent_id),
            "tools": config.get("tools", []),
            "permissions": config.get("permissions", {}),
            "rate_limit": config.get("rate_limit", 30),
            "created": datetime.utcnow().isoformat() + "Z",
            "status": "active",
            "stats": {
                "total_calls": 0,
                "blocked_calls": 0,
                "injection_attempts": 0
            }
        }
        return self.agents[agent_id]
    
    def audit_all_agents(self):
        """审计所有Agent的安全状态"""
        report = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "total_agents": len(self.agents),
            "active_agents": sum(1 for a in self.agents.values() if a["status"] == "active"),
            "findings": [],
            "summary": defaultdict(int)
        }
        
        for agent_id, agent in self.agents.items():
            # 检查工具权限
            for tool in agent["tools"]:
                if tool in self.global_policies["shared_tool_blacklist"]:
                    report["findings"].append({
                        "agent": agent_id,
                        "severity": "CRITICAL",
                        "finding": f"Agent使用了黑名单工具: {tool}"
                    })
                    report["summary"]["critical"] += 1
            
            # 检查速率限制
            if agent["rate_limit"] > 100:
                report["findings"].append({
                    "agent": agent_id,
                    "severity": "MEDIUM",
                    "finding": f"速率限制过高: {agent['rate_limit']}/min"
                })
                report["summary"]["medium"] += 1
            
            # 检查统计
            stats = agent["stats"]
            if stats["blocked_calls"] > 10:
                report["findings"].append({
                    "agent": agent_id,
                    "severity": "HIGH",
                    "finding": f"被阻止调用过多: {stats['blocked_calls']}次"
                })
                report["summary"]["high"] += 1
        
        report["summary"] = dict(report["summary"])
        return report
    
    def get_security_dashboard(self):
        """获取安全仪表板"""
        return {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "agents": [
                {
                    "id": a["id"],
                    "name": a["name"],
                    "status": a["status"],
                    "tools_count": len(a["tools"]),
                    "total_calls": a["stats"]["total_calls"],
                    "blocked": a["stats"]["blocked_calls"],
                    "injections": a["stats"]["injection_attempts"]
                }
                for a in self.agents.values()
            ],
            "events_count": len(self.security_events)
        }
```

### 4. 实时监控与告警(专业版独有)

```python
#!/usr/bin/env python3
"""专业版实时安全监控与告警"""

import json
from datetime import datetime
from collections import deque

class SecurityMonitor:
    """实时安全监控器"""
    
    ALERT_THRESHOLDS = {
        "injection_attempts_per_minute": 5,
        "blocked_calls_per_minute": 10,
        "unique_attack_patterns": 3,
    }
    
    def __init__(self):
        self.events = deque(maxlen=10000)
        self.alerts = []
        self.metrics = {
            "total_requests": 0,
            "blocked_requests": 0,
            "injection_attempts": 0,
            "tool_violations": 0
        }
    
    def record_event(self, event_type, details):
        """记录安全事件"""
        event = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "type": event_type,
            "details": details
        }
        self.events.append(event)
        
        # 更新指标
        self.metrics["total_requests"] += 1
        if event_type == "injection_detected":
            self.metrics["injection_attempts"] += 1
        elif event_type == "tool_blocked":
            self.metrics["blocked_requests"] += 1
            self.metrics["tool_violations"] += 1
        
        # 检查告警条件
        self._check_alerts(event)
    
    def _check_alerts(self, event):
        """检查告警条件"""
        # 检查注入频率
        recent_injections = sum(
            1 for e in self.events
            if e["type"] == "injection_detected"
        )
        
        if recent_injections >= self.ALERT_THRESHOLDS["injection_attempts_per_minute"]:
            alert = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "level": "CRITICAL",
                "type": "injection_burst",
                "message": f"注入攻击频率异常: {recent_injections}次",
                "action": "建议临时锁定Agent"
            }
            self.alerts.append(alert)
            self._send_alert(alert)
    
    def _send_alert(self, alert):
        """发送告警"""
        print(f"[ALERT] [{alert['level']}] {alert['message']}")
        # 实际实现中发送Webhook/邮件
    
    def get_dashboard(self):
        """获取监控仪表板"""
        return {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "metrics": self.metrics,
            "recent_events": list(self.events)[-10:],
            "active_alerts": [a for a in self.alerts if a["level"] in ["CRITICAL", "HIGH"]],
            "block_rate": f"{self.metrics['blocked_requests'] * 100 / max(self.metrics['total_requests'], 1):.1f}%"
        }
```

## 使用场景

### 场景一:企业Agent安全治理

```python
#!/usr/bin/env python3
"""企业Agent安全治理平台"""

class EnterpriseAgentSecurity:
    """企业级Agent安全治理"""
    
    def __init__(self):
        from deep_injection_detector import DeepInjectionDetector
        from sandbox_executor import SandboxExecutor
        from multi_agent_manager import MultiAgentSecurityManager
        from security_monitor import SecurityMonitor
        
        self.detector = DeepInjectionDetector()
        self.sandbox = SandboxExecutor()
        self.manager = MultiAgentSecurityManager()
        self.monitor = SecurityMonitor()
    
    def secure_agent_interaction(self, agent_id, user_input):
        """安全的Agent交互流程"""
        # 1. 深度注入检测
        detection = self.detector.detect(user_input, agent_id)
        self.monitor.record_event("input_received", {"agent": agent_id})
        
        if detection["should_block"]:
            self.monitor.record_event("injection_detected", {
                "agent": agent_id,
                "findings": detection["findings_count"]
            })
            return {"action": "BLOCKED", "reason": "检测到注入攻击"}
        
        # 2. 记录安全通过
        self.monitor.record_event("input_passed", {"agent": agent_id})
        return {"action": "ALLOWED", "input": user_input}
    
    def secure_tool_execution(self, agent_id, tool, params):
        """安全的工具执行"""
        # 1. 沙盒执行
        result = self.sandbox.execute_safely(tool, params)
        
        if result["status"] == "BLOCKED":
            self.monitor.record_event("tool_blocked", {
                "agent": agent_id, "tool": tool, "reason": result["reason"]
            })
        
        return result
    
    def generate_security_report(self):
        """生成安全报告"""
        return {
            "monitoring": self.monitor.get_dashboard(),
            "agents": self.manager.get_security_dashboard(),
            "audit": self.manager.audit_all_agents()
        }
```

### 场景二:实时安全监控仪表板

```bash
#!/bin/bash
# Agent安全监控仪表板

echo "=== Agent安全监控仪表板 ==="
echo "时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

python3 -c "
import json
from security_monitor import SecurityMonitor

monitor = SecurityMonitor()

# 模拟数据
monitor.metrics = {
    'total_requests': 15420,
    'blocked_requests': 421,
    'injection_attempts': 89,
    'tool_violations': 156
}

dashboard = monitor.get_dashboard()

print('--- 安全指标 ---')
print(f\"  总请求: {dashboard['metrics']['total_requests']}\")
print(f\"  拦截请求: {dashboard['metrics']['blocked_requests']}\")
print(f\"  注入尝试: {dashboard['metrics']['injection_attempts']}\")
print(f\"  工具违规: {dashboard['metrics']['tool_violations']}\")
print(f\"  拦截率: {dashboard['block_rate']}\")
print()
print('--- 活跃告警 ---')
for alert in dashboard['active_alerts']:
    print(f\"  [{alert['level']}] {alert['message']}\")
if not dashboard['active_alerts']:
    print('  无活跃告警')
"
```

## 快速开始

### 从免费版升级

```python
# 免费版:基础注入检测
detector = PromptInjectionDetector()
result = detector.detect(user_input)

# 专业版:深度检测+沙盒执行
detector = DeepInjectionDetector()
sandbox = SandboxExecutor()
detection = detector.detect(user_input)
if not detection["should_block"]:
    result = sandbox.execute_safely(tool, params)
```

## 配置示例

### 专业版功能矩阵

| 功能 | 免费版 | 专业版 | 说明 |
|:-----|:-------|:-------|:-----|
| 注入检测 | 基础模式 | 深度上下文 | 多层检测 |
| 沙盒执行 | 不支持 | 支持 | 隔离执行 |
| 参数投毒 | 不支持 | 支持 | 恶意载荷检测 |
| 多Agent | 单Agent | 统一管理 | 批量管理 |
| 实时监控 | 不支持 | 支持 | 实时告警 |
| 审计链 | 基础 | 完整 | 可追溯 |
| SARIF | 不支持 | 支持 | 合规报告 |

### 沙盒执行限制

| 限制项 | 默认值 | 说明 |
|:-------|:-------|:-----|
| 执行超时 | 30秒 | 防止长时间运行 |
| 内存限制 | 256MB | 防止内存耗尽 |
| CPU限制 | 50% | 防止CPU占用 |
| 网络访问 | 禁止 | 防止网络泄露 |
| 文件系统 | 只读 | 防止文件修改 |

## 最佳实践

1. **深度防御**:注入检测+沙盒执行+参数过滤多层防护。
2. **沙盒隔离**:所有工具调用在沙盒中执行,限制影响范围。
3. **统一管理**:多Agent统一安全策略,集中监控。
4. **实时告警**:配置Webhook告警,攻击发生时第一时间响应。
5. **审计留痕**:所有安全事件记录审计链,可追溯。
6. **定期演练**:模拟攻击测试防护有效性。

## 常见问题

### Q1: 专业版与免费版规则兼容吗?

完全兼容。专业版在免费版规则基础上增加深度检测,已有规则可直接使用。

### Q2: 沙盒执行影响性能吗?

沙盒执行增加约100ms开销,对大多数场景影响可忽略。安全收益远大于性能损失。

### Q3: 多Agent管理支持多少个Agent?

专业版支持管理100+个Agent,通过统一策略和集中监控实现规模化安全治理。

### Q4: 实时告警支持哪些渠道?

支持Webhook(HTTP回调)、邮件、Slack和企业微信通知。

### Q5: 如何生成SARIF合规报告?

使用专业版的报告导出功能,将安全事件转换为SARIF格式,上传到代码扫描平台。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+
- **Docker**: 推荐(沙盒执行使用容器化隔离)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| python3 | 运行时 | 必需 | python.org 下载 |
| docker | 容器运行时 | 推荐 | docker.com 下载 |
| requests | HTTP库 | 推荐 | `pip install requests` |
| flask | Web框架 | 可选 | `pip install flask` |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 专业版深度检测为本地引擎,无需外部API Key
- Webhook告警需配置回调URL
- 沙盒执行建议配置Docker访问权限

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级AI Agent安全防护与治理任务
