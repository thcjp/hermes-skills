---
slug: poetry-craftsman
name: poetry-craftsman
version: "1.1.0"
displayName: "诗词匠心"
summary: "一人做古诗词内容厂牌,6种融合模式+平仄校验+意境评分,图文短视频双输出"
license: Proprietary
description: |-
  诗词匠心是一款古诗词融合故事编织工具,打造古诗词内容厂牌。
  支持6种融合模式、平仄韵律校验、意境评分,图文与短视频双输出。
  
  核心能力:
  - 6种诗词融合模式
  - 平仄韵律自动校验
  - 意境融合度评分
  - 图文+短视频双输出
homepage: "https://skillhub.cn"
tags: [古诗词, 内容创作, 短视频, 文化IP]
tools:
  - read
  - exec
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
---
# 诗词匠心 Poetry Craftsman v1.1.0

古诗词融合故事编织工具,将历史人物诗词自然融入故事叙述,支持6种融合模式与图文/短视频双输出格式,可选画外音解说。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 诗词匠心平仄校验 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 核心能力

1. **6种融合模式**: 直接引用(quote)/化用(paraphrase)/意境延伸(blend)/正经对比(contrast)/打油诗改编(parody)/双角色对比(dual_character),覆盖从正经到搞笑全风格
2. **平仄韵律自动校验**: 古体诗/词模式自动校验平仄格律,标注不合律处,保证专业度
3. **意境融合度评分**: 量化评估诗词与故事情节的融合度(0-1评分),指导优化方向
4. **图文+短视频双输出**: article图文模式输出融合段落,short_video短视频脚本模式输出分镜(画面+台词+时长)
5. **诗词数据库查询与历史人物档案**: 按人物名查询相关诗词与背景资料,不可用时降级为纯LLM创作
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 历史人物故事连载 | character人物名+story_context故事背景+mode融合模式 | 融合诗词的故事段落+诗词标注+平仄校验+意境评分 |
| 古诗词教育内容(小学/中学/成人) | character+target_audience+poem_title | 适配受众理解力的诗词解读故事 |
| 短视频脚本创作 | character+output_format=short_video+voiceover | 分镜脚本(画面+台词+时长+角色)+总时长 |
| 打油诗/反差爆款内容 | mode=parody或contrast+character | 原诗+打油诗改编/正经+搞笑对比版本 |
| 双角色对比叙事 | mode=dual_character+character+poem_title | 真实人物念原诗+虚构孪生角色打油诗重说 |

**不适用于**: 现代诗创作(仅支持古诗词)、纯诗词翻译(无故事融合需求)、非中文诗词(仅支持中文古诗词)、长篇小说连载(单次输出为段落级非全篇)。

## 使用流程

### Step 1: 环境准备
- 确认Agent已加载本SKILL.md,且支持exec工具
- 在Agent环境变量中配置 `LLM_API_KEY`(必需)
- 诗词数据库和历史人物档案API为可选,不可用时自动降级为纯LLM创作

### Step 2: 接收输入参数
- 必填: `character`(历史人物名)
- 选填: `story_context`(故事上下文)、`poem_title`(指定诗词,不指定则自动匹配)、`mode`(融合模式,默认blend)、`target_audience`(受众,默认elementary)、`output_format`(输出格式,默认article)、`voiceover`(画外音,默认off)

### Step 3: 查询诗词与人物资料
- 调用诗词数据库API查询该人物相关诗词
- 调用历史人物档案API获取人物背景资料
- 异常处理: 诗词未找到→降级为无诗词融合的纯故事,poem_used=null;数据库不可用→降级为纯LLM创作

### Step 4: 根据融合模式用LLM编织故事
- quote: 原诗直接嵌入故事
- paraphrase: 改写为白话融入叙述
- blend: 诗词意境扩展为场景描写
- contrast: 正经解读+搞笑解读,极致反差
- parody: 古诗词→打油诗/顺口溜/网络梗版本
- dual_character: 真实人物念原诗,虚构孪生兄弟用打油诗重说

### Step 5: 平仄韵律校验(古体诗/词模式)
- 校验原诗平仄格律是否合律
- 输出meter_check(passed/notes)

### Step 6: 意境融合度评分
- LLM评估诗词与故事情节的有机融合度
- 输出imagery_score(0-1)

### Step 7: 输出结果
- article模式: 输出融合段落+诗词标注+校验+评分
- short_video模式: 输出分镜脚本(shot/duration/visual/dialogue/character)+总时长

