---
slug: node-red-manager
name: node-red-manager
version: 1.0.0
displayName: Node Red Manager
summary: Manage Node-RED instances via Admin API or CLI. Automate flow deployment,
  install nodes, and trou...
license: MIT
description: 'Manage Node-RED instances via Admin API or CLI。Automate flow deployment,

  install nodes, and trou。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。'
tags: '[''Automation'', ''Operations'']'
tools:
- read
- exec
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
---

# Node Red Manager

## Setup

1. Copy `.env.example` to `.env`.
2. Set `NODE_RED_URL`, `NODE_RED_USERNAME`, and `NODE_RED_PASSWORD` in `.env`.
3. The script automatically handles dependencies on first run.

## Infrastructure

* **Stack Location**: `deployments/node-red`
* **Data Volume**: `deployments/node-red/data`
* **Docker Service**: `mema-node-red`
* **URL**: `https://flow.glassgallery.my.id`

## Usage

### Flow Management

```bash
scripts/nr list-flows

scripts/nr get-flow <flow-id>

scripts/nr deploy --file assets/flows/watchdog.json

scripts/nr update-flow <flow-id> --file updated-flow.json

scripts/nr delete-flow <flow-id>

scripts/nr get-flow-state

scripts/nr set-flow-state --file state.json
```

### Backup & Restore

```bash
scripts/nr backup
scripts/nr backup --output my-backup.json

scripts/nr restore node-red-backup-20260210_120000.json
```

### Node Management

```bash
scripts/nr list-nodes

scripts/nr install-node node-red-contrib-http-request

scripts/nr get-node node-red-contrib-http-request

scripts/nr enable-node node-red-contrib-http-request
scripts/nr disable-node node-red-contrib-http-request

scripts/nr remove-node node-red-contrib-http-request
```

### Runtime Information

```bash
scripts/nr get-settings

scripts/nr get-diagnostics
```

### Context Management

```bash
scripts/nr get-context flow my-key
scripts/nr get-context global shared-data

scripts/nr set-context flow my-key '"value"'
scripts/nr set-context global counter '42'
scripts/nr set-context global config '{"key": "value"}'
```

## Docker Operations

```bash
cd deployments/node-red && docker compose restart

docker logs mema-node-red --tail 100

docker logs -f mema-node-red
```

## Environment Variables

* `NODE_RED_URL`: Node-RED API endpoint (default: `http://localhost:1880`)
* `NODE_RED_USERNAME`: Admin username
* `NODE_RED_PASSWORD`: Admin password

Legacy variable names (`NR_URL`, `NR_USER`, `NR_PASS`) are supported for backward compatibility.

## API Reference

See `references/admin-api.md` for complete Admin API endpoint documentation.

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

- Manage Node-RED instances via Admin API or CLI
- Automate flow deployment,
  install nodes, and trou
- 触发关键词: node, red, admin, manager, manage, instances, automate

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Node Red Manager？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Node Red Manager有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
