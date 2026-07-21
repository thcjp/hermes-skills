---
slug: azure-cli
name: azure-cli
version: "1.0.0"
displayName: azure-cli
summary: Comprehensive Azure Cloud Platform management via command-line interface
license: MIT
description: |-
  Comprehensive Azure Cloud Platform management via command-line interface

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

tags:
- Development
tools:
  - - read
- exec
---
# azure-cli

## 核心能力


## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景
### 基础使用

执行基础使用操作,处理用户输入并返回结果。

**输入**: 用户提供基础使用所需的参数和指令。

**输出**: 返回基础使用的处理结果。

- 执行`基础使用`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`基础使用`相关配置参数进行设置
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: Comprehensive、Azure、Cloud、Platform、management、via、command、line、interface。这些能力在上述核心功能中均有对应处理逻辑。
### 源能力映射
本skill覆盖源skill的以下能力点:

| 源能力点 | 支持状态 | 实现方式 |
|:---------|:---------|:---------|
| Authentication Methods | 支持 | 通过核心功能实现对应能力 |

**输入**: 用户提供源能力映射所需的指令和必要参数。
**处理**: 按照skill规范执行源能力映射操作,遵循单一意图原则。
**输出**: 返回源能力映射的执行结果,包含操作状态和输出数据。
### 领域术语
本skill涉及以下领域术语: `virtual`, `apps`, `automation`, `provider`, `kubernetes`, `verbose`, `github`, `exit`, `token`, `networking`, `formatting`, `rbac`, `identify`, `sets`, `handling`

**处理**: 按照skill规范执行领域术语操作,遵循单一意图原则。
**输出**: 返回领域术语的执行结果,包含操作状态和输出数据。

## 使用流程

### Installation

**macOS:**

```bash
brew install azure-cli
```

**Linux (Ubuntu/Debian):**

```bash
curl -sL https://aka.ms/InstallAzureCliLinux | bash
```

**Windows:**

```powershell
choco install azure-cli
```

**Verify Installation:**

```bash
az --version          # Show version
az --help             # Show general help
```

### First Steps

```bash
az login

az account list

az account set --subscription "My Subscription"

az group create -g myResourceGroup -l eastus

az group list
```

### 命令参数说明

- `-sL`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

### 命令参数说明

- `-sL`: 命令参数,用于指定操作选项

### 命令参数说明

- `-sL`: 命令参数,用于指定操作选项

### 命令参数说明

- `-sL`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
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

### 示例1：基础用法

```
### Installation

**macOS:**

```bash
brew install azure-cli
```

**Linux (Ubuntu/Debian):**

```bash
curl -sL https://aka.ms/InstallAzureCliLinux | bash
```

**Windows:**

```powershell
choco install azure-cli
```

**Verify Installation:**

```bash
az --version          # Show version
az --help             # Show general help
```

### First Steps

```bash
az login

az account list

az account set --subscription "My Subscription"

az group create -g myResourceGroup -l eastus

az group list
```
```

## 常见问题

### Q1: 如何开始使用azure-cli？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: azure-cli有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖云服务，需要网络连接
