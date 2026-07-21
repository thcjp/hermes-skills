# Skill生产/改造模块 架构审查报告

> 审查日期: 2026-07-20
> 审查范围: pricing_engine.py, upload_gate.py, market_monitor.py, skill_batch_upgrader_v3.py, trace_llm_scorer.py
> 审查方法: staff-engineer-mode / architecture-decisions 专家指导
> 审查阶段: 维护期既有系统审查

---

## Context (上下文)

本系统是一套位于 `d:\skills\skill-registry\` 的 Python 脚本集合，服务于"Skill商业化发布"全生命周期：评分 -> 合规修复 -> 定价 -> 市场监控 -> 上传门控。5 个模块总计约 3500 行代码，共享一个 SQLite 数据库 `d:\skills\skill-registry.db` 和一批 SKILL.md 文件。当前形态是"脚本拼装型"架构——每个模块是独立 CLI，彼此通过文件系统和数据库隐式耦合，没有显式契约层。

## Goals And Non-Goals (目标与非目标)

| Type | Statement | Evidence | Owner |
| --- | --- | --- | --- |
| Goal | 让每个 SKILL.md 通过评分+合规+定价门控后可发布 | upload_gate.py 的 gate 命令 | 用户 + 本地脚本 |
| Goal | 基于 market research 自动定价 | pricing_engine.py 的 price-all | 用户 + 本地脚本 |
| Goal | 监控竞品市场指导定价和开发 | market_monitor.py 的 report/recommend | 用户 + 本地脚本 |
| Goal | 批量合规修复 | skill_batch_upgrader_v3.py 的 fix | 用户 + 本地脚本 |
| Non-Goal | 分布式/多租户 | 单机 SQLite + 本地文件 | - |
| Non-Goal | 实时定价调整 | 定价矩阵为硬编码常量 | - |
| Non-Goal | 在线支付/收入追踪 | 无相关代码 | - |

## Bounded Contexts (限界上下文)

| Context | Responsibility | Model/Language | Interfaces | Owned Data |
| --- | --- | --- | --- | --- |
| 评分 (trace_llm_scorer) | 计算 TRACE 五维度分数 | 0-10 维度分 + A/B/C/D 等级 | CLI + scores 表 | scores 表 |
| 合规修复 (upgrader_v3) | 30 项合规检查 + 自动修复 | pass/fail + fix 列表 | CLI + SKILL.md 文件 | SKILL.md 文件 |
| 定价 (pricing_engine) | 多维矩阵计算定价 | 价格分层 + 系数 | CLI + skills 表 + SKILL.md | pricing_report.json |
| 市场监控 (market_monitor) | 竞品扫描 + 趋势分析 | 竞品 skill 数据 | CLI + JSON 文件 | market-data/*.json |
| 上传门控 (upload_gate) | 发布前最终检查 | BLOCKER/WARN | CLI + DB + 文件 | gate_report.json |

| Context | Upstream | Downstream | Translation Surface |
| --- | --- | --- | --- |
| 评分 | SKILL.md 文件 | 上传门控 (查 scores 表) | scores 表字段语义错位（见风险 R1） |
| 合规修复 | SKILL.md + v2 模块 | 上传门控 (重复检查) | 检查项重叠无统一规则源 |
| 定价 | SKILL.md + 硬编码矩阵 | 上传门控 (查 suggested_price) | pricing_engine 与 upgrader 的 categorize 重复 |
| 市场监控 | SkillHub API + 手工录入 | 定价引擎 (理应反哺但未实现) | 类别映射不一致（见风险 R5） |
| 上传门控 | 评分 + 合规 + 定价 + 文件 | 发布决策 | 聚合层，无独立数据 |

## System Map (系统地图)

| Element | Data Flow | Dependency | Trust Boundary | Responsibility |
| --- | --- | --- | --- | --- |
| pricing_engine | 硬编码矩阵 -> SKILL.md + DB | skills 表, SKILL.md | 本地单机 | 双写无事务 |
| upload_gate | DB(scores) + SKILL.md -> gate_report | scores 表, skills 表, 文件 | 本地单机 | 聚合检查无幂等性 |
| market_monitor | SkillHub API -> JSON 文件 | 外部 API, JSON 文件 | 外部网络 | 数据孤岛不入库 |
| upgrader_v3 | SKILL.md -> SKILL.md (原地改) | v2 模块, DB, 文件 | 本地单机 | 无备份无回滚 |
| trace_llm_scorer | SKILL.md + 手工 LLM -> scores 表 | DB, 临时导出文件 | 本地单机 | 字段映射错位 |

## Interaction Style (交互风格)

| Interaction | Style | Why This Style | Failure Behavior | Backward Compatibility |
| --- | --- | --- | --- | --- |
| 评分 -> 门控 | 同步 DB 查询 (隐式) | 简单直接 | 查无评分则 BLOCKER | 无版本协商 |
| 定价 -> SKILL.md | 同步文件覆写 | 脚本习惯 | 覆写失败无回滚 | 覆盖旧字段 |
| 市场扫描 -> JSON | 批量一次性写入 | 离线脚本 | API 失败即停止 | 无增量更新 |
| 合规修复 -> SKILL.md | 同步原地覆写 | 脚本习惯 | 中途失败部分修改 | 不可逆 |

**问题**: 所有交互都是同步文件/DB 操作，没有事件、没有批处理幂等性、没有失败隔离。`upgrader_v3.auto_fix` 在 1000 个 skill 上跑，第 500 个抛异常会留下 500 个已改 + 500 个未改的撕裂状态。

---

## 架构问题清单 (按严重程度排序)

### R1 [Critical] 数据库 Schema 语义错位 — scores 表字段名与实际语义不符

**位置**: `trace_llm_scorer.py` save_trace_score (L342-363) + `upload_gate.py` get_trace_score (L163-172)

**问题**: scores 表复用了一套通用字段名来存 TRACE 五维度，但映射关系与字段名完全不符：

| 数据库字段名 | 字面语义 | 实际存的内容 | 查询方读取为 |
| --- | --- | --- | --- |
| debranding_score | 去品牌化分 | Trust 分 | trust |
| quality_score | 质量分 | Reliability 分 | reliability |
| practicality_score | 实用性分 | Adaptability 分 | adaptability |
| simplicity_score | 简洁性分 | Convention 分 | convention |
| performance_score | 性能分 | Effectiveness 分 | effectiveness |
| differentiation_score | 差异化分 | (又存一份 trust) | differentiation |
| compliance_score | 合规分 | (又存一份 trust) | compliance |

这意味着：任何不熟悉这套隐式映射的人查询 scores 表都会得到错误结论；`upload_gate.py` 又用 `sc.differentiation_score` 和 `sc.compliance_score` 做维度阈值检查（L310-313），实际上检查的是两份重复的 trust 分。这是一个会静默产生错误决策的架构缺陷。

**改进建议**:
1. 新建 `trace_scores` 表，字段名与 TRACE 维度一一对应：`trust_score, reliability_score, adaptability_score, convention_score, effectiveness_score, total_score, grade`。
2. 写迁移脚本把旧 scores 表的 trace_llm 行迁移过去。
3. 废弃 scores 表中的 trace_llm 记录或保留只读视图。

**优先级**: P0 — 错误数据会直接导致门控误判。

---

### R2 [Critical] 数据双写一致性缺失 — pricing_engine 同时写文件和 DB 无事务

**位置**: `pricing_engine.py` cmd_apply (L406-484) + cmd_update_db (L487-527)

**问题**: 定价信息有两个真理来源——SKILL.md 的 frontmatter (`suggested_price, pricing_tier, pricing_rationale`) 和 skills 表的同名列。`cmd_apply` 写文件，`cmd_update_db` 写数据库，两者是独立命令，无事务、无版本号、无对账。

实际风险场景：
- 运行 `apply` 后 `update-db` 前被人编辑了 SKILL.md -> DB 覆盖新值，文件是旧值。
- `apply` 成功 `update-db` 中途异常 -> 部分行更新，部分未更新。
- `upload_gate.check_pricing` 只读 SKILL.md frontmatter（L330），不读 DB；但 `market_monitor.load_our_skills` 只读 DB（L202），不读文件。两个模块对"同一个 skill 的价格"可能给出不同答案。

**改进建议**:
1. 确立单一真理来源（建议 DB 为准，SKILL.md 仅作发布产物）。
2. 或者引入 `pricing_version` 字段，写时带版本，读时校验版本一致。
3. 合并 `apply` 和 `update-db` 为一个原子命令，先写 DB 事务，再写文件，文件失败则回滚 DB。

**优先级**: P0 — 数据不一致会直接污染下游所有分析。

---

### R3 [Critical] 硬编码绝对路径 — 系统完全不可移植

**位置**: 全部 5 个文件

**问题**:
- `DB_PATH = r"d:\skills\skill-registry.db"` 在 5 个文件中重复出现。
- `Path(r"d:\skills\packaged-skills\skillhub")` 等目录在 pricing_engine/upload_gate/upgrader_v3/trace_llm_scorer 中各出现 2-4 次。
- `trace_llm_scorer.py` 的 `EXPORT_DIR` 硬编码到 `c:\Users\thcd\.trae-cn\work\...`（一个特定用户的临时目录），这会把中间产物路径污染进源码。

**改进建议**:
1. 新建 `config.py` 或 `paths.py`，集中所有路径常量，从环境变量或 `.env` 读取。
2. `EXPORT_DIR` 改为 `tempfile.gettempdir() / "trace_eval"` 或可配置输出目录。

**优先级**: P0 — 阻塞任何迁移/协作/部署。

---

### R4 [High] 职责严重重叠 — 检查规则与分类逻辑在多文件重复且不一致

**位置**: 多处

**问题**:

| 重复内容 | 出现位置 | 不一致点 |
| --- | --- | --- |
| `MARKETING_KEYWORDS` 字典 | pricing_engine.py L85-104, upgrader_v3.py L77-96 | upgrader 版多了 'programming','brand','storage' 等词 |
| `categorize_skill` 函数 | pricing_engine.py L115-124, upgrader_v3.py L629-646 | 签名不同（一个多 body 参数），返回默认值不同（'效率工具' vs None） |
| 保留词检查 | upgrader_v3.py L142-162, trace_llm_scorer.py L212-220, upload_gate.py L57-59 | 三处各自维护 RESERVED_WORDS 列表 |
| 夸大词检查 | upgrader_v3.py L39-50, trace_llm_scorer.py L226 | 两处各自维护 EXAGGERATION 列表 |
| 硬编码凭证检查 | upgrader_v3.py L66-74, trace_llm_scorer.py L200-208, upload_gate.py L82-87 | 三处模式列表不同 |
| description 长度检查 | upgrader_v3.py L353-377, upload_gate.py L242-245, trace_llm_scorer.py L187-196 | 三处各自实现 |
| displayName 长度检查 | upgrader_v3.py L280-295, upload_gate.py L229-231 | 两处独立实现 |
| frontmatter 解析 | pricing_engine.py L194-220, upload_gate.py L120-148, upgrader_v3.py (用 v2 的 parse_skill_md), trace_llm_scorer.py L173-235 | 四套解析逻辑 |

后果：修复一个 bug 需要改 3-4 个地方，漏改一个就产生行为分歧。例如夸大词列表在 upgrader 和 trace_scorer 中如果不同步，会出现"门控放行但评分扣分"或反之的矛盾。

**改进建议**:
1. 抽取 `skill_core/` 共享包：`parser.py` (frontmatter 解析), `classifier.py` (分类), `rules.py` (保留词/夸大词/凭证模式), `checks.py` (通用检查函数)。
2. upload_gate 和 upgrader_v3 都调用 `checks.py`，规则只有一份。
3. pricing_engine 和 upgrader_v3 都调用 `classifier.py`，分类只有一份。

**优先级**: P1 — 不修复则 bug 修不完。

---

### R5 [High] 类别映射不一致 — 市场监控数据无法反哺定价

**位置**: `pricing_engine.py` CATEGORY_BASE_PRICE (L39-58) vs `market_monitor.py` CATEGORY_MAPPING (L44-56)

**问题**: 两个模块用了完全不同的类别体系：

| pricing_engine 类别 | market_monitor 类别 | 状态 |
| --- | --- | --- |
| 视频音频 | 视频制作 | 名称不同 |
| 翻译 | 翻译国际化 | 名称不同 |
| 数据库 | 数据分析 (合并) | 归并不同 |
| 无 | 财务法务 | pricing 无此类 |
| 无 | 教育学习 | pricing 无此类 |

`market_monitor.generate_recommendations` 试图用 `our['category']`（来自 pricing_engine 的 18 类）去匹配 `category_prices`（来自 market_monitor 的归一化类别），但两套类别名对不上，导致"无竞品数据"的判断大量误报，定价建议失效。

**改进建议**:
1. 建立统一的 `categories.yaml`，定义权威类别列表。
2. pricing_engine 和 market_monitor 都从该文件加载。
3. market_monitor 的 CATEGORY_MAPPING 改为"原始标签 -> 权威类别"的归一化映射，不再自定义类别名。

**优先级**: P1 — 直接破坏"市场数据指导定价"的核心价值流。

---

### R6 [High] 无共享核心层 — 5 个模块各自重复基础设施

**位置**: 全部 5 个文件

**问题**: 没有任何共享的 core/common 模块。以下基础设施在多文件重复：
- 数据库连接（5 个文件各自 `sqlite3.connect(DB_PATH)`，无连接池、无上下文管理器）
- BOM 处理（`if content.startswith('\ufeff'): content = content[1:]` 出现 20+ 次）
- frontmatter 分割（`re.split(r'^---\s*$', ...)` 出现 6+ 次）
- 字段提取（`re.search(rf'^{field}:\s*["\']?(.+?)["\']?\s*$', ...)` 出现 15+ 次）
- 路径遍历 packaged skills（4 个文件各自遍历 skillhub + opensource 目录）

**改进建议**: 新建 `skill_core/` 包：
```
skill_core/
  __init__.py
  config.py        # 路径、DB、常量
  db.py            # 连接管理、上下文管理器
  skill_md.py      # 解析、字段提取、BOM 处理
  paths.py         # packaged skills 路径发现
  classifier.py    # 分类逻辑
  rules.py         # 检查规则常量
```

**优先级**: P1 — 是 R4 的根因，修 R4 必然要先修 R6。

---

### R7 [High] 数据孤岛 — 市场数据存 JSON 不入库

**位置**: `market_monitor.py` (market-data/*.json)

**问题**: 市场监控数据全部存为 JSON 文件（skillhub_latest.json, manual_entries.json, market_report_*.json, recommendations_*.json），不入数据库。而定价、评分、skill 元数据都在 DB。后果：
- 市场数据无法用 SQL 与定价数据 join 查询。
- 历史趋势无法追溯（每次 scan 覆盖 latest）。
- `load_market_data` 用 `seen_names` 去重（L168-193），name 重复但 platform 不同会被错误去重。
- JSON 文件无 schema 校验，手工编辑 manual_entries.json 易出错。

**改进建议**:
1. 新建 `market_skills` 表和 `market_snapshots` 表（带 scanned_at 时间戳）。
2. scan 结果入库，保留历史快照支持趋势分析。
3. recommendations 也入库，可追踪建议是否被采纳。

**优先级**: P1 — 阻塞"数据驱动定价"能力。

---

### R8 [High] 批量修复无备份无回滚 — 单点失败导致撕裂状态

**位置**: `skill_batch_upgrader_v3.py` auto_fix (L871-943) + cmd_fix (L1046-1093)

**问题**: `auto_fix` 直接对 SKILL.md 原地覆写（如 `fix_reserved_words` L437-496 直接 `skill_md_path.write_text`），无备份、无 dry-run、无事务、无回滚。`cmd_fix` 在循环中对 N 个 skill 调用 auto_fix，任何一个抛异常只影响当前 skill（因为 auto_fix 内部有 try/except pass），但 `fix_summary_style_description` 等函数内没有 try/except，一旦异常会中断整个循环。

更严重的是 `fix_reserved_words` 用正则替换 frontmatter，如果 SKILL.md 格式异常（如 description 是单行而非 block），正则可能误伤其他字段，且不可逆。

**改进建议**:
1. 每次修改前 `shutil.copy2` 备份到 `.skill_backup/` 目录。
2. 引入 dry-run 模式，先输出 diff 再确认。
3. cmd_fix 用 try/except 包裹每个 skill，记录失败列表，最后输出报告。
4. 提供 `rollback` 命令从备份恢复。

**优先级**: P1 — 一次误操作可能毁掉几十个 SKILL.md。

---

### R9 [Medium] 模块间隐式依赖 — 无显式契约

**位置**: `skill_batch_upgrader_v3.py` L29-34 import v2; `upload_gate.py` 隐式依赖 scores 表 schema

**问题**:
- `upgrader_v3.py` 通过 `from skill_batch_upgrader_v2 import ...` 依赖 v2 模块，但 v2 不在审查范围，其 API 稳定性未知。如果 v2 重构 `parse_skill_md` 或 `optimize_description`，v3 静默 break。
- `upload_gate.py` 的 `get_trace_score` 依赖 scores 表的 `score_type != 'baseline'` 过滤（L170），这个过滤逻辑与 `trace_llm_scorer.py` 的写入逻辑（只写 `trace_llm` 类型）隐式耦合。如果 trace_llm_scorer 改了 score_type 命名，upload_gate 会查不到评分。
- `pricing_engine` 的 `cmd_update_db` 用 `ALTER TABLE skills ADD COLUMN` 动态加列（L507-508），假设 skills 表已存在且结构兼容，但没有任何 schema 版本校验。

**改进建议**:
1. v2 和 v3 合并为单文件或明确版本契约（在 v2 顶部标注 `# API STABLE: do not change signatures of parse_skill_md, optimize_description`）。
2. scores 表的 score_type 枚举值定义为常量，upload_gate 和 trace_llm_scorer 共享。
3. 引入 schema migration 脚本，启动时校验版本。

