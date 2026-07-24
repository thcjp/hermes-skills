---
slug: "mongo-manager"
name: "mongo-manager"
version: 1.0.1
displayName: "Mongo管理工具专业版"
summary: "MongoDB企业级管理与优化全功能版，含分片集群、副本集高可用、Atlas Search、Change Stream与基准测试。"
license: "Proprietary"
edition: "pro"
description: |-
  面向MongoDB运维与架构师的企业级全功能专业版。在免费版基础上新增分片集群配置、副本集高可用、Atlas Search全文搜索、Change Stream实时同步、性能基准测试套件、容量规划模型等高级能力，配套面向DBA、架构师、SRE的多角色场景指南。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段.
tags:
  - 集成工具
  - 数据库
  - NoSQL
  - 企业级
  - 工具
  - 效率
  - 自动化
  - 研究
  - 分析
  - 创意
  - 图像
  - 知识
  - 按流程执
  - javascript
  - schema
  - mydb
  - true
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"
---
# Mongo管理工具专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Mongo管理工具专业版ngoDB企业级管理 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 核心能力

| 能力分类 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| Schema设计 | 单机设计 | 分片键设计+数据分布 |
| 高可用 | 无 | 副本集自动故障切换 |
| 水平扩展 | 无 | 分片集群+均衡器调优 |
| 全文搜索 | 基础文本索引 | Atlas Search（Lucene引擎） |
| 实时同步 | 无 | Change Stream+ETL管道 |
| 性能基准 | 无 | YSBench压测套件 |
| 容量规划 | 经验估算 | 数据模型+增长率预测 |
| 监控告警 | 基础explain | Ops Manager集成 |
| 优先支持 | 社区 | 工单优先响应 |
### 能力分类

针对能力分类,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力分类相关的配置参数、输入数据和处理选项.
**输出**: 返回能力分类的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力分类`的配置文档进行参数调优
### Schema设计

针对Schema设计,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Schema设计相关的配置参数、输入数据和处理选项.
**输出**: 返回Schema设计的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Schema设计`的配置文档进行参数调优
### 高可用

针对高可用,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供高可用相关的配置参数、输入数据和处理选项.
**输出**: 返回高可用的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`高可用`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：分片集群扩容（架构师视角）

单机性能瓶颈时通过分片水平扩展，关键在于分片键选择.
```javascript
// 启用分片
sh.enableSharding("mydb")
// ...
// 选择分片键（避免单调递增导致热点）
// 错误：{createdAt: 1}（所有写入集中到一个分片）
// 正确：{userId: 1, createdAt: 1}（哈希分布）
sh.shardCollection("mydb.orders", {userId: "hashed"})
// ...
// 查看分片状态
sh.status()
db.orders.getShardDistribution()
```

### 场景二：副本集高可用（DBA视角）

配置3节点副本集，主节点故障自动切换.
```javascript
// 初始化副本集
rs.initiate({
    _id: "rs0",
    members: [
        {_id: 0, host: "mongo1:27017", priority: 2},   // 主节点
        {_id: 1, host: "mongo2:27017", priority: 1},   // 从节点
        {_id: 2, host: "mongo3:27017", arbiterOnly: true} // 仲裁节点
    ]
})
// ...
// 故障切换配置
rs.conf().settings.electionTimeoutMillis = 10000  // 10秒超时
rs.conf().settings.chainingAllowed = true          // 允许从节点链式复制
```

### 场景三：Atlas Search全文搜索（开发者视角）

替代Elasticsearch，在MongoDB内实现高性能全文搜索.
```javascript
// 创建Atlas Search索引
db.collection.createSearchIndex({
    mappings: {dynamic: true},
    analyzers: [
        {name: "chineseAnalyzer", charFilters: [], tokenizer: {type: "standard"}, tokenFilters: []}
    ]
})
// ...
// 全文搜索查询
db.collection.aggregate([
    {$search: {
        index: "default",
        text: {query: "MongoDB教程", path: ["title", "content"]}
    }},
    {$limit: 10}
])
```

### 场景四：Change Stream实时同步（SRE视角）

监听集合变更，实时同步到下游系统.
```javascript
// 监听变更
const changeStream = db.collection.watch([
    {$match: {operationType: {$in: ["insert", "update", "delete"]}}}
], {fullDocument: "updateLookup"})
// ...
changeStream.on("change", (event) => {
    // 同步到下游
    syncToElasticsearch(event)
    // 或发送到Kafka
    publishToKafka(event)
})
```

## 使用流程

### 优秀步：连接集群

```javascript
// 分片集群连接（mongos路由）
mongodb://mongos1:27017,mongos2:27017/mydb?replicaSet=rs0
// ...
// 副本集连接
mongodb://mongo1:27017,mongo2:27017,mongo3:27017/mydb?replicaSet=rs0
```

### 第二步：配置分片

```javascript
// 启用分片
sh.enableSharding("mydb")
// ...
// 对集合分片
sh.shardCollection("mydb.orders", {userId: "hashed"})
// ...
// 配置均衡器
sh.setBalancerState(true)
sh.startBalancer()
```

### 第三步：启用Atlas Search

```javascript
db.articles.createSearchIndex({
    mappings: {dynamic: true},
    analyzers: [{name: "standard", charFilters: [], tokenizer: {type: "standard"}, tokenFilters: []}]
})
```

完整上手时间约300秒（含集群配置）.
**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | mongo-manager处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "manager_result": "manager_result_value",
      "manager_metadata": "manager_metadata_value",
      "manager_status": "manager_status_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/mongo-manager_template`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **MongoDB**: 5.0+（推荐6.0+以使用Atlas Search等特性）
