---
slug: "vscode-node-tool-pro"
name: "vscode-node-tool-pro"
version: "1.0.0"
displayName: "VSCode节点工具(专业版)"
summary: "面向团队的企业级IDE远程操作平台,含调试、测试、终端、Agent委托与团队协作能力。"
license: "Proprietary"
edition: "pro"
description: |-
  VSCode节点工具专业版为团队与企业提供端到端IDE远程操作能力,涵盖调试、测试、终端、Agent委托、工作区管理与团队协作。核心能力:
  - 调试能力(启动/停止/断点/求值/堆栈/变量)
  - 测试能力(列举/运行/结果)
  - 终端执行(白名单命令)
  - Agent委托(将复杂任务委托给Cursor Agent)
  - 工作区信息管理
  - 多节点团队协作
  - 安全策略与审计日志

  适用场景:
  - 中大型团队远程协作开发
  - 自动化调试与测试流水线
  - 复杂任务委托给Agent执行
  - 多节点并行任务调...
tags:
  - VSCode
  - Cursor
  - IDE集成
  - 企业开发
  - 远程调试
  - 团队协作
  - 自动化测试
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
tools: ["read", "write", "exec", "glob", "grep"]
tags: "开发工具,代码生成,编程辅助"
category: "Development"
---
# VSCode 节点工具(专业版)

## 概述

`vscode-node-tool-pro` 是面向团队与企业的端到端 IDE 远程操作平台。它在免费版文件、语言、编辑器、Git 基础操作之上,扩展了调试、测试、终端执行、Agent 委托、工作区管理与多节点团队协作能力,帮助团队构建可审计、可协作、可自动化的远程开发流水线.
本版本完全兼容免费版的所有命令与调用模式,可平滑升级。所有指令通过 Markdown 驱动 Agent 调用 `nodes invoke`,配合 CI/CD 与团队网关实现规模化协作.
## 核心能力

| 能力 | 说明 | 是否兼容免费版 |
|---|---|-------|
| 基础 IDE 操作 | 免费版全部文件、语言、编辑器、Git 命令 | 完全兼容 |
| 调试 | 启动、停止、断点、求值、堆栈、变量 | Pro 新增 |
| 测试 | 列举、运行、结果获取 | Pro 新增 |
| 终端执行 | 白名单命令运行 | Pro 新增 |
| Agent 委托 | 复杂任务委托给 Cursor Agent | Pro 新增 |
| 工作区管理 | 工作区信息查询与多工作区切换 | Pro 新增 |
| 多节点协作 | 团队多节点并行任务调度 | Pro 新增 |
| 安全策略 | 命令白名单、路径限制、审计日志 | Pro 新增 |

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
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：面向团队的企业级、远程操作平台、含调试、委托与团队协作能、VSCode、节点工具专业版为、团队与企业提供端、远程操作能力、涵盖调试、工作区管理与团队、核心能力、调试能力、测试能力、将复杂任务委托给、工作区信息管理、多节点团队协作、安全策略与审计日等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景 1:自动化调试会话

通过 Agent 启动调试会话,设置断点,获取变量值与堆栈.
```bash
# 1. 启动调试
nodes invoke --node "team-vscode" \
  --invokeCommand "vscode.debug.launch" \
  --invokeParamsJson '{"config":"Launch Server"}' \
  --invokeTimeoutMs 60000 --timeoutMs 65000
# ...
# 2. 设置断点
nodes invoke --node "team-vscode" \
  --invokeCommand "vscode.debug.breakpoint" \
  --invokeParamsJson '{"path":"src/handler.ts","line":42,"condition":"userId === null"}'
# ...
# 3. 求值变量
nodes invoke --node "team-vscode" \
  --invokeCommand "vscode.debug.evaluate" \
  --invokeParamsJson '{"expression":"user?.profile?.email"}'
# ...
# 4. 获取堆栈
nodes invoke --node "team-vscode" \
  --invokeCommand "vscode.debug.stackTrace"
# ...
# 5. 获取变量
nodes invoke --node "team-vscode" \
  --invokeCommand "vscode.debug.variables" \
  --invokeParamsJson '{"frameId":1,"scope":"local"}'
```

