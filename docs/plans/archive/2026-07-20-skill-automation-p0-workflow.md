---
intent: 修复Skill自动化流水线P0级阻断问题, 使体系能稳定自动化产出"审核必过且真可运行"的skill
success_criteria: 4个P0任务全部通过单skill试跑验证, 质量门禁能挡住slug不一致/超长/缺字段等审核必拒问题, import能写DB, 上传失败能自动重试, 门禁集成到流水线
risk_level: medium
auto_approve: false
created_at: 2026-07-20
based_on: 前一轮FRAMEWORK_ADR.md + WORKFLOW_INTEGRITY_REPORT.md + architecture_review_report.md分析
---

# Skill自动化流水线 P0修复工作流

> **前一轮分析依据**:
> - `skill-registry/FRAMEWORK_ADR.md` (5个ADR, 6个框架缺陷)
> - `skill-registry/WORKFLOW_INTEGRITY_REPORT.md` (综合完整度60%, 5处断点)
> - `skill-registry/architecture_review_report.md` (3个Critical + 5个High)
> - 数据库核实: 1917条skill, workflow_states仅981条, 11条上传失败无重试
> - 代码核实: auto_discover.py L419 cmd_import()不写DB, update_mechanism.py L592无retry
> - 抽样核实: ai-video-director slug≠name≠folder, 2个SKILL.md超500行

## 核心原则

1. **小规模试点**: 每个任务只用1个skill验证, 通过后再扩展
2. **实事求是**: 所有验证基于实际运行结果, 不虚假实现
3. **不引入新bug**: 修改前先读取原代码, 修改后先试跑再确认
4. **可追溯**: 每个任务有明确的验收标准和证据

## P0-1: 质量门禁集成

- [ ] **Step 1.1: 编写quality_gate.py**
action: 在d:\skills\skill-registry\quality_gate.py新建质量门禁脚本, 集成check_debranding.check_skill_md() + 新增6项检查(slug==name==folder一致性, 行数≤500, frontmatter 8必需字段, displayName≤20字符, summary≤100字符, tools为YAML数组). 输出JSON报告+终端友好输出. 任一fail则总体fail.
loop: false
verify: python d:\skills\skill-registry\quality_gate.py --help 能正常显示帮助
gate: auto

- [ ] **Step 1.2: 对ai-artist-workstation试跑(应基本通过)**
action: 运行 python quality_gate.py d:\skills\packaged-skills\skillhub\ai-artist-workstation\SKILL.md
loop: false
verify: 输出JSON报告, ai-artist-workstation大部分检查pass(可能行数接近500但未超)
gate: auto

- [ ] **Step 1.3: 对ai-video-director试跑(应被挡住)**
action: 运行 python quality_gate.py d:\skills\packaged-skills\skillhub\ai-video-director\SKILL.md
loop: false
verify: 输出JSON报告, ai-video-director的slug==name==folder检查fail(slug=ai-video-studio-pro≠name=ai-video-director), 行数检查fail(531>500), 总体fail
gate: auto

- [ ] **Step 1.4: 记录试跑结果到报告**
action: 将两个skill的试跑结果保存到d:\skills\skill-registry\quality_gate_test_report.json, 对比预期与实际
loop: false
verify: 报告文件存在, 包含两个skill的完整检查结果
gate: human

## P0-2: import写DB

- [ ] **Step 2.1: 修改db.py register_skill()接受workflow_state参数**
action: 读取db.py L299 register_skill()当前签名, 增加workflow_state=None参数, 插入时使用该值或默认'step1_read_original'
loop: false
verify: python -c "from db import register_skill; import inspect; print(inspect.signature(register_skill))" 显示新参数
gate: auto

- [ ] **Step 2.2: 修改auto_discover.py cmd_import()调用register_skill()**
action: 读取auto_discover.py L419 cmd_import(), 在print指导信息前调用register_skill()写入DB, 设置workflow_state='step1_read_original'
loop: false
verify: 准备1个测试候选skill, 运行cmd_import, 查询DB确认记录存在
gate: auto

