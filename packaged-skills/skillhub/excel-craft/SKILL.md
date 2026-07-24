---
slug: "excel-craft"
name: "excel-craft"
version: 1.0.1
displayName: "Excel工艺专业版"
summary: "企业级 Excel 生成引擎，含批量处理、条件格式、高级图表、模板系统与数据源对接。。Excel 工艺专业版在免费版基础上扩展批量生成、多文件合并拆分、条件格式与数据验证、高级图表、模板系统"
license: "Proprietary"
edition: "pro"
description: |-
  Excel 工艺专业版在免费版基础上扩展批量生成、多文件合并拆分、条件格式与数据验证、高级图表、模板系统与数据源对接能力。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解.
tags:
  - 集成工具
  - 表格生成
  - 企业级
  - 自动化
  - 工具
  - 效率
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# Excel工艺专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Excel工艺专业版含批量处理 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 核心能力

### 错误恢复步骤
| 错误场景 | 原因 | 处理方式 |
|:-----|:-----|:-----|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
### 错误场景

针对错误场景,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供错误场景相关的配置参数、输入数据和处理选项.
**输出**: 返回错误场景的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`错误场景`的配置文档进行参数调优
### LLM响应超时或无响应

针对LLM响应超时或无响应,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供LLM响应超时或无响应相关的配置参数、输入数据和处理选项.
**输出**: 返回LLM响应超时或无响应的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`LLM响应超时或无响应`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 已知限制
- 多 Sheet 工作簿生成
- 基础格式化（字体 / 填充 / 边框 / 对齐）
- 公式支持
- 基础图表（柱状 / 折线 / 饼图）
- 自动列宽与合并单元格

### 专业版新增能力
| 能力模块 | 输入 | 输出 | 适用场景 |
|---:|---:|---:|---:|
| 批量生成 | 数据数组 + 模板 | 多份 .xlsx | 月度报告 |
| 文件合并 | 多文件列表 | 单个汇总文件 | 分公司整合 |
| 文件拆分 | 大文件 + 拆分键 | 多份小文件 | 按区域分发 |
| 条件格式 | 规则定义 | 高亮 / 色阶 / 图标集 | 数据可视化 |
| 数据验证 | 验证规则 | 下拉 / 范围限制 | 录入规范 |
| 高级图表 | 数据 + 类型 | 散点 / 瀑布 / 组合图 | 深度分析 |
| 模板系统 | 模板 + 变量 | 渲染后文件 | 重复报告 |
| 数据源对接 | 连接配置 | 数据抽取 | 数据库集成 |
| 保护规则 | 区域 + 密码 | 锁定 / 隐藏 | 防误改 |

## 适用场景

### 场景一：月度报告批量生成（运营角色）
按分公司生成 30 份月度报告。专业版通过模板系统定义一份模板，注入各分公司数据批量生成，相比手工快 50 倍.
### 场景二：多文件合并汇总（财务角色）
30 个分公司上传各自 Excel，需汇总到一份主报告。专业版提供合并脚本——按 Sheet 名匹配、按字段对齐、合并后做总计与差异校验.
### 场景三：数据库抽取报表（数据角色）
从 `PostgreSQL` 抽取销售数据，按区域分 Sheet 生成报告。专业版提供完整数据抽取 → 清洗 → 生成 → 邮件分发流水线.
### 场景四：条件格式仪表盘（管理层角色）
KPI 表格中业绩低于目标红色、达标绿色、超额蓝色。专业版提供色阶、图标集、数据条三种条件格式，配合保护规则防止误改.
### 场景五：跨平台分发（IT 角色）
同一报告需在 Excel / WPS / LibreOffice 三个平台打开。专业版提供深度格式优化策略，针对各平台特性调整.
### 场景六：模板系统复用（产品角色）
周报、月报、季报共享一份模板，仅变量不同。专业版支持变量插值、条件渲染、循环结构，类似 Jinja2 语法.
## 使用流程

### 批量生成多份报告

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from pathlib import Path
# ...
TEMPLATE = {
    'title': '2026年{month}月销售报告',
    'headers': ['日期', '产品', '数量', '金额'],
}
# ...
def generate_report(branch: str, month: str, data: list, output_dir: str):
    """根据模板生成单份报告。"""
    wb = Workbook()
    ws = wb.active
    ws.title = f"{branch}_{month}"
