---
slug: bsession
name: bsession
version: "0.1.0"
displayName: browser
summary: Browser automation — setup the bsession environment, fetch info from a website
  (one-shot), create...
license: MIT-0
description: |-
  Browser automation — setup the bsession environment, fetch info from
  a website (one-shot), create。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
- Research
- Automation
tools:
  - - read
- exec
---

# browser

You help users automate browsers inside the bsession Docker container — whether it's initial setup, a quick interactive fetch, a scripted automation (one-shot or recurring), or debugging an existing session.

**This is a global skill** — it works from any repo. bsession is installed at `~/.bsession/`, and the `bsession` CLI is on PATH.

## Resolve paths

Before doing anything, determine how to reach bsession. Check in this order:

1. `bsession` on PATH → use `bsession`
2. `~/.bsession/bsession` exists → use `~/.bsession/bsession`
3. `./bsession` in current directory → use `./bsession`
4. None found but container is running (`docker exec agent-browser echo ok`) → use `docker exec agent-browser python3 /app/session.py` as the CLI

Similarly, resolve workspace:

1. `~/.bsession/workspace/` exists → use it
2. `./workspace/` in current directory → use it
3. Ask `docker exec agent-browser ls /workspace/conf` → use docker exec to access files

Use these resolved paths for **all** commands throughout the session.

## Constants (defaults)

* **BSESSION_HOME**: `~/.bsession/` — where bsession source + docker-compose live
* **WORKSPACE**: `~/.bsession/workspace/` (default, overridable) — or resolved per above
* **bsession CLI**: resolved per above

## Routing

Parse the user's slash command arguments:

* **No arguments or `list`** → List mode (show all available scripts and sessions)
* **`setup`** → Setup mode (install and configure bsession)
* **`fetch <url>`** → Fetch mode (interactive one-shot extraction, with option to persist)
* **`new <name>`** → Create mode (scaffold a script — one-shot or recurring)
* **`run <name>`** → Run mode (execute a saved session and show results)
* **Otherwise** → Debug mode (inspect/fix an existing session)

## Pre-check (all modes except setup)

Before running any mode except setup, verify the container is running:

```bash
docker exec agent-browser echo ok 2>/dev/null
```

If this fails, tell the user to either:

* Run `/browser setup` for a fresh install, or
* Run `docker compose up -d` from the bsession project directory

---

## List mode (`/browser` or `/browser list`)

Show all available scripts, their status, and what they do.

### Step 1: Get session status

```bash
bsession list
```

### Step 2: Read script docstrings

For each `.py` file in `~/.bsession/workspace/scripts/`, read the module docstring (the triple-quoted string at the top of the file).

### Step 3: Read conf files

For each `.conf` file in `~/.bsession/workspace/conf/`, read the `[env]` section to show current configuration.

### Step 4: Present as a table

Display a summary like:

```text
Session       Status    Type        Description
─────────────────────────────────────────────────────────────────
uscis         running   recurring   USCIS case status monitor
price-check   stopped   one-shot    Amazon product price scraper

Available commands:
  /browser <name>           debug a session
  /browser new <name>       create a new automation
  /browser fetch <url>      quick one-shot fetch
```

---

## Setup mode (`/browser setup`)

Run the install script:

```bash
bash ~/.skill-platform/workspace/skills/browser/scripts/install.sh
```

Or with options:

```bash
bash ~/.skill-platform/workspace/skills/browser/scripts/install.sh --workspace /path/to/workspace
bash ~/.skill-platform/workspace/skills/browser/scripts/install.sh --vnc-password secret
bash ~/.skill-platform/workspace/skills/browser/scripts/install.sh --repo https://github.com/gaxxx/bsession.git
```

Ask the user for custom options before running. The script handles Docker check, uv/Python install, image build, container start, and CLI setup.

---

## Fetch mode (`/browser fetch <url>`)

One-shot: open a URL, extract information, return it. No script, no conf file, no loop.

### Step 1: Find an available CDP port

```bash
docker exec agent-browser python3 -c "
import urllib.request
try:
    urllib.request.urlopen('http://localhost:9222/json/version', timeout=2)
    print('IN_USE')
except:
    print('FREE')
"
```

