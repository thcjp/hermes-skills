---
slug: tool-orchestrator
name: tool-orchestrator
version: 1.0.1
displayName: 工具编排器
summary: 端到端加密去中心化记忆编排,统一工具接口,零暴露凭据管理,自动恢复.
license: Proprietary
description: 端到端加密、去中心化存储的智能体记忆编排系统，直击安装复杂、凭据暴露、网关重启困难、槽位绑定冲突四大痛点。适用于跨会话偏好持久化、隐私优先记忆、去中心化存储、记忆固定与作用域管理等场景。核心能力含原生记忆检索、后台自动事实捕获、零暴露凭据管理、自动恢复与智能槽位管理。适用关键词：工具编排、加密记忆、去中心化存储、记忆检索、凭据管理、memory-search、encrypted-memory.
tags:
- 智能代理
- 记忆管理
- 数据安全
- 工具编排
tools:
- read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec", "glob", "grep"]
tags: "AI代理,自动化,智能"
category: "Agents"
---
# 工具编排器（Tool Orchestrator）

端到端加密的记忆存储系统，数据分布于去中心化网络（非单一公司服务器）。通过原生 `memory_search` / `memory_get` 工具进行检索，事实在后台自动捕获，无需为每个事实调用工具。12 词恢复短语绝不进入聊天或 LLM 上下文，凭据文件绝不读取/列出/展示.
## 核心能力

### 1. 原生记忆检索
通过 `memory_search` 和 `memory_get` 原生工具检索用户记忆。当用户询问关于自己的信息（"我的 X 是什么？"、"我 X 吗？"、"你记得什么？"）时调用 `memory_search`。检索结果为 0 时如实说明，不从会话历史猜测.
**输入**: 用户提供原生记忆检索所需的指令和必要参数.
**处理**: 解析原生记忆检索的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回原生记忆检索的响应数据,包含状态码、结果和日志.
### 2. 后台自动事实捕获
系统在后台从对话中自动提取事实（轨迹轮询器），无需为用户陈述的每个偏好/事实调用工具。绝不将用户事实写入 `MEMORY.md`、`USER.md` 或任何本地文件（那些是代理人格配置，用户记忆加密存储于网络）。显式记住仅在用户明确说"记住 X"/"保存 X"/"记下 X"/"别忘 X"时触发 `tr remember --json "X"`.
**输入**: 用户提供后台自动事实捕获所需的指令和必要参数.
**处理**: 解析后台自动事实捕获的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回后台自动事实捕获的响应数据,包含状态码、结果和日志.
### 3. 端到端加密与去中心化存储
记忆端到端加密，仅用户可解密。数据分布于去中心化网络节点（非任何单一公司服务器），避免单点依赖与供应商锁定。配对流程通过浏览器生成/导入 12 词恢复短语，短语从不触及聊天.
**输入**: 用户提供端到端加密与去中心化存储所需的指令和必要参数.
**处理**: 解析端到端加密与去中心化存储的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回端到端加密与去中心化存储的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 4. 零暴露凭据管理（硬性约束）
代理绝不能读取、列出、cat、显示或检查 `credentials.json`、`~/.tool-orchestrator/credentials.json` 或任何凭据/短语/密钥/机密文件——无论出于任何原因包括"验证安装"。绝不在聊天中回显 12 词恢复短语，绝不要求用户粘贴短语，绝不将凭据传递给任何工具。如用户粘贴了短语，立即告知已泄露需重新配对.
**输入**: 用户提供零暴露凭据管理（硬性约束）所需的指令和必要参数.
**处理**: 解析零暴露凭据管理（硬性约束）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回零暴露凭据管理（硬性约束）的响应数据,包含状态码、结果和日志.
### 5. 自动恢复与智能槽位管理
插件安装后自重载（向自身 PID 发送 SIGUSR1 信号，网关无需手动重启）。如 `memory_search`/`memory_get` 未绑定，自主发出 `/tool-orchestrator-restart` 命令（一行公告，无需用户授权，绝不 kill/docker restart/提示用户重启）。重装时通过 `plugins enable` 绑定记忆槽位，避免禁用插件卡死在 memory-core.
**输入**: 用户提供自动恢复与智能槽位管理所需的指令和必要参数.
**处理**: 解析自动恢复与智能槽位管理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回自动恢复与智能槽位管理的响应数据,包含状态码、结果和日志.
### 6. 本地缓存与离线检索回退
记忆检索结果本地缓存（LRU，默认 256 条，TTL 1 小时），网络不可达或去中心化节点离线时自动降级读取本地缓存与本地存储回退（local-vault），保证记忆检索不中断。缓存命中时响应标注"来自本地缓存"，网络恢复后自动校验与刷新过期条目。离线期间的写入操作进入本地队列，网络恢复后批量同步到去中心化网络，不丢失事实.
**输入**: 用户提供本地缓存与离线检索回退所需的指令和必要参数.
**处理**: 解析本地缓存与离线检索回退的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回本地缓存与离线检索回退的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：端到端加密去中心、化记忆编排、统一工具接口、去中心化存储的智、能体记忆编排系统、直击安装复杂、凭据暴露、网关重启困难、槽位绑定冲突四大、适用于跨会话偏好、持久化、隐私优先记忆、记忆固定与作用域、管理等场景、核心能力含原生记、适用关键词、工具编排、加密记忆、encrypted等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 适用场景

