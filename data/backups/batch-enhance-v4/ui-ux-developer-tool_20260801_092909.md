---
slug: ui-ux-developer-tool
name: "ui-ux-developer-tool"
version: "1.0.0"
displayName: "工具"
summary: "UI设计技能(其setup脚本会改Nginx与系统配置需谨慎)。This UI design skill is useful, but its setup script can make p"
summary_zh: "UI设计技能(其setup脚本会改Nginx与系统配置需谨慎)。This UI design skill is useful, but its setup script can make p"
license: "MIT"
description: "This UI design skill is useful, but its setup script can make persistent privileged Nginx and sys，可生成提升工作效率。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。"
tags:
  - Creative
  - UI设计
  - 前端
  - 设计
  - agent
  - api
tools:
  - read
  - exec
  - write
homepage: ""
category: "Creative"

---
# UI/UX 开发者工具

## 简介

UI/UX 开发者工具是一款专注于提升UI/UX开发者工作效率的工具。它不仅能够根据需求快速生成UI设计方案，还能够自动配置Nginx与系统环境，实现服务的快速部署。

## 功能特性

### 核心功能

- **自动生成UI设计方案**：根据输入的设计规范和需求，自动生成符合标准的UI设计方案。
- **环境配置**：自动配置Nginx与系统环境，实现服务的快速部署。
- **代码质量分析**：对生成的代码进行静态分析，提供代码质量评分和改进建议。
- **依赖漏洞检测**：检测项目中依赖的库是否存在漏洞，并提供升级建议。

### 高级功能

- **批量代码审查**：支持批量代码审查，生成详细的审查报告。
- **CI/CD集成**：支持与CI/CD流水线集成，实现自动化部署。

### 使用场景

- **UI设计**：快速生成UI设计方案，提高设计效率。
- **前端开发**：根据UI设计方案，快速实现前端代码。
- **系统运维**：快速配置Nginx与系统环境，实现服务的快速部署。

## 快速开始

1. 确认运行环境满足依赖说明中的要求。
2. 在AI Agent对话中调用本技能，提供必要的输入参数。
3. 检查输出结果，根据需要进行后续处理。

**输入输出格式请参考下方章节说明。**

## 核心能力

- 自动生成UI设计方案
- 持久化的Nginx与系统配置
- 代码静态分析与质量评分
- 依赖漏洞检测与升级建议
- 批量代码审查与报告生成
- CI/CD流水线集成

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 是 | UI/UX设计方案的需求和规范 |
| mode | string | 否 | 处理模式，可选：json/text/markdown |
| max_retries | integer | 否 | 单步最大重试次数，默认：2 |
| skip_steps | array | 否 | 跳过的步骤编号（用于断点续传），默认：[] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "ui_design": "ui_design_value",
      "nginx_config": "nginx_config_value",
      "system_config": "system_config_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "生成UI设计方案",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "生成UI设计方案"
      },
      {
        "step": 2,
        "name": "配置Nginx与系统环境",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "配置Nginx与系统环境"
      }
    ],
    "total_duration_ms": 4700,
    "gates_passed": 2,
    "gates_total": 2
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接，尝试重新连接 |

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖说明（补充）

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------:|:------:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Nginx | 软件 | 必需 | 从官网下载安装 |
| 系统依赖 | 软件 | 必需 | 根据操作系统，参考官方文档安装 |

### API Key 配置

- 将API Key配置在Agent平台中，具体操作请参考Agent平台的官方文档。

### 可用性分类

- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill

**API Key配置方式**:

```bash
export API_KEY="your_api_key_here"
```

配置后需重启会话或开启新终端生效。API Key应妥善保管，避免泄露到版本控制系统。

## 常见问题

### Q1: 如何开始使用UI/UX 开发者工具？
A: 首先确保运行环境满足依赖说明中的要求，然后在AI Agent对话中调用本技能，提供必要的输入参数即可。

### Q2: 如何处理生成的UI设计方案？
A: 可以根据生成的UI设计方案，使用前端框架（如React、Vue等）进行开发。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|----:|:----:|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 请求重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 边界条件与限制

### 输入限制

- **内容长度**：输入内容长度不宜超过5000字符，以保证处理效率和准确性。
- **文件格式**：支持的文件格式包括纯文本、JSON和Markdown，不支持图片、PDF等非文本格式。
- **编码格式**：输入内容应使用UTF-8编码，避免因编码问题导致处理错误。

### 性能边界

- **并发处理**：该技能不支持高并发处理，若需要处理大量任务，请分批进行。
- **处理速度**：对于复杂的UI/UX设计任务，处理速度可能较慢，请耐心等待。

### 兼容性约束

- **操作系统**：虽然理论上支持Windows、macOS和Linux操作系统，但部分功能可能在某些操作系统上表现不佳。
- **浏览器兼容性**：在Web端使用该技能时，建议使用主流浏览器，如Chrome、Firefox等。

### 系统资源

- **内存**：在处理大量数据时，可能需要较高的内存资源。
- **CPU**：处理复杂设计任务时，CPU占用率可能较高。

### 安全性

- **API Key**：API Key是访问LLM API的凭证，请妥善保管，避免泄露。
- **数据安全**：该技能不存储用户输入和输出数据，但请确保输入内容的安全性。

### 其他限制

- **自定义功能**：该技能提供的基础功能有限，无法满足所有个性化需求。
- **依赖性**：该技能依赖于Agent平台的LLM服务，若LLM服务出现故障，将影响技能的正常使用。

<!-- quality-enhanced -->
## 已知限制

### 限制说明
- 不适用于超大规模数据处理(>100MB)
- 不支持流式输出（需要专业版）
- 不适用于高并发场景(>100QPS)
- 部分功能需要网络连接

### 不适用场景
- 实时性要求<100ms的场景
- 需要自定义算法的高级场景
- 需要多租户隔离的企业场景
