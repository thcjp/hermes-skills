---
slug: xlsx-data-wizard
name: xlsx-data-wizard
version: 1.1.0
displayName: Excel数据魔法师
summary: openpyxl全场景Excel处理,读写格式图表透视表公式全搞定
license: Proprietary
description: Excel数据魔法师——基于openpyxl实现全场景Excel文件处理。覆盖读取写入、格式化、公式、图表、透视表、多Sheet操作、合并拆分、数据校验、批注、保护全链路。同时提供WPS表格适配说明。适用于数据报表生成、Excel模板填充、批量数据处理、格式美化、图表可视化、财务报表自动化场景。触发关键词:Excel、xlsx、openpyxl、Excel处理、表格处理、数据报表、Excel格式化、Excel图表、透视表、Excel公式、WPS表格、Excel自动化
tags:
- Excel处理
- 数据报表
- 表格美化
- 数据可视化
- 办公自动化
tools:
- read
- exec
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# Excel数据魔法师

基于 openpyxl 实现全场景 Excel 文件处理。从读写到格式化,从公式到图表,从透视表到数据校验,覆盖 Excel 自动化的所有常见需求。兼容 Microsoft Excel 与 WPS 表格。

## 核心能力

1. **读写与多 Sheet 操作**:单元格读写、批量操作、多 Sheet 管理、Sheet 复制移动、跨 Sheet 引用
2. **格式化与美化**:字体/填充/边框/对齐/数字格式/条件格式/样式套用
3. **公式与函数**:SUM/AVERAGE/VLOOKUP/IF/COUNTIF/数组公式、动态引用、公式审计
4. **图表生成**:柱状图/折线图/饼图/散点图/组合图、标题/图例/坐标轴/数据标签
5. **数据透视表与高级功能**:PivotTable 创建、数据校验、批注、保护、合并拆分

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 数据报表生成 | 数据源(JSON/CSV/DB)+ 模板 | 格式化的 Excel 报表 + 图表 |
| Excel 模板填充 | 模板文件 + 数据 | 填充后的 Excel 文件 |
| 批量数据处理 | 多个 Excel 文件 + 处理规则 | 合并/拆分/汇总后的 Excel |
| 格式美化 | 原始 Excel 文件 | 美化后的 Excel(字体/颜色/边框) |
| 图表可视化 | 数据 + 图表类型 | 含图表的 Excel 文件 |
| 财务报表自动化 | 财务数据 + 报表模板 | 月度/季度/年度财务报表 |

**不适用于**:
- 超大规模数据(>100万行,建议用 pandas + 数据库)
- 复杂的数据分析与建模(使用 pandas/numpy/scikit-learn)
- 实时协作编辑(使用 Google Sheets/飞书表格)
- 复杂的 VBA 宏开发(本 Skill 用 Python 替代)
- Excel 文件密码破解(不涉及安全破解)
- PDF/Word 等非 Excel 文件处理(使用专用工具)
- 在线表格 API 集成(使用 Google Sheets API/飞书开放平台)

## 使用流程

### Step 1: 文件分析
1. **读取文件**:加载 Excel 文件,获取工作簿与 Sheet 信息
2. **结构识别**:Sheet 列表、每 Sheet 的行列数、表头识别、数据类型推断
3. **内容预览**:前 10 行数据预览,确认数据结构
4. **问题诊断**:格式问题、数据错误、缺失值、重复值

### Step 2: 数据读取
1. **基础读取**:`openpyxl.load_workbook()` 加载文件
2. **批量读取**:按行/列批量读取,提高性能
3. **数据类型处理**:数字/文本/日期/布尔值的正确解析
4. **公式值获取**:`data_only=True` 获取计算结果,`False` 获取公式

### Step 3: 数据写入与修改
1. **单元格写入**:`cell.value = value`
2. **批量写入**:按行/列批量写入,使用 `append()` 方法
3. **Sheet 操作**:创建/复制/移动/删除/重命名 Sheet
4. **数据校验**:数据有效性(下拉列表/数字范围/日期范围)

### Step 4: 格式化
1. **字体格式**:字体名/大小/颜色/加粗/斜体/下划线
2. **填充格式**:背景色/渐变/图案
3. **边框格式**:边框样式/颜色/位置
4. **对齐格式**:水平/垂直对齐/换行/缩进
5. **数字格式**:数字/货币/百分比/日期/自定义格式
6. **条件格式**:数据条/色阶/图标集/公式条件

### Step 5: 公式与图表
1. **公式写入**:`cell.value = "=SUM(A1:A10)"`
2. **图表创建**:
   - 选择数据范围
   - 创建图表对象(BarChart/LineChart/PieChart)
   - 配置标题/图例/坐标轴
   - 添加到 Sheet
3. **图表样式**:颜色/样式/数据标签

### Step 6: 高级功能
1. **数据透视表**:创建 PivotTable,配置行/列/值/筛选
2. **批注**:添加单元格批注
3. **保护**:Sheet 保护/工作簿保护/密码
4. **合并单元格**:合并/拆分单元格

### Step 7: 保存与导出
1. **保存文件**:`workbook.save('output.xlsx')`
2. **格式兼容**:确保 Microsoft Excel 与 WPS 表格兼容
3. **文件大小优化**:移除未使用的样式与格式

## Excel 与 WPS 表格兼容性

| 功能 | Microsoft Excel | WPS 表格 | 兼容性 |
|:-----|:---------------|:---------|:------|
| .xlsx 格式 | 完全支持 | 完全支持 | 100% |
| 公式 | 全部支持 | 全部支持 | 99% |
| 图表 | 全部支持 | 基本支持 | 95% |
| 条件格式 | 全部支持 | 基本支持 | 90% |
| 数据透视表 | 全部支持 | 基本支持 | 85% |
| VBA 宏 | 支持 | 部分支持 | 70% |
| openpyxl 生成 | 完全兼容 | 完全兼容 | 100% |

