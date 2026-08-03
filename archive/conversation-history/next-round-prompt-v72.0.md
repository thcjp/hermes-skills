# 下一轮执行提示词 v72.0

> 日期: 2026-07-27
> 版本: v72.0
> 前序: v71.0
> 关联: task-list-v1.0.md, implementation-plan-v1.0.md
> Git: 18172c465 (feat(stage-1-2): 全量扫描+金融技能深度差异化生产30个)

## 前置必读（强制）

在执行任何操作之前，必须完整阅读以下文档：

1. **任务清单**: `docs/plans/task-list-v1.0.md` — 3大任务17阶段51子任务的完整清单
2. **实施计划**: `docs/plans/implementation-plan-v1.0.md` — 详细的分步执行计划
3. **设计方案**: `docs/specs/2026-07-27-quality-governance-finance-skills-design.md` — 三层质量评分架构设计
4. **金融分配决策**: `data/discovery/finance_allocation.json` — 10免费+10仅付费分配
5. **命名规范**: `docs/NAMING_CONVENTION.md`

**严禁补丁式修复、碎片化功能、冗余化已有的主线和功能模块。**

## v71.0 完成情况回顾

| 任务 | 状态 | 产出 |
|------|------|------|
| T1-005 | ✅ 完成 | `local_quality_scorer.py scan-all` 子命令（并行5线程+断点续扫） |
| T1-006 | ⏳ 进行中 | 后台扫描1072个skill，已评分125个（平均3.55分） |
| T1-007 | ⏳ 待生成 | 报告将在扫描完成后自动生成 |
| T2-004 | ✅ 完成 | `finance_candidates.json` final_20字段（20个源技能去重确定） |
| T2-007 | ✅ 完成 | 5个金融skill定价验证通过（19.9-99.9元，L3/L4层级） |
| T2-008 | ✅ 完成 | 20个付费版SKILL.md深度差异化生产（含10个GitHub/Web合成内容） |
| T2-009 | ✅ 完成 | `finance_allocation.json` — 10免费+10仅付费分配决策 |
| T2-010 | ✅ 完成 | 10个免费版SKILL.md生产（license=MIT, edition=free） |
| T2-011 | ✅ 完成 | 20个付费版定价写入frontmatter（L2:2/L3:8/L4:6/L5:4，19.9-199元） |

**关键验证结果**:
- 30个金融skill DB记录已创建（id 4627-4656），workflow_state=finance_differentiate
- 20个付费版: license=Proprietary, edition=pro, 含pricing_tier/suggested_price
- 10个免费版: license=MIT, edition=free, 无定价字段
- 定价层级分布: L2(2个@19.9) + L3(8个@29.9) + L4(6个@99.9) + L5(4个@199.0)
- 本地评分器: 125个skill已评分，平均3.55分，全部≤4.5（需批量重做）
- 安全预检: 所有差异化SKILL.md通过后差异化安全验证（exec误报已豁免）

**已知问题**:
- 全量扫描速度约0.2/s（5线程），1072个skill预计需要约90分钟
- 当前125个已评分skill全部≤4.5，平均3.55分，说明存量skill质量普遍需要提升
- 评分维度反馈显示创新性(innovation)和完整性(completeness)是最薄弱维度
- DB并发写入需注意：全量扫描期间避免同时执行DB写入操作

## 本轮目标

本轮执行**第三批: 全量扫描完成+低分重做+金融技能质检上传（T1-006~T1-015, T2-012~T2-016, T3-001~T3-002）**。

这是规模最大的执行轮次:
- 向上: 完成全量扫描，生成质量报告，识别所有需重做的低分skill
- 中间: 对低分skill执行批量重做循环，直到评分>4.5
- 向下: 对30个金融skill执行正式质检+全平台上传

### 核心任务清单

| 优先级 | 编号 | 任务 | 预计耗时 | 依赖 |
|--------|------|------|---------|------|
| P0 | T1-006 | 等待全量扫描完成（后台进行中） | 80分钟 | T1-005 ✅ |
| P0 | T1-007 | 生成全量质量评分报告 | 5分钟 | T1-006 |
| P0 | T1-008 | 分析低分skill的5维度反馈，制定重做策略 | 30分钟 | T1-007 |
| P0 | T1-009 | 批量重做低分skill（根据反馈升级内容） | 120分钟 | T1-008 |
| P0 | T1-010 | 对重做后的skill重新评分 | 60分钟 | T1-009 |
| P0 | T1-011 | 循环重做直到评分>4.5（最多3轮） | 180分钟 | T1-010 |
| P0 | T1-012 | 标记通过质检的skill，更新workflow_state | 15分钟 | T1-011 |
| P1 | T1-013 | 批量上传通过质检的skill到SkillHub | 60分钟 | T1-012 |
| P1 | T1-014 | 跟踪平台AI评分（上传后24h） | 24小时 | T1-013 |
| P1 | T1-015 | 评估是否升级本地评分系统 | 30分钟 | T1-014 |
| P0 | T2-012 | 对30个金融skill执行run_full_quality_check | 30分钟 | T2-008~T2-011 ✅ |
| P0 | T2-013 | 记录30个金融skill的质检结果到DB | 15分钟 | T2-012 |
| P0 | T2-014 | 对质检未通过的金融skill打回重做 | 60分钟 | T2-013 |
| P0 | T2-015 | 30个金融skill上传SkillHub | 60分钟 | T2-014 |
| P0 | T2-016 | 30个金融skill上传ClawHub + GitHub | 60分钟 | T2-015 |
| P1 | T3-001 | 批量同步SkillHub平台评分到DB | 30分钟 | T1-013, T2-015 |
| P1 | T3-002 | 批量同步ClawHub评分到DB | 30分钟 | T2-016 |

## 详细执行指令

### T1-006/T1-007: 完成全量扫描+生成报告

**前提**: 后台扫描进程正在运行（job-0041c4e89b394cafae9039635b383704）

**检查命令**:
```bash
# 检查扫描进度
# 通过 CheckCommandStatus 工具查看 job-0041c4e89b394cafae9039635b383704 的输出

# 如果扫描中断，重新启动（支持断点续扫）
python tools/local_quality_scorer.py scan-all
```

**完成标准**:
- DB中 `local_quality_score > 0` 的skill数 ≥ 1000
- `data/reports/local_quality_scan.json` 报告已自动生成

**报告内容预期**:
```json
{
  "scan_at": "2026-07-27T...",
  "total_scanned": 1072,
  "score_distribution": {
    "0.0-2.0": ~5,
    "2.0-3.0": ~50,
    "3.0-3.5": ~400,
    "3.5-4.0": ~500,
    "4.0-4.5": ~117,
    "4.5-5.0": 0
  },
  "low_score_count": 1072,
  "passed_count": 0,
  "avg_score": 3.55,
  "dimension_avg": {
    "completeness": 0.65,
    "accuracy": 0.75,
    "usability": 0.72,
    "security": 0.80,
    "innovation": 0.55
  }
}
```

### T1-008: 分析低分skill反馈，制定重做策略

**分析方法**:
```bash
# 查询DB中所有已评分skill的5维度分数和反馈
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('SELECT slug, local_quality_score, local_score_feedback FROM skills WHERE local_quality_score > 0 ORDER BY local_quality_score ASC LIMIT 20')
for row in c.fetchall():
    print(f'{row[0]:30s} | score={row[1]:.2f} | feedback={row[2][:100]}')
conn.close()
"
```

**重做策略制定原则**:
1. 按5维度反馈识别最薄弱维度（预计: innovation < completeness < usability < accuracy < security）
2. 按slug前缀分组（同类skill批量处理）
3. 按分数分层处理:
   - ≤2.0分: 需要完全重写（内容质量极差）
   - 2.0-3.0分: 需要大幅增强（缺失核心内容）
   - 3.0-4.0分: 需要针对性提升（补强弱维度）
   - 4.0-4.5分: 需要微调（接近通过线）

**产出**: `data/reports/low_score_rework_strategy.json`

### T1-009~T1-011: 批量重做循环

**重做流程**:
1. 读取低分skill的SKILL.md
2. 根据5维度反馈识别弱项
3. 调用LLM增强内容（补全缺失章节、增加使用示例、增强安全性描述）
4. 写回SKILL.md
5. 重新调用 `local_quality_scorer.py score <slug>` 评分
6. 如果评分 ≤ 4.5，根据新反馈继续重做（最多3轮）

