---
slug: health-toolkit-pro
name: health-toolkit-pro
version: "1.0.0"
displayName: 健康管理工具箱专业版
summary: 企业级健康管理平台,支持多用户、设备同步、AI建议与医疗级报告
license: MIT
edition: pro
description: |-
  面向家庭、企业健康关怀与医疗机构的健康管理平台。
  核心能力: 多用户管理、可穿戴设备同步、AI个性化建议、医疗级报告、异常预警、专业分析
  适用场景: 家庭健康管理、企业员工健康关怀、健身工作室会员管理、慢病管理
  差异化: 专业版支持多用户与专业能力,与免费版数据格式兼容
  触发关键词: 多用户健康, 设备同步, AI健康建议, 医疗报告, 异常预警, 慢病管理
tags:
- 健康管理
- 企业级
- 多用户
- 设备同步
- AI建议
- 医疗报告
tools:
- read
- exec
---

# 健康管理工具箱 (专业版)

## 概述

专业版面向家庭、企业健康关怀项目与医疗机构,在免费版个人健康管理之上,扩展多用户管理、可穿戴设备同步、AI 个性化建议、医疗级报告、异常预警、专业分析等企业级能力。支持家庭多成员管理、企业员工健康关怀、健身工作室会员跟踪、慢病管理等场景。

专业版与免费版数据格式完全兼容,个人用户升级后历史数据无缝迁移。

## 核心能力

| 能力模块 | 描述 | 免费版 | 专业版 |
|:--------|:-----|:------:|:------:|
| 运动记录 | 跑步、力量等 | 支持 | 支持 |
| 睡眠追踪 | 睡眠时长、质量 | 支持 | 支持 |
| 饮食日记 | 食物摄入、热量 | 支持 | 支持 |
| 健康指标 | 体重、心率、血压 | 支持 | 支持 |
| 多用户管理 | 家庭/团队成员 | 不支持 | 支持 |
| 设备同步 | 可穿戴设备 | 不支持 | 支持 |
| AI 建议 | 个性化健康建议 | 基础 | 高级 |
| 医疗报告 | 医疗级报告 | 不支持 | 支持 |
| 异常预警 | 健康风险预警 | 不支持 | 支持 |
| 慢病管理 | 慢性病跟踪 | 不支持 | 支持 |
| 数据导出 | 医生共享 | 不支持 | 支持 |
| 优先支持 | 专属支持 | 不支持 | 支持 |

## 使用场景

### 场景一: 家庭健康管理

管理全家人健康数据,关注每位成员状况。

```python
import os
import requests
from datetime import datetime

API_BASE = "https://api.health-toolkit-pro.local/v1"
ADMIN_KEY = os.environ["HEALTH_ADMIN_KEY"]

class FamilyHealthManager:
    def __init__(self, admin_key):
        self.headers = {"X-API-Key": admin_key, "X-Edition": "pro"}

    def add_member(self, name, age, gender, relation):
        """添加家庭成员"""
        payload = {
            "name": name,
            "age": age,
            "gender": gender,
            "relation": relation,  # self, spouse, child, parent
            "health_profile": {
                "height_cm": None,
                "weight_kg": None,
                "blood_type": None,
                "allergies": [],
                "medications": [],
                "chronic_conditions": [],
            },
        }
        resp = requests.post(
            f"{API_BASE}/members",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        return resp.json()

    def family_dashboard(self):
        """家庭健康仪表盘"""
        resp = requests.get(
            f"{API_BASE}/family/dashboard",
            headers=self.headers,
            timeout=60,
        )
        return resp.json()

    def member_report(self, member_id, period="month"):
        """生成成员健康报告"""
        resp = requests.get(
            f"{API_BASE}/members/{member_id}/report",
            headers=self.headers,
            params={"period": period},
            timeout=120,
        )
        return resp.json()

    def health_alerts(self):
        """获取健康预警"""
        resp = requests.get(
            f"{API_BASE}/alerts",
            headers=self.headers,
            timeout=30,
        )
        return resp.json()


manager = FamilyHealthManager(ADMIN_KEY)
manager.add_member("张三", 35, "male", "self")
manager.add_member("李四", 33, "female", "spouse")
manager.add_member("张小明", 8, "male", "child")
```

