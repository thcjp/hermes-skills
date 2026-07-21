---
slug: github-trending-feed
name: github-trending-feed
version: "1.0.0"
displayName: GitHub Trending Feed
summary: 获取 GitHub Trending 热门仓库列表。当用户要求查看 GitHub 热榜、每日 GitHub trending、推送 GitHub
  热门项目时使用。支持可选语言过滤，返回结构化 J...
license: MIT-0
description: |-
  获取 GitHub Trending 热门仓库列表。当用户要求查看 GitHub 热榜、每日 GitHub trending、推送 GitHub
  热门项目时使用。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
---
# GitHub Trending Feed

## 核心能力

- 获取 GitHub Trending 热门仓库列表
- 当用户要求查看 GitHub 热榜、每日 GitHub trending、推送 GitHub
  热门项目时使用
- 支持可选语言过滤，返回结构化 J
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: Use、需要消息发送、通知推送、邮件短信、通信集成时使用、不适用于垃圾信息、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 基础用法

```bash
python3 ~/.skill-platform/workspace/skills/github-trending/scripts/fetch_trending.py
```

### 语言过滤

```bash
python3 ~/.skill-platform/workspace/skills/github-trending/scripts/fetch_trending.py python
python3 ~/.skill-platform/workspace/skills/github-trending/scripts/fetch_trending.py javascript
```

### 输出格式

返回 JSON 数组，每个元素：

```json
{
  "full_name": "owner/repo",
  "description": "仓库描述",
  "language": "Python",
  "stars": 12345,
  "url": "(已移除GitHub链接)
}
```

### Agent 使用建议

获取数据后，根据所在平台格式化输出：

**飞书**：

```text
📊 **GitHub Trending · 今日热榜**
🔥 1. owner/repo - 描述 ⭐ 12345 | Python 🔗 (已移除GitHub链接)
```

**Discord/Telegram**：

```text
📊 GitHub Trending 今日热榜
1. owner/repo - 描述 ⭐ 12345 | Python | (已移除GitHub链接)
```

**控制台**：

```text
1. owner/repo (⭐ 12345 | Python)
   描述
   (已移除GitHub链接)
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | （根据实际场景填充） | 是 | 相关说明 |
| content | （根据实际场景填充） | 否 | 相关说明 |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明"
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 示例1：基础用法

```
1. **抓取 Trending 页面**：获取 GitHub 热门仓库列表
2. **获取仓库详情**：对每个仓库调用 GitHub REST API 获取 description、stars、language
3. **返回 JSON**：agent 自行格式化为目标平台的消息
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪。

### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界。

## 已知限制

* GitHub API 有速率限制，高频使用建议配合缓存
* 脚本自动处理 API 错误，失败时会返回 fallback 数据
* 默认返回 9 个仓库，语言过滤时返回 10 个
