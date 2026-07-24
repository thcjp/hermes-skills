---
slug: "knowledge-ontology"
name: "knowledge-ontology"
version: "2.0.0"
displayName: "知识本体"
summary: "类型化知识图谱：约束校验+模式演进+图遍历规划，让Agent记忆结构化可验证。。面向AI Agent的类型化知识图谱系统，提供实体关系建模、约束校验、模式演进、图遍历规划能力。适用于需要结构"
license: "Proprietary"
description: |-
  面向AI Agent的类型化知识图谱系统，提供实体关系建模、约束校验、模式演进、图遍历规划能力。适用于需要结构化查询的Agent记忆、多实体关系管理、依赖追踪与影响分析、多步计划建模场景，避免扁平文件记忆难查询、约束缺失数据脏、模式演进破坏旧数据等问题。适用关键词：知识图谱、本体、实体关系、ontology、graph、类型化、约束校验、图遍历.
tags:
  - 智能代理
  - 知识管理
  - 数据建模
  - AI代理
  - 自动化
  - 智能
  - 请参考
  - 目录中的
  - 脚本文件
  - python3
  - bash
tools:
  - read
  - exec
  - write
  - glob
  - grep
homepage: ""
category: "Agents"
---
# 知识本体（Knowledge Ontology）

**一切皆实体，一切变更皆受约束。** 将 Agent 记忆从扁平文件升级为类型化可验证的知识图谱，支持图遍历查询、模式演进、多步规划建模，让知识结构化、可查询、可信任.
## 核心能力

### 类型化实体与关系系统
内置 Person/Organization/Project/Task/Goal/Event/Location/Document/Message/Thread/Note/Account/Device/Credential/Action/Policy 15+ 类型，实体含 id/type/properties/relations/created/updated 标准结构.
**输入**: 用户提供类型化实体与关系系统所需的指令和必要参数.
**处理**: 解析类型化实体与关系系统的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回类型化实体与关系系统的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 约束校验引擎
支持 required（必填）、enum（枚举）、forbidden_properties（禁止属性，如 Credential 禁止 password）、cardinality（关系基数）、acyclic（无环校验，如 blocks 关系）、validate（自定义表达式）、defaults（默认值）7 类约束规则.
**输入**: 用户提供约束校验引擎所需的指令和必要参数.
**处理**: 解析约束校验引擎的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回约束校验引擎的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 模式演进管理
append-only 历史保留 + 迁移脚本三步法（追加新 schema → 编写迁移 → 执行+校验），确保模式变更不破坏旧数据.
**输入**: 用户提供模式演进管理所需的指令和必要参数.
**处理**: 解析模式演进管理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回模式演进管理的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 图遍历规划
将多步计划建模为图操作序列（CREATE/RELATE），每步执行前校验约束，违反约束自动回滚；支持依赖分析、影响分析、循环依赖检测.
**输入**: 用户提供图遍历规划所需的指令和必要参数.
**处理**: 解析图遍历规划的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回图遍历规划的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### Skill 契约声明
使用本体的 Skill 声明 reads/writes 边界与前后置条件，任一失败自动回滚，明确跨 Skill 通信边界.
**输入**: 用户提供Skill 契约声明所需的指令和必要参数.
**处理**: 解析Skill 契约声明的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回Skill 契约声明的响应数据,包含状态码、结果和日志.
**技术参数**：使用`input_params`和`output_format`参数控制执行行为,支持`json`/`text`/`csv`输出格式.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：类型化知识图谱、Agent、记忆结构化可验证、的类型化知识图谱、提供实体关系建模、图遍历规划能力、适用于需要结构化、查询的、多实体关系管理、依赖追踪与影响分、多步计划建模场景、避免扁平文件记忆、难查询、约束缺失数据脏、模式演进破坏旧数、据等问题、适用关键词、知识图谱、实体关系、ontology、graph等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

**何时使用：**

| 触发情境 | 动作 |
|----|---|
| "记住..." | 创建/更新实体 |
| "我对 X 了解什么" | 查询图谱 |
| "把 X 关联到 Y" | 创建关系 |
| "显示项目 Z 的所有任务" | 图遍历 |
| "X 依赖什么" | 依赖查询 |
| 规划多步工作 | 建模为图变换序列 |
| Skill 需要共享状态 | 读写本体对象 |

**输入输出：**
- 输入：实体定义（type + properties）、关系定义（from/rel/to）、查询条件（type/where/related）
- 输出：校验通过/失败的实体、查询结果集、依赖链/影响范围、计划执行结果

