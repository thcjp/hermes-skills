---
slug: notion-cli-tool-pro
name: notion-cli-tool-pro
version: "1.0.0"
displayName: Notion命令行(专业版)
summary: 企业级Notion命令行工具,支持多工作空间、文件上传、Schema管理、批量操作与审计日志,适合团队与企业规模化使用。
license: MIT
edition: pro
description: |-
  Notion命令行(专业版)是面向团队与企业的全功能Notion操作Skill,在免费版基础上新增多工作空间管理、文件上传、Schema管理、页面移动、批量操作、模板管理、自定义输出与审计日志等高级能力。

  核心能力:

  - 多工作空间Profile,同时管理多个Notion账户
  - 文件上传(图片、PDF、文档),MIME自动检测
  - 数据库Schema管理(增删改属性列、重命名)
  - 跨数据库页面移动
  - 批量操作(批量创建/更新/删除),带检查点
  - 页面模板列表与使用
  - 自定义输出格式(Jinja2模板)
  - 审计日志,全操作可追溯
  - 多级缓存与并行处理,支撑高并发

  适用场景:

  - 中大型企业的Notion工作空间自动化
  - SaaS产品的Notion数据双向同步
  - 跨团队的项目管理与任务调度
  - 数据迁移与备份恢复

  差异化:相比免费版,专业版聚焦"全、稳、可控"三字诀,提供企业级的多账户治理与批量处理能力。所有写操作支持幂等控制与审计追溯,可满足金融、咨询等强合规行业的使用要求。

  触发关键词:企业Notion、多工作空间、文件上传、Schema管理、批量操作、页面移动、审计日志
tags:
- 集成工具
- 企业Notion
- 命令行
tools:
- read
- exec
---

# Notion命令行(专业版)

一个面向团队与企业的全功能Notion操作Skill,在免费版基础上扩展了多工作空间管理、文件上传、Schema管理、页面移动、批量操作、模板管理、自定义输出与审计日志等高级能力,适合规模化使用场景。

## 概述

本Skill提供从Notion数据查询、批量处理到Schema管理的端到端命令行解决方案。专业版默认支持企业级SLA(99.9%可用性),所有写操作支持幂等控制与审计追溯,可满足金融、咨询、教育等强合规行业的使用要求。

## 核心能力

### 与免费版能力对比

| 能力 | 免费版 | 专业版 |
|------|--------|--------|
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

## 使用场景

### 场景一:企业多工作空间管理

集团企业拥有多个Notion工作空间(各部门独立),需要统一管理。

```bash
# 1. 添加多个工作空间Profile
notion workspace add work --key ntn_work_key
notion workspace add personal --key ntn_personal_key
notion workspace add research --key ntn_research_key

# 2. 列出所有工作空间
notion workspace list

# 3. 切换工作空间
notion workspace use work

# 4. 跨工作空间操作
notion query tasks --workspace personal
notion -w work add projects --prop "Name=Q2 Plan"

# 5. 在指定工作空间初始化
notion init --workspace research --key ntn_research_key
```

### 场景二:数据库Schema演进

产品团队需要根据业务发展,动态调整Notion数据库的属性列。

```bash
# 1. 查看当前Schema
notion --json query tasks --limit 1 | jq '.properties | keys'

# 2. 添加新属性列
notion db-update tasks --add-prop "Priority:select"
notion db-update tasks --add-prop "Rating:number"
notion db-update tasks --add-prop "DueDate:date"

# 3. 修改属性列(重命名)
notion db-update tasks --title "任务管理库(2026版)"

# 4. 删除过期属性列
notion db-update tasks --remove-prop "OldColumn"

# 5. 创建新数据库(带Schema)
notion db-create <parent-page-id> "新项目库" \
  --prop "Name:title" \
  --prop "Status:select" \
  --prop "Priority:select" \
  --prop "DueDate:date"

# 6. 查看可用模板
notion templates tasks
```

### 场景三:批量数据迁移与文件上传

企业需要将大量本地数据迁移到Notion,并上传相关附件。

