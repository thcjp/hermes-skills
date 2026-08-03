---
slug: game-asset-generation-cellcog
name: game-asset-generation-cellcog
version: "1.0.14"
displayName: Game Asset Generatio
summary: "CellCog驱动AI游戏资产与开发,角色一致美术"
  art, sprit...
license: MIT-0
description: |-
  AI game asset generation and game development powered by CellCog。Character-consistent
  art, sprit。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
- Lifestyle
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Game Asset Generation Cellcog

Game development assets and prototypes with character consistency across all assets.

Game development is a multi-discipline problem — mechanics, art, music, UI, and level design all need to feel unified. CellCog reasons deeply about your game's vision first, then produces character-consistent art, tilesets, music, sound effects, UI elements, 3D models, and full game design documents — all cohesive from a single brief.

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

## What You Can Create

### Character Design

Bring your game characters to life:

* **Player Characters**: "Design a cyberpunk samurai protagonist with multiple poses"
* **NPCs**: "Create a friendly merchant character for a fantasy RPG"
* **Enemies**: "Design a boss monster - corrupted tree guardian"
* **Character Sheets**: "Create a full character sheet with idle, run, attack poses"
* **Portraits**: "Generate dialogue portraits for my visual novel cast"

**Example prompt:**

> "Design a main character for a cozy farming game:
>
> Style: Stardew Valley / pixel art inspired but higher resolution
> Character: Young farmer, customizable gender, friendly expression
>
> Need:
>
> * Front, back, side views
> * Idle pose
> * Walking animation frames (4 directions)
> * Tool-holding poses (hoe, watering can)
>
> Color palette: Warm, earthy tones"

### Environment & Tiles

Build your game worlds:

* **Tilesets**: "Create a forest tileset for a top-down RPG"
* **Backgrounds**: "Design parallax backgrounds for a side-scroller"
* **Level Concepts**: "Create concept art for a haunted mansion level"
* **Props**: "Generate decorative props for a medieval tavern"
* **UI Elements**: "Design health bars, inventory slots, and buttons"

**Example prompt:**

> "Create a tileset for a dungeon crawler:
>
> Style: 16-bit inspired, dark fantasy
>
> Include:
>
> * Floor tiles (stone, dirt, water)
> * Wall tiles (brick, cave, decorated)
> * Doors (wooden, iron, magic)
> * Props (torches, chests, barrels, bones)
> * Traps (spikes, pressure plates)
>
> All tiles should seamlessly connect."

### Game Concepts

Develop your game ideas:

* **Game Design Documents**: "Create a GDD for a roguelike deckbuilder"
* **Story Outlines**: "Write the main storyline for a sci-fi RPG"
* **Mechanics Design**: "Design a unique combat system for my action game"
* **World Building**: "Create the lore for a post-apocalyptic world"
* **Pitch Decks**: "Build a pitch deck for my indie game to show publishers"

**Example prompt:**

> "Create a game design document for a mobile puzzle game:
>
> Core concept: Match-3 meets city building
> Target: Casual players, 5-minute sessions
>
> Include:
>
> * Core loop explanation
> * Progression system
> * Monetization strategy (ethical F2P)
> * First 10 levels design
> * Art style recommendations
>
> Reference games: Gardenscapes meets SimCity"

### 3D Models & Assets

Production-ready 3D models in GLB format for your game engine:

* **Characters**: "Create a 3D model of my RPG protagonist"
* **Weapons & Items**: "Generate 3D weapon models — sword, axe, bow, staff"
* **Props**: "Create 3D dungeon props — chests, barrels, torches"
* **Vehicles**: "Build a low-poly spaceship for my mobile game"
* **Environment pieces**: "Generate 3D trees, rocks, and buildings for my world"

CellCog handles the full pipeline — describe what you want, and it generates optimized reference images then converts to textured 3D models. Batch generation supported (e.g., "create 10 weapon models").

GLB output works with Unity, Unreal, Godot, Three.js, and Blender. Specify poly count and PBR materials for your target platform.

For dedicated 3D generation workflows, also check out `3d-model-generation-cellcog`.

### Sprites & Animation

Assets ready for your game engine:

* **Sprite Sheets**: "Create a sprite sheet for a ninja character"
* **Animated Effects**: "Design explosion and hit effect animations"
* **Items**: "Generate icons for weapons, potions, and armor"
* **Particle Effects**: "Create magic spell effect concepts"

### UI/UX Design

Make your game feel polished:

* **Main Menus**: "Design a main menu for a horror game"
* **HUD Elements**: "Create health, mana, and stamina bars"
* **Inventory Systems**: "Design an inventory UI for a survival game"
* **Dialogue Boxes**: "Create dialogue UI for a visual novel"

---

## Art Styles

| Style | Best For | Characteristics |
| --- | --- | --- |
| **Pixel Art** | Retro, indie | Nostalgic, clear, limited palette |
| **Hand-Painted** | RPGs, fantasy | Rich, detailed, artistic |
| **Vector/Flat** | Mobile, casual | Clean, scalable, modern |
| **Low Poly 3D** | Stylized 3D games | Geometric, distinctive |
| **Anime/Manga** | Visual novels, JRPGs | Expressive, stylized |
| **Realistic** | AAA-style | Detailed, immersive |
| **3D Models (GLB)** | Game engines, AR/VR | Textured, customizable topology and poly count |

---

## Chat Mode for Game Dev

| Scenario | Recommended Mode |
| --- | --- |
| Individual assets, sprites, character designs, UI elements | `"agent"` |
| Full game concepts, complex world building, narrative design | `"agent team"` |

**Use `"agent"` for most game assets.** Characters, tilesets, UI elements execute well in agent mode.

**Use `"agent team"` for game design depth** - full GDDs, complex narratives, or when you need multiple creative angles explored.

---

## 示例

**Full character design:**

> "Design an enemy type for my metroidvania:
>
> Concept: Shadow creatures that emerge from walls
> Behavior: Ambush predator, retreats when hit
>
> Need:
>
> * Concept art showing the creature emerging from shadow
> * Idle animation frames (lurking)
> * Attack animation frames
> * Death/dissolve animation
>
> Style: Dark, fluid, unsettling but not gory (Teen rating)"

**Complete tileset:**

> "Create a complete tileset for a beach/tropical level:
>
> Style: Bright, colorful, 32x32 pixel tiles
>
> Include:
>
> * Sand (multiple variations)
> * Water (shallow, deep, animated waves)
> * Palm trees and tropical plants
> * Rocks and cliffs
> * Beach items (shells, starfish, umbrellas)
> * Wooden platforms/bridges
>
> Should work for a platformer game."

**Game concept:**

> "Design a game concept: 'Wizard's Delivery Service'
>
> Pitch: You're a wizard who delivers magical packages across a fantasy kingdom
> Genre: Cozy adventure / time management
> Platform: PC and Switch
>
> I need:
>
> * Core gameplay loop
> * Progression systems
> * Character concepts for the wizard and NPCs
> * 3 sample delivery missions
> * Art style moodboard
>
> Vibe: Studio Ghibli meets Overcooked"

---

## Tips for Better Game Assets

1. **Specify dimensions**: "32x32 tiles" or "1920x1080 background" prevents mismatched assets.
2. **Reference existing games**: "Style like Hollow Knight" or "Celeste-inspired" gives clear direction.
3. **Think about implementation**: Request assets in formats your engine can use. Mention if you need transparency, layers, or specific file types.
4. **Consistency matters**: When requesting multiple assets, describe your game's overall style guide so everything matches.
5. **Animation frames**: Specify frame count and whether you need sprite sheets or individual frames.
6. **Consider your scope**: Start with placeholder assets and iterate. Perfect is the enemy of shipped.

---

## If CellCog is not installed

Run `/cellcog-setup` (or `/cellcog:cellcog-setup` depending on your tool) to install and authenticate.
**Skill平台 users:** Run `* 安装此Skill请参考SkillHub平台指南
**Manual setup:** `pip install -U cellcog` and set `CELLCOG_API_KEY`. See the **cellcog** skill for SDK reference.

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

- AI game asset generation and game development powered by CellCog
- Character-consistent
  art, sprit
- 触发关键词: development, cellcog, asset, generation, game

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Game Asset Generatio？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Game Asset Generatio有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
