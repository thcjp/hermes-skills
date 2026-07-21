---
slug: knowledge-ontology-free
name: knowledge-ontology-free
version: "1.0.0"
displayName: 知识本体
summary: 类型化知识图谱基础版：实体关系建模+约束校验+图遍历查询。
license: MIT
description: |-
  面向AI Agent的类型化知识图谱系统基础版，提供实体关系建模、约束校验、图遍历查询三大核心能力。
  内置Person/Project/Task等基础实体类型与required/enum/forbidden_properties等约束规则。
  支持按类型与条件查询实体、关联查询、依赖关系遍历。
  适用于需要结构化查询的Agent记忆、多实体关系管理、依赖追踪场景。
  避免扁平文件记忆难查询、约束缺失数据脏等基础问题。
tools:
  - read
  - exec
---

# 知识本体（基础版）

将Agent记忆从扁平文件升级为类型化可验证的知识图谱，支持实体关系建模、约束校验与图遍历查询，让知识结构化、可查询。

## 核心能力

- **类型化实体与关系系统**：内置 Person/Organization/Project/Task/Goal/Event/Location/Document/Note 共9种基础实体类型。每个实体遵循标准结构 `{"id":"ent_001","type":"Project","properties":{...},"relations":[...],"created":"2026-01-15T10:00:00Z","updated":"2026-01-15T10:00:00Z"}`。支持 has_owner/has_task/depends_on/relates_to 等基础关系类型，关系建立前校验类型兼容性。
- **约束校验引擎**：支持3类基础约束规则——required（必填属性，如 Task 必须有 title 和 status）、enum（枚举值，如 status 只能是 open/in_progress/done/blocked）、defaults（默认值，如 status 默认 open）。执行 `python3 scripts/ontology.py validate` 输出校验报告，标记通过与失败的实体。
- **图遍历查询**：按类型与条件查询实体（`query --type Task --where '{"status":"open"}'`），执行关联查询（`related --id proj_001 --rel has_task`），遍历依赖关系链（`traverse --id task_001 --rel depends_on --direction outgoing`），支持正向与反向遍历。
### 类型化实体与关系系统

执行类型化实体与关系系统操作,处理用户输入并返回结果。

**输入**: 用户提供类型化实体与关系系统所需的参数和指令。

**输出**: 返回类型化实体与关系系统的处理结果。

- 执行`类型化实体与关系系统`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`类型化实体与关系系统`相关配置参数进行设置
### 约束校验引擎

执行约束校验引擎操作,处理用户输入并返回结果。

**输入**: 用户提供约束校验引擎所需的参数和指令。

**输出**: 返回约束校验引擎的处理结果。

- 执行`约束校验引擎`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`约束校验引擎`相关配置参数进行设置
### 图遍历查询

执行图遍历查询操作,处理用户输入并返回结果。

**输入**: 用户提供图遍历查询所需的参数和指令。

**输出**: 返回图遍历查询的处理结果。

- 执行`图遍历查询`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`图遍历查询`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: 类型化知识图谱基、实体关系建模、Agent、的类型化知识图谱、系统基础版、提供实体关系建模、图遍历查询三大核、心能力、等基础实体类型与、forbidden、等约束规则、支持按类型与条件、依赖关系遍历、适用于需要结构化、多实体关系管理、依赖追踪场景、避免扁平文件记忆、难查询、约束缺失数据脏等、基础问题。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

### 第一步：初始化目录与schema

创建图谱存储目录并写入初始schema定义。

```bash
mkdir -p memory/ontology
touch memory/ontology/graph.jsonl
python3 scripts/ontology.py schema-append --data '{
  "types": {
    "Task": { "required": ["title", "status"], "defaults": {"status": "open"} },
    "Project": { "required": ["name"] },
    "Person": { "required": ["name"] }
  },
  "relations": {
    "has_owner": { "from_types": ["Project"], "to_types": ["Person"] },
    "has_task": { "from_types": ["Project"], "to_types": ["Task"] },
    "depends_on": { "from_types": ["Task"], "to_types": ["Task"] }
  }
}'
```

### 第二步：创建实体与关系

使用 create 命令追加实体到图谱文件末尾，使用 relate 命令建立关系。

```bash
python3 scripts/ontology.py create --type Person --props '{"name":"Alice","role":"developer"}'
python3 scripts/ontology.py create --type Project --props '{"name":"用户中心重构","status":"active"}'
python3 scripts/ontology.py relate --from proj_001 --rel has_owner --to p_001
python3 scripts/ontology.py relate --from proj_001 --rel has_task --to task_001
```