```bash
# 1. 批量创建页面(从CSV)
notion batch-add tasks --input ./data/tasks.csv \
  --checkpoint --interval 100 \
  --idempotency-key "migration-2026-07"

# 2. 批量更新页面状态
notion batch-update tasks \
  --filter "Status=Done" \
  --prop "Archived=true" \
  --parallel 5

# 3. 批量归档过期页面
notion batch-delete tasks \
  --filter "DueDate<2026-01-01" \
  --confirm

# 4. 上传文件到页面
notion upload tasks --filter "Name=季度报告" ./reports/q2-report.pdf
notion upload <page-id> ./screenshots/dashboard.png

# 5. 跨数据库移动页面
notion move tasks --filter "Status=Done" --to archive
notion move tasks --filter "Status=Done" --to <page-id>
```

## 快速开始

预计上手时间:<120秒(适合中等复杂度工具)。

### 步骤1:升级到专业版

```bash
notion license apply --key $PRO_LICENSE_KEY
```

### 步骤2:配置多工作空间

```bash
notion workspace add work --key ntn_work_key
notion workspace add personal --key ntn_personal_key
notion workspace list
```

### 步骤3:体验Schema管理

```bash
notion db-update tasks --add-prop "Priority:select"
```

## 配置示例

### 多工作空间配置

```yaml
# ~/.notion-cli/config.yaml
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

default_workspace: work

batch:
  defaultPageSize: 100
  maxRetries: 3
  backoff: exponential
  checkpoint: true
  parallel: 5

cache:
  l1:
    enabled: true
    ttl: 60
    maxSize: 10000
  l2:
    enabled: true
    backend: redis
    ttl: 300

audit:
  enabled: true
  retention: 180d
  export: [json, csv]

dualIds:
  mode: auto  # auto | manual
  prefer: database_id  # database_id | data_source_id
```

### 批量操作示例

```bash
# 批量创建(从CSV文件)
notion batch-add tasks --input ./data/tasks.csv \
  --checkpoint --parallel 5

# tasks.csv格式:
# Name,Status,Priority
# 任务1,Todo,High
# 任务2,Done,Medium
# 任务3,Todo,Low

# 批量更新
notion batch-update tasks \
  --input ./data/updates.json \
  --parallel 5 --on-failure continue

# 批量归档
notion batch-delete tasks \
  --filter "DueDate<2026-01-01" \
  --confirm --dry-run  # 先预览,确认后去掉--dry-run

# 查看批量任务进度
notion batch status --job-id <jobId>

# 断点续传
notion batch resume --job-id <jobId>
```

### 文件上传示例

```bash
# 上传到指定页面
notion upload <page-id> ./report.pdf
notion upload <page-id> ./screenshot.png
notion upload <page-id> ./document.docx

# 按别名+筛选上传
notion upload tasks --filter "Name=季度报告" ./q2-report.pdf

# 支持的文件类型
# 图片:png, jpg, jpeg, gif, webp, svg
# 文档:pdf, docx, xlsx, pptx
# 文本:txt, md, csv, json, yaml
# 压缩:zip, tar, gz
```

### Schema管理示例

```bash
# 查看当前属性
notion props tasks --filter "Name=Sample"

# 添加属性列
notion db-update tasks --add-prop "Priority:select"
notion db-update tasks --add-prop "Rating:number"
notion db-update tasks --add-prop "Tags:multi_select"
notion db-update tasks --add-prop "DueDate:date"

# 删除属性列
notion db-update tasks --remove-prop "OldColumn"

# 重命名数据库
notion db-update tasks --title "任务管理库(2026版)"

# 创建带Schema的数据库
notion db-create <parent-page-id> "新项目库" \
  --prop "Name:title" \
  --prop "Status:select" \
  --prop "Priority:select" \
  --prop "StartDate:date" \
  --prop "EndDate:date" \
  --prop "Assignee:people" \
  --prop "Tags:multi_select"

# 列出页面模板
notion templates tasks
```

### 页面移动示例

```bash
# 按别名移动到归档库
notion move tasks --filter "Status=Done" --to archive

# 按别名移动到指定页面下
notion move tasks --filter "Status=Done" --to <page-id>

# 跨工作空间移动(需指定源与目标)
notion move tasks --filter "Name=迁移任务" \
  --from work --to personal
```

### 自定义输出模板

