# 技能自动化系统全面修复计划 v3

> 基于实际代码深度审计，非文档承诺。4个 Explore 子代理并行审计（管道完整性/质量门控/数据库追踪/冗余文件）。
> 制定日期：2026-07-25
> 前序：v2计划已完成第1轮(C1-C4关键崩溃)和第2轮(H1-H2质量门控)，本v3基于修复后的最新代码状态重新审计。

---

## 进度总览

| 轮次 | 目标 | 状态 | 预计改动文件数 |
|------|------|------|---------------|
| 第1轮 | P0-1~P0-3 关键管道断裂修复 | ✅ 已完成并验证 | 4 |
| 第2轮 | Q1-Q5 质量门控有效性修复 | ✅ 已完成并验证 | 3 |
| 第3轮 | D1-D3 数据库追踪链路修复 | ✅ 已完成并验证 | 3 |
| 第4轮 | D4-D6 DB写入收口与历史保护 | ✅ 已完成并验证 | 5 |
| 第5轮 | A1-A3 生成质量与运维闭环 | ⬜ 待执行 | 5 |
| 第6轮 | L1-L8 冗余文件清理 | ⬜ 待执行 | 删除~34MB |

---

## 一、痛点分析（基于代码事实）

### 痛点1：管道"看似连通，实则三处断裂"

| 断裂点 | 文件:行号 | 后果 |
|--------|----------|------|
| 发现→入库断裂 | `auto_discover.py:370` | 扫描结果只写candidates.json，不入DB，需手动import |
| 付费上传是stub | `update_mechanism.py:702-714` | `upload_paid_via_api`只生成payload文件返回`payload_ready`，不实际上传 |
| 每日同步永dry-run | `daily_sync.py:121` | `step_sync_clawhub`硬编码`--dry-run`，ClawHub永不实际上传 |

### 痛点2：质量门"13项检查，5项形同虚设"

| 问题 | 文件:行号 | 后果 |
|------|----------|------|
| description阈值与SSOT不一致 | `rules.py:13-14`(50-300) vs `project_config.py:115-116`(150-280) | 过短/过长description通过门禁 |
| 占位符检测覆盖不足 | `rules.py:26-35` | 遗漏`待填充/TBD/xxx/HACK/[PLACEHOLDER]`等10+种 |
| 夸大词列表不一致 | `rules.py:39-42` vs `generate_skill.py:622` | `终极/完美/顶级/极致`未被门禁检查 |
| 去标识化medium级不阻止上传 | `quality_gate.py:76` | `author:/created by/MCP`等medium问题通过 |
| 第三套检查实现 | `trace_llm_scorer.py:155-274` | 完全独立于skill_core，自维护规则 |

### 痛点3：数据库"有骨架无血脉"

| 问题 | 实测验证 | 后果 |
|------|---------|------|
| 发现→入库数据断链 | `sources JOIN skills`结果=0（4587条发现记录成孤岛） | 无法追溯skill来源 |
| Schema漂移 | 实际DB比db.py多7列（runtime ALTER TABLE添加） | 新环境init后缺列报错 |
| 40+处裸SQL | 14个文件绕过db.py业务函数 | 字段填充不一致，事务混乱 |
| 2处DELETE销毁历史 | `agent_trial.py:389`, `batch_l2_eval.py:146` | 评分历史丢失 |
| 平台命名混乱 | `skillhub` vs `skillhub_free/paid`混用 | 统计遗漏 |

### 痛点4：运维"检测不修复，开环不闭环"

| 问题 | 文件:行号 | 后果 |
|------|----------|------|
| ops闭环实为报告生成器 | `ops闭环.py:173-209` | 检测到问题不触发修复 |
| L2验证未自动化 | `llm_validator.py:254-357` | 只生成prompt，需人工执行 |
| L3/L4实为静态检查 | `l3_function_checker.py:400`, `l4_task_gate.py:494` | 非真实运行，是模式匹配 |

### 痛点5：34MB冗余文件堆积

