---
slug: knowledge-ontology
name: knowledge-ontology
version: "2.0.0"
displayName: 知识本体
summary: 类型化知识图谱：约束校验+模式演进+图遍历规划，让Agent记忆结构化可验证。
license: MIT
description: |-
  面向 AI Agent 的类型化知识图谱系统，直击"非结构化记忆难查询、约束缺失数据脏、模式演进破坏旧数据、图遍历无规划"四大痛点。将知识表示为可验证的类型化实体图，每次变更前自动校验类型约束，支持将多步规划建模为图变换序列。

  核心能力包括类型化实体与关系系统（Person/Project/Task/Event 等 15+ 内置类型）、约束校验引擎（必填/枚举/禁止属性/基数/无环校验）、模式演进管理（append-only 历史保留 + 迁移脚本）、图遍历规划（多步计划建模为图操作序列）、Skill 契约声明（读写声明 + 前后置条件）、JSONL 到 SQLite 平滑迁移、跨 Skill 通信模式。

  适用场景：需要结构化查询的 Agent 记忆、多实体关系管理、依赖追踪与影响分析、多步计划建模与验证、跨 Skill 共享状态、需要数据完整性的知识库。

  差异化：相比扁平文件记忆，本系统提供类型约束防止脏数据、图遍历支持复杂关系查询、模式演进保留历史不破坏旧数据、Skill 契约明确读写边界、规划即图变换支持回滚。从 JSONL 到 SQLite 提供清晰扩展路径。

  触发关键词：知识图谱、本体、实体关系、知识管理、ontology、graph、类型化、约束校验、图遍历
tags:
- 智能代理
- 知识管理
- 数据建模
tools:
- read
- exec
---

# 知识本体（Knowledge Ontology）

**一切皆实体，一切变更皆受约束。** 将 Agent 记忆从扁平文件升级为类型化可验证的知识图谱，支持图遍历查询、模式演进、多步规划建模，让知识结构化、可查询、可信任。

## 痛点与对策速查

| 用户痛点 | 发生场景 | 本系统对策 |
|:---|:---|:---|
| 记忆难查询 | 扁平文件无法按关系查找 | 类型化实体 + 图遍历查询 |
| 数据脏乱 | 无约束，字段缺失/类型错 | 约束校验引擎（必填/枚举/类型） |
| 模式演进破坏旧数据 | 改 schema 后旧记录失效 | append-only 历史 + 迁移脚本 |
| 依赖关系不清 | 不知改一个任务影响哪些 | 图遍历依赖查询 + 影响分析 |
| 多步计划无验证 | 计划中途出错难回滚 | 规划即图变换，每步校验+回滚 |
| Skill 间状态混乱 | 多 Skill 读写无边界 | Skill 契约声明（读写+前后置条件） |
| 大图性能差 | JSONL 全量扫描太慢 | JSONL→SQLite 平滑迁移路径 |
| 敏感信息直存 | 凭证/密码写入图谱 | forbidden_properties 强制间接引用 |

## 核心概念

一切皆**实体**，有**类型**、**属性**、**关系**。每次变更前校验类型约束。

```text
Entity: { id, type, properties, relations, created, updated }
Relation: { from_id, relation_type, to_id, properties }
```

## 何时使用

| 触发情境 | 动作 |
|:---|:---|
| "记住..." | 创建/更新实体 |
| "我对 X 了解什么" | 查询图谱 |
| "把 X 关联到 Y" | 创建关系 |
| "显示项目 Z 的所有任务" | 图遍历 |
| "X 依赖什么" | 依赖查询 |
| 规划多步工作 | 建模为图变换序列 |
| Skill 需要共享状态 | 读写本体对象 |

## 内置类型系统

```yaml
Person: { name, email?, phone?, notes? }
Organization: { name, type?, members[] }

Project: { name, status, goals[], owner? }
Task: { title, status, due?, priority?, assignee?, blockers[] }
Goal: { description, target_date?, metrics[] }

Event: { title, start, end?, location?, attendees[], recurrence? }
Location: { name, address?, coordinates? }

Document: { title, path?, url?, summary? }
Message: { content, sender, recipients[], thread? }
Thread: { subject, participants[], messages[] }
Note: { content, tags[], refs[] }

Account: { service, username, credential_ref? }
Device: { name, type, identifiers[] }
Credential: { service, secret_ref }  # 永不直接存储密钥

Action: { type, target, timestamp, outcome? }
Policy: { scope, rule, enforcement }
```

## 存储与演进

### 默认存储：JSONL（append-only）

```text
memory/ontology/graph.jsonl

{"op":"create","entity":{"id":"p_001","type":"Person","properties":{"name":"Alice"}}}
{"op":"create","entity":{"id":"proj_001","type":"Project","properties":{"name":"网站重构","status":"active"}}}
{"op":"relate","from":"proj_001","rel":"has_owner","to":"p_001"}
```

### Append-Only 规则（关键）

处理已有本体数据时，**追加/合并**而非覆盖文件。保留历史，避免破坏先前定义。

```text
错误做法：读取 graph.jsonl → 修改 → 覆盖写入
正确做法：读取 graph.jsonl → 追加新 op 到文件末尾
```

### 规模扩展：JSONL → SQLite

| 规模 | 存储选择 | 性能 |
|:---|:---|:---|
| <1000 实体 | JSONL | 足够 |
| 1000-10000 | JSONL + 索引 | 可接受 |
| >10000 | SQLite | 推荐 |

迁移命令：

```bash
python3 scripts/ontology.py migrate --from jsonl --to sqlite
```

## 约束系统（差异化核心）

在 `memory/ontology/schema.yaml` 定义约束：

```yaml
types:
  Task:
    required: [title, status]
    status_enum: [open, in_progress, blocked, done]
    defaults:
      priority: 3

  Event:
    required: [title, start]
    validate: "end >= start if end exists"

  Credential:
    required: [service, secret_ref]
    forbidden_properties: [password, secret, token, api_key]  # 强制间接引用

relations:
  has_owner:
    from_types: [Project, Task]
    to_types: [Person]
    cardinality: many_to_one

  blocks:
    from_types: [Task]
    to_types: [Task]
    acyclic: true  # 禁止循环依赖

  depends_on:
    from_types: [Task, Project]
    to_types: [Task, Project, Document]
    cardinality: many_to_many
```

### 校验规则类型

| 规则类型 | 说明 | 示例 |
|:---|:---|:---|
| required | 必填属性 | Task 必须有 title 和 status |
| enum | 枚举值限制 | status 只能是 4 种之一 |
| forbidden_properties | 禁止属性 | Credential 禁止存 password |
| cardinality | 关系基数 | has_owner 多对一 |
| acyclic | 无环校验 | blocks 关系不能成环 |
| validate | 自定义表达式 | Event 的 end >= start |
| defaults | 默认值 | Task priority 默认 3 |

### 校验执行

```bash
# 全量校验
python3 scripts/ontology.py validate

# 输出示例
✓ 142 个实体校验通过
✗ 3 个实体校验失败：
  - task_042: 缺少必填属性 'status'
  - event_015: end(2026-01-01) < start(2026-01-15)
  - cred_001: 包含禁止属性 'password'
```

## 模式演进管理（差异化核心）

模式变更不破坏旧数据的三步法：

### 第 1 步：追加新 schema（不删旧）

```bash
python3 scripts/ontology.py schema-append --data '{
  "types": {
    "Task": {
      "required": ["title", "status", "priority"],
      "status_enum": ["open", "in_progress", "blocked", "done", "cancelled"],
      "defaults": {"priority": 3}
    }
  }
}'
```

### 第 2 步：编写迁移脚本

```python
# migrations/001_add_priority_to_tasks.py
def migrate(graph):
    for entity in graph.query(type="Task"):
        if "priority" not in entity.properties:
            entity.properties["priority"] = 3  # 默认值
    return graph
```

