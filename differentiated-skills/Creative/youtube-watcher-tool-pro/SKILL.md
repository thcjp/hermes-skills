---
slug: youtube-watcher-tool-pro
name: youtube-watcher-tool-pro
version: "1.0.0"
displayName: YouTube字幕提取-专业版
summary: 企业级YouTube内容分析平台，支持批量字幕提取、频道监控、多语言对比与关键词追踪，适合内容研究团队。
license: MIT
edition: pro
description: |-
  YouTube 内容分析专业版，面向企业团队与内容研究机构的高级字幕提取与分析方案。

  核心能力:
  - 批量字幕提取（50+ 视频并行）
  - 频道监控与自动追踪
  - 多语言字幕对比提取
  - 跨视频关键词追踪
  - 字幕带时间戳标记
  - 内容趋势分析
  - 自动摘要与要点提取
  - 字幕全文检索
  - 定时任务与增量更新
  - 提取结果导出（JSON/CSV/Markdown）

  适用场景:
  - 内容研究团队竞品分析
  - 媒体机构新闻素材整理
  - 教育机构课程字幕归档
  - 市场调研内容挖掘
  - 知识管理字幕库构建

  差异化:
  - 专业版支持 50+ 视频批量提取，自动并行调度
  - 内置频道监控，新视频自动提取字幕
  - 多语言字幕对比，便于跨语言内容研究
  - 与免费版完全兼容，已有配置可无缝迁移
  - 提供时间戳标记与全文检索能力

  触发关键词: 批量字幕提取, 频道监控, 多语言字幕, 关键词追踪, 内容分析, 字幕检索, channel monitor, batch transcript
tags:
- Creative
- 视频处理
- 字幕提取
- 专业版
- 批量处理
- 内容分析
- 企业级
tools:
- read
- exec
---

# YouTube 字幕提取工具 - 专业版

## 概述

YouTube 内容分析专业版是一款面向企业团队与内容研究机构的高级字幕提取与分析平台。在免费版单视频字幕提取能力之上，专业版扩展了批量提取、频道监控、多语言对比、关键词追踪等企业级能力。

专业版采用任务队列架构，支持并行提取、失败重试、断点续传，可稳定处理 50+ 视频的批量提取任务。同时完全兼容免费版配置，已有项目可无缝迁移。

### 免费版与专业版能力对比

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 单视频字幕提取 | 支持 | 支持 |
| 自动字幕 | 支持 | 支持 |
| CC 字幕 | 支持 | 支持 |
| 内容摘要 | 支持 | 支持 |
| 关键信息检索 | 支持 | 支持 |
| 视频问答 | 支持 | 支持 |
| 字幕导出 | 支持 | 支持 |
| 批量提取 | 不支持 | 50+ 并行 |
| 频道监控 | 不支持 | 支持 |
| 多语言字幕 | 不支持 | 支持 |
| 关键词追踪 | 不支持 | 支持 |
| 时间戳标记 | 不支持 | 支持 |
| 内容趋势分析 | 不支持 | 支持 |
| 全文检索 | 不支持 | 支持 |
| 定时任务 | 不支持 | 支持 |
| 结果导出 | 不支持 | JSON/CSV/MD |
| 优先支持 | 社区 | 优先响应 |

## 核心能力

### 1. 批量字幕提取

支持单任务提取 50+ 视频字幕：

```text
输入视频清单（CSV/JSON/播放列表）
      ↓
任务调度器分配并行提取
      ↓
多 yt-dlp 进程并行执行
      ↓
失败重试 + 结果聚合
      ↓
生成提取报告
```

### 2. 频道监控与自动追踪

监控指定频道，新视频自动提取字幕：

- 频道新视频检测（定时轮询）
- 自动提取新视频字幕
- 增量更新（避免重复提取）
- 新字幕通知（邮件/Webhook）

### 3. 多语言字幕对比

单视频提取多语言字幕并对比：

- 同时提取中英文字幕
- 字幕对齐显示
- 翻译质量分析
- 适合语言学习与研究

### 4. 跨视频关键词追踪

在多个视频字幕中追踪关键词：

- 关键词出现频次统计
- 关键词出现时间戳
- 关键词上下文分析
- 趋势变化追踪

### 5. 时间戳标记与全文检索

- 字幕带精确时间戳
- 全文检索（支持模糊匹配）
- 关键词定位到视频时间点
- 跳转到指定时间查看

## 使用场景

