---
slug: web-crawler-engine-free
name: web-crawler-engine-free
version: "1.0.0"
displayName: 网页抓取引擎(免费版)
summary: 轻量级网页与社区数据抓取工具，支持本地归档、搜索查询与新鲜度检查。
license: MIT
edition: free
description: |-
  网页抓取引擎免费版是一套面向个人开发者与小型团队的数据抓取与归档工具，帮助用户高效采集网页内容与社区消息并建立本地可搜索的归档库。

  核心能力：提供网页内容抓取模板、社区频道消息归档、本地全文搜索、数据新鲜度检查、只读 SQL 查询接口。所有数据存储在本地，确保隐私与安全。

  适用场景：技术资料离线归档、社区讨论采集与分析、竞品内容监控、研究数据收集、个人知识库构建。

  差异化：以中文场景化表达重构数据抓取流程，将操作浓缩为"检查新鲜度-同步数据-查询归档-导出结果"四步流程，附带安全边界说明与隐私保护指南。

  触发关键词：网页抓取、数据归档、全文搜索、社区采集、新鲜度检查、本地存储、SQL查询
tags:
- 数据抓取
- 集成工具
- 信息检索
- 免费版
tools:
- read
- exec
---

# 网页抓取引擎（免费版）

## 概述

在信息快速流转的今天，将重要的网页内容与社区讨论归档到本地、建立可搜索的知识库，是避免信息丢失、提升检索效率的关键。本引擎将数据抓取与归档流程整理为结构化指南，帮助你在数分钟内完成数据采集与检索。

免费版聚焦于**日常使用最高频的四大能力**：网页内容抓取、社区消息归档、本地全文搜索、数据新鲜度检查。

## 核心能力

### 能力一：网页内容抓取

提供结构化的网页内容抓取模板，支持 HTML 解析、文本提取、链接发现。

```bash
# 抓取网页并提取正文
curl -s "https://example.com/article" | \
  python -c "
import sys, html.parser
class TextExtractor(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.skip = True
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.skip = False
    def handle_data(self, data):
        if not self.skip: self.text.append(data.strip())
p = TextExtractor()
p.feed(sys.stdin.read())
print(' '.join(t for t in p.text if t))
"
```

### 能力二：社区消息归档

将社区频道（如 Discord、Slack）的消息归档到本地数据库，建立可检索的历史记录。

| 归档维度 | 说明 | 存储字段 |
|:---------|:-----|:---------|
| 消息内容 | 正文与附件 URL | content, attachments |
| 发送者 | 用户名与 ID | author, author_id |
| 时间戳 | 发送时间与编辑时间 | timestamp, edited_at |
| 频道信息 | 频道名与 ID | channel, channel_id |
| 回复关系 | 被回复消息 ID | reply_to |

### 能力三：本地全文搜索

基于 SQLite FTS5 建立全文索引，支持快速关键词检索与高亮显示。

```bash
# 搜索归档消息（限制结果数量）
search --limit 20 "关键词"

# 按频道与时间范围搜索
messages --channel '#tech-news' --days 7

# 查看最近私信
dms --last 20
```

### 能力四：数据新鲜度检查

在查询前检查归档数据的新鲜度，避免使用过时数据回答问题。

```bash
# 检查归档状态
status --json

# 诊断工具
doctor

# 输出示例：
# {
#   "last_sync": "2026-07-18T10:00:00Z",
#   "freshness": "fresh",     # fresh / stale / unknown
#   "message_count": 15423,
#   "channels": 12,
#   "gaps": []
# }
```

## 使用场景

### 场景一：技术资料离线归档

开发者将常参考的技术文档、博客文章抓取到本地，断网时也可查阅。

### 场景二：社区讨论采集

将技术社区的优质讨论归档，使用全文搜索快速查找历史解决方案。

### 场景三：研究数据收集

研究人员批量采集特定主题的网页内容，建立本地研究语料库。

## 快速开始

**典型提问模板**：

```
我想抓取某个技术博客的全部文章并归档到本地，如何实现？
```

```
归档的社区消息如何按关键词搜索并限定时间范围？
```

```
如何检查我的归档数据是否是最新的？
```

