---
slug: content-filter-tool-free
name: content-filter-tool-free
version: "1.0.0"
displayName: 内容过滤工具
summary: 面向个人的信息流内容过滤工具，关键词与作者过滤。
license: Proprietary
edition: free
description: |-
  面向个人用户的信息流内容过滤工具。

  核心能力:
  - 关键词过滤与正则匹配
  - 作者屏蔽与白名单
  - 单用户过滤规则管理
  - 过滤后内容查看

  适用场景:
  - 个人过滤信息流噪音
  - 屏蔽特定作者或关键词
  - 单用户过滤规则管理

  差异化: 免费版聚焦个人单用户过滤，提供关键词与作者规则，零成本降噪。

  触发关键词: 内容过滤, 关键词过滤, 作者屏蔽, 白名单, 信息流降噪, content filter, spam filter
tags:
- 内容过滤
- 信息流
- 个人效率
- 其他工具
tools:
  - - read
- exec
---
# 内容过滤工具（免费版）

## 概述

本工具帮助个人用户过滤信息流中的噪音内容，覆盖关键词过滤（含正则）、作者屏蔽与白名单、单用户规则管理与过滤后内容查看。适合个人单用户降噪。

## 核心能力

| 能力 | 说明 | 免费版范围 |
|:-----|:-----|:-----------|
| 关键词过滤 | 关键词与正则匹配 | 单用户 |
| 作者管理 | 屏蔽与白名单 | 单用户 |
| 规则管理 | 增删改查过滤规则 | 本地 |
| 内容查看 | 过滤后信息流 | 只读 |

## 使用场景

### 场景一：关键词过滤

```bash
# 添加关键词过滤规则
{baseDir}/scripts/filter.sh add-keyword "广告"
{baseDir}/scripts/filter.sh add-keyword --regex "(?i)加微信"

# 查看规则
{baseDir}/scripts/filter.sh list
```

### 场景二：作者屏蔽与白名单

```bash
# 屏蔽作者
{baseDir}/scripts/filter.sh block-author "spam-user"

# 加白名单（优先于屏蔽）
{baseDir}/scripts/filter.sh whitelist-author "friend"
```

### 场景三：查看过滤后内容

```bash
# 拉取并过滤信息流
{baseDir}/scripts/filter.sh feed --apply

# 查看被过滤项（调试用）
{baseDir}/scripts/filter.sh feed --show-blocked
```

## 不适用场景

以下场景内容过滤工具不适合处理：

- 非法营销手段
- 虚假宣传
- 恶意竞争


## 触发条件

需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非本工具能力范围的需求。


## 快速开始

1. 配置关键词与作者规则。
2. 拉取信息流并应用过滤。
3. 查看过滤后内容。
4. 按需调整规则。

## 示例

规则配置（`filter-rules.json`）：

```json
{
  "keywords": ["广告", "推广", "加微信"],
  "regex": ["(?i)vx[: ]?\\d+"],
  "blocked_authors": ["spam-user"],
  "whitelist_authors": ["friend"],
  "whitelist_priority": true
}
```

## 最佳实践

- **白名单优先**：白名单优先于屏蔽，避免误伤关注作者。
- **正则控范围**：正则别写太宽，避免误杀正常内容。
- **先看被过滤**：用 `--show-blocked` 检查误杀，再调规则。
- **规则定期清理**：定期清理过时关键词，保持规则精简。
- **敏感词分级**：硬屏蔽与软标记分级，软标记只降权不删。

## 常见问题

**Q1：能多账号过滤吗？**
A：不能。多账号与团队规则同步为专业版能力。

**Q2：正则误杀怎么办？**
A：用 `--show-blocked` 查看被过滤项，缩小正则范围或加白名单。

**Q3：过滤规则存哪？**
A：本地 `filter-rules.json`，可手动备份。

**Q4：免费版支持 AI 语义过滤吗？**
A：不支持。AI 语义识别与多语言过滤为专业版能力。

**Q5：能按时间过滤吗？**
A：免费版支持基础时间范围，复杂调度为专业版能力。

## 进阶用法

### 关键词与正则进阶

```bash
# 普通关键词
{baseDir}/scripts/filter.sh add-keyword "广告"

# 正则匹配（大小写不敏感）
{baseDir}/scripts/filter.sh add-keyword --regex "(?i)加微信|加v|加vx"

# 匹配微信号变体
{baseDir}/scripts/filter.sh add-keyword --regex "vx[: ]?\\d{6,}|微信[: ]?\\d{6,}"
```

### 作者管理策略

```bash
# 屏蔽作者
{baseDir}/scripts/filter.sh block-author "spam-user"

# 白名单（优先于屏蔽）
{baseDir}/scripts/filter.sh whitelist-author "friend"

# 批量屏蔽
{baseDir}/scripts/filter.sh block-author --file blocklist.txt
```

```text
作者管理原则:
  - 白名单优先于屏蔽，避免误伤关注作者
  - 屏蔽累计 3 次违规的作者
  - 白名单定期复核，移除不活跃
  - 屏蔽名单定期清理，避免膨胀
```

### 过滤调试

```bash
# 查看被过滤项（调试误杀）
{baseDir}/scripts/filter.sh feed --show-blocked

# 命中规则追踪
{baseDir}/scripts/filter.sh feed --trace
```

```text
调试输出:
  内容: "加微信低价出"
  命中规则: regex("(?i)加微信")
  动作: 屏蔽
  → 确认无误杀
```

## 规则配置示例

```json
{
  "keywords": ["广告", "推广", "代购"],
  "regex": ["(?i)加微信", "vx[: ]?\\d+"],
  "blocked_authors": ["spam-user-1", "spam-user-2"],
  "whitelist_authors": ["friend-1"],
  "whitelist_priority": true,
  "soft_filter": {
    "enabled": true,
    "keywords": ["可能有帮助"],
    "action": "deprioritize"
  }
}
```

## 过滤策略

- **硬屏蔽与软标记**：硬屏蔽直接删，软标记只降权。
- **白名单优先**：白名单优先于屏蔽，保护关注作者。
- **正则控范围**：正则别太宽，避免误杀正常内容。
- **先看被过滤**：用 `--show-blocked` 检查误杀。
- **规则定期清**：清理过时关键词，保持精简。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 可访问信息流服务端点

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| curl | 命令行工具 | 必需 | 系统包管理器 |
| jq | JSON 处理 | 必需 | 系统包管理器 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 信息流服务访问令牌，建议存环境变量
- 令牌仅用于信息流鉴权，不要泄露

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 应用过滤规则处理信息流

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
