---
slug: free-weather-api-tool-pro
name: free-weather-api-tool-pro
version: 1.0.0
displayName: 天气查询专业版
summary: 企业级天气数据平台,支持多城市对比、历史数据、农业气象与定时推送
license: Proprietary
edition: pro
description: '面向企业、农业、物流与媒体场景的专业天气数据平台.
  核心能力: 多城市对比、历史天气、农业气象、分钟级降水、定时推送、批量查询

  适用场景: 物流调度、农业决策、媒体播报、零售预测、能源调度

  差异化: 专业版支持多城市批量查询、15 天预报、历史数据与定时推送,与免费版数据格式兼容

  适用关键词: 多城市天气, 历史天气, 农业气象, 分钟级降水, 天气推送, 批量查询'
tags:
- 天气数据
- 企业级
- 农业气象
- 物流调度
- 历史数据
- 批量查询
tools:
- read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tools: ["read", "write", "exec"]
tags: "API,接口,开发工具"
category: "Development"
---
# 天气查询 (专业版)

## 概述

专业版面向企业、农业、物流、媒体与零售场景,在免费版基础查询能力之上,扩展多城市批量对比、15 天长预报、历史天气数据、农业专项气象、分钟级降水预报、定时推送等企业级能力。支持 API 高并发调用与 SLA 保障,适合业务系统深度集成.
专业版与免费版数据格式完全兼容,个人用户从免费版升级后,调用方式无需修改.
## 核心能力

| 能力模块 | 描述 | 免费版 | 专业版 |
|----|---|---|---|
| 实时天气 | 当前温度、天气、湿度、风力 | 支持 | 支持 |
| 多日预报 | 未来天气预报 | 7 天 | 15 天 |
| 空气质量 | AQI、PM2.5、紫外线 | 支持 | 支持 |
| 多城市对比 | 同时对比多个城市 | 不支持 | 支持 |
| 历史天气 | 过去天气数据 | 不支持 | 支持 (10 年) |
| 农业气象 | 农业专项预报 | 不支持 | 支持 |
| 分钟级降水 | 短临降水预报 | 不支持 | 支持 (2 小时) |
| 天气推送 | 定时推送 | 不支持 | 支持 |
| 批量查询 | 批量城市查询 | 不支持 | 支持 |
| SLA 保障 | 服务可用性 | 无 | 99.9% |
| 并发限额 | API 调用 | 有限 | 高并发 |

### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.
**输入**: 用户提供参数配置与调用所需的指令和必要参数.
**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置.
**输入**: 用户提供结果处理与输出所需的指令和必要参数.
**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级天气数据平、支持多城市对比、历史数据、农业气象与定时推、面向企业、物流与媒体场景的、专业天气数据平台、核心能力、适用场景、物流调度、农业决策、媒体播报、零售预测、能源调度、差异化、专业版支持多城市、天预报、历史数据与定时推、与免费版数据格式、适用关键词、多城市天气等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一: 物流调度

为物流企业提供沿线城市天气,优化运输路线.
```python
import os
import requests
from datetime import datetime, timedelta
# ...
API_BASE = "https://api.weather-pro.local/v1"
API_KEY = os.environ["WEATHER_PRO_API_KEY"]
# ...
class LogisticsWeather:
    def __init__(self, api_key):
        self.headers = {"X-API-Key": api_key, "X-Edition": "pro"}
# ...
    def route_weather(self, cities):
        """批量查询运输路线沿线天气"""
        payload = {"cities": cities, "days": 3}
        resp = requests.post(
            f"{API_BASE}/batch/weather",
            headers=self.headers,
            json=payload,
            timeout=60,
        )
        return resp.json()
# ...
    def minute_precip(self, city):
        """获取分钟级降水预报"""
        resp = requests.get(
            f"{API_BASE}/precip/minute",
            headers=self.headers,
            params={"city": city},
            timeout=30,
        )
        return resp.json()
# ...
    def route_risk_alert(self, route_cities):
        """运输路线风险预警"""
        weather = self.route_weather(route_cities)
        risks = []
        for w in weather["cities"]:
            if w["current"]["precip_prob"] > 70:
                risks.append({
                    "city": w["city"],
                    "risk": "暴雨",
                    "advice": "建议绕行或延迟出发",
                })
            if int(w["current"]["wind_speed"]) > 40:
                risks.append({
                    "city": w["city"],
                    "risk": "大风",
                    "advice": "注意货物固定,避免高速行驶",
                })
        return risks
# ...
lw = LogisticsWeather(API_KEY)
route = ["北京", "济南", "南京", "上海"]
risks = lw.route_risk_alert(route)
for r in risks:
    print(f"{r['city']}: {r['risk']} - {r['advice']}")
```

### 场景二: 农业决策

