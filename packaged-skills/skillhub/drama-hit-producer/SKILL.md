---

slug: drama-hit-producer
name: drama-hit-producer
version: 1.0.1
displayName: "短剧爆款生产线"
summary: "小说一键转竖屏短剧,25步全链路从脚本到成片自动产出。短剧爆款生产线——丢进一章小说,25步全自动管道吐出可发布的竖屏短剧。核心功能:双轨风格(真人剧InstantID+动漫FLUX/Kli"
license: "MIT"
description: |-
  短剧爆款生产线——丢进一章小说,25步全自动管道吐出可发布的竖屏短剧。核心功能:双轨风格(真人剧InstantID+动漫FLUX/Kling)、三轨角色构建(手工/AI批量/自动提取)、四层TTS智能配音(云端/本地GPU/免费)、质量闭环(A/B/C/D评分+自动重做+人工兜底)、25步管道从剧本转换到多平台发布全链路覆盖、资产持久化、经验回写自生长闭环
homepage: ""
tags: 短剧,api,style_track,tts,anime,real_person
tools:
  - read
  - exec
  - write
category: "Automation"

---

# 短剧爆款生产线

从小说章节自动生成竖屏短剧,支持多集、多角色配音、多平台发布。核心能力包括双轨风格(真人剧/动漫)、三轨角色构建(手工/AI批量/自动提取)、四层TTS配音(云端/本地GPU/免费)、质量闭环(自动重做+人工兜底)、资产持久化.
## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 核心能力

1. **25步全自动管道**:从章节获取→事件图谱→角色工坊→TTS匹配→剧本转换→导演规划→分镜生成→配音→画面生成→视频合成→字幕→质量监督→重做→裁决→一致性验证→内容审核→营销注入→SEO→多平台发布→状态回写→资产回写,全链路覆盖
2. **双轨风格切换**:real_person(真人剧,InstantID云端API+视频生成,约45元/分钟) / anime(动漫,FLUX标准约14元/分钟或Kling高级约35元/分钟),按style_track参数选择
3. **三轨角色构建**:manual(手工创建) / ai_batch_generate(AI批量生成) / auto_extract(从剧本自动提取),支持seed_source 3选1(manual_input/from_novel_chapter/from_script)
4. **四层TTS智能配音**:L1 CosyVoice2(云端) / L2 Fish-Speech(本地GPU) / L3 GPT-SoVITS(本地GPU) / L4 Edge-TTS(云端免费),自动降级链保证配音可用
5. **质量闭环+经验回写**:A/B/C/D四级评分+R1-R4红线检查,C/D级自动重做(最大2次)+人工兜底裁决;生成完成后自动回写经验到自生长系统供后续参考
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 | 是否适用 |
|:-----|:-----|:-----|:-----|
| 小说IP短剧化 | book_id+chapter_number+style_track | 可发布竖屏短剧视频 | 适用 |
| 内容矩阵批量生产 | 多章节+多platforms | 多集短剧+多平台发布 | 适用 |
| 真人剧风格短剧 | style_track=real_person+scene_8 | InstantID真人剧视频 | 适用 |
| 动漫风格短剧 | style_track=anime+scene_6/7 | FLUX/Kling动漫短剧 | 适用 |
| 多平台分发发布 | 已生成短剧+platforms列表 | 多平台同步发布结果 | 适用 |
| 实时直播短剧演出 | 实时演员表演+直播推流 | 不适用(本Skill为离线AI生成) | 不适用 |
| 横屏电影级长片制作 | 90分钟横屏院线需求 | 不适用(本Skill为竖屏短剧) | 不适用 |
| 纯文字小说续写创作 | 小说文本续写 | 不适用(本Skill为视频生成非文字创作) | 不适用 |

## 使用流程

