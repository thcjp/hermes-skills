---
slug: repo-manager-pro
name: repo-manager-pro
version: "1.0.0"
displayName: 仓库管理器(专业版)
summary: 全功能仓库管理工具,含工作流管理、Release管理、批量操作、工具目录搜索与团队共享,适合企业级仓库治理。
license: MIT
edition: pro
description: |-
  仓库管理器(专业版)是企业级GitHub仓库管理工具,在免费版基础能力上,扩展工作流管理、Release管理、批量操作、工具目录搜索、自定义工具集成与团队共享配置等高级能力。

  核心能力:
  - 工作流管理: 列出、查看、取消、重新运行GitHub Actions工作流
  - Release管理: 创建、查看、发布Release与构建产物
  - 批量操作: 批量调用工具,含并行执行与结果聚合
  - 工具目录搜索: 全文搜索可用工具,快速定位
  - 自定义工具集成: 接入自有MCP server,扩展能力边界
  - 团队共享配置: 统一管理团队仓库权限与工具配置

  适用场景:
  - 企业级仓库群的统一管理
  - CI/CD工作流的集中监控与控制
  - Release发布流程的自动化
  - 团队协作与权限治理
  - 自定义工具生态的构建

  差异化: 相比免费版,新增工作流与Release管理能力,适合需要深度仓库治理的团队/企业。

  触发关键词: 仓库管理、工作流、Release管理、批量操作、MCP工具、工具搜索、企业治理、CI/CD控制
tags:
- GitHub
- 仓库管理
- 工作流
- 企业版
tools:
- read
- exec
---

# 仓库管理器(专业版)

全功能GitHub仓库管理工具,在免费版基础上,扩展工作流管理、Release管理、批量操作、工具目录搜索与团队共享,适合企业级仓库治理。

## 概述

在企业级仓库管理中,不仅需要管理Issue与PR,更需要控制CI/CD工作流、管理Release发布、批量处理资源,并构建统一的工具生态。专业版围绕"治理"与"效率"构建完整能力矩阵,帮助团队在多仓库环境中保持高效与可控。

专业版兼容免费版的所有工具调用,可直接升级,无需重新连接账号。

## 核心能力

### 工作流管理

通过MCP工具协议管理GitHub Actions工作流:

```bash
# 列出仓库的工作流
repo-manager call --tool "github_list_repository_workflows" --params '{
  "owner": "owner",
  "repo": "repo-name"
}'

# 列出工作流运行
repo-manager call --tool "github_list_workflow_runs" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "status": "in_progress"
}'

# 查看运行详情
repo-manager call --tool "github_get_a_workflow_run" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "run_id": 123456
}'

# 取消运行中的工作流(写操作)
repo-manager call --tool "github_cancel_workflow_run" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "run_id": 123456
}' --confirm

# 重新运行失败的工作流
repo-manager call --tool "github_rerun_workflow_failed_jobs" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "run_id": 123456
}' --confirm
```

工作流管理场景:

| 场景 | 工具 | 说明 |
| --- | --- | --- |
| 查看运行状态 | list_workflow_runs | 按状态过滤(in_progress/success/failure) |
| 定位失败原因 | get_a_workflow_run | 查看失败步骤与日志 |
| 取消卡住的运行 | cancel_workflow_run | 避免浪费资源 |
| 重跑失败步骤 | rerun_workflow_failed_jobs | 仅重跑失败部分,节省时间 |
| 触发工作流 | create_workflow_dispatch | 手动触发指定工作流 |

### Release管理

```bash
# 列出Release
repo-manager call --tool "github_list_releases" --params '{
  "owner": "owner",
  "repo": "repo-name"
}'

# 查看Release详情
repo-manager call --tool "github_get_a_release" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "release_id": 123
}'

# 创建Release(写操作)
repo-manager call --tool "github_create_a_release" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "tag_name": "v1.2.0",
  "name": "v1.2.0 - 性能优化版本",
  "body": "## 新增\n- 功能A\n## 修复\n- Bug #123\n## 优化\n- 性能提升30%",
  "draft": false,
  "prerelease": false
}' --confirm

# 更新Release
repo-manager call --tool "github_update_a_release" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "release_id": 123,
  "body": "更新发布说明"
}' --confirm

# 删除Release(高风险操作)
repo-manager call --tool "github_delete_a_release" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "release_id": 123
}' --confirm --force
```

### 批量操作

