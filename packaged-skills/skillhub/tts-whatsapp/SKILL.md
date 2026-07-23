---
slug: "tts-whatsapp"
name: "tts-whatsapp"
version: "1.0.0"
displayName: "TTS WhatsApp"
summary: "在WhatsApp发40+语言高质量TTS语音消息,自动送达"
license: "Proprietary"
description: |-
  Send high-quality text-to-speech voice messages on WhatsApp in 40+ languages
  with automatic delivery

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依...
tags:
  - Creative
  - Communication
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# TTS WhatsApp

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |
| 消息频控与智能排队 | 不支持 | 支持 |

## 核心能力

* 🎙️ **High-quality TTS** powered by Piper (40+ languages)
* 🎵 **Automatic conversion** to OGG/Opus (WhatsApp format)
* 📤 **Automatic sending** via SkillHub
* 👥 **Group support** - Send to individuals or WhatsApp groups
* 🌍 **Multi-language** - French, English, Spanish, German, and 40+ more
* 🧹 **Smart cleanup** - Auto-delete files after successful send
* ⚡ **Fast** - ~2-3s from command to delivery
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 质量检查 | 代码库与标准配置 | 问题列表与修复建议 |
| 消息发送 | 目标与消息内容 | 送达回执与消息ID |
| 在WhatsApp发 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Basic usage

```bash
tts-whatsapp "Hello, this is a test" --target "+15555550123"
```

### Send to WhatsApp group

```bash
tts-whatsapp "Hello everyone" --target "120363257357161211@g.us"
```

### Change language

```bash
tts-whatsapp "Hola mundo" --lang es_ES --voice carlfm --target "+34..."
```

### Different quality levels

```bash
tts-whatsapp "High quality" --quality high --target "+1..."
```

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | tts-whatsapp处理的内容输入 |,  |
| content | string | 否 | tts-whatsapp处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "whatsapp 相关配置参数",
    result: "whatsapp 相关配置参数",
    result: "whatsapp 相关配置参数",
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

### 示例1：基础用法

```
### Basic usage(补充)
# ...
```bash
tts-whatsapp "Hello, this is a test" --target "+15555550123"
```
# ...
### Send to WhatsApp group(补充)
# ...
```bash
tts-whatsapp "Hello everyone" --target "120363257357161211@g.us"
```
# ...
### Change language(补充)
# ...
```bash
tts-whatsapp "Hola mundo" --lang es_ES --voice carlfm --target "+34..."
```
# ...
### Different quality levels(补充)
# ...
```bash
tts-whatsapp "High quality" --quality high --target "+1..."
```
```

## 常见问题

### Q1: 如何开始使用TTS WhatsApp？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

