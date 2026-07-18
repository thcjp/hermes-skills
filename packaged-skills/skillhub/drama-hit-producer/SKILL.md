---
slug: drama-hit-producer
name: drama-hit-producer
version: "1.0.0"
displayName: "短剧爆款生产线"
summary: "小说一键转竖屏短剧,25步全链路从脚本到成片自动产出"
license: MIT
description: |-
  短剧爆款生产线——丢进一章小说,25步全自动管道吐出可发布的竖屏短剧。从剧本转换到多平台发布全链路覆盖,真人剧与动漫双风格切换,三轨角色构建,四层TTS智能配音,质量闭环自动重做,一条龙产出短剧赛道爆款。

  核心能力:
  - 25步全自动管道:章节获取→事件图谱→剧本转换→导演规划→分镜生成→配音→画面→合成→字幕→质检→发布
  - 双轨风格:真人剧(InstantID+视频生成)/动漫(FLUX/Kling)
  - 三轨角色构建:手工创建/AI批量生成/从剧本自动提取
  - 四层TTS配音:云端/本地GPU/免费方案智能降级匹配
  - 质量闭环:A/B/C/D四级评分,C/D级自动重做(最大2次)+人工兜底
  - 多平台发布:抖音/快手/B站一键同步

  适用场景:
  - 小说IP改编方:把库存小说批量转短剧,低成本变现IP
  - 短剧创作者:一条龙生产,不用懂剪辑也能出片
  - 内容矩阵批量生产:多集多角色,流水线作业
  - 副业达人做短剧分发:低成本入场短剧赛道

  输入要求:小说章节内容+项目配置(风格/平台/TTS偏好)

  差异化:不是单点工具,而是25步端到端全链路,双轨风格+三轨角色+四层TTS+质量闭环,从小说到成片零人工干预,成本最低14元/分钟。

  触发关键词:短剧生成、漫剧创作、分镜制作、事件图谱、质量监督、导演规划、角色工坊、TTS匹配、真人剧、动漫、小说转短剧
homepage: "https://skillhub.cn"
tags: [视频创作, 短剧, 内容创作, 自动化, AI视频]
tools: [read, exec]
---

# 短剧爆款生产线

从小说章节自动生成竖屏短剧,支持多集、多角色配音、多平台发布。核心能力包括双轨风格(真人剧/动漫)、三轨角色构建(手工/AI批量/自动提取)、四层TTS配音(云端/本地GPU/免费)、质量闭环(自动重做+人工兜底)、资产持久化。

**核心能力**:
- **双轨风格**: real_person(真人剧,InstantID云端API+视频生成) / anime(动漫,FLUX标准/Kling高级)
- **三轨角色**: manual(手工创建) / ai_batch_generate(AI批量生成) / auto_extract(从剧本自动提取)
- **四层TTS**: L1 CosyVoice2(云端) / L2 Fish-Speech(本地GPU) / L3 GPT-SoVITS(本地GPU) / L4 Edge-TTS(云端免费)
- **质量闭环**: auto_redo(C/D级自动重做,最大2次) + final_arbitration(人工兜底裁决)

**触发关键词**: 短剧生成/漫剧创作/分镜制作/事件图谱/质量监督/导演规划/资产提取/角色工坊/TTS匹配/真人剧/动漫

## 使用场景

从小说章节自动生成竖屏短剧,支持多集、多角色配音、多平台发布。适用于小说IP短剧化、内容矩阵批量生产、社交媒体短剧运营等场景。

## 工作流(25步管道)

### 输入格式
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

### 25步管道

1. **章节获取** - 调用章节存储API获取最新章节内容
2. **事件图谱构建** - 调用事件图谱API,提取章节事件+关系+embedding
3. **角色工坊匹配** - 调用角色管理API,三轨角色构建入口(manual/ai_batch/auto_extract)。支持seed_source 3选1: manual_input(手工输入种子文本) / from_novel_chapter(从小说章节提取) / from_script(从剧本提取),通过seed_source_ref关联来源ID
4. **TTS匹配** - 调用TTS匹配API,四层TTS智能匹配
5. **剧本转换** - 调用剧本转换API,+style_track分支(real_person/anime)
6. **导演规划** - 调用导演规划API,4项规划(场次拆分/台词字数/情绪强度/过渡)
7. **系列管理** - 调用系列管理API,创建系列+获取人设
8. **分镜生成** - 调用分镜生成API,+real_person分支(生成真人剧脚本)
9. **配音生成** - 调用TTS合成API,4层TTS路由(L1/L2/L3/L4)
10. **角色画面生成** - 调用角色一致性生成API,+style_track分支
11. **资产提取与衍生** - 调用资产提取API,衍生资产规则+@图N引用
12. **资产持久化** - 调用资产持久化API,持久化到JSON文件
13. **画面生成** - 调用视频生成API,+style_track分支(scene_8/scene_6/scene_7)。支持挑卡机制: N=3候选并行生成 + LLM 3维度评分(角色一致性40%+画面质量30%+剧本忠实度30%),通过selection_metadata记录候选列表和最终选择
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

### 输出格式
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