```jinja2
{# ./templates/task-report.md.j2 #}
# {{ properties.Name.title[0].text.content }}

- **状态**:{{ properties.Status.select.name }}
- **优先级**:{{ properties.Priority.select.name }}
- **截止日期**:{{ properties.DueDate.date.start }}
- **负责人**:{{ properties.Assign.people | map(attribute='name') | join(", ") }}

## 内容
{% for block in blocks %}
{% if block.type == "paragraph" %}
{{ block.paragraph.rich_text | map(attribute='text.content') | join("") }}
{% elif block.type == "heading_2" %}
## {{ block.heading_2.rich_text | map(attribute='text.content') | join("") }}
{% endif %}
{% endfor %}

## 评论
{% for comment in comments %}
- **{{ comment.created_by.name }}** ({{ comment.created_time }}):{{ comment.rich_text | map(attribute='text.content') | join("") }}
{% endfor %}
```

```bash
# 应用自定义模板
notion get tasks --filter "Name=Ship feature" \
  --transform ./templates/task-report.md.j2
```

### 审计日志查询

```bash
# 查询所有写操作
notion audit logs --action write --limit 100

# 按工作空间查询
notion audit logs --workspace work --limit 50

# 按时间范围查询
notion audit logs --start "2026-07-01" --end "2026-07-31"

# 按资源查询
notion audit logs --resource-type page --resource-id <pageId>

# 导出审计日志
notion audit export --format csv --output ./audit-2026-07.csv
```

## 最佳实践

1. **多工作空间按业务隔离**:工作空间与业务线对应,避免混用
2. **批量操作使用幂等键**:每次批量请求携带`Idempotency-Key`,失败重试不产生重复数据
3. **Schema变更先dry-run**:`--dry-run`预览影响范围,确认后执行
4. **文件上传注意大小限制**:单文件不超过5MB,大文件建议先压缩
5. **页面移动前确认目标**:跨数据库移动会改变属性映射,确认目标Schema兼容
6. **审计日志保留180天以上**:满足等保2.0与GDPR的日志留存要求
7. **多级缓存合理配置**:L1缓存(60秒)应对热点查询,L2缓存(300秒)应对冷启动
8. **并行控制避免频率限制**:`--parallel 5`避免触发Notion API频率限制
9. **自定义模板统一输出**:团队共用一套Jinja2模板,保证输出格式一致

## 性能优化策略

### 多级缓存架构

```
查询请求 → L1缓存(进程内,60s) → L2缓存(Redis,300s) → Notion API
              ↓ 命中                ↓ 命中
              返回                   返回
```

- **L1缓存**:进程内LRU,容量10000条,TTL 60秒
- **L2缓存**:Redis集群,TTL 300秒,支持主动失效
- **命中率监控**:命中率<80%时告警

### 批量处理与检查点

```
批量请求 → 分片(每片100条) → 并行执行(并发5) → 检查点记录
                                    ↓ 失败
                                 指数退避重试(最多3次)
                                    ↓ 仍失败
                                 记录失败项,继续下一片
```

### 双ID自动处理

Notion API 2025-09-03使用双ID(database_id + data_source_id),专业版自动处理:

```bash
# 自动模式(默认):内部自动切换双ID
notion query tasks  # 无需关心ID类型

# 手动模式:显式指定
notion query tasks --id-type database_id
notion query tasks --id-type data_source_id
```

## 多平台集成示例

### 与`PostgreSQL`数据仓库同步

```bash
# Notion数据同步到PostgreSQL做深度分析
notion sync-to-warehouse \
  --source tasks \
  --destination postgresql://user:pass@host:5432/notion_db \
  --mode incremental \
  --schedule "0 4 * * *"
```

### 与企业微信集成

```bash
# 任务变更推送到企业微信群
notion notify tasks \
  --filter "Status=Done" \
  --webhook https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx \
  --template wecom
```

### 与对象存储集成

```bash
# 导出归档页面到对象存储
notion export tasks \
  --filter "Status=Archived" \
  --format markdown \
  --destination s3://your-bucket/notion-archive/
```

## 版本升级迁移指南

### 从免费版升级到专业版

1. 应用专业版License,功能自动解锁
2. 原有别名与配置自动继承,无需迁移
3. 启用多工作空间前,建议先梳理各工作空间的API Key
4. 启用审计日志前,需要配置日志存储位置与保留策略
5. 启用多级缓存前,确保Redis服务可用

```bash
# 触发历史操作审计日志回填
notion audit backfill --start "2026-01-01"

# 重新发现所有工作空间的别名
notion init --workspace work
notion init --workspace personal
```

## 常见问题

### Q1: 多工作空间如何切换?

A: 1)用`notion workspace use <name>`切换默认;2)用`-w <name>`或`--workspace <name>`临时指定。

### Q2: 批量操作失败如何重试?

A: 使用`Idempotency-Key`重发同一批请求,系统跳过已成功部分。也可通过`batch status --job-id`查看进度,用`batch resume --job-id`断点续传。

### Q3: Schema变更会影响现有数据吗?

A: 添加属性列不影响现有数据(新列为空)。删除属性列会导致该列数据丢失,建议先`--dry-run`预览。重命名数据库仅改变显示名,不影响数据。

### Q4: 文件上传支持哪些格式?

A: 支持图片(png/jpg/jpeg/gif/webp/svg)、文档(pdf/docx/xlsx/pptx)、文本(txt/md/csv/json/yaml)、压缩(zip/tar/gz)。单文件不超过5MB。

### Q5: 跨工作空间移动页面会丢失数据吗?

A: 不会。但目标数据库的Schema需要与源兼容(属性名与类型匹配),不匹配的属性会被丢弃。建议移动前先对比Schema。

### Q6: 双ID如何处理?

A: 专业版默认自动处理,无需关心。在`auto`模式下,系统根据操作类型自动选择合适的ID。需要手动控制时,用`--id-type`指定。

### Q7: 自定义模板支持哪些语法?

A: 支持Jinja2完整语法,包括变量、条件、循环、过滤器、宏等。

### Q8: 审计日志可以导出吗?

A: 可以。支持按时间、操作类型、资源ID、工作空间筛选,导出为JSON或CSV。

### Q9: 多级缓存如何主动失效?

A: 通过`notion cache invalidate --alias tasks`主动失效,或在页面更新时自动失效相关缓存。

### Q10: 专业版的SLA承诺是什么?

A: 99.9%可用性,故障4小时响应,数据可恢复性RPO<15分钟、RTO<4小时。

## 故障排查表

| 症状 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 批量操作部分失败 | 个别数据格式错误 | 查看failedItems,修正后用幂等键重试 | 高 |
| Schema变更失败 | 属性名冲突或类型不兼容 | 检查现有属性,用`props`命令查看 | 高 |
| 文件上传失败 | 文件过大或格式不支持 | 检查文件大小(<5MB)与格式 | 中 |
| 跨工作空间移动失败 | Schema不兼容 | 对比源与目标Schema,调整后重试 | 中 |
| 多工作空间切换异常 | API Key失效或权限不足 | 检查Key有效性,确认Integration权限 | 高 |
| 缓存命中率下降 | 缓存Key设计不合理 | 调整Key粒度与TTL,监控命中率 | 低 |
| 审计日志缺失 | 日志存储未配置 | 检查`audit.enabled`与存储路径 | 低 |

## 专业版特性

本专业版相比免费版新增以下能力:

- 多工作空间Profile:无限制同时管理多个Notion账户
- 文件上传:图片/PDF/文档/文本/压缩,自动MIME检测
- 数据库Schema管理:增删改属性列、重命名数据库
- 跨数据库页面移动:支持按别名与跨工作空间移动
- 批量操作:万级批量处理,带检查点与失败重试
- 页面模板管理:列表与使用
- 自定义输出格式:Jinja2模板灵活转换数据
- 审计日志:全操作可追溯,支持导出与筛选
- 多级缓存:L1进程内 + L2 Redis,带命中率监控
- 并行控制:批量任务自动并行,提升吞吐量
- 双ID自动处理:database_id与data_source_id自动切换
- 优先支持:4小时响应工单,专属技术经理

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | 0元 | 核心功能 + 单工作空间 | 个人试用、小型项目 |
| 收费专业版 | 39.9元/月 或 399元/年 | 全功能 + 多工作空间 + 批量 + Schema管理 + 优先支持 | 团队/企业规模化使用 |

专业版通过SkillHub SkillPay发布,支持按月订阅或一次性年付(享8折优惠)。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+(用于运行CLI工具)
- **Python**: 3.8+(可选,用于辅助脚本与ETL)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
