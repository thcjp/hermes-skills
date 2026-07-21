---
slug: json-repair-kit
name: json-repair-kit
version: "1.0.0"
displayName: JSON修复工具
summary: 通过Node.js解析修复格式错误的JSON文件，支持尾逗号、单引号等修复。
license: MIT
description: |-
  JSON修复工具通过Node.js解析将格式错误的"宽松"JSON文件（如含尾逗号、单引号、未加引号键）
  解析为JavaScript对象并重新序列化为有效JSON。支持Trailing Commas、Single Quotes、
  Unquoted Keys、Comments、Hex/Octal Numbers五种修复模式，内置备份与验证安全机制。
tags:
  - Integrations
  - JSON
  - 修复
tools:
  - read
  - exec
---

# JSON Repair Kit — JSON修复工具

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 需要Node.js运行环境执行修复脚本

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | nodejs.org 下载安装 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，

## 核心能力

### Trailing Commas 修复
修复JSON中多余的尾逗号。将 `{"a": 1,}` 规范化为 `{"a": 1}`，消除解析器拒绝的尾逗号问题。解析为JavaScript对象后重新序列化，自动去除逗号。

**输入**: 用户提供Trailing Commas 修复所需的指令和必要参数。
**输出**: 返回Trailing Commas 修复的执行结果,包含操作状态和输出数据。### Single Quotes 修复
修复JSON中使用单引号而非双引号的问题。将 `{'a': 'b'}` 转换为 `{"a": "b"}`，确保字符串使用标准双引号。通过Node.js的JavaScript对象解析能力自动转换引号风格。

**输入**: 用户提供Single Quotes 修复所需的指令和必要参数。
**输出**: 返回Single Quotes 修复的执行结果,包含操作状态和输出数据。### Unquoted Keys 修复
修复JSON中键名未加引号的问题。将 `{key: "value"}` 转换为 `{"key": "value"}`，确保所有键名使用双引号包裹。JavaScript对象语法允许未加引号的键，修复后重新序列化为标准JSON。

**输入**: 用户提供Unquoted Keys 修复所需的指令和必要参数。
**输出**: 返回Unquoted Keys 修复的执行结果,包含操作状态和输出数据。### Comments 移除

移除JS风格注释。处理 `//` 行注释（标准Node解析器在字符串外时会剥离行注释），确保输出为纯净JSON。注释在JavaScript对象解析阶段被自动移除。

### Hex/Octal Numbers 修复

修复JSON中的十六进制和八进制数字。将 `0xFF` 转换为 `255`，确保所有数字使用标准十进制格式。JavaScript支持十六进制字面量，解析后转换为十进制数字输出。
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。


## 使用方式

```bash
# 修复单个文件
node skills/json-repair-kit/index.js --file path/to/broken.json

# 修复并输出到新文件
node skills/json-repair-kit/index.js --file broken.json --out fixed.json

# 递归修复整个目录
node skills/json-repair-kit/index.js --dir config/ --recursive
```

## 安全机制

- **备份（Backup）**：覆盖前始终创建 `.bak` 文件（除非使用 `--no-backup`，默认安全）
- **验证（Validation）**：写入前验证修复后的内容是有效JSON
- **Eval沙箱**：使用 `vm.runInNewContext` 解析，确保无法访问全局作用域或process，比直接 `eval` 更安全

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 文件不存在 | `--file` 路径错误 | 检查文件路径是否正确 |
| JSON解析失败 | 语法错误超出修复能力 | 检查是否有超出5种修复模式的语法问题 |
| Node.js未安装 | 运行时依赖缺失 | 安装Node.js后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 |
| 写入权限不足 | 目标目录不可写 | 检查目录权限，或使用 `--out` 指定可写路径 |
| `.bak` 文件已存在 | 之前修复的备份残留 | 手动删除旧 `.bak` 文件或确认覆盖 |
| 递归目录为空 | `--dir` 路径无JSON文件 | 检查目录路径和 `--recursive` 参数 |
| 修复后验证失败 | 修复结果仍非有效JSON | 检查原始文件是否有嵌套语法错误 |
| `vm.runInNewContext` 异常 | 恶意代码注入尝试 | 沙箱已隔离，检查输入文件来源是否可信 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪。

### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界。

## 已知限制

- 仅支持5种修复模式：Trailing Commas、Single Quotes、Unquoted Keys、Comments、Hex/Octal Numbers
- 不支持加密文件破解
- 需要 Node.js 运行环境
- `vm.runInNewContext` 虽然安全，但不应处理不受信任的恶意文件
- 复杂嵌套语法错误可能无法自动修复
