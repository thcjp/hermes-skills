---
slug: "feishu-card"
name: "feishu-card"
version: 1.4.12
displayName: "协作平台卡片"
summary: "发送富交互协作平台卡片，支持Markdown、标题、按钮、图片和人格化消息。向协作平台用户或群组发送富交互卡片。支持Markdown（代码块、表格）、标题、彩色头部、 按钮组件、图片嵌入和多"
license: "Proprietary"
description: |-
  向协作平台用户或群组发送富交互卡片。支持Markdown（代码块、表格）、标题、彩色头部、
  按钮组件、图片嵌入和多种AI人格化消息样式。适用于自动化通知、告警推送、
  团队协作和AI助手消息场景.
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 通用办公
  - 工具
  - 效率
  - 自动化
category: "Automation"
---
# 协作平台卡片

向协作平台用户或群组发送富交互卡片。支持Markdown（代码块、表格）、标题、彩色头部、按钮组件、图片嵌入和多种AI人格化消息样式.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 协作平台卡片处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |
| 消息频控与智能排队 | 不支持 | 支持 |

## 前置依赖

- 需先安装 `feishu-common` 依赖
- 本skill依赖 `../feishu-common/index.js` 进行Token和API认证

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 简单文本卡片
通过 `node skills/feishu-card/send.js --target "ou_..." --text "Hello World"` 发送简单文本卡片。`--target` 参数接受用户Open ID（`ou_` 前缀）或群组Chat ID（`oc_` 前缀）。适用于不含特殊字符的简单消息推送场景.
**输出**: 返回简单文本卡片的处理结果,包含执行状态码、结果数据和执行日志.
### 2. Markdown复杂卡片

通过 `--text-file` 参数从文件读取Markdown内容发送复杂卡片。支持代码块、表格、列表等完整Markdown语法。**关键**：为防止shell转义问题（如反引号被吞），始终先将内容写入临时文件，再用 `--text-file "temp/msg.md"` 发送。适用于发送代码片段、日志和格式化报告。- 验证返回数据的完整性和格式正确性
- 参考`Markdown复杂卡片`的配置文档进行参数调优
### 3. 安全发送

通过 `node skills/feishu-card/send_safe.js` 包装器安全发送原始文本。自动处理临时文件创建和清理，避免shell转义问题。支持 `--text` 直接传入含反引号和Markdown的内容，配合 `--title` 设置卡片标题。适用于自动化流程中的安全消息发送。- 验证返回数据的完整性和格式正确性
- 参考`安全发送`的配置文档进行参数调优
### 4. 卡片标题和颜色
通过 `--title <string>` 设置卡片头部标题，`--color <string>` 设置头部颜色。支持6种颜色：`blue`（默认）、`red`、`orange`、`green`、`purple`、`grey`。适用于按消息类型或紧急程度区分卡片视觉样式.
**输入**: 用户提供卡片标题和颜色所需的指令和必要参数.
**处理**: 解析卡片标题和颜色的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回卡片标题和颜色的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 按钮组件
通过 `--button-text <string>` 设置底部操作按钮文本，`--button-url <url>` 设置按钮跳转链接。卡片底部渲染可点击按钮，点击后跳转到指定URL。适用于消息内嵌操作入口，如"查看详情"、"立即处理"等交互场景.
**输入**: 用户提供按钮组件所需的指令和必要参数.
**输出**: 返回按钮组件的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`按钮组件`的配置文档进行参数调优
### 6. 图片嵌入

通过 `--image-path <path>` 上传本地图片并嵌入到卡片中。支持常见图片格式（PNG/JPG/GIF等）。图片先上传到协作平台服务器获取image_key，再嵌入到卡片内容中渲染。适用于发送截图、图表和视觉内容。- 验证返回数据的完整性和格式正确性
- 参考`图片嵌入`的配置文档进行参数调优
### 7. 人格化消息

通过 `node skills/feishu-card/send_persona.js --target "ou_..." --persona "d-guide" --text "Critical error detected."` 发送带主题样式的人格化消息。自动添加匹配的头部颜色、格式前缀和风格化后缀。适用于AI助手不同角色的消息输出场景。- 验证返回数据的完整性和格式正确性
- 参考`人格化消息`的配置文档进行参数调优
### 8. 多种人格样式
支持4种预设人格：`d-guide`（红色警告头部，粗体/代码前缀，讽刺后缀）、`green-tea`（胭脂红头部，柔软可爱风格）、`mad-dog`（灰色头部，原始运行时错误风格）、`default`（标准蓝色头部）。通过 `--persona <type>` 参数选择，`--text` 或 `--text-file` 提供内容。适用于不同场景和语气的消息表达.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用流程

1. 确认已安装 `feishu-common` 依赖，Token和API认证已配置
2. 获取目标ID：用户Open ID（`ou_` 前缀）或群组Chat ID（`oc_` 前缀）
3. 根据内容复杂度选择发送方式：简单文本用 `--text`，Markdown内容用 `--text-file`，含特殊字符用 `send_safe.js`
4. 按需配置 `--title`、`--color`、`--button-text`、`--button-url`、`--image-path` 等卡片元素
5. 如需人格化样式，使用 `send_persona.js` 并选择 `--persona` 类型
6. 执行发送命令并检查响应确认消息已送达

