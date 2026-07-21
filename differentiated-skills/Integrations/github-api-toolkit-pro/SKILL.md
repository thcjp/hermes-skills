---
slug: github-api-toolkit-pro
name: github-api-toolkit-pro
version: "1.0.0"
displayName: GitHub API工具包(专业版)
summary: 全功能GitHub API集成工具,含GraphQL、批量操作、Webhook管理、Actions API与组织管理,适合企业级集成场景。
license: Proprietary
edition: pro
description: |-
  GitHub API工具包(专业版)是企业级GitHub API集成工具,在免费版REST基础能力上,扩展GraphQL查询、批量操作、Webhook管理、GitHub Actions API、组织与团队管理等高级能力。核心能力:
  - GraphQL API: 高效关联查询,减少请求次数,支持复杂分页
  - 批量操作: 批量创建/更新/删除资源,含速率控制与回滚
  - Webhook管理: 订阅事件、配置回调、测试与调试
  - GitHub Actions API: 工作流管理、运行控制、产物下载
  - 组织与团队管理: 成员管理、团队...
tags:
- GitHub
- API
- 企业集成
- 自动化
tools:
  - - read
- exec
# GitHub API工具包(专业版)
---
全功能GitHub API集成工具,在免费版REST基础上,扩展GraphQL、批量操作、Webhook管理、Actions API与组织管理,适合企业级集成场景。

## 概述
在企业级集成中, GitHub API不仅是"调用端点",更涉及高效查询(GraphQL)、批量处理、事件驱动(Webhook)、CI/CD控制(Actions API)与组织治理。专业版围绕"深度集成"构建完整能力矩阵,帮助企业将GitHub能力嵌入现有系统。

专业版兼容免费版的所有REST端点,可直接升级,无需更换token。

## 核心能力
### GraphQL API
GraphQL相比REST的优势: 一次查询获取关联数据,减少请求次数:

```bash
curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query { repository(owner: \"owner\", name: \"repo\") { issues(first: 10, states: OPEN) { totalCount nodes { number title labels(first: 5) { nodes { name } } } } pullRequests(first: 10, states: OPEN) { totalCount } releases(first: 3) { nodes { tagName publishedAt } } } }"
  }' \
  https://api.graphql
```

GraphQL查询模板库:

```graphql
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
            mergedAt
          }
        }
      }
      issueContributions(first: 100) {
        totalCount
      }
    }
  }
}

query dependencyGraph($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    dependencyGraphManifests(first: 50) {
      nodes {
        filename
        dependencies(first: 100) {
          nodes {
            packageManager
            packageName
            requirements
          }
        }
      }
    }
  }
}
```

**输入**: 用户提供GraphQL API所需的指令和必要参数。
**处理**: 按照skill规范执行GraphQL API操作,遵循单一意图原则。
**输出**: 返回GraphQL API的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 批量操作
```bash
gh-api-toolkit batch-create-issues \
  --repo owner/repo \
  --input issues.csv \
  --fields title,body,labels \
  --rate-limit 30/min

gh-api-toolkit batch-update-repos \
  --repos "repo1,repo2,repo3" \
  --settings '{"has_issues":true,"has_wiki":false}'

gh-api-toolkit batch-add-collaborators \
  --repo owner/repo \
  --users "alice,bob,carol" \
  --permission push

gh-api-toolkit batch-archive-repos \
  --org my-org \
  --filter "inactive:>180d" \
  --dry-run
```

批量操作安全机制:
- **预演模式**: `--dry-run`预览变更,不实际执行
- **速率控制**: 自动遵守API限速,可配置QPS
- **断点续传**: 失败时记录进度,支持从断点恢复
- **回滚支持**: 生成反向操作脚本,支持撤销
- **进度报告**: 实时显示进度与成功/失败计数

**输入**: 用户提供批量操作所需的指令和必要参数。
**处理**: 按照skill规范执行批量操作操作,遵循单一意图原则。
**输出**: 返回批量操作的执行结果,包含操作状态和输出数据。

### Webhook管理
```bash
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.repos/owner/repo/hooks

curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "config": {
      "url": "https://hooks.example.com/github",
      "content_type": "json",
      "secret": "'$WEBHOOK_SECRET'"
    },
    "events": ["issues", "pull_request", "push", "release"],
    "active": true
  }' \
  https://api.repos/owner/repo/hooks

curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.repos/owner/repo/hooks/123/pings

curl -X DELETE -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.repos/owner/repo/hooks/123
```

支持的事件类型:

