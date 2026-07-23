---
slug: tool-finder
name: tool-finder
version: "1.7.0"
displayName: Tool Finder
summary: 统一搜索 ClawHub skills 和 Smithery MCP servers 的工具发现引擎。支持评分排序、推荐规则、来源标识。优先原词搜索，扩展补充。**自动触发：看到\
license: MIT
description: |-
  统一搜索 ClawHub skills 和 Smithery MCP servers 的工具发现引擎。支持评分排序、推荐规则、来源标识。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。
tags: '[''Research'']'
tools:
  - read
  - exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Tool Finder

**统一搜索 SkillHub skills 和 Smithery MCP servers 的工具发现引擎。**

---

## 🎯 自动触发规则（AI 必读）

**安装本技能后，AI 会自动在以下场景使用 tool-finder：**

### 触发关键词

| 用户说 | AI 操作 |
| --- | --- |
| "找个...skill" / "找...工具" | `tool-finder search "<关键词>"` |
| "搜索 skill" / "搜索工具" | `tool-finder search "<关键词>"` |
| "有什么 MCP" / "MCP 推荐" | `tool-finder search "<关键词>" --type mcp` |
| "安装..." / "帮我装..." | `tool-finder install <name> --type skill|mcp` |
| "SkillHub" / "Smithery" | `tool-finder search "<相关词>"` |
| "推荐工具" / "有哪些工具" | `tool-finder search "<功能>"` |
| "能...的 skill" | `tool-finder search "<功能>" --type skill` |

### 为什么不直接用 SkillHub 命令？

| 对比项 | SkillHub search | tool-finder |
| --- | --- | --- |
| 名称匹配 | ❌ 只看评分 | ✅ 名称匹配优先 |
| 结果过滤 | ❌ 无过滤 | ✅ 隐藏低质结果 |
| 推荐等级 | ❌ 无 | ✅ ⭐⭐⭐⭐⭐ 到 ❌ |
| 限流处理 | ❌ 直接失败 | ✅ 自动回退 |
| 来源标识 | ❌ 无 | ✅ SkillHub/Smithery |

**结论：tool-finder 是 SkillHub 的智能封装，搜索结果更精准！**

---

---

## 适用场景

**看到以下关键词 → 立即调用 tool-finder：**

| 关键词/短语 | 触发操作 |
| --- | --- |
| "找个...skill" / "找...工具" | `tool-finder search "<关键词>"` |
| "有什么 MCP" / "MCP 推荐" | `tool-finder search "<关键词>" --type mcp` |
| "安装..." / "帮我装..." | `tool-finder install <name> --type skill|mcp` |
| " SkillHub" / "Smithery" | `tool-finder search "<相关词>"` |
| "推荐工具" / "有哪些工具" | `tool-finder search "<功能>"` |
| "能...的 skill" | `tool-finder search "<功能>" --type skill` |

---

## ⚡ 快速命令参考

```bash
~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh search "<query>"

~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh search "<query>" --type skill

~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh search "<query>" --type mcp

~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh search "<query>" --limit 5

~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh search "agent-orchestrator" --exact

~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh search "<query>" --verbose

~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh search "<query>" --all

~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh install <name> --type skill
~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh install <name> --type mcp
```

---

## 📋 激活条件详解

### ✅ 必须触发的场景

1. **用户明确要找工具**

   * "帮我找个能搜索 web 的 skill"
   * "有什么 MCP 可以连接 GitHub？"
   * "推荐一个数据库工具"
2. **用户提到工具市场**

   * "SkillHub 上有什么好工具？"
   * "Smithery 上有搜索 MCP 吗？"
3. **用户要安装/卸载**

   * "安装 tavily-search"
   * "帮我装个 GitHub MCP"
4. **当前技能不足**

   * 用户需要的功能当前没有合适 skill/MCP
   * 你需要推荐替代方案

### ❌ 不要触发的场景