**优先级**: P2。

---

### R10 [Medium] 无配置管理 — 阈值全部硬编码

**位置**: 全部 5 个文件

**问题**: 所有关键阈值散落代码中：
- `upload_gate.py`: MIN_TRACE_SCORE=42, MAX_SKILL_MD_LINES=500, MIN_DESCRIPTION_LEN=150
- `pricing_engine.py`: CATEGORY_BASE_PRICE 18 个类别的 min/max/base
- `upgrader_v3.py`: EXAGGERATION_MAP, RESERVED_WORDS, description 150-280 范围

调整任何阈值都要改代码、重启脚本，无法在不同环境（测试/生产）用不同配置，无法 A/B 测试定价参数。

**改进建议**: 抽取 `config.yaml` 或 ` thresholds.yaml`，所有模块启动时加载。

**优先级**: P2 — 影响 R11 的 A/B 测试能力。

---

### R11 [Medium] LLM 评分是手动导出/导入 — 无法规模化

**位置**: `trace_llm_scorer.py` cmd_export + cmd_import

**问题**: LLM 评分流程是：`static` 算静态分 -> `export` 导出 JSON 批次 -> 人工用外部 LLM 评估 -> `import` 导入结果。这是一个 manual batch process，无法自动化：
- 每新增一个 skill 都要手动跑 export -> 手动喂给 LLM -> 手动 import。
- 导出文件存到 `EXPORT_DIR = c:\Users\thcd\.trae-cn\work\...`（特定用户临时目录），团队协作时路径不可用。
- 无 LLM 调用记录、无重试、无结果校验（import 不验证 JSON schema）。

