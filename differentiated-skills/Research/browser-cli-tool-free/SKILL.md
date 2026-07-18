---
slug: browser-cli-tool-free
name: browser-cli-tool-free
version: "1.0.0"
displayName: 浏览器CLI工具-免费版
summary: 基于Playwright的浏览器自动化CLI,支持签到、填表、截图与信息抓取,适合个人用户
license: MIT
edition: free
description: |-
  浏览器自动化命令行工具,提供导航、交互、信息获取与截图能力,
  适合签到、填表、信息抓取等需要控制浏览器的任务。

  核心能力:
  - 页面导航与历史控制
  - 基于ref引用与CSS选择器的元素交互
  - 文本、HTML、属性等信息提取
  - 截图与页面快照

  适用场景:
  - 个人用户的每日签到与表单填写
  - 网页信息抓取与数据收集
  - 独立开发者的自动化工作流

  差异化:免费版提供核心浏览器自动化能力,操作直观,适合个人轻量场景。

  触发关键词: 浏览器自动化, 签到, 填表, 截图, 信息抓取, agent-browser, cli
tags:
- 研究工具
- 浏览器自动化
- 自动化
tools:
- read
- exec
---

# 浏览器CLI工具(免费版)

## 概述

本工具是一个浏览器自动化命令行工具,提供页面导航、元素交互、信息获取与截图等能力,适合签到、填表、信息抓取等需要控制浏览器的任务。免费版面向个人用户,提供直观的命令行操作体验。

### 适用场景判断

| 场景 | 是否推荐本工具 |
|:-----|:--------------|
| 自动化浏览器操作(签到/填表/点击) | 推荐 |
| 需要截图或抓取页面信息 | 推荐 |
| 需要可视化查看浏览器界面 | 推荐(配合 `--headed`) |
| 仅需纯API数据请求(无页面交互) | 不推荐(改用 curl/httpie) |

## 核心能力

### 命令总览

| 命令分类 | 命令示例 | 说明 |
|:-------|:-----|:-----|
| 导航 | `open <url>` / `back` / `forward` / `reload` | 页面跳转控制 |
| 交互 | `click` / `fill` / `type` / `select` / `check` | 元素操作 |
| 获取信息 | `snapshot` / `get text` / `get html` / `screenshot` | 信息提取 |
| 元素定位 | `find role` / `find text` / `find label` | 多种定位方式 |

## 使用场景

### 场景一:每日签到任务

个人用户每日完成站点签到。

```bash
# 打开签到页面
agent-browser open https://example.com/checkin

# 获取页面快照,查看可交互元素
agent-browser snapshot

# 点击签到按钮(根据 snapshot 输出的 ref)
agent-browser click @eXX

# 等待页面响应
sleep 2

# 再次快照确认结果
agent-browser snapshot

# 关闭浏览器
agent-browser close
```

### 场景二:自动填表

自动填写并提交表单。

```bash
agent-browser open https://example.com/form
agent-browser snapshot

# 通过 label 定位并填写
agent-browser find label "用户名" fill "myuser"
agent-browser find label "密码" fill "mypassword"

# 通过 ARIA 角色点击提交按钮
agent-browser find role button click --name "提交"
```

### 场景三:定时签到(配合 cron)

将签到脚本加入定时任务,实现每日自动签到。

```bash
# 创建脚本 ~/.skill-platform/scripts/daily-checkin.sh
cat > ~/.skill-platform/scripts/daily-checkin.sh << 'EOF'
#!/bin/bash
agent-browser open https://example.com/checkin
sleep 2
agent-browser find role button click --name "签到"
agent-browser screenshot /tmp/checkin_$(date +%Y%m%d).png
agent-browser close
EOF

chmod +x ~/.skill-platform/scripts/daily-checkin.sh

# 加入 crontab(每天 9:00 执行)
# crontab -e
# 0 9 * * * ~/.skill-platform/scripts/daily-checkin.sh
```

## 快速开始

### 1. 安装

如果 `agent-browser` 未安装:

```bash
npm install -g agent-browser
agent-browser install
```

