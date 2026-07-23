---
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
---

Analyze construction drawings (PDF, DWG) to extract dimensions, annotations, symbols, title block data, and support automated quantity takeoff and design review.

## Business Case
Drawing analysis automation enables:

* **Faster Takeoffs**: Extract quantities from drawings
* **Quality Control**: Verify drawing completeness
* **Data Extraction**: Pull metadata for project systems
* **Design Review**: Automated checking against standards

## Technical Implementation

> 详细代码示例已移至 `references/detail.md`

## Quick Start
```python
analyzer = DrawingAnalyzer()

result = analyzer.analyze_pdf_drawing("A101_Floor_Plan.pdf")

if result.title_block:
    print(f"Sheet: {result.title_block.sheet_number}")
    print(f"Title: {result.title_block.sheet_title}")
    print(f"Scale: {result.title_block.scale}")

print(f"Dimensions: {len(result.dimensions)}")
print(f"Annotations: {len(result.annotations)}")
print(f"Symbols: {len(result.symbols)}")

for issue in result.quality_issues:
    print(f"Issue: {issue}")

report = analyzer.generate_report(result)
print(report)
```

## Dependencies
```bash
pip install pdfplumber
```

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
Analyze construction drawings (PDF, DWG) to extract dimensions, annotations, symbols, title block data, and support automated quantity takeoff and design review.

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例
### 示例1：基础用法
```
```python
analyzer = DrawingAnalyzer()

result = analyzer.analyze_pdf_drawing("A101_Floor_Plan.pdf")

if result.title_block:
    print(f"Sheet: {result.title_block.sheet_number}")
    print(f"Title: {result.title_block.sheet_title}")
    print(f"Scale: {result.title_block.scale}")

print(f"Dimensions: {len(result.dimensions)}")
print(f"Annotations: {len(result.annotations)}")
print(f"Symbols: {len(result.symbols)}")

for issue in result.quality_issues:
    print(f"Issue: {issue}")

report = anal
```

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用Drawing Analyzer？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Drawing Analyzer有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