Agent 会根据问题匹配对应知识条目，输出包含操作步骤、命令模板、注意事项的完整回答。

## 配置示例

### 归档数据库结构

```sql
-- 归档消息表
CREATE TABLE messages (
    id TEXT PRIMARY KEY,
    channel_id TEXT NOT NULL,
    channel_name TEXT,
    author_id TEXT NOT NULL,
    author_name TEXT,
    content TEXT,
    attachments TEXT,        -- JSON 数组
    timestamp DATETIME NOT NULL,
    edited_at DATETIME,
    reply_to TEXT
);

-- 全文搜索索引
CREATE VIRTUAL TABLE messages_fts USING fts5(
    content, author_name, channel_name,
    content='messages',
    content_rowid='rowid'
);

-- 频道元数据
CREATE TABLE channels (
    channel_id TEXT PRIMARY KEY,
    channel_name TEXT NOT NULL,
    last_synced DATETIME,
    message_count INTEGER DEFAULT 0
);
```

### 新鲜度策略配置

```yaml
# 新鲜度检查策略
freshness:
  stale_threshold_hours: 24    # 超过24小时标记为stale
  auto_sync: false              # 免费版不自动同步
  sync_on_query: false          # 查询时不自动触发同步

search:
  default_limit: 20             # 默认返回结果数
  max_limit: 100                # 单次最大结果数
  highlight: true               # 关键词高亮
```

## 最佳实践

### 实践一：先检查新鲜度再查询

回答时效性问题时，先检查归档新鲜度。数据过时时提示用户手动同步或直接查询在线源。

### 实践二：限制查询结果数量

无限制的查询会消耗大量内存与时间，默认限制 20 条，按需调整上限。

### 实践三：只读查询保护数据

归档数据应视为只读，避免误操作修改或删除。需要修改时使用 `--unsafe --confirm` 并经过人工审核。

### 实践四：隐私数据不外传

归档中可能包含用户私信等敏感信息，导出快照时务必排除敏感内容与用户凭据。

### 实践五：定期清理过期数据

设置保留策略，定期清理超过保留期限的归档数据，控制存储空间增长。

## 常见问题

### Q1：抓取被网站封禁怎么办？

遵守网站的 robots.txt 与服务条款，设置合理的请求间隔（建议 1-3 秒），使用 User-Agent 标识身份。高频抓取应使用官方 API 而非网页爬取。

### Q2：全文搜索不返回结果？

检查 FTS 索引是否已正确创建并同步。使用 `doctor` 命令诊断索引状态，必要时重建索引。

### Q3：归档数据占用空间太大？

对历史数据设置保留期限，过期数据归档到压缩文件后从主库删除。附件 URL 仅存储链接不下载文件。

### Q4：如何只同步特定频道？

使用 `--channel` 参数指定频道，避免全量同步消耗过多时间与带宽。

### Q5：数据新鲜度显示 unknown？

表示从未同步过该数据源。首次使用需手动执行同步命令建立基线数据。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **存储**: 本地磁盘（SQLite 数据库）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| SQLite | 数据库 | 必需 | Python 内置 sqlite3 模块 |
| curl / HTTP 客户端 | 工具 | 推荐 | 系统自带或安装 |
| Python 3.8+ | 运行时 | 推荐 | 官方网站下载 |

### API Key 配置
- **社区 Bot Token**: 若需归档社区消息，通过环境变量注入对应平台的 Bot Token
- **禁止**: 在代码、脚本、SKILL.md 中硬编码任何凭据
- **禁止**: 提取用户 Token 冒充用户身份访问平台
- **推荐**: 仅使用 Bot API 合法采集公开数据

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，核心功能需要exec执行抓取与查询命令）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent完成数据抓取与归档查询

## 免费版限制

本免费体验版限制以下高级功能：
- 增量同步与自动刷新调度（仅专业版提供）
- SQL 高级分析与聚合统计（仅专业版提供）
- 批量抓取与并发调度（仅专业版提供）
- 多格式数据导出（CSV/JSON/Excel）（仅专业版提供）
- 监控告警与同步异常通知（仅专业版提供）
- 分布式归档与云端备份（仅专业版提供）

解锁全部功能请使用专业版：web-crawler-engine-pro
