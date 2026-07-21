---
slug: rust
name: rust
version: "1.0.1"
displayName: Rust避坑指南
summary: 规避所有权、借用、生命周期、字符串、错误处理、并发与内存的常见陷阱。
license: MIT
description: |-
  编写地道Rust代码,规避所有权移动、借用检查器、生命周期推断、
  UTF-8字符串、错误处理、惰性迭代器、线程安全与智能指针的高频
  陷阱。覆盖常见编译错误与Cargo包管理陷阱。适用于独立开发者、
  企业团队和自动化工作流场景。
tools:
  - read
  - exec
---

# Rust避坑指南

编写地道Rust代码,规避所有权、借用、生命周期、字符串、错误处理、迭代器、并发与内存的高频陷阱,以及常见编译错误与Cargo陷阱。

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

### 1. 所有权与借用
- 变量移动后使用:显式 `clone()` 或用 `&` 借用
- `for item in vec` 移动vec:改用 `&vec` 或 `.iter()` 借用
- `String` 移入函数:只读访问传 `&str`
- 所有权是Rust编译错误的第一大来源

**输入**: 用户提供所有权与借用所需的指令和必要参数。
**处理**: 按照skill规范执行所有权与借用操作,遵循单一意图原则。
**输出**: 返回所有权与借用的执行结果,包含操作状态和输出数据。

### 2. 借用检查器
- 不能同时持有 `&mut` 和 `&`:重构结构或用内部可变性
- 返回局部引用失败:返回所有权值而非引用
- `&mut self` 的可变借用阻塞所有访问:拆分结构体或用 `RefCell`

**输入**: 用户提供借用检查器所需的指令和必要参数。
**处理**: 按照skill规范执行借用检查器操作,遵循单一意图原则。

### 3. 生命周期
- `'static` 表示"可以"永久存活,非"已经":`String` 是 'static capable
- 含引用的结构体需要 `<'a>`:`struct Foo<'a> { bar: &'a str }`
- 返回引用的函数必须绑定输入:`fn get<'a>(s: &'a str) -> &'a str`

**处理**: 按照skill规范执行生命周期操作,遵循单一意图原则。
### 4. 字符串UTF-8陷阱
- `s[0]` 不编译:用 `.chars().nth(0)` 或 `.bytes()`
- `.len()` 返回字节数非字符数:用 `.chars().count()` 获取字符数
- `s1 + &s2` 移动s1:用 `format!("{}{}", s1, s2)` 保留两者

**输入**: 用户提供字符串UTF-8陷阱所需的指令和必要参数。
**处理**: 按照skill规范执行字符串UTF-8陷阱操作,遵循单一意图原则。

### 5. 错误处理
- `unwrap()` 在生产环境panic:用 `?` 或 `match`
- `?` 需要 `Result`/`Option` 返回类型:main 需要 `-> Result<(), Box<dyn Error>>`
- `expect("context")` 优于 `unwrap()`:显示panic原因

**输入**: 用户提供错误处理所需的指令和必要参数。
**处理**: 按照skill规范执行错误处理操作,遵循单一意图原则。

### 6. 迭代器惰性求值
- `.iter()` 借用,`.into_iter()` 移动:谨慎选择
- `.collect()` 需要类型标注:`collect::<Vec<_>>()` 或显式类型绑定
- 迭代器是惰性的:不消费不执行

**输入**: 用户提供迭代器惰性求值所需的指令和必要参数。
**输出**: 返回迭代器惰性求值的执行结果,包含操作状态和输出数据。

### 7. 并发线程安全
- `Rc` 不是 `Send`:跨线程用 `Arc`
- `Mutex` lock返回guard:drop时自动解锁,不要跨await持有
- `RwLock` 死锁:读锁升级写锁会永久阻塞

**输入**: 用户提供并发线程安全所需的指令和必要参数。
**处理**: 按照skill规范执行并发线程安全操作,遵循单一意图原则。

### 8. 智能指针与内存
- `RefCell` 运行时panic:违反借用规则时
- `Box` 用于递归类型:编译器需要已知大小
- 避免 `Rc<RefCell<T>>` 意大利面:重新思考所有权

