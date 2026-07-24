---
slug: viral-prophet
name: viral-prophet
version: 1.0.1
displayName: "爆款预言机"
summary: "发布前预测爆款潜力,6维潜力评分+5大爆款要素+竞品对比,3秒出预测报告"
license: Proprietary
description: |-
  爆款预言机是一款内容爆款潜力预测工具,发布前评估内容表现.
  基于6维潜力评分、5大爆款要素分析与竞品对比,3秒生成预测报告.
  核心能力:
  - 6维潜力评分模型
  - 5大爆款要素分析
  - 竞品对比分析
  - 优化建议与发布时机推荐
homepage: "https://skillhub.cn"
tags:
  - 爆款预测
  - 内容评估
  - 发布前自检
  - 数据驱动
tools:
  - read
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "exec", "glob", "grep"]
tags: "工具,效率,自动化"
category: "Automation"
---
# 爆款预言机 v1.1.0

发布前预测内容的爆款潜力,基于6维潜力评分+5大爆款要素+竞品对比,3秒生成预测报告,指导内容优化和发布决策.
> **关键说明**: 本工具基于历史爆款规律和LLM分析进行预测,预测结果仅供参考,实际爆款效果受平台算法/发布时机/账号权重等多因素影响,无法保证100%准确.
## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 高级参数配置与自定义规则 | 不支持 | 支持 |
| 批量任务编排与队列管理 | 不支持 | 支持 |
| 结果导出与多格式转换 | 不支持 | 支持 |
| 实时状态监控与异常告警 | 不支持 | 支持 |
| 历史记录回溯与差异对比 | 不支持 | 支持 |

## 核心能力

1. **6维潜力评分模型**: 钩子吸引力(20%)+情绪强度(20%)+价值密度(20%)+结构清晰度(15%)+节奏控制(15%)+CTA转化(10%),0-100分加权计算
2. **5大爆款要素分析**: 选题热度/标题吸引力/开篇钩子/内容价值/互动设计,逐要素评估爆款潜力
3. **竞品对比分析**: 与同类爆款内容对比,识别优势和差距,提供差异化建议
4. **优化建议生成**: 基于评分和要素分析,提供具体的优化建议(哪里需要改进)
5. **发布时机建议**: 基于平台活跃时间和热点趋势,建议最佳发布时间
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 发布前潜力预测 | content+platform | prediction(6维评分+5要素分析+爆款概率+优化建议) |
| 竞品对比分析 | content+competitor_contents | 对比评分+优势差距+差异化建议 |
| 内容优化指导 | content+platform | 优化建议+优先级排序+优化后预估评分 |
| 发布时机建议 | content+platform+target_audience | 最佳发布时间+活跃时段分析 |
| 多内容筛选 | contents[]+platform | 多篇内容评分排序+推荐发布顺序 |

**不适用于**: 已发布内容的效果分析(使用viral-decoder拆解)、海外平台内容预测(聚焦国内平台)、非中文内容、纯图片/视频内容(需文本)、新闻/学术等专业内容(非爆款导向).
## 使用流程

### Step 1: 环境准备
- 确认Agent已加载本SKILL.md,且支持exec工具
- 在Agent环境变量中配置 `LLM_API_KEY`(必需)
- 热搜API为可选,用于选题热度分析,不可用时降级为LLM判断

### Step 2: 接收输入参数
- 必填: `content`(待预测内容文本)
- 选填: `platform`(发布平台)、`competitor_contents`(竞品内容列表)、`target_audience`(目标受众)

### Step 3: 6维潜力评分
- 钩子吸引力(20%): 开篇3秒抓注意力能力
- 情绪强度(20%): 情绪触发和共鸣程度
- 价值密度(20%): 单位字数的价值交付
- 结构清晰度(15%): 内容组织逻辑性
- 节奏控制(15%): 阅读节奏和信息密度
- CTA转化(10%): 转化引导有效性
- 加权计算总分(0-100)

### Step 4: 5大爆款要素分析
- 选题热度: 话题是否处于上升趋势(依赖热搜API,不可用时LLM判断)
- 标题吸引力: 标题的点击吸引力
- 开篇钩子: 前3秒钩子手法和强度
- 内容价值: 提供给读者的价值类型和密度
- 互动设计: 互动引导和分享触发设计

