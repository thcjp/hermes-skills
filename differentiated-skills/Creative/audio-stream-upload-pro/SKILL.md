---
slug: audio-stream-upload-pro
name: audio-stream-upload-pro
version: "1.0.0"
displayName: 音频流上传专业版
summary: 企业级音频上传工具，支持批量上传、自定义编码、多质量预设、分片上传与元数据管理。
license: Proprietary
edition: pro
description: |-
  音频流上传专业版 —— 面向企业团队与专业创作者的高级音频上传工具。核心能力:
  - 批量音频上传，支持队列管理与断点续传
  - 完全自定义编码配置：比特率、采样率、声道、编解码器
  - 多质量预设输出（标准/良好/最高/无损），满足不同播放场景
  - HLS与DASH双流媒体格式支持，适配多终端播放
  - 丰富的元数据管理：标签、描述、自定义键值对
  - 分片上传支持大文件...
tags:
- 音频处理
- 流媒体
- 企业工具
- 批量处理
- 编码配置
tools:
  - - read
- exec
---
# 音频流上传专业版

## 概述

音频流上传专业版是企业级音频上传工具，在免费版三步上传流程（创建 → 上传 → 完成）基础上，提供批量上传、完全自定义编码配置、多质量预设、HLS/DASH双格式支持、分片上传与元数据管理等高级能力。适用于音频内容平台、专业音乐团队、企业培训系统等专业场景。

### 免费版与专业版对比

| 能力 | 免费版 | 专业版 |
| --- | --- | --- |
| 基础三步上传 | 支持 | 支持 |
| 批量上传 | 不支持 | 支持（队列管理） |
| 自定义编码 | 不支持 | 完全自定义 |
| 多质量预设 | 默认配置 | 标准/良好/最高/无损 |
| 流媒体格式 | HLS | HLS + DASH |
| 分片上传 | 不支持 | 支持（自动分片） |
| 元数据管理 | 仅标题 | 标签、描述、自定义键值 |
| 断点续传 | 不支持 | 支持 |
| 失败重试 | 手动 | 自动重试机制 |

## 核心能力

### 1. 批量上传与队列管理

```python
import requests
import hashlib
import os
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

class AudioBatchUploader:
    def __init__(self, public_key, secret_key, max_workers=3):
        self.public_key = public_key
        self.secret_key = secret_key
        self.base_url = 'https://api-w3stream.attoaioz.cyou/api'
        self.max_workers = max_workers
        self.results = []
        self.failed = []

    @property
    def headers(self):
        return {
            'stream-public-key': self.public_key,
            'stream-secret-key': self.secret_key
        }

    def upload_single(self, file_path, title, config=None):
        """上传单个音频文件，支持自定义编码配置"""
        try:
            # 步骤1：创建音频对象
            create_data = {'title': title, 'type': 'audio'}
            if config:
                create_data.update(config)
            
            resp = requests.post(
                f'{self.base_url}/videos/create',
                headers={**self.headers, 'Content-Type': 'application/json'},
                json=create_data
            )
            audio_id = resp.json()['data']['id']

            # 步骤2：上传文件
            file_size = os.path.getsize(file_path)
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            
            with open(file_path, 'rb') as f:
                requests.post(
                    f'{self.base_url}/videos/{audio_id}/part',
                    headers={
                        **self.headers,
                        'Content-Range': f'bytes 0-{file_size-1}/{file_size}'
                    },
                    files={'file': f},
                    data={'index': 0, 'hash': file_hash}
                )

            # 步骤3：完成上传
            requests.get(
                f'{self.base_url}/videos/{audio_id}/complete',
                headers={'accept': 'application/json', **self.headers}
            )
            
            self.results.append({'file': file_path, 'audio_id': audio_id, 'status': 'success'})
            return audio_id
        except Exception as e:
            self.failed.append({'file': file_path, 'error': str(e)})
            return None

    def batch_upload(self, file_list, config=None):
        """批量上传音频文件"""
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self.upload_single, item['path'], item['title'], config): item
                for item in file_list
            }
            for future in as_completed(futures):
                future.result()
        
        print(f"成功: {len(self.results)}, 失败: {len(self.failed)}")
        return {'success': self.results, 'failed': self.failed}

    def retry_failed(self, config=None):
        """重试失败的 uploads"""
        retry_list = [{'path': f['file'], 'title': os.path.basename(f['file'])} for f in self.failed]
        self.failed = []
        return self.batch_upload(retry_list, config)
```

### 2. 自定义编码配置

