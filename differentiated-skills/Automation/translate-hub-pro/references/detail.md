# 详细参考 - translate-hub-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────┐
│             中英翻译中枢专业版 (TRANSLATE HUB PRO)                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  输入层       │  │  翻译引擎层   │  │  输出层       │          │
│  │  INPUT       │  │  ENGINE      │  │  OUTPUT      │          │
│  │              │  │              │  │              │          │
│  │  文本/文档   │  │  LLM翻译     │  │  原格式回写   │          │
│  │  批量目录    │→ │  术语匹配    │→ │  多格式导出   │          │
│  │  API/Webhook │  │  TM记忆复用  │  │  API响应     │          │
│  │  ✅ 专业版   │  │  上下文记忆  │  │  CI产物      │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│                  ┌──────────────┐                                │
│                  │  资产管理层   │  ← 专业版独有                  │
│                  │  ASSETS     │                                │
│                  │              │                                │
│                  │  术语库(TB)  │                                │
│                  │  翻译记忆(TM)│                                │
│                  │  领域术语库  │                                │
│                  │  质量评估    │                                │
│                  └──────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 代码示例 (yaml)

```yaml
name: 国际化翻译
on:
  pull_request:
    paths: ['i18n/en/**']
jobs:
  translate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: 翻译至所有语言
        run: |
          pip install translate-hub-pro
          for lang in zh ja ko fr de es ru; do
            translate-hub batch i18n/en/ i18n/$lang/ \
              --source en --target $lang \
              --glossary glossary.yaml \
              --tm tm.tmx \
              --parallel 4
          done
      - name: 质量检查
        run: translate-hub evaluate --min-bleu 0.7
      - name: 提交翻译
        run: |
          git add i18n/
          git commit -m "i18n: 自动翻译更新"
          git push
```

## 代码示例 (yaml)

```yaml
metadata:
  project: "MyApp"
  version: "1.2.0"
  last_updated: "2026-01-15"

terms:
  - source: "Dashboard"
    target: "仪表盘"
    context: "产品主界面"
    forbidden: ["控制面板", "仪表板"]  # 禁止使用的译法
  - source: "Workspace"
    target: "工作空间"
    context: "用户工作区域"

  - source: "API Gateway"
    target: "API网关"
    note: "保留API原文，不译为'应用程序接口'"

  - source: "Webhook"
    target: "Webhook"
    note: "保留原文，行业惯例不翻译"

  - source: "SkillHub"
    target: "SkillHub"
    note: "品牌名不翻译"
```

## 代码示例 (yaml)

```yaml
name: 文档本地化
on:
  push:
    paths: ['docs/en/**']
jobs:
  translate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: 批量翻译文档
        run: |
          pip install translate-hub-pro
          translate-hub batch ./docs/en/ ./docs/zh/ \
            --source en --target zh \
            --glossary glossary.yaml \
            --tm translation_memory.tmx \
            --parallel 4
      - name: 提交翻译结果
        run: |
          git add docs/zh/
          git commit -m "docs: 自动翻译更新"
          git push
```

## 代码示例 (yaml)

```yaml
project:
  name: MyApp Localization
  languages: [zh, ja, ko, fr, de, es, ru]

glossary:
  files: [glossary.yaml, brand_glossary.yaml]
  domains: [it, legal]

translation_memory:
  file: translation_memory.tmx
  auto_save: true
  fuzzy_threshold: 0.75

quality:
  evaluation: true
  min_bleu: 0.7
  glossary_compliance: 1.0

automation:
  ci_integration: true
  webhook: true
  api: true
```

## 代码示例 (python)

```python
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/api/translate", methods=["POST"])
def translate_api():
    payload = request.json
    result = translator.translate(
        text=payload["text"],
        source=payload["source_lang"],
        target=payload["target_lang"],
        glossary=payload.get("glossary"),
        use_tm=payload.get("use_tm", True)
    )
    return jsonify({
        "translation": result.translation,
        "match_type": result.match_type,
        "match_score": result.match_score,
        "glossary_applied": result.glossary_applied
    })
```

## 代码示例 (python)

```python
@app.route("/webhook/cms-content-published", methods=["POST"])
def auto_translate_cms():
    payload = request.json
    content = payload["content"]
    source_lang = payload["language"]

    translator = Translator.from_config("config.yaml")
    for target_lang in ["zh", "ja", "ko"]:
        translated = translator.translate(
            content, source=source_lang, target=target_lang
        )
        cms_api.create_translation(
            original_id=payload["content_id"],
            language=target_lang,
            content=translated.translation
        )
    return {"status": "ok", "translated_to": 3}
```

## 代码示例 (python)

```python
translator = Translator()
translator.load_glossary("glossary.yaml")
translator.load_tm("translation_memory.tmx")
translator.load_domain("it")  # 加载IT领域术语库
stats = translator.translate_directory(
    source_dir="./docs/en/",
    target_dir="./docs/zh/",
    source_lang="en",
    target_lang="zh",
    formats=["md", "docx"],
    parallel=4
)

print(f"翻译完成：{stats.success}/{stats.total}，TM复用率：{stats.tm_reuse_rate}")
translator.save_tm("translation_memory.tmx")  # 保存更新后的TM
```

### 完整搭建（<300秒）
企业级本地化流水线：

```yaml
project:
  name: MyApp Localization
  languages: [zh, ja, ko, fr, de, es, ru]

glossary:
  files: [glossary.yaml, brand_glossary.yaml]
  domains: [it, legal]

translation_memory:
  file: translation_memory.tmx
  auto_save: true
  fuzzy_threshold: 0.75

quality:
  evaluation: true
  min_bleu: 0.7
  glossary_compliance: 1.0

automation:
  ci_integration: true
  webhook: true
  api: true
```

```python
translator = Translator.from_config("localization_config.yaml")

for lang in ["zh", "ja", "ko", "fr", "de", "es", "ru"]:
    translator.translate_directory(
        source_dir="./docs/en/",
        target_dir=f"./docs/{lang}/",
        source_lang="en",
        target_lang=lang,
        parallel=4
    )

report = translator.generate_quality_report()
translator.export_report(report, "quality_report.xlsx")
```



## 架构总览
```text
┌─────────────────────────────────────────────────────────────────┐
│             中英翻译中枢专业版 (TRANSLATE HUB PRO)                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  输入层       │  │  翻译引擎层   │  │  输出层       │          │
│  │  INPUT       │  │  ENGINE      │  │  OUTPUT      │          │
│  │              │  │              │  │              │          │
│  │  文本/文档   │  │  LLM翻译     │  │  原格式回写   │          │
│  │  批量目录    │→ │  术语匹配    │→ │  多格式导出   │          │
│  │  API/Webhook │  │  TM记忆复用  │  │  API响应     │          │
│  │  ✅ 专业版   │  │  上下文记忆  │  │  CI产物      │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│                  ┌──────────────┐                                │
│                  │  资产管理层   │  ← 专业版独有                  │
│                  │  ASSETS     │                                │
│                  │              │                                │
│                  │  术语库(TB)  │                                │
│                  │  翻译记忆(TM)│                                │
│                  │  领域术语库  │                                │
│                  │  质量评估    │                                │
│                  └──────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```



### 翻译性能优化
1. **TM优先**：先查翻译记忆，命中则直接复用，避免调用LLM
2. **批量并行**：多文档并行翻译，根据API限制调整并发数
3. **增量翻译**：仅翻译变更部分，非全量重译
4. **缓存策略**：术语库与TM缓存至内存，减少IO开销



## 性能优化策略


## 版本升级迁移指南


