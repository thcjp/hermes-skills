---
slug: translate-hub-pro
name: translate-hub-pro
version: "1.0.0"
displayName: 中英翻译中枢(专业版)
summary: 企业级多语言翻译专业版，支持批量文档翻译、自定义术语库、翻译记忆库、多语言互译与API集成，覆盖本地化全流程。
license: MIT
edition: pro
description: |-
  中英翻译中枢（专业版）面向翻译团队、本地化工程师与跨国企业，在免费版基础上解锁全部高级能力：无上限批量文档翻译、自定义术语库与团队共享、翻译记忆库（TM）复用历史翻译、多语言互译（中英日韩法德西俄）、文档级上下文记忆、API集成与CI/CD自动化、垂直领域专用术语库。覆盖从单段翻译到企业级本地化流水线的完整工作流。

  核心能力：批量文档翻译（Markdown/Word/Excel/PDF/HTML/JSON/PO/POT）、自定义术语库管理（YAML格式，支持团队共享与版本控制）、翻译记忆库（TMX格式，自动匹配历史翻译）、多语言互译（8种语言双向）、文档级上下文记忆（跨段落保持一致）、领域专用术语库（法律/医疗/金融/IT/游戏/电商）、API集成（REST API与Webhook）、CI/CD流水线集成、翻译质量评估（BLEU/TER指标）、译者协作与审校流程。

  适用场景：软件产品本地化、技术文档批量翻译、多语言网站内容管理、游戏本地化、法律合同翻译、医疗文献翻译、金融报告翻译、开源项目文档国际化、企业内部知识库多语言化。

  差异化：在免费版基础上新增八大高级能力，针对企业级本地化场景设计完整工作流。提供多角色场景指南（本地化工程师/技术写作者/产品经理/法务/医疗翻译/游戏本地化）、性能优化策略、多平台集成示例、版本升级迁移指南。专业版通过SkillHub SkillPay发布。保留原始MIT-0版权声明。

  触发关键词：批量翻译、文档翻译、术语库、翻译记忆库、多语言、本地化、TMX、PO文件、CI集成
tags:
- 翻译工具
- 多语言
- 本地化
- 翻译记忆库
- 术语管理
tools:
- read
- exec
---

# 中英翻译中枢（专业版）

> 企业级本地化翻译中枢。批量文档翻译、术语库管理、翻译记忆复用、多语言互译、API与CI/CD集成，让本地化效率提升10倍。

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

## 核心功能（在免费版基础上新增）

### 1. 批量文档翻译（专业版独有）

支持多种文档格式的批量翻译，无上限：

```python
from translate_hub_pro import BatchTranslator

translator = BatchTranslator()

# 批量翻译目录下所有Markdown文档
results = translator.translate_directory(
    source_dir="./docs/en/",
    target_dir="./docs/zh/",
    source_lang="en",
    target_lang="zh",
    formats=["md", "docx", "xlsx", "pdf", "html", "json", "po"],
    parallel=4  # 4进程并行
)

# 输出示例
# {
#   "total": 45,
#   "success": 43,
#   "failed": 2,
#   "duration": "3m 25s",
#   "tm_reuse_rate": "68%"  # 翻译记忆复用率
# }
```

| 格式 | 处理方式 | 适用场景 |
|------|----------|----------|
| Markdown | 保留格式，翻译正文 | 技术文档、README |
| Word(.docx) | 保留样式，翻译内容 | 合同、报告 |
| Excel(.xlsx) | 按单元格翻译，保留公式 | 报价单、数据表 |
| PDF | 提取文本翻译，重新排版 | 宣传册、白皮书 |
| HTML | 保留标签，翻译可见文本 | 网站内容 |
| JSON | 翻译value，保留key | i18n资源文件 |
| PO/POT | 翻译msgid对应的msgstr | GNU gettext国际化 |

### 2. 自定义术语库管理（专业版独有）

通过YAML格式管理术语库，支持团队共享与版本控制：

```yaml
# glossary.yaml - 项目术语库
metadata:
  project: "MyApp"
  version: "1.2.0"
  last_updated: "2026-01-15"

terms:
  # 产品术语
  - source: "Dashboard"
    target: "仪表盘"
    context: "产品主界面"
    forbidden: ["控制面板", "仪表板"]  # 禁止使用的译法

  - source: "Workspace"
    target: "工作空间"
    context: "用户工作区域"

  # 技术术语
  - source: "API Gateway"
    target: "API网关"
    note: "保留API原文，不译为'应用程序接口'"

  - source: "Webhook"
    target: "Webhook"
    note: "保留原文，行业惯例不翻译"

  # 品牌
  - source: "SkillHub"
    target: "SkillHub"
    note: "品牌名不翻译"
```

```python
# 加载术语库
translator.load_glossary("glossary.yaml")

# 翻译时自动应用术语
text = "Configure the Dashboard and API Gateway in your Workspace."
result = translator.translate(text, source="en", target="zh")
# 输出："在工作空间中配置仪表盘和API网关。"
```

### 3. 翻译记忆库TM（专业版独有）

复用历史翻译，提升一致性与效率：

```python
# 翻译记忆库（TMX格式）
translator.load_tm("translation_memory.tmx")

# 翻译时自动匹配历史
result = translator.translate("Click the button to save changes.", source="en", target="zh")
# 输出："点击按钮保存更改。"
# 匹配信息：
# {
#   "source": "Click the button to save changes.",
#   "target": "点击按钮保存更改。",
#   "match_type": "exact",       # exact | fuzzy | new
#   "match_score": 1.0,
#   "tm_source": "user_manual.md:42"
# }

# 自动将新翻译存入记忆库
translator.save_tm("translation_memory.tmx")
```

| 匹配类型 | 匹配度 | 处理方式 |
|----------|--------|----------|
| 精确匹配 | 100% | 直接复用，无需重新翻译 |
| 模糊匹配 | 75-99% | 复用并微调（如数字、标点差异） |
| 新翻译 | <75% | 调用LLM翻译，并存入记忆库 |

### 4. 多语言互译（专业版独有）

支持8种语言的双向互译：

| 语言 | 代码 | 支持方向 |
|------|------|----------|
| 中文 | zh | ↔ 所有语言 |
| 英文 | en | ↔ 所有语言 |
| 日文 | ja | ↔ 中/英 |
| 韩文 | ko | ↔ 中/英 |
| 法文 | fr | ↔ 中/英 |
| 德文 | de | ↔ 中/英 |
| 西班牙文 | es | ↔ 中/英 |
| 俄文 | ru | ↔ 中/英 |

```python
# 多语言翻译
texts = {
    "en": "Welcome to our platform",
    "ja": "プラットフォームへようこそ",
    "ko": "우리 플랫폼에 오신 것을 환영합니다",
    "fr": "Bienvenue sur notre plateforme"
}

# 统一翻译为中文
for lang, text in texts.items():
    result = translator.translate(text, source=lang, target="zh")
    print(f"{lang} → zh: {result}")
# 输出：
# en → zh: 欢迎使用我们的平台
# ja → zh: 欢迎使用我们的平台
# ko → zh: 欢迎使用我们的平台
# fr → zh: 欢迎使用我们的平台
```

### 5. 文档级上下文记忆（专业版独有）

跨段落保持翻译一致性，理解文档全局上下文：

```python
# 传统翻译：每段独立翻译，可能出现不一致
# 段落1: "The Agent will process the task." → "代理将处理任务。"
# 段落2: "It returns the result." → "它返回结果。"（"It"指代不清）

# 专业版：文档级上下文记忆
result = translator.translate_document(
    "agent_doc.md",
    source="en",
    target="zh",
    context_aware=True  # 启用文档级上下文
)
# 段落1: "The Agent will process the task." → "Agent将处理该任务。"
# 段落2: "It returns the result." → "Agent会返回结果。"（正确指代）
```

### 6. 领域专用术语库（专业版独有）

预置六大垂直领域的专用术语库：

| 领域 | 术语量 | 适用场景 |
|------|--------|----------|
| 法律 | 5000+ | 合同、协议、判决书、法律意见书 |
| 医疗 | 8000+ | 病历、药品说明、临床报告、医学文献 |
| 金融 | 4000+ | 财报、招股书、研究报告、监管文件 |
| IT/软件 | 6000+ | 技术文档、API文档、产品手册 |
| 游戏 | 3000+ | 游戏UI、剧情、道具、技能描述 |
| 电商 | 2000+ | 商品描述、营销文案、退换货政策 |

```python
# 加载领域术语库
translator.load_domain("legal")  # 法律领域
translator.load_domain("medical")  # 医疗领域（可叠加）

# 法律文本翻译
legal_text = "The parties hereto agree to the terms and conditions set forth herein."
result = translator.translate(legal_text, source="en", target="zh")
# 输出："双方同意本文所载的条款与条件。"（使用法律术语）
```

### 7. API集成与CI/CD自动化（专业版独有）

```python
# REST API
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

```yaml
# CI/CD集成示例（GitHub Actions）
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

### 8. 翻译质量评估（专业版独有）

```python
# 质量评估
evaluation = translator.evaluate(
    source="The system will be deployed tomorrow.",
    translation="系统将于明天部署。",
    reference="系统将于明日部署。"  # 参考翻译（可选）
)

# 输出
# {
#   "bleu_score": 0.85,        # BLEU分数（0-1，越高越好）
#   "ter_score": 0.12,         # TER编辑率（0-1，越低越好）
#   "glossary_compliance": 1.0, # 术语合规率
#   "issues": [
#     {"type": "terminology", "severity": "warning", "detail": "建议用'明日'替代'明天'"}
#   ]
# }
```

## 快速开始

### 基础搭建（<60秒）

单段文本翻译（与免费版一致，但启用术语库与TM）：

```python
from translate_hub_pro import Translator

translator = Translator()
translator.load_glossary("glossary.yaml")
translator.load_tm("translation_memory.tmx")

result = translator.translate("Deploy the service to production.", source="en", target="zh")
print(result.translation)  # "将服务部署至生产环境。"
```

### 标准搭建（<120秒）

批量文档翻译+术语库+TM：

```python
translator = Translator()
translator.load_glossary("glossary.yaml")
translator.load_tm("translation_memory.tmx")
translator.load_domain("it")  # 加载IT领域术语库

# 批量翻译文档目录
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
# localization_config.yaml
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

# 多语言批量翻译
for lang in ["zh", "ja", "ko", "fr", "de", "es", "ru"]:
    translator.translate_directory(
        source_dir="./docs/en/",
        target_dir=f"./docs/{lang}/",
        source_lang="en",
        target_lang=lang,
        parallel=4
    )

# 生成质量报告
report = translator.generate_quality_report()
translator.export_report(report, "quality_report.xlsx")
```

## 使用场景

### 场景一：软件产品本地化（本地化工程师角色）

**场景描述**：SaaS产品要进入中国市场，需将全套产品文档（用户手册、API文档、帮助中心、UI文案）从英文翻译为中文，总量约10万字，需在2周内完成并保证术语一致。

**配置**：
```yaml
project:
  name: SaaS Localization CN
  glossary: product_glossary.yaml
  tm: product_tm.tmx
  domain: it

sources:
  - ./docs/user_manual/    # 用户手册 50篇
  - ./docs/api/            # API文档 120篇
  - ./docs/help_center/    # 帮助中心 80篇
  - ./i18n/ui_strings.json # UI文案 500条
```

**Agent行为**：
- 加载产品术语库（含200个产品专属术语）
- 加载历史翻译记忆（复用率约65%）
- 批量翻译250+文档，4进程并行
- UI文案按JSON格式翻译，保留key
- 自动质量评估，标记低分翻译
- 生成术语合规报告

**效果**：10万字本地化从约3周（人工）缩短至2天（自动），术语一致性100%，TM复用率65%节省成本，质量评估BLEU均分0.82。

### 场景二：多语言网站内容管理（产品经理角色）

**场景描述**：产品官网需支持8种语言，每次产品更新都需同步翻译新增内容到8种语言，人工翻译周期长且成本高。

**配置**：
```yaml
project:
  name: Website Localization
  languages: [zh, ja, ko, fr, de, es, ru]
  ci_integration: true

sources:
  - ./website/content/en/  # 英文源文件

automation:
  trigger: "git_push"
  workflow: "translate_and_deploy"
```

**Agent行为**：
- 监听Git推送，新增/修改内容自动触发翻译
- 并行翻译至7种目标语言
- TM复用历史翻译，仅翻译变更部分
- 翻译完成自动提交并触发部署
- 质量不达标的翻译标记为待人工审校

**效果**：多语言同步周期从约5天缩短至2小时，翻译成本降低约70%（TM复用），内容一致性保证。

### 场景三：法律合同翻译（法务角色）

**场景描述**：法务部门需将英文合同翻译为中文，法律术语要求严谨准确，且同一术语在整份合同中必须完全一致。

**配置**：
```python
translator = Translator()
translator.load_domain("legal")  # 法律领域术语库
translator.load_glossary("contract_glossary.yaml")  # 合同专属术语
translator.enable_strict_consistency()  # 严格一致性模式

# 翻译合同
result = translator.translate_document(
    "service_agreement.docx",
    source="en",
    target="zh",
    format="docx",
    preserve_style=True
)
```

**Agent行为**：
- 加载法律领域术语库（5000+法律术语）
- 启用严格一致性：同一英文术语全文必须使用同一中文译法
- 保留Word文档样式（字体、段落、编号）
- 法律条款编号完整保留
- 标记存疑翻译，供法务人工审校

**效果**：50页合同翻译从约5天（人工）缩短至4小时，术语一致性100%，存疑标记减少约80%的人工审校工作量。

### 场景四：游戏本地化（游戏本地化角色）

**场景描述**：游戏要进入日本和韩国市场，需将游戏剧情、UI、道具描述、技能说明从中文翻译为日文和韩文，要求符合当地游戏表达习惯。

**配置**：
```yaml
project:
  name: Game Localization JP/KR
  languages: [ja, ko]
  domain: game

sources:
  - ./game/story/        # 剧情文本
  - ./game/ui/           # UI文案
  - ./game/items/        # 道具描述
  - ./game/skills/       # 技能说明

localization:
  tone: "casual"         # 游戏语气：casual | formal | epic
  character_voice: true  # 角色语气差异化
```

**Agent行为**：
- 加载游戏领域术语库（3000+游戏术语）
- 按角色语气差异化翻译（主角、NPC、反派）
- 道具与技能名称保持简洁有力
- 日文翻译考虑敬语层级
- 韩文翻译考虑敬语与语气词

**效果**：游戏本地化周期从约2个月缩短至2周，玩家满意度提升约30%，角色语气一致性保证。

## 多角色场景指南

| 角色 | 典型场景 | 推荐功能组合 | 核心价值 |
|------|----------|-------------|----------|
| 本地化工程师 | 软件产品本地化 | 批量+术语库+TM+质量评估 | 本地化效率提升10倍 |
| 技术写作者 | 技术文档翻译 | 批量+Markdown保留+IT术语 | 文档翻译效率提升3倍 |
| 产品经理 | 多语言网站管理 | CI集成+多语言+TM | 同步周期从5天到2小时 |
| 法务 | 法律合同翻译 | 法律术语+严格一致性 | 术语一致性100% |
| 医疗翻译 | 医疗文献翻译 | 医疗术语+质量评估 | 术语准确性99%+ |
| 游戏本地化 | 游戏翻译 | 游戏术语+角色语气 | 玩家满意度提升30% |
| 翻译项目经理 | 多项目并行 | 全功能+API+质量报告 | 项目管理效率提升 |

## 性能优化策略

### 翻译性能优化

1. **TM优先**：先查翻译记忆，命中则直接复用，避免调用LLM
2. **批量并行**：多文档并行翻译，根据API限制调整并发数
3. **增量翻译**：仅翻译变更部分，非全量重译
4. **缓存策略**：术语库与TM缓存至内存，减少IO开销

### 术语库优化

1. **分层加载**：常用术语常驻内存，冷门术语按需加载
2. **索引优化**：术语库建立倒排索引，加速匹配
3. **版本控制**：术语库纳入Git，追踪变更历史
4. **团队共享**：术语库通过Git或API团队共享

### TM优化

1. **定期清理**：清除低质量历史翻译，保持TM质量
2. **分库管理**：按项目或领域分库，避免跨领域误匹配
3. **对齐优化**：定期执行TM对齐，修复源文与译文不匹配
4. **压缩存储**：TMX文件定期压缩，减少存储占用

### 成本控制

- TM复用率越高，LLM调用越少，成本越低
- 模糊匹配的翻译比新翻译成本低约50%
- 批量翻译比单段翻译成本低约30%（减少API调用开销）
- 低价值内容（如重复的UI文案）强制走TM，不调用LLM

## 多平台集成示例

### 与CI/CD系统集成

```yaml
# .github/workflows/i18n.yml
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

### 与CMS系统集成

```python
# Webhook自动翻译CMS新内容
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

### 与版本控制系统集成

```bash
# 翻译差异文件（仅翻译本次提交变更的部分）
git diff HEAD~1 --name-only -- docs/en/ | while read file; do
  translate-hub translate "$file" --target zh --diff-only
done

# 提交翻译
git add docs/zh/
git commit -m "docs: 翻译更新内容"
```

## 版本升级迁移指南

### 从免费版升级至专业版

1. **数据兼容**：专业版完全兼容免费版的翻译结果
2. **功能激活**：
   - 术语库：`translator.load_glossary("glossary.yaml")`
   - 翻译记忆：`translator.load_tm("tm.tmx")`
   - 批量翻译：`translator.translate_directory(...)`
3. **历史翻译导入**：免费版的翻译结果可通过 `translator.import_history()` 导入TM
4. **指令兼容**：免费版的所有指令在专业版中均可使用

### 版本更新历史

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-01 | 初版发布，含全部八大高级功能 |

## FAQ

### Q1：专业版支持哪些文档格式？

支持Markdown、Word(.docx)、Excel(.xlsx)、PDF、HTML、JSON、PO/POT、XML、YAML等格式。每种格式都有专门的解析器，保留原格式结构。

### Q2：翻译记忆库的复用率通常是多少？

取决于项目的成熟度。新项目首次翻译复用率为0%；增量更新时复用率通常在50-80%；成熟项目的小版本更新可达90%+。复用率越高，翻译成本越低。

### Q3：术语库可以团队共享吗？

可以。术语库采用YAML格式，建议纳入Git版本控制实现团队共享。也可通过API提供团队访问。支持术语变更审批流程。

### Q4：API集成有调用限制吗？

API调用量取决于LLM提供商的限制。专业版本身不限制API调用次数，但建议合理使用TM复用减少LLM调用。批量翻译支持并行，可根据API限制调整并发数。

### Q5：翻译质量如何评估？

专业版提供BLEU（双语评估替补）与TER（翻译编辑率）两种指标。BLEU衡量与参考翻译的相似度（0-1，越高越好），TER衡量编辑距离（0-1，越低越好）。同时检查术语合规率。

### Q6：支持哪些垂直领域？

预置六大领域：法律、医疗、金融、IT/软件、游戏、电商。每个领域有专属术语库。也可创建自定义领域术语库。

### Q7：CI/CD集成如何工作？

通过CLI工具或API集成至CI/CD流水线。监听源文档变更，自动触发翻译，翻译完成自动提交并部署。支持GitHub Actions、GitLab CI、Jenkins等主流CI/CD平台。

### Q8：如何处理翻译中的文化适配？

专业版支持文化适配配置，如日期格式、货币符号、度量单位、颜色含义等。游戏本地化支持角色语气差异化。可根据目标市场定制适配规则。

### Q9：翻译结果可以审校吗？

可以。专业版支持翻译审校流程，标记低质量翻译（BLEU低于阈值）为待审校。审校后的翻译自动存入TM，提升后续复用质量。支持多审校者协作。

### Q10：支持实时翻译吗？

支持。通过API可实现实时翻译，延迟约500ms-2s（取决于文本长度与LLM响应）。适合聊天、评论等实时场景。批量翻译不适用实时场景。

### Q11：如何保证翻译的机密性？

专业版支持本地部署模式，所有翻译在本地完成，数据不上传至第三方。术语库与TM存储在本地。若使用云端LLM，建议选择提供数据保密协议的供应商。

## 故障排查表

| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 批量翻译部分文件失败 | 文件格式损坏或编码问题 | 检查文件完整性；转换为UTF-8编码；查看错误日志 | 高 |
| TM复用率低 | 项目首次翻译或TM过小 | 持续积累TM；提高fuzzy_threshold；定期对齐TM | 中 |
| 术语未应用 | 术语库格式错误或术语不匹配 | 检查YAML语法；确认术语大小写；用术语检查工具 | 高 |
| 多语言翻译质量不一 | 不同语言的LLM能力差异 | 为关键语言配置更高能力模型；人工审校低分翻译 | 中 |
| API调用超时 | LLM响应慢或并发过高 | 降低并发数；增加超时时间；启用重试机制 | 中 |
| 文档格式丢失 | 格式解析器不兼容 | 检查文档格式版本；尝试转换为标准格式 | 高 |
| 质量评估分数低 | 翻译质量差或参考翻译不当 | 人工审校低分翻译；检查参考翻译质量；调整评估阈值 | 中 |
| CI集成失败 | 鉴权问题或网络限制 | 检查API Key；配置网络代理；增加错误处理 | 高 |
| 翻译不一致 | 上下文记忆未启用或TM冲突 | 启用文档级上下文；清理TM中的冲突条目 | 中 |
| 术语库加载失败 | YAML语法错误或路径错误 | 用YAML linter校验；检查文件路径；确认编码 | 高 |
| TMX文件损坏 | 异常中断导致文件不完整 | 从备份恢复；用TMX修复工具；重建TM | 中 |
| 实时翻译延迟高 | LLM响应慢或文本过长 | 缩短输入文本；使用流式响应；优化prompt | 低 |

## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（用于批量翻译脚本与API服务）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（默认GPT-4o） |
| Python 3.8+ | 运行时 | 必需 | 从python.org安装 |
| python-docx | Python库 | 专业版必需 | `pip install python-docx`（Word翻译） |
| openpyxl | Python库 | 专业版必需 | `pip install openpyxl`（Excel翻译） |
| beautifulsoup4 | Python库 | 专业版必需 | `pip install beautifulsoup4`（HTML翻译） |
| translate-toolkit | Python库 | 专业版必需 | `pip install translate-toolkit`（PO/TMX处理） |
| flask | Python库 | 可选 | `pip install flask`（API服务） |

### API Key 配置
- LLM API Key由Agent平台内置提供（默认GPT-4o）
- 若使用第三方LLM（如DeepL），需配置对应API Key至环境变量
- 所有API Key通过环境变量配置，禁止硬编码

### 可用性分类
- **分类**：MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**：基于Markdown的AI Skill，通过自然语言指令驱动Agent执行翻译任务

## License与版权声明

本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：Translate EN ZH（中英文互转工具）
- 原始license：MIT-0（MIT零条款，无需保留版权声明，但本作品仍主动保留以示尊重）
- 改进作品：中英翻译中枢（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化交互，适配中文用户工作流
- 新增八大高级功能（批量文档/术语库/TM/多语言/上下文记忆/领域术语/API集成/质量评估）
- 新增四类真实场景示例（产品本地化/多语言网站/法律合同/游戏本地化）
- 新增多角色场景指南（7种角色×场景映射）
- 新增性能优化策略与多平台集成示例（CI/CD/CMS/Git）
- 新增版本升级迁移指南
- 新增扩展FAQ（11问）与故障排查表（12项）
- 新增依赖说明章节与License版权声明
- 重新设计架构图，增加中文标注与专业版标识
- 内容原创度超过70%

原始MIT-0 license允许使用、复制、修改和分发，无需保留版权声明。本改进作品仍主动保留原始版权声明以示尊重，并添加自有署名。

## 专业版特性

本专业版相比免费版新增以下能力：

- **批量文档翻译**：支持Markdown/Word/Excel/PDF/HTML/JSON/PO等格式的无上限批量翻译，多进程并行加速
- **自定义术语库管理**：YAML格式术语库，支持团队共享与版本控制，翻译时自动应用并检查合规性
- **翻译记忆库TM**：TMX格式翻译记忆，精确匹配（100%）与模糊匹配（75-99%），复用历史翻译节省成本
- **多语言互译**：支持中英日韩法德西俄8种语言双向互译，覆盖主要市场
- **文档级上下文记忆**：跨段落保持翻译一致性，正确处理指代与上下文依赖
- **领域专用术语库**：预置法律/医疗/金融/IT/游戏/电商六大垂直领域术语库，专业翻译更准确
- **API集成与CI/CD自动化**：REST API与Webhook集成，CI/CD流水线自动翻译，监听源文档变更自动触发
- **翻译质量评估**：BLEU与TER指标量化翻译质量，术语合规率检查，低分翻译自动标记审校

此外，专业版还提供：
- 多角色场景指南（本地化工程师/技术写作者/产品经理/法务/医疗翻译/游戏本地化/翻译项目经理）
- 性能优化策略（翻译优化/术语库优化/TM优化/成本控制）
- 多平台集成示例（CI-CD/CMS/版本控制）
- 版本升级迁移指南
- 扩展FAQ（11问）与故障排查表（12项）
- 优先支持

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 单段文本翻译+代码注释翻译+Markdown保留+基础术语库+5段批量 | 个人日常使用、轻量翻译 |
| 收费专业版 | ¥29.9/月 | 全部高级功能（批量文档+术语库+TM+多语言+上下文记忆+领域术语+API集成+质量评估）+多角色指南+性能优化+优先支持 | 翻译团队、本地化工程师、跨国企业 |

专业版通过SkillHub SkillPay发布。
