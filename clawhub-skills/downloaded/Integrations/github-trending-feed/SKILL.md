---
slug: github-trending-feed
name: github-trending-feed
version: "1.0.0"
displayName: GitHub Trending Feed
summary: 获取 GitHub Trending 热门仓库列表。当用户要求查看 GitHub 热榜、每日 GitHub trending、推送 GitHub
  热门项目时使用。支持可选语言过滤，返回结构化 J...
license: MIT-0
description: |-
  获取 GitHub Trending 热门仓库列表。当用户要求查看 GitHub 热榜、每日 GitHub trending、推送 GitHub
  热门项目时使用。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# GitHub Trending Feed

## Overview

The GitHub Trending Feed skill is a powerful tool for developers and teams looking to stay on top of the latest and most popular projects on GitHub. By integrating this skill into your workflow, you can receive real-time updates on trending repositories, enabling you to make informed decisions and stay ahead of the curve.

## Features

- **Real-time Trending Repositories**: Fetch the most popular repositories from GitHub as they appear on the Trending page.
- **Language Filtering**: Filter repositories by programming language to focus on the projects that matter to you.
- **Structured JSON Output**: Receive the repository details in a structured JSON format, making it easy to integrate with other tools and platforms.
- **Automated Workflows**: Use the skill in conjunction with automation tools to create custom workflows that trigger when new trending repositories are identified.

## Workflow

1. **Fetch Trending Repositories**: The skill retrieves the list of trending repositories from GitHub.
2. **Language Filtering (Optional)**: Apply language filters to narrow down the list to repositories in your preferred programming language.
3. **JSON Output**: The skill returns the filtered list of repositories in a structured JSON format.
4. **Integration**: Use the JSON output to integrate trending repositories into your application, dashboard, or notification system.

## Usage

### Basic Usage

```bash
python3 ~/.skill-platform/workspace/skills/github-trending/scripts/fetch_trending.py
```

### Language Filtering

```bash
python3 ~/.skill-platform/workspace/skills/github-trending/scripts/fetch_trending.py python
python3 ~/.skill-platform/workspace/skills/github-trending/scripts/fetch_trending.py javascript
```

### Output Format

The skill returns a JSON array with each element representing a repository:

```json
[
  {
    "full_name": "owner/repo",
    "description": "Repository description",
    "language": "Python",
    "stars": 12345,
    "url": "https://github.com/owner/repo"
  }
  // ... more repositories
]
```

## Agent Integration

After fetching the data, you can format the output according to your platform:

**Feishu (飞书)**:

```text
📊 **GitHub Trending · 今日热榜**
🔥 1. owner/repo - 描述 ⭐ 12345 | Python 🔗 https://github.com/owner/repo
```

**Discord/Telegram**:

```text
📊 GitHub Trending 今日热榜
1. owner/repo - 描述 ⭐ 12345 | Python | https://github.com/owner/repo
```

**Console**:

```text
1. owner/repo (⭐ 12345 | Python)
   描述
   https://github.com/owner/repo
```

## Considerations

- **GitHub API Rate Limits**: Be mindful of the GitHub API rate limits to avoid being blocked. Consider implementing caching if you plan to fetch data frequently.
- **Error Handling**: The skill automatically handles API errors and provides fallback data in case of failures.
- **Default Output**: By default, the skill returns the top 9 repositories. When using language filtering, it returns the top 10 repositories.

## Dependencies

### Environment

- **Agent Platform**: Supports any SKILL.md AI Agent (Claude Code, Cursor, Codex, Gemini CLI, etc.).
- **Operating System**: Windows, macOS, Linux.

### Dependencies

| Dependency | Type | Required | Source |
|------------|------|----------|--------|
| LLM API | API | Required | Provided by the Agent's built-in LLM |

### API Key Configuration

- This skill uses Markdown instructions and does not require an additional API key unless specified for external APIs.

### Usability Classification

- **Category**: MD+EXEC (Markdown instructions with some exec command-line capabilities)
- **Description**: A Markdown-based AI Skill that drives Agent tasks through natural language commands.

## Core Capabilities

- Fetch GitHub Trending repositories list
- View GitHub hotlists, daily trending, and GitHub trending projects
- Optional language filtering
- Structured JSON output

## Use Cases

| Scenario | Input | Output |
|----------|-------|--------|
| Basic Use | User request | Processed result |

**Not Suitable for**: Complex decision-making scenarios requiring human judgment.

## Examples

### Example 1: Basic Usage

1. Fetch the Trending page to get the GitHub trending repository list.
2. Fetch repository details by calling the GitHub REST API for description, stars, and language.
3. Return the JSON formatted message to the target platform.

## Error Handling

| Error Scenario | Reason | Resolution |
|----------------|--------|------------|
| Configuration Error | Missing or incorrectly formatted parameters | Check the dependency requirements in the documentation. |
| Runtime Error | Inadequate runtime environment | Confirm that the runtime environment meets the requirements. |
| Network Error | Connection timeout or unreachability | Check network connection and retry, or consider alternative solutions. |

## Common Questions

### Q1: How do I start using GitHub Trending Feed?
A: Please refer to the Usage section to ensure your environment meets the requirements outlined in the Dependency section.

### Q2: What should I do if I encounter an error?
A: Refer to the Error Handling section for steps on how to resolve common issues.

### Q3: What are the limitations of GitHub Trending Feed?
A: Refer to the Known Limitations section for more information on the skill's constraints.