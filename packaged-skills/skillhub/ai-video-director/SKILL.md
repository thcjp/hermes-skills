---
slug: ai-video-studio-pro
name: ai-video-studio-pro
version: "1.0.0"
displayName: "AI视频导演"
summary: "一个人就是一支视频团队,脚本到成片一站式+智能路由+营销策略注入"
license: MIT
description: |-
  AI视频导演——一个人就是一支视频团队。从脚本到成片一站式搞定,热点短视频生成、TTS配音、字幕烧录、多平台适配、口型同步数字人,智能路由选最优引擎,营销策略自动注入卖点钩子CTA。

  核心能力:
  - 脚本到成片一站式:脚本生成→配音→画面→字幕→质检全链路
  - 7大场景覆盖:热点短视频/指令生成/剪辑合并/配音/字幕/多平台适配/口型同步
  - 智能路由决策树:按一致性需求/内容类型/成本预算选最优引擎
  - 多引擎降级保障:主引擎失败自动降级,保障稳定性
  - 营销策略注入:卖点提炼+情绪钩子+CTA话术自动注入关键帧
  - 口型同步数字人:数字人出镜视频,口型与语音精准同步

  适用场景:
  - 短视频矩阵操盘手:批量出片,多平台分发最大化曝光
  - 独立博主热点追踪:热点短视频自动生成,抢占流量窗口
  - 副业达人批量出片:低成本批量生产视频内容变现
  - 数字人内容创作者:口型同步数字人视频,虚拟主播内容

  差异化:不是单点视频工具,而是脚本到成片一站式工作站,智能路由决策树按场景选最优引擎,多引擎降级保障可用性,营销策略自动注入让视频自带转化能力,一个人就能完成一支视频团队的工作。

  触发关键词:视频生成、短视频制作、视频剪辑、配音合成、口型同步、数字人视频、字幕添加、视频导演、分镜制作、成片制作
homepage: "https://skillhub.cn"
tags: [视频创作, AI视频, 短视频, 数字人, 内容自动化]
tools: [read, exec]
---

# AI视频导演

> 定位: 脚本到成片一站式视频制作
> 设计: 热点短视频生成 + 口型同步视频 + 智能路由决策树 + 多引擎降级

## 使用场景

| 编号 | 场景 | 触发条件 | 优先级 |
|:-----|:-----|:---------|:-------|
| VG-01 | 热点短视频生成 | 定时任务/手动触发 | P0 |
| VG-02 | 指令生成 | 用户发送"生成视频:xxx" | P1 |
| VG-03 | 视频剪辑合并 | 有原始素材时 | P1 |
| VG-04 | 配音合成 | 视频需要配音时 | P2 |
| VG-05 | 字幕添加 | 视频无字幕时 | P2 |
| VG-06 | 多平台适配 | 视频需发布多平台时 | P2 |
| VG-07 | 口型同步视频 | 需要数字人出镜视频 | P1 |

## 工作流

### 热点短视频生成(VG-01)

1. 接收请求→验证topic非空&&duration在15-300秒&&platform支持,失败→VG-ERR-01
2. 如未指定topic→调用趋势发现接口获取TOP3热点,失败→使用默认话题"日常生活"
3. 生成视频脚本→调用内容模板接口,失败→VG-ERR-02使用默认脚本模板
4. **营销策略注入**→调用营销文案接口,输入脚本内容+商品信息→提炼卖点(selling_points)+选择情绪钩子(emotional_hook)+生成CTA话术→注入脚本关键帧(开头钩子/中段卖点/结尾CTA),失败→跳过营销注入,使用原始脚本
5. 钩子结尾图检查→调用配置接口获取钩子结尾卡配置
   - status=unset→提示用户设置 / status=configured→修改分镜最后帧 / status=dismissed→跳过
   - 配置接口不可用→跳过,不阻塞主流程
6. 生成配音→调用TTS引擎(从配置获取voice_config),失败→VG-ERR-03重试3次降级默认音色
7. 调用视频生成接口→**按智能路由决策树选择引擎**(详见下方),失败→VG-ERR-04重试3次
8. 生成字幕→ffmpeg烧录SRT,失败→VG-ERR-05跳过字幕返回无字幕视频
9. 钩子结尾帧注入→image_source="custom"时ffmpeg拼接结尾帧(3秒),失败→跳过不阻塞
10. 质量检查→视频时长≈配音时长(误差<2秒),失败→重新生成
11. 保存到输出目录 + 记录日志,失败→VG-ERR-06
12. (可选)调用发布接口发布

### 口型同步视频(VG-07)

