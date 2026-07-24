# Round 08: 定稿与全面升级 + 文件深度清理 (Phase 4 + Section 5)

> **前置条件**: Round 07 已完成（运维层补全：health_check.py + cron 定时任务 + 文档冲突解决）
> **设计文档**: `D:\skills\docs\plans\2026-07-20-skill-automation-v2-design.md` 第4节 + 第5节
> **预估时间**: 45-60 分钟
> **验收标准**: 3个skill全链路L3验证通过 + 文件清理完成 + 项目功能正常

---

## 背景与目标

Phase 1（验证层）、Phase 2（生成层）、Phase 3（运维层）已全部完成：
- L1/L2/L3 三层验证体系就绪
- 5种设计模式模板 + generate_skill.py 生成流水线就绪
- health_check.py 健康检查 + 3个cron定时任务就绪
- 文档冲突已解决

Phase 4 是最后的定稿与全面升级阶段，同时执行文件深度清理：
1. **定稿验证**: 对3个已通过L1+L2的skill执行L3真实agent试运行
2. **批量推广策略**: 基于定稿结果制定批量推广计划
3. **10步工作流启用**: 将workflow_states从2步扩展到10步
4. **文件深度清理**: 删除26个临时文件 + 归档14个报告 + 清理冗余脚本

---

## 任务清单

### Step 4.1: 3个skill全链路定稿验证 (L3)

**目标**: 对3个已通过L1+L2的skill执行L3真实agent试运行

**3个定稿候选skill**:

| Skill | 模板 | L1 | L2 | L3状态 |
|-------|------|-----|-----|--------|
| daily-report-writer | Generator | 10/10 | 47/50 (A级) | 待执行 |
| code-quality | Reviewer | 10/10 | 38/50 (B级) | 待执行 |
| auto-workflow | Pipeline | 10/10 | 35/50 (B级) | 待执行 |

**执行步骤** (每个skill):

1. 生成L3试运行prompt:
   ```bash
   cd D:\skills\skill-registry
   python agent_trial.py trial daily-report-writer --json -o l3_trial_daily-report-writer.json
   python agent_trial.py trial code-quality --json -o l3_trial_code-quality.json
   python agent_trial.py trial auto-workflow --json -o l3_trial_auto-workflow.json
   ```

2. AI agent 读取生成的prompt，模拟真实用户场景执行skill:
   - 模拟用户输入典型请求
   - 检查skill是否被正确触发
   - 评估输出质量和可用性
   - 记录执行日志和结果

3. 将AI试运行结果导入DB:
   ```bash
   python agent_trial.py import daily-report-writer l3_result_daily-report-writer.json
   python agent_trial.py import code-quality l3_result_code-quality.json
   python agent_trial.py import auto-workflow l3_result_auto-workflow.json
   ```

**L3评估标准**:
- 触发成功率: 3/3个测试用例正确触发
- 输出可用性: 输出能解决用户问题
- 依赖可达性: 所有依赖可用
- 综合评分: ≥70/100 通过

**验收标准**:
- [ ] 3个skill的L3试运行prompt全部生成
- [ ] 3个skill的L3试运行结果全部导入DB
- [ ] 3个skill的L3综合评分 ≥70
- [ ] 定稿验证报告生成

---

### Step 4.2: 定稿后批量推广策略

**目标**: 基于定稿验证结果，制定批量推广计划

**分析内容**:

1. **定稿质量分析**:
   - 3个skill的L1+L2+L3综合评分对比
   - 5种模板的适用性评估（Generator/Reviewer/Pipeline已验证，Tool Wrapper/Inversion待验证）
   - 生成流水线的瓶颈和优化点

2. **批量推广计划**:
   - 从DB中筛选待推广skill（workflow_state = step7_validate 或 step5_add_deps）
   - 按优先级排序：P0(8个零依赖) → P1(5个获奖) → P2(3个获奖) → P3(12个变现) → P4+P5(32个开源改造)
   - 估算推广工作量：每个skill约2分钟（generate_skill.py + L1 + dep + L2）

3. **推广执行策略**:
   - 批量生成: `python generate_skill.py batch --category Productivity --limit 10`
   - 批量验证: 逐个运行L1+L2，记录通过率
   - 批量上传: 通过 `update_mechanism.py sync` 上传到平台

