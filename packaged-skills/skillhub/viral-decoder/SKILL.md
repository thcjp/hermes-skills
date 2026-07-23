---
slug: viral-decoder
name: viral-decoder
version: "1.1.0"
displayName: "爆款拆解师"
summary: "把爆款拆成可复用配方,6大爆款要素+11维拆解+逐字逐句拆解,3秒生成拆解报告"
license: Proprietary
description: |-
  爆款拆解师是一款把爆款内容拆解成可复用创作配方的工具。基于6大爆款要素进行11维度逐字逐句拆解,
  生成量化评分、可复用配方模板和差异化创作建议,3秒生成拆解报告。

  核心能力:
  - 6大爆款要素拆解:钩子/情绪/价值/结构/节奏/CTA,逐要素分析爆款成功原因
  - 11维度逐字逐句拆解:标题/开篇/钩子/情绪曲线/价值点/结构框架/节奏/CTA/关键词/互动/平台适配
  - 量化评分模型:6维度评分(钩子吸引力/情绪强度/价值密度/结构清晰度/节奏控制/CTA转化),0-100分加权
  - 可复用配方生成:提取爆款可复用要素,生成创作配方模板,标注通用手法与平台特色
  - 差异化创作建议:基于拆解结果提供差异化角度,避免直接模仿,打造原创爆款
homepage: "https://skillhub.cn"
tags: [爆款拆解, 内容分析, 创作配方, 竞品研究]
tools:
  - read
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# 爆款拆解师 v1.1.0

把爆款内容拆解成可复用的创作配方,基于6大爆款要素进行11维度逐字逐句拆解,生成可复用配方和差异化创作建议。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

1. **6大爆款要素拆解**: 钩子(hook)/情绪(emotion)/价值(value)/结构(structure)/节奏(pacing)/CTA(call_to_action),逐要素分析爆款成功原因
2. **11维度逐字逐句拆解**: 标题/开篇/钩子/情绪曲线/价值点/结构框架/节奏控制/CTA/关键词/互动设计/平台适配,全方位拆解爆款逻辑
3. **量化评分模型**: 6维度评分(钩子吸引力/情绪强度/价值密度/结构清晰度/节奏控制/CTA转化),0-100分加权计算
4. **可复用配方生成**: 提取爆款的可复用要素,生成创作配方模板,指导后续内容创作
5. **差异化创作建议**: 基于拆解结果,提供差异化创作角度,避免直接模仿,打造原创爆款
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 爆款内容拆解 | content(爆款内容文本)+platform | decode_result(6要素+11维度拆解)+score+formula |
| 爆款配方提取 | content+platform | reusable_formula(可复用创作配方模板) |
| 竞品爆款分析 | competitor_content+own_positioning | 拆解报告+差异化创作建议 |
| 爆款评分对比 | content1+content2 | 两篇爆款的评分对比+优劣势分析 |
| 钩子/开篇专项拆解 | content+focus=hook | 钩子/开篇的逐字拆解+优化建议 |

**不适用于**: 非中文内容拆解(仅支持中文)、纯图片/视频内容拆解(需文本)、非爆款内容拆解(普通内容拆解价值有限)、学术文献分析(非内容创作场景)、新闻稿件分析(需专业新闻判断)。

## 使用流程

### Step 1: 环境准备
- 确认Agent已加载本SKILL.md,且支持exec工具
- 在Agent环境变量中配置 `LLM_API_KEY`(必需)
- 本Skill纯LLM驱动,无额外API依赖

### Step 2: 接收输入参数
- 必填: `content`(爆款内容文本)
- 选填: `platform`(发布平台)、`focus`(拆解重点,默认all)

### Step 3: 6大爆款要素拆解
- 钩子(hook): 开篇3秒抓注意力的手法
- 情绪(emotion): 情绪触发点和情绪曲线
- 价值(value): 提供给读者的价值点(信息/娱乐/情感/实用)
- 结构(structure): 内容组织框架(总分总/并列/递进等)
- 节奏(pacing): 信息密度和阅读节奏控制
- CTA(call_to_action): 转化引导话术

### Step 4: 11维度逐字逐句拆解
- 标题分析: 关键词/钩子公式/字数/吸引力
- 开篇分析: 前3秒钩子手法/痛点触发
- 钩子分析: 钩子类型/强度/位置
- 情绪曲线: 情绪触发点/情绪变化轨迹
- 价值点: 价值类型/价值密度/价值交付
- 结构框架: 内容组织方式/逻辑层次
- 节奏控制: 信息密度/段落长度/转折频率
- CTA分析: CTA类型/位置/话术
- 关键词: 核心关键词/长尾词/平台标签
- 互动设计: 互动引导/评论诱饵/分享触发
- 平台适配: 平台风格匹配度/字数适配