1. 接收请求→验证agent_id存在&&text非空,失败→VG-ERR-08
2. 获取人设外观→从人设配置读取,失败→VG-ERR-08
3. 生成/获取人设图片→检查缓存,无则AI生成,失败→使用默认图片
4. 生成情感语音→调用TTS引擎,失败→VG-ERR-03
5. 提交口型同步→口型同步引擎(主方案)→本地GPU降级方案
6. 轮询等待→每30秒轮询,超时600秒,失败/超时→VG-ERR-09
7. 下载验证→文件大小>0&&时长≈语音时长,失败→VG-ERR-10

## 智能路由决策树

```
视频生成请求到达
│
├─ Step1: 硬约束过滤 → API Key可用性检查 → available_engines
├─ Step2: 一致性需求判断 → agent_id出镜=HIGH / series_id=MEDIUM / 独立=NONE
├─ Step3: 内容类型判断
│   ├─ 数字人出镜 → VG-07口型同步(主引擎→降级引擎)
│   ├─ 角色一致性HIGH → 角色一致性引擎(75-90%) → 降级I2V引擎(70-85%)
│   ├─ AI原创画面 → 画质引擎(1.2元/5秒) → 降级通用引擎
│   ├─ AI风格化 → 风格化引擎 → 降级通用引擎
│   ├─ 真实素材 → 通用引擎(免费) → 降级风格化引擎
│   └─ 不确定 → 默认通用引擎(免费+字幕)
├─ Step4: 成本预算过滤 → free=仅免费引擎 / low=+角色一致性 / unlimited=全部
└─ Step5: 风格偏好注入 → 读取风格配置 → prompt_prefix+video_style+品牌叠加注入
```

### Step5 风格注入详情

1. 读取风格配置文件: 风格关键词映射(科技→technology/专业→professional/温暖→warm/活泼→lively/高端→premium) → prompt_prefix注入 → global_prompt_suffix注入
2. 品牌叠加: overlay_config参数化,从配置读取(位置/透明度/时长/图片URL),替代硬编码

| 场景 | 首选引擎 | 理由 | 降级路径 |
|:-----|:---------|:-----|:---------|
| 连续剧(角色一致性) | 角色一致性引擎 | 75-90%一致性 | I2V引擎→通用引擎 |
| AI原创画面 | 画质引擎 | 画质最好 | 通用引擎→免费引擎 |
| AI风格化 | 风格化引擎 | 模板+一键合成 | 免费引擎 |
| 真实素材 | 通用引擎 | 免费+字幕 | 风格化引擎 |
| 不确定/默认 | 通用引擎 | 免费+降级风险最低 | 无 |
| 预算受限 | 免费引擎 | 均免费 | 无 |
| 数字人出镜 | 口型同步引擎 | 口型同步 | 本地GPU降级 |

## 输入格式

### 生成短视频

```json
{"action": "generate", "agent_id": "agent_001", "topic": "春季穿搭", "duration": 60, "platform": "douyin", "with_subtitle": true}
```

### 生成短视频(场景路由模式)

```json
{"action": "generate", "topic": "春季穿搭", "duration": 60, "platform": "douyin", "scene": "scene_1", "with_subtitle": true}
```

> `scene` 参数: 场景ID(scene_1~scene_7),存在时走场景路由+渲染引擎(7场景+5卡片+降级链+成本预估+配额管理); 不存在时走legacy路径(直接调通用引擎,向后兼容)。
> `duration` 参数: 视频时长(秒),15-300,默认60。
> 配额管理: scene路径会在渲染前检查日/月配额,渲染成功后记录用量。配额用尽返回 VG-ERR-QUOTA。

### 口型同步视频

```json
{"action": "lip_sync_video", "agent_id": "mengyao", "text": "嗨,今天想我了没?", "resolution": "480P", "scene": "咖啡厅"}
```

## 输出格式

```json
{"success": true, "data": {"video_url": "...", "duration": 58, "with_subtitle": true}, "error": null, "code": "VG-SUCCESS-01"}
```

### 输出格式(场景路由模式)

```json
{"success": true, "data": {"video_url": "...", "duration": 58, "with_subtitle": true, "route_metadata": {"scene": "scene_1", "engine_used": "universal_engine", "fallback_applied": false, "fallback_chain_used": [], "cost_estimate": 0}}, "error": null, "code": "VG-SUCCESS-01"}
```

> `route_metadata`: 场景路由元数据,仅scene路径返回。包含scene/engine_used/fallback_applied/fallback_chain_used/cost_estimate。

## 异常处理

