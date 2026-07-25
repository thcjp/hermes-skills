# Round 6 清理 + 全链路 E2E 测试 + V4 计划 实施方案

> **目标**: 执行 round6 清理 → 平台重新认证 → 全链路 E2E 测试(发现→生成→质量门→TRACE≥45→上传→升级→重传) → 创建 v4 计划 → 生成 round7 提示词
> **约束**: 禁止 mock/TODO/pass/fallback;真实上传;仅团队账号(orgId=862);AI 评分≥4.5(=45/50)

---

## 一、当前状态分析(基于实测)

### 1.1 Round 6 清理状态:未开始

| 清理项 | 实测文件 | round6 提示词覆盖? | 处置 |
|--------|---------|-------------------|------|
| `__pycache__` 目录 | 3 个: `tools\`、`tools\skill_core\`、`config\` | ❌ 漏 `config\__pycache__` | L1 补全 |
| 0 字节空 DB 文件 | `data\skill-registry.db`(0B)、`data\skills.db`(0B) | ❌ 完全遗漏 | L2 新增 |
| 0 字节空脚本 | `tools\parse_report.py`(0B) | ✅ | L3 |
| DB 备份 | 3 个(含 `pre-v42-fix`),共~31.4MB | ❌ 只列 2 个,多列 3 个不存在的 | L4 修正 |
| 过期报告 | `tools\update-report.json` | ✅ | L5 |
| 版本化旧脚本 | `batch_approve_v2.js`、`batch_operations_v2.py`、`update_v2_and_report.py` | ✅ | L6 |
| 被取代文档 | 4 个(已确认存在) | ✅ | L7 |

### 1.2 V3 计划进度表偏差

v3 文件 `skill-automation-comprehensive-fix-plan-v3.md` 第 17 行标注第 5 轮(A1-A3)为 "⬜ 待执行",但:
- round6 提示词前言确认 "前 5 轮修复...A1-A3 架构闭环已修复完毕"
- `trace_llm_scorer.py:43-44` 已从 `skill_core` 导入 `RESERVED_WORDS`(A3 落地)
- `generate_skill.py` 的 `llm_generated` 标志已修正(A1 落地)
- `ops闭环.py` 已增加修复动作建议(A2 落地)

**结论**: v3 进度表过期,需在 v4 中修正为 "✅ 已完成"。

### 1.3 平台认证状态:均过期

| 平台 | 认证方式 | 实测结果 | 解决方案 |
|------|---------|---------|---------|
| SkillHub CLI | Python 脚本 `~/.skillhub/skills_store_cli.py` | `auth whoami` 返回 HTTP 401 | 用 org API key `sk-ent-...` 重新 login |
| SkillHub API | Cookie 文件 `~/.skillhub_cookies.txt`(112 字节) | 可能过期 | 备用方案,优先用 CLI |
| ClawHub CLI | `npx clawhub`,token 在 `%APPDATA%\clawhub\config.json` | `whoami` 返回 "user: invalid value" | 尝试现有 token publish;若失败需 `npx clawhub login` |

### 1.4 关键基础设施

| 组件 | 位置/状态 |
|------|----------|
| 活跃 DB | `d:\skills\skill-registry.db`(12.3MB,2882 skills) |
| SkillHub CLI | `C:\Users\thcd\.skillhub\skills_store_cli.py`(支持 `publish/login/auth`) |
| SkillHub 凭证 | `C:\Users\thcd\.skillhub\credentials.json`(org: "科创少年", orgId: 862, apiKey: `sk-ent-...`) |
| ClawHub CLI | `npx clawhub` v0.23.1,token: `clh_PNX0...` |
| auto_publish.py | 存在,但使用 `npx skillhub`(不兼容 Windows),需改用 Python CLI 直调 |
| TRACE 评分器 | `static`(T+C 维度)+ `export`/`import`(R+A+E 维度需 AI 评分) |

### 1.5 遗留项

| 编号 | 说明 | 状态 |
|------|------|------|
| D4 剩余 | 15 个文件/45 处裸 SQL 未收口到 db.py 业务函数 | 分批后续处理 |
| L7(791 个 generation_report) | 评估去重整理 | 本轮评估结论 |

---

## 二、实施计划

### 阶段 0: V3 计划完整性核验(只读)

**目标**: 确认前 5 轮修复全部落地,无遗漏。

**0.1 核验命令**
```powershell
# A1: generate_skill.py 的 llm_generated 标志已修正
Select-String -Path d:\skills\tools\generate_skill.py -Pattern "llm_generated" | Select-Object LineNumber,Line

