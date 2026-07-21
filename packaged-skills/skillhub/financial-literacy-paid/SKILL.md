---
slug: financial-literacy-paid
name: financial-literacy-paid
version: "1.0.0"
displayName: 金融素养专业版
summary: 专业金融教育与理财规划系统，支持个性化方案、认证培训与企业内训。
license: Proprietary
edition: pro
description: |-
  面向专业用户与机构的全栈金融素养教育系统。支持个性化理财方案生成、
  金融从业认证培训课程、企业内训定制与学习进度追踪。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。
tags:
- Finance
- 金融教育
- 理财规划
- 企业级
tools:
  - - read
- exec
---
# 金融素养专业版

## 核心能力

### PRO版功能增强对比
| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 知识体系 | 基础科普 | 完整体系+专业课程 |
| 个性化方案 | 不支持 | 定制理财规划 |
| 认证培训 | 不支持 | 基金/证券/保险 |
| 企业内训 | 不支持 | 批量学员管理 |
| 情景模拟 | 不支持 | 人生财务沙盘 |
| 案例库 | 基础案例 | 高级真实案例 |
| 进度追踪 | 基础自测 | 知识图谱+评估 |
| 报告导出 | 不支持 | PDF学习报告 |

**输入**: 用户提供PRO版功能增强对比所需的指令和必要参数。
**处理**: 按照skill规范执行PRO版功能增强对比操作,遵循单一意图原则。### 个性化理财方案

| 方案类型 | 输入参数 | 输出内容 |
| --- | --- | --- |
| 储蓄规划 | 收入/支出/目标 | 储蓄计划+产品推荐 |
| 投资组合 | 风险偏好/资产 | 资产配置建议 |
| 保险规划 | 家庭状况/预算 | 保险配置方案 |
| 退休规划 | 年龄/收入/期望 | 退休金缺口与补充 |
| 教育金 | 子女年龄/目标 | 教育金积累计划 |

### 认证培训课程
| 认证 | 课程数 | 题库量 | 模拟考 |
| --- | --- | --- | --- |
| 基金从业 | 15章 | 2000+ | 支持 |
| 证券从业 | 12章 | 1500+ | 支持 |
| 保险从业 | 10章 | 1200+ | 支持 |
| 银行从业 | 14章 | 1800+ | 支持 |

**输入**: 用户提供认证培训课程所需的指令和必要参数。
**处理**: 按照skill规范执行认证培训课程操作,遵循单一意图原则。
**输出**: 返回认证培训课程的执行结果,包含操作状态和输出数据。
### 知识体系

执行知识体系操作,处理用户输入并返回结果。

**输入**: 用户提供知识体系所需的参数和指令。

**输出**: 返回知识体系的处理结果。


## 适用场景

### 场景一：个性化理财规划

用户输入："35岁，年收入30万，有房贷，想规划退休"

```bash
# 生成个性化理财方案
python3 scripts/financial_plan.py \
  --age 35 \
  --income 300000 \
  --mortgage 15000 \
  --goal retirement \
  --retirement-age 60 \
  --risk-tolerance moderate

# 输出包含：
# - 当前财务健康度评估
# - 退休金缺口计算
# - 资产配置建议
# - 每月储蓄投资计划
# - 保险配置建议
# - 10年/20年/25年财务预测
```

### 场景二：认证备考

用户输入："帮我备考基金从业资格考试"

```bash
# 开始认证课程
python3 scripts/certification.py \
  --exam "基金从业" \
  --mode study

# 模拟考试
python3 scripts/certification.py \
  --exam "基金从业" \
  --mode mock \
  --count 100

# 错题复习
python3 scripts/certification.py \
  --exam "基金从业" \
  --mode review \
  --focus wrong_answers
```

### 场景三：企业内训管理

用户输入："为公司50名员工安排金融素养培训"

```bash
# 创建企业内训计划
python3 scripts/corporate_training.py \
  --create \
  --company "某科技公司" \
  --employees 50 \
  --course "financial_literacy_101" \
  --duration "8周"

# 查看学员进度
python3 scripts/corporate_training.py \
  --progress \
  --company "某科技公司"

# 生成培训报告
python3 scripts/corporate_training.py \
  --report \
  --output training_report.pdf
```

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install financial-literacy-pro

# 初始化学习档案
python3 scripts/init.py --user "学员姓名" --level intermediate
```

### 常用命令

```bash
# 个性化理财方案
python3 scripts/financial_plan.py --age 35 --income 300000 --goal retirement

# 认证学习
python3 scripts/certification.py --exam "基金从业" --mode study
python3 scripts/certification.py --exam "基金从业" --mode mock

# 情景模拟
python3 scripts/simulator.py --scenario "life_planning" --age 25 --retire 60

# 企业内训
python3 scripts/corporate_training.py --create --company "公司名" --employees 50
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
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
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+（理财计算功能需要）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 可选 | 理财计算与报告生成 |
| numpy | Python库 | 可选 | `pip install numpy`（财务计算） |
| pandas | Python库 | 可选 | `pip install pandas`（数据分析） |
| matplotlib | Python库 | 可选 | `pip install matplotlib`（图表） |

### API Key 配置

- PRO版无需外部API Key
- 所有理财计算与培训内容本地处理
- 学习数据存储在本地数据库

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 专业金融教育与理财规划系统，支持个性化方案与认证培训
- **PRO版特性**: 个性化理财方案、认证培训、企业内训、情景模拟、高级案例库
- **兼容性**: 完全包含免费版知识内容，支持学习进度迁移

## 案例展示

### PRO系统配置

```yaml
pro_config:
  user_profile:
    age: 35
    income: 300000
    risk_tolerance: moderate
    goals: ["retirement", "education_fund"]

  learning:
    level: intermediate
    track: professional          # professional | certification | corporate
    certification:
      target: "基金从业"
      study_plan: "3_months"
      daily_goal: 60             # 每日学习分钟

  planning:
    scenarios:
      - retirement
      - education
      - insurance
      - emergency_fund
    forecast_years: 25
    inflation_rate: 0.03
    return_assumption: 0.07

  corporate:
    enabled: true
    max_employees: 100
    progress_tracking: true
    report_frequency: weekly
```

## 常见问题

### Q1：个性化方案需要哪些输入？

需要提供年龄、收入、支出、资产、负债、风险偏好和理财目标等信息。输入越详细，方案越精准。所有数据本地存储，不会上传服务器。

### Q2：认证培训覆盖哪些考试？

PRO版覆盖基金从业、证券从业、保险从业和银行从业四类主要金融认证。题库定期更新，与最新考试大纲保持同步。

### Q3：企业内训支持多少人？

PRO版单企业最多支持100名学员。支持分层培训、进度追踪和培训报告生成。如需更大规模，可联系获取企业旗舰版。

### Q4：情景模拟器是什么？

情景模拟器是一个人生财务规划沙盘。用户输入起始年龄和目标，系统模拟不同人生阶段（结婚/购房/育儿/退休）的财务变化，帮助理解长期财务规划的重要性。

### Q5：学习进度如何追踪？

PRO版内置知识图谱，可视化展示学习进度与能力评估。系统自动记录学习时长、测试成绩和薄弱环节，生成个性化学习建议。

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