### Step 1: 输入参数准备
- 必填参数:project_id(项目ID)、book_id(小说ID)、chapter_number(章节号,正整数)
- 可选参数:platforms(发布平台列表)、style_track(real_person/anime,默认anime)、scene_id(scene_6/7/8)、character_set_id(角色集合ID)、tts_config(TTS配置)

### Step 2: 25步管道执行
按以下25步顺序执行,每步失败按异常处理策略处理:

1. **章节获取** - 调用章节存储API获取最新章节内容
2. **事件图谱构建** - 调用事件图谱API,提取章节事件+关系+embedding
3. **角色工坊匹配** - 调用角色管理API,三轨角色构建入口(manual/ai_batch/auto_extract)
4. **TTS匹配** - 调用TTS匹配API,四层TTS智能匹配
5. **剧本转换** - 调用剧本转换API,+style_track分支(real_person/anime)
6. **导演规划** - 调用导演规划API,4项规划(场次拆分/台词字数/情绪强度/过渡)
7. **系列管理** - 调用系列管理API,创建系列+获取人设
8. **分镜生成** - 调用分镜生成API,+real_person分支
9. **配音生成** - 调用TTS合成API,4层TTS路由(L1/L2/L3/L4)
10. **角色画面生成** - 调用角色一致性生成API,+style_track分支
11. **资产提取与衍生** - 调用资产提取API,衍生资产规则+@图N引用
12. **资产持久化** - 调用资产持久化API,持久化到JSON文件
13. **画面生成** - 调用视频生成API,+style_track分支。支持挑卡机制:N=3候选并行生成+LLM 3维度评分
14. **视频合成** - 调用视频合成API,分镜合并
15. **字幕生成** - 调用字幕生成API
16. **质量监督审核** - 调用质量监督API,A/B/C/D评分+R1-R4红线
17. **质量闭环重做** - 调用自动重做API,C/D级自动重做(最大2次)
18. **最终裁决** - 调用人工裁决API,人工兜底裁决(pass/reject)
19. **一致性验证** - 调用系列验证API,集间一致性检查
20. **内容审核** - 调用敏感词检测API
21. **营销注入** - 调用营销文案API,适配各平台
22. **SEO/GEO优化** - 调用SEO优化API,注入品牌关键词+FAQ Schema
23. **多平台发布** - 调用发布API,多平台同步发布
24. **短剧状态回写** - 调用状态回写API,更新短剧生成状态
25. **资产回写** - 调用资产持久化API,整体资产回写闭环

### Step 3: 经验回写(自生长闭环)
- 生成前查询历史经验:查询关键词"短剧生成"的历史经验,注入生成参数,避免重复犯错
- 生成成功后记录经验:记录成功生成模式(drama_id/style_track/scene_id等)
- 生成失败时记录错误教训:错误经验自动记录(错误码和原因)

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 双轨风格配置

| style_track | scene_id | 画面生成 | TTS推荐 | 成本 |
|---------:|---------:|---------:|---------:|---------:|
| real_person | scene_8 | InstantID云端API+视频生成 | CosyVoice2/Fish-Speech | 约45元/分钟 |
| anime | scene_6 | FLUX | CosyVoice2/Edge-TTS | 约14元/分钟 |
| anime | scene_7 | Kling | CosyVoice2/Edge-TTS | 约35元/分钟 |

## 质量监督标准

### A/B/C/D四级评分

| 等级 | 说明 | 处理 |
|:---:|:---:|:---:|
| A | 优秀,可直接发布 | 通过 |
| B | 良好,微调后发布 | 通过 |
| C | 合格,需重做 | 触发auto_redo(最大2次) |
| D | 不合格,需重做 | 触发auto_redo(最大2次) |

### R1-R4绝对红线
- R1: 角色一致性(面部/服装/发型跨镜头一致)
- R2: 剧本忠实度(不得偏离原著核心剧情)
- R3: 画面质量(不得出现明显崩坏/扭曲)
- R4: 配音质量(音画同步/情感匹配)

