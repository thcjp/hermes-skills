---
slug: grok-image-generate
name: grok-image-generate
version: "1.0.0"
displayName: grok_image_generate
summary: 通过 Grok Imagine 生成用户描述的图片，并指导保存及发送至飞书的完整流程。
license: MIT-0
description: |-
  通过 Grok Imagine 生成用户描述的图片，并指导保存及发送至飞书的完整流程。

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 并指导保存及, imagine, generate, grok_image_generate, 生成用户描述, 的图片, 发送至飞书的, grok
tags:
- Creative
tools:
- read
- exec
---

# grok_image_generate

使用 Grok Imagine 生成图片的技能。

## 触发条件

用户要求：

* "用 Grok 生成图片"
* "生成一张图片"
* "帮我画个图"
* "生成 xxx 图片"

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

等待页面加载后，在输入框中输入提示词，然后点击提交按钮生成图片。

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

等待图片生成完成（约 8-10 秒）。

### 3. 获取图片并下载

图片生成后，需要保存到本地。有两种方式：

#### 方式一：使用 Desktop Control 技能保存（推荐）

使用 `desktop-control` 技能通过鼠标操作保存图片：

**步骤1：移动鼠标到图片上并右键点击**

```bash
uvx desktop-agent screen size

uvx desktop-agent mouse move <x> <y>

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

// 然后发送
message({
  action: "send",
  filePath: "/Users/xiaohuozi/.skill-platform/workspace/images/描述.jpg",
  message: "图片描述"
})
```

## 飞书发送图片正确姿势

1. 将图片保存到 `~/.skill-platform/workspace/images/` 目录
2. 使用 message 工具直接发送图片
3. 工具会自动处理图片上传和发送

## 保存路径建议

* 推荐保存到 `~/.skill-platform/workspace/images/` 目录
* 文件名建议：`描述关键词.jpg` 或带时间戳：`peacock_king.jpg`
* 如果需要发送到飞书，直接使用该路径即可

## 注意事项

* Grok Imagine 免费用户可能有生成次数限制
* 生成的图片是 AI 生成的，可能需要等待加载
* 如果页面元素有变化，需要根据实际情况调整 DOM 选择器

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
