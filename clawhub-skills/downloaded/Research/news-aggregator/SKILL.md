---
slug: news-aggregator
name: news-aggregator
version: "1.0.3"
displayName: News Aggregator
summary: 国内外社会、科技、军事新闻汇总。自动搜索、筛选、整理新闻要点。
license: MIT
description: |-
  国内外社会、科技、军事新闻汇总。自动搜索、筛选、整理新闻要点。

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 科技, 筛选, aggregator, 军事新闻汇总, 国内外社会, 自动搜索, news
tags:
- Research
tools:
- read
- exec
---

# News Aggregator

聚合国内外社会、科技、军事新闻，自动筛选要点。

## 新闻源

### 国内科技

* 36氪 (<https://36kr.com/information/tech/>)
* 机器之心 (<https://www.jiqizhixin.com/>)
* 量子位 (<https://www.1baijia.com/>)
* IT之家 (<https://www.ithome.com/>)

### 国内军事

* 观察者网 (<https://www.guancha.cn/>)
* 澎湃新闻 (<https://www.thepaper.cn/>)
* 腾讯军事 (<https://new.qq.com/om/mil/>)

### 国际科技

* TechCrunch
* The Verge
* Wired
* Ars Technica

### 国际军事

* Defense News
* Jane's Defence
* Military Times

## 工作流

1. **搜索** - 用 tavily 或 web_fetch 搜索各源
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
