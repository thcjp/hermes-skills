# 下一轮执行提示词 v71.0

> 日期: 2026-07-27
> 版本: v71.0
> 前序: v70.0
> 关联: task-list-v1.0.md, implementation-plan-v1.0.md
> Git: 3f06a5da2 (feat(stage-1-1): 构建本地LLM质量评分器+金融技能采集+定价升级)

## 前置必读（强制）

在执行任何操作之前，必须完整阅读以下文档：

1. **任务清单**: `docs/plans/task-list-v1.0.md` — 3大任务17阶段51子任务的完整清单
2. **实施计划**: `docs/plans/implementation-plan-v1.0.md` — 详细的分步执行计划
3. **设计方案**: `docs/specs/2026-07-27-quality-governance-finance-skills-design.md` — 三层质量评分架构设计
4. **深度差异化方法论**: `docs/deep-differentiation-methodology.md`
5. **命名规范**: `docs/NAMING_CONVENTION.md`
6. **金融候选清单**: `data/discovery/finance_candidates.json` — 23个金融技能源候选

**严禁补丁式修复、碎片化功能、冗余化已有的主线和功能模块。**

## v70.0 完成情况回顾

| 任务 | 状态 | 产出 |
|------|------|------|
| T1-001 | ✅ 完成 | `tools/local_quality_scorer.py` — 5维度LLM评分器(智谱GLM-4-Flash) |
| T1-002 | ✅ 完成 | `data/config/quality_scoring_config.json` — 评分器配置 |
| T1-003 | ✅ 完成 | `tools/quality_gate.py` — 集成local_score到run_full_quality_check() |
| T1-004 | ✅ 完成 | `tools/db.py` — 新增local_quality_score等3个字段；验证通过(accounting-and-finance评分3.90) |
| T2-001 | ✅ 完成 | ClawHub Finance筛选10个优质源技能 |
| T2-002 | ✅ 完成 | GitHub扫描8个金融仓库(OpenBB/freqtrade/vnpy等) |
| T2-003 | ✅ 完成 | Web搜索5个金融技能源 |
| T2-005 | ✅ 完成 | `pricing_engine.py` — 新增金融量化类别(19.9-199元)+finance_premium层级 |
| T2-006 | ✅ 完成 | `task3_pricing_calibration.py` — 新增40+金融关键词+L5金融级(199.9元/月)+金融slug免除惩罚 |

**关键验证结果**:
- 本地评分器对accounting-and-finance skill评出3.90分（5维度: 完整性0.8/准确性0.9/易用性0.7/安全性0.9/创新性0.6）
- 向后兼容: `include_local_score=False`时返回结果不含local_score字段
- 金融定价: t-trading被正确识别为金融量化类别, market=small
- 金融slug免除惩罚: stock-filter-skills/okx-dex-token等penalty=0, 而json-formatter/csv-parser等penalty=4

**已知限制**:
- `github_scanner.py` 不支持 `--keywords`/`--min-stars` 参数,仅扫描配置文件中预定义的15个通用仓库。T2-002的GitHub候选通过Web搜索补充获取。
- 智谱GLM-4-Flash API调用需设置 `ZHIPU_API_KEY` 环境变量

## 本轮目标

本轮执行**第二批: 全量扫描+金融技能生产准备（T1-005~T1-007, T2-004, T2-007, T2-008~T2-011）**。

这是承上启下的关键轮次:
- 向上: 利用v70.0构建的评分器对全部存量skill执行质量扫描
- 向下: 对金融候选执行深度差异化生产,产出30个可上传的新技能

### 核心任务清单

| 优先级 | 编号 | 任务 | 预计耗时 | 依赖 |
|--------|------|------|---------|------|
| P0 | T1-005 | 编写批量扫描脚本（内联到现有工具，不新建文件） | 20分钟 | T1-004 ✅ |
| P0 | T1-006 | 执行全量扫描，结果写入DB `local_quality_score` 字段 | 60分钟 | T1-005 |
| P0 | T1-007 | 生成全量质量评分报告 `data/reports/local_quality_scan.json` | 15分钟 | T1-006 |
| P0 | T2-004 | 去重+质量初筛，确定最终20个源技能 | 20分钟 | T2-001~T2-003 ✅ |
| P1 | T2-007 | 验证升级后的定价策略对5个金融skill示例定价合理 | 15分钟 | T2-005~T2-006 ✅ |
| P0 | T2-008 | 对20个源技能执行 `auto_differentiate.py` 深度差异化 | 90分钟 | T2-004, T2-007 |
| P0 | T2-009 | 免费/收费分配决策：10个普及型产免费版，10个高价值仅付费 | 15分钟 | T2-008 |
| P0 | T2-010 | 为10个普及型技能生产免费版SKILL.md | 30分钟 | T2-009 |
| P0 | T2-011 | 对20个付费版应用升级后的定价策略，写入suggested_price | 20分钟 | T2-008, T2-005~T2-006 |

