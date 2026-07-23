---
slug: "search-2"
name: "search-2"
version: "0.1.0"
displayName: "Search"
summary: "用Tavily的LLM优化搜索API搜网,返相关结果与片段"
license: "Proprietary"
description: |-
  Search the web using Tavily's LLM-optimized search API。Returns relevant
  results with content sni。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Research
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# Search

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Search the web using Tavily's LLM-optimized search API | 支持 | 支持 |
| Returns relevant | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Search the web using Tavily's LLM-optimized search API
- Returns relevant
  results with content sni
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Using the Script

```bash
./scripts/search.sh '<json>'
```

**Examples:**

```bash
./scripts/search.sh '{"query": "python async patterns"}'

./scripts/search.sh '{"query": "React hooks tutorial", "max_results": 10}'

./scripts/search.sh '{"query": "AI news", "topic": "news", "time_range": "week", "max_results": 10}'

./scripts/search.sh '{"query": "machine learning", "include_domains": ["arxiv.org", "github.com"], "search_depth": "advanced"}'
```

### Basic Search

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "latest developments in quantum computing",
    "max_results": 5
  }'
```

### Advanced Search

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "machine learning best practices",
    "max_results": 10,
    "search_depth": "advanced",
    "include_domains": ["arxiv.org", "github.com"],
    "chunks_per_source": 3
  }'
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


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### News Search

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "AI news today",
    "topic": "news",
    "time_range": "day",
    "max_results": 10
  }'
```

### Domain-Filtered Search

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "Python async best practices",
    "include_domains": ["docs.python.org", "realpython.com", "github.com"],
    "search_depth": "advanced"
  }'
```

### Search with Full Content

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "React hooks tutorial",
    "max_results": 3,
    "include_raw_content": true
  }'
```

### Finance Search

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "AAPL earnings Q4 2024",
    "topic": "finance",
    "max_results": 10
  }'
```

## 常见问题

### Q1: 如何开始使用Search？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Search有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 
