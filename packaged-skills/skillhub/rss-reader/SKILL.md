---
slug: "rss-reader"
name: "rss-reader"
version: "1.0.0"
displayName: "RSS Reader"
summary: "监控RSS与Atom订阅做内容研究,追踪博客/新闻/邮件"
license: "Proprietary"
description: |-
  Monitor RSS and Atom feeds for content research。Track blogs, news sites,
  newsletters, and any fe。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修。适用于独立开发者、企业团队和自动化工作流场景。
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
# RSS Reader

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Monitor RSS and Atom feeds for content research | 支持 | 支持 |
| Track blogs, news sites, | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Monitor RSS and Atom feeds for content research
- Track blogs, news sites,
  newsletters, and any fe
#
## 适用场景

### Content Research

Monitor competitor blogs, industry publications, and thought leaders:

```bash
node scripts/rss.js add "https://competitor.com/blog/feed" --category competitors
node scripts/rss.js add "https://techcrunch.com/feed" --category news
node scripts/rss.js add "https://news.ycombinator.com/rss" --category tech

node scripts/rss.js check --since 24h --format ideas
```

### Newsletter Aggregation

Track newsletters and digests:

```bash
node scripts/rss.js add "https://newsletter.com/feed" --category newsletters
```

### Keyword Monitoring

Filter items by keywords:

```bash
node scripts/rss.js check --keywords "AI,agents,automation"
```

## 使用流程

```bash
node scripts/rss.js add "https://example.com/feed.xml" --category tech

node scripts/rss.js check

node scripts/rss.js check --category tech

node scripts/rss.js list

node scripts/rss.js remove "https://example.com/feed.xml"
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明"
  },
  "error": null
}
```

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

### 示例1：基础用法

```
```bash
node scripts/rss.js add "https://example.com/feed.xml" --category tech

node scripts/rss.js check

node scripts/rss.js check --category tech

node scripts/rss.js list

node scripts/rss.js remove "https://example.com/feed.xml"
```
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪。

### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界。

