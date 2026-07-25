# Round 6 清理 + auto_publish.py 修复 + 平台认证 + 全链路 E2E 测试 + V4 计划 实施方案

> 基于代码实测研究(非文档承诺)，覆盖 L1-L8 清理、Windows 兼容性修复、平台重新认证、全链路 E2E 测试、V4 计划创建、Round 7 提示词生成。
> 约束: 禁止 mock/TODO/pass/fallback; 真实上传; 仅团队账号(orgId=862); AI 评分>=4.5(TRACE>=45/50)

---

## 一、当前状态分析(基于代码实测)

### 1.1 Round 6 清理状态: 全部未开始(实测确认)

| 清理项 | 实测文件清单 | 大小 | 处置 |
|--------|------------|------|------|
| L1: __pycache__ 目录 | `config\__pycache__`、`tools\__pycache__`、`tools\skill_core\__pycache__` | ~1.2MB | 删除 |
| L2: 0字节空 DB 文件 | `data\skill-registry.db`(0B)、`data\skills.db`(0B) | 0 | 删除 |
| L3: 0字节空脚本 | `tools\parse_report.py`(0B) | 0 | 删除 |
| L4: DB 备份(3个) | `data\backups\skill-registry.db.pre-v42-fix-20260724130053`(11.7MB)、`data\backups\skill-registry_phase3_backup_20260724_120254.db`(11.7MB)、`data\backups\skill-registry_pre_pricing_v34_backup.db`(7.9MB) | ~31.4MB | 归档到 `data\archive\` |
| L5: 过期报告 | `tools\update-report.json` | 小 | 删除 |
| L6: 版本化旧脚本 | `tools\batch_approve_v2.js`、`tools\batch_operations_v2.py`、`tools\update_v2_and_report.py` | ~21KB | 删除 |
| L7: 被取代文档(4个) | `.trae\documents\P0-pipeline-breakage-fix-plan.md`、`.trae\documents\round5-prompt-and-review.md`、`.trae\documents\skill-automation-comprehensive-audit-and-fix-plan.md`、`.trae\documents\skill-automation-comprehensive-fix-plan-v2.md` | ~530KB | 归档到 `.trae\documents\archive\` |
| L8: 综合回归验证 | 清理后全量验证 | - | py_compile + quality_gate + ops闭环 |

**实测发现**: `data\archive\` 目录不存在(需创建); 所有待清理文件均确认存在。

### 1.2 auto_publish.py Windows 兼容性问题(实测确认)

| 文件 | 行号 | 问题代码 | 影响 |
|------|------|---------|------|
| `tools\auto_publish.py` | 119-120 | `cmd = f'npx skillhub publish "{skill_dir}" --changelog "Automated publish"'` | Windows 上 `npx skillhub` 不存在(npm 包未安装)，CLI 实际是 Python 脚本 |

**实测确认**: 全项目仅 `auto_publish.py` 1处使用 `npx skillhub`; SkillHub CLI 实际路径为 `C:\Users\thcd\.skillhub\skills_store_cli.py`(Python 脚本)。

### 1.3 平台认证状态

| 平台 | 凭证位置 | 实测凭证 | 状态 |
|------|---------|---------|------|
| SkillHub | `C:\Users\thcd\.skillhub\credentials.json` | orgId=862, orgName=科创少年, apiKey=`sk-ent-a760...` | 需重新 login(可能过期) |
| ClawHub | `%APPDATA%\clawhub\config.json` | token=`clh_PNX0...`, registry=`https://mirror-cn.clawhub.com` | 需验证 whoami |

### 1.4 关键阻塞问题: skill_batch_upgrader_v3.py 无法运行(新发现)

| 文件 | 行号 | 问题 | 影响 |
|------|------|------|------|
| `tools\skill_batch_upgrader_v3.py` | 37-42 | `from skill_batch_upgrader_v2 import (SECTION_MAP, DOMESTIC_ALTERNATIVES, parse_skill_md, ...)` | **ModuleNotFoundError** - v2 文件不存在(git 历史中也没有) |

