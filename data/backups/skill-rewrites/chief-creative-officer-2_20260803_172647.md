---
name: chief-creative-officer-2
slug: chief-creative-officer-2
displayName: "Chief Creative Offic"
version: "0.1.0"
summary: "AI首席创意官Agent,统揽创意决策"
description: "AI首席创意官Agent,统揽创意决策。提供专业的能力支持,适用于多种工作场景。开箱即用,无需复杂配置,支持中文交互与结构化输出。内置错误恢复与降级机制,多格式兼容,适配多源数据。"
license: "MIT"
tools:
  - read
---

# Chief Creative Officer

## Overview

This skill provides specialized capabilities for chief creative officer.

## Instructions

## Usage Notes

* This skill is 基于 the chief_creative_officer agent configuration
* Template variables (if any) like $DATE$, $SESSION_GROUP_ID$ may require runtime substitution
* Follow the instructions and guidelines provided in the content above

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent( Code / Cursor / Codex /  CLI等)
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

This skill provides specialized capabilities for chief creative officer.

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

### Q1: 如何开始使用Chief Creative Offic？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Chief Creative Offic有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **输入格式**: 输入内容需遵循Markdown格式，确保可读性和正确解析。
- **内容长度**: 输入内容长度不宜过长，建议不超过5000字符，以避免性能下降或解析错误。

### 性能边界
- **处理速度**: 在理想网络条件下，技能处理单个请求的平均响应时间约为几秒。
- **并发处理**: 单个Agent实例同时处理的请求数量有限，建议避免过高并发请求。

### 兼容性约束
- **平台兼容性**: 本技能适用于支持SKILL.md的任意AI Agent，如 Code、Cursor、Codex、 CLI等。
- **操作系统兼容性**: 支持Windows、macOS和Linux操作系统。
- **LLM支持**: 需要底层LLM支持，无法在没有LLM的环境中运行。

### 功能限制
- **复杂决策**: 由于技能基于AI模型，无法处理需要高度人工判断的复杂决策场景。
- **定制化需求**: 技能提供的基础功能有限，对于高度定制化的需求可能无法满足。

### 安全性限制
- **数据隐私**: 技能不会存储或处理敏感数据，所有输入内容在处理过程中均保持匿名。
- **代码执行**: 技能不支持直接执行代码，所有操作均通过Markdown指令和exec命令实现。

### 其他限制
- **模型能力**: 技能的性能取决于底层模型的能力，随着模型更新，性能可能会有所提升。
- **外部依赖**: 技能可能依赖于外部API或服务，外部服务的不可用可能导致技能无法正常工作。
---
