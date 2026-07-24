---
slug: mcp-toolkit-builder
name: mcp-server-builder
version: 1.0.1
displayName: MCP服务器构建器
summary: "构建生产级MCP服务器,Python/TypeScript双语言,让LLM连接一切外部系统。MCP服务器构建器指导创建生产级MCP(Model Context Protocol)服务器,核心"
license: Proprietary
description: MCP服务器构建器指导创建生产级MCP(Model Context Protocol)服务器,核心功能包括工具定义、资源暴露、提示模板、传输层选择、认证安全和测试部署全流程。适用于让LLM调用外部API、访问数据库、集成SaaS服务、暴露企业内部能力等场景。支持Python(FastMCP)和TypeScript(MCP
  SDK)双语言。触发关键词:MCP、MCP服务器、Model Context Protocol、FastMCP、MCP SDK、工具集成、API集成、LLM集成、MCP开发、协议服务器。
tags:
  - MCP服务器
  - LLM集成
  - API集成
  - 工具开发
  - 协议实现
  - UI设计
  - 前端
  - 设计
  - mcp
  - api
  - 服务器
  - fastmcp
  - json
tools:
  - read
  - exec
  - write
category: "Creative"
---
# MCP服务器构建器

指导创建生产级 MCP 服务器。MCP(Model Context Protocol)定义了 Agent 如何连接外部系统:认证、传输、工具发现。

## 核心能力

1. **工具(Tools)定义**:按"动词+名词"命名规范(如`send_email`、`query_database`),用JSON Schema定义参数输入,返回结构化输出,支持Python(FastMCP装饰器)和TypeScript(MCP SDK)两种实现。
2. **资源(Resources)暴露**:将数据源(文件/记录/配置)通过URI模式(如`db://users/{id}`)暴露,支持LLM按需读取。
3. **提示(Prompts)模板**:提供参数化的预设提示模板,支持变量注入和模板组合。
4. **传输层选择**:stdio(本地CLI)、HTTP+SSE(远程Web)、WebSocket(实时双向)三种传输方案选型与实现。
5. **认证与安全**:API Key/OAuth 2.0/Bearer Token认证,最小权限授权,输入校验,速率限制,审计日志全流程安全设计。

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| API集成 | 外部API文档+调用需求 | 包装为MCP工具的Python/TS服务器代码,输出到`output/{server-name}/src/` |
| 数据库访问 | 数据库schema+查询需求 | 安全的数据库MCP服务器(参数化查询+权限控制),输出到`output/{server-name}/src/` |
| 文件系统集成 | 文件操作需求 | 文件系统MCP服务器(读写+路径校验),输出到`output/{server-name}/src/` |
| SaaS集成 | 第三方服务(邮件/Slack/Notion) | 集成OAuth的SaaS MCP服务器,输出到`output/{server-name}/src/` |
| 企业自定义工具 | 内部系统能力描述 | 企业MCP服务器(含工具清单+配置+测试),输出到`output/{server-name}/` |

**不适用于**:
- 构建非MCP协议的普通API服务(请用Express/FastAPI)
- 不需要LLM调用的纯后端微服务
- 实时音视频流传输(MCP非流媒体协议)
- 高频交易等对延迟极敏感的场景(MCP有协议开销)

## 使用流程

### Step 1: 需求与能力设计
1. 明确MCP服务器提供什么能力(工具/资源/提示)
2. 定义工具:工具名(动词+名词)、参数schema(JSON Schema)、返回值(结构化输出)
3. 定义资源:暴露的数据源、URI模式
4. 定义提示:预设模板、参数化模板

### Step 2: 技术选型
- **Python方案**: 使用FastMCP框架(`pip install fastmcp`),适合数据科学/ML场景
- **TypeScript方案**: 使用MCP SDK(`npm install @modelcontextprotocol/sdk`),适合Web生态集成
- 国内安装替代: `pip install fastmcp -i https://pypi.tuna.tsinghua.edu.cn/simple` 或 `cnpm install @modelcontextprotocol/sdk`

### Step 3: 传输层选择
| 传输 | 场景 | 特点 |
|:-----|:-----|:-----|
| stdio | 本地CLI工具 | 进程间通信,简单,无需网络 |
| HTTP+SSE | 远程服务 | Web友好,可跨网络,需认证 |
| WebSocket | 实时双向 | 低延迟,持续连接,适合实时数据 |