**实测验证**: `python -c "import skill_batch_upgrader_v3"` 返回 `ModuleNotFoundError: No module named 'skill_batch_upgrader_v2'`。

v3 从 v2 导入 10 个符号(SECTION_MAP, DOMESTIC_ALTERNATIVES, parse_skill_md, find_section_header, check_missing_sections, extract_section_content, rename_section, optimize_description, generate_section_content, upgrade_skill)，其中 `parse_skill_md` 在 auto_fix 中被调用 14 处，`optimize_description` 在 auto_fix(line 928) 中被调用。

**E2E 影响**: 阻塞步骤 3.8(升级本地 skill)，必须在本轮修复。

### 1.5 V3 计划进度表偏差

`skill-automation-comprehensive-fix-plan-v3.md` 第 17 行标注 "第5轮 | A1-A3 | 待执行"，但代码实测确认 A1-A3 已全部落地:
- A1: `generate_skill.py` 的 `llm_generated` 标志已修正
- A2: `ops闭环.py` 已增加 fix_action 修复动作建议
- A3: `trace_llm_scorer.py:43-44` 已从 skill_core 导入 RESERVED_WORDS

V4 计划需修正此状态为 "已完成"。

### 1.6 关键基础设施确认

| 组件 | 路径/状态 |
|------|----------|
| 活跃 DB | `d:\skills\skill-registry.db`(12.8MB, 2882 skills) |
| SkillHub CLI | `C:\Users\thcd\.skillhub\skills_store_cli.py`(支持 publish/login/auth whoami/skill evaluation) |
| SkillHub 凭证 | `C:\Users\thcd\.skillhub\credentials.json`(org: 科创少年, orgId: 862, apiKey: sk-ent-...) |
| ClawHub CLI | `npx clawhub`(token: clh_PNX0...) |
| TRACE 评分器 | static(T+C维度) + export/import(R+A+E维度需AI评分) |
| 生成器 | `generate_skill.py from-candidate`(支持 --template --description --skip-dep-verify) |
| 发现器 | `multi_source_discover.py --source github/awesome/hermes` |
| 质量门 | `quality_gate.py`(13项检查，使用 skill_core) |

---

## 二、实施计划(6个阶段)

### 阶段 0: V3 计划完整性核验(只读)

**目标**: 确认前 5 轮修复全部落地，建立基线。

**0.1 核验命令(PowerShell)**
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
# 核心脚本语法(注意: skill_batch_upgrader_v3.py 预期失败，阶段1修复后重测)
python -m py_compile d:\skills\tools\quality_gate.py d:\skills\tools\trace_llm_scorer.py d:\skills\tools\generate_skill.py d:\skills\tools\multi_source_discover.py d:\skills\tools\ops闭环.py d:\skills\tools\batch_l2_eval.py

