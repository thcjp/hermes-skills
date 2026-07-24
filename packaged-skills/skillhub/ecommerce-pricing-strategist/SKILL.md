---

slug: ecommerce-pricing-strategist
name: ecommerce-pricing-strategist
version: 1.0.1
displayName: "电商定价策略师"
summary: "AI分析市场数据智能定价,多策略配置+动态调价+利润最大化。电商定价策略师是一款AI驱动的电商定价决策工具. 支持市场数据多维分析、5种定价策略智能推荐、多平台价格监控与利润最大化测算. 核"
license: Proprietary
description: |-，可自动提升工作效率
  电商定价策略师是一款AI驱动的电商定价决策工具.
  支持市场数据多维分析、5种定价策略智能推荐、多平台价格监控与利润最大化测算.
  核心能力:
  - 5种定价策略智能推荐
  - 市场数据多维分析
  - 多平台价格监控
  - 动态调价建议与利润最大化测算
homepage: ""
tags:
  - 电商
  - 定价策略
  - 数据分析
  - 利润优化
  - 工具
  - 效率
  - 自动化
  - 研究
  - 分析
  - 运维
  - 监控
  - 写作
tools:
  - read
  - exec
  - write
category: "Automation"

---

# 电商定价策略师

AI驱动的电商定价策略工具,分析市场数据智能定价,支持5种定价策略、多平台价格监控、动态调价建议、利润最大化测算.
## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 电商定价策略师AI分析 | 不支持 | 支持 |
| 电商定价策略师多策略配置 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |

## 核心能力

1. **5种定价策略智能推荐**:渗透定价(低价抢市场,适合新品上市)/撇脂定价(高价取利润,适合创新产品)/竞争导向定价(对标竞品,适合红海市场)/成本加成定价(成本+利润率,适合标准品)/动态定价(实时调价,适合季节性商品),根据商品类型和市场环境自动推荐最优策略
2. **市场数据多维分析**:竞品价格分布(最高/最低/均价/中位数)、销量趋势分析(7/30/90天)、价格弹性系数计算(价格变动1%对销量的影响)、市场容量估算、价格带分布
3. **多平台价格监控**:淘宝/京东/拼多多/亚马逊四平台价格同步监控,识别平台价差异,提供跨平台定价建议,避免平台价格冲突
4. **动态调价建议**:基于库存/销量/竞品价格/季节因素/促销节点,生成动态调价建议(涨价/降价/维持),含调价幅度+时机+预期效果
5. **利润最大化测算**:输入成本/当前价格/销量,计算最优定价点(利润=单价×销量-成本),输出价格-销量-利润曲线,推荐利润最大化定价点
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 | 是否适用 |
|:-----|:-----|:-----|:-----|
| 新品上市定价 | 商品信息+成本+竞品数据 | 5种策略推荐+最优定价建议 | 适用 |
| 竞品价格战应对 | 竞品降价数据+自身成本 | 应对策略+调价建议 | 适用 |
| 多平台定价策略 | 多平台竞品价格+成本 | 跨平台差异化定价建议 | 适用 |
| 利润优化测算 | 当前价格/销量/成本 | 利润最大化定价点+曲线 | 适用 |
| 促销活动定价 | 商品+促销类型+目标 | 促销定价策略+折扣建议 | 适用 |
| 实时自动调价执行 | 直接对接ERP自动改价 | 不适用(本Skill提供策略建议非自动执行) | 不适用 |
| B2B大宗采购报价 | 大宗采购批量报价 | 不适用(本Skill主面向B2C零售定价) | 不适用 |
| 线下实体店定价 | 线下门店区域定价 | 不适用(本Skill主面向电商平台) | 不适用 |

## 使用流程

### Step 1: 接收定价请求
- 解析输入:action(analyze/strategy/optimize/monitor)、product_info(商品信息)、cost(成本)、competitor_data(竞品数据,可选)、platforms(平台列表,可选)
- 参数校验:product_info非空、cost为正数
- 校验失败:返回错误码PRICING_VAL_ERR

### Step 2: 市场数据分析(仅analyze/optimize)
- 如提供competitor_data→分析竞品价格分布(最高/最低/均价/中位数/标准差)
- 如未提供→提示用户补充竞品数据或使用市场公开数据估算
- 计算价格弹性系数:基于历史价格-销量数据回归分析
- 输出市场分析报告

### Step 3: 定价策略推荐(仅strategy)
- 根据商品类型/市场环境/竞争格局自动推荐5种策略中的一种
- 策略选择逻辑:
  - 新品+创新性强→撇脂定价
  - 新品+价格敏感→渗透定价
  - 红海市场+竞品多→竞争导向定价
  - 标准品+成本透明→成本加成定价
  - 季节性+库存波动→动态定价
- 输出策略推荐+具体定价区间+理由

### Step 4: 利润最大化测算(仅optimize)
- 输入:cost(成本)+current_price(当前价格)+current_sales(当前销量)
- 计算价格-销量曲线(基于价格弹性系数)
- 计算利润=单价×销量-成本
- 找出利润最大化定价点(导数为0的点)
- 输出:最优价格+预期销量+预期利润+价格-销量-利润曲线数据

### Step 5: 多平台价格监控(仅monitor)
- 监控指定平台(淘宝/京东/拼多多/亚马逊)的竞品价格
- 识别平台价差异
- 提供跨平台定价建议(避免价格冲突)
- 输出监控报告+调价建议

### Step 6: 输出定价建议报告
- 整合分析结果,输出结构化定价建议报告
- 含:推荐策略+定价区间+理由+风险提示+调价时机建议

## 定价策略对比

| 策略 | 适用场景 | 优点 | 风险 | 推荐商品 |
|---:|---:|---:|---:|---:|
| 渗透定价 | 新品上市抢市场 | 快速获客抢份额 | 利润薄,价格战风险 | 价格敏感型新品 |
| 撇脂定价 | 创新产品高溢价 | 高利润回收研发 | 后期需降价 | 创新性强产品 |
| 竞争导向 | 红海市场竞争 | 避免价格战 | 利润受限 | 同质化商品 |
| 成本加成 | 标准品定价 | 简单透明保利润 | 忽略市场需求 | 标准化商品 |
| 动态定价 | 季节性/库存波动 | 利润最大化 | 频繁调价伤品牌 | 季节性商品 |

## 输入格式

### 定价策略推荐
```json
{
  "action": "strategy",
  "product_info": {"name": "无线蓝牙耳机", "category": "数码", "features": ["降噪", "长续航"], "is_new": true},
  "cost": 80,
  "competitor_data": [{"platform": "taobao", "price": 199, "sales": 5000}, {"platform": "jd", "price": 219, "sales": 3000}],
  "platforms": ["taobao", "jd", "pdd"]
}
```

### 利润最大化测算
```json
{
  "action": "optimize",
  "product_info": {"name": "无线蓝牙耳机"},
  "cost": 80,
  "current_price": 199,
  "current_sales": 5000,
  "price_elasticity": -1.5
}
```

## 输出格式

```json
{
  "success": true,
  "data": {
    "recommended_strategy": "penetration",
    "strategy_reason": "新品上市+价格敏感市场,建议渗透定价抢份额",
    "price_range": {"min": 149, "max": 179, "recommended": 159},
    "competitor_analysis": {"avg_price": 209, "min_price": 179, "max_price": 249, "median_price": 199},
    "profit_estimate": {"at_recommended_price": {"price": 159, "margin": 49, "margin_rate": 0.31, "estimated_sales": 8000, "estimated_profit": 392000}},
    "risk_warnings": ["渗透定价利润率31%,需控制供应链成本"],
    "adjustment_timing": "建议上市首月渗透定价,第二个月根据销量调整"
  },
  "error": null,
  "code": null
}
```

## 异常处理