| 编号 | 类型 | 触发条件 | 处理方式 |
|:-----|:-----|:---------|:---------|
| VG-ERR-01 | 参数无效 | topic空/duration超范围 | 返回错误,提示正确参数 |
| VG-ERR-02 | 脚本生成失败 | 内容模板接口失败 | 降级使用默认脚本模板 |
| VG-ERR-03 | TTS失败 | TTS引擎失败 | 重试3次→降级默认音色→备用TTS→静默+字幕 |
| VG-ERR-04 | 视频生成失败 | 视频接口返回失败 | 重试3次(间隔2分钟)→3次失败告警 |
| VG-ERR-05 | 字幕烧录失败 | ffmpeg失败 | 跳过字幕,返回无字幕视频 |
| VG-ERR-06 | 记录失败 | 日志写入失败 | 记录日志稍后重试,3次失败告警 |
| VG-ERR-07 | 素材缺失 | 源视频不存在 | 跳过缺失素材,提示补充 |
| VG-ERR-08 | 人设未找到 | agent_id无档案 | 返回错误,提示先初始化人设 |
| VG-ERR-09 | 口型同步失败 | 口型同步接口失败 | 重试2次→告警→检查API额度 |
| VG-ERR-10 | 视频下载失败 | 口型同步视频下载失败 | 重试3次 |
| VG-ERR-11 | 引擎权限不足 | 权限校验失败 | 降级到允许的最高级引擎,记录告警 |
| VG-ERR-12 | 风格配置缺失 | 风格配置未找到 | 使用默认风格(default),不阻塞主流程 |
| VG-ERR-QUOTA | 视频配额已用尽 | 日/月配额达到上限 | 返回配额状态数据,提示升级或等待配额重置 |
| VG-ERR-ROUTE | 场景路由失败 | scene_id无效 | 返回错误,提示检查scene_id |
| VG-ERR-RENDER | 视频渲染失败 | 所有引擎(含降级链)均失败 | 返回错误,记录降级链日志,提示重试或更换场景 |

## TTS降级策略

```
Layer1: 高质量TTS引擎(免费,85%场景) → Layer2: 备用TTS(本地,免费,10%) → Layer3: 静默+字幕(5%)
```

## 依赖关系

- TTS引擎(配音,强依赖) / 内容模板(脚本,强依赖) / 趋势发现(热点,中依赖)
- 人设配置(人设,口型同步强依赖) / 发布接口(发布,弱依赖)

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 |
| TTS引擎 | API | 必需 | 高质量TTS/备用TTS/Edge-TTS三层降级 |
| 视频生成API | API | 必需 | 按智能路由决策树选择引擎 |
| ffmpeg | 工具 | 可选 | 字幕烧录(ffmpeg未安装时跳过字幕) |

### API Key 配置
- **LLM_API_KEY**: 必需(通常由Agent内置) - 脚本生成/营销策略注入
- **TTS_API_KEY**: 可选 - TTS引擎(Edge-TTS免费可用)
- **VIDEO_API_KEY**: 可选 - 视频生成引擎
- 配置方式: 在Agent的环境变量中设置

### 纯Markdown使用说明
TTS降级链最终方案为静默+字幕。通用视频引擎免费。ffmpeg用于字幕烧录,未安装时返回无字幕视频。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 热点短视频生成(VG-01)

**输入**:
```json
{"action": "generate", "agent_id": "agent_001", "topic": "春季穿搭", "duration": 60, "platform": "douyin", "with_subtitle": true}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "video_url": "output/videos/20260701_spring_outfit.mp4",
    "duration": 58,
    "with_subtitle": true,
    "engine_used": "quality_engine",
    "voice_used": "default_voice"
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```

### 示例2: 口型同步视频(VG-07)

**输入**:
```json
{"action": "lip_sync_video", "agent_id": "mengyao", "text": "嗨,今天想我了没?", "resolution": "480P", "scene": "咖啡厅"}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "video_url": "output/videos/20260701_mengyao_lipsync.mp4",
    "duration": 5.2,
    "engine_used": "lip_sync_engine",
    "agent_id": "mengyao"
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```

### 示例3: 引擎权限不足降级(VG-ERR-11)

**输入**: 基础套餐用户请求高级引擎
```json
{"action": "generate", "topic": "产品介绍", "duration": 30, "platform": "xhs"}
```

**输出**: 降级到免费引擎
```json
{
  "success": true,
  "data": {
    "video_url": "output/videos/20260701_product.mp4",
    "duration": 30,
    "engine_used": "universal_engine",
    "downgraded_from": "quality_engine",
    "downgrade_reason": "PERMISSION_DENIED"
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```

### 示例4: 场景路由模式

**输入**: 选择"真实素材视频"场景(scene_1)
```json
{"action": "generate", "topic": "产品介绍", "duration": 30, "platform": "douyin", "scene": "scene_1"}
```

**输出**: 走场景路由+配额管理
```json
{
  "success": true,
  "data": {
    "video_url": "output/videos/20260707_product.mp4",
    "duration": 30,
    "with_subtitle": true,
    "route_metadata": {
      "scene": "scene_1",
      "engine_used": "universal_engine",
      "fallback_applied": false,
      "fallback_chain_used": [],
      "cost_estimate": 0
    }
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```
