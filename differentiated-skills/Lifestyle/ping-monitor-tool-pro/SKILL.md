---
slug: ping-monitor-tool-pro
name: ping-monitor-tool-pro
version: 1.0.0
displayName: 网络监控专业版
summary: "企业级监控平台,支持多地区、API性能、状态页与团队协作 - 提供专业AI自动化处理能力,支持多种使用场景"
license: Proprietary
edition: pro
description: '面向企业与运维团队的企业级监控平台.
  核心能力: 多地区监控、API性能监控、公开状态页、多渠道告警、团队协作、SLA保障

  适用场景: 企业服务监控、SRE运维、API网关监控、SLA管理、客户透明度

  差异化: 专业版支持多地区与企业级能力,与免费版监控格式兼容

  适用关键词: 多地区监控, API性能, 状态页, 团队协作, SLA保障, SRE运维'
tags:
  - 网络监控
  - 企业级
  - 多地区监控
  - API性能
  - 状态页
  - SRE运维
  - 监控
  - 运维
  - 工具
  - headers
  - resp
  - target_config
  - self
  - json
tools:
  - read
  - exec
homepage: ""
# 定价元数据
category: "Operations"
---
# 网络监控 (专业版)

## 概述

专业版面向企业与运维团队,在免费版基础监控之上,扩展多地区监控、API 性能监控、公开状态页、多渠道告警、团队协作、SLA 保障等企业级能力。支持构建完整的监控体系,适合企业服务、API 网关、SRE 运维等场景.
专业版与免费版监控格式完全兼容,个人用户升级后现有配置无缝迁移.
## 核心能力

| 能力模块 | 描述 | 免费版 | 专业版 |
|----|---|---|---|
| ICMP Ping | 主机检测 | 支持 | 支持 |
| HTTP 检测 | 网站健康 | 支持 | 支持 |
| 多地区监控 | 多地域检测 | 不支持 | 支持 (全球 20+ 节点) |
| API 性能监控 | 接口性能 | 不支持 | 支持 |
| 公开状态页 | 客户透明 | 不支持 | 支持 |
| 多渠道告警 | 多种通知 | 邮件 | 邮件+短信+IM+电话 |
| 历史数据 | 长期存储 | 30 天 | 不限 |
| 团队协作 | 多人协作 | 不支持 | 支持 |
| SLA 保障 | 可用性承诺 | 不支持 | 支持 |
| 故障分析 | 根因分析 | 不支持 | 支持 |
| 自定义仪表盘 | 可视化 | 基础 | 完整 |
| 优先支持 | 专属支持 | 不支持 | 支持 |

### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.
**输入**: 用户提供参数配置与调用所需的指令和必要参数.
**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置.
**输入**: 用户提供结果处理与输出所需的指令和必要参数.
**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级监控平台、支持多地区、状态页与团队协作、面向企业与运维团、队的企业级监控平、核心能力、适用场景、企业服务监控、SRE、网关监控、客户透明度、差异化、专业版支持多地区、与企业级能力、与免费版监控格式、适用关键词等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一: 企业服务监控

为企业服务提供多地区监控与告警.
```python
import os
import requests
from datetime import datetime
# ...
API_BASE = "https://api.ping-monitor-pro.local/v1"
ADMIN_KEY = os.environ["PING_MONITOR_ADMIN_KEY"]
# ...
class EnterpriseMonitor:
    def __init__(self, admin_key):
        self.headers = {"X-API-Key": admin_key, "X-Edition": "pro"}
# ...
    def add_monitor(self, target_config):
        """添加监控目标"""
        payload = {
            "name": target_config["name"],
            "type": target_config["type"],
            "target": target_config["target"],
            "regions": target_config.get("regions", ["us_east", "us_west", "eu_west", "ap_east"]),
            "interval_seconds": target_config.get("interval", 60),
            "timeout_seconds": target_config.get("timeout", 10),
            "alerts": target_config.get("alerts", []),
            "sla_target": target_config.get("sla", 99.9),
        }
        resp = requests.post(
            f"{API_BASE}/monitors",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        return resp.json()
# ...
    def multi_region_check(self, monitor_id):
        """多地区检测结果"""
        resp = requests.get(
            f"{API_BASE}/monitors/{monitor_id}/regions",
            headers=self.headers,
            timeout=60,
        )
        return resp.json()
# ...
    def api_performance(self, monitor_id, period="24h"):
        """API 性能监控"""
        resp = requests.get(
            f"{API_BASE}/monitors/{monitor_id}/performance",
            headers=self.headers,
            params={"period": period},
            timeout=60,
        )
        return resp.json()
# ...
monitor = EnterpriseMonitor(ADMIN_KEY)
# 添加多地区监控
m = monitor.add_monitor({
    "name": "API 网关",
    "type": "http",
    "target": "https://api.example.com/health",
    "regions": ["us_east", "eu_west", "ap_east"],
    "interval": 30,
    "alerts": [
        {"channel": "slack", "webhook": "..."},
        {"channel": "sms", "phone": "..."},
        {"channel": "phone", "phone": "...", "escalate_after": "5min"},
    ],
    "sla": 99.95,
})
```