## 输入格式

```json
{
  "character": "李白",
  "story_context": "李白被赐金放还,离开长安...",
  "poem_title": "行路难",
  "mode": "blend",
  "target_audience": "elementary",
  "output_format": "article",
  "voiceover": "off"
}
```

字段说明:
- `character`: 历史人物名(必填)
- `story_context`: 故事上下文背景
- `poem_title`: 指定诗词标题(可选,不指定则自动匹配)
- `mode`: 融合模式,可选: quote(直接引用)/paraphrase(化用)/blend(意境延伸)/contrast(对比)/parody(打油诗改编)/dual_character(双角色对比)
- `target_audience`: 目标受众,可选: elementary(小学)/middle(中学)/adult(成人)
- `output_format`: 输出格式,可选: article(图文,默认)/short_video(短视频脚本)
- `voiceover`: 画外音,可选: off(无画外音,默认)/on(有画外音解说)

## 输出格式

### 图文模式(output_format=article)

```json
{
  "success": true,
  "data": {
    "paragraph": "融合后的故事段落...",
    "poem_used": {"title": "行路难", "author": "李白", "lines_used": ["长风破浪会有时"]},
    "mode": "blend",
    "output_format": "article",
    "audience": "elementary",
    "voiceover": "off",
    "meter_check": {"passed": true, "notes": "平仄韵律校验结果"},
    "imagery_score": 0.88
  }
}
```

### 短视频脚本模式(output_format=short_video)

```json
{
  "success": true,
  "data": {
    "script": [
      {"shot": 1, "duration": "5s", "visual": "画面描述", "dialogue": "台词", "character": "画外音"},
      {"shot": 2, "duration": "8s", "visual": "画面描述", "dialogue": "台词", "character": "李白"}
    ],
    "total_duration": "60s",
    "poem_used": {"title": "静夜思", "author": "李白", "lines_used": ["床前看月光"]},
    "mode": "dual_character",
    "output_format": "short_video",
    "audience": "elementary",
    "voiceover": "on"
  }
}
```

## 异常处理

| 异常场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 人物名缺失 | 未提供character参数 | 返回success=false, error="必须提供character参数" |
| 诗词未找到 | 数据库无该人物诗词或poem_title不存在 | 降级为无诗词融合的纯故事,poem_used=null,标注warning |
| 诗词数据库不可用 | API超时或服务下线 | 降级为纯LLM创作(无诗词数据支撑),标注warning |
| 历史人物档案不可用 | API超时或服务下线 | 降级为通用历史知识创作,标注warning |
| LLM调用失败 | LLM服务不可用或超时 | 返回success=false, error="故事编织LLM调用失败" |
| mode参数无效 | 输入的mode不在6种支持范围内 | 默认使用blend模式,标注warning |
| target_audience无效 | 输入的受众不在支持范围内 | 默认使用elementary,标注warning |
| 平仄校验异常 | 诗词格式不规范无法校验 | 跳过校验,meter_check返回null,标注warning |
| 短视频脚本生成失败 | LLM返回格式异常 | 降级为article模式输出,标注warning |
| 故事上下文过长 | story_context超过5000字 | 截断保留前5000字,标注warning |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:---:|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | 国内可用: 通义千问/文心一言/智谱GLM/DeepSeek/Kimi |
| 诗词数据库 | API | 可选 | 诗词查询(不可用时降级为纯LLM创作) | 国内替代: 中华诗词数据库/古诗文网API/本地下载数据集 |
| 历史人物档案 | API | 可选 | 人物背景资料(不可用时降级为通用知识) | 国内替代: 维基百科中文/百度百科/本地历史知识库 |

### API Key 配置(零暴露原则)
- **LLM_API_KEY**: 必需(通常由Agent内置) - 诗词融入故事/平仄校验/意境评分
- **POETRY_DB_API_KEY**: 可选 - 诗词数据库查询(不可用时降级)
- **配置方式**: 必须通过Agent环境变量注入,严禁在SKILL.md或代码中硬编码API Key
- **安全检查**: 本SKILL.md中不包含任何API Key示例,所有Key均通过 `$env:LLM_API_KEY` 等环境变量读取

### 使用流程(补充)
诗词数据库不可用时降级为纯LLM创作。历史人物档案不可用时使用通用历史知识。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 意境延伸模式(图文)