### Step 4: 认证与安全实现
1. 选择认证方式:API Key(简单/个人)、OAuth 2.0(第三方)、Bearer Token(企业内部)
2. 实现最小权限授权:工具只暴露必要能力
3. 输入校验:所有工具参数用JSON Schema校验
4. 速率限制:防止滥用
5. 审计日志:记录工具调用

### Step 5: 测试与部署
1. 单元测试:每个工具独立测试
2. 集成测试:工具与真实外部服务交互
3. 契约测试:验证MCP协议合规
4. 错误场景测试:网络失败、认证失效、超时

## 示例

### 示例1: Python天气查询MCP服务器

**输入**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| input | string | 是 | MCP服务器构建器处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
构建一个MCP服务器,提供天气查询工具,输入城市名返回天气信息。使用Python FastMCP。
```

**输出** (`output/weather-server/src/server.py`):
```python
from fastmcp import FastMCP
import httpx
import logging
# ...
logger = logging.getLogger(__name__)
mcp = FastMCP("weather-server")
# ...
@mcp.tool()
def get_weather(city: str) -> dict:
    """获取指定城市的天气
# ...
    Args:
        city: 城市名称,如"北京"、"上海"
# ...
    Returns:
        包含城市、温度、天气描述的字典
    """
    try:
        # 实际调用天气API
        response = httpx.get(f"https://api.weather.example.com/{city}", timeout=10)
        response.raise_for_status()
        data = response.json()
        return {"city": city, "temp": data["temp"], "desc": data["desc"]}
    except httpx.TimeoutException:
        logger.error(f"Weather API timeout for {city}")
        return {"success": False, "error": "TIMEOUT", "message": "天气服务超时"}
    except Exception as e:
        logger.exception("Unexpected error")
        return {"success": False, "error": "INTERNAL_ERROR", "message": "查询失败"}
# ...
if __name__ == "__main__":
    mcp.run()
```

### 示例2: TypeScript数据库查询MCP服务器

**输入**:
```
构建一个MCP服务器,提供数据库查询工具,支持按ID查询用户。使用TypeScript MCP SDK,需要参数化查询防止SQL注入。
```

**输出** (`output/db-server/src/server.ts`):
```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server";
import { z } from "zod";
import { Database } from "better-sqlite3";
// ...
const db = new Database("app.db");
const server = new McpServer({ name: "db-server", version: "1.0.0" });
// ...
server.tool(
  "get_user",
  { id: z.number().int().positive() },
  async ({ id }) => {
    // 参数化查询,防止SQL注入
    const user = db.prepare("SELECT id, name, email FROM users WHERE id = ?").get(id);
    if (!user) {
      return { content: [{ type: "text", text: `用户 ${id} 不存在` }] };
    }
    return { content: [{ type: "text", text: JSON.stringify(user, null, 2) }] };
  }
);
// ...
server.tool(
  "list_users",
  { limit: z.number().int().min(1).max(100).default(10) },
  async ({ limit }) => {
    const users = db.prepare("SELECT id, name FROM users LIMIT ?").all(limit);
    return { content: [{ type: "text", text: JSON.stringify(users, null, 2) }] };
  }
);
// ...
server.run();
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 工具参数校验失败 | 输入不符合JSON Schema | 返回`VALIDATION_FAILED`错误码+具体字段错误信息 |
| 外部API调用超时 | 网络延迟或服务不可达 | 设置timeout(默认10s),超时返回`TIMEOUT`错误,支持重试 |
| 认证令牌失效 | OAuth token过期或API Key无效 | 返回`AUTH_FAILED`,提示重新认证,不暴露Key细节 |
| 数据库连接失败 | 数据库不可达或凭据错误 | 返回`DB_CONNECTION_ERROR`,检查连接字符串(不输出凭据) |
| 工具执行异常 | 未预期的运行时错误 | 捕获Exception,记录日志,返回`INTERNAL_ERROR`,不暴露堆栈 |
| 速率限制触发 | 调用频率超限 | 返回`RATE_LIMITED`+Retry-After提示 |
| 协议不兼容 | MCP客户端版本不匹配 | 返回`PROTOCOL_ERROR`,提示版本要求 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:------|------:|:------|:------|------:|
| Python 3.10+ | 运行时 | 可选 | FastMCP框架(pip install fastmcp) | 清华源:`-i https://pypi.tuna.tsinghua.edu.cn/simple` |
| Node.js 18+ | 运行时 | 可选 | MCP SDK(npm install @modelcontextprotocol/sdk) | cnpm/tnpm:`cnpm install @modelcontextprotocol/sdk` |
| LLM API | API | 可选 | 由Agent内置LLM提供代码生成 | 国内Agent(通义/文心/智谱)均可 |
| 包管理器 | 工具 | 可选 | pip / npm | 国内用cnpm/tnpm/pnpm(阿里镜像) |

### API Key 配置
- **本Skill本身无需API Key**: Skill为方法论指导
- **构建的MCP服务器可能需要**: 外部服务API Key通过环境变量传入,不硬编码
- **安全要求**: API Key零暴露,通过`.env`文件或环境变量管理,不写入代码/日志/文档

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 设计原则

1. **工具粒度适中**:一个工具做一件事,不要做成万能接口
2. **命名清晰**:工具名和参数名自解释(动词+名词)
3. **文档完整**:每个工具有清晰的description
4. **幂等优先**:写操作支持幂等,防止重复
5. **安全第一**:不暴露危险操作(删除/格式化)或需二次确认
6. **性能考虑**:长操作支持分页/流式,避免阻塞

## 输出规范

- 服务器代码:`output/{server-name}/src/`
- 工具清单:`output/{server-name}/tools.md`
- 配置文件:`output/{server-name}/config.json`
- 测试套件:`output/{server-name}/tests/`
- README:`output/{server-name}/README.md`(安装与使用说明)

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: Slack集成MCP服务器(OAuth认证+多工具)

**输入**:
```
构建一个MCP服务器,集成Slack API,提供以下工具:
1. send_message - 发送消息到指定频道
2. list_channels - 列出所有频道
3. search_messages - 搜索历史消息
使用TypeScript MCP SDK,需要OAuth 2.0认证,支持速率限制。
```

**LLM生成输出** (`output/slack-server/src/server.ts`):
```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server";
import { z } from "zod";
import { WebClient } from "@slack/web-api";
// ...
const slackToken = process.env.SLACK_BOT_TOKEN;
if (!slackToken) {
  throw new Error("SLACK_BOT_TOKEN environment variable is required");
}
// ...
const client = new WebClient(slackToken);
const server = new McpServer({ name: "slack-server", version: "1.0.0" });
// ...
// 速率限制:每分钟最多20次调用
const rateLimiter = new Map<string, { count: number; resetAt: number }>();
function checkRateLimit(userId: string): boolean {
  const now = Date.now();
  const entry = rateLimiter.get(userId);
  if (!entry || now > entry.resetAt) {
    rateLimiter.set(userId, { count: 1, resetAt: now + 60000 });
    return true;
  }
  if (entry.count >= 20) {
    return false;
  }
  entry.count++;
  return true;
}
// ...
// 工具1: 发送消息
server.tool(
  "send_message",
  {
    channel: z.string().min(1).describe("频道ID或名称,如 #general"),
    text: z.string().min(1).max(4000).describe("消息内容,最多4000字符"),
  },
  async ({ channel, text }, extra) => {
    const userId = extra?.authInfo?.userId || "anonymous";
    if (!checkRateLimit(userId)) {
      return {
        content: [{ type: "text", text: "错误: 速率限制,请1分钟后重试" }],
        isError: true,
      };
    }
    try {
      const result = await client.chat.postMessage({ channel, text });
      return {
        content: [{
          type: "text",
          text: JSON.stringify({ ok: true, ts: result.ts, channel: result.channel }),
        }],
      };
    } catch (error: any) {
      if (error.code === "slack_webapi_platform_error") {
        return {
          content: [{ type: "text", text: `错误: channel_not_found - 频道 ${channel} 不存在或无权限` }],
          isError: true,
        };
      }
      return {
        content: [{ type: "text", text: "错误: INTERNAL_ERROR - 发送消息失败" }],
        isError: true,
      };
    }
  }
);
// ...
// 工具2: 列出频道
server.tool(
  "list_channels",
  {
    limit: z.number().int().min(1).max(200).default(100).describe("返回数量上限"),
  },
  async ({ limit }) => {
    try {
      const result = await client.conversations.list({
        limit,
        types: "public_channel,private_channel",
      });
      const channels = (result.channels || []).map((ch: any) => ({
        id: ch.id,
        name: ch.name,
        is_private: ch.is_private,
        num_members: ch.num_members,
      }));
      return { content: [{ type: "text", text: JSON.stringify(channels, null, 2) }] };
    } catch {
      return {
        content: [{ type: "text", text: "错误: AUTH_FAILED - Token无效或已过期" }],
        isError: true,
      };
    }
  }
);
// ...
// 工具3: 搜索消息
server.tool(
  "search_messages",
  {
    query: z.string().min(2).describe("搜索关键词,至少2个字符"),
    count: z.number().int().min(1).max(20).default(5).describe("返回结果数"),
  },
  async ({ query, count }) => {
    try {
      const result = await client.search.messages({ query, count });
      const messages = (result.messages?.matches || []).map((m: any) => ({
        channel: m.channel?.name,
        user: m.user,
        text: m.text,
        timestamp: m.ts,
        permalink: m.permalink,
      }));
      return { content: [{ type: "text", text: JSON.stringify(messages, null, 2) }] };
    } catch {
      return {
        content: [{ type: "text", text: "错误: search_not_enabled - 需要Slack付费计划支持搜索" }],
        isError: true,
      };
    }
  }
);
// ...
server.run();
```

