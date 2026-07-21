# 详细参考 - analytics-dashboard-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (json)

```json
// ~/workspace/dashboard/config.json
{
  "edition": "pro",
  "port": 19195,
  "host": "0.0.0.0",
  "token": "env:DASHBOARD_TOKEN",
  "refresh_interval": 5,
  "realtime": {
    "enabled": true,
    "transport": "websocket"
  },
  "widgets": {
    "builder_enabled": true,
    "custom_widgets_dir": "./widgets/"
  },
  "analytics": {
    "trend_analysis": true,
    "anomaly_detection": true,
    "forecasting": true,
    "forecast_horizon_days": 7
  },
  "alerts": {
    "channels": ["email", "dingtalk", "feishu"],
    "rules": []
  },
  "export": {
    "formats": ["pdf", "csv", "json", "excel"],
    "scheduled_reports": []
  },
  "team": {
    "enabled": true,
    "auth_provider": "local",
    "roles": ["admin", "viewer"]
  },
  "data_sources": {
    "custom_enabled": true,
    "sources": []
  },
  "theme": {
    "mode": "auto",
    "branding": {}
  }
}
```

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────┐
│            数据分析面板专业版 (ANALYTICS DASHBOARD PRO)            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ Widget构建器  │  │  高级分析     │  │  多通道告警   │           │
│  │ Builder      │  │  Analytics   │  │  Alert Hub   │           │
│  │  ✅ 专业版    │  │  ✅ 专业版    │  │  ✅ 专业版    │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  报表导出     │  ← PDF/CSV/JSON/Excel          │
│                  │  Export      │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  团队协作     │  ← 多用户/共享/权限             │
│                  │  Team        │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  自定义数据源  │  ← DB/API/Webhook/MQTT         │
│                  │  Data Source │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  实时推送     │  ← WebSocket                   │
│                  │  Realtime    │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 代码示例 (json)

```json
{
  "data_sources": {
    "custom_enabled": true,
    "sources": [
      {
        "name": "production_db",
        "type": "postgresql",
        "connection": "env:DB_CONNECTION_STRING",
        "query": "SELECT date, count(*) FROM events GROUP BY date",
        "refresh": 300
      },
      {
        "name": "api_metrics",
        "type": "api",
        "url": "https://api.example.com/metrics",
        "method": "GET",
        "headers": {"Authorization": "env:API_TOKEN"},
        "refresh": 60
      },
      {
        "name": "webhook_events",
        "type": "webhook",
        "path": "/webhook/events",
        "storage": "./data/webhook-events.jsonl"
      },
      {
        "name": "iot_sensor",
        "type": "mqtt",
        "broker": "mqtt://broker.example.com",
        "topic": "sensors/+/temperature"
      }
    ]
  }
}
```

## 代码示例 (json)

```json
{
  "alerts": {
    "channels": {
      "email": {"to": ["ops@company.com"]},
      "dingtalk": {"webhook": "env:DINGTALK_WEBHOOK"},
      "feishu": {"webhook": "env:FEISHU_WEBHOOK"},
      "telegram": {"bot_token": "env:TELEGRAM_BOT_TOKEN", "chat_id": "env:TELEGRAM_CHAT_ID"}
    },
    "rules": [
      {
        "name": "邮件量异常激增",
        "condition": "email_count > avg * 3",
        "window": "1h",
        "channels": ["dingtalk", "email"],
        "message": "邮件量异常：当前{{count}}，历史均值{{avg}}"
      },
      {
        "name": "任务失败率过高",
        "condition": "failure_rate > 0.1",
        "window": "1h",
        "channels": ["dingtalk", "feishu", "email"],
        "message": "任务失败率{{rate}}，超过10%阈值"
      },
      {
        "name": "会话过期预警",
        "condition": "session_status == 'expiring_soon'",
        "channels": ["dingtalk"],
        "message": "浏览器会话即将过期"
      }
    ]
  }
}
```

## 代码示例 (json)

```json
{
  "team": {
    "enabled": true,
    "auth_provider": "local|ldap|oauth",
    "users": [
      {"username": "admin", "role": "admin", "password_hash": "***"},
      {"username": "viewer1", "role": "viewer", "password_hash": "***"}
    ],
    "roles": {
      "admin": ["view", "edit", "manage_users", "export", "configure"],
      "editor": ["view", "edit", "export"],
      "viewer": ["view"]
    },
    "shared_dashboards": [
      {
        "name": "运营监控大屏",
        "url": "/shared/ops-dashboard",
        "access": "team",
        "widgets": ["email_trend", "task_status", "sla_monitor"]
      }
    ]
  }
}
```

## 代码示例 (json)