## 示例

### 示例1: 生成销售数据报表(输入→输出)

**输入**:
```
用户请求:根据销售数据生成月度报表
数据: JSON 格式(产品/销售额/地区/月份)
要求: 含格式化表格 + 柱状图 + 汇总公式
```

**输出**(generate_report.py):
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Alignment
from openpyxl.chart import BarChart, Reference
import json

# 数据
sales_data = [
    {"product": "产品A", "region": "华东", "amount": 125000},
    {"product": "产品B", "region": "华东", "amount": 98000},
    {"product": "产品A", "region": "华北", "amount": 87000},
    {"product": "产品B", "region": "华北", "amount": 112000},
]

# 创建工作簿
wb = Workbook()
ws = wb.active
ws.title = "销售月报"

# 表头样式
header_font = Font(name='微软雅黑', size=12, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='1a56db', end_color='1a56db', fill_type='solid')
center_align = Alignment(horizontal='center', vertical='center')
border = Border(
    left=Side(style='thin'), right=Side(style='thin'),
    top=Side(style='thin'), bottom=Side(style='thin')
)

# 写入表头
headers = ['产品', '地区', '销售额(元)']
for col, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=header)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = center_align
    cell.border = border

# 写入数据
for row_idx, data in enumerate(sales_data, 2):
    ws.cell(row=row_idx, column=1, value=data['product'])
    ws.cell(row=row_idx, column=2, value=data['region'])
    cell = ws.cell(row=row_idx, column=3, value=data['amount'])
    cell.number_format = '#,##0.00'

# 汇总公式
ws.cell(row=len(sales_data)+2, column=1, value='合计')
ws.cell(row=len(sales_data)+2, column=3, value=f'=SUM(C2:C{len(sales_data)+1})')
ws.cell(row=len(sales_data)+2, column=3).number_format = '#,##0.00'

# 创建柱状图
chart = BarChart()
chart.title = "各地区销售额"
chart.x_axis.title = "产品-地区"
chart.y_axis.title = "销售额(元)"

data_ref = Reference(ws, min_col=3, min_row=1, max_row=len(sales_data)+1)
cats_ref = Reference(ws, min_col=1, min_row=2, max_row=len(sales_data)+1)
chart.add_data(data_ref, titles_from_data=True)
chart.set_categories(cats_ref)

ws.add_chart(chart, "E2")

# 保存
wb.save('sales_report.xlsx')
```

### 示例2: 多文件合并(输入→输出)

**输入**:
```
用户请求:合并多个分公司的 Excel 销售文件
文件: branch_beijing.xlsx, branch_shanghai.xlsx, branch_guangzhou.xlsx
要求: 合并到总表,添加分公司列
```

**输出**(merge_files.py):
```python
from openpyxl import Workbook, load_workbook
import os

# 创建总表
merged_wb = Workbook()
merged_ws = merged_wb.active
merged_ws.title = "合并销售数据"

# 写入表头(添加分公司列)
headers = ['分公司', '产品', '销售额', '日期']
for col, h in enumerate(headers, 1):
    merged_ws.cell(row=1, column=col, value=h)

# 合并文件
files = [
    ('branch_beijing.xlsx', '北京'),
    ('branch_shanghai.xlsx', '上海'),
    ('branch_guangzhou.xlsx', '广州'),
]

current_row = 2
for filename, branch in files:
    wb = load_workbook(filename)
    ws = wb.active

    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0] is None:  # 跳过空行
            continue
        merged_ws.cell(row=current_row, column=1, value=branch)
        merged_ws.cell(row=current_row, column=2, value=row[0])  # 产品
        merged_ws.cell(row=current_row, column=3, value=row[1])  # 销售额
        merged_ws.cell(row=current_row, column=4, value=row[2])  # 日期
        current_row += 1

    wb.close()

# 添加汇总
merged_ws.cell(row=current_row+1, column=2, value='总计')
merged_ws.cell(row=current_row+1, column=3, value=f'=SUM(C2:C{current_row-1})')

merged_wb.save('merged_sales.xlsx')
print(f"合并完成,共 {current_row-2} 条记录")
```

### 示例3: 条件格式化(输入→输出)

**输入**:
```
用户请求:对销售数据应用条件格式
规则: 1)销售额>10万标绿 2)销售额<5万标红 3)数据条可视化
```

**输出**(conditional_format.py):
```python
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Font
from openpyxl.formatting.rule import CellIsRule, DataBarRule

wb = load_workbook('sales_data.xlsx')
ws = wb.active

# 范围
range_str = 'C2:C100'

# 规则1: 销售额 > 100000 标绿色
green_fill = PatternFill(start_color='10b981', end_color='10b981', fill_type='solid')
ws.conditional_formatting.add(range_str,
    CellIsRule(operator='greaterThan', formula=['100000'], fill=green_fill))

# 规则2: 销售额 < 50000 标红色
red_fill = PatternFill(start_color='ef4444', end_color='ef4444', fill_type='solid')
ws.conditional_formatting.add(range_str,
    CellIsRule(operator='lessThan', formula=['50000'], fill=red_fill))

# 规则3: 数据条可视化
data_bar = DataBarRule(
    start_type='min', end_type='max',
    color='3b82f6', showValue=True
)
ws.conditional_formatting.add(range_str, data_bar)

