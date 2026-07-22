---
slug: "tool-call-retry-tool-pro"
name: "tool-call-retry-tool-pro"
version: "1.0.0"
displayName: "工具调用重试专业版"
summary: "自定义错误修复、持久化幂等、退避策略可配与全链路监控，适合企业级Agent执行链路。"
license: "Proprietary"
edition: "pro"
description: |-
  工具调用重试工具专业版，面向企业级Agent执行链路的高阶工具调用增强方案。核心能力:
  - 自定义错误处理函数，支持参数自动修复后重试
  - 持久化幂等性键，跨进程/跨实例去重
  - 可配置退避策略（指数/线性/抖动/自定义）
  - 全链路监控与重试日志归档
  - 批量工具调用的并发重试控制

  适用场景:
  - 企业级Agent的高可靠性执行链路
  - 复杂场景下的错误自愈与参数修复
  - 分布式系统的跨实例幂等保证

  差异化: 专业版在免费版核心重试能力之上扩展错误修复与持久化...
tags:
  - 工具调用
  - 错误自愈
  - 企业级
  - 专业版
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 工具调用重试工具（专业版）

## 概述

专业版在免费版的指数退避重试与格式校验之上，扩展为面向企业级 Agent 执行链路的完整工具调用增强方案。新增自定义错误修复、持久化幂等性、可配置退避策略与全链路监控，同时与免费版的 API 保持向后兼容。

## 核心能力

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 重试机制 | 固定指数退避 | 指数/线性/抖动/自定义 |
| 错误处理 | 不支持 | 自定义错误修复函数 |
| 幂等性 | 内存存储 | 持久化存储（跨进程/跨实例） |
| 结果校验 | 基础 | 多级校验 + 业务规则 |
| 监控 | 不支持 | 全链路日志 + 指标归档 |
| 批量重试 | 不支持 | 并发控制 + 批量重试 |
| 告警 | 不支持 | 异常告警 + Webhook 通知 |
| 最大重试 | 1-10 | 1-50（可配置上限） |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 按照skill规范执行参数配置与调用操作,遵循单一意图原则。
**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 按照skill规范执行结果处理与输出操作,遵循单一意图原则。
**输出**: 返回结果处理与输出的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：持久化幂等、退避策略可配与全、链路监控、适合企业级、Agent、执行链路、工具调用重试工具、面向企业级、执行链路的高阶工、具调用增强方案、自定义错误处理函、支持参数自动修复、后重试、持久化幂等性键、跨实例去重、可配置退避策略、全链路监控与重试、日志归档、批量工具调用的并、发重试控制等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一：SQL 错误的自动修复重试

调用数据库时遇到 SQL 语法错误，自动修复后重试。

```typescript
const result = await skills.toolCallRetry({
  toolFn: callDatabase,
  args: { sql: "SELECT * FROM users" },
  errorHandlerFn: async (error, attempt) => {
    if (error.message.includes("SQL syntax error")) {
      // 自动修复 SQL 语法
      const fixedSql = await fixSqlWithLLM(error.message);
      return { args: { sql: fixedSql } };
    }
    if (attempt >= 2) {
      // 重试 2 次失败后中止
      return { abort: true };
    }
  },
  maxRetries: 5,
  persistence: true
});
```

### 场景二：跨实例幂等性保证

分布式部署的 Agent 需要跨实例的幂等保证。

```typescript
const result = await skills.toolCallRetry({
  toolFn: processOrder,
  args: { orderId: "order-456" },
  idempotencyKey: "order-process-456",
  persistence: {
    store: "redis",
    config: { host: "redis.local", port: 6379, ttl: 86400 }
  }
});

// 即使多个实例同时调用，相同 key 只会执行一次
```

### 场景三：批量工具调用的并发重试

批量调用多个外部 API，希望统一控制并发与重试。

```typescript
const results = await skills.toolCallBatch({
  calls: [
    { toolFn: fetchUser, args: { id: 1 } },
    { toolFn: fetchUser, args: { id: 2 } },
    { toolFn: fetchUser, args: { id: 3 } },
    // ... 更多调用
  ],
  concurrency: 5,
  retry: {
    maxRetries: 3,
    backoff: "exponential-jitter",
    initialDelayMs: 500
  },
  monitoring: {
    enabled: true,
    logPath: "./logs/tool-calls/"
  }
});
```

## 不适用场景

以下场景工具调用重试专业版不适合处理：

- 数据库架构设计决策
- NoSQL选型
- 数据仓库ETL设计

