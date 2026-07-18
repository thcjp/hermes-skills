---
slug: vscode-node-tool-free
name: vscode-node-tool-free
version: "1.0.0"
displayName: VSCode节点工具(免费版)
summary: 面向个人开发者的VSCode/Cursor远程操作工具,覆盖文件读写、语言特性、Git基础操作。
license: MIT
edition: free
description: |-
  VSCode节点工具免费版为个人开发者提供通过节点协议远程操作VSCode/Cursor IDE的能力,涵盖文件读写、语言特性查询、编辑器状态与Git基础操作。

  核心能力:
  - 文件读写与目录列举
  - 语言特性查询(定义/引用/悬停/重命名)
  - 编辑器状态(活动文件/打开文件/选区)
  - 诊断信息获取
  - Git基础操作(status/diff/log/blame)

  适用场景:
  - 个人远程操作IDE完成日常开发
  - 通过Agent自动化简单文件操作
  - 快速查询代码引用与定义

  差异化:免费版聚焦个人开发者的基础IDE操作需求。Pro版扩展调试、测试、终端、Agent委托与团队协作能力。

  触发关键词: vscode, cursor, ide, 远程操作, 文件读写, 语言特性, git, 节点协议
tags:
- VSCode
- Cursor
- IDE集成
- 个人开发
- 远程操作
tools:
- read
- exec
---

# VSCode 节点工具(免费版)

## 概述

`vscode-node-tool-free` 为个人开发者提供通过节点协议远程操作 VSCode 或 Cursor IDE 的能力。它覆盖文件读写、语言特性查询、编辑器状态与 Git 基础操作,帮助你通过 Agent 自动化日常 IDE 任务。

本工具通过 `nodes invoke` 命令调用已连接的 IDE 节点,需要预先安装对应 IDE 扩展并完成连接。

## 核心能力

| 能力 | 说明 |
| --- | --- |
| 文件操作 | 读取、写入、编辑、删除文件 |
| 目录列举 | 列出工作区目录内容 |
| 语言特性 | 定义跳转、引用查找、悬停信息、符号、重命名、代码操作、格式化 |
| 编辑器状态 | 活动文件、打开文件列表、选区信息 |
| 诊断信息 | 获取错误与警告列表 |
| Git 基础 | status、diff、log、blame |

## 使用场景

### 场景 1:读取项目文件

```bash
nodes invoke --node "my-vscode" \
  --invokeCommand "vscode.file.read" \
  --invokeParamsJson '{"path":"src/main.ts"}'
```

返回:`{ content, totalLines, language }`

### 场景 2:查找所有引用

```bash
nodes invoke --node "my-vscode" \
  --invokeCommand "vscode.lang.references" \
  --invokeParamsJson '{"path":"src/main.ts","line":10,"character":5}'
```

返回:`{ locations: [{ path, line, character }] }`

### 场景 3:Git 状态查询

```bash
nodes invoke --node "my-vscode" \
  --invokeCommand "vscode.git.status"
```

返回:`{ branch, staged, modified, untracked, ahead, behind }`

## 快速开始

### 第一步:安装扩展

在 VSCode 或 Cursor 的扩展市场搜索并安装"节点协议"扩展,启动后状态栏显示连接状态。

### 第二步:验证节点连接

```bash
nodes status
```

确认节点已连接且可见。

### 第三步:执行命令

使用 `nodes invoke` 模式调用具体命令:

```bash
nodes invoke --node "<节点名>" \
  --invokeCommand "<命令>" \
  --invokeParamsJson '<参数JSON>'
```

## 配置示例

### 超时配置参考

| 操作类型 | invokeTimeoutMs | timeoutMs |
| --- | --- | --- |
| 文件/编辑器/语言 | 15000 | 20000 |
| Git | 30000 | 35000 |
| 测试 | 60000 | 65000 |

### 命令分类速查

| 分类 | 前缀 | 关键命令 |
| --- | --- | --- |
| 文件 | `vscode.file.*` | read, write, edit, delete |
| 目录 | `vscode.dir.*` | list |
| 语言 | `vscode.lang.*` | definition, references, hover, symbols, rename |
| 编辑器 | `vscode.editor.*` | active, openFiles, selections |
| 诊断 | `vscode.diagnostics.*` | get |
| Git | `vscode.git.*` | status, diff, log, blame |

## 最佳实践

1. **使用相对路径**:所有路径相对于工作区根目录,绝对路径与 `../` 会被阻止,保证安全。
2. **设置合理超时**:文件操作 15s,Git 操作 30s,避免长时间阻塞。
3. **先验证再操作**:对未知文件先 `read` 确认存在,再决定是否 `edit` 或 `delete`。
4. **利用语言特性**:用 `references` 与 `definition` 替代手动 `grep`,结果更精确。
5. **Git 操作前先 status**:提交前先查看 `git.status`,避免误提交。
6. **只读优先**:对生产代码优先使用只读命令(`read`、`references`、`log`),写操作需明确意图。

## 常见问题

### Q1: 节点连接不上怎么办?

检查:1) 扩展是否已安装并启用;2) 状态栏是否显示已连接;3) 节点是否出现在 `nodes status` 列表中;4) 网络与防火墙是否阻止节点通信。

### Q2: 命令报"not allowed"是什么原因?

该命令未加入网关白名单。需要在网关配置的 `allowCommands` 中添加该命令,或联系管理员授权。

### Q3: 超时怎么处理?

增加 `invokeTimeoutMs` 与 `timeoutMs` 两个参数(后者必须大于前者)。文件操作建议 15s/20s,Git 建议 30s/35s。

### Q4: 路径被阻止怎么办?

工具仅允许工作区相对路径,绝对路径与 `../` 会被阻止。请改用相对路径,如 `src/main.ts`。

### Q5: 免费版与 Pro 版的区别?

免费版提供文件、语言、编辑器、Git 基础操作;Pro 版扩展调试、测试、终端、Agent 委托与团队协作能力。

### Q6: 多个节点如何区分?

每个节点在网关注册时有唯一名称,通过 `nodes status` 查看所有已连接节点。调用时用 `--node "<节点名>"` 指定目标节点。

### Q7: 离线环境能用吗?

节点协议需要 IDE 与网关之间持续通信,完全离线时无法使用。但 IDE 本地功能(编辑、保存)不受影响,仅远程命令调用不可用。

### Q8: 如何排查命令执行失败?

按以下顺序排查:1) 检查 `nodes status` 确认节点在线;2) 确认命令在白名单内;3) 检查参数 JSON 是否合法;4) 查看网关日志获取详细错误;5) 增加超时参数重试。

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **IDE**:VSCode 或 Cursor(需安装节点协议扩展)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| VSCode / Cursor | IDE | 必需 | 官方安装 |
| 节点协议扩展 | IDE 扩展 | 必需 | IDE 扩展市场搜索安装 |
| 网关服务 | 服务 | 必需 | 团队或个人部署 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 基于节点协议,无需额外 API Key
- 节点连接通过设备唯一身份(Ed25519)认证,由网关批准
- 如网关启用 OAuth,需配置对应平台的访问令牌

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言指令驱动 Agent 调用 `nodes invoke` 命令;需要预先安装 IDE 扩展并连接网关
