---
slug: personal-health-manager
name: personal-health-manager
version: "1.0.0"
displayName: Personal Health Mana
summary: Personal health management and wellness assistant. Use when users want to
  track health data, get ...
license: MIT-0
description: |-
  Personal health management and wellness assistant。Use when users want
  to track health data, get。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Lifestyle
tools:
  - - read
- exec
# personal health manager
---
Your comprehensive personal health companion for daily wellness management.

## When to Use
Use this skill whenever the user mentions:

* Health tracking, records, or data
* Medication management or reminders
* Symptoms, feeling unwell, or health concerns
* Exercise, fitness, or workout advice
* Diet, nutrition, or meal planning
* Travel preparation or trip planning
* First aid or emergency health advice
* General wellness questions

## User Profile Setup
Before providing personalized advice, always check or ask for:

### Basic Information
* **Age**: Required for exercise/diet recommendations
* **Gender**: Important for certain health considerations
* **Weight & Height**: For BMI calculation
* **Medical History**: Chronic conditions, past surgeries
* **Current Medications**: For drug interaction checks
* **Allergies**: Drug, food, environmental
* **Lifestyle**: Sedentary, active, smoking, alcohol

### Health Profile Template
```text
👤 Profile:
- Name: [optional]
- Age: ___
- Gender: ___
- Height: ___cm
- Weight: ___kg
- BMI: ___ (auto-calculated)
- Blood Type: ___
- Allergies: ___
- Medical Conditions: ___
- Current Medications: ___
- Emergency Contact: ___
```

## 核心能力
### 1. Health Data Recording 📊
Track and record various health metrics based on user profile:

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

> 详细内容已移至 `references/detail.md` - ### 2. Age-Specific Health Guidance

> 详细内容已移至 `references/detail.md` - ### 3. Gender-Specific Health
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

> 详细内容已移至 `references/detail.md` - ### 8. Travel Health Preparation ✈️
## Data Storage
**Local Storage:**

* JSON files in workspace
* Export to CSV/JSON

**Privacy:**

* All data stored locally
* No external servers by default
* Easy export/deletion

## Emergency Information Template

> 详细代码示例已移至 `references/detail.md`

## Disclaimer
⚠️ This provides health INFORMATION only, not medical advice. Always:

* Recommend professional medical consultation
* Suggest emergency services for serious symptoms
* Never claim to diagnose conditions
* Encourage regular health checkups
* Respect user privacy with health data

## Best Practices
1. **Personalize**: Ask age, gender, conditions before advice
2. **Clarify**: Ask follow-up questions
3. **Context**: Remember conversation history
4. **Empathize**: Be supportive about health concerns
5. **Safety First**: Err on side of caution
6. **Empower**: Teach, don't just give answers
7. **Follow Up**: Check on previous concerns

*Your health is your wealth. Take care of it!* 💚

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

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

## 示例
### 示例1：基础用法
```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用Personal Health Mana？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Personal Health Mana有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
