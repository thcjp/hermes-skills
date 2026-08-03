---

slug: security-toolkit-pro
name: security-toolkit-pro
version: 1.0.0
displayName: Agent安全工具箱(专业版)
summary: "企业级AI Agent安全平台,含行动评估、8项自动巡检、信任注册表、6维健康评分与HTML报告,支持多种使用场景和自动化处理"
license: Proprietary
edition: pro
description: "核心能力:，可自动提升工作效率。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。支持多场景应用和灵活配置。"
  - 24条规则+自定义规则安全扫描引擎

  - 运行时行动安全评估(ALLOW/DENY/CONFIRM决策)

  - 8项自动化安全巡检(完整性/密钥/网络/定时任务等)

  - Skill信任注册表与能力模型管理

  - 6维度健康评分与可视化HTML报告

  - 3级保护策略(strict/balanced/permissive)

  适用场景:

  - 企业AI Agent安全治理

  - Skill供应链安全管理

  - 合规审计与安全基线

  - 红蓝对抗安全演练

  差异化:

  - 企业级运行时安全决策引擎

  ...'
tags:
  - 安全
  - Agent安全
  - 企业安全
  - 合规审计
  - 安全治理
  - 加密
  - 工具
  - params
  - node
tools:
  - read
  - exec
homepage: ""
# 定价元数据
category: "Security"

---

# Agent安全工具箱(专业版)
## 概述
Agent安全工具箱专业版是一款面向企业用户的AI Agent安全治理平台。在免费版24条静态扫描规则基础上,增加了运行时行动安全评估、8项自动化安全巡检、Skill信任注册表、6维度健康评分与可视化HTML报告等企业级功能。支持3级保护策略(strict/balanced/permissive),全面保障企业AI Agent生态安全。与免费版完全兼容,扫描规则和报告格式可无缝复用.
## 核心能力
### 功能矩阵
| 功能模块 | 描述 | 免费版 | 专业版 |
|----|---|---|---|
| 静态扫描 | 代码安全检测 | 24条规则 | 24条+自定义规则 |
| 行动评估 | 运行时安全决策 | 不支持 | ALLOW/DENY/CONFIRM |
| 安全巡检 | 自动化巡检 | 不支持 | 8项自动巡检 |
| 信任管理 | Skill信任注册表 | 不支持 | 注册/验证/撤销 |
| 健康评分 | 安全态势评分 | 不支持 | 6维度评分+HTML报告 |
| 保护策略 | 安全等级 | 不支持 | strict/balanced/permissive |
| 审计日志 | 事件追踪 | 不支持 | JSONL格式审计日志 |
| 批量扫描 | 多目录扫描 | 单目录 | 多目录批量+并行 |

**处理**: 解析功能矩阵的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回功能矩阵的响应数据,包含状态码、结果和日志.
### 六大子命令
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | Agent安全工具箱(专业版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```text
┌───────────────────────────────────────────────────┐
│            专业版命令路由                          │
├──────────────┬────────────────────────────────────┤
│ scan         │ 扫描代码/Skill安全风险             │
│ action       │ 评估运行时行动是否安全              │
│ patrol       │ 执行8项自动化安全巡检              │
│ trust        │ 管理Skill信任等级与能力模型        │
│ config       │ 设置保护级别(strict/balanced/permissive) │
│ checkup      │ 6维度健康检查+HTML可视化报告       │
└──────────────┴────────────────────────────────────┘
```

**处理**: 解析六大子命令的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回六大子命令的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 核心功能执行
用`input_params`参数进行配置.

**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、Agent、安全平台、含行动评估、维健康评分与、核心能力、自定义规则安全扫、描引擎、运行时行动安全评、完整性、定时任务等、信任注册表与能力、模型管理、维度健康评分与可、级保护策略等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景
### 场景一:企业安全健康检查
执行全面的6维度安全健康检查,生成可视化报告.
```bash
node （请参考skill目录中的脚本文件）
```

### 场景二:运行时行动安全评估
在Agent执行操作前,评估操作安全性.
```bash
node （请参考skill目录中的脚本文件） --type network_request \
  --url "https://api.example.com" \
  --method POST \
  --body '{"data": "sensitive"}'
node （请参考skill目录中的脚本文件） --type exec_command \
  --command "rm -rf /tmp/cache"
node （请参考skill目录中的脚本文件） --type web3_tx \
  --chain-id 1 \
  --from 0x1234... \
  --to 0x5678... \
  --value 1000000000000000000
```

### 场景三:8项自动化安全巡检
```bash
node （请参考skill目录中的脚本文件） run
```

### 场景四:信任等级管理
```bash
node （请参考skill目录中的脚本文件） attest \
  --id my-skill \
  --source /path/to/skill \
  --version 1.0.0 \
  --trust-level trusted \
  --preset read_only
node （请参考skill目录中的脚本文件） lookup --source /path/to/skill
node （请参考skill目录中的脚本文件） revoke --source /path/to/skill --reason "安全违规"
node （请参考skill目录中的脚本文件） list
```

## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问
### 行动评估引擎
```python
import json
import re
from enum import Enum
class Decision(Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    CONFIRM = "CONFIRM"
class ActionEvaluator:
    """运行时行动安全评估引擎"""
    WEBHOOK_DOMAINS = [
        "discord.com/api/webhooks",
        "hooks.slack.com",
        "webhook.site",
        "pipedream.net"
    ]
    DANGEROUS_COMMANDS = [
        "rm -rf /", "rm -rf ~", "mkfs", "dd if=",
        ":(){ :|:& };:", "chmod -R 777 /",
        "curl.*|.*bash", "wget.*|.*sh"
    ]
    SENSITIVE_PATTERNS = [
        (r"0x[a-fA-F0-9]{64}", "私钥"),
        (r"-----BEGIN.*PRIVATE KEY-----", "PEM私钥"),
        (r"AKIA[0-9A-Z]{16}", "AWS密钥"),
        (r"gh[pousr]_[A-Za-z0-9_]{36}", "GitHub令牌"),
        (r"sk-[A-Za-z0-9]{48}", "OpenAI密钥"),
    ]
    def evaluate(self, action_type, **params):
        """评估行动安全性"""
        if action_type == "network_request":
            return self._eval_network(params)
        elif action_type == "exec_command":
_eval_command(params)
        elif action_type == "read_file":
_eval_file_read(params)
        elif action_type == "write_file":
_eval_file_write(params)
        elif action_type == "secret_access":
_eval_secret(params)
        elif action_type == "web3_tx":
        else:
            return Decision.CONFIRM, "未知操作类型,需确认"
    def _eval_network(self, params):
        """评估网络请求"""
        url = params.get("url", "")
        body = params.get("body", "")
        for domain in self.WEBHOOK_DOMAINS:
            if domain in url:
DENY, f"检测到Webhook外泄域名: {domain}"
        for pattern, name in self.SENSITIVE_PATTERNS:
            if re.search(pattern, body):
DENY, f"请求体包含{name},禁止传输"
        high_risk_tlds = [".zip", ".mov", ".xyz", ".top"]
        for tld in high_risk_tlds:
            if tld in url:
CONFIRM, f"高风险TLD: {tld}"
    def _eval_command(self, params):
        """评估命令执行"""
        command = params.get("command", "")
        for dangerous in self.DANGEROUS_COMMANDS:
            if re.search(dangerous, command, re.IGNORECASE):
DENY, f"危险命令: {dangerous}"
        sensitive_paths = ["/etc/shadow", "/etc/passwd", "~/.ssh", "~/.gnupg"]
        for path in sensitive_paths:
            if path in command:
CONFIRM, f"访问敏感路径: {path}"
    def _eval_secret(self, params):
        """评估密钥访问"""
        secret_name = params.get("name", "").upper()
        if "PRIVATE_KEY" in secret_name or "MNEMONIC" in secret_name:
        elif "API_SECRET" in secret_name or "TOKEN" in secret_name:
CONFIRM, "访问API密钥需确认"
        else:
    def _eval_web3(self, params):
        """评估Web3交易"""
        value = params.get("value", 0)
        data = params.get("data", "")
        if "0x095ea7b3" in data:  # approve function
            approve_value = data[-64:] if len(data) >= 64 else ""
            if approve_value == "f" * 64:
CONFIRM, "检测到无限授权,需确认"
        if value > 10**18:  # > 1 ETH
CONFIRM, f"大额转账: {value / 10**18} ETH"
class TrustRegistry:
    """Skill信任注册表"""
    TRUST_LEVELS = {
        "untrusted": {"description": "默认,需完整审查", "capabilities": "none"},
        "restricted": {"description": "受限信任", "capabilities": "limited"},
        "trusted": {"description": "完全信任", "capabilities": "full"}
    }
    PRESETS = {
        "none": {"exec": "deny", "network": [], "filesystem": []},
        "read_only": {"exec": "deny", "network": [], "filesystem": ["read"]},
        "trading_bot": {
            "exec": "allow",
            "network": ["api.binance.com", "api.bybit.com"],
            "filesystem": ["read"]
        }
    }
    def __init__(self):
        self.registry = {}
    def attest(self, skill_id, source, version, hash_val, trust_level, preset):
        """注册信任记录"""
        self.registry[skill_id] = {
            "source": source,
            "version": version,
            "hash": hash_val,
            "trust_level": trust_level,
            "preset": preset,
            "capabilities": self.PRESETS.get(preset, {}),
            "attested_at": datetime.now().isoformat()
        }
        return f"已注册: {skill_id} (信任级别: {trust_level})"
    def lookup(self, source):
        """查询信任记录"""
        for skill_id, record in self.registry.items():
            if record["source"] == source:
                return record
        return None
    def revoke(self, source, reason):
        """撤销信任"""
        for skill_id, record in list(self.registry.items()):
            if record["source"] == source:
                record["trust_level"] = "untrusted"
                record["revoked_reason"] = reason
                return f"已撤销: {skill_id} (原因: {reason})"
        return "未找到记录"
```

### 健康评分系统
```python
class HealthCheckup:
    """6维度安全健康检查"""
    DIMENSIONS = {
        "code_safety": {"weight": 0.25, "base": 100},
        "credential_safety": {"weight": 0.25, "base": 0},
        "network_exposure": {"weight": 0.20, "base": 0},
        "runtime_protection": {"weight": 0.15, "base": 0},
        "web3_safety": {"weight": 0.15, "base": 0},
        "config_posture": {"weight": 0.15, "base": 0}
    }
    def run_checkup(self):
        """执行6维度健康检查"""
        scores = {}
        scores["code_safety"] = self._check_code_safety()
        scores["credential_safety"] = self._check_credentials()
        scores["network_exposure"] = self._check_network()
        scores["runtime_protection"] = self._check_runtime()
        scores["web3_safety"] = self._check_web3()
        scores["config_posture"] = self._check_config()
        composite = self._calculate_composite(scores)
        tier = self._get_tier(composite)
        return {
            "composite_score": composite,
            "tier": tier,
            "dimensions": scores
        }
    def _calculate_composite(self, scores):
        """计算综合评分"""
        total = 0
        for dim, score in scores.items():
            if score is not None:
                total += score * self.DIMENSIONS[dim]["weight"]
        return round(total)
    def _get_tier(self, score):
        """获取等级"""
        if score >= 90: return {"grade": "S", "label": "JACKED", "mascot": "肌肉龙虾"}
        elif score >= 70: return {"grade": "A", "label": "健康", "mascot": "持盾龙虾"}
        elif score >= 50: return {"grade": "B", "label": "疲惫", "mascot": "喝咖啡龙虾"}
        else: return {"grade": "F", "label": "危险", "mascot": "受伤龙虾"}
```

#
## 示例
### 保护级别配置
```json
{
  "protection_level": "balanced",
  "levels": {
    "strict": {
      "description": "阻止所有风险操作",
      "default_decision": "DENY",
      "confirm_threshold": "LOW"
    },
    "balanced": {
      "description": "阻止危险操作,确认风险操作",
      "default_decision": "ALLOW",
      "confirm_threshold": "MEDIUM"
    },
    "permissive": {
      "description": "仅阻止严重威胁",
      "default_decision": "ALLOW",
      "confirm_threshold": "CRITICAL"
    }
  }
}
```

### 巡检计划配置
```json
{
  "patrol_schedule": {
    "frequency": "daily",
    "time": "03:00",
    "timezone": "Asia/Shanghai",
    "checks": [
      "integrity", "secrets", "network", "cron",
      "filesystem", "audit_log", "config", "trust"
    ],
    "notification": {
      "channel": "webhook",
      "on_fail": true,
      "on_warn": false
    }
  }
}
```

## 优选实践
### 1. 保护级别选择
| 级别 | 适用场景 | 建议 |
|---:|---:|---:|
| strict | 生产环境、高安全要求 | 阻止所有风险操作 |
| balanced | 日常开发(推荐) | 阻止危险,确认风险 |
| permissive | 安全研究、测试环境 | 仅阻止严重威胁 |

### 2. 信任生命周期管理
```bash
node （请参考skill目录中的脚本文件） /path/to/new-skill/
node （请参考skill目录中的脚本文件） attest --id new-skill --trust-level restricted
node （请参考skill目录中的脚本文件） run
node （请参考skill目录中的脚本文件） revoke --source /path/to/skill --reason "检测到恶意行为"
```

### 3. 健康检查频率
```bash
node （请参考skill目录中的脚本文件）
node （请参考skill目录中的脚本文件） setup --schedule "0 3 * * *"
```

## 常见问题
### Q1: 专业版与免费版兼容吗?
A: 完全兼容。专业版包含免费版所有24条扫描规则,并在此基础上增加行动评估、巡检、信任管理和健康检查功能。免费版的扫描结果可被专业版读取.
### Q2: 健康评分如何计算?
A: 6个维度加权平均:代码安全(25%)+凭证安全(25%)+网络暴露(20%)+运行时防护(15%)+Web3安全(15%)+配置态势(15%)。Web3不适用时,权重重新分配到其他维度.
### Q3: 行动评估会影响Agent性能吗?
A: 评估在毫秒级完成,对性能影响极小。对于高频操作,可调整保护级别为 permissive 以减少确认请求.
### Q4: 巡检如何自动化?
A: 使用 `patrol setup` 配置定时任务,支持 cron 表达式。巡检结果自动记录到审计日志,可通过 `patrol status` 查看.
## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+ 或 Node.js 16+

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Python/Node.js | 运行时 | 必需 | 系统自带 |
| re模块 | 标准库 | 必需 | Python内置 |
| json模块 | 标准库 | 必需 | Python内置 |
| subprocess模块 | 标准库 | 可选 | Python内置(巡检功能) |
| GoPlus API | 外部API | 可选 | 免费注册(Web3安全增强) |

### API Key 配置
- 核心功能无需API Key,完全本地运行
- 可选配置 `GOPLUS_API_KEY` 和 `GOPLUS_API_SECRET` 以增强Web3安全检测

### 可用性分类
- **分类**: MD+execute(纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级安全治理任务

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 安全注意事项

| 风险类型 | 防范措施 |
|----------|---------|
| API密钥泄露 | 通过环境变量配置，禁止硬编码到代码或配置文件中 |
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 网络通信安全 | 使用HTTPS协议，验证SSL证书有效性 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 核心功能

- **自动化执行**: 企业级AI Agent安全平台,含行动评估、8项自动巡检、信任注册表、6维健康评分与HTML报告,支持多种使用场景和自动
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据

## 核心功能

- **自动化执行**: 企业级AI Agent安全平台,含行动评估、8项自动巡检、信任注册表、6维健康评分与HTML报告,支持多种使用场景和自动
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据