---
slug: docker-sandbox
name: docker-sandbox
version: "1.0.0"
displayName: Docker Sandbox
summary: Create and manage Docker sandboxed VM environments for safe agent execution.
  Use when running unt...
license: MIT
description: |-
  Create and manage Docker sandboxed VM environments for safe agent execution.
  Use when running unt...

  核心能力:

  - 运维工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 系统运维、监控告警、资源管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: environments, create, docker, sandboxed, manage, sandbox
tags:
- Operations
tools:
- read
- exec
---

# Docker Sandbox

Run agents and commands in **isolated VM environments** using Docker Desktop's sandbox feature. Each sandbox gets its own lightweight VM with filesystem isolation, network proxy controls, and workspace mounting via virtiofs.

## When to Use

* Exploring **untrusted packages** or skills before installing them system-wide
* Running **arbitrary code** from external sources safely
* Testing **destructive operations** without risking the host
* Isolating **agent workloads** that need network access controls
* Setting up **reproducible environments** for experiments

## Requirements

* Docker Desktop 4.49+ with the `docker sandbox` plugin
* Verify: `docker sandbox version`

## Quick Start

### Create a sandbox for the current project

```bash
docker sandbox create --name my-sandbox claude .
```

This creates a VM-isolated sandbox with:

* The current directory mounted via virtiofs
* Node.js, git, and standard dev tools pre-installed
* Network proxy with allowlist controls

### Run commands inside

```bash
docker sandbox exec my-sandbox node --version
docker sandbox exec my-sandbox npm install -g some-package
docker sandbox exec -w /path/to/workspace my-sandbox bash -c "ls -la"
```

### Run an agent directly

```bash
docker sandbox run claude . -- -p "What files are in this project?"

docker sandbox run my-sandbox -- -p "Analyze this codebase"
```

## Commands Reference

### Lifecycle

```bash
docker sandbox create --name <name> <agent> <workspace-path>

docker sandbox run <agent> <workspace> [-- <agent-args>...]
docker sandbox run <existing-sandbox> [-- <agent-args>...]

docker sandbox exec [options] <sandbox> <command> [args...]
  -e KEY=VAL          # Set environment variable
  -w /path            # Set working directory
  -d                  # Detach (background)
  -i                  # Interactive (keep stdin open)
  -t                  # Allocate pseudo-TTY

docker sandbox stop <sandbox>

docker sandbox rm <sandbox>

docker sandbox ls

docker sandbox reset

docker sandbox save <sandbox>
```

### Network Controls

The sandbox includes a network proxy for controlling outbound access.

```bash
docker sandbox network proxy <sandbox> --allow-host example.com
docker sandbox network proxy <sandbox> --allow-host api.github.com

docker sandbox network proxy <sandbox> --block-host malicious.com

docker sandbox network proxy <sandbox> --block-cidr 10.0.0.0/8

docker sandbox network proxy <sandbox> --bypass-host localhost

docker sandbox network proxy <sandbox> --policy deny  # Block everything, then allowlist
docker sandbox network proxy <sandbox> --policy allow  # Allow everything, then blocklist

docker sandbox network log <sandbox>
```

### Custom Templates

```bash
docker sandbox create --template my-custom-image:latest claude .

docker sandbox save my-sandbox
```

## Workspace Mounting

The workspace path on the host is mounted into the sandbox via virtiofs. The mount path inside the sandbox preserves the host path structure:

| Host OS | Host Path | Sandbox Path |
| --- | --- | --- |
| Windows | `H:\Projects\my-app` | `/h/Projects/my-app` |
| macOS | `/Users/me/projects/my-app` | `/Users/me/projects/my-app` |
| Linux | `/home/me/projects/my-app` | `/home/me/projects/my-app` |

The agent's home directory is `/home/agent/` with a symlinked `workspace/` directory.

## Environment Inside the Sandbox

Each sandbox VM includes:

* **Node.js** (v20.x LTS)
* **Git** (latest)
* **Python** (system)
* **curl**, **wget**, standard Linux utilities
* **npm** (global install directory at `/usr/local/share/npm-global/`)
* **Docker socket** (at `/run/docker.sock` - Docker-in-Docker capable)

### Proxy Configuration (auto-set)

```text
HTTP_PROXY=http://host.docker.internal:3128
HTTPS_PROXY=http://host.docker.internal:3128
NODE_EXTRA_CA_CERTS=/usr/local/share/ca-certificates/proxy-ca.crt
SSL_CERT_FILE=/usr/local/share/ca-certificates/proxy-ca.crt
```

**Important**: Node.js `fetch` (undici) does NOT respect `HTTP_PROXY` env vars by default. For npm packages that use `fetch`, create a require hook:

```javascript
// /tmp/proxy-fix.js
const proxy = process.env.HTTPS_PROXY || process.env.HTTP_PROXY;
if (proxy) {
  const { ProxyAgent } = require('undici');
  const agent = new ProxyAgent(proxy);
  const origFetch = globalThis.fetch;
  globalThis.fetch = function(url, opts = {}) {
    return origFetch(url, { ...opts, dispatcher: agent });
  };
}
```

Run with: `node -r /tmp/proxy-fix.js your-script.js`

## Patterns

### Safe Package Exploration

```bash
docker sandbox create --name pkg-test claude .

docker sandbox network proxy pkg-test --policy deny
docker sandbox network proxy pkg-test --allow-host registry.npmjs.org
docker sandbox network proxy pkg-test --allow-host api.npmjs.org

docker sandbox exec pkg-test npm install -g suspicious-package
docker sandbox exec pkg-test bash -c "find /usr/local/share/npm-global/lib/node_modules/suspicious-package -name '*.js' | head -20"

docker sandbox network log pkg-test

docker sandbox rm pkg-test
```

### Persistent Dev Environment

```bash
docker sandbox create --name dev claude ~/projects/my-app

docker sandbox exec dev npm test
docker sandbox exec dev npm run build

docker sandbox save dev
```

### Locked-Down Agent Execution

```bash
docker sandbox create --name secure claude .
docker sandbox network proxy secure --policy deny
docker sandbox network proxy secure --allow-host api.openai.com
docker sandbox network proxy secure --allow-host github.com

docker sandbox run secure -- -p "Review this code for security issues"
```

## Troubleshooting

### "client version X is too old"

Update Docker Desktop to 4.49+. The sandbox plugin requires engine API v1.44+.

### "fetch failed" inside sandbox

Node.js `fetch` doesn't use the proxy. Use the proxy-fix.js require hook above, or use `curl` instead:

```bash
docker sandbox exec my-sandbox curl -sL https://api.example.com/data
```

### Path conversion on Windows (Git Bash / MSYS2)

Git Bash converts `/path` to `C:/Program Files/Git/path`. Prefix commands with:

```bash
MSYS_NO_PATHCONV=1 docker sandbox exec my-sandbox ls /home/agent
```

### Sandbox won't start after Docker update

```bash
docker sandbox reset  # Clears all sandbox state
```

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
