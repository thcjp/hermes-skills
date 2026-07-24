---
slug: "jira-flow-skill"
name: "jira-flow-skill"
version: 1.0.1
displayName: "Jira Flow 专业版"
summary: "全功能Jira任务管理与团队工时分析，支持批量操作、自定义报表与自动化集成。。Jira Flow Skill 专业版面向团队负责人与项目经理，在免费版基础上解锁批量任务操作、多项目工时对比、"
license: "MIT"
edition: "pro"
description: |-
  Jira Flow Skill 专业版面向团队负责人与项目经理，在免费版基础上解锁批量任务操作、多项目工时对比、自定义报表模板与团队工时聚合视图。核心能力：单条命令完成批量状态流转、跨项目工时对比报表、自定义工时模板导出（Markdown/CSV/JSON）、团队成员工时聚合、Webhook 自动化触发、并发请求与缓存优化
tags:
  - 集成工具
  - 任务管理
  - 团队协作
  - 自动化
  - 工具
  - 写作
  - 电商
  - bash
  - basedir
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
category: "Automation"
---
# Jira Flow 专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Jira Flow 专业版功能Jira任务管理 | 不支持 | 支持 |
| Jira Flow 专业版与团队工时分析 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |

## 核心能力

| 能力域 | 命令族 | 说明 | 专业版增强 |
|:-----|:-----|:-----|:-----|
| 任务检索 | `search` / `my` / `team` | 模糊搜索、个人任务、团队任务 | 新增 `team` 团队视角 |
| 状态管理 | `status` / `transitions` / `batch-status` | 单条与批量状态流转 | 新增批量操作 |
| 任务分配 | `assign` / `batch-assign` | 单条与批量分配 | 新增批量分配 |
| 工时记录 | `log` / `batch-log` | 单条与批量工时记录 | 新增批量记录 |
| 工时统计 | `hours` / `hours-day` / `hours-issue` / `hours-team` | 多维工时统计 | 新增团队聚合 |
| 报表导出 | `report` | 自定义模板导出 | 专业版独有 |
| 自动化 | `webhook` / `watch` | Webhook 注册与事件监听 | 专业版独有 |
| 缓存优化 | `cache` | 多级缓存管理 | 专业版独有 |
### 能力域

针对能力域,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力域相关的配置参数、输入数据和处理选项.
**输出**: 返回能力域的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力域`的配置文档进行参数调优
### 任务检索

针对任务检索,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供任务检索相关的配置参数、输入数据和处理选项.
**输出**: 返回任务检索的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`任务检索`的配置文档进行参数调优
### 状态管理

针对状态,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供状态管理相关的配置参数、输入数据和处理选项.
**输出**: 返回状态管理的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`状态管理`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：项目经理一键生成团队周报（项目经理角色）

每周一上午需要汇总上周团队工时投入分布，并按项目维度对比。专业版提供 `hours-team` 命令与 `report` 模板能力：

```bash
# 拉取团队上周工时（按用户+任务聚合）
bash {baseDir}/（请参考skill目录中的脚本文件） hours-team 2025-01-06 2025-01-12
# ...
# 按自定义模板生成 Markdown 周报
bash {baseDir}/（请参考skill目录中的脚本文件） report --template weekly --format markdown --output weekly-report.md
```

### 场景二：Sprint 结束时批量关闭已完成任务（Scrum Master 角色）

Sprint 评审后需要将一批已验证的任务统一关闭。免费版需要逐条执行，专业版支持批量：

```bash
# 批量更新状态（自动并发，带限流）
bash {baseDir}/（请参考skill目录中的脚本文件） batch-status ABC-101,ABC-102,ABC-103 "Done"
# ...
# 批量记录工时
bash {baseDir}/（请参考skill目录中的脚本文件） batch-log "ABC-101:2.5,ABC-102:1.5,ABC-103:3.0" 2025-01-18
```

### 场景三：CI/CD 流水线自动更新 Jira 状态（DevOps 工程师角色）

部署成功后自动将关联任务流转到"已部署"状态，并通过 Webhook 通知 IM 群：

```bash
# 注册 Webhook（部署成功事件）
bash {baseDir}/（请参考skill目录中的脚本文件） webhook register \
  --event deployment.success \
  --action "status {ISSUE_KEY} '已部署'"
