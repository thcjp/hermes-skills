---
slug: calendar-toolkit-free
name: calendar-toolkit-free
version: "1.0.0"
displayName: 日历管理工具包基础版
summary: 日历管理与调度工具,支持创建事件、安排会议与跨平台同步,适合个人用户
license: MIT
edition: free
description: |-
  核心能力: 日程管理领域的专业化 AI 辅助工具,提供核心基础功能支持。

  适用场景: 个人用户与轻量级场景,涵盖日常操作、自动化工作流与智能决策辅助。

  差异化: FREE 版本,面向个人用户提供核心功能、简洁操作与社区支持。

  触发关键词: 日历, 日程, 会议, 事件创建, 时间安排, 提醒
tags:
- 日历管理
- 日程安排
- 会议调度
tools:
- read
- exec
---

# 日历管理工具包基础版

## 概述

本工具是 **日程管理** 领域的 **FREE 版本** AI Skill,专为个人用户与轻量级场景设计。通过自然语言指令驱动 AI Agent 执行任务,提供核心功能与简洁易用的操作体验。

FREE 版本与 PRO 版本完全兼容,可在需要时升级至 PRO 版本获取高级功能、批量操作与团队协同能力。

### 版本定位

| 维度 | FREE 版本 | PRO 版本 |
|:-----|:----------|:---------|
| 目标用户 | 个人用户 | 企业团队 |
| 功能范围 | 核心功能 | 全部功能 |
| 批量操作 | 不支持 | 支持 |
| 团队协作 | 不支持 | 支持 |
| 技术支持 | 社区支持 | 优先响应 |
| 数据分析 | 基础统计 | 高级分析 |


## 核心能力

FREE 版本提供以下能力:

- 创建日历事件并设置提醒
- 安排会议并查看参与者可用时间
- 查看今日/本周日程安排
- 支持重复事件设置
- 跨 Google/Apple/Outlook 平台同步

### 功能详情

本版本提供 5 项核心能力,覆盖 日程管理 的常见使用场景。如需批量操作、团队协作、数据分析等高级功能,可升级至 PRO 版本。

**FREE 版本核心功能清单:**

- 创建日历事件并设置提醒
- 安排会议并查看参与者可用时间
- 查看今日/本周日程安排
- 支持重复事件设置
- 跨 Google/Apple/Outlook 平台同步

**PRO 版本扩展功能预览:**

- 多租户日历管理与权限隔离
- 会议室与资源预订系统
- 智能排程:自动优化会议时间安排
- 团队日历可视化与冲突检测
- 日历数据分析:时间利用率与会议负担统计
- API 集成与 Webhook 事件通知


## 使用场景

### 场景 1: 快速安排会议

通过自然语言创建会议并查看可用时间

```bash
用户: "明天下午2点开个会"
Agent: 创建事件 -> 检查冲突 -> 设置提醒 -> 返回确认
```

### 场景 2: 查看本周安排

快速浏览本周所有日程

```bash
用户: "这周有什么安排"
Agent: 列出本周所有事件 -> 按时间排序 -> 标注重要事项
```



## 快速开始

### 1. 环境准备

确保已安装并配置好 AI Agent 环境(Claude Code / Cursor / Codex / Gemini CLI 等),本 Skill 通过 SKILL.md 指令驱动 Agent 执行任务。

**系统要求:**

- 操作系统: Windows / macOS / Linux
- Agent 平台: 支持 SKILL.md 格式的任意 AI Agent
- 运行时: Python 3.8+ 或 Node.js 18+(视具体操作需求)

### 2. 配置参数

```bash
{
  "provider": "google",
  "timezone": "Asia/Shanghai",
  "default_reminder": 15,
  "sync_interval": 300
}
```

### 3. 验证配置

配置完成后,可通过以下方式验证是否正常工作:

```bash
# 验证环境变量是否设置
echo "配置检查:"
env | grep -E "API|KEY|TOKEN|SECRET" | sed "s/=.*/=***/"  # Linux/macOS
# 或 PowerShell
# Get-ChildItem Env: | Where-Object {$_.Name -match "API|KEY|TOKEN"} | Format-Table
```