### 第三步：查询与遍历

按类型与条件查询实体，执行关联查询与依赖遍历。

```bash
python3 scripts/ontology.py query --type Task --where '{"status":"open"}'
python3 scripts/ontology.py related --id proj_001 --rel has_task
python3 scripts/ontology.py traverse --id task_001 --rel depends_on --direction outgoing
python3 scripts/ontology.py validate
```

## 错误处理

| 错误类型 | 原因 | 处理方式 |
|:---|:---|:---|
| 校验失败：缺必填属性 | 实体未提供 required 字段，如 Task 缺少 status | 按提示补全属性后重新提交；或使用 defaults 配置自动填充默认值 |
| 关系创建失败：类型不匹配 | relate 命令的 from/to 类型与 schema 中声明不符 | 检查 schema 中该关系的 from_types/to_types 声明，确认实体类型后再建立关系 |
| 查询无结果 | 实体不存在、类型名拼写错误或 where 条件过严 | 执行 `list --type Project` 确认实体存在；检查 where 条件中的属性名与值 |

## 示例

### 示例1：项目任务依赖查询

**输入：** 用户问"用户中心重构项目有哪些未完成的任务？"

**执行：**
1. 查询项目：`query --type Project --where '{"name":"用户中心重构"}'` 返回 proj_001
2. 遍历 has_task 关系：`related --id proj_001 --rel has_task`
3. 过滤状态为 open 的 Task

**输出：**
```
项目：用户中心重构（proj_001）
未完成任务（3条）：
- task_001: 设计用户认证接口（status: open）
- task_002: 实现权限管理模块（status: open，depends on task_001）
- task_005: 编写集成测试（status: open，depends on task_002）

建议执行顺序：task_001 → task_002 → task_005
```

## FAQ

**Q1：JSONL存储有性能问题吗？**
A：实体数小于1000条时JSONL性能足够。超过1000条后查询会变慢，建议定期清理无用实体或考虑升级到付费版使用SQLite数据库存储。

**Q2：约束校验支持哪些规则？**
A：基础版支持3类约束——required（必填）、enum（枚举）、defaults（默认值）。如需 forbidden_properties、cardinality、acyclic、validate 等高级约束规则，请升级到付费版。

**Q3：基础版支持模式演进吗？**
A：基础版不支持三步法模式演进与迁移脚本。如需在不破坏旧数据的前提下修改schema，请升级到付费版获取完整的模式演进管理能力。

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---|:---|:---|:---|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| Python 3.8+ | 运行时 | 必需 | 系统安装Python 3.8或更高版本 |
| PyYAML | Python包 | 必需 | 执行 `pip install pyyaml` 解析schema定义文件 |
| Agent平台 | 运行环境 | 必需 | 支持SKILL.md的任意AI Agent平台 |

**API Key配置：** 本Skill无需任何API Key，纯本地文件操作，无网络请求。

**可用性分类：** MD+EXEC（Markdown指令 + exec命令行执行）。核心实体与关系概念纯Markdown可理解；创建、查询、校验操作需Python脚本执行。

## 已知限制

1. **实体类型有限**：基础版内置9种实体类型，不支持自定义实体类型与扩展类型系统。
2. **约束规则有限**：仅支持required/enum/defaults共3类约束，不支持forbidden_properties/cardinality/acyclic/validate等高级约束。
3. **无模式演进管理**：不支持三步法迁移与append-only历史回滚，schema变更需手动处理旧数据兼容性。
4. **无多步规划建模**：不支持将工作流建模为图变换序列与自动回滚机制。

## 升级提示

本基础版提供知识图谱的核心创建与查询能力。升级到付费版可解锁以下高级能力：

- **完整15+实体类型**：包含Credential/Action/Policy等高级类型，覆盖更广泛的业务场景
- **7类完整约束规则**：新增forbidden_properties（敏感字段防护）、cardinality（关系基数控制）、acyclic（无环校验）、validate（自定义表达式）四类高级约束
- **模式演进管理**：append-only历史保留 + 三步迁移法，确保schema变更不破坏旧数据，支持任意时间点回滚
- **图遍历规划**：多步计划建模为图操作序列，每步自动校验约束，违反约束自动回滚
- **Skill契约声明**：声明reads/writes边界与前后置条件，避免多Skill并发写入冲突
- **循环依赖检测**：`cycle-check`命令自动定位blocks关系中的环路
- **SQLite数据库存储**：实体数超过10000条时自动迁移，支持事务与高性能查询

升级后可处理更复杂的知识管理场景，包括凭证安全存储、影响分析、拓扑排序等高级图遍历任务。