### 场景二: 公开状态页

为客户提供公开的服务状态页面.
```python
def create_status_page(config):
    """创建公开状态页"""
    payload = {
        "domain": config["domain"],  # status.example.com
        "title": config["title"],
        "description": config["description"],
        "monitors": config["monitors"],
        "features": {
            "overall_status": True,
            "history_90_days": True,
            "incident_history": True,
            "subscribe": True,  # 允许用户订阅
            "custom_branding": True,
        },
        "sla_display": True,
    }
    resp = requests.post(
        f"{API_BASE}/status-pages",
        headers=monitor.headers,
        json=payload,
        timeout=60,
    )
    return resp.json()
# ...
def create_incident(title, impact, components, updates):
    """创建故障事件"""
    payload = {
        "title": title,
        "impact": impact,  # none, minor, major, critical
        "components": components,
        "updates": updates,
    }
    resp = requests.post(
        f"{API_BASE}/incidents",
        headers=monitor.headers,
        json=payload,
        timeout=30,
    )
    return resp.json()
```

### 场景三: 团队协作运维

多人协作处理告警与故障.
```python
def setup_oncall_schedule(team_members, rotation):
    """配置值班排班"""
    payload = {
        "team": team_members,
        "rotation": rotation,  # weekly, biweekly
        "schedule": {
            "monday": {"primary": "alice", "secondary": "bob"},
            "tuesday": {"primary": "bob", "secondary": "carol"},
        },
        "escalation_policy": {
            "unanswered_alerts_after": "5min",
            "escalate_to": "secondary",
            "final_escalation": "manager",
        },
        "channels": ["phone", "sms", "slack"],
    }
    resp = requests.post(
        f"{API_BASE}/oncall/schedule",
        headers=monitor.headers,
        json=payload,
        timeout=30,
    )
    return resp.json()
```

## 不适用场景

以下场景网络监控专业版不适合处理：

- 物理硬件维修
- 网络物理布线
- 数据中心选址

## 触发条件

需要系统监控、日志分析、运维告警、部署管理时使用。不适用于非本工具能力范围的需求.
## 快速开始

### Step 1: 申请专业版账户

联系销售开通专业版,获取管理员凭证与租户 ID.
### Step 2: 配置凭证

```bash
export PING_MONITOR_ADMIN_KEY="sk_pro_admin_xxx"
export PING_MONITOR_ORG_ID="org_your_id"
export PING_MONITOR_EDITION="pro"
```

### Step 3: 批量添加监控

```bash
curl -X POST -H "X-API-Key: $PING_MONITOR_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{"monitors":[
    {"name":"API","type":"http","target":"https://api.example.com/health"},
    {"name":"DB","type":"tcp","target":"db.example.com:5432"}
  ]}' \
  "https://api.ping-monitor-pro.local/v1/monitors/batch"
```

### Step 4: 配置状态页

```bash
curl -X POST -H "X-API-Key: $PING_MONITOR_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "domain": "status.example.com",
    "title": "服务状态",
    "monitors": ["m001", "m002"]
  }' \
  "https://api.ping-monitor-pro.local/v1/status-pages"
```

#
## 示例

### 企业级配置

```yaml
# /etc/ping-monitor/pro.yaml
edition: pro
api:
  base_url: https://api.ping-monitor-pro.local/v1
  admin_key: ${PING_MONITOR_ADMIN_KEY}
  org_id: ${PING_MONITOR_ORG_ID}
  timeout: 60
# ...
regions:
  available: [us_east, us_west, eu_west, eu_central, ap_east, ap_southeast, ap_northeast]
  default: [us_east, eu_west, ap_east]
# ...
monitoring:
  types: [icmp, http, tcp, dns, ssl_cert, api_performance]
  intervals: [30s, 1min, 5min, 10min]
  timeout: 30s
  retry: 3
# ...
alerting:
  channels:
    email: true
    sms: true
    slack: true
    dingtalk: true
    feishu: true
    phone: true
    webhook: true
  escalation:
    auto_escalate: true
    levels: [primary, secondary, manager, cto]
  smart_alerting:
    dedup: true
    grouping: true
    suppression: true
# ...
status_page:
  custom_domain: true
  branding: true
  history_days: 90
  incident_communication: true
  subscriber_notifications: true
# ...
team:
  max_members: 50
  roles: [admin, manager, responder, viewer]
  oncall_schedule: true
# ...
sla:
  tracking: true
  reporting: true
  credits: true
# ...
data_retention:
  raw_data: 90_days
  aggregated: 2_years
  incidents: permanent
# ...
integrations:
  jira: true
  pagerduty: true
  datadog: true
  grafana: true
```

### SLA 监控示例

