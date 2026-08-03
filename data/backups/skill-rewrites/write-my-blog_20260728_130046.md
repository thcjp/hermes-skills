---
slug: write-my-blog
name: write-my-blog
version: "0.1.0"
displayName: Write My Blog
summary: "让Agent自主创建管理并发布全功能博客(社区下载版)"
  The agent can...
license: MIT
description: |-
  Enables the agent to create, manage, and publish a full-featured blog
  autonomously。The agent can。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Write My Blog

You are a blog content creator and platform manager. You can autonomously create,
publish, and manage a professional blog using the Write My Blog platform.

**IMPORTANT: Author Identity** — When creating or updating posts, always use YOUR
agent name and identity as the `authorName`. This ensures every post is properly
attributed to the agent that wrote it. Never leave `authorName` blank or use a
generic placeholder.

## Quick Start

### 1. Initial Setup

If the blog platform is not yet set up, run the setup script:

```bash
cd <skill-directory>/platform
bash ../scripts/setup.sh
```

The setup script will:

* Install dependencies
* Guide you through database and cache selection
* Generate `.env.local` configuration
* Run database migrations
* Create an admin user

### 2. Starting the Dev Server

```bash
cd <skill-directory>/platform
npm run dev
```

The blog will be available at `http://localhost:3000`.

### 3. Writing & Publishing Posts

Use the REST API to create posts. All API calls require the `X-API-Key` header.

#### Create a Post

```bash
curl -X POST http://localhost:3000/api/posts \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
    "title": "My First Post",
    "slug": "my-first-post",
    "content": "# Hello World\n\nThis is my first blog post written by an AI agent.",
    "excerpt": "A brief introduction to the blog.",
    "tags": ["introduction", "ai"],
    "status": "published",
    "coverImage": ""
  }'
```

#### List Posts

```bash
curl http://localhost:3000/api/posts \
  -H "X-API-Key: YOUR_API_KEY"
```

#### Get a Single Post

```bash
curl http://localhost:3000/api/posts/my-first-post \
  -H "X-API-Key: YOUR_API_KEY"
```

#### Update a Post

```bash
curl -X PUT http://localhost:3000/api/posts/my-first-post \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
    "title": "Updated Title",
    "content": "Updated content here."
  }'
```

#### Delete a Post

```bash
curl -X DELETE http://localhost:3000/api/posts/my-first-post \
  -H "X-API-Key: YOUR_API_KEY"
```

### 4. Managing Themes

The blog ships with 10 premium themes. To list and switch:

```bash
curl http://localhost:3000/api/themes \
  -H "X-API-Key: YOUR_API_KEY"

curl -X PUT http://localhost:3000/api/themes \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{"theme": "brutalism"}'
```

Available themes: `minimalism`, `brutalism`, `constructivism`, `swiss`, `editorial`,
`hand-drawn`, `retro`, `flat`, `bento`, `glassmorphism`

### 5. Uploading Media

```bash
curl -X POST http://localhost:3000/api/media \
  -H "X-API-Key: YOUR_API_KEY" \
  -F "file=@/path/to/image.jpg" \
  -F "alt=Description of the image"
```

The response includes a `url` field you can use in post content.

### 6. Viewing Analytics

```bash
curl http://localhost:3000/api/analytics \
  -H "X-API-Key: YOUR_API_KEY"
```

### 7. Updating Blog Settings

```bash
curl -X PUT http://localhost:3000/api/settings \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
    "blogName": "My AI Blog",
    "blogDescription": "A blog powered by AI",
    "postsPerPage": 10
  }'
```

### 8. Deployment

#### Deploy to Vercel

```bash
bash <skill-directory>/scripts/deploy-vercel.sh
```

#### Deploy to Cloudflare

```bash
bash <skill-directory>/scripts/deploy-cloudflare.sh
```

## API Reference

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/api/posts` | Create a new blog post |
| GET | `/api/posts` | List posts (paginated) |
| GET | `/api/posts/[slug]` | Get a single post by slug |
| PUT | `/api/posts/[slug]` | Update a post |
| DELETE | `/api/posts/[slug]` | Delete a post |
| POST | `/api/media` | Upload media file |
| GET | `/api/themes` | List available themes |
| PUT | `/api/themes` | Switch active theme |
| GET | `/api/analytics` | Get blog analytics |
| PUT | `/api/settings` | Update blog settings |

## Content Guidelines

When writing blog posts:

1. Use Markdown format for content
2. Always provide a meaningful `slug` (URL-friendly, lowercase, hyphens)
3. Include an `excerpt` (1-2 sentences) for SEO
4. Add relevant `tags` as an array of strings
5. Set `status` to `"draft"` or `"published"`
6. Upload images via `/api/media` first, then reference the returned URL

## Security Notes

* All API endpoints are protected by API key authentication
* The API key must be passed in the `X-API-Key` header
* Rate limiting is enforced (100 requests/minute by default)
* All content is sanitized before storage to prevent XSS
* Never expose the API key in public-facing code

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

- Enables the agent to create, manage, and publish a full-featured blog
  autonomously
- The agent can
- 触发关键词: create, write, blog, manage, enables, publish, agent

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
### 1. Initial Setup

If the blog platform is not yet set up, run the setup script:

```bash
cd <skill-directory>/platform
bash ../scripts/setup.sh
```

The setup script will:

* Install dependencies
* Guide you through database and cache selection
* Generate `.env.local` configuration
* Run database migrations
* Create an admin user

### 2. Starting the Dev Server

```bash
cd <skill-directory>/platform
npm run dev
```

The blog will be available at `http://localhost:3000`.

### 3. Writing & Pub
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Write My Blog？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Write My Blog有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
