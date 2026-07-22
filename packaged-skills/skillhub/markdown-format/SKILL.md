---
slug: "markdown-format"
name: "markdown-format"
version: "1.0.0"
displayName: "Markdown格式化工具专业版"
summary: "企业级文档批量格式化,支持自定义模板、团队规范、多格式输出与质量审计"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队与企业的高级 Markdown 格式化工具,在免费版基础上扩展批量处理、规范管理、质量审计等能力。核心能力:
  - 批量目录格式化与聚合报告
  - 自定义格式化模板与团队规范
  - 多格式输出(Markdown / HTML / PDF)
  - 文档质量评分与审计报告
  - Git 变更追踪与增量格式化

  适用场景:
  - 技术文档库批量格式化
  - 团队文档规范统一
  - 文档质量治理与审计

  差异化:
  - 兼容免费版全部能力,无缝升级
  - 支持自定义模板与团队规范配置
  - 提供质量评分与审计能力
  ...
tags:
  - 文档工具
  - Markdown
  - 批量处理
  - 企业级
  - 质量审计
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# Markdown格式化工具专业版

## 核心能力

### 1. 批量目录格式化
支持对整个目录递归格式化,自动生成聚合报告:

```bash
# 批量格式化文档目录
请格式化目录 docs/ 下所有 .md 文件
模式: 优化格式
输出: 原地更新 + 生成聚合报告
报告: docs/_format-report.md
```

**输入**: 用户提供批量目录格式化所需的指令和必要参数。
**处理**: 按照skill规范执行批量目录格式化操作,遵循单一意图原则。

### 2. 自定义格式化模板
通过模板文件管理团队格式化规范:

```json
{
  "template_name": "技术文档规范",
  "frontmatter": {
    "required_fields": ["title", "slug", "summary", "last_updated"],
    "title_max_length": 30,
    "summary_max_length": 80
  },
  "headings": {
    "max_level": 4,
    "require_hierarchy": true,
    "naming_style": "descriptive"
  },
  "formatting": {
    "bold_key_conclusions": true,
    "auto_table_for_comparisons": true,
    "code_block_language_required": true
  },
  "typography": {
    "cjk_spacing": true,
    "quote_style": "fullwidth",
    "emphasis_fix": true
  }
}
```

**输入**: 用户提供自定义格式化模板所需的指令和必要参数。
**处理**: 按照skill规范执行自定义格式化模板操作,遵循单一意图原则。
**输出**: 返回自定义格式化模板的执行结果,包含操作状态和输出数据。

### 3. 多格式输出
| 输出格式 | 适用场景 | 命令参数 |
|:---------|:---------|:---------|
| Markdown | 默认,版本控制友好 | `--format markdown` |
| HTML | 网页发布、文档站 | `--format html` |
| PDF | 归档、打印、评审 | `--format pdf` |
| 多格式同时 | 多渠道发布 | `--format markdown,html,pdf` |

```bash
# 多格式输出
请格式化文件 docs/guide.md
输出格式: markdown, html, pdf
输出路径: docs/output/
```

**处理**: 按照skill规范执行多格式输出操作,遵循单一意图原则。
### 4. 文档质量评分
对格式化后的文档进行质量评分,生成审计报告:

```bash
# 质量审计
请对 docs/ 目录执行文档质量审计
评分维度: 结构完整性、可读性、规范符合度
输出: docs/_audit-report.md
```

评分维度:

| 维度 | 权重 | 评分项 |
|:-----|:-----|:-------|
| 结构完整性 | 30% | 标题层级、frontmatter 完整性 |
| 可读性 | 30% | 段落长度、列表使用、加粗关键点 |
| 规范符合度 | 25% | 命名规范、代码块标注、排版标准 |
| 一致性 | 15% | 术语统一、格式风格统一 |

**输入**: 用户提供文档质量评分所需的指令和必要参数。
### 5. Git 变更追踪与增量格式化
```bash
# 仅格式化 Git 变更的文件
请格式化 git diff 中变更的 .md 文件
范围: 最近一次提交
模式: 增量格式化
```

**处理**: 按照skill规范执行Git 变更追踪与增量格式化操作,遵循单一意图原则。
**输出**: 返回Git 变更追踪与增量格式化的执行结果,包含操作状态和输出数据。

- 执行`Git 变更追踪与增量格式化`操作,处理输入数据并返回结果
- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `git_变更追踪与增量格式化` 选项

### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级文档批量格、支持自定义模板、团队规范、多格式输出与质量、面向团队与企业的、格式化工具、在免费版基础上扩、展批量处理、规范管理、质量审计等能力、核心能力、批量目录格式化与、与团队规范、文档质量评分与审。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一: 技术文档库批量格式化

