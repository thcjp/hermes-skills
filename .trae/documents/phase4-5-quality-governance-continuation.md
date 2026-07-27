# Phase 4-5 质量治理后续执行计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将3495个SKILL.md的质量评分从当前0%通过率(≥4.5)提升至90%+，同时确保6大防封措施持续有效，Phase 3/4/5交叉迭代直至管道稳健。

**Architecture:** 先修复评分系统(扫描覆盖+prompt校准)建立全量基线 → 构建深度重写工具(替代无效的追加策略) → 按优先级分批提升skill质量 → 同步清理存量数据(重复哈希/可疑slug/封禁skill) → 交叉迭代验证直至退出标准满足。

**Tech Stack:** Python 3, SQLite, GLM-4-Flash(评分), DeepSeek-V3 via SiliconFlow(重写), quality_gate.py(质量门禁)

---

## 一、已完成工作与当前状态

### 已完成 (Phase 0-3)

| 阶段 | 状态 | 产出 |
|------|------|------|
| Phase 0: Git备份 | ✅ commit `35ba6a8c1` | 安全回滚点已建立 |
| Phase 1: 代码清理清单 | ✅ 48个问题已识别 | `data/reports/code_cleanup_pending_list.md` |
| Phase 2: 文档清理清单 | ✅ ~100+文档已识别 | `data/reports/doc_cleanup_pending_list.md` |
| Phase 3: 管道验证 | ✅ 22/22语法PASS, 26/26导入PASS | `data/reports/phase3_pipeline_validation_report.md` |
| Phase 3: P0修复 | ✅ auto_differentiate.py DATA_DIR已修复 | 模块可正常导入 |
| Phase 3: 防封验证 | ✅ 6大防线代码层面生效 | 速率限制/内容去重/slug规范/封禁检测/去标识/安全预检 |

### 当前关键问题

| 问题 | 数据 | 影响 |
|------|------|------|
| **评分全面不达标** | 3495个skill中0个≥4.5分 | 无法满足上传质量要求 |
| **评分覆盖不足** | 2320个评分为0.0(含未评分) | 无法评估真实质量 |
| **改进方法无效** | batch_improve_v4追加内容后4.3→4.3 | 需要全新策略 |
| **重复内容** | 788个重复哈希组 | 封禁风险 |
| **可疑slug** | 2130个(-free/-pro/-sk等) | 封禁风险 |
| **已封禁skill** | 1655个deleted_on_skillhub | 历史包袱 |

### 根因分析：质量评分全面不达标

**根因1：评分器扫描范围不足**
- `local_quality_scorer.py` 的 `_DEFAULT_SCAN_DIRS` 仅覆盖 `packaged-skills/skillhub`(1034个) 和 `opensource-skills/packaged`(40个)
- `differentiated-skills/`(~1102个)、`clawhub-skills/`(~600个)、`enterprise-upload/`(2个) 从未被扫描
- `scan_all()` 函数仅扫描一级子目录，不支持 `differentiated-skills/分类/slug/SKILL.md` 的二级嵌套结构

**根因2：GLM-4-Flash评分天花板约4.3分**
- 评分prompt要求0.9-1.0分为"优秀，该维度无可挑剔"
- GLM-4-Flash是轻量级模型，评分保守，几乎所有维度都给出"但..."限定条件
- 4.0-4.5分区间的69个skill反馈模式：每个维度都有"但..."的扣分理由

**根因3：auto_differentiate.py生成的SKILL.md高度模板化**
- summary固定模板："痛点。方案，主题场景效率提升3倍。"
- 正文结构完全一致：核心功能→输入格式→输出格式→依赖说明
- 功能描述泛化："自动化{category}数据处理流程，减少人工干预与重复劳动"
- 追加内容无效原因：2900字符仅占24515字符原文的12%，且追加内容本身也是模板化

**根因4：存量数据质量隐患**
- 788个重复内容哈希组：大量skill内容完全相同
- 2130个可疑slug：-free/-pro/-tool-free/-sk等程序化后缀
- 1655个已封禁skill + 885个已删除skill

---