### 2. 基础工作流

```bash
# 打开网页
agent-browser open <url>

# 获取页面可访问性树(推荐)
agent-browser snapshot

# 点击元素(用 ref 引用)
agent-browser click @<ref>

# 填入内容
agent-browser fill @<ref> "内容"

# 关闭浏览器
agent-browser close
```

## 配置示例

### 导航命令

```bash
agent-browser open <url>      # 打开URL(别名:goto, navigate)
agent-browser back            # 后退
agent-browser forward         # 前进
agent-browser reload          # 刷新
```

### 交互命令

```bash
agent-browser click <sel>                    # 点击
agent-browser dblclick <sel>                 # 双击
agent-browser fill <sel> "text"              # 填入(清空后填)
agent-browser type <sel> "text"              # 输入(追加)
agent-browser select <sel> <value>           # 选择下拉选项
agent-browser check <sel>                    # 勾选复选框
agent-browser uncheck <sel>                  # 取消勾选
agent-browser press <key>                    # 按键(Enter/Tab/Escape等)
```

### 获取信息

```bash
agent-browser snapshot                       # 获取可访问性树(推荐)
agent-browser get text <sel>                 # 获取文本
agent-browser get html <sel>                 # 获取HTML
agent-browser get value <sel>                # 获取输入值
agent-browser get title                      # 获取页面标题
agent-browser get url                        # 获取当前URL
agent-browser screenshot [path]              # 截图
agent-browser screenshot --annotate          # 带标注的截图
```

### 元素定位(三种方式)

**方式一:通过 snapshot 输出的 ref 引用(推荐)**

```bash
agent-browser click @e14
agent-browser fill @e13 "hello"
```

**方式二:使用 CSS 选择器**

```bash
agent-browser click "#submit"
agent-browser fill "input[name='email']" "test@test.com"
```

**方式三:使用 ARIA 角色查找**

```bash
agent-browser find role button click --name "Submit"
agent-browser find text "Sign In" click
agent-browser find label "Email" fill "test@test.com"
agent-browser find placeholder "Search" type "query"
```

## 最佳实践

1. **先 snapshot 再操作**:每次页面变化后重新获取 ref,避免引用失效。
2. **添加等待**:页面加载需要时间,用 `sleep 2` 或等待命令。
3. **保持浏览器开启**:多个操作可在同一浏览器会话中完成,减少启动开销。
4. **完成后关闭**:用 `agent-browser close` 释放资源。
5. **优先使用 ref**:相比 CSS 选择器,ref 更稳定,不易因页面结构变化而失效。
6. **使用 `find` 提升可读性**:`find label "用户名"` 比硬编码选择器更直观。

## 常见问题

### Q1: snapshot 后 ref 找不到元素?
页面 DOM 可能已变化,需要重新执行 `agent-browser snapshot` 获取最新 ref。在异步加载的页面上,建议先 `sleep 2` 等待加载完成。

### Q2: 元素被遮挡无法点击?
- 尝试滚动到元素位置后再点击
- 检查是否有弹窗遮挡,先关闭弹窗
- 使用 `find role button click --name "xxx"` 替代 ref

### Q3: 安装失败怎么办?
```bash
# 检查 Node.js 版本(需 >= 18)
node --version

# 重新安装
npm uninstall -g agent-browser
npm install -g agent-browser
agent-browser install
```

### Q4: 免费版与专业版的区别?
免费版提供核心浏览器自动化能力,适合个人签到、填表等轻量任务。专业版在此基础上提供批量任务调度、并发会话、监控告警、企业集成等高阶能力。

### Q5: 如何调试脚本?
```bash
# 使用有头模式可视化调试
agent-browser --headed open https://example.com
# 截图查看当前状态
agent-browser screenshot debug.png
```

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: >= 18.0.0

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| agent-browser | CLI 工具 | 必需 | `npm install -g agent-browser` |
| Chromium | 运行时 | 必需 | `agent-browser install` 自动下载 |
| Node.js | 运行环境 | 必需 | 系统包管理器安装 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本 Skill 基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
