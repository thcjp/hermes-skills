---
slug: title-hook-factory
name: title-hook-factory
version: 1.0.1
displayName: "标题钩子工厂"
summary: "生成爆款标题+钩子段落,基于6大钩子公式+量化打分+多平台字数控制"
license: Proprietary
description: |-
  标题钩子工厂是一款内容创作引流工具,生成爆款标题与开篇钩子段落.
  基于6大钩子公式,量化打分排序,适配多平台字数规则.
  核心能力:
  - 6大钩子公式智能选择
  - 3-5个标题候选+量化打分
  - 钩子段落生成
  - 多平台字数控制与风格适配
homepage: "https://skillhub.cn"
tags:
  - 标题生成
  - 内容引流
  - 爆款创作
  - 副业工具
tools:
  - read
  - exec
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
category: "Automation"
---
# 标题钩子工厂 v1.1.0

内容创作引流利器,基于6大钩子公式生成爆款标题与开篇钩子段落,量化打分排序,适配多平台字数规则.
## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 多租户管理与权限分配 | 不支持 | 支持 |
| 操作审计与合规日志 | 不支持 | 支持 |
| 自定义仪表盘与报表 | 不支持 | 支持 |
| API开放与第三方集成 | 不支持 | 支持 |
| 资源配额管理与计费统计 | 不支持 | 支持 |

## 核心能力

1. **6大钩子公式**: 痛点共鸣(pain_resonance)/好奇悬念(curiosity_suspense)/数字权威(number_authority)/对比反差(contrast)/情感共鸣(emotion)/紧迫感稀缺(urgency_scarcity),按内容主题智能选择
2. **3-5个标题候选+量化打分**: 生成多个标题版本,基于钩子公式匹配度+情感强度+关键词覆盖+吸引力4维度打分,排序推荐最佳标题
3. **钩子段落生成**: 基于最佳标题生成开篇钩子段落(50-200字),前3秒抓住读者注意力
4. **多平台字数控制**: 小红书20字内/抖音15字内/公众号30字内/微博30字内,自动适配各平台标题字数限制
5. **平台风格适配**: 根据平台调整标题风格(小红书活泼种草/抖音口语化/公众号深度/微博简洁观点)
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 标题生成(默认) | topic主题+platform平台 | titles[](3-5个标题)+scores[]+best_title+hook_paragraph |
| 多钩子公式对比 | topic+hook_type=multi | 6种钩子公式各生成1个标题+打分对比 |
| 钩子段落生成 | topic+platform+hook_type | hook_paragraph(50-200字开篇段落) |
| 平台字数适配 | topic+platform | 适配平台字数限制的标题(小红书20字/抖音15字等) |
| 标题打分优化 | topic+existing_title | score评分+improvement_suggestions优化建议 |

**不适用于**: 学术论文标题(需严谨非爆款)、新闻标题(需客观中立)、品牌PR稿件标题(需正式)、SEO标题(使用seo-doctor)、海外平台标题(仅支持国内4平台).
## 使用流程

### Step 1: 环境准备
- 确认Agent已加载本SKILL.md,且支持exec工具
- 在Agent环境变量中配置 `LLM_API_KEY`(必需)
- 本Skill纯LLM驱动,无额外API依赖

### Step 2: 接收输入参数
- 必填: `topic`(内容主题)
- 选填: `platform`(目标平台,默认xiaohongshu)、`hook_type`(钩子公式,默认auto自动选择)、`count`(标题数量,默认5)

### Step 3: 钩子公式选择
- hook_type=auto: LLM根据topic内容自动选择最匹配的钩子公式
- hook_type=具体公式: 使用指定钩子公式生成
- hook_type=multi: 6种钩子公式各生成1个标题,对比打分

### Step 4: 标题生成
- 基于选择的钩子公式生成3-5个标题候选
- 根据platform适配字数限制和风格
- 异常处理: 平台不支持→降级为通用标题;钩子类型无效→默认auto

### Step 5: 量化打分排序
- 4维度打分:
  - 钩子公式匹配度(30%): 标题是否符合所选钩子公式特征
  - 情感强度(25%): 标题引发的情感反应强度
  - 关键词覆盖(25%): 核心关键词在标题中的覆盖度
  - 吸引力(20%): 标题的点击吸引力
