---
slug: seo-doctor
name: seo-doctor
version: "1.1.0"
displayName: "SEO体检医生"
summary: "给网站做全面SEO体检,技术+内容+结构化数据三维度诊断,BERT关键词+排名追踪"
license: Proprietary
description: |-
  SEO体检医生是一款给网站做全面SEO体检的工具。基于BERT语义模型提取关键词,品牌词最高优先级注入,
  技术SEO审计+内容SEO优化+结构化数据三维度诊断,发布前优化与发布后排名追踪闭环.
  核心能力:
  - 技术SEO审计:网站速度/移动适配/索引状态三维度技术诊断
  - 内容SEO优化:BERT语义关键词提取+标题优化+meta标签生成+标签体系搭建
  - 品牌词最高优先级注入:品牌词前置到核心关键词列表,最高权重,大小写不敏感去重
  - 标题A/B测试与排名预估:生成3-5个SEO友好标题版本,基于竞争度预估排名区间
  - 发布后排名追踪:监控搜索排名变化,与历史数据对比生成趋势分析和优化建议
homepage: "https://skillhub.cn"
tags:
  - SEO优化
  - 搜索排名
  - 网站诊断
  - 内容营销
tools:
  - read
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"


---
# SEO体检医生 v1.1.0

给网站做全面SEO体检,基于BERT语义模型提取关键词,品牌词最高优先级注入,发布前优化+发布后排名追踪闭环.
## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 多源数据聚合与去重 | 不支持 | 支持 |
| 语义搜索与智能摘要 | 不支持 | 支持 |
| 定时监控与变化推送 | 不支持 | 支持 |
| 研究结论结构化导出 | 不支持 | 支持 |
| 知识图谱构建与关系推理 | 不支持 | 支持 |

## 核心能力

1. **技术SEO审计**: 网站速度/移动适配/索引状态三维度技术诊断,发现影响收录的技术问题
2. **内容SEO优化**: 关键词密度分析/标题优化/meta标签生成/标签体系搭建,基于BERT语义模型而非简单词频统计
3. **品牌词最高优先级注入**: 读取品牌关键词配置,将品牌词前置到核心关键词列表(最高权重),大小写不敏感去重
4. **标题A/B测试与排名预估**: 生成3-5个SEO友好标题版本,基于关键词竞争度和内容质量预估排名区间
5. **发布后排名追踪**: 监控已发布内容的搜索排名变化,与历史数据对比,生成上升/下降/新入榜/跌出趋势分析和优化建议
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 发布前SEO优化 | title+content+platform+target_keywords | title_options[]+best_title+description+tags+keywords+estimated_rank+seo_score |
| 关键词研究 | content+brand_keywords | primary核心词+secondary次要词+long_tail长尾词+brand_keywords_injected |
| 标题A/B测试 | title+content+competitor_urls | 3-5个标题候选+综合评分+推荐标题 |
| 发布后排名追踪 | mode=track+content_url+target_keywords+history_data | tracking_result(排名/趋势/变化/建议)+summary汇总 |
| 品牌关键词注入 | brand_keywords+content | 品牌词前置注入后的关键词方案+SEO评分提升 |
| 竞品分析 | competitor_urls+target_keywords | 关键词覆盖差距分析+差异化SEO策略 |

**不适用于**: 海外Google/Bing SEO(聚焦国内搜索引擎)、黑帽SEO手法(关键词堆砌/隐藏文本/链接农场)、SEM竞价广告优化、网站技术开发(仅做SEO诊断非代码开发)、APP ASO优化.
## 使用流程

### Step 1: 环境准备
- 确认Agent已加载本SKILL.md,且支持exec工具
- 在Agent环境变量中配置 `LLM_API_KEY`(必需)和 `SEARCH_API_KEY`(可选,用于排名追踪)
- BERT模型为可选,加载失败时降级为正则+词频统计

### Step 2: 选择工作流
- **发布前优化**(工作流1+2): 关键词优化+标题优化
- **发布后追踪**(工作流3): 排名追踪+趋势分析

