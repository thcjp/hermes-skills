# 文档清理待处理清单

**生成时间**：2026-07-28
**生成原因**：Phase 2 文档清理扫描
**扫描范围**：`d:\skills` 项目全部文档文件（.md, .html, .txt）
**方法论**：逐一阅读分析，按状态分类

> **重要**：本清单仅记录发现的问题和建议，**未删除任何文件**。用户审阅后决定实际处理。

---

## 一、汇总统计

| 状态 | 文件数 | 建议处理 |
|------|--------|---------|
| **有效** | ~30个 | 保留 |
| **过期** | ~100个 | 归档（~75个）或删除（~25个） |
| **重复** | ~15个 | 删除被取代版本，保留较新版本 |
| **已归档** | ~56个 | 保留（docs/plans/archive/中的round计划） |

---

## 二、建议删除的文档（25个，一次性/无价值/被取代）

### 2.1 .trae/documents/ 目录（12个删除）

| 序号 | 文件路径 | 状态 | 理由 |
|------|---------|------|------|
| 1 | `.trae/documents/round1-7-comprehensive-review.md` | 重复/过期 | v1版本（76.7%），已被v2取代 |
| 2 | `.trae/documents/round5-implementation-plan.md` | 过期 | 已完成 |
| 3 | `.trae/documents/round5-review-and-prompt.md` | 过期 | 已完成 |
| 4 | `.trae/documents/round6-cleanup-e2e-test-v4-plan.md` | 重复/过期 | 三份round6文档重叠 |
| 5 | `.trae/documents/round6-cleanup-e2e-v4-implementation-plan.md` | 重复/过期 | 三份round6文档重叠 |
| 6 | `.trae/documents/round6-cleanup-e2e-v4-master-plan.md` | 重复/过期 | 三份round6文档重叠 |
| 7 | `.trae/documents/round6-prompt.md` | 过期 | 已完成 |
| 8 | `.trae/documents/round7-prompt.md` | 过期 | 已完成 |
| 9 | `.trae/documents/skill-automation-comprehensive-fix-plan-v3.md` | 过期 | 已被v4取代 |
| 10 | `.trae/documents/skillhub-12-factor-deep-review-and-fix-plan.md` | 重复/过期 | 与visibility-fix重叠 |
| 11 | `.trae/documents/skillhub-visibility-fix-and-v57-implementation.md` | 过期 | 已完成，当前v76 |
| 12 | `.trae/documents/v58-execution-plan.md` | 过期 | 已完成，当前v76 |

### 2.2 .trae/documents/archive/ 目录（4个删除）

| 序号 | 文件路径 | 状态 | 理由 |
|------|---------|------|------|
| 13 | `.trae/documents/archive/P0-pipeline-breakage-fix-plan.md` | 过期 | round1已完成 |
| 14 | `.trae/documents/archive/round5-prompt-and-review.md` | 过期 | 已完成 |
| 15 | `.trae/documents/archive/skill-automation-comprehensive-audit-and-fix-plan.md` | 过期 | v1，已被v2-v4取代 |
| 16 | `.trae/documents/archive/skill-automation-comprehensive-fix-plan-v2.md` | 过期 | v2，已被v3-v4取代 |

### 2.3 docs/reports/ 目录（5个删除）

| 序号 | 文件路径 | 状态 | 理由 |
|------|---------|------|------|
| 17 | `docs/reports/update-report.md` | 过期 | 一次性快照（0变更），无价值 |
| 18 | `docs/reports/debranding-report.md` | 重复 | data/reports有更新版本（180文件） |
| 19 | `docs/plans/integration-test-report-v4.md` | 过期 | 已被v5/v6取代 |
| 20 | `docs/plans/integration-test-report-v5.md` | 过期 | 已被v6取代 |
| 21 | `docs/plans/integration-test-report-v6.md` | 过期 | data/reports有v69更新版本 |

### 2.4 data/reports/ 目录（6个删除）

| 序号 | 文件路径 | 状态 | 理由 |
|------|---------|------|------|
| 22 | `data/reports/scan_all_log.txt` | 过期 | 一次性扫描日志 |
| 23 | `data/reports/full_l7_audit_log.txt` | 过期 | 一次性L7审计日志 |
| 24 | `data/reports/full_l7b_audit_log.txt` | 过期 | 一次性L7b审计日志 |
| 25 | `data/reports/full_l7b_audit_log_postfix.txt` | 过期 | 一次性L7b修复后日志 |
| 26 | `data/reports/deleted_skills_round24.txt` | 过期 | round24删除列表，一次性 |
| 27 | `data/reports/differentiated_verification_log.txt` | 过期 | 差异化验证日志，一次性 |

