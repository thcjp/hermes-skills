<!--
  ============================================================
  设计模式: Pipeline (多步骤流水线)
  适用场景: 多步骤依赖流程, 数据处理全流程, 端到端转换
  推荐行数: 200-350行, 上限400行
  核心结构: 步骤间gate条件 + assets/+references/+三目录齐全
  ============================================================
  使用说明:
  1. 复制本文件, 重命名为 SKILL.md
  2. 填充所有 {{占位符}} 为具体内容
  3. 删除所有 <!-- 写作指引 --> 和 <!-- 质量检查点 --> 注释
  4. 将中间模板放到 assets/ 目录
  5. 将流程规范/检查清单放到 references/ 目录
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

<!-- 写作指引: Pipeline模式的能力应聚焦于"端到端流程"+"步骤间衔接"+"质量gate"。 -->

- {{capability_1}} - {{step_count}}步端到端{{pipeline_type}}流程
- {{capability_2}} - 步骤间自动质量gate检查
- {{capability_3}} - 支持{{variation_1}}等多种处理模式
- {{capability_4}} - 失败自动重试+断点续传
- {{capability_5}} - 全流程可追溯, 输出执行日志

<!-- 质量检查点: [ ] 能力≥4条 [ ] 提及步骤数 [ ] 提及gate/重试 -->

## 适用场景

<!-- 写作指引: Pipeline模式的场景应描述"用户要完成什么多步骤任务"。 -->

- 用户说"{{user_phrase_1}}" → 执行{{pipeline_desc_1}}
- 用户说"{{user_phrase_2}}" → 执行{{pipeline_desc_2}}
- 用户说"{{user_phrase_3}}" → 执行{{pipeline_desc_3}}
- 不适用: {{exclusion_scenario}}

<!-- 质量检查点: [ ] 场景≥3个 [ ] 含多步骤描述 [ ] 含不适用场景 -->

## 使用流程

<!-- 写作指引: Pipeline模式的流程是核心, 需要详细描述每个步骤和步骤间的gate条件。 -->

### Step 1: {{step_1_name}}
{{step_1_instruction}}

**输入**: {{step_1_input}}
**处理**:
1. {{step_1_action_1}}
2. {{step_1_action_2}}
**输出**: {{step_1_output}}

**Gate条件** (满足后进入Step 2):
- {{gate_1_1}}
- {{gate_1_2}}

### Step 2: {{step_2_name}}
{{step_2_instruction}}

**输入**: Step 1的输出
**处理**:
1. {{step_2_action_1}}
2. {{step_2_action_2}}
**输出**: {{step_2_output}}

**Gate条件** (满足后进入Step 3):
- {{gate_2_1}}
- {{gate_2_2}}

### Step 3: {{step_3_name}}
{{step_3_instruction}}

**输入**: Step 2的输出
**处理**:
1. {{step_3_action_1}}
2. {{step_3_action_2}}
**输出**: {{step_3_output}}

**Gate条件** (满足后进入Step 4):
- {{gate_3_1}}
- {{gate_3_2}}

### Step 4: {{step_4_name}} (最终输出)
{{step_4_instruction}}

**输入**: Step 3的输出
**处理**:
1. {{step_4_action_1}}
2. {{step_4_action_2}}
**输出**: 最终结果 {{final_output_desc}}

**流程规范参考**: `references/{{pipeline_spec}}`

<!-- 质量检查点: [ ] 步骤≥4个 [ ] 每步有输入/处理/输出 [ ] 步骤间有Gate条件 -->

## 输入格式

<!-- 写作指引: Pipeline模式的输入通常包含原始数据和流程配置参数。 -->

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| {{param_1}} | string | 是 | {{desc_1}} |
| {{param_2}} | string | 否 | {{desc_2}}, 默认: {{default_2}} |
| mode | string | 否 | 处理模式, 可选: {{mode_options}}, 默认: {{default_mode}} |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

<!-- 质量检查点: [ ] 参数表格化 [ ] 含模式参数 [ ] 含重试/续传参数 -->

## 输出格式

<!-- 写作指引: Pipeline模式的输出应包含最终结果和执行日志。 -->

```json
{
  "success": true,
  "data": {
    "final_result": {
      {{final_field_1}}: "{{final_desc_1}}",
      {{final_field_2}}: "{{final_desc_2}}",
      {{final_field_3}}: "{{final_desc_3}}"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "{{step_1_name}}",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "{{step_1_log}}"
      },
      {
        "step": 2,
        "name": "{{step_2_name}}",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "{{step_2_log}}"
      },
      {
        "step": 3,
        "name": "{{step_3_name}}",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "{{step_3_log}}"
      },
      {
        "step": 4,
        "name": "{{step_4_name}}",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "{{step_4_log}}"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/{{intermediate_template}}`

<!-- 质量检查点: [ ] 有JSON示例 [ ] 含执行日志 [ ] 含Gate统计 [ ] 引用assets模板 -->

## 异常处理