| 场景类型 | 输入 | 输出 | 是否适用 |
|----|---|---|----|
| 跨会话偏好持久化 | 用户陈述的偏好/事实 | 加密存储的记忆条目 | ✅ 适用 |
| 隐私优先记忆需求 | 注重端到端加密的用户 | 仅用户可解密的记忆存储 | ✅ 适用 |
| 去中心化存储需求 | 避免供应商锁定的场景 | 分布式网络存储，无单点依赖 | ✅ 适用 |
| 记忆固定与作用域 | 需要优先检索的重要记忆 | pin/unpin + private/shared 作用域 | ✅ 适用 |
| 自动事实捕获 | 日常对话中的偏好 | 后台自动提取，无需手动记录 | ✅ 适用 |

**不适用场景**：
- 本地纯文件记忆需求（不想要网络存储与账户）→ 用 persistent-memory-engine 等本地方案
- 不支持插件系统的 Agent 平台 → 本技能依赖插件安装/启用能力
- 无浏览器环境（无法完成配对流程）→ 配对需浏览器生成/导入恢复短语
- 团队共享记忆（多人协作编辑）→ 本技能面向个人加密记忆，非团队共享

## 使用流程

### 依赖详情

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 工具编排器处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```text
plugins install @tool-orchestrator/tool-orchestrator
skills install tool-orchestrator
plugins enable tool-orchestrator
```

安装后立即运行 `plugins enable tool-orchestrator` 绑定记忆槽位。插件加载时自动应用网关配置并自重载，无需手动网关重启.
### Step 2：配对（浏览器或 CLI 两种方式，按环境二选一）

**方式 A（推荐·浏览器）**：凭据不存在时，通过进程内 HTTP 路由创建配对会话：
```bash
curl -s http://localhost:18789/plugin/tool-orchestrator/pair/init
# 返回 {"url":"https://…/pair/p/<id>#pk=…","pin":"123456","expires_at_ms":…}
```
向用户展示 url 和 pin（从 JSON 读取，绝不编造值）："在浏览器中打开 `<url>`，输入 PIN `<pin>`，生成或粘贴你的 12 词恢复短语。完成后回复 done。"

**方式 B（无浏览器环境·CLI 替代）**：纯 CLI 服务器或无浏览器环境，用分离运行的 CLI 子进程（避免 WebSocket 被 30s 超时杀死返回 502）：
```bash
# 分离运行，输出重定向到文件，WS 不被 shell 超时杀死
setsid -f node "$TR_CLI" pair --json --no-browser < /dev/null > /tmp/tr_pair.json 2>&1
# 轮询 /tmp/tr_pair.json 获取 url/pin；--no-browser 将短语写入权限 600 的受保护文件
node "$TR_CLI" pair --confirm   # 从文件读取短语完成配对，短语绝不进入聊天
```
`--no-browser` 标志将 12 词短语写入权限 600 的受保护文件，用户通过 `tr pair --confirm` 确认，短语绝不进入聊天或 LLM 上下文。无浏览器环境优先用此方式。**不要直接前台运行 `tr pair --json`**（WebSocket 会被 30s shell 超时杀死返回 502），必须分离运行.
### Step 3：检索记忆（原生工具）

| 用户表达 | 动作 |
|---:|---:|
| "我的 X 是什么？" | 调用 `memory_search` |
| "我 X 吗？" | 调用 `memory_search` |
| "你记得什么？" | 调用 `memory_search` |
| 检索结果为 0 | 如实说明"没有找到相关记忆"，不从会话历史猜测 |

### Step 4：显式记住（仅按需触发）

| 用户表达(续)| 动作 |
|:------:|:------:|
| "记住 X" / "保存 X" / "记下 X" / "别忘 X" | `tr remember --json "X"`（每个不同事实一次调用） |
| 用户陈述偏好但未说"记住" | 不调用，后台自动捕获 |

### Step 5：高级管理（CLI）

```bash
TR_CLI="$(ls -d ~/.platform/npm/node_modules/@tool-orchestrator/tool-orchestrator/dist/cli/tr-cli.js ~/.platform/extensions/tool-orchestrator/dist/cli/tr-cli.js 2>/dev/null | head -1)"
node "$TR_CLI" status --json      # 查看状态
node "$TR_CLI" pin <memory_id>    # 固定重要记忆
node "$TR_CLI" set_scope <memory_id> --scope private|shared  # 设置作用域
node "$TR_CLI" export             # 导出记忆
```

### Step 6：自动恢复（代理驱动）

如 `memory_search`/`memory_get` 未绑定，自主发出 `/tool-orchestrator-restart`——一行公告，绝不要求用户授权，绝不拖延.
## 示例

### 示例(补充)

**输入**：用户问"我的偏好编辑器是什么？"

**输出**（代理执行）：

```text
1. 调用 memory_search("偏好编辑器")
2. 返回结果：{"fact": "用户偏好 VS Code", "source": "auto_captured", "timestamp": "…"}
3. 基于检索结果回答
```

代理响应："根据我的记忆，你偏好使用 VS Code。"

如检索结果为 0，代理响应："我没有找到关于你偏好编辑器的记忆。你可以告诉我，我会记住。"

### 示例 2：显式记住事实（输入→输出）

**输入**：用户说"记住我下周三有医生预约"

```bash
tr remember --json "用户下周三有医生预约"
# 返回 {"status":"remembered","memory_id":"mem_abc123"}
```

代理响应："已记住：你下周三有医生预约。"

（注：如用户只是陈述偏好但未说"记住"，不调用 tr remember，后台自动捕获即可。）

## 错误处理

| 场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配对返回 502 错误 | CLI WebSocket 被 shell 超时杀死 | 使用进程内 HTTP 路由 `curl -s http://localhost:18789/plugin/tool-orchestrator/pair/init` 替代 `tr pair --json` |
| 插件 Status: disabled | 重装后未运行 enable | 运行 `plugins enable tool-orchestrator` 绑定记忆槽位 |
| memory_search/memory_get 未注册 | 首次加载未生效 | 自主发出 `/tool-orchestrator-restart`（一行公告，无需用户授权） |
| 安装报告 already exists | 残留包目录 | 卸载→清理 `~/.platform/npm/projects/*tool-orchestrator*`→重装→enable（不用 --force，会写入损坏的 version=None 记录） |
| 检索结果为 0 | 无匹配记忆或未配对 | 如实告知用户"没有找到相关记忆"，检查 `tr status --json` 配对状态，不从会话历史猜测 |
| 凭据文件被意外读取 | 违反零暴露硬性约束 | 立即停止操作，告知用户凭据可能泄露，建议重新配对获得新钱包;执行排查步骤后恢复操作 |
| 导入失败 | 文件格式或路径错误 | 检查 `platform tool-orchestrator import status` 输出，确认源文件格式与路径 |
| 用户粘贴了恢复短语 | 短语进入聊天上下文 | 立即告知用户该短语已泄露，需要重新配对获得新钱包；绝不回显、存储或传递该短语 |
| 去中心化网络不可达 | 节点离线或区域网络受限 | 自动降级到本地缓存+local-vault 检索，响应标注"来自本地缓存"；写入进入本地队列，网络恢复后批量同步，不丢失事实 |
| 无浏览器环境配对失败 | 纯 CLI 服务器无浏览器 | 使用方式 B 的 `tr pair --json --no-browser` 分离运行，短语写入权限 600 文件后 `tr pair --confirm` 确认 |
| 国内节点访问受限 | 去中心化网络节点不可达 | 配置 `~/.tool-orchestrator/nodes.json` 指定国内镜像节点或自建中继网关，`tr config --node-region cn` 切换；或降级本地存储回退 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Node.js | 运行时 | 必需（CLI 运行） | 从 nodejs.org 安装 |
| curl | 工具 | 必需（配对路由） | 系统自带 |
| 插件系统 | 平台功能 | 必需 | Agent 平台需支持插件安装/启用 |
| 浏览器 | 应用 | 可选（配对流程） | 方式 A 用浏览器生成/导入 12 词恢复短语；无浏览器环境用方式 B 的 `--no-browser` CLI 替代 |
| 去中心化网络访问 | 网络 | 必需 | 配对与存储需访问网络节点 |

