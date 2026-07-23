---
slug: "finance-acct"
name: "finance-acct"
version: "1.0.0"
displayName: "财务会计专业版"
summary: "企业级财务会计系统，支持多账套、全税种、批量发票、ERP集成与审计追踪。"
license: "Proprietary"
edition: "pro"
description: |-
  面向中大型企业财务部门的全栈会计处理系统。支持多公司多账套管理、
  全税种自动计算、批量电子发票生成、银行API直连对账、ERP系统集成
  与完整审计追踪。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Finance
  - 会计记账
  - 企业级
  - 审计合规
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# 财务会计专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

### PRO版功能增强对比

| 功能模块 | 免费版 | PRO版 |
| --- | --- | --- |
| 账套数量 | 单账套 | 多账套+合并报表 |
| 币种支持 | 单币种 | 多币种+汇率转换 |
| 税种覆盖 | 增值税+所得税 | 全税种 |
| 发票处理 | 基础模板 | 批量生成+验真 |
| 银行对账 | CSV导入 | API直连 |
| 报表模板 | 基础三表 | 自定义+合并报表 |
| 审计追踪 | 无 | 完整操作日志 |
| ERP集成 | 无 | 主流ERP对接 |
| 团队协作 | 单用户 | 多角色权限 |

### 多账套管理
```yaml
accounts_sets:
  - id: "company_a"
    name: "母公司"
    currency: "CNY"
    standard: "CAS"           # 中国会计准则
    fiscal_year: "Jan-Dec"
  - id: "subsidiary_b"
    name: "子公司B"
    currency: "USD"
    standard: "IFRS"          # 国际准则
    fiscal_year: "Apr-Mar"
  - id: "subsidiary_c"
    name: "子公司C"
    currency: "EUR"
    standard: "IFRS"
    fiscal_year: "Jan-Dec"
```

**处理**: 按照skill规范执行多账套管理操作,遵循单一意图原则。
**输出**: 返回多账套管理的执行结果,包含操作状态和输出数据。### 全税种计算模块
| 税种 | 功能 | PRO版特性 |
| --- | --- | --- |
| 增值税 | 销项/进项/应纳 | 多税率自动适配 |
| 企业所得税 | 季度预缴/年度汇算 | 税务筹划建议 |
| 个人所得税 | 工资薪金/劳务 | 专项附加扣除 |
| 印花税 | 合同/产权 | 自动识别应税凭证 |
| 附加税 | 城建/教育费附加 | 联动增值税自动计算 |

**输入**: 用户提供全税种计算模块所需的指令和必要参数。
**处理**: 按照skill规范执行全税种计算模块操作,遵循单一意图原则。
**输出**: 返回全税种计算模块的执行结果,包含操作状态和输出数据。
### 功能模块

执行功能模块操作,处理用户输入并返回结果。

**输入**: 用户提供功能模块所需的参数和指令。

**输出**: 返回功能模块的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`功能模块`相关配置参数进行设置
#
## 适用场景

### 场景一：集团合并报表

用户输入："生成集团合并资产负债表"

```bash
# 合并多子公司报表
python finance_pro.py consolidate \
  --parent "company_a" \
  --subsidiaries "subsidiary_b,subsidiary_c" \
  --period 2026-Q2 \
  --report balance-sheet \
  --eliminate intercompany \
  --output consolidated_balance_sheet.pdf

# 输出包含：
# - 合并资产负债表
# - 少数股东权益计算
# - 内部交易抵消明细
# - 汇率转换差异表
```

### 场景二：批量发票处理

用户输入："批量生成本月销售发票"

```bash
# 批量生成电子发票
python finance_pro.py invoice batch-create \
  --source sales_records.csv \
  --template "vat_special" \
  --output "./invoices/" \
  --verify                    # 自动验真

# 输出：
# - 批量PDF发票
# - 发票明细汇总Excel
# - 验真结果报告
```

### 场景三：银行API实时对账

用户输入："自动获取银行流水并对账"

```bash
# 银行API直连获取流水
python finance_pro.py bank sync \
  --bank "icbc" \
  --account "6222详情见说明x" \
  --period 2026-02 \
  --auto-reconcile

# 生成对账报告
python finance_pro.py bank report \
  --output bank_reconciliation.pdf \
  --include-unmatched
```

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install finance-pro

# 初始化多账套
python finance_pro.py init \
  --config pro_config.yaml \
  --migrate-from free         # 从免费版迁移数据
```

### 多账套操作

```bash
# 切换账套
python finance_pro.py use --set "company_a"

