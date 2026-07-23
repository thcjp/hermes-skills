---
slug: "video-frames-paid"
name: "video-frames-paid"
version: "1.0.0"
displayName: "视频帧提取-专业版"
summary: "企业级视频帧提取与剪辑工具，支持批量处理、区间抓取、分辨率调整、水印添加等高级能力。"
license: "Proprietary"
edition: "pro"
description: |-
  视频帧提取专业版。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Creative
  - 视频处理
  - 帧提取
  - 专业版
  - 批量处理
  - 企业级
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# 视频帧提取-专业版

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

### 1. 批量视频处理

支持单次处理 100+ 视频，自动并行调度：

```text
输入视频列表 (CSV/JSON)
      ↓
任务调度器分配并行任务
      ↓
多 ffmpeg 进程并行抓帧
      ↓
结果聚合 + 失败重试
      ↓
生成处理报告
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `批量视频处理` 选项
- 处理流程: 接收输入 -> 执行批量视频处理 -> 返回结果
- 输入: 用户提供批量视频处理所需的参数和指令
- 输出: 返回批量视频处理的执行结果,包含操作状态和输出数据

### 2. 区间帧提取与剪辑
- 按时间区间提取多帧（如 10s-30s 每 2 秒一帧）
- 视频片段剪辑输出为 GIF 或 MP4
- 支持精确到帧的区间控制

**处理**: 按照skill规范执行区间帧提取与剪辑操作,遵循单一意图原则。
### 3. 智能关键帧检测
基于场景变化自动识别关键帧：

- 场景切换检测（`select=gt(scene\,0.3)`）
- 自动跳过黑屏与过渡帧
- 智能去重（相似度阈值可调）

**输入**: 用户提供智能关键帧检测所需的指令和必要参数。
**处理**: 按照skill规范执行智能关键帧检测操作,遵循单一意图原则。
**输出**: 返回智能关键帧检测的执行结果,包含操作状态和输出数据。

### 4. 水印与分辨率自定义
- 图片水印：支持 PNG 透明水印，可设置位置与透明度
- 文字水印：支持字体、大小、颜色、位置
- 分辨率：输出任意分辨率，保持纵横比或强制拉伸

**输入**: 用户提供水印与分辨率自定义所需的指令和必要参数。
**处理**: 按照skill规范执行水印与分辨率自定义操作,遵循单一意图原则。

### 5. 任务队列与断点续传
- 大批量任务自动入队
- 异常中断后可从断点继续
- 处理进度实时查询
- 失败任务自动重试（最多 3 次）

**输入**: 用户提供任务队列与断点续传所需的指令和必要参数。
**输出**: 返回任务队列与断点续传的执行结果,包含操作状态和输出数据。

#
## 适用场景

### 场景 1：电商商品视频批量封面采集

某电商平台运营团队需要为 200 个商品视频自动生成封面图。

**配置文件 `batch-config.json`：**

```json
{
  "videos": [
    {"file": "/videos/product-001.mp4", "time": "00:00:03"},
    {"file": "/videos/product-002.mp4", "time": "00:00:05"},
    {"file": "/videos/product-003.mp4", "time": "00:00:08"}
  ],
  "output_dir": "/tmp/covers/",
  "format": "jpg",
  "resolution": "1280x720",
  "watermark": {
    "image": "/assets/logo.png",
    "position": "bottom-right",
    "opacity": 0.8
  }
}
```

**执行命令：**

```bash
{baseDir}/（请参考skill目录中的脚本文件） --config /path/to/batch-config.json --parallel 8
```

**输出结构：**

```text
/tmp/covers/
├── product-001_00-00-03.jpg
├── product-002_00-00-05.jpg
├── product-003_00-00-08.jpg
└── report.json   # 处理报告（成功/失败统计）
```

### 场景 2：在线教育课件智能配图

教育机构需要从一节 45 分钟的课程视频中，自动提取关键知识点对应的画面。

**使用智能关键帧检测：**

```bash
{baseDir}/（请参考skill目录中的脚本文件） \
  --input /videos/lesson-01.mp4 \
  --output /tmp/keyframes/ \
  --scene-threshold 0.3 \
  --min-interval 5s \
  --max-frames 30
```

**效果说明：**

- 自动检测场景切换点
- 跳过黑屏与过渡动画
- 最小间隔 5 秒，避免相邻重复
- 最多输出 30 张关键帧
- 输出文件名包含时间戳，方便对照

### 场景 3：影视后期素材区间剪辑

剪辑师需要从原始素材中提取多个片段用于后期合成。

**区间提取配置 `clips.yaml`：**

```yaml
source: /videos/raw-footage.mp4
output_dir: /tmp/clips/
segments:
  - name: "opening"
    start: "00:00:15"
    end: "00:00:25"
    format: mp4
    resolution: "1920x1080"
  - name: "highlight"
    start: "00:05:30"
    end: "00:06:10"
    format: gif
    fps: 15
    resolution: "800x450"
  - name: "ending"
    start: "00:12:00"
    end: "00:12:20"
    format: mp4
    resolution: "1920x1080"
```

**执行命令：**

```bash
{baseDir}/（请参考skill目录中的脚本文件） --config /path/to/clips.yaml
```

## 使用流程

### 优秀步：环境检查

```bash
# 检查 ffmpeg 版本（需 4.0+）
ffmpeg -version

