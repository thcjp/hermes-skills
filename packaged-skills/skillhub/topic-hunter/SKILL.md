---
slug: topic-hunter
name: topic-hunter
version: "1.0.0"
displayName: "选题捕手"
summary: "一个人顶一个选题编辑部,4平台热榜监控+三类趋势识别+爆款打分,每日Top10直达"
license: MIT
description: |-
  选题捕手——一个人顶一个选题编辑部,4平台热榜监控每日直达爆款选题,告别拍脑袋选题。

  核心能力: 多平台热榜监控 / 上升衰退新兴三类趋势识别 / 商业价值评估过滤敏感话题 / 爆款选题打分 / 创作建议生成 / 突发热点预警 / 预估流量排序

  适用场景: 内容矩阵操盘手每日选题 / 独立博主追热点找方向 / 副业达人借势营销 / 品牌方热点借势投放

  差异化: 不只抓热点,更识别上升/衰退/新兴三类趋势走向;商业价值评估自动过滤敏感话题;突发热点(热度≥80且上升≥50%/h)自动预警;Top10上升+Top5新兴报告每日送达。

  触发关键词: 热点发现、趋势话题、热榜监控、内容创作建议、选题捕手、爆款选题、选题打分
homepage: "https://skillhub.cn"
tags: [选题, 热点追踪, 内容创作, 副业工具]
tools: [read, exec]
---

# 选题捕手 Topic Hunter

热点发现引擎,监控主流内容平台热榜,识别趋势话题,生成创作建议与爆款选题。

## 使用场景

1. 热点监控:定时获取各平台热榜,识别新热点与持续热点
2. 趋势识别:识别上升/衰退/新兴话题,评估商业价值
3. 创作建议:基于热点生成标题方向、内容要素与预估流量
4. 热点预警:突发热点(热度≥80且上升≥50%/h)触发预警通知
5. 选题打分:对候选选题进行内容匹配度与流量潜力综合评分

## 工作流

### 热点监控(monitor)

1. 定时触发,通过网络请求获取多平台热榜(抖音/微博/知乎/小红书)
2. 解析热榜数据:提取话题、热度、排名,去重并标准化
3. 对比历史热点数据(存储于JSON文件),识别新热点与持续热点,标记上升/下降/平稳
4. 保存至本地JSON文件(`hotspots/YYYY-MM-DD.json`),更新热点索引

### 趋势识别(analyze)

1. 手动或定时触发,读取近N天热点数据
2. 计算热度变化率(日环比)
3. 识别三类话题:上升中(环比+20%)、衰退中(环比-20%)、新兴(≤2天但热度高)
4. 商业价值评估:电商相关→高 / 生活日常→中 / 敏感话题→低(过滤)
5. 生成Top10上升+Top5新兴话题报告

### 创作建议(suggest)

1. 接收请求(分类/平台/数量),获取匹配的趋势话题
2. 对每个热点:获取内容模板→生成标题/方向/关键要素→预估流量
3. 按预估流量排序,取Top N

### 热点预警(alert)

1. 条件:新话题热度≥80 且 上升速度≥50%/小时
2. 评估商业价值、情感倾向与风险→生成预警→触发通知→记录存档

### 选题打分(score)

1. 接收候选选题列表与账号定位
2. 从内容匹配度、热度时效性、流量潜力三个维度评分
3. 输出综合得分与推荐排序

## 数据源

| 平台 | 获取方式 | 更新频率 |
|:-----|:---------|:---------|
| 抖音 | 网络请求热榜 | 每2小时 |
| 微博 | 网络请求热搜 | 每2小时 |
| 知乎 | 网络请求热榜 | 每2小时 |
| 小红书 | 网络请求热门 | 每2小时 |

## 异常处理

