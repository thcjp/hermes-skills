---
slug: scrape-web
name: scrape-web
version: "1.0.0"
displayName: Scrape Web
summary: 使用 Python + Scrapling 获取网页内容，支持简单选择器
license: MIT-0
description: |-
  使用 Python + Scrapling 获取网页内容，支持简单选择器

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: web, 支持简单选择, python, 使用, scrape, 获取网页内容, scrapling
tags:
- Research
tools:
- read
- exec
---

# Scrape Web

使用 Scrapling 获取网页内容，返回纯文本或选择器结果。

## 安装依赖

```bash
pip install "scrapling[all]"
scrapling install
pip install httpx
```

## 用法

### 1) 直接抓取纯文本

```bash
python scripts/scrape_web.py --url "https://example.com"
```

### 2) 使用 CSS 选择器

```bash
python scripts/scrape_web.py --url "https://example.com" --selector "title::text"
```

### 3) 保存到文件

```bash
python scripts/scrape_web.py --url "https://example.com" --out "output.txt"
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