```python
# 最高质量HLS配置
HIGHEST_QUALITY_CONFIG = {
    "description": "高品质音乐上传",
    "is_public": True,
    "tags": ["music", "high-quality"],
    "metadata": [
        {"key": "artist", "value": "艺术家名"},
        {"key": "album", "value": "专辑名"},
        {"key": "track_number", "value": "01"}
    ],
    "qualities": [
        {
            "resolution": "highest",
            "type": "hls",
            "container_type": "mpegts",
            "audio_config": {
                "codec": "aac",
                "bitrate": 320000,
                "channels": "2",
                "sample_rate": 48000,
                "language": "zh",
                "index": 0
            }
        }
    ]
}

# 多质量自适应配置（适配不同网络环境）
ADAPTIVE_QUALITY_CONFIG = {
    "qualities": [
        {
            "resolution": "highest",
            "type": "hls",
            "container_type": "mpegts",
            "audio_config": {
                "codec": "aac", "bitrate": 320000,
                "channels": "2", "sample_rate": 48000, "index": 0
            }
        },
        {
            "resolution": "standard",
            "type": "hls",
            "container_type": "mpegts",
            "audio_config": {
                "codec": "aac", "bitrate": 128000,
                "channels": "2", "sample_rate": 44100, "index": 0
            }
        }
    ]
}

# DASH格式配置（适配Web端播放）
DASH_CONFIG = {
    "qualities": [
        {
            "resolution": "highest",
            "type": "dash",
            "container_type": "fmp4",
            "audio_config": {
                "codec": "aac", "bitrate": 256000,
                "channels": "2", "sample_rate": 48000, "index": 0
            }
        }
    ]
}
```

### 3. 分片上传大文件

```python
def upload_large_file(self, file_path, title, chunk_size=10*1024*1024):
    """分片上传大文件，支持断点续传"""
    file_size = os.path.getsize(file_path)
    
    # 创建音频对象
    resp = requests.post(f'{self.base_url}/videos/create',
        headers={**self.headers, 'Content-Type': 'application/json'},
        json={'title': title, 'type': 'audio'})
    audio_id = resp.json()['data']['id']
    
    # 分片上传
    chunk_index = 0
    uploaded_chunks = self.get_upload_progress(audio_id)  # 断点续传检查
    
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            if chunk_index in uploaded_chunks:
                chunk_index += 1
                continue
            
            chunk_hash = hashlib.md5(chunk).hexdigest()
            start = chunk_index * chunk_size
            end = min(start + len(chunk) - 1, file_size - 1)
            
            requests.post(f'{self.base_url}/videos/{audio_id}/part',
                headers={**self.headers, 'Content-Range': f'bytes {start}-{end}/{file_size}'},
                files={'file': chunk},
                data={'index': chunk_index, 'hash': chunk_hash})
            
            chunk_index += 1
    
    # 完成上传
    requests.get(f'{self.base_url}/videos/{audio_id}/complete',
        headers={'accept': 'application/json', **self.headers})
    return audio_id
```

## 使用场景

### 场景一：音频内容平台批量入库

平台运营团队需要将大量音频内容批量上传至流媒体平台，支持自定义编码与元数据。

```bash
# 批量上传脚本
python3 -c "
from uploader import AudioBatchUploader

uploader = AudioBatchUploader(
    public_key='YOUR_PUBLIC_KEY',
    secret_key='YOUR_SECRET_KEY',
    max_workers=3
)

# 定义上传任务
file_list = [
    {'path': '/audio/episode01.mp3', 'title': '节目第一期'},
    {'path': '/audio/episode02.mp3', 'title': '节目第二期'},
    {'path': '/audio/episode03.mp3', 'title': '节目第三期'},
]

# 使用自适应质量配置批量上传
result = uploader.batch_upload(file_list, config=ADAPTIVE_QUALITY_CONFIG)
print(f'上传结果: {result}')

# 重试失败的 uploads
if result['failed']:
    uploader.retry_failed(config=ADAPTIVE_QUALITY_CONFIG)
"
```

### 场景二：专业音乐多版本发布

音乐制作团队上传同一作品的不同质量版本，适配不同播放场景。

```bash
# 上传无损品质版本
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H 'stream-public-key: YOUR_PUBLIC_KEY' \
  -H 'stream-secret-key: YOUR_SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "原创音乐 - 无损版",
    "type": "audio",
    "description": "高品质无损音乐",
    "tags": ["music", "lossless", "original"],
    "metadata": [
      {"key": "artist", "value": "音乐人"},
      {"key": "bpm", "value": "120"},
      {"key": "genre", "value": "电子"}
    ],
    "qualities": [
      {
        "resolution": "lossless",
        "type": "hls",
        "container_type": "mpegts",
        "audio_config": {
          "codec": "aac",
          "bitrate": 320000,
          "channels": "2",
          "sample_rate": 96000,
          "language": "zh",
          "index": 0
        }
      }
    ]
  }'
```

### 场景三：企业培训音频管理系统

企业内部培训系统批量上传培训音频，支持元数据分类管理与DASH格式播放。

