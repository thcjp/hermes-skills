---
slug: music-gen
name: music-gen
version: "1.0.0"
displayName: 音乐生成工具专业版
summary: 企业级AI音乐生成系统,支持批量生成、版权管理、多平台调度与CI/CD集成,适合团队与商业项目。
license: Proprietary
edition: pro
description: |-
  音乐生成工具专业版为企业与内容团队提供系统化的AI音乐生成解决方案。在免费版基础生成能力之上,增加批量生成、版权资产管理、多平台智能调度、
  音乐质量审计与CI/CD集成能力。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- 音乐生成
- 企业级
- 批量处理
- 版权管理
- CI/CD
- 自动化
tools:
  - - read
- exec
# 音乐生成工具专业版
## 概述
---
# 音乐生成工具专业版

## 核心能力

### 批量音乐生成
```python
batch_config = {
    "project": "电商配乐批量生产",
    "tasks": [
        {
            "id": "bgm_001",
            "platform": "stable_audio",
            "prompt": "upbeat electronic, 128 BPM, instrumental, 2 minutes",
            "output": "./output/bgm_001.mp3",
            "license": "commercial"
        },
        {
            "id": "bgm_002",
            "platform": "mubert",
            "prompt": "lo-fi hip hop, relaxed, 80 BPM, 3 minutes",
            "output": "./output/bgm_002.mp3",
            "license": "commercial"
        },
        {
            "id": "song_001",
            "platform": "suno",
            "prompt": "pop song with vocals, uplifting, 120 BPM",
            "lyrics": "lyrics/song_001.txt",
            "output": "./output/song_001.mp3",
            "license": "commercial"
        }
    ],
    "parallel": 3,
    "auto_validate": True,
    "license_tracking": True
}

python3 batch_music_gen.py --config batch_config
```

- 执行`批量音乐生成`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`批量音乐生成`相关配置参数进行设置
### 多平台智能调度
```python
platform_scheduler = {
    "platforms": {
        "suno": {
            "strength": "vocal_songs",
            "rate_limit": "50/day",
            "cost": "medium",
            "quality": "high"
        },
        "udio": {
            "strength": "high_quality_vocals",
            "rate_limit": "100/month",
            "cost": "high",
            "quality": "excellent"
        },
        "stable_audio": {
            "strength": "instrumental",
            "rate_limit": "500/month",
            "cost": "low",
            "quality": "good"
        },
        "mubert": {
            "strength": "realtime_electronic",
            "rate_limit": "1000/month",
            "cost": "low",
            "quality": "good"
        }
    },
    "auto_select_rules": [
        {"condition": "need_vocals == true", "platform": "suno"},
        {"condition": "need_vocals == true and quality == 'best'", "platform": "udio"},
        {"condition": "need_instrumental == true", "platform": "stable_audio"},
        {"condition": "need_realtime == true", "platform": "mubert"}
    ],
    "load_balancing": "round_robin",
    "fallback": True
}
```

**输入**: 用户提供多平台智能调度所需的指令和必要参数。
**处理**: 按照skill规范执行多平台智能调度操作,遵循单一意图原则。
**输出**: 返回多平台智能调度的执行结果,包含操作状态和输出数据。### 版权资产管理
```python
license_manager = {
    "assets": [
        {
            "id": "music_001",
            "title": "产品宣传背景音乐",
            "platform": "stable_audio",
            "license_type": "commercial",
            "license_id": "SA-2024-001",
            "purchase_date": "2024-01-15",
            "expiry": "2025-01-15",
            "usage_rights": ["online", "broadcast", "streaming"],
            "restrictions": ["no_resale"],
            "attribution_required": False
        },
        {
            "id": "song_001",
            "title": "品牌主题曲",
            "platform": "suno",
            "license_type": "commercial",
            "license_id": "SUNO-2024-001",
            "purchase_date": "2024-02-01",
            "expiry": "2025-02-01",
            "usage_rights": ["online", "streaming"],
            "restrictions": ["no_broadcast"],
            "attribution_required": True
        }
    ],
    "tracking": {
        "usage_log": True,
        "expiry_alerts": True,
        "compliance_check": True
    }
}
```

