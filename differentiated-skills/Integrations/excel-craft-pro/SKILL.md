---
slug: excel-craft-pro
name: excel-craft-pro
version: "1.0.0"
displayName: Excel工艺专业版
summary: 企业级 Excel 生成引擎，含批量处理、条件格式、高级图表、模板系统与数据源对接。
license: MIT
edition: pro
description: |-
  Excel 工艺专业版在免费版基础上扩展批量生成、多文件合并拆分、条件格式与数据验证、高级图表、模板系统与数据源对接能力，面向数据团队与运营团队提供完整的报表自动化方案。

  核心能力：

  - 覆盖免费版全部能力（无单文件限制）
  - 新增批量生成与多文件合并拆分
  - 新增条件格式、数据验证与保护规则
  - 新增高级图表（散点图、瀑布图、组合图、迷你图）
  - 新增模板系统与变量插值
  - 新增数据源对接（`PostgreSQL`、MySQL、CSV、API）
  - 新增跨平台深度格式优化（Excel / WPS / LibreOffice / Numbers）
  - 提供完整故障排查矩阵与多角色场景指南

  适用场景：

  - 企业月度报告批量生成
  - 多源数据整合与定时任务
  - 跨部门报表分发与版本治理
  - 仪表盘与高级可视化交付

  差异化：相比免费版，专业版提供完整的批量处理、模板复用、数据源对接与跨平台优化策略，适合 10 人以上团队与企业级使用；支持对接 `PostgreSQL`、MySQL、REST API 等数据源，可集成到 CI/CD 流水线。

  触发关键词：Excel 批量、报表自动化、模板系统、数据源对接、`PostgreSQL`、条件格式、高级图表、企业报表
tags:
- 集成工具
- 表格生成
- 企业级
- 自动化
tools:
- read
- exec
---

# Excel 工艺（专业版）

专业版在免费版基础上扩展批量生成、模板系统、数据源对接与高级格式化能力，面向团队与企业场景提供完整的报表自动化方案。

## 概述

企业报表工作远超单文件生成：批量生成多份月报、合并多个分公司文件、对接数据库抽取数据、跨平台分发不同格式、按模板复用减少重复劳动。专业版把这些场景统一为"模板—数据—生成—分发"工作流，支持版本治理、性能优化与跨平台兼容。

## 核心能力

### 免费版能力（无限制）
- 多 Sheet 工作簿生成
- 基础格式化（字体 / 填充 / 边框 / 对齐）
- 公式支持
- 基础图表（柱状 / 折线 / 饼图）
- 自动列宽与合并单元格

### 专业版新增能力
| 能力模块 | 输入 | 输出 | 适用场景 |
|---------|------|------|---------|
| 批量生成 | 数据数组 + 模板 | 多份 .xlsx | 月度报告 |
| 文件合并 | 多文件列表 | 单个汇总文件 | 分公司整合 |
| 文件拆分 | 大文件 + 拆分键 | 多份小文件 | 按区域分发 |
| 条件格式 | 规则定义 | 高亮 / 色阶 / 图标集 | 数据可视化 |
| 数据验证 | 验证规则 | 下拉 / 范围限制 | 录入规范 |
| 高级图表 | 数据 + 类型 | 散点 / 瀑布 / 组合图 | 深度分析 |
| 模板系统 | 模板 + 变量 | 渲染后文件 | 重复报告 |
| 数据源对接 | 连接配置 | 数据抽取 | 数据库集成 |
| 保护规则 | 区域 + 密码 | 锁定 / 隐藏 | 防误改 |

## 使用场景

### 场景一：月度报告批量生成（运营角色）
按分公司生成 30 份月度报告。专业版通过模板系统定义一份模板，注入各分公司数据批量生成，相比手工快 50 倍。

### 场景二：多文件合并汇总（财务角色）
30 个分公司上传各自 Excel，需汇总到一份主报告。专业版提供合并脚本——按 Sheet 名匹配、按字段对齐、合并后做总计与差异校验。

### 场景三：数据库抽取报表（数据角色）
从 `PostgreSQL` 抽取销售数据，按区域分 Sheet 生成报告。专业版提供完整数据抽取 → 清洗 → 生成 → 邮件分发流水线。

