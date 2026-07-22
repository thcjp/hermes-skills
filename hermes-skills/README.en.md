# Hermes Skills

> 759 free AI agent skills in [agentskills.io](https://agentskills.io) format

[English](README.en.md) | [简体中文](README.md) | [繁體中文](README.zh-TW.md)

## About

This repository contains a curated collection of 759 free AI agent skills, each packaged in the agentskills.io standard format. These skills are compatible with popular AI coding agents including:

- **Claude Code** (Anthropic)
- **Cursor** (Anysphere)
- **Codex** (OpenAI)
- **Gemini CLI** (Google)
- Any agent platform that supports the SKILL.md standard

## Directory Structure

Each skill is a self-contained directory with a `SKILL.md` file:

```
hermes-skills/
├── ad-creative-intel-free/
│   └── SKILL.md
├── aws-agent-orchestrator-free/
│   └── SKILL.md
├── ...
└── README.md
```

## Skill Format

Each `SKILL.md` file follows the agentskills.io standard:

```yaml
---
name: skill-name-free
description: Brief description of the skill
license: MIT
allowed-tools: read write
compatibility:
  - claude-code
  - cursor
  - codex
  - gemini-cli
metadata:
  version: 1.0.0
  category: productivity
  tags: [automation, workflow]
---

# Skill Name

## Description
Detailed description of what the skill does...

## Usage
How to use this skill...
```

## Categories

Skills are organized across multiple categories:

| Category | Count | Examples |
|----------|-------|---------|
| Automation & Workflow | ~60 | cron-scheduler, task-queue-manager, workflow-orchestrator |
| Communication | ~50 | discord-toolkit, slack-hub-tool, telegram-chat-tool |
| Creative & Design | ~80 | logo-design-tool, ui-ux-toolkit, video-producer-tool |
| Development Tools | ~70 | git-cli-tool, docker-essentials, code-analysis-toolkit |
| Memory & Context | ~25 | context-compressor, memory-fortress, neural-context-engine |
| Productivity | ~50 | excel-ninja, notes-sync-cli, schedule-manager |
| Security | ~15 | encryption-tool, ssl-toolkit, aegis-security |
| Data & Analytics | ~30 | data-analysis-toolkit, knowledge-graph-builder |
| AI & LLM | ~40 | llm-provider-tool, prompt-architect, ai-image-gen-tool |
| Other | ~339 | Various specialized tools |

## Usage

### With Claude Code
1. Clone this repository
2. Copy any skill directory to your `.claude/skills/` folder
3. The skill is automatically available in your Claude Code session

### With Cursor
1. Clone this repository
2. Copy any skill directory to your `.cursor/skills/` folder
3. Restart Cursor to load the skill

### With Codex
1. Clone this repository
2. Reference the skill path in your Codex configuration

### With Gemini CLI
1. Clone this repository
2. Add the skill directory to Gemini CLI's skill search path

## Quality Assurance

All skills pass a 6-layer quality audit:
- **Layer 1-3**: Format validation (YAML frontmatter, required fields, structure)
- **Layer 4**: Functional validation (task definition, input/output, error handling)
- **Layer 5**: Sellability assessment (market value, target audience, differentiation)
- **Layer 6**: Content authenticity (no template padding, real executable code)

## License

MIT License - see [LICENSE](LICENSE) for details.

## Related Platforms

These skills are also published on:
- **SkillHub** - Chinese AI skill marketplace (monetization)
- **ClawHub** - International open-source skill ecosystem

## Last Updated

July 2026
