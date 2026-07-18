---
slug: tarot-reader-tool-pro
name: tarot-reader-tool-pro
version: "1.0.0"
displayName: 韦特塔罗占卜专业版
summary: 完整韦特塔罗牌阵库、客户档案管理、批量占卜与报告导出，适合专业占卜师与内容工作室。
license: MIT
edition: pro
description: |-
  韦特塔罗占卜专业版，面向专业占卜师与内容工作室的高阶塔罗占卜平台。

  核心能力:
  - 完整 78 张韦特塔罗牌意库 + 自定义牌意扩展
  - 8 种牌阵模板（单张、时间之流、凯尔特十字、关系阵、年运阵等）
  - 客户档案管理与占卜历史归档
  - 批量占卜与 Markdown/PDF 报告导出
  - 正逆位概率可配置 + 牌阵位置自定义

  适用场景:
  - 专业占卜师的客户服务与档案管理
  - 内容工作室的塔罗栏目批量生产
  - 线上塔罗课程的案例演示

  差异化: 专业版在免费版核心能力之上扩展完整牌阵库与客户管理，新增批量占卜、报告导出、自定义牌意等企业级能力，并与免费版保持输出格式兼容。

  触发关键词: 塔罗, 专业占卜, 韦特塔罗, 凯尔特十字, 客户档案, 批量占卜, 报告导出, 牌意扩展
tags:
- 塔罗
- 专业占卜
- 韦特塔罗
- 客户管理
- 专业版
tools:
- read
- exec
---

# 韦特塔罗占卜（专业版）

## 概述

专业版在免费版的温暖治愈风格与理性洞察之上，扩展为面向专业占卜师与内容工作室的完整占卜平台。覆盖完整 78 张韦特塔罗牌意，内置 8 种牌阵模板，支持客户档案管理、占卜归档、批量解读与多格式报告导出，同时与免费版的输出格式保持向后兼容。

## 核心能力

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 牌意库 | 78 张默认牌意 | 78 张 + 自定义牌意覆盖 |
| 牌阵模板 | 单张、时间之流 | 单张、时间之流、凯尔特十字、关系阵、年运阵、抉择阵、月相阵、自定义 |
| 正逆位概率 | 固定 50% | 可配置（0%-100%） |
| 客户档案 | 不支持 | 按客户隔离的占卜历史 |
| 占卜归档 | 不支持 | 本地归档 + 全文检索 |
| 批量占卜 | 不支持 | 批量主题占卜与导出 |
| 报告导出 | 不支持 | Markdown / PDF / JSON |
| 解读长度 | 100-150 字/牌 | 可配置（50-500 字/牌） |

## 使用场景

### 场景一：专业占卜师的客户服务

为固定客户提供深度占卜并归档至客户档案。

```bash
# 为客户「陈先生」执行凯尔特十字牌阵并归档
tarot-reader-pro draw --spread celtic-cross --client "陈先生" --question "本年度事业方向" --archive

# 输出示例
# 牌阵: 凯尔特十字（10张）
# 客户: 陈先生
# 归档ID: 2026-07-18-chen-001
```

```text
解读报告（节选）：
1. 现状 — 女祭司（正位）
   你正处于一个需要倾听内在直觉的阶段，答案已在你心中浮现。

2. 挑战 — 月亮（逆位）
   之前的迷雾正在散去，但残留的不安仍需被看见。

...（共10个位置）

✨ 整体指引
本年度的核心课题是「从直觉到行动」。女祭司的智慧需要通过战车的执行力落地，避免停留在思考层面。
```

### 场景二：内容工作室的批量栏目生产

为塔罗栏目一次性生成 12 星座的月度运势解读。

```bash
# 批量为 12 星座生成月度运势
tarot-reader-pro batch --template monthly-horoscope --count 12 --format markdown --output ./2026-07-report/

# 每个星座抽取时间之流牌阵并生成 300-500 字解读
# 输出目录：./2026-07-report/
```

### 场景三：线上课程的案例演示

为塔罗教学课程生成标准化的案例解读。

