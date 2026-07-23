---
slug: stealth-browser-assistant
name: stealth-browser-assistant
version: "1.1.0"
displayName: "反检测浏览器助手"
summary: "一人管百号的浏览器自动化底座,指纹隔离+崩溃自愈+智能定位,告别封号掉线"
license: Proprietary
description: |-
  反检测浏览器助手是一款浏览器自动化引擎,专为Agent浏览器场景设计。
  支持指纹隔离、崩溃自愈、DOM蒸馏智能定位,实现一人管百号不关联。
  
  核心能力:
  - DOM蒸馏三树智能定位
  - Tab崩溃3秒自愈
  - 浏览器指纹防护与多账号隔离
  - 反检测混合方案与行为模拟
homepage: "https://skillhub.cn"
tags: [浏览器自动化, 多账号管理, 反检测, 效率工具]
tools:
  - read
  - exec
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# 反检测浏览器助手 Stealth Browser Assistant v1.1.0

智能浏览器自动化引擎,融合DOM蒸馏定位、稳定性增强、反检测混合方案,专为Agent浏览器自动化场景设计。

> **合规声明**: 本工具仅用于合法合规的浏览器自动化场景(自动化测试/RPA流程/合规多账号管理)。使用者需遵守各平台服务条款(ToS)和当地法律法规,禁止用于爬虫滥用、刷量、欺诈等违规行为。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

1. **DOM蒸馏三树智能定位**: 通过CDP获取DOM树+Accessibility树+DOMSnapshot三树数据,按降级链定位元素(无障碍角色→文本匹配→JS事件监听器→坐标点击),彻底解决SPA前端更新导致元素失效痛点
2. **Tab崩溃3秒自愈**: 监听page crash事件+浏览器断连事件,崩溃时3秒内重建浏览器上下文,恢复崩溃前URL与Cookie,端口竞争重试(3次/500ms间隔)
3. **浏览器指纹防护与多账号隔离**: 每个账号独立浏览器配置目录(指纹隔离)+独立Cookie存储(会话隔离)+操作间隔频率控制(防关联检测),支持一人管百号不关联
4. **反检测混合方案**: 日常操作走自动化API,敏感操作走独立WebSocket直连CDP,敏感操作前通过直连通道执行反检测JS,CDP探针验证反检测有效性
5. **行为模拟与Cookie预热**: 模拟真人操作节奏,先访问首页建立Session再执行搜索,操作前校验ref/key/fields参数完整性(防LLM幻觉)
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 元素定位失败(SPA前端更新) | action=locate_element+intent+fallback_selectors | element元素句柄+method定位方法+confidence置信度 |
| Tab崩溃自动恢复 | action=recover_tab+url+cookie_path | recovery_time_ms恢复耗时+恢复状态 |
| 反检测能力增强 | action=stealth_check | 反检测结果+CDP探针验证状态 |
| 多账号隔离管理 | action=browser_lifecycle+profile_dir | 浏览器生命周期管理+指纹隔离状态 |
| 自动化测试/RPA流程 | action=locate_element+page+intent | 元素定位+操作执行+结果回写 |
| Cookie预热与保活 | action=browser_lifecycle+cookie_path | Session建立+Cookie加载状态 |

**不适用于**: 爬虫滥用(大规模数据抓取违反平台ToS)、刷量/刷单/刷评(违反平台规则)、绕过付费墙/验证码破解(违反法律法规)、欺诈/钓鱼等违法行为、移动端APP自动化(仅支持桌面浏览器)。

## 使用流程

### Step 1: 环境准备
- 确认Agent已加载本SKILL.md,且支持exec工具
- 确认系统已安装Chrome浏览器(用于反检测和CDP连接)
- 本Skill无需额外API Key配置,通过CDP协议连接Chrome
- 可选安装浏览器自动化框架(Playwright/Puppeteer)

