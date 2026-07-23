---
name: "dashboard-analytics-tool"
slug: "dashboard-analytics-tool"
displayName: "仪表盘分析工具"
version: "1.0.0"
summary: "封装仪表盘分析API,请求参数直转响应数据,付费版独享批量与高级配置"
description: |-
  API封装工具。适用于需要调用外部API的场景，API请求参数→API响应数据。
  Use when 用户说"Dashboard Analytics Tool 核心处理"、Dashboard Analytics Tool 核心处理时使用。
  不适用于需要人工判断的复杂场景。
license: "Proprietary"
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
---
# Dashboard Analytics Tool 智能分析

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 仪表盘分析工具封装仪表盘分析 | 不支持 | 支持 |
| 仪表盘分析工具版独享批量与高级配置 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |

## 核心能力

- Dashboard Analytics Tool 实时监控
- Dashboard Analytics Tool 错误重试
- Dashboard Analytics Tool 多格式支持
#
## 适用场景

- 用户说"Dashboard Analytics Tool 扩展能力9" → 执行API调用
- 用户说"Dashboard Analytics Tool 扩展能力10" → 执行API调用
- 用户说"Dashboard Analytics Tool 扩展能力11" → 执行API调用
- 不适用: 需要人工判断的复杂场景

## 使用流程

### Step 1: 认证与权限校验
仪表盘分析工具验证用户身份与操作权限，加载租户配置

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
    result: "tool 相关配置参数",
    result: "tool 相关配置参数"
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

## 常见问题

### Q: 如何使用此Skill?
A: 请参考使用流程章节

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
