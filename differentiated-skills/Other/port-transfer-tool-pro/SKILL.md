---
slug: port-transfer-tool-pro
name: port-transfer-tool-pro
version: "1.0.0"
displayName: 工具移植工具专业版
summary: 面向团队的多环境批量同步、冲突合并与版本治理工具。
license: MIT
edition: pro
description: |-
  面向团队的 MCP工具配置多环境同步与版本治理专业工具。

  核心能力:
  - 多环境批量同步与一致性校验
  - 配置冲突合并与版本治理
  - 凭证集中管理与轮换
  - 团队配置模板与 RBAC

  适用场景:
  - 团队多 Agent 环境统一同步
  - 配置冲突合并与版本回滚
  - 凭证集中管理与团队模板

  差异化: 专业版在免费版单环境移植上扩展多环境同步、冲突合并、凭证集中管理与团队模板，兼容免费版清单格式。

  触发关键词: 多环境同步, 冲突合并, 版本治理, 凭证轮换, 团队模板, port pro, sync, rbac
tags:
- 工具移植
- 企业级
- 配置治理
- MCP工具
- 其他工具
tools:
- read
- exec
---

# 工具移植工具（专业版）

## 概述

专业版面向团队与企业，在免费版单环境移植基础上，扩展多环境批量同步、配置冲突合并与版本治理、凭证集中管理与轮换、团队配置模板与 RBAC。清单格式与免费版兼容，已有 bundle 可直接纳入版本治理。

## 核心能力

| 能力 | 说明 | 专业版增强 |
|:-----|:-----|:-----------|
| 多环境同步 | 批量同步多个 Agent 环境 | 一致性校验 |
| 冲突合并 | 配置差异合并与冲突解决 | 三方合并 |
| 版本治理 | 配置版本化与回滚 | 历史追踪 |
| 凭证管理 | 集中存储与轮换 | RBAC |
| 团队模板 | 标准配置模板分发 | 角色基线 |

## 使用场景

### 场景一：多环境批量同步

```bash
# 同步到多个环境（专业版）
{baseDir}/scripts/port-pro.sh sync \
  --bundle team-baseline.json \
  --targets claude,cursor,codex,gemini
```

```text
同步结果:
  claude:  ✓ 8 工具已同步
  cursor:  ✓ 8 工具已同步
  codex:   ⚠ 1 冲突待合并
  gemini:  ✓ 8 工具已同步
```

### 场景二：冲突合并

```bash
# 三方合并冲突配置
{baseDir}/scripts/port-pro.sh merge \
  --base base.json \
  --ours local.json \
  --theirs upstream.json \
  --out merged.json
```

### 场景三：凭证集中管理

```json
{
  "vault": "team-secrets",
  "rotation": {"interval_days": 90, "auto": true},
  "rbac": {"admin": ["rotate", "read"], "dev": ["read"]},
  "templates": {"frontend-dev": ["search", "fs", "browser"]}
}
```

## 快速开始

1. 将免费版 bundle 纳入版本治理。
2. 定义团队基线模板。
3. 配置多环境同步与冲突合并。
4. 接入凭证集中管理与轮换。

## 配置示例

同步配置（`port-sync.json`）：

```json
{
  "baseline": "team-baseline.json",
  "targets": ["claude", "cursor", "codex", "gemini"],
  "merge_strategy": "three-way",
  "consistency_check": true,
  "versioning": {"enabled": true, "retention": 30}
}
```

## 最佳实践

- **基线先定**：团队基线模板定义标准工具集，个人在此基础上扩展。
- **同步前校验**：批量同步前先一致性校验，避免部分失败。
- **冲突三方合**：用三方合并保留本地与上游改动，别简单覆盖。
- **凭证定期轮换**：API Key 90 天轮换，降低泄露风险。
- **RBAC 控权限**：凭证读取按角色，管理员才能轮换。

## 免费版兼容性

| 项目 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 清单格式 | 相同 | 相同（纳入版本） |
| 范围 | 单环境 | 多环境同步 |
| 冲突 | 不支持 | 三方合并 |
| 凭证 | 占位符 | 集中轮换 |

## 常见问题

**Q1：多环境同步会覆盖本地配置吗？**
A：默认三方合并，保留本地改动，冲突项提示人工处理。

**Q2：凭证轮换会中断服务吗？**
A：滚动轮换，新凭证生效后再废弃旧凭证，避免中断。

**Q3：团队模板怎么分发？**
A：基线模板存版本库，成员 `sync` 时自动拉取最新。

**Q4：免费版能升级同步吗？**
A：能。单环境 bundle 作为同步目标之一即可。

**Q5：专业版有优先支持吗？**
A：有。专业版享配置治理与凭证策略咨询。

## 进阶用法

### 多环境同步与一致性校验

```bash
# 同步前一致性校验
{baseDir}/scripts/port-pro.sh check --targets claude,cursor,codex,gemini

# 同步并生成差异报告
{baseDir}/scripts/port-pro.sh sync \
  --bundle team-baseline.json \
  --targets claude,cursor,codex,gemini \
  --report sync-report.json
```

```text
一致性校验:
  claude:  8 工具，配置一致 ✓
  cursor:  7 工具，缺 search ⚠️
  codex:   8 工具，1 配置差异 ⚠️
  gemini:  8 工具，配置一致 ✓
  建议: 同步 baseline 到所有环境
```

### 三方冲突合并

```bash
# 三方合并
{baseDir}/scripts/port-pro.sh merge \
  --base base.json \
  --ours local.json \
  --theirs upstream.json \
  --out merged.json \
  --strategy auto
```

```text
合并策略:
  auto:    自动选择非冲突改动
  ours:    冲突时保留本地
  theirs:  冲突时保留上游
  manual:  冲突项标记待人工

冲突示例:
  工具 search:
    base:  args=["server"]
    ours:  args=["server","--verbose"]
    theirs: args=["server","--debug"]
    → 标记冲突，人工选择
```

### 凭证轮换流程

```text
轮换流程:
  1. 凭证库生成新 Key
  2. 同步新 Key 到所有环境
  3. 验证新 Key 可用
  4. 废弃旧 Key
  5. 记录轮换日志

轮换策略:
  - 90 天定期轮换
  - 泄露即时轮换
  - 滚动轮换（新 Key 生效后再废旧）
```

## 团队模板治理

```text
角色基线模板:
  frontend-dev: [search, fs, browser, design]
  backend-dev:  [search, fs, db, deploy]
  data-dev:     [search, fs, db, notebook]

模板分发:
  - 基线存版本库
  - 新成员 sync 自动拉取角色模板
  - 个人可在基线上扩展，不可删基线工具
```

## 版本治理

- **清单版本化**：配置清单存 Git，变更走 PR 评审。
- **回滚可追溯**：每次同步留版本，可回滚到任意版本。
- **变更审计**：谁在何时改了什么，全留痕。
- **基线评审**：团队基线变更需设计+前端共同评审。
- **豁免限期**：临时豁免标注期限，到期告警。

## 安全与 RBAC

- **凭证集中管**：API Key 集中存凭证库，RBAC 控访问。
- **轮换自动化**：定期轮换，泄露即时轮换。
- **同步密钥范围**：团队同步密钥限范围，避免越权。
- **操作留痕**：所有同步与轮换操作留审计日志。
- **最小权限**：成员按角色授予最小权限。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | nodejs.org |
| jq | JSON 处理 | 必需 | 系统包管理器 |
| 凭证库 | 密钥管理 | 推荐 | Vault / 1Password 等 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 各 MCP工具 API Key 集中存于凭证库，RBAC 控访问
- 团队同步密钥用于多环境统一调度，范围受限
- 凭证库访问凭证建议短时令牌

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 完成多环境同步与治理
