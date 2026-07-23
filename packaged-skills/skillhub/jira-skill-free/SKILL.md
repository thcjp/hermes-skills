---
slug: "jira-skill-free"
name: "jira-skill-free"
version: "1.0.0"
displayName: "Jira集成助手-免费版"
summary: "通过Jira Cloud REST API查看事务详情、状态流转与浏览器链接，适合只读浏览场景。"
license: "MIT"
description: |-
  Jira集成助手免费版提供Jira事务的只读浏览能力。
  支持模糊搜索、事务详情查看、浏览器链接生成与可用流转列表查看。
  核心能力：
  - 事务搜索：按summary或key模糊搜索
  - 事务详情与浏览器链接
  - 可用流转列表查看
  - 自己的未关闭事务列表
  升级付费版专享：状态变更、指派、评论、创建、工时记录、多维工时统计。
  适用场景：只读浏览Jira事务、快速定位事务、查看自己的待办。
tags:
  - 通用办公
  - Productivity
  - Jira
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
---
# Jira集成助手（免费版）

Jira集成助手免费版提供Jira事务的只读浏览能力。支持模糊搜索、事务详情查看、浏览器链接生成与可用流转列表查看。

## 环境配置

1. 获取API Token: <https://id.atlassian.com/manage-profile/security/api-tokens>
2. 点击"Create API Token"
3. 设置环境变量：

   ```bash
   export JIRA_EMAIL="you@example.com"
   export JIRA_API_TOKEN="[REDACTED]"
   export JIRA_URL="https://your-domain.atlassian.net"
   # 可选项目范围（逗号分隔）。空=搜索全部。
   export JIRA_BOARD="ABC"
   ```

依赖：`curl`、`jq`。

## 快速命令（免费版）

所有命令位于 `{baseDir}/scripts/jira.sh`。

| 命令 | 用途 |
|------|------|
| `jira.sh search "关键词" [max]` | 在 `JIRA_BOARD` 内按summary或key模糊搜索 |
| `jira.sh link ABC-123` | 生成事务浏览器链接 |
| `jira.sh issue ABC-123` | 快速查看事务详情 |
| `jira.sh transitions ABC-123` | 列出允许的流转 |
| `jira.sh my [max]` | 自己的未关闭事务 |

> `status`/`assign`/`assign-me`/`comment`/`create`/`log`/`hours`/`hours-day`/`hours-issue` 为付费版专享。

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

### 环境配置

1. 获取API Token: <https://id.atlassian.com/manage-profile/security/api-tokens>
2. 点击"Create API Token"
3. 设置环境变量：

   ```bash
   export JIRA_EMAIL="you@example.com"
   export JIRA_API_TOKEN="[REDACTED]

**输入**: 用户提供环境配置所需的参数和指令。
**处理**: 按照skill规范执行环境配置操作。
**输出**: 返回环境配置的执行结果,包含操作状态和输出数据。

### 快速命令（免费版）

所有命令位于 `{baseDir}/scripts/jira.sh`。

| 命令 | 用途 |
|------|------|
| `jira.sh search "关键词" [max]` | 在 `JIRA_BOARD` 内按summary或key模糊搜索 |
| `jira.sh link ABC-123` | 生成事务浏览器链接 |
| `jira.sh issue ABC-123` | 

**输入**: 用户提供快速命令（免费版）所需的参数和指令。
**处理**: 按照skill规范执行快速命令（免费版）操作。

### 核心能力（免费版）


**输入**: 用户提供核心能力（免费版）所需的指令和必要参数。
**处理**: 按照skill规范执行核心能力（免费版）操作,遵循单一意图原则。
**输出**: 返回核心能力（免费版）的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`核心能力（免费版）`相关配置参数进行设置
### 1. 事务搜索
```bash
{baseDir}/scripts/jira.sh search "payment failure" [maxResults]
```

在 `JIRA_BOARD` 项目范围内按 summary 或 key 模糊搜索。`maxResults` 可选，控制返回条数。

**输入**: 用户提供事务搜索所需的指令和必要参数。
### 2. 事务链接与详情
```bash
{baseDir}/scripts/ji

**输入**: 用户提供核心能力（免费版）所需的参数和指令。
**处理**: 按照skill规范执行核心能力（免费版）操作。

**输出**: 返回事务链接与详情的执行结果,包含操作状态和输出数据。
### 付费版专享能力

> 升级付费版解锁以下高级能力：

- **状态变更**：`status ABC-123 "Done"` 变更状态（含流转校验）。
- **指派**：`assign ABC-123 "Jane Doe"` 按姓名/邮箱搜索后指派；`assign-me` 指派给自己。
- **评论**：`comment ABC-123 "Deployed to staging"` 添加评论。
- **创建事务**：

**输入**: 用户提供付费版专享能力所需的参数和指令。
**处理**: 按照skill规范执行付费版专享能力操作。
**输出**: 返回付费版专享能力的执行结果,包含操作状态和输出数据。
### jira.sh search "关键词" max

执行jira.sh search "关键词" max操作,处理用户输入并返回结果。

**输入**: 用户提供jira.sh search "关键词" max所需的参数和指令。

**输出**: 返回jira.sh search "关键词" max的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`jira.sh search "关键词" max`相关配置参数进行设置

#
## 核心能力（免费版）

### 1. 事务搜索

```bash
{baseDir}/scripts/jira.sh search "payment failure" [maxResults]
```

在 `JIRA_BOARD` 项目范围内按 summary 或 key 模糊搜索。`maxResults` 可选，控制返回条数。

### 2. 事务链接与详情

