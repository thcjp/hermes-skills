---
slug: "linear-api"
name: "linear-api"
version: "1.0.0"
displayName: "项目管理API"
summary: "通过GraphQL操作工作项、项目、周期、标签与评论,覆盖创建查询转换全流程。"
license: "Proprietary"
description: |-
  通过项目管理工具的GraphQL API操作工作项全生命周期:工作项CRUD、
  项目管理、团队管理、周期管理、标签管理、评论与关联。覆盖GraphQL
  查询构造、工作流状态转换与自定义视图。适用于独立开发者、企业团队
  和自动化工作流场景。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tags:
  - 研发工具
---
# 项目管理API集成

通过项目管理工具的 GraphQL API 操作工作项全生命周期,从创建到状态推进,覆盖项目、周期、标签、评论与关联管理。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 工作项管理
- `createIssue` 创建工作项:含 title、description、teamId、priority
- `updateIssue` 更新工作项:状态、指派、估算、标签
- `archiveIssue` 归档工作项,保留历史但不显示在默认视图
- 工作项字段:title、description、priority、estimate、assignee、labels、state、project、cycle
- 优先级数值:0=紧急、1=高、2=中、3=低、4=无(对应 priorityUrgent 到 priorityNone)

**输入**: 用户提供工作项管理所需的指令和必要参数。
**处理**: 按照skill规范执行工作项管理操作,遵循单一意图原则。

### 2. 项目管理
- `createProject` 创建项目:含 name、description、teamIds
- `updateProject` 更新项目状态:planned、started、paused、completed、canceled
- `projectIssues` 查询项目下所有工作项
- 项目作为跨周期的工作容器,工作项可关联到项目

**输入**: 用户提供项目管理所需的指令和必要参数。
**处理**: 按照skill规范执行项目管理操作,遵循单一意图原则。

### 3. 团队管理
- `teams` 查询所有团队:含 id、name、key
- `team` 查询单个团队详情:含 workflow、states、labels
- 工作项必须归属于一个团队,teamId 是创建工作项的必填字段
- 团队 key 作为工作项标识前缀(如 ENG-123)

**输入**: 用户提供团队管理所需的指令和必要参数。
**处理**: 按照skill规范执行团队管理操作,遵循单一意图原则。

### 4. 周期管理
- `createCycle` 创建周期:含 name、startsAt、endsAt、teamId
- 标准周期14天,可自定义
- `cycleIssues` 查询周期内工作项
- 周期状态:active、upcoming、past,过去周期不可添加工作项
- `updateIssue` 的 cycleId 字段将工作项加入周期

**输入**: 用户提供周期管理所需的指令和必要参数。
**处理**: 按照skill规范执行周期管理操作,遵循单一意图原则。

### 5. 标签管理
- `createLabel` 创建标签:含 name、color、teamId
- `updateIssue` 的 labelIds 字段为工作项添加标签
- 标签用于分类筛选:bug、feature、tech-debt、customer-request
- 标签颜色用十六进制(如 `#E5484D` 表示红色)

**处理**: 按照skill规范执行标签管理操作,遵循单一意图原则。
### 6. 评论管理
- `createComment` 创建评论:含 body、issueId
- `updateComment` 编辑评论,`deleteComment` 删除评论
- 评论支持 Markdown 格式
- `issueComments` 查询工作项所有评论

**输入**: 用户提供评论管理所需的指令和必要参数。
**处理**: 按照skill规范执行评论管理操作,遵循单一意图原则。

### 7. 工作项关联
- `issueRelation` 建立关联:type=blocks、is blocked by、relates to、duplicate
- 关联方向有向:blocks 表示 A 阻塞 B
- `issueRelations` 查询工作项的所有关联

**输入**: 用户提供工作项关联所需的指令和必要参数。
**处理**: 按照skill规范执行工作项关联操作,遵循单一意图原则。
**输出**: 返回工作项关联的执行结果,包含操作状态和输出数据。

### 8. 工作流状态
- `teamWorkflow` 查询团队工作流:含 states 与 transitions
- 默认状态:Backlog、Triage、Todo、In Progress、In Review、Done、Canceled
- `updateIssue` 的 stateId 字段转换状态
- 状态类型:backlog、unstarted、started、completed、canceled

**输入**: 用户提供工作流状态所需的指令和必要参数。
**输出**: 返回工作流状态的执行结果,包含操作状态和输出数据。

### 9. 自定义视图
- `createView` 创建视图:含 name、query、filters
- 视图查询语法:`status = "In Progress" AND priority = 1`
- `views` 查询所有视图,`viewIssues` 获取视图内工作项

**输入**: 用户提供自定义视图所需的指令和必要参数。
**处理**: 按照skill规范执行自定义视图操作,遵循单一意图原则。

### 10. GraphQL查询构造
- 查询用 `query` 关键字,变更用 `mutation`
- 字段选择:只查询需要的字段,减少响应体积
- 分页:用 `first`、`after` 参数,默认 first 50
- 变量:用 `$variable` 参数化,避免字符串拼接

**处理**: 按照skill规范执行GraphQL查询构造操作,遵循单一意图原则。
**输出**: 返回GraphQL查询构造的执行结果,包含操作状态和输出数据。

#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 创建工作项 | title+teamId+priority | 工作项对象(含 id、identifier) |
| 周期规划 | 工作项列表+周期名 | 周期 ID + 工作项更新结果 |
| GraphQL查询 | 查询语句 | 匹配工作项列表(first 50) |
| 状态转换 | issueId + stateId | 更新后工作项状态 |
| 项目进度 | projectId | 项目工作项完成率 |

