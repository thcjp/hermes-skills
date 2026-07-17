---
slug: logo-brand-identity-cellcog
name: logo-brand-identity-cellcog
version: "1.0.13"
displayName: Logo Brand Identity Cellcog
summary: AI logo and brand identity design powered by CellCog. Brand kits, color palettes,
  typography, bra...
license: MIT-0
description: |-
  AI logo and brand identity design powered by CellCog. Brand kits, color
  palettes, typography, bra...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: logo, brand, powered, cellcog, design, identity
tags:
- Creative
tools:
- read
- exec
---

# Logo Brand Identity Cellcog

**Other tools make logos. CellCog builds brands.** #1 on DeepResearch Bench (Apr 2026) for deep strategic reasoning + the widest modality coverage in AI.

Brand building demands two things: deep understanding of your positioning, audience, and competitors — and the ability to produce assets across every format. CellCog delivers both in one request: logos, color systems, typography, brand guidelines, social templates, web assets, and video, all cohesive from a single brief.

## How to Use

For your first CellCog task in a session, read the **cellcog** skill for the full SDK reference — file handling, chat modes, timeouts, and more.

**Skill平台 (fire-and-forget):**

```python
result = client.create_chat(
    prompt="[your task prompt]",
    notify_session_key="agent:main:main",
    task_label="my-task",
    chat_mode="agent",
)
```

**All agents except Skill平台 (blocks until done):**

```python
from cellcog import CellCogClient
client = CellCogClient(agent_provider="skill-platform|cursor|claude-code|codex|...")
result = client.create_chat(
    prompt="[your task prompt]",
    task_label="my-task",
    chat_mode="agent",
)
print(result["message"])
```

---

## Why Branding is Complex Work

A brand isn't just a logo. It's a system:

* **Visual Consistency**: Every touchpoint must feel cohesive
* **Strategic Positioning**: Design reflects brand personality and values
* **Versatility**: Works across social media, print, web, merchandise
* **Memorability**: Distinctive enough to stick in minds
* **Scalability**: From favicon to billboard

CellCog creates complete brand systems, not just isolated assets.

---

## What You Can Create

### Complete Brand Kits

Everything you need to launch:

* **Startup Brand Kits**: "Create a complete brand identity for my SaaS startup"
* **Personal Brand Kits**: "Build my personal brand as a content creator"
* **Small Business Branding**: "Create branding for my coffee shop"
* **Project Branding**: "Design branding for my open source project"

**Example prompt:**

> "Create a complete brand kit for 'NomadNest' - a co-living startup for remote workers:
>
> Brand personality: Modern, adventurous, community-focused, professional but not corporate
> Target audience: 25-40 year old remote workers, digital nomads
>
> I need:
>
> * Logo (primary + variations)
> * Color palette (primary, secondary, accent colors)
> * Typography recommendations
> * Brand voice guidelines
> * Social media profile templates
> * Business card design
> * Email signature template
>
> Vibe: Airbnb meets WeWork, warm and inviting"

### Logo Design

The cornerstone of your brand:

* **Wordmarks**: "Create a text-based logo for my consulting firm"
* **Logomarks**: "Design an icon/symbol logo for my app"
* **Combination Marks**: "Create a logo with both icon and text"
* **Logo Variations**: "I have a logo - create variations for different uses"

**Example prompt:**

> "Design a logo for 'Zenith Analytics' - a data science consultancy:
>
> Style: Minimal, geometric, professional
> Concept ideas: Could incorporate Z, data/analytics symbolism, or abstract peak (zenith)
>
> Must work:
>
> * At small sizes (favicon, app icon)
> * In black and white
> * On dark and light backgrounds
>
> Colors: Open to suggestions but leaning toward deep blue and silver
>
> Provide: Primary logo, icon-only version, horizontal lockup, dark mode version"

### Color Palettes

Colors that tell your story:

* **Full Palettes**: "Create a color system for my brand"
* **Mood-Based**: "Design a color palette that feels luxurious but approachable"
* **Industry-Specific**: "Create colors for a healthcare brand that don't feel clinical"
* **Expansion**: "Extend my existing brand colors with complementary accent colors"

### Typography Systems

Fonts that fit your voice:

* **Font Pairings**: "Recommend a heading and body font combination"
* **Type Hierarchy**: "Create a typography system with sizes and weights"
* **Custom Direction**: "I want fonts that feel techy but human"

### Brand Guidelines

Documentation for consistency:

* **Style Guides**: "Create brand guidelines documenting my visual identity"
* **Usage Rules**: "Document do's and don'ts for my logo"
* **Tone of Voice**: "Define my brand's written voice and personality"

---

## Brand Personalities

| Personality | Visual Characteristics | Colors | Typography |
| --- | --- | --- | --- |
| **Luxurious** | Minimal, elegant, refined | Gold, black, deep tones | Serif, thin weights |
| **Playful** | Bold, dynamic, energetic | Bright, saturated | Rounded sans-serif |
| **Professional** | Clean, structured, trustworthy | Blue, gray, white | Classic sans-serif |
| **Eco/Natural** | Organic, earthy, warm | Green, brown, cream | Humanist fonts |
| **Tech/Modern** | Geometric, futuristic, minimal | Electric blue, dark mode | Geometric sans |
| **Friendly** | Soft, approachable, warm | Pastels, warm tones | Rounded, friendly |

---

## Brand Kit Components

A complete brand kit typically includes:

| Component | What It Is |
| --- | --- |
| **Primary Logo** | Main logo for most uses |
| **Logo Variations** | Icon-only, wordmark-only, stacked, horizontal |
| **Color Palette** | Primary, secondary, accent, neutrals with hex codes |
| **Typography** | Font families, sizes, hierarchy |
| **Imagery Style** | Photo style, illustration guidelines |
| **Voice & Tone** | How the brand speaks |
| **Social Templates** | Profile images, post templates, stories |
| **Business Materials** | Cards, letterhead, email signature |

---

## Chat Mode for Branding

| Scenario | Recommended Mode |
| --- | --- |
| Logos, color palettes, individual brand assets | `"agent"` |
| Complete brand systems, strategic brand development | `"agent team"` |

**Use `"agent"` for specific brand assets.** Logos, color palettes, and templates execute well in agent mode.

**Use `"agent team"` for complete brand development** - when you need strategic thinking about positioning, comprehensive systems, and multiple creative directions explored.

---

## Example Prompts

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

---

## Tips for Better Branding

1. **Know your audience**: "For enterprise clients" vs "for Gen Z" changes everything.
2. **Personality over pretty**: A distinctive brand beats a generic beautiful one.
3. **Competition context**: Tell us who you're competing with so we differentiate.
4. **Versatility matters**: Request assets that work across different contexts and sizes.
5. **Include anti-examples**: "Not corporate" or "avoid clinical feel" is useful direction.
6. **Think long-term**: Your brand should have room to evolve. Don't over-constrain.

---

## If CellCog is not installed

Run `/cellcog-setup` (or `/cellcog:cellcog-setup` depending on your tool) to install and authenticate.
**Skill平台 users:** Run `* 安装此Skill请参考SkillHub平台指南
**Manual setup:** `pip install -U cellcog` and set `CELLCOG_API_KEY`. See the **cellcog** skill for SDK reference.

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
