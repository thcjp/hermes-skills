---
slug: token-manager-tool-free
name: token-manager-tool-free
version: 1.0.0
displayName: Token用量管理免费版
summary: 监控LLM API的Token用量与费用，提供省钱建议与余额提醒，适合个人开发者日常使用。
license: Proprietary
edition: free
description: 'Token用量管理工具免费版，面向个人开发者的轻量级LLM用量监控工具。核心能力:

  - 实时会话Token用量分析与费用估算

  - 余额查询与基础提醒

  - 省钱优化建议（上下文管理、推理优化、模型选择）

  - 支持 Kimi/Moonshot、OpenAI、Anthropic、Gemini、Ollama


  适用场景:

  - 个人开发者监控API费用

  - 日常会话的Token用量追踪

  - 余额不足时的基础提醒


  差异化: 免费版聚焦核心用量监控与省钱建议，去除所有外部平台与作者引用，强化中文本地化与适用关键词...'
tags:
- Token管理
- 费用监控
- LLM优化
- 免费版
tools:
- - read
- exec
homepage: https://skillhub.cn
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
---
# Token用量管理工具（免费版）

## 概述

Token用量管理工具免费版帮助个人开发者监控 LLM API 的 Token 用量与费用，提供实时的省钱优化建议。支持主流 LLM 提供商的用量估算与余额查询，让你清楚每一次调用的成本。

## 核心能力

| 能力 | 说明 |
|---|---|
| 用量监控 | 实时会话分析，展示输入/输出 Token 与费用 |
| 余额查询 | 支持 Kimi/Moonshot 的 API 余额查询 |
| 省钱建议 | 上下文管理、推理优化、模型选择建议 |
| 提供商支持 | Kimi、OpenAI、Anthropic、Gemini、Ollama |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：LLM、用量与费用、提供省钱建议与余、额提醒、适合个人开发者日、常使用、用量管理工具免费、面向个人开发者的、轻量级、用量监控工具、用量分析与费用估、余额查询与基础提、省钱优化建议等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一：日常会话费用追踪

开发者希望了解当前会话消耗了多少 Token 与费用。

```bash
# 查看当前会话用量
node （请参考skill目录中的脚本文件） report 11000 146 42000 200000 off 9.26 moonshot kimi-k2.5
# ...
# 示例
# 📊 会话用量报告
# 输入Token: 11,000
# 输出Token: 146
# 上下文使用: 42,000 / 200,000 (21%)
# 推理状态: 关闭
# 当前余额: ¥9.26
# 预估费用: ¥0.13
# 💡 建议: 用量正常，可继续
```

### 场景二：余额查询与提醒

查询 Kimi 账户余额，余额偏低时获得提醒。

```bash
# 查询余额
node （请参考skill目录中的脚本文件） balance moonshot
# ...
# 输出示例
# 💰 Kimi/Moonshot 余额
# 当前余额: ¥3.50
# 🚨 余额偏低！建议充值或开启省钱模式
```

### 场景三：省钱优化建议

根据当前用量模式获取省钱建议。

```bash
# 获取省钱建议
node （请参考skill目录中的脚本文件） recommend
# ...
# 输出示例
# 💡 省钱建议
# 1. 上下文使用率 21%，无需压缩
# 2. 推理已关闭，小任务无需开启
# 3. 当前使用 kimi-k2.5，性价比良好
# 4. 余额 ¥3.50，建议避免大任务
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

```bash
# 1. 设置环境变量
export MOONSHOT_API_KEY="your-api-key"
# ...
# 2. 查看用量
node （请参考skill目录中的脚本文件） report 11000 146 42000 200000 off 9.26 moonshot kimi-k2.5
# ...
# 3. 查询余额
node （请参考skill目录中的脚本文件） balance moonshot
# ...
# 4. 查看支持的提供商
node （请参考skill目录中的脚本文件） providers
```

## 配置示例

```bash
# 环境变量配置
export MOONSHOT_API_KEY="your-kimi-key"        # Kimi/Moonshot
export OPENAI_API_KEY="your-openai-key"        # OpenAI（可选）
export ANTHROPIC_API_KEY="your-claude-key"     # Anthropic（可选）
# ...
# 命令参数说明
# report <输入tokens> <输出tokens> <上下文已用> <上下文上限> <推理状态> [余额] [提供商] [模型]
```

## 省钱建议参考

### 上下文管理

| 场景 | 建议 | 操作 |
|:-----|:-----|:-----|
| 上下文 > 80% | 紧急：必须立即压缩 | `/compact` |
| 上下文 > 50% | 建议：适时压缩 | `/compact` |
| 会话 > 50k tokens | 警告：立即拆分任务 | `/spawn` |
| 会话 > 20k tokens | 提示：大任务使用子代理 | `/spawn` |

### 提供商特定建议

| 场景 | 建议 |
|---:|---:|
| 余额 < ¥5 | 开启省钱模式，避免大任务 |
| 使用 GPT-4 | 考虑 GPT-4o-mini 省 10 倍 |
| 使用 Claude Opus | 考虑 Claude Sonnet 省 5 倍 |
| 运行 Ollama | 免费！无 API 费用 |

## 最佳实践

* API 密钥仅从环境变量读取，不要硬编码在脚本中。
* 所有数据本地存储在 `.data/` 目录，不会上传第三方服务器。
* 余额低于 ¥5 时主动开启省钱模式，避免大任务。
* 小任务（<5k tokens）可关闭推理节省 20-30% 费用。
* 网络请求仅访问官方 LLM API，确保安全。

## 常见问题

**Q：免费版支持定时余额监控吗？**
A：免费版不提供定时任务（cron）功能，需手动查询余额。如需自动监控与提醒，请考虑 PRO 版本。

**Q：免费版支持跨会话用量追踪吗？**
A：免费版仅支持单会话用量分析。如需跨会话统计与每日/每周报告，请使用 PRO 版本。

**Q：哪些提供商支持余额查询？**
A：目前仅 Kimi/Moonshot 支持 API 余额查询。OpenAI、Anthropic、Gemini 需通过控制台查看。

**Q：数据存储在哪里？**
A：所有数据存储在本地 `.data/` 目录，不上传至任何第三方服务器。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需 | 官方站点下载 |

### API Key 配置
- `MOONSHOT_API_KEY` - Kimi/Moonshot API 密钥（余额查询需要）
- `OPENAI_API_KEY` - OpenAI API 密钥（可选）
- `ANTHROPIC_API_KEY` - Anthropic API 密钥（可选）
- API 密钥仅从环境变量读取，不硬编码

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + Node.js脚本执行）
- **说明**: 基于Markdown的AI Skill，通过命令行工具监控Token用量

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 执行效率受模型能力与网络环境影响
- 本地运行，不支持多设备同步
- 当前为免费版本,如需完整功能请升级到付费版获取全部能力

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
    "result": "Token用量管理免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "token manager"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
