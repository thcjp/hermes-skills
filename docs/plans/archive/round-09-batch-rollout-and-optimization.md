# Round 09: 批量推广与持续优化 (Phase 5)

> **前置条件**: Round 08 已完成（定稿验证 + 文件清理）
> **设计文档**: `D:\skills\docs\plans\2026-07-20-skill-automation-v2-design.md`
> **预估时间**: 60-90 分钟
> **验收标准**: P0-P2(16个skill)全链路推广完成 + 质量看板建立

---

## 背景与目标

Phase 1-4 已全部完成：
- L1/L2/L3 三层验证体系就绪
- 5种设计模式模板 + generate_skill.py 生成流水线就绪
- health_check.py + 3个cron定时任务 + workflow_migrator.py 运维层就绪
- 3个定稿skill验证通过（L1 10/10 + L2 ≥35 + L3 90/100）
- 10步workflow_states启用（11625条记录）
- 文件深度清理完成（28临时 + 14归档 + 4冗余脚本删除）

Phase 5 聚焦批量推广和持续优化：
1. **P0-P2快速推广**: 16个高优先级skill全链路验证+上传
2. **Tool Wrapper/Inversion模板验证**: 补全5种模板的验证覆盖
3. **质量看板建立**: 创建可视化质量监控面板
4. **持续优化机制**: 基于定稿反馈优化生成流水线

---

## 任务清单

### Step 5.1: P0-P2快速推广 (16个skill)

**目标**: 对16个高优先级skill执行全链路验证并上传

**执行步骤**:

1. **筛选P0-P2候选**:
   ```bash
   cd D:\skills\skill-registry
   python -c "
   import sys; sys.path.insert(0, '.')
   from config import get_db_connection
   conn = get_db_connection()
   c = conn.cursor()
   # P0: 零依赖(无外部API/npm/pip)
   c.execute(\"\"\"
     SELECT slug, category, workflow_state
     FROM skills
     WHERE workflow_state = 'step7_validate'
       AND slug NOT LIKE '%-free%' AND slug NOT LIKE '%-pro%'
     ORDER BY category, slug
     LIMIT 16
   \"\"\")
   for r in c.fetchall():
       print(f'{r[\"slug\"]} | {r[\"category\"]} | {r[\"workflow_state\"]}')
   conn.close()
   "
   ```

2. **批量生成SKILL.md**:
   ```bash
   python generate_skill.py batch --category Productivity --limit 8
   python generate_skill.py batch --category Development --limit 8
   ```

3. **逐个L1+L2+L3验证**:
   对每个skill执行:
   ```bash
   python quality_gate.py packaged-skills/skillhub/<slug>/SKILL.md --json
   python dependency_verifier.py verify <slug> --json
   python llm_validator.py validate <slug> --json
   python agent_trial.py trial <slug> -o l3_trial_<slug>.json
   # AI评估L2+L3后导入
   python llm_validator.py import <slug> l2_eval_<slug>.json
   python agent_trial.py import <slug> l3_result_<slug>.json
   ```

4. **批量上传到SkillHub**:
   ```bash
   python update_mechanism.py sync <slug> --platform skillhub --free
   python update_mechanism.py sync <slug> --platform skillhub --paid --price 9.9
   ```

**验收标准**:
- [ ] 16个skill全部通过L1 10/10
- [ ] 16个skill全部通过L2 ≥35
- [ ] 16个skill全部通过L3 ≥70
- [ ] 16个skill全部上传到SkillHub

---

### Step 5.2: Tool Wrapper/Inversion模板验证

**目标**: 补全5种设计模式模板的验证覆盖

**候选skill筛选**:
- Tool Wrapper: 从DB中筛选API封装类skill (含"wrapper/api/sdk/client"关键词)
- Inversion: 从DB中筛选需求收集类skill (含"反推/还原/问答/收集"关键词)

**执行步骤**:
1. 筛选2个候选skill (各1个)
2. 使用对应模板生成SKILL.md
3. 执行L1+L2+L3验证
4. 对比5种模板的质量评分

**验收标准**:
- [ ] Tool Wrapper模板验证通过 (L1 10/10 + L2 ≥35)
- [ ] Inversion模板验证通过 (L1 10/10 + L2 ≥35)
- [ ] 5种模板质量评分对比报告生成

---

### Step 5.3: 质量看板建立

