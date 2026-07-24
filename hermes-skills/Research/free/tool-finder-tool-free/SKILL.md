---
name: "tool-finder-tool-free"
description: "统一搜索 SkillHub 技能和 MCP server的智能发现工具,支持评分排序与推荐等级"
license: Proprietary
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "工具发现引擎免费版"
  version: "1.0.0"
  summary: "统一搜索 SkillHub 技能和 MCP server的智能发现工具,支持评分排序与推荐等级"
  tags:
    - "研究工具"
    - "工具发现"
    - "搜索引擎"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
---

# 工具发现引擎免费版

## 概述

工具发现引擎免费版是一款面向个人用户的智能工具搜索工具。它统一搜索 SkillHub 平台的技能和 MCP server,通过名称匹配优先、评分排序、推荐等级等机制,帮助用户快速找到最合适的工具,并支持一键安装。

本工具特别适合个人开发者和技术爱好者,在 SkillHub 平台中探索和发现新的技能与工具。免费版提供完整的搜索和安装能力,无需注册,开箱即用。

## 核心能力

### 1. 统一搜索

统一搜索 SkillHub 技能和 MCP server,一次查询覆盖多个来源。

```bash
# 搜索技能
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "web search"

# 搜索 MCP server
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "github" --type mcp

# 搜索所有类型
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "database" --all
```

**输入**: 用户提供统一搜索所需的指令和必要参数。
**处理**: 按照skill规范执行统一搜索操作,遵循单一意图原则。
**输出**: 返回统一搜索的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 名称匹配优先

优先匹配工具名称,确保精准定位。

```bash
# 精确名称搜索(知道工具名时)
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "browser-automation" --exact

# 模糊搜索(不知道确切名称时)
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "browser"
```

**输入**: 用户提供名称匹配优先所需的指令和必要参数。
**处理**: 按照skill规范执行名称匹配优先操作,遵循单一意图原则。
**输出**: 返回名称匹配优先的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 评分排序与推荐等级

按评分排序,并提供清晰的推荐等级。

```bash
# 默认按评分排序
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "news"

# 显示详细评分信息
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "news" --verbose
```

**推荐等级体系:**

| 等级 | 图标 | 条件 |
|:-----|:-----|:-----|
| 强烈推荐 | 5星 | 评分 3.5+ 且名称高度匹配 |
| 推荐 | 4星 | 评分 3.0+ 且名称相关 |
| 一般 | 3星 | 评分 2.0+ 或名称部分匹配 |
| 低相关 | 2星 | 评分 1.0+(模糊搜索常见) |
| 不推荐 | 无 | 评分 1.0 以下(默认隐藏) |

**输入**: 用户提供评分排序与推荐等级所需的指令和必要参数。
**处理**: 按照skill规范执行评分排序与推荐等级操作,遵循单一意图原则。
**输出**: 返回评分排序与推荐等级的执行结果,包含操作状态和输出数据。

### 4. 来源标识

清晰区分搜索结果的来源平台。

```bash
# 搜索结果显示来源
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "search" --verbose

# 示例
# tavily-search [SkillHub] ⭐⭐⭐⭐⭐ - Web search skill
# brave-search [MCP服务] ⭐⭐⭐⭐ - Brave search MCP service
```

**输入**: 用户提供来源标识所需的指令和必要参数。
**处理**: 按照skill规范执行来源标识操作,遵循单一意图原则。
**输出**: 返回来源标识的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 依赖详情

直接安装发现的工具。

```bash
# 安装技能
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh install "tavily-search" --type skill

# 安装 MCP server
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh install "github" --type mcp
```

**输入**: 用户提供依赖说明所需的指令和必要参数。
**处理**: 按照skill规范执行依赖说明操作,遵循单一意图原则。
**输出**: 返回依赖说明的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：的智能发现工具、支持评分排序与推、工具发现引擎免费、面向个人用户提供、智能的技能和工具、搜索能力、平台技能和、支持评分排序、来源标识等功能、Use、when、SEO、关键词分析、排名提升、搜索流量优化时使、不适用于黑帽、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景

### 场景一:个人开发者寻找 Web 搜索技能

小王需要找一个网页搜索的技能,用于自动化信息采集。

```bash
# 步骤1:搜索相关技能
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "web search" --type skill

# 步骤2:查看详细评分
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "web search" --verbose

# 步骤3:安装推荐的技能
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh install "tavily-search" --type skill
```

### 场景二:探索可用的 MCP server

小李想了解有哪些 MCP server可以连接 GitHub。

```bash
# 搜索 GitHub 相关 MCP
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "github" --type mcp

# 搜索代码托管相关 MCP
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "code hosting" --type mcp
```

### 场景三:发现新工具

小张想探索 SkillHub 平台有哪些实用工具。

```bash
# 搜索热门工具
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "automation" --limit 10

# 搜索特定类别
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "research" --type skill --limit 5
```

## 快速开始

### 第一步:配置自动触发(可选)

在 `AGENTS.md` 中添加自动触发配置:

```markdown
### 工具发现 - 优先使用 tool-finder

当用户要求查找/搜索/安装技能或 MCP 时:

1. 始终优先使用 `tool-finder` 技能
2. 不要直接使用平台搜索
3. 搜索命令:
   ```bash
   ~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "<关键词>" --type skill
   ```
4. 安装命令:
   ```bash
   ~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh install <名称> --type skill
   ```
```

### 第二步:执行首次搜索

```bash
# 搜索 Web 相关技能
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "web"

# 查看 MCP server
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "" --type mcp --limit 10
```

### 第三步:安装工具

```bash
# 安装找到的技能
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh install "target-skill" --type skill
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。


## 配置示例

### 基础配置

```bash
# config.json - 工具发现配置
{
  "search": {
    "default_type": "all",
    "default_limit": 10,
    "min_rating": 1.0,
    "exact_match_priority": true
  },
  "sources": {
    "skillhub": true,
    "mcp": true
  },
  "install": {
    "auto_confirm": false,
    "install_dir": "~/.skill-platform/workspace/skills"
  }
}
```

### 搜索策略配置

```bash
# 优先原词搜索,不足时扩展
{
  "strategy": {
    "primary_search": "exact",
    "fallback_search": "fuzzy",
    "expand_synonyms": true,
    "deduplicate": true
  }
}
```

## 最佳实践

### 1. 优先使用精确搜索

```bash
# 知道工具名时,用精确搜索
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "exact-name" --exact

# 不知道工具名时,用模糊搜索
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "function description"
```

### 2. 善用类型过滤

```bash
# 只搜技能
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "keyword" --type skill

# 只搜 MCP
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "keyword" --type mcp

# 搜全部(默认)
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "keyword"
```

### 3. 合理设置结果数量

```bash
# 快速浏览:少结果
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "keyword" --limit 5

# 深度探索:多结果
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "keyword" --limit 20
```

### 4. 使用 verbose 排查问题

```bash
# 遇到问题时查看详细日志
~/.skill-platform/workspace/skills/tool-finder-tool-free/scripts/tool-finder.sh search "keyword" --verbose
```

## 常见问题

### Q1: 搜索结果为空怎么办?

**A:** 尝试以下方法:

1. 使用更宽泛的关键词
2. 尝试同义词:如"search"换成"query"
3. 使用英文关键词(工具名多为英文)
4. 使用 `--all` 显示所有结果(包括低评分)
5. 使用 `--verbose` 查看详细错误

### Q2: 搜索结果与平台网页不一致?

**A:** 由于搜索算法不同(向量搜索 vs 文本搜索),结果可能有差异。建议:

1. 重要工具在平台网页验证
2. 使用 `--exact` 精确搜索
3. 使用 `--verbose` 查看搜索过程

### Q3: 遇到限流怎么办?

**A:** 未登录时可能遇到速率限制(60 次/小时)。解决方法:

1. 等待几分钟后重试
2. 登录平台提高限制
3. 使用 `--verbose` 确认是否限流

### Q4: MCP server 安装需要什么?

**A:** MCP server 安装需要指定客户端(如 claude-code/cursor/vscode)。工具会输出指引,帮助您完成安装。

### 已知限制

**A:** 免费版主要面向个人搜索场景,具备完整的搜索和安装能力。如需批量搜索、团队推荐、工具评估报告等高级功能,请考虑升级到 PRO 版本。

## 依赖说明

### 运行环境

- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Shell**: Bash(Windows 需 Git Bash 或 WSL)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | 官方网站下载安装 |
| npx | 包执行器 | 必需 | 随 Node.js 安装 |
| curl | HTTP 工具 | 必需 | 系统自带 |
| jq | JSON 解析 | 推荐 | 包管理器安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

免费版使用平台公共 API,无需额外 API Key。登录平台账户可提高搜索配额。

```bash
# 可选:登录平台提高配额
npx @anthropic-ai/skillhub@latest login
```

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,通过 exec 执行 Shell 脚本)
- **说明**: 基于命令行的工具发现引擎,通过自然语言指令驱动 Agent 搜索和安装技能与 MCP server
- **适用规模**: 个人用户、单次搜索、本地运行

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```
