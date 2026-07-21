---
slug: bilibili-helper
name: bilibili-helper
version: "2.3.5"
displayName: Bilibili Helper
summary: B站创作助手。视频标题优化、标签推荐、简介模板、投稿策略、UP主运营、弹幕互动。Bilibili video creator assistant.
  B站运营、视频SEO、粉丝增长、投币收藏、充电...
license: MIT-0
description: |-
  B站创作助手。视频标题优化、标签推荐、简介模板、投稿策略、UP主运营、弹幕互动。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。
tags:
- Creative
tools:
  - - read
- exec
---

# Bilibili Helper

B站视频运营助手。标题、简介、标签、分区建议、评论互动。

## Usage

```bash
bili.sh title "主题"

bili.sh desc "视频主题"

bili.sh script "主题" [--length 5|10|15]

bili.sh tags "主题"

bili.sh help
```

## When to Use

* 用户要发B站视频，需要标题/简介/标签
* 需要写视频口播脚本
* 需要B站运营建议和内容策划

脚本使用 Python 生成符合B站平台调性的内容模板，包含标题公式、简介结构、标签策略等。

## Commands

| Command | Description |
| --- | --- |
| `title` | 生成5个B站爆款标题 |
| `desc` | 生成视频简介+标签 |
| `script` | 生成视频口播脚本 |
| `tags` | 标签推荐 |
| `help` | 显示帮助信息 |

## Output

## 所有输出为纯文本，直接可用于B站平台。

💬 Feedback & Feature Requests: <https://bytesagain.com/feedback>
Powered by BytesAgain | bytesagain.com

* Run `bilibili-helper help` for all commands

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 视频标题优化、标签推荐、简介模板、投稿策略、UP主运营、弹幕互动
- Bilibili video creator assistant
- B站运营、视频SEO、粉丝增长、投币收藏、充电
- 触发关键词: 标签推荐, bilibili, 视频标题优化, video, assistant, 站创作助手, creator, 投稿策略

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Bilibili Helper？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Bilibili Helper有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
