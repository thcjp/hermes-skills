# 项目清理与质量治理执行计划

## 一、摘要 (Summary)

本计划对 `d:\skills` 项目（Skill 收集-增强-分发平台）执行 6 个阶段的清理与质量治理。项目当前有 90 个 Python 脚本、3996 个 SKILL.md 文件，93.4% 的已上传 skill 被封禁（1378/1476）。核心目标：清理冗余代码与文档（存入待处理清单不删除）→ 验证管道完整性与防封有效性 → 确保所有收费/免费 skill 质量评分 >4.5 分且不会被第三方系统再次封禁 → 交叉迭代直至稳健。

**执行约束**：用户睡眠期间自主执行，无需人工确认。如 Git 备份失败，跳过 Phase 1/2，直接执行 Phase 3/4/5。

## 二、当前状态分析 (Current State Analysis)

### 2.1 代码状态
- **90 个 Python 脚本**：23 个核心、~30 个冗余/可合并、13 个死代码/桩代码
- **三编排器并存**：`orchestrator.py`、`daily_sync.py`、`ops闭环.py` 功能重叠，`daily_sync.py` (v3.0) 最完整
- **模块级副作用泛滥**：8 个脚本在导入时执行 `cookies=load_cookies()` 或 `open()`（`check_status.py`、`verify_skill.py`、`diagnose_566.py`、`compare_clawhub_local.py`、`batch_delete_clawhub.py`、`test_api_endpoints.py`、`check_coverage.py`、`check_progress.py`）
- **评分系统分裂**：`trace_llm_scorer.py` (TRACE 评分) 与 `local_quality_scorer.py` (5 维 LLM 评分) 两套并行
- **修复脚本失控**：5 个历史 L3/L4 修复脚本（`diff_batch_fix.py`/`2`/`3`、`diff_l4_batch_fix.py`、`l3_batch_fix.py`、`l4_batch_fix.py`）

### 2.2 文档状态
- **17 个当前有效文档**（根级规范 + specs + plans 主线 + v76）
- **35 个被取代的 next-round-prompt**（v40-v75，v76 为最新）
- **56 个已归档文件**（`docs/plans/archive/` 内 round-01~44 + v34-v39 + 设计文档）
- **5 个旧版可见性分析**（v1-v5，v6 为最新）
- **16 个 `.trae/documents/` 临时文档**（round1-7 + v57/v58 阶段）
- **4 对疑似重复报告**（architecture/security/platform_review/中文审查）

### 2.3 Git 状态
- **68 个未提交更改**
- **最新 commit**: `e6cf1ff13` (v76.0 - 防封机制全面加固)
- **网络状态**: `github.com:443` 可达 ✅
- **远程仓库**: `origin` 和 `hermes-skills` 均指向 `https://github.com/thcjp/hermes-skills.git`（公开引流仓库，无私有备份仓库）

### 2.4 封禁状态与根因
- **1378/1476 (93.4%) synced_from_skillhub 技能被封禁**
- **五大根因**（按贡献度）：
  1. 爆发式上传（2026-07-24 单日 1098 个，同一微秒时间戳）
  2. 近似重复派生内容（-free/-pro/-tool-* 差异化复制，990+ 个）
  3. 程序化 slug 变异（-sk/-sk1/-sk2/-sk3 系列后缀，136 个）
  4. 乐观同步标记放大误判（db.py 凭目录路径假设标记 synced，912 个）
  5. 短/通用 slug 占用（≤8 字符，如 api-free, sql-free，27 个）
- **已建防封措施**：速率限制(30/hour, 100/day, 2min间隔)、内容指纹去重(>85%阻断)、slug变异消除、fail-safe速率限制
- **本地评分器已建但全量扫描未完成**：125/1072 已评分，平均 3.55 分（全部 ≤4.5）

### 2.5 平台状态
| 平台 | 成功 | 封禁/失败 | 待处理 | 阻塞项 |
|------|------|----------|--------|--------|
| SkillHub | 1120 | 563 封禁 | 4 pending | admin token 401 |
| ClawHub | 1401 | 2 cancelled | 971 pending | 认证失效 |
| GitHub | 1640 | - | - | - |
| 评分覆盖 | 2/3495 (0%) | - | - | 需批量同步 |

### 2.6 质量门禁体系现状
完整链路已建成：`L1静态(13项) → L1.5内容(7项) → 营销(7项) → 安全(21项) → 防幻觉(3项) → L2 LLM → L3 Agent → 平台同步`
- 本地评分器：`local_quality_scorer.py`，5 维度（功能完整性/准确性/易用性/安全性/创新性），阈值 4.5
- 集成入口：`quality_gate.py` 的 `run_full_quality_check(include_local_score=True)`
- DB 字段：`local_quality_score`、`local_score_feedback`、`local_score_at`

---

## 三、分阶段执行计划 (Proposed Changes)

### Phase 0: Git 全量备份

**目标**：执行任何危险操作前，全量提交并推送当前代码到远程仓库，建立安全回滚点。

**前置检查**：
```powershell
# 1. 检查网络连通性
Test-NetConnection -ComputerName github.com -Port 443 -InformationLevel Quiet

# 2. 检查当前 git 状态
cd d:\skills
git status --short
git log --oneline -3
```

