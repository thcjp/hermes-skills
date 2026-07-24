---
slug: "write-my-blog"
name: "write-my-blog"
version: 0.1.1
displayName: "Write My Blog"
summary: "让Agent自主创建管理并发布全功能博客。Enables the agent to create, manage, and publish a full-featured blog auto"
license: "Proprietary"
description: |-
  Enables the agent to create, manage, and publish a full-featured blog
  autonomously。The agent can。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估.
tags:
  - Integrations
  - 工具
  - 效率
  - 自动化
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# Write My Blog

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Write My Blog让Agent自主创建 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

- Enables the agent to create, manage, and publish a full-featured blog
  autonomously
- The agent can
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 管理操作 | 操作目标与参数 | 操作结果与状态变更 |
| 让Agent自主创建 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 1. Initial Setup

If the blog platform is not yet set up, run the setup script:

```bash
cd <skill-directory>/platform
bash .（请参考skill目录中的脚本文件）
```

The setup script will:

1. Install dependencies
2. Guide you through database and cache selection
3. Generate `.env.local` configuration
4. Run database migrations
5. Create an admin user

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
# ...
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
bash <skill-directory>/（请参考skill目录中的脚本文件）
```

#### Deploy to Cloudflare

```bash
bash <skill-directory>/（请参考skill目录中的脚本文件）
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | write-my-blog处理的内容输入 |, 默认: 全部维度 |
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
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 示例1：基础用法

```
### 1. Initial Setup(补充)
# ...
If the blog platform is not yet set up, run the setup script:
# ...
```bash
cd <skill-directory>/platform
bash .（请参考skill目录中的脚本文件）
```
# ...
The setup script will:
# ...
* Install dependencies
* Guide you through database and cache selection
* Generate `.env.local` configuration
* Run database migrations
* Create an admin user
# ...
### 2. Starting the Dev Server(补充)
# ...
```bash
cd <skill-directory>/platform
npm run dev
```
# ...
The blog will be available at `http://localhost:3000`.
# ...
### 3. Writing & Pub
```

## 常见问题

### Q1: 如何开始使用Write My Blog？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