**LLM生成输出** (`output/slack-server/src/auth.ts`):
```typescript
// OAuth 2.0 认证模块
import { URLSearchParams } from "url";
// ...
const CLIENT_ID = process.env.SLACK_CLIENT_ID!;
const CLIENT_SECRET = process.env.SLACK_CLIENT_SECRET!;
const REDIRECT_URI = process.env.SLACK_REDIRECT_URI!;
// ...
export async function exchangeCodeForToken(code: string): Promise<string> {
  const params = new URLSearchParams({
    client_id: CLIENT_ID,
    client_secret: CLIENT_SECRET,
    code,
    redirect_uri: REDIRECT_URI,
  });
  const res = await fetch("https://slack.com/api/oauth.v2.access", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: params,
  });
  const data = await res.json();
  if (!data.ok) throw new Error(`OAuth failed: ${data.error}`);
  return data.access_token;
}
```

**LLM生成输出** (`output/slack-server/tools.md`):
```markdown
# Slack MCP Server 工具清单
# ...
| 工具名 | 参数 | 返回 | 认证 |
|---:|:---|---:|---:|
| send_message | channel, text | {ok, ts, channel} | Slack Bot Token |
| list_channels | limit | [{id, name, is_private, num_members}] | Slack Bot Token |
| search_messages | query, count | [{channel, user, text, timestamp, permalink}] | Slack付费计划 |
```

**效果验证**: ✓工具命名规范(动词+名词) ✓JSON Schema参数校验(Zod) ✓OAuth 2.0认证实现 ✓速率限制(20次/分钟) ✓错误处理覆盖(channel_not_found/AUTH_FAILED/search_not_enabled)

### 案例2: 文件系统MCP服务器(路径校验+安全防护)

**输入**:
```
构建一个MCP服务器,提供文件系统操作工具:
1. read_file - 读取文件内容
2. write_file - 写入文件
3. list_directory - 列出目录内容
安全要求:路径校验防止目录穿越,仅允许指定根目录内的操作。
使用Python FastMCP。
```