- **mongosh**: 1.5+

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| MongoDB | 数据库 | 必需 | mongodb.com 官方下载 |
| mongosh | 客户端 | 必需 | 随MongoDB附带 |
| PyMongo | Python驱动 | 可选 | `pip install pymongo` |
| Kafka | 消息队列 | 可选 | kafka.apache.org（Change Stream下游） |
| Ops Manager | 运维平台 | 可选 | mongodb.com 企业版 |
| Prometheus | 监控 | 可选 | prometheus.io 官方下载 |
| Grafana | 可视化 | 可选 | grafana.com 官方下载 |

### API Key 配置
- **MONGODB_URI**: 集群连接字符串，通过环境变量注入，禁止硬编码
- **数据库密码**: 通过MONGODB_PASSWORD环境变量配置
- **Atlas API Key**: 若使用Atlas云服务，通过ATLAS_PUBLIC_KEY/ATLAS_PRIVATE_KEY环境变量配置
- **Ops Manager API Key**: 通过OPSMANAGER_API_KEY环境变量配置
- **Kafka SASL凭证**: 通过KAFKA_SASL_USERNAME/KAFKA_SASL_PASSWORD环境变量配置

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，

## 案例展示

### 分片键设计决策表

| 数据特征 | 推荐分片键 | 示例 |
|---:|:---|---:|
| 用户数据，按用户查询 | `{userId: "hashed"}` | 用户订单 |
| 时间序列数据，按时间范围查询 | `{timestamp: 1, deviceId: "hashed"}` | IoT数据 |
| 地理分布数据 | `{region: 1, id: "hashed"}` | 多地部署 |
| 单调递增ID（避免） | - | ObjectId作为分片键导致热点 |

### 副本集高可用配置

```yaml
# mongod.conf
replication:
  replSetName: rs0
  oplogSizeMB: 2048       # oplog大小
  enableMajorityReadConcern: true
# ...
# 故障切换参数
setParameter:
  electionTimeoutMillis: 10000
  heartbeatIntervalMillis: 2000
  chainingAllowed: true
```

### Atlas Search索引定义

```javascript
db.products.createSearchIndex({
    name: "product-search",
    mappings: {
        dynamic: false,
        fields: {
            name: {type: "string", analyzer: "standard"},
            description: {type: "string", analyzer: "standard"},
            price: {type: "number"},
            category: {type: "stringFacet"},
            tags: {type: "stringFacet"}
        }
    },
    analyzers: [
        {name: "chinese", charFilters: [], tokenizer: {type: "standard"}, tokenFilters: [{type: "lowercase"}]}
    ]
})
```

### Change Stream可靠性保障

```javascript
// 使用resumeToken保证不丢事件
let resumeToken = loadResumeToken() // 从持久化存储加载
// ...
const stream = db.collection.watch([], {
    resumeAfter: resumeToken,
    fullDocument: "updateLookup",
    maxAwaitTimeMS: 30000
})
// ...
stream.on("change", (event) => {
    try {
        processEvent(event)
        saveResumeToken(event._id) // 持久化resumeToken
    } catch (e) {
        logger.error("处理失败", e)
        // 重试或死信队列
    }
})
```

## 常见问题

### Q1：分片后数据倾斜怎么办？

A：(1) 检查分片键基数是否过低；(2) jumbo chunk手动分裂：`sh.splitFind()`；(3) 关闭均衡器手动迁移：`moveChunk`；(4) 长期方案是重新选择分片键，需停机迁移.
### Q2：副本集故障切换后旧主节点数据回滚？

A：回滚是必然的，因为旧主节点的未复制写入会丢失。预防措施：(1) 使用`w:majority`写关注；(2) 旧主节点恢复后作为从节点重新加入，回滚数据保存到rollback目录.
### Q3：Atlas Search索引构建慢？

A：(1) 使用`$search`前先确认索引状态为`READY`；(2) 大集合构建索引会占用资源，建议低峰期执行；(3) 索引构建失败查看`db.collection.getSearchIndexes()`状态.
### Q4：Change Stream断开后如何恢复？

A：使用持久化的`resumeToken`通过`resumeAfter`恢复。若token过期（oplog被覆盖），使用`startAtOperationTime`从指定时间点重新消费，需配合幂等处理.
### Q5：分片集群查询走广播怎么办？

A：广播查询（scatter-gather）说明查询未包含分片键。优化方案：(1) 查询条件增加分片键；(2) 业务层先按分片键路由；(3) 无法避免的聚合查询使用`$merge`分片并行.
### Q6：副本集oplog满了怎么办？

A：(1) 增大oplog：`db.adminCommand({replSetResizeOplog: 1, size: 4096})`；(2) 从节点长时间离线后需全量重新同步；(3) 监控oplog窗口，低于1小时告警.
### Q7：如何监控分片均衡？

A：(1) `sh.status()`查看各分片chunk数；(2) `db.collection.getShardDistribution()`查看数据分布；(3) 均衡器日志：`mongos`日志过滤`balancer`关键字；(4) 集成Ops Manager做可视化监控.
### Q8：跨集群数据同步方案？

A：(1) 同构MongoDB使用Atlas Live Migration；(2) 异构系统使用Change Stream + Kafka；(3) 离线同步使用`mongodump/mongorestore`；(4) 专业版提供`mongo-manager-pro sync`工具支持双向同步.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