### Step 5: 竞品对比(可选)
- 与competitor_contents中的同类爆款对比
- 识别优势和差距
- 提供差异化建议

### Step 6: 爆款概率预测
- 基于评分和要素分析,预测爆款概率
- 概率分级: 高(>80分)/中高(70-79)/中(60-69)/低(<60)

### Step 7: 优化建议生成
- 基于评分最低维度,提供优化建议
- 建议按优先级排序(先优化最低分维度)
- 提供优化后预估评分

### Step 8: 发布时机建议
- 基于平台活跃时间(小红书晚8-10点/抖音午12-14点和晚8-10点等)
- 结合热点趋势(如有热搜数据)
- 建议最佳发布时间

### Step 9: 输出预测报告
- prediction: 6维评分+5要素分析+爆款概率
- optimization: 优化建议+优先级
- timing: 发布时机建议

## 输入格式

```json
{
  "content": "待预测的内容全文...",
  "platform": "xiaohongshu",
  "competitor_contents": ["竞品内容1", "竞品内容2"],
  "target_audience": "25-35岁女性"
}
```

| 字段 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 是 | 待预测的内容全文 |
| platform | string | 否 | 发布平台: xiaohongshu/douyin/wechat/weibo/zhihu |
| competitor_contents | string[] | 否 | 竞品内容列表,用于对比分析 |
| target_audience | string | 否 | 目标受众描述,用于发布时机建议 |

## 输出格式

```json
{
  "success": true,
  "data": {
    "prediction": {
      "viral_score": 82,
      "viral_probability": "中高",
      "score_details": {
        "hook_attractiveness": 85,
        "emotion_intensity": 80,
        "value_density": 88,
        "structure_clarity": 82,
        "pacing_control": 78,
        "cta_conversion": 75
      },
      "elements_analysis": {
        "topic_heat": {"score": 88, "trend": "rising", "analysis": "AI编程话题处于上升趋势"},
        "title_attractiveness": {"score": 85, "analysis": "标题含数字+痛点,吸引力强"},
        "opening_hook": {"score": 85, "type": "curiosity_suspense", "analysis": "开篇用疑问句制造悬念"},
        "content_value": {"score": 88, "type": "practical", "analysis": "提供5个工具+实操步骤,价值密度高"},
        "interaction_design": {"score": 75, "analysis": "互动引导较弱,可增加评论诱饵"}
      }
    },
    "optimization": {
      "suggestions": [
        {"dimension": "cta_conversion", "current_score": 75, "suggestion": "增加互动诱饵,如'评论区告诉我你用哪个'", "estimated_improvement": 8},
        {"dimension": "pacing_control", "current_score": 78, "suggestion": "中段信息密度过高,可拆分为更短段落", "estimated_improvement": 5}
      ],
      "estimated_score_after_optimization": 87
    },
    "timing": {
      "best_publish_time": "20:00-22:00",
      "reason": "小红书用户活跃高峰,AI类内容晚间互动率更高",
      "alternative_time": "12:00-14:00",
      "alternative_reason": "午休时段次高峰"
    },
    "competitor_comparison": {
      "avg_competitor_score": 78,
      "your_score": 82,
      "advantages": ["价值密度更高", "结构更清晰"],
      "gaps": ["CTA转化较弱", "互动设计不足"],
      "differentiation_suggestion": "可强化互动设计,增加评论区诱饵,差异化竞争"
    }
  },
  "error": null,
  "code": null
}
```

## 6维潜力评分模型

| 维度 | 权重 | 评分标准 | 优化方向 |
|:---:|:---:|:---:|:---:|
| 钩子吸引力 | 20% | 开篇3秒抓注意力能力 | 优化开篇钩子手法 |
| 情绪强度 | 20% | 情绪触发和共鸣程度 | 增强情绪触发点 |
| 价值密度 | 20% | 单位字数的价值交付 | 提升信息密度 |
| 结构清晰度 | 15% | 内容组织逻辑性 | 优化内容结构 |
| 节奏控制 | 15% | 阅读节奏和信息密度 | 调整段落和节奏 |
| CTA转化 | 10% | 转化引导有效性 | 强化CTA话术 |

