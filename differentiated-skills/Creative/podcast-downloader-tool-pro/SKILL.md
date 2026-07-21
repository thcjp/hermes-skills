---
slug: podcast-downloader-tool-pro
name: podcast-downloader-tool-pro
version: "1.0.0"
displayName: 播客下载工具专业版
summary: 企业级播客下载工具,支持批量下载、播放列表订阅、定时同步与多平台扩展,适配生产环境。
license: Proprietary
edition: pro
description: |-
  面向团队与高级用户的播客下载工具(专业版)。核心能力:
  - 涵盖免费版全部能力(单集下载、MP3 转换、节目笔记)
  - 批量下载:URL 列表与目录级处理
  - 播放列表订阅:自动跟踪节目更新
  - 定时同步:cron 任务自动下载新集
  - 多平台扩展:支持小宇宙及其他播客源
  - 元数据管理:ID3 标签与封面嵌入
  - 去重与断点续传
  - 下载队列与并发控制
  - API 服务化:远程触发下载

  适用场景:
  - 播客矩阵批量归档
  - 自动化订阅与同步
  - 团队共享播客库
  - 内容分析数据采集
  -...
tags:
- 创意设计
- 播客
- 下载工具
- 企业级
- 批量下载
- 自动订阅
- 多平台
tools:
  - - read
- exec
---
# 播客下载工具 - 专业版

## 概述

播客下载工具(专业版)在免费版(`podcast-downloader-tool-free`)单集下载能力之上,新增批量下载、播放列表订阅、定时同步、多平台扩展与元数据管理等企业级能力。适合需要大规模下载与自动化的内容团队。

专业版与免费版命令完全兼容,已使用免费版的脚本无需修改即可运行。升级后可启用高级特性。

## 核心能力

### 免费版 vs 专业版对比

| 能力 | 免费版 | 专业版 | 增量价值 |
|:-----|:-------|:-------|:---------|
| 单集下载 | 支持 | 支持 | - |
| MP3 转换 | 支持 | 支持 | - |
| 节目笔记 | 支持 | 支持 | - |
| 自定义音质 | 支持 | 支持 | - |
| 批量下载 | 不支持 | URL 列表 + 目录 | 生产力 |
| 播放列表订阅 | 不支持 | 自动跟踪更新 | 自动化 |
| 定时同步 | 不支持 | cron 任务 | 零干预 |
| 多平台 | 不支持 | 小宇宙 + RSS + 其他 | 覆盖广 |
| 元数据管理 | 不支持 | ID3 + 封面 | 媒体库 |
| 去重 | 不支持 | 哈希校验 | 避免重复 |
| 断点续传 | 不支持 | 支持 | 容错 |
| 并发控制 | 不支持 | 队列 + 并发 | 高吞吐 |
| API 服务 | 不支持 | FastAPI | 远程调用 |

## 使用场景

### 场景一:批量下载多个单集

从 URL 列表批量下载。

```bash
#!/bin/bash
# batch_download.sh - 批量下载

URL_FILE="download_list.txt"
OUTPUT_DIR="/data/podcasts"
MAX_PARALLEL=3

# 读取 URL 列表
mapfile -t URLs < "$URL_FILE"

# 并发下载
for url in "${URLs[@]}"; do
    # 控制并发数
    while [ $(jobs -r | wc -l) -ge $MAX_PARALLEL ]; do
        sleep 1
    done

    PODCAST_DIR="$OUTPUT_DIR" ./scripts/download.sh "$url" &
done

wait
echo "批量下载完成: ${#URLs[@]} 集"
```

```text
# download_list.txt
https://www.xiaoyuzhoufm.com/episode/abc123
https://www.xiaoyuzhoufm.com/episode/def456
https://www.xiaoyuzhoufm.com/episode/ghi789
```

### 场景二:订阅与自动同步

订阅播客节目,自动下载新集。