# A2: ops闭环.py 已增加修复动作建议
Select-String -Path "d:\skills\tools\ops闭环.py" -Pattern "修复|fix_action|repair" | Select-Object -First 5

# A3: trace_llm_scorer.py 从 skill_core 导入
Select-String -Path d:\skills\tools\trace_llm_scorer.py -Pattern "from skill_core" | Select-Object LineNumber,Line

# Q5: check_debranding medium 级也判 fail
Select-String -Path d:\skills\tools\quality_gate.py -Pattern "len\(issues\) == 0|len\(high_issues\)" | Select-Object LineNumber,Line

# D5: scores 表有 is_current 列
python -c "import sys;sys.path.insert(0,r'd:\skills\config');from project_config import get_db_connection;c=get_db_connection();cols=[r[1] for r in c.execute('PRAGMA table_info(scores)').fetchall()];print('is_current' in cols, cols)"

# D1: sources-skill JOIN > 0
python -c "import sys;sys.path.insert(0,r'd:\skills\config');from project_config import get_db_connection;c=get_db_connection();print('JOIN:',c.execute('SELECT COUNT(*) FROM sources s JOIN skills sk ON s.skill_id=sk.id').fetchone()[0])"
```

**0.2 基线健康检查**
```powershell
# 核心脚本语法
python -m py_compile d:\skills\tools\quality_gate.py d:\skills\tools\trace_llm_scorer.py d:\skills\tools\generate_skill.py d:\skills\tools\skill_batch_upgrader_v3.py d:\skills\tools\multi_source_discover.py d:\skills\tools\ops闭环.py d:\skills\tools\batch_l2_eval.py

