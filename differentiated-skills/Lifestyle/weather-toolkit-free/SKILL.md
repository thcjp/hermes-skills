---
slug: weather-toolkit-free
name: weather-toolkit-free
version: "1.0.0"
displayName: 天气查询工具包免费版
summary: 基于wttr.in与Open-Meteo的免费天气查询,无需API Key,支持当前天气与预报
license: MIT
edition: free
description: |-
  面向个人用户的免费天气查询工具包,基于wttr.in与Open-Meteo公开API,无需API Key即可获取当前天气与预报。

  核心能力:
  - 当前天气快速查询(一行命令)
  - 多格式天气输出(紧凑/完整/PNG)
  - 城市坐标查询与JSON结构化数据
  - 温度、湿度、风速、天气状况、月相
  - 公制与美制单位切换
  - 历史天气基础查询

  适用场景:
  - 个人出行前快速查看天气
  - 脚本中集成天气数据
  - 终端/命令行环境天气查询
  - 开发调试与API验证

  差异化:
  - 完全免费,无需注册与API Key
  - 聚焦核心天气查询功能,轻量高效
  - 支持命令行与脚本两种使用方式
  - 中文优先的天气描述输出
  - 双数据源互为备份,提升可用性

  触发关键词: 天气查询, 实时天气, 天气预报, wttr.in, open-meteo, 免费天气, 当前天气, weather, forecast, 天气工具
tags:
- Lifestyle
- 天气
- 生活工具
- 命令行工具
- 免费API
tools:
- read
- exec
---

# 天气查询工具包免费版

基于 wttr.in 与 Open-Meteo 两大免费公开服务的天气查询工具包,无需API Key,适合个人用户在命令行或脚本中快速获取天气信息。

## 概述

本工具包整合两个免费天气数据源:`wttr.in`(主要,支持中文与多种格式)和 `Open-Meteo`(备选,JSON结构化输出),无需注册与API Key即可使用。支持当前天气查询、天气预报、多格式输出与单位切换,适合个人出行规划与脚本集成。

## 核心能力

| 能力 | 免费版 | 说明 |
|:-----|:------:|:-----|
| 当前天气查询 | 支持 | 一行命令获取 |
| 天气预报 | 支持 | 3天预报 |
| 紧凑格式输出 | 支持 | 适合脚本解析 |
| 完整格式输出 | 支持 | 含详细图表 |
| PNG图片输出 | 支持 | 天气图导出 |
| JSON结构化数据 | 支持 | Open-Meteo源 |
| 单位切换 | 支持 | 公制/美制 |
| 历史天气查询 | 不支持 | 需PRO版 |
| 多城市批量查询 | 不支持 | 需PRO版 |
| 天气预警推送 | 不支持 | 需PRO版 |
| 自定义数据源 | 不支持 | 需PRO版 |

## 使用场景

### 场景一:命令行快速查询天气

```bash
# 最简洁的一行查询
curl -s "wttr.in/Beijing?format=3"

# 输出示例: Beijing: ⛅️ +28°C

# 紧凑格式(位置+天气+温度+湿度+风速)
curl -s "wttr.in/Beijing?format=%l:+%c+%t+%h+%w"

# 完整预报(中文显示)
curl -s "wttr.in/Beijing?lang=zh&T"

# 仅查看当天
curl -s "wttr.in/Beijing?1&lang=zh"

# 仅查看当前状态
curl -s "wttr.in/Beijing?0&lang=zh"
```

### 场景二:脚本中集成天气数据

```python
# Python脚本集成Open-Meteo JSON数据
import urllib.request
import json

def get_weather(lat, lon):
    """获取指定坐标的当前天气"""
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    return data["current_weather"]

# 北京坐标查询示例
weather = get_weather(39.9, 116.4)
print(f"温度: {weather['temperature']}°C")
print(f"风速: {weather['windspeed']} km/h")
print(f"风向: {weather['winddirection']}°")
print(f"天气代码: {weather['weathercode']}")
```

### 场景三:多格式输出与导出

```bash
# 导出天气PNG图片
curl -s "wttr.in/Shanghai.png" -o /tmp/weather_shanghai.png

# 使用机场代码查询
curl -s "wttr.in/JFK?format=3"

# URL编码空格(多词城市名)
curl -s "wttr.in/New+York?format=3"

# 切换单位制式
curl -s "wttr.in/London?m&format=3"   # 公制(默认)
curl -s "wttr.in/London?u&format=3"   # 美制

# wttr.in 格式代码速查:
# %c - 天气状况图标
# %t - 温度
# %h - 湿度
# %w - 风速
# %l - 位置
# %m - 月相
```

## 快速开始

1. **确认环境**:确保系统已安装 `curl`(Windows/macOS/Linux默认自带)
2. **选择数据源**:wttr.in(人类可读)或 Open-Meteo(JSON程序化)
3. **构造查询**:使用城市名或坐标
4. **执行命令**:在终端或脚本中运行
5. **解析结果**:根据格式代码或JSON字段提取所需信息

## 配置示例

```bash
# 免费版天气查询配置(环境变量)
export WEATHER_DEFAULT_SOURCE="wttr"      # 默认数据源: wttr 或 open-meteo
export WEATHER_DEFAULT_LANG="zh"           # 默认语言
export WEATHER_DEFAULT_UNIT="m"            # 默认单位: m(公制) 或 u(美制)
export WEATHER_DEFAULT_FORMAT="3"          # 默认输出格式

# 常用城市坐标配置(用于Open-Meteo)
# 城市:        纬度     经度
# 北京:        39.9     116.4
# 上海:        31.2     121.5
# 广州:        23.1     113.3
# 深圳:        22.5     114.1
# 成都:        30.6     104.1
# 香港:        22.3     114.2
# 台北:        25.0     121.5
# 东京:        35.7     139.7
# 首尔:        37.6     127.0
# 新加坡:      1.4      103.8
```

## 最佳实践

- **优先wttr.in**:人类可读场景优先使用wttr.in,支持中文与丰富格式
- **JSON用Open-Meteo**:程序化处理优先使用Open-Meteo,返回标准JSON
- **备选机制**:wttr.in不可用时自动切换到Open-Meteo
- **缓存结果**:同一城市短时间内的查询结果可缓存,减少请求
- **错误处理**:网络异常时返回友好提示而非报错
- **编码处理**:多词城市名使用 `+` 或 `%20` 编码空格

## 常见问题

### Q1: 真的完全免费吗?有什么限制?

完全免费,无需注册与API Key。wttr.in 与 Open-Meteo 均为公开免费服务。高频请求(每分钟数十次)可能被限流,正常使用不会触发。

### Q2: 支持哪些城市的查询?

几乎所有有人居住的城市都支持。wttr.in 支持城市名、机场代码查询;Open-Meteo 通过经纬度查询,覆盖全球。

### Q3: 天气数据多久更新一次?

- **wttr.in**: 约30分钟更新一次
- **Open-Meteo**: 每小时更新,预报数据最长可达16天

### Q4: 可以查询历史天气吗?

免费版不支持历史天气查询。如需历史数据(如过去30天的天气),请使用PRO版本。

### Q5: 网络异常时如何处理?

```bash
# 带错误处理的查询脚本
#!/bin/bash
CITY=${1:-Beijing}

# 主数据源
result=$(curl -s --max-time 5 "wttr.in/$CITY?format=3" 2>/dev/null)
if [ -n "$result" ] && [ "$result" != *"Unknown"* ]; then
    echo "$result"
    exit 0
fi

# 备选数据源
echo "wttr.in 不可用,切换到 Open-Meteo..."
curl -s --max-time 5 "https://api.open-meteo.com/v1/forecast?latitude=39.9&longitude=116.4&current_weather=true" 2>/dev/null | python -c "
import sys, json
try:
    data = json.load(sys.stdin)
    w = data['current_weather']
    print(f\"{w['temperature']}°C, 风速{w['windspeed']}km/h\")
except:
    print('天气查询失败,请稍后重试')
"
```

### Q6: 如何在脚本中判断天气状况?

```python
# Open-Meteo 天气代码对照表
WEATHER_CODES = {
    0: "晴朗",
    1: "大致晴朗", 2: "局部多云", 3: "阴天",
    45: "雾", 48: "雾凇",
    51: "小毛毛雨", 53: "毛毛雨", 55: "大毛毛雨",
    61: "小雨", 63: "中雨", 65: "大雨",
    71: "小雪", 73: "中雪", 75: "大雪",
    77: "冰粒",
    80: "阵雨", 81: "中阵雨", 82: "大阵雨",
    85: "阵雪", 86: "大阵雪",
    95: "雷暴", 96: "雷暴冰雹", 99: "强雷暴冰雹"
}

def describe_weather(code):
    return WEATHER_CODES.get(code, "未知天气")
```

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **网络连接**: 需要访问公网(wttr.in 与 Open-Meteo)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| wttr.in | 公开API | 可选 | 免费免Key,主要数据源 |
| Open-Meteo | 公开API | 可选 | 免费免Key,备选数据源 |
| curl | 系统工具 | 推荐 | 系统自带,命令行查询 |
| Python 3.x | 运行时 | 可选 | 脚本集成时使用 |

### API Key 配置

- **完全无需API Key**:本工具包使用的所有数据源均为公开免费API
- **wttr.in**: 直接访问 `https://wttr.in/{city}`,无需任何认证
- **Open-Meteo**: 直接访问 `https://api.open-meteo.com/v1/forecast`,无需任何认证
- **无速率限制配置**:正常使用不会触发限流,高频请求建议增加缓存

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
- **免费版限制**: 单城市查询、3天预报、无历史数据、无预警推送、无批量查询
