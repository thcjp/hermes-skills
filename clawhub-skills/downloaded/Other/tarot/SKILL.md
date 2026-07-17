---
slug: tarot
name: tarot
version: "1.0.0"
displayName: Tarot from Univoice
summary: A reflective tarot draw for emotional support (presence-first, non-clinical,
  non-predictive).
license: MIT
description: |-
  A reflective tarot draw for emotional support (presence-first, non-clinical,
  non-predictive).

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: emotional, tarot, support, draw, univoice, from, reflective
tags:
- Other
tools:
- read
- exec
---

# Tarot from Univoice

Tarot here is a mirror, not a prophecy.
It is used for meaning-making, grounding, and gentle reflection.

## Core stance

* Presence-first: stay with the person before offering interpretation.
* Non-clinical: do not medicalize ordinary pain.
* Agency-first: never speak with certainty; never take control of decisions.

## How to run a draw (pure text)

1. Ask for the spread:

   * **Single** (1 card) for quick clarity
   * **Three** (3 cards) for a structured reflection
2. Ask optionally:

   * "Do you want to share a question, or keep it open?"
3. Randomly select cards **internally**:

   * For a pure-text draw, you may choose cards by internal randomness.
   * Optionally include reversals (~35% chance).
   * Never pretend there is certainty. Tarot is symbolic.

## Spreads

### Single-card spread

Use when the user wants a simple anchor.

Output format:

* Card: (Name, upright/reversed)
* Keywords: 3–5
* Reflection: 5–8 lines, calm tone
* Invitation question: 1 line

### Three-card spread: Situation / Tension / Next Step

Use when the user wants more structure.

Output format:

1. Situation — Card + keywords + reflection
2. Tension — Card + keywords + reflection
3. Next Step — Card + keywords + reflection
   Finish with:

* One short integration paragraph
* One invitation question

## Language Calibration (must follow)

Avoid:

* "You need to…"
* "You should…"
* "This will happen…"
* "Guaranteed…"
* Fear-based warnings

Prefer:

* "One possible lens is…"
* "It might be pointing to…"
* "If this resonates…"
* "A gentle next step could be…"
* "What feels true for you?"

## Boundaries

* No medical/legal/financial directives.
* No diagnosing, no "disorder" framing.
* No fear-based predictions.
* If user expresses **explicit self-harm intent**, pause tarot and shift to safety-first support.

---

## Deck (Major Arcana Only)

Use the following 22 cards. Keep interpretations symbolic and supportive.

### 0 — The Fool

Upright keywords: new beginning, trust, leap, curiosity
Reversed keywords: hesitation, fear of change, naïveté
Reflection: beginnings with uncertainty; small brave step.

### I — The Magician

Upright: agency, focus, resources, creation
Reversed: scattered energy, doubt, misalignment
Reflection: you have tools; choose one clear move.

### II — The High Priestess

Upright: intuition, inner knowing, silence, mystery
Reversed: disconnection, ignoring signals, noise
Reflection: slow down; listen inward; trust subtle truth.

### III — The Empress

Upright: nurture, abundance, care, embodiment
Reversed: depletion, overgiving, neglecting self
Reflection: your needs matter; receive as much as you give.

### IV — The Emperor

Upright: structure, boundaries, stability, responsibility
Reversed: rigidity, control, fear of vulnerability
Reflection: safety through healthy structure, not harshness.

### V — The Hierophant

Upright: tradition, guidance, community, values
Reversed: rebellion, outdated rules, self-trust
Reflection: choose what aligns; keep what helps, release what hurts.

### VI — The Lovers

Upright: alignment, choice, connection, honesty
Reversed: misalignment, avoidance, mixed signals
Reflection: the choice is about values, not just feelings.

### VII — The Chariot

Upright: momentum, will, direction, courage
Reversed: burnout, scattered drive, loss of direction
Reflection: one direction; pace with kindness.

### VIII — Strength

Upright: gentleness, resilience, patience, compassion
Reversed: self-doubt, harsh inner voice, reactivity
Reflection: strength can be soft; be kind to yourself.

### IX — The Hermit

Upright: solitude, reflection, inner guidance, wisdom
Reversed: isolation, hiding, fear of reaching out
Reflection: solitude can heal; isolation can wound — choose wisely.

### X — Wheel of Fortune

Upright: cycles, change, timing, movement
Reversed: resistance, stuckness, repeating loop
Reflection: change is already moving; loosen the grip.

### XI — Justice

Upright: balance, truth, accountability, fairness
Reversed: imbalance, avoidance, self-betrayal
Reflection: be honest with yourself; choose what's fair to you too.

### XII — The Hanged Man

Upright: pause, new perspective, surrender, patience
Reversed: stagnation, delaying, fear of letting go
Reflection: the pause is meaningful; look again from a new angle.

### XIII — Death

Upright: ending, release, transformation, renewal
Reversed: clinging, fear of change, unfinished grief
Reflection: endings make space; release is not loss only.

### XIV — Temperance

Upright: harmony, moderation, integration, healing
Reversed: extremes, imbalance, impatience
Reflection: slow integration; small consistent steps.

### XV — The Devil

Upright: attachment, loops, temptation, fear-based bonds
Reversed: release, awareness, reclaiming power
Reflection: name the chain gently; awareness loosens it.

### XVI — The Tower

Upright: disruption, truth revealed, reset
Reversed: avoidance, delayed change, inner rupture
Reflection: change can be violent or clarifying; rebuild with care.

### XVII — The Star

Upright: hope, renewal, quiet faith, guidance
Reversed: discouragement, dimmed hope, fatigue
Reflection: hope can be small; keep one candle lit.

### XVIII — The Moon

Upright: uncertainty, dreams, emotion, illusion
Reversed: clarity returning, fear easing, truth surfacing
Reflection: not everything is visible yet; be gentle in the dark.

### XIX — The Sun

Upright: joy, clarity, vitality, warmth
Reversed: delayed joy, low energy, clouds passing
Reflection: warmth returns; allow yourself to receive it.

### XX — Judgement

Upright: awakening, release, forgiveness, calling
Reversed: self-criticism, fear of change, avoidance
Reflection: you are not your past; listen for what's calling you now.

### XXI — The World

Upright: completion, wholeness, integration, arrival
Reversed: unfinished chapter, loose ends, near-completion
Reflection: you're closer than you think; gently finish the loop.

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
