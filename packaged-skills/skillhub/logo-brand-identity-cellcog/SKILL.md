---
slug: "logo-brand-identity-cellcog"
name: "logo-brand-identity-cellcog"
version: "1.0.13"
displayName: "Logo Brand Identity"
summary: "CellCog驱动AI logo与品牌识别设计,品牌套件/色板/字体"
license: "Proprietary"
homepage: "https://skillhub.ai/skills/logo-brand-identity-cellcog"
tools:
- read
- exec
tags:
- logo
- brand
- identity
- cellcog
description: |-
  AI logo and brand identity design powered by CellCog。Brand kits, color
  palettes, typography, brand guidelines generation.
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

## 使用指南

1. 提供品牌基本信息和设计方向
2. 系统基于CellCog引擎生成多个Logo概念
3. 根据反馈迭代优化设计方案

```bash
# 示例：生成品牌识别系统
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
A: 提供品牌名称、行业和目标受众信息，系统将自动生成Logo概念、配色方案和品牌指南。可通过自然语言描述设计方向，如"为科技公司设计极简风格Logo"。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

