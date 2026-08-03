---
slug: creator-alpha-feed
name: creator-alpha-feed
version: "1.0.8"
displayName: Creator Alpha Feed
summary: "为创作者发布流收集并排序每日AI内容"
  Use when users ask fo...
license: MIT
description: |-
  Collect and rank daily AI content for creator-focused publishing workflows。Use when users ask fo。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Creator Alpha Feed

1. Read config first:
   * `${OBSIDIAN_CONFIG_PATH:-<your_obsidian_vault>/Skill平台/项目/AI内容日报/采集配置.md}`
2. Execute collection in this order for X:
   * homepage feed → whitelist accounts → keywords
3. Prefer API where available; fallback to browser when unavailable.
4. Enforce browser tab cap:
   * max 7 concurrent tabs; close finished tabs first; end with 0 tabs (close all temporary tabs before finishing).
5. Build ranked outputs by configured structure (default):
   * KOL TOP3 (last 6h)
   * Practical/Tutorial/Opinion TOP10
   * Industry TOP3 (last 6h)
6. Push concise results to group channel; write full report to Obsidian path.
7. Name report files with timestamp format: `YYYY-MM-DD_HHMM.md`.
8. Prefer real Obsidian Vault path (not workspace mirror) when available.
9. Use structured Obsidian directories:
   * `Skill平台/项目/AI内容日报/01-日报/` for final reports
   * `Skill平台/项目/AI内容日报/02-运行记录/` for verification/debug runs
   * `Skill平台/项目/AI内容日报/03-文档/` for installation/operational docs
10. If login is required for a source, pause and notify user to log in; wait up to 3 minutes with periodic checks, then continue remaining sources if still unavailable.

## Bundled scripts

Use `scripts/collect-v4.sh` and related scripts for deterministic fallback/automation when needed.

## Required output checks

* Include must-track account status for `@xiaohu @dotey @marclou`
* Include fallback/degradation notes
* Include final report path
* In group replies, mention the question asker (`@who asked`) when channel supports mentions

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

- Collect and rank daily AI content for creator-focused publishing workflows
- Use when users ask fo
- 触发关键词: collect, feed, content, alpha, creator, daily, rank

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

### Q1: 如何开始使用Creator Alpha Feed？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Creator Alpha Feed有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **输入格式**: Creator Alpha Feed技能仅接受符合预设格式的输入，如关键词、特定账号等。
- **数据量**: 对于大量数据输入，技能可能需要较长时间处理，且性能可能受到影响。
- **个性化需求**: 对于非常个性化的需求，技能可能无法完全满足，需要用户自行调整配置。

### 性能边界
- **并发处理**: 技能支持的最大并发处理数量有限，超过限制可能导致性能下降或错误。
- **数据更新频率**: 技能的数据更新频率受限于API和资源，可能无法实时更新。

### 兼容性约束
- **操作系统**: 技能主要在Windows、macOS和Linux操作系统上运行，其他操作系统可能不支持。
- **LLM API**: 技能依赖于LLM API，如果API更新或更改，技能可能需要相应调整。
- **Obsidian版本**: 技能可能需要与特定版本的Obsidian兼容，不保证在所有版本上都能正常运行。

### 其他限制
- **隐私保护**: 技能处理的数据需符合隐私保护要求，不得包含敏感信息。
- **内容合规性**: 技能处理的内容需符合相关法律法规和平台政策。
- **外部API限制**: 如果技能使用的外部API有使用限制，技能的性能和可用性可能受到影响。