<!-- 写作指引: Pipeline模式的异常应覆盖步骤失败、Gate不通过、断点续传等场景。 -->

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| Step {{n}}处理失败 | {{step_failure_reason}} | 自动重试(最多max_retries次), 仍失败则记录断点, 暂停流程 |
| Gate条件不满足 | Step {{n}}输出质量不达标 | 返回Step {{n}}重新处理, 或提示用户调整输入 |
| 输入数据格式错误 | {{param_1}}格式不符合要求 | 列出期望格式, 提供示例, 中止流程 |
| 断点续传失败 | 缓存的中间产物已过期或损坏 | 从Step 1重新开始, 清除旧缓存 |
| 超时 | 总处理时间超过{{timeout}}分钟 | 返回已完成步骤的结果, 标记为partial |
| {{error_scene_6}} | {{error_reason_6}} | {{error_fix_6}} |

<!-- 质量检查点: [ ] 异常≥5种 [ ] 表格化 [ ] 含Gate异常 [ ] 含断点续传异常 -->

## 依赖说明

<!-- 写作指引: Pipeline模式通常依赖LLM + 多个参考文件 + 中间模板。 -->

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM执行各步骤的智能处理, 推荐GPT-4/智谱GLM-4/DeepSeek |
| `references/{{pipeline_spec}}` | 文件 | 是 | {{spec_desc}} |
| `assets/{{intermediate_template}}` | 文件 | 是 | {{template_desc}} |
| `references/{{quality_checklist}}` | 文件 | 否 | {{checklist_desc}} |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

<!-- 质量检查点: [ ] 表格化 [ ] 含多文件依赖 [ ] 含国内替代方案 -->

## 案例展示

<!-- 写作指引: Pipeline模式的案例应展示完整的"输入→各步骤日志→最终输出"过程。 -->

### 示例1: {{case_1_title}}
**输入**:
```json
{
  "{{param_1}}": "{{case_1_param_1}}",
  "{{param_2}}": "{{case_1_param_2}}",
  "mode": "{{case_1_mode}}"
}
```
**执行日志**:
```
Step 1 [{{step_1_name}}]: {{case_1_step1_log}} ✓ (1.2s)
  Gate: {{case_1_gate1}} ✓
Step 2 [{{step_2_name}}]: {{case_1_step2_log}} ✓ (3.5s)
  Gate: {{case_1_gate2}} ✓
Step 3 [{{step_3_name}}]: {{case_1_step3_log}} ✓ (2.1s)
  Gate: {{case_1_gate3}} ✓
Step 4 [{{step_4_name}}]: {{case_1_step4_log}} ✓ (0.8s)
```
**最终输出**:
```
{{case_1_final_output}}
```

### 示例2: {{case_2_title}}
**输入**:
```json
{
  "{{param_1}}": "{{case_2_param_1}}",
  "mode": "{{case_2_mode}}"
}
```
**执行日志**:
```
Step 1 [{{step_1_name}}]: {{case_2_step1_log}} ✓ (0.9s)
  Gate: {{case_2_gate1}} ✓
Step 2 [{{step_2_name}}]: {{case_2_step2_log}} ✓ (2.8s)
  Gate: {{case_2_gate2}} ✗ → 重试
Step 2 [{{step_2_name}}]: {{case_2_step2_retry_log}} ✓ (3.1s)
  Gate: {{case_2_gate2}} ✓
Step 3 [{{step_3_name}}]: {{case_2_step3_log}} ✓ (1.5s)
  Gate: {{case_2_gate3}} ✓
Step 4 [{{step_4_name}}]: {{case_2_step4_log}} ✓ (0.6s)
```
**最终输出**:
```
{{case_2_final_output}}
```

### 示例3: 边界情况 - {{case_3_title}}
**输入**:
```json
{
  "{{param_1}}": "{{case_3_param_1}}",
  "max_retries": 1
}
```
**执行日志**:
```
Step 1 [{{step_1_name}}]: {{case_3_step1_log}} ✓ (1.1s)
  Gate: {{case_3_gate1}} ✓
Step 2 [{{step_2_name}}]: {{case_3_step2_log}} ✗ → 重试(1/1)
Step 2 [{{step_2_name}}]: {{case_3_step2_retry_log}} ✗ → 超过最大重试次数
流程暂停, 断点: Step 2
```
**输出**(部分结果):
```json
{
  "success": false,
  "error": "Step 2 failed after 1 retries",
  "data": {
    "completed_steps": [1],
    "checkpoint": "step_2",
    "partial_result": "{{case_3_partial}}"
  }
}
```

<!-- 质量检查点: [ ] 示例≥3个 [ ] 含执行日志 [ ] 含Gate重试 [ ] 含边界情况(失败) -->

## 常见问题

### Q: {{faq_q_1}}?
A: {{faq_a_1}}

### Q: {{faq_q_2}}?
A: {{faq_a_2}}

### Q: {{faq_q_3}}?
A: {{faq_a_3}}

### Q: {{faq_q_4}}?
A: {{faq_a_4}}

<!-- 质量检查点: [ ] FAQ≥3条 [ ] 问答格式 [ ] 覆盖常见疑问 -->

## 已知限制

<!-- 写作指引: Pipeline模式的限制应说明流程能力的边界。 -->

- {{limitation_1}}
- {{limitation_2}}
- {{limitation_3}}
- {{limitation_4}}
- {{limitation_5}}

<!-- 质量检查点: [ ] 限制≥3条 [ ] 具体可操作 [ ] 非空泛表述 -->