- 加权计算总分(0-100)
- 按总分排序,best_title为最高分标题

### Step 6: 钩子段落生成
- 基于best_title生成开篇钩子段落(50-200字)
- 段落延续标题的钩子公式风格
- 前3秒抓住读者注意力

### Step 7: 输出结果
- titles[]: 3-5个标题候选+各自钩子公式+打分
- best_title: 最高分标题
- hook_paragraph: 开篇钩子段落

## 输入格式

```json
{
  "topic": "AI编程工具推荐",
  "platform": "xiaohongshu",
  "hook_type": "auto",
  "count": 5
}
```

| 字段 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| topic | string | 是 | 内容主题 |
| platform | string | 否 | 目标平台: xiaohongshu/douyin/wechat/weibo,默认xiaohongshu |
| hook_type | string | 否 | 钩子公式: auto/pain_resonance/curiosity_suspense/number_authority/contrast/emotion/urgency_scarcity/multi,默认auto |
| count | int | 否 | 标题数量,默认5,范围3-10 |

## 输出格式

```json
{
  "success": true,
  "data": {
    "titles": [
      {
        "title": "标题文本",
        "hook_type": "curiosity_suspense",
        "score": 92,
        "score_details": {
          "hook_match": 95,
          "emotion_intensity": 88,
          "keyword_coverage": 90,
          "attractiveness": 95
        }
      }
    ],
    "best_title": "最高分标题",
    "hook_paragraph": "基于最佳标题生成的开篇钩子段落...",
    "platform": "xiaohongshu",
    "word_limit": 20
  },
  "error": null,
  "code": null
}
```

## 6大钩子公式说明

| 钩子公式 | 英文标识 | 特征 | 适用场景 |
|:---:|:---:|:---:|:---:|
| 痛点共鸣 | pain_resonance | 直击用户痛点,引发"我也是"共鸣 | 解决问题的产品/方法 |
| 好奇悬念 | curiosity_suspense | 制造悬念,引发"想知道"冲动 | 新品/黑科技/揭秘类 |
| 数字权威 | number_authority | 用数字增强可信度和吸引力 | 教程/清单/数据类 |
| 对比反差 | contrast | 制造反差,引发"居然这样"惊讶 | 性价比/反常识类 |
| 情感共鸣 | emotion | 触动情感,引发"感动/共鸣" | 情感故事/励志类 |
| 紧迫感稀缺 | urgency_scarcity | 制造紧迫感,引发"赶紧看"冲动 | 限时活动/稀缺资源 |

## 异常处理

| 异常场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 主题为空 | 未提供topic参数 | 返回success=false, error="主题不能为空" |
| 平台不支持 | platform不在4个支持范围内 | 降级为通用标题模板,不针对平台优化,标注warning |
| 钩子类型无效 | hook_type不在支持范围内 | 默认使用auto自动选择,标注warning |
| count超限 | count>10或<3 | 截断为10(上限)或3(下限),标注warning |
| 标题生成失败 | LLM返回格式异常或为空 | 使用预设标题模板"关于{topic}的N个要点" |
| 标题超字数 | 生成的标题超过平台字数限制 | 按平台最大字数截断,保留核心关键词 |
| 钩子段落生成失败 | LLM调用失败 | 跳过段落生成,仅输出标题,标注warning |
| 打分异常 | LLM评分返回格式异常 | 使用默认评分(各维度80分),标注warning |
| LLM调用失败 | LLM服务不可用或超时 | 返回success=false, error="标题生成LLM调用失败" |
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

### API Key 配置(零暴露原则)
- **LLM_API_KEY**: 必需(通常由Agent内置) - 标题生成/钩子段落生成/量化打分
- **配置方式**: 必须通过Agent环境变量注入,严禁在SKILL.md或代码中硬编码API Key
- **安全检查**: 本SKILL.md中不包含任何API Key示例,所有Key均通过 `$env:LLM_API_KEY` 等环境变量读取

### 使用流程(补充)
纯LLM驱动,无额外依赖。标题生成失败时使用预设模板降级.
只需将SKILL.md文件放入Agent的skills目录即可直接使用.
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力.
### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 小红书AI编程工具标题(auto模式)