### 2.5 archive/ 目录（1个删除）

| 序号 | 文件路径 | 状态 | 理由 |
|------|---------|------|------|
| 28 | `archive/skill_test_report.md` | 重复 | 与skill_case_test_report.md重叠 |

---

## 三、建议归档的文档（~75个，移至archive目录）

### 3.1 根目录散落文档（4个归档至archive/）

| 序号 | 文件路径 | 目标位置 | 理由 |
|------|---------|---------|------|
| 1 | `fix_verification_report.md` | `archive/` | 一次性验证报告 |
| 2 | `skill-registry-审计报告.md` | `archive/` | 一次性审计快照 |
| 3 | `skillhub_publish_flow_review.md` | `archive/` | 重复+过期 |
| 4 | `skillhub_publish_flow_analysis.md` | `archive/` | 重复+过期 |

### 3.2 .trae/documents/ 主目录（3个归档至.trae/documents/archive/）

| 序号 | 文件路径 | 目标位置 | 理由 |
|------|---------|---------|------|
| 5 | `.trae/documents/project-cleanup-quality-governance-plan.md` | `.trae/documents/archive/` | 一次性清理计划 |
| 6 | `.trae/documents/round1-7-comprehensive-review-v2.md` | `.trae/documents/archive/` | 历史快照 |
| 7 | `.trae/documents/skill-automation-comprehensive-fix-plan-v4.md` | `.trae/documents/archive/` | v4计划最终状态 |

### 3.3 docs/plans/ next-round-prompt系列（36个归档至docs/plans/archive/）

v40.0-v75.0（缺v60/v62），共36个文件，全部为已完成的历史任务提示词。

| 序号 | 文件路径范围 | 目标位置 | 理由 |
|------|------------|---------|------|
| 8-43 | `docs/plans/next-round-prompt-v40.0.md` ~ `v75.0.md` | `docs/plans/archive/` | 历史任务提示词，v76为最新 |

### 3.4 docs/plans/ 其他计划文档（3个归档）

| 序号 | 文件路径 | 目标位置 | 理由 |
|------|---------|---------|------|
| 44 | `docs/plans/new-conversation-first-prompt.md` | `docs/plans/archive/` | v62已完成 |
| 45 | `docs/plans/new-conversation-starter-design.md` | `docs/plans/archive/` | 截至V64，已过时 |
| 46 | `docs/plans/new-conversation-task-list.md` | `docs/plans/archive/` | 已完成 |

### 3.5 docs/reports/ 审查报告（~20个归档至archive/或docs/reports/archive/）

| 序号 | 文件路径 | 理由 |
|------|---------|------|
| 47 | `docs/reports/QA-review.md` | 第1轮QA审核，历史 |
| 48 | `docs/reports/architecture-review.md` | 第2轮架构审核，历史 |
| 49 | `docs/reports/architecture_review_report.md` | 架构审查，历史 |
| 50 | `docs/reports/PM-review.md` | 第3轮PM审核，历史 |
| 51 | `docs/reports/developer-review.md` | 第4轮开发者审核，历史 |
| 52 | `docs/reports/security-compliance-audit.md` | 第5轮安全合规，历史 |
| 53 | `docs/reports/第2轮_代码质量与安全审查报告.md` | 第2轮代码审查，历史 |
| 54 | `docs/reports/第3轮_开发方法论审查报告.md` | 第3轮方法论，历史 |
| 55 | `docs/reports/第4轮_产品与商业化审查报告.md` | 第4轮产品审查，历史 |
| 56 | `docs/reports/第5轮_最终整合审查报告.md` | 第5轮最终整合，历史 |
| 57 | `docs/reports/COMPREHENSIVE_GOVERNANCE_REPORT.md` | 全面治理报告，历史快照 |
| 58 | `docs/reports/WORKFLOW_INTEGRITY_REPORT.md` | 工作流完整性，历史快照 |
| 59 | `docs/reports/security-analysis-report.md` | 安全审核分析，历史 |
| 60 | `docs/reports/round-13-quality-trend-report.md` | round13质量趋势，已完成 |
| 61 | `docs/reports/round24_platform_review_strategy.md` | round24策略，历史 |
| 62 | `docs/reports/round25_platform_review_strategy.md` | round25策略，历史 |
| 63 | `docs/reports/round25_triple_platform_alignment_report.md` | round25对齐报告，已完成 |
| 64 | `docs/reports/platform_review_followup.md` | 平台审查跟进，已完成 |
| 65 | `docs/reports/quality-analysis-report.md` | 功能质量分析，历史快照 |
| 66 | `docs/reports/skillhub-visibility-root-cause-analysis.md` | 可见性根因，已被v6取代 |
| 67 | `docs/reports/task2_task3_report.md` | Task2&3报告，已完成 |
| 68 | `docs/reports/v68-task-execution-report.md` | v68执行报告，已完成 |