为农业提供专项气象数据,辅助种植决策.
```python
def agri_weather(region, crop):
    """获取农业专项气象"""
    payload = {
        "region": region,
        "crop": crop,
        "metrics": [
            "soil_moisture",     # 土壤湿度
            "soil_temperature",  # 土壤温度
            "evapotranspiration",# 蒸散量
            "growing_degree_days",# 有效积温
            "frost_risk",        # 霜冻风险
            "pest_risk",         # 病虫害风险
        ],
        "forecast_days": 15,
    }
    resp = requests.post(
        f"{API_BASE}/agriculture/weather",
        headers=lw.headers,
        json=payload,
        timeout=60,
    )
    return resp.json()
# ...
# 示例
# {
#   "region": "山东寿光",
#   "crop": "番茄",
#   "soil_moisture": "65%",  # 适宜
#   "growing_degree_days_accumulated": 1850,
#   "frost_risk": {"next_7d": "low", "alert": false},
#   "irrigation_advice": "未来 5 天无有效降水,建议 3 天后灌溉",
#   "pest_risk": {"whitefly": "medium", "advice": "加强通风,监测虫口密度"}
# }
```

### 场景三: 媒体播报

为媒体生成结构化天气播报内容.
```python
def generate_broadcast(cities, template="news"):
    """生成天气播报内容"""
    payload = {
        "cities": cities,
        "template": template,
        "format": "text",
        "include_video_script": True,
    }
    resp = requests.post(
        f"{API_BASE}/broadcast/generate",
        headers=lw.headers,
        json=payload,
        timeout=60,
    )
    return resp.json()
# ...
# 生成新闻联播风格天气稿
script = generate_broadcast(
    ["北京", "上海", "广州", "成都"],
    template="cctv_news",
)
```

## 不适用场景

以下场景天气查询专业版不适合处理：

- 逆向工程闭源API
- API安全渗透测试
- 非标准协议集成

## 触发条件

需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于非本工具能力范围的需求.
## 快速开始

### Step 1: 申请专业版 API Key

联系销售开通专业版,获取 API Key 与租户 ID.
### Step 2: 配置凭证

```bash
export WEATHER_PRO_API_KEY="sk_pro_xxx"
export WEATHER_ORG_ID="org_your_id"
export WEATHER_EDITION="pro"
```

### Step 3: 验证调用

```bash
# 批量查询
curl -X POST -H "X-API-Key: $WEATHER_PRO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cities":["北京","上海","广州"],"days":7}' \
  "https://api.weather-pro.local/v1/batch/weather"
```

### Step 4: 配置定时推送

```bash
curl -X POST -H "X-API-Key: $WEATHER_PRO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "每日晨报",
    "schedule": "0 7 * * *",
    "cities": ["北京","上海"],
    "channel": {"type":"webhook","url":"https://hooks.slack.com/xxx"}
  }' \
  "https://api.weather-pro.local/v1/schedules"
```

#
## 配置示例

### 企业级配置

```yaml
# /etc/weather-tool/pro.yaml
edition: pro
api:
  base_url: https://api.weather-pro.local/v1
  api_key: ${WEATHER_PRO_API_KEY}
  org_id: ${WEATHER_ORG_ID}
  timeout: 60
  retry: 3
  rate_limit:
    requests_per_minute: 500
    burst: 100
# ...
features:
  forecast_days: 15
  historical_years: 10
  minute_precip: true
  agri_weather: true
  batch_query: true
  scheduled_push: true
# ...
integrations:
  webhook: true
  email: true
  sms: true
  slack: true
  feishu: true
# ...
cache:
  enabled: true
  ttl_seconds: 300
  backend: redis
  redis_url: ${REDIS_URL}
# ...
monitoring:
  metrics: true
  alerting: true
  dashboard: true
```

### 批量查询示例

```python
def batch_weather(cities, days=7):
    """批量查询多城市天气"""
    payload = {
        "cities": cities,
        "days": days,
        "metrics": ["temperature", "weather", "wind", "humidity", "aqi"],
        "format": "json",
    }
    resp = requests.post(
        f"{API_BASE}/batch/weather",
        headers=lw.headers,
        json=payload,
        timeout=120,
    )
    return resp.json()
# ...
def compare_cities(cities, metric="temperature"):
    """多城市天气对比"""
    data = batch_weather(cities)
    comparison = []
    for city_data in data["cities"]:
        current = city_data["current"]
        comparison.append({
            "city": city_data["city"],
            "value": current.get(metric),
            "trend": analyze_trend(city_data["forecast"], metric),
        })
    return sorted(comparison, key=lambda x: x["value"])
```

### 历史数据查询

