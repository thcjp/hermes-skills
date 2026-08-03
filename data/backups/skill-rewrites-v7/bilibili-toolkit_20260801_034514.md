---
slug: "bilibili-toolkit"
name: "bilibili-toolkit"
version: 1.0.1
displayName: "B站工具箱专业版"
summary: "企业级B站运营工具，支持高清下载、视频发布、批量操作、数据追踪与凭证安全管理。B站工具箱专业版 —— 面向专业UP主与企业运营的全功能B站工具。核心能力: - 高清视频下载：支持1080p"
summary_zh: "企业级B站运营工具，支持高清下载、视频发布、批量操作、数据追踪与凭证安全管理。B站工具箱专业版 —— 面向专业UP主与企业运营的全功能B站工具。核心能力: - 高清视频下载：支持1080p"
license: "MIT"
edition: "pro"
description: |-
  B站工具箱专业版 —— 面向专业UP主与企业运营的全功能B站工具。核心能力:
  - 高清视频下载：支持1080p+、4K超清画质下载
  - 视频发布管理：上传、定时发布、草稿管理、视频编辑
  - 批量下载与处理：批量下载多个视频，队列管理
  - 数据追踪监控：定时追踪视频播放量、点赞等指标变化
  - 视频对比分析：多视频数据对比...
tags:
  - B站
  - 视频发布
  - 企业工具
  - 数据追踪
  - 批量处理
  - 视频
  - 媒体
  - python
  - app
  - await
  - execute
  - publisher
tools:
  - read
  - exec
  - write
homepage: ""
category: "Creative"
---

# B站工具箱专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| B站工具箱专业版据追踪与凭证安全管理 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

## 核心能力

### 1. 视频发布管理

```python
import asyncio
from bilibili_toolkit_pro import BilibiliAllInOne

# 初始化B站工具箱
app = BilibiliAllInOne(
    sessdata="your_sessdata",
    bili_jct="your_bili_jct",
    buvid3="your_buvid3"
)

# 异步发布视频
async def publish_video():
    result = await app.execute("publisher", "upload",
        file_path="./video.mp4",
        title="我的专业视频",
        description="使用B站工具箱专业版上传",
        tags=["python", "bilibili", "教程"],
        category="122",  # 开源软件分类
        no_reprint=1,    # 原创内容
        open_elec=1      # 开启充电
    )
    print(f"发布结果: {result}")

# 运行异步任务
asyncio.run(publish_video())
```

```bash
# 命令行发布
python bilibili_toolkit_pro.py publisher upload '{
    "file_path": "./video.mp4",
    "title": "我的专业视频",
    "description": "专业版上传测试",
    "tags": ["教程", "python"],
    "category": "122"
}'
# ...
# 保存为草稿
python bilibili_toolkit_pro.py publisher draft '{
    "file_path": "./video.mp4",
    "title": "草稿视频"
}'
# ...
# 定时发布
python bilibili_toolkit_pro.py publisher schedule '{
    "file_path": "./video.mp4",
    "title": "定时发布视频",
    "schedule_time": "2026-12-31T20:00:00+08:00"
}'
# ...
# 编辑已发布视频
python bilibili_toolkit_pro.py publisher edit '{
    "bvid": "BV1xx411c7mD",
    "title": "新标题",
    "tags": ["更新", "标签"]
}'
```

### 2. 批量下载与队列管理

```python
async def batch_download():
    urls = [
        "BV1xx411c7mD",
        "BV1yy411c8nE",
        "BV1zz411c9oF"
    ]

    result = await app.execute("downloader", "batch_download",
        urls=urls,
        quality="1080p+",  # 专业版支持高清
        format="mp4",
        output_dir="./downloads"
    )
    print(f"批量下载完成: {result}")

# 运行异步任务
asyncio.run(batch_download())
```

### 3. 数据追踪与对比分析

```python
async def track_and_compare():
    track_result = await app.execute("watcher", "track",
        url="BV1xx411c7mD",
        interval=30,    # 30分钟间隔
        duration=12     # 持续12小时
    )
    print(f"追踪完成: {track_result}")

    compare_result = await app.execute("watcher", "compare",
        urls=["BV1xx411c7mD", "BV1yy411c8nE", "BV1zz411c9oF"]
    )
    print(f"对比结果: {compare_result}")

# 运行异步任务
asyncio.run(track_and_compare())
```

