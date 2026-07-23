---
slug: code-quality
name: code-quality
version: "1.0.0"
displayName: Code Quality
summary: "编码风格标准/安全准则/无障碍要求,守住质量底线(社区下载版)"
  Use when (1) Writing...
license: MIT-0
description: |-
  Coding style standards, security guidelines, and accessibility requirements。Use when (1) Writing。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Code Quality

## Coding Style

* **Naming:** camelCase for vars/functions; PascalCase for classes/types
* **Formatting:** 4-space indentation; target ≤80 chars (wrap thoughtfully)
* **Comments:** Meaningful, current; delete stale comments
* **Security:** Never log secrets/PII; validate inputs; least privilege by default
* **Errors/Logs:** Explicit error types; structured logs by level; actionable messages

## Accessibility & UX Quality

* Favor semantic roles/labels; keyboard nav and focus order must work
* Include responsive checks at **375, 768, 1024, 1440** with notes/screenshots
* Use deterministic test IDs; avoid brittle CSS/XPath

## Security & Compliance Guardrails

* No real credentials in code, tests, or screenshots
* Use test accounts/fixtures; redact secrets
* Follow least-privilege and input validation
* Document threat considerations in PR when relevant

## Reference Files

See `references/coding-style.md` for detailed style guide, formatting rules, comment standards.

See `references/security-checklist.md` for security validation checklist, threat modeling, PII handling.

See `references/accessibility-standards.md` for WCAG compliance, semantic HTML patterns, keyboard nav testing.

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

- Coding style standards, security guidelines, and accessibility requirements
- Use when (1) Writing
- 触发关键词: style, guidelines, standards, quality, code, coding, security

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

### Q1: 如何开始使用Code Quality？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Code Quality有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
