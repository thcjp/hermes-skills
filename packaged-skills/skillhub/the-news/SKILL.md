---
slug: "the-news"
name: "the-news"
version: 1.0.18
displayName: "The News"
summary: "给Agent实时与归档访问20国头版头条"
license: "Proprietary"
description: |-
  gives agents real-time and archival access to front-page headlines across
  20 countries for breaki
tags:
  - Research
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# The News

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 多源数据聚合与去重 | 不支持 | 支持 |
| 语义搜索与智能摘要 | 不支持 | 支持 |
| 定时监控与变化推送 | 不支持 | 支持 |
| 研究结论结构化导出 | 不支持 | 支持 |
| 知识图谱构建与关系推理 | 不支持 | 支持 |

## 核心能力

- gives agents real-time and archival access to front-page headlines across
  20 countries for breaki
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 给Agent实时与归 | 目标数据与配置参数 | 处理结果与执行状态 |
| the操作执行 | the相关参数与配置 | 执行结果与返回数据 |
| the状态查询 | 查询条件与过滤选项 | 当前状态与详细信息 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | the-news处理的内容输入 |,  |
| content | string | 否 | the-news处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "news 相关配置参数",
    result: "news 相关配置参数",
    result: "news 相关配置参数",
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
## 案例展示

User: `What's going on in Germany right now?`
Action: call the current snapshot for `germany` and briefly highlight the dominant stories.

User: `What happened yesterday night in Israel?`
Action: call `.../israel?at=<timestamp>` and answer from that historical snapshot.

User: `How did the story mix in Turkey change over the last three days?`
Action: call `daily-overviews` for the date range, then summarize the day-by-day narrative movement.

## 常见问题

### Q1: 如何开始使用The News？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

