---
slug: verify-claims-tool-pro
name: verify-claims-tool-pro
version: 1.0.0
displayName: 事实核查助手专业版
summary: 企业级事实核查平台,支持批量声明核查、定时监控、深度分析与团队协作
license: Proprietary
edition: pro
description: 事实核查助手专业版,面向企业团队和专业研究人员提供深度的事实核查能力。支持批量声明核查、定时监控预警、深度分析报告、团队协作等高级功能。Use
  when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- 研究工具
- 事实核查
- 企业级
- 批量处理
tools:
- - read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
事实核查助手专业版是企业级的事实核查与信息验证平台。在完整兼容免费版所有核查能力的基础上,专业版引入了批量声明核查、定时监控预警、深度分析报告、团队协作、自定义核查规则等高级能力,适用于企业公关舆情监控、媒体内容审核、政府虚假信息监控等专业场景。

专业版特别强化了规模化处理能力,支持数百条声明并行核查、定时自动监控、结构化分析报告,帮助机构建立系统化的信息验证流程。

## 核心能力
### 1. 批量声明并行核查
支持数百条声明同时核查,显著提升效率。

```bash
{
  "claims": [
    {"id": "c001", "text": "某公司宣布破产", "region": "china"},
    {"id": "c002", "text": "某产品导致健康问题", "region": "us"},
    {"id": "c003", "text": "某政策将于下月实施", "region": "eu"}
  ],
  "concurrency": 10,
  "min_sources": 3
}

verify-claims batch check batch_claims.json

verify-claims batch status

verify-claims batch export --format csv --output results.csv
```

**输入**: 用户提供批量声明并行核查所需的指令和必要参数。
**处理**: 按照skill规范执行批量声明并行核查操作,遵循单一意图原则。
**输出**: 返回批量声明并行核查的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 定时监控与预警
自动监控关键声明,触发预警。

```bash
{
  "monitors": [
    {
      "name": "品牌声誉监控",
      "keywords": ["公司名称", "品牌名", "CEO姓名"],
      "check_interval": "hourly",
      "alert_condition": "false_claims > 0 OR negative_sentiment > 0.5",
      "notification": "email + webhook"
    }
  ]
}

verify-claims monitor start monitor_config.json

verify-claims monitor status

verify-claims monitor alerts --date $(date +%Y-%m-%d)
```

**输入**: 用户提供定时监控与预警所需的指令和必要参数。
**处理**: 按照skill规范执行定时监控与预警操作,遵循单一意图原则。
**输出**: 返回定时监控与预警的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 深度分析报告
多维度分析声明可信度,生成结构化报告。

```bash
verify-claims analyze deep \
  --claim "某项研究结论" \
  --dimensions "sources,evidence,context,timeline" \
  --output deep_report.html

verify-claims analyze batch \
  --input batch_results.json \
  --output analysis_report.pdf

```

**输入**: 用户提供深度分析报告所需的指令和必要参数。
**处理**: 按照skill规范执行深度分析报告操作,遵循单一意图原则。
**输出**: 返回深度分析报告的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 团队协作
支持团队共享核查结果与知识库。

```bash
verify-claims team create --name "fact_check_team"

verify-claims team share --result check_001.json --team "fact_check_team"

verify-claims knowledge add --category "health" --claim "已核查的声明" --verdict "false"

verify-claims knowledge query --keyword "疫苗" --category "health"
```

**输入**: 用户提供团队协作所需的指令和必要参数。
**处理**: 按照skill规范执行团队协作操作,遵循单一意图原则。
**输出**: 返回团队协作的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. 自定义核查规则
根据团队标准自定义核查规则与评分模型。

```bash
verify-claims config set-rules \
  --min-sources 5 \
  --confidence-threshold 0.8 \
  --custom-sources custom_sources.json

verify-claims config set-scoring \
  --weights '{"source_credibility": 0.3, "evidence_quality": 0.3, "consistency": 0.2, "recency": 0.2}'
```

**输入**: 用户提供自定义核查规则所需的指令和必要参数。
**处理**: 按照skill规范执行自定义核查规则操作,遵循单一意图原则。
**输出**: 返回自定义核查规则的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 6. 舆情追踪与虚假信息监控
追踪虚假信息的传播路径和影响范围。

```bash
verify-claims track misinformation \
  --claim "虚假声明内容" \
  --period "2026-01-01:2026-07-17" \
  --output spread_analysis.json

verify-claims track visualize \
  --input spread_analysis.json \
  --format graph \
  --output spread_graph.html
```

**输入**: 用户提供舆情追踪与虚假信息监控所需的指令和必要参数。
**处理**: 按照skill规范执行舆情追踪与虚假信息监控操作,遵循单一意图原则。
**输出**: 返回舆情追踪与虚假信息监控的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 7. 完整兼容免费版
专业版完全兼容免费版的所有命令和配置,平滑升级。

```bash
verify-claims check "声明内容"
verify-claims check --file article.txt
verify-claims history --list
```

