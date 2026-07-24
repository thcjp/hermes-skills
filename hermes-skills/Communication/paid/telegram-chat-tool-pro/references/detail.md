# 详细参考 - telegram-chat-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
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

## 代码示例 (python)

```python
#!/usr/bin/env python3
"""CI/CD 构建结果推送脚本"""
import subprocess
import json
from datetime import datetime

def notify_build_result(job_name, status, commit_msg, commit_author):
    """推送构建结果到 Telegram 群组"""
    if status == "success":
        icon = "[PASS]"
        color_msg = "构建成功"
    elif status == "failed":
        icon = "[FAIL]"
        color_msg = "构建失败"
    else:
        icon = "[WARN]"
        color_msg = "构建异常"

    message = f"""{icon} **{color_msg}**

**任务**: {job_name}
**状态**: {status}
**提交**: {commit_msg}
**提交者**: {commit_author}
**时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

[查看详情](https://ci.company.com/job/{job_name})"""

    subprocess.run([
        'python3', '{SKILL_DIR}/scripts/telegram_push.py',
        '--bot', 'dev_team_bot',
        '--target', '研发群',
        '--message', message,
        '--format', 'markdown'
    ])

notify_build_result(
    job_name="backend-api-deploy",
    status="success",
    commit_msg="fix: 修复用户登录超时问题",
    commit_author="zhangsan"
)
```

## 代码示例 (yaml)

```yaml
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

## 代码示例 (python)

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

automation = TelegramAutomation('{SKILL_DIR}/scripts/telegram_broadcast.py')
automation.push_message(bot='dev_team_bot', target='研发群',
    message='【版本发布】后端服务 v2.1.0 已发布,请更新测试环境。')
automation.broadcast(bot='company_bot', targets='研发群,市场群,财务群',
    message='【放假通知】下周一起公司团建,放假3天。')
automation.schedule_message(bot='team_bot', target='研发群', time='09:50',
    message='【站会提醒】10分钟后开始站会。', repeat='weekdays')
```

