---
slug: "figma"
name: "figma"
version: "2.1.0"
displayName: "Figma"
summary: "This skill does what it advertises: reads Figma data, exports assets, and
license: "Proprietary"
description: |-
  This skill does what it advertises: reads Figma data, exports assets,
  and writes user-requested r。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Knowledge
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# Figma

## 核心能力

### API Rate Limiting
Built-in rate limiting and retry logic to handle Figma's API constraints gracefully.

**输入**: 用户提供API Rate Limiting所需的指令和必要参数。
**处理**: 按照skill规范执行API Rate Limiting操作,遵循单一意图原则。
**输出**: 返回API Rate Limiting的执行结果,包含操作状态和输出数据。### Error Handling
Comprehensive error handling with detailed logging and recovery suggestions.

**输入**: 用户提供Error Handling所需的指令和必要参数。
**处理**: 按照skill规范执行Error Handling操作,遵循单一意图原则。
**输出**: 返回Error Handling的执行结果,包含操作状态和输出数据。### Multi-Format Support

Export assets in PNG, SVG, PDF, and WEBP with platform-specific sizing.- 验证执行结果，确认输出符合预期格式
- 参考`API Rate Limiting`相关配置参数进行设置
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

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

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

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

### 依赖说明
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

## 常见问题

### Q1: 如何开始使用Figma？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Figma有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

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
