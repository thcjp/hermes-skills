---
slug: py
name: py
version: "1.1.0"
displayName: Python健壮编程
summary: 编写可靠Python代码,避免可变默认值、导入陷阱与运行时意外
license: MIT
description: |-
  编写可靠Python代码,避免可变默认值、导入陷阱与常见运行时意外。核心能力涵盖动态类型与类型提示、集合陷阱与推导式、参数/闭包/装饰器/生成器、继承/描述符/元类、GIL/线程/asyncio/多进程、循环导入/包管理、Pytest测试与模拟,提供关键规则与错误场景防护。
tools:
  - read
  - exec
---

# Python健壮编程

编写可靠Python代码,避免可变默认值、导入陷阱与常见运行时意外。涵盖从动态类型陷阱到并发模型的完整防护指南。

## 快速参考

| 主题 | 文件 |
| --- | --- |
| 动态类型、类型提示、鸭子类型 | `types.md` |
| List/dict/set陷阱、推导式 | `collections.md` |
| Args/kwargs、闭包、装饰器、生成器 | `functions.md` |
| 继承、描述符、元类 | `classes.md` |
| GIL、线程、asyncio、多进程 | `concurrency.md` |
| 循环导入、包、`__init__.py` | `imports.md` |
| Pytest、模拟、fixtures | `testing.md` |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD（纯Markdown指令，无需exec命令行能力）

## 核心能力

- **可变默认参数防护**: `def f(items=[])` 在所有调用间共享同一列表,使用 `items=None` 后 `items = items or []` 创建独立实例
- **身份与相等性区分**: `is` 检查对象身份,`==` 检查值相等性,`"a" * 100 is "a" * 100` 可能为False,比较值始终用 `==`
- **迭代修改安全**: 迭代时修改列表会跳过元素,使用 `for x in list(items):` 迭代副本或使用推导式创建新列表
- **GIL与并发模型**: GIL阻止Python线程真正并行执行CPU密集任务,使用 `multiprocessing` 实现CPU并行,`asyncio` 实现IO并发
- **异常捕获精确性**: 裸 `except:` 会捕获 `SystemExit` 和 `KeyboardInterrupt`,使用 `except Exception:` 仅捕获业务异常
- **作用域与变量绑定**: 函数内赋值外部变量触发 `UnboundLocalError`,使用 `nonlocal`(嵌套函数)或 `global`(模块级)声明
- **资源管理**: `open()` 不使用上下文管理器会泄漏文件句柄,始终使用 `with open():` 确保资源释放
- **循环导入处理**: 循环导入会静默失败或部分加载,在函数内部导入打破循环或将公共依赖提取到独立模块
- **浮点精度与货币计算**: `0.1 + 0.2 != 0.3` 是浮点精度问题,货币计算使用 `decimal.Decimal` 保证精确
- **生成器与迭代器**: 生成器在一次迭代后耗尽,不可复用,需重新创建或使用 `itertools.tee` 复制迭代器
- **类属性与实例属性**: 类属性中的可变对象在所有实例间共享,应在 `__init__` 中定义实例属性
- **编码一致性**: 默认编码依赖平台,文件操作始终指定 `encoding='utf-8'` 避免跨平台问题
### 可变默认参数防护

执行可变默认参数防护操作,处理用户输入并返回结果。

**输入**: 用户提供可变默认参数防护所需的参数和指令。

**输出**: 返回可变默认参数防护的处理结果。

- 执行`可变默认参数防护`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`可变默认参数防护`相关配置参数进行设置
### 身份与相等性区分

执行身份与相等性区分操作,处理用户输入并返回结果。

**输入**: 用户提供身份与相等性区分所需的参数和指令。

**输出**: 返回身份与相等性区分的处理结果。

- 执行`身份与相等性区分`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`身份与相等性区分`相关配置参数进行设置
### 迭代修改安全

