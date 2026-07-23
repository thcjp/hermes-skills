---
slug: geo-rank-architect
name: geo-rank-architect
version: 1.0.0
displayName: GEO搜索占位架构师
summary: AI搜索时代品牌霸屏,5维GEO评分+JSON-LD注入+评分门控,提升AI引用率
license: Proprietary
description: 'GEO搜索占位架构师——AI搜索时代品牌霸屏利器,5维GEO评分+JSON-LD注入+评分门控,提升AI搜索引擎引用率。核心能力: JSON-LD结构化数据注入
  / FAQ Schema自动生成 / 5维GEO评分模型 / llms。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。'
homepage: https://skillhub.cn
tags:
- AI搜索优化
- GEO
- 品牌占位
- 结构化数据
tools:
- read
- exec
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# GEO搜索占位架构师

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| **GEO优化** | 内容生成后发布前 | 注入JSON-LD结构化数据+FAQ+评分优化 |
| **GEO评分** | 内容质量审核 | geo_score>=60才允许发布,不达标自动重试 |
| **FAQ生成** | 内容优化时 | 自动生成3-5个FAQ片段,提升AI引用率 |
| **AI搜索占位** | 品牌词搜索优化 | 优化内容结构,提升在AI搜索引擎中的引用概率 |
| **多区域SEO** | 跨区域内容发布 | 针对不同区域搜索习惯优化内容结构 |

**关键原则**: 本工具只承诺"优化",不承诺"排名"。通过结构化数据和内容质量提升,增加AI搜索引擎引用内容的概率。

---

## 工作流

### 工作流1: GEO优化流程

1. **接收内容**: 获取图文内容或视频描述文本
2. **评估SEO基础指标**: 分析关键词密度、标题结构、meta标签
3. **注入JSON-LD结构化数据**: 根据内容类型注入Article/FAQPage/Organization/HowTo等Schema
4. **评估AI引用潜力评分**: 基于5维度11项指标进行评分
5. **生成llms_txt摘要**: 生成AI友好的内容摘要
6. **生成FAQ Schema**: 自动生成3-5个FAQ片段
7. **计算GEO评分**: 0-100分加权计算
8. **评分门控**: GEO评分<60时自动优化重试(最多2次)
9. **输出优化结果**: 优化后内容+GEO评分+各维度详情

### 工作流2: GEO评分流程

1. **接收内容文本**
2. **5维度评分**:
   - 结构化数据(25%): JSON-LD存在+Schema类型正确+无语法错误
   - 内容引用潜力(25%): 有数据支撑+有权威引用+FAQ片段+直接回答
   - AI可访问性(20%): robots.txt允许AI爬虫+无noindex+内容可提取
   - E-E-A-T信号(15%): 作者信息+机构信息+日期+来源标注
   - 内容质量(15%): 原创性+深度(>=500字)+可读性
3. **加权计算总分**
4. **返回评分+各维度详情**

---

## 输入格式

### 优化模式

```json
{
  "action": "optimize",
  "content": "文章正文内容...",
  "content_type": "article",
  "title": "AI编程启蒙第3课"
}
```

| 字段 | 类型 | 必填 | 说明 |
|:-----|:-----|:----:|:-----|
| action | string | 是 | 操作类型: optimize(优化)/score(评分) |
| content | string | 是 | 内容正文 |
| content_type | string | 否 | 内容类型: article/howto/faq/product,默认article |
| title | string | 否 | 内容标题 |

### 评分模式

```json
{
  "action": "score",
  "content": "文章内容..."
}
```

---

## 输出格式

### 优化模式输出

```json
{
  "success": true,
  "data": {
    "optimized_content": "优化后的内容(含JSON-LD结构化数据)",
    "geo_score": 72,
    "score_details": {
      "structured_data": 80,
      "citation_potential": 70,
      "ai_accessibility": 75,
      "eeat_signals": 65,
      "content_quality": 70
    },
    "json_ld": {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "AI编程启蒙第3课",
      "author": {"@type": "Person", "name": "作者名"},
      "datePublished": "2026-07-17",
      "description": "内容描述"
    },
    "faq_schema": [
      {"question": "什么是AI编程启蒙?", "answer": "AI编程启蒙是..."},
      {"question": "适合什么年龄段?", "answer": "适合6-12岁..."},
      {"question": "需要什么基础?", "answer": "零基础即可开始..."}
    ],
    "llms_txt": "本文介绍AI编程启蒙第3课的核心内容,涵盖...",
    "retry_count": 0,
    "optimization_notes": [
      "已注入Article类型JSON-LD结构化数据",
      "已生成3个FAQ片段提升AI引用潜力",
      "已补充作者信息和发布日期增强EEAT信号"
    ]
  },
  "error": null,
  "code": null
}
```

### 评分模式输出

```json
{
  "success": true,
  "data": {
    "total": 72.5,
    "details": {
      "structured_data": 80,
      "citation_potential": 70,
      "ai_accessibility": 75,
      "eeat_signals": 65,
      "content_quality": 70
    },
    "suggestions": [
      "建议增加FAQ片段以提升引用潜力",
      "建议补充作者权威信息以增强EEAT信号",
      "建议添加数据支撑以增强内容可信度"
    ]
  },
  "error": null,
  "code": null
}
```

---

## GEO评分模型

