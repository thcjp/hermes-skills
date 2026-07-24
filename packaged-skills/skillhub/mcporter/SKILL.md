---

slug: "mcporter"
name: "mcporter"
version: 1.0.1
displayName: "Mcporter"
summary: "用mcporter CLI列出/配置/认证/调用MCP服务与工具。Use the mcporter CLI to list, configure, auth, and call 协议 ser"
license: "Proprietary"
description: |-，可处理提升工作效率
  Use the mcporter CLI to list, configure, auth, and call 协议 servers/tools。核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Other
  - 工具
  - 效率
  - 自动化
  - 开发
  - 代码
  - 写作
  - 电商
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"

---

# Mcporter

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

- **MCP服务发现**：通过 `mcporter list` 列出已注册的MCP（Model Context Protocol）服务器及其暴露的工具
- **服务配置管理**：通过 `mcporter config` 添加、修改、删除MCP服务器连接配置（transport类型、URL、认证方式）
- **认证与授权**：通过 `mcporter auth` 管理API Key、OAuth Token、Bearer Token等认证凭据，支持多环境配置
- **工具调用**：通过 `mcporter call` 直接调用MCP服务器暴露的工具，传递参数并接收结构化结果
- **协议兼容**：支持 stdio（本地进程）、SSE（Server-Sent Events）、WebSocket 三种传输协议
- **健康检查**：通过 `mcporter ping` 检测MCP服务器连通性与响应延迟

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 服务注册与发现 | 服务器名称与连接配置 | 已注册服务列表 + 连接状态 |
| 工具调用测试 | 工具名称与参数 | 调用结果 + 执行耗时 + 状态码 |
| 认证凭据管理 | 认证类型与凭据 | 配置生效状态 + 过期时间 |
| 批量服务健康检查 | 多服务器地址列表 | 各服务连通性报告 + 延迟数据 |
| 配置导出与迁移 | 当前环境配置 | 可移植配置文件（JSON/YAML） |

**不适用于**：MCP服务器自身的开发与部署、非MCP协议的API调用、图形化GUI管理（本工具为CLI）

## 使用流程