**改进建议**:
1. 集成实际 LLM API 调用（带重试、超时、成本预算）。
2. EXPORT_DIR 改为可配置输出目录。
3. import 时校验 JSON schema，拒绝非法结果。

**优先级**: P2 — 阻塞规模化但当前可手动跑。

---

### R12 [Medium] 无并发控制 — 文件/DB 竞态

**位置**: 全部 5 个文件

**问题**: 多个模块可能同时操作同一个 SKILL.md（如 upgrader_v3 在 fix 的同时 pricing_engine 在 apply），没有文件锁。SQLite 默认的并发模型在多进程写时可能 `database is locked`。`cmd_fix` 和 `cmd_apply` 都没有 `BEGIN TRANSACTION`。

**改进建议**:
1. 文件操作用 `filelock` 库加锁。
2. DB 写操作用 `with conn:` 上下文管理事务。
3. 长批次操作时定期 commit 避免大事务。

**优先级**: P2 — 单人使用时低风险，多人协作时必爆。

---

### R13 [Low] 错误处理不充分 — 静默吞异常

**位置**: `upgrader_v3.py` auto_fix L923 `except Exception: pass`; `market_monitor.py` fetch_json 只 print 不 raise

**问题**: 大量 `except Exception: pass` 或 `except Exception as e: print(...)`，错误被静默吞掉或只 print 不记录。`upgrader_v3.auto_fix` 的 description 优化失败直接 `pass`（L923-924），用户不知道哪些 skill 修复失败、为什么失败。

**改进建议**:
1. 失败记录到结果列表，最终输出失败报告。
2. 引入 `logging` 模块替代 print，支持日志级别和文件输出。

**优先级**: P3。

---

### R14 [Low] 无日志系统 — 全用 print

**位置**: 全部 5 个文件

**问题**: 所有输出用 `print()`，无结构化日志、无级别、无文件持久化。`upload_gate.cmd_check_all` 把报告存 JSON 但运行日志只到 stdout。事后排查问题只能靠记忆。

**改进建议**: 引入 `logging`，配置 `FileHandler` 写到 `logs/{module}_{date}.log`。

**优先级**: P3。

---

### R15 [Low] 无测试

**位置**: 全部 5 个文件

**问题**: 没有看到任何 `test_*.py` 或 `tests/` 目录。`categorize_skill`、`calculate_price`、`static_check` 等纯函数非常适合单元测试，但没有覆盖。正则解析逻辑（frontmatter、description block）极易出错，无测试保护下改一行可能坏一片。

**改进建议**:
1. 为纯函数（分类、定价计算、静态检查、frontmatter 解析）写单元测试。
2. 为 cmd_* 命令写集成测试（用临时 DB + 临时 SKILL.md）。
3. 把测试加入 CI，每次改规则必须跑测试。

**优先级**: P3 — 但在修 R4/R6 重构时必须先补测试。