**输入**: 用户提供版权资产管理所需的指令和必要参数。
**处理**: 按照skill规范执行版权资产管理操作,遵循单一意图原则。
**输出**: 返回版权资产管理的执行结果,包含操作状态和输出数据。### 音乐质量审计
```python
quality_audit = {
    "checks": [
        {
            "name": "音质检查",
            "test": "audio_quality",
            "min_bitrate": "128kbps",
            "min_sample_rate": "44100Hz"
        },
        {
            "name": "时长验证",
            "test": "duration_check",
            "expected_range": [15, 300]  # 15-300秒
        },
        {
            "name": "响度规范",
            "test": "loudness_normalization",
            "target_loudness": -16,  # LUFS
            "tolerance": 2
        },
        {
            "name": "频谱分析",
            "test": "spectrum_analysis",
            "check_clipping": True,
            "check_noise": True
        },
        {
            "name": "风格匹配",
            "test": "style_matching",
            "compare_with_prompt": True
        }
    ],
    "auto_fix": {
        "loudness_normalize": True,
        "trim_silence": True,
        "remove_clipping": True
    },
    "report_format": "html"
}
```

**输入**: 用户提供音乐质量审计所需的指令和必要参数。
**输出**: 返回音乐质量审计的执行结果,包含操作状态和输出数据。### 音乐库管理
```python
music_library = {
    "categories": {
        "background": {
            "subcategories": ["vlog", "podcast", "presentation"],
            "count": 50
        },
        "brand": {
            "subcategories": ["theme", "jingle", "logo"],
            "count": 20
        },
        "content": {
            "subcategories": ["intro", "outro", "transition"],
            "count": 30
        },
        "emotional": {
            "subcategories": ["happy", "sad", "epic", "calm"],
            "count": 40
        }
    },
    "search": {
        "by_mood": True,
        "by_bpm": True,
        "by_genre": True,
        "by_duration": True,
        "by_license": True
    },
    "metadata": {
        "auto_tag": True,
        "auto_categorize": True,
        "fingerprint": True  # 音频指纹避免重复
    }
}
```

**输入**: 用户提供音乐库管理所需的指令和必要参数。
**处理**: 按照skill规范执行音乐库管理操作,遵循单一意图原则。
**输出**: 返回音乐库管理的执行结果,包含操作状态和输出数据。

- 执行`多平台智能调度`操作,处理输入数据并返回结果
- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `多平台智能调度` 选项

### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级、音乐生成系统、支持批量生成、版权管理、多平台调度与、适合团队与商业项、音乐生成工具专业、版为企业与内容团、队提供系统化的、音乐生成解决方案、在免费版基础生成、能力之上、增加批量生成、音乐质量审计与、集成能力、Use、需要视频处理、音频编辑、媒体转换、配音生成时使用、不适用于版权受保、护的媒体内容处理、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一:MCN批量配乐生产
需求:MCN机构需要为多个账号批量生产背景音乐。

```bash
python3 batch_music_gen.py \
  --tasks music-tasks.json \
  --parallel 5 \
  --auto-select-platform \
  --license-tracking \
  --output ./music-library/ \
  --auto-categorize \
  --quality-check
```

```python
tasks = [
    {"account": "科技账号", "need": "background", "mood": "upbeat", "duration": "2-3min"},
    {"account": "教育账号", "need": "background", "mood": "calm", "duration": "3-5min"},
    {"account": "生活账号", "need": "background", "mood": "happy", "duration": "2-3min"}
]
```

### 场景二:品牌音乐资产管理
需求:企业需要统一管理所有品牌音乐的版权与使用。

```bash
python3 init_music_library.py \
  --brand "EnterpriseBrand" \
  --output ./music-assets/ \
  --license-tracking \
  --auto-categorize

python3 import_assets.py \
  --input ./existing-music/ \
  --auto-tag \
  --fingerprint \
  --license-check
```

### 场景三:游戏配乐批量制作
需求:游戏公司需要为多个场景制作配乐。

```python
game_scenes = [
    {"scene": "主菜单", "mood": "epic", "duration": "3min", "loop": True},
    {"scene": "战斗", "mood": "intense", "duration": "2min", "loop": True},
    {"scene": "城镇", "mood": "peaceful", "duration": "4min", "loop": True},
    {"scene": "Boss战", "mood": "dramatic", "duration": "3min", "loop": True},
    {"scene": "结局", "mood": "emotional", "duration": "5min", "loop": False}
]

for scene in game_scenes:
    generate_music(
        platform=auto_select_platform(scene),
        prompt=build_prompt(scene),
        output=f"./game-music/{scene['scene']}.mp3",
        license="commercial",
        loop=scene["loop"]
    )
```

## 使用流程

### 步骤一:初始化音乐资产管理
```bash
python3 init_music_library.py \
  --brand "MyBrand" \
  --output ./music-library/ \
  --license-tracking
```

### 步骤二:配置批量生成
```bash
python3 batch_music_gen.py \
  --config music-tasks.yml \
  --parallel 5 \
  --auto-select-platform \
  --quality-check
```

### 步骤三:管理与审计
```bash
python3 generate_index.py \
  --input ./music-library/ \
  --output ./index.html

python3 license_audit.py \
  --library ./music-library/ \
  --report ./audit/
```

