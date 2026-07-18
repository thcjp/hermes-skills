---
slug: xlsx-handler-pro
name: xlsx-handler-pro
version: "1.0.0"
displayName: XLSX处理专业版
summary: 企业级 XLSX 读写引擎，含批量处理、大文件流式、公式审计、跨平台兼容与数据源对接。
license: MIT
edition: pro
description: |-
  XLSX 处理专业版在免费版基础上扩展批量处理、大文件流式读写、工作簿差异对比、公式审计与依赖追踪、数据源对接与跨平台深度兼容能力，面向数据团队与企业场景提供完整的工作簿治理方案。

  核心能力：

  - 覆盖免费版全部能力（无单文件限制）
  - 新增批量文件处理与并行读写
  - 新增大文件流式处理（>10MB）
  - 新增工作簿差异对比与合并
  - 新增公式审计与依赖追踪
  - 新增跨平台深度兼容测试（Excel / WPS / LibreOffice / Numbers）
  - 新增数据源对接（`PostgreSQL`、MySQL、CSV、API）
  - 新增完整故障排查矩阵与多角色场景指南

  适用场景：

  - 企业批量工作簿处理与版本治理
  - 大文件流式读写与内存优化
  - 公式审计与依赖关系分析
  - 跨平台分发与兼容性测试

  差异化：相比免费版，专业版提供完整的批量处理、流式读写、公式审计与跨平台兼容策略，适合 10 人以上团队与企业级使用；支持对接 `PostgreSQL`、MySQL 等数据源，可集成到 CI/CD 流水线。

  触发关键词：XLSX 批量、流式处理、公式审计、跨平台兼容、工作簿对比、`PostgreSQL`、企业表格
tags:
- 集成工具
- 表格处理
- 企业级
- 工作簿治理
tools:
- read
- exec
---

# XLSX 处理（专业版）

专业版在免费版基础上扩展批量处理、流式读写、公式审计、跨平台兼容与数据源对接能力，面向团队与企业场景提供完整的工作簿治理方案。

## 概述

企业场景下的 XLSX 处理远超单文件编辑：批量处理数百份文件、流式读写超过 100MB 的大文件、审计公式依赖关系、跨平台分发兼容、与数据库双向同步。专业版把这些场景统一为"读取—治理—校验—分发"工作流，支持版本管理、性能优化与跨平台兼容。

## 核心能力

### 免费版能力（无限制）
- 按任务选择 pandas / openpyxl 路径
- 保留公式、样式、合并单元格、定义名称
- 日期序列号与 1900/1904 系统处理
- 类型保护（长数字、电话、邮编）
- 工作簿结构保护与错误校验

### 专业版新增能力
| 能力模块 | 输入 | 输出 | 适用场景 |
|---------|------|------|---------|
| 批量处理 | 文件列表 | 处理结果 | 大规模编辑 |
| 流式读写 | 大文件 | 流式结果 | >10MB 文件 |
| 工作簿对比 | 两个文件 | 差异报告 | 版本治理 |
| 公式审计 | 工作簿 | 依赖图 | 错误排查 |
| 跨平台兼容测试 | 文件 | 兼容性报告 | 多端分发 |
| 数据源对接 | 连接配置 | 双向同步 | 数据库集成 |
| 公式追踪 | 单元格 | 影响范围 | 修改影响评估 |
| 保护与权限 | 区域 + 密码 | 锁定规则 | 防误改 |

## 使用场景

### 场景一：批量文件处理（数据团队角色）
部门有 200 份结构相同的 Excel 文件，需要批量修改某个 Sheet 的某个字段。专业版提供批量处理脚本，并行执行并输出成功 / 失败列表。

### 场景二：大文件流式读写（运维角色）
单文件 500MB，包含百万行数据。专业版使用 `read_only=True` 与 `write_only=True` 流式模式，内存占用控制在 100MB 以内。

### 场景三：公式审计与依赖追踪（财务角色）
修改一个单元格后哪些公式会受影响？专业版输出完整依赖图——从源单元格追踪到所有引用它的公式，可视化影响范围。

### 场景四：跨平台兼容测试（IT 角色）
报表需在 Excel / WPS / LibreOffice 三个平台打开。专业版自动检测使用了哪些高级特性，给出各平台兼容性报告与降级建议。

### 场景五：工作簿差异对比（合规角色）
两版财务报表差异在哪？专业版逐 Sheet 逐单元格对比，输出新增、删除、修改的清单。

### 场景六：数据库双向同步（数据工程师角色）
`PostgreSQL` 表与 Excel 双向同步——从数据库抽取数据写入 Excel，或从 Excel 读取数据回写到数据库。专业版提供完整流水线，含错误处理与重试机制。

## 快速开始

### 批量处理脚本

```python
from openpyxl import load_workbook
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_file(path: str, field: str, new_value: str) -> dict:
    """处理单个文件：修改指定字段。"""
    try:
        wb = load_workbook(path)
        ws = wb['Data']
        # 找到字段并修改
        for row in ws.iter_rows():
            for cell in row:
                if cell.value == field:
                    ws.cell(row=cell.row, column=cell.column + 1).value = new_value
        wb.save(path)
        return {'file': path, 'status': 'ok'}
    except Exception as e:
        return {'file': path, 'status': 'failed', 'error': str(e)}

def batch_process(file_list: list, field: str, new_value: str, workers: int = 4) -> dict:
    """批量处理多个文件。"""
    results = {'success': 0, 'failed': []}
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(process_file, f, field, new_value): f for f in file_list}
        for fut in as_completed(futures):
            r = fut.result()
            if r['status'] == 'ok':
                results['success'] += 1
            else:
                results['failed'].append(r)
    return results

files = list(Path('reports').glob('*.xlsx'))
result = batch_process(files, '状态', '已审核')
print(f"成功：{result['success']}，失败：{len(result['failed'])}")
```

### 大文件流式读写

```python
from openpyxl import load_workbook, Workbook

def stream_filter_large(input_path: str, output_path: str, condition):
    """流式过滤大文件，保留符合条件的数据。"""
    # 流式读取
    wb_in = load_workbook(input_path, read_only=True)
    ws_in = wb_in.active

    # 流式写入
    wb_out = Workbook(write_only=True)
    ws_out = wb_out.create_sheet('Filtered')

    # 写入表头
    headers = next(ws_in.iter_rows(values_only=True))
    ws_out.append(headers)

    # 流式过滤
    count = 0
    for row in ws_in.iter_rows(min_row=2, values_only=True):
        if condition(row):
            ws_out.append(row)
            count += 1

    wb_out.save(output_path)
    wb_in.close()
    print(f"过滤完成，保留 {count} 行")

# 示例：保留金额 > 10000 的记录
stream_filter_large(
    'large_data.xlsx',
    'filtered.xlsx',
    lambda row: row[3] is not None and row[3] > 10000
)
```

### 公式依赖追踪

```python
from openpyxl import load_workbook
import re

def trace_dependents(wb_path: str, sheet: str, cell: str) -> dict:
    """追踪单元格的所有依赖（哪些公式引用了它）。"""
    wb = load_workbook(wb_path, data_only=False)
    ws = wb[sheet]
    dependents = []

    # 遍历所有单元格找引用
    for row in ws.iter_rows():
        for c in row:
            if c.value and isinstance(c.value, str) and c.value.startswith('='):
                # 简化版：检查是否引用了目标单元格
                if re.search(rf'\b{re.escape(cell)}\b', c.value, re.IGNORECASE):
                    dependents.append({
                        'cell': c.coordinate,
                        'formula': c.value
                    })

    return {'target': cell, 'dependents': dependents}

result = trace_dependents('report.xlsx', 'Sheet1', 'A1')
print(f"A1 被以下 {len(result['dependents'])} 个公式引用：")
for d in result['dependents']:
    print(f"  {d['cell']}: {d['formula']}")
```

