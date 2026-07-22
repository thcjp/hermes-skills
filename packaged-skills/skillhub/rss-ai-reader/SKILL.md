---
slug: "rss-ai-reader"
name: "rss-ai-reader"
version: "1.0.0"
displayName: "RSS AI 摘要推送"
summary: "RSS自动抓取与LLM摘要生成,推送飞书/Telegram/Email,SQLite去重与定时任务"
license: "MIT"
description: |-
  RSS AI 阅读器。自动抓取 RSS/Atom 订阅源,通过 ai-assistant 或 llm-provider 生成中文摘要,
  并推送到飞书、Telegram、Email 三个渠道。基于 SQLite 存储实现条目去重,避免重复推送。
  支持单次执行与定时任务两种运行模式,通过命令行参数控制执行行为。
  覆盖五大核心能力:Feed 抓取(支持 RSS 2.0 与 Atom 1.0)、LLM 摘要生成(中文输出、长度可控)、
  多渠道推送(飞书 Webhook 与 Telegram Bot 与 SMTP Email)、SQLite 去重(按 feed URL 与条目 ID)、
  定时任务(cron 式调度)。适用于技术博客监控、新闻早报推送、竞品动态追踪、论文筛选等场景。
  基于 Markdown 指令驱动,需配合 Python 运行环境与对应推送渠道的凭证配置。
tags:
  - 研发工具
  - Research
  - Automation
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
---
# RSS AI 摘要推送

自动抓取 RSS/Atom 订阅源,通过 LLM 生成中文摘要,推送到飞书、Telegram、Email。基于 SQLite 去重,支持定时任务。

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Python 环境**: Python 3.9 及以上,需安装 feedparser、requests、PyYAML 等依赖

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供,或配置 ai-assistant / llm-provider 的 API Key |
| 飞书 Webhook | 凭证 | 可选 | 飞书群机器人配置后获取 Webhook URL |
| Telegram Bot Token | 凭证 | 可选 | 通过 @BotFather 创建 Bot 获取 token 与 chat_id |
| SMTP 配置 | 凭证 | 可选 | 邮件服务商提供的 SMTP 服务器、端口、账号密码 |

### API Key 配置
- LLM API Key 通过环境变量注入(如 ANTHROPIC_API_KEY),在配置文件 llm 节点引用
- 飞书 Webhook URL 通过环境变量 FEISHU_WEBHOOK 注入
- Telegram Bot Token 与 Chat ID 通过环境变量 TELEGRAM_BOT_TOKEN 与 TELEGRAM_CHAT_ID 注入
- SMTP 凭证通过环境变量 SMTP_HOST、SMTP_USER、SMTP_PASS 注入

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于 Markdown 的 AI Skill,通过自然语言指令驱动 Agent 执行 Python 脚本完成任务

## 核心能力

### 1. RSS/Atom Feed 抓取
- **协议支持**: 兼容 RSS 2.0 与 Atom 1.0 两种主流订阅协议
- **多源管理**: 配置文件中以列表形式维护多个 feed,每个 feed 含 name、url、category 三个字段
- **分类标记**: 通过 category 字段对 feed 分组(如 tech、news、research),便于后续按类筛选
- **抓取容错**: 单个 feed 抓取失败不中断整体流程,记录失败源并继续抓取下一个
- **条目解析**: 从 feed 中提取标题、链接、发布时间、正文摘要等字段供 LLM 处理

**输入**: 用户提供RSS/Atom Feed 抓取所需的指令和必要参数。
**输出**: 返回RSS/Atom Feed 抓取的执行结果,包含操作状态和输出数据。

### 2. LLM 中文摘要生成
- **双 Provider 支持**: 支持 ai-assistant 与 llm-provider 两种后端,在配置文件 llm.provider 字段切换
- **中文输出**: 无论原文语言,摘要统一输出为中文,降低阅读门槛
- **长度可控**: 通过 prompt 约束摘要长度(默认 3 到 5 句),避免过长影响推送体验
- **批量处理**: 对每批新条目逐条生成摘要,单条失败不影响其他条目
- **模型选择**: 通过 llm.model 字段指定具体模型(如 ai-assistant-sonnet-4-20250514)

**输入**: 用户提供LLM 中文摘要生成所需的指令和必要参数。
### 3. 多渠道推送
- **飞书**: 通过群机器人 Webhook 推送,消息含标题、摘要、原文链接,支持富文本卡片格式
- **Telegram**: 通过 Bot API 推送到指定 chat_id,消息含标题、摘要、原文链接
- **Email**: 通过 SMTP 发送邮件,正文含标题、摘要、原文链接,支持 Gmail 等服务商
- **多渠道组合**: 可同时启用多个渠道,同一摘要推送到飞书与 Telegram 等组合
- **推送格式统一**: 三个渠道的推送内容结构一致(标题 + 摘要 + 原文链接),便于跨平台阅读