# 3 个基线 skill 质量门
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Creative\free\ad-creative-intel-free" --json
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Creative\free\agentvibes-skill-free" --json
python d:\skills\tools\quality_gate.py "d:\skills\hermes-skills\Agents\free\agent-assistant-free" --json
```

**验收**: A1-A3 已落地、Q5 medium 级 fail、D5 有 is_current、D1 JOIN>0、语法无误(除 v3 外)、基线 skill 无回归。

---

### 阶段 1: L1-L8 冗余文件清理 + 关键阻塞修复

> 以实测清单为准。先修复 skill_batch_upgrader_v3.py 阻塞问题(新发现)，再执行清理。

**1.0 修复 skill_batch_upgrader_v3.py 缺失依赖(新发现阻塞问题)**

**问题**: `tools\skill_batch_upgrader_v3.py:37-42` 导入 `skill_batch_upgrader_v2`，但该文件不存在(git 历史中也没有)。

**修复方案**: 创建 `tools\skill_batch_upgrader_v2.py`，实现 v3 所需的 10 个符号。

**文件**: `d:\skills\tools\skill_batch_upgrader_v2.py`(新建)

**需实现的符号清单(基于 v3 代码分析)**:
1. `SECTION_MAP` - 章节映射常量(dict)
2. `DOMESTIC_ALTERNATIVES` - 国内替代品映射(dict)
3. `parse_skill_md(content)` - 解析 SKILL.md frontmatter 和 body(返回 (fm_dict, body_str))
4. `find_section_header(body, section_name)` - 查找章节标题位置
5. `check_missing_sections(fm, body)` - 检查缺失章节
6. `extract_section_content(body, section_name)` - 提取章节内容
7. `rename_section(body, old_name, new_name)` - 重命名章节
8. `optimize_description(fm)` - 优化 description(返回 (new_fm, changed_bool))
9. `generate_section_content(section_name, skill_data)` - 生成章节内容
10. `upgrade_skill(skill_md_path)` - 综合升级 skill

**实现要点**:
- `parse_skill_md` 复用 `skill_core.parser.parse_frontmatter`(单一来源原则)
- `optimize_description` 实现: 检查 description 长度是否在 150-280 范围内(MIN_DESCRIPTION_LEN/MAX_DESCRIPTION_LEN 从 project_config 导入)，过短则补充默认描述，过长则截断
- `SECTION_MAP` 包含标准章节映射: 能力清单/使用场景/操作步骤/依赖说明/注意事项 等
- `DOMESTIC_ALTERNATIVES` 包含国外服务到国内服务的映射: GitHub→Gitee, OpenAI→通义千问 等
- 其他函数基于 SKILL.md 标准结构实现实际的章节操作逻辑

**验证**:
```powershell
python -m py_compile d:\skills\tools\skill_batch_upgrader_v2.py
python -c "import sys; sys.path.insert(0, r'd:\skills\tools'); sys.path.insert(0, r'd:\skills\config'); import skill_batch_upgrader_v3; print('v3 import OK')"
python d:\skills\tools\skill_batch_upgrader_v3.py fix --slug ad-creative-intel-free
```

**1.1 L1: 删除 3 个 __pycache__ 目录(~1.2MB)**
```powershell
Remove-Item -Recurse -Force d:\skills\config\__pycache__
Remove-Item -Recurse -Force d:\skills\tools\__pycache__
Remove-Item -Recurse -Force d:\skills\tools\skill_core\__pycache__
# 验证
(Get-ChildItem -Recurse -Directory -Filter __pycache__ d:\skills\config,d:\skills\tools -ErrorAction SilentlyContinue).Count  # 预期 0
python -c "import sys;sys.path.insert(0,r'd:\skills\config');from project_config import DB_PATH;print('config import OK')"
```

**1.2 L2: 删除 2 个 0字节空 DB 文件**
```powershell
Remove-Item d:\skills\data\skill-registry.db -Force
Remove-Item d:\skills\data\skills.db -Force
# 验证: 活跃 DB 仍在
(Get-Item d:\skills\skill-registry.db).Length  # 预期 >0 (12886016)
Test-Path d:\skills\data\skill-registry.db     # 预期 False
```

**1.3 L3: 删除 0字节空脚本**
```powershell
Remove-Item d:\skills\tools\parse_report.py -Force
Test-Path d:\skills\tools\parse_report.py  # 预期 False
```

**1.4 L4: 归档 3 个 DB 备份(~31.4MB)**
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

**1.5 L5: 删除过期报告**
```powershell
Remove-Item d:\skills\tools\update-report.json -Force
Test-Path d:\skills\tools\update-report.json  # 预期 False
```

**1.6 L6: 删除 3 个版本化旧脚本(~21KB)**
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

**1.7 L7: 归档被取代的文档(4个)**
```powershell
New-Item -ItemType Directory -Force -Path d:\skills\.trae\documents\archive | Out-Null
Move-Item d:\skills\.trae\documents\P0-pipeline-breakage-fix-plan.md d:\skills\.trae\documents\archive\ -Force
Move-Item d:\skills\.trae\documents\round5-prompt-and-review.md d:\skills\.trae\documents\archive\ -Force
Move-Item d:\skills\.trae\documents\skill-automation-comprehensive-audit-and-fix-plan.md d:\skills\.trae\documents\archive\ -Force
Move-Item d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v2.md d:\skills\.trae\documents\archive\ -Force
# 验证
(Get-ChildItem d:\skills\.trae\documents\archive).Count  # 预期 4
```

**1.8 L8: 综合回归验证**
```powershell
# 全部核心脚本语法(含修复后的 v3)
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

**验收**: __pycache__ 全部删除、空文件删除、DB 备份归档、旧脚本删除、文档归档、skill_batch_upgrader_v3 可运行、核心脚本语法通过、基线 skill 无回归。

---

### 阶段 2: 修复 auto_publish.py Windows 兼容性

**目标**: 将 `npx skillhub publish` 替换为 Python CLI 直调，使 auto_publish.py 在 Windows 上可用。

**文件**: `d:\skills\tools\auto_publish.py`

**修改位置**: 第 119-120 行 `publish_to_skillhub` 函数

**当前代码(第119-120行)**:
```python
    # 执行上传 (使用 npx skillhub 确保 CLI 可用)
    cmd = f'npx skillhub publish "{skill_dir}" --changelog "Automated publish"'
```

**修改为**:
```python
    # 执行上传 (使用 Python CLI 直调，Windows 兼容)
    # SkillHub CLI 实际是 Python 脚本: C:\Users\thcd\.skillhub\skills_store_cli.py
    # npx skillhub 是 npm 包，Windows 上不可用
    skillhub_cli = r"C:\Users\thcd\.skillhub\skills_store_cli.py"
    cmd = f'python "{skillhub_cli}" publish "{skill_dir}" --changelog "Automated publish"'
```

**验证**:
```powershell
python -m py_compile d:\skills\tools\auto_publish.py
# dry-run 测试(不实际上传)
python d:\skills\tools\auto_publish.py publish-skillhub ad-creative-intel-free --dry-run
```

**注意**: 仅修改 `publish_to_skillhub` 函数中的命令构造; 错误处理逻辑(VERSION_EXISTS/SLUG_CONFLICT/429/401 等解析)保持不变，因为 Python CLI 的输出格式与 npx 版本一致。

---

### 阶段 3: 平台重新认证

**3.1 SkillHub 重新登录(团队账号)**
```powershell
# 从 credentials.json 读取企业 API key
$cred = Get-Content C:\Users\thcd\.skillhub\credentials.json -Raw | ConvertFrom-Json
$orgKey = $cred.orgs.'org-xxo535hs'.apiKey  # sk-ent-a760... 格式
python C:\Users\thcd\.skillhub\skills_store_cli.py login --key $orgKey
# 验证
python C:\Users\thcd\.skillhub\skills_store_cli.py auth whoami
```
> 仅使用团队企业 key `sk-ent-...`，不使用个人 `skh_` token。

**3.2 ClawHub 认证验证**
```powershell
# 先测试现有 token 是否可用
npx clawhub whoami
# 若返回 "user: invalid value" 或失败，则重新登录:
# npx clawhub login  (device flow，可能需浏览器交互)
# 验证
npx clawhub whoami
```

**3.3 认证连通性确认**
```powershell
# SkillHub: 列出已安装 skill(只读)
python C:\Users\thcd\.skillhub\skills_store_cli.py list --limit 1
# ClawHub: whoami 返回用户名
npx clawhub whoami
```

**验收**: SkillHub `whoami` 返回用户信息(非 401); ClawHub `whoami` 返回用户名(非 "invalid value")。

---

### 阶段 4: 全链路 E2E 测试

> 3 个 skill 分别来自 github/awesome/hermes 三个源，覆盖全部发现器。无 mock，真实上传，仅团队账号。

**4.1 发现 3 个候选 skill**
```powershell
cd d:\skills\tools
python multi_source_discover.py --source github
python multi_source_discover.py --source awesome
python multi_source_discover.py --source hermes
# 查看统一候选输出
python -c "import json; data=json.load(open(r'd:\skills\data\discovery\candidates_unified.json')); [print(f\"{c['source']:10s} | {c['source_id']:40s} | {c['name'][:50]}\") for c in data[:20]]"
```
从输出挑选 3 个候选(每源 1 个)，记为 `$S1`(github)、`$S2`(awesome)、`$S3`(hermes)。

**选择标准**: 未在本地 DB 中注册的 slug; description 可提取 150-280 字符; 分类明确。

**4.2 生成 3 个 skill**
```powershell
cd d:\skills\tools
python generate_skill.py from-candidate <slug1> --template tool_wrapper_template --description "<desc1 150-280字符>" --skip-dep-verify
python generate_skill.py from-candidate <slug2> --template tool_wrapper_template --description "<desc2>" --skip-dep-verify
python generate_skill.py from-candidate <slug3> --template tool_wrapper_template --description "<desc3>" --skip-dep-verify
```
> 生成产物: `d:\skills\packaged-skills\skillhub\<slug>\SKILL.md`。`--skip-dep-verify` 因新 skill 无外部依赖。

**4.3 质量门(13 项检查)**
```powershell
python d:\skills\tools\quality_gate.py "d:\skills\packaged-skills\skillhub\<slug1>" --json
python d:\skills\tools\quality_gate.py "d:\skills\packaged-skills\skillhub\<slug2>" --json
python d:\skills\tools\quality_gate.py "d:\skills\packaged-skills\skillhub\<slug3>" --json
```
**验收**: 3 个 `overall_passed=true`。若 fail，用 `skill_batch_upgrader_v3.py fix --slug <slug>` 修复后重跑，迭代至全过。

**4.4 TRACE 评分达>=45/50**

> 静态分只覆盖 T+C(上限~20)，达标必须走 export->AI 评分->import 全流程。

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
读取导出 JSON 中这 3 个 skill 的内容，按 5 个 TRACE 维度打分:
- T (Trust, /10): 信任度 - 无虚假声明、无夸大词、依赖说明透明
- R (Reliability, /10): 可靠性 - 逻辑完整、错误处理充分、边界条件覆盖
- A (Adaptability, /10): 适应性 - 可适配不同场景、参数灵活、扩展性好
- C (Convention, /10): 规范性 - frontmatter 完整、格式标准、命名规范
- E (Effectiveness, /10): 有效性 - 实际解决问题、用户价值高、操作可行

产出 `d:\skills\data\reports\trace_e2e_results.json`，schema:
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
> trust 与 convention 会与静态分取 max。总分须>=45(A+ 级 = 4.5/5.0)。

**Step D: 导入评分**
```powershell
python trace_llm_scorer.py import d:\skills\data\reports\trace_e2e_results.json
python trace_llm_scorer.py report
```
**验收**: DB 中这 3 个 skill 的 `total_score>=45`。若<45，回到 4.2/4.3 用 upgrader 优化 SKILL.md 内容后重评，迭代直至>=45。

**4.5 上传双平台(真实上传)**

**SkillHub(团队账号) - 使用 Python CLI 直调**
```powershell
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug1>" --changelog "E2E test v1.0.0" --json
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug2>" --changelog "E2E test v1.0.0" --json
python C:\Users\thcd\.skillhub\skills_store_cli.py publish "d:\skills\packaged-skills\skillhub\<slug3>" --changelog "E2E test v1.0.0" --json
```
> 若报 `VERSION_EXISTS`: 递增 SKILL.md frontmatter 的 version 字段后重传。若报 `SLUG_CONFLICT`: 改名为唯一 slug 后重传。若报 `401`: 重新执行阶段 3.1。

