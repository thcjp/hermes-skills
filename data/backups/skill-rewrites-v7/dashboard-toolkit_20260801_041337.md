---
slug: dashboard-toolkit
name: dashboard-toolkit
version: "1.7.3"
displayName: "仪表盘工具箱"
summary: "SkillHub实时运营仪表盘,监控会话/成本/cron/网关。Real-time operations dashboard for SkillHub。Monitors sessions,"
summary_zh: "SkillHub实时运营仪表盘,监控会话/成本/cron/网关。Real-time operations dashboard for SkillHub。Monitors sessions,"
license: "MIT"
description: |-
  Real-time operations dashboard for SkillHub。监控会话、成本、定时任务和网关健康状态。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。
tags:
  - api
  - agent
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"

---
# SkillHub-dashboard

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

仪表盘工具箱提供实时运营监控能力，支持会话监控、成本分析、定时任务管理和网关健康检查。帮助运维团队全面掌握系统运行状态，及时发现并处理异常。

### 核心功能

仪表盘工具箱提供以下核心功能：

1. **自动化处理**：根据输入参数自动执行核心处理流程，返回结构化结果
2. **多模式支持**：支持JSON、文本和Markdown三种输入输出模式
3. **错误恢复**：内置重试机制和断点续传能力，确保任务可靠完成
4. **配置灵活**：通过环境变量和配置文件管理运行参数，适配不同环境

### 输入输出规范

接收用户提供的输入数据和配置参数，经过核心逻辑处理后返回包含处理结果、执行状态和元数据的结构化响应。

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 仪表盘构建 | 数据源与布局配置 | 仪表盘页面与刷新状态 |
| Cron配置 | 时间表达式与命令 | 调度ID与下次执行时间 |
| 监控告警 | 监控目标与阈值 | 告警事件与指标快照 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | -dashboard处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "dashboard_result": "dashboard_result_value",
      "dashboard_metadata": "dashboard_metadata_value",
      "dashboard_status": "dashboard_status_value"
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

中间产物模板参考: `assets/-dashboard_template`

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

- 通过环境变量 `API_KEY` 设置LLM服务的API密钥
### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.## 故障排查

| 问题 | 可能原因 | 解决方案 |
|:-----|:---------|:---------|
| 技能调用无响应 | LLM服务不可达 | 检查网络连接和API Key配置 |
| 输出格式异常 | 输入参数不符合规范 | 参考输入格式章节校验参数 |
| 执行超时 | 处理数据量过大 | 分批处理或增加超时时间 |
| 权限错误 | 运行环境权限不足 | 检查文件系统和命令执行权限 |
## 安全注意事项

- **无硬编码密钥**: 所有API Key和凭证通过环境变量加载
- **无敏感信息泄露**: 日志中对敏感字段进行脱敏处理
- **凭证存储安全**: 配置文件建议加入.gitignore
- **最小权限原则**: 仅授予完成任务所需的最小权限
- **数据传输加密**: 所有API调用使用HTTPS加密传输

## 常见问题

### Q1: 如何开始使用-dashboard？
A: 请参考使用流程和依赖说明章节，确保运行环境满足要求后调用本技能。
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 请求重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
