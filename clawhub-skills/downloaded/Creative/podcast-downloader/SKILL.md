---
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
---

# Podcast Downloader

Download podcast audio and show notes from xiaoyuzhoufm.com (小宇宙).

## Quick Start

```bash
./scripts/download.sh "https://www.xiaoyuzhoufm.com/episode/abc123def456ghi789jklmno"
```

## Output

```text
/Users/zym/Documents/podcast/  # Baidu cloud sync directory
└── PodcastName-EpisodeTitle/
    ├── EpisodeTitle.mp3
    └── EpisodeTitle.md
```

## Workflow

1. **Extract Info** - Parse `__NEXT_DATA__` JSON from episode page
2. **Download m4a** - Get audio file from CDN
3. **Convert to MP3** - Required for Bluetooth headphones compatibility
4. **Delete m4a** - Save disk space
5. **Save Show Notes** - Extract shownotes as markdown

## Requirements

* `curl` - HTTP requests
* `jq` - JSON parsing
* `ffmpeg` - Audio conversion

## Environment Variables

| Variable | Default | Description |
| --- | --- | --- |
| `PODCAST_DIR` | `/Users/zym/Documents/podcast/` | Output directory (Baidu cloud sync) |
| `AUDIO_QUALITY` | `0` | MP3 quality (0=best, 2=good, 4=normal) |
| `KEEP_M4A` | `false` | Keep original m4a file |

## Quick Reference

| Task | Command |
| --- | --- |
| Download single episode | `./scripts/download.sh <URL>` |
| Batch download | See reference.md |
| Custom quality | `AUDIO_QUALITY=2 ./scripts/download.sh <URL>` |
| Keep m4a | `KEEP_M4A=true ./scripts/download.sh <URL>` |

## Files

* `SKILL.md` - This file (quick start)
* `reference.md` - Advanced usage, batch download, troubleshooting
* `scripts/download.sh` - Main download script
* `LICENSE.txt` - MIT License

## Next Steps

* For batch download, see reference.md
* For troubleshooting, see reference.md

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 从小宇宙(xiaoyuzhoufm
- com)下载播客音频和Show Notes
- 自动转换为MP3格式（兼容Sanag、小游等骨传导蓝牙耳机、水下游泳时离线播放）
- 触发关键词: xiaoyuzhoufm, 下载播客音频, show, 从小宇宙, 小宇宙播客下, 自动转换为, downloader, 载工具

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
```bash
./scripts/download.sh "https://www.xiaoyuzhoufm.com/episode/abc123def456ghi789jklmno"
```
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Podcast Downloader？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Podcast Downloader有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
