---
slug: "grok-image-generate"
name: "grok-image-generate"
version: 1.0.1
displayName: "grok_image_generate"
summary: "通过 Grok Imagine 生成用户描述的图片，并指导保存及发送至飞书的完整流程。。通过 Grok Imagine 生成用户描述的图片，并指导保存及发送至飞书的完整流程。核心能力: -"
license: "Proprietary"
description: |-
  通过 Grok Imagine 生成用户描述的图片，并指导保存及发送至飞书的完整流程。核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Creative
  - 图像处理
  - AI绘图
  - 创意
  - uvx
  - desktop-agent
  - grok
  - imagine
  - action
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Creative"
---
# grok_image_generate

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| grok_image_generate并指导保存及发送 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |

## 核心能力

- 通过 Grok Imagine 生成用户描述的图片，并指导保存及发送至飞书的完整流程
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 内容生成 | 提示词与风格参数 | 生成内容与质量评分 |
| 图片生成 | 提示词与尺寸参数 | 图片文件与分辨率 |
| 通过 Grok Im | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 1. 打开 Grok Imagine 页面

```javascript
// 使用 browser 工具打开 Grok Imagine 页面
playwright({
  action: "open",
  profile: "skill-platform",
  url: "https://grok.com/imagine"
})
```

### 2. 输入提示词并生成

等待页面加载后，在输入框中输入提示词，然后点击提交按钮生成图片.
```javascript
// 输入提示词
playwright({
  action: "act",
  request: { "kind": "type", "ref": "输入框ref", "text": "用户想要生成的内容" }
})
// ...
// 点击提交按钮
playwright({
  action: "act",
  request: { "kind": "click", "ref": "提交按钮ref" }
})
```

等待图片生成完成（约 8-10 秒）.
### 3. 获取图片并下载

图片生成后，需要保存到本地。有两种方式：

#### 方式一：使用 Desktop Control 技能保存（推荐）

使用 `desktop-control` 技能通过鼠标操作保存图片：

**步骤1：移动鼠标到图片上并右键点击**

```bash
uvx desktop-agent screen size
# ...
uvx desktop-agent mouse move <x> <y>
# ...
uvx desktop-agent mouse right-click
```

**步骤2：选择"图片另存为"**

```bash
uvx desktop-agent keyboard press down --presses 2
uvx desktop-agent keyboard press return
```

**步骤3：点击存储**

```bash
uvx desktop-agent keyboard press return
```

**完整示例：**

```bash
uvx desktop-agent mouse move 720 400
uvx desktop-agent mouse right-click
sleep 1
uvx desktop-agent keyboard press down --presses 2
uvx desktop-agent keyboard press return
sleep 1
uvx desktop-agent keyboard press return
```

**步骤4：找到保存的图片**

```bash
ls -lat ~/Downloads/ | head -10
```

### 4. 发送图片到飞书

图片保存到本地后，可以使用 message 工具发送到飞书：

**方式一：从下载目录发送**

```bash
ls -lat ~/Downloads/*.jpg | head -5
# ...
message({
  action: "send",
  filePath: "/Users/xiaohuozi/Downloads/图片文件名.jpg",
  message: "图片描述"
})
```

**方式二：从图片目录发送（如果是截图）**

```javascript
// 先复制到图片目录
cp ~/Downloads/图片文件名.jpg ~/.skill-platform/workspace/images/描述.jpg
// ...
// 然后发送
message({
  action: "send",
  filePath: "/Users/xiaohuozi/.skill-platform/workspace/images/描述.jpg",
  message: "图片描述"
})
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | grok-image-generate处理的内容输入 |,  |
| content | string | 否 | grok-image-generate处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "generate 相关配置参数",
    result: "generate 相关配置参数",
    result: "generate 相关配置参数",
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
### 1. 打开 Grok Imagine 页面(补充)
# ...
```javascript
// 使用 browser 工具打开 Grok Imagine 页面
playwright({
  action: "open",
  profile: "skill-platform",
  url: "https://grok.com/imagine"
})
```
# ...
### 2. 输入提示词并生成(补充)
# ...
等待页面加载后，在输入框中输入提示词，然后点击提交按钮生成图片.
# ...
```javascript
// 输入提示词
playwright({
  action: "act",
  request: { "kind": "type", "ref": "输入框ref", "text": "用户想要生成的内容" }
})

// 点击提交按钮
playwright({
  action: "act",
  request: { "kind": "click", "ref": "提交按钮ref" }
})
```
# ...
等待图片生成完成（约 8-10 秒）.
# ...
### 3. 获取图片并下载(补充)
# ...
图片生成后，需要保存到本
```

## 常见问题

### Q1: 如何开始使用grok_image_generate？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

* Grok Imagine 免费用户可能有生成次数限制
* 生成的图片是 AI 生成的，可能需要等待加载
* 如果页面元素有变化，需要根据实际情况调整 DOM 选择器