**批量重做脚本要求**:
- 不新建脚本文件，扩展 `local_quality_scorer.py` 新增 `rework` 子命令
- 支持按分数范围筛选: `--min-score 0 --max-score 3.0`
- 支持按slug前缀筛选: `--prefix api-`
- 支持限制数量: `--limit 50`
- 每个skill重做后立即重新评分
- 评分 > 4.5 的标记为passed，跳过后续轮次

**CLI用法**:
```bash
# 重做所有≤3.0分的skill
python tools/local_quality_scorer.py rework --max-score 3.0

# 重做前50个低分skill
python tools/local_quality_scorer.py rework --limit 50

# 重做特定前缀的skill
python tools/local_quality_scorer.py rework --prefix api-
```

### T1-012: 标记通过质检的skill

```bash
# 批量更新workflow_state为quality_passed
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('UPDATE skills SET workflow_state = ? WHERE local_quality_score > 4.5 AND workflow_state IS NULL', ('quality_passed',))
print(f'已标记 {c.rowcount} 个skill为quality_passed')
conn.commit()
conn.close()
"
```

### T2-012: 30个金融skill正式质检

**执行**:
```bash
# 对30个金融skill执行完整质检
python tools/quality_gate.py check --category Finance --include-local-score
```

**验证标准**:
- 30个金融skill全部通过L2/L3/L4检查
- local_score > 4.5（如果≤4.5，需打回重做）

### T2-013~T2-014: 质检记录+打回重做

**记录到DB**:
```sql
UPDATE skills SET workflow_state = 'quality_passed'
WHERE slug IN (30个金融skill的slug列表)
AND local_quality_score > 4.5;
```

**打回重做**: 对local_score ≤ 4.5的金融skill，根据5维度反馈增强SKILL.md内容

### T2-015~T2-016: 全平台上传

**SkillHub上传**:
```bash
# 上传30个金融skill到SkillHub
python tools/auto_publish.py publish --category Finance
```

**ClawHub上传**:
```bash
# 上传30个金融skill到ClawHub
python tools/clawhub_batch_uploader.py --from-db --limit 30 --category Finance
```

**GitHub公开引流**:
```bash
# 推送到GitHub公开仓库
cd d:\skills
git add packaged-skills/skillhub/*-free/
git commit -m "feat: add 10 free finance skills"
git push hermes-skills main
```

### T3-001~T3-002: 平台评分同步

**SkillHub评分同步**:
```bash
python tools/market_monitor.py sync-ratings --limit 200
```

**ClawHub评分同步**:
```bash
python tools/market_monitor.py sync-ratings --platform clawhub --limit 200
```

## 执行约束

1. **严禁mock/fallback/todo/pass**: LLM调用必须真实，重做必须实质性提升内容
2. **严禁补丁式修复**: 批量重做功能是local_quality_scorer.py的CLI扩展
3. **DB并发安全**: 全量扫描期间不执行DB写入操作；扫描完成后再执行重做
4. **重做质量**: 每次重做必须根据5维度反馈针对性提升，不是简单重写
5. **循环上限**: 单个skill最多重做3轮，3轮后仍≤4.5则标记为manual_review
6. **单向依赖**: local_quality_scorer → quality_gate → upload_gate，不反向依赖
7. **安全预检**: 重做后的SKILL.md仍需通过21项安全预检
8. **Git提交**: 完成后提交: `feat(stage-1-3): 全量扫描完成+低分重做+金融技能质检上传`

## 验证标准

本轮完成需满足以下全部条件:

1. DB中 `local_quality_score > 0` 的skill数 ≥ 1000
2. `data/reports/local_quality_scan.json` 报告已生成
3. 低分skill重做后，`local_quality_score > 4.5` 的skill数 ≥ 500
4. 30个金融skill全部通过质检（local_score > 4.5）
5. 30个金融skill已上传SkillHub
6. 10个免费版金融skill已上传ClawHub + GitHub
7. DB中30个金融skill的workflow_state为quality_passed或uploaded
8. 平台评分已同步到DB

## 下一轮预告

v73.0将执行:
- T3-003~T3-010: 平台存量skill评分治理（≤4.5分的批量升级）
- 评估本地评分系统是否需要升级（对比平台AI评分与本地评分的差异）
- 金融skill上架后的市场反馈跟踪
- 自动化流水线整合（daily_sync.py集成全量扫描+重做+上传）