### Step 5: 量化评分
- 6维度评分:
  - 钩子吸引力(20%): 开篇抓注意力能力
  - 情绪强度(20%): 情绪触发和共鸣程度
  - 价值密度(20%): 单位字数的价值交付
  - 结构清晰度(15%): 内容组织逻辑性
  - 节奏控制(15%): 阅读节奏和信息密度
  - CTA转化(10%): 转化引导有效性
- 加权计算总分(0-100)

### Step 6: 可复用配方生成
- 提取爆款的可复用要素
- 生成创作配方模板(可填入新主题直接使用)
- 标注哪些要素是平台特色(不可复用),哪些是通用手法(可复用)

### Step 7: 差异化创作建议
- 基于拆解结果,提供差异化创作角度
- 避免直接模仿,打造原创爆款
- 建议改进点(哪里可以做得更好)

### Step 8: 输出拆解报告
- decode_result: 6要素+11维度拆解详情
- score: 量化评分+各维度分
- formula: 可复用创作配方
- suggestions: 差异化创作建议

## 输入格式

```json
{
  "content": "爆款内容全文...",
  "platform": "xiaohongshu",
  "focus": "all"
}
```

| 字段 | 类型 | 必填 | 说明 |
|:-----|:-----|:----:|:-----|
| content | string | 是 | 爆款内容全文 |
| platform | string | 否 | 发布平台: xiaohongshu/douyin/wechat/weibo/zhihu |
| focus | string | 否 | 拆解重点: all(全部,默认)/hook(钩子)/emotion(情绪)/structure(结构) |

## 输出格式

```json
{
  "success": true,
  "data": {
    "decode_result": {
      "elements": {
        "hook": {"type": "curiosity_suspense", "strength": 92, "analysis": "开篇用疑问句制造悬念..."},
        "emotion": {"type": "pain_resonance", "intensity": 88, "curve": "低开高走,中段共鸣峰值"},
        "value": {"type": "practical", "density": 85, "points": ["5个工具推荐", "实操步骤", "避坑指南"]},
        "structure": {"framework": "总分总", "clarity": 90, "analysis": "开头抛出问题,中间分点解答,结尾总结升华"},
        "pacing": {"rhythm": "快-慢-快", "control": 85, "analysis": "前3秒快节奏抓注意力,中段放慢详述,结尾快速收束"},
        "cta": {"type": "follow", "conversion": 80, "analysis": "结尾引导关注,话术自然不生硬"}
      },
      "dimensions": {
        "title": "标题分析...",
        "opening": "开篇分析...",
        "hook_detail": "钩子逐字拆解...",
        "emotion_curve": "情绪曲线分析...",
        "value_points": "价值点分析...",
        "structure_detail": "结构框架分析...",
        "pacing_detail": "节奏控制分析...",
        "cta_detail": "CTA分析...",
        "keywords": ["核心关键词1", "长尾词1"],
        "interaction": "互动设计分析...",
        "platform_fit": "平台适配分析..."
      }
    },
    "score": {
      "total": 88,
      "details": {
        "hook_attractiveness": 92,
        "emotion_intensity": 88,
        "value_density": 85,
        "structure_clarity": 90,
        "pacing_control": 85,
        "cta_conversion": 80
      }
    },
    "formula": {
      "name": "小红书种草爆款配方",
      "template": "疑问钩子+痛点共鸣+分点价值+总结升华+关注CTA",
      "reusable": ["疑问钩子", "分点价值", "总结升华"],
      "platform_specific": ["小红书emoji风格", "标签策略"]
    },
    "suggestions": [
      "差异化角度:可从反面切入,讲踩坑经历而非成功经验",
      "改进点:CTA可更自然,避免硬广感",
      "原创爆款:保留分点价值结构,替换为不同主题"
    ]
  },
  "error": null,
  "code": null
}
```

## 6大爆款要素说明

