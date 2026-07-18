---
slug: telegram-chat-tool-pro
name: telegram-chat-tool-pro
version: "1.0.0"
displayName: 电报聊天工具专业版
summary: 企业级Telegram多Bot管理与跨实例通信工具,支持主动推送、消息归档审计与群组批量管理。
license: MIT
edition: pro
description: |-
  电报聊天工具专业版,面向团队与企业用户提供多 Bot 管理、主动消息推送、消息归档审计与群组批量管理能力。

  核心能力:
  - 多 Bot 统一管理与快速切换
  - 主动消息推送(无需被艾特即可发送)
  - 消息归档与审计日志
  - 群组批量管理与成员同步
  - 跨实例群组广播
  - Webhook 集成与自动化工作流
  - 消息模板与定时发送

  适用场景:
  - 企业团队多 Bot 协作管理
  - 跨群组消息广播与公告
  - 自动化通知与告警推送
  - 消息合规存档与审计追溯

  差异化:专业版完全兼容免费版配置与命令体系,额外提供多 Bot 管理、主动推送、消息归档、群组批量操作与企业级集成能力,适合中大型团队与企业级通信场景。

  触发关键词: telegram, bot, 聊天, 艾特, 电报, 群组, 多bot, 广播, 推送, 归档, 审计, 自动化, 企业
tags:
- 沟通协作
- 即时通讯
- Telegram
- 机器人
- 企业效率
- 自动化
- 消息归档
tools:
- read
- exec
---

# 电报聊天工具 - 专业版

## 概述

电报聊天工具专业版是一款面向团队与企业用户的 Telegram 多 Bot 管理与跨实例通信解决方案。在完全兼容免费版单 Bot 配置与基础聊天能力的基础上,专业版解锁了多 Bot 统一管理、主动消息推送、消息归档审计、群组批量管理与 Webhook 集成等高级能力。

无论是管理团队多个 Bot 实例、跨群组广播重要公告、自动化推送告警通知,还是满足消息合规存档需求,专业版都能通过统一的配置与命令体系高效完成。

### 免费版与专业版能力对比

| 能力维度 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 单 Bot 配置 | 支持 | 支持 |
| 多 Bot 管理 | 不支持 | 支持(无上限) |
| 被动响应(被艾特后回复) | 支持 | 支持 |
| 主动消息推送 | 不支持 | 支持 |
| 群组消息收发 | 支持 | 支持 |
| 群组批量管理 | 不支持 | 支持 |
| 跨群组广播 | 不支持 | 支持 |
| 消息归档 | 不支持 | 支持 |
| 审计日志 | 不支持 | 支持 |
| 消息模板 | 不支持 | 支持 |
| 定时发送 | 不支持 | 支持 |
| Webhook 集成 | 不支持 | 支持 |
| 成员同步管理 | 不支持 | 支持 |

## 核心能力

### 一、多 Bot 统一管理(专业版独有)

- 同时管理多个 Bot 实例
- Bot 间快速切换与消息路由
- 统一配置管理与权限控制
- Bot 健康状态监控

### 二、主动消息推送(专业版独有)

- 无需被艾特即可主动发送消息
- 支持指定群组/用户定向推送
- 支持富文本与 Markdown 格式消息
- 支持消息卡片与按钮交互

### 三、消息归档与审计(专业版独有)

- 全量消息自动归档存储
- 按时间/群组/用户多维度检索
- 审计日志记录所有操作
- 支持导出归档数据

### 四、群组批量管理(专业版独有)

- 批量将 Bot 加入多个群组
- 群组成员列表同步与导出
- 群组权限统一配置
- 跨群组消息同步

### 五、跨群组广播(专业版独有)

- 一条消息同时推送到多个群组
- 支持按标签筛选目标群组
- 广播任务调度与进度追踪
- 失败自动重试

### 六、Webhook 集成与自动化(专业版独有)

- 接收外部系统 Webhook 触发消息推送
- 与 CI/CD、监控系统、告警系统对接
- 支持自定义消息模板
- 定时任务调度

### 七、消息模板与定时发送(专业版独有)

- 预设常用消息模板
- 支持变量插值(如日期、姓名)
- 定时发送消息(如每日站会提醒)
- 重复任务调度(如每周周报提醒)

## 使用场景

### 场景一:跨群组广播重要公告

公司行政需向多个部门群组同时推送放假通知,避免逐群发送。

```bash
# 跨群组广播通知
python3 {SKILL_DIR}/scripts/telegram_broadcast.py \
    --bot "company_bot" \
    --targets "研发群,市场群,财务群,行政群" \
    --message "【放假通知】2026年国庆假期为10月1日至10月7日,10月8日正常上班。请各部门提前安排好工作。" \
    --format markdown
```

**广播任务输出示例**:

```text
==================================================
广播任务报告
==================================================
任务ID: broadcast_20260718_001
发起Bot: @company_bot
消息类型: markdown
目标群组: 4个

--------------------------------------------------
发送结果:
[成功] 研发群 (-1001111111111) - 已送达
[成功] 市场群 (-1002222222222) - 已送达
[成功] 财务群 (-1003333333333) - 已送达
[失败] 行政群 (-1004444444444) - Bot非管理员,已加入重试队列

--------------------------------------------------
统计: 成功 3/4, 失败 1/4
状态: 部分成功,失败项已自动重试
```

### 场景二:CI/CD 构建结果自动推送

开发团队希望将 CI/CD 构建结果自动推送到团队 Telegram 群组。

```python
#!/usr/bin/env python3
"""CI/CD 构建结果推送脚本"""
import subprocess
import json
from datetime import datetime

def notify_build_result(job_name, status, commit_msg, commit_author):
    """推送构建结果到 Telegram 群组"""
    # 根据构建状态选择图标与颜色
    if status == "success":
        icon = "[PASS]"
        color_msg = "构建成功"
    elif status == "failed":
        icon = "[FAIL]"
        color_msg = "构建失败"
    else:
        icon = "[WARN]"
        color_msg = "构建异常"

    # 构建消息内容
    message = f"""{icon} **{color_msg}**

**任务**: {job_name}
**状态**: {status}
**提交**: {commit_msg}
**提交者**: {commit_author}
**时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

[查看详情](https://ci.company.com/job/{job_name})"""

    # 推送到 Telegram 群组
    subprocess.run([
        'python3', '{SKILL_DIR}/scripts/telegram_push.py',
        '--bot', 'dev_team_bot',
        '--target', '研发群',
        '--message', message,
        '--format', 'markdown'
    ])

# 使用示例
notify_build_result(
    job_name="backend-api-deploy",
    status="success",
    commit_msg="fix: 修复用户登录超时问题",
    commit_author="zhangsan"
)
```

### 场景三:每日站会提醒定时推送

团队希望每天早上 9:50 自动在群组中推送站会提醒。

```bash
# 设置定时推送任务
python3 {SKILL_DIR}/scripts/telegram_schedule.py \
    --bot "team_bot" \
    --target "研发群" \
    --time "09:50" \
    --repeat "weekdays" \
    --message "【站会提醒】10分钟后(10:00)开始每日站会,请各位准备:
1. 昨日完成事项
2. 今日计划事项
3. 遇到的问题与阻碍" \
    --format markdown
```

**定时任务管理**:

```bash
# 查看所有定时任务
python3 {SKILL_DIR}/scripts/telegram_schedule.py --list

# 暂停某个定时任务
python3 {SKILL_DIR}/scripts/telegram_schedule.py --pause task_id_001

# 恢复定时任务
python3 {SKILL_DIR}/scripts/telegram_schedule.py --resume task_id_001

# 删除定时任务
python3 {SKILL_DIR}/scripts/telegram_schedule.py --delete task_id_001
```

## 快速开始

### 第一步:配置多个 Bot

```yaml
# skill-platform.yaml 多 Bot 配置
messaging:
  telegram:
    bots:
      - name: "company_bot"
        token: "111111111:AAAaaaBBBbbbCCCccc"
        display_name: "公司官方Bot"
        allowed_chats:
          - "-1001111111111"
          - "-1002222222222"

      - name: "dev_team_bot"
        token: "222222222:DDDdddEEEeeeFFFfff"
        display_name: "研发团队Bot"
        allowed_chats:
          - "-1003333333333"

      - name: "hr_bot"
        token: "333333333:GGGgggHHHhhhIIIiii"
        display_name: "人事Bot"
        allowed_chats:
          - "-1004444444444"
```

### 第二步:验证多 Bot 配置

```bash
# 验证所有 Bot 状态
python3 {SKILL_DIR}/scripts/telegram_status.py --all

# 验证单个 Bot
python3 {SKILL_DIR}/scripts/telegram_status.py --bot "dev_team_bot"
```

**状态输出示例**:

```text
==================================================
Bot 状态总览
==================================================
[正常] company_bot    @company_official_bot    在线    管理3个群组
[正常] dev_team_bot   @dev_team_bot            在线    管理2个群组
[异常] hr_bot         @hr_assistant_bot        离线    Token可能过期

统计: 正常 2/3, 异常 1/3
```

### 第三步:开始使用高级功能

```bash
# 主动推送消息
python3 {SKILL_DIR}/scripts/telegram_push.py \
    --bot "dev_team_bot" \
    --target "研发群" \
    --message "版本 v2.1.0 已发布,请更新测试。" \
    --format markdown

# 跨群组广播
python3 {SKILL_DIR}/scripts/telegram_broadcast.py \
    --bot "company_bot" \
    --targets "研发群,市场群" \
    --message "公司年会定于1月20日举办,请各部门准备节目。"
```

## 配置示例

### 多 Bot 统一配置

```yaml
# skill-platform.yaml 企业配置
messaging:
  telegram:
    bots:
      - name: "company_bot"
        token: "${COMPANY_BOT_TOKEN}"
        display_name: "公司官方Bot"
        allowed_chats:
          - "-1001111111111"
          - "-1002222222222"
        features:
          broadcast: true
          archive: true
          audit: true

      - name: "dev_team_bot"
        token: "${DEV_BOT_TOKEN}"
        display_name: "研发团队Bot"
        allowed_chats:
          - "-1003333333333"
        features:
          broadcast: false
          archive: true
          audit: true

    # 全局配置
    archive:
      enabled: true
      storage: "local"
      path: "/data/telegram_archive/"
      retention_days: 365

    audit:
      enabled: true
      log_path: "/var/log/telegram_audit.log"
      sensitive_operations:
        - "broadcast"
        - "delete_message"
        - "kick_member"
```

### 消息模板配置

```yaml
# templates.yaml 消息模板
templates:
  - name: "daily_standup"
    title: "每日站会提醒"
    content: |
      【站会提醒】{minutes}分钟后({time})开始每日站会,请各位准备:
      1. 昨日完成事项
      2. 今日计划事项
      3. 遇到的问题与阻碍
    variables:
      - name: "minutes"
        default: "10"
      - name: "time"
        default: "10:00"

  - name: "release_notify"
    title: "版本发布通知"
    content: |
      【版本发布】{project} v{version} 已发布
      更新内容:{changelog}
      请相关同学更新测试环境验证。
    variables:
      - name: "project"
        required: true
      - name: "version"
        required: true
      - name: "changelog"
        required: true

  - name: "incident_alert"
    title: "故障告警"
    content: |
      【故障告警】{severity}
      服务:{service} | 时间:{time}
      描述:{description}
      请值班同学立即处理!
    variables:
      - name: "severity"
        default: "P2"
      - name: "service"
        required: true
      - name: "time"
        required: true
      - name: "description"
        required: true
```

### Webhook 集成配置

