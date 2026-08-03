---
slug: agent-browser-cli
name: agent-browser-cli
version: "1.0.0"
displayName: Agent Browser CLI
summary: 使用 agent-browser CLI 进行浏览器自动化。用于签到、填表、截图、信息抓取等需要控制浏览器的任务。触发条件：(1) 用户要求自动化浏览器操作
  (2) 需要签到、填表、点击按钮 (...
license: MIT
description: |-
  使用 agent-browser CLI 进行浏览器自动化。用于签到、填表、截图、信息抓取等需要控制浏览器的任务。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
- Research
- Automation
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Agent Browser CLI

Vercel 出品的浏览器自动化 CLI，基于 Playwright，比标准浏览器工具更快更灵活。

## 快速开始

```bash
agent-browser open <url>     # 打开网页
agent-browser snapshot       # 获取页面可访问性树
agent-browser click @<ref>   # 点击元素（用ref引用）
agent-browser fill @<ref> "内容"  # 填入内容
agent-browser close         # 关闭浏览器
```

## 常用命令

### 导航

```bash
agent-browser open <url>      # 打开URL（别名：goto, navigate）
agent-browser back            # 后退
agent-browser forward         # 前进
agent-browser reload          # 刷新
```

### 交互

```bash
agent-browser click <sel>                    # 点击
agent-browser dblclick <sel>                  # 双击
agent-browser fill <sel> "text"               # 填入（清空后填）
agent-browser type <sel> "text"               # 输入（追加）
agent-browser select <sel> <value>             # 选择下拉选项
agent-browser check <sel>                      # 勾选复选框
agent-browser uncheck <sel>                   # 取消勾选
agent-browser press <key>                      # 按键（Enter, Tab, Escape等）
```

### 获取信息

```bash
agent-browser snapshot              # 获取可访问性树（推荐）
agent-browser get text <sel>        # 获取文本
agent-browser get html <sel>        # 获取HTML
agent-browser get value <sel>       # 获取输入值
agent-browser get title             # 获取页面标题
agent-browser get url               # 获取当前URL
agent-browser screenshot [path]     # 截图
agent-browser screenshot --annotate  # 带标注的截图
```

### 元素定位

通过 snapshot 输出的 ref（如 @e14）直接引用：

```bash
agent-browser click @e14
agent-browser fill @e13 "hello"
```

或使用 CSS 选择器：

```bash
agent-browser click "#submit"
agent-browser fill "input[name='email']" "test@test.com"
```

或使用 ARIA 角色查找：

```bash
agent-browser find role button click --name "Submit"
agent-browser find text "Sign In" click
agent-browser find label "Email" fill "test@test.com"
agent-browser find placeholder "Search" type "query"
```

## 典型工作流

### 1. 签到任务

```bash
agent-browser open <签到页面URL>

agent-browser snapshot

agent-browser click @eXX

sleep 2
agent-browser snapshot
```

### 2. 填表任务

```bash
agent-browser open <表单URL>
agent-browser snapshot

agent-browser find label "用户名" fill "myuser"
agent-browser find label "密码" fill "mypassword"
agent-browser find role button click --name "提交"
```

### 3. 定时签到（配合cron）

创建脚本 `~/.skill-platform/scripts/daily-checkin.sh`：

```bash
#!/bin/bash
agent-browser open <签到URL>
sleep 2
agent-browser find role button click --name "签到"
agent-browser screenshot /tmp/checkin_$(date +%Y%m%d).png
agent-browser close
```

## 注意事项

1. **先 snapshot 再操作** - 每次页面变化后重新获取 ref
2. **添加等待** - 页面加载需要时间，用 `sleep 2` 或等待
3. **保持浏览器开启** - 多个操作可以在同一浏览器会话中完成
4. **完成后关闭** - 用 `agent-browser close` 释放资源

## 依赖说明

如果 agent-browser 未安装：

```bash
npm install -g agent-browser
agent-browser install
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 使用 agent-browser CLI 进行浏览器自动化
- 用于签到、填表、截图、信息抓取等需要控制浏览器的任务
- 触发条件：(1) 用户要求自动化浏览器操作
  (2) 需要签到、填表、点击按钮 (
- 触发关键词: 填表, 使用, browser, agent, 进行浏览器自, 用于签到, 动化, cli

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Agent Browser CLI？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Agent Browser CLI有什么限制？
A: 请参考已知限制章节了解具体限制。