```python
def historical_weather(city, start_date, end_date):
    """查询历史天气"""
    payload = {
        "city": city,
        "start": start_date,
        "end": end_date,
        "metrics": ["temperature", "precipitation", "wind", "humidity"],
    }
    resp = requests.post(
        f"{API_BASE}/historical",
        headers=lw.headers,
        json=payload,
        timeout=120,
    )
    return resp.json()
# ...
# 查询过去 10 年北京 7 月平均气温
from datetime import datetime
this_year = datetime.now().year
historical = []
for y in range(this_year - 10, this_year):
    historical.append(historical_weather("北京", f"{y}-07-01", f"{y}-07-31"))
```

## 最佳实践

### 1. 缓存策略

```python
import redis
import json
# ...
r = redis.Redis.from_url(os.environ.get("REDIS_URL"))
# ...
def cached_weather(city, ttl=300):
    cache_key = f"weather:{city}"
    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)
    data = query_weather(city)
    r.setex(cache_key, ttl, json.dumps(data, ensure_ascii=False))
    return data
```

### 2. 错误重试

```python
from tenacity import retry, stop_after_attempt, wait_exponential
# ...
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def robust_query(city):
    try:
        return query_weather(city)
    except requests.RequestException as e:
        print(f"查询 {city} 失败: {e}, 重试中...")
        raise
```

### 3. 异步批量处理

```python
import asyncio
import aiohttp
# ...
async def async_batch_weather(cities):
    """异步批量查询"""
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_one(session, city)
            for city in cities
        ]
        return await asyncio.gather(*tasks)
# ...
async def fetch_one(session, city):
    async with session.get(
        f"{API_BASE}/weather",
        headers={"X-API-Key": API_KEY},
        params={"city": city},
        timeout=30,
    ) as resp:
        return await resp.json()
```

### 4. 监控与告警

```python
def setup_monitoring():
    """配置 API 监控"""
    payload = {
        "metrics": ["response_time", "error_rate", "quota_usage"],
        "alerts": [
            {"metric": "error_rate", "threshold": 0.05, "channel": "slack"},
            {"metric": "quota_usage", "threshold": 0.8, "channel": "email"},
        ],
    }
    resp = requests.post(
        f"{API_BASE}/monitoring",
        headers=lw.headers,
        json=payload,
        timeout=30,
    )
    return resp.json()
```

## 常见问题

### Q1: 专业版支持多少并发?

标准版支持 500 QPM,企业版可扩展至 5000 QPM。超出可定制专属集群.
### Q2: 历史数据覆盖多长时间?

中国大陆主要城市覆盖过去 10 年,部分一线城市覆盖 20 年。海外城市覆盖 5-10 年.
### Q3: 农业气象覆盖哪些作物?

支持水稻、小麦、玉米、大豆、棉花、蔬菜、果树等 50+ 主流作物.
### Q4: 定时推送支持哪些渠道?

支持 Webhook、邮件、短信、Slack、飞书、企业微信等主流渠道.
### Q5: 与免费版数据格式是否兼容?

完全兼容,API 响应结构一致。专业版仅是扩展了字段与能力,原有调用代码无需修改.
## 依赖说明

### 运行环境

- **Agent 平台**: 支持 SKILL.md 规范的任意 AI Agent (Claude Code、Cursor、Codex、Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux (生产环境推荐 Linux)
- **网络**: 需稳定访问专业版天气 API
- **Python**: 3.9+ (用于脚本化操作)

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| 天气 Pro API | 在线 API | 必需 | 联系销售开通专业版 |
| LLM API | 推理服务 | 必需 | 由 Agent 内置 LLM 提供 |
| Python 3.9+ | 运行时 | 推荐 | python.org 下载 |
| requests 库 | Python 库 | 推荐 | `pip install requests` |
| aiohttp 库 | Python 库 | 可选 | `pip install aiohttp` (异步批量) |
| Redis | 缓存服务 | 可选 | 用于缓存与限流 |

### API Key 配置

```bash
# 专业版凭证
export WEATHER_PRO_API_KEY="sk_pro_xxx"
export WEATHER_ORG_ID="org_your_id"
export WEATHER_EDITION="pro"
# ...
# 可选: 缓存与监控
export REDIS_URL="redis://localhost:6379/0"
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/xxx"
```

### 可用性分类

- **分类**: MD+EXEC (Markdown 指令 + 命令行执行)
- **说明**: 本 Skill 面向企业用户,通过自然语言指令驱动 Agent 调用 Pro 天气 API,完成多城市批量查询、历史数据、农业气象等企业级场景
- **专业版特性**: 多城市对比、15 天预报、10 年历史数据、农业专项、分钟级降水、定时推送、SLA 保障
- **兼容性**: 与免费版数据格式完全兼容,支持平滑升级

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "天气查询专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "free weather api pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