**输入**:
```json
{"character":"李白","story_context":"李白月下独酌","mode":"blend","target_audience":"elementary"}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "paragraph": "夜色如水,月光洒满庭院。李白独自坐在石桌旁,一壶酒,一只杯。他举杯邀明月,月光在酒中荡漾,仿佛三位老友对饮。这便是'举杯邀明月,对影成三人'的意境——孤独,却不寂寞;一人,却似三人。",
    "poem_used": {"title": "月下独酌", "author": "李白", "lines_used": ["举杯邀明月,对影成三人"]},
    "mode": "blend",
    "output_format": "article",
    "audience": "elementary",
    "voiceover": "off",
    "meter_check": {"passed": true, "notes": "五言古诗,平仄合律"},
    "imagery_score": 0.88
  }
}
```

### 示例2: 双角色对比模式(短视频脚本)

**输入**:
```json
{"character":"李白","poem_title":"静夜思","mode":"dual_character","output_format":"short_video","voiceover":"on"}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "script": [
      {"shot": 1, "duration": "5s", "visual": "月光透过窗户照在床上", "dialogue": "话说李白那晚睡不着...", "character": "画外音"},
      {"shot": 2, "duration": "8s", "visual": "李白白衣站起,望月吟诗", "dialogue": "床前明月光,疑是地上霜。举头望明月,低头思故乡。", "character": "李白"},
      {"shot": 3, "duration": "8s", "visual": "李黑(孪生兄弟)睡眼惺忪", "dialogue": "抬头瞅月亮,低头想老家。被窝真暖和,不想去上朝。", "character": "李黑"},
      {"shot": 4, "duration": "5s", "visual": "两人同框对比", "dialogue": "同一轮月亮,两种心情。诗仙与凡人,只差一首诗。", "character": "画外音"}
    ],
    "total_duration": "26s",
    "poem_used": {"title": "静夜思", "author": "李白", "lines_used": ["床前明月光","举头望明月","低头思故乡"]},
    "mode": "dual_character",
    "output_format": "short_video",
    "audience": "elementary",
    "voiceover": "on"
  }
}
```

### 示例3: 打油诗改编模式

**输入**:
```json
{"character":"李白","poem_title":"静夜思","mode":"parody","target_audience":"adult"}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "paragraph": "李白原版:床前明月光,疑是地上霜。举头望明月,低头思故乡。\n\n打油诗版:空调坏了没电咯,月光照进被窝窝。抬头瞅瞅大月亮,低头想想老家锅。\n\n同一首诗,千年后读来,乡愁依旧,只是多了几分烟火气。",
    "poem_used": {"title": "静夜思", "author": "李白", "lines_used": ["床前明月光","疑是地上霜","举头望明月","低头思故乡"]},
    "mode": "parody",
    "output_format": "article",
    "audience": "adult",
    "voiceover": "off",
    "meter_check": {"passed": true, "notes": "原诗合律,打油诗为自由体不校验"},
    "imagery_score": 0.75
  }
}
```

### 示例4: 对比模式(正经+搞笑)

