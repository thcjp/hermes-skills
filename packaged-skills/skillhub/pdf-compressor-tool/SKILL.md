---
slug: "pdf-compressor-tool"
name: "pdf-compressor-tool"
version: "1.0.1"
displayName: "Compress PDF"
summary: "上传PDF到Cross-Service-Solutions压缩,轮询至完成。Compress a user-provided PDF by uploading it to Cross-Ser"
license: "Proprietary"
description: |-
  Compress a user-provided PDF by uploading it to Cross-Service-Solutions,
  polling until completion. Returns download URL and compression settings.
  自动化压缩PDF文件,节省存储空间,优化文档处理流程
tags:
  - Knowledge
  - pdf
  - llm
  - 压缩
  - 文件
  - 上传
  - 下载
tools:
  - read
  - write
  - exec
homepage: ""
category: "Automation"
---
# Compress PDF

## 核心能力

- **PDF上传压缩**: 将用户提供的PDF文件上传至Cross-Service-Solutions服务进行压缩处理,轮询任务状态直至完成
- **智能压缩策略**: 根据PDF内容类型(扫描件/文本/混合)自动选择最优压缩参数,平衡文件大小与清晰度
- **图像质量调节**: 支持自定义图像质量(imageQuality: 10-100)和DPI设置,精确控制压缩程度
- **批量压缩支持**: 支持多个PDF文件依次上传压缩,返回每个文件的处理结果与下载链接
- **状态轮询机制**: 自动轮询压缩任务状态(processing/done/error),无需人工等待,完成后返回下载URL
- **压缩结果下载**: 压缩完成后返回可下载的压缩PDF链接,支持获取原始文件名与压缩设置信息

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 批量PDF压缩(10+) | 不支持 | 支持 |
| 自定义压缩参数(质量/DPI) | 不支持 | 支持 |
| 压缩历史记录与审计 | 不支持 | 支持 |
| API调用额度提升 | 有限 | 高额度 |
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| PDF处理 | PDF文件与操作类型 | 提取文本或生成文档 |
| 上传PDF到Cros | 目标数据与配置参数 | 处理结果与执行状态 |
| 轮询至完成 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| file_path | string | 是 | 待压缩的PDF文件本地路径 |
| image_quality | number | 否 | 图像质量(10-100),默认75,值越低压缩率越高 |
| dpi | number | 否 | 输出DPI,默认144,扫描件建议降低至72-96 |
| output_dir | string | 否 | 压缩结果保存目录,默认与源文件同目录 |
| callback_url | string | 否 | 异步回调通知URL,压缩完成后推送结果 |

## 输出格式

Return a structured result:

* `job_id` (number)
* `status` (string)
* `download_url` (string, when done)
* `file_name` (string, when available)
* `settings` (object)

Example output:

```json
{
  "job_id": 123,
  "status": "done",
  "download_url": "https://.../compressed.pdf",
  "file_name": "compressed.pdf",
  "settings": { "imageQuality": 75, "dpi": 144 }
}
```

## 示例代码

### 1. 单文件PDF压缩（PowerShell）

上传PDF文件并轮询压缩状态直至完成:

```powershell
# 上传PDF到压缩服务
$filePath = "C:\Documents\large_report.pdf"
$uploadResponse = Invoke-RestMethod -Uri "https://api.cross-service-solutions.com/upload" `
    -Method Post -InFile $filePath -ContentType "application/pdf"

$jobId = $uploadResponse.job_id
Write-Host "压缩任务已创建, Job ID: $jobId"

# 轮询任务状态
$status = "processing"
while ($status -eq "processing") {
    Start-Sleep -Seconds 3
    $statusResponse = Invoke-RestMethod -Uri "https://api.cross-service-solutions.com/status/$jobId"
    $status = $statusResponse.status
    Write-Host "当前状态: $status"
}

# 下载压缩结果
if ($status -eq "done") {
    $downloadUrl = $statusResponse.download_url
    Invoke-WebRequest -Uri $downloadUrl -OutFile "C:\Documents\compressed_report.pdf"
    Write-Host "压缩完成! 已保存至 C:\Documents\compressed_report.pdf"
}
```

### 2. 自定义压缩参数（JSON请求体）

指定图像质量与DPI进行精细压缩:

```json
{
  "file_path": "/documents/scanned_contract.pdf",
  "image_quality": 50,
  "dpi": 96,
  "output_dir": "/documents/compressed/"
}
```

**参数选择建议**:
- 扫描件PDF: `image_quality=50, dpi=96` (大幅压缩,文字仍可读)
- 文本PDF: `image_quality=80, dpi=144` (轻度压缩,保持清晰度)
- 混合PDF: `image_quality=70, dpi=120` (平衡压缩率与质量)

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试 |
| PDF文件损坏 | 文件格式无效或已损坏 | 使用PDF修复工具修复后重新上传,或更换源文件 |
| 文件过大超限 | 超过服务端文件大小限制 | 拆分PDF为大文件分段上传,或降低原始扫描分辨率 |
| 压缩任务超时 | 服务端处理排队或文件复杂度高 | 增加轮询超时时间至120s,或稍后重试 |
| 压缩无效果 | PDF已高度优化(纯文本) | 此为正常现象,纯文本PDF压缩空间极小,建议使用ZIP归档 |
| 下载链接过期 | 下载URL有时效限制 | 重新发起压缩任务获取新链接,或及时下载保存 |

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

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪.
### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界.

## 已知限制

- PDF文件需上传至第三方服务（Cross-Service-Solutions）处理，含敏感信息的文档存在数据外泄风险
- 压缩效果取决于原始PDF内容结构，已高度优化的PDF（如纯文本PDF）可能无法进一步压缩
- 依赖网络连接与第三方服务可用性，服务中断或网络不稳定时无法完成压缩任务
