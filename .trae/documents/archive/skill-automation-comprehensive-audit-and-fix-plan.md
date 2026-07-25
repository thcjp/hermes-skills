# Skill自动化体系全面审计与修复计划

> 生成时间: 2026-07-25
> 基于代码实际实现核查(非文档承诺)
> 核查范围: d:\skills\tools\ 全部Python文件 + d:\skills\skill-registry.db + d:\skills\ 目录结构

## 一、当前痛点总结

### 核心发现:前几轮P0修复可能存在路径错误

**重要发现**: 实际代码位于 `d:\skills\tools\` 而非 `d:\skills\skill-registry\`。前几轮P0-1~P1-1创建的 `quality_gate.py` 和 `skill_core/` 确实存在于 `d:\skills\tools\` 下(探索确认),但 `update_mechanism.py`、`check_debranding.py`、`auto_discover.py`、`db.py` 也都在 `d:\skills\tools\` 下。需要验证前几轮的修改是否作用于了正确的文件。

### 痛点0: 自动化流水线存在6处致命断链

| 编号 | 文件 | 问题 | 后果 |
|------|------|------|------|
| A1 | `update_mechanism.py` L280/510/521/522 | 引用未定义变量 `DIFFERENTIATED_SKILLS_DIR` | find_skill_md/find_source_skill_md一调用就NameError,上传链路全断 |
| A2 | `skill_batch_upgrader_v3.py` L36-42 | import不存在的`skill_batch_upgrader_v2` | 整脚本ModuleNotFoundError,30项合规检查全不可用 |
| A3 | `check_debranding.py` L243/252 | `r'str(DIFFERENTIATED_DIR)'`是字符串字面量非函数调用; `DATA_DIR`未导入 | 去标识化检查崩溃,quality_gate第1项检查失效 |
| A4 | `trace_llm_scorer.py` L779 | `DATA_DIR`未导入 | 报告生成NameError |
| A5 | `update_mechanism.py` L72 | `SKILLHUB_RUNNER`指向`d:\skills\run-skillhub.sh`,实际在`d:\skills\tools\scripts\` | bash即使存在也找不到脚本 |
| A6 | `update_mechanism.py` L627 | 用`bash`调用`.sh`,Windows上bash不在PATH | WSL bash问题未解决,免费版上传不可用 |

### 痛点1: 质量门禁存在硬编码敷衍

| 编号 | 文件 | 问题 | 后果 |
|------|------|------|------|
| B1 | `skill_core/rules.py` L50 | version正则`^\d+\.\d+\.\d+`缺`$`锚定 | `1.0.0-beta`/`1.0.0.0`/`1.0.0abc`都能通过,version检查形同虚设 |
| B2 | `quality_gate.py` | 遗漏5项SkillHub审核必拒点 | license值不合法/homepage指向开源仓库/硬编码凭证/保留词(claude/anthropic)/摘要式描述 全部漏检 |
| B3 | 3处文件 | 夸大词表有3套不同版本(rules.py 10个/upgrader_v3 10个/trace_llm_scorer 10个,内容各不相同) | 同一skill在不同检查器下结果不同 |
| B4 | `skill_core/rules.py` | 占位符词表过窄,遗漏TBD/XXX/待填充/待实现/replace_here等 | 大量占位符漏检 |
| B5 | `skill_core/checks.py` L174 | `check_no_placeholders`直接`continue`跳过链接检查 | 注释说"仅frontmatter检查"但实际完全不查,实现与注释矛盾 |
| B6 | 2处文件 | description长度阈值不一致(quality_gate 50-300 vs config 150-280) | 同一description在不同检查器下结果不同 |
| B7 | `quality_gate.py` L130 | `overall_passed = all()`导致medium级失败也阻断上传 | 与注释"任一high级fail则总体fail"矛盾 |
| B8 | `skill_core/checks.py` | tools格式检查不校验数组元素 | `tools: [""]`或`tools: [123]`也能通过 |

### 痛点2: 数据库无法可靠跟踪skill全生命周期

| 编号 | 问题 | 影响 |
|------|------|------|
| C1 | 无`review_status`字段 | 审核状态完全无法跟踪(只有upload_status,无pending_review/approved/rejected) |
| C2 | 无`platform_skill_id` | 平台返回的技能ID未记录,无法回查平台端实体 |
| C3 | `current_score` 35%不同步(1002个skill score=0但scores表有分) | 评分写入scores表但未回写skills表 |
| C4 | 1015个skill(35%)在workflow_states表无记录 | 工作流跟踪覆盖不全 |
| C5 | versions表版本号与platform_uploads版本号脱节 | 升级血缘断裂,无法按版本号回溯 |
| C6 | `workflow_states.started_at` 100%为NULL | 无法追踪每步耗时 |
| C7 | `dependencies`表完全空(0行) | 依赖关系跟踪能力存在但无数据采集 |
| C8 | 123个skill的local_path指向不存在的目录 | DB与文件系统不同步 |
| C9 | 654组重复version记录 | versions表有654个完全相同的(skill_id,version,content_hash)多余行 |
| C10 | 52%上传记录http_status为NULL | 上传HTTP状态码半数未采集 |

### 痛点3: 存在虚假实现

| 编号 | 文件 | 问题 |
|------|------|------|
| D1 | `update_mechanism.py` L708 | `upload_paid_via_api`返回`payload_ready`,无真实HTTP调用,付费上传是假的 |
| D2 | `market_monitor.py` L195-206 | `scan_skillhub_via_browser`只print指导信息,return空列表 |
| D3 | `market_monitor.py` L661 | `scan-coze`命令打印"开发中..." |
| D4 | `auto_discover.py` L234 | GitHub扫描只扫仓库根目录,不递归子目录 |
| D5 | `auto_discover.py` L461/484 | import写DB时`local_path=''`空串,后续find_skill_md找不到文件 |

### 痛点4: 架构重复未消除

| 编号 | 问题 |
|------|------|
| E1 | 3套frontmatter解析器(skill_core/parser.py + update_mechanism.py + db.py) |
| E2 | 3套夸大词表(rules.py + upgrader_v3 + trace_llm_scorer) |
| E3 | 2套description长度标准(50-300 vs 150-280) |
| E4 | update_mechanism.py未使用skill_core,仍自带parse_skill_md |

### 痛点5: 冗余文件占用约77MB

| 类别 | 大小 | 说明 |
|------|------|------|
| data/reports历史报告 | ~34.9MB / 988文件 | 确定删除 |
| data/backups DB快照 | ~30.7MB / 3文件 | 需确认 |
| __pycache__ | ~1.2MB | 确定删除 |
| tools/一次性脚本 | ~0.6MB / 20文件 | 确定删除 |
| upload_tracking备份 | ~3.7MB / 3文件 | 确定删除 |

---

## 二、问题清单(按严重级别排序)

### Critical (致命 — 流水线完全不可用)

1. **A1**: update_mechanism.py引用未定义DIFFERENTIATED_SKILLS_DIR → 上传链路全断
2. **A2**: skill_batch_upgrader_v3.py import不存在的v2 → 30项检查全不可用
3. **A3**: check_debranding.py r'str()'字面量bug + DATA_DIR未导入 → 去标识化检查崩溃
4. **A4**: trace_llm_scorer.py DATA_DIR未导入 → 报告生成崩溃
5. **A5**: SKILLHUB_RUNNER路径错误 → bash找不到脚本
6. **B1**: version正则缺$锚定 → version检查形同虚设
7. **B2**: quality_gate遗漏5项审核必拒点 → 不合规skill能通过门禁

### High (严重 — 功能失效或数据不可靠)

8. **A6**: WSL bash不可用 → 免费版上传不可用
9. **B3**: 3套夸大词表不一致 → 检查结果不可靠
10. **B4**: 占位符词表过窄 → 大量漏检
11. **B5**: check_no_placeholders跳过链接检查 → 实现与注释矛盾
12. **B6**: description长度阈值不一致 → 检查结果不可靠
13. **C1**: 无review_status字段 → 审核状态无法跟踪
14. **C3**: current_score 35%不同步 → 评分数据不可靠
15. **C5**: 版本号脱节 → 升级血缘断裂
16. **C8**: 123个local_path失效 → DB与文件系统不同步
17. **D1**: 付费上传是payload_ready占位 → 付费版上传是假的
18. **D5**: import写DB时local_path空串 → 导入后无法进入上传流程

### Medium (中等 — 质量或效率问题)

19. **B7**: overall_passed用all()非high-only → medium级失败也阻断
20. **B8**: tools格式检查不校验元素 → 空元素能通过
21. **C2**: 无platform_skill_id → 无法回查平台端
22. **C4**: 1015个skill无workflow_states → 跟踪覆盖不全
23. **C6**: started_at全NULL → 无法追踪耗时
24. **C9**: 654组重复version记录 → 数据冗余
25. **C10**: 52%上传缺http_status → 状态码未采集
26. **D2/D3**: market_monitor占位实现 → 市场监控不可用
27. **D4**: GitHub扫描不递归 → 漏检严重
28. **E1-E4**: 架构重复未消除 → 维护成本高

---

## 三、修改计划任务清单(分6轮,每轮小规模验证)

### 第1轮: 修复致命断链(Round 1 — Critical Breakages)

**目标**: 让流水线从"完全不可用"变为"基本可运行"

| 任务 | 文件 | 修改内容 | 验证方式 |
|------|------|---------|---------|
| R1-1 | `update_mechanism.py` | 修复DIFFERENTIATED_SKILLS_DIR: 改为从config导入DIFFERENTIATED_DIR或定义别名 | import不报错, find_skill_md能找到1个skill |
| R1-2 | `skill_batch_upgrader_v3.py` | 修复import v2: 将v2的依赖内联或创建v2 shim模块 | python -c "import skill_batch_upgrader_v3"不报错 |
| R1-3 | `check_debranding.py` | 修复L243 r'str()'字面量bug + L252 DATA_DIR导入 | python check_debranding.py能正常运行 |
| R1-4 | `trace_llm_scorer.py` | 修复L779 DATA_DIR导入 | python -c "from trace_llm_scorer import cmd_report"不报错 |
| R1-5 | `update_mechanism.py` | 修复SKILLHUB_RUNNER路径: 改为tools/scripts/run-skillhub.sh | 路径常量指向正确位置 |
| R1-6 | `update_mechanism.py` | 修复bash调用: 检测Windows环境,优先用Git Bash或PowerShell替代 | upload_free_via_cli能找到执行器(不要求上传成功,只要求不FileNotFoundError) |

**验证**: 对1个skill(如ai-artist-workstation)运行 `python quality_gate.py` + `python update_mechanism.py status`,确认不崩溃。

### 第2轮: 修复质量门禁硬编码(Round 2 — Quality Gate Fixes)

**目标**: 让质量门禁从"表面检查"变为"真实有效"

| 任务 | 文件 | 修改内容 | 验证方式 |
|------|------|---------|---------|
| R2-1 | `skill_core/rules.py` | version正则加`$`锚定: `^\d+\.\d+\.\d+$` | `1.0.0-beta`被拒, `1.0.0`通过 |
| R2-2 | `skill_core/rules.py` | 扩充占位符词表: 增加TBD/XXX/待填充/待实现/待完善/replace_here/your-token/示例文本等 | 构造含TBD的SKILL.md, 被检出 |
| R2-3 | `skill_core/rules.py` | 统一夸大词表: 合并3套词表为1套(取并集), 所有模块从rules.py导入 | grep确认只有1处EXAGGERATION_WORDS定义 |
| R2-4 | `skill_core/checks.py` | 修复check_no_placeholders: 实现frontmatter内链接检查(不跳过) | 含`[xxx](yyy)`的frontmatter被检出 |
| R2-5 | `skill_core/checks.py` | 新增check_license_value: 校验license值在合法名单内(MIT/Apache-2.0/Proprietary等) | license=MIT通过, license=Random被拒 |
| R2-6 | `skill_core/checks.py` | 新增check_hardcoded_keys: 检测sk-/AKIA/ghp_/password=/api_key=等 | 含sk-xxx的SKILL.md被拒 |
| R2-7 | `skill_core/checks.py` | 新增check_reserved_words: 检测claude/anthropic/openai/chatgpt保留词 | 含"claude"的SKILL.md被拒 |
| R2-8 | `skill_core/rules.py` | 统一description长度阈值: 从config导入,消除50-300 vs 150-280不一致 | grep确认只有1处description长度定义 |
| R2-9 | `quality_gate.py` | 修复overall_passed: 改为`all(c['passed'] for c in checks if c['severity']=='high')` | medium级失败不阻断, high级才阻断 |
| R2-10 | `quality_gate.py` | 集成R2-5/R2-6/R2-7新检查到run_quality_gate | 13项→16项检查 |

**验证**: 对3个skill(ai-artist-workstation/ai-video-director/linear-workflow-bot)运行quality_gate, 结果符合预期。

### 第3轮: 修复数据库跟踪(Round 3 — DB Tracking Fixes)

**目标**: 让DB从"能记录"变为"能可靠跟踪"

| 任务 | 文件 | 修改内容 | 验证方式 |
|------|------|---------|---------|
| R3-1 | `db.py` | ALTER TABLE platform_uploads ADD COLUMN review_status TEXT | 新字段存在 |
| R3-2 | `db.py` | ALTER TABLE platform_uploads ADD COLUMN platform_skill_id TEXT | 新字段存在 |
| R3-3 | `db.py` | 修复current_score同步: record_score时回写skills.current_score | 对1个skill评分后, skills.current_score与scores.total_score一致 |
| R3-4 | `db.py` | 修复local_path空串: cmd_import时设置正确的local_path(基于slug推断) | import后local_path非空且目录存在 |
| R3-5 | `db.py` | 清理654组重复version记录(保留最新1条) | SELECT COUNT of duplicates = 0 |
| R3-6 | `db.py` | 修复upload_status与http_status矛盾: success但http=500的记录改为failed | 无矛盾记录 |

**验证**: 对1个skill运行完整发现→注册→评分流程, 查询DB确认所有字段正确同步。

### 第4轮: 修复虚假实现(Round 4 — Fix Fake Implementations)

**目标**: 消除所有mock/placeholder/fallback

| 任务 | 文件 | 修改内容 | 验证方式 |
|------|------|---------|---------|
| R4-1 | `update_mechanism.py` | upload_paid_via_api: 实现真实HTTP调用(用requests库), 不再返回payload_ready | 代码审查确认有真实HTTP POST |
| R4-2 | `auto_discover.py` | GitHub扫描: 改为递归扫描(用git tree API或递归列目录) | 能发现子目录下的SKILL.md |
| R4-3 | `auto_discover.py` | cmd_import: 设置正确的local_path(基于source_url或slug推断目录) | import后local_path非空 |
| R4-4 | `market_monitor.py` | scan_skillhub_via_browser: 标注为deprecated或实现真实API调用 | 不再有只print的函数 |

**验证**: grep确认无`payload_ready`/`开发中`/`请在浏览器中`等占位文本。

### 第5轮: 清理冗余文件(Round 5 — File Cleanup)

**目标**: 释放约40MB确定删除 + 确认30MB需确认

| 任务 | 路径 | 操作 | 验证方式 |
|------|------|------|---------|
| R5-1 | `data/reports/` | 删除988个历史报告文件(~34.9MB) | 目录为空或仅保留当前需要的 |
| R5-2 | `tools/__pycache__/` + `skill_core/__pycache__/` | 删除所有.pyc文件(~1.2MB) | 无__pycache__目录 |
| R5-3 | `data/reports/upload_tracking*.backup*` | 删除3个备份文件(~3.7MB) | 无backup文件 |
| R5-4 | `tools/` 一次性脚本 | 删除20个带v36/fix/task/batch_fix后缀的脚本(~0.6MB) | 确认batch_l3_trial.py和batch_l2_eval.py是否仍被引用 |
| R5-5 | `.gitignore` | 添加__pycache__/、*.pyc、data/reports/、data/backups/ | git status不显示这些 |
| R5-6 | `data/backups/` | 确认无回滚需求后删除3个DB快照(~30.7MB) | 用户确认后执行 |

**验证**: 磁盘空间释放, git status干净, 核心功能不受影响。

### 第6轮: 架构统一(Round 6 — Architecture Consolidation)

**目标**: 消除重复实现, 所有模块使用skill_core单一来源

| 任务 | 文件 | 修改内容 | 验证方式 |
|------|------|---------|---------|
| R6-1 | `update_mechanism.py` | 删除自带parse_skill_md, 改为from skill_core.parser import parse_frontmatter | 只有1处frontmatter解析器 |
| R6-2 | `db.py` | 删除自带parse_skill_md, 改为from skill_core.parser import parse_frontmatter | 只有1处frontmatter解析器 |
| R6-3 | `trace_llm_scorer.py` | 夸大词表改为from skill_core.rules import EXAGGERATION_WORDS | 只有1处夸大词定义 |
| R6-4 | `skill_batch_upgrader_v3.py` | 夸大词表改为from skill_core.rules import EXAGGERATION_WORDS | 只有1处夸大词定义 |
| R6-5 | `pricing_engine.py` | description长度阈值改为from skill_core.rules import | 只有1处阈值定义 |

**验证**: grep确认全项目只有1处parse_frontmatter定义、1处EXAGGERATION_WORDS定义、1处description长度阈值定义。

---

## 四、第1轮修改提示词(直接可执行)

```
任务: 修复6处致命断链, 让自动化流水线基本可运行

