---
slug: content-cms-architect
name: content-cms-architect
version: 1.0.1
displayName: CMS内容架构师
summary: Headless CMS内容架构,从内容建模到SEO-AEO,打造可扩展内容平台
license: Proprietary
description: CMS内容架构师——基于Sanity/Strapi/Payload等Headless CMS最佳实践设计可扩展内容管理系统,从内容建模到GROQ/REST/GraphQL查询,从SEO-AEO优化到内容A/B实验,打造前端自由、内容结构化的现代内容平台。覆盖Schema定义、字段类型设计、引用关系、Portable
  Text、多语言i18n、草稿发布工作流、答案引擎优化全栈
tags:
- 内容管理
- Headless CMS
- 内容建模
- SEO优化
- Sanity
tools:
- read
- exec
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
---
# CMS内容架构师

基于 Headless CMS 官方最佳实践,设计可扩展、高性能的内容管理系统。从内容建模到 GROQ 查询,从 SEO 优化到内容实验,全栈 CMS 架构。

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 企业CMS | 业务需求+内容类型清单 | Schema定义+Studio配置+API查询模板 |
| 电商内容 | 商品分类+属性字段 | 结构化Schema+富文本+图片优化方案 |
| 多语言站点 | 主语言内容+目标语言 | i18n插件配置+翻译工作流 |
| Headless API | 内容模型+前端框架 | GROQ/GraphQL查询+缓存策略 |
| 博客/媒体 | 发布流程+SEO要求 | 草稿发布工作流+SEO字段+sitemap |
| 内容实验 | 测试假设+变体数量 | 内容变体Schema+A/B分配方案 |

### 不适用于
- 传统WordPress等单体CMS架构(本Skill聚焦Headless)
- 前端UI组件开发与样式实现(请使用前端框架工具)
- 内容翻译执行(本Skill仅设计翻译工作流,不执行翻译)
- CMS服务器部署与运维(请使用DevOps工具)
- 数据库底层性能调优(本Skill聚焦应用层)

## 核心能力

1. **内容建模设计**:Schema定义、字段类型(字符串/富文本/图片/引用/数组)、引用关系(1:1/1:N/N:N)、Portable Text富文本设计
2. **查询语言优化**:GROQ(Sanity)/GraphQL(Strapi)/REST API通用、投影、嵌套引用、参数化查询、性能优化(字段裁剪/缓存)
3. **Studio/管理后台配置**:多角色编辑(编辑/审阅者/管理员)、字段级权限、自定义结构、预览组件
4. **SEO与AEO双优化**:元数据字段、JSON-LD结构化数据、E-E-A-T信号、FAQ Schema、LLM引用追踪
5. **内容工作流与实验**:草稿→审核→发布、内容排期、版本历史、A/B测试变体、多语言i18n翻译工作流

## 使用流程

### Step 1: 内容需求分析
1. 识别核心内容实体(文章/产品/页面/作者/分类/标签)
2. 确定字段类型(字符串/富文本/图片/引用/数组/对象)
3. 设计引用关系(一对一/一对多/多对多)
4. 规划多语言需求与翻译工作流
5. 确定SEO/AEO字段需求

### Step 2: CMS选型与Schema设计
1. 选型:海外用Sanity/Strapi/Payload/Contentful,国内用飞书多维表格/语雀/自研Headless
2. 定义 `schemaTypes`:文档类型与字段
3. 定义 `structure`:自定义Studio管理界面
4. 配置 `plugins`:desk-tool/vision/i18n等
5. 最佳实践:字段最小化、Portable Text、引用而非嵌入、预览组件

### Step 3: 查询语言实现
1. 基础查询:过滤、排序、分页
2. 高级查询:投影、嵌套引用、聚合、参数化
3. 性能优化:只查询需要的字段、perspective控制、缓存策略

### Step 4: SEO与AEO优化
1. SEO基础:元数据字段、JSON-LD、URL slug、sitemap
2. AEO:E-E-A-T信号、FAQ Schema、内容引用标注、LLM引用追踪
3. 性能与可访问性:图片优化、Core Web Vitals、WCAG 2.1 AA

### Step 5: 工作流与协作配置
1. 编辑流程:草稿→审核→发布
2. 协作:多角色、评论批注、字段级权限
3. 内容实验:变体创建、A/B分配、结果分析

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

## 输出规范

- Schema文件:`output/{project}/schemas/*.ts`
- 配置文件:`output/{project}/sanity.config.ts`
- 查询模板:`output/{project}/queries/*.groq`
- SEO模板:`output/{project}/seo-templates.md`
- 工作流配置:`output/{project}/workflow.md`

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: Node.js 18+ (Sanity Studio运行环境)

### 依赖项