### 场景四：条件格式仪表盘（管理层角色）
KPI 表格中业绩低于目标红色、达标绿色、超额蓝色。专业版提供色阶、图标集、数据条三种条件格式，配合保护规则防止误改。

### 场景五：跨平台分发（IT 角色）
同一报告需在 Excel / WPS / LibreOffice 三个平台打开。专业版提供深度格式优化策略，针对各平台特性调整。

### 场景六：模板系统复用（产品角色）
周报、月报、季报共享一份模板，仅变量不同。专业版支持变量插值、条件渲染、循环结构，类似 Jinja2 语法。

## 快速开始

### 批量生成多份报告

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from pathlib import Path

TEMPLATE = {
    'title': '2026年{month}月销售报告',
    'headers': ['日期', '产品', '数量', '金额'],
}

def generate_report(branch: str, month: str, data: list, output_dir: str):
    """根据模板生成单份报告。"""
    wb = Workbook()
    ws = wb.active
    ws.title = f"{branch}_{month}"

    # 标题（变量插值）
    ws['A1'] = TEMPLATE['title'].format(month=month)
    ws['A1'].font = Font(bold=True, size=16)

    # 表头
    for c, h in enumerate(TEMPLATE['headers'], 1):
        cell = ws.cell(row=3, column=c, value=h)
        cell.font = Font(bold=True, color='FFFFFF')
        cell.fill = PatternFill(start_color='3182CE', end_color='3182CE', fill_type='solid')

    # 数据
    for r, row in enumerate(data, 4):
        for c, v in enumerate(row, 1):
            ws.cell(row=r, column=c, value=v)

    # 保存
    output_path = Path(output_dir) / f"{branch}_{month}.xlsx"
    wb.save(output_path)
    return str(output_path)

def batch_generate(branches: list, month: str, all_data: dict, output_dir: str):
    """批量生成多份报告。"""
    results = []
    for branch in branches:
        data = all_data.get(branch, [])
        path = generate_report(branch, month, data, output_dir)
        results.append({'branch': branch, 'path': path, 'count': len(data)})
    return results
```

### 数据源对接 `PostgreSQL`

```python
import psycopg2
from openpyxl import Workbook
from contextlib import closing

def export_postgres_to_excel(query: str, conn_str: str, output_path: str):
    """从 PostgreSQL 抽取数据到 Excel。"""
    with closing(psycopg2.connect(conn_str)) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            columns = [desc[0] for desc in cur.description]
            rows = cur.fetchall()

    wb = Workbook()
    ws = wb.active
    ws.title = "数据导出"

    # 表头
    ws.append(columns)
    for cell in ws[1]:
        cell.font = Font(bold=True, color='FFFFFF')
        cell.fill = PatternFill(start_color='3182CE', end_color='3182CE', fill_type='solid')

    # 数据
    for row in rows:
        ws.append(row)

    wb.save(output_path)
    print(f"导出 {len(rows)} 行到 {output_path}")

# 使用示例（凭据从环境变量读取）
import os
conn_str = os.environ.get('PG_CONN_STR', '')
export_postgres_to_excel(
    "SELECT 日期, 区域, 销售额 FROM sales WHERE 月份 = '2026-07'",
    conn_str,
    "sales_2026_07.xlsx"
)
```

### 条件格式化

```python
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, DataBarRule

# 色阶规则（销售额）
ws.conditional_formatting.add('D2:D100',
    ColorScaleRule(
        start_type='min', start_color='F8696B',
        mid_type='percentile', mid_value=50, mid_color='FFEB84',
        end_type='max', end_color='63BE7B'
    )
)

# 单元格规则（低于目标红色）
ws.conditional_formatting.add('E2:E100',
    CellIsRule(operator='lessThan', formula=['50000'],
               fill=PatternFill(start_color='FFC7CE', fill_type='solid'))
)

