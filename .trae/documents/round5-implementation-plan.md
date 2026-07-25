# 第5轮实施计划 (A1-A3 生成质量与运维闭环)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 修复3处架构与运维闭环问题——生成模块标记名不副实、运维闭环实为报告生成器、trace_llm_scorer独立于skill_core

**Architecture:** A1修正generate_skill.py的llm_generated标记为all_placeholders_filled；A2在ops闭环.py中增加fix_actions修复建议闭环；A3将trace_llm_scorer.py的重复检查迁移至skill_core共享层，并在rules.py中新增RESERVED_WORDS统一保留词来源

**Tech Stack:** Python 3, SQLite, skill_core共享模块(parser/rules/checks)

---

## 概述

| 任务 | 文件 | 修改类型 | 预计改动 |
|------|------|---------|---------|
| A1 | `d:\skills\tools\generate_skill.py` | 标记名修正 | ~3行 |
| A2 | `d:\skills\tools\ops闭环.py` | 增加修复建议闭环 | ~40行 |
| A3 | `d:\skills\tools\skill_core\rules.py` | 新增RESERVED_WORDS常量 | ~3行 |
| A3 | `d:\skills\tools\trace_llm_scorer.py` | 导入skill_core+替换硬编码 | ~20行 |
| A3 | `d:\skills\tools\skill_batch_upgrader_v3.py` | 导入skill_core+删除本地定义 | ~3行 |

**约束:**
- 禁止 mock/TODO/pass/fallback
- 每步修改后立即 `python -m py_compile` 语法检查
- A1: 不删除 `llm_generated` 字段(保持向后兼容),只改变其语义(不再设为True)
- A2: 不自动执行修复脚本,只输出建议命令
- A3: 保留TRACE特有检查项(`has_core_capability`/`has_use_cases`等),仅迁移重复的通用检查
- A3: `parse_frontmatter` 返回 dict `{'raw': str, 'fields': dict, 'body': str}`,不是 tuple,需用 `parsed['raw']` 和 `parsed['body']`

---

## 前置检查: 基线确认

### Task P: 建立验证基线

**Files:**
- Read: `d:\skills\tools\quality_gate.py`
- Read: `d:\skills\tools\batch_l2_eval.py`

- [ ] **Step 1: 确认3个验证skill的基线质量门结果**

所有命令在 `d:\skills\tools` 目录下执行:

```powershell
cd d:\skills\tools

# Skill 1: ad-creative-intel-free
python quality_gate.py "d:\skills\hermes-skills\Creative\free\ad-creative-intel-free" --json

# Skill 2: agentvibes-skill-free
python quality_gate.py "d:\skills\hermes-skills\Creative\free\agentvibes-skill-free" --json

# Skill 3: agent-assistant-free
python quality_gate.py "d:\skills\hermes-skills\Agents\free\agent-assistant-free" --json
```

记录每个skill的 `passed` 状态和 `issues` 列表,作为回归对比基线。

- [ ] **Step 2: 确认 batch_l2_eval.py 基线**

```powershell
cd d:\skills\tools
python batch_l2_eval.py --limit 1 --dry-run
```

预期: 无报错,正常输出候选skill列表。

---

## A1: generate_skill.py — llm_generated 标记名不副实

**问题:** `generate_from_template` 是纯模板规则填充,未调用任何LLM API,但第1103行将 `llm_generated` 设为True,名不副实。

**Files:**
- Modify: `d:\skills\tools\generate_skill.py:1051-1053, 1102-1103`

### Task A1: 修正 llm_generated 标记

- [ ] **Step 1: 在 result 初始化中增加 all_placeholders_filled 字段**

位置: 第1051-1053行

当前代码:
```python
        'llm_generated': False,  # Round 13: 标记是否使用LLM生成
        'template_filled': False,  # Round 13: 标记是否使用模板默认值填充
    }
```

修改后:
```python
        'llm_generated': False,  # Round 13: 标记是否使用LLM生成 (A1修复: 保留字段但不再设为True,因无LLM调用)
        'template_filled': False,  # Round 13: 标记是否使用模板默认值填充
        'all_placeholders_filled': False,  # A1修复: 诚实标记所有placeholder已通过模板规则填充完成
    }
```