1. **工具已存在，只是不会用**

   * "怎么用 weather skill？" → 直接教用法，别搜索
2. **通用问题**

   * "今天天气怎么样" → 直接用 weather 工具
3. **闲聊**

   * "你觉得哪个工具好用" → 先搜索再回答

---

## 示例

### 配置自动触发（让 AI 默认使用 tool-finder）

**在 AGENTS.md 中添加以下内容：**

```markdown
### 🔍 Tool Discovery — Use `tool-finder` First!

**When user asks to find/search/install skills or MCPs:**

1. **ALWAYS use `tool-finder` skill first**
2. **DO NOT use `SkillHub search` directly**
3. **Search command:**
   ```bash
   ~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh search "<query>" --type skill
```

4. **Install command:**

   bash

   ```
   ~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh install <name> --type skill
   ```

**Why tool-finder?**

* ✅ Name matching priority (relevant skills appear first)
* ✅ Rating-based filtering (hides irrelevant low-quality results)
* ✅ Clear recommendation levels (⭐⭐⭐⭐⭐ to ❌)
* ✅ Rate limit handling with fallback
* ✅ Shows source (SkillHub vs Smithery)

```text
**效果：** AI 会自动在找 skill/MCP 时使用 tool-finder，无需每次指定！

---

### 示例 1：找 skill
```

用户：帮我找个能搜索 web 的 skill

AI：[执行 tool-finder search "web search" --type skill]

AI：找到以下 web 搜索 skill：

* tavily-search: Tavily Web Search
* baidu-search: baidu web search
* multi-search-engine: Multi Search Engine

推荐 tavily-search，需要安装吗？

```text
### 示例 2：找 MCP
```

用户：有什么 MCP 可以连接 GitHub？

AI：[执行 tool-finder search "github" --type mcp]

AI：找到 GitHub 相关 MCP：

* GitHub: GitHub is a code hosting platform for version control...

需要我帮你安装吗？

```text
### 依赖说明
```

用户：安装 tavily-search

AI：[执行 tool-finder install tavily-search --type skill]

AI：正在安装 tavily-search...
[输出安装结果]

```text
---

## 🔧 实现细节

### 路径

```bash
TOOL_FINDER="~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh"
```

### SkillHub 搜索

```bash
npx SkillHub@latest search "<query>"
```

### Smithery 搜索

```bash
npx @smithery/cli@latest mcp search "<query>" --json

npx @smithery/cli@latest skill search "<query>" --json
```

---

## 已知限制

### 0. 自动触发配置 ✅ 新增

**让 AI 默认使用 tool-finder：**

在 `AGENTS.md` 中添加：

```markdown
### 🔍 Tool Discovery — Use `tool-finder` First!

**When user asks to find/search/install skills or MCPs:**
1. ALWAYS use `tool-finder` skill first
2. DO NOT use `SkillHub search` directly
```

**效果：** AI 会自动使用 tool-finder，无需每次指定！

**分享配置：** 将 AGENTS.md 和 TOOLS.md 分享给其他人，他们也能享受同样的智能搜索体验。

### 1. 搜索策略 ✅ v1.3.0 优化

**优先原词搜索**：先用原词搜索，保证基础结果；如果结果不足，再用同义词扩展补充。

**搜索流程**：

```text
1. 原词搜索 → 返回 N 条结果
2. 如果 N < limit 且未限流 → 扩展搜索（补充结果）
3. 合并去重 → 按评分降序排列
```

**优势**：

* ✅ 原词结果优先，避免扩展词污染
* ✅ 限流时保证有结果
* ✅ 结果不足时自动补充

### 2. 推荐规则 ✅ v1.2.0 新增

**评分排序**：结果按 SkillHub 评分降序排列，高评分技能优先显示。

**推荐等级**：

| 等级 | 图标 | 条件 |
| --- | --- | --- |
| 强烈推荐 | ⭐⭐⭐⭐⭐ | 评分 ≥ 3.5 + 名称高度匹配 |
| 推荐 | ⭐⭐⭐⭐ | 评分 ≥ 3.0 + 名称相关 |
| 一般 | ⭐⭐⭐ | 评分 ≥ 2.0 或 名称部分匹配 |
| 低相关 | ⭐⭐ | 评分 ≥ 1.0（模糊搜索常见） |
| 不推荐 | ❌ | 评分 < 1.0（默认隐藏） |

**过滤规则**：

* 默认隐藏评分 < 1.0 的技能（几乎无关）
* 使用 `--all` 显示所有结果（包括 < 1.0）
* **说明**：模糊搜索分数通常较低（1.0-2.0），这是正常的

### 2. 错误透明化 ✅ 新增

**改进**：遇到 API 限流或搜索失败时，会显示明确的警告信息，而不是内部消化。

**示例输出**：

```text
⚠️  SkillHub API 限流 (Rate limit exceeded)
   建议：等待几分钟后重试，或登录 SkillHub login

══════════════════════════════════════════════════════════════
⚠️  搜索警告
══════════════════════════════════════════════════════════════
• SkillHub: 2 次错误/限流

提示：结果可能不完整，建议:
  1. 等待几分钟后重试（限流情况）
  2. 使用精确模式：--exact（知道技能名时）
  3. 直接访问 https://SkillHub.ai 搜索验证
  4. 使用 --verbose 查看详细错误
```

### 3. 结果可验证性 ✅ 新增

**问题**：搜索结果可能与 SkillHub 网页搜索有差异（向量搜索 vs 文本搜索）。

**解决方案**：

* 使用 `--verbose` 查看详细错误信息
* 重要技能建议访问 <https://SkillHub.ai> 验证
* 使用 `SkillHub inspect <skill-name>` 获取详细信息
* 对比多次搜索结果，确保没有遗漏

### 4. SkillHub 搜索限制

**问题**：SkillHub 使用向量搜索，有时搜功能词（如"RAG"）找不到名字包含该词的 skill（如 `clawrag`）。

**解决方案**：

* 知道名字 → 用 `--exact` 模式：`tool-finder search "clawrag" --exact`
* 不知道名字 → 多试几个关键词：`"rag"`, `"memory"`, `"retrieval"`
* 使用 `SkillHub search` 直接搜索作为补充

### 5. SkillHub Rate Limit

未登录时可能遇到速率限制（60 次/小时）。

**解决**：

* 等待几分钟后重试
* `npx SkillHub login` 登录后提高限制
* 使用 `--verbose` 确认是否限流

### 6. MCP 安装需要客户端

Smithery MCP 安装需指定客户端（claude-code/cursor/vscode 等）。

**解决**：输出指引让用户手动安装。

### 7. 搜索关键词

* 优先用英文（工具名多为英文）
* 中文可试，但效果可能较差
* 使用连字符的技能名要精确搜索（如 `agent-orchestrator`）

### 8. 路径问题

* 使用绝对路径：`~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh`
* 或确保 PATH 包含 scripts 目录

---

## 📦 依赖

* Node.js + npx
* curl
* jq

---

## 🦞 总结

**一句话：用户找工具 → 用 tool-finder search → 返回结果 → 问要不要安装**

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

## 核心能力

- 统一搜索 ClawHub skills 和 Smithery MCP servers 的工具发现引擎
- 支持评分排序、推荐规则、来源标识
- 优先原词搜索，扩展补充
- 触发关键词: 支持评分排序, clawhub, smithery, 来源标识, servers, tool, 统一搜索, finder

## 使用流程

Smithery MCP 安装需指定客户端（claude-code/cursor/vscode 等）。

**解决**：输出指引让用户手动安装。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Tool Finder？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Tool Finder有什么限制？
A: 请参考已知限制章节了解具体限制。
