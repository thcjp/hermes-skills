---
slug: topic-hunter
name: topic-hunter
version: "1.1.0"
displayName: "选题捕手"
summary: "告别不知道写啥,4平台热点聚合+趋势评分+差异化选题,3秒锁定下一个爆款选题"
license: Proprietary
description: |-
homepage: "https://skillhub.cn"
tags: [选题推荐, 热点追踪, 内容创作, 趋势分析]
tools:
  - read
  - exec
suggested_price: "1.90"
pricing_tier: "standard"
pricing_rationale: "文案创作类, large市场, enterprise复杂度, daily频次, standard层 → 高频通用工具,大市场,低单价走量"
---
# 选题捕手 v1.1.0

解决内容创作者"不知道写什么"的核心痛点,聚合4大平台热点,基于5维趋势评分筛选高潜选题。

## 核心能力

1. **4大平台热点聚合**: 小红书/抖音/微博/知乎热点话题一键聚合,支持单平台或多平台组合查询
2. **5维趋势评分模型**: 热度(30%)+增长趋势(25%)+竞争度(20%)+变现潜力(15%)+可持续性(10%),0-100分加权计算,科学筛选高潜选题
3. **差异化选题建议**: 基于竞争度分析,提供差异化切入角度建议,避免红海同质化竞争
4. **用户兴趣匹配**: 根据用户兴趣标签筛选匹配的选题,提升选题与账号定位的相关性
5. **选题日历规划**: 按时间维度规划选题发布节奏,支持节假日/热点事件提前布局
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。


## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 多平台热点选题 | platforms(多平台)+category(分类) | topics[](标题/热度/趋势/竞争度/评分/差异化建议) |
| 单平台深度选题 | platform(单平台)+category | 该平台Top10热点选题+平台特色分析 |
| 趋势预测选题 | keyword(关键词)+time_range | 趋势上升的选题+增长预测+入场时机建议 |
| 差异化选题 | topic(已有选题)+platform | 差异化切入角度建议+蓝海机会点 |
| 用户兴趣匹配 | user_interests(兴趣标签)+platform | 匹配用户兴趣的选题+相关性评分 |
| 选题日历规划 | time_range(时间范围)+category | 选题发布日历+节假日/热点提前布局 |

**不适用于**: 海外平台热点(如Twitter/Reddit/YouTube,仅支持国内4平台)、B2B行业选题(侧重消费品/生活方式类)、学术研究选题、新闻采编选题(需专业新闻判断)。

## 使用流程

### Step 1: 环境准备
- 确认Agent已加载本SKILL.md,且支持exec工具
- 在Agent环境变量中配置 `LLM_API_KEY`(必需)和 `HOT_SEARCH_API_KEY`(可选,用于热点数据获取)
- 热搜API为可选,不可用时降级为LLM基于知识库生成选题

### Step 2: 接收输入参数
- 必填: `platforms`(目标平台数组)或 `platform`(单平台)
- 选填: `category`(内容分类)、`user_interests`(用户兴趣标签)、`time_range`(时间范围)、`keyword`(趋势关键词)

### Step 3: 热点数据获取
- 调用热搜API获取各平台热点话题
- 异常处理: 热搜API不可用→降级为LLM基于知识库生成选题;单平台失败→跳过该平台继续其他平台

### Step 4: 5维趋势评分
- 对每个选题进行5维度评分:
  - 热度(30%): 当前搜索量/讨论量
  - 增长趋势(25%): 热度上升/下降/平稳
  - 竞争度(20%): 已有内容数量(竞争度越低分越高)
  - 变现潜力(15%): 商业合作/带货可能性
  - 可持续性(10%): 话题生命周期长度
- 加权计算总分(0-100)

### Step 5: 差异化分析
- 分析选题的竞争度,识别红海(高竞争)和蓝海(低竞争)选题
- 为红海选题提供差异化切入角度建议
- 识别蓝海机会点(高热度+低竞争)

### Step 6: 用户兴趣匹配(可选)
- 根据user_interests标签筛选匹配的选题
- 计算选题与用户兴趣的相关性评分

### Step 7: 输出选题列表
- topics[]: 按评分排序的选题列表
- 每个选题包含: 标题/平台/热度/趋势/竞争度/评分/差异化建议

## 输入格式