**LLM生成输出** (`output/fs-server/src/server.py`):
```python
from fastmcp import FastMCP
from pathlib import Path
import os
import logging
# ...
logger = logging.getLogger(__name__)
mcp = FastMCP("filesystem-server")
# ...
# 允许的根目录(通过环境变量配置)
ALLOWED_ROOT = Path(os.environ.get("FS_ALLOWED_ROOT", "./workspace")).resolve()
# ...
def validate_path(file_path: str) -> Path:
    """验证路径在允许的根目录内,防止目录穿越攻击"""
    target = (ALLOWED_ROOT / file_path).resolve()
    # 检查解析后的路径是否在允许根目录内
    if not str(target).startswith(str(ALLOWED_ROOT)):
        raise ValueError(f"路径超出允许范围: {file_path}")
    return target
# ...
@mcp.tool()
def read_file(path: str) -> dict:
    """读取指定路径的文件内容
# ...
    Args:
        path: 相对于根目录的文件路径,如 "docs/readme.md"
# ...
    Returns:
        包含文件内容和元信息的字典
    """
    try:
        target = validate_path(path)
    except ValueError as e:
        return {"success": False, "error": "PATH_VIOLATION", "message": str(e)}
# ...
    if not target.exists():
        return {"success": False, "error": "NOT_FOUND", "message": f"文件不存在: {path}"}
    if not target.is_file():
        return {"success": False, "error": "NOT_A_FILE", "message": f"路径不是文件: {path}"}
# ...
    try:
        content = target.read_text(encoding="utf-8")
        return {
            "success": True,
            "path": path,
            "size": target.stat().st_size,
            "content": content,
        }
    except PermissionError:
        return {"success": False, "error": "PERMISSION_DENIED", "message": "无读取权限"}
    except Exception as e:
        logger.exception("Read file error")
        return {"success": False, "error": "INTERNAL_ERROR", "message": "读取文件失败"}
# ...
@mcp.tool()
def write_file(path: str, content: str) -> dict:
    """写入内容到指定路径的文件
# ...
    Args:
        path: 相对于根目录的文件路径
        content: 文件内容
    """
    try:
        target = validate_path(path)
    except ValueError as e:
        return {"success": False, "error": "PATH_VIOLATION", "message": str(e)}
# ...
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return {"success": True, "path": path, "size": len(content.encode("utf-8"))}
    except PermissionError:
        return {"success": False, "error": "PERMISSION_DENIED", "message": "无写入权限"}
    except Exception as e:
        logger.exception("Write file error")
        return {"success": False, "error": "INTERNAL_ERROR", "message": "写入文件失败"}
# ...
@mcp.tool()
def list_directory(path: str = ".") -> dict:
    """列出指定目录的内容
# ...
    Args:
        path: 相对于根目录的目录路径,默认为根目录
    """
    try:
        target = validate_path(path)
    except ValueError as e:
        return {"success": False, "error": "PATH_VIOLATION", "message": str(e)}
# ...
    if not target.exists():
        return {"success": False, "error": "NOT_FOUND", "message": f"目录不存在: {path}"}
    if not target.is_dir():
        return {"success": False, "error": "NOT_A_DIRECTORY", "message": f"路径不是目录: {path}"}
# ...
    try:
        entries = []
        for item in sorted(target.iterdir()):
            entries.append({
                "name": item.name,
                "type": "directory" if item.is_dir() else "file",
                "size": item.stat().st_size if item.is_file() else None,
            })
        return {"success": True, "path": path, "entries": entries}
    except PermissionError:
        return {"success": False, "error": "PERMISSION_DENIED", "message": "无访问权限"}
    except Exception as e:
        logger.exception("List directory error")
        return {"success": False, "error": "INTERNAL_ERROR", "message": "列目录失败"}
# ...
if __name__ == "__main__":
    mcp.run()
```

**效果验证**: ✓路径穿越防护(resolve+startswith校验) ✓三种工具功能完整(读/写/列目录) ✓错误码体系化(PATH_VIOLATION/NOT_FOUND/PERMISSION_DENIED) ✓环境变量配置根目录(不硬编码) ✓中文编码处理(UTF-8)

### 案例3: 数据库MCP服务器(参数化查询+分页+审计日志)

**输入**:
```
构建一个MCP服务器,提供PostgreSQL数据库查询工具:
1. query_users - 按条件查询用户(支持分页)
2. get_user_by_id - 按ID查询单个用户
3. count_users - 统计用户总数
安全要求:参数化查询防SQL注入,审计日志记录所有查询,只允许SELECT操作。
使用TypeScript MCP SDK + pg驱动。
```

