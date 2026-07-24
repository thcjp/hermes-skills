---
slug: cron-guard
name: cron-guard
version: 1.0.1
displayName: 定时守护
summary: "cron 作业可靠性护栏，脚本优先、确定环境、静默成功，跨平台故障模式一网打尽. 定时守护为cron作业与后台任务提供可靠性护栏,遵循脚本优先、确定环境、静默成功三原则,覆盖shell引用陷"
license: Proprietary
description: 定时守护为cron作业与后台任务提供可靠性护栏,遵循脚本优先、确定环境、静默成功三原则,覆盖shell引用陷阱、cwd/env漂移、SIGPIPE误报、git推送冲突、并发执行冲突等高频故障模式,提供跨平台适配(POSIX+PowerShell)与上线前预检清单。适用于cron作业加固、后台任务可靠性提升、跨平台定时作业场景。适用关键词:定时守护、cron加固、脚本可靠性、shell陷阱、静默成功、cron、shell、guardrails
tags:
  - 自动化
  - 定时调度
  - 可靠性工程
  - 工作流
  - 效率
  - cron
  - no_reply
  - powershell
  - 静默成功
  - bash
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# 定时守护

cron 作业的失败很少是"逻辑 bug",多半是 shell 引用炸了、环境漂移了、管道误报了。本技能用"脚本优先 + 确定环境 + 静默成功"三原则,把这些无聊但致命的坑堵死.

## 核心能力

### 1. 脚本优先原则
禁止在cron里写多行`bash -lc '..'`,把逻辑放进仓库脚本(`tools/<job>.py`),cron只跑一行短命令,避免引用地狱。使用`input_params`参数支持创建/查询/导出操作。

### 2. 确定环境
显式确定cwd(`cd "$(dirname "$0")/."`)、PATH(不依赖.bashrc)、文档化必需环境变量(`: "${API_KEY:?未设置}"`),解决"本地能跑cron里失败"。使用`input_params`参数支持创建/查询/导出操作。

### 3. 静默成功约定
成功时输出`NO_REPLY`(或空),只在失败时输出`ALERT`到stderr,避免每次成功都发通知淹没用户。

### 4. 故障模式目录
8种高频故障(EOF引号错误/SIGPIPE误报/cwd漂移/git push被拒/Python -c陷阱/Windows路径/临时文件残留/并发冲突)附修复模板。使用`input_params`参数支持创建/查询/导出操作。

### 5. 跨平台适配
POSIX(bash/sh)与Windows(PowerShell)等效模式对照表,覆盖三大平台。使用`input_params`参数支持创建/查询/导出操作。

### 6. 上线前预检清单
10项检查清单(逻辑在脚本/cwd确定/变量校验/PATH设置/静默成功/trap清理/文件锁/无force-push等)+ 本地cron环境模拟测试。使用`input_params`参数支持创建/查询/导出操作。

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

**何时使用**: 编写或加固cron作业、定时任务脚本;后台无人值守脚本需提升可靠性;Agent长驻守护脚本的健康检查与告警;跨平台定时作业编写;CI定时任务与调度系统的被调度脚本

**不适用场景**: 调度系统本身的配置(时区/并发/熔断,由"定时调度专家"负责);非定时一次性脚本;纯业务逻辑bug修复(本skill聚焦环境与shell陷阱)

## 关键参数说明

| 方法/模式 | 关键参数 | 说明 |
|---|---|---|
| 脚本提取 | `tools/<job>.py`或`tools/<job>.sh` | cron多行逻辑移入脚本,cron只跑`python3 tools/<job>.py` |
| 确定cwd/env | `cd "$(dirname "$0")/."`, `: "${VAR:?未设置}"` | 脚本开头确定cwd、显式设置PATH、校验环境变量 |
| 静默成功 | `echo "NO_REPLY"`(成功), `echo "ALERT" >&2`(失败) | 精确输出`NO_REPLY`,失败时告警到stderr |
| trap清理 | `trap 'rm -f "$TMPFILE"' EXIT` | 退出时清理临时文件 |
| 文件锁 | `flock -n 200`或PowerShell Mutex | 防止周期任务并发执行 |
| 本地模拟 | `env -i HOME="$HOME" PATH="..." bash -c '...'` | 模拟cron最小环境测试 |

**典型流程**: 逻辑进脚本→确定cwd/env→实现静默成功→添加trap清理与文件锁→上线前预检→本地模拟cron环境测试。跨平台用`uname -s`检测平台跑对应脚本,Windows用PowerShell等效模式。

## 输入格式

```json
{
  "input": "定时任务脚本路径或命令",
  "options": {
    "mode": "create|query|export",
    "silent_success": true,
    "lock_file": "/tmp/cron-guard.lock"
  }
}
```

## 输出格式

```json
{
  "success": true,
  "result": "NO_REPLY",
  "metadata": {
    "exit_code": 0,
    "duration_ms": 150,
    "locked": true
  }
}
```

