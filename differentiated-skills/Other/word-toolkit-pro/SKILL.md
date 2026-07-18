---
slug: word-toolkit-pro
name: word-toolkit-pro
version: "1.0.0"
displayName: Word文档控制专业版
summary: 批量文档处理、模板工作流、修订审计与跨平台支持，适合团队与企业文档自动化。
license: MIT
edition: pro
description: |-
  Word文档控制工具专业版，面向团队与企业的高阶Word文档自动化平台。

  核心能力:
  - 批量文档处理与目录递归
  - 模板工作流与自动化
  - 修订审计与版本对比
  - 跨平台支持（macOS + Windows）
  - 文档质量检查与报告

  适用场景:
  - 团队文档批量处理与标准化
  - 企业合同与报告的自动化生成
  - 修订审计与合规检查

  差异化: 专业版在免费版核心 Word 控制之上扩展批量与模板，新增修订审计、跨平台、质量检查等企业级能力，并与免费版 osascript 规则兼容。

  触发关键词: Word控制, 批量文档, 模板工作流, 修订审计, 跨平台, 文档自动化, 质量检查, 合规
tags:
- Word文档
- 批量处理
- 企业自动化
- 专业版
tools:
- read
- exec
---

# Word文档控制工具（专业版）

## 概述

专业版在免费版的 osascript 应用控制、选区编辑与文档导出之上，扩展为面向团队与企业的完整 Word 文档自动化平台。新增批量文档处理、模板工作流、修订审计与跨平台支持，同时与免费版的 osascript 规则保持向后兼容。

## 核心能力

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 文档处理 | 单文档 | 批量 + 目录递归 |
| 模板工作流 | 不支持 | 模板 + 变量替换 |
| 修订审计 | 基础查看 | 审计 + 版本对比 |
| 平台支持 | macOS | macOS + Windows |
| 质量检查 | 不支持 | 自动检查 + 报告 |
| 自动化 | 手动 | 脚本 + 计划任务 |
| 报告导出 | 不支持 | Markdown / PDF |
| 权限管理 | 不支持 | 文档权限检查 |

## 使用场景

### 场景一：批量文档处理

团队需要批量处理目录下的 Word 文档。

```bash
# 批量导出为 PDF
word-pro batch export \
  --input ./docs/ \
  --output ./pdfs/ \
  --format pdf \
  --recursive

# 批量替换内容
word-pro batch replace \
  --input ./contracts/ \
  --find "旧公司名" \
  --replace "新公司名" \
  --backup

# 输出
# 📊 批量处理报告
# 总文档: 45
# 成功: 43
# 失败: 2（受保护文档，已跳过）
# 备份: ./backup/2026-07-18/
```

### 场景二：模板工作流

基于模板批量生成合同。

```bash
# 基于模板生成合同
word-pro template generate \
  --template ./templates/contract-template.docx \
  --data ./contracts-data.csv \
  --output ./generated-contracts/ \
  --variables "甲方,乙方,金额,日期"

# contracts-data.csv 示例
# 甲方,乙方,金额,日期
# A公司,B公司,¥100,000,2026-07-18
# C公司,D公司,¥250,000,2026-07-19

# 输出
# 📊 模板生成报告
# 总记录: 12
# 成功: 12
# 📁 输出: ./generated-contracts/
```

### 场景三：修订审计

审计文档的修订历史与变更内容。

```bash
# 审计文档修订
word-pro audit revisions \
  --document ./report.docx \
  --include-comments \
  --include-changes \
  --output audit-report.md

# 输出
# 📊 修订审计报告
# 文档: report.docx
# 总修订: 28
#   - 插入: 15
#   - 删除: 8
#   - 格式: 5
# 总评论: 6
# 审计者: 张三
# 审计时间: 2026-07-18
```

## 快速开始

```bash
# 1. 初始化专业版工作区
word-pro init --workspace ~/word-pro

# 2. 单文档操作（兼容免费版）
word-pro edit --document "report.docx" --find "旧内容" --replace "新内容"

# 3. 批量处理
word-pro batch export --input ./docs/ --output ./pdfs/ --format pdf

# 4. 模板生成
word-pro template generate --template ./templates/contract.docx --data ./data.csv

# 5. 修订审计
word-pro audit revisions --document ./report.docx --output audit.md

# 6. 质量检查
word-pro check quality --document ./report.docx --output quality-report.md
```

## 配置示例

```yaml
# ~/word-pro/config.yaml
edition: pro
platform: macos  # macos | windows
word:
  path: /Applications/Microsoft Word.app
  timeout: 30
batch:
  max_concurrent: 3
  recursive: true
  backup: true
  backup_dir: ./backup
template:
  path: ~/word-pro/templates/
  variables_support: true
  output_format: docx
audit:
  include_comments: true
  include_changes: true
  include_metadata: true
  retention_days: 365
quality:
  checks:
    - spelling
    - grammar
    - formatting
    - accessibility
  threshold: 80
report:
  formats: [markdown, pdf]
  template: professional
history:
  enabled: true
  retention_days: 90
  path: ~/word-pro/history/
```

## 质量检查维度

| 维度 | 说明 | 检查项 |
|:-----|:-----|:-----|
| 拼写 | 拼写错误检查 | 错别字、专业术语 |
| 语法 | 语法结构检查 | 句式、标点 |
| 格式 | 格式规范检查 | 标题层级、间距、字体 |
| 可访问性 | 可访问性检查 | alt 文本、对比度、结构 |

## 最佳实践

* 批量处理前先用 `--dry-run` 预览，确认变更方案。
* 启用 `--backup` 保留原始文件，便于回滚。
* 模板变量使用 CSV 管理，便于批量维护。
* 修订审计保留至少 365 天，满足合规要求。
* 跨平台场景注意路径格式与编码差异。
* 受保护文档批量处理时会跳过，需单独处理。
* 破坏性操作（接受所有修订、删除评论）需明确确认。
* 定期导出处理报告，作为文档治理依据。

## 常见问题

**Q：专业版与免费版的 osascript 规则兼容吗？**
A：兼容。免费版的所有 osascript 操作在专业版中可直接使用，专业版额外提供 `batch`、`template`、`audit` 等子命令。

**Q：支持 Windows 吗？**
A：专业版支持 Windows（通过 COM 自动化）与 macOS（通过 osascript）。

**Q：批量处理有文档数量上限吗？**
A：无硬性上限，建议单批不超过 100 个文档以保证报告可读性。

**Q：模板支持哪些变量？**
A：支持文本、日期、数字等变量。在模板中用 `{{variable}}` 标记，通过 CSV 提供数据。

**Q：修订审计数据存储在哪里？**
A：所有审计数据存储在本地 `~/word-pro/history` 目录，不上传至第三方服务器。

**Q：可以与文档管理系统对接吗？**
A：专业版支持导出 JSON 格式的元数据，便于与 DMS、ERP 等系统对接。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: macOS（osascript）或 Windows（COM 自动化）
- **Microsoft Word**: 已安装
- **Node.js**: 18+（批量与审计功能需要）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Microsoft Word | 应用 | 必需 | 官方购买安装 |
| Node.js | 运行时 | 必需 | 官方站点下载 |
| osascript/COM | 工具 | 必需 | 系统自带 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）
- 本工具不使用 Microsoft Graph、云文档 API 或 OAuth 流程

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + 脚本执行能力）
- **说明**: 专业版在 Markdown 指令基础上，提供批量处理、模板工作流与修订审计能力