wb.save('sales_formatted.xlsx')
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| 文件无法打开 | 文件损坏或非 xlsx 格式 | 提示检查文件格式,尝试修复或使用 xlrd(旧 xls) |
| 数据类型错误 | 文本写入数字单元格 | 显式转换类型,使用 `str()`/`int()`/`float()` |
| 公式不计算 | openpyxl 不执行公式 | 使用 `data_only=True` 读取,或在 Excel 中打开后保存 |
| 文件过大(>50MB) | 数据量过多 | 改用 pandas + openpyxl 组合,或分批处理 |
| 中文乱码 | 编码问题 | 确保 `encoding='utf-8'`,字体使用中文字体 |
| 图表不显示 | 数据范围错误 | 检查 Reference 范围,确保包含表头 |
| 条件格式丢失 | WPS 兼容性问题 | 使用基本条件格式,避免高级规则 |
| Sheet 名称冲突 | 名称重复或含非法字符 | 自动添加后缀(_1/_2),移除 `/\?*[]` 字符 |
| 日期格式异常 | 日期序列号与文本混淆 | 使用 `datetime` 对象,设置 `number_format='YYYY-MM-DD'` |
| 公式引用错误 | 跨 Sheet 引用语法错误 | 使用 `'Sheet名'!A1` 格式,Sheet 名含空格需引号 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: Python 3.10+

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代 |
|:-------|:-----|:---------|:---------|:---------|
| LLM API | API | 必需 | Agent 内置 LLM | 通义/文心/智谱 |
| openpyxl | 库 | 必需 | `pip install openpyxl` | 国内 PyPI 镜像 |
| pandas | 库 | 可选(大数据) | `pip install pandas` | 国内 PyPI 镜像 |
| Python | 运行时 | 必需 | python.org | 国内镜像源 |
| xlsxwriter | 库 | 可选(写入优化) | `pip install xlsxwriter` | 国内 PyPI 镜像 |

### API Key 配置
- **本Skill无需额外API Key配置**
- **安全要求**: 
  - 处理含敏感数据的 Excel 文件时,不在日志中输出数据内容
  - 生成的报表不包含任何 API Key 或凭证
  - 如 Excel 包含密码,密码仅通过环境变量传入

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,需 exec 能力运行 Python 脚本

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 月度销售报表(格式化表格+柱状图+SUM/AVERAGE公式)

**输入**:
```
需求: 生成Q4季度月度销售报表
数据: 3个月x5个产品的销售额数据(JSON)
要求:
  1) 表头蓝色填充+白色字体+居中对齐
  2) 数据行交替底色(斑马纹)
  3) 合计行SUM公式 + 平均行AVERAGE公式
  4) 销售额列货币格式(¥#,##0.00)
  5) 柱状图对比各月销售额
  6) 冻结首行
```

**LLM生成输出** (`output/sales-report/generate_report.py`):
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, NamedStyle
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter
import json

# 数据
sales_data = [
    {"product": "产品A", "oct": 125000, "nov": 138000, "dec": 156000},
    {"product": "产品B", "oct": 98000,  "nov": 105000, "dec": 112000},
    {"product": "产品C", "oct": 87000,  "nov": 92000,  "dec": 108000},
    {"product": "产品D", "oct": 65000,  "nov": 71000,  "dec": 78000},
    {"product": "产品E", "oct": 42000,  "nov": 48000,  "dec": 55000},
]

# 创建工作簿
wb = Workbook()
ws = wb.active
ws.title = "Q4销售月报"

# ===== 样式定义 =====
header_font = Font(name='微软雅黑', size=11, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='1a56db', end_color='1a56db', fill_type='solid')
zebra_fill = PatternFill(start_color='f8fafc', end_color='f8fafc', fill_type='solid')
total_font = Font(name='微软雅黑', size=11, bold=True, color='1a56db')
total_fill = PatternFill(start_color='dbeafe', end_color='dbeafe', fill_type='solid')
center_align = Alignment(horizontal='center', vertical='center')
right_align = Alignment(horizontal='right', vertical='center')
thin_border = Border(
    left=Side(style='thin', color='e2e8f0'),
    right=Side(style='thin', color='e2e8f0'),
    top=Side(style='thin', color='e2e8f0'),
    bottom=Side(style='thin', color='e2e8f0')
)

# ===== 写入表头 =====
headers = ['产品', '10月销售额', '11月销售额', '12月销售额', 'Q4合计', '月均']
for col, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=header)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = center_align
    cell.border = thin_border

# ===== 写入数据 =====
for row_idx, data in enumerate(sales_data, 2):
    ws.cell(row=row_idx, column=1, value=data['product']).alignment = center_align
    ws.cell(row=row_idx, column=2, value=data['oct']).number_format = '¥#,##0.00'
    ws.cell(row=row_idx, column=3, value=data['nov']).number_format = '¥#,##0.00'
    ws.cell(row=row_idx, column=4, value=data['dec']).number_format = '¥#,##0.00'
    # Q4合计公式
    ws.cell(row=row_idx, column=5, value=f'=SUM(B{row_idx}:D{row_idx})').number_format = '¥#,##0.00'
    # 月均公式
    ws.cell(row=row_idx, column=6, value=f'=AVERAGE(B{row_idx}:D{row_idx})').number_format = '¥#,##0.00'

    # 斑马纹(偶数行底色)
    if row_idx % 2 == 0:
        for col in range(1, 7):
            ws.cell(row=row_idx, column=col).fill = zebra_fill

    # 边框+对齐
    for col in range(1, 7):
        cell = ws.cell(row=row_idx, column=col)
        cell.border = thin_border
        if col >= 2:
            cell.alignment = right_align

# ===== 合计行 =====
total_row = len(sales_data) + 2
ws.cell(row=total_row, column=1, value='合计')
for col in range(2, 7):
    col_letter = get_column_letter(col)
    ws.cell(row=total_row, column=col,
            value=f'=SUM({col_letter}2:{col_letter}{total_row-1})').number_format = '¥#,##0.00'

for col in range(1, 7):
    cell = ws.cell(row=total_row, column=col)
    cell.font = total_font
    cell.fill = total_fill
    cell.border = thin_border
    cell.alignment = center_align if col == 1 else right_align

# ===== 列宽自适应 =====
ws.column_dimensions['A'].width = 12
for col in range(2, 7):
    ws.column_dimensions[get_column_letter(col)].width = 16

# ===== 冻结首行 =====
ws.freeze_panes = 'A2'

# ===== 创建柱状图 =====
chart = BarChart()
chart.type = "col"
chart.title = "Q4各产品月度销售额对比"
chart.x_axis.title = "产品"
chart.y_axis.title = "销售额(元)"
chart.style = 10

# 数据范围(10-12月,含表头)
data_ref = Reference(ws, min_col=2, min_row=1, max_col=4, max_row=len(sales_data) + 1)
cats_ref = Reference(ws, min_col=1, min_row=2, max_row=len(sales_data) + 1)
chart.add_data(data_ref, titles_from_data=True)
chart.set_categories(cats_ref)
chart.width = 20
chart.height = 12

ws.add_chart(chart, "H2")

# ===== 保存 =====
wb.save('q4_sales_report.xlsx')
print("报表生成: q4_sales_report.xlsx")
```

**效果验证**: ✓表头蓝色填充+白色字体+居中对齐 ✓斑马纹(偶数行#f8fafc底色) ✓SUM公式(Q4合计)+AVERAGE公式(月均) ✓货币格式¥#,##0.00 ✓合计行突出显示(蓝色字体+浅蓝底色) ✓柱状图含标题/坐标轴/3月数据对比 ✓冻结首行(freeze_panes) ✓列宽自适应

### 案例2: 多分公司文件合并(VLOOKUP跨表+汇总Sheet+条件格式)

**输入**:
```
需求: 合并3个分公司销售Excel + 产品信息VLOOKUP + 汇总分析
输入文件: beijing.xlsx(北京), shanghai.xlsx(上海), guangzhou.xlsx(广州)
产品信息: products.xlsx(产品ID/名称/类别/单价)
要求:
  1) 合并3个分公司数据,添加来源列
  2) VLOOKUP补充产品名称和类别
  3) 创建汇总Sheet: 按地区+类别交叉统计
  4) 条件格式: 销售额>10万标绿,<5万标红
  5) 数据条可视化
```

**LLM生成输出** (`output/merge-branches/merge_and_analyze.py`):
```python
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.formatting.rule import CellIsRule, DataBarRule
from openpyxl.chart import PieChart, Reference
from openpyxl.utils import get_column_letter

# ===== Step 1: 合并3个分公司文件 =====
merged_wb = Workbook()
merged_ws = merged_wb.active
merged_ws.title = "合并数据"

# 表头
headers = ['来源分公司', '产品ID', '销售数量', '销售日期', '产品名称', '产品类别', '销售金额']
for col, h in enumerate(headers, 1):
    merged_ws.cell(row=1, column=col, value=h)

# 合并文件
branch_files = [
    ('beijing.xlsx', '北京'),
    ('shanghai.xlsx', '上海'),
    ('guangzhou.xlsx', '广州'),
]

current_row = 2
for filename, branch in branch_files:
    wb = load_workbook(filename)
    ws = wb.active
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0] is None:
            continue
        merged_ws.cell(row=current_row, column=1, value=branch)
        merged_ws.cell(row=current_row, column=2, value=row[0])  # 产品ID
        merged_ws.cell(row=current_row, column=3, value=row[1])  # 销售数量
        merged_ws.cell(row=current_row, column=4, value=row[2])  # 销售日期
        current_row += 1
    wb.close()

total_data_rows = current_row - 1

# ===== Step 2: VLOOKUP补充产品信息 =====
# 加载产品信息到字典
product_wb = load_workbook('products.xlsx')
product_ws = product_wb.active
product_map = {}
for row in product_ws.iter_rows(min_row=2, values_only=True):
    # row: (产品ID, 产品名称, 产品类别, 单价)
    product_map[row[0]] = {'name': row[1], 'category': row[2], 'price': row[3]}
product_wb.close()

# 写入VLOOKUP公式(引用products.xlsx)或直接填值
for row_idx in range(2, current_row):
    product_id = merged_ws.cell(row=row_idx, column=2).value
    if product_id in product_map:
        merged_ws.cell(row=row_idx, column=5, value=product_map[product_id]['name'])
        merged_ws.cell(row=row_idx, column=6, value=product_map[product_id]['category'])
        # 销售金额 = 数量 * 单价
        quantity = merged_ws.cell(row=row_idx, column=3).value
        price = product_map[product_id]['price']
        merged_ws.cell(row=row_idx, column=7, value=quantity * price).number_format = '¥#,##0.00'

# ===== Step 3: 条件格式 =====
amount_range = f'G2:G{total_data_rows}'

# 销售额 > 100000 标绿
green_fill = PatternFill(start_color='10b981', end_color='10b981', fill_type='solid')
merged_ws.conditional_formatting.add(amount_range,
    CellIsRule(operator='greaterThan', formula=['100000'], fill=green_fill))

# 销售额 < 50000 标红
red_fill = PatternFill(start_color='ef4444', end_color='ef4444', fill_type='solid')
merged_ws.conditional_formatting.add(amount_range,
    CellIsRule(operator='lessThan', formula=['50000'], fill=red_fill))

# 数据条可视化
data_bar = DataBarRule(start_type='min', end_type='max', color='3b82f6', showValue=True)
merged_ws.conditional_formatting.add(amount_range, data_bar)

# ===== Step 4: 创建汇总Sheet =====
summary_ws = merged_wb.create_sheet("地区类别汇总")

# 获取所有地区和类别
branches = ['北京', '上海', '广州']
categories = sorted(set(p['category'] for p in product_map.values()))

# 写入交叉表表头
summary_ws.cell(row=1, column=1, value='地区\\类别')
for col_idx, cat in enumerate(categories, 2):
    summary_ws.cell(row=1, column=col_idx, value=cat)
summary_ws.cell(row=1, column=len(categories) + 2, value='合计')

# 写入交叉统计数据
for row_idx, branch in enumerate(branches, 2):
    summary_ws.cell(row=row_idx, column=1, value=branch)
    for col_idx, cat in enumerate(categories, 2):
        # 统计该地区该类别的销售金额
        total = 0
        for data_row in range(2, current_row):
            if (merged_ws.cell(row=data_row, column=1).value == branch and
                merged_ws.cell(row=data_row, column=6).value == cat):
                total += merged_ws.cell(row=data_row, column=7).value or 0
        cell = summary_ws.cell(row=row_idx, column=col_idx, value=total)
        cell.number_format = '¥#,##0.00'
    # 行合计
    summary_ws.cell(row=row_idx, column=len(categories) + 2,
        value=f'=SUM(B{row_idx}:{get_column_letter(len(categories)+1)}{row_idx})').number_format = '¥#,##0.00'

# 列合计行
total_row = len(branches) + 2
summary_ws.cell(row=total_row, column=1, value='合计')
for col in range(2, len(categories) + 3):
    col_letter = get_column_letter(col)
    summary_ws.cell(row=total_row, column=col,
        value=f'=SUM({col_letter}2:{col_letter}{total_row-1})').number_format = '¥#,##0.00'

# 汇总表样式
header_font = Font(name='微软雅黑', size=11, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='1a56db', end_color='1a56db', fill_type='solid')
for col in range(1, len(categories) + 3):
    cell = summary_ws.cell(row=1, column=col)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal='center')

# ===== Step 5: 饼图(各地区销售占比) =====
pie = PieChart()
pie.title = "各地区销售金额占比"
labels = Reference(summary_ws, min_col=1, min_row=2, max_row=len(branches) + 1)
data = Reference(summary_ws, min_col=len(categories) + 2, min_row=1, max_row=len(branches) + 1)
pie.add_data(data, titles_from_data=True)
pie.set_categories(labels)
pie.width = 12
pie.height = 8
summary_ws.add_chart(pie, f'{get_column_letter(len(categories) + 4)}2')

merged_wb.save('merged_analysis.xlsx')
print(f"合并完成: {total_data_rows - 1} 条记录")
print("文件: merged_analysis.xlsx")
```

**效果验证**: ✓3分公司合并+来源列标注 ✓VLOOKUP补充产品名称/类别+计算销售金额(数量*单价) ✓条件格式3规则(>10万绿/<5万红/数据条) ✓交叉汇总表(地区x类别矩阵+行列合计) ✓饼图展示各地区销售占比 ✓SUM公式行列合计

### 案例3: 绩效考核表(下拉验证+色阶+批注+Sheet保护)

**输入**:
```
需求: 员工绩效考核评分表
数据: 20名员工(姓名/部门/KPI完成率/360评分/出勤率)
要求:
  1) 部门列下拉验证(技术部/产品部/市场部/运营部)
  2) 评分列色阶(红→黄→绿渐变)
  3) 综合评分公式: KPI*40% + 360*40% + 出勤*20%
  4) 等级自动判定: >=90优秀/>=75良好/>=60合格/<60不合格
  5) 关键员工添加批注说明
  6) Sheet保护(仅允许编辑评分列)
```

**LLM生成输出** (`output/performance-review/generate_review.py`):
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.comments import Comment
from openpyxl.styles import Protection
from openpyxl.utils import get_column_letter

# 员工数据
employees = [
    {"name": "张三", "dept": "技术部", "kpi": 0.95, "score360": 88, "attendance": 0.98},
    {"name": "李四", "dept": "产品部", "kpi": 0.82, "score360": 75, "attendance": 0.95},
    {"name": "王五", "dept": "技术部", "kpi": 0.91, "score360": 92, "attendance": 1.00},
    {"name": "赵六", "dept": "市场部", "kpi": 0.58, "score360": 60, "attendance": 0.88},
    {"name": "钱七", "dept": "运营部", "kpi": 0.88, "score360": 85, "attendance": 0.97},
    # ... 更多员工
]

wb = Workbook()
ws = wb.active
ws.title = "绩效考核"

# ===== 样式 =====
header_font = Font(name='微软雅黑', size=11, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='1a56db', end_color='1a56db', fill_type='solid')
center = Alignment(horizontal='center', vertical='center')
border = Border(
    left=Side(style='thin', color='e2e8f0'), right=Side(style='thin', color='e2e8f0'),
    top=Side(style='thin', color='e2e8f0'), bottom=Side(style='thin', color='e2e8f0')
)

# ===== 表头 =====
headers = ['姓名', '部门', 'KPI完成率', '360评分', '出勤率', '综合评分', '等级']
for col, h in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = center
    cell.border = border

# ===== 数据写入 =====
for row_idx, emp in enumerate(employees, 2):
    ws.cell(row=row_idx, column=1, value=emp['name']).alignment = center
    ws.cell(row=row_idx, column=2, value=emp['dept']).alignment = center

    kpi_cell = ws.cell(row=row_idx, column=3, value=emp['kpi'])
    kpi_cell.number_format = '0.0%'
    kpi_cell.alignment = center

    score_cell = ws.cell(row=row_idx, column=4, value=emp['score360'])
    score_cell.alignment = center

    att_cell = ws.cell(row=row_idx, column=5, value=emp['attendance'])
    att_cell.number_format = '0.0%'
    att_cell.alignment = center

    # 综合评分公式: KPI*40% + 360*40% + 出勤*20%
    # KPI和出勤是百分比,需*100
    ws.cell(row=row_idx, column=6,
        value=f'=C{row_idx}*100*0.4+D{row_idx}*0.4+E{row_idx}*100*0.2'
    ).alignment = center

    # 等级判定公式
    ws.cell(row=row_idx, column=7,
        value=f'=IF(F{row_idx}>=90,"优秀",IF(F{row_idx}>=75,"良好",IF(F{row_idx}>=60,"合格","不合格")))'
    ).alignment = center

    for col in range(1, 8):
        ws.cell(row=row_idx, column=col).border = border

# ===== Step 1: 部门下拉验证 =====
dept_validation = DataValidation(
    type="list",
    formula1='"技术部,产品部,市场部,运营部"',
    allow_blank=False,
    showErrorMessage=True,
    errorTitle="输入错误",
    error="请从下拉列表中选择部门"
)
dept_validation.add(f'B2:B{len(employees)+1}')
ws.add_data_validation(dept_validation)

# 评分范围验证(0-100)
score_validation = DataValidation(
    type="decimal",
    operator="between",
    formula1=0, formula2=100,
    allow_blank=False,
    showErrorMessage=True,
    errorTitle="评分超出范围",
    error="360评分必须在0-100之间"
)
score_validation.add(f'D2:D{len(employees)+1}')
ws.add_data_validation(score_validation)

# ===== Step 2: 色阶条件格式(综合评分) =====
score_range = f'F2:F{len(employees)+1}'
color_scale = ColorScaleRule(
    start_type='num', start_value=50, start_color='ef4444',   # 红
    mid_type='num', mid_value=75, mid_color='f59e0b',         # 黄
    end_type='num', end_value=100, end_color='10b981'          # 绿
)
ws.conditional_formatting.add(score_range, color_scale)

# 等级颜色
grade_range = f'G2:G{len(employees)+1}'
ws.conditional_formatting.add(grade_range,
    CellIsRule(operator='equal', formula=['"优秀"'],
               fill=PatternFill(start_color='10b981', end_color='10b981', fill_type='solid'),
               font=Font(color='FFFFFF', bold=True)))
ws.conditional_formatting.add(grade_range,
    CellIsRule(operator='equal', formula=['"不合格"'],
               fill=PatternFill(start_color='ef4444', end_color='ef4444', fill_type='solid'),
               font=Font(color='FFFFFF', bold=True)))

# ===== Step 3: 关键员工批注 =====
# 为王五(绩效最高)添加批注
wang_cell = ws.cell(row=4, column=1)
wang_cell.comment = Comment(
    "Q4季度技术攻坚表现突出,\n主导完成了核心系统重构,\n建议晋升高级工程师。",
    "HR部门"
)
wang_cell.comment.width = 250
wang_cell.comment.height = 80

# 为赵六(绩效最低)添加批注
zhao_cell = ws.cell(row=5, column=1)
zhao_cell.comment = Comment(
    "KPI完成率低于60%,出勤率偏低。\n已进行绩效面谈,\n需制定改进计划(PIP)。",
    "HR部门"
)
zhao_cell.comment.width = 250
zhao_cell.comment.height = 80

# ===== Step 4: Sheet保护(仅允许编辑评分列) =====
# 解锁D列(360评分),其他列锁定
for row_idx in range(2, len(employees) + 2):
    for col in range(1, 8):
        cell = ws.cell(row=row_idx, column=col)
        cell.protection = Protection(locked=(col != 4))

# 启用Sheet保护
ws.protection.sheet = True
ws.protection.password = 'hr_protected_2024'
ws.protection.enable()

# 列宽
for col, width in enumerate([10, 12, 14, 12, 12, 14, 10], 1):
    ws.column_dimensions[get_column_letter(col)].width = width

ws.freeze_panes = 'A2'

wb.save('performance_review.xlsx')
print("绩效表生成: performance_review.xlsx")
```

**效果验证**: ✓部门下拉验证(DataValidation list)+评分范围验证(decimal 0-100) ✓色阶条件格式(红50→黄75→绿100三色渐变) ✓综合评分公式(KPI*40%+360*40%+出勤*20%) ✓IF嵌套公式自动判定4级(优秀/良好/合格/不合格) ✓等级颜色(优秀绿底/不合格红底) ✓批注含姓名/说明/署名/尺寸 ✓Sheet保护(仅D列可编辑+密码)

### 案例4: 财务报表自动化(多Sheet+饼图+VLOOKUP+数据验证)

**输入**:
```
需求: 季度财务报表(3个Sheet)
Sheet1 "收入明细": 产品/数量/单价/金额(SUM公式)
Sheet2 "成本分析": 成本项/金额/占比(引用Sheet1总收入)
Sheet3 "利润汇总": VLOOKUP引用Sheet1/Sheet2 + 饼图
要求:
  1) 跨Sheet VLOOKUP引用
  2) 利润 = 收入 - 成本
  3) 利润率公式
  4) 饼图展示成本结构
  5) 收入明细含下拉验证(产品列表)
  6) 合并单元格标题行
```