### 场景 1：竞品频道批量内容分析

某市场研究团队需要分析 5 个竞品频道的最新 10 个视频内容。

**批量配置 `batch-extract.json`：**

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

**执行命令：**

```bash
python3 batch_extract.py --config /path/to/batch-extract.json --parallel 8
```

**输出结构：**

```text
/transcripts/competitors/
├── competitor-a/
│   ├── VIDEO_1/
│   │   ├── transcript-zh.txt
│   │   ├── transcript-en.txt
│   │   ├── summary.md
│   │   └── metadata.json
│   └── VIDEO_2/
│       └── ...
├── competitor-b/
│   └── ...
└── batch-report.json   # 批量提取报告
```

### 场景 2：频道监控与关键词追踪

某媒体机构需要监控科技频道的新视频，并追踪「AI」「芯片」等关键词。

**频道监控配置 `channel-monitor.yaml`：**

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

**执行命令：**

```bash
# 启动频道监控（后台运行）
python3 channel_monitor.py --config /path/to/channel-monitor.yaml --daemon

# 手动触发检查
python3 channel_monitor.py --config /path/to/channel-monitor.yaml --check-now
```

### 场景 3：多语言字幕对比研究

某语言研究机构需要对比同一视频的中英文字幕，分析翻译质量。

**多语言配置：**

```bash
python3 batch_extract.py \
  --url "https://www.youtube.com/watch?v=VIDEO_ID" \
  --languages zh,en \
  --align \
  --output /transcripts/comparison/
```

**输出示例：**

```text
/transcripts/comparison/
├── VIDEO_ID/
│   ├── transcript-zh.txt       # 中文字幕
│   ├── transcript-en.txt       # 英文字幕
│   ├── aligned.json            # 对齐数据
│   └── analysis-report.md      # 翻译质量分析
```

### 场景 4：关键词跨视频追踪

某研究团队需要在 100 个视频中追踪「可持续发展」相关关键词。

**关键词追踪配置：**

```json
{
  "project": "可持续发展关键词追踪",
  "keywords": ["可持续发展", "碳中和", "绿色能源", "ESG"],
  "videos": [
    "https://www.youtube.com/watch?v=VIDEO_1",
    "https://www.youtube.com/watch?v=VIDEO_2"
  ],
  "options": {
    "include_timestamps": true,
    "context_lines": 3,
    "output_format": "csv"
  }
}
```

**执行命令：**

```bash
python3 keyword_tracker.py --config /path/to/keyword-config.json --parallel 8
```

## 快速开始

### 第一步：环境检查

```bash
# 检查 Python 版本（需 3.8+）
python3 --version

# 检查 yt-dlp 版本
yt-dlp --version
```

### 第二步：批量提取示例

创建视频清单：

```json
[
  {"url": "https://www.youtube.com/watch?v=VIDEO_1"},
  {"url": "https://www.youtube.com/watch?v=VIDEO_2"},
  {"url": "https://www.youtube.com/watch?v=VIDEO_3"}
]
```

执行批量提取：

```bash
python3 batch_extract.py \
  --config /tmp/videos.json \
  --output-dir /tmp/transcripts/ \
  --parallel 8 \
  --include-timestamps
```

### 第三步：频道监控

```bash
python3 channel_monitor.py \
  --config /tmp/channel-monitor.yaml \
  --daemon
```

### 第四步：关键词追踪

```bash
python3 keyword_tracker.py \
  --config /tmp/keyword-config.json \
  --keywords "AI,芯片,半导体" \
  --output /tmp/keyword-report.csv
```

## 配置示例

### 完整配置文件模板

```yaml
# pro-config.yaml - 专业版完整配置
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

### 时间戳标记格式

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

### 频道监控配置

```yaml
channels:
  - id: "UC_xxxxx"
    name: "频道名称"
    enabled: true
    max_videos: 50                  # 最多提取视频数
    languages: ["zh"]
```

## 最佳实践

### 1. 并行提取数调优

| 网络带宽 | 建议并行数 | 单视频耗时 |
|:---------|:-----------|:-----------|
| 10 Mbps | 2-3 | 5-10 秒 |
| 50 Mbps | 4-6 | 3-5 秒 |
| 100 Mbps+ | 6-8 | 1-3 秒 |

### 2. 频道监控策略

```yaml
# 高频监控（新闻类频道）
monitor:
  check_interval: 1800              # 30 分钟检查一次

