# 第6轮提示词 (L1-L8 冗余文件清理)

```
任务: 清理项目中的冗余文件，释放~23.9MB磁盘空间

背景: 经过前5轮修复（P0管道断裂→Q1-Q5质量门→D1-D3数据追踪→D4-D6写入收口→A1-A3架构闭环），项目核心功能已修复完毕。但项目中积累了大量__pycache__、DB备份、旧版本脚本和过期报告文件，占用~23.9MB空间。本轮聚焦安全清理这些冗余文件。

约束:
- 禁止删除活跃使用的文件（模板、当前轮文档）
- DB备份必须先归档再删除（移动到d:\skills\data\archive\）
- 每步删除后立即验证项目功能不受影响
- 不使用mock/TODO/pass/fallback
- 删除前确认文件无外部引用

---

## L1: 删除__pycache__目录 (2个目录, 75个.pyc, 1,228.1 KB)

文件清单:
- d:\skills\tools\__pycache__ (74个.pyc文件)
- d:\skills\tools\skill_core\__pycache__ (1个.pyc文件)

操作:
```powershell
cd d:\skills\tools
Remove-Item -Recurse -Force __pycache__
Remove-Item -Recurse -Force skill_core\__pycache__
```

验证:
```powershell
# 确认目录已删除
Test-Path __pycache__
Test-Path skill_core\__pycache__
# 预期: 两者均为False

# 确认核心功能不受影响（重新生成pycache）
python -c "import sys; sys.path.insert(0,'.'); sys.path.insert(0,'../config'); from skill_core.rules import RESERVED_WORDS; print('OK:', RESERVED_WORDS)"
# 预期: 正常输出 RESERVED_WORDS
```

---

## L2: 删除0字节空文件 (1个文件, 0 KB)

文件清单:
- d:\skills\tools\parse_report.py (0字节, 已确认无外部引用)

操作:
```powershell
cd d:\skills\tools
Remove-Item parse_report.py
```

验证:
```powershell
Test-Path parse_report.py
# 预期: False
```

---

## L3: 删除旧版本脚本 (3个文件, ~21.2 KB)

已确认无外部引用（grep验证：仅自身匹配，无其他文件import）。

文件清单:
- d:\skills\tools\batch_approve_v2.js (5.1 KB) - 旧版批量审批脚本
- d:\skills\tools\batch_operations_v2.py (10.1 KB) - 旧版批量操作脚本
- d:\skills\tools\update_v2_and_report.py (6.0 KB) - 旧版更新报告脚本

操作:
```powershell
cd d:\skills\tools
Remove-Item batch_approve_v2.js
Remove-Item batch_operations_v2.py
Remove-Item update_v2_and_report.py
```

验证:
```powershell
# 确认文件已删除
Test-Path batch_approve_v2.js
Test-Path batch_operations_v2.py
Test-Path update_v2_and_report.py
# 预期: 三者均为False

# 确认核心脚本仍正常
python -m py_compile quality_gate.py
python -m py_compile trace_llm_scorer.py
python -m py_compile generate_skill.py
# 预期: 无报错
```

---

## L4: 归档后删除DB备份 (5个文件, 22.5 MB)

DB备份文件占空间最大。先归档到d:\skills\data\archive\，再从原位置删除。

文件清单:
- d:\skills\data\backups\skill-registry_phase3_backup_20260724_120254.db (11.2 MB)
- d:\skills\data\backups\skill-registry_pre_pricing_v34_backup.db (7.6 MB)
- d:\skills\data\reports\upload_tracking.json.backup_round25 (0.7 MB)
- d:\skills\data\reports\upload_tracking_v1_backup.json (0.7 MB)
- d:\skills\data\reports\upload_tracking_v2_backup.json (2.2 MB)

操作:
```powershell
# 创建归档目录
New-Item -ItemType Directory -Force -Path d:\skills\data\archive

# 移动DB备份到归档目录
Move-Item d:\skills\data\backups\skill-registry_phase3_backup_20260724_120254.db d:\skills\data\archive\
Move-Item d:\skills\data\backups\skill-registry_pre_pricing_v34_backup.db d:\skills\data\archive\

# 移动JSON备份到归档目录
Move-Item d:\skills\data\reports\upload_tracking.json.backup_round25 d:\skills\data\archive\
Move-Item d:\skills\data\reports\upload_tracking_v1_backup.json d:\skills\data\archive\
Move-Item d:\skills\data\reports\upload_tracking_v2_backup.json d:\skills\data\archive\
```

验证:
```powershell
# 确认原位置已无备份文件
Get-ChildItem d:\skills\data\backups\*.db | Measure-Object
# 预期: Count=0 (或仅保留当前活跃DB)

Get-ChildItem d:\skills\data\reports\*backup* | Measure-Object
# 预期: Count=0

# 确认归档目录有5个文件
Get-ChildItem d:\skills\data\archive | Measure-Object
# 预期: Count=5

# 确认活跃DB仍可访问
python -c "import sys; sys.path.insert(0, r'd:\skills\tools'); sys.path.insert(0, r'd:\skills\config'); from config import DB_PATH; import sqlite3; conn=sqlite3.connect(DB_PATH); print('DB OK, tables:', len(conn.execute('SELECT name FROM sqlite_master WHERE type=\"table\"').fetchall())); conn.close()"
# 预期: DB OK, tables: N (N>0)
```

---

## L5: 删除过期报告文件 (1个文件, 1.7 KB)

文件清单:
- d:\skills\tools\update-report.json (1.7 KB) - 旧版更新报告（已被upload_tracking.json替代）

操作:
```powershell
cd d:\skills\tools
Remove-Item update-report.json
```

验证:
```powershell
Test-Path update-report.json
# 预期: False
```

---

## L6: 整理.trae/documents/文档 (7个文件, 128.4 KB)

评估每个文档的保留价值:

| 文件 | 大小 | 状态 | 操作 |
|------|------|------|------|
| P0-pipeline-breakage-fix-plan.md | 14.0 KB | 已被round5文档取代 | 归档 |
| round5-implementation-plan.md | 24.3 KB | 当前轮实施计划 | 保留 |
| round5-prompt-and-review.md | 13.9 KB | round5早期版本 | 归档 |
| round5-review-and-prompt.md | 18.6 KB | 当前轮复核报告 | 保留 |
| skill-automation-comprehensive-audit-and-fix-plan.md | 19.0 KB | 原始审计报告 | 归档 |
| skill-automation-comprehensive-fix-plan-v2.md | 12.3 KB | 已被v3取代 | 归档 |
| skill-automation-comprehensive-fix-plan-v3.md | 26.5 KB | V3修复文档 | 保留 |

操作:
```powershell
# 创建文档归档目录
New-Item -ItemType Directory -Force -Path d:\skills\.trae\documents\archive

# 移动被取代的文档
Move-Item d:\skills\.trae\documents\P0-pipeline-breakage-fix-plan.md d:\skills\.trae\documents\archive\
Move-Item d:\skills\.trae\documents\round5-prompt-and-review.md d:\skills\.trae\documents\archive\
Move-Item d:\skills\.trae\documents\skill-automation-comprehensive-audit-and-fix-plan.md d:\skills\.trae\documents\archive\
Move-Item d:\skills\.trae\documents\skill-automation-comprehensive-fix-plan-v2.md d:\skills\.trae\documents\archive\
```

验证:
```powershell
# 确认归档目录有4个文件
Get-ChildItem d:\skills\.trae\documents\archive | Measure-Object
# 预期: Count=4

# 确认活跃文档保留
Get-ChildItem d:\skills\.trae\documents\*.md | Measure-Object
# 预期: Count=3 (round5-implementation-plan, round5-review-and-prompt, fix-plan-v3)
```

---

## L7-L8: 综合验证

```powershell
cd d:\skills\tools

# 1. 全部核心脚本语法检查
python -m py_compile quality_gate.py
python -m py_compile trace_llm_scorer.py
python -m py_compile generate_skill.py
python -m py_compile ops闭环.py
python -m py_compile batch_l2_eval.py
python -m py_compile skill_batch_upgrader_v3.py
python -m py_compile skill_core\rules.py
python -m py_compile skill_core\parser.py
# 预期: 全部无报错

# 2. 3个验证skill质量门无回归
python quality_gate.py "d:\skills\hermes-skills\Creative\free\ad-creative-intel-free" --json
python quality_gate.py "d:\skills\hermes-skills\Creative\free\agentvibes-skill-free" --json
python quality_gate.py "d:\skills\hermes-skills\Agents\free\agent-assistant-free" --json
# 预期: 结果与第5轮基线一致

# 3. batch_l2_eval无报错
python batch_l2_eval.py --limit 1 --dry-run
# 预期: 正常输出候选skill列表

# 4. ops闭环.py正常运行
python ops闭环.py -o "$env:TEMP\ops_final.json" 2>&1 | Out-Null
# 预期: 正常生成报告

# 5. 确认磁盘空间已释放
# __pycache__: ~1.2 MB
# DB备份(归档): ~22.5 MB (从工作目录移至archive)
# 旧脚本: ~21.2 KB
# 过期报告: ~1.7 KB
# 被取代文档(归档): ~59.2 KB
# 总计释放工作目录空间: ~23.9 MB
```

---

## 验收标准

| # | 验收项 | 验证方法 |
|---|--------|---------|
| 1 | __pycache__目录已删除 | L1验证 Test-Path=False |
| 2 | 0字节空文件已删除 | L2验证 Test-Path=False |
| 3 | 3个旧版本脚本已删除 | L3验证 Test-Path=False |
| 4 | 5个DB备份已归档 | L4验证 archive目录Count=5 |
| 5 | 过期报告已删除 | L5验证 Test-Path=False |
| 6 | 4个被取代文档已归档 | L6验证 archive目录Count=4 |
| 7 | 核心脚本语法全部通过 | L7 Step 1 |
| 8 | 3个skill质量门无回归 | L7 Step 2 |
| 9 | batch_l2_eval无报错 | L7 Step 3 |
| 10 | ops闭环.py正常运行 | L7 Step 4 |

---

## 执行顺序

1. L1: 删除__pycache__ → 验证skill_core导入
2. L2: 删除空文件
3. L3: 删除旧脚本 → 验证核心脚本语法
4. L4: 归档DB备份 → 验证DB可访问
5. L5: 删除过期报告
6. L6: 归档被取代文档
7. L7-L8: 综合验证

完成后生成第7轮提示词（如有剩余裸SQL批次处理或其他待办）。
```