**目标**: 创建可视化质量监控面板

**文件**: `D:\skills\skill-registry\quality_dashboard.py`

**看板内容**:
1. **验证覆盖率**: L1/L2/L3各层验证的skill数量和覆盖率
2. **质量分布**: L2 TRACE评分分布 (A/B/C/D等级)
3. **模板使用**: 5种模板的使用数量和平均评分
4. **推广进度**: 10步workflow_states的完成分布
5. **平台状态**: SkillHub/ClawHub的上传成功率和待审核数

**输出格式**: JSON + 终端表格 (不依赖外部可视化库)

**验收标准**:
- [ ] quality_dashboard.py 创建完成
- [ ] 能输出5个维度的质量指标
- [ ] 终端表格格式清晰可读

---

### Step 5.4: 持续优化机制

**目标**: 基于定稿反馈优化生成流水线

**优化项**:

1. **章节替换增强**:
   - 问题: 原始skill章节名与模板不匹配时内容无法替换
   - 优化: 增加模糊匹配(如"功能"→"核心能力", "快速开始"→"使用流程")

2. **占位符填充优化**:
   - 问题: 部分默认值偏通用(如"按流程执行")
   - 优化: 根据模板类型和skill category定制默认值

3. **L2评分提升**:
   - 问题: rule-based生成质量为B级(35-44),达不到A级(≥45)
   - 优化: 在L2评估后,对低于40分的skill自动标注需AI手动优化的章节

4. **TRACE_PASS_THRESHOLD统一**:
   - 问题: 计划要求≥35, config.py设为42
   - 优化: 统一为35,或在config.py中区分L2_threshold(35)和L2_excellent(45)

**验收标准**:
- [ ] generate_skill.py 章节替换增强
- [ ] fill_remaining_placeholders 默认值优化
- [ ] L2低分标注机制实现
- [ ] TRACE_PASS_THRESHOLD 统一

---

## 执行顺序

1. **Step 5.1** → P0-P2快速推广 (30-40 分钟)
2. **Step 5.2** → Tool Wrapper/Inversion模板验证 (15-20 分钟)
3. **Step 5.3** → 质量看板建立 (10-15 分钟)
4. **Step 5.4** → 持续优化机制 (10-15 分钟)
5. **汇总** → 生成最终验证报告

---

## Round 08 完成总结

### 已完成成果

| 项目 | 状态 | 详情 |
|------|------|------|
| 3个skill L3定稿验证 | ✅ 完成 | daily-report-writer/code-quality/auto-workflow 全部 90/100 (A级) |
| agent_trial.py DB写入修复 | ✅ 完成 | L3评分现在写入scores表 (agent_trial类型) |
| 定稿质量分析 | ✅ 完成 | finalization-quality-analysis.md 生成 |
| workflow_states 10步启用 | ✅ 完成 | 1866个skill迁移, 10644条记录添加, 总计11625条 |
| 文件深度清理 | ✅ 完成 | 28临时+14归档+4冗余脚本+pycache 清理完成 |
| 清理后验证 | ✅ 完成 | L1/健康检查/生成流水线/发现机制 4项全部正常 |

### 修复的Bug

| Bug | 根因 | 修复方案 |
|-----|------|---------|
| agent_trial.py L3评分未写入DB | import_trial_result只保存JSON文件,不写scores表 | 添加INSERT INTO scores语句,映射L3评分到表字段 |
| daily-report-writer有大量{{占位符}} | Round 05生成时无fill_remaining_placeholders | 用增强版generate_skill.py重新生成 |

### Phase 4 验收清单

- [x] 3个skill全链路定稿验证通过 (L3 ≥70, 实际90/100)
- [x] 定稿后批量推广策略制定
- [x] workflow_states 10步表启用
- [x] 26+个临时文件删除
- [x] 14+个报告文件归档
- [x] 清理后项目功能正常

### 项目总体进度

| Phase | 内容 | 状态 |
|-------|------|------|
| Phase 1 | 验证层 (L1+L2+L3) | ✅ 完成 |
| Phase 2 | 生成层 (模板+流水线) | ✅ 完成 |
| Phase 3 | 运维层 (健康检查+定时任务) | ✅ 完成 |
| Phase 4 | 定稿与清理 | ✅ 完成 |
| Phase 5 | 批量推广与持续优化 | ⏳ 待执行 (Round 09) |
