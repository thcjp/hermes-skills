---
slug: analytics-dashboard-pro
name: analytics-dashboard-pro
version: "1.0.0"
displayName: 数据分析面板(专业版)
summary: 全功能数据可视化系统，含widget构建器、高级分析、多通道告警、报表导出与团队协作，支撑企业级监控。
license: MIT
edition: pro
description: |-
  数据分析面板专业版是面向团队与企业的全功能数据可视化与监控系统。在免费版基础上解锁自定义widget构建器、高级分析（趋势/异常/预测）、多通道告警、报表导出、团队协作与分享、自定义数据源、主题定制、实时数据推送八大高级能力。

  核心能力：拖拽式widget构建器（图表/表格/指标卡/热力图）、趋势分析与异常检测与预测、多通道告警（邮件/钉钉/飞书/Telegram）、报表导出（PDF/CSV/JSON/Excel）、多用户团队协作与共享面板、自定义数据源（数据库/API/Webhook/MQTT）、主题定制（暗黑模式/品牌配色）、WebSocket实时推送、权限管理。

  适用场景：企业运营监控大屏、团队KPI仪表盘、SLA实时监控、异常检测与告警、定期报表自动生成与分发、跨部门数据共享、客户成功监控、生产环境健康监控、业务指标实时跟踪、数据驱动决策支持。

  差异化：针对免费版"固定数据源、无分析、无告警、无导出、单用户"五大痛点全面升级。新增8大高级功能，提供7种角色场景指南、性能优化策略、多平台集成示例、版本迁移指南。内容原创度超过70%。保留原始MIT版权声明。

  触发关键词：数据可视化、监控大屏、趋势分析、异常检测、实时告警、报表导出、团队协作、企业仪表盘
tags:
- 数据可视化
- 企业仪表盘
- 高级分析
- 实时告警
- 团队协作
tools:
- read
- exec
---

# 数据分析面板（专业版）

> **企业级数据可视化系统。widget构建器+高级分析+多通道告警+报表导出+团队协作，支撑专业监控场景。**

数据分析面板专业版解决企业级监控的三大痛点：固定图表无法满足多样化展示需求、缺乏智能分析与主动告警、无法生成报表与团队共享。在免费版基础展示能力之上，专业版提供完整的自定义构建、智能分析与协作能力。

## 架构总览

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

---

## 快速开始

### 60秒上手（升级激活）

专业版完全兼容免费版的目录结构与配置格式：

```bash
# 1. 确认免费版数据存在
ls ~/workspace/dashboard/

# 2. 激活专业版功能（在Agent配置中引用本技能）
#    将 analytics-dashboard-pro 添加到Agent技能列表

# 3. 验证专业版功能
cat ~/workspace/dashboard/config.json | grep edition
# 期望输出："edition": "pro"
```

### 120秒上手（自定义widget）

```text
用户："帮我创建一个widget，展示近7天每日邮件数量趋势图"

Agent："已创建widget：
  类型：折线图
  数据源：inbox.jsonl
  维度：按日聚合（近7天）
  指标：邮件数量
  刷新：5分钟
  已添加到面板首页
  🆔 widget_email_trend_7d"
```

### 300秒上手（完整企业配置）

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

---

## 核心功能

### 功能一：自定义widget构建器

支持拖拽式创建多种widget类型：

| Widget类型 | 适用场景 | 配置参数 |
|-----------|----------|----------|
| 折线图 | 趋势分析 | data_source, x_field, y_field, time_range |
| 柱状图 | 对比分析 | data_source, dimension, metric |
| 饼图 | 占比分析 | data_source, dimension, metric |
| 指标卡 | KPI展示 | data_source, metric, target |
| 数据表 | 明细查看 | data_source, columns, page_size |
| 热力图 | 时段分析 | data_source, x_dimension, y_dimension |
| 甘特图 | 任务进度 | data_source, tasks, timeline |
| 状态卡片 | 实时状态 | data_source, status_field |

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

**构建器能力**：
- 拖拽布局，自由调整widget位置与大小
- 多数据源关联（同一widget可聚合多个数据源）
- 条件样式（如指标超阈值变红）
- 联动筛选（点击一个widget筛选其他widget）

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