- [ ] **Step 2.3: 端到端验证发现→DB录入**
action: 选1个候选skill, 运行scan→dedup→import完整流程, 确认DB有记录
loop: false
verify: SELECT * FROM skills WHERE slug=<测试slug> 返回记录, workflow_state='step1_read_original'
gate: human

## P0-3: 上传重试机制

- [ ] **Step 3.1: 修改upload_free_via_cli()增加重试**
action: 读取update_mechanism.py L592 upload_free_via_cli(), 增加指数退避重试(3次, 1s/2s/4s), 区分可重试错误(returncode!=0或timeout)与不可重试错误(protected slug)
loop: false
verify: 代码审查确认重试逻辑正确, 无语法错误
gate: auto

- [ ] **Step 3.2: 完整保存API响应**
action: 修改result['stdout']/result['stderr']去掉[:2000]截断, 完整保存
loop: false
verify: 代码审查确认无截断
gate: auto

- [ ] **Step 3.3: 对1个失败skill试重试**
action: 从DB查1个skillhub fail记录(如linear-workflow-bot), 运行upload命令, 观察重试行为
loop: false
verify: 重试日志显示3次尝试, 最终结果记录到DB
gate: human

## P0-4: 质量门禁集成到流水线

- [ ] **Step 4.1: 在update_mechanism.py upload命令前调用quality_gate**
action: 读取update_mechanism.py upload相关函数, 在上传前调用quality_gate.check_skill_md(), 不通过则返回'blocked_by_quality_gate'
loop: false
verify: 对ai-video-director运行upload命令, 应被门禁挡住, 不执行上传
gate: auto

- [ ] **Step 4.2: 更新DISCOVER_TRIGGER.md插入质量门禁步骤**
action: 在DISCOVER_TRIGGER.md阶段3与阶段4之间插入"阶段3.5: 质量验证", 引用quality_gate.py
loop: false
verify: 文档审查确认新增步骤
gate: human

- [ ] **Step 4.3: 端到端验证1个skill完整流程**
action: 选1个skill, 运行质量门禁→generate→upload完整流程, 确认门禁工作
loop: false
verify: 质量门禁pass的skill能正常上传, fail的skill被挡住
gate: human

## 完成标准

- [x] P0-1: quality_gate.py能挡住ai-video-director的slug不一致和超长问题 (2026-07-20完成)
- [x] P0-2: cmd_import()能写DB, DB有记录 (2026-07-20完成)
- [x] P0-3: upload_free_via_cli()有重试逻辑, 失败skill能自动重试 (2026-07-20完成)
- [x] P0-4: upload命令前有门禁, 不通过则阻止上传 (2026-07-20完成)
- [x] 所有修改不引入新bug, 不破坏现有功能 (向后兼容验证通过)
- [x] 每个任务有实际运行证据(非声称)

## P0阶段完成记录 (2026-07-20)

### P0-1: 质量门禁集成 ✓
- 新建: `d:\skills\skill-registry\quality_gate.py` (10项检查)
- 修复: frontmatter块标量(|-)解析bug, 重写为状态机模式
- 验证: ai-artist-workstation 10/10通过, ai-video-director被挡住(slug不一致+532行>500)
- 证据: `quality_gate_test_report.json` + `quality_gate_test_report_video.json`

### P0-2: import写DB ✓
- 修改: `db.py register_skill()` 增加`workflow_state`参数(默认None→'step1_read_original')
- 修改: `auto_discover.py cmd_import()` 调用`register_skill()`写入DB(付费版+免费版)
- 验证: 测试候选skill成功写入2条记录(skill_id=1918/1919, wf_state正确), 测试数据已清理
- 向后兼容: scan_and_import.py的关键字参数调用不受影响

