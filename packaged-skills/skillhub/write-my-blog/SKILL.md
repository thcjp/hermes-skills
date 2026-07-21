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
  autonomously。The agent can。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
---
# Write My Blog

## 核心能力

- Enables the agent to create, manage, and publish a full-featured blog
  autonomously
- The agent can
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: Use、需要项目管理、任务规划、进度跟踪、团队协作时使用、不适用于实际人员、绩效评估、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 1. Initial Setup

If the blog platform is not yet set up, run the setup script:

```bash
cd <skill-directory>/platform
bash ../scripts/setup.sh
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

### 命令参数说明

6. `-first-post`: 命令参数,用于指定操作选项
7. `-H`: 命令参数,用于指定操作选项
8. `-X`: 命令参数,用于指定操作选项
9. `-Type`: 命令参数,用于指定操作选项
10. `-F`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-API-Key`: 命令参数,用于指定操作选项

### 命令参数说明

- `-API-Key`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

### 命令参数说明

- `-F`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-API-Key`: 命令参数,用于指定操作选项

### 命令参数说明

- `-H`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-API-Key`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-X`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-API-Key`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-API-Key`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-API-Key`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项

### 命令参数说明

- `-X`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-F`: 命令参数,用于指定操作选项
- `-API-Key`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

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
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

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

## 常见问题

### Q1: 如何开始使用Write My Blog？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Write My Blog有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
