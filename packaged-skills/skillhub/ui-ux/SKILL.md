---
slug: "ui-ux"
name: "ui-ux"
version: "1.0.0"
displayName: "UI / UX"
summary: "可搜UI/UX设计库,50+风格/97色板/57字体对/99规则"
license: "Proprietary"
homepage: "https://skillhub.ai/skills/ui-ux"
description: |-
  Searchable UI/UX design databases: 50+ styles, 97 palettes, 57 font
  pairings, 99 UX rules, 25 character sets.
tools:
- read
- exec
tags:
- ui
- ux
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

## 使用指南

1. 分析设计需求，提取关键词
2. 搜索设计系统、补充领域和技术栈

```bash
# 搜索设计系统
python3 design_db.py "beauty spa wellness service elegant" --design-system -p "Serenity Spa"

# 补充搜索UX规则和字体
python3 design_db.py "animation accessibility" --domain ux
python3 design_db.py "elegant luxury serif" --domain typography

# 搜索技术栈组件
python3 design_db.py "layout responsive form" --stack html-tailwind
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
A: 提供设计需求关键词（如"beauty spa elegant"），系统会从50+风格、97色板、57字体对和99条UX规则中检索匹配方案，输出完整设计系统供直接使用。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 设计库内容为静态预设数据，无法根据最新设计趋势自动更新，需定期手动维护
- 配色方案和字体配对基于通用设计原则，特定品牌场景（如强品牌色约束）仍需人工调整
- 99条UX规则为通用最佳实践，不涵盖医疗、金融等强监管行业的特殊合规要求