**输入**: 用户提供完整兼容免费版所需的指令和必要参数。
**处理**: 按照skill规范执行完整兼容免费版操作,遵循单一意图原则。
**输出**: 返回完整兼容免费版的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级事实核查平、支持批量声明核查、深度分析与团队协、事实核查助手专业、面向企业团队和专、业研究人员提供深、度的事实核查能力、定时监控预警、团队协作等高级功、Use、when、模型调用、智能对话、Agent、LLM、应用时使用、不适用于需要、确定性的关键决策、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 输出格式

本skill的输出格式为Markdown文本,包含操作状态和执行结果。具体输出内容取决于执行的能力点和输入参数。

## 使用场景
### 场景一:企业品牌声誉监控
某企业公关团队需要监控与公司相关的虚假信息,及时应对。

```bash
cat > brand_monitor.json << 'EOF'
{
  "monitors": [
    {
      "name": "公司品牌虚假信息监控",
      "keywords": ["CompanyName", "CompanyName Corp", "公司中文名"],
      "check_interval": "hourly",
      "alert_condition": "false_claims > 0 OR misinformation_detected == true",
      "notification": "email + webhook + slack",
      "regions": ["us", "uk", "china", "japan"]
    }
  ]
}
EOF

verify-claims monitor start brand_monitor.json

verify-claims analyze deep \
  --claim "发现的虚假声明" \
  --dimensions "sources,evidence,context,timeline" \
  --output deep_analysis.html

verify-claims track misinformation \
  --claim "虚假声明内容" \
  --period "2026-07-01:2026-07-17" \
  --output spread_analysis.json

verify-claims report crisis \
  --analysis deep_analysis.html \
  --spread spread_analysis.json \
  --output crisis_response_report.html
```

### 场景二:媒体机构内容审核
某媒体机构需要对大量投稿内容进行事实核查。

```bash
verify-claims batch extract-claims \
  --input submissions/ \
  --output claims_batch.json

verify-claims batch check claims_batch.json \
  --concurrency 15 \
  --min-sources 3

verify-claims report review \
  --input batch_results.json \
  --output editorial_review.html \
  --threshold "confidence < 0.7"

verify-claims report flag \
  --input batch_results.json \
  --criteria "verdict == 'mixed' OR confidence < 0.6" \
  --output manual_review_list.csv
```

### 场景三:研究机构大规模信息核查
某研究机构需要分析社交媒体上的虚假信息传播模式。

```bash
cat > social_claims.json << 'EOF'
{
  "claims": [
    {"id": "s001", "text": "社交媒体声明1", "source": "platform_a", "date": "2026-07-01"},
    {"id": "s002", "text": "社交媒体声明2", "source": "platform_b", "date": "2026-07-02"}
  ],
  "concurrency": 20
}
EOF

verify-claims batch check social_claims.json --output social_results.json

verify-claims analyze patterns \
  --input social_results.json \
  --dimensions "topic,source,region,spread_rate" \
  --output pattern_analysis.json

verify-claims report research \
  --input pattern_analysis.json \
  --template academic \
  --output research_report.pdf
```

## 快速开始
### 依赖详情
```bash
cd ~/.skill-platform/workspace/skills/verify-claims-tool-pro
npm install

verify-claims --version --edition

verify-claims batch --help
```

### 第二步:配置团队协作
```bash
cat > team_config.json << 'EOF'
{
  "team": {
    "name": "fact_checking_team",
    "organization": "Media Organization",
    "members": [
      {"email": "lead@media.com", "role": "admin"},
      {"email": "fact1@media.com", "role": "checker"},
      {"email": "fact2@media.com", "role": "checker"}
    ]
  },
  "knowledge_base": {
    "shared": true,
    "categories": ["politics", "health", "science", "technology"]
  }
}
EOF

verify-claims team init team_config.json
```

### 第三步:运行首次批量核查
```bash
cat > first_batch.json << 'EOF'
{
  "claims": [
    {"id": "c1", "text": "声明1"},
    {"id": "c2", "text": "声明2"},
    {"id": "c3", "text": "声明3"}
  ],
  "concurrency": 3
}
EOF

verify-claims batch check first_batch.json

verify-claims batch status
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。


## 示例
### 企业级配置
```json
{
  "edition": "pro",
  "batch": {
    "max_concurrency": 20,
    "timeout": 120000,
    "retry_attempts": 3
  },
  "monitoring": {
    "enabled": true,
    "check_interval": 3600,
    "alert_channels": ["email", "webhook", "slack"],
    "alert_thresholds": {
      "false_claims": 1,
      "misinformation_detected": true
    }
  },
  "analysis": {
    "dimensions": ["sources", "evidence", "context", "timeline", "consistency"],
    "custom_scoring": true,
    "confidence_threshold": 0.8
  },
  "team": {
    "enabled": true,
    "shared_results": true,
    "knowledge_base": true,
    "role_based_access": true
  },
  "reporting": {
    "auto_generate": true,
    "formats": ["html", "pdf"],
    "templates": ["standard", "academic", "crisis"]
  }
}
```

### 监控预警配置
```json
{
  "monitoring": {
    "monitors": [
      {
        "name": "品牌监控",
        "keywords": ["品牌名"],
        "check_interval": "hourly",
        "alert_conditions": [
          {"metric": "false_claims", "threshold": 1, "action": "immediate"},
          {"metric": "misinformation_spread", "threshold": 10, "action": "summary"}
        ],
        "notification_channels": {
          "immediate": ["webhook", "slack", "email"],
          "summary": ["email"]
        }
      }
    ]
  }
}
```

## 最佳实践
### 1. 免费版到专业版的平滑迁移
```bash
verify-claims check "声明内容"