**输入**: 用户提供多渠道推送所需的指令和必要参数。
**输出**: 返回多渠道推送的执行结果,包含操作状态和输出数据。

### 4. SQLite 去重
- **去重维度**: 按 feed URL 与条目 ID(或 GUID)联合去重,确保同一篇文章不重复推送
- **持久存储**: 去重记录存储在 SQLite 数据库(默认 rss_reader.db),跨进程持久化
- **增量抓取**: 每次执行时只处理数据库中不存在的新条目,已推送的自动跳过
- **统计查询**: 通过 --stats 参数查看已处理条目数、各 feed 抓取量等统计信息
- **数据库路径可配**: 通过 --db 参数或配置文件指定数据库路径

**输出**: 返回SQLite 去重的执行结果,包含操作状态和输出数据。
### 5. 定时任务
- **单次执行**: 通过 --once 参数只执行一轮抓取与推送,适合手动触发或外部调度
- **定时循环**: 不加 --once 参数时启动定时任务,按配置文件的间隔自动循环执行
- **cron 集成**: 可配合系统 cron 或 Agent 平台的调度能力实现每日定时推送
- **状态查看**: 通过 --stats 参数查看历史执行统计,辅助调整调度频率

#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 技术博客监控 | Hacker News、阮一峰、V2EX 等 feed 列表 | 新文章中文摘要推送到飞书群 |
| 新闻早报推送 | 多个新闻源 feed,每日定时执行 | 每日早间飞书群收到摘要合集 |
| 竞品动态追踪 | 竞品官方博客 feed 列表 | 竞品更新摘要推送到 Telegram |
| 论文筛选 | arXiv 特定分类 feed | 论文中文摘要推送到 Email |

**不适用于**: 需要原文全文推送的场景(本 Skill 只生成摘要);需要实时推送的场景(定时任务有执行间隔);需要非中文摘要输出的场景。

## 使用流程

1. **准备运行环境**: 确认 Python 3.9 已安装,克隆项目并安装依赖(`pip install -r requirements.txt`)
2. **创建配置文件**: 复制 config.yaml 为 my_config.yaml,填入 feed 列表、llm 配置、推送渠道配置
3. **配置环境变量**: 将 LLM API Key、飞书 Webhook URL、Telegram Token 等凭证设为环境变量
4. **单次测试执行**: 运行 `python main.py --config my_config.yaml --once` 验证抓取与推送链路
5. **查看执行统计**: 运行 `python main.py --stats` 确认条目已入库与去重生效
6. **启动定时任务**: 测试通过后运行 `python main.py --config my_config.yaml` 启动定时循环
7. **按需调整**: 根据推送效果调整 feed 列表、摘要长度、推送频率

#
## 配置文件结构

```yaml
feeds:
  - name: "Hacker News"
    url: "https://hnrss.org/frontpage"
    category: "tech"
  - name: "阮一峰周刊"
    url: "https://www.ruanyifeng.com/blog/atom.xml"
    category: "tech"

llm:
  provider: "ai-assistant"
  model: "ai-assistant-sonnet-4-20250514"
  api_key: "${ANTHROPIC_API_KEY}"

notify:
  feishu:
    enabled: true
    webhook_url: "${FEISHU_WEBHOOK}"
  telegram:
    enabled: false
    bot_token: "${TELEGRAM_BOT_TOKEN}"
    chat_id: "${TELEGRAM_CHAT_ID}"
  email:
    enabled: false
    smtp_host: "${SMTP_HOST}"
    smtp_user: "${SMTP_USER}"
    smtp_pass: "${SMTP_PASS}"
    to: "recipient@example.com"
```

## 命令行参数

```bash
python main.py [options]

--config, -c  配置文件路径 (默认: config.yaml)
--once        只执行一次抓取与推送
--stats       显示数据库中的统计信息
--db          数据库路径 (默认: rss_reader.db)
```

## 案例展示

### 案例 1: 订阅 Hacker News 与阮一峰,推送到飞书群

**场景**: 团队飞书群希望每天收到技术博客更新摘要

**配置文件 my_config.yaml 关键片段**:

```yaml
feeds:
  - name: "Hacker News"
    url: "https://hnrss.org/frontpage"
    category: "tech"
  - name: "阮一峰周刊"
    url: "https://www.ruanyifeng.com/blog/atom.xml"
    category: "tech"

llm:
  provider: "ai-assistant"
  model: "ai-assistant-sonnet-4-20250514"
  api_key: "${ANTHROPIC_API_KEY}"

notify:
  feishu:
    enabled: true
    webhook_url: "${FEISHU_WEBHOOK}"
```

