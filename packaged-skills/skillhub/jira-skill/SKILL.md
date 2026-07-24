---
slug: "jira-skill"
name: "jira-skill"
version: "1.0.0"
displayName: "Jira集成助手"
summary: "通过Jira Cloud REST API管理事务、状态流转与工时日志，支持搜索、创建、指派、评论、工时统计。"
license: "Proprietary"
description: |-
  Jira集成助手通过Jira Cloud REST API管理事务、状态流转与工时日志.
  支持模糊搜索、详情查看、状态变更、指派、评论、创建、工时记录与多维度工时统计.
  核心能力：
  - 事务搜索：按summary或key模糊搜索，支持maxResults限制
  - 事务详情与浏览器链接：快速查看与跳转
  - 状态流转：transitions列出可用流转，status变更前校验
  - 指派：按姓名/邮箱搜索用户并指派，assign-me指派给自己
  - 评论与创建：添加评论、在JIRA_BOARD创建Task
  - 工时记录：log按小时记录，支持指定日期（默认今日UTC）
  - 工时统计：hours（按事务）/ hours-day（按日全员）/ hours-issue（按事务+用户过滤）
  - 工时命令输出JSON，便于其他工具复用
  适用场景：第三方API集成、平台对接、数据同步、独立开发者与一人公司效率提升、自动化工作流.
tags:
  - 通用办公
  - Productivity
  - Jira
  - 工具
  - 效率
  - 自动化
  - 开发
  - 代码
  - 知识
  - 文档
  - 研究
  - 请参考
  - 目录中的
  - 脚本文件
  - basedir
  - jira
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"
---
# Jira集成助手

通过Jira Cloud REST API管理事务、状态流转与工时日志。支持搜索、详情、状态变更、指派、评论、创建、工时记录与多维度工时统计.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Jira集成助手处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| Jira集成助手API管理 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 环境配置

1. 获取API Token: <https://id.atlassian.com/manage-profile/security/api-tokens>
2. 点击"Create API Token"
3. 设置环境变量：

   ```bash
   export JIRA_EMAIL="you@example.com"
   export JIRA_API_TOKEN="[REDACTED]"
   export JIRA_URL="https://your-domain.atlassian.net"
   # 可选项目范围（逗号分隔）。空=搜索全部.
   export JIRA_BOARD="ABC"
   ```

依赖：`curl`、`jq`、`bc`、`python3`.
## 快速命令

所有命令位于 `{baseDir}/（请参考skill目录中的脚本文件）`.
| 命令 | 用途 |
|---:|---:|
| `jira.sh search "关键词" [max]` | 在 `JIRA_BOARD` 内按summary或key模糊搜索 |
| `jira.sh link ABC-123` | 生成事务浏览器链接 |
| `jira.sh issue ABC-123` | 快速查看事务详情 |
| `jira.sh status ABC-123 "In Progress"` | 变更状态（校验可用流转） |
| `jira.sh transitions ABC-123` | 列出允许的流转 |
| `jira.sh assign ABC-123 "name or email"` | 按用户搜索后指派 |
| `jira.sh assign-me ABC-123` | 指派给自己 |
| `jira.sh comment ABC-123 "text"` | 添加评论 |
| `jira.sh create "Title" ["Description"]` | 在 `JIRA_BOARD` 创建Task |
| `jira.sh log ABC-123 2.5 [YYYY-MM-DD]` | 记录工时（默认今日UTC） |
| `jira.sh my [max]` | 自己的未关闭事务 |
| `jira.sh hours 2025-01-01 2025-01-07` | 按事务列出工时（JSON） |
| `jira.sh hours-day 2025-01-07 [name\|email]` | 按日全员工时，可按用户过滤 |
| `jira.sh hours-issue ABC-123 [name\|email]` | 按事务列工时，可按用户过滤 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 事务搜索
```bash
{baseDir}/（请参考skill目录中的脚本文件） search "payment failure" [maxResults]
```

在 `JIRA_BOARD` 项目范围内按 summary 或 key 模糊搜索。`maxResults` 可选，控制返回条数.
**输入**: 用户提供事务搜索所需的指令和必要参数.
### 2. 事务链接与详情
```bash
{baseDir}/（请参考skill目录中的脚本文件） link ABC-321       # 浏览器链接
{baseDir}/（请参考skill目录中的脚本文件） issue ABC-321      # 快速详情
```