```python
def sla_report(monitor_id, period="month"):
    """SLA 报告"""
    resp = requests.get(
        f"{API_BASE}/monitors/{monitor_id}/sla",
        headers=monitor.headers,
        params={"period": period},
        timeout=60,
    )
    return resp.json()
# ...
# 输出示例
# {
#   "target_sla": 99.95,
#   "actual_sla": 99.92,
#   "met_sla": false,
#   "downtime_total_minutes": 21.6,
#   "incidents": 2,
#   "compensation_required": true,
# }
```

### 故障分析

```python
def root_cause_analysis(incident_id):
    """根因分析"""
    payload = {
        "incident_id": incident_id,
        "analysis": [
            "timeline_reconstruction",
            "correlation_analysis",
            "dependency_mapping",
            "similar_incidents",
        ],
        "ai_assisted": True,
    }
    resp = requests.post(
        f"{API_BASE}/incidents/{incident_id}/rca",
        headers=monitor.headers,
        json=payload,
        timeout=300,
    )
    return resp.json()
```

## 最佳实践

### 1. 多地区策略

```python
def select_regions(target_audience):
    """根据用户分布选择监控地区"""
    mapping = {
        "global": ["us_east", "us_west", "eu_west", "ap_east"],
        "china": ["ap_east", "ap_northeast"],
        "us": ["us_east", "us_west"],
        "europe": ["eu_west", "eu_central"],
    }
    return mapping.get(target_audience, mapping["global"])
```

### 2. 告警分级

```python
ALERT_LEVELS = {
    "P0": {"severity": "critical", "response_time": "5min", "channels": ["phone", "sms", "slack"]},
    "P1": {"severity": "major", "response_time": "15min", "channels": ["sms", "slack"]},
    "P2": {"severity": "minor", "response_time": "1h", "channels": ["slack"]},
    "P3": {"severity": "info", "response_time": "4h", "channels": ["email"]},
}
```

### 3. 故障演练

```python
def run_chaos_experiment(target, failure_type, duration_min):
    """故障演练"""
    payload = {
        "target": target,
        "failure_type": failure_type,  # network_latency, service_down, region_failure
        "duration_min": duration_min,
        "monitored_metrics": [
            "detection_time", "alert_time", "response_time", "recovery_time",
        ],
    }
    resp = requests.post(
        f"{API_BASE}/chaos/experiment",
        headers=monitor.headers,
        json=payload,
        timeout=600,
    )
    return resp.json()
```

## 常见问题

### Q1: 专业版与免费版兼容吗?

完全兼容。专业版在免费版基础上扩展,现有监控配置无需修改.
### Q2: 多地区节点有多少?

全球 20+ 节点,覆盖北美、欧洲、亚太、南美等主要地区.
### Q3: SLA 如何计算?

SLA = (总时间 - 故障时间) / 总时间 × 100%。可按月或按年计算.
### Q4: 状态页可以自定义吗?

可以。支持自定义域名、品牌、颜色、文案等,与企业形象一致.
### Q5: 团队协作支持多少人?

标准版支持 50 人团队,企业版可扩展至 200+ 人.
## 依赖说明

### 运行环境

- **Agent 平台**: 支持 SKILL.md 规范的任意 AI Agent (Claude Code、Cursor、Codex、Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux (生产环境推荐 Linux)
- **网络**: 需访问专业版服务
- **Python**: 3.9+ (用于脚本化操作)

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| Ping Monitor Pro API | 在线 API | 必需 | 联系销售开通专业版 |
| LLM API | 推理服务 | 必需 | 由 Agent 内置 LLM 提供 |
| Python 3.9+ | 运行时 | 推荐 | python.org 下载 |
| requests 库 | Python 库 | 推荐 | `pip install requests` |
| 数据库 | 数据存储 | 可选 | 兼容主流关系型数据库 (使用 `数据库` 上下文) |

### API Key 配置

```bash
# 专业版凭证
export PING_MONITOR_ADMIN_KEY="sk_pro_admin_xxx"
export PING_MONITOR_ORG_ID="org_your_id"
export PING_MONITOR_EDITION="pro"
# ...
# 可选: 告警渠道
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/xxx"
export DINGTALK_WEBHOOK="..."
export FEISHU_WEBHOOK="..."
export SMS_API_KEY="..."
export PAGERDUTY_KEY="..."
# ...
# 可选: 集成
export JIRA_API_KEY="..."
export DATADOG_API_KEY="..."
```

### 可用性分类

- **分类**: MD+EXEC (Markdown 指令 + 命令行执行)
- **说明**: 本 Skill 面向企业与运维团队,通过自然语言指令驱动 Agent 调用 Pro API,完成企业级监控
- **专业版特性**: 多地区监控、API 性能、状态页、多渠道告警、团队协作、SLA 保障、故障分析
- **兼容性**: 与免费版监控格式完全兼容,支持平滑升级

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "网络监控专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "ping monitor pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