# ...
    # 标题（变量插值）
    ws['A1'] = TEMPLATE['title'].format(month=month)
    ws['A1'].font = Font(bold=True, size=16)
# ...
    # 表头
    for c, h in enumerate(TEMPLATE['headers'], 1):
        cell = ws.cell(row=3, column=c, value=h)
        cell.font = Font(bold=True, color='FFFFFF')
        cell.fill = PatternFill(start_color='3182CE', end_color='3182CE', fill_type='solid')
# ...
    # 数据
    for r, row in enumerate(data, 4):
        for c, v in enumerate(row, 1):
            ws.cell(row=r, column=c, value=v)
# ...
    # 保存
    output_path = Path(output_dir) / f"{branch}_{month}.xlsx"
    wb.save(output_path)
    return str(output_path)
# ...
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
# ...
def export_postgres_to_excel(query: str, conn_str: str, output_path: str):
    """从 PostgreSQL 抽取数据到 Excel。"""
    with closing(psycopg2.connect(conn_str)) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            columns = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
# ...
    wb = Workbook()
    ws = wb.active
    ws.title = "数据导出"
# ...
    # 表头
    ws.append(columns)
    for cell in ws[1]:
        cell.font = Font(bold=True, color='FFFFFF')
        cell.fill = PatternFill(start_color='3182CE', end_color='3182CE', fill_type='solid')
# ...
    # 数据
    for row in rows:
        ws.append(row)
# ...
    wb.save(output_path)
    print(f"导出 {len(rows)} 行到 {output_path}")
# ...
# 示例
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
# ...
# 色阶规则（销售额）
ws.conditional_formatting.add('D2:D100',
    ColorScaleRule(
        start_type='min', start_color='F8696B',
        mid_type='percentile', mid_value=50, mid_color='FFEB84',
        end_type='max', end_color='63BE7B'
    )
)
# ...
# 单元格规则（低于目标红色）
ws.conditional_formatting.add('E2:E100',
    CellIsRule(operator='lessThan', formula=['50000'],
               fill=PatternFill(start_color='FFC7CE', fill_type='solid'))
)
# ...
# 数据条规则
ws.conditional_formatting.add('F2:F100',
    DataBarRule(start_type='min', end_type='max', color='638EC6')
)
```

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | excel-craft处理的内容输入 |,  |
| content | string | 否 | excel-craft处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "craft 相关配置参数",
    result: "craft 相关配置参数",
    result: "craft 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|:------|------:|:------|:------|
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

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.9+
- **办公软件**：Microsoft Excel / WPS / LibreOffice / Numbers

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本兼容性 |
|---:|:---|---:|---:|:---|
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

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1：批量生成时内存飙升？
A：openpyxl 默认载入全部数据。大文件用 `write_only=True` 模式，批量场景使用 `ThreadPoolExecutor` 并控制 worker 数.
### Q2：条件格式在 WPS 不生效？
A：WPS 对色阶、图标集支持不全。降级为单元格规则或手工配色.
### Q3：`PostgreSQL` 连接报认证失败？
A：检查 `pg_hba.conf` 是否允许来源 IP；密码建议存储到凭据管理器而非环境变量明文.
### Q4：合并文件后字段错位？
A：合并前确认所有文件的列顺序一致。建议按字段名匹配而非位置匹配.
### Q5：模板渲染速度慢？
A：Jinja2 渲染大量数据时使用 `Environment(trim_blocks=True)`，避免空白处理开销.
### Q6：保护规则被 WPS 绕过？
A：WPS 对工作表保护实现较弱。需要高安全级别时建议改用数字签名或文件加密.
### Q7：跨平台格式丢失？
A：测试时同时用 Excel / WPS / LibreOffice 打开。条件格式、迷你图、自定义数字格式是高发问题区.
### Q8：模板变量与公式冲突？
A：模板变量用 `excel-craft_template` 语法，公式用 `=` 开头，两者不会冲突。但若公式中含 `{{` 字符，需转义.
### Q9：数据库抽取超时？
A：报表场景使用只读事务 + 短超时（30 秒）。大表查询加索引或物化视图.
### Q10：批量生成后文件大小不一？
A：openpyxl 默认不压缩。可在保存后用 `zipfile` 重新压缩，或设置 `wb.properties.title` 等元数据减小体积.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 数据处理能力受限于本地硬件资源
- 大数据量时分析性能可能显著下降
