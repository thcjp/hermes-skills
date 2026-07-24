# Skill 治理触发机制

> **触发词**: "治理"
> **创建时间**: 2026-07-20
> **位置**: `d:\skills\skill-registry\GOVERNANCE_TRIGGER.md`

---

## 触发规则

当用户输入 **"治理"** 时，立即启动本文件定义的全面治理流水线。
系统性清理数据库中的命名规范、字段一致性、工作流状态、孤儿记录等问题。

---

## 执行流程（7阶段）

### 阶段1: 诊断扫描 (Diagnostic Scan)

**目标**: 全面扫描数据库，识别所有治理问题

**命令**:
```bash
cd d:\skills\skill-registry
python clean_naming.py dry-run
python clean_naming.py report
```

**检查项**:

| 检查项 | 检查方法 | 严重度 |
|--------|---------|--------|
| slug含版本号 | `WHERE slug GLOB '*-[0-9]*'` | 高 |
| slug含-pro后缀 | `WHERE slug LIKE '%-pro'` | 高 |
| pricing_model与edition不一致 | 字段交叉验证 | 高 |
| category被source污染 | `WHERE category IN ('opensource','original','enterprise')` | 中 |
| displayName超长(>20字符) | `WHERE LENGTH(current_display_name) > 20` | 中 |
| summary超长(>100字符) | `WHERE LENGTH(current_summary) > 100` | 中 |
| skill_type为NULL | `WHERE skill_type IS NULL` | 中 |
| workflow_state卡在step1 | `WHERE workflow_state = 'step1_read_original' AND current_status != 'registered'` | 高 |
| local_path文件不存在 | 逐条检查Path.exists() | 高 |
| YAML解析错误 | 逐条解析SKILL.md frontmatter | 高 |
| 孤儿记录(无parent_slug且被取代) | 检查round-1遗留 | 中 |
| 重复source_slug(>3条) | `GROUP BY source_slug HAVING COUNT(*) > 3` | 中 |

**输出**: `d:\skills\skill-registry\governance-report.json`

---

### 阶段2: 命名治理 (Naming Governance)

**目标**: 修复slug命名规范问题

**命令**:
```bash
# 合并 -free/-pro 成对记录
python clean_naming.py merge-pairs --execute

# 修复字段不一致
python clean_naming.py fix-fields --execute

# 修复category污染
python clean_naming.py fix-category --execute
```

**治理规则**:

| 问题类型 | 治理策略 | 保护措施 |
|---------|---------|---------|
| -pro后缀(无-free配对) | 改为-paid后缀或base slug | 检查是否已上传 |
| 版本号写入slug | 移除版本号，写入current_version | 检查是否已上传 |
| pricing_model=NULL | 根据edition推断填充 | - |
| edition=NULL | 根据pricing_model推断填充 | - |
| category=opensource | 改为Development | - |
| category=original | 改为Productivity | - |

**已上传保护**: 已上传到平台的slug不可修改，标记为legacy_slug

---

### 阶段3: 字段修复 (Field Repair)

**目标**: 修复displayName、summary、YAML语法等问题

**AI操作**:

1. **displayName超长修复**:
   - >40字符: 从slug派生Title Case名称，截断至20字符
   - 26-40字符: 去除副标题，保留主名称
   - 21-25字符: 评估是否可接受，否则精简

2. **YAML解析错误修复**:
   - 引号未转义: 改用单引号包裹并转义
   - 反引号: 去除或改用块标量
   - 缩进错误: 修正缩进层级

3. **编码错误修复**:
   - 检测displayName中的乱码字符
   - 重新以UTF-8编码读取源文件

---

### 阶段4: 孤儿记录治理 (Orphan Governance)

**目标**: 处理多轮差异化产生的孤儿记录

**检查逻辑**:
```sql
-- 查找round-1孤立paid记录(被round-2取代)
SELECT s.* FROM skills s
WHERE s.edition = 'paid'
  AND s.parent_slug IS NULL
  AND EXISTS (
    SELECT 1 FROM skills s2
    WHERE s2.source_slug = s.source_slug
      AND s2.edition = 'paid'
      AND s2.id != s.id
      AND s2.parent_slug IS NOT NULL
  )
```

**治理策略**:

| 策略 | 适用场景 | 操作 |
|------|---------|------|
| A. 标记废弃(推荐) | 已上传到平台 | 设置 `workflow_state='deprecated'`, 添加 `superseded_by` 字段 |
| B. 重分配source_slug | 未上传 | 修改source_slug为 `{原值}__r1` |
| C. 级联删除 | 未上传且无子表引用 | 删除记录及所有子表引用 |

---

### 阶段5: 工作流状态回填 (Workflow State Backfill)

**目标**: 修复1848条卡在step1的记录

**命令**:
```bash
cd c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5
python round2_workflow_fix.py          # dry-run预览
python round2_workflow_fix.py --apply  # 执行回填
```

**回填规则**:

| current_status | 上传状态 | 目标workflow_state | 预计记录数 |
|---------------|---------|-------------------|-----------|
| registered | 未上传 | step1_read_original | 20 |
| differentiated | 未上传 | step5_add_deps | 847 |
| optimized | 未上传 | step7_validate | 879 |
| * | 已上传免费版 | step8_upload_free | 102 |
| * | 双版本均上传 | completed | 61 |

---

### 阶段6: 质量验证 (Quality Validation)

**目标**: 验证治理结果，确保无遗留问题

**检查项**:

```bash
# 1. 验证命名规范
python clean_naming.py report  # 确认0个问题

# 2. 验证工作流状态
python -c "
import sqlite3
conn = sqlite3.connect(r'd:\skills\skill-registry.db')
c = conn.cursor()
c.execute('SELECT workflow_state, COUNT(*) FROM skills GROUP BY workflow_state')
for row in c.fetchall():
    print(f'{row[0]}: {row[1]}')
"

# 3. 验证local_path有效性
python -c "
import sqlite3
from pathlib import Path
conn = sqlite3.connect(r'd:\skills\skill-registry.db')
c = conn.cursor()
c.execute('SELECT slug, local_path FROM skills')
missing = 0
for slug, path in c.fetchall():
    if path and not Path(path).exists():
        print(f'Missing: {slug} -> {path}')
        missing += 1
print(f'Total missing: {missing}')
"
```

---

### 阶段7: 治理报告 (Governance Report)

**目标**: 生成治理结果报告

**AI操作**:

1. 汇总治理结果:
   - 命名问题修复数
   - 字段修复数
   - 孤儿记录处理数
   - 工作流状态回填数
   - 质量验证结果

2. 生成可视化报告（PureShowWidget）

3. 更新 `governance-report.json`

---

## 与其他触发机制的协作

| 触发词 | 系统 | 作用 | 治理关系 |
|--------|------|------|---------|
| **"更新"** | update_mechanism.py | 检查来源更新 | 治理验证更新后的命名 |
| **"发现"** | auto_discover.py | 发现新skill | 治理确保新skill符合规范 |
| **"治理"** | clean_naming.py | 全面清理DB | 治理是其他两个的保障层 |

治理应在"发现"和"更新"之后执行，确保新增/更新的记录符合规范。

---

## 完整一键执行

```bash
# 步骤1: 诊断扫描
cd d:\skills\skill-registry
python clean_naming.py dry-run

# 步骤2: 执行命名治理
python clean_naming.py execute

# 步骤3: AI执行字段修复（displayName/YAML/编码）

# 步骤4: AI执行孤儿记录治理

# 步骤5: 工作流状态回填
cd c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5
python round2_workflow_fix.py --apply

# 步骤6: 质量验证
cd d:\skills\skill-registry
python clean_naming.py report

# 步骤7: 生成报告
```

---

## 治理频率

| 场景 | 频率 |
|------|------|
| 日常维护 | 每次"发现"或"更新"后 |
| 全面治理 | 用户输入"治理"时 |
| 定期检查 | 每周一次dry-run扫描 |

---

## 文件清单

| 文件 | 路径 | 作用 |
|------|------|------|
| 治理脚本 | `d:\skills\skill-registry\clean_naming.py` | 命名治理主控 |
| 触发指令 | `d:\skills\skill-registry\GOVERNANCE_TRIGGER.md` | 治理流程AI手册(本文件)|
| 工作流修复 | `c:\Users\thcd\.trae-cn\work\...\round2_workflow_fix.py` | 工作流状态回填 |
| 治理报告 | `d:\skills\skill-registry\governance-report.json` | 治理结果报告 |
| 框架ADR | `d:\skills\skill-registry\FRAMEWORK_ADR.md` | 架构决策记录 |

---

## 更新日志

| 日期 | 变更 |
|------|------|
| 2026-07-20 | 初版创建，7阶段治理流水线，补全三触发体系 |