| 要素 | 英文标识 | 作用 | 拆解维度 |
|:-----|:---------|:-----|:---------|
| 钩子 | hook | 开篇3秒抓注意力 | 类型/强度/位置 |
| 情绪 | emotion | 触发情感共鸣 | 类型/强度/曲线 |
| 价值 | value | 提供读者价值 | 类型/密度/交付点 |
| 结构 | structure | 组织内容逻辑 | 框架/层次/清晰度 |
| 节奏 | pacing | 控制阅读节奏 | 信息密度/段落/转折 |
| CTA | call_to_action | 引导转化行动 | 类型/位置/话术 |

## 异常处理

| 异常场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| 内容为空 | 未提供content参数 | 返回success=false, error="内容不能为空" |
| 内容过短 | content<50字 | 返回success=false, error="内容过短,无法有效拆解(需≥50字)" |
| 内容过长 | content>10000字 | 截断保留前10000字,标注warning |
| 平台不支持 | platform不在支持范围内 | 降级为通用拆解,不针对平台优化,标注warning |
| focus无效 | focus不在支持范围内 | 默认使用all全维度拆解,标注warning |
| 要素拆解失败 | LLM分析异常 | 跳过该要素,继续拆解其他要素,标注warning |
| 维度拆解失败 | LLM分析异常 | 跳过该维度,继续拆解其他维度,标注warning |
| 评分异常 | LLM评分返回格式异常 | 使用默认评分(各维度80分),标注warning |
| 配方生成失败 | LLM生成异常 | 跳过配方生成,仅输出拆解和评分,标注warning |
| 差异化建议失败 | LLM生成异常 | 跳过差异化建议,仅输出拆解和评分,标注warning |
| LLM调用失败 | LLM服务不可用或超时 | 返回success=false, error="拆解LLM调用失败" |
| LLM_API_KEY未配置 | 环境变量缺失 | 返回error,提示配置环境变量 |

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
- **LLM_API_KEY**: 必需(通常由Agent内置) - 爆款拆解/要素提取/量化评分/配方生成
- **配置方式**: 必须通过Agent环境变量注入,严禁在SKILL.md或代码中硬编码API Key
- **安全检查**: 本SKILL.md中不包含任何API Key示例,所有Key均通过 `$env:LLM_API_KEY` 等环境变量读取

### 使用流程
纯LLM驱动,无额外依赖。拆解失败时跳过该要素/维度继续拆解。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 小红书种草爆款拆解

**输入**:
```json
{
  "content": "你绝对想不到这个AI工具这么好用!作为一个非程序员,我用了3天就做出了自己的小程序。今天分享5个超好用的AI编程工具,让你也能轻松上手,告别代码恐惧!\n\n1. Cursor:AI代码编辑器,支持自然语言编程\n2. GitHub Copilot:智能代码补全\n3. ChatGPT:全能AI助手\n4. Claude:长文本理解强\n5. v0:UI生成神器\n\n每个工具我都实测过,真的太好用了!赶紧试试吧~\n\n#AI编程 #效率工具 #副业赚钱",
  "platform": "xiaohongshu"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "decode_result": {
      "elements": {
        "hook": {"type": "curiosity_suspense", "strength": 92, "analysis": "开篇用'你绝对想不到'制造悬念,引发好奇"},
        "emotion": {"type": "pain_resonance", "intensity": 85, "curve": "痛点(代码恐惧)→共鸣(非程序员)→解决(5个工具)"},
        "value": {"type": "practical", "density": 88, "points": ["5个工具推荐", "实测体验", "适用人群"]},
        "structure": {"framework": "总分总", "clarity": 90, "analysis": "钩子开头→分点列举→总结引导"},
        "pacing": {"rhythm": "快-慢-快", "control": 85, "analysis": "前3秒快速抓注意力,中段分点详述,结尾快速收束"},
        "cta": {"type": "follow", "conversion": 80, "analysis": "结尾'赶紧试试吧'自然引导,无硬广感"}
      },
      "dimensions": {
        "title": "无独立标题,开篇第一句承担标题功能",
        "opening": "疑问句+'你绝对想不到'制造悬念,3秒内抓住注意力",
        "hook_detail": "钩子类型:好奇悬念;位置:开篇第一句;强度:92分",
        "emotion_curve": "情绪曲线:低开(痛点)→高走(解决方案)→平稳(工具列举)→上升(CTA)",
        "value_points": "价值类型:实用型;价值密度:88分;交付点:5个工具+实测体验",
        "structure_detail": "结构:总分总;层次:钩子→背景→分点→总结;清晰度:90分",
        "pacing_detail": "节奏:快-慢-快;信息密度:中段最高;段落:短段落便于阅读",
        "cta_detail": "CTA类型:关注引导;位置:结尾;话术:'赶紧试试吧~'",
        "keywords": ["AI编程", "效率工具", "副业赚钱", "Cursor", "Copilot"],
        "interaction": "互动设计:评论区可问工具选择;分享触发:实用价值高",
        "platform_fit": "平台适配:小红书风格(emoji+标签+短段落),适配度90分"
      }
    },
    "score": {
      "total": 88,
      "details": {
        "hook_attractiveness": 92,
        "emotion_intensity": 85,
        "value_density": 88,
        "structure_clarity": 90,
        "pacing_control": 85,
        "cta_conversion": 80
      }
    },
    "formula": {
      "name": "小红书种草爆款配方",
      "template": "好奇钩子+痛点共鸣+分点价值+总结引导+关注CTA",
      "reusable": ["好奇钩子", "分点价值", "总结引导"],
      "platform_specific": ["小红书emoji风格", "标签策略", "短段落"]
    },
    "suggestions": [
      "差异化角度:可从踩坑经历切入,讲用错工具的教训,反向种草",
      "改进点:CTA可增加互动诱饵,如'评论区告诉我你用哪个'",
      "原创爆款:保留分点价值结构,替换为不同主题(如AI写作工具)"
    ]
  },
  "error": null,
  "code": null
}
```

