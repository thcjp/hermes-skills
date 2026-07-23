---
slug: "timer"
name: "timer"
version: "1.0.0"
displayName: "后台定时器与提醒"
summary: "在后台运行定时器与闹钟，完成后通过系统通知提醒用户，支持多种时间格式与多任务并行管理。"
license: "Proprietary"
description: |-
  在后台设置定时器和闹钟。当后台定时器完成时，会收到系统通知，必须将提醒内容传达给用户。
  支持秒、分、时及复合时间格式，可同时运行多个独立定时器，每个定时器以独立后台进程运行并拥有唯一 sessionId。
  适用于烹饪计时、番茄工作法、会议提醒、任务切换、休息提醒等需要准确倒计时与到期通知的场景。
  可对运行中的定时器执行列出、轮询、查看日志、终止等管理操作。
tags:
  - 通用办公
  - Productivity
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
---
# timer

在后台运行定时器。当定时器完成时，你会收到一条系统通知，必须以提醒形式告知用户。每个定时器作为独立后台进程运行，拥有唯一 sessionId，支持并行运行多个定时器并分别管理。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 后台定时器与提醒处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 后台定时器与提醒格式与多任务并行管理 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |

## Quick Start

```bash
bash background:true command:"node {baseDir}/timer.js 5m"
bash background:true command:"node {baseDir}/timer.js 10m 'Check the oven'"
bash background:true command:"node {baseDir}/timer.js 30s"
bash background:true command:"node {baseDir}/timer.js 1h"
```

第一个参数为时长，第二个可选参数为提醒文案。提醒文案会在定时器完成时回传给 Agent，再由 Agent 转达给用户。若不提供文案，将使用默认提示。

**执行步骤**:

1. 准备输入参数并确认运行环境
2. 执行核心操作,处理输入数据
3. 验证处理结果的正确性

**结果处理**: 执行完成后,输出格式化的处理结果供用户查看和保存。结果包含执行状态、输出数据和错误信息(如有)。

## Time Formats

| Format | Description | Example |
|----:|----:|----:|
| `Ns` | N 秒 | `30s`, `90s` |
| `Nm` | N 分钟 | `5m`, `15m` |
| `Nh` | N 小时 | `1h`, `2h` |
| `N` | N 分钟（默认单位） | `5` 等价于 5 分钟 |
| `MM:SS` | 分:秒 | `5:30` |
| `HH:MM:SS` | 时:分:秒 | `1:30:00` |

未带单位时默认按分钟解析。带冒号的格式按位置解析为时、分、秒，缺省高位视为 0。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

- 后台倒计时：以独立进程运行，不阻塞当前会话，完成后通过系统通知触发 Agent 响应
- 多时间格式：支持秒、分、时、纯数字（默认分钟）、`MM:SS`、`HH:MM:SS` 六种格式互转
- 自定义提醒文案：第二个参数作为到期提醒文本回传，支持任意语言、emoji 与常见标点
- 多定时器并行：每个定时器独立 sessionId，可同时运行烹饪、会议、休息等多个计时任务互不干扰
- 进程生命周期管理：列出运行中定时器、轮询状态、查看日志、按 sessionId 终止
- 完成回传约定：完成时退出码为 0，被 kill 终止时退出码为 130，便于 Agent 区分正常完成与取消
- 进度日志输出：短定时器每秒记录一次进度，长定时器每 10 秒记录一次，可按需查看剩余时间
#
## 适用场景

### 烹饪与厨房计时
用户在做饭时需要精确的倒计时提醒，例如意面 12 分钟、蒸蛋 8 分钟、烘焙 45 分钟。可同时启动多个食材计时，每个到期独立提醒，避免漏关火或煮过头。提醒文案可具体到食材名称，到期时直接告知用户该处理哪一道菜。

### 番茄工作法与专注节奏
启动 25 分钟专注计时，完成后提示休息；紧接着启动 5 分钟休息计时，完成后提示回到工作。形成专注-休息循环，帮助维持节奏而无需手动看表。Agent 在每次完成通知到达时自动启动下一阶段，实现连续循环。

### 会议与日程提醒
在会议开始前 5 分钟、10 分钟分别启动提醒，或在长会议中设置每 30 分钟一次的轮询点，到期通过系统通知打断当前对话，确保重要节点不被遗漏。适合需要准时参加线上会议或切换会场的远程办公场景。

### 任务切换与休息
长时间编码或写作后设置 90 分钟提醒起身活动，或为上下文切换的任务设置分段计时，到期提醒帮助及时切换上下文，避免单一任务超时。可与番茄工作法组合使用，形成多层级的专注-休息节奏。

## 使用案例

### 案例一：并行烹饪计时

用户同时煮意面、蒸蛋、烤面包，需要在各自完成时分别提醒。

```bash
bash background:true command:"node {baseDir}/timer.js 12m 'Pasta is ready!'"
bash background:true command:"node {baseDir}/timer.js 8m 'Eggs are done'"
bash background:true command:"node {baseDir}/timer.js 25m 'Bread is done'"
```

每个定时器独立运行，到期后分别收到系统通知。Agent 收到通知后应立即向用户转达对应提醒，例如："⏰ 您的 8 分钟计时已到：Eggs are done"。三个定时器互不影响，即使意面计时仍在运行，蒸蛋到期也会准时提醒。

### 案例二：番茄工作法循环

用户希望进行两轮番茄工作法，每轮专注 25 分钟、休息 5 分钟。

```bash
bash background:true command:"node {baseDir}/timer.js 25m 'Pomodoro done - time for a break!'"
# 专注计时完成后，再启动休息计时
bash background:true command:"node {baseDir}/timer.js 5m 'Break over - back to work!'"
```

专注计时到期时提醒休息，休息计时到期时提醒回到工作。Agent 在每次系统通知到达时，直接以提醒文案开头回复用户，不要附加无关上下文。需要继续下一轮时，由 Agent 再次启动 25 分钟专注计时。

### 案例三：会议前分段提醒

用户在 14:00 有会议，当前时间 13:45，希望提前 10 分钟和准点各提醒一次。

```bash
bash background:true command:"node {baseDir}/timer.js 10m 'Meeting in 10 minutes'"
bash background:true command:"node {baseDir}/timer.js 15m 'Meeting starts now'"
```

两个定时器并行运行，分别在 13:55 和 14:00 触发。Agent 收到通知后直接转达，确保用户在会议前有充足准备时间。提前 10 分钟的提醒让用户有时间收尾当前工作，准点提醒确保不迟到。

## Timer Completion Notification

当定时器完成时，会收到一条 `System:` 消息，格式如下：

```text
System: [2026-01-24 21:27:13] Exec completed (swift-me, code 0) :: ⏰ Timer complete! Check the pasta!
```

### 回复约定

收到完成通知后，回复必须直接以提醒内容开头，例如：

```text
⏰ Timer Alert! Your timer is complete: Check the pasta!
```

不要以 `HEARTBEAT_OK` 开头。以 `HEARTBEAT_OK` 开头且后续内容少于 300 字符的回复会被自动过滤，用户将收不到提醒，导致定时器形同虚设。

退出码含义：
- `code 0`：定时器正常完成，应向用户转达提醒文案
- `code 130`：定时器被 kill 终止，属于用户主动取消，无需再提示到期

## Managing Timers

```bash
# 列出所有运行中的后台进程（含定时器）
process action:list
# ...
# 轮询指定 sessionId 的当前状态
process action:poll sessionId:XXX
# ...
# 查看指定 sessionId 的输出日志
process action:log sessionId:XXX
# ...
# 终止指定 sessionId 的定时器
process action:kill sessionId:XXX
```

`list` 返回所有后台进程及其 sessionId，用于定位需要管理的定时器。`poll` 返回当前是否仍在运行。`log` 返回进度输出，短定时器每秒记录一次，长定时器每 10 秒记录一次，可从中读取剩余时间。`kill` 终止后会触发退出码 130 的完成通知，Agent 应识别为取消而非到期。

## 异常处理

### 启动命令未识别 time 参数
当第一个参数为空或无法解析为已知时间格式时，timer.js 会立即退出并输出错误。处理：确认参数使用了支持的格式（`Ns`/`Nm`/`Nh`/`N`/`MM:SS`/`HH:MM:SS`），不要传入纯字符串如 "ten minutes" 或空值。

