---
slug: university-app-tool-pro
name: university-app-tool-pro
version: "1.0.0"
displayName: 命理咨询专业版
summary: 专业命理分析系统，支持八字、紫微、合婚、大运流年与批量排盘。
license: MIT
edition: pro
description: |-
  面向命理研究者的专业命理分析系统。支持八字命理、紫微斗数、合婚
  分析、大运流年推演与批量排盘。内置命理案例库与术语词典，提供
  深度命盘解读与人生趋势分析。

  核心能力:
  - 八字命理深度分析（命盘/大运/流年）
  - 紫微斗数排盘与解读
  - 合婚分析（两人命盘匹配度）
  - 大运流年十年走势推演
  - 批量排盘与导出
  - 命理案例库与术语词典
  - 事业财运健康多维分析

  适用场景:
  - 专业命理研究与咨询
  - 命理文化深度学习
  - 批量排盘服务
  - 命理教学辅助
  - 传统文化研究

  差异化:
  - 兼容免费版八字命理功能，无缝升级
  - 新增紫微斗数与合婚分析
  - 大运流年深度推演
  - 批量排盘与导出
  - 命理案例库与术语词典

  触发关键词: 命理, 八字, 紫微斗数, 合婚, 大运, 流年, 批量排盘, 命盘, 运势, destiny, bazi, ziwei
tags:
- Finance
- 命理文化
- 传统文化
- 专业版
tools:
- read
- exec
---

# 命理咨询专业版（PRO版）

## 概述

本系统为命理研究者和专业用户提供全功能的命理分析能力。相比免费版，PRO版新增紫微斗数、合婚分析、大运流年推演、批量排盘和命理案例库等高级功能，全面满足专业命理研究与咨询的复杂需求。

PRO版完全兼容免费版八字命理功能，升级后原有命盘数据可直接迁移。

## 核心能力

### PRO版功能增强对比

| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 命理体系 | 仅八字 | 八字+紫微斗数 |
| 合婚分析 | 不支持 | 完整合婚报告 |
| 大运流年 | 不支持 | 十年走势推演 |
| 批量排盘 | 不支持 | CSV批量导入 |
| 案例库 | 不支持 | 历史案例参考 |
| 术语词典 | 基础 | 完整专业词典 |
| 分析维度 | 性格+运势 | +事业+财运+健康 |
| 报告导出 | 文本 | PDF/HTML格式 |

### 支持的命理体系

| 体系 | 功能 | PRO版特性 |
| --- | --- | --- |
| 八字命理 | 四柱排盘+大运流年 | 深度分析 |
| 紫微斗数 | 十二宫排盘+星曜解读 | 完整命盘 |
| 合婚分析 | 两人命盘匹配度 | 匹配评分 |
| 奇门遁甲 | 基础排盘 | 时局分析 |
| 风水方位 | 方位吉凶 | 简要参考 |

## 使用场景

### 场景一：紫微斗数排盘

用户输入："帮我排紫微斗数命盘"

```bash
# 紫微斗数排盘
python3 scripts/ziwei.py chart \
  --year 1990 --month 5 --day 15 --hour 8 \
  --gender male \
  --output ziwei_chart.html

# 输出包含：
# - 十二宫位图
# - 主星副星分布
# - 化禄化权化科化忌
# - 各宫位解读
```

### 场景二：合婚分析

用户输入："分析我们两个人的命盘匹配度"

```bash
# 合婚分析
python3 scripts/match.py analyze \
  --person1 "1990-05-15 08:00 male" \
  --person2 "1992-08-20 14:00 female" \
  --output marriage_report.pdf

# 输出包含：
# - 八字匹配度评分
# - 五行互补分析
# - 日主相生相克
# - 合婚建议
```

### 场景三：批量排盘

用户输入："帮这20个人批量排八字"

```bash
# 批量排盘
python3 scripts/batch.py \
  --input people.csv \
  --output-dir ./charts/ \
  --format html \
  --parallel 5

# CSV格式：
# name,year,month,day,hour,gender
# 张三,1990,5,15,8,male
# 李四,1992,8,20,14,female
```

## 快速开始

### PRO版初始化