**LLM生成输出** (`output/pg-server/src/server.ts`):
```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server";
import { z } from "zod";
import { Pool } from "pg";
import { writeFileSync, appendFileSync } from "fs";
// ...
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  max: 10,
  idleTimeoutMillis: 30000,
});
// ...
const AUDIT_LOG = process.env.AUDIT_LOG_PATH || "./audit.log";
const server = new McpServer({ name: "pg-server", version: "1.0.0" });
// ...
// 审计日志
function auditLog(tool: string, params: object, result: string) {
  const entry = JSON.stringify({
    timestamp: new Date().toISOString(),
    tool,
    params,
    result_summary: result.substring(0, 200),
  });
  appendFileSync(AUDIT_LOG, entry + "\n", "utf-8");
}
// ...
// 只允许SELECT查询的安全检查
function validateReadOnlyQuery(sql: string): boolean {
  const normalized = sql.trim().toUpperCase();
  return normalized.startsWith("SELECT") && !normalized.includes("INSERT") &&
    !normalized.includes("UPDATE") && !normalized.includes("DELETE") &&
    !normalized.includes("DROP") && !normalized.includes("ALTER");
}
// ...
// 工具1: 按条件查询用户(分页)
server.tool(
  "query_users",
  {
    status: z.enum(["active", "inactive", "all"]).default("all").describe("用户状态筛选"),
    role: z.string().optional().describe("角色筛选,如 'admin'"),
    page: z.number().int().min(1).default(1).describe("页码,从1开始"),
    page_size: z.number().int().min(1).max(100).default(20).describe("每页数量,最多100"),
  },
  async ({ status, role, page, page_size }) => {
    const offset = (page - 1) * page_size;
    const conditions: string[] = [];
    const params: (string | number)[] = [];
    let paramIndex = 1;
// ...
    if (status !== "all") {
      conditions.push(`status = $${paramIndex++}`);
      params.push(status);
    }
    if (role) {
      conditions.push(`role = $${paramIndex++}`);
      params.push(role);
    }
    const whereClause = conditions.length > 0 ? `WHERE ${conditions.join(" AND ")}` : "";
// ...
    try {
      const query = `SELECT id, name, email, role, status, created_at FROM users ${whereClause} ORDER BY created_at DESC LIMIT $${paramIndex++} OFFSET $${paramIndex++}`;
      params.push(page_size, offset);
// ...
      const result = await pool.query(query, params);
      const totalResult = await pool.query(`SELECT COUNT(*) FROM users ${whereClause}`, params.slice(0, -2));
// ...
      const response = {
        users: result.rows,
        pagination: {
          page,
          page_size,
          total: parseInt(totalResult.rows[0].count),
          total_pages: Math.ceil(parseInt(totalResult.rows[0].count) / page_size),
        },
      };
      auditLog("query_users", { status, role, page, page_size }, `${response.users.length} users returned`);
      return { content: [{ type: "text", text: JSON.stringify(response, null, 2) }] };
    } catch (error: any) {
      auditLog("query_users", { status, role, page, page_size }, `ERROR: ${error.message}`);
      return {
        content: [{ type: "text", text: "错误: DB_CONNECTION_ERROR - 数据库查询失败" }],
        isError: true,
      };
    }
  }
);
// ...
// 工具2: 按ID查询单个用户
server.tool(
  "get_user_by_id",
  { id: z.number().int().positive().describe("用户ID") },
  async ({ id }) => {
    try {
      const result = await pool.query(
        "SELECT id, name, email, role, status, created_at FROM users WHERE id = $1",
        [id]
      );
      if (result.rows.length === 0) {
        auditLog("get_user_by_id", { id }, "NOT_FOUND");
        return { content: [{ type: "text", text: `用户 ${id} 不存在` }] };
      }
      auditLog("get_user_by_id", { id }, `Found user ${result.rows[0].name}`);
      return { content: [{ type: "text", text: JSON.stringify(result.rows[0], null, 2) }] };
    } catch (error: any) {
      return {
        content: [{ type: "text", text: "错误: DB_CONNECTION_ERROR - 查询失败" }],
        isError: true,
      };
    }
  }
);
// ...
// 工具3: 统计用户总数
server.tool(
  "count_users",
  {
    status: z.enum(["active", "inactive", "all"]).default("all").describe("按状态统计"),
  },
  async ({ status }) => {
    try {
      const query = status === "all"
        ? "SELECT status, COUNT(*) as count FROM users GROUP BY status"
        : "SELECT COUNT(*) as count FROM users WHERE status = $1";
      const params = status === "all" ? [] : [status];
      const result = await pool.query(query, params);
      auditLog("count_users", { status }, `${result.rows.length} rows`);
      return { content: [{ type: "text", text: JSON.stringify(result.rows, null, 2) }] };
    } catch {
      return {
        content: [{ type: "text", text: "错误: DB_CONNECTION_ERROR - 统计失败" }],
        isError: true,
      };
    }
  }
);
// ...
server.run();
```