## 详细执行指令

### T1-005: 编写批量扫描脚本

**要求**: 不新建文件，将批量扫描功能内联到 `tools/local_quality_scorer.py` 的 CLI 入口

**实现方式**:
- 在 `local_quality_scorer.py` 的 `main()` 函数中新增 `scan-all` 子命令
- 遍历 `packaged-skills/skillhub/` 和 `opensource-skills/packaged/` 目录
- 对每个含SKILL.md的目录调用 `score_skill()` 获取评分
- 将评分结果写入DB skills表的 `local_quality_score`、`local_score_feedback`、`local_score_at` 字段
- 支持断点续扫: 跳过DB中 `local_quality_score > 0` 的skill
- 支持限速: 每次LLM调用间隔1秒（避免API限流）
- 输出进度: 每扫描10个skill打印一次进度

**CLI用法**:
```bash
# 全量扫描
python tools/local_quality_scorer.py scan-all

# 扫描指定目录
python tools/local_quality_scorer.py scan-all --dir packaged-skills/skillhub

# 强制重新扫描（不跳过已评分的）
python tools/local_quality_scorer.py scan-all --force
```

**关键约束**:
- 不新建脚本文件，仅扩展 `local_quality_scorer.py` 的main函数
- 不复制 `quality_gate.py` 的检查逻辑，仅调用 `score_skill()`
- LLM调用失败时记录error并继续（不中断批量扫描）
- 扫描结果直接写入DB，不生成中间文件

### T1-006: 执行全量扫描

**执行命令**: `python tools/local_quality_scorer.py scan-all`

**预期**:
- 扫描 `packaged-skills/skillhub/` 下约1046个skill
- 每个skill调用一次LLM API（约2-3秒/个）
- 总耗时约60分钟（含1秒间隔）
- DB中 `local_quality_score` 非空的skill数 ≥ 1000

**中断恢复**: 如果扫描中断，重新执行 `scan-all` 命令即可，已扫描的skill会被跳过（除非加 `--force`）

### T1-007: 生成全量质量评分报告

**文件**: `data/reports/local_quality_scan.json`（自动生成）

**报告内容**:
```json
{
  "scan_at": "2026-07-27T...",
  "total_scanned": 1046,
  "score_distribution": {
    "0.0-2.0": 0,
    "2.0-3.0": 15,
    "3.0-3.5": 80,
    "3.5-4.0": 200,
    "4.0-4.5": 350,
    "4.5-5.0": 401
  },
  "low_score_count": 295,  // score <= 4.5
  "passed_count": 751,     // score > 4.5
  "avg_score": 4.12,
  "dimension_avg": {
    "completeness": 0.82,
    "accuracy": 0.85,
    "usability": 0.78,
    "security": 0.88,
    "innovation": 0.65
  },
  "low_score_skills": [
    {"slug": "xxx", "score": 3.2, "weakest_dim": "innovation", "feedback": "..."}
  ]
}
```

### T2-004: 金融候选去重合并

**输入**: `data/discovery/finance_candidates.json`（23个候选）
**输出**: 确定最终20个源技能（去重后）

**去重规则**:
1. ClawHub和Web来源重叠的技能合并为一个（如Alpaca-MCP在GitHub和Web都出现）
2. 功能高度相似的技能选择质量更高的一个
3. 确保20个源技能覆盖三个差异化方向:
   - A股方向: 6-7个（stock-filter-skills, t-trading, TradingAgents-Astock, finance-radar, finance-report-analyzer, financial-literacy, finance）
   - 加密货币方向: 6-7个（okx-dex-token, test, freqtrade, Freqtrade-MCP, Alpaca-MCP, rho-telegram-alerts）
   - 财务分析方向: 6-7个（accounting-and-finance, OpenBB, Investor-Agent, backtrader, vnpy）

**产出**: 更新 `data/discovery/finance_candidates.json`，添加 `final_20` 字段列出最终20个源技能

### T2-007: 定价验证

**验证方法**: 对5个代表性金融skill执行完整定价流程

```bash
# 对5个金融skill示例执行定价
python tools/pricing_engine.py price <skill_dir>
python tools/task3_pricing_calibration.py  # 执行定价校准
```

**验证标准**:
- 5个示例定价在19.9-199元区间
- 层级分布合理（至少1个L3, 1个L4, 1个L5）
- 金融类skill不会被误判为简单工具（penalty=0）
- 定价依据清晰可解释

**产出**: 定价验证结果记录到 `data/reports/finance_pricing_validation.json`

### T2-008: 深度差异化生产20个付费版

**输入**: 最终20个源技能（T2-004产出）
**工具**: `tools/auto_differentiate.py`

**执行流程**:
1. 对每个源技能执行安全预检（21项）
2. 去标识化（移除源项目名/作者/仓库链接）
3. 功能增强（根据差异化方法论提升内容质量）
4. 生成差异化SKILL.md（付费版，license=Proprietary）
5. 对差异化后的SKILL.md执行 `run_full_quality_check(include_local_score=True)`
6. local_score ≤ 4.5 的根据反馈重做，循环直到 > 4.5

