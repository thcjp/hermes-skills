---
slug: use-my-browser
name: use-my-browser
version: "2.0.0"
displayName: 浏览器控制工具
summary: 控制用户Chrome浏览器进行页面读取、导航、表单填充和数据提取
license: MIT-0
description: |-
  控制用户Chrome浏览器进行页面读取、导航、表单填充和数据提取。通过浏览器扩展
  桥接，直接操作用户已登录的浏览器会话，无需重新认证。支持页面文本提取、
  元素查找、JavaScript执行、截图和标签页管理。适用于独立开发者、企业团队
  和自动化工作流场景。不适用于无头浏览器或远程浏览器场景。
tools:
  - read
  - exec
---

# 浏览器控制工具

控制用户Chrome浏览器进行页面读取、导航、表单填充和数据提取。

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| Shell环境 (用于执行命令行操作) | 运行环境 | 是 | 见核心能力章节 |
| Git版本控制 | 运行环境 | 否 | 见核心能力章节 |

## 核心能力

### 1. 浏览器状态检查
通过 `tmwd_status` 检查浏览器连接状态，确认是否有已连接的标签页。

```json
{"tool": "tmwd_status"}
```

**输入**: 用户提供浏览器状态检查所需的指令和必要参数。
**输出**: 返回浏览器状态检查的执行结果,包含操作状态和输出数据。

### 2. 页面导航
通过 `tmwd_navigate` 导航到指定URL，支持等待页面加载完成。

```json
{"tool": "tmwd_navigate", "url": "https://example.com", "wait": "load"}}
```

**输入**: 用户提供页面导航所需的指令和必要参数。
**处理**: 按照skill规范执行页面导航操作,遵循单一意图原则。
**输出**: 返回页面导航的执行结果,包含操作状态和输出数据。

### 3. 页面文本提取
通过 `tmwd_text` 提取页面文本内容，`max_chars` 参数限制提取长度（默认5000）。

```json
{"tool": "tmwd_text", "max_chars": 5000}}
```

**处理**: 按照skill规范执行页面文本提取操作,遵循单一意图原则。
**输出**: 返回页面文本提取的执行结果,包含操作状态和输出数据。

### 4. 元素查找与交互
通过 `tmwd_elements` 查找页面元素，支持CSS选择器和XPath。

```json
{"tool": "tmwd_elements", "selector": "#search-input", "action": "click"}}
```

**处理**: 按照skill规范执行元素查找与交互操作,遵循单一意图原则。
**输出**: 返回元素查找与交互的执行结果,包含操作状态和输出数据。

### 5. JavaScript执行
通过 `tmwd_exec` 在页面上下文中执行JavaScript代码。

```json
{"tool": "tmwd_exec", "script": "document.title"}}
```

**输入**: 用户提供JavaScript执行所需的指令和必要参数。
**输出**: 返回JavaScript执行的执行结果,包含操作状态和输出数据。

### 6. 表单填充
自动查找表单字段并填充数据，支持输入框、下拉选择和复选框。

```json
{"tool": "tmwd_elements", "selector": "#username", "action": "type", "value": "testuser"}}
```

**处理**: 按照skill规范执行表单填充操作,遵循单一意图原则。
**输出**: 返回表单填充的执行结果,包含操作状态和输出数据。

### 7. 截图
对当前页面进行截图，保存为PNG文件。

```json
{"tool": "tmwd_exec", "script": "screenshot()"}}
```

### 8. 标签页管理
列出、切换和关闭浏览器标签页。

```json
{"tool": "tmwd_status", "action": "list_tabs"}}
```

**输入**: 用户提供标签页管理所需的指令和必要参数。
**处理**: 按照skill规范执行标签页管理操作,遵循单一意图原则。
**输出**: 返回标签页管理的执行结果,包含操作状态和输出数据。
## 使用流程

### 第一步：检查连接状态

始终先调用 `tmwd_status` 确认浏览器已连接。如果指示灯为红色，说明扩展未连接。

### 第二步：导航或操作

根据任务需要，使用 `tmwd_navigate` 导航到目标页面，或直接操作当前页面。

### 第三步：提取数据

使用 `tmwd_text` 或 `tmwd_elements` 提取所需数据。

### 第四步：验证结果

通过 `tmwd_exec` 执行验证脚本，确认操作成功。

## 真实示例

### 示例1：读取页面标题

```json
{"tool": "tmwd_status"}
```

