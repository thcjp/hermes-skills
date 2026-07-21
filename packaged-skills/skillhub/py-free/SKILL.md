---
slug: py-free
name: py-free
version: "1.0.0"
displayName: Python基础版
summary: 编写可靠 Python 代码的基础能力，覆盖可变默认参数陷阱、import 规范与基础异常处理。
license: MIT
description: |-
  编写可靠 Python 代码的基础能力，覆盖可变默认参数陷阱、
  import 规范与基础异常处理。

  核心能力:

  - 可变默认参数陷阱识别与修复

  - import 顺序规范与循环依赖基础检测

  - 基础异常处理与上下文管理器

  - 基础类型提示与 None 检查

  适用场景:

  - 日常 Python 开发、代码审查、缺陷修复

  - 独立开发者与一人公司效率提升

  - 自动化工作流中的 Python 代码生成

  差异化:基础版聚焦 Python 高频陷阱防护，去除了高级版的并发陷阱（GIL、asyncio）、性能调优与元类高级用法。
tags:
- Other
tools:
  - read
  - exec
---
# Python 基础版

## 核心能力

- 可变默认参数陷阱识别：检测 def foo(items=[])、def foo(config={}) 等可变默认参数陷阱，推荐使用 None 与函数内初始化
- import 规范与循环依赖检测：按 PEP 8 规范排序 import（标准库、第三方、本地），检测基础的循环依赖
- 基础异常处理：区分 except Exception 与 except BaseException，避免裸 except 与吞没异常，推荐 logging 记录
- 上下文管理器使用：对文件、锁、连接等资源使用 with 语句，确保资源正确释放
- 基础类型提示与 None 检查：为函数添加 type hints，识别潜在的 None 解引用风险

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 可变参数检查 | Python 函数定义 | 风险点列表与修复建议 |
| import 整理 | Python 模块文件 | 排序后的 import 语句 |
| 异常处理审查 | try-except 代码块 | 规范化建议与潜在问题 |
| 资源管理 | 涉及文件/连接的方法 | with 语句改写建议 |
| 类型提示补全 | 函数签名 | 带类型提示的函数签名 |

**不适用于**：复杂并发（asyncio、threading、multiprocessing、GIL）、性能调优（Cython、NumPy 优化）、元类与描述符深度用法、C 扩展与原生绑定等场景（请使用高级版）

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 读取待审查或待生成的 Python 代码
3. 按核心能力维度逐项分析（可变参数、import、异常、资源、类型提示）
4. 给出问题清单与修复建议，必要时生成改写后的代码
5. 输出结果与执行日志

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| code | string | 是 | 待审查的 Python 代码片段或文件路径 |
| focus | string | 否 | 关注维度，可选: mutable/import/exception/resource/typing/all，默认: all |
| strict_level | string | 否 | 审查严格度，可选: strict/normal/loose，默认: normal |
| output_format | string | 否 | 输出格式，可选: markdown/json/text，默认: markdown |
| style | string | 否 | 输出风格参考，可选: 简洁/详细，默认: 详细 |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "B",
    "total_score": 80,
    "max_score": 100,
    "summary": "发现 1 个可变默认参数陷阱与 1 个裸 except 问题",
    "details": [
      {
        "item": "可变默认参数",
        "status": "fail",
        "score": 60,
        "comment": "第 8 行 def add_item(item, items=[]) 使用可变默认参数，建议改为 items=None"
      },
      {
        "item": "import 规范",
        "status": "pass",
        "score": 95,
        "comment": "import 顺序符合 PEP 8"
      },
      {
        "item": "异常处理",
        "status": "warn",
        "score": 75,
        "comment": "第 15 行使用裸 except，建议捕获具体异常类型"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "将 items=[] 改为 items=None，并在函数内初始化为空列表",
        "expected_gain": "+10分"
      },
      {
        "priority": "medium",
        "suggestion": "将裸 except 改为 except Exception as e 并记录日志",
        "expected_gain": "+5分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 代码无法解析 | 语法错误或不完整的 Python 代码 | 提示用户修正语法后重试，标记错误位置 |
| 文件不存在 | code 参数为路径但文件不存在 | 检查路径是否为绝对路径，确认文件存在 |
| focus 维度无效 | focus 参数值不在可选范围内 | 提示可选值列表，建议使用默认值 all |
| 输出格式不支持 | output_format 参数值无效 | 回退为默认 markdown 格式并提示 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md规范的任意AI Agent
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 建议 3.8 及以上（涉及 type hints、walrus operator 等）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行Python代码审查

## 案例展示

### 示例1：审查一个工具函数

```
输入: code=utils.py 片段, focus=mutable
处理: 识别 def add_item(item, items=[]) -> 标记陷阱 -> 给出修复建议
输出: 可变默认参数得分 60，建议改为 items=None 并在函数内初始化
```

### 示例2：整理 import 顺序

```
输入: code=app.py, focus=import
处理: 解析现有 import -> 按 PEP 8 分组排序 -> 生成整理后的 import
输出: 标准 -> 第三方 -> 本地 三组排序后的 import 语句
```

## 常见问题

### Q1: 如何开始使用 Python 基础版？
A: 请先阅读使用流程章节，准备待审查的 Python 代码，然后按"输入格式"提供 code 与 focus 参数即可。

### Q2: 审查严格度 strict、normal、loose 有何区别？
A: strict 会标记所有潜在风险点（包括风格问题）；normal 聚焦明确的缺陷；loose 仅报告高风险问题。建议初次使用选择 normal。

### Q3: Python 基础版支持 asyncio 与并发问题审查吗？
A: 不支持。基础版聚焦可变默认参数、import、异常、资源与类型提示五个维度，如需审查 asyncio、GIL、线程安全、性能调优，请升级至高级版。

### Q4: 如何获取 asyncio 并发、GIL、性能调优、元类等高级能力？
A: 这些属于高级版能力。基础版聚焦高频陷阱防护，如需深入并发（asyncio、threading、multiprocessing）、性能调优（Cython、profiling）与元类深度用法，请升级至高级版。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 不支持并发问题审查（asyncio、threading、multiprocessing、GIL、线程安全集合）
- 不支持性能调优（Cython、NumPy 优化、profiling、内存分析）
- 不支持元类与描述符的深度用法分析
- 不支持 C 扩展与原生绑定（Cython、ctypes、cffi）
- 不支持异步上下文管理器的深度分析
- 不支持框架深度问题（Django、Flask、FastAPI 等框架特定陷阱）
- 类型提示仅做基础检查，不支持 mypy / pyright 的完整类型系统分析