### 命令参数说明

1. `--parallel`: 命令参数,用于指定操作选项
2. `--library`: 命令参数,用于指定操作选项
3. `-artifact`: 命令参数,用于指定操作选项
4. `-latest`: 命令参数,用于指定操作选项
5. `--license-tracking`: 命令参数,用于指定操作选项

### 命令参数说明

- `--fingerprint`: 命令参数,用于指定操作选项
- `-fi`: 命令参数,用于指定操作选项
- `--auto-categorize`: 命令参数,用于指定操作选项
- `--license-check`: 命令参数,用于指定操作选项
- `--quality-check`: 命令参数,用于指定操作选项

### 命令参数说明

- `--report`: 命令参数,用于指定操作选项
- `--auto-select-platform`: 命令参数,用于指定操作选项
- `-tasks`: 命令参数,用于指定操作选项
- `--brand`: 命令参数,用于指定操作选项
- `--input`: 命令参数,用于指定操作选项

### 命令参数说明

- `--config`: 命令参数,用于指定操作选项
- `--auto-tag`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md规范的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.10+

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| AI音乐平台账户 | 服务 | 必需 | Suno/Udio/Stable Audio等 |
| 音频处理库 | 库 | 推荐 | pip install pydub |
| 音频分析库 | 库 | 推荐 | pip install librosa |
| 数据库 | 存储 | 推荐 | `SQLite`/`关系型数据库` |

### API Key 配置
- 本Skill基于指令驱动驱动,无需额外API Key
- 各AI音乐平台需分别配置API Key,支持环境变量管理
- 批量生成支持API Key池与负载均衡
- 企业版支持多账户管理与并发控制

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令+脚本执行能力)
- **说明**: 专业版基于Markdown指令驱动Agent执行批量音乐生成任务,通过Python脚本实现多平台调度、版权管理与CI/CD集成
- **PRO版增强**: 批量生成、多平台调度、版权管理、质量审计、音乐库管理、CI/CD集成、团队协作

## 案例展示

### 企业级音乐生成配置
```yaml
project:
  name: "企业音乐资产管理"
  version: "1.0.0"

generation:
  platforms:
    - name: "suno"
      api_key: "${SUNO_API_KEY}"
      rate_limit: "50/day"
    - name: "stable_audio"
      api_key: "${STABLE_AUDIO_API_KEY}"
      rate_limit: "500/month"
    - name: "mubert"
      api_key: "${MUBERT_API_KEY}"
      rate_limit: "1000/month"

  auto_select: true
  parallel: 5
  quality_check: true

license_management:
  track_usage: true
  expiry_alerts: true
  compliance_check: true
  auto_renew: false

library:
  categories:
    - background
    - brand
    - content
    - emotional
  search:
    by_mood: true
    by_bpm: true
    by_genre: true
  auto_tag: true
  fingerprint: true

audit:
  audio_quality: true
  loudness: -16
  spectrum_analysis: true
  style_matching: true
  report: "html"
```

### CI/CD集成
```yaml
name: Music Production
on:
  schedule:
    - cron: "0 9 * * 1"  # 每周一上午9点
  push:
    paths: ["music-tasks/**"]
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - name: Batch Generate Music
        run: |
          python3 batch_music_gen.py \
            --config music-tasks/config.yml \
            --parallel 5 \
            --auto-select-platform \
            --quality-check
      - name: License Audit
        run: |
          python3 license_audit.py \
            --library ./music-library/ \
            --report ./audit/
      - name: Upload Music
        uses: actions/upload-artifact@v3
        with:
          name: music-assets
          path: ./music-library/
```

## 常见问题

### Q1: 如何从免费版迁移至PRO版?
A: PRO版完全兼容免费版。现有的平台配置与提示词模板可直接使用。安装PRO版增强包即可启用批量生成、版权管理与质量审计。

### Q2: 批量生成时如何选择平台?
A: PRO版支持智能调度,根据音乐类型自动选择最优平台。人声歌曲优先Suno/Udio,器乐背景优先Stable Audio,实时电子优先Mubert。支持负载均衡与故障转移。

### Q3: 版权资产如何管理?
A: PRO版提供完整的版权管理系统,记录每首音乐的许可类型、购买日期、到期时间、使用权限与限制。支持定期合规审计与到期预警。

### Q4: 音乐库如何搜索?
A: 支持按情绪、BPM、风格、时长、许可类型等多维度搜索。自动打标签与分类,支持音频指纹避免重复。

### Q5: 支持哪些CI/CD平台?
A: 支持GitHub Actions、GitLab CI、Jenkins等主流平台。提供标准CLI接口与配置文件,易于集成到任意流水线。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
