---
slug: mongodb-atlas-admin
name: mongodb-atlas-admin
version: "1.0.0"
displayName: MongoDB Atlas
summary: browse MongoDB Atlas Admin API specifications and execute operations (if
  credentials provided).
license: MIT
description: |-
  browse MongoDB Atlas Admin API specifications and execute operations
  (if credentials provided).

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: specifications, atlas, mongodb, admin, browse
tags:
- Integrations
tools:
- read
- exec
---

# MongoDB Atlas

Tool to browse OpenAPI specifications for MongoDB Atlas.
**Note:** If `ATLAS_CLIENT_ID` and `ATLAS_CLIENT_SECRET` are configured in the environment, this tool can also execute live API calls. Without credentials, it functions as a read-only documentation browser.

## Commands

### 1. List API Catalog

List all available API categories or filter by keyword.

```bash
node {baseDir}/scripts/atlas-api.mjs catalog # list all categories
node {baseDir}/scripts/atlas-api.mjs catalog Clusters
```

### 2. Get API Details

Get full endpoint definition (method, path, params) for a specific Operation ID.

```bash
node {baseDir}/scripts/atlas-api.mjs detail listClusterDetails
```

### 3. Get Schema Definition

Get the data model schema for complex types.

```bash
node {baseDir}/scripts/atlas-api.mjs schema "#/components/schemas/ApiError"
```

### 4. Execute Live API Calls

Execute real HTTP requests against the Atlas API.

**Script:** `node {baseDir}/scripts/atlas-call.mjs <METHOD> <ENDPOINT> [flags]`

#### ⚠️ Mandatory Safety Protocol

**For any state-changing operation (POST, PUT, PATCH, DELETE):**

1. **STOP & REVIEW**: You MUST NOT execute the command immediately.
2. **PREVIEW**: Use `--dry-run` first to verify the payload and endpoint.
3. **CONFIRM**: Display the full command and JSON body to the user.
4. **EXECUTE**: Only run with `--yes` after receiving explicit user approval.

#### Usage Examples

**1. Read-Only (Safe)**

```bash
node {baseDir}/scripts/atlas-call.mjs GET groups/{groupId}/clusters
```

**2. Create/Modify (RISKY - Require Approval)**

```bash
node {baseDir}/scripts/atlas-call.mjs POST groups/{groupId}/clusters \
  --data '{"name":"DemoCluster", "providerSettings":{...}}' \
  --dry-run
```

#### Options

* `-d, --data <json>`: Request body string (ensure proper JSON escaping).
* `-p, --params <json>`: Query parameters.
* `--dry-run`: Print the request details without executing (Recommended for verification).
* `--yes`: Skip interactive confirmation (Use CAREFULLY).

#### Environment

Requires `ATLAS_CLIENT_ID` and `ATLAS_CLIENT_SECRET` to be set.

## Core Categories

(Use `catalog` command to see the full list of 50+ categories)

* **Clusters** / **Cloud Backups**
* **Projects** / **Organizations**
* **Database Users** / **Custom Database Roles**
* **Alerts** / **Alert Configurations**
* **Monitoring and Logs** / **Events**
* **Network Peering** / **Private Endpoint Services**
* **Serverless Instances**
* **Access Tracking** / **Auditing**

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
