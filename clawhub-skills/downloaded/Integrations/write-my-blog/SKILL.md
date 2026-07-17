---
slug: write-my-blog
name: write-my-blog
version: "0.1.0"
displayName: Write My Blog
summary: Enables the agent to create, manage, and publish a full-featured blog autonomously.
  The agent can...
license: MIT
description: |-
  Enables the agent to create, manage, and publish a full-featured blog
  autonomously. The agent can...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: create, write, blog, manage, enables, publish, agent
tags:
- Integrations
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
