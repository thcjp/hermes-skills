---
slug: "hugo-blog-publisher"
name: "hugo-blog-publisher"
version: "2.0.0"
displayName: "博客发布工具"
summary: "将Markdown文章发布到静态站点生成器博客并推送到代码仓库"
license: "Proprietary"
description: |-
  将Markdown文章发布到静态站点生成器博客并推送到代码仓库。自动分析内容提取
  标题、标签、分类，生成front matter，创建标签分类映射文件，添加截断标记，
  执行Git推送并返回部署链接。支持Taxonomy Branch Bundle映射机制，无需i18n
  配置。适用于独立开发者、企业团队和自动化工作流场景。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 研发工具
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
---
# 博客发布工具

将Markdown文章发布到静态站点生成器博客并推送到代码仓库。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 博客发布工具处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 博客发布工具章发布到静态站点生成 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 自动内容分析
从用户提供的文章内容中自动提取：
- 标题：从front matter或内容中提取
- 标签：根据内容主题自动判断（如AI → `["ai"]`）
- 分类：根据内容类型判断（如技术文章 → `["tech"]`）

**处理**: 解析自动内容分析的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回自动内容分析的处理结果,包含执行状态码、结果数据和执行日志。

### 2. 文件名生成
- 格式：`content/posts/{slug}.md`
- slug：标题转为URL友好格式（小写、连字符、去除特殊字符）
- 文件名不包含日期，日期在front matter的 `date` 字段中指定

**输入**: 用户提供文件名生成所需的指令和必要参数。
**处理**: 解析文件名生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回文件名生成的处理结果,包含执行状态码、结果数据和执行日志。

### 3. Front Matter渲染
```yaml
---
title: "文章标题"
date: 2026-07-21
draft: false
tags: ["tag1", "tag2"]
categories: ["tech"]
description: "文章描述"
---
```

规则：
- `categories`：使用已有分类的小写英文slug，如 `tech`, `investment`, `ai`, `photo`
- `tags`：使用小写英文slug，不用中文
- `slug`：文件名使用小写英文，不用中文

**输入**: 用户提供Front Matter渲染所需的指令和必要参数。
**处理**: 解析Front Matter渲染的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回Front Matter渲染的处理结果,包含执行状态码、结果数据和执行日志。

### 4. 标签分类映射（Taxonomy Branch Bundle）
文章frontmatter用英文slug，页面展示用中文，通过 `_index.md` 实现：

1. frontmatter中使用英文slug：
```yaml
tags: ["ssg", "ssr"]
categories: ["tech"]
```

2. 遇到新标签/分类没有映射文件时，创建：
```
content/tags/<slug>/_index.md
content/categories/<slug>/_index.md
```

3. 文件内容极简：
```yaml
---
title: "显示的中文名"
---
```

#### 常用分类

| Slug | 中文显示 |
|:---:|:---:|
| tech | 技术 |
| photo | 摄影 |
| ai | AI |
| investment | 投资 |
| science | 科学 |
| art | 艺术 |
| life | 生活 |
| reading-notes | 读书笔记 |

#### 常用标签

| Slug(续)| 中文显示 |
|:---------|---------:|
| ai | AI |
| llm | 大语言模型 |
| agent | 智能体 |
| programming | 编程 |
| kubernetes | Kubernetes |
| rag | RAG |

**处理**: 解析标签分类映射（Taxonomy Branch Bundle）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
### 5. 截断标记
在第一段或导言后添加 `<!--more-->`，让列表页显示摘要。位置通常在第一段结束后的空行或导言和正文之间。

**输入**: 用户提供截断标记所需的指令和必要参数。
**处理**: 解析截断标记的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回截断标记的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`截断标记`的配置文档进行参数调优
### 6. Git推送
从博客目录自动检测git状态并推送：
```bash
cd {博客路径}
git add content/posts/{文件名}
git commit -m "新增：{文章标题}"
git push
```

**输入**: 用户提供Git推送所需的指令和必要参数。
**处理**: 解析Git推送的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回Git推送的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `git推送` 选项

### 7. 部署链接返回
根据用户提供的博客信息返回相应链接，不硬编码域名。

