---
slug: database-admin
name: database-admin
version: "2.0.0"
displayName: database-admin
summary: 提供数据库表结构设计、数据批量操作、复杂查询优化、类型处理及事务安全的全面数据库管理服务。
license: MIT-0
description: |-
  提供数据库表结构设计、数据批量操作、复杂查询优化、类型处理及事务安全的全面数据库管理服务。核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# database-admin

> "先严父后慈" —— 杜子美

本技能提供全面的数据库管理功能，包括表结构创建、数据操作、查询优化、类型处理（如 BIGINT）等。所有操作均遵循 SQL 最佳实践和事务安全原则。

## 核心能力

### 🔹 表结构设计

* 自动设计最优表结构（主键、索引、约束）
* 支持多种数据类型（TEXT、VARCHAR、BIGINT、UUID、JSONB、ENUM）
* 自动创建适当的索引以提高查询性能
* 设置外键约束和检查约束
* 处理 NULL 值和默认值策略

### 🔹 数据插入

* 批量插入大量数据（使用事务优化）
* 处理 BIGINT 等大数类型数据
* 验证数据类型兼容性
* 避免主键冲突和外键违规

### 🔹 查询优化

* 编写高效的 JOIN 查询
* 聚合统计和分析查询
* 子查询和 CTE 的使用
* 执行计划分析和优化建议

### 🔹 数据库维护

* CREATE TABLE、ALTER TABLE、DROP TABLE
* INDEX 创建和 DROP INDEX
* TRUNCATE 清空表（保留结构）
* VACUUM 分析表
* 备份和恢复操作

## 使用场景

当你需要以下操作时，请触发此技能：

* "创建一个用户表，包含用户名、邮箱、注册时间"
* "向 products 表中插入这些商品数据..."
* "查询所有销售额超过 10 万元的订单"
* "为 orders 表的 customer_id 创建索引"
* "将 text_column 从 TEXT 转换为 VARCHAR(255)"
* "批量导入 10 万条记录，使用事务优化"
* "修复 BIGINT 类型数据溢出问题"

## 不适用场景

以下场景database-admin不适合处理：

- 实时流数据处理
- 小规模数据手动分析
- 非结构化文本情感分析


## 触发条件

需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于非本工具能力范围的需求。


## 技术细节

本技能在幕后会使用：

* **驱动**: `pg` (PostgreSQL)
* **连接池**: `pgpool` 管理并发连接
* **批量插入**: 使用 COPY 或批量 INSERT 优化性能
* **事务控制**: 自动开启/提交事务，保证 ACID 属性
* **错误处理**: 捕获并报告约束违规、类型不匹配等

## 数据库配置（roadflow）

* **主机**: 192.168.1.136
* **端口**: 35438
* **用户**: postgres
* **密码**: Hxkj510510
* **目标库**: roadflow

## 示例

### 创建表

```text
创建一个库存表 stock_info，包含：
- id (SERIAL PRIMARY KEY)
- product_name (VARCHAR(100))
- quantity (INT)
- price (DECIMAL(10,2))
- created_at (TIMESTAMP)
- 为 product_name 创建索引
```

### 插入数据

```text
向 stock_info 表插入以下商品：
[{product_name: "苹果", quantity: 100, price: 8.5}, ...]
```

### 查询统计

```text
计算每个类别的商品平均价格
WHERE quantity > 50
GROUP BY category
ORDER BY avg_price DESC
```

---

*技能由杜甫（📜）编写，秉承"致君尧舜上，再使风俗淳"的务实精神*

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

### Q1: 如何开始使用database-admin？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: database-admin有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
