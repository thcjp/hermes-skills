---
slug: diagram-tools-tool-free
name: diagram-tools-tool-free
version: "1.0.0"
displayName: 图表工具基础版
summary: 支持 Mermaid 和 Graphviz 生成流程图、思维导图、时序图等多种图表
license: MIT
edition: free
description: |-
  核心能力: 可视化工具领域的专业化 AI 辅助工具,提供核心基础功能支持。

  适用场景: 个人用户与轻量级场景,涵盖日常操作、自动化工作流与智能决策辅助。

  差异化: FREE 版本,面向个人用户提供核心功能、简洁操作与社区支持。

  触发关键词: 图表, mermaid, graphviz, 流程图, 思维导图, 时序图, 架构图
tags:
- 图表
- Mermaid
- Graphviz
- 流程图
- 思维导图
tools:
- read
- exec
---

# 图表工具基础版

## 概述

本工具是 **可视化工具** 领域的 **FREE 版本** AI Skill,专为个人用户与轻量级场景设计。通过自然语言指令驱动 AI Agent 执行任务,提供核心功能与简洁易用的操作体验。

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

- 使用 Mermaid 语法生成流程图与时序图
- 使用 Graphviz DOT 语言生成有向图
- 支持思维导图、甘特图、饼图等多种类型
- 提供主题颜色配置
- 生成数据图表(柱状图/折线图/饼图)

### 功能详情

本版本提供 5 项核心能力,覆盖 可视化工具 的常见使用场景。如需批量操作、团队协作、数据分析等高级功能,可升级至 PRO 版本。

**FREE 版本核心功能清单:**

- 使用 Mermaid 语法生成流程图与时序图
- 使用 Graphviz DOT 语言生成有向图
- 支持思维导图、甘特图、饼图等多种类型
- 提供主题颜色配置
- 生成数据图表(柱状图/折线图/饼图)

**PRO 版本扩展功能预览:**

- 自定义品牌主题与企业视觉规范适配
- 批量图表渲染与高清输出(SVG/PDF/PNG)
- 图表版本管理与变更对比
- 与文档系统集成的图表嵌入
- 图表模板库与团队共享
- API 自动生成图表并嵌入 CI/CD


## 使用场景

### 场景 1: 绘制流程图

使用 Mermaid 语法快速绘制业务流程图

```bash
graph TD
  A[开始] --> B{条件判断}
  B -->|是| C[处理A]
  B -->|否| D[处理B]
  C --> E[结束]
  D --> E
```

### 场景 2: 生成架构图

使用 Graphviz 绘制系统架构图

```bash
from graphviz import Digraph
dot = Digraph()
dot.node("A", "API网关")
dot.node("B", "业务服务")
dot.edge("A", "B")
dot.render("arch", format="png")
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
  "engine": "mermaid",
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#1976d2",
    "lineColor": "#666666"
  }
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
请帮我绘制流程图
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
  "engine": "mermaid",
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#1976d2",
    "lineColor": "#666666"
  }
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

1. **节点标签保持简短提高可读性**
2. **使用子图分组相关组件**
3. **高清输出使用 -s 2 或 -s 3 参数**
4. **统一主题颜色保持图表风格一致**

### 个人使用建议

- 从简单任务开始熟悉工具行为,逐步扩展到复杂场景
- 定期备份配置文件与数据,防止意外丢失
- 遇到问题先查阅常见问题章节,再寻求社区帮助
- 保持配置简洁,只启用必要的功能选项
- 定期更新工具版本以获取最新功能与修复
- 记录常用操作命令,提高日常使用效率


## 常见问题

### Q: 支持哪些图表类型?

A: Mermaid: 流程图/时序图/类图/状态图/ER图/甘特图/饼图/思维导图/时间线;Graphviz: 有向图/无向图/层级图。

### Q: 如何自定义颜色?

A: 通过 themeVariables 配置 primaryColor、lineColor 等参数。

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
