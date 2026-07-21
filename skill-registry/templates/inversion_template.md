<!--
  ============================================================
  设计模式: Inversion (反向操作器)
  适用场景: 先收集需求再执行, 反向推导/还原/解密/反推
  推荐行数: 150-250行, 上限300行
  核心结构: 多轮问答收集信息 + assets/放输出模板
  ============================================================
  使用说明:
  1. 复制本文件, 重命名为 SKILL.md
  2. 填充所有 {{占位符}} 为具体内容
  3. 删除所有 <!-- 写作指引 --> 和 <!-- 质量检查点 --> 注释
  4. 将输出模板放到 assets/ 目录
  5. 运行 L1+L2 验证
  ============================================================
-->

---
name: {{slug}}
slug: {{slug}}
displayName: {{display_name}}
version: "1.0.0"
summary: {{summary}}
description: |-
  {{feature}}。适用于{{applicable_scenario}}，{{input_type}}→{{output_type}}。
  Use when 用户说"{{trigger_phrase_1}}"、{{trigger_phrase_2}}"时使用。
  不适用于{{exclusion_scenario}}。
license: Proprietary
tools:
  - read
  - exec
---

# {{display_name}}

## 核心能力

<!-- 写作指引: Inversion模式的能力应聚焦于"从结果反推输入"或"收集信息后反向执行"。核心是"反向"思维。 -->

- {{capability_1}} - 从{{result_type}}反推{{input_type}}
- {{capability_2}} - 通过{{round_count}}轮问答收集完整需求
- {{capability_3}} - 生成{{output_type}}的反向映射结果
- {{capability_4}} - 支持{{variation_1}}等多种反向模式

<!-- 质量检查点: [ ] 能力≥3条 [ ] 体现"反向"特征 [ ] 提及多轮问答 -->

## 适用场景

<!-- 写作指引: Inversion模式的场景应描述"用户有什么结果,需要反推什么"。 -->

- 用户说"{{user_phrase_1}}" → {{inversion_action_1}}
- 用户说"{{user_phrase_2}}" → {{inversion_action_2}}
- 用户说"{{user_phrase_3}}" → {{inversion_action_3}}
- 不适用: {{exclusion_scenario}}

<!-- 质量检查点: [ ] 场景≥3个 [ ] 含反向操作 [ ] 含不适用场景 -->

## 使用流程

<!-- 写作指引: Inversion模式的核心是"多轮问答收集信息→反向推导→输出结果"。重点描述问答流程。 -->

### Step 1: 初始需求收集
{{step_1_instruction}}
向用户提出第一轮问题:
- Q1: {{question_1}}
- Q2: {{question_2}}

根据用户回答, 判断是否有足够信息进行反向推导。
若信息不足, 进入Step 2补充收集。

### Step 2: 补充信息收集(按需)
{{step_2_instruction}}
根据第一轮回答的缺失部分, 提出针对性问题:
- Q3: {{question_3}} (当{{condition_3}}时提问)
- Q4: {{question_4}} (当{{condition_4}}时提问)

收集完毕后进入Step 3。

### Step 3: 反向推导
{{step_3_instruction}}
基于收集到的信息, 执行反向推导:
1. {{derivation_step_1}}
2. {{derivation_step_2}}
3. {{derivation_step_3}}

### Step 4: 结果确认与输出
{{step_4_instruction}}
生成反向推导结果, 按 `assets/{{output_template}}` 格式输出。
向用户确认结果是否符合预期, 若不符合则回到Step 2补充信息。

<!-- 质量检查点: [ ] 步骤≥4个 [ ] 含多轮问答 [ ] 含条件分支 [ ] 含结果确认 -->

## 输入格式

<!-- 写作指引: Inversion模式的输入是渐进式收集的, 应说明每轮需要什么信息。 -->

**第一轮输入**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| {{param_1}} | string | 是 | {{desc_1}} |
| {{param_2}} | string | 否 | {{desc_2}} |

**第二轮补充(按需)**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| {{param_3}} | string | 条件必填 | {{desc_3}}, 当{{condition_3}}时必填 |
| {{param_4}} | string | 条件必填 | {{desc_4}}, 当{{condition_4}}时必填 |

<!-- 质量检查点: [ ] 分轮次说明 [ ] 含条件必填 [ ] 表格化 -->

## 输出格式

<!-- 写作指引: Inversion模式的输出应展示反向推导的结果结构。 -->