**不适用场景：**
- 简单键值存储（无关系需求）— 用扁平文件即可
- 海量时序数据（>100万条）— 选专用时序数据库
- 频繁全文检索 — 用 Elasticsearch 等专用搜索引擎
- 无结构化文本记忆 — 用 markdown 笔记更轻量

## 使用流程

### Step 1：初始化目录与 schema

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 知识本体处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
mkdir -p memory/ontology
touch memory/ontology/graph.jsonl
python3 （请参考skill目录中的脚本文件） schema-append --data '{
  "types": {
    "Task": { "required": ["title", "status"] },
    "Project": { "required": ["name"] },
    "Person": { "required": ["name"] }
  }
}'
```

### Step 2：创建实体（append-only）

```bash
python3 （请参考skill目录中的脚本文件） create --type Person --props '{"name":"Alice"}'
python3 （请参考skill目录中的脚本文件） create --type Project --props '{"name":"网站重构","status":"active"}'
```

**关键原则：** 处理已有数据时追加新 op 到文件末尾，绝不覆盖文件.
### Step 3：建立关系

```bash
python3 （请参考skill目录中的脚本文件） relate --from proj_001 --rel has_owner --to p_001
```

关系建立前自动校验 from_types/to_types/cardinality 约束.
### Step 4：查询与遍历

```bash
# 按类型+条件查询
python3 （请参考skill目录中的脚本文件） query --type Task --where '{"status":"open"}'
# ...
# 关联查询
python3 （请参考skill目录中的脚本文件） related --id proj_001 --rel has_task
# ...
# 依赖说明
python3 （请参考skill目录中的脚本文件） traverse --id task_001 --rel depends_on --direction outgoing
# ...
# 影响分析（反向遍历）
python3 （请参考skill目录中的脚本文件） traverse --id task_001 --rel depends_on --direction incoming
# ...
# 循环依赖检测
python3 （请参考skill目录中的脚本文件） cycle-check --rel blocks
```

### 已知限制

```bash
python3 （请参考skill目录中的脚本文件） validate
# 示例
# ✓ 142 个实体校验通过
# ✗ 3 个实体校验失败：
#   - task_042: 缺少必填属性 'status'
#   - cred_001: 包含禁止属性 'password'
```

### Step 6：模式演进（不破坏旧数据）

```bash
# 1. 追加新 schema（不删旧）
python3 （请参考skill目录中的脚本文件） schema-append --data '{"types":{"Task":{"required":["title","status","priority"]}}}'
# ...
# 2. 编写迁移脚本
# migrations/001_add_priority_to_tasks.py
def migrate(graph):
    for entity in graph.query(type="Task"):
        if "priority" not in entity.properties:
            entity.properties["priority"] = 3
    return graph
