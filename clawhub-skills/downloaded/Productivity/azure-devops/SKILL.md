---
slug: azure-devops
name: azure-devops
version: "1.0.0"
displayName: Azure DevOps
summary: "管理Azure DevOps项目、仓库、分支,创建PR与工作项,提升研发协作效率"
  manage work items; ...
license: MIT
description: |-
  List Azure DevOps projects, repositories, and branches; create pull
  requests; manage work items; 。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Productivity
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Azure DevOps

List projects, repositories, branches. Create pull requests. Manage work items. Check build status.

## Check before running for valid Configuration, if values missing ask the user!

**Required:**

* `AZURE_DEVOPS_PAT`: Personal Access Token
* `AZURE_DEVOPS_ORG`: Organization name

**If values are missing from `~/.skill-platform/skill-platform.json`, the agent should:**

1. **ASK** the user for the missing PAT and/or organization name
2. Store them in `~/.skill-platform/skill-platform.json` under `skills.entries["azure-devops"]`

### 示例

json5

```
{
  skills: {
    entries: {
      "azure-devops": {
        apiKey: "YOUR_PERSONAL_ACCESS_TOKEN",  // AZURE_DEVOPS_PAT
        env: {
          AZURE_DEVOPS_ORG: "YourOrganizationName"
        }
      }
    }
  }
}
```

## Commands

### List Projects

```bash
curl -s -u ":${AZURE_DEVOPS_PAT}" \
  "https://dev.azure.com/${AZURE_DEVOPS_ORG}/_apis/projects?api-version=7.1" \
  | jq -r '.value[] | "(.name) - (.description // "No description")"'
```

### List Repositories in a Project

```bash
PROJECT="YourProject"
curl -s -u ":${AZURE_DEVOPS_PAT}" \
  "https://dev.azure.com/${AZURE_DEVOPS_ORG}/${PROJECT}/_apis/git/repositories?api-version=7.1" \
  | jq -r '.value[] | "(.name) - (.webUrl)"'
```

### List Branches in a Repository

```bash
PROJECT="YourProject"
REPO="YourRepo"
curl -s -u ":${AZURE_DEVOPS_PAT}" \
  "https://dev.azure.com/${AZURE_DEVOPS_ORG}/${PROJECT}/_apis/git/repositories/${REPO}/refs?filter=heads/&api-version=7.1" \
  | jq -r '.value[] | .name | sub("refs/heads/"; "")'
```

### Create a Pull Request

```bash
PROJECT="YourProject"
REPO_ID="repo-id-here"
SOURCE_BRANCH="feature/my-branch"
TARGET_BRANCH="main"
TITLE="PR Title"
DESCRIPTION="PR Description"

curl -s -u ":${AZURE_DEVOPS_PAT}" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "sourceRefName": "refs/heads/'"${SOURCE_BRANCH}"'",
    "targetRefName": "refs/heads/'"${TARGET_BRANCH}"'",
    "title": "'"${TITLE}"'",
    "description": "'"${DESCRIPTION}"'"
  }' \
  "https://dev.azure.com/${AZURE_DEVOPS_ORG}/${PROJECT}/_apis/git/repositories/${REPO_ID}/pullrequests?api-version=7.1"
```

### Get Repository ID

```bash
PROJECT="YourProject"
REPO_NAME="YourRepo"
curl -s -u ":${AZURE_DEVOPS_PAT}" \
  "https://dev.azure.com/${AZURE_DEVOPS_ORG}/${PROJECT}/_apis/git/repositories/${REPO_NAME}?api-version=7.1" \
  | jq -r '.id'
```

### List Pull Requests

```bash
PROJECT="YourProject"
REPO_ID="repo-id"
curl -s -u ":${AZURE_DEVOPS_PAT}" \
  "https://dev.azure.com/${AZURE_DEVOPS_ORG}/${PROJECT}/_apis/git/repositories/${REPO_ID}/pullrequests?api-version=7.1" \
  | jq -r '.value[] | "#(.pullRequestId): (.title) [(.sourceRefName | sub("refs/heads/"; ""))] -> [(.targetRefName | sub("refs/heads/"; ""))] - (.createdBy.displayName)"'
```

## Notes

* Base URL: `https://dev.azure.com/${AZURE_DEVOPS_ORG}`
* API Version: `7.1`
* Auth: Basic Auth with empty username and PAT as password
* Never log or expose the PAT in responses
* Documentation: <https://learn.microsoft.com/en-us/rest/api/azure/devops/>

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

- List Azure DevOps projects, repositories, and branches
- create pull
  requests
- manage work items
- 触发关键词: devops, list, azure, projects, repositories

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

### Q1: 如何开始使用Azure DevOps？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Azure DevOps有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 依赖云服务，需要网络连接
