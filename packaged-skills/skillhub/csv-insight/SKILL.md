---
slug: csv-insight
name: csv-insight
version: "1.0.0"
displayName: CSV洞察 专业版
summary: 全功能CSV分析，支持流式大文件、相关性分析、分布可视化与高级异常检测。
license: Proprietary
edition: pro
description: |-
  CSV Insight 专业版面向专业数据分析师与数据科学家，在免费版基础上解锁流式大文件处理、相关性分析、分布可视化与高级异常检测算法。核心能力：GB 级 CSV 流式分析、列间相关系数矩阵、分布可视化（直方图/箱线图/散点图）、高级聚合（median/std/percentile）、多异常检测算法（IQR/DBSCAN/Z-Score）、多文件对比分析、Schema 配置与列类型强制、报表导出（Markdown/HTML）
tags:
- 集成工具
- 数据分析
- 数据科学
- 可视化
tools:
  - - read
- exec
---
# CSV洞察 专业版

## 核心能力

| 能力域 | 命令 | 说明 | 专业版增强 |
|--------|------|------|-----------|
| 流式统计 | `stream stats` | GB 级文件流式统计 | 专业版独有 |
| 相关性分析 | `correlate` | 列间相关系数矩阵 | 专业版独有 |
| 分布可视化 | `plot histogram` / `plot boxplot` / `plot scatter` | 直方图/箱线图/散点图 | 专业版独有 |
| 高级聚合 | `group --agg` | median/std/percentile | 专业版增强 |
| 异常检测 | `anomalies --method` | IQR/DBSCAN/Z-Score 三种 | 专业版增强 |
| 多文件对比 | `compare` | 多数据集并排对比 | 专业版独有 |
| Schema 配置 | `schema` | 列类型强制指定 | 专业版独有 |
| 报表导出 | `report` | Markdown/HTML 报表 | 专业版独有 |
| 统计摘要 | `stats` | 继承免费版 | 继承 |
| 行筛选 | `filter` | 继承免费版 | 继承 |
| Top/Bottom N | `top` / `bottom` | 继承免费版 | 继承 |
### 能力域

执行能力域操作,处理用户输入并返回结果。

**输入**: 用户提供能力域所需的参数和指令。

**输出**: 返回能力域的处理结果。
### 流式统计

执行流式统计操作,处理用户输入并返回结果。

**输入**: 用户提供流式统计所需的参数和指令。

**输出**: 返回流式统计的处理结果。
### 相关性分析

执行相关性分析操作,处理用户输入并返回结果。

**输入**: 用户提供相关性分析所需的参数和指令。

**输出**: 返回相关性分析的处理结果。


## 适用场景
- 不适用: 需要人工判断的复杂决策场景

### 场景一：GB 级日志数据分析（数据工程师）

5GB 的访问日志 CSV 需要统计各状态码分布与响应时间分位数。免费版会 OOM，专业版流式处理：

```bash
# 流式统计（内存占用 < 300MB）
csv-insight stream stats access_log.csv --chunk-size 100MB

# 流式分组聚合
csv-insight stream group access_log.csv \
  --by status_code \
  --agg "count:id" "avg:response_time" "percentile:response_time:95" \
  --chunk-size 100MB
```

### 场景二：特征相关性挖掘（数据科学家）

构建机器学习模型前，需要识别强相关特征以避免多重共线性。专业版提供相关系数矩阵：

```bash
# 计算所有数值列的相关系数
csv-insight correlate features.csv --method pearson

# 输出热力图（ASCII）
csv-insight correlate features.csv --method pearson --heatmap

# 识别强相关对（|r| > 0.8）
csv-insight correlate features.csv --method pearson --threshold 0.8
```

输出示例：

```
相关性矩阵（Pearson）:
              age    income   score   visits
age       1.000   0.452   -0.123   0.089
income    0.452   1.000    0.678   0.234
score    -0.123   0.678    1.000   0.567
visits    0.089   0.234    0.567   1.000

强相关对（|r| > 0.5）:
  income  <->  score    : 0.678
  score   <->  visits   : 0.567
```

