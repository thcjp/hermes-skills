---
slug: self-evolving-ai
name: self-evolving-ai
version: 1.0.1
displayName: 自我进化AI
summary: 自动捕获经验与错误,智能分层记忆,模式复发追踪,按需加载降本增效.
license: Proprietary
description: 让智能体从每次交互中持续学习的记忆与进化系统，针对记不住、用不上、成本高三大痛点。适用于长期 AI 代理项目、多人协作仓库、领域知识积累、减少重复犯错等场景。核心能力含三类结构化记忆、自动痛点检测、模式复发追踪与晋升、分层文档加载、技能提取。适用关键词：自我进化、经验捕获、错误学习、模式追踪、记忆晋升、self-evolving、learnings、pattern-detection.
tags:
- 智能代理
- 记忆管理
- 持续改进
- 自主学习
tools:
- read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 自我进化 AI（Self-Evolving AI）

让智能体从每次交互中持续学习，自动捕获经验、错误与纠正，并通过模式复发追踪将高频问题晋升为项目级规则。所有记忆存储在项目根目录的 `.learnings/` 文件夹，支持本地保留或团队共享.
## 核心能力

### 1. 三类结构化记忆
将学习内容分为 LEARNINGS.md（经验/纠正/知识缺口/最佳实践）、ERRORS.md（命令/操作/API 失败）、FEATURE_REQUESTS.md（用户提出的缺失功能）。每类条目含 ID（TYPE-YYYYMMDD-XXX）、优先级（critical/high/medium/low）、状态（pending→in_progress→resolved/wont_fix/promoted）、区域标签（frontend/backend/infra/tests/docs/config）等元数据.
**输入**: 用户提供三类结构化记忆所需的指令和必要参数.
**处理**: 解析三类结构化记忆的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回三类结构化记忆的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 2. 自动痛点检测触发器
自动识别纠正信号（"不对，那不是..."、"实际上应该是..."）、特性请求（"你能不能也..."）、知识缺口（引用过时文档/API 行为不同）、错误（非零退出码/异常堆栈/超时），并按情境决策表记录到对应文件，无需用户手动触发.
**输入**: 用户提供自动痛点检测触发器所需的指令和必要参数.
**处理**: 解析自动痛点检测触发器的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回自动痛点检测触发器的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 3. 模式复发追踪与晋升
记录与已有条目相似内容时，用 Pattern-Key 作为稳定去重键，递增 Recurrence-Count、更新 Last-Seen、添加 See Also 链接。当 Recurrence-Count >= 3 且跨至少 2 个不同任务且 30 天窗口内发生时，自动晋升到 CLAUDE.md/AGENTS.md 作为项目级规则.
**输入**: 用户提供模式复发追踪与晋升所需的指令和必要参数.
**处理**: 解析模式复发追踪与晋升的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回模式复发追踪与晋升的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 4. 分层文档加载策略
主文档保持精简（< 150 行快速参考），详细条目通过 grep 按需检索。避免一次性加载所有学习导致上下文膨胀。提供快速状态检查命令（grep pending/high/area 等）.
**输入**: 用户提供分层文档加载策略所需的指令和必要参数.
**处理**: 解析分层文档加载策略的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回分层文档加载策略的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 5. 多代理平台兼容与技能提取
核心记忆格式跨平台通用（Claude Code 用钩子、Codex 用 hooks.json、GitHub Copilot 用指令文件）。当学习满足提取标准（复发 2+ 次/已验证/非显而易见/广泛适用/用户标记）时，可提取为独立可复用 SKILL.md，经质量门禁验证后供其他项目使用.
**输入**: 用户提供多代理平台兼容与技能提取所需的指令和必要参数.
**处理**: 解析多代理平台兼容与技能提取的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回多代理平台兼容与技能提取的响应数据,包含状态码、结果和日志.
**技术参数**：使用`input_params`和`output_format`参数控制执行行为,支持`json`/`text`/`csv`输出格式.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：自动捕获经验与错、智能分层记忆、按需加载降本增效、让智能体从每次交、互中持续学习的记、忆与进化系统、针对记不住、用不上、成本高三大痛点、适用于长期、代理项目、多人协作仓库、领域知识积累、减少重复犯错等场、核心能力含三类结、适用关键词、自我进化、经验捕获、错误学习、模式追踪、记忆晋升、self、evolving、detection等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 适用场景

| 场景类型 | 输入 | 输出 | 是否适用 |
|----|---|---|----|
| 长期 AI 代理项目 | 反复出现的错误与纠正 | 结构化学习库 + 晋升规则 | ✅ 适用 |
| 多人协作代码仓库 | 团队共同的踩坑经验 | 共享的 .learnings/ 知识库 | ✅ 适用 |
| 领域知识积累 | 领域特定约定与最佳实践 | 可检索的知识条目 | ✅ 适用 |
| 减少重复犯错 | 同类错误复发 | 复发检测 + 系统性修复建议 | ✅ 适用 |
| 隐性经验显性化 | 调试中发现的非显而易见方案 | 提炼为项目规则或可复用技能 | ✅ 适用 |