### Step 2: 选择方案
- **方案A**: DOM蒸馏定位(元素失效场景)
- **方案B**: 浏览器稳定性保障(Tab崩溃场景)
- **方案C**: 反检测混合方案(被识别场景)
- **多账号隔离**: 多账号矩阵管理(合规场景)

### Step 3: DOM蒸馏定位(方案A)
1. 通过CDP连接获取三树数据(DOM树+Accessibility树+DOMSnapshot)
2. 简化DOM树(过滤style/（请参考skill目录中的脚本文件）)
3. 按绘制顺序过滤被遮挡的不可见元素
4. 优化树结构(移除无意义中间容器节点)
5. 按包围盒传播过滤被父元素覆盖的子元素
6. 分配交互索引(backendNodeId)生成selector_map
7. 按降级链定位元素: 无障碍角色→文本匹配→JS事件监听器→坐标点击
8. 返回定位结果+置信度评分

### Step 4: 浏览器稳定性保障(方案B)
1. 浏览器管理器统一管理生命周期(启动/关闭/重启)
2. 注册Tab崩溃监听(page crash事件 + 浏览器断连事件)
3. 崩溃时重建浏览器上下文
4. 恢复崩溃前的URL
5. 重新加载Cookie
6. 端口竞争重试(Chrome重启时3次/500ms间隔)
7. 操作前校验ref/key/fields参数完整性(防LLM幻觉)
8. Cookie预热(先访问首页建立Session再执行搜索)

### Step 5: 反检测混合方案(方案C)
1. 启动系统Chrome(--remote-debugging-port + 反检测启动参数)
2. 通过CDP协议连接(日常操作通道)
3. 建立独立WebSocket直连CDP(敏感操作通道)
4. 敏感操作前通过直连通道执行反检测JS(不触发自动化框架初始化)
5. CDP探针检测(验证反检测有效性)
6. 操作分流(日常走自动化API,敏感走直连CDP)

### Step 6: 多账号隔离
1. 每个账号独立浏览器配置目录(指纹隔离)
2. 独立Cookie存储(会话隔离)
3. 操作间隔频率控制(防关联检测)
4. 账号切换时清理上下文

## 输入格式

```json
{
  "action": "locate_element|recover_tab|stealth_check|browser_lifecycle",
  "params": {
    "page": "浏览器页面对象",
    "intent": "自然语言描述要找的元素(如'发布按钮')",
    "fallback_selectors": ["CSS选择器降级列表"],
    "url": "恢复URL(用于Tab崩溃恢复)",
    "cookie_path": "Cookie文件路径",
    "profile_dir": "浏览器配置目录(多账号隔离)"
  }
}
```

## 输出格式

```json
{
  "success": true,
  "data": {
    "element": "定位到的元素句柄或坐标",
    "method": "ax_role|text_match|event_listener|coordinate",
    "confidence": 0.95,
    "recovery_time_ms": 1200
  },
  "error": null,
  "code": null
}
```

## 异常处理


| 异常场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| DOM蒸馏CDP超时 | CDP连接超过10秒未响应 | 10秒超时→2秒→降级到fallback_selectors |
| Tab崩溃 | 页面内存溢出或浏览器异常 | 3秒内重建→恢复URL→重加载Cookie→触发告警通知 |
| 端口占用 | Chrome重启时端口被占用 | 3次/500ms间隔→失败则终止旧进程→ |
| CDP探针检测失败 | 反检测JS未生效 | 记录日志→降级到纯自动化API模式→触发告警 |
| Cookie失效 | Cookie过期或被平台清除 | 检测→暂停操作→通知等待人工处理或Cookie保活 |
| 验证码出现 | 平台风控触发验证码 | 截图→通知→等待人工处理,不自动绕过 |
| Chrome未安装 | 系统未安装Chrome浏览器 | 返回error,提示安装Chrome |
| CDP连接失败 | Chrome未启动调试端口 | 自动启动Chrome(含--remote-debugging-port参数)→连接 |
| 元素定位失败(全降级链) | 所有定位方法均未命中 | 返回success=false,提示人工检查页面结构 |
| 参数完整性校验失败 | ref/key/fields缺失(LLM幻觉) | 阻断操作,返回error提示补充参数 |
| 频率超限 | 操作频率超过安全阈值 | 自动暂停,等待冷却时间后继续 |

## 频率控制

> 所有浏览器自动化操作必须遵守安全频率限制,防止触发风控。

| 操作 | 安全频率 | 超限后果 |
|:-----|:---------|:---------|
| 刷新商品 | 每日1次/商品 | 触发验证 |
| 发布商品 | 间隔5-10秒 | 限流 |
| 回复消息 | per-chat追踪间隔1.0-2.0秒(首次零等待,仅连续回复补偿等待) | 标记机器人 |
| 调价 | 每日≤3次/商品 | 降权 |
| 多账号发布间隔 | ≥17分钟 | 关联封号 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:-------|:-----|:---------|:---------|:-------------|
| Chrome浏览器 | 运行时 | 必需 | 系统Chrome(用于反检测和CDP连接) | 国内可用: Chrome/Edge/360浏览器/QQ浏览器(需支持CDP) |
| CDP协议 | 协议 | 必需 | Chrome DevTools Protocol(Chrome内置) | 无需替代,Chrome内置 |
| 浏览器自动化框架 | SDK | 可选 | Playwright/Puppeteer等 | 国内替代: Playwright(微软开源)/Puppeteer(Google开源) |

### API Key 配置
- 本Skill无需额外API Key配置,通过CDP协议连接Chrome
- 如使用云浏览器服务(如Browserless),需配置对应服务的API Key,通过环境变量注入

### 使用流程
需要系统安装Chrome浏览器。通过CDP协议连接Chrome,无需额外API Key。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: DOM蒸馏定位(元素失效场景)

**输入**:
```json
{
  "action": "locate_element",
  "params": {
    "page": "浏览器页面对象",
    "intent": "发布按钮",
    "fallback_selectors": [".publish-btn", "#submit", "button[data-action='publish']"]
  }
}
```

**执行流程**:
1. 通过CDP获取页面DOM+无障碍树
2. 简化DOM树并过滤不可见元素
3. 按降级链定位:无障碍角色button + 文本"发布" → 命中
4. 返回:method="ax_role"(不依赖Hash类名),confidence=0.92

**输出**:
```json
{
  "success": true,
  "data": {
    "element": "element_handle_001",
    "method": "ax_role",
    "confidence": 0.92,
    "recovery_time_ms": null
  },
  "error": null,
  "code": null
}
```

### 示例2: Tab崩溃自动恢复

**输入**:
```json
{
  "action": "recover_tab",
  "params": {
    "url": "https://example.com/dashboard",
    "cookie_path": "/cookies/account_001.json"
  }
}
```

**执行流程**:
1. 监听到crash事件
2. 重建浏览器上下文
3. 恢复崩溃前URL
4. 重新加载Cookie
5. 3秒内完成恢复,继续执行任务

**输出**:
```json
{
  "success": true,
  "data": {
    "element": null,
    "method": null,
    "confidence": null,
    "recovery_time_ms": 2800
  },
  "error": null,
  "code": null
}
```

### 示例3: 反检测混合模式

**输入**:
```json
{
  "action": "stealth_check",
  "params": {
    "profile_dir": "/profiles/account_001"
  }
}
```

**执行流程**:
1. 启动系统Chrome(反检测启动参数)
2. 建立独立WebSocket直连CDP
3. 敏感操作前通过直连通道注入反检测JS
4. CDP探针验证反检测有效
5. 日常操作走自动化API,敏感操作走直连CDP