---

### R16 [Low] 市场监控 API 不稳定且无重试

**位置**: `market_monitor.py` scan_skillhub (L77-149)

**问题**: `fetch_json` 只 try 一次，失败返回 None。`scan_skillhub` 遇到 None 直接 break（L98-99），导致部分页数据丢失但报告显示"扫描完成"。`scan-coze` 直接是 `print("Coze扫描功能开发中...")`（L608），是空壳。

**改进建议**:
1. fetch_json 加重试（3 次，指数退避）。
2. scan 失败时记录失败页，继续后续页，最终报告失败页。
3. scan-coze 要么实现要么从 CLI 移除避免误导。

**优先级**: P3。

---

## Runtime Dependency Adoption (运行时依赖采纳)

| Dependency | Capability | Alternative | Failure Mode | Timeout/Retry/Fallback | Adoption Criteria |
| --- | --- | --- | --- | --- | --- |
| SQLite (skill-registry.db) | 元数据/评分/定价存储 | 文件 JSON | locked/corrupt | 无重试 | 单机够用但不支持并发 |
| SkillHub API | 竞品市场数据 | 手工录入 manual_entries | HTTP 错误/限流 | 无重试, break 退出 | 数据源单一无冗余 |
| skill_batch_upgrader_v2 | v3 复用的解析/优化函数 | 自行实现 | import 失败 | 无 | 隐式依赖无契约 |
| SKILL.md 文件系统 | 唯一可发布产物 | 无 | 并发写撕裂 | 无 | 无备份无回滚 |
| 外部 LLM (手动) | R/A/E 维度评分 | 仅静态分 | 手动流程断链 | 无 | 不可规模化 |

