---
slug: smart-crawler-pro
name: smart-crawler-pro
version: "1.0.0"
displayName: 智能爬虫(专业版)
summary: 企业级知识库爬取与检索平台,支持多工作空间、分布式调度、增量索引、全文检索与自定义导出,适合团队与企业规模化使用。
license: Proprietary
edition: pro
description: |-
  智能爬虫(专业版)是面向团队与企业的全功能知识库爬取Skill,在免费版基础上新增多工作空间管理、分布式调度、增量索引、全文检索引擎、自定义导出等高级能力。核心能力:

  - 多工作空间并行归档,支持团队级权限隔离
  - 分布式调度,多节点并行爬取,支撑万级页面规模
  - 增量索引,仅更新变更部分,同步效率提升10倍
  - 全文检索引擎,支持中文分词、同义词、模糊匹配
  - 自定义导出(Markdown/PDF/HTML/EPUB),带模板系统
  - 定时自动同步,支持cron表达式与事件触发
  - 多级缓存与查询优化,支撑高并发检索...
tags:
- 集成工具
- 企业检索
- 数据平台
tools:
  - - read
- exec
---
# 智能爬虫(专业版)

一个面向团队与企业的全功能知识库爬取Skill,在免费版基础上扩展了多工作空间管理、分布式调度、增量索引、全文检索引擎、自定义导出等高级能力,适合规模化使用场景。

## 概述

本Skill提供从知识库爬取、索引构建到检索服务的端到端解决方案。专业版默认支持企业级SLA(99.9%可用性),万级页面检索响应时间<100ms,所有操作全程审计可追溯,可满足金融、医疗、教育等强合规行业的使用要求。

## 核心能力

### 与免费版能力对比

| 能力 | 免费版 | 专业版 |
|------|--------|--------|
| 工作空间数量 | 单个 | 无限制 |
| 同步方式 | 桌面/API | 桌面/API/Webhook触发 |
| 索引更新 | 全量 | 增量(仅变更部分) |
| 调度能力 | 手动 | 定时cron + 事件触发 |
| 检索方式 | 关键词+基础SQL | 全文检索+高级SQL+语义检索 |
| 分布式 | 不支持 | 多节点并行 |
| 导出格式 | 不支持 | Markdown/PDF/HTML/EPUB |
| 团队协作 | 不支持 | 共享归档+权限治理 |
| 缓存策略 | 无 | 多级缓存+命中率监控 |
| 页面规模 | ≤5000 | 无限制(分布式支撑) |
| 技术支持 | 社区 | 优先工单(4小时响应) |

## 使用场景

### 场景一:企业知识库统一检索

集团企业拥有多个Notion工作空间(各部门独立),需要建立统一检索入口。

```bash
# 1. 添加多个工作空间
smart-crawler workspace add research --token $NOTION_TOKEN_RESEARCH
smart-crawler workspace add product --token $NOTION_TOKEN_PRODUCT
smart-crawler workspace add marketing --token $NOTION_TOKEN_MARKETING

# 2. 配置定时同步(每天凌晨2点)
smart-crawler schedule add --cron "0 2 * * *" --workspaces all --mode incremental

# 3. 跨工作空间检索
smart-crawler search "用户研究" --workspaces research,product

# 4. 生成统一报告
smart-crawler report --workspaces all --format json
```

### 场景二:研究机构文献爬取

研究机构需要爬取多个外部知识源,建立文献索引库。

```bash
# 1. 配置多源爬取
smart-crawler source add notion-research --type notion --token $TOKEN_1
smart-crawler source add notion-papers --type notion --token $TOKEN_2

# 2. 启用增量索引
smart-crawler sync --source notion-research --mode incremental --checkpoint

# 3. 全文检索(支持中文分词)
smart-crawler search "深度学习 模型压缩" --mode fulltext --highlight

# 4. 高级SQL查询(多表JOIN)
smart-crawler sql "
  SELECT p.title, p.last_updated, d.name as database
  FROM pages p
  JOIN databases d ON p.database_id = d.id
  WHERE p.last_updated > '2026-01-01'
  ORDER BY p.last_updated DESC
  LIMIT 20;
"

# 5. 导出检索结果为Markdown
smart-crawler export --query "深度学习" --format markdown --output ./research-notes/
```

