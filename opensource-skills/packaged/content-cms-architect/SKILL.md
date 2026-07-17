---
slug: content-cms-architect
name: content-cms-architect
version: "1.0.0"
displayName: "CMS内容架构师"
summary: "Headless CMS内容架构,从内容建模到SEO-AEO,打造可扩展内容平台"
license: MIT
description: |-
  CMS内容架构师——基于Sanity官方最佳实践设计可扩展的内容管理系统,从内容建模到SEO-AEO优化,打造前端自由、内容结构化的现代内容平台。

  核心能力:
  - 内容建模设计:Schema定义/字段类型/引用关系/内容结构化
  - GROQ查询语言:高效查询与过滤,替代REST API
  - Sanity Studio配置:多角色编辑/工作流/草稿发布
  - SEO与AEO优化:搜索引擎优化+答案引擎优化双覆盖
  - 内容A/B实验:内容变体+实验设计+数据分析
  - 多语言国际化:i18n插件+翻译工作流

  适用场景:
  - 独立创业者企业网站:内容管理+SEO优化一体化
  - 电商卖家商品内容:结构化商品描述+富文本+图片管理
  - 一人公司多语言站点:国际化内容管理+翻译工作流
  - 副业达人博客媒体:草稿发布排期+SEO+A/B测试

  差异化:不是通用CMS搭建教程,而是基于Sanity最佳实践的深度架构指导,覆盖内容建模到AEO优化的完整链路,让小团队也能构建企业级内容管理平台。

  触发关键词:CMS、内容管理、Sanity、GROQ、内容建模、SEO、AEO、答案引擎优化、内容实验、Headless CMS
tags: [内容管理, Headless CMS, 内容建模, SEO优化, Sanity]
tools: [read, exec]
---

# CMS内容架构师

基于 Sanity 官方最佳实践,设计可扩展、高性能的内容管理系统。从内容建模到 GROQ 查询,从 SEO 优化到内容实验,全栈 CMS 架构。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| 企业CMS | 企业网站内容管理 | Sanity Studio + 多角色编辑 |
| 电商内容 | 商品描述/分类/营销 | 结构化内容 + 富文本 + 图片 |
| 多语言站点 | 国际化内容 | i18n 插件 + 翻译工作流 |
| Headless CMS | 前后端分离 | API 优先 + 前端自由选择 |
| 博客/媒体 | 内容发布平台 | 草稿/发布/排期 + SEO |
| 内容实验 | A-B测试 | 内容变体 + 实验 + 分析 |

## 工作流

### 1. 内容建模设计

1. **内容类型规划**
   - 识别核心内容实体(文章/产品/页面/作者)
   - 定义字段类型(字符串/富文本/图片/引用/数组)
   - 设计引用关系(一对一/一对多/多对多)
2. **Schema 定义**
   - `schemaTypes`:定义文档类型与字段
   - `structure`:自定义 Studio 管理界面
   - `plugins`:启用 desk-tool/vision/i18n 等
3. **内容建模最佳实践**
   - 字段最小化:只存结构化数据
   - 便携文本(Portable Text):富文本而非 HTML
   - 引用而非嵌入:避免数据冗余
   - 预览组件:实时内容预览

### 2. GROQ 查询优化

1. **基础查询**
   - `*[_type == "post"]`:获取所有文章
   - `[0...5]`:分页切片
   - `| order(publishedAt desc)`:排序
   - `[slug.current == $slug]`:条件过滤
2. **高级查询**
   - 投影(Projection):`{ title, "author": author->name }`
   - 嵌套引用:`author->{name, "avatar": avatar.asset->url}`
   - 聚合:`count(*[_type == "comment" && post._ref == ^._id])`
   - 参数化查询:变量注入
3. **性能优化**
   - 只查询需要的字段
   - 使用 perspective(published/raw/drafts)
   - 缓存策略(Next.js ISR/CDN)

### 3. SEO 与 AEO 优化

1. **SEO 基础**
   - 元数据字段(title/description/ogImage)
   - 结构化数据(JSON-LD)
   - URL slug 管理
   - sitemap 自动生成
2. **AEO(答案引擎优化)**
   - E-E-A-T 信号:作者权威性/可信度
   - FAQ Schema:问题-答案结构
   - 内容引用与来源标注
   - LLM 引用追踪(GPT/Gemini/Claude)
3. **性能与可访问性**
   - 图片优化(Next.js Image + Sanity CDN)
   - Core Web Vitals 目标
   - WCAG 2.1 AA 合规

### 4. 内容工作流

1. **编辑流程**
   - 草稿 → 审核 → 发布
   - 内容排期
   - 版本历史
2. **协作**
   - 多角色(编辑/审阅者/管理员)
   - 评论与批注
   - 字段级权限
3. **内容实验**
   - 创建内容变体
   - A-B 测试分配
   - 结果分析

## 依赖说明

| 依赖类型 | 要求 | 说明 |
|:---------|:-----|:-----|
| LLM | 任意支持 Agent Skills 的 LLM | Claude/GPT/Gemini 等 |
| 运行环境 | Node.js 18+ | Sanity Studio 运行环境 |
| CLI | Sanity CLI (npm i -g @sanity/cli) | 初始化与管理项目 |
| API Key | Sanity Project ID + Dataset | 从 Sanity Manage 获取 |
| 前端 | Next.js/Remix/Astro(可选) | 前端渲染框架 |
| 可选 | Sanity 自定义计划 | 免费版:3 用户/10k 文档 |

## 异常处理

| 异常场景 | 处理方式 |
|:---------|:---------|
| GROQ 查询超时 | 优化查询,减少嵌套,使用索引 |
| 图片加载慢 | 使用 Sanity CDN + srcset + lazy load |
| 内容冲突 | 使用实时协作 + 字段级锁定 |
| Studio 启动失败 | 检查 Node 版本,清理 node_modules |
| API 限流 | Sanity 免费版有速率限制,升级或缓存 |
| 数据丢失 | 启用草稿/历史,定期导出备份 |

## 示例

### 输入:设计博客内容模型

```
用户请求:为一个技术博客设计内容模型,包含文章、作者、分类、标签

输出:
- schemas/post.ts (文章:标题/正文/封面/作者引用/分类引用/标签/SEO字段)
- schemas/author.ts (作者:名称/头像/简介/社交链接)
- schemas/category.ts (分类:名称/描述/封面)
- schemas/tag.ts (标签:名称)
- schema.ts (组装所有类型)
- sanity.config.ts (Studio 配置)
```

### 输入:GROQ查询热门文章

```
用户请求:查询最近30天浏览量最高的5篇文章,包含作者信息

输出GROQ:
*[_type == "post" && publishedAt > now() - 30*24*60*60*1000]
  | order(views desc) [0...5]
  {
    title,
    "slug": slug.current,
    publishedAt,
    "author": author->{name, "avatar": avatar.asset->url},
    excerpt,
    "categories": categories[]->{title, "slug": slug.current}
  }
```
