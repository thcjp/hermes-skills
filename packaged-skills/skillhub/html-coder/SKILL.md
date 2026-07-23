---
slug: "html-coder"
name: "html-coder"
version: "2.0.1"
displayName: "HTML Coder"
summary: "专家级HTML开发,构建网页/表单/交互内容"
license: "Proprietary"
description: |-
  Expert HTML development skill for building web pages, forms, and interactive
  content。Use when cr。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Creative
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# HTML Coder

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Expert HTML development skill for building web pages, forms, and interactive | 支持 | 支持 |
| Use when cr | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Expert HTML development skill for building web pages, forms, and interactive
  content
- Use when cr
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 网页开发 | 页面需求和设计规范 | 语义化HTML和响应式布局 |
| 表单构建 | 表单字段和验证规则 | 可访问的HTML表单和验证脚本 |
| 交互组件 | 组件描述和交互行为 | HTML组件和事件处理代码 |

**不适用于**：后端API开发和数据库设计场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| page_description | string | 是 | 页面需求描述 |
| framework | string | 否 | 目标框架, 可选: vanilla/bootstrap/tailwind, 默认: vanilla |

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

## 常见问题

### Q1: 如何开始使用HTML Coder？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: HTML Coder有什么限制？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

