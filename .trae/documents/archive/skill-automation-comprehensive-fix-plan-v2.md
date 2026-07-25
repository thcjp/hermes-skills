# 技能自动化系统全面修复计划 v2

> 基于实际代码阅读验证，非文档承诺。所有问题均通过阅读 `.py` 源码确认。
> 制定日期：2026-07-25
> 验证方法：4个 Explore 子代理并行审计（代码状态/DB追踪/冗余文件/质量门硬编码）

---

## 进度总览

| 轮次 | 目标 | 状态 |
|------|------|------|
| 第1轮 | C1-C4 关键崩溃修复 | ✅ 已完成并验证 |
| 第2轮 | H1-H2 质量门控修复 | ⬜ 待执行（本轮） |
| 第3轮 | H3-H4 DB连接统一 | ⬜ 待执行 |
| 第4轮 | H5-H8 DB数据完整性 | ⬜ 待执行 |
| 第5轮 | M1-M4 架构修复 | ⬜ 待执行 |
| 第6轮 | L1-L8 清理 | ⬜ 待执行 |

---

## 第1轮完成记录（C1-C4）

| 编号 | 文件 | 修复内容 | 验证结果 |
|------|------|---------|---------|
| C1 | `update_mechanism.py:62` | 注释改为赋值 `DIFFERENTIATED_SKILLS_DIR = DIFFERENTIATED_DIR` | 变量=`d:\skills\differentiated-skills`，4处引用正常解析 |
| C2 | `update_mechanism.py:56-57` | 导入`DATA_DIR`，`PAYLOADS_DIR`改为`DATA_DIR/"payloads"`并自动创建 | 路径=`d:\skills\data\payloads`，无旧会话ID，目录已创建 |
| C3 | `check_debranding.py:244` | `r'str(DIFFERENTIATED_DIR)'`→`str(DIFFERENTIATED_DIR)` | 无`r'str(`残留，target_dir解析为真实路径 |
| C4 | `check_debranding.py:12` | 增加`from project_config import DATA_DIR` | `DATA_DIR`=`d:\skills\data`，可访问 |

端到端验证：
- `check_debranding.py`扫描71文件0错误
- `update_mechanism.py status`列出2882个skill无NameError
- `update_mechanism.py check --slug ad-creative-intel-free`退出码0

---

## 第2轮：质量门控修复（H1-H2）

### 目标
修复版本号正则漏洞和链接占位符检查缺失，使质量门真正有效。

---

### H1: 修复 VERSION_PATTERN 缺少 `$` 锚点

**文件**: `d:\skills\tools\skill_core\rules.py` 第50行

**当前代码**（已通过 Read 验证）:
```python
# version必须为x.y.z格式
VERSION_PATTERN = r'^\d+\.\d+\.\d+'
```

**问题**: 有 `^` 但无 `$` 结尾锚定。`re.match` 从头匹配但不要求到尾，因此 `1.2.3-rc1`、`1.2.3.4`、`1.2.3abc` 都会通过检查。对比第47行 `SLUG_KEBAB_PATTERN = r'^[a-z0-9]+(-[a-z0-9]+)*$'` 是正确锚定的。

**修复**:
```python
VERSION_PATTERN = r'^\d+\.\d+\.\d+$'
```

**验证**:
```powershell
cd d:\skills
python -c "
import re
from skill_core.rules import VERSION_PATTERN
# 应通过
assert re.match(VERSION_PATTERN, '1.0.0'), '1.0.0应通过'
assert re.match(VERSION_PATTERN, '0.0.1'), '0.0.1应通过'
# 应拒绝
assert not re.match(VERSION_PATTERN, '1.2.3-rc1'), '1.2.3-rc1应拒绝'
assert not re.match(VERSION_PATTERN, '1.2'), '1.2应拒绝'
assert not re.match(VERSION_PATTERN, '1.2.3.4'), '1.2.3.4应拒绝'
assert not re.match(VERSION_PATTERN, 'v1.0.0'), 'v1.0.0应拒绝'
print('H1 验证通过: 6个测试用例全部正确')
"
```

---

### H2: 修复链接占位符检查被跳过

**文件1**: `d:\skills\tools\skill_core\checks.py` 第169-185行
**文件2**: `d:\skills\tools\quality_gate.py` 第125行

**当前代码**（已通过 Read 验证）:

`checks.py:169-185`:
```python
def check_no_placeholders(content: str) -> dict:
    """检查: 无占位符"""
    issues = []
    for pattern, desc in PLACEHOLDER_PATTERNS:
        # 跳过链接检查(链接在正文中合法)
        if '未替换链接' in desc:
            continue
        for m in re.finditer(pattern, content):
            issues.append(f"{desc}: '{m.group(0)}'")
    ...
```

`quality_gate.py:125`:
```python
check_no_placeholders(content),
```

**问题**: `rules.py:34` 定义了 `(r'\[.*?\]\s*\(.*?\)', '占位符-未替换链接')` 模式，注释说"仅在frontmatter中检查"，但 `checks.py:174` 用 `continue` 直接跳过，该检查从未在任何地方执行。frontmatter 中的未替换链接占位符（如 `[项目名](url)`）完全不被检测。

**修复策略**: 不能简单删除 `continue`（会导致正文中合法 Markdown 链接误报）。需要区分 frontmatter 和正文区域：
- 非链接占位符模式：检查全文（保持不变）
- 链接占位符模式：仅检查 frontmatter 原始文本

**修复步骤**:

**步骤1**: 修改 `checks.py` 的 `check_no_placeholders` 函数签名和实现:

将第169-185行从：
```python
def check_no_placeholders(content: str) -> dict:
    """检查: 无占位符"""
    issues = []
    for pattern, desc in PLACEHOLDER_PATTERNS:
        # 跳过链接检查(链接在正文中合法)
        if '未替换链接' in desc:
            continue
        for m in re.finditer(pattern, content):
            issues.append(f"{desc}: '{m.group(0)}'")
```

改为：
```python
def check_no_placeholders(content: str, fm_raw: str = '') -> dict:
    """检查: 无占位符

    链接占位符仅在frontmatter中检查(正文中的Markdown链接合法)
    其他占位符检查全文
    """
    issues = []
    for pattern, desc in PLACEHOLDER_PATTERNS:
        if '未替换链接' in desc:
            # 链接占位符仅在frontmatter中检查
            for m in re.finditer(pattern, fm_raw):
                issues.append(f"{desc}: '{m.group(0)}'")
            continue
        for m in re.finditer(pattern, content):
            issues.append(f"{desc}: '{m.group(0)}'")
```

**步骤2**: 修改 `quality_gate.py` 第125行的调用:

从：
```python
check_no_placeholders(content),
```

改为：
```python
check_no_placeholders(content, fm['raw']),
```

**验证**:
```powershell
cd d:\skills

# 1. 语法检查
python -m py_compile tools\skill_core\checks.py
python -m py_compile tools\quality_gate.py

# 2. 单元测试: frontmatter中的链接占位符被捕获
python -c "
import sys
sys.path.insert(0, 'tools')
from skill_core.checks import check_no_placeholders

# 模拟frontmatter中有未替换链接
content = '''---
slug: test-skill
name: test-skill
version: 1.0.0
displayName: 测试
summary: 测试技能
license: MIT
description: 这是一个[未替换链接](placeholder)的测试
tools:
  - read
---

# 正文
这里有合法的[Markdown链接](https://example.com)，不应报错。
'''
fm_raw = '''slug: test-skill
name: test-skill
version: 1.0.0
displayName: 测试
summary: 测试技能
license: MIT
description: 这是一个[未替换链接](placeholder)的测试
tools:
  - read'''

result = check_no_placeholders(content, fm_raw)
print('检查结果:', result)
assert not result['passed'], '应检测到frontmatter中的链接占位符'
assert any('未替换链接' in d for d in result['details']), '应报告链接占位符'
print('H2 单元测试通过: frontmatter链接占位符被捕获')
"

# 3. 单元测试: 正文中的合法链接不误报
python -c "
import sys
sys.path.insert(0, 'tools')
from skill_core.checks import check_no_placeholders

content = '''---
slug: test-skill
name: test-skill
version: 1.0.0
displayName: 测试
summary: 测试技能
license: MIT
description: 这是一个正常的描述没有链接
tools:
  - read
---

# 正文
这里有合法的[Markdown链接](https://example.com)，不应报错。
'''
fm_raw = '''slug: test-skill
name: test-skill
version: 1.0.0
displayName: 测试
summary: 测试技能
license: MIT
description: 这是一个正常的描述没有链接
tools:
  - read'''

result = check_no_placeholders(content, fm_raw)
print('检查结果:', result)
assert result['passed'], '正文中的合法链接不应误报'
print('H2 单元测试通过: 正文合法链接不误报')
"
```

---

### T2.3: 对3个真实skill运行完整质量门检查

选取3个不同类型的真实skill验证无回归：

```powershell
cd d:\skills

# 选取3个skill（从differentiated-skills不同分类中各选1个）
python tools\quality_gate.py "differentiated-skills\Agents\ad-creative-intel-free"
python tools\quality_gate.py "differentiated-skills\Creative\agentvibes-skill-free"
python tools\quality_gate.py "differentiated-skills\Other\agent-assistant-free"
```

**通过标准**:
- 3个skill的质量门检查均正常运行，无报错
- 检查结果与第1轮一致（无回归）
- 版本号检查仍能正确通过（这些skill的version应为x.y.z格式）

---

### 第2轮完成后的第3轮提示词

```
第2轮（H1-H2 质量门控修复）已完成并验证通过。请开始第3轮：DB连接统一（H3-H4）。

第3轮目标：
1. [H3] 将26个文件中直接调用 sqlite3.connect(DB_PATH) 替换为 from skill_core.db import get_db; conn = get_db()
   - 优先处理写入类脚本（init_baseline.py、scan_and_import.py、analyze_status.py 等）
   - 保留 db.py 内部的 connect（它是 get_db 的实现）和 skill_core/db.py 自身
   - 验证: grep确认 sqlite3.connect 调用数从51处降至约11处（仅db.py内部）

2. [H4] 将41个INSERT + 18个UPDATE中绕过db.py业务函数的裸SQL改为调用已有业务函数
   - 先审计 db.py 已有的业务函数（register_skill/record_score/set_pricing/record_upload等）
   - 将裸SQL改为调用对应业务函数
   - 补充 skill_core/db.py 中缺失的业务函数（如 upsert_score、update_skill_status）
   - 验证: grep确认裸INSERT/UPDATE数大幅下降

约束：
- 每次只改3-5个文件，改完立即验证
- 禁止 mock/TODO
- 保留 db.py 作为业务函数库，skill_core/db.py 作为连接工厂
完成第3轮后，输出第4轮提示词（DB数据完整性 H5-H8）。
```

---

## 问题清单（完整保留供参考）

### CRITICAL（运行时崩溃）- 已全部修复 ✅

| 编号 | 文件 | 问题 | 状态 |
|------|------|------|------|
| C1 | `tools/update_mechanism.py` | 使用未定义的 `DIFFERENTIATED_SKILLS_DIR` | ✅ 已修复 |
| C2 | `tools/update_mechanism.py` | `PAYLOADS_DIR` 硬编码旧会话临时路径 | ✅ 已修复 |
| C3 | `tools/check_debranding.py` | `r'str(DIFFERENTIATED_DIR)'` 字面量误用 | ✅ 已修复 |
| C4 | `tools/check_debranding.py` | `DATA_DIR` 未导入 | ✅ 已修复 |

### HIGH（质量门控 / DB追踪）

| 编号 | 文件 | 问题 | 状态 |
|------|------|------|------|
| H1 | `tools/skill_core/rules.py:50` | `VERSION_PATTERN` 缺少 `$` 锚点 | ⬜ 待修复（本轮） |
| H2 | `tools/skill_core/checks.py:174` | 链接占位符检查被跳过，从不执行 | ⬜ 待修复（本轮） |
| H3 | `tools/` (26个文件) | 绕过 `get_db()`，直接 `sqlite3.connect()`（51处） | ⬜ 待修复（第3轮） |
| H4 | `tools/` (15+个文件) | 41个INSERT + 18个UPDATE绕过业务函数写裸SQL | ⬜ 待修复（第3轮） |
| H5 | `agent_trial.py:389`, `batch_l2_eval.py:146` | DELETE销毁质量门历史 | ⬜ 待修复（第4轮） |
| H6 | `upload_tracking.json`相关 | 双轨数据无同步机制 | ⬜ 待修复（第4轮） |
| H7 | `multi_source_discover.py:283` | `discovered_at` 未持久化到DB | ⬜ 待修复（第4轮） |
| H8 | `upload_tracking.json`相关 | 升级历史仅存JSON，不在SQLite | ⬜ 待修复（第4轮） |

### MEDIUM（架构）

| 编号 | 文件 | 问题 | 状态 |
|------|------|------|------|
| M1 | `tools/parse_report.py` | 0字节空文件 | ⬜ 待修复（第5轮） |
| M2 | `tools/init_baseline.py` | 3处重复INSERT代码块 | ⬜ 待修复（第5轮） |
| M3 | `task3_pricing_calibration.py:431` | UPDATE丢弃字段 | ⬜ 待修复（第5轮） |
| M4 | `tools/db.py` | 无迁移系统 | ⬜ 待修复（第5轮） |

### LOW（清理）

| 编号 | 位置 | 问题 | 可释放 | 状态 |
|------|------|------|--------|------|
| L1 | 3个`__pycache__` | 76个`.pyc`文件 | ~1.2MB | ⬜ 第6轮 |
| L2 | `data\skill-registry.db` | 0字节空文件 | 0 | ⬜ 第6轮 |
| L3 | `data\market-data\` | 重复文件 | ~10KB | ⬜ 第6轮 |
| L4 | `skillhub_20260720.json` | 仅含`[]` | 2B | ⬜ 第6轮 |
| L5 | `data\backups\` | 3个旧DB备份 | ~30MB | ⬜ 第6轮 |
| L6 | `data\reports\` | 791个generation_report | ~34MB | ⬜ 第6轮 |
| L7 | `tools/` | 废弃版本化脚本 | ~72KB | ⬜ 第6轮 |
| L8 | `docs\plans\` | 旧版prompt文件 | 整理 | ⬜ 第6轮 |

---

## 关键设计决策

1. **H2 修复策略**: 不能简单删除 `continue`（会导致正文中合法Markdown链接误报），必须区分frontmatter和正文区域。通过给 `check_no_placeholders` 增加可选参数 `fm_raw`，仅在frontmatter原始文本中检查链接占位符。
2. **H1 修复策略**: 仅增加 `$` 锚点，最小改动。`re.match` 已有隐式 `^`，只需显式加 `$`。
3. **分轮依赖**: 第1轮是前提（已完成）；第2轮独立于DB修复；第3轮应在第4轮之前（统一连接后修改DELETE逻辑更安全）；第6轮放最后。
