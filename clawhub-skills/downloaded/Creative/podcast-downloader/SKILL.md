---
slug: podcast-downloader
name: podcast-downloader
version: "1.0.0"
displayName: Podcast Downloader
summary: 小宇宙播客下载工具。从小宇宙(xiaoyuzhoufm.com)下载播客音频和Show Notes。自动转换为MP3格式（兼容Sanag、小游等骨传导蓝牙耳机、水下游泳时离线播放）。当用户需要下...
license: MIT-0
description: |-
  小宇宙播客下载工具。从小宇宙(xiaoyuzhoufm.com)下载播客音频和Show Notes。自动转换为MP3格式（兼容Sanag、小游等骨传导蓝牙耳机、水下游泳时离线播放）。当用户需要下...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: xiaoyuzhoufm, 下载播客音频, show, 从小宇宙, 小宇宙播客下, 自动转换为, downloader, 载工具
tags:
- Creative
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
