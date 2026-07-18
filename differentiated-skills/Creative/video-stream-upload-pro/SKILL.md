---
slug: video-stream-upload-pro
name: video-stream-upload-pro
version: "1.0.0"
displayName: 视频上传-专业版
summary: 企业级视频上传与流媒体管理平台，支持自定义编码、多分辨率、批量上传、缩略图管理与转码费用预估。
license: MIT
edition: pro
description: |-
  视频上传专业版，面向企业团队与内容平台的高级视频上传与流媒体管理方案。

  核心能力:
  - 自定义编码配置（分辨率/码率/编码器/容器）
  - 多分辨率输出（240p-4320p 共 8 档）
  - 批量视频上传（50+ 并行）
  - 自定义缩略图上传
  - 转码费用预估
  - 视频管理（列表/更新/删除）
  - HLS 与 DASH 双协议支持
  - 多分片大文件上传（单文件可达数 GB）
  - 元数据与标签管理
  - 上传任务队列与失败重试

  适用场景:
  - 企业视频内容批量托管
  - 在线教育平台视频分发
  - 电商商品视频管理
  - 媒体机构内容归档
  - 直播回放点播化

  差异化:
  - 专业版提供完整自定义编码能力，支持 8 档分辨率输出
  - 内置批量上传工作流，支持 50+ 视频并行
  - 多分片上传支持大文件（数 GB 级别）
  - 与免费版完全兼容，已有 API Key 可直接使用
  - 提供转码费用预估与视频全生命周期管理

  触发关键词: 批量视频上传, 自定义编码, 多分辨率, 缩略图上传, 转码费用, 视频管理, HLS DASH, batch upload, transcoding
tags:
- Creative
- 视频上传
- 流媒体
- 专业版
- 批量处理
- 企业级
tools:
- read
- exec
---

# 视频上传工具 - 专业版

## 概述

视频上传专业版是一款面向企业团队与内容平台的高级视频上传与流媒体管理工具。在免费版默认上传能力之上，专业版扩展了自定义编码配置、多分辨率输出、批量上传、缩略图管理、视频全生命周期管理等企业级能力。

专业版采用任务队列架构，支持多分片大文件上传、失败重试、断点续传，可稳定处理 50+ 视频的批量上传任务。同时完全兼容免费版 API Key 与调用方式，已有项目可无缝迁移。

### 免费版与专业版能力对比

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 默认上传 | 支持 | 支持 |
| 三步流程 | 支持 | 支持 |
| HLS 链接 | 支持 | 支持 |
| 自定义编码 | 不支持 | 支持 |
| 多分辨率输出 | 不支持（默认档） | 8 档（240p-4320p） |
| 缩略图上传 | 不支持 | 支持 |
| 批量上传 | 不支持 | 50+ 并行 |
| 视频管理 | 不支持 | 列表/更新/删除 |
| 转码费用预估 | 不支持 | 支持 |
| DASH 协议 | 不支持 | 支持 |
| 多分片上传 | 不支持 | 支持（单文件数 GB） |
| 元数据管理 | 不支持 | 支持 |
| 任务队列 | 不支持 | 支持 |
| 优先支持 | 社区 | 优先响应 |

## 核心能力

### 1. 自定义编码配置

支持完整编码参数自定义：

- **分辨率**：240p / 360p / 480p / 720p / 1080p / 1440p / 2160p / 4320p
- **编码器**：H.264（最高 4K）/ H.265（最高 8K）
- **流媒体协议**：HLS / DASH
- **容器格式**：mpegts / mp4 / fmp4
- **码率**：自定义视频与音频码率
- **音频配置**：采样率、声道数、语言

### 2. 多分辨率输出

单次上传支持输出多档分辨率：

| 分辨率 | 像素 | 最大码率 | 适用场景 |
|:-------|:-----|:---------|:---------|
| 240p | 426×240 | 700,000 bps | 移动端低带宽 |
| 360p | 640×360 | 1,200,000 bps | 移动端标准 |
| 480p | 854×480 | 2,000,000 bps | 标清播放 |
| 720p | 1280×720 | 4,000,000 bps | 高清播放 |
| 1080p | 1920×1080 | 6,000,000 bps | 全高清播放 |
| 1440p | 2560×1440 | 12,000,000 bps | 2K 高清 |
| 2160p | 3840×2160 | 30,000,000 bps | 4K 超高清 |
| 4320p | 7680×4320 | 60,000,000 bps | 8K 极致画质 |

### 3. 批量视频上传

支持单任务上传 50+ 视频：

```text
输入视频清单（CSV/JSON）
      ↓
任务调度器分配并行上传
      ↓
多上传进程并行执行
      ↓
多分片大文件处理
      ↓
失败重试 + 结果聚合
      ↓
生成上传报告
```

