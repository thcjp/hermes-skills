---
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
summary: "桥接Azure Claude与Skill平台的轻量Node代理"
---
# Azure llm-provider Proxy

A lightweight Node.js proxy that bridges Azure llm-provider with Skill平台.

## The Problem

Skill平台 constructs API URLs like this:

```javascript
const endpoint = `${baseUrl}/chat/completions`;
```

Azure llm-provider requires:

```text
https://{resource}.llm-provider.azure.com/llm-provider/deployments/{model}/chat/completions?api-version=2025-01-01-preview
```

When `api-version` is in the baseUrl, Skill平台's path append breaks it.

## Quick Setup

### 1. Configure and Run the Proxy

```bash
export AZURE_OPENAI_ENDPOINT="your-resource.llm-provider.azure.com"
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
        "api": "llm-provider-completions",
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

**Content Filter Errors:** Azure has aggressive content filtering — some prompts that work on llm-provider may get blocked.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
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

- This skill is a disclosed local proxy for routing OpenClaw requests
  to a user-configured Azure Op
- 触发关键词: local, azure, disclosed, proxy, llm-provider, skill

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 常见问题

### Q1: 如何开始使用Azure llm-provider Proxy？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Azure llm-provider Proxy有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
- 依赖云服务，需要网络连接
- 本地运行，不支持多设备同步
