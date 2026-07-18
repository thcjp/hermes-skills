---
slug: feishu-card-builder-free
name: feishu-card-builder-free
version: "1.0.0"
displayName: 飞书卡片免费版
summary: 飞书富文本卡片消息构建工具，支持Markdown与按钮交互
license: MIT
edition: free
description: |-
  飞书卡片免费版是一款面向个人用户的飞书卡片消息构建与发送工具，支持向飞书用户或
  群组发送包含 Markdown、标题、彩色头部、按钮与图片的富交互卡片消息，提供安全发送
  机制避免特殊字符转义问题。

  核心能力:
  - 飞书卡片消息发送（用户/群组）
  - Markdown 内容渲染（代码块、表格、列表）
  - 卡片标题与彩色头部（蓝/红/橙/绿/紫/灰）
  - 底部按钮交互（文本+链接）
  - 本地图片上传与嵌入
  - 安全发送模式（自动临时文件处理）
  - 多种消息风格（Persona 人设消息）

  适用场景:
  - 个人用户发送富文本通知
  - 代码片段与日志格式化展示
  - 带操作按钮的引导消息
  - 独立开发者与一人公司效率提升

  差异化: 免费版聚焦个人卡片消息发送，提供安全发送机制解决特殊字符转义问题，操作
  简单直观。专业版在此基础上增加批量推送、卡片模板系统、高级交互组件与企业级特性。

  触发关键词: 飞书卡片, 飞书消息, 卡片消息, Markdown卡片, 交互按钮, 富文本消息, Lark卡片, 飞书通知
tags:
- 沟通协作
- 飞书
- 卡片消息
- 个人效率
tools:
- read
- exec
---

# 飞书卡片免费版

**版本**: 1.0.0
**适用对象**: 个人用户、独立开发者、一人公司
**核心定位**: 飞书富文本卡片消息构建与发送基础工具

---

## 概述

飞书卡片免费版是一款帮助个人用户向飞书（Lark）用户或群组发送富交互卡片消息的工具。支持在卡片中渲染 Markdown 内容（代码块、表格、列表）、设置标题与彩色头部、添加底部操作按钮以及嵌入本地图片，让消息展示更加丰富专业。

工具特别解决了命令行环境下特殊字符（如反引号）被 shell 吞掉的常见问题，提供安全发送模式通过临时文件自动处理内容传递，确保 Markdown 代码块等内容完整传递。同时支持多种消息风格（Persona），可按不同场景选择合适的展示样式。免费版聚焦个人用户的卡片消息发送需求，配置简洁、使用便捷。

---

## 核心能力

### 卡片消息发送

- **目标对象**: 支持用户 Open ID（`ou_...`）与群组 Chat ID（`oc_...`）
- **简单文本**: 直接发送纯文本内容
- **文件内容**: 从文件读取内容发送（推荐，支持完整 Markdown）

### Markdown 渲染

- 代码块（支持语法高亮）
- 表格
- 有序/无序列表
- 加粗、斜体、行内代码
- 链接

### 卡片样式

- **标题**: 自定义卡片头部标题
- **彩色头部**: 蓝/红/橙/绿/紫/灰六种颜色
- **底部按钮**: 文本按钮 + 跳转链接

### 图片支持

- 本地图片上传
- 图片嵌入卡片
- 自动获取 image_key

### 安全发送

- 自动创建临时文件处理特殊字符
- 自动清理临时文件
- 避免反引号等字符被 shell 吞掉

### 人设消息

- 多种消息风格切换
- 自动添加主题化头部与格式
- 不同场景适用不同风格

---

## 使用场景

### 场景一：发送代码片段通知

向开发群发送包含代码块的技术通知。

```bash
# 将内容写入临时文件（避免反引号被吞）
write temp/msg.md "代码审查通知：
\`\`\`js
function greet(name) {
  console.log('Hello, ' + name);
}
\`\`\`
请各位review以上代码。"

# 使用文件发送卡片
node skills/feishu-card-builder/send.js \
  --target "oc_xxxxxxx" \
  --text-file "temp/msg.md" \
  --title "代码审查通知" \
  --color blue
```

