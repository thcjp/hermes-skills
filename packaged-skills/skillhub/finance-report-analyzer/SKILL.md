---
slug: "finance-report-analyzer"
name: "finance-report-analyzer"
version: "1.2.0"
displayName: "Finance Report Analy"
summary: "分析Excel/PDF财务数据,生成含迷你图的交互报告"
license: "Proprietary"
description: |-
  Analyze financial data from uploaded Excel/PDF files and generate interactive
  reports with sparkl。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Finance
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "金融,财务,数据"
---
# Finance Report Analy

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| DCF估值建模与敏感性分析 | 不支持 | 支持 |
| 财务舞弊识别(Beneish M-Score) | 不支持 | 支持 |
| 批量财报处理与自动化报告 | 不支持 | 支持 |
| 行业基准对比与跨期趋势分析 | 不支持 | 支持 |
| 多币种折算与汇率风险管理 | 不支持 | 支持 |

## 核心能力

* **Sparkline trend charts**: Each metric row has an inline SVG showing the trend (solid=actual, dashed=forecast)
* **Forecast markers**: Predicted values marked with ⟡ symbol and yellow background
* **Color coding**: Green=positive, Red=negative
* **Responsive**: Works on mobile and desktop
* **Print-ready**: CSS print styles included
### Sparkline trend charts

针对Sparkline trend charts,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供Sparkline trend charts相关的配置参数、输入数据和处理选项。

**输出**: 返回Sparkline trend charts的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Sparkline trend charts`的配置文档进行参数调优
### Forecast markers

针对Forecast markers,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供Forecast markers相关的配置参数、输入数据和处理选项。

**输出**: 返回Forecast markers的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Forecast markers`的配置文档进行参数调优
### Color coding

针对Color coding,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供Color coding相关的配置参数、输入数据和处理选项。

**输出**: 返回Color coding的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Color coding`的配置文档进行参数调优
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

```bash
python3 （请参考skill目录中的脚本文件） input.xlsx -o pdf --company "公司名" --ticker "000001.SZ"
```

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤。

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | finance-report-analyzer处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "analyzer_result": "analyzer_result_value",
      "analyzer_metadata": "analyzer_metadata_value",
      "analyzer_status": "analyzer_status_value"
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

中间产物模板参考: `assets/finance-report-analyzer_template`

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
## 案例展示

### 示例1：基础用法

```
```bash
python3 （请参考skill目录中的脚本文件） input.xlsx -o pdf --company "公司名" --ticker "000001.SZ"
```
```

## 常见问题

### Q1: 如何开始使用Finance Report Analy？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

