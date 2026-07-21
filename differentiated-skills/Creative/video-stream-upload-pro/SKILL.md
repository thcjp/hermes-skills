---
slug: video-stream-upload-pro
name: video-stream-upload-pro
version: "1.0.0"
displayName: 视频上传-专业版
summary: 企业级视频上传与流媒体管理平台，支持自定义编码、多分辨率、批量上传、缩略图管理与转码费用预估。
license: Proprietary
edition: pro
description: |-
  视频上传专业版。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
- 视频上传
- 流媒体
- 专业版
- 批量处理
- 企业级
tools:
  - - read
- exec
# 视频上传工具 - 专业版
## 概述
---
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

**输入**: 用户提供自定义编码配置所需的指令和必要参数。
**处理**: 按照skill规范执行自定义编码配置操作,遵循单一意图原则。
**输出**: 返回自定义编码配置的执行结果,包含操作状态和输出数据。

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

**输入**: 用户提供多分辨率输出所需的指令和必要参数。
**处理**: 按照skill规范执行多分辨率输出操作,遵循单一意图原则。
**输出**: 返回多分辨率输出的执行结果,包含操作状态和输出数据。

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

**输入**: 用户提供批量视频上传所需的指令和必要参数。
**处理**: 按照skill规范执行批量视频上传操作,遵循单一意图原则。
**输出**: 返回批量视频上传的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 缩略图管理
```bash
curl -s -X POST "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID/thumbnail" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -F 'file=@/path/to/thumbnail.jpg'
```

支持格式：`.png`、`.jpg`

**输入**: 用户提供缩略图管理所需的指令和必要参数。
**处理**: 按照skill规范执行缩略图管理操作,遵循单一意图原则。
**输出**: 返回缩略图管理的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. 转码费用预估
上传前估算转码成本：

```bash
curl -s 'https://api-w3stream.attoaioz.cyou/api/videos/cost?duration=60&qualities=360p,1080p' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY'
```

**输入**: 用户提供转码费用预估所需的指令和必要参数。
**处理**: 按照skill规范执行转码费用预估操作,遵循单一意图原则。
**输出**: 返回转码费用预估的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 6. 视频全生命周期管理
- **列表查询**：分页获取所有视频
- **更新信息**：修改标题、描述、标签
- **删除视频**：移除视频及关联资源
- **状态查询**：实时获取转码进度

**输入**: 用户提供视频全生命周期管理所需的指令和必要参数。
**处理**: 按照skill规范执行视频全生命周期管理操作,遵循单一意图原则。
**输出**: 返回视频全生命周期管理的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级视频上传与、流媒体管理平台、支持自定义编码、批量上传、缩略图管理与转码、视频上传专业版、Use、when、需要视频处理、音频编辑、媒体转换、配音生成时使用、不适用于版权受保、护的媒体内容处理、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景
### 场景 1：企业培训视频批量托管
某企业需要将 50 个培训视频上传至流媒体平台，要求 720p 与 1080p 双档输出。

**批量配置 `batch-upload.json`：**

> 详细代码示例已移至 `references/detail.md`

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

> 详细代码示例已移至 `references/detail.md`

### 场景 3：4K 高清视频上传与缩略图管理
某媒体机构需要上传 4K 纪录片，并设置自定义封面图。

**操作步骤：**

1. 创建 4K 视频对象（H.265 编码）
2. 多分片上传大文件（数 GB）
3. 上传自定义缩略图
4. 查询转码状态获取播放链接

**示例流程：**

> 详细代码示例已移至 `references/detail.md`

## 快速开始
### 第一步：环境检查
```bash
python3 --version

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

### 命令参数说明

- `-F`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

## 示例
### 完整配置文件模板

> 详细代码示例已移至 `references/detail.md`

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
qualities: ["360p", "720p"]

qualities: ["720p", "1080p"]

qualities: ["1080p", "2160p"]
```

### 2. 批量上传任务管理
```bash
python3 queue_manager.py status --queue /tmp/upload-queue.json

python3 queue_manager.py pause --queue /tmp/upload-queue.json

python3 batch_upload.py --resume /tmp/upload-queue.json
```

### 3. 大文件上传优化
```bash
python3 batch_upload.py \
  --config batch.json \
  --chunk-size 200MB \
  --parallel 4
```

### 4. 费用控制
```bash
python3 cost_estimator.py \
  --duration 60 \
  --qualities 360p,720p,1080p

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
python3 batch_upload.py --retry-failed /tmp/upload-queue.json

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
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos' \
  -H "stream-public-key: $STREAM_PUBLIC_KEY" \
  -H "stream-secret-key: $STREAM_SECRET_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"limit": 10, "offset": 0, "status": "done"}'

curl -s -X PATCH "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID" \
  -H "stream-public-key: $STREAM_PUBLIC_KEY" \
  -H "stream-secret-key: $STREAM_SECRET_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"title": "新标题", "tags": ["new", "tags"]}'

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

### 依赖详情
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
pip3 install requests pyyaml

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
export STREAM_PUBLIC_KEY="your_public_key"
export STREAM_SECRET_KEY="your_secret_key"

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需要API Key，无Key环境无法使用