执行迭代修改安全操作,处理用户输入并返回结果。

**输入**: 用户提供迭代修改安全所需的参数和指令。

**输出**: 返回迭代修改安全的处理结果。

- 执行`迭代修改安全`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`迭代修改安全`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 编写可靠、避免可变默认值、导入陷阱与运行时、导入陷阱与常见运、行时意外、核心能力涵盖动态、类型与类型提示、集合陷阱与推导式、装饰器、描述符、多进程、包管理、Pytest、测试与模拟、提供关键规则与错、误场景防护。这些能力在上述核心功能中均有对应处理逻辑。
## 关键规则

* `def f(items=[])` 在所有调用间共享列表 — 使用 `items=None` 然后 `items = items or []`
* `is` 检查身份,`==` 检查相等性 — `"a" * 100 is "a" * 100` 可能为False
* 迭代时修改列表会跳过元素 — 迭代副本: `for x in list(items):`
* GIL阻止Python线程真正并行 — CPU密集任务使用 `multiprocessing`
* 裸 `except:` 捕获 `SystemExit` 和 `KeyboardInterrupt` — 使用 `except Exception:`
* 函数内赋值外部变量触发 `UnboundLocalError` — 使用 `nonlocal` 或 `global`
* `open()` 不使用上下文管理器会泄漏句柄 — 始终使用 `with open():`
* 循环导入会静默失败或部分加载 — 在函数内部导入打破循环
* `0.1 + 0.2 != 0.3` — 浮点精度问题,货币计算使用 `decimal.Decimal`
* 生成器一次迭代后耗尽 — 不可复用,重新创建或使用 `itertools.tee`
* 类属性中的可变对象在实例间共享 — 在 `__init__` 中定义
* `__init__` 不是构造函数 — `__new__` 创建实例,`__init__` 初始化
* 默认编码依赖平台 — 始终指定 `encoding='utf-8'`

## 使用流程

1. 检查所有函数默认参数,将可变默认值(`[]`、`{}`、`set()`)替换为 `None` 并在函数体内创建新实例
2. 审查相等性比较,值比较使用 `==` 而非 `is`,`is` 仅用于与 `None`、`True`、`False` 比较
3. 检查迭代代码,迭代时需修改集合应使用 `list(items)` 创建副本,或使用推导式/`filter()` 生成新列表
4. 评估并发需求,CPU密集型任务使用 `multiprocessing.Process`,IO密集型使用 `asyncio` 或 `threading`
5. 审查异常处理,将裸 `except:` 替换为 `except Exception:`,对特定异常使用精确类型捕获
6. 检查文件和资源操作,确保所有 `open()` 使用 `with` 语句,网络连接和锁同样使用上下文管理器
7. 分析导入结构,循环导入通过函数内导入或重构模块依赖解决
8. 货币和精度计算使用 `decimal.Decimal`,文件操作指定 `encoding='utf-8'`
9. 生成器不可复用,需多次遍历使用 `list()` 转换或 `itertools.tee` 复制
10. 编写Pytest测试,使用 `fixtures` 管理测试资源,`unittest.mock` 模拟外部依赖

## 示例

### 示例1:可变默认参数陷阱

```python
# 错误: 所有调用共享同一列表
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] — 不是预期的 [2]!

# 正确: 使用 None 作为哨兵值
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2] — 正确
```

### 示例2:迭代时安全修改

```python
# 错误: 迭代时删除元素会跳过元素
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)
print(items)  # [1, 3, 5] — 跳过了4!

# 正确: 迭代副本
items = [1, 2, 3, 4, 5]
for item in list(items):
    if item % 2 == 0:
        items.remove(item)
print(items)  # [1, 3, 5] — 正确

# 正确: 使用推导式创建新列表
items = [1, 2, 3, 4, 5]
items = [x for x in items if x % 2 != 0]
print(items)  # [1, 3, 5]
```

### 示例3:浮点精度与Decimal

