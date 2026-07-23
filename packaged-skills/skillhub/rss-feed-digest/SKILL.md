---
slug: "rss-feed-digest"
name: "rss-feed-digest"
version: "1.0.0"
displayName: "RSS Feed Digest"
summary: "抓取/过滤/汇总RSS与Atom为日或周报,支持多源"
license: "Proprietary"
description: |-
  Fetch, filter, and summarize RSS/Atom feeds into a clean daily or weekly
  digest。Supports multipl。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
  - Research
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# RSS Feed Digest

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Rss Feed Digest 核心处理 - 按流程执行步端到端pipeline配置流程 | 支持 | 支持 |
| Rss Feed Digest 智能分析 - 步骤间自动质量gate检查 | 不支持 | 支持 |
| Rss Feed Digest 批量处理 - 支持多种变体等多种处理模式 | 不支持 | 支持 |
| Rss Feed Digest 自定义配置 - 失败自动重试+断点续传 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Rss Feed Digest 结果导出 - 按流程执行步端到端pipeline配置流程
- Rss Feed Digest 实时监控 - 步骤间自动质量gate检查
- Rss Feed Digest 错误重试 - 支持多种变体等多种处理模式
- Rss Feed Digest 多格式支持 - 失败自动重试+断点续传
- Rss Feed Digest 扩展能力9 - 全流程可追溯, 输出执行日志
#
## 适用场景

* **Daily briefings**: Summarize industry news for your team
* **Newsletter automation**: Generate content for Beehiiv/Substack newsletters
* **Competitive monitoring**: Track mentions of competitors or keywords
* **Research**: Aggregate academic/industry feeds on a topic
* **Heartbeat integration**: Run during Skill平台 heartbeat to check for relevant news

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | rss-feed-digest处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "digest_result": "digest_result_value",
      "digest_metadata": "digest_metadata_value",
      "digest_status": "digest_status_value"
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

中间产物模板参考: `assets/rss-feed-digest_template`

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

```bash
https://hnrss.org/frontpage
https://feeds.arstechnica.com/arstechnica/technology-lab
https://www.artificialintelligence-news.com/feed/
https://openai.com/blog/rss.xml

python3 rss_digest.py fetch --feed-file feeds.txt --keywords "AI,LLM,GPT,Claude,agent" --hours 24 --output /tmp/daily-ai-digest.md
```

## 常见问题

### Q1: 如何开始使用RSS Feed Digest？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: RSS Feed Digest有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