**关键约束**:
- 严禁直接复制源技能内容，必须实质性差异化
- 去标识化必须彻底（无源项目名/作者/仓库URL）
- frontmatter的slug必须全局唯一（kebab-case）
- frontmatter的homepage不能指向原始开源仓库
- 每个差异化后的SKILL.md必须通过21项安全预检

### T2-009: 免费/收费分配决策

**分配原则**:
- **免费版（10个）**: 普及型、教育型、基础工具型技能
  - 候选: financial-literacy, finance(行情跟踪), finance-radar(选股雷达), rho-telegram-alerts(告警), financial-literacy等
  - 特征: 功能相对简单、容易被提示词逆向、市场教育价值高
- **仅付费版（10个）**: 高价值、专业级、易被逆向的技能
  - 候选: accounting-and-finance(58个子技能), stock-filter-skills(A股17个CLI), t-trading(交易策略), okx-dex-token(13个命令)等
  - 特征: 功能复杂、专业壁垒高、直接关联投资收益

**产出**: 分配决策表记录到 `data/discovery/finance_allocation.json`

### T2-010: 生产10个免费版

**要求**:
- 对10个普及型技能生产免费版SKILL.md
- 免费版功能精简但完整（不是阉割版，是聚焦核心功能的精炼版）
- frontmatter: `license: MIT`, `edition: free`
- 放置目录: `packaged-skills/skillhub/<slug>-free/`
- 对免费版也执行 `run_full_quality_check(include_local_score=True)`
- local_score > 4.5 才算通过

### T2-011: 20个付费版定价写入

**执行**:
```bash
# 对20个付费版执行定价
python tools/pricing_engine.py price-all
python tools/pricing_engine.py apply
python tools/task3_pricing_calibration.py
```

**验证**:
- 每个付费版SKILL.md的frontmatter含 `suggested_price` 字段
- 金额在19.9-199元区间
- 层级分布: L2(2-3个), L3(5-6个), L4(7-8个), L5(3-4个)
- DB中对应skill的 `suggested_price` 和 `pricing_tier` 已更新

## 执行约束

1. **严禁补丁式修复**: 批量扫描功能是local_quality_scorer.py的CLI扩展，不是新建脚本
2. **严禁碎片化功能**: 本轮不新建独立脚本文件，仅扩展已有工具
3. **严禁冗余化**: 不复制现有46项检查逻辑，评分器是独立的LLM评测层
4. **严禁mock/fallback/todo/pass**: LLM调用必须真实实现，批量扫描必须真实执行
5. **单向依赖**: `local_quality_scorer` → `quality_gate` → `upload_gate`，不反向依赖
6. **差异化质量**: 深度差异化必须实质性提升内容质量，不是简单改名换词
7. **安全预检**: 所有差异化后的SKILL.md必须通过21项安全预检
8. **Git提交**: 完成后提交: `feat(stage-1-2): 全量扫描+金融技能深度差异化生产30个`

## 验证标准

本轮完成需满足以下全部条件:

1. `local_quality_scorer.py scan-all` 命令可执行，支持断点续扫
2. DB中 `local_quality_score` 非空的skill数 ≥ 1000
3. `data/reports/local_quality_scan.json` 报告已生成，含评分分布和低分清单
4. `finance_candidates.json` 的 `final_20` 字段含20个最终源技能
5. 5个金融skill定价验证通过（19.9-199元区间，层级合理）
6. 20个付费版SKILL.md已差异化生产，全部通过安全预检和local_score > 4.5
7. 10个免费版SKILL.md已生产，全部通过local_score > 4.5
8. 20个付费版的frontmatter含suggested_price，金额在19.9-199元
9. DB中30个新skill的记录已创建，workflow_state为quality_passed

## 本轮不执行的任务

以下任务在后续轮次执行，本轮不涉及:
- T1-008~T1-012（低分重做）— 依赖T1-007全量扫描完成
- T1-013~T1-015（上传跟踪）— 依赖T1-012
- T2-012~T2-014（三层质检+打回重做）— 本轮T2-008~T2-011已包含质检，T2-012~T2-014为正式质检记录
- T2-015~T2-016（全平台上传）— 依赖T2-014
- T3-001~T3-010（平台治理）— 依赖T1-004和T2-014

## 下一轮预告

v72.0将执行:
- T1-008~T1-012: 低分skill批量重做循环（≤4.5分的skill根据5维度反馈升级）
- T1-013~T1-015: 通过质检的skill批量上传SkillHub + 评分跟踪
- T2-012~T2-014: 30个金融skill正式质检记录
- T2-015~T2-016: 30个金融skill全平台上传（SkillHub + ClawHub + GitHub）
- T3-001~T3-002: 平台评分批量同步