## 配置示例

### 工作簿差异对比

```python
from openpyxl import load_workbook

def compare_workbooks(path1: str, path2: str) -> dict:
    """对比两个工作簿，输出差异清单。"""
    wb1 = load_workbook(path1, data_only=False)
    wb2 = load_workbook(path2, data_only=False)

    diff = {
        'sheets_added': [],
        'sheets_removed': [],
        'cell_changes': []
    }

    # Sheet 级差异
    s1, s2 = set(wb1.sheetnames), set(wb2.sheetnames)
    diff['sheets_added'] = list(s2 - s1)
    diff['sheets_removed'] = list(s1 - s2)

    # 共有 Sheet 的单元格差异
    for name in s1 & s2:
        ws1, ws2 = wb1[name], wb2[name]
        max_row = max(ws1.max_row, ws2.max_row)
        max_col = max(ws1.max_column, ws2.max_column)
        for r in range(1, max_row + 1):
            for c in range(1, max_col + 1):
                v1 = ws1.cell(row=r, column=c).value
                v2 = ws2.cell(row=r, column=c).value
                if v1 != v2:
                    diff['cell_changes'].append({
                        'sheet': name,
                        'cell': ws1.cell(row=r, column=c).coordinate,
                        'before': v1,
                        'after': v2
                    })

    return diff

import json
diff = compare_workbooks('v1.xlsx', 'v2.xlsx')
print(json.dumps(diff, indent=2, ensure_ascii=False, default=str))
```

### 跨平台兼容性测试

```python
from openpyxl import load_workbook

COMPAT_MATRIX = {
    'dynamic_arrays': {'Excel365': True, 'LegacyExcel': False, 'WPS': False, 'LibreOffice': True, 'Numbers': False},
    'xlookup': {'Excel365': True, 'LegacyExcel': False, 'WPS': True, 'LibreOffice': True, 'Numbers': False},
    'let_lambda': {'Excel365': True, 'LegacyExcel': False, 'WPS': False, 'LibreOffice': False, 'Numbers': False},
    'power_query': {'Excel365': True, 'LegacyExcel': 'partial', 'WPS': False, 'LibreOffice': False, 'Numbers': False},
    'slicers': {'Excel365': True, 'LegacyExcel': True, 'WPS': True, 'LibreOffice': 'partial', 'Numbers': False},
}

def check_compatibility(wb_path: str) -> dict:
    """检查工作簿使用的特性，输出跨平台兼容性。"""
    wb = load_workbook(wb_path, data_only=False)
    used_features = set()

    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if cell.value and isinstance(cell.value, str):
                    v = cell.value.upper()
                    if 'XLOOKUP' in v: used_features.add('xlookup')
                    if 'FILTER(' in v or 'UNIQUE(' in v or 'SORT(' in v: used_features.add('dynamic_arrays')
                    if 'LET(' in v or 'LAMBDA(' in v: used_features.add('let_lambda')

    # 检查 Power Query（queries 元数据）
    if hasattr(wb, 'queries') and wb.queries:
        used_features.add('power_query')

    # 生成兼容性报告
    report = {'used_features': list(used_features), 'platforms': {}}
    for platform in ['Excel365', 'LegacyExcel', 'WPS', 'LibreOffice', 'Numbers']:
        issues = []
        for f in used_features:
            support = COMPAT_MATRIX.get(f, {}).get(platform, 'unknown')
            if support is False:
                issues.append(f)
        report['platforms'][platform] = {
            'compatible': len(issues) == 0,
            'incompatible_features': issues
        }

    return report
```

### 数据源对接 `PostgreSQL`

```python
import psycopg2
from openpyxl import Workbook
from contextlib import closing
import os

def sync_pg_to_excel(query: str, output_path: str):
    """从 PostgreSQL 抽取数据到 Excel。"""
    conn_str = os.environ.get('PG_CONN_STR', '')
    if not conn_str:
        raise ValueError("请设置 PG_CONN_STR 环境变量")

    with closing(psycopg2.connect(conn_str)) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            columns = [desc[0] for desc in cur.description]
            rows = cur.fetchall()

    wb = Workbook(write_only=True)
    ws = wb.create_sheet('数据')
    ws.append(columns)
    for row in rows:
        ws.append(row)
    wb.save(output_path)
    print(f"导出 {len(rows)} 行到 {output_path}")

sync_pg_to_excel(
    "SELECT 日期, 区域, 销售额 FROM sales WHERE 月份 = '2026-07'",
    'sales_2026_07.xlsx'
)
```

## 最佳实践

### 批量处理
1. **并行控制**：worker 数不超过 5（受文件 IO 限制），过多会拖慢速度。
2. **错误隔离**：单文件失败不影响整体，记录失败列表后继续。
3. **进度反馈**：长任务每 10 个文件打印进度。
4. **原子保存**：先写入临时文件，成功后重命名覆盖原文件，避免半成品。

### 大文件流式
1. **读写分离**：用 `read_only` + `write_only` 模式，避免全量载入。
2. **分块处理**：单次处理 1 万行，写完后释放内存。
3. **避免样式**：流式模式不支持样式，需样式时改为分批处理。
4. **索引优化**：流式读取时不要随机访问，按顺序遍历。

### 公式审计
1. **依赖图**：构建单元格引用图，可视化影响范围。
2. **修改前评估**：改动源单元格前查询所有依赖，避免连锁错误。
3. **错误隔离**：公式审计发现的错误应隔离标记，不应静默忽略。
4. **版本对比**：审计结果与上一版对比，跟踪新增 / 删除的公式。

### 跨平台兼容
1. **特性矩阵**：建立特性 × 平台支持矩阵，分发前自动检查。
2. **降级建议**：对不兼容特性提供降级方案（如 XLOOKUP → INDEX-MATCH）。
3. **测试平台**：分发前至少在 Excel 与 WPS 中打开验证。
4. **保留备份**：分发版本与原版分目录存放，便于回滚。

### 数据源对接
1. **凭据安全**：连接字符串从环境变量读取，不硬编码。
2. **流式查询**：大结果集使用 `fetchmany` 而非 `fetchall`。
3. **事务隔离**：报表场景使用只读事务。
4. **错误重试**：网络抖动场景加 3 次重试。

## 常见问题

### Q1：批量处理内存飙升？
A：每个文件处理完立即 `wb.close()` 释放。worker 数控制在 4 以内，过多会争抢内存。

### Q2：流式模式不支持样式？
A：`write_only=True` 模式不支持单元格样式。需要样式时分批处理（每批 1 万行用普通模式），或先流式生成数据再用普通模式重新打开加样式。

### Q3：公式追踪漏掉跨 Sheet 引用？
A：简化版正则只匹配同一 Sheet 内引用。跨 Sheet 引用形如 `Sheet2!A1`，需要单独处理 `!` 分隔符。

### Q4：`PostgreSQL` 抽取超时？
A：报表场景使用只读事务 + 短超时（30 秒）。大表查询加索引或物化视图。

### Q5：跨平台兼容性测试耗时？
A：测试 100+ 特性 × 5 平台较慢。建议建立特性白名单，只测试工作簿实际使用的特性。

### Q6：工作簿对比工具输出过多差异？
A：先对比 Sheet 列表，再针对共有 Sheet 对比。单元格差异按区域聚合，避免逐条列出。

### Q7：保护规则被绕过？
A：openpyxl 的工作表保护可被脚本绕过。需要高安全级别时建议改用文件加密或数字签名。

### Q8：流式写入后文件无法打开？
A：`write_only=True` 模式必须用 `ws.append()` 添加数据，不能直接设置单元格值。保存前确认所有数据已 append。