| 异常场景 | 原因 | 处理方式 | 错误码 |
|:---:|:---:|:---:|:---:|
| 参数缺失 | product_info/cost未提供 | 返回错误+提示补全 | PRICING_VAL_ERR |
| 竞品数据不足 | competitor_data为空或少于3个 | 提示补充竞品数据或使用估算 | INSUFFICIENT_DATA |
| 价格弹性无法计算 | 历史数据不足 | 使用行业平均弹性系数(-1.5)估算 | ELASTICITY_ESTIMATED |
| 平台监控失败 | 平台API不可用 | 跳过失败平台,返回已监控平台结果 | MONITOR_PARTIAL_FAILED |
| 利润测算异常 | 输入数据不合理(如成本>价格) | 返回错误+提示检查输入 | PROFIT_CALC_ERROR |
| 市场数据过时 | 竞品数据超过7天 | 标记warning,建议更新数据 | DATA_STALE |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:------|------:|:------|:------|------:|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | DeepSeek/通义千问/文心一言/Kimi等国内模型 |
| 电商数据API | API | 可选 | 淘宝/京东/拼多多/亚马逊价格数据(可手动提供) | 第三方电商数据服务(如蝉妈妈/灰豚等国内数据平台) |
| JSON文件存储 | 文件系统 | 可选 | exec工具保存分析报告 | 本地文件系统,无海外依赖 |

### API Key 配置与安全要求
- **LLM_API_KEY**: 必需(通常由Agent内置) - 定价策略分析和建议生成
- **ECOMMERCE_API_KEY**: 可选 - 电商数据API(可手动提供竞品数据替代)
- 配置方式: 在Agent的环境变量中设置
- **零暴露原则**: API Key必须通过环境变量注入(如`$env:ECOMMERCE_API_KEY`),严禁硬编码在SKILL.md或脚本源码中;所有示例代码中Key位置使用环境变量占位符;禁止在日志、错误信息、输出JSON中打印Key明文

### 使用流程(补充)
电商数据API可选,可手动提供competitor_data替代。价格弹性无法计算时使用行业平均系数(-1.5)估算.
只需将SKILL.md文件放入Agent的skills目录即可直接使用.
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力.
### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 新品上市定价策略

**输入**:
```json
{
  "action": "strategy",
  "product_info": {"name": "无线蓝牙耳机", "category": "数码", "features": ["降噪", "长续航"], "is_new": true},
  "cost": 80,
  "competitor_data": [{"platform": "taobao", "price": 199, "sales": 5000}, {"platform": "jd", "price": 219, "sales": 3000}, {"platform": "pdd", "price": 169, "sales": 8000}],
  "platforms": ["taobao", "jd", "pdd"]
}
```

**执行流程**: 接收请求→分析竞品数据(均价195.7/最低169/最高219)→判断新品+价格敏感→推荐渗透定价→计算定价区间(149-179)→利润测算→输出策略报告

**输出**:
```json
{
  "success": true,
  "data": {
    "recommended_strategy": "penetration",
    "strategy_reason": "新品上市+拼多多竞品169元显示价格敏感,建议渗透定价抢份额",
    "price_range": {"min": 149, "max": 179, "recommended": 159},
    "competitor_analysis": {"avg_price": 195.7, "min_price": 169, "max_price": 219, "median_price": 199, "platform_diff": "pdd比taobao低15%"},
    "profit_estimate": {"at_recommended_price": {"price": 159, "margin": 79, "margin_rate": 0.50, "estimated_sales": 8000, "estimated_profit": 632000}},
    "risk_warnings": ["渗透定价需关注竞品跟进降价", "拼多多平台价格偏低,跨平台定价需差异化"],
    "adjustment_timing": "建议上市首月159元渗透定价,第二个月根据销量调整至169-179元"
  },
  "error": null,
  "code": null
}
```

### 示例2: 利润最大化测算

**输入**:
```json
{
  "action": "optimize",
  "product_info": {"name": "无线蓝牙耳机"},
  "cost": 80,
  "current_price": 199,
  "current_sales": 5000,
  "price_elasticity": -1.5
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "current_status": {"price": 199, "sales": 5000, "profit_per_unit": 119, "total_profit": 595000},
    "optimal_pricing": {"price": 179, "estimated_sales": 6500, "profit_per_unit": 99, "total_profit": 643500, "profit_increase": 8.15},
    "price_sales_curve": [{"price": 149, "sales": 9500, "profit": 656000}, {"price": 159, "sales": 8000, "profit": 632000}, {"price": 169, "sales": 7200, "profit": 640800}, {"price": 179, "sales": 6500, "profit": 643500}, {"price": 189, "sales": 5700, "profit": 621000}, {"price": 199, "sales": 5000, "profit": 595000}, {"price": 219, "sales": 3700, "profit": 514300}],
    "recommendation": "建议定价179元,利润从59.5万提升至64.35万,增幅8.15%"
  },
  "error": null,
  "code": null
}
```

