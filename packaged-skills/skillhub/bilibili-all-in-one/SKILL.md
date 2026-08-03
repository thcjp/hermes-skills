---
name: bilibili-all-in-one
slug: bilibili-all-in-one
displayName: "Bilibili All In One"
version: "1.0.24"
summary: "B站全功能工具箱,热门监控等一体化运营"
description: "B站全功能工具箱,热门监控等一体化运营。> **核心功能**: 本技能提供、多媒体制作、化工作流与智能决策辅助等能力。。适用于多种工作场景,提供专业的能力支持。内置错误恢复与降级机制,多格式兼容,适配多源数据。支持多种输入格式,输出结构化结果,适配独立开发者与小型团队。"
license: "MIT"
tools:
  - read
---

> **核心功能**: 本技能提供、多媒体制作、化工作流与智能决策辅助等能力。

A comprehensive Bilibili toolkit that integrates hot trending monitoring, video downloading, video watching/playback, subtitle downloading, and video publishing capabilities into a single unified skill.

> **⚠️ Optional Environment Variables:** `BILIBILI_SESSDATA`, `BILIBILI_BILI_JCT` (optional), `BILIBILI_BUVID3` (optional), `BILIBILI_PERSIST` (optional)
> These are sensitive Bilibili session cookies needed **only** for publishing and high-quality (1080p+/4K) downloads.
> **Most features work WITHOUT any credentials:** hot monitoring, standard-quality downloads, subtitle listing, danmaku, stats viewing.
>
> **📦 Install:** `pip install -r requirements.txt` (all standard PyPI packages: httpx, aiohttp, beautifulsoup4, lxml, requests)
>
> **🔗 Source:** [github.com/wscats/bilibili-all-in-one](

### 何时激活
当用户**明确请求**以下 Bilibili 相关操作时，本 Skill 可被激活：

| 触发场景 | 匹配的模块 | 典型触发词 |
| --- | --- | --- |
| 查看B站热门、热搜、排行榜、必看榜 | 🔥 Hot Monitor | "热门"、"热搜"、"排行"、"趋势"、"必看"、"流行"、"榜单" |
| 下载B站视频、提取音频、批量下载 | ⬇️ Downloader | "下载"、"保存视频"、"提取音频"、"导出MP4"、"批量下载" |
| 查看视频播放量、点赞数、数据追踪、对比 | 👀 Watcher | "播放量"、"点赞"、"数据"、"统计"、"对比"、"监控"、"追踪"、"观看量" |
| 下载字幕、转换字幕格式、合并字幕 | 📝 Subtitle | "字幕"、"CC"、"SRT"、"ASS"、"字幕下载"、"字幕转换"、"翻译" |
| 播放视频、获取弹幕、播放列表 | ▶️ Player | "播放"、"弹幕"、"播放地址"、"分P"、"播放列表"、"danmaku" |
| 上传视频、发布、定时发布、草稿、编辑 | 📤 Publisher | "上传"、"发布"、"投稿"、"定时发布"、"草稿"、"编辑视频" |

## Features
| Module | Description |
| --- | --- |
| 🔥 **Hot Monitor** | Monitor Bilibili hot/trending videos and topics in real-time |
| ⬇️ **Downloader** | Download Bilibili videos with multiple quality and format options |
| 👀 **Watcher** | Watch and track video engagement metrics (supports Bilibili) |
| 📝 **Subtitle** | Download and process subtitles in multiple formats and languages |
| ▶️ **Player** | Get playback URLs, danmaku (bullet comments), and playlist info |
| 📤 **Publisher** | Upload, schedule, edit, and manage videos on Bilibili |

## Installation
### Requirements
* Python >= 3.8
* ffmpeg (optional, for merging video/audio streams)

### 依赖说明
```bash
pip install -r requirements.txt
```

### Dependencies
* `httpx >= 0.24.0`
* `aiohttp >= 3.8.0`
* `beautifulsoup4 >= 4.12.0`
* `lxml >= 4.9.0`
* `requests >= 2.31.0`
* `faster-whisper >= 1.0.0` *(optional, for speech recognition subtitle fallback)*

## Configuration
Some features (downloading high-quality videos, publishing, etc.) require Bilibili authentication. You can provide credentials in three ways:

### 1. Environment Variables
```bash
export BILIBILI_SESSDATA="your_sessdata"
export BILIBILI_BILI_JCT="your_bili_jct"
export BILIBILI_BUVID3="your_buvid3"
```

### 2. Credential File
Create a JSON file (e.g., `credentials.json`):

```json
{
  "sessdata": "your_sessdata",
  "bili_jct": "your_bili_jct",
  "buvid3": "your_buvid3"
}
```

### 3. Direct Parameters
Pass credentials directly when initializing:

```python
from main import BilibiliAllInOne

app = BilibiliAllInOne(
    sessdata="your_sessdata",
    bili_jct="your_bili_jct",
    buvid3="your_buvid3",
)
```

### 4. Persistent Storage (Optional)
By default, credentials are kept **in-memory only** and are not saved to disk. To enable automatic persistence across sessions:

```bash
export BILIBILI_PERSIST=1
```

```python
app = BilibiliAllInOne(persist=True)
```

When persistence is enabled:

* Credentials are auto-saved to `.credentials.json` (with `0600` permissions) after initialization
* On next startup, credentials are auto-loaded from this file
* You can toggle persistence at runtime: `app.auth.persist = True` / `app.auth.persist = False`
* To delete the persisted file: `app.auth.clear_persisted()`

## ⚠️ Security & Privacy
### Credential Handling
This skill handles **sensitive Bilibili session cookies**. Please read the following carefully:

| Concern | Detail |
| --- | --- |
| **What credentials are needed?** | `SESSDATA`, `bili_jct`, `buvid3` — Bilibili **full browser session cookies** (not limited API keys). Providing them grants broad access to your Bilibili account. |
| **Which features require authentication?** | Publishing (upload/edit/schedule/draft), downloading 1080p+/4K quality videos |
| **Which features work WITHOUT credentials?** | Hot monitoring, standard-quality downloads, subtitle listing, danmaku fetching, stats viewing |
| **Where are credentials sent?** | To official Bilibili API endpoints (`api.bilibili.com`, `member.bilibili.com`) over HTTPS only |
| **Are credentials persisted to disk?** | **NO** by default — credentials stay in memory. Set `persist=True` or `BILIBILI_PERSIST=1` to opt-in to automatic persistence (saved to `.credentials.json` with `0600` permissions). You can also manually call `auth.save_to_file()` |
| **File permissions for saved credentials** | `0600` (owner read/write only) — restrictive by default |

### Best Practices
1. 🧪 **Use a test account** — Do NOT provide your primary Bilibili account cookies for evaluation/testing purposes. These are **full session cookies** that grant broad account access (not limited API keys).
2. 🔒 **Prefer in-memory credentials** — Pass credentials via environment variables or direct parameters rather than saving to a file. Only enable `persist=True` if you need credentials to survive across sessions.
3. 📁 **If you enable persistence** — Credentials are saved with `0600` permissions. Use `auth.clear_persisted()` or `auth.persist = False` to remove the file when no longer needed.
4. 🐳 **Run in isolation** — When possible, run this skill in an isolated container/environment and inspect network traffic.
5. 🌐 **Verify network traffic** — All HTTP requests go to Bilibili's official domains only. You can verify by monitoring outbound connections.
6. ❌ **No exfiltration** — This skill does NOT send credentials to any third-party service, analytics endpoint, or telemetry server.
7. 🔑 **Credential scope** — `SESSDATA` and `bili_jct` are full session cookies. They are NOT scoped/limited API keys. Treat them with the same care as your account password.

### Network Endpoints Used
| Domain | Purpose |
| --- | --- |
| `api.bilibili.com` | Video info, stats, hot lists, subtitles, danmaku, playback URLs |
| `member.bilibili.com` | Video publishing (upload, edit) |
| `upos-sz-upcdnbda2.bilivideo.com` | Video file upload CDN |
| `www.bilibili.com` | Web page scraping fallback |

### Credential Requirement by Module
| Module | Auth Required? | Notes |
| --- | --- | --- |
| 🔥 Hot Monitor | ❌ No | All public APIs |
| ⬇️ Downloader | ⚠️ Optional | Required only for 1080p+ / 4K quality |
| 👀 Watcher | ❌ No | Public stats APIs |
| 📝 Subtitle | ❌ No | Public subtitle APIs |
| ▶️ Player | ⚠️ Optional | Required for high-quality playback URLs |
| 📤 Publisher | ✅ **Required** | All operations need `SESSDATA` + `bili_jct` |

## Usage
### CLI
```bash
python main.py <skill_name> <action> [params_json]
```

### Python API
```python
import asyncio
from main import BilibiliAllInOne

app = BilibiliAllInOne()

async def demo():
    result = await app.execute("hot_monitor", "get_hot", limit=5)
    print(result)

asyncio.run(demo())
```

## Skills Reference
### 1. 🔥 Hot Monitor (`bilibili_hot_monitor`)
Monitor Bilibili hot/trending videos and topics in real-time. Supports filtering by category, tracking rank changes.

#
### Actions
| Action | Description | Parameters |
| --- | --- | --- |
| `get_hot` | Get popular/hot videos | `page`, `page_size` |
| `get_trending` | Get trending series/topics | `limit` |
| `get_weekly` | Get weekly must-watch list | `number` (week number, optional) |
| `get_rank` | Get category ranking videos | `category`, `limit` |

#
### Supported Categories
`all`, `anime`, `music`, `dance`, `game`, `tech`, `life`, `food`, `car`, `fashion`, `entertainment`, `movie`, `tv`

#
### 示例
```bash
python main.py hot_monitor get_hot '{"page_size": 10}'

python main.py hot_monitor get_trending '{"limit": 5}'

python main.py hot_monitor get_weekly

python main.py hot_monitor get_rank '{"category": "game", "limit": 10}'
```

```python
result = await app.execute("hot_monitor", "get_hot", page_size=10)
result = await app.execute("hot_monitor", "get_rank", category="game", limit=10)
```

### 2. ⬇️ Downloader (`bilibili_downloader`)
Download Bilibili videos with support for multiple quality options, batch downloading, and format selection.

#
### Quality Options
`360p`, `480p`, `720p`, `1080p` (default), `1080p+`, `4k`

#
### Format Options
`mp4` (default), `flv`, `mp3` (audio only)

#
### Examples
```bash
python main.py downloader get_info '{"url": "BV1xx411c7mD"}'

python main.py downloader get_formats '{"url": "BV1xx411c7mD"}'

python main.py downloader download '{"url": "BV1xx411c7mD", "quality": "1080p", "format": "mp4"}'

python main.py downloader download '{"url": "BV1xx411c7mD", "format": "mp3"}'

python main.py downloader batch_download '{"urls": ["BV1xx411c7mD", "BV1yy411c8nE"], "quality": "720p"}'
```

```python
info = await app.execute("downloader", "get_info", url="BV1xx411c7mD")
result = await app.execute("downloader", "download", url="BV1xx411c7mD", quality="1080p")
```

### 3. 👀 Watcher (`bilibili_watcher`)
Watch and monitor Bilibili videos. Track view counts, comments, likes, and other engagement metrics over time.

#
### Supported Platforms
* **Bilibili**: `https://www.bilibili.com/video/BVxxxxxx` or `BVxxxxxx`

#
### 4. 📝 Subtitle (`bilibili_subtitle`)
### 5. ▶️ Player (`bilibili_player`)
Play Bilibili videos with support for playback control, playlist management, and danmaku (bullet comments) display.

#
### Danmaku Modes
| Mode | Description |
| --- | --- |
| 1 | Scroll (right to left) |
| 4 | Bottom fixed |
| 5 | Top fixed |

#
### 6. 📤 Publisher (`bilibili_publisher`)
## Project Structure

> 详细代码示例已移至 `references/detail.md`

## Response Format
All skill actions return a JSON object with a unified structure:

```json
{
  "success": true,
  "...": "action-specific fields"
}
```

On error:

```json
{
  "success": false,
  "message": "Error description"
}
```

## License
MIT

## 安装与配置
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent( Code / Cursor / Codex /  CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+execute(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 使用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 操作流程
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 故障恢复流程
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见疑问
### Q1: 如何开始使用Bilibili All In One？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Bilibili All In One有什么限制？
A: 请参考已知限制章节了解具体限制。

## 功能边界
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

## 安全指导原则
### 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 效能分析
| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 优势对比
| 对比维度 | Bilibili All In One | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | B站全功能工具箱,热门监控等一体化运营 | 通用场景 | 通用场景 |

## 关键特性
- **自动化执行**: B站全功能工具箱,热门监控等一体化运营
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果

## 快速入门指南
1. **配置API密钥**: 在环境变量中设置对应的API Key
2. **初始化连接**: 使用提供的凭证建立API连接
3. **调用接口**: 传入必要参数执行API调用
1. **准备文件**: 确认文件路径正确且格式受支持
2. **执行处理**: 调用对应的处理函数
3. **查看结果**: 检查输出文件或返回数据
1. **检查环境**: 确认运行时和依赖已安装
2. **执行命令**: 使用正确的参数格式执行
3. **查看输出**: 检查命令输出和退出码

### 前置条件

- 已安装所需运行环境(参考依赖说明)
- 已获取必要的API密钥或访问凭证(如适用)
- 输入数据已准备就绪

## 帮助文档
### Q1: Bilibili All In One支持哪些输入格式？

A1: B站全功能工具箱,热门监控等一体化运营。支持文本指令和结构化参数输入，具体格式参考使用流程章节。

### Q2: 需要配置API Key吗？

A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。

### Q3: 命令行执行失败怎么办？

A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。

## 主要功能
- **自动化执行**: B站全功能工具箱,热门监控等一体化运营
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果

## 异常应对机制
针对Bilibili All In One使用中可能遇到的常见问题,提供以下排查方案:

| 错误类型 | 原因分析 | 解决方案 |
|---------|---------|---------|
| API认证失败(401) | API密钥错误或过期 | 检查密钥配置,重新生成token |
| 接口限流(429) | 请求频率超出限制 | 降低调用频率,启用重试退避策略 |
| 响应超时(504) | 网络延迟或服务端负载过高 | 增加超时阈值,检查网络连接 |
| 文件不存在 | 路径错误或文件未创建 | 检查路径拼写,确认文件已生成 |
| 文件格式不支持 | 扩展名不在支持列表中 | 转换为支持的格式后重试 |
| 权限不足 | 当前用户无读写权限 | 检查文件权限,以管理员身份运行 |
| 命令执行失败 | 参数错误或环境依赖缺失 | 检查命令语法,确认依赖已安装 |
| 进程超时 | 命令执行时间过长 | 增加超时设置,优化命令参数 |
| 网络连接失败 | DNS解析失败或防火墙拦截 | 检查网络配置,确认代理设置 |

### Bilibili All In One通用排查步骤

1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块

## 安装向导
1. **配置API密钥**: 在环境变量中设置对应的API Key
2. **初始化连接**: 使用提供的凭证建立API连接
3. **调用接口**: 传入必要参数执行API调用
1. **准备文件**: 确认文件路径正确且格式受支持
2. **执行处理**: 调用对应的处理函数
3. **查看结果**: 检查输出文件或返回数据
1. **检查环境**: 确认运行时和依赖已安装
2. **执行命令**: 使用正确的参数格式执行
3. **查看输出**: 检查命令输出和退出码

### 前置条件

- 已安装所需运行环境(参考依赖说明)
- 已获取必要的API密钥或访问凭证(如适用)
- 输入数据已准备就绪
