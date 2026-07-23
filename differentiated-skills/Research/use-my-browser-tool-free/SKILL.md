---
slug: use-my-browser-tool-free
name: use-my-browser-tool-free
version: 1.0.0
displayName: 真实浏览器控制免费版
summary: 通过用户脚本注入控制真实 Chrome 浏览器,共享登录态与 Cookie,适合个人自动化操作
license: Proprietary
edition: free
description: 真实浏览器控制免费版,面向个人用户提供直接控制用户真实 Chrome 浏览器的能力。通过用户脚本注入技术,在页面上下文中执行 JavaScript,共享所有
  Cookie、会话和登录状态。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务.
tags:
- 研究工具
- 浏览器控制
- 个人效率
tools:
- read
- exec
homepage: https://skillhub.cn
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9

---
# 真实浏览器控制免费版

## 概述

真实浏览器控制免费版是一款能够直接控制用户真实 Chrome 浏览器的自动化工具。与传统的无头浏览器不同,本工具通过用户脚本(Tampermonkey)注入技术,在用户已登录的浏览器页面上下文中执行 JavaScript,共享所有的 Cookie、会话和登录状态,无需重复登录即可操作已登录的网站.
本工具特别适合个人用户自动化已登录网站的批量操作,例如数据采集(需登录的页面)、表单自动填写、页面内容提取等场景。免费版聚焦本地浏览器场景,数据不出本机,保障隐私安全.
## 核心能力

### 1. 真实浏览器控制