| 类别 | 大小 | 说明 |
|------|------|------|
| 3个DB备份 | 29.97MB | data/backups/下旧快照 |
| 76个.pyc文件 | 1.18MB | 3个__pycache__目录 |
| 3个0字节文件 | 0 | 异常空文件 |
| 版本化旧脚本 | ~260KB | diff_batch_fix.py v1/v2等 |
| 791个生成报告 | ~2.45MB | data/reports/下 |

---

## 二、完整问题清单

### P0 - 关键管道断裂（系统不可用）- 已全部修复 ✅

| 编号 | 文件:行号 | 问题 | 影响 | 状态 |
|------|----------|------|------|------|
| P0-1 | `daily_sync.py:121` | `step_sync_clawhub`硬编码`--dry-run`，ClawHub每日同步永不实际上传 | 运维管道断裂 | ✅ 已修复 |
| P0-2 | `update_mechanism.py:702-714` | `upload_paid_via_api`是stub，只生成payload返回`payload_ready`；payload未写入磁盘 | 付费版上传不可用 | ✅ 已修复（含payload落盘bug修复） |
| P0-3 | `db.py:40-67` | `init_database()`缺少5列（suggested_price/pricing_category等），由`pricing_engine.py:546-550`运行时ALTER TABLE补齐 | 新环境初始化后缺列报错 | ✅ 已修复 |

### Q - 质量门控失效（门禁形同虚设）- 已全部修复 ✅

| 编号 | 文件:行号 | 问题 | 影响 | 状态 |
|------|----------|------|------|------|
| Q1 | `rules.py:13-14` | description阈值(50-300)与SSOT `project_config.py:115-116`(150-280)不一致 | 不合格description通过 | ✅ 已修复 |
| Q2 | `rules.py:26-35` | PLACEHOLDER_PATTERNS遗漏`待填充/TBD/xxx/HACK/[PLACEHOLDER]`等10+种 | 占位符漏检 | ✅ 已修复 |
| Q3 | `rules.py:30-32` | 模板占位符`能力1[::]`仅匹配字面"1"，不匹配"能力2:"等 | 模板残留漏检 | ✅ 已修复 |
| Q4 | `rules.py:39-42` | 夸大词列表与`generate_skill.py:622`不一致，缺`终极/完美/顶级/极致` | 夸大词漏检 | ✅ 已修复 |
| Q5 | `quality_gate.py:76` | `check_debranding`仅HIGH级判fail，medium级(`author:/MCP`)通过 | 去标识化不彻底 | ✅ 已修复 |

### D - 数据库追踪断裂（数据不可信）- D1-D3已修复 ✅

| 编号 | 文件:行号 | 问题 | 影响 | 状态 |
|------|----------|------|------|------|
| D1 | `multi_source_discover.py:214` vs `db.py`register_skill | sources.original_slug与skills.source_slug编码规则不一致，JOIN结果=0 | 4587条发现记录成孤岛 | ✅ 已修复（469条已关联） |
| D2 | `db.py:104-116` | operations表实际无FOREIGN KEY约束（代码有定义，实际DB缺失） | 参照完整性无保障 | ✅ 已修复（52/52连接开启PRAGMA，含20个额外文件补全） |
| D3 | `db.py:165-178` | sources表无skill_id外键字段 | 无法直接关联发现→skill | ✅ 已修复（skill_id列+backfill） |
| D4 | 18个文件/45处(不含db.py 14处) | 裸INSERT/UPDATE绕过db.py业务函数 | 字段不一致，事务混乱 | ⚠️ 部分完成（D5+D6已修复3个文件，剩余15个文件待分批处理） |
| D5 | `agent_trial.py:389`, `batch_l2_eval.py:146`, `trace_llm_scorer.py:371-397` | DELETE/UPDATE-in-place销毁评分历史 | 评分趋势丢失 | ✅ 已修复（is_current版本化标记，历史保留验证通过） |
| D6 | `update_mechanism.py:226-248` | `record_upload`与`db.py:602-634`同名重复实现，参数不同 | 调用错版本丢字段 | ✅ 已修复（删除重复实现，7处调用改为db_record_upload+error_message=） |

### A - 架构与运维（闭环不闭合）

| 编号 | 文件:行号 | 问题 | 影响 |
|------|----------|------|------|
| A1 | `generate_skill.py:490-589` | 生成无LLM调用，纯模板填充，`llm_generated`标志名不副实 | 生成质量低 |
| A2 | `ops闭环.py:173-209` | "闭环"实为报告生成器，检测到问题不触发修复 | 运维开环 |
| A3 | `trace_llm_scorer.py:155-274` | 完全独立于skill_core，第三套检查实现，硬编码路径(line 676/681) | 违反单一来源原则 |

### L - 冗余文件清理

| 编号 | 位置 | 问题 | 可释放 |
|------|------|------|--------|
| L1 | 3个`__pycache__` | 76个`.pyc`文件 | ~1.2MB |
| L2 | `data/skill-registry.db`, `data/skills.db` | 0字节空文件 | 0 |
| L3 | `tools/parse_report.py` | 0字节空脚本 | 0 |
| L4 | `data/backups/` | 3个旧DB备份 | ~30MB |
| L5 | `data/reports/` | 旧版本报告(dedup_all_v36/fix_missing_fields_v36/v46/diff_fix_report/diff_fix2_report) | ~3.4MB |
| L6 | `tools/` | 版本化旧脚本(diff_batch_fix.py v1/v2, l3_batch_fix.py, l4_batch_fix.py, update_v2_and_report.py) | ~200KB |
| L7 | `data/reports/` | 791个generation_report（评估去重） | ~2.45MB |
| L8 | `docs/plans/` | 旧版prompt文件整理 | ~530KB |

---

## 三、修改计划任务清单（6轮）

### 设计原则
1. **小规模验证**：每轮只改3-6个文件，改完立即用3个真实skill验证
2. **依赖有序**：P0(管道通) → Q(门禁准) → D(数据可信) → A(架构优) → L(清理)
3. **禁止mock/TODO/pass/fallback**
4. **每轮输出下一轮提示词**

---

### 第1轮：P0 关键管道断裂修复（3个文件）

**目标**：修复3处使系统不可用的关键断裂。

| 任务 | 文件 | 修复内容 |
|------|------|---------|
| P0-1 | `daily_sync.py:121` | 移除`--dry-run`硬编码，改为配置项控制 |
| P0-2 | `update_mechanism.py:702-714` | `upload_paid_via_api`改为调用`enterprise_uploader.py`的真实上传逻辑 |
| P0-3 | `db.py:40-67` | 将7个缺失列加入`init_database()`建表语句 |

**验证**：3个skill走完发现→入库→上传（free+paid）全流程

---

### 第2轮：Q1-Q5 质量门控有效性修复（4个文件）

**目标**：修复5项使质量门形同虚设的问题。

**当前状态分析（基于实际代码）**：

| 任务 | 文件 | 当前状态 | 需修复内容 |
|------|------|---------|-----------|
| Q1 | `rules.py:13-14` | ❌ `MIN_DESCRIPTION_LEN=50, MAX_DESCRIPTION_LEN=300`，与SSOT `project_config.py:118-119`(150-280)不一致 | 改为从project_config导入 |
| Q2 | `rules.py:26-35` | ❌ 缺`待填充/待完善/待确定/TBD/xxx/XXX/HACK/[PLACEHOLDER]` | 补全（generate_skill.py:628有`待填充/待完善/待确定/TBD/xxx/XXX`） |
| Q3 | `rules.py:30-32` | ❌ `能力1[::]`仅匹配字面"1" | 改为`能力\d+[::]`支持任意数字 |
| Q4 | `rules.py:39-42` | ❌ 缺`终极/完美/第一/顶级/极致/最好` | 合并generate_skill.py:622的完整列表 |
| Q5 | `quality_gate.py:76` | ❌ `passed = len(high_issues) == 0`，medium级通过 | 改为medium级也判fail |