## Risks (风险登记)

| Risk | Likelihood | Impact | Mitigation | Responsibility Path | Evidence | Decision Record |
| --- | --- | --- | --- | --- | --- | --- |
| R1 scores 字段语义错位 | High | High (门控误判) | 迁移到 trace_scores 表 | 用户 + DB 迁移脚本 | trace_llm_scorer L342-363 | 待决策 |
| R2 双写不一致 | Medium | High (定价数据污染) | 单一真理源 + 事务 | 用户 + pricing_engine 重构 | pricing_engine L406-527 | 待决策 |
| R3 硬编码路径 | High | Medium (不可迁移) | config.py + 环境变量 | 用户 | 全部文件 | 待决策 |
| R4 规则重复不一致 | High | Medium (行为分歧) | 抽取 skill_core | 用户 | 多文件对比 | 待决策 |
| R5 类别映射不一致 | High | High (建议失效) | 统一 categories.yaml | 用户 | pricing vs monitor 对比 | 待决策 |
| R8 批量修复无回滚 | Medium | High (文件毁损) | 备份 + dry-run + rollback | 用户 | upgrader_v3 auto_fix | 待决策 |
| R12 无并发控制 | Low (单人) | Medium (数据撕裂) | filelock + 事务 | 用户 | 全部文件 | 待决策 |

## Fitness Functions (适应度函数)

| Invariant | Metric Or Rule | Threshold | Measurement Source | Cadence | Failure Response | Local Check Path |
| --- | --- | --- | --- | --- | --- | --- |
| 定价数据一致 | SKILL.md price == DB price | 0 不一致 | 对账脚本 | 每次 apply 后 | 报告差异并阻断 | `python check_pricing_consistency.py` |
| 类别集合统一 | pricing 类别集 == monitor 类别集 | 集合相等 | categories.yaml 加载校验 | 启动时 | 拒绝启动 | `python -c "from skill_core import validate_categories"` |
| 检查规则单一来源 | RESERVED_WORDS 等常量只定义一次 | import 计数==1 | grep + ast 检查 | CI | 阻断合并 | `pytest tests/test_single_source.py` |
| 修复可回滚 | 每个 fix 有对应 backup | 100% 覆盖 | 备份目录扫描 | 每次 fix 后 | 报告未备份项 | `python check_backups.py` |
| scores 字段语义正确 | 字段名 == 语义 | 100% | schema 校验 | 迁移后 | 阻断 | `pytest tests/test_scores_schema.py` |

## Decision Table (决策表)

| Decision | Default | Rejected Alternatives | Exception Conditions |
| --- | --- | --- | --- |
| 单一真理源选 DB | DB 为准, SKILL.md 为发布产物 | 文件为准 (查询慢); 双写 (当前, 不一致) | 发布产物必须从 DB 生成 |
| 共享 core 包 | 抽取 skill_core/ | 每个脚本自包含 (当前, 重复); 完全服务化 (过度工程) | 单机脚本无需微服务 |
| 统一类别 | categories.yaml 权威 | pricing 内嵌 (当前); monitor 自定义 (当前) | 新增类别必须改 yaml |
| scores 表迁移 | 新建 trace_scores 表 | 复用 scores 加注释 (语义仍错); 视图 (写复杂) | 保留旧表只读 |
| 批量修复安全 | 备份 + dry-run + rollback | 直接覆写 (当前, 危险); git 兜底 (SKILL.md 可能未提交) | 无 |

---

## 商业目标 ("赚钱") 支持度评估

### 核心结论: 当前架构**不足以**稳定支持"赚钱"目标

"赚钱"需要的数据闭环是：**市场数据 -> 定价决策 -> 发布 -> 用户反馈 -> 定价调整**。当前架构在这个闭环上有 4 处断裂：

