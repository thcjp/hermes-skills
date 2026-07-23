---
slug: hugo-blog-publisher
name: hugo-blog-publisher
version: "1.1.1"
displayName: Hugo Blog Publisher
summary: 发布文章到 Hugo 博客。用于当用户说\
license: MIT-0
description: |-
  发布文章到 Hugo 博客。用于当用户说\

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: blog, hugo, 用于当用户说, publisher, 发布文章到, 博客
tags: '[''Development'']'
tools:
  - read
  - exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Hugo Blog Publisher

将 Markdown 文章发布到 Hugo 博客并推送到 GitHub。

## 自动读取配置

此 Skill 会自动尝试从以下位置读取博客配置：

1. 用户记忆文件（MEMORY.md / USER.md）中的博客域名、路径等
2. 博客目录下的 .git 配置

如果未找到配置，才询问用户。

## 使用前提

1. **本地运行**：此 Skill 需要在能够访问博客目录的机器上运行
2. **Git 配置**：确保机器上有 Git 和 GitHub 访问权限

## 发布流程

### 1. 分析内容

从用户提供的文章内容中自动提取：

* **标题**：从 front matter 或内容中提取
* **标签**：根据内容主题自动判断（如 AI → ["ai"]）
* **分类**：根据内容类型判断（如技术文章 → ["tech"]）

### 2. 生成文件名

* 格式: `content/posts/{slug}.md`
* slug: 标题转为 URL 友好格式（小写、连字符、去除特殊字符）
* 注意：文件名不要包含日期，日期在 front matter 的 `date` 字段中指定

### 3. 渲染 Front Matter

```yaml
---
title: "文章标题"
date: YYYY-MM-DD
draft: false
tags: ["tag1", "tag2"]
categories: ["Category"]
description: "文章描述"
---
```

**重要规则**：

* **categories**：使用已有分类（小写英文 slug），如 `tech`, `investment`, `ai`, `photo`
* **tags**：使用小写英文 slug，不要用中文
* **slug**：文件名使用小写英文，不要用中文

### 4. 标签/分类映射（重要）

**文章 frontmatter 用英文 slug，页面展示用中文**，通过 Hugo Taxonomy Branch Bundle 实现：

1. frontmatter 中使用英文 slug：

   yaml

   ```
   tags: ["ssg", "ssr"]
   categories: ["tech"]
   ```
2. 如果遇到新标签/分类没有映射文件，需要创建：

   text

   ```
   content/tags/<slug>/_index.md
   content/categories/<slug>/_index.md
   ```
3. 文件内容极简：

   yaml

   ```
   ---
   title: "显示的中文名"
   ---
   ```

**不用 i18n，全部用 _index.md 映射！**

#### 常用分类 (categories)

| Slug | 中文显示 |
| --- | --- |
| tech | 技术 |
| photo | 摄影 |
| ai | AI |
| investment | 投资 |
| tech-news | 科技资讯 |
| science | 科学 |
| art | 艺术 |
| life | 生活 |
| reading-notes | 读书笔记 |

#### 常用标签 (tags)

| Slug | 中文显示 |
| --- | --- |
| ai | AI |
| llm | 大语言模型 |
| agent | 智能体 |
| programming | 编程 |
| thinking | 思考 |
| photography | 摄影 |
| camera | 相机 |
| photo | 照片 |
| options | 期权 |
| trading | 交易 |
| investment | 投资 |
| stock | 股票 |
| php | PHP |
| go | Go |
| kubernetes | Kubernetes |
| rag | RAG |

#### 专属名词（保持英文显示）

* AI、RAG、NLP、Kubernetes、Go、Elasticsearch、PHP、SQL、Kimi、DeepSeek、Claude、GPT、SSG、SSR 等技术名称用英文 slug

### 5. 添加 截断标记

在第一段或导言后添加 `<!--more-->`，让列表页显示摘要。

位置通常在：

* 第一段结束后的空行
* 导言和正文之间

### 6. Git 推送

从博客目录自动检测 git 状态并推送：

```bash
cd {博客路径}
git add content/posts/{文件名}
git commit -m "新增：{文章标题}"
git push
```

如果 git push 需要认证，确保用户已配置 SSH key 或 git credentials。

### 7. 返回部署链接

告知用户文章已发布成功。

注意：不要硬编码域名，应该根据用户提供的博客信息返回相应链接。

## 示例

```text
用户：帮我发布这篇blog（附文章内容）

系统自动完成：
1. 分析内容，提取标题、标签、分类
2. 生成文件名（slug）
3. 添加 front matter 和 <!--more--> 标记
4. 如需新标签/分类，创建 _index.md 映射文件
5. 检测博客目录并推送
6. 返回部署链接
```

## 注意事项

* slug 生成：英文直接用，中文可用拼音或英文关键词
* 位置：根据文章结构选择合适位置
* commit message：建议用 "新增:" 前缀
* 如果用户没有提供博客路径，默认用当前目录的 blog 子目录
* **所有标签/分类映射都用 _index.md 文件方式，不用 i18n/zh.toml！**

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 发布文章到 Hugo 博客
- 触发关键词: blog, hugo, 用于当用户说, publisher, 发布文章到, 博客

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Hugo Blog Publisher？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Hugo Blog Publisher有什么限制？
A: 请参考已知限制章节了解具体限制。