```python
# 企业培训音频批量上传
training_audio_list = [
    {'path': '/training/onboarding_01.mp3', 'title': '新人培训-公司文化'},
    {'path': '/training/onboarding_02.mp3', 'title': '新人培训-制度规范'},
    {'path': '/training/safety_01.mp3', 'title': '安全培训-基础篇'},
]

ENTERPRISE_CONFIG = {
    "is_public": False,
    "tags": ["企业培训", "内部资料"],
    "metadata": [
        {"key": "department", "value": "人力资源部"},
        {"key": "category", "value": "新人培训"},
        {"key": "version", "value": "2026.1"}
    ],
    "qualities": [
        {
            "resolution": "standard",
            "type": "dash",
            "container_type": "fmp4",
            "audio_config": {
                "codec": "aac", "bitrate": 128000,
                "channels": "2", "sample_rate": 44100, "index": 0
            }
        }
    ]
}

uploader = AudioBatchUploader('YOUR_PUBLIC_KEY', 'YOUR_SECRET_KEY', max_workers=5)
result = uploader.batch_upload(training_audio_list, config=ENTERPRISE_CONFIG)
```

## 不适用场景

以下场景音频流上传专业版不适合处理：

- 版权受保护的媒体内容处理
- 实时直播推流
- 专业影视后期


## 触发条件

需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于非本工具能力范围的需求。


## 快速开始

### 1. 环境准备

```bash
# 依赖说明
pip install requests

# 配置环境变量
export STREAM_PUBLIC_KEY="your_public_key"
export STREAM_SECRET_KEY="your_secret_key"
```

### 2. 自定义编码上传

```bash
# 使用自定义编码配置创建音频对象
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H "stream-public-key: $STREAM_PUBLIC_KEY" \
  -H "stream-secret-key: $STREAM_SECRET_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"title":"专业音频","type":"audio","qualities":[{"resolution":"highest","type":"hls","audio_config":{"codec":"aac","bitrate":320000,"channels":"2","sample_rate":48000,"index":0}}]}'
```

## 示例

### 质量预设参考

| 预设 | 分辨率字段 | 适用场景 |
| --- | --- | --- |
| 标准 | `standard` | 语音内容、播客 |
| 良好 | `good` | 日常音乐播放 |
| 最高 | `highest` | 高品质音乐 |
| 无损 | `lossless` | 专业音乐制作 |

### 比特率推荐

| 内容类型 | 推荐比特率 | 推荐采样率 |
| --- | --- | --- |
| 语音/播客 | 64000-128000 | 22050或32000 |
| 标准音乐 | 128000-192000 | 44100 |
| 高品质音乐 | 192000-256000 | 48000 |
| 无损音乐 | 256000-320000 | 96000 |

### 流媒体格式对比

| 格式 | type字段 | 容器格式 | 适用场景 |
| --- | --- | --- | --- |
| HLS | `hls` | mpegts / mp4 | 移动端、直播 |
| DASH | `dash` | fmp4 | Web端、自适应码率 |

## 最佳实践

1. **批量上传并发控制**：建议并发数控制在3-5个，避免API限流
2. **编码配置选择**：语音内容使用标准预设即可，音乐内容建议最高或无损
3. **元数据完整性**：充分利用标签和自定义键值对，便于内容检索和管理
4. **分片大小**：大文件分片建议10MB一片，平衡上传速度与内存占用
5. **失败重试策略**：实现指数退避重试机制，避免短时间内大量重试
6. **多质量输出**：同时配置标准和最高两个质量预设，适配不同网络环境
7. **格式选择**：移动端优先HLS，Web端优先DASH，兼顾两端可同时配置

## 常见问题

### Q1：批量上传时遇到API限流怎么办？

降低并发数至2-3个，并在请求间添加适当延迟。专业版支持自动限流检测与退避重试。

### Q2：分片上传中断后如何恢复？

专业版支持断点续传。通过记录已上传的分片索引，重新上传时跳过已完成的分片即可。

### Q3：HLS和DASH应该选哪个？

移动端和直播场景优先HLS，Web端自适应码率播放优先DASH。如需同时覆盖两端，可配置两种格式。

### Q4：自定义编码配置中的bitrate单位是什么？

bitrate单位为bits/sec，例如320kbps应写为320000，128kbps应写为128000。

### Q5：与免费版的API密钥是否通用？

是的，专业版与免费版使用相同的API密钥体系，`stream-public-key`和`stream-secret-key`完全通用。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8及以上
- **命令行工具**: curl、md5sum（或md5命令）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| curl | 系统工具 | 必需 | 系统自带或包管理器安装 |
| 流媒体平台API | 外部API | 必需 | 在平台注册获取 |
| Python 3 | 运行时 | 必需 | python.org 下载安装 |
| requests | Python库 | 必需 | `pip install requests` |
| concurrent.futures | Python标准库 | 必需 | Python自带 |

### API Key 配置

- `stream-public-key`：流媒体平台公钥，通过HTTP头发送
- `stream-secret-key`：流媒体平台密钥，通过HTTP头发送
- 与免费版使用相同的密钥体系，完全兼容

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，核心功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行高级音频上传任务。支持批量处理、自定义编码、分片上传等企业级功能，通过Python脚本实现复杂逻辑。与免费版完全兼容，可直接复用免费版的API密钥与基础上传流程。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用