### 场景三:SaaS内容聚合服务

SaaS产品需要为客户聚合多个Notion工作空间的内容,提供统一检索API。

```bash
# 1. 启用分布式调度
smart-crawler cluster init --nodes 4
smart-crawler cluster status

# 2. 配置Webhook触发同步
smart-crawler webhook add --url https://your-app.example/hooks/notion-updated --events page.updated

# 3. 启用多级缓存
smart-crawler cache config --l1-ttl 60 --l2-ttl 300 --l2-backend redis

# 4. 启动检索服务
smart-crawler serve --port 8080 --concurrency 100

# 5. 监控检索性能
smart-crawler metrics --query-latency-p99 --cache-hit-rate --index-size
```

## 不适用场景

以下场景智能爬虫(专业版)不适合处理：

- 渗透测试未授权目标
- 物理安全防护
- 社会工程学攻击


## 触发条件

需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于非本工具能力范围的需求。


## 快速开始

预计上手时间:<120秒(适合中等复杂度工具)。

### 步骤1:升级到专业版

```bash
smart-crawler license apply --key $PRO_LICENSE_KEY
```

### 步骤2:配置多工作空间

```bash
smart-crawler workspace add main --token $NOTION_TOKEN_MAIN
smart-crawler workspace add secondary --token $NOTION_TOKEN_SECONDARY
smart-crawler workspace list
```

### 步骤3:启用增量索引

```bash
smart-crawler sync --mode incremental --workspaces all
```

### 步骤4:体验全文检索

```bash
smart-crawler search "你的关键词" --mode fulltext --highlight
```

## 示例

### 多工作空间配置

```yaml
# ~/.smart-crawler/config.yaml
workspaces:
  - name: research
    token: ${NOTION_TOKEN_RESEARCH}
    syncMode: incremental
    schedule: "0 2 * * *"
  - name: product
    token: ${NOTION_TOKEN_PRODUCT}
    syncMode: incremental
    schedule: "0 3 * * *"

cluster:
  nodes: 4
  coordinator: localhost:9092

cache:
  l1:
    enabled: true
    ttl: 60
    maxSize: 10000
  l2:
    enabled: true
    backend: redis
    ttl: 300
    endpoints:
      - redis://localhost:6379

index:
  type: fulltext
  analyzer: ik_smart
  synonyms: ./synonyms.txt
```

### 全文检索查询示例

```bash
# 基础全文检索
smart-crawler search "时间管理" --mode fulltext

# 带高亮显示
smart-crawler search "时间管理" --mode fulltext --highlight

# 限定工作空间
smart-crawler search "时间管理" --workspaces research,product

# 模糊匹配
smart-crawler search "时间管" --mode fuzzy --fuzziness 2

# 同义词扩展
smart-crawler search "效率" --mode fulltext --expand-synonyms

# 语义检索(基于向量)
smart-crawler search "如何提升工作效率" --mode semantic --top-k 10
```

### 高级SQL查询

```sql
-- 多表JOIN查询
SELECT p.title, p.last_updated, d.name as database, w.name as workspace
FROM pages p
JOIN databases d ON p.database_id = d.id
JOIN workspaces w ON p.workspace_id = w.id
WHERE p.last_updated > '2026-01-01'
  AND w.name IN ('research', 'product')
ORDER BY p.last_updated DESC
LIMIT 20;

-- 聚合统计
SELECT
  w.name as workspace,
  COUNT(DISTINCT p.id) as page_count,
  COUNT(DISTINCT d.id) as database_count,
  MAX(p.last_updated) as latest_update
FROM pages p
LEFT JOIN databases d ON p.database_id = d.id
JOIN workspaces w ON p.workspace_id = w.id
GROUP BY w.name
ORDER BY page_count DESC;
```

### 导出模板配置

```json
{
  "export": {
    "format": "markdown",
    "template": "./templates/note.md.j2",
    "output": "./exports/",
    "structure": {
      "groupBy": "database",
      "sortBy": "last_updated",
      "includeMetadata": true
    },
    "transform": {
      "pageBreak": true,
      "toc": true,
      "frontMatter": true
    }
  }
}
```

