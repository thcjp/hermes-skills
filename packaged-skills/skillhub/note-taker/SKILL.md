---
slug: "note-taker"
name: "note-taker"
version: "2.0.1"
displayName: "Note Taker"
summary: "笔记整理助手。康奈尔笔记法、卡片盒笔记(Zettelkasten)、思维导图笔记、会议笔记、课堂笔记、笔记整理。Note-taking with"
license: "Proprietary"
description: |-
  笔记整理助手。康奈尔笔记法、卡片盒笔记(Zettelkasten)、思维导图笔记、会议笔记、课堂笔记、笔记整理。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
  - Productivity
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
---
# Note Taker

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

- 康奈尔笔记法、卡片盒笔记(Zettelkasten)、思维导图笔记、会议笔记、课堂笔记、笔记整理
- Note-taking
  with Cornell method, Zettelka
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 康奈尔笔记 | 课堂或会议内容 | 结构化的康奈尔笔记模板 |
| 卡片盒笔记 | 知识点和参考链接 | Zettelkasten格式笔记和链接 |
| 思维导图笔记 | 主题和子话题 | 层次化思维导图和大纲 |

**不适用于**：需要自动语音转写的实时会议记录场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| note_type | string | 是 | 笔记类型, 可选: cornell/zettelkasten/mindmap/meeting |
| subject | string | 否 | 笔记主题, 默认: 通用 |

## 输出格式

Commands print concise confirmations to stdout. `list` and `export` output the full data file. `stats` shows a total count. All actions are also logged to `history.log` for auditing. Redirect output with standard shell operators: `note-taker list > tasks.txt`.

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

```bash
note-taker add "Review pull request for auth module"
# ...
note-taker add "Prepare slides for Friday meeting"
# ...
note-taker list
# ...
note-taker done "Review pull request for auth module"
# ...
note-taker priority "Prepare slides for Friday meeting" high
# ...
note-taker today
# ...
note-taker remind "Submit expense report" "Friday 5pm"
# ...
note-taker stats
# ...
note-taker export > backup.txt
```

## 常见问题

### Q1: 如何开始使用Note Taker？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

