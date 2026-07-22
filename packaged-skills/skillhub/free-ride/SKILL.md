---
slug: "free-ride"
name: "free-ride"
version: "1.0.11"
displayName: "Free Ride"
summary: "Manages free AI models from OpenRouter for SkillHub."
license: "Proprietary"
description: |-
  Manages free AI models from OpenRouter for SkillHub。核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Integrations
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# Free Ride

## 核心能力

- Manages free AI models from OpenRouter for SkillHub
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
| mode | string | 否 | 处理模式, 可选: json/text/markdown, 默认: 默认值 |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明"
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

中间产物模板参考: `assets/（根据实际场景填充）`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| Step （根据实际场景填充）处理失败 | 按流程执行 | 自动执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令(最多max_retries次), 仍失败则记录断点, 暂停流程 |
| Gate条件不满足 | Step （根据实际场景填充）输出质量不达标 | 返回Step （根据实际场景填充）重新处理, 或提示用户调整输入 |
| 输入数据格式错误 | content格式不符合要求 | 列出期望格式, 提供示例, 中止流程 |
| 断点续传失败 | 缓存的中间产物已过期或损坏 | 从Step 1重新开始, 清除旧缓存 |
| 超时 | 总处理时间超过（根据实际场景填充）分钟 | 返回已完成步骤的结果, 标记为partial |
| 其他异常 | 内部处理异常 | 检查输入后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 |

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

### Q1: 如何开始使用Free Ride？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Free Ride有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 