**输入**:
```json
{"character":"孔子","story_context":"孔子讲学","mode":"contrast","target_audience":"middle"}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "paragraph": "正经解读:孔子曰'人不知而不愠,不亦君子乎'——别人不了解自己却不生气,这不就是君子的修养吗?\n\n搞笑解读:孔子曰'人不知道我的大名,可我还没发怒,这已经很君子了好吧'——毕竟要是发怒了,就不只是君子,而是君子剑了。",
    "poem_used": {"title": "论语·学而", "author": "孔子", "lines_used": ["人不知而不愠,不亦君子乎"]},
    "mode": "contrast",
    "output_format": "article",
    "audience": "middle",
    "voiceover": "off",
    "meter_check": {"passed": true, "notes": "散文体,无需平仄校验"},
    "imagery_score": 0.82
  }
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 意境延伸模式(图文,李白行路难,小学受众)

**输入**:
```json
{
  "character": "李白",
  "story_context": "李白被赐金放还,离开长安,心情低落地走在崎岖山路上",
  "poem_title": "行路难",
  "mode": "blend",
  "target_audience": "elementary",
  "output_format": "article"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "paragraph": "长安的城门渐渐远去,李白独自走在崎岖的山路上。夕阳将他的影子拉得很长,像一条看不到尽头的路。他停下脚步,望着前方被云雾遮蔽的山峰,心中五味杂陈。曾经的翰林学士,如今却像个被遗弃的孩子。山风呼啸,吹动他的衣袍,也吹动了心底的那句诗——'长风破浪会有时,直挂云帆济沧海'。是啊,眼前的路虽然难走,但总有一天,他会乘着长风,破开万里浪,扬起云帆,横渡沧海。想到这里,李白的眼中重新燃起了光芒,他紧了紧背上的行囊,大步向前走去。",
    "poem_used": {"title": "行路难", "author": "李白", "lines_used": ["长风破浪会有时", "直挂云帆济沧海"]},
    "mode": "blend",
    "output_format": "article",
    "audience": "elementary",
    "voiceover": "off",
    "meter_check": {"passed": true, "notes": "七言古诗,平仄基本合律。'长风破浪会有时'平平仄仄仄仄平,'直挂云帆济沧海'仄仄平平仄平仄,符合古体诗宽韵要求。"},
    "imagery_score": 0.92
  }
}
```

**效果验证**: ✓意境延伸模式正确应用(诗词意境融入场景描写) ✓小学受众语言适配(通俗易懂) ✓平仄校验通过 ✓意境融合度0.92(高度融合) ✓诗句自然嵌入故事叙述

### 案例2: 打油诗改编模式(图文,苏轼,反差爆款)

**输入**:
```json
{
  "character": "苏轼",
  "story_context": "苏轼被贬黄州,夜游赤壁,写下念奴娇赤壁怀古",
  "poem_title": "念奴娇·赤壁怀古",
  "mode": "parody",
  "target_audience": "adult",
  "output_format": "article"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "paragraph": "苏轼被贬黄州那会儿,日子过得紧巴巴。有天晚上睡不着,溜达到赤壁边上看江景。看着滔滔江水,老苏突然来了灵感,提笔就是千古名篇:'大江东去,浪淘尽,千古风流人物。'\n\n但是呢,如果让苏轼用现代打油诗重写,大概是这样的:\n\n大江东去哗啦啦,\n浪花拍碎大家好。\n千古风流全跑了,\n只剩苏轼在发呆。\n小乔嫁人别惦记,\n周瑜年轻别比较,\n人生如梦别多想,\n还是喝酒最实在。\n\n写完打油诗,苏轼自己都笑了。或许,这就是他能'一蓑烟雨任平生'的原因吧——管他什么千古风流,活在当下,笑对人生,才是真豪杰。",
    "poem_used": {"title": "念奴娇·赤壁怀古", "author": "苏轼", "lines_used": ["大江东去,浪淘尽,千古风流人物", "一蓑烟雨任平生"]},
    "mode": "parody",
    "output_format": "article",
    "audience": "adult",
    "voiceover": "off",
    "meter_check": {"passed": true, "notes": "原词为词牌念奴娇,平仄合律。打油诗为顺口溜形式,不拘格律。"},
    "imagery_score": 0.85
  }
}
```

**效果验证**: ✓打油诗改编模式正确应用(原诗→打油诗) ✓反差幽默效果有效(千古名篇vs顺口溜) ✓原诗引用+打油诗改编双呈现 ✓意境融合度0.85 ✓成人受众适配(网络化表达)

### 案例3: 双角色对比模式(短视频脚本,杜甫,画外音)

**输入**:
```json
{
  "character": "杜甫",
  "story_context": "杜甫秋日登高,感慨万千",
  "poem_title": "登高",
  "mode": "dual_character",
  "target_audience": "middle",
  "output_format": "short_video",
  "voiceover": "on"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "script": [
      {"shot": 1, "duration": "5s", "visual": "秋日黄昏,长江两岸,落叶纷飞,江水奔涌", "dialogue": "公元767年,杜甫登高远眺。", "character": "画外音"},
      {"shot": 2, "duration": "8s", "visual": "杜甫(中年形象,衣衫朴素)站在高台上,望向远方,风拂衣袍", "dialogue": "风急天高猿啸哀,渚清沙白鸟飞回。", "character": "杜甫"},
      {"shot": 3, "duration": "8s", "visual": "画面切换:孪生兄弟'杜小甫'(现代打扮,手持奶茶)出现在同一场景", "dialogue": "风好大!猴子叫得贼惨!鸟都飞回窝了,我也想回家!", "character": "杜小甫"},
      {"shot": 4, "duration": "6s", "visual": "杜甫低头,看到落叶和江水,表情凝重", "dialogue": "无边落木萧萧下,不尽长江滚滚来。", "character": "杜甫"},
      {"shot": 5, "duration": "6s", "visual": "杜小甫也低头看落叶,吐槽", "dialogue": "叶子掉光了,江水还在流。这不就是...时间不等人嘛!", "character": "杜小甫"},
      {"shot": 6, "duration": "8s", "visual": "杜甫独坐,远眺落日,背景渐暗", "dialogue": "万里悲秋常作客,百年多病独登台。", "character": "杜甫"},
      {"shot": 7, "duration": "6s", "visual": "杜小甫也坐下来,表情从嬉笑变得认真", "dialogue": "一个人在外漂泊,身体还不好...老杜,原来你也挺难的。", "character": "杜小甫"},
      {"shot": 8, "duration": "4s", "visual": "画面定格,字幕浮现原诗全文", "dialogue": "登高——杜甫。千百年后,我们依然能读懂他的孤独。", "character": "画外音"}
    ],
    "total_duration": "51s",
    "poem_used": {"title": "登高", "author": "杜甫", "lines_used": ["风急天高猿啸哀,渚清沙白鸟飞回", "无边落木萧萧下,不尽长江滚滚来", "万里悲秋常作客,百年多病独登台"]},
    "mode": "dual_character",
    "output_format": "short_video",
    "audience": "middle",
    "voiceover": "on"
  }
}
```

**效果验证**: ✓双角色对比模式正确应用(杜甫原诗+杜小甫打油诗) ✓8个分镜完整(画面+台词+时长+角色) ✓总时长51秒(适合短视频) ✓画外音解说贯穿首尾 ✓原诗3句+打油诗3句交替呈现

### 案例4: 诗词数据库降级(纯LLM创作,无数据支撑)

**输入**:
```json
{
  "character": "王维",
  "story_context": "王维隐居辋川,秋日傍晚散步",
  "mode": "blend",
  "output_format": "article"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "paragraph": "辋川的秋天来得格外安静。王维沿着山路慢慢走着,夕阳的余晖洒在松林间,斑驳的光影落在青苔上。山间空无一人,只有偶尔传来的鸟鸣打破寂静。他想起那句'空山不见人,但闻人语响。返景入深林,复照青苔上。'此刻的辋川,不正是诗中描绘的景象吗?王维微微一笑,心中充满了宁静。这山水之间,有他想要的一切——远离尘嚣,与自然为伴,在诗画中度过余生。",
    "poem_used": {"title": "鹿柴", "author": "王维", "lines_used": ["空山不见人,但闻人语响", "返景入深林,复照青苔上"]},
    "mode": "blend",
    "output_format": "article",
    "audience": "elementary",
    "voiceover": "off",
    "meter_check": {"passed": true, "notes": "五言绝句,平仄合律。'空山不见人'平平仄仄平,'但闻人语响'仄平平仄仄,符合五绝格律。"},
    "imagery_score": 0.88
  },
  "error": "诗词数据库不可用,已降级为纯LLM创作(基于通用诗词知识),诗词准确性可能略有偏差",
  "code": "POETRY_DB_FALLBACK"
}
```

**效果验证**: ✓诗词数据库降级为纯LLM创作 ✓降级原因在error字段标注 ✓错误码POETRY_DB_FALLBACK正确返回 ✓自动匹配诗词(鹿柴) ✓意境融合度0.88(高度融合)

### 案例5: 正经对比模式(图文,李清照,反差解读)

**输入**:
```json
{
  "character": "李清照",
  "story_context": "李清照南渡后,秋日独酌,思念故土",
  "poem_title": "声声慢",
  "mode": "contrast",
  "target_audience": "adult",
  "output_format": "article"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "paragraph": "南渡后的李清照,住在临安一间小院里。秋风吹过窗棂,带来桂花的冷香。她端起酒杯,却怎么也喝不下去。那些寻寻觅觅的日子,那些冷冷清清的夜晚,那些凄凄惨惨戚戚的心事,都化作了笔下的词句。\n\n【正经解读】\n'寻寻觅觅,冷冷清清,凄凄惨惨戚戚。'这十四个叠字,是词史上最惊心动魄的开篇。李清照用最朴素的文字,写出了最深沉的孤独。每一组叠字都是一层递进:先是动作上的寻寻觅觅(寻找什么?故土?逝去的爱情?曾经的自己?),再到环境的冷冷清清(物理上的寒冷,更是心灵的荒凉),最后是情感的凄凄惨惨戚戚(层层加深的悲凉)。这不是无病呻吟,而是一个经历了国破家亡的女性,在乱世中对生命本质的叩问。\n\n【接地气解读】\n翻译成现代话就是:翻箱倒柜找东西(找啥呢?),屋里冷得要命还没人陪(惨),心里堵得慌想哭又哭不出来(更惨)。李清照要是发朋友圈,大概就是:'今天又是一个人,冷。配图:一杯酒。'但人家愣是把这种状态写成了千古绝唱,这就是才女的实力。",
    "poem_used": {"title": "声声慢", "author": "李清照", "lines_used": ["寻寻觅觅,冷冷清清,凄凄惨惨戚戚"]},
    "mode": "contrast",
    "output_format": "article",
    "audience": "adult",
    "voiceover": "off",
    "meter_check": {"passed": true, "notes": "词牌声声慢,叠字开篇为李清照独创,格律自由但不失韵律。"},
    "imagery_score": 0.90
  }
}
```

**效果验证**: ✓正经对比模式正确应用(正经解读+接地气解读) ✓反差效果显著(学术分析vs朋友圈吐槽) ✓原词引用+深度解析 ✓意境融合度0.90 ✓成人受众适配(两种解读层次丰富)

## 常见问题

### Q1: 如何开始使用诗词匠心?
A: 三步启动:(1)将SKILL.md放入Agent的skills目录;(2)确认Agent环境变量已配置LLM_API_KEY;(3)调用时传入character(必填)和mode(可选,默认blend)即可。诗词数据库和历史人物档案API为可选,不可用时自动降级为纯LLM创作。

### Q2: 诗词数据库不可用会影响输出质量吗?
A: 会一定程度影响。诗词数据库不可用时,系统降级为纯LLM创作,LLM依赖内置知识库生成诗词,可能出现诗词引用不准确或张冠李戴。建议关键内容人工核对诗词原文。可配置国内替代数据源(中华诗词数据库/古诗文网API)提升准确度。

### Q3: 6种融合模式如何选择?
A: 按内容定位选择:(1)正经文化科普→quote/paraphrase/blend;(2)教育内容(小学/中学)→paraphrase+elementary受众;(3)搞笑爆款→parody/contrast/dual_character;(4)短视频带货→dual_character+short_video+voiceover=on。contrast和parody适合制造反差引流,dual_character适合短视频双角色对话。

### Q4: 平仄校验不准确怎么办?
A: 平仄校验基于LLM内置诗词格律知识,可能存在误差。处理方式:(1)关键内容建议人工复核平仄;(2)使用专业诗词格律工具(如诗词吾爱/搜韵网)二次校验;(3)meter_check返回null时表示诗词格式不规范无法校验,需人工确认诗词版本。

### Q5: 短视频脚本可以直接用于拍摄吗?
A: 脚本输出包含分镜(shot/duration/visual/dialogue/character)和总时长,结构完整可直接作为拍摄参考。但实际拍摄还需:(1)根据visual描述制作画面/分镜图;(2)录制dialogue台词(可配合TTS工具);(3)按duration控制节奏。建议拍摄前人工微调台词口语化程度。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **诗词范围**: 仅支持中文古诗词(诗/词/曲),不支持现代诗、外国诗歌、自创诗词校验
- **人物覆盖**: 依赖诗词数据库和LLM知识,冷门历史人物可能查不到诗词,需手动指定poem_title
- **平仄校验精度**: 基于LLM内置格律知识,对生僻词或多音字可能误判,专业场景需人工复核
- **意境评分主观性**: imagery_score为LLM主观评估,不同模型评分可能差异较大,仅作参考
- **短视频时长**: 总时长通常控制在60秒内,长视频需多次调用拼接
- **受众适配**: target_audience主要影响语言难度,不改变诗词原文和核心意境
- **输出段落长度**: 单次输出为段落级(约300-800字),不支持全文小说级长篇输出

## 安全

### API Key 零暴露原则
- **环境变量注入**: 所有API Key(LLM_API_KEY/POETRY_DB_API_KEY)必须通过Agent环境变量注入,严禁在SKILL.md、配置文件或代码中硬编码
- **本文件无Key示例**: 本SKILL.md中不包含任何真实或示例API Key,所有引用均使用 `$env:LLM_API_KEY` 占位
- **日志脱敏**: exec工具记录日志时,自动过滤包含"key"/"token"/"secret"字段的值

### 内容安全
- **诗词版权**: 古诗词多为公共领域作品,但部分现代注解/翻译可能有版权,商业使用前需确认
- **历史人物表述**: 对历史人物的解读应尊重史实,搞笑模式(parody/contrast)避免恶意歪曲或贬损
- **教育内容审核**: target_audience=elementary时,系统自动过滤不适合未成年人的解读方式
