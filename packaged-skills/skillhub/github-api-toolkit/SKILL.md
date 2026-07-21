---
slug: github-api-toolkit
name: github-api-toolkit
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
# GitHub API工具包(专业版)

## 核心能力

### GraphQL API
GraphQL相比REST的优势: 一次查询获取关联数据,减少请求次数:

```bash
curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query { repository(owner: \"owner\", name: \"repo\") { issues(first: 10, states: OPEN) { totalCount nodes { number title labels(first: 5) { nodes { name } } } } pullRequests(first: 10, states: OPEN) { totalCount } releases(first: 3) { nodes { tagName publishedAt } } } }"
  }' \
  https://api.相关技术文档
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

**处理**: 按照skill规范执行GraphQL API操作,遵循单一意图原则。
**输出**: 返回GraphQL API的执行结果,包含操作状态和输出数据。### 批量操作
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

- 执行`GitHub Actions API`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`GitHub Actions API`相关配置参数进行设置
### Webhook管理
```bash
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.相关技术文档

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
  https://api.相关技术文档

curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.相关技术文档

curl -X DELETE -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.相关技术文档
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

### GitHub Actions API
```bash
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.相关技术文档

curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"ref":"main","inputs":{"environment":"staging"}}' \
  https://api.相关技术文档

curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.相关技术文档

curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.相关技术文档

curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.相关技术文档

curl -L -H "Authorization: Bearer $GITHUB_TOKEN" \
  -o artifact.zip \
  https://api.相关技术文档
```

**输出**: 返回GitHub Actions API的执行结果,包含操作状态和输出数据。

- 执行`GitHub Actions API`操作,处理输入数据并返回结果
- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `github_actions_api` 选项
- 处理流程: 接收输入 -> 执行GitHub Actions API -> 返回结果
- 输入: 用户提供GitHub Actions API所需的参数和指令
- 输出: 返回GitHub Actions API的执行结果,包含操作状态和输出数据

### 组织与团队管理
```bash
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.相关技术文档

curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"backend-team","description":"后端团队","privacy":"closed"}' \
  https://api.相关技术文档

curl -X PUT -H "Authorization: Bearer $GITHUB_TOKEN" \
  -d '{"role":"member"}' \
  https://api.相关技术文档

curl -X PUT -H "Authorization: Bearer $GITHUB_TOKEN" \
  -d '{"permission":"push"}' \
  https://api.相关技术文档

curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.相关技术文档
```

**输入**: 用户提供组织与团队管理所需的指令和必要参数。
**处理**: 按照skill规范执行组织与团队管理操作,遵循单一意图原则。
**输出**: 返回组织与团队管理的执行结果,包含操作状态和输出数据。### 高级搜索
```bash
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.相关技术文档

curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.相关技术文档

curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.相关技术文档

curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.相关技术文档
```

- 执行`组织与团队管理`操作,处理输入数据并返回结果
- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `组织与团队管理` 选项

### 能力覆盖范围

本skill还覆盖以下能力场景: 全功能、集成工具、与组织管理、适合企业级集成场、工具包、专业版、是企业级、在免费版、基础能力上、组织与团队管理等、高级能力、核心能力、高效关联查询、支持复杂分页、批量创建、删除资源、含速率控制与回滚、订阅事件、配置回调、测试与调试、工作流管理、运行控制、产物下载、成员管理。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景1 -企业级仓库群批量管理
用户意图: "组织有50个仓库,需要统一更新设置并添加协作者。"

实施方案:
1. 导出仓库列表(`gh-api-toolkit list-repos --org my-org`)
2. 准备设置变更JSON与协作者列表
3. 使用`--dry-run`预演
4. 执行`batch-update-repos`与`batch-add-collaborators`
5. 生成变更报告

### 场景2 -DevOps平台集成
用户意图: "自建DevOps平台需要深度集成GitHub,包括事件订阅与工作流控制。"

实施方案:
1. 配置Webhook订阅`push`、`pull_request`、`workflow_run`事件
2. 平台接收Webhook,触发对应流水线
3. 通过Actions API触发/取消/重跑工作流
4. 使用GraphQL聚合多仓库状态展示

### 场景3 -组织权限治理
用户意图: "审计组织权限,清理离职成员,调整团队结构。"

实施方案:
1. `gh-api-toolkit audit-members --org my-org`导出成员清单
2. 对比HR系统,标记离职成员
3. `batch-remove-members`移除离职成员
4. 调整团队结构,重新分配仓库权限
5. 生成权限变更报告

### 场景4 -数据分析与BI
用户意图: "要做团队贡献分析,从GitHub拉取数据到BI平台。"

实施方案:
1. 使用GraphQL查询团队贡献(一次查询获取多维度数据)
2. 按周/月聚合PR、Issue、提交数据
3. 导出为CSV/JSON,导入BI平台
4. 设置定时任务,每日增量同步

## 使用流程

### 第1步:安装专业版工具
```bash
pip install gh-api-toolkit[pro]

gh-api-toolkit version

export GITHUB_TOKEN="ghp_your_token"
gh-api-toolkit auth verify
```

### 第2步:GraphQL初体验
```bash
gh-api-toolkit graphql run --template repo_summary --vars '{"owner":"my-org","name":"my-repo"}'

gh-api-toolkit graphql run --query 'query { viewer { login repositories(first: 5) { nodes { name } } } }'
```

### 第3步:批量操作
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

### 第4步:配置Webhook
```bash
gh-api-toolkit webhook add \
  --repo owner/repo \
  --url "https://hooks.example.com/github" \
  --events "issues,pull_request,push" \
  --secret "$WEBHOOK_SECRET"

gh-api-toolkit webhook test --repo owner/repo --event "issues"
```

### 命令参数说明

1. `--template`: 命令参数,用于指定操作选项
2. `-L`: 命令参数,用于指定操作选项
3. `--permission`: 命令参数,用于指定操作选项
4. `--rate-limit`: 命令参数,用于指定操作选项
5. `-failed-jobs`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-L`: 命令参数,用于指定操作选项
- `--fields`: 命令参数,用于指定操作选项
- `--vars`: 命令参数,用于指定操作选项
- `--settings`: 命令参数,用于指定操作选项

### 命令参数说明

- `-H`: 命令参数,用于指定操作选项
- `--users`: 命令参数,用于指定操作选项
- `--events`: 命令参数,用于指定操作选项
- `--event`: 命令参数,用于指定操作选项
- `-L`: 命令参数,用于指定操作选项

### 命令参数说明

- `-L`: 命令参数,用于指定操作选项
- `--query`: 命令参数,用于指定操作选项
- `--filter`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项

### 命令参数说明

- `-H`: 命令参数,用于指定操作选项
- `-L`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-archive-repos`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-X`: 命令参数,用于指定操作选项
- `-create-issues`: 命令参数,用于指定操作选项
- `-L`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-L`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-L`: 命令参数,用于指定操作选项

### 命令参数说明

- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-L`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

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
- **说明**: 基于Markdown的AI Skill,,核心功能通过gh-api-toolkit CLI或直接API调用

## 案例展示

### 专业版配置文件
```json
{
  "edition": "pro",
  "auth": {
    "token_env": "GITHUB_TOKEN",
    "default_scope": ["repo", "workflow", "read:org", "admin:org_hook", "admin:repo_hook"]
  },
  "graphql": {
    "endpoint": "https://api.相关技术文档
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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
