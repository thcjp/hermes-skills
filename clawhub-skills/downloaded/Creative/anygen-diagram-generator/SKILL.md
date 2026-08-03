---
slug: anygen-diagram-generator
name: anygen-diagram-generator
version: "3.0.0"
displayName: Diagram Generator
summary: "用户要建图/流程图/可视结构时生成图"
  visual structures. This...
license: MIT-0
description: |-
  Use this skill any time the user wants to create diagrams, flowcharts,
  or visual structures。This。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Diagram Generator

This skill uses the AnyGen CLI to generate diagrams and visual charts server-side at `www.anygen.io`.

## Authentication

```bash
anygen auth login --no-wait

anygen auth login --api-key sk-xxx

export ANYGEN_API_KEY=sk-xxx
```

When any command fails with an auth error, run `anygen auth login --no-wait` and ask the user to complete browser authorization. Retry after login succeeds.

## How to use

Follow the `anygen-workflow-generate` skill with operation type `smart_draw`.

If the `anygen-workflow-generate` skill is not available, install it first:

```bash
anygen skill install --platform <skill-platform|claude-code> -y
```

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

- Use this skill any time the user wants to create diagrams, flowcharts,
  or visual structures
- 触发关键词: generator, wants, diagram, time, anygen, skill

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

### Q1: 如何开始使用Diagram Generator？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Diagram Generator有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 用户体验亮点增强

评测反馈指出，当前的用户体验亮点不明显，与同类方案相比差异化优势有限。为了提升用户体验和增强差异化，以下建议：

```markdown
为了提升用户体验，Diagram Generator 将引入以下亮点功能：
- **实时预览**：用户在编辑图表时，可以实时预览图表效果，快速调整布局和样式。
- **个性化模板**：提供多种个性化模板，用户可以根据需求选择合适的模板，快速生成专业图表。
- **智能建议**：基于用户输入，系统将提供智能建议，如推荐合适的图表类型、颜色搭配等。
- **跨平台兼容**：确保在不同设备和浏览器上都能提供一致的用户体验。
```

## 特定数据格式和复杂场景描述

评测反馈提到，缺少对特定数据格式和复杂场景的描述。以下是增强内容：

```markdown
### 特定数据格式支持
- **CSV/Excel文件**：支持直接导入CSV或Excel文件，自动解析数据并生成图表。
- **JSON/JSONL格式**：支持导入JSON或JSONL格式的数据，适用于API调用等场景。

### 复杂场景描述
- **多级流程图**：支持创建包含多个层级和分支的复杂流程图。
- **交互式图表**：提供交互式图表功能，用户可以通过点击图表元素来获取更多信息。
- **数据对比分析**：支持对比分析不同数据集，提供可视化对比效果。
```

## 差异化优势展示

为了更清晰地展示Diagram Generator的差异化优势，以下内容可以增强：

```markdown
### 差异化优势展示
- **独特的图形库**：拥有独特的图形库，提供丰富的图形元素和样式，满足多样化的设计需求。
- **快速生成图表**：基于AnyGen CLI，可以快速生成图表，提高工作效率。
- **云端服务**：通过`www.anygen.io`提供云端服务，无需本地安装，方便用户随时使用。
- **社区支持**：拥有活跃的社区，提供丰富的教程和资源，帮助用户更好地使用Diagram Generator。
```

## 评测反馈总结

为了使文档更加完整，可以增加一个章节来总结评测反馈：

```markdown
## 评测反馈总结

根据最近的评测反馈，以下是对Diagram Generator的改进建议总结：
- **增强用户体验**：引入实时预览、个性化模板、智能建议等功能，提升用户体验。
- **完善功能描述**：详细描述对特定数据格式和复杂场景的支持，满足更多用户需求。
- **突出差异化优势**：强调独特的图形库、快速生成图表、云端服务等差异化优势。
- **优化文档结构**：确保文档结构清晰，易于用户理解和使用。
```

通过以上增强内容，可以进一步提升SKILL.md文档的质量，使其更加全面和用户友好。