**执行步骤**：
```powershell
cd d:\skills
# 3. 全量暂存所有更改（包括新增、修改、删除的文件）
git add -A

# 4. 提交备份
git commit -m "backup: 全量备份 - 清理前安全回滚点

- 68 个未提交更改全量提交
- 执行前状态快照
- 后续将执行代码清理、文档清理、管道验证、skill质量检查"

# 5. 推送到远程
git push origin main

# 6. 验证推送成功
git log origin/main --oneline -1
git status
```

**判断逻辑**：
- 推送成功 → `backup_status = "success"` → 继续执行 Phase 1、2
- 推送失败 → `backup_status = "failed"` → 跳过 Phase 1、2，直接执行 Phase 3/4/5
- 记录备份结果到 `d:\skills\data\reports\backup_status.json`

**产出文件**：`d:\skills\data\reports\backup_status.json`
```json
{
  "timestamp": "2026-07-27T...",
  "network_check": "pass/fail",
  "commit_hash": "...",
  "push_status": "success/failed",
  "files_committed": 68,
  "skip_phase_1_2": false
}
```

**验证**：
- `git status` 显示 clean（无未提交更改）
- `git log origin/main -1` 显示备份 commit
- `backup_status.json` 记录成功状态

---

### Phase 1: 代码冗余清理（待处理清单）

**目标**：全量扫描 `tools/` 目录，识别冗余/死代码/桩代码/碎片化功能/模块级副作用，统一存入待处理清单。**不删除任何文件**。

**产出文件**：`d:\skills\data\reports\code_cleanup_pending_list.md`

**使用技能**：architecture skill 方法论（Deletion test、Seam 分析）

**步骤**：

#### 1.1 死代码/桩代码识别（13 个）

逐一检查以下脚本，记录：文件路径、问题类型、严重度、被引用情况、建议处理方式。

| 脚本 | 问题类型 | 严重度 | 详情 |
|------|---------|--------|------|
| `task6_enhance.py` | 桩代码 | 高 | 引用未定义 `TOOLS_DIR`，是修改 `dashboard_server.py` 的代码生成脚本，有 BOM |
| `diagnose_566.py` | 一次性+硬编码 | 高 | 硬编码 slug `clickhouse-olap-expert`，模块级 `cookies=load_cookies()` |
| `verify_skill.py` | 一次性+硬编码 | 高 | 硬编码 slug `ad-creative-intel-free`，模块级 cookies + `time.sleep(2)`，无 `__main__` |
| `check_status.py` | 模块级副作用 | 高 | 模块级 cookies 加载（导入即执行网络请求），无 `__main__` 守卫 |
| `check_progress.py` | 一次性 | 中 | 仅 11 行，读特定 JSON 文件打印 success/failed，无 `__main__` |
| `check_coverage.py` | 被取代 | 中 | 已被 `check_coverage_fast.py` 取代，模块级 cookies |
| `compare_clawhub_local.py` | Bug+副作用 | 高 | 模块级 `open()`，引用未导入的 `DATA_DIR`（bug），无 `__main__` |
| `batch_delete_clawhub.py` | 一次性+副作用 | 高 | 模块级 `open()` 读删除清单，无 `__main__` 守卫，一次性批量删除 |
| `test_api_endpoints.py` | 一次性+副作用 | 高 | 模块级 cookies，API 端点测试，无 `__main__`，一次性 |
| `test_fixes.py` | 位置错误 | 低 | 单元测试（U-09 回归），应在 `tests/` 而非 `tools/` |
| `github_repo_strategy.py` | 位置错误+重复 | 中 | 纯策略配置（无执行逻辑），应在 `config/`，与 `version_sync_pipeline.py` 内联 GitHub 配置重复 |
| `clean_naming.py` | 待确认 | 低 | 独立 CLI，无被导入，功能较窄 |
| `template_cleanup.py` | 待确认 | 低 | 独立 CLI，无被导入，功能较窄 |

#### 1.2 冗余/可合并脚本识别（~30 个）

| 类别 | 涉及脚本 | 建议 |
|------|---------|------|
| **三编排器并存** | `orchestrator.py`、`daily_sync.py`、`ops闭环.py` | 统一到 `daily_sync.py` (v3.0 最完整) |
| **三仪表盘分散** | `dashboard_server.py`、`platform_dashboard.py`、`quality_dashboard.py` | 合并为统一看板模块 |
| **历史修复脚本** | `diff_batch_fix.py`/`2`/`3`、`diff_l4_batch_fix.py`、`l3_batch_fix.py`、`l4_batch_fix.py` | 全部标记为历史残留，建议归档 |
| **版本化重复** | `skill_batch_upgrader_v2.py`/`v3.py`、`hermes_converter.py`/`hermes_batch_convert.py` | 合并到最新版本 |
| **状态检查碎片化** | `check_status.py`/`check_progress.py`/`analyze_status.py`/`health_check.py` | 统一为单一状态检查入口 |
| **修复脚本碎片化** | `batch_field_fix.py`/`fix_missing_fields.py`/`fix_marketing.py`/`batch_optimize_description.py` | 合并为统一字段修复工具 |
| **评分系统分裂** | `trace_llm_scorer.py` (TRACE) vs `local_quality_scorer.py` (5维) | 评估是否可统一，或明确分工 |
| **重叠系统** | `automated_review_system.py` vs `upload_gate`+`version_sync_pipeline`+`platform_ops` | 评估是否可移除 `automated_review_system.py` |
| **去重分散** | `deduplicate_all_v36.py`、`deduplicate_blocks.py` | 合并去重逻辑 |
| **升级检查重复** | `upgrade_checker.py` vs `update_mechanism.py` | 评估合并 |

#### 1.3 模块级副作用全面排查

对 `tools/` 目录所有 `.py` 文件执行 grep，识别模块顶层（非函数内）的副作用代码：
```powershell
# 搜索模块级 cookies 加载
Select-String -Path "d:\skills\tools\*.py" -Pattern "^cookies\s*=" -SimpleMatch
# 搜索模块级 open() 调用
Select-String -Path "d:\skills\tools\*.py" -Pattern "^\s*open\(" -SimpleMatch
# 搜索模块级 requests 调用
Select-String -Path "d:\skills\tools\*.py" -Pattern "^requests\." -SimpleMatch
```

#### 1.4 生成待处理清单

将所有发现统一写入 `code_cleanup_pending_list.md`，格式：

```markdown
# 代码清理待处理清单

生成时间：2026-07-27
生成原因：Phase 1 代码冗余扫描

## 一、死代码/桩代码（建议删除）

| 序号 | 文件路径 | 问题类型 | 严重度 | 被引用情况 | 建议处理方式 | Deletion Test |
|------|---------|---------|--------|-----------|-------------|--------------|
| 1 | tools/task6_enhance.py | 桩代码 | 高 | 无 | 删除 | 删除后复杂度消失 |

## 二、冗余/可合并脚本（建议合并/归档）
...

## 三、模块级副作用（建议修复为延迟加载）
...

## 四、碎片化功能（建议整合）
...
```

**验证**：
- 待处理清单包含所有识别的问题
- `git status` 无文件删除（仅新增待处理清单文件）
- 清单中每个条目都有明确的建议处理方式

---

### Phase 2: 文档清理

**目标**：检查项目全部文档，识别过期/无用/重复文档，统一存入待处理清单。**不删除/移动任何文件**。

**产出文件**：`d:\skills\data\reports\doc_cleanup_pending_list.md`

**步骤**：

#### 2.1 被取代的提示词文档（35 个）

`docs/plans/` 下的 `next-round-prompt-v40.0.md` ~ `v75.0.md`（v76.0 为最新，保留）。
- 缺口确认：v60.0、v62.0 未生成（非遗失）
- 建议处理：移入 `docs/plans/archive/`

#### 2.2 旧版可见性分析（5 个文件 + 2 个文件夹）

| 文件/文件夹 | 版本 | 建议处理 |
|------------|------|---------|
| `docs/skillhub-visibility-analysis.html` | v1 | 归档 |
| `docs/skillhub-visibility-optimization-v2.html` | v2 | 归档 |
| `docs/skillhub-audit-visibility-analysis-v3.html` | v3 | 归档 |
| `docs/skillhub-visibility-analysis-v4/` | v4 文件夹 | 归档 |
| `docs/skillhub-visibility-analysis-v5/` | v5 文件夹 | 归档 |
| `docs/skillhub-visibility-analysis-v6.html` | **v6 当前** | **保留** |

#### 2.3 `.trae/documents/` 临时文档（16 个）

- `round1-7-comprehensive-review.md` / `-v2.md`
- `round5-implementation-plan.md`、`round5-review-and-prompt.md`
- `round6-*` 系列（4 个）、`round6-prompt.md`、`round7-prompt.md`
- `skill-automation-comprehensive-fix-plan-v3.md` / `-v4.md`
- `skillhub-12-factor-deep-review-and-fix-plan.md`
- `skillhub-visibility-fix-and-v57-implementation.md`
- `v58-execution-plan.md`
- `archive/` 内 4 个更早版本
- 建议处理：清理（非正式 docs，Trae 会话过程文档）

#### 2.4 疑似重复报告（4 对）

| 疑似重复对 | 建议处理 |
|-----------|---------|
| `architecture-review.md` ↔ `architecture_review_report.md` | 保留最新，归档另一份 |
| `security-analysis-report.md` ↔ `security-compliance-audit.md` | 保留最新，归档另一份 |
| `round24_platform_review_strategy.md` ↔ `round25_platform_review_strategy.md` ↔ `platform_review_followup.md` | 仅保留 followup，归档 round24/25 |
| `第2轮`~`第5轮_最终整合审查报告.md`（4 个） | 仅保留第 5 轮 |

#### 2.5 轮次绑定过期报告（6 个）

| 文件 | 绑定轮次 | 建议处理 |
|------|---------|---------|
| `round-13-quality-trend-report.md` | round-13 | 归档 |
| `round24_platform_review_strategy.md` | round-24 | 归档 |
| `round25_platform_review_strategy.md` | round-25 | 归档 |
| `round25_triple_platform_alignment_report.md` | round-25 | 归档 |
| `v68-task-execution-report.md` | v68 | 归档 |
| `task2_task3_report.md` | 早期 | 归档 |

#### 2.6 新对话启动文档更新

- `new-conversation-first-prompt.md` 内容实为 v62.0 主题（四平台同步），与 v76.0（防封/解封）脱节
- 建议处理：更新内容或标注"已过时，参考 v76.0"

#### 2.7 生成待处理清单

将所有发现统一写入 `doc_cleanup_pending_list.md`，格式：

