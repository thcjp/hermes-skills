---
slug: v2ray-proxy-tool-pro
name: v2ray-proxy-tool-pro
version: "1.0.0"
displayName: V2Ray代理管理专业版
summary: 多节点切换、定时开关、负载均衡与连接监控，适合团队与企业级代理管理需求。
license: MIT
edition: pro
description: |-
  V2Ray代理管理工具专业版，面向团队与企业的高阶代理管理平台。

  核心能力:
  - 多代理节点管理与智能切换
  - 定时开关与计划任务
  - 负载均衡与故障自动切换
  - 连接质量监控与告警
  - 团队代理配置共享

  适用场景:
  - 团队多人共享代理资源
  - 企业级网络代理统一管理
  - 需要高可用性的代理场景

  差异化: 专业版在免费版核心开关能力之上扩展多节点与自动化，新增负载均衡、监控告警、团队共享等企业级能力，并与免费版命令兼容。

  触发关键词: V2Ray, 多节点, 定时开关, 负载均衡, 故障切换, 连接监控, 团队代理, 企业代理
tags:
- V2Ray
- 代理管理
- 多节点
- 专业版
tools:
- read
- exec
---

# V2Ray代理管理（专业版）

## 概述

专业版在免费版的启动/停止、系统代理配置、自动模式之上，扩展为面向团队与企业的完整代理管理平台。新增多节点切换、定时开关、负载均衡、故障自动切换与连接监控，同时与免费版的命令行语法保持向后兼容。

## 核心能力

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 节点管理 | 单节点 | 多节点 + 智能切换 |
| 开关模式 | 手动 + auto | 手动 + auto + 定时 + 计划 |
| 负载均衡 | 不支持 | 多节点负载均衡 |
| 故障切换 | 不支持 | 自动故障切换 |
| 连接监控 | 基础测试 | 持续监控 + 告警 |
| 团队共享 | 不支持 | 配置共享 + 权限管理 |
| 报告 | 不支持 | 连接质量报告 |
| 端口管理 | 固定端口 | 多端口 + 端口转发 |

## 使用场景

### 场景一：多节点智能切换

团队有多个代理节点，希望根据质量自动选择最优节点。

```bash
# 添加多个节点
v2ray-pro node add --name "节点A-东京" --config ./nodes/tokyo.json
v2ray-pro node add --name "节点B-新加坡" --config ./nodes/singapore.json
v2ray-pro node add --name "节点C-美国" --config ./nodes/us.json

# 智能选择最优节点
v2ray-pro node select --strategy latency

# 输出
# 📊 节点质量检测
# 节点A-东京:    延迟 45ms,  丢包 0.1%
# 节点B-新加坡:  延迟 78ms,  丢包 0.3%
# 节点C-美国:    延迟 156ms, 丢包 0.5%
# ✅ 已切换至: 节点A-东京
```

### 场景二：定时开关与计划任务

根据工作时段自动开关代理。

```bash
# 设置工作时段自动开关
v2ray-pro schedule add \
  --name "work-hours" \
  --on "0 9 * * 1-5" \
  --off "0 18 * * 1-5"

# 输出
# ✅ 计划任务已添加
# 工作日 09:00 自动开启代理
# 工作日 18:00 自动关闭代理

# 查看所有计划任务
v2ray-pro schedule list
```

### 场景三：负载均衡与故障切换

多个节点负载均衡，故障时自动切换。

```bash
# 启用负载均衡
v2ray-pro balance enable \
  --nodes "tokyo,singapore,us" \
  --strategy round-robin \
  --health-check 60

# 故障切换配置
v2ray-pro failover enable \
  --max-retries 3 \
  --cooldown 300 \
  --alert webhook

# 输出
# ✅ 负载均衡已启用
# 节点池: tokyo, singapore, us
# 策略: 轮询
# 健康检查间隔: 60s
# 故障切换: 3次失败后切换，冷却5分钟
```

## 快速开始