### 示例2: 抖音口播爆款拆解

**输入**:
```json
{
  "content": "月入3万的副业,居然只需要一部手机?今天告诉你3个手机就能做的副业...\n\n第一,短视频带货:拍视频挂链接,有人买就有佣金\n第二,知识付费:把你的技能做成课程,一次制作反复售卖\n第三,社群运营:建群分享价值,收会员费\n\n这3个副业我都做过,真的能赚钱!想知道具体怎么操作?关注我,下期详细讲!",
  "platform": "douyin"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "decode_result": {
      "elements": {
        "hook": {"type": "curiosity_suspense", "strength": 95, "analysis": "'月入3万'+'一部手机'制造强反差悬念"},
        "emotion": {"type": "aspiration", "intensity": 90, "curve": "好奇→渴望→行动"},
        "value": {"type": "practical", "density": 85, "points": ["3个副业项目", "操作门槛", "变现方式"]},
        "structure": {"framework": "总分总", "clarity": 88, "analysis": "悬念开头→分点列举→关注引导"},
        "pacing": {"rhythm": "快-快-快", "control": 88, "analysis": "全程快节奏,适合短视频15秒内抓注意力"},
        "cta": {"type": "follow", "conversion": 92, "analysis": "'关注我,下期详细讲'制造期待,转化强"}
      },
      "dimensions": {
        "title": "无独立标题,开篇承担标题功能",
        "opening": "数字+反差制造强悬念,15秒内抓住注意力",
        "hook_detail": "钩子类型:好奇悬念+数字权威;位置:开篇;强度:95分",
        "emotion_curve": "情绪曲线:好奇(月入3万)→渴望(一部手机)→行动(3个副业)→期待(下期)",
        "value_points": "价值类型:实用型;价值密度:85分;交付点:3个副业+操作方式",
        "structure_detail": "结构:总分总;层次:悬念→分点→引导;清晰度:88分",
        "pacing_detail": "节奏:全程快节奏;信息密度:高;段落:口语化短句",
        "cta_detail": "CTA类型:关注引导;位置:结尾;话术:'关注我,下期详细讲'",
        "keywords": ["副业", "月入3万", "手机副业", "短视频带货", "知识付费"],
        "interaction": "互动设计:下期预告制造期待;分享触发:副业话题高分享率",
        "platform_fit": "平台适配:抖音口语化风格,适配度92分"
      }
    },
    "score": {
      "total": 90,
      "details": {
        "hook_attractiveness": 95,
        "emotion_intensity": 90,
        "value_density": 85,
        "structure_clarity": 88,
        "pacing_control": 88,
        "cta_conversion": 92
      }
    },
    "formula": {
      "name": "抖音口播爆款配方",
      "template": "数字反差钩子+分点价值+下期预告CTA",
      "reusable": ["数字反差钩子", "分点价值", "下期预告CTA"],
      "platform_specific": ["抖音口语化", "快节奏", "15秒内抓注意力"]
    },
    "suggestions": [
      "差异化角度:可从失败经历切入,讲3个赔钱的副业,反向避坑",
      "改进点:可增加数据佐证,如'我第1个月赚了XX'",
      "原创爆款:保留数字反差钩子,替换为不同主题(如AI工具)"
    ]
  },
  "error": null,
  "code": null
}
```

