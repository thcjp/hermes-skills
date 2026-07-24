---
slug: "logo-brand-identity-cellcog"
name: "logo-brand-identity-cellcog"
version: 1.0.14
displayName: "Logo Brand Identity"
summary: "CellCog驱动AI logo与品牌识别设计,品牌套件/色板/字体。AI logo and brand identity design powered by CellCog。Brand k"
license: "Proprietary"
homepage: "https://skillhub.ai/skills/logo-brand-identity-cellcog"
tools:
  - read
  - exec
  - write
tags:
  - logo
  - brand
  - identity
  - cellcog
  - 工具
  - 效率
  - 自动化
description: |-
  AI logo and brand identity design powered by CellCog。Brand kits, color
  palettes, typography, brand guidelines generation.
category: "Automation"
---
## 任务定义

根据用户提供的品牌信息（名称、行业、目标受众、品牌个性等），生成完整的品牌识别系统，包括Logo设计方案、配色方案、字体推荐、品牌指南等。

## 输入输出

| 输入 | 说明 |
|------|------|
| 品牌名称 | 必填，品牌或产品名称 |
| 行业领域 | 必填，如科技、餐饮、医疗等 |
| 目标受众 | 推荐填写，年龄、职业、偏好等 |
| 品牌个性 | 推荐填写，如专业、活泼、奢华等 |
| 竞品参考 | 可选，提供竞品名称或URL |

| 输出 | 说明 |
|------|------|
| Logo方案 | 多个Logo概念，含矢量描述和配色 |
| 配色方案 | 主色、辅色、背景色及色值 |
| 字体推荐 | 标题字体和正文字体配对 |
| 品牌指南 | Logo使用规范、间距、最小尺寸等 |

## 输出格式

品牌识别系统以结构化 Markdown 文档输出，包含以下内容块：

- **Logo概念**：每个方案含设计理念说明、矢量路径描述（SVG片段）、配色色值（HEX/RGB）
- **配色方案**：JSON 格式的调色板，含 `primary`、`secondary`、`accent`、`background` 字段及对应 HEX 值
- **字体推荐**：字体名称、Google Fonts 链接、字体栈 CSS 代码片段
- **品牌指南**：Markdown 表格列出的使用规范（最小尺寸、安全间距、禁用场景）

输出结果可直接复制到设计文档或通过 API 返回 JSON 结构化数据。

## 使用指南

1. 提供品牌基本信息和设计方向
2. 系统基于CellCog引擎生成多个Logo概念
3. 根据反馈迭代优化设计方案

```bash
# 示例：生成品牌识别系统

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。
# 输入品牌信息后，系统将输出完整的品牌套件
cellcog brand --name "MyBrand" --industry tech --audience "developers"
```

```python
# 示例：获取配色方案
palette = cellcog.get_palette(brand="MyBrand", mood="professional")
print(palette.primary, palette.secondary, palette.accent)
```

## 依赖说明

- LLM API Key（用于AI生成Logo概念和品牌文案）
- CellCog引擎运行时环境
- 网络：在线生成需要网络连接

## 案例展示

**Complete brand identity:**

> "Create a brand identity for 'Bloom' - a mental health app for young professionals:
>
> Mission: Make therapy-informed self-care accessible and non-stigmatized
> Audience: 22-35, stressed professionals, first time exploring mental health tools
> Competitors: Calm, Headspace (but we want to feel different - less meditation, more practical)
>
> Brand personality: Warm, knowledgeable, empowering (not patronizing), modern
>
> Deliver:
>
> * Logo with variations
> * Color palette (calming but not boring)
> * Font recommendations
> * App icon
> * Social media templates
> * Brand voice guidelines
>
> Avoid: Clinical/medical feel, overly 'zen'/spiritual aesthetic, childish"

**Logo design:**

> "Design a logo for 'Axiom Ventures' - a tech-focused VC firm:
>
> Positioning: Smart money, founder-friendly, sector expertise in AI/ML
>
> Direction:
>
> * Could be abstract, geometric, or incorporate 'A'
> * Should feel: Confident, forward-thinking, substantial
> * Should NOT feel: Stuffy, generic corporate, startup-bro
>
> Versatility needed: Website, pitch decks, swag, business cards
>
> Provide multiple concepts to choose from."

**Personal brand:**

> "Create a personal brand kit for me as a tech content creator:
>
> Name: Alex Chen
> Platforms: YouTube, Twitter, Newsletter
> Content: Programming tutorials, career advice, tech industry commentary
> Personality: Helpful, slightly nerdy, approachable expert
>
> I need:
>
> * A simple logo/avatar that's recognizable
> * Color palette for my content
> * YouTube thumbnail template style
> * Twitter header and profile pic
> * Newsletter banner
>
> Should feel: Personal but polished, trustworthy, not corporate"

## 常见问题

### Q1: 如何开始使用Logo Brand Identity？
A: 首次使用无需准备设计稿，自然语言即可驱动。两个小建议能让首轮结果更准：一是把"品牌个性"写成具象形容词（如"克制、专业、略带未来感"而非"好看"）；二是若已有竞品，提供名称或链接可帮助系统规避雷同方向。生成后可在同一会话中用"换个配色""再简洁一点"等口语指令逐轮微调，无需重新描述全部需求。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:----|:----|:----|
| Logo概念与品牌定位偏差 | 品牌个性描述过于抽象(如"好看""大气")导致CellCog引擎理解发散 | 将品牌个性替换为具象形容词组合(如"克制、专业、略带未来感")，重新执行cellcog brand命令 |
| 配色方案在印刷物料色差严重 | 屏幕RGB色值直接用于CMYK印刷时色域转换损失 | 将HEX值通过Pantone Color Bridge转换为印刷安全色，或在palette中指定Pantone专色编号 |
| 字体配对商用授权不明确 | Google Fonts中部分字体仅限个人免费使用 | 访问fonts.google.com确认每个字体的License标签，企业用途选择OFL/SIL协议字体或购买商业授权 |
| 品牌指南中Logo最小尺寸不适用 | 系统默认28px下限对小屏favicon或社交媒体头像过大 | 根据实际最小使用场景(如16px favicon)设置简化版Logo变体，在品牌指南中分别标注全色版和简化版的尺寸下限 |