输出：
```json
{
  "connected": true,
  "indicator": "green",
  "tabs": [
    {"id": "tab-1", "title": "Google", "url": "https://www.google.com"},
    {"id": "tab-2", "title": "GitHub", "url": "https://github.com"}
  ],
  "active_tab": "tab-1"
}
```

### 示例2：导航并提取文本

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

### 示例3：查找并点击元素

```json
{"tool": "tmwd_elements", "selector": ".search-button", "action": "click"}
```

输出：
```json
{
  "found": 1,
  "elements": [
    {"tag": "button", "class": "search-button", "text": "搜索", "visible": true}
  ],
  "action_result": "clicked"
}
```

### 示例4：执行JavaScript

```json
{"tool": "tmwd_exec", "script": "JSON.stringify({title: document.title, url: window.location.href, links: document.querySelectorAll('a').length})"}
```

输出：
```json
{
  "result": "{\"title\":\"今日新闻\",\"url\":\"https://news.example.com\",\"links\":42}",
  "success": true
}
```

### 示例5：表单填充

```json
{"tool": "tmwd_elements", "selector": "#login-form #email", "action": "type", "value": "user@example.com"}
```

输出：
```json
{
  "found": 1,
  "elements": [{"tag": "input", "type": "email", "id": "email"}],
  "action_result": "typed",
  "value": "user@example.com"
}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 无已连接标签页 | 浏览器扩展未安装或未激活 | 安装浏览器扩展，确保Chrome正在运行且扩展已启用 |
| 指示灯为红色 | 扩展与桥接服务断开 | 点击扩展图标重新连接，检查桥接服务是否运行 |
| CSP策略阻止脚本执行 | 网站内容安全策略限制 | 使用 `tmwd_elements` 替代 `tmwd_exec`，或联系网站管理员 |
| 点击元素无效果 | 元素被遮挡或不可见 | 检查元素 `visible` 属性，先滚动到元素位置再点击 |
| 跨域iframe无法访问 | 浏览器同源策略限制 | 只能操作同源页面，跨域iframe内容不可访问 |
| `tmwd_text`返回空 | 页面尚未加载完成 | 增加 `tmwd_navigate` 的 `wait` 参数等待时间 |
| `max_chars`超出5000 | 提取文本过长 | 分多次提取，或使用 `tmwd_elements` 精确定位 |

## 常见问题

### Q1: 如何确认浏览器已连接？
A: 调用 `tmwd_status`，检查 `connected` 是否为 `true` 且 `indicator` 为 `green`。如果为 `false` 或 `red`，说明扩展未连接。

### Q2: `tmwd_text` 的 `max_chars` 参数有什么限制？
A: 默认值为5000字符。如果页面文本超过5000字符，`truncated` 字段为 `true`。需要完整文本时，分多次提取或使用 `tmwd_elements` 精确定位特定区域。

### Q3: 为什么 `tmwd_exec` 在某些网站上失败？
A: 部分网站设置了严格的CSP（内容安全策略），阻止在页面上下文中执行JavaScript。此时改用 `tmwd_elements` 的 `action` 参数（如 `click`、`type`）替代脚本执行。

### Q4: 点击元素后没有反应怎么办？
A: 检查元素的 `visible` 属性是否为 `true`。如果元素被其他元素遮挡，先使用 `tmwd_exec` 执行 `element.scrollIntoView()` 滚动到元素位置。如果是动态加载的元素，增加等待时间。

### Q5: 能否操作跨域iframe中的内容？
A: 不能。浏览器同源策略限制了对跨域iframe的访问。只能操作与主页面同源的iframe内容。跨域iframe需要通过其他方式（如浏览器扩展的background script）访问。

### Q6: 如何同时操作多个标签页？
A: 通过 `tmwd_status` 的 `list_tabs` 操作列出所有标签页，使用 `tab_id` 参数指定操作的目标标签页。每次操作只能针对一个标签页。

### Q7: 截图保存在哪里？
A: 截图通过 `tmwd_exec` 执行 `screenshot()` 函数，返回Base64编码的PNG图片数据。需要手动解码保存为文件。截图分辨率为当前浏览器窗口大小。

## 已知限制

- 需要安装浏览器扩展并保持Chrome运行
- 指示灯为红色时无法操作，需重新连接
- `tmwd_text` 的 `max_chars` 默认5000字符
- CSP严格的网站无法使用 `tmwd_exec`
- 跨域iframe内容不可访问（同源策略限制）
- 每次操作仅针对一个标签页
- 截图返回Base64数据，需手动解码保存