# 低频监控（教育类频道）
monitor:
  check_interval: 21600             # 6 小时检查一次
```

### 3. 关键词追踪优化

```bash
# 使用同义词扩展关键词
python3 keyword_tracker.py \
  --keywords "AI,人工智能,artificial intelligence" \
  --synonyms-file /tmp/synonyms.json
```

### 4. 结果导出格式选择

| 格式 | 适用场景 | 特点 |
|:-----|:---------|:-----|
| JSON | 程序处理 | 结构化，含元数据 |
| CSV | 表格分析 | 适合 Excel 处理 |
| Markdown | 人工阅读 | 可读性最佳 |

## 常见问题

### Q1：专业版与免费版配置是否兼容？

**A：** 完全兼容。专业版包含免费版所有参数，单视频提取命令可直接运行。专业版扩展的是批量、监控、追踪等能力。

### Q2：批量提取中部分视频失败怎么办？

**A：** 专业版自动记录失败任务：

```bash
# 仅重试失败任务
python3 batch_extract.py --retry-failed /tmp/extract-queue.json

# 从断点续传
python3 batch_extract.py --resume /tmp/extract-queue.json
```

### Q3：频道监控如何避免重复提取？

**A：** 专业版支持增量更新：

```bash
python3 channel_monitor.py \
  --config /tmp/channel-monitor.yaml \
  --incremental
```

已提取的视频会被记录，不会重复提取。

### Q4：多语言字幕如何对齐？

**A：** 使用 `--align` 参数：

```bash
python3 batch_extract.py \
  --url "URL" \
  --languages zh,en \
  --align
```

对齐结果保存在 `aligned.json` 中。

### Q5：关键词追踪结果如何查看？

**A：** 支持多种导出格式：

```bash
# CSV 格式（适合 Excel）
python3 keyword_tracker.py --config config.json --output report.csv

# JSON 格式（适合程序处理）
python3 keyword_tracker.py --config config.json --output report.json
```

### Q6：如何监控多个频道？

**A：** 在配置文件中添加多个频道：

```yaml
channels:
  - id: "UC_channel_1"
    name: "频道 A"
  - id: "UC_channel_2"
    name: "频道 B"
  - id: "UC_channel_3"
    name: "频道 C"
```

### Q7：提取的字幕可以全文检索吗？

**A：** 专业版支持全文检索：

```bash
# 在已提取的字幕中检索
python3 search_engine.py \
  --index /transcripts/ \
  --query "关键词" \
  --output /tmp/search-results.json
```

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 规范的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（批量脚本依赖）
- **网络**：需要网络连接（访问 YouTube）
- **磁盘**：建议预留 5GB+（字幕存储与索引）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:-------|:-----|:---------|:---------|:---------|
| Python | 运行时 | 必需 | python.org | 3.8+ |
| yt-dlp | 命令行工具 | 必需 | `pip install yt-dlp` | 2023.0+ |
| requests | Python 库 | 必需 | `pip install requests` | 2.25+ |
| PyYAML | Python 库 | 可选 | `pip install pyyaml` | 5.4+ |
| whoosh | Python 库 | 可选 | `pip install whoosh` | 2.7+（全文检索） |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |

#### 完整安装命令

```bash
# 安装 Python 依赖
pip3 install yt-dlp requests pyyaml whoosh

# 验证安装
python3 --version
yt-dlp --version
python3 -c "import requests; print('requests ready')"
```

### API Key 配置

- 本 Skill 纯本地运行，**无需任何 API Key**
- 字幕提取通过 yt-dlp 公开接口完成
- 如需访问私人视频或避免限流，可配置 YouTube Cookie（可选）

```bash
# 可选：配置 YouTube Cookie
# 用于访问私人视频或会员视频
yt-dlp --cookies /path/to/cookies.txt "URL"
```

### 可用性分类

- **分类**：MD+EXEC（Markdown 指令 + 命令行执行 + Python 脚本）
- **说明**：通过自然语言指令驱动 Agent 调用 Python 脚本完成批量字幕提取与分析
- **离线可用**：否（需要网络访问 YouTube）
- **隐私等级**：高（字幕本地处理与存储）
- **企业部署**：支持私有化部署，字幕库本地存储

## 版本说明

- **当前版本**：1.0.0
- **版本类型**：PRO（专业版）
- **兼容性**：与 `youtube-watcher-tool-free` 完全兼容，免费版配置可直接迁移
- **支持策略**：优先响应企业用户问题，提供工单支持