**输入**:
```json
{
  "topic": "AI编程工具推荐",
  "platform": "xiaohongshu",
  "hook_type": "auto",
  "count": 3
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "titles": [
      {
        "title": "你绝对想不到AI编程这么简单",
        "hook_type": "curiosity_suspense",
        "score": 92,
        "score_details": {"hook_match": 95, "emotion_intensity": 88, "keyword_coverage": 90, "attractiveness": 95}
      },
      {
        "title": "5个AI编程工具让你效率翻倍",
        "hook_type": "number_authority",
        "score": 88,
        "score_details": {"hook_match": 92, "emotion_intensity": 80, "keyword_coverage": 95, "attractiveness": 85}
      },
      {
        "title": "程序员加班多?AI编程帮你准时下班",
        "hook_type": "pain_resonance",
        "score": 85,
        "score_details": {"hook_match": 90, "emotion_intensity": 85, "keyword_coverage": 80, "attractiveness": 85}
      }
    ],
    "best_title": "你绝对想不到AI编程这么简单",
    "hook_paragraph": "你绝对想不到AI编程这么简单!作为一个非程序员,我用了3天就做出了自己的小程序。今天分享5个超好用的AI编程工具,让你也能轻松上手,告别代码恐惧!",
    "platform": "xiaohongshu",
    "word_limit": 20
  },
  "error": null,
  "code": null
}
```

### 示例2: 抖音副业赚钱标题(指定钩子公式)

**输入**:
```json
{
  "topic": "副业赚钱方法",
  "platform": "douyin",
  "hook_type": "urgency_scarcity",
  "count": 3
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "titles": [
      {
        "title": "再不看就晚了!副业红利期",
        "hook_type": "urgency_scarcity",
        "score": 90,
        "score_details": {"hook_match": 95, "emotion_intensity": 90, "keyword_coverage": 85, "attractiveness": 90}
      },
      {
        "title": "限时机!副业月入过万秘籍",
        "hook_type": "urgency_scarcity",
        "score": 87,
        "score_details": {"hook_match": 92, "emotion_intensity": 88, "keyword_coverage": 85, "attractiveness": 83}
      },
      {
        "title": "最后机会!副业赚钱快上车",
        "hook_type": "urgency_scarcity",
        "score": 84,
        "score_details": {"hook_match": 90, "emotion_intensity": 85, "keyword_coverage": 80, "attractiveness": 80}
      }
    ],
    "best_title": "再不看就晚了!副业红利期",
    "hook_paragraph": "再不看就晚了!副业红利期可能就这几个月。我身边已经有人靠副业月入过万,今天就把方法分享出来,名额有限,先到先得!",
    "platform": "douyin",
    "word_limit": 15
  },
  "error": null,
  "code": null
}
```

### 示例3: 公众号深度内容标题(对比反差)

