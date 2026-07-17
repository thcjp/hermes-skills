---
slug: rss-ai-reader
name: rss-ai-reader
version: "1.0.0"
displayName: Rss Ai Reader
summary: "📰 RSS AI 阅读器 — 自动抓取订阅、LLM生成摘要、多渠道推送！ 支持 Claude/OpenAI 生成中文摘要，推送到飞书/Telegram/Email。
  触发条件: 用户要求订阅RS"
license: MIT
description: |-
  📰 RSS AI 阅读器 — 自动抓取订阅、LLM生成摘要、多渠道推送！ 支持 Claude/OpenAI 生成中文摘要，推送到飞书/Telegram/Email。
  触发条件: 用户要求订阅RS...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 阅读器, reader, 多渠道推送, 自动抓取订阅, 支持, 生成摘要, telegram, rss
tags: '[''Communication'', ''Research'']'
tools: '[read, exec]'
---

# Rss Ai Reader

自动抓取 RSS 订阅 → LLM 生成中文摘要 → 推送到 IM

## ✨ 核心功能

* 📡 自动抓取 RSS/Atom feeds
* 🤖 Claude/OpenAI 生成中文摘要
* 📬 多渠道推送：飞书、Telegram、Email
* 💾 SQLite 去重，不重复推送
* ⏰ 支持定时任务

## 🚀 快速开始

```bash
git clone https://github.com/BENZEMA216/rss-reader.git ~/rss-reader
cd ~/rss-reader && pip install -r requirements.txt

cp config.yaml my_config.yaml

python main.py --once              # 单次执行
python main.py                     # 启动定时任务
python main.py --stats             # 查看统计
```

## 📝 配置示例

```yaml
feeds:
  - name: "Hacker News"
    url: "https://hnrss.org/frontpage"
    category: "tech"
  - name: "阮一峰周刊"
    url: "https://www.ruanyifeng.com/blog/atom.xml"
    category: "tech"

llm:
  provider: "claude"  # 或 "openai"
  model: "claude-sonnet-4-20250514"
  api_key: "${ANTHROPIC_API_KEY}"

notify:
  feishu:
    enabled: true
    webhook_url: "${FEISHU_WEBHOOK}"
```

## 📬 支持的推送渠道

| 渠道 | 配置项 | 说明 |
| --- | --- | --- |
| **飞书** | `webhook_url` | 群机器人 Webhook |
| **Telegram** | `bot_token` + `chat_id` | Bot API |
| **Email** | SMTP 配置 | 支持 Gmail 等 |

## 🔧 命令行参数

```bash
python main.py [options]

--config, -c  配置文件路径 (默认: config.yaml)
--once        只执行一次
--stats       显示统计信息
--db          数据库路径 (默认: rss_reader.db)
```

## 💡 使用场景

1. **技术博客监控** — 订阅 HN、阮一峰、V2EX 等
2. **新闻早报** — 每天定时推送摘要到飞书群
3. **竞品监控** — 订阅竞品博客，自动摘要
4. **论文追踪** — 订阅 arXiv，AI 帮你筛选

## 📊 输出效果

飞书消息示例：

```text
📰 Hacker News

**Why SQLite is Taking Over**

📝 SQLite 正在从嵌入式数据库扩展到更多应用场景。
文章分析了其在边缘计算、移动应用中的优势...

[🔗 阅读原文]
```

---

## ☕ 支持作者

* **GitHub Sponsors**: [@BENZEMA216](https://github.com/sponsors/BENZEMA216)
* **Buy Me a Coffee**: [buymeacoffee.com/benzema216](https://buymeacoffee.com/benzema216)

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