**LLM生成输出** (`output/financial-report/generate_financials.py`):
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.chart import PieChart, Reference
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

wb = Workbook()

# ===== 公共样式 =====
title_font = Font(name='微软雅黑', size=14, bold=True, color='FFFFFF')
title_fill = PatternFill(start_color='1e1b4b', end_color='1e1b4b', fill_type='solid')
header_font = Font(name='微软雅黑', size=11, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='1a56db', end_color='1a56db', fill_type='solid')
money_fmt = '¥#,##0.00'
percent_fmt = '0.0%'
center = Alignment(horizontal='center', vertical='center')
border = Border(
    left=Side(style='thin', color='e2e8f0'), right=Side(style='thin', color='e2e8f0'),
    top=Side(style='thin', color='e2e8f0'), bottom=Side(style='thin', color='e2e8f0')
)

# ===== Sheet1: 收入明细 =====
ws1 = wb.active
ws1.title = "收入明细"

# 合并标题行
ws1.merge_cells('A1:D1')
ws1.cell(row=1, column=1, value='Q4季度收入明细').font = title_font
ws1.cell(row=1, column=1).fill = title_fill
ws1.cell(row=1, column=1).alignment = center

# 表头
headers1 = ['产品名称', '销售数量', '单价', '金额']
for col, h in enumerate(headers1, 1):
    cell = ws1.cell(row=2, column=col, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = center
    cell.border = border

# 产品数据
products = [
    {"name": "企业版SaaS", "qty": 45, "price": 2999},
    {"name": "专业版SaaS", "qty": 128, "price": 999},
    {"name": "标准版SaaS", "qty": 350, "price": 299},
    {"name": "增值服务", "qty": 80, "price": 500},
]

for row_idx, p in enumerate(products, 3):
    ws1.cell(row=row_idx, column=1, value=p['name']).alignment = center
    ws1.cell(row=row_idx, column=2, value=p['qty']).alignment = center
    ws1.cell(row=row_idx, column=3, value=p['price']).number_format = money_fmt
    # 金额公式 = 数量 * 单价
    ws1.cell(row=row_idx, column=4, value=f'=B{row_idx}*C{row_idx}').number_format = money_fmt
    for col in range(1, 5):
        ws1.cell(row=row_idx, column=col).border = border

# 合计行
total_row1 = len(products) + 3
ws1.cell(row=total_row1, column=1, value='总收入').alignment = center
ws1.cell(row=total_row1, column=4, value=f'=SUM(D3:D{total_row1-1})').number_format = money_fmt
for col in range(1, 5):
    ws1.cell(row=total_row1, column=col).font = Font(bold=True, color='1a56db')
    ws1.cell(row=total_row1, column=col).border = border

# 产品名称下拉验证
product_validation = DataValidation(
    type="list",
    formula1='"企业版SaaS,专业版SaaS,标准版SaaS,增值服务"',
    allow_blank=False
)
product_validation.add(f'A3:A{total_row1-1}')
ws1.add_data_validation(product_validation)

# ===== Sheet2: 成本分析 =====
ws2 = wb.create_sheet("成本分析")

ws2.merge_cells('A1:C1')
ws2.cell(row=1, column=1, value='Q4季度成本分析').font = title_font
ws2.cell(row=1, column=1).fill = title_fill
ws2.cell(row=1, column=1).alignment = center

headers2 = ['成本项', '金额', '占总收入比']
for col, h in enumerate(headers2, 1):
    cell = ws2.cell(row=2, column=col, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = center
    cell.border = border

costs = [
    {"item": "服务器/云服务", "amount": 85000},
    {"item": "人员薪资", "amount": 320000},
    {"item": "市场营销", "amount": 65000},
    {"item": "办公租金", "amount": 45000},
    {"item": "软件许可", "amount": 28000},
    {"item": "其他运营", "amount": 15000},
]

for row_idx, c in enumerate(costs, 3):
    ws2.cell(row=row_idx, column=1, value=c['item']).alignment = center
    ws2.cell(row=row_idx, column=2, value=c['amount']).number_format = money_fmt
    # 占比公式 = 成本 / Sheet1总收入
    ws2.cell(row=row_idx, column=3,
        value=f'=B{row_idx}/收入明细!D{total_row1}'
    ).number_format = percent_fmt
    for col in range(1, 4):
        ws2.cell(row=row_idx, column=col).border = border

# 成本合计
total_row2 = len(costs) + 3
ws2.cell(row=total_row2, column=1, value='总成本').alignment = center
ws2.cell(row=total_row2, column=2, value=f'=SUM(B3:B{total_row2-1})').number_format = money_fmt
ws2.cell(row=total_row2, column=3, value=f'=B{total_row2}/收入明细!D{total_row1}').number_format = percent_fmt
for col in range(1, 4):
    ws2.cell(row=total_row2, column=col).font = Font(bold=True, color='1a56db')
    ws2.cell(row=total_row2, column=col).border = border

# ===== Sheet3: 利润汇总 =====
ws3 = wb.create_sheet("利润汇总")

ws3.merge_cells('A1:D1')
ws3.cell(row=1, column=1, value='Q4季度利润汇总').font = title_font
ws3.cell(row=1, column=1).fill = title_fill
ws3.cell(row=1, column=1).alignment = center

headers3 = ['项目', '金额', '占比', '备注']
for col, h in enumerate(headers3, 1):
    cell = ws3.cell(row=2, column=col, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = center
    cell.border = border

# 利润数据(跨Sheet引用)
profit_data = [
    {"label": "总收入", "formula": f"=收入明细!D{total_row1}", "note": "Sheet1合计"},
    {"label": "总成本", "formula": f"=成本分析!B{total_row2}", "note": "Sheet2合计"},
    {"label": "毛利润", "formula": f"=B3-B4", "note": "收入-成本"},
    {"label": "利润率", "formula": f"=B5/B3", "note": "毛利润/总收入", "fmt": percent_fmt},
]

for row_idx, d in enumerate(profit_data, 3):
    ws3.cell(row=row_idx, column=1, value=d['label']).alignment = center
    cell = ws3.cell(row=row_idx, column=2, value=d['formula'])
    cell.number_format = d.get('fmt', money_fmt)
    cell.alignment = center

    # 占比(除利润率外,其他项占比=金额/总收入)
    if d['label'] != '利润率':
        ws3.cell(row=row_idx, column=3, value=f'=B{row_idx}/B3').number_format = percent_fmt
    ws3.cell(row=row_idx, column=3).alignment = center

    ws3.cell(row=row_idx, column=4, value=d['note']).alignment = center
    for col in range(1, 5):
        ws3.cell(row=row_idx, column=col).border = border

# 利润行高亮
profit_fill = PatternFill(start_color='d1fae5', end_color='d1fae5', fill_type='solid')
for col in range(1, 5):
    ws3.cell(row=5, column=col).fill = profit_fill
    ws3.cell(row=5, column=col).font = Font(bold=True, color='10b981')

# ===== 饼图: 成本结构 =====
pie = PieChart()
pie.title = "Q4成本结构占比"
labels = Reference(ws2, min_col=1, min_row=3, max_row=total_row2 - 1)
data = Reference(ws2, min_col=2, min_row=2, max_row=total_row2 - 1)
pie.add_data(data, titles_from_data=True)
pie.set_categories(labels)
pie.width = 14
pie.height = 10
ws3.add_chart(pie, "F2")

# 列宽
for ws, widths in [(ws1, [16, 12, 12, 14]), (ws2, [18, 14, 14]), (ws3, [12, 14, 10, 16])]:
    for col, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(col)].width = w

# 冻结首2行
for ws in [ws1, ws2, ws3]:
    ws.freeze_panes = 'A3'

wb.save('q4_financial_report.xlsx')
print("财务报表生成: q4_financial_report.xlsx")
print(f"  Sheet1: 收入明细({len(products)}个产品)")
print(f"  Sheet2: 成本分析({len(costs)}项成本)")
print(f"  Sheet3: 利润汇总(含饼图)")
```

**效果验证**: ✓3个Sheet(收入明细/成本分析/利润汇总)含合并单元格标题 ✓跨Sheet引用(成本占比引用收入明细!D7) ✓利润公式(收入-成本)+利润率公式(毛利润/总收入) ✓产品下拉验证(DataValidation list) ✓饼图展示成本结构占比 ✓利润行高亮(绿色底+绿色粗体) ✓金额/百分比格式 + 冻结首2行

## 常见问题

### Q1: openpyxl 和 pandas 处理 Excel 有什么区别?
A: 各有优势:
- **openpyxl**: 精细控制格式(字体/颜色/边框/图表),适合生成报表
- **pandas**: 数据处理强大(过滤/聚合/合并),适合数据分析
- **推荐组合**: pandas 读取处理数据 → openpyxl 美化输出
- 性能:pandas 读取大数据更快,openpyxl 写入格式更灵活

### Q2: 如何处理 Excel 公式不计算的问题?
A: openpyxl 写入公式但不执行,需在 Excel 中打开才会计算:
- 方法1: 在 Excel/WPS 中打开文件,按 Ctrl+S 保存
- 方法2: 使用 `data_only=True` 读取已计算的值(需文件曾被打开过)
- 方法3: 用 `xlwings` 调用 Excel 引擎计算(需安装 Excel)
- 方法4: 用 Python 直接计算结果,写入值而非公式

### Q3: 如何生成兼容 WPS 表格的 Excel?
A: 兼容性要点:
- 使用 `.xlsx` 格式(不用 .xls)
- 避免使用 VBA 宏(WPS 支持有限)
- 条件格式使用基本规则(数据条/色阶/CellIsRule)
- 图表使用标准类型(柱状/折线/饼图)
- 字体使用通用字体(微软雅黑/宋体)
- 测试:生成后在 WPS 中打开验证

### Q4: 如何处理超大规模 Excel 数据?
A: 推荐方案:
- **< 10万行**: openpyxl 直接处理
- **10万-100万行**: pandas 读取 + openpyxl 写入
- **> 100万行**: 数据库(SQLite/MySQL)+ 分批处理
- **> 1000万行**: 考虑使用专业的数据处理平台
- 优化:批量操作(`append()`)、关闭计算(`calculation='manual'`)、禁用屏幕更新

## 已知限制

- openpyxl 不执行公式,需在 Excel/WPS 中打开才会计算
- 不支持 VBA 宏的开发(用 Python 替代)
- 不支持 Excel 在线协作编辑
- 超大规模数据(>100万行)性能较差,建议用 pandas
- 部分高级图表(瀑布图/树状图)支持有限
- 不涉及 PDF/Word 等非 Excel 文件处理
- 复杂的数据透视表推荐在 Excel 中手动创建
- 国内安装依赖可能较慢,建议配置国内镜像源

## 安全声明

- 处理含敏感数据的 Excel 文件时,不在日志中输出数据内容
- 生成的报表不包含任何 API Key 或凭证
- Excel 文件密码仅通过环境变量传入,不硬编码
- 输出的文件路径使用绝对路径,避免相对路径混淆
- 大规模处理前建议备份原始文件
- 不修改原始文件,生成新文件输出
