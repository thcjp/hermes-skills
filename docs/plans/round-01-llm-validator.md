# 本轮任务提示词 (Round 01)

> **生成时间**: 2026-07-20
> **基于**: `D:\skills\docs\plans\2026-07-20-skill-automation-v2-design.md` Phase 1 Step 1.1-1.2
> **目标**: 编写 llm_validator.py 并对 sales-copy-writer 试跑 L2 验证

## 任务概述

当前 Skill 自动化体系的验证层只有 L1 静态检查（quality_gate.py 10 项格式检查），缺少 L2 LLM 模拟验证。这导致 skill 通过格式检查后仍无法保证内容质量和可运行性。本轮任务是补全验证层的第一个步骤：编写 LLM 模拟验证器并小规模试跑。

## 本轮范围（严格限定）

1. **Step 1.1**: 编写 `d:\skills\skill-registry\llm_validator.py`
2. **Step 1.2**: 对 `sales-copy-writer` 试跑 L2 验证，保存报告

## 不在本轮范围

- dependency_verifier.py（下一轮）
- agent_trial.py（后续轮次）
- 三层验证集成到流水线（后续轮次）
- 批量处理（定稿后才推广）

## 关键约束

1. **小规模**: 只用 sales-copy-writer 一个 skill 验证
2. **实事求是**: 验证结果基于实际运行，不虚假实现
3. **不引入新 bug**: 修改前先读取原代码，修改后先试跑
4. **可追溯**: 验证结果保存为 JSON 报告
5. **复用现有**: 复用 trace_llm_scorer.py 的 TRACE_EVAL_PROMPT 和 static_check，不重复造轮子
6. **不调用外部 LLM API**: llm_validator.py 设计为"生成评估 prompt + 等待 LLM 响应"模式，由 AI（当前会话）充当 LLM 评估器，不硬编码 API 调用

## 验收标准

- [ ] `python llm_validator.py --help` 正常显示帮助
- [ ] `python llm_validator.py validate sales-copy-writer` 输出 L2 验证报告
- [ ] 报告包含 4 项检查结果（触发精准度/输出完整性/依赖可达性/TRACE 快评）
- [ ] 报告保存到 `d:\skills\skill-registry\l2_validation_report_sales-copy-writer.json`
- [ ] TRACE 评分合理（sales-copy-writer 纯 LLM 驱动，预期 ≥35/50）
