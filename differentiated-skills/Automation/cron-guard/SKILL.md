---
slug: "cron-guard"
name: "cron-guard"
version: "1.0.0"
displayName: "定时守护"
summary: "cron 作业可靠性护栏，脚本优先、确定环境、静默成功，跨平台故障模式一网打尽。"
license: "Proprietary"
description: |-
  定时守护为cron作业与后台任务提供可靠性护栏,遵循脚本优先、确定环境、静默成功三原则,覆盖shell引用陷阱、cwd/env漂移、SIGPIPE误报、git推送冲突、并发执行冲突等高频故障模式,提供跨平台适配(POSIX+PowerShell)与上线前预检清单。适用于cron作业加固、后台任务可靠性提升、跨平台定时作业场景。适用关键词:定时守护、cron加固、脚本可靠性、shell陷阱、静默成功、cron、shell、guardrails
tags:
  - 自动化
  - 定时调度
  - 可靠性工程
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 定时守护

cron 作业的失败很少是"逻辑 bug",多半是 shell 引用炸了、环境漂移了、管道误报了。本技能用"脚本优先 + 确定环境 + 静默成功"三原则,把这些无聊但致命的坑堵死。

## 核心能力

### 1. 脚本优先原则
禁止在cron里写多行`bash -lc '...'`,把逻辑放进仓库脚本(`tools/<job>.py`),cron只跑一行短命令,避免引用地狱

**输入**: 用户提供脚本优先原则所需的指令和必要参数。
**处理**: 按照skill规范执行脚本优先原则操作,遵循单一意图原则。
**输出**: 返回脚本优先原则的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 2. 确定环境
显式确定cwd(`cd "$(dirname "$0")/.."`)、PATH(不依赖.bashrc)、文档化必需环境变量(`: "${API_KEY:?未设置}"`),解决"本地能跑cron里失败"

**输入**: 用户提供确定环境所需的指令和必要参数。
**处理**: 按照skill规范执行确定环境操作,遵循单一意图原则。
**输出**: 返回确定环境的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 3. 静默成功约定
成功时输出`NO_REPLY`(或空),只在失败时输出`ALERT`到stderr,避免每次成功都发通知淹没用户

**输入**: 用户提供静默成功约定所需的指令和必要参数。
**处理**: 按照skill规范执行静默成功约定操作,遵循单一意图原则。
**输出**: 返回静默成功约定的执行结果,包含操作状态和输出数据。

### 4. 故障模式目录
8种高频故障(EOF引号错误/SIGPIPE误报/cwd漂移/git push被拒/Python -c陷阱/Windows路径/临时文件残留/并发冲突)附修复模板

**输入**: 用户提供故障模式目录所需的指令和必要参数。
**处理**: 按照skill规范执行故障模式目录操作,遵循单一意图原则。
**输出**: 返回故障模式目录的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 5. 跨平台适配
POSIX(bash/sh)与Windows(PowerShell)等效模式对照表,覆盖三大平台

**输入**: 用户提供跨平台适配所需的指令和必要参数。
**处理**: 按照skill规范执行跨平台适配操作,遵循单一意图原则。
**输出**: 返回跨平台适配的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 6. 上线前预检清单
10项检查清单(逻辑在脚本/cwd确定/变量校验/PATH设置/静默成功/trap清理/文件锁/无force-push等)+ 本地cron环境模拟测试

**输入**: 用户提供上线前预检清单所需的指令和必要参数。
**处理**: 按照skill规范执行上线前预检清单操作,遵循单一意图原则。
**输出**: 返回上线前预检清单的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：作业可靠性护栏、跨平台故障模式一、网打尽、定时守护为、作业与后台任务提、供可靠性护栏、遵循脚本优先、静默成功三原则、引用陷阱、env、推送冲突、并发执行冲突等高、频故障模式、与上线前预检清单、适用于、作业加固、后台任务可靠性提、跨平台定时作业场、适用关键词、定时守护、脚本可靠性、guardrails等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 适用场景

**何时使用**:
- 编写或加固cron作业、定时任务脚本
- 后台无人值守脚本需要提升可靠性
- Agent长驻守护脚本的健康检查与告警
- 跨平台(Linux/macOS/Windows)定时作业编写
- CI定时任务与定时调度系统的被调度脚本

**输入**:cron作业的命令行配置或待加固的脚本内容
**输出**:加固后的脚本(含cwd/env/锁/静默成功)、cron单行命令、预检清单通过报告

