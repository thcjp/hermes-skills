---
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
summary: "工作区文件浏览读取,防路径逃逸"
---
# file-browser

## Quick Start

Resolve all paths relative to WORKSPACE=/home/alfred/.skill-platform/workspace. Sanitize inputs to prevent escapes or absolutes.

* To list directory: exec("scripts/list_files.sh", [rel_path]) → JSON {success: bool, data: array of names, error: string}
* To read file: exec("scripts/read_file.sh", [rel_path]) → JSON {success: bool, data: string (text content), error: string}
* Handle errors: For binary/large/non-text files, return error JSON.

## Step-by-Step Workflow

1. Parse user query for action (list/read) and relative path.
2. Call appropriate script with sanitized rel_path.
3. Parse JSON output; respond to user with results or error message.
4. If path invalid or outside workspace, reject immediately.

## Safety Guidelines

* Enforce read-only: No writes, deletes, or exec beyond scripts.
* Log accesses if verbose mode enabled.
* For large files (>10k chars), truncate or summarize.

## Edge Cases

* Empty path: Default to "." (workspace root).
* Binary file: Return error "Non-text file".
* See references/examples.md for more (if added).

## Bundled Resources

* scripts/list_files.sh: Bash wrapper for ls.
* scripts/read_file.sh: Bash wrapper for cat with limits.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Read-only file browsing and reading in the OpenClaw workspace (/home/alfred/
- openclaw/workspace)
- 触发关键词: read, reading, browsing, file, browser, file-browser

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```

sh", [rel_path]) → JSON {success: bool, data: array of names, error: string}
sh", [rel_path]) → JSON {success: bool, data: string (text content), error: string}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用file-browser？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: file-browser有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **路径长度**：输入的相对路径长度不应超过系统允许的最大路径长度限制，以避免路径处理错误。
- **特殊字符**：路径中不应包含可能导致命令注入或路径逃逸的特殊字符，如`<`, `>`, `|`, `&`, `;`等。
- **文件名大小写**：由于文件系统的大小写敏感性，确保文件名大小写与实际文件一致。

### 性能边界
- **文件大小**：对于大于10KB的文件，技能会返回错误信息，因为技能不支持读取大型文件。
- **并发请求**：技能可能不支持高并发请求，因为内部脚本执行可能存在瓶颈。

### 兼容性约束
- **操作系统**：技能在Windows、macOS和Linux操作系统上均应能正常工作，但可能存在细微的兼容性问题。
- **文件系统**：技能主要针对POSIX兼容的文件系统，如ext4、btrfs等，对于NTFS等非POSIX文件系统可能存在限制。

### 安全限制
- **只读访问**：技能仅支持读取文件，不支持写入、删除或执行文件，以防止潜在的安全风险。
- **脚本执行**：技能通过预定义的脚本执行文件操作，不接收用户自定义的脚本或命令，以避免安全漏洞。

### 资源限制
- **内存使用**：技能在处理大量文件或大型文件时，可能会占用较多内存资源，可能导致系统性能下降。
- **磁盘I/O**：频繁的文件读取操作可能会对磁盘I/O产生较大压力，影响系统整体性能。