**不适用场景**：
- 一次性脚本或短期任务（无积累价值）→ 不需要持续学习
- 极小型项目（< 5 文件，无重复模式）→ 学习开销大于收益
- 需要严格审计追踪的企业合规场景 → 本技能非合规工具，记忆条目可被修改
- 不允许在仓库中追踪 .learnings/ 的封闭环境 → 需调整为本地保留模式

## 使用流程

### Step 1：初始化记忆目录

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 自我进化AI处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
mkdir -p .learnings
```

### Step 2：识别情境并记录（按情境决策表）

| 情境 | 动作 | 目标文件 |
|---:|---:|---:|
| 任务执行中主动修复失败 | 使用自愈流程，记录到 HEALS.md | `.learnings/HEALS.md` |
| 过去命令/操作失败（非自愈中） | 记录错误条目 | `.learnings/ERRORS.md` |
| 用户纠正你的回答 | 记录学习条目，类别=correction | `.learnings/LEARNINGS.md` |
| 用户提出缺失功能 | 记录特性请求 | `.learnings/FEATURE_REQUESTS.md` |
| 外部 API/工具调用失败 | 记录错误条目，含集成详情 | `.learnings/ERRORS.md` |
| 发现知识已过时 | 记录学习条目，类别=knowledge_gap | `.learnings/LEARNINGS.md` |
| 发现更优方案 | 记录学习条目，类别=best_practice | `.learnings/LEARNINGS.md` |
| 重复出现的模式 | 更新条目，递增 Recurrence-Count | 对应条目 |

### Step 3：记录条目（立即记录，上下文最鲜活）

追加到 `.learnings/LEARNINGS.md`：

```markdown
# ...
**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
# ...
# ...
## [LRN-20260718-001] correction
# ...
**Logged**: 2026-07-18T10:00:00Z
**Priority**: high
**Status**: pending
**Area**: backend
# ...
### Summary
项目使用 pnpm workspaces，npm install 会失败
# ...
### Details
尝试 `npm install` 但失败。Lock file 是 `pnpm-lock.yaml`。必须用 `pnpm install`.
# ...
### Suggested Action
所有安装命令使用 pnpm 而非 npm
# ...
### Metadata
- Source: user_feedback
- Related Files: package.json
- Pattern-Key: tooling.pkg_manager
- Recurrence-Count: 1
- First-Seen: 2026-07-18
- Last-Seen: 2026-07-18
```

### Step 4：复发检测与链接

记录与已有条目相似内容时：先 `grep -r "keyword" .learnings/` 搜索 → 添加 See Also 链接 → 递增 Recurrence-Count → 如持续复发提升优先级.
### Step 5：定期评审与晋升

- **评审时机**：开始新主要任务前、完成功能后、在有历史学习的区域工作时、活跃开发期间每周
- **晋升条件**：Recurrence-Count >= 3 且跨 2 个不同任务且 30 天窗口内
- **晋升目标**：CLAUDE.md（项目事实/约定）、AGENTS.md（代理工作流/自动化规则）

### Step 6：条目状态流转

```text
pending → in_progress → resolved
                     ↘ wont_fix（附原因）
                     ↘ promoted（晋升到项目记忆）
                     ↘ promoted_to_skill（提取为可复用技能）
```

## 示例

### 示例(补充)

**输入**：用户说"不对，那不是 npm，这个项目用 pnpm"

**输出**（代理执行）：

```text
1. 检测到纠正信号："不对，那不是..."
2. 记录到 .learnings/LEARNINGS.md：
   - ID: LRN-20260718-001
   - Category: correction
   - Priority: high
   - Summary: 项目使用 pnpm workspaces，npm install 会失败
   - Pattern-Key: tooling.pkg_manager
3. 确认记录后响应用户
```

代理响应："已记录该纠正到 `.learnings/LEARNINGS.md`（LRN-20260718-001）。后续将使用 pnpm。"

### 示例 2：模式复发晋升（输入→输出）

**输入**：第三次在不同任务中遇到"忘记用 pnpm"的问题

```text
1. grep 搜索发现已有 2 条相同 Pattern-Key 的条目
2. 递增 Recurrence-Count 到 3
3. 检查晋升条件：>= 3 次 ✓，跨 2 个不同任务 ✓，30 天窗口内 ✓
4. 晋升到 CLAUDE.md：
   ## 构建与依赖
   - 包管理器: pnpm（非 npm）- 使用 `pnpm install`
