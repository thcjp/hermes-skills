---
slug: port-transfer-tool-free
name: port-transfer-tool-free
version: "1.0.0"
displayName: 工具移植工具
summary: 面向个人的 MCP工具配置跨环境移植工具，支持导入导出。
license: Proprietary
edition: free
description: |-
  面向个人用户的 MCP工具配置跨环境移植工具。

  核心能力:
  - MCP工具配置导出为可移植清单
  - 跨 Agent 环境导入配置
  - 凭证安全处理与占位符替换
  - 单环境配置校验

  适用场景:
  - 个人把 MCP工具配置从一个环境迁到另一个
  - 备份当前 MCP工具清单
  - 单环境配置导入与校验

  差异化: 免费版聚焦个人单环境移植与备份，提供凭证占位符处理，零成本迁移。

  触发关键词: 工具移植, 配置迁移, mcp 导入导出, 跨环境, 凭证占位, port transfer, import export
tags:
- 工具移植
- MCP工具
- 个人效率
- 其他工具
tools:
  - - read
- exec
---

# 工具移植工具（免费版）

## 概述

本工具帮助个人用户把 MCP工具配置在不同 AI Agent 环境间移植。免费版覆盖配置导出为可移植清单、跨环境导入、凭证安全占位符处理与单环境校验。适合个人单环境迁移与备份。

## 核心能力

| 能力 | 说明 | 免费版范围 |
|:-----|:-----|:-----------|
| 配置导出 | 导出为可移植 JSON 清单 | 单环境 |
| 配置导入 | 跨环境导入并安装 | 单环境 |
| 凭证处理 | 敏感值占位符化 | 全覆盖 |
| 配置校验 | 格式与依赖校验 | 单环境 |

## 使用场景

### 场景一：导出可移植清单

```bash
# 导出当前环境 MCP工具配置
{baseDir}/scripts/port.sh export --from claude --out bundle.json
```

```json
{
  "format": "port-bundle-v1",
  "agents": [{"name": "search", "command": "npx", "args": ["-y", "search-server"]}],
  "secrets": {"API_KEY": "{{PLACEHOLDER:API_KEY}}"}
}
```

### 场景二：跨环境导入

```bash
# 导入到另一个 Agent 环境
{baseDir}/scripts/port.sh import --to cursor --bundle bundle.json

# 替换占位符（导入后填真实凭证）
{baseDir}/scripts/port.sh fill --bundle bundle.json --env .env
```

### 场景三：配置校验

```bash
# 依赖说明
{baseDir}/scripts/port.sh validate --bundle bundle.json
```

## 快速开始

1. 在源环境执行 `export` 生成清单。
2. 检查清单中占位符项。
3. 在目标环境执行 `import`。
4. 填入真实凭证并校验。

## 示例

凭证占位符约定：

| 占位符 | 说明 |
|:-------|:-----|
| `{{PLACEHOLDER:KEY}}` | 导出时敏感值占位 |
| `.env` | 导入后填真实值 |
| `secrets` 字段 | 集中管理所有占位符 |

## 最佳实践

- **凭证必占位**：导出时所有密钥占位符化，清单可安全分享。
- **导入后校验**：导入后跑 `validate` 确认依赖与格式。
- **清单版本化**：导出清单存版本库（不含真实凭证），便于回滚。
- **单环境先试**：新环境先导入单个工具验证，再批量。
- **依赖先装**：导入前确认 Node/Python 等运行时已装。

## 常见问题

**Q1：能批量迁移多环境吗？**
A：不能。批量多环境与团队同步为专业版能力。

**Q2：凭证会泄露吗？**
A：不会。导出时占位符化，真实凭证仅本地 `.env`。

**Q3：导入失败怎么办？**
A：跑 `validate` 看依赖与格式，缺依赖先装。

**Q4：免费版支持冲突合并吗？**
A：不支持。冲突合并与版本治理为专业版能力。

**Q5：清单能在不同 OS 间用吗？**
A：能。清单为 JSON，路径用占位符，导入时按 OS 适配。

## 进阶用法

### 导出清单详解

```json
{
  "format": "port-bundle-v1",
  "exported_at": "2026-07-18T10:00:00+08:00",
  "source_env": "claude",
  "agents": [
    {
      "name": "search",
      "command": "npx",
      "args": ["-y", "search-server"],
      "env": {"API_KEY": "{{PLACEHOLDER:SEARCH_API_KEY}}"}
    },
    {
      "name": "filesystem",
      "command": "npx",
      "args": ["-y", "fs-server", "--root", "/data"]
    }
  ],
  "secrets": {
    "SEARCH_API_KEY": "{{PLACEHOLDER:SEARCH_API_KEY}}"
  }
}
```

### 凭证占位符替换

```bash
# .env 文件填真实凭证
SEARCH_API_KEY=sk-real-key-xxx

# 导入时自动替换占位符
{baseDir}/scripts/port.sh import --to cursor --bundle bundle.json --env .env
```

```text
占位符替换流程:
  1. 导出时敏感值 → {{PLACEHOLDER:KEY}}
  2. 清单可安全分享（无真实密钥）
  3. 导入时读 .env 替换占位符
  4. 真实密钥仅存本地 .env
```

### 配置校验

```bash
# 校验格式与依赖
{baseDir}/scripts/port.sh validate --bundle bundle.json

# 校验结果
{baseDir}/scripts/port.sh validate --bundle bundle.json --report
```

```text
校验项:
  [✓] 格式: port-bundle-v1
  [✓] agents 字段完整
  [✓] command 可执行（npx 已装）
  [⚠] SEARCH_API_KEY 占位符待填
  [✓] 无重复工具名
```

## 跨环境适配

| 环境 | 配置位置 | 适配说明 |
|:-----|:---------|:---------|
| Claude | `.claude/agents/` | JSON 配置 |
| Cursor | `.cursor/` | 设置文件 |
| Codex | 配置文件 | 兼容格式 |
| Gemini CLI | 配置目录 | 兼容格式 |

路径在不同 OS 自动适配，清单用占位符表示路径变量。

## 安全实践

- **凭证必占位**：导出时所有密钥占位符化，清单可分享。
- **.env 不入库**：真实凭证的 `.env` 加入 `.gitignore`。
- **导入后校验**：导入后跑 `validate` 确认依赖与格式。
- **清单版本化**：清单（不含凭证）存版本库，便于回滚。
- **单环境先试**：新环境先导入单工具验证，再批量。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（多数 MCP工具运行时）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | nodejs.org |
| jq | JSON 处理 | 推荐 | 系统包管理器 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 各 MCP工具自身所需 API Key 在导入后填入 `.env`
- 导出清单只含占位符，不含真实密钥

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 完成 MCP工具配置移植

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