### Step 3: 关键词优化(工作流1)
1. 读取原始内容(title/content)
2. BERT语义关键词提取(加载失败降级为正则+词频统计)
3. 品牌关键词注入(brand_keywords前置,最高权重,大小写不敏感去重)
4. 热搜关键词匹配(通过热搜API,不可用时跳过)
5. 生成关键词策略(primary核心词+secondary次要词+long_tail长尾词)

### Step 4: 标题优化(工作流2)
1. 基于关键词策略生成3-5个SEO友好标题版本
2. 根据平台规则生成SEO描述和标签
3. 基于关键词竞争度和内容质量预估排名区间
4. 竞品分析(对标competitor_urls,无法访问时跳过)
5. 输出完整SEO方案+SEO评分

### Step 5: 排名追踪(工作流3)
1. 接收已发布内容URL和目标关键词列表
2. 调用搜索API对每个关键词执行搜索查询
3. 检测排名位置,记录排名序号
4. 与历史排名数据对比,计算趋势(上升/下降/新入榜/跌出)
5. 生成优化建议(排名下降→调整关键词密度;未入榜→增加外链;上升→保持策略)

### Step 6: 验证
- V1: 检查关键词API返回非空结果
- V2: 至少3个关键词有搜索量
- V3: 优化后标题无敏感词+长度合规

## 输入格式

### 优化模式(工作流1+2)

```json
{
  "title": "原始标题",
  "content": "正文内容",
  "platform": "xiaohongshu",
  "target_keywords": ["AI代写", "文案生成"],
  "competitor_urls": ["对标链接1", "对标链接2"],
  "brand_keywords": ["品牌词1", "品牌词2"]
}
```

| 字段 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| title | string | 是 | 原始标题 |
| content | string | 是 | 正文内容 |
| platform | string | 是 | 目标平台 |
| target_keywords | string[] | 否 | 目标关键词列表 |
| competitor_urls | string[] | 否 | 竞品内容URL |
| brand_keywords | string[] | 否 | 品牌关键词,优先级最高 |

### 追踪模式(工作流3)

```json
{
  "mode": "track",
  "content_url": "已发布内容的URL",
  "target_keywords": ["AI代写", "文案生成"],
  "platform": "xiaohongshu",
  "history_data": {
    "AI代写": {"last_rank": 5, "date": "2026-05-27"},
    "文案生成": {"last_rank": 12, "date": "2026-05-27"}
  }
}
```

## 输出格式

### 优化模式输出

```json
{
  "success": true,
  "data": {
    "title_options": ["标题A", "标题B", "标题C"],
    "best_title": "推荐标题",
    "description": "SEO描述",
    "tags": ["标签1", "标签2", "标签3"],
    "keywords": {
      "primary": "核心关键词(1-2个)",
      "secondary": ["次要关键词1", "次要关键词2", "次要关键词3(3-5个)"],
      "long_tail": ["长尾关键词1", "长尾关键词2", "长尾关键词3(5-10个)"],
      "brand_keywords_injected": ["实际注入的品牌词1", "品牌词2"]
    },
    "estimated_rank": "预估排名区间",
    "seo_score": 85
  },
  "error": null,
  "code": null
}
```

### 追踪模式输出

```json
{
  "success": true,
  "data": {
    "tracking_result": {
      "content_url": "已发布内容URL",
      "check_date": "2026-05-28",
      "keywords": [
        {
          "keyword": "AI代写",
          "rank": 3,
          "last_rank": 5,
          "trend": "上升",
          "change": 2,
          "suggestion": "排名上升,保持当前策略"
        }
      ],
      "summary": {
        "total_keywords": 3,
        "ranked": 2,
        "improved": 1,
        "declined": 1,
        "not_ranked": 1
      }
    }
  },
  "error": null,
  "code": null
}
```

## SEO评分模型

| 评分维度 | 权重 | 检查项 |
|:---:|:---:|:---:|
| 关键词覆盖 | 25% | 核心词密度/长尾词覆盖/品牌词注入 |
| 标题质量 | 20% | 关键词前置/长度合规/吸引力 |
| 内容质量 | 20% | 原创性/深度/可读性 |
| 标签优化 | 15% | 标签数量/相关性/热门标签覆盖 |
| 结构化数据 | 10% | meta描述/H标签/alt属性 |
| 用户体验 | 10% | 加载速度/移动适配/内链结构 |

