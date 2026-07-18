---
slug: skill-writer-tool-pro
name: skill-writer-tool-pro
version: "1.0.0"
displayName: Skill编写工具专业版
summary: 模板库、多人协作、技能质量评估与发布管理，适合技能团队与企业技能生态治理。
license: MIT
edition: pro
description: |-
  Skill编写工具专业版，面向技能团队与企业的高阶技能创建与治理平台。

  核心能力:
  - 技能模板库与分类复用
  - 多人协作编写与审核流程
  - 技能质量评估与评分
  - 发布管理与版本控制
  - 技能生态搜索与发现

  适用场景:
  - 技能团队的标准化技能生产
  - 企业内部技能生态治理
  - 技能市场的内容审核与发布

  差异化: 专业版在免费版核心创建能力之上扩展模板与协作，新增质量评估、发布管理、生态搜索等企业级能力，并与免费版结构规范兼容。

  触发关键词: Skill编写, 模板库, 多人协作, 质量评估, 发布管理, 技能生态, 版本控制, 审核流程
tags:
- Skill编写
- 技能治理
- 团队协作
- 专业版
tools:
- read
- exec
---

# Skill编写工具（专业版）

## 概述

专业版在免费版的 SKILL.md 创建、渐进式展开与资源捆绑之上，扩展为面向技能团队与企业的完整技能治理平台。新增模板库、多人协作、质量评估与发布管理，同时与免费版的结构规范保持向后兼容。

## 核心能力

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 模板库 | 基础模板 | 分类模板库 + 复用 |
| 协作模式 | 个人 | 多人 + 审核 + 评论 |
| 质量评估 | 审查清单 | 自动评分 + 多维评估 |
| 发布管理 | 不支持 | 版本控制 + 发布流程 |
| 生态搜索 | 不支持 | 技能搜索 + 发现 |
| 权限管理 | 不支持 | 角色 + 权限分级 |
| 报告 | 不支持 | 技能统计 + 质量报告 |
| 国际化 | 不支持 | 多语言技能支持 |

## 使用场景

### 场景一：团队标准化技能生产

技能团队按标准流程生产新技能。

```bash
# 创建技能项目（基于模板）
skill-writer-pro create \
  --name "data-validator" \
  --template "utility-skill" \
  --category "数据处理" \
  --team "数据工具组"

# 邀请协作者
skill-writer-pro invite --skill "data-validator" --members "writer-a,reviewer-b"

# 提交审核
skill-writer-pro submit --skill "data-validator" --reviewer "reviewer-b"

# 审核反馈
skill-writer-pro review --skill "data-validator" \
  --status "needs-revision" \
  --comment "触发关键词需补充'校验'与'验证'"

# 输出
# 📊 技能生产流程
# 创建: ✅ 基于模板 utility-skill
# 编写: ✅ v1.0 完成
# 审核: ⚠️ 需修订（触发关键词）
# 发布: ⏳ 待审核通过
```

### 场景二：技能质量评估

对新技能进行多维质量评估。

```bash
# 执行质量评估
skill-writer-pro assess --skill "data-validator"

# 输出
# 📊 技能质量评估报告
# 技能: data-validator
# 版本: v1.0
# 评估维度:
#   - 描述精准度: 92/100
#   - 触发关键词: 78/100 ⚠️
#   - 结构规范: 95/100
#   - 示例完整: 90/100
#   - 文档质量: 88/100
#   - 可维护性: 92/100
# 综合评分: 89.2/100
# 💡 建议: 补充触发关键词'校验'与'验证'
```

### 场景三：技能生态搜索

在技能库中搜索与发现。

```bash
# 搜索技能
skill-writer-pro search --keyword "数据校验" --category "数据处理"

# 输出
# 🔍 技能搜索结果
# 1. data-validator (v1.2) - 数据校验工具
#    评分: 92/100 | 下载: 1,234 | 团队: 数据工具组
# 2. schema-checker (v2.0) - Schema 校验
#    评分: 88/100 | 下载: 856 | 团队: API工具组

# 发现相关技能
skill-writer-pro discover --related-to "data-validator"
```

## 快速开始

```bash
# 1. 初始化专业版工作区
skill-writer-pro init --workspace ~/skill-writer-pro

# 2. 创建技能（基于模板）
skill-writer-pro create --name "my-skill" --template "utility-skill"

# 3. 协作编写
skill-writer-pro invite --skill "my-skill" --members "writer-a"

# 4. 质量评估
skill-writer-pro assess --skill "my-skill"

# 5. 提交审核与发布
skill-writer-pro submit --skill "my-skill"
skill-writer-pro publish --skill "my-skill" --version "1.0.0"

# 6. 搜索与发现
skill-writer-pro search --keyword "工具"
```

## 配置示例

```yaml
# ~/skill-writer-pro/config.yaml
edition: pro
templates:
  path: ~/skill-writer-pro/templates/
  categories:
    - utility-skill
    - integration-skill
    - analysis-skill
    - automation-skill
collaboration:
  enabled: true
  roles: [writer, reviewer, publisher, admin]
  review_required: true
  min_reviewers: 1
assessment:
  dimensions:
    - 描述精准度
    - 触发关键词
    - 结构规范
    - 示例完整
    - 文档质量
    - 可维护性
  threshold: 85
publish:
  version_control: true
  changelog_required: true
  auto_archive: true
search:
  enabled: true
  index_path: ~/skill-writer-pro/index/
  fuzzy_match: true
permissions:
  default: writer
  admin_can_publish: true
report:
  formats: [markdown, json]
  schedule: monthly
```

## 技能模板库

| 模板名 | 适用场景 | 包含内容 |
|:-------|:---------|:---------|
| utility-skill | 通用工具技能 | SKILL.md + scripts/ |
| integration-skill | 集成类技能 | SKILL.md + REFERENCE.md + scripts/ |
| analysis-skill | 分析类技能 | SKILL.md + REFERENCE.md + EXAMPLES.md |
| automation-skill | 自动化技能 | SKILL.md + scripts/ + workflow.yaml |
| documentation-skill | 文档类技能 | SKILL.md + REFERENCE.md |
| custom | 自定义 | 用户定义 |

## 最佳实践

* 新技能优先基于模板创建，确保结构规范。
* 协作场景明确角色分工（编写/审核/发布/管理）。
* 质量评估阈值建议 85 分，低于阈值需修订。
* 触发关键词评估尤为重要，直接影响技能被发现率。
* 发布前必须通过审核，确保质量。
* 版本控制保留变更日志，便于追溯。
* 技能生态搜索定期更新索引，确保发现率。
* 国际化技能注意多语言描述的准确性。

## 常见问题

**Q：专业版与免费版的结构规范兼容吗？**
A：兼容。免费版的所有结构规范在专业版中默认遵循，专业版额外提供模板、协作、评估等能力。

**Q：模板库可以自定义吗？**
A：可以。在 `~/skill-writer-pro/templates/` 目录下添加自定义模板即可。

**Q：协作审核需要多少人？**
A：默认至少 1 名审核者。可通过配置调整最少审核人数。

**Q：质量评估的评分标准是什么？**
A：基于描述精准度、触发关键词、结构规范、示例完整、文档质量、可维护性六维度，权重可配。

**Q：发布的技能可以回滚吗？**
A：可以。专业版支持版本控制，可回滚至历史版本。

**Q：技能搜索支持模糊匹配吗？**
A：支持。搜索索引支持模糊匹配与相关性排序。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（协作与搜索功能需要）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需 | 官方站点下载 |
| Git | 工具 | 可选（版本控制） | 系统自带 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）
- 协作通知若使用 Webhook，需配置 Webhook URL

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + 脚本执行能力）
- **说明**: 专业版在 Markdown 指令基础上，提供模板库、协作审核、质量评估与发布管理能力
