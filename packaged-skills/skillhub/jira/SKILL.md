---
slug: jira
name: jira
version: "1.0.0"
displayName: 项目管理工具
summary: 通过工具操作史诗、故事、缺陷、冲刺与看板,覆盖创建搜索转换全流程。
license: MIT
description: |-
  通过项目管理工具集成操作工作项全生命周期:史诗、故事、缺陷、
  子任务、冲刺、看板、关联、状态转换与用户管理。覆盖JQL高级搜索、
  工作流转换与字段配置。适用于独立开发者、企业团队和自动化工作流场景。
tools:
  - read
  - exec
---

# 项目管理工具集成

通过项目管理工具集成操作工作项的全生命周期,从史诗拆分到冲刺执行,覆盖创建、搜索、状态转换与看板管理。

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

### 1. 史诗管理
- `create_issue` 创建史诗:type=Epic,含 summary、description
- `link_issues` 将故事关联到史诗:link type=Epic-Story
- `update_issue` 更新史诗状态与字段
- 史诗作为大粒度工作容器,拆分为多个故事追踪

**输入**: 用户提供史诗管理所需的指令和必要参数。
**处理**: 按照skill规范执行史诗管理操作,遵循单一意图原则。

### 2. 故事管理
- `create_issue` 创建故事:type=Story,含 summary、description、priority、assignee
- 故事字段:Story Points(1/2/3/5/8/13)、Sprint、Epic Link
- `get_issue` 读取故事详情,含评论、附件、子任务
- 故事可拆分为子任务,子任务完成度反映故事进度

**输入**: 用户提供故事管理所需的指令和必要参数。
**处理**: 按照skill规范执行故事管理操作,遵循单一意图原则。

### 3. 缺陷管理
- `create_issue` 创建缺陷:type=Bug,含 priority、environment、steps to reproduce
- 缺陷优先级:Highest、High、Medium、Low、Lowest
- `link_issues` 关联缺陷到故事或史诗:link type=Blocks/Is Blocked By
- 缺陷字段:Affected Version、Fix Version、Resolution

**输入**: 用户提供缺陷管理所需的指令和必要参数。
**处理**: 按照skill规范执行缺陷管理操作,遵循单一意图原则。

### 4. 子任务管理
- `create_issue` 创建子任务:type=Subtask,parent=父故事key
- 子任务继承父任务的字段默认值
- 子任务状态转换独立于父任务,但父任务状态由子任务聚合

### 5. 冲刺管理
- `create_sprint` 创建冲刺:name、startDate、endDate、goal
- 标准冲刺周期30天,可配置为14天或7天
- `add_to_sprint` 将工作项加入冲刺
- `get_sprint_issues` 获取冲刺内所有工作项,`maxResults: 50` 默认返回前50条
- 冲刺状态:Future、Active、Closed,关闭后无法添加工作项

**输入**: 用户提供冲刺管理所需的指令和必要参数。
**处理**: 按照skill规范执行冲刺管理操作,遵循单一意图原则。

### 6. 看板管理
- `get_board_issues` 获取看板工作项,按状态列分组
- 看板列映射工作流状态:To Do、In Progress、In Review、Done
- `move_issue_in_board` 调整工作项在看板中的顺序

**输入**: 用户提供看板管理所需的指令和必要参数。
**处理**: 按照skill规范执行看板管理操作,遵循单一意图原则。
**输出**: 返回看板管理的执行结果,包含操作状态和输出数据。

### 7. JQL高级搜索
- `search_issues` 使用 JQL 查询:`jql="project = PROJ AND status = Open ORDER BY priority DESC"`
- 常用 JQL 操作符:`=、!=、>、<、IN、NOT IN、AND、OR`
- 函数搜索:`assignee = currentUser()`、`sprint in openSprints()`
- `maxResults: 50` 控制返回数量,大结果集需分页

### 8. 工作项关联
- `link_issues` 建立关联:type=Blocks、Is Blocked By、Relates To、Duplicate、Epic-Story
- 关联方向有向:Blocks 表示 A 阻塞 B,Is Blocked By 表示 A 被 B 阻塞
- 关联用于依赖管理、缺陷溯源、史诗聚合

**输入**: 用户提供工作项关联所需的指令和必要参数。
**处理**: 按照skill规范执行工作项关联操作,遵循单一意图原则。
**输出**: 返回工作项关联的执行结果,包含操作状态和输出数据。

### 9. 状态转换
- `transition_issue` 转换工作项状态:issue_key + transition_id
- 工作流状态:Open → In Progress → In Review → Done
- 转换需符合工作流定义,非法转换被拒绝
- 转换可触发事件:自动指派、发送通知、更新字段

### 10. 用户与项目管理
- `get_user` 查询用户信息:username、displayName、email
- `get_project` 查询项目信息:key、name、lead、issue types
- `get_all_projects` 列出所有可访问项目

**处理**: 按照skill规范执行用户与项目管理操作,遵循单一意图原则。
**输出**: 返回用户与项目管理的执行结果,包含操作状态和输出数据。

### 输出格式

执行结果以Markdown格式返回,包含操作状态(成功/失败)、处理摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。

- 执行`输出格式`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`输出格式`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 通过工具操作史诗、冲刺与看板、覆盖创建搜索转换、全流程、通过项目管理工具、集成操作工作项全、生命周期、状态转换与用户管、工作流转换与字段、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 创建史诗 | 标题+描述 | Epic 工作项 key(如 PROJ-123) |
| 冲刺规划 | 工作项列表+冲刺名 | 冲刺 ID + 工作项加入结果 |
| JQL搜索 | JQL语句 | 匹配工作项列表(maxResults 50) |
| 状态转换 | issue_key + 目标状态 | 转换结果 + 更新后状态 |
| 依赖分析 | 工作项key | Blocks/Is Blocked By 关联图 |