```bash
# 生成教学案例（含牌面位置说明 + 解读 + 教学注解）
tarot-reader-pro demo --spread three-card --teaching-mode --format markdown

# 输出包含：牌面位置含义、正逆位说明、解读思路、常见误读提醒
```

## 快速开始

```bash
# 1. 初始化专业版工作区
tarot-reader-pro init --workspace ~/tarot-reader-pro

# 2. 执行首次占卜
tarot-reader-pro draw --spread three-card --question "本季度的核心课题"

# 3. 查看客户档案与历史
tarot-reader-pro client list
tarot-reader-pro client history --name "陈先生"

# 4. 搜索历史占卜
tarot-reader-pro archive search --keyword "女祭司"
```

## 配置示例

```yaml
# ~/tarot-reader-pro/config.yaml
edition: pro
deck: rider-waite-smith
reversal_probability: 0.50
default_spread: three-card
interpretation:
  length_per_card: 150
  style: warm-rational
  language: zh
archive:
  enabled: true
  path: ~/tarot-reader-pro/archives
  format: json+markdown
  retention_days: 730
batch:
  max_concurrent: 5
  default_format: markdown
custom_dictionary:
  enabled: true
  path: ~/tarot-reader-pro/dictionary.yaml
clients:
  isolation: true
  profile_fields: [name, question_history, notes]
export:
  formats: [markdown, pdf, json]
  template: professional
```

## 牌阵模板库

| 牌阵 | 张数 | 适用场景 | 教学难度 |
|:-----|:-----|:---------|:---------|
| 单张牌 | 1 | 每日指引 | 入门 |
| 时间之流 | 3 | 简单问题、趋势预览 | 入门 |
| 凯尔特十字 | 10 | 深度问题分析 | 进阶 |
| 关系阵 | 6 | 双人关系动态 | 进阶 |
| 年运阵 | 12 | 年度十二个月主题 | 进阶 |
| 抉择阵 | 5 | 二选一深度对比 | 中级 |
| 月相阵 | 8 | 月度能量流转 | 中级 |
| 自定义 | 自定义 | 专业场景定制 | 高级 |

## 最佳实践

* 为固定客户建立独立档案，便于追踪占卜脉络与反馈。
* 批量生产内容时先用草稿模式快速迭代，锁定方向后再生成完整报告。
* 自定义牌意词典时，保留默认牌意作为对照，避免个人偏差累积。
* 教学场景下启用 `--teaching-mode`，输出包含位置含义与解读思路注解。
* 定期导出归档至外部存储，按客户分类备份。

## 常见问题

**Q：专业版与免费版的输出格式兼容吗？**
A：兼容。专业版的纯文本输出与免费版格式一致，免费版用户可无缝升级。专业版额外支持 Markdown、PDF、JSON 格式。

**Q：客户档案数据存储在哪里？**
A：所有档案与归档数据存储在本地 `~/tarot-reader-pro/archives` 目录，不上传至任何第三方服务器。可通过配置文件自定义路径与保留天数。

**Q：批量占卜有数量上限吗？**
A：单次批量建议不超过 50 条以保证解读质量。如需更大批量，建议分批执行并启用并发控制。

**Q：自定义牌意词典如何编写？**
A：编辑 `~/tarot-reader-pro/dictionary.yaml`，按牌名与正逆位覆盖关键词与解读即可。未覆盖的牌面会回退到默认牌意。

**Q：专业版支持多语言解读吗？**
A：默认中文输出，可通过配置 `language: en` 或 `language: ja` 切换。教学场景下支持中英双语对照输出。

**Q：可以导出 PDF 报告吗？**
A：可以。需安装 PDF 导出依赖（如 pandoc + LaTeX），通过 `--format pdf` 导出专业排版报告。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（批量与归档功能需要）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需 | 官方站点下载 |
| pandoc | 工具 | 可选（PDF导出） | 系统包管理器安装 |
| YAML 解析库 | 库 | 可选 | npm 安装 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）
- 批量占卜若调用外部 LLM API，需配置对应的 API Key 环境变量

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令 + 脚本执行能力）
- **说明**: 专业版在 Markdown 指令基础上，提供命令行工具支持批量、归档与导出功能
