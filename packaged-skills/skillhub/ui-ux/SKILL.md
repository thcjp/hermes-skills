---

slug: "ui-ux"
name: "ui-ux"
version: 1.0.1
displayName: "UI / UX"
summary: "可搜UI/UX设计库,50+风格/97色板/57字体对/99规则。Searchable UI/UX design databases: 50+ styles, 97 palettes, 57"
license: "MIT"
homepage: "https://skillhub.ai/skills/ui-ux"
description: Searchable UI/UX design databases: 50+ styles, 97 palettes, 57 font pairings, 99 UX rules, 25 character sets，可生成提升工作效率
tools:
  - read
  - exec
  - write
tags:
  - ui
  - ux
  - UI设计
  - 前端
  - 设计
  - python3
  - design_db
  - css
  - domain
  - 配色方案
category: "Creative"

---

## 任务定义

根据用户的设计需求，从可搜索的UI/UX设计库中检索匹配的设计风格、配色方案、字体配对和UX规则，输出完整的设计系统供开发者使用。

## 输入输出

| 输入 | 说明 |
|------|------|
| 设计关键词 | 必填，如"beauty spa elegant"、"dashboard minimal" |
| 项目名称 | 推荐填写，用于生成设计系统标识 |
| 技术栈 | 可选，如html-tailwind、react、vue等 |
| 补充领域 | 可选，如typography、ux、animation |

| 输出 | 说明 |
|------|------|
| 设计系统 | 风格定义、色彩变量、排版规范 |
| 配色方案 | 97种色板中匹配的最佳方案 |
| 字体配对 | 57组字体配对中的推荐组合 |
| UX规则 | 99条规则中相关的最佳实践 |

## 输出格式

设计系统以结构化 Markdown 输出，包含以下内容块：

- **设计系统定义**：风格关键词列表 + 设计理念段落描述
- **色彩变量**：CSS 自定义属性代码块（`--color-primary`、`--color-secondary` 等），含 HEX 值和 WCAG AA 对比度标注
- **排版规范**：字体配对方案 + 七级字体层级表（Display 到 Caption，含 `font-size`、`font-weight`、`line-height`）
- **组件规范**：按钮、表单、卡片等组件的 HTML + CSS 代码片段，标注设计要点
- **UX规则**：匹配到的规则编号、规则标题、应用建议

输出结果可直接粘贴到项目的设计文档或 `design-tokens.css` 文件中使用。

## 使用指南

1. 分析设计需求，提取关键词
2. 搜索设计系统、补充领域和技术栈

```bash
# 搜索设计系统

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。
python3 design_db.py "saas dashboard data-heavy minimal" --design-system -p "MetricsPro"

# 补充搜索UX规则和字体
python3 design_db.py "form validation feedback" --domain ux
python3 design_db.py "modern geometric sans" --domain typography

# 搜索技术栈组件
python3 design_db.py "table chart navigation" --stack react
```

## 依赖说明

- Python 3.8+ 运行环境
- 设计库数据文件（随skill分发）
- LLM API Key（用于综合分析和方案生成）

## 案例展示

**User request:** "Build a landing page for a professional skincare service"

**Step 1 — Analyze:** Beauty/Spa service, elegant/professional, html-tailwind default.

**Step 2 — Design system:**

```bash
python3 （请参考skill目录中的脚本文件） "beauty spa wellness service elegant" --design-system -p "Serenity Spa"
```

**Step 3 — Supplement:**

```bash
python3 （请参考skill目录中的脚本文件） "animation accessibility" --domain ux
python3 （请参考skill目录中的脚本文件） "elegant luxury serif" --domain typography
```

**Step 4 — Stack:**

```bash
python3 （请参考skill目录中的脚本文件） "layout responsive form" --stack html-tailwind
```

Then synthesize design system + detailed searches and implement.

## 常见问题

### Q1: 如何开始使用UI / UX？
A: 上手的关键在于"关键词质量"：叠加风格、场景与情绪词（如"fitness app energetic bold dark-mode"）远比单写"fitness"匹配精准。建议先用主检索拿到整体骨架，再按"缺什么补什么"逐项追加细分领域检索；若首轮风格偏离预期，调整关键词往往比反复更换项目名更见效。所有检索结果可合并为 CSS 变量与组件规范直接落地，无需手动换算色值。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:----|:----|:----|
| design_db.py返回空结果 | 关键词过于宽泛或与库中风格标签不匹配 | 拆分关键词为"风格+场景+情绪"三层叠加，如将"modern"改为"minimal saas dashboard dark-mode"后重试 |
| 配色方案WCAG对比度不足 | 选中色板的前景/背景色对未达AA标准 | 在输出CSS变量中手动将浅色背景调暗10-15%，或使用design_db.py追加--domain ux搜索更高对比度的替代色板 |
| 字体配对在目标平台不可用 | Google Fonts在部分地区加载缓慢或被阻断 | 下载字体文件本地托管，在font-family栈末尾添加系统字体fallback如system-ui, sans-serif |
| UX规则与项目设计规范冲突 | 99条规则为通用最佳实践，未覆盖特定行业合规要求 | 以项目设计规范为准，将冲突规则记录为例外并在团队设计文档中注明偏差理由 |

## 已知限制

- 设计库内容为静态预设数据，无法根据最新设计趋势自动更新，需定期手动维护
- 配色方案和字体配对基于通用设计原则，特定品牌场景（如强品牌色约束）仍需人工调整
- 99条UX规则为通用最佳实践，不涵盖医疗、金融等强监管行业的特殊合规要求
