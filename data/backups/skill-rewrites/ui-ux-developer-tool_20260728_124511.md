---

slug: "ui-ux-developer-tool"
name: "ui-ux-developer-tool"
version: "1.0.0"
displayName: "工具"
summary: "UI设计技能(其setup脚本会改Nginx与系统配置需谨慎)。This UI design skill is useful, but its setup script can make p"
summary_zh: "UI设计技能(其setup脚本会改Nginx与系统配置需谨慎)。This UI design skill is useful, but its setup script can make p"
license: "MIT"
description: This UI design skill is useful, but its setup script can make persistent privileged Nginx and sys，可生成提升工作效率
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

# Ui Ux Dev

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Ui Ux DevNginx与系统配置 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

- This UI design skill is useful, but its setup script can make persistent
  privileged Nginx and sys
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| UI设计 | 界面需求与设计规范 | UI设计方案与实现代码 |
| 环境配置 | Nginx与系统配置参数 | 持久化的服务部署配置 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | ui-ux-developer-tool处理的内容输入 |,  |
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

中间产物模板参考: `assets/ui-ux-developer-tool_template`

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

## 常见问题

### Q1: 如何开始使用Ui Ux Dev？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |


---

## 边界条件与限制 (Boundary Conditions)

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