### 3.6 docs/ 可见性分析HTML（5个归档，v1-v5）

| 序号 | 文件路径 | 理由 |
|------|---------|------|
| 69 | `docs/skillhub-visibility-analysis.html` | v1，已被v6取代 |
| 70 | `docs/skillhub-visibility-optimization-v2.html` | v2，已被v6取代 |
| 71 | `docs/skillhub-audit-visibility-analysis-v3.html` | v3，已被v6取代 |
| 72 | `docs/skillhub-visibility-analysis-v4/skillhub-visibility-analysis-v4.html` | v4，已被v6取代 |
| 73 | `docs/skillhub-visibility-analysis-v5/skillhub-visibility-analysis-v5.html` | v5，已被v6取代 |

### 3.7 docs/ 其他（1个归档）

| 序号 | 文件路径 | 理由 |
|------|---------|------|
| 74 | `docs/enhancement-plan.md` | Free→Paid增强计划，已被取代 |

### 3.8 data/reports/（1个归档）

| 序号 | 文件路径 | 理由 |
|------|---------|------|
| 75 | `data/reports/integration-test-report-v69.md` | v69集成测试报告，已完成 |

---

## 四、保留的有效文档（~30个）

### 规范类（长期有效）
- `docs/ARCHITECTURE.md` - 唯一权威架构文档
- `docs/NAMING_CONVENTION.md` - 命名规范
- `docs/FRAMEWORK_ADR.md` - 架构决策记录
- `docs/SKILL_QUALITY_STANDARD.md` - 质量标准v3.0
- `docs/deep-differentiation-methodology.md` - 差异化方法论
- `docs/version-sync-pipeline.md` - 版本同步流水线
- `docs/skillhub-security-avoidance-guide.md` - 安全审核规避指南
- `PROJECT_MEMORY.md` - 项目记忆文档
- `README.md` - 项目说明
- `docs/specs/2026-07-24-architecture-governance-design.md` - 架构治理设计
- `docs/specs/2026-07-27-quality-governance-finance-skills-design.md` - 质量治理设计
- `tools/templates/README.md` + 5个模板文件

### 当前活跃计划
- `docs/plans/next-round-prompt-v76.0.md` - 最新任务提示词
- `docs/plans/implementation-plan-v1.0.md` - 当前实施计划
- `docs/plans/task-list-v1.0.md` - 当前任务清单

### 当前活跃报告
- `SkillHub平台规则与账号封禁申诉研究报告.md`
- `data/reports/skillhub_account_ban_analysis_and_unban_strategy.md`
- `data/reports/banned_skills_root_cause_analysis.md`
- `data/reports/code_cleanup_pending_list.md`
- `data/reports/doc_cleanup_pending_list.md`（本文件）
- `docs/skillhub-visibility-analysis-v6.html` - 最新可见性分析

### 已归档保留（docs/plans/archive/中round-01~round-43计划）
- ~56个历史轮次计划，记录项目完整演进历史，保留不处理

---

## 五、重复文档清单（4组确认重复）

1. **架构审查**：`architecture-review.md`（第2轮，65分）vs `architecture_review_report.md`（2026-07-20，不同范围）
2. **安全审查**：`security-analysis-report.md`（29个skill拒绝）vs `security-compliance-audit.md`（第5轮终审63分）
3. **平台审查策略**：`round24_platform_review_strategy.md` vs `round25_platform_review_strategy.md`
4. **去标识报告**：`docs/reports/debranding-report.md`（71文件）vs `data/reports/debranding-report.md`（180文件，后者更新）

---

## 六、处理优先级建议

1. **P0（立即）**：删除28个一次性/无价值文档（日志文件、被取代版本）
2. **P1（高）**：归档75个过期文档至对应archive目录
3. **P2（中）**：处理4组重复文档（删除旧版本，保留新版本）
4. **P3（低）**：评估docs/plans/archive/中56个round计划是否需要进一步精简

> **注意**：以上所有建议均需用户审阅后执行。本清单仅记录发现，未做任何修改。
