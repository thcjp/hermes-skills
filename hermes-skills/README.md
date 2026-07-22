# Hermes Skills Collection

> 759 production-ready AI skills in [agentskills.io](https://agentskills.io) standard format.

## Overview

This repository contains 759 free AI skills converted from SkillHub format to the agentskills.io standard. Each skill is a self-contained Markdown document with YAML frontmatter that can be loaded by any compatible AI agent runtime (Claude Code, Cursor, Codex, Gemini CLI, etc.).

## Skill Format

Each skill follows the agentskills.io specification:

```yaml
---
name: "skill-name"
description: "What this skill does (max 1024 chars)"
license: MIT
allowed-tools: read write exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "Human-friendly name"
  version: "1.0.0"
  summary: "One-line summary"
  tags:
    - category
    - topic
---
# Skill Title

...skill content...
```

## Categories

Skills span multiple categories including:

- Development & Code (API, backend, frontend, DevOps)
- Data & Analytics (CSV, JSON, database, visualization)
- Content & Writing (blog, copywriting, documentation)
- Productivity (calendar, email, task management)
- Design (UI/UX, diagrams, presentations)
- Research (web search, news, RSS)
- Communication (Discord, Telegram, social media)
- Security (encryption, audit, firewall)
- Cloud & Infrastructure (AWS, Azure, GCP, Docker, K8s)

## Quality Assurance

All 759 skills have passed a 6-layer quality audit:

| Layer | Check | Result |
|-------|-------|--------|
| 1-3 | Format (frontmatter, fields, encoding) | 100% |
| 4 | Functional quality (instructions, code, I/O) | 100% A+B |
| 5 | Sellability (depth, completeness, UX) | 100% A+B |
| 6 | Content authenticity (no template padding) | 100% A+B |

## Usage

### Install via agentskills.io CLI

```bash
# Install a specific skill
agentskills install <skill-name>

# List available skills
agentskills list
```

### Manual Installation

Copy the desired skill's `SKILL.md` file to your agent's skills directory:

```bash
# Claude Code
cp <skill-name>/SKILL.md ~/.claude/skills/

# Cursor
cp <skill-name>/SKILL.md ~/.cursor/skills/
```

## License

All skills are licensed under MIT unless otherwise specified in the skill's frontmatter.

## Contributing

These skills are auto-generated and quality-audited. For issues or improvements, please open an issue describing the skill and the problem.
