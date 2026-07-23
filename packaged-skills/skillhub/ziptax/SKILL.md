---
slug: "ziptax"
name: "ziptax"
version: "1.0.0"
displayName: "Ziptax Sales Tax"
summary: "销售税查询(其脚本可本地运行需谨慎)"
license: "Proprietary"
description: |-
  This sales-tax lookup skill is legitimate in purpose, but its bundled
  lookup script can run local。Use when 用户需要Ziptax Sales Tax相关功能时使用。不适用于超出本技能能力范围的复杂需求。
tags:
  - Development
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# Ziptax Sales Tax

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| This sales-tax lookup skill is legitimate in purpose, but its bundled | 支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- This sales-tax lookup skill is legitimate in purpose, but its bundled
  lookup script can run local
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

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
|--------|------|------|------|
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
| 网络错误 | 连接超时或不可达 | 

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

### 示例1：基础用法

```
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
```

## 常见问题

### Q1: 如何开始使用Ziptax Sales Tax？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Ziptax Sales Tax有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 本地运行，不支持多设备同步
