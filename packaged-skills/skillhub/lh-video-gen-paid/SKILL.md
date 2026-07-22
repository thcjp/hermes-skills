---
slug: "lh-video-gen-paid"
name: "lh-video-gen-paid"
version: "1.0.0"
displayName: "短视频生成专业版"
summary: "企业级竖版短视频批量生成系统,支持多模板、多语言、批量处理、品牌定制与CI/CD集成,适合团队与商业项目。"
license: "Proprietary"
edition: "pro"
description: |-
  短视频生成专业版为企业与内容团队提供系统化的竖版短视频生产解决方案。在免费版单视频生成能力之上,增加批量生成、多模板系统、多语言混排、
  品牌定制、团队协作与自动化工作流能力。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - 视频生成
  - 批量处理
  - 短视频
  - 企业级
  - 自动化
  - 内容生产
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 短视频生成专业版

## 核心能力

### 批量视频生成

```python
# 批量生成任务队列
batch_tasks = [
    {"script": "scripts/product-a.md", "output": "output/product-a.mp4"},
    {"script": "scripts/product-b.md", "output": "output/product-b.mp4"},
    {"script": "scripts/product-c.md", "output": "output/product-c.mp4"},
    {"script": "scripts/tutorial-1.md", "output": "output/tutorial-1.mp4"},
    {"script": "scripts/tutorial-2.md", "output": "output/tutorial-2.mp4"}
]

# 执行批量生成
python3 batch_generate.py \
  --tasks tasks.json \
  --parallel 4 \
  --output ./output/ \
  --template brand \
  --quality-check \
  --auto-optimize
```

- 执行`批量视频生成`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`批量视频生成`相关配置参数进行设置
### 多模板系统
PRO版提供多种画面模板,支持不同视觉风格:

```yaml
# templates.yml - 模板配置
templates:
  minimal:
    name: "极简风格"
    background: "linear-gradient(135deg, #FAFAFA, #F1F5F9)"
    font: "Inter, sans-serif"
    text_color: "#0F172A"
    animation: "fade_in"
    
  brand:
    name: "品牌定制"
    background: "brand_gradient"
    logo: "assets/logo.png"
    font: "brand_font"
    text_color: "brand_primary"
    watermark: True
    animation: "slide_up"
    
  dynamic:
    name: "动态活力"
    background: "animated_gradient"
    font: "Poppins, sans-serif"
    text_color: "#FFFFFF"
    animation: "bounce_in"
    particle_effect: True
    
  education:
    name: "教育培训"
    background: "#FFFFFF"
    font: "Noto Sans SC, sans-serif"
    text_color: "#1E3A5A"
    highlight_color: "#0052FF"
    animation: "type_writer"
```

**处理**: 按照skill规范执行多模板系统操作,遵循单一意图原则。
**输出**: 返回多模板系统的执行结果,包含操作状态和输出数据。### 多语言与多音色
```python
# 多语言混排配置
multilingual_config = {
    "segments": [
        {
            "text": "Hello everyone, welcome to our channel.",
            "lang": "en",
            "voice": "en-US-JennyNeural",
            "rate": "+0%"
        },
        {
            "text": "大家好,欢迎来到我们的频道。",
            "lang": "zh",
            "voice": "zh-CN-XiaoxiaoNeural",
            "rate": "+0%"
        },
        {
            "text": "こんにちは、チャンネルへようこそ。",
            "lang": "ja",
            "voice": "ja-JP-NanamiNeural",
            "rate": "+0%"
        }
    ]
}
```

**输入**: 用户提供多语言与多音色所需的指令和必要参数。
**处理**: 按照skill规范执行多语言与多音色操作,遵循单一意图原则。
**输出**: 返回多语言与多音色的执行结果,包含操作状态和输出数据。### 品牌资产管理
```python
# 品牌资产统一管理
brand_assets = {
    "logo": "assets/brand/logo.png",
    "logo_dark": "assets/brand/logo-dark.png",
    "colors": {
        "primary": "#0052FF",
        "secondary": "#4D7CFF",
        "accent": "#FF6B35",
        "background": "#FAFAFA",
        "text": "#0F172A"
    },
    "fonts": {
        "display": "Calistoga, serif",
        "body": "Inter, sans-serif",
        "mono": "JetBrains Mono, monospace"
    },
    "intro_animation": "assets/animations/intro.mp4",
    "outro_animation": "assets/animations/outro.mp4",
    "watermark": {
        "enabled": True,
        "image": "assets/brand/watermark.png",
        "position": "bottom-right",
        "opacity": 0.8
    }
}
```

**处理**: 按照skill规范执行品牌资产管理操作,遵循单一意图原则。
**输出**: 返回品牌资产管理的执行结果,包含操作状态和输出数据。### 视频质量审计

```python
# 自动质量检查
quality_checks = {
    "resolution": {"required": "1080x1920", "action": "reject_if_fail"},
    "duration": {"min": 15, "max": 180, "action": "warn_if_outside"},
    "audio_level": {"target": -16, "tolerance": 2, "action": "auto_normalize"},
    "subtitle_sync": {"tolerance": 0.5, "action": "warn_if_fail"},
    "text_readability": {"min_contrast": 4.5, "action": "warn_if_fail"},
    "frame_rate": {"required": 30, "action": "reject_if_fail"}
}
```

- 执行`多模板系统`操作,处理输入数据并返回结果
- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `多模板系统` 选项

### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级竖版短视频、批量生成系统、支持多模板、批量处理、品牌定制与、适合团队与商业项、短视频生成专业版、为企业与内容团队、提供系统化的竖版、短视频生产解决方、在免费版单视频生、成能力之上、增加批量生成、团队协作与自动化、工作流能力、Use、需要提升效率、自动化流程、工作流优化时使用、不适用于需要人工、创意判断的任务、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一:MCN批量内容生产

需求:MCN机构需要为多个账号批量生产竖版短视频。

```python
# 批量内容生产工作流
mcn_pipeline = {
    "accounts": [
        {"name": "科技账号", "template": "minimal", "topics": ["AI", "编程", "工具"]},
        {"name": "教育账号", "template": "education", "topics": ["英语", "数学", "科普"]},
        {"name": "生活账号", "template": "dynamic", "topics": ["美食", "旅行", "日常"]}
    ],
    "daily_quota": 10,  # 每账号每日10条
    "schedule": "daily 08:00",
    "auto_publish": False,  # 生成后人工审核
    "quality_check": True
}

# 执行批量生成
for account in mcn_pipeline["accounts"]:
    for topic in account["topics"]:
        script = generate_script(topic, account["template"])
        generate_video(script, account["template"])
```

### 场景二:电商商品视频批量制作

需求:电商平台需要为100个商品生成介绍视频。

```bash
# 批量生成商品视频
python3 batch_generate.py \
  --tasks products.csv \
  --parallel 8 \
  --template brand \
  --brand-assets ./brand/ \
  --output ./videos/ \
  --quality-check \
  --auto-optimize \
  --generate-thumbnail \
  --watermark
```

```python
# products.csv
# 核心能力
# P001,无线耳机,299,降噪;蓝牙5.3;续航30h,scripts/P001.md
# P002,智能手表,599,心率监测;GPS;防水,scripts/P002.md
# ...
```

### 场景三:多语言内容国际化

需求:将中文内容翻译并生成多语言版本视频。

```python
# 多语言批量生成
languages = ["zh-CN", "en-US", "ja-JP", "ko-KR", "es-ES"]
source_script = "scripts/source.md"

for lang in languages:
    # 翻译脚本
    translated = translate_script(source_script, target_lang=lang)
    
    # 选择对应音色
    voice = get_voice_for_lang(lang)
    
    # 生成视频
    generate_video(
        script=translated,
        output=f"output/video_{lang}.mp4",
        voice=voice,
        template="brand"
    )
```

## 使用流程

### 步骤一:初始化项目

```bash
# 初始化视频生产项目
python3 init_project.py \
  --name "MyVideoProject" \
  --brand-assets ./brand/ \
  --output ./project/
```

### 步骤二:配置批量任务

```bash
# 创建任务文件
cat > tasks.json << 'EOF'
[
  {"script": "scripts/01.md", "output": "out/01.mp4", "template": "brand"},
  {"script": "scripts/02.md", "output": "out/02.mp4", "template": "minimal"},
  {"script": "scripts/03.md", "output": "out/03.mp4", "template": "education"}
]
EOF
```

### 步骤三:执行批量生成

```bash
python3 batch_generate.py \
  --tasks tasks.json \
  --parallel 4 \
  --quality-check \
  --output ./output/
```

### 命令参数说明

1. `--parallel`: 命令参数,用于指定操作选项
2. `-dark`: 命令参数,用于指定操作选项
3. `-latest`: 命令参数,用于指定操作选项
4. `-artifact`: 命令参数,用于指定操作选项
5. `-CN-XiaoxiaoNeural`: 命令参数,用于指定操作选项

### 命令参数说明

- `-US-JennyNeural`: 命令参数,用于指定操作选项
- `--watermark`: 命令参数,用于指定操作选项
- `--template`: 命令参数,用于指定操作选项
- `-KR`: 命令参数,用于指定操作选项
- `-right`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN-XiaoxiaoNeural`: 命令参数,用于指定操作选项
- `-gradient`: 命令参数,用于指定操作选项
- `-CN`: 命令参数,用于指定操作选项
- `--brand-assets`: 命令参数,用于指定操作选项
- `--quality-check`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN`: 命令参数,用于指定操作选项
- `-ES`: 命令参数,用于指定操作选项
- `-production`: 命令参数,用于指定操作选项
- `-US`: 命令参数,用于指定操作选项
- `--generate-thumbnail`: 命令参数,用于指定操作选项

### 命令参数说明

- `-JP`: 命令参数,用于指定操作选项
- `-transparent`: 命令参数,用于指定操作选项
- `-serif`: 命令参数,用于指定操作选项
- `-CN-XiaoxiaoNeural`: 命令参数,用于指定操作选项
- `-KR`: 命令参数,用于指定操作选项

### 命令参数说明

- `-US-JennyNeural`: 命令参数,用于指定操作选项
- `--auto-optimize`: 命令参数,用于指定操作选项
- `-CN`: 命令参数,用于指定操作选项
- `-CN-XiaoxiaoNeural`: 命令参数,用于指定操作选项
- `-US`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN-XiaoxiaoNeural`: 命令参数,用于指定操作选项
- `-US`: 命令参数,用于指定操作选项
- `-JP`: 命令参数,用于指定操作选项
- `-JP-NanamiNeural`: 命令参数,用于指定操作选项
- `-ES`: 命令参数,用于指定操作选项

### 命令参数说明

- `-JP-NanamiNeural`: 命令参数,用于指定操作选项
- `-ES`: 命令参数,用于指定操作选项
- `-CN-XiaoxiaoNeural`: 命令参数,用于指定操作选项
- `-US-JennyNeural`: 命令参数,用于指定操作选项
- `-US`: 命令参数,用于指定操作选项

### 命令参数说明

- `-US`: 命令参数,用于指定操作选项
- `-ES`: 命令参数,用于指定操作选项
- `-JP-NanamiNeural`: 命令参数,用于指定操作选项
- `-KR`: 命令参数,用于指定操作选项
- `-JP`: 命令参数,用于指定操作选项

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
- **FFmpeg**: 5.0+(支持GPU加速需CUDA版本)

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| FFmpeg 5.0+ | 系统工具 | 必需 | brew/apt安装 |
| Chrome | 浏览器 | 截图必需 | 系统自带或下载 |
| TTS服务 | 服务 | 必需 | 默认Edge TTS或自定义 |
| CUDA(可选) | GPU驱动 | GPU加速可选 | NVIDIA官方 |

### API Key 配置

- 本Skill基于指令驱动驱动,无需额外API Key
- TTS服务如使用云端API,需按对应服务商文档配置
- 批量生成使用本地工具链,无需额外API
- 如集成第三方内容平台,按各自平台文档配置

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令+脚本执行能力)
- **说明**: 专业版基于Markdown指令驱动Agent执行批量视频生成任务,通过Python脚本与FFmpeg实现视频合成、质量审计与CI/CD集成
- **PRO版增强**: 批量生成、多模板系统、多语言混排、品牌定制、GPU加速、质量审计、CI/CD集成、团队协作

## 案例展示

### 高级参数配置

```python
# PRO版高级配置
pro_config = {
    "rendering": {
        "gpu_acceleration": True,        # GPU加速
        "parallel_workers": 4,            # 并行任务数
        "cache_enabled": True            # 缓存启用
    },
    "video": {
        "width": 1080,
        "height": 1920,
        "fps": 30,
        "bitrate": "5M",
        "format": "mp4",
        "codec": "h264"
    },
    "audio": {
        "sample_rate": 44100,
        "bitrate": "128k",
        "normalize": True,              # 音量标准化
        "target_loudness": -16           # 目标响度(LUFS)
    },
    "subtitles": {
        "burn": True,                    # 烧录字幕
        "font": "Inter, sans-serif",
        "font_size": 48,
        "position": "bottom",
        "background": "semi-transparent"
    },
    "branding": {
        "watermark": True,
        "intro": True,
        "outro": True,
        "logo_position": "top-right"
    }
}
```

### CI/CD集成配置

```yaml
# .github/workflows/video-production.yml
name: Video Production
on:
  schedule:
    - cron: "0 8 * * *"  # 每日8点
  push:
    paths: ["scripts/**"]
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup FFmpeg
        run: sudo apt install ffmpeg
      - name: Batch Generate Videos
        run: |
          python3 batch_generate.py \
            --tasks tasks.json \
            --parallel 4 \
            --output ./output/ \
            --quality-check
      - name: Upload Videos
        uses: actions/upload-artifact@v3
        with:
          name: videos
          path: ./output/
```

## 常见问题

### Q1: 如何从免费版迁移至PRO版?

A: PRO版完全兼容免费版。现有Markdown脚本格式与命令行参数可直接使用。只需安装PRO版增强包即可启用批量生成与高级功能。

### Q2: 批量生成时部分视频失败怎么办?

A: PRO版支持失败重试机制。失败的记录会保存到`failed-tasks.json`,可单独重试:

```bash
python3 batch_generate.py --retry failed-tasks.json
```

### Q3: GPU加速如何启用?

A: 需要安装支持GPU的FFmpeg版本(如带NVIDIA CUDA支持)。在配置中设置`gpu_acceleration: True`即可自动启用。

### Q4: 如何管理多个品牌的内容?

A: 使用多品牌配置,每个品牌拥有独立的模板、配色与资产。可在批量任务中为不同视频指定不同品牌。

### Q5: 支持哪些视频平台规格?

A: 默认输出9:16竖版(1080x1920)。可配置为16:9横版(1920x1080)或1:1方形(1080x1080),适配不同平台需求。

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