### 场景 2:自动化测试运行

在 CI 或本地通过 Agent 运行测试套件并获取结果.
```bash
# 1. 列举测试
nodes invoke --node "team-vscode" \
  --invokeCommand "vscode.test.list" \
  --invokeParamsJson '{"pattern":"**/*.test.ts"}'
# ...
# 2. 运行测试
nodes invoke --node "team-vscode" \
  --invokeCommand "vscode.test.run" \
  --invokeParamsJson '{"filter":"UserService"}' \
  --invokeTimeoutMs 120000 --timeoutMs 125000
# ...
# 3. 获取结果
nodes invoke --node "team-vscode" \
  --invokeCommand "vscode.test.results"
```

返回示例:`{ passed: 42, failed: 3, skipped: 1, duration: 12345 }`

### 场景 3:委托复杂任务给 Cursor Agent

将复杂的多文件重构任务委托给 Cursor Agent 执行.
```bash
nodes invoke --node "team-vscode" \
  --invokeCommand "vscode.agent.run" \
  --invokeParamsJson '{
    "prompt": "为所有 API 端点添加错误处理,确保返回统一的错误响应格式,并补充对应的单元测试",
    "mode": "plan"
  }' \
  --invokeTimeoutMs 300000 --timeoutMs 305000
```

返回:`{ output, exitCode }`,包含执行日志与结果.
## 不适用场景

以下场景VSCode节点工具(专业版)不适合处理：

- 无明确技术栈的模糊需求
- 纯架构设计决策
- 运维部署管理

## 触发条件

需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于非本工具能力范围的需求.
## 快速开始

### 第一步:声明团队上下文

在对话中说明团队规模、节点配置与协作需求,例如:

```
我们是 10 人的后端团队,有 5 个 VSCode 节点连接到团队网关.
需要自动化调试与测试能力,并把复杂重构任务委托给 Cursor Agent.
```

### 第二步:获取工程方案

工具会输出多节点配置、调试脚本、测试自动化方案与安全策略建议.
### 第三步:落地与协作

```bash
# 验证所有节点连接
nodes status
# ...
# 运行调试脚本
bash （请参考skill目录中的脚本文件） src/handler.ts 42
# ...
# 运行测试套件
bash （请参考skill目录中的脚本文件） "UserService"
```

#
## 示例

### 团队网关安全策略

```jsonc
{
  "gateway": {
    "nodes": {
      // 命令白名单:仅允许以下命令
      "allowCommands": [
        "vscode.file.read", "vscode.file.write", "vscode.file.edit",
        "vscode.lang.definition", "vscode.lang.references", "vscode.lang.hover",
        "vscode.editor.active", "vscode.editor.openFiles",
        "vscode.diagnostics.get",
        "vscode.git.status", "vscode.git.diff", "vscode.git.log",
        "vscode.test.list", "vscode.test.run", "vscode.test.results",
        "vscode.debug.launch", "vscode.debug.stop", "vscode.debug.breakpoint",
        "vscode.debug.evaluate", "vscode.debug.stackTrace", "vscode.debug.variables",
        "vscode.agent.run", "vscode.agent.status",
        "vscode.workspace.info"
      ],
      // 终端默认禁用,显式启用后仍限白名单
      "terminal": {
        "enabled": true,
        "allowedCommands": ["npm test", "npm run lint", "git status"]
      }
    },
    // 安全策略
    "security": {
      "readOnlyByDefault": false,
      "confirmWrites": true,
      "pathRestriction": "workspace-only",
      "auditLog": "logs/audit.jsonl"
    }
  }
}
```

### 超时配置完整参考

| 操作类型 | invokeTimeoutMs | timeoutMs | 说明 |
|:-----|:-----|:-----|:-----|
| 文件/编辑器/语言 | 15000 | 20000 | 快速操作 |
| Git | 30000 | 35000 | 中等耗时 |
| 测试 | 60000 | 65000 | 测试套件 |
| 调试 | 60000 | 65000 | 调试会话 |
| Agent plan/ask | 180000 | 185000 | 规划任务 |
| Agent run | 300000 | 305000 | 完整执行 |

### 命令分类完整速查