### 第 3 步：执行迁移 + 校验

```bash
python3 scripts/ontology.py migrate --script 001_add_priority_to_tasks.py
python3 scripts/ontology.py validate
```

## 工作流

### 创建实体

```bash
python3 scripts/ontology.py create --type Person --props '{"name":"Alice","email":"alice@example.com"}'
```

### 查询

```bash
# 按类型+条件查询
python3 scripts/ontology.py query --type Task --where '{"status":"open"}'

# 按 ID 获取
python3 scripts/ontology.py get --id task_001

# 关联查询
python3 scripts/ontology.py related --id proj_001 --rel has_task
```

### 关联实体

```bash
python3 scripts/ontology.py relate --from proj_001 --rel has_task --to task_001
```

### 依赖分析（差异化核心）

```bash
# 查询某任务的所有依赖
python3 scripts/ontology.py traverse --id task_001 --rel depends_on --direction outgoing

# 查询依赖某任务的所有任务（反向影响分析）
python3 scripts/ontology.py traverse --id task_001 --rel depends_on --direction incoming

# 检测循环依赖
python3 scripts/ontology.py cycle-check --rel blocks
```

## 规划即图变换（差异化核心）

将多步计划建模为图操作序列，每步校验，违反约束则回滚：

```text
计划："安排团队会议并创建后续任务"

1. CREATE Event { title: "团队同步", attendees: [p_001, p_002] }
2. RELATE Event -> has_project -> proj_001
3. CREATE Task { title: "准备议程", assignee: p_001 }
4. RELATE Task -> for_event -> event_001
5. CREATE Task { title: "发送纪要", assignee: p_001, blockers: [task_001] }
```

每步执行前校验约束，失败则回滚到上一步。

```bash
python3 scripts/ontology.py plan --file plan.yaml --validate-each --rollback-on-fail
```

## Skill 契约声明（差异化核心）

使用本体的 Skill 应声明读写边界：

```yaml
ontology:
  reads: [Task, Project, Person]
  writes: [Task, Action]
  preconditions:
    - "Task.assignee 必须存在"
    - "Project.status == active"
  postconditions:
    - "创建的 Task status=open"
    - "Action 已记录"
```

### 契约执行流程

```text
Skill 调用 → 检查 reads 声明 → 验证前置条件
  → 执行操作 → 验证后置条件 → 检查 writes 声明
  → 全部通过 → 提交
  → 任一失败 → 回滚 + 报错
```

## 跨 Skill 通信模式

```python
# Skill A 创建承诺
commitment = ontology.create("Commitment", {
    "source_message": msg_id,
    "description": "周五前发报告",
    "due": "2026-01-31"
})

# Skill B 查询待办承诺并转为任务
tasks = ontology.query("Commitment", {"status": "pending"})
for c in tasks:
    ontology.create("Task", {
        "title": c.description,
        "due": c.due,
        "source": c.id
    })
```

## 快速开始

```bash
# 1. 初始化目录
mkdir -p memory/ontology
touch memory/ontology/graph.jsonl

# 2. 定义基础 schema
python3 scripts/ontology.py schema-append --data '{
  "types": {
    "Task": { "required": ["title", "status"] },
    "Project": { "required": ["name"] },
    "Person": { "required": ["name"] }
  }
}'

# 3. 创建实体
python3 scripts/ontology.py create --type Person --props '{"name":"Alice"}'
python3 scripts/ontology.py create --type Project --props '{"name":"网站重构","status":"active"}'

# 4. 建立关系
python3 scripts/ontology.py relate --from proj_001 --rel has_owner --to p_001

# 5. 查询
python3 scripts/ontology.py list --type Person
python3 scripts/ontology.py related --id proj_001 --rel has_owner
```

## 真实场景示例

### 场景 1：项目依赖管理