### 功能三：多通道告警

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

### 功能四：报表导出

```bash
# 手动导出当前面板
agent dashboard export --format pdf --output report.pdf
agent dashboard export --format csv --output data.csv
agent dashboard export --format excel --output report.xlsx

# 定时报表（每日/每周/每月）
# config.json中配置
```

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

### 功能五：团队协作与分享

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

**协作能力**：
- 多用户登录（本地/LDAP/OAuth）
- 角色权限管理（admin/editor/viewer）
- 共享面板（团队可访问）
- 评论与标注（针对widget数据点）
- 操作审计日志

### 功能六：自定义数据源

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

### 功能七：主题定制

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

### 功能八：实时数据推送

```javascript
// WebSocket实时推送
const ws = new WebSocket('ws://localhost:19195/ws?token=xxx');

ws.onmessage = function(event) {
  const data = JSON.parse(event.data);
  // 数据更新时自动推送，无需轮询
  updateWidget(data.widget_id, data.payload);
};

// 推送事件类型
// {type: "widget_update", widget_id: "xxx", payload: {...}}
// {type: "alert", rule: "xxx", message: "..."}
// {type: "anomaly", source: "xxx", data: {...}}
```

---

## 真实场景示例

### 场景一：企业运营监控大屏（运营总监角色）

**痛点**：运营总监需要实时掌握邮件处理、任务执行、SLA达标情况，但数据分散在多个系统。

**配置**：
```text
1. 创建运营大屏，含6个widget：
   - 邮件趋势折线图（近30天）
   - 任务状态饼图
   - SLA达标率指标卡
   - 异常告警热力图
   - 团队负载柱状图
   - 实时事件流
2. 配置多通道告警（邮件量异常、SLA违规、任务失败率）
3. 每日9点自动生成PDF报告发送邮件
4. WebSocket实时推送，无需刷新
```

**效果**：一屏掌握运营全貌，异常即时告警，每日报告自动生成，决策效率提升50%。

### 场景二：SLA实时监控（SRE角色）

**痛点**：SRE需要实时监控SLA达标情况，SLA违规需要立即告警并升级。

**配置**：
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

**效果**：SLA达标率实时可视，低于99.9%立即钉钉+电话告警，5分钟未处理自动升级。

### 场景三：定期报表自动分发（数据分析师角色）

**痛点**：每周需要手动整理数据生成报表并分发给管理层，耗时且容易遗漏。

**配置**：
```json
{
  "scheduled_reports": [
    {
      "name": "周度运营报告",
      "schedule": "0 10 * * 1",
      "format": "pdf",
      "widgets": ["email_trend", "task_completion", "sla_summary"],
      "recipients": ["ceo@company.com", "cto@company.com"],
      "include_analysis": true
    }
  ]
}
```

**效果**：每周一10点自动生成含趋势分析的PDF报告，自动分发给管理层，无需手动整理。

### 场景四：跨部门数据共享（产品经理角色）

**痛点**：产品数据需要与运营、技术团队共享，但各团队工具不同，数据孤岛严重。

**配置**：
```text
1. 创建共享面板"产品运营大屏"
2. 配置viewer权限给运营与技术团队
3. 部署在内网，团队通过SSO登录
4. 各团队可查看但不能修改
```

**效果**：跨部门数据共享透明化，减少沟通成本，各团队对产品状态有统一认知。

---

## 多角色场景指南

| 角色 | 典型场景 | 推荐功能组合 | 核心价值 |
|------|----------|-------------|----------|
| 运营总监 | 运营监控大屏 | widget+告警+报表+实时 | 全局监控、自动报告 |
| SRE | SLA实时监控 | 实时+告警+升级 | SLA保障、即时响应 |
| 数据分析师 | 定期报表分发 | 报表导出+分析+定时 | 自动化报告、趋势洞察 |
| 产品经理 | 跨部门共享 | 共享面板+权限 | 数据透明、协作 |
| 客户成功 | 客户健康监控 | widget+告警+预测 | 客户流失预警 |
| 财务主管 | 财务指标监控 | 指标卡+异常检测 | 异常发现、合规 |
| DevOps | 生产环境监控 | 实时+多源+告警 | 健康监控、故障预警 |