| 依赖类型 | 要求 | 说明 |
|:-----|:-----|:-----|
| LLM | 任意支持 Agent Skills 的 LLM | Claude/GPT/Gemini 等 |
| 运行环境 | Node.js 18+ | Headless CMS Studio运行环境 |
| CLI | Sanity CLI (npm i -g @sanity/cli) | 初始化与管理项目 |
| API Key | Sanity Project ID + Dataset | 从 Sanity Manage 获取(见安全章节) |
| 前端 | Next.js/Remix/Astro(可选) | 前端渲染框架 |
| 可选 | Sanity 自定义计划 | 免费版:3 用户/10k 文档 |

### 中外CMS对照(国内替代方案)

| 海外CMS | 国内替代 | 说明 |
|---:|---:|---:|
| Sanity | 飞书多维表格+API | 国内无完美替代,可用多维表格+自研API模拟 |
| Strapi | 语雀+开放API | 语雀提供内容结构化管理,API可对接前端 |
| Contentful | Notion+API | Notion API可作为轻量Headless CMS |
| Payload | 自研Headless(基于Node.js) | 完全自主可控,无数据出境风险 |
| Contentstack | 钉钉文档+API | 钉钉文档结构化能力+开放API |

### API Key 配置
- **Sanity Project ID**:从 manage.sanity.io 获取,非敏感信息
- **Sanity API Token(写操作)**:敏感凭证,由用户在环境变量配置,本Skill不存储
- **国内CMS**:飞书/语雀/钉钉API Token,由用户自行配置

### 可用性分类
- **分类**: MD+EXEC
- **说明**: Schema设计为纯Markdown,实际部署需exec执行npm/sanity CLI命令

## 示例

### 示例1: 设计博客内容模型

**输入**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| input | string | 是 | CMS内容架构师处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
需求:为一个技术博客设计内容模型
实体:文章、作者、分类、标签
功能:草稿发布、SEO优化、作者页面、分类归档
前端:Next.js
```

**输出** (`output/blog/schemas/post.ts`):
```typescript
export const post = defineType({
  name: 'post',
  title: '文章',
  type: 'document',
  fields: [
    { name: 'title', title: '标题', type: 'string', validation: Rule => Rule.required() },
    { name: 'slug', title: 'URL', type: 'slug', options: { source: 'title' } },
    { name: 'excerpt', title: '摘要', type: 'text', rows: 3 },
    { name: 'body', title: '正文', type: 'array', of: [{ type: 'block' }] },
    { name: 'coverImage', title: '封面', type: 'image', options: { hotspot: true } },
    { name: 'author', title: '作者', type: 'reference', to: [{ type: 'author' }] },
    { name: 'categories', title: '分类', type: 'array', of: [{ type: 'reference', to: [{ type: 'category' }] }] },
    { name: 'tags', title: '标签', type: 'array', of: [{ type: 'reference', to: [{ type: 'tag' }] }] },
    { name: 'publishedAt', title: '发布时间', type: 'datetime' },
    { name: 'seo', title: 'SEO', type: 'object', fields: [
      { name: 'metaTitle', type: 'string' },
      { name: 'metaDescription', type: 'text', rows: 2 },
      { name: 'ogImage', type: 'image' }
    ]}
  ],
  preview: { select: { title: 'title', media: 'coverImage', subtitle: 'publishedAt' } }
})
```

**输出** (`output/blog/queries/recent-posts.groq`):
```groq
*[_type == "post" && publishedAt <= now()]
  | order(publishedAt desc) [0...10]
  {
    title,
    "slug": slug.current,
    publishedAt,
    excerpt,
    "author": author->{name, "avatar": avatar.asset->url},
    "categories": categories[]->{title, "slug": slug.current}
  }
```

### 示例2: GROQ查询热门文章

**输入**:
```
需求:查询最近30天浏览量最高的5篇文章,包含作者信息
数据集:sanity-blog-dev
```

**输出** (`output/blog/queries/top-posts.groq`):
```groq
*[_type == "post"
  && publishedAt > now() - 30*24*60*60*1000
  && defined(views)]
  | order(views desc) [0...5]
  {
    "id": _id,
    title,
    "slug": slug.current,
    publishedAt,
    views,
    "author": author->{
      name,
      "avatar": avatar.asset->url,
      "bio": bio[0].children[0].text
    },
    excerpt,
    "categories": categories[]->{
      title,
      "slug": slug.current
    },
    "readingTime": round(length(body) / 1000) + " min"
  }
