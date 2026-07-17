---
slug: quant-data-quality
name: quant-data-quality
version: "1.0.0"
displayName: Quant Data Quality
summary: 数据质量检查技能。当用户说\
license: MIT-0
description: |-
  数据质量检查技能。当用户说\

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 当用户说, 技能, quant, quality, data, 数据质量检查
tags: '[''Productivity'']'
tools: '[read, exec]'
---

# Quant Data Quality

> 版本：1.0.0
> 适用项目：量化策略项目

---

## 🎯 检查目标

**确保数据完整性、准确性、一致性、时效性**

---

## 📋 数据质量检查清单

### 1. 数据完整性

#### 1.1 价格数据完整性

**检查项**：

* 数据量是否充足？（股票数 × 交易日数）
* 是否有缺失日期？
* 是否有缺失股票？

**检查方法**：

```python
import pandas as pd

price = pd.read_parquet('data/integrated/price_integrated.parquet')

print(f"记录数: {len(price)}")
print(f"股票数: {price['code'].nunique()}")
print(f"日期范围: {price['date'].min()} ~ {price['date'].max()}")

dates = pd.to_datetime(price['date'].unique())
all_dates = pd.date_range(start=dates.min(), end=dates.max(), freq='B')  # 工作日
missing_dates = set(all_dates) - set(dates)
print(f"缺失日期: {len(missing_dates)}")
```

---

#### 1.2 因子数据完整性

**检查项**：

* 因子数量是否合理？
* 是否有大量nan值？
* 是否有极端值？

**检查方法**：

```python
import pandas as pd
import numpy as np

factors = pd.read_parquet('data/factors_v2/alphagbm_rolling_factors_active.parquet')

nan_count = factors.isna().sum().sum()
total_count = factors.size
nan_ratio = nan_count / total_count
print(f"nan值数量: {nan_count:,}")
print(f"nan值比例: {nan_ratio:.2%}")

for col in factors.select_dtypes(include=[np.number]).columns:
    q1 = factors[col].quantile(0.01)
    q99 = factors[col].quantile(0.99)
    extreme_count = ((factors[col] < q1) | (factors[col] > q99)).sum()
    print(f"{col}: 极端值数量 {extreme_count}")
```

---

#### 1.3 信号数据完整性

**检查项**：

* 信号数量是否合理？
* 信号日期是否最新？
* 信号股票是否在股票池内？

---

### 2. 数据准确性

#### 2.1 价格数据准确性

**检查项**：

* 是否有零价格？
* 是否有负价格？
* 是否有异常收益率（>20%）？

**检查方法**：

```python
zero_price = price[price['close'] == 0]
print(f"零价格记录: {len(zero_price)}")

neg_price = price[price['close'] < 0]
print(f"负价格记录: {len(neg_price)}")

price['return'] = price.groupby('code')['close'].pct_change()
abnormal_return = price[abs(price['return']) > 0.2]
print(f"异常收益率记录: {len(abnormal_return)}")
```

---

#### 2.2 因子数据准确性

**检查项**：

* 是否有inf值？
* 是否有极端值（>1e10）？
* 因子分布是否合理？

**检查方法**：

```python
import numpy as np

inf_count = np.isinf(factors.select_dtypes(include=[np.number])).sum().sum()
print(f"inf值数量: {inf_count}")

extreme_count = (abs(factors.select_dtypes(include=[np.number])) > 1e10).sum().sum()
print(f"极端值数量: {extreme_count}")
```

---

### 3. 数据一致性

#### 3.1 价格-成交量一致性

**检查项**：

* 零成交量比例是否合理？
* 价格-成交量时间是否对齐？

**检查方法**：

```python
zero_volume = price[price['volume'] == 0]
print(f"零成交量记录: {len(zero_volume)}")
print(f"零成交量比例: {len(zero_volume) / len(price):.2%}")
```

---

#### 3.2 跨源数据一致性

**检查项**：

* 不同数据源的价格是否一致？
* 不同数据源的日期范围是否一致？

---

### 4. 数据时效性

#### 4.1 价格数据时效性

**检查项**：

* 最新数据日期？
* 滞后天数？

**检查方法**：

```python
from datetime import datetime

latest_date = pd.to_datetime(price['date'].max())
today = datetime.now()
lag = (today - latest_date).days
print(f"最新日期: {latest_date}")
print(f"滞后天数: {lag}")
```

---

#### 4.2 因子数据时效性

**检查项**：

* 因子更新频率？
* 因子滞后天数？

---

## 🔍 常见数据问题

### 问题1：价格数据缺失

**表现**：

* 某些日期没有数据
* 某些股票没有数据

**原因**：

* 数据源问题
* 爬虫失败
* 停牌

**解决方案**：

* ✅ 使用多数据源
* ✅ 定期检查数据完整性
* ✅ 建立数据更新告警

---

### 问题2：因子数据大量nan

**表现**：

* 因子列有很多nan值

**原因**：

* 计算窗口不足
* 数据源缺失
* 计算逻辑错误

**解决方案**：

* ✅ 检查计算窗口
* ✅ 填充缺失值
* ✅ 修复计算逻辑

---

### 问题3：因子极端值

**表现**：

* 因子值异常大或异常小

**原因**：

* 除零错误
* 计算逻辑错误
* 数据质量问题

**解决方案**：

* ✅ Winsorize处理
* ✅ 检查计算逻辑
* ✅ 过滤极端值

---

### 问题4：信号过期

**表现**：

* 信号日期滞后很久

**原因**：

* 信号生成任务未运行
* 数据更新任务未运行

**解决方案**：

* ✅ 检查cron任务
* ✅ 建立更新告警
* ✅ 手动触发更新

---

## 📊 数据质量报告模板

```markdown

**检查日期**：YYYY-MM-DD

---

## 一、数据概览

| 数据类型 | 记录数 | 股票数 | 日期范围 | 滞后天数 |
|---------|--------|--------|---------|---------|
| 价格数据 | 1.16M | 525 | 2015-2026 | 1 |
| 因子数据 | 991K | 525 | 2020-2026 | 17 |
| 信号数据 | 10 | 10 | 2026-03-27 | 0 |

---

## 二、数据质量评分

| 维度 | 评分 | 说明 |
|------|------|------|
| 完整性 | 100/100 | 数据完整 |
| 准确性 | 100/100 | 无异常值 |
| 一致性 | 100/100 | 跨源一致 |
| 时效性 | 70/100 | 因子滞后17天 |

**总评分**：92.5/100

---

## 三、问题清单

| 问题 | 严重程度 | 建议 |
|------|---------|------|
| 因子数据滞后 | 中 | 下周一更新 |

---

*检查人：Skill平台 Assistant*
*日期：YYYY-MM-DD*
```

---

## 🚫 禁止事项

1. ❌ 使用未经检查的数据
2. ❌ 忽略数据质量问题
3. ❌ 没有数据质量报告

---

*技能版本：1.0.0*

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
