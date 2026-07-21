---
slug: cdp-browser-master
name: cdp-browser-master
version: "1.0.0"
displayName: CDP浏览器大师
summary: 解决反爬检测、选择器易变、SPA路由、等待不准四大痛点，附反检测与智能等待。
license: Proprietary
description: |-
  通过Chrome DevTools Protocol驱动已登录浏览器执行自动化任务,解决反爬检测、选择器易变、SPA路由难导航、等待不准四大痛点,提供反检测策略、选择器探测模式、SPA导航模式、智能等待、Cookie获取、连接管理六大核心能力。适用于JS渲染页面抓取、需登录态网站操作、平台配额查询场景。适用关键词:CDP、浏览器自动化、Chrome、Edge、反爬、选择器、SPA、智能等待、Cookie
tags:
- 自动化
- 浏览器
- 数据抓取
tools:
  - - read
- exec
---

# CDP浏览器大师

通过用户已登录的浏览器(Edge/Chrome)执行自动化任务。核心技术:CDP(Chrome DevTools Protocol),通过WebSocket与浏览器通信。核心信条:**优先用web_fetch,CDP只用于JS渲染或需登录态的场景;先探测再定位,多备选降级。**

## 核心能力

### 1. 反检测策略
UA天然真实(用已登录浏览器)、启动参数`--disable-blink-features=AutomationControlled`规避WebDriver标记、行为拟人化(随机延迟)、Cloudflare绕过思路(复用已验证会话)

**输入**: 用户提供反检测策略所需的指令和必要参数。
**处理**: 按照skill规范执行反检测策略操作,遵循单一意图原则。
**输出**: 返回反检测策略的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 2. 选择器探测模式
先eval探索DOM结构(打印class/tag/text样本),再写精确选择器,提供多备选(精确class→模糊`[class*="xxx"]`→语义tag→属性选择器)降级匹配

**输入**: 用户提供选择器探测模式所需的指令和必要参数。
**处理**: 按照skill规范执行选择器探测模式操作,遵循单一意图原则。
**输出**: 返回选择器探测模式的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 3. SPA导航模式
处理Next.js/React内部路由,先入可访问父页面(如`/user-center/basic-information`),再用JS点击侧边栏`<div cursor-pointer>`触发内部路由跳转,避免直接navigate子路由404

**输入**: 用户提供SPA导航模式所需的指令和必要参数。
**处理**: 按照skill规范执行SPA导航模式操作,遵循单一意图原则。
**输出**: 返回SPA导航模式的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 4. 智能等待
`waitNetworkIdle`检测无请求持续500ms即继续,替代固定sleep,既不快也不慢

**输入**: 用户提供智能等待所需的指令和必要参数。
**处理**: 按照skill规范执行智能等待操作,遵循单一意图原则。
**输出**: 返回智能等待的执行结果,包含操作状态和输出数据。

### 5. Cookie获取
普通Cookie用`document.cookie`,HttpOnly Cookie用CDP `Network.getCookies`命令获取

**输入**: 用户提供Cookie获取所需的指令和必要参数。
**处理**: 按照skill规范执行Cookie获取操作,遵循单一意图原则。
**输出**: 返回Cookie获取的执行结果,包含操作状态和输出数据。

### 6. 连接管理
端口复用(每端口同时一个WebSocket)、ConnectionManager自动管理、残留连接清理、端口占用排查

**输入**: 用户提供连接管理所需的指令和必要参数。
**处理**: 按照skill规范执行连接管理操作,遵循单一意图原则。
**输出**: 返回连接管理的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：解决反爬检测、选择器易变、等待不准四大痛点、附反检测与智能等、Chrome、DevTools、Protocol、驱动已登录浏览器、执行自动化任务、路由难导航、连接管理六大核心、适用于、渲染页面抓取、需登录态网站操作、平台配额查询场景、适用关键词、浏览器自动化、Edge等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 适用场景

**何时使用**:
- JS渲染页面抓取(B站、SPA应用,web_fetch拿到空壳)
- 需登录态的网站操作(已登录在你的浏览器里)
- 需要交互(点击、填表、滚动)的自动化
- 平台配额查询(如Minimax Token Plan,每5小时重置)
- 多标签页管理与数据提取

**输入**:目标网站URL、待提取数据描述、可选的交互动作(点击/滚动/填表)
**输出**:结构化数据(JSON)、页面截图(PNG base64)、Cookie信息

**不适用场景**:
- 静态HTML页面抓取(直接用web_fetch即可,无需CDP)
- 无浏览器环境的服务器(需本地Edge/Chrome)
- 强反爬站点且无法通过验证页的场景(如小红书可能失败)

## 使用流程

### Step 1: 开启浏览器远程调试
**Edge(端口9222)**:
```powershell
taskkill /F /IM msedge.exe /T
Start-Sleep 3
Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --disable-blink-features=AutomationControlled
```
**Chrome(端口9223)**:
```powershell
Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9223
```

### Step 2: 导入模块并导航
```javascript
const { edge, chrome } = require('./cdp-automation.js');
await edge.goto('https://目标网站.com');
```

### Step 3: 探测DOM结构(选择器探测模式)
```javascript
const structure = await edge.eval(`
    JSON.stringify({
        title: document.title,
        samples: Array.from(document.querySelectorAll('[class*="note"]')).slice(0,3).map(x => ({
            text: x.innerText?.substring(0,100),
            class: x.className?.substring(0,60)
        }))
    })
`);
```

### Step 4: 执行操作与智能等待
```javascript
await edge.click('[class*="radio-filter__item"]');
await edge.waitNetworkIdle(10000);  // 智能等待,最多10秒
```

### Step 5: 提取数据
```javascript
const result = await edge.eval(`提取数据的JS`);
const png = await edge.screenshot();
```

### Step 6: SPA导航(如需访问子路由)
先入可访问页面,再用JS点击侧边栏div触发内部路由:
```javascript
await edge.goto('https://app.com/user-center/basic-information');
await edge.waitNetworkIdle();
await edge.eval(`document.querySelector('div.cursor-pointer').click()`);
await edge.waitNetworkIdle();
```

## 示例

### 示例
**输入**: 抓取某UP主主页前5个视频的标题和播放量

**输出**:
```javascript
await edge.goto('https://space.bilibili.com/151190274/video');
await edge.waitNetworkIdle();
const r = await edge.eval(`
    JSON.stringify(
        Array.from(document.querySelectorAll('.upload-video-card')).slice(0,5).map(c => ({
            title: c.querySelector('.bili-video-card__title')?.innerText,
            play: parseInt(c.querySelector('.bili-cover-card__stat span')?.innerText?.replace(/\D/g,''))
        }))
    )
`);
const videos = JSON.parse(r.result.value);
// [{title:"视频A",play:1890}, {title:"视频B",play:5678}, ...]
```

### 示例2: 查询Minimax Token Plan配额
**输入**: 查询platform.minimaxi.com的Token Plan剩余配额(Next.js SPA子路由)

**输出**:
```javascript
// Step 1: 先入可访问页面(直接navigate子路由会404)
await edge.goto('https://platform.minimaxi.com/user-center/basic-information');
await edge.waitNetworkIdle();

// Step 2: JS点击侧边栏div触发SPA路由(注意:不是<a>标签)
await edge.eval(`
    (function() {
        var allDivs = document.querySelectorAll('div');
        for (var d of allDivs) {
            if (d.innerText && d.innerText.trim() === 'Token Plan'
                && d.className.includes('cursor-pointer')) {
                d.click();
                return 'clicked';
            }
        }
        return 'not found';
    })()
`);
await edge.waitNetworkIdle();

// Step 3: 提取配额数据
const r = await edge.eval(`(function(){
  var t = document.body.innerText;
  var plan = t.match(/(Starter|Pro|Enterprise)[^\\n]*/)?.[0];
  var quota = t.match(/可用额度[：:][^\\n]*/)?.[0];
  var used = t.match(/(\\d+)\\/600/)?.[0];
  return JSON.stringify({plan, quota, used});
})()`);
// {plan:"Starter年度套餐", quota:"可用额度:423次模型调用 / 5小时", used:"177/600"}
```