```python
import os
import json
import time
import hashlib
from pathlib import Path
import requests

class PodcastSubscriber:
    """播客订阅管理器"""

    def __init__(self, config_file="subscriptions.json"):
        self.config_file = config_file
        self.subscriptions = self._load()
        self.downloaded = self._load_downloaded()

    def _load(self):
        """加载订阅配置"""
        try:
            with open(self.config_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"shows": []}

    def _load_downloaded(self):
        """加载已下载记录(去重)"""
        try:
            with open(".downloaded.json", "r", encoding="utf-8") as f:
                return set(json.load(f))
        except FileNotFoundError:
            return set()

    def subscribe(self, show_name, feed_url, platform="xiaoyuzhoufm"):
        """订阅新节目"""
        self.subscriptions["shows"].append({
            "name": show_name,
            "feed_url": feed_url,
            "platform": platform,
            "last_checked": None,
            "auto_download": True,
            "quality": 2,
            "output_dir": f"/data/podcasts/{show_name}"
        })
        self._save()

    def check_updates(self):
        """检查所有订阅的更新"""
        new_episodes = []
        for show in self.subscriptions["shows"]:
            episodes = self._fetch_episodes(show)
            for ep in episodes:
                ep_hash = hashlib.md5(ep["url"].encode()).hexdigest()
                if ep_hash not in self.downloaded:
                    new_episodes.append((show, ep))
        return new_episodes

    def sync(self):
        """同步下载所有新集"""
        new_eps = self.check_updates()
        for show, ep in new_eps:
            print(f"下载: {show['name']} - {ep['title']}")
            os.system(
                f"PODCAST_DIR={show['output_dir']} "
                f"AUDIO_QUALITY={show['quality']} "
                f"./scripts/download.sh {ep['url']}"
            )
            ep_hash = hashlib.md5(ep["url"].encode()).hexdigest()
            self.downloaded.add(ep_hash)
        self._save_downloaded()
        print(f"同步完成: 新增 {len(new_eps)} 集")

    def _save(self):
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(self.subscriptions, f, ensure_ascii=False, indent=2)

    def _save_downloaded(self):
        with open(".downloaded.json", "w", encoding="utf-8") as f:
            json.dump(list(self.downloaded), f)

# 使用
sub = PodcastSubscriber()
sub.subscribe("独立开发者", "https://www.xiaoyuzhoufm.com/podcast/abc123")
sub.sync()
```

### 场景三:定时同步(cron)

配置定时任务自动同步。

```bash
# 编辑 crontab
crontab -e

# 每天早上 6 点同步下载
0 6 * * * cd /path/to/podcast-downloader && python subscriber.py sync >> /var/log/podcast-sync.log 2>&1

# 每周日凌晨清理 30 天前的已下载记录
0 3 * * 0 find /data/podcasts -name "*.mp3" -mtime +30 -delete
```

### 场景四:元数据管理

为下载的音频嵌入 ID3 标签与封面。

```python
import subprocess
import os

def embed_metadata(mp3_path, title, artist, album, cover_path=None):
    """嵌入 ID3 元数据"""
    cmd = [
        "ffmpeg", "-y", "-i", mp3_path,
        "-metadata", f"title={title}",
        "-metadata", f"artist={artist}",
        "-metadata", f"album={album}",
        "-metadata", "genre=Podcast",
        "-codec", "copy"
    ]

    if cover_path and os.path.exists(cover_path):
        cmd.extend(["-i", cover_path, "-map", "0:a", "-map", "1:v",
                   "-c:v", "mjpeg", "-disposition:v", "attached_pic"])

    cmd.append(mp3_path.replace(".mp3", "_tagged.mp3"))
    subprocess.run(cmd, check=True)

    # 替换原文件
    os.replace(mp3_path.replace(".mp3", "_tagged.mp3"), mp3_path)
```

## 不适用场景

以下场景播客下载工具专业版不适合处理：

- 需要人工创意判断的任务
- 非结构化头脑风暴
- 人际沟通协调


## 触发条件

需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于非本工具能力范围的需求。


## 快速开始

### 依赖说明

```bash
# 基础依赖(同免费版)
brew install curl jq ffmpeg  # macOS
# 或
sudo apt install curl jq ffmpeg  # Linux

# Python 依赖(订阅功能)
pip install requests
```

### 2. 配置订阅

```json
// subscriptions.json
{
  "shows": [
    {
      "name": "独立开发者",
      "feed_url": "https://www.xiaoyuzhoufm.com/podcast/abc123",
      "platform": "xiaoyuzhoufm",
      "auto_download": true,
      "quality": 2,
      "output_dir": "/data/podcasts/indie-maker"
    },
    {
      "name": "设计对谈",
      "feed_url": "https://www.xiaoyuzhoufm.com/podcast/def456",
      "platform": "xiaoyuzhoufm",
      "auto_download": true,
      "quality": 0,
      "output_dir": "/data/podcasts/design-talk"
    }
  ]
}
```

### 3. 启动同步

```bash
# 手动同步一次
python subscriber.py sync

# 配置定时任务
crontab -e
# 0 6 * * * cd /path/to/tool && python subscriber.py sync
```

## 示例

### 批量下载配置

```yaml
# batch-config.yaml
batch:
  url_file: "download_list.txt"
  output_dir: "/data/podcasts"
  max_parallel: 3
  quality: 2
  keep_m4a: false
  retry: 3
  skip_existing: true
  log_file: "./batch-download.log"
```

