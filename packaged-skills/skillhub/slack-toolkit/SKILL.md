---
slug: "slack-toolkit"
name: "slack-toolkit"
version: "1.0.0"
displayName: "Slack工具箱专业版"
summary: "企业级Slack管理工具，支持批量消息操作、定时发送、消息模板、频道分析与团队协作场景。"
license: "Proprietary"
edition: "pro"
description: |-
  Slack工具箱（专业版）—— 面向团队和企业的全功能Slack管理工具。核心能力:
  - 批量消息发送、编辑与删除
  - 定时消息调度与计划管理
  - 消息模板库与变量替换
  - 频道消息统计分析
  - 多频道广播与跨团队协作
  - 表情回应自动化与工作流触发

  适用场景:
  - 企业级公告批量推送
  - 跨频道信息同步与广播
  - 定时提醒与周期通知
  - 团队沟通数据分析与优化

  差异化: 在免费版基础上增加批量操作、定时调度、模板管理、数据分析等企业级能力，完全兼容免费版操作格式
tags:
  - 沟通协作
  - 企业级
  - Slack
  - 自动化
  - 批量处理
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# Slack工具箱专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

### 1. 批量消息操作
支持向多个频道同时发送消息，批量编辑或删除消息，大幅提升管理效率。

**输入**: 用户提供批量消息操作所需的指令和必要参数。
**输出**: 返回批量消息的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`批量消息操作`的配置文档进行参数调优
### 2. 定时消息调度
支持定时发送消息，管理待发送消息队列，查看与取消计划消息。

**输入**: 用户提供定时消息调度所需的指令和必要参数。
**输出**: 返回定时消息调度的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`定时消息调度`的配置文档进行参数调优
### 3. 消息模板库
内置常用消息模板，支持变量替换、分类管理与团队共享。

**输入**: 用户提供消息模板库所需的指令和必要参数。
**处理**: 解析消息模板库的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回消息模板库的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`消息模板库`的配置文档进行参数调优
### 4. 频道消息分析
统计频道活跃度、消息量趋势、成员参与度等指标，生成可视化报告。

**输入**: 用户提供频道消息分析所需的指令和必要参数。
**处理**: 解析频道消息分析的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证返回数据的完整性和格式正确性
- 参考`频道消息分析`的配置文档进行参数调优
### 5. 多频道广播
一条消息同时推送到多个频道，支持频道分组与广播规则配置。

**输入**: 用户提供多频道广播所需的指令和必要参数。
**处理**: 解析多频道广播的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回多频道广播的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`多频道广播`的配置文档进行参数调优
### 6. 表情回应自动化
根据消息内容关键词自动添加表情回应，或触发后续工作流。

**处理**: 解析表情回应自动化的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回表情回应自动化的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`表情回应自动化`的配置文档进行参数调优
#
## 适用场景

### 场景一：跨频道公告广播

向多个团队频道同时发送重要公告。

```python
# broadcast_sender.py
import json

class BroadcastSender:
    """多频道广播发送器"""

    def __init__(self, slack_client):
        self.client = slack_client

    def broadcast(self, message, channels, template_vars=None):
        """
        向多个频道广播消息
        :param message: 消息内容或模板
        :param channels: 频道ID列表
        :param template_vars: 模板变量
        """
        if template_vars:
            message = self.apply_template(message, template_vars)

        results = []
        for channel in channels:
            result = self.client.send_message(
                channel=channel,
                text=message
            )
            results.append({
                'channel': channel,
                'success': result.get('ok', False),
                'timestamp': result.get('ts')
            })

        # 生成广播报告
        self.generate_report(results)
        return results

    def apply_template(self, template, variables):
        """应用模板变量"""
        for key, value in variables.items():
            template = template.replace(f"{"toolkit_result"}", str(value))
        return template

# 示例
sender = BroadcastSender(slack_client)
results = sender.broadcast(
    message="【公告】{event} 将于 {date} 举行，请各位安排好时间参加。",
    channels=["C001", "C002", "C003", "C004"],
    template_vars={
        "event": "季度全员大会",
        "date": "2026年7月25日 14:00"
    }
)
```

### 场景二：定时提醒调度

```python
# schedule_manager.py
from datetime import datetime, timedelta
import schedule
import time

class ScheduleManager:
    """定时消息调度管理器"""

    def __init__(self, slack_client):
        self.client = slack_client
        self.scheduled = []

    def schedule_message(self, channel, message, send_time):
        """调度定时消息"""
        result = self.client.schedule_message(
            channel=channel,
            text=message,
            post_at=send_time
        )
        self.scheduled.append({
            'channel': channel,
            'message': message,
            'send_time': send_time,
            'scheduled_id': result.get('scheduled_message_id')
        })
        return result

    def list_scheduled(self, channel):
        """列出待发送消息"""
        return self.client.list_scheduled_messages(channel=channel)

    def cancel_scheduled(self, channel, message_id):
        """取消定时消息"""
        return self.client.delete_scheduled_message(
            channel=channel,
            scheduled_message_id=message_id
        )

# 使用示例
manager = ScheduleManager(slack_client)

# 安排每天早上9点的站会提醒
schedule.every().day.at("09:00").do(
    manager.schedule_message,
    channel="C0123456789",
    message="大家早上好！15分钟后开始每日站会，请准备好进展汇报。",
    send_time=int(time.time())
)

# 安排每周五的周报提醒
schedule.every().friday.at("17:00").do(
    manager.schedule_message,
    channel="C0123456789",
    message="提醒：请在本周内提交周报到 #weekly-reports 频道。",
    send_time=int(time.time())
)
```