## 异常处理

| 异常场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 内容为空 | 未提供content参数 | 返回error="必须提供内容",无法降级 |
| 关键词API超时 | API响应超过10秒 | 使用本地关键词库,从历史关键词数据中读取替代 |
| 标题过长 | 标题超过平台最大长度 | 按平台最大长度截断,保留核心关键词 |
| 标签违规 | 标签含敏感词或违禁词 | 移除违规标签,用同义安全标签替换 |
| 热搜API不可用 | API服务下线或鉴权失败 | 跳过热搜关键词辅助,仅使用BERT语义提取结果 |
| BERT模型加载失败 | 模型文件缺失或加载异常 | 降级为正则+词频统计方式提取关键词 |
| 竞品URL无法访问 | URL失效或反爬限制 | 跳过竞品分析步骤,仅基于自身内容生成SEO方案 |
| 搜索API不可用 | SEARCH_API_KEY未配置或失效 | 返回追踪失败,标注"排名追踪不可用",仅输出优化方案 |
| 搜索结果未找到URL | 内容未收录或排名靠后 | 记录为"未入榜",输出trend="未入榜"+增加权重建议 |
| 历史排名数据缺失 | 首次追踪或history_data为空 | 视为首次追踪,trend="新入榜",不显示change值 |
| 品牌关键词为空 | 未提供brand_keywords | 跳过品牌词注入,使用原始关键词方案 |
| LLM_API_KEY未配置 | 环境变量缺失 | 返回error,提示配置环境变量 |
| 平台不支持 | platform不在支持范围内 | 降级为通用SEO规则,标注warning |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|---:|:---|---:|---:|:---|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | 国内可用: 通义千问/文心一言/智谱GLM/DeepSeek/Kimi |
| BERT模型 | 模型 | 可选 | 语义关键词提取(加载失败降级为正则+词频统计) | 国内替代: 哈工大LTP/百度ERNIE/本地jieba分词+TF-IDF |
| 热搜数据API | API | 可选 | 热搜关键词(不可用时仅用BERT结果) | 国内替代: 微博热搜API/百度热搜/头条热榜 |
| 搜索API | API | 可选 | 排名追踪(不可用时仅输出优化方案) | 国内替代: 百度搜索API/搜狗搜索/360搜索 |

### API Key 配置(零暴露原则)
- **LLM_API_KEY**: 必需(通常由Agent内置) - SEO优化/标题生成/关键词策略
- **SEARCH_API_KEY**: 可选 - 搜索排名追踪
- **配置方式**: 必须通过Agent环境变量注入,严禁在SKILL.md或代码中硬编码API Key
- **安全检查**: 本SKILL.md中不包含任何API Key示例,所有Key均通过 `$env:LLM_API_KEY` 等环境变量读取

### 使用流程(补充)
BERT模型加载失败时降级为正则+词频统计。热搜API不可用时跳过热搜匹配。搜索API不可用时仅输出优化方案不做排名追踪.
只需将SKILL.md文件放入Agent的skills目录即可直接使用.
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力.
### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 小红书内容SEO优化

**输入**:
```json
{
  "title": "AI代写文案服务",
  "content": "正文内容...",
  "platform": "xiaohongshu",
  "target_keywords": ["AI", "代写", "文案"]
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "title_options": [
      "2026年最新AI代写服务|1分钟生成高质量文案",
      "AI代写文案神器|效率提升10倍的写作助手",
      "告别加班!AI代写服务实测,文案1分钟搞定"
    ],
    "best_title": "2026年最新AI代写服务|1分钟生成高质量文案",
    "description": "AI代写文案服务实测推荐,1分钟生成高质量文案,效率提升10倍,告别加班写文案",
    "tags": ["AI代写", "文案生成", "效率工具", "写作助手", "AI工具推荐"],
    "keywords": {
      "primary": "AI代写",
      "secondary": ["文案生成", "AI写作", "效率工具"],
      "long_tail": ["AI代写文案服务推荐", "AI写作工具哪个好", "小红书文案AI生成", "AI代写多少钱", "AI文案生成器免费"],
      "brand_keywords_injected": []
    },
    "estimated_rank": "前3页",
    "seo_score": 92
  },
  "error": null,
  "code": null
}
```

