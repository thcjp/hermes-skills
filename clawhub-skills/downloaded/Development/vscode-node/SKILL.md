---
slug: vscode-node
name: vscode-node
version: "1.0.2"
displayName: VS Code Node
summary: Operate on code through a VS Code/Cursor IDE connected as an OpenClaw Node.
  Provides 40+ commands...
license: MIT
description: |-
  Operate on code through a VS Code/Cursor IDE connected as an OpenClaw
  Node。Provides 40+ commands。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# VS Code Node

Control a VS Code or Cursor IDE remotely through the Skill平台 Node protocol.

## Related

* **[Skill平台 Node for VS Code](https://marketplace.visualstudio.com/items?itemName=xiaoyaner.skill-platform-node-vscode)** — The VS Code/Cursor extension you need to install (required)
* **[cursor-ide-agent](https://SkillHub.ai/xiaoyaner0201/cursor-ide-agent)** — Combined skill with both CLI and Node paths (install this instead if you also use Cursor CLI)
* **Source**: [github.com/xiaoyaner-home/skill-platform-vscode](https://github.com/xiaoyaner-home/skill-platform-vscode)

## Prerequisites

* Extension `skill-platform-node-vscode` installed and connected (status bar 🟢)
* Node visible in `nodes status`
* Commands in Gateway's `allowCommands` whitelist

## Invocation Pattern

```text
nodes invoke --node "<name>" --invokeCommand "<cmd>" --invokeParamsJson '{"key":"val"}'
```

Both `invokeTimeoutMs` (Gateway internal) and `timeoutMs` (HTTP layer, must be larger) are required for long operations.

**Timeout guide:**

| Type | invokeTimeoutMs | timeoutMs |
| --- | --- | --- |
| File/editor/lang | 15000 | 20000 |
| Git | 30000 | 35000 |
| Test | 60000 | 65000 |
| Agent plan/ask | 180000 | 185000 |
| Agent run | 300000 | 305000 |

## Command Categories

| Category | Prefix | Key Commands | Reference |
| --- | --- | --- | --- |
| **File** | `vscode.file.*` | read, write, edit, delete | [commands/file.md](/api/v1/skills/vscode-node/file?path=references%2Fcommands%2Ffile.md&ownerHandle=xiaoyaner0201) |
| **Directory** | `vscode.dir.*` | list | [commands/file.md](/api/v1/skills/vscode-node/file?path=references%2Fcommands%2Ffile.md&ownerHandle=xiaoyaner0201) |
| **Language** | `vscode.lang.*` | definition, references, hover, symbols, rename, codeActions, format | [commands/language.md](/api/v1/skills/vscode-node/file?path=references%2Fcommands%2Flanguage.md&ownerHandle=xiaoyaner0201) |
| **Editor** | `vscode.editor.*` | active, openFiles, selections | [commands/editor.md](/api/v1/skills/vscode-node/file?path=references%2Fcommands%2Feditor.md&ownerHandle=xiaoyaner0201) |
| **Diagnostics** | `vscode.diagnostics.*` | get | [commands/editor.md](/api/v1/skills/vscode-node/file?path=references%2Fcommands%2Feditor.md&ownerHandle=xiaoyaner0201) |
| **Git** | `vscode.git.*` | status, diff, log, blame, stage, commit, stash | [commands/git.md](/api/v1/skills/vscode-node/file?path=references%2Fcommands%2Fgit.md&ownerHandle=xiaoyaner0201) |
| **Test** | `vscode.test.*` | list, run, results | [commands/test-debug.md](/api/v1/skills/vscode-node/file?path=references%2Fcommands%2Ftest-debug.md&ownerHandle=xiaoyaner0201) |
| **Debug** | `vscode.debug.*` | launch, stop, breakpoint, evaluate, stackTrace, variables | [commands/test-debug.md](/api/v1/skills/vscode-node/file?path=references%2Fcommands%2Ftest-debug.md&ownerHandle=xiaoyaner0201) |
| **Terminal** | `vscode.terminal.*` | run (disabled by default) | [commands/terminal.md](/api/v1/skills/vscode-node/file?path=references%2Fcommands%2Fterminal.md&ownerHandle=xiaoyaner0201) |
| **Agent** | `vscode.agent.*` | status, run, setup (Cursor only) | [commands/agent.md](/api/v1/skills/vscode-node/file?path=references%2Fcommands%2Fagent.md&ownerHandle=xiaoyaner0201) |
| **Workspace** | `vscode.workspace.*` | info | [commands/editor.md](/api/v1/skills/vscode-node/file?path=references%2Fcommands%2Feditor.md&ownerHandle=xiaoyaner0201) |

## 示例

### Read a file

```text
nodes invoke --node "my-vscode" --invokeCommand "vscode.file.read" --invokeParamsJson '{"path":"src/main.ts"}'
→ { content, totalLines, language }
```

### Find all references

```text
nodes invoke --node "my-vscode" --invokeCommand "vscode.lang.references" --invokeParamsJson '{"path":"src/main.ts","line":10,"character":5}'
→ { locations: [{ path, line, character }] }
```

### Git status + commit

```text
nodes invoke --node "my-vscode" --invokeCommand "vscode.git.status"
→ { branch, staged, modified, untracked, ahead, behind }

nodes invoke --node "my-vscode" --invokeCommand "vscode.git.stage" --invokeParamsJson '{"paths":["src/main.ts"]}'
nodes invoke --node "my-vscode" --invokeCommand "vscode.git.commit" --invokeParamsJson '{"message":"fix: resolve type error"}'
```

### Delegate to Cursor Agent

```text
nodes invoke --node "my-vscode" --invokeCommand "vscode.agent.run" --invokeParamsJson '{"prompt":"Add error handling to all API endpoints","mode":"plan"}' --invokeTimeoutMs 180000 --timeoutMs 185000
→ { output, exitCode }
```

## Common Workflows

See [references/workflows.md](/api/v1/skills/vscode-node/file?path=references%2Fworkflows.md&ownerHandle=xiaoyaner0201) for detailed step-by-step workflows:

* Fix a type error
* Safe cross-file refactor
* Delegate complex task to Cursor Agent

## Error Handling

| Error | Cause | Solution |
| --- | --- | --- |
| `node command not allowed` | Not in Gateway whitelist | Add to `gateway.nodes.allowCommands` |
| `node not found` | Extension not connected | Check extension status bar |
| `timeout` | Operation too long | Increase both timeout params |
| `path traversal blocked` | Path outside workspace | Use relative paths only |
| `read-only mode` | Extension in read-only | Disable `skill-platform.readOnly` setting |

## Security

* All paths are **relative to workspace root** — absolute paths and `../` blocked
* Writes respect `readOnly` and `confirmWrites` extension settings
* Terminal disabled by default, whitelist-only when enabled
* Each device has unique Ed25519 identity, must be approved by Gateway

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

- Operate on code through a VS Code/Cursor IDE connected as an OpenClaw
  Node
- Provides 40+ commands
- 触发关键词: through, node, operate, cursor, code, vscode

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用VS Code Node？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: VS Code Node有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