```bash
{baseDir}/scripts/jira.sh link ABC-321       # 浏览器链接
{baseDir}/scripts/jira.sh issue ABC-321      # 快速详情
```

### 3. 可用流转列表

```bash
{baseDir}/scripts/jira.sh transitions ABC-321
```

查看事务当前可用的流转列表（只读，不执行变更）。

### 4. 自己的未关闭事务

```bash
{baseDir}/scripts/jira.sh my [max]
```

列出指派给自己且未关闭的事务。

## 使用流程

1. **配置环境变量**：设置 `JIRA_EMAIL`、`JIRA_API_TOKEN`、`JIRA_URL`，可选 `JIRA_BOARD`。
2. **校验依赖**：确认 `curl`、`jq` 可用。
3. **搜索或定位事务**：用 `search` 模糊搜索，或直接用事务key（如 `ABC-123`）。
4. **查看详情与流转**：用 `issue` 查看详情，`transitions` 查看可用流转。
5. **跳转浏览器**：用 `link` 生成浏览器链接，手动在Jira Web界面执行变更操作。

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 示例

### 示例1：搜索并查看事务

```bash
{baseDir}/scripts/jira.sh search "timeout" 5
# 输出：匹配的5条事务，含key与summary
{baseDir}/scripts/jira.sh issue ABC-123
# 输出：状态、指派人、优先级、summary
```

### 示例2：查看可用流转

```bash
{baseDir}/scripts/jira.sh transitions ABC-123
# 输出：可用流转列表（如 To Do → In Progress → Done）
```

### 示例3：生成浏览器链接

```bash
{baseDir}/scripts/jira.sh link ABC-123
# 输出：https://your-domain.atlassian.net/browse/ABC-123
```

### 示例4：查看自己的待办

```bash
{baseDir}/scripts/jira.sh my 10
# 输出：指派给自己的10条未关闭事务
```

## 付费版专享能力

> 升级付费版解锁以下高级能力：

- **状态变更**：`status ABC-123 "Done"` 变更状态（含流转校验）。
- **指派**：`assign ABC-123 "Jane Doe"` 按姓名/邮箱搜索后指派；`assign-me` 指派给自己。
- **评论**：`comment ABC-123 "Deployed to staging"` 添加评论。
- **创建事务**：`create "Title" "Description"` 在 `JIRA_BOARD` 创建Task。
- **工时记录**：`log ABC-123 2.5 2025-01-18` 按小时记录工时，支持指定日期。
- **工时统计**：`hours`/`hours-day`/`hours-issue` 按事务、按日、按用户多维度统计。
- **JSON输出**：工时命令输出JSON，便于其他工具复用。
- **完整依赖支持**：付费版额外支持 `bc` 与 `python3` 用于工时计算与解析。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `JIRA_API_TOKEN` 未设置 | 环境变量缺失 | 在 shell 配置中 `export JIRA_API_TOKEN`，重新加载会话 |
| `JIRA_URL` 格式错误 | 未包含 `https://` 或域名错误 | 确保格式为 `https://your-domain.atlassian.net` |
| `401 Unauthorized` | 邮箱与Token不匹配 | 校验 `JIRA_EMAIL` 与 `JIRA_API_TOKEN` 是否对应同一账户 |
| `404 Not Found` | 事务key不存在或无权限 | 确认事务key拼写与项目访问权限 |
| `JIRA_BOARD` 未设置导致搜索范围过大 | 项目范围为空 | 设置 `JIRA_BOARD` 限定项目，或接受搜索全部项目 |
| `jq: command not found` | JSON解析依赖缺失 | 安装 `jq`（如 `apt install jq`）后检查网络连接和配置后重试 |
| 调用付费版专享命令 | 免费版仅支持只读浏览 | 升级付费版解锁status/assign/comment/create/log/hours等命令 |

## 常见问题

### Q1：免费版支持哪些命令？
免费版支持 `search`、`link`、`issue`、`transitions`、`my` 五个只读命令。`status`/`assign`/`comment`/`create`/`log`/`hours` 等写操作与统计命令为付费版专享。

### Q2：如何获取Jira API Token？
访问 <https://id.atlassian.com/manage-profile/security/api-tokens>，点击"Create API Token"，复制后设置为 `JIRA_API_TOKEN` 环境变量。

### Q3：免费版能变更事务状态吗？
不能。`status` 为付费版专享。免费版可用 `transitions` 查看可用流转，再用 `link` 跳转浏览器手动变更。

### Q4：免费版能记录工时吗？
不能。`log`/`hours`/`hours-day`/`hours-issue` 为付费版专享。免费版无法记录与统计工时。

### Q5：`JIRA_BOARD` 不设置会怎样？
`JIRA_BOARD` 为空时，`search` 会搜索所有可访问项目。建议设置以限定范围。

### Q6：如何升级到付费版？
参考 `-jira-skill` 付费版SKILL.md，解锁状态变更、指派、评论、创建、工时记录与多维工时统计。

### Q7：免费版依赖哪些工具？
仅依赖 `curl` 与 `jq`。付费版额外依赖 `bc` 与 `python3` 用于工时计算与解析。

## 已知限制

- 仅支持Jira Cloud REST API，不支持Jira Server/Data Center。
- 仅支持只读命令（search/link/issue/transitions/my），无写操作能力。
- 不支持状态变更（`status` 为付费版专享）。
- 不支持指派（`assign`/`assign-me` 为付费版专享）。
- 不支持评论与创建（`comment`/`create` 为付费版专享）。
- 不支持工时记录与统计（`log`/`hours`/`hours-day`/`hours-issue` 为付费版专享）。
- 依赖云服务，需要网络连接。
- 依赖 `curl` 与 `jq` 两个外部工具。
