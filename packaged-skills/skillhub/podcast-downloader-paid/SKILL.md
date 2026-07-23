---
slug: "podcast-downloader-paid"
name: "podcast-downloader-paid"
version: "1.0.0"
displayName: "播客下载工具专业版"
summary: "企业级播客下载工具,支持批量下载、播放列表订阅、定时同步与多平台扩展,适配生产环境。"
license: "Proprietary"
edition: "pro"
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
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# 播客下载工具专业版

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

**输入**: 用户提供免费版 vs 专业版对比所需的指令和必要参数。
**输出**: 返回免费版 vs 专业版对比的执行结果,包含操作状态和输出数据。
### 单集下载

执行单集下载,自动处理参数解析、任务调度和结果格式化,返回结构化输出。

**输入**: 用户提供单集下载相关的配置参数、输入数据和处理选项。

**输出**: 返回单集下载的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`单集下载`相关配置参数进行设置
### MP3 转换

执行MP3 转换,自动处理参数解析、任务调度和结果格式化,返回结构化输出。

**输入**: 用户提供MP3 转换相关的配置参数、输入数据和处理选项。

**输出**: 返回MP3 转换的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`MP3 转换`相关配置参数进行设置
#
## 适用场景
- 不适用: 需要人工判断的复杂决策场景

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

    PODCAST_DIR="$OUTPUT_DIR" （请参考skill目录中的脚本文件） "$url" &
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
                f"（请参考skill目录中的脚本文件） {ep['url']}"
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

## 使用流程

### 依赖说明

### 运行环境
1. **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
2. **操作系统**: Windows / macOS / Linux
3. **Shell**: Bash(Windows 建议使用 WSL 或 Git Bash)
4. **Python**: 3.9 及以上(订阅与同步功能)
5. **网络**: 需访问播客平台

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
6. 核心下载功能**无需任何 API Key**
7. 部分平台可能需要登录 Cookie(配置在环境变量)
8. API 服务化建议配置鉴权 Token
9. 企业部署建议通过密钥管理服务统一托管

### 可用性分类
10. **分类**: MD+EXEC()
11. **说明**: 基于Markdown的AI Skill,。专业版支持批量下载、订阅同步与多平台扩展,适合企业级播客内容归档与自动化管理。

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "downloader 相关配置参数",
    result: "downloader 相关配置参数"
  },
  "error": null
}
```

## 异常处理

- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM理解用户意图并调用工具 |

## 案例展示

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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
- 需要LLM支持
- 需要LLM支持


## 常见问题

**Q: 如何处理异常输入?**
A: 系统会自动检测并返回错误提示, 同时提供修复建议。

**Q: 支持哪些输入格式?**
A: 支持标准文本、JSON、CSV等常见格式。