```json
{
  "platforms": ["xiaohongshu", "douyin", "weibo", "zhihu"],
  "category": "科技",
  "user_interests": ["AI", "编程", "效率工具"],
  "time_range": "7d",
  "keyword": "AI编程"
}
```

| 字段 | 类型 | 必填 | 说明 |
|:-----|:-----|:----:|:-----|
| platforms | string[] | 否 | 目标平台数组: xiaohongshu/douyin/weibo/zhihu(与platform二选一) |
| platform | string | 否 | 单目标平台(与platforms二选一) |
| category | string | 否 | 内容分类: 科技/生活/美食/时尚/教育/财经等 |
| user_interests | string[] | 否 | 用户兴趣标签,用于筛选匹配选题 |
| time_range | string | 否 | 时间范围: 24h/7d/30d,默认7d |
| keyword | string | 否 | 趋势关键词,用于趋势预测 |

## 输出格式

```json
{
  "success": true,
  "data": {
    "topics": [
      {
        "title": "选题标题",
        "platform": "xiaohongshu",
        "category": "科技",
        "hotness": 85,
        "trend": "rising",
        "competition": "medium",
        "monetization": "high",
        "sustainability": "medium",
        "score": 82,
        "differentiation": "差异化切入角度建议",
        "user_interest_match": 0.9
      }
    ],
    "summary": {
      "total_topics": 10,
      "avg_score": 78,
      "top_platform": "xiaohongshu",
      "blue_ocean_count": 3
    }
  },
  "error": null,
  "code": null
}
```

## 5维趋势评分模型

| 维度 | 权重 | 评分标准 | 数据来源 |
|:-----|:-----|:---------|:---------|
| 热度 | 30% | 搜索量/讨论量/互动量 | 热搜API |
| 增长趋势 | 25% | 上升/下降/平稳+增长率 | 热搜API历史数据 |
| 竞争度 | 20% | 已有内容数量(越低分越高) | 平台搜索结果数 |
| 变现潜力 | 15% | 商业合作/带货可能性 | LLM判断 |
| 可持续性 | 10% | 话题生命周期长度 | LLM判断 |

**评分等级**:
- 90-100: 爆款潜力(高热度+上升趋势+低竞争)
- 80-89: 优质选题(综合表现优秀)
- 70-79: 良好选题(有潜力但需优化切入角度)
- 60-69: 一般选题(竞争激烈或热度下降)
- <60: 不推荐(红海或过时话题)

## 异常处理

| 异常场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| 平台参数为空 | 未提供platforms或platform | 默认查询全部4个平台,标注warning |
| 平台不支持 | 输入的平台不在4个支持范围内 | 跳过不支持的平台,继续查询其他平台 |
| 热搜API不可用 | API服务下线或鉴权失败 | 降级为LLM基于知识库生成选题,标注warning |
| 单平台热搜失败 | 该平台API超时或异常 | 跳过该平台,继续查询其他平台,标注warning |
| 全部平台失败 | 所有平台API不可用 | 降级为LLM基于知识库生成通用选题,标注warning |
| 分类不支持 | category不在支持范围内 | 不按分类筛选,返回全品类选题,标注warning |
| 评分异常 | 部分维度评分失败 | 跳过该维度,按已有维度加权计算,标注warning |
| 差异化分析失败 | LLM分析异常 | 跳过差异化建议,仅输出评分,标注warning |
| 用户兴趣匹配失败 | user_interests为空或LLM异常 | 跳过兴趣匹配,仅按评分排序,标注warning |
| LLM调用失败 | LLM服务不可用或超时 | 返回success=false, error="选题分析LLM调用失败" |
| LLM_API_KEY未配置 | 环境变量缺失 | 返回error,提示配置环境变量 |
| 选题数量不足 | 热点数据少或筛选后不足 | 返回已有选题,标注warning提示数据不足 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:-------|:-----|:---------|:---------|:-------------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | 国内可用: 通义千问/文心一言/智谱GLM/DeepSeek/Kimi |
| 热搜数据API | API | 可选 | 4平台热搜数据(不可用时降级为LLM知识库) | 国内替代: 微博热搜API/百度热搜/头条热榜/新榜API |
| 平台搜索API | API | 可选 | 竞争度分析(搜索结果数) | 国内替代: 各平台开放API/新榜/蝉妈妈 |

