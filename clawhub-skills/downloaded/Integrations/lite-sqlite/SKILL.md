---
slug: lite-sqlite
name: lite-sqlite
version: "1.0.0"
displayName: Lite Sqlite
summary: Fast lightweight local SQLite database for OpenClaw agents with minimal RAM
  and storage usage. Us...
license: MIT
description: |-
  Fast lightweight local SQLite database for OpenClaw agents with minimal
  RAM and storage usage。Us。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
---

# Lite Sqlite
Ultra-lightweight SQLite database management optimized for Skill平台 agents with minimal RAM (~2-5MB) and storage overhead.

## Why SQLite?
✅ **Zero setup** - No server, no configuration, file-based
✅ **Minimal RAM** - 2-5MB typical usage
✅ **Fast** - Millions of queries/second
✅ **Portable** - Single .db file
✅ **Reliable** - ACID compliant, crash-proof
✅ **Cross-platform** - Works everywhere Python works

## 核心能力
* In-memory mode for temporary data (even faster!)
* WAL mode for concurrent access
* Connection pooling
* Automatic schema migration
* Built-in backup/restore
* Query optimization hints

## Quick Start
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

## Performance Optimization
### Essential Settings
```python
import sqlite3

conn = sqlite3.connect("agent_data.db")
conn.execute("PRAGMA journal_mode=WAL")

conn.execute("PRAGMA synchronous=NORMAL")

conn.execute("PRAGMA cache_size=-64000")  # 64MB cache
conn.execute("PRAGMA page_size=4096")

conn.execute("PRAGMA temp_store=MEMORY")
```

### Query Optimization
```python
db.create_index("memos", "tags")
db.create_index("memos", "created_at")

db.query("SELECT * FROM memos WHERE id = ?", (id,))

db.batch_insert("memos", rows_data)
```

---

## Predefined Schemas
### Agent Memo Schema (Memory Store)
```python
db.create_table("agent_memos", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "agent_id": "TEXT NOT NULL",           # Which agent created it
    "key": "TEXT NOT NULL",               # Lookup key
    "value": "TEXT",                      # Stored value
    "priority": "INTEGER DEFAULT 0",       # For retrieval ordering
    "created_at": "TEXT DEFAULT CURRENT_TIMESTAMP",
    "expires_at": "TEXT"                  # Optional TTL
})

db.create_index("agent_memos", "agent_id")
db.create_index("agent_memos", "key")
db.create_index("agent_memos", "expires_at")
```

### Session Log Schema
```python
db.create_table("session_logs", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "session_id": "TEXT NOT NULL",
    "agent": "TEXT NOT NULL",
    "message": "TEXT",
    "metadata": "TEXT",                   # JSON
    "created_at": "TEXT DEFAULT CURRENT_TIMESTAMP"
})

db.create_index("session_logs", "session_id")
db.create_index("session_logs", "created_at")
```

### Cache Schema (TTL-based)
```python
db.create_table("cache", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "key": "TEXT UNIQUE NOT NULL",
    "value": "BLOB",                      # Supports binary data
    "created_at": "TEXT DEFAULT CURRENT_TIMESTAMP",
    "expires_at": "TEXT NOT NULL"
})

db.query("DELETE FROM cache WHERE expires_at < ?", (datetime.now().isoformat(),))

db.create_index("cache", "key")
db.create_index("cache", "expires_at")
```

---

## Advanced Features
### Connection Pooling
```python
from sqlite_connector import ConnectionPool

pool = ConnectionPool("agent_data.db", max_connections=5)

conn = pool.get_connection()
pool.release_connection(conn)
```

### Automatic Backup
```python
db.backup("agent_data_backup.db")

db.auto_backup("backups/", "daily")
```

### Schema Migration
```python
db.add_column("memos", "updated_at", "TEXT DEFAULT CURRENT_TIMESTAMP")

db.migrate("memos", {
    "old_column": "new_column"
})
```

---

## Performance Benchmarks
### Typical Performance
| Operation | Rows | Time (In-Memory) | Time (Disk) |
| --- | --- | --- | --- |
| Insert | 10,000 | 0.05s | 0.3s |
| Select (indexed) | 10,000 | 0.001s | 0.01s |
| Select (full scan) | 10,000 | 0.05s | 0.5s |
| Update | 1,000 | 0.01s | 0.1s |
| Delete | 1,000 | 0.01s | 0.1s |

### Memory Usage
* Base Memory: 2-5MB
* With 100K rows: ~10-15MB
* With 1M rows: ~50-100MB
* In-memory mode: Same as data size + overhead

---

## Best Practices for Skill平台 Agents
### 1. Choose the Right Mode
```python
temp_db = SQLiteDB(":memory:")

persist_db = SQLiteDB("agent_storage.db")
```

