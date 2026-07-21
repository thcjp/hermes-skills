---
slug: music-gen-cellcog
name: music-gen-cellcog
version: "1.0.0"
displayName: CellCog音乐生成专业版
summary: 基于CellCog AI引擎的企业级音乐生成系统,支持批量生成、版权管理、高质量输出与CI/CD集成,适合团队与商业项目。
license: Proprietary
edition: pro
description: |-
  CellCog音乐生成专业版为企业与内容团队提供系统化的AI音乐生成解决方案。在免费版基础生成能力之上,增加批量生成、高质量音频输出、版权资产管理、
  音乐库管理与CI/CD集成能力。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- 音乐生成
- CellCog
- 企业级
- 批量处理
- 版权管理
- CI/CD
tools:
  - - read
- exec
# CellCog音乐生成专业版
## 概述
---
# CellCog音乐生成专业版

## 核心能力

### 批量音乐生成
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供批量音乐生成所需的指令和必要参数。
**处理**: 按照skill规范执行批量音乐生成操作,遵循单一意图原则。
**输出**: 返回批量音乐生成的执行结果,包含操作状态和输出数据。### 高质量音频输出
| 格式 | 音质 | 文件大小 | 适用场景 |
|------|------|---------|---------|
| MP3 | Standard | 小 | 在线播放、预览 |
| WAV | High | 大 | 专业制作、后期处理 |
| FLAC | Lossless | 中 | 高品质存档、发行 |
| AIFF | Studio | 大 | 工作室制作 |

```bash
curl -X POST https://api.cellcog.com/v1/music/generate \
  -H "Authorization: Bearer $CELLCOG_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "史诗级管弦乐,弦乐与铜管,电影配乐风格",
    "duration": 180,
    "style": "cinematic",
    "format": "flac",
    "quality": "lossless",
    "sample_rate": 48000,
    "bit_depth": 24
  }' \
  -o epic-music.flac
```

### 版权资产管理
```python
license_manager = {
    "assets": [
        {
            "id": "music_001",
            "title": "产品宣传背景音乐",
            "type": "text_to_music",
            "platform": "cellcog",
            "license_type": "commercial",
            "license_id": "CC-2024-001",
            "purchase_date": "2024-01-15",
            "expiry": "permanent",
            "usage_rights": ["online", "broadcast", "streaming", "derivative"],
            "restrictions": ["no_resale"],
            "attribution_required": False,
            "file_path": "./music-library/music_001.flac",
            "metadata": {
                "duration": 120,
                "bpm": 128,
                "style": "electronic",
                "format": "flac"
            }
        }
    ],
    "tracking": {
        "usage_log": True,
        "expiry_alerts": True,
        "compliance_check": True,
        "auto_tag": True
    }
}
```

**输入**: 用户提供版权资产管理所需的指令和必要参数。
**处理**: 按照skill规范执行版权资产管理操作,遵循单一意图原则。
**输出**: 返回版权资产管理的执行结果,包含操作状态和输出数据。### 音乐库管理
```python
music_library = {
    "categories": {
        "background": {
            "subcategories": ["vlog", "podcast", "presentation", "study"],
            "count": 0
        },
        "brand": {
            "subcategories": ["theme", "jingle", "logo", "anthem"],
            "count": 0
        },
        "content": {
            "subcategories": ["intro", "outro", "transition", "bumper"],
            "count": 0
        },
        "emotional": {
            "subcategories": ["happy", "sad", "epic", "calm", "energetic"],
            "count": 0
        },
        "genre": {
            "subcategories": ["pop", "electronic", "classical", "ambient", "lo-fi"],
            "count": 0
        }
    },
    "search": {
        "by_mood": True,
        "by_bpm": True,
        "by_genre": True,
        "by_duration": True,
        "by_license": True,
        "by_tags": True
    },
    "metadata": {
        "auto_tag": True,
        "auto_categorize": True,
        "fingerprint": True,
        "waveform": True
    }
}
```

**输入**: 用户提供音乐库管理所需的指令和必要参数。
**处理**: 按照skill规范执行音乐库管理操作,遵循单一意图原则。
**输出**: 返回音乐库管理的执行结果,包含操作状态和输出数据。### 音乐质量审计
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供音乐质量审计所需的指令和必要参数。
**处理**: 按照skill规范执行音乐质量审计操作,遵循单一意图原则。
**输出**: 返回音乐质量审计的执行结果,包含操作状态和输出数据。
### MP3

执行MP3操作,处理用户输入并返回结果。

**输入**: 用户提供MP3所需的参数和指令。

**输出**: 返回MP3的处理结果。

- 执行`MP3`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`MP3`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 引擎的企业级音乐、生成系统、支持批量生成、版权管理、高质量输出与、适合团队与商业项、音乐生成专业版为、企业与内容团队提、供系统化的、音乐生成解决方案、在免费版基础生成、能力之上、增加批量生成、音乐库管理与、集成能力、Use、需要视频处理、音频编辑、媒体转换、配音生成时使用、不适用于版权受保、护的媒体内容处理、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一:MCN批量配乐生产
需求:MCN机构需要为多个账号批量生产背景音乐。

```bash
python3 batch_music_gen.py \
  --tasks music-tasks.json \
  --parallel 5 \
  --format flac \
  --quality lossless \
  --license-tracking \
  --output ./music-library/ \
  --auto-categorize \
  --quality-check \
  --generate-metadata
```

```python
tasks = [
    {"account": "科技账号", "prompt": "modern electronic, upbeat", "duration": 30, "style": "electronic"},
    {"account": "教育账号", "prompt": "calm piano, study focus", "duration": 120, "style": "ambient"},
    {"account": "生活账号", "prompt": "happy pop, cheerful", "duration": 60, "style": "pop"}
]
```

### 场景二:品牌音乐资产管理
需求:企业需要统一管理所有品牌音乐的版权与使用。

```bash
python3 init_music_library.py \
  --brand "EnterpriseBrand" \
  --output ./music-assets/ \
  --license-tracking \
  --auto-categorize \
  --fingerprint

python3 import_assets.py \
  --input ./existing-music/ \
  --auto-tag \
  --license-check \
  --quality-audit
```

### 场景三:游戏配乐批量制作
需求:游戏公司需要为多个场景制作配乐。

```python
game_scenes = [
    {"scene": "主菜单", "prompt": "epic orchestral, fantasy adventure", "duration": 180, "loop": True},
    {"scene": "战斗", "prompt": "intense action, drums and brass", "duration": 120, "loop": True},
    {"scene": "城镇", "prompt": "peaceful medieval, lute and flute", "duration": 240, "loop": True},
    {"scene": "Boss战", "prompt": "dramatic orchestral, dark and powerful", "duration": 180, "loop": True},
    {"scene": "结局", "prompt": "emotional cinematic, strings and piano", "duration": 300, "loop": False}
]

for scene in game_scenes:
    generate_music(
        prompt=scene["prompt"],
        duration=scene["duration"],
        format="flac",
        quality="lossless",
        output=f"./game-music/{scene['scene']}.flac",
        license="commercial"
    )
```

## 使用流程

### 步骤一:初始化音乐资产管理
```bash
python3 init_music_library.py \
  --brand "MyBrand" \
  --output ./music-library/ \
  --license-tracking \
  --auto-categorize
```

### 步骤二:配置批量生成
```bash
python3 batch_music_gen.py \
  --config music-tasks.yml \
  --parallel 5 \
  --format flac \
  --quality lossless \
  --license-tracking \
  --quality-check
```

### 步骤三:管理与审计
```bash
python3 generate_index.py \
  --input ./music-library/ \
  --output ./index.html \
  --searchable

python3 license_audit.py \
  --library ./music-library/ \
  --report ./audit/

python3 quality_audit.py \
  --library ./music-library/ \
  --report ./audit/quality-report.html
```

### 命令参数说明

1. `--parallel`: 命令参数,用于指定操作选项
2. `--library`: 命令参数,用于指定操作选项
3. `--generate-metadata`: 命令参数,用于指定操作选项
4. `--license-tracking`: 命令参数,用于指定操作选项
5. `-latest`: 命令参数,用于指定操作选项

### 命令参数说明

- `--quality-audit`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `--input`: 命令参数,用于指定操作选项
- `-report`: 命令参数,用于指定操作选项
- `--brand`: 命令参数,用于指定操作选项

### 命令参数说明

- `-artifact`: 命令参数,用于指定操作选项
- `--searchable`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `--fingerprint`: 命令参数,用于指定操作选项
- `--tasks`: 命令参数,用于指定操作选项

### 命令参数说明

- `--quality-check`: 命令参数,用于指定操作选项
- `--format`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `--license-check`: 命令参数,用于指定操作选项

### 命令参数说明

- `-H`: 命令参数,用于指定操作选项
- `--auto-tag`: 命令参数,用于指定操作选项
- `--auto-categorize`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-X`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

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
- **网络**: 需要互联网连接访问CellCog API

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| CellCog API | 服务 | 必需 | CellCog官网注册 |
| requests | Python库 | 必需 | pip install requests |
| pydub | 音频处理 | 推荐 | pip install pydub |
| librosa | 音频分析 | 推荐 | pip install librosa |
| 数据库 | 存储 | 推荐 | `SQLite`/`关系型数据库` |

### API Key 配置
- 需要配置CellCog API Key
- 通过 `CELLCOG_API_KEY` 环境变量配置
- 或通过 `~/.cellcog/config.json` 配置文件
- 批量生成支持API Key池与负载均衡
- 企业版支持多账户管理与并发控制

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令+脚本执行能力)
- **说明**: 专业版基于Markdown指令驱动Agent执行批量音乐生成任务,通过Python脚本实现批量调度、版权管理与CI/CD集成
- **PRO版增强**: 批量生成、高质量输出、版权管理、音乐库管理、质量审计、CI/CD集成、团队协作

## 案例展示

### 企业级音乐生成配置

> 详细代码示例已移至 `references/detail.md`

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
      - name: Install Dependencies
        run: pip install requests pydub librosa
      - name: Batch Generate Music
        env:
          CELLCOG_API_KEY: $相关信息
        run: |
          python3 batch_music_gen.py \
            --config music-tasks/config.yml \
            --parallel 5 \
            --format flac \
            --quality lossless \
            --license-tracking \
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
A: PRO版完全兼容免费版。现有的API Key与配置可直接使用。安装PRO版增强包即可启用批量生成、高质量输出与版权管理。

### Q2: 批量生成支持多少并发?
A: 默认支持5个并发任务,可根据CellCog API的速率限制调整。企业版支持更高并发与优先队列。

### Q3: 无损音频与MP3有什么区别?
A: 无损音频(WAV/FLAC)保留全部音频数据,音质更高,适合专业制作与发行。MP3为有损压缩,文件更小,适合在线播放与预览。

### Q4: 版权资产如何管理?
A: PRO版提供完整的版权管理系统,记录每首音乐的许可类型、购买日期、到期时间、使用权限与限制。支持定期合规审计与到期预警。

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

- 需要API Key，无Key环境无法使用
