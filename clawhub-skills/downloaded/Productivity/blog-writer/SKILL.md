---
slug: blog-writer
name: blog-writer
version: "0.1.0"
displayName: Blog Writer
summary: This blog-writing skill is coherent and disclosed, but users should understand
  it is designed to ...
license: MIT
description: |-
  This blog-writing skill is coherent and disclosed, but users should
  understand it is designed to 。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Productivity
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Blog Writer

## Overview

This skill enables writing blog posts and articles that authentically capture the writer's distinctive voice and style. It draws on examples of the writer's published work to produce content that is direct, opinionated, conversational, and grounded in practical experience. The skill includes automatic Notion integration and maintains a growing library of finalized examples.

## When to Use This Skill

Trigger this skill when:

* The user requests blog post or article writing in "my style" or "like my other posts"
* Drafting thought leadership content on AI, productivity, marketing, or technology
* Creating articles that need the writer's authentic voice and perspective
* The user provides research materials, links, or notes to incorporate into writing

## Core Responsibilities

1. **Follow the writer's Writing Style**: Match voice, word choice, structure, and length of example posts in `references/blog-examples/`
2. **Incorporate Research**: Review and integrate any information, research material, or links provided by the user
3. **Follow User Instructions**: Adhere closely to the user's specific requests for topic, angle, and emphasis
4. **Produce Authentic Writing**: Create content that reads as genuinely the writer's voice, not generic AI-generated content

## Workflow

### Phase 1: Gather Information

Request from the user:

* Topic or subject matter
* Any specific angle or thesis to explore
* Research materials, links, or notes (if available)
* Target length preference (default: 800-1500 words)

Review all provided materials thoroughly before beginning to write.

### Phase 2: Draft the Content

Reference the style guide at `references/style-guide.md` and examples in `references/blog-examples/` for calibration.

When writing:

1. Start with a strong opening statement establishing the thesis
2. Use personal voice and first-person perspective where natural
3. Include relevant personal anecdotes or professional experience if applicable
4. Structure with clear subheadings (###) every 2-3 paragraphs
5. Keep paragraphs short (2-4 sentences)
6. Weave in research materials naturally, not as block quotes
7. End with reflection, call-to-action, or forward-looking statement

### Phase 3: Review and Iterate

Present the draft and gather feedback. Iterate until the user confirms satisfaction.

### Phase 4: Publish to Notion (REQUIRED)

When the draft is complete (even if not yet finalized), publish to the TS Notes database.

**Notion Publication Details:**

* Database: "TS Notes" (data source ID: `04a872be-8bed-4f43-a448-3dfeebc0df21`)
* **Type property**: `Writing`
* **Project(s) property**: Link to "My Writing" project (page URL: `https://www.notion.so/2a5b4629bb3780189199f3c496980c0c`)
* **Note property**: The title of the blog post
* **Content**: The full blog post content in Notion-flavored Markdown

**Example Notion API call properties:**

```json
{
  "Note": "Blog Post Title Here",
  "Type": "Writing",
  "Project(s)": "[\"https://www.notion.so/2a5b4629bb3780189199f3c496980c0c\"]"
}
```

**CRITICAL**: The outcome is considered a **failure** if the content is not added to Notion. Always publish to Notion as part of the workflow, even for drafts.

### 示例

When the user confirms the draft is **final**:

1. Save the finalized post to `references/blog-examples/` with filename format:

   text

   ```
   YYYY-MM-DD-slug-title.md
   ```

   Example: `2025-11-25-why-ai-art-is-useless.md`
2. Check the examples library count:

   * If exceeding 20 examples, ask user permission to remove the 5 oldest
   * Sort by filename date prefix to identify oldest files

The post-outcome is considered **successful** when the final draft is saved to the skill folder.

## Success Criteria

| Outcome | Success | Failure |
| --- | --- | --- |
| Primary | User receives requested content AND it is added to TS Notes with Type=Writing and Project=My Writing | Content delivered but NOT added to Notion |
| Post-outcome | Final draft saved to `references/blog-examples/` | Final draft not saved when user confirms it's final |

## the writer's Writing Style Profile

### Voice & Tone

* **Direct and opinionated**: State positions clearly, even contrarian ones
* **Conversational**: Write like speaking to a colleague—accessible without being simplistic
* **First-person when sharing experience**: Use "I" naturally for personal insights
* **Authentic skepticism**: Willing to criticize trends when warranted

### Structure Patterns

* **Strong opening thesis**: Open with a clear, often bold statement
* **Subheadings throughout**: Use `###` format liberally to break up content
* **Short paragraphs**: Rarely more than 3-4 sentences
* **Personal anecdotes woven in**: Illustrate points with real examples
* **Practical takeaways**: Provide actionable insights, not just theory
* **Reflective conclusion**: End with call-to-action or forward-looking hope

### Length & Format

* Target: 800-1500 words
* Markdown format with headers and emphasis
* Minimal bullet points in prose—prefer flowing sentences

### Vocabulary Markers

* Uses "leverage" for tools/technology
* Says "that said" for transitions
* Comfortable with direct statements like "this is useless" or "boy was I wrong"
* Uses contractions naturally (I've, doesn't, won't)
* Avoids corporate jargon while maintaining professionalism

### Thematic Elements

* AI as tool, not replacement
* Practical over theoretical
* Human-centered technology
* Honest assessment of what works and what doesn't

## Resources

### references/style-guide.md

Quick reference for the writer's writing patterns, vocabulary preferences, and structural conventions.

### references/blog-examples/

Contains example blog posts demonstrating the writer's writing style. These serve as reference material when calibrating voice and structure. New finalized posts expand this library over time.

## Notion API Reference

To create a page in TS Notes:

```text
Database data source ID: 04a872be-8bed-4f43-a448-3dfeebc0df21

Properties:
- "Note": (title) - The blog post title
- "Type": "Writing"
- "Project(s)": ["https://www.notion.so/2a5b4629bb3780189199f3c496980c0c"]

Content: Full blog post in Notion-flavored Markdown
```

The "My Writing" project page ID is: `2a5b4629-bb37-8018-9199-f3c496980c0c`

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

This skill enables writing blog posts and articles that authentically capture the writer's distinctive voice and style. It draws on examples of the writer's published work to produce content that is direct, opinionated, conversational, and grounded in practical experience. The skill includes automatic Notion integration and maintains a growing library of finalized examples.

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Blog Writer？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Blog Writer有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