# 3 个基线 skill 质量门
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Creative\free\ad-creative-intel-free" --json
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Creative\free\agentvibes-skill-free" --json
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Agents\free\agent-assistant-free" --json
```

**验收**: 所有核验命令返回预期结果(A1-A3 已落地、Q5 medium 级 fail、D5 有 is_current、D1 JOIN>0、语法无误、基线 skill 无回归)。

---

### 阶段 1: L1-L8 冗余文件清理

> 以实测清单为准,不照搬 round6 提示词(有漏项和过期项)。DB 备份先归档再删,每步删除后验证核心功能。

**L1: 删除 3 个 `__pycache__` 目录(~1.2MB)**
```powershell
Remove-Item -Recurse -Force d:\skills\config\__pycache__
Remove-Item -Recurse -Force d:\skills\tools\__pycache__
Remove-Item -Recurse -Force d:\skills\tools\skill_core\__pycache__
# 验证
(Get-ChildItem -Recurse -Directory -Filter __pycache__ d:\skills\config,d:\skills\tools -ErrorAction SilentlyContinue).Count  # 预期 0
python -c "import sys;sys.path.insert(0,r'd:\skills\config');from project_config import DB_PATH;print('config import OK')"
```

**L2: 删除 2 个 0 字节空 DB 文件**
```powershell
Remove-Item d:\skills\data\skill-registry.db -Force
Remove-Item d:\skills\data\skills.db -Force
# 验证: 活跃 DB 仍在
(Get-Item d:\skills\skill-registry.db).Length  # 预期 >0
Test-Path d:\skills\data\skill-registry.db     # 预期 False
```

**L3: 删除 0 字节空脚本**
```powershell
Remove-Item d:\skills\tools\parse_report.py -Force
Test-Path d:\skills\tools\parse_report.py  # 预期 False
```

**L4: 归档 3 个 DB 备份(~31.4MB)**
```powershell
New-Item -ItemType Directory -Force -Path d:\skills\data\archive | Out-Null
Move-Item d:\skills\data\backups\skill-registry.db.pre-v42-fix-20260724130053 d:\skills\data\archive\
Move-Item d:\skills\data\backups\skill-registry_phase3_backup_20260724_120254.db d:\skills\data\archive\
Move-Item d:\skills\data\backups\skill-registry_pre_pricing_v34_backup.db d:\skills\data\archive\
# 验证
(Get-ChildItem d:\skills\data\backups -Filter *.db -ErrorAction SilentlyContinue).Count  # 预期 0
(Get-ChildItem d:\skills\data\archive).Count  # 预期 3
python -c "import sys;sys.path.insert(0,r'd:\skills\config');from project_config import get_db_connection;c=get_db_connection();print('tables:',len(c.execute('SELECT name FROM sqlite_master WHERE type=''table''').fetchall()))"
```

**L5: 删除过期报告**
```powershell
Remove-Item d:\skills\tools\update-report.json -Force
Test-Path d:\skills\tools\update-report.json  # 预期 False
```

**L6: 删除 3 个版本化旧脚本(~21KB)**
```powershell
# 先确认无外部引用
Select-String -Path d:\skills\tools\*.py -Pattern "batch_approve_v2|batch_operations_v2|update_v2_and_report" -ErrorAction SilentlyContinue
# 删除
Remove-Item d:\skills\tools\batch_approve_v2.js -Force
Remove-Item d:\skills\tools\batch_operations_v2.py -Force
Remove-Item d:\skills\tools\update_v2_and_report.py -Force
# 验证核心脚本语法
python -m py_compile d:\skills\tools\quality_gate.py d:\skills\tools\generate_skill.py d:\skills\tools\skill_batch_upgrader_v3.py
```

**L7: 归档被取代的文档**
```powershell
New-Item -ItemType Directory -Force -Path d:\skills\.trae\documents\archive | Out-Null
Move-Item d:\skills\.trae\documents\P0-pipeline-breakage-fix-plan.md d:\skills\.trae\documents\archive\ -Force
Move-Item d:\skills\.trae\documents\round5-prompt-and-review.md d:\skills\.trae\documents\archive\ -Force
Move-Item d:\skills\.trae\documents\skill-automation-comprehensive-audit-and-fix-plan.md d:\skills\.trae\documents\archive\ -Force
Move-Item d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v2.md d:\skills\.trae\documents\archive\ -Force
# 验证
(Get-ChildItem d:\skills\.trae\documents\archive).Count  # 预期 4
```

**L8: 综合回归验证**
```powershell
# 全部核心脚本语法
python -m py_compile d:\skills\tools\quality_gate.py d:\skills\tools\trace_llm_scorer.py d:\skills\tools\generate_skill.py d:\skills\tools\ops闭环.py d:\skills\tools\batch_l2_eval.py d:\skills\tools\skill_batch_upgrader_v3.py d:\skills\tools\skill_core\rules.py d:\skills\tools\skill_core\parser.py d:\skills\tools\skill_core\checks.py d:\skills\tools\skill_core\db.py

# 3 个基线 skill 质量门无回归
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Creative\free\ad-creative-intel-free" --json
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Creative\free\agentvibes-skill-free" --json
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Agents\free\agent-assistant-free" --json

# ops闭环 正常运行
python d:\skills\tools\ops闭环.py -o "$env:TEMP\ops_post_cleanup.json" 2>&1 | Out-Null

