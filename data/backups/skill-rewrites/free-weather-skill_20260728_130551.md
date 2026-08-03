---
slug: free-weather-skill
name: free-weather-skill
version: "0.1.0"
displayName: Weather
summary: "免API Key获取实时天气与预报,解决出行前需快速了解天气状况的需求"
license: MIT-0
description: |-
  Get current weather and forecasts (no API key required)。核心能力:

  - 生活工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 个人健康、生活管理、习惯养成

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Lifestyle
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---


# Weather

Two free services, no API keys needed.

## wttr.in (primary)

Quick one-liner:

```bash
curl -s "wttr.in/London?format=3"
```

Compact format:

```bash
curl -s "wttr.in/London?format=%l:+%c+%t+%h+%w"
```

Full forecast:

```bash
curl -s "wttr.in/London?T"
```

Format codes: `%c` condition · `%t` temp · `%h` humidity · `%w` wind · `%l` location · `%m` moon

Tips:

* URL-encode spaces: `wttr.in/New+York`
* Airport codes: `wttr.in/JFK`
* Units: `?m` (metric) `?u` (USCS)
* Today only: `?1` · Current only: `?0`
* PNG: `curl -s "wttr.in/Berlin.png" -o /tmp/weather.png`

## Open-Meteo (fallback, JSON)

Free, no key, good for programmatic use:

```bash
curl -s "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"
```

Find coordinates for a city, then query. Returns JSON with temp, windspeed, weathercode.

Docs: <https://open-meteo.com/en/docs>

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

- Get current weather and forecasts (no API key required)
- 触发关键词: weather, forecasts, required, current, free, skill

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

### Q1: 如何开始使用Weather？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Weather有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用

---
## 边界条件与限制 (Boundary Conditions)

### 输入限制
- **地理位置**: 由于技能依赖于外部API，因此输入的地理位置必须是API支持的城市或机场代码。不支持的地理位置将无法提供天气信息。
- **格式规范**: 输入的地理位置必须符合URL编码规范，例如空格应被替换为`+`或`%20`。
- **查询深度**: 对于`wttr.in`服务，查询深度有限制。例如，使用`?T`参数获取完整预报时，可能不会返回所有细节，特别是对于某些地区。

### 性能边界
- **响应时间**: 由于技能依赖于外部API，响应时间受API服务器的性能影响。在高峰时段，响应时间可能会增加。
- **数据更新频率**: 天气数据通常每几分钟更新一次，但具体更新频率取决于所使用的API。

### 兼容性约束
- **操作系统**: 技能应在Windows、macOS和Linux操作系统上运行，但具体兼容性取决于Agent平台的实现。
- **Agent平台**: 技能基于SKILL.md规范，因此应与所有支持SKILL.md规范的AI Agent兼容。
- **网络连接**: 技能需要稳定的网络连接来访问外部API。

### 单位转换
- **温度单位**: 技能默认使用摄氏度（Celsius），但可以通过添加`?u`参数转换为华氏度（Fahrenheit）。
- **风速单位**: 风速单位默认为米/秒（m/s），但可以通过添加`?m`参数转换为英里/小时（mph）。

### 限制条件
- **免费API限制**: 由于技能使用的是免费API，可能存在请求频率限制，超过限制可能导致服务不可用。
- **数据准确性**: 免费API提供的数据可能不如付费API准确，特别是在极端天气条件下。


## 已知限制

- **API Key需求**: 虽然技能描述中提到无需API Key，但在实际使用中，某些API可能需要API Key以访问所有功能。
- **数据覆盖范围**: 免费API可能不提供所有地区的天气数据，特别是偏远地区。
- **功能限制**: 免费API可能不支持所有高级功能，如历史天气数据或特定气象参数的查询。


## 注意事项

- **隐私保护**: 技能在使用过程中不会存储或收集用户的个人信息。
- **免责声明**: 技能提供的信息仅供参考，不应对任何决策产生直接影响。
- **技术支持**: 技能不提供直接的技术支持，用户应自行解决使用过程中遇到的问题。