### 场景二：发送带按钮的引导消息

向用户发送带操作按钮的引导卡片。

```bash
# 安全发送带按钮的卡片
node skills/feishu-card-builder/send_safe.js \
  --target "ou_xxxxxxx" \
  --text "您的报告已生成，请点击下方按钮查看。" \
  --title "报告生成完成" \
  --color green \
  --button-text "查看报告" \
  --button-url "https://example.com/report/123"
```

### 场景三：发送带图片的展示卡片

上传本地图片并发送带图片的展示卡片。

```bash
# 发送带图片的卡片
node skills/feishu-card-builder/send.js \
  --target "oc_xxxxxxx" \
  --text "本周数据图表如下：" \
  --title "周报数据" \
  --color orange \
  --image-path "charts/weekly_chart.png"
```

---

## 快速开始

### 第一步：安装依赖

本工具依赖 `feishu-common` 模块提供 Token 与 API 认证：

```bash
# 确保已安装 feishu-common
# 配置飞书应用凭证（app_id 与 app_secret）
```

### 第二步：发送简单文本卡片

```bash
# 发送简单文本
node skills/feishu-card-builder/send.js --target "ou_xxxxxxx" --text "Hello World"
```

### 第三步：发送 Markdown 卡片（推荐）

对于包含特殊字符的内容，始终使用文件方式发送：

```bash
# 写入内容到文件
write temp/msg.md "这里有一些代码：
\`\`\`python
print('hello')
\`\`\`"

# 使用文件发送
node skills/feishu-card-builder/send.js --target "ou_xxxxxxx" --text-file "temp/msg.md"
```

### 第四步：使用安全发送模式

```bash
# 安全发送（自动处理临时文件）
node skills/feishu-card-builder/send_safe.js \
  --target "ou_xxxxxxx" \
  --text "包含 \`反引号\` 和 *markdown* 的内容" \
  --title "安全消息"
```

---

## 配置示例

### 命令参数说明

| 参数 | 说明 | 示例 |
|:-----|:-----|:-----|
| `-t, --target` | 目标 ID（用户 ou_ 或群组 oc_） | `--target "ou_xxxxxxx"` |
| `-x, --text` | 简单文本内容 | `--text "Hello"` |
| `-f, --text-file` | 文本文件路径（支持 Markdown） | `--text-file "msg.md"` |
| `--title` | 卡片标题 | `--title "通知"` |
| `--color` | 头部颜色 | `--color blue` |
| `--button-text` | 按钮文本 | `--button-text "查看"` |
| `--button-url` | 按钮链接 | `--button-url "https://..."` |
| `--image-path` | 本地图片路径 | `--image-path "img.png"` |

### 头部颜色选项

| 颜色 | 适用场景 |
|:-----|:---------|
| blue（默认） | 普通通知、信息分享 |
| red | 紧急告警、错误通知 |
| orange | 警告提醒、注意事项 |
| green | 成功通知、完成提示 |
| purple | 特殊标识、创意内容 |
| grey | 系统消息、辅助信息 |

### 人设消息风格

```bash
# 使用不同人设发送
node skills/feishu-card-builder/send_persona.js \
  --target "ou_xxxxxxx" \
  --persona "d-guide" \
  --text "检测到严重错误。"
```

| 人设 | 风格说明 |
|:-----|:---------|
| d-guide | 红色警告头部，加粗/代码前缀 |
| green-tea | 胭脂色头部，柔和可爱风格 |
| mad-dog | 灰色头部，原始运行时错误风格 |
| default | 标准蓝色头部 |

---

## 最佳实践

### 内容传递安全

**核心原则**: 包含特殊字符（反引号、星号等）的内容，始终使用文件方式发送。