### 提醒文案含特殊字符导致命令解析失败
当提醒文案中包含单引号或双引号时，可能导致 shell 解析截断，文案被切断或命令报错。处理：用与外层不同的引号包裹文案，或将文案中的引号转义；复杂文案建议仅用字母、数字、空格与常见标点。

### 完成通知未送达用户
若 Agent 回复以 `HEARTBEAT_OK` 开头且字符数不足 300，回复会被自动过滤，用户收不到提醒。处理：回复直接以提醒文案开头（如 `⏰ ...`），不要以 `HEARTBEAT_OK` 开头，也不要在提醒前加无关的会话上下文。

### kill 后仍收到完成通知
通过 `process action:kill` 终止定时器后，仍会收到一条退出码为 130 的完成通知。这是预期行为而非错误。处理：将退出码 130 识别为"用户已取消"，不必再向用户提示到期，也无需重新启动同名定时器。

### macOS 下无声音提示
timer.js 在 macOS 上尝试调用 `afplay` 播放提示音。若 `afplay` 不可用或被系统静音，定时器仍会正常完成并回传文案，只是无声音。处理：确认系统未静音且 `afplay` 存在，或仅依赖 Agent 的文本提醒作为到期信号。

### sessionId 找不到
`poll`/`log`/`kill` 传入不存在的 sessionId 时，会返回找不到进程的错误。处理：先执行 `process action:list` 获取当前有效的 sessionId 列表，再使用列表中实际存在的 sessionId，避免使用已结束定时器的旧 sessionId。

### 长时间定时器日志过长
数小时的定时器会累积大量进度日志，全量拉取会占用较多上下文。处理：仅在需要排查时调用 `log`；日常管理用 `list` 查看状态即可，必要时用 `poll` 确认是否仍在运行。

### 并行定时器过多导致进程堆积
同时运行大量定时器会占用系统进程资源，可能导致新定时器启动失败。处理：对已不需要的定时器及时 `kill`；并行数量建议控制在合理范围内（如不超过 10 个），并将长时长的提醒拆分到外部日历。

## FAQ

### 能否设置循环或重复定时器？
不能。timer.js 每次只执行一次倒计时。需要循环时（如番茄工作法），在收到完成通知后由 Agent 再次启动下一个定时器，形成手动循环。

### 定时器在 Agent 重启后是否保留？
不保留。定时器依赖 Agent 的后台进程机制，Agent 会话结束或重启后，后台进程会被清理。需要跨会话的提醒应使用外部日历或系统级定时任务。

### 提醒文案是否支持中文和 emoji？
支持。提醒文案作为字符串参数传入，会在完成通知中原样回传，中文、英文、emoji 与常见标点均可使用。注意文案中的引号需正确转义以避免 shell 解析问题。

### 如何同时查看多个定时器的剩余时间？
调用 `process action:list` 查看所有运行中的后台进程，再对每个 sessionId 调用 `process action:log` 查看最近一条进度记录，其中包含剩余时间。短定时器每秒更新，长定时器每 10 秒更新。

### 定时器最大支持多长时间？
时间格式本身无硬性上限，可设置数小时甚至更长的计时。但过长的计时建议改用系统级 cron 或日历提醒，避免 Agent 会话中断导致后台进程被清理，到期通知丢失。

### 如何取消一个正在运行的定时器？
先执行 `process action:list` 找到目标定时器的 sessionId，再执行 `process action:kill sessionId:XXX` 终止。终止后会收到退出码 130 的完成通知，Agent 应识别为取消而不向用户提示到期。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 定时器仅在当前 Agent 会话的后台进程中存活，会话结束即失效，不适合跨会话或长期提醒
- 不支持循环/重复定时，需要循环时须由 Agent 在每次完成后手动重启
- 不支持指定绝对触发时刻（如 14:00），只支持从当前时刻开始的相对时长
- 声音提示仅在 macOS 上通过 `afplay` 播放，其他系统仅依赖文本通知
- 进度日志对长定时器每 10 秒记录一次，短定时器每秒记录一次，无法获取毫秒级精度
- 并行定时器数量受系统进程资源限制，过多可能导致启动失败
- 提醒文案通过 shell 参数传递，包含引号等特殊字符时需手动转义

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "后台定时器与提醒处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "timer"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
