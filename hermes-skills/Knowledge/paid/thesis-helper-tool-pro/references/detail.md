# 详细参考 - thesis-helper-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (json)

```json
{
  "edition": "pro",
  "batch": {
    "max_concurrency": 20,
    "timeout": 300000,
    "retry_attempts": 3
  },
  "plagiarism": {
    "engine": "premium",
    "threshold": 0.15,
    "database": "academic + web"
  },
  "team": {
    "enabled": true,
    "version_control": true,
    "real_time_collaboration": true,
    "role_based_access": true
  },
  "languages": {
    "supported": ["zh", "en", "ja", "de", "fr"],
    "standards": {
      "zh": "gbt7714",
      "en": "apa",
      "ja": "jst",
      "de": "din",
      "fr": "afnor"
    }
  },
  "ethics": {
    "checks": ["data_fabrication", "plagiarism", "authorship", "conflict_of_interest"],
    "auto_report": true
  },
  "storage": {
    "archive": true,
    "retention_days": 365,
    "backup": "daily"
  }
}
```

## 代码示例 (bash)

```bash
cat > company_template.json << 'EOF'
{
  "format": {
    "headings": "numeric",
    "references": "ieee",
    "figures": "centered_numbered",
    "tables": "top_numbered"
  },
  "structure": {
    "required_sections": ["abstract", "introduction", "methodology", "results", "conclusion"],
    "abstract_words": 200
  }
}
EOF

thesis-helper batch template \
  --input tech_docs/ \
  --template company_template.json \
  --output standardized_docs/

thesis-helper batch format \
  --input standardized_docs/ \
  --template company_template.json \
  --output format_reports/

thesis-helper report compliance \
  --input format_reports/ \
  --output compliance_report.html
```

## 代码示例 (bash)

```bash
thesis-helper batch abstract \
  --input submissions/ \
  --extract \
  --output abstracts/

thesis-helper batch format \
  --input submissions/ \
  --template journal_standard.json \
  --output format_check/

thesis-helper batch plagiarism \
  --input submissions/ \
  --engine "academic" \
  --output plagiarism_check/

thesis-helper batch ethics \
  --input submissions/ \
  --output ethics_check/

thesis-helper report initial_review \
  --format-reports format_check/ \
  --plagiarism-reports plagiarism_check/ \
  --ethics-reports ethics_check/ \
  --output initial_review_$(date +%Y%m).html
```

## 代码示例 (bash)

```bash
thesis-helper batch format \
  --input /theses/2026/ \
  --output format_reports/ \
  --check "headings,references,tables,figures,abstract" \
  --concurrency 20

thesis-helper batch plagiarism \
  --input /theses/2026/ \
  --engine "premium" \
  --output plagiarism_reports/ \
  --threshold 0.15 \
  --concurrency 10

thesis-helper report summary \
  --format-reports format_reports/ \
  --plagiarism-reports plagiarism_reports/ \
  --output annual_report_2026.html

thesis-helper report filter \
  --format-reports format_reports/ \
  --plagiarism-reports plagiarism_reports/ \
  --criteria "format_score < 80 OR plagiarism_rate > 0.15" \
  --output review_list.csv
```

