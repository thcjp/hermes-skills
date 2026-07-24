---
slug: "docker-sandbox"
name: "docker-sandbox"
version: 1.0.1
displayName: "Docker Sandbox"
summary: "建管Docker沙箱VM环境,让Agent安全执行不可信代码。Create and manage Docker sandboxed VM environments for safe agen"
license: "Proprietary"
description: |-
  Create and manage Docker sandboxed VM environments for safe agent execution。Use when running unt。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策.
tags:
  - Operations
  - 容器
  - Docker
  - DevOps
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Development"
---
# Docker Sandbox

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |
| 零日漏洞检测与防护规则下发 | 不支持 | 支持 |

## 核心能力

- Create and manage Docker sandboxed VM environments for safe agent execution
- Use when running unt
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 代码处理 | 源代码文件路径 | 分析报告与修改建议 |
| 容器管理 | 镜像名与运行参数 | 容器状态与日志输出 |
| 沙箱管理 | 镜像与资源限制 | 沙箱ID与隔离状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Create a sandbox for the current project

```bash
docker sandbox create --name my-sandbox claude .
```

This creates a VM-isolated sandbox with:

1. The current directory mounted via virtiofs
2. Node.js, git, and standard dev tools pre-installed
3. Network proxy with allowlist controls

### Run commands inside

```bash
docker sandbox exec my-sandbox node --version
docker sandbox exec my-sandbox npm install -g some-package
docker sandbox exec -w /path/to/workspace my-sandbox bash -c "ls -la"
```

### Run an agent directly

```bash
docker sandbox run claude . -- -p "What files are in this project?"
# ...
docker sandbox run my-sandbox -- -p "Analyze this codebase"
```

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | docker-sandbox处理的内容输入 |,  |
| content | string | 否 | docker-sandbox处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "sandbox 相关配置参数",
    result: "sandbox 相关配置参数",
    result: "sandbox 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 输入content为空 | 用户未提供必要信息 | 提示用户提供content, 并给出示例格式 |
| 输入内容过长(>5000字) | 超出单次处理能力 | 建议分段处理, 每段不超过2000字 |
| 风格参数不识别 | 传入不支持的风格 | 列出支持的风格选项, 使用默认风格 |
| 生成内容不达标 | 质量校验未通过 | 自动1次, 仍不达标则标注问题返回 |
| 其他异常 | 内部处理异常 | 检查输入后 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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

### 示例1：基础用法

```
### Create a sandbox for the current project(补充)
# ...
```bash
docker sandbox create --name my-sandbox claude .
```
# ...
This creates a VM-isolated sandbox with:
# ...
* The current directory mounted via virtiofs
* Node.js, git, and standard dev tools pre-installed
* Network proxy with allowlist controls
# ...
### Run commands inside(补充)
# ...
```bash
docker sandbox exec my-sandbox node --version
docker sandbox exec my-sandbox npm install -g some-package
docker sandbox exec -w /path/to/workspace my-sandbox bash -c "ls -la"
```
```

## 常见问题

### Q1: 如何开始使用Docker Sandbox？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

