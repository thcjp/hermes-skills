---
slug: accounting-finance
name: accounting-finance
version: "1.0.0"
displayName: 财务分析专业套件
summary: 企业级财务分析与估值建模全套技能，58个专业分析模块，支持批量处理与自动化报告。
license: Proprietary
edition: pro
description: |-
  面向专业分析师、机构投资者与企业财务部门的全栈财务分析技能套件。包含58个
  专家级分析技能，覆盖估值建模、财务分析、风险评估三大核心领域，支持批量
  处理、自动化报告生成与企业级工作流。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Finance
- 估值分析
- 财务建模
- 风险评估
- 企业级
tools:
  - - read
- exec
---
# 财务分析专业套件

## 核心能力

### 一、估值建模（14个技能）


**输入**: 用户提供一、估值建模（14个技能）所需的指令和必要参数。
**处理**: 按照skill规范执行一、估值建模（14个技能）操作,遵循单一意图原则。
**输出**: 返回一、估值建模（14个技能）的执行结果,包含操作状态和输出数据。

- 执行`一、估值建模（14个技能）`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`一、估值建模（14个技能）`相关配置参数进行设置
### DCF估值模型

| 技能 | 用途 | PRO版增强 |
| --- | --- | --- |
| `dcf-zero-growth` | DCF零增长模型 | 支持概率加权情景分析 |
| `dcf-constant-growth` | DCF恒定增长模型 | 多期增长率分段 |
| `dcf-two-stage` | DCF二阶段模型 | 蒙特卡洛模拟 |
| `dcf-three-stage` | DCF三阶段模型 | PRO专属：复杂增长模式 |

#### 可比估值模型

| 技能 | 用途 | 关键指标 |
| --- | --- | --- |
| `pe-valuation` | 市盈率估值 | 滚动/预期PE对比 |
| `pb-valuation` | 市净率估值 | 账面价值调整 |
| `ps-valuation` | 市销率估值 | 收入质量调整 |
| `peg-valuation` | PEG估值 | 增长预期校准 |

#### 资本成本与行业特化估值（PRO专属）

| 技能 | 用途 | 输出结果 |
| --- | --- | --- |
| `wacc-calculation` | 加权平均资本成本 | WACC、折现率、资本结构优化 |
| `cost-of-equity-capm` | 股权成本（CAPM） | Beta校准、预期收益率 |
| `bank-valuation` | 银行估值 | 剩余收益模型、P/PPOP |
| `insurance-valuation` | 保险估值 | 内含价值、新业务价值 |
| `real-estate-valuation` | 房地产估值 | DCF、资本化率、NAV |
| `tech-company-valuation` | 科技公司估值 | SaaS指标、用户价值模型 |

### 二、财务分析（26个技能）
#### 财务比率与盈利分析

| 技能 | 用途 | PRO版增强 |
| --- | --- | --- |
| `financial-ratio-framework` | 财务比率综合分析 | 五维比率+同业百分位 |
| `dupont-five-factor` | 杜邦五因素分析 | 多期对比与归因 |
| `roe-analysis` | ROE分析 | 分解至经营杠杆 |
| `roic-analysis` | ROIC分析 | PRO专属：投入资本回报 |
| `gross-margin-analysis` | 毛利率分析 | 成本结构拆解 |
| `revenue-analysis` | 收入分析 | 收入质量与集中度 |
| `cost-analysis` | 成本分析 | PRO专属：成本控制 |
| `expense-analysis` | 费用分析 | PRO专属：费用效率 |

#### 现金流分析（PRO完整版）

| 技能 | 用途 | 现金流类型 |
| --- | --- | --- |
| `cashflow-forecasting` | 现金流预测 | 未来现金流建模 |
| `free-cashflow-calculation` | 自由现金流计算 | FCFF/FCFE |
| `operating-cashflow-analysis` | 经营现金流分析 | 核心经营活动 |
| `investing-cashflow-analysis` | 投资现金流分析 | 资本支出效率 |
| `financing-cashflow-analysis` | 融资现金流分析 | 融资活动评估 |
| `cashflow-profit-reconciliation` | 现金流利润调节 | 净利润→经营现金流 |
| `cash-cycle-analysis` | 现金周期分析 | CCC、周转效率 |
| `working-capital-analysis` | 营运资本分析 | 流动性管理 |

#### 资产结构与报表处理（PRO专属）

