---

slug: "video-upload-stream-tool"
name: "video-upload-stream-tool"
version: "1.0.2"
displayName: "Video Upload Aioz St"
summary: "快速上传视频到AIOZ Stream API,建视频对象配编码。Quick upload video to AIOZ Stream API. Create video objects wit"
license: "Proprietary"
description: |-，可生成提升工作效率
  Quick upload video to AIOZ Stream API. Create video objects with default
  or custom encoding config, upload thumbnails, manage and delete videos.
tags:
  - Creative
  - 视频处理
  - 媒体
  - 创意
tools:
  - read
  - write
  - exec
homepage: ""
category: "Creative"

---

# Video Upload Aioz St

## 核心能力

### Calculate Transcode Price
Before uploading, estimate the transcoding cost. 请参考平台API文档了解具体调用方式。

**输入**: 用户提供Calculate Transcode Price所需的指令和必要参数.
**处理**: 解析Calculate Transcode Price的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Calculate Transcode Price的处理结果,包含执行状态码、结果数据和执行日志。### Upload Thumbnail
After creating a video, upload a custom thumbnail. 请参考平台API文档了解具体调用方式。

Supported formats: `.png`, `.jpg`

**输入**: 用户提供Upload Thumbnail所需的指令和必要参数.
**处理**: 解析Upload Thumbnail的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Upload Thumbnail的处理结果,包含执行状态码、结果数据和执行日志。### Update Video Object
Modify video metadata after creation. 请参考平台API文档了解具体调用方式。

**处理**: 解析Update Video Object的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Update Video Object的处理结果,包含执行状态码、结果数据和执行日志。### List All Videos
Retrieve all videos with filtering. 请参考平台API文档了解具体调用方式。

**输入**: 用户提供List All Videos所需的指令和必要参数.
**处理**: 解析List All Videos的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### Delete Video
Remove a video. 请参考平台API文档了解具体调用方式。

**输入**: 用户提供Delete Video所需的指令和必要参数.
**处理**: 解析Delete Video的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Delete Video的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 编码执行 | 需求描述与约束条件 | 代码文件与测试结果 |
| 视频生成 | 脚本与画面描述 | 视频文件与时长信息 |
| 快速上传视频到AIO | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | video-upload-stream-tool处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "tool_result": "tool_result_value",
      "tool_metadata": "tool_metadata_value",
      "tool_status": "tool_status_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/video-upload-stream-tool_template`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

## 案例展示

1. User: "Upload my video to AIOZ Stream"
2. Ask for API keys (public + secret) if not known
3. Ask for the video file path
4. Ask: "Default upload (quick) or custom config?"
   * If default: ask for title only
   * If custom: ask for title, qualities (e.g., 720p, 1080p), codec preference, tags, etc.
5. **Step 1:** Create video object → get `VIDEO_ID`
6. **Step 2:** Compute file hash, upload file part
7. **Step 3:** Call complete endpoint
8. Fetch video detail → return streaming URL to user

## 常见问题

### Q1: 如何开始使用Video Upload Aioz St？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要AIOZ Stream API密钥才能使用完整功能
- 需要LLM支持，无LLM环境无法使用