| 事件类别 | 事件 | 说明 |
| --- | --- | --- |
| 仓库 | push, create, delete, fork, public | 仓库级别事件 |
| Issue | issues, issue_comment, label | Issue相关事件 |
| PR | pull_request, pull_request_review | PR相关事件 |
| Release | release, deployment | 发布相关事件 |
| Actions | workflow_run, workflow_job | 工作流事件 |
| 组织 | organization, member, team | 组织事件 |
| 安全 | security_advisory, secret_scanning_alert | 安全事件 |

**输入**: 用户提供Webhook管理所需的指令和必要参数。
**处理**: 按照skill规范执行Webhook管理操作,遵循单一意图原则。
**输出**: 返回Webhook管理的执行结果,包含操作状态和输出数据。

### GitHub Actions API
```bash
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.repos/owner/repo/actions/workflows

curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"ref":"main","inputs":{"environment":"staging"}}' \
  https://api.repos/owner/repo/actions/workflows/123/dispatches

curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.repos/owner/repo/actions/runs?status=in_progress"

curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.repos/owner/repo/actions/runs/123/cancel

curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.repos/owner/repo/actions/runs/123/rerun-failed-jobs

curl -L -H "Authorization: Bearer $GITHUB_TOKEN" \
  -o artifact.zip \
  https://api.repos/owner/repo/actions/artifacts/123/zip
```

**输入**: 用户提供GitHub Actions API所需的指令和必要参数。
**处理**: 按照skill规范执行GitHub Actions API操作,遵循单一意图原则。
**输出**: 返回GitHub Actions API的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 组织与团队管理
```bash
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.orgs/my-org/members?per_page=100"

curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"backend-team","description":"后端团队","privacy":"closed"}' \
  https://api.orgs/my-org/teams

curl -X PUT -H "Authorization: Bearer $GITHUB_TOKEN" \
  -d '{"role":"member"}' \
  https://api.orgs/my-org/teams/123/members/alice

curl -X PUT -H "Authorization: Bearer $GITHUB_TOKEN" \
  -d '{"permission":"push"}' \
  https://api.orgs/my-org/teams/123/repos/my-org/repo

curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.orgs/my-org/teams/123/repos
```

**输入**: 用户提供组织与团队管理所需的指令和必要参数。
**处理**: 按照skill规范执行组织与团队管理操作,遵循单一意图原则。
**输出**: 返回组织与团队管理的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 高级搜索
```bash
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.search/issues?q=bug+is:issue+is:open+org:my-org&sort=created&order=desc"

curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.search/code?q=TODO+language:python+org:my-org"

curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.search/repositories?q=topic:microservices+org:my-org&sort=stars"

curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.search/users?q=language:python+location:china"
```

**输入**: 用户提供高级搜索所需的指令和必要参数。
**处理**: 按照skill规范执行高级搜索操作,遵循单一意图原则。
**输出**: 返回高级搜索的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：全功能、集成工具、与组织管理、适合企业级集成场、工具包、专业版、是企业级、在免费版、基础能力上、组织与团队管理等、高级能力、核心能力、高效关联查询、支持复杂分页、批量创建、删除资源、含速率控制与回滚、订阅事件、配置回调、测试与调试、工作流管理、运行控制、产物下载、成员管理等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景1:企业级仓库群批量管理
用户意图: "组织有50个仓库,需要统一更新设置并添加协作者。"

实施方案:
1. 导出仓库列表(`gh-api-toolkit list-repos --org my-org`)
2. 准备设置变更JSON与协作者列表
3. 使用`--dry-run`预演
4. 执行`batch-update-repos`与`batch-add-collaborators`
5. 生成变更报告

### 场景2:DevOps平台集成
用户意图: "自建DevOps平台需要深度集成GitHub,包括事件订阅与工作流控制。"

实施方案:
1. 配置Webhook订阅`push`、`pull_request`、`workflow_run`事件
2. 平台接收Webhook,触发对应流水线
3. 通过Actions API触发/取消/重跑工作流
4. 使用GraphQL聚合多仓库状态展示

### 场景3:组织权限治理
用户意图: "审计组织权限,清理离职成员,调整团队结构。"

实施方案:
1. `gh-api-toolkit audit-members --org my-org`导出成员清单
2. 对比HR系统,标记离职成员
3. `batch-remove-members`移除离职成员
4. 调整团队结构,重新分配仓库权限
5. 生成权限变更报告

### 场景4:数据分析与BI
用户意图: "要做团队贡献分析,从GitHub拉取数据到BI平台。"

实施方案:
1. 使用GraphQL查询团队贡献(一次查询获取多维度数据)
2. 按周/月聚合PR、Issue、提交数据
3. 导出为CSV/JSON,导入BI平台
4. 设置定时任务,每日增量同步

## 不适用场景

以下场景GitHub API工具包(专业版)不适合处理：

- 逆向工程闭源API
- API安全渗透测试
- 非标准协议集成

## 触发条件

需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于非本工具能力范围的需求。

## 快速开始
### Step 1:安装专业版工具
```bash
pip install gh-api-toolkit[pro]

gh-api-toolkit version

export GITHUB_TOKEN="ghp_your_token"
gh-api-toolkit auth verify
```

### Step 2:GraphQL初体验
```bash
gh-api-toolkit graphql run --template repo_summary --vars '{"owner":"my-org","name":"my-repo"}'

gh-api-toolkit graphql run --query 'query { viewer { login repositories(first: 5) { nodes { name } } } }'
```

### Step 3:批量操作
```bash
cat > issues.csv << 'EOF'
title,body,labels
"Bug 1","描述1","bug"
"Bug 2","描述2","bug"
"Feature 1","描述3","enhancement"
EOF

gh-api-toolkit batch-create-issues --repo owner/repo --input issues.csv --dry-run

gh-api-toolkit batch-create-issues --repo owner/repo --input issues.csv
```

### Step 4:配置Webhook
```bash
gh-api-toolkit webhook add \
  --repo owner/repo \
  --url "https://hooks.example.com/github" \
  --events "issues,pull_request,push" \
  --secret "$WEBHOOK_SECRET"

gh-api-toolkit webhook test --repo owner/repo --event "issues"
```

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-L`: 命令参数,用于指定操作选项

## 示例
### 专业版配置文件
```json
{
  "edition": "pro",
  "auth": {
    "token_env": "GITHUB_TOKEN",
    "default_scope": ["repo", "workflow", "read:org", "admin:org_hook", "admin:repo_hook"]
  },
  "graphql": {
    "endpoint": "https://api.graphql",
    "timeout": 30,
    "complexity_limit": 500000,
    "cache_ttl": 300
  },
  "batch": {
    "rate_limit_qps": 10,
    "max_retries": 3,
    "checkpoint_interval": 10,
    "dry_run_by_default": true
  },
  "webhook": {
    "default_events": ["issues", "pull_request", "push"],
    "secret_env": "WEBHOOK_SECRET",
    "retry_count": 3
  },
  "actions": {
    "default_ref": "main",
    "artifact_retention": 90
  }
}
```

### 批量操作脚本示例
```python
from gh_api_toolkit import GitHubAPI, BatchProcessor

api = GitHubAPI(token=os.environ['GITHUB_TOKEN'])

issues = [
    {"title": f"任务{i}", "body": f"任务{i}的描述", "labels": ["task"]}
    for i in range(1, 101)
]

processor = BatchProcessor(api, rate_limit_qps=10)
results = processor.batch_create_issues(
    owner="my-org",
    repo="my-repo",
    issues=issues,
    dry_run=False,
    checkpoint_file="checkpoint.json"
)

print(f"成功: {results.success_count}, 失败: {results.failure_count}")
if results.failures:
    results.export_failures("failures.csv")
