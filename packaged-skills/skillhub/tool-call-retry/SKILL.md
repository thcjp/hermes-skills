---
slug: "tool-call-retry"
name: "tool-call-retry"
version: 1.0.2
displayName: "tool-call-retry"
summary: "指数退避自动重试并修复LLM工具调用,格式校验/纠错。Auto retry & fix LLM tool calls with exponential backoff, format val"
license: "MIT"
description: |-
  Auto retry & fix LLM tool calls with exponential backoff, format validation,
  error correction, bo。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策.
tags:
  - Other
  - 工具
  - 效率
  - api
  - error
  - const
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# tool-call-retry

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| tool-call-retry格式校验 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

- Auto retry & fix LLM tool calls with exponential backoff, format validation,
  error correction, bo
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

* 所有调用外部API/工具的Agent场景
* 不稳定的第三方服务调用
* 大模型工具调用格式错误自动修复
* 高可靠性要求的Agent执行链路

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "retry 相关配置参数",
    result: "retry 相关配置参数"
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 基础用法（零配置）

```typescript
const fetchWeather = async (params: { city: string }) => {
  const res = await fetch(`https://api.weather.com/${params.city}`);
  return res.json();
};
// ...
const result = await skills.toolCallRetry({
  toolFn: fetchWeather,
  args: { city: "Beijing" }
});
```

### 带结果校验

```typescript
const result = await skills.toolCallRetry({
  toolFn: callLLM,
  args: { prompt: "Generate JSON output" },
  validatorFn: (res) => typeof res === "object" && res !== null && res.code === 0,
  maxRetries: 5
});
```

### 高级用法（错误自动修复）

```typescript
const result = await skills.toolCallRetry({
  toolFn: callDatabase,
  args: { sql: "SELECT * FROM users" },
  errorHandlerFn: async (error, attempt) => {
    if (error.message.includes("SQL syntax error")) {
      // 自动修复SQL语法
      const fixedSql = await fixSqlWithLLM(error.message);
      return { args: { sql: fixedSql } };
    }
    if (attempt >= 2) {
      // 重试2次失败后中止
      return { abort: true };
    }
  }
});
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪.
### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界.