### 定时同步配置

```yaml
# sync-config.yaml
sync:
  schedule: "0 6 * * *"        # cron 表达式
  subscriptions_file: "subscriptions.json"
  downloaded_db: ".downloaded.json"
  cleanup_days: 30             # 清理 30 天前的记录
  notify_webhook: ""           # 完成后通知
```

### 多平台支持

```python
class MultiPlatformDownloader:
    """多平台下载器"""

    def __init__(self):
        self.platforms = {
            "xiaoyuzhoufm": self._download_xiaoyuzhoufm,
            "rss": self._download_rss,
            "apple": self._download_apple,
        }

    def download(self, url, output_dir, quality=2):
        platform = self._detect_platform(url)
        downloader = self.platforms.get(platform)
        if downloader:
            return downloader(url, output_dir, quality)
        raise ValueError(f"不支持的平台: {platform}")

    def _detect_platform(self, url):
        if "xiaoyuzhoufm.com" in url:
            return "xiaoyuzhoufm"
        elif "feed" in url or "rss" in url:
            return "rss"
        elif "podcasts.apple.com" in url:
            return "apple"
        return "unknown"
```

## 最佳实践

### 1. 批量下载优化

- **并发控制**:建议 3-5 并发,避免被封禁
- **间隔下载**:每集间隔 2-5 秒,降低频率
- **失败重试**:网络错误自动重试 3 次
- **断点续传**:记录已下载 URL,中断后续传

### 2. 订阅同步策略

- **频率**:每天 1 次足够,避免过度请求
- **时间**:选择凌晨低峰时段
- **去重**:URL 哈希去重,避免重复下载
- **通知**:完成后 webhook 通知

### 3. 存储管理

```bash
# 自动清理脚本
#!/bin/bash
# cleanup.sh - 清理旧文件

PODCAST_DIR="/data/podcasts"
DAYS=30

# 清理 30 天前的 MP3
find "$PODCAST_DIR" -name "*.mp3" -mtime +$DAYS -delete

# 清理空目录
find "$PODCAST_DIR" -type d -empty -delete

# 统计当前存储
du -sh "$PODCAST_DIR"
```

### 4. 元数据规范

- **标题**:单集标题
- **艺术家**:节目名称
- **专辑**:节目名称
- **流派**:Podcast
- **封面**:嵌入节目封面图
- **年份**:发布年份

## 常见问题

### 已知限制

- 降低并发数到 1-2
- 增加下载间隔到 5-10 秒
- 添加随机延迟
- 使用代理轮换

### Q2: 订阅同步如何判断新集?

通过 URL 哈希去重。每集 URL 唯一,已下载的 URL 哈希记录在 `.downloaded.json` 中,同步时跳过已存在的。

### Q3: 定时任务不执行?

检查:
- crontab 是否正确配置(`crontab -l`)
- 路径是否为绝对路径
- 日志文件是否有权限写入
- cron 服务是否运行(`systemctl status cron`)

### Q4: 多平台支持哪些?

专业版支持:
- 小宇宙(xiaoyuzhoufm.com)
- RSS 订阅源
- Apple Podcasts 链接
- 通用 MP3 直链

### Q5: 专业版与免费版的迁移?

零迁移成本。专业版是免费版的超集,命令行完全兼容。升级后原有单集下载脚本继续可用,新特性按需启用。

### Q6: 下载的音频可以分发吗?

下载的音频仅供个人或团队内部使用。公开分发需获得版权方授权。请遵守相关法律法规与平台条款。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Shell**: Bash(Windows 建议使用 WSL 或 Git Bash)
- **Python**: 3.9 及以上(订阅与同步功能)
- **网络**: 需访问播客平台

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| curl | 命令行工具 | 必需 | 系统自带或下载 |
| jq | JSON 处理工具 | 必需 | `brew install jq` / `apt install jq` |
| ffmpeg | 音频转换工具 | 必需 | `brew install ffmpeg` / `apt install ffmpeg` |
| requests | Python 库 | 必需(订阅) | `pip install requests` |
| Python 3.9+ | 运行时 | 必需(脚本) | `python.org` 下载 |
| cron | 定时任务 | 推荐(定时同步) | 系统自带 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 核心下载功能**无需任何 API Key**
- 部分平台可能需要登录 Cookie(配置在环境变量)
- API 服务化建议配置鉴权 Token
- 企业部署建议通过密钥管理服务统一托管

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务。专业版支持批量下载、订阅同步与多平台扩展,适合企业级播客内容归档与自动化管理。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |
