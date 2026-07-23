---
slug: "vscode-node"
name: "vscode-node"
version: "1.0.2"
displayName: "VS Code Node"
summary: "Operate on code through a VS Code/Cursor IDE connected as an SkillHub Node."
license: "Proprietary"
description: |-
  Operate on code through a VS Code/Cursor IDE connected as an SkillHub
  Node。Provides 40+ commands。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Development
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# VS Code Node

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Operate on code through a VS Code/Cursor IDE connected as an SkillHub | 支持 | 支持 |
| Provides 40+ commands | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Operate on code through a VS Code/Cursor IDE connected as an SkillHub
  Node
- Provides 40+ commands
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

#
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

### Read a file

```text
nodes invoke --node "my-vscode" --invokeCommand "vscode.file.read" --invokeParamsJson '{"path":"src/main.ts"}'
→ { content, totalLines, language }
```

### Find all references

```text
nodes invoke --node "my-vscode" --invokeCommand "vscode.lang.references" --invokeParamsJson '{"path":"src/main.ts","line":10,"character":5}'
→ { locations: [{ path, line, character }] }
```

### Git status + commit

```text
nodes invoke --node "my-vscode" --invokeCommand "vscode.git.status"
→ { branch, staged, modified, untracked, ahead, behind }

nodes invoke --node "my-vscode" --invokeCommand "vscode.git.stage" --invokeParamsJson '{"paths":["src/main.ts"]}'
nodes invoke --node "my-vscode" --invokeCommand "vscode.git.commit" --invokeParamsJson '{"message":"fix: resolve type error"}'
```

### Delegate to Cursor Agent

```text
nodes invoke --node "my-vscode" --invokeCommand "vscode.agent.run" --invokeParamsJson '{"prompt":"Add error handling to all API endpoints","mode":"plan"}' --invokeTimeoutMs 180000 --timeoutMs 185000
→ { output, exitCode }
```

## 常见问题

### Q1: 如何开始使用VS Code Node？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: VS Code Node有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