```bash
# 1. 初始化专业版工作区
v2ray-pro init --workspace ~/v2ray-pro

# 2. 添加节点
v2ray-pro node add --name "主节点" --config ./nodes/main.json

# 3. 开启代理（兼容免费版命令）
v2ray-pro on

# 4. 智能切换节点
v2ray-pro node select --strategy latency

# 5. 设置定时开关
v2ray-pro schedule add --name "work" --on "0 9 * * 1-5" --off "0 18 * * 1-5"

# 6. 查看监控
v2ray-pro monitor status
```

## 配置示例

```yaml
# ~/v2ray-pro/config.yaml
edition: pro
proxy:
  default_port: 10808
  timeout: 30
nodes:
  - name: 节点A-东京
    config: ./nodes/tokyo.json
    priority: 1
  - name: 节点B-新加坡
    config: ./nodes/singapore.json
    priority: 2
  - name: 节点C-美国
    config: ./nodes/us.json
    priority: 3
schedule:
  - name: work-hours
    on: "0 9 * * 1-5"
    off: "0 18 * * 1-5"
  - name: nightly-off
    off: "0 23 * * *"
balance:
  enabled: false
  strategy: round-robin
  health_check_interval: 60
failover:
  enabled: true
  max_retries: 3
  cooldown: 300
  alert:
    - console
    - webhook
monitor:
  enabled: true
  metrics: [latency, packet_loss, bandwidth]
  alert_threshold:
    latency: 500
    packet_loss: 0.05
team:
  enabled: false
  config_share: false
report:
  formats: [markdown, json]
  schedule: daily
```

## 节点切换策略

| 策略 | 说明 | 适用场景 |
|:-----|:-----|:---------|
| latency | 选择延迟最低的节点 | 实时交互场景 |
| bandwidth | 选择带宽最大的节点 | 下载/流媒体 |
| round-robin | 轮询切换节点 | 负载均衡 |
| weighted | 按权重分配 | 混合质量节点 |
| manual | 手动指定 | 精确控制 |

## 最佳实践

* 多节点场景建议启用健康检查，及时剔除异常节点。
* 定时开关根据实际工作时段设置，避免代理长期开启。
* 负载均衡策略根据使用场景选择（实时用 latency，下载用 bandwidth）。
* 故障切换的冷却时间建议 5 分钟，避免频繁切换。
* 定期查看监控报告，识别节点质量退化。
* 团队共享配置时注意权限隔离，避免敏感信息泄露。
* 系统代理配置会修改系统网络设置，关闭时务必清除。

## 常见问题

**Q：专业版与免费版的命令兼容吗？**
A：兼容。免费版的 `on`/`off`/`auto`/`status`/`test` 命令在专业版中可直接使用，专业版额外提供 `node`、`schedule`、`balance`、`failover`、`monitor` 等子命令。

**Q：支持多少个节点？**
A：无硬性上限，建议单个配置不超过 20 个节点以保证切换性能。

**Q：定时开关需要额外的服务吗？**
A：需要系统支持 cron 调度（Linux/macOS 自带，Windows 需使用任务计划程序）。

**Q：故障切换如何判断节点故障？**
A：连续健康检查失败达到 max-retries 次时判定为故障，自动切换至下一优先级节点。

**Q：监控数据存储在哪里？**
A：所有监控数据存储在本地 `~/v2ray-pro/data` 目录，不上传至第三方服务器。

**Q：团队共享配置如何实现？**
A：将节点配置导出为加密文件，团队成员导入即可。敏感信息（如密码）不随配置共享。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **V2Ray**: 已安装并配置完成
- **cron**: 系统自带（Linux/macOS）或任务计划程序（Windows）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| V2Ray | 服务 | 必需 | 官方发布渠道下载 |
| Node.js | 运行时 | 必需 | 官方站点下载 |
| cron | 调度器 | 可选 | 系统自带 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）
- V2Ray 的节点配置在各自配置文件中管理
- 告警通知若使用 Webhook，需配置 Webhook URL

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + 脚本执行 + cron调度）
- **说明**: 专业版在 Markdown 指令基础上，提供多节点、定时、负载均衡与监控能力