## 输入格式
```json
{
  "project_id": "项目ID(必填)",
  "book_id": "小说ID(必填)",
  "chapter_number": "章节号(必填,正整数)",
  "platforms": ["douyin", "kuaishou", "bilibili"],
  "style_track": "real_person或anime(可选,默认anime)",
  "scene_id": "scene_6/scene_7/scene_8(可选,根据style_track自动选择)",
  "character_set_id": "角色集合ID(可选,从角色工坊选择)",
  "tts_config": {"engine": "cosyvoice2", "voice_id": "xxx"}
}
```

## 输出格式
```json
{
  "success": true,
  "data": {
    "drama_id": "短剧ID",
    "video_url": "视频URL",
    "style_track": "real_person",
    "scene_id": "scene_8",
    "publish_results": [{"platform": "douyin", "success": true, "url": "..."}]
  }
}
```

## 异常处理

| 异常场景 | 原因 | 处理方式 | 错误码 |
|:------|------:|:------|:------|
| 章节不存在 | book_id/chapter_number无效 | 返回错误提示 | CHAPTER_NOT_FOUND |
| 配额不足 | 日/月配额达到上限 | 返回错误,提示升级或等待 | QUOTA_EXCEEDED |
| 生成锁冲突 | 该书正在生成中 | 返回错误,提示稍后 | GENERATION_LOCKED |
| LLM调用失败 | LLM服务不可用 | 降级链备用模型,均失败返回错误 | LLM_FAILED |
| 超时(60分钟) | 管道执行超过60分钟 | 返回超时错误 | DRAMA_TIMEOUT |
| 质量监督C/D级 | 评分不达标 | 触发auto_redo重做(最大2次),仍不达标触发人工兜底 | QUALITY_REDO |
| 角色工坊匹配失败 | 角色集合无匹配角色 | 返回错误,提示先创建角色 | CHARACTER_NOT_FOUND |
| TTS匹配失败 | 所有TTS引擎不可用 | 降级链L1→L4,均失败返回错误 | TTS_ALL_UNAVAILABLE |
| 资产持久化失败 | 文件写入失败 | 返回错误,检查文件路径权限 | PERSIST_FAILED |
| 最终裁决reject | 人工裁决拒绝 | 返回错误,需整体返工 | ARBITRATION_REJECT |

## 数据存储

| 存储位置 | 说明 |
|---:|:---|
| drama_assets/{project_id}/characters.json | 角色资产持久化,含角色ID/种子/衍生资产 |
| drama_assets/{project_id}/episodes/{chapter}.json | 每集短剧资产(分镜/配音/画面/视频) |
| drama_assets/{project_id}/style_track.json | 风格轨道配置(双轨风格+场景ID) |
| predictions/{drama_id}.json | 质量评分记录 |
| reviews/{drama_id}.json | 质量复盘记录 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:------:|--------|:-------|:------:|--------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | DeepSeek/通义千问/文心一言/Kimi等国内模型 |
| TTS引擎 | API | 必需 | CosyVoice2/Fish-Speech/GPT-SoVITS/Edge-TTS四层降级 | CosyVoice2(阿里)/Edge-TTS(微软免费)等国内可用 |
| 图像生成API | API | 必需 | InstantID/FLUX/Kling等,按style_track选择 | 可灵AI(快手)/即梦AI(字节)等国内图像生成 |
| 视频生成API | API | 必需 | 视频合成引擎 | 可灵AI/即梦AI/腾讯智影等国内视频生成 |
| JSON文件存储 | 文件系统 | 必需 | exec工具创建drama_assets/目录 | 本地文件系统,无海外依赖 |

