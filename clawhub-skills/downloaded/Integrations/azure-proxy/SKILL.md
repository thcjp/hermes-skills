---
slug: azure-proxy
name: azure-proxy
version: "1.0.0"
displayName: Azure OpenAI Proxy
summary: This skill is a disclosed local proxy for routing OpenClaw requests to a
  user-configured Azure Op...
license: MIT
description: |-
  This skill is a disclosed local proxy for routing OpenClaw requests
  to a user-configured Azure Op...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: local, azure, disclosed, proxy, openai, skill
tags:
- Integrations
tools:
- read
- exec
---

# Azure OpenAI Proxy

A lightweight Node.js proxy that bridges Azure OpenAI with Skill平台.

## The Problem

Skill平台 constructs API URLs like this:

```javascript
const endpoint = `${baseUrl}/chat/completions`;
```

Azure OpenAI requires:

```text
https://{resource}.openai.azure.com/openai/deployments/{model}/chat/completions?api-version=2025-01-01-preview
```

When `api-version` is in the baseUrl, Skill平台's path append breaks it.

## Quick Setup

### 1. Configure and Run the Proxy

```bash
export AZURE_OPENAI_ENDPOINT="your-resource.openai.azure.com"
export AZURE_OPENAI_DEPLOYMENT="gpt-4o"
export AZURE_OPENAI_API_VERSION="2025-01-01-preview"

node scripts/server.js
```

### 2. Configure Skill平台 Provider

Add to `~/.skill-platform/skill-platform.json`:

```json
{
  "models": {
    "providers": {
      "azure-gpt4o": {
        "baseUrl": "http://127.0.0.1:18790",
        "apiKey": "YOUR_AZURE_API_KEY",
        "api": "openai-completions",
        "authHeader": false,
        "headers": {
          "api-key": "YOUR_AZURE_API_KEY"
        },
        "models": [
          { "id": "gpt-4o", "name": "GPT-4o (Azure)" }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "models": {
        "azure-gpt4o/gpt-4o": {}
      }
    }
  }
}
```

**Important:** Set `authHeader: false` — Azure uses `api-key` header, not Bearer tokens.

### 3. (Optional) Use for Subagents

Save Azure credits by routing automated tasks through Azure:

```json
{
  "agents": {
    "defaults": {
      "subagents": {
        "model": "azure-gpt4o/gpt-4o"
      }
    }
  }
}
```

## Run as systemd Service

Copy the template and configure:

```bash
mkdir -p ~/.config/systemd/user
cp scripts/azure-proxy.service ~/.config/systemd/user/

nano ~/.config/systemd/user/azure-proxy.service

systemctl --user daemon-reload
systemctl --user enable azure-proxy
systemctl --user start azure-proxy
```

## Environment Variables

| Variable | Default | Description |
| --- | --- | --- |
| `AZURE_PROXY_PORT` | `18790` | Local proxy port |
| `AZURE_PROXY_BIND` | `127.0.0.1` | Bind address |
| `AZURE_OPENAI_ENDPOINT` | — | Azure resource hostname |
| `AZURE_OPENAI_DEPLOYMENT` | `gpt-4o` | Deployment name |
| `AZURE_OPENAI_API_VERSION` | `2025-01-01-preview` | API version |

## Health Check

```bash
curl http://localhost:18790/health
```

## Troubleshooting

**404 Resource not found:** Check endpoint hostname and deployment name match Azure Portal.

**401 Unauthorized:** API key is wrong or expired.

**Content Filter Errors:** Azure has aggressive content filtering — some prompts that work on OpenAI may get blocked.

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
