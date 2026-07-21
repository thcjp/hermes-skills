---
slug: bailian-search-tool-free
name: bailian-search-tool-free
version: "1.0.0"
displayName: 百炼搜索工具-免费版
summary: 基于百炼API的AI优化网页搜索,返回多源简洁结果,适合个人开发者
license: Proprietary
edition: free
description: |-
  基于百炼(阿里云模型工作室)WebSearch API 的 AI 优化网页搜索工具,
  为 AI 代理设计,返回干净、相关的内容。

  核心能力:
  - AI 优化的网页搜索
  - 多源结果聚合
  - 简洁干净的内容返回
  - 可配置结果数量

  适用场景:
  - 个人开发者的信息检索
  - AI 代理的实时知识获取
  - 快速事实查询

  差异化:免费版提供核心搜索能力,适合个人用户与轻量场景。

  触发关键词: 网页搜索, 百炼, 模型工作室, WebSearch, bailian, 实时信息
tags:
- 研究工具
- 网页搜索
- 信息检索
tools:
  - - read
- exec
---
# 百炼搜索工具(免费版)

## 概述

本工具基于百炼(阿里云模型工作室)WebSearch API 实现 AI 优化的网页搜索,专为 AI 代理设计,返回干净、相关的内容。免费版面向个人开发者,提供核心搜索能力与可配置的结果数量。

### 与传统搜索引擎 API 的对比

| 对比维度 | 传统搜索 API | 本工具(AI 优化) |
|:---------|:------------|:----------------|
| 结果质量 | 原始网页片段 | AI 优化,干净相关 |
| 内容处理 | 原始返回 | 自动清洗与摘要 |
| 多源聚合 | 单一来源 | 多源结果聚合 |
| AI 适配 | 需后处理 | 直接可用于 AI |
| 适用场景 | 通用搜索 | AI 代理知识获取 |

## 核心能力

| 能力 | 说明 | 示例 |
|:-----|:-----|:-----|
| 网页搜索 | AI 优化的多源搜索 | `mcp-websearch.sh "查询词"` |
| 结果数量配置 | 可指定返回结果数 | `mcp-websearch.sh "查询词" 10` |
| 干净内容 | 自动清洗与去噪 | 返回简洁相关的内容 |
| 多源聚合 | 聚合多个信息源 | 一次查询返回多源结果 |

## 使用场景

### 场景一:快速事实查询

个人开发者需要快速查询某个事实或概念。

```bash
# 基础搜索(默认5条结果)
./scripts/mcp-websearch.sh "Python asyncio 基本用法"

# 指定结果数量
./scripts/mcp-websearch.sh "Python asyncio 基本用法" 10
```

### 场景二:AI 代理知识获取

AI 代理在对话中需要获取实时信息,通过本工具搜索补充知识。

```bash
# 用户询问最新技术动态
# AI 代理调用搜索获取实时信息
./scripts/mcp-websearch.sh "2026 年 AI 智能体最新进展" 5

# 用户询问某概念解释
./scripts/mcp-websearch.sh "什么是 RAG 检索增强生成" 3
```

### 场景三:多主题快速调研

对多个主题进行快速搜索调研,收集初步信息。

```bash
#!/bin/bash
# quick-research.sh - 快速主题调研
TOPICS=("AI智能体" "大模型微调" "向量数据库" "RAG技术")

for topic in "${TOPICS[@]}"; do
  echo "=== ${topic} ==="
  ./scripts/mcp-websearch.sh "$topic" 3
  echo ""
done

echo "调研完成"
```

## 不适用场景

以下场景百炼搜索工具-免费版不适合处理：

- 黑帽SEO手段
- 搜索引擎作弊
- 付费广告投放管理


## 触发条件

需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于非本工具能力范围的需求。


## 快速开始

### 1. 基础搜索

```bash
# 基础搜索(默认5条结果)
{baseDir}/scripts/mcp-websearch.sh "查询词"

# 指定结果数量(最多20条)
{baseDir}/scripts/mcp-websearch.sh "查询词" 10
```

### 2. 参数说明

| 参数 | 说明 | 默认值 | 范围 |
|:-----|:-----|:------|:-----|
| `<query>` | 搜索查询词 | 必填 | - |
| `<count>` | 返回结果数量 | 5 | 1-20 |

### 3. 输出格式

```text
=== 结果 1 ===
标题: 网页标题
链接: https://example.com/page
摘要: 来自搜索结果的描述
内容: (干净的相关内容)

=== 结果 2 ===
标题: 网页标题
链接: https://example.com/page
摘要: 来自搜索结果的描述
内容: (干净的相关内容)

...
```

## 示例

### 环境变量配置

