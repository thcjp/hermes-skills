---
slug: "ziptax"
name: "ziptax"
version: 1.0.1
displayName: "Ziptax Sales Tax"
summary: "销售税查询(其脚本可本地运行需谨慎)。This sales-tax lookup skill is legitimate in purpose, but its bundled lookup"
license: "MIT"
description: |-
  This sales-tax lookup skill is legitimate in purpose, but its bundled
  lookup script can run local。Use when 用户需要Ziptax Sales Tax相关功能时使用。不适用于超出本技能能力范围的复杂需求.
tags:
  - Development
  - 工具
  - 效率
  - api
  - lookup
  - bash
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# Ziptax Sales Tax

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Ziptax Sales Tax销售税查询 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

- This sales-tax lookup skill is legitimate in purpose, but its bundled
  lookup script can run local
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 信息查询 | 查询条件与关键词 | 查询结果与匹配记录 |
| 销售税查询 | 目标数据与配置参数 | 处理结果与执行状态 |
| 其脚本可本地运行需谨 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Address Lookup (most accurate)

```bash
curl -s "https://api.zip-tax.com/request/v60?address=200+Spectrum+Center+Drive+Irvine+CA+92618" \
  -H "X-API-KEY: $ZIPTAX_API_KEY"
```

### Postal Code Lookup

```bash
curl -s "https://api.zip-tax.com/request/v60?postalcode=92618" \
  -H "X-API-KEY: $ZIPTAX_API_KEY"
```

### Lat/Lng Lookup

```bash
curl -s "https://api.zip-tax.com/request/v60?lat=33.6525&lng=-117.7479" \
  -H "X-API-KEY: $ZIPTAX_API_KEY"
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | ziptax处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "ziptax_result": "ziptax_result_value",
      "ziptax_metadata": "ziptax_metadata_value",
      "ziptax_status": "ziptax_status_value"
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

中间产物模板参考: `assets/ziptax_template`

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
### Address Lookup (most accurate)(补充)
# ...
```bash
curl -s "https://api.zip-tax.com/request/v60?address=200+Spectrum+Center+Drive+Irvine+CA+92618" \
  -H "X-API-KEY: $ZIPTAX_API_KEY"
```
# ...
### Postal Code Lookup(补充)
# ...
```bash
curl -s "https://api.zip-tax.com/request/v60?postalcode=92618" \
  -H "X-API-KEY: $ZIPTAX_API_KEY"
```
# ...
### Lat/Lng Lookup(补充)
# ...
```bash
curl -s "https://api.zip-tax.com/request/v60?lat=33.6525&lng=-117.7479" \
  -H "X-API-KEY: $ZIPTAX_API_KEY"
```
```

## 常见问题

### Q1: 如何开始使用Ziptax Sales Tax？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 本地运行，不支持多设备同步
- 依赖Agent平台的LLM能力与运行环境配置
- 免费版功能受限，高级能力需升级专业版
- 处理能力受限于本地硬件资源
