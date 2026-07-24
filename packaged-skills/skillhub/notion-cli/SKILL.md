---
slug: "notion-cli"
name: "notion-cli"
version: 1.0.1
displayName: "Notion命令行(专业版)"
summary: "企业级Notion命令行工具,支持多工作空间、文件上传、Schema管理、批量操作与审计日志,适合团队与企业规模化使用。"
license: "Proprietary"
edition: "pro"
description: |-
  Notion命令行(专业版)是面向团队与企业的全功能Notion操作Skill,在免费版基础上新增多工作空间管理、文件上传、Schema管理、页面移动、批量操作、模板管理、自定义输出与审计日志等高级能力。核心能力:

  - 多工作空间Profile,同时管理多个Notion账户
  - 文件上传(图片、PDF、文档),MIME自动检测
  - 数据库Schema管理(增删改属性列、重命名)
  - 跨数据库页面移动
  - 批量操作(批量创建/更新/删除),带检查点
  - 页面模板列表与使用
  - 自定义输出格式(Jinja2模板)
  - ...
tags:
  - 集成工具
  - 企业Notion
  - 命令行
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "exec", "glob", "grep"]
tags: "工具,效率,自动化"
category: "Automation"
---
# Notion命令行(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Notion命令行(专业版)Schema管理 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

### 与免费版能力对比
| 能力 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 工作空间数量 | 单个 | 无限制 |
| 文件上传 | 不支持 | 图片/PDF/文档,自动MIME |
| Schema管理 | 不支持 | 增删改属性列、重命名 |
| 页面移动 | 不支持 | 跨数据库移动 |
| 批量操作 | 不支持 | 万级批量,带检查点 |
| 模板管理 | 不支持 | 列表与使用 |
| 自定义输出 | 不支持 | Jinja2模板 |
| 审计日志 | 不支持 | 全操作可追溯 |
| 缓存策略 | 无 | 多级缓存+命中率监控 |
| 并发控制 | 串行 | 并行+速率限制 |
| 双ID处理 | 自动 | 自动+手动切换 |
| 技术支持 | 社区 | 优先工单(4小时响应) |

**输入**: 用户提供与免费版能力对比所需的指令和必要参数.
### 工作空间数量

针对工作空间数量,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供工作空间数量相关的配置参数、输入数据和处理选项.
**输出**: 返回工作空间数量的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`工作空间数量`的配置文档进行参数调优
### 文件上传

针对文件上传,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供文件上传相关的配置参数、输入数据和处理选项.
**输出**: 返回文件上传的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`文件上传`的配置文档进行参数调优
#
## 适用场景

### 场景一:企业多工作空间管理
集团企业拥有多个Notion工作空间(各部门独立),需要统一管理.
```bash
notion workspace add work --key ntn_work_key
notion workspace add personal --key ntn_personal_key
notion workspace add research --key ntn_research_key
# ...
notion workspace list
# ...
notion workspace use work
# ...
notion query tasks --workspace personal
notion -w work add projects --prop "Name=Q2 Plan"
# ...
notion init --workspace research --key ntn_research_key
```

### 场景二:数据库Schema演进
产品团队需要根据业务发展,动态调整Notion数据库的属性列.
```bash
notion --json query tasks --limit 1 | jq '.properties | keys'
# ...
notion db-update tasks --add-prop "Priority:select"
notion db-update tasks --add-prop "Rating:number"
notion db-update tasks --add-prop "DueDate:date"
# ...
notion db-update tasks --title "任务管理库(2026版)"
# ...
notion db-update tasks --remove-prop "OldColumn"
# ...
notion db-create <parent-page-id> "新项目库" \
  --prop "Name:title" \
  --prop "Status:select" \
  --prop "Priority:select" \
  --prop "DueDate:date"
# ...
notion templates tasks
```

### 场景三:批量数据迁移与文件上传
企业需要将大量本地数据迁移到Notion,并上传相关附件.
```bash
notion batch-add tasks --input ./data/tasks.csv \
  --checkpoint --interval 100 \
  --idempotency-key "migration-2026-07"
# ...
notion batch-update tasks \
  --filter "Status=Done" \
  --prop "Archived=true" \
  --parallel 5
# ...
notion batch-delete tasks \
  --filter "DueDate<2026-01-01" \
  --confirm
# ...
notion upload tasks --filter "Name=季度报告" ./reports/q2-report.pdf
notion upload <page-id> ./screenshots/dashboard.png
# ...
notion move tasks --filter "Status=Done" --to archive
notion move tasks --filter "Status=Done" --to <page-id>
```

## 使用流程

预计上手时间:<120秒(适合中等复杂度工具).
### 第1步:升级到专业版
```bash
notion license apply --key $PRO_LICENSE_KEY
```

### 第2步:配置多工作空间
```bash
notion workspace add work --key ntn_work_key
notion workspace add personal --key ntn_personal_key
notion workspace list
```

### 第3步:体验Schema管理
```bash
notion db-update tasks --add-prop "Priority:select"
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | notion-cli处理的内容输入 |, 默认: 全部维度 |
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

| 症状 | 可能原因 | 解决方案 | 优先级 |
|:---:|:---:|:---:|:---:|
| 批量操作部分失败 | 个别数据格式错误 | 查看failedItems,修正后用幂等键 | 高 |
| Schema变更失败 | 属性名冲突或类型不兼容 | 检查现有属性,用`props`命令查看 | 高 |
| 文件上传失败 | 文件过大或格式不支持 | 检查文件大小(<5MB)与格式 | 中 |
| 跨工作空间移动失败 | Schema不兼容 | 对比源与目标Schema,调整后 | 中 |
| 多工作空间切换异常 | API Key失效或权限不足 | 检查Key有效性,确认Integration权限 | 高 |
| 缓存命中率下降 | 缓存Key设计不合理 | 调整Key粒度与TTL,监控命中率 | 低 |
| 审计日志缺失 | 日志存储未配置 | 检查`audit.enabled`与存储路径 | 低 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+(用于运行CLI工具)
- **Python**: 3.8+(可选,用于辅助脚本与ETL)

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| notion-cli-tool CLI | 命令行工具 | 必需 | `npm install -g notion-cli-tool` |
| Notion Integration | 在线服务 | 必需 | 通过Notion开发者平台创建 |
| Redis | 缓存服务 | 可选 | 用于多级缓存,自建或使用云服务 |
| `PostgreSQL` | 数据库 | 可选 | 用于数据仓库同步,版本12+ |
| 对象存储 | 存储服务 | 可选 | 用于归档导出,兼容S3协议 |

### API Key 配置
- **NOTION_API_KEY**: 各工作空间的Integration Token,通过`workspace add`命令配置
- **PRO_LICENSE_KEY**: 专业版License,通过环境变量或配置文件传入
- **Redis连接串**: 通过`REDIS_URL`环境变量传入
- **加密密钥**: 通过KMS服务管理,禁止在配置文件中明文存储
- **安全建议**: 所有Key遵循"最小权限 + 定期轮换"原则,建议每90天轮换一次

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

## 案例展示

### 多工作空间配置
```yaml
workspaces:
  - name: work
    key: ${NOTION_WORK_KEY}
    aliases:
      tasks: "abc123-def456-..."
      projects: "ghi789-jkl012-..."
  - name: personal
    key: ${NOTION_PERSONAL_KEY}
    aliases:
      reading-list: "mno345-pqr678-..."
  - name: research
    key: ${NOTION_RESEARCH_KEY}
# ...
default_workspace: work
# ...
batch:
  defaultPageSize: 100
  maxRetries: 3
  backoff: exponential
  checkpoint: true
  parallel: 5
# ...
cache:
  l1:
    enabled: true
    ttl: 60
    maxSize: 10000
  l2:
    enabled: true
    backend: redis
    ttl: 300
# ...
audit:
  enabled: true
  retention: 180d
  export: [json, csv]
# ...
dualIds:
  mode: auto  # auto | manual
  prefer: database_id  # database_id | data_source_id
```

### 批量操作示例
```bash
notion batch-add tasks --input ./data/tasks.csv \
  --checkpoint --parallel 5
# ...
notion batch-update tasks \
  --input ./data/updates.json \
  --parallel 5 --on-failure continue
# ...
notion batch-delete tasks \
  --filter "DueDate<2026-01-01" \
  --confirm --dry-run  # 先预览,确认后去掉--dry-run
notion batch status --job-id <jobId>
# ...
notion batch resume --job-id <jobId>
```

### 文件上传示例
```bash
notion upload <page-id> ./report.pdf
notion upload <page-id> ./screenshot.png
notion upload <page-id> ./document.docx
# ...
notion upload tasks --filter "Name=季度报告" ./q2-report.pdf
# ...
```

### Schema管理示例
```bash
notion props tasks --filter "Name=Sample"
# ...
notion db-update tasks --add-prop "Priority:select"
notion db-update tasks --add-prop "Rating:number"
notion db-update tasks --add-prop "Tags:multi_select"
notion db-update tasks --add-prop "DueDate:date"
# ...
notion db-update tasks --remove-prop "OldColumn"
# ...
notion db-update tasks --title "任务管理库(2026版)"
# ...
notion db-create <parent-page-id> "新项目库" \
  --prop "Name:title" \
  --prop "Status:select" \
  --prop "Priority:select" \
  --prop "StartDate:date" \
  --prop "EndDate:date" \
  --prop "Assignee:people" \
  --prop "Tags:multi_select"
# ...
notion templates tasks
```

### 页面移动示例
```bash
notion move tasks --filter "Status=Done" --to archive
# ...
notion move tasks --filter "Status=Done" --to <page-id>
# ...
notion move tasks --filter "Name=迁移任务" \
  --from work --to personal
```

### 自定义输出模板
```jinja2
{# ./templates/task-report.md.j2 #}
- **状态**:notion-cli
- **优先级**:notion-cli
- **截止日期**:相关信息
- **负责人**:notion-cli
# ...
{% for block in blocks %}
{% if block.type == "paragraph" %}
cli 相关配置参数
{% elif block.type == "heading_2" %}
{% endif %}
{% endfor %}
# ...
{% for comment in comments %}
- **notion-cli** (相关信息):cli 相关配置参数
{% endfor %}
```

```bash
notion get tasks --filter "Name=Ship feature" \
  --transform ./templates/task-report.md.j2
```

### 审计日志查询
```bash
notion audit logs --action write --limit 100
# ...
notion audit logs --workspace work --limit 50
# ...
notion audit logs --start "2026-07-01" --end "2026-07-31"
# ...
notion audit logs --resource-type page --resource-id <pageId>
# ...
notion audit export --format csv --output ./audit-2026-07.csv
```

## 常见问题

### Q1: 多工作空间如何切换?
A: 1)用`notion workspace use <name>`切换默认;2)用`-w <name>`或`--workspace <name>`临时指定.
### Q2: 批量操作失败如何重试?
A: 使用`Idempotency-Key`重发同一批请求,系统跳过已成功部分。也可通过`batch status --job-id`查看进度,用`batch resume --job-id`断点续传.
### Q3: Schema变更会影响现有数据吗?
A: 添加属性列不影响现有数据(新列为空)。删除属性列会导致该列数据丢失,建议先`--dry-run`预览。重命名数据库仅改变显示名,不影响数据.
### Q4: 文件上传支持哪些格式?
A: 支持图片(png/jpg/jpeg/gif/webp/svg)、文档(pdf/docx/xlsx/pptx)、文本(txt/md/csv/json/yaml)、压缩(zip/tar/gz)。单文件不超过5MB.
### Q5: 跨工作空间移动页面会丢失数据吗?
A: 不会。但目标数据库的Schema需要与源兼容(属性名与类型匹配),不匹配的属性会被丢弃。建议移动前先对比Schema.
### Q6: 双ID如何处理?
A: 专业版默认自动处理,无需关心。在`auto`模式下,系统根据操作类型自动选择合适的ID。需要手动控制时,用`--id-type`指定.
### Q7: 自定义模板支持哪些语法?
A: 支持Jinja2完整语法,包括变量、条件、循环、过滤器、宏等.
### Q8: 审计日志可以导出吗?
A: 可以。支持按时间、操作类型、资源ID、工作空间筛选,导出为JSON或CSV.
### Q9: 多级缓存如何主动失效?
A: 通过`notion cache invalidate --alias tasks`主动失效,或在页面更新时自动失效相关缓存.
### Q10: 专业版的SLA承诺是什么?
A: 99.9%可用性,故障4小时响应,数据可恢复性RPO<15分钟、RTO<4小时.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