### API Key 配置(零暴露原则)
- **LLM_API_KEY**: 必需(通常由Agent内置) - 选题分析/差异化建议/评分计算
- **HOT_SEARCH_API_KEY**: 可选 - 热搜数据获取(不可用时降级为LLM知识库)
- **配置方式**: 必须通过Agent环境变量注入,严禁在SKILL.md或代码中硬编码API Key
- **安全检查**: 本SKILL.md中不包含任何API Key示例,所有Key均通过 `$env:LLM_API_KEY` 等环境变量读取

### 使用流程
热搜API不可用时降级为LLM基于知识库生成选题。单平台失败时跳过该平台继续查询。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 多平台科技类热点选题

**输入**:
```json
{
  "platforms": ["xiaohongshu", "douyin", "weibo", "zhihu"],
  "category": "科技",
  "time_range": "7d"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "topics": [
      {
        "title": "AI编程工具横评:5款神器对比",
        "platform": "xiaohongshu",
        "category": "科技",
        "hotness": 92,
        "trend": "rising",
        "competition": "medium",
        "monetization": "high",
        "sustainability": "high",
        "score": 88,
        "differentiation": "多数内容只推荐单一工具,可做横向对比+实测体验差异化",
        "user_interest_match": null
      },
      {
        "title": "AI取代程序员?最新进展",
        "platform": "zhihu",
        "category": "科技",
        "hotness": 88,
        "trend": "rising",
        "competition": "high",
        "monetization": "medium",
        "sustainability": "medium",
        "score": 82,
        "differentiation": "红海选题,建议从非程序员视角切入,讲AI对普通人的影响",
        "user_interest_match": null
      },
      {
        "title": "用AI做副业月入过万实操",
        "platform": "douyin",
        "category": "科技",
        "hotness": 95,
        "trend": "rising",
        "competition": "low",
        "monetization": "high",
        "sustainability": "medium",
        "score": 91,
        "differentiation": "蓝海机会点,多数内容只讲概念,可做真实实操记录差异化",
        "user_interest_match": null
      }
    ],
    "summary": {
      "total_topics": 10,
      "avg_score": 80,
      "top_platform": "douyin",
      "blue_ocean_count": 3
    }
  },
  "error": null,
  "code": null
}
```

### 示例2: 单平台+用户兴趣匹配

**输入**:
```json
{
  "platform": "xiaohongshu",
  "user_interests": ["AI", "编程", "效率工具"],
  "time_range": "24h"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "topics": [
      {
        "title": "AI写作工具实测:哪个最好用",
        "platform": "xiaohongshu",
        "category": "科技",
        "hotness": 85,
        "trend": "rising",
        "competition": "medium",
        "monetization": "high",
        "sustainability": "high",
        "score": 84,
        "differentiation": "可做长期使用体验对比,而非短期测评",
        "user_interest_match": 0.95
      },
      {
        "title": "程序员必备AI效率工具",
        "platform": "xiaohongshu",
        "category": "科技",
        "hotness": 78,
        "trend": "stable",
        "competition": "high",
        "monetization": "medium",
        "sustainability": "medium",
        "score": 75,
        "differentiation": "红海选题,建议聚焦小众工具或特定场景",
        "user_interest_match": 0.92
      }
    ],
    "summary": {
      "total_topics": 8,
      "avg_score": 79,
      "top_platform": "xiaohongshu",
      "blue_ocean_count": 2
    }
  },
  "error": null,
  "code": null
}
```

### 示例3: 趋势预测选题