#
## 示例

### 示例1：发送带按钮的Markdown报告卡片

```bash
# 将Markdown内容写入临时文件
write temp/msg.md "# 周报\n\n| 指标 | 数值 |\n|------|------|\n| 任务完成 | 15 |\n| 待处理 | 3 |\n\n```js\nconsole.log('done');\n```"
# ...
# 发送带标题、颜色和按钮的卡片
node skills/feishu-card/send.js \
  --target "ou_abc123def456" \
  --text-file "temp/msg.md" \
  --title "本周工作周报" \
  --color green \
  --button-text "查看完整报告" \
  --button-url "https://reports.example.com/weekly"
```

### 示例2：使用人格化消息发送告警

```bash
# 使用d-guide人格发送严重错误告警
node skills/feishu-card/send_persona.js \
  --target "oc_group123456" \
  --persona "d-guide" \
  --text "服务API响应延迟超过5000ms，已触发自动降级。当前错误率: 12.3%"
# ...
# 使用green-tea人格发送日常提醒
node skills/feishu-card/send_persona.js \
  --target "ou_xyz789abc" \
  --persona "green-tea" \
  --text "今天的代码评审会议15分钟后开始哦~"
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| `--text` 中反引号消失 | Shell将反引号解释为命令替换 | 改用 `--text-file` 从文件读取内容，或使用 `send_safe.js` 包装器 |
| 目标ID格式错误 | 传入的ID不以 `ou_` 或 `oc_` 开头 | 确认Open ID格式为 `ou_` 前缀，群组Chat ID为 `oc_` 前缀 |
| 图片上传失败 | 图片路径不存在或格式不支持 | 确认 `--image-path` 指向有效图片文件（PNG/JPG/GIF），检查文件路径 |
| 颜色参数无效 | 传入了不在支持列表中的颜色 | 使用6种有效颜色之一：`blue`/`red`/`orange`/`green`/`purple`/`grey` |
| 依赖缺失 | 未安装 `feishu-common` | 先安装 `feishu-common`，确保 `../feishu-common/index.js` 可访问 |
| Markdown表格渲染异常 | 表格格式不符合Markdown规范 | 确保表格使用标准 `|---|---|` 分隔符，表头和数据行对齐 |
| 人格类型不存在 | `--persona` 传入了无效类型 | 使用4种有效人格之一：`d-guide`/`green-tea`/`mad-dog`/`default` |
| Token认证失败 | `feishu-common` Token过期或无效 | 检查 `feishu-common` 配置，重新获取有效的access_token |

## 常见问题

### Q1: 如何发送含代码块的Markdown内容？

先将Markdown内容写入临时文件（如 `temp/msg.md`），再使用 `--text-file "temp/msg.md"` 参数发送。**不要**直接在 `--text` 参数中传含反引号的代码块，Shell会将反引号解释为命令替换导致内容丢失.
### Q2: 为什么反引号消失了？

Shell将反引号（`` ` ``）解释为命令替换，导致代码块标记被吞掉。解决方案：使用 `--text-file` 从文件读取内容，或使用 `send_safe.js` 包装器自动处理临时文件创建和转义.
### Q3: 如何发送图片？

使用 `--image-path <path>` 参数指定本地图片路径。图片会先上传到协作平台服务器获取image_key，再嵌入卡片渲染。支持PNG、JPG、GIF等常见格式。确保文件路径正确且有读取权限.
### Q4: 支持哪些人格类型？

支持4种预设人格：`d-guide`（红色警告头部，粗体前缀，讽刺后缀）、`green-tea`（胭脂红头部，可爱风格）、`mad-dog`（灰色头部，运行时错误风格）、`default`（标准蓝色头部）。通过 `--persona <type>` 参数选择，使用 `send_persona.js` 脚本发送.
### Q5: Open ID和Group Chat ID有什么区别？

Open ID（`ou_` 前缀）标识单个用户，消息发送到该用户的私聊。Group Chat ID（`oc_` 前缀）标识群组，消息发送到群聊中所有成员。通过 `--target` 参数指定，两种ID均可用于所有发送方式.
### Q6: 如何设置卡片颜色？

使用 `--color <string>` 参数设置卡片头部颜色。支持6种颜色：`blue`（默认）、`red`、`orange`、`green`、`purple`、`grey`。不同颜色适用于不同场景：`red` 用于告警，`green` 用于成功，`orange` 用于警告，`grey` 用于普通通知.
## 已知限制

- 含特殊字符（反引号、$等）的内容必须使用 `--text-file` 或 `send_safe.js`
- 依赖 `feishu-common` 进行Token认证，需提前配置
- 图片上传依赖协作平台服务器，大图可能上传缓慢
- 人格化消息的样式由预设模板决定，暂不支持自定义

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "协作平台卡片处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "feishu-card"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