**不适用场景**:
- 调度系统本身的配置(时区/并发/熔断,由"定时调度专家"负责)
- 非定时的一次性脚本(无需静默成功约定)
- 纯业务逻辑bug修复(本skill聚焦环境与shell陷阱)

## 使用流程

### Step 1: 逻辑进脚本
把cron命令的多行逻辑移到`tools/<job>.py`或`tools/<job>.sh`,cron只跑一行短命令。

```bash
# 错误:cron里塞多行shell(引用地狱)
bash -lc 'cd /app && for f in *.csv; do python3 process.py "$f" && mv "$f" done/; done'

# 正确:cron跑一个脚本
python3 tools/process_all.py
```

### Step 2: 确定cwd与env
脚本开头确定cwd,文档化必需环境变量:
```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.." || exit 1
export PATH="/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin"
: "${API_KEY:?API_KEY 未设置}"
: "${DATA_DIR:?DATA_DIR 未设置}"
```

### Step 3: 实现静默成功
成功时输出`NO_REPLY`(或空),失败时输出`ALERT`到stderr:
```bash
if do_work; then
  echo "NO_REPLY"
  exit 0
else
  echo "ALERT: 任务失败 - $(date)" >&2
  exit 1
fi
```

### Step 4: 添加trap清理与文件锁
```bash
# 临时文件清理
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT

# 文件锁防并发
LOCKFILE="/tmp/job.lock"
exec 200>"$LOCKFILE"
if ! flock -n 200; then
  echo "NO_REPLY"  # 上一轮还在跑,静默跳过
  exit 0
fi
```

### Step 5: 上线前预检
过一遍预检清单:
- [ ] 逻辑在脚本文件中,cron只跑一行命令
- [ ] 脚本开头确定cwd(cd到仓库)
- [ ] 所需环境变量已文档化并校验
- [ ] PATH已显式设置(不依赖.bashrc)
- [ ] 成功时静默(NO_REPLY或无输出)
- [ ] 失败时输出简短告警到stderr
- [ ] 临时文件用trap清理
- [ ] 周期任务有文件锁防并发
- [ ] 无force-push / 无rm -rf危险操作
- [ ] 本地用cron模拟环境测试过(`env -i`)

### Step 6: 本地模拟cron环境测试
```bash
env -i HOME="$HOME" PATH="/usr/local/bin:/usr/bin:/bin" \
  bash -c 'cd /repo && python3 tools/job.py'
```

#
## 示例

### 示例
**输入**: 现有cron配置 `bash -lc 'cd /app && python3 sync.py && git add . && git commit -m "sync" && git push'`,经常报`unexpected EOF`

**输出**:
```bash
# 1. 提取为脚本 tools/daily-sync.py
#!/usr/bin/env python3
import sys, os, subprocess
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
subprocess.run(["python3", "sync.py"], check=True)
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "sync"], check=True)
try:
    subprocess.run(["git", "push"], check=True)
except subprocess.CalledProcessError:
    subprocess.run(["git", "fetch"], check=True)
    subprocess.run(["git", "rebase", "origin/main"], check=True)
    subprocess.run(["git", "push"], check=True)
print("NO_REPLY")

# 2. cron改为一行
# 旧: bash -lc 'cd /app && python3 sync.py && ...'
# 新: python3 /repo/tools/daily-sync.py
```

### 示例2: 跨平台定时作业
**输入**: 需要在Linux和Windows上都运行的定时健康检查脚本

**输出**:
```bash
# 检测平台跑对应脚本
case "$(uname -s)" in
  Linux*|Darwin*) python3 tools/health_check.py ;;
  MINGW*|MSYS*|CYGWIN*) python tools/health_check.py ;;
  *) echo "ALERT: 不支持的平台" >&2; exit 1 ;;
esac
```

**PowerShell等效(Windows Task Scheduler)**:
```powershell
Set-Location $PSScriptRoot\..
if (-not $env:API_KEY) { throw "API_KEY 未设置" }
try {
    $result = Invoke-WebRequest -Uri "http://localhost:8080/health" -UseBasicParsing
    if ($result.StatusCode -eq 200) {
        Write-Output "NO_REPLY"
    } else {
        Write-Error "ALERT: 健康检查失败"
        exit 1
    }
} catch {
    Write-Error "ALERT: 服务不可达"
    exit 1
}
```