| 异常 | 错误码 | 处理 |
|:-----|:-------|:-----|
| 平台不可用 | PLATFORM_UNAVAILABLE | 跳过,返回其他平台数据 |
| 数据解析失败 | PARSE_ERROR | 使用缓存数据 |
| 网络请求失败 | NETWORK_ERROR | 重试3次,返回最近成功数据+过期标记 |
| 热榜结构变更 | PARSE_STRUCTURE_CHANGED | 降级为原始HTML解析 |
| 情感分析异常 | SENTIMENT_ERROR | 默认sentiment=neutral |

## 输入格式

```json
{
  "action": "monitor|analyze|suggest|alert|score",
  "category": "ecommerce|lifestyle|tech|entertainment|all",
  "platform": "douyin|weibo|zhihu|xiaohongshu|all",
  "count": 10,
  "days": 7,
  "threshold": {
    "heat_min": 80,
    "rising_rate_min": 0.5
  }
}
```

字段说明:
- `action`: 操作类型(monitor监控热榜/analyze趋势分析/suggest创作建议/alert热点预警/score选题打分)
- `category`: 话题分类筛选(ecommerce电商/lifestyle生活/tech科技/entertainment娱乐/all全部)
- `platform`: 平台筛选(douyin抖音/weibo微博/zhihu知乎/xiaohongshu小红书/all全部)
- `count`: 返回数量(suggest操作使用,默认10)
- `days`: 分析天数(analyze操作使用,默认7,最大30)
- `threshold`: 预警阈值(alert操作使用,heat_min最低热度/rising_rate_min最低上升率)

## 输出格式

```json
{
  "success": true,
  "data": {
    "action": "monitor",
    "trends": [
      {
        "topic": "春季穿搭",
        "heat": 95,
        "rank": 1,
        "platforms": ["douyin", "weibo"],
        "trend": "rising",
        "category": "lifestyle",
        "first_seen": "2026-04-25T08:00:00Z",
        "business_value": "medium",
        "sentiment": "positive"
      }
    ],
    "new_count": 3,
    "rising_count": 5,
    "fetched_at": "2026-04-26T10:00:00Z"
  },
  "error": null,
  "code": null
}
```

字段说明:
- `trends`: 趋势话题数组(topic话题/heat热度0-100/rank排名/platforms出现平台/trend趋势rising/falling/stable)
- `category`: 话题分类
- `business_value`: 商业价值评估(high/medium/low)
- `sentiment`: 情感倾向(positive/neutral/negative)
- `new_count`: 新增热点数(monitor操作返回)
- `rising_count`: 上升热点数(analyze操作返回)

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 |
| 热榜数据源 | API | 可选 | 抖音/微博/知乎/小红书热榜(可手动输入) |
| JSON文件存储 | 文件系统 | 必需 | exec工具创建hotspots/目录 |

### API Key 配置
- **LLM_API_KEY**: 必需(通常由Agent内置) - 趋势识别/创作建议/选题打分
- 配置方式: 在Agent的环境变量中设置

### 纯Markdown使用说明
热榜数据可手动输入。网络请求失败时使用缓存数据并标记过期。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 热点监控

输入:
```json
{"action": "monitor", "platform": "all", "category": "all"}
```

执行流程: 获取4平台热榜 → 解析标准化 → 对比历史识别新热点 → 保存JSON

输出:
```json
{
  "success": true,
  "data": {
    "trends": [
      {"topic": "春季穿搭", "heat": 95, "platforms": ["douyin", "weibo"], "trend": "rising"}
    ],
    "new_count": 3,
    "fetched_at": "2026-04-26T10:00:00Z"
  }
}
```

### 示例2: 趋势分析

输入:
```json
{"action": "analyze", "days": 7}
```

执行流程: 读取近7天热点 → 计算环比变化 → 识别上升/衰退/新兴 → 生成报告

### 示例3: 创作建议

输入:
```json
{"action": "suggest", "category": "ecommerce", "platform": "douyin", "count": 5}
```

执行流程: 匹配电商类上升热点 → 生成标题方向与关键要素 → 预估流量 → 按流量排序取Top5
