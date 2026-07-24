---
slug: "timeline-digest"
name: "timeline-digest"
version: 1.0.1
displayName: "时间线摘要工具-专业版"
summary: "企业级X/Twitter时间线摘要平台,支持定时调度/智能分类/多源聚合/自动推送"
license: "Proprietary"
edition: "pro"
description: |-
  时间线摘要工具专业版,面向企业和专业用户的高级X/Twitter时间线信息聚合平台。核心能力:
  - 全时间线抓取(For You + Following + 自定义列表)
  - 智能分类摘要(AI分类:科技/加密货币/商业洞察/其他)
  - 高级语义过滤与降噪
  - 定时自动调度与增量处理
  - 多源信息聚合(X/Twitter + RSS + 自定义源)
  - 自动推送通知(Telegram/邮件/Webhook)
  - 状态管理与云端同步
  - 摘要分析仪表盘与趋势追踪

  适用场景:
  - 企业舆情监控与行业动态追踪
tags:
  - 沟通协作
  - 信息聚合
  - X/Twitter
  - 企业级
  - 智能摘要
  - 自动化
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# 时间线摘要工具-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 时间线摘要工具-专业版支持定时调度 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

### 1. 智能分类摘要
PRO版通过LLM对去重后的推文进行智能分类和中文摘要生成.
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供智能分类摘要所需的指令和必要参数.
**处理**: 解析智能分类摘要的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 2. 定时自动调度
PRO版支持cron式定时调度,自动执行摘要生成流程.
**输入**: 用户提供定时自动调度所需的指令和必要参数.
### 3. 多源信息聚合
除X/Twitter时间线外,PRO版支持聚合RSS源和自定义信息源.
**输入**: 用户提供多源信息聚合所需的指令和必要参数.
**处理**: 解析多源信息聚合的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回多源信息聚合的处理结果,包含执行状态码、结果数据和执行日志.
**输入**: 用户提供自动推送通知所需的指令和必要参数.
**处理**: 解析自动推送通知的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回自动推送通知的处理结果,包含执行状态码、结果数据和执行日志.
#
## 适用场景

### 场景一:企业舆情自动监控
企业设置每6小时自动抓取X/Twitter时间线,生成分类摘要并推送到Telegram群组.
```python
config = {
    "intervalHours": 6,
    "fetchLimitForYou": 100,
    "fetchLimitFollowing": 60,
    "maxItemsPerDigest": 25,
    "notifications": {
        "telegram": {
            "enabled": True,
            "bot_token": "YOUR_BOT_TOKEN",
            "chat_id": "@company_pr_monitor"
        }
    }
}
# ...
scheduler = DigestScheduler(config)
scheduler.start()
```

### 场景二:投资研究信息聚合
投资团队聚合X/Twitter和多个RSS源,生成每日投资简报.
```python
aggregator = MultiSourceAggregator()
aggregator.add_twitter_source("X-Crypto", limit=100)
aggregator.add_rss_source("CoinDesk", "https://feeds.coindesk.com/coinbase")
aggregator.add_rss_source("TechCrunch", "https://techcrunch.com/feed/")
# ...
all_items = aggregator.fetch_all()
digest = SmartDigestGenerator().generate_smart_digest(all_items)
# ...
pusher = NotificationPusher({
    "email": {
        "enabled": True,
        "from": "digest@company.com",
        "to": "research@company.com",
        "smtp_host": "smtp.company.com",
        "smtp_port": 587,
        "username": "digest@company.com",
        "password": "PASSWORD"
    }
})
pusher.push_email(digest["digestText"])
```

### 场景三:内容团队素材采集
内容团队定期采集时间线中的热门话题,作为创作素材.
```python
aggregator = MultiSourceAggregator()
aggregator.add_twitter_source("X-Trending", limit=200)
# ...
items = aggregator.fetch_all()
digest = SmartDigestGenerator().generate_smart_digest(items)
# ...
for section in digest["sections"]:
    print(f"\n{section['icon']} {section['category_name']} - {section['count']}条素材")
    for item in section["items"][:5]:
        print(f"  • {item['author']}: {item['summary']}")
        print(f"    {item['url']}")
```

## 使用流程

### 从免费版升级
```bash
skill-platform skills install timeline-digest-tool-pro
skill-platform gateway restart
# ...
```

### 全新安装
```bash
bird --version
python3 --version
# ...
skill-platform skills install timeline-digest-tool-pro
# ...
python3 init_config.py --interval 6 --output config.json
# ...
python3 setup_notifications.py --telegram --email
# ...
python3 start_scheduler.py --config config.json
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | timeline-digest处理的内容输入 |,  |
| content | string | 否 | timeline-digest处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "digest 相关配置参数",
    result: "digest 相关配置参数",
    result: "digest 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+
- **网络环境**: 需可访问X/Twitter服务和推送服务

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| bird | CLI工具 | 必需 | 参考bird工具文档安装 |
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| feedparser | Python库 | 可选 | `pip install feedparser` |
| requests | Python库 | 可选 | `pip install requests` |
| schedule | Python库 | 可选 | `pip install schedule` |

### API Key 配置
- bird工具的认证(cookie)由bird工具自行管理
- Telegram推送需要Bot Token(通过 @BotFather 创建)
- 邮件推送需要SMTP账号密码
- Webhook推送需要目标URL和认证Token
- LLM智能摘要由Agent内置LLM提供,无需额外Key

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行时间线摘要和推送任务
- **运行模式**: 本地脚本执行 + 定时调度 + 远程推送
- **安全等级**: 只读抓取操作;推送通知需配置认证凭证;状态文件支持云端加密同步
- **兼容性**: 与免费版(timeline-digest-tool-free)完全兼容,支持无缝升级

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1: PRO版的智能分类准确率如何?
**A:** PRO版使用关键词匹配+LLM语义分析双重分类机制。对于明确领域的内容(如AI、加密货币)准确率较高。用户可通过配置自定义分类关键词来提升特定领域的分类准确率.
### Q2: 定时调度如何保证不遗漏推文?
**A:** PRO版使用增量过滤机制,每次运行只处理上次运行后的新推文。状态文件记录已处理的推文ID,即使调度间隔较长也不会遗漏。状态文件保留30天的记录,确保去重有效.
### Q3: 多源聚合会增加API调用吗?
**A:** X/Twitter源的抓取通过bird工具完成,不额外增加API调用。RSS源是标准HTTP请求,不涉及API限制。自定义源取决于具体实现。建议合理设置抓取频率,避免对源站造成压力.
### Q4: 推送通知支持哪些渠道?
**A:** PRO版支持Telegram Bot推送、邮件推送(SMTP)和Webhook推送。Webhook可对接Slack、飞书、企业微信等支持Webhook的平台.
### Q5: 状态文件可以云端同步吗?
**A:** PRO版支持状态文件云端同步,适合多设备或团队共享去重状态的场景。配置中设置 `cloud_sync` 相关参数即可启用.
### Q6: 如何与免费版协作?
**A:** PRO版与免费版完全兼容。免费版的状态文件格式与PRO版一致,升级后直接继承。免费版用户手动生成的JSON摘要也可以导入PRO版进行智能分类处理.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

