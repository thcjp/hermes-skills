---
slug: git-helper
name: git-helper
version: "1.0.0"
displayName: Git Helper
summary: "常用git操作技能,涵盖status/pull/push/branch/log(社区下载版)"
license: MIT
description: |-
  Common git operations as a skill (status, pull, push, branch, log)

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---

# Git Helper

Common git operations as a skill. Provides convenient wrappers for frequently used git commands including status, pull, push, branch management, and log viewing.

## Commands

```bash
git-helper status

git-helper pull

git-helper push

git-helper branch

git-helper log [--limit 10]
```

## Install

No installation needed. `git` is always present on the system.

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

- 触发关键词: common, pull, operations, status, git, helper, skill

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

### Q1: 如何开始使用Git Helper？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Git Helper有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

Git Helper技能在执行过程中存在一些边界条件和限制，以下是该技能可能遇到的具体情况：

- **输入限制**：Git Helper技能接受基于Markdown的指令，对于非Markdown格式的输入，技能可能无法正确解析或执行。
- **性能边界**：由于技能基于命令行执行，执行速度可能受到系统资源（如CPU、内存）的限制。在高负载或资源受限的环境中，执行时间可能会增加。
- **兼容性约束**：Git Helper技能主要针对支持SKILL.md的AI Agent，如Claude Code、Cursor、Codex、Gemini CLI等。在不支持SKILL.md的Agent上，技能可能无法正常工作。
- **命令行环境**：Git Helper技能依赖于命令行环境，因此需要确保系统已安装并配置了Git。在某些环境中，如Windows的Git Bash或WSL，可能需要额外的配置才能正常使用。
- **权限限制**：执行某些Git操作（如push）可能需要具有相应的文件系统权限。如果技能在无权限的环境中执行，可能会遇到错误。
- **网络依赖**：某些操作（如pull）可能需要网络连接。在网络不稳定或不可用的情况下，这些操作可能会失败。
- **外部依赖**：Git Helper技能可能依赖于外部工具或服务，如LLM API。如果这些外部服务不可用或出现故障，技能的功能可能会受到影响。

---