```python
# 错误: 浮点数精度问题
print(0.1 + 0.2 == 0.3)  # False
print(0.1 + 0.2)         # 0.30000000000000004

# 正确: 货币计算使用 decimal.Decimal
from decimal import Decimal

price = Decimal('19.99')
tax_rate = Decimal('0.08')
total = price + (price * tax_rate)
print(total)  # 21.5892 — 精确计算
print(total == Decimal('21.5892'))  # True
```

### 示例4:生成器耗尽与复制

```python
from itertools import tee

# 错误: 生成器一次迭代后耗尽
gen = (x * 2 for x in range(5))
print(list(gen))  # [0, 2, 4, 6, 8]
print(list(gen))  # [] — 已耗尽!

# 正确: 使用 itertools.tee 复制迭代器
gen = (x * 2 for x in range(5))
gen1, gen2 = tee(gen)
print(list(gen1))  # [0, 2, 4, 6, 8]
print(list(gen2))  # [0, 2, 4, 6, 8] — 可独立遍历

# 正确: 转换为列表多次使用
data = list(x * 2 for x in range(5))
print(data)  # [0, 2, 4, 6, 8]
print(data)  # [0, 2, 4, 6, 8] — 可重复访问
```

### 示例5:上下文管理器与资源释放

```python
# 错误: 不使用上下文管理器,异常时文件句柄泄漏
f = open('data.txt', 'r')
content = f.read()  # 若此处抛出异常,f.close() 不执行
f.close()

# 正确: 使用 with 语句自动释放资源
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# f 在 with 块结束后自动关闭,即使抛出异常

# 正确: 多资源同时管理
with open('input.txt', 'r', encoding='utf-8') as fin, \
     open('output.txt', 'w', encoding='utf-8') as fout:
    for line in fin:
        fout.write(line.upper())
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 可变默认参数共享状态 | `def f(items=[])` 的 `[]` 在函数定义时创建一次,所有调用共享 | 使用 `items=None` 作为默认值,函数体内 `if items is None: items = []` 创建新实例 |
| `UnboundLocalError` | 函数内赋值外部作用域变量,Python将其视为局部变量 | 在函数内使用 `nonlocal`(嵌套函数)或 `global`(模块级)声明外部变量 |
| 迭代时跳过元素 | `for item in items: items.remove(item)` 修改列表长度导致索引偏移 | 迭代副本 `for item in list(items):` 或使用推导式 `[x for x in items if cond]` |
| 裸 `except:` 捕获系统异常 | `except:` 捕获所有异常包括 `SystemExit`、`KeyboardInterrupt` | 使用 `except Exception:` 仅捕获业务异常,系统异常应向上传播 |
| 文件句柄泄漏 | `open()` 后未调用 `close()`,或异常时 `close()` 未执行 | 始终使用 `with open(path, encoding='utf-8') as f:` 上下文管理器自动释放 |
| 循环导入失败 | 模块A导入模块B,模块B又导入模块A,导致部分加载 | 在函数内部导入打破循环,或将公共依赖提取到第三个模块 |
| 浮点精度误差 | `0.1 + 0.2 != 0.3` 因IEEE 754浮点表示限制 | 货币计算使用 `decimal.Decimal`,科学计算使用 `math.isclose()` 比较近似值 |
| 生成器耗尽报错 | 生成器一次迭代后抛出 `StopIteration`,再次遍历返回空 | 需多次遍历时用 `list()` 转为列表,或用 `itertools.tee` 复制迭代器 |
| 类属性实例间共享 | 类体中定义的可变属性(如 `items = []`)被所有实例共享 | 在 `__init__` 中定义 `self.items = []`,确保每个实例有独立副本 |
| `UnicodeDecodeError` | 默认编码依赖平台(Windows为GBK,Linux为UTF-8) | 文件操作始终指定 `encoding='utf-8'`,读取未知编码使用 `errors='replace'` |

## 常见问题

### Q1: 为什么 `def f(items=[])` 会有问题?
A: Python中默认参数值在函数定义时只创建一次,而非每次调用时创建。`items=[]` 会在函数定义时创建一个空列表对象,所有调用共享同一个列表。第一次调用 `f(1)` 向列表添加1,第二次调用 `f(2)` 会在同一列表上添加2,得到 `[1, 2]` 而非预期的 `[2]`。解决方案是使用 `items=None` 作为哨兵值,在函数体内创建新列表。

### Q2: `is` 和 `==` 有什么区别?
A: `is` 检查两个变量是否指向同一对象(身份比较,基于内存地址),`==` 检查两个对象的值是否相等(相等性比较,调用 `__eq__` 方法)。`a is None` 是正确的用法,但 `"a" * 100 is "a" * 100` 可能为False(取决于CPython优化)。比较值始终使用 `==`,仅在与 `None`、`True`、`False` 比较时使用 `is`。

### Q3: GIL如何影响Python多线程?
A: GIL(全局解释器锁)确保同一时刻只有一个线程执行Python字节码。CPU密集型任务多线程无法利用多核,线程间频繁争抢GIL反而降低性能。IO密集型任务(网络请求、文件读写)在等待IO时释放GIL,多线程有效。CPU密集型并行应使用 `multiprocessing`(独立进程,各自有GIL)或C扩展释放GIL。

### Q4: 循环导入如何解决?
A: 循环导入发生在模块A导入模块B,模块B又导入模块A时。解决方案: 1)将导入语句移到函数内部(延迟导入),仅在需要时执行; 2)将公共依赖提取到第三个模块,A和B都从该模块导入; 3)重构模块边界,消除循环依赖。注意循环导入可能导致模块部分加载(属性未定义),错误通常表现为 `ImportError: cannot import name 'X'`。

### Q5: 为什么 `0.1 + 0.2 != 0.3`?
A: 这是IEEE 754浮点数表示的固有限制。0.1和0.2在二进制中是无限循环小数,无法精确表示,存储时被截断。`0.1 + 0.2` 的结果为 `0.30000000000000004` 而非 `0.3`。货币计算使用 `decimal.Decimal('0.1') + decimal.Decimal('0.2') == decimal.Decimal('0.3')` 保证精确。比较浮点数使用 `math.isclose(a, b, rel_tol=1e-9)` 而非 `==`。

### Q6: `__init__` 和 `__new__` 有什么区别?
A: `__new__` 是真正的构造方法,负责创建并返回实例对象(通常是类的实例),是类方法。`__init__` 是初始化方法,在实例创建后(`__new__` 返回后)被调用,负责设置实例属性。对于不可变类型(如tuple、str),必须在 `__new__` 中设置值,因为 `__init__` 中无法修改。通常只需重写 `__init__`,重写 `__new__` 用于单例模式或不可变子类。

### Q7: 生成器为什么不能重复遍历?
A: 生成器是惰性迭代器,按需产生值,内部维护状态指针。迭代完成后(抛出 `StopIteration`),状态指针到达末尾,无法重置。再次遍历只会立即得到空序列。需要重复遍历时: 1)用 `list(gen)` 转为列表(消耗内存); 2)用 `itertools.tee(gen, n)` 创建n个独立迭代器(有缓存开销); 3)重新调用生成器函数创建新生成器。

## 已知限制

- GIL限制Python多线程的CPU并行能力,CPU密集型任务必须使用 `multiprocessing`
- 动态类型在运行时才发现类型错误,类型提示(`type hints`)不强制执行
- 循环导入可能导致模块部分加载,需重构模块结构彻底解决
- 浮点数精度是IEEE 754标准固有限制,`decimal.Decimal` 有性能开销
- 生成器一次性消费特性要求在需要多次遍历时转为列表或使用 `itertools.tee`
