---
slug: expanso-log-sanitize
name: expanso-log-sanitize
version: "1.0.0"
displayName: Expanso log-sanitize
summary: "清除日志中的密码、令牌等敏感信息,防止日志泄露凭证,满足安全合规要求"
  using Expanso Ed...
license: MIT
description: |-
  Sanitize log entries by removing passwords, tokens, and other sensitive
  patterns using Expanso Ed。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Expanso log-sanitize

"Sanitize log entries by removing passwords, tokens, and sensitive patterns"

## Requirements

* Expanso Edge installed (`expanso-edge` binary in PATH)
* Install via: `* 安装此Skill请参考SkillHub平台指南

## Usage

### CLI Pipeline

```bash
echo '<input>' | expanso-edge run pipeline-cli.yaml
```

### MCP Pipeline

```bash
expanso-edge run pipeline-mcp.yaml
```

### Deploy to Expanso Cloud

```bash
expanso-cli job deploy https://skills.expanso.io/log-sanitize/pipeline-cli.yaml
```

## Files

| File | Purpose |
| --- | --- |
| `skill.yaml` | Skill metadata (inputs, outputs, credentials) |
| `pipeline-cli.yaml` | Standalone CLI pipeline |
| `pipeline-mcp.yaml` | MCP server pipeline |

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

- Sanitize log entries by removing passwords, tokens, and other sensitive
  patterns using Expanso Ed
- 触发关键词: log-sanitize, sanitize, passwords, entries, removing, tokens, expanso, log

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

### Q1: 如何开始使用Expanso log-sanitize？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Expanso log-sanitize有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

Expanso log-sanitize 技能在使用过程中存在以下边界条件和限制：

- **输入格式限制**：技能仅接受有效的日志文本输入，对于非文本或格式不正确的输入，技能可能无法正确处理，并返回错误。
- **敏感信息识别限制**：技能依赖于预定义的敏感信息模式来识别和清除密码、令牌等，对于新的或非标准化的敏感信息模式，技能可能无法识别。
- **性能限制**：处理大量或复杂的日志文件时，技能的性能可能会受到影响，导致处理时间延长。
- **兼容性限制**：技能在处理不同日志格式时可能存在兼容性问题，如不支持某些特定日志格式的特殊标记或结构。
- **外部依赖限制**：技能依赖于 Expanso Edge 和 LLM API，如果这些依赖项不可用或配置不当，技能将无法执行。
- **安全性限制**：技能本身不提供加密功能，因此处理后的日志文件可能仍然需要额外的安全措施来防止未授权访问。
- **错误处理限制**：技能的错误处理机制可能无法覆盖所有可能的错误情况，某些错误可能需要用户手动干预或联系技术支持来解决。

---