**验证**：3个skill质量门检查，对比修复前后结果差异

---

## 四-2、第2轮修改提示词（Q1-Q5）

```
任务: 修复5项质量门控失效问题（Q1-Q5）

背景: 质量门13项检查中5项形同虚设，导致不合格skill通过门禁。
前序H1-H2已修复VERSION_PATTERN和frontmatter链接占位符检查，本轮修复剩余5项。

执行步骤(小规模, 3个skill验证):

【Q1】修复 rules.py:13-14 description阈值与SSOT不一致
1. 读取 rules.py 第8-14行，确认当前 MIN_DESCRIPTION_LEN=50, MAX_DESCRIPTION_LEN=300
2. 读取 project_config.py 第118-119行，确认 SSOT 值为 MIN_DESCRIPTION_LEN=150, MAX_DESCRIPTION_LEN=280
3. 修改: rules.py 删除硬编码值，改为从project_config导入:
   from project_config import MIN_DESCRIPTION_LEN, MAX_DESCRIPTION_LEN
   （注意: rules.py 当前不导入project_config，需添加sys.path设置）
4. 验证: python -c "from skill_core.rules import MIN_DESCRIPTION_LEN; print(MIN_DESCRIPTION_LEN)" 输出150

【Q2】修复 rules.py:26-35 PLACEHOLDER_PATTERNS遗漏
1. 读取 rules.py 第26-35行，确认当前8条模式
2. 读取 generate_skill.py 第628行，确认生成时清除的占位符: 待补充/待填充/待完善/待确定/TODO/TBD/FIXME/xxx/XXX
3. 修改: 在PLACEHOLDER_PATTERNS中补全缺失模式:
   - (r'待填充', '占位符-待填充')
   - (r'待完善', '占位符-待完善')
   - (r'待确定', '占位符-待确定')
   - (r'TBD', '占位符-TBD')
   - (r'xxx', '占位符-xxx')
   - (r'XXX', '占位符-XXX')
   - (r'HACK', '占位符-HACK')
   - (r'\[PLACEHOLDER\]', '占位符-PLACEHOLDER标记')
4. 验证: 构造含"待填充/TBD/xxx"的测试文本，确认被check_no_placeholders检测到

【Q3】修复 rules.py:30-32 模板占位符正则不匹配数字变量
1. 读取 rules.py 第30-32行，确认当前: 能力1[::] / 场景1[::] / 步骤1[::] 仅匹配字面"1"
2. 读取 generate_skill.py 第634-637行，确认生成时用 re.sub(r'能力(\d+):', ...) 匹配任意数字
3. 修改: 将3条模式改为支持任意数字:
   - (r'能力\d+[::]', '占位符-能力N模板')
   - (r'场景\d+[::]', '占位符-场景N模板')
   - (r'步骤\d+[::]', '占位符-步骤N模板')
4. 验证: 构造含"能力2:"和"步骤3::"的测试文本，确认被检测到

【Q4】修复 rules.py:39-42 夸大词列表不完整
1. 读取 rules.py 第39-42行，确认当前10个词: 万能/超级/最强/最佳/最完美/最专业/全球首发/业界第一/独一无二/绝无仅有
2. 读取 generate_skill.py 第622行，确认生成时清除10个词: 最佳/最强/万能/超级/终极/完美/第一/顶级/极致/最好
3. 修改: 合并两个列表为完整集（去重后15个词）:
   EXAGGERATION_WORDS = [
       '万能', '超级', '最强', '最佳', '最完美', '最专业',
       '全球首发', '业界第一', '独一无二', '绝无仅有',
       '终极', '完美', '第一', '顶级', '极致', '最好',
   ]
4. 验证: 构造含"终极/完美/顶级/极致"的测试文本，确认被检测到

【Q5】修复 quality_gate.py:76 check_debranding medium级不阻止上传
1. 读取 quality_gate.py 第66-87行，确认 check_debranding 函数
2. 确认第76行: passed = len(high_issues) == 0 （仅HIGH级fail）
3. 修改: 改为 passed = len(issues) == 0 （HIGH+medium都fail）
   注意: 保留severity字段用于报告区分级别，但passed判断包含所有级别
4. 验证: 对含medium级去标识化问题(如author:)的skill运行quality_gate，确认overall_passed=False

验收标准:
- rules.py的description阈值从project_config导入，值为150-280
- PLACEHOLDER_PATTERNS包含全部占位符模式（≥15条）
- 模板占位符正则支持任意数字（\d+）
- EXAGGERATION_WORDS包含generate_skill.py的全部夸大词（≥15个）
- check_debranding的medium级问题也判fail
- 3个skill(ad-creative-intel-free/agentvibes-skill-free/agent-assistant-free)质量门检查结果与P0验证一致或更严格
- 不引入新bug，不改变现有行为（除修复的5处外）

约束:
- 禁止 mock/TODO/pass/fallback
- 每步修改后立即语法检查 python -m py_compile
- rules.py导入project_config需正确设置sys.path（参考quality_gate.py的导入方式）
- 完成第2轮后，输出第3轮提示词（D1-D3 数据库追踪链路修复）
```