### 4. 缩略图管理

```bash
# 上传自定义缩略图
curl -s -X POST "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID/thumbnail" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -F 'file=@/path/to/thumbnail.jpg'
```

支持格式：`.png`、`.jpg`

### 5. 转码费用预估

上传前估算转码成本：

```bash
curl -s 'https://api-w3stream.attoaioz.cyou/api/videos/cost?duration=60&qualities=360p,1080p' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY'
```

### 6. 视频全生命周期管理

- **列表查询**：分页获取所有视频
- **更新信息**：修改标题、描述、标签
- **删除视频**：移除视频及关联资源
- **状态查询**：实时获取转码进度

## 使用场景

### 场景 1：企业培训视频批量托管

某企业需要将 50 个培训视频上传至流媒体平台，要求 720p 与 1080p 双档输出。

**批量配置 `batch-upload.json`：**

```json
{
  "project": "企业培训视频托管",
  "output_dir": "/reports/",
  "videos": [
    {
      "file": "/videos/training-01.mp4",
      "title": "新员工入职培训",
      "qualities": ["720p", "1080p"],
      "codec": "h264",
      "tags": ["training", "onboarding"]
    },
    {
      "file": "/videos/training-02.mp4",
      "title": "安全规范培训",
      "qualities": ["720p", "1080p"],
      "codec": "h264",
      "tags": ["training", "safety"]
    }
  ]
}
```

**执行命令：**

```bash
python3 batch_upload.py --config /path/to/batch-upload.json --parallel 8
```

**输出报告：**

```text
/reports/
├── batch-upload-report.json   # 批量上传总报告
├── training-01.json           # 单视频详情
└── training-02.json
```

### 场景 2：在线教育多分辨率课程

某教育平台需要上传课程视频，同时输出 360p（移动端）与 1080p（PC 端）版本。

**自定义编码配置：**

```bash
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Python 进阶教程",
    "description": "适合有基础的开发者进阶学习",
    "is_public": true,
    "tags": ["python", "programming", "tutorial"],
    "qualities": [
      {
        "resolution": "360p",
        "type": "hls",
        "container_type": "mpegts",
        "video_config": {
          "codec": "h264",
          "bitrate": 1200000,
          "index": 0
        },
        "audio_config": {
          "codec": "aac",
          "bitrate": 128000,
          "channels": "2",
          "sample_rate": 44100,
          "language": "zh",
          "index": 0
        }
      },
      {
        "resolution": "1080p",
        "type": "hls",
        "container_type": "mpegts",
        "video_config": {
          "codec": "h264",
          "bitrate": 6000000,
          "index": 0
        },
        "audio_config": {
          "codec": "aac",
          "bitrate": 192000,
          "channels": "2",
          "sample_rate": 48000,
          "language": "zh",
          "index": 0
        }
      }
    ]
  }'
```

### 场景 3：4K 高清视频上传与缩略图管理

某媒体机构需要上传 4K 纪录片，并设置自定义封面图。

**操作步骤：**

1. 创建 4K 视频对象（H.265 编码）
2. 多分片上传大文件（数 GB）
3. 上传自定义缩略图
4. 查询转码状态获取播放链接

**示例流程：**

```bash
# Step 1: 创建 4K 视频对象
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "自然纪录片 4K",
    "qualities": [{
      "resolution": "2160p",
      "type": "hls",
      "container_type": "mp4",
      "video_config": {
        "codec": "h265",
        "bitrate": 30000000,
        "index": 0
      }
    }]
  }'

# Step 2: 多分片上传（每片 100MB）
CHUNK_SIZE=104857600
FILE_SIZE=$(stat -c%s /videos/4k-doc.mp4)
CHUNKS=$(( (FILE_SIZE + CHUNK_SIZE - 1) / CHUNK_SIZE ))

for ((i=0; i<CHUNKS; i++)); do
  START=$((i * CHUNK_SIZE))
  END=$((START + CHUNK_SIZE - 1))
  [ $END -ge $FILE_SIZE ] && END=$((FILE_SIZE - 1))
  
  dd if=/videos/4k-doc.mp4 bs=1 skip=$START count=$((END - START + 1)) of=/tmp/chunk.tmp 2>/dev/null
  HASH=$(md5sum /tmp/chunk.tmp | awk '{print $1}')
  
  curl -s -X POST "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID/part" \
    -H 'stream-public-key: PUBLIC_KEY' \
    -H 'stream-secret-key: SECRET_KEY' \
    -H "Content-Range: bytes $START-$END/$FILE_SIZE" \
    -F "file=@/tmp/chunk.tmp" \
    -F "index=$i" \
    -F "hash=$HASH"
done

# Step 3: 上传自定义缩略图
curl -s -X POST "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID/thumbnail" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -F 'file=@/path/to/cover.jpg'
```