**ClawHub**
```powershell
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug1>" --changelog "E2E test v1.0.0"
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug2>" --changelog "E2E test v1.0.0"
npx clawhub publish "d:\skills\packaged-skills\skillhub\<slug3>" --changelog "E2E test v1.0.0"
```

**验收**: 两端均返回 success。记录上传结果到 DB。

**4.6 验证 SkillHub AI 评分**
```powershell
# 查询 SkillHub 平台 AI 评分(上传后需等待审核)
python C:\Users\thcd\.skillhub\skills_store_cli.py skill evaluation <slug1>
python C:\Users\thcd\.skillhub\skills_store_cli.py skill evaluation <slug2>
python C:\Users\thcd\.skillhub\skills_store_cli.py skill evaluation <slug3>
```
**验收**: SkillHub 平台 AI 评分>=4.5(若平台使用 5 分制)或>=45(若使用 50 分制)。若暂无评分(pending_review)，记录状态并等待。

**4.7 重新发现相似 skill(验证发现去重+升级环)**
```powershell
# 再次跑发现，刚上传的 skill 应被去重逻辑识别为"已存在"
python multi_source_discover.py --source github
# 验证 sources 表对这 3 个 slug 已关联 skill_id(D1 修复链路)
python -c "import sys;sys.path.insert(0,r'd:\skills\config');from project_config import get_db_connection;c=get_db_connection();rows=c.execute('SELECT original_slug,skill_id FROM sources WHERE skill_id IS NOT NULL ORDER BY id DESC LIMIT 10').fetchall();[print(r) for r in rows]"
```

**4.8 升级本地 skill(使用修复后的 v3)**
```powershell
cd d:\skills\tools
# 针对这 3 个 skill 修复+优化
python skill_batch_upgrader_v3.py fix --slug <slug1>
python skill_batch_upgrader_v3.py fix --slug <slug2>
python skill_batch_upgrader_v3.py fix --slug <slug3>
python skill_batch_upgrader_v3.py report
# 升级后重跑质量门，确认无回归
python quality_gate.py "d:\skills\packaged-skills\skillhub\<slug1>" --json
python quality_gate.py "d:\skills\packaged-skills\skillhub\<slug2>" --json
python quality_gate.py "d:\skills\packaged-skills\skillhub\<slug3>" --json
```
> 若 fix 修改了内容，需将 SKILL.md frontmatter 的 `version` 从 `1.0.0` 递增至 `1.1.0`(否则 4.9 重传报 VERSION_EXISTS)。

**4.9 重新上传(版本递增后)**
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
**验收**: 重传 success; DB 中每个 slug 有 2 条成功记录(v1.0.0 + v1.1.0)，评分历史保留(D5 is_current 版本化)。

---

### 阶段 5: 创建 V4 计划

**文件**: `d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v4.md`

**V4 计划需包含**:

1. **修正 V3 进度表**: 将第 5 轮(A1-A3)状态从 "待执行" 改为 "已完成"(以代码事实为准)
2. **记录 L1-L8 清理的实测修正**:
   - `config\__pycache__` 补入 L1(round6 漏列)
   - 3 个 DB 备份(含 `pre-v42-fix` 文件)，归档到 `data\archive\`
   - 删除 2 个 0 字节空 DB 文件(`data\skill-registry.db`、`data\skills.db`)
   - 删除 3 个旧脚本(`batch_approve_v2.js`、`batch_operations_v2.py`、`update_v2_and_report.py`)
3. **记录新发现问题**: skill_batch_upgrader_v2.py 缺失(已修复)
4. **记录 auto_publish.py Windows 兼容性修复**: `npx skillhub` -> Python CLI 直调
5. **E2E 测试结论章节**: 记录 3 个 skill 全链路结果、TRACE 分数、双平台上传状态、升级环验证
6. **平台认证状态**: 记录 SkillHub/ClawHub 认证修复过程和最终状态
7. **遗留项追踪**:
   - D4 剩余 15 个文件的裸 SQL 收口(本轮未处理，分批后续)
   - L7(791 个 generation_report)评估结论
   - 其他 npx clawhub 调用点(automated_review_system.py:52, batch_delete_clawhub.py:29, clawhub_batch_uploader.py:95, version_sync_pipeline.py:624/637)的 registry 参数一致性
8. **下一阶段建议**: 裸 SQL 收口批次计划 / 大规模批量上传运营计划

---

### 阶段 6: 生成 Round 7 提示词

**文件**: `d:\skills\.trae\documents\round7-prompt.md`

**Round 7 提示词内容大纲**:

- **标题**: 第 7 轮提示词(E2E 全链路验证与遗留项处理)
- **背景**: L1-L8 清理已完成(附实测修正清单)，skill_batch_upgrader_v2.py 缺失已修复，auto_publish.py Windows 兼容性已修复，平台已重新认证，E2E 全链路验证结果
- **任务块**:
  - 若 E2E 测试发现新 bug: 针对性修复提示词
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
| 2 | 先修复 skill_batch_upgrader_v2.py 缺失问题 | v3 无法运行，阻塞 E2E 升级步骤(4.8) |
| 3 | SkillHub 上传使用 Python CLI 直调，不用 auto_publish.py | auto_publish.py 使用 `npx skillhub`(npm 包)，Windows 上不兼容; CLI 实际是 Python 脚本 |
| 4 | auto_publish.py 修复仅改命令构造，不改错误处理 | Python CLI 输出格式与 npx 版本一致 |
| 5 | TRACE 评分走 export->AI 评分->import 全流程 | 静态分只覆盖 T+C(上限~20)，要达到>=45 必须补全 R+A+E 维度 |
| 6 | AI 评分由执行代理(即 AI 会话自身)完成 | TRACE 评分器不直接调用 LLM API，需手动评估后导入 |
| 7 | ClawHub 认证若失败需用户手动 login | `npx clawhub login` 使用 device flow，需浏览器交互 |
| 8 | 仅使用团队账号(orgId=862) | 用户明确要求 "本次测试只考虑团队号" |
| 9 | 测试 3 个 skill(每源 1 个) | 覆盖 3 种发现器，规模适中，与前序验证一致 |

---

## 四、风险与应对

| 风险 | 概率 | 应对 |
|------|------|------|
| skill_batch_upgrader_v2.py 重建后函数行为与预期不符 | 中 | 阶段1.0 修复后用基线 skill 验证; parse_skill_md 复用 skill_core.parser 确保一致性 |
| SkillHub login 仍失败(401) | 低 | 删除 credentials.json 后重新 login; 确认使用 `sk-ent-` 企业 key |
| ClawHub login 需浏览器交互 | 中 | 提示用户手动完成 `npx clawhub login`; 若无法完成则仅测 SkillHub 端 |
| from-candidate 生成质量门不过 | 中 | 用 `skill_batch_upgrader_v3.py fix --slug` 修复后重跑，迭代至通过 |
| TRACE 总分<45 | 中 | 重点优化 effectiveness 维度; 检查 description 是否充分、依赖说明是否透明 |
| 上传报 VERSION_EXISTS | 低 | 递增 version 字段(1.0.0->1.1.0)后重传 |
| 上传报 SLUG_CONFLICT | 低 | 改名为唯一 slug 后重传 |
| 发现器无新候选(去重后空) | 低 | 切换至 hermes 源(本地仓库必有内容)或扩展 github 关键词 |
| SkillHub AI 评分暂无(pending_review) | 中 | 记录状态; 用 TRACE 分数(>=45)作为质量代理指标 |
| GitHub API 限频(60 次/小时未认证) | 低 | 3 个 skill 的发现请求远低于限额 |

---

## 五、验证步骤汇总

| 阶段 | 验证项 | 验证方法 |
|------|--------|---------|
| 0 | V3 计划全部修复已落地 | 代码 grep + DB schema 检查 |
| 1.0 | skill_batch_upgrader_v3 可运行 | `python -c "import skill_batch_upgrader_v3"` 无报错 |
| 1 | 清理后核心功能无回归 | py_compile + quality_gate 3 个基线 skill + ops闭环 + batch_l2_eval |
| 2 | auto_publish.py Windows 兼容 | py_compile + dry-run 测试 |
| 3 | 双平台认证成功 | SkillHub whoami 非 401; ClawHub whoami 非 invalid |
| 4.1 | 3 个候选 skill 发现成功 | candidates_unified.json 有 3 条新记录 |
| 4.2 | 3 个 skill 生成成功 | packaged-skills/skillhub/<slug>/SKILL.md 存在 |
| 4.3 | 质量门全通过 | 3 个 overall_passed=true |
| 4.4 | TRACE 总分>=45 | DB scores 表 total_score>=45 |
| 4.5 | 双平台上传成功 | 两端返回 success |
| 4.6 | SkillHub AI 评分>=4.5 | skill evaluation 命令返回评分>=4.5 |
| 4.7 | 发现去重+sources 关联 | sources 表 skill_id 关联>0 |
| 4.8 | 升级后质量门无回归 | quality_gate 仍通过 |
| 4.9 | 重传成功+历史保留 | DB 有 2 条上传记录，scores 有 is_current 版本化 |
| 5 | V4 计划创建 | 文件存在且内容完整 |
| 6 | Round 7 提示词生成 | 文件存在且包含完整任务块 |

---

## 六、关键文件路径索引

| 用途 | 路径 |
|------|------|
| V3 计划 | `d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v3.md` |
| 参考方案 | `d:\skills\.trae\documents\round6-cleanup-e2e-test-v4-plan.md` |
| V4 计划(待建) | `d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v4.md` |
| Round 7 提示词(待建) | `d:\skills\.trae\documents\round7-prompt.md` |
| 发现器 | `d:\skills\tools\multi_source_discover.py` |
| 生成器 | `d:\skills\tools\generate_skill.py` |
| 质量门 | `d:\skills\tools\quality_gate.py` |
| TRACE 评分器 | `d:\skills\tools\trace_llm_scorer.py` |
| 升级器 v3 | `d:\skills\tools\skill_batch_upgrader_v3.py` |
| 升级器 v2(待建) | `d:\skills\tools\skill_batch_upgrader_v2.py` |
| 自动发布 | `d:\skills\tools\auto_publish.py`(修复: npx skillhub -> Python CLI) |
| 配置 SSOT | `d:\skills\config\project_config.py`、`d:\skills\config\platform_config.py` |
| SkillHub CLI | `C:\Users\thcd\.skillhub\skills_store_cli.py` |
| SkillHub 凭证 | `C:\Users\thcd\.skillhub\credentials.json` |
| ClawHub 配置 | `%APPDATA%\clawhub\config.json` |
| 活跃 DB | `d:\skills\skill-registry.db`(12.8MB) |
| 候选输出 | `d:\skills\data\discovery\candidates_unified.json` |
| 生成产物 | `d:\skills\packaged-skills\skillhub\<slug>\SKILL.md` |
| 归档目录(DB) | `d:\skills\data\archive\`(待创建) |
| 归档目录(文档) | `d:\skills\.trae\documents\archive\`(待创建) |

---

## 七、执行顺序与依赖关系

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

**关键依赖**: 阶段1的v2修复是阶段4.8(升级步骤)的前置条件; 阶段3(认证)是阶段4.5(上传)的前置条件。
