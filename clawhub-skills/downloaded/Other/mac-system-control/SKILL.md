---
slug: mac-system-control
name: mac-system-control
version: "1.0.0"
displayName: mac-system-control
summary: 管理和控制 macOS 系统功能。包括查看系统信息、管理进程、控制音量/亮度、 网络管理、电源管理、截图、剪贴板、Finder 操作等。当用户要求查看系统状态、
  控制系统设置、管理进程、截图、调...
license: MIT-0
description: |-
  管理和控制 macOS 系统功能。包括查看系统信息、管理进程、控制音量/亮度、 网络管理、电源管理、截图、剪贴板、Finder 操作等。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。
tags:
- Other
tools:
  - - read
- exec
---

# mac-system-control

## 系统信息

```bash
system_profiler SPSoftwareDataType SPHardwareDataType

top -l 1 -n 0 | head -10

vm_stat | head -6

df -h /

pmset -g batt

sw_vers
```

## 进程管理

```bash
ps aux --sort=-%cpu | head -11

ps aux --sort=-%mem | head -11

pgrep -fl "<关键词>"

kill <PID>
killall "<进程名>"
```

操作前务必向用户确认目标进程，避免误杀。

## 音量与亮度

```bash
osascript -e 'output volume of (get volume settings)'

osascript -e 'set volume output volume <0-100>'

osascript -e 'set volume output muted true'
osascript -e 'set volume output muted false'

brightness <0.0-1.0>
```

## 网络

```bash
networksetup -getairportnetwork en0

ipconfig getifaddr en0

curl -s ifconfig.me

networksetup -getdnsservers Wi-Fi

ping -c 3 <host>

/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -s

networksetup -setairportpower en0 off
networksetup -setairportpower en0 on
```

## 电源管理

```bash
pmset sleepnow

sudo shutdown -h now

sudo shutdown -r now

pmset displaysleepnow

caffeinate -d -t <秒数>
```

关机和重启操作必须先向用户确认。

## 截图

```bash
screencapture ~/Desktop/screenshot.png

screencapture -i ~/Desktop/screenshot.png

screencapture -w ~/Desktop/screenshot.png

screencapture -c
```

## 剪贴板

```bash
pbpaste

echo "内容" | pbcopy

pbcopy < /path/to/file
```

## Finder 操作

```bash
open /path/to/directory

open -R /path/to/file

osascript -e 'tell application "Finder" to empty trash'

defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder
defaults write com.apple.finder AppleShowAllFiles -bool false && killall Finder
```

## 系统设置快捷方式

```bash
open "x-apple.systempreferences:"

open "x-apple.systempreferences:com.apple.Network-Settings.extension"
open "x-apple.systempreferences:com.apple.Sound-Settings.extension"
open "x-apple.systempreferences:com.apple.Bluetooth-Settings.extension"
open "x-apple.systempreferences:com.apple.Display-Settings.extension"
```

## 工作流

1. 用户描述要执行的系统操作
2. 判断属于哪个类别（信息查询 / 设置调整 / 进程管理等）
3. 信息查询类直接执行并展示结果
4. 破坏性操作（关机、重启、杀进程、清空废纸篓）先向用户确认
5. 需要 `sudo` 的命令提前告知用户

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

- 管理和控制 macOS 系统功能
- 包括查看系统信息、管理进程、控制音量/亮度、 网络管理、电源管理、截图、剪贴板、Finder 操作等
- 当用户要求查看系统状态、
  控制系统设置、管理进程、截图、调
- 触发关键词: 系统功能, system, 包括查看系统, 管理进程, finder, 管理和控制, 信息, mac

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

### Q1: 如何开始使用mac-system-control？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: mac-system-control有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
