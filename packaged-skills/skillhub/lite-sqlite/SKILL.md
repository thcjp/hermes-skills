---
slug: "lite-sqlite"
name: "lite-sqlite"
version: 1.0.1
displayName: "Lite Sqlite"
summary: "SkillHub Agent用的快速轻量本地SQLite,低RAM低存储"
license: "Proprietary"
description: |-
  Fast lightweight local SQLite database for SkillHub agents with minimal
  RAM and storage usage。Us。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策.
tags:
  - Integrations
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Lite Sqlite

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |
| 数据质量检测与清洗规则 | 不支持 | 支持 |

## 核心能力

* In-memory mode for temporary data (even faster!)
* WAL mode for concurrent access
* Connection pooling
* Automatic schema migration
* Built-in backup/restore
* Query optimization hints
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| SkillHub A | 目标数据与配置参数 | 处理结果与执行状态 |
| 低RAM低存储 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Basic Database Operations
```python
from sqlite_connector import SQLiteDB
# ...
db = SQLiteDB("agent_data.db")
# ...
db.create_table("memos", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "title": "TEXT NOT NULL",
    "content": "TEXT",
    "created_at": "TEXT DEFAULT CURRENT_TIMESTAMP",
    "tags": "TEXT"
})
# ...
db.insert("memos", [title="First memo", content="Hello world", tags="test"])
# ...
results = db.query("SELECT * FROM memos WHERE tags = ?", ("test",))
# ...
db.update("memos", "id = ?", [content="Updated content"], (1,))
# ...
db.delete("memos", "id = ?", (1,))
# ...
db.close()
```

### In-Memory Database (Fastest)
```python
db = SQLiteDB(":memory:")
# ...
db.create_table("temp", {...})
# ...
```

---

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | lite-sqlite处理的内容输入 |,  |
| content | string | 否 | lite-sqlite处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "sqlite 相关配置参数",
    result: "sqlite 相关配置参数",
    result: "sqlite 相关配置参数",
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

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ;确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 对照使用流程章节检查输入格式;参考示例章节修正输入 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述,补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 对照依赖说明章节确认环境配置;检查命令权限设置 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 示例1：基础用法
```
### Basic Database Operations(补充)
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
# ...
## 常见问题
# ...
### Q1: 如何开始使用Lite Sqlite？
A: 
# ...
### Q2: 遇到错误怎么办？
A: 
# ...
### Q3: Lite Sqlite有什么限制？
A: 
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
## 已知限制
# ...
- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步
# ...