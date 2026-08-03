# 下一轮执行提示词 v70.0

> 日期: 2026-07-27
> 版本: v70.0
> 前序: v69.0
> 关联: task-list-v1.0.md, implementation-plan-v1.0.md

## 前置必读（强制）

在执行任何操作之前，必须完整阅读以下文档：

1. **任务清单**: `docs/plans/task-list-v1.0.md` — 3大任务17阶段51子任务的完整清单
2. **实施计划**: `docs/plans/implementation-plan-v1.0.md` — 详细的分步执行计划
3. **设计方案**: `docs/specs/2026-07-27-quality-governance-finance-skills-design.md` — 三层质量评分架构设计
4. **深度差异化方法论**: `docs/deep-differentiation-methodology.md`
5. **命名规范**: `docs/NAMING_CONVENTION.md`

**严禁补丁式修复、碎片化功能、冗余化已有的主线和功能模块。**

## 本轮目标

本轮执行**第一批: 构建本地评分器（T1-001 ~ T1-004）**，这是阻塞后续所有任务的基础设施。

同时并行启动**第二批中可独立执行的部分**: T2-001（ClawHub金融技能筛选）、T2-002（GitHub扫描）、T2-003（Web搜索）、T2-005~T2-007（定价策略升级）。

### 核心任务清单

| 优先级 | 编号 | 任务 | 预计耗时 |
|--------|------|------|---------|
| P0 | T1-001 | 编写 `tools/local_quality_scorer.py` 5维度LLM评分器 | 30分钟 |
| P0 | T1-002 | 编写 `data/config/quality_scoring_config.json` 配置 | 10分钟 |
| P0 | T1-003 | 扩展 `tools/quality_gate.py` 集成local_score | 20分钟 |
| P0 | T1-004 | DB新增字段 + 评分器验证 | 20分钟 |
| P1 | T2-001 | ClawHub Finance分类筛选8-10个优质源技能 | 15分钟 |
| P1 | T2-002 | GitHub扫描金融相关高星仓库 | 15分钟 |
| P1 | T2-003 | Web搜索补充金融技能源 | 15分钟 |
| P1 | T2-005 | 升级 `pricing_engine.py` 金融定价 | 20分钟 |
| P1 | T2-006 | 升级 `task3_pricing_calibration.py` 金融定价 | 15分钟 |

## 详细执行指令

### T1-001: 编写 local_quality_scorer.py

**文件**: `tools/local_quality_scorer.py`（新增，唯一新增核心模块）

**要求**:
- 实现5维度评测: 功能完整性/准确性/易用性/安全性/创新性
- 每维度0.0-1.0分，总分0.0-5.0分
- 附文字改进建议（每维度说明扣分原因）
- 阈值4.5（与 `quality_gate.py` 的 `RATING_GATE_THRESHOLD` 一致）
- 支持输入: SKILL.md文件路径 或 目录路径 或 文件内容字符串
- 输出: `{total_score, dimensions: {key: {score, reason}}, feedback, passed}`
- LLM调用配置从 `data/config/quality_scoring_config.json` 读取
- 评测prompt要求LLM返回严格JSON格式
- CLI入口: `python tools/local_quality_scorer.py <skill_dir_or_path>`

**关键约束**:
- 不创建mock/fallback逻辑——LLM调用失败时返回 `{total_score: 0.0, error: "..."}`，由上层判断
- 不复制 `quality_gate.py` 的检查逻辑——评分器是独立的LLM评测，与46项合规检查互补
- 评测维度对齐SkillHub平台AI评测维度，使本地分数与平台分数可比

### T1-002: 编写评分器配置

**文件**: `data/config/quality_scoring_config.json`（新增）

包含: LLM API端点/密钥/模型/温度、5维度定义和权重、评分阈值、评测prompt模板。

### T1-003: 扩展 quality_gate.py

**文件**: `tools/quality_gate.py`（修改，仅扩展不重构）

**修改点**:
1. `run_full_quality_check()` 新增 `include_local_score=True` 参数
2. 在5层46项检查之后，汇总之前，新增 `run_local_scoring()` 调用
3. 返回结果新增 `local_score`(0.0-5.0)、`local_score_feedback`(文字)、`local_score_dimensions`(dict)
4. `local_score < 4.5` → `overall_passed = False`，追加失败检查项