### API Key 配置与安全要求
- **LLM_API_KEY**: 必需(通常由Agent内置) - 剧本转换/导演规划/分镜生成
- **TTS_API_KEY**: 可选 - 云端TTS引擎(如CosyVoice2)
- **IMAGE_API_KEY**: 可选 - 角色画面生成(InstantID/FLUX)
- **VIDEO_API_KEY**: 可选 - 视频生成引擎
- 配置方式: 在Agent的环境变量中设置
- **零暴露原则**: API Key必须通过环境变量注入(如`$env:IMAGE_API_KEY`),严禁硬编码在SKILL.md或脚本源码中;所有示例代码中Key位置使用环境变量占位符;禁止在日志、错误信息、输出JSON中打印Key明文

### 使用流程(补充)
四层TTS降级链中L4(Edge-TTS)为免费方案,无API Key可使用。本地GPU方案(Fish-Speech/GPT-SoVITS)需GPU环境.
只需将SKILL.md文件放入Agent的skills目录即可直接使用.
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力.
### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 动漫风格短剧生成

**输入**:
```json
{
  "project_id": "proj_001",
  "book_id": "book_001",
  "chapter_number": 1,
  "platforms": ["douyin"],
  "style_track": "anime",
  "scene_id": "scene_6"
}
```

**执行流程**: 章节获取→事件图谱→角色工坊→TTS匹配→剧本转换(anime分支)→导演规划→分镜生成→配音(L1 CosyVoice2)→角色画面(FLUX)→画面生成(挑卡N=3)→视频合成→字幕→质量监督→发布

**输出**:
```json
{
  "success": true,
  "data": {
    "drama_id": "drama_20260717_001",
    "video_url": "output/dramas/drama_20260717_001.mp4",
    "style_track": "anime",
    "scene_id": "scene_6",
    "quality_grade": "A",
    "publish_results": [{"platform": "douyin", "success": true, "url": "https://douyin.com/video/xxx"}]
  },
  "error": null,
  "code": null
}
```

### 示例2: 真人剧风格短剧生成

**输入**:
```json
{
  "project_id": "proj_001",
  "book_id": "book_001",
  "chapter_number": 1,
  "platforms": ["douyin", "kuaishou"],
  "style_track": "real_person",
  "scene_id": "scene_8"
}
```

**执行流程**: 章节获取→事件图谱→角色工坊→TTS匹配→剧本转换(real_person分支)→导演规划→分镜生成(真人剧脚本)→配音→角色画面(InstantID)→画面生成→视频合成→字幕→质量监督→多平台发布

**输出**:
```json
{
  "success": true,
  "data": {
    "drama_id": "drama_20260717_002",
    "video_url": "output/dramas/drama_20260717_002.mp4",
    "style_track": "real_person",
    "scene_id": "scene_8",
    "quality_grade": "B",
    "publish_results": [
      {"platform": "douyin", "success": true, "url": "https://douyin.com/video/yyy"},
      {"platform": "kuaishou", "success": true, "url": "https://kuaishou.com/video/zzz"}
    ]
  },
  "error": null,
  "code": null
}
```

### 示例3: 质量不达标自动重做

**输入**: 质量监督评分为C级
```json
{"project_id": "proj_001", "book_id": "book_001", "chapter_number": 2, "style_track": "anime"}
```

