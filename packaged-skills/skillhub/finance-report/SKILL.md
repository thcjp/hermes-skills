---
slug: "finance-report"
name: "finance-report"
version: 1.0.1
displayName: "财报分析专业版"
summary: "企业级财报分析系统，支持批量处理、多格式导出、行业基准与深度预测模型。"
license: "Proprietary"
edition: "pro"
description: |-
  面向专业分析师与机构的财报分析系统。支持批量文件处理、PDF/DOCX/
  Markdown多格式导出、行业基准对比、高级预测模型与自定义报告模板。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - Finance
  - 财报分析
  - 企业级
  - 报告生成
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 财报分析专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 财报分析专业版企业级财报分析 | 不支持 | 支持 |
| 财报分析专业版支持批量处理 | 不支持 | 支持 |
| 财报分析专业版多格式导出 | 不支持 | 支持 |
| DCF估值建模与敏感性分析 | 不支持 | 支持 |
| 财务舞弊识别(Beneish M-Score) | 不支持 | 支持 |

## 核心能力

### PRO版功能增强对比
| 功能 | 免费版 | PRO版 |
|:-----|:-----|:-----|
| 数据提取 | Excel/PDF | +扫描版PDF(OCR) |
| 报告格式 | 仅HTML | HTML/PDF/DOCX/MD |
| 批量处理 | 不支持 | 多文件并行 |
| 行业基准 | 不支持 | 同业对标+百分位 |
| 预测模型 | 基础外推 | ARIMA/ML/回归 |
| 报告模板 | 固定模板 | 自定义品牌模板 |
| 对比报告 | 不支持 | 多公司横向对比 |

**输入**: 用户提供PRO版功能增强对比所需的指令和必要参数.
**输出**: 返回PRO版功能增强对比的处理结果,包含执行状态码、结果数据和执行日志。### 高级预测模型
| 模型 | 适用场景 | 准确度 |
|---:|---:|---:|
| 线性回归 | 线性趋势数据 | 中 |
| ARIMA | 时间序列预测 | 高 |
| 指数平滑 | 短期预测 | 中高 |
| 机器学习 | 复杂模式 | 高（需训练数据） |
| 蒙特卡洛 | 概率区间预测 | 高 |

**输入**: 用户提供高级预测模型所需的指令和必要参数.
**处理**: 解析高级预测模型的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回高级预测模型的处理结果,包含执行状态码、结果数据和执行日志.
### 数据提取

针对数据提取,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供数据提取相关的配置参数、输入数据和处理选项.
**输出**: 返回数据提取的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`数据提取`的配置文档进行参数调优
### 报告格式

针对报告格式,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供报告格式相关的配置参数、输入数据和处理选项.
**输出**: 返回报告格式的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`报告格式`的配置文档进行参数调优
#
## 适用场景

### 场景一：批量财报分析

用户输入："分析这20家公司的年报"

```bash
# 批量处理多个文件
python3 （请参考skill目录中的脚本文件） \
  --input-dir ./annual_reports/ \
  --output-dir ./reports/ \
  --format pdf \
  --parallel 5
# ...
# 生成对比报告
python3 （请参考skill目录中的脚本文件） \
  --input-dir ./reports/ \
  --output industry_comparison.xlsx \
  --benchmark "industry_average"
```

### 场景二：行业基准对比

用户输入："对比这家公司与行业平均水平"

```bash
# 行业基准分析
python3 （请参考skill目录中的脚本文件） \
  --company "600519.SH" \
  --industry "白酒" \
  --metrics "roe,gross_margin,pe,pb" \
  --output benchmark_report.pdf
```

### 场景三：自定义报告模板

用户输入："用我们公司的模板生成财报分析"

