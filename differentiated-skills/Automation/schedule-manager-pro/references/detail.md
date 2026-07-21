# 详细参考 - schedule-manager-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (json)

```json
// ~/workspace/schedule/chains.json
{
  "daily_pipeline": {
    "trigger": { "cron": "0 8 * * *", "timezone": "Asia/Shanghai" },
    "nodes": {
      "fetch": {
        "task": "从API抓取昨日数据",
        "requires": ["fetch"],
        "timeout_minutes": 30
      },
      "clean": {
        "task": "清洗与去重数据",
        "requires": ["data-clean"],
        "depends_on": ["fetch"],
        "timeout_minutes": 20
      },
      "report": {
        "task": "生成日报并归档",
        "requires": ["report"],
        "depends_on": ["clean"],
        "timeout_minutes": 15
      },
      "notify": {
        "task": "发送日报给团队",
        "requires": ["mail"],
        "depends_on": ["report"],
        "timeout_minutes": 5
      }
    },
    "on_failure": "alert_and_pause",
    "id": "chain_pipeline_001"
  }
}
```

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────┐
│                任务调度管家专业版 (SCHEDULE MANAGER PRO)          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │  DAG编排引擎  │  │  重试与容错   │  │  多通道告警   │           │
│  │  Dependency  │  │  Retry Engine │  │  Alert Hub   │           │
│  │  Engine      │  │              │  │              │           │
│  │  ✅ 专业版    │  │  ✅ 专业版    │  │  ✅ 专业版    │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  优先级调度   │  ← 资源并发控制                 │
│                  │  Scheduler   │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  监控仪表盘   │  ← 执行健康度可视化             │
│                  │  Dashboard   │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  日历集成     │  ← Google/Outlook双向同步       │
│                  │  Calendar    │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 代码示例 (json)

```json
// ~/workspace/schedule/preferences.json
{
  "timezone": "Asia/Shanghai",
  "edition": "pro",
  "retry": {
    "default_max_retries": 3,
    "backoff_strategy": "exponential",
    "base_delay_seconds": 60
  },
  "alerts": {
    "channels": ["dingtalk", "email", "telegram"],
    "on_failure": true,
    "on_retry": false,
    "on_recovery": true
  },
  "calendar": {
    "provider": "google",
    "sync_direction": "both",
    "create_events_for_tasks": true
  },
  "dashboard": {
    "enabled": true,
    "port": 19196,
    "retention_days": 90
  },
  "priority": {
    "levels": ["critical", "high", "normal", "low"],
    "max_concurrent": 5
  }
}
```

## 代码示例 (json)

```json
{
  "alerts": {
    "channels": {
      "dingtalk": {
        "webhook": "env:DINGTALK_WEBHOOK",
        "mentions": ["@all"]
      },
      "email": {
        "to": ["ops@company.com"],
        "subject_template": "[调度告警] {{task_name}} 失败"
      },
      "telegram": {
        "bot_token": "env:TELEGRAM_BOT_TOKEN",
        "chat_id": "env:TELEGRAM_CHAT_ID"
      },
      "feishu": {
        "webhook": "env:FEISHU_WEBHOOK"
      }
    },
    "on_failure": true,
    "on_retry": false,
    "on_recovery": true,
    "on_dead_letter": true
  }
}
```

## 代码示例 (json)

```json
{
  "cicd_pipeline": {
    "trigger": { "type": "github_push", "branch": "main" },
    "nodes": {
      "build": { "task": "构建Docker镜像", "retry": {"max_retries": 2} },
      "unit_test": { "task": "单元测试", "depends_on": ["build"] },
      "security_scan": { "task": "安全扫描", "depends_on": ["build"] },
      "integration_test": { "task": "集成测试", "depends_on": ["unit_test", "security_scan"] },
      "deploy_staging": { "task": "部署到预发", "depends_on": ["integration_test"] },
      "smoke_test": { "task": "冒烟测试", "depends_on": ["deploy_staging"] },
      "deploy_production": { "task": "部署到生产", "depends_on": ["smoke_test"], "priority": "critical" }
    },
    "on_failure": "alert_and_pause",
    "alerts": { "channels": ["dingtalk", "email"] }
  }
}
```

## 代码示例 (json)

```json
{
  "cicd_pipeline": {
    "trigger": { "type": "github_push", "branch": "main" },
    "nodes": {
      "build": { "task": "构建Docker镜像", "retry": {"max_retries": 2} },
      "unit_test": { "task": "单元测试", "depends_on": ["build"] },
      "security_scan": { "task": "安全扫描", "depends_on": ["build"] },
      "integration_test": { "task": "集成测试", "depends_on": ["unit_test", "security_scan"] },
      "deploy_staging": { "task": "部署到预发", "depends_on": ["integration_test"] },
      "smoke_test": { "task": "冒烟测试", "depends_on": ["deploy_staging"] },
      "deploy_production": { "task": "部署到生产", "depends_on": ["smoke_test"], "priority": "critical" }
    },
    "on_failure": "alert_and_pause",
    "alerts": { "channels": ["dingtalk", "email"] }
  }
}
```

## 代码示例 (json)

```json
{
  "daily_settlement": {
    "trigger": { "cron": "0 23 * * *" },
    "task": "执行每日结算",
    "priority": "critical",
    "retry": { "max_retries": 3, "backoff": "exponential" },
    "alerts": {
      "channels": ["dingtalk", "email", "phone_call"],
      "on_failure": true,
      "on_dead_letter": true
    },
    "sla_minutes": 60
  }
}
```

### 300秒上手（完整企业配置）
配置完整的监控仪表盘与日历集成：

```json
// ~/workspace/schedule/preferences.json
{
  "timezone": "Asia/Shanghai",
  "edition": "pro",
  "retry": {
    "default_max_retries": 3,
    "backoff_strategy": "exponential",
    "base_delay_seconds": 60
  },
  "alerts": {
    "channels": ["dingtalk", "email", "telegram"],
    "on_failure": true,
    "on_retry": false,
    "on_recovery": true
  },
  "calendar": {
    "provider": "google",
    "sync_direction": "both",
    "create_events_for_tasks": true
  },
  "dashboard": {
    "enabled": true,
    "port": 19196,
    "retention_days": 90
  },
  "priority": {
    "levels": ["critical", "high", "normal", "low"],
    "max_concurrent": 5
  }
}
```



## 架构总览
```text
┌─────────────────────────────────────────────────────────────────┐
│                任务调度管家专业版 (SCHEDULE MANAGER PRO)          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │  DAG编排引擎  │  │  重试与容错   │  │  多通道告警   │           │
│  │  Dependency  │  │  Retry Engine │  │  Alert Hub   │           │
│  │  Engine      │  │              │  │              │           │
│  │  ✅ 专业版    │  │  ✅ 专业版    │  │  ✅ 专业版    │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  优先级调度   │  ← 资源并发控制                 │
│                  │  Scheduler   │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  监控仪表盘   │  ← 执行健康度可视化             │
│                  │  Dashboard   │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  日历集成     │  ← Google/Outlook双向同步       │
│                  │  Calendar    │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```



