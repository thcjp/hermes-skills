---
slug: social-sentiment
name: social-sentiment
version: "1.4.0"
displayName: Social Sentiment
summary: This skill is a disclosed social-listening workflow that uses Xpoz and an
  npm-installed helper, w...
license: MIT
description: |-
  This skill is a disclosed social-listening workflow that uses Xpoz and
  an npm-installed helper, w。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
- Research
tools:
  - - read
- exec
---

# Social Sentiment

**Analyze brand sentiment from live social conversations at scale.**

Surfaces themes, flags viral complaints, compares competitors. Analyzes 1K-70K posts via bulk CSV + Python.

## Setup

Run `xpoz-setup` skill. Verify: `mcporter call xpoz.checkAccessKeyStatus`

## 4-Step Process

### Step 1: Search Platforms

Queries: (1) `"Brand"` (2) `"Brand" AND (slow OR buggy)` (3) `"Brand" AND (love OR amazing)`

```bash
mcporter call xpoz.getTwitterPostsByKeywords query='"Notion"' startDate="YYYY-MM-DD"
mcporter call xpoz.checkOperationStatus operationId="op_..." # Poll 5s
```

Repeat for Reddit/Instagram. Default: 30 days.

### Step 2: Download CSVs

Use `dataDumpExportOperationId`, poll with `checkOperationStatus` for download URL (up to 64K rows).

### Step 3: Analyze

Python/pandas:

```python
import pandas as pd
df = pd.read_csv('/tmp/twitter-sentiment.csv')

POSITIVE = ['love', 'amazing', 'best', 'recommend']
NEGATIVE = ['hate', 'terrible', 'worst', 'broken']

def classify(text):
    t = str(text).lower()
    pos = sum(1 for k in POSITIVE if k in t)
    neg = sum(1 for k in NEGATIVE if k in t)
    return 'positive' if pos>neg else ('negative' if neg>pos else 'neutral')

df['sentiment'] = df['text'].apply(classify)
```

Extract themes, find viral by engagement. Customize keywords.

### Step 4: Report

```text
Sentiment: 72/100 | Posts: 14,832
😊 58% | 😠 24% | 😐 18%

Themes: Performance (2K, 81% neg), UX (1.8K, 72% pos)
Viral: [Top 10]
```

Score: Engagement-weighted, 0-100. Include insights.

## Tips

Download full CSVs | Reddit = honest | Store `data/social-sentiment/` for trends

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

- This skill is a disclosed social-listening workflow that uses Xpoz and
  an npm-installed helper, w
- 触发关键词: sentiment, listening, social, disclosed, skill

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

### Q1: 如何开始使用Social Sentiment？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Social Sentiment有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
