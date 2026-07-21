# 详细参考 - file-compressor-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
pipeline:
  name: knowledge-base-compression
  description: 企业知识库批量压缩

input:
  path: ./knowledge-base/
  recursive: true
  filter: "*.md,*.txt,*.json"

stages:
  - name: extract-anchors
    type: anchor-extraction
    config: ./anchors.yaml

  - name: compress
    type: compression
    level: L2
    parallel: 8
    chunk_size: 100

  - name: verify
    type: multi-model-verification
    models: ["gpt-4o", "claude-3-5-sonnet"]
    strategy: majority-vote

  - name: report
    type: quality-report
    format: html
    output: ./reports/

output:
  path: ./compressed/
  preserve_structure: true
  naming: "{original}.compressed{ext}"

checkpoint:
  enabled: true
  file: ./batch-state.json
  interval: 100  # 每100个文件保存检查点
on_failure:
  strategy: continue  # continue | stop | retry
  retry: 3
  backoff: exponential
```

## 代码示例 (yaml)

```yaml
formats:
  code:
    preserve:
      - function_signatures
      - class_definitions
      - import_statements
      - type_annotations
    compress:
      - function_bodies: "summary_comment"
      - comments: "preserve_key_only"

  json:
    preserve:
      - required_keys
      - environment_keys
      - secrets_keys
    compress:
      - default_values: "remove"
      - descriptions: "summarize"

  yaml:
    preserve:
      - anchors_and_aliases
      - required_fields
    compress:
      - long_strings: "multiline_to_single"

  markdown:
    preserve:
      - headings
      - code_blocks
      - tables
    compress:
      - paragraphs: "summarize"
      - examples: "compress_to_reference"
```

## 代码示例 (yaml)

```yaml
anchor_sets:
  finance:
    name: 金融领域锚点
    patterns:
      - "\\$[\\d,]+(?:\\.\\d+)?"           # 金额
      - "\\d+(?:\\.\\d+)?%"                # 百分比
      - "\\b[A-Z]{2,5}\\b"                 # 股票代码
      - "\\d{4}-\\d{2}-\\d{2}"             # 日期
    entities:
      types: [organization, person, location]
      min_confidence: 0.9
    preserve_quotes: true
    preserve_source: true

  medical:
    name: 医疗领域锚点
    patterns:
      - "\\d+(?:\\.\\d+)?\\s*(?:mg|ml|g|μg)"  # 剂量
      - "ICD-\\d+"                              # 疾病代码
    warning: "医疗内容压缩需人工复核"

  legal:
    name: 法律领域锚点
    patterns:
      - "第[一二三四五六七八九十百]+条"
      - "《[^》]+》"
    strict_match: true
```

## 代码示例 (yaml)

```yaml
verification:
  models:
    - name: gpt-4o
      role: compressor
      weight: 1.0

    - name: claude-3-5-sonnet
      role: reconstructor
      weight: 1.0

    - name: gemini-1.5-pro
      role: reconstructor
      weight: 0.8

  strategy: majority-vote
  threshold: 0.8  # 80%模型一致即通过
  metrics:
    - anchor_match_rate
    - semantic_similarity
    - information_density
    - readability_score
```

## 代码示例 (yaml)

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: knowledge-compress
spec:
  schedule: "0 3 * * 0"  # 每周日凌晨3点
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: compressor
            image: file-compressor:pro-latest
            args: ["batch", "--config", "/etc/compressor/batch.yaml"]
            env:
            - name: OPENAI_API_KEY
              valueFrom:
                secretKeyRef:
                  name: llm-secrets
                  key: openai-key
```

