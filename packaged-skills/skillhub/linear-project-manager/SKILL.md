---
name: "Linear Project Manager 核心处理"
slug: "linear-project-manager"
displayName: "Linear项目管理"
version: 1.0.2
summary: "封装Linear项目管理API,请求参数直转响应数据,付费版独享批量与高级配置。API封装工具。适用于需要调用外部API的场景，API请求参数→API响应数据. Use when 用户说"L"
description: |-
  API封装工具。适用于需要调用外部API的场景，API请求参数→API响应数据.
  Use when 用户说"Linear Project Manager 智能分析"、Linear Project Manager 智能分析时使用.
  不适用于需要人工判断的复杂场景.
license: "MIT"
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 通用办公
  - 工具
  - 效率
  - linear
  - manager
  - api
  - project
category: "Automation"
---
# Linear Project Manager 批量处理

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Linear项目管理Linear项目管理 | 不支持 | 支持 |
| Linear项目管理版独享批量与高级配置 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |

## 核心能力

- Linear Project Manager 错误重试
- Linear Project Manager 多格式支持
- Linear Project Manager 扩展能力9
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

- 用户说"Linear Project Manager 扩展能力10" → 执行API调用
- 用户说"Linear Project Manager 扩展能力11" → 执行API调用
- 用户说"Linear Project Manager 扩展能力12" → 执行API调用
- 不适用: 需要人工判断的复杂场景

## 使用流程

### Step 1: 认证与权限校验
Linear项目管理验证用户身份与操作权限，加载租户配置

### Step 2: 执行管理操作
根据请求类型执行CRUD操作，更新系统状态

### Step 3: 返回操作结果
封装操作响应，记录审计日志并返回结果

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "manager 相关配置参数",
    result: "manager 相关配置参数"
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
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

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪.
### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界.
## 已知限制

- 需要LLM支持
- 数据处理能力受限于本地硬件资源
- 大数据量时分析性能可能显著下降
- 数据准确性依赖输入质量，无法自动修正脏数据
