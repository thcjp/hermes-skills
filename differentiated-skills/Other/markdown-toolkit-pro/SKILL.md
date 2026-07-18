---
slug: markdown-toolkit-pro
name: markdown-toolkit-pro
version: "1.0.0"
displayName: Markdown 工具箱专业版
summary: 面向团队的多文件站点、目录生成与文档规范治理工具。
license: MIT
edition: pro
description: |-
  面向团队的多文件 Markdown 站点与文档规范治理专业工具。

  核心能力:
  - 多文件站点与目录（TOC）自动生成
  - 文档规范 lint 与团队规则集
  - 链接校验与死链检测
  - 多格式导出（HTML/PDF/DocBook）

  适用场景:
  - 团队文档站点多文件生成
  - 文档规范 lint 与 CI 集成
  - 死链检测与多格式导出

  差异化: 专业版在免费版单文件基础上扩展多文件站点、规范 lint、死链检测与多格式导出，兼容免费版规则。

  触发关键词: 多文件站点, 目录生成, 文档 lint, 死链检测, 多格式导出, markdown pro, docbook, pdf
tags:
- Markdown
- 企业级
- 文档治理
- 其他工具
tools:
- read
- exec
---

# Markdown 工具箱（专业版）

## 概述

专业版面向团队与企业，在免费版单文件生成基础上，扩展多文件站点与目录生成、文档规范 lint 与团队规则集、链接校验与死链检测、多格式导出。规则与免费版兼容，已有校验可直接纳入规则集。

## 核心能力

| 能力 | 说明 | 专业版增强 |
|:-----|:-----|:-----------|
| 多文件站点 | 目录结构与 TOC 生成 | 站点级 |
| 文档 lint | 规则集与豁免治理 | CI 集成 |
| 链接校验 | 死链检测与锚点校验 | 全站扫描 |
| 多格式导出 | HTML/PDF/DocBook | 一键转换 |

## 使用场景

### 场景一：多文件站点与目录

```bash
# 生成站点目录与 TOC（专业版）
{baseDir}/scripts/md-site.sh build --src docs/ --toc
```

```text
站点结构:
  docs/
    index.md          # 首页（唯一 H1）
    guide/
      getting-started.md
      advanced.md
    _toc.yml          # 自动生成目录
```

### 场景二：文档规范 lint

```yaml
# .markdownlint.json 团队规则集
{
  "default": true,
  "MD013": false,
  "MD024": { "siblings_only": true },
  "MD041": false
}
```

```bash
# CI 校验
markdownlint docs/**/*.md --config .markdownlint.json
```

### 场景三：死链检测与导出

```bash
# 死链检测
{baseDir}/scripts/md-site.sh check-links docs/

# 多格式导出
{baseDir}/scripts/md-site.sh export --to pdf --src docs/ --out build/
```

## 快速开始

1. 将免费版规则纳入团队 lint 规则集。
2. 组织多文件目录结构。
3. 接入 CI lint 与死链检测。
4. 配置多格式导出。

## 配置示例

站点配置（`md-site.json`）：

```json
{
  "src": "docs/",
  "toc": true,
  "lint": {"config": ".markdownlint.json", "block_on_error": true},
  "link_check": {"internal": true, "external": false},
  "export": ["html", "pdf"]
}
```

## 最佳实践

- **目录先规划**：多文件站点先定目录结构，再写内容。
- **lint 入 CI**：文档变更跑 lint，违规阻断合并。
- **死链定期扫**：每周扫描内部链接，修复死链。
- **TOC 自动生**：别手维护目录，用脚本生成避免漏。
- **导出按需**：PDF 用于归档，HTML 用于在线浏览。

## 免费版兼容性

| 项目 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 规则 | 相同 | 相同（纳入规则集） |
| 范围 | 单文件 | 多文件站点 |
| 校验 | 基础 | lint + 死链 |
| 导出 | 不支持 | 多格式 |

## 常见问题

**Q1：多文件站点怎么组织？**
A：按主题分目录，每文件单一 H1，TOC 用脚本生成。

**Q2：lint 规则怎么协同？**
A：规则集 JSON 版本化管理，团队评审后合并。

**Q3：死链检测要联网吗？**
A：内部链接不需联网，外部链接可选检测。

**Q4：导出 PDF 质量如何？**
A：通过 pandoc/wkhtmltopdf 转换，样式可定制模板。

**Q5：专业版有优先支持吗？**
A：有。专业版享文档站点设计与规范咨询。

## 进阶用法

### 多文件站点结构

```text
docs/
  index.md              # 首页（唯一 H1）
  guide/
    getting-started.md  # 入门
    advanced.md         # 进阶
  reference/
    api.md              # API 参考
    config.md           # 配置
  _toc.yml              # 自动生成目录
  _meta.yml             # 元信息
```

### TOC 自动生成

```yaml
# _toc.yml（自动生成，勿手改）
toc:
  - title: 指南
    items:
      - title: 入门
        path: guide/getting-started.md
      - title: 进阶
        path: guide/advanced.md
  - title: 参考
    items:
      - title: API
        path: reference/api.md
```

```bash
# 从目录结构生成 TOC
{baseDir}/scripts/md-site.sh toc --src docs/ --out _toc.yml
```

### 死链检测

```bash
# 内部链接检测
{baseDir}/scripts/md-site.sh check-links docs/ --internal

# 锚点检测
{baseDir}/scripts/md-site.sh check-links docs/ --anchors

# 输出报告
{baseDir}/scripts/md-site.sh check-links docs/ --report broken.json
```

```text
死链报告示例:
  docs/guide/advanced.md:
    - [无效链接](./missing.md) → 文件不存在
    - [无效锚点](#不存在的章节) → 锚点缺失
```

### 多格式导出

```bash
# 导出 PDF（pandoc + LaTeX）
pandoc docs/*.md -o build/manual.pdf \
  --pdf-engine=xelatex \
  -V CJKmainfont="Noto Sans CJK SC"

# 导出 HTML 站点
{baseDir}/scripts/md-site.sh export --to html --src docs/ --out build/

# 导出 DocBook
pandoc docs/*.md -o build/manual.xml -t docbook
```

## 文档规范 lint 规则

| 规则 | 说明 | 严重级 |
|:-----|:-----|:-------|
| MD041 | 首行应为 H1 | block |
| MD024 | 标题不重复 | warn |
| MD012 | 去除多余空行 | warn |
| MD040 | 代码块标语言 | block |
| MD009 | 去除行尾空格 | warn |

## 站点治理

- **目录先规划**：先定目录结构，再写内容，避免后期重构。
- **TOC 自动生**：别手维护目录，脚本生成避免漏。
- **lint 入 CI**：文档变更跑 lint，违规阻断合并。
- **死链定期扫**：每周扫描内部链接，修复死链。
- **导出按需**：PDF 归档，HTML 在线，按需导出。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（lint 工具）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| markdownlint-cli | lint 工具 | 必需 | `npm install -g markdownlint-cli` |
| pandoc | 格式转换 | 导出时必需 | pandoc.org |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令，无需额外 API Key

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 完成多文件站点与文档治理
