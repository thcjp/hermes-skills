---
slug: lite-sqlite
name: lite-sqlite
version: "1.0.0"
displayName: Lite Sqlite
summary: Fast lightweight local SQLite database for SkillHub agents with minimal RAM
  and storage usage. Us...
license: MIT
description: |-
  Fast lightweight local SQLite database for SkillHub agents with minimal
  RAM and storage usage。Us。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
---
# Lite Sqlite

## 核心能力

* In-memory mode for temporary data (even faster!)
* WAL mode for concurrent access
* Connection pooling
* Automatic schema migration
* Built-in backup/restore
* Query optimization hints
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。


## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Basic Database Operations
```python
from sqlite_connector import SQLiteDB

db = SQLiteDB("agent_data.db")

db.create_table("memos", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "title": "TEXT NOT NULL",
    "content": "TEXT",
    "created_at": "TEXT DEFAULT CURRENT_TIMESTAMP",
    "tags": "TEXT"
})

db.insert("memos", [title="First memo", content="Hello world", tags="test"])

results = db.query("SELECT * FROM memos WHERE tags = ?", ("test",))

db.update("memos", "id = ?", [content="Updated content"], (1,))

db.delete("memos", "id = ?", (1,))

db.close()
```

### In-Memory Database (Fastest)
```python
db = SQLiteDB(":memory:")

db.create_table("temp", {...})

```

---

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

```python
try:
    db.insert("metrics", {...})
except sqlite3.IntegrityError:
    # Duplicate key violation
    pass
except sqlite3.OperationalError:
    # Table doesn't exist or database locked
    pass
```

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 示例1：基础用法
```
### Basic Database Operations
```python
from sqlite_connector import SQLiteDB

db = SQLiteDB("agent_data.db")

db.create_table("memos", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "title": "TEXT NOT NULL",
    "content": "TEXT",
    "created_at": "TEXT DEFAULT CURRENT_TIMESTAMP",
    "tags": "TEXT"
})

db.insert("memos", [title="First memo", content="Hello world", tags="test"])

results = db.query("SELECT * FROM memos WHERE tags = ?", ("test",))

db.update("memos", "id = ?", [content="
```

## 常见问题

### Q1: 如何开始使用Lite Sqlite？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Lite Sqlite有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步
