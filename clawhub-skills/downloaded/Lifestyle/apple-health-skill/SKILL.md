---
slug: apple-health-skill
name: apple-health-skill
version: "1.0.0"
displayName: Apple Health Skill
summary: "查询Apple Health运动心率活动数据,将分散健康指标转为可问答的结构化洞察"
  rate, activity rings, a...
license: MIT
description: |-
  Talk to your Apple Health data — ask questions about your workouts,
  heart rate, activity rings, a。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Lifestyle
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Apple Health Skill

Chat with your Apple Health data using AI. Ask about your workouts, heart rate trends, activity rings, VO2 Max, and more. Powered by [Transition](https://www.transition.fun), which syncs with Apple Health to give AI agents access to your fitness data.

## Setup

1. Download [Transition](https://www.transition.fun) and grant Apple Health access
2. Go to **Settings > API Keys** and tap **Generate New Key**
3. Set the environment variable:

```bash
export TRANSITION_API_KEY="[REDACTED]"
```

## No Auth Required

### Workout of the Day

Generate a random structured workout — no account needed.

```bash
curl "https://api.transition.fun/api/v1/wod?sport=run&duration=45"
```

**Parameters:**

* `sport` — `run`, `bike`, `swim`, or `strength` (default: `run`)
* `duration` — minutes, 10-300 (default: `45`)

## Authenticated Endpoints

**Base URL:** `https://api.transition.fun`
**Auth:** Pass `X-API-Key` header on every request.

### AI Coach Chat

Ask questions about your Apple Health data. The AI coach has full context on your workouts and health metrics.

```bash
curl -X POST -H "X-API-Key: $TRANSITION_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"message": "How has my resting heart rate changed over the last month?"}' \
  "https://api.transition.fun/api/v1/coach/chat"
```

Example questions:

* "How many workouts did I do this week?"
* "What's my VO2 Max trend?"
* "How has my sleep been trending this week?"
* "Compare my running pace this month vs last month"
* "Should I take a rest day based on my recent training?"

### Get Workouts

Retrieve scheduled workouts for a date range.

```bash
curl -H "X-API-Key: $TRANSITION_API_KEY" \
  "https://api.transition.fun/api/v1/workouts?start=2026-02-09&end=2026-02-15"
```

**Parameters:**

* `start` — Start date (YYYY-MM-DD, required)
* `end` — End date (YYYY-MM-DD, required)
* Maximum range between `start` and `end` is 90 days.

### Performance Management Chart (PMC)

Get CTL (fitness), ATL (fatigue), and TSB (form) calculated from your Apple Health workouts.

```bash
curl -H "X-API-Key: $TRANSITION_API_KEY" \
  "https://api.transition.fun/api/v1/performance/pmc"
```

### Performance Stats

Get FTP, threshold paces, heart rate zones, and other metrics derived from your Apple Health data.

```bash
curl -H "X-API-Key: $TRANSITION_API_KEY" \
  "https://api.transition.fun/api/v1/performance/stats"
```

### Athlete Profile

```bash
curl -H "X-API-Key: $TRANSITION_API_KEY" \
  "https://api.transition.fun/api/v1/profile"
```

### Chat History

```bash
curl -H "X-API-Key: $TRANSITION_API_KEY" \
  "https://api.transition.fun/api/v1/coach/history"
```

## Rate Limits

| Tier | Read Endpoints | AI Endpoints |
| --- | --- | --- |
| Free | 100/day | 3/day |
| Paid | 10,000/day | 100/day |

## Tips for Agents

1. **Use coach chat as the primary interface.** It has full context on the user's Apple Health workouts, heart rate, and performance — just ask natural questions.
2. **Check fatigue before recommending hard workouts.** Call `GET /api/v1/performance/pmc` and look at TSB. If TSB is below -20, the athlete is fatigued.
3. **Use the free WOD endpoint for quick workouts.** No auth needed — great for users who just want a workout suggestion.
4. **Date format is always YYYY-MM-DD** for all date parameters.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Talk to your Apple Health data — ask questions about your workouts,
  heart rate, activity rings, a
- 触发关键词: health, data, apple, talk, skill

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Apple Health Skill？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Apple Health Skill有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