重要前提: 实际代码路径是 d:\skills\tools\ 不是 d:\skills\skill-registry\

执行步骤(小规模, 每步验证):

R1-1: 修复update_mechanism.py的DIFFERENTIATED_SKILLS_DIR
- 读取 d:\skills\tools\update_mechanism.py 的import部分(约L22-26)和L280/L510附近
- 确认config.py导出的变量名(是DIFFERENTIATED_DIR还是DIFFERENTIATED_SKILLS_DIR)
- 在update_mechanism.py顶部添加: from config import DIFFERENTIATED_DIR as DIFFERENTIATED_SKILLS_DIR
- 或直接将L280/L510/L521/L522的DIFFERENTIATED_SKILLS_DIR改为DIFFERENTIATED_DIR
- 验证: python -c "import update_mechanism; update_mechanism.find_skill_md('ai-artist-workstation')"不报NameError

R1-2: 修复skill_batch_upgrader_v3.py的import v2
- 读取 d:\skills\tools\skill_batch_upgrader_v3.py L36-42, 确认从v2导入了哪些符号
- 检查v2是否真的不存在(Glob d:\skills\tools\skill_batch_upgrader_v2*)
- 如果v2不存在: 将v2的依赖(SECTION_MAP/DOMESTIC_ALTERNATIVES/parse_skill_md等)内联到v3中
  或创建一个最小shim模块skill_batch_upgrader_v2.py提供这些符号
