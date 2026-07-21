# Round 10: 大规模推广与质量提升 (Phase 6)

> **前置条件**: Round 09 已完成（批量推广+模板验证+质量看板+持续优化）
> **设计文档**: `D:\skills\docs\plans\2026-07-20-skill-automation-v2-design.md`
> **预估时间**: 90-120 分钟
> **验收标准**: 100+skill批量推广 + L2低分skill优化 + L3覆盖扩展 + 运维闭环验证

---

## 背景与目标

Phase 1-5 已全部完成：
- L1/L2/L3 三层验证体系就绪（L2覆盖率100%, L3覆盖率0.2%）
- 5种设计模式模板全部验证通过（generator/reviewer/pipeline/tool_wrapper/inversion）
- generate_skill.py 生成流水线就绪（含章节模糊匹配+定制占位符+夸大词清除）
- health_check.py + quality_dashboard.py + 3个cron定时任务就绪
- 16个P0-P2 skill全链路验证完成（L1 16/16 + L2 16/16 A级）
- TRACE阈值分层启用（L2_PASS=35, L2_EXCELLENT=45, L2_MANUAL_REVIEW=40）
- L2低分标注机制就绪（发现2个需优化skill: auto-workflow, cad-insight-pro）

Phase 6 聚焦大规模推广和质量提升：
1. **100+skill批量推广**: 扩展P3-P5批量的全链路验证
2. **L2低分skill优化**: 对73个B/C级skill进行AI手动优化
3. **L3覆盖扩展**: 从3个扩展到20+个skill的L3试运行
4. **运维闭环验证**: 整合health_check + quality_dashboard + cron形成完整闭环

---

## 当前状态快照

| 指标 | 当前值 | 目标值 |
|------|--------|--------|
| 总skill数 | 1866 | 1866 |
| L1覆盖率 | 55.8% (1042) | ≥80% (1500+) |
| L2覆盖率 | 100% (1866) | 100% |
| L2通过率 | 99.8% (1863) | 100% |
| L2 A级比例 | 96.1% (1793) | ≥98% (1830+) |
| L3覆盖率 | 0.2% (3) | ≥1% (20+) |
| 完成率 | 3.3% (61) | ≥10% (186+) |
| 平台上传 | 188成功 | 300+ |
| 需优化skill | 2个 (B/C级) | 0个 |

---

## 任务清单

### Step 6.1: 100+skill批量推广

**目标**: 扩展P3-P5批量的全链路验证，覆盖100+个skill

**执行步骤**:

1. **筛选P3-P5候选** (目标100个):
   ```bash
   cd D:\skills\skill-registry
   python -c "
   import sys; sys.path.insert(0, '.')
   from config import get_db_connection
   conn = get_db_connection()
   c = conn.cursor()
   c.execute('''
     SELECT slug, category, workflow_state
     FROM skills
     WHERE workflow_state IN ('step5_add_deps', 'step7_validate')
       AND slug NOT LIKE '%-free%' AND slug NOT LIKE '%-pro%'
     ORDER BY category, slug
     LIMIT 100
   ''')
   for r in c.fetchall():
       print(f'{r[\"slug\"]} | {r[\"category\"]} | {r[\"workflow_state\"]}')
   conn.close()
   "
   ```

2. **分批生成+L1验证** (每批20个):
   ```bash
   # 批量生成脚本 (复用Round 09的batch_rollout逻辑)
   python batch_generate.py --limit 100 --batch-size 20
   ```

3. **批量L2评估**:
   ```bash
   # 复用Round 09的batch_l2_eval逻辑
   python batch_l2_eval.py --limit 100
   ```

4. **更新workflow_state**:
   - 通过L1+L2的skill: step5_add_deps → step6_generate_skill → step7_validate

**验收标准**:
- [ ] 100个skill通过L1 10/10
- [ ] 100个skill通过L2 ≥35
- [ ] L1覆盖率提升到≥80%
- [ ] 生成batch_generate.py和batch_l2_eval.py可复用脚本

---

### Step 6.2: L2低分skill优化

**目标**: 对73个B/C级skill进行AI手动优化，提升到A级

**执行步骤**:

1. **扫描低分skill**:
   ```bash
   python trace_llm_scorer.py annotate --json > low_score_annotations.json
   ```

2. **分类优化策略**:
   - **B级(40-44, 71个)**: 基于薄弱维度标注，针对性优化章节内容
   - **C级(35-39, 2个)**: 需重新生成或大幅优化
   - **A级但接近临界(45-46)**: 可选优化，提升安全边际

3. **批量优化执行**:
   - 对每个低分skill，根据annotated的weak_chapters列表
   - 使用generate_skill.py重新生成（启用所有优化）
   - 重新运行L1+L2验证
   - 对比优化前后评分

4. **优化效果验证**:
   ```bash
   python trace_llm_scorer.py annotate  # 确认低分skill数量减少
   python quality_dashboard.py --dimension 2  # 查看质量分布变化
   ```

**验收标准**:
- [ ] C级skill(35-39)数量降为0
- [ ] B级skill(40-44)数量减少50%以上
- [ ] A级skill(≥45)比例提升到≥98%
- [ ] 优化前后评分对比报告生成

---

### Step 6.3: L3覆盖扩展

**目标**: 从3个扩展到20+个skill的L3真实agent试运行

**执行步骤**:

1. **筛选L3候选** (20个):
   - 优先选择L2评分≥45的skill
   - 覆盖5种模板类型（每种至少3个）
   - 覆盖主要category（Communication, Development, Productivity等）