**关键约束**:
- 不改动现有5层46项检查的任何逻辑
- `include_local_score=False` 时行为与现有完全一致（向后兼容）
- `local_quality_scorer` 导入失败时不阻断流程（返回score=0.0 + warning）

### T1-004: DB schema + 验证

- DB skills表新增: `local_quality_score`(REAL)、`local_score_feedback`(TEXT)、`local_score_at`(TEXT)
- 通过 `tools/db.py` 的 `_ensure_columns()` 幂等添加
- 验证: 对已知平台评分的skill（如university-applications-sk 3.3分）执行本地评分，偏差≤0.5分

### T2-001~T2-003: 金融技能采集（并行）

- T2-001: 读取 `clawhub-skills/downloaded/Finance/` 下12个技能，筛选8-10个优质源
- T2-002: `python tools/github_scanner.py --keywords "quant,trading,stock,futures,crypto" --min-stars 50`
- T2-003: WebSearch搜索 "AI agent stock trading skill"、"quantitative trading MCP tool" 等

### T2-005~T2-006: 定价策略升级（并行）

- T2-005: `pricing_engine.py` 新增金融类别基础价(19.9-199元)、扩展价格点、MAX_PRICE提升至199
- T2-006: `task3_pricing_calibration.py` 新增金融高价值关键词、L4上限提升、金融类免除简单工具惩罚

## 执行约束

1. **严禁补丁式修复**: 评分器是整体性新模块，不是对现有检查的打补丁
2. **严禁碎片化功能**: 本轮仅新增2个文件(`local_quality_scorer.py` + `quality_scoring_config.json`)，修改2个文件(`quality_gate.py` + DB schema)，不创建其他新文件
3. **严禁冗余化**: 不复制现有46项检查逻辑，评分器是独立的LLM评测层
4. **严禁mock/fallback/todo/pass**: LLM调用必须真实实现，不使用模拟数据
5. **单向依赖**: `local_quality_scorer` → `quality_gate` → `upload_gate`，不反向依赖
6. **向后兼容**: `run_full_quality_check(include_local_score=False)` 与现有行为完全一致
7. **Git提交**: 完成T1-001~T1-004后提交一次: `feat(stage-1-1): 构建本地LLM质量评分器并集成到quality_gate`

## 验证标准

本轮完成需满足以下全部条件:

1. `tools/local_quality_scorer.py` 存在且可执行: `python tools/local_quality_scorer.py <任一skill目录>` 输出JSON评分
2. `data/config/quality_scoring_config.json` 存在且可被正确加载
3. `run_full_quality_check(skill_md, include_local_score=True)` 返回结果含 `local_score` 字段
4. `run_full_quality_check(skill_md, include_local_score=False)` 返回结果不含 `local_score`（向后兼容）
5. DB skills表含 `local_quality_score` 字段
6. 对已知3.3分skill执行本地评分，偏差≤0.5分（即本地评分在2.8-3.8之间）
7. `pricing_engine.py` 的MAX_PRICE已更新为199.0
8. `task3_pricing_calibration.py` 含金融高价值关键词
9. ClawHub Finance候选清单已生成（8-10个技能）
10. GitHub金融候选清单已生成（5-8个仓库）

## 本轮不执行的任务

以下任务在后续轮次执行，本轮不涉及:
- T1-005~T1-007（全量扫描）— 依赖T1-004完成
- T1-008~T1-012（低分重做）— 依赖T1-007
- T2-004（去重合并候选）— 依赖T2-001~T2-003
- T2-007（定价验证）— 依赖T2-005~T2-006
- T2-008~T2-011（差异化生产）— 依赖T2-004和T2-007
- T3-001~T3-010（平台治理）— 依赖T1-004

## 下一轮预告

v71.0将执行:
- T1-005~T1-007: 全量存量扫描（1046个skill）
- T2-004: 金融候选去重合并
- T2-007: 定价验证
- T2-008~T2-011: 深度差异化生产30个金融技能