```json
// ~/workspace/dashboard/widgets/email-trend.json
{
  "id": "widget_email_trend_7d",
  "type": "line_chart",
  "title": "近7天邮件趋势",
  "data_source": {
    "type": "file",
    "path": "./data/inbox.jsonl",
    "aggregation": {
      "dimension": "date",
      "metric": "count",
      "time_range": "7d"
    }
  },
  "x_field": "date",
  "y_field": "count",
  "refresh_interval": 300,
  "style": {
    "color": "#1a73e8",
    "height": 300
  }
}
```

## 代码示例 (json)

```json
// 分析结果示例
{
  "trend": {
    "direction": "increasing",
    "slope": 2.3,
    "confidence": 0.92,
    "description": "邮件数量呈上升趋势，日均增加2.3封"
  },
  "anomalies": [
    {
      "date": "2026-07-15",
      "value": 156,
      "expected": 45,
      "deviation": 3.47,
      "severity": "high"
    }
  ],
  "forecast": [
    {"date": "2026-07-19", "predicted": 52, "lower": 40, "upper": 64},
    {"date": "2026-07-20", "predicted": 55, "lower": 42, "upper": 68}
  ]
}
```

## 代码示例 (json)

```json
{
  "export": {
    "scheduled_reports": [
      {
        "name": "每日运营报告",
        "schedule": "0 9 * * *",
        "format": "pdf",
        "widgets": ["email_trend", "task_status", "session_health"],
        "recipients": ["ops@company.com"],
        "subject": "每日运营报告 - {{date}}"
      },
      {
        "name": "周度总结报告",
        "schedule": "0 10 * * 1",
        "format": "excel",
        "widgets": "all",
        "recipients": ["manager@company.com"],
        "subject": "周度总结 - 第{{week}}周"
      }
    ]
  }
}
```

## 代码示例 (json)

```json
{
  "analytics": {
    "trend_analysis": {
      "enabled": true,
      "methods": ["linear_regression", "moving_average", "seasonal_decompose"],
      "confidence_interval": 0.95
    },
    "anomaly_detection": {
      "enabled": true,
      "algorithm": "isolation_forest",
      "sensitivity": 0.95,
      "min_data_points": 30
    },
    "forecasting": {
      "enabled": true,
      "model": "prophet",
      "horizon_days": 7,
      "confidence_interval": 0.8
    }
  }
}
```

## 代码示例 (json)

```json
{
  "widgets": [
    {
      "type": "gauge",
      "title": "SLA达标率",
      "data_source": "sla_metrics",
      "target": 99.9,
      "thresholds": {"green": 99.9, "yellow": 99.5, "red": 99.0}
    }
  ],
  "alerts": [
    {
      "name": "SLA违规",
      "condition": "sla_rate < 99.9",
      "channels": ["dingtalk", "phone_call"],
      "escalate_after": "5m"
    }
  ]
}
```

## 代码示例 (json)

```json
{
  "theme": {
    "mode": "auto|light|dark",
    "branding": {
      "logo": "./assets/logo.png",
      "primary_color": "#1a73e8",
      "secondary_color": "#34a853",
      "font_family": "Noto Sans SC, sans-serif"
    },
    "layout": {
      "sidebar": true,
      "density": "comfortable|compact",
      "grid_columns": 12
    }
  }
}
```

### 功能二：高级分析
```json
{
  "analytics": {
    "trend_analysis": {
      "enabled": true,
      "methods": ["linear_regression", "moving_average", "seasonal_decompose"],
      "confidence_interval": 0.95
    },
    "anomaly_detection": {
      "enabled": true,
      "algorithm": "isolation_forest",
      "sensitivity": 0.95,
      "min_data_points": 30
    },
    "forecasting": {
      "enabled": true,
      "model": "prophet",
      "horizon_days": 7,
      "confidence_interval": 0.8
    }
  }
}
```

**分析能力**：
- **趋势分析**：线性回归判断上升/下降趋势，移动平均平滑波动，季节性分解识别周期
- **异常检测**：基于Isolation Forest算法，自动识别异常数据点，灵敏度可调
- **预测**：基于历史数据预测未来7天趋势，含置信区间

```json
// 分析结果示例
{
  "trend": {
    "direction": "increasing",
    "slope": 2.3,
    "confidence": 0.92,
    "description": "邮件数量呈上升趋势，日均增加2.3封"
  },
  "anomalies": [
    {
      "date": "2026-07-15",
      "value": 156,
      "expected": 45,
      "deviation": 3.47,
      "severity": "high"
    }
  ],
  "forecast": [
    {"date": "2026-07-19", "predicted": 52, "lower": 40, "upper": 64},
    {"date": "2026-07-20", "predicted": 55, "lower": 42, "upper": 68}
  ]
}
```