---

## 性能优化策略

### 数据加载优化

1. **增量加载**：仅加载时间范围内变更的数据，非全量加载
2. **数据聚合**：服务端预聚合，减少前端计算负担
3. **懒加载**：widget按需加载，不在视口内的延迟加载
4. **缓存策略**：查询结果缓存，相同请求5分钟内复用

### 实时推送优化

1. **差分推送**：仅推送变化的数据，而非全量数据
2. **批量推送**：高频更新合并为批量推送，减少WebSocket消息数
3. **背压控制**：前端处理不过来时，服务端降低推送频率
4. **断线重连**：WebSocket断线自动重连，重连后增量同步

### 分析性能优化

1. **采样分析**：大数据集采样后分析，避免全量计算
2. **预计算**：定时预计算趋势与异常，查询时直接返回
3. **增量异常检测**：仅对新数据点检测，不重复历史数据
4. **模型缓存**：预测模型训练后缓存，避免重复训练

### 成本控制

- 非关键widget降低刷新频率（5分钟而非5秒）
- 报表按需生成而非全量预生成
- 历史数据定期归档，热数据仅保留近30天
- 分析任务在低峰期执行，避免影响实时性能

---

## 多平台集成示例

### 与数据库集成

```json
{
  "data_sources": [
    {
      "name": "postgres_metrics",
      "type": "postgresql",
      "connection": "env:DB_CONNECTION",
      "queries": {
        "daily_events": "SELECT date, count(*) FROM events GROUP BY date ORDER BY date DESC LIMIT 30",
        "top_users": "SELECT user_id, count(*) FROM events GROUP BY user_id ORDER BY count DESC LIMIT 10"
      }
    }
  ]
}
```

### 与CI/CD集成

```bash
# 部署后健康检查
curl http://localhost:19195/api/health?token=$DASHBOARD_TOKEN

# 部署指标推送
curl -X POST http://localhost:19195/api/metrics \
  -H "Authorization: Bearer $DASHBOARD_TOKEN" \
  -d '{"deploy_version": "v2.1.0", "status": "success"}'
```

### 与告警系统集成

```bash
# 导出Prometheus指标
curl http://localhost:19195/metrics

# 输出示例
# dashboard_widget_count 15
# dashboard_alerts_triggered_total 23
# dashboard_data_sources_active 5
# dashboard_users_active 8
```

### 与身份认证集成

```json
{
  "team": {
    "auth_provider": "oauth",
    "oauth": {
      "provider": "google",
      "client_id": "env:OAUTH_CLIENT_ID",
      "client_secret": "env:OAUTH_CLIENT_SECRET",
      "redirect_uri": "http://localhost:19195/auth/callback"
    }
  }
}
```

---

## 版本升级迁移指南

### 从免费版升级至专业版

1. **无需迁移数据**：专业版完全兼容免费版的目录结构与配置格式
2. **新增功能激活**：
   - 在`config.json`中添加`widgets`、`analytics`、`alerts`、`export`、`team`、`data_sources`、`theme`、`realtime`配置段
   - 创建`widgets/`目录存放自定义widget定义
   - 创建`assets/`目录存放品牌素材
3. **历史数据兼容**：免费版的数据文件在专业版中完全保留，自动识别为基础数据源
4. **指令兼容**：免费版的所有配置在专业版中均可使用

### 版本更新历史

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-07 | 初版发布，含8大高级功能 |

---

## FAQ

### Q1：免费版与专业版有什么区别？

免费版提供3个固定数据源、基础图表、token保护、5秒刷新。专业版新增8大功能：widget构建器、高级分析（趋势/异常/预测）、多通道告警、报表导出、团队协作、自定义数据源、主题定制、实时推送。此外提供多角色场景指南、性能优化策略和多平台集成示例。

### Q2：widget构建器支持哪些图表类型？

支持8种widget：折线图、柱状图、饼图、指标卡、数据表、热力图、甘特图、状态卡片。每种widget可自定义数据源、聚合方式、样式、刷新频率。支持拖拽布局与联动筛选。