### 示例3: 公众号深度内容拆解

**输入**:
```json
{
  "content": "AI会取代程序员吗?这个问题我问了100个程序员...\n\n有人说会,有人说不会。但真正的答案是:AI不会取代程序员,但会用AI的程序员会取代不用AI的程序员。\n\n我采访了100个程序员,发现一个规律:月薪3万以上的,都在用AI提效;月薪1万以下的,还在抗拒AI。\n\n这不是巧合。AI时代,工具决定效率,效率决定收入。\n\n如果你想提升竞争力,我建议从这3个AI工具开始...\n\n(后续内容省略)",
  "platform": "wechat"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "decode_result": {
      "elements": {
        "hook": {"type": "number_authority", "strength": 88, "analysis": "'问了100个程序员'用数字增强可信度和好奇心"},
        "emotion": {"type": "anxiety_relief", "intensity": 85, "curve": "焦虑(被取代)→缓解(真相)→行动(建议)"},
        "value": {"type": "insight", "density": 82, "points": ["行业真相", "数据规律", "行动建议"]},
        "structure": {"framework": "悬念-解答-深化", "clarity": 85, "analysis": "抛出问题→给出答案→数据佐证→行动建议"},
        "pacing": {"rhythm": "慢-快-慢", "control": 82, "analysis": "开头慢节奏制造悬念,中段快速给数据,结尾慢节奏建议"},
        "cta": {"type": "read_more", "conversion": 78, "analysis": "引导继续阅读,留存读者"}
      }
    },
    "score": {
      "total": 84,
      "details": {
        "hook_attractiveness": 88,
        "emotion_intensity": 85,
        "value_density": 82,
        "structure_clarity": 85,
        "pacing_control": 82,
        "cta_conversion": 78
      }
    },
    "formula": {
      "name": "公众号深度内容配方",
      "template": "数字钩子+反转答案+数据佐证+行动建议",
      "reusable": ["数字钩子", "反转答案", "数据佐证"],
      "platform_specific": ["公众号长文风格", "深度分析"]
    },
    "suggestions": [
      "差异化角度:可从非程序员视角切入,讲AI对普通人的影响",
      "改进点:CTA可更强,如引导关注或转发",
      "原创爆款:保留数字钩子+反转结构,替换为不同主题"
    ]
  },
  "error": null,
  "code": null
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 小红书种草爆款拆解(6要素+11维度全拆解)

**输入**:
```json
{
  "content": "姐妹们!这个平价面霜绝了!才59元,用了一周皮肤细腻到发光!之前花300多买的大牌面霜都没这效果,真的是越贵的不一定越好!我是混干皮,之前换季起皮特别严重,用了这个之后完全不起了!成分里有烟酰胺+玻尿酸,保湿提亮一步到位!用法:早晚洁面后取黄豆大小,先手心搓热再按压上脸,吸收超快不黏腻!真心建议预算有限的姐妹试试,不好用你来找我!#平价护肤 #面霜推荐 #烟酰胺 #学生党护肤",
  "platform": "xiaohongshu",
  "focus": "all"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "decode_result": {
      "elements": {
        "hook": {"type": "pain_resonance+curiosity_suspense", "strength": 92, "analysis": "开篇'姐妹们!这个平价面霜绝了!'双重钩子:情绪共鸣(姐妹们)+好奇悬念(绝了),3秒内抓住注意力"},
        "emotion": {"type": "惊喜+信任", "intensity": 88, "curve": "低开高走:惊讶(绝了)→对比(300vs59)→共鸣(混干皮)→信任(成分分析)→行动(不好用找我)"},
        "value": {"type": "practical", "density": 90, "points": ["价格对比(59vs300)", "肤质适配(混干皮)", "成分解析(烟酰胺+玻尿酸)", "使用方法(搓热按压)", "效果验证(一周细腻发光)"]},
        "structure": {"framework": "钩子-痛点-产品-方法-CTA", "clarity": 88, "analysis": "开头钩子→痛点(换季起皮)→产品介绍→成分解析→使用方法→信任承诺,逻辑清晰"},
        "pacing": {"rhythm": "快-慢-快", "control": 85, "analysis": "前3秒快节奏(绝了!)→中段放慢(成分+用法详述)→结尾快速收束(不好用找我!)"},
        "cta": {"type": "trust_guarantee", "conversion": 90, "analysis": "'不好用你来找我'信任承诺式CTA,降低决策门槛,转化率极高"}
      },
      "dimensions": {
        "title": "无独立标题,首句即标题:姐妹们!这个平价面霜绝了!——情绪+悬念双重钩子",
        "opening": "前3秒:姐妹们!+绝了!+59元——情绪词+悬念词+价格锚点,3秒内传递3个关键信息",
        "hook_detail": "'姐妹们'(群体归属)→'绝了'(情绪夸张)→'才59元'(价格锚点)——逐字拆解:每个词都有功能,无废字",
        "emotion_curve": "惊讶(绝了)→对比(300vs59)→痛点共鸣(换季起皮)→信任(成分)→行动(找我)——五段式情绪递进",
        "value_points": "5个价值点:价格/肤质/成分/用法/效果——每点都用具体数据或感受支撑,无空话",
        "structure_detail": "钩子→痛点→产品→成分→方法→CTA——六步式种草结构,小红书标准爆款框架",
        "pacing_detail": "感叹号5个/问号0个/段落1段——信息密度高,适合手机快速阅读",
        "cta_detail": "信任承诺型CTA:'不好用你来找我'——零风险承诺,转化心理学经典手法",
        "keywords": ["平价护肤", "面霜推荐", "烟酰胺", "学生党护肤", "混干皮", "保湿提亮", "59元面霜", "平价面霜"],
        "interaction": "4个话题标签+评论区承诺(找我)——引导互动+话题流量双重设计",
        "platform_fit": "小红书满分适配:口语化+emoji感+话题标签+种草风格——100%符合平台调性"
      }
    },
    "score": {
      "total": 88,
      "details": {
        "hook_attractiveness": 92,
        "emotion_intensity": 88,
        "value_density": 90,
        "structure_clarity": 88,
        "pacing_control": 85,
        "cta_conversion": 90
      }
    },
    "formula": {
      "name": "小红书平价种草爆款配方",
      "template": "情绪钩子(姐妹们+绝了)+价格锚点(XX元)+痛点共鸣(肤质问题)+成分背书+使用方法+信任承诺CTA",
      "reusable": ["情绪钩子结构", "价格锚点对比", "成分背书模式", "信任承诺CTA"],
      "platform_specific": ["小红书话题标签策略", "口语化种草语气", "单段式排版"]
    },
    "suggestions": [
      "差异化角度:可做'59元vs590元面霜28天实测对比',用对比实验增强可信度",
      "改进点:缺少使用前后对比图引导,可在CTA前增加'看评论区放对比图'",
      "原创爆款:保留信任承诺CTA+价格锚点结构,替换为不同品类(如平价精华/平价防晒)"
    ]
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓6大爆款要素完整拆解(钩子/情绪/价值/结构/节奏/CTA) ✓11维度逐字逐句拆解 ✓6维度评分(总分88分) ✓可复用配方提取(4个通用要素) ✓差异化创作建议3条

### 案例2: 钩子专项拆解(focus=hook,逐字拆解)

**输入**:
```json
{
  "content": "我月薪3千的时候,从来不买超过50块的护肤品。直到有一天,闺蜜递给我一瓶59元的面霜说:你试试。一周后,我把柜子里300多的大牌全扔了...",
  "platform": "xiaohongshu",
  "focus": "hook"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "decode_result": {
      "elements": {
        "hook": {"type": "story+contrast+curiosity_suspense", "strength": 95, "analysis": "三重钩子叠加:故事钩子(月薪3千)+对比钩子(59vs300)+悬念钩子(全扔了),开篇即高潮"}
      },
      "dimensions": {
        "opening": "前3秒:'我月薪3千的时候'——身份代入+收入锚点,精准锁定目标人群(平价护肤受众)",
        "hook_detail": "逐字拆解:\n• '我月薪3千'——身份代入(目标人群秒共鸣)\n• '从来不买超过50块'——消费习惯锚点(建立平价人设)\n• '直到有一天'——转折悬念(好奇心触发)\n• '闺蜜递给我一瓶59元的面霜'——具体产品+价格(信息交付)\n• '说:你试试'——极简推荐语(降低推销感)\n• '一周后'——时间锚点(效果验证周期)\n• '柜子里300多的大牌全扔了'——极端对比+行为转变(震撼收尾)\n\n钩子强度分析:每个短句都承载一个功能(代入/锚点/悬念/交付/验证/震撼),零废字,信息密度极高",
        "emotion_curve": "共鸣(月薪3千)→认同(不买贵的)→好奇(直到有一天)→信任(闺蜜推荐)→震撼(全扔了)——五段情绪递进,3秒内完成",
        "keywords": ["月薪3千", "50块", "59元面霜", "大牌", "闺蜜推荐"],
        "platform_fit": "小红书故事型钩子,适配种草场景,前3秒完播率预估95%+"
      }
    },
    "score": {
      "total": 92,
      "details": {
        "hook_attractiveness": 95,
        "emotion_intensity": 90,
        "value_density": 85,
        "structure_clarity": 90,
        "pacing_control": 92,
        "cta_conversion": 80
      }
    },
    "formula": {
      "name": "故事型三重钩子配方",
      "template": "身份代入(月薪XX)+消费锚点(不买超过XX)+转折悬念(直到有一天)+产品交付(XX元XX)+行为转变(全扔了)",
      "reusable": ["身份代入+消费锚点开头", '转折悬念结构(直到)', "极端对比收尾(全扔了)"],
      "platform_specific": ["小红书故事型种草语气"]
    },
    "suggestions": [
      "钩子优化:可在'全扔了'后增加'别急,听我说完'防止读者误以为是广告而跳出",
      "差异化角度:可替换身份(如'身为两个孩子的妈妈')切入不同人群",
      "原创爆款:保留三重钩子结构(身份+锚点+转折),替换为不同品类"
    ]
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓钩子专项拆解(focus=hook)正确执行 ✓逐字逐句拆解(7个短句逐一分析) ✓三重钩子叠加识别(故事+对比+悬念) ✓钩子吸引力95分(极高) ✓可复用配方提取(3个通用钩子手法)

### 案例3: 竞品爆款对比分析(2篇内容评分对比)

**输入**:
```json
{
  "content": "姐妹们!这个平价面霜绝了!才59元,用了一周皮肤细腻到发光!成分里有烟酰胺+玻尿酸,保湿提亮一步到位!不好用你来找我!",
  "platform": "xiaohongshu",
  "focus": "all"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "decode_result": {
      "elements": {
        "hook": {"type": "pain_resonance+curiosity_suspense", "strength": 92, "analysis": "情绪+悬念双重钩子"},
        "emotion": {"type": "惊喜+信任", "intensity": 88, "curve": "惊讶→对比→信任→行动"},
        "value": {"type": "practical", "density": 85, "points": ["价格59元", "成分烟酰胺+玻尿酸", "效果一周发光"]},
        "structure": {"framework": "钩子-产品-成分-CTA", "clarity": 85, "analysis": "简洁四步式,适合短图文"},
        "pacing": {"rhythm": "快", "control": 80, "analysis": "全篇快节奏,信息密度高但篇幅较短"},
        "cta": {"type": "trust_guarantee", "conversion": 90, "analysis": "信任承诺式CTA效果极强"}
      },
      "dimensions": {
        "title": "无独立标题,首句即钩子",
        "opening": "姐妹们!+绝了!+59元——3秒3信息",
        "hook_detail": "情绪词+悬念词+价格锚点,三重钩子",
        "emotion_curve": "惊讶→信任→行动,快速递进",
        "value_points": "3个价值点:价格/成分/效果",
        "structure_detail": "钩子→产品→成分→CTA,四步式",
        "pacing_detail": "感叹号4个,快节奏",
        "cta_detail": "信任承诺:'不好用你来找我'",
        "keywords": ["平价面霜", "59元", "烟酰胺", "玻尿酸"],
        "interaction": "话题标签+评论区承诺",
        "platform_fit": "小红书种草风格,适配度高"
      }
    },
    "score": {
      "total": 85,
      "details": {
        "hook_attractiveness": 92,
        "emotion_intensity": 88,
        "value_density": 85,
        "structure_clarity": 85,
        "pacing_control": 80,
        "cta_conversion": 90
      }
    },
    "formula": {
      "name": "小红书简短种草配方",
      "template": "情绪钩子+价格+成分+信任CTA",
      "reusable": ["情绪钩子", "信任CTA"],
      "platform_specific": ["小红书种草语气"]
    },
    "suggestions": [
      "本篇为简短版,与案例1(完整版)对比:完整版评分88分>简短版85分",
      "差异分析:简短版缺少痛点共鸣(肤质问题)和使用方法,价值密度略低",
      "建议:在保持简洁的同时,增加1句痛点描述(如'混干皮换季必入')可提升3-5分"
    ]
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓6要素+11维度拆解完整 ✓6维度评分(总分85分) ✓与案例1对比分析(88分vs85分) ✓差异分析清晰(缺痛点/方法) ✓优化建议(增加痛点描述+3-5分)

### 案例4: 内容过短异常处理(<50字)

**输入**:
```json
{
  "content": "这个面霜很好用,推荐大家买。",
  "platform": "xiaohongshu",
  "focus": "all"
}
```

**LLM生成输出**:
```json
{
  "success": false,
  "data": null,
  "error": "内容过短,无法有效拆解(需≥50字)。当前内容仅14字,缺少钩子/情绪/价值/结构等爆款要素,拆解价值有限。建议提供至少50字的完整内容。",
  "code": "CONTENT_TOO_SHORT"
}
```

**效果验证**: ✓内容过短正确检测(14字<50字) ✓错误原因清晰描述 ✓字数对比展示(14字vs50字) ✓错误码CONTENT_TOO_SHORT正确返回 ✓不执行拆解(避免无效输出)

## 常见问题

### Q1: 如何开始使用爆款拆解师?
A: 两步启动:(1)将SKILL.md放入Agent的skills目录;(2)确认Agent环境变量已配置LLM_API_KEY。调用时传入content(必填,爆款内容全文)即可拆解,platform和focus可选。纯LLM驱动,无额外API依赖。

### Q2: 6大爆款要素分别拆解什么?
A: (1)钩子→开篇3秒抓注意力的手法;(2)情绪→情绪触发点和情绪曲线;(3)价值→提供给读者的价值点;(4)结构→内容组织框架;(5)节奏→信息密度和阅读节奏;(6)CTA→转化引导话术。每个要素都会分析类型/强度/位置等维度。

### Q3: 11维度拆解和6要素拆解有什么区别?
A: 6要素拆解是横向分析(从6个爆款要素角度),11维度拆解是纵向分析(从标题/开篇/钩子/情绪曲线等11个具体维度逐字逐句拆解)。两者互补,6要素提供宏观视角,11维度提供微观细节。

### Q4: 可复用配方如何使用?
A: formula字段提取爆款的可复用要素,生成创作配方模板:(1)reusable标注哪些要素可跨主题复用;(2)platform_specific标注哪些是平台特色不可复用;(3)template提供配方结构。使用时保留reusable要素,替换主题内容,适配平台特色。

### Q5: 拆解结果可以用于直接模仿吗?
A: 不建议直接模仿。suggestions字段提供差异化创作建议,帮助你在拆解基础上创新:(1)差异化角度(从反面/不同视角切入);(2)改进点(哪里可以做得更好);(3)原创爆款(保留结构替换主题)。目标是学习爆款逻辑,打造原创内容。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **语言限制**: 仅支持中文内容拆解,不支持英文/其他语种
- **内容类型**: 仅支持文本内容拆解,纯图片/视频内容需先转为文本(如视频字幕)
- **内容长度**: 建议50-10000字,过短无法有效拆解,过长会截断
- **评分主观性**: 6维度评分基于LLM判断,不同模型评分可能差异较大,评分仅作参考
- **平台覆盖**: 主要支持国内5平台(小红书/抖音/公众号/微博/知乎),海外平台适配度可能降低
- **配方通用性**: 可复用配方基于单篇爆款提取,可能不完全适用于所有同类内容
- **差异化建议**: 建议基于LLM理解,可能与实际创作需求有偏差,需人工判断

## 安全

### API Key 零暴露原则
- **环境变量注入**: LLM_API_KEY必须通过Agent环境变量注入,严禁在SKILL.md、配置文件或代码中硬编码
- **本文件无Key示例**: 本SKILL.md中不包含任何真实或示例API Key,所有引用均使用 `$env:LLM_API_KEY` 占位
- **日志脱敏**: exec工具记录日志时,自动过滤包含"key"/"token"/"secret"字段的值

### 内容安全
- **版权尊重**: 拆解的爆款内容需为公开可访问内容,拆解结果用于学习参考,不建议直接抄袭
- **差异化创作**: 系统主动提供差异化建议,鼓励原创而非模仿,避免版权纠纷
- **配方使用边界**: 可复用配方为创作框架,非具体内容,使用者需自行创作原创内容
- **竞品分析合规**: 竞品拆解仅用于学习参考,不用于恶意竞争或贬低竞品
- **数据隐私**: 拆解内容不包含个人隐私信息,如意外包含会自动脱敏处理
