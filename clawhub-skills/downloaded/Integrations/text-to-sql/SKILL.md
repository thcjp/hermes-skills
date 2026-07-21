---
slug: text-to-sql
name: text-to-sql
version: "999.0.0"
displayName: Text To Sql
summary: Use when (1) user describes what data they want in plain English and asks
  for the corresponding S...
license: MIT-0
description: |-
  Use when (1) user describes what data they want in plain English and
  asks for the corresponding S。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags: '[''Integrations'']'
tools:
  - read
  - exec
---

# Text To Sql

Use when (1) user describes what data they want in plain English and asks for the corresponding SQL query. (2) user says "write SQL for this", "convert to query", "how do I select", or "give me the SQL". (3) user provides a database schema or table descriptions and asks a question answerable by SQL.

## Core Position

This skill solves the specific problem of: *non-technical users who know what data they want cannot translate their intent into SQL — they need a bridge from natural language to query.*

This skill IS NOT:

* A SQL execution environment — it writes queries, does not run them
* A schema design tool — it works with existing schema the user provides
* A data analysis tool — it produces SQL, not results or insights

This skill IS activated ONLY when: natural language description + database schema + SQL request are all present.

## Modes

### `/text-to-sql`

**Default mode.** Converts natural language into a syntactically correct SQL query.

When to use: User describes data needs and provides schema — wants the query.

### `/text-to-sql/explain`

Outputs the SQL query with inline comments explaining each clause.

When to use: User wants to understand the query while seeing it, for learning purposes.

### `/text-to-sql/alternatives`

Provides 2-3 alternative query approaches (different JOINs, subqueries vs CTEs, etc.).

When to use: User is learning SQL or wants to compare query strategies.

## Execution Steps

### Step 1 — Confirm Schema

1. Receive natural language request and detect if schema is present
2. Schema may be provided as:
   * Table/column names explicitly in the request
   * A CREATE TABLE statement
   * A DESCRIBE output
   * Column names from a previous query
3. If schema is NOT provided, ask the user for it before proceeding — do not guess table or column names
4. Build a schema map: `table_name → {column: type}`

### Step 2 — Translate Intent to SQL Clauses

Map natural language intent to SQL components:

| Natural Language | SQL Clause |
| --- | --- |
| "all", "every", "complete list" | `SELECT *` or `SELECT all columns` |
| "only", "just", "specifically" | `SELECT [specific columns]` |
| "where [condition]" | `WHERE` clause |
| "sorted by", "in order of" | `ORDER BY` |
| "grouped by", "each [X]" | `GROUP BY` |
| "top N", "first N", "N most" | `LIMIT N` + `ORDER BY` |
| "not", "exclude", "without" | `WHERE NOT` or `!=` / `<>` |
| "both X and Y", "along with" | `AND` in WHERE, or JOIN |
| "either X or Y", "or" | `OR` in WHERE |
| "between X and Y" | `BETWEEN` |
| "like", "containing", "includes" | `LIKE '%value%'` |
| "before", "after", "earlier than" | `WHERE date_column < 'date'` |
| "latest", "most recent", "newest" | `ORDER BY date DESC LIMIT 1` |
| "count of", "how many" | `COUNT(*)` aggregate |
| "total of", "sum of" | `SUM(column)` |
| "average of" | `AVG(column)` |

### Step 3 — Handle Joins and Relationships

If the request involves multiple tables:

1. Identify which tables contain the needed columns
2. Determine the join key (foreign key relationship)
3. Select join type: `INNER JOIN` (default), `LEFT JOIN` (if some side may be empty), `RIGHT JOIN` (rare)
4. Write join on the correct key pair

If schema doesn't include relationship info, ask user to clarify which column links the tables.

### Step 4 — Generate and Validate

```sql
SELECT
  o.order_id,
  o.created_at,
  c.customer_name,
  SUM(o.total_amount) AS total_revenue
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.created_at >= '2024-01-01'
GROUP BY o.order_id, o.created_at, c.customer_name
ORDER BY total_revenue DESC
LIMIT 10;
```

Check:

* All columns referenced exist in the schema
* All table aliases are defined
* JOIN conditions are valid (same type, correct keys)
* No ambiguous column references (all tables have aliases)
* Aggregate queries have appropriate GROUP BY

## Mandatory Rules

### Do not

* Do not invent table names or column names not in the provided schema
* Do not use SQL keywords as column names without backtick quoting where needed
* Do not write `SELECT *` in production queries — list specific columns
* Do not assume which table a column belongs to — qualify all column references

### Do

* Ask for schema information before writing the query if it wasn't provided
* Qualify all column references with table aliases (e.g., `o.order_id`)
* Use backtick or quoted identifiers if column names are SQL reserved words
* Provide both the query and a one-line plain English translation of what it does

## Quality Bar

**A good output:**

* Query is syntactically correct for the stated dialect (PostgreSQL, MySQL, SQLite, etc.)
* All column and table names match the provided schema exactly
* JOIN conditions are valid and use the correct key types
* The query actually answers the stated question

**A bad output:**

* References a column not in the schema
* `SELECT *` without justification in a query that should return specific columns
* Missing `GROUP BY` for an aggregate query
* JOIN on mismatched types (string ID to integer ID)

## 示例

| Scenario | Bad Output | Good Output |
| --- | --- | --- |
| Schema: `users(id, name)`, `orders(user_id, total)` | `SELECT * FROM orders` | `SELECT u.name, SUM(o.total) FROM users u JOIN orders o ON u.id = o.user_id GROUP BY u.name` |
| "top 10 customers" | No `LIMIT 10` or `ORDER BY` | `ORDER BY total DESC LIMIT 10` |
| No schema provided | Writes a query with invented columns | "Could you share the table schema (column names and types)?" |
| "show me revenue by month" | `SELECT revenue` without `GROUP BY` | `SELECT DATE_TRUNC('month', date), SUM(revenue) FROM orders GROUP BY 1` |

## References

* `references/` — SQL dialect cheat sheet (PostgreSQL, MySQL, SQLite), JOIN types and when to use each, common intent-to-clause mapping

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

- Use when (1) user describes what data they want in plain English and
  asks for the corresponding S
- 触发关键词: data, text, describes, sql

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Text To Sql？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Text To Sql有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
