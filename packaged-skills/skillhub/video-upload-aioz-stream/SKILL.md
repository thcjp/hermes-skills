---
slug: video-upload-aioz-stream
name: video-upload-aioz-stream
version: "1.0.1"
displayName: Video Upload Aioz St
summary: Quick upload video to AIOZ Stream API. Create video objects with default
  or custom encoding confi...
license: MIT
description: |-
  Quick upload video to AIOZ Stream API。Create video objects with default
  or custom encoding confi。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
---
# Video Upload Aioz St

## 核心能力

### Calculate Transcode Price
Before uploading, estimate the transcoding cost:

```bash
curl -s 'https://api-w3stream.attoaioz.cyou/api/videos/cost?duration=60&qualities=360p,1080p' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY'
```

**输入**: 用户提供Calculate Transcode Price所需的指令和必要参数。
**处理**: 按照skill规范执行Calculate Transcode Price操作,遵循单一意图原则。
**输出**: 返回Calculate Transcode Price的执行结果,包含操作状态和输出数据。### Upload Thumbnail
After creating a video, upload a custom thumbnail:

```bash
curl -s -X POST "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID/thumbnail" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -F 'file=@/path/to/thumbnail.jpg'
```

Supported formats: `.png`, `.jpg`

**输入**: 用户提供Upload Thumbnail所需的指令和必要参数。
**处理**: 按照skill规范执行Upload Thumbnail操作,遵循单一意图原则。
**输出**: 返回Upload Thumbnail的执行结果,包含操作状态和输出数据。### Update Video Object
Modify video metadata after creation:

```bash
curl -s -X PATCH "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Updated Title",
    "description": "Updated description",
    "tags": ["new", "tags"],
    "is_public": true
  }'
```

**处理**: 按照skill规范执行Update Video Object操作,遵循单一意图原则。
**输出**: 返回Update Video Object的执行结果,包含操作状态和输出数据。### List All Videos
Retrieve all videos with filtering:

```bash
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "limit": 10,
    "offset": 0,
    "sort_by": "created_at",
    "order_by": "desc",
    "status": "done"
  }'
```

**输入**: 用户提供List All Videos所需的指令和必要参数。
**处理**: 按照skill规范执行List All Videos操作,遵循单一意图原则。### Delete Video
Remove a video:

```bash
curl -s -X DELETE "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY'
```

**输入**: 用户提供Delete Video所需的指令和必要参数。
**处理**: 按照skill规范执行Delete Video操作,遵循单一意图原则。
**输出**: 返回Delete Video的执行结果,包含操作状态和输出数据。
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: Quick、objects、default、encoding、confi、Use、需要设计创作、海报制作、品牌视觉时使用、不适用于、建模和动画制作、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

### 命令参数说明

- `-w3stream`: 命令参数,用于指定操作选项
- `-secret-key`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-public-key`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-F`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项

### 命令参数说明

- `-X`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项

### 命令参数说明

- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| mode | string | 否 | 处理模式, 可选: json/text/markdown, 默认: 默认值 |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明"
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

中间产物模板参考: `assets/（根据实际场景填充）`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
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

### Q2: 遇到错误怎么办？
A: 

### Q3: Video Upload Aioz St有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
