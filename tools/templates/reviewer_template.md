<!--
  ============================================================
  设计模式: Reviewer (审查评估器)
  适用场景: 代码/内容审查、质量评估、合规检查、打分评级
  推荐行数: 150-250行, 上限300行
  核心结构: references/放检查清单/评分标准
  ============================================================
  使用说明:
  1. 复制本文件, 重命名为 SKILL.md
  2. 填充所有 {{占位符}} 为具体内容
  3. 删除所有 <!-- 写作指引 --> 和 <!-- 质量检查点 --> 注释
  4. 将检查清单/评分标准放到 references/ 目录
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

<!-- 写作指引: Reviewer模式的能力应聚焦于"检查什么"+"依据什么标准"+"输出什么结论"。 -->

- {{capability_1}} - 基于{{standard_1}}标准审查
- {{capability_2}} - 输出{{output_type_1}}评级报告
- {{capability_3}} - 提供{{feedback_type}}改进建议
- {{capability_4}} - 支持{{scope_1}}全维度评估

<!-- 质量检查点: [ ] 能力≥3条 [ ] 提及检查标准 [ ] 提及输出类型 -->

## 适用场景

<!-- 写作指引: Reviewer模式的场景应描述"用户要审查什么内容"。 -->

- 用户说"{{user_phrase_1}}" → {{review_action_1}}
- 用户说"{{user_phrase_2}}" → {{review_action_2}}
- 用户说"{{user_phrase_3}}" → {{review_action_3}}
- 不适用: {{exclusion_scenario}}

<!-- 质量检查点: [ ] 场景≥3个 [ ] 含审查动作 [ ] 含不适用场景 -->

## 使用流程

<!-- 写作指引: Reviewer模式的流程重点是"读取内容→逐项检查→生成报告"。 -->

### Step 1: 内容解析
{{step_1_instruction}}
解析待审查内容, 提取以下要素:
- {{element_1}}: {{element_1_desc}}
- {{element_2}}: {{element_2_desc}}

### Step 2: 逐项检查
{{step_2_instruction}}
按照 `references/{{checklist}}` 中的检查清单逐项审查:

| 检查项 | 检查方法 | 通过标准 |
|--------|---------|---------|
| {{check_item_1}} | {{check_method_1}} | {{pass_criteria_1}} |
| {{check_item_2}} | {{check_method_2}} | {{pass_criteria_2}} |
| {{check_item_3}} | {{check_method_3}} | {{pass_criteria_3}} |

### Step 3: 评级判定
{{step_3_instruction}}
根据检查结果评定等级:
- A级(优秀): {{grade_a_criteria}}
- B级(良好): {{grade_b_criteria}}
- C级(及格): {{grade_c_criteria}}
- D级(不及格): {{grade_d_criteria}}

### Step 4: 生成报告
{{step_4_instruction}}
输出审查报告, 包含: 总评/各项详情/改进建议/优先级排序。

<!-- 质量检查点: [ ] 步骤≥4个 [ ] 含检查清单引用 [ ] 含评级标准 -->

## 输入格式

<!-- 写作指引: Reviewer模式的输入通常包含待审查内容和审查维度。 -->

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| {{param_1}} | string | 是 | {{desc_1}} |
| {{param_2}} | string | 否 | {{desc_2}}, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

<!-- 质量检查点: [ ] 参数表格化 [ ] 含严格度参数 [ ] 有默认值 -->

## 输出格式