### 4. 开始使用

在 AI Agent 对话中描述你的需求,Agent 会根据本 Skill 的指令自动执行对应操作。

```text
请帮我快速安排会议
```

Agent 将自动:
1. 解析你的自然语言指令
2. 调用相应的工具或 API
3. 执行操作并返回结果
4. 返回执行结果供你确认


## 配置示例

### 基础配置

```bash
{
  "provider": "google",
  "timezone": "Asia/Shanghai",
  "default_reminder": 15,
  "sync_interval": 300
}
```
### 可选配置

```json
{
  "edition": "free",
  "auto_retry": false,
  "max_concurrent": 1,
  "log_level": "info",
  "cache_enabled": true,
  "timeout": 30
}
```

**FREE 配置项说明:**

| 配置项 | 类型 | 默认值 | 说明 |
|:-------|:-----|:-------|:-----|
| auto_retry | bool | false | 失败后自动重试 |
| max_concurrent | int | 1 | 最大并发数(FREE 限制为1) |
| log_level | string | info | 日志级别 |
| cache_enabled | bool | true | 启用结果缓存 |
| timeout | int | 30 | 操作超时时间(秒) |


## 最佳实践

1. **每天早上查看当日日程做好规划**
2. **为重要会议设置多重提醒**
3. **定期归档已完成的事件**
4. **利用空闲时间段安排深度工作**

### 个人使用建议

- 从简单任务开始熟悉工具行为,逐步扩展到复杂场景
- 定期备份配置文件与数据,防止意外丢失
- 遇到问题先查阅常见问题章节,再寻求社区帮助
- 保持配置简洁,只启用必要的功能选项
- 定期更新工具版本以获取最新功能与修复
- 记录常用操作命令,提高日常使用效率


## 常见问题

### Q: 如何同步多个日历?

A: 在配置中添加多个 provider,系统会自动合并并检测冲突。

### Q: 支持自然语言创建事件吗?

A: 支持。直接描述如'下周三上午10点开会'即可自动解析。

### Q: 如何升级到 PRO 版本?

A: 升级到 PRO 版本非常简单:
1. 获取 PRO 版本授权
2. 安装 PRO 版本 Skill
3. 原有配置自动迁移,无需额外操作
4. 即可使用批量操作、团队协作等高级功能

### Q: FREE 版本有什么限制?

A: FREE 版本主要限制:
- 不支持批量操作(每次只能处理一个任务)
- 不支持团队协作(仅限个人使用)
- 不支持高级数据分析
- 技术支持依赖社区
如需这些功能,建议升级至 PRO 版本。

### Q: FREE 版本的数据安全吗?

A: FREE 版本所有数据本地存储,不上传云端,确保隐私安全。建议定期备份配置文件与数据目录。


## 依赖说明

### 运行环境

- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Python 3.8+ 或 Node.js 18+(视具体操作需求)
- **网络**: 部分功能需要网络连接访问外部 API

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| curl | CLI 工具 | 推荐 | 系统自带或包管理器安装 |
| jq | JSON 处理 | 推荐 | apt install jq / brew install jq |
| Python 3.8+ | 运行时 | 视需求 | python.org 下载 |
| Node.js 18+ | 运行时 | 视需求 | nodejs.org 下载 |

### API Key 配置

FREE 版本支持单一 API Key 配置,满足个人使用需求:
- **环境变量**:通过环境变量配置 API Key
- **配置文件**:支持配置文件方式存储 API Key
- **安全提醒**:切勿将 API Key 硬编码到脚本或提交到版本控制系统

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于 Markdown 的 AI Skill,通过自然语言指令驱动 Agent 执行任务
- **FREE 特性**: 支持单次执行、基础配置与社区支持
- **安全等级**: 基础,数据本地存储,建议定期备份
- **SLA**: 社区支持,尽力响应

---

**版本信息**

| 项目 | 值 |
|:-----|:---|
| 版本号 | 1.0.0 |
| 版本类型 | FREE |
| 许可证 | MIT |
| 兼容性 | 可升级至 PRO 版本 |