## 最佳实践

1. **增量索引优先**:日常同步使用`--mode incremental`,仅更新变更部分,效率提升10倍
2. **多级缓存合理配置**:L1缓存(60秒)应对热点查询,L2缓存(300秒)应对冷启动
3. **分布式节点按需扩容**:节点数与工作空间数量成正比,建议每3个工作空间1个节点
4. **定时同步错峰执行**:不同工作空间的同步时间错开,避免峰值压力
5. **全文检索用ik_smart分词**:中文场景下`ik_smart`分词效果最佳
6. **导出使用模板系统**:通过Jinja2模板统一导出格式,便于团队协作
7. **Webhook触发实时同步**:对时效性要求高的场景,用Webhook替代定时同步
8. **监控P99延迟**:检索P99延迟>500ms时告警,提示扩容或优化索引

## 性能优化策略

### 增量索引机制

```
源数据变更 → Webhook通知 → 增量拉取 → 索引差量更新 → 缓存失效
                ↓ 无变更
              跳过同步
```

- **变更检测**:基于`last_updated`时间戳,仅拉取变更部分
- **索引差量**:对比新旧内容,仅更新变更字段
- **缓存失效**:精准失效相关缓存,避免全量刷新

### 分布式调度架构

```
Coordinator(协调节点)
    ├── Worker-1 → 工作空间A
    ├── Worker-2 → 工作空间B
    ├── Worker-3 → 工作空间C
    └── Worker-4 → 工作空间D
```

- **任务分片**:按工作空间维度分片,每个Worker负责一个或多个工作空间
- **故障转移**:Worker宕机时,任务自动迁移到其他节点
- **负载均衡**:根据Worker负载动态调整任务分配

### 多级缓存命中率监控

```bash
# 实时监控缓存命中率
smart-crawler metrics --cache-hit-rate --realtime

# 输出示例:
# L1 Cache Hit Rate: 87.3%
# L2 Cache Hit Rate: 94.1%
# Overall Hit Rate: 91.2%
# Avg Query Latency: 23ms
# P99 Query Latency: 87ms
```

命中率<80%时触发告警,提示调整缓存策略。

## 多平台集成示例

### 与企业微信集成

```bash
# 检索结果推送到企业微信群
smart-crawler search "项目周报" --notify wecom --webhook $WECOM_WEBHOOK
```

### 与`PostgreSQL`数据仓库同步

```bash
# 归档数据同步到PostgreSQL数据仓库做深度分析
smart-crawler sync-to-warehouse \
  --source archive \
  --destination postgresql://user:pass@host:5432/knowledge_db \
  --mode incremental \
  --schedule "0 4 * * *"
```

### 与Elasticsearch集成

```bash
# 索引同步到Elasticsearch,支持更复杂的检索
smart-crawler sync-to-es \
  --endpoints http://es-1:9200,http://es-2:9200 \
  --index knowledge-v2 \
  --mapping ./es-mapping.json
```

## 版本升级迁移指南

### 从免费版升级到专业版

1. 应用专业版License,功能自动解锁
2. 原有归档数据自动继承,无需迁移
3. 启用多工作空间前,建议先梳理工作空间清单与Token
4. 启用分布式调度前,确保各节点网络互通
5. 启用全文检索前,需要对历史归档执行一次"全量索引构建"

```bash
# 触发历史数据全量索引构建
smart-crawler index rebuild --workspaces all --mode fulltext
```

## 常见问题

### Q1: 多工作空间同步顺序如何控制?

A: 通过`sync.priority`配置项控制,数字越小优先级越高。默认按工作空间名称字母序。

### Q2: 增量索引如何判断"变更"?

A: 基于`last_updated`时间戳。若时间戳较归档中最新时间更新,则判定为变更,触发差量更新。

### Q3: 分布式节点如何扩容?

A: 1)在新机器上安装smart-crawler;2)执行`smart-crawler cluster join --coordinator host:9092`;3)协调节点自动分配任务。

### Q4: 全文检索支持哪些分词器?

