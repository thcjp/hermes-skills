---
slug: rss-ai-reader
name: rss-ai-reader
version: "1.0.0"
displayName: Rss Ai Reader
summary: "📰 RSS AI 阅读器 — 自动抓取订阅、LLM生成摘要、多渠道推送！ 支持 ai-assistant/llm-provider 生成中文摘要，推送到飞书/Telegram/Email。
  触发条件: 用户要求订阅RS"
license: MIT
description: |-
  📰 RSS AI 阅读器 — 自动抓取订阅、LLM生成摘要、多渠道推送！ 支持 ai-assistant/llm-provider 生成中文摘要，推送到飞书/Telegram/Email。触发条件: 用户要求订阅RS。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags: '[''Communication'', ''Research'']'
tools:
  - read
  - exec
---

# Rss Ai Reader

自动抓取 RSS 订阅 → LLM 生成中文摘要 → 推送到 IM

## 核心能力

* 📡 自动抓取 RSS/Atom feeds
* 🤖 ai-assistant/llm-provider 生成中文摘要
* 📬 多渠道推送：飞书、Telegram、Email
* 💾 SQLite 去重，不重复推送
* ⏰ 支持定时任务

## 使用流程

```bash
git clone https://github.com/BENZEMA216/rss-reader.git ~/rss-reader
cd ~/rss-reader && pip install -r requirements.txt

cp config.yaml my_config.yaml

python main.py --once              # 单次执行
python main.py                     # 启动定时任务
python main.py --stats             # 查看统计
```

## 示例

```yaml
feeds:
  - name: "Hacker News"
    url: "https://hnrss.org/frontpage"
    category: "tech"
  - name: "阮一峰周刊"
    url: "https://www.ruanyifeng.com/blog/atom.xml"
    category: "tech"

llm:
  provider: "ai-assistant"  # 或 "llm-provider"
  model: "ai-assistant-sonnet-4-20250514"
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

## 适用场景

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
- **Agent平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Rss Ai Reader？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Rss Ai Reader有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
- 性能取决于底层模型能力
