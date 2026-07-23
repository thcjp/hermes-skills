---
slug: "university-app"
name: "university-app"
version: "1.0.0"
displayName: "命理咨询专业版"
summary: "专业命理分析系统，支持八字、紫微、合婚、大运流年与批量排盘。"
license: "Proprietary"
edition: "pro"
description: |-
  面向命理研究者的专业命理分析系统。支持八字命理、紫微斗数、合婚
  分析、大运流年推演与批量排盘。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
  - Finance
  - 命理文化
  - 传统文化
  - 专业版
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# 命理咨询专业版

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

**输入**: 用户提供PRO版功能增强对比所需的指令和必要参数。
### 支持的命理体系
| 体系 | 功能 | PRO版特性 |
| --- | --- | --- |
| 八字命理 | 四柱排盘+大运流年 | 深度分析 |
| 紫微斗数 | 十二宫排盘+星曜解读 | 完整命盘 |
| 合婚分析 | 两人命盘匹配度 | 匹配评分 |
| 奇门遁甲 | 基础排盘 | 时局分析 |
| 风水方位 | 方位吉凶 | 简要参考 |

**输入**: 用户提供支持的命理体系所需的指令和必要参数。
**输出**: 返回支持的命理体系的执行结果,包含操作状态和输出数据。
### 命理体系

执行命理体系操作,处理用户输入并返回结果。

**输入**: 用户提供命理体系所需的参数和指令。

**输出**: 返回命理体系的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`命理体系`相关配置参数进行设置
#
## 适用场景

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

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt

# 示例
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

### 示例2: 进阶用法
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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