**执行命令**:

```bash
python main.py --config my_config.yaml --once
```

**飞书群收到的消息**:

```text
📰 Hacker News

**Why SQLite is Taking Over**

📝 SQLite 正在从嵌入式数据库扩展到更多应用场景。文章分析了其在边缘计算、移动应用中的优势,并对比了 PostgreSQL 在轻量级场景下的局限。

[🔗 阅读原文]

📰 阮一峰周刊

**科技爱好者周刊第 350 期**

📝 本期周刊介绍了 WebGPU 的最新进展、一个开源的 Markdown 编辑器项目,以及关于 AI Agent 架构的讨论。

[🔗 阅读原文]
```

**分析**: 单次执行抓取两个 feed 的新条目,LLM 为每条生成中文摘要,飞书 Webhook 推送到群。SQLite 记录已推送的条目 ID,下次执行时自动跳过。

### 案例 2: arXiv 论文追踪,推送到 Telegram

**场景**: 研究人员希望追踪 arXiv 上 LLM 相关论文,中文摘要推送到 Telegram

**配置文件关键片段**:

```yaml
feeds:
  - name: "arXiv LLM"
    url: "https://rss.arxiv.org/rss/cs.CL"
    category: "research"

llm:
  provider: "llm-provider"
  model: "gpt-4o"
  api_key: "${OPENAI_API_KEY}"

notify:
  telegram:
    enabled: true
    bot_token: "${TELEGRAM_BOT_TOKEN}"
    chat_id: "${TELEGRAM_CHAT_ID}"
```

**执行命令**:

```bash
python main.py --config my_config.yaml --once
```

**Telegram 收到的消息**:

```text
📰 arXiv LLM

**Scaling Laws for Multilingual Language Models**

📝 本文研究了多语言大语言模型的缩放规律,发现在低资源语言上的性能提升速度低于高资源语言。作者提出了跨语言迁移的量化模型。

[🔗 阅读原文]
```

**分析**: 使用 llm-provider 作为后端(非 ai-assistant),Telegram Bot API 推送到指定 chat_id。arXiv 的 RSS feed 按 cs.CL 分类订阅,LLM 将英文论文标题与摘要翻译为中文。

### 案例 3: 竞品博客监控,推送到 Email

**场景**: 产品团队监控三个竞品官方博客,新文章摘要通过邮件发送

**配置文件关键片段**:

```yaml
feeds:
  - name: "竞品A博客"
    url: "https://competitor-a.com/blog/feed.xml"
    category: "competitor"
  - name: "竞品B博客"
    url: "https://competitor-b.com/blog/rss"
    category: "competitor"
  - name: "竞品C博客"
    url: "https://competitor-c.com/feed"
    category: "competitor"

llm:
  provider: "ai-assistant"
  model: "ai-assistant-sonnet-4-20250514"
  api_key: "${ANTHROPIC_API_KEY}"

notify:
  email:
    enabled: true
    smtp_host: "smtp.gmail.com"
    smtp_user: "${SMTP_USER}"
    smtp_pass: "${SMTP_PASS}"
    to: "product-team@company.com"
```

**执行命令**:

```bash
python main.py --config my_config.yaml --once
```

**收到的邮件正文**:

```text
📰 竞品A博客

**Introducing v3.0: New API Gateway**

📝 竞品A 发布了 3.0 版本,新增 API 网关功能,支持自动限流与熔断。文章重点介绍了与上一版的性能对比数据。

[🔗 阅读原文]
```

**分析**: 三个竞品 feed 归入 competitor 分类,LLM 生成摘要后通过 Gmail SMTP 发送邮件。SQLite 去重确保同一篇博客只推送一次,即使 cron 多次触发。

## 异常处理


