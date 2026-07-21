---
slug: skill-creator
name: skill-creator
version: "1.0.0"
displayName: AI技能创建指南
summary: 创建有效AI Skill的完整指南，覆盖frontmatter、SKILL.md结构与Progressive Disclosure设计原则
license: Proprietary
description: |-
  创建有效AI Skill的完整指南，基于Core Principles与Anatomy of a Skill规范。
  覆盖frontmatter编写、SKILL.md结构设计、Bundled Resources（scripts/references/assets）组织，
  以及Progressive Disclosure三级加载体系。支持从需求理解到skill打包的完整创建流程。
  适用于独立开发者、企业团队构建专属AI技能与自动化工作流。
tools:
  - read
  - exec
---

# AI技能创建指南

创建有效AI Skill的完整指南，覆盖从需求理解到skill打包的完整流程，基于Core Principles与Progressive Disclosure设计原则。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（用于运行init_skill.py与package_skill.py）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 用于执行skill初始化与打包脚本 |
| Bash/Shell | 运行时 | 可选 | 用于测试skill中的脚本 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行skill创建任务

## 核心能力

### Core Principles指导

提供skill创建的三大核心原则指导：

- **Concise is Key**：context window是公共资源，skill仅添加Claude不具备的知识。默认假设"Claude already is very smart"，对每段内容质疑"Does Claude really need this explanation?"与"Does this paragraph justify its token cost?"。优先用简洁examples替代冗长explanations。
- **Set Appropriate Degrees of Freedom**：根据任务的fragility和variability匹配specificity级别
  - High freedom（text-based instructions）：多种方法valid、决策依赖context时使用
  - Medium freedom（pseudocode or scripts with parameters）：有preferred pattern但允许variation时使用
  - Low freedom（specific scripts, few parameters）：操作fragile且error-prone、consistency关键时使用
- **Anatomy of a Skill**：每个skill由required的SKILL.md与optional的Bundled Resources组成

### SKILL.md结构设计
提供SKILL.md的标准结构与编写规范：

```text
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation intended to be loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

- **Frontmatter（YAML）**：包含`name`和`description`字段。这是Claude读取以判断何时使用skill的唯一依据，必须清晰全面地描述skill是什么以及何时使用。`description`是primary triggering mechanism，应包含skill做什么与具体触发场景。
- **Body（Markdown）**：使用skill的instructions和guidance。仅在skill触发后加载。

**处理**: 按照skill规范执行SKILL.md结构设计操作,遵循单一意图原则。
### Bundled Resources组织

提供三类bundled resources的组织规范：

- **Scripts（`scripts/`）**：Executable code用于需要deterministic reliability或反复重写的任务
  - 包含时机：同一代码被反复重写或需要deterministic reliability时
  - 示例：`scripts/rotate_pdf.py`
  - 优势：Token efficient、deterministic、可不加载入context即执行
- **References（`references/`）**：按需加载的文档与参考材料
  - 包含时机：Claude工作时需参考的文档
  - 示例：`references/finance.md`、`references/api_docs.md`
  - 最佳实践：大文件（>10k words）在SKILL.md中包含grep search patterns
  - 避免重复：信息只存在于SKILL.md或references之一
- **Assets（`assets/`）**：用于输出而非加载入context的文件
  - 包含时机：skill需要用于最终输出的文件
  - 示例：`assets/logo.png`、`assets/slides.pptx`、`assets/frontend-template/`

### Progressive Disclosure设计
提供三级加载系统的设计原则与三种Patterns：

- **Level 1 - Metadata（name + description）**：始终在context中（约100 words）
- **Level 2 - SKILL.md body**：skill触发时加载（<5k words）
- **Level 3 - Bundled resources**：Claude按需加载（Unlimited，因scripts可不读入context即执行）

保持SKILL.md body在essentials以内且<500 lines，接近限制时拆分内容。三种Patterns：

- **Pattern 1: High-level guide with references**：SKILL.md保留核心workflow，variant-specific details移至reference files
- **Pattern 2: Domain-specific organization**：多领域skill按domain组织references目录
- **Pattern 3: Conditional details**：展示基础内容，链接高级内容

重要准则：references保持一级深度；长reference文件（>100 lines）顶部包含table of contents。

**输出**: 返回Progressive Disclosure设计的执行结果,包含操作状态和输出数据。
### Skill Creation Process

提供从理解到迭代的六步创建流程：

1. **Understand the skill with concrete examples**：通过直接user examples或generated examples理解skill用法
2. **Plan reusable skill contents**：分析每个example，识别reusable的scripts、references、assets
3. **Initialize the skill**：运行`scripts/init_skill.py <skill-name> --path <output-directory>`生成模板
4. **Edit the skill**：实现resources并编写SKILL.md，使用imperative/infinitive form
5. **Package the skill**：运行`scripts/package_skill.py <path/to/skill-folder>`验证并打包为.skill文件
6. **Iterate based on real usage**：实际使用后识别struggles或inefficiencies并改进

### 不应包含的内容

明确skill应避免的extraneous文件：

- 不创建README.md、INSTALLATION_GUIDE.md、QUICK_REFERENCE.md、CHANGELOG.md等
- skill仅包含AI agent执行任务所需的essential files
- 不包含创建过程的auxiliary context、setup/testing procedures、user-facing documentation

### 能力覆盖范围

本skill还覆盖以下能力场景: 创建有效、的完整指南、三级加载体系、支持从需求理解到、打包的完整创建流、适用于独立开发者、企业团队构建专属、技能与自动化工作。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

1. **理解需求**：通过concrete examples明确skill应支持的功能与触发场景
2. **规划资源**：分析examples，列出reusable的scripts、references、assets清单
3. **初始化skill**：运行`scripts/init_skill.py`生成模板目录结构
4. **编辑skill**：从reusable resources开始实现，编写SKILL.md frontmatter（name + description）与body
5. **测试脚本**：实际运行添加的scripts，确保无bug且输出符合预期
6. **打包skill**：运行`scripts/package_skill.py`自动验证并打包为.skill文件
7. **迭代优化**：实际使用后识别改进点并更新

### 命令参数说明

- `-query-skill`: 命令参数,用于指定操作选项

## 示例

### 示例1：创建pdf-editor skill

```
需求: 用户频繁请求"帮我旋转这个PDF"
Step 1 - Understand:
  - 功能: PDF旋转
  - 触发: "rotate this PDF"、"rotate PDF"
