---
slug: "github-manager"
name: "github-manager"
version: 1.0.1
displayName: "GitHub管理器(专业版)"
summary: "全功能GitHub管理工具,含批量操作、GraphQL高级查询、自动化工作流、团队仪表盘与Webhook管理,适合团队企业级协作。"
license: "Proprietary"
edition: "pro"
description: |-
  GitHub管理器(专业版)是企业级GitHub协作管理工具,在免费版基础查询能力上,扩展批量操作、GraphQL高级查询、自动化工作流、团队仪表盘与Webhook管理等高级能力。核心能力:
  - 批量Issue/PR操作: 批量关闭、打标签、分配负责人、迁移
  - GraphQL高级查询: 复杂关联查询、跨仓库聚合、深度分页
  - 自动化工作流: 定时检查、自动分配、状态流转、通知告警
  - 团队仪表盘: 多仓库汇总、成员贡献统计、燃尽图
  - Webhook管理: 事件订阅、自动触发、回调配置
  - 安全审计: 权限审查、敏感信息扫...
tags:
  - GitHub
  - 团队协作
  - 自动化
  - 企业版
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# GitHub管理器(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| GitHub管理器(专业版)功能GitHub管理 | 不支持 | 支持 |
| GitHub管理器(专业版)raphQL高级查询 | 不支持 | 支持 |
| GitHub管理器(专业版)与Webhook管理 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |

## 核心能力

### 批量Issue/PR操作

```bash
# 批量关闭带"stale"标签的Issue
gh-manager issue batch-close --repo owner/repo --label stale --reason "not_planned"
# ...
# 批量打标签
gh-manager issue batch-label --repo owner/repo --issues 1,3,5,7 --labels "bug,priority:high"
# ...
# 批量分配负责人
gh-manager issue batch-assign --repo owner/repo --issues 10-20 --assignee "alice"
# ...
# 批量迁移Issue到另一仓库
gh-manager issue migrate --from owner/repo-a --to owner/repo-b --issues 1-50
# ...
# 批量重新打开
gh-manager issue batch-reopen --repo owner/repo --issues 30,32,35
```

批量操作安全机制:
- **预演模式**: `--dry-run`先预览变更,不实际执行
- **确认机制**: 影响超过10条记录时需二次确认
- **回滚支持**: 每次批量操作生成回滚脚本
- **速率控制**: 自动遵守API限速,避免触发429

### GraphQL高级查询
```bash
# 跨仓库查询某作者的所有PR
gh-manager graphql query --file queries/cross_repo_prs.graphql --vars '{"author":"alice"}'
# ...
# 依赖说明
gh-manager graphql query --file queries/dependency_graph.graphql --vars '{"repo":"owner/repo"}'
# ...
# 深度分页查询(自动处理cursor)
gh-manager graphql paginate --file queries/all_issues.graphql --limit 1000
```

GraphQL查询示例:

```graphql
# 查询团队的PR贡献统计
query teamContributions($logins: [String!]!, $since: DateTime!) {
  users(filter: {logins: $logins}) {
    login
    contributionsCollection(from: $since) {
      pullRequestContributions(first: 100) {
        totalCount
        nodes {
          pullRequest {
            repository { nameWithOwner }
            state
            additions
            deletions
          }
        }
      }
    }
  }
}
```

**输出**: 返回GraphQL高级查询的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `graphql高级查询` 选项

### 自动化工作流

```bash
# 创建自动化规则
gh-manager automation create --name "stale-issue-triage" \
  --trigger "schedule:0 9 * * 1" \
  --condition "label:none AND updated:<7d" \
  --action "add-label:stale AND comment:'此Issue已7天未更新,7天后将自动关闭'"
# ...
# 查看所有自动化规则
gh-manager automation list
# ...
# 手动触发规则
gh-manager automation run --name "stale-issue-triage" --repo owner/repo
# ...
# 查看执行历史
gh-manager automation history --name "stale-issue-triage" --last 10
```

自动化场景模板:

| 模板 | 触发条件 | 动作 |
|:-----|:-----|:-----|
| Stale Issue | 7天无更新 | 加stale标签,14天后关闭 |
| Auto Assign | 新Issue创建 | 按轮询分配给团队成员 |
| PR Review Reminder | PR 24h未review | 通知指定reviewer |
| CI Failure Alert | 工作流失败 | 发送通知到IM |
| Branch Cleanup | PR合并后 | 删除已合并分支 |
| Release Notes | 发布Release | 自动生成变更日志 |

### 团队仪表盘
```bash
# 生成团队周报
gh-manager dashboard weekly --repos "owner/repo1,owner/repo2" --team "alice,bob,carol" --format pdf
# ...
# 查看贡献统计
gh-manager dashboard contributions --repos "owner/repo1" --period 30d
# ...
# 燃尽图(基于Issue/PR)
gh-manager dashboard burndown --repo owner/repo --milestone "v2.0"
# ...
# 多仓库汇总
gh-manager dashboard summary --org my-org --period week
```

