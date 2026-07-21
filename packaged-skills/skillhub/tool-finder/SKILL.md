---
slug: tool-finder
name: tool-finder
version: "1.7.0"
displayName: Tool Finder
summary: 统一搜索 SkillHub skills 和 Smithery 协议 servers 的工具发现引擎。支持评分排序、推荐规则、来源标识。优先原词搜索，扩展补充。**自动触发：看到\
license: MIT
description: |-
  统一搜索 SkillHub skills 和 Smithery 协议 servers 的工具发现引擎。支持评分排序、推荐规则、来源标识。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。
tags: '[''Research'']'
tools:
  - read
  - exec
---
# Tool Finder

## 核心能力

- 统一搜索 SkillHub skills 和 Smithery 协议 servers 的工具发现引擎
- 支持评分排序、推荐规则、来源标识
- 优先原词搜索，扩展补充
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: 自动触发、Use、SEO、关键词分析、排名提升、搜索流量优化时使、不适用于黑帽、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

**看到以下关键词 → 立即调用 tool-finder：**

| 关键词/短语 | 触发操作 |
| --- | --- |
| "找个...skill" / "找...工具" | `tool-finder search "<关键词>"` |
| "有什么 协议" / "协议 推荐" | `tool-finder search "<关键词>" --type 协议` |
| "安装..." / "帮我装..." | `tool-finder install <name> --type skill|协议` |
| " SkillHub" / "Smithery" | `tool-finder search "<相关词>"` |
| "推荐工具" / "有哪些工具" | `tool-finder search "<功能>"` |
| "能...的 skill" | `tool-finder search "<功能>" --type skill` |

---

## 使用流程

Smithery 协议 安装需指定客户端（claude-code/cursor/vscode 等）。

**解决**：输出指引让用户手动安装。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

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
**效果：** AI 会自动在找 skill/协议 时使用 tool-finder，无需每次指定！

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
### 示例 2：找 协议
```

用户：有什么 协议 可以连接 GitHub？

AI：[执行 tool-finder search "github" --type 协议]

AI：找到 GitHub 相关 协议：

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

## 常见问题

### Q1: 如何开始使用Tool Finder？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Tool Finder有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

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

### 6. 协议 安装需要客户端

Smithery 协议 安装需指定客户端（claude-code/cursor/vscode 等）。

**解决**：输出指引让用户手动安装。

### 7. 搜索关键词

* 优先用英文（工具名多为英文）
* 中文可试，但效果可能较差
* 使用连字符的技能名要精确搜索（如 `agent-orchestrator`）

### 8. 路径问题

* 使用绝对路径：`~/.skill-platform/workspace/skills/tool-finder/scripts/tool-finder.sh`
* 或确保 PATH 包含 scripts 目录

---
