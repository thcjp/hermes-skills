---
slug: "translate-hub"
name: "translate-hub"
version: 1.0.1
displayName: "中英翻译中枢(专业版)"
summary: "企业级多语言翻译专业版，支持批量文档翻译、自定义术语库、翻译记忆库、多语言互译与API集成，覆盖本地化全流程。"
license: "MIT"
edition: "pro"
description: |-
  中英翻译中枢（专业版）面向翻译团队、本地化工程师与跨国企业，在免费版基础上解锁全部高级能力：无上限批量文档翻译、自定义术语库与团队共享、翻译记忆库（TM）复用历史翻译、多语言互译（中英日韩法德西俄）、文档级上下文记忆、API集成与CI/CD自动化、垂直领域专用术语库。覆盖从单段翻译到企业级本地化流水线的完整工作流
tags:
  - 翻译工具
  - 多语言
  - 本地化
  - 翻译记忆库
  - 术语管理
  - 翻译
  - 语言
  - 工具
  - translator
  - 用户提供
  - 所需的指
tools:
  - read
  - exec
  - write
homepage: ""
category: "Knowledge"
---
# 中英翻译中枢(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |
| 数据质量检测与清洗规则 | 不支持 | 支持 |

## 核心能力

### 1. 批量文档翻译（专业版独有）
支持多种文档格式的批量翻译，无上限：

```python
from translate_hub_pro import BatchTranslator
# ...
translator = BatchTranslator()
# ...
results = translator.translate_directory(
    source_dir="./docs/en/",
    target_dir="./docs/zh/",
    source_lang="en",
    target_lang="zh",
    formats=["md", "docx", "xlsx", "pdf", "html", "json", "po"],
    parallel=4  # 4进程并行
)
# ...
```

| 格式 | 处理方式 | 适用场景 |
|:-----|:-----|:-----|
| Markdown | 保留格式，翻译正文 | 技术文档、README |
| Word(.docx) | 保留样式，翻译内容 | 合同、报告 |
| Excel(.xlsx) | 按单元格翻译，保留公式 | 报价单、数据表 |
| PDF | 提取文本翻译，重新排版 | 宣传册、白皮书 |
| HTML | 保留标签，翻译可见文本 | 网站内容 |
| JSON | 翻译value，保留key | i18n资源文件 |
| PO/POT | 翻译msgid对应的msgstr | GNU gettext国际化 |

**输入**: 用户提供批量文档翻译（专业版独有）所需的指令和必要参数.
### 2. 自定义术语库管理（专业版独有）
通过YAML格式管理术语库，支持团队共享与版本控制：

> 详细代码示例已移至 `references/detail.md`

```python
translator.load_glossary("glossary.yaml")
# ...
text = "Configure the Dashboard and API Gateway in your Workspace."
result = translator.translate(text, source="en", target="zh")
```

**输入**: 用户提供自定义术语库管理（专业版独有）所需的指令和必要参数.
**处理**: 解析自定义术语库管理（专业版独有）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 3. 翻译记忆库TM（专业版独有）
复用历史翻译，提升一致性与效率：

```python
translator.load_tm("translation_memory.tmx")
# ...
result = translator.translate("Click the button to save changes.", source="en", target="zh")
translator.save_tm("translation_memory.tmx")
```

| 匹配类型 | 匹配度 | 处理方式 |
|---:|---:|---:|
| 精确匹配 | 100% | 直接复用，无需重新翻译 |
| 模糊匹配 | 75-99% | 复用并微调（如数字、标点差异） |
| 新翻译 | <75% | 调用LLM翻译，并存入记忆库 |

**输入**: 用户提供翻译记忆库TM（专业版独有）所需的指令和必要参数.
### 4. 多语言互译（专业版独有）
支持8种语言的双向互译：

| 语言 | 代码 | 支持方向 |
|:---:|:---:|:---:|
| 中文 | zh | ↔ 所有语言 |
| 英文 | en | ↔ 所有语言 |
| 日文 | ja | ↔ 中/英 |
| 韩文 | ko | ↔ 中/英 |
| 法文 | fr | ↔ 中/英 |
| 德文 | de | ↔ 中/英 |
| 西班牙文 | es | ↔ 中/英 |
| 俄文 | ru | ↔ 中/英 |

```python
texts = {
    "en": "Welcome to our platform",
    "ja": "プラットフォームへようこそ",
    "ko": "우리 플랫폼에 오신 것을 환영합니다",
    "fr": "Bienvenue sur notre plateforme"
}
# ...
for lang, text in texts.items():
    result = translator.translate(text, source=lang, target="zh")
    print(f"{lang} → zh: {result}")
```

**输入**: 用户提供多语言互译（专业版独有）所需的指令和必要参数.
**处理**: 解析多语言互译（专业版独有）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 5. 文档级上下文记忆（专业版独有）
跨段落保持翻译一致性，理解文档全局上下文：

```python
result = translator.translate_document(
    "agent_doc.md",
    source="en",
    target="zh",
    context_aware=True  # 启用文档级上下文
)
```

**输入**: 用户提供文档级上下文记忆（专业版独有）所需的指令和必要参数.
**处理**: 解析文档级上下文记忆（专业版独有）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `文档级上下文记忆（专业版独有）` 选项

### 6. 领域专用术语库（专业版独有）
预置六大垂直领域的专用术语库：

| 领域 | 术语量 | 适用场景 |
|:------|------:|:------|
| 法律 | 5000+ | 合同、协议、判决书、法律意见书 |
| 医疗 | 8000+ | 病历、药品说明、临床报告、医学文献 |
| 金融 | 4000+ | 财报、招股书、研究报告、监管文件 |
| IT/软件 | 6000+ | 技术文档、API文档、产品手册 |
| 游戏 | 3000+ | 游戏UI、剧情、道具、技能描述 |
| 电商 | 2000+ | 商品描述、营销文案、退换货政策 |

```python
translator.load_domain("legal")  # 法律领域
translator.load_domain("medical")  # 医疗领域（可叠加）
legal_text = "The parties hereto agree to the terms and conditions set forth herein."
result = translator.translate(legal_text, source="en", target="zh")
```

**输入**: 用户提供领域专用术语库（专业版独有）所需的指令和必要参数.
**处理**: 解析领域专用术语库（专业版独有）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输入**: 用户提供API集成与CI/CD自动化（专业版独有）所需的指令和必要参数.
**处理**: 解析API集成与CI/CD自动化（专业版独有）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回API集成与CI/CD自动化（专业版独有）的处理结果,包含执行状态码、结果数据和执行日志.
### 8. 翻译质量评估（专业版独有）
```python
evaluation = translator.evaluate(
    source="The system will be deployed tomorrow.",
    translation="系统将于明天部署。",
    reference="系统将于明日部署。"  # 参考翻译（可选）
)
# ...
```

**输入**: 用户提供翻译质量评估（专业版独有）所需的指令和必要参数.
**处理**: 解析翻译质量评估（专业版独有）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回翻译质量评估（专业版独有）的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：软件产品本地化（本地化工程师角色）
**场景描述**：SaaS产品要进入中国市场，需将全套产品文档（用户手册、API文档、帮助中心、UI文案）从英文翻译为中文，总量约10万字，需在2周内完成并保证术语一致.
**配置**：
```yaml
project:
  name: SaaS Localization CN
  glossary: product_glossary.yaml
  tm: product_tm.tmx
  domain: it
# ...
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

**效果**：10万字本地化从约3周（人工）缩短至2天（自动），术语一致性100%，TM复用率65%节省成本，质量评估BLEU均分0.82.
### 场景二：多语言网站内容管理（产品经理角色）
**场景描述**：产品官网需支持8种语言，每次产品更新都需同步翻译新增内容到8种语言，人工翻译周期长且成本高.
**配置**：
```yaml
project:
  name: Website Localization
  languages: [zh, ja, ko, fr, de, es, ru]
  ci_integration: true
# ...
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

**效果**：多语言同步周期从约5天缩短至2小时，翻译成本降低约70%（TM复用），内容一致性保证.
### 场景三：法律合同翻译（法务角色）
**场景描述**：法务部门需将英文合同翻译为中文，法律术语要求严谨准确，且同一术语在整份合同中必须完全一致.
**配置**：
```python
translator = Translator()
translator.load_domain("legal")  # 法律领域术语库
translator.load_glossary("contract_glossary.yaml")  # 合同专属术语
translator.enable_strict_consistency()  # 严格一致性模式
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

**效果**：50页合同翻译从约5天（人工）缩短至4小时，术语一致性100%，存疑标记减少约80%的人工审校工作量.
### 场景四：游戏本地化（游戏本地化角色）
**场景描述**：游戏要进入日本和韩国市场，需将游戏剧情、UI、道具描述、技能说明从中文翻译为日文和韩文，要求符合当地游戏表达习惯.
**配置**：
```yaml
project:
  name: Game Localization JP/KR
  languages: [ja, ko]
  domain: game
# ...
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

**效果**：游戏本地化周期从约2个月缩短至2周，玩家满意度提升约30%，角色语气一致性保证.
## 使用流程

### 基础搭建（<60秒）
单段文本翻译（与免费版一致，但启用术语库与TM）：

```python
from translate_hub_pro import Translator
# ...
translator = Translator()
translator.load_glossary("glossary.yaml")
translator.load_tm("translation_memory.tmx")
# ...
result = translator.translate("Deploy the service to production.", source="en", target="zh")
print(result.translation)  # "将服务部署至生产环境。"
```

### 标准搭建（<120秒）
批量文档翻译+术语库+TM：

> 详细内容已移至 `references/detail.md` - ### 完整搭建（<300秒）

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|:---|---:|---:|
| content | string | 否 | translate-hub处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 问题 | 可能原因 | 解决方案 | 优先级 |
|:------:|--------|:-------|:------:|
| 批量翻译部分文件失败 | 文件格式损坏或编码问题 | 检查文件完整性；转换为UTF-8编码；查看错误日志 | 高 |
| TM复用率低 | 项目首次翻译或TM过小 | 持续积累TM；提高fuzzy_threshold；定期对齐TM | 中 |
| 术语未应用 | 术语库格式错误或术语不匹配 | 检查YAML语法；确认术语大小写；用术语检查工具 | 高 |
| 多语言翻译质量不一 | 不同语言的LLM能力差异 | 为关键语言配置更高能力模型；人工审校低分翻译 | 中 |
| API调用超时 | LLM响应慢或并发过高 | 降低并发数；增加超时时间；启用机制 | 中 |
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

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|----|:--:|---:|----|
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
- **分类**：MD+EXEC（）
- **说明**：基于Markdown的AI Skill，通过自然语言指令驱动Agent执行翻译任务

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100
# ...
检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100
# ...
检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100
# ...
检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过
# ...
改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1：专业版支持哪些文档格式？
支持Markdown、Word(.docx)、Excel(.xlsx)、PDF、HTML、JSON、PO/POT、XML、YAML等格式。每种格式都有专门的解析器，保留原格式结构.
### Q2：翻译记忆库的复用率通常是多少？
取决于项目的成熟度。新项目首次翻译复用率为0%；增量更新时复用率通常在50-80%；成熟项目的小版本更新可达90%+。复用率越高，翻译成本越低.
### Q3：术语库可以团队共享吗？
可以。术语库采用YAML格式，建议纳入Git版本控制实现团队共享。也可通过API提供团队访问。支持术语变更审批流程.
### 错误恢复步骤
| 错误场景 | 原因 | 处理方式 |
|----|----|----|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制
API调用量取决于LLM提供商的限制。专业版本身不限制API调用次数，但建议合理使用TM复用减少LLM调用。批量翻译支持并行，可根据API限制调整并发数.
### Q5：翻译质量如何评估？
专业版提供BLEU（双语评估替补）与TER（翻译编辑率）两种指标。BLEU衡量与参考翻译的相似度（0-1，越高越好），TER衡量编辑距离（0-1，越低越好）。同时检查术语合规率.
### Q6：支持哪些垂直领域？
预置六大领域：法律、医疗、金融、IT/软件、游戏、电商。每个领域有专属术语库。也可创建自定义领域术语库.
### Q7：CI/CD集成如何工作？
通过CLI工具或API集成至CI/CD流水线。监听源文档变更，自动触发翻译，翻译完成自动提交并部署。支持GitHub Actions、GitLab CI、Jenkins等主流CI/CD平台.
### Q8：如何处理翻译中的文化适配？
专业版支持文化适配配置，如日期格式、货币符号、度量单位、颜色含义等。游戏本地化支持角色语气差异化。可根据目标市场定制适配规则.
### Q9：翻译结果可以审校吗？
可以。专业版支持翻译审校流程，标记低质量翻译（BLEU低于阈值）为待审校。审校后的翻译自动存入TM，提升后续复用质量。支持多审校者协作.
### Q10：支持实时翻译吗？
支持。通过API可实现实时翻译，延迟约500ms-2s（取决于文本长度与LLM响应）。适合聊天、评论等实时场景。批量翻译不适用实时场景.
### Q11：如何保证翻译的机密性？
专业版支持本地部署模式，所有翻译在本地完成，数据不上传至第三方。术语库与TM存储在本地。若使用云端LLM，建议选择提供数据保密协议的供应商.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:--------|:--------|:--------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 文档处理依赖原文件的格式规范性与完整性
- 免费版不支持OCR识别与复杂排版还原
