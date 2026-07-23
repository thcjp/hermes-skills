---
slug: "music-gen-tool-pro"
name: "music-gen-tool-pro"
version: "1.0.0"
displayName: "音乐生成工具专业版"
summary: "企业级AI音乐生成系统,支持批量生成、版权管理、多平台调度与CI/CD集成,适合团队与商业项目。"
license: "Proprietary"
edition: "pro"
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
homepage: "https://skillhub.cn"
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

音乐生成工具专业版为企业与内容团队提供系统化的AI音乐生成解决方案。在免费版基础生成能力之上,PRO版增加批量生成、版权资产管理、多平台智能调度、音乐质量审计与CI/CD集成能力,满足商业级音乐生产的效率与合规需求。

PRO版完全兼容免费版,可直接继承免费版的平台配置与提示词模板,并在此基础上扩展为完整的音乐生产系统。

## 核心能力
### 批量音乐生成
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| input | string | 是 | 音乐生成工具专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

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

**输入**: 用户提供批量音乐生成所需的指令和必要参数。
**处理**: 解析批量音乐生成的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回批量音乐生成的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

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
**处理**: 解析多平台智能调度的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回多平台智能调度的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 版权资产管理
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
**处理**: 解析版权资产管理的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回版权资产管理的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 音乐质量审计
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
**处理**: 解析音乐质量审计的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回音乐质量审计的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 音乐库管理
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
**处理**: 解析音乐库管理的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回音乐库管理的响应数据,包含状态码、结果和日志。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、音乐生成系统、支持批量生成、版权管理、多平台调度与、适合团队与商业项、音乐生成工具专业、版为企业与内容团、队提供系统化的、音乐生成解决方案、在免费版基础生成、能力之上、增加批量生成、版权资产管理、多平台智能调度、音乐质量审计与、集成能力、Use、when、需要视频处理、音频编辑、媒体转换、配音生成时使用、不适用于版权受保、护的媒体内容处理、适用于独立开发者、企业团队和自动化、工作流场景等。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
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

## 快速开始
### Step 1:初始化音乐资产管理
```bash
python3 init_music_library.py \
  --brand "MyBrand" \
  --output ./music-library/ \
  --license-tracking
```

### Step 2:配置批量生成
```bash
python3 batch_music_gen.py \
  --config music-tasks.yml \
  --parallel 5 \
  --auto-select-platform \
  --quality-check
```

### Step 3:管理与审计
```bash
python3 generate_index.py \
  --input ./music-library/ \
  --output ./index.html

python3 license_audit.py \
  --library ./music-library/ \
  --report ./audit/
```

## 示例
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

## 最佳实践
### 免费版与PRO版能力对比
| 能力维度 | 免费版 | PRO版 |
|---------|--------|-------|
| 生成方式 | 单个手动 | 批量+任务队列 |
| 平台选择 | 手动选择 | 智能调度+负载均衡 |
| 版权管理 | 注意事项指南 | 完整资产追踪系统 |
| 质量审计 | 不支持 | 自动审计+报告 |
| 音乐库 | 不支持 | 分类管理+搜索 |
| 并行处理 | 不支持 | 多任务并行 |
| 团队协作 | 单人 | 多人+版本管理 |
| 音频指纹 | 不支持 | 避免重复 |
| CI/CD | 不支持 | 流水线集成 |

### 平台选择策略
| 需求 | 推荐平台 | 原因 |
|------|---------|------|
| 流行歌曲(含人声) | Suno | 综合表现最佳 |
| 高品质人声歌曲 | Udio | 音质优秀 |
| 纯器乐背景 | Stable Audio | 性价比高 |
| 实时电子音乐 | Mubert | 适合直播 |
| 可编辑结构 | Soundraw | 灵活编辑 |

### 版权管理最佳实践
```python
license_workflow = {
    "purchase": {
        "record_license": True,      # 记录许可
        "store_receipt": True,       # 存储凭证
        "set_expiry": True           # 设置到期提醒
    },
    "usage": {
        "track_usage": True,         # 追踪使用
        "log_platform": True,        # 记录使用平台
        "check_rights": True         # 使用前检查权限
    },
    "compliance": {
        "regular_audit": True,       # 定期审计
        "expiry_alerts": True,       # 到期预警
        "auto_renew_check": True    # 自动续费检查
    }
}
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

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md规范的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.10+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| AI音乐平台账户 | 服务 | 必需 | Suno/Udio/Stable Audio等 |
| 音频处理库 | 库 | 推荐 | pip install pydub |
| 音频分析库 | 库 | 推荐 | pip install librosa |
| 数据库 | 存储 | 推荐 | `SQLite`/`PostgreSQL` |

### API Key 配置
- 本skill基于Markdown指令规范驱动,无需额外API Key
- 各AI音乐平台需分别配置API Key,支持环境变量管理
- 批量生成支持API Key池与负载均衡
- 企业版支持多账户管理与并发控制

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令+脚本执行能力)
- **说明**: 专业版基于Markdown指令驱动Agent执行批量音乐生成任务,通过Python脚本实现多平台调度、版权管理与CI/CD集成
- **PRO版增强**: 批量生成、多平台调度、版权管理、质量审计、音乐库管理、CI/CD集成、团队协作

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "音乐生成工具专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "music gen pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