```yaml
# webhook.yaml Webhook 配置
webhooks:
  - name: "ci_build"
    path: "/webhook/ci"
    bot: "dev_team_bot"
    target: "研发群"
    template: "release_notify"
    secret: "your_webhook_secret"
  - name: "monitor_alert"
    path: "/webhook/alert"
    bot: "ops_bot"
    target: "运维群"
    template: "incident_alert"
    secret: "your_alert_secret"
```

### 企业级自动化工作流

```python
#!/usr/bin/env python3
"""企业 Telegram 通信自动化工作流"""
import subprocess, json

class TelegramAutomation:
    def __init__(self, script_path):
        self.script = script_path

    def push_message(self, bot, target, message, fmt='markdown'):
        """主动推送消息"""
        r = subprocess.run(['python3', self.script.replace('broadcast', 'push'),
            '--bot', bot, '--target', target, '--message', message, '--format', fmt],
            capture_output=True, text=True)
        return r.returncode == 0

    def broadcast(self, bot, targets, message, fmt='markdown'):
        """跨群组广播"""
        r = subprocess.run(['python3', self.script, '--bot', bot,
            '--targets', targets, '--message', message, '--format', fmt],
            capture_output=True, text=True)
        return json.loads(r.stdout) if r.stdout else {}

    def schedule_message(self, bot, target, time, message, repeat='once'):
        """定时发送消息"""
        r = subprocess.run(['python3', self.script.replace('broadcast', 'schedule'),
            '--bot', bot, '--target', target, '--time', time,
            '--repeat', repeat, '--message', message], capture_output=True, text=True)
        return json.loads(r.stdout) if r.stdout else {}

# 使用示例
automation = TelegramAutomation('{SKILL_DIR}/scripts/telegram_broadcast.py')
automation.push_message(bot='dev_team_bot', target='研发群',
    message='【版本发布】后端服务 v2.1.0 已发布,请更新测试环境。')
automation.broadcast(bot='company_bot', targets='研发群,市场群,财务群',
    message='【放假通知】下周一起公司团建,放假3天。')
automation.schedule_message(bot='team_bot', target='研发群', time='09:50',
    message='【站会提醒】10分钟后开始站会。', repeat='weekdays')
```

## 最佳实践

### 1. 多 Bot 按职能划分

企业环境建议按职能划分 Bot,避免单个 Bot 承担过多职责:

| Bot 名称 | 职能 | 使用场景 |
|:---------|:-----|:---------|
| company_bot | 公司官方 | 全公司公告、政策通知 |
| dev_team_bot | 研发团队 | 版本发布、CI/CD 通知 |
| ops_bot | 运维团队 | 告警推送、故障通知 |
| hr_bot | 人事行政 | 考勤、放假、活动通知 |

### 2. 广播任务分批发送

大量群组广播时,分批发送避免触发 Telegram 速率限制:

```bash
# 推荐分批发送(每批10个群组,间隔1秒)
python3 {SKILL_DIR}/scripts/telegram_broadcast.py \
    --bot "company_bot" \
    --targets-file "all_groups.txt" \
    --message "通知内容" \
    --batch-size 10 \
    --interval 1
```

### 3. 敏感操作启用审计日志

广播、消息删除、成员踢出等敏感操作务必记录审计日志:

```bash
# 查看审计日志
python3 {SKILL_DIR}/scripts/telegram_audit.py --log /var/log/telegram_audit.log \
    --from "2026-07-01" --to "2026-07-18"

# 按操作类型筛选
python3 {SKILL_DIR}/scripts/telegram_audit.py --action "broadcast" --limit 50
```

### 4. 消息模板统一管理

常用消息使用模板管理,确保格式一致:

```bash
# 使用模板发送消息
python3 {SKILL_DIR}/scripts/telegram_push.py \
    --bot "dev_team_bot" \
    --target "研发群" \
    --template "release_notify" \
    --var "project=后端服务" \
    --var "version=v2.1.0" \
    --var "changelog=1. 修复登录问题\n2. 优化性能"
```

### 5. 归档数据定期备份

消息归档数据定期备份,防止数据丢失:

```bash
# 每周备份归档数据
0 2 * * 0 tar -czf /backup/telegram_archive_$(date +\%Y\%m\%d).tar.gz /data/telegram_archive/
```

## 常见问题

### Q1: 多个 Bot 之间如何区分消息来源?

**A**: 专业版为每个 Bot 维护独立身份标识。归档记录与审计日志中会标注消息来源 Bot 名称,便于追溯:

```bash
# 查看消息来源
python3 {SKILL_DIR}/scripts/telegram_archive.py --search "关键词" --show-source
```

### Q2: 广播任务部分群组失败怎么办?

**A**: 广播任务会自动重试失败的群组。常见失败原因:
- Bot 不是该群组的管理员
- 群组 ID 配置错误
- 网络波动

查看广播报告中的失败列表,针对性修复后重试:

```bash
# 重试失败的群组
python3 {SKILL_DIR}/scripts/telegram_broadcast.py --retry task_id_001
```

### Q3: 定时任务如何管理?

**A**: 专业版提供完整的定时任务管理:

```bash
python3 {SKILL_DIR}/scripts/telegram_schedule.py --list          # 查看所有任务
python3 {SKILL_DIR}/scripts/telegram_schedule.py --pause <id>    # 暂停任务
python3 {SKILL_DIR}/scripts/telegram_schedule.py --resume <id>   # 恢复任务
python3 {SKILL_DIR}/scripts/telegram_schedule.py --delete <id>   # 删除任务
```

### Q4: 消息归档占用空间过大怎么办?

**A**: 建议配置归档保留策略(`retention_days: 365`、`auto_cleanup: true`、`compress: true`),定期清理过期数据并压缩存储。

### Q5: 免费版用户升级后配置是否兼容?

**A**: 完全兼容。专业版支持免费版的单 Bot 配置格式,升级后原有配置无需修改,直接获得多 Bot 管理与高级功能权限。

### Q6: Webhook 集成如何保证安全?

**A**: 专业版 Webhook 支持密钥验证(`secret` 字段),确保仅授权的系统可触发推送。请求需携带此密钥才能通过验证。

### Q7: 是否支持与其他 IM 平台互通?

**A**: 专业版专注 Telegram 生态。如需跨平台消息同步(如 Telegram 与 Slack 互通),可通过 Webhook 中转实现。

## 依赖说明

### 运行环境

- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 建议 3.8+(运行自动化脚本)
- **网络环境**: 需可访问 Telegram API(部分区域需网络代理)
- **定时任务**: 建议 cron(Linux/macOS)或任务计划程序(Windows)
- **存储空间**: 消息归档需预留磁盘空间(建议 10GB+)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Telegram 账户 | 账户 | 必需 | 注册 Telegram |
| Telegram Bot Token | 凭据 | 必需 | 通过 @BotFather 创建(支持多个) |
| skill-platform.yaml | 配置 | 必需 | 手动创建配置文件 |
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| requests | Python库 | 必需 | pip install requests |
| 网络代理 | 网络 | 视情况 | 部分地区需代理访问 Telegram |
| Webhook 服务 | 服务 | 可选 | 用于接收外部系统触发 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 通过 Telegram 中的 @BotFather 创建多个 Bot 获取各自 Token
- 将 Token 配置到 `skill-platform.yaml` 的 `messaging.telegram.bots` 列表
- 将各 Bot 允许通信的群组 ID 填入对应 `allowed_chats` 列表
- Webhook 集成需配置密钥(`secret`字段)用于请求验证
- Token 属于敏感凭据,建议使用环境变量引用,定期轮换

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,核心功能通过 Python 脚本与 Telegram API 调用实现)
- **说明**: 基于脚本的企业级 AI Skill,通过自然语言指令驱动 Agent 执行 Telegram 多 Bot 管理与跨实例通信。专业版完全兼容免费版单 Bot 配置与基础聊天能力,额外提供多 Bot 统一管理、主动消息推送、消息归档审计、群组批量管理、跨群组广播、Webhook 集成与定时任务调度能力,适合中大型团队与企业级通信场景。