```bash
# 批量查询多个仓库的Issue
repo-manager batch-call --file batch_query.json --parallel 5

# batch_query.json 示例:
[
  {"tool": "github_list_issues_for_a_repository", "params": {"owner":"o","repo":"r1","state":"open"}},
  {"tool": "github_list_issues_for_a_repository", "params": {"owner":"o","repo":"r2","state":"open"}},
  {"tool": "github_list_issues_for_a_repository", "params": {"owner":"o","repo":"r3","state":"open"}}
]

# 批量创建Issue(从CSV)
repo-manager batch-create-issues \
  --repo owner/repo \
  --input issues.csv \
  --fields title,body,labels \
  --parallel 3 \
  --rate-limit 30/min

# 批量关闭带"stale"标签的Issue
repo-manager batch-close-stale \
  --repo owner/repo \
  --label stale \
  --older-than 30d \
  --dry-run
```

批量操作特性:
- **并行执行**: 支持配置并行度(默认3,最大10)
- **速率控制**: 自动遵守API限速,可配置QPS
- **断点续传**: 失败时记录进度,支持恢复
- **结果聚合**: 自动聚合多工具调用结果
- **预演模式**: `--dry-run`预览变更

### 工具目录搜索

```bash
# 全文搜索工具
repo-manager search-tools --query "issue label"

# 按集成过滤
repo-manager search-tools --query "branch" --integration github

# 按操作模式过滤
repo-manager search-tools --query "create" --mode write

# 查看工具详情(含whenToUse、askBefore、examples)
repo-manager describe-tool --tool "github_create_an_issue" --verbose
```

搜索能力:
- 全文索引所有工具的名称、描述、`whenToUse`
- 支持模糊匹配与语义搜索
- 返回工具的参数schema、示例、followups
- 按集成、操作模式、风险等级过滤

### 自定义工具集成

接入自有MCP server,扩展能力边界:

```bash
# 添加自定义MCP server
repo-manager integrations add \
  --name "my-ci-tool" \
  --endpoint "https://mcp.my-company.com/ci" \
  --auth-token "$MCP_TOKEN"

# 列出所有集成
repo-manager integrations list

# 查看自定义集成的工具
repo-manager list-tools --integration my-ci-tool

# 调用自定义工具
repo-manager call --tool "my_ci_trigger_pipeline" --params '{"project":"api"}' --confirm
```

### 团队共享配置

```bash
# 初始化团队配置
repo-manager team init --name "dev-team"

# 添加团队成员
repo-manager team add-members --members "alice,bob,carol"

# 共享仓库列表
repo-manager team share-repos --repos "owner/repo1,owner/repo2"

# 共享工具配置
repo-manager team share-config --file team-config.json

# 查看团队配置
repo-manager team show
```

## 使用场景

### 场景1:CI/CD集中监控

用户意图: "团队有5个仓库,需要集中监控所有CI运行状态。"

实施方案:
1. 配置团队共享的仓库列表
2. 使用批量操作查询所有仓库的工作流运行
3. 对失败运行自动创建Issue跟踪
4. 设置告警,失败时通知团队

```bash
# 批量查询所有仓库的工作流状态
repo-manager batch-call --file ci_monitor.json --parallel 5

# 对失败运行创建跟踪Issue
repo-manager batch-call --file create_tracking_issues.json --confirm
```

### 场景2:Release发布自动化

用户意图: "版本发布流程需要自动化,包括创建Release、通知团队、归档产物。"

实施方案:
1. 调用`github_create_a_release`创建Release
2. 自动生成变更日志(基于commit历史)
3. 上传构建产物到Release
4. 通知团队新版本发布
5. 归档旧版本

```bash
# 一键发布Release
repo-manager release publish \
  --repo owner/repo \
  --tag v1.2.0 \
  --auto-changelog \
  --upload-artifacts "dist/*.zip" \
  --notify-team
```

### 场景3:多仓库批量治理

用户意图: "组织有20个仓库,需要统一更新设置、清理stale Issue。"

实施方案:
1. 导出仓库列表
2. 使用`batch-update-repos`统一更新设置
3. 使用`batch-close-stale`清理过期Issue
4. 生成治理报告

```bash
# 预演批量清理
repo-manager batch-close-stale \
  --org my-org \
  --older-than 60d \
  --dry-run

# 执行清理
repo-manager batch-close-stale \
  --org my-org \
  --older-than 60d \
  --confirm

# 生成报告
repo-manager report governance --org my-org --period 30d --format pdf
```

### 场景4:自定义工具生态

用户意图: "我们有自建的CI系统,想通过统一的工具接口管理。"

实施方案:
1. 开发自有MCP server,封装CI系统能力
2. 通过`integrations add`接入
3. 在Agent会话中使用自然语言调用自定义工具
4. 与GitHub工具组合使用,形成完整工作流

