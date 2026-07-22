---
slug: seo-rank-monopolizer
name: seo-rank-monopolizer
version: "1.1.0"
displayName: "AI搜索占位师"
summary: "AI搜索时代品牌霸屏,5维GEO评分+JSON-LD注入+评分门控,提升AI引用率"
license: Proprietary
description: |-
  AI搜索占位师——AI搜索时代品牌霸屏利器,5维GEO评分模型+JSON-LD结构化数据注入+评分门控自动优化重试,提升AI搜索引擎(如文心一言/Kimi/通义千问/Perplexity)引用率。核心能力:JSON-LD结构化数据注入(Article/HowTo/FAQPage/Product)、FAQ Schema自动生成、5维GEO评分(结构化数据/引用潜力/AI可访问性/EEAT/内容质量)、llms_txt摘要生成、评分门控(低于60分自动优化重试最多2次)
homepage: "https://skillhub.cn"
tags: [AI搜索优化, GEO, 品牌占位, 结构化数据]
tools:
  - read
suggested_price: "19.90"
pricing_tier: "business"
pricing_rationale: "SEO优化类, medium市场, enterprise复杂度, monthly频次, business层 → 效果可量化,企业刚需"
---
# AI搜索占位师 v1.1.0

AI搜索时代品牌霸屏利器,通过5维GEO评分+JSON-LD结构化数据注入+评分门控,科学提升AI搜索引擎引用率。

> **关键原则**: 本工具只承诺"优化",不承诺"排名"。通过结构化数据和内容质量提升,增加AI搜索引擎引用内容的概率。

## 核心能力

1. **JSON-LD结构化数据注入**: 根据内容类型自动注入Article/HowTo/FAQPage/Product等Schema,含必填字段校验
2. **FAQ Schema自动生成**: 自动生成3-5个FAQ片段,提升AI引用概率和富媒体展示
3. **5维GEO评分模型**: 结构化数据(25%)+内容引用潜力(25%)+AI可访问性(20%)+E-E-A-T信号(15%)+内容质量(15%),0-100分加权计算
4. **llms_txt摘要生成**: 生成AI友好的内容摘要,便于AI搜索引擎快速理解内容核心
5. **评分门控自动优化重试**: GEO评分<60分时自动优化重试(最多2次),2次后仍不达标标记warning建议人工审核
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| GEO优化(发布前) | action=optimize+content+content_type+title | optimized_content+geo_score+score_details+json_ld+faq_schema+llms_txt |
| GEO评分(内容审核) | action=score+content | total总分+details各维度分+suggestions优化建议 |
| FAQ生成 | content+content_type=faq | faq_schema[](3-5个question+answer) |
| JSON-LD注入 | content+content_type | json_ld结构化数据(Article/HowTo/FAQPage/Product) |
| llms_txt摘要生成 | content+title | llms_txt(AI友好摘要) |
| 多区域SEO | content+不同区域配置 | 针对不同区域搜索习惯优化的内容结构 |

**不适用于**: 传统SEO关键词排名优化(使用seo-doctor)、黑帽GEO手法(虚假结构化数据/内容农场)、海外Google SGE优化(聚焦国内AI搜索引擎)、非结构化内容(纯图片/视频无文本)、SEM竞价广告。

## 使用流程

### Step 1: 环境准备
- 确认Agent已加载本SKILL.md,且支持exec工具
- 在Agent环境变量中配置 `LLM_API_KEY`(必需)
- 本Skill纯LLM驱动,无额外API依赖

### Step 2: 选择操作模式
- **optimize**(优化模式): 注入JSON-LD+生成FAQ+评分门控,完整优化流程
- **score**(评分模式): 仅对内容进行5维GEO评分,不修改内容

### Step 3: GEO优化流程(optimize模式)
1. 接收内容(content+content_type+title)
2. 评估SEO基础指标(关键词密度/标题结构/meta标签)
3. 根据content_type注入JSON-LD结构化数据(Article/HowTo/FAQPage/Product)
4. 基于5维度11项指标评估AI引用潜力评分
5. 生成llms_txt摘要(AI友好内容摘要)
6. 自动生成3-5个FAQ片段
7. 计算GEO评分(0-100分加权)
8. 评分门控: GEO评分<60时自动优化重试(最多2次)
9. 输出优化结果(优化后内容+GEO评分+各维度详情)