# ...
# 监听事件并触发动作
bash {baseDir}/（请参考skill目录中的脚本文件） watch --event deployment.success
```

### 场景四：跨项目工时投入对比（技术负责人角色）

需要对比本月团队在两个项目上的工时投入比例，作为资源调配依据：

```bash
# 跨项目工时对比
bash {baseDir}/（请参考skill目录中的脚本文件） hours-team 2025-01-01 2025-01-31 \
  --projects "ABC,XYZ" \
  --group-by project
```

### 场景五：大型项目工时统计性能优化（团队负责人角色）

万级任务的项目工时统计耗时较长，专业版提供缓存与并发优化：

```bash
# 预热缓存（transitions 与用户列表）
bash {baseDir}/（请参考skill目录中的脚本文件） cache warm --include transitions,users
# ...
# 并发拉取工时（默认 5 并发，可调整）
bash {baseDir}/（请参考skill目录中的脚本文件） hours 2025-01-01 2025-01-31 --concurrency 8
```

## 使用流程

### 前置准备（约 60 秒）

1. 访问 Atlassian API Token 管理页：`https://id.atlassian.com/manage-profile/security/api-tokens`
2. 点击"Create API Token"生成令牌
3. 配置环境变量：

```bash
export JIRA_EMAIL="you@example.com"
export JIRA_API_TOKEN="你的API令牌"
export JIRA_URL="https://your-domain.atlassian.net"
export JIRA_BOARD="ABC"
# 专业版新增：并发与缓存配置
export JIRA_FLOW_CONCURRENCY=5
export JIRA_FLOW_CACHE_DIR="$HOME/.jira-flow-cache"
```

### 验证专业版能力（约 30 秒）

```bash
# 验证团队工时聚合
bash {baseDir}/（请参考skill目录中的脚本文件） hours-team 2025-01-01 2025-01-07
# ...
# 验证缓存预热
bash {baseDir}/（请参考skill目录中的脚本文件） cache warm
```

### 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows（需 WSL 或 Git Bash）/ macOS / Linux
- **Shell**：bash 4.0+
- **磁盘**：缓存目录建议预留 50MB

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|---:|---:|---:|---:|---:|
| curl | 命令行工具 | 必需 | 系统自带或包管理器安装 | 7.0+ |
| jq | JSON 处理工具 | 必需 | `apt install jq` / `brew install jq` | 1.6+ |
| bc | 数值计算工具 | 必需 | `apt install bc` / `brew install bc` | 1.07+ |
| python3 | 运行时 | 必需 | `apt install python3` / 官网下载 | 3.8+ |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |

### API Key 配置

- **JIRA_EMAIL**：通过环境变量配置，存储于 Shell 配置文件
- **JIRA_API_TOKEN**：通过环境变量配置，禁止明文写入脚本或提交到版本库
- **JIRA_URL**：通过环境变量配置
- **JIRA_BOARD**：可选，通过环境变量配置
- **Webhook Secret**：通过环境变量 `JIRA_FLOW_WEBHOOK_SECRET` 配置

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 调用脚本完成任务

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | jira-flow-skill处理的内容输入 |,  |
| content | string | 否 | jira-flow-skill处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "skill 相关配置参数",
    result: "skill 相关配置参数",
    result: "skill 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|:------|------:|:------|:------|
| 401 未授权 | Token 过期或邮箱错误 | 重新生成 Token，核对邮箱 | P0 |
| 404 任务不存在 | 键值错误或项目无权限 | 核对键值，检查项目权限 | P1 |
| 429 速率限制 | 并发过高或高峰时段 | 降低并发数，避开高峰 | P1 |
| 500 服务端错误 | Jira 实例异常 | 等待 5 分钟查看 Jira 状态页 | P2 |
| 缓存命中率为 0 | 缓存目录权限或路径错误 | 检查 `JIRA_FLOW_CACHE_DIR` 权限 | P2 |
| Webhook 无事件 | URL 不可达或 secret 错误 | 校验 URL 公网可达性，核对 secret | P1 |
| 批量操作部分失败 | 个别任务状态不允许流转 | 查看失败 CSV，逐条修复后 | P2 |

## 依赖说明(补充)

| 依赖项 | 类型 | 必需 | 说明 |
|---:|:---|---:|---:|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 环境变量配置表

| 变量名 | 必填 | 默认值 | 说明 |
|:------:|--------|:-------|:------:|
| `JIRA_EMAIL` | 是 | 无 | 登录 Jira 的邮箱 |
| `JIRA_API_TOKEN` | 是 | 无 | Atlassian API 令牌 |
| `JIRA_URL` | 是 | 无 | Jira 实例地址（含 https://） |
| `JIRA_BOARD` | 否 | 空 | 项目键值过滤 |
| `JIRA_FLOW_CONCURRENCY` | 否 | 5 | 并发请求数（建议 3-10） |
| `JIRA_FLOW_CACHE_DIR` | 否 | `~/.jira-flow-cache` | 缓存目录 |
| `JIRA_FLOW_CACHE_TTL` | 否 | 3600 | 缓存有效期（秒） |

### 自定义报表模板

在 `$JIRA_FLOW_CACHE_DIR/templates/` 下放置模板文件，支持以下变量：

| 变量 | 含义 | 示例 |
|----|:--:|---:|
| `Jira Flow Skill 核心处理` | 统计区间起点 | 2025-01-01 |
| `Jira Flow Skill 智能分析` | 统计区间终点 | 2025-01-07 |
| `Jira Flow Skill 批量处理` | 总工时 | 120.5 |
| `Jira Flow Skill 自定义配置` | 按用户聚合 | JSON 数组 |
| `Jira Flow Skill 结果导出` | 按项目聚合 | JSON 数组 |

### Webhook 自动化配置

```bash
# 注册 Webhook
bash {baseDir}/（请参考skill目录中的脚本文件） webhook register \
  --event issue.updated \
  --url "https://your-im-bot/webhook" \
  --secret "your-webhook-secret"
# ...
# 查看已注册 Webhook
bash {baseDir}/（请参考skill目录中的脚本文件） webhook list
# ...
# 删除 Webhook
bash {baseDir}/（请参考skill目录中的脚本文件） webhook delete --id 12345
```

## 常见问题

### Q1：批量操作中部分任务失败如何处理？

专业版采用"部分成功"策略：成功的任务正常更新，失败的任务会输出到 stderr 并记录到 `$JIRA_FLOW_CACHE_DIR/failed-<timestamp>.csv`，可基于该文件重试.
### Q2：并发数设置多少合适？

取决于 Jira 实例的速率限制策略。建议从默认值 5 开始，观察是否出现 429 错误。如果稳定无错误，可逐步提升到 8-10；如果频繁报错，降低到 3.
### Q3：缓存数据会过期吗？

默认 TTL 为 3600 秒（1 小时）。可通过 `JIRA_FLOW_CACHE_TTL` 调整。`transitions` 缓存过期后会自动重新拉取；用户列表缓存过期后会在下次分配操作时刷新.
### Q4：Webhook 接收不到事件？

检查三项：Webhook URL 是否可被 Jira 实例访问（需公网可达）、secret 是否与注册时一致、事件类型是否匹配。可在 Webhook 管理页查看投递日志.
### Q5：报表模板变量未渲染？

确认模板文件位于 `$JIRA_FLOW_CACHE_DIR/templates/` 目录，且变量使用双花括号语法 `jira-flow-skill_template`。模板修改后无需重启，下次执行 `report` 命令会自动加载.
### Q6：跨项目工时对比耗时较长？

跨项目查询需要遍历多个项目的 worklog，建议先 `cache warm` 预热，并使用 `--concurrency 8` 提升并发。对于超过 3 个项目的对比，建议分批执行后本地合并.
### 错误恢复步骤
| 错误场景 | 原因 | 处理方式 |
|----|----|----|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

专业版内置自动退避重试，默认重试 3 次，每次间隔指数退避（1s、2s、4s）。如果仍失败，建议降低并发数或避开高峰时段.
### Q8：如何在 CI/CD 中安全使用 API Token？

将 Token 存储在 CI/CD 平台的密钥管理中（如 GitHub Actions Secrets、GitLab CI Variables），通过环境变量注入。禁止将 Token 写入脚本或配置文件.
### Q9：报表导出支持哪些格式？

支持 Markdown、CSV、JSON 三种格式。Markdown 适合周报与月报；CSV 适合导入 Excel 二次加工；JSON 适合被其他脚本消费.
### Q10：专业版与免费版可以共存吗？

可以。两个版本的 slug 不同（`-free` 与 `-pro`），可同时安装。建议根据场景切换：日常个人操作用免费版，团队管理与自动化用专业版.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:--------|:--------|:--------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 本地存储任务数据，不支持团队协作分配
- 免费版不支持甘特图与依赖关系管理等高级功能
