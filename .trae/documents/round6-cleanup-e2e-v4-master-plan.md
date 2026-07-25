# Round 6 清理 + E2E 全链路测试 + V4 计划 — 主实施计划

> **目标**: 执行 round6 清理 → 修复关键阻塞 → 平台认证 → 全链路 E2E 测试(发现→生成→质量门→TRACE≥45→上传→验证AI评分≥4.5→升级→重传) → 创建 V4 计划 → 生成 round7 提示词
> **约束**: 禁止 mock/TODO/pass/fallback; 真实上传; 仅团队账号(orgId=862); AI 评分≥4.5(TRACE≥45/50)

---

## 一、当前状态分析(基于代码实测)

### 1.1 V3 计划前5轮修复 — 全部确认已落地 ✅

| 轮次 | 核验结果 |
|------|---------|
| P0-1~P0-3 | ✅ daily_sync.py 配置化 dry-run; update_mechanism.py 真实上传; db.py 含全部列 |
| Q1-Q5 | ✅ rules.py 阈值从 project_config 导入; 占位符/夸大词补全; quality_gate.py:76 `len(issues)==0`(medium 级也 fail) |
| D1-D3 | ✅ sources-skill JOIN=469; FK enabled=1; skill_id 列存在 |
| D4-D6 | ✅ is_current 列存在; record_upload 去重; DELETE→UPDATE is_current=0 |
| A1-A3 | ✅ llm_generated=False(generate_skill.py:1051); ops闭环.py:255-289 fix_actions; trace_llm_scorer.py:43-44 从 skill_core 导入 |

### 1.2 Round 6 清理(L1-L8) — 全部未开始

| 清理项 | 实测确认 | 处置 |
|--------|---------|------|
| 3个 `__pycache__` 目录 | `config\`、`tools\`、`tools\skill_core\` 均存在 | 删除 |
| 2个 0字节空 DB | `data\skill-registry.db`(0B)、`data\skills.db`(0B) | 删除 |
| 1个 0字节空脚本 | `tools\parse_report.py`(0B) | 删除 |
| 3个 DB 备份(~31.4MB) | `data\backups\` 下3个文件 | 归档到 `data\archive\` |
| 1个过期报告 | `tools\update-report.json` | 删除 |
| 3个旧脚本 | `batch_approve_v2.js`、`batch_operations_v2.py`、`update_v2_and_report.py` | 删除 |
| 4个被取代文档 | P0-plan、round5-prompt、audit-plan、v2-plan | 归档到 `.trae\documents\archive\` |

### 1.3 关键阻塞问题(新发现) — skill_batch_upgrader_v2.py 缺失

`tools\skill_batch_upgrader_v3.py:37-42` 导入 `skill_batch_upgrader_v2`，但该文件**完全不存在**(glob 全项目无匹配)。v3 从 v2 导入 10 个符号: SECTION_MAP, DOMESTIC_ALTERNATIVES, parse_skill_md, find_section_header, check_missing_sections, extract_section_content, rename_section, optimize_description, generate_section_content, upgrade_skill。

**影响**: 阻塞 E2E 测试步骤 4.8(升级本地 skill)，必须在清理阶段前置修复。

### 1.4 auto_publish.py Windows 兼容性问题

`tools\auto_publish.py:119-120` 使用 `npx skillhub publish`，但 SkillHub CLI 实际是 Python 脚本 `C:\Users\thcd\.skillhub\skills_store_cli.py`，`npx skillhub` 在 Windows 上不可用。全项目仅此1处。

### 1.5 平台凭证

| 平台 | 凭证 | 状态 |
|------|------|------|
| SkillHub(团队) | orgId=862, apiKey=`sk-ent-a760...` | 需重新 login |
| ClawHub | token=`clh_PNX0...` | 需验证 whoami |

---

## 二、实施计划(6个阶段)

### 阶段 0: V3 计划完整性核验(只读)

**目标**: 确认前5轮修复全部落地，建立基线。

```powershell
# 0.1 核验 A1-A3/Q5/D1/D5
Select-String -Path d:\skills\tools\generate_skill.py -Pattern "llm_generated" | Select-Object LineNumber,Line
Select-String -Path "d:\skills\tools\ops闭环.py" -Pattern "fix_action" | Select-Object -First 3
Select-String -Path d:\skills\tools\trace_llm_scorer.py -Pattern "from skill_core" | Select-Object LineNumber,Line
Select-String -Path d:\skills\tools\quality_gate.py -Pattern "len\(issues\) == 0" | Select-Object LineNumber,Line
python -c "import sys;sys.path.insert(0,r'd:\skills\config');from project_config import get_db_connection;c=get_db_connection();cols=[r[1] for r in c.execute('PRAGMA table_info(scores)').fetchall()];print('is_current:', 'is_current' in cols);print('JOIN:',c.execute('SELECT COUNT(*) FROM sources s JOIN skills sk ON s.skill_id=sk.id').fetchone()[0])"

# 0.2 基线语法检查(注意: skill_batch_upgrader_v3.py 预期失败，阶段1修复后重测)
python -m py_compile d:\skills\tools\quality_gate.py d:\skills\tools\trace_llm_scorer.py d:\skills\tools\generate_skill.py d:\skills\tools\multi_source_discover.py d:\skills\tools\ops闭环.py d:\skills\tools\batch_l2_eval.py

# 0.3 基线 skill 质量门
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Creative\free\ad-creative-intel-free" --json
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Creative\free\agentvibes-skill-free" --json
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Agents\free\agent-assistant-free" --json
```

**验收**: A1-A3 已落地、Q5 medium 级 fail、D5 有 is_current、D1 JOIN=469>0、语法无误(除 v3 外)、基线 skill 无回归。

---

### 阶段 1: L1-L8 清理 + 关键阻塞修复

> 先修复 skill_batch_upgrader_v2.py 缺失问题(E2E 前置)，再执行清理。

#### 1.0 修复 skill_batch_upgrader_v2.py 缺失(新建文件)

**文件**: `d:\skills\tools\skill_batch_upgrader_v2.py`(新建)

**需实现的 10 个符号**(基于 v3 代码分析):
1. `SECTION_MAP` — 章节映射常量(dict): 核心能力/适用场景/使用流程/依赖说明/常见问题/已知限制 等
2. `DOMESTIC_ALTERNATIVES` — 国外→国内服务映射(dict): GitHub→Gitee, OpenAI→通义千问, Slack→飞书 等
3. `parse_skill_md(content)` — 解析 SKILL.md(返回 (fm_dict, body_str))，复用 `skill_core.parser.parse_frontmatter`
4. `find_section_header(body, section_name)` — 查找 `## {section_name}` 位置
5. `check_missing_sections(fm, body)` — 检查缺失的标准章节
6. `extract_section_content(body, section_name)` — 提取章节内容(到下一个 `## ` 或文件末尾)
7. `rename_section(body, old_name, new_name)` — 重命名章节标题
8. `optimize_description(fm)` — 优化 description 长度到 150-280 范围(从 project_config 导入阈值)
9. `generate_section_content(section_name, skill_data)` — 生成标准章节模板内容
10. `upgrade_skill(skill_md_path)` — 综合升级: 调用上述函数完成章节补全+描述优化+去标识化

**实现要点**:
- `parse_skill_md` 必须复用 `skill_core.parser.parse_frontmatter`(单一来源原则)
- `optimize_description` 从 `project_config` 导入 `MIN_DESCRIPTION_LEN=150, MAX_DESCRIPTION_LEN=280`
- `SECTION_MAP` 包含标准章节: 核心能力、适用场景、使用流程、依赖说明、常见问题、已知限制
- `DOMESTIC_ALTERNATIVES` 包含: GitHub→Gitee, OpenAI→通义千问/文心一言, Slack→飞书, Discord→钉钉 等
- `upgrade_skill` 返回 `{'changed': bool, 'changes': list}` 格式，与 v3 调用兼容
- 函数签名和返回类型必须与 v3 中的调用方式完全匹配

**验证**:
```powershell
python -m py_compile d:\skills\tools\skill_batch_upgrader_v2.py
python -c "import sys; sys.path.insert(0, r'd:\skills\tools'); sys.path.insert(0, r'd:\skills\config'); import skill_batch_upgrader_v3; print('v3 import OK')"
python d:\skills\tools\skill_batch_upgrader_v3.py check --slug ad-creative-intel-free
```

#### 1.1 L1: 删除 3 个 __pycache__ 目录
```powershell
Remove-Item -Recurse -Force d:\skills\config\__pycache__
Remove-Item -Recurse -Force d:\skills\tools\__pycache__
Remove-Item -Recurse -Force d:\skills\tools\skill_core\__pycache__
# 验证
(Get-ChildItem -Recurse -Directory -Filter __pycache__ d:\skills\config,d:\skills\tools -ErrorAction SilentlyContinue).Count  # 预期 0
python -c "import sys;sys.path.insert(0,r'd:\skills\config');from project_config import DB_PATH;print('config import OK')"
```

#### 1.2 L2: 删除 2 个 0字节空 DB 文件
```powershell
Remove-Item d:\skills\data\skill-registry.db -Force
Remove-Item d:\skills\data\skills.db -Force
# 验证
(Get-Item d:\skills\skill-registry.db).Length  # 预期 >0
Test-Path d:\skills\data\skill-registry.db     # 预期 False
```

#### 1.3 L3: 删除 0字节空脚本
```powershell
Remove-Item d:\skills\tools\parse_report.py -Force
Test-Path d:\skills\tools\parse_report.py  # 预期 False
```

#### 1.4 L4: 归档 3 个 DB 备份(~31.4MB)
```powershell
New-Item -ItemType Directory -Force -Path d:\skills\data\archive | Out-Null
Move-Item d:\skills\data\backups\skill-registry.db.pre-v42-fix-20260724130053 d:\skills\data\archive\
Move-Item d:\skills\data\backups\skill-registry_phase3_backup_20260724_120254.db d:\skills\data\archive\
Move-Item d:\skills\data\backups\skill-registry_pre_pricing_v34_backup.db d:\skills\data\archive\
# 验证
(Get-ChildItem d:\skills\data\backups -Filter *.db* -ErrorAction SilentlyContinue).Count  # 预期 0
(Get-ChildItem d:\skills\data\archive).Count  # 预期 3
python -c "import sys;sys.path.insert(0,r'd:\skills\config');from project_config import get_db_connection;c=get_db_connection();print('tables:',len(c.execute('SELECT name FROM sqlite_master WHERE type=''table''').fetchall()))"
```

#### 1.5 L5: 删除过期报告
```powershell
Remove-Item d:\skills\tools\update-report.json -Force
Test-Path d:\skills\tools\update-report.json  # 预期 False
```

#### 1.6 L6: 删除 3 个旧脚本
```powershell
# 先确认无外部引用
Select-String -Path d:\skills\tools\*.py -Pattern "batch_approve_v2|batch_operations_v2|update_v2_and_report" -ErrorAction SilentlyContinue
Remove-Item d:\skills\tools\batch_approve_v2.js -Force
Remove-Item d:\skills\tools\batch_operations_v2.py -Force
Remove-Item d:\skills\tools\update_v2_and_report.py -Force
python -m py_compile d:\skills\tools\quality_gate.py d:\skills\tools\generate_skill.py d:\skills\tools\skill_batch_upgrader_v3.py
```

#### 1.7 L7: 归档被取代的文档(4个)
```powershell
New-Item -ItemType Directory -Force -Path d:\skills\.trae\documents\archive | Out-Null
Move-Item d:\skills\.trae\documents\P0-pipeline-breakage-fix-plan.md d:\skills\.trae\documents\archive\ -Force
Move-Item d:\skills\.trae\documents\round5-prompt-and-review.md d:\skills\.trae\documents\archive\ -Force
Move-Item d:\skills\.trae\documents\skill-automation-comprehensive-audit-and-fix-plan.md d:\skills\.trae\documents\archive\ -Force
Move-Item d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v2.md d:\skills\.trae\documents\archive\ -Force
(Get-ChildItem d:\skills\.trae\documents\archive).Count  # 预期 4
```

#### 1.8 L8: 综合回归验证
```powershell
# 全部核心脚本语法(含修复后的 v2+v3)
python -m py_compile d:\skills\tools\quality_gate.py d:\skills\tools\trace_llm_scorer.py d:\skills\tools\generate_skill.py d:\skills\tools\ops闭环.py d:\skills\tools\batch_l2_eval.py d:\skills\tools\skill_batch_upgrader_v3.py d:\skills\tools\skill_batch_upgrader_v2.py d:\skills\tools\skill_core\rules.py d:\skills\tools\skill_core\parser.py d:\skills\tools\skill_core\checks.py d:\skills\tools\skill_core\db.py

# 3 个基线 skill 质量门无回归
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Creative\free\ad-creative-intel-free" --json
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Creative\free\agentvibes-skill-free" --json
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Agents\free\agent-assistant-free" --json

# ops闭环 正常运行
python d:\skills\tools\ops闭环.py -o "$env:TEMP\ops_post_cleanup.json" 2>&1 | Out-Null

# batch_l2_eval 无报错
python d:\skills\tools\batch_l2_eval.py --limit 1 --dry-run

# skill_batch_upgrader_v3 可运行(修复后)
python d:\skills\tools\skill_batch_upgrader_v3.py check --slug ad-creative-intel-free
```

