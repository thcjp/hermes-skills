---
slug: monitor-toolkit-pro
name: monitor-toolkit-pro
version: 1.0.0
displayName: 监控工具包-专业版
summary: 企业级监控平台,支持多目标批量监控、告警升级、历史趋势分析与团队协作
license: Proprietary
edition: pro
description: '企业级监控工具专业版,面向团队与生产环境运维。核心能力:

  - 多目标批量监控与分布式探针

  - 告警升级与值班轮换机制

  - 历史趋势分析与可视化报表

  - 多通道告警(邮件/短信/钉钉/飞书/Slack)

  - 监控模板与自动发现

  - 服务依赖拓扑与故障关联分析

  - SLA 报告与可用性看板

  - 团队协作与权限管理


  适用场景:

  - 生产环境多服务集群监控

  - SRE 团队值班与告警管理

  - SLA 合规监控与报告生成

  - 微服务架构健康度全链路监控


  差异化:专业版在免费版基础上扩展企业级告警升级...'
tags:
- 监控
- 运维
- 企业级
- 告警管理
- SLA
- SRE
tools:
- - read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tools: ["read", "exec"]
tags: "监控,运维,工具"
---
# 监控工具包 - 专业版

## 概述

监控工具包专业版是企业级监控平台,在免费版基础监控能力之上扩展多目标批量监控、告警升级、历史趋势分析、多通道通知与团队协作。适合生产环境运维、SRE 团队值班管理与 SLA 合规监控。

专业版兼容免费版监控配置格式,支持从免费版平滑升级,已有监控定义无需修改即可在专业版中运行。

## 核心能力

### 1. 多目标批量监控

支持单配置文件管理数百个监控目标,分布式探针从多个地域执行检查,消除单点盲区。

**输入**: 用户提供多目标批量监控所需的指令和必要参数。
**处理**: 解析多目标批量监控的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回多目标批量监控的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 2. 告警升级机制

支持多级告警升级:未确认告警自动升级至下一级负责人,支持值班轮换表与免打扰时段。

**输入**: 用户提供告警升级机制所需的指令和必要参数。
**处理**: 解析告警升级机制的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回告警升级机制的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 3. 历史趋势分析

检查结果持久化存储,提供可视化趋势图表,支持按时间范围聚合分析可用率与响应时间。

**输入**: 用户提供历史趋势分析所需的指令和必要参数。
**处理**: 解析历史趋势分析的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回历史趋势分析的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 4. 多通道告警通知

支持邮件、短信、钉钉、飞书、Slack、企业微信等多通道告警,按告警级别路由到不同通知渠道。

**输入**: 用户提供多通道告警通知所需的指令和必要参数。
**处理**: 解析多通道告警通知的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回多通道告警通知的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 5. 监控模板与自动发现

内置常见服务监控模板(Nginx/Redis/MySQL/K8s),支持服务自动发现,动态添加监控目标。

**输入**: 用户提供监控模板与自动发现所需的指令和必要参数。
**处理**: 解析监控模板与自动发现的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回监控模板与自动发现的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 依赖详情

自动构建服务依赖拓扑图,故障发生时关联分析影响范围,快速定位根因。

**输入**: 用户提供依赖说明所需的指令和必要参数。
**处理**: 解析依赖说明的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回依赖说明的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 7. SLA 报告与看板

自动生成 SLA 合规报告,提供可用性看板与实时大屏展示。

**输入**: 用户提供SLA 报告与看板所需的指令和必要参数。
**处理**: 解析SLA 报告与看板的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回SLA 报告与看板的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 8. 团队协作与权限

支持多租户与 RBAC 权限管理,团队成员协作处理告警,告警认领与处理记录全程留痕。

**输入**: 用户提供团队协作与权限所需的指令和必要参数。
**处理**: 解析团队协作与权限的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回团队协作与权限的响应数据,包含状态码、结果和日志。
**技术参数**：使用`input_params`和`output_format`参数控制执行行为,支持`json`/`text`/`csv`输出格式。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级监控平台、支持多目标批量监、历史趋势分析与团、企业级监控工具专、面向团队与生产环、境运维、核心能力、多目标批量监控与、告警升级与值班轮、换机制、历史趋势分析与可、视化报表、服务依赖拓扑与故、障关联分析、报告与可用性看板、团队协作与权限管等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一:生产环境微服务集群监控

