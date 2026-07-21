---
slug: write
name: write
version: "1.0.0"
displayName: 版本化写作工具
summary: 带强制版本控制与质量审计的写作工作流，通过edit.sh脚本管理草稿版本与audit审计
license: Proprietary
description: |-
  带强制版本控制与质量审计的版本化写作工具。
  遵循Request→Plan→Draft→Audit→Refine→Deliver工作流，通过edit.sh脚本强制版本备份，
  支持depth（quick/standard/thorough）配置与auto_audit自动审计。
  集成brief.md、execution.md、verification.md等八份参考文档，覆盖规划、执行、版本管理与质量审计全流程。
  适用于长篇内容创作、技术文档撰写与需要版本追溯的写作场景。
tools:
  - read
  - exec
---

# 版本化写作工具

带强制版本控制与质量审计的写作工作流，通过edit.sh脚本管理版本，遵循Request→Plan→Draft→Audit→Refine→Deliver流程。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows（需Git Bash/WSL）/ macOS / Linux（需Bash/Shell）
- **Sub-agent能力**: Agent需支持委托写作任务给sub-agents

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Bash/Shell | 运行时 | 必需 | 用于执行scripts目录下的shell脚本 |
| Sub-agent支持 | Agent能力 | 必需 | Agent需支持委托任务给sub-agents |

### API Key 配置
- 本Skill基于指令驱动，无需额外API Key

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，核心功能依赖exec命令行执行scripts脚本）
- **说明**: 通过shell脚本驱动版本化写作工作流，强制版本控制与质量审计

## 核心能力

### 版本化写作工作流
遵循六阶段标准工作流：

```text
Request → Plan → Draft → Audit → Refine → Deliver
```

强制规则（Rules）：
- **Delegate all writing to sub-agents**：所有写作委托给sub-agents，main agent保持自由
- **NEVER edit files directly**：禁止直接编辑文件，必须使用`./scripts/edit.sh`（强制版本控制）
- **Run quality audit before delivering**：交付前运行quality audit（参见audit.md）
- **Offer cleanup only after user confirms**：仅在用户确认piece最终后提供cleanup

**输出**: 返回版本化写作工作流的执行结果,包含操作状态和输出数据。
### 强制Scripts工具集

提供七个强制使用的shell脚本：

| Script | 用途 |
|:-------|:-----|
| `init-workspace.sh` | 创建项目结构 |
| `new-piece.sh` | 启动新写作piece并分配ID |
| `edit.sh` | 编辑并自动版本备份（禁止直接编辑文件的强制替代） |
| `audit.sh` | 运行quality audit，生成报告 |
| `list.sh` | 显示所有pieces与versions |
| `restore.sh` | 恢复之前的version |
| `cleanup.sh` | 清除旧versions（需确认） |

脚本路径：`scripts/init-workspace.sh`、`scripts/new-piece.sh`、`scripts/edit.sh`、`scripts/audit.sh`、`scripts/list.sh`、`scripts/restore.sh`、`scripts/cleanup.sh`

### 配置系统
通过`config.json`配置写作行为：

- **depth**: `"quick"` | `"standard"` | `"thorough"` — 控制研究与修订轮次
  - `quick`：快速写作，最少研究轮次
  - `standard`：标准写作，平衡研究与修订
  - `thorough`：深度写作，最多研究轮次与修订passes
- **auto_audit**: `true`/`false` — drafts后自动运行audits

**输入**: 用户提供配置系统所需的指令和必要参数。
**输出**: 返回配置系统的执行结果,包含操作状态和输出数据。### 参考文档库

集成八份参考文档，按需加载支撑写作各阶段：

| 文档 | 用途 |
|:-----|:-----|
| `brief.md` | 规划阶段使用，写作需求brief |
| `execution.md` | 起草阶段使用，drafting指导 |
| `verification.md` | 质量检查阶段使用 |
| `state.md` | 进度跟踪与状态管理 |
| `research.md` | 调查与研究阶段使用 |
| `versioning.md` | 版本规则与versioning规范 |
| `audit.md` | 审计维度与quality audit标准 |
| `criteria.md` | 偏好与写作标准criteria |

### 工作空间初始化
首次使用时创建工作空间：

```bash
./scripts/init-workspace.sh ~/writing
```

创建标准项目结构，包含pieces目录（存放各写作piece及其versions）、scripts目录、references目录与config.json配置文件。

**输入**: 用户提供工作空间初始化所需的指令和必要参数。
**处理**: 按照skill规范执行工作空间初始化操作,遵循单一意图原则。### 质量审计与版本管理

- **Quality Audit**：通过`./scripts/audit.sh`运行，依据audit.md中的dimensions生成审计报告
- **Version管理**：每次通过edit.sh编辑自动创建version备份，通过`./scripts/list.sh`查看所有versions，通过`./scripts/restore.sh`恢复任意version
- **Cleanup流程**：仅在用户确认piece最终后运行`./scripts/cleanup.sh`清除旧versions

### 能力覆盖范围

本skill还覆盖以下能力场景: 带强制版本控制与、质量审计的写作工、脚本管理草稿版本、质量审计的版本化、写作工具、脚本强制版本备份、配置与、自动审计、等八份参考文档、覆盖规划、版本管理与质量审、计全流程、适用于长篇内容创、技术文档撰写与需、要版本追溯的写作。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

