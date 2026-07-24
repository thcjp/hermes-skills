<!--
  ============================================================
  设计模式: Generator (内容生成器)
  适用场景: 输出固定格式内容(文案/代码/设计/报告等)
  推荐行数: 150-250行, 上限300行
  核心结构: assets/放模板 + references/放风格指南
  ============================================================
  使用说明:
  1. 复制本文件, 重命名为 SKILL.md
  2. 填充所有 {{占位符}} 为具体内容
  3. 删除所有 <!-- 写作指引 --> 和 <!-- 质量检查点 --> 注释
  4. 将输出模板放到 assets/ 目录
  5. 将风格指南/写作规范放到 references/ 目录
  6. 运行 L1+L2 验证
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

<!-- 写作指引: Generator模式的能力应聚焦于"生成什么内容"+"遵循什么风格/模板"。每条能力要具体到输出类型。 -->

- {{capability_1}} - 生成{{output_type_1}}
- {{capability_2}} - 遵循{{style_name}}风格规范
- {{capability_3}} - 支持{{variation_1}}等多种变体
- {{capability_4}} - 自动适配{{adaptation_target}}

<!-- 质量检查点: [ ] 能力≥3条 [ ] 每条含输出类型 [ ] 提及风格/模板 -->

## 适用场景

<!-- 写作指引: Generator模式的场景应描述"用户要生成什么内容"。每个场景含输入和期望输出。 -->

- 用户说"{{user_phrase_1}}" → 生成{{output_desc_1}}
- 用户说"{{user_phrase_2}}" → 生成{{output_desc_2}}
- 用户说"{{user_phrase_3}}" → 生成{{output_desc_3}}
- 不适用: {{exclusion_scenario}}

<!-- 质量检查点: [ ] 场景≥3个 [ ] 含输出描述 [ ] 含不适用场景 -->

## 使用流程

<!-- 写作指引: Generator模式的流程重点是"理解需求→选择模板→填充内容→风格调整"。 -->

### Step 1: 需求理解
{{step_1_instruction}}
确认以下要素:
- {{element_1}}: {{element_1_desc}}
- {{element_2}}: {{element_2_desc}}
- {{element_3}}: {{element_3_desc}}

### Step 2: 模板选择
{{step_2_instruction}}
根据需求选择对应模板:
- {{template_1}}: {{template_1_desc}}
- {{template_2}}: {{template_2_desc}}

### Step 3: 内容生成
{{step_3_instruction}}
按照 `references/{{style_guide}}` 中的风格规范生成内容。

### Step 4: 质量校验
{{step_4_instruction}}
检查生成结果是否满足:
- {{check_1}}
- {{check_2}}
- {{check_3}}

<!-- 质量检查点: [ ] 步骤≥3个 [ ] 含模板选择 [ ] 含质量校验步骤 -->

## 输入格式

<!-- 写作指引: Generator模式的输入通常包含主题、风格、长度等参数。 -->

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| {{param_1}} | string | 是 | {{desc_1}} |
| {{param_2}} | string | 否 | {{desc_2}}, 默认: {{default_2}} |
| {{param_3}} | string | 否 | {{desc_3}}, 可选值: {{options_3}} |
| style | string | 否 | 输出风格, 参考 `references/{{style_guide}}` |

<!-- 质量检查点: [ ] 参数表格化 [ ] 含默认值说明 [ ] 含可选值 -->

## 输出格式

<!-- 写作指引: Generator模式的输出应展示完整的结构化格式。 -->

```json
{
  "success": true,
  "data": {
    {{output_field_1}}: "{{output_desc_1}}",
    {{output_field_2}}: "{{output_desc_2}}",
    {{output_field_3}}: "{{output_desc_3}}",
    "metadata": {
      "template_used": "{{template_name}}",
      "word_count": 0,
      "style": "{{style_name}}"
    }
  },
  "error": null
}
```

输出模板参考: `assets/{{output_template}}`

<!-- 质量检查点: [ ] 有JSON示例 [ ] 含metadata [ ] 引用assets模板 -->

## 异常处理

<!-- 写作指引: Generator模式的异常应覆盖输入不足、风格冲突、长度超限等场景。 -->

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 输入{{param_1}}为空 | 用户未提供必要信息 | 提示用户提供{{param_1}}, 并给出示例格式 |
| 输入内容过长(>5000字) | 超出单次处理能力 | 建议分段处理, 每段不超过2000字 |
| 风格参数不识别 | 传入不支持的风格 | 列出支持的风格选项, 使用默认风格 |
| 生成内容不达标 | 质量校验未通过 | 自动重试1次, 仍不达标则标注问题返回 |
| {{error_scene_5}} | {{error_reason_5}} | {{error_fix_5}} |

<!-- 质量检查点: [ ] 异常≥4种 [ ] 表格化 [ ] 含输入异常+生成异常 -->

## 依赖说明

<!-- 写作指引: Generator模式通常依赖LLM + 风格指南文件。 -->

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| `references/{{style_guide}}` | 文件 | 是 | {{style_guide_desc}} |
| `assets/{{output_template}}` | 文件 | 是 | {{template_desc}} |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

<!-- 质量检查点: [ ] 表格化 [ ] 含文件依赖 [ ] 含国内替代方案 -->

## 案例展示

<!-- 写作指引: Generator模式的案例应展示完整的"输入→输出"对比, 至少3个案例含1个边界情况。 -->

### 示例1: {{case_1_title}}
**输入**:
```json
{
  "{{param_1}}": "{{case_1_param_1_value}}",
  "{{param_2}}": "{{case_1_param_2_value}}",
  "style": "{{case_1_style}}"
}
```
**输出**:
```
{{case_1_output}}
```

### 示例2: {{case_2_title}}
**输入**:
```json
{
  "{{param_1}}": "{{case_2_param_1_value}}",
  "{{param_2}}": "{{case_2_param_2_value}}",
  "style": "{{case_2_style}}"
}
```
**输出**:
```
{{case_2_output}}
```

### 示例3: 边界情况 - {{case_3_title}}
**输入**:
```json
{
  "{{param_1}}": "{{case_3_param_1_value}}"
}
```
**输出**:
```
{{case_3_output}}
```

<!-- 质量检查点: [ ] 示例≥3个 [ ] 含JSON输入 [ ] 含边界情况 [ ] 输出完整 -->

## 常见问题

### Q: {{faq_q_1}}?
A: {{faq_a_1}}

### Q: {{faq_q_2}}?
A: {{faq_a_2}}

### Q: {{faq_q_3}}?
A: {{faq_a_3}}

<!-- 质量检查点: [ ] FAQ≥3条 [ ] 问答格式 [ ] 覆盖常见疑问 -->

## 已知限制

<!-- 写作指引: Generator模式的限制应说明生成能力的边界。 -->

- {{limitation_1}}
- {{limitation_2}}
- {{limitation_3}}
- {{limitation_4}}

<!-- 质量检查点: [ ] 限制≥3条 [ ] 具体可操作 [ ] 非空泛表述 -->