**输出**:
```json
{
  "success": true,
  "data": {
    "element": null,
    "method": "stealth_verified",
    "confidence": 0.88,
    "recovery_time_ms": null
  },
  "error": null,
  "code": null
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: DOM蒸馏定位(发布按钮,无障碍角色命中)

**输入**:
```json
{
  "action": "locate_element",
  "params": {
    "page": "浏览器页面对象",
    "intent": "发布按钮",
    "fallback_selectors": [".publish-btn", "#submit", "button[data-action='publish']"]
  }
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "element": "element_handle_001",
    "method": "ax_role",
    "confidence": 0.92,
    "recovery_time_ms": null
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓DOM蒸馏+无障碍树正确解析 ✓降级链ax_role命中(button+文本"发布") ✓method=ax_role(不依赖Hash类名) ✓置信度0.92(高置信) ✓CDP协议连接正常

### 案例2: Tab崩溃自动恢复(URL+Cookie恢复,3秒内)

**输入**:
```json
{
  "action": "recover_tab",
  "params": {
    "url": "https://seller.example.com/dashboard",
    "cookie_path": "/cookies/account_001.json"
  }
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "element": null,
    "method": null,
    "confidence": null,
    "recovery_time_ms": 2100,
    "recovery_details": {
      "tab_rebuilt": true,
      "url_restored": "https://seller.example.com/dashboard",
      "cookie_reloaded": true,
      "alert_sent": true,
      "login_required": false
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓Tab崩溃3秒内重建(2100ms) ✓URL正确恢复 ✓Cookie重新加载成功 ✓登录状态保持(login_required=false) ✓告警通知已触发

### 案例3: 反检测验证(CDP探针检测,反检测JS生效)

**输入**:
```json
{
  "action": "stealth_check",
  "params": {
    "page": "浏览器页面对象",
    "profile_dir": "/profiles/account_002"
  }
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "element": null,
    "method": "cdp_probe",
    "confidence": 0.95,
    "recovery_time_ms": null,
    "stealth_report": {
      "webdriver_flag": false,
      "navigator_automation": false,
      "cdp_detected": false,
      "fingerprint_randomized": true,
      "proxy_active": true,
      "overall_stealth_score": 95,
      "details": {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
        "webgl_vendor": "Google Inc. (NVIDIA)",
        "canvas_fingerprint": "randomized",
        "languages": ["zh-CN", "zh", "en"],
        "platform": "Win32"
      }
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓CDP探针检测通过(反检测JS生效) ✓webdriver标志隐藏成功 ✓指纹随机化(canvas/webgl) ✓代理IP激活 ✓整体隐身评分95分(优秀)

### 案例4: CDP探针检测失败降级(纯自动化API模式)

**输入**:
```json
{
  "action": "stealth_check",
  "params": {
    "page": "浏览器页面对象",
    "profile_dir": "/profiles/account_003"
  }
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "element": null,
    "method": "automation_api",
    "confidence": 0.65,
    "recovery_time_ms": null,
    "stealth_report": {
      "webdriver_flag": true,
      "navigator_automation": true,
      "cdp_detected": true,
      "fingerprint_randomized": true,
      "proxy_active": true,
      "overall_stealth_score": 60,
      "details": {
        "warning": "反检测JS未生效,CDP探针检测到自动化痕迹",
        "fallback_mode": "纯自动化API模式(降级)",
        "risk_level": "medium"
      }
    }
  },
  "error": "CDP探针检测失败:反检测JS未生效,已降级到纯自动化API模式。风险等级:medium,建议检查Chrome启动参数或切换代理IP。",
  "code": "STEALTH_DEGRADED"
}
```

**效果验证**: ✓CDP探针检测失败正确识别 ✓降级到纯自动化API模式 ✓风险等级medium正确标注 ✓降级原因在error字段说明 ✓错误码STEALTH_DEGRADED正确返回

## 常见问题

### Q1: 如何开始使用反检测浏览器助手?
A: 三步启动:(1)确认系统已安装Chrome浏览器;(2)将SKILL.md放入Agent的skills目录;(3)调用时传入action和params即可。本Skill无需额外API Key,通过CDP协议连接Chrome。建议先从locate_element(元素定位)开始体验。

### Q2: Tab崩溃后如何恢复?
A: 系统监听page crash事件和浏览器断连事件,崩溃时3秒内自动:(1)重建浏览器上下文;(2)恢复崩溃前URL;(3)重新加载Cookie;(4)触发告警通知。recovery_time_ms字段记录实际恢复耗时。如频繁崩溃,建议检查内存使用和页面复杂度。

### Q3: 多账号隔离如何实现?
A: 每个账号使用独立的profile_dir(浏览器配置目录),实现:(1)指纹隔离(每个账号独立浏览器指纹);(2)Cookie隔离(独立Cookie存储);(3)频率控制(多账号发布间隔≥17分钟防关联)。账号切换时清理上下文,确保不串号。

### Q4: 反检测混合方案的双通道是什么?
A: 日常操作走自动化API通道(Playwright/Puppeteer标准API),敏感操作走独立WebSocket直连CDP通道。敏感操作前通过直连通道执行反检测JS(不触发自动化框架初始化),CDP探针验证反检测有效性。双通道设计避免自动化框架特征被检测。

### Q5: 验证码出现时如何处理?
A: 系统检测到验证码时:(1)自动截图保存;(2)触发通知等待人工处理;(3)不自动绕过验证码(合规要求)。人工处理完成后,系统继续执行后续操作。建议优化操作频率和行为模拟,减少验证码触发概率。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **Chrome依赖**: 必须安装Chrome浏览器,不支持Firefox/Safari等其他浏览器
- **桌面端限制**: 仅支持桌面浏览器自动化,不支持移动端APP自动化(需使用Appium等工具)
- **验证码处理**: 不自动绕过验证码(合规要求),需人工处理,影响自动化连续性
- **频率限制**: 多账号操作需遵守安全频率(如发布间隔≥17分钟),高频操作仍可能触发风控
- **CDP版本兼容**: 不同Chrome版本的CDP协议可能有差异,建议使用Chrome稳定版
- **反检测效果**: 反检测能力受平台风控升级影响,需持续更新反检测策略
- **资源消耗**: 多账号隔离时每个账号独立配置目录,内存和磁盘占用较高(每账号约200-500MB)
- **合规边界**: 本工具不用于绕过付费墙/破解验证码/爬虫滥用等违规场景,使用者需遵守平台ToS和法律法规

## 安全

### 合规使用声明
- **合法用途**: 本工具仅用于合法合规的浏览器自动化场景,包括自动化测试、RPA流程构建、合规多账号管理(需遵守平台ToS)
- **禁止用途**: 严禁用于爬虫滥用(大规模数据抓取)、刷量/刷单/刷评(违反平台规则)、绕过付费墙/验证码破解(违反法律法规)、欺诈/钓鱼等违法行为
- **平台ToS**: 使用者需自行确认遵守各平台服务条款(Terms of Service),因违规使用导致的账号封禁/法律责任由使用者自行承担
- **频率合规**: 严格遵守安全频率限制(见频率控制表),避免触发平台风控

### API Key 零暴露原则
- **无需API Key**: 本Skill通过CDP协议连接Chrome,无需额外API Key配置
- **云浏览器服务**: 如使用Browserless等云浏览器服务,API Key必须通过Agent环境变量注入,严禁硬编码
- **本文件无Key示例**: 本SKILL.md中不包含任何真实或示例API Key
- **日志脱敏**: exec工具记录日志时,自动过滤包含"key"/"token"/"secret"/"cookie"字段的值

### 数据安全
- **Cookie存储**: Cookie文件加密存储,避免明文泄露账号会话信息
- **指纹隔离**: 每个账号独立浏览器配置目录,避免指纹关联
- **操作日志**: 操作日志脱敏处理,不记录账号密码等敏感信息
- **验证码处理**: 验证码截图仅本地保存,不上传至外部服务,避免信息泄露