```markdown
# 文档清理待处理清单

生成时间：2026-07-27

## 一、被取代的提示词文档（35个，建议归档）
| 序号 | 文件路径 | 版本 | 被取代版本 | 建议处理 |
...

## 二、旧版可见性分析（5个，建议归档）
...

## 三、临时文档（16个，建议清理）
...

## 四、疑似重复报告（4对，建议合并）
...

## 五、轮次绑定过期报告（6个，建议归档）
...
```

**验证**：
- 待处理清单包含所有识别的文档
- `git status` 无文件删除/移动

---

### Phase 3: 管道验证

**目标**：确保所有管道在清理后仍能准确运行，防封处理确定生效。通过静态测试和运行时测试双重验证。

**产出文件**：`d:\skills\data\reports\pipeline_validation_report.md`

**使用技能**：systematic-debugging（调试管道问题）、verification-before-completion（验证）

**步骤**：

#### 3.1 静态语法测试

对 `tools/` 目录所有 `.py` 文件执行语法检查：
```powershell
# 批量语法检查
$results = @()
Get-ChildItem d:\skills\tools\*.py | ForEach-Object {
    $result = python -m py_compile $_.FullName 2>&1
    $results += [PSCustomObject]@{
        File = $_.Name
        Status = if ($LASTEXITCODE -eq 0) { "PASS" } else { "FAIL" }
        Error = $result
    }
}
$results | Format-Table -AutoSize
```

同时检查 `config/` 和 `tools/skill_core/` 下的 Python 文件。

#### 3.2 导入依赖测试

对 23 个核心脚本执行导入测试，验证模块间依赖完整：
```powershell
$coreScripts = @(
    "config", "db", "quality_gate", "upload_gate", "version_sync_pipeline",
    "platform_ops", "daily_sync", "orchestrator", "deep_quality_audit",
    "local_quality_scorer", "trace_llm_scorer", "market_monitor",
    "enterprise_uploader", "clawhub_batch_uploader", "auto_differentiate",
    "auto_discover", "pricing_engine", "l2_capability_checker",
    "l3_function_checker", "l4_task_gate", "source_fidelity_checker",
    "generate_skill", "check_debranding"
)
foreach ($script in $coreScripts) {
    python -c "import sys; sys.path.insert(0, 'd:/skills/tools'); import $script" 2>&1
    # 记录通过/失败
}
```

#### 3.3 关键管道运行时测试

执行以下管道的状态检查或 dry-run：

| 管道 | 测试命令 | 预期结果 |
|------|---------|---------|
| 每日同步 | `python tools/daily_sync.py --status` | 显示同步状态 |
| 质量门禁 | `python tools/quality_gate.py --help` | 显示帮助信息 |
| 版本同步 | `python tools/version_sync_pipeline.py --status` | 显示同步状态 |
| 平台运维 | `python tools/platform_ops.py --status` | 显示平台状态 |
| 市场监控 | `python tools/market_monitor.py --status` | 显示评分状态 |
| 上传门控 | `python tools/upload_gate.py --help` | 显示帮助信息 |
| 本地评分 | `python tools/local_quality_scorer.py --help` | 显示帮助信息 |
| DB 查询 | `python -c "from db import *; print(get_skill_count())"` | 返回 skill 数量 |

#### 3.4 防封处理验证（5 项核心检查）

这是 Phase 3 的关键部分，验证封禁根因的修复措施是否生效：

**检查 1: 速率限制**
```powershell
# 验证 upload_rate_limits 表存在且配置正确
python -c "
import sys; sys.path.insert(0, 'd:/skills/tools')
from db import get_connection
conn = get_connection()
# 检查表是否存在
cursor = conn.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='upload_rate_limits'\")
table_exists = cursor.fetchone() is not None
# 检查配置
cursor = conn.execute('SELECT * FROM upload_rate_limits ORDER BY timestamp DESC LIMIT 5')
recent_uploads = cursor.fetchall()
print(f'Table exists: {table_exists}')
print(f'Recent uploads tracked: {len(recent_uploads)}')
# 检查配置常量
import config
print(f'MAX_UPLOADS_PER_HOUR: {getattr(config, \"MAX_UPLOADS_PER_HOUR\", \"NOT FOUND\")}')
print(f'MAX_UPLOADS_PER_DAY: {getattr(config, \"MAX_UPLOADS_PER_DAY\", \"NOT FOUND\")}')
print(f'MIN_INTERVAL_SECONDS: {getattr(config, \"MIN_INTERVAL_SECONDS\", \"NOT FOUND\")}')
"
```
预期：表存在，配置为 30/hour, 100/day, 120s

**检查 2: 内容指纹去重**
```powershell
# 验证 quality_gate.py 中的内容指纹去重逻辑
python -c "
import sys; sys.path.insert(0, 'd:/skills/tools')
import quality_gate
# 检查是否有内容指纹去重函数
import inspect
source = inspect.getsource(quality_gate)
has_fingerprint = 'fingerprint' in source.lower() or 'content_hash' in source.lower()
has_threshold = '0.85' in source or '85' in source
print(f'Has fingerprint logic: {has_fingerprint}')
print(f'Has 85% threshold: {has_threshold}')
"
```
预期：有指纹去重逻辑，阈值 85%

**检查 3: slug 变异消除**
```powershell
# 验证 publish_to_community 中已移除 -sk/-sk1/-sk2/-sk3 改名逻辑
python -c "
import sys; sys.path.insert(0, 'd:/skills/tools')
import platform_ops
import inspect
source = inspect.getsource(platform_ops)
# 搜索 -sk 后缀逻辑
has_sk_suffix = '-sk1' in source or '-sk2' in source or '-sk3' in source or \"-sk'\" in source
# 搜索新的 slug 处理逻辑
has_slug_cleanup = 'clean_slug' in source or 'remove_suffix' in source
print(f'Has -sk suffix logic (should be False): {has_sk_suffix}')
print(f'Has slug cleanup logic: {has_slug_cleanup}')
"
```
预期：无 -sk 后缀逻辑

**检查 4: 派生内容消除**
```powershell
# 验证已停止 -free/-pro 独立 slug 生成
python -c "
import sys; sys.path.insert(0, 'd:/skills/tools')
import auto_differentiate
import inspect
source = inspect.getsource(auto_differentiate)
# 检查是否还有 -free/-pro slug 生成
has_free_pro_slug = \"-free'\" in source or \"-pro'\" in source or '-free\"' in source or '-pro\"' in source
# 检查是否有 edition 元数据方式
has_edition = 'edition' in source.lower()
print(f'Has -free/-pro slug generation (should be False): {has_free_pro_slug}')
print(f'Has edition metadata: {has_edition}')
"
```
预期：无 -free/-pro slug 生成，有 edition 元数据

**检查 5: 安全预检集成**
```powershell
# 验证 21 项安全检查集成到上传管道
python -c "
import sys; sys.path.insert(0, 'd:/skills/tools')
import upload_gate
import inspect
source = inspect.getsource(upload_gate)
# 检查安全预检调用
has_security_check = 'source_security_scan' in source or 'security_pre_check' in source or 'security_scan' in source
print(f'Has security check integration: {has_security_check}')
# 验证 quality_gate 中的安全检查
import quality_gate
qg_source = inspect.getsource(quality_gate)
security_patterns = ['ssrf', 'data_exfiltration', 'obfuscation', 'reverse_shell', 'privilege_escalation', 'mining', 'prompt_injection', 'persistence', 'deserialization', 'dependency_confusion']
found_patterns = [p for p in security_patterns if p in qg_source.lower()]
print(f'Security patterns found: {len(found_patterns)}/10')
print(f'Patterns: {found_patterns}')
"
```
预期：安全检查已集成，10+ 项安全模式检测

#### 3.5 DB 一致性检查

```powershell
python -c "
import sys; sys.path.insert(0, 'd:/skills/tools')
from db import get_connection
conn = get_connection()

# 1. 检查 local_quality_score 字段存在
cursor = conn.execute('PRAGMA table_info(skills)')
columns = [row[1] for row in cursor.fetchall()]
has_score_field = 'local_quality_score' in columns
has_feedback_field = 'local_score_feedback' in columns
has_at_field = 'local_score_at' in columns

# 2. 检查评分覆盖
cursor = conn.execute('SELECT COUNT(*) FROM skills WHERE local_quality_score IS NOT NULL')
scored_count = cursor.fetchone()[0]
cursor = conn.execute('SELECT COUNT(*) FROM skills')
total_count = cursor.fetchone()[0]

# 3. 检查 upload_rate_limits 表
cursor = conn.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='upload_rate_limits'\")
rate_limit_table = cursor.fetchone() is not None

print(f'Score field exists: {has_score_field}')
print(f'Feedback field exists: {has_feedback_field}')
print(f'Timestamp field exists: {has_at_field}')
print(f'Scored skills: {scored_count}/{total_count}')
print(f'Rate limit table: {rate_limit_table}')
"
```

#### 3.6 生成管道验证报告

产出 `d:\skills\data\reports\pipeline_validation_report.md`，包含：
- 静态语法测试结果（通过/失败文件列表）
- 导入依赖测试结果（通过/失败模块列表）
- 运行时测试结果（各管道状态）
- 防封处理验证结果（5 项检查通过/失败）
- DB 一致性检查结果
- 发现的问题列表和修复建议

**验证标准**：
- 所有核心脚本通过 `py_compile`
- 所有核心脚本可正常导入（允许模块级副作用的脚本除外，记录为已知问题）
- 关键管道可执行状态检查
- 5 项防封措施全部生效
- DB 字段和表结构完整

---

### Phase 4: Skill 质量检查

**目标**：检查所有收费和免费 skill 的质量，确保每个 skill 评分 >4.5 分，防封处理得到保证。逐一处理，确保所有 skill 完全不会被第三方系统再次封禁。

**产出文件**：`d:\skills\data\reports\skill_quality_check_report.md`

**使用技能**：verification-before-completion、systematic-debugging

**Skill 检查范围**（"用于赚钱的收费和免费 skill"）：

| 范围 | 数量 | 说明 |
|------|------|------|
| 金融 skill（已生产） | 30 | 20 付费 + 10 免费，`differentiated-skills/` |
| 企业付费 skill | 2 | `enterprise-upload/` 下 |
| 开源打包 skill | 40 | `opensource-skills/packaged/` |
| DB 中已上传 SkillHub 的 skill | 1120 | 含 563 已封禁，需逐一检查 |
| DB 中 local_only skill | 1691 | 待评分，按优先级处理 |

**步骤**：

#### 4.1 全量本地评分扫描（继续/启动）

当前 125/1072 已评分，继续扫描剩余 skill：
```powershell
# 批量扫描，使用 local_quality_scorer
python d:\skills\tools\quality_gate.py --batch-scan --limit 2000
```
预计 1072 个 skill × ~3 秒 ≈ 54 分钟（LLM 调用为瓶颈）。

如果 LLM API 不可用，记录为阻塞项，跳到 4.4 手动检查。

#### 4.2 低分 skill 识别

```powershell
python -c "
import sys; sys.path.insert(0, 'd:/skills/tools')
from db import get_connection
conn = get_connection()

# 低分 skill（≤4.5）
cursor = conn.execute('''
    SELECT slug, local_quality_score, local_score_feedback 
    FROM skills 
    WHERE local_quality_score <= 4.5 AND local_quality_score IS NOT NULL
    ORDER BY local_quality_score ASC
''')
low_score = cursor.fetchall()

# 未评分 skill
cursor = conn.execute('''
    SELECT slug FROM skills WHERE local_quality_score IS NULL
''')
unscored = cursor.fetchall()

# 高分 skill（>4.5）
cursor = conn.execute('''
    SELECT COUNT(*) FROM skills WHERE local_quality_score > 4.5
''')
high_score_count = cursor.fetchone()[0]

print(f'Low score (≤4.5): {len(low_score)}')
print(f'Unscored: {len(unscored)}')
print(f'High score (>4.5): {high_score_count}')
print(f'\\nLow score skills (first 20):')
for slug, score, feedback in low_score[:20]:
    print(f'  {slug}: {score} - {feedback[:80] if feedback else \"N/A\"}')
"
```

#### 4.3 低分 skill 逐一升级（循环重做）

对每个低分 skill（≤4.5）：

1. **读取 SKILL.md 内容**
2. **分析最弱 1-2 维度**（基于 `local_score_feedback`）
3. **执行实质性内容增强**（非补丁式修复）：
   - 功能完整性不足 → 补充功能描述、使用场景、示例
   - 准确性不足 → 修正错误信息、补充技术细节
   - 易用性不足 → 优化结构、添加快速入门
   - 安全性不足 → 添加安全注意事项、移除风险代码
   - 创新性不足 → 增加独特功能、差异化描述
4. **重新评分**
5. **循环直到 >4.5 或 3 轮上限**

```powershell
# 使用 upgrade_single_skill 升级单个 skill
python d:\skills\tools\version_sync_pipeline.py upgrade --slug {slug}
# 重新评分
python d:\skills\tools\quality_gate.py --score-single --slug {slug}
```

**升级原则**：
- 严禁补丁式修复（如仅改 description 的几个字）
- 必须针对最弱维度做实质性内容增强
- 每轮升级后重新评分验证
- 3 轮后仍 ≤4.5 的标记为"需人工介入"

#### 4.4 防封处理逐一验证

对每个 skill 检查以下 7 项防封指标：

| 检查项 | 标准 | 检查方法 |
|--------|------|---------|
| **slug 规范性** | 无 -sk/-sk1/-sk2/-sk3 后缀，无 -free/-pro 独立 slug | DB 查询 slug 模式 |
| **内容唯一性** | 与其他 skill 内容指纹相似度 <85% | 内容指纹比对 |
| **displayName 中文化** | 非英文/非模板 | DB 查询 displayName |
| **summary 营销质量** | 非模板套话、非占位符 | 质量门禁检查 |
| **description 非模板** | 无占位符、无重复句子 | 质量门禁检查 |
| **安全合规** | 通过 21 项安全检查 | 安全预检 |
| **防幻觉** | 通过 3 项防幻觉检查 | 防幻觉检查 |

```powershell
# 批量检查 slug 规范性
python -c "
import sys; sys.path.insert(0, 'd:/skills/tools')
from db import get_connection
import re
conn = get_connection()

# 查找有问题的 slug
cursor = conn.execute('SELECT slug FROM skills')
bad_slugs = []
for (slug,) in cursor.fetchall():
    # 检查 -sk 后缀
    if re.search(r'-sk\d*$', slug):
        bad_slugs.append((slug, 'sk_suffix'))
    # 检查 -free/-pro 独立 slug
    elif re.search(r'-free$|-pro$', slug):
        bad_slugs.append((slug, 'free_pro_suffix'))
    # 检查短 slug
    elif len(slug) <= 8:
        bad_slugs.append((slug, 'short_slug'))

print(f'Problematic slugs: {len(bad_slugs)}')
for slug, issue in bad_slugs[:20]:
    print(f'  {slug}: {issue}')
"
```

#### 4.5 平台评分同步

对已上传的 skill 同步平台评分：
```powershell
# 批量同步评分（每次 200 个）
python d:\skills\tools\market_monitor.py sync-ratings --limit 200
```

#### 4.6 30 个金融 skill 专项检查

对 30 个金融 skill（20 付费 + 10 免费）执行专项质量检查：
```powershell
# 检查金融 skill 的定价、license、质量
python -c "
import sys; sys.path.insert(0, 'd:/skills/tools')
from db import get_connection
conn = get_connection()

# 查询金融 skill
cursor = conn.execute('''
    SELECT slug, local_quality_score, license, pricing_model, price
    FROM skills 
    WHERE slug LIKE '%finance%' OR slug LIKE '%trading%' OR slug LIKE '%stock%' 
    OR slug LIKE '%quant%' OR slug LIKE '%crypto%' OR slug LIKE '%investment%'
    OR slug LIKE '%portfolio%' OR slug LIKE '%risk%' OR slug LIKE '%accounting%'
    OR slug LIKE '%tax%' OR slug LIKE '%budget%' OR slug LIKE '%forex%'
    OR slug LIKE '%banking%' OR slug LIKE '%insurance%' OR slug LIKE '%loan%'
''')
finance_skills = cursor.fetchall()
print(f'Finance skills: {len(finance_skills)}')
for slug, score, license, pricing, price in finance_skills:
    status = 'OK' if score and score > 4.5 else 'NEEDS_WORK'
    print(f'  {slug}: score={score}, license={license}, price={price} [{status}]')
"
```

#### 4.7 生成质量检查报告

产出 `d:\skills\data\reports\skill_quality_check_report.md`，包含：
- 全量评分统计（已评分数、平均分、分布）
- 低分 skill 列表和处理状态
- 防封处理验证结果（7 项检查通过/失败）
- 30 个金融 skill 专项检查结果
- 平台评分同步状态
- 发现的管道问题（反馈给 Phase 3）

**验证标准**：
- 所有已评分 skill 的 `local_quality_score > 4.5`
- 所有 skill 通过 7 项防封处理检查
- 无 -sk/-sk1/-sk2/-sk3 后缀的 slug
- 无 -free/-pro 独立 slug
- 无内容指纹相似度 >85% 的 skill 对

---

### Phase 5: 交叉迭代

**目标**：Phase 3/4/5 作为一个计划单元反复交叉执行，直到所有管道完全通畅有效且稳健，同时所有 skill 高质量不会被第三方系统再次评价为低于 4.5 分。

**迭代逻辑**：

```
迭代轮次 N（最多 5 轮）:

  ┌─────────────────────────────────────────────────────┐
  │  Step 1: 执行 Phase 3（管道验证）                      │
  │    → 发现管道问题？                                    │
  │      是 → 修复管道 → 记录修复 → 继续 Step 2           │
  │      否 → 继续 Step 2                                │
  ├─────────────────────────────────────────────────────┤
  │  Step 2: 执行 Phase 4（Skill 质量检查）                │
  │    → 发现 skill ≤4.5？                                │
  │      是 → 升级 skill → 重新评分 → 回到 Step 2         │
  │      否 → 继续 Step 3                                │
  │    → 发现管道问题（从 skill 检查中反映）？              │
  │      是 → 记录问题 → 回到 Step 1                      │
  │      否 → 继续 Step 3                                │
  ├─────────────────────────────────────────────────────┤
  │  Step 3: 检查退出条件                                 │
  │    1. 所有核心脚本通过 py_compile？                    │
  │    2. 所有核心脚本可正常导入？                         │
  │    3. 关键管道可执行状态检查？                         │
  │    4. 5 项防封措施全部生效？                           │
  │    5. 所有已评分 skill >4.5？                         │
  │    6. 低分 skill 通过率 ≥95%？                        │
  │    → 全部满足 → 退出循环，生成最终报告                 │
  │    → 有不满足 → 回到 Step 1（下一轮迭代）              │
  └─────────────────────────────────────────────────────┘
```

**退出条件**（全部满足）：
1. ✅ 所有核心脚本通过 `py_compile`
2. ✅ 所有核心脚本可正常导入
3. ✅ 关键管道可执行状态检查
4. ✅ 5 项防封措施全部生效（速率限制/内容去重/slug规范/派生消除/安全预检）
5. ✅ 所有已评分 skill 的 `local_quality_score > 4.5`
6. ✅ 低分 skill 通过率 ≥ 95%（剩余 ≤5% 标记人工介入）

**迭代上限**：5 轮。如 5 轮后仍有未解决项，记录为"需人工介入"并生成最终报告。

**每轮迭代产出**：
- `d:\skills\data\reports\iteration_round_{N}_report.md`（每轮迭代报告）

**最终产出**：
- `d:\skills\data\reports\final_quality_governance_report.md`（最终质量治理报告）

---

## 四、执行顺序与依赖关系

```
Phase 0 (Git备份)
  │
  ├── 成功 ──→ Phase 1 (代码清理清单) ──→ Phase 2 (文档清理清单)
  │                                          │
  └── 失败 ──────────────────────────────────┤
                                             │
                                             ▼
                              Phase 3+4+5 (交叉迭代单元)
                                    │
                                    ▼
                              最终报告生成
                                    │
                                    ▼
                              Git 提交（成果备份）
```

**关键依赖**：
- Phase 1/2 依赖 Phase 0 成功（如失败则跳过）
- Phase 3/4/5 互为依赖，交叉执行
- Phase 4 的 skill 升级可能影响 Phase 3 的管道（需重新验证）
- Phase 3 的管道修复可能影响 Phase 4 的评分（需重新评分）

---

## 五、假设与决策 (Assumptions & Decisions)

### 假设
1. GitHub 网络（github.com:443）在执行期间保持可达（当前测试通过）
2. 智谱 GLM-4-Flash API 可用（本地评分器依赖；如不可用，跳过自动评分，执行手动检查）
3. SQLite 数据库（`skill-registry.db`）可正常读写
4. 用户已有的 git 凭证有效（无需重新认证）
5. Python 3.x 环境正常可用

### 决策
1. **Git 备份仓库**：使用现有公开仓库（`origin`/`hermes-skills`），因无私有备份仓库且用户睡眠无法创建。如推送失败，跳过 Phase 1/2 但继续 Phase 3/4/5（不涉及删除操作）。
2. **代码清理方式**：仅生成待处理清单（`code_cleanup_pending_list.md`），**不删除任何文件**。用户醒来后审阅清单决定实际处理。
3. **文档清理方式**：同上，仅生成待处理清单（`doc_cleanup_pending_list.md`），**不删除/移动任何文件**。
4. **Skill 质量检查范围**：优先检查 30 个金融 skill + 2 个企业付费 skill + 40 个开源打包 skill + DB 中已上传 SkillHub 的 skill。全量扫描 1072 个 DB 中 skill。
5. **防封处理标准**：基于 `banned_skills_root_cause_analysis.md` 的五大根因，逐一验证 5 项修复措施生效。
6. **交叉迭代上限**：5 轮，避免无限循环。每轮包含完整的 Phase 3 + Phase 4。
7. **自主执行**：所有操作无需用户确认，包括 git 提交、管道测试、skill 升级、评分同步等。
8. **LLM API 不可用时的降级策略**：如 GLM-4-Flash 不可用，跳过自动评分，改为手动检查 skill 内容质量（基于质量门禁的静态检查项）。
9. **防封处理优先级**：slug 规范性 > 内容唯一性 > 安全合规 > 质量评分。即使评分不达标，防封处理也必须完成。

---

## 六、验证步骤 (Verification Steps)

### Phase 0 验证
- [ ] `git status` 显示 clean（无未提交更改）
- [ ] `git log origin/main -1` 显示备份 commit
- [ ] `backup_status.json` 记录成功状态
- [ ] 如失败：记录失败原因，标记 `skip_phase_1_2 = true`

### Phase 1 验证
- [ ] `code_cleanup_pending_list.md` 存在且包含所有识别的问题
- [ ] 覆盖 13 个死代码 + 30 个冗余 + 8 个模块级副作用
- [ ] `git status` 无文件删除（仅新增待处理清单）
- [ ] 每个条目有明确的建议处理方式和 Deletion Test 分析

### Phase 2 验证
- [ ] `doc_cleanup_pending_list.md` 存在且包含所有识别的文档
- [ ] 覆盖 35 个被取代提示词 + 5 个旧版分析 + 16 个临时文档 + 4 对重复 + 6 个过期报告
- [ ] `git status` 无文件删除/移动

### Phase 3 验证
- [ ] `pipeline_validation_report.md` 存在
- [ ] 所有核心脚本通过 `py_compile`（记录失败的为已知问题）
- [ ] 所有核心脚本可导入（模块级副作用的记录为已知问题）
- [ ] 关键管道可执行状态检查
- [ ] 5 项防封措施全部生效：
  - [ ] 速率限制（30/hour, 100/day, 120s）
  - [ ] 内容指纹去重（>85% 阻断）
  - [ ] slug 变异消除（无 -sk 后缀）
  - [ ] 派生内容消除（无 -free/-pro 独立 slug）
  - [ ] 安全预检集成（21 项检查）
- [ ] DB 字段完整（local_quality_score 等字段存在）

### Phase 4 验证
- [ ] `skill_quality_check_report.md` 存在
- [ ] 全量评分扫描完成（或记录阻塞原因）
- [ ] 所有已评分 skill 的 `local_quality_score > 4.5`（或记录为"需人工介入"）
- [ ] 所有 skill 通过 7 项防封处理检查
- [ ] 30 个金融 skill 专项检查完成
- [ ] 平台评分同步执行（或记录阻塞原因）

### Phase 5 验证
- [ ] 退出条件全部满足，或达到 5 轮迭代上限
- [ ] 每轮迭代报告生成
- [ ] `final_quality_governance_report.md` 生成
- [ ] 最终 git 提交（成果备份）

---

## 七、技能与插件使用说明

| 阶段 | 技能/插件 | 用途 |
|------|----------|------|
| Phase 1 | `architecture` skill | 代码冗余分析、Deletion Test、Seam 分析 |
| Phase 1 | `code-review` (coderabbit) | 审查识别的冗余代码 |
| Phase 3 | `systematic-debugging` (hotl/superpowers) | 调试管道问题 |
| Phase 3 | `verification-before-completion` (hotl/superpowers) | 验证管道完整性 |
| Phase 3 | `chrome-devtools` / `agent-browser` | 检查 SkillHub/ClawHub 在线状态 |
| Phase 4 | `verification-before-completion` | 验证 skill 质量 |
| Phase 4 | `dogfood` | 测试 SkillHub 平台 skill 展示 |
| Phase 5 | `staff-engineer-mode` | 工程决策（迭代优先级） |
| 全程 | `tailtest` | 测试关键管道脚本 |
| 全程 | `writing-plans` (hotl/superpowers) | 每轮迭代计划更新 |

---

## 八、风险与缓解

| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|---------|
| Git 推送失败（网络中断） | 中 | 跳过 Phase 1/2 | 先验证网络，失败则跳过清理，直接管道验证 |
| LLM API 不可用 | 中 | 无法自动评分 | 降级为手动检查，记录阻塞项 |
| 管道修复引入新 bug | 低 | 管道中断 | 每次修复后立即运行 Phase 3 验证 |
| Skill 升级破坏内容 | 低 | 质量下降 | 升级前备份原内容，升级后验证 |
| 迭代不收敛 | 低 | 无限循环 | 5 轮上限，剩余项标记人工介入 |
| DB 锁定/损坏 | 极低 | 数据丢失 | Phase 0 已备份，可恢复 |
