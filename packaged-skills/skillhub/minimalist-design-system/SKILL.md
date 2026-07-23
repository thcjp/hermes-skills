---
slug: "minimalist-design-system"
name: "minimalist-design-system"
version: "1.0.0"
displayName: "Minimalist Design Sy"
summary: "专家级前端架构师与UI/UX设计系统集成指南。极简现代主义设计系统，帮助将精密设计系统无缝集成到现有代码库。适用于：前端组件开发、UI设计实现、设计令牌配置、Tailwind"
license: "Proprietary"
description: |-
  专家级前端架构师与UI/UX设计系统集成指南。极简现代主义设计系统，帮助将精密设计系统无缝集成到现有代码库。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。
tags:
  - Creative
  - Development
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "设计,UI/UX,创意"
---
# Minimalist Design Sy

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Minimalist Design Sy设计令牌配置 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

- 专家级前端架构师与UI/UX设计系统集成指南
- 极简现代主义设计系统，帮助将精密设计系统无缝集成到现有代码库
- 适用于：前端组件开发、UI设计实现、设计令牌配置、Tailwind
  CSS定制、响应式
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 1. 深度系统建模（动笔前必做）

1. **技术栈识别**：框架(React/Next.js/Vue/Svelte)、样式方案(Tailwind/shadcn/CSS Modules)
2. **设计令牌解析**：色彩体系、空间系统、字体阶梯、圆角、阴影
3. **组件架构审查**：封装深度、命名规范、布局原语
4. **工程约束记录**：CSS冲突、包体积限制、第三方UI库覆盖

### 2. 需求聚焦

明确集成意图：

5. 特定局部重塑？
6. 全局架构重构？
7. 全新功能增量？

### 3. 实施原则

8. **设计令牌中心化**：通过全局变量统一管理
9. **可复用性与组合性**：无状态、高内聚组件
10. **消除样式冗余**：拒绝一次性硬编码
11. **维护性与语义化**：命名反映意图而非外观

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | minimalist-design-system处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

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
### 1. 深度系统建模（动笔前必做）(补充)
# ...
* **技术栈识别**：框架(React/Next.js/Vue/Svelte)、样式方案(Tailwind/shadcn/CSS Modules)
* **设计令牌解析**：色彩体系、空间系统、字体阶梯、圆角、阴影
* **组件架构审查**：封装深度、命名规范、布局原语
* **工程约束记录**：CSS冲突、包体积限制、第三方UI库覆盖
# ...
### 2. 需求聚焦(补充)
# ...
明确集成意图：
# ...
* 特定局部重塑？
* 全局架构重构？
* 全新功能增量？
# ...
### 3. 实施原则(补充)
# ...
* **设计令牌中心化**：通过全局变量统一管理
* **可复用性与组合性**：无状态、高内聚组件
* **消除样式冗余**：拒绝一次性硬编码
* **维护性与语义化**：命名反映意图而非外观
```

## 常见问题

### Q1: 如何开始使用Minimalist Design Sy？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

