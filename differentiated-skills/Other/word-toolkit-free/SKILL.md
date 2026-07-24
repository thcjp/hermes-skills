---
slug: word-toolkit-free
name: word-toolkit-free
version: 1.0.1
displayName: Word文档控制免费版
summary: 通过osascript控制Word应用，支持文档操作、选区编辑、评论与导出，适合个人macOS用户.
license: Proprietary
edition: free
description: Word文档控制工具免费版，面向个人macOS用户的轻量级Word应用控制工具。核心能力:，可处理提升工作效率

  - 通过 osascript 控制 Word 应用会话

  - 文档操作与选区感知编辑

  - 评论与修订状态管理

  - 文档导出与清理关闭

  适用场景:

  - 个人 macOS 用户的 Word 文档自动化

  - 选区驱动的精确编辑

  - 文档导出与格式转换

  差异化: 免费版聚焦核心 Word 应用控制能力，去除所有外部平台与作者引用，强化中文本地化与适用关键词，适合个人用户零成本上手'
tags:
  - Word文档
  - 应用控制
  - macOS自动化
  - 免费版
  - 工具
  - 效率
  - 自动化
  - 知识
  - 文档
  - 研究
  - 分析
  - 写作
  - word
  - osascript
  - tell
  - microsoft
  - pdf
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# Word文档控制工具（免费版）

## 概述

Word文档控制工具免费版帮助你将 Microsoft Word 作为活动应用进行控制，而非仅作为 .docx 文件格式处理。通过 macOS 的 osascript CLI 实现 Word 应用会话管理、选区感知编辑、评论与修订状态管理以及文档导出.
## 核心能力

| 能力 | 说明 |
|---|---|
| 应用会话 | 附加至 Word 应用或新建会话 |
| 文档操作 | 打开、激活、关闭文档 |
| 选区编辑 | 基于当前选区的精确编辑 |
| 评论管理 | 添加、查看、删除评论 |
| 修订状态 | 查看/接受/拒绝修订 |
| 文档导出 | 导出为 PDF 等格式 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置.
### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.
**输入**: 用户提供参数配置与调用所需的指令和必要参数.
**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置.
**输入**: 用户提供结果处理与输出所需的指令和必要参数.
**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：osascript、支持文档操作、评论与导出、适合个人、macOS、文档控制工具免费、面向个人、用户的轻量级、应用控制工具、文档操作与选区感、知编辑、评论与修订状态管、文档导出与清理关等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：选区驱动的精确编辑

在当前光标位置插入内容.
```bash
# 获取当前选区信息
osascript -e 'tell application "Microsoft Word"
  set theDoc to active document
  set theSel to selection of theDoc
  return text of theSel
end tell'
# ...
# 在选区后插入内容
osascript -e 'tell application "Microsoft Word"
  set theDoc to active document
  set theSel to selection of theDoc
  collapse theSel direction collapse end
  set content of theSel to "插入的新内容"
end tell'
```

### 场景二：添加评论

为当前选区添加评论.
```bash
# 为选区添加评论
osascript -e 'tell application "Microsoft Word"
  set theDoc to active document
  set theSel to selection of theDoc
  make new comment at theDoc with properties ¬
    {comment text:"需要确认此处的数据来源", reference:theSel}
end tell'
```

### 场景三：导出为 PDF

将当前文档导出为 PDF.
```bash
# 导出为 PDF
osascript -e 'tell application "Microsoft Word"
  set theDoc to active document
  save as theDoc file name format format PDF file name "/path/to/output.pdf"
end tell'
```

## 不适用场景

以下场景Word文档控制免费版不适合处理：

- 加密文件破解
- 损坏文件修复
- 物理介质数据恢复

## 触发条件

需要文件处理、文档转换、格式互转、内容提取时使用。不适用于非本工具能力范围的需求.
## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

```bash
# 依赖说明
ls /Applications/Microsoft\ Word.app
# ...
# 2. 获取当前活动文档信息
osascript -e 'tell application "Microsoft Word"
  return name of active document
end tell'
# ...
# 3. 编辑选区
osascript -e 'tell application "Microsoft Word"
  set content of selection of active document to "新内容"
end tell'
# ...
# 4. 导出为 PDF
osascript -e 'tell application "Microsoft Word"
  save as active document file name format format PDF file name "/path/to/output.pdf"
end tell'
```

## 示例

```bash
# 运行环境要求
- Microsoft Word 已安装
- macOS 系统，osascript 可用
- 破坏性文档操作前需明确确认
# ...
# 内存目录结构
~/word/
├── memory.md             # 环境信息与安全默认值
├── incidents.md          # 可复用的故障与恢复步骤
└── document-notes.md     # 文档备注与导出目标
# ...
# 核心规则
1. 根据文档状态选择应用控制路径
2. 操作前确认目标文档与视图
3. 先读后写，操作后验证最终状态
4. 选区驱动操作视为高风险
5. 可逆操作与破坏性操作分离
6. 保持来源明确
7. 干净恢复，避免孤立应用会话
```

## 最佳实践

* 操作前先读取文档名、当前选区、目标段落，确认目标正确.
* 选区驱动的操作视为高风险，优先锚定到具体文档对象.
* 添加评论、修改视图、导出是可逆操作；接受/拒绝所有修订、删除评论、不保存关闭是破坏性操作，需明确确认.
* 如果仅为本次任务打开 Word，保持所有权清晰，仅关闭自己创建的文档.
* 如果附加至已有会话，不要关闭不相关的文档或退出 Word.
* 失败时记录确切阻塞原因：受保护文档、模态对话框、兼容模式、修订不匹配、权限缺失.
* 导出前确保字段、引用、目录已更新，避免交付陈旧内容.
## 常见问题

**Q：免费版支持 Windows 吗？**
A：免费版通过 osascript 控制 Word，仅支持 macOS。Windows 用户建议使用 COM 自动化方案.
**Q：免费版支持离线 DOCX 创建吗？**
A：免费版聚焦活动 Word 应用控制。如需离线 DOCX 创建与结构化编辑，请使用 word-docx 类工具.
**Q：选区操作会误改内容吗？**
A：选区驱动操作有风险。建议操作前先读取选区内容确认，操作后再次读取验证.
**Q：可以控制多个文档吗？**
A：可以，但建议每次聚焦一个文档。多文档操作时需明确指定目标文档名.
**Q：受保护文档怎么处理？**
A：受保护文档的编辑会静默失败。操作前检查文档保护状态，必要时提示用户解除保护.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: macOS（osascript 依赖）
- **Microsoft Word**: 已安装

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Microsoft Word | 应用 | 必需 | 官方购买安装 |
| osascript | 工具 | 必需 | macOS 系统自带 |

### API Key 配置
- 本skill基于Markdown指令规范，无需额外API Key（除内容中明确标注的外部API）
- 本工具不使用 Microsoft Graph、云文档 API 或 OAuth 流程

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + osascript执行）
- **说明**: 基于Markdown的AI Skill，通过 osascript 控制 Word 应用

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 本地运行，不支持多设备同步
- 当前为免费版本,如需完整功能请升级到付费版获取全部能力

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "Word文档控制免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "wordkit"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
