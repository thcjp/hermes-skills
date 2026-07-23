---
slug: "repo-manager"
name: "repo-manager"
version: "1.0.0"
displayName: "仓库管理器(专业版)"
summary: "全功能仓库管理工具,含工作流管理、Release管理、批量操作、工具目录搜索与团队共享,适合企业级仓库治理。"
license: "Proprietary"
edition: "pro"
description: |-
  仓库管理器(专业版)是企业级GitHub仓库管理工具,在免费版基础能力上,扩展工作流管理、Release管理、批量操作、工具目录搜索、自定义工具集成与团队共享配置等高级能力。核心能力:
  - 工作流管理: 列出、查看、取消、重新运行GitHub Actions工作流
  - Release管理: 创建、查看、发布Release与构建产物
  - 批量操作: 批量调用工具,含并行执行与结果聚合
  - 工具目录搜索: 全文搜索可用工具,快速定位
  - 自定义工具集成: 接入自有MCP server,扩展能力边界
  - 团队共享配置: 统一管理团...
tags:
  - GitHub
  - 仓库管理
  - 工作流
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
# 仓库管理器(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 仓库管理器(专业版)全功能仓库管理 | 不支持 | 支持 |
| 仓库管理器(专业版)含工作流管理 | 不支持 | 支持 |
| 仓库管理器(专业版)Release管理 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |

## 核心能力

### 工作流管理
通过MCP工具协议管理GitHub Actions工作流:

> 详细代码示例已移至 `references/detail.md`

工作流管理场景:

| 场景 | 工具 | 说明 |
|:-----|:-----|:-----|
| 查看运行状态 | list_workflow_runs | 按状态过滤(in_progress/success/failure) |
| 定位失败原因 | get_a_workflow_run | 查看失败步骤与日志 |
| 取消卡住的运行 | cancel_workflow_run | 避免浪费资源 |
| 重跑失败步骤 | rerun_workflow_failed_jobs | 仅重跑失败部分,节省时间 |
| 触发工作流 | create_workflow_dispatch | 手动触发指定工作流 |

**输入**: 用户提供Release管理所需的指令和必要参数.
**处理**: 解析Release管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Release管理的解析响应,包含完成状态码、响应数据和完成日志。### 批量任务
```bash
repo-manager batch-call --file batch_query.json --parallel 5
# ...
[
  {"tool": "github_list_issues_for_a_repository", "params": {"owner":"o","repo":"r1","state":"open"}},
  {"tool": "github_list_issues_for_a_repository", "params": {"owner":"o","repo":"r2","state":"open"}},
  {"tool": "github_list_issues_for_a_repository", "params": {"owner":"o","repo":"r3","state":"open"}}
]
# ...
repo-manager batch-create-issues \
  --repo owner/repo \
  --input issues.csv \
  --fields title,body,labels \
  --parallel 3 \
  --rate-limit 30/min
# ...
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
repo-manager search-tools --query "issue label"
# ...
repo-manager search-tools --query "branch" --integration github
# ...
repo-manager search-tools --query "create" --mode write
# ...
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
repo-manager integrations add \
  --name "my-ci-tool" \
  --endpoint "https://mcp.my-company.com/ci" \
  --auth-token "$MCP_TOKEN"
# ...
repo-manager integrations list
# ...
repo-manager list-tools --integration my-ci-tool
# ...
repo-manager call --tool "my_ci_trigger_pipeline" --params '{"project":"api"}' --confirm
```- 验证返回数据的完整性和格式正确性
- 参考`自定义工具集成`的配置文档进行参数调优
### 团队共享配置
```bash
repo-manager team init --name "dev-team"
# ...
repo-manager team add-members --members "alice,bob,carol"
# ...
repo-manager team share-repos --repos "owner/repo1,owner/repo2"
# ...
repo-manager team share-config --file team-config.json
# ...
repo-manager team show
```

**输入**: 用户提供团队共享配置所需的指令和必要参数.
**处理**: 解析团队共享配置的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回团队共享配置的处理结果,包含执行状态码、结果数据和执行日志.
#
## 适用场景

### 场景1 -CI/CD集中监控
用户意图: "团队有5个仓库,需要集中监控所有CI运行状态。"

实施方案:
1. 配置团队共享的仓库列表
2. 使用批量操作查询所有仓库的工作流运行
3. 对失败运行自动创建Issue跟踪
4. 设置告警,失败时通知团队

```bash
repo-manager batch-call --file ci_monitor.json --parallel 5
# ...
repo-manager batch-call --file create_tracking_issues.json --confirm
```