### 4. 凭证安全管理

```python
# 环境变量方式
import os
os.environ["BILIBILI_SESSDATA"] = "your_sessdata"
os.environ["BILIBILI_BILI_JCT"] = "your_bili_jct"
os.environ["BILIBILI_BUVID3"] = "your_buvid3"

# 凭证文件方式
app = BilibiliAllInOne(
    sessdata="your_sessdata",
    bili_jct="your_bili_jct",
    buvid3="your_buvid3",
    persist=True  # 启用持久化存储（0600权限）
)

# 运行时管理方式
app.auth.persist = True   # 启用持久化
app.auth.clear_persisted()  # 清除持久化文件
```

## 快速开始

1. 确认运行环境满足依赖说明中的要求。
2. 在AI Agent对话中调用本技能，提供必要的输入参数。
3. 检查输出结果，根据需要进行后续处理。

## 适用场景

### 场景一：UP主内容发布管理

专业UP主批量管理视频发布，包括上传、定时发布与草稿管理。

```python
async def up_master_workflow():
    # 1. 上传并保存为草稿
    draft_result = await app.execute("publisher", "draft",
        file_path="./videos/episode01.mp4",
        title="系列教程优秀期",
        description="Python基础教程",
        tags=["Python", "教程", "编程"],
        category="122"
    )

    # 2. 定时发布第二期
    schedule_result = await app.execute("publisher", "schedule",
        file_path="./videos/episode02.mp4",
        title="系列教程第二期",
        schedule_time="2026-01-20T19:00:00+08:00",
        tags=["Python", "教程", "编程"],
        category="122"
    )

    # 3. 编辑已发布视频信息
    edit_result = await app.execute("publisher", "edit",
        bvid="BV1xx411c7mD",
        title="更新后的标题",
        tags=["更新标签", "Python"]
    )

    print(f"草稿: {draft_result}")
    print(f"定时: {schedule_result}")
    print(f"编辑: {edit_result}")
```

### 场景二：竞品数据追踪分析

运营团队追踪竞品视频数据变化，进行对比分析。

```python
async def competitor_analysis():
    competitor_videos = [
        "BV1xx411c7mD",  # 竞品A
        "BV1yy411c8nE",  # 竞品B
        "BV1zz411c9oF"   # 竞品C
    ]

    # 获取当前数据
    for bv in competitor_videos:
        stats = await app.execute("watcher", "get_stats", url=bv)
        print(f"视频{bv}: 播放{stats['data']['view']} 点赞{stats['data']['like']}")

    # 多视频对比
    comparison = await app.execute("watcher", "compare", urls=competitor_videos)
    print(f"对比分析: {comparison}")

    # 长期追踪（每小时采集，持续24小时）
    track = await app.execute("watcher", "track",
        url="BV1xx411c7mD",
        interval=60,
        duration=24
    )
```

### 场景三：高清视频批量归档

企业批量下载高清视频用于内容归档。

```python
async def batch_archive():
    video_list = [
        "BV1xx411c7mD",
        "BV1yy411c8nE",
        "BV1zz411c9oF",
        "BV1aa411c0pG"
    ]

    execute("downloader", "batch_download",
        urls=video_list,
        quality="4k",      # 4K超清
        format="mp4",
    )

    for bv in video_list:
        await app.execute("subtitle", "download",
            url=bv,
            language="zh-CN",
            format="srt",
        )

    print(f"归档完成: {result}")
```

## 使用流程

### 依赖说明

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8及以上
- **可选工具**: ffmpeg（用于合并音视频流）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3 | 运行时 | 必需 | python.org 下载安装 |
| httpx | Python库 | 必需 | `pip install httpx` |
| aiohttp | Python库 | 必需 | `pip install aiohttp` |
| beautifulsoup4 | Python库 | 必需 | `pip install beautifulsoup4` |
| lxml | Python库 | 必需 | `pip install lxml` |
| requests | Python库 | 必需 | `pip install requests` |
| faster-whisper | Python库 | 可选 | `pip install faster-whisper` |
| ffmpeg | 系统工具 | 可选 | 系统包管理器安装 |