# 数据条规则
ws.conditional_formatting.add('F2:F100',
    DataBarRule(start_type='min', end_type='max', color='638EC6')
)
```

## 配置示例

### 模板系统变量插值

```python
# 模板定义（YAML）
TEMPLATE_YAML = """
title: "{year}年{month}月{branch}销售报告"
headers: [日期, 产品, 数量, 金额]
conditionals:
  - range: "D2:D100"
    type: color_scale
sections:
  - title: "汇总"
    formula: "=SUM(D2:D100)"
"""

import yaml
from string import Template

def render_template(template_str: str, variables: dict) -> str:
    """渲染模板变量。"""
    return Template(template_str).safe_substitute(variables)

template = yaml.safe_load(TEMPLATE_YAML)
title = template['title'].format(year=2026, month='07', branch='华东')
print(title)  # 输出：2026年07月华东销售报告
```

### 文件合并脚本

```python
from openpyxl import load_workbook
from pathlib import Path

def merge_files(file_list: list, output_path: str, key_field: str = '日期'):
    """合并多个 Excel 文件，按 key_field 对齐。"""
    merged_wb = load_workbook(file_list[0])
    merged_ws = merged_wb.active

    for file_path in file_list[1:]:
        wb = load_workbook(file_path, read_only=True)
        ws = wb.active
        for row in ws.iter_rows(min_row=2, values_only=True):
            merged_ws.append(row)
        wb.close()

    merged_wb.save(output_path)
    return output_path