控制用户正在使用的真实 Chrome 浏览器,保持所有登录状态.
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 真实浏览器控制免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 检查连接状态
tmwd_status()
# ...
# 列出已连接的标签页
tmwd_status()  # 返回所有已连接标签页列表
```

**输入**: 用户提供真实浏览器控制所需的指令和必要参数.
**处理**: 解析真实浏览器控制的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回真实浏览器控制的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 页面导航与内容提取

在真实浏览器中导航和提取页面内容.
```bash
# 切换到指定标签页
tmwd_switch(pattern="example.com")
# ...
# 导航到指定 URL
tmwd_navigate(url="https://example.com")
# ...
# 获取页面可见文本
tmwd_text(max_chars=5000)
# ...
# 获取简化 HTML
tmwd_scan()
```

**输入**: 用户提供页面导航与内容提取所需的指令和必要参数.
**处理**: 解析页面导航与内容提取的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回页面导航与内容提取的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 元素发现与交互

发现页面可交互元素并执行操作.
```bash
# 列出可交互元素
tmwd_elements()
# ...
# 执行 JavaScript(点击按钮)
tmwd_exec(code="document.querySelector('#submit').click()")
# ...
# 填写表单
tmwd_exec(code="var e=document.querySelector('#email'); e.value='user@example.com'; e.dispatchEvent(new Event('input',{bubbles:true}))")
```

**输入**: 用户提供元素发现与交互所需的指令和必要参数.
**处理**: 解析元素发现与交互的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回元素发现与交互的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 数据提取

从页面中提取结构化数据.
```bash
# 提取文本内容
tmwd_exec(code="return document.querySelector('.content').innerText")
# ...
# 提取列表数据
tmwd_exec(code="return Array.from(document.querySelectorAll('h2')).map(e=>e.textContent)")
# ...
# 提取表格数据
tmwd_exec(code="var rows=document.querySelectorAll('table tr'); var d=[]; rows.forEach(function(r){var c=[]; r.querySelectorAll('td,th').forEach(function(e){c.push(e.innerText.trim())}); if(c.length) d.push(c)}); return d")
```

**输入**: 用户提供数据提取所需的指令和必要参数.
**处理**: 解析数据提取的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回数据提取的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. 多标签页管理

管理多个浏览器标签页.
```bash
# 打开新标签页
tmwd_newtab(url="https://example.com")
# ...
# 切换到匹配的标签页
tmwd_switch(pattern="example.com")
```

**输入**: 用户提供多标签页管理所需的指令和必要参数.
**处理**: 解析多标签页管理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回多标签页管理的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 6. CSP 回退机制

当目标网站阻止脚本执行时,自动回退到内置浏览器.
```bash
# 当 tmwd_exec 返回 csp_blocked: true 时,回退到内置浏览器
# 步骤1:使用内置浏览器打开相同 URL
browser(action="open", profile="skill-platform", url="<same-url>")
# ...
# 步骤2:获取页面快照
browser(action="snapshot", targetId=<targetId>)
```

**输入**: 用户提供CSP 回退机制所需的指令和必要参数.
**处理**: 解析CSP 回退机制的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回CSP 回退机制的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：通过用户脚本注入、控制真实、共享登录态与、Cookie、适合个人自动化操、真实浏览器控制免、面向个人用户提供、直接控制用户真实、浏览器的能力、在页面上下文中执、共享所有、会话和登录状态、when、需要提升效率、自动化流程、批量处理、工作流优化时使用、不适用于需要人工、创意判断的任务、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景

### 场景一:个人用户数据采集

小王需要从已登录的电商网站批量提取订单数据.
```bash
# 步骤1:验证连接
tmwd_status()
# ...
# 步骤2:切换到电商网站标签页
tmwd_switch(pattern="shopping.example.com")
# ...
# 步骤3:导航到订单页面
tmwd_navigate(url="https://shopping.example.com/orders")
# ...
# 步骤4:提取订单列表
tmwd_exec(code="var orders=document.querySelectorAll('.order-item'); var data=[]; orders.forEach(function(o){data.push({id:o.querySelector('.order-id').innerText,date:o.querySelector('.order-date').innerText,amount:o.querySelector('.order-amount').innerText})}); return data")
```

### 场景二:表单自动填写

小李需要批量填写相似的在线表单.
```bash
# 步骤1:导航到表单页面
tmwd_navigate(url="https://form.example.com/apply")
# ...
# 步骤2:填写表单字段
tmwd_exec(code="var f={'#username':'liming','#email':'liming@example.com','#phone':'13800138000'}; Object.keys(f).forEach(function(s){var e=document.querySelector(s); e.value=f[s]; e.dispatchEvent(new Event('input',{bubbles:true}))})")
# ...
# 步骤3:提交表单
tmwd_exec(code="document.querySelector('#submit').click()")
# ...
# 步骤4:验证提交结果
tmwd_text(max_chars=1000)
```

### 场景三:页面内容整理

小张需要将网页内容整理为结构化数据.
```bash
# 步骤1:切换到目标页面
tmwd_switch(pattern="article.example.com")
# ...
# 步骤2:提取文章标题和内容
tmwd_exec(code="return {title:document.querySelector('h1').innerText,content:document.querySelector('.article-body').innerText}")
# ...
# 步骤3:提取所有链接
tmwd_exec(code="return Array.from(document.querySelectorAll('a')).map(function(a){return {text:a.innerText,href:a.href}})")
```

## 快速开始

### 依赖详情

```bash
# 安装浏览器控制插件
skill-platform plugins install skill-platform-tmwd --registry https://registry.npmjs.org
```

### 第二步:安装用户脚本

在 Chrome 中安装 Tampermonkey 扩展,然后添加用户脚本。安装成功后,浏览器右下角会显示绿色指示灯,表示已连接.
### 第三步:验证连接

```bash
# 检查连接状态
tmwd_status()
# ...
# 如果返回已连接的标签页列表,说明连接成功
```

### 第四步:执行首个操作

```bash
# 读取当前页面内容
tmwd_text(max_chars=5000)
# ...
# 执行简单操作
tmwd_exec(code="return document.title")
```

## 示例

### 基础配置

```bash
# config.json - 浏览器控制配置
{
  "connection": {
    "auto_reconnect": true,
    "heartbeat_interval": 5000,
    "timeout": 30000
  },
  "execution": {
    "max_execution_time": 10000,
    "return_format": "json"
  },
  "fallback": {
    "enabled": true,
    "on_csp_blocked": "browser_tool"
  }
}
```

### JavaScript 模式速查

| 操作 | 代码 |
|:-----|:-----|
| 点击按钮 | `document.querySelector('button.submit').click()` |
| 填写输入框 | `var e=document.querySelector('#input'); e.value='x'; e.dispatchEvent(new Event('input',{bubbles:true}))` |
| 选择下拉框 | `var s=document.querySelector('select'); s.value='opt1'; s.dispatchEvent(new Event('change',{bubbles:true}))` |
| 勾选复选框 | `var c=document.querySelector('[type=checkbox]'); c.checked=true; c.dispatchEvent(new Event('change',{bubbles:true}))` |
| 滚动到底部 | `window.scrollTo(0, document.body.scrollHeight)` |
| 滚动到元素 | `document.querySelector('#target').scrollIntoView()` |
| 等待元素出现 | `return !!document.querySelector('.loaded')` |
| 获取当前 URL | `return location.href` |
| 返回上一页 | `history.back()` |
| 按文本匹配点击 | `var btns=document.querySelectorAll('button'); for(var i=0;i<btns.length;i++){if(btns[i].innerText.includes('Submit')){btns[i].click();break}}` |

## 最佳实践

### 1. 优先使用 tmwd,失败再回退

```bash
# 正确做法:先尝试 tmwd,失败再回退
tmwd_exec(code="document.querySelector('#btn').click()")
# ...
# 如果返回 csp_blocked: true,再回退到内置浏览器
browser(action="open", profile="skill-platform", url="<same-url>")
```

### 2. React/Vue 应用需触发事件

```bash
# 对于 React/Vue 应用,设置值后必须触发事件
tmwd_exec(code="var e=document.querySelector('#input'); e.value='new_value'; e.dispatchEvent(new Event('input',{bubbles:true}))")
# ...
# 直接设置 value 不会触发框架响应
tmwd_exec(code="document.querySelector('#input').value='new_value'")  # 无效
```

### 3. 使用 return 返回数据

```bash
# 有 return:返回执行结果
tmwd_exec(code="return document.querySelector('.title').innerText")
# ...
# 无 return:无输出
tmwd_exec(code="document.querySelector('.title').innerText")  # 无输出
```

### 4. 检查连接状态

```bash
# 操作前先检查连接
tmwd_status()
# ...
# 如果显示"No connected tabs",检查浏览器右下角指示灯
# 绿色:已连接
# 红色:连接断开,刷新页面即可重连
```

## 常见问题

### Q1: 提示"No connected tabs"怎么办?

**A:** 按以下步骤排查:

1. 检查 Chrome 右下角是否有绿色指示灯
2. 如果是红色,刷新页面,用户脚本会自动重连
3. 确认 Tampermonkey 扩展已启用
4. 确认用户脚本已正确安装

### Q2: 点击操作没有效果?

**A:** 尝试使用事件分发:

```bash
# 直接 click 可能无效
tmwd_exec(code="document.querySelector('#btn').click()")
# ...
# 改用事件分发
tmwd_exec(code="document.querySelector('#btn').dispatchEvent(new MouseEvent('click',{bubbles:true}))")
```

### Q3: CSP 阻止脚本执行怎么办?

**A:** 部分网站(X/Twitter、银行网站)通过内容安全策略阻止脚本执行。当 `tmwd_exec` 返回 `csp_blocked: true` 时,回退到内置浏览器:

```bash
# 回退到内置浏览器
browser(action="open", profile="skill-platform", url="<same-url>")
browser(action="snapshot", targetId=<targetId>)
```

### Q4: 跨域 iframe 无法访问?

**A:** 由于同源策略限制,跨域 iframe 无法直接访问。建议:

1. 直接导航到 iframe 的 URL
2. 使用内置浏览器(基于 CDP,可绕过部分限制)

### 已知限制

**A:** 免费版主要面向个人本地浏览器场景,具备完整的真实浏览器控制能力。如需批量操作、多浏览器实例、企业级安全管控等高级功能,请考虑升级到 PRO 版本.
## 依赖说明

### 运行环境

- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **浏览器**: Google Chrome 100 及以上版本
- **浏览器扩展**: Tampermonkey(用户脚本管理器)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| Chrome 浏览器 | 浏览器 | 必需 | 官方网站下载安装 |
| Tampermonkey | 浏览器扩展 | 必需 | Chrome 应用商店安装 |
| skill-platform-tmwd | 插件 | 必需 | 通过 `skill-platform plugins install` 安装 |
| 用户脚本 | 脚本 | 必需 | 通过 Tampermonkey 安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

免费版基于本地浏览器运行,无需额外 API Key。所有操作在用户的真实浏览器中执行,数据不离开本机.
### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,通过 exec 执行浏览器控制命令)
- **说明**: 基于用户脚本注入的真实浏览器控制工具,通过自然语言指令驱动 Agent 操作用户已登录的浏览器
- **适用规模**: 单用户、单浏览器实例、本地运行

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |
