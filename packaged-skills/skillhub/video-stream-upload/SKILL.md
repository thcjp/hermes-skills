---
slug: "video-stream-upload"
name: "video-stream-upload"
version: "1.0.0"
displayName: "视频上传-专业版"
summary: "企业级视频上传与流媒体管理平台，支持自定义编码、多分辨率、批量上传、缩略图管理与转码费用预估。"
license: "Proprietary"
edition: "pro"
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
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# 视频上传-专业版

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

### 1. 自定义编码配置
支持完整编码参数自定义：

- **分辨率**：240p / 360p / 480p / 720p / 1080p / 1440p / 2160p / 4320p
- **编码器**：H.264（最高 4K）/ H.265（最高 8K）
- **流媒体协议**：HLS / DASH
- **容器格式**：mpegts / mp4 / fmp4
- **码率**：自定义视频与音频码率
- **音频配置**：采样率、声道数、语言

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
| 4320p | 7680×4320 | 60,000,000 bps | 8K 优秀画质 |

**输入**: 用户提供多分辨率输出所需的指令和必要参数。
**处理**: 按照skill规范执行多分辨率输出操作,遵循单一意图原则。

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
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `批量视频上传` 选项
- 处理流程: 接收输入 -> 执行批量视频上传 -> 返回结果
- 输入: 用户提供批量视频上传所需的参数和指令
- 输出: 返回批量视频上传的执行结果,包含操作状态和输出数据

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

### 5. 转码费用预估
上传前估算转码成本：

```bash
curl -s 'https://api-w3stream.attoaioz.cyou/api/videos/cost?duration=60&qualities=360p,1080p' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY'
```

**输入**: 用户提供转码费用预估所需的指令和必要参数。
**处理**: 按照skill规范执行转码费用预估操作,遵循单一意图原则。
**输出**: 返回转码费用预估的执行结果,包含操作状态和输出数据。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `转码费用预估` 选项

### 6. 视频全生命周期管理
- **列表查询**：分页获取所有视频
- **更新信息**：修改标题、描述、标签
- **删除视频**：移除视频及关联资源
- **状态查询**：实时获取转码进度

**输入**: 用户提供视频全生命周期管理所需的指令和必要参数。
**处理**: 按照skill规范执行视频全生命周期管理操作,遵循单一意图原则。
**输出**: 返回视频全生命周期管理的执行结果,包含操作状态和输出数据。

#
## 适用场景

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

## 使用流程

### 优秀步：环境检查
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

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
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
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 规范的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（批量脚本依赖）
- **网络**：需要稳定网络连接（上传视频至流媒体平台）
- **磁盘**：建议预留 20GB+（大文件缓存）

### 依赖说明
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

## 案例展示

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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
