# 详细参考 - video-stream-upload-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (bash)

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

## 代码示例 (bash)

```bash
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

curl -s -X POST "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID/thumbnail" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -F 'file=@/path/to/cover.jpg'
```

## 代码示例 (yaml)

```yaml
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

## 代码示例 (json)

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

