---
slug: "job-auto-apply"
name: "job-auto-apply"
version: 1.0.1
displayName: "Job Auto Apply"
summary: "求职申请自动化,代你提交申请(需授权谨慎)"
license: "Proprietary"
description: |-
  This skill fits its job-application automation purpose, but it gives
  an agent authority to submit。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务.
tags:
  - Research
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "exec", "glob", "grep"]
tags: "工具,效率,自动化"
category: "Automation"
---
# Job Auto Apply

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

- Job Auto Apply 结果导出 - 按流程执行步端到端pipeline配置流程
- Job Auto Apply 实时监控 - 步骤间自动质量gate检查
- Job Auto Apply 错误重试 - 支持多种变体等多种处理模式
- Job Auto Apply 多格式支持 - 失败自动重试+断点续传
- Job Auto Apply 扩展能力9 - 全流程可追溯, 输出执行日志
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 自动化流程 | 流程定义与触发参数 | 执行状态与步骤日志 |
| 求职申请自动化 | 目标数据与配置参数 | 处理结果与执行状态 |
| 代你提交申请 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 1. Set Up User Profile

First, create a user profile using the template:

```bash
cp profile_template.json ~/job_profile.json
# ...
```

### 2. Run Job Search and Apply

```bash
python job_search_apply.py \
  --title "Software Engineer" \
  --location "San Francisco, CA" \
  --remote \
  --max-applications 10 \
  --dry-run
# ...
python job_search_apply.py \
  --profile ~/job_profile.json \
  --title "Backend Engineer" \
  --platforms linkedin,indeed \
  --auto-apply
# ...
python job_search_apply.py \
  --profile ~/job_profile.json \
  --title "Senior Developer" \
  --no-dry-run \
  --require-confirmation
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | job-auto-apply处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "apply_result": "apply_result_value",
      "apply_metadata": "apply_metadata_value",
      "apply_status": "apply_status_value"
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

中间产物模板参考: `assets/job-auto-apply_template`

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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 示例1：基础用法

```
### 1. Set Up User Profile(补充)
# ...
First, create a user profile using the template:
# ...
```bash
cp profile_template.json ~/job_profile.json

```
# ...
### 2. Run Job Search and Apply(补充)
# ...
```bash
python job_search_apply.py \
  --title "Software Engineer" \
  --location "San Francisco, CA" \
  --remote \
  --max-applications 10 \
  --dry-run

python job_search_apply.py \
  --profile ~/job_profile.json \
  --title "Backend Engineer" \
  --platforms linkedin,indeed \
  --auto-apply

python job_search_apply.py \
  --p
```
# ...
## 常见问题
# ...
### Q1: 如何开始使用Job Auto Apply？
A: 
# ...
### Q2: 遇到错误怎么办？
A: 
# ...
### Q3: Job Auto Apply有什么限制？
A: 
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
# ...