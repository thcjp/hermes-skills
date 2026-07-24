---
slug: "use-my-browser-free"
name: "use-my-browser-free"
version: 1.0.1
displayName: "浏览器控制工具(免费版)"
summary: "控制用户Chrome浏览器进行页面读取、导航、表单填充和数据提取(免费版)。控制用户Chrome浏览器进行页面读取、导航、表单填充和数据提取。通过浏览器扩展 桥接，直接操作用户已登录的浏览器"
license: "MIT"
description: |-
  控制用户Chrome浏览器进行页面读取、导航、表单填充和数据提取。通过浏览器扩展
  桥接，直接操作用户已登录的浏览器会话，无需重新认证。支持页面文本提取、
  元素查找、JavaScript执行、截图和标签页管理。适用于独立开发者、企业团队
  和自动化工作流场景。不适用于无头浏览器或远程浏览器场景.
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
tags:
  - 通用办公
  - 工具
  - 效率
  - 自动化
  - 研究
  - 分析
  - AI代理
  - agent
  - 开发
  - json
  - url
  - tmwd_text
  - tmwd_elements
  - max_chars
category: "Automation"
---
# 浏览器控制工具(免费版)

控制用户Chrome浏览器进行页面读取、导航、表单填充和数据提取.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 浏览器控制工具(免费版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 核心能力

### 1. 浏览器状态检查
通过 `tmwd_status` 检查浏览器连接状态，确认是否有已连接的标签页.
```json
{"tool": "tmwd_status"}
```

**输入**: 用户提供浏览器状态检查所需的指令和必要参数.
**输出**: 返回浏览器状态检查的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 页面导航
通过 `tmwd_navigate` 导航到指定URL，支持等待页面加载完成.
```json
{"tool": "tmwd_navigate", "url": "https://example.com", "wait": "load"}}
```

**输入**: 用户提供页面导航所需的指令和必要参数.
**处理**: 解析页面导航的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回页面导航的处理结果,包含执行状态码、结果数据和执行日志.
### 3. 页面文本提取
通过 `tmwd_text` 提取页面文本内容，`max_chars` 参数限制提取长度（默认5000）.
```json
{"tool": "tmwd_text", "max_chars": 5000}}
```

**处理**: 解析页面文本提取的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回页面文本提取的处理结果,包含执行状态码、结果数据和执行日志.
### 4. 元素查找与交互
通过 `tmwd_elements` 查找页面元素，支持CSS选择器和XPath.
```json
{"tool": "tmwd_elements", "selector": "#search-input", "action": "click"}}
```

**处理**: 解析元素查找与交互的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回元素查找与交互的处理结果,包含执行状态码、结果数据和执行日志.
### 输出格式

完成响应以Markdown格式返回,包含任务状态(成功/失败)、解析摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。- 验证返回数据的完整性和格式正确性
- 参考`输出格式`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 页面读取 | URL | 页面文本内容 |
| 表单填充 | 表单选择器+数据 | 填充结果 |
| 数据提取 | CSS选择器 | 元素内容 |

## 使用流程

1. 检查连接状态: 调用 `tmwd_status` 确认浏览器已连接(指示灯为绿色)
2. 导航或操作: 使用 `tmwd_navigate` 导航到目标页面
3. 提取数据: 使用 `tmwd_text` 或 `tmwd_elements` 提取所需数据
4. 验证结果: 通过 `tmwd_exec` 执行验证脚本确认操作成功

## 示例

### 示例:导航并提取文本

```json
{"tool": "tmwd_navigate", "url": "https://news.example.com", "wait": "load"}
```

输出：
```json
{
  "success": true,
  "url": "https://news.example.com",
  "title": "今日新闻",
  "load_time": 1234
}
```

```json
{"tool": "tmwd_text", "max_chars": 5000}
```

输出：
```json
{
  "text": "今日新闻\n头条：科技行业最新动态...\n正文内容...",
  "chars": 3420,
  "truncated": false
}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 无已连接标签页 | 浏览器扩展未安装或未激活 | 安装浏览器扩展，确保Chrome正在运行且扩展已启用 |
| 指示灯为红色 | 扩展与桥接服务断开 | 点击扩展图标重新连接，检查桥接服务是否运行 |
| CSP策略阻止脚本执行 | 网站内容安全策略限制 | 使用 `tmwd_elements` 替代 `tmwd_exec`，或联系网站管理员 |
| 点击元素无效果 | 元素被遮挡或不可见 | 检查元素 `visible` 属性，先滚动到元素位置再点击 |

## 常见问题

### Q1: 如何确认浏览器已连接？
A: 调用 `tmwd_status`，检查 `connected` 是否为 `true` 且 `indicator` 为 `green`。如果为 `false` 或 `red`，说明扩展未连接.
### Q2: `tmwd_text` 的 `max_chars` 参数有什么限制？
A: 默认值为5000字符。如果页面文本超过5000字符，`truncated` 字段为 `true`。需要完整文本时，分多次提取或使用 `tmwd_elements` 精确定位特定区域.
### Q3: 为什么 `tmwd_exec` 在某些网站上失败？
A: 部分网站设置了严格的CSP（内容安全策略），阻止在页面上下文中执行JavaScript。此时改用 `tmwd_elements` 的 `action` 参数（如 `click`、`type`）替代脚本执行.
## 已知限制

- 需要安装浏览器扩展并保持Chrome运行
- 指示灯为红色时无法操作，需重新连接
- `tmwd_text` 的 `max_chars` 默认5000字符

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

## 升级提示

本免费版提供基础功能。升级到完整版 use-my-browser 获取全部能力和高级特性.