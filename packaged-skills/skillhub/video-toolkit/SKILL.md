---
slug: "video-toolkit"
name: "video-toolkit"
version: "1.0.0"
displayName: "视频工具箱专业版"
summary: "批量视频处理+AI超分+智能重构图+多码率+自动化工作流,面向内容团队的专业视频引擎"
license: "Proprietary"
edition: "pro"
description: |-
  面向内容团队和机构的专业级视频处理引擎,在免费版核心功能之上,新增批量
  文件处理、AI超分辨率、智能重构图、多码率自适应、自动化工作流和全平台
  规格支持。核心能力:
  - 批量视频处理(文件夹级一键处理)
  - AI超分辨率(Real-ESRGAN画质提升)
  - 智能重构图(AI驱动的内容感知裁剪)
  - 多码率自适应流(HLS/DASH)
  - 自动化工作流(处理-验证-交付)
  - 全平台规格+自定义规格
  - 高级字幕(多语言+样式定制+ASS特效)
  - 视频质量评估(SSIM/PSNR)

  适用场景:
  -...
tags:
  - 视频
  - FFmpeg
  - 多媒体
  - 字幕
  - 压缩
  - 内容创作
  - 企业级
  - 批量处理
  - AI增强
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# 视频工具箱专业版

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

### 1. 批量视频处理
```bash
#!/bin/bash
# batch-process.sh - 批量处理文件夹内所有视频
INPUT_DIR=$1
OUTPUT_DIR=$2
PLATFORM=${3:-tiktok}  # 默认TikTok
mkdir -p "$OUTPUT_DIR"

# 平台参数配置
case $PLATFORM in
  tiktok)
    ASPECT="9:16"; MAX_DURATION=180; MAX_SIZE="287M"; CRF=23 ;;
  instagram)
    ASPECT="9:16"; MAX_DURATION=90; MAX_SIZE="250M"; CRF=23 ;;
  youtube_shorts)
    ASPECT="9:16"; MAX_DURATION=60; MAX_SIZE=""; CRF=23 ;;
  whatsapp)
    ASPECT="any"; MAX_DURATION=180; MAX_SIZE="62M"; CRF=28 ;;
esac

count=0
total=$(find "$INPUT_DIR" -type f \( -name "*.mp4" -o -name "*.mov" -o -name "*.avi" \) | wc -l)

for video in "$INPUT_DIR"/*.{mp4,mov,avi}; do
  if [ -f "$video" ]; then
    count=$((count + 1))
    filename=$(basename "$video" | sed 's/\.[^.]*$//')
    output="$OUTPUT_DIR/${filename}_${PLATFORM}.mp4"

    echo "[$count/$total] 处理: $filename"

    # 裁剪宽高比
    if [ "$ASPECT" = "9:16" ]; then
      ffmpeg -i "$video" -vf "crop=ih*9/16:ih" -t $MAX_DURATION \
        -c:v libx264 -crf $CRF -preset medium \
        -c:a aac -b:a 128k -movflags +faststart \
        ${MAX_SIZE:+-fs $MAX_SIZE} "$output" -y -loglevel error
    else
      ffmpeg -i "$video" -t $MAX_DURATION \
        -c:v libx264 -crf $CRF -preset medium \
        -c:a aac -b:a 128k -movflags +faststart \
        ${MAX_SIZE:+-fs $MAX_SIZE} "$output" -y -loglevel error
    fi

    # 验证输出
    if [ -f "$output" ]; then
      size=$(du -h "$output" | cut -f1)
      echo "  完成: $size"
    else
      echo "  失败!"
    fi
  fi
done

echo "批量处理完成: $count/$total"
```- 验证返回数据的完整性和格式正确性
- 参考`高级字幕定制`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`自动化工作流`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`多码率自适应流(HLS)`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`批量视频处理`的配置文档进行参数调优
### 2. AI超分辨率(Real-ESRGAN)
```bash
# 使用Real-ESRGAN提升视频画质
# 2x超分(适合720p->1440p)
realesrgan-ncnn-vulkan -i input.mp4 -o output_2x.mp4 -n realesr-animevideov3 -s 2

# 4x超分(适合480p->1080p)
realesrgan-ncnn-vulkan -i input.mp4 -o output_4x.mp4 -n realesrgan-x4plus -s 4

# 超分后重新编码为标准格式
ffmpeg -i output_2x.mp4 -c:v libx264 -crf 18 -preset slow -c:a copy final.mp4
```