```

## 最佳实践
### GraphQL查询优化
| 优化项 | 说明 | 示例 |
| --- | --- | --- |
| 限制first参数 | 避免一次查太多 | `first: 10`而非`first: 1000` |
| 按需选字段 | 不查询多余字段 | 明确列出所需字段 |
| 使用别名 | 一次查多个仓库 | `repo1: repository(...) repo2: repository(...)` |
| 分页处理 | 使用cursor | `after: $cursor` |
| 复杂度控制 | 监控query cost | 避免深层嵌套 |

### 批量操作规范
1. **永远先预演**: `--dry-run`是必经步骤
2. **小批量验证**: 先执行5-10条,确认效果
3. **速率控制**: 默认10 QPS,可根据组织限制调整
4. **断点续传**: 大批量操作必须启用checkpoint
5. **失败处理**: 记录失败项,支持单独重试
6. **回滚预案**: 提前准备反向操作脚本

### Webhook安全
- **验证签名**: 使用`X-Hub-Signature-256`验证请求来源
- **HTTPS强制**: Webhook URL必须为HTTPS
- **Secret管理**: 通过环境变量配置,定期轮换
- **超时处理**: Webhook响应应在30秒内返回200
- **重试机制**: GitHub对失败请求会重试3次

### Actions API使用
- **触发前确认**: `workflow_dispatch`需确认参数正确
- **取消要及时**: 长时间运行的job及时取消,节省资源
- **产物清理**: 定期清理旧产物,避免占用配额
- **权限最小化**: token仅需`workflow` scope即可管理Actions

## 常见问题
### Q1: GraphQL查询复杂度超限怎么办?
A: GitHub限制单次查询复杂度≤500000点。优化方案: (1)减少`first`参数值; (2)拆分为多次查询; (3)使用分页(cursor); (4)避免深层嵌套。专业版工具会自动计算复杂度并提示。

### Q2: 批量操作中部分失败如何处理?
A: 专业版支持断点续传。失败项记录到`failures.csv`,可单独重试。检查失败原因(权限不足、资源不存在、限速等),修复后重试。

### Q3: Webhook签名验证失败怎么办?
A: 检查: (1)secret是否与GitHub配置一致; (2)签名算法是否为HMAC-SHA256; (3)是否对原始请求体(非解析后JSON)计算签名; (4)比较时使用constant-time comparison。

### Q4: Actions API触发工作流失败?
A: 常见原因: (1)工作流未配置`workflow_dispatch`触发器; (2)指定的`ref`不存在; (3)token缺少`workflow`scope; (4)inputs参数与工作流定义不匹配。

### Q5: 如何监控API用量?
A: 通过响应头`X-RateLimit-Remaining`与`X-RateLimit-Reset`监控。专业版工具自动记录用量,运行`gh-api-toolkit usage stats`查看趋势。GraphQL与REST共享5000/小时配额。

### Q6: 组织操作需要什么权限?
A: 组织级操作(管理成员、团队、仓库)需要`admin:org`scope。团队管理还需对应团队的maintainer角色。建议使用组织级App而非个人token。

### Q7: 如何导出搜索结果?
A: 搜索API返回`total_count`与`items`。使用分页参数`page`与`per_page`遍历。专业版支持`--export csv/json`直接导出全部结果。

### Q8: 专业版支持GitHub App吗?
A: 支持。配置App ID、私钥、installation ID后,自动获取installation token。相比PAT,App token更安全(可细粒度授权、自动过期)。

### Q9: 如何处理API版本兼容?
A: GitHub API通过`Accept`头指定版本(如`application/vnd.github+json`)。专业版工具会自动添加正确的Accept头。建议关注GitHub API变更日志,及时适配新版本。

### Q10: 大规模数据同步如何优化?
A: (1)使用GraphQL减少请求次数; (2)启用增量同步(基于`updated_at`过滤); (3)并行请求(遵守限速); (4)本地缓存已同步数据; (5)使用Webhook实时同步变更。

## 专业版特性
本专业版相比免费版新增以下能力:
- GraphQL API: 高效关联查询,支持复杂分页与模板库
- 批量操作: 批量CRUD,含速率控制、断点续传、回滚
- Webhook管理: 事件订阅、配置回调、测试与调试
- GitHub Actions API: 工作流触发、取消、重跑、产物下载
- 组织与团队管理: 成员管理、团队配置、权限设置
- 高级搜索: 复杂查询、跨仓库聚合、结果导出
- GitHub App支持: 细粒度授权、自动过期token
- 优先支持: 专属技术支持通道,SLA响应

## 定价
| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | REST基础CRUD | 个人试用 |
| 收费专业版 | ¥49.9/月 | 全功能+GraphQL+批量+Webhook+优先支持 | 团队/企业 |

专业版通过SkillHub SkillPay发布。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **网络**: 可访问GitHub API
- **Python**: 3.8+(运行gh-api-toolkit CLI)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| gh-api-toolkit[pro] | CLI工具 | 必需 | `pip install gh-api-toolkit[pro]` |
| curl | 命令行工具 | 必需 | 系统自带 |
| requests | Python库 | 必需 | 随gh-api-toolkit安装 |
| gql | Python库 | 必需 | 随gh-api-toolkit安装(GraphQL客户端) |
| GitHub账号 | 在线服务 | 必需 | 注册GitHub账号并生成PAT或App |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- **GitHub Token**: 通过环境变量`GITHUB_TOKEN`配置,禁止硬编码
- **Webhook Secret**: 通过环境变量`WEBHOOK_SECRET`配置
- **GitHub App私钥**: 存储于`~/.gh-api-toolkit/app-private-key.pem`(权限600)
- **Token权限**: 根据场景选择scope,企业场景推荐使用GitHub App
- **Token轮换**: PAT每90天轮换,App token自动过期
- **禁止**: 在SKILL.md或脚本中硬编码任何Token或私钥

### 可用性分类
- **分类**: MD+EXEC+CLI+API(Markdown指令+命令行工具+REST/GraphQL API)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent完成操作,核心功能通过gh-api-toolkit CLI或直接API调用

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需要API Key，无Key环境无法使用
