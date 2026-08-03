---
slug: bsession
name: bsession
version: "0.1.0"
displayName: browser
summary: "浏览器自动化环境:一次性抓取网站信息、创建持久会话,灵活适配不同场景需求"
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
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
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

## 差异化优势

### 差异化优势

bsession与同类方案相比，具有以下差异化优势：

- **灵活的脚本编写**：bsession支持使用Python编写脚本，用户可以根据自己的需求定制脚本，实现复杂的自动化任务。
- **持久化会话**：bsession支持创建持久化会话，用户可以在会话中保存状态，方便后续操作。
- **跨平台支持**：bsession支持Windows、macOS和Linux操作系统，用户可以在不同的平台上使用bsession。
- **易于集成**：bsession可以与其他工具和平台集成，例如Jenkins、GitLab等，方便用户进行自动化工作流。

## 同类方案对比

### 同类方案对比

与同类方案相比，bsession具有以下优势：

- **Selenium**：Selenium是一个流行的自动化测试工具，但它需要编写大量的代码，且学习曲线较陡峭。bsession使用Python编写脚本，学习曲线更平缓。
- **Playwright**：Playwright是一个现代的自动化测试工具，它支持多种编程语言，但bsession在性能和易用性方面更具优势。
- **Puppeteer**：Puppeteer是一个Node.js库，用于通过DevTools协议控制Chrome或Chromium。bsession与Puppeteer类似，但bsession支持Python，更适合Python开发者。

## 解决的痛点

### 解决的真实验证痛点

bsession解决了以下真实验证痛点：

- **自动化重复性任务**：bsession可以帮助用户自动化重复性任务，提高工作效率。
- **数据抓取**：bsession可以帮助用户从网站抓取数据，为数据分析提供数据源。
- **自动化测试**：bsession可以帮助用户进行自动化测试，提高软件质量。
- **爬虫开发**：bsession可以帮助用户开发爬虫程序，从网站抓取大量数据。

## 技术或方法创新点

### 技术或方法创新点

bsession在技术或方法上具有以下创新点：

- **Python脚本编写**：bsession支持使用Python编写脚本，这使得用户可以方便地实现复杂的自动化任务。
- **持久化会话**：bsession支持创建持久化会话，用户可以在会话中保存状态，方便后续操作。
- **跨平台支持**：bsession支持Windows、macOS和Linux操作系统，这使得用户可以在不同的平台上使用bsession。
- **易于集成**：bsession可以与其他工具和平台集成，例如Jenkins、GitLab等，方便用户进行自动化工作流。

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 场景不足

### 补充使用场景

除了当前文档中提到的使用场景外，bsession还可以应用于以下场景：

- **数据抓取**：bsession可以用于从网站抓取数据，例如产品价格、用户评论等。
- **自动化测试**：bsession可以用于自动化测试网站的功能和性能。
- **爬虫开发**：bsession可以用于开发爬虫程序，从网站抓取大量数据。
- **自动化报告生成**：bsession可以用于自动化生成报告，例如网站分析报告、产品评测报告等。

这些场景可以帮助用户更有效地使用bsession，提高工作效率。

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

## 错误处理

### 错误处理指南

在bsession的使用过程中，可能会遇到以下错误情况：

- **bsession容器未启动**：请确保容器已启动，或者使用`docker compose up -d`命令启动容器。
- **网络错误**：请检查您的网络连接是否正常，并确保bsession容器可以访问目标服务器。
- **配置错误**：请检查您的配置文件是否正确，并确保所有必需的参数都已设置。
- **脚本错误**：请检查您的脚本是否存在语法错误或逻辑错误，并确保所有依赖项都已正确安装。

对于每种错误，以下是一些可能的解决方法：

- **bsession容器未启动**：使用`docker ps`命令检查容器状态，如果容器未启动，则使用`docker compose up -d`命令启动容器。
- **网络错误**：检查您的网络连接是否正常，并确保bsession容器可以访问目标服务器。如果问题仍然存在，请尝试更换网络环境。
- **配置错误**：检查您的配置文件是否正确，并确保所有必需的参数都已设置。如果问题仍然存在，请参考bsession的官方文档。
- **脚本错误**：检查您的脚本是否存在语法错误或逻辑错误，并确保所有依赖项都已正确安装。如果问题仍然存在，请参考bsession的官方文档或寻求社区支持。

## 常见问题

### Q1: 如何开始使用browser？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: browser有什么限制？
A: 请参考已知限制章节了解具体限制。

## FAQ

### Q1: 如何开始使用browser？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 如何处理bsession容器未启动的情况？
A: 如果在执行bsession命令时遇到容器未启动的情况，请先检查容器是否正在运行。可以使用以下命令检查容器状态：
```bash
docker ps
```
如果容器未运行，请使用以下命令启动容器：
```bash
docker compose up -d
```

### Q3: 如何处理网络错误？
A: 如果遇到网络错误，例如连接超时或无法连接到目标服务器，请检查您的网络连接是否正常。如果问题仍然存在，请尝试以下操作：
- 确保您的网络设置允许访问bsession容器。
- 检查bsession容器是否配置了正确的代理设置。
- 如果您使用的是代理，请确保代理服务器地址和端口正确。

### Q4: 如何查看bsession的日志？
A: 您可以使用以下命令查看bsession的日志：
```bash
docker logs <container_name>
```
其中<container_name>是bsession容器的名称。

### Q5: 如何更新bsession到最新版本？
A: 您可以使用以下命令更新bsession到最新版本：
```bash
docker pull <image_name>
```
其中<image_name>是bsession容器的镜像名称。然后，您可以使用以下命令重启容器以应用更新：
```bash
docker restart <container_name>
```

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

## 边界条件

### 边界条件

bsession在处理边界条件时需要注意以下情况：

- **空URL**：如果用户提供的URL为空，bsession应返回错误信息，并提示用户输入有效的URL。
- **无效的URL**：如果用户提供的URL无效，bsession应返回错误信息，并提示用户输入有效的URL。
- **不存在的脚本**：如果用户尝试运行一个不存在的脚本，bsession应返回错误信息，并提示用户输入有效的脚本名称。
- **不存在的会话**：如果用户尝试查看一个不存在的会话，bsession应返回错误信息，并提示用户输入有效的会话名称。

对于这些边界条件，bsession应采取以下措施：

- 对于空URL，bsession应返回错误信息，并提示用户输入有效的URL。
- 对于无效的URL，bsession应返回错误信息，并提示用户输入有效的URL。
- 对于不存在的脚本，bsession应返回错误信息，并提示用户输入有效的脚本名称。
- 对于不存在的会话，bsession应返回错误信息，并提示用户输入有效的会话名称。
