---
slug: qq-zone-photo-tool-pro
name: qq-zone-photo-tool-pro
version: "1.0.0"
displayName: QQ空间相册专业版
summary: 专业相册管理平台，支持批量下载、相册创建上传与多平台迁移。
license: MIT
edition: pro
description: |-
  面向专业用户的QQ空间相册管理平台。支持批量下载整个相册、创建
  新相册、批量上传照片、相册管理与多平台迁移（至Google Photos/
  iCloud等）。内置照片去重与元数据管理。

  核心能力:
  - 批量下载整个相册（并行加速）
  - 相册创建与编辑管理
  - 批量照片上传
  - 多平台迁移（Google Photos/iCloud/本地）
  - 照片去重与智能整理
  - EXIF元数据管理
  - 照片时间线整理

  适用场景:
  - 大规模照片备份迁移
  - 相册整理与重组
  - 多平台照片同步
  - 照片归档管理
  - 家庭照片整理

  差异化:
  - 兼容免费版浏览与单张下载，无缝升级
  - 新增批量下载与上传
  - 相册创建与管理
  - 多平台迁移
  - 照片去重与元数据管理

  触发关键词: QQ空间, 相册, 批量下载, 批量上传, 相册管理, 迁移, 去重, EXIF, qzone, migrate
tags:
- Operations
- QQ空间
- 相册管理
- 专业版
tools:
- read
- exec
---

# QQ空间相册专业版（PRO版）

## 概述

本平台为专业用户提供全功能的QQ空间相册管理能力。相比免费版，PRO版新增批量下载、相册创建、批量上传、多平台迁移和照片去重等高级功能，全面满足大规模照片管理与迁移的需求。

PRO版完全兼容免费版浏览与下载命令，升级后原有操作可直接使用。

## 核心能力

### PRO版功能增强对比

| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 下载方式 | 单张 | 批量并行 |
| 上传功能 | 不支持 | 批量上传 |
| 相册管理 | 仅浏览 | 创建/编辑/删除 |
| 平台迁移 | 不支持 | Google/iCloud/本地 |
| 照片去重 | 不支持 | 智能去重 |
| 元数据 | 不支持 | EXIF管理 |
| 时间线 | 不支持 | 智能整理 |
| 下载速度 | 单线程 | 多线程并行 |

## 使用场景

### 场景一：批量下载相册

用户输入："下载我所有相册的全部照片"

```bash
# 批量下载所有相册
python3 scripts/qzone_pro.py batch download \
  --albums all \
  --output ./photos_backup/ \
  --parallel 5 \
  --quality original

# 输出：
# === 批量下载进度 ===
# 旅行照片: 156/156 [完成]
# 家庭聚会: 89/89 [完成]
# 工作记录: 45/45 [进行中...]
# 总计: 290张 已下载: 245张
```

### 场景二：批量上传

用户输入："把这个文件夹的照片上传到QQ空间"

```bash
# 批量上传照片
python3 scripts/qzone_pro.py batch upload \
  --source-dir ./new_photos/ \
  --album "2026年新照片" \
  --create-if-not-exist \
  --parallel 3

# 自动创建相册并上传
```

### 场景三：多平台迁移

用户输入："把QQ空间照片迁移到Google Photos"

```bash
# 迁移到Google Photos
python3 scripts/qzone_pro.py migrate \
  --from qzone \
  --to google-photos \
  --albums all \
  --preserve-metadata \
  --output-log ./migration_log.json
```

## 快速开始

### PRO版初始化

```bash
# 安装PRO版依赖
pip install -r requirements_pro.txt

# 登录QQ空间
python3 scripts/qzone_pro.py login --qq 123456789
```

### 常用命令

```bash
# 批量下载
python3 scripts/qzone_pro.py batch download --albums all --output ./backup/ --parallel 5
python3 scripts/qzone_pro.py batch download --album "旅行照片" --output ./travel/

# 批量上传
python3 scripts/qzone_pro.py batch upload --source-dir ./photos/ --album "新相册"

# 相册管理
python3 scripts/qzone_pro.py albums create --name "2026旅行" --description "旅行照片"
python3 scripts/qzone_pro.py albums edit --name "旧相册" --new-name "重命名相册"
python3 scripts/qzone_pro.py albums delete --name "测试相册"

# 迁移
python3 scripts/qzone_pro.py migrate --from qzone --to google-photos --albums all
python3 scripts/qzone_pro.py migrate --from qzone --to local --albums all --output ./archive/

# 去重
python3 scripts/qzone_pro.py deduplicate --scan ./photos/
python3 scripts/qzone_pro.py deduplicate --remove-duplicates

# 元数据
python3 scripts/qzone_pro.py metadata extract --dir ./photos/
python3 scripts/qzone_pro.py metadata timeline --dir ./photos/
```