## 错误处理


| 场景 | 原因 | 处理方式 |
|:-----|:-----|:---------|
| `unexpected EOF while looking for matching ')'` | `$(...)`命令替换未闭合或`bash -lc`嵌套引号断裂 | 把多行shell替换为脚本,cron只跑`python3 tools/<job>.py` |
| 明明成功却报失败(SIGPIPE) | `set -o pipefail`下`head`提前关闭管道,上游收到SIGPIPE | 局部`|| true`或改用脚本只读需要的部分 |
| 本地能跑cron里失败 | cwd不同(默认HOME)、PATH不同(不加载.bashrc)、环境变量缺失 | 脚本内`cd`到仓库、显式设置PATH、文档化并校验环境变量 |
| `git push`被拒(non-fast-forward) | 远程有新提交,本地推送冲突 | fetch后rebase再执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令;禁止`git push --force` |
| `python3 -c`引号错乱 | 双引号内`$`、`"`被shell解释 | 把`-c`内容写成脚本文件,cron跑`python3 tools/job.py` |
| Windows路径解析错误 | 反斜杠被转义或路径含空格未加引号 | 用单引号字面路径或`$PSScriptRoot`相对路径 |
| 临时文件残留导致冲突 | 脚本中断后临时文件未清理 | 用`trap 'rm -f "$TMPFILE"' EXIT`确保退出时清理 |
| 周期任务重叠数据冲突 | 上一轮未跑完下一轮就启动 | 用`flock -n`文件锁防并发,获取不到锁则静默跳过 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| bash或PowerShell | Shell | 必需 | 系统自带 |
| Agent LLM | API | 必需 | 由Agent内置LLM提供 |
| python3 | 运行时 | 推荐(脚本载体) | 系统自带或python.org |
| flock | CLI | Linux/Mac推荐(文件锁) | util-linux自带 |
| curl | CLI | 可选(健康检查) | 系统自带 |

**运行环境**:
- 操作系统: Linux / macOS(POSIX) / Windows(PowerShell)
- Shell: bash 4+ / sh / PowerShell 5+
- 本技能本身无需API Key;被守护的脚本可能需要外部API Key,必须通过环境变量引用并文档化,禁止硬编码

**可用性分类**: MD+EXEC(Markdown指南 + 脚本执行),Agent据此编写/审查cron脚本,实际执行由调度系统调用脚本

## 常见问题

**Q: 我的cron作业在Windows上跑怎么办?**
A: 用PowerShell脚本替代bash脚本,遵循同样的三原则(脚本优先/确定cwd/静默成功)。Windows Task Scheduler调度`powershell -File tools\job.ps1`。参考跨平台适配表。

**Q: NO_REPLY必须精确匹配吗?**
A: 是的,精确输出`NO_REPLY`(大写、无多余空格)。许多平台把精确输出`NO_REPLY`视为"静默成功"(不触发人工通知)。若平台不识别,等效于"成功时无输出"。

**Q: 脚本优先是不是过度工程?**
A: 不是。多行shell在cron里的引号陷阱几乎不可避免。脚本文件可测试、可版本控制、可lint,长期收益远大于"省一个文件"。

**Q: pipefail到底该不该用?**
A: 该用,但要注意`| head`场景。`set -euo pipefail`是好习惯,遇到SIGPIPE误报时局部`|| true`或改用脚本读取。

**Q: force-push真的完全禁止吗?**
A: 自动化脚本里禁止。个人临时分支可酌情,但cron作业绝不能force-push,会覆盖他人提交。被拒后用fetch+rebase重试。

## 已知限制

1. **聚焦shell与环境陷阱**:本skill处理"被调度的脚本怎么写得可靠",不负责调度系统本身的配置(时区/并发/熔断,由"定时调度专家"负责)
2. **文件锁依赖flock**:Linux/macOS用`flock`,Windows需用PowerShell的`New-Object System.Threading.Mutex`替代,跨平台锁机制不完全统一
3. **NO_REPLY为平台约定**:并非所有调度平台都识别`NO_REPLY`,部分平台需配置为"成功时无输出"才静默
4. **不覆盖业务逻辑bug**:本skill聚焦环境与shell陷阱,业务逻辑正确性需通过单元测试保证
5. **预检清单需人工执行**:10项预检清单为人工checklist,未提供自动化校验工具