**爆款概率分级**:
- 高(90-100): 爆款潜力强,建议直接发布
- 中高(80-89): 爆款潜力较好,建议小优化后发布
- 中(70-79): 有一定潜力,建议优化后发布
- 中低(60-69): 潜力一般,建议重点优化
- 低(<60): 爆款潜力弱,建议大改或放弃

## 异常处理

| 异常场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 内容为空 | 未提供content参数 | 返回success=false, error="内容不能为空" |
| 内容过短 | content<50字 | 返回success=false, error="内容过短,无法有效预测(需≥50字)" |
| 内容过长 | content>10000字 | 截断保留前10000字,标注warning |
| 平台不支持 | platform不在支持范围内 | 降级为通用预测,不针对平台优化,标注warning |
| 评分异常 | LLM评分返回格式异常 | 使用默认评分(各维度75分),标注warning |
| 要素分析失败 | LLM分析异常 | 跳过该要素,继续分析其他要素,标注warning |
| 竞品对比失败 | competitor_contents为空或LLM异常 | 跳过竞品对比,仅输出评分和建议,标注warning |
| 热搜API不可用 | API服务下线或鉴权失败 | 选题热度降级为LLM判断,标注warning |
| 优化建议生成失败 | LLM生成异常 | 跳过优化建议,仅输出评分,标注warning |
| 发布时机建议失败 | LLM分析异常 | 使用默认建议(晚8-10点),标注warning |
| LLM调用失败 | LLM服务不可用或超时 | 返回success=false, error="预测LLM调用失败" |
| LLM_API_KEY未配置 | 环境变量缺失 | 返回error,提示配置环境变量 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|---:|:---|---:|---:|:---|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | 国内可用: 通义千问/文心一言/智谱GLM/DeepSeek/Kimi |
| 热搜数据API | API | 可选 | 选题热度分析(不可用时降级为LLM判断) | 国内替代: 微博热搜API/百度热搜/头条热榜/新榜API |

### API Key 配置(零暴露原则)
- **LLM_API_KEY**: 必需(通常由Agent内置) - 潜力评分/要素分析/优化建议/发布时机
- **HOT_SEARCH_API_KEY**: 可选 - 选题热度分析(不可用时降级为LLM判断)
- **配置方式**: 必须通过Agent环境变量注入,严禁在SKILL.md或代码中硬编码API Key
- **安全检查**: 本SKILL.md中不包含任何API Key示例,所有Key均通过 `$env:LLM_API_KEY` 等环境变量读取

### 使用流程(补充)
纯LLM驱动,热搜API不可用时降级为LLM判断选题热度。预测结果仅供参考,不保证100%准确.
只需将SKILL.md文件放入Agent的skills目录即可直接使用.
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力.
### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 小红书内容发布前预测

**输入**:
```json
{
  "content": "你绝对想不到这个AI工具这么好用!作为一个非程序员,我用了3天就做出了自己的小程序。今天分享5个超好用的AI编程工具,让你也能轻松上手,告别代码恐惧!\n\n1. Cursor:AI代码编辑器\n2. GitHub Copilot:智能代码补全\n3. ChatGPT:全能AI助手\n4. Claude:长文本理解强\n5. v0:UI生成神器\n\n赶紧试试吧~\n\n#AI编程 #效率工具",
  "platform": "xiaohongshu"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "prediction": {
      "viral_score": 82,
      "viral_probability": "中高",
      "score_details": {
        "hook_attractiveness": 85,
        "emotion_intensity": 80,
        "value_density": 88,
        "structure_clarity": 82,
        "pacing_control": 78,
        "cta_conversion": 75
      },
      "elements_analysis": {
        "topic_heat": {"score": 88, "trend": "rising", "analysis": "AI编程话题处于上升趋势"},
        "title_attractiveness": {"score": 85, "analysis": "标题含数字+痛点,吸引力强"},
        "opening_hook": {"score": 85, "type": "curiosity_suspense", "analysis": "开篇用疑问句制造悬念"},
        "content_value": {"score": 88, "type": "practical", "analysis": "提供5个工具+实操步骤,价值密度高"},
        "interaction_design": {"score": 75, "analysis": "互动引导较弱,可增加评论诱饵"}
      }
    },
    "optimization": {
      "suggestions": [
        {"dimension": "cta_conversion", "current_score": 75, "suggestion": "增加互动诱饵,如'评论区告诉我你用哪个'", "estimated_improvement": 8},
        {"dimension": "pacing_control", "current_score": 78, "suggestion": "中段信息密度过高,可拆分为更短段落", "estimated_improvement": 5}
      ],
      "estimated_score_after_optimization": 87
    },
    "timing": {
      "best_publish_time": "20:00-22:00",
      "reason": "小红书用户活跃高峰,AI类内容晚间互动率更高",
      "alternative_time": "12:00-14:00",
      "alternative_reason": "午休时段次高峰"
    }
  },
  "error": null,
  "code": null
}
```

