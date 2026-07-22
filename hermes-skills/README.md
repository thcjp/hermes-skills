# Hermes Skills

> 759 个免费 AI 智能体技能，采用 [agentskills.io](https://agentskills.io) 标准格式

[English](README.en.md) | [简体中文](README.md) | [繁體中文](README.zh-TW.md)

## 关于

本仓库包含 759 个精心整理的免费 AI 智能体技能，每个技能均采用 agentskills.io 标准格式打包。这些技能兼容主流 AI 编程智能体：

- **Claude Code** (Anthropic)
- **Cursor** (Anysphere)
- **Codex** (OpenAI)
- **Gemini CLI** (Google)
- 任何支持 SKILL.md 标准的智能体平台

## 目录结构

每个技能是一个独立的目录，包含一个 `SKILL.md` 文件：

```
hermes-skills/
├── ad-creative-intel-free/
│   └── SKILL.md
├── aws-agent-orchestrator-free/
│   └── SKILL.md
├── ...
└── README.md
```

## 技能格式

每个 `SKILL.md` 文件遵循 agentskills.io 标准：

```yaml
---
name: skill-name-free
description: 技能的简要描述
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

# 技能名称

## 描述
技能功能的详细说明...

## 用法
如何使用此技能...
```

## 分类

技能按多个类别组织：

| 类别 | 数量 | 示例 |
|------|------|------|
| 自动化与工作流 | ~60 | cron-scheduler, task-queue-manager, workflow-orchestrator |
| 通讯 | ~50 | discord-toolkit, slack-hub-tool, telegram-chat-tool |
| 创意与设计 | ~80 | logo-design-tool, ui-ux-toolkit, video-producer-tool |
| 开发工具 | ~70 | git-cli-tool, docker-essentials, code-analysis-toolkit |
| 记忆与上下文 | ~25 | context-compressor, memory-fortress, neural-context-engine |
| 生产力 | ~50 | excel-ninja, notes-sync-cli, schedule-manager |
| 安全 | ~15 | encryption-tool, ssl-toolkit, aegis-security |
| 数据与分析 | ~30 | data-analysis-toolkit, knowledge-graph-builder |
| AI 与 LLM | ~40 | llm-provider-tool, prompt-architect, ai-image-gen-tool |
| 其他 | ~339 | 各类专用工具 |

## 使用方法

### Claude Code
1. 克隆本仓库
2. 将任意技能目录复制到 `.claude/skills/` 文件夹
3. 技能将自动在 Claude Code 会话中可用

### Cursor
1. 克隆本仓库
2. 将任意技能目录复制到 `.cursor/skills/` 文件夹
3. 重启 Cursor 以加载技能

### Codex
1. 克隆本仓库
2. 在 Codex 配置中引用技能路径

### Gemini CLI
1. 克隆本仓库
2. 将技能目录添加到 Gemini CLI 的技能搜索路径中

## 质量保证

所有技能均通过 6 层质量审计：
- **第 1-3 层**：格式验证（YAML 前置元数据、必填字段、结构）
- **第 4 层**：功能验证（任务定义、输入/输出、错误处理）
- **第 5 层**：可销售性评估（市场价值、目标受众、差异化）
- **第 6 层**：内容真实性（无模板填充、真实可执行代码）

## 开源协议

MIT 协议 - 详情见 [LICENSE](LICENSE)

## 相关平台

这些技能同时发布于：
- **SkillHub** - 中文 AI 技能市场（商业化变现）
- **ClawHub** - 国际开源技能生态

## 最后更新

2026 年 7 月
