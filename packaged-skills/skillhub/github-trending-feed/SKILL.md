---
slug: "github-trending-feed"
name: "github-trending-feed"
version: 1.0.1
displayName: "GitHub Trending Feed"
summary: "获取 GitHub Trending 热门仓库列表。当用户要求查看 GitHub 热榜、每日 GitHub trending、推送 GitHub"
license: "Proprietary"
description: |-
  获取 GitHub Trending 热门仓库列表。当用户要求查看 GitHub 热榜、每日 GitHub trending、推送 GitHub
  热门项目时使用。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发.
tags:
  - Integrations
  - 版本控制
  - Git
  - 开发工具
  - github
  - api
  - agent
  - trending
  - 不支持
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Development"
---
# GitHub Trending Feed

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

- 获取 GitHub Trending 热门仓库列表
- 当用户要求查看 GitHub 热榜、每日 GitHub trending、推送 GitHub
  热门项目时使用
- 支持可选语言过滤，返回结构化 J
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| Git操作 | 仓库路径与分支名 | 操作结果与变更记录 |
| 获取 GitHub  | 目标数据与配置参数 | 处理结果与执行状态 |
| 当用户要求查看 Gi | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 基础用法

```bash
python3 ~/.skill-platform/workspace/skills/github-trending/（请参考skill目录中的脚本文件）
```

### 语言过滤

```bash
python3 ~/.skill-platform/workspace/skills/github-trending/（请参考skill目录中的脚本文件） python
python3 ~/.skill-platform/workspace/skills/github-trending/（请参考skill目录中的脚本文件） javascript
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

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|

## 输出格式(补充)

```json
{
  "success": true,
  "data": {
    result: "feed 相关配置参数",
    result: "feed 相关配置参数"
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 示例1：基础用法

```
1. **抓取 Trending 页面**：获取 GitHub 热门仓库列表
2. **获取仓库详情**：对每个仓库调用 GitHub REST API 获取 description、stars、language
3. **返回 JSON**：agent 自行格式化为目标平台的消息
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪.
### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界.
## 已知限制

* GitHub API 有速率限制，高频使用建议配合缓存
* 脚本自动处理 API 错误，失败时会返回 fallback 数据
* 默认返回 9 个仓库，语言过滤时返回 10 个