仪表盘维度:
- Issue/PR数量与状态分布
- 成员贡献排名(提交、PR、review)
- 平均响应时间与关闭周期
- CI/CD成功率与平均时长
- 标签分布与趋势

**输入**: 用户提供团队仪表盘所需的指令和必要参数.
**处理**: 解析团队仪表盘的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### Webhook管理
```bash
# 列出仓库Webhook
gh-manager webhook list --repo owner/repo
# ...
# 添加Webhook
gh-manager webhook add --repo owner/repo \
  --url "https://hooks.example.com/github" \
  --events "issues,pull_request,push" \
  --secret "$WEBHOOK_SECRET"
# ...
# 测试Webhook
gh-manager webhook test --repo owner/repo --id 123 --event "issues"
# ...
# 删除Webhook
gh-manager webhook delete --repo owner/repo --id 123
```

**处理**: 解析Webhook管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Webhook管理的处理结果,包含执行状态码、结果数据和执行日志。### 安全审计
```bash
# 权限审查
gh-manager audit permissions --repo owner/repo --format csv
# ...
# 敏感信息扫描
gh-manager audit secrets --repo owner/repo --depth 100
# ...
# 合规报告
gh-manager audit compliance --org my-org --standard SOC2 --format pdf
# ...
# Token使用审计
gh-manager audit tokens --org my-org --period 90d
```

**输入**: 用户提供安全审计所需的指令和必要参数.
**处理**: 解析安全审计的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回安全审计的处理结果,包含执行状态码、结果数据和执行日志.
#
## 适用场景

### 场景1 -开源项目Issue triage自动化

用户意图: "开源项目Issue太多,需要自动化triage流程。"

实施方案:
1. 创建"stale-issue-triage"自动化规则(7天无更新加标签,14天关闭)
2. 创建"auto-assign"规则(新Issue按标签分配给maintainer)
3. 创建"bug-report-template"规则(缺少复现步骤的Issue自动回复模板)
4. 每周生成triage报告,review未处理Issue

### 场景2 -多仓库团队管理

用户意图: "团队管理5个仓库,需要统一视图。"

实施方案:
1. 使用`gh-manager dashboard summary --org my-org`汇总多仓库状态
2. 配置跨仓库Webhook,统一接收事件
3. 设置CI失败自动告警(通知到IM)
4. 每月生成团队贡献报告

### 场景3 -安全合规审计

用户意图: "准备SOC2审计,需要GitHub权限与操作记录。"

实施方案:
1. 运行`gh-manager audit permissions`导出权限矩阵
2. 运行`gh-manager audit secrets`扫描敏感信息
3. 运行`gh-manager audit compliance --standard SOC2`生成合规报告
4. 导出90天操作日志作为审计证据

### 场景4 -大规模Issue迁移

用户意图: "要把旧仓库的200个Issue迁移到新仓库。"

实施方案:
1. 使用`--dry-run`预演迁移,确认映射关系
2. 执行`gh-manager issue migrate --from old --to new --issues 1-200`
3. 自动保留原始标签、assignee、评论
4. 生成迁移报告,核对数量

## 使用流程

### 第1步:安装与认证

```bash
# 安装专业版
pip install gh-manager[pro]
# ...
# 完成GitHub认证(继承gh的认证)
gh auth login
# ...
# 验证专业版功能
gh-manager version
gh-manager status
```

### 第2步:配置团队

```bash
# 初始化团队配置
gh-manager team init --org my-org
# ...
# 添加团队成员
gh-manager team add --members "alice,bob,carol"
# ...
# 配置多仓库
gh-manager repo add --repos "owner/repo1,owner/repo2,owner/repo3"
```

### 第3步:启用自动化

```bash
# 启用stale issue自动化
gh-manager automation enable --template stale-issue-triage
# ...
# 启用CI失败告警
gh-manager automation enable --template ci-failure-alert --notify "im:#devops"
# ...
# 查看已启用的自动化
gh-manager automation list --enabled
```

### 第4步:生成仪表盘

