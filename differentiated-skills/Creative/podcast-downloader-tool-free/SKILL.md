---
slug: podcast-downloader-tool-free
name: podcast-downloader-tool-free
version: "1.0.0"
displayName: 播客下载工具免费版
summary: 从小宇宙平台下载播客音频与节目笔记,自动转换为MP3格式,适合个人离线收听。
license: MIT
edition: free
description: |-
  面向个人用户的播客下载工具(免费版)。

  核心能力:
  - 从小宇宙(xiaoyuzhoufm.com)下载单集播客
  - 自动提取节目笔记(Show Notes)为 Markdown
  - 音频自动转换为 MP3 格式
  - 兼容骨传导蓝牙耳机等设备
  - 支持自定义音质与输出目录

  适用场景:
  - 个人离线收听播客
  - 节目笔记归档与检索
  - 兼容特殊播放设备
  - 网络不稳定环境预下载

  差异化:
  - 免费版聚焦单集下载核心能力
  - 自动 m4a 转 mp3,提升兼容性
  - 节目笔记同步保存为 Markdown
  - 适配个人用户离线收听需求

  触发关键词: podcast, downloader, 小宇宙, xiaoyuzhoufm, 下载, mp3, show notes, 离线, free
tags:
- 创意设计
- 播客
- 下载工具
- 离线收听
- 音频转换
tools:
- read
- exec
---

# 播客下载工具 - 免费版

## 概述

播客下载工具(免费版)帮助个人用户从小宇宙(xiaoyuzhoufm.com)下载播客音频与节目笔记。工具自动提取音频与 Show Notes,并将音频转换为 MP3 格式,兼容骨传导蓝牙耳机、水下游泳设备等特殊播放场景。

免费版聚焦单集下载,专业版(`podcast-downloader-tool-pro`)在此基础上提供批量下载、播放列表支持、定时订阅与多平台扩展等高级能力。

## 核心能力

| 能力 | 免费版 | 说明 |
|:-----|:-------|:-----|
| 单集下载 | 支持 | 指定 URL 下载 |
| 音频格式转换 | m4a -> mp3 | 兼容更多设备 |
| 节目笔记提取 | 支持 | 输出 Markdown |
| 自定义音质 | 支持 | 0-4 五档 |
| 输出目录配置 | 支持 | 环境变量 |
| 保留原始文件 | 可选 | KEEP_M4A |
| 批量下载 | 不支持 | 升级专业版 |
| 播放列表 | 不支持 | 升级专业版 |
| 定时订阅 | 不支持 | 升级专业版 |
| 多平台 | 不支持 | 升级专业版 |

## 使用场景

### 场景一:离线收听下载

为通勤或运动场景预下载播客。

```bash
# 下载单集
./scripts/download.sh "https://www.xiaoyuzhoufm.com/episode/abc123def456"

# 指定输出目录
PODCAST_DIR="/mnt/sdcard/podcasts" ./scripts/download.sh "https://www.xiaoyuzhoufm.com/episode/abc123"
```

### 场景二:自定义音质下载

根据存储空间选择音质。

```bash
# 最佳音质(文件较大)
AUDIO_QUALITY=0 ./scripts/download.sh "https://www.xiaoyuzhoufm.com/episode/abc123"

# 普通音质(节省空间)
AUDIO_QUALITY=4 ./scripts/download.sh "https://www.xiaoyuzhoufm.com/episode/abc123"

# 保留原始 m4a 文件
KEEP_M4A=true ./scripts/download.sh "https://www.xiaoyuzhoufm.com/episode/abc123"
```

### 场景三:节目笔记归档

下载音频的同时保存节目笔记。

```bash
# 下载后自动生成 Show Notes Markdown
./scripts/download.sh "https://www.xiaoyuzhoufm.com/episode/abc123"

# 输出结构
# /output/节目名-单集标题/
# ├── 单集标题.mp3       # 音频文件
# └── 单集标题.md        # 节目笔记
```

## 快速开始

### 1. 安装依赖

```bash
# macOS
brew install curl jq ffmpeg

# Ubuntu / Debian
sudo apt install curl jq ffmpeg

# Windows (scoop)
scoop install curl jq ffmpeg
```

### 2. 下载第一集

```bash
# 基本用法
./scripts/download.sh "https://www.xiaoyuzhoufm.com/episode/YOUR_EPISODE_ID"
```

### 3. 查看输出

```text
输出目录/
└── 节目名-单集标题/
    ├── 单集标题.mp3       # 转换后的 MP3
    └── 单集标题.md        # 节目笔记
```

## 配置示例

### 环境变量配置

| 变量 | 默认值 | 说明 |
|:-----|:-------|:-----|
| `PODCAST_DIR` | `~/Documents/podcast/` | 输出目录 |
| `AUDIO_QUALITY` | `0` | MP3 音质(0=最佳, 2=良好, 4=普通) |
| `KEEP_M4A` | `false` | 是否保留原始 m4a 文件 |

