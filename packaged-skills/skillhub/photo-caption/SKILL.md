---
slug: "photo-caption"
name: "photo-caption"
version: "1.0.0"
displayName: "照片配文工具专业版"
summary: "全平台照片配文生成工具,支持13个社交平台,提供批量配文、品牌风格定制与编辑分析能力。"
license: "Proprietary"
edition: "pro"
description: |-
  照片配文工具专业版,面向专业摄影师与内容创作者提供 13 个社交平台的配文生成能力,支持批量处理、品牌风格定制与照片编辑分析。核心能力:
  - 13 个平台全覆盖(Instagram/Flickr/X/Glass/Tumblr/Bluesky/Threads/500px/Reddit/Facebook/VSCO/Substack/Pinterest)
  - 批量照片配文生成
  - 品牌风格与语气定制
  - 照片编辑分析(配合 photo-edit-analysis)
  - 多语言配文支持
  - 平台原生格式严格适配

  适用场景:
tags:
  - 沟通协作
  - 社交媒体
  - 内容创作
  - 摄影配文
  - 专业效率
  - 品牌管理
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# 照片配文工具专业版

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

### 一、13 个平台全覆盖(专业版独有 10 个平台)
每个平台拥有独立的语气、格式与标签策略:

| 平台 | 语气风格 | 格式特点 | 标签策略 |
|:-----|:---------|:---------|:---------|
| Instagram | 简洁、具体、观察式 | 1-2行+器材+5标签 | 精选5个高质量标签 |
| Flickr | 描述性、沉思感 | 标题+1-3句+器材 | 无标签限制 |
| X (Twitter) | 简练、有冲击力 | 280字符以内 | 不堆砌标签 |
| Glass | 摄影师间对话 | 1-3句+器材(中点分隔) | 无标签 |
| Tumblr | 文学性、表达感 | 粗体地点+2-4句+标签 | 8-12个带空格标签 |
| Bluesky | 对话感、温暖 | 1-2句,300字符以内 | 极少或不使用标签 |
| Threads | 随性、对话式 | 1-2句+话题建议 | 无标签 |
| 500px | 技术性、工艺感 | 标题+1-3句+完整器材 | 无标签 |
| Reddit | 真实、社区友好 | 标题+评论+子版块 | 无标签 |
| Facebook | 个人化、叙事感 | 2-3句随性分享 | 0-2个标签 |
| VSCO | 极简、诗意 | 1行以内 | 无标签 |
| Substack | 叙事性、散文感 | 2-4句内嵌配文 | 无标签 |
| Pinterest | 描述性、可搜索 | 标题+描述(SEO优化) | 关键词替代标签 |

**输入**: 用户提供一、13 个平台全覆盖(专业版独有 10 个平台)所需的指令和必要参数。
**输出**: 返回一、13 个平台全覆盖(专业版独有 10 个平台)的执行结果,包含操作状态和输出数据。### 二、批量配文生成(专业版独有)
- 一组照片一次性生成全部平台配文
- 支持系列作品统一风格
- 批量导出配文清单
- 按平台分组输出

