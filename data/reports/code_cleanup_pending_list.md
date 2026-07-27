# 代码清理待处理清单

**生成时间**：2026-07-27
**生成原因**：Phase 1 代码冗余扫描
**扫描范围**：`d:\skills\tools\` 目录全部 Python 脚本（~90 个）
**方法论**：architecture skill（Deletion Test、Seam 分析）+ Grep 引用验证

> **重要**：本清单仅记录发现的问题和建议，**未删除任何文件**。用户审阅后决定实际处理。

---

## 一、死代码/桩代码（13 个，建议删除/归档）

以下脚本经 Grep 验证，**均未被任何其他脚本 import 导入**，且存在硬编码、模块级副作用、Bug 或桩代码问题。

| 序号 | 文件路径 | 问题类型 | 严重度 | 被引用情况 | 建议处理方式 | Deletion Test |
|------|---------|---------|--------|-----------|-------------|--------------|
| 1 | `tools/task6_enhance.py` | 桩代码 | 高 | 无被导入 | 删除 | 删除后复杂度消失，引用未定义 `TOOLS_DIR`，有 BOM |
| 2 | `tools/diagnose_566.py` | 一次性+硬编码+模块级副作用 | 高 | 无被导入 | 删除 | 硬编码 slug `clickhouse-olap-expert`，第13行 `cookies = load_cookies()` 模块级执行 |
| 3 | `tools/verify_skill.py` | 一次性+硬编码+模块级副作用 | 高 | 无被导入 | 删除 | 硬编码 slug `ad-creative-intel-free`，第8行 `cookies = load_cookies()`，`time.sleep(2)`，无 `__main__` |
| 4 | `tools/check_status.py` | 模块级副作用 | 高 | 无被导入 | 删除或修复 | 第10行 `cookies = load_cookies()` 导入即执行网络请求，无 `__main__` 守卫 |
| 5 | `tools/check_progress.py` | 一次性 | 中 | 无被导入 | 删除 | 仅 11 行，读特定 JSON 文件打印 success/failed，无 `__main__` |
| 6 | `tools/check_coverage.py` | 被取代+模块级副作用 | 中 | 无被导入 | 删除 | 已被 `check_coverage_fast.py` 取代，模块级 cookies |
| 7 | `tools/compare_clawhub_local.py` | Bug+模块级副作用 | 高 | 无被导入 | 删除或修复 | 第14行模块级 `open()`，引用未导入的 `DATA_DIR`（Bug），导入的是 `TOOLS_DIR, PACKAGED_SKILLS_DIR, DIFFERENTIATED_DIR` |
| 8 | `tools/batch_delete_clawhub.py` | 一次性+副作用 | 高 | 无被导入 | 删除 | 模块级 `open()` 读删除清单，无 `__main__` 守卫，一次性批量删除 |
| 9 | `tools/test_api_endpoints.py` | 一次性+模块级副作用 | 高 | 无被导入 | 删除 | 第16行 `cookies = load_cookies()`，API 端点测试，无 `__main__`，一次性 |
| 10 | `tools/test_fixes.py` | 位置错误 | 低 | 无被导入 | 移动到 `tests/` | 单元测试（U-09 回归），应在 `tests/` 而非 `tools/` |
| 11 | `tools/github_repo_strategy.py` | 位置错误+重复 | 中 | 无被导入 | 移动到 `config/` 并合并 | 纯策略配置（无执行逻辑），与 `version_sync_pipeline.py` 内联 GitHub 配置重复 |
| 12 | `tools/clean_naming.py` | 待确认 | 低 | 无被导入 | 待用户确认 | 独立 CLI，无被导入，功能较窄 |
| 13 | `tools/template_cleanup.py` | 待确认 | 低 | 无被导入 | 待用户确认 | 独立 CLI，无被导入，功能较窄 |

**Grep 验证命令**：
```
# 确认以上脚本均未被导入
grep -r "import (diff_batch_fix|diagnose_566|verify_skill|check_progress|task6_enhance|test_api_endpoints|batch_delete_clawhub)" tools/
# 结果：No matches found ✅
```

---

## 二、冗余/可合并脚本（~30 个，建议合并/归档）

### 2.1 三编排器并存（最高优先级合并）

| 脚本 | 被引用情况 | 功能 | 建议 |
|------|-----------|------|------|
| `tools/orchestrator.py` | 无被 import（可能通过 subprocess 调用） | 早期编排器 | 归档，功能已被 daily_sync 取代 |
| `tools/daily_sync.py` | 被 subprocess 调用 | **每日同步 v3.0（最完整）** | **保留作为唯一主入口** |
| `tools/ops闭环.py` | 无被 import，无被 subprocess 调用 | health_check+quality_dashboard+annotate 小循环 | 归档，功能可并入 daily_sync |

**Deletion Test**：删除 `orchestrator.py` 和 `ops闭环.py` 后，`daily_sync.py` (v3.0) 已覆盖 discover→audit→banned→github→clawhub→ratings→report 全流程，复杂度不会增加。

### 2.2 三仪表盘分散

| 脚本 | 被引用情况 | 功能 | 建议 |
|------|-----------|------|------|
| `tools/dashboard_server.py` | 被 `fix_marketing.py` 导入（`get_marketing_stats`） | Web 服务 | 保留，但评估 `get_marketing_stats` 是否可独立 |
| `tools/platform_dashboard.py` | 无被导入 | 三平台发布看板（读 upload_tracking.json） | 归档或合并 |
| `tools/quality_dashboard.py` | 无被导入 | 5 维质量看板 | 归档或合并 |

### 2.3 历史修复脚本残留（5 个，全部无被导入）

| 脚本 | 被引用情况 | 建议 |
|------|-----------|------|
| `tools/diff_batch_fix.py` | 无被导入 | 归档（L3 修复第1轮） |
| `tools/diff_batch_fix2.py` | 无被导入 | 归档（L3 修复第2轮） |
| `tools/diff_batch_fix3.py` | 无被导入 | 归档（L3 修复第3轮） |
| `tools/diff_l4_batch_fix.py` | 无被导入 | 归档（L4 修复） |
| `tools/l3_batch_fix.py` | 无被导入 | 归档（与 diff_* 系列重复） |
| `tools/l4_batch_fix.py` | 无被导入 | 归档（与 diff_l4_* 重复） |

### 2.4 版本化重复

| 脚本 | 被引用情况 | 建议 |
|------|-----------|------|
| `tools/skill_batch_upgrader_v2.py` | 被 `skill_batch_upgrader_v3.py` 导入 | 合并到 v3，删除 v2 |
| `tools/skill_batch_upgrader_v3.py` | 独立 CLI | 保留（合并 v2 后） |
| `tools/hermes_converter.py` | 无被导入 | 归档（Round 34，单个转换） |
| `tools/hermes_batch_convert.py` | 无被导入 | 保留（批量版本，功能更全） |

### 2.5 状态检查碎片化

| 脚本 | 被引用情况 | 建议 |
|------|-----------|------|
| `tools/check_status.py` | 无被导入 | 删除（模块级副作用，见第一节） |
| `tools/check_progress.py` | 无被导入 | 删除（一次性，见第一节） |
| `tools/analyze_status.py` | 待确认 | 评估是否可合并到 `health_check.py` |
| `tools/health_check.py` | 被 daily_sync 调用 | 保留作为统一状态检查入口 |

### 2.6 修复脚本碎片化

| 脚本 | 被引用情况 | 建议 |
|------|-----------|------|
| `tools/batch_field_fix.py` | 无被导入 | 归档或合并 |
| `tools/fix_missing_fields.py` | 无被导入 | 归档或合并 |
| `tools/fix_marketing.py` | 导入 `dashboard_server` | 评估是否可合并到 `quality_gate.py` |
| `tools/batch_optimize_description.py` | 无被导入 | 归档或合并 |

### 2.7 评分系统分裂

| 脚本 | 被引用情况 | 功能 | 建议 |
|------|-----------|------|------|
| `tools/trace_llm_scorer.py` | 被 `agent_trial`/`batch_l2_eval`/`llm_validator`/`dependency_verifier`/`batch_l3_trial` 导入 | TRACE 评分（L2 用） | 保留（L2 层使用） |
| `tools/local_quality_scorer.py` | 被 `quality_gate` 导入 | 5 维 LLM 评分（本地评分器） | 保留（本地评分用） |

**结论**：两套评分系统**职责不同**（TRACE 用于 L2 能力验证，local_quality_scorer 用于本地质量评分），不建议合并，但建议在文档中明确分工。

### 2.8 重叠系统

| 脚本 | 被引用情况 | 重叠对象 | 建议 |
|------|-----------|---------|------|
| `tools/automated_review_system.py` | 无被导入 | `upload_gate`(pre-check) + `version_sync_pipeline`(status/sync-log) + `platform_ops`(status) | 归档，功能已被三个核心模块覆盖 |

### 2.9 去重分散

| 脚本 | 被引用情况 | 建议 |
|------|-----------|------|
| `tools/deduplicate_all_v36.py` | 无被导入 | 归档（v36 去重，已过期） |
| `tools/deduplicate_blocks.py` | 无被导入 | 评估是否仍有用 |

### 2.10 升级检查重复

| 脚本 | 被引用情况 | 建议 |
|------|-----------|------|
| `tools/upgrade_checker.py` | 无被导入 | 评估合并到 `update_mechanism.py` |
| `tools/update_mechanism.py` | 待确认 | 保留（如果功能更完整） |

---

## 三、模块级副作用（4 个确认 + 1 个 Bug，建议修复为延迟加载）

以下脚本在模块顶层（非函数内）执行副作用代码，导入即触发网络请求或文件读取，是危险反模式。

| 序号 | 文件路径 | 行号 | 副作用代码 | 严重度 | 建议处理方式 |
|------|---------|------|-----------|--------|------------|
| 1 | `tools/check_status.py` | 10 | `cookies = load_cookies()` | 高 | 删除（死代码）或移入函数内 |
| 2 | `tools/diagnose_566.py` | 13 | `cookies = load_cookies()` | 高 | 删除（死代码）或移入函数内 |
| 3 | `tools/test_api_endpoints.py` | 16 | `cookies = load_cookies()` | 高 | 删除（死代码）或移入函数内 |
| 4 | `tools/verify_skill.py` | 8 | `cookies = load_cookies()` | 高 | 删除（死代码）或移入函数内 |
| 5 | `tools/compare_clawhub_local.py` | 14 | `with open(str(DATA_DIR / "clawhub_published_slugs.json"), ...) as f:` | 高 | 删除（死代码+Bug）或修复 DATA_DIR 引用并移入函数 |

**Grep 验证命令**：
```
grep -n "^cookies\s*=" tools/*.py
# 结果：4 个文件，均在模块顶层执行 cookies 加载
```

---

## 四、碎片化功能（建议整合）

以下功能分散在多个脚本中，建议整合为统一模块。

### 4.1 状态检查整合

当前有 4 个状态检查脚本（`check_status`/`check_progress`/`analyze_status`/`health_check`），且 `orchestrator`/`version_sync`/`platform_ops` 各自还有 `status` 子命令。

**建议**：统一到 `health_check.py` 作为唯一状态检查入口，其他脚本通过 `--status` 参数委托。

### 4.2 字段修复整合

当前有 4 个字段修复脚本（`batch_field_fix`/`fix_missing_fields`/`fix_marketing`/`batch_optimize_description`），功能分散。

**建议**：整合到 `quality_gate.py` 的 `--fix` 参数，按字段类型自动选择修复策略。

### 4.3 编排器整合

当前有 3 个编排器（`orchestrator`/`daily_sync`/`ops闭环`），功能重叠。

**建议**：统一到 `daily_sync.py` (v3.0) 作为唯一主入口。

### 4.4 仪表盘整合

当前有 3 个仪表盘（`dashboard_server`/`platform_dashboard`/`quality_dashboard`），报告/看板功能分散。

**建议**：合并为统一看板模块，`dashboard_server.py` 作为 Web 服务入口。

---

## 五、汇总统计

| 类别 | 数量 | 严重度分布 | 建议处理 |
|------|------|-----------|---------|
| 死代码/桩代码 | 13 | 高8/中3/低2 | 10个删除/归档，2个移动，1个待确认 |
| 冗余/可合并 | ~30 | 高10/中15/低5 | 合并/归档 |
| 模块级副作用 | 5 | 高5 | 删除（与死代码重叠）或修复 |
| 碎片化功能 | 4组 | 中 | 整合 |
| **总计** | **~48 个问题** | | |

---

## 六、核心脚本清单（23 个，保留）

以下脚本为核心功能，**必须保留**：

### 基础设施层
- `config.py`（中央配置，被~30脚本导入）
- `db.py`（数据库层，被15+脚本导入）
- `skill_core/`（parser/checks/rules/db，统一SKILL.md解析层）

### 流水线编排层
- `daily_sync.py`（每日同步v3.0，最完整主入口）
- `version_sync_pipeline.py`（版本同步流水线）
- `platform_ops.py`（平台运维v4.0）
- `quality_gate.py`（质量门禁v2.2）
- `upload_gate.py`（上传门控v2.2）
- `deep_quality_audit.py`（L1-L8全量审计）

### 分层检查器
- `l2_capability_checker.py`、`l3_function_checker.py`、`l4_task_gate.py`
- `source_fidelity_checker.py`

### 评分与试验
- `trace_llm_scorer.py`（TRACE评分，L2用）
- `local_quality_scorer.py`（5维LLM评分，本地评分用）
- `llm_validator.py`、`agent_trial.py`

### 平台与上传
- `enterprise_uploader.py`、`clawhub_batch_uploader.py`
- `auto_discover.py`、`market_monitor.py`
- `generate_skill.py`、`check_debranding.py`
- `pricing_engine.py`、`auto_differentiate.py`

### 其他核心
- `init_baseline.py`（基线初始化）

---

## 七、处理优先级建议

1. **P0（立即）**：删除13个死代码/桩代码脚本（均无被导入，无风险）
2. **P1（高）**：修复5个模块级副作用脚本（如不删除则修复为延迟加载）
3. **P2（中）**：归档6个历史修复脚本（diff_batch_fix系列+l3/l4_batch_fix）
4. **P3（中）**：合并3个编排器为1个（daily_sync.py）
5. **P4（低）**：整合状态检查、字段修复、仪表盘等碎片化功能
6. **P5（低）**：评估评分系统分工、去重逻辑合并等

> **注意**：以上所有建议均需用户审阅后执行。本清单仅记录发现，未做任何修改。
