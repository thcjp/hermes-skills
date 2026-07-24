---
slug: "logo-brand-identity"
name: "logo-brand-identity"
version: 1.0.1
displayName: "品牌标识设计专业版"
summary: "企业级AI品牌标识设计系统,支持完整品牌套件、多品牌管理、批量生成、品牌审计与CI/CD集成,适合团队与商业项目"
license: "Proprietary"
edition: "pro"
description: |-
  品牌标识设计专业版为企业与设计团队提供系统化的AI品牌标识设计解决方案。在免费版基础品牌套件能力之上,增加完整品牌系统、多品牌管理、
  批量资产生成、品牌一致性审计与CI/CD集成能力。
tags:
  - 品牌设计
  - 企业级
  - 品牌系统
  - 品牌标识
  - CI/CD
  - 设计管理
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
category: "Automation"
---
# 品牌标识设计专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 品牌标识设计专业版多品牌管理 | 不支持 | 支持 |
| 品牌标识设计专业版批量生成 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |

## 核心能力

### 完整品牌系统
```yaml
# enterprise-brand-system.yml
brand:
  name: "EnterpriseBrand"
  strategy:
    positioning: "行业领先的智能解决方案提供商"
    mission: "用技术赋能每一个团队"
    values: ["创新", "可靠", "协作", "成长"]
    personality: "专业、前瞻、可信、温暖"
# .
  identity:
    logo:
      primary: "assets/logo-primary.svg"
      variations:
        - horizontal
        - stacked
        - icon_only
        - dark_mode
        - monochrome
      clear_space: "logo高度的1/2"
      min_size: "24px digital / 10mm print"
# .
    color_system:
      primary: "#0052FF"
      secondary: "#4D7CFF"
      accent: "#FF6B35"
      neutrals: ["#FAFAFA", "#0F172A", "#F1F5F9", "#E2E8F0"]
      semantic:
        success: "#10B981"
        warning: "#F59E0B"
        error: "#EF4444"
        info: "#3B82F6"
      usage_rules: "主色占比60%,辅助色30%,强调色10%"
# .
    typography:
      display: { family: "Calistoga, serif", sizes: [2, 3, 4, 5] }
      body: { family: "Inter, sans-serif", sizes: [0.875, 1, 1.125] }
      mono: { family: "JetBrains Mono, monospace" }
      hierarchy: "h1-h6明确的字号与字重规范"
# .
    imagery:
      style: "明亮、自然光、真实人物"
      photography: "避免摆拍感,强调真实瞬间"
      illustration: "扁平化、几何、品牌色调"
      iconography: "线描风格,线宽2px"
# .
    voice:
      tone: "专业但平易近人"
      personality: "知识丰富、赋能、前瞻"
      writing_rules: "避免空洞的企业话术,用具体例子说话"
# .
  assets:
    digital:
      - website_header
      - email_signature
      - social_profiles
      - presentation_template
      - email_template
    print:
      - business_card
      - letterhead
      - envelope
      - brochure
      - banner
    motion:
      - intro_animation
      - logo_reveal
      - transition_effects
```

**处理**: 解析完整品牌系统的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回完整品牌系统的处理结果,包含执行状态码、结果数据和执行日志。### 多品牌管理
```python
# 多品牌配置管理
brand_portfolio = {
    "master_brand": {
        "name": "集团主品牌",
        "identity": "master_identity",
        "sub_brands_relationship": "endorsed"  # 背书式
    },
    "sub_brands": [
        {
            "name": "科技子品牌",
            "parent": "master_brand",
            "shared_elements": ["typography", "imagery_style"],
            "unique_elements": ["color_primary", "logo_symbol"],
            "identity": "tech_identity"
        },
        {
            "name": "金融子品牌",
            "parent": "master_brand",
            "shared_elements": ["typography", "logo_structure"],
            "unique_elements": ["color_primary", "imagery_style"],
            "identity": "finance_identity"
        },
        {
            "name": "教育子品牌",
            "parent": "master_brand",
            "shared_elements": ["typography"],
            "unique_elements": ["color_primary", "logo_symbol", "imagery_style"],
            "identity": "education_identity"
        }
    ]
}
# .
# 批量生成所有品牌资产
for brand in brand_portfolio["sub_brands"]:
    generate_brand_system(brand, shared=brand_portfolio["master_brand"])
```

**输入**: 用户提供多品牌管理所需的指令和必要参数。
**处理**: 解析多品牌管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 批量资产生成
```bash
# 批量生成品牌资产
python3 generate_brand_assets.py \
  --brand-config brand-system.yml \
  --assets all \
  --output ./brand-assets/ \
  --formats "svg,png,pdf,ai" \
  --parallel 4 \
  --quality-check
```

```python
# 批量资产生成配置
assets_config = {
    "digital": {
        "website_header": {"formats": ["svg", "png"], "sizes": ["1x", "2x"]},
        "social_profiles": {"platforms": ["twitter", "linkedin", "youtube"]},
        "email_signature": {"formats": ["html", "png"]},
        "presentation": {"template": "powerpoint", "themes": ["light", "dark"]}
    },
    "print": {
        "business_card": {"formats": ["pdf", "ai"], "bleed": "3mm"},
        "letterhead": {"formats": ["pdf", "docx"]},
        "brochure": {"formats": ["pdf"], "pages": 8}
    },
    "motion": {
        "intro_animation": {"format": "mp4", "duration": "3s"},
        "logo_reveal": {"format": "mp4", "duration": "2s"}
    }
}
```

**输入**: 用户提供批量资产生成所需的指令和必要参数。
**处理**: 解析批量资产生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 品牌一致性审计
```python
# 品牌一致性自动审计
brand_audit = {
    "checks": [
        {
            "name": "color_compliance",
            "test": "all_colors_from_palette",
            "scan": ["website", "presentations", "social_media"],
            "action": "report_violations"
        },
        {
            "name": "typography_consistency",
            "test": "font_usage_matches_spec",
            "scan": ["all_digital_assets"],
            "action": "flag_inconsistencies"
        },
        {
            "name": "logo_usage",
            "test": "clear_space_and_min_size",
            "scan": ["all_touchpoints"],
            "action": "report_violations"
        },
        {
            "name": "voice_consistency",
            "test": "tone_matches_guidelines",
            "scan": ["copywriting", "social_posts"],
            "action": "suggest_improvements"
        }
    ],
    "report_format": "html",
    "auto_fix_suggestions": True
}
```

**输入**: 用户提供品牌一致性审计所需的指令和必要参数。
**处理**: 解析品牌一致性审计的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回品牌一致性审计的处理结果,包含执行状态码、结果数据和执行日志。### 品牌策略分析
```python
# 品牌定位与策略分析
brand_strategy = {
    "market_analysis": {
        "competitors": ["竞品A", "竞品B", "竞品C"],
        "differentiation": "我们更注重.",
        "positioning_map": "quality vs price quadrant"
    },
    "audience_personas": [
        {"name": "决策者", "demographics": "35-50岁,高管", "needs": "."},
        {"name": "使用者", "demographics": "25-35岁,专业人士", "needs": "."}
    ],
    "brand_archetype": "智者(The Sage)",
    "value_proposition": ".",
    "brand_story": ""
}
```
#
## 适用场景

### 场景一:企业品牌系统化建设
需求:大型企业需要建立完整的品牌系统,覆盖所有触点。

```bash
# 生成完整企业品牌系统
python3 generate_enterprise_brand.py \
  --config enterprise-brand.yml \
  --strategy-analysis \
  --assets all \
  --guidelines full \
  --output ./enterprise-brand/ \
  --quality-check \
  --audit
```

输出结构:

```
enterprise-brand/
├── strategy/
│   ├── positioning.md
│   ├── personas.md
│   └── competitive-analysis.md
├── identity/
│   ├── logo/
│   ├── colors/
│   ├── typography/
│   └── imagery/
├── assets/
│   ├── digital/
│   ├── print/
│   └── motion/
├── guidelines/
│   ├── brand-guide.pdf
│   ├── usage-rules.md
│   └── dos-and-donts.md
└── audit/
    ├── consistency-report.html
    └── compliance-check.json
```

### 场景二:多品牌集团管理
需求:集团企业需要统一管理多个子品牌,确保一致性又保留个性。

```python
# 多品牌系统生成
group_config = {
    "group_name": "集团品牌",
    "master_identity": load_identity("master.yml"),
    "sub_brands": load_brands("sub-brands.yml"),
    "consistency_rules": {
        "shared": ["typography", "logo_structure"],
        "flexible": ["primary_color", "imagery_style"],
        "strict": ["clear_space", "min_size"]
    }
}
# .
# 批量生成所有品牌系统
generate_brand_portfolio(group_config)
```

### 场景三:品牌焕新项目
需求:传统企业需要品牌形象现代化升级。

```bash
# 品牌焕新工作流
python3 brand_refresh.py \
  --current-brand ./current/ \
  --target-personality "modern,tech,dynamic" \
  --preserve-equity True \
  --generate-migration-guide \
  --output ./refreshed/ \
  --stakeholder-presentation
```

## 使用流程

### 步骤一:品牌策略分析
```bash
python3 analyze_brand.py \
  --company "企业名称" \
  --industry "行业" \
  --competitors "竞品A,竞品B" \
  --output ./strategy/
```

### 步骤二:生成品牌系统
```bash
python3 generate_brand_system.py \
  --config brand-system.yml \
  --assets all \
  --guidelines full \
  --output ./brand/
```

### 步骤三:品牌审计
```bash
python3 audit_brand.py \
  --brand ./brand/ \
  --scan-assets ./assets/ \
  --report ./audit/
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | logo-brand-identity处理的内容输入 |,  |
| content | string | 否 | logo-brand-identity处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "identity 相关配置参数",
    result: "identity 相关配置参数",
    result: "identity 相关配置参数",
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
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md规范的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.10+
- **Node.js**: 18+(用于CI/CD集成)

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| AI图像生成 | 服务 | 必需 | 各AI平台提供 |
| 图像处理库 | 库 | 推荐 | pip install Pillow |
| 矢量化工具 | 库 | 推荐 | pip install potrace |
| 设计工具 | 工具 | 推荐 | Figma / Illustrator |

### API Key 配置
- 本Skill基于指令驱动驱动,无需额外API Key
- AI图像生成服务需按各自平台文档配置
- 批量生成支持API Key池与负载均衡
- 企业版支持多账户管理与并发控制

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令+脚本执行能力)
- **说明**: 专业版基于Markdown指令驱动Agent执行企业级品牌标识设计任务,通过Python脚本实现批量生成、品牌审计与CI/CD集成
- **PRO版增强**: 完整品牌系统、多品牌管理、批量生成、品牌审计、策略分析、CI/CD集成、团队协作

## 案例展示

### 品牌指南文档结构
```markdown
# 品牌指南 - [品牌名称]
# .
## 常见问题
# .
### Q1: 如何从免费版迁移至PRO版?
A: PRO版完全兼容免费版。现有品牌简介与配置可直接使用。运行迁移脚本将免费版资产升级为完整品牌系统:
# .
```bash
python3 migrate.py --from free --to pro --upgrade-assets
```
# .
### Q2: 多品牌如何确保一致性?
A: PRO版提供"一致性规则"配置,指定哪些元素必须共享(如字体、Logo结构),哪些可以灵活调整(如主色、图像风格)。系统自动验证规则遵守情况。
# .
### Q3: 品牌审计能检测哪些问题?
A: 可检测:颜色未使用品牌色、字体不符合规范、Logo使用不当(清晰空间不足、尺寸过小)、文案语调偏离品牌个性等。生成详细报告并提供修复建议。
# .
### Q4: 支持哪些输出格式?
A: 数字资产:SVG、PNG、HTML、PPTX。印刷资产:PDF、AI、EPS。动态资产:MP4、GIF。可根据使用场景自动选择优秀格式。
# .
### Q5: 如何管理品牌资产的版本?
A: PRO版支持语义化版本控制,每次品牌变更自动生成变更日志。可集成Git进行团队协作,支持品牌资产的审批与发布流程。
# .
## 错误处理
# .
# .
| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# .
# .