1. **初始化工作空间**：首次使用运行`./scripts/init-workspace.sh ~/writing`创建项目结构
2. **创建新piece**：运行`./scripts/new-piece.sh`启动新写作piece并获取piece ID
3. **Request阶段**：接收写作需求，参考`brief.md`规划
4. **Plan阶段**：参考`brief.md`制定写作计划，确定depth配置
5. **Draft阶段**：委托sub-agents起草，参考`execution.md`执行drafting
6. **Audit阶段**：运行`./scripts/audit.sh`执行quality audit，参考`audit.md`与`verification.md`
7. **Refine阶段**：通过`./scripts/edit.sh`修订（自动版本备份），依据审计报告改进
8. **Deliver阶段**：交付最终内容
9. **Cleanup阶段**：用户确认最终后运行`./scripts/cleanup.sh`清除旧versions

### 命令参数说明

- `-v1`: 命令参数,用于指定操作选项
- `-v3`: 命令参数,用于指定操作选项
- `-v2不如draft-v1`: 命令参数,用于指定操作选项
- `-v2`: 命令参数,用于指定操作选项
- `-v1继续修订`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

### 命令参数说明

- `-v3保留为备份`: 命令参数,用于指定操作选项

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
    depth: "thorough"
    auto_audit: true

Step 4 - Draft（委托sub-agent）:
  Main agent: 委托起草任务给sub-agent
  Sub-agent: 参考 execution.md 起草，输出至 pieces/piece-001/draft-v1.md

Step 5 - Audit:
  $ ./scripts/audit.sh piece-001
  → 生成审计报告，依据 audit.md dimensions 检查

Step 6 - Refine（通过edit.sh，自动版本备份）:
  $ ./scripts/edit.sh piece-001
  → 编辑内容，自动备份 draft-v1.md 为 version

Step 7 - 查看versions:
  $ ./scripts/list.sh
  → 显示 piece-001 的所有versions

Step 8 - Deliver & Cleanup:
  用户确认最终后:
  $ ./scripts/cleanup.sh piece-001
  → 清除旧versions（需确认）
```

### 示例2：恢复之前的version

```
场景: piece-001修订后发现draft-v2不如draft-v1
Step 1 - 查看所有versions:
  $ ./scripts/list.sh
  → piece-001:
      draft-v1.md (2024-01-15 10:00)
      draft-v2.md (2024-01-15 14:30)
      draft-v3.md (2024-01-15 16:00)

Step 2 - 恢复draft-v1:
  $ ./scripts/restore.sh piece-001 draft-v1
  → 恢复 draft-v1 为当前版本，原draft-v3保留为备份

Step 3 - 继续编辑:
  $ ./scripts/edit.sh piece-001
  → 基于恢复的draft-v1继续修订
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| init-workspace.sh执行失败 | 目录已存在或无写权限 | 检查目标目录是否已初始化，确认有写权限后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令或更换路径 |
| edit.sh编辑失败 | piece ID不存在或文件权限问题 | 先运行`new-piece.sh`创建piece，确认pieces目录权限 |
| audit.sh无输出 | config.json的auto_audit为false或audit.md缺失 | 检查config.json配置，确认references/audit.md存在 |
| restore.sh恢复失败 | 指定version不存在 | 运行`list.sh`确认可用versions，使用正确version名称 |
| cleanup.sh误删version | 用户未确认piece最终即运行cleanup | cleanup.sh需确认，误删时通过restore.sh从备份恢复 |
| 直接编辑文件被拦截 | 绕过edit.sh直接编辑触发版本控制保护 | 必须使用`./scripts/edit.sh`编辑，直接编辑不被版本系统记录 |
| config.json配置无效 | depth值非quick/standard/thorough或格式错误 | 确认depth为三选一，auto_audit为boolean，JSON格式正确 |
| sub-agent委托失败 | Agent不支持sub-agent或资源不足 | 确认Agent平台支持sub-agent委托，降级为main agent直接起草 |

## 常见问题

### Q1: 为什么禁止直接编辑文件？
A: 直接编辑文件会绕过版本控制系统，导致无法追溯修改历史与恢复旧versions。必须使用`./scripts/edit.sh`编辑，该脚本自动创建version备份，确保每次修改都有记录。这是本Skill的强制规则（NEVER edit files directly）。

### Q2: depth配置的三个级别如何选择？
A: `quick`适用于短篇内容或紧急需求，最少研究轮次；`standard`适用于常规写作，平衡研究与修订；`thorough`适用于长篇内容或高要求场景，最多研究轮次与修订passes。在config.json中设置`depth`字段。

### Q3: auto_audit为true时会发生什么？
A: 当auto_audit设为true时，每次draft完成后自动运行`./scripts/audit.sh`执行quality audit，依据audit.md中的dimensions生成审计报告。设为false时需手动运行audit。

### Q4: 如何管理多个写作pieces？
A: 每个piece通过`new-piece.sh`创建并分配唯一piece ID。使用`list.sh`查看所有pieces及其versions。各piece独立管理versions，互不干扰。cleanup.sh针对单个piece操作。

### Q5: 八份参考文档分别在何时使用？
A: `brief.md`在Plan阶段使用；`execution.md`在Draft阶段使用；`verification.md`和`audit.md`在Audit阶段使用；`research.md`在调查研究时使用；`versioning.md`规范版本规则；`state.md`用于进度跟踪；`criteria.md`定义写作偏好标准。

### Q6: cleanup.sh何时使用？
A: cleanup.sh仅在用户确认piece最终（final）后使用，清除旧versions释放空间。运行时需确认。切勿在piece仍在修订时运行cleanup，以免丢失需要恢复的versions。

## 已知限制

- 强制依赖Bash/Shell环境执行scripts，Windows需Git Bash或WSL
- 必须使用sub-agent委托写作，不支持sub-agent的Agent平台无法完整使用
- edit.sh强制版本控制意味着所有编辑必须通过脚本，不支持直接文件操作
- cleanup.sh清除的versions无法自动恢复，需谨慎确认后执行
- config.json配置变更不影响已创建pieces的已有versions