## 配置示例

### PRO平台配置

```yaml
pro_config:
  auth:
    method: "cookie"
    cookie_file: "./qzone_cookies.json"
    auto_refresh: true             # 自动刷新Cookie

  download:
    parallel: 5                    # 并行下载数
    quality: "original"
    naming: "date_original"        # 按拍摄日期+原名
    retry: 3                       # 失败重试
    chunk_size: "1MB"

  upload:
    parallel: 3
    max_filesize: "50MB"
    auto_resize: false             # 不自动压缩
    preserve_exif: true            # 保留EXIF

  migration:
    targets:
      google_photos:
        credentials: "./google_credentials.json"
      icloud:
        apple_id: "${APPLE_ID}"
        app_password: "${APP_PASSWORD}"
      local:
        output_dir: "./photo_archive"

  deduplication:
    algorithm: "phash"            # 感知哈希
    threshold: 0.95               # 相似度阈值
    action: "mark"                # mark | remove

  metadata:
    extract_exif: true
    extract_gps: true
    timeline: true
    timezone: "Asia/Shanghai"
```

## 最佳实践

### PRO版高级实践

| 实践领域 | 建议做法 |
| --- | --- |
| 批量下载 | 并行数设3-5，避免被限流 |
| 批量上传 | 单次上传不超过100张，分批进行 |
| 迁移 | 先小批量测试，确认后再全量迁移 |
| 去重 | 先mark标记，人工确认后再remove |
| 元数据 | 保留EXIF信息，便于时间线整理 |

### 免费版兼容性

```text
免费版命令 → PRO版命令（增强）：
qzone.py photo download (单张)  → qzone_pro.py batch download (批量)
qzone.py albums list (浏览)     → +创建/编辑/删除
不支持上传                      → batch upload (批量上传)
```

## 常见问题

### Q1：批量下载会被限制吗？

QQ空间对下载频率有一定限制。PRO版通过控制并行数和请求间隔避免触发限流。建议并行数不超过5，如被限流可降低并行数。

### Q2：迁移到Google Photos需要什么？

需要Google Photos API凭证。在Google Cloud Console创建项目，启用Photos Library API，下载OAuth凭证文件。PRO版会引导完成授权流程。

### Q3：照片去重准确吗？

PRO版使用感知哈希（pHash）算法检测相似照片，准确率较高。默认使用mark模式标记重复项，人工确认后再删除，避免误删。

### Q4：支持视频下载吗？

PRO版支持相册中的视频下载。视频文件较大，建议在WiFi环境下进行。上传视频可能受QQ空间格式和大小限制。

### Q5：迁移后照片质量会下降吗？

不会。PRO版默认下载原图原质量，不进行压缩。迁移过程中保留完整EXIF元数据，包括拍摄时间、GPS位置等信息。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| requests | Python库 | 必需 | `pip install requests` |
| Pillow | Python库 | 必需 | `pip install Pillow`（图片处理） |
| imagehash | Python库 | 可选 | `pip install imagehash`（去重） |
| google-api-python-client | Python库 | 可选 | `pip install google-api-python-client`（迁移） |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:-------|:---------|:---------|:-----|
| Google Photos | 凭证文件 | 可选 | 迁移到Google Photos |
| iCloud | `APPLE_ID`/`APP_PASSWORD` | 可选 | 迁移到iCloud |

- QQ空间通过Cookie认证，无需API Key
- 迁移目标平台的凭证按需配置

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 专业QQ空间相册管理平台，支持批量与迁移
- **PRO版特性**: 批量下载、批量上传、相册管理、多平台迁移、去重、元数据
- **兼容性**: 完全兼容免费版浏览与单张下载命令
- **合规声明**: 仅支持管理自己的照片，请尊重他人隐私与版权
