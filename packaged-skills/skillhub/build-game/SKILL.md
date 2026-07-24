---
slug: "build-game"
name: "build-game"
version: 1.2.1
displayName: "3D Game Builder"
summary: "自然语言生成并迭代精修3D浏览器游戏,任意类型即说即得。Generate and iteratively develop polished 3D browser games from nat"
license: "Proprietary"
description: |-
  Generate and iteratively develop polished 3D browser games from natural
  language。Supports any ge。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求.
tags:
  - Lifestyle
  - UI设计
  - 前端
  - 设计
  - game
  - 不支持
  - agent
  - api
  - 依赖说明
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Creative"
---
# 3D Game Builder

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 3D Game Builder自然语言生成 | 不支持 | 支持 |
| 多标签页并行抓取 | 不支持 | 支持 |
| 反爬虫策略自动绕过 | 不支持 | 支持 |
| 页面结构变化自适应 | 不支持 | 支持 |
| 批量导出结构化数据 | 不支持 | 支持 |

## 核心能力

- Generate and iteratively develop polished 3D browser games from natural
  language
- Supports any ge
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 场景1: 自然语言生成并迭代精修3D浏览器游戏 | 用户请求数据 | 结构化处理结果 |
| 场景2: 任意类型即说即得 | 用户请求数据 | 结构化处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. **初始化浏览器会话**: 启动无头浏览器实例,配置代理与用户代理参数
2. **执行页面交互**: 按照用户指令进行导航/点击/输入/提取等页面操作
3. **采集与返回数据**: 提取页面内容或操作结果,返回结构化数据与截图
4. **异常处理**: 如遇错误,参考错误处理章节中对应场景的处理方式

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | build-game处理的内容输入 |,  |
| content | string | 否 | build-game处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "game 相关配置参数",
    result: "game 相关配置参数",
    result: "game 相关配置参数",
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

### 第三方依赖
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

### "Make the main character a raccoon and enemies are tigers on a snow mountain"
→ Change player asset factory to raccoon model, create tiger enemy factory, swap environment to snow biome (white ground, pine trees with snow caps, snow particles, blue-white fog, ice rocks)

### "Add a Pokemon-style catching system"
→ Add creature database, capture mechanic (weaken + throw), creature storage, party system, turn-based battles with type effectiveness. See reference/game-systems.md.

### "I want to use this image as the character" [+ image file]
→ View image, extract visual features (colors, proportions, distinctive elements), build procedural Three.js model matching those features. Note: explain to user that the model will be a low-poly interpretation.

### "Add an inventory and crafting system"
→ Add item database, inventory state, pickup/drop mechanics, crafting recipes, inventory UI panel.

### "Make it multiplayer"
→ Not supported in single-file mode. Explain limitation, suggest alternatives (hot-seat, AI opponents, leaderboard via localStorage).

## 常见问题

### Q1: 如何开始使用3D Game Builder？
A: 

## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

