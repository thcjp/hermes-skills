---
slug: write-free
name: write-free
version: "1.0.0"
displayName: 版本化写作工具（免费版）
summary: 免费版版本化写作工具，支持基础工作流与edit.sh版本控制
license: MIT
description: |-
  带版本控制的写作工具（免费版）。
  遵循Request→Plan→Draft→Audit→Refine→Deliver基础工作流，通过edit.sh脚本管理版本。
  支持depth基础配置。免费版不含完整参考文档库与质量审计深度能力。
tools:
  - read
  - exec
---

# 版本化写作工具（免费版）

带基础版本控制的写作工具，通过edit.sh脚本管理版本，遵循Request→Plan→Draft→Audit→Refine→Deliver流程。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows（需Git Bash/WSL）/ macOS / Linux（需Bash/Shell）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Bash/Shell | 运行时 | 必需 | 用于执行scripts目录下的shell脚本 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，核心功能依赖exec命令行执行scripts脚本）
- **说明**: 通过shell脚本驱动版本化写作工作流，支持基础版本控制

## 核心能力

### 版本化写作工作流
遵循六阶段标准工作流：

```text
Request → Plan → Draft → Audit → Refine → Deliver
```

强制规则（Rules）：
- **Delegate all writing to sub-agents**：所有写作委托给sub-agents，main agent保持自由
- **NEVER edit files directly**：禁止直接编辑文件，必须使用`./scripts/edit.sh`（强制版本控制）
- **Run quality audit before delivering**：交付前运行quality audit
- **Offer cleanup only after user confirms**：仅在用户确认piece最终后提供cleanup

**输出**: 返回版本化写作工作流的执行结果,包含操作状态和输出数据。
### 基础Scripts工具集

提供核心shell脚本：

| Script | 用途 |
|:-------|:-----|
| `init-workspace.sh` | 创建项目结构 |
| `new-piece.sh` | 启动新写作piece并分配ID |
| `edit.sh` | 编辑并自动版本备份 |
| `audit.sh` | 运行quality audit，生成报告 |
| `list.sh` | 显示所有pieces与versions |
| `restore.sh` | 恢复之前的version |
| `cleanup.sh` | 清除旧versions（需确认） |

### 配置系统
通过`config.json`配置写作行为：

- **depth**: `"quick"` | `"standard"` | `"thorough"` — 控制研究与修订轮次
- **auto_audit**: `true`/`false` — drafts后自动运行audits

**输入**: 用户提供配置系统所需的指令和必要参数。
**输出**: 返回配置系统的执行结果,包含操作状态和输出数据。### 工作空间初始化
首次使用时创建工作空间：

```bash
./scripts/init-workspace.sh ~/writing
```

创建标准项目结构，包含pieces目录、scripts目录、references目录与config.json配置文件。

**输入**: 用户提供工作空间初始化所需的指令和必要参数。
**处理**: 按照skill规范执行工作空间初始化操作,遵循单一意图原则。

### 能力覆盖范围

本skill还覆盖以下能力场景: 免费版版本化写作、支持基础工作流与、带版本控制的写作、免费版、基础工作流、脚本管理版本、基础配置、免费版不含完整参、考文档库与质量审、计深度能力。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

1. **初始化工作空间**：首次使用运行`./scripts/init-workspace.sh ~/writing`创建项目结构
2. **创建新piece**：运行`./scripts/new-piece.sh`启动新写作piece并获取piece ID
3. **Plan阶段**：制定写作计划，确定depth配置
4. **Draft阶段**：委托sub-agents起草
5. **Audit阶段**：运行`./scripts/audit.sh`执行quality audit
6. **Refine阶段**：通过`./scripts/edit.sh`修订（自动版本备份）
7. **Deliver阶段**：交付最终内容
8. **Cleanup阶段**：用户确认最终后运行`./scripts/cleanup.sh`清除旧versions

### 命令参数说明

- `-v1`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 示例

### 示例1：创建并完成一篇技术文档

```
Step 1 - 初始化工作空间:
  $ ./scripts/init-workspace.sh ~/writing
  → 创建项目结构（pieces/、scripts/、references/、config.json）

Step 2 - 创建新piece:
  $ ./scripts/new-piece.sh
  → 分配 piece ID: piece-001

Step 3 - 配置:
  config.json:
    depth: "standard"
    auto_audit: false

Step 4 - Draft（委托sub-agent）:
  Main agent: 委托起草任务给sub-agent
  Sub-agent: 起草，输出至 pieces/piece-001/draft-v1.md

Step 5 - Audit:
  $ ./scripts/audit.sh piece-001
  → 生成审计报告

Step 6 - Refine（通过edit.sh，自动版本备份）:
  $ ./scripts/edit.sh piece-001
  → 编辑内容，自动备份为version

Step 7 - 查看versions:
  $ ./scripts/list.sh
  → 显示 piece-001 的所有versions

Step 8 - Deliver & Cleanup:
  用户确认最终后:
  $ ./scripts/cleanup.sh piece-001
  → 清除旧versions（需确认）
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| init-workspace.sh执行失败 | 目录已存在或无写权限 | 检查目标目录是否已初始化，确认有写权限后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令或更换路径 |
| edit.sh编辑失败 | piece ID不存在或文件权限问题 | 先运行`new-piece.sh`创建piece，确认pieces目录权限 |
| restore.sh恢复失败 | 指定version不存在 | 运行`list.sh`确认可用versions，使用正确version名称 |

## 常见问题

### Q1: 免费版与付费版有何区别？
A: 免费版提供基础版本化写作工作流与七项核心scripts。不含完整八份参考文档库（brief.md、execution.md、verification.md、state.md、research.md、versioning.md、audit.md、criteria.md）的详细使用指导与深度质量审计能力。

### Q2: 为什么禁止直接编辑文件？
A: 直接编辑文件会绕过版本控制系统，导致无法追溯修改历史与恢复旧versions。必须使用`./scripts/edit.sh`编辑，该脚本自动创建version备份。这是本Skill的强制规则（NEVER edit files directly）。

### Q3: depth配置的三个级别如何选择？
A: `quick`适用于短篇内容，最少研究轮次；`standard`适用于常规写作；`thorough`适用于长篇内容，最多研究轮次与修订passes。在config.json中设置`depth`字段。

## 已知限制

- 不含完整八份参考文档库（brief.md、execution.md、verification.md、state.md、research.md、versioning.md、audit.md、criteria.md）的详细使用指导
- 不含深度质量审计能力，audit为基础版
- 强制依赖Bash/Shell环境执行scripts，Windows需Git Bash或WSL
- cleanup.sh清除的versions无法自动恢复，需谨慎确认后执行
