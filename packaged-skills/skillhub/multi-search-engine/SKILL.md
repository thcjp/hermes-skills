---
slug: "multi-search-engine"
name: "multi-search-engine"
version: "2.1.3"
displayName: "Multi Search Engine"
summary: "多搜索引擎集成,16引擎(7国内+9全球)"
license: "Proprietary"
description: |-
  Multi search engine integration with 16 engines (7 CN + 9 Global)。核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Security
  - Integrations
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tools: ["read", "exec", "glob", "grep"]
tags: "搜索,检索,工具"
---
# Multi Search Engine

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

- Multi search engine integration with 16 engines (7 CN + 9 Global)
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 多引擎搜索 | 搜索关键词和目标引擎 | 聚合搜索结果和排名 |
| 中文搜索 | 中文查询词 | 国内搜索引擎结果汇总 |
| 全球搜索 | 英文查询词 | 国际搜索引擎结果汇总 |

**不适用于**：需要实时索引和全文检索的私有数据搜索

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| query | string | 是 | 搜索关键词 |
| engines | string | 否 | 搜索引擎列表, 如: google,bing,baidu, 默认: 全部16引擎 |

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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

```javascript
// Basic search
web_fetch({"url": "https://www.google.com/search?q=python+tutorial"})
// ...
// Site-specific
web_fetch({"url": "https://www.google.com/search?q=site:github.com+react"})
// ...
// File type
web_fetch({"url": "https://www.google.com/search?q=machine+learning+filetype:pdf"})
// ...
// Time filter (past week)
web_fetch({"url": "https://www.google.com/search?q=ai+news&tbs=qdr:w"})
// ...
// Privacy search
web_fetch({"url": "https://duckduckgo.com/html/?q=privacy+tools"})
// ...
// DuckDuckGo Bangs
web_fetch({"url": "https://duckduckgo.com/html/?q=!gh+tensorflow"})
// ...
// Knowledge calculation
web_fetch({"url": "https://www.wolframalpha.com/input?i=100+USD+to+CNY"})
```

## 常见问题

### Q1: 如何开始使用Multi Search Engine？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