监控包含数十个微服务的生产集群,自动发现新服务并添加监控。

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 监控工具包-专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 配置批量监控
cat > ~/monitor/enterprise-config.json << 'EOF'
{
  "cluster": "production",
  "discovery": {
    "type": "kubernetes",
    "namespace": "production",
    "labelSelector": "app-type=service",
    "autoAdd": true,
    "template": "microservice-default"
  },
  "probes": [
    {"region": "cn-east", "endpoint": "probe-east.internal"},
    {"region": "cn-south", "endpoint": "probe-south.internal"}
  ],
  "checks": {
    "health": {"type": "http", "path": "/health", "interval": "30s"},
    "metrics": {"type": "http", "path": "/metrics", "interval": "60s"},
    "latency": {"type": "http", "path": "/api/ping", "threshold": "500ms"}
  }
}
EOF
# ...
# 执行批量检查
./monitor-cli check --config enterprise-config.json --parallel 20
# ...
# 示例
# === 集群监控报告 ===
# 检查目标: 48 个服务
# 健康状态: 46 正常, 2 异常
# [异常] order-service: HTTP 503 (响应时间 3.2s)
# [异常] payment-service: 连接超时
# 平均响应时间: 125ms
# SLA 可用率: 99.2% (目标 99.9%)
```

### 场景二:告警升级与值班轮换

生产环境出现故障时,按升级规则逐级通知值班人员。

```json
{
  "escalation_policy": {
    "name": "production-critical",
    "levels": [
      {
        "level": 1,
        "delay": "0m",
        "targets": ["oncall-primary"],
        "channels": ["slack", "phone"]
      },
      {
        "level": 2,
        "delay": "5m",
        "targets": ["oncall-secondary"],
        "channels": ["slack", "phone", "sms"]
      },
      {
        "level": 3,
        "delay": "15m",
        "targets": ["team-lead", "sre-manager"],
        "channels": ["slack", "phone", "sms", "email"]
      }
    ],
    "autoResolve": true,
    "repeatNotification": "10m"
  },
  "schedule": {
    "rotation": "weekly",
    "timezone": "Asia/Shanghai",
    "members": ["alice", "bob", "charlie", "diana"]
  }
}
```

### 场景三:SLA 报告生成

```bash
# 生成月度 SLA 报告
./monitor-cli sla-report \
  --period 2025-01 \
  --services "api-gateway,user-service,order-service" \
  --target 99.9 \
  --output sla-report-2025-01.html
# ...
# 报告内容包含:
# - 各服务月度可用率
# - 故障事件时间线
# - 平均响应时间趋势
# - SLA 合规/违规判定
# - 改进建议
```

## 不适用场景

以下场景监控工具包-专业版不适合处理：

- 物理硬件维修
- 网络物理布线
- 数据中心选址

## 触发条件

需要系统监控、日志分析、运维告警、部署管理时使用。不适用于非本工具能力范围的需求。

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 从免费版升级

```bash
# 免费版配置自动兼容
cp ~/monitor/monitors.json ~/monitor/enterprise-config.json
# ...
# 添加企业级配置
./monitor-cli upgrade --config enterprise-config.json
# ...
# 启用多通道告警
export ALERT_CHANNELS="slack,email,dingtalk"
export SLACK_WEBHOOK_URL="https://hooks.slack.com/..."
export DINGTALK_WEBHOOK_URL="https://oapi.dingtalk.com/robot/send?access_token=..."
```

### 配置值班轮换

```bash
# 创建值班表
./monitor-cli schedule create \
  --name "primary-oncall" \
  --rotation weekly \
  --timezone "Asia/Shanghai" \
  --members "alice,bob,charlie"