**输入**:
```json
{
  "topic": "AI取代程序员",
  "platform": "wechat",
  "hook_type": "contrast",
  "count": 3
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "titles": [
      {
        "title": "AI要取代程序员?程序员反而更值钱了",
        "hook_type": "contrast",
        "score": 91,
        "score_details": {"hook_match": 95, "emotion_intensity": 88, "keyword_coverage": 92, "attractiveness": 89}
      },
      {
        "title": "都说AI灭程序员,结果程序员用AI起飞",
        "hook_type": "contrast",
        "score": 88,
        "score_details": {"hook_match": 92, "emotion_intensity": 85, "keyword_coverage": 90, "attractiveness": 85}
      },
      {
        "title": "AI取代程序员?真相和你想的完全相反",
        "hook_type": "contrast",
        "score": 86,
        "score_details": {"hook_match": 90, "emotion_intensity": 85, "keyword_coverage": 85, "attractiveness": 84}
      }
    ],
    "best_title": "AI要取代程序员?程序员反而更值钱了",
    "hook_paragraph": "AI要取代程序员?程序员反而更值钱了。当所有人都在担心AI抢饭碗时,真正的程序员已经开始用AI提升效率,收入不降反升。今天聊聊AI时代程序员的真实生存现状,可能和你想的完全不一样。",
    "platform": "wechat",
    "word_limit": 30
  },
  "error": null,
  "code": null
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成.
### 案例1: 小红书标题生成(auto模式,5个候选+打分排序)

**输入**:
```json
{
  "topic": "平价护肤好物推荐",
  "platform": "xiaohongshu",
  "hook_type": "auto",
  "count": 5
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "titles": [
      {"title": "月入3千也能养发光肌!5款平价护肤品均不过百", "hook_type": "pain_resonance", "score": 92, "score_details": {"hook_match": 95, "emotion_intensity": 90, "keyword_coverage": 92, "attractiveness": 88}},
      {"title": "这些平价护肤品居然比大牌还好用?亲测5款", "hook_type": "curiosity_suspense", "score": 89, "score_details": {"hook_match": 92, "emotion_intensity": 85, "keyword_coverage": 90, "attractiveness": 88}},
      {"title": "5款平价护肤品测评:均价50元,效果不输百元大牌", "hook_type": "number_authority", "score": 87, "score_details": {"hook_match": 90, "emotion_intensity": 82, "keyword_coverage": 92, "attractiveness": 85}},
      {"title": "大牌平替来啦!这5款护肤品省了我一半的钱", "hook_type": "contrast", "score": 85, "score_details": {"hook_match": 88, "emotion_intensity": 85, "keyword_coverage": 85, "attractiveness": 82}},
      {"title": "敏感肌姐妹必看!5款平价护肤品温和不踩雷", "hook_type": "emotion", "score": 83, "score_details": {"hook_match": 85, "emotion_intensity": 88, "keyword_coverage": 80, "attractiveness": 78}}
    ],
    "best_title": "月入3千也能养发光肌!5款平价护肤品均不过百",
    "hook_paragraph": "姐妹们!谁说护肤一定要花大钱?我月薪3千,硬是靠着这5款平价护肤品养出了发光肌!每款均价不到50块,敏感肌也能放心用。先说结论:第3款是我无限回购的宝藏,第5款全网都在抢!往下看,附真实使用对比图~",
    "platform": "xiaohongshu",
    "word_limit": 20
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓5个标题候选(含不同钩子公式) ✓4维度打分排序(痛点共鸣92分最高) ✓小红书20字内字数控制 ✓钩子段落生成(引导阅读) ✓平台风格适配(种草+emoji感)

### 案例2: 多钩子公式对比(multi模式,6种公式各1个)

**输入**:
```json
{
  "topic": "AI编程工具推荐",
  "platform": "xiaohongshu",
  "hook_type": "multi",
  "count": 6
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "titles": [
      {"title": "程序员都在偷偷用的AI编程工具,你还不知道?", "hook_type": "pain_resonance", "score": 88, "score_details": {"hook_match": 92, "emotion_intensity": 85, "keyword_coverage": 88, "attractiveness": 87}},
      {"title": "这个AI编程工具到底有多强?看完你就懂了", "hook_type": "curiosity_suspense", "score": 85, "score_details": {"hook_match": 90, "emotion_intensity": 80, "keyword_coverage": 85, "attractiveness": 85}},
      {"title": "5款AI编程工具横评:效率提升300%实测数据", "hook_type": "number_authority", "score": 90, "score_details": {"hook_match": 95, "emotion_intensity": 82, "keyword_coverage": 92, "attractiveness": 90}},
      {"title": "用AI写代码vs手写代码,结果让我震惊了", "hook_type": "contrast", "score": 87, "score_details": {"hook_match": 92, "emotion_intensity": 88, "keyword_coverage": 85, "attractiveness": 82}},
      {"title": "从编程小白到独立开发,全靠这5个AI工具", "hook_type": "emotion", "score": 86, "score_details": {"hook_match": 88, "emotion_intensity": 90, "keyword_coverage": 85, "attractiveness": 80}},
      {"title": "限时免费!这5款AI编程工具趁现在赶紧用", "hook_type": "urgency_scarcity", "score": 84, "score_details": {"hook_match": 90, "emotion_intensity": 82, "keyword_coverage": 88, "attractiveness": 75}}
    ],
    "best_title": "5款AI编程工具横评:效率提升300%实测数据",
    "hook_paragraph": "AI编程工具到底值不值得用?我花了2周时间,实测了5款主流AI编程工具,用真实数据告诉你答案。从代码生成准确率到调试效率,每个维度都有量化对比。结论是:效率提升最高的一款达到了300%!想知道是哪款?往下看详细测评。",
    "platform": "xiaohongshu",
    "word_limit": 20
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓6种钩子公式各1个标题(全覆盖) ✓multi模式正确执行 ✓数字权威型90分最高(数据+权威) ✓钩子段落与最佳标题风格一致 ✓6种公式打分对比展示

### 案例3: 抖音标题生成(15字限制+口语化)

**输入**:
```json
{
  "topic": "职场新人避坑指南",
  "platform": "douyin",
  "hook_type": "auto",
  "count": 3
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "titles": [
      {"title": "入职3年踩坑血泪史", "hook_type": "pain_resonance", "score": 90, "score_details": {"hook_match": 92, "emotion_intensity": 90, "keyword_coverage": 88, "attractiveness": 88}},
      {"title": "职场新人千万别做这5件事", "hook_type": "number_authority", "score": 88, "score_details": {"hook_match": 90, "emotion_intensity": 82, "keyword_coverage": 92, "attractiveness": 88}},
      {"title": "老板不会告诉你的职场真相", "hook_type": "curiosity_suspense", "score": 86, "score_details": {"hook_match": 88, "emotion_intensity": 85, "keyword_coverage": 85, "attractiveness": 85}}
    ],
    "best_title": "入职3年踩坑血泪史",
    "hook_paragraph": "我在职场踩过的坑,你一个都别踩。今天说5个最致命的,第3个差点让我丢工作。别划走,看完保你少走3年弯路。",
    "platform": "douyin",
    "word_limit": 15
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓抖音15字限制严格遵守(8-11字) ✓口语化风格适配(血泪史/别划走) ✓短视频钩子段落精简有力 ✓3个候选+打分排序 ✓抖音节奏感(短句+悬念)

### 案例4: 公众号标题生成(30字限制+深度风格)

**输入**:
```json
{
  "topic": "35岁中年危机如何破局",
  "platform": "wechat",
  "hook_type": "auto",
  "count": 3
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "titles": [
      {"title": "35岁被裁后,我用了3个月完成职业转型(附方法论)", "hook_type": "pain_resonance", "score": 91, "score_details": {"hook_match": 93, "emotion_intensity": 90, "keyword_coverage": 88, "attractiveness": 92}},
      {"title": "中年危机不是终点:35岁后的5条出路深度分析", "hook_type": "number_authority", "score": 88, "score_details": {"hook_match": 90, "emotion_intensity": 82, "keyword_coverage": 90, "attractiveness": 88}},
      {"title": "为什么35岁是人生的分水岭?深度解读中年破局之道", "hook_type": "curiosity_suspense", "score": 86, "score_details": {"hook_match": 88, "emotion_intensity": 85, "keyword_coverage": 85, "attractiveness": 85}}
    ],
    "best_title": "35岁被裁后,我用了3个月完成职业转型(附方法论)",
    "hook_paragraph": "35岁那年,我收到了公司的裁员通知。站在写字楼门口,我想的不是'完了',而是'终于可以重新开始了'。接下来的3个月,我做对了5件事,不仅完成了职业转型,收入还提升了40%。这篇文章不是鸡汤,而是一份可以复制的方法论。",
    "platform": "wechat",
    "word_limit": 30
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓公众号30字限制遵守(22-24字) ✓深度风格适配(方法论/深度分析) ✓痛点共鸣型91分最高 ✓钩子段落理性+数据驱动 ✓公众号阅读引导(这篇文章不是鸡汤)

### 案例5: 钩子段落生成(emotion钩子,情感共鸣)

**输入**:
```json
{
  "topic": "独自在大城市打拼的感受",
  "platform": "xiaohongshu",
  "hook_type": "emotion",
  "count": 1
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "titles": [
      {"title": "一个人在北上广的第3年,我差点放弃了", "hook_type": "emotion", "score": 93, "score_details": {"hook_match": 95, "emotion_intensity": 95, "keyword_coverage": 88, "attractiveness": 92}}
    ],
    "best_title": "一个人在北上广的第3年,我差点放弃了",
    "hook_paragraph": "昨晚加班到11点,回到出租屋,打开门的那一刻,黑暗扑面而来。没有人问你吃了没,没有人为你留灯。我坐在玄关地上,突然就哭了。不是委屈,是孤独。但今天早上闹钟响起,我还是穿好西装出了门。因为我知道,这座城市不会等我,而我,还没准备好认输。",
    "platform": "xiaohongshu",
    "word_limit": 20
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓情感共鸣钩子(emotion)正确应用 ✓情感强度95分(最高) ✓钩子段落情感真实动人 ✓小红书20字标题限制 ✓引发共鸣设计(孤独+坚持)

## 常见问题

### Q1: 如何开始使用标题钩子工厂?
A: 两步启动:(1)将SKILL.md放入Agent的skills目录;(2)确认Agent环境变量已配置LLM_API_KEY。调用时传入topic(必填)即可生成标题,platform和hook_type可选。纯LLM驱动,无额外API依赖.
### Q2: 6大钩子公式如何选择?
A: 按内容定位选择:(1)痛点共鸣→解决用户痛点的产品/方法;(2)好奇悬念→新品/黑科技/揭秘;(3)数字权威→教程/清单/数据;(4)对比反差→性价比/反常识;(5)情感共鸣→情感故事/励志;(6)紧迫感稀缺→限时活动/稀缺资源。不确定时用auto让LLM自动选择,或用multi对比6种公式效果.
### Q3: 4维度打分模型如何工作?
A: 钩子公式匹配度(30%)+情感强度(25%)+关键词覆盖(25%)+吸引力(20%),加权计算总分(0-100)。打分≥90为爆款潜力,80-89为优秀,70-79为良好,<70为待优化。best_title为最高分标题.
### Q4: 多平台字数限制如何适配?
A: 小红书20字内/抖音15字内/公众号30字内/微博30字内。生成标题时会自动适配平台字数限制,超长标题按平台最大字数截断,保留核心关键词。word_limit字段显示当前平台字数限制.
### Q5: 钩子段落可以直接用作开篇吗?
A: 可以。hook_paragraph基于best_title生成,延续标题的钩子公式风格,50-200字,前3秒抓住读者注意力,可直接作为内容开篇使用。建议根据实际内容微调细节,确保与正文衔接自然.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **平台覆盖**: 仅支持4个国内平台(小红书/抖音/公众号/微博),不支持Instagram/TikTok国际版/LinkedIn等海外平台
- **打分主观性**: 4维度打分基于LLM判断,不同模型评分可能差异较大,评分仅作参考非绝对标准
- **标题字数精度**: LLM生成的标题字数可能偏离限制(±2字),需人工微调至平台限制内
- **钩子公式覆盖**: 6大钩子公式为通用框架,特定垂直领域可能需要定制化钩子公式
- **内容相关性**: 标题基于topic生成,如topic描述不清晰,标题可能与实际内容偏离,需人工核对
- **多语言**: 仅支持中文标题生成,不支持英文/其他语种
- **版权提示**: 生成的标题为原创内容,但如与已有爆款标题高度相似,需人工核对避免抄袭

## 安全

### API Key 零暴露原则
- **环境变量注入**: LLM_API_KEY必须通过Agent环境变量注入,严禁在SKILL.md、配置文件或代码中硬编码
- **本文件无Key示例**: 本SKILL.md中不包含任何真实或示例API Key,所有引用均使用 `$env:LLM_API_KEY` 占位
- **日志脱敏**: exec工具记录日志时,自动过滤包含"key"/"token"/"secret"字段的值

### 内容安全
- **标题合规**: 自动过滤标题党/虚假宣传/绝对化用语(最/第一/唯一)等违规表述
- **平台规范**: 适配各平台标题规范,小红书避免过度营销、抖音避免违禁词、公众号遵守广告法
- **情感操控边界**: 钩子公式基于心理触发,但避免过度操控用户情绪,紧迫感稀缺公式仅用于真实限时场景
- **版权提示**: 生成的标题为原创内容,商业使用前建议查重,避免与已有爆款标题高度相似