### 示例2: 抖音内容预测+竞品对比

**输入**:
```json
{
  "content": "月入3万的副业,居然只需要一部手机?今天告诉你3个手机就能做的副业...\n第一,短视频带货\n第二,知识付费\n第三,社群运营\n关注我,下期详细讲!",
  "platform": "douyin",
  "competitor_contents": ["月入过万的3个副业,手把手教你...", "手机就能做的副业,亲测有效..."]
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "prediction": {
      "viral_score": 88,
      "viral_probability": "中高",
      "score_details": {
        "hook_attractiveness": 92,
        "emotion_intensity": 88,
        "value_density": 85,
        "structure_clarity": 88,
        "pacing_control": 88,
        "cta_conversion": 90
      },
      "elements_analysis": {
        "topic_heat": {"score": 90, "trend": "rising", "analysis": "副业话题持续热门"},
        "title_attractiveness": {"score": 92, "analysis": "数字+反差,吸引力极强"},
        "opening_hook": {"score": 92, "type": "curiosity_suspense", "analysis": "月入3万+一部手机制造强反差"},
        "content_value": {"score": 85, "type": "practical", "analysis": "3个副业+操作方式,价值明确"},
        "interaction_design": {"score": 90, "analysis": "下期预告制造期待,关注转化强"}
      }
    },
    "optimization": {
      "suggestions": [
        {"dimension": "value_density", "current_score": 85, "suggestion": "可增加数据佐证,如'我第1个月赚了XX'", "estimated_improvement": 5}
      ],
      "estimated_score_after_optimization": 90
    },
    "timing": {
      "best_publish_time": "12:00-14:00",
      "reason": "抖音午休时段副业类内容互动率最高",
      "alternative_time": "20:00-22:00",
      "alternative_reason": "晚间高峰时段"
    },
    "competitor_comparison": {
      "avg_competitor_score": 82,
      "your_score": 88,
      "advantages": ["钩子更强(反差更大)", "CTA转化更高(下期预告)"],
      "gaps": ["价值密度略低(缺少数据佐证)"],
      "differentiation_suggestion": "保持钩子优势,补充数据佐证提升价值密度,可形成差异化竞争"
    }
  },
  "error": null,
  "code": null
}
```

### 示例3: 多内容筛选

**输入**:
```json
{
  "contents": [
    "你绝对想不到这个AI工具这么好用!分享5个AI编程工具...",
    "AI编程工具哪个好?对比了10款工具,这3款最值得用...",
    "用AI编程3个月,我的效率提升了10倍..."
  ],
  "platform": "xiaohongshu"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "ranking": [
      {"index": 0, "viral_score": 82, "viral_probability": "中高", "recommendation": "推荐发布,建议优化CTA"},
      {"index": 1, "viral_score": 78, "viral_probability": "中", "recommendation": "建议优化标题后发布"},
      {"index": 2, "viral_score": 75, "viral_probability": "中", "recommendation": "建议增加价值密度后发布"}
    ],
    "recommended_order": [0, 1, 2],
    "summary": {
      "total_contents": 3,
      "best_score": 82,
      "avg_score": 78,
      "publish_recommendation": "建议优先发布内容0,评分最高且优化空间小"
    }
  },
  "error": null,
  "code": null
}
```