| 技能 | 用途 | 分析对象 |
| --- | --- | --- |
| `asset-structure-analysis` | 资产结构分析 | 资产配置优化 |
| `asset-capital-matching` | 资产资本匹配 | 期限匹配评估 |
| `capital-structure-analysis` | 资本结构分析 | 债务/股权优化 |
| `interest-bearing-debt-analysis` | 有息负债分析 | 债务成本测算 |
| `balance-sheet-restructuring` | 资产负债表重组 | 重组方案设计 |
| `financial-statement-extraction` | 财务报表提取 | 自动化数据提取 |
| `financial-data-standardization` | 财务数据标准化 | 口径统一 |
| `income-statement-restructuring` | 利润表重组 | 重分类调整 |
| `notes-to-financial-statements` | 财务报表附注分析 | 附注深度解读 |

#### 可比公司与竞争分析

| 技能 | 用途 | 功能 |
| --- | --- | --- |
| `peer-selection` | 可比公司筛选 | 智能对标选择 |
| `peer-comparison-analysis` | 可比公司分析 | 横向对比矩阵 |
| `industry-benchmarking` | 行业基准对比 | 行业百分位 |
| `competitive-positioning` | 竞争定位分析 | 市场地位评估 |

**输入**: 用户提供二、财务分析（26个技能）所需的指令和必要参数。
**输出**: 返回二、财务分析（26个技能）的执行结果,包含操作状态和输出数据。### 三、风险评估（18个技能）

#### 风险检测与质量评估

| 技能 | 用途 | PRO版增强 |
| --- | --- | --- |
| `fraud-risk-detection` | 欺诈风险检测 | Beneish模型集成 |
| `liquidity-risk-assessment` | 流动性风险评估 | 压力测试 |
| `sensitivity-analysis` | 敏感性分析 | 多变量蒙特卡洛 |
| `earnings-quality-analysis` | 盈利质量分析 | 应计利润模型 |
| `profit-quality-analysis` | 利润质量分析 | PRO专属：利润真实性 |
| `financial-statement-quality` | 财务报表质量 | 整体质量评分 |
| `financial-statement-quality-check` | 财务报表质量检查 | 质量清单核验 |

#### 特殊事项分析（PRO专属）

| 技能 | 用途 | 关注点 |
| --- | --- | --- |
| `related-party-transaction-analysis` | 关联交易分析 | 利益输送识别 |
| `audit-report-analysis` | 审计报告分析 | 审计意见解读 |
| `accounting-policy-analysis` | 会计政策分析 | 政策选择影响 |
| `accounting-estimate-evaluation` | 会计估计评估 | 估计合理性 |
| `tax-analysis` | 税务分析 | 税务风险与优化 |

#### 决策支持

| 技能 | 用途 | 输出 |
| --- | --- | --- |
| `trend-analysis` | 趋势分析 | 时间序列预测 |
| `investment-thesis-generation` | 投资论点生成 | 多情景投资建议 |
| `portfolio-tracking` | 投资组合跟踪 | 组合批量监控 |
| `valuation-report-writer` | 估值报告撰写 | 专业报告自动生成 |

### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级财务分析与、估值建模全套技能、个专业分析模块、支持批量处理与自、动化报告、面向专业分析师、机构投资者与企业、财务部门的全栈财、务分析技能套件、专家级分析技能、覆盖估值建模、风险评估三大核心、支持批量、自动化报告生成与、企业级工作流、Use、需要提升效率、自动化流程、批量处理、工作流优化时使用、不适用于需要人工、创意判断的任务、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一：IPO估值全流程

用户输入："某科技公司准备IPO，需要完整的估值分析"

```text
PRO执行流程：
1. tech-company-valuation    - 确定科技公司估值方法
2. dcf-three-stage           - 三阶段DCF估值（含蒙特卡洛）
3. peer-selection            - 智能筛选可比公司
4. peer-comparison-analysis  - 可比公司估值矩阵
5. sensitivity-analysis      - 多变量敏感性分析
6. valuation-report-writer   - 自动生成估值报告
```

### 场景二：投资组合批量监控

用户输入："监控我的50只持仓股票的财务健康度"

```bash
# PRO批量分析模式
python3 batch_analysis.py --portfolio portfolio.csv \
  --skills "fraud-risk-detection,earnings-quality-analysis,liquidity-risk-assessment" \
  --output portfolio_risk_report.xlsx \
  --format excel
```

### 场景三：深度财务尽调

用户输入："对目标公司做完整的财务尽调"

```text
PRO执行流程：
1. financial-statement-extraction     - 报表数据提取
2. financial-data-standardization     - 口径标准化
3. financial-ratio-framework          - 五维比率分析
4. dupont-five-factor                 - ROE深度拆解
5. cashflow-profit-reconciliation     - 现金流利润调节
6. related-party-transaction-analysis - 关联交易排查
7. audit-report-analysis              - 审计意见分析
8. accounting-policy-analysis         - 会计政策评估
9. fraud-risk-detection               - 欺诈风险检测
10. valuation-report-writer           - 生成尽调报告
```