### 场景二: 可穿戴设备同步

自动同步智能手表、手环等设备数据。

```python
class DeviceSyncManager:
    def __init__(self, admin_key):
        self.headers = {"X-API-Key": admin_key}

    def connect_device(self, member_id, device_type, credentials):
        """连接可穿戴设备"""
        payload = {
            "member_id": member_id,
            "device_type": device_type,  # apple_watch, fitbit, garmin, huawei_band
            "credentials": credentials,
            "sync_frequency": "realtime",
            "data_types": [
                "heart_rate", "steps", "sleep", "workout",
                "blood_oxygen", "ecg", "stress"
            ],
        }
        resp = requests.post(
            f"{API_BASE}/devices/connect",
            headers=self.headers,
            json=payload,
            timeout=60,
        )
        return resp.json()

    def sync_now(self, device_id):
        """立即同步"""
        resp = requests.post(
            f"{API_BASE}/devices/{device_id}/sync",
            headers=self.headers,
            timeout=60,
        )
        return resp.json()

    def sync_history(self, device_id, start_date, end_date):
        """同步历史数据"""
        payload = {
            "device_id": device_id,
            "start": start_date,
            "end": end_date,
        }
        resp = requests.post(
            f"{API_BASE}/devices/{device_id}/sync-history",
            headers=self.headers,
            json=payload,
            timeout=300,
        )
        return resp.json()


sync = DeviceSyncManager(ADMIN_KEY)
# 连接 Apple Watch
sync.connect_device("member_001", "apple_watch", {"token": "..."})
```

### 场景三: AI 个性化建议

基于个人健康数据生成 AI 建议。

```python
def generate_ai_advice(member_id):
    """生成 AI 个性化健康建议"""
    payload = {
        "member_id": member_id,
        "advice_types": [
            "exercise_plan",      # 运动计划
            "nutrition_guide",    # 营养指导
            "sleep_optimization", # 睡眠优化
            "stress_management",  # 压力管理
            "risk_prevention",   # 风险预防
        ],
        "based_on": [
            "health_history",
            "current_metrics",
            "lifestyle_patterns",
            "genetic_factors",
            "age_gender",
        ],
        "personalization": "high",
    }
    resp = requests.post(
        f"{API_BASE}/ai/advice",
        headers=manager.headers,
        json=payload,
        timeout=120,
    )
    return resp.json()

# 输出示例
# {
#   "exercise_plan": {
#     "weekly_schedule": [...],
#     "intensity_progression": "逐渐增加",
#     "specific_exercises": [...]
#   },
#   "nutrition_guide": {
#     "daily_calories_target": 2000,
#     "macros": {"protein": "30%", "carbs": "40%", "fat": "30%"},
#     "meal_suggestions": [...]
#   },
#   "risk_prevention": {
#     "identified_risks": ["久坐", "睡眠不足"],
#     "recommendations": [...]
#   }
# }
```

## 快速开始

### 步骤 1: 申请专业版账户

联系销售开通专业版,获取管理员凭证与租户 ID。

### 步骤 2: 配置凭证

```bash
export HEALTH_ADMIN_KEY="sk_pro_admin_xxx"
export HEALTH_ORG_ID="org_your_id"
export HEALTH_EDITION="pro"
```

### 步骤 3: 添加家庭成员

```bash
curl -X POST -H "X-API-Key: $HEALTH_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name":"张三","age":35,"gender":"male","relation":"self"}' \
  "https://api.health-toolkit-pro.local/v1/members"
```

### 步骤 4: 连接设备

```bash
curl -X POST -H "X-API-Key: $HEALTH_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{"member_id":"m001","device_type":"apple_watch","credentials":{"token":"..."}}' \
  "https://api.health-toolkit-pro.local/v1/devices/connect"
```

## 配置示例

### 企业级配置