- 验证: python -c "import skill_batch_upgrader_v3"不报ModuleNotFoundError

R1-3: 修复check_debranding.py两个bug
- 读取 d:\skills\tools\check_debranding.py L243和L252
- L243: 将 r'str(DIFFERENTIATED_DIR)' 改为 str(DIFFERENTIATED_DIR) (去掉r前缀和外层引号)
- L252: 确认DATA_DIR的定义位置, 在文件顶部import或定义 DATA_DIR
- 验证: python d:\skills\tools\check_debranding.py 能正常运行不报NameError

R1-4: 修复trace_llm_scorer.py的DATA_DIR
- 读取 d:\skills\tools\trace_llm_scorer.py L35-40(import部分)和L779
- 确认DATA_DIR应该从哪里导入(config.py?)
- 在import部分添加 DATA_DIR 的导入
- 验证: python -c "from trace_llm_scorer import cmd_report"不报NameError

R1-5: 修复SKILLHUB_RUNNER路径
- 读取 d:\skills\tools\update_mechanism.py L72
- 确认run-skillhub.sh的实际位置(Glob d:\skills\**\run-skillhub.sh)
- 修改SKILLHUB_RUNNER指向正确路径
- 验证: python -c "from update_mechanism import SKILLHUB_RUNNER; from pathlib import Path; print(Path(SKILLHUB_RUNNER).exists())"返回True

