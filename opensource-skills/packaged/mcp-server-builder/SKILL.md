---
slug: mcp-toolkit-builder
name: mcp-toolkit-builder
version: "1.0.0"
displayName: "MCP服务器构建器"
summary: "构建生产级MCP服务器,Python/TypeScript双语言,让LLM连接一切外部系统"
license: Apache-2.0
description: |-
  MCP服务器构建器——指导创建生产级MCP(Model Context Protocol)服务器,让LLM安全连接外部API、数据库与服务。Python/TypeScript双语言支持,从工具定义到认证部署全流程覆盖。

  核心能力:
  - 双语言支持:Python(FastMCP)/TypeScript(MCP SDK)
  - 工具定义:类型安全的工具接口设计
  - 资源暴露:文件/数据/API资源结构化暴露
  - 传输层:stdio/SSE/HTTP多种传输协议
  - 认证授权:OAuth/API Key/令牌安全集成
  - 错误处理:标准化错误码与重试策略
  - 测试部署:单元测试+集成测试+容器化部署

  适用场景:
  - 独立开发者API集成:将外部API包装为MCP工具供LLM调用
  - SaaS创业者产品能力暴露:企业MCP服务器连接客户系统
  - 一人公司数据访问:LLM安全查询数据库与文件系统
  - 副业达人SaaS连接:Gmail/Slack/Notion第三方服务集成

  差异化:不是简单的API封装教程,而是生产级MCP服务器构建指南,覆盖工具定义到认证部署的全链路,让个人开发者也能构建企业级LLM集成方案。

  触发关键词:MCP、MCP服务器、Model Context Protocol、FastMCP、MCP SDK、工具集成、API集成、LLM集成、MCP开发、协议服务器
tags: [MCP服务器, LLM集成, API集成, 工具开发, 协议实现]
tools: [read, exec]
---

# MCP服务器构建器

指导创建生产级 MCP 服务器。MCP(Model Context Protocol)定义了 Agent 如何连接外部系统:认证、传输、工具发现。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| API 集成 | 让 LLM 调用外部 API | 包装为 MCP 工具 |
| 数据库访问 | LLM 查询数据库 | 安全的数据库 MCP |
| 文件系统 | LLM 读写文件 | 文件系统 MCP |
| SaaS 集成 | 连接 Gmail/Slack/Notion | 第三方服务 MCP |
| 自定义工具 | 内部系统能力暴露 | 企业 MCP 服务器 |

## 工作流

### 1. 需求与能力设计

1. **明确目标**:MCP 服务器提供什么能力?
2. **定义工具(Tools)**:
   - 工具名:动词+名词(`send_email`、`query_database`)
   - 参数 schema:JSON Schema 定义输入
   - 返回值:结构化输出
3. **定义资源(Resources)**:
   - 暴露的数据源(文件/记录/配置)
   - URI 模式(`db://users/{id}`)
4. **定义提示(Prompts)**:
   - 预设的提示模板
   - 参数化模板

### 2. 技术选型

#### Python(FastMCP)
```python
from fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def get_weather(city: str) -> dict:
    """获取指定城市的天气"""
    # 实现逻辑
    return {"city": city, "temp": 25}

if __name__ == "__main__":
    mcp.run()
```

#### TypeScript(MCP SDK)
```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server";

const server = new McpServer({ name: "my-server", version: "1.0.0" });

server.tool("get_weather", { city: z.string() }, async ({ city }) => {
  return { content: [{ type: "text", text: `${city}: 25°C` }] };
});
```

### 3. 传输层选择

| 传输 | 场景 | 特点 |
|:-----|:-----|:-----|
| stdio | 本地 CLI 工具 | 进程间通信,简单 |
| HTTP+SSE | 远程服务 | Web 友好,可跨网络 |
| WebSocket | 实时双向 | 低延迟,持续连接 |

### 4. 认证与安全

1. **认证方式**:
   - API Key:简单,适合个人工具
   - OAuth 2.0:第三方服务集成
   - Bearer Token:企业内部
2. **授权范围**:最小权限原则,工具只暴露必要能力
3. **输入校验**:所有工具参数必须校验(JSON Schema)
4. **速率限制**:防止滥用
5. **审计日志**:记录工具调用

### 5. 错误处理

```python
@mcp.tool()
def risky_operation(data: str) -> dict:
    try:
        result = process(data)
        return {"success": True, "data": result}
    except ValidationError as e:
        return {"success": False, "error": "VALIDATION_FAILED", "message": str(e)}
    except Exception as e:
        logger.exception("Unexpected error")
        return {"success": False, "error": "INTERNAL_ERROR", "message": "操作失败"}
```

### 6. 测试

1. **单元测试**:每个工具独立测试
2. **集成测试**:工具与真实外部服务交互
3. **契约测试**:验证 MCP 协议合规
4. **错误场景**:网络失败、认证失效、超时

## 设计原则

1. **工具粒度适中**:一个工具做一件事,不要做成万能接口
2. **命名清晰**:工具名和参数名自解释
3. **文档完整**:每个工具有清晰的 description
4. **幂等优先**:写操作支持幂等,防止重复
5. **安全第一**:不暴露危险操作(删除/格式化)或需二次确认
6. **性能考虑**:长操作支持分页/流式,避免阻塞

## 输出规范

- 服务器代码:`output/{server-name}/src/`
- 工具清单:`output/{server-name}/tools.md`
- 配置文件:`output/{server-name}/config.json`
- 测试套件:`output/{server-name}/tests/`
- README:`output/{server-name}/README.md`(安装与使用说明)

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.10+ | 运行时 | 可选 | FastMCP框架(pip install fastmcp) |
| Node.js 18+ | 运行时 | 可选 | MCP SDK(npm install @modelcontextprotocol/sdk) |
| LLM API | API | 可选 | 由Agent内置LLM提供代码生成 |

### API Key 配置
- 本Skill无需额外API Key配置

### 纯Markdown使用说明
本Skill指导构建MCP(Model Context Protocol)服务器。Python方案使用FastMCP,TypeScript方案使用MCP SDK。MCP为开源协议标准。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用
