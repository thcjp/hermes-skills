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
  Node. Provides 40+ commands...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: through, node, operate, cursor, code, vscode
tags:
- Development
tools:
- read
- exec
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

## Quick Examples

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