| 错误场景 | 错误现象 | 原因分析 | 处理方式 |
|---------|---------|---------|---------|
| Feed URL 无法访问 | 抓取报 `ConnectionError` 或超时 | 网络不通或 feed URL 已失效 | 执行ping命令测试网络连通性,检查防火墙和代理设置连通性,在浏览器中打开 feed URL 确认是否可访问;URL 失效则更新配置 |
| LLM API 调用失败 | 报 `401 Unauthorized` 或 `429 Too Many Requests` | API Key 无效或额度耗尽 | 核对环境变量中的 API Key 是否正确;429 时降低抓取频率或更换 provider |
| 摘要内容为空 | LLM 返回空字符串或仅含标点 | feed 条目正文为空或 LLM 判断无有效内容 | 检查 feed 条目是否含 summary 或 content 字段;在 prompt 中加入"若内容过少则输出原文标题"兜底 |
| 飞书 Webhook 返回错误 | HTTP 状态码 400 或 `{"code": 19021}` | Webhook URL 失效或消息体格式不符飞书规范 | 在飞书群设置中重新获取 Webhook URL;检查消息体是否含必填字段(msg_type) |
| Telegram Bot 推送失败 | 报 `401 Unauthorized` 或 `400 chat not found` | Bot Token 无效或 chat_id 错误 | 通过 @BotFather 重新获取 Token;向 Bot 发送一条消息后用 getUpdates 获取正确的 chat_id |
| SMTP 连接失败 | 报 `SMTPAuthenticationError` 或连接超时 | SMTP 主机、端口、账号或密码错误 | 确认 SMTP 主机与端口(Gmail 用 smtp.gmail.com 端口 587);Gmail 需使用应用专用密码而非登录密码 |
| SQLite 数据库锁定 | 报 `database is locked` | 多个进程同时写入同一数据库文件 | 确保只有一个 main.py 进程在运行;通过 --db 参数为不同配置使用不同数据库文件 |
| 定时任务重复执行 | 同一条目被推送多次 | cron 调度重叠或 --once 模式被并发触发 | 检查 cron 表达式是否有重叠时段;使用文件锁(flock)防止并发执行 |

## 常见问题

### Q1: 如何在 ai-assistant 与 llm-provider 之间切换?
A: 在配置文件的 llm.provider 字段修改即可。设为 `ai-assistant` 使用 Anthropic 系列模型(需配置 ANTHROPIC_API_KEY),设为 `llm-provider` 使用 OpenAI 兼容接口(需配置对应 API Key)。切换后无需改代码,只需确保对应的环境变量已设置且 model 字段填写了该 provider 支持的模型名。

### Q2: SQLite 去重机制如何工作?清理旧数据怎么办?
A: 去重基于 feed URL 与条目 ID(或 GUID)的联合唯一键。每次抓取新条目时,先查询数据库中是否已存在该条目 ID,存在则跳过,不存在则生成摘要、推送并写入数据库。数据库会持续增长,如需清理历史数据,可直接删除 rss_reader.db 文件(下次执行会自动重建),或定期用 SQL 删除超过一定时间的记录。

### Q3: 如何同时推送到飞书、Telegram、Email 三个渠道?
A: 在配置文件的 notify 节点下,将 feishu.enabled、telegram.enabled、email.enabled 均设为 true,并分别配置各自的凭证字段。程序会对每条新条目依次调用已启用的渠道推送,某个渠道失败不影响其他渠道。注意三个渠道的环境变量需全部设置,否则对应渠道会在初始化时报错。

### Q4: 定时任务的执行频率如何控制?
A: 程序本身的定时循环间隔由配置文件中的 schedule.interval 字段(单位分钟)控制。若使用系统 cron 调度,建议用 `python main.py --config my_config.yaml --once` 配合 cron 表达式(如 `0 9 * * *` 表示每天 9 点执行),避免程序内置循环与 cron 重复触发。两种方式选其一,不要混用。

### Q5: 摘要质量不满意,如何调整输出?
A: 摘要质量受 prompt 与模型两方面影响。模型方面,可切换到更强的模型(如从 ai-assistant-sonnet 切换到 ai-assistant-opus)。Prompt 方面,可在配置文件 llm 节点增加 prompt 字段自定义摘要要求(如"侧重技术细节"、"控制在 2 句话以内"、"保留关键数据指标")。若摘要过于笼统,在 prompt 中加入"必须包含文章的核心结论与至少一个具体数据点"。

### Q6: 如何查看已抓取与推送的统计信息?
A: 运行 `python main.py --stats --config my_config.yaml` 即可。输出包含:数据库中记录的条目总数、各 feed 的抓取量、最近一次执行时间、推送成功与失败计数。统计信息从 SQLite 数据库读取, --stats 不会触发新的抓取与推送,只读不写。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **依赖 LLM 能力**: 摘要质量取决于底层模型,弱模型上摘要可能出现事实偏差或语句不通
- **仅生成摘要**: 不推送原文全文,如需全文需用户点击原文链接自行阅读
- **非实时推送**: 定时任务有执行间隔,新文章不会在发布瞬间推送,最快也需等下一次执行周期
- **摘要语言固定中文**: 当前版本统一输出中文摘要,暂不支持配置输出其他语言
- **凭证依赖外部配置**: 飞书 Webhook、Telegram Token、SMTP 凭证需用户自行在各平台申请并配置
- **单机运行**: 不支持分布式部署,SQLite 数据库为本地文件,多机器需各自维护独立数据库