```bash
# 使用自定义模板
python3 （请参考skill目录中的脚本文件） data.xlsx \
  -o pdf \
  --template "company_brand" \
  --logo ./logo.png \
  --colors "#1a5276,#2e86c1"
```

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt
# ...
# 配置报告模板
cp config_pro_template.yaml config_pro.yaml
```

### 常用命令

```bash
# 批量处理
python3 （请参考skill目录中的脚本文件） --input-dir ./data/ --format pdf
# ...
# 多格式导出
python3 （请参考skill目录中的脚本文件） data.xlsx -o pdf,docx,html
# ...
# OCR提取
python3 （请参考skill目录中的脚本文件） scanned_report.pdf --ocr
# ...
# 行业基准
python3 （请参考skill目录中的脚本文件） --company "000001.SZ" --industry "银行业"
# ...
# 高级预测
python3 （请参考skill目录中的脚本文件） data.xlsx \
  --forecast-model arima \
  --forecast-years 3
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | finance-report处理的内容输入 |,  |
| content | string | 否 | finance-report处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "report 相关配置参数",
    result: "report 相关配置参数",
    result: "report 相关配置参数",
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

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+
- **Tesseract OCR**: 4.0+（扫描版PDF识别）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| pandas | Python库 | 必需 | `pip install pandas` |
| openpyxl | Python库 | 必需 | `pip install openpyxl` |
| pdfplumber | Python库 | 必需 | `pip install pdfplumber` |
| pytesseract | Python库 | 可选 | `pip install pytesseract`（OCR） |
| jinja2 | Python库 | 必需 | `pip install jinja2`（模板） |
| statsmodels | Python库 | 可选 | `pip install statsmodels`（ARIMA） |
| weasyprint | Python库 | 可选 | `pip install weasyprint`（PDF导出） |

### API Key 配置

- PRO版无需外部API Key
- 所有数据处理与报告生成在本地完成
- 行业基准数据内置在系统中

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 企业级财报分析系统，支持批量处理、OCR识别与多格式导出
- **PRO版特性**: 批量处理、OCR识别、多格式导出、行业基准、高级预测、自定义模板
- **兼容性**: 完全兼容免费版全部命令与报告格式

## 案例展示

### PRO企业级配置

```yaml
pro_config:
  processing:
    batch:
      max_parallel: 5              # 最大并行数
      timeout: 600                 # 超时（秒）
    ocr:
      enabled: true
      engine: "tesseract"
      languages: ["chi_sim", "eng"]
# ...
  output:
    formats: ["html", "pdf", "docx", "markdown"]
    dir: "./reports"
    template_dir: "./templates"
    branding:
      logo: "./assets/logo.png"
      primary_color: "#1a5276"
      font: "Microsoft YaHei"
# ...
  forecast:
    models: ["arima", "linear", "exponential"]
    default_model: "arima"
    forecast_years: 3
    confidence_interval: [0.05, 0.95]
# ...
  benchmark:
    industry_data: "./benchmarks/"
    metrics:
      - roe
      - roa
      - gross_margin
      - net_margin
      - pe
      - pb
      - debt_ratio
    percentile_ranking: true
```

## 常见问题

### Q1：OCR识别准确率如何？

OCR准确率取决于扫描质量。300DPI以上的清晰扫描件准确率可达90%+。建议优先使用原生PDF或Excel格式，扫描版作为备选.
### Q2：批量处理支持多少文件？

PRO版单批次支持最多50个文件的并行处理。建议根据CPU核心数调整并行度，避免内存不足.
### Q3：行业基准数据从哪来？

PRO版内置常见行业的基准数据。用户也可导入自定义基准数据（如同业公司的财务数据），进行更精准的对标分析.
### Q4：自定义模板如何制作？

PRO版支持基于Jinja2的自定义模板。在templates目录创建HTML模板文件，使用变量占位符（如Finance Report 核心处理、Finance Report 核心处理），系统自动填充数据.
### Q5：预测模型的置信区间如何解读？

置信区间表示预测值的可能范围。例如95%置信区间表示预测值有95%的概率落在该范围内。区间越窄说明预测越精确，但过低可能意味着模型过拟合.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