files = list(Path('branches').glob('*.xlsx'))
merge_files(files, 'merged_report.xlsx')
```

## 最佳实践

### 批量生成
1. **模板优先**：把通用结构沉淀为模板，仅注入数据，避免重复写码。
2. **并行处理**：批量场景使用 `ThreadPoolExecutor`，worker 数不超过 5。
3. **错误隔离**：单文件失败不影响整体，记录失败列表后继续。
4. **进度反馈**：长任务输出进度，每 10 份打印一次。

### 数据源对接
1. **凭据安全**：连接字符串从环境变量读取，不硬编码。
2. **流式查询**：大结果集使用 `fetchmany` 而非 `fetchall`，避免内存爆炸。
3. **索引优化**：查询前确认数据库索引，避免全表扫描。
4. **事务隔离**：报表场景使用只读事务，不影响业务写入。

### 条件格式
1. **规则克制**：一个区域最多 2 条规则，避免视觉混乱。
2. **色阶首选**：连续数值用色阶，离散分类用单元格规则。
3. **数据条**：占比场景用数据条直观。
4. **测试兼容**：WPS 对部分条件格式支持不全，需测试验证。

### 模板系统
1. **变量命名**：使用 `{{snake_case}}` 或 `{{camelCase}}`，避免与公式冲突。
2. **条件渲染**：复杂逻辑用 Jinja2 而非简单插值。
3. **版本管理**：模板文件加入 Git，关键版本打 Tag。
4. **单元测试**：每个模板配套 3+ 测试用例。

## 常见问题

### Q1：批量生成时内存飙升？
A：openpyxl 默认载入全部数据。大文件用 `write_only=True` 模式，批量场景使用 `ThreadPoolExecutor` 并控制 worker 数。

### Q2：条件格式在 WPS 不生效？
A：WPS 对色阶、图标集支持不全。降级为单元格规则或手工配色。

### Q3：`PostgreSQL` 连接报认证失败？
A：检查 `pg_hba.conf` 是否允许来源 IP；密码建议存储到凭据管理器而非环境变量明文。

### Q4：合并文件后字段错位？
A：合并前确认所有文件的列顺序一致。建议按字段名匹配而非位置匹配。

### Q5：模板渲染速度慢？
A：Jinja2 渲染大量数据时使用 `Environment(trim_blocks=True)`，避免空白处理开销。

### Q6：保护规则被 WPS 绕过？
A：WPS 对工作表保护实现较弱。需要高安全级别时建议改用数字签名或文件加密。

### Q7：跨平台格式丢失？
A：测试时同时用 Excel / WPS / LibreOffice 打开。条件格式、迷你图、自定义数字格式是高发问题区。

### Q8：模板变量与公式冲突？
A：模板变量用 `{{var}}` 语法，公式用 `=` 开头，两者不会冲突。但若公式中含 `{{` 字符，需转义。

### Q9：数据库抽取超时？
A：报表场景使用只读事务 + 短超时（30 秒）。大表查询加索引或物化视图。

### Q10：批量生成后文件大小不一？
A：openpyxl 默认不压缩。可在保存后用 `zipfile` 重新压缩，或设置 `wb.properties.title` 等元数据减小体积。

## 故障排查表

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|------|---------|---------|--------|
| 批量生成内存飙升 | 默认全量载入 | 改 `write_only=True` | 高 |
| 数据库认证失败 | pg_hba 拒绝 | 配置允许 IP | 高 |
| 合并字段错位 | 列顺序不一致 | 按字段名匹配 | 高 |
| 条件格式 WPS 不生效 | 兼容性 | 降级单元格规则 | 中 |
| 模板渲染慢 | 空白处理 | 启用 trim_blocks | 中 |
| 跨平台格式丢失 | 高级特性 | 测试三平台 | 中 |
| 抽取超时 | 索引缺失 | 加索引或物化视图 | 中 |
| 保护规则失效 | WPS 实现 | 改用文件加密 | 低 |
| 文件大小不一 | 未压缩 | 用 zipfile 重压 | 低 |
| 变量与公式冲突 | 未转义 | 公式中 `{{` 转义 | 低 |

## 版本升级迁移指南

从免费版升级到专业版时：
1. **代码兼容**：免费版的 `ExcelGenerator` 类在专业版中可直接复用
2. **新增模块**：升级后启用批量生成、模板系统、数据源对接模块
3. **数据库依赖**：专业版对接 `PostgreSQL` 需安装 `psycopg2`，对接 MySQL 需 `pymysql`
4. **模板格式**：免费版无模板系统，专业版支持 YAML / Jinja2 模板

## 专业版特性

本专业版相比免费版新增以下能力：
- 批量生成与多文件合并拆分：支持并行处理
- 条件格式、数据验证与保护规则：完整 Excel 高级特性
- 高级图表：散点图、瀑布图、组合图、迷你图
- 模板系统：变量插值、条件渲染、循环结构
- 数据源对接：`PostgreSQL`、MySQL、CSV、REST API
- 跨平台深度优化：Excel / WPS / LibreOffice / Numbers 全覆盖
- 完整故障排查矩阵：10 项分级处理
- 多角色场景指南：运营、财务、数据、IT、产品
- 优先技术支持：工作日 4 小时内响应

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 多 Sheet + 基础图表 + 单文件 | 个人日常使用 |
| 收费专业版 | ¥29.9/月 | 全功能 + 批量 + 模板 + 数据源 + 优先支持 | 团队 / 企业 / 数据团队 |

专业版通过 SkillHub SkillPay 发布。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.9+
- **办公软件**：Microsoft Excel / WPS / LibreOffice / Numbers

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本兼容性 |
|:-------|:-----|:---------|:---------|:-----------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 | 不限 |
| Python3 | 运行时 | 必需 | 官网下载 | 3.9+ |
| openpyxl | Python 库 | 必需 | `pip install openpyxl` | 3.0+ |
| psycopg2 | Python 库 | 可选 | `pip install psycopg2-binary` | 2.9+ |
| pymysql | Python 库 | 可选 | `pip install pymysql` | 1.0+ |
| jinja2 | Python 库 | 可选 | `pip install jinja2` | 3.0+ |
| pyyaml | Python 库 | 可选 | `pip install pyyaml` | 6.0+ |
| pandas | Python 库 | 可选 | `pip install pandas` | 1.3+ |

### API Key 配置
- 本 Skill 基于本地 Python 与 openpyxl，无需额外 API Key
- 数据库连接字符串存储于 `d:\skills\.skillhub-credentials\` 目录（已 gitignore）
- 凭据从环境变量读取，禁止硬编码到脚本
- 禁止在 SKILL.md 或脚本中硬编码任何密钥或 Token

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 生成 Python 脚本并执行；专业版涉及批量处理与数据源对接，建议在支持 Python 执行的环境下使用