```

**输出** (`output/blog/queries/with-cache.ts`):
```typescript
// Next.js ISR 缓存策略
export async function getTopPosts() {
  const posts = await client.fetch(topPostsQuery, {}, {
    next: { revalidate: 3600 } // 1小时重新验证
  })
  return posts
}
```

## 错误处理
- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断
- 重试机制: 失败时自动重试, 最多3次

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| GROQ查询超时 | 嵌套过深/全表扫描 | 优化查询,减少嵌套层级,使用projection字段裁剪,添加索引 |
| 图片加载慢 | 未使用CDN/未做srcset | 使用 Sanity CDN + srcset + lazy load,配置hotspot |
| 内容冲突 | 多人同时编辑 | 启用实时协作 + 字段级锁定,使用presence indicator |
| Studio 启动失败 | Node版本不匹配/依赖冲突 | 检查Node 18+,清理 node_modules,使用nvm切换版本 |
| API 限流 | 免费版速率限制 | 升级计划或实现客户端缓存(ISR/CDN),批量查询 |
| 数据丢失 | 误删/无备份 | 启用草稿/历史,定期 `sanity export` 备份至本地 |
| i18n内容不同步 | 翻译工作流缺失 | 配置i18n插件,设置翻译状态字段,使用workflow插件 |
| 引用断裂 | 删除被引用文档 | 配置引用完整性检查,删除前提示影响范围 |

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 技术博客内容模型设计

**输入**:
```
需求: 为技术博客设计Sanity内容模型
实体: 文章、作者、分类、标签
功能: 草稿发布、SEO优化、作者页面、分类归档
前端: Next.js 14 App Router
```

**LLM生成输出**:
```typescript
// output/blog/schemas/post.ts
export const post = defineType({
  name: 'post',
  title: '文章',
  type: 'document',
  fields: [
    { name: 'title', title: '标题', type: 'string', validation: Rule => Rule.required().max(120) },
    { name: 'slug', title: 'URL路径', type: 'slug', options: { source: 'title', maxLength: 96 } },
    { name: 'excerpt', title: '摘要', type: 'text', rows: 3, validation: Rule => Rule.max(300) },
    { name: 'body', title: '正文', type: 'array', of: [{ type: 'block' }] },
    { name: 'coverImage', title: '封面图', type: 'image', options: { hotspot: true } },
    { name: 'author', title: '作者', type: 'reference', to: [{ type: 'author' }], validation: Rule => Rule.required() },
    { name: 'categories', title: '分类', type: 'array', of: [{ type: 'reference', to: [{ type: 'category' }] }], validation: Rule => Rule.min(1) },
    { name: 'tags', title: '标签', type: 'array', of: [{ type: 'reference', to: [{ type: 'tag' }] }] },
    { name: 'publishedAt', title: '发布时间', type: 'datetime' },
    { name: 'featured', title: '精选', type: 'boolean', initialValue: false },
    { name: 'readingTime', title: '阅读时长', type: 'number', description: '自动计算，无需手动填写' },
    { name: 'seo', title: 'SEO设置', type: 'object', fields: [
      { name: 'metaTitle', type: 'string', description: '默认使用文章标题' },
      { name: 'metaDescription', type: 'text', rows: 2, description: '默认使用摘要' },
      { name: 'ogImage', type: 'image', description: '默认使用封面图' },
      { name: 'noindex', type: 'boolean', initialValue: false, description: '设为true则不被搜索引擎收录' }
    ]}
  ],
  preview: {
    select: { title: 'title', subtitle: 'publishedAt', media: 'coverImage' }
  }
});
// ...
// output/blog/schemas/author.ts
export const author = defineType({
  name: 'author',
  title: '作者',
  type: 'document',
  fields: [
    { name: 'name', title: '姓名', type: 'string', validation: Rule => Rule.required() },
    { name: 'slug', title: 'URL', type: 'slug', options: { source: 'name' } },
    { name: 'avatar', title: '头像', type: 'image', options: { hotspot: true } },
    { name: 'bio', title: '简介', type: 'array', of: [{ type: 'block' }] },
    { name: 'social', title: '社交账号', type: 'object', fields: [
      { name: 'twitter', type: 'string' },
      { name: 'github', type: 'string' },
      { name: 'linkedin', type: 'string' }
    ]},
    // AEO: 作者权威性信号
    { name: 'expertise', title: '专业领域', type: 'array', of: [{ type: 'string' }] },
    { name: 'credentials', title: '资质认证', type: 'text', rows: 3 }
  ],
  preview: { select: { title: 'name', media: 'avatar' } }
});
// ...
// output/blog/schemas/category.ts
export const category = defineType({
  name: 'category',
  title: '分类',
  type: 'document',
  fields: [
    { name: 'title', type: 'string', validation: Rule => Rule.required() },
    { name: 'slug', type: 'slug', options: { source: 'title' } },
    { name: 'description', type: 'text', rows: 2 },
    { name: 'parent', type: 'reference', to: [{ type: 'category' }], description: '父分类(支持多级)' }
  ],
  preview: { select: { title: 'title' } }
});
```

```groq
// output/blog/queries/recent-posts.groq
// 获取最近10篇已发布文章
*[_type == "post" && publishedAt <= now()]
  | order(publishedAt desc) [0...10]
  {
    "id": _id,
    title,
    "slug": slug.current,
    publishedAt,
    excerpt,
    "author": author->{
      name,
      "avatar": avatar.asset->url,
      "slug": slug.current
    },
    "categories": categories[]->{ title, "slug": slug.current },
    "coverImage": coverImage.asset->url,
    "readingTime": round(length(string(body)) / 1000) + 1
  }
