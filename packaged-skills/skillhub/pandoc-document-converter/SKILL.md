---
name: "Pandoc Document Converter 核心处理"
slug: "pandoc-document-converter"
displayName: "Pandoc文档转换"
version: "1.0.0"
summary: "使用Pandoc进行多格式文档转换,支持Markdown、HTML、PDF、Word等格式互转"
description: |-
  API封装工具。适用于需要调用外部API的场景，API请求参数→API响应数据。
  Use when 用户说"Pandoc Document Converter 智能分析"、Pandoc Document Converter 智能分析时使用。
  不适用于需要人工判断的复杂场景。
license: "Proprietary"
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 文档处理
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "文档处理,工具,效率"
---
# Pandoc Document Converter 批量处理

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Pandoc文档转换c进行多格式文档转换 | 不支持 | 支持 |
| 跨平台任务同步 | 不支持 | 支持 |
| 智能优先级排序 | 不支持 | 支持 |
| 团队协作与权限管理 | 不支持 | 支持 |
| 自动化提醒与跟进 | 不支持 | 支持 |

## 核心能力

- Pandoc Document Converter 错误重试
- Pandoc Document Converter 多格式支持
- Pandoc Document Converter 扩展能力9
#
## 适用场景

- 用户说"Pandoc Document Converter 扩展能力10" → 执行API调用
- 用户说"Pandoc Document Converter 扩展能力11" → 执行API调用
- 用户说"Pandoc Document Converter 扩展能力12" → 执行API调用
- 不适用: 需要人工判断的复杂场景

## 使用流程

### Step 1: 解析输入参数
Pandoc文档转换校验输入数据格式与必填字段，准备处理上下文

### Step 2: 执行核心处理逻辑
根据参数执行主要功能，处理中间状态与边界情况

### Step 3: 格式化并返回结果
将处理结果按输出规范封装，包含状态与数据

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "converter 相关配置参数",
    result: "converter 相关配置参数"
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 其他异常 | 内部处理异常 | 检查输入后 |
| 其他异常 | 内部处理异常 | 检查输入后 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 示例1: 基础用法
**输入**: 示例数据
**输出**: 示例数据

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪。

### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界。

## 已知限制

- 需要LLM支持