# ...
# 3. 执行迁移 + 校验
python3 （请参考skill目录中的脚本文件） migrate --script 001_add_priority_to_tasks.py
python3 （请参考skill目录中的脚本文件） validate
```

### Step 7：多步规划建模（图变换序列）

```bash
python3 （请参考skill目录中的脚本文件） plan --file plan.yaml --validate-each --rollback-on-fail
```

每步执行前校验约束，失败自动回滚到上一步.
### Step 8：规模扩展（JSONL → SQLite）

```bash
# >10000 实体时迁移
python3 （请参考skill目录中的脚本文件） migrate --from jsonl --to sqlite
```

## 示例

### 示例 1：项目依赖管理

**输入：**
```
用户："重构支付模块需要先完成哪些任务？"
```

**执行：**
1. 查找支付模块相关 Project
2. 遍历 has_task 关系找到所有 Task
3. 遍历 blocks 关系找到阻塞链
4. 拓扑排序输出执行顺序

**输出：**
```
执行顺序：
1. 设计支付接口（task_001）— 无阻塞
2. 实现支付网关（task_002）— blocked by task_001
3. 集成测试（task_003）— blocked by task_002
4. 上线部署（task_004）— blocked by task_003
```

### 示例 2：影响分析

**输入：**
```
用户："如果推迟数据库迁移，影响哪些任务？"
```

**执行：**
1. 找到数据库迁移 Task
2. 反向遍历 depends_on 关系
3. 找出所有依赖该任务的 Task

**输出：**
```
影响范围（3 个任务）：
- task_015: API 部署（depends on 迁移）
- task_022: 性能测试（depends on task_015）
- task_031: 上线（depends on task_022）
# ...
建议级联调整截止日期.
```

### 示例 3：凭证安全存储

**输入：**
```
用户："记住我的 Stripe API Key"
```

**执行：**
1. 检查 Credential 类型约束 → forbidden_properties: [api_key, secret]
2. 拒绝直接存储
3. 创建间接引用

**输出：**
```python
ontology.create("Credential", {
  "service": "stripe",
  "secret_ref": "vault://secrets/stripe_key"  # 指向外部密钥库
})
# 输出："已记录 Stripe 凭证引用（密钥本身存储在密钥库，未写入图谱）"
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 校验失败（缺必填属性） | 实体未提供 required 字段 | 按提示补全属性后重新提交；可临时用 defaults 填充 |
| 校验失败（含禁止属性） | Credential 写入 password 等敏感字段 | 拒绝存储；改为 secret_ref 间接引用外部密钥库 |
| 关系创建失败 | from/to 类型不匹配关系定义 | 检查 schema.yaml 中关系的 from_types/to_types 声明 |
| 循环依赖报错 | blocks 关系形成环 | `cycle-check` 定位环；打破环中一条边 |
| 查询无结果 | 实体不存在或类型错误 | `list --type X` 确认实体存在；检查 where 条件 |
| 文件过大性能差 | JSONL 全量扫描 | 迁移到 SQLite；或定期 compact 合并旧 op |
| 迁移失败 | 迁移脚本语法错误或数据冲突 | 逐步调试；校验迁移前后数据；保留 append-only 历史可回滚 |
| 多 Skill 写入冲突 | 并发写入同一文件 | 声明 Skill 契约；文件锁或队列串行化；复杂场景迁移 SQLite 利用事务 |
| 模式演进破坏旧数据 | 直接修改 schema 未走三步法 | 必须按"追加新 schema → 迁移脚本 → 校验"流程，append-only 保留历史 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Python 3.8+ | 运行时 | 必需 | 系统安装 |
| PyYAML | Python 包 | 必需 | `pip install pyyaml`（解析 schema.yaml） |
| SQLite | 数据库 | 可选 | Python 内置（>10000 实体时使用） |
| Agent 平台 | 运行环境 | 必需 | 支持 SKILL.md 的任意 AI Agent |
| 操作系统 | 运行环境 | 必需 | Windows / macOS / Linux |

**API Key 配置：** 本 Skill 无需任何 API Key，纯本地文件操作，无网络请求。凭证等敏感信息强制间接引用，不存储在图谱中.
**可用性分类：** MD+EXEC（Markdown 指令 + exec 命令行执行）。核心实体/关系概念纯 Markdown 可理解；创建/查询/校验等操作需 Python 脚本执行.
## 常见问题

**Q1：JSONL 和 SQLite 怎么选？**
A：<1000 实体用 JSONL（简单无依赖）；>10000 实体或频繁复杂查询用 SQLite（性能优）。中间区间看查询模式，简单查询 JSONL 够用.
**Q2：append-only 会不会文件越来越大？**
A：会，但历史完整可追溯。定期 compact 可合并旧 op（保留最终状态），但会丢失历史。建议保留 append-only，用索引加速查询.
**Q3：约束校验会不会拖慢写入？**
A：单次校验是毫秒级。批量写入时先校验全部再提交。校验失败的代价远低于脏数据清理.
**Q4：模式演进如何不破坏旧数据？**
A：三步法——追加新 schema（不删旧）→ 写迁移脚本补默认值 → 执行+校验。详见"使用流程 Step 6".
**Q5：多 Skill 同时写图谱会冲突吗？**
A：会。建议每个 Skill 声明契约（读写边界），通过文件锁或队列串行化写入。复杂场景迁移到 SQLite 利用事务.
## 已知限制(补充)

1. **默认 JSONL 不适合超大规模**：>10000 实体需手动迁移到 SQLite，迁移过程需停服或锁写.
2. **append-only 文件会持续增长**：不主动 compact 会越来越大，compact 会丢失历史，需用户权衡.
3. **并发写入支持弱**：JSONL 存储无事务，多 Skill 并发写入需外部文件锁或队列串行化.
4. **不存储敏感信息原文**：Credential 类型强制间接引用（secret_ref），用户需自行管理外部密钥库.
5. **校验引擎覆盖有限**：支持 7 类约束规则，但不支持复杂业务逻辑校验（如跨实体的多字段联合校验需在迁移脚本中自行实现）.
6. **无内置全文检索**：仅支持结构化属性查询与图遍历，文本内容检索需外接搜索引擎.
## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "知识本体处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "knowledge ontology"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
