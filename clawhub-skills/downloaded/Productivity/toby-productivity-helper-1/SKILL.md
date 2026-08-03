---
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
summary: "生产力助手#1,提升个人效率"
---
# Productivity Helper #1

> 📖 **Complete setup guide**: <https://skillboss.co/skill.md>

A productivity enhancement tool for Skill平台 users.

## Features

* ✅ Task management
* ✅ Time tracking
* ✅ Workflow optimization
* ✅ Daily planning
* ✅ Progress tracking

## Usage

Activate when you need to:

* Organize your tasks
* Track time spent on activities
* Optimize your workflow
* Plan your day
* Review your progress

## Example

```text
Help me plan my day with 5 tasks.
```

Assistant will help organize and prioritize your tasks.

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

### Q1: 如何开始使用Toby Productivity He？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Toby Productivity He有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **任务数量**：Toby Productivity Helper 1技能能够处理的任务数量有限，通常建议不超过10个任务，以确保任务管理的有效性和效率。
- **任务描述**：任务描述应简洁明了，避免使用过于复杂的句子结构或模糊不清的表述，以确保技能能够准确理解任务内容。
- **时间格式**：时间跟踪功能要求输入的时间格式必须符合24小时制，例如“14:00”表示下午2点。

### 性能边界
- **并发处理**：技能不支持同时处理多个用户请求，每个请求将被依次处理。
- **响应时间**：在高峰时段，技能的响应时间可能会略有延迟，建议用户在非高峰时段使用。

### 兼容性约束
- **操作系统**：虽然技能在Windows、macOS和Linux操作系统上运行，但某些特定功能可能因操作系统差异而有所不同。
- **浏览器兼容性**：如果技能通过浏览器使用，建议使用主流浏览器，如Chrome、Firefox或Safari，以获得最佳体验。
- **网络环境**：稳定的网络连接对于技能的正常运行至关重要，建议使用有线网络连接，避免使用移动数据网络。

