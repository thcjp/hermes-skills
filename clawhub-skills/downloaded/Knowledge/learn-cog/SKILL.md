---
slug: learn-cog
name: learn-cog
version: "1.0.12"
displayName: Learn Cog
summary: AI tutoring and education powered by CellCog. Study guides, exam prep, coding
  tutorials, language...
license: MIT-0
description: |-
  AI tutoring and education powered by CellCog。Study guides, exam prep,
  coding tutorials, language。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Knowledge
tools:
  - - read
- exec
---

# Learn Cog

**The best tutors explain the same concept five different ways.** CellCog does too.

# 示例

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

## How Learn-Cog Helps

### Concept Explanations

Understand anything:

* **Break It Down**: "Explain quantum entanglement like I'm 10 years old"
* **Multiple Angles**: "Explain recursion using 3 different analogies"
* **Deep Dives**: "Give me a comprehensive explanation of how neural networks learn"
* **Visual Learning**: "Create a diagram explaining the water cycle"

**Example prompt:**

> "Explain blockchain technology:
>
> Level: Complete beginner, no tech background
>
> Include:
>
> * Simple analogy to start
> * How transactions work
> * Why it's secure
> * Real-world examples
> * Common misconceptions
>
> Use simple language, avoid jargon. Include a visual diagram."

### Homework & Problem Solving

Work through problems:

* **Math Problems**: "Solve this calculus problem and explain each step"
* **Science Questions**: "Help me understand this physics concept and solve these problems"
* **Essay Help**: "Help me structure an essay on the causes of World War I"
* **Code Debugging**: "Explain why my code isn't working and help me fix it"

**Example prompt:**

> "Help me understand this math problem:
>
> Problem: Find the derivative of f(x) = x³sin(x)
>
> I know basic derivatives but I'm confused about the product rule.
>
> Please:
>
> 1. Remind me of the product rule
> 2. Apply it step by step
> 3. Give me 2 similar problems to practice
> 4. Show me how to check my answer"

### Study Materials

Prepare for success:

* **Study Guides**: "Create a study guide for AP Chemistry exam"
* **Flashcards**: "Generate 50 flashcards for Spanish vocabulary"
* **Practice Tests**: "Create a practice quiz on US History 1900-1950"
* **Summary Notes**: "Summarize Chapter 5 of my biology textbook"
* **Cheat Sheets**: "Create a one-page reference for Python syntax"

**Example prompt:**

> "Create a comprehensive study guide for the AWS Solutions Architect exam:
>
> Cover:
>
> * Key services and when to use them
> * Networking concepts
> * Security best practices
> * Cost optimization strategies
>
> Format: Clear sections, bullet points, diagrams where helpful
> Include: Practice questions after each section"

### Coding & Tech Learning

Level up your skills:

* **Language Learning**: "Teach me Python from zero to building a web app"
* **Code Review**: "Review my code and explain how to improve it"
* **Project Tutorials**: "Walk me through building a REST API step by step"
* **Concept Deep Dives**: "Explain how Docker containers actually work"

**Example prompt:**

> "Teach me React hooks:
>
> My level: I know basic JavaScript and HTML/CSS, never used React
>
> Structure:
>
> 1. What problem do hooks solve?
> 2. useState with simple examples
> 3. useEffect with practical use cases
> 4. When to use which hook
> 5. A mini-project putting it together
>
> Include code examples I can run."

### Language Learning

Master new languages:

* **Grammar Explanations**: "Explain Japanese particles with examples"
* **Conversation Practice**: "Practice ordering food in French"
* **Writing Feedback**: "Check my Spanish essay and explain my mistakes"
* **Vocabulary Building**: "Teach me 20 essential business Chinese phrases"

---

## Learning Styles

Tell CellCog how you learn best:

| Style | Ask For |
| --- | --- |
| **Visual** | Diagrams, charts, infographics |
| **Examples** | Multiple worked examples, real-world applications |
| **Analogies** | Comparisons to familiar concepts |
| **Step-by-Step** | Detailed breakdowns, numbered procedures |
| **Big Picture** | Overview first, then details |
| **Hands-On** | Practice problems, projects |

---

## Subjects

CellCog can help with virtually any subject:

**STEM:**

* Mathematics (all levels through advanced calculus and beyond)
* Physics, Chemistry, Biology
* Computer Science and Programming
* Statistics and Data Science
* Engineering concepts

**Humanities:**

* History and Social Studies
* Literature and Writing
* Philosophy
* Languages
* Psychology

**Professional:**

* Business and Finance
* Marketing
* Project Management
* Design
* Legal concepts

**Tech Skills:**

* Programming languages
* Cloud platforms (AWS, GCP, Azure)
* DevOps and infrastructure
* Data engineering
* AI/ML concepts

---

## Chat Mode for Learning

| Scenario | Recommended Mode |
| --- | --- |
| Homework help, concept explanations, practice problems | `"agent"` |
| Comprehensive study guides, full curriculum design, deep research | `"agent team"` |

**Use `"agent"` for most learning.** Quick explanations, homework help, and study materials execute well in agent mode.

**Use `"agent team"` for comprehensive learning** - full course outlines, research papers, or when you need multi-source synthesis.

---

## Example Prompts

**Concept explanation:**

> "Explain the concept of recursion in programming:
>
> My level: Beginner programmer, comfortable with loops
>
> I need:
>
> * Clear definition
> * Visual representation
> * 3 progressively harder examples (factorial, fibonacci, tree traversal)
> * Common mistakes to avoid
> * When to use recursion vs iteration
>
> Language: Python"

**Exam prep:**

> "Create a study plan for the GRE:
>
> Timeline: 2 months
> Goal: 320+ score
> Weak areas: Vocabulary and geometry
>
> Include:
>
> * Weekly schedule
> * Resources to use
> * Practice test strategy
> * Day-before checklist
>
> Make it realistic for someone working full-time."

**Language practice:**

> "Help me practice Japanese:
>
> Level: JLPT N4
> Focus: Conversational situations
>
> Create a dialogue practice:
>
> * Scenario: Asking for directions in Tokyo
> * Include vocabulary list
> * Grammar points used
> * Cultural notes
> * Variations to practice
>
> Use romaji and kanji with hiragana readings."

---

## Tips for Better Learning

1. **State your level**: "Complete beginner" vs "I understand the basics" changes everything.
2. **Ask why**: Don't just ask for answers. Ask for explanations of the reasoning.
3. **Request practice**: Learning happens through doing. Ask for practice problems.
4. **Admit confusion**: "I don't understand the part where..." helps CellCog target explanations.
5. **Build on previous**: Reference what you already understand to get appropriate explanations.
6. **Active recall**: Ask CellCog to quiz you, not just explain. Testing improves retention.

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

- AI tutoring and education powered by CellCog
- Study guides, exam prep,
  coding tutorials, language
- 触发关键词: education, powered, learn, cellcog, study, cog, tutoring

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

### Q1: 如何开始使用Learn Cog？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Learn Cog有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
