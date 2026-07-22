---
slug: "java"
name: "java"
version: "1.1.0"
displayName: "Java健壮编程"
summary: "编写健壮Java代码,避免空指针陷阱、相等性Bug与并发问题"
license: "MIT"
description: |-
  编写健壮Java代码,避免空指针陷阱、相等性Bug与并发问题。核心能力涵盖空值与Optional处理、集合迭代陷阱、泛型与类型擦除、并发与同步、类继承与内存模型、Stream与CompletableFuture、测试(JUnit/Mockito)及JVM/GC/模块系统,提供关键规则与错误场景防护。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 研发工具
---
# Java健壮编程

编写健壮Java代码,避免空指针陷阱、相等性Bug与并发问题。涵盖从基础语法陷阱到高级并发模型的完整防护指南。

## 快速参考

| 主题 | 文件 |
| --- | --- |
| 空值、Optional、自动装箱 | `nulls.md` |
| 集合与迭代陷阱 | `collections.md` |
| 泛型与类型擦除 | `generics.md` |
| 并发与同步 | `concurrency.md` |
| 类、继承、内存 | `classes.md` |
| Stream与CompletableFuture | `streams.md` |
| 测试(JUnit、Mockito) | `testing.md` |
| JVM、GC、模块 | `jvm.md` |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
## 核心能力

- **空值与Optional处理**: 使用 `Optional.orElse()`、`orElseGet()`、`ifPresent()` 替代 `Optional.get()` 防止空值异常,避免自动拆箱NPE
- **相等性与hashCode一致性**: `==` 比较引用而非内容,字符串必须用 `.equals()`;重写 `equals()` 必须同时重写 `hashCode()`,否则 `HashMap`/`HashSet` 失效
- **集合与迭代陷阱**: 迭代时修改集合抛出 `ConcurrentModificationException`,使用 `Iterator.remove()` 安全删除;`Integer == Integer` 在 -128 到 127 范围外使用引用比较
- **泛型与类型擦除**: 泛型类型信息在运行时擦除,无法执行 `new T()` 或 `instanceof List<String>`,需通过类型令牌传递Class对象
- **并发与同步**: `volatile` 保证可见性但不保证原子性,`count++` 仍需同步;使用 `synchronized`、`ReentrantLock` 或 `AtomicInteger` 保证线程安全
- **Stream与CompletableFuture**: Stream是单次使用的,终端操作后不可复用;`thenApply` 处理同步转换,`thenCompose` 用于链式编排 `CompletableFuture`
- **类继承与内存模型**: 内部类持有外部类引用,不需要时使用静态嵌套类;Records隐式final不可继承,组件为final
- **资源管理与序列化**: 使用try-with-resources自动关闭实现 `AutoCloseable` 的资源;`serialVersionUID` 不匹配导致反序列化失败,必须显式声明
- **测试(JUnit/Mockito)**: 使用JUnit断言和Mockito模拟依赖,验证交互行为与状态
### 空值与Optional处理

执行空值与Optional处理操作,处理用户输入并返回结果。

**输入**: 用户提供空值与Optional处理所需的参数和指令。

**输出**: 返回空值与Optional处理的处理结果。

- 执行`空值与Optional处理`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`空值与Optional处理`相关配置参数进行设置
### 相等性与hashCode一致性

执行相等性与hashCode一致性操作,处理用户输入并返回结果。

**输入**: 用户提供相等性与hashCode一致性所需的参数和指令。

**输出**: 返回相等性与hashCode一致性的处理结果。

- 执行`相等性与hashCode一致性`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`相等性与hashCode一致性`相关配置参数进行设置
### 集合与迭代陷阱

执行集合与迭代陷阱操作,处理用户输入并返回结果。

**输入**: 用户提供集合与迭代陷阱所需的参数和指令。

**输出**: 返回集合与迭代陷阱的处理结果。

- 执行`集合与迭代陷阱`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`集合与迭代陷阱`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 编写健壮、Java、避免空指针陷阱、Bug、与并发问题、核心能力涵盖空值、集合迭代陷阱、JVM、模块系统、提供关键规则与错、误场景防护。这些能力在上述核心功能中均有对应处理逻辑。
## 关键规则

* `==` 比较引用,不是内容 — 字符串始终使用 `.equals()`
* 重写 `equals()` 必须同时重写 `hashCode()` — 否则 `HashMap`/`HashSet` 会失效
* `Optional.get()` 在空时抛出异常 — 使用 `orElse()`、`orElseGet()` 或 `ifPresent()`
* 迭代时修改集合抛出 `ConcurrentModificationException` — 使用 `Iterator.remove()`
* 类型擦除: 泛型类型信息运行时丢失 — 无法执行 `new T()` 或 `instanceof List<String>`
* `volatile` 保证可见性,不保证原子性 — `count++` 仍需同步
* 拆箱null抛出NPE — `Integer i = null; int x = i;` 会崩溃
* `Integer == Integer` 在 -128 到 127 范围外使用引用比较 — 使用 `.equals()`
* try-with-resources自动关闭 — 实现 `AutoCloseable`,Java 7+
* 内部类持有外部类引用 — 不需要时使用静态嵌套类
* Stream是单次使用的 — 终端操作后不可复用
* `thenApply` vs `thenCompose` — `thenCompose` 用于链式编排 `CompletableFuture`
* Records隐式final — 不可继承,组件为final
* `serialVersionUID` 不匹配会破坏反序列化 — 始终显式声明