### API Key 配置

- `BILIBILI_SESSDATA`：B站会话凭证（发布与高清下载必需）
- `BILIBILI_BILI_JCT`：B站CSRF Token（写操作必需）
- `BILIBILI_BUVID3`：B站设备标识（辅助验证）
- `BILIBILI_PERSIST`：是否启用凭证持久化（设为1启用）

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，核心功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行专业B站运营任务。支持视频发布、高清下载、批量操作、数据追踪等全功能能力，通过Python脚本调用B站API实现。与免费版完全兼容，可直接复用免费版的无登录功能。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | bilibili-toolkit-pro处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接，重试请求 |

## 依赖说明(补充)

| 依赖项 | 类型 | 必需 | 说明 |
|:------|------:|:------|:------|
| LLM | 模型 | 是 | 需要LLM进行智能审查，推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

## 案例展示

### 凭证获取方式

登录bilibili.com，打开浏览器开发者工具（F12）→ Application → Cookies，复制以下值：

| 凭证 | 说明 | 用途 |
|---:|:---|---:|
| `SESSDATA` | 会话凭证 | 登录验证 |
| `bili_jct` | CSRF Token | 写操作（发布/编辑） |
| `buvid3` | 设备标识 | 辅助验证 |

### 发布参数说明

| 参数 | 类型 | 默认值 | 说明 |
|:------:|--------|:-------|:------:|
| `file_path` | string | 必填 | 视频文件路径 |
| `title` | string | 必填 | 标题（最多80字） |
| `description` | string | 空 | 简介（最多2000字） |
| `tags` | string[] | ["bilibili"] | 标签（最多12个，每个最多20字） |
| `category` | string | "171" | 分区TID |
| `cover_path` | string | null | 封面图片路径 |
| `no_reprint` | int | 1 | 1=原创，0=转载 |
| `open_elec` | int | 0 | 1=开启充电，0=关闭 |

### 凭证安全说明

| 关注点 | 说明 |
|----|:--:|
| 凭证类型 | 完整浏览器会话Cookie，非受限API Key |
| 存储方式 | 默认内存存储，不落盘 |
| 持久化 | 可选启用，0600权限保护 |
| 网络传输 | 仅发送至B站官方域名，HTTPS加密 |
| 第三方共享 | 不发送至任何第三方服务 |

## 常见问题

### Q1：发布视频失败提示认证错误怎么办？

检查SESSDATA和bili_jct是否正确且未过期。发布操作必须同时提供这两个凭证。

### Q2：4K下载失败怎么办？

4K下载需要登录凭证。确认已正确配置SESSDATA，且账号有4K观看权限。

### Q3：凭证持久化安全吗？

持久化文件使用0600权限（仅所有者可读写）。建议仅在需要跨会话使用时启用，用完及时清除。

### Q4：定时发布的时间格式是什么？

使用ISO 8601格式，如 `2026-12-31T20:00:00+08:00`（北京时间20:00）。

### Q5：与免费版的功能是否兼容？

完全兼容。专业版包含免费版所有功能，免费版的无登录功能在专业版中同样可用。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接，重试请求 |

## 已知限制

- 需要API Key，无Key环境无法使用

## 边界条件与限制 (Boundary Conditions)

### 输入限制

- **视频文件大小**：由于网络和服务器限制，单个视频文件大小上限可能存在限制，具体大小需参考B站API文档。
- **视频时长**：上传的视频时长可能存在限制，通常为30分钟以内，具体时长限制需参考B站API文档。
- **标题和描述长度**：标题长度限制在80个字符以内，描述长度限制在2000个字符以内。
- **标签数量**：最多可添加12个标签，每个标签最多20个字符。

### 性能边界

- **批量下载速度**：批量下载速度受限于网络带宽和服务器处理能力，可能存在一定延迟。
- **数据追踪频率**：数据追踪的频率受限于API调用频率限制，通常为每30分钟采集一次数据。

###