### 音质选择指南

| 等级 | 码率 | 文件大小(30分钟) | 适用场景 |
|:-----|:-----|:-------------------|:---------|
| 0 | 320kbps | ~70MB | 最佳音质,耳机收听 |
| 2 | 192kbps | ~45MB | 良好平衡,日常推荐 |
| 4 | 128kbps | ~30MB | 节省空间,扬声器 |

### 下载脚本核心流程

```bash
#!/bin/bash
# download.sh - 单集下载脚本

URL="$1"
OUTPUT_DIR="${PODCAST_DIR:-$HOME/Documents/podcast/}"
QUALITY="${AUDIO_QUALITY:-0}"
KEEP_M4A="${KEEP_M4A:-false}"

# 1. 提取页面信息
HTML=$(curl -s "$URL")
DATA=$(echo "$HTML" | grep -o '__NEXT_DATA__.*' | head -1)

# 2. 解析音频地址与标题
AUDIO_URL=$(echo "$DATA" | jq -r '.props.pageProps.episodeInfo.audioUrl')
TITLE=$(echo "$DATA" | jq -r '.props.pageProps.episodeInfo.title')
SHOW_NAME=$(echo "$DATA" | jq -r '.props.pageProps.episodeInfo.podcast.title')

# 3. 创建输出目录
EPISODE_DIR="${OUTPUT_DIR}/${SHOW_NAME}-${TITLE}"
mkdir -p "$EPISODE_DIR"

# 4. 下载 m4a
curl -L -o "$EPISODE_DIR/${TITLE}.m4a" "$AUDIO_URL"

# 5. 转换为 MP3
ffmpeg -i "$EPISODE_DIR/${TITLE}.m4a" \
    -codec:a libmp3lame -qscale:a "$QUALITY" \
    "$EPISODE_DIR/${TITLE}.mp3"

# 6. 删除 m4a(可选)
if [ "$KEEP_M4A" != "true" ]; then
    rm "$EPISODE_DIR/${TITLE}.m4a"
fi

# 7. 提取节目笔记
echo "$DATA" | jq -r '.props.pageProps.episodeInfo.shownotes' > "$EPISODE_DIR/${TITLE}.md"

echo "下载完成: $EPISODE_DIR"
```

## 最佳实践

1. **音质选择策略**
   - 耳机收听:等级 0(320kbps),体验最佳
   - 日常通勤:等级 2(192kbps),平衡质量与空间
   - 存储紧张:等级 4(128kbps),节省空间
   - 兼容老设备:必须 MP3 格式

2. **目录管理规范**
   - 按节目名分类存储
   - 定期清理已听完的单集
   - 使用云同步目录(如百度网盘)备份
   - 文件名包含节目名与单集标题

3. **网络优化**
   - 大文件建议在 WiFi 环境下载
   - 网络不稳定时启用 curl 重试
   - 使用代理加速(如需要)

4. **设备兼容性**
   - MP3 格式兼容所有播放设备
   - 骨传导蓝牙耳机需 MP3 格式
   - 水下游泳设备需离线 MP3
   - 车载系统优先 MP3

## 常见问题

### Q1: 下载失败提示 "403 Forbidden"?

小宇宙可能有反爬虫机制。建议:
- 添加 User-Agent 请求头
- 避免短时间内频繁下载
- 检查 URL 是否正确

### Q2: 转换 MP3 失败?

确保已安装 ffmpeg:
```bash
ffmpeg -version
```
如未安装,参考快速开始的依赖安装步骤。

### Q3: 节目笔记为空?

部分单集可能没有 Show Notes。检查页面是否存在 `shownotes` 字段。如内容为 HTML 格式,可能需要额外转换。

### Q4: 免费版与专业版的区别?

免费版支持单集下载;专业版支持批量下载、播放列表、定时订阅与多平台。需要大量下载或自动化的场景建议升级。

### Q5: 是否支持其他播客平台?

免费版专注小宇宙平台。专业版扩展支持更多平台。如有其他平台需求,建议升级专业版。

### Q6: 下载的音频可以商用吗?

下载的音频仅供个人离线收听。商业使用需获得版权方授权。请遵守相关法律法规与平台条款。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Shell**: Bash(Windows 建议使用 WSL 或 Git Bash)
- **网络**: 需访问 `xiaoyuzhoufm.com`

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| curl | 命令行工具 | 必需 | 系统自带或下载 |
| jq | JSON 处理工具 | 必需 | `brew install jq` / `apt install jq` |
| ffmpeg | 音频转换工具 | 必需 | `brew install ffmpeg` / `apt install ffmpeg` |
| Bash | Shell 环境 | 必需 | 系统自带(Windows 用 WSL) |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本 Skill **无需任何 API Key**
- 下载流程通过 HTTP 请求直接获取公开内容
- 不依赖第三方 API 服务

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务。免费版聚焦单集下载与格式转换,适合个人离线收听场景。
