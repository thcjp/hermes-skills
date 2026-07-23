---
slug: "mac-node-snapshot"
name: "mac-node-snapshot"
version: "1.0.0"
displayName: "mac-node-snapshot"
summary: "经SkillHub screen record权限友好地截macOS屏幕"
license: "Proprietary"
description: |-
  A robust, permission-friendly method to capture macOS screens via SkillHub
  screen。record。Use when 用户需要mac-node-snapshot相关功能时使用。不适用于超出本技能能力范围的复杂需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Security
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
---
# mac-node-snapshot

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

Uses node screen.record to record a 1-second clip and extract a high-quality PNG frame. This workflow bypasses common screencapture permission issues and ensures a reliable image return.
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

All paths are **relative** to `{skill}`.

```bash
mkdir -p "{skill}/tmp" \
&& skill-platform nodes screen record --node "<node>" --duration 1000 --fps 10 --no-audio --out "{skill}/tmp/snap.mp4" \
&& ffmpeg -hide_banner -loglevel error -y -ss 00:00:00 -i "{skill}/tmp/snap.mp4" -frames:v 1 "{skill}/tmp/snap.png"
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态


## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | mac-node-snapshot处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "snapshot_result": "snapshot_result_value",
      "snapshot_metadata": "snapshot_metadata_value",
      "snapshot_status": "snapshot_status_value"
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

中间产物模板参考: `assets/mac-node-snapshot_template`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| Step Mac Node Snapshot 核心处理处理失败 | 按流程执行 | 自动(最多max_retries次), 仍失败则记录断点, 暂停流程 |
| Gate条件不满足 | Step Mac Node Snapshot 智能分析输出质量不达标 | 返回Step Mac Node Snapshot 智能分析重新处理, 或提示用户调整输入 |
| 输入数据格式错误 | content格式不符合要求 | 列出期望格式, 提供示例, 中止流程 |
| 断点续传失败 | 缓存的中间产物已过期或损坏 | 从Step 1重新开始, 清除旧缓存 |
| 超时 | 总处理时间超过Mac Node Snapshot 批量处理分钟 | 返回已完成步骤的结果, 标记为partial |
| 其他异常 | 内部处理异常 | 检查输入后 |

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
All paths are **relative** to `{skill}`.

```bash
mkdir -p "{skill}/tmp" \
&& skill-platform nodes screen record --node "<node>" --duration 1000 --fps 10 --no-audio --out "{skill}/tmp/snap.mp4" \
&& ffmpeg -hide_banner -loglevel error -y -ss 00:00:00 -i "{skill}/tmp/snap.mp4" -frames:v 1 "{skill}/tmp/snap.png"
```
```

## 常见问题

### Q1: 如何开始使用mac-node-snapshot？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: mac-node-snapshot有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