**输入**: 用户提供智能指针与内存所需的指令和必要参数。
**输出**: 返回智能指针与内存的执行结果,包含操作状态和输出数据。

### 9. 常见编译错误处理
| 错误 | 原因 | 修复 |
|------|------|------|
| `value moved here` | 移动后使用 | `clone()` 或 `&` 借用 |
| `cannot borrow as mutable` | 已被借用 | 重构结构或 `RefCell` |
| `missing lifetime specifier` | 引用歧义 | 添加 `<'a>` |
| `the trait bound X is not satisfied` | 缺少impl | 检查trait bound |
| `type annotations needed` | 无法推断 | turbofish或显式类型 |
| `cannot move out of borrowed content` | 解引用移动 | `clone()` 或模式匹配 |

**输出**: 返回常见编译错误处理的执行结果,包含操作状态和输出数据。
### 10. Cargo包管理陷阱
- `cargo update` 更新 Cargo.lock 而非 Cargo.toml:版本号需手动提升
- features是加性的:无法禁用依赖已启用的feature
- `[dev-dependencies]` 不进release二进制:但在测试与示例中可用
- `cargo build --release` 显著更快:debug构建故意放慢以利调试

**输入**: 用户提供Cargo包管理陷阱所需的指令和必要参数。
**处理**: 按照skill规范执行Cargo包管理陷阱操作,遵循单一意图原则。
**输出**: 返回Cargo包管理陷阱的执行结果,包含操作状态和输出数据。

### 输出格式

执行结果以Markdown格式返回,包含操作状态(成功/失败)、处理摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。

- 执行`输出格式`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`输出格式`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 规避所有权、并发与内存的常见、编写地道、规避所有权移动、生命周期推断、惰性迭代器、线程安全与智能指、针的高频、覆盖常见编译错误、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 所有权错误诊断 | 编译错误信息 | 移动/借用修复方案 |
| 生命周期标注 | 含引用的结构体/函数 | `<'a>` 标注与绑定规则 |
| 错误处理改造 | `unwrap()` 生产代码 | `?` + `Result` 返回类型 |
| 并发安全审查 | 多线程代码 | `Rc`→`Arc`、`RefCell`→`Mutex` 修复 |
| Cargo配置 | 依赖与features | 版本锁定与feature隔离方案 |

不适用于:Rust生态框架选型、嵌入式Rust特殊约束、FFI深度绑定、过程宏开发。

## 使用流程

1. 识别错误类别:所有权、借用、生命周期、字符串、错误处理、迭代器、并发、内存
2. 查阅对应参考:`ownership-borrowing.md`、`types-strings.md`、`errors-iteration.md`、`concurrency-memory.md`、`advanced-traps.md`
3. 按编译错误表匹配修复方案
4. 优先借用而非clone,优先 `?` 而非 `unwrap()`
5. 并发场景验证 `Send`/`Sync` trait bound

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 示例

### 示例1:所有权修复
```rust
// 问题:变量移动后使用
let s1 = String::from("hello");
let s2 = s1;          // s1 移动到 s2
println!("{}", s1);   // 编译错误: value moved here

// 修复1:clone
let s1 = String::from("hello");
let s2 = s1.clone();
println!("{}", s1);   // OK

// 修复2:借用
let s1 = String::from("hello");
let s2 = &s1;         // 借用
println!("{} {}", s1, s2);  // OK
```

### 示例2:生命周期标注
```rust
// 问题:含引用的结构体缺少生命周期
struct Config {
    name: &str,  // 编译错误: missing lifetime specifier
}

// 修复:添加 <'a>
struct Config<'a> {
    name: &'a str,
}

// 函数返回引用必须绑定输入
fn first_word<'a>(s: &'a str) -> &'a str {
    &s[..s.find(' ').unwrap_or(s.len())]
}
```

### 示例3:错误处理改造
```rust
// 问题:unwrap 在生产环境 panic
fn read_config(path: &str) -> Config {
    let content = std::fs::read_to_string(path).unwrap();  // 危险
    parse_config(&content).unwrap()  // 危险
}

// 修复:用 ? 传播错误
fn read_config(path: &str) -> Result<Config, Box<dyn std::error::Error>> {
    let content = std::fs::read_to_string(path)?;
    let config = parse_config(&content)?;
    Ok(config)
}
```

### 示例4:并发安全
```rust
// 问题:Rc 不是 Send,无法跨线程
use std::rc::Rc;
use std::thread;
let data = Rc::new(vec![1, 2, 3]);
thread::spawn(move || {  // 编译错误: Rc 不满足 Send
    println!("{:?}", data);
});

// 修复:用 Arc
use std::sync::Arc;
let data = Arc::new(vec![1, 2, 3]);
let data_clone = Arc::clone(&data);
thread::spawn(move || {
    println!("{:?}", data_clone);  // OK
});
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `value moved here` 编译错误 | 变量移动后仍使用 | 显式 `clone()` 或改用 `&` 借用 |
| `cannot borrow as mutable` 编译错误 | 已有不可变借用时取可变借用 | 重构借用顺序,或用 `RefCell` 内部可变性 |
| `missing lifetime specifier` 编译错误 | 编译器无法推断引用生命周期 | 为结构体与函数添加 `<'a>` 标注并绑定输入输出 |
| `the trait bound Send is not satisfied` | `Rc`/`RefCell` 跨线程使用 | 改用 `Arc`/`Mutex` 满足 `Send`/`Sync` |
| `RefCell` 运行时panic | 运行时违反借用规则(多次可变借用) | 改用 `Mutex` 或重构所有权避免 `Rc<RefCell<T>>` |
| `RwLock` 死锁 | 读锁升级写锁永久阻塞 | 避免在读锁中请求写锁;用 `parking_lot::RwLock` 的升级API |
| `cargo update` 未更新Cargo.toml | 只更新了lock文件 | 手动编辑 Cargo.toml 提升版本号,再 `cargo update` |

## 常见问题

### Q1: `String` 与 `&str` 如何选择?
A: 函数参数优先 `&str`(只读、可接受 `String` 与 `&str`);结构体字段与返回值用 `String`(拥有所有权);需要零拷贝高性能场景用 `Cow<'a, str>`。`String` 移入函数会转移所有权,只读访问传 `&str` 更高效。

### Q2: `?` 操作符的返回类型要求?
A: `?` 用于 `Result`/`Option`,要求函数返回类型也是 `Result`/`Option`。`main` 函数用 `?` 需声明 `fn main() -> Result<(), Box<dyn std::error::Error>>`。`?` 会自动转换错误类型(若实现了 `From`)。

### Q3: `.iter()` 与 `.into_iter()` 有何区别?
A: `.iter()` 借用集合元素( `&T`),原集合保留;`.into_iter()` 移动元素( `T`),原集合被消费。只读遍历用 `.iter()`,需要所有权转移用 `.into_iter()`。`.iter_mut()` 提供可变借用 `&mut T`。

### Q4: `Rc` 为何不是 `Send`?
A: `Rc`(引用计数)不是原子操作,跨线程共享会导致计数竞争。用 `Arc`(原子引用计数)替代,`Arc` 满足 `Send`/`Sync`。`Arc<Mutex<T>>` 用于跨线程可变共享,`Arc<RwLock<T>>` 用于读多写少场景。

### Q5: `RefCell` 为何会运行时panic?
A: `RefCell` 将借用检查从编译期推迟到运行期。若运行时违反借用规则(如已有可变借用时再取借用),`borrow_mut()` 会panic。编译期无法确定的借用规则用 `RefCell`,但需确保运行时不会违反,否则改用 `Mutex`。

### Q6: `cargo build --release` 为何显著快于debug?
A: debug构建关闭优化并包含调试符号,便于调试但运行慢;release构建启用 `opt-level=3` 优化,运行快但编译慢且调试符号少。生产部署必须用 `--release`,开发调试用默认debug构建。

## 已知限制

- 需要LLM支持生成代码修复方案
- 编译错误修复依赖完整错误信息,模糊描述可能误判
- 并发安全审查需理解完整调用图,局部代码可能遗漏
- 不覆盖过程宏开发、嵌入式Rust特殊约束、FFI深度绑定