### Q9：批量处理中途中断如何续传？
A：把已完成文件列表写入检查点文件，重启时跳过已完成项。失败列表单独记录以便重试。

### Q10：跨平台分发后筛选丢失？
A：LibreOffice 与 Numbers 对部分筛选语法支持不全。建议分发前同时测试三个平台，必要时降级为基本筛选。

## 故障排查表

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|------|---------|---------|--------|
| 批量处理内存飙升 | 未释放工作簿 | 每文件后 wb.close() | 高 |
| 流式写入文件损坏 | 用了 cell 赋值 | 改用 ws.append() | 高 |
| 公式追踪漏跨 Sheet | 未处理 ! 分隔符 | 单独处理跨 Sheet | 高 |
| PG 抽取超时 | 索引缺失 | 加索引或物化视图 | 中 |
| 兼容性测试耗时 | 测试全部特性 | 用特性白名单 | 中 |
| 对比输出过多差异 | 逐条列出 | 按区域聚合 | 中 |
| 保护规则被绕过 | 脚本可破解 | 改用文件加密 | 中 |
| 大文件读取慢 | 全量载入 | 改 read_only 模式 | 低 |
| 续传失败 | 检查点损坏 | 改用 SQLite 存检查点 | 低 |
| 跨平台筛选丢失 | 高级筛选 | 降级为基本筛选 | 低 |

## 版本升级迁移指南

从免费版升级到专业版时：
1. **代码兼容**：免费版的所有脚本在专业版中可直接复用
2. **新增模块**：升级后启用批量处理、流式读写、公式审计模块
3. **数据库依赖**：专业版对接 `PostgreSQL` 需安装 `psycopg2`，对接 MySQL 需 `pymysql`
4. **兼容性测试**：分发版本前运行兼容性测试脚本

## 专业版特性

本专业版相比免费版新增以下能力：
- 批量文件处理：并行读写与错误隔离
- 大文件流式处理：>10MB 文件内存可控
- 工作簿差异对比：版本治理利器
- 公式审计与依赖追踪：影响范围可视化
- 跨平台兼容性测试：5 平台全覆盖
- 数据源对接：`PostgreSQL`、MySQL、CSV、REST API
- 保护与权限管理：锁定 / 隐藏 / 密码
- 完整故障排查矩阵：10 项分级处理
- 多角色场景指南：数据、运维、财务、IT、合规
- 优先技术支持：工作日 4 小时内响应

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 单文件读写 + 结构检查 | 个人开发调试 |
| 收费专业版 | ¥39.9/月 | 全功能 + 批量 + 流式 + 数据源 + 优先支持 | 团队 / 企业 / 数据团队 |

专业版通过 SkillHub SkillPay 发布。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.9+
- **办公软件**：Excel / WPS / LibreOffice / Numbers

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本兼容性 |
|:-------|:-----|:---------|:---------|:-----------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 | 不限 |
| Python3 | 运行时 | 必需 | 官网下载 | 3.9+ |
| openpyxl | Python 库 | 必需 | `pip install openpyxl` | 3.0+ |
| pandas | Python 库 | 可选 | `pip install pandas` | 1.3+ |
| psycopg2 | Python 库 | 可选 | `pip install psycopg2-binary` | 2.9+ |
| pymysql | Python 库 | 可选 | `pip install pymysql` | 1.0+ |
| networkx | Python 库 | 可选 | `pip install networkx`（公式依赖图） | 2.6+ |

### API Key 配置
- 本 Skill 基于本地 Python 与 openpyxl，无需额外 API Key
- 数据库连接字符串存储于 `d:\skills\.skillhub-credentials\` 目录（已 gitignore）
- 凭据从环境变量读取，禁止硬编码到脚本
- 禁止在 SKILL.md 或脚本中硬编码任何密钥或 Token

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 生成 Python 脚本并执行；专业版涉及批量处理与数据源对接，建议在支持 Python 执行的环境下使用