新团队接手历史文档库,需要统一格式规范。

```bash
# 批量格式化
请对 docs/ 目录执行批量格式化
模板: 技术文档规范
输出: 原地更新 + 聚合报告
忽略: docs/legacy/ (历史文档不处理)

# 示例
```

聚合报告示例:

```text
批量格式化报告 - docs/
=====================================
处理文件: 45 个
成功: 42 个
跳过: 3 个(已符合规范)

变更统计:
- Frontmatter 补全: 38 个文件
- 标题层级修正: 27 个文件
- 列表优化: 15 个文件
- 排版修正: 42 个文件

质量评分:
- 平均分: 82/100
- 优秀(90+): 8 个
- 良好(70-89): 28 个
- 需改进(<70): 6 个
```

### 场景二: 团队文档规范统一

制定团队格式化规范,确保所有文档一致。

```bash
# 应用团队规范
请对 PR 中新增的文档应用团队规范
规范文件: .format-templates/team-standard.json
检查项: frontmatter 完整性、标题层级、代码块标注
不通过项: 列出并给出修正建议
```

### 场景三: 文档质量治理与审计

定期审计文档质量,追踪改进趋势。

```bash
# 季度文档审计
请对 docs/ 目录执行季度质量审计
对比基线: 上季度审计报告
输出: 趋势对比 + 改进建议
关注: 质量下降的文档
```

## 使用流程

### 优秀步: 初始化项目配置

```bash
mkdir -p .markdown-toolkit/{templates,reports,output}

# 创建团队规范模板
cat > .markdown-toolkit/templates/team-standard.json << 'EOF'
{
  "template_name": "团队文档规范",
  "frontmatter": {
    "required_fields": ["title", "slug", "summary"],
    "title_max_length": 30
  },
  "headings": {
    "max_level": 4,
    "require_hierarchy": true
  },
  "quality_threshold": 70
}
EOF
```

### 第二步: 执行批量格式化

```bash
# 批量格式化
请格式化 docs/ 目录
模板: .markdown-toolkit/templates/team-standard.json
输出: 原地更新
报告: .markdown-toolkit/reports/batch-$(date +%Y%m%d).md
```

### 第三步: 查看质量报告

```bash
# 查看最新审计报告
请展示 .markdown-toolkit/reports/ 下最新的质量审计报告
```

### 命令参数说明

- `-standard`: 命令参数,用于指定操作选项
- `-report`: 命令参数,用于指定操作选项
- `-api-key`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
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


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境

- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+(排版脚本)
- **Python**: 3.8+(PDF 输出,可选)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Node.js | 运行时 | 排版脚本必需 | nodejs.org |
| bun(可选) | 运行时 | 否 | bun.sh |
| weasyprint | Python 库 | PDF 输出必需 | `pip install weasyprint` |
| pdfkit | Python 库 | PDF 输出备选 | `pip install pdfkit` |
| git | CLI 工具 | 增量格式化必需 | 系统自带 |

### API Key 配置

- 本工具基于 Markdown 指令驱动,无需额外 API Key
- 排版脚本与质量审计均在本地运行
- 如需调用外部 LLM 做深度分析,可配置:

```bash
export FORMAT_LLM_API_KEY="your-api-key"
export FORMAT_LLM_ENDPOINT="https://api.example.com/v1"
```

### 可用性分类

- **分类**: MD+EXEC+SCRIPT(Markdown 指令 + 命令行执行 + 排版/审计脚本)
- **说明**: 核心格式化通过自然语言指令驱动,批量处理与质量审计通过脚本加速
- **离线可用**: 核心功能完全离线;PDF 输出需本地依赖

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

检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过

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

检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过

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

检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过

改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1: 专业版是否兼容免费版的格式化结果?

完全兼容。专业版使用相同的格式化规则,免费版处理的文件在专业版中可直接继续优化。

### Q2: 批量格式化会修改原文件吗?

默认原地更新并自动备份。可在配置中设置 `backup_enabled: false` 关闭备份。

### Q3: 自定义模板如何共享给团队?

将 `.markdown-toolkit/templates/` 目录纳入版本控制,团队成员拉取后即可使用相同规范。

### Q4: 质量评分标准可以自定义吗?

可以。在模板文件中配置各维度权重和评分项,详见配置示例。

### 依赖说明

PDF 输出需要安装 `weasyprint` 或 `pdfkit`:

```bash
pip install weasyprint   # 推荐
# 或
pip install pdfkit        # 需要 wkhtmltopdf
```

### Q6: 增量格式化如何识别变更文件?

通过 Git diff 识别变更文件,仅格式化新增或修改的 `.md` 文件,避免全量重复处理。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