**验收**: __pycache__ 全部删除、空文件删除、DB 备份归档(3个)、旧脚本删除、文档归档(4个)、skill_batch_upgrader_v3 可运行、核心脚本语法通过、基线 skill 无回归。

---

### 阶段 2: 修复 auto_publish.py Windows 兼容性

**文件**: `d:\skills\tools\auto_publish.py`
**修改位置**: 第 119-120 行 `publish_to_skillhub` 函数

**当前代码**:
```python
    # 执行上传 (使用 npx skillhub 确保 CLI 可用)
    cmd = f'npx skillhub publish "{skill_dir}" --changelog "Automated publish"'
```

**修改为**:
```python
    # 执行上传 (使用 Python CLI 直调，Windows 兼容)
    # SkillHub CLI 实际是 Python 脚本: C:\Users\thcd\.skillhub\skills_store_cli.py
    skillhub_cli = r"C:\Users\thcd\.skillhub\skills_store_cli.py"
    cmd = f'python "{skillhub_cli}" publish "{skill_dir}" --changelog "Automated publish"'
```

**验证**:
```powershell
python -m py_compile d:\skills\tools\auto_publish.py
python d:\skills\tools\auto_publish.py publish-skillhub ad-creative-intel-free --dry-run
```

**注意**: 仅修改命令构造; 错误处理逻辑(VERSION_EXISTS/SLUG_CONFLICT/429/401 等解析)保持不变。

---

### 阶段 3: 平台重新认证

#### 3.1 SkillHub 重新登录(团队账号)
```powershell
$cred = Get-Content C:\Users\thcd\.skillhub\credentials.json -Raw | ConvertFrom-Json
$orgKey = $cred.orgs.'org-xxo535hs'.apiKey  # sk-ent-a760... 格式
python C:\Users\thcd\.skillhub\skills_store_cli.py login --key $orgKey
# 验证
python C:\Users\thcd\.skillhub\skills_store_cli.py auth whoami
```

#### 3.2 ClawHub 认证验证
```powershell
npx clawhub whoami
# 若失败则: npx clawhub login (device flow，可能需浏览器交互)
```

#### 3.3 连通性确认
```powershell
python C:\Users\thcd\.skillhub\skills_store_cli.py list --limit 1
npx clawhub whoami
```

**验收**: SkillHub `whoami` 返回用户信息(非 401); ClawHub `whoami` 返回用户名。

---

### 阶段 4: 全链路 E2E 测试

> 3 个 skill 分别来自 github/awesome/hermes 三个源。无 mock，真实上传，仅团队账号。

#### 4.1 发现 3 个候选 skill
```powershell
cd d:\skills\tools
python multi_source_discover.py --source github
python multi_source_discover.py --source awesome
python multi_source_discover.py --source hermes
# 查看候选
python -c "import json; data=json.load(open(r'd:\skills\data\discovery\candidates_unified.json')); [print(f\"{c['source']:10s} | {c.get('source_id',''):40s} | {c.get('name','')[:50]}\") for c in data[:20]]"
```
从输出挑选 3 个候选(每源 1 个)，记为 `$S1`、`$S2`、`$S3`。
**选择标准**: 未在本地 DB 中注册的 slug; description 可提取 150-280 字符; 分类明确。

#### 4.2 生成 3 个 skill
```powershell
cd d:\skills\tools
python generate_skill.py from-candidate <slug1> --template tool_wrapper_template --description "<desc1 150-280字符>" --skip-dep-verify
python generate_skill.py from-candidate <slug2> --template tool_wrapper_template --description "<desc2>" --skip-dep-verify
python generate_skill.py from-candidate <slug3> --template tool_wrapper_template --description "<desc3>" --skip-dep-verify
```
> 生成产物: `d:\skills\packaged-skills\skillhub\<slug>\SKILL.md`