## 快速开始

### 步骤1:升级到专业版

```bash
# 安装专业版插件
agent plugins install repo-manager-plugin[pro]

# 更新工具权限
agent config set tools.alsoAllow '["repo-manager-plugin"]' --strict-json

# 重启Agent会话
agent restart
```

### 步骤2:验证专业版功能

```bash
# 查看版本
repo-manager version

# 验证工作流工具可用
repo-manager search-tools --query "workflow"

# 验证Release工具可用
repo-manager search-tools --query "release"
```

### 步骤3:配置团队

```bash
# 初始化团队
repo-manager team init --name "dev-team"

# 添加成员与仓库
repo-manager team add-members --members "alice,bob,carol"
repo-manager team share-repos --repos "owner/repo1,owner/repo2"
```

### 步骤4:首次批量操作

```bash
# 批量查询多个仓库状态
repo-manager batch-call --file repos_status.json --parallel 3
```

## 配置示例

### 专业版配置文件

```json
{
  "edition": "pro",
  "integration": {
    "github": {
      "connected": true,
      "scope": ["repo", "workflow", "read:org"]
    }
  },
  "batch": {
    "default_parallel": 3,
    "max_parallel": 10,
    "rate_limit_qps": 10,
    "checkpoint_enabled": true,
    "dry_run_by_default": true
  },
  "search": {
    "index_enabled": true,
    "cache_ttl": 300,
    "fuzzy_match": true
  },
  "custom_integrations": [
    {
      "name": "my-ci-tool",
      "endpoint": "https://mcp.my-company.com/ci",
      "auth_token_env": "MCP_TOKEN"
    }
  ],
  "team": {
    "name": "dev-team",
    "members": ["alice", "bob", "carol"],
    "shared_repos": ["owner/repo1", "owner/repo2"]
  },
  "release": {
    "auto_changelog": true,
    "artifact_pattern": "dist/*.zip",
    "notify_on_publish": true
  }
}
```

### 批量操作配置示例

```json
// batch_ci_monitor.json
[
  {
    "tool": "github_list_workflow_runs",
    "params": {"owner":"my-org","repo":"repo1","status":"failure"},
    "label": "repo1-failures"
  },
  {
    "tool": "github_list_workflow_runs",
    "params": {"owner":"my-org","repo":"repo2","status":"failure"},
    "label": "repo2-failures"
  },
  {
    "tool": "github_list_workflow_runs",
    "params": {"owner":"my-org","repo":"repo3","status":"in_progress"},
    "label": "repo3-running"
  }
]
```

### Release发布脚本

```bash
#!/bin/bash
# 自动化Release发布流程

VERSION=$1
REPO="owner/repo"

# 1. 生成变更日志
CHANGELOG=$(repo-manager changelog generate --repo $REPO --since last-release)

# 2. 创建Release
repo-manager call --tool "github_create_a_release" --params "{
  \"owner\": \"owner\",
  \"repo\": \"repo\",
  \"tag_name\": \"$VERSION\",
  \"name\": \"$VERSION\",
  \"body\": \"$CHANGELOG\"
}" --confirm

# 3. 上传构建产物
repo-manager release upload-artifacts \
  --repo $REPO \
  --tag $VERSION \
  --files "dist/*.zip"

# 4. 通知团队
repo-manager team notify --message "Release $VERSION 已发布"
```

## 最佳实践

### 工作流管理策略

| 场景 | 策略 | 说明 |
| --- | --- | --- |
| 日常监控 | 定时批量查询状态 | 每小时查询所有仓库运行状态 |
| 失败处理 | 先查看日志再重跑 | 避免盲目重跑导致重复失败 |
| 资源清理 | 及时取消卡住的运行 | 避免浪费Actions配额 |
| 发布前检查 | 确认CI全绿 | 发布前检查所有仓库CI状态 |

### Release发布规范

1. **语义化版本号**: 遵循SemVer(major.minor.patch)
2. **变更日志**: 自动生成,基于commit历史
3. **预发布验证**: 先创建draft Release,验证后发布
4. **产物归档**: 构建产物上传到Release,保留至少90天
5. **通知机制**: 发布后自动通知团队
6. **回滚预案**: 保留上一版本产物,支持快速回滚

### 批量操作安全

- **永远先预演**: `--dry-run`是必经步骤
- **小批量验证**: 先执行3-5条,确认效果
- **并行度控制**: 默认3,根据API限速调整
- **断点续传**: 大批量操作必须启用checkpoint
- **结果核对**: 操作后核对数量,确保完整

### 自定义集成开发