**输出**: 第一次重做后达标
```json
{
  "success": true,
  "data": {
    "drama_id": "drama_20260717_003",
    "video_url": "output/dramas/drama_20260717_003.mp4",
    "quality_grade": "B",
    "quality_history": [
      {"redo_count": 0, "grade": "C", "triggered_redo": true},
      {"redo_count": 1, "grade": "B", "triggered_redo": false}
    ]
  },
  "error": null,
  "code": null
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成.
### 案例1: 动漫风格短剧生成(FLUX标准画质,多平台发布)

**输入**:
```json
{
  "project_id": "proj_001",
  "book_id": "novel_001",
  "chapter_number": 1,
  "platforms": ["douyin", "kuaishou", "bilibili"],
  "style_track": "anime",
  "scene_id": "scene_6",
  "tts_config": {"engine": "cosyvoice2", "voice_id": "voice_001"}
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "drama_id": "drama_20260720_001",
    "video_url": "https://cdn.dramastudio.com/output/drama_20260720_001.mp4",
    "style_track": "anime",
    "scene_id": "scene_6",
    "duration": 90,
    "quality_grade": "A",
    "character_count": 3,
    "publish_results": [
      {"platform": "douyin", "success": true, "url": "https://douyin.com/video/drama_001"},
      {"platform": "kuaishou", "success": true, "url": "https://kuaishou.com/video/drama_001"},
      {"platform": "bilibili", "success": true, "url": "https://bilibili.com/video/drama_001"}
    ],
    "pipeline_steps_completed": 25,
    "cost_estimate": 21
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓25步管道全流程完成 ✓动漫风格FLUX引擎正确路由 ✓质量评分A级(可直接发布) ✓三平台同步发布成功 ✓成本约21元(14元/分钟x1.5分钟)

### 案例2: 真人剧风格短剧生成(InstantID,高保真)

**输入**:
```json
{
  "project_id": "proj_002",
  "book_id": "novel_002",
  "chapter_number": 3,
  "platforms": ["douyin"],
  "style_track": "real_person",
  "scene_id": "scene_8",
  "character_set_id": "char_set_001",
  "tts_config": {"engine": "cosyvoice2", "voice_id": "voice_real_01"}
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "drama_id": "drama_20260720_002",
    "video_url": "https://cdn.dramastudio.com/output/drama_20260720_002.mp4",
    "style_track": "real_person",
    "scene_id": "scene_8",
    "duration": 120,
    "quality_grade": "A",
    "character_count": 4,
    "publish_results": [
      {"platform": "douyin", "success": true, "url": "https://douyin.com/video/drama_002"}
    ],
    "pipeline_steps_completed": 25,
    "cost_estimate": 90
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓真人剧InstantID引擎正确路由 ✓角色一致性验证通过(R1红线) ✓质量评分A级 ✓抖音平台发布成功 ✓成本约90元(45元/分钟x2分钟)

### 案例3: TTS降级场景(L1不可用,降级到L4免费方案)

**输入**:
```json
{
  "project_id": "proj_003",
  "book_id": "novel_003",
  "chapter_number": 5,
  "platforms": ["douyin"],
  "style_track": "anime",
  "scene_id": "scene_6",
  "tts_config": {"engine": "cosyvoice2", "voice_id": "voice_002"}
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "drama_id": "drama_20260720_003",
    "video_url": "https://cdn.dramastudio.com/output/drama_20260720_003.mp4",
    "style_track": "anime",
    "scene_id": "scene_6",
    "duration": 60,
    "quality_grade": "B",
    "character_count": 2,
    "publish_results": [
      {"platform": "douyin", "success": true, "url": "https://douyin.com/video/drama_003"}
    ],
    "pipeline_steps_completed": 25,
    "cost_estimate": 14,
    "tts_engine_used": "edge_tts",
    "tts_fallback_chain": ["cosyvoice2_failed", "fish_speech_unavailable", "gpt_sovits_unavailable", "edge_tts_success"]
  },
  "error": "L1 CosyVoice2不可用,已降级到L4 Edge-TTS(免费方案),配音质量略有降低",
  "code": "TTS_FALLBACK"
}
```

**效果验证**: ✓TTS四层降级链正确触发(L1→L2→L3→L4) ✓L4 Edge-TTS免费方案成功兜底 ✓降级链完整记录 ✓质量评分B级(微调后可发布) ✓服务可用性保证(降级而非失败)

### 案例4: 质量监督C级重做(自动重做后通过)

**输入**:
```json
{
  "project_id": "proj_004",
  "book_id": "novel_004",
  "chapter_number": 7,
  "platforms": ["douyin", "kuaishou"],
  "style_track": "anime",
  "scene_id": "scene_7",
  "tts_config": {"engine": "cosyvoice2", "voice_id": "voice_003"}
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "drama_id": "drama_20260720_004",
    "video_url": "https://cdn.dramastudio.com/output/drama_20260720_004.mp4",
    "style_track": "anime",
    "scene_id": "scene_7",
    "duration": 75,
    "quality_grade": "A",
    "character_count": 3,
    "publish_results": [
      {"platform": "douyin", "success": true, "url": "https://douyin.com/video/drama_004"},
      {"platform": "kuaishou", "success": true, "url": "https://kuaishou.com/video/drama_004"}
    ],
    "pipeline_steps_completed": 25,
    "cost_estimate": 44,
    "quality_history": [
      {"attempt": 1, "grade": "C", "red_line_violation": "R3:画面质量-角色面部扭曲", "redo_triggered": true},
      {"attempt": 2, "grade": "A", "red_line_violation": null, "redo_triggered": false}
    ]
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓质量监督C级正确检测(R3画面质量红线) ✓自动重做机制触发(第1次重做) ✓重做后质量提升至A级 ✓R1-R4红线全部通过 ✓双平台发布成功

## 常见问题

### Q1: 真人剧和动漫风格有什么区别?如何选择?
A: 真人剧(style_track=real_person)使用InstantID云端API生成真人风格画面,成本约45元/分钟,适合现实题材;动漫(style_track=anime)使用FLUX(约14元/分钟,标准画质)或Kling(约35元/分钟,高级画质),适合玄幻/二次元题材。建议:预算有限选anime+FLUX(scene_6),追求真实感选real_person(scene_8),追求画质选anime+Kling(scene_7).
### Q2: 四层TTS降级链如何工作?
A: TTS按L1→L2→L3→L4降级:L1 CosyVoice2(云端,高质量,需API Key)→L2 Fish-Speech(本地GPU,免费)→L3 GPT-SoVITS(本地GPU,免费)→L4 Edge-TTS(云端免费,兜底)。无API Key时直接使用L4 Edge-TTS免费方案。本地GPU方案需GPU环境,无GPU时跳过L2/L3直接到L4.
### Q3: 质量监督C/D级如何处理?
A: C/D级触发auto_redo自动重做(最大2次),重做后仍不达标触发final_arbitration人工兜底裁决(pass/reject)。R1-R4红线检查:角色一致性/剧本忠实度/画面质量/配音质量,任一红线不通过直接判D级。人工裁决reject需整体返工(ARBITRATION_REJECT).
### Q4: 25步管道执行超时怎么办?
A: 管道执行超时上限为60分钟,超时返回DRAMA_TIMEOUT错误。建议:1)检查各API服务是否正常;2)降低单集复杂度(减少分镜数量);3)使用anime+FLUX(scene_6)降低生成时间;4)分章节分批生成避免单次管道过长。生成锁冲突(GENERATION_LOCKED)时同一book_id不可并行生成.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

1. **单次管道超时60分钟**:25步管道执行超时上限60分钟,超时返回DRAMA_TIMEOUT,复杂章节可能超时,需分批生成或降低复杂度
2. **同一book_id不可并行生成**:生成锁机制(GENERATION_LOCKED)限制同一book_id同时只能有一个生成任务,需等待前一个完成
3. **真人剧成本较高**:real_person风格使用InstantID云端API,成本约45元/分钟,动漫FLUX仅约14元/分钟,预算有限建议选择动漫风格
4. **本地GPU TTS需GPU环境**:L2 Fish-Speech和L3 GPT-SoVITS需本地GPU环境,无GPU时只能使用L1(需Key)或L4(Edge-TTS免费)
5. **竖屏短剧输出固定**:本Skill输出为竖屏短剧(9:16),不支持横屏电影级长片制作

## 变更历史

| 版本 | 日期 | 变更 |
|----|----|----|
| v1.0.0 | 2026-07-17 | 初版创建,25步管道+双轨风格(real_person/anime)+三轨角色+四层TTS+质量闭环+资产持久化,JSON文件存储 |