#### 4.3 质量门(13 项检查)
```powershell
python d:\skills\tools\quality_gate.py "d:\skills\packaged-skills\skillhub\<slug1>" --json
python d:\skills\tools\quality_gate.py "d:\skills\packaged-skills\skillhub\<slug2>" --json
python d:\skills\tools\quality_gate.py "d:\skills\packaged-skills\skillhub\<slug3>" --json
```
**验收**: 3 个 `overall_passed=true`。若 fail，用 `skill_batch_upgrader_v3.py fix --slug <slug>` 修复后重跑，迭代至全过。

#### 4.4 TRACE 评分达≥45/50

> 静态分只覆盖 T+C(上限~20)，达标必须走 export→AI 评分→import 全流程。

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
读取导出 JSON 中这 3 个 skill 的内容，按 5 个 TRACE 维度打分(每维度 0-10):
- T (Trust): 无虚假声明、无夸大词、依赖说明透明
- R (Reliability): 逻辑完整、错误处理充分、边界条件覆盖
- A (Adaptability): 可适配不同场景、参数灵活、扩展性好
- C (Convention): frontmatter 完整、格式标准、命名规范
- E (Effectiveness): 实际解决问题、用户价值高、操作可行

产出 `d:\skills\data\reports\trace_e2e_results.json`:
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
**验收**: DB 中这 3 个 skill 的 `total_score≥45`。若<45，回到 4.2/4.3 优化后重评，迭代直至≥45。

#### 4.5 上传双平台(真实上传)

**SkillHub(团队账号)**:
```powershell
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug1>" --changelog "E2E test v1.0.0" --json
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug2>" --changelog "E2E test v1.0.0" --json
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug3>" --changelog "E2E test v1.0.0" --json
```
> 若报 `VERSION_EXISTS`: 递增 version 字段后重传。若报 `SLUG_CONFLICT`: 改名后重传。若报 `401`: 重新执行阶段 3.1。

**ClawHub**:
```powershell
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug1>" --changelog "E2E test v1.0.0" --json
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug2>" --changelog "E2E test v1.0.0" --json
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug3>" --changelog "E2E test v1.0.0" --json
```

**验收**: 两端均返回 success。

#### 4.6 验证 SkillHub AI 评分
```powershell
python C:\Users\thcd\.skillhub\skills_store_cli.py skill evaluation <slug1> --json
python C:\Users\thcd\.skillhub\skills_store_cli.py skill evaluation <slug2> --json
python C:\Users\thcd\.skillhub\skills_store_cli.py skill evaluation <slug3> --json
```
**验收**: SkillHub 平台 AI 评分≥4.5(5分制)或≥45(50分制)。若暂无评分(pending_review)，记录状态，用 TRACE 分数(≥45)作为质量代理指标。

#### 4.7 重新发现相似 skill(验证去重+升级环)
```powershell
python multi_source_discover.py --source github
# 验证 sources 表关联
python -c "import sys;sys.path.insert(0,r'd:\skills\config');from project_config import get_db_connection;c=get_db_connection();rows=c.execute('SELECT original_slug,skill_id FROM sources WHERE skill_id IS NOT NULL ORDER BY id DESC LIMIT 10').fetchall();[print(r) for r in rows]"
```

#### 4.8 升级本地 skill(使用修复后的 v3)
```powershell
cd d:\skills\tools
python skill_batch_upgrader_v3.py fix --slug <slug1>
python skill_batch_upgrader_v3.py fix --slug <slug2>
python skill_batch_upgrader_v3.py fix --slug <slug3>
python skill_batch_upgrader_v3.py report
# 升级后重跑质量门
python quality_gate.py "d:\skills\packaged-skills\skillhub\<slug1>" --json
python quality_gate.py "d:\skills\packaged-skills\skillhub\<slug2>" --json
python quality_gate.py "d:\skills\packaged-skills\skillhub\<slug3>" --json
```
> 若 fix 修改了内容，需将 SKILL.md frontmatter 的 `version` 从 `1.0.0` 递增至 `1.1.0`。