- **遵循MCP工具协议**: 确保工具接口规范
- **参数schema完整**: 每个参数标注类型、必填、默认值
- **提供whenToUse**: 帮助Agent正确选择工具
- **安全标注**: 写操作标记`askBefore`,高风险标记`force`
- **示例丰富**: 每个工具提供2+使用示例

## 常见问题

### Q1: 工作流工具不可用怎么办?

A: 检查: (1)GitHub连接的scope是否包含`workflow`; (2)仓库是否启用了Actions; (3)插件版本是否为专业版; (4)用`search-tools --query workflow`验证工具是否存在。

### Q2: 批量操作中部分失败如何处理?

A: 专业版支持断点续传。失败项记录到`failures.json`,可单独重试。检查失败原因(权限、限速、资源不存在),修复后重试。

### Q3: Release创建后如何上传产物?

A: 使用`repo-manager release upload-artifacts --repo owner/repo --tag v1.0.0 --files "dist/*.zip"`。支持通配符,自动上传到Release的assets。

### Q4: 自定义MCP server如何开发?

A: 遵循MCP工具协议规范,实现工具注册、参数schema、执行接口。参考MCP工具生态的官方文档。开发完成后通过`integrations add`接入。

### Q5: 团队配置如何共享?

A: 使用`team share-config`导出配置JSON,团队成员通过`team import-config`导入。配置包含仓库列表、工具权限、告警规则,不含认证信息。

### Q6: 工具搜索结果不准怎么办?

A: 尝试: (1)使用更具体的关键词; (2)用英文搜索(工具名多为英文); (3)启用模糊匹配; (4)重建索引`repo-manager search rebuild-index`。

### Q7: 如何监控多个仓库的CI状态?

A: 使用批量操作,配置`batch_ci_monitor.json`,并行查询所有仓库的工作流运行状态。可设置定时任务,每小时执行一次,失败时告警。

### Q8: Release发布后能修改吗?

A: 可以。使用`github_update_a_release`更新标题、描述等。已上传的产物可单独删除或替换。但已发布的Release修改需谨慎,建议仅修改draft状态。

### Q9: 专业版支持GitHub Enterprise吗?

A: 支持。在集成配置中指定Enterprise Server的API endpoint,所有工具调用自动路由到Enterprise实例。

### Q10: 如何导出操作审计日志?

A: 运行`repo-manager audit log --period 30d --format csv --output audit.csv`,记录所有工具调用(含调用者、时间、参数、结果),支持合规审计。

## 专业版特性

本专业版相比免费版新增以下能力:
- 工作流管理: 列出、查看、取消、重跑GitHub Actions工作流
- Release管理: 创建、查看、更新、发布Release与构建产物
- 批量操作: 批量调用工具,含并行执行、断点续传、结果聚合
- 工具目录搜索: 全文搜索、模糊匹配、语义搜索
- 自定义工具集成: 接入自有MCP server,扩展能力边界
- 团队共享配置: 统一管理团队仓库权限与工具配置
- 操作审计: 完整的工具调用日志,支持合规审计
- 优先支持: 专属技术支持通道,SLA响应

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 基础仓库+Issue+PR管理 | 个人试用 |
| 收费专业版 | ¥49.9/月 | 全功能+工作流+Release+批量+优先支持 | 团队/企业 |

专业版通过SkillHub SkillPay发布。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **集成插件**: repo-manager-plugin[pro](通过MCP工具协议提供GitHub能力)
- **网络**: 可访问GitHub API与自定义MCP端点

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| repo-manager-plugin[pro] | 集成插件 | 必需 | `agent plugins install repo-manager-plugin[pro]` |
| GitHub账号 | 在线服务 | 必需 | 注册GitHub账号并完成OAuth授权(scope含workflow) |
| jq | 命令行工具 | 可选 | `brew install jq`(JSON处理) |
| 自定义MCP server | API服务 | 可选 | 自行开发,遵循MCP工具协议 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- **GitHub OAuth**: 通过集成面板完成,token由插件安全存储
- **自定义MCP server令牌**: 通过环境变量`MCP_TOKEN`配置,禁止硬编码
- **Token存储**: 加密存储于`~/.repo-manager/credentials.enc`(AES-256)
- **权限范围**: 建议包含`repo`、`workflow`、`read:org`
- **团队配置**: 共享配置不含认证信息,认证各自管理
- **禁止**: 在SKILL.md或脚本中硬编码任何Token

### 可用性分类
- **分类**: MD+EXEC+MCP工具+CLI(Markdown指令+命令行工具+MCP工具协议+批量操作)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent调用MCP工具执行GitHub操作,高级功能通过repo-manager CLI