## 错误处理

| 场景 | 原因 | 处理方式 |
|:-----|:-----|:-----|
| `unexpected EOF` | `$(..)`未闭合或`bash -lc`嵌套引号断裂 | 把多行shell替换为脚本,cron只跑`python3 tools/<job>.py` |
| 本地能跑cron里失败 | cwd不同、PATH不同、环境变量缺失 | 脚本内`cd`到仓库、显式设置PATH、文档化并校验环境变量 |
| `git push`被拒(non-fast-forward) | 远程有新提交,本地推送冲突 | fetch后rebase再推送;禁止`git push --force` |
| 临时文件残留导致冲突 | 脚本中断后临时文件未清理 | 用`trap 'rm -f "$TMPFILE"' EXIT`确保退出时清理 |
| 周期任务重叠数据冲突 | 上一轮未跑完下一轮就启动 | 用`flock -n`文件锁防并发,获取不到锁则静默跳过 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| bash或PowerShell | Shell | 必需 | 系统自带 |
| Agent LLM | API | 必需 | 由Agent内置LLM提供 |
| python3 | 运行时 | 推荐(脚本载体) | 系统自带或python.org |
| flock | CLI | Linux/Mac推荐(文件锁) | util-linux自带 |
| curl | CLI | 可选(健康检查) | 系统自带 |

**运行环境**: Linux/macOS(POSIX)/Windows(PowerShell),bash 4+/sh/PowerShell 5+。本技能无需API Key;被守护脚本可能需外部API Key,必须通过环境变量引用并文档化,禁止硬编码。

**可用性分类**: MD+EXEC(Markdown指南 + 脚本执行),Agent据此编写/审查cron脚本,实际执行由调度系统调用脚本

## 示例代码

### POSIX cron 脚本模板

```bash
#!/usr/bin/env bash
set -euo pipefail

# 确定环境
cd "$(dirname "$0")/."
: "${API_KEY:?未设置API_KEY环境变量}"
export PATH="/usr/local/bin:/usr/bin:/bin"

# 文件锁防并发
exec 200>/tmp/cron-guard.lock
flock -n 200 || { echo "ALERT: 另一个实例正在运行" >&2; exit 0; }

# 静默成功约定
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT

# 主逻辑
if python3 tools/job.py --input "$1" 2>"$TMPFILE"; then
    echo "NO_REPLY"
else
    echo "ALERT: 任务失败" >&2
    cat "$TMPFILE" >&2
    exit 1
fi
```

### Windows PowerShell 等效模板

```powershell
# cron-guard PowerShell 模式
$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

# 环境变量校验
if (-not $env:API_KEY) {
    Write-Error "未设置API_KEY环境变量"
    exit 1
}

# Mutex 防并发
$mutex = New-Object System.Threading.Mutex($false, "Global\cron-guard")
if (-not $mutex.WaitOne(0, $false)) {
    Write-Output "NO_REPLY"
    exit 0
}

# 静默成功
try {
    python3 tools/job.py --input $args[0]
    Write-Output "NO_REPLY"
} catch {
    Write-Error "ALERT: 任务失败 - $_"
    exit 1
} finally {
    $mutex.ReleaseMutex()
}
```

### crontab 配置示例

```cron
# 每5分钟执行,静默成功,失败时告警
*/5 * * * * cd /opt/app && ./tools/cron-guard.sh >> /var/log/cron-guard.log 2>&1

# 每日凌晨备份,使用文件锁防重叠
0 2 * * * cd /opt/app && flock -n /tmp/backup.lock python3 tools/backup.py
```

## 常见问题

**Q: NO_REPLY必须精确匹配吗?**
A: 是的,精确输出`NO_REPLY`(大写、无多余空格)。许多平台视为"静默成功"(不触发人工通知)。若平台不识别,等效于"成功时无输出"。

**Q: pipefail到底该不该用?**
A: 该用,但要注意`| head`场景。`set -euo pipefail`是好习惯,遇到SIGPIPE误报时局部`|| true`或改用脚本读取。

**Q: force-push真的完全禁止吗?**
A: 自动化脚本里禁止。cron作业绝不能force-push,会覆盖他人提交。被拒后用fetch+rebase重试。

## 已知限制

1. **聚焦shell与环境陷阱**:本skill处理"被调度的脚本怎么写得可靠",不负责调度系统本身的配置(时区/并发/熔断,由"定时调度专家"负责)
2. **文件锁依赖flock**:Linux/macOS用`flock`,Windows需用PowerShell的`New-Object System.Threading.Mutex`替代,跨平台锁机制不完全统一
3. **NO_REPLY为平台约定**:并非所有调度平台都识别`NO_REPLY`,部分平台需配置为"成功时无输出"才静默
4. **不覆盖业务逻辑bug**:本skill聚焦环境与shell陷阱,业务逻辑正确性需通过单元测试保证
5. **预检清单需人工执行**:10项预检清单为人工checklist,未提供自动化校验工具