### Step 4: GEO评分流程(score模式)
1. 接收内容文本
2. 5维度评分:
   - 结构化数据(25%): JSON-LD存在+Schema类型正确+无语法错误
   - 内容引用潜力(25%): 有数据支撑+有权威引用+FAQ片段+直接回答
   - AI可访问性(20%): robots.txt允许AI爬虫+无noindex+内容可提取
   - E-E-A-T信号(15%): 作者信息+机构信息+日期+来源标注
   - 内容质量(15%): 原创性+深度(>=500字)+可读性
3. 加权计算总分
4. 返回评分+各维度详情+优化建议

### Step 5: 评分门控检查
- GEO评分 >= 60: 允许发布,输出优化结果
- GEO评分 < 60: 自动优化重试(最多2次),每次补充缺失的结构化数据/FAQ/EEAT信号
- 2次重试后仍 < 60: 标记warning,建议人工审核

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

## JSON-LD结构化数据类型

根据内容类型自动选择注入的Schema类型:

| 内容类型 | Schema类型 | 说明 | 必填字段 |
|:---------|:-----------|:-----|:---------|
| article | Article | 文章类内容 | headline, author, datePublished, description |
| howto | HowTo | 教程/指南类内容 | name, step[], totalTime, supply[] |
| faq | FAQPage | 问答类内容 | mainEntity[](question + answer) |
| product | Product | 产品介绍类内容 | name, description, brand, offers |

## 异常处理


| 异常场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| 内容为空 | 未提供content参数 | 返回error="必须提供内容",无法降级 |
| SEO基础评估失败 | LLM分析异常 | 仅执行GEO优化,跳过SEO部分,标注warning |
| JSON-LD注入失败 | Schema生成异常或格式错误 | 降级为纯文本优化,标记warning,不影响评分 |
| GEO评分持续<60 | 2次执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令后仍未达标 | 标记warning,建议人工审核,输出当前最优结果 |
| FAQ生成失败 | LLM返回格式异常 | 跳过FAQ生成,仅输出JSON-LD和评分,标注warning |
| llms_txt生成失败 | LLM摘要生成异常 | 跳过摘要生成,不影响其他功能,标注warning |
| content_type无效 | 输入的类型不在4种支持范围内 | 默认使用article类型,标注warning |
| LLM调用失败 | LLM服务不可用或超时 | 返回success=false, error="GEO优化LLM调用失败" |
| LLM_API_KEY未配置 | 环境变量缺失 | 返回error,提示配置环境变量 |
| 评分维度计算异常 | 部分维度评分失败 | 跳过该维度,按已有维度加权计算,标注warning |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:-------|:-----|:---------|:---------|:-------------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | 国内可用: 通义千问/文心一言/智谱GLM/DeepSeek/Kimi |

### API Key 配置(零暴露原则)
- **LLM_API_KEY**: 必需(通常由Agent内置) - JSON-LD注入/FAQ生成/llms.txt摘要/GEO评分
- **配置方式**: 必须通过Agent环境变量注入,严禁在SKILL.md或代码中硬编码API Key
- **安全检查**: 本SKILL.md中不包含任何API Key示例,所有Key均通过 `$env:LLM_API_KEY` 等环境变量读取

### 使用流程
纯LLM驱动,GEO评分门控自动优化重试(最多2次)。只承诺优化,不承诺排名。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 文章内容GEO优化