### 示例4: 低分内容优化建议

**输入**:
```json
{
  "content": "今天给大家推荐几个AI工具。第一个是Cursor,第二个是Copilot,第三个是ChatGPT。这些工具都很好用,大家可以试试。",
  "platform": "xiaohongshu"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "prediction": {
      "viral_score": 58,
      "viral_probability": "低",
      "score_details": {
        "hook_attractiveness": 50,
        "emotion_intensity": 45,
        "value_density": 65,
        "structure_clarity": 60,
        "pacing_control": 55,
        "cta_conversion": 40
      },
      "elements_analysis": {
        "topic_heat": {"score": 85, "trend": "rising", "analysis": "AI工具话题热门"},
        "title_attractiveness": {"score": 50, "analysis": "无标题,开篇平淡无吸引力"},
        "opening_hook": {"score": 50, "type": "none", "analysis": "无钩子,开篇无法抓注意力"},
        "content_value": {"score": 65, "type": "practical", "analysis": "有工具推荐但缺少实操细节"},
        "interaction_design": {"score": 40, "analysis": "无互动引导,无CTA"}
      }
    },
    "optimization": {
      "suggestions": [
        {"dimension": "cta_conversion", "current_score": 40, "suggestion": "增加CTA,如'评论区告诉我你用哪个'", "estimated_improvement": 20},
        {"dimension": "emotion_intensity", "current_score": 45, "suggestion": "增加痛点共鸣,如'非程序员也能上手'", "estimated_improvement": 18},
        {"dimension": "hook_attractiveness", "current_score": 50, "suggestion": "优化开篇钩子,用疑问句或数字制造悬念", "estimated_improvement": 25}
      ],
      "estimated_score_after_optimization": 78
    },
    "timing": {
      "best_publish_time": "20:00-22:00",
      "reason": "小红书用户活跃高峰",
      "alternative_time": "12:00-14:00",
      "alternative_reason": "午休时段"
    }
  },
  "error": null,
  "code": null
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成.
### 案例1: 小红书内容发布前预测(6维评分+优化建议+发布时机)

**输入**:
```json
{
  "content": "姐妹们!这个平价面霜绝了!才59元,用了一周皮肤细腻到发光!之前花300多买的大牌面霜都没这效果!我是混干皮,换季起皮特别严重,用了这个完全不起了!成分有烟酰胺+玻尿酸,保湿提亮一步到位!用法:早晚洁面后取黄豆大小,手心搓热按压上脸,吸收超快不黏腻!预算有限的姐妹试试,不好用你来找我!#平价护肤 #面霜推荐 #烟酰胺 #学生党护肤",
  "platform": "xiaohongshu",
  "target_audience": "18-25岁女性"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "prediction": {
      "viral_score": 85,
      "viral_probability": "中高",
      "score_details": {
        "hook_attractiveness": 90,
        "emotion_intensity": 85,
        "value_density": 88,
        "structure_clarity": 85,
        "pacing_control": 82,
        "cta_conversion": 88
      },
      "elements_analysis": {
        "topic_heat": {"score": 86, "trend": "rising", "analysis": "平价护肤话题持续上升,学生党护肤需求旺盛"},
        "title_attractiveness": {"score": 88, "analysis": "首句'绝了+59元'双重钩子,吸引力强"},
        "opening_hook": {"score": 90, "type": "pain_resonance+curiosity_suspense", "analysis": "情绪共鸣(姐妹们)+好奇悬念(绝了)+价格锚点(59元),3秒3信息"},
        "content_value": {"score": 88, "type": "practical", "analysis": "5个价值点(价格/肤质/成分/用法/效果),价值密度高"},
        "interaction_design": {"score": 75, "analysis": "话题标签有但互动引导较弱,可增加评论区诱饵"}
      }
    },
    "optimization": {
      "suggestions": [
        {"dimension": "interaction_design", "current_score": 75, "suggestion": "增加评论诱饵,如'评论区告诉我你的肤质,我帮你选'", "estimated_improvement": 10},
        {"dimension": "pacing_control", "current_score": 82, "suggestion": "中段信息密集,可拆分为短段落增强可读性", "estimated_improvement": 5},
        {"dimension": "structure_clarity", "current_score": 85, "suggestion": "可增加小标题(如【成分】【用法】)提升结构感", "estimated_improvement": 3}
      ],
      "estimated_score_after_optimization": 90
    },
    "timing": {
      "best_publish_time": "20:00-22:00",
      "reason": "小红书用户活跃高峰时段,18-25岁女性晚间护肤话题互动率最高",
      "alternative_time": "12:00-14:00",
      "alternative_reason": "午休时段次高峰,适合种草类内容浏览"
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓6维潜力评分正确(总分85分,中高概率) ✓5大爆款要素分析完整 ✓优化建议3条(按优先级排序) ✓优化后预估90分(+5分) ✓发布时机建议(晚8-10点+午12-14点)

### 案例2: 竞品对比分析(多竞品对比+差异化建议)

**输入**:
```json
{
  "content": "姐妹们!这个平价面霜绝了!才59元,用了一周皮肤细腻到发光!成分有烟酰胺+玻尿酸,保湿提亮一步到位!不好用你来找我!#平价护肤 #面霜推荐",
  "platform": "xiaohongshu",
  "competitor_contents": [
    "推荐一款好用的面霜,59元,含有烟酰胺成分,保湿效果不错,适合干皮使用。",
    "最近入手的平价面霜,价格59元,用了一段时间感觉还可以,成分有玻尿酸和烟酰胺,性价比还行。"
  ]
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "prediction": {
      "viral_score": 82,
      "viral_probability": "中高",
      "score_details": {
        "hook_attractiveness": 90,
        "emotion_intensity": 85,
        "value_density": 80,
        "structure_clarity": 82,
        "pacing_control": 80,
        "cta_conversion": 88
      },
      "elements_analysis": {
        "topic_heat": {"score": 86, "trend": "rising", "analysis": "平价护肤话题上升趋势"},
        "title_attractiveness": {"score": 88, "analysis": "情绪+悬念+价格三重钩子"},
        "opening_hook": {"score": 90, "type": "pain_resonance+curiosity_suspense", "analysis": "3秒3信息,吸引力强"},
        "content_value": {"score": 80, "type": "practical", "analysis": "价值点完整但篇幅较短"},
        "interaction_design": {"score": 75, "analysis": "有话题标签但互动引导弱"}
      }
    },
    "optimization": {
      "suggestions": [
        {"dimension": "interaction_design", "current_score": 75, "suggestion": "增加评论诱饵", "estimated_improvement": 10},
        {"dimension": "pacing_control", "current_score": 80, "suggestion": "增加痛点描述提升节奏感", "estimated_improvement": 5}
      ],
      "estimated_score_after_optimization": 88
    },
    "timing": {
      "best_publish_time": "20:00-22:00",
      "reason": "小红书活跃高峰",
      "alternative_time": "12:00-14:00",
      "alternative_reason": "午休次高峰"
    },
    "competitor_comparison": {
      "avg_competitor_score": 68,
      "your_score": 82,
      "advantages": ["钩子吸引力远超竞品(90vs65)", "情绪强度更高(85vs60)", "CTA转化更强(88vs55)", "信任承诺式CTA竞品缺失"],
      "gaps": ["内容篇幅较短", "缺少使用方法详述"],
      "differentiation_suggestion": "你的内容在钩子和CTA上显著优于竞品,建议保持情绪化表达+信任承诺策略。可补充使用方法和肤质适配描述,进一步拉大差距。竞品均为平铺直叙型,你的情绪种草风格是核心差异化优势。"
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓竞品对比分析正确(你的82分vs竞品均68分) ✓优势识别4条(钩子/情绪/CTA/信任承诺) ✓差距识别2条(篇幅/方法) ✓差异化建议针对性(情绪种草vs平铺直叙) ✓优势量化对比(90vs65/85vs60/88vs55)

### 案例3: 多内容筛选排序(3篇内容评分排序+推荐发布顺序)

**输入**:
```json
{
  "content": "placeholder",
  "platform": "xiaohongshu",
  "contents": [
    "姐妹们!这个平价面霜绝了!才59元,用了一周皮肤细腻到发光!成分有烟酰胺+玻尿酸,保湿提亮一步到位!不好用你来找我!#平价护肤",
    "推荐一款59元面霜,含有烟酰胺和玻尿酸,保湿效果不错,适合干皮,性价比高。",
    "救命!这款59元面霜也太好用了吧!混干皮本命!烟酰胺+玻尿酸双效保湿,一周告别起皮!姐妹们冲!评论区告诉我你的肤质!"
  ]
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "ranking": [
      {"index": 2, "viral_score": 88, "viral_probability": "中高", "recommendation": "情绪钩子最强(救命!)+互动设计最佳(评论区告诉我),建议首发"},
      {"index": 0, "viral_score": 82, "viral_probability": "中高", "recommendation": "信任承诺CTA(不好用找我)+价格锚点清晰,建议第2发布"},
      {"index": 1, "viral_score": 65, "viral_probability": "中低", "recommendation": "平铺直叙缺钩子,建议优化后再发或作为SEO长尾内容"}
    ],
    "recommended_order": [2, 0, 1],
    "summary": {
      "total_contents": 3,
      "best_score": 88,
      "avg_score": 78,
      "publish_recommendation": "建议优先发布内容2(88分),情绪钩子和互动设计最强;内容1(65分)建议增加情绪钩子优化后再发"
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓3篇内容评分排序正确(88/82/65) ✓推荐发布顺序清晰(recommended_order=[2,0,1]) ✓每篇recommendation理由说明 ✓summary汇总统计完整(3篇/best88/avg78) ✓爆款概率分级正确(中高/中高/中低)

### 案例4: 低分内容优化指导(优化后预估提升15分)

**输入**:
```json
{
  "content": "推荐一款面霜,59元,有烟酰胺,保湿效果不错,适合干皮,大家可以试试。",
  "platform": "xiaohongshu"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "prediction": {
      "viral_score": 58,
      "viral_probability": "低",
      "score_details": {
        "hook_attractiveness": 50,
        "emotion_intensity": 45,
        "value_density": 65,
        "structure_clarity": 60,
        "pacing_control": 55,
        "cta_conversion": 50
      },
      "elements_analysis": {
        "topic_heat": {"score": 86, "trend": "rising", "analysis": "平价护肤话题热度高,但内容未能借势"},
        "title_attractiveness": {"score": 50, "analysis": "无钩子,平铺直叙,缺乏吸引力"},
        "opening_hook": {"score": 50, "type": "none", "analysis": "无开篇钩子,前3秒无抓力"},
        "content_value": {"score": 65, "type": "practical", "analysis": "有基本价值点(价格/成分/肤质)但缺少效果描述"},
        "interaction_design": {"score": 40, "analysis": "无互动引导,无话题标签"}
      }
    },
    "optimization": {
      "suggestions": [
        {"dimension": "hook_attractiveness", "current_score": 50, "suggestion": "增加情绪钩子:'姐妹们!这款59元面霜绝了!'", "estimated_improvement": 35},
        {"dimension": "emotion_intensity", "current_score": 45, "suggestion": "增加效果感受:'用了一周皮肤细腻到发光!'", "estimated_improvement": 30},
        {"dimension": "cta_conversion", "current_score": 50, "suggestion": "增加信任承诺CTA:'不好用你来找我!'", "estimated_improvement": 35},
        {"dimension": "pacing_control", "current_score": 55, "suggestion": "增加感叹号和短句提升节奏感", "estimated_improvement": 20},
        {"dimension": "interaction_design", "current_score": 40, "suggestion": "增加话题标签和评论诱饵", "estimated_improvement": 30}
      ],
      "estimated_score_after_optimization": 88,
      "optimized_content_example": "姐妹们!这款59元面霜绝了!用了一周皮肤细腻到发光!有烟酰胺+玻尿酸,保湿提亮一步到位!混干皮换季必入,不好用你来找我!#平价护肤 #面霜推荐 #烟酰胺"
    },
    "timing": {
      "best_publish_time": "20:00-22:00",
      "reason": "小红书活跃高峰",
      "alternative_time": "12:00-14:00",
      "alternative_reason": "午休次高峰"
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓低分内容正确识别(58分,低概率) ✓5个维度优化建议(按优先级排序) ✓优化后预估88分(+30分提升) ✓优化后内容示例提供 ✓最弱维度精准定位(互动设计40分/情绪强度45分)

## 常见问题

### Q1: 如何开始使用爆款预言机?
A: 两步启动:(1)将SKILL.md放入Agent的skills目录;(2)确认Agent环境变量已配置LLM_API_KEY。调用时传入content(必填)即可预测,platform和competitor_contents可选。纯LLM驱动,热搜API为可选.
### Q2: 预测结果准确吗?
A: 预测基于历史爆款规律和LLM分析,准确率受多因素影响:(1)内容本身质量(评分越高越准);(2)平台算法变化;(3)发布时机和账号权重。评分>80的内容爆款概率较高,评分<60建议优化。预测仅供参考,不保证100%准确.
### Q3: 6维潜力评分和5大爆款要素有什么区别?
A: 6维潜力评分是量化评分(钩子/情绪/价值/结构/节奏/CTA,0-100分),5大爆款要素是定性分析(选题热度/标题/开篇/价值/互动,含趋势分析)。两者互补,评分提供量化参考,要素分析提供优化方向.
### Q4: 优化建议如何使用?
A: optimization字段按优先级排序优化建议:(1)先优化current_score最低的维度;(2)estimated_improvement显示预估提升分数;(3)estimated_score_after_optimization显示优化后预估总分。建议按优先级逐项优化,优化后重新预测.
### Q5: 竞品对比如何使用?
A: 传入competitor_contents(竞品内容列表)后,系统对比你的内容与竞品:(1)avg_competitor_score显示竞品平均分;(2)advantages/gaps识别你的优势和差距;(3)differentiation_suggestion提供差异化建议。建议选择同类爆款作为竞品,对比更有参考价值.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **预测准确度**: 预测基于历史规律和LLM分析,无法保证100%准确,实际效果受平台算法/发布时机/账号权重等多因素影响
- **语言限制**: 仅支持中文内容预测,不支持英文/其他语种
- **内容类型**: 仅支持文本内容预测,纯图片/视频内容需先转为文本
- **内容长度**: 建议50-10000字,过短无法有效预测,过长会截断
- **平台覆盖**: 主要支持国内5平台(小红书/抖音/公众号/微博/知乎),海外平台预测准确度可能降低
- **评分主观性**: 6维度评分基于LLM判断,不同模型评分可能差异较大,评分仅作参考
- **热搜依赖**: 选题热度分析依赖热搜API,不可用时降级为LLM判断,准确度降低
- **竞品对比限制**: 竞品对比基于文本相似度,无法完全反映实际竞争情况

## 安全

### API Key 零暴露原则
- **环境变量注入**: 所有API Key(LLM_API_KEY/HOT_SEARCH_API_KEY)必须通过Agent环境变量注入,严禁在SKILL.md、配置文件或代码中硬编码
- **本文件无Key示例**: 本SKILL.md中不包含任何真实或示例API Key,所有引用均使用 `$env:LLM_API_KEY` 占位
- **日志脱敏**: exec工具记录日志时,自动过滤包含"key"/"token"/"secret"字段的值
- **热搜API隔离**: HOT_SEARCH_API_KEY仅用于选题热度分析,不与LLM_API_KEY混用

### 内容安全
- **预测合规**: 预测结果用于内容优化参考,不用于恶意操控平台算法或刷量
- **竞品分析合规**: 竞品对比仅用于学习参考,不用于恶意竞争或贬低竞品
- **数据隐私**: 预测内容不包含个人隐私信息,如意外包含会自动脱敏处理
- **版权提示**: 预测的内容为用户原创,用户需自行确认拥有内容版权
- **预测结果使用边界**: 预测结果仅供参考,不作为发布决策的唯一依据,使用者需结合自身判断