## 使用流程

1. 识别代码中的空值风险点,使用 `Optional` 包装返回值,用 `orElse()` / `orElseGet()` 提供默认值
2. 检查所有相等性比较,字符串和对象使用 `.equals()` 而非 `==`,确认 `equals()` 和 `hashCode()` 成对重写
3. 审查集合迭代代码,将 `for-each` 中删除元素改为 `Iterator.remove()`,或使用 `removeIf()`
4. 分析并发访问场景,对共享可变状态使用 `synchronized`、`ReentrantLock` 或 `AtomicInteger`,`volatile` 仅用于可见性
5. 检查Stream使用,确保不在终端操作后复用Stream,`CompletableFuture` 链式调用使用 `thenCompose` 而非 `thenApply`
6. 验证资源管理,所有实现了 `AutoCloseable` 的资源使用try-with-resources,确认 `serialVersionUID` 已显式声明
7. 编写JUnit测试用例,使用Mockito模拟外部依赖,覆盖边界条件和异常场景

## 示例

### 示例1:Optional安全使用

```java
// 错误: Optional.get() 在空时抛出 NoSuchElementException
Optional<User> user = userRepository.findById(id);
String name = user.get().getName();  // 危险!

// 正确: 使用 orElse() 提供默认值
String name = user.map(User::getName).orElse("unknown");

// 正确: 使用 orElseGet() 延迟计算默认值
String name = user.map(User::getName).orElseGet(() -> generateDefaultName());

// 正确: 使用 ifPresent() 条件执行
user.ifPresent(u -> sendWelcomeEmail(u));
```

### 示例2:equals与hashCode一致性

```java
// 错误: 只重写 equals() 不重写 hashCode()
public class Person {
    private String name;
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Person)) return false;
        return Objects.equals(name, ((Person) o).name);
    }
    // 缺少 hashCode() — HashSet<Person> 会包含重复元素!
}

// 正确: equals() 和 hashCode() 成对重写
@Override
public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Person)) return false;
    return Objects.equals(name, ((Person) o).name);
}
@Override
public int hashCode() {
    return Objects.hash(name);
}
```

### 示例3:集合迭代安全删除

```java
// 错误: for-each 中删除元素抛出 ConcurrentModificationException
List<String> items = new ArrayList<>(Arrays.asList("a", "b", "c"));
for (String item : items) {
    if (item.equals("b")) {
        items.remove(item);  // 抛出异常!
    }
}

// 正确: 使用 Iterator.remove()
Iterator<String> it = items.iterator();
while (it.hasNext()) {
    if (it.next().equals("b")) {
        it.remove();  // 安全
    }
}

// 正确: 使用 removeIf() (Java 8+)
items.removeIf(item -> item.equals("b"));
```

### 示例4:CompletableFuture链式编排

```java
// 错误: thenApply 嵌套产生 CompletableFuture<CompletableFuture<String>>
CompletableFuture<CompletableFuture<String>> bad = 
    userService.findById(id)
        .thenApply(user -> orderService.getOrders(user));  // 嵌套!

// 正确: thenCompose 展平链式调用
CompletableFuture<String> good = 
    userService.findById(id)
        .thenCompose(user -> orderService.getOrders(user))  // 展平
        .thenApply(orders -> "Found " + orders.size() + " orders");
```

### 示例5:try-with-resources自动关闭

```java
// 错误: 手动关闭资源,异常时可能遗漏
FileReader reader = new FileReader("data.txt");
try {
    // 读取数据
} catch (IOException e) {
    e.printStackTrace();
} finally {
    reader.close();  // 若try块抛出异常,close()可能不执行
}

// 正确: try-with-resources 自动关闭 AutoCloseable
try (FileReader reader = new FileReader("data.txt");
     BufferedReader br = new BufferedReader(reader)) {
    String line = br.readLine();
    // 资源在try块结束后自动关闭,即使抛出异常
} catch (IOException e) {
    e.printStackTrace();
}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `NullPointerException` (拆箱null) | `Integer i = null; int x = i;` 自动拆箱触发NPE | 使用 `Optional<Integer>` 或显式null检查,避免将包装类型赋null后自动拆箱 |
| `ConcurrentModificationException` | `for-each` 循环中直接调用 `list.remove()` | 使用 `Iterator.remove()` 或 Java 8+ 的 `removeIf()` 方法安全删除 |
| `HashMap`/`HashSet`包含重复键 | 重写了 `equals()` 但未重写 `hashCode()` | `equals()` 和 `hashCode()` 必须成对重写,使用 `Objects.hash()` 生成hashCode |
| `NoSuchElementException` (Optional空) | 调用 `Optional.get()` 但Optional为空 | 使用 `orElse()`、`orElseGet()` 提供默认值,或 `ifPresent()` 条件执行 |
| `Integer == Integer`比较错误 | 两个超出 -128 到 127 缓存范围的 `Integer` 对象用 `==` 比较 | 包装类型始终使用 `.equals()` 比较,`==` 仅在Integer缓存范围内有效 |
| `ClassCastException` (类型擦除) | 运行时尝试 `instanceof List<String>` 或强制转换泛型类型 | 泛型类型运行时擦除,使用类型令牌(`Class<T>`)传递类型信息 |
| `IllegalStateException` (Stream复用) | 终端操作后再次操作同一个Stream | Stream是单次使用的,需要重新创建Stream或使用 `Supplier<Stream>` 供应器 |
| `serialVersionUID`反序列化失败 | 类修改后 `serialVersionUID` 变化导致反序列化不匹配 | 始终显式声明 `private static final long serialVersionUID = 1L;` |
| `OutOfMemoryError` (内部类泄漏) | 非静态内部类隐式持有外部类引用,阻止GC回收 | 不需要外部类引用时使用 `static` 嵌套类 |
| `InterruptedException`处理不当 | 捕获后吞掉异常,破坏线程中断状态 | 捕获 `InterruptedException` 后恢复中断状态: `Thread.currentThread().interrupt()` |

## 常见问题

### Q1: 为什么 `==` 比较字符串有时正确有时错误?
A: `==` 比较的是对象引用而非内容。Java对字符串字面量有驻留机制,相同字面量指向同一对象所以 `==` 可能成立。但通过 `new String()` 或运行时拼接的字符串是不同对象,`==` 会返回false。始终使用 `.equals()` 比较字符串内容,`==` 仅用于比较基本类型。

### Q2: `volatile` 能保证 `count++` 的线程安全吗?
A: 不能。`volatile` 仅保证变量的可见性(一个线程修改后其他线程立即可见),不保证操作的原子性。`count++` 实际上是"读取-修改-写入"三步操作,可能被中断。使用 `AtomicInteger.incrementAndGet()` 或 `synchronized` 块保证原子性。

### Q3: `thenApply` 和 `thenCompose` 有什么区别?
A: `thenApply` 接收同步函数,将 `CompletableFuture<T>` 转换为 `CompletableFuture<R>`,适用于同步转换。`thenCompose` 接收返回 `CompletableFuture` 的函数,将 `CompletableFuture<T>` 展平为 `CompletableFuture<R>`,适用于异步链式调用。类似 `Stream.map` 与 `flatMap` 的关系。

### Q4: 为什么重写 `equals()` 必须重写 `hashCode()`?
A: Java契约规定: 相等的对象必须有相同的hashCode。如果只重写 `equals()` 不重写 `hashCode()`,`HashMap` 和 `HashSet` 会使用默认的 `Object.hashCode()` (基于内存地址),导致两个 `equals()` 为true的对象hashCode不同,被放到不同的桶中,查找时找不到。使用 `Objects.hash(field1, field2)` 生成一致的hashCode。

### Q5: 类型擦除会带来什么实际影响?
A: 泛型类型在运行时被擦除为原始类型或上界。这意味着: 无法在运行时执行 `instanceof List<String>`(只能 `instanceof List`)、无法创建泛型数组 `new T[]`、无法直接实例化类型参数 `new T()`。需要传递 `Class<T>` 类型令牌,通过反射创建实例。这也是方法重载时 `List<String>` 和 `List<Integer>` 不能共存的原因。

### Q6: Stream为什么不能复用?
A: Stream设计为单次使用的管道,终端操作(forEach、collect、count等)会消费Stream并关闭管道。复用已消费的Stream会抛出 `IllegalStateException: stream has already been operated upon or closed`。如需多次遍历,从数据源重新创建Stream,或使用 `Supplier<Stream<T>>` 供应器每次获取新Stream。

### Q7: 什么时候应该用静态嵌套类而非内部类?
A: 非静态内部类隐式持有外部类实例的引用,这会导致: 外部类无法被GC回收(内存泄漏)、无法独立实例化内部类、序列化时需序列化整个外部类。当内部类不需要访问外部类实例成员时,声明为 `static` 嵌套类,消除隐式引用,降低耦合。

## 已知限制

- 泛型类型擦除是Java语言层面设计,无法在运行时获取泛型参数类型
- `volatile` 不保证复合操作原子性,需配合 `Atomic` 类或锁
- Integer缓存范围固定为 -128 到 127,无法扩展
- Stream单次使用限制要求重新创建或使用供应器模式
- 自动装箱/拆箱可能引入隐蔽的NPE,需在包装类型使用时显式null检查