## 经验回写(自生长闭环)

生成完成后,自动回写经验到自生长系统,供后续生成参考:

1. **生成前查询历史经验**: 查询关键词"短剧生成"的历史经验,注入生成参数,避免重复犯错
2. **生成成功后记录经验**: 记录成功生成模式(drama_id/style_track/scene_id等)
3. **生成失败时记录错误教训**: 错误经验自动记录(错误码和原因),避免重复犯错
4. **定期统计经验**: 统计经验积累情况

## 双轨风格配置

| style_track | scene_id | 画面生成 | TTS推荐 | 成本 |
|:-----------|:---------|:---------|:--------|:-----|
| real_person | scene_8 | InstantID云端API+视频生成 | CosyVoice2/Fish-Speech | 约45元/分钟 |
| anime | scene_6 | FLUX | CosyVoice2/Edge-TTS | 约14元/分钟 |
| anime | scene_7 | Kling | CosyVoice2/Edge-TTS | 约35元/分钟 |

## 质量监督标准

### A/B/C/D四级评分

| 等级 | 说明 | 处理 |
|:-----|:-----|:-----|
| A | 优秀,可直接发布 | 通过 |
| B | 良好,微调后发布 | 通过 |
| C | 合格,需重做 | 触发auto_redo(最大2次) |
| D | 不合格,需重做 | 触发auto_redo(最大2次) |

### R1-R4绝对红线

- R1: 角色一致性(面部/服装/发型跨镜头一致)
- R2: 剧本忠实度(不得偏离原著核心剧情)
- R3: 画面质量(不得出现明显崩坏/扭曲)
- R4: 配音质量(音画同步/情感匹配)

## 异常处理

1. **章节不存在**: 返回 `{"success": false, "error": "章节不存在", "code": "CHAPTER_NOT_FOUND"}`
2. **配额不足**: 返回 `{"success": false, "error": "配额不足", "code": "QUOTA_EXCEEDED"}`
3. **生成锁冲突**: 返回 `{"success": false, "error": "该书正在生成中", "code": "GENERATION_LOCKED"}`
4. **LLM调用失败**: 降级链备用模型,均失败返回 `{"success": false, "error": "LLM调用失败", "code": "LLM_FAILED"}`
5. **超时(60分钟)**: 返回 `{"success": false, "error": "短剧生成超时(60分钟)", "code": "DRAMA_TIMEOUT"}`
6. **质量监督C/D级**: 触发auto_redo重做(最大2次),仍不达标触发final_arbitration人工兜底
7. **角色工坊匹配失败**: 返回 `{"success": false, "error": "角色工坊无匹配角色", "code": "CHARACTER_NOT_FOUND"}`
8. **TTS匹配失败**: 降级链L1->L4,均失败返回 `{"success": false, "error": "TTS引擎全部不可用", "code": "TTS_ALL_UNAVAILABLE"}`
9. **资产持久化失败**: 返回 `{"success": false, "error": "资产持久化失败", "code": "PERSIST_FAILED"}`
10. **最终裁决reject**: 返回 `{"success": false, "error": "人工裁决拒绝,需整体返工", "code": "ARBITRATION_REJECT"}`

## 数据存储

| 存储位置 | 说明 |
|:---------|:-----|
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 |
| TTS引擎 | API | 必需 | CosyVoice2/Fish-Speech/GPT-SoVITS/Edge-TTS四层降级 |
| 图像生成API | API | 必需 | InstantID/FLUX/Kling等,按style_track选择 |
| 视频生成API | API | 必需 | 视频合成引擎 |
| JSON文件存储 | 文件系统 | 必需 | exec工具创建drama_assets/目录 |

### API Key 配置
- **LLM_API_KEY**: 必需(通常由Agent内置) - 剧本转换/导演规划/分镜生成
- **TTS_API_KEY**: 可选 - 云端TTS引擎(如CosyVoice2)
- **IMAGE_API_KEY**: 可选 - 角色画面生成(InstantID/FLUX)
- **VIDEO_API_KEY**: 可选 - 视频生成引擎
- 配置方式: 在Agent的环境变量中设置

### 纯Markdown使用说明
四层TTS降级链中L4(Edge-TTS)为免费方案,无API Key可使用。本地GPU方案(Fish-Speech/GPT-SoVITS)需GPU环境。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

```bash
# 调用方式(动漫风格)
python drama_pipeline.py \
  --action execute \
  --params '{"project_id":"proj_001","book_id":"book_001","chapter_number":1,"platforms":["douyin"],"style_track":"anime","scene_id":"scene_6"}'

# 调用方式(真人剧风格)
python drama_pipeline.py \
  --action execute \
  --params '{"project_id":"proj_001","book_id":"book_001","chapter_number":1,"platforms":["douyin"],"style_track":"real_person","scene_id":"scene_8"}'
```

## 变更历史

| 版本 | 日期 | 变更 |
|:-----|:-----|:-----|
| v1.0.0 | 2026-07-17 | 初版创建,25步管道+双轨风格(real_person/anime)+三轨角色+四层TTS+质量闭环+资产持久化,JSON文件存储 |