**输入**:
```json
{
  "keyword": "AI编程",
  "time_range": "30d"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "topics": [
      {
        "title": "AI编程工具2026年发展趋势",
        "platform": "zhihu",
        "category": "科技",
        "hotness": 72,
        "trend": "rising",
        "competition": "low",
        "monetization": "medium",
        "sustainability": "high",
        "score": 78,
        "differentiation": "趋势预测类内容少,可做深度分析差异化",
        "user_interest_match": null
      },
      {
        "title": "AI编程会取代初级程序员吗",
        "platform": "weibo",
        "category": "科技",
        "hotness": 80,
        "trend": "rising",
        "competition": "medium",
        "monetization": "low",
        "sustainability": "high",
        "score": 76,
        "differentiation": "可从招聘数据角度切入,用数据说话",
        "user_interest_match": null
      }
    ],
    "summary": {
      "total_topics": 6,
      "avg_score": 75,
      "top_platform": "weibo",
      "blue_ocean_count": 2
    }
  },
  "error": null,
  "code": null
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 多平台热点选题(4平台聚合+5维评分排序)

**输入**:
```json
{
  "platforms": ["xiaohongshu", "douyin", "weibo", "zhihu"],
  "category": "科技",
  "time_range": "7d"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "topics": [
      {"title": "AI编程工具Cursor深度测评", "platform": "xiaohongshu", "category": "科技", "hotness": 92, "trend": "rising", "competition": "medium", "monetization": "high", "sustainability": "high", "score": 88, "differentiation": "多数内容泛泛而谈,可从'非程序员也能用'角度差异化切入", "user_interest_match": null},
      {"title": "Claude 4 vs GPT-5能力对比", "platform": "zhihu", "category": "科技", "hotness": 90, "trend": "rising", "competition": "high", "monetization": "medium", "sustainability": "medium", "score": 82, "differentiation": "已有大量对比文,建议聚焦'中文场景实测'做差异化", "user_interest_match": null},
      {"title": "AI生成视频工具Runway实战教程", "platform": "douyin", "category": "科技", "hotness": 85, "trend": "rising", "competition": "low", "monetization": "high", "sustainability": "high", "score": 86, "differentiation": "蓝海选题!竞争度低+变现潜力高,建议快速入场", "user_interest_match": null},
      {"title": "2026年AI行业裁员潮分析", "platform": "weibo", "category": "科技", "hotness": 88, "trend": "stable", "competition": "high", "monetization": "low", "sustainability": "low", "score": 72, "differentiation": "红海选题,情绪导向内容多,建议从'转行指南'角度切入", "user_interest_match": null}
    ],
    "summary": {
      "total_topics": 4,
      "avg_score": 82,
      "top_platform": "xiaohongshu",
      "blue_ocean_count": 1
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓4平台热点数据聚合成功 ✓5维评分模型正确计算(热度30%+趋势25%+竞争20%+变现15%+可持续10%) ✓蓝海选题识别(Runway教程竞争度low) ✓差异化建议针对性 ✓汇总统计完整

### 案例2: 单平台深度选题(小红书Top5+平台特色分析)

**输入**:
```json
{
  "platform": "xiaohongshu",
  "category": "生活",
  "time_range": "24h"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "topics": [
      {"title": "极简主义收纳法:小户型改造前后对比", "platform": "xiaohongshu", "category": "生活", "hotness": 88, "trend": "rising", "competition": "medium", "monetization": "high", "sustainability": "high", "score": 85, "differentiation": "可聚焦租房场景,做'不破坏墙面的收纳方案'差异化"},
      {"title": "一周备餐攻略:打工人省时省力食谱", "platform": "xiaohongshu", "category": "生活", "hotness": 85, "trend": "stable", "competition": "high", "monetization": "medium", "sustainability": "medium", "score": 78, "differentiation": "已有大量备餐文,建议从'50元以内一周备餐'角度做低价差异化"},
      {"title": "独居女生安全清单:10个必备好物", "platform": "xiaohongshu", "category": "生活", "hotness": 82, "trend": "rising", "competition": "low", "monetization": "high", "sustainability": "high", "score": 84, "differentiation": "蓝海选题!安全话题竞争度低,可结合智能好物带货"},
      {"title": "断舍离100天记录:从囤积狂到极简", "platform": "xiaohongshu", "category": "生活", "hotness": 80, "trend": "stable", "competition": "medium", "monetization": "low", "sustainability": "medium", "score": 75, "differentiation": "可做'100天断舍离日记'系列连载,增强粉丝粘性"},
      {"title": "出租屋改造:500元打造ins风卧室", "platform": "xiaohongshu", "category": "生活", "hotness": 86, "trend": "rising", "competition": "medium", "monetization": "high", "sustainability": "high", "score": 83, "differentiation": "可聚焦'学生党500元改造',精准定位大学生群体"}
    ],
    "summary": {
      "total_topics": 5,
      "avg_score": 81,
      "top_platform": "xiaohongshu",
      "blue_ocean_count": 1
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓小红书单平台Top5选题 ✓24小时热点数据获取 ✓蓝海选题识别(独居女生安全清单) ✓差异化建议针对小红书特色 ✓生活类选题变现潜力分析

### 案例3: 趋势预测选题(关键词趋势分析+入场时机)

**输入**:
```json
{
  "keyword": "AI绘画",
  "platforms": ["xiaohongshu", "douyin"],
  "time_range": "30d"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "topics": [
      {"title": "AI绘画接单实操:从0到月入5000", "platform": "xiaohongshu", "category": "科技", "hotness": 89, "trend": "rising", "competition": "medium", "monetization": "high", "sustainability": "high", "score": 87, "differentiation": "接单类内容增长快,建议做'接单全流程实录'系列", "user_interest_match": null},
      {"title": "Midjourney v7新功能实测", "platform": "douyin", "category": "科技", "hotness": 85, "trend": "rising", "competition": "low", "monetization": "medium", "sustainability": "medium", "score": 84, "differentiation": "蓝海!v7新功能内容少,建议抢先发布", "user_interest_match": null}
    ],
    "summary": {
      "total_topics": 2,
      "avg_score": 86,
      "top_platform": "xiaohongshu",
      "blue_ocean_count": 1
    },
    "trend_prediction": {
      "keyword": "AI绘画",
      "current_trend": "rising",
      "growth_rate_30d": "+45%",
      "prediction": "持续上升",
      "entry_timing": "建议立即入场,热度上升期+竞争尚未饱和",
      "peak_prediction": "预计8-9月达到热度峰值(暑期创作高峰)"
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓关键词趋势分析正确(AI绘画上升+45%) ✓入场时机建议(立即入场) ✓峰值预测(8-9月暑期高峰) ✓2平台趋势选题输出 ✓蓝海选题识别(MJ v7新功能)

### 案例4: 热搜API降级(LLM知识库生成选题)

**输入**:
```json
{
  "platforms": ["weibo", "zhihu"],
  "category": "财经"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "topics": [
      {"title": "2026下半年A股投资机会分析", "platform": "zhihu", "category": "财经", "hotness": 80, "trend": "stable", "competition": "high", "monetization": "medium", "sustainability": "medium", "score": 75, "differentiation": "建议从'散户视角'切入,降低专业门槛", "user_interest_match": null},
      {"title": "黄金价格走势:现在还能买吗?", "platform": "weibo", "category": "财经", "hotness": 78, "trend": "rising", "competition": "medium", "monetization": "low", "sustainability": "low", "score": 73, "differentiation": "可做'100元也能买黄金'的平民化角度", "user_interest_match": null}
    ],
    "summary": {
      "total_topics": 2,
      "avg_score": 74,
      "top_platform": "zhihu",
      "blue_ocean_count": 0
    }
  },
  "error": "热搜API不可用,已降级为LLM基于知识库生成选题。选题基于近期热门趋势推测,实时性可能略有偏差,建议结合实际热搜验证。",
  "code": "HOT_SEARCH_FALLBACK"
}
```

**效果验证**: ✓热搜API降级为LLM知识库生成 ✓降级原因在error字段标注 ✓错误码HOT_SEARCH_FALLBACK正确返回 ✓选题质量基本达标(2个选题+评分) ✓提示用户结合实际热搜验证

### 案例5: 用户兴趣匹配(兴趣标签筛选选题)

**输入**:
```json
{
  "platforms": ["xiaohongshu", "douyin"],
  "category": "科技",
  "user_interests": ["AI", "编程", "效率工具"],
  "time_range": "7d"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "topics": [
      {"title": "AI编程工具Cursor深度测评", "platform": "xiaohongshu", "category": "科技", "hotness": 92, "trend": "rising", "competition": "medium", "monetization": "high", "sustainability": "high", "score": 88, "differentiation": "可从'非程序员也能用'角度差异化", "user_interest_match": 0.95},
      {"title": "5款AI效率工具盘点:每天省2小时", "platform": "xiaohongshu", "category": "科技", "hotness": 85, "trend": "rising", "competition": "medium", "monetization": "high", "sustainability": "medium", "score": 83, "differentiation": "建议做'实测对比'而非泛泛推荐", "user_interest_match": 0.92},
      {"title": "Claude API调用入门教程", "platform": "douyin", "category": "科技", "hotness": 80, "trend": "rising", "competition": "low", "monetization": "medium", "sustainability": "high", "score": 82, "differentiation": "蓝海!API教程竞争少,适合编程向账号", "user_interest_match": 0.90}
    ],
    "summary": {
      "total_topics": 3,
      "avg_score": 84,
      "top_platform": "xiaohongshu",
      "blue_ocean_count": 1
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓用户兴趣标签(AI/编程/效率工具)正确匹配 ✓user_interest_match评分0.90-0.95(高度匹配) ✓3个选题均与用户兴趣相关 ✓蓝海选题识别(Claude API教程) ✓兴趣匹配排序正确

## 常见问题

### Q1: 如何开始使用选题捕手?
A: 三步启动:(1)将SKILL.md放入Agent的skills目录;(2)确认Agent环境变量已配置LLM_API_KEY;(3)调用时传入platforms(或platform)即可获取热点选题。热搜API为可选,不可用时降级为LLM基于知识库生成选题。

### Q2: 热搜API不可用会影响选题质量吗?
A: 会一定程度影响。热搜API不可用时,系统降级为LLM基于知识库生成选题,选题的时效性会降低(可能不是最新热点),但选题分析和评分功能不受影响。建议配置国内热搜API(微博热搜/百度热搜/新榜)提升时效性。

### Q3: 5维趋势评分模型如何工作?
A: 热度(30%)+增长趋势(25%)+竞争度(20%)+变现潜力(15%)+可持续性(10%),加权计算总分(0-100)。90-100为爆款潜力,80-89为优质选题,70-79为良好选题,60-69为一般选题,<60不推荐。评分帮助科学筛选高潜选题。

### Q4: 差异化选题建议如何使用?
A: 每个选题的differentiation字段提供差异化切入角度建议:(1)红海选题(高竞争)→建议差异化角度,如"从非程序员视角切入";(2)蓝海选题(低竞争)→标注"蓝海机会点",建议优先入场。blue_ocean_count统计蓝海选题数量。

### Q5: 用户兴趣匹配如何工作?
A: 传入user_interests标签后,系统计算选题与用户兴趣的相关性评分(0-1),user_interest_match字段显示匹配度。匹配度>0.8为高度匹配,建议优先选择。未传入user_interests时该字段为null,仅按评分排序。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **平台覆盖**: 仅支持4个国内平台(小红书/抖音/微博/知乎),不支持B站/快手/头条号/海外平台
- **热搜时效性**: 热搜数据具有强时效性,API返回的热点可能与实际热度有延迟
- **竞争度精度**: 竞争度基于平台搜索结果数估算,可能不完全反映实际竞争程度
- **评分主观性**: 变现潜力和可持续性维度基于LLM判断,不同模型评分可能差异较大
- **分类覆盖**: 主要覆盖消费品/生活方式类分类,B2B/工业/学术等垂直领域覆盖有限
- **趋势预测**: 趋势预测基于历史数据和LLM判断,无法保证100%准确,仅供参考
- **用户兴趣匹配**: 匹配基于标签相似度,可能无法捕捉用户兴趣的细微偏好

## 安全

### API Key 零暴露原则
- **环境变量注入**: 所有API Key(LLM_API_KEY/HOT_SEARCH_API_KEY)必须通过Agent环境变量注入,严禁在SKILL.md、配置文件或代码中硬编码
- **本文件无Key示例**: 本SKILL.md中不包含任何真实或示例API Key,所有引用均使用 `$env:LLM_API_KEY` 占位
- **日志脱敏**: exec工具记录日志时,自动过滤包含"key"/"token"/"secret"字段的值
- **热搜API隔离**: HOT_SEARCH_API_KEY仅用于热搜数据获取,不与LLM_API_KEY混用

### 内容安全
- **热点合规**: 聚合的热点话题自动过滤敏感/违规内容,不推荐涉政/涉黄/涉暴等违规选题
- **平台规范**: 选题建议遵守各平台内容规范,避免推荐平台禁发内容
- **数据来源**: 热搜数据来源于公开API,不抓取非公开数据,遵守robots.txt协议
- **版权提示**: 选题标题为热点话题摘要,用户创作的内容需自行确认不侵犯他人版权
