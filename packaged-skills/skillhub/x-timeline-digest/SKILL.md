---
slug: x-timeline-digest
name: x-timeline-digest
version: "1.0.0"
displayName: X 时间线摘要
summary: 使用 bird 读取 X/Twitter For You 与 Following 时间线,增量去重后生成中文分类简报与结构化 JSON
license: MIT
description: |-
  基于 bird 命令行工具读取 X(Twitter)的 For You 与 Following 两条时间线,
  对推文进行增量过滤、ID 硬去重、近重复文本合并与排序修剪,
  输出结构化 JSON 负载与中文分类简报。
  简报按 AI 与技术、加密与市场、观点洞察、其他四个类别分组,
  自动剔除广告、早安帖与短文本噪声。
  状态持久化到本地 JSON 文件,避免跨次运行重复推送。
  适用于需要定期追踪 X 动态并生成可读摘要的自动化工作流。
tags:
  - Communication
  - Social Media
  - Digest
tools:
  - read
  - exec
---

# X Timeline Digest

## 概述

本 Skill 通过 bird 命令行工具读取 X/Twitter 的 For You 与 Following 两条时间线,
构建高信号去重摘要。核心处理链路包含拉取、增量过滤、去重、排序修剪、
中文简报生成与结构化输出六个阶段。

简报生成依赖外部 LLM 与 PROMPT.md 模板协作完成:
脚本输出干净的去重 JSON,Agent 读取 PROMPT.md 后将 JSON 注入 LLM,
由 LLM 产出分类中文摘要。

本 Skill 仅负责摘要生成,不处理 Telegram、邮件等投递通道。
投递由上游工作流决定。

---

## 配置

所有配置从 `skills.entries["x-timeline-digest"].config` 读取。

### 配置字段

| 名称 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| intervalHours | number | 6 | 增量窗口小时数 |
| fetchLimitForYou | number | 100 | For You 拉取条数 |
| fetchLimitFollowing | number | 60 | Following 拉取条数 |
| maxItemsPerDigest | number | 25 | 单次摘要最多保留条数 |
| similarityThreshold | number | 0.9 | 近重复文本相似度阈值 |
| statePath | string | ~/.skill-platform/state/x-timeline-digest.json | 状态文件路径 |

---

## 依赖

- bird 已安装并可在 PATH 中调用
- bird 已通过 cookie 完成登录认证
- Node.js 运行时(执行 digest.js)
- 外部 LLM(用于智能简报生成)
- 只读使用,不回写 X 平台

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD（纯Markdown指令，无需exec命令行能力）

## 核心能力

### 时间线拉取
通过 bird 命令分别拉取 For You 与 Following 两条时间线:

- For You:`bird home -n 100 --json`
- Following:`bird home --following -n 60 --json`

`-n` 控制拉取条数,`--json` 输出结构化 JSON。

**输入**: 用户提供时间线拉取所需的指令和必要参数。
**处理**: 按照skill规范执行时间线拉取操作,遵循单一意图原则。### 增量过滤
读取 statePath 中的 lastRunAt,仅保留该时间点之后发布的推文,
避免跨次运行重复处理。已推送的推文 ID 记录在 sentTweetIds 中,
30 天内不会再次进入摘要。

**输入**: 用户提供增量过滤所需的指令和必要参数。
**输出**: 返回增量过滤的执行结果,包含操作状态和输出数据。### 去重
两层去重策略:

- 硬去重:按推文 ID 唯一化
- 近重复合并:基于文本相似度(similarityThreshold 默认 0.9)合并内容相近的推文,
  保留信息量更高的一条

**输入**: 用户提供去重所需的指令和必要参数。
**处理**: 按照skill规范执行去重操作,遵循单一意图原则。
**输出**: 返回去重的执行结果,包含操作状态和输出数据。### 启发式过滤
脚本在输出 JSON 前自动剔除低价值内容:

- 广告推文
- "gm" 等早安帖
- 过短的垃圾文本

**输入**: 用户提供启发式过滤所需的指令和必要参数。
**处理**: 按照skill规范执行启发式过滤操作,遵循单一意图原则。### 排序与修剪
按时间与质量信号排序,裁剪到 maxItemsPerDigest 条。

**输入**: 用户提供排序与修剪所需的指令和必要参数。
**输出**: 返回排序与修剪的执行结果,包含操作状态和输出数据。### 中文分类简报
通过 PROMPT.md 模板与 LLM 协作生成,类别包括:

- AI 与技术
- 加密与市场
- 观点洞察
- 其他

格式为 `[作者](URL): 摘要`,语言为简体中文。

---

**输入**: 用户提供中文分类简报所需的指令和必要参数。
**处理**: 按照skill规范执行中文分类简报操作,遵循单一意图原则。
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: Twitter、增量去重后生成中、文分类简报与结构、命令行工具读取、对推文进行增量过、近重复文本合并与、排序修剪、负载与中文分类简、简报按、其他四个类别分组、自动剔除广告、早安帖与短文本噪、状态持久化到本地、适用于需要定期追、动态并生成可读摘、要的自动化工作流。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`x-timeline-digest`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 适用场景

### 定时信息简报

每 6 小时自动拉取时间线,生成中文分类简报,接入上游投递通道推送到即时通讯工具。
适合需要持续追踪 X 动态但不希望被信息流淹没的信息消费者。

### 主题监控与归档

将多条推文按主题聚合,输出结构化 JSON 存档,供后续检索、复盘或二次分析。
适合研究员、分析师对特定时间段内 X 舆情进行沉淀。

### 噪声清理后的高质量阅读

对 For You 与 Following 时间线做去重与降噪,只保留高信号内容,
适合信息过载用户在固定时间集中阅读。

### 多源合并去重

For You 与 Following 存在大量重叠,本 Skill 在 ID 与文本两层去重,
适合希望合并两条时间线去重阅读的用户。

---

## 使用方式

### 基础用法:原始 JSON

执行摘要生成脚本,获得干净的去重 JSON:

```bash
node skills/x-timeline-digest/digest.js
```

### 智能简报:分类中文摘要

1. 执行脚本并将结果落盘:`node skills/x-timeline-digest/digest.js > digest.json`
2. 读取提示词模板:`read skills/x-timeline-digest/PROMPT.md`
3. 将 digest.json 内容注入 PROMPT.md 中的数据占位位置,发送给 LLM
4. LLM 返回分类中文简报

脚本会自动应用启发式过滤(移除 gm、广告、短垃圾文本)后再输出 JSON。

---

## 状态管理

状态持久化到 statePath 指定的 JSON 文件。

### 状态结构

```json
{
  "lastRunAt": "2026-02-01T00:00:00+08:00",
  "sentTweetIds": {
    "123456789": "2026-02-01T00:00:00+08:00"
  }
}
```

### 规则

- 已存在于 sentTweetIds 的推文不会再次进入摘要
- 成功运行后更新 lastRunAt,并将本次推送的推文 ID 写入 sentTweetIds
- 推文 ID 至少保留 30 天

---

## 输出结构

脚本返回单个 JSON 对象:

```json
{
  "window": {
    "start": "2026-02-01T00:00:00+08:00",
    "end": "2026-02-01T06:00:00+08:00",
    "intervalHours": 6
  },
  "counts": {
    "forYouFetched": 100,
    "followingFetched": 60,
    "afterIncremental": 34,
    "afterDedup": 26,
    "final": 20
  },
  "digestText": "中文摘要内容",
  "items": [
    {
      "id": "123456",
      "author": "@handle",
      "createdAt": "2026-02-01T02:15:00+08:00",
      "text": "推文正文",
      "url": "https://x.com/handle/status/123456",
      "sources": ["following"]
    }
  ]
}
```

counts 字段反映各阶段过滤后的剩余条数,可用于调参与健康度检查。

---

## 案例

### 案例:每日早晨简报生成

用户希望每天早晨获得前一天 X 上的重要动态。
将 intervalHours 设为 24,fetchLimitForYou 设为 200,
配合定时任务在每天早晨执行 digest.js,再将 digest.json 注入 LLM 生成中文简报,
接入即时通讯投递通道。counts 字段可用于观察信息密度变化。

### 案例:特定主题舆情归档

研究员希望按周归档 X 上与某主题相关的讨论。
保持默认配置每周执行一次,将每次输出的 items 数组追加到归档文件,
利用 sources 字段区分 For You 与 Following 来源,
后续可对 author 与 text 做二次分析。近重复合并确保归档库中不会出现大量转发副本。