### 场景2 -Release发布自动化
用户意图: "版本发布流程需要自动化,包括创建Release、通知团队、归档产物。"

实施方案:
1. 调用`github_create_a_release`创建Release
2. 自动生成变更日志(基于commit历史)
3. 上传构建产物到Release
4. 通知团队新版本发布
5. 归档旧版本

```bash
repo-manager release publish \
  --repo owner/repo \
  --tag v1.2.0 \
  --auto-changelog \
  --upload-artifacts "dist/*.zip" \
  --notify-team
```

### 场景3 -多仓库批量治理
用户意图: "组织有20个仓库,需要统一更新设置、清理stale Issue。"

实施方案:
1. 导出仓库列表
2. 使用`batch-update-repos`统一更新设置
3. 使用`batch-close-stale`清理过期Issue
4. 生成治理报告

```bash
repo-manager batch-close-stale \
  --org my-org \
  --older-than 60d \
  --dry-run
# ...
repo-manager batch-close-stale \
  --org my-org \
  --older-than 60d \
  --confirm
# ...
repo-manager report governance --org my-org --period 30d --format pdf
```

### 场景4 -自定义工具生态
用户意图: "我们有自建的CI系统,想通过统一的工具接口管理。"

实施方案:
1. 开发自有MCP server,封装CI系统能力
2. 通过`integrations add`接入
3. 在Agent会话中使用自然语言调用自定义工具
4. 与GitHub工具组合使用,形成完整工作流

## 使用流程

### 第1步:升级到专业版
```bash
agent plugins install repo-manager-plugin[pro]
# ...
agent config set tools.alsoAllow '["repo-manager-plugin"]' --strict-json
# ...
agent restart
```

### 第2步:验证专业版功能
```bash
repo-manager version
# ...
repo-manager search-tools --query "workflow"
# ...
repo-manager search-tools --query "release"
```

### 第3步:配置团队
```bash
repo-manager team init --name "dev-team"
# ...
repo-manager team add-members --members "alice,bob,carol"
repo-manager team share-repos --repos "owner/repo1,owner/repo2"
```

### 第4步:首次批量操作
```bash
repo-manager batch-call --file repos_status.json --parallel 3
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | repo-manager处理的内容输入 |,  |
| content | string | 否 | repo-manager处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "manager 相关配置参数",
    result: "manager 相关配置参数",
    result: "manager 相关配置参数",
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

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **集成插件**: repo-manager-plugin[pro](通过MCP工具协议提供GitHub能力)
- **网络**: 可访问GitHub API与自定义MCP端点

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1: 工作流工具不可用怎么办?
A: 检查: (1)GitHub连接的scope是否包含`workflow`; (2)仓库是否启用了Actions; (3)插件版本是否为专业版; (4)用`search-tools --query workflow`验证工具是否存在.
### Q2: 批量操作中部分失败如何处理?
A: 专业版支持断点续传。失败项记录到`failures.json`,可单独重试。检查失败原因(权限、限速、资源不存在),修复后重试.
### Q3: Release创建后如何上传产物?
A: 使用`repo-manager release upload-artifacts --repo owner/repo --tag v1.0.0 --files "dist/*.zip"`。支持通配符,自动上传到Release的assets.
### Q4: 自定义MCP server如何开发?
A: 遵循MCP工具协议规范,实现工具注册、参数schema、执行接口。参考MCP工具生态的官方文档。开发完成后通过`integrations add`接入.
### Q5: 团队配置如何共享?
A: 使用`team share-config`导出配置JSON,团队成员通过`team import-config`导入。配置包含仓库列表、工具权限、告警规则,不含认证信息.
### Q6: 工具搜索结果不准怎么办?
A: 尝试: (1)使用更具体的关键词; (2)用英文搜索(工具名多为英文); (3)启用模糊匹配; (4)重建索引`repo-manager search rebuild-index`.
### Q7: 如何监控多个仓库的CI状态?
A: 使用批量操作,配置`batch_ci_monitor.json`,并行查询所有仓库的工作流运行状态。可设置定时任务,每小时执行一次,失败时告警.
### Q8: Release发布后能修改吗?
A: 可以。使用`github_update_a_release`更新标题、描述等。已上传的产物可单独删除或替换。但已发布的Release修改需谨慎,建议仅修改draft状态.
### Q9: 专业版支持GitHub Enterprise吗?
A: 支持。在集成配置中指定Enterprise Server的API endpoint,所有工具调用自动路由到Enterprise实例.
### Q10: 如何导出操作审计日志?
A: 运行`repo-manager audit log --period 30d --format csv --output audit.csv`,记录所有工具调用(含调用者、时间、参数、结果),支持合规审计.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