# batch_l2_eval 无报错
python d:\skills\tools\batch_l2_eval.py --limit 1 --dry-run
```

**验收**: __pycache__ 全部删除、空文件删除、DB 备份归档、旧脚本删除、文档归档、核心脚本语法通过、基线 skill 无回归。

---

### 阶段 2: 平台重新认证

**2.1 SkillHub 重新登录(团队账号)**
```powershell
# 从 credentials.json 读取企业 API key
$cred = Get-Content C:\Users\thcd\.skillhub\credentials.json -Raw | ConvertFrom-Json
$orgKey = $cred.orgs.'org-xxo535hs'.apiKey  # sk-ent-... 格式
python C:\Users\thcd\.skillhub\skills_store_cli.py login --key $orgKey
# 验证
python C:\Users\thcd\.skillhub\skills_store_cli.py auth whoami
```
> 仅使用团队企业 key `sk-ent-...`,不使用个人 `skh_` token。

**2.2 ClawHub 认证**
```powershell
# 先测试现有 token 是否可用于 publish(whoami 失败不代表 publish 失败)
# 如果 publish 也失败,则重新登录:
npx clawhub login
# 验证
npx clawhub whoami
```
> `npx clawhub login` 使用 device flow,可能需要浏览器交互。若无法自动完成,需用户手动操作。

**2.3 认证连通性确认**
```powershell
# SkillHub: 列出已安装 skill(只读)
python C:\Users\thcd\.skillhub\skills_store_cli.py list --limit 1
# ClawHub: whoami 返回用户名
npx clawhub whoami
```

**验收**: SkillHub `whoami` 返回用户信息(非 401);ClawHub `whoami` 返回用户名(非 "invalid value")。

---

### 阶段 3: 全链路 E2E 测试

> 3 个 skill 分别来自 github/awesome/hermes 三个源,覆盖全部发现器。无 mock,真实上传,仅团队账号。

**3.1 发现 3 个候选 skill**
```powershell
cd d:\skills\tools
python multi_source_discover.py --source github
python multi_source_discover.py --source awesome
python multi_source_discover.py --source hermes
# 查看统一候选输出
python -c "import json; data=json.load(open(r'd:\skills\data\discovery\candidates_unified.json')); [print(f\"{c['source']:10s} | {c['source_id']:40s} | {c['name'][:50]}\") for c in data[:20]]"
```
从输出挑选 3 个候选(每源 1 个),记为 `$S1`(github)、`$S2`(awesome)、`$S3`(hermes)。

**选择标准**: 未在本地 DB 中注册的 slug;description 可提取 150-280 字符;分类明确。

**3.2 生成 3 个 skill**
```powershell
cd d:\skills\tools
python generate_skill.py from-candidate <slug1> --template tool_wrapper_template --description "<desc1 150-280字符>" --skip-dep-verify
python generate_skill.py from-candidate <slug2> --template tool_wrapper_template --description "<desc2>" --skip-dep-verify
python generate_skill.py from-candidate <slug3> --template tool_wrapper_template --description "<desc3>" --skip-dep-verify
```
> 生成产物: `d:\skills\packaged-skills\skillhub\<slug>\SKILL.md`。`--skip-dep-verify` 因新 skill 无外部依赖。禁止加 `--skip-l2`。

**3.3 质量门(L1 13 项检查)**
```powershell
python d:\skills\tools\quality_gate.py "d:\skills\packaged-skills\skillhub\<slug1>" --json
python d:\skills\tools\quality_gate.py "d:\skills\packaged-skills\skillhub\<slug2>" --json
python d:\skills\tools\quality_gate.py "d:\skills\packaged-skills\skillhub\<slug3>" --json
```
**验收**: 3 个 `overall_passed=true`。若 fail,用 `skill_batch_upgrader_v3.py fix --slug <slug>` 修复后重跑,迭代至全过。

**3.4 TRACE 评分达≥45/50**

> 静态分只覆盖 T+C(上限~20),达标必须走 export→AI 评分→import 全流程。

**Step A: 静态评分**
```powershell
cd d:\skills\tools
python trace_llm_scorer.py static --packaged
```

**Step B: 导出待评 skill**
```powershell
python trace_llm_scorer.py export --packaged
# 导出文件: %TEMP%\skills-exports\trace_eval_batch_*.json
```

**Step C: AI 评分(由执行代理完成)**
读取导出 JSON 中这 3 个 skill 的内容,按 5 个 TRACE 维度打分:
- T (Trust, /10): 信任度 — 无虚假声明、无夸大词、依赖说明透明
- R (Reliability, /10): 可靠性 — 逻辑完整、错误处理充分、边界条件覆盖
- A (Adaptability, /10): 适应性 — 可适配不同场景、参数灵活、扩展性好
- C (Convention, /10): 规范性 — frontmatter 完整、格式标准、命名规范
- E (Effectiveness, /10): 有效性 — 实际解决问题、用户价值高、操作可行

产出 `d:\skills\data\reports\trace_e2e_results.json`,schema:
```json
[{
  "slug": "<slug>",
  "quality_grade": "A+",
  "total_score": 46,
  "trace_scores": {
    "trust": {"score": 9, "reason": "..."},
    "reliability": {"score": 9, "reason": "..."},
    "adaptability": {"score": 9, "reason": "..."},
    "convention": {"score": 9, "reason": "..."},
    "effectiveness": {"score": 10, "reason": "..."}
  }
}]
```
> trust 与 convention 会与静态分取 max。总分须≥45(A+ 级 = 4.5/5.0)。

**Step D: 导入评分**
```powershell
python trace_llm_scorer.py import d:\skills\data\reports\trace_e2e_results.json
python trace_llm_scorer.py report
```
**验收**: DB 中这 3 个 skill 的 `total_score≥45`。若<45,回到 3.2/3.3 用 upgrader 优化 SKILL.md 内容后重评,迭代直至≥45。

**3.5 上传双平台(真实上传)**

**SkillHub(团队账号)— 使用 Python CLI 直调**
```powershell
# 方法: 直接调用 SkillHub CLI Python 脚本(auto_publish.py 使用 npx skillhub 不兼容 Windows)
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug1>" --changelog "E2E test v1.0.0" --json
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug2>" --changelog "E2E test v1.0.0" --json
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug3>" --changelog "E2E test v1.0.0" --json
```
> 若报 `VERSION_EXISTS`: 递增 SKILL.md frontmatter 的 version 字段后重传。若报 `SLUG_CONFLICT`: 改名为唯一 slug 后重传。若报 `401`: 重新执行阶段 2.1。

**ClawHub**
```powershell
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug1>" --changelog "E2E test v1.0.0"
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug2>" --changelog "E2E test v1.0.0"
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug3>" --changelog "E2E test v1.0.0"
```

**验收**: 两端均返回 success。记录上传结果到 DB。

**3.6 验证 SkillHub AI 评分**
```powershell
# 查询 SkillHub 平台 AI 评分(上传后需等待审核)
python C:\Users\thcd\.skillhub\skills_store_cli.py skill evaluation <slug1>
python C:\Users\thcd\.skillhub\skills_store_cli.py skill evaluation <slug2>
python C:\Users\thcd\.skillhub\skills_store_cli.py skill evaluation <slug3>
```
**验收**: SkillHub 平台 AI 评分≥4.5(若平台使用 5 分制)或≥45(若使用 50 分制)。若暂无评分(pending_review),记录状态并等待。

**3.7 重新发现相似 skill(验证发现去重+升级环)**
```powershell
# 再次跑发现,刚上传的 skill 应被去重逻辑识别为"已存在"
python multi_source_discover.py --source github
# 验证 sources 表对这 3 个 slug 已关联 skill_id(D1 修复链路)
python -c "import sys;sys.path.insert(0,r'd:\skills\config');from project_config import get_db_connection;c=get_db_connection();rows=c.execute('SELECT original_slug,skill_id FROM sources WHERE skill_id IS NOT NULL ORDER BY id DESC LIMIT 10').fetchall();[print(r) for r in rows]"
```

**3.8 升级本地 skill**
```powershell
cd d:\skills\tools
# 针对这 3 个 skill 修复+优化
python skill_batch_upgrader_v3.py fix --slug <slug1>
python skill_batch_upgrader_v3.py fix --slug <slug2>
python skill_batch_upgrader_v3.py fix --slug <slug3>
python skill_batch_upgrader_v3.py report
# 升级后重跑质量门,确认无回归
python quality_gate.py "d:\skills\packaged-skills\skillhub\<slug1>" --json
python quality_gate.py "d:\skills\packaged-skills\skillhub\<slug2>" --json
python quality_gate.py "d:\skills\packaged-skills\skillhub\<slug3>" --json
```
> 若 fix 修改了内容,需将 SKILL.md frontmatter 的 `version` 从 `1.0.0` 递增至 `1.1.0`(否则 3.9 重传报 VERSION_EXISTS)。

**3.9 重新上传(版本递增后)**
```powershell
# SkillHub
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug1>" --changelog "E2E upgrade v1.1.0" --json
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug2>" --changelog "E2E upgrade v1.1.0" --json
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug3>" --changelog "E2E upgrade v1.1.0" --json

