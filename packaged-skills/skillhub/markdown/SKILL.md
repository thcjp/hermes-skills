---
slug: "markdown"
name: "markdown"
version: 1.0.2
displayName: "Markdown"
summary: "生成干净可移植Markdown,跨解析器正确渲染。Generate clean, portable Markdown that renders correctly across parser"
license: "MIT"
description: |-
  Generate clean, portable Markdown that renders correctly across parsers。核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Other
  - Markdown
  - 文档
  - 工具
  - markdown
  - html
  - toc
  - github
tools:
  - read
  - exec
  - write
homepage: ""
category: "Development"
---
# Markdown

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 高级参数配置与自定义规则 | 不支持 | 支持 |
| 批量任务编排与队列管理 | 不支持 | 支持 |
| 结果导出与多格式转换 | 不支持 | 支持 |
| 实时状态监控与异常告警 | 不支持 | 支持 |
| 历史记录回溯与差异对比 | 不支持 | 支持 |

## 核心能力

- **跨解析器兼容性生成**：生成在GitHub Flavored Markdown、CommonMark、Obsidian、GitLab等解析器中一致渲染的Markdown
- **语法规范化**：统一标题层级（`#`到`######`）、列表标记（`-`/`*`/`+`统一为`-`）、代码块标记（使用三反引号+语言标识）
- **表格格式化**：自动对齐表格列宽、补全分隔行、处理含管道符的转义内容
- **链接与图片优化**：规范化链接格式（行内/引用式）、处理相对路径与锚点、生成TOC目录
- **HTML转Markdown**：将HTML标签转为等效Markdown语法，保留语义结构，丢弃样式属性
- **Markdown Lint**：检测常见格式问题（行尾空格、连续空行、标题跳级、代码块缺语言标识）

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 文档格式规范化 | 混合格式Markdown | 统一风格的规范Markdown + lint报告 |
| HTML转Markdown | HTML页面内容 | 纯Markdown（保留标题/列表/表格/链接） |
| 多平台发布适配 | 原始Markdown | 平台特定Markdown（GitHub/Notion/Obsidian） |
| API文档生成 | 接口描述与参数表 | 标准化Markdown文档 + 自动TOC |
| 技术博客撰写 | 大纲与要点 | 结构化Markdown文章 + 元数据frontmatter |

**不适用于**：富文本编辑器直接渲染（需配合解析器）、PDF排版输出（需额外转换工具）、LaTeX公式排版

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 确定目标平台（GitHub/Notion/Obsidian/GitLab），不同平台对语法的支持有差异
3. 将原始内容（Markdown/HTML/纯文本）作为输入传入，指定转换模式
4. 检查输出Markdown的渲染效果，重点确认表格、代码块、嵌套列表
5. 运行lint检查，按报告修复格式问题
6. 在目标平台预览确认渲染一致后发布

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 是 | 待处理的Markdown/HTML/纯文本内容 |
| mode | string | 否 | 处理模式，可选值: `normalize`(规范化)/`html2md`(HTML转MD)/`lint`(检查)/`toc`(生成目录)，默认 `normalize` |
| target | string | 否 | 目标平台，可选值: `github`/`gitlab`/`obsidian`/`notion`/`commonmark`，默认 `github` |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "markdown": "# 标题\n\n正文内容...",
    "lint_report": [
      {
        "line": 5,
        "rule": "MD012",
        "message": "连续多个空行，应为单个空行",
        "severity": "warning"
      }
    ],
    "toc": [
      {"level": 1, "title": "概述", "anchor": "#概述"},
      {"level": 2, "title": "安装", "anchor": "#安装"}
    ],
    "metadata": {
      "template_used": "reviewer",
      "word_count": 1250,
      "heading_count": 8,
      "table_count": 2,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 详细使用示例

### 示例1：规范化Markdown格式

```text
输入(content):
#标题          ← 标题后缺空格
- 列表项1
* 列表项2      ← 列表标记不统一
```python       ← 代码块语言标识后有多余空格
print("hello")
```

操作(mode): normalize

输出(markdown):
# 标题

- 列表项1
- 列表项2

​```python
print("hello")
​```
```

### 示例2：HTML转Markdown

```text
输入(content):
<h2>功能列表</h2>
<ul>
  <li><strong>快速</strong>：毫秒级响应</li>
  <li><a href="https://example.com">文档</a>：详细说明</li>
</ul>
<table>
  <tr><th>参数</th><th>说明</th></tr>
  <tr><td>mode</td><td>处理模式</td></tr>
</table>

操作(mode): html2md

输出(markdown):
## 功能列表

- **快速**：毫秒级响应
- [文档](https://example.com)：详细说明

| 参数 | 说明 |
|---|---|
| mode | 处理模式 |
```

### 示例3：生成目录（TOC）

```text
输入(content):
# 项目文档
## 安装
### 系统要求
## 使用方法
### 基础用法
### 高级用法
## FAQ

操作(mode): toc

输出(toc):
- [项目文档](#项目文档)
  - [安装](#安装)
    - [系统要求](#系统要求)
  - [使用方法](#使用方法)
    - [基础用法](#基础用法)
    - [高级用法](#高级用法)
  - [FAQ](#faq)
```

## 跨平台兼容性指南

### 各平台语法差异对照

| 语法特性 | GitHub | GitLab | Obsidian | Notion |
|:---------|:------:|:------:|:--------:|:------:|
| 标准表格 | 支持 | 支持 | 支持 | 支持 |
| 任务列表 `- [ ]` | 支持 | 支持 | 支持 | 支持 |
| 脚注 `[^1]` | 支持 | 支持 | 支持 | 不支持 |
| 数学公式 `$$` | 支持 | 支持 | 支持 | 部分支持 |
| Mermaid图表 | 支持 | 支持 | 需插件 | 不支持 |
| 双向链接 `[[ ]]` | 不支持 | 不支持 | 支持 | 不支持 |
| HTML标签 | 部分支持 | 部分支持 | 支持 | 不支持 |
| 目录 `[TOC]` | 不支持 | 支持 | 需插件 | 自动生成 |

### 平台适配建议
- **GitHub发布**：使用GFM语法，任务列表和表格可直接使用，脚注用 `[^1]` 格式
- **Notion导入**：避免使用HTML标签和Mermaid图表，双向链接转为普通链接，脚注转为行内引用
- **Obsidian发布**：可使用 `[[wiki链接]]` 和 `![[嵌入]]`，但导出分享时需转为标准Markdown
- **CommonMark严格模式**：不使用任何扩展语法，仅保留标题、段落、列表、代码块、链接、图片、强调

## 最佳实践

### 标题层级
- 文档只有一个 `#`（H1）作为标题
- 层级递增不跳级（H1 → H2 → H3，不直接H1 → H3）
- 标题前后各保留一个空行
- 标题文本后不加标点（除问号、冒号外）

### 代码块
- 始终标注语言标识：` ```python ` 而非 ` ``` `
- 行内代码用单反引号：`` `code` ``
- 代码块前后各保留一个空行
- 嵌套代码块使用4个反引号 `````

### 列表与缩进
- 统一使用 `-` 作为无序列表标记
- 有序列表使用 `1.` 格式（自动编号）
- 嵌套列表缩进2个空格（非4个，兼容更多解析器）
- 列表项跨行时，续行缩进与标记后的内容对齐

### 链接与图片
- 短链接用行内式：`[文本](url)`
- 长URL用引用式：`[文本][1]` + 文末 `[1]: url`
- 图片加alt文本：`![描述](图片路径)`
- 相对路径使用正斜杠 `/`（跨平台兼容）

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接与代理设置 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.

## 常见问题

### Q1: 如何开始使用Markdown处理功能？
A: 将待处理的Markdown、HTML或纯文本内容作为 `content` 传入，指定 `mode` 为 `normalize`（规范化格式）、`html2md`（HTML转Markdown）、`lint`（格式检查）或 `toc`（生成目录）。默认模式为规范化，目标平台为GitHub。输出包含处理后的Markdown文本、lint报告（如有问题）和自动生成的目录。

### Q2: 如何选择目标平台？
A: 根据Markdown的最终发布位置选择 `target`。GitHub和GitLab支持GFM扩展语法（任务列表、脚注、Mermaid）；Obsidian支持双向链接和嵌入语法；Notion导入时不支持HTML标签和Mermaid，需提前转换；CommonMark模式仅保留标准语法，兼容性最高但功能最少。

### Q3: lint检查包含哪些规则？
A: 检查规则基于markdownlint规则集，包括：MD001（标题层级不跳级）、MD009（行尾空格）、MD012（连续空行）、MD013（行长度限制，默认80字符）、MD032（列表前后空行）、MD040（代码块需语言标识）、MD041（首行应为H1标题）等。每条规则可配置为 `error`、`warning` 或 `off`。

### Q4: HTML转Markdown时如何处理复杂表格？
A: 支持含 `colspan`/`rowspan` 的合并单元格表格转换为标准Markdown表格。由于标准Markdown表格不支持合并单元格，合并单元格会被拆分为独立单元格并填充内容。如果表格结构过于复杂无法准确转换，输出中会包含 `warning` 提示建议手动调整。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
| 表格渲染错位 | 管道符未转义或列数不匹配 | 检查表格分隔行 `|---|` 的列数是否与表头一致 |
| 代码块嵌套渲染异常 | 外层代码块反引号数不足 | 嵌套代码块外层使用4+反引号，内层使用3反引号 |

