---
slug: "meeting-note"
name: "meeting-note"
version: "1.0.0"
displayName: "Meeting Note"
summary: "探讨决策型会议纪要(结论/共识/分歧/行动项)+Zettelkasten连接"
license: "Proprietary"
description: |-
  探讨/决策型会议与谈话纪要（结论/共识/分歧/决策轨迹/隐含假设/风险机会/行动项）+ Zettelkasten 连接。Use when
  用户要整理会议纪要、复盘讨论、把多方探讨变成可执行资产。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
  - Productivity
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
---
# Meeting Note

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 探讨/决策型会议与谈话纪要（结论/共识/分歧/决策轨迹/隐含假设/风险机会/行动项）+ Zettelkasten 连接 | 支持 | 支持 |
| Use when | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- 探讨/决策型会议与谈话纪要（结论/共识/分歧/决策轨迹/隐含假设/风险机会/行动项）+ Zettelkasten 连接
- Use when
  用户要整理会议纪要、复盘讨论、把多方探讨变成可执行资产
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. **缺信息不硬猜**：未知信息统一用 `详情见说明` 标注（时间/地点/参会人/负责人/截止时间/数据来源等）。
2. **先分层再结构化**：先识别会议类型与决策状态（✅/⏳/❓），再按议题逐一结构化。
3. **强制交付物**（缺一不可）：
  + 结论/共识/分歧（带发言人+理由）
  + 决策轨迹（从提出→争论→收敛/搁置）
  + 隐含假设/房间里的大象（必须给"依据"）
  + 风险与机会（含缓释/利用建议）
  + 行动项（可衡量+责任人+截止时间+成功标准）
  + Zettelkasten 连接（≥2 条，使用 `[[文件名]]`）

---

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | meeting-note处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "note_result": "note_result_value",
      "note_metadata": "note_metadata_value",
      "note_status": "note_status_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/meeting-note_template`

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
## 案例展示

### 示例1：基础用法

```
* **缺信息不硬猜**：未知信息统一用 `详情见说明` 标注（时间/地点/参会人/负责人/截止时间/数据来源等）。
* **先分层再结构化**：先识别会议类型与决策状态（✅/⏳/❓），再按议题逐一结构化。
* **强制交付物**（缺一不可）：
  + 结论/共识/分歧（带发言人+理由）
  + 决策轨迹（从提出→争论→收敛/搁置）
  + 隐含假设/房间里的大象（必须给"依据"）
  + 风险与机会（含缓释/利用建议）
  + 行动项（可衡量+责任人+截止时间+成功标准）
  + Zettelkasten 连接（≥2 条，使用 `[[文件名]]`）

---
```

## 常见问题

### Q1: 如何开始使用Meeting Note？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Meeting Note有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