**验收标准**:
- [ ] 定稿质量分析报告生成
- [ ] 批量推广计划文档生成（含优先级排序和工作量估算）
- [ ] 推广执行策略明确

---

### Step 4.3: 启用workflow_states 10步表

**目标**: 将workflow_states从当前2步（step7_validate + step8_upload_free）扩展到完整10步

**10步工作流定义**:

| 步骤 | step_name | 说明 | 当前状态 |
|------|-----------|------|---------|
| 1 | read_original | 读取原始SKILL.md | 有记录(step1_read_original 18条) |
| 2 | parse_metadata | 解析frontmatter | 无记录 |
| 3 | analyze_content | 分析核心能力 | 无记录 |
| 4 | select_template | 选择设计模式模板 | 无记录 |
| 5 | add_deps | 添加依赖说明 | 有记录(step5_add_deps 807条) |
| 6 | generate_skill | 生成新SKILL.md | 无记录 |
| 7 | validate | L1+L2验证 | 有记录(validate 879条) |
| 8 | upload_free | 上传免费版 | 有记录(upload_free 102条) |
| 9 | upload_paid | 上传付费版 | 无记录 |
| 10 | completed | 完成定稿 | 有记录(completed 61条) |

**执行步骤**:

1. 编写 `workflow_migrator.py` 脚本:
   - 为每个active skill补全缺失的workflow_states记录
   - 根据当前workflow_state推断已完成的步骤
   - 例如: workflow_state=step7_validate → 补全step1-7的记录

2. 更新 `update_mechanism.py` 的 `sync_skill_to_platform()`:
   - 在每个步骤执行后写入workflow_states记录
   - 支持步骤回退和重试

3. 验证迁移结果:
   ```bash
   python workflow_migrator.py --dry-run  # 预览
   python workflow_migrator.py migrate    # 执行迁移
   python workflow_migrator.py verify     # 验证结果
   ```

**验收标准**:
- [ ] workflow_migrator.py 脚本创建完成
- [ ] dry-run 预览结果正确
- [ ] 迁移后workflow_states覆盖10个步骤
- [ ] verify 验证通过

---

### Step 5: 文件深度清理

**目标**: 清理项目中的临时文件、过期报告、冗余脚本

#### A. 删除临时文件 (26个)