### 场景三：频道活跃度分析

```python
# channel_analytics.py
class ChannelAnalytics:
    """频道消息分析器"""

    def analyze_channel(self, channel_id, days=7):
        """分析频道活跃度"""
        messages = self.fetch_messages(channel_id, days)

        report = {
            "频道ID": channel_id,
            "分析周期": f"最近{days}天",
            "总消息数": len(messages),
            "活跃成员数": len(set(m['user'] for m in messages)),
            "日均消息": len(messages) // days,
            "高峰时段": self.find_peak_hours(messages),
            "活跃成员TOP5": self.get_top_contributors(messages, 5),
            "表情回应统计": self.get_reaction_stats(messages),
            "线程回复率": self.get_thread_reply_rate(messages)
        }
        return report

    def get_top_contributors(self, messages, top_n=5):
        """获取最活跃成员"""
        from collections import Counter
        user_counts = Counter(m['user'] for m in messages)
        return [
            {"用户": user, "消息数": count}
            for user, count in user_counts.most_common(top_n)
        ]

# 生成报告
analytics = ChannelAnalytics()
report = analytics.analyze_channel("C0123456789", days=30)
```

## 使用流程

### 安装

```bash
npx skillhub@latest install slack-toolkit-pro
```

### 配置

```bash
# .env 配置
SLACK_BOT_TOKEN=xoxb-your-bot-token-here
SLACK_APP_TOKEN=xapp-your-app-token-here  # 专业版需要Socket Mode
```

### 批量操作

```bash
# 批量发送消息到多个频道
slack-toolkit-pro batch-send \
  --channels "C001,C002,C003" \
  --message "重要系统维护通知：今晚22:00-24:00"

# 定时发送消息
slack-toolkit-pro schedule \
  --channel "C0123456789" \
  --message "每周五周报提醒" \
  --time "every friday 17:00"

# 查看频道分析报告
slack-toolkit-pro analytics --channel "C0123456789" --days 30
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | slack-toolkit处理的内容输入 |,  |
| content | string | 否 | slack-toolkit处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.8+
- **网络环境**: 需能访问 `https://slack.com/api/` 端点

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Slack Bot Token | API凭证 | 必需 | Slack App管理页面创建 |
| Slack App Token | API凭证 | 必需 | 启用Socket Mode时需要 |
| Python 3.8+ | 运行时 | 必需 | python.org 官方下载 |
| slack-sdk | Python库 | 必需 | `pip install slack-sdk` |
| schedule | Python库 | 推荐 | `pip install schedule` |
| sqlite3 | 标准库 | 必需 | Python内置 |
| jinja2 | Python库 | 推荐 | `pip install jinja2`（模板引擎） |

### API Key 配置

```bash
# Slack Token（必需）
export SLACK_BOT_TOKEN="xoxb-your-bot-token-here"
export SLACK_APP_TOKEN="xapp-your-app-token-here"

# 专业版所需额外Bot Token Scopes:
# - chat:write              发送消息
# - chat:write.public       发送到任意公开频道
# - chat:schedule:write     定时消息
# - chat:schedule:read      查看定时消息
# - channels:read           读取频道列表
# - channels:history        读取频道历史
# - reactions:write         添加表情回应
# - reactions:read          查看表情回应
# - pins:write              置顶管理
# - pins:read               查看置顶
# - users:read              成员信息
# - emoji:read              表情列表
# - team:read               团队信息
```

### 可用性分类

- **分类**: MD+EXEC+SCRIPT+API（Markdown指令 + 命令行执行 + Python脚本 + Slack API）
- **说明**: 基于Markdown的AI Skill，专业版支持批量操作、定时调度与数据分析
- **适用人群**: 企业团队、项目经理、运营团队、Slack管理员
- **兼容性**: 完全兼容免费版操作格式与配置，支持无缝升级
- **支持级别**: 优先技术支持，工作日24小时内响应

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

### 示例2: 进阶用法
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

### Q: 专业版与免费版如何兼容？

专业版完全兼容免费版的所有操作格式。免费版的JSON参数格式可直接在专业版中使用，升级无需修改现有配置。

### 错误恢复步骤
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

专业版单次广播最大支持50个频道，发送频率限制为每秒1条，避免触发Slack API限流。如需更大规模广播，建议分批次执行。

### Q: 定时消息最远可以排到什么时候？

Slack API限制定时消息最多可排到未来120天。超过此限制需要使用外部调度器（如cron）在到期时重新调度。

### Q: 频道分析数据存储在哪里？

分析数据存储在本地SQLite数据库中，不会上传到外部服务器。数据默认保留90天，可通过配置调整。

### Q: 模板变量支持哪些格式？

```python
# 支持的变量格式
template = """
{name}你好，

你的项目 {project} 将于 {date} 到期。
当前进度：{progress}%

请及时更新状态。
"""

# 变量替换
variables = {
    "name": "张三",
    "project": "Alpha",
    "date": "2026-07-31",
    "progress": 75
}
```

### Q: 自动表情回应如何配置？

在配置文件中设置关键词与对应表情的映射规则。当频道中出现包含关键词的消息时，Bot会自动添加指定的表情回应。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
- 需要LLM支持
- 需要LLM支持
- 需要LLM支持