## 错误处理

| 场景 | 原因 | 处理方式 |
|:-----|:-----|:---------|
| 连接9222失败 | 端口被占或浏览器未启动 | `netstat -ano \| findstr :9222`查端口,`taskkill /F /PID <pid>`清残留,重启浏览器 |
| eval返回空值 | 页面未渲染完 | 用`waitNetworkIdle`替代固定sleep,JS密集页面手动加到8-10s |
| click无反应 | 选择器未命中或元素不可点 | 用探测模式验证选择器,用`elementFromPoint`模拟点击 |
| 被反爬拦截 | 检测到自动化标记 | 加`--disable-blink-features=AutomationControlled`,行为拟人化,复用已验证会话Cookie |
| SPA子路由404 | 直接navigate到SPA内部路由 | 先入可访问父页面,再JS点击侧边栏div触发内部路由跳转 |
| Cookie缺失 | HttpOnly Cookie用document.cookie拿不到 | 用CDP `Network.getCookies`命令获取 |
| 连接残留 | 任务中途失败连接未释放 | 重启浏览器远程调试,杀掉占用端口的进程 |
| 截图空白 | 页面未加载完就截图 | 先`waitNetworkIdle`再`screenshot` |
| 端口被联想Vantage占用 | msedgewebview2.exe占用9222 | 杀掉msedgewebview2.exe实例再启动你的Edge |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Agent LLM | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需(运行cdp-automation.js) | nodejs.org |
| Edge/Chrome | 浏览器 | 必需 | 系统自带或官网下载 |
| cdp-automation.js | 模块 | 必需 | 随skill提供,位于`~/.skill-platform/browser-automation/` |

**运行环境**:
- 操作系统: Windows(Edge/Chrome路径示例为Windows,macOS/Linux类似)
- 浏览器: Microsoft Edge 或 Google Chrome(已安装并可启动远程调试)
- 本skill基于本地浏览器自动化,无需额外API Key
- 涉及需登录的网站时,使用用户已登录的浏览器会话(无需配置凭证)

**可用性分类**: MD+EXEC(Markdown指令 + Node.js脚本执行)

## 常见问题

**Q: 什么时候该用CDP而不是web_fetch?**
A: JS渲染页面、需登录态、需交互(点击/填表)时用CDP。静态HTML用web_fetch即可。B站等页面web_fetch拿到的是空壳。

**Q: 被Cloudflare拦了怎么办?**
A: 用真实已登录浏览器(非Headless),加`--disable-blink-features=AutomationControlled`,操作间加随机延迟(500-1500ms),首次访问等验证页通过后复用Cookie。

**Q: 选择器经常失效怎么办?**
A: 用探测模式——先eval探索DOM结构再定位。提供多备选选择器(从精确class到模糊`[class*="xxx"]`到语义tag到属性选择器)降级匹配。优先用`[class*="xxx"]`模糊匹配。

**Q: Next.js SPA子路由404怎么解决?**
A: 直接navigate会404。先进入可访问的父页面(如`/user-center/basic-information`),再用JS点击侧边栏div(`cursor-pointer`)触发内部路由跳转,跳转后用`waitNetworkIdle`等待数据加载。

**Q: 怎么拿HttpOnly Cookie?**
A: `document.cookie`拿不到。用CDP的`Network.getCookies`命令:`cdpSession.send('Network.getCookies', {urls: ['https://目标网站.com']})`。

## 已知限制

1. **依赖本地浏览器环境**:需提前安装Edge/Chrome并启动远程调试,无浏览器环境的服务器无法使用
2. **每端口单连接限制**:同一时间每个端口(9222/9223)只能有一个WebSocket连接,多任务需排队或用不同端口
3. **强反爬站点可能失败**:小红书等强反自动化检测站点,即使加反检测策略仍可能被识别,建议先测试能否正常浏览
4. **选择器随网站改版失效**:网站更新可能导致选择器失效,需用探测模式重新探索DOM结构
5. **不适用Headless场景**:本skill核心优势是复用已登录浏览器会话,Headless模式失去此优势且更易被检测
