---
slug: v2ray-proxy
name: v2ray-proxy
version: "1.0.1"
displayName: V2ray Proxy
summary: V2Ray代理管理 - 自动开关代理、根据网络状况自动配置系统代理。使用场景：OpenClaw需要访问外网时自动开启代理、不需要时关闭。
license: MIT
description: |-
  V2Ray代理管理 - 自动开关代理、根据网络状况自动配置系统代理。使用场景：OpenClaw需要访问外网时自动开启代理、不需要时关闭。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。
tags:
- Other
tools:
  - - read
- exec
---

# V2ray Proxy

管理 V2Ray 代理的自动开关，根据网络状况自动配置系统代理。

## 功能

* 🚀 启动/停止 V2Ray
* 🌐 自动配置/清除系统代理
* 🔄 自动模式（根据网络状况自动开关）
* 📊 状态查看和连接测试

## 配置

V2Ray 位置: `/media/felix/d/v2rayN-linux-64/`
代理端口: `10808`

## 使用方式

```bash
bash <skill>/scripts/v2ray-proxy.sh on

bash <skill>/scripts/v2ray-proxy.sh off

bash <skill>/scripts/v2ray-proxy.sh auto

bash <skill>/scripts/v2ray-proxy.sh status

bash <skill>/scripts/v2ray-proxy.sh test
```

## 命令说明

| 命令 | 说明 |
| --- | --- |
| `start` | 仅启动 V2Ray |
| `stop` | 仅停止 V2Ray |
| `on` | 启动 + 设置系统代理 |
| `off` | 清除代理 + 停止 |
| `auto` | 自动模式 |
| `status` | 查看状态 |
| `test` | 测试连接 |

## 自动代理工作流

1. 当 Skill平台 需要访问外网（如搜索、API调用）
2. 执行 `auto` 或 `on` 开启代理
3. 访问完成后执行 `off` 关闭代理

## 开机自启

V2Ray 可以设置开机自启，但代理开关由本脚本控制：

```bash
```

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

* 🚀 启动/停止 V2Ray
* 🌐 自动配置/清除系统代理
* 🔄 自动模式（根据网络状况自动开关）
* 📊 状态查看和连接测试

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

### Q1: 如何开始使用V2ray Proxy？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: V2ray Proxy有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
