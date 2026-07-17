---
slug: bilibili-helper
name: bilibili-helper
version: "2.3.5"
displayName: Bilibili Helper
summary: B站创作助手。视频标题优化、标签推荐、简介模板、投稿策略、UP主运营、弹幕互动。Bilibili video creator assistant.
  B站运营、视频SEO、粉丝增长、投币收藏、充电...
license: MIT-0
description: |-
  B站创作助手。视频标题优化、标签推荐、简介模板、投稿策略、UP主运营、弹幕互动。Bilibili video creator assistant.
  B站运营、视频SEO、粉丝增长、投币收藏、充电...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 标签推荐, bilibili, 视频标题优化, video, assistant, 站创作助手, creator, 投稿策略
tags:
- Creative
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
