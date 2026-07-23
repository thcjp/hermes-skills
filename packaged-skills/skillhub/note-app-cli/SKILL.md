---
slug: "note-app-cli"
name: "note-app-cli"
version: "1.0.0"
displayName: "Obsidian Official Cl"
summary: "Obsidian管理技能,管笔记库(权限较广需谨慎)"
license: "Proprietary"
description: |-
  This skill matches its Obsidian-management purpose, but it gives an
  agent broad power to change, 。Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Integrations
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# Obsidian Official Cl

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

### Obsidian Sync
```bash
obsidian sync:status                   # Status and usage
obsidian sync on/off                   # Resume/pause
obsidian sync:history file=Note
obsidian sync:restore file=Note version=2
obsidian sync:deleted                  # Deleted files
```

**输入**: 用户提供Obsidian Sync所需的指令和必要参数。
**处理**: 按照skill规范执行Obsidian Sync操作,遵循单一意图原则。
**输出**: 返回Obsidian Sync的执行结果,包含操作状态和输出数据。### File History
```bash
obsidian history file=Note             # List versions
obsidian history:read file=Note version=1
obsidian history:restore file=Note version=2
obsidian diff file=Note from=2 to=1   # Compare versions
```

**处理**: 按照skill规范执行File History操作,遵循单一意图原则。
**输出**: 返回File History的执行结果,包含操作状态和输出数据。### Developer Tools
```bash
obsidian devtools                      # Toggle dev tools
obsidian dev:console                   # Show console
obsidian dev:errors                    # JS errors
obsidian eval code="app.vault.getFiles().length"

obsidian dev:screenshot path=screenshot.png
obsidian dev:dom selector=".workspace-leaf"
obsidian dev:css selector=".mod-active" prop=background

obsidian dev:mobile on/off
obsidian dev:debug on/off
```

**输入**: 用户提供Developer Tools所需的指令和必要参数。
**处理**: 按照skill规范执行Developer Tools操作,遵循单一意图原则。
**输出**: 返回Developer Tools的执行结果,包含操作状态和输出数据。
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | note-app-cli处理的内容输入 |,  |
| content | string | 否 | note-app-cli处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "cli 相关配置参数",
    result: "cli 相关配置参数",
    result: "cli 相关配置参数",
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
|---------|------|---------|
| 输入content为空 | 用户未提供必要信息 | 提示用户提供content, 并给出示例格式 |
| 输入内容过长(>5000字) | 超出单次处理能力 | 建议分段处理, 每段不超过2000字 |
| 风格参数不识别 | 传入不支持的风格 | 列出支持的风格选项, 使用默认风格 |
| 生成内容不达标 | 质量校验未通过 | 自动1次, 仍不达标则标注问题返回 |
| 其他异常 | 内部处理异常 | 检查输入后 |

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

## 常见问题

### Q1: 如何开始使用Obsidian Official Cl？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Obsidian Official Cl有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