---

### 第3轮：D1-D3 数据库追踪链路修复（3个文件）

**目标**：修复发现→入库数据断链，使4587条发现记录不再成孤岛。

**当前状态分析（基于实际代码）**：

| 任务 | 文件 | 当前状态 | 需修复内容 |
|------|------|---------|-----------|
| D1 | `multi_source_discover.py:196-234` | ❌ `record_source_to_db`写`sources.original_slug=candidate['source_id']`，但`register_skill`写`skills.source_slug=source_slug参数`，两者编码规则不同，JOIN=0 | sources表增加skill_id字段，record_source_to_db在skill已注册时关联skill_id |
| D2 | `db.py:128-141` | ⚠️ operations表有FK定义但SQLite默认不强制FK，`PRAGMA foreign_keys=ON`仅当前连接有效 | 在get_db()中统一开启PRAGMA foreign_keys=ON（已有但需确认所有连接） |
| D3 | `db.py:189-203` | ❌ sources表无skill_id字段，无法直接关联发现→skill | sources表增加skill_id INTEGER字段+FK约束，ALTER TABLE迁移 |

**验证**：`SELECT COUNT(*) FROM sources s JOIN skills sk ON s.skill_id = sk.id` > 0

---

## 四-3、第3轮修改提示词（D1-D3）