**输入**: 用户提供二、批量配文生成(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行二、批量配文生成(专业版独有)操作,遵循单一意图原则。### 三、品牌风格定制(专业版独有)
- 自定义语气风格(如品牌调性:专业/活泼/文艺)
- 自定义标签策略
- 保存品牌风格配置
- 多品牌快速切换

**输入**: 用户提供三、品牌风格定制(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行三、品牌风格定制(专业版独有)操作,遵循单一意图原则。### 四、编辑分析(专业版独有)
- 配合 `photo-edit-analysis` 技能
- 分析照片构图、曝光、色彩
- 提供编辑改进建议
- 作为独立章节输出

### 五、多语言完整支持(专业版独有)
- 中英文配文自由切换
- 平台语言习惯适配
- 地点相关的语言选择
- 多语言批量生成

**输入**: 用户提供五、多语言完整支持(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行五、多语言完整支持(专业版独有)操作,遵循单一意图原则。
### Instagram

执行Instagram,自动处理参数解析、任务调度和结果格式化,返回结构化输出。

**输入**: 用户提供Instagram相关的配置参数、输入数据和处理选项。

**输出**: 返回Instagram的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`Instagram`相关配置参数进行设置
#
## 适用场景

### 场景一:专业摄影师全平台作品发布
摄影师完成一组作品后,需同时在 13 个平台发布,每个平台配文风格各异。

**输入信息**:

```text
照片内容:沙漠公路日落,光影层次丰富
地点:Amboy, California
器材:Canon EOS 1V, Tri-X 400(胶片)
氛围:孤独、辽阔、美式公路感
拍摄方式:胶片
语言:英文
```

**13 个平台配文生成结果**:

**Instagram**:

```text
The road ends where the sky turns orange. Dust and heat in the air.

Canon EOS 1V · Tri-X 400

```

**Flickr**:

```text
Desert Road at Dusk, Amboy California
Shot on a stretch of Route 66 where the road goes straight into the horizon. The light changed fast, maybe ten minutes from flat to this. Tri-X 400 handled the grain the way I wanted, dry and a little rough.
Canon EOS 1V · Tri-X 400
```

**X (Twitter)**:

```text
Caught this sunset in Amboy. The road looks like it leads to another world. Tri-X 400 got that dry, wide-open feeling exactly right.
```

**Glass**:

```text
Somewhere on Route 66 near Amboy. The light dropped fast and the road just kept going.
Canon EOS 1V · Tri-X 400
```

**Tumblr**:

```text
**Amboy, California**

Drove out to the desert to clear my head and the sky did this thing where it just kept getting more intense. Ten minutes of light worth sitting in the dust for. The Tri-X grain feels right for a place this dry and quiet.

#film photography #desert #route 66 #mojave #analog photography #road trip #canon eos 1v #tri x 400 #american west #sunset
```

**Bluesky**:

```text
Drove out to Amboy for the sunset. The road goes straight into the horizon and the light changes fast out there. Tri-X 400 was the right call.
```

**Threads**:

```text
Desert sunsets hit different when you're standing in the middle of nowhere.
Topic: Desert Photography
```

**500px**:

```text
Desert Road at Dusk
Shot on Route 66 near Amboy, California. The light dropped fast, maybe a ten minute window from flat to this. Exposed for the highlights and let the shadows go dark. Tri-X 400 at box speed, developed in HC-110.
Camera: Canon EOS 1V · Lens: 50mm · Film: Tri-X 400
```

**Reddit**:

```text
Title: Desert road at dusk, Amboy California [Canon EOS 1V, Tri-X 400]

Comment: Shot this on Route 66 last weekend. The light changed fast, maybe a ten minute window. Tri-X 400 at box speed, developed in HC-110. The desert just keeps going out there.
Posted to r/analog
```

**Facebook**:

```text
Drove out to Amboy last weekend to shoot the sunset. The desert is so quiet out there, just dust and road and sky. The light only lasted about ten minutes but it was worth the drive.
```

**VSCO**:

```text
desert dusk
```

**Substack**:

```text
I drove out to Amboy on a Sunday, mostly to get out of the city. The desert does this thing where the light drops fast and everything changes in about ten minutes. I shot it on Tri-X because the grain felt right for how dry and quiet it was out there. The road just goes straight into the horizon and you stop thinking about anything else.
```

**Pinterest**:

```text
Title: Desert Road at Dusk, Amboy California
Description: A film photograph of a desert road at sunset near Amboy, California. Shot on Tri-X 400 with a Canon EOS 1V. The muted tones and grain capture the dry, wide-open feeling of the Mojave Desert. Perfect for desert aesthetic, Route 66 road trip inspiration, and analog landscape photography.
```

**编辑分析(独立章节)**:

```text
Edit Analysis:
- 构图:低地平线构图,天空占画面2/3,突出光影层次
- 曝光:高光区域略有过曝,建议下次减半档曝光
- 色彩:Tri-X 400 的颗粒感与沙漠干燥氛围契合
- 改进建议:可尝试增加前景元素(如路标)增强纵深感
```

### 场景二:批量生成系列作品配文
摄影师完成一个城市街拍系列(5张照片),需批量生成配文。

```text
请为以下5张照片批量生成 Instagram 配文,保持系列风格统一:

照片1:武康路梧桐树下光影,Leica M6, Portra 400
照片2:外滩夜景反光,Leica M6, Portra 400
照片3:弄堂里老人下棋,Leica M6, Portra 400
照片4:雨后街道水洼倒影,Leica M6, Portra 400
照片5:咖啡馆窗边阅读的人,Leica M6, Portra 400

系列主题:上海日常
统一风格:安静、观察式、不煽情
```

### 场景三:品牌风格定制配文
品牌需为产品摄影配文,要求统一品牌语气。

```text
品牌配置:
品牌名:ANALOG CO.
品牌语气:克制、专业、不卖弄
禁用词:amazing, stunning, perfect
标签策略:固定使用 #analogco #filmlife,其余按内容选2个
语言:中英双语

请为以下产品照生成配文:
照片内容:皮质相机包放在木桌上,自然光
器材: Hasselblad 500C/M, Kodak Portra 160
```

## 使用流程

### 优秀步:提供照片信息
```text
照片内容: [详细描述]
地点: [拍摄地点]
器材: [相机/镜头/胶片]
氛围: [情绪/感觉]
拍摄方式: [胶片/数码]
语言: [中文/英文/双语]
```

### 第二步:指定目标平台
```text
请为这张照片生成所有平台的配文。

请为这张照片生成 Instagram、Flickr、500px、Reddit 的配文。
```

### 第三步:获取配文与编辑分析
工具会一次性返回所有指定平台的配文,并在末尾附上编辑分析章节。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | photo-caption处理的内容输入 |,  |
| content | string | 否 | photo-caption处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "caption 相关配置参数",
    result: "caption 相关配置参数",
    result: "caption 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **网络环境**: 无特殊网络要求(纯文本生成)

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| photo-edit-analysis | 技能 | 推荐 | 随 Skill 安装(编辑分析功能) |

### API Key 配置
- 本 Skill 基于自然语言指令驱动,无需额外 API Key
- 配文生成完全依赖 Agent 内置 LLM 能力,不调用外部图片识别或文案 API
- 编辑分析功能依赖 `photo-edit-analysis` 技能,同样无需额外 API Key

### 可用性分类
- **分类**: MD(纯 Markdown 指令,无需 exec 命令行执行能力)
- **说明**: 基于自然语言的 AI Skill,通过指令驱动 Agent 为照片生成 13 个社交平台适配的配文内容。专业版完全兼容免费版三大平台配文能力,额外解锁 Flickr、Glass、Tumblr、Bluesky、Threads、500px、Reddit、VSCO、Substack、Pinterest 共 10 个专业平台,并提供批量配文生成、品牌风格定制与照片编辑分析能力,适合专业摄影师与内容创作者的规模化内容生产。

## 案例展示

### 品牌风格配置
```yaml
brand:
  name: "ANALOG CO."
  tone: "克制、专业、不卖弄"
  voice: "像和一个懂行的朋友聊天,不卖弄术语"
  banned_words:
    - "amazing"
    - "stunning"
    - "perfect"
    - "captured"
    - "timeless"
  fixed_hashtags:
    - "#analogco"
    - "#filmlife"
  hashtag_count: 5          # 固定5个标签(含2个品牌标签)
  language: "bilingual"     # 中英双语
  gear_format: "full"       # 完整器材信息
```

### 批量配文输入模板
```text
系列主题: [系列名称]
统一风格: [风格描述]
平台: [目标平台,如 Instagram]

照片1:
  内容: [描述]
  地点: [地点]
  器材: [器材]
  氛围: [氛围]

照片2:
  内容: [描述]
  地点: [地点]
  器材: [器材]
  氛围: [氛围]

[更多照片...]
```

### 平台格式规范参考
```text
Instagram:
  - 1-2行正文
  - 空行
  - 器材行(如有)
  - 空行
  - 恰好5个标签
  - 禁止使用破折号(—)

Flickr:
  - 标题(纯文本,无markdown)
  - 破折号
  - 1-3句故事/背景
  - 器材信息

X (Twitter):
  - 280字符以内
  - 单行强表达
  - 器材自然融入末尾

Glass:
  - 1-3句
  - 器材单独一行,用中点(·)分隔
  - 无标签,无互动诱饵

Tumblr:
  - 粗体地点作为标题
  - 2-4句叙事/反思
  - 器材行
  - 8-12个标签(标签内用空格)

500px:
  - 标题行
  - 1-3句技术/条件描述
  - 完整器材细节

VSCO:
  - 最多1行
  - 有时只需一个词或短语
  - 无标签,无器材(除非胶片型号)

Pinterest:
  - 标题(5-10词,关键词丰富)
  - 描述(2-3句,含自然关键词)
  - 无标签,用关键词替代
```

## 常见问题

### Q1: 13 个平台的配文会同时生成吗?
**A**: 是的。提供照片信息后,工具会一次性返回所有 13 个平台的配文(或指定的平台子集),每个平台独立呈现,无需多次请求。

### Q2: 批量配文最多支持多少张照片?
**A**: 专业版无硬性上限,但建议单次批量不超过 20 张,确保配文质量。超过 20 张建议分批处理。

### Q3: 品牌风格配置如何保存与复用?
**A**: 品牌风格配置以 YAML 文件形式保存,可在不同项目中复用。支持同时维护多个品牌配置,按需切换:

```text
请使用 brand_a.yaml 的品牌风格为这张照片生成配文。

请使用 brand_b.yaml 的品牌风格为这张照片生成配文。
```

### Q4: 编辑分析可以单独使用吗?
**A**: 编辑分析默认随配文一起生成(作为独立章节)。如只需编辑分析不需配文,可在请求中说明:"请只提供编辑分析,不需要配文。"

### Q5: 双语配文如何呈现?
**A**: 专业版支持中英双语配文。每个平台会同时输出中文与英文两个版本,便于跨地区发布:

```text
Instagram (中文):
公路尽头是橘红色的天...

Instagram (English):
The road ends where the sky turns orange...
```

### Q6: 免费版用户升级后使用方式有变化吗?
**A**: 完全兼容。专业版沿用免费版的输入方式与配文格式,升级后直接获得全部 13 个平台与高级功能的访问权限,原有使用习惯无需改变。

### Q7: 平台格式规范会随平台更新调整吗?
**A**: 会。各平台的字数限制、标签策略、格式规范会随平台更新动态调整。专业版会定期同步最新规范,确保配文始终符合平台原生风格。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

