# 详细参考 - youtube-watcher-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
batch:
  parallel_workers: 8              # 并行提取数
  max_retries: 3                    # 失败重试次数
  retry_delay: 5                    # 重试间隔（秒）
  queue_file: /tmp/extract-queue.json

extraction:
  prefer_cc: true                   # 优先 CC 字幕
  default_languages: ["zh", "en"]   # 默认提取语言
  include_timestamps: true          # 包含时间戳
  generate_summary: true            # 自动生成摘要
  summary_max_length: 500           # 摘要最大字数
monitor:
  check_interval: 3600              # 频道检查间隔（秒）
  timezone: "Asia/Shanghai"          # 时区
  incremental: true                 # 增量更新
  notification:
    webhook: ""                     # Webhook 通知地址
    email: ""                       # 邮件通知地址
keywords:
  track: []                         # 追踪关键词列表
  alert_on_match: false             # 命中时通知
  context_lines: 3                  # 上下文行数
export:
  format: "json"                    # 导出格式（json/csv/markdown）
  include_metadata: true            # 包含元数据
  output_dir: /transcripts/

report:
  enabled: true
  output: /tmp/reports/extract-report.json
  include_statistics: true          # 包含统计信息
```

## 代码示例 (yaml)

```yaml
project: 科技频道监控
output_dir: /transcripts/monitored/

channels:
  - id: "UC_channel_1"
    name: "科技频道 A"
    enabled: true
  - id: "UC_channel_2"
    name: "科技频道 B"
    enabled: true

schedule:
  check_interval: 3600              # 检查间隔（秒）
  timezone: "Asia/Shanghai"

keywords:
  track:
    - "AI"
    - "人工智能"
    - "芯片"
    - "半导体"
  alert_on_match: true              # 关键词命中时通知
  notification:
    webhook: "https://hooks.example.com/notify"

options:
  prefer_cc: true
  languages: ["zh"]
  include_timestamps: true
  generate_summary: true
```

## 代码示例 (json)

```json
{
  "project": "竞品内容分析",
  "output_dir": "/transcripts/competitors/",
  "videos": [
    {"url": "https://www.youtube.com/watch?v=VIDEO_1", "channel": "competitor-a"},
    {"url": "https://www.youtube.com/watch?v=VIDEO_2", "channel": "competitor-a"},
    {"url": "https://www.youtube.com/watch?v=VIDEO_3", "channel": "competitor-b"},
    {"url": "https://www.youtube.com/watch?v=VIDEO_4", "channel": "competitor-b"}
  ],
  "options": {
    "prefer_cc": true,
    "languages": ["zh", "en"],
    "include_timestamps": true,
    "generate_summary": true
  }
}
```

## 代码示例 (json)

```json
{
  "video_id": "VIDEO_ID",
  "title": "视频标题",
  "duration": "00:45:30",
  "language": "zh",
  "transcript": [
    {
      "timestamp": "00:00:00",
      "text": "大家好，欢迎来到本期视频"
    },
    {
      "timestamp": "00:00:05",
      "text": "今天我们来聊聊 AI"
    }
  ]
}
```

### 完整配置文件模板
```yaml
batch:
  parallel_workers: 8              # 并行提取数
  max_retries: 3                    # 失败重试次数
  retry_delay: 5                    # 重试间隔（秒）
  queue_file: /tmp/extract-queue.json

extraction:
  prefer_cc: true                   # 优先 CC 字幕
  default_languages: ["zh", "en"]   # 默认提取语言
  include_timestamps: true          # 包含时间戳
  generate_summary: true            # 自动生成摘要
  summary_max_length: 500           # 摘要最大字数
monitor:
  check_interval: 3600              # 频道检查间隔（秒）
  timezone: "Asia/Shanghai"          # 时区
  incremental: true                 # 增量更新
  notification:
    webhook: ""                     # Webhook 通知地址
    email: ""                       # 邮件通知地址
keywords:
  track: []                         # 追踪关键词列表
  alert_on_match: false             # 命中时通知
  context_lines: 3                  # 上下文行数
export:
  format: "json"                    # 导出格式（json/csv/markdown）
  include_metadata: true            # 包含元数据
  output_dir: /transcripts/

report:
  enabled: true
  output: /tmp/reports/extract-report.json
  include_statistics: true          # 包含统计信息
```