### 场景三：数据分布可视化（数据分析师）

需要查看金额列的分布形态，判断是否正态分布。专业版提供 ASCII 直方图与箱线图：

```bash
# 直方图（自动分箱）
csv-insight plot histogram data.csv --column amount --bins 20

# 箱线图（识别离群点）
csv-insight plot boxplot data.csv --column amount

# 散点图（两列关系）
csv-insight plot scatter data.csv --x income --y score
```

直方图输出示例：

```
amount 分布直方图（20 箱）:
0-450      | ████████████████████ (3200)
450-900    | ██████████████ (2100)
900-1350   | ████████ (1200)
1350-1800  | ████ (600)
1800-2250  | ██ (300)
2250-2700  | █ (150)
2700+      | ▏ (50)
```

### 场景四：复杂异常检测（数据质量工程师）

单一 Z-Score 无法识别非正态分布的异常。专业版提供 IQR 与 DBSCAN 算法：

```bash
# IQR 方法（适合偏态分布）
csv-insight anomalies data.csv --column amount --method iqr --factor 1.5

# DBSCAN 方法（适合多维异常）
csv-insight anomalies data.csv \
  --columns amount,frequency,recency \
  --method dbscan \
  --eps 0.5 --min-samples 5

# 多方法对比
csv-insight anomalies data.csv --column amount --method all --compare
```

### 场景五：多数据集对比（业务分析师）

需要对比本季度与上季度的订单数据分布差异。专业版提供对比分析：

```bash
# 对比两个数据集的统计差异
csv-insight compare q1_orders.csv q2_orders.csv \
  --columns amount,quantity \
  --report comparison.md
```

### 场景六：数据质量评估报告（数据治理角色）

需要生成数据质量评估报告供团队评审。专业版支持报表导出：

```bash
# 生成完整数据质量报告
csv-insight report data.csv \
  --include stats,schema,anomalies,distribution,correlation \
  --format markdown \
  --output data-quality-report.md

# HTML 格式（含图表）
csv-insight report data.csv \
  --include stats,schema,anomalies,distribution \
  --format html \
  --output data-quality-report.html
```

## 使用流程

### 前置准备（约 60 秒）

1. 确认 Python 3.8+ 已安装
2. 可选安装高级依赖（用于 DBSCAN 等算法）：

```bash
pip install numpy scipy scikit-learn
```

3. 配置专业版工作目录：

```bash
export CSV_INSIGHT_HOME="$HOME/.csv-insight"
```

### 验证专业版能力（约 30 秒）

```bash
# 验证流式统计
csv-insight stream stats large.csv --chunk-size 10MB

# 验证相关性分析
csv-insight correlate sample.csv --method pearson
```

### 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+
- **内存**：建议 4GB+（流式处理可低于 2GB）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:-------|:-----|:---------|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |
| Python | 运行时 | 必需 | 官网下载 | 3.8+ |
| csv 模块 | Python 标准库 | 必需 | Python 自带 | - |
| numpy | 第三方库 | 可选 | `pip install numpy` | 1.20+ |
| scipy | 第三方库 | 可选 | `pip install scipy` | 1.7+ |
| scikit-learn | 第三方库 | 可选 | `pip install scikit-learn` | 1.0+ |

### API Key 配置

- 本 Skill 基于 Python 标准库与可选第三方库，无需额外 API Key
- 第三方库安装通过 pip 完成，无需 API 凭据

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 调用 Python 脚本完成任务

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
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

- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断
- 执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令机制: 失败时自动执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令, 最多3次

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|------|----------|----------|--------|
| OOM 内存溢出 | 全量加载大文件 | 切换流式处理 | P0 |
| 相关系数为 NaN | 列含缺失值 | 用 `--handle-missing` 处理 | P1 |
| DBSCAN 聚类失败 | 数据未标准化 | 先 z-score 标准化 | P1 |
| 直方图分箱异常 | 列含异常值 | 先 IQR 过滤异常 | P1 |
| Schema 校验失败 | 列名或类型不匹配 | 核对 Schema 与数据 | P1 |
| 报表导出失败 | 磁盘空间不足 | 清理临时目录 | P2 |
| 流式中断 | 网络或进程被杀 | 从检查点恢复 | P2 |
| 多文件对比列不匹配 | 列名不一致 | 启用 `--normalize-headers` | P2 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行智能审查, 推荐GPT-4/智谱GLM-4/DeepSeek |
| `references/checklist.md` | 文件 | 是 | 相关说明 |
| `references/scoring.md` | 文件 | 否 | 相关说明 |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

## 案例展示

### Schema 配置（列类型强制）

```yaml
# $CSV_INSIGHT_HOME/schema.yaml
columns:
  - name: order_id
    type: integer
    required: true
  - name: amount
    type: float
    required: true
  - name: created_at
    type: datetime
    format: "%Y-%m-%d %H:%M:%S"
  - name: zipcode
    type: string    # 强制为字符串，避免前导零丢失
```

```bash
# 使用 Schema 解析
csv-insight stats data.csv --schema schema.yaml
```

### 报表配置

```yaml
# $CSV_INSIGHT_HOME/report-config.yaml
sections:
  - overview        # 数据概览
  - schema          # 列类型与约束
  - stats           # 统计摘要
  - distribution    # 分布可视化
  - anomalies       # 异常检测
  - correlation     # 相关性分析
  - quality_score   # 数据质量评分
format: markdown
include_charts: true
anomaly_method: iqr
correlation_method: pearson
```

### 异常检测算法对比

| 算法 | 适用场景 | 优点 | 局限 |
|------|----------|------|------|
| Z-Score | 正态分布数据 | 计算简单 | 不适合偏态分布 |
| IQR | 偏态分布数据 | 不受极端值影响 | 仅单变量 |
| DBSCAN | 多维异常 | 可识别聚类异常 | 需调参（eps/min_samples） |

## 常见问题

### Q1：流式处理的精度与全量一致吗？

统计摘要（count/sum/min/max）完全一致。均值与方差在分块累加下精度略有差异，但误差可忽略。分位数采用近似算法（t-digest），误差 <1%。

### Q2：相关系数矩阵对缺失值如何处理？

默认跳过含缺失值的行（pairwise deletion）。可通过 `--handle-missing drop`（删除缺失行）或 `--handle-missing impute`（均值填充）调整。

### Q3：DBSCAN 的 eps 与 min_samples 怎么选？

eps 是邻域半径，min_samples 是核心点最小邻居数。建议从 `eps=0.5, min_samples=5` 开始，根据聚类结果调整。数据需先标准化（z-score）。

### Q4：直方图分箱数怎么确定？

可用 `--bins auto` 让算法自动选择（Freedman-Diaconis 规则）。也可手动指定，建议范围 10-50。

### Q5：报表导出包含哪些内容？

默认包含：数据概览、Schema、统计摘要、分布可视化、异常检测、相关性分析、数据质量评分。可通过 `--include` 参数选择章节。

### Q6：多文件对比支持哪些统计？

支持：行数、列数、数值列的 min/max/mean/median/std、文本列唯一值数、缺失率、异常率。对比结果以表格形式呈现差异。

### Q7：Schema 配置后类型还是不对？

检查 Schema 文件路径是否正确（`--schema` 参数）、列名是否与数据一致（大小写敏感）、日期格式是否匹配。可用 `csv-insight schema validate` 校验 Schema 配置。

### Q8：流式处理能否中断恢复？

支持。启用 `--checkpoint` 后，中断后可从断点恢复：

```bash
csv-insight stream stats large.csv --checkpoint --resume-on-failure
```

### Q9：HTML 报表的图表是图片吗？

不是。HTML 报表使用 ASCII 字符渲染图表，无需额外图片资源，可在任何浏览器查看。

### Q10：专业版与免费版可以共存吗？

可以。两个版本 slug 不同，可同时安装。日常快速统计用免费版，深度分析与报表用专业版。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
