---
slug: "personal-health-manager"
name: "personal-health-manager"
version: "1.0.0"
displayName: "Personal Health Mana"
summary: "Personal health management and wellness assistant. Use when users want to"
license: "Proprietary"
description: |-
  Personal health management and wellness assistant。Use when users want
  to track health data, get。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Lifestyle
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# Personal Health Mana

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

### 1. Health Data Recording 📊
Track and record various health metrics 基于 user profile:

#### Blood Pressure 💉
| Category | Systolic | Diastolic |
| --- | --- | --- |
| Normal | <120 | <80 |
| Elevated | 120-129 | <80 |
| Stage 1 HTN | 130-139 | 80-89 |
| Stage 2 HTN | ≥140 | ≥90 |
| Crisis | >180 | >120 ⚠️ |

#### Blood Glucose 🍬
| Status | Fasting | 2h Post-Meal |
| --- | --- | --- |
| Normal | <100 | <140 |
| Prediabetes | 100-125 | 140-199 |
| Diabetes | ≥126 | ≥200 |

#### Heart Rate ❤️
| Age Group | Normal Resting | Max Heart Rate |
| --- | --- | --- |
| 20-29 | 60-100 | 190-200 |
| 30-39 | 60-100 | 180-190 |
| 40-49 | 60-100 | 170-180 |
| 50-59 | 60-100 | 160-170 |
| 60+ | 60-100 | 150-160 |

#### BMI Calculator ⚖️
| Category | BMI Range |
| --- | --- |
| Underweight | <18.5 |
| Normal | 18.5-24.9 |
| Overweight | 25-29.9 |
| Obese | ≥30 |

> 详细内容已移至 `references/detail.md` -

**处理**: 按照skill规范执行Health Data Recording 📊操作,遵循单一意图原则。
**输出**: 返回Health Data Recording 📊的执行结果,包含操作状态和输出数据。
### 2. Age-Specific Health Guidance
> 详细内容已移至 `references/detail.md` -

**输入**: 用户提供Age-Specific Health Guidance所需的指令和必要参数。
**处理**: 按照skill规范执行Age-Specific Health Guidance操作,遵循单一意图原则。
**输出**: 返回Age-Specific Health Guidance的执行结果,包含操作状态和输出数据。
### 3. Gender-Specific Health

**处理**: 按照skill规范执行Health Data Recording 📊操作,遵循单一意图原则。
**输出**: 返回Health Data Recording 📊的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`Gender-Specific Health`相关配置参数进行设置
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
| --- | --- | --- |
| Warfarin | Aspirin | Bleeding risk |
| Metformin | Alcohol | Lactic acidosis |
| Statins | Grapefruit | Increased side effects |
| ACE inhibitors | Potassium | High potassium |

**输入**: 用户提供Medication Management 💊所需的指令和必要参数。
**处理**: 按照skill规范执行Medication Management 💊操作,遵循单一意图原则。
**输出**: 返回Medication Management 💊的执行结果,包含操作状态和输出数据。

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

**输出**: 返回Symptom Analysis 🩺的执行结果,包含操作状态和输出数据。
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

**Diabetes:**

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

- 参考`Exercise Recommendations 🏃`相关配置参数进行设置

**输出**: 返回Exercise Recommendations 🏃的执行结果,包含操作状态和输出数据。
### 7. Nutrition Advice 🥗
#### By Age
**Children:**

* Make food fun
* Involve in cooking
* Model healthy eating
* Don't force foods

**Adults:**

* Balanced macronutrients
* Meal prep for busy days
* Mindful eating
* Limit processed foods

**Seniors:**

* High protein (1.0-1.2g/kg)
* Vitamin D + B12
* Easy-to-chew foods
* Small, frequent meals

#### By Condition
**High Blood Pressure:**

* Low sodium (<1500mg/day)
* DASH diet
* Limit alcohol

**Diabetes:**

* Consistent carb intake
* High fiber
* Limit simple sugars
* Spread meals throughout day

**High Cholesterol:**

* Low saturated fat
* High fiber
* Omega-3 fatty acids
* Plant sterols

**Weight Management:**

* Calorie awareness (not counting)
* Protein + fiber for fullness
* Limit added sugars
* Drink water before meals

> 详细内容已移至 `references/detail.md` -

**输入**: 用户提供Nutrition Advice 🥗所需的指令和必要参数。
**输出**: 返回Nutrition Advice 🥗的执行结果,包含操作状态和输出数据。
### 8. Travel Health Preparation ✈️

**输入**: 用户提供Nutrition Advice 🥗所需的指令和必要参数。
**输出**: 返回Nutrition Advice 🥗的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`Travel Health Preparation ✈️`相关配置参数进行设置
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

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
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。

## 常见问题

### Q1: 如何开始使用Personal Health Mana？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Personal Health Mana有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