#### 4.9 重新上传(版本递增后)
```powershell
# SkillHub
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug1>" --changelog "E2E upgrade v1.1.0" --json
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug2>" --changelog "E2E upgrade v1.1.0" --json
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug3>" --changelog "E2E upgrade v1.1.0" --json

# ClawHub
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug1>" --changelog "E2E upgrade v1.1.0" --json
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug2>" --changelog "E2E upgrade v1.1.0" --json
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug3>" --changelog "E2E upgrade v1.1.0" --json
```
**验收**: 重传 success; DB 中每个 slug 有 2 条成功记录(v1.0.0 + v1.1.0)，评分历史保留(D5 is_current 版本化)。

---

### 阶段 5: 创建 V4 计划

**文件**: `d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v4.md`

**V4 计划需包含**:
1. **修正 V3 进度表**: 第5轮(A1-A3)状态从 "待执行" 改为 "已完成"
2. **记录 L1-L8 清理实测修正**: config\__pycache__ 补入; 3个DB备份(含pre-v42-fix); 2个0字节空DB; 3个旧脚本
3. **记录新发现问题及修复**: skill_batch_upgrader_v2.py 缺失(已重建); auto_publish.py Windows兼容性(已修复)
4. **E2E 测试结论**: 3个skill全链路结果、TRACE分数、双平台上传状态、升级环验证
5. **平台认证状态**: SkillHub/ClawHub 认证修复过程和最终状态
6. **遗留项追踪**:
   - D4 剩余 15 个文件的裸 SQL 收口(分批后续)
   - L7(791个 generation_report)评估结论
   - auto_publish.py 其他 npx 调用点一致性
7. **下一阶段建议**: 裸 SQL 收口批次计划 / 大规模批量上传运营计划

---

### 阶段 6: 生成 Round 7 提示词

**文件**: `d:\skills\.trae\documents\round7-prompt.md`

**内容大纲**:
- **标题**: 第7轮提示词(E2E全链路验证与遗留项处理)
- **背景**: L1-L8清理完成; skill_batch_upgrader_v2.py缺失已修复; auto_publish.py已修复; 平台已认证; E2E全链路验证结果
- **任务块**:
  - 若 E2E 测试发现新 bug: 针对性修复
  - 若 E2E 测试通过: D4 剩余 15 个文件裸 SQL 收口批次处理
  - npx clawhub 调用点 registry 参数一致性检查
- **约束**: 无 mock/真实数据/仅团队账号
- **验收标准**: 视任务内容而定
- **完成后输出**: 下一轮提示词(或收尾)

---

## 三、假设与决策

| # | 决策 | 理由 |
|---|------|------|
| 1 | 清理清单以实测为准，不照搬 round6 提示词 | round6 有漏项(config\__pycache__)和过期项 |
| 2 | 先修复 skill_batch_upgrader_v2.py 缺失 | v3 无法运行，阻塞 E2E 升级步骤(4.8) |
| 3 | SkillHub 上传使用 Python CLI 直调 | auto_publish.py 的 `npx skillhub` 在 Windows 上不可用 |
| 4 | auto_publish.py 修复仅改命令构造，不改错误处理 | Python CLI 输出格式与 npx 版本一致 |
| 5 | TRACE 评分走 export→AI 评分→import 全流程 | 静态分只覆盖 T+C(上限~20)，要达到≥45 必须补全 R+A+E |
| 6 | AI 评分由执行代理完成 | TRACE 评分器不直接调用 LLM API |
| 7 | ClawHub 认证若失败需用户手动 login | device flow 需浏览器交互 |
| 8 | 仅使用团队账号(orgId=862) | 用户明确要求 |
| 9 | 测试 3 个 skill(每源 1 个) | 覆盖 3 种发现器，规模适中 |

---

## 四、风险与应对

| 风险 | 概率 | 应对 |
|------|------|------|
| skill_batch_upgrader_v2.py 重建后函数行为与预期不符 | 中 | 阶段1.0修复后用基线skill验证; parse_skill_md复用skill_core.parser |
| SkillHub login 仍失败(401) | 低 | 删除 credentials.json 后重新 login |
| ClawHub login 需浏览器交互 | 中 | 提示用户手动完成; 若无法完成则仅测 SkillHub 端 |
| from-candidate 生成质量门不过 | 中 | 用 skill_batch_upgrader_v3.py fix 修复后重跑 |
| TRACE 总分<45 | 中 | 重点优化 effectiveness 维度 |
| 上传报 VERSION_EXISTS | 低 | 递增 version 字段后重传 |
| 上传报 SLUG_CONFLICT | 低 | 改名后重传 |
| 发现器无新候选 | 低 | 切换至 hermes 源或扩展 github 关键词 |
| SkillHub AI 评分暂无(pending_review) | 中 | 记录状态; 用 TRACE 分数作为质量代理指标 |