```bash
# 安装PRO版依赖
pip install -r requirements_pro.txt

# 初始化案例库
python3 scripts/init.py --load-cases
```

### 常用命令

```bash
# 紫微斗数
python3 scripts/ziwei.py chart --year 1990 --month 5 --day 15 --hour 8 --gender male

# 合婚分析
python3 scripts/match.py analyze --person1 "1990-05-15 08:00 male" --person2 "1992-08-20 14:00 female"

# 大运流年
python3 scripts/bazi.py dayun --year 1990 --month 5 --day 15 --hour 8 --gender male

# 批量排盘
python3 scripts/batch.py --input people.csv --output-dir ./charts/

# 案例查询
python3 scripts/cases.py search --keyword "富贵命"
```

## 配置示例

### PRO系统配置

```yaml
pro_config:
  systems:
    bazi:
      enabled: true
      dayun: true                  # 大运分析
      liunian: true                # 流年分析
    ziwei:
      enabled: true
      stars: "all"                 # 全星曜
      palaces: 12                  # 十二宫
    match:
      enabled: true
      scoring: true                # 匹配评分

  analysis:
    dimensions:
      - personality                # 性格
      - career                     # 事业
      - wealth                     # 财运
      - marriage                   # 婚姻
      - health                     # 健康
      - children                   # 子女
    depth: "professional"          # professional | basic

  batch:
    max_parallel: 5
    input_formats: ["csv", "excel"]
    output_formats: ["html", "pdf"]

  library:
    cases: true                    # 案例库
    dictionary: true               # 术语词典
    auto_reference: true           # 自动引用案例

  output:
    language: "zh-CN"
    template_dir: "./templates"
    include_explanation: true
```

## 最佳实践

### PRO版高级实践

| 实践领域 | 建议做法 |
| --- | --- |
| 综合分析 | 八字与紫微结合，交叉验证 |
| 合婚评估 | 不只看匹配度，结合实际相处 |
| 大运流年 | 关注大运转折点，提前规划 |
| 批量服务 | 确认数据准确后再批量处理 |
| 案例参考 | 相似命盘案例仅供参考，不可套用 |

### 免费版兼容性

```text
免费版命令 → PRO版命令（增强）：
bazi.py chart (基础排盘)  → +大运流年+深度解读
性格解读                  → +事业+财运+健康多维分析
单盘分析                  → 批量排盘+合婚分析
```

## 常见问题

### Q1：紫微斗数和八字有什么区别？

八字以天干地支四柱为基础，侧重五行生克；紫微斗数以星曜入十二宫为基础，侧重人生各领域细节。两者可互为补充，PRO版支持两种体系联合分析。

### Q2：合婚分析的准确率如何？

合婚分析基于命理学说，属于传统文化范畴，非科学预测。匹配度评分仅供参考，实际婚姻幸福取决于双方经营。不应作为婚恋决策的唯一依据。

### Q3：大运流年如何推演？

大运根据性别和年柱阴阳推排，每十年一运。流年按当年干支分析与大运、命盘的互动。PRO版提供十年大运走势图和年度流年详解。

### Q4：批量排盘支持多少人？

PRO版单批次支持最多100人的批量排盘。结果自动生成HTML/PDF格式命盘，便于查阅和分享。

### Q5：案例库包含什么内容？

案例库收录历史名人和典型命盘案例，包含命盘分析、人生轨迹与命理解读。仅供学习参考，不可直接套用至个人命盘。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| lunardate | Python库 | 必需 | `pip install lunardate`（农历） |
| sxtwl | Python库 | 必需 | `pip install sxtwl`（精确排盘） |
| pandas | Python库 | 可选 | `pip install pandas`（批量处理） |
| jinja2 | Python库 | 可选 | `pip install jinja2`（HTML模板） |

### API Key 配置

- PRO版无需外部API Key
- 所有命理计算在本地完成
- 案例库内置在系统中

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 专业命理分析系统，支持多体系分析与批量处理
- **PRO版特性**: 紫微斗数、合婚分析、大运流年、批量排盘、案例库
- **兼容性**: 完全兼容免费版八字命理功能
- **文化声明**: 内容仅供传统文化研究娱乐参考，不构成任何决策建议