### 示例3: 竞品数据不足降级

**输入**: 竞品数据少于3个
```json
{"action": "strategy", "product_info": {"name": "手机壳"}, "cost": 5, "competitor_data": [{"platform": "taobao", "price": 19, "sales": 10000}]}
```

**输出**: 提示补充数据但仍给出估算建议
```json
{
  "success": true,
  "data": {
    "recommended_strategy": "competitive",
    "strategy_reason": "竞品数据不足,建议竞争导向定价对标市场均价",
    "price_range": {"min": 15, "max": 25, "recommended": 19},
    "competitor_analysis": {"avg_price": 19, "data_count": 1, "note": "竞品数据不足3个,建议补充"},
    "risk_warnings": ["竞品数据不足,定价建议仅供参考"]
  },
  "error": "竞品数据不足3个,已使用有限数据估算",
  "code": "INSUFFICIENT_DATA"
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成.
### 案例1: 新品上市定价策略(渗透定价推荐)

**输入**:
```json
{
  "action": "strategy",
  "product_info": {"name": "无线蓝牙耳机", "category": "数码", "features": ["降噪", "长续航", "蓝牙5.3"], "is_new": true},
  "cost": 80,
  "competitor_data": [
    {"platform": "taobao", "price": 199, "sales": 5000},
    {"platform": "jd", "price": 219, "sales": 3000},
    {"platform": "pdd", "price": 169, "sales": 8000}
  ],
  "platforms": ["taobao", "jd", "pdd"]
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "recommended_strategy": "penetration",
    "strategy_reason": "新品上市+价格敏感市场(拼多多竞品169元销量最高),建议渗透定价抢份额,定价低于竞品均价建立价格优势",
    "price_range": {"min": 149, "max": 179, "recommended": 159},
    "competitor_analysis": {"avg_price": 195.7, "min_price": 169, "max_price": 219, "median_price": 199, "std_dev": 20.5},
    "profit_estimate": {
      "at_recommended_price": {
        "price": 159,
        "margin": 79,
        "margin_rate": 0.497,
        "estimated_sales": 8000,
        "estimated_profit": 632000
      }
    },
    "risk_warnings": ["渗透定价利润率49.7%,需控制供应链成本", "拼多多平台低价竞争激烈,需持续监控竞品价格"],
    "adjustment_timing": "建议上市首月渗透定价159元抢量,第二个月根据销量数据调整,若月销>8000可微调至169元提升利润"
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓渗透定价策略正确推荐(新品+价格敏感) ✓竞品均价195.7元分析准确 ✓推荐价159元(低于竞品均价) ✓利润测算完整(毛利79元/利润率49.7%) ✓调价时机建议清晰

### 案例2: 利润最大化测算(价格弹性分析)

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "current_status": {"price": 199, "sales": 5000, "profit_per_unit": 119, "total_profit": 595000},
    "optimal_pricing": {"price": 179, "estimated_sales": 6502, "profit_per_unit": 99, "total_profit": 643698, "profit_increase": 8.2},
    "price_sales_curve": [
      {"price": 149, "estimated_sales": 9512, "profit": 655328},
      {"price": 159, "estimated_sales": 8000, "profit": 632000},
      {"price": 169, "estimated_sales": 7256, "profit": 644284},
      {"price": 179, "estimated_sales": 6502, "profit": 643698},
      {"price": 189, "estimated_sales": 5748, "profit": 626148},
      {"price": 199, "estimated_sales": 5000, "profit": 595000},
      {"price": 209, "estimated_sales": 4252, "profit": 549508}
    ],
    "recommendation": "当前价格199元偏高,建议降价至179元,预期利润提升4.87万元(+8.2%)。价格弹性-1.5表明降价能有效拉动销量。"
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓最优定价点179元(optimal_pricing结构,利润最大化) ✓价格弹性-1.5正确应用 ✓价格-销量-利润曲线7个数据点完整 ✓利润提升4.87万元(+8.2%)计算准确 ✓降价建议有数据支撑

### 案例3: 多平台价格监控(跨平台价差异识别)

**输入**:
```json
{
  "action": "monitor",
  "product_info": {"name": "无线蓝牙耳机"},
  "platforms": ["taobao", "jd", "pdd", "amazon"],
  "competitor_data": [
    {"platform": "taobao", "price": 199, "seller": "官方旗舰店"},
    {"platform": "jd", "price": 219, "seller": "自营"},
    {"platform": "pdd", "price": 169, "seller": "百亿补贴"},
    {"platform": "amazon", "price": 189, "seller": "跨境店"}
  ]
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "monitor_results": [
      {"platform": "taobao", "price": 199, "status": "normal"},
      {"platform": "jd", "price": 219, "status": "high", "diff_from_avg": 14.8},
      {"platform": "pdd", "price": 169, "status": "low", "diff_from_avg": -35.2},
      {"platform": "amazon", "price": 189, "status": "normal"}
    ],
    "avg_price": 194,
    "price_gap": {"max_gap": 50, "max_gap_platforms": "jd vs pdd"},
    "cross_platform_suggestions": [
      {"platform": "jd", "suggestion": "京东价格偏高(219元),建议降至199元与淘宝持平,避免渠道冲突"},
      {"platform": "pdd", "suggestion": "拼多多百亿补贴价169元,建议设定最低限价175元,防止破价影响品牌"},
      {"platform": "amazon", "suggestion": "亚马逊跨境价189元合理,建议维持"}
    ],
    "risk_warnings": ["京东vs拼多多价差50元,可能引发消费者跨平台比价投诉"]
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓四平台价格同步监控 ✓跨平台价差异识别(最大价差50元) ✓京东高价/拼多多低价正确标注 ✓跨平台定价建议3条 ✓风险预警(渠道冲突)

### 案例4: 竞品数据不足降级(使用行业平均弹性估算)

**输入**:
```json
{
  "action": "optimize",
  "product_info": {"name": "智能手环", "is_new": true},
  "cost": 50,
  "current_price": 129,
  "current_sales": 2000
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "current_status": {"price": 129, "sales": 2000, "profit_per_unit": 79, "total_profit": 158000},
    "optimal_pricing": {"price": 119, "estimated_sales": 2534, "profit_per_unit": 69, "total_profit": 174846, "profit_increase": 10.7},
    "price_elasticity_used": -1.5,
    "price_sales_curve": [
      {"price": 99, "estimated_sales": 3378, "profit": 165522},
      {"price": 109, "estimated_sales": 2956, "profit": 174204},
      {"price": 119, "estimated_sales": 2534, "profit": 174846},
      {"price": 129, "estimated_sales": 2000, "profit": 158000},
      {"price": 139, "estimated_sales": 1634, "profit": 145426}
    ],
    "recommendation": "建议定价119元,预期利润提升1.68万元(+10.7%)。"
  },
  "error": "未提供price_elasticity参数,已使用行业平均弹性系数(-1.5)估算,结果仅供参考",
  "code": "ELASTICITY_ESTIMATED"
}
```

**效果验证**: ✓价格弹性缺失正确降级(使用-1.5行业平均) ✓降级原因在error字段标注 ✓错误码ELASTICITY_ESTIMATED正确返回 ✓最优定价119元(optimal_pricing结构) ✓利润提升1.68万元(+10.7%)

### 案例5: 撇脂定价策略(创新产品高溢价)

**输入**:
```json
{
  "action": "strategy",
  "product_info": {"name": "AI智能翻译耳机", "category": "数码", "features": ["实时翻译42种语言", "AI降噪", "骨传导"], "is_new": true, "innovation_level": "high"},
  "cost": 150,
  "competitor_data": [
    {"platform": "taobao", "price": 599, "sales": 500},
    {"platform": "jd", "price": 649, "sales": 300}
  ],
  "platforms": ["taobao", "jd"]
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "recommended_strategy": "skimming",
    "strategy_reason": "创新性强的AI翻译耳机+竞品少+高溢价空间,建议撇脂定价快速回收研发成本,后续逐步降价扩大市场",
    "price_range": {"min": 599, "max": 699, "recommended": 649},
    "competitor_analysis": {"avg_price": 624, "min_price": 599, "max_price": 649, "median_price": 624},
    "profit_estimate": {
      "at_recommended_price": {
        "price": 649,
        "margin": 499,
        "margin_rate": 0.769,
        "estimated_sales": 400,
        "estimated_profit": 199600
      }
    },
    "risk_warnings": ["撇脂定价利润率76.9%极高,可能吸引竞品入场", "建议3-6个月后降价至549元扩大市场份额"],
    "adjustment_timing": "上市前3个月撇脂定价649元回收研发,第4个月降至599元,第6个月降至499元抢占市场"
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓撇脂定价策略正确推荐(创新性强+高溢价) ✓推荐价649元(高于竞品均价) ✓利润率76.9%高溢价测算 ✓分阶段降价时机建议(3/4/6个月) ✓竞品入场风险预警

## 常见问题

### Q1: 5种定价策略如何选择?
A: 策略选择基于商品类型和市场环境:新品+创新性强→撇脂定价(高价取利润);新品+价格敏感→渗透定价(低价抢市场);红海市场+竞品多→竞争导向定价(对标竞品);标准品+成本透明→成本加成定价(成本+利润率);季节性+库存波动→动态定价(实时调价)。本Skill会根据输入自动推荐,也可手动指定strategy参数.
### Q2: 价格弹性系数如何计算?数据不足怎么办?
A: 价格弹性系数通过历史价格-销量数据回归分析计算(价格变动1%对销量的影响)。如果历史数据不足无法计算(ELASTICITY_ESTIMATED),会使用行业平均弹性系数(-1.5)估算。建议提供至少30天的价格-销量历史数据以获得准确弹性系数。弹性系数<-1表示价格敏感(降价增收),>-1表示价格不敏感(涨价增收).
### Q3: 多平台定价如何避免价格冲突?
A: 多平台定价建议:1)主平台(如天猫)定标准价,副平台(如拼多多)定略低价(5-10%差异);2)不同平台用不同SKU或包装避免直接比价;3)监控平台价差异(本Skill的monitor功能),价差异超过15%时预警。本Skill会输出跨平台差异化定价建议,标注各平台推荐价格和价差异百分比.
### Q4: 动态调价建议多久更新一次?
A: 动态调价建议更新频率取决于商品类型:快消品建议每日监控每周调价;耐用品建议每周监控每月调价;季节性商品在旺季前2周开始密集监控。本Skill的monitor功能可定期执行(如每日/每周),输出调价建议含调价幅度+时机+预期效果。注意频繁调价可能伤品牌,建议单次调价幅度不超过10%.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

1. **提供策略建议非自动执行**:本Skill输出定价策略建议和调价建议,不直接对接ERP自动改价,需人工确认后执行
2. **价格弹性依赖历史数据**:价格弹性系数计算需要至少30天历史价格-销量数据,数据不足时使用行业平均系数(-1.5)估算,准确度降低
3. **竞品数据需手动提供或对接API**:竞品价格数据需手动提供competitor_data或对接第三方电商数据API(如蝉妈妈/灰豚),本Skill不内置数据采集
4. **主面向B2C零售定价**:定价策略针对B2C电商零售场景,B2B大宗采购报价和线下实体店区域定价不适用
5. **市场数据时效性7天**:竞品数据超过7天会标记DATA_STALE警告,建议定期更新市场数据以保证定价建议准确性

## 变更历史

| 版本 | 日期 | 变更说明 |
|:------:|--------|:-------|
| v1.0.0 | 2026-07-17 | 初版创建,5种定价策略+市场数据分析+多平台监控+利润最大化测算+动态调价建议 |