### 示例2: 品牌关键词注入

**输入**:
```json
{
  "title": "AI代写文案服务",
  "content": "正文内容...",
  "platform": "xiaohongshu",
  "target_keywords": ["AI", "代写", "文案"],
  "brand_keywords": ["笔灵AI", "灵犀写作"]
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "title_options": ["笔灵AI代写服务|1分钟生成高质量文案", "灵犀写作AI代写神器|效率提升10倍"],
    "best_title": "笔灵AI代写服务|1分钟生成高质量文案",
    "description": "笔灵AI代写文案服务,灵犀写作加持,1分钟生成高质量文案",
    "tags": ["笔灵AI", "灵犀写作", "AI代写", "文案生成", "效率工具"],
    "keywords": {
      "primary": "笔灵AI",
      "secondary": ["灵犀写作", "AI代写", "文案生成"],
      "long_tail": ["笔灵AI代写服务推荐", "灵犀写作怎么样", "AI代写文案服务"],
      "brand_keywords_injected": ["笔灵AI", "灵犀写作"]
    },
    "estimated_rank": "前2页",
    "seo_score": 95
  },
  "error": null,
  "code": null
}
```

### 示例3: 发布后排名追踪

**输入**:
```json
{
  "mode": "track",
  "content_url": "https://example.com/article/123",
  "target_keywords": ["AI代写", "文案生成", "AI写作工具"],
  "platform": "xiaohongshu",
  "history_data": {
    "AI代写": {"last_rank": 5, "date": "2026-05-27"},
    "文案生成": {"last_rank": 12, "date": "2026-05-27"}
  }
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "tracking_result": {
      "content_url": "https://example.com/article/123",
      "check_date": "2026-05-28",
      "keywords": [
        {"keyword": "AI代写", "rank": 3, "last_rank": 5, "trend": "上升", "change": 2, "suggestion": "排名上升,保持当前策略"},
        {"keyword": "文案生成", "rank": 15, "last_rank": 12, "trend": "下降", "change": -3, "suggestion": "排名下降,建议调整标题关键词密度或增加互动数据"},
        {"keyword": "AI写作工具", "rank": null, "trend": "未入榜", "change": null, "suggestion": "未进入搜索结果,建议增加外链和平台互动提升权重"}
      ],
      "summary": {"total_keywords": 3, "ranked": 2, "improved": 1, "declined": 1, "not_ranked": 1}
    }
  },
  "error": null,
  "code": null
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成.
### 案例1: 发布前SEO优化(小红书,品牌词注入+排名预估)

**输入**:
```json
{
  "title": "AI写作工具推荐",
  "content": "现在AI写作工具越来越多了,选哪个好?今天给大家推荐几款实用的AI写作工具,包括文案生成、论文润色、营销文案等场景...",
  "platform": "xiaohongshu",
  "target_keywords": ["AI写作工具", "文案生成"],
  "brand_keywords": ["笔灵AI", "笔灵写作"]
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "title_options": [
      "笔灵AI写作工具推荐:5款文案生成神器测评(附教程)",
      "2026最新AI写作工具排名:笔灵AI领衔,文案生成效率提升10倍",
      "AI写作工具怎么选?笔灵AI等5款文案生成神器对比评测"
    ],
    "best_title": "笔灵AI写作工具推荐:5款文案生成神器测评(附教程)",
    "description": "AI写作工具怎么选?本文测评笔灵AI等5款主流文案生成工具,从功能、价格、效果多维度对比,附使用教程和效率提升技巧。",
    "tags": ["AI写作工具", "文案生成", "笔灵AI", "写作效率", "工具推荐", "AI助手", "内容创作", "笔灵写作"],
    "keywords": {
      "primary": "笔灵AI",
      "secondary": ["AI写作工具", "文案生成", "笔灵写作", "写作效率"],
      "long_tail": ["AI写作工具哪个好", "文案生成工具推荐", "笔灵AI怎么用", "AI写作工具免费", "AI文案生成器", "笔灵AI测评", "AI写作助手", "自动化文案工具"],
      "brand_keywords_injected": ["笔灵AI", "笔灵写作"]
    },
    "estimated_rank": "前3(关键词竞争度中等,品牌词加持)",
    "seo_score": 87
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓品牌词笔灵AI前置注入(最高权重primary) ✓3个标题候选+1个推荐 ✓8个标签(含品牌词) ✓8个长尾词挖掘 ✓SEO评分87分(优良)

### 案例2: 关键词研究(BERT语义提取+三级分类)

**输入**:
```json
{
  "title": "Python入门教程",
  "content": "Python是一门简单易学的编程语言,适合零基础入门。本教程涵盖Python基础语法、数据类型、流程控制、函数、面向对象等内容...",
  "platform": "zhihu",
  "brand_keywords": ["编程猫"]
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "title_options": [
      "编程猫Python入门教程:零基础到精通完整指南2026",
      "Python入门教程|编程猫带你零基础学Python(附代码)",
      "2026 Python入门教程:编程猫整理的零基础学习路线图"
    ],
    "best_title": "编程猫Python入门教程:零基础到精通完整指南2026",
    "description": "Python入门教程零基础也能学!编程猫整理Python基础语法、数据类型、函数、面向对象等核心知识,附完整代码示例。",
    "tags": ["Python入门", "编程猫", "Python教程", "零基础学编程", "Python基础", "编程入门", "Python语法"],
    "keywords": {
      "primary": "编程猫",
      "secondary": ["Python入门", "Python教程", "Python基础", "零基础学编程"],
      "long_tail": ["Python入门教程", "零基础学Python", "Python基础语法", "Python数据类型", "Python函数", "Python面向对象", "编程猫Python", "Python学习路线"],
      "brand_keywords_injected": ["编程猫"]
    },
    "estimated_rank": "前5(关键词竞争度高,品牌词加持)",
    "seo_score": 82
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓BERT语义关键词提取(非简单词频) ✓品牌词编程猫前置注入 ✓三级关键词分类(primary/secondary/long_tail) ✓8个长尾词覆盖 ✓SEO评分82分(良好)

### 案例3: 发布后排名追踪(趋势分析+优化建议)

**输入**:
```json
{
  "mode": "track",
  "content_url": "https://zhuanlan.zhihu.com/p/123456",
  "target_keywords": ["AI写作工具", "文案生成", "AI文案助手"],
  "platform": "zhihu",
  "history_data": {
    "AI写作工具": {"last_rank": 5, "date": "2026-07-13"},
    "文案生成": {"last_rank": 12, "date": "2026-07-13"},
    "AI文案助手": {"last_rank": null, "date": "2026-07-13"}
  }
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "tracking_result": {
      "content_url": "https://zhuanlan.zhihu.com/p/123456",
      "check_date": "2026-07-20",
      "keywords": [
        {"keyword": "AI写作工具", "rank": 3, "last_rank": 5, "trend": "上升", "change": 2, "suggestion": "排名上升2位,保持当前内容策略,可考虑增加外链巩固排名"},
        {"keyword": "文案生成", "rank": 15, "last_rank": 12, "trend": "下降", "change": -3, "suggestion": "排名下降3位,建议优化该关键词密度,增加相关长尾词覆盖"},
        {"keyword": "AI文案助手", "rank": 8, "last_rank": null, "trend": "新入榜", "change": null, "suggestion": "新入榜第8位,表现良好,建议增加该关键词在标题中的权重"}
      ],
      "summary": {
        "total_keywords": 3,
        "ranked": 3,
        "improved": 1,
        "declined": 1,
        "not_ranked": 0
      }
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓3个关键词排名全部追踪 ✓趋势分析正确(上升/下降/新入榜) ✓变化幅度计算准确(+2/-3) ✓优化建议针对性(每个关键词独立建议) ✓汇总统计完整(3全上榜,1升1降,not_ranked=0)

### 案例4: BERT模型降级(正则+词频统计提取关键词)

**输入**:
```json
{
  "title": "健身减脂饮食指南",
  "content": "减脂期间饮食很重要,要控制热量摄入,多吃蛋白质,少吃碳水。推荐鸡胸肉、西兰花、鸡蛋等减脂食物...",
  "platform": "xiaohongshu"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "title_options": [
      "健身减脂饮食指南:高蛋白低碳水食谱一周安排",
      "减脂饮食怎么吃?健身减脂食物清单+热量控制指南",
      "2026健身减脂饮食攻略:鸡胸肉西兰花等减脂食物推荐"
    ],
    "best_title": "健身减脂饮食指南:高蛋白低碳水食谱一周安排",
    "description": "减脂饮食怎么吃?健身减脂饮食指南推荐鸡胸肉、西兰花、鸡蛋等高蛋白低碳水食物,附热量控制方法和一周食谱安排。",
    "tags": ["健身减脂", "减脂饮食", "高蛋白", "低碳水", "鸡胸肉", "减脂食物", "热量控制"],
    "keywords": {
      "primary": "减脂饮食",
      "secondary": ["健身减脂", "高蛋白", "低碳水", "热量控制"],
      "long_tail": ["减脂饮食指南", "减脂食物推荐", "鸡胸肉减脂", "高蛋白低碳水饮食", "减脂热量控制", "西兰花减脂", "减脂食谱一周安排"],
      "brand_keywords_injected": []
    },
    "estimated_rank": "前10(关键词竞争度中高)",
    "seo_score": 78
  },
  "error": "BERT模型加载失败,已降级为正则+词频统计方式提取关键词,语义准确度可能略有降低",
  "code": "BERT_FALLBACK"
}
```

**效果验证**: ✓BERT模型降级为正则+词频统计 ✓降级原因在error字段标注 ✓错误码BERT_FALLBACK正确返回 ✓关键词提取质量基本达标(7个长尾词) ✓SEO评分78分(合格)

### 案例5: 标题A/B测试(3个候选+竞品对标)

**输入**:
```json
{
  "title": "副业赚钱方法",
  "content": "2026年副业赚钱方法有很多,包括自媒体、电商、知识付费等。本文分享5个亲测有效的副业项目...",
  "platform": "toutiao",
  "target_keywords": ["副业赚钱", "副业项目"],
  "competitor_urls": ["https://toutiao.com/article/111", "https://toutiao.com/article/222"]
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "title_options": [
      {"title": "2026副业赚钱指南:5个亲测有效的副业项目(月入过万)", "score": 92, "reason": "年份+数字+利益承诺+括号补充,头条点击率高"},
      {"title": "副业赚钱方法大全:从0到月入过万的5个项目实操", "score": 88, "reason": "从0到月入过万制造落差,5个项目实操增加可信度"},
      {"title": "我靠这5个副业项目月入过万(附详细操作步骤)", "score": 90, "reason": "第一人称增强真实感,附操作步骤提升点击意愿"}
    ],
    "best_title": "2026副业赚钱指南:5个亲测有效的副业项目(月入过万)",
    "description": "2026副业赚钱方法分享:5个亲测有效的副业项目,包括自媒体、电商、知识付费等,附详细操作步骤,助你月入过万。",
    "tags": ["副业赚钱", "副业项目", "月入过万", "自媒体", "电商", "知识付费", "兼职"],
    "keywords": {
      "primary": "副业赚钱",
      "secondary": ["副业项目", "月入过万", "自媒体", "电商"],
      "long_tail": ["副业赚钱方法", "副业项目推荐", "月入过万副业", "副业赚钱指南", "在家做的副业", "副业自媒体", "副业电商", "知识付费副业"],
      "brand_keywords_injected": []
    },
    "estimated_rank": "前5(关键词竞争度中等,标题质量高)",
    "seo_score": 85,
    "competitor_analysis": {
      "analyzed": 2,
      "keyword_gaps": ["竞品覆盖了'手机副业'但本文未涉及", "竞品有实操截图但本文无"],
      "differentiation": "本文优势:亲测有效+5个项目;建议补充:手机端副业+实操截图"
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓3个标题候选+评分+推荐理由 ✓竞品分析2个URL(关键词差距+差异化建议) ✓头条平台标题适配(数字+利益承诺) ✓8个长尾词 ✓SEO评分85分(优良)

## 常见问题

### Q1: 如何开始使用SEO体检医生?
A: 三步启动:(1)将SKILL.md放入Agent的skills目录;(2)确认Agent环境变量已配置LLM_API_KEY;(3)发布前优化传入title+content+platform,发布后追踪传入mode=track+content_url+target_keywords。BERT模型和搜索API为可选,不可用时自动降级.
### Q2: BERT模型加载失败会有什么影响?
A: BERT模型用于语义关键词提取,加载失败时降级为正则+词频统计方式。降级后关键词提取精度略降(可能漏掉语义相关但词形不同的关键词),但基础功能不受影响。建议关键内容人工复核关键词方案.
### Q3: 品牌关键词注入的逻辑是什么?
A: 读取brand_keywords配置,将品牌词前置到核心关键词列表(最高权重),执行大小写不敏感去重。注入后品牌词会出现在:标题(title_options)、标签(tags)、关键词(primary/secondary)、SEO描述(description)中,提升品牌曝光和搜索权重。SEO评分会因品牌词注入而提升.
### Q4: 排名追踪需要什么前提?
A: 需要配置SEARCH_API_KEY环境变量,且内容已发布并收录。追踪时传入content_url和target_keywords,系统调用搜索API查询每个关键词的搜索结果,检测content_url的排名位置。首次追踪无需history_data,系统会标记为"新入榜".
### Q5: SEO评分模型6维度如何计算?
A: 关键词覆盖25%+标题质量20%+内容质量20%+标签优化15%+结构化数据10%+用户体验10%,加权计算总分(0-100)。评分≥85为优秀,70-84为良好,60-69为合格,<60为待优化。品牌词注入可提升关键词覆盖维度分数.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **搜索引擎覆盖**: 排名追踪依赖搜索API,主要支持国内搜索引擎(百度/搜狗/360),Google/Bing等海外搜索引擎追踪需额外配置
- **BERT模型精度**: BERT语义提取依赖预训练模型,对特定行业/垂直领域的关键词可能理解不够精准,需人工补充行业词库
- **热搜时效性**: 热搜数据具有强时效性,API返回的热搜可能与实际搜索热度有延迟
- **竞品分析限制**: 竞品URL如设置反爬或需登录访问,系统会跳过该竞品分析
- **排名追踪频率**: 频繁调用搜索API可能触发反爬限制,建议每日追踪不超过1次
- **平台规则差异**: 各平台(小红书/抖音/公众号等)的SEO规则不同,部分平台不开放搜索API导致无法追踪排名
- **内容原创性检测**: SEO评分中的原创性维度基于LLM判断,非专业查重工具,商业场景建议配合查重服务

## 安全

### API Key 零暴露原则
- **环境变量注入**: 所有API Key(LLM_API_KEY/SEARCH_API_KEY)必须通过Agent环境变量注入,严禁在SKILL.md、配置文件或代码中硬编码
- **本文件无Key示例**: 本SKILL.md中不包含任何真实或示例API Key,所有引用均使用 `$env:LLM_API_KEY` 占位
- **日志脱敏**: exec工具记录日志时,自动过滤包含"key"/"token"/"secret"字段的值
- **搜索API隔离**: SEARCH_API_KEY仅用于排名追踪,不与LLM_API_KEY混用,避免单Key泄露影响多服务

### 内容安全
- **白帽SEO**: 仅使用白帽SEO手法(关键词优化/结构化数据/内容质量),不使用黑帽手法(关键词堆砌/隐藏文本/链接农场)
- **平台合规**: 适配各平台内容规范,避免过度优化导致平台降权
- **竞品数据**: 竞品分析仅用于学习参考,不抓取竞品非公开数据,遵守robots.txt协议
- **数据隐私**: 排名追踪不收集用户搜索行为数据,仅查询公开搜索结果中的排名位置
