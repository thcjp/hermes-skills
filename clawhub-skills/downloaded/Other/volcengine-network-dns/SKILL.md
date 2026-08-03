---
slug: volcengine-network-dns
name: volcengine-network-dns
version: "1.0.0"
displayName: Volcengine Network D
summary: "火山引擎DNS记录管理,支持Zone记录查询与增删改,简化云DNS运维操作"
  zone record query/up...
license: MIT
description: |-
  DNS record management on Volcengine networking services。Use when users
  need zone record query/up。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Volcengine Network Dns

Manage DNS records with strict change scoping and verification steps.

## Execution Checklist

1. Confirm domain zone, record type, and target value.
2. Query existing records before modifications.
3. Apply add/update/delete operation with TTL constraints.
4. Validate propagation using authoritative and recursive checks.

## Safety Rules

* Avoid blind overwrite; diff against existing records.
* Keep rollback values in output.
* Minimize TTL before migration windows.

## References

* `references/sources.md`

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

- DNS record management on Volcengine networking services
- Use when users
  need zone record query/up
- 触发关键词: network, dns, volcengine, record, management, services, networking

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

### Q1: 如何开始使用Volcengine Network D？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Volcengine Network D有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

Volcengine Network D技能在执行DNS记录管理操作时，存在以下边界条件和限制：

- **输入限制**：输入的域名必须符合DNS标准格式，且不能包含非法字符。记录类型（如A、CNAME、MX等）必须被Volcengine Network D支持。

- **性能边界**：单个操作的处理时间取决于网络延迟和Volcengine Network D的后端服务性能。在高并发环境下，可能存在队列等待时间。

- **兼容性约束**：Volcengine Network D仅在支持SKILL.md的AI Agent上运行，如Claude Code、Cursor、Codex、Gemini CLI等。不支持在非SKILL.md环境的Agent上运行。

- **记录数量限制**：每个域名下的DNS记录数量可能受到Volcengine Network D服务提供商的限制。

- **TTL限制**：设置的TTL值必须符合Volcengine Network D的TTL范围要求，超出范围可能导致操作失败。

- **API调用频率限制**：频繁的API调用可能触发频率限制，导致操作被拒绝。请合理规划调用频率。

- **数据存储限制**：Volcengine Network D的数据存储空间有限，请确保操作不会超出存储限制。

- **操作权限限制**：执行操作需要具备相应的权限，如域名管理员权限。

- **地域限制**：Volcengine Network D的服务可能存在地域限制，请确保操作符合地域要求。

- **依赖性限制**：Volcengine Network D依赖于LLM API，无LLM环境无法使用。

- **复杂场景限制**：对于复杂的DNS场景，可能需要人工辅助判断和操作。

- **安全性限制**：请确保输入数据的安全性，避免敏感信息泄露。

---