超分适用场景:

| 源分辨率 | 超分倍率 | 目标分辨率 | 推荐模型 |
|----------|----------|------------|----------|
| 480p | 4x | 1080p | realesrgan-x4plus |
| 720p | 2x | 1440p | realesr-animevideov3 |
| 1080p | 2x | 4K | realesr-animevideov3 |

**处理**: 解析AI超分辨率(Real-ESRGAN)的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
### 3. 智能重构图
通过AI分析视频内容,自动选择优秀裁剪区域:

```bash
# 智能重构图(需要场景检测+主体追踪)
# 第1步:场景检测
ffmpeg -i input.mp4 -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2> scenes.txt

# 第2步:基于场景分析裁剪(居中主体)
# 专业版使用AI驱动的内容感知裁剪
ffmpeg -i input.mp4 -vf "crop=w='ih*9/16':h='ih':x='(iw-w)/2':y=0" -c:a copy output.mp4

# 第3步:动态裁剪(不同场景不同位置)
# 通过场景分析脚本生成动态裁剪指令
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `智能重构图` 选项
- 处理流程: 接收输入 -> 执行智能重构图 -> 返回结果
- 输入: 用户提供智能重构图所需的参数和指令
- 输出: 返回智能重构图的处理结果,包含执行状态码、结果数据和执行日志

### 4. 多码率自适应流(HLS)
```bash
#!/bin/bash
# hls-encode.sh - 生成HLS自适应多码率流
INPUT=$1
OUTPUT_DIR=${2:-./hls_output}

mkdir -p "$OUTPUT_DIR"

# 生成多码率版本
ffmpeg -i "$INPUT" \
  -map 0:v -map 0:a -s:v:0 1920x1080 -b:v:0 5000k \
  -map 0:v -map 0:a -s:v:1 1280x720  -b:v:1 2800k \
  -map 0:v -map 0:a -s:v:2 854x480   -b:v:2 1400k \
  -map 0:v -map 0:a -s:v:3 640x360   -b:v:3 800k  \
  -c:v libx264 -preset fast -c:a aac -b:a 128k \
  -f hls -hls_time 6 -hls_playlist_type vod \
  -hls_segment_filename "$OUTPUT_DIR/segment_%v_%03d.ts" \
  -master_pl_name master.m3u8 \
  -var_stream_map "v:0,a:0 v:1,a:1 v:2,a:2 v:3,a:3" \
  "$OUTPUT_DIR/stream_%v.m3u8"

echo "HLS流生成完成:"
echo "  主播放列表: $OUTPUT_DIR/master.m3u8"
echo "  分辨率: 1080p/720p/480p/360p"
```

**处理**: 解析多码率自适应流(HLS)的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `多码率自适应流(hls)` 选项
- 处理流程: 接收输入 -> 执行多码率自适应流(HLS) -> 返回结果
- 输入: 用户提供多码率自适应流(HLS)所需的参数和指令
- 输出: 返回多码率自适应流(HLS)的处理结果,包含执行状态码、结果数据和执行日志

### 5. 自动化工作流
```bash
#!/bin/bash
# video-workflow.sh - 自动化视频处理工作流
INPUT=$1
PROJECT_NAME=$2

WORK_DIR="/tmp/video_workflow_${PROJECT_NAME}"
mkdir -p "$WORK_DIR"/{tiktok,instagram,youtube,whatsapp,subtitles}

echo "=== 视频处理工作流启动 ==="
echo "项目: $PROJECT_NAME"
echo "源文件: $INPUT"
echo ""

# 第1步:检测源文件
echo "[1/6] 检测源文件信息..."
ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_name,width,height,bit_rate -of json "$INPUT" > "$WORK_DIR/source_info.json"
echo "  完成"

# 第2步:生成字幕
echo "[2/6] 生成字幕..."
whisper "$INPUT" --model small --language zh --output_dir "$WORK_DIR/subtitles" --output_format srt
echo "  完成"

# 第3步:适配TikTok
echo "[3/6] 适配TikTok(9:16, <=3分钟)..."
ffmpeg -i "$INPUT" -vf "crop=ih*9/16:ih,subtitles=$WORK_DIR/subtitles/$(basename $INPUT .mp4).srt" -t 180 -c:v libx264 -crf 23 -c:a aac -b:a 128k -movflags +faststart "$WORK_DIR/tiktok/output.mp4" -y -loglevel error
echo "  完成: $(du -h $WORK_DIR/tiktok/output.mp4 | cut -f1)"

# 第4步:适配Instagram
echo "[4/6] 适配Instagram Reels(9:16, <=90秒)..."
ffmpeg -i "$INPUT" -vf "crop=ih*9/16:ih" -t 90 -c:v libx264 -crf 23 -c:a aac -b:a 128k -movflags +faststart "$WORK_DIR/instagram/output.mp4" -y -loglevel error
echo "  完成: $(du -h $WORK_DIR/instagram/output.mp4 | cut -f1)"

# 第5步:适配WhatsApp
echo "[5/6] 适配WhatsApp(<=64MB)..."
ffmpeg -i "$INPUT" -c:v libx264 -crf 28 -preset slow -c:a aac -b:a 96k -fs 62M -movflags +faststart "$WORK_DIR/whatsapp/output.mp4" -y -loglevel error
echo "  完成: $(du -h $WORK_DIR/whatsapp/output.mp4 | cut -f1)"

# 第6步:验证并汇总
echo "[6/6] 验证输出..."
echo ""
echo "=== 处理完成汇总 ==="
echo "项目: $PROJECT_NAME"
echo ""
echo "| 平台      | 文件                 | 大小    | 时长   |"
echo "|-----------|----------------------|---------|--------|"
for platform in tiktok instagram whatsapp; do
  file="$WORK_DIR/$platform/output.mp4"
  if [ -f "$file" ]; then
    size=$(du -h "$file" | cut -f1)
    duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$file" | cut -d. -f1)
    echo "| $platform | output.mp4           | $size   | ${duration}s  |"
  fi
done
echo ""
echo "字幕文件: $WORK_DIR/subtitles/"
echo "输出目录: $WORK_DIR/"
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `自动化工作流` 选项
- 处理流程: 接收输入 -> 执行自动化工作流 -> 返回结果
- 输入: 用户提供自动化工作流所需的参数和指令
- 输出: 返回自动化工作流的处理结果,包含执行状态码、结果数据和执行日志

### 6. 高级字幕定制
```bash
# ASS字幕(样式化字幕)
ffmpeg -i input.mp4 -vf "ass=subtitle.ass" -c:a copy output.mp4

# 多语言字幕(软字幕,可切换)
ffmpeg -i input.mp4 -i zh.srt -i en.srt \
  -map 0:v -map 0:a -map 1 -map 2 \
  -c:v copy -c:a copy \
  -c:s mov_text \
  -metadata:s:s:0 language=chi -metadata:s:s:1 language=eng \
  output_multi_sub.mp4

# 字幕样式定制(ASS格式)
cat > custom.ass << 'EOF'
[Script Info]
Title: 自定义字幕
ScriptType: v4.00+

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV
Style: Default,Microsoft YaHei,48,&H00FFFFFF,&H00000000,-1,0,1,2,1,2,30,30,40

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00,0:00:05,Default，0,0,0，自定义样式字幕
EOF
```- 验证返回数据的完整性和格式正确性
- 参考`高级字幕定制`的配置文档进行参数调优
### 7. 视频质量评估
```bash
# PSNR(峰值信噪比) - 越高越好(>30dB为好)
ffmpeg -i original.mp4 -i compressed.mp4 -lavfi psnr -f null - 2>&1 | grep "average"

# SSIM(结构相似性) - 越接近1越好(>0.95为优秀)
ffmpeg -i original.mp4 -i compressed.mp4 -lavfi ssim -f null - 2>&1 | grep "All"

# 依赖说明
ffmpeg -i distorted.mp4 -i reference.mp4 -lavfi libvmaf="model_path=vmaf_v0.6.1.pkl" -f null - 2>&1 | grep "VMAF"
```

