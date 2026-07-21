---
slug: youtube-watcher-tool-pro
name: youtube-watcher-tool-pro
version: "1.0.0"
displayName: YouTube字幕提取-专业版
summary: 企业级YouTube内容分析平台，支持批量字幕提取、频道监控、多语言对比与关键词追踪，适合内容研究团队。
license: Proprietary
edition: pro
description: |-
  YouTube 内容分析专业版。Use when 需要文本翻译、多语言转换、本地化处理时使用。不适用于专业医学法律翻译认证。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要文本翻译、多语言转换、本地化处理时使用。不适用于专业医学法律翻译认证。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
- 视频处理
- 字幕提取
- 专业版
- 批量处理
- 内容分析
- 企业级
tools:
  - - read
- exec
# YouTube 字幕提取工具 - 专业版
## 概述
---
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

> 详细代码示例已移至 `references/detail.md`

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

> 详细代码示例已移至 `references/detail.md`

**执行命令：**

```bash
python3 channel_monitor.py --config /path/to/channel-monitor.yaml --daemon

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
python3 --version

yt-dlp --version
```

### 示例
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

> 详细内容已移至 `references/detail.md` - ### 完整配置文件模板
### 时间戳标记格式

> 详细代码示例已移至 `references/detail.md`

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
monitor:
  check_interval: 1800              # 30 分钟检查一次
monitor:
  check_interval: 21600             # 6 小时检查一次
```

### 3. 关键词追踪优化
```bash
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
python3 batch_extract.py --retry-failed /tmp/extract-queue.json

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
python3 keyword_tracker.py --config config.json --output report.csv

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

### 依赖说明
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
pip3 install yt-dlp requests pyyaml whoosh

python3 --version
yt-dlp --version
python3 -c "import requests; print('requests ready')"
```

### API Key 配置
- 本 Skill 纯本地运行，**无需任何 API Key**
- 字幕提取通过 yt-dlp 公开接口完成
- 如需访问私人视频或避免限流，可配置 YouTube Cookie（可选）

```bash
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

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