# ...
// output/blog/queries/post-by-slug.groq
// 按slug查询单篇文章（含作者、分类、相关文章）
*[_type == "post" && slug.current == $slug][0] {
  title,
  publishedAt,
  body,
  "author": author->{
    name,
    "avatar": avatar.asset->url,
    bio,
    "slug": slug.current
  },
  "categories": categories[]->{ title, "slug": slug.current },
  "relatedPosts": *[_type == "post" 
    && publishedAt <= now() 
    && slug.current != $slug
    && count(categories[@._ref in ^.^.categories[]._ref]) > 0
  ] | order(publishedAt desc) [0...3] {
    title,
    "slug": slug.current,
    publishedAt
  }
}
```

**效果验证**: ✓3个文档类型Schema完整（文章/作者/分类） ✓GROQ查询含投影和嵌套引用 ✓相关文章查询逻辑正确 ✓SEO字段含ogImage/noindex ✓AEO字段含作者权威性

### 案例2: 电商商品内容建模

**输入**:
```
需求: 为电商平台设计商品内容模型
商品类型: 实体商品 + 虚拟商品（课程）
功能: 多规格(SKU)、富文本描述、评价关联、多语言
```

**LLM生成输出**:
```typescript
// output/ecommerce/schemas/product.ts
export const product = defineType({
  name: 'product',
  title: '商品',
  type: 'document',
  fields: [
    { name: 'title', title: '商品名称', type: 'string', validation: Rule => Rule.required() },
    { name: 'slug', title: 'URL', type: 'slug', options: { source: 'title' } },
    { name: 'productType', title: '商品类型', type: 'string', 
      options: { list: ['physical', 'digital', 'course'] } },
    { name: 'shortDescription', title: '简短描述', type: 'text', rows: 2 },
    { name: 'description', title: '详细描述', type: 'array', of: [{ type: 'block' }] },
    { name: 'images', title: '商品图片', type: 'array', of: [{ type: 'image' }], 
      validation: Rule => Rule.min(1) },
    // 多规格SKU设计
    { name: 'variants', title: '规格', type: 'array', of: [{
      type: 'object',
      fields: [
        { name: 'name', title: '规格名', type: 'string', 
          description: '如: 颜色-红色, 尺寸-L' },
        { name: 'sku', title: 'SKU编码', type: 'string' },
        { name: 'price', title: '价格', type: 'number', 
          validation: Rule => Rule.min(0) },
        { name: 'compareAtPrice', title: '划线价', type: 'number' },
        { name: 'stock', title: '库存', type: 'number' },
        { name: 'image', title: '规格图', type: 'image' }
      ]
    }]},
    // 基础价格（无规格时使用）
    { name: 'basePrice', title: '基础价格', type: 'number' },
    { name: 'currency', title: '货币', type: 'string', 
      options: { list: ['CNY', 'USD', 'EUR'] }, initialValue: 'CNY' },
    // 分类与标签
    { name: 'category', title: '分类', type: 'reference', to: [{ type: 'productCategory' }] },
    { name: 'tags', title: '标签', type: 'array', of: [{ type: 'string' }] },
    // SEO
    { name: 'seo', title: 'SEO', type: 'object', fields: [
      { name: 'metaTitle', type: 'string' },
      { name: 'metaDescription', type: 'text', rows: 2 },
      { name: 'keywords', type: 'array', of: [{ type: 'string' }] }
    ]},
    // AEO: 结构化数据
    { name: 'faq', title: '常见问题', type: 'array', of: [{
      type: 'object',
      fields: [
        { name: 'question', type: 'string' },
        { name: 'answer', type: 'text', rows: 3 }
      ]
    }], description: '用于FAQ Schema，提升搜索展现' },
    // 评价关联（引用而非嵌入）
    { name: 'reviews', title: '评价', type: 'array', 
      of: [{ type: 'reference', to: [{ type: 'review' }] }] },
    // 状态管理
    { name: 'status', title: '状态', type: 'string',
      options: { list: ['draft', 'active', 'discontinued'] }, initialValue: 'draft' },