# ClawHub
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug1>" --changelog "E2E upgrade v1.1.0"
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug2>" --changelog "E2E upgrade v1.1.0"
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug3>" --changelog "E2E upgrade v1.1.0"
```
**验收**: 重传 success;DB 中每个 slug 有 2 条成功记录(v1.0.0 + v1.1.0),评分历史保留(D5 is_current 版本化)。

---

### 阶段 4: 创建 V4 计划

**文件**: `d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v4.md`

**V4 计划需包含**:

1. **修正 V3 进度表**: 将第 5 轮(A1-A3)状态从 "⬜ 待执行" 改为 "✅ 已完成"(以代码事实为准)
2. **记录 L1-L8 清理的实测修正**:
   - `config\__pycache__` 补入 L1(round6 漏列)
   - 3 个 DB 备份(非 2 个),含 `pre-v42-fix` 文件
   - 删除 2 个 0 字节空 DB 文件(`data\skill-registry.db`、`data\skills.db`)
   - 移除不存在的 `upload_tracking` 备份项
3. **E2E 测试结论章节**: 记录 3 个 skill 全链路结果、TRACE 分数、双平台上传状态、升级环验证
4. **平台认证状态**: 记录 SkillHub/ClawHub 认证修复过程和最终状态
5. **遗留项追踪**:
   - D4 剩余 15 个文件的裸 SQL 收口(本轮未处理,分批后续)
   - L7(791 个 generation_report)评估结论
   - auto_publish.py 使用 `npx skillhub` 不兼容 Windows 的问题(需修复或改用 Python CLI)
6. **下一阶段建议**: 裸 SQL 收口批次计划 / 大规模批量上传运营计划

---

### 阶段 5: 生成 Round 7 提示词

**文件**: `d:\skills\.trae\documents\round7-prompt.md`

**Round 7 提示词内容大纲**:

- **标题**: 第 7 轮提示词(E2E 全链路验证与遗留项处理)
- **背景**: L1-L8 清理已完成(附实测修正清单),平台已重新认证,E2E 全链路验证结果
- **任务块**:
  - 若 E2E 测试发现新 bug: 针对性修复提示词
  - 若 E2E 测试通过: D4 剩余 15 个文件裸 SQL 收口批次处理
  - auto_publish.py 的 `npx skillhub` 兼容性修复
- **约束**: 无 mock/真实数据/仅团队账号
- **验收标准**: 视任务内容而定
- **完成后输出**: 下一轮提示词(或收尾)

---

## 三、假设与决策

| # | 决策 | 理由 |
|---|------|------|
| 1 | 清理清单以实测为准,不照搬 round6 提示词 | round6 有漏项(config\__pycache__)和过期项(不存在的 upload_tracking 备份) |
| 2 | SkillHub 上传使用 Python CLI 直调,不用 auto_publish.py | auto_publish.py 使用 `npx skillhub`(npm 包),Windows 上不兼容;CLI 实际是 Python 脚本 |
| 3 | TRACE 评分走 export→AI 评分→import 全流程 | 静态分只覆盖 T+C(上限~20),要达到≥45 必须补全 R+A+E 维度 |
| 4 | AI 评分由执行代理(即 AI 会话自身)完成 | TRACE 评分器不直接调用 LLM API,需手动评估后导入 |
| 5 | ClawHub 认证若失败需用户手动 login | `npx clawhub login` 使用 device flow,需浏览器交互 |
| 6 | 仅使用团队账号(orgId=862) | 用户明确要求 "本次测试只考虑团队号" |
| 7 | 测试 3 个 skill(每源 1 个) | 覆盖 3 种发现器,规模适中,与前序验证一致 |

---

## 四、风险与应对

| 风险 | 概率 | 应对 |
|------|------|------|
| SkillHub login 仍失败(401) | 低 | 删除 credentials.json 后重新 login;确认使用 `sk-ent-` 企业 key |
| ClawHub login 需浏览器交互 | 中 | 提示用户手动完成 `npx clawhub login`;若无法完成则仅测 SkillHub 端 |
| from-candidate 生成质量门不过 | 中 | 用 `skill_batch_upgrader_v3.py fix --slug` 修复后重跑,迭代至通过 |
| TRACE 总分<45 | 中 | 重点优化 effectiveness 维度;检查 description 是否充分、依赖说明是否透明 |
| 上传报 VERSION_EXISTS | 低 | 递增 version 字段(1.0.0→1.1.0)后重传 |
| 上传报 SLUG_CONFLICT | 低 | 改名为唯一 slug 后重传 |
| 发现器无新候选(去重后空) | 低 | 切换至 hermes 源(本地仓库必有内容)或扩展 github 关键词 |
| SkillHub AI 评分暂无(pending_review) | 中 | 记录状态;用 TRACE 分数(≥45)作为质量代理指标 |
| GitHub API 限频(60 次/小时未认证) | 低 | 3 个 skill 的发现请求远低于限额 |

---

## 五、验证步骤汇总

| 阶段 | 验证项 | 验证方法 |
|------|--------|---------|
| 0 | V3 计划全部修复已落地 | 代码 grep + DB schema 检查 |
| 1 | 清理后核心功能无回归 | py_compile + quality_gate 3 个基线 skill + ops闭环 + batch_l2_eval |
| 2 | 双平台认证成功 | SkillHub whoami 非 401;ClawHub whoami 非 invalid |
| 3.1 | 3 个候选 skill 发现成功 | candidates_unified.json 有 3 条新记录 |
| 3.2 | 3 个 skill 生成成功 | packaged-skills/skillhub/<slug>/SKILL.md 存在 |
| 3.3 | 质量门全通过 | 3 个 overall_passed=true |
| 3.4 | TRACE 总分≥45 | DB scores 表 total_score≥45 |
| 3.5 | 双平台上传成功 | 两端返回 success |
| 3.6 | SkillHub AI 评分≥4.5 | skill evaluation 命令返回评分≥4.5 |
| 3.7 | 发现去重+sources 关联 | sources 表 skill_id 关联>0 |
| 3.8 | 升级后质量门无回归 | quality_gate 仍通过 |
| 3.9 | 重传成功+历史保留 | DB 有 2 条上传记录,scores 有 is_current 版本化 |
| 4 | V4 计划创建 | 文件存在且内容完整 |
| 5 | Round 7 提示词生成 | 文件存在且包含完整任务块 |

---

## 六、关键文件路径索引

| 用途 | 路径 |
|------|------|
| V3 计划 | `d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v3.md` |
| Round 6 提示词 | `d:\skills\.trae\documents\round6-prompt.md` |
| V4 计划(待建) | `d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v4.md` |
| Round 7 提示词(待建) | `d:\skills\.trae\documents\round7-prompt.md` |
| 发现器 | `d:\skills\tools\multi_source_discover.py` |
| 生成器 | `d:\skills\tools\generate_skill.py` |
| 质量门 | `d:\skills\tools\quality_gate.py` |
| TRACE 评分器 | `d:\skills\tools\trace_llm_scorer.py` |
| 升级器 | `d:\skills\tools\skill_batch_upgrader_v3.py` |
| 自动发布 | `d:\skills\tools\auto_publish.py`(注意:使用 npx skillhub,不兼容 Windows) |
| 企业上传器 | `d:\skills\tools\enterprise_uploader.py`(cookie 认证,备用) |
| 配置 SSOT | `d:\skills\config\project_config.py`、`d:\skills\config\platform_config.py` |
| SkillHub CLI | `C:\Users\thcd\.skillhub\skills_store_cli.py` |
| SkillHub 凭证 | `C:\Users\thcd\.skillhub\credentials.json` |
| ClawHub 配置 | `%APPDATA%\clawhub\config.json` |
| 活跃 DB | `d:\skills\skill-registry.db`(12.3MB) |
| 候选输出 | `d:\skills\data\discovery\candidates_unified.json` |
| 生成产物 | `d:\skills\packaged-skills\skillhub\<slug>\SKILL.md` |