# 跨账套查询
python finance_pro.py query \
  --sets "company_a,subsidiary_b" \
  --report "revenue_comparison"
```

### ERP集成

```python
from finance_pro import ERPConnector

# 对接SAP
sap = ERPConnector("sap", config=sap_config)
sap.sync_accounts()        # 同步科目
sap.sync_vouchers()        # 同步凭证
sap.sync_statements()      # 同步报表

# 对接用友
yonyou = ERPConnector("yonyou", config=yonyou_config)
yonyou.import_vouchers("vouchers.csv")
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+
- **数据库**: `PostgreSQL` 12+ 或 MySQL 8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| psycopg2 | Python库 | 必需 | `pip install psycopg2-binary`（`PostgreSQL`驱动） |
| sqlalchemy | Python库 | 必需 | `pip install sqlalchemy` |
| openpyxl | Python库 | 必需 | `pip install openpyxl`（Excel处理） |
| reportlab | Python库 | 可选 | `pip install reportlab`（PDF生成） |
| requests | Python库 | 必需 | `pip install requests`（API调用） |

### API Key 配置

| 服务 | 环境变量 | 用途 |
|:-------|:---------|:-----|
| 工商银行API | `ICBC_API_KEY` | 银行流水直连 |
| 招商银行API | `CMB_API_KEY` | 银行流水直连 |
| SAP ERP | `SAP_API_KEY` | ERP集成 |
| 用友ERP | `YONYOU_API_KEY` | ERP集成 |
| 汇率数据 | `FOREX_API_KEY` | 多币种汇率 |

- 所有凭证存储在本地配置文件，加密存储
- 数据库连接使用SSL加密传输

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本+数据库执行）
- **说明**: 企业级财务会计系统，支持多账套、多币种、多用户协作
- **PRO版特性**: 多账套合并、全税种计算、银行API直连、ERP集成、审计追踪
- **兼容性**: 完全兼容免费版数据格式与工作流，支持一键迁移

## 案例展示

### PRO企业级配置

```yaml
pro_config:
  database:
    type: "postgresql"          # 数据库类型
    host: "${DB_HOST}"
    port: 5432
    name: "finance_pro"
    pool_size: 20

  accounts:
    multi_set: true
    consolidation: true
    intercompany_elimination: true
    currency:
      base: "CNY"
      rate_source: "state_admin_foreign_exchange"
      rate_cache_ttl: 3600

  tax:
    full_coverage: true
    auto_planning: true
    declarations:
      vat: "monthly"
      income_tax: "quarterly"
      individual_income_tax: "monthly"
      stamp_duty: "as_needed"

  invoice:
    batch_enabled: true
    e_invoice: true
    verify: true
    templates: ["vat_special", "vat_normal", "electronic"]

  bank:
    api_enabled: true
    connections:
      - bank: "icbc"
        api_key: "${ICBC_API_KEY}"
      - bank: "cmb"
        api_key: "${CMB_API_KEY}"

  audit:
    enabled: true
    log_all_operations: true
    retention_days: 2555        # 7年留存

  erp:
    integration: true
    connectors: ["sap", "yonyou", "kingdee"]

  team:
    multi_user: true
    roles:
      - name: "accountant"
        permissions: ["record", "report"]
      - name: "manager"
        permissions: ["approve", "audit"]
      - name: "admin"
        permissions: ["all"]
```

## 常见问题

### Q1：如何从免费版迁移到PRO版？

PRO版提供一键迁移工具。运行 `python finance_pro.py init --migrate-from free` 即可自动将免费版的账套数据、科目设置和历史记录迁移至PRO版数据库。

### Q2：合并报表支持哪些准则？

PRO版支持中国会计准则（CAS）和国际财务报告准则（IFRS）的合并报表编制。可处理母子公司间内部交易抵消、少数股东权益计算和汇率转换差异。

### Q3：银行API直连支持哪些银行？

目前支持工商银行、招商银行、建设银行、中国银行等主要商业银行的API直连。需向对应银行申请企业网银API权限。未支持的银行可继续使用CSV导入方式。

### Q4：审计日志保存多久？

PRO版默认保存7年操作日志（2555天），满足税务与审计合规要求。日志内容包括操作人、操作时间、操作类型、变更前后数据等完整信息。

### Q5：支持多用户协作吗？

PRO版支持多用户协作，内置三种角色：会计（记账与报表）、经理（审批与审计）、管理员（全部权限）。所有操作关联具体用户，确保责任可追溯。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
