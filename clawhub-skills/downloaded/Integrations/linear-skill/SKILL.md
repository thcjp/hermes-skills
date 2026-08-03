---
slug: linear-skill
name: linear-skill
version: "1.0.0"
displayName: Linear
summary: "经内置Node CLI与Linear API管项目/issue/任务(社区下载版)"
  official Linear API. U...
license: MIT
description: |-
  Manage Linear projects, issues, and tasks via the bundled Node CLI and
  the official Linear API。U。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

# Linear Workflow Management

Linear provides a comprehensive solution for managing projects, issues, and tasks. This document outlines how to effectively use Linear through its Node CLI and official API.

## Overview

Linear is designed to streamline project management processes, making it easier to plan, track, and collaborate on tasks. The Linear skill integrates with the Linear API, allowing users to manage their projects and issues directly from the command line.

## Installation and Setup

### Prerequisites

1. **Node.js and npm**: Ensure you have Node.js and npm installed on your system.
2. **Linear API Key**: Obtain your Linear API key from your Linear account settings.

### Installation Steps

1. Clone the Linear skill repository to your local machine.
2. Navigate to the repository directory and install dependencies:
   ```bash
   cd {baseDir}/scripts && npm install
   ```
3. Set your Linear API key in the local environment:
   ```bash
   export LINEAR_API_KEY="[REDACTED]"
   ```

## Authentication and Credentials

- **Credential**: `LINEAR_API_KEY`
- **Obtaining API Key**: Access your Linear account settings at `https://linear.app/settings/api` to generate a new API key.
- **Access Level**: Use a least-privilege access token for automation to ensure security.

## Core Functionality

### Commands Overview

- **Teams and Projects**: Manage teams and projects with commands like `teams`, `projects`, and `createProject`.
- **Issues**: Create, update, and manage issues with `issues`, `createIssue`, and `updateIssue`.
- **Comments**: Add comments to issues using `createComment`.
- **States and Labels**: Manage states and labels with `states` and `labels`.
- **Users**: Retrieve information about users with `user`.

### Workflow Steps

1. **Clarify Intent and Scope**: Define the team/project, labels, cycle, assignee, due date, and priority.
2. **Read Current State**: List or get issues, projects, statuses, labels, users, and cycles.
3. **Apply Mutations**: Create or update issues, comments, projects, milestones, and labels.
4. **Summarize Changes**: Document the changes made, including IDs, states, assignees, blockers, and follow-up actions.

## Practical Workflows

- **Triage Urgent Bugs**: List high-priority open issues, assign owners, move state to 'In Progress', and add triage comments.
- **Sprint Planning**: Review cycle scope, create missing issues, set priorities and estimates, and align assignees.
- **Release Prep**: Verify blockers, update project status, create milestone tasks, and add rollout comments.
- **Documentation Cleanup**: Find stale docs/issue, open follow-up tasks, and link related records.

## Safety and Operational Rules

- **ID Management**: Never invent IDs; fetch and confirm before updates.
- **Narrow Updates**: Prefer narrow updates over broad bulk edits.
- **Bulk Edits**: Explain grouping logic before applying changes.
- **Secrets**: Do not include secrets in issue comments or descriptions.
- **API Scope**: Do not send data to endpoints outside Linear API scope.

## Command Examples

```bash
node {baseDir}/scripts/linear-cli.js teams
node {baseDir}/scripts/linear-cli.js projects
node {baseDir}/scripts/linear-cli.js issues
node {baseDir}/scripts/linear-cli.js issue ENG-123
node {baseDir}/scripts/linear-cli.js createIssue "Title" "Description" "team-id" '{"priority":2}'
node {baseDir}/scripts/linear-cli.js updateIssue "issue-id" '{"stateId":"state-id"}'
```

## Error Handling

### Common Errors

- **Configuration Errors**: Check the dependencies and ensure the `LINEAR_API_KEY` is set correctly.
- **Runtime Errors**: Verify the runtime environment meets the requirements.
- **Network Errors**: Check your network connection and try again.

### Troubleshooting

- **Configuration Issues**: Review the setup instructions and ensure all prerequisites are met.
- **Dependency Issues**: Reinstall dependencies or check for package compatibility.
- **API Key Issues**: Ensure the API key is valid and has the necessary permissions.

## Security Considerations

- **API Key Security**: Keep your API key secure and do not share it with unauthorized users.
- **Least Privilege Access**: Use a dedicated token with the least privilege access for automation.

## Conclusion

Linear is a powerful tool for managing projects, issues, and tasks. By following this guide, users can effectively leverage the Linear skill to streamline their project management processes and enhance team collaboration.