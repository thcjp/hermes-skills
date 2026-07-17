---
slug: finance-report-analyzer
name: finance-report-analyzer
version: "1.2.0"
displayName: Finance Report Analyzer
summary: Analyze financial data from uploaded Excel/PDF files and generate interactive
  reports with sparkl...
license: MIT
description: |-
  Analyze financial data from uploaded Excel/PDF files and generate interactive
  reports with sparkl...

  核心能力:

  - 金融工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 交易分析、投资决策、财务计算

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: financial, uploaded, report, finance, data, analyze, analyzer
tags:
- Finance
tools:
- read
- exec
---

# Finance Report Analyzer

Generate financial analysis reports from uploaded Excel/PDF files with inline SVG sparkline trend charts and multi-format output.

## Quick Start

```bash
python3 scripts/generate_report.py input.xlsx -o pdf --company "公司名" --ticker "000001.SZ"
```

## Output Formats

`-o` flag controls output. **HTML is always generated** as the base; other formats convert from HTML.

| Flag | Output | Requires |
| --- | --- | --- |
| `-o html` | HTML only | (built-in) |
| `-o pdf` | HTML + PDF (default) | wkhtmltopdf or chromium |
| `-o doc` | HTML + DOCX | pandoc |
| `-o md` | HTML + Markdown | pandoc or markdownify |

## Workflow

### Step 1: Acquire Data File

Try in order:

1. **Feishu chat file attachment** — Download via API:

   bash

   ```
   # Get token
   TOKEN=$(curl -s -X POST 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal' \
     -H 'Content-Type: application/json' \
     -d '{"app_id":"APP_ID","app_secret":"APP_SECRET"}' | python3 -c "import json,sys; print(json.load(sys.stdin)['tenant_access_token'])")
   # Get file_key from message
   curl -s "https://open.feishu.cn/open-apis/im/v1/messages/{message_id}" -H "Authorization: Bearer $TOKEN"
   # Download
   curl -s "https://open.feishu.cn/open-apis/im/v1/messages/{message_id}/resources/{file_key}?type=file" \
     -H "Authorization: Bearer $TOKEN" -o /tmp/data.xlsx
   ```

   Get app credentials: read `channels.feishu.appId`/`appSecret` from skill-platform.json.
2. **Feishu Doc/Bitable link** — Use feishu_doc/feishu_bitable tools
3. **Local file** — Use directly
4. **Pasted text** — Parse and save as xlsx

### Step 2: Generate Report

```bash
python3 scripts/generate_report.py /tmp/data.xlsx -o pdf \
  --company "百济神州-U" --ticker "688235.SH" --output-dir /tmp/reports
```

### Step 3: Web Search Enhancement (Optional)

Search for industry benchmarks:

```text
web_search("{company} 行业对比 市场份额 {year}")
```

### Step 4: Deliver File via Feishu API

The `message` tool may send paths as text. Use direct Feishu API to send real file messages:

```bash
UPLOAD=$(curl -s -X POST 'https://open.feishu.cn/open-apis/im/v1/files' \
  -H "Authorization: Bearer $TOKEN" \
  -F 'file_type=stream' \
  -F "file_name=report.html" \
  -F "file=@/path/to/report.html")
FILE_KEY=$(echo "$UPLOAD" | python3 -c "import json,sys; print(json.load(sys.stdin)['data']['file_key'])")

curl -s -X POST 'https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d "{\"receive_id\":\"CHAT_ID\",\"msg_type\":\"file\",\"content\":\"{\\\"file_key\\\":\\\"$FILE_KEY\\\"}\"}"
```

## Report Features

* **Sparkline trend charts**: Each metric row has an inline SVG showing the trend (solid=actual, dashed=forecast)
* **Forecast markers**: Predicted values marked with ⟡ symbol and yellow background
* **Color coding**: Green=positive, Red=negative
* **Responsive**: Works on mobile and desktop
* **Print-ready**: CSS print styles included

## Metric Definitions

See [references/metrics.md](/api/v1/skills/finance-report-analyzer/file?path=references%2Fmetrics.md&ownerHandle=qiujiahong) for financial metric calculations.

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