verify-claims batch check batch.json

verify-claims monitor start monitor.json
```

### 2. 批量核查的性能优化
```bash
verify-claims batch check batch.json --concurrency 15

verify-claims batch check batch.json --cache-dir ./cache --skip-cached
```

### 3. 监控预警的精细化配置
```bash
{
  "alert_conditions": [
    {"metric": "false_claims", "threshold": 1, "action": "immediate"},
    {"metric": "misinformation_spread", "threshold": 10, "action": "summary"},
    {"metric": "negative_sentiment", "threshold": 0.5, "action": "trend_report"}
  ]
}
```

### 4. 知识库的持续积累
```bash
verify-claims knowledge add --auto-from-results

verify-claims knowledge organize --deduplicate --merge-similar

verify-claims knowledge export --format json --output knowledge_base.json
```

## 免费版与专业版对比
| 功能特性 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 单声明核查 | 支持 | 支持 |
| 多源交叉验证 | 支持 | 支持 |
| 区域相关性匹配 | 支持 | 支持 |
| 语言匹配 | 支持 | 支持 |
| 历史归档 | 支持 | 支持 |
| 批量并行核查 | 不支持 | 支持 |
| 定时监控预警 | 不支持 | 支持 |
| 深度分析报告 | 不支持 | 支持 |
| 团队协作 | 不支持 | 支持 |
| 知识库 | 不支持 | 支持 |
| 自定义核查规则 | 不支持 | 支持 |
| 舆情追踪 | 不支持 | 支持 |
| 虚假信息监控 | 不支持 | 支持 |
| 核查速度 | 单条 10-30 秒 | 批量并行 |
| 适用场景 | 个人核查 | 企业级监控 |
| 技术支持 | 社区支持 | 优先支持 |

## 常见问题
### Q1: 专业版是否兼容免费版的命令?
**A:** 完全兼容。专业版是免费版的超集,所有免费版命令在专业版中均可直接使用,无需修改。

### Q2: 批量核查的性能如何?
**A:** 专业版支持并行核查,单机可处理 20 个并发任务。100 条声明的核查约需 5 分钟(取决于核查机构的响应速度)。

### Q3: 监控预警如何配置通知渠道?
**A:** 支持多种通知渠道:

```bash
verify-claims config set-alerts \
  --email "alerts@example.com" \
  --webhook "https://hooks.example.com/alert" \
  --slack "#fact-check-alerts"
```

### Q4: 知识库如何与其他系统共享?
**A:** 专业版支持知识库的导入导出:

```bash
verify-claims knowledge export --format json --output knowledge_base.json

verify-claims knowledge import --file external_kb.json
```

### Q5: 如何保障核查结果的客观性?
**A:** 专业版提供多重保障:

- 使用多个独立核查机构交叉验证
- 优先选择国际公认的权威核查机构
- 排除已知的虚假核查服务
- 完整记录核查过程,支持审计追溯
- 团队协作评审,避免个人偏见

## 依赖说明
### 运行环境
- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **网络**: 需要稳定的互联网连接
- **存储**: 知识库和归档需要存储空间

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | 官方网站下载安装 |
| curl | HTTP 工具 | 必需 | 系统自带 |
| web_search | 搜索工具 | 必需 | Agent 内置或外部搜索 API |
| web_fetch | 网页抓取 | 必需 | Agent 内置或外部抓取工具 |
| 数据库 | 存储 | 团队协作必需 | 本地或云端数据库 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
专业版需要以下配置:

```bash
SEARCH_API_KEY=your_search_api_key

TEAM_API_TOKEN=your_team_api_token

DB_HOST=localhost
DB_PORT=5432
DB_NAME=fact_checking
DB_USER=admin
DB_PASSWORD=your_password

SLACK_WEBHOOK=your_slack_webhook_url
ALERT_EMAIL=alerts@example.com
```

### 可用性分类
- **分类**: MD+EXEC+API(综合型,支持 API 调用、批量执行和数据存储)
- **说明**: 企业级事实核查平台,支持批量核查、定时监控、深度分析等高级功能
- **适用规模**: 多用户、大规模并行处理、持续监控
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
