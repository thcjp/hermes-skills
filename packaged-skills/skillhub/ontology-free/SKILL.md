---
slug: "ontology-free"
name: "ontology-free"
version: "1.0.0"
displayName: "类型化知识图谱引擎"
summary: "基于类型约束的知识图谱系统，为智能代理提供基础结构化记忆。类型化知识图谱引擎，将知识表示为可验证的实体-关系图谱。每个实体拥有类型、属性和关系， 所有变更在提交前根据类型约束进行验证。基础能"
license: "MIT"
description: |-
  类型化知识图谱引擎，将知识表示为可验证的实体-关系图谱。每个实体拥有类型、属性和关系，
  所有变更在提交前根据类型约束进行验证。基础能力涵盖类型化实体创建与验证、关系图谱与基数约束、
  Schema约束系统。支持 Person、Project、Task 等核心实体类型，可通过Schema自定义扩展.
  数据以追加式 JSONL 格式存储。适用于项目任务管理、依赖关系追踪、知识库构建等场景.
tools:
  - read
  - exec
  - write
homepage: ""
tags: 效率,schema,task,status,type,返回
category: "Automation"
---
# 类型化知识图谱引擎（基础版）

将知识表示为可验证的实体-关系图谱系统。一切皆为实体，拥有类型、属性和与其他实体的关系。每次变更在提交前根据类型约束进行验证，确保图谱一致性。支持追加式变更日志，保留完整历史记录.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 类型化知识图谱引擎处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 核心能力

### 1. 类型化实体创建与验证
创建带有类型约束的实体，支持核心预定义类型和自定义扩展：

| 核心类型 | 必需属性 | 可选属性 |
|:-----|:-----|:-----|
| Person | name | email, phone, notes |
| Project | name, status | goals[], owner |
| Task | title, status | due, priority, assignee |
| Document | title | path, url, summary |
| Note | content | tags[], refs[] |

参数：`--type`（实体类型）、`--props`（JSON格式属性）

输出：实体ID（如 `p_001`、`task_003`）、创建时间戳、验证结果.
**处理**: 解析类型化实体创建与验证的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 2. 关系图谱与基数约束
在实体之间建立类型化关系，支持基数约束验证：

| 关系类型 | 源类型 | 目标类型 | 基数 |
|---:|---:|---:|---:|
| has_owner | Project, Task | Person | many_to_one |
| has_task | Project | Task | one_to_many |
| has_member | Organization | Person | many_to_many |

参数：`--from`（源实体ID）、`--rel`（关系类型）、`--to`（目标实体ID）

输出：关系记录、基数验证结果.
**处理**: 解析关系图谱与基数约束的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 3. Schema约束系统
通过 `memory/ontology/schema.yaml` 定义类型约束，所有变更在提交前强制验证：

```yaml
types:
  Task:
    required: [title, status]
    status_enum: [open, in_progress, blocked, done]
  Event:
    required: [title, start]
    validate: "end >= start if end exists"
```

支持的约束类型：必填属性（required）、枚举值（enum）、自定义验证（validate）、关系基数（cardinality）.
**处理**: 解析Schema约束系统的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Schema约束系统的处理结果,包含执行状态码、结果数据和执行日志.
### 4. 图谱遍历查询
支持基础查询和关联遍历操作：

| 查询类型 | 命令 | 用途 |
|:---:|:---:|:---:|
| 类型查询 | `query --type Task --where '{"status":"open"}'` | 按类型和条件筛选实体 |
| ID查询 | `get --id task_001` | 获取单个实体详情 |
| 关联查询 | `related --id proj_001 --rel has_task` | 查询实体的关联实体 |

**输入**: 用户提供图谱遍历查询所需的指令和必要参数.
**处理**: 解析图谱遍历查询的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回图谱遍历查询的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用流程

### 第一步：初始化图谱目录与Schema

创建 `memory/ontology/` 目录和空的 `graph.jsonl` 文件。编写 `schema.yaml` 定义项目所需的实体类型和关系约束。执行 `python3 （请参考skill目录中的脚本文件） validate` 验证Schema格式正确.
### 第二步：创建核心实体并建立关系

根据项目需求创建 Person、Project、Task 等基础实体，使用 `relate` 命令在实体之间建立关系。创建关系时系统自动验证基数约束，违反约束的操作被拒绝并返回错误信息.
### 第三步：查询与验证图谱

使用 `query`、`get`、`related` 等命令查询图谱信息。定期执行 `validate` 命令检查所有约束是否满足.
## 错误处理

| 错误类型 | 原因 | 处理方式 |
|:------|------:|:------|
| 必填属性缺失 | 创建实体时未提供 required 列表中的属性 | 检查 schema.yaml 中该类型的 required 定义，补全缺失属性后重新创建 |
| 枚举值非法 | 属性值不在 status_enum 定义的允许范围内 | 查阅 schema.yaml 中该属性的 enum 列表，使用合法值重新提交 |
| 基数约束违反 | 在 many_to_one 关系中为目标实体分配了多个源实体 | 检查已有关系记录，移除冲突关系或将关系类型改为 many_to_many |

## 示例

### 示例：创建项目任务体系并建立关系

场景：为"网站重设计"项目创建负责人和任务列表.
```bash
# 创建人员
python3 （请参考skill目录中的脚本文件） create --type Person --props '{"name":"Alice","email":"alice@example.com"}'
# 返回: {"id":"p_001","type":"Person","properties":{"name":"Alice","email":"alice@example.com"}}
# ...
# 创建项目
python3 （请参考skill目录中的脚本文件） create --type Project --props '{"name":"Website Redesign","status":"active"}'
# 返回: {"id":"proj_001","type":"Project","properties":{"name":"Website Redesign","status":"active"}}
# ...
# 建立项目-负责人关系
python3 （请参考skill目录中的脚本文件） relate --from proj_001 --rel has_owner --to p_001
# 返回: {"from":"proj_001","rel":"has_owner","to":"p_001","validated":true}
# ...
# 创建任务
python3 （请参考skill目录中的脚本文件） create --type Task --props '{"title":"设计首页原型","status":"open","priority":8}'
# 返回: {"id":"task_001","type":"Task","properties":{"title":"设计首页原型","status":"open","priority":8}}
# ...
# 建立项目-任务关系
python3 （请参考skill目录中的脚本文件） relate --from proj_001 --rel has_task --to task_001
# 返回: {"validated":true}
# ...
# 查询项目所有任务
python3 （请参考skill目录中的脚本文件） related --id proj_001 --rel has_task
# 返回: [task_001]
```

## FAQ

### Q1: 知识图谱的数据存储在哪里？支持什么格式？

默认存储在 `memory/ontology/graph.jsonl`，采用追加式JSONL格式，每行一个操作记录。追加式写入保证历史可追溯，支持回放重建任意时间点状态.
### Q2: 如何自定义新的实体类型和关系类型？

在 `memory/ontology/schema.yaml` 中的 `types` 下新增类型定义，指定 `required`（必填属性）、`enum`（枚举值）等约束。在 `relations` 下新增关系定义，指定 `from_types`、`to_types`、`cardinality`（基数）。新增后执行 `validate` 命令确认Schema格式正确.
### Q3: 图谱文件被意外修改后如何恢复？

graph.jsonl 采用追加式写入，每行是独立的JSON记录。如果部分行损坏，可手动检查并修复损坏的JSON行。建议将 `memory/ontology/` 目录纳入Git版本控制，定期提交变更，通过 `git checkout` 恢复到最近的有效版本.
## 依赖说明

### 运行环境
- **Agent平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python环境**：Python 3.8+（脚本执行依赖）
- **本地存储**：可写的 `memory/ontology/` 目录

### 依赖项

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| Python 3.8+ | 运行时环境 | 必需 | 系统安装 |
| ontology.py 脚本 | 运行时库 | 必需 | 随技能安装 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 核心功能无需任何 API Key

### 可用性分类
- **分类**：MD+EXEC（Markdown指令驱动，需exec执行Python脚本）
- **说明**：通过自然语言指令驱动Agent执行图谱创建、查询和验证操作

## 已知限制

1. **无无环验证**：基础版不支持 depends_on 和 blocks 关系的循环依赖检测，无法自动防止任务依赖形成环.
2. **实体类型有限**：基础版仅支持 Person、Project、Task、Document、Note 5种核心类型，不支持 Credential、Event、Location 等高级类型.
3. **无跨技能契约**：基础版不支持技能间的读写权限声明和前后置条件验证，多技能协作时需手动协调.
4. **无计划即图谱变换**：基础版不支持将多步计划建模为图谱操作序列，无法实现步骤级验证和自动回滚.
5. **查询深度有限**：基础版关联查询仅支持单跳遍历，无法进行多跳依赖链和路径查询.
## 升级提示

当前为基础版，以下高级能力需升级至完整版解锁：

- **无环验证（DAG检查）**：对 blocks 和 depends_on 关系执行有向无环图检查，自动防止循环依赖，检测到环时返回完整环路路径.
- **12种核心实体类型**：在基础5种类型上增加 Organization、Goal、Event、Location、Message、Account、Credential 共7种高级类型，支持更丰富的知识建模.
- **跨技能契约声明**：通过 reads/writes/preconditions/postconditions 声明技能读写范围，前置条件执行前验证，后置条件执行后验证，违反时自动回滚.
- **计划即图谱变换**：将多步计划建模为图谱操作序列，每步验证通过后提交，任一步骤失败则回滚已执行步骤.
- **多跳图谱遍历**：支持 `--depth` 参数控制遍历深度（最多3跳），支持路径查询 `path --from --to` 查找两实体间的关系路径.
- **追加式变更日志修复**：提供 `validate --repair` 命令自动修复损坏的JSONL行，支持从最近有效状态重建图谱.
- **大规模图谱迁移**：支持将JSONL图谱迁移至 SQLite数据库，提升1000+实体规模的查询性能.
升级至完整版以获取全部8项核心能力、8个领域专属错误处理场景和2个完整实战案例.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "类型化知识图谱引擎处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "ontology"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