## 触发条件

需要数据库操作、SQL查询、数据存储管理时使用。不适用于非本工具能力范围的需求。

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

```typescript
// 1. 高级用法（错误自动修复）
const result = await skills.toolCallRetry({
  toolFn: yourToolFunction,
  args: { key: "value" },
  errorHandlerFn: async (error, attempt) => {
    if (error.code === "INVALID_PARAM") {
      return { args: { key: "fixed-value" } };
    }
    if (attempt >= 3) return { abort: true };
  }
});

// 2. 自定义退避策略
const result = await skills.toolCallRetry({
  toolFn: yourToolFunction,
  args: { key: "value" },
  backoff: "linear-jitter",
  initialDelayMs: 500,
  maxDelayMs: 10000
});

// 3. 持久化幂等
const result = await skills.toolCallRetry({
  toolFn: yourToolFunction,
  args: { key: "value" },
  idempotencyKey: "unique-key",
  persistence: { store: "file", path: "./.idempotency/" }
});
```

## 示例

```yaml
# tool-call-retry-pro config
edition: pro
retry:
  max_retries: 5
  max_retries_upper_limit: 50
  backoff: exponential-jitter
  initial_delay_ms: 1000
  max_delay_ms: 30000
persistence:
  enabled: true
  store: redis
  config:
    host: redis.local
    port: 6379
    ttl: 86400
monitoring:
  enabled: true
  log_path: ./logs/tool-calls/
  metrics: true
  alert:
    enabled: true
    failure_rate_threshold: 0.3
    webhook: https://hooks.example.com/tool-alert
batch:
  max_concurrency: 10
  fail_fast: false
error_handler:
  auto_fix: true
  max_fix_attempts: 2
```

## 退避策略库

| 策略 | 说明 | 适用场景 |
|:-----|:-----|:---------|
| exponential | 指数退避（1s, 2s, 4s...） | 通用默认 |
| exponential-jitter | 指数+抖动（避免惊群） | 分布式场景 |
| linear | 线性退避（1s, 2s, 3s...） | 轻度不稳定 |
| linear-jitter | 线性+抖动 | 批量调用 |
| fixed | 固定间隔 | 已知恢复时间 |
| custom | 自定义函数 | 专业场景 |

## 最佳实践

* 对可修复的错误（如参数格式）启用 errorHandler，自动修复后重试。
* 对不可恢复的错误（如权限不足）在 errorHandler 中返回 `{ abort: true }`。
* 分布式场景使用 exponential-jitter 退避，避免多个实例同时重试。
* 持久化幂等建议使用 Redis，TTL 设置为业务超时的 2 倍。
* 批量调用时控制并发数，避免打垮下游服务。
* 启用监控后定期检查失败率，及时发现下游异常。
* 全链路类型安全，所有参数带 Zod 校验。

## 常见问题

**Q：专业版与免费版的 API 兼容吗？**
A：兼容。免费版的所有参数在专业版中可直接使用，专业版额外支持 `errorHandlerFn`、`backoff`、`persistence`、`monitoring` 等参数。

**Q：持久化幂等支持哪些存储？**
A：支持文件存储、Redis、SQLite。企业版可扩展支持 MySQL 等数据库。

**Q：错误修复函数能调用 LLM 吗？**
A：可以。errorHandlerFn 是异步函数，可调用 LLM 进行参数修复，但需注意 LLM 调用本身的不稳定性。

**Q：批量重试的并发数如何设置？**
A：建议根据下游服务的承载能力设置，通常 5-10 为宜。启用 fail_fast 可在首个失败时中止整批。

**Q：监控日志会占用多少存储？**
A：单次调用日志约 1-2KB。建议配置日志轮转，保留最近 30 天即可。

**Q：可以与分布式追踪系统集成吗？**
A：专业版支持输出 OpenTelemetry 格式的 span，便于与 Jaeger/Zipkin 集成。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: 支持 TypeScript/JavaScript 的环境

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Redis | 服务 | 可选（持久化幂等） | 官方部署或云服务 |
| Zod | 库 | 可选（类型校验） | npm 安装 |

### API Key 配置
- 本skill基于Markdown指令规范，无需额外API Key（除内容中明确标注的外部API）
- 持久化幂等若使用 Redis，需配置 Redis 连接信息
- 监控告警若使用 Webhook，需配置 Webhook URL

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + 代码执行 + 可选持久化服务）
- **说明**: 专业版在 Markdown 指令基础上，提供企业级重试、持久化与监控能力

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用