**文件列表** (位于 `D:\skills\` 根目录):
```
.api-probe.sh, .api-probe.txt, .api-probe2.sh, .api-probe2.txt,
.api-probe3.sh, .api-probe3.txt, .api-probe4.sh, .api-probe4.txt,
.api-probe5.sh, .api-probe5.txt, .api-probe6.sh, .api-probe6.txt,
.inspect.sh, .inspect2.sh, .dryrun.txt, .dryrun-both.sh, .dryrun-both.txt,
.cli-src.py, .cli-info.txt, .auth-help.txt, .config-help.txt,
.login-help.txt, .pub-help.txt, .publish-free.sh, .publish-free.txt,
retry-results.txt, upload-results.txt
```

**执行**: 使用 DeleteFile 工具批量删除

#### B. 归档报告文件 (14个)

**归档到** `D:\skills\archive\`:
```
round2_displayname_anomalies.csv → archive/round2/
round2_duplicate_analysis_report.md → archive/round2/
round2_duplicate_groups.csv → archive/round2/
round3_cross_validation_report.md → archive/round3/
round4_verify_cleanup_report.md → archive/round4/
round5_final_validation_report.md → archive/round5/
LLM类Skill案例展示审核报告.md → archive/
SKILL-规范性分析报告.md → archive/
SKILLHUB_质量差距分析报告.md → archive/
TRACE评估与增强报告.md → archive/
skill_case_test_report.md → archive/
skill_test_report.md → archive/
差异化改造质量分析报告.md → archive/
WORKFLOW_STATE_MACHINE_FIX.md → archive/
```

**执行**:
1. 创建 `D:\skills\archive\` 及子目录
2. 移动文件到对应目录

#### C. 评估后删除冗余脚本

| 文件 | 位置 | 处理 |
|------|------|------|
| `skill_batch_upgrader_v2.py` | skill-registry/ | 删除(v3已取代) |
| `batch12_mapping.txt` | skill-registry/ | 删除 |
| `batch12_mapping_full.txt` | skill-registry/ | 删除 |
| `batch12_pending_list.txt` | skill-registry/ | 删除 |
| `__pycache__/` | skill-registry/ | 删除(自动重建) |
| `__pycache__/` | skill-registry/skill_core/ | 删除(自动重建) |
| `skillhub-*-analysis.html` (4个) | D:\skills\ | 归档到archive/ |
| `.skillhub-bin.txt` | D:\skills\ | 删除 |
| `run-skillhub.sh` | D:\skills\ | 评估后保留(可能有用) |

#### D. 清理验证

清理完成后运行以下命令确认项目功能正常:
```bash
cd D:\skills\skill-registry
python quality_gate.py --help                    # L1检查器正常
python auto_discover.py scan --source clawhub --limit 1  # 发现机制正常
python health_check.py --section db              # 健康检查正常
python generate_skill.py auto-select daily-report-writer  # 生成流水线正常
```

**验收标准**:
- [ ] 26个临时文件已删除
- [ ] 14个报告文件已归档
- [ ] 冗余脚本已删除/归档
- [ ] __pycache__ 已清理
- [ ] 清理后4个验证命令全部通过

---

## 执行顺序

1. **Step 4.1** → 3个skill L3定稿验证（15-20 分钟）
2. **Step 4.2** → 定稿质量分析 + 批量推广策略（10-15 分钟）
3. **Step 4.3** → 启用10步workflow_states（10-15 分钟）
4. **Step 5** → 文件深度清理（10-15 分钟）
5. **汇总** → 生成最终验证报告，确认全部验收标准
6. **项目完成** → Skill 自动化系统 v2 全部 4 个 Phase 完成

---

## Round 07 完成总结

### 已完成成果

| 项目 | 状态 | 详情 |
|------|------|------|
| health_check.py | ✅ 完成 | DB+文件+平台三维度健康检查，整体状态 healthy |
| 3个cron定时任务 | ✅ 完成 | 每日来源更新 + 每周治理扫描 + 每周健康检查 |
| 文档冲突解决 | ✅ 完成 | deep-differentiation-methodology.md 移入skill-registry/，-pro矛盾已修正 |

### health_check.py 首次运行结果

| 维度 | 指标 | 结果 |
|------|------|------|
| DB | workflow_state覆盖率 | 100.0% |
| DB | 孤儿记录 | 0 |
| DB | 重复slug | 0 |
| DB | TRACE评分覆盖率 | 100.0% (1866个已评分) |
| 文件 | 抽样数 | 50 |
| 文件 | 有效路径 | 50/50 |
| 文件 | SKILL.md存在 | 50/50 |
| 文件 | 行数合规 | 50/50 |
| 文件 | frontmatter完整 | 50/50 |
| 平台 | 上传成功率 | 91.3% (188/206) |
| 平台 | 待审核 | 23个 |
| 平台 | 付费分布 | 59付费 / 1免费 / 1806未指定 |
| **整体状态** | | **✓ healthy** |

### 3个定时任务

| 任务名 | 频率 | 下次执行 | ID |
|--------|------|---------|-----|
| skill-source-update | 每日 09:00 | 2026-07-21 09:00 | 74caff5b |
| skill-governance-scan | 每周一 10:00 | 2026-07-27 10:00 | 214dafe3 |
| skill-health-check | 每周一 11:00 | 2026-07-27 11:00 | dba2b4fd |

### 文档冲突修复

- **文件移动**: `D:\skills\deep-differentiation-methodology.md` → `D:\skills\skill-registry\deep-differentiation-methodology.md`
- **矛盾修正**: 第57行从 "`[原意]-pro` 或 `[新概念]`" 改为 "`[功能化新概念]`，不使用 -pro/-free 后缀"
- **交叉引用**: 新增 "付费版与免费版的命名规则参见 `NAMING_CONVENTION.md` 第2.1节"

---

## Phase 3 验收清单

- [x] health_check.py输出健康报告
- [x] 定时任务创建并激活
- [x] 文档冲突解决

## Phase 4 验收清单（待完成）

- [ ] 3个skill全链路定稿验证通过 (L3 ≥70)
- [ ] 定稿后批量推广策略制定
- [ ] workflow_states 10步表启用
- [ ] 26个临时文件删除
- [ ] 14个报告文件归档
- [ ] 清理后项目功能正常
