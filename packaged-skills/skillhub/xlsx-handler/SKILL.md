---

slug: "xlsx-handler"
name: "xlsx-handler"
version: 1.0.1
displayName: "XLSX处理专业版"
summary: "企业级 XLSX 读写引擎，含批量处理、大文件流式、公式审计、跨平台兼容与数据源对接。。XLSX 处理专业版在免费版基础上扩展批量处理、大文件流式读写、工作簿差异对比、公式审计与依赖追踪、数"
license: "MIT"
edition: "pro"
description: |-
  XLSX 处理专业版在免费版基础上扩展批量处理、大文件流式读写、工作簿差异对比、公式审计与依赖追踪、数据源对接与跨平台深度兼容能力。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags: 分析,python,str,row,llm,openpyxl
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
category: "Automation"

---

# XLSX处理专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| XLSX处理专业版含批量处理 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

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
- 按任务选择 pandas / openpyxl 路径
- 保留公式、样式、合并单元格、定义名称
- 日期序列号与 1900/1904 系统处理
- 类型保护（长数字、电话、邮编）
- 工作簿结构保护与错误校验

### 专业版新增能力
| 能力模块 | 输入 | 输出 | 适用场景 |
|---:|---:|---:|---:|
| 批量处理 | 文件列表 | 处理结果 | 大规模编辑 |
| 流式读写 | 大文件 | 流式结果 | >10MB 文件 |
| 工作簿对比 | 两个文件 | 差异报告 | 版本治理 |
| 公式审计 | 工作簿 | 依赖图 | 错误排查 |
| 跨平台兼容测试 | 文件 | 兼容性报告 | 多端分发 |
| 数据源对接 | 连接配置 | 双向同步 | 数据库集成 |
| 公式追踪 | 单元格 | 影响范围 | 修改影响评估 |
| 保护与权限 | 区域 + 密码 | 锁定规则 | 防误改 |

## 适用场景

### 场景一：批量文件处理（数据团队角色）
部门有 200 份结构相同的 Excel 文件，需要批量修改某个 Sheet 的某个字段。专业版提供批量处理脚本，并行执行并输出成功 / 失败列表.
### 场景二：大文件流式读写（运维角色）
单文件 500MB，包含百万行数据。专业版使用 `read_only=True` 与 `write_only=True` 流式模式，内存占用控制在 100MB 以内.
### 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.9+
- **办公软件**：Excel / WPS / LibreOffice / Numbers

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本兼容性 |
|:---:|:---:|:---:|:---:|:---:|
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

## 使用流程

### 批量处理脚本

```python
from openpyxl import load_workbook
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
# ...
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
# ...
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
# ...
files = list(Path('reports').glob('*.xlsx'))
result = batch_process(files, '状态', '已审核')
print(f"成功：{result['success']}，失败：{len(result['failed'])}")
```

### 大文件流式读写

```python
from openpyxl import load_workbook, Workbook
# ...
def stream_filter_large(input_path: str, output_path: str, condition):
    """流式过滤大文件，保留符合条件的数据。"""
    # 流式读取
    wb_in = load_workbook(input_path, read_only=True)
    ws_in = wb_in.active
# ...
    # 流式写入
    wb_out = Workbook(write_only=True)
    ws_out = wb_out.create_sheet('Filtered')
# ...
    # 写入表头
    headers = next(ws_in.iter_rows(values_only=True))
    ws_out.append(headers)
# ...
    # 流式过滤
    count = 0
    for row in ws_in.iter_rows(min_row=2, values_only=True):
        if condition(row):
            ws_out.append(row)
            count += 1
# ...
    wb_out.save(output_path)
    wb_in.close()
    print(f"过滤完成，保留 {count} 行")
# ...
# 示例
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
# ...
def trace_dependents(wb_path: str, sheet: str, cell: str) -> dict:
    """追踪单元格的所有依赖（哪些公式引用了它）。"""
    wb = load_workbook(wb_path, data_only=False)
    ws = wb[sheet]
    dependents = []
# ...
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
# ...
    return {'target': cell, 'dependents': dependents}
# ...
result = trace_dependents('report.xlsx', 'Sheet1', 'A1')
print(f"A1 被以下 {len(result['dependents'])} 个公式引用：")
for d in result['dependents']:
    print(f"  {d['cell']}: {d['formula']}")
```

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:------|------:|:------|:------|
| content | string | 否 | xlsx-handler处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|---:|:---|---:|---:|
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

## 依赖说明(补充)

| 依赖项 | 类型 | 必需 | 说明 |
|:------:|--------|:-------|:------:|
| LLM | 模型 | 是 | 需要LLM进行智能审查, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100
# ...
检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100
# ...
检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100
# ...
检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过
# ...
改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1：批量处理内存飙升？
A：每个文件处理完立即 `wb.close()` 释放。worker 数控制在 4 以内，过多会争抢内存.
### Q2：流式模式不支持样式？
A：`write_only=True` 模式不支持单元格样式。需要样式时分批处理（每批 1 万行用普通模式），或先流式生成数据再用普通模式重新打开加样式.
### Q3：公式追踪漏掉跨 Sheet 引用？
A：简化版正则只匹配同一 Sheet 内引用。跨 Sheet 引用形如 `Sheet2!A1`，需要单独处理 `!` 分隔符.
### Q4：`关系型数据库` 抽取超时？
A：报表场景使用只读事务 + 短超时（30 秒）。大表查询加索引或物化视图.
### Q5：跨平台兼容性测试耗时？
A：测试 100+ 特性 × 5 平台较慢。建议建立特性白名单，只测试工作簿实际使用的特性.
### Q6：工作簿对比工具输出过多差异？
A：先对比 Sheet 列表，再针对共有 Sheet 对比。单元格差异按区域聚合，避免逐条列出.
### Q7：保护规则被绕过？
A：openpyxl 的工作表保护可被脚本绕过。需要高安全级别时建议改用文件加密或数字签名.
### Q8：流式写入后文件无法打开？
A：`write_only=True` 模式必须用 `ws.append()` 添加数据，不能直接设置单元格值。保存前确认所有数据已 append.
### Q9：批量处理中途中断如何续传？
A：把已完成文件列表写入检查点文件，重启时跳过已完成项。失败列表单独记录以便重试.
### Q10：跨平台分发后筛选丢失？
A：LibreOffice 与 Numbers 对部分筛选语法支持不全。建议分发前同时测试三个平台，必要时降级为基本筛选.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 数据处理能力受限于本地硬件资源
- 大数据量时分析性能可能显著下降