| 类别 | 权重 | 检查项 | 满分标准 |
|:-----|:-----|:-------|:---------|
| 结构化数据 | 25% | JSON-LD存在+Schema类型正确+无语法错误 | 含Article/HowTo/FAQ三种Schema |
| 内容引用潜力 | 25% | 有数据支撑+有权威引用+FAQ片段+直接回答 | 含数据+引用+FAQ+直接回答格式 |
| AI可访问性 | 20% | robots.txt允许AI爬虫+无noindex+内容可提取 | 全部满足 |
| E-E-A-T信号 | 15% | 作者信息+机构信息+日期+来源标注 | 四项信息齐全 |
| 内容质量 | 15% | 原创性+深度(>=500字)+可读性 | 原创+500字以上+结构清晰 |

**评分门控规则**:
- GEO评分 >= 60: 允许发布
- GEO评分 < 60: 自动优化重试(最多2次)
- 2次重试后仍 < 60: 标记warning,建议人工审核

---

## JSON-LD结构化数据类型

根据内容类型自动选择注入的Schema类型:

| 内容类型 | Schema类型 | 说明 |
|:---------|:-----------|:-----|
| article | Article | 文章类内容 |
| howto | HowTo | 教程/指南类内容 |
| faq | FAQPage | 问答类内容 |
| product | Product | 产品介绍类内容 |

**必填字段**:
- Article: headline, author, datePublished, description
- HowTo: name, step[], totalTime, supply[]
- FAQPage: mainEntity[](question + answer)
- Product: name, description, brand, offers

---

## 业务规则

| 规则 | 阈值 |
|:-----|:-----|
| GEO评分门控 | geo_score >= 60才允许发布 |
| JSON-LD结构化数据 | 每篇必须添加Article/HowTo/FAQ之一 |
| llms.txt摘要 | 每篇必须生成AI友好摘要 |
| E-E-A-T信号 | Experience+Expertise+Authoritativeness+Trustworthiness四维度 |
| FAQ片段数量 | 每篇3-5个FAQ |
| AI可引用格式 | 引用块+表格+编号列表 |

---

## 异常处理

| 异常类型 | 错误代码 | 处理方式 |
|:---------|:---------|:---------|
| SEO基础评估失败 | SEO_FALLBACK | 仅执行GEO优化,跳过SEO部分 |
| JSON-LD注入失败 | JSONLD_ERROR | 降级为纯文本优化,标记warning |
| GEO评分持续<60 | GEO_LOW_SCORE | 标记warning+建议人工审核 |
| 内容为空 | EMPTY_CONTENT | 返回错误,提示输入内容 |
| FAQ生成失败 | FAQ_GEN_ERROR | 跳过FAQ,仅输出JSON-LD和评分 |
| llms_txt生成失败 | LLMS_TXT_ERROR | 跳过摘要生成,不影响其他功能 |

---

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 |

### API Key 配置
- **LLM_API_KEY**: 必需(通常由Agent内置) - JSON-LD注入/FAQ生成/llms.txt摘要/GEO评分
- 配置方式: 在Agent的环境变量中设置

### 使用流程
纯LLM驱动,GEO评分门控自动优化重试(最多2次)。只承诺优化,不承诺排名。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例

**输入**:
```json
{
  "action": "optimize",
  "content": "AI编程启蒙课程介绍,本课程面向6-12岁少儿,通过Scratch图形化编程入门...",
  "content_type": "article",
  "title": "AI编程启蒙第3课"
}
```

**输出**:
- GEO评分: 72/100
- 各维度: 结构化数据80/引用潜力70/AI可访问性75/EEAT信号65/内容质量70
- JSON-LD: Article类型,含headline/author/datePublished
- FAQ: 3个问答("什么是AI编程启蒙?"/"适合什么年龄?"/"需要什么基础?")
- llms_txt: "本文介绍AI编程启蒙第3课的核心内容..."
- 优化说明: 已注入结构化数据/已生成FAQ/已补充EEAT信号
- 重试次数: 0

### 示例2: 教程内容GEO优化

**输入**:
```json
{
  "action": "optimize",
  "content": "教你用Scratch制作一个简单的动画,分5步完成...",
  "content_type": "howto",
  "title": "Scratch动画制作教程"
}
```

**输出**:
- GEO评分: 78/100
- JSON-LD: HowTo类型,含name/step[]/totalTime
- FAQ: 3个问答("Scratch是什么?"/"需要安装软件吗?"/"适合几岁孩子?")
- 优化说明: 已注入HowTo Schema/已生成FAQ/已补充步骤说明

## 核心能力

- GEO搜索占位架构师——AI搜索时代品牌霸屏利器,5维GEO评分+JSON-LD注入+评分门控,提升AI搜索引擎引用率
- 核心能力: JSON-LD结构化数据注入 / FAQ Schema自动生成 / 5维GEO评分模型 / llms
- 评分门控低于60自动优化重试最多2次
- 只承诺优化不承诺排名,通过结构化数据科学提升AI引用概率
- 触发关键词: AI搜索占位、GEO优化、生成式引擎优化、JSON-LD、FAQ Schema、AI引用、搜索霸屏、品牌占位、结构化数据、AI搜索优化

## 常见问题

### Q1: 如何开始使用GEO搜索占位架构师？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: GEO搜索占位架构师有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 性能取决于底层模型能力
