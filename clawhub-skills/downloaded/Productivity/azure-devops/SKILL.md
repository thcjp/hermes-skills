---
slug: azure-devops
name: azure-devops
version: "1.0.0"
displayName: Azure DevOps
summary: List Azure DevOps projects, repositories, and branches; create pull requests;
  manage work items; ...
license: MIT
description: |-
  List Azure DevOps projects, repositories, and branches; create pull
  requests; manage work items; ...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: devops, list, azure, projects, repositories
tags:
- Productivity
tools:
- read
- exec
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

### Example Config

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
