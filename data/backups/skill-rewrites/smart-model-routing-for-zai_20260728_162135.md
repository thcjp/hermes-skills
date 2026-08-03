---
slug: "smart-model-routing-for-zai"
name: "smart-model-routing-for-zai"
version: 1.0.1
displayName: "模型路由指南"
summary: "z.ai模型路由指南,不装代码不索凭据。This skill is a disclosed z。ai model-routing guide and does not install cod"
summary_zh: "z.ai模型路由指南,不装代码不索凭据。This skill is a disclosed z。ai model-routing guide and does not install cod"
license: "MIT"
description: |-
  This skill is a disclosed z。ai model-routing guide and does not install
  code, request credentials。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策.
tags:
  - Development
  - 工具
  - 效率
  - 创意
  - api
  - llm
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# Smart Model Routing

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

- This skill is a disclosed z
- ai model-routing guide and does not install
  code, request credentials
- ai, zai, disclosed, smart, skill
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 模型路由选择 | 任务类型和性能需求 | 最优模型推荐和路由配置 |
| 成本优化分析 | 使用量和预算限制 | 模型切换策略和成本预测 |
| 路由规则配置 | 路由条件和优先级 | z.ai模型路由规则集 |

**不适用于**：非z.ai平台的模型路由和切换

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| task_type | string | 是 | 任务类型, 如: chat/code/vision |
| optimize_for | string | 否 | 优化目标, 可选: speed/cost/quality, 默认: quality |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 工具依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
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
## 常见问题

### Q1: 如何开始使用Smart Model Routing？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |


---
## 边界条件与限制 (Boundary Conditions)

### 输入限制
- **任务类型限制**：技能仅支持特定的任务类型，如chat、code、vision等，不支持自定义任务类型。
- **性能参数限制**：输入的优化目标参数`optimize_for`只能是speed、cost或quality，且默认值为quality。
- **输入格式限制**：输入参数必须符合规定的格式，否则技能将无法正确处理。

### 性能边界
- **并发处理限制**：技能可能无法同时处理大量请求，特别是在高负载情况下。
- **响应时间限制**：技能的响应时间可能受到网络延迟和模型负载的影响，无法保证在所有情况下都能达到实时响应。

### 兼容性约束
- **平台兼容性**：技能仅在支持SKILL.md的AI Agent平台上运行，如Claude Code、Cursor、Codex、Gemini CLI等。
- **操作系统兼容性**：技能在Windows、macOS和Linux操作系统上运行，但不保证在其他操作系统上的兼容性。
- **LLM API兼容性**：技能依赖于内置的LLM API，如果LLM API更新或更改，可能需要技能进行相应的调整。

### 其他限制
- **模型路由范围**：技能仅适用于z.ai平台的模型路由和切换，不支持非z.ai平台的模型。
- **确定性限制**：技能不适用于需要100%确定性的关键决策场景，因为AI模型的预测结果可能存在不确定性。