不适用于:项目管理工具配置(工作流设计、团队设置)、SSO配置、账单管理。

## 使用流程

1. 确认 API Key 配置,获取团队 ID 与工作流状态 ID
2. 用 `createIssue` 创建工作项,填 title、teamId、priority
3. 用 `updateIssue` 关联项目、周期、标签
4. 用 `createCycle` 规划周期,将工作项加入
5. 用 GraphQL `query` 配合筛选跟踪进度
6. 用 `updateIssue` 的 stateId 推进工作流状态

#
## 示例

### 示例1:创建工作项(GraphQL mutation)
```graphql
mutation {
  issueCreate(input: {
    title: "实现用户登录接口"
    description: "支持邮箱+密码登录,返回JWT"
    teamId: "team-uuid-123"
    priority: 1
    estimate: 5
    labelIds: ["label-uuid-feature"]
  }) {
    success
    issue {
      id
      identifier
      title
      state { name }
    }
  }
}
// 返回: {"success": true, "issue": {"id": "issue-uuid-456", "identifier": "ENG-101", "title": "实现用户登录接口", "state": {"name": "Triage"}}}
```

### 示例2:GraphQL查询工作项
```graphql
query {
  team(id: "team-uuid-123") {
    issues(first: 50, filter: {
      state: { type: { eq: "started" } }
      priority: { lte: 1 }
    }) {
      nodes {
        identifier
        title
        priority
        estimate
        assignee { name }
        state { name }
      }
    }
  }
}
```

### 示例3:周期规划
```graphql
mutation {
  cycleCreate(input: {
    name: "Cycle 2026-W30"
    startsAt: "2026-07-21"
    endsAt: "2026-08-04"
    teamId: "team-uuid-123"
  }) {
    success
    cycle { id number }
  }
}
// 返回: {"success": true, "cycle": {"id": "cycle-uuid-789", "number": 30}}

// 将工作项加入周期
mutation {
  issueUpdate(input: {
    id: "issue-uuid-456"
    cycleId: "cycle-uuid-789"
  }) { success }
}
```

### 示例4:状态转换
```graphql
mutation {
  issueUpdate(input: {
    id: "issue-uuid-456"
    stateId: "state-uuid-in-progress"
  }) {
    success
    issue { state { name type } }
  }
}
// 返回: {"success": true, "issue": {"state": {"name": "In Progress", "type": "started"}}}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| API Key 无效(401 Unauthorized) | key 过期或权限不足 | 重新生成 API Key,确认 key 对目标团队有读写权限 |
| GraphQL 语法错误(400 Bad Request) | 字段名拼写错误或类型不匹配 | 检查 mutation/query 结构,确认字段名与枚举值合法 |
| teamId 不存在(404 Not Found) | 团队 ID 拼写错误或已删除 | 用 `query { teams { id name key } }` 验证 teamId |
| 周期已关闭无法添加工作项 | 周期状态为 past | 创建新周期或将工作项移到下个 upcoming 周期 |
| 优先级值越界 | priority 取值非 0-4 | 确认 priority 为整数 0-4,0=紧急、4=无;不要传字符串 |
| 自定义字段 ID 错误 | 不同团队字段配置不同 | 用 `query { team(id: ...) { workflow { states } } }` 反查 stateId |
| 关联循环引用 | A blocks B 且 B blocks A | 检查关联方向,blocks 与 is blocked by 不可同时存在形成环 |

## 常见问题

### Q1: 优先级数值 0-4 如何映射?
A: 0=priorityUrgent(紧急)、1=priorityHigh(高)、2=priorityMedium(中)、3=priorityLow(低)、4=priorityNone(无)。创建工作项时传整数,查询时返回对应枚举标签。

### Q2: GraphQL 查询默认返回多少条?
A: 默认 `first: 50`。需要更多时显式传 `first: 100`(上限250),并用 `after` 游标分页:`issues(first: 50, after: "cursor-xyz")`。

### Q3: estimate 估算值用哪些数字?
A: 与故事点一致,用斐波那契数列:1、2、3、5、8、13。也可配置为任意整数,但建议团队统一数列便于速率对比。

### Q4: `updateIssue` 的 stateId 与 state name 有何区别?
A: stateId 是状态的唯一标识(如 `state-uuid-123`),state name 是显示名(如 "In Progress")。`updateIssue` 必须用 stateId,不能用 name。用 `teamWorkflow` 查询获取所有 stateId。

### Q5: `issueRelation` 的 blocks 与 is blocked by 有何区别?
A: 方向相反。A blocks B 表示 A 阻塞 B(B 等 A 完成);A is blocked by B 表示 A 被 B 阻塞(A 等 B 完成)。建立关联时需明确方向,否则依赖图会反,且不可形成循环。

### Q6: 周期14天如何调整?
A: `createCycle` 时指定 `startsAt` 与 `endsAt`,可设为7天或30天。建议团队统一周期长度,避免不同周期影响速率(burndown)对比。过去周期不可修改,只能创建新周期。

## 已知限制

- 需要项目管理工具的 API Key 与团队访问权限
- GraphQL 查询受 first 上限(250)限制,大结果集需分页
- 工作流状态 ID 因团队而异,不可硬编码
- 过去周期不可添加工作项,只能移到当前或未来周期
- 不覆盖工作流设计、SSO配置与账单管理