- [ ] **Step 2: 将 llm_generated=True 改为 all_placeholders_filled=True**

位置: 第1102-1103行

当前代码:
```python
        else:
            result['llm_generated'] = True
```

修改后:
```python
        else:
            # A1修复: generate_from_template是纯模板规则填充,未调用LLM API
            # 原llm_generated=True名不副实,改为all_placeholders_filled=True诚实标记
            result['all_placeholders_filled'] = True
```

- [ ] **Step 3: 语法检查 + grep 确认**

```powershell
cd d:\skills\tools
python -m py_compile generate_skill.py

# 确认 llm_generated 不再被设为True (应仅在初始化处为False)
Select-String -Path generate_skill.py -Pattern "llm_generated" | ForEach-Object { "$($_.LineNumber): $($_.Line.Trim())" }

# 确认 all_placeholders_filled 有初始化(False)和设为True两处
Select-String -Path generate_skill.py -Pattern "all_placeholders_filled" | ForEach-Object { "$($_.LineNumber): $($_.Line.Trim())" }
```

预期:
- `llm_generated`: 仅1处匹配(初始化,值为False)
- `all_placeholders_filled`: 2处匹配(初始化False + 设为True)

---

## A2: ops闭环.py — 检测不修复的开环问题

**问题:** `generate_ops_report()` 检测到issues后只写入report字典,不触发任何修复动作,运维环不闭合(检测→报告→无动作)。

**Files:**
- Modify: `d:\skills\tools\ops闭环.py:253-255, 295-298, 311-313`

### Task A2: 增加修复建议闭环

- [ ] **Step 1: 在 generate_ops_report() 中生成 fix_actions 列表**

位置: 第253行(report字典定义结束的 `}` 之后)与第255行(`return report`)之间

当前代码:
```python
    }
    
    return report
```

修改后:
```python
    }
    
    # A2修复: 检测到问题后生成修复建议,闭合运维环(检测→报告→建议→人工执行→复验)
    fix_actions = []
    for issue in issues:
        if 'L1覆盖率不足' in issue:
            fix_actions.append({
                'action': 'run_l1_quality_gate',
                'script': 'python quality_gate.py --batch',
                'reason': issue
            })
        elif 'L2 A级比例不足' in issue:
            fix_actions.append({
                'action': 'run_l2_evaluation',
                'script': 'python batch_l2_eval.py --only-unevaluated',
                'reason': issue
            })
        elif '低分skill' in issue:
            fix_actions.append({
                'action': 'annotate_low_scores',
                'script': 'python trace_llm_scorer.py annotate',
                'reason': issue
            })
        elif 'L3覆盖率不足' in issue:
            fix_actions.append({
                'action': 'run_l3_trial',
                'script': 'python agent_trial.py batch --limit 5',
                'reason': issue
            })
        elif '健康检查' in issue:
            fix_actions.append({
                'action': 'run_health_check_detail',
                'script': 'python health_check.py --json',
                'reason': issue
            })
    
    report['fix_actions'] = fix_actions
    report['has_fix_actions'] = len(fix_actions) > 0
    
    return report
```

说明: issue字符串与匹配模式的对应关系(已验证):
- `'健康检查: 有严重问题'` / `'健康检查: 有警告'` → 匹配 `'健康检查' in issue`
- `f'L1覆盖率不足: {l1_coverage}%'` → 匹配 `'L1覆盖率不足' in issue`
- `f'L2 A级比例不足: {a_ratio:.1f}%'` → 匹配 `'L2 A级比例不足' in issue`
- `f'L3覆盖率不足: {l3_pct}%'` → 匹配 `'L3覆盖率不足' in issue`
- `f'低分skill数量: {low_count}'` → 匹配 `'低分skill' in issue`

- [ ] **Step 2: 语法检查**

```powershell
cd d:\skills\tools
python -m py_compile ops闭环.py
```

- [ ] **Step 3: 在 print_terminal_report() 中输出修复建议**

位置: 第296行(`print(f"\n{'='*70}")` 之前)

