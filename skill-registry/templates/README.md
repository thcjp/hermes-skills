# Skill 设计模式模板库

> **版本**: v1.0
> **创建时间**: 2026-07-20
> **基于**: SKILL_QUALITY_STANDARD.md v3.0 + TRACE评测体系 + 5种设计模式

---

## 一、模板选型指南

根据用户需求选择对应的设计模式模板：

| 用户需求 | 选择模式 | 模板文件 | 推荐行数 | 上限 |
|---------|---------|---------|---------|------|
| 遵循某库/框架规范 | Tool Wrapper | `tool_wrapper_template.md` | 80-150行 | 200行 |
| 输出固定格式内容 | Generator | `generator_template.md` | 150-250行 | 300行 |
| 代码/内容审查评估 | Reviewer | `reviewer_template.md` | 150-250行 | 300行 |
| 先收集需求再执行 | Inversion | `inversion_template.md` | 150-250行 | 300行 |
| 多步骤依赖流程 | Pipeline | `pipeline_template.md` | 200-350行 | 400行 |

## 二、模板使用方法

### 2.1 基本流程

```
1. 确定用户需求 → 选择对应模板
2. 复制模板文件 → 重命名为 SKILL.md
3. 填充 {{占位符}} → 替换为具体内容
4. 删除 <!-- 写作指引 --> 和 <!-- 质量检查点 --> 注释
5. 运行 L1 静态检查 → 确认 10/10 通过
6. 运行 L2 LLM验证 → 确认 TRACE ≥ 35
7. (可选) 运行 L3 试运行 → 确认可运行性
```

### 2.2 占位符说明

模板使用 `{{占位符}}` 标记 AI 需要填充的位置：

| 占位符 | 含义 | 示例 |
|--------|------|------|
| `{{slug}}` | skill的kebab-case名称 | `seo-meta-generator` |
| `{{display_name}}` | 中文显示名(≤20字符) | `SEO元描述生成器` |
| `{{summary}}` | 一句话摘要(≤100字符) | `当需要生成SEO友好的meta描述时使用` |
| `{{topic}}` | skill的核心主题 | `SEO优化` |
| `{{feature}}` | 核心功能 | `生成meta description` |
| `{{input_type}}` | 输入类型 | `关键词列表` |
| `{{output_type}}` | 输出类型 | `HTML meta标签` |
| `{{dependency}}` | 依赖项 | `LLM / 无外部API` |

### 2.3 8标准章节

每个模板都包含以下8个标准章节（按顺序）：

1. **核心能力** - 3-5条具体能力描述
2. **适用场景** - 用户会怎么说 + skill做什么
3. **使用流程** - Step by step 操作指引
4. **输入格式** - 输入参数说明
5. **输出格式** - 输出结构说明
6. **异常处理** - 错误场景|原因|处理方式 表格
7. **依赖说明** - LLM/API Key/运行环境
8. **案例展示** - 至少2个输入→输出示例

## 三、质量检查

### 3.1 L1静态检查（10项）

| # | 检查项 | 通过标准 |
|---|--------|---------|
| 1 | 8标准章节齐全 | 8/8全部存在 |
| 2 | description长度 | 150-280字符 |
| 3 | description含三要素 | 核心功能+适用场景+触发关键词 |
| 4 | 总行数 | 200-400行(按模式) |
| 5 | 错误处理表格化 | 包含"场景\|原因\|处理方式"表格 |
| 6 | 至少2个示例 | 示例章节含2+个输入→输出 |
| 7 | 依赖说明表格化 | 包含依赖项表格 |
| 8 | 已知限制3+条 | 至少3条具体限制 |
| 9 | 无占位符 | 无"待补充"/"TODO"/"{{}}"等 |
| 10 | frontmatter完整 | slug/name/version/displayName/summary/license/tools齐全 |

### 3.2 L2 LLM验证（TRACE五维度）

| 维度 | 评分标准 | 目标分 |
|------|---------|--------|
| Trust | 安全+国内可用+中文支持 | ≥7/10 |
| Reliability | 异常处理+边界输入 | ≥7/10 |
| Adaptability | description精准+边界清晰 | ≥7/10 |
| Convention | 信息架构+文档质量 | ≥7/10 |
| Effectiveness | 结果正确+输出完整 | ≥7/10 |
| **总分** | | **≥35/50** |

## 四、模板文件清单

```
templates/
  ├── README.md                      # 本文件
  ├── tool_wrapper_template.md       # Tool Wrapper 模式
  ├── generator_template.md          # Generator 模式
  ├── reviewer_template.md           # Reviewer 模式
  ├── inversion_template.md          # Inversion 模式
  └── pipeline_template.md           # Pipeline 模式
```
