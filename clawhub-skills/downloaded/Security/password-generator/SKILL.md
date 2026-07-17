---
slug: password-generator
name: password-generator
version: "1.1.0"
displayName: Password Generator
summary: 生成随机安全密码。长度12-16位随机(默认)，包含大小写字母、数字、符号。当用户要求生成密码、创建密码、随机密码时使用此技能。
license: MIT
description: |-
  生成随机安全密码。长度12-16位随机(默认)，包含大小写字母、数字、符号。当用户要求生成密码、创建密码、随机密码时使用此技能。

  核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: generator, password, 生成随机安全, 位随机, 长度, 默认, 密码
tags:
- Security
tools:
- read
- exec
---

# Password Generator

生成随机安全密码的工具技能。

## Usage

当用户要求:

* "生成密码"
* "创建一个密码"
* "随机密码"
* "生成12位密码"

执行 `scripts/generate_password.py` 并将生成的密码保存到 `memory/passwords.md`。

## 功能

* 长度: 12-16位随机
* 字符: 大小写字母 + 数字 + 符号

## 保存密码

将生成的密码保存到 `memory/passwords.md`，格式:

```markdown
## [日期]

- **随机密码**
  - 密码: `[密码]`
  - 长度: [长度] 位 (12-16位随机)
  - 字符: 大小写字母 + 数字 + 符号
```

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