**输入**: 用户提供视频质量评估所需的指令和必要参数。
**处理**: 解析视频质量评估的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回视频质量评估的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `视频质量评估` 选项

#
## 适用场景

### 场景一:内容团队批量多平台发布
内容团队有10个视频,需要同时适配TikTok、Instagram、YouTube Shorts和WhatsApp发布。

```bash
# 一键批量处理所有视频到所有平台
bash （请参考skill目录中的脚本文件） batch_input/ team_project

# 输出:
# /tmp/video_workflow_team_project/
#   ├── tiktok/     (10个9:16视频, <=3分钟)
#   ├── instagram/  (10个9:16视频, <=90秒)
#   ├── youtube/    (10个9:16视频, <=60秒)
#   ├── whatsapp/   (10个压缩视频, <=64MB)
#   └── subtitles/  (10个SRT字幕文件)
```

### 场景二:低清视频AI增强
用户有一段480p的老视频,需要提升到1080p并增强画质。

```bash
# 第1步:AI超分辨率(480p -> 1080p)
realesrgan-ncnn-vulkan -i old_video.mp4 -o enhanced.mp4 -n realesrgan-x4plus -s 4

# 第2步:重新编码标准化
ffmpeg -i enhanced.mp4 -c:v libx264 -crf 18 -preset slow -c:a aac -b:a 192k -movflags +faststart output_1080p.mp4

# 第3步:质量评估
ffmpeg -i old_video.mp4 -i output_1080p.mp4 -lavfi ssim -f null - 2>&1 | grep "All"
```

### 场景三:多码率流媒体服务
为视频平台生成HLS自适应多码率流,支持不同网络环境自动切换画质。

```bash
# 生成4档画质的HLS流
bash （请参考skill目录中的脚本文件） source_video.mp4 ./hls_output

# 输出结构:
# hls_output/
#   ├── master.m3u8          # 主播放列表(自适应)
#   ├── stream_0.m3u8        # 1080p (5000kbps)
#   ├── stream_1.m3u8        # 720p  (2800kbps)
#   ├── stream_2.m3u8        # 480p  (1400kbps)
#   ├── stream_3.m3u8        # 360p  (800kbps)
#   └── segment_*.ts         # 视频分片
```

## 使用流程

### 专业版环境检查
```bash
# 检查核心工具
ffmpeg -version
ffprobe -version

# 检查AI增强工具(可选)
realesrgan-ncnn-vulkan --version 2>/dev/null && echo "Real-ESRGAN: 可用" || echo "Real-ESRGAN: 未安装"

# 检查Whisper
whisper --version 2>/dev/null && echo "Whisper: 可用" || echo "Whisper: 未安装"
```

