---
slug: screen-monitor
name: screen-monitor
version: "1.0.1"
displayName: Screen Monitor
summary: Dual-mode screen sharing and analysis. Model-agnostic (Gemini/ai-assistant/Qwen3-VL).
license: MIT
description: |-
  Dual-mode screen sharing and analysis。Model-agnostic (Gemini/ai-assistant/Qwen3-VL)。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Screen Monitor

This skill provides two ways for the agent to see and interact with your screen.

## 🟢 Path A: Fast Share (WebRTC)

*Best for: Quick visual checks, restricted browsers, or non-technical environments.*

### Tools

* **`screen_share_link`**: Generates a local WebRTC portal URL.
* **`screen_analyze`**: Captures the current frame from the portal and analyzes it with vision.

**Usage:**

```bash
bash command:"{baseDir}/references/get-share-url.sh"

bash command:"{baseDir}/references/screen-analyze.sh"
```

---

## 🔵 Path B: Full Control (Browser Relay)

*Best for: Deep debugging, UI automation, and clicking/typing in tabs.*

### Setup

1. Run `clawdbot browser extension install`.
2. Load the unpacked extension from `clawdbot browser extension path`.
3. Click the Clawdbot icon in your Chrome toolbar to **Attach**.

### Tools

* **`browser action:snapshot`**: Take a precise screenshot of the attached tab.
* **`browser action:click`**: Interact with elements (requires `profile="chrome"`).

---

## Technical Details

* **Port**: 18795 (WebRTC Backend)
* **Files**:
  + `web/screen-share.html`: The sharing portal.
  + `references/backend-endpoint.js`: Frame storage server.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
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

## 核心能力

- Dual-mode screen sharing and analysis
- Model-agnostic (Gemini/ai-assistant/Qwen3-VL)
- 触发关键词: screen, mode, monitor, analysis, sharing, dual

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

### Q1: 如何开始使用Screen Monitor？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Screen Monitor有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
- 性能取决于底层模型能力