If 9222 is in use, try 9223, 9224, etc. Start a temporary Chrome on a free port:

```bash
docker exec agent-browser python3 -c "
import sys; sys.path.insert(0, '/app')
from lib.browser import start_chrome
pid = start_chrome(PORT, '/workspace/data/profile-tmp')
print(f'Chrome started, pid={pid}')
"
```

### Step 2: Navigate and extract

```bash
docker exec agent-browser agent-browser --cdp PORT open "URL"
sleep 5
docker exec agent-browser agent-browser --cdp PORT snapshot
```

Handle Cloudflare if detected:

```bash
docker exec agent-browser python3 -c "
import sys; sys.path.insert(0, '/app')
from lib.browser import ab, is_cloudflare, wait_for_cloudflare
snap = ab(PORT, 'snapshot')
if is_cloudflare(snap):
    wait_for_cloudflare(PORT, snap)
    snap = ab(PORT, 'snapshot')
print(snap)
"
```

### Step 3: Parse and interact

```bash
docker exec agent-browser agent-browser --cdp PORT fill REF "value"
docker exec agent-browser agent-browser --cdp PORT click REF
docker exec agent-browser agent-browser --cdp PORT snapshot
```

### Step 4: Return results

Parse the relevant information and present it cleanly.

### Step 5: Offer to persist

After returning results, always ask if the user wants to save as a reusable script. If yes, create a one-shot script + conf in `~/.bsession/workspace/`.

### Step 6: Cleanup

```bash
docker exec agent-browser python3 -c "
import sys; sys.path.insert(0, '/app')
from lib.browser import stop_chrome
stop_chrome(PORT)
"
```

---

## Create mode (`/browser new <name>`)

Ask the user:

1. What URL(s) to target
2. One-shot or recurring?
3. What to detect / extract
4. Where to send results (webhook, file, etc.)
5. Env vars needed

Then scaffold `~/.bsession/workspace/conf/<name>.conf` and `~/.bsession/workspace/scripts/<name>.py` following the conventions in the reference section below.

---

## Run mode (`/browser run <name>`)

1. Verify session exists: `bsession show <name>`
2. Run it: `bsession run <name>`
3. Wait and tail logs: `bsession logs <name> -n 50`
4. Present results. If failed, switch to debug mode.

---

## Debug mode (`/browser <session-id>`)

1. Gather state: `bsession list`, `bsession show <id>`, read logs and script
2. Diagnose: Cloudflare stuck, element not found, crash, wrong data, process dead
3. Fix the script or conf, then `bsession restart <id>`

---

## Script conventions

**Imports:**

```python
import os, re, sys, time
sys.path.insert(0, "/app")
from lib.browser import (
    ab, ab_quiet, find_ref, is_cloudflare, wait_for_cloudflare,
    send_webhook, make_logger,
)
```

**Config from env vars:**

```python
port = int(os.environ.get("CDP_PORT", 9222))
session_name = os.environ.get("SESSION_NAME", "<name>")
webhook_url = os.environ.get("N8N_WEBHOOK_URL", "")
check_interval = int(os.environ.get("CHECK_INTERVAL", 1800))
```

**Core pattern:** open URL → wait → snapshot → handle Cloudflare → find elements → interact → parse results

**One-shot:** execute and exit. **Recurring:** wrap in `while True` with sleep, compare state, webhook on change.

## Reference: lib/browser.py

* `ab(port, cmd, *args)` / `ab_quiet(port, cmd, *args)` — run agent-browser commands
* `find_ref(snapshot, pattern)` / `find_all_refs(snapshot, pattern)` — parse accessibility tree
* `is_cloudflare(snapshot)` / `wait_for_cloudflare(port, snapshot, ...)` — Cloudflare handling
* `send_webhook(url, payload)` — POST JSON to webhook
* `make_logger(session_name)` — create timestamped logger

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

- Browser automation — setup the bsession environment, fetch info from
  a website (one-shot), create
- 触发关键词: setup, automation, browser, bsession, environment

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用browser？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: browser有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
