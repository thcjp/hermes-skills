---
slug: vector-control
name: vector-control
version: "1.0.1"
displayName: Vector Control
summary: Control a Vector robot via Wirepod’s local HTTP API on the same network.
  Use when you need to mov...
license: MIT
description: |-
  Control a Vector robot via Wirepod’s local HTTP API on the same network。Use when you need to mov。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Integrations
tools:
  - - read
- exec
---
# Vector Control

## 核心能力

Control Vector through Wirepod’s `/api-sdk/*` endpoints and the camera stream at `/cam-stream`. Use this skill for movement, speech, camera snapshots, patrols, and exploration from the Pi.
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。


## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

Use the bundled script:

```bash
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> assume
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> say --text "Hello Dom"
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> move --lw 160 --rw 160 --time 1.5
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> snapshot --out /tmp/vector.mjpg
```

### Find ESN/serial

If you don’t have it, read:

* `/etc/wire-pod/wire-pod/jdocs/botSdkInfo.json`

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | （根据实际场景填充） | 是 | 相关说明 |
| content | （根据实际场景填充） | 否 | 相关说明 |

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

- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断

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

### 示例1：基础用法

```
Use the bundled script:

```bash
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> assume
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> say --text "Hello Dom"
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> move --lw 160 --rw 160 --time 1.5
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> snapshot --out /tmp/vector.mjpg
```

### Find ESN/serial

If you don’t have it, read:

* `/etc/wire-pod/wire-pod/jdocs/
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步

## 常见问题

**Q: 如何处理异常输入?**
A: 系统会自动检测并返回错误提示, 同时提供修复建议。

**Q: 支持哪些输入格式?**
A: 支持标准文本、JSON、CSV等常见格式。