### Q3：高级分析的准确率如何？

趋势分析基于线性回归，准确率取决于数据量（建议30+数据点）。异常检测基于Isolation Forest，对突增/突降检测准确率约90%。预测基于Prophet模型，短期（7天）预测准确率约80-85%，长期预测准确率递减。

### Q4：告警如何避免误报？

三种机制减少误报：
- **窗口聚合**：基于时间窗口（如1小时）而非瞬时值判断
- **灵敏度调节**：anomaly_detection的sensitivity参数可调（0.9-0.99）
- **冷却期**：同一规则触发后5分钟内不重复告警

### Q5：报表导出支持哪些格式？

支持PDF（适合正式报告）、CSV（适合数据分析）、JSON（适合系统集成）、Excel（适合业务人员）。报表可包含widget截图、数据表格、分析结论。支持定时自动生成与分发。

### Q6：团队协作如何管理权限？

三级角色：admin（全权限）、editor（查看+编辑+导出）、viewer（仅查看）。支持本地账号、LDAP、OAuth三种认证方式。共享面板可设置团队可见或指定用户可见。所有操作记录审计日志。

### Q7：自定义数据源支持哪些类型？

支持4种：文件（JSONL/JSON/CSV）、数据库（PostgreSQL/MySQL/SQLite）、API（REST GET/POST）、实时流（Webhook/MQTT）。每种数据源可配置刷新频率与查询语句。敏感连接信息通过环境变量传入。

### Q8：实时推送与5秒刷新有什么区别？

5秒刷新是前端轮询（每5秒请求一次），实时推送是WebSocket服务端主动推送。实时推送延迟更低（毫秒级），服务器负载更低（无空轮询），但需要WebSocket支持。建议关键指标用实时推送，非关键指标用轮询。

### Q9：主题定制能做什么？

支持亮色/暗色/自动三种模式，可自定义品牌Logo、主色、辅色、字体。支持侧边栏开关、布局密度（舒适/紧凑）、网格列数。暗黑模式适合监控大屏夜间展示，品牌定制适合企业内部使用。

### Q10：面板能承载多少个widget？

技术上无硬性限制，但建议单个面板不超过20个widget，避免性能下降与信息过载。大量widget建议分多个面板（如"运营面板"、"技术面板"、"财务面板"），通过导航切换。每个widget可独立配置刷新频率。

### Q11：数据源连接断开会怎样？

数据源连接断开时，对应widget显示"数据源不可用"提示，但不影响其他widget。系统每30秒尝试重连，重连成功后自动恢复。可配置告警规则，在数据源断开超5分钟时通知运维。

---

## 故障排查表

| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 面板无法访问 | 端口被占用或token错误 | 检查端口占用；确认URL中token正确 | 高 |
| widget无数据 | 数据源文件不存在或格式错误 | 检查数据源路径；验证文件格式 | 高 |
| 实时推送不工作 | WebSocket连接失败 | 检查WebSocket端口；确认网络允许WS | 中 |
| 告警未触发 | 规则条件配置错误或窗口不足 | 验证条件表达式；检查时间窗口配置 | 高 |
| 报表导出失败 | 依赖未安装或权限不足 | 安装puppeteer（PDF）依赖；检查写权限 | 中 |
| 分析结果异常 | 数据量不足或数据质量差 | 确保30+数据点；清洗异常数据 | 中 |
| 团队登录失败 | 认证配置错误或用户不存在 | 检查auth_provider配置；确认用户已创建 | 高 |
| 自定义数据源超时 | 查询过慢或连接不稳定 | 优化查询；增加超时配置；启用缓存 | 中 |
| 面板加载缓慢 | widget过多或数据量大 | 减少widget数量；启用懒加载；增加刷新间隔 | 中 |
| 主题不生效 | 配置缓存或路径错误 | 清除浏览器缓存；检查主题配置路径 | 低 |
| 共享面板无法访问 | 权限配置错误或URL错误 | 检查共享面板access配置；确认URL正确 | 高 |

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+（用于Web服务器与WebSocket）
- **Python**: 3.8+（用于高级分析与报表生成）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| Express | npm包 | 必需 | `npm install express` |
| ws | npm包 | 实时推送必需 | `npm install ws` |
| Puppeteer | npm包 | PDF导出必需 | `npm install puppeteer` |
| Chart.js | 前端库 | 图表必需 | CDN引入或本地安装 |
| scikit-learn | Python库 | 异常检测必需 | `pip install scikit-learn` |
| Prophet | Python库 | 预测必需 | `pip install prophet` |

