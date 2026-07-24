---
slug: "youtube-watcher-paid"
name: "youtube-watcher-paid"
version: 1.0.1
displayName: "YouTube字幕提取-专业版"
summary: "企业级YouTube内容分析平台，支持批量字幕提取、频道监控、多语言对比与关键词追踪，适合内容研究团队。"
license: "Proprietary"
edition: "pro"
description: |-
  YouTube 内容分析专业版。Use when 需要文本翻译、多语言转换、本地化处理时使用。不适用于专业医学法律翻译认证。Use when 需要文本翻译、多语言转换、本地化处理时使用。不适用于专业医学法律翻译认证.
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
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# YouTube字幕提取-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| YouTube字幕提取-专业版ouTube内容分析 | 不支持 | 支持 |
| YouTube字幕提取-专业版频道监控 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |

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
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `批量字幕提取` 选项
- 处理流程: 接收输入 -> 执行批量字幕提取 -> 返回结果
- 输入: 用户提供批量字幕提取所需的参数和指令
- 输出: 返回批量字幕提取的处理结果,包含执行状态码、结果数据和执行日志

### 2. 频道监控与自动追踪
监控指定频道，新视频自动提取字幕：

- 频道新视频检测（定时轮询）
- 自动提取新视频字幕
- 增量更新（避免重复提取）
- 新字幕通知（邮件/Webhook）

**输入**: 用户提供频道监控与自动追踪所需的指令和必要参数.
**处理**: 解析频道监控与自动追踪的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回频道监控与自动追踪的处理结果,包含执行状态码、结果数据和执行日志.
### 3. 多语言字幕对比
单视频提取多语言字幕并对比：

- 同时提取中英文字幕
- 字幕对齐显示
- 翻译质量分析
- 适合语言学习与研究

**输入**: 用户提供多语言字幕对比所需的指令和必要参数.
**输出**: 返回多语言字幕对比的处理结果,包含执行状态码、结果数据和执行日志.
### 4. 跨视频关键词追踪
在多个视频字幕中追踪关键词：

- 关键词出现频次统计
- 关键词出现时间戳
- 关键词上下文分析
- 趋势变化追踪

**输入**: 用户提供跨视频关键词追踪所需的指令和必要参数.
**输出**: 返回跨视频关键词追踪的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 时间戳标记与全文检索
- 字幕带精确时间戳
- 全文检索（支持模糊匹配）
- 关键词定位到视频时间点
- 跳转到指定时间查看

**输入**: 用户提供时间戳标记与全文检索所需的指令和必要参数.
**输出**: 返回时间戳标记与全文检索的处理结果,包含执行状态码、结果数据和执行日志.
#
## 适用场景

### 场景 1：竞品频道批量内容分析
某市场研究团队需要分析 5 个竞品频道的最新 10 个视频内容.
**批量配置 `batch-extract.json`：**

> 详细代码示例已移至 `references/detail.md`

**执行命令：**

```bash
python3 batch_extract.py --config /path/to/batch-extract.json --parallel 8
```

**输出结构：**

```text
/tran（请参考skill目录中的脚本文件）/
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
某媒体机构需要监控科技频道的新视频，并追踪「AI」「芯片」等关键词.
**频道监控配置 `channel-monitor.yaml`：**

**执行命令：**

```bash
python3 channel_monitor.py --config /path/to/channel-monitor.yaml --daemon
# ...
python3 channel_monitor.py --config /path/to/channel-monitor.yaml --check-now
```

### 场景 3：多语言字幕对比研究
某语言研究机构需要对比同一视频的中英文字幕，分析翻译质量.
**多语言配置：**

```bash
python3 batch_extract.py \
  --url "https://www.youtube.com/watch?v=VIDEO_ID" \
  --languages zh,en \
  --align \
  --output /tran（请参考skill目录中的脚本文件）/
```

**输出示例：**

```text
/tran（请参考skill目录中的脚本文件）/
├── VIDEO_ID/
│   ├── transcript-zh.txt       # 中文字幕
│   ├── transcript-en.txt       # 英文字幕
│   ├── aligned.json            # 对齐数据
│   └── analysis-report.md      # 翻译质量分析
```

### 场景 4：关键词跨视频追踪
某研究团队需要在 100 个视频中追踪「可持续发展」相关关键词.
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

## 使用流程

### 优秀步：环境检查
```bash
python3 --version
# ...
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

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | youtube-watcher处理的内容输入 |,  |
| content | string | 否 | youtube-watcher处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "watcher 相关配置参数",
    result: "watcher 相关配置参数",
    result: "watcher 相关配置参数",
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
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 规范的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（批量脚本依赖）
- **网络**：需要网络连接（访问 YouTube）
- **磁盘**：建议预留 5GB+（字幕存储与索引）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:---:|:---:|:---:|:---:|:---:|
| Python | 运行时 | 必需 | python.org | 3.8+ |
| yt-dlp | 命令行工具 | 必需 | `pip install yt-dlp` | 2023.0+ |
| requests | Python 库 | 必需 | `pip install requests` | 2.25+ |
| PyYAML | Python 库 | 可选 | `pip install pyyaml` | 5.4+ |
| whoosh | Python 库 | 可选 | `pip install whoosh` | 2.7+（全文检索） |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |

#### 完整安装命令
```bash
pip3 install yt-dlp requests pyyaml whoosh
# ...
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

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1：专业版与免费版配置是否兼容？
**A：** 完全兼容。专业版包含免费版所有参数，单视频提取命令可直接运行。专业版扩展的是批量、监控、追踪等能力.
### Q2：批量提取中部分视频失败怎么办？
**A：** 专业版自动记录失败任务：

```bash
python3 batch_extract.py --retry-failed /tmp/extract-queue.json
# ...
python3 batch_extract.py --resume /tmp/extract-queue.json
```

### Q3：频道监控如何避免重复提取？
**A：** 专业版支持增量更新：

```bash
python3 channel_monitor.py \
  --config /tmp/channel-monitor.yaml \
  --incremental
```

已提取的视频会被记录，不会重复提取.
### Q4：多语言字幕如何对齐？
**A：** 使用 `--align` 参数：

```bash
python3 batch_extract.py \
  --url "URL" \
  --languages zh,en \
  --align
```

对齐结果保存在 `aligned.json` 中.
### Q5：关键词追踪结果如何查看？
**A：** 支持多种导出格式：

```bash
python3 keyword_tracker.py --config config.json --output report.csv
# ...
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

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