```text
用户："重构支付模块需要先完成哪些任务？"

代理执行：
1. 查找支付模块相关 Project
2. 遍历 has_task 关系找到所有 Task
3. 遍历 blocks 关系找到阻塞链
4. 拓扑排序输出执行顺序

输出：
  执行顺序：
  1. 设计支付接口（task_001）— 无阻塞
  2. 实现支付网关（task_002）— blocked by task_001
  3. 集成测试（task_003）— blocked by task_002
  4. 上线部署（task_004）— blocked by task_003
```

### 场景 2：影响分析

```text
用户："如果推迟数据库迁移，影响哪些任务？"

代理执行：
1. 找到数据库迁移 Task
2. 反向遍历 depends_on 关系
3. 找出所有依赖该任务的 Task

输出：
  影响范围（3 个任务）：
  - task_015: API 部署（depends on 迁移）
  - task_022: 性能测试（depends on task_015）
  - task_031: 上线（depends on task_022）
  
  建议级联调整截止日期。
```

### 场景 3：凭证安全存储

```text
用户："记住我的 Stripe API Key"

代理执行：
1. 检查 Credential 类型约束 → forbidden_properties: [api_key, secret]
2. 拒绝直接存储
3. 创建间接引用：
   ontology.create("Credential", {
     "service": "stripe",
     "secret_ref": "vault://secrets/stripe_key"  # 指向外部密钥库
   })

输出："已记录 Stripe 凭证引用（密钥本身存储在密钥库，未写入图谱）"
```

## 常见问题 FAQ

**Q1：JSONL 和 SQLite 怎么选？**
A：<1000 实体用 JSONL（简单无依赖）；>10000 实体或频繁复杂查询用 SQLite（性能优）。中间区间看查询模式，简单查询 JSONL 够用。

**Q2：append-only 会不会文件越来越大？**
A：会，但历史完整可追溯。定期 compact 可合并旧 op（保留最终状态），但会丢失历史。建议保留 append-only，用索引加速查询。

**Q3：约束校验会不会拖慢写入？**
A：单次校验是毫秒级。批量写入时先校验全部再提交。校验失败的代价远低于脏数据清理。

**Q4：模式演进如何不破坏旧数据？**
A：三步法——追加新 schema（不删旧）→ 写迁移脚本补默认值 → 执行+校验。详见"模式演进管理"章节。

**Q5：多 Skill 同时写图谱会冲突吗？**
A：会。建议每个 Skill 声明契约（读写边界），通过文件锁或队列串行化写入。复杂场景迁移到 SQLite 利用事务。

## 故障排查

| 现象 | 排查步骤 | 解决方案 |
|:---|:---|:---|
| 校验失败 | `validate` 查看具体错误 | 按提示修复属性/关系 |
| 查询无结果 | 确认实体存在 | `list --type X` 检查 |
| 关系创建失败 | 检查类型约束 | 确认 from/to 类型匹配关系定义 |
| 循环依赖报错 | `cycle-check` 定位环 | 打破环中一条边 |
| 文件过大 | 检查实体数量 | 迁移到 SQLite；或 compact 合并 |
| 迁移失败 | 检查迁移脚本语法 | 逐步调试；校验迁移前后数据 |

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（运行 ontology.py 脚本）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---|:---|:---|:---|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Python 3.8+ | 运行时 | 必需 | 系统安装 |
| SQLite | 数据库 | 可选 | Python 内置（大规模时使用） |
| PyYAML | Python 包 | 必需 | `pip install pyyaml`（解析 schema.yaml） |

### API Key 配置
- **本 Skill 无需任何 API Key**
- 纯本地文件操作，无网络请求
- 凭证等敏感信息强制间接引用，不存储在图谱中

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令 + exec 命令行执行）
- **说明**：基于 Markdown 的 AI Skill 驱动 Agent 执行知识图谱管理。核心实体/关系概念纯 Markdown 可理解；创建/查询/校验等操作需 Python 脚本执行。