```bash
# 错误做法：直接用 --text 传递含反引号的内容
# node send.js --text "代码: `code`"  # 反引号会被 shell 吞掉

# 正确做法1：写入文件后用 --text-file 发送
write temp/msg.md "代码: \`code\`"
node skills/feishu-card-builder/send.js --target "ou_xxx" --text-file "temp/msg.md"

# 正确做法2：使用 send_safe.js 自动处理
node skills/feishu-card-builder/send_safe.js --target "ou_xxx" --text "代码: \`code\`"
```

### Markdown 内容组织

```bash
# 结构化 Markdown 内容
write temp/report.md "## 本周进展

### 已完成
- 功能A开发完成
- Bug修复12个

### 进行中
- 性能优化

\`\`\`bash
# 部署命令
npm run deploy
\`\`\`"

node skills/feishu-card-builder/send.js \
  --target "oc_xxx" \
  --text-file "temp/report.md" \
  --title "周报" \
  --color blue
```

### 按钮设计

- 按钮文本简洁明确（不超过10个字）
- 链接确保有效可访问
- 一个卡片建议不超过2个按钮

### 图片使用

```bash
# 确保图片大小合理（建议不超过1MB）
ls -lh chart.png

# 发送带图片的卡片
node skills/feishu-card-builder/send.js \
  --target "oc_xxx" \
  --text "数据图表" \
  --image-path "chart.png" \
  --title "数据展示" \
  --color green
```

---

## 常见问题

### 问题1：Markdown 反引号被吞掉

```text
发送的代码块显示不完整，反引号丢失
```

**原因**: Shell 会解析反引号作为命令替换。

**解决**: 使用文件方式或安全发送模式：

```bash
# 使用文件方式
write temp/msg.md "代码: \`code\`"
node skills/feishu-card-builder/send.js --target "ou_xxx" --text-file "temp/msg.md"

# 或使用安全发送
node skills/feishu-card-builder/send_safe.js --target "ou_xxx" --text "代码: \`code\`"
```

### 问题2：图片上传失败

**解决**: 检查图片路径与格式：

```bash
# 确认文件存在
ls -la path/to/image.png

# 确认格式支持（PNG/JPG）
file image.png
```

### 问题3：消息发送失败，提示认证错误

**解决**: 检查 feishu-common 配置：

```bash
# 确认 app_id 与 app_secret 配置正确
# 确认应用有发送消息权限
# 确认 target ID 正确（ou_ 开头为用户，oc_ 开头为群组）
```

### 问题4：按钮链接无法跳转

**解决**: 确保链接格式正确且可访问：

```bash
# 使用完整 URL
--button-url "https://example.com/page"

# 确认链接可访问
curl -I https://example.com/page
```

### 问题5：长内容被截断

**解决**: 飞书卡片有内容长度限制，超长内容建议拆分发送或使用文件附件：

```bash
# 拆分长内容
write temp/part1.md "第一部分内容..."
write temp/part2.md "第二部分内容..."

node send.js --target "oc_xxx" --text-file "temp/part1.md" --title "报告 (1/2)"
node send.js --target "oc_xxx" --text-file "temp/part2.md" --title "报告 (2/2)"
```

---

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js版本**: 16 及以上
- **网络环境**: 需可访问飞书开放平台 API

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需 | 官方网站下载安装 |
| feishu-common | 模块 | 必需 | 飞书通用认证模块 |
| 飞书应用 | 应用 | 必需 | 飞书开放平台创建应用 |
| app_id/app_secret | 凭证 | 必需 | 飞书应用配置页获取 |

### API Key 配置

- 本工具通过飞书应用凭证（app_id 与 app_secret）进行认证
- 凭证由 feishu-common 模块统一管理
- 无需额外 API Key
- 应用需在飞书开放平台开通消息发送权限

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，部分功能需要 exec 命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行 Node.js 脚本，完成飞书卡片消息的构建与发送