## 使用流程

### 依赖说明

### 运行环境

1. **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
2. **操作系统**: Windows / macOS / Linux
3. **Python版本**: 3.9+（推荐3.11）
4. **内存要求**: 建议8GB+（批量分析与蒙特卡洛模拟）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| numpy | Python库 | 必需 | `pip install numpy` |
| pandas | Python库 | 必需 | `pip install pandas` |
| scipy | Python库 | 必需 | `pip install scipy`（蒙特卡洛） |
| matplotlib | Python库 | 可选 | `pip install matplotlib`（图表） |
| openpyxl | Python库 | 可选 | `pip install openpyxl`（Excel导出） |
| jinja2 | Python库 | 可选 | `pip install jinja2`（报告模板） |

### API Key 配置

| 数据源 | 环境变量 | 用途 |
|:-------|:---------|:-----|
| Wind | `WIND_API_KEY` | 中国市场财务数据 |
| Bloomberg | `BLOOMBERG_API_KEY` | 全球市场财务数据 |
| 同花顺 | `THS_API_KEY` | A股行情与基本面 |

5. 未配置外部数据源时，可手动导入财务数据进行分析
6. API Key存储在本地config.yaml，不会上传至任何服务器

### 可用性分类

7. **分类**: MD+EXEC（纯Markdown指令+Python脚本执行）
8. **说明**: 基于Markdown的AI Skill配合Python分析脚本，支持批量处理与自动化报告
9. **PRO版特性**: 批量分析、蒙特卡洛模拟、自动化报告生成、行业特化估值模型
10. **兼容性**: 完全兼容免费版全部技能与工作流

### 命令参数说明

11. `--format`: 命令参数,用于指定操作选项
12. `--output`: 命令参数,用于指定操作选项
13. `--skills`: 命令参数,用于指定操作选项
14. `-CN`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN`: 命令参数,用于指定操作选项

### 命令参数说明

- `-CN`: 命令参数,用于指定操作选项

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


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

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

### PRO企业级配置

```yaml
pro_config:
  workspace:
    root_dir: "./analysis_workspace"
    output_dir: "./reports"
    cache_dir: "./cache"

  data_sources:
    primary:
      provider: "wind"
      api_key: "${WIND_API_KEY}"
      cache_ttl: 3600
    secondary:
      provider: "bloomberg"
      api_key: "${BLOOMBERG_API_KEY}"

  analysis:
    batch:
      max_parallel: 10              # 最大并行分析数
      timeout: 300                  # 单标的超时（秒）
      retry: 3                      # 失败重试次数
    report:
      template_dir: "./templates"
      formats: ["pdf", "docx", "html"]
      language: "zh-CN"

  valuation:
    monte_carlo:
      simulations: 10000            # 蒙特卡洛模拟次数
      confidence_interval: [0.05, 0.95]
    sensitivity:
      variables: ["growth_rate", "discount_rate", "terminal_growth"]
      steps: 5                      # 每变量测试步数

  risk_models:
    fraud_detection:
      models: ["beneish_m_score", "piotroski_f_score", "altman_z_score"]
    stress_test:
      scenarios: ["base", "adverse", "severe"]
```

## 常见问题

### Q1：PRO版与免费版如何切换？

PRO版完全包含免费版全部技能。升级后原有分析工作流无需修改，直接运行即可获得增强结果。如需使用免费版行为，可在配置中关闭PRO增强选项。

### Q2：批量分析支持多少只标的？

PRO版支持单批次最多100只标的的并行分析。建议根据数据源API限额调整并行度，避免触发限流。批量结果自动汇总为对比矩阵并导出Excel。

### Q3：估值报告支持哪些格式？

支持PDF、DOCX、HTML三种格式。PDF适合正式提交，DOCX便于团队协作编辑，HTML适合在线展示。所有报告包含图表、敏感性矩阵和风险提示。

### Q4：蒙特卡洛模拟需要多长时间？

10000次模拟通常需要30-60秒（取决于标的复杂度和硬件性能）。可通过配置降低模拟次数（如1000次）进行快速预览，确认参数后运行完整模拟。

### Q5：如何接入Wind/Bloomberg等专业数据源？

在config.yaml的data_sources部分配置API凭证。PRO版支持自动数据拉取、缓存管理和限流控制。首次配置后，后续分析自动从指定数据源获取最新数据。

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