#### 断裂 1: 市场数据无法反哺定价 (R5 + R7)
- market_monitor 用 JSON 文件存数据，不入库，无法与 pricing_engine 的定价数据 join。
- 两套类别名对不上，`generate_recommendations` 的"建议降价/涨价"判断大量失效。
- 市场数据无历史快照，无法看趋势。
- **后果**: 定价是"拍脑袋 + 静态矩阵"，不是"数据驱动"。

#### 断裂 2: 无收入追踪与反馈闭环
- 整个系统没有"实际收入/下载量/转化率"的数据接入点。
- pricing_engine 计算的是"suggested_price"（建议价），没有"actual_price"（实际成交价）字段。
- 没有"定价调整后收入变化"的 A/B 测试能力（R10 阈值硬编码）。
- **后果**: 无法回答"这个 skill 定价 9.9 还是 19.9 赚得多"这个核心问题。

#### 断裂 3: 评分无法规模化 (R11)
- LLM 评分是手动 export/import，每新增一个 skill 需要人工跑全流程。
- 静态评分只覆盖 T+C 两维，R+A+E 必须靠 LLM。
- 上传门控要求 TRACE >= 42（upload_gate MIN_TRACE_SCORE=42），但大量 skill 只有静态分（远低于 42），卡在门控外。
- **后果**: skill 上线速度瓶颈在人工 LLM 评分，无法快速扩品。

#### 断裂 4: 发布管道脆弱 (R2 + R8)
- 定价双写不一致可能导致发布的 SKILL.md 价格与 DB 不符。
- 批量修复无回滚，一次误操作可能毁掉几十个待发布 skill。
- 无并发控制，多人协作时数据撕裂。
- **后果**: 发布过程不可靠，可能上线错误定价或损坏的 skill。

### 改进优先级路线图

**P0 (立即修，阻断商业化的根本问题)**:
1. R1 scores 表迁移 — 修复门控误判
2. R2 定价双写统一 — 修复数据污染
3. R3 硬编码路径 — 支持环境隔离

**P1 (1-2 周内修，打通数据闭环)**:
4. R5 + R7 统一类别 + 市场数据入库 — 打通"市场 -> 定价"链路
5. R4 + R6 抽取 skill_core — 消除重复，为后续扩展打底
6. R8 批量修复加备份回滚 — 保护发布管道

**P2 (1 个月内修，提升规模化能力)**:
7. R10 配置化管理 — 支持 A/B 测试定价
8. R11 LLM 评分自动化 — 解锁扩品速度
9. R9 + R12 显式契约 + 并发控制 — 支持团队协作

**新增建议 (架构缺失能力)**:
- 新增 `revenue_tracker.py` 模块：接入实际下载量/收入数据，与定价决策关联。
- 新增 `pricing_ab_test.py` 模块：支持对不同 skill 试不同定价，追踪收入差异。
- 新增 `feedback_loop.py` 模块：收集用户评分/退款数据，反哺定价矩阵调整。

---

## Follow-Up Routes (后续路由)

1. **dependency-resilience**: market_monitor 的 SkillHub API 调用和 trace_llm_scorer 的 LLM 调用需要重试/超时/降级策略。
2. **testing-and-quality-gates**: 在重构 R4/R6 前，必须先为核心纯函数（分类、定价计算、frontmatter 解析）补单元测试，否则重构会引入回归。

---

## 总结

当前架构是"脚本拼装型"——5 个独立 CLI 通过文件系统和数据库隐式耦合，没有共享核心层、没有显式契约、没有数据一致性保障。它在"单人手动跑通一次流程"的场景下勉强可用，但要支持"赚钱"这个商业目标——意味着需要数据驱动定价、规模化扩品、可靠发布——存在 3 个 Critical 和 5 个 High 级架构缺陷。

最优先要修的不是某个 bug，而是**建立共享核心层 (skill_core) 和单一真理源**，否则后续每加一个功能都会加剧重复和不一致。建议按 P0 -> P1 -> P2 路线图推进，并在重构前先补核心函数的单元测试。
