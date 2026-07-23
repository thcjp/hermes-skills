---
slug: "vscode-node-paid"
name: "vscode-node-paid"
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
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec", "glob", "grep"]
tags: "开发工具,代码生成,编程辅助"
---
# VSCode节点工具(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

| 能力 | 说明 | 是否兼容免费版 |
|:-----|:-----|:-----|
| 基础 IDE 操作 | 免费版全部文件、语言、编辑器、Git 命令 | 完全兼容 |
| 调试 | 启动、停止、断点、求值、堆栈、变量 | Pro 新增 |
| 测试 | 列举、运行、结果获取 | Pro 新增 |
| 终端执行 | 白名单命令运行 | Pro 新增 |
| Agent 委托 | 复杂任务委托给 Cursor Agent | Pro 新增 |
| 工作区管理 | 工作区信息查询与多工作区切换 | Pro 新增 |
| 多节点协作 | 团队多节点并行任务调度 | Pro 新增 |
| 安全策略 | 命令白名单、路径限制、审计日志 | Pro 新增 |
### 基础 IDE 操作

针对基础 IDE ,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供基础 IDE 操作相关的配置参数、输入数据和处理选项。

**输出**: 返回基础 IDE 操作的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`基础 IDE 操作`的配置文档进行参数调优
### 终端执行

针对终端,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供终端执行相关的配置参数、输入数据和处理选项。

**输出**: 返回终端执行的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`终端执行`的配置文档进行参数调优
### Agent 委托

针对Agent 委托,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供Agent 委托相关的配置参数、输入数据和处理选项。

**输出**: 返回Agent 委托的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Agent 委托`的配置文档进行参数调优
#
## 适用场景

### 场景 1:自动化调试会话

通过 Agent 启动调试会话,设置断点,获取变量值与堆栈。

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

在 CI 或本地通过 Agent 运行测试套件并获取结果。

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

将复杂的多文件重构任务委托给 Cursor Agent 执行。

```bash
nodes invoke --node "team-vscode" \
  --invokeCommand "vscode.agent.run" \
  --invokeParamsJson '{
    "prompt": "为所有 API 端点添加错误处理,确保返回统一的错误响应格式,并补充对应的单元测试",
    "mode": "plan"
  }' \
  --invokeTimeoutMs 300000 --timeoutMs 305000
```

返回:`{ output, exitCode }`,包含执行日志与结果。

## 使用流程

### 优秀步:声明团队上下文

在对话中说明团队规模、节点配置与协作需求,例如:

```
我们是 10 人的后端团队,有 5 个 VSCode 节点连接到团队网关。
需要自动化调试与测试能力,并把复杂重构任务委托给 Cursor Agent。
```

### 第二步:获取工程方案

工具会输出多节点配置、调试脚本、测试自动化方案与安全策略建议。

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
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | vscode-node处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **IDE**:VSCode 或 Cursor(需安装节点协议扩展)
- **网关服务**:团队或企业部署的节点网关

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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

## 案例展示

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
|---:|:---|---:|---:|
| 文件/编辑器/语言 | 15000 | 20000 | 快速操作 |
| Git | 30000 | 35000 | 中等耗时 |
| 测试 | 60000 | 65000 | 测试套件 |
| 调试 | 60000 | 65000 | 调试会话 |
| Agent plan/ask | 180000 | 185000 | 规划任务 |
| Agent run | 300000 | 305000 | 完整执行 |

### 命令分类完整速查

| 分类 | 前缀 | 关键命令 | 是否兼容免费版 |
|:------:|--------|:-------|:------:|
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

## 常见问题

### Q1: 多节点如何并行执行任务?

将任务分片,通过脚本循环调用不同节点的 `nodes invoke`。例如测试套件按文件分片,每个节点执行一部分,最后汇总结果。

### Q2: Agent 委托的任务如何审查?

先用 `mode: "plan"` 让 Agent 输出计划,人工审查计划合理后再用 `mode: "run"` 执行。所有 Agent 输出记录到审计日志。

### Q3: 调试会话如何断点条件化?

`vscode.debug.breakpoint` 支持 `condition` 字段,设置条件表达式(如 `userId === null`),仅在条件满足时暂停。

### Q4: 终端命令如何安全启用?

在网关配置的 `terminal.allowedCommands` 中预定义允许的命令(如 `npm test`、`git status`),未列出的命令会被拒绝。

### Q5: Pro 版与免费版如何协同?

Pro 版完全兼容免费版的所有命令与调用模式。个人开发者可继续使用免费版,团队场景启用 Pro 版获得调试、测试、Agent 委托与多节点能力。两个版本可连接同一网关,无冲突。

### Q6: 如何度量团队协作效率?

跟踪四个指标:节点平均利用率、命令调用成功率、Agent 委托任务完成率、测试自动化覆盖率。四者共同反映团队协作效率。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