R1-6: 修复bash调用(WSL问题)
- 读取 d:\skills\tools\update_mechanism.py upload_free_via_cli函数
- 当前用['bash', SKILLHUB_RUNNER, 'publish', str(skill_dir)]
- Windows上检测可用执行器: 优先git bash, 其次WSL bash, 最后报错明确提示
- 实现: import shutil; bash_path = shutil.which('bash') or shutil.which('git')
- 如果bash不可用, 尝试直接用python subprocess调用skillhub CLI(如果skillhub在PATH)
- 验证: upload_free_via_cli不再因FileNotFoundError失败(可以因业务原因失败,但不能因找不到bash失败)

端到端验证:
- 对1个skill(ai-artist-workstation)运行:
  python d:\skills\tools\quality_gate.py d:\skills\packaged-skills\skillhub\ai-artist-workstation\SKILL.md
  python d:\skills\tools\update_mechanism.py status
- 确认两个命令都不崩溃, quality_gate输出检查结果, status输出skill状态

注意:
- 每步修改前先读取原文件确认当前代码
- 每步修改后立即验证
- 不修改功能逻辑, 只修复断链
- 不引入新bug
- 路径一律用 d:\skills\tools\ 而非 d:\skills\skill-registry\
```

---

## 五、后续每轮提示词模板

每轮完成后,按以下模板生成下一轮提示词:

```
[本轮完成情况]
- R(X)-1: [任务名] ✓/✗ [验证结果]
- R(X)-2: [任务名] ✓/✗ [验证结果]
...

[下一轮提示词]
任务: [轮次目标]

执行步骤(小规模, 每步验证):
R(X+1)-1: ...
- 读取 [文件] [行号]
- 修改 [具体内容]
- 验证: [具体命令]

...

端到端验证: [具体验证步骤]

注意: 每步修改前先读取原文件, 每步修改后立即验证, 不引入新bug
```

---

## 六、假设与决策

1. **路径决策**: 所有修改基于 `d:\skills\tools\` 为实际代码路径。前几轮在 `d:\skills\skill-registry\` 的修改需验证是否同步到了 `d:\skills\tools\`。
2. **小规模原则**: 每轮最多修改6个任务, 每个任务用1-3个skill验证, 不批量处理60个。
3. **不破坏原则**: 修复断链时不改变功能逻辑, 只修复NameError/ImportError/路径错误。
4. **配置优先**: 阈值和路径尽量从config.py导入, 不硬编码。
5. **清理顺序**: 先修复功能(R1-R4), 再清理文件(R5), 最后统一架构(R6)。避免清理后找不到文件导致修复困难。
6. **DB修改安全**: ALTER TABLE ADD COLUMN是安全操作(不丢数据), 清理重复记录前先备份。
