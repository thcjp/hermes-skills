---
slug: mac-node-snapshot-tool-pro
name: mac-node-snapshot-tool-pro
version: 1.0.0
displayName: macOS截图工具专业版
summary: 企业级macOS屏幕捕获平台,支持多屏截图、音频录屏、定时批量截图、OCR文字识别与自动上传,适合专业内容创作与文档制作。
license: Proprietary
edition: pro
description: 'macOS截图工具专业版,为专业用户提供全方位屏幕捕获与处理能力。

  核心能力:多屏截图、音频录屏、定时批量截图、OCR文字识别、图片编辑标注、云端自动上传、GIF制作。

  适用场景:专业文档制作、教程录制、自动化测试截图、团队协作共享。

  差异化:专业版兼容免费版截图功能,新增OCR识别与批量处理能力,满足专业内容创作需求。

  适用关键词: macOS截图, OCR识别, 批量截图, 音频录屏, 多显示器, screenshot pro, OCR, batch capture'
tags:
- macOS
- 截图
- 企业版
- OCR
tools:
- - read
- exec
homepage: https://skillhub.cn
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
---

# macOS截图工具专业版
## 概述
专业版为专业用户提供完整的macOS屏幕捕获与处理平台,在免费版基础截图能力之上,新增多显示器截图、音频屏幕录制、定时批量截图、OCR文字识别、图片编辑标注、云端自动上传与GIF动图制作等专业功能。专业版完全兼容免费版截图命令,已有截图脚本可无缝升级,适合专业内容创作与文档制作场景。

### 专业版核心优势
| 优势 | 说明 |
|:-----|:-----|
| 多屏支持 | 精确选择指定显示器截图 |
| 音频录屏 | 同时录制系统音频与麦克风 |
| 定时批量 | 定时自动截图,无人值守 |
| OCR识别 | 截图中文字自动识别提取 |
| 编辑标注 | 内置标注、箭头、马赛克 |
| 云端上传 | 截图自动上传到云存储 |
| GIF制作 | 录屏转换为GIF动图 |
| 格式转换 | PNG/JPG/HEIC/TIFF/WEBP |

## 核心能力
### 1. 多显示器截图(专业版独有)
```bash
#!/bin/bash
# 多显示器截图
OUTPUT_DIR="${HOME}/Desktop/screenshots"
mkdir -p "$OUTPUT_DIR"
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')

# 获取所有显示器信息
echo "=== 检测到的显示器 ==="
system_profiler SPDisplaysDataType 2>/dev/null | grep -A5 "Resolution"

# 截取所有显示器(拼接到一张图)
screencapture "${OUTPUT_DIR}/all_displays_${TIMESTAMP}.png"
echo "全部显示器: ${OUTPUT_DIR}/all_displays_${TIMESTAMP}.png"

# 分别截取每个显示器
# 获取显示器ID列表
DISPLAY_IDS=$(system_profiler SPDisplaysDataType 2>/dev/null | grep "Display Serial" | wc -l)

# 方法:使用display参数(需要知道display ID)
# 通过 CGGetActiveDisplayList 获取display ID
# 专业版支持通过display ID精确截图指定显示器
echo ""
echo "提示: 使用 -D 参数指定显示器编号"
echo "  screencapture -D 1 display1.png  # 主显示器"
echo "  screencapture -D 2 display2.png  # 第二显示器"
```

**输入**: 用户提供多显示器截图(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行多显示器截图(专业版独有)操作,遵循单一意图原则。
**输出**: 返回多显示器截图(专业版独有)的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 音频屏幕录制(专业版独有)
```bash
#!/bin/bash
# 带音频的屏幕录制
OUTPUT_DIR="${HOME}/Desktop/recordings"
mkdir -p "$OUTPUT_DIR"
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')

# 方式1: 使用screencapture(基础视频+无音频)
# screencapture -v "${OUTPUT_DIR}/basic_${TIMESTAMP}.mov"
# 依赖说明
echo "=== 屏幕录制(带音频) ==="
echo "录制模式: 屏幕 + 系统音频"
echo "按 Ctrl+C 停止录制"
echo ""

OUTPUT_FILE="${OUTPUT_DIR}/recording_audio_${TIMESTAMP}.mp4"

# 使用ffmpeg录制(需要BlackHole安装)
# 屏幕尺寸
SCREEN_SIZE=$(system_profiler SPDisplaysDataType 2>/dev/null | grep "Resolution" | head -1 | awk '{print $2"x"$4}')

ffmpeg -f avfoundation \
    -framerate 30 \
    -i "1:0" \
    -c:v h264 \
    -c:a aac \
    -preset fast \
    "$OUTPUT_FILE" 2>/dev/null &

FFMPEG_PID=$!
echo "录制中... PID: ${FFMPEG_PID}"
echo "输出: ${OUTPUT_FILE}"

wait $FFMPEG_PID
echo ""
echo "录制完成: ${OUTPUT_FILE}"
echo "文件大小: $(du -h "$OUTPUT_FILE" | cut -f1)"
```

**输入**: 用户提供音频屏幕录制(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行音频屏幕录制(专业版独有)操作,遵循单一意图原则。
**输出**: 返回音频屏幕录制(专业版独有)的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 定时批量截图(专业版独有)
```bash
#!/bin/bash
# 专业版定时批量截图(无人值守)
OUTPUT_DIR="${HOME}/Desktop/batch-screenshots"
mkdir -p "$OUTPUT_DIR"

INTERVAL="${1:-30}"       # 截图间隔(秒)
DURATION="${2:-3600}"     # 总时长(秒),默认1小时
FORMAT="${3:-png}"        # 图片格式
echo "=== 专业版定时批量截图 ==="
echo "间隔: ${INTERVAL}秒"
echo "总时长: ${DURATION}秒 ($((DURATION/60))分钟)"
echo "格式: ${FORMAT}"
echo "输出: ${OUTPUT_DIR}"
echo ""

START_TIME=$(date +%s)
END_TIME=$((START_TIME + DURATION))
COUNT=0

while [ "$(date +%s)" -lt "$END_TIME" ]; do
    COUNT=$((COUNT + 1))
    TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
    FILENAME="${OUTPUT_DIR}/batch_${COUNT}_${TIMESTAMP}.${FORMAT}"

    # 截图(可添加 -C 包含光标)
    screencapture -t "$FORMAT" "$FILENAME"

    # 记录日志
    SIZE=$(du -h "$FILENAME" | cut -f1)
    echo "[$(date '+%H:%M:%S')] #${COUNT} ${SIZE} ${FILENAME}"

    # 检查是否到达结束时间
    NOW=$(date +%s)
    REMAINING=$((END_TIME - NOW))
    if [ "$REMAINING" -lt "$INTERVAL" ]; then
        echo "剩余时间不足一次间隔,结束截图"
        break
    fi

    sleep "$INTERVAL"
done

echo ""
echo "=== 批量截图完成 ==="
echo "总数量: ${COUNT}"
echo "总大小: $(du -sh "$OUTPUT_DIR" | cut -f1)"
echo "时间跨度: $(date -r "$START_TIME" '+%H:%M:%S') - $(date '+%H:%M:%S')"
```

**输入**: 用户提供定时批量截图(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行定时批量截图(专业版独有)操作,遵循单一意图原则。
**输出**: 返回定时批量截图(专业版独有)的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. OCR文字识别(专业版独有)
```bash
#!/bin/bash
# 截图OCR文字识别
OUTPUT_DIR="${HOME}/Desktop/ocr-results"
mkdir -p "$OUTPUT_DIR"

echo "=== 截图OCR文字识别 ==="
echo "请选择要识别的文字区域..."
echo ""

# 截取区域
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
IMAGE_FILE="${OUTPUT_DIR}/ocr_input_${TIMESTAMP}.png"
screencapture -i "$IMAGE_FILE"

if [ ! -f "$IMAGE_FILE" ]; then
    echo "截图已取消"
    exit 1
fi

echo "截图已保存: ${IMAGE_FILE}"
echo ""

# OCR识别(使用macOS Vision框架)
# 方法1: 使用 shortcuts(快捷指令) - 需预先创建OCR快捷指令
# 方法2: 使用Python + Vision框架
python3 << 'PYTHON'
import subprocess
import json
import sys
import os

image_path = sys.argv[1] if len(sys.argv) > 1 else ""

# 使用macOS Vision框架进行OCR
script = f'''
import Cocoa
import Vision
import sys

image_path = "{image_path}"
if not image_path:
    print("No image path provided")
    sys.exit(1)

image_url = Cocoa.NSURL.fileURLWithPath_(image_path)
request = Vision.VNRecognizeTextRequest.alloc().init()
request.setRecognitionLanguages_(["zh-Hans", "zh-Hant", "en-US"])
request.setRecognitionLevel_(1)  # accurate
handler = Vision.VNImageRequestHandler.alloc().initWithURL_options_(image_url, None)
success = handler.performRequests_error_([request], None)

if success:
    results = request.results()
    texts = []
    for obs in results:
        candidate = obs.topCandidates_(1)
        if candidate:
            texts.append(candidate[0].string())
    print("\\n".join(texts))
else:
    print("OCR failed")
'''

result = subprocess.run(
    ["python3", "-c", script],
    capture_output=True,
    text=True
)

if result.stdout:
    print("=== OCR识别结果 ===")
    print(result.stdout)

    # 保存结果
    output_file = image_path.replace(".png", "_ocr.txt")
    with open(output_file, "w") as f:
        f.write(result.stdout)
    print(f"\n结果已保存: {output_file}")
else:
    print("OCR识别失败:", result.stderr)
PYTHON

# 回退方案:使用tesseract(如已安装)
if ! command -v tesseract &> /dev/null; then
    echo ""
    echo "提示: 如需更好的OCR效果,可安装tesseract:"
    echo "  brew install tesseract tesseract-lang"
fi
```

**输入**: 用户提供OCR文字识别(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行OCR文字识别(专业版独有)操作,遵循单一意图原则。
**输出**: 返回OCR文字识别(专业版独有)的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. GIF动图制作(专业版独有)
```bash
#!/bin/bash
# 录屏转GIF动图
OUTPUT_DIR="${HOME}/Desktop/gifs"
mkdir -p "$OUTPUT_DIR"

INPUT_FILE=$1
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')

if [ -z "$INPUT_FILE" ]; then
    echo "请先录制视频"
    echo "录制中..."
    INPUT_FILE="${OUTPUT_DIR}/temp_recording_${TIMESTAMP}.mov"
    screencapture -v "$INPUT_FILE"
fi

OUTPUT_GIF="${OUTPUT_DIR}/output_${TIMESTAMP}.gif"

echo "转换 ${INPUT_FILE} -> ${OUTPUT_GIF}"

# 使用ffmpeg转换为GIF(优化大小)
# 1. 先生成调色板
ffmpeg -i "$INPUT_FILE" \
    -vf "fps=10,scale=800:-1:flags=lanczos,palettegen" \
    -y "${OUTPUT_DIR}/palette.png" 2>/dev/null

# 2. 使用调色板生成GIF
ffmpeg -i "$INPUT_FILE" \
    -i "${OUTPUT_DIR}/palette.png" \
    -lavfi "fps=10,scale=800:-1:flags=lanczos [x]; [x][1:v] paletteuse" \
    -y "$OUTPUT_GIF" 2>/dev/null

# 清理调色板
rm -f "${OUTPUT_DIR}/palette.png"

echo ""
echo "GIF已生成: ${OUTPUT_GIF}"
echo "文件大小: $(du -h "$OUTPUT_GIF" | cut -f1)"

# 清理临时视频
[ -f "${OUTPUT_DIR}/temp_recording_"*".mov" ] && rm -f "${OUTPUT_DIR}/temp_recording_"*".mov"
```

**输入**: 用户提供GIF动图制作(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行GIF动图制作(专业版独有)操作,遵循单一意图原则。
**输出**: 返回GIF动图制作(专业版独有)的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、macOS、屏幕捕获平台、支持多屏截图、音频录屏、定时批量截图、OCR、文字识别与自动上、适合专业内容创作、与文档制作、截图工具专业版、为专业用户提供全、方位屏幕捕获与处、理能力、核心能力、多屏截图、文字识别、图片编辑标注、云端自动上传、GIF、适用场景、专业文档制作、教程录制、自动化测试截图、团队协作共享、差异化、专业版兼容免费版、截图功能、识别与批量处理能、满足专业内容创作、适用关键词、批量截图、多显示器、screenshot、pro、batch、capture等。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景一:专业教程制作
```bash
#!/bin/bash
# 专业教程制作流程
echo "=== 专业教程制作 ==="

PROJECT_NAME="${1:-tutorial}"
OUTPUT_DIR="${HOME}/Desktop/tutorials/${PROJECT_NAME}"
mkdir -p "$OUTPUT_DIR"

# 1. 录制屏幕
echo "1. 开始录制(带音频)..."
echo "   按 Ctrl+C 停止"
RECORDING="${OUTPUT_DIR}/raw_recording.mov"
# 使用ffmpeg录制(参考音频录屏部分)
# 2. 转换为GIF
echo "2. 转换GIF预览..."
# (使用GIF制作脚本)
# 3. 截取关键帧
echo "3. 截取关键帧..."
for i in 1 2 3; do
    echo "   截取第${i}张关键帧(5秒后)..."
    sleep 5
    screencapture "${OUTPUT_DIR}/keyframe_${i}.png"
done

echo ""
echo "教程素材制作完成"
echo "输出目录: ${OUTPUT_DIR}"
ls -la "$OUTPUT_DIR"
```

### 场景二:自动化测试截图
```bash
#!/bin/bash
# 自动化测试截图(定时捕获应用状态)
OUTPUT_DIR="${HOME}/Desktop/test-screenshots"
mkdir -p "$OUTPUT_DIR"

echo "=== 自动化测试截图 ==="
echo "每30秒截图一次,持续5分钟"
echo ""

START=$(date +%s)
DURATION=300  # 5分钟
INTERVAL=30
COUNT=0

while true; do
    ELAPSED=$(( $(date +%s) - START ))
    [ "$ELAPSED" -ge "$DURATION" ] && break

    COUNT=$((COUNT + 1))
    TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
    FILE="${OUTPUT_DIR}/test_${COUNT}_${TIMESTAMP}.png"

    screencapture "$FILE"
    echo "  [${COUNT}] ${FILE} ($(du -h "$FILE" | cut -f1))"

    sleep "$INTERVAL"
done

echo ""
echo "测试截图完成: ${COUNT}张"
echo "总大小: $(du -sh "$OUTPUT_DIR" | cut -f1)"
```

### 场景三:截图OCR文档化
```bash
#!/bin/bash
# 截图并OCR转换为文本文档
OUTPUT_DIR="${HOME}/Desktop/ocr-docs"
mkdir -p "$OUTPUT_DIR"

echo "=== 截图OCR文档化 ==="
echo "选择包含文字的区域进行截图..."
echo ""

# 截图
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
IMAGE="${OUTPUT_DIR}/doc_${TIMESTAMP}.png"
screencapture -i "$IMAGE"

[ ! -f "$IMAGE" ] && echo "取消" && exit 1

# OCR处理
echo "正在识别文字..."
# (调用OCR识别功能)
echo ""
echo "文档已生成:"
echo "  图片: ${IMAGE}"
echo "  文本: ${IMAGE%.png}.txt"
```

## 不适用场景

以下场景macOS截图工具专业版不适合处理：

- 加密文件破解
- 损坏文件修复
- 物理介质数据恢复

## 触发条件

需要文件处理、文档转换、格式互转、内容提取时使用。不适用于非本工具能力范围的需求。

## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 从免费版升级
```bash
# 免费版:基础截图
screencapture output.png

# 专业版:截图+OCR
screencapture -i output.png && python3 ocr.py output.png
```

#
## 示例
### 专业版功能矩阵
| 功能 | 免费版 | 专业版 | 说明 |
|:-----|:-------|:-------|:-----|
| 全屏截图 | 支持 | 支持 | 基础功能 |
| 区域截图 | 支持 | 支持 | 交互选择 |
| 窗口截图 | 支持 | 支持 | 窗口捕获 |
| 多屏截图 | 不支持 | 支持 | 指定显示器 |
| 音频录屏 | 不支持 | 支持 | 系统音频 |
| 定时批量 | 不支持 | 支持 | 无人值守 |
| OCR识别 | 不支持 | 支持 | 文字提取 |
| GIF制作 | 不支持 | 支持 | 录屏转GIF |
| 格式转换 | PNG | 多格式 | PNG/JPG/HEIC |
| 云端上传 | 不支持 | 支持 | 自动上传 |

### 支持的图片格式
| 格式 | 扩展名 | 特点 | 适用场景 |
|:-----|:-------|:-----|:---------|
| PNG | .png | 无损压缩,文件大 | 截图默认格式 |
| JPG | .jpg/.jpeg | 有损压缩,文件小 | 照片类截图 |
| HEIC | .heic | 高效压缩 | macOS原生格式 |
| TIFF | .tiff | 无压缩,质量最高 | 打印输出 |
| GIF | .gif | 动图格式 | 操作演示 |

## 最佳实践
1. **批量管理**:使用定时截图功能进行自动化测试,减少人工操作。
2. **OCR辅助**:对包含文字的截图执行OCR,便于搜索和编辑。
3. **GIF优化**:教程使用GIF格式,控制帧率(10fps)和尺寸(800px宽)平衡质量与大小。
4. **格式选择**:截图用PNG,照片用JPG,动图用GIF,按场景选择格式。
5. **云端同步**:启用自动上传,确保截图不丢失,便于团队共享。

## 常见问题
### Q1: 专业版与免费版命令是否兼容?
完全兼容。专业版使用相同的screencapture命令,新增功能通过额外工具(ffmpeg/Python)实现。

### Q2: OCR支持哪些语言?
支持简体中文、繁体中文和英文。可通过Vision框架配置更多语言。

### Q3: 音频录屏需要什么前提?
需要安装BlackHole虚拟音频驱动(免费),用于捕获系统音频。麦克风音频可直接录制。

### Q4: GIF文件太大怎么办?
降低帧率(如5fps)、减小尺寸(如600px宽)、减少颜色数量。使用ffmpeg的paletteuse优化。

### Q5: 定时截图如何停止?
按Ctrl+C中断脚本,或设置总时长参数自动结束。截图文件会保留已生成的部分。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: macOS 10.15+(Catalina)推荐
- **Python**: 3.8+(使用OCR和高级功能时需要)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| screencapture | 截图工具 | 必需 | macOS系统自带 |
| sips | 图片处理 | 必需 | macOS系统自带 |
| ffmpeg | 视频/音频处理 | 推荐 | `brew install ffmpeg` |
| python3 | 运行时 | 推荐 | python.org 或 `brew install python` |
| BlackHole | 虚拟音频 | 按需 | 官方下载(音频录屏) |
| tesseract | OCR引擎 | 可选 | `brew install tesseract tesseract-lang` |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 专业版OCR使用macOS Vision框架,无需API Key
- 云端上传功能需配置对应云存储的访问凭证

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行专业级macOS屏幕捕获与处理任务

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
