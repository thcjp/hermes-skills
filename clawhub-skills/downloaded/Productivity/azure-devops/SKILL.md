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

## 增强功能列表与边界条件

为了增强功能完整性，我们将详细列出所有功能，并特别强调边界条件处理。例如，对于API版本选择，我们将解释为什么选择7.1版本，以及未来可能升级到更高版本的原因。以下是详细的功能列表和边界条件处理：

- **项目列表**：支持列出所有项目，包括项目名称和描述。边界条件包括处理无项目或项目列表为空的情况。
- **仓库列表**：支持列出指定项目下的所有仓库，包括仓库名称和Web URL。边界条件包括处理无仓库或仓库列表为空的情况。
- **分支列表**：支持列出指定仓库的所有分支。边界条件包括处理无分支或分支列表为空的情况。
- **创建PR**：支持创建新的Pull Request，包括设置源分支、目标分支、标题和描述。边界条件包括处理分支不存在或PR创建失败的情况。
- **获取仓库ID**：支持根据仓库名称获取其ID。边界条件包括处理仓库不存在的情况。
- **列表PR**：支持列出指定仓库的所有PR，包括PR ID、标题、源分支、目标分支和创建者。边界条件包括处理PR列表为空的情况。

我们将确保所有功能都有明确的错误处理机制，并在文档中详细说明。

## 增强输入输出参数说明

为了提高易用性，我们将详细说明每个命令的输入输出参数，包括默认值、类型和取值范围。例如，对于创建PR的命令，我们将详细说明以下参数：

- `sourceRefName`：源分支名称，类型为字符串，必须提供。
- `targetRefName`：目标分支名称，类型为字符串，必须提供。
- `title`：PR标题，类型为字符串，必须提供。
- `description`：PR描述，类型为字符串，可选。

我们将为每个参数提供示例，并说明其作用和限制。

## 增强错误码定义和处理方案

为了帮助用户更好地理解和使用Azure DevOps，我们将定义常见的错误码，并提供相应的处理方案。例如，对于错误码401（未授权），我们将解释其含义，并提供以下处理方案：

- 确认Personal Access Token是否有效。
- 检查组织名称是否正确。
- 确认用户是否有权限访问所需资源。

我们将为每个错误码提供详细的说明和处理步骤。

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

## 差异化优势分析

Azure DevOps在同类方案中具有以下差异化优势：

- **集成性**：与Azure DevOps服务深度集成，提供无缝的体验。
- **自动化**：支持自动化工作流，提高研发效率。
- **灵活性**：支持多种配置和定制，满足不同团队的需求。

我们将通过具体的案例和用户反馈来展示这些优势，并与其他同类方案进行对比。

## 解决的真实验证痛点

Azure DevOps解决了以下真实验证痛点：

- **提高研发效率**：通过自动化和集成，减少手动操作，提高研发效率。
- **增强团队协作**：提供统一的平台，方便团队成员之间的沟通和协作。
- **简化项目管理**：提供项目管理工具，帮助团队更好地规划和管理项目。

我们将通过用户案例和成功故事来展示这些痛点是如何被解决的。