不适用于:项目管理工具配置(工作流设计、字段schema)、报表仪表盘搭建、跨实例迁移。

## 使用流程

1. 确认项目管理工具实例 URL 与 API token 配置
2. 用 `get_project` 确认目标项目 key 与可用 issue type
3. 用 `create_issue` 创建工作项,填 summary、type、priority
4. 用 `link_issues` 建立史诗-故事-子任务层级与依赖关系
5. 用 `create_sprint` + `add_to_sprint` 规划冲刺
6. 用 `search_issues` 配合 JQL 跟踪进度
7. 用 `transition_issue` 推进工作流状态

## 示例

### 示例1:创建史诗与故事
```json
// 创建史诗
{
  "fields": {
    "project": {"key": "PROJ"},
    "summary": "用户认证模块",
    "issuetype": {"name": "Epic"},
    "priority": {"name": "High"}
  }
}
// 返回: {"key": "PROJ-100"}

// 创建故事并关联史诗
{
  "fields": {
    "project": {"key": "PROJ"},
    "summary": "实现JWT登录接口",
    "issuetype": {"name": "Story"},
    "priority": {"name": "Medium"},
    "customfield_10001": "PROJ-100"  // Epic Link
  }
}
// 返回: {"key": "PROJ-101"}
```

### 示例2:JQL搜索
```
输入: "查找 PROJ 项目中所有未关闭的高优先级缺陷"
JQL: project = PROJ AND issuetype = Bug AND priority in (Highest, High) AND status != Closed ORDER BY created DESC
maxResults: 50
输出: 匹配的缺陷列表,含 key、summary、status、assignee
```

### 示例3:冲刺规划
```json
// 创建冲刺
{
  "name": "Sprint 2026-W30",
  "startDate": "2026-07-21",
  "endDate": "2026-08-04",
  "goal": "完成用户认证与权限管理"
}
// 返回: {"id": 42, "state": "Future"}

// 将故事加入冲刺
add_to_sprint(sprintId=42, issues=["PROJ-101", "PROJ-102", "PROJ-103"])
```

### 示例4:状态转换
```json
// 转换 PROJ-101 从 Open 到 In Progress
transition_issue("PROJ-101", "11")  // 11 = In Progress 的 transition_id
// 返回: {"status": "In Progress", "assignee": "张三"}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| API token 无效(401 Unauthorized) | token 过期或权限不足 | 重新生成 API token,确认用户对目标项目有读写权限 |
| Issue key 不存在(404 Not Found) | key 拼写错误或已删除 | 用 `search_issues` 验证 key 是否存在,检查拼写 |
| 工作流转换被拒(过渡非法) | 当前状态不允许直接转到目标状态 | 查询工作流定义,确认合法转换路径,如 Open 不能直接到 Done |
| 自定义字段 customfield ID 错误 | 不同实例字段 ID 不同 | 用 `get_issue` 读取已有工作项,反查 Epic Link 等字段的 customfield ID |
| 冲刺已关闭无法添加工作项 | 冲刺状态为 Closed | 创建新冲刺或激活已关闭冲刺(需管理员权限) |
| JQL 语法错误(400 Bad Request) | 操作符或函数拼写错误 | 检查 JQL 语法,确认字段名与操作符合法,用 `IN` 替代多个 `OR` |
| 超出 maxResults 限制 | 默认50条不够 | 分页查询,用 `startAt` 参数偏移,或缩小 JQL 范围 |

## 常见问题

### Q1: Story Points 为何用 1/2/3/5/8/13 而非连续值?
A: 斐波那契数列避免虚假精度。3 与 4 的差异难以区分,但 3 与 5 的差异明确。这迫使团队做粗粒度估算,避免陷入精确错误的陷阱。

### Q2: `maxResults: 50` 不够时如何获取全部结果?
A: 用分页:第一次 `startAt=0, maxResults=50`,第二次 `startAt=50, maxResults=50`,依此类推。或缩小 JQL 范围,按时间或状态分段查询。

### Q3: 工作流转换的 transition_id 如何获取?
A: 用 `get_issue` 读取工作项,响应中的 `transitions` 字段列出所有可用转换及其 ID。不同项目、不同状态的 transition_id 不同,不能硬编码。

### Q4: Epic Link 字段的 customfield ID 为何每个实例不同?
A: 自定义字段 ID 在创建实例时自动生成,不同实例的 Epic Link 可能是 `customfield_10001` 或 `customfield_10014`。用 `get_issue` 读取含史诗关联的工作项,反查实际字段 ID。

### Q5: `link_issues` 的 Blocks 与 Is Blocked By 有何区别?
A: 方向相反。A Blocks B 表示 A 阻塞 B(B 等 A 完成);A Is Blocked By B 表示 A 被 B 阻塞(A 等 B 完成)。建立关联时需明确方向,否则依赖图会反。

### Q6: 冲刺30天周期如何调整?
A: `create_sprint` 时指定 `startDate` 与 `endDate`,可设为14天或7天。建议团队统一周期,避免不同冲刺长度影响速率(burndown)对比。

## 已知限制

- 需要项目管理工具实例的访问权限与 API token
- 自定义字段 ID 因实例而异,不可硬编码
- 工作流转换需符合工作流定义,无法跳过中间状态
- 大量工作项查询受 maxResults 限制,需分页
- 不覆盖工作流设计、字段schema配置与报表搭建