## 快速开始

### 第一步：环境检查

```bash
# 检查 Python 版本（需 3.8+）
python3 --version

# 检查 curl 与 jq
curl --version
jq --version
```

### 第二步：配置 API Key

```bash
export STREAM_PUBLIC_KEY="your_public_key"
export STREAM_SECRET_KEY="your_secret_key"
```

### 第三步：自定义编码上传

```bash
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H "stream-public-key: $STREAM_PUBLIC_KEY" \
  -H "stream-secret-key: $STREAM_SECRET_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "自定义编码视频",
    "qualities": [{
      "resolution": "1080p",
      "type": "hls",
      "container_type": "mpegts",
      "video_config": {"codec": "h264", "bitrate": 5000000, "index": 0},
      "audio_config": {"codec": "aac", "bitrate": 192000, "channels": "2", "sample_rate": 48000, "language": "zh", "index": 0}
    }]
  }'
```

### 第四步：转码费用预估

```bash
# 估算 60 秒视频、360p+1080p 双档转码费用
curl -s 'https://api-w3stream.attoaioz.cyou/api/videos/cost?duration=60&qualities=360p,1080p' \
  -H "stream-public-key: $STREAM_PUBLIC_KEY" \
  -H "stream-secret-key: $STREAM_SECRET_KEY"
```

### 第五步：批量上传

```bash
python3 batch_upload.py \
  --config /tmp/batch-upload.json \
  --parallel 8 \
  --report /tmp/upload-report.json
```

## 配置示例

### 完整配置文件模板

```yaml
# pro-config.yaml - 专业版完整配置
batch:
  parallel_workers: 8              # 并行上传数
  max_retries: 3                    # 失败重试次数
  retry_delay: 5                    # 重试间隔（秒）
  queue_file: /tmp/upload-queue.json

upload:
  chunk_size: 104857600            # 分片大小（100MB）
  max_file_size: 5368709120        # 单文件最大（5GB）
  timeout: 3600                    # 上传超时（秒）

encoding:
  default_codec: "h264"            # 默认编码器
  default_qualities: ["720p", "1080p"]  # 默认输出档位
  default_container: "mpegts"      # 默认容器
  default_audio:
    codec: "aac"
    bitrate: 192000
    channels: "2"
    sample_rate: 48000
    language: "zh"

video_management:
  default_public: true             # 默认公开
  default_tags: []
  metadata_enabled: true

thumbnail:
  auto_generate: true              # 自动生成缩略图
  custom_path: null                # 自定义缩略图路径

cost_control:
  estimate_before_upload: true     # 上传前预估费用
  max_cost_per_video: 100          # 单视频最大费用
  alert_threshold: 80              # 费用预警阈值

report:
  enabled: true
  output: /tmp/reports/upload-report.json
  include_links: true              # 包含播放链接
  include_cost: true                # 包含费用明细
```

### 支持的编码参数

| 参数 | 可选值 | 说明 |
|:-----|:-------|:-----|
| resolution | 240p-4320p | 输出分辨率 |
| codec | h264 / h265 | 视频编码器 |
| type | hls / dash | 流媒体协议 |
| container_type | mpegts / mp4 / fmp4 | 容器格式 |
| audio_codec | aac | 音频编码器 |
| channels | "2" / "1" | 声道数 |

### Apple HLS 兼容性

| 编码器 | 容器 | Apple 兼容 |
|:-------|:-----|:-----------|
| H.264 | mpegts | 支持 |
| H.264 | mp4 | 支持 |
| H.265 | mpegts | 不支持 |
| H.265 | mp4 | 支持（fMP4/CMAF） |

## 最佳实践

### 1. 多分辨率策略

```yaml
# 标准内容（性价比优先）
qualities: ["360p", "720p"]

# 高清内容（画质优先）
qualities: ["720p", "1080p"]

# 4K 内容（极致画质）
qualities: ["1080p", "2160p"]
```

### 2. 批量上传任务管理

```bash
# 查看队列状态
python3 queue_manager.py status --queue /tmp/upload-queue.json

# 暂停队列
python3 queue_manager.py pause --queue /tmp/upload-queue.json

# 断点续传
python3 batch_upload.py --resume /tmp/upload-queue.json
```

### 3. 大文件上传优化

```bash
# 推荐分片大小
# 100MB - 500MB：100MB 分片
# 500MB - 2GB：200MB 分片
# 2GB+：使用 PRO 版本自动分片

python3 batch_upload.py \
  --config batch.json \
  --chunk-size 200MB \
  --parallel 4
```

### 4. 费用控制

```bash
# 上传前预估费用
python3 cost_estimator.py \
  --duration 60 \
  --qualities 360p,720p,1080p

# 设置单视频费用上限
python3 batch_upload.py \
  --config batch.json \
  --max-cost 100
```

