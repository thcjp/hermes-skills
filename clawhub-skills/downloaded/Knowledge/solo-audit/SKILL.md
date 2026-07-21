---
slug: solo-audit
name: solo-audit
version: "1.4.1"
displayName: Audit
summary: Health check knowledge base for broken links, missing frontmatter, tag inconsistencies,
  and cover...
license: MIT
description: |-
  Health check knowledge base for broken links, missing frontmatter, tag
  inconsistencies, and cover。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。适用于独立开发者、企业团队和自动化工作流场景。
tags: '[''Knowledge'']'
tools:
  - read
  - exec
---

# Audit

Audit the knowledge base for quality issues: missing frontmatter, broken links, tag inconsistencies, orphaned files, and coverage gaps. Works on any markdown-heavy project.

## Steps

1. **Parse focus area** from `$ARGUMENTS` (optional). If provided, focus on that area (e.g., "tags", "frontmatter", "links"). If empty, run full audit.
2. **Find all markdown files:** Use Glob to find all .md files, excluding common non-content directories: `.venv/`, `node_modules/`, `.git/`, `archive/`, `.archive_old/`.
3. **Frontmatter audit:** First, scan a sample of existing files (first 10-20) to detect the frontmatter schema in use (which fields exist, what values are common for `type` and `status`). Then for each markdown file, check:

   * Has YAML frontmatter (starts with `---` and has closing `---`)
   * Core fields present: `title`, `tags` (and any other fields consistently used across the KB)
   * `type` and `status` values (if used) are consistent with the detected schema
   * `tags` is a non-empty list
     Track files missing frontmatter and files with incomplete/invalid frontmatter.
4. **Link check:** Look for broken internal links:

   * Grep for markdown links `[.*](.*\.md)` and verify each target file exists
   * If a link-checking script exists in the project (e.g., `scripts/check_links.py`), run it as well
5. **Tag consistency audit:** Use Grep to find all `tags:` sections across .md files. Look for:

   * Near-duplicate tags (e.g., "ai" vs "AI" vs "artificial-intelligence")
   * Tags used only once (potential typos)
   * Very common tags that might be too broad
     List all unique tags with counts.
6. **Orphaned files:** Check which files are NOT referenced in any other file's `related:` field. Files that exist but are never cross-referenced may be orphaned.
7. **Content quality:** Find documents that appear to be ideas or opportunities (based on detected `type` field or directory location) and check:

   * Documents still in `draft` status for more than 30 days
   * Documents missing key metadata fields that other similar documents have
   * Documents with very little content (< 100 words, excluding frontmatter)
8. **Coverage gaps:** Check each directory for content:

   * Flag any empty or near-empty directories
   * Look for directories with only 1-2 files (may need more content)
9. **Output report:**

   text

   ```
   ## KB Audit Report

   **Date:** [today]

   ### Summary
   - Total .md files: X
   - With frontmatter: X (X%)
   - Without frontmatter: X

   ### Frontmatter Issues
   | File | Issue |
   |------|-------|
   | path | Missing field: type |

   ### Broken Links
   [list of broken references]

   ### Tag Analysis
   - Total unique tags: X
   - Single-use tags: [list]
   - Potential duplicates: [list]

   ### Orphaned Files
   [files not referenced anywhere]

   ### Content Quality
   - Stale drafts (> 30 days): [list]
   - Missing metadata: [list]
   - Low-content files: [list]

   ### Coverage
   [directory analysis]

   ### Recommendations
   1. [specific action]
   2. [specific action]
   3. [specific action]
   ```

## Common Issues

### No markdown files found

**Cause:** Running in wrong directory or all files excluded.
**Fix:** Ensure you're in the knowledge base root. Check exclude patterns in step 2.

### Too many single-use tags

**Cause:** Inconsistent tagging across documents.
**Fix:** Pick canonical tags from the most-used list. Run audit again after cleanup.

### Frontmatter validation errors

**Cause:** YAML syntax issues (missing quotes, wrong indentation).
**Fix:** Ensure `---` delimiters are present. Use `type:` and `status:` values consistent with your KB's detected schema.

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

- Health check knowledge base for broken links, missing frontmatter, tag
  inconsistencies, and cover
- 触发关键词: health, knowledge, base, check, audit, broken, solo

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

### Q1: 如何开始使用Audit？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Audit有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