```yaml
# /etc/health-toolkit/pro.yaml
edition: pro
api:
  base_url: https://api.health-toolkit-pro.local/v1
  admin_key: ${HEALTH_ADMIN_KEY}
  org_id: ${HEALTH_ORG_ID}
  timeout: 120

family:
  max_members: 20
  roles: [admin, member, viewer]
  permissions:
    admin: [manage_all, view_all, edit_all]
    member: [view_own, edit_own]
    viewer: [view_own]

devices:
  supported: [apple_watch, fitbit, garmin, huawei_band, xiaomi_band]
  sync_frequency: realtime
  data_types: [heart_rate, steps, sleep, workout, blood_oxygen, ecg, stress]

ai_advice:
  enabled: true
  models: [exercise, nutrition, sleep, stress, risk]
  personalization: high
  update_frequency: daily

medical_reports:
  formats: [pdf, hl7_fhir]
  share_with_doctor: true
  include_charts: true
  language: zh

alerts:
  enabled: true
  thresholds:
    heart_rate_high: 120
    heart_rate_low: 50
    blood_pressure_high: "140/90"
    sleep_deficit_hours: 6
    inactivity_days: 3
  channels: [push, email, sms]

chronic_disease:
  supported: [diabetes, hypertension, hyperlipidemia, asthma]
  tracking_metrics: [...]
  medication_reminder: true
  doctor_sharing: true

data_security:
  encryption: AES-256
  hipaa_compliant: true
  gdpr_compliant: true
  data_residency: cn
```

### 异常预警配置

```python
def configure_alerts(member_id, thresholds):
    """配置健康预警阈值"""
    payload = {
        "member_id": member_id,
        "thresholds": thresholds,
        "channels": [
            {"type": "push", "priority": "high"},
            {"type": "email", "priority": "medium"},
            {"type": "sms", "priority": "critical"},
        ],
        "quiet_hours": {"start": "22:00", "end": "07:00"},
    }
    resp = requests.post(
        f"{API_BASE}/alerts/configure",
        headers=manager.headers,
        json=payload,
        timeout=30,
    )
    return resp.json()

# 配置预警
configure_alerts("m001", {
    "heart_rate_high": 120,
    "heart_rate_low": 50,
    "blood_pressure_high": "140/90",
    "blood_oxygen_low": 95,
    "sleep_deficit_hours": 6,
    "inactivity_days": 3,
    "weight_change_pct": 5,  # 一周体重变化超过 5%
})
```

### 医疗报告生成

```python
def generate_medical_report(member_id, period, share_with_doctor=True):
    """生成医疗级报告"""
    payload = {
        "member_id": member_id,
        "period": period,
        "format": "hl7_fhir",  # 医疗标准格式
        "sections": [
            "vital_signs_summary",
            "heart_rate_analysis",
            "blood_pressure_trends",
            "sleep_quality_assessment",
            "activity_summary",
            "risk_assessment",
            "recommendations",
        ],
        "include_charts": True,
        "share_with_doctor": share_with_doctor,
        "doctor_email": "doctor@hospital.com" if share_with_doctor else None,
    }
    resp = requests.post(
        f"{API_BASE}/reports/medical",
        headers=manager.headers,
        json=payload,
        timeout=300,
    )
    return resp.json()
```

### 慢病管理

```python
def setup_chronic_disease_tracking(member_id, condition, medications):
    """配置慢病管理"""
    payload = {
        "member_id": member_id,
        "condition": condition,  # diabetes, hypertension, ...
        "tracking_metrics": get_condition_metrics(condition),
        "medications": medications,
        "reminders": {
            "medication": True,
            "measurement": True,
            "checkup": True,
        },
        "targets": get_condition_targets(condition),
    }
    resp = requests.post(
        f"{API_BASE}/chronic/setup",
        headers=manager.headers,
        json=payload,
        timeout=60,
    )
    return resp.json()

# 糖尿病管理
setup_chronic_disease_tracking("m001", "diabetes", [
    {"name": "二甲双胍", "dose": "500mg", "schedule": "每日两次,饭后"},
])
```

## 最佳实践

### 1. 多成员数据隔离