Step 2 - Plan:
  - 分析: 旋转PDF每次都需重写相同代码
  - 资源: scripts/rotate_pdf.py
Step 3 - Init:
  $ scripts/init_skill.py pdf-editor --path ./skills
Step 4 - Edit:
  - 实现 scripts/rotate_pdf.py 并测试
  - 编写 SKILL.md frontmatter:
    name: pdf-editor
    description: "PDF manipulation toolkit. Use when user needs to rotate, split, merge PDFs..."
  - 编写 body 使用说明
Step 5 - Package:
  $ scripts/package_skill.py ./skills/pdf-editor
  → 生成 pdf-editor.skill
```

### 示例2：创建big-query skill（Progressive Disclosure实践）

```
需求: 用户查询BigQuery数据，需反复发现schema
Step 1 - Understand:
  - 功能: 查询BigQuery
  - 触发: "how many users logged in today?"
Step 2 - Plan:
  - 分析: 每次查询需重新发现table schemas
  - 资源: references/schema.md
Step 3 - 应用 Pattern 2 (Domain-specific organization):
  big-query-skill/
  ├── SKILL.md (overview and navigation)
  └── references/
      ├── finance.md (revenue, billing metrics)
      ├── sales.md (opportunities, pipeline)
      ├── product.md (API usage, features)
      └── marketing.md (campaigns, attribution)
Step 4 - Edit:
  - SKILL.md 仅包含核心workflow与各reference的导航说明
  - 用户问sales metrics时，Claude仅读取sales.md
Step 5 - Validate:
  - 确认SKILL.md <500 lines
  - 确认frontmatter的description含触发信息
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| init_skill.py执行失败 | Python版本不兼容或路径不存在 | 确认Python 3.8+，检查`--path`目录存在且有写权限 |
| frontmatter格式错误 | YAML缩进或字段缺失 | 确保`name`和`description`字段存在且格式正确，description不为空 |
| package_skill.py验证失败 | SKILL.md超限或reference缺失 | 检查SKILL.md是否<500 lines，确认所有reference路径有效 |
| skill未触发 | description缺少触发信息 | 在description中补充"when to use"信息与具体触发场景 |
| scripts运行出错 | 脚本依赖缺失或路径错误 | 实际运行scripts测试，确认依赖安装且使用绝对路径 |
| context window溢出 | SKILL.md过长或未使用Progressive Disclosure | 将detailed info移至references/，保持SKILL.md <5k words |
| Bundled Resources重复 | 信息同时存在于SKILL.md和references | 信息只存在于一处，detailed info优先放references |

## 常见问题

### Q1: description应该包含哪些内容？
A: description是skill的primary triggering mechanism，必须包含：skill做什么、具体的触发场景（when to use）。不应在body中放"When to Use"sections，因为body仅在触发后加载。示例："Comprehensive document creation... Use when Claude needs to work with professional documents (.docx files) for: (1) Creating new documents, (2) Modifying content..."

### Q2: 何时应该使用scripts而非inline code？
A: 当同一代码被反复重写（repeatedly rewritten）或需要deterministic reliability时使用scripts。scripts的优势是token efficient、deterministic、可不加载入context即执行。注意scripts仍可能需被Claude读取以进行patching或environment-specific adjustments。

### Q3: Progressive Disclosure的三个层级如何划分？
A: Level 1是Metadata（name + description），始终在context（约100 words）；Level 2是SKILL.md body，skill触发时加载（<5k words）；Level 3是Bundled resources，Claude按需加载（unlimited，因scripts可执行不读入context）。

### Q4: references文件应该多大？
A: 大文件（>10k words）应在SKILL.md中包含grep search patterns。长reference文件（>100 lines）顶部应包含table of contents。references保持一级深度（one level deep from SKILL.md），所有reference文件直接从SKILL.md链接。

### Q5: init_skill.py和package_skill.py如何使用？
A: 初始化：`scripts/init_skill.py <skill-name> --path <output-directory>`，生成含SKILL.md模板和scripts/references/assets目录的skill。打包：`scripts/package_skill.py <path/to/skill-folder> [./dist]`，自动验证frontmatter、命名规范、description质量后打包为.skill文件（zip格式）。

### Q6: 如何判断应该使用High/Medium/Low freedom？
A: High freedom（text-based）适用于多种方法valid、决策依赖context；Medium freedom（pseudocode/参数化scripts）适用于有preferred pattern但允许variation；Low freedom（specific scripts）适用于操作fragile且error-prone、consistency关键。类比：narrow bridge with cliffs需specific guardrails（low freedom），open field允许many routes（high freedom）。

## 已知限制

- 需要Python 3.8+环境运行init_skill.py与package_skill.py
- 依赖用户提供准确的concrete examples以理解skill需求
- scripts需实际运行测试，无法自动验证所有edge cases
- SKILL.md的<500 lines限制对于复杂skill可能需要大量内容拆分
- Progressive Disclosure的Pattern选择需人工判断，无自动推荐机制
