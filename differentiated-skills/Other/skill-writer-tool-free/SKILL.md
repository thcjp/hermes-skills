---
slug: skill-writer-tool-free
name: skill-writer-tool-free
version: "1.0.0"
displayName: Skill编写工具免费版
summary: 创建结构规范的Agent技能，支持渐进式展开与资源捆绑，适合个人开发者快速上手。
license: MIT
edition: free
description: |-
  Skill编写工具免费版，面向个人开发者的轻量级Agent技能创建工具。

  核心能力:
  - 结构化 SKILL.md 创建与模板
  - 渐进式内容展开（主文件+引用文件）
  - 资源捆绑与脚本集成
  - 描述规范与触发关键词校准

  适用场景:
  - 个人开发者创建自定义技能
  - 团队内部技能的快速原型
  - 学习 Agent 技能结构与规范

  差异化: 免费版聚焦核心技能创建与结构规范，去除所有外部平台与作者引用，强化中文本地化与触发关键词，适合个人用户零成本上手。

  触发关键词: Skill编写, 技能创建, SKILL.md, 渐进式展开, 资源捆绑, 触发关键词, 技能模板
tags:
- Skill编写
- 技能创建
- 结构规范
- 免费版
tools:
- read
- exec
---

# Skill编写工具（免费版）

## 概述

Skill编写工具免费版帮助你创建结构规范的 Agent 技能。提供 SKILL.md 模板、渐进式内容展开与资源捆绑能力，确保技能描述精准、结构清晰、触发关键词明确。

## 核心能力

| 能力 | 说明 |
|:-----|:-----|
| 结构化创建 | SKILL.md + REFERENCE.md + EXAMPLES.md + scripts/ |
| 渐进式展开 | 主文件简洁，详细内容拆分至引用文件 |
| 资源捆绑 | 脚本与文档统一管理 |
| 描述校准 | 触发关键词明确，描述符合规范 |
| 审查清单 | 创建后自动检查规范合规性 |

## 使用场景

### 场景一：创建自定义技能

开发者希望为常见任务创建一个技能。

```text
用户：帮我创建一个「代码格式化」的技能。
助手：
让我先了解几个问题：
1. 这个技能覆盖什么任务/领域？ → 代码格式化
2. 具体处理哪些用例？ → Python、JavaScript、Go 的格式化
3. 需要可执行脚本还是仅指令？ → 调用 prettier/black/gofmt
4. 有参考资料需要包含吗？ → 各工具的配置示例

基于你的需求，技能结构如下：

skill-code-formatter/
├── SKILL.md           # 主指令（含触发关键词）
├── REFERENCE.md       # 各语言格式化工具详情
├── EXAMPLES.md        # 使用示例
└── scripts/
    └── format.sh      # 格式化脚本
```

### 场景二：编写 SKILL.md

按照规范编写主指令文件。

```markdown
---
name: code-formatter
description: Format code with prettier, black, gofmt. Use when user mentions
  formatting, code style, or when files need formatting.
---

## Quick start

\`\`\`bash
./scripts/format.sh --language python --file path/to/file.py
\`\`\`

## Workflows

1. 检测文件语言
2. 选择对应格式化工具
3. 执行格式化
4. 验证格式化结果

## Advanced features

See [REFERENCE.md](REFERENCE.md) for tool-specific configurations.
```

### 场景三：审查技能规范

创建后自动检查规范合规性。

```text
助手：
📋 技能审查清单：
✅ 描述包含触发关键词（"Use when..."）
✅ SKILL.md 控制在 100 行以内
⚠️ 部分内容可拆分至 REFERENCE.md
✅ 包含具体示例
✅ 引用深度仅一层
✅ 无时效性信息
✅ 术语一致

建议：将「各工具配置详情」移至 REFERENCE.md，保持主文件简洁。
```

## 快速开始

```bash
# 1. 收集需求
# - 任务/领域
# - 具体用例
# - 是否需要脚本
# - 参考资料来源

# 2. 创建技能结构
mkdir -p my-skill/scripts
touch my-skill/SKILL.md
touch my-skill/REFERENCE.md

# 3. 编写 SKILL.md（参考模板）
# 4. 编写引用文件（如需要）
# 5. 编写脚本（如需要）
# 6. 审查规范合规性
```

## 配置示例

```markdown
# SKILL.md 模板
---
name: skill-name
description: 简要描述能力。Use when [具体触发条件]。
---

## Quick start

[最小可用示例]

## Workflows

[复杂任务的分步骤流程与清单]

## Advanced features

[详细内容链接至: See REFERENCE.md]
```

```text
# 描述规范
- 最大 1024 字符
- 第三人称书写
- 第一句: 做什么
- 第二句: "Use when [触发条件]"

# 好的描述示例:
Extract text and tables from PDF files, fill forms, merge documents.
Use when working with PDF files or when user mentions PDFs, forms, or document extraction.

# 差的描述示例:
Helps with documents.
（Agent 无法区分此技能与其他文档技能）
```

## 最佳实践

* 描述是 Agent 选择技能的唯一依据，务必精准。
* SKILL.md 控制在 100 行以内，超出时拆分至引用文件。
* 触发关键词要具体（文件类型、操作动词、场景）。
* 确定性操作优先编写脚本，节省 Token 并提升可靠性。
* 引用深度保持一层，避免多层嵌套增加加载成本。
* 不包含时效性信息（版本号、日期等会过时）。
* 术语保持一致，避免同义词混用。
* 包含具体可运行的示例。

## 常见问题

**Q：免费版支持技能模板库吗？**
A：免费版提供基础模板。如需模板库与复用，请考虑 PRO 版本。

**Q：免费版支持多人协作编写吗？**
A：免费版面向个人编写。如需多人协作与审核，请使用 PRO 版本。

**Q：SKILL.md 超过 100 行怎么办？**
A：将详细内容拆分至 REFERENCE.md，主文件仅保留快速开始与工作流。

**Q：什么时候需要编写脚本？**
A：操作是确定性的（校验、格式化）、相同代码会重复生成、错误需要显式处理时，编写脚本更优。

**Q：描述里应该包含哪些触发关键词？**
A：文件类型（PDF/CSV）、操作动词（提取/合并/格式化）、场景（表单/文档）等具体词汇。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent创建技能
