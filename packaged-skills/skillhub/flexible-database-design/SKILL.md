---
slug: "flexible-database-design"
name: "flexible-database-design"
version: 1.0.1
displayName: "Flexible Database De"
summary: "指导Agent与用户设计实现灵活数据库,建模不踩坑。Guide agents and users to design and implement a \

核心能力:
- 集成工具领"
license: "Proprietary"
description: |-
  Guide agents and users to design and implement a \\\n\n核心能力:\n- 集成工具领域的专业化AI辅助工具\n\
  - 基于高人气开源Skill深度优化升级\n- 移除风险代码,增强安全性和稳定性\n\n适用场景:\n- 第三方API集成、平台对接、数据同步\n- 独立开发者与一人公司效率提升\n\
tags:
  - Integrations
  - Knowledge
  - 数据处理
  - 数据分析
  - 工具
  - 依赖说明
  - agent
  - key
  - created_at
  - api
tools:
  - read
  - exec
  - write
  - glob
homepage: ""
# 定价元数据
category: "Research"
---
# Flexible Database De

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 核心能力

本工具的核心能力包括：指导Agent与用户设计实现灵活数据库,建模不踩坑。具体功能详情请参考下方能力说明表格与使用场景.
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

根据用户描述，选择最接近的场景并适配：

| 场景 | 主干字段建议 | 软字段典型 key |
|:-----|:-----|:-----|
| **个人知识库 / 碎片收集** | id, created_at, source, content_type, raw_content | title, tags, url, project, deadline |
| **政策信息收集** | id, created_at, source, source_type | title, release_date, issuing_org, policy_type, url, policy_no, industry, subsidy_amount |
| **财务报表收集** | id, created_at, source, source_type | company, report_type, report_date, revenue, net_income, total_assets, roa, roe |
| **表单/问卷** | id, created_at, form_id, respondent_id, raw_response | 各题目 id 或题目名 |
| **PDF/报告知识库** | id, created_at, source, content_type, raw_content | report_title, report_type, period_start, period_end, file_path |
| **多源异构（如群消息聚合）** | id, created_at, source, sender, raw_content | data_type, items[], trend, 各业务字段 |

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | flexible-database-design处理的内容输入 |,  |
| content | string | 否 | flexible-database-design处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "design 相关配置参数",
    result: "design 相关配置参数",
    result: "design 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

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
## 常见问题

### Q1: 如何开始使用Flexible Database De？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