2. **批量L3试运行**:
   ```bash
   # 对每个候选skill生成L3试运行prompt
   for slug in "${L3_CANDIDATES[@]}"; do
     python agent_trial.py trial "$slug" -o "l3_trial_${slug}.json"
   done
   ```

3. **AI执行L3试运行**:
   - 读取每个l3_trial_*.json中的trial_prompt
   - AI作为agent执行6个试运行用例（3典型+3异常）
   - 评估输出可用性
   - 生成l3_result_*.json

4. **批量导入L3结果**:
   ```bash
   for slug in "${L3_CANDIDATES[@]}"; do
     python agent_trial.py import "$slug" "l3_result_${slug}.json"
   done
   ```

**验收标准**:
- [ ] 20个skill完成L3试运行
- [ ] L3通过率≥80% (≥16/20)
- [ ] L3覆盖率提升到≥1%
- [ ] 5种模板均有L3验证记录

---

### Step 6.4: 运维闭环验证

**目标**: 整合health_check + quality_dashboard + cron形成完整运维闭环

**执行步骤**:

1. **运维闭环流程验证**:
   ```bash
   # Step 1: 健康检查
   python health_check.py --json
   
   # Step 2: 质量看板
   python quality_dashboard.py --json
   
   # Step 3: 低分标注
   python trace_llm_scorer.py annotate --json
   
   # Step 4: 检查cron任务状态
   # (通过Schedule tool list查看3个cron任务的执行历史)
   ```

2. **闭环自动化脚本**:
   创建 `ops闭环.py`，整合以下流程:
   - 运行health_check → 识别问题
   - 运行quality_dashboard → 识别低分
   - 运行annotate → 标注需优化skill
   - 自动生成优化建议报告

3. **cron任务状态验证**:
   - skill-source-update (daily 09:00): 验证最近执行结果
   - skill-governance-scan (weekly Mon 10:00): 验证最近执行结果
   - skill-health-check (weekly Mon 11:00): 验证最近执行结果

4. **运维报告生成**:
   ```bash
   python ops闭环.py -o ops_report_$(date +%Y%m%d).json
   ```

**验收标准**:
- [ ] ops闭环.py创建完成
- [ ] 3个cron任务最近执行状态正常
- [ ] 运维闭环报告生成（含健康检查+质量看板+低分标注）
- [ ] 闭环流程文档化

---

## 执行顺序

1. **Step 6.1** → 100+skill批量推广 (40-50 分钟)
2. **Step 6.2** → L2低分skill优化 (20-30 分钟)
3. **Step 6.3** → L3覆盖扩展 (20-30 分钟)
4. **Step 6.4** → 运维闭环验证 (10-15 分钟)
5. **汇总** → 生成Phase 6完成报告

---

## Round 09 完成总结

### 已完成成果

| 项目 | 状态 | 详情 |
|------|------|------|
| 16个P0-P2 skill全链路验证 | ✅ 完成 | L1 16/10通过, L2 16/16通过(平均47/50, 全A级) |
| 5种模板验证覆盖 | ✅ 完成 | tool_wrapper(aws-toolkit 44/50 B) + inversion(doc-parse 47/50 A) |
| 质量看板建立 | ✅ 完成 | quality_dashboard.py 5维度监控, 终端表格+JSON输出 |
| 章节替换增强 | ✅ 完成 | 模糊匹配: 功能→核心能力, 快速开始→使用流程等10+映射 |
| 占位符填充优化 | ✅ 完成 | 5种模板+5种category定制默认值 |
| L2低分标注机制 | ✅ 完成 | annotate命令, 发现2个需优化skill(auto-workflow, cad-insight-pro) |
| TRACE阈值分层 | ✅ 完成 | L2_PASS=35, L2_MANUAL_REVIEW=40, L2_EXCELLENT=45 |
| slug/name修正 | ✅ 完成 | 解决-pro后缀导致L1不一致问题 |
| 夸大词+占位符文本清除 | ✅ 完成 | "最佳/最强"→"优秀", "待补充"→"详情见说明" |

### 修复的Bug

| Bug | 根因 | 修复方案 |
|-----|------|---------|
| 16个skill L1全部失败(8-9/10) | 原始差异化skill带-pro后缀, slug/name与文件夹名不一致 | generate_from_template添加target_slug参数, 修正frontmatter |
| discord-chat-manager含夸大词"最佳" | 原始内容携带夸大词未被清理 | Step 5.5添加夸大词清除(10个词→"优秀") |
| google-workspace-cli含"待补充" | 原始代码示例携带占位符文本 | Step 5.6添加占位符文本清除(8个词→"详情见说明") |
| quality_dashboard.py平台查询失败 | platform_uploads表无price列, 实际为pricing_on_platform | 修改SQL查询使用正确列名 |

### 项目总体进度

| Phase | 内容 | 状态 |
|-------|------|------|
| Phase 1 | 验证层 (L1+L2+L3) | ✅ 完成 |
| Phase 2 | 生成层 (模板+流水线) | ✅ 完成 |
| Phase 3 | 运维层 (健康检查+定时任务) | ✅ 完成 |
| Phase 4 | 定稿与清理 | ✅ 完成 |
| Phase 5 | 批量推广与持续优化 | ✅ 完成 |
| Phase 6 | 大规模推广与质量提升 | ⏳ 待执行 (Round 10) |