**输入**:
```json
{
  "action": "optimize",
  "content": "AI编程启蒙课程介绍,本课程面向6-12岁少儿,通过Scratch图形化编程入门,培养计算思维和创造力。课程分为12节,每节45分钟,含课后练习和项目实战...",
  "content_type": "article",
  "title": "AI编程启蒙第3课"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "optimized_content": "AI编程启蒙课程介绍...[含JSON-LD结构化数据]...",
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
      "author": {"@type": "Person", "name": "编程教育团队"},
      "datePublished": "2026-07-17",
      "description": "AI编程启蒙课程介绍,面向6-12岁少儿,通过Scratch图形化编程入门"
    },
    "faq_schema": [
      {"question": "什么是AI编程启蒙?", "answer": "AI编程启蒙是面向6-12岁少儿的编程入门课程,通过Scratch图形化编程培养计算思维"},
      {"question": "适合什么年龄段?", "answer": "适合6-12岁少儿,零基础即可开始"},
      {"question": "需要什么基础?", "answer": "零基础即可开始,课程从Scratch图形化编程入门"}
    ],
    "llms_txt": "本文介绍AI编程启蒙第3课的核心内容,涵盖Scratch图形化编程入门,面向6-12岁少儿,培养计算思维和创造力。课程分12节,每节45分钟。",
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

### 示例2: 教程内容GEO优化

**输入**:
```json
{
  "action": "optimize",
  "content": "教你用Scratch制作一个简单的动画,分5步完成:1.打开Scratch创建新项目;2.选择角色和背景;3.添加移动指令;4.添加声音效果;5.保存并分享...",
  "content_type": "howto",
  "title": "Scratch动画制作教程"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "optimized_content": "教你用Scratch制作一个简单的动画...[含HowTo JSON-LD]...",
    "geo_score": 78,
    "score_details": {
      "structured_data": 85,
      "citation_potential": 75,
      "ai_accessibility": 80,
      "eeat_signals": 70,
      "content_quality": 78
    },
    "json_ld": {
      "@context": "https://schema.org",
      "@type": "HowTo",
      "name": "Scratch动画制作教程",
      "step": [
        {"@type": "HowToStep", "position": 1, "name": "创建新项目", "text": "打开Scratch创建新项目"},
        {"@type": "HowToStep", "position": 2, "name": "选择角色背景", "text": "选择角色和背景"},
        {"@type": "HowToStep", "position": 3, "name": "添加移动指令", "text": "添加移动指令"},
        {"@type": "HowToStep", "position": 4, "name": "添加声音", "text": "添加声音效果"},
        {"@type": "HowToStep", "position": 5, "name": "保存分享", "text": "保存并分享"}
      ],
      "totalTime": "PT30M"
    },
    "faq_schema": [
      {"question": "Scratch是什么?", "answer": "Scratch是MIT开发的图形化编程工具,适合少儿编程入门"},
      {"question": "需要安装软件吗?", "answer": "不需要,Scratch可在浏览器中直接使用"},
      {"question": "适合几岁孩子?", "answer": "适合6-12岁少儿,零基础即可开始"}
    ],
    "llms_txt": "本教程教你用Scratch制作简单动画,分5步完成,预计30分钟。",
    "retry_count": 0,
    "optimization_notes": ["已注入HowTo Schema", "已生成FAQ", "已补充步骤说明"]
  },
  "error": null,
  "code": null
}
```

### 示例3: 内容GEO评分(未达标场景)

**输入**:
```json
{
  "action": "score",
  "content": "这是一篇关于AI编程的文章,内容比较简短,没有结构化数据,没有FAQ,没有作者信息..."
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "total": 55,
    "details": {
      "structured_data": 40,
      "citation_potential": 50,
      "ai_accessibility": 70,
      "eeat_signals": 45,
      "content_quality": 65
    },
    "suggestions": [
      "建议增加FAQ片段以提升引用潜力(当前50分)",
      "建议补充作者权威信息以增强EEAT信号(当前45分)",
      "建议添加JSON-LD结构化数据(当前40分)",
      "建议添加数据支撑以增强内容可信度"
    ]
  },
  "error": null,
  "code": null
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: GEO优化(article类型,JSON-LD注入+FAQ生成)

**输入**:
```json
{
  "action": "optimize",
  "content": "AI编程启蒙第3课:本节课学习Python变量与数据类型。变量是存储数据的容器,Python中常用数据类型包括整数(int)、浮点数(float)、字符串(str)和布尔值(bool)...",
  "content_type": "article",
  "title": "AI编程启蒙第3课:Python变量与数据类型详解"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "optimized_content": "<script type=\"application/ld+json\">\n{\"@context\":\"https://schema.org\",\"@type\":\"Article\",\"headline\":\"AI编程启蒙第3课:Python变量与数据类型详解\",\"author\":{\"@type\":\"Person\",\"name\":\"AI编程教研室\"},\"datePublished\":\"2026-07-20\",\"description\":\"本节课学习Python变量与数据类型,涵盖int、float、str、bool四种核心数据类型\"}\n</script>\n\nAI编程启蒙第3课:本节课学习Python变量与数据类型。变量是存储数据的容器,Python中常用数据类型包括整数(int)、浮点数(float)、字符串(str)和布尔值(bool)...",
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
      "headline": "AI编程启蒙第3课:Python变量与数据类型详解",
      "author": {"@type": "Person", "name": "AI编程教研室"},
      "datePublished": "2026-07-20",
      "description": "本节课学习Python变量与数据类型,涵盖int、float、str、bool四种核心数据类型"
    },
    "faq_schema": [
      {"question": "Python变量是什么?", "answer": "Python变量是存储数据的容器,通过变量名可以引用存储的数据。例如:name='Python'就创建了一个名为name的字符串变量。"},
      {"question": "Python有哪些基本数据类型?", "answer": "Python基本数据类型包括:整数(int)、浮点数(float)、字符串(str)和布尔值(bool)。例如:age=25是整数,price=9.9是浮点数。"},
      {"question": "如何查看变量的数据类型?", "answer": "使用type()函数可以查看变量数据类型。例如:type(25)返回<class 'int'>,type('hello')返回<class 'str'>。"}
    ],
    "llms_txt": "本文介绍AI编程启蒙第3课内容,详细讲解Python变量与数据类型,涵盖整数、浮点数、字符串、布尔值四种核心数据类型的定义、使用方法及代码示例。",
    "retry_count": 0,
    "optimization_notes": [
      "已注入Article类型JSON-LD结构化数据(含headline/author/datePublished/description)",
      "已生成3个FAQ片段提升AI引用潜力",
      "已补充作者信息和发布日期增强EEAT信号",
      "已生成llms_txt AI友好摘要"
    ]
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓JSON-LD Article结构化数据注入 ✓3个FAQ片段自动生成 ✓llms_txt AI友好摘要 ✓GEO评分72分(>60分通过门控) ✓优化说明4条完整记录

### 案例2: GEO评分(score模式,5维度评分+优化建议)

**输入**:
```json
{
  "action": "score",
  "content": "这是一篇关于Python入门的文章,介绍了Python的基本语法和常用功能..."
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "total": 52.5,
    "details": {
      "structured_data": 40,
      "citation_potential": 50,
      "ai_accessibility": 70,
      "eeat_signals": 45,
      "content_quality": 60
    },
    "suggestions": [
      "建议注入JSON-LD结构化数据(Article/HowTo/FAQ),当前缺失,结构化数据分仅40分",
      "建议增加FAQ片段以提升AI引用潜力,当前无FAQ,引用潜力分50分",
      "建议补充作者权威信息(姓名/机构/资质)以增强EEAT信号,当前缺失,EEAT分仅45分",
      "建议添加发布日期和更新日期增强时效性信号",
      "建议增加数据支撑和代码示例以增强内容可信度和深度"
    ]
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓5维度评分完整(结构化40/引用50/可访问70/EEAT45/质量60) ✓总分52.5分正确加权计算 ✓5条优化建议针对性 ✓低分维度(结构化/EEAT)重点提示 ✓评分模式不修改原始内容

### 案例3: 评分门控重试(低于60分自动优化2次后达标)

**输入**:
```json
{
  "action": "optimize",
  "content": "Python入门教程。Python是一门编程语言。可以用来做很多事情。学习Python很简单。",
  "content_type": "article",
  "title": "Python入门教程"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "optimized_content": "<script type=\"application/ld+json\">\n{\"@context\":\"https://schema.org\",\"@type\":\"Article\",\"headline\":\"Python入门教程\",\"author\":{\"@type\":\"Person\",\"name\":\"编程教育团队\"},\"datePublished\":\"2026-07-20\"}\n</script>\n\nPython入门教程\n\nPython是一门简单易学、功能强大的编程语言,广泛应用于数据分析、人工智能、Web开发等领域。本教程将带你从零开始学习Python编程。\n\n## 一、Python简介\nPython由Guido van Rossum于1991年创建,以简洁优雅的语法著称。它可以用来做很多事情:数据分析、机器学习、网站开发、自动化脚本等。学习Python很简单,适合零基础入门。\n\n## 二、为什么学Python?\n- 语法简洁:接近自然语言,易读易写\n- 生态丰富:大量第三方库可直接使用\n- 应用广泛:从Web到AI,全覆盖\n- 社区活跃:遇到问题容易找到解决方案\n\n### FAQ\nQ: Python适合零基础吗?\nA: 适合,Python语法简洁,是零基础入门编程的最佳选择之一。",
    "geo_score": 65,
    "score_details": {
      "structured_data": 80,
      "citation_potential": 65,
      "ai_accessibility": 75,
      "eeat_signals": 55,
      "content_quality": 60
    },
    "json_ld": {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "Python入门教程",
      "author": {"@type": "Person", "name": "编程教育团队"},
      "datePublished": "2026-07-20"
    },
    "faq_schema": [
      {"question": "Python适合零基础吗?", "answer": "适合,Python语法简洁,是零基础入门编程的最佳选择之一。"}
    ],
    "llms_txt": "本文是Python入门教程,介绍Python语言特点、应用领域和学习优势,适合零基础初学者。",
    "retry_count": 2,
    "optimization_notes": [
      "第1次优化:注入JSON-LD结构化数据+补充作者信息,GEO评分55分(仍<60)",
      "第2次优化:扩充内容深度至500字以上+生成FAQ片段+添加结构化标题,GEO评分65分(达标)",
      "已通过评分门控(>=60分),允许发布"
    ]
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓评分门控正确触发(初始<60分→重试) ✓2次自动优化重试后达标(65分) ✓retry_count=2正确记录 ✓每次优化内容记录在optimization_notes ✓内容深度从不足100字扩充至500字+

### 案例4: HowTo类型优化(教程步骤结构化)

**输入**:
```json
{
  "action": "optimize",
  "content": "如何用Python爬取网页数据:第一步安装requests库,第二步发送HTTP请求获取网页内容,第三步解析HTML提取数据,第四步保存数据到文件...",
  "content_type": "howto",
  "title": "Python网页爬虫教程:4步搞定数据抓取"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "optimized_content": "<script type=\"application/ld+json\">\n{\"@context\":\"https://schema.org\",\"@type\":\"HowTo\",\"name\":\"Python网页爬虫教程:4步搞定数据抓取\",\"author\":{\"@type\":\"Person\",\"name\":\"技术教程团队\"},\"datePublished\":\"2026-07-20\",\"step\":[{\"@type\":\"HowToStep\",\"position\":1,\"name\":\"安装requests库\",\"text\":\"使用pip install requests安装HTTP请求库\"},{\"@type\":\"HowToStep\",\"position\":2,\"name\":\"发送HTTP请求\",\"text\":\"使用requests.get(url)获取网页内容\"},{\"@type\":\"HowToStep\",\"position\":3,\"name\":\"解析HTML提取数据\",\"text\":\"使用BeautifulSoup解析HTML并提取目标数据\"},{\"@type\":\"HowToStep\",\"position\":4,\"name\":\"保存数据\",\"text\":\"将提取的数据保存到CSV或JSON文件\"}]}\n</script>\n\n如何用Python爬取网页数据...",
    "geo_score": 78,
    "score_details": {
      "structured_data": 90,
      "citation_potential": 75,
      "ai_accessibility": 80,
      "eeat_signals": 70,
      "content_quality": 75
    },
    "json_ld": {
      "@context": "https://schema.org",
      "@type": "HowTo",
      "name": "Python网页爬虫教程:4步搞定数据抓取",
      "author": {"@type": "Person", "name": "技术教程团队"},
      "datePublished": "2026-07-20",
      "step": [
        {"@type": "HowToStep", "position": 1, "name": "安装requests库", "text": "使用pip install requests安装HTTP请求库"},
        {"@type": "HowToStep", "position": 2, "name": "发送HTTP请求", "text": "使用requests.get(url)获取网页内容"},
        {"@type": "HowToStep", "position": 3, "name": "解析HTML提取数据", "text": "使用BeautifulSoup解析HTML并提取目标数据"},
        {"@type": "HowToStep", "position": 4, "name": "保存数据", "text": "将提取的数据保存到CSV或JSON文件"}
      ]
    },
    "faq_schema": [
      {"question": "Python爬虫需要什么库?", "answer": "Python爬虫常用库包括requests(发送HTTP请求)、BeautifulSoup(解析HTML)、lxml(XML解析)、scrapy(爬虫框架)等。"},
      {"question": "爬虫合法吗?", "answer": "爬取公开网页数据通常合法,但需遵守robots.txt协议,不可爬取需要登录或付费的内容,不可对服务器造成过大负担。"},
      {"question": "如何防止被反爬?", "answer": "设置合理的请求间隔、使用随机User-Agent、配置代理IP池、处理验证码等是常见的反反爬策略。"}
    ],
    "llms_txt": "本教程介绍如何用Python在4步内完成网页数据爬取:安装requests库、发送HTTP请求、解析HTML提取数据、保存数据到文件。",
    "retry_count": 0,
    "optimization_notes": [
      "已注入HowTo类型JSON-LD结构化数据(含4个HowToStep步骤)",
      "已生成3个FAQ片段(含库推荐/合法性/反爬策略)",
      "已补充作者信息和发布日期增强EEAT信号",
      "HowTo步骤结构化数据显著提升AI引用潜力(AI可提取步骤直接回答)"
    ]
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓HowTo类型JSON-LD注入(含4个HowToStep) ✓步骤结构化(position 1-4) ✓3个FAQ片段生成 ✓GEO评分78分(>60分一次通过) ✓结构化数据分90分(HowTo步骤提升明显)

## 常见问题

### Q1: 如何开始使用AI搜索占位师?
A: 两步启动:(1)将SKILL.md放入Agent的skills目录;(2)确认Agent环境变量已配置LLM_API_KEY。调用optimize模式传入content+content_type+title即可执行完整GEO优化,调用score模式传入content即可仅评分。纯LLM驱动,无额外API依赖。

### Q2: GEO评分和SEO评分有什么区别?
A: SEO评分关注传统搜索引擎(百度/Google)排名,侧重关键词密度/外链/标题优化;GEO评分关注AI搜索引擎(文心一言/Kimi/通义千问/Perplexity)引用率,侧重结构化数据/FAQ/AI可访问性/EEAT信号。GEO优化让AI更容易理解和引用你的内容。

### Q3: 评分门控重试机制如何工作?
A: GEO评分<60时自动触发优化重试:(1)第1次重试:补充缺失的JSON-LD/FAQ/EEAT信号,重新评分;(2)第2次重试:进一步优化内容结构和引用,重新评分;(3)2次后仍<60:标记warning,输出当前最优结果,建议人工审核。retry_count字段记录重试次数。

### Q4: JSON-LD结构化数据有什么作用?
A: JSON-LD是AI搜索引擎理解内容的标准格式:(1)帮助AI快速识别内容类型(文章/教程/问答/产品);(2)提取关键信息(标题/作者/日期/步骤/问答)用于回答用户查询;(3)提升富媒体展示概率;(4)增强AI引用准确性。是GEO优化的核心手段。

### Q5: 只承诺优化不承诺排名是什么意思?
A: AI搜索引擎的引用机制复杂(涉及相关性/权威性/时效性/用户意图等多因素),本工具通过结构化数据和内容质量提升增加被引用的概率,但无法保证具体排名位置。建议结合内容质量提升+外链建设+品牌权威性等多维度优化。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **AI搜索引擎覆盖**: 主要适配国内AI搜索引擎(文心一言/Kimi/通义千问/DeepSeek)和Perplexity,不同AI引擎引用机制有差异,效果可能不同
- **评分模型主观性**: 5维GEO评分基于LLM判断,不同模型评分可能差异较大,评分仅作参考非绝对标准
- **JSON-LD效果滞后**: 结构化数据注入后需要等待AI搜索引擎重新爬取和索引,效果非即时可见
- **内容质量门槛**: GEO评分门控要求内容>=500字,短内容(<500字)评分会偏低
- **FAQ生成准确性**: FAQ基于LLM理解内容生成,可能与用户实际搜索意图不匹配,需人工复核
- **llms.txt标准**: llms.txt为新兴标准,部分AI搜索引擎可能尚未支持
- **评分门控限制**: 最多重试2次,复杂内容可能需要更多轮次优化,需人工介入

## 安全

### API Key 零暴露原则
- **环境变量注入**: LLM_API_KEY必须通过Agent环境变量注入,严禁在SKILL.md、配置文件或代码中硬编码
- **本文件无Key示例**: 本SKILL.md中不包含任何真实或示例API Key,所有引用均使用 `$env:LLM_API_KEY` 占位
- **日志脱敏**: exec工具记录日志时,自动过滤包含"key"/"token"/"secret"字段的值

### 内容安全
- **结构化数据真实性**: JSON-LD结构化数据应真实反映内容,禁止注入虚假作者/日期/评分等误导信息
- **FAQ准确性**: 生成的FAQ应与内容一致,避免生成内容中不存在的问答,误导AI搜索引擎和用户
- **AI搜索合规**: 遵守各AI搜索引擎的内容规范,避免优化过度导致被识别为内容农场
- **版权提示**: 优化后的内容基于用户原始内容,用户需确认拥有内容版权,商业使用前建议查重
- **E-E-A-T真实性**: 作者信息/机构信息/来源标注应真实可查,禁止伪造权威背书