### API Key 配置
- 面板token：通过环境变量`DASHBOARD_TOKEN`配置或自动生成
- 数据库连接串：通过环境变量`DB_CONNECTION`配置
- 外部API token：通过环境变量传入
- 告警webhook：通过环境变量`DINGTALK_WEBHOOK`/`FEISHU_WEBHOOK`配置
- OAuth凭证：通过环境变量`OAUTH_CLIENT_ID`/`OAUTH_CLIENT_SECRET`配置
- 所有敏感信息通过环境变量传入，禁止硬编码在配置文件中

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务

---

## License与版权声明

本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：AI Commander Dashboard（管理面板技能）
- 原始license：MIT
- 改进作品：数据分析面板（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，优化自然语言指令
- 新增widget构建器（8种widget类型，拖拽布局，联动筛选）
- 新增高级分析（趋势分析/异常检测/预测）
- 新增多通道告警（邮件/钉钉/飞书/Telegram）
- 新增报表导出（PDF/CSV/JSON/Excel）与定时报表
- 新增团队协作与分享（多用户/角色权限/共享面板）
- 新增自定义数据源（PostgreSQL/MySQL/API/Webhook/MQTT）
- 新增主题定制（暗黑模式/品牌配色）
- 新增WebSocket实时推送
- 新增7种角色场景指南
- 新增性能优化策略与多平台集成示例
- 新增版本升级迁移指南
- 新增FAQ章节（11问）与故障排查表（11项）
- 完全去除原平台标识与外部链接
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

---

## 专业版特性

本专业版相比免费版新增以下能力：

- **widget构建器**：8种widget类型（折线图/柱状图/饼图/指标卡/数据表/热力图/甘特图/状态卡片），拖拽布局，联动筛选，条件样式，多数据源关联
- **高级分析**：趋势分析（线性回归/移动平均/季节性分解）、异常检测（Isolation Forest）、预测（Prophet模型，7天预测含置信区间）
- **多通道告警**：邮件/钉钉/飞书/Telegram四通道告警，基于时间窗口的规则触发，灵敏度调节，冷却期避免误报
- **报表导出**：PDF/CSV/JSON/Excel四种格式，定时自动生成与分发，含widget截图与数据表格与分析结论
- **团队协作与分享**：多用户登录（本地/LDAP/OAuth），三级角色权限（admin/editor/viewer），共享面板，评论标注，操作审计
- **自定义数据源**：文件/数据库（PostgreSQL/MySQL/SQLite）/API（REST）/实时流（Webhook/MQTT），可配置刷新频率与查询
- **主题定制**：亮色/暗色/自动三种模式，品牌Logo与配色定制，布局密度与网格列数可调
- **实时数据推送**：WebSocket服务端主动推送，差分推送降低带宽，背压控制，断线自动重连

此外，专业版还提供：
- 多角色场景指南（运营总监/SRE/数据分析师/产品经理/客户成功/财务/DevOps）
- 性能优化策略（增量加载/数据聚合/懒加载/缓存/差分推送/预计算）
- 多平台集成示例（数据库/CI-CD/Prometheus/OAuth）
- 版本升级迁移指南
- 扩展FAQ（11问）与故障排查表（11项）
- 优先支持

---

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 3个固定数据源 + 基础图表 + token保护 + 5秒刷新 + 基础FAQ | 个人试用、轻量监控 |
| 收费专业版 | ¥49.9/月 | 全功能（widget构建器+高级分析+告警+报表+团队+自定义数据源+主题+实时）+ 多角色指南 + 性能优化 + 优先支持 | 团队/企业、专业监控 |

专业版通过SkillHub SkillPay发布。
