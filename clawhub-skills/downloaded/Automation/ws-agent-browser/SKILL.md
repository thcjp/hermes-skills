---
slug: ws-agent-browser
name: ws-agent-browser
version: "1.0.0"
displayName: Agent Browser
summary: 浏览器智能控制。自动化操作、截图、填表、数据抓取。
license: MIT-0
description: |-
  浏览器智能控制。自动化操作、截图、填表、数据抓取。

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 截图, 填表, 数据抓取, 自动化操作, browser, 浏览器智能控, agent
tags:
- Automation
tools:
- read
- exec
---

# Agent Browser

智能浏览器控制助手。

## 功能

### 📸 页面操作

* 打开网页
* 截图/录屏
* 点击/输入
* 滚动/导航

### 🤖 自动化

* 表单自动填写
* 批量操作
* 定时任务
* 登录认证

### 📥 数据抓取

* 提取网页内容
* 表格数据导出
* 动态内容抓取
* 定期监控

### ✅ 测试

* UI 测试
* 回归测试
* 性能监控

## 使用方式

```text
帮我打开这个网页并截图
URL：https://example.com

自动化操作：帮我填写这个表单
字段：姓名、电话、地址

抓取数据：把这个页面的表格导出成CSV
URL：https://example.com/data

监控：每小时检查这个页面有无更新
URL：https://example.com/status
```

## 浏览器配置

Skill平台 内置浏览器功能。

**环境要求：**

* 需要在有浏览器的机器上运行（如本地电脑）
* 支持 Chrome/Brave/Edge/Chromium

**使用方式：**

* 直接告诉我："打开某网页" / "截图" / "填表"
* 使用 `browser` 工具进行操作

**可用操作：**

* `browser_open` - 打开网页
* `browser_snapshot` - 页面快照
* `browser_screenshot` - 截图
* `browser_click` - 点击元素
* `browser_type` - 输入文字
* `browser_evaluate` - 执行脚本

## 安全说明

* 🔒 敏感操作需要确认
* 📝 操作日志可追溯
* ⚠️ 遵守网站 robots.txt

---

**数据存储**:

* 截图/录屏：`/workspace/data/browser/screenshots/`
* 抓取数据：`/workspace/data/browser/data/`
* 配置：`/workspace/data/browser/config.json`

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
