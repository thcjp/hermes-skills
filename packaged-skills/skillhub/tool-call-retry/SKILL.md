---
slug: "tool-call-retry"
name: "tool-call-retry"
version: "1.0.1"
displayName: "tool-call-retry"
summary: "Auto retry & fix LLM tool calls with exponential backoff, format validation,"
license: "Proprietary"
description: |-
  Auto retry & fix LLM tool calls with exponential backoff, format validation,
  error correction, bo。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
  - Other
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# tool-call-retry

## 核心能力

- Auto retry & fix LLM tool calls with exponential backoff, format validation,
  error correction, bo
#
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
|--------|------|------|------|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明"
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

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

### 基础用法（零配置）

```typescript
const fetchWeather = async (params: { city: string }) => {
  const res = await fetch(`https://api.weather.com/${params.city}`);
  return res.json();
};

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


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪。

### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界。