1. 确认运行环境满足依赖说明中的要求，已安装 `mcporter` CLI 并在PATH中可用
2. 使用 `mcporter config add` 添加MCP服务器连接配置
3. 使用 `mcporter auth set` 配置认证凭据（如需）
4. 使用 `mcporter list` 确认服务已注册且可达
5. 使用 `mcporter call` 调用具体工具，传入参数获取结果
6. 使用 `mcporter ping` 定期检查服务健康状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | mcporter处理的命令或配置内容 |
| command | string | 否 | mcporter子命令，可选值: `list`/`config`/`auth`/`call`/`ping`，默认 `list` |
| server | string | 否 | 目标MCP服务器名称 |
| tool | string | 否 | 调用的工具名称（`call`命令时使用） |
| params | object | 否 | 工具调用参数（JSON对象） |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "servers": [
      {
        "name": "github-mcp",
        "transport": "stdio",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "status": "connected",
        "latency_ms": 45,
        "tools": ["create_issue", "search_repos", "get_file_contents"]
      }
    ],
    "metadata": {
      "template_used": "reviewer",
      "total_servers": 1,
      "connected": 1,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 详细使用示例

### 示例1：添加MCP服务器配置

```bash
# 添加基于 stdio 的本地MCP服务器
mcporter config add \
  --name "filesystem" \
  --transport stdio \
  --command "npx" \
  --args "-y,@modelcontextprotocol/server-filesystem,/path/to/dir"

# 添加基于 SSE 的远程MCP服务器
mcporter config add \
  --name "remote-api" \
  --transport sse \
  --url "https://mcp.example.com/sse"

# 查看所有已配置的服务器
mcporter config list
```

### 示例2：配置认证凭据

```bash
# 设置 API Key 认证
mcporter auth set \
  --server "github-mcp" \
  --type apikey \
  --key "GITHUB_TOKEN" \
  --value "ghp_xxxxxxxxxxxx"

# 设置 Bearer Token 认证
mcporter auth set \
  --server "remote-api" \
  --type bearer \
  --token "eyJhbGciOiJIUzI1NiIs..."

# 查看认证状态
mcporter auth list --server "github-mcp"
```

### 示例3：列出服务与工具

```bash
# 列出所有已注册的MCP服务器
mcporter list

# 输出示例:
# NAME           TRANSPORT  STATUS     TOOLS  LATENCY
# filesystem     stdio      connected  8      12ms
# github-mcp     stdio      connected  12     45ms
# remote-api     sse        connected  5      120ms

# 列出特定服务器的所有工具
mcporter list --server "github-mcp" --tools

# 输出示例:
# TOOL              DESCRIPTION
# create_issue      Create a new GitHub issue
# search_repos      Search GitHub repositories
# get_file_contents Get file contents from a repo
```

### 示例4：调用MCP工具

```bash
# 调用 github-mcp 的 create_issue 工具
mcporter call \
  --server "github-mcp" \
  --tool "create_issue" \
  --params '{
    "owner": "myorg",
    "repo": "myrepo",
    "title": "Bug: login page crash",
    "body": "Steps to reproduce..."
  }'

# 调用 filesystem 的 read_file 工具
mcporter call \
  --server "filesystem" \
  --tool "read_file" \
  --params '{"path": "/path/to/dir/config.json"}'
```

### 示例5：健康检查

```bash
# 检查单个服务器连通性
mcporter ping --server "github-mcp"
# 输出: github-mcp: OK (45ms)

# 检查所有服务器
mcporter ping --all
# 输出:
# filesystem: OK (12ms)
# github-mcp: OK (45ms)
# remote-api: FAIL (timeout after 5000ms)
```

## 传输协议说明

| 协议 | 适用场景 | 配置方式 | 特点 |
|:-----|:---------|:---------|:-----|
| stdio | 本地进程通信 | `--command` + `--args` | 低延迟，无需网络，适合本地工具 |
| SSE | 远程HTTP服务 | `--url` (HTTP/HTTPS) | 单向流，需处理重连，适合只读API |
| WebSocket | 双向实时通信 | `--url` (ws/wss) | 双向流，低延迟，适合交互式工具 |

## 最佳实践

### 配置管理
- 为不同环境（dev/staging/prod）使用独立的配置文件：`mcporter config --env dev`
- 敏感凭据使用环境变量注入，不硬编码在配置文件中
- 定期使用 `mcporter config export` 导出配置备份

### 认证安全
- API Key 和 Token 存储在系统密钥库中（macOS Keychain / Windows Credential Manager）
- 使用 `mcporter auth rotate` 定期轮换Token
- 生产环境使用短期Token（如OAuth的access_token + refresh_token机制）

### 性能优化
- 对频繁调用的工具启用结果缓存：`mcporter config set --cache-ttl 300`
- stdio协议优先于网络协议，减少网络延迟
- 批量调用时使用 `mcporter call --batch` 合并请求

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接与防火墙规则 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| mcporter CLI | CLI | 必需 | `npm install -g mcporter` 或 `pip install mcporter` |
| Node.js | Runtime | 推荐 | v18+，用于stdio协议的MCP服务器 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.

## 常见问题

### Q1: 如何开始使用Mcporter？
A: 首先安装mcporter CLI（`npm install -g mcporter`），然后使用 `mcporter config add` 添加MCP服务器配置。配置时需指定服务器名称、传输协议（stdio/sse/websocket）和连接参数。添加后使用 `mcporter list` 确认服务已注册，使用 `mcporter ping` 验证连通性，最后用 `mcporter call` 调用工具。

### Q2: stdio和SSE传输协议如何选择？
A: stdio适用于本地安装的MCP服务器（如通过npx启动的Node.js服务），延迟最低且无需网络配置。SSE适用于远程托管的MCP服务器，通过HTTP连接。如果工具需要双向实时通信（如流式输出），使用WebSocket协议。优先选择stdio以获得最佳性能。

### Q3: 认证Token过期后如何自动刷新？
A: 对于OAuth类型的认证，mcporter支持自动刷新。配置时同时设置 `--token`（access_token）和 `--refresh-token`，mcporter在access_token过期时自动使用refresh_token获取新token。对于API Key类型，需手动使用 `mcporter auth set` 更新。使用 `mcporter auth list` 查看各凭据的过期时间。

### Q4: 如何在CI/CD环境中使用mcporter？
A: 在CI/CD中使用环境变量注入认证凭据（如 `GITHUB_TOKEN`），配置文件使用 `mcporter config import config.json` 从文件加载。调用工具时使用 `--non-interactive` 标志避免交互式提示。使用 `mcporter call --output json` 获取结构化输出便于脚本解析。建议在CI步骤前添加 `mcporter ping --all` 健康检查。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
| MCP服务器连接拒绝 | 服务器未启动或端口被占用 | 检查MCP服务器进程状态，确认端口可用 |
| 认证失败(401/403) | Token过期或权限不足 | 使用 `mcporter auth set` 更新凭据，确认Token具有所需scope |