```bash
# 百炼 API 配置(在 .env 或环境变量中)
export DASHSCOPE_API_KEY="your-bailian-api-key"

# 可选:默认结果数量
export BAILIAN_SEARCH_DEFAULT_COUNT=5
```

### 脚本调用示例

```bash
#!/bin/bash
# search-example.sh - 搜索调用示例

# 基础搜索
echo "=== 基础搜索 ==="
./scripts/mcp-websearch.sh "Python 异步编程"

# 指定数量
echo "=== 指定数量 ==="
./scripts/mcp-websearch.sh "Python 异步编程" 10

# 搜索并保存结果
echo "=== 保存结果 ==="
./scripts/mcp-websearch.sh "Python 异步编程" 5 > search-results.txt
echo "结果已保存到 search-results.txt"
```

### 集成到 AI 工作流

```bash
#!/bin/bash
# ai-workflow-search.sh - AI 工作流中的搜索集成

QUERY="$1"
COUNT="${2:-5}"

# 调用搜索
RESULTS=$(./scripts/mcp-websearch.sh "$QUERY" "$COUNT")

# 将结果传递给 AI 处理
# (由 AI Agent 解析并基于结果生成回答)
echo "$RESULTS"
```

### 多轮搜索与结果归档

```bash
#!/bin/bash
# multi-round-search.sh - 多轮搜索与归档
TOPIC="$1"
DATE=$(date +%Y%m%d)

# 第一轮:广泛搜索
echo "=== 第一轮:广泛搜索 ==="
./scripts/mcp-websearch.sh "$TOPIC" 10 > "round1-${DATE}.txt"

# 第二轮:聚焦搜索(基于第一轮结果细化)
echo "=== 第二轮:聚焦搜索 ==="
./scripts/mcp-websearch.sh "${TOPIC} 最佳实践" 5 > "round2-${DATE}.txt"

# 合并结果
cat "round1-${DATE}.txt" "round2-${DATE}.txt" > "research-${TOPIC}-${DATE}.md"
echo "调研结果已归档到 research-${TOPIC}-${DATE}.md"
```

## 最佳实践

1. **查询词要具体**:"Python asyncio 基本用法" 优于 "Python"。
2. **合理设置结果数**:事实查询用 3-5 条,深度调研用 10-20 条。
3. **结合 AI 处理**:搜索结果交给 AI 解析,提取关键信息生成回答。
4. **避免频繁请求**:注意 API 调用频率,避免触发限流。
5. **结果缓存**:相同查询结果可缓存,减少重复请求。
6. **多角度查询**:复杂主题用不同关键词多次查询,获取全面信息。

## 常见问题

### Q1: API 调用失败怎么办?
- 检查 `DASHSCOPE_API_KEY` 是否正确配置
- 确认网络可访问百炼 API 服务
- 检查 API 配额是否耗尽
- 查看错误信息,确认查询参数是否合法

### Q2: 搜索结果质量不佳?
- 优化查询词,使其更具体
- 增加结果数量获取更多候选
- 尝试用不同关键词重新搜索
- 结合 AI 对结果进行二次筛选

### Q3: 结果数量上限是多少?
单次查询最多返回 20 条结果。如需更多,可分页查询或用不同关键词多次搜索。

### 已知限制
免费版提供核心搜索能力,结果数量上限 20 条。如需批量搜索、结果缓存、搜索历史、多查询并发等高阶能力,请升级至专业版。

### Q5: 如何缓存搜索结果?
```bash
# 简单缓存:按查询词哈希命名
CACHE_KEY=$(echo -n "$QUERY" | md5sum | awk '{print $1}')
CACHE_FILE="cache/${CACHE_KEY}.txt"

if [ -f "$CACHE_FILE" ]; then
  cat "$CACHE_FILE"
else
  ./scripts/mcp-websearch.sh "$QUERY" 5 > "$CACHE_FILE"
  cat "$CACHE_FILE"
fi
```

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **网络**: 需可访问百炼 API 服务
- **Shell**: Bash / Zsh(用于运行脚本)

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| mcp-websearch.sh | 脚本工具 | 必需 | 随 Skill 安装 |
| curl | 网络工具 | 必需 | 系统自带 |
| 百炼 API | 数据源 | 必需 | 阿里云百炼服务订阅 |
| DASHSCOPE_API_KEY | API Key | 必需 | 阿里云百炼控制台获取 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- **DASHSCOPE_API_KEY**:百炼(阿里云模型工作室)API Key
  - 获取方式:阿里云百炼控制台 -> API Key 管理
  - 配置方式:环境变量或 `.env` 文件
- 本 Skill 基于Markdown指令,除百炼 API Key 外无需额外配置

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |
