# Skill 生产工作流完整性评估报告

> **评估时间**: 2026-07-20
> **评估范围**: `d:\skills\skill-registry` 目录下的 skill 生产工作流
> **评估对象**: 更新/发现/治理 三大触发机制、流水线完整性、质量检查、重试机制、工作流状态追踪

---

## 一、执行摘要

| 评估维度 | 状态 | 评分 |
|---------|------|------|
| 三大触发文档完整性 | 缺失治理触发文档 | 不合格 |
| 发现流水线完整性 | 存在多处断点 | 待改进 |
| 差异化方法论文档 | 存在但位置不规范 | 合格 |
| 质量检查自动化 | 仅去标识检查，缺综合验证 | 不合格 |
| 上传失败重试机制 | 完全缺失 | 不合格 |
| workflow_state 追踪 | 严重失效（1848/1909 卡在 step1） | 不合格 |

**总体结论**: 工作流设计架构完整（三大系统分工明确），但工程化落地存在显著缺口。核心问题集中在：治理触发文档缺失、质量验证未自动化、上传无重试、workflow_state 字段大面积失效。

---

## 二、三大触发机制文档完整性评估

### 2.1 现状

| 触发词 | 触发文档 | 主控脚本 | 状态 |
|--------|---------|---------|------|
| "更新" | `UPDATE_TRIGGER.md` | `update_mechanism.py` | 存在，6阶段流水线完整定义 |
| "发现" | `DISCOVER_TRIGGER.md` | `auto_discover.py` | 存在，5阶段流水线完整定义 |
| "治理" | **缺失** | `clean_naming.py` | 脚本存在，但无触发文档 |

### 2.2 问题：缺少 GOVERNANCE_TRIGGER.md

**证据**: 在 `d:\skills\skill-registry\` 目录下仅存在两个触发文档：
- `UPDATE_TRIGGER.md`
- `DISCOVER_TRIGGER.md`

`NAMING_CONVENTION.md` 第七章和 `DISCOVER_TRIGGER.md` 的"协作"章节都提到了"治理"触发词对应 `clean_naming.py`，但**没有为"治理"定义独立的触发文档**。

**影响**:
- AI 收到"治理"指令时无标准化的执行手册
- 治理流程的触发规则、执行顺序、边界情况处理未文档化
- 治理操作（合并-free/-pro、修复字段、修复category）的优先级和依赖关系不明确

**建议**: 创建 `GOVERNANCE_TRIGGER.md`，内容包括：
1. 触发规则（精确匹配"治理"）
2. 执行流程（dry-run 预览 → 确认 → execute → report）
3. 治理策略A/B/C的执行条件
4. 已上传skill的保护逻辑（legacy_slug 标记）
5. 治理后的验证步骤

---

## 三、发现流水线完整性评估

### 3.1 流水线设计（DISCOVER_TRIGGER.md 定义）

```
阶段1: 来源扫描 → 阶段2: 去重比对 → 阶段3: 差异化改造 → 阶段4: 双版本生成+上传 → 阶段5: 汇报
```

### 3.2 发现的断点

#### 断点1: 差异化方法论文档路径不一致

**问题**: `DISCOVER_TRIGGER.md` 阶段3引用 `deep-differentiation-methodology.md`，但未指定路径。实际文件位于 `d:\skills\deep-differentiation-methodology.md`（父目录），而非 `d:\skills\skill-registry\` 内。

**影响**: AI 执行时可能找不到该文件，或在不同目录下查找浪费时间。

#### 断点2: auto_discover.py import 命令未真正导入数据库

**问题**: `auto_discover.py` 的 `cmd_import()` 函数（第419-452行）仅打印指导信息，**不执行实际数据库导入操作**：

```python
def cmd_import(args):
    # ... 查找候选skill ...
    print(f"导入skill: {args.slug}")
    print(f"  注意: 导入需要AI执行差异化改造，请参考NAMING_CONVENTION.md")
    # 没有任何 DB 写入操作
```

**影响**: 流水线在"导入"环节断裂，需要AI手动接续。没有数据库记录意味着后续的版本追踪、上传状态追踪都无法关联。

#### 断点3: 差异化改造与数据库录入脱节

**问题**: `DISCOVER_TRIGGER.md` 阶段3步骤5"录入数据库"仅写了 `python update_mechanism.py status`，但该命令只是**显示状态**，并不录入新skill。

实际录入需要调用 `db.py` 的 `register_skill()` 函数，但发现流程中没有任何脚本调用它。

**影响**: 差异化改造完成后的skill可能不会被录入数据库，导致"影子skill"（文件存在但DB无记录）。

#### 断点4: 质量验证未集成到流水线

**问题**: `check_debranding.py` 脚本存在，但 `DISCOVER_TRIGGER.md` 的流水线中**没有调用它的步骤**。差异化改造后直接进入双版本生成和上传，缺少质量门禁。

**影响**: 含有原始仓库名、作者名、平台烙印词的skill可能直接上传到平台。

#### 断点5: 付费版上传依赖人工浏览器操作

**问题**: `update_mechanism.py` 的 `upload_paid_via_api()` 函数（第610-622行）只准备payload，实际上传需要AI通过浏览器MCP完成：

```python
def upload_paid_via_api(slug, payload):
    result['status'] = 'payload_ready'
    result['note'] = '企业API上传需要浏览器session cookies认证，请通过browser_evaluate执行上传'
    return result
```

**影响**: 付费版上传无法自动化，每次都需要人工介入。session cookies过期后需要重新登录。

### 3.3 流水线断点汇总图

```
阶段1: 来源扫描 ──[OK]──> 阶段2: 去重比对 ──[断点2]──> 阶段3: 差异化改造
                                                         │
                                                  [断点1: 方法论路径]
                                                  [断点4: 无质量门禁]
                                                         │
                                                         v
阶段5: 汇报 <──[断点5: 付费版需人工]── 阶段4: 双版本+上传
                                    [断点3: DB录入脱节]
```

---

## 四、差异化改造方法论文档评估

### 4.1 现状

**文件**: `d:\skills\deep-differentiation-methodology.md` （存在）

### 4.2 文档内容评估

| 章节 | 内容 | 完整度 |
|------|------|--------|
| 核心原则 | 不重写、不抄袭、不伪装 | 完整 |
| 五大差异化维度 | 质量/实用性/易用性/成本/性能 | 完整 |
| 改造流程（5步） | 分析→痛点研究→设计→重写→验证 | 完整 |
| slug命名规则 | 功能化命名，kebab-case | 完整 |
| frontmatter规范 | 含完整字段定义 | 完整 |
| 依赖说明章节 | 运行环境/第三方依赖/API Key/可用性分类 | 完整 |
| 进度跟踪 | 保存到 differentiation-log.csv | 有定义但未与DB集成 |

### 4.3 发现的问题

**问题1: 文档位置不规范**
- 文件位于 `d:\skills\deep-differentiation-methodology.md`（父目录）
- 应移至 `d:\skills\skill-registry\deep-differentiation-methodology.md` 与其他工作流文档同目录

**问题2: 命名规则与 NAMING_CONVENTION.md 冲突**
- 方法论文档说：`新slug命名：[原意]-pro 或 [新概念]`
- NAMING_CONVENTION.md 说：`不允许 -pro 后缀，统一用 {base-slug} 和 {base-slug}-free`
- 两份文档对slug后缀的规则**相互矛盾**

**问题3: 进度跟踪未与数据库集成**
- 方法论文档要求保存到 `differentiation-log.csv`
- 但数据库已有 `workflow_states` 表（10步追踪）和 `workflow_state` 字段
- 双重跟踪机制未统一，且 `workflow_states` 表完全为空（见第六节）

**问题4: 验证步骤（步骤5）未自动化**
- 方法论步骤5"验证"为人工检查
- 实际有 `check_debranding.py` 可自动检查去标识，但未集成

---

## 五、质量检查自动化评估

### 5.1 现有质量检查能力

| 检查项 | 脚本 | 自动化程度 | 集成到流水线 |
|--------|------|-----------|-------------|
| 去标识化检测 | `check_debranding.py` | 自动（支持目录扫描） | **未集成** |
| frontmatter合规 | 无独立脚本 | 仅在 `parse_skill_md()` 中解析 | 未集成 |
| 八大维度评分 | `db.py record_score()` | 函数存在，无调用脚本 | 未集成 |
| 依赖说明章节 | 无 | 无 | 无 |
| slug命名规范 | `clean_naming.py` 可分析 | 自动 | 独立运行，未集成到发现流水线 |

### 5.2 关键缺失

**缺失1: SKILL.md 生成后无自动验证步骤**

发现流水线阶段3（差异化改造）完成后，直接进入阶段4（双版本生成+上传），**中间没有验证步骤**：

```
差异化改造完成 → [应在此处验证] → 双版本生成 → 上传
                  ↑ 缺失
```

应有的验证项：
1. frontmatter 必填字段检查（slug, name, version, displayName, summary, license）
2. 去标识化检测（调用 `check_debranding.py`）
3. 依赖说明章节存在性检查
4. slug 命名规范检查（不含版本号、不含 -pro 后缀）
5. displayName 中文化检查
6. 八大维度评分（需达到40分阈值）

**缺失2: 八大维度评分无自动化脚本**

`db.py` 定义了 `record_score()` 函数和 `scores` 表，支持八大维度评分：
- quality, practicality, simplicity, cost, performance, debranding, compliance, differentiation
- 阈值40分，`is_pass` 字段记录是否通过

但**没有任何脚本自动调用此函数**。评分完全依赖人工判断，且 `scores` 表可能为空。

**缺失3: 质量门禁机制不存在**

即使有检查脚本，也没有"不通过则阻止上传"的门禁机制。`update_mechanism.py` 的 `upload-all` 命令不检查质量分数，直接上传所有已变更skill。

### 5.3 数据库验证

经查询，`scores` 表和 `workflow_states` 表均无记录（`workflow_states` 表完全为空），证实质量评分和工作流状态追踪均未实际运行。

---

## 六、上传失败重试机制评估

### 6.1 数据库查询结果

```
platform_uploads 上传统计:
  clawhub | success | 159
  clawhub | fail    | 2
  skillhub | success | 29
  skillhub | fail    | 9

上传总记录: 199
失败总记录: 11
```

### 6.2 失败记录详情

| Slug | 平台 | HTTP状态 | 错误原因 |
|------|------|---------|---------|
| openclaw-automation-recipes | clawhub | 1 | 使用了受保护的"openclaw" slug |
| linear-workflow-bot | skillhub | 500 | `{"success": false`（错误信息被截断） |
| cron-guard | skillhub | 500 | `{"success": false`（错误信息被截断） |
| cdp-browser-master | skillhub | 500 | `{"success": false`（错误信息被截断） |

### 6.3 重试机制评估

**结论：完全缺失重试机制**

**证据1**: `update_mechanism.py` 的上传函数无重试逻辑

```python
def upload_free_via_cli(slug, skill_md_path):
    # 单次执行，失败直接返回 'failed'
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    result['status'] = 'success' if proc.returncode == 0 else 'failed'
    # 无重试
```

**证据2**: `workflow_states` 表有 `retry_count` 字段，但表完全为空，从未使用。

**证据3**: 失败记录在数据库中存在多条重复（如 linear-workflow-bot 有3条失败记录），说明是**人工多次尝试**而非自动重试。

**证据4**: 错误信息被截断（`{"success": false`），无法用于诊断失败原因。`record_upload()` 的 `error_message` 字段未完整保存API响应。

### 6.4 改进建议

1. **实现自动重试**: 在 `upload_free_via_cli()` 和付费版上传中增加指数退避重试（最多3次）
2. **完善错误信息**: 完整保存API响应body，不截断
3. **失败队列机制**: 上传失败的skill进入重试队列，可通过 `python update_mechanism.py retry-failed` 批量重试
4. **区分错误类型**: 
   - 可重试错误（500、超时）→ 自动重试
   - 不可重试错误（400、protected slug）→ 标记为永久失败，需人工修复
5. **利用 workflow_states.retry_count**: 实际启用该字段追踪重试次数

---

## 七、workflow_state 字段追踪有效性评估

### 7.1 数据库查询结果

```
workflow_state 各状态记录数:
  step1_read_original : 1848
  completed           : 61
  TOTAL skills        : 1909

workflow_states 表（10步工作流）状态分布:
  [EMPTY] workflow_states table has no records!
```

### 7.2 问题诊断

**核心问题：1848条记录（96.8%）卡在 `step1_read_original`，但实际这些skill多数已完成差异化改造。**

**根因分析**:

| 导入脚本 | 是否设置 workflow_state | 记录数 |
|---------|------------------------|--------|
| `init_baseline.py` | 是，设为 `'completed'` | 61 |
| `scan_and_import.py` | **否**，使用DB默认值 `'step1_read_original'` | 1848 |

**证据**: 
- `init_baseline.py` 第104行显式设置 `workflow_state='completed'`
- `scan_and_import.py` 的 `import_skills_to_db()` 函数调用 `register_skill()`，但 `register_skill()` 函数（db.py 第299行）**不接受 workflow_state 参数**，使用Schema定义的默认值 `'step1_read_original'`

**证据2**: `workflow_states` 表（10步详细追踪表）完全为空，说明 `db.py` 的 `update_workflow_state()` 函数**从未被任何脚本调用**。

### 7.3 影响分析

1. **状态不可信**: 无法通过 `workflow_state` 字段判断skill的真实进度
2. **断点续作失效**: 如果AI想从断点恢复工作流，无法知道哪些skill完成了哪些步骤
3. **10步工作流形同虚设**: `db.py` 定义了完整的10步工作流状态机，但没有任何脚本使用它

### 7.4 矛盾点

`current_status` 字段显示：
```
optimized     : 930
differentiated : 898
packaged      : 39
published     : 22
registered    : 20
```

这说明 **1828条记录的 `current_status` 是 `optimized` 或 `differentiated`**，但它们的 `workflow_state` 仍然是 `step1_read_original`。两个字段语义矛盾。

### 7.5 改进建议

1. **修复 scan_and_import.py**: 在导入时根据 `is_differentiated` 设置正确的 `workflow_state`
   - 已差异化 → `completed` 或 `step10_uploaded`
   - 未差异化 → `step1_read_original`

2. **修复 register_skill()**: 增加 `workflow_state` 参数

3. **编写迁移脚本**: 为现有1848条记录根据 `current_status` 和 `is_differentiated` 回填 `workflow_state`

4. **启用 workflow_states 表**: 在发现流水线的每个阶段调用 `update_workflow_state()`，实现真正的10步追踪

---

## 八、其他发现

### 8.1 影子skill（无versions记录）

```
没有 versions 记录的 skill 总数: 1
  skill-production-standards | source=original_creation | status=optimized | wf=step1_read_original
```

`skill-production-standards` 由 `update_v2_and_report.py` 创建，但该脚本没有插入 `versions` 记录，导致版本追踪缺失。

### 8.2 上传覆盖率严重不足

```
总差异化skill: 1887
已差异化但未上传成功: 1785
```

**94.5%的差异化skill未上传到任何平台**。这可能不是工作流问题，而是有意为之（分批上传策略），但需要确认。

### 8.3 错误信息不完整

skillhub 失败记录的错误信息均为 `{"success": false`（被截断），无法判断具体失败原因。`record_upload()` 函数的 `error_message` 参数可能未完整保存API响应。

### 8.4 platform_uploads 缺少唯一约束

`NAMING_CONVENTION.md` 第114行提到"platform_uploads缺唯一约束 | 重复记录"。数据库查询证实存在重复记录（如 `linear-workflow-bot` 有3条相同的失败记录），说明同一skill同一版本可能被重复上传。

---

## 九、改进建议汇总

### 9.1 高优先级（P0）

| 编号 | 问题 | 建议 | 涉及文件 |
|------|------|------|---------|
| P0-1 | 缺少 GOVERNANCE_TRIGGER.md | 创建治理触发文档 | 新建 `GOVERNANCE_TRIGGER.md` |
| P0-2 | workflow_state 字段大面积失效 | 修复 scan_and_import.py 和 register_skill()，编写迁移脚本回填 | `scan_and_import.py`, `db.py` |
| P0-3 | 上传无重试机制 | 在 upload 函数中增加指数退避重试（3次），实现 retry-failed 命令 | `update_mechanism.py` |
| P0-4 | 质量检查未集成到流水线 | 在发现流水线阶段3和阶段4之间增加质量验证步骤 | `auto_discover.py`, `update_mechanism.py` |

### 9.2 中优先级（P1）

| 编号 | 问题 | 建议 | 涉及文件 |
|------|------|------|---------|
| P1-1 | 差异化方法论与命名规范冲突 | 统一slug命名规则，移除方法论中的"-pro"建议 | `deep-differentiation-methodology.md` |
| P1-2 | 方法论文档位置不规范 | 移至 `d:\skills\skill-registry\` 目录 | 文件移动 |
| P1-3 | auto_discover.py import 未真正导入 | 实现 DB 写入逻辑 | `auto_discover.py` |
| P1-4 | 错误信息被截断 | 完整保存API响应 | `update_mechanism.py` |
| P1-5 | workflow_states 表未启用 | 在发现流水线各阶段调用 update_workflow_state() | `auto_discover.py`, `update_mechanism.py` |
| P1-6 | 八大维度评分无自动化 | 编写评分脚本，集成到质量门禁 | 新建 `quality_score.py` |

### 9.3 低优先级（P2）

| 编号 | 问题 | 建议 | 涉及文件 |
|------|------|------|---------|
| P2-1 | platform_uploads 缺唯一约束 | 添加 UNIQUE(skill_id, version, platform) 约束 | `db.py` |
| P2-2 | skill-production-standards 无versions记录 | 补录版本记录 | 数据修复 |
| P2-3 | 付费版上传依赖人工浏览器 | 探索 session cookies 自动刷新方案 | `update_mechanism.py` |

---

## 十、工作流完整性最终评估

### 10.1 理想工作流 vs 实际工作流

**理想工作流（设计层面）**:
```
触发 → 扫描 → 去重 → 差异化改造 → 质量验证 → DB录入 → 双版本生成 → 上传 → 状态追踪 → 汇报
```

**实际工作流（执行层面）**:
```
触发 → 扫描 → 去重 → 差异化改造 → [缺失质量验证] → [DB录入需人工] → 双版本生成 → 上传[无重试] → [状态追踪失效] → 汇报
```

### 10.2 完整度评分

| 环节 | 设计完整度 | 执行完整度 | 差距 |
|------|-----------|-----------|------|
| 触发机制 | 67% (2/3) | 67% | 缺治理触发文档 |
| 扫描+去重 | 100% | 100% | 无 |
| 差异化改造 | 90% | 70% | 方法论文档位置/冲突 |
| 质量验证 | 30% | 10% | 仅有去标识检查，未集成 |
| DB录入 | 80% | 40% | import命令未实现 |
| 双版本生成 | 100% | 100% | 无 |
| 上传 | 70% | 50% | 无重试，付费版需人工 |
| 状态追踪 | 90% | 5% | workflow_state失效 |
| 汇报 | 100% | 100% | 无 |

**综合完整度: 约 60%** — 架构设计完善，但工程化落地和自动化程度不足。

---

## 附录：评估依据文件清单

| 文件 | 路径 | 用途 |
|------|------|------|
| UPDATE_TRIGGER.md | `d:\skills\skill-registry\UPDATE_TRIGGER.md` | 更新触发文档 |
| DISCOVER_TRIGGER.md | `d:\skills\skill-registry\DISCOVER_TRIGGER.md` | 发现触发文档 |
| NAMING_CONVENTION.md | `d:\skills\skill-registry\NAMING_CONVENTION.md` | 命名规范与系统设计 |
| deep-differentiation-methodology.md | `d:\skills\deep-differentiation-methodology.md` | 差异化改造方法论 |
| update_mechanism.py | `d:\skills\skill-registry\update_mechanism.py` | 更新机制主控脚本 |
| auto_discover.py | `d:\skills\skill-registry\auto_discover.py` | 自动发现脚本 |
| clean_naming.py | `d:\skills\skill-registry\clean_naming.py` | 命名治理脚本 |
| db.py | `d:\skills\skill-registry\db.py` | 数据库操作封装 |
| scan_and_import.py | `d:\skills\skill-registry\scan_and_import.py` | 扫描导入脚本 |
| init_baseline.py | `d:\skills\skill-registry\init_baseline.py` | 基线初始化 |
| check_debranding.py | `d:\skills\skill-registry\check_debranding.py` | 去标识检测 |
| analyze_status.py | `d:\skills\skill-registry\analyze_status.py` | 状态分析 |
| github_scanner.py | `d:\skills\skill-registry\github_scanner.py` | GitHub扫描器 |
| update_v2_and_report.py | `d:\skills\skill-registry\update_v2_and_report.py` | V2上传记录 |
| skill-registry.db | `d:\skills\skill-registry.db` | SQLite数据库 |
