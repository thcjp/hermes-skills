---
slug: "personal-health-manager"
name: "personal-health-manager"
version: 1.0.1
displayName: "Personal Health Mana"
summary: "个人健康管理与养生助手,追踪健康数据。Personal health management and wellness assistant。Use when users want to tra"
license: "Proprietary"
description: |-
  Personal health management and wellness assistant。Use when users want
  to track health data, get。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - Lifestyle
  - 工具
  - 效率
  - 自动化
  - 创意
  - 图像
  - 研究
  - 分析
  - health
  - medication
  - 返回
  - 的处理结
  - 包含执行
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# Personal Health Mana

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Personal Health Mana个人健康管理 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

### 1. Health Data Recording 📊
Track and record various health metrics 基于 user profile:

#### Blood Pressure 💉
| Category | Systolic | Diastolic |
|:---------|:---------|:---------|
| Normal | <120 | <80 |
| Elevated | 120-129 | <80 |
| Stage 1 HTN | 130-139 | 80-89 |
| Stage 2 HTN | ≥140 | ≥90 |
| Crisis | >180 | >120 ⚠️ |

#### Blood Glucose 🍬
| Status | Fasting | 2h Post-Meal |
|----:|----:|----:|
| Normal | <100 | <140 |
| Prediabetes | 100-125 | 140-199 |
| Diabetes | ≥126 | ≥200 |

#### Heart Rate ❤️
| Age Group | Normal Resting | Max Heart Rate |
|:--------:|:--------:|:--------:|
| 20-29 | 60-100 | 190-200 |
| 30-39 | 60-100 | 180-190 |
| 40-49 | 60-100 | 170-180 |
| 50-59 | 60-100 | 160-170 |
| 60+ | 60-100 | 150-160 |

#### BMI Calculator ⚖️
| Category | BMI Range |
|:----------|----------:|
| Underweight | <18.5 |
| Normal | 18.5-24.9 |
| Overweight | 25-29.9 |
| Obese | ≥30 |

> 详细内容已移至 `references/detail.md` -

**处理**: 解析Health Data Recording 📊的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Health Data Recording 📊的处理结果,包含执行状态码、结果数据和执行日志.
### 2. Age-Specific Health Guidance
> 详细内容已移至 `references/detail.md` -

**输入**: 用户提供Age-Specific Health Guidance所需的指令和必要参数.
**处理**: 解析Age-Specific Health Guidance的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Age-Specific Health Guidance的处理结果,包含执行状态码、结果数据和执行日志.
### 3. Gender-Specific Health

**处理**: 解析Health Data Recording 📊的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Health Data Recording 📊的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`Gender-Specific Health`的配置文档进行参数调优
### 4. Medication Management 💊
**Features:**

* Add/edit/delete medications
* Track dosage and frequency
* Set medication schedules
* Drug interaction warnings
* Refill reminders
* Medication history

#### Common Medications by Condition
**Hypertension:**

* ACE inhibitors (enalapril, lisinopril)
* ARBs (losartan, valsartan)
* Beta blockers (metoprolol)
* Diuretics (hydrochlorothiazide)

**Diabetes:**

* Metformin
* Sulfonylureas
* SGLT2 inhibitors
* Insulin

**High Cholesterol:**

* Statins (atorvastatin, rosuvastatin)
* Fibrates
* Ezetimibe

**Pain:**

* Acetaminophen
* Ibuprofen
* Naproxen

**Drug Interactions to Watch:**

| Drug A | Drug B | Effect |
|---:|:---|---:|
| Warfarin | Aspirin | Bleeding risk |
| Metformin | Alcohol | Lactic acidosis |
| Statins | Grapefruit | Increased side effects |
| ACE inhibitors | Potassium | High potassium |

**输入**: 用户提供Medication Management 💊所需的指令和必要参数.
**处理**: 解析Medication Management 💊的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Medication Management 💊的处理结果,包含执行状态码、结果数据和执行日志.
### 5. Symptom Analysis 🩺
**Process:**

1. Collect symptom details (location, duration, severity)
2. Ask relevant follow-up questions
3. Provide possible causes (informational only)
4. Recommend when to seek medical attention
5. Suggest self-care measures if appropriate

#### Age-Specific Symptom Considerations
**Children:**

* Temperature thresholds lower
* Behavior changes more important than specific symptoms
* Dehydration happens faster
* When to seek care: fever >48h, unable to drink, rash with fever

**Adults:**

* Standard symptom assessment
* Chronic conditions affect presentation
* Medication side effects

**Elderly:**

* Symptoms often less typical
* Confusion can be only sign of infection
* Falls may indicate underlying problem
* Medication side effects more common

#### Red Flags - Seek Immediate Care 🚨
* Chest pain + sweating + pain in arm/jaw
* Difficulty breathing
* Severe bleeding
* Sudden severe headache
* Confusion/loss of consciousness
* Sudden weakness/numbness (stroke)
* High fever + rash
* Severe vomiting + unable to keep fluids down
* Overdose symptoms

**输出**: 返回Symptom Analysis 🩺的处理结果,包含执行状态码、结果数据和执行日志.
### 6. Exercise Recommendations 🏃
#### By Age & Fitness Level
**Beginner (Any Age):**

* Start with 10-minute walks
* Chair exercises
* Water aerobics
* Dancing

**Intermediate:**

* Brisk walking 30 min
* Swimming
* Cycling
* Light strength training

**Advanced:**

* Running
* HIIT
* Heavy strength training
* Sports

#### By Health Condition
**High Blood Pressure:**

* Walking, swimming, cycling
* Avoid heavy weightlifting
* Include cool-down

* Check blood sugar before/after exercise
* Carry fast-acting carbs
* Avoid exercise if glucose >250

**Arthritis:**

* Swimming (joint-friendly)
* Stationary bike
* Gentle yoga
* Avoid high-impact

**Heart Disease:**

* Cardiac rehab programs
* Start slow, gradual increase
* Monitor heart rate

- 参考`Exercise Recommendations 🏃`的配置文档进行参数调优

**输出**: 返回Exercise Recommendations 🏃的处理结果,包含执行状态码、结果数据和执行日志.
### 7. Nutrition Advice 🥗
#### By Age
**Children:**

* Make food fun
* Involve in cooking
* Model healthy eating
* Don't force foods

* Balanced macronutrients
* Meal prep for busy days
* Mindful eating
* Limit processed foods

**Seniors:**

* High protein (1.0-1.2g/kg)
* Vitamin D + B12
* Easy-to-chew foods
* Small, frequent meals

* Low sodium (<1500mg/day)
* DASH diet
* Limit alcohol

* Consistent carb intake
* High fiber
* Limit simple sugars
* Spread meals throughout day

* Low saturated fat
* High fiber
* Omega-3 fatty acids
* Plant sterols

**Weight Management:**

* Calorie awareness (not counting)
* Protein + fiber for fullness
* Limit added sugars
* Drink water before meals

**输入**: 用户提供Nutrition Advice 🥗所需的指令和必要参数.
**输出**: 返回Nutrition Advice 🥗的处理结果,包含执行状态码、结果数据和执行日志.
### 8. Travel Health Preparation ✈️

**输入**: 用户提供Nutrition Advice 🥗所需的指令和必要参数.
**输出**: 返回Nutrition Advice 🥗的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`Travel Health Preparation ✈️`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:------:|--------|:-------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|----|:--:|---:|----|
| content | string | 否 | personal-health-manager处理的内容输入 |,  |
| content | string | 否 | personal-health-manager处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "manager 相关配置参数",
    result: "manager 相关配置参数",
    result: "manager 相关配置参数",
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
|----|----|----|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 常见问题

### Q1: 如何开始使用Personal Health Mana？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|-----:|-----:|-----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