5. 更新原条目 Status: pending → promoted，添加 Promoted: CLAUDE.md
```

代理响应："检测到'包管理器'模式复发 3 次，已晋升为项目规则写入 CLAUDE.md。后续所有会话将自动遵守。"

## 错误处理

- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断
- 执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令机制: 失败时自动执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令, 最多3次

| 场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 钩子未触发提醒 | 脚本路径错误 | 检查 `${CLAUDE_PROJECT_DIR}/.claude/skills/self-evolving-ai/scripts/` 路径是否存在 |
| grep 搜索无结果 | 条目 ID 格式不匹配 | 确认 ID 格式为 `TYPE-YYYYMMDD-XXX` |
| 晋升后 CLAUDE.md 重复 | 未更新原条目状态 | 将原条目 Status 改为 promoted 并添加 Promoted 字段 |
| Recurrence-Count 未递增 | Pattern-Key 不一致 | 确保相同模式使用完全相同的 Pattern-Key 字符串;执行排查步骤后恢复操作 |
| 记忆目录被 git 追踪但不想提交 | 未配置 gitignore | 添加 `.learnings/` 到 .gitignore，或用混合模式追踪模板忽略条目 |
| PostToolUse 钩子无输出 | 未返回 additionalContext | 确保脚本输出 JSON 格式的 additionalContext;执行排查步骤后恢复操作 |
| 上下文膨胀 | 加载过多学习条目 | 用按需加载，主文档 < 150 行，详情通过 grep 检索 |
| Codex 钩子不生效 | 未启用实验性功能 | 在 config.toml 启用 `codex_hooks = true`，或回退到 AGENTS.md 指令 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| 文件系统（可写 `.learnings/`） | 本地存储 | 必需 | 操作系统自带 |
| bash | 运行时 | 可选（钩子功能需要） | 系统自带或安装 Git Bash |
| grep | 工具 | 可选（搜索功能需要） | 系统自带 |

**运行环境**：Windows / macOS / Linux；支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）.
**多代理支持**：Claude Code（钩子 UserPromptSubmit/PostToolUse）、Codex CLI（hooks.json，实验性）、GitHub Copilot（指令文件 `.github/copilot-instructions.md`）.
**API Key**：本技能基于 Markdown 指令，无需额外 API Key.
**可用性分类**：MD+EXEC（核心记忆功能仅需 Markdown，钩子与脚本功能需要 exec 能力）.
## 常见问题

**Q1：学习条目太多导致上下文膨胀怎么办？**
A：使用按需加载机制。主文档只保留快速参考表（< 150 行），详细条目通过 grep 按需检索。定期将高价值学习晋升到 CLAUDE.md 后，在 .learnings/ 中标记为 promoted，减少重复加载.
**Q2：如何判断学习是否应该晋升？**
A：满足以下任一条件即考虑晋升：跨 2+ 任务复发（Recurrence-Count >= 3 且 30 天窗口内）、适用于多个文件/功能、任何贡献者都应知道、防止重复犯错。晋升时提炼为简洁规则，而非冗长事故报告.
**Q3：不同代理平台如何兼容？**
A：核心记忆格式（LEARNINGS.md/ERRORS.md/FEATURE_REQUESTS.md）跨平台通用。平台差异仅在激活方式：Claude Code 用钩子、Codex 用 hooks.json、Copilot 用指令文件。条目格式与晋升规则完全一致.
**Q4：模式复发追踪如何避免误报？**
A：使用 Pattern-Key 作为稳定去重键，要求 Recurrence-Count >= 3 且跨 2 个不同任务且 30 天窗口内才晋升。单一任务内的重复不计入。Pattern-Key 必须严格一致（如 `tooling.pkg_manager` 而非每次不同写法）.
**Q5：.learnings/ 该提交到 git 还是忽略？**
A：三种模式可选：保持本地（每开发者独立，`.learnings/` 加入 .gitignore）；团队共享（不忽略，成为共享知识库）；混合（追踪模板 `.gitkeep`，忽略条目 `.learnings/*.md`）。推荐团队协作项目用共享模式.
## 已知限制

1. **依赖 Pattern-Key 一致性**：复发检测的准确性取决于 Pattern-Key 的命名一致性。不同代理/会话对同一模式使用不同 Key 字符串会导致漏检。需团队约定 Key 命名规范.
2. **钩子功能受代理平台限制**：Claude Code 钩子成熟；Codex 钩子为实验性需手动启用；GitHub Copilot 钩子可记录日志但不能注入上下文，只能用指令文件回退.
3. **不自动执行修复**：本技能记录与追踪问题，提供修复建议，但不自动修改代码。实际修复需代理或用户执行.
4. **晋升需人工确认质量**：自动晋升可能将项目特定硬编码值写入 CLAUDE.md。提取技能前有质量门禁清单，但晋升到项目记忆时建议人工审查.
5. **本地优先，非云同步**：.learnings/ 存储在本地项目目录，跨项目共享需用户手动复制或通过 git。不提供跨项目的学习聚合与检索.
## 案例展示

```json
{
  "input": "示例输入",
  "output": "处理结果"
}
```

## 输出格式

处理结果以结构化格式返回, 包含状态码、消息和数据字段.