---
slug: v2ray-proxy
name: v2ray-proxy
version: "1.0.1"
displayName: V2ray Proxy
summary: V2Ray代理管理 - 自动开关代理、根据网络状况自动配置系统代理。使用场景：OpenClaw需要访问外网时自动开启代理、不需要时关闭。
license: MIT
description: |-
  V2Ray代理管理 - 自动开关代理、根据网络状况自动配置系统代理。使用场景：OpenClaw需要访问外网时自动开启代理、不需要时关闭。

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 自动配置系统, 代理, 根据网络状况, v2ray, 自动开关代理, openclaw, 代理管理, proxy
tags:
- Other
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