```
任务: 修复3处数据库追踪链路断裂（D1-D3）

背景: 数据库sources表(4587条发现记录)与skills表无有效关联，JOIN结果=0。
sources.original_slug与skills.source_slug编码规则不一致，且sources表无skill_id外键。

执行步骤(小规模, 3个skill验证):

【D1+D3】修复 sources表增加skill_id字段 + record_source_to_db关联
1. 读取 db.py 第189-203行，确认 sources 表建表语句（当前无skill_id字段）
2. 读取 multi_source_discover.py 第196-234行，确认 record_source_to_db 实现:
   - 当前: INSERT INTO sources (..., original_slug, ...) VALUES (..., candidate['source_id'], ...)
   - 不调用 register_skill，不关联 skill_id
3. 修改 db.py:
   a. sources表CREATE TABLE增加: skill_id INTEGER
   b. 增加: FOREIGN KEY (skill_id) REFERENCES skills(id)
   c. 增加ALTER TABLE迁移: ALTER TABLE sources ADD COLUMN skill_id INTEGER
4. 修改 multi_source_discover.py record_source_to_db:
   a. INSERT时增加skill_id字段
   b. 写入前查询 skills 表: SELECT id FROM skills WHERE source_slug = ? OR slug = ?
      参数: candidate['source_id'], candidate['source_id']+'-free', candidate['source_id']+'-pro'
   c. 若找到skill_id，写入sources.skill_id; 若未找到，skill_id=NULL（待后续register_skill时回填）
5. 增加 backfill_source_skill_id() 函数:
   - UPDATE sources SET skill_id = (SELECT id FROM skills WHERE source_slug = sources.original_slug)
   - WHERE sources.skill_id IS NULL
   - 在 init_database() 末尾调用
6. 验证: SELECT COUNT(*) FROM sources s JOIN skills sk ON s.skill_id = sk.id
   （执行backfill后应 > 0）

【D2】确认所有DB连接开启FK约束
1. 读取 db.py get_db_connection() (project_config.py:158-163)，确认是否有 PRAGMA foreign_keys = ON
2. 读取 db.py get_db() (如果存在)，确认是否有 PRAGMA foreign_keys = ON
3. 搜索所有 sqlite3.connect 调用，确认是否都通过统一函数
4. 修改: 在 project_config.py 的 get_db_connection() 中增加 c.execute("PRAGMA foreign_keys = ON")
   （如果db.py的init_database已有但get_db_connection没有，需补上）
5. 验证: python -c "from project_config import get_db_connection; c=get_db_connection(); print(c.execute('PRAGMA foreign_keys').fetchone())"
   输出应为 (1,)

验收标准:
- sources表包含skill_id字段（新DB通过init_database创建即有）
- record_source_to_db写入时尝试关联skill_id
- backfill_source_skill_id()能回填已有记录
- SELECT COUNT(*) FROM sources s JOIN skills sk ON s.skill_id = sk.id > 0（backfill后）
- 所有DB连接开启PRAGMA foreign_keys = ON
- 3个skill(ad-creative-intel-free/agentvibes-skill-free/agent-assistant-free)验证无回归
- 不引入新bug，不改变现有行为（除修复的3处外）

约束:
- 禁止 mock/TODO/pass/fallback
- 每步修改后立即语法检查 python -m py_compile
- sources表已有数据，ALTER TABLE必须用IF NOT EXISTS模式(try/except)
- backfill用UPDATE而非DELETE+INSERT，保护历史数据
- 完成第3轮后，输出第4轮提示词（D4-D6 DB写入收口与历史保护）
```

---

### 第4轮：D4-D6 DB写入收口与历史保护（3个文件）

**目标**：消除裸SQL，保护历史数据。

**当前状态分析（基于实际代码）**：

| 任务 | 文件 | 当前状态 | 需修复内容 |
|------|------|---------|-----------|
| D4 | 18个文件/59处裸SQL | ⚠️ 大量INSERT/UPDATE绕过db.py业务函数 | 本轮优先修复写入类（D5/D6涉及的3个文件），其余分批后续处理 |
| D5 | `agent_trial.py:389`, `batch_l2_eval.py:146` | ❌ `DELETE FROM scores WHERE skill_id=? AND score_type=?` 销毁评分历史 | 改为版本化标记（新增is_current字段或用created_at排序取最新） |
| D6 | `update_mechanism.py:226-248` | ❌ 自带`record_upload()`与`db.py:513`同名重复，参数不同(update_mechanism用get_db()，db.py用sqlite3.connect) | 删除update_mechanism的重复实现，改为从db.py导入 |

**验证**：评分历史可查（同一skill同一score_type有多条记录），record_upload不再重复

---

## 四-4、第4轮修改提示词（D4-D6）

```
任务: 修复3处DB写入收口与历史保护问题（D4-D6）

背景: 14+个文件绕过db.py业务函数直接写裸SQL，2处DELETE销毁评分历史，
update_mechanism.py与db.py有同名record_upload重复实现。
本轮聚焦3个最关键的文件，其余裸SQL分批后续处理。

执行步骤(小规模, 3个skill验证):

【D5】修复 agent_trial.py:389 + batch_l2_eval.py:146 DELETE销毁评分历史
1. 读取 agent_trial.py 第383-400行，确认: c.execute("DELETE FROM scores WHERE skill_id = ? AND score_type = 'agent_trial'")
2. 读取 batch_l2_eval.py 第140-148行，确认: c.execute("DELETE FROM scores WHERE skill_id = ? AND score_type = 'trace_llm'")
3. 读取 db.py scores表建表语句，确认是否有is_current字段（如果没有需增加）
4. 修改 db.py:
   a. scores表CREATE TABLE增加: is_current INTEGER DEFAULT 1
   b. 增加ALTER TABLE迁移: ALTER TABLE scores ADD COLUMN is_current INTEGER DEFAULT 1
   c. 增加索引: CREATE INDEX IF NOT EXISTS idx_scores_current ON scores(skill_id, score_type, is_current)
5. 修改 agent_trial.py:
   - 将 DELETE 改为: UPDATE scores SET is_current = 0 WHERE skill_id = ? AND score_type = 'agent_trial'
   - 新评分插入时带 is_current = 1
6. 修改 batch_l2_eval.py:
   - 将 DELETE 改为: UPDATE scores SET is_current = 0 WHERE skill_id = ? AND score_type = 'trace_llm'
7. 验证: 对同一skill多次评分，SELECT * FROM scores WHERE skill_id=? 应返回多条记录（is_current=0的历史 + is_current=1的最新）

【D6】修复 update_mechanism.py:226-248 record_upload重复实现
1. 读取 update_mechanism.py 第226-248行，确认自带的record_upload函数
2. 读取 db.py 第602-634行，确认db.py的record_upload函数（参数更完整，含community_published/download_ready）
3. 修改 update_mechanism.py:
   a. 删除第226-248行的record_upload函数
   b. 在文件顶部增加: from db import record_upload as db_record_upload
   c. 将所有调用 record_upload(...) 改为 db_record_upload(...)
   d. 注意参数映射: update_mechanism的record_upload参数(status, http_status, error) vs db.py的(upload_status, http_status, error_message)
4. 验证: grep "def record_upload" update_mechanism.py 应无结果；grep "db_record_upload" 应有调用

【D4-部分】确认裸SQL数量并标记后续处理
1. 统计当前裸SQL: grep -rn "INSERT INTO\|UPDATE.*SET" tools/*.py | grep -v db.py | wc -l
2. 记录数量到修复计划，标记为"第4轮部分完成，剩余分批处理"
3. 不修改其他文件（本轮仅D5+D6）

验收标准:
- scores表包含is_current字段（新DB通过init_database创建即有）
- agent_trial.py和batch_l2_eval.py不再DELETE，改为UPDATE is_current=0
- 同一skill同一score_type可查多条评分记录（历史保留）
- update_mechanism.py不再有record_upload定义，改为从db.py导入
- 3个skill(ad-creative-intel-free/agentvibes-skill-free/agent-assistant-free)验证无回归
- 不引入新bug，不改变现有行为（除修复的3处外）

约束:
- 禁止 mock/TODO/pass/fallback
- 每步修改后立即语法检查 python -m py_compile
- scores表已有数据，ALTER TABLE用try/except模式
- is_current默认1（已有记录自动标记为current）
- 完成第4轮后，输出第5轮提示词（A1-A3 生成质量与运维闭环）
```

---

### 第5轮：A1-A3 生成质量与运维闭环（5个文件）

**目标**：提升生成质量，闭合运维环。

| 任务 | 文件 | 修复内容 |
|------|------|---------|
| A1 | `generate_skill.py:490-589` | 评估LLM API接入方案，或诚实标记为模板生成(非llm_generated) |
| A2 | `ops闭环.py:173-209` | 增加检测→修复→重新验证的闭环逻辑 |
| A3 | `trace_llm_scorer.py:155-274` | 迁移到skill_core，复用parser/rules/checks |

**验证**：ops闭环检测到问题后自动触发修复并重新验证

---

### 第6轮：L1-L8 冗余文件清理

**目标**：释放~34MB空间，规范文件管理。

| 任务 | 操作 | 可释放 |
|------|------|--------|
| L1 | 删除3个__pycache__目录 | ~1.2MB |
| L2-L3 | 删除3个0字节文件 | 0 |
| L4 | 归档后删除3个DB备份 | ~30MB |
| L5 | 删除旧版本报告 | ~3.4MB |
| L6 | 删除版本化旧脚本 | ~200KB |
| L7-L8 | 评估整理生成报告和prompt文件 | ~3MB |