---

## 五、验证步骤汇总

| 阶段 | 验证项 | 验证方法 |
|------|--------|---------|
| 0 | V3 计划全部修复已落地 | 代码 grep + DB schema 检查 |
| 1.0 | skill_batch_upgrader_v3 可运行 | `import skill_batch_upgrader_v3` 无报错 |
| 1 | 清理后核心功能无回归 | py_compile + quality_gate 3个基线 + ops闭环 + batch_l2_eval |
| 2 | auto_publish.py Windows 兼容 | py_compile + dry-run 测试 |
| 3 | 双平台认证成功 | SkillHub whoami 非401; ClawHub whoami 非 invalid |
| 4.1 | 3个候选skill发现成功 | candidates_unified.json 有3条新记录 |
| 4.2 | 3个skill生成成功 | packaged-skills/skillhub/<slug>/SKILL.md 存在 |
| 4.3 | 质量门全通过 | 3个 overall_passed=true |
| 4.4 | TRACE 总分≥45 | DB scores 表 total_score≥45 |
| 4.5 | 双平台上传成功 | 两端返回 success |
| 4.6 | SkillHub AI 评分≥4.5 | skill evaluation 命令返回评分≥4.5 |
| 4.7 | 发现去重+sources关联 | sources 表 skill_id 关联>0 |
| 4.8 | 升级后质量门无回归 | quality_gate 仍通过 |
| 4.9 | 重传成功+历史保留 | DB有2条上传记录, scores有is_current版本化 |
| 5 | V4 计划创建 | 文件存在且内容完整 |
| 6 | Round 7 提示词生成 | 文件存在且包含完整任务块 |

---

## 六、执行顺序与依赖关系

```
阶段0 (V3核验)
  |
  v
阶段1 (L1-L8清理 + v2修复)  <-- v2修复是E2E的前置依赖
  |
  +---> 阶段2 (auto_publish.py修复)  <-- 独立，可并行
  |
  +---> 阶段3 (平台认证)  <-- 独立，可并行
  |
  v
阶段4 (E2E测试)  <-- 依赖阶段1(v2修复)、阶段3(认证)
  |
  v
阶段5 (V4计划)  <-- 依赖阶段4结果
  |
  v
阶段6 (Round7提示词)  <-- 依赖阶段5
```

---

## 七、关键文件路径索引

| 用途 | 路径 |
|------|------|
| V3 计划 | `d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v3.md` |
| 参考方案 | `d:\skills\.trae\documents\round6-cleanup-e2e-test-v4-plan.md` |
| 详细研究 | `d:\skills\.trae\documents\round6-cleanup-e2e-v4-implementation-plan.md` |
| V4 计划(待建) | `d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v4.md` |
| Round 7 提示词(待建) | `d:\skills\.trae\documents\round7-prompt.md` |
| 发现器 | `d:\skills\tools\multi_source_discover.py` |
| 生成器 | `d:\skills\tools\generate_skill.py` |
| 质量门 | `d:\skills\tools\quality_gate.py` |
| TRACE 评分器 | `d:\skills\tools\trace_llm_scorer.py` |
| 升级器 v3 | `d:\skills\tools\skill_batch_upgrader_v3.py` |
| 升级器 v2(待建) | `d:\skills\tools\skill_batch_upgrader_v2.py` |
| 自动发布 | `d:\skills\tools\auto_publish.py` |
| 配置 SSOT | `d:\skills\config\project_config.py`、`d:\skills\config\platform_config.py` |
| SkillHub CLI | `C:\Users\thcd\.skillhub\skills_store_cli.py` |
| SkillHub 凭证 | `C:\Users\thcd\.skillhub\credentials.json` |
| 活跃 DB | `d:\skills\skill-registry.db` |
| 候选输出 | `d:\skills\data\discovery\candidates_unified.json` |
| 生成产物 | `d:\skills\packaged-skills\skillhub\<slug>\SKILL.md` |
| 归档目录(DB) | `d:\skills\data\archive\`(待创建) |
| 归档目录(文档) | `d:\skills\.trae\documents\archive\`(待创建) |