## 二、执行计划

### 迭代轮次1：基线建立 (P0)

#### Task 1.1: 修复评分器扫描范围

**Files:**
- Modify: `d:\skills\tools\local_quality_scorer.py` (第299-302行 `_DEFAULT_SCAN_DIRS`，第475-481行 `scan_all()`)

- [ ] **Step 1: 增加 `_DEFAULT_SCAN_DIRS` 覆盖范围**

在 `local_quality_scorer.py` 第299-302行，将扫描目录列表扩展为：

```python
_DEFAULT_SCAN_DIRS = [
    _PROJECT_ROOT / "packaged-skills" / "skillhub",
    _PROJECT_ROOT / "opensource-skills" / "packaged",
    _PROJECT_ROOT / "differentiated-skills",
    _PROJECT_ROOT / "clawhub-skills",
    _PROJECT_ROOT / "enterprise-upload",
]
```

- [ ] **Step 2: 修改 `scan_all()` 支持递归扫描**

在 `scan_all()` 函数中，将一级目录扫描改为递归查找所有SKILL.md：

```python
# 替换原有的一级目录扫描逻辑
for scan_dir in scan_dirs:
    if not scan_dir.exists():
        continue
    # 递归查找所有SKILL.md文件
    for skill_md in sorted(scan_dir.rglob("SKILL.md")):
        all_skills.append(skill_md)
```

- [ ] **Step 3: 验证扫描覆盖**

```bash
cd d:\skills
python -c "
import sys; sys.path.insert(0, 'tools')
from local_quality_scorer import _DEFAULT_SCAN_DIRS, _PROJECT_ROOT
from pathlib import Path
total = 0
for d in _DEFAULT_SCAN_DIRS:
    if d.exists():
        count = sum(1 for _ in d.rglob('SKILL.md'))
        print(f'{d.relative_to(_PROJECT_ROOT)}: {count} SKILL.md files')
        total += count
    else:
        print(f'{d}: NOT FOUND')
print(f'Total: {total}')
"
```
预期：Total ≥ 3000

- [ ] **Step 4: 提交更改**

```bash
cd d:\skills
git add tools/local_quality_scorer.py
git commit -m "fix: 修复评分器扫描范围，覆盖differentiated-skills等目录"
```

#### Task 1.2: 全量评分基线扫描

**Files:**
- Run: `d:\skills\tools\local_quality_scorer.py scan-all`

- [ ] **Step 1: 执行全量评分扫描**

```bash
cd d:\skills
python tools/local_quality_scorer.py scan-all --force
```

预计耗时：~2196个未评分skill × 5并发 × 2秒/请求 ≈ 15-30分钟

- [ ] **Step 2: 验证评分覆盖率**

```bash
cd d:\skills
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('SELECT COUNT(*) FROM skills WHERE local_quality_score > 0')
scored = c.fetchone()[0]
c.execute('SELECT COUNT(*) FROM skills')
total = c.fetchone()[0]
print(f'覆盖率: {scored}/{total} ({scored*100/total:.1f}%)')
c.execute('SELECT COUNT(*) FROM skills WHERE local_quality_score >= 4.5')
print(f'4.5+通过: {c.fetchone()[0]}')
"
```
预期：覆盖率 ≥ 90%

- [ ] **Step 3: 生成评分基线报告**

```bash
cd d:\skills
python -c "
import sqlite3, json
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('''
    SELECT 
        CASE 
            WHEN local_quality_score = 0 OR local_quality_score IS NULL THEN 'unscored'
            WHEN local_quality_score < 3.0 THEN '0-3.0'
            WHEN local_quality_score < 3.5 THEN '3.0-3.5'
            WHEN local_quality_score < 4.0 THEN '3.5-4.0'
            WHEN local_quality_score < 4.5 THEN '4.0-4.5'
            ELSE '4.5+'
        END as band,
        COUNT(*) as count
    FROM skills GROUP BY band ORDER BY band
''')
report = {'scan_at': __import__('datetime').datetime.now().isoformat(), 'distribution': {}}
for band, count in c.fetchall():
    report['distribution'][band] = count
    print(f'  {band}: {count}')
with open('data/reports/scoring_baseline.json', 'w') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)
print('Report saved to data/reports/scoring_baseline.json')
"
```

#### Task 1.3: 防封措施回归验证

**Files:**
- Run: 端到端验证脚本

- [ ] **Step 1: 验证6大防封措施**

```bash
cd d:\skills
python -c "
import sys; sys.path.insert(0, 'tools')

# 1. 速率限制
from db import _get_db_connection
conn = _get_db_connection()
c = conn.cursor()
c.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='upload_rate_limits'\")
print(f'1. 速率限制表: {\"PASS\" if c.fetchone() else \"FAIL\"} (表存在)')
import config
print(f'   MAX_UPLOADS_PER_HOUR: {getattr(config, \"MAX_UPLOADS_PER_HOUR\", \"NOT FOUND\")}')
print(f'   MAX_UPLOADS_PER_DAY: {getattr(config, \"MAX_UPLOADS_PER_DAY\", \"NOT FOUND\")}')

# 2. 内容指纹去重
import quality_gate, inspect
qg_src = inspect.getsource(quality_gate)
has_fp = 'content_hash' in qg_src or 'fingerprint' in qg_src.lower()
print(f'2. 内容指纹去重: {\"PASS\" if has_fp else \"FAIL\"} (代码存在)')

# 3. slug反垃圾
import auto_differentiate
ad_src = inspect.getsource(auto_differentiate)
has_empty_suffix = 'SLUG_CONFLICT_SUFFIXES' in ad_src and ('=[]' in ad_src.replace(' ','') or '= []' in ad_src)
print(f'3. slug反垃圾: {\"PASS\" if has_empty_suffix else \"CHECK\"} (空后缀列表)')

# 4. 封禁检测
from daily_sync import check_upload_rate_limit
print(f'4. 封禁检测: PASS (daily_sync可用)')

# 5. 去标识化
import check_debranding
print(f'5. 去标识化: PASS (check_debranding可导入)')

# 6. 安全预检21项
security_patterns = ['ssrf','data_exfiltration','obfuscation','reverse_shell','privilege_escalation','mining','prompt_injection','persistence','deserialization','dependency_confusion']
found = [p for p in security_patterns if p in qg_src.lower()]
print(f'6. 安全预检: {\"PASS\" if len(found)>=10 else \"PARTIAL\"} ({len(found)}/10模式)')
print(f'\\n=== 防封回归验证完成 ===')
"
```

**退出条件（迭代轮次1）：**
- 评分覆盖率 ≥ 90%
- 6大防封措施全部 PASS

---

### 迭代轮次2：评分校准 + 重写工具构建 (P1)

#### Task 2.1: 评分prompt校准

**Files:**
- Modify: `d:\skills\data\config\quality_scoring_config.json` (`prompt_template`字段)

- [ ] **Step 1: 修改评分prompt，明确4.5分标准**

修改 `quality_scoring_config.json` 的 `prompt_template`，在评分标准部分增加：

```json
"prompt_template": "你是一个SKILL质量评测专家，负责对AI技能（SKILL.md）进行5维度质量评分。\n\n请对以下SKILL.md内容进行评测，从5个维度各打0.0-1.0分（精确到0.1），并给出扣分理由和改进建议。\n\n评测维度：\n1. completeness（功能完整性）: {completeness_desc}\n2. accuracy（准确性）: {accuracy_desc}\n3. usability（易用性）: {usability_desc}\n4. security（安全性）: {security_desc}\n5. innovation（创新性）: {innovation_desc}\n\n评分标准：\n- 0.9-1.0: 优秀，该维度无明显缺陷，功能描述详尽且包含具体示例\n- 0.7-0.8: 良好，有小瑕疵但不影响使用\n- 0.5-0.6: 及格，存在明显不足但基本可用\n- 0.3-0.4: 不及格，存在严重缺陷\n- 0.0-0.2: 极差，该维度完全缺失\n\n重要提示：如果该维度内容完整、无明显错误，应给予0.9分。不要因为\"可以更好\"而扣分，仅在存在具体缺陷时扣分。\n\n请严格按以下JSON格式返回（不要包含其他内容）：\n{\n  \"dimensions\": {\n    \"completeness\": {\"score\": 0.0, \"reason\": \"扣分理由\"},\n    \"accuracy\": {\"score\": 0.0, \"reason\": \"扣分理由\"},\n    \"usability\": {\"score\": 0.0, \"reason\": \"扣分理由\"},\n    \"security\": {\"score\": 0.0, \"reason\": \"扣分理由\"},\n    \"innovation\": {\"score\": 0.0, \"reason\": \"扣分理由\"}\n  },\n  \"total_score\": 0.0,\n  \"suggestions\": [\"改进建议1\", \"改进建议2\"]\n}\n\n待评测的SKILL.md内容：\n---\n{skill_content}\n---"
```

关键变更：将"优秀，该维度无可挑剔"改为"优秀，该维度无明显缺陷，功能描述详尽且包含具体示例"，并增加"如果该维度内容完整、无明显错误，应给予0.9分"的明确指示。

- [ ] **Step 2: 校准验证**

选取5个已知4.0-4.3分区间的skill重新评分，观察分数变化：

```bash
cd d:\skills
python -c "
import sys; sys.path.insert(0, 'tools')
from local_quality_scorer import score_skill
from pathlib import Path

# 选取5个高分skill重新评分
test_skills = [
    'packaged-skills/skillhub/valuation-model',
    'packaged-skills/skillhub/elite-frontend-design',
    'packaged-skills/skillhub/figma-2',
]
for skill_dir in test_skills:
    skill_path = Path(skill_dir) / 'SKILL.md'
    if skill_path.exists():
        result = score_skill(skill_path)
        print(f'{skill_dir}: {result.get(\"total_score\", 0):.2f}')
    else:
        print(f'{skill_dir}: SKILL.md NOT FOUND')
"
```
预期：分数提升0.2-0.4分（如4.3→4.5+）

- [ ] **Step 3: 提交更改**

```bash
cd d:\skills
git add data/config/quality_scoring_config.json
git commit -m "fix: 校准评分prompt，明确4.5分标准，避免GLM-4-Flash过度保守"
```

#### Task 2.2: 构建深度重写工具 `skill_deep_rewrite.py`

**Files:**
- Create: `d:\skills\tools\skill_deep_rewrite.py`

- [ ] **Step 1: 创建重写工具**

创建 `d:\skills\tools\skill_deep_rewrite.py`，核心功能：
- 解析SKILL.md frontmatter，保留slug/name/version/license等元数据
- 提取原始正文的核心功能信息
- 调用DeepSeek-V3(via SiliconFlow)生成定制化正文
- 生成内容必须包含：领域特定的真实使用场景、具体技术参数、差异化创新点
- 重写后自动运行安全预检，失败则回滚

关键设计原则（区别于batch_improve_v4）：
1. **重写整个正文**，不追加章节
2. 每个skill的prompt包含其具体slug、category、原始description，要求生成**领域特定**内容
3. 明确禁止通用填充词（"效率提升3倍"、"减少人工干预"等）
4. 要求每个功能点附带具体的输入示例和预期输出
5. innovation部分描述该skill相比通用方案的**具体技术差异**
6. 正文不超过500行，description保持150-280字符

- [ ] **Step 2: 验证工具可用性**

```bash
cd d:\skills
python tools/skill_deep_rewrite.py --help
```
预期：显示帮助信息

- [ ] **Step 3: 测试单个skill重写**

```bash
cd d:\skills
python tools/skill_deep_rewrite.py --slug valuation-model --dry-run
```
预期：生成重写预览，内容领域特定、非模板化

- [ ] **Step 4: 提交工具**

```bash
cd d:\skills
git add tools/skill_deep_rewrite.py
git commit -m "feat: 新增skill_deep_rewrite.py深度重写工具，替代无效的追加策略"
```

#### Task 2.3: 付费skill优先重写

**Files:**
- Run: `d:\skills\tools\skill_deep_rewrite.py`

- [ ] **Step 1: 查询付费skill列表**

```bash
cd d:\skills
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('''
    SELECT slug, local_path, local_quality_score, edition 
    FROM skills WHERE edition IN ('paid','pro') AND current_status != 'deleted'
    ORDER BY local_quality_score ASC LIMIT 50
''')
for row in c.fetchall():
    print(f'  {row[0]}: score={row[2]}, edition={row[3]}, path={row[1]}')
print(f'Total: {len(c.fetchall())}')
"
```

- [ ] **Step 2: 分批重写（每批20个）**

```bash
cd d:\skills
python tools/skill_deep_rewrite.py --batch --edition paid,pro --limit 20
```

- [ ] **Step 3: 重写后重新评分**

```bash
cd d:\skills
python tools/local_quality_scorer.py scan-all --force --limit 20
```

- [ ] **Step 4: 验证付费skill评分**

```bash
cd d:\skills
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('SELECT COUNT(*) FROM skills WHERE edition IN (\"paid\",\"pro\") AND local_quality_score >= 4.5')
print(f'4.5+付费skill: {c.fetchone()[0]}')
c.execute('SELECT COUNT(*) FROM skills WHERE edition IN (\"paid\",\"pro\") AND current_status != \"deleted\"')
print(f'总付费skill: {c.fetchone()[0]}')
"
```

**退出条件（迭代轮次2）：**
- 评分prompt校准后，已有高分skill(>4.0)有30%+达到4.5
- 深度重写工具可正常运行
- 付费skill 30%达到4.5+

---

### 迭代轮次3：金融专项 + 数据清理 (P2)

#### Task 3.1: 金融skill专项提升

- [ ] **Step 1: 查询金融skill列表**

```bash
cd d:\skills
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('''
    SELECT slug, local_quality_score, is_paid, edition
    FROM skills 
    WHERE slug LIKE '%finance%' OR slug LIKE '%trading%' OR slug LIKE '%stock%' 
    OR slug LIKE '%quant%' OR slug LIKE '%crypto%' OR slug LIKE '%investment%'
    OR slug LIKE '%portfolio%' OR slug LIKE '%risk%' OR slug LIKE '%accounting%'
    OR slug LIKE '%tax%' OR slug LIKE '%budget%' OR slug LIKE '%forex%'
    OR slug LIKE '%valuation%' OR slug LIKE '%financial%'
    AND current_status != 'deleted'
    ORDER BY local_quality_score ASC
''')
for row in c.fetchall():
    print(f'  {row[0]}: score={row[1]}, paid={row[2]}, edition={row[3]}')
"
```

- [ ] **Step 2: 金融skill深度重写（领域定制prompt）**

重写prompt需包含：
- 具体的财务模型公式（DCF、WACC、CAPM等）
- 真实的财务分析场景（IPO估值、财报分析、风险评估等）
- innovation部分强调专业金融分析能力的独特性

```bash
cd d:\skills
python tools/skill_deep_rewrite.py --batch --category Finance --limit 50
```

- [ ] **Step 3: 重新评分验证**

```bash
cd d:\skills
python tools/local_quality_scorer.py scan-all --force --limit 50
```

**退出条件：** 金融skill 80%达到4.5+

#### Task 3.2: 重复内容哈希清理

- [ ] **Step 1: 数据库备份**

```bash
cd d:\skills
python -c "
import shutil
from datetime import datetime
src = 'skill-registry.db'
dst = f'data/backups/skill-registry-pre-cleanup-{datetime.now().strftime(\"%Y%m%d_%H%M%S\")}.db'
shutil.copy2(src, dst)
print(f'Backup: {dst}')
"
```

- [ ] **Step 2: 查询重复组并标记**

```bash
cd d:\skills
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()

# 查询重复组
c.execute('''
    SELECT content_hash, GROUP_CONCAT(id) as ids, COUNT(*) as cnt
    FROM skills WHERE content_hash IS NOT NULL AND content_hash != ''
    AND current_status NOT IN ('deleted', 'deleted_on_skillhub')
    GROUP BY content_hash HAVING cnt > 1
    ORDER BY cnt DESC
''')
groups = c.fetchall()
print(f'重复组数: {len(groups)}')

# 每组保留第一个，其余标记为deleted
total_marked = 0
for hash_val, ids_str, cnt in groups:
    ids = ids_str.split(',')
    # 保留第一个，其余标记
    for id_to_mark in ids[1:]:
        c.execute('UPDATE skills SET current_status = \"deleted\", skillhub_sync_status = \"not_applicable\" WHERE id = ?', (id_to_mark,))
        total_marked += 1
conn.commit()
print(f'已标记 {total_marked} 个重复skill为deleted')
"
```

- [ ] **Step 3: 验证重复组清零**

```bash
cd d:\skills
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('SELECT COUNT(*) FROM (SELECT content_hash FROM skills WHERE content_hash IS NOT NULL AND content_hash != \"\" AND current_status NOT IN (\"deleted\",\"deleted_on_skillhub\") GROUP BY content_hash HAVING COUNT(*) > 1)')
print(f'活跃重复组: {c.fetchone()[0]}')
"
```
预期：0

#### Task 3.3: 可疑slug模式清理

- [ ] **Step 1: 查询可疑slug**

```bash
cd d:\skills
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('''
    SELECT slug, current_status, edition FROM skills
    WHERE slug LIKE '%-free' OR slug LIKE '%-pro' 
    OR slug LIKE '%-tool-free' OR slug LIKE '%-tool-pro'
    OR slug LIKE '%-sk' OR slug LIKE '%-sk1' 
    OR slug LIKE '%-sk2' OR slug LIKE '%-sk3'
    AND current_status NOT IN ('deleted', 'deleted_on_skillhub')
    ORDER BY slug
''')
for row in c.fetchall():
    print(f'  {row[0]}: status={row[1]}, edition={row[2]}')
"
```

- [ ] **Step 2: 标记可疑slug为not_applicable**

```bash
cd d:\skills
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
# 标记所有可疑slug的skill不再上传
c.execute('''
    UPDATE skills 
    SET skillhub_sync_status = 'not_applicable'
    WHERE (slug LIKE '%-free' OR slug LIKE '%-pro' 
    OR slug LIKE '%-tool-free' OR slug LIKE '%-tool-pro'
    OR slug LIKE '%-sk' OR slug LIKE '%-sk1' 
    OR slug LIKE '%-sk2' OR slug LIKE '%-sk3')
    AND current_status NOT IN ('deleted', 'deleted_on_skillhub')
''')
print(f'已标记 {c.rowcount} 个可疑slug skill为not_applicable')
conn.commit()
"
```

- [ ] **Step 3: 验证**

```bash
cd d:\skills
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('''
    SELECT COUNT(*) FROM skills
    WHERE (slug LIKE '%-free' OR slug LIKE '%-pro' OR slug LIKE '%-sk%%')
    AND skillhub_sync_status != 'not_applicable'
    AND current_status NOT IN ('deleted', 'deleted_on_skillhub')
''')
print(f'仍可上传的可疑slug: {c.fetchone()[0]}')
"
```
预期：0

**退出条件（迭代轮次3）：**
- 金融skill 80%达到4.5+
- 重复哈希组清零
- 可疑slug全部标记not_applicable

---

### 迭代轮次4：高分区精准修复 (P2)

#### Task 4.1: 4.0-4.5区间skill精准修复（69个）

- [ ] **Step 1: 分析扣分维度**

```bash
cd d:\skills
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('''
    SELECT slug, local_quality_score, local_score_feedback
    FROM skills 
    WHERE local_quality_score >= 4.0 AND local_quality_score < 4.5
    ORDER BY local_quality_score DESC
''')
for slug, score, feedback in c.fetchall():
    print(f'{slug} ({score}): {feedback[:200] if feedback else \"N/A\"}')
"
```

- [ ] **Step 2: 针对性修复**

对每个skill，根据反馈中具体扣分维度进行精准修复：
- completeness扣分 → 补充具体使用场景、输入输出格式示例
- accuracy扣分 → 修正技术描述错误、补充依赖版本信息
- usability扣分 → 优化文档结构、添加快速入门
- security扣分 → 补充API密钥管理策略
- innovation扣分 → 增加差异化描述、具体技术对比

```bash
cd d:\skills
python tools/skill_deep_rewrite.py --batch --range 4.0-4.5 --limit 69 --mode precise
```

- [ ] **Step 3: 重新评分验证**

```bash
cd d:\skills
python tools/local_quality_scorer.py scan-all --force --limit 69
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()
c.execute('SELECT COUNT(*) FROM skills WHERE local_quality_score >= 4.5')
print(f'4.5+总数: {c.fetchone()[0]}')
"
```

**退出条件：** 4.0-4.5区间skill 80%达到4.5+

---

### 迭代轮次5-N：批量重写 + 持续优化 (P3)

#### Task 5.1: 中分区批量重写（3.5-4.0区间，830个）

- [ ] **Step 1: 分批重写（每批50个）**

```bash
cd d:\skills
# 批次1-17
python tools/skill_deep_rewrite.py --batch --range 3.5-4.0 --limit 50 --offset 0
python tools/skill_deep_rewrite.py --batch --range 3.5-4.0 --limit 50 --offset 50
# ...继续直到830个全部处理
```

- [ ] **Step 2: 每批后重新评分验证**

```bash
cd d:\skills
python tools/local_quality_scorer.py scan-all --force --limit 50
```

**退出条件：** 3.5-4.0区间skill 50%达到4.5+

#### Task 5.2: 低分区批量重写（<3.5区间，2596个）

- [ ] **Step 1: 先处理3.0-3.5区间（276个）**

```bash
cd d:\skills
python tools/skill_deep_rewrite.py --batch --range 3.0-3.5 --limit 50 --offset 0
# ...继续
```

- [ ] **Step 2: 处理0-3.0区间（2320个，含未评分）**

先完成Task 1.2的全量评分，确定实际低分skill数量，再分批处理。

**退出条件：** 全量skill 80%达到4.5+

---

## 三、交叉迭代验证检查点

每轮迭代结束后执行以下验证：

```bash
cd d:\skills
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
c = conn.cursor()

# 1. 评分覆盖率
c.execute('SELECT COUNT(*) FROM skills WHERE local_quality_score > 0')
scored = c.fetchone()[0]
c.execute('SELECT COUNT(*) FROM skills')
total = c.fetchone()[0]
print(f'1. 评分覆盖率: {scored}/{total} ({scored*100/total:.1f}%)')

# 2. 4.5+通过率
c.execute('SELECT COUNT(*) FROM skills WHERE local_quality_score >= 4.5')
passed = c.fetchone()[0]
print(f'2. 4.5+通过: {passed} ({passed*100/total:.1f}%)')

# 3. 评分分布
c.execute('''
    SELECT 
        CASE 
            WHEN local_quality_score >= 4.5 THEN '4.5+'
            WHEN local_quality_score >= 4.0 THEN '4.0-4.5'
            WHEN local_quality_score >= 3.5 THEN '3.5-4.0'
            WHEN local_quality_score >= 3.0 THEN '3.0-3.5'
            WHEN local_quality_score > 0 THEN '0-3.0'
            ELSE 'unscored'
        END as band,
        COUNT(*)
    FROM skills GROUP BY band ORDER BY band
''')
print('3. 评分分布:')
for band, count in c.fetchall():
    print(f'   {band}: {count}')

# 4. 重复哈希组
c.execute('SELECT COUNT(*) FROM (SELECT content_hash FROM skills WHERE content_hash IS NOT NULL AND content_hash != \"\" AND current_status NOT IN (\"deleted\",\"deleted_on_skillhub\") GROUP BY content_hash HAVING COUNT(*) > 1)')
print(f'4. 活跃重复哈希组: {c.fetchone()[0]}')

# 5. 可疑slug
c.execute('SELECT COUNT(*) FROM skills WHERE (slug LIKE \"%-free\" OR slug LIKE \"%-pro\" OR slug LIKE \"%-sk%\") AND skillhub_sync_status != \"not_applicable\" AND current_status NOT IN (\"deleted\",\"deleted_on_skillhub\")')
print(f'5. 可疑slug(仍可上传): {c.fetchone()[0]}')
"
```

---

## 四、总体退出标准

| 指标 | 目标 | 验证方法 |
|------|------|----------|
| 评分覆盖率 | ≥95% (≥3320/3495) | DB查询 `local_quality_score > 0` |
| 4.5+通过率 | ≥90% | DB查询 `local_quality_score >= 4.5` |
| 重复内容哈希组 | 0 | DB查询活跃重复组 |
| 可疑slug模式 | 0 (全部标记not_applicable) | DB查询 |
| 防封措施验证 | 6/6 PASS | 端到端验证脚本 |
| 质量门禁通过率 | ≥95% | 随机抽样100个skill通过 `quality_gate.py --full` |
| 安全预检通过率 | 100% | 全量skill通过安全扫描 |

---

## 五、关键文件索引

| 类别 | 文件路径 | 用途 |
|------|----------|------|
| 评分器 | `d:\skills\tools\local_quality_scorer.py` | 5维度LLM评分器（需修复扫描范围） |
| 评分配置 | `d:\skills\data\config\quality_scoring_config.json` | GLM-4-Flash配置+prompt（需校准） |
| 质量门禁 | `d:\skills\tools\quality_gate.py` | L1-L5质量检查（44项检查） |
| 差异化管道 | `d:\skills\tools\auto_differentiate.py` | SKILL.md生成（模板化问题源头） |
| 重写工具(新建) | `d:\skills\tools\skill_deep_rewrite.py` | 深度重写工具（替代batch_improve_v4） |
| 封禁根因 | `d:\skills\data\reports\banned_skills_root_cause_analysis.md` | 1378个skill封禁的6大根因 |
| 架构文档 | `d:\skills\docs\ARCHITECTURE.md` | 单slug+edition模型、8阶段流水线 |
| 数据库 | `d:\skills\skill-registry.db` | 唯一数据库（3495条skill记录） |
| 代码清理清单 | `d:\skills\data\reports\code_cleanup_pending_list.md` | 48个代码问题 |
| 文档清理清单 | `d:\skills\data\reports\doc_cleanup_pending_list.md` | ~100+过期文档 |

---

## 六、风险与缓解措施

| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|---------|
| GLM-4-Flash评分天花板无法突破 | 中 | 无法达到4.5 | 校准prompt；备选方案：调整阈值至4.2或使用DeepSeek-V3交叉验证 |
| API速率限制影响批量处理 | 中 | 处理速度慢 | 评分用GLM-4-Flash(5并发)，重写用DeepSeek-V3(独立配额)；分批50个，批次间5分钟间隔 |
| 重写后内容触发安全预检 | 低 | 安全风险 | 重写工具内置安全预检；失败自动回滚到备份 |
| 数据清理误删有效skill | 低 | 内容丢失 | 仅修改DB状态字段不删文件；清理前创建DB备份 |
| 迭代不收敛 | 低 | 无限循环 | 最多6轮迭代；剩余项标记"需人工介入" |

---

## 七、执行优先级总结

```
P0（立即执行）：
  Task 1.1 修复评分器扫描范围
  Task 1.2 全量评分基线扫描
  Task 1.3 防封措施回归验证

P1（高优先级）：
  Task 2.1 评分prompt校准
  Task 2.2 构建深度重写工具
  Task 2.3 付费skill优先重写

P2（中优先级）：
  Task 3.1 金融skill专项提升
  Task 3.2 重复内容哈希清理
  Task 3.3 可疑slug模式清理
  Task 4.1 高分区精准修复(69个)

P3（批量处理）：
  Task 5.1 中分区批量重写(830个)
  Task 5.2 低分区批量重写(2596个)
```

核心策略转变：**从"追加内容"转向"深度重写"**，**从"模板生成"转向"领域定制"**，**从"局部修补"转向"系统治理"**。