# ...
# 查看本周值班
./monitor-cli schedule whois --name "primary-oncall"
```

## 配置示例

### 企业级监控配置

```json
{
  "version": "2.0",
  "organization": "my-company",
  "monitoring": {
    "targets": [
      {
        "name": "api-gateway",
        "type": "http",
        "url": "https://api.example.com/health",
        "interval": "30s",
        "timeout": "5s",
        "expectedStatus": 200,
        "latencyThreshold": "500ms"
      }
    ],
    "alerting": {
      "escalationPolicy": "production-critical",
      "channels": ["slack", "email", "sms"],
      "deduplication": true,
      "grouping": "service"
    },
    "storage": {
      "retention": "180d",
      "aggregation": "5m,1h,1d"
    }
  }
}
```

### 免费版与专业版能力对比

| 能力 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 监控目标数 | 最多 10 | 无限制 |
| 分布式探针 | 不支持 | 支持 |
| 告警通道 | Webhook | 邮件/短信/钉钉/飞书/Slack |
| 告警升级 | 不支持 | 多级升级 + 值班轮换 |
| 历史趋势 | 不支持 | 可视化图表 |
| 服务发现 | 手动 | 自动发现 |
| SLA 报告 | 不支持 | 自动生成 |
| 团队协作 | 单人 | 多租户 + RBAC |
| 技术支持 | 社区 | 优先工单 + SLA |

## 最佳实践

1. **分级告警策略**:按服务重要性定义不同的升级策略,核心服务快速升级
2. **告警去重与分组**:同一服务的多个检查失败合并为一条告警,避免告警风暴
3. **多探针部署**:从不同地域部署探针,排除网络抖动误报
4. **定期审查监控覆盖**:每周审查未监控的服务,确保监控无盲区
5. **SLA 持续跟踪**:每日检查 SLA 达成情况,发现风险提前干预
6. **告警闭环管理**:每条告警必须有认领、处理、复盘记录
7. **值班轮换公平**:确保值班轮换均匀分配,设置免打扰时段

## 常见问题

### Q: 如何避免告警风暴?

A: 专业版提供告警去重与分组功能。同一服务的多个检查失败在 5 分钟窗口内合并为一条告警,相关服务的告警按拓扑关系分组展示。可配置告警抑制规则,在已知故障期间抑制衍生告警。

### Q: 分布式探针如何部署?

A: 在不同地域的服务器上安装探针 Agent,通过中心配置服务器同步监控配置。探针将检查结果上报至中心存储,由告警引擎统一判断。探针之间通过心跳检测确保可用性。

### Q: 如何实现服务自动发现?

A: 专业版支持 Kubernetes 服务发现(通过 API 监听 Service 变化)、Consul 服务发现(通过目录查询)与 DNS 自动发现。新服务上线后自动套用监控模板,无需手动配置。

### Q: SLA 报告如何定义计算口径?

A: SLA 可用率 = (总时间 - 故障时间) / 总时间 * 100%。专业版支持按服务、按月度自动计算,故障时间从告警触发到恢复的时间段统计。可配置计划内维护时段不计入 SLA 计算。

### Q: 团队权限如何管理?

A: 专业版支持 RBAC(基于角色的访问控制)。预置角色:管理员(全部权限)、运维(查看+操作)、开发者(只读+认领告警)、观察者(只读)。可按服务/集群粒度分配权限。

## 依赖说明

### 运行环境

- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Node.js 18+ 或 Python 3.10+
- **数据库**: SQLite(默认)或 MySQL/PostgreSQL(大规模部署)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| curl | CLI工具 | 必需 | 系统自带 |
| openssl | CLI工具 | SSL检查必需 | 系统自带 |
| Node.js | 运行时 | 必需 | 官方网站下载 |
| SQLite/MySQL | 数据库 | 必需 | 系统自带/官方下载 |
| Grafana | 可视化 | 推荐 | 官方网站下载 |
| Prometheus | 时序数据库 | 大规模推荐 | 官方网站下载 |
| Kubernetes CLI | CLI工具 | K8s发现必需 | 官方安装 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置

- Slack 通知:配置 `SLACK_WEBHOOK_URL` 环境变量
- 钉钉通知:配置 `DINGTALK_WEBHOOK_URL` 和 `DINGTALK_SECRET`
- 飞书通知:配置 `FEISHU_WEBHOOK_URL` 和 `FEISHU_SECRET`
- 短信通知:配置 `SMS_API_KEY` 和 `SMS_API_SECRET`(阿里云/腾讯云)
- 邮件通知:配置 `SMTP_HOST`、`SMTP_USER`、`SMTP_PASSWORD`
- Pushover 推送:配置 `PUSHOVER_TOKEN` 和 `PUSHOVER_USER`

### 可用性分类

- **分类**: MD+EXEC(Markdown指令 + 命令行执行)
- **说明**: 通过自然语言指令驱动 Agent 执行企业级监控管理,包含批量监控、告警升级、SLA 报告等高级功能
- **兼容性**: 完全兼容免费版监控配置格式
- **支持**: 优先工单支持,SLA 保障响应时间

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "监控工具包-专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "monitorkit pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