## 常见问题

### Q1：专业版与免费版 API Key 是否通用？

**A：** 完全通用。专业版与免费版使用相同的 API Key 与服务地址，专业版扩展的是客户端能力（批量、自定义编码等）。

### Q2：H.265 编码在 Apple 设备无法播放？

**A：** Apple HLS 对 H.265 有限制：

- H.265 + mpegts 容器：不支持
- H.265 + mp4 容器（fMP4/CMAF）：支持

建议 Apple 兼容场景使用 H.264，或使用 H.265 时指定 `container_type: mp4`。

### Q3：批量上传中部分视频失败怎么办？

**A：** 专业版自动记录失败任务：

```bash
# 仅重试失败任务
python3 batch_upload.py --retry-failed /tmp/upload-queue.json

# 从断点续传
python3 batch_upload.py --resume /tmp/upload-queue.json
```

### Q4：4K 视频转码费用如何估算？

**A：** 使用费用预估接口：

```bash
curl -s 'https://api-w3stream.attoaioz.cyou/api/videos/cost?duration=60&qualities=2160p' \
  -H "stream-public-key: $STREAM_PUBLIC_KEY" \
  -H "stream-secret-key: $STREAM_SECRET_KEY"
```

### Q5：多分片上传如何计算分片大小？

**A：** 推荐分片大小：

- 单分片：50MB 以下文件
- 多分片：50MB-200MB 每片
- 大文件自动分片：使用 PRO 版本 `--chunk-size` 参数

### Q6：视频管理 API 如何使用？

```bash
# 列出所有视频
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos' \
  -H "stream-public-key: $STREAM_PUBLIC_KEY" \
  -H "stream-secret-key: $STREAM_SECRET_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"limit": 10, "offset": 0, "status": "done"}'

# 更新视频信息
curl -s -X PATCH "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID" \
  -H "stream-public-key: $STREAM_PUBLIC_KEY" \
  -H "stream-secret-key: $STREAM_SECRET_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"title": "新标题", "tags": ["new", "tags"]}'

# 删除视频
curl -s -X DELETE "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID" \
  -H "stream-public-key: $STREAM_PUBLIC_KEY" \
  -H "stream-secret-key: $STREAM_SECRET_KEY"
```

### Q7：如何设置视频为私密？

**A：** 创建时设置 `is_public: false`：

```json
{
  "title": "私密视频",
  "is_public": false
}
```

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 规范的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（批量脚本依赖）
- **网络**：需要稳定网络连接（上传视频至流媒体平台）
- **磁盘**：建议预留 20GB+（大文件缓存）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:-------|:-----|:---------|:---------|:---------|
| Python | 运行时 | 必需 | python.org | 3.8+ |
| curl | 命令行工具 | 必需 | 系统自带 | 任意版本 |
| jq | JSON 处理 | 可选 | 系统包管理器 | 1.6+ |
| requests | Python 库 | 必需 | `pip install requests` | 2.25+ |
| PyYAML | Python 库 | 可选 | `pip install pyyaml` | 5.4+ |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |

#### 完整安装命令

```bash
# 安装 Python 依赖
pip3 install requests pyyaml

# 验证安装
python3 --version
curl --version
jq --version
```

### API Key 配置

专业版需要以下 API Key：

| API 类型 | 环境变量 | 用途 | 获取方式 |
|:---------|:---------|:-----|:---------|
| 流媒体公钥 | `STREAM_PUBLIC_KEY` | API 认证 | 流媒体平台控制台 |
| 流媒体私钥 | `STREAM_SECRET_KEY` | API 认证 | 流媒体平台控制台 |

```bash
# 配置环境变量
export STREAM_PUBLIC_KEY="your_public_key"
export STREAM_SECRET_KEY="your_secret_key"

# 验证配置
curl -s 'https://api-w3stream.attoaioz.cyou/api/videos' \
  -X POST \
  -H "stream-public-key: $STREAM_PUBLIC_KEY" \
  -H "stream-secret-key: $STREAM_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 1}'
```

### 可用性分类

- **分类**：MD+EXEC（Markdown 指令 + 命令行执行 + Python 脚本）
- **说明**：通过自然语言指令驱动 Agent 调用流媒体 API 完成高级视频上传与管理
- **离线可用**：否（依赖在线流媒体服务）
- **隐私等级**：中（视频上传至流媒体平台）
- **企业部署**：支持私有化部署客户端，无外部依赖

## 版本说明

- **当前版本**：1.0.0
- **版本类型**：PRO（专业版）
- **兼容性**：与 `video-stream-upload-free` 完全兼容，免费版 API Key 可直接使用
- **支持策略**：优先响应企业用户问题，提供工单支持