### 2. Use Proper Indexes
```python
db.create_index("table", "column_name")

db.create_index("table", "col1, col2")
```

### 3. Batch Operations
```python
for row in rows:
    db.insert("table", row)  # Slow!
db.batch_insert("table", rows)  # Fast!
```

### 4. Use TTL for Expiring Data
```python
db.cleanup_expired("cache", "expires_at")
db.cleanup_old("logs", "created_at", days=7)
```

### 5. Compact Database Periodically
```python
db.vacuum()  # Should be run during downtime
```

---

## DuckDB Alternative (Analytics)
For analytical queries (aggregations, joins on large datasets), consider DuckDB:

```python
import duckdb

conn = duckdb.connect(":memory:")

conn.execute("""
    SELECT COUNT(*) as rows,
           AVG(value) as avg_value
    FROM large_table
""").fetchall()
```

**When to use DuckDB:**

* Analytics on large datasets (>100M rows)
* Complex aggregations and joins
* Columnar data operations
* Statistical analysis

**When to use SQLite:**

* Transactional operations
* Small to medium datasets (<100M rows)
* Point queries and updates
* General-purpose storage

---

## Common Patterns
### 1. Memo Storage
```python
def save_memo(db, agent_id, key, value, ttl_hours=24):
    expires_at = (datetime.now() + timedelta(hours=ttl_hours)).isoformat()
    db.insert("agent_memos", {
        "agent_id": agent_id,
        "key": key,
        "value": json.dumps(value),
        "expires_at": expires_at
    })
```

### 2. Session Persistence
```python
def save_session(db, session_id, agent, message, metadata=None):
    db.insert("session_logs", {
        "session_id": session_id,
        "agent": agent,
        "message": message,
        "metadata": json.dumps(metadata) if metadata else None
    })
```

### 3. Caching Layer
```python
def cache_get(db, key):
    if expired_key := db.query_one(
        "SELECT value FROM cache WHERE key = ? AND expires_at > ?",
        (key, datetime.now().isoformat())
    ):
        return json.loads(expired_key)
    return None

def cache_set(db, key, value, ttl_seconds=3600):
    expires_at = (datetime.now() + timedelta(seconds=ttl_seconds)).isoformat()
    db.insert_or_replace("cache", {
        "key": key,
        "value": json.dumps(value),
        "expires_at": expires_at
    })
```

---

## Error Handling
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

## Size Optimization Tips
### Reduce Storage
1. **Use appropriate data types:**

   * INTEGER instead of TEXT for numbers
   * REAL instead of TEXT for floats
   * Use CHECK constraints for validation
2. **Normalize data:**

   * Store JSON as TEXT
   * Use TEXT for variable-length strings
   * Avoid storing redundant data
3. **Vacuum regularly:**

   python

   ```
   db.vacuum()  # Reclaims space after deletes
   ```
4. **Use WAL instead of journal:**

   python

   ```
   conn.execute("PRAGMA journal_mode=WAL")
   ```

---

## Migration from Other Stores
### From JSON Files
```python
import json

with open("data.json") as f:
    data = json.load(f)

db.create_table("json_data", {key: "TEXT" for key in data[0].keys()})
db.batch_insert("json_data", data)
```

### From CSV Files
```python
import pandas as pd

df = pd.read_csv("data.csv")
df.to_sql("csv_data", conn, if_exists="replace", index=False)
```

---

## Troubleshooting
### Database Locked Error
```python
conn.execute("PRAGMA journal_mode=WAL")

pool = ConnectionPool("db.db", timeout=5.0)
```

### Slow Queries
```python
plan = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM ...").fetchall()

db.create_index("table", "column")

conn.execute("ANALYZE")
```

### Large Database Size
```python
size_info = conn.execute("PRAGMA page_count, page_size").fetchone()
print(f"Size: {(page_count * page_size) / (1024*1024):.2f} MB")

db.vacuum()
```

---

## CLI Tool
The bundled `sqlite_cli.py` provides command-line access:

```bash
python scripts/sqlite_cli.py create agent_data.db

python scripts/sqlite_cli.py create-table agent_memos -c id:INTEGER:P -c title:TEXT -c content:TEXT

python scripts/sqlite_cli.py insert agent_memos '{"title": "Test", "content": "Hello"}'

python scripts/sqlite_cli.py query "SELECT * FROM agent_memos"

python scripts/sqlite_cli.py optimize agent_data.db
```

---

## Resources
* **SQLite Documentation:** <https://www.sqlite.org/docs.html>
* **Python sqlite3:** <https://docs.python.org/3/library/sqlite3.html>
* **DuckDB:** <https://duckdb.org/docs/>
* **Performance:** <https://www.sqlite.org/optoverview.html>

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

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例
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
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Lite Sqlite有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步
