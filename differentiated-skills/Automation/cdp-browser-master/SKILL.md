---
slug: cdp-browser-master
name: cdp-browser-master
version: 1.0.1
displayName: CDP浏览器大师
summary: 解决反爬检测、选择器易变、SPA路由、等待不准四大痛点，附反检测与智能等待.
license: Proprietary
description: 通过Chrome DevTools Protocol驱动已登录浏览器执行自动化任务,解决反爬检测、选择器易变、SPA路由难导航、等待不准四大痛点,提供反检测策略、选择器探测模式、SPA导航模式、智能等待、Cookie获取、连接管理六大核心能力。适用于JS渲染页面抓取、需登录态网站操作、平台配额查询场景。适用关键词:CDP、浏览器自动化、Chrome、Edge、反爬、选择器、SPA、智能等待、Cookie
tags:
- 自动化
- 浏览器
- 数据抓取
tools:
- read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "自动化,工作流,效率"
category: "Automation"
---
# CDP浏览器大师

通过用户已登录的浏览器(Edge/Chrome)执行自动化任务。核心技术:CDP(Chrome DevTools Protocol),通过WebSocket与浏览器通信。核心信条:**优先用web_fetch,CDP只用于JS渲染或需登录态的场景;先探测再定位,多备选降级。**

## 核心能力

### 1. 反检测策略
UA天然真实(用已登录浏览器)、启动参数`--disable-blink-features=AutomationControlled`规避WebDriver标记、行为拟人化(随机延迟)、Cloudflare绕过(复用已验证会话)。使用`input_params`参数支持创建/查询/导出操作。

### 2. 选择器探测模式
先eval探索DOM结构(打印class/tag/text样本),再写精确选择器,提供多备选(精确class→模糊`[class*="xxx"]`→语义tag→属性选择器)降级匹配。使用`input_params`参数支持创建/查询/导出操作。

### 3. SPA导航模式
处理Next.js/React内部路由,先入可访问父页面(如`/user-center/basic-information`),再用JS点击侧边栏`<div cursor-pointer>`触发内部路由跳转,避免直接navigate子路由404。使用`input_params`参数支持创建/查询/导出操作。

### 4. 智能等待
`waitNetworkIdle`检测无请求持续500ms即继续,替代固定sleep,既不快也不慢。

### 5. Cookie获取
普通Cookie用`document.cookie`,HttpOnly Cookie用CDP `Network.getCookies`命令获取。

### 6. 连接管理
端口复用(每端口同时一个WebSocket)、ConnectionManager自动管理、残留连接清理、端口占用排查。使用`input_params`参数支持创建/查询/导出操作。

## 适用场景

**何时使用**: JS渲染页面抓取(B站、SPA应用)、需登录态的网站操作、需要交互(点击/填表/滚动)的自动化、平台配额查询、多标签页管理与数据提取

**不适用场景**: 静态HTML页面抓取(用web_fetch即可)、无浏览器环境的服务器、强反爬站点且无法通过验证页的场景

## 关键参数说明

| 模块 | 方法 | 关键参数 | 说明 |
|---|---|---|---|
| edge/chrome | `goto(url)` | url:目标地址 | 导航到指定页面 |
| edge/chrome | `eval(js)` | js:JS表达式字符串 | 在页面执行JS并返回结果 |
| edge/chrome | `click(selector)` | selector:CSS选择器 | 点击元素 |
| edge/chrome | `waitNetworkIdle(timeout)` | timeout:最大等待ms(默认10000) | 智能等待网络空闲 |
| edge/chrome | `screenshot()` | 无 | 返回PNG base64截图 |

**启动浏览器远程调试**:
- Edge: `Start-Process msedge.exe --remote-debugging-port=9222 --disable-blink-features=AutomationControlled`
- Chrome: `Start-Process chrome.exe --remote-debugging-port=9223`
- 模块导入: `const { edge, chrome } = require('./cdp-automation.js');`

**典型流程**: 导航→探测DOM(eval打印结构)→操作(click/填表)→智能等待(waitNetworkIdle)→提取数据(eval/screenshot)。SPA导航需先入父页面再JS点击侧边栏div。

## 错误处理

| 场景 | 原因 | 处理方式 |
|:-----|:-----|:-----|
| 连接9222失败 | 端口被占或浏览器未启动 | `netstat -ano \| findstr :9222`查端口,`taskkill /F /PID <pid>`清残留,重启浏览器 |
| eval返回空值 | 页面未渲染完 | 用`waitNetworkIdle`替代固定sleep,JS密集页面手动加到8-10s |
| 被反爬拦截 | 检测到自动化标记 | 加`--disable-blink-features=AutomationControlled`,行为拟人化,复用已验证会话Cookie |
| SPA子路由404 | 直接navigate到SPA内部路由 | 先入可访问父页面,再JS点击侧边栏div触发内部路由跳转 |
| Cookie缺失 | HttpOnly Cookie用document.cookie拿不到 | 用CDP `Network.getCookies`命令获取 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| Agent LLM | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需(运行cdp-automation.js) | nodejs.org |
| Edge/Chrome | 浏览器 | 必需 | 系统自带或官网下载 |
| cdp-automation.js | 模块 | 必需 | 随skill提供,位于`~/.skill-platform/browser-automation/` |

**运行环境**: Windows(macOS/Linux类似),Microsoft Edge或Google Chrome(已安装并启动远程调试)。基于本地浏览器自动化,无需额外API Key;涉及需登录的网站时使用用户已登录的浏览器会话。

**可用性分类**: MD+EXEC(Markdown指令 + Node.js脚本执行)

## 常见问题

**Q: 什么时候该用CDP而不是web_fetch?**
A: JS渲染页面、需登录态、需交互(点击/填表)时用CDP。静态HTML用web_fetch即可。B站等页面web_fetch拿到的是空壳。

**Q: 选择器经常失效怎么办?**
A: 用探测模式——先eval探索DOM结构再定位。提供多备选选择器(从精确class到模糊`[class*="xxx"]`到语义tag到属性选择器)降级匹配。优先用`[class*="xxx"]`模糊匹配。

**Q: 怎么拿HttpOnly Cookie?**
A: `document.cookie`拿不到。用CDP的`Network.getCookies`命令:`cdpSession.send('Network.getCookies', {urls: ['https://目标网站.com']})`。

## 已知限制

1. **依赖本地浏览器环境**:需提前安装Edge/Chrome并启动远程调试,无浏览器环境的服务器无法使用
2. **每端口单连接限制**:同一时间每个端口(9222/9223)只能有一个WebSocket连接,多任务需排队或用不同端口
3. **强反爬站点可能失败**:小红书等强反自动化检测站点,即使加反检测策略仍可能被识别
4. **选择器随网站改版失效**:网站更新可能导致选择器失效,需用探测模式重新探索DOM结构
5. **不适用Headless场景**:核心优势是复用已登录浏览器会话,Headless模式失去此优势且更易被检测
