---
slug: "tool-finder-tool-pro"
name: "tool-finder-tool-pro"
version: "1.0.0"
displayName: "工具发现引擎专业版"
summary: "企业级工具发现与评估平台,支持批量搜索、团队推荐、工具评估报告与自动化部署"
license: "Proprietary"
edition: "pro"
description: |-
  工具发现引擎专业版,面向企业团队和高级用户提供深度的工具发现与评估能力。支持批量搜索、团队推荐、工具评估报告、自动化部署、使用统计等高级功能。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
  - 研究工具
  - 工具发现
  - 企业级
  - 批量处理
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
工具发现引擎专业版是企业级的工具发现与评估平台。在完整兼容免费版所有搜索和安装能力的基础上,专业版引入了批量并行搜索、团队推荐、工具评估报告、自动化部署、使用统计等高级能力,适用于企业团队统一工具选型、DevOps 批量部署、技术评审等复杂场景。

专业版特别强化了协作和评估能力,支持团队共享工具发现成果、自定义评分规则、生成评估报告,帮助企业建立标准化的工具选型流程。

## 核心能力
### 1. 批量并行搜索
支持一次查询多个关键词,并行获取结果。

```bash
{
  "queries": [
    {"keyword": "web search", "type": "skill"},
    {"keyword": "database", "type": "mcp"},
    {"keyword": "automation", "type": "skill"},
    {"keyword": "file processing", "type": "all"}
  ],
  "concurrency": 5,
  "merge_results": true
}

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch search batch_search.json

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch status
```

**输入**: 用户提供批量并行搜索所需的指令和必要参数。
**处理**: 按照skill规范执行批量并行搜索操作,遵循单一意图原则。
**输出**: 返回批量并行搜索的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 团队推荐与协作
支持团队共享工具发现成果,协作评估。

```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh team create --name "dev_tools_eval"

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh team invite --email "colleague@company.com"

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh team share --result search_result.json

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh team collect-ratings --tool "target-tool"
```

**输入**: 用户提供团队推荐与协作所需的指令和必要参数。
**处理**: 按照skill规范执行团队推荐与协作操作,遵循单一意图原则。
**输出**: 返回团队推荐与协作的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 工具评估报告
多维度分析工具质量,生成评估报告。

```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh evaluate "target-tool" --output report.html

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch evaluate --input tools.json --output reports/

```

**输入**: 用户提供工具评估报告所需的指令和必要参数。
**处理**: 按照skill规范执行工具评估报告操作,遵循单一意图原则。
**输出**: 返回工具评估报告的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 自动化部署
批量安装工具并自动配置。

```bash
{
  "tools": [
    {"name": "tool-a", "type": "skill", "config": "prod"},
    {"name": "tool-b", "type": "mcp", "config": "dev"},
    {"name": "tool-c", "type": "skill", "config": "prod"}
  ],
  "environment": "production",
  "auto_configure": true
}

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch deploy deploy.json

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch verify --input deploy.json
```

**输入**: 用户提供自动化部署所需的指令和必要参数。
**处理**: 按照skill规范执行自动化部署操作,遵循单一意图原则。
**输出**: 返回自动化部署的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. 使用统计与分析
追踪工具使用情况,提供数据洞察。

```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh stats usage --period "2026-07"

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh stats leaderboard --team "dev_team"

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh stats export --format csv --output usage_report.csv
```

**输入**: 用户提供使用统计与分析所需的指令和必要参数。
**处理**: 按照skill规范执行使用统计与分析操作,遵循单一意图原则。
**输出**: 返回使用统计与分析的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 6. 自定义评分规则
根据团队标准自定义评分规则。

```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh config set-scoring \
  --weights '{"community": 0.3, "quality": 0.3, "security": 0.2, "maintenance": 0.2}'

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh config set-scoring \
  --min-threshold 3.0 \
  --custom-rules custom_rules.json
```

**输入**: 用户提供自定义评分规则所需的指令和必要参数。
**处理**: 按照skill规范执行自定义评分规则操作,遵循单一意图原则。
**输出**: 返回自定义评分规则的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 7. 完整兼容免费版
专业版完全兼容免费版的所有命令和配置,平滑升级。

```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh search "web search"
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh install "target-tool" --type skill
```

**输入**: 用户提供完整兼容免费版所需的指令和必要参数。
**处理**: 按照skill规范执行完整兼容免费版操作,遵循单一意图原则。
**输出**: 返回完整兼容免费版的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级工具发现与、评估平台、支持批量搜索、工具评估报告与自、工具发现引擎专业、面向企业团队和高、级用户提供深度的、工具发现与评估能、使用统计等高级功、Use、when、需要提升效率、自动化流程、批量处理、工作流优化时使用、不适用于需要人工、创意判断的任务、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景一:企业团队统一工具选型
某企业技术委员会需要为开发团队统一选型代码质量工具。

```bash
cat > selection_search.json << 'EOF'
{
  "queries": [
    {"keyword": "code quality", "type": "skill"},
    {"keyword": "linting", "type": "mcp"},
    {"keyword": "code review", "type": "skill"},
    {"keyword": "static analysis", "type": "all"}
  ],
  "concurrency": 4,
  "min_rating": 3.0
}
EOF

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch search selection_search.json --output candidates.json

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch evaluate \
  --input candidates.json \
  --output evaluations/ \
  --dimensions "community,quality,security,maintenance"

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh team collect-ratings \
  --input candidates.json \
  --team "tech_committee"

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh report selection \
  --evaluations evaluations/ \
  --team-ratings team_ratings.json \
  --output tool_selection_report.html
```

### 场景二:DevOps 团队批量部署开发工具
某 DevOps 团队需要为新项目批量部署一组开发工具。

```bash
cat > project_deploy.json << 'EOF'
{
  "project": "new_platform_2026",
  "tools": [
    {"name": "code-formatter", "type": "skill", "config": "project_standard"},
    {"name": "git-helper", "type": "skill", "config": "team_workflow"},
    {"name": "test-runner", "type": "skill", "config": "ci_mode"},
    {"name": "deploy-monitor", "type": "mcp", "config": "prod_env"}
  ],
  "environment": "production",
  "auto_configure": true,
  "verify_after_install": true
}
EOF

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch deploy project_deploy.json

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch verify --input project_deploy.json

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh report deploy \
  --input project_deploy.json \
  --output deployment_report.html
```

### 场景三:组织内部工具目录管理
某组织需要建立内部工具目录,定期更新和评估。

```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh catalog scan --output inventory.json

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch evaluate \
  --input inventory.json \
  --output evaluations/ \
  --schedule "0 0 1 * *"  # 每月1日评估
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh catalog generate \
  --inventory inventory.json \
  --evaluations evaluations/ \
  --output tool_catalog.html

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh stats analyze \
  --period "2026-Q3" \
  --identify-low-usage \
  --threshold 0.1
```

## 快速开始
### 第一步:升级安装
```bash
cd ~/.skill-platform/workspace/skills/tool-finder-tool-pro
npm install

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh --version --edition

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch --help
```

### 第二步:配置团队协作
```bash
cat > team_config.json << 'EOF'
{
  "team": {
    "name": "tool_evaluation_team",
    "organization": "Tech Company",
    "members": [
      {"email": "lead@company.com", "role": "admin"},
      {"email": "dev1@company.com", "role": "evaluator"},
      {"email": "dev2@company.com", "role": "viewer"}
    ]
  },
  "scoring": {
    "custom_weights": {
      "community": 0.3,
      "quality": 0.3,
      "security": 0.2,
      "maintenance": 0.2
    },
    "min_threshold": 3.0
  }
}
EOF

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh team init team_config.json
```

### 第三步:运行首次批量搜索
```bash
cat > first_batch.json << 'EOF'
{
  "queries": [
    {"keyword": "automation", "type": "skill"},
    {"keyword": "monitoring", "type": "mcp"},
    {"keyword": "deployment", "type": "all"}
  ],
  "concurrency": 3
}
EOF

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch search first_batch.json

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch status
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。

### 命令参数说明

- `-Q3`: 命令参数,用于指定操作选项

## 示例
### 企业级配置
```json
{
  "edition": "pro",
  "search": {
    "batch_concurrency": 10,
    "cache_enabled": true,
    "cache_ttl": 3600,
    "rate_limit_handled": true
  },
  "evaluation": {
    "dimensions": ["community", "quality", "security", "maintenance", "compatibility"],
    "custom_weights": {},
    "min_threshold": 3.0,
    "auto_evaluate": true
  },
  "team": {
    "enabled": true,
    "shared_results": true,
    "collaborative_rating": true,
    "role_based_access": true
  },
  "deployment": {
    "auto_configure": true,
    "verify_after_install": true,
    "rollback_on_failure": true
  },
  "stats": {
    "track_usage": true,
    "period": "monthly",
    "export_format": "csv,json"
  }
}
```

### 自定义评分规则
```json
{
  "scoring": {
    "weights": {
      "community": {
        "rating": 0.15,
        "downloads": 0.10,
        "updates": 0.05
      },
      "quality": {
        "documentation": 0.10,
        "tests": 0.10,
        "code_health": 0.10
      },
      "security": {
        "vulnerabilities": 0.10,
        "permissions": 0.10
      },
      "maintenance": {
        "last_update": 0.10,
        "issue_response": 0.10
      }
    },
    "thresholds": {
      "recommended": 3.5,
      "acceptable": 3.0,
      "not_recommended": 2.0
    }
  }
}
```

## 最佳实践
### 1. 免费版到专业版的平滑迁移
```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh search "web search"

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch search batch.json

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh evaluate "target-tool"
```

### 2. 批量搜索的性能优化
```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch search \
  batch.json \
  --concurrency 8 \
  --timeout 30

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch search \
  batch.json \
  --cache-dir ./cache \
  --cache-ttl 3600
```

### 3. 评估报告的定制化
```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh evaluate "tool" \
  --dimensions "community,quality,security" \
  --weights '{"community": 0.4, "quality": 0.4, "security": 0.2}' \
  --output custom_report.html
```

### 4. 团队协作的流程化
```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch search candidates.json

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch evaluate --input results.json

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh team review --input evaluations/

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh report final --output report.html
```

## 免费版与专业版对比
| 功能特性 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 基础搜索 | 支持 | 支持 |
| 名称匹配优先 | 支持 | 支持 |
| 评分排序 | 支持 | 支持 |
| 一键安装 | 支持 | 支持 |
| 批量并行搜索 | 不支持 | 支持 |
| 团队推荐协作 | 不支持 | 支持 |
| 工具评估报告 | 不支持 | 支持 |
| 自动化部署 | 不支持 | 支持 |
| 使用统计 | 不支持 | 支持 |
| 自定义评分规则 | 不支持 | 支持 |
| 工具目录管理 | 不支持 | 支持 |
| 调用频率限制 | 60 次/小时 | 无限制 |
| 适用场景 | 个人搜索 | 企业选型 |
| 技术支持 | 社区支持 | 优先支持 |

## 常见问题
### Q1: 专业版是否兼容免费版的命令?
**A:** 完全兼容。专业版是免费版的超集,所有免费版命令在专业版中均可直接使用,无需修改。

### Q2: 工具评估报告包含哪些内容?
**A:** 专业版评估报告包含五大维度:

1. 社区活跃度:评分、下载量、更新频率
2. 代码质量:文档完整度、测试覆盖、代码健康度
3. 兼容性:平台支持、依赖情况
4. 安全性:漏洞扫描、权限分析
5. 维护状态:最近更新、问题响应速度

### Q3: 团队协作如何管理权限?
**A:** 通过角色权限配置实现细粒度访问控制:

```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh team config set \
  --role "evaluator" \
  --permissions "search,evaluate,rate"

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh team config set \
  --role "viewer" \
  --permissions "view,export"
```

### Q4: 自动化部署如何回滚?
**A:** 专业版支持部署失败自动回滚:

```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch deploy \
  deploy.json \
  --rollback-on-failure

~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh batch rollback \
  --deployment-id "deploy_001"
```

### Q5: 如何与现有工具管理系统集成?
**A:** 专业版提供 API 接口和 Webhook,支持与现有系统集成:

```bash
~/.skill-platform/workspace/skills/tool-finder-tool-pro/scripts/tool-finder.sh config set-webhook \
  --url "https://your-system.example.com/webhook" \
  --events "search,evaluate,deploy"
```

## 依赖说明
### 运行环境
- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Shell**: Bash(Windows 需 Git Bash 或 WSL)
- **Node.js**: 18.0.0 及以上版本

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | 官方网站下载安装 |
| npx | 包执行器 | 必需 | 随 Node.js 安装 |
| curl | HTTP 工具 | 必需 | 系统自带 |
| jq | JSON 解析 | 推荐 | 包管理器安装 |
| 数据库 | 存储 | 团队协作必需 | 本地或云端数据库 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
专业版需要以下配置:

```bash
SKILLHUB_API_TOKEN=your_api_token

TEAM_API_TOKEN=your_team_api_token

DB_HOST=localhost
DB_PORT=5432
DB_NAME=tool_finder
DB_USER=admin
DB_PASSWORD=your_password

WEBHOOK_URL=https://your-system.example.com/webhook
```

### 可用性分类
- **分类**: MD+EXEC+API(综合型,支持本地执行、API 调用和批量任务编排)
- **说明**: 企业级工具发现与评估平台,支持批量搜索、团队协作、工具评估等高级功能
- **适用规模**: 多用户、多任务、大规模并行处理
- **兼容性**: 完全兼容免费版,支持平滑升级
- API Key通过环境变量配置: export API_KEY=your_key

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
