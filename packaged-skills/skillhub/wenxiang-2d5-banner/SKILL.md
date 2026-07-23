---
slug: "wenxiang-2d5-banner"
name: "wenxiang-2d5-banner"
version: "1.0.0"
displayName: "Wenxiang 2d5 Banner"
summary: "用Nano Banana Pro(Gemini 3 Pro Image)生成编辑图片"
license: "Proprietary"
description: |-
  Generate/edit images with Nano Banana Pro (Gemini 3 Pro Image)。Use\
  \ for image create/modify reque。Use when 用户需要Wenxiang 2d5 Banner相关功能时使用。不适用于超出本技能能力范围的复杂需求。
tags: "'[''Other'']'"
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# Wenxiang 2d5 Banner

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Generate/edit images with Nano Banana Pro (Gemini 3 Pro Image) | 支持 | 支持 |
| Use\ | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Generate/edit images with Nano Banana Pro (Gemini 3 Pro Image)
- Use\
  \ for image create/modify reque
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
| content | string | 否 | wenxiang-2d5-banner处理的内容输入 |,  |
| content | string | 否 | wenxiang-2d5-banner处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

* Saves PNG to current directory (or specified path if filename includes directory)
* Script outputs the full path to the generated image
* **Do not read the image back** - just inform the user of the saved path

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

**Generate new image:**

```bash
uv run ~/.codex/skills/nano-banana-pro/（请参考skill目录中的脚本文件） --prompt "A serene Japanese garden with cherry blossoms" --filename "2025-11-23-14-23-05-japanese-garden.png" --resolution 4K
```

**Edit existing image:**

```bash
uv run ~/.codex/skills/nano-banana-pro/（请参考skill目录中的脚本文件） --prompt "make the sky more dramatic with storm clouds" --filename "2025-11-23-14-25-30-dramatic-sky.png" --input-image "original-photo.jpg" --resolution 2K
```

## 常见问题

### Q1: 如何开始使用Wenxiang 2d5 Banner？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Wenxiang 2d5 Banner有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