**处理**: 解析部署链接返回的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证返回数据的完整性和格式正确性
- 参考`部署链接返回`的配置文档进行参数调优
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`hugo-blog-publisher`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 配置读取

自动尝试从以下位置读取博客配置：
1. 用户记忆文件（`MEMORY.md` / `USER.md`）中的博客域名、路径等
2. 博客目录下的 `.git` 配置

如果未找到配置，才询问用户。

## 真实示例

### 示例1：发布技术文章

用户输入文章内容后，系统自动完成：

```bash
# 1. 生成文件
content/posts/hugo-blog-deployment.md
# ...
# 2. 文件内容
```
```yaml
---
title: "静态站点部署指南"
date: 2026-07-21
draft: false
tags: ["ssg", "deployment"]
categories: ["tech"]
description: "如何将静态站点部署到生产环境"
---
# ...
本文介绍静态站点的部署流程。
# ...
<!--more-->
# ...
## 准备工作
# ...
首先确保本地环境已安装所有依赖...
```

```bash
# 3. 如需新标签，创建映射
content/tags/deployment/_index.md
# 内容: ---\ntitle: "部署"\n---
# ...
# 4. Git推送
cd ~/my-blog
git add content/posts/hugo-blog-deployment.md
git commit -m "新增：静态站点部署指南"
git push
```

输出：
```
文章已发布成功！
部署链接: https://example.com/posts/hugo-blog-deployment/
```

### 示例2：创建新标签映射

当文章使用了新标签 `docker`，需要创建映射文件：

```bash
# 创建 content/tags/docker/_index.md
---
title: "Docker"
---
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 博客路径未找到 | 配置文件缺失 | 检查 `MEMORY.md` 或 `.git` 配置，询问用户提供博客路径 |
| Git推送认证失败 | SSH key或credentials未配置 | 确保用户已配置SSH key或git credentials |
| 文件名slug冲突 | 同名文章已存在 | 检查 `content/posts/` 目录，添加日期前缀或修改slug |
| front matter格式错误 | YAML语法问题 | 确保YAML缩进正确，字符串用引号包裹 |
| 新标签缺少映射文件 | `_index.md` 未创建 | 为每个新标签/分类创建 `content/tags/<slug>/_index.md` |
| `<!--more-->` 位置错误 | 截断标记缺失或位置不当 | 在第一段结束后的空行添加截断标记 |
| 中文slug问题 | 文件名包含中文字符 | 使用拼音或英文关键词作为slug，保持小写连字符格式 |

## 常见问题

### Q1: 标签和分类应该用中文还是英文？
A: frontmatter中使用小写英文slug（如 `tech`, `ai`），页面展示通过 `_index.md` 映射为中文。不用i18n配置，全部用 `_index.md` 映射。

### Q2: 如何处理新标签没有中文映射的情况？
A: 需要创建 `content/tags/<slug>/_index.md` 文件，内容为 `---\ntitle: "中文显示名"\n---`。例如标签 `docker` 创建文件后title设为 `"Docker"`。

### Q3: 截断标记 `<!--more-->` 应该放在哪里？
A: 通常放在第一段结束后的空行，或导言和正文之间。列表页只显示截断标记之前的内容作为摘要。

### Q4: commit message有什么格式要求？
A: 建议使用 "新增:" 前缀，如 `git commit -m "新增：文章标题"`。

### Q5: 如果用户没有提供博客路径怎么办？
A: 默认使用当前目录的 `blog` 子目录。也可从用户记忆文件（`MEMORY.md` / `USER.md`）或 `.git` 配置中自动检测。

### Q6: 专属技术名词如何处理？
A: AI、RAG、NLP、Kubernetes、Go、PHP、SQL、SSG、SSR等技术名称直接用英文slug，不需要中文映射。

### Q7: 文件名中可以包含日期吗？
A: 文件名不包含日期，日期在front matter的 `date` 字段中指定。文件名格式为 `content/posts/{slug}.md`。

## 已知限制

- 需要本地运行，必须能访问博客目录
- 需要Git和代码仓库访问权限（SSH key或credentials）
- 标签分类映射使用 `_index.md` 文件方式，不用i18n
- 所有标签和分类使用英文slug，中文显示通过映射文件
- 文件名使用小写英文，不用中文
- 需要预先配置好博客域名和路径信息