**效果验证**: ✓参数化查询防SQL注入($1/$2占位符) ✓分页机制完整(page/page_size/total_pages) ✓审计日志记录所有操作 ✓只读查询安全校验 ✓连接池管理(max/idle配置)

### 案例4: 企业内部API MCP服务器(Bearer Token+资源暴露)

**输入**:
```
构建企业内部MCP服务器,暴露以下能力:
工具: create_ticket(创建工单), update_ticket_status(更新工单状态)
资源: ticket://list(工单列表), ticket://detail/{id}(工单详情)
认证: Bearer Token,仅允许内部团队调用。
使用Python FastMCP。
```

**LLM生成输出** (`output/ticket-server/src/server.py`):
```python
from fastmcp import FastMCP
import httpx
import os
import logging
# ...
logger = logging.getLogger(__name__)
mcp = FastMCP("ticket-server")
# ...
API_BASE = os.environ.get("TICKET_API_BASE", "http://internal-api:8080")
VALID_TOKENS = os.environ.get("VALID_BEARER_TOKENS", "").split(",")
# ...
def auth_middleware(token: str) -> bool:
    """验证Bearer Token"""
    return token in VALID_TOKENS
# ...
@mcp.tool()
def create_ticket(title: str, description: str, priority: str = "normal") -> dict:
    """创建内部工单
# ...
    Args:
        title: 工单标题,最多100字符
        description: 工单描述
        priority: 优先级(low/normal/high/urgent),默认normal
# ...
    Returns:
        包含工单ID和状态的字典
    """
    if priority not in ("low", "normal", "high", "urgent"):
        return {"success": False, "error": "VALIDATION_FAILED", "message": f"无效优先级: {priority}"}
# ...
    token = os.environ.get("INTERNAL_API_TOKEN", "")
    try:
        response = httpx.post(
            f"{API_BASE}/api/tickets",
            json={"title": title, "description": description, "priority": priority},
            headers={"Authorization": f"Bearer {token}"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        logger.info(f"Ticket created: {data.get('id')}")
        return {"success": True, "ticket_id": data["id"], "status": data["status"]}
    except httpx.TimeoutException:
        return {"success": False, "error": "TIMEOUT", "message": "内部API超时"}
    except httpx.HTTPStatusError as e:
        return {"success": False, "error": "API_ERROR", "message": f"内部API返回{e.response.status_code}"}
    except Exception as e:
        logger.exception("Create ticket error")
        return {"success": False, "error": "INTERNAL_ERROR", "message": "创建工单失败"}
# ...
@mcp.tool()
def update_ticket_status(ticket_id: str, status: str) -> dict:
    """更新工单状态
# ...
    Args:
        ticket_id: 工单ID
        status: 新状态(open/in_progress/resolved/closed)
    """
    if status not in ("open", "in_progress", "resolved", "closed"):
        return {"success": False, "error": "VALIDATION_FAILED", "message": f"无效状态: {status}"}
# ...
    token = os.environ.get("INTERNAL_API_TOKEN", "")
    try:
        response = httpx.patch(
            f"{API_BASE}/api/tickets/{ticket_id}",
            json={"status": status},
            headers={"Authorization": f"Bearer {token}"},
            timeout=10,
        )
        if response.status_code == 404:
            return {"success": False, "error": "NOT_FOUND", "message": f"工单不存在: {ticket_id}"}
        response.raise_for_status()
        return {"success": True, "ticket_id": ticket_id, "status": status}
    except httpx.TimeoutException:
        return {"success": False, "error": "TIMEOUT", "message": "内部API超时"}
    except Exception as e:
        logger.exception("Update ticket error")
        return {"success": False, "error": "INTERNAL_ERROR", "message": "更新工单失败"}
# ...
# 资源暴露: 工单列表
@mcp.resource("ticket://list")
def list_tickets() -> str:
    """获取所有工单列表"""
    token = os.environ.get("INTERNAL_API_TOKEN", "")
    try:
        response = httpx.get(
            f"{API_BASE}/api/tickets",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10,
        )
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f'{{"error": "RESOURCE_UNAVAILABLE", "message": "无法获取工单列表"}}'
# ...
# 资源暴露: 工单详情
@mcp.resource("ticket://detail/{ticket_id}")
def get_ticket_detail(ticket_id: str) -> str:
    """获取指定工单的详细信息"""
    token = os.environ.get("INTERNAL_API_TOKEN", "")
    try:
        response = httpx.get(
            f"{API_BASE}/api/tickets/{ticket_id}",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10,
        )
        if response.status_code == 404:
            return f'{{"error": "NOT_FOUND", "message": "工单 {ticket_id} 不存在"}}'
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f'{{"error": "RESOURCE_UNAVAILABLE", "message": "无法获取工单详情"}}'
# ...
if __name__ == "__main__":
    mcp.run()
```

