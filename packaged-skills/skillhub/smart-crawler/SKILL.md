---
slug: "smart-crawler"
name: "smart-crawler"
version: "1.0.0"
displayName: "智能爬虫(专业版)"
summary: "企业级知识库爬取与检索平台,支持多工作空间、分布式调度、增量索引、全文检索与自定义导出,适合团队与企业规模化使用。"
license: "Proprietary"
edition: "pro"
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
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# 智能爬虫(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

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

**处理**: 按照skill规范执行与免费版能力对比操作,遵循单一意图原则。
### 工作空间数量

执行工作空间数量操作,处理用户输入并返回结果。

**输入**: 用户提供工作空间数量所需的参数和指令。

**输出**: 返回工作空间数量的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`工作空间数量`相关配置参数进行设置
### 同步方式

执行同步方式操作,处理用户输入并返回结果。

**输入**: 用户提供同步方式所需的参数和指令。

**输出**: 返回同步方式的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`同步方式`相关配置参数进行设置
#
## 适用场景

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

## 使用流程

预计上手时间:<120秒(适合中等复杂度工具)。

### 第1步:升级到专业版

```bash
smart-crawler license apply --key $PRO_LICENSE_KEY
```

### 第2步:配置多工作空间

```bash
smart-crawler workspace add main --token $NOTION_TOKEN_MAIN
smart-crawler workspace add secondary --token $NOTION_TOKEN_SECONDARY
smart-crawler workspace list
```

### 第3步:启用增量索引

```bash
smart-crawler sync --mode incremental --workspaces all
```

### 第4步:体验全文检索

```bash
smart-crawler search "你的关键词" --mode fulltext --highlight
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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

| 症状 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 同步超时 | 工作空间过大或网络慢 | 启用分布式调度,分片同步 | 高 |
| 全文检索无结果 | 索引未构建或分词器不匹配 | 执行`index rebuild`,检查分词器配置 | 高 |
| 增量索引漏更新 | last_updated时间戳精度问题 | 启用Webhook触发,补充定时全量同步 | 中 |
| 分布式节点失联 | 网络故障或节点宕机 | 检查节点健康,任务自动迁移 | 中 |
| 缓存命中率下降 | 缓存Key设计不合理或TTL过短 | 调整Key粒度与TTL,监控命中率曲线 | 低 |
| 导出PDF中文乱码 | 字体缺失 | 安装中文字体,在模板中指定font-family | 低 |

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
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

## 案例展示

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


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