<!-- 写作指引: Reviewer模式的输出应包含评级、详情、建议三部分。 -->

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "{{overall_summary}}",
    "details": [
      {
        "item": "{{check_item_1}}",
        "status": "pass",
        "score": 95,
        "comment": "{{item_comment_1}}"
      },
      {
        "item": "{{check_item_2}}",
        "status": "warn",
        "score": 80,
        "comment": "{{item_comment_2}}"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "{{suggestion_1}}",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "{{suggestion_2}}",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

<!-- 质量检查点: [ ] 有JSON示例 [ ] 含评级/评分 [ ] 含改进建议 [ ] 含优先级 -->

## 异常处理

<!-- 写作指引: Reviewer模式的异常应覆盖输入无效、格式不支持、检查失败等场景。 -->

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 待审查内容为空 | 用户未提供内容 | 提示用户提供待审查的{{input_type}} |
| 内容格式不识别 | 传入不支持的内容格式 | 列出支持的格式, 建议转换后重试 |
| 检查项超出范围 | 传入了不存在的检查维度 | 列出可用检查维度, 使用默认全部检查 |
| 审查超时 | 内容过长导致处理超时 | 建议分段审查, 每段不超过{{max_length}} |
| {{error_scene_5}} | {{error_reason_5}} | {{error_fix_5}} |

<!-- 质量检查点: [ ] 异常≥4种 [ ] 表格化 [ ] 含格式异常+超时异常 -->

## 依赖说明

<!-- 写作指引: Reviewer模式通常依赖LLM + 检查清单文件。 -->

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行智能审查, 推荐GPT-4/智谱GLM-4/DeepSeek |
| `references/{{checklist}}` | 文件 | 是 | {{checklist_desc}} |
| `references/{{scoring_rubric}}` | 文件 | 否 | {{rubric_desc}} |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

<!-- 质量检查点: [ ] 表格化 [ ] 含检查清单依赖 [ ] 含国内替代方案 -->

## 案例展示

<!-- 写作指引: Reviewer模式的案例应展示"待审查内容→审查报告"的完整对比。 -->

### 示例1: {{case_1_title}}
**输入**:
```json
{
  "{{param_1}}": "{{case_1_content}}",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100

检查详情:
- {{check_item_1}}: 通过(95分) - {{case_1_comment_1}}
- {{check_item_2}}: 警告(75分) - {{case_1_comment_2}}
- {{check_item_3}}: 通过(85分) - {{case_1_comment_3}}

改进建议:
1. [高优先级] {{case_1_suggestion_1}}
2. [中优先级] {{case_1_suggestion_2}}
```

### 示例2: {{case_2_title}}
**输入**:
```json
{
  "{{param_1}}": "{{case_2_content}}",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100

检查详情:
- {{check_item_1}}: 通过(90分) - {{case_2_comment_1}}
- {{check_item_2}}: 不通过(50分) - {{case_2_comment_2}}
- {{check_item_3}}: 警告(70分) - {{case_2_comment_3}}

改进建议:
1. [高优先级] {{case_2_suggestion_1}}
2. [高优先级] {{case_2_suggestion_2}}
3. [低优先级] {{case_2_suggestion_3}}
```

### 示例3: 边界情况 - {{case_3_title}}
**输入**:
```json
{
  "{{param_1}}": "{{case_3_content}}"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100

检查详情:
- {{check_item_1}}: 不通过(40分) - {{case_3_comment_1}}
- {{check_item_2}}: 不通过(30分) - {{case_3_comment_2}}
- {{check_item_3}}: 通过(65分) - {{case_3_comment_3}}

改进建议:
1. [紧急] {{case_3_suggestion_1}}
2. [高优先级] {{case_3_suggestion_2}}
```

<!-- 质量检查点: [ ] 示例≥3个 [ ] 含不同评级 [ ] 含边界情况 [ ] 输出完整 -->

## 常见问题

### Q: {{faq_q_1}}?
A: {{faq_a_1}}

### Q: {{faq_q_2}}?
A: {{faq_a_2}}

### Q: {{faq_q_3}}?
A: {{faq_a_3}}

<!-- 质量检查点: [ ] FAQ≥3条 [ ] 问答格式 [ ] 覆盖常见疑问 -->

## 已知限制

<!-- 写作指引: Reviewer模式的限制应说明审查能力的边界。 -->

- {{limitation_1}}
- {{limitation_2}}
- {{limitation_3}}
- {{limitation_4}}

<!-- 质量检查点: [ ] 限制≥3条 [ ] 具体可操作 [ ] 非空泛表述 -->
