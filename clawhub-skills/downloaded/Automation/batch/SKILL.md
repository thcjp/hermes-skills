---
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
summary: "批量处理,先dry run再计数预估时长"
---
# Batch

## Before Starting

1. **Dry run:** Test with 2-3 items first
2. **Count:** "Processing 47 items, ~2 min estimated"
3. **Confirm destructive ops:** "This will delete 200 files. Proceed?"

## During Processing

* **Progress every 10 items:** "23/47 complete (49%)"
* **Checkpoint every 10-50 items:** Save state to resume if interrupted
* **On error:** Log it, continue with rest (don't abort entire batch)

## After Completion

Always report:

```text
✅ 44 succeeded
❌ 3 failed (saved to failed.json for retry)
```

## Error Handling

| Error | Action |
| --- | --- |
| Timeout, rate limit | Retry 3x with backoff (1s, 2s, 4s) |
| Bad format, missing data | Skip, log, continue |
| Auth failed, disk full | Abort entire batch |

Check `strategies.md` for parallel vs sequential decision matrix.
Check `errors.md` for retry logic and rollback patterns.

---

**Related:** For delegating to sub-agents, see `delegate`.

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

- Process multiple items with progress tracking, checkpointing, and failure
  recovery
- 触发关键词: items, progress, batch, multiple, process

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

```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Batch？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Batch有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

1. **输入限制**：Batch技能能够处理的项数有限制，通常建议不超过1000项，以避免长时间运行和资源消耗过大的问题。
2. **性能边界**：处理速度受限于底层模型能力和系统资源。在资源充足的情况下，处理速度可以达到每秒处理数十项。
3. **兼容性约束**：Batch技能依赖于LLM API，因此需要确保使用的Agent平台支持SKILL.md规范，并且LLM API版本兼容。
4. **数据格式**：输入数据必须符合规定的格式，否则可能导致处理失败。例如，数据项应包含必要的字段，且字段类型正确。
5. **网络稳定性**：Batch技能的执行依赖于稳定的网络连接。在网络不稳定的情况下，可能导致处理中断或失败。
6. **错误处理**：Batch技能对某些错误类型有预设的处理策略，但对于未预见的错误，可能需要人工介入解决。
7. **系统资源**：Batch技能的执行需要消耗系统资源，如CPU和内存。在高负载环境下，可能需要调整系统资源分配以避免性能下降。
8. **环境依赖**：Batch技能可能依赖于特定的环境变量或配置文件，这些依赖项需要在执行前正确设置。
---