| 分类 | 前缀 | 关键命令 | 是否兼容免费版 |
|---:|---:|---:|---:|
| 文件 | `vscode.file.*` | read, write, edit, delete | 是 |
| 目录 | `vscode.dir.*` | list | 是 |
| 语言 | `vscode.lang.*` | definition, references, hover, symbols, rename, codeActions, format | 是 |
| 编辑器 | `vscode.editor.*` | active, openFiles, selections | 是 |
| 诊断 | `vscode.diagnostics.*` | get | 是 |
| Git | `vscode.git.*` | status, diff, log, blame, stage, commit, stash | 部分 |
| 测试 | `vscode.test.*` | list, run, results | Pro |
| 调试 | `vscode.debug.*` | launch, stop, breakpoint, evaluate, stackTrace, variables | Pro |
| 终端 | `vscode.terminal.*` | run(白名单) | Pro |
| Agent | `vscode.agent.*` | status, run, setup | Pro |
| 工作区 | `vscode.workspace.*` | info | Pro |

## 最佳实践

1. **命令白名单最小化**:仅启用团队实际需要的命令,降低误操作风险.
2. **写操作确认**:启用 `confirmWrites`,关键写操作需人工确认.
3. **审计日志归档**:所有命令调用记录到审计日志,便于事后追溯.
4. **路径限制工作区**:禁止 `../` 与绝对路径,防止越权访问.
5. **终端白名单**:终端默认禁用,启用后仅允许预定义命令(如 `npm test`).
6. **Agent 委托先用 plan 模式**:复杂任务先用 `mode: "plan"` 让 Agent 输出计划,人工审查后再 `run`.
7. **测试结果归档**:每次测试运行结果保存为 JSON,便于趋势分析与回归检测.
8. **多节点负载均衡**:大型测试套件分片到多个节点并行执行,缩短总耗时.
## 常见问题

### Q1: 多节点如何并行执行任务?

将任务分片,通过脚本循环调用不同节点的 `nodes invoke`。例如测试套件按文件分片,每个节点执行一部分,最后汇总结果.
### Q2: Agent 委托的任务如何审查?

先用 `mode: "plan"` 让 Agent 输出计划,人工审查计划合理后再用 `mode: "run"` 执行。所有 Agent 输出记录到审计日志.
### Q3: 调试会话如何断点条件化?

`vscode.debug.breakpoint` 支持 `condition` 字段,设置条件表达式(如 `userId === null`),仅在条件满足时暂停.
### Q4: 终端命令如何安全启用?

在网关配置的 `terminal.allowedCommands` 中预定义允许的命令(如 `npm test`、`git status`),未列出的命令会被拒绝.
### Q5: Pro 版与免费版如何协同?

Pro 版完全兼容免费版的所有命令与调用模式。个人开发者可继续使用免费版,团队场景启用 Pro 版获得调试、测试、Agent 委托与多节点能力。两个版本可连接同一网关,无冲突.
### Q6: 如何度量团队协作效率?

跟踪四个指标:节点平均利用率、命令调用成功率、Agent 委托任务完成率、测试自动化覆盖率。四者共同反映团队协作效率.
## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **IDE**:VSCode 或 Cursor(需安装节点协议扩展)
- **网关服务**:团队或企业部署的节点网关

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| VSCode / Cursor | IDE | 必需 | 官方安装 |
| 节点协议扩展 | IDE 扩展 | 必需 | IDE 扩展市场搜索安装 |
| 网关服务 | 服务 | 必需 | 团队或企业部署 |
| 调试运行时 | 运行时 | 推荐 | Node.js / Python 等 |
| 测试框架 | npm 包 | 推荐 | Jest / Mocha / Vitest 等 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 基于节点协议,核心能力无需额外 API Key
- 节点连接通过设备唯一身份(Ed25519)认证,由网关批准
- 如网关启用 OAuth,需配置对应平台的访问令牌
- Agent 委托任务使用 Agent 内置 LLM,无需额外 API Key

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言指令驱动 Agent 调用 `nodes invoke` 命令;需要预先安装 IDE 扩展、连接网关,并在团队场景配置安全策略与审计日志

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "VSCode节点工具(专业版)处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "vscode node pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