### 案例:降噪阅读列表

信息过载用户不希望实时刷信息流。
每 6 小时运行一次,将 final 条数控制在 20 以内,
只阅读中文简报与高排序推文,避免被广告与早安帖干扰。

---

## 异常处理


### bird 未安装或不在 PATH

执行 bird 命令时报 command not found。
确认 bird 已安装,执行 `which bird` 或 `where bird` 检查路径,
未安装时先完成安装再加入 PATH。

### bird 未完成 cookie 登录

bird 返回认证失败或空结果。
执行 bird 的登录子命令完成 cookie 登录后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令,
登录态过期时需要重新登录。

### Node.js 运行时缺失

执行 digest.js 报 node 不是内部命令。
安装 Node.js 并确认 `node --version` 可正常输出版本号。

### statePath 不可写

脚本无法写入状态文件,导致 lastRunAt 不更新,下次运行会重复处理。
检查 statePath 所在目录是否存在且有写权限,
默认路径 `~/.skill-platform/state/` 需要提前创建。

### 近重复阈值过高导致漏合并

similarityThreshold 设为 0.9 时,仅高度相似的推文会被合并,
内容相近但表述不同的转发可能各自保留。
若发现摘要中仍有大量重复信息,可下调阈值到 0.8 左右观察效果。

### LLM 简报生成失败

PROMPT.md 注入 digest.json 后 LLM 返回异常或格式不符合预期。
确认 digest.json 为合法 JSON,检查 PROMPT.md 中的数据占位位置,
必要时将 JSON 截断到更小体积后再注入。

### 拉取条数为 0

bird 返回空数组,counts 中 forYouFetched 与 followingFetched 均为 0。
确认 bird 登录态有效,执行ping命令测试网络连通性,检查防火墙和代理设置连通性,
账号被限流时适当拉长 intervalHours 后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令。

### 推文 ID 过早被清理

sentTweetIds 中的 ID 不足 30 天即被清除,导致重复推送。
检查是否有外部进程清理了 statePath 文件,
确认脚本未因异常中断而跳过状态写入步骤。

---

## 常见问题

### 智能简报必须依赖 LLM 吗?

基础 JSON 输出不依赖 LLM,直接执行 digest.js 即可获得去重后的结构化数据。
中文分类简报需要 LLM 配合 PROMPT.md 生成,无 LLM 环境只能获得原始 JSON。

### For You 与 Following 的拉取条数如何取舍?

For You 信息密度较低、噪声较多,建议拉取较多条数(默认 100)再靠过滤压缩。
Following 信号更集中,默认 60 条通常足够。
可根据关注账号活跃度调整。

### 状态文件被删除会怎样?

sentTweetIds 丢失后,已推送过的推文会在下次运行时被当作新推文再次进入摘要。
建议将 statePath 设置在有备份的目录,避免误删。

### 可以同时拉取多条时间线以外的数据吗?

本 Skill 仅处理 For You 与 Following 两条时间线,
列表、搜索、单条推文拉取不在范围内,
需要扩展时建议新建独立 Skill 而非修改本 Skill。

### intervalHours 设得多小合适?

默认 6 小时适合多数信息消费节奏。
低于 1 小时会导致增量过滤效果减弱、重复率上升,
不建议低于 2 小时。

### 简报中的 URL 为什么是 x.com 而不是 twitter.com?

X 平台已迁移域名,推文链接统一使用 x.com,
bird 返回的 url 字段即为 x.com 格式,简报中应保持一致。

---

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖 bird 命令行工具,不提供替代拉取方式
- 依赖外部 LLM 生成中文简报,无 LLM 环境仅输出原始 JSON
- 仅处理 For You 与 Following 两条时间线,不支持列表与搜索
- 投递通道(Telegram、邮件等)不在本 Skill 范围内
- 近重复合并基于文本相似度,语义近似但表述差异大的内容可能漏合并
- bird 登录态过期需要人工重新认证,无法自动续期
- 推文 ID 保留策略固定为 30 天,不可配置
- 受 X 平台限流影响,短时间内高频运行可能拉取失败