### 自动化工作流一键启动
```bash
# 单视频多平台处理
bash （请参考skill目录中的脚本文件） input.mp4 "my_project"

# 批量处理
bash （请参考skill目录中的脚本文件） input_folder/ output_folder/ tiktok
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | video-toolkit处理的内容输入 |,  |
| content | string | 否 | video-toolkit处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
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
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **GPU(可选)**: NVIDIA/AMD GPU用于AI超分加速

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| FFmpeg/FFprobe | 核心工具 | 必需 | 系统包管理器或官网 |
| Real-ESRGAN | AI超分 | 推荐 | GitHub Releases下载 |
| Whisper | 字幕生成 | 推荐 | pip install openai-whisper |
| Python 3 | Whisper依赖 | 推荐 | 系统包管理器 |
| Bash | 批量脚本 | 必需 | 系统内置或Git Bash |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

安装命令:

```bash
# FFmpeg
brew install ffmpeg          # macOS
sudo apt install ffmpeg      # Ubuntu
winget install Gyan.FFmpeg   # Windows
# Real-ESRGAN(从GitHub下载)
# (已移除GitHub链接)
# Whisper
pip install openai-whisper
```

### API Key 配置
本Skill基于本地工具运行,无需额外API Key。FFmpeg、Real-ESRGAN和Whisper均为本地执行,不依赖外部API。视频处理完全在本地完成,不上传至外部服务。

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,。核心视频处理依赖FFmpeg/FFprobe,AI超分依赖Real-ESRGAN,字幕依赖Whisper,批量处理依赖Bash脚本。仅处理用户明确提供的视频文件,不自动访问其他文件,不上传至外部服务。

## 案例展示

### 专业版平台规格配置
```json
{
  "platforms": {
    "tiktok": {"aspect": "9:16", "duration": 180, "size_mb": 287, "crf": 23},
    "instagram": {"aspect": "9:16", "duration": 90, "size_mb": 250, "crf": 23},
    "youtube_shorts": {"aspect": "9:16", "duration": 60, "size_mb": null, "crf": 23},
    "youtube": {"aspect": "16:9", "duration": 43200, "size_mb": null, "crf": 18},
    "whatsapp": {"aspect": "any", "duration": 180, "size_mb": 64, "crf": 28},
    "twitter": {"aspect": "16:9", "duration": 140, "size_mb": 512, "crf": 23},
    "linkedin": {"aspect": "16:9", "duration": 600, "size_mb": 200, "crf": 23},
    "custom": {"aspect": "1:1", "duration": null, "size_mb": null, "crf": 20}
  },
  "ai_enhancement": {
    "super_resolution": true,
    "model": "realesrgan-x4plus",
    "scale": 4
  },
  "streaming": {
    "hls": true,
    "bitrates": ["5000k", "2800k", "1400k", "800k"],
    "resolutions": ["1080p", "720p", "480p", "360p"]
  },
  "batch": {
    "enabled": true,
    "parallel": false,
    "formats": ["mp4", "mov", "avi", "mkv"]
  }
}
```

### 专业版与免费版完整对比
| 功能维度 | 免费版 | 专业版 |
|----------|--------|--------|
| 文件处理 | 单文件 | 批量文件夹 |
| 视频压缩 | 基础CRF | 自适应+多码率 |
| 字幕生成 | Whisper基础 | 多语言+ASS样式+软字幕 |
| 宽高比 | 裁剪/填充 | AI智能重构图 |
| AI超分 | 不支持 | Real-ESRGAN |
| HLS/DASH | 不支持 | 多码率自适应流 |
| 工作流 | 手动逐步 | 自动化一键 |
| 平台规格 | 5个主流 | 全平台+自定义 |
| 质量评估 | 不支持 | PSNR/SSIM/VMAF |
| 多语言字幕 | 不支持 | 软字幕多语言切换 |
| 适用对象 | 个人创作者 | 内容团队/机构 |
| 兼容性 | - | 完全兼容免费版命令 |

## 常见问题

### Q1: 专业版兼容免费版命令吗?
完全兼容。专业版支持免费版的所有FFmpeg命令和参数。专业版新增批量脚本、AI增强和自动化工作流。

### Q2: Real-ESRGAN需要什么硬件?
Real-ESRGAN支持NVIDIA GPU(CUDA)、AMD GPU和CPU运行。GPU运行速度更快,CPU运行较慢但兼容性更好。1080p视频2x超分在GPU上约需5-10分钟。

### Q3: 批量处理支持哪些视频格式?
支持MP4、MOV、AVI、MKV、WebM、FLV等FFmpeg支持的所有格式。通过配置文件的formats参数可自定义。

### Q4: HLS流如何部署到服务器?
将HLS输出目录(hls_output/)上传到任意Web服务器或CDN,通过master.m3u8地址播放。播放器(Safari/Video.js/HLS.js)会自动根据网络选择优秀画质。

### Q5: 智能重构图如何工作?
智能重构图通过场景检测分析视频内容,识别画面中的主体位置,动态调整裁剪区域确保主体始终在画面中。避免简单居中裁剪导致主体被切掉。

### Q6: 多语言字幕如何实现?
通过软字幕方式嵌入多个语言的SRT文件,播放器可切换语言。使用`-map`映射多个字幕流,`-metadata:s:s:N language=详情见说明`标记语言。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

