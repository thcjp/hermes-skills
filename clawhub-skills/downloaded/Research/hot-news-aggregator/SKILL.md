---
slug: hot-news-aggregator
name: hot-news-aggregator
version: "1.0.0"
displayName: hot-news-aggregator
summary: 国内外社会、科技、军事新闻汇总。自动搜索、筛选、整理新闻要点。Use When 需要获取最新的国内外社会、科技、军事新闻，并且希望自动筛选和整理新闻要点时。
license: MIT-0
description: |-
  国内外社会、科技、军事新闻汇总。自动搜索、筛选、整理新闻要点。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# hot-news-aggregator

聚合国内外社会、科技、军事新闻，自动筛选要点。

## 新闻源

国内科技

* 36氪: `https://36kr.com/information/tech`
* 机器之心: `https://www.jiqizhixin.com`
* 量子位: `https://www.1baijia.com`
* IT之家: `https://www.ithome.com`

国内军事

* 观察者网: `https://www.guancha.cn`
* 澎湃新闻: `https://www.thepaper.cn`
* 腾讯军事: `https://new.qq.com/om/mil`

国际科技

* TechCrunch: `https://techcrunch.com`
* The Verge: `https://www.theverge.com`
* Wired: `https://www.wired.com`
* Ars Technica: `https://arstechnica.com`

国际军事

* Defense News: `https://www.defensenews.com`
* Jane's Defence: `https://www.janes.com`
* Military Times: `https://www.militarytimes.com`

## 工作流

1. **搜索** - 用 `web_search` 或 `web_fetch` 工具搜索各源
2. **筛选** - 过滤重复、过期、不可靠来源
3. **整理** - 按类别整理，每条含标题、来源、要点
4. **输出** - 生成结构化汇总

## 可信度规则

**优先：**

* 官方媒体报道
* 权威机构发布

**谨慎：**

* 论坛帖子
* 匿名消息
* 二手转载

## 输出格式

```markdown
## 科技新闻

1. [标题](链接)
   来源：xxx | 时间：xxx
   要点：xxx

## 军事新闻

1. [标题](链接)
   来源：xxx | 时间：xxx
   要点：xxx
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 国内外社会、科技、军事新闻汇总
- 自动搜索、筛选、整理新闻要点
- Use When 需要获取最新的国内外社会、科技、军事新闻，并且希望自动筛选和整理新闻要点时
- 触发关键词: hot, 科技, 筛选, aggregator, hot-news-aggregator, 军事新闻汇总, 国内外社会, 自动搜索

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用hot-news-aggregator？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: hot-news-aggregator有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