### P0-3: 上传重试机制 ✓
- 修改: `update_mechanism.py upload_free_via_cli()` 增加指数退避重试(1s/2s/4s)
- 新增: 不可重试错误模式(protected/already exists/slug conflict/unauthorized等)
- 修复: stdout/stderr完整保存(去掉[:2000]截断)
- 验证: 对linear-workflow-bot真实测试2次重试, 退避1.0s, 错误正确分类, stderr完整109字符
- 发现环境问题: WSL bash不可用(execvpe /bin/bash failed), 影响CLI上传(非重试机制问题)

### P0-4: 质量门禁集成到流水线 ✓
- 修改: `sync_skill_to_platform()` 上传前调用`quality_gate.run_quality_gate()`
- 新增: `skip_quality_gate`参数(仅调试用), 阻止时记录到DB(blocked_by_quality_gate)
- 更新: `DISCOVER_TRIGGER.md` 插入"阶段3.5: 质量验证"
- 验证: ai-video-director被挡住(blocked_by_quality_gate, DB有记录), ai-artist-workstation通过(10/10)

## P0阶段验证总结

| 任务 | 验收标准 | 结果 | 证据 |
|------|---------|------|------|
| P0-1 | 挡住slug不一致+超长 | ✓ | ai-video-director 2项fail |
| P0-2 | import写DB | ✓ | 2条记录写入, wf_state正确 |
| P0-3 | 重试机制工作 | ✓ | 2次重试, 退避1.0s, 完整保存 |
| P0-4 | 门禁集成到上传 | ✓ | blocked_by_quality_gate, DB记录 |

## 待解决问题(非P0范围, 记录供后续处理)

1. **WSL bash不可用**: skillhub CLI通过WSL调用bash, 但`/bin/bash`不存在. 需修复WSL或改用原生调用(Git Bash/PowerShell)
2. **9条历史fail记录**: cdp-browser-master/cron-guard/linear-workflow-bot各3次失败, 待WSL修复后重试
3. **ai-video-director等不合规skill**: 需批量修复slug不一致+超长问题(属于P1-3批量修复安全范围)

## P1-1: 共享core层 ✓ (2026-07-20完成)

### 实施内容
- 新建 `d:\skills\skill-registry\skill_core\` 目录
- 创建4个模块:
  - `__init__.py`: 统一导出
  - `parser.py`: frontmatter解析(从quality_gate.py迁移parse_frontmatter, 状态机模式)
  - `rules.py`: 阈值/必需字段/占位符/夸大词/不可重试错误模式(单一来源)
  - `db.py`: DB路径+get_db()连接函数(支持环境变量SKILL_REGISTRY_DB)
  - `checks.py`: 9个通用检查函数(slug一致性/行数/字段/displayName/summary/tools/尖括号/占位符/夸大词)
- 重构 `quality_gate.py`: 从skill_core导入, 不再自带重复实现(保留去标识化检查, 因依赖外部check_debranding.py)

### 验证结果
| skill | P0-1结果 | P1-1结果 | 一致性 |
|-------|---------|---------|--------|
| ai-artist-workstation | 10/10 PASS | 10/10 PASS | ✓ |
| ai-video-director | 8/10 FAIL | 8/10 FAIL | ✓ |
| linear-workflow-bot | (新测试) | 10/10 PASS | N/A |

- `update_mechanism.py` import正常(门禁集成未受影响)
- CLI退出码正确(FAIL→1)
- 报告: `p1_1_consistency_report.json`

### 架构改善
- 消除规则重复: PLACEHOLDER_PATTERNS/EXAGGERATION_WORDS从2处→1处(rules.py)
- 消除解析重复: parse_frontmatter从1处→1处(parser.py, 供后续其他模块复用)
- 消除DB路径硬编码: 从5处→1处(db.py, 支持环境变量)
- 仅迁移quality_gate.py(试点), 其他模块后续逐步迁移(遵循小规模原则)
