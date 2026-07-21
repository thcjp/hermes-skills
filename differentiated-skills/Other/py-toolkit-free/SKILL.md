---
slug: py-toolkit-free
name: py-toolkit-free
version: "1.0.0"
displayName: Python工具包-免费版
summary: Python开发优选实践助手,避免可变默认参数、导入陷阱与常见运行时问题
license: Proprietary
edition: free
description: |-
  Python 开发优选实践助手免费版,面向个人开发者与学习者。核心能力:
  - Python 常见陷阱检测与修复建议
  - 类型提示与鸭子类型指导
  - 列表/字典/集合使用规范
  - 装饰器、闭包、生成器优选实践
  - GIL 与并发编程建议
  - 循环导入预防
  - pytest 测试编写指导

  适用场景:
  - 日常 Python 开发避坑
  - 代码审查参考
  - 学习 Python 高级特性
  - 编写可靠的生产级代码

  差异化:免费版覆盖核心陷阱与优选实践
tags:
- Python
- 编程规范
- 优选实践
- 代码质量
tools:
  - - read
- exec
---
# Python 工具包 - 免费版

## 概述

Python 工具包免费版是面向个人开发者的 Python 优选实践助手。覆盖 Python 开发中最常见的陷阱与高频问题,提供即查即用的修复建议与代码规范,帮助开发者写出可靠的生产级代码。

从可变默认参数到 GIL 并发限制,从循环导入到浮点数精度,全面覆盖 Python 开发中的雷区。

## 核心能力

### 1. 常见陷阱检测

识别 Python 开发中 13 类高频陷阱,提供修复建议与正确写法。

### 2. 类型系统指导

动态类型、类型提示(Type Hints)、鸭子类型的正确使用方式。

### 3. 集合操作规范

列表、字典、集合的常见陷阱与推导式优选实践。

### 4. 函数式编程

参数传递、闭包、装饰器、生成器的正确使用模式。

### 5. 并发编程建议

GIL 限制说明,threading、asyncio、multiprocessing 的选择策略。

### 6. 导入管理

循环导入预防,包结构与 `__init__.py` 优选实践。

### 7. 测试编写

pytest 框架使用,mock 与 fixtures 优选实践。

## 使用场景

### 场景一:避免可变默认参数陷阱

Python 中最常见的陷阱之一:可变默认参数在函数定义时只创建一次,所有调用共享同一实例。

```python
# 错误写法 - 所有调用共享同一个列表
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - 不是 [2]!

# 正确写法 - 使用 None 作为默认值
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2] - 正确
```

### 场景二:正确使用 is 与 ==

`is` 检查身份(同一对象),`==` 检查相等(值相同)。

```python
# is vs == 的陷阱
a = "hello"
b = "hello"
print(a == b)  # True - 值相等
print(a is b)  # True - 小字符串有缓存

# 长字符串可能不缓存
s1 = "a" * 1000
s2 = "a" * 1000
print(s1 == s2)  # True
print(s1 is s2)  # False - 不同对象!

# 正确做法:比较值用 ==,检查 None 用 is
if x is None:     # 正确
if x == None:     # 不推荐

# 检查类型用 isinstance,不用 type()
if isinstance(x, int):   # 正确,支持继承
if type(x) == int:       # 不推荐,不支持继承
```

### 场景三:安全处理文件与编码

文件操作必须使用上下文管理器,并显式指定编码。

```python
# 依赖说明
f = open('data.txt')
content = f.read()
# 忘记 f.close() -> 句柄泄漏

# 正确写法 - 使用 with 语句,指定编码
with open('data.txt', encoding='utf-8') as f:
    content = f.read()
# 文件自动关闭

# 浮点数精度问题
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False

# 金额计算使用 Decimal
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))  # True
```

## 不适用场景

以下场景Python工具包-免费版不适合处理：

- 无明确技术栈的模糊需求
- 纯架构设计决策
- 运维部署管理


## 触发条件

需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于非本工具能力范围的需求。


## 快速开始

### 常见陷阱速查

```python
# 1. 可变默认参数 -> 用 None
def func(items=None):
    items = items or []

# 2. 迭代时修改列表 -> 迭代副本
for item in list(my_list):
    if condition(item):
        my_list.remove(item)

# 3. 裸 except 捕获 -> 用 Exception
try:
    risky_code()
except Exception as e:  # 不是 bare except:
    handle(e)

# 4. 上下文管理器 -> 总是用 with
with open('file.txt', encoding='utf-8') as f:
    data = f.read()

# 5. 浮点数 -> 用 Decimal 处理金额
from decimal import Decimal
price = Decimal('19.99')

# 6. 生成器只能迭代一次 -> 重建或用 itertools.tee
gen = (x for x in range(10))
list(gen)  # [0,1,...,9]
list(gen)  # [] - 已耗尽!
```

### 示例

```python
from typing import List, Dict, Optional, Union

def process_data(
    items: List[int],
    config: Dict[str, str],
    threshold: Optional[int] = None
) -> Dict[str, Union[int, float]]:
    """处理数据并返回统计结果"""
    result = {
        'count': len(items),
        'avg': sum(items) / len(items) if items else 0.0
    }
    return result
```

## 配置示例

### pyproject.toml 推荐配置

```toml
[tool.black]
line-length = 88
target-version = ['py38']

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q --cov=myproject"
testpaths = ["tests"]
```

### 陷阱速查表

| 陷阱 | 错误写法 | 正确写法 |
|------|----------|----------|
| 可变默认参数 | `def f(x=[])` | `def f(x=None): x = x or []` |
| is 比较值 | `if a is "hello"` | `if a == "hello"` |
| 迭代时修改 | `for x in lst: lst.remove(x)` | `for x in list(lst): ...` |
| 裸 except | `except:` | `except Exception:` |
| 文件不用 with | `f = open(...)` | `with open(...) as f:` |
| 浮点金额 | `price = 19.99` | `price = Decimal('19.99')` |
| 生成器复用 | `gen = (x for x in ...)` | 每次重建或用 `itertools.tee` |
| 类属性可变 | `class C: items = []` | 在 `__init__` 中定义 |
| 编码依赖平台 | `open('f')` | `open('f', encoding='utf-8')` |

## 优选实践

1. **始终指定编码**:文件操作显式传 `encoding='utf-8'`,不依赖平台默认值
2. **用 None 替代可变默认值**:任何可变对象(list/dict/set)作为默认参数时用 None
3. **优先用 `except Exception`**:不要用裸 `except:`,避免捕获 `SystemExit` 和 `KeyboardInterrupt`
4. **迭代副本**:需要修改集合时,迭代其副本 `for x in list(items):`
5. **金额用 Decimal**:涉及货币计算使用 `decimal.Decimal`,不用 float
6. **用 with 管理资源**:文件、数据库连接、锁都使用上下文管理器
7. **类型提示从简到详**:逐步添加类型提示,核心函数优先

## 常见问题

### Q: `UnboundLocalError` 是什么原因?

A: 在函数内部对外部变量赋值时,Python 会将该变量视为局部变量。如果赋值前尝试读取,会报 `UnboundLocalError`。解决方法:使用 `nonlocal`(嵌套函数)或 `global`(全局变量)声明。

### Q: 循环导入怎么解决?

A: 循环导入是两个模块互相 import 导致的。解决方案:1) 将导入移到函数内部(延迟导入);2) 重构代码,提取共享部分到第三个模块;3) 合并循环依赖的模块。

### Q: GIL 对我的程序有影响吗?

A: GIL(全局解释器锁)阻止 Python 线程真正并行执行。对 I/O 密集型任务影响不大(线程会在 I/O 等待时释放 GIL)。对 CPU 密集型任务,使用 `multiprocessing` 替代 `threading` 实现真正的并行。

### Q: `__init__` 和 `__new__` 的区别?

A: `__new__` 创建实例(负责对象分配),`__init__` 初始化实例(负责设置属性)。通常只重写 `__init__`。重写 `__new__` 的场景:单例模式、不可变类型(如 tuple 的子类)。

## 依赖说明

### 运行环境

- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3 | 运行时 | 必需 | 官方网站下载 |
| pytest | 测试框架 | 推荐 | pip install pytest |
| mypy | 类型检查 | 推荐 | pip install mypy |
| black | 代码格式化 | 推荐 | pip install black |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置

- 本 Skill 无需 API Key
- 纯知识型工具,不涉及外部 API 调用

### 可用性分类

- **分类**: MD(纯 Markdown 指令)
- **说明**: 通过自然语言指令驱动 Agent 提供 Python 开发优选实践建议
- **限制**: 免费版不包含性能优化深度指导与企业级代码规范定制

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