A: 支持IK分词(ik_smart/ik_max_word)、jieba、standard、whitespace等。中文场景推荐ik_smart。

### Q5: 语义检索如何工作?

A: 基于向量数据库(支持Faiss/Milvus),将页面内容向量化后做相似度检索。需要预先构建向量索引。

### Q6: Webhook触发同步延迟多少?

A: 端到端延迟<5秒(从源变更到归档更新)。相比定时同步的分钟级延迟,适合时效性要求高的场景。

### Q7: 缓存命中率突然下降怎么办?

A: 1)检查是否近期有大量新数据(索引未构建);2)检查缓存Key设计是否合理;3)调整TTL或容量;4)必要时清空缓存重建。

### Q8: 导出PDF支持中文吗?

A: 支持。需要安装中文字体(如思源黑体),在导出模板中指定`font-family: 'Source Han Sans CN'`。

### Q9: 如何监控归档存储用量?

A: `smart-crawler storage stats`命令查看各工作空间的归档大小、文件数、增长率。

### Q10: 专业版的SLA承诺是什么?

A: 99.9%可用性,故障4小时响应,数据可恢复性RPO<15分钟、RTO<4小时。

## 错误处理

| 症状 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 同步超时 | 工作空间过大或网络慢 | 启用分布式调度,分片同步 | 高 |
| 全文检索无结果 | 索引未构建或分词器不匹配 | 执行`index rebuild`,检查分词器配置 | 高 |
| 增量索引漏更新 | last_updated时间戳精度问题 | 启用Webhook触发,补充定时全量同步 | 中 |
| 分布式节点失联 | 网络故障或节点宕机 | 检查节点健康,任务自动迁移 | 中 |
| 缓存命中率下降 | 缓存Key设计不合理或TTL过短 | 调整Key粒度与TTL,监控命中率曲线 | 低 |
| 导出PDF中文乱码 | 字体缺失 | 安装中文字体,在模板中指定font-family | 低 |

## 专业版特性

本专业版相比免费版新增以下能力:

- 多工作空间管理:无限制并行归档,支持团队级权限隔离
- 分布式调度:多节点并行爬取,支撑万级页面规模
- 增量索引:仅更新变更部分,同步效率提升10倍
- 全文检索引擎:支持中文分词、同义词、模糊匹配、语义检索
- 自定义导出:Markdown/PDF/HTML/EPUB四种格式,带模板系统
- 定时自动同步:支持cron表达式与Webhook事件触发
- 多级缓存:L1进程内 + L2 Redis,带命中率监控
- 团队协作:共享归档 + 权限治理
- 优先支持:4小时响应工单,专属技术经理

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | 0元 | 核心功能 + 单工作空间 | 个人知识管理 |
| 收费专业版 | 49.9元/月 或 499元/年 | 全功能 + 分布式 + 全文检索 + 优先支持 | 团队/企业知识库 |

专业版通过SkillHub SkillPay发布,支持按月订阅或一次性年付(享8折优惠)。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+(用于运行smart-crawler CLI)
- **Python**: 3.8+(可选,用于辅助脚本与ETL)
- **Docker**: 20+(可选,用于分布式部署)

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| smart-crawler CLI | 命令行工具 | 必需 | `npm install -g smart-crawler` |
| Notion Integration | 在线服务 | 必需 | 通过Notion开发者平台创建 |
| Redis | 缓存服务 | 可选 | 用于多级缓存,自建或使用云服务 |
| `PostgreSQL` | 数据库 | 可选 | 用于数据仓库同步,版本12+ |
| Elasticsearch | 检索引擎 | 可选 | 用于高级检索,版本7+ |
| Faiss/Milvus | 向量数据库 | 可选 | 用于语义检索 |

### API Key 配置
- **NOTION_TOKEN_***: 各工作空间的Integration Token,通过环境变量传入
- **PRO_LICENSE_KEY**: 专业版License,通过环境变量或配置文件传入
- **Redis连接串**: 通过`REDIS_URL`环境变量传入
- **加密密钥**: 通过KMS服务管理,禁止在配置文件中明文存储
- **安全建议**: 所有Token遵循"最小权限 + 定期轮换"原则,建议每90天轮换一次

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
