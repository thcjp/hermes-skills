<!--
  ============================================================
  设计模式: Tool Wrapper (工具包装器)
  适用场景: 遵循某库/框架规范, 将外部工具/API包装为skill
  推荐行数: 80-150行, 上限200行
  核心结构: references/目录放规范文档
  ============================================================
  使用说明:
  1. 复制本文件, 重命名为 SKILL.md
  2. 填充所有 {{占位符}} 为具体内容
  3. 删除所有 <!-- 写作指引 --> 和 <!-- 质量检查点 --> 注释
  4. 将详细规范文档放到 references/ 目录
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
  Use when 用户说"{{trigger_phrase_1}}"、{{trigger_phrase_2}}时使用。
  不适用于{{exclusion_scenario}}。
license: Proprietary
tools:
  - read
  - exec
---

# {{display_name}}

## 核心能力

<!-- 写作指引: 列出3-5条具体能力, 每条能力应包含"能做什么"而非"是什么"。避免"帮助用户处理各种任务"等宽泛表述。 -->

- {{capability_1}}
- {{capability_2}}
- {{capability_3}}

<!-- 质量检查点: [ ] 能力≥3条 [ ] 每条含动词+对象 [ ] 无宽泛表述 -->

## 适用场景

<!-- 写作指引: 每个场景包含"用户会怎么说→skill做什么", 至少3个场景, 含1个不适用场景。 -->

- 用户说"{{user_phrase_1}}" → {{skill_action_1}}
- 用户说"{{user_phrase_2}}" → {{skill_action_2}}
- 用户说"{{user_phrase_3}}" → {{skill_action_3}}
- 不适用: {{exclusion_scenario}}

<!-- 质量检查点: [ ] 场景≥3个 [ ] 含"用户说"原话 [ ] 含不适用场景 -->

## 使用流程

<!-- 写作指引: 按步骤描述操作流程, 每步1-3句指引。Tool Wrapper模式重点是"如何调用工具/API"。 -->

### Step 1: {{step_1_name}}
{{step_1_instruction}}

### Step 2: {{step_2_name}}
{{step_2_instruction}}

### Step 3: {{step_3_name}}
{{step_3_instruction}}

<!-- 质量检查点: [ ] 步骤≥3个 [ ] 每步有具体操作 [ ] 步骤间有逻辑顺序 -->

## 输入格式

<!-- 写作指引: 说明输入参数, Tool Wrapper重点是工具/API的参数映射。 -->

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| {{param_1}} | {{type_1}} | 是 | {{desc_1}} |
| {{param_2}} | {{type_2}} | 否 | {{desc_2}} |

<!-- 质量检查点: [ ] 参数表格化 [ ] 必填/选填标注 [ ] 每参数有说明 -->

## 输出格式

<!-- 写作指引: 说明输出结构, Tool Wrapper重点是工具/API返回值的格式化。 -->

```json
{
  "success": true,
  "data": {
    {{output_field_1}}: "{{output_desc_1}}",
    {{output_field_2}}: "{{output_desc_2}}"
  },
  "error": null
}
```

<!-- 质量检查点: [ ] 有JSON示例 [ ] 含success/error字段 [ ] 字段有说明 -->

## 异常处理

<!-- 写作指引: 列出常见错误场景, 每行包含"场景|原因|处理方式"。 -->

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| {{error_scene_1}} | {{error_reason_1}} | {{error_fix_1}} |
| {{error_scene_2}} | {{error_reason_2}} | {{error_fix_2}} |
| {{error_scene_3}} | {{error_reason_3}} | {{error_fix_3}} |

<!-- 质量检查点: [ ] 异常≥3种 [ ] 表格化 [ ] 每项有处理方式 -->

## 依赖说明

<!-- 写作指引: 说明运行依赖, Tool Wrapper模式通常需要外部工具/API。 -->

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| {{dependency_1}} | {{dep_type_1}} | 是 | {{dep_desc_1}} |
| LLM | 模型 | 是 | 需要LLM理解用户意图并调用工具 |

<!-- 质量检查点: [ ] 表格化 [ ] 含LLM说明 [ ] 外部依赖明确 -->

## 案例展示

<!-- 写作指引: 至少2个输入→输出示例, 含1个边界情况。 -->

### 示例1: {{case_1_title}}
**输入**: {{case_1_input}}
**输出**: {{case_1_output}}

### 示例2: {{case_2_title}}
**输入**: {{case_2_input}}
**输出**: {{case_2_output}}

### 示例3: 边界情况 - {{case_3_title}}
**输入**: {{case_3_input}}
**输出**: {{case_3_output}}

<!-- 质量检查点: [ ] 示例≥2个 [ ] 含边界情况 [ ] 输入输出完整 -->

## 已知限制

<!-- 写作指引: 列出3-5条具体限制, 说明skill不能做什么。 -->

- {{limitation_1}}
- {{limitation_2}}
- {{limitation_3}}

<!-- 质量检查点: [ ] 限制≥3条 [ ] 具体可操作 [ ] 非空泛表述 -->