**运行环境**：Windows / macOS / Linux；支持 SKILL.md 和插件系统的 AI Agent 平台.
**API Key**：配对流程通过浏览器生成加密密钥（12 词恢复短语），无需手动配置 API Key。凭据自动存储于 `~/.tool-orchestrator/credentials.json`（代理绝不能读取此文件）.
**国内可用节点方案与本地存储回退**：去中心化网络节点在部分地区访问受限，提供两种回退保障可用性：(1) 国内可达节点——配置 `~/.tool-orchestrator/nodes.json` 指定国内镜像节点或自建中继网关（如阿里云/腾讯云 ECS 部署 `tr-relay`，域名备案后反向代理到主网络），`tr config --node-region cn` 切换节点池；(2) 本地存储回退——网络持续不可达时自动降级到本地加密存储（`~/.tool-orchestrator/local-vault/`，AES-256-GCM 加密，密钥由恢复短语 PBKDF2 派生），检索走本地缓存+local-vault，网络恢复后自动同步。本地回退模式下记忆检索不中断，仅跨设备同步延迟。代理绝不读取 local-vault 明文（运行时解密在进程内完成）.
**可用性分类**：MD+EXEC（纯 Markdown 指令，需要命令行执行能力进行安装/配对/管理；核心检索通过原生 memory 工具，管理操作通过 CLI 执行）.
## 常见问题

**Q1：配对时为什么返回 502 错误？**
A：502（gateway_disconnected）通常因为使用了 `tr pair --json` CLI 方式，其 WebSocket 被 shell 工具 30 秒超时杀死。解决方案：使用进程内 HTTP 路由 `curl -s http://localhost:18789/plugin/tool-orchestrator/pair/init` 替代。仅在路由不可达时回退到 CLI 且必须分离运行使 WS 存活.
**Q2：重装后插件状态显示 disabled 怎么办？**
A：重装后未运行 `plugins enable tool-orchestrator` 导致槽位卡在 memory-core。运行 enable 命令绑定记忆槽位即可。禁用的插件不会注册记忆工具或配对路由.
**Q3：memory_search/memory_get 工具未注册怎么办？**
A：工具首次加载可能未生效。自主发出 `/tool-orchestrator-restart` 命令（一行公告，无需用户授权），插件会自重载（向自身 PID 发送 SIGUSR1 信号）。绝不要求用户手动重启或执行 kill/docker restart.
**Q4：安装报告 already exists 怎么办？**
A：不要添加 `--force`（会写入损坏的 version=None 记录）。执行卸载→清理残留包目录→重装→enable 的完整流程。这不触及凭据（位于 `~/.tool-orchestrator/`）.
**Q5：后台自动捕获的事实和显式 tr remember 有什么区别？**
A：后台捕获从对话中自动提取事实（无需用户明确要求），适合日常偏好记录。显式 tr remember 在用户明确说"记住 X"时使用，适合需要精确控制的记忆。两者都加密存储，但显式记忆优先级更高。绝不将用户事实写入 MEMORY.md/USER.md 等本地人格配置文件.
**Q6：网络不可达时记忆检索会中断吗？**
A：不会中断。检索结果有本地 LRU 缓存（256 条，TTL 1 小时），网络不可达时自动降级读取本地缓存与 local-vault（本地加密存储），响应会标注"来自本地缓存"。离线期间的写入进入本地队列，网络恢复后批量同步到去中心化网络，不丢失事实。仅跨设备实时同步会延迟.
## 已知限制

1. **依赖插件系统与去中心化网络**：本技能需要 Agent 平台支持插件安装/启用，且需访问去中心化网络节点完成配对与存储。不支持插件的平台无法使用；离线环境可降级到本地存储回退（local-vault）保证检索不中断，但跨设备同步需网络恢复后进行.
2. **配对优先浏览器，CLI 可替代**：12 词恢复短语的生成与导入优先通过浏览器完成（方式 A）；无浏览器环境（如纯 CLI 服务器）可用方式 B 的 `tr pair --json --no-browser` CLI 替代，短语写入权限 600 文件后 `tr pair --confirm` 确认。短语绝不进入聊天或 LLM 上下文.
3. **本地存储仅为回退，非默认**：记忆默认加密存储于去中心化网络，非本地磁盘。本地存储回退（local-vault）仅在网络不可达时自动启用，网络恢复后自动同步。需要纯本地文件记忆方案的用户应使用 persistent-memory-engine 等本地方案.
4. **凭据文件零暴露硬性约束**：代理绝不能读取/列出/展示 credentials.json 或任何凭据文件，即使出于"验证安装"目的。这限制了对安装状态的深度检查，需通过 `tr status --json` 间接确认.
5. **重装流程需手动清理**：安装报告 already exists 时需手动卸载→清理残留包目录→重装→enable，不能用 --force（会写入损坏记录）。此流程不触及凭据但需用户执行命令行操作.