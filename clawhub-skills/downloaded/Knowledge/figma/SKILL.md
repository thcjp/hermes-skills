---
slug: figma
name: figma
version: "2.1.0"
displayName: Figma
summary: "This skill does what it advertises: reads Figma data, exports assets, and
  writes user-requested r"
license: MIT
description: |-
  This skill does what it advertises: reads Figma data, exports assets,
  and writes user-requested r。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Knowledge
tools:
  - - read
- exec
---

# Figma

Professional-grade Figma integration for design system analysis, asset export, and comprehensive design auditing.

## Core Capabilities

### 1. File Operations & Analysis

* **File inspection**: Get complete JSON representation of any Figma file
* **Component extraction**: List all components, styles, and design tokens
* **Asset export**: Batch export frames, components, or specific nodes as PNG/SVG/PDF
* **Version management**: Access specific file versions and branch information

**Example usage:**

* "Export all components from this design system file"
* "Get the JSON data for these specific frames"
* "Show me all the colors and typography used in this file"

### 2. Design System Management

* **Style auditing**: Analyze color usage, typography consistency, spacing patterns
* **Component analysis**: Identify unused components, measure usage patterns
* **Brand compliance**: Check adherence to brand guidelines across files
* **Design token extraction**: Generate CSS/JSON design tokens from Figma styles

**Example usage:**

* "Audit this design system for accessibility issues"
* "Generate CSS custom properties from these Figma styles"
* "Find all inconsistencies in our component library"

### 3. Bulk Asset Export

* **Multi-format exports**: Export assets as PNG, SVG, PDF, or WEBP
* **Platform-specific sizing**: Generate @1x, @2x, @3x assets for iOS/Android
* **Organized output**: Automatic folder organization by format or platform
* **Client packages**: Complete deliverable packages with documentation

**Example usage:**

* "Export all components in PNG and SVG formats"
* "Generate complete asset package for mobile app development"
* "Create client deliverable with all marketing assets"

### 4. Accessibility & Quality Analysis

* **Contrast checking**: Verify WCAG color contrast requirements
* **Font size analysis**: Ensure readable typography scales
* **Interactive element sizing**: Check touch target requirements
* **Focus state validation**: Verify keyboard navigation patterns

**Example usage:**

* "Check this design for WCAG AA compliance"
* "Analyze touch targets for mobile usability"
* "Generate an accessibility report for this app design"

## Quick Start

### Authentication Setup

```bash
export FIGMA_ACCESS_TOKEN="[REDACTED]"

echo "FIGMA_ACCESS_TOKEN=your-token" >> .env
```

### Basic Operations

```bash
python scripts/figma_client.py get-file "your-file-key"

python scripts/export_manager.py export-frames "file-key" --formats png,svg

python scripts/style_auditor.py audit-file "file-key" --generate-html

python scripts/accessibility_checker.py "file-key" --level AA --format html
```

## Workflow Patterns

### Design System Audit Workflow

1. **Extract file data** → Get components, styles, and structure
2. **Analyze consistency** → Check for style variations and unused elements
3. **Generate report** → Create detailed findings and recommendations
4. **Manual implementation** → Use findings to guide design improvements

### Asset Export Workflow

1. **Identify export targets** → Specify frames, components, or nodes
2. **Configure export settings** → Set formats, sizes, and naming conventions
3. **Batch process** → Export multiple assets simultaneously
4. **Organize output** → Structure files for handoff or implementation

### Analysis & Documentation Workflow

1. **Extract design data** → Pull components, styles, and design tokens
2. **Audit compliance** → Check accessibility and brand consistency
3. **Generate documentation** → Create style guides and component specs
4. **Export deliverables** → Package assets for development or client handoff

## Resources

### scripts/

* `figma_client.py` - Complete Figma API wrapper with all REST endpoints
* `export_manager.py` - Professional asset export with multiple formats and scales
* `style_auditor.py` - Design system analysis and brand consistency checking
* `accessibility_checker.py` - Comprehensive WCAG compliance validation and reporting

### references/

* `figma-api-reference.md` - Complete API documentation and examples
* `design-patterns.md` - UI patterns and component best practices
* `accessibility-guidelines.md` - WCAG compliance requirements
* `export-formats.md` - Asset export options and specifications

### assets/

* `templates/design-system/` - Pre-built component library templates
* `templates/brand-kits/` - Standard brand guideline structures
* `templates/wireframes/` - Common layout patterns and flows

## 示例

### With Development Workflows

```bash
python scripts/export_manager.py export-tokens "file-key" --format css

python scripts/figma_client.py document-components "file-key" --output docs/
```

### With Brand Management

```bash
python scripts/style_auditor.py audit-file "file-key" --brand-colors "#FF0000,#00FF00,#0000FF"

python scripts/figma_client.py extract-colors "file-key" --output brand-colors.json
```

### With Client Deliverables

```bash
python scripts/export_manager.py client-package "file-key" --template presentation

python scripts/export_manager.py dev-handoff "file-key" --include-specs
```

## 已知限制

### Read-Only Operations

This skill provides **read-only access** to Figma files through the REST API. It can:

* ✅ Extract data, components, and styles
* ✅ Export assets in multiple formats
* ✅ Analyze and audit design files
* ✅ Generate comprehensive reports

### What It Cannot Do

* ❌ **Modify existing files** (colors, text, components)
* ❌ **Create new designs** or components
* ❌ **Batch update** multiple files
* ❌ **Real-time collaboration** features

For file modifications, you would need to develop a **Figma plugin** using the Plugin API.

## 核心能力

### API Rate Limiting

Built-in rate limiting and retry logic to handle Figma's API constraints gracefully.

### Error Handling

Comprehensive error handling with detailed logging and recovery suggestions.

### Multi-Format Support

Export assets in PNG, SVG, PDF, and WEBP with platform-specific sizing.

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

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Figma？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Figma有什么限制？
A: 请参考已知限制章节了解具体限制。
