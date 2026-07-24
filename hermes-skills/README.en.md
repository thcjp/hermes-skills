# Hermes Skills

> AI Agent Skill Library · Categorized Index

[English](README.en.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

## About

This repository hosts **1218** AI agent skills (759 free + 459 paid) in the [agentskills.io](https://agentskills.io) standard format, compatible with Claude Code / Cursor / Codex / Gemini CLI and other agent platforms. Skills are organized into the 14 categories below, each split into `free/` (free) and `paid/` (paid) subdirectories.

Of these, **459** are paid skills licensed under Proprietary terms; please review the license information in each skill's directory before use. The free skills are licensed under the MIT open-source license and can be freely used and modified.

## Category overview

| Category | Free skills | Paid skills | Total | Description |
|---|---|---|---|---|
| [Agents](Agents/README.md) | 20 | 27 | 47 | Agents — AI agent frameworks, orchestration and multi-agent collaboration tools. |
| [Automation](Automation/README.md) | 20 | 238 | 258 | Automation — Workflow automation, scheduled tasks and process orchestration tools. |
| [Communication](Communication/README.md) | 56 | 12 | 68 | Communication — Messaging, email, notifications and social communication tools. |
| [Creative](Creative/README.md) | 124 | 47 | 171 | Creative — Content creation, image/music generation, writing and visual design tools. |
| [Development](Development/README.md) | 194 | 35 | 229 | Development — Coding, code quality, databases, frontend and DevOps tooling. |
| [Finance](Finance/README.md) | 34 | 10 | 44 | Finance — Financial analysis, investing, tax and cryptocurrency tools. |
| [Integrations](Integrations/README.md) | 5 | 0 | 5 | Integrations — Third-party platform and API integration connectors. |
| [Knowledge](Knowledge/README.md) | 50 | 49 | 99 | Knowledge — Notes, knowledge bases, knowledge graphs and document management tools. |
| [Lifestyle](Lifestyle/README.md) | 12 | 0 | 12 | Lifestyle — Weather, travel, health, smart home and daily-life tools. |
| [Operations](Operations/README.md) | 41 | 17 | 58 | Operations — Cloud, infrastructure, networking and systems monitoring/operations tools. |
| [Other](Other/README.md) | 0 | 0 | 0 | Other — Miscellaneous tools not fitting the above categories. |
| [Productivity](Productivity/README.md) | 69 | 2 | 71 | Productivity — Task management, scheduling, office and personal-efficiency tools. |
| [Research](Research/README.md) | 87 | 3 | 90 | Research — Information retrieval, data analysis, news and academic research tools. |
| [Security](Security/README.md) | 47 | 19 | 66 | Security — Security auditing, vulnerability scanning, privacy and compliance tools. |
| **Total** | **759** | **459** | **1218** | — |

## Directory structure

```
hermes-skills/
├── README.md            # Main index (Simplified Chinese)
├── README.zh-CN.md      # 简体中文
├── README.zh-TW.md      # 繁體中文
├── README.en.md         # English
├── Agents/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 20
│   └── paid/            # 27
├── Automation/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 20
│   └── paid/            # 238
├── Communication/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 56
│   └── paid/            # 12
├── Creative/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 124
│   └── paid/            # 47
├── Development/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 194
│   └── paid/            # 35
├── Finance/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 34
│   └── paid/            # 10
├── Integrations/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 5
│   └── paid/            # 0
├── Knowledge/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 50
│   └── paid/            # 49
├── Lifestyle/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 12
│   └── paid/            # 0
├── Operations/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 41
│   └── paid/            # 17
├── Other/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 0
│   └── paid/            # 0
├── Productivity/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 69
│   └── paid/            # 2
├── Research/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 87
│   └── paid/            # 3
├── Security/
│   ├── README.md        # Category description (3 languages)
│   ├── free/            # 47
│   └── paid/            # 19
```

## Usage

1. Clone this repository.
2. Copy the desired skill directory (e.g. `Development/free/git-cli-tool-free/`) into your agent's skills folder:
   - **Claude Code**: `.claude/skills/`
   - **Cursor**: `.cursor/skills/`
   - **Codex**: reference the skill path in config
   - **Gemini CLI**: add to the skill search path
3. The skill becomes available automatically in the agent session.

---

License: Free skills MIT | Paid skills Proprietary

Last updated: July 25, 2026