# 检查 Python 版本（需 3.8+）
python3 --version
```

### 示例

创建一个简单的批量配置文件：

```json
[
  {"file": "/videos/a.mp4", "time": "00:00:05"},
  {"file": "/videos/b.mp4", "time": "00:00:10"},
  {"file": "/videos/c.mp4", "time": "00:00:15"}
]
```

执行批量处理：

```bash
{baseDir}/（请参考skill目录中的脚本文件） \
  --config /tmp/videos.json \
  --output-dir /tmp/frames/ \
  --parallel 4 \
  --format jpg
```

### 第三步：智能关键帧检测

```bash
{baseDir}/（请参考skill目录中的脚本文件） \
  --input /videos/long-video.mp4 \
  --output /tmp/keyframes/ \
  --scene-threshold 0.4
```

### 第四步：添加水印

```bash
# 图片水印
{baseDir}/（请参考skill目录中的脚本文件） /videos/promo.mp4 \
  --time 00:00:10 \
  --out /tmp/watermarked.jpg \
  --watermark /assets/logo.png \
  --wm-position bottom-right \
  --wm-opacity 0.7

# 文字水印
{baseDir}/（请参考skill目录中的脚本文件） /videos/promo.mp4 \
  --time 00:00:10 \
  --out /tmp/watermarked.jpg \
  --text-watermark "© 2026 Company" \
  --wm-font-size 24 \
  --wm-color white
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | video-frames处理的内容输入 |,  |
| content | string | 否 | video-frames处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "frames 相关配置参数",
    result: "frames 相关配置参数",
    result: "frames 相关配置参数",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 规范的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（批量脚本依赖）
- **Shell**：Bash 或兼容 Shell
- **磁盘空间**：建议预留输出目录 5GB+ 可用空间

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:-------|:-----|:---------|:---------|:---------|
| ffmpeg | 命令行工具 | 必需 | 系统包管理器 | 4.0+ |
| ffprobe | 命令行工具 | 必需 | 随 ffmpeg 安装 | 4.0+ |
| Python | 运行时 | 必需 | python.org | 3.8+ |
| PyYAML | Python 库 | 可选 | `pip install pyyaml` | 5.4+ |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |

#### 完整安装命令

```bash
# 安装 ffmpeg + Python 依赖
sudo apt update && sudo apt install ffmpeg python3 python3-pip
pip3 install pyyaml

# 验证安装
ffmpeg -version
python3 --version
python3 -c "import yaml; print('PyYAML ready')"
```

### API Key 配置

- 本 Skill 纯本地运行，**无需任何 API Key**
- 所有视频处理均在本地完成，数据不离开本地环境
- 如需集成云存储（如 S3、OSS），请在配置文件中单独配置对应云服务凭证

### 可用性分类

- **分类**：MD+EXEC（Markdown 指令 + 命令行执行 + Python 脚本）
- **说明**：通过自然语言指令驱动 Agent 调用 `ffmpeg` 和 Python 脚本完成高级视频帧处理
- **离线可用**：是（完全本地运行）
- **隐私等级**：高（视频数据不离开本地）
- **企业部署**：支持私有化部署，无外部依赖

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

### 示例2: 进阶用法
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

**A：** 完全兼容。专业版包含免费版所有参数，已有的单帧抓取命令可直接运行。专业版扩展的参数（如 `--watermark`、`--resolution`）为可选配置。

### Q2：批量处理中部分视频失败怎么办？

**A：** 专业版自动记录失败任务，并提供两种恢复方式：

```bash
# 方式一：仅重试失败任务
{baseDir}/（请参考skill目录中的脚本文件） --retry-failed /tmp/queue.json

# 方式二：从断点续传
{baseDir}/（请参考skill目录中的脚本文件） --resume /tmp/queue.json
```

### Q3：智能关键帧检测的阈值如何选择？

**A：** 阈值范围为 0-1，数值越小检测越敏感：

- `0.2-0.3`：适合场景变化平缓的视频（讲座、会议）
- `0.3-0.4`：通用推荐值，适合大多数视频
- `0.4-0.5`：适合场景变化明显的视频（电影、动画）

### Q4：能否处理超长视频（如 2 小时以上）？

**A：** 专业版针对长视频优化：

- 支持流式处理，无需一次性加载
- 智能关键帧检测可显著减少输出数量
- 建议配合 `--max-frames` 参数限制输出

### Q5：水印位置可以自定义坐标吗？

**A：** 可以，使用 `custom` 位置并指定坐标：

```bash
{baseDir}/（请参考skill目录中的脚本文件） video.mp4 \
  --time 00:00:10 \
  --out /tmp/output.jpg \
  --watermark /assets/logo.png \
  --wm-position custom \
  --wm-x 100 --wm-y 200
```

### Q6：批量处理支持哪些输入格式？

**A：** 支持 CSV、JSON、YAML 三种配置格式，以及纯文本（每行一个视频路径）：

```bash
# 纯文本列表
{baseDir}/（请参考skill目录中的脚本文件） --list /tmp/video-list.txt --output-dir /tmp/frames/
```

### Q7：网络 URL 抓帧如何使用？

**A：** 专业版支持直接输入网络视频 URL：

```bash
{baseDir}/（请参考skill目录中的脚本文件） "https://example.com/video.mp4" \
  --time 00:00:10 \
  --out /tmp/frame-from-url.jpg
```

注意：网络抓帧需要稳定网络环境，大文件建议先下载到本地再处理。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