**输入**: 用户提供事务链接与详情所需的指令和必要参数.
**处理**: 解析事务链接与详情的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回事务链接与详情的处理结果,包含执行状态码、结果数据和执行日志.
### 3. 状态流转
```bash
{baseDir}/（请参考skill目录中的脚本文件） transitions ABC-321        # 列出可用流转
{baseDir}/（请参考skill目录中的脚本文件） status ABC-321 "Done"      # 变更状态
```

状态变更前先调用 `transitions` 获取服务端提供的可用流转列表，校验通过后才应用，避免无效流转.
**输出**: 返回状态流转的处理结果,包含执行状态码、结果数据和执行日志.
### 4. 指派
```bash
{baseDir}/（请参考skill目录中的脚本文件） assign ABC-321 "Jane Doe"  # 按姓名/邮箱搜索后指派
{baseDir}/（请参考skill目录中的脚本文件） assign-me ABC-321          # 指派给自己
```

`assign` 会先按姓名或邮箱搜索用户，解析到 accountId 后再指派.
**输出**: 返回指派的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 评论与创建
```bash
{baseDir}/（请参考skill目录中的脚本文件） comment ABC-321 "Deployed to staging"
{baseDir}/（请参考skill目录中的脚本文件） create "Fix auth timeout" "Users being logged out after 5m"
```

`create` 在 `JIRA_BOARD` 项目创建 Task 类型事务，描述可选.
**处理**: 解析评论与创建的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 6. 工时记录
```bash
{baseDir}/（请参考skill目录中的脚本文件） log PB-321 1.5 2025-01-18
```

按小时记录工时。日期可选，默认今日UTC。数值支持小数（如 `1.5` 表示1.5小时）.
**输入**: 用户提供工时记录所需的指令和必要参数.
**处理**: 解析工时记录的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回工时记录的处理结果,包含执行状态码、结果数据和执行日志.
### 7. 工时统计

```bash
{baseDir}/（请参考skill目录中的脚本文件） hours 2025-01-01 2025-01-05                       # 自己按事务的工时
{baseDir}/（请参考skill目录中的脚本文件） hours-day 2025-01-05                              # 全员按日工时
{baseDir}/（请参考skill目录中的脚本文件） hours-day 2025-01-05 "jane"                       # 按日+用户过滤
{baseDir}/（请参考skill目录中的脚本文件） hours-issue ABC-321 "jane"                        # 按事务+用户过滤
```

- `hours`：按 `JIRA_EMAIL` 过滤，返回自己在指定日期范围内按事务分组的工时.
- `hours-day`：返回所有用户按事务与用户分组的工时汇总；可选按 name/email 过滤（同时解析为 accountId）.
- `hours-issue`：返回指定事务的工时；可选按 name/email 过滤.
- 所有工时命令输出 JSON，便于其他工具复用.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用流程

1. **配置环境变量**：设置 `JIRA_EMAIL`、`JIRA_API_TOKEN`、`JIRA_URL`，可选 `JIRA_BOARD`.
2. **校验依赖**：确认 `curl`、`jq`、`bc`、`python3` 可用.
3. **搜索或定位事务**：用 `search` 模糊搜索，或直接用事务key（如 `ABC-123`）.
4. **查看详情与流转**：用 `issue` 查看详情，`transitions` 查看可用流转.
5. **执行操作**：按需调用 `status`/`assign`/`assign-me`/`comment`/`create`/`log`.
6. **统计工时**：用 `hours`/`hours-day`/`hours-issue` 按事务、按日、按用户统计.
7. **复用输出**：工时命令的JSON输出可直接喂给其他工具或报表.
## 示例

### 示例1：搜索并查看事务

```bash
{baseDir}/（请参考skill目录中的脚本文件） search "timeout" 5
# 输出：匹配的5条事务，含key与summary
{baseDir}/（请参考skill目录中的脚本文件） issue ABC-123
# 输出：状态、指派人、优先级、summary
```

### 示例2：变更状态（含流转校验）

```bash
{baseDir}/（请参考skill目录中的脚本文件） transitions ABC-123
# 输出：可用流转列表（如 To Do → In Progress → Done）
{baseDir}/（请参考skill目录中的脚本文件） status ABC-123 "In Progress"
# 输出：状态已变更为 In Progress
```

### 示例3：记录工时

```bash
{baseDir}/（请参考skill目录中的脚本文件） log ABC-123 2.5 2025-01-18
# 输出：已在 ABC-123 记录 2.5 小时工时，日期 2025-01-18
```

### 示例4：按日全员工时统计

```bash
{baseDir}/（请参考skill目录中的脚本文件） hours-day 2025-01-07
# 输出：JSON，含每个用户在每个事务的工时汇总
{
  "2025-01-07": [
    {"user":"jane@example.com","issue":"ABC-123","hours":3.5},
    {"user":"john@example.com","issue":"ABC-124","hours":2.0}
  ]
}
```

### 示例5：创建Task

```bash
{baseDir}/（请参考skill目录中的脚本文件） create "Fix auth timeout" "Users being logged out after 5m"
# 输出：已创建 ABC-125（Task）
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| `JIRA_API_TOKEN` 未设置 | 环境变量缺失 | 在 shell 配置中 `export JIRA_API_TOKEN`，重新加载会话 |
| `JIRA_URL` 格式错误 | 未包含 `https://` 或域名错误 | 确保格式为 `https://your-domain.atlassian.net` |
| `401 Unauthorized` | 邮箱与Token不匹配 | 校验 `JIRA_EMAIL` 与 `JIRA_API_TOKEN` 是否对应同一账户 |
| `404 Not Found` | 事务key不存在或无权限 | 确认事务key拼写与项目访问权限 |
| `JIRA_BOARD` 未设置导致搜索范围过大 | 项目范围为空 | 设置 `JIRA_BOARD` 限定项目，或接受搜索全部项目 |
| `transitions` 校验失败 | 目标状态不在可用流转列表 | 先调用 `transitions` 查看可用状态，再选择合法流转 |
| `assign` 找不到用户 | 姓名或邮箱未匹配到用户 | 改用完整邮箱或Jira displayName，确认用户在项目内 |
| `log` 日期格式错误 | 非 `YYYY-MM-DD` | 严格使用 `2025-01-18` 格式，默认今日UTC可省略 |
| `bc: command not found` | 工时计算依赖缺失 | 安装 `bc`（如 `apt install bc`）后 |
| `jq: command not found` | JSON解析依赖缺失 | 安装 `jq`（如 `apt install jq`）后 |
| Worklog查询超时 | 大项目worklog/updated+list组合慢 | 等待几秒或缩小日期范围 |
| `create` 项目无Task类型 | `JIRA_BOARD` 项目未启用Task | 改用项目支持的事务类型，或联系Jira管理员 |

## 常见问题

### Q1：如何获取Jira API Token？
访问 <https://id.atlassian.com/manage-profile/security/api-tokens>，点击"Create API Token"，复制后设置为 `JIRA_API_TOKEN` 环境变量.
### Q2：`JIRA_BOARD` 不设置会怎样？
`JIRA_BOARD` 为空时，`search` 与 `create` 会搜索/创建在所有可访问项目内。建议设置以限定范围，避免误操作.
### Q3：`hours` 与 `hours-day` 有何区别？
`hours` 按 `JIRA_EMAIL` 过滤，只返回自己的工时，按事务分组；`hours-day` 返回所有用户的工时，按事务与用户分组，可选按 name/email 过滤.
### Q4：状态变更为何要先校验？
Jira的工作流决定了每个状态可达的下一个状态。`status` 命令先调用 `transitions` 获取服务端可用流转列表，校验通过才应用，避免无效流转报错.
### Q5：工时命令输出为何是JSON？
JSON格式便于其他工具（如报表、仪表盘）直接消费与复用。可用 `jq` 进一步过滤或格式化.
### Q6：`assign` 如何解析用户？
`assign` 先按姓名或邮箱调用Jira用户搜索API，解析到 accountId 后再指派。`hours-day`/`hours-issue` 的可选过滤参数也会同样解析为 accountId.
### Q7：工时记录的单位是什么？
单位为小时，支持小数。`log ABC-123 2.5` 表示记录2.5小时。日期可选，默认今日UTC.
### Q8：Worklog查询为何慢？
Worklog命令使用Jira的 worklog/updated + worklog/list 组合API，在大项目上可能耗时几秒。可缩小日期范围或耐心等待.
## 已知限制

- 仅支持Jira Cloud REST API，不支持Jira Server/Data Center.
- 依赖 `curl`、`jq`、`bc`、`python3` 四个外部工具，缺一不可.
- `create` 仅创建 Task 类型事务，不支持Bug/Story/Epic等其他类型.
- Worklog查询在大项目上较慢，因使用 worklog/updated + worklog/list 组合.
- `hours` 仅按 `JIRA_EMAIL` 过滤，无法直接按其他用户过滤（需用 `hours-day` 的可选参数）.
- 状态变更受Jira工作流约束，不可跳过流转校验.
- 依赖云服务，需要网络连接.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Jira集成助手处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "jira-skill"
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