```python
def with_member_context(member_id, func):
    """成员上下文装饰器"""
    def wrapper(*args, **kwargs):
        prev_value = os.environ.get("HEALTH_MEMBER_ID")
        os.environ["HEALTH_MEMBER_ID"] = member_id
        try:
            return func(*args, **kwargs)
        finally:
            if prev_value:
                os.environ["HEALTH_MEMBER_ID"] = prev_value
            else:
                os.environ.pop("HEALTH_MEMBER_ID", None)
    return wrapper
```

### 2. 数据安全

```python
def encrypt_health_data(data, key):
    """加密健康数据 (AES-256)"""
    from cryptography.fernet import Fernet
    f = Fernet(key)
    return f.encrypt(json.dumps(data).encode())

def decrypt_health_data(encrypted, key):
    """解密健康数据"""
    from cryptography.fernet import Fernet
    f = Fernet(key)
    return json.loads(f.decrypt(encrypted).decode())
```

### 3. 定期报告自动化

```python
def schedule_monthly_reports():
    """定时生成月度报告"""
    payload = {
        "schedule": "0 8 1 * *",  # 每月 1 日 8 点
        "task": "generate_monthly_reports",
        "params": {
            "format": "pdf",
            "share_with_doctor": True,
            "email_to_members": True,
        },
    }
    resp = requests.post(
        f"{API_BASE}/schedules",
        headers=manager.headers,
        json=payload,
        timeout=30,
    )
    return resp.json()
```

## 常见问题

### Q1: 专业版与免费版数据兼容吗?

完全兼容。专业版在免费版数据格式上扩展,升级后历史数据无缝迁移。

### Q2: 支持哪些可穿戴设备?

Apple Watch、Fitbit、Garmin、华为手环、小米手环等主流设备。

### Q3: 医疗报告是否符合标准?

支持 HL7 FHIR 医疗数据标准,可直接与医院系统对接。

### Q4: 慢病管理支持哪些疾病?

糖尿病、高血压、高血脂、哮喘等常见慢性病。

### Q5: 数据安全如何保障?

传输加密 (TLS 1.3)、存储加密 (AES-256)、符合 HIPAA、GDPR 等合规要求,数据可指定存储区域。

## 依赖说明

### 运行环境

- **Agent 平台**: 支持 SKILL.md 规范的任意 AI Agent (Claude Code、Cursor、Codex、Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux (生产环境推荐 Linux)
- **网络**: 需访问专业版服务
- **Python**: 3.9+ (用于脚本化操作)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Health Toolkit Pro API | 在线 API | 必需 | 联系销售开通专业版 |
| LLM API | 推理服务 | 必需 | 由 Agent 内置 LLM 提供 |
| Python 3.9+ | 运行时 | 推荐 | python.org 下载 |
| requests 库 | Python 库 | 推荐 | `pip install requests` |
| cryptography | Python 库 | 可选 | `pip install cryptography` (数据加密) |
| 数据库 | 持久化 | 可选 | 兼容主流关系型数据库 (使用 `数据库` 上下文) |

### API Key 配置

```bash
# 专业版凭证
export HEALTH_ADMIN_KEY="sk_pro_admin_xxx"
export HEALTH_ORG_ID="org_your_id"
export HEALTH_EDITION="pro"

# 可选: 设备同步凭证
export APPLE_HEALTH_TOKEN="..."
export FITBIT_TOKEN="..."
export GARMIN_TOKEN="..."

# 可选: 通知渠道
export ALERT_EMAIL="alerts@example.com"
export ALERT_SMS_API="https://sms-api.example.com"
```

### 可用性分类

- **分类**: MD+EXEC (Markdown 指令 + 命令行执行)
- **说明**: 本 Skill 面向家庭、企业与医疗机构,通过自然语言指令驱动 Agent 调用 Pro API,完成多用户健康管理与专业分析
- **专业版特性**: 多用户管理、设备同步、AI 建议、医疗报告、异常预警、慢病管理、数据加密
- **兼容性**: 与免费版数据格式完全兼容,支持平滑升级