```json
{
  "success": true,
  "data": {
    "inversion_type": "{{inversion_type}}",
    "collected_info": {
      {{collected_field_1}}: "{{collected_desc_1}}",
      {{collected_field_2}}: "{{collected_desc_2}}"
    },
    "result": {
      {{result_field_1}}: "{{result_desc_1}}",
      {{result_field_2}}: "{{result_desc_2}}",
      {{result_field_3}}: "{{result_desc_3}}"
    },
    "confidence": 0.95,
    "derivation_steps": [
      "{{derivation_log_1}}",
      "{{derivation_log_2}}",
      "{{derivation_log_3}}"
    ]
  },
  "error": null
}
```

输出模板参考: `assets/{{output_template}}`

<!-- 质量检查点: [ ] 有JSON示例 [ ] 含推导步骤 [ ] 含置信度 [ ] 引用assets模板 -->

## 异常处理

<!-- 写作指引: Inversion模式的异常应覆盖信息不足、推导失败、置信度低等场景。 -->

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 关键信息缺失 | 用户未回答必填问题 | 列出缺失项, 重新提问, 提供示例引导 |
| 信息矛盾 | 不同轮次回答互相矛盾 | 指出矛盾点, 请用户确认正确信息 |
| 推导置信度低(<60%) | 收集的信息不足以确定推导 | 补充提问, 或提供多个候选结果供用户选择 |
| 推导失败 | 信息完整但无法完成反向推导 | 说明失败原因, 建议提供更多上下文或换种方式描述 |
| {{error_scene_5}} | {{error_reason_5}} | {{error_fix_5}} |

<!-- 质量检查点: [ ] 异常≥4种 [ ] 表格化 [ ] 含置信度异常 [ ] 含信息矛盾处理 -->

## 依赖说明

<!-- 写作指引: Inversion模式通常依赖LLM进行多轮对话和反向推导。 -->

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行多轮问答和反向推导, 推荐GPT-4/智谱GLM-4/DeepSeek |
| `assets/{{output_template}}` | 文件 | 是 | {{template_desc}} |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

<!-- 质量检查点: [ ] 表格化 [ ] 含LLM依赖 [ ] 含国内替代方案 -->

## 案例展示

<!-- 写作指引: Inversion模式的案例应展示完整的"多轮问答→反向结果"过程。 -->

### 示例1: {{case_1_title}}
**第一轮输入**: {{case_1_round1_input}}
**第一轮追问**: {{case_1_round2_question}}
**第二轮输入**: {{case_1_round2_input}}
**输出**:
```json
{
  "inversion_type": "{{case_1_type}}",
  "result": {
    {{result_field_1}}: "{{case_1_result_1}}",
    {{result_field_2}}: "{{case_1_result_2}}"
  },
  "confidence": 0.92
}
```

### 示例2: {{case_2_title}}
**第一轮输入**: {{case_2_round1_input}}
**输出**(信息充足, 无需追问):
```json
{
  "inversion_type": "{{case_2_type}}",
  "result": {
    {{result_field_1}}: "{{case_2_result_1}}",
    {{result_field_2}}: "{{case_2_result_2}}"
  },
  "confidence": 0.88
}
```

### 示例3: 边界情况 - {{case_3_title}}
**第一轮输入**: {{case_3_round1_input}}
**第一轮追问**: {{case_3_round2_question}}
**第二轮输入**: {{case_3_round2_input}}
**输出**(置信度低, 提供候选):
```json
{
  "inversion_type": "{{case_3_type}}",
  "result": {
    "candidates": [
      {"{{result_field_1}}": "{{case_3_candidate_1}}", "confidence": 0.55},
      {"{{result_field_1}}": "{{case_3_candidate_2}}", "confidence": 0.42}
    ]
  },
  "confidence": 0.55
}
```

<!-- 质量检查点: [ ] 示例≥3个 [ ] 含多轮问答 [ ] 含边界情况 [ ] 含置信度展示 -->

## 常见问题

### Q: {{faq_q_1}}?
A: {{faq_a_1}}

### Q: {{faq_q_2}}?
A: {{faq_a_2}}

### Q: {{faq_q_3}}?
A: {{faq_a_3}}

<!-- 质量检查点: [ ] FAQ≥3条 [ ] 问答格式 [ ] 覆盖常见疑问 -->

## 已知限制

<!-- 写作指引: Inversion模式的限制应说明反向推导能力的边界。 -->

- {{limitation_1}}
- {{limitation_2}}
- {{limitation_3}}
- {{limitation_4}}

<!-- 质量检查点: [ ] 限制≥3条 [ ] 具体可操作 [ ] 非空泛表述 -->