当前代码:
```python
            print(f"  {s['slug']}: {s['score']}/100")
    
    print(f"\n{'='*70}")
```

修改后:
```python
            print(f"  {s['slug']}: {s['score']}/100")
    
    # A2修复: 输出修复建议
    fix_actions = report.get('fix_actions', [])
    if fix_actions:
        print(f"\n--- 修复建议 ({len(fix_actions)}个) ---")
        for i, fa in enumerate(fix_actions, 1):
            print(f"  [{i}] {fa['action']}")
            print(f"      原因: {fa['reason']}")
            print(f"      命令: {fa['script']}")
    
    print(f"\n{'='*70}")
```

- [ ] **Step 4: 语法检查**

```powershell
cd d:\skills\tools
python -m py_compile ops闭环.py
```

- [ ] **Step 5: 在 main() 中输出执行提示**

位置: 第312行(`print_terminal_report(report)`)之后,仍在 `else:` 块内

当前代码:
```python
    else:
        print_terminal_report(report)
    
    if args.output:
```

修改后:
```python
    else:
        print_terminal_report(report)
        # A2修复: 如果有修复建议,输出执行提示(不自动执行,由用户/AI决定)
        if report.get('has_fix_actions'):
            print(f"\n⚠ 检测到{len(report['fix_actions'])}个问题,建议执行上述修复脚本")
            print(f"  复制命令执行后,重新运行 python ops闭环.py 验证修复效果")
    
    if args.output:
```

- [ ] **Step 6: 语法检查**

```powershell
cd d:\skills\tools
python -m py_compile ops闭环.py
```

- [ ] **Step 7: 功能验证 fix_actions 字段**

注意: `generate_ops_report()` 内有 `print()` 语句输出到stdout,与 `--json` 的JSON输出混合,直接管道解析会失败。使用 `-o` 保存到文件再解析。

```powershell
cd d:\skills\tools

# 保存到文件后解析(推荐,可靠)
python ops闭环.py -o ops_report_temp.json | Out-Null
python -c "import json; r=json.load(open('ops_report_temp.json',encoding='utf-8')); print('fix_actions count:', len(r.get('fix_actions',[]))); print('has_fix_actions:', r.get('has_fix_actions')); [print(f'  [{i+1}] {fa[\"action\"]}: {fa[\"script\"]}') for i,fa in enumerate(r.get('fix_actions',[]))]"
del ops_report_temp.json
```

预期: `fix_actions` 列表非空(取决于当前DB状态),`has_fix_actions` 为 True(如果有issues)。每个 fix_action 包含 `action`/`script`/`reason` 三个字段。

---

## A3: trace_llm_scorer.py — 迁移至 skill_core 共享实现

**问题:** trace_llm_scorer.py 独立于 skill_core 实现了第三套检查:
1. 自行解析frontmatter(与 `skill_core/parser.py` 的 `parse_frontmatter` 重复)
2. 硬编码保留词4个(与 `skill_batch_upgrader_v3.py:61` 的 `RESERVED_WORDS` 重复)
3. 硬编码夸大词10个(与 `skill_core/rules.py` 的 `EXAGGERATION_WORDS` 16个不一致)

**关键依赖:** A3.1(新增RESERVED_WORDS)必须在A3.2-A3.6之前完成,因为后续步骤依赖该常量存在。

**Files:**
- Modify: `d:\skills\tools\skill_core\rules.py:59-61` (新增RESERVED_WORDS)
- Modify: `d:\skills\tools\trace_llm_scorer.py:40, 186-193, 230, 240, 245-249` (导入+替换)
- Modify: `d:\skills\tools\skill_batch_upgrader_v3.py:42, 60-62` (导入+删除本地定义)

### Task A3.1: 在 skill_core/rules.py 中新增 RESERVED_WORDS 常量

- [ ] **Step 1: 新增 RESERVED_WORDS**

文件: `d:\skills\tools\skill_core\rules.py`
位置: 第59行(`EXAGGERATION_WORDS` 定义结束的 `]`)之后,第61行(`# ============ 格式正则 ============`)之前

当前代码:
```python
EXAGGERATION_WORDS = [
    '万能', '超级', '最强', '最佳', '最完美', '最专业',
    '全球首发', '业界第一', '独一无二', '绝无仅有',
    # Q4修复: 合并generate_skill.py:622的夸大词,消除列表不一致
    '终极', '完美', '第一', '顶级', '极致', '最好',
]

# ============ 格式正则 ============
```

修改后:
```python
EXAGGERATION_WORDS = [
    '万能', '超级', '最强', '最佳', '最完美', '最专业',
    '全球首发', '业界第一', '独一无二', '绝无仅有',
    # Q4修复: 合并generate_skill.py:622的夸大词,消除列表不一致
    '终极', '完美', '第一', '顶级', '极致', '最好',
]

# ============ 保留词模式 ============
# A3修复: 统一保留词列表,消除trace_llm_scorer.py和skill_batch_upgrader_v3.py的重复硬编码
RESERVED_WORDS = ['claude', 'anthropic', 'openai', 'chatgpt']

# ============ 格式正则 ============
```

- [ ] **Step 2: 语法检查 + 导入验证**

```powershell
cd d:\skills\tools
python -m py_compile skill_core\rules.py
python -c "import sys; sys.path.insert(0,'.'); sys.path.insert(0,'../config'); from skill_core.rules import RESERVED_WORDS; print('RESERVED_WORDS:', RESERVED_WORDS)"
```

预期输出: `RESERVED_WORDS: ['claude', 'anthropic', 'openai', 'chatgpt']`

### Task A3.2: 在 trace_llm_scorer.py 中添加 skill_core 导入

- [ ] **Step 1: 添加导入语句**

文件: `d:\skills\tools\trace_llm_scorer.py`
位置: 第40行(`from config import (...)` 的结束 `)`)之后

当前代码:
```python
from config import (
    DB_PATH, EXPORT_DIR, TRACE_PASS_THRESHOLD, TRACE_FIELD_MAPPING,
    PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, SCORE_TYPE_TRACE_LLM,
    L2_PASS_THRESHOLD, L2_EXCELLENT_THRESHOLD, L2_MANUAL_REVIEW_THRESHOLD,
    create_backup
)

def get_db():
```

修改后:
```python
from config import (
    DB_PATH, EXPORT_DIR, TRACE_PASS_THRESHOLD, TRACE_FIELD_MAPPING,
    PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, SCORE_TYPE_TRACE_LLM,
    L2_PASS_THRESHOLD, L2_EXCELLENT_THRESHOLD, L2_MANUAL_REVIEW_THRESHOLD,
    create_backup
)

# A3修复: 从skill_core导入共享解析和规则,消除第三套检查实现
from skill_core.parser import parse_frontmatter
from skill_core.rules import EXAGGERATION_WORDS, RESERVED_WORDS

def get_db():
```

说明: trace_llm_scorer.py 第31-34行已将自身目录插入 `sys.path`,且 `skill_core` 是有 `__init__.py` 的正式包,导入路径可靠。`import re` 必须保留(文件中有20处 `re.` 调用)。

- [ ] **Step 2: 语法检查**

```powershell
cd d:\skills\tools
python -m py_compile trace_llm_scorer.py
```

### Task A3.3: 替换 trace_llm_scorer.py 的 frontmatter 自行解析

- [ ] **Step 1: 替换 frontmatter 解析逻辑**

文件: `d:\skills\tools\trace_llm_scorer.py`
位置: 第186-193行(frontmatter解析)和第245-249行(两个else分支)

当前代码 (第186-193行):
```python
    # 解析frontmatter
    if skill_content.startswith('---'):
        parts = re.split(r'^---\s*$', skill_content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2]
            checks['has_frontmatter'] = True
            checks['frontmatter_valid'] = True
```

修改后:
```python
    # A3修复: 使用skill_core.parse_frontmatter替代自行解析
    parsed = parse_frontmatter(skill_content)
    if parsed['raw']:
        fm = parsed['raw']
        body = parsed['body']
        checks['has_frontmatter'] = True
        checks['frontmatter_valid'] = True
```

当前代码 (第245-249行,两个else分支):
```python
        else:
            checks['issues'].append('frontmatter格式错误')
    else:
        body = skill_content
        checks['issues'].append('缺少frontmatter')
```

修改后:
```python
    else:
        body = parsed['body']
        if skill_content.startswith('---'):
            checks['issues'].append('frontmatter格式错误')
        else:
            checks['issues'].append('缺少frontmatter')
```

关键细节:
- `parse_frontmatter` 返回 dict `{'raw': str, 'fields': dict, 'body': str}`,不是 tuple
- `parsed['raw']` 对应原 `parts[1]`(frontmatter文本),`parsed['body']` 对应原 `parts[2]`(正文)
- `parse_frontmatter` 无匹配时返回 `{'raw': '', 'body': content}`,需用 `skill_content.startswith('---')` 区分"缺少frontmatter"和"格式错误"两种情况,保持原行为
- `parse_frontmatter` 自动处理BOM(`\ufeff`),比原实现更健壮
- `fm` 变量类型不变(均为str),后续 `re.search(r'^displayName:', fm, ...)` 等检查无需修改
- `body` 变量在两个分支中均有定义,后续第252行 `any(kw in body for kw in ...)` 不会报 NameError

- [ ] **Step 2: 语法检查**

```powershell
cd d:\skills\tools
python -m py_compile trace_llm_scorer.py
```

### Task A3.4: 替换 trace_llm_scorer.py 的硬编码保留词

- [ ] **Step 1: 替换保留词列表**

文件: `d:\skills\tools\trace_llm_scorer.py`
位置: 第230行(保留词检查的 for 循环)

当前代码:
```python
                    for word in ['claude', 'anthropic', 'openai', 'chatgpt']:
```

修改后:
```python
                    # A3修复: 使用skill_core.rules.RESERVED_WORDS替代硬编码
                    for word in RESERVED_WORDS:
```

- [ ] **Step 2: 语法检查**

```powershell
cd d:\skills\tools
python -m py_compile trace_llm_scorer.py
```

### Task A3.5: 替换 trace_llm_scorer.py 的硬编码夸大词

- [ ] **Step 1: 替换夸大词列表**

文件: `d:\skills\tools\trace_llm_scorer.py`
位置: 第240行(夸大词检查的 for 循环)

当前代码:
```python
                    for word in ['万能', '超级', '最强', '最好', '最佳', '终极', '完美', '第一', '顶级', '极致']:
```

修改后:
```python
                    # A3修复: 使用skill_core.rules.EXAGGERATION_WORDS替代硬编码(消除16词vs10词不一致)
                    for word in EXAGGERATION_WORDS:
```

说明: `EXAGGERATION_WORDS` 含16个词,比原硬编码10个词多6个(`最完美`/`最专业`/`全球首发`/`业界第一`/`独一无二`/`绝无仅有`)。这是预期行为——统一到SSOT的更严格标准。

- [ ] **Step 2: 语法检查**

```powershell
cd d:\skills\tools
python -m py_compile trace_llm_scorer.py
```

### Task A3.6: 修改 skill_batch_upgrader_v3.py 导入 RESERVED_WORDS

- [ ] **Step 1: 添加导入 + 删除本地定义**

文件: `d:\skills\tools\skill_batch_upgrader_v3.py`

位置1: 在 `from config import (...)` 结束之后(约第42行),`EXAGGERATION_MAP` 定义之前 — 添加导入

位置2: 第61行 — 删除本地硬编码定义

需先读取文件确认精确行号,再执行修改。

添加导入(在config导入结束后):
```python
# A3修复: 从skill_core导入RESERVED_WORDS,消除本地重复硬编码
from skill_core.rules import RESERVED_WORDS
```

删除本地定义(原第60-62行):
```python
# 当前(待删除):
# v3.0新增: 保留词检查
RESERVED_WORDS = ['claude', 'anthropic', 'openai', 'chatgpt']

# 修改后:
# v3.0新增: 保留词检查 (A3修复: 已迁移至skill_core.rules,此处不再重复定义)
```

说明: 第165行 `for word in RESERVED_WORDS:` 无需修改,变量名一致。该文件约第36行 `sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))` 已确保 skill_core 可导入。

- [ ] **Step 2: 语法检查 + grep 确认**

```powershell
cd d:\skills\tools
python -m py_compile skill_batch_upgrader_v3.py

# 确认 RESERVED_WORDS 在文件中只被导入,不再被本地定义
Select-String -Path skill_batch_upgrader_v3.py -Pattern "RESERVED_WORDS" | ForEach-Object { "$($_.LineNumber): $($_.Line.Trim())" }
```

预期输出: 2行
- 导入行: `from skill_core.rules import RESERVED_WORDS`
- 使用行: `for word in RESERVED_WORDS:`

---

## 综合验证

### Task V: 全量验证

- [ ] **Step 1: 全部修改文件语法检查**

```powershell
cd d:\skills\tools
python -m py_compile generate_skill.py
python -m py_compile ops闭环.py
python -m py_compile trace_llm_scorer.py
python -m py_compile skill_core\rules.py
python -m py_compile skill_batch_upgrader_v3.py
```

预期: 全部无输出(无语法错误)。

- [ ] **Step 2: trace_llm_scorer.py static_check 功能测试**

```powershell
cd d:\skills\tools
python -c "import sys; sys.path.insert(0,'.'); sys.path.insert(0,'../config'); from trace_llm_scorer import static_check; r=static_check('---\ndisplayName: test\nsummary: 最强工具\n---\n# test\n核心能力'); print('has_frontmatter:', r['has_frontmatter']); print('has_exaggeration:', r['has_exaggeration']); print('has_reserved_words:', r['has_reserved_words']); print('issues:', r['issues'])"
```

预期:
- `has_frontmatter: True` (parse_frontmatter 成功解析)
- `has_exaggeration: True` ("最强"在 EXAGGERATION_WORDS 16词列表中)
- `has_reserved_words: False` ("test" 不含保留词)
- `issues` 包含 `'summary含夸大词最强'`

- [ ] **Step 3: RESERVED_WORDS 导入验证**

```powershell
cd d:\skills\tools
python -c "import sys; sys.path.insert(0,'.'); sys.path.insert(0,'../config'); from skill_core.rules import RESERVED_WORDS, EXAGGERATION_WORDS; print('RESERVED_WORDS:', RESERVED_WORDS); print('EXAGGERATION_WORDS count:', len(EXAGGERATION_WORDS))"
```

预期:
- `RESERVED_WORDS: ['claude', 'anthropic', 'openai', 'chatgpt']`
- `EXAGGERATION_WORDS count: 16`

- [ ] **Step 4: 3个验证skill质量门回归测试**

```powershell
cd d:\skills\tools

# Skill 1: ad-creative-intel-free
python quality_gate.py "d:\skills\hermes-skills\Creative\free\ad-creative-intel-free" --json

# Skill 2: agentvibes-skill-free
python quality_gate.py "d:\skills\hermes-skills\Creative\free\agentvibes-skill-free" --json

# Skill 3: agent-assistant-free
python quality_gate.py "d:\skills\hermes-skills\Agents\free\agent-assistant-free" --json
```

预期: 每个skill的 `passed` 状态和 `issues` 列表与步骤 P.1 基线一致,无回归。

- [ ] **Step 5: batch_l2_eval.py 无报错验证**

```powershell
cd d:\skills\tools
python batch_l2_eval.py --limit 1 --dry-run
```

预期: 无报错,正常输出候选skill列表(与步骤 P.2 基线一致)。

- [ ] **Step 6: ops闭环.py fix_actions 验证**

```powershell
cd d:\skills\tools
python ops闭环.py -o ops_report_temp.json | Out-Null
python -c "import json; r=json.load(open('ops_report_temp.json',encoding='utf-8')); print('fix_actions count:', len(r.get('fix_actions',[]))); print('has_fix_actions:', r.get('has_fix_actions')); [print(f'  [{i+1}] {fa[\"action\"]}: {fa[\"script\"]}') for i,fa in enumerate(r.get('fix_actions',[]))]"
del ops_report_temp.json
```

预期: `fix_actions` 列表非空(如果DB中存在issues),`has_fix_actions` 为 True。

- [ ] **Step 7: grep 确认无残留硬编码**

```powershell
cd d:\skills\tools

# trace_llm_scorer.py 不应再有硬编码保留词列表
Select-String -Path trace_llm_scorer.py -Pattern "claude.*anthropic.*openai" | ForEach-Object { "$($_.LineNumber): $($_.Line.Trim())" }
# 预期: 无匹配

# trace_llm_scorer.py 不应再有硬编码夸大词列表
Select-String -Path trace_llm_scorer.py -Pattern "'万能'.*'极致'" | ForEach-Object { "$($_.LineNumber): $($_.Line.Trim())" }
# 预期: 无匹配

# skill_batch_upgrader_v3.py 不应再有本地 RESERVED_WORDS 定义
Select-String -Path skill_batch_upgrader_v3.py -Pattern "^RESERVED_WORDS\s*=" | ForEach-Object { "$($_.LineNumber): $($_.Line.Trim())" }
# 预期: 无匹配(只有import行和使用行)

# generate_skill.py 不应再有 llm_generated = True
Select-String -Path generate_skill.py -Pattern "llm_generated.*True" | ForEach-Object { "$($_.LineNumber): $($_.Line.Trim())" }
# 预期: 无匹配
```

---

## 验收标准检查清单

| # | 验收项 | 验证方法 |
|---|--------|---------|
| 1 | generate_skill.py 的 `llm_generated` 不再被设为True | V.7 grep |
| 2 | 新增 `all_placeholders_filled` 标记诚实反映模板填充状态 | A1 Step 3 grep |
| 3 | ops闭环.py 检测到问题后输出 fix_actions 修复建议列表 | V.6 |
| 4 | ops闭环.py 终端输出包含"修复建议"区块 | A2 Step 7 |
| 5 | ops闭环.py JSON输出包含 fix_actions 和 has_fix_actions 字段 | V.6 |
| 6 | trace_llm_scorer.py 使用 skill_core.parse_frontmatter 替代自行解析 | V.2 |
| 7 | trace_llm_scorer.py 夸大词检查使用 EXAGGERATION_WORDS(16词) | V.2 + V.3 |
| 8 | trace_llm_scorer.py 保留词检查使用 RESERVED_WORDS | V.7 |
| 9 | skill_core/rules.py 新增 RESERVED_WORDS 常量 | V.3 |
| 10 | skill_batch_upgrader_v3.py 从 skill_core.rules 导入 RESERVED_WORDS | V.7 |
| 11 | 3个skill质量门验证无回归 | V.4 |
| 12 | batch_l2_eval.py --limit 1 --dry-run 无报错 | V.5 |
| 13 | 不引入新bug,不改变现有行为(除修复的3处外) | V.4 + V.5 |

---

## 最终任务: 生成第6轮提示词

完成 A1-A3 全部修改和验证后,在 `d:\skills\.trae\documents\round6-prompt.md` 中生成第6轮提示词(L1-L8 冗余文件清理)。

第6轮将聚焦清理~34MB冗余文件:
- L1: 删除3个__pycache__目录(76个.pyc,~1.2MB)
- L2-L3: 删除3个0字节空文件(0)
- L4: 归档后删除3个DB备份(~30MB)
- L5: 删除旧版本报告(~3.4MB)
- L6: 删除版本化旧脚本(~200KB)
- L7-L8: 评估整理生成报告和prompt文件(~3MB)

---

## 执行顺序总结

1. **前置检查** (Task P): 建立基线
2. **A1** (Task A1): generate_skill.py 标记修正
3. **A2** (Task A2): ops闭环.py 运维闭环
4. **A3** (Task A3.1-A3.6): skill_core 迁移(先 rules.py,再 trace_llm_scorer.py,最后 skill_batch_upgrader_v3.py)
5. **综合验证** (Task V): 全量检查
6. **第6轮提示词**: 生成 round6-prompt.md

**关键依赖**: A3.1(新增RESERVED_WORDS)必须在A3.2-A3.6之前完成。