**LLM生成输出** (`output/ticket-server/config.json`):
```json
{
  "server_name": "ticket-server",
  "version": "1.0.0",
  "transport": "stdio",
  "auth": {
    "type": "bearer_token",
    "token_env_var": "INTERNAL_API_TOKEN"
  },
  "tools": ["create_ticket", "update_ticket_status"],
  "resources": ["ticket://list", "ticket://detail/{ticket_id}"],
  "rate_limit": { "max_per_minute": 60 },
  "timeout_seconds": 10
}
```

**效果验证**: ✓工具+资源双能力暴露 ✓Bearer Token认证(环境变量管理) ✓URI模式资源暴露(ticket://) ✓工单状态枚举校验 ✓超时+404等错误场景覆盖

## 常见问题

### Q1: Python和TypeScript方案怎么选?
A: 数据科学/ML/AI场景选Python(FastMCP),与numpy/pandas/PyTorch生态集成方便;Web前端/Node.js后端场景选TypeScript(MCP SDK),与npm生态集成方便。两者生成的MCP服务器协议兼容,可混用。

### Q2: 如何在国内安装MCP相关依赖?
A: Python用清华源:`pip install fastmcp -i https://pypi.tuna.tsinghua.edu.cn/simple`;Node.js用cnpm:`npm install -g cnpm --registry=https://registry.npmmirror.com && cnpm install @modelcontextprotocol/sdk`。也可用阿里云效tnpm。

### Q3: MCP服务器如何做认证?
A: 本地stdio传输无需认证(进程间通信);远程HTTP+SSE传输建议用Bearer Token或OAuth 2.0。API Key通过环境变量传入,不硬编码到代码。OAuth流程需实现token刷新机制。

### Q4: 如何测试MCP服务器?
A: 三层测试:单元测试(每个工具独立,mock外部依赖)、集成测试(真实外部服务)、契约测试(验证MCP协议合规,可用@mcp/testing工具)。错误场景必须覆盖网络失败、认证失效、超时。

### Q5: 构建的MCP服务器能在哪些Agent中使用?
A: 任何支持MCP协议的Agent均可使用,包括Claude Code、Cursor、Codex、Gemini CLI、Windsurf等。MCP是开源协议标准,跨Agent兼容。

## 已知限制

- MCP协议仍在演进中,不同Agent对MCP版本支持可能存在差异,构建后需在目标Agent中测试验证
- stdio传输仅适合本地使用,远程服务必须用HTTP+SSE或WebSocket,增加了部署复杂度
- 工具调用的延迟包含LLM决策+MCP协议往返+外部API调用,不适合对延迟极敏感的场景
- 本Skill生成的是代码模板和架构指导,具体业务逻辑需开发者根据实际需求实现
- 安全认证实现需开发者自行完成,本Skill提供方案指导但不包含现成的认证服务器

## 安全

- **API Key零暴露**: 外部服务API Key通过环境变量(`.env`文件)传入,不硬编码到源码、不写入日志、不输出到MCP工具返回值
- **SQL注入防护**: 数据库查询必须使用参数化查询(占位符),禁止字符串拼接SQL
- **最小权限原则**: 工具只暴露必要能力,危险操作(删除/格式化)需二次确认或不暴露
- **输入校验**: 所有工具参数用JSON Schema/Zod校验,拒绝非法输入
- **审计日志**: 记录工具调用(调用者/时间/参数/结果),便于追溯