```bash
# 生成本周团队报告
gh-manager dashboard weekly --format pdf --output weekly-report.pdf
# ...
# 查看实时仪表盘
gh-manager dashboard live --port 8080
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | github-manager处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **gh CLI**: 2.0+(GitHub官方命令行工具,作为底层依赖)
- **Python**: 3.8+(运行gh-manager CLI)
- **Node.js**: 16+(可选,用于实时仪表盘)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| gh-manager[pro] | CLI工具 | 必需 | `pip install gh-manager[pro]` |
| gh | CLI工具 | 必需 | `brew install gh` |
| jq | 命令行工具 | 可选 | `brew install jq` |
| GraphQL client | Python库 | 必需 | 随gh-manager安装 |
| GitHub账号 | 在线服务 | 必需 | 注册GitHub账号 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- **GitHub认证**: 通过`gh auth login`完成OAuth,token存储于`~/.config/gh/hosts.yml`
- **Webhook Secret**: 通过环境变量`WEBHOOK_SECRET`配置,加密存储
- **IM通知Token**: 通过环境变量配置(如Slack/钉钉的webhook URL)
- **Token权限**: 建议包含`repo`、`workflow`、`read:org`、`admin:org_hook`
- **禁止**: 在SKILL.md或脚本中硬编码任何Token或Secret

### 可用性分类
- **分类**: MD+EXEC+CLI+DAEMON(Markdown指令+命令行工具+自动化守护)
- **说明**: 基于Markdown的AI Skill，高级功能需要gh-manager CLI与自动化守护进程

## 案例展示

### 完整专业版配置

```json
{
  "edition": "pro",
  "github": {
    "auth_mode": "oauth",
    "default_scope": ["repo", "workflow", "read:org", "admin:org_hook"]
  },
  "team": {
    "org": "my-org",
    "members": ["alice", "bob", "carol"],
    "repos": ["owner/repo1", "owner/repo2", "owner/repo3"]
  },
  "automation": {
    "enabled": true,
    "rules": [
      {
        "name": "stale-issue-triage",
        "trigger": "schedule:0 9 * * 1",
        "condition": "label:none AND updated:<7d",
        "action": "add-label:stale"
      },
      {
        "name": "ci-failure-alert",
        "trigger": "workflow_run:completed:failure",
        "action": "notify:im:#devops"
      }
    ]
  },
  "dashboard": {
    "enabled": true,
    "port": 8080,
    "refresh_interval": 300
  },
  "audit": {
    "enabled": true,
    "log_retention": 365,
    "alert_on_secret": true
  }
}
```

### 自动化规则示例

```yaml
# automation_rules.yaml
- name: auto-assign-by-label
  description: 按Issue标签自动分配负责人
  trigger:
    type: event
    event: issues
    action: opened
  condition:
    label: bug
  action:
    type: assign
    strategy: round_robin
    team: [alice, bob, carol]
# ...
- name: pr-review-sla
  description: PR review SLA监控
  trigger:
    type: schedule
    cron: "0 10 * * *"
  condition:
    pr_state: open
    review_age: ">24h"
  action:
    type: notify
    channel: im
    target: "#pr-reviews"
    message: "PR #"manager_result" 待review已超过24小时"
```

## 常见问题

### Q1: 批量操作会不会触发GitHub限速?

A: 专业版自动遵守API限速(5000请求/小时),超限时自动排队等待。大批量操作(>100条)建议在低峰期执行,并启用`--rate-limit wait`模式.
### 错误恢复步骤
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

A: GitHub GraphQL API有复杂度评分限制(单次查询≤500000点)。专业版会自动计算复杂度,超限时建议拆分查询或使用分页.
### Q3: 自动化规则失败会通知吗?

A: 会。自动化规则执行失败时,自动发送通知到配置的channel(邮件/IM)。同时记录到`automation_history`表,可通过`gh-manager automation history --failed`查看.
### Q4: 团队仪表盘数据多久更新一次?

A: 实时仪表盘默认5分钟刷新一次(可配置)。周报/月报在生成时全量拉取。建议启用数据缓存,降低API消耗.
### Q5: Webhook secret如何管理?

A: 通过环境变量`WEBHOOK_SECRET`配置,加密存储于`~/.gh-manager/secrets.enc`。禁止在配置文件中明文存储。支持按仓库配置不同secret.
### Q6: 安全审计会扫描哪些敏感信息?

A: 扫描内容包括: API Key、密码、私钥、token等(基于正则与熵值检测)。支持自定义扫描规则。发现敏感信息会自动告警并生成Issue.
### Q7: 如何导出审计报告给合规团队?

A: 运行`gh-manager audit compliance --standard SOC2 --format pdf --output audit.pdf`,支持SOC2、ISO27001、GDPR等标准。报告包含权限矩阵、操作日志、敏感信息扫描结果.
### Q8: 多组织场景如何管理?

A: 通过`gh-manager org add`添加多个组织,切换时用`--org`参数指定。仪表盘支持跨组织汇总视图.
### Q9: 自动化规则支持哪些触发条件?

A: 支持: (1)定时(cron表达式); (2)事件(Issue/PR/Push/Release等); (3)状态变化(标签添加、状态流转); (4)外部webhook。可组合多条件.
### Q10: 专业版支持GitHub Enterprise吗?

A: 支持。配置`GITHUB_ENTERPRISE_HOST`环境变量即可连接Enterprise Server。所有功能在Enterprise环境下均可用.
## 错误处理

| 错误场景(续)(续)| 原因 | 处理方式 |
|:------------:|--------------|:-------------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- API调用依赖第三方服务的可用性与稳定性
- 免费版有调用次数限制与并发限制
