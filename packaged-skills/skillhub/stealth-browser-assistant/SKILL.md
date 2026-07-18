---
slug: stealth-browser-assistant
name: stealth-browser-assistant
version: "1.0.0"
displayName: "反检测浏览器助手"
summary: "一人管百号的浏览器自动化底座,指纹隔离+崩溃自愈+智能定位,告别封号掉线"
license: MIT
description: |-
  反检测浏览器助手——一人管百号的浏览器自动化底座,指纹隔离+崩溃自愈让浏览器永不掉线。

  核心能力: DOM蒸馏三树智能定位 / Tab崩溃3秒自动恢复 / 浏览器指纹防护 / 行为模拟 / 多账号隔离 / Cookie预热 / 端口竞争重试

  适用场景: 多账号矩阵运营者 / 自动化爬虫开发者 / RPA流程构建者 / 副业达人做浏览器自动化批量操作

  差异化: 三树数据(DOM+无障碍+快照)智能降级链定位,彻底解决元素失效痛点;崩溃3秒自愈恢复URL与Cookie;反检测双通道(日常API+敏感直连CDP),指纹隔离一人管百号不关联。

  触发关键词: 浏览器自动化、元素定位失败、Tab崩溃、反检测、指纹防护、行为模拟、多账号隔离
homepage: "https://skillhub.cn"
tags: [浏览器自动化, 多账号管理, 反检测, 效率工具]
tools: [read, exec]
---

# 反检测浏览器助手 Stealth Browser Assistant

智能浏览器自动化引擎,融合DOM蒸馏定位、稳定性增强、反检测混合方案,专为Agent浏览器自动化场景设计。

## 使用场景

1. 元素定位失败时:电商/社交等SPA前端更新导致CSS Hash选择器失效,需要智能降级定位
2. 浏览器Tab崩溃时:长时间运行中Tab意外关闭/崩溃,需要自动恢复到崩溃前状态
3. 反检测需求时:访问保护站点时浏览器被识别,需要增强反检测能力
4. 多账号隔离时:同一机器管理多个账号,需要指纹与Cookie隔离
5. 浏览器生命周期管理:统一管理浏览器启动/关闭/重启

## 工作流

### 方案A: DOM蒸馏定位

1. 通过CDP连接获取三树数据(DOM树+Accessibility树+DOMSnapshot)
2. 简化DOM树(过滤style/script/head等非内容元素)
3. 按绘制顺序过滤被遮挡的不可见元素
4. 优化树结构(移除无意义中间容器节点)
5. 按包围盒传播过滤被父元素覆盖的子元素
6. 分配交互索引(backendNodeId)生成selector_map
7. 按降级链定位元素: 无障碍角色→文本匹配→JS事件监听器→坐标点击
8. 返回定位结果+置信度评分

### 方案B: 浏览器稳定性保障

1. 浏览器管理器统一管理生命周期(启动/关闭/重启)
2. 注册Tab崩溃监听(page crash事件 + 浏览器断连事件)
3. 崩溃时重建浏览器上下文
4. 恢复崩溃前的URL
5. 重新加载Cookie
6. 端口竞争重试(Chrome重启时3次/500ms间隔)
7. 超时可配置(通过环境变量设置)
8. 操作前校验ref/key/fields参数完整性(防LLM幻觉)
9. Cookie预热(先访问首页建立Session再执行搜索)

### 方案C: 反检测混合方案

1. 启动系统Chrome(--remote-debugging-port + 反检测启动参数)
2. 通过CDP协议连接(日常操作通道)
3. 建立独立WebSocket直连CDP(敏感操作通道)
4. 敏感操作前通过直连通道执行反检测JS(不触发自动化框架初始化)
5. CDP探针检测(验证反检测有效性)
6. 操作分流(日常走自动化API,敏感走直连CDP)

### 多账号隔离

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

| 异常 | 处理 |
|:-----|:-----|
| DOM蒸馏CDP超时 | 10秒超时→2秒重试→降级到fallback_selectors |
| Tab崩溃 | 3秒内重建→恢复URL→重加载Cookie→触发告警通知 |
| 端口占用 | 3次重试/500ms间隔→失败则终止旧进程→重试 |
| CDP探针检测失败 | 记录日志→降级到纯自动化API模式→触发告警 |
| Cookie失效 | 检测→暂停操作→通知等待人工处理或Cookie保活 |
| 验证码出现 | 截图→通知→等待人工处理 |

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Chrome浏览器 | 运行时 | 必需 | 系统Chrome(用于反检测和CDP连接) |
| CDP协议 | 协议 | 必需 | Chrome DevTools Protocol(Chrome内置) |
| 浏览器自动化框架 | SDK | 可选 | Playwright/Puppeteer等 |

### API Key 配置
- 本Skill无需额外API Key配置

### 纯Markdown使用说明
需要系统安装Chrome浏览器。通过CDP协议连接Chrome,无需额外API Key。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 智能定位发布按钮

场景:电商网站前端更新导致CSS类名变化,原选择器失效。

执行流程:
1. 通过CDP获取页面DOM+无障碍树
2. 简化DOM树并过滤不可见元素
3. 按降级链定位:无障碍角色button + 文本"发布" → 命中
4. 返回:method="ax_role"(不依赖Hash类名),confidence=0.92

### 示例2: Tab崩溃自动恢复

场景:长时间运行中浏览器Tab意外崩溃。

执行流程:
1. 监听到crash事件
2. 重建浏览器上下文
3. 恢复崩溃前URL
4. 重新加载Cookie
5. 3秒内完成恢复,继续执行任务

### 示例3: 反检测混合模式

场景:访问受保护站点,常规自动化被识别。

执行流程:
1. 启动系统Chrome(反检测启动参数)
2. 建立独立WebSocket直连CDP
3. 敏感操作前通过直连通道注入反检测JS
4. CDP探针验证反检测有效
5. 日常操作走自动化API,敏感操作走直连CDP