**验证**：项目功能不受影响，磁盘空间释放

---

## 四、第1轮修改提示词（P0-1~P0-3）

```
任务: 修复3处关键管道断裂（P0-1~P0-3）

背景: 4维审计发现自动化管道有3处关键断裂，导致系统不可用：
1. daily_sync.py硬编码--dry-run，ClawHub每日同步永不实际上传
2. update_mechanism.py的upload_paid_via_api是stub，只生成payload不实际上传
3. db.py的init_database()缺少7列，由pricing_engine.py运行时ALTER TABLE补齐，新环境初始化后缺列报错

执行步骤(小规模, 3个skill验证):

【P0-1】修复 daily_sync.py:121 硬编码 --dry-run
1. 读取 daily_sync.py 第116-130行，确认 --dry-run 硬编码位置
2. 修改: 将 --dry-run 改为从配置项读取(如 project_config.py 的 CLAWHUB_DRY_RUN 默认 False)
3. 在 project_config.py 中增加 CLAWHUB_DRY_RUN = False 配置项
4. 验证: python daily_sync.py step clawhub 时不带 --dry-run 参数

【P0-2】修复 update_mechanism.py:702-714 付费版上传stub
1. 读取 update_mechanism.py 第695-720行，确认 upload_paid_via_api 的stub实现
2. 读取 enterprise_uploader.py 第300-410行，确认真实上传逻辑(urlopen Request)
3. 修改: upload_paid_via_api 改为调用 enterprise_uploader.upload_skill() 的真实逻辑
4. 保留payload生成作为备份方案(网络不可用时fallback到payload_ready)
5. 验证: 对1个付费skill调用 upload_paid_via_api，确认发起真实HTTP请求(可先用--dry-run测试)

【P0-3】修复 db.py:40-67 init_database() 缺少7列
1. 读取 db.py 第40-67行，确认 skills 表建表语句
2. 读取 pricing_engine.py 第540-555行，确认 ALTER TABLE 添加的7列:
   suggested_price, pricing_category, pricing_rationale, pricing_tier, is_paid, free_slug, paid_slug
3. 修改: 将7列加入 db.py 的 CREATE TABLE skills 语句中(带默认值)
4. 验证: 在临时目录创建新DB，执行 init_database()，确认所有列存在

验收标准:
- daily_sync.py 的 clawhub 步骤不再硬编码 --dry-run
- update_mechanism.py 的 upload_paid_via_api 调用真实上传逻辑而非返回 payload_ready
- db.py 的 init_database() 包含全部字段，新环境初始化后无需ALTER TABLE
- 3个skill(ad-creative-intel-free/agentvibes-skill-free/agent-assistant-free)验证无回归
- 不引入新bug，不改变现有行为(除修复的3处外)

约束:
- 禁止 mock/TODO/pass/fallback(payload生成仅作为网络不可用时的备份)
- 每步修改后立即语法检查 python -m py_compile
- 完成第1轮后，输出第2轮提示词（Q1-Q5 质量门控有效性修复）
```

---

## 五、关键设计决策

1. **P0-2修复策略**: 不删除payload生成逻辑（它是网络不可用时的合理备份），但主路径必须调用真实上传。payload_ready状态仅作为fallback。
2. **P0-3修复策略**: 将ALTER TABLE的7列直接加入CREATE TABLE，保留ALTER TABLE作为旧环境迁移手段（IF NOT EXISTS）。
3. **Q1修复策略**: rules.py从project_config导入阈值，而非硬编码。这是SSOT原则的正确实现。
4. **分轮依赖**: P0(管道通)是前提 → Q(门禁准)依赖管道通 → D(数据可信)依赖门禁准 → A(架构优)依赖数据可信 → L(清理)放最后。
5. **小规模验证**: 每轮固定用3个skill(ad-creative-intel-free/agentvibes-skill-free/agent-assistant-free)验证，确保无回归。
