---
slug: job-auto-apply
name: job-auto-apply
version: "1.0.0"
displayName: Job Auto Apply
summary: This skill fits its job-application automation purpose, but it gives an agent
  authority to submit...
license: MIT
description: |-
  This skill fits its job-application automation purpose, but it gives
  an agent authority to submit。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
- Research
tools:
  - - read
- exec
---

# Job Auto Apply

Automate job searching and application submission across multiple job platforms using Clawdbot.

## Overview

This skill enables automated job search and application workflows. It searches for jobs matching user criteria, analyzes compatibility, generates tailored cover letters, and submits applications automatically or with user confirmation.

**Supported Platforms:**

* LinkedIn (including Easy Apply)
* Indeed
* Glassdoor
* ZipRecruiter
* Wellfound (AngelList)

## Quick Start

### 1. Set Up User Profile

First, create a user profile using the template:

```bash
cp profile_template.json ~/job_profile.json

```

### 2. Run Job Search and Apply

```bash
python job_search_apply.py \
  --title "Software Engineer" \
  --location "San Francisco, CA" \
  --remote \
  --max-applications 10 \
  --dry-run

python job_search_apply.py \
  --profile ~/job_profile.json \
  --title "Backend Engineer" \
  --platforms linkedin,indeed \
  --auto-apply

python job_search_apply.py \
  --profile ~/job_profile.json \
  --title "Senior Developer" \
  --no-dry-run \
  --require-confirmation
```

## Workflow Steps

### Step 1: Profile Configuration

Load the user's profile from the template or create programmatically:

```python
from job_search_apply import ApplicantProfile

profile = ApplicantProfile(
    full_name="Jane Doe",
    email="jane@example.com",
    phone="+1234567890",
    resume_path="~/Documents/resume.pdf",
    linkedin_url="https://linkedin.com/in/janedoe",
    years_experience=5,
    authorized_to_work=True,
    requires_sponsorship=False
)
```

### Step 2: Define Search Parameters

```python
from job_search_apply import JobSearchParams, JobPlatform

search_params = JobSearchParams(
    title="Software Engineer",
    location="Remote",
    remote=True,
    experience_level="mid",
    job_type="full-time",
    salary_min=100000,
    platforms=[JobPlatform.LINKEDIN, JobPlatform.INDEED]
)
```

### Step 3: Run Automated Application

```python
from job_search_apply import auto_apply_workflow

results = auto_apply_workflow(
    search_params=search_params,
    profile=profile,
    max_applications=10,
    min_match_score=0.75,
    dry_run=False,
    require_confirmation=True
)
```

## Integration with Clawdbot

### Using as a Clawdbot Tool

When installed as a Clawdbot skill, invoke via natural language:

**Example prompts:**

* "Find and apply to Python developer jobs in San Francisco"
* "Search for remote backend engineer positions and apply to the top 5 matches"
* "Auto-apply to senior software engineer roles with 100k+ salary"
* "Apply to jobs at tech startups on Wellfound"

The skill will:

1. Parse the user's intent and extract search parameters
2. Load the user's profile from saved configuration
3. Search across specified platforms
4. Analyze job compatibility
5. Generate tailored cover letters
6. Submit applications (with confirmation if enabled)
7. Report results and track applications

### Configuration in Clawdbot

Add to your Clawdbot configuration:

```json
{
  "skills": {
    "job-auto-apply": {
      "enabled": true,
      "profile_path": "~/job_profile.json",
      "default_platforms": ["linkedin", "indeed"],
      "max_daily_applications": 10,
      "require_confirmation": true,
      "dry_run": false
    }
  }
}
```

## Features

### 1. Multi-Platform Search

* Searches across all major job platforms
* Uses official APIs when available
* Falls back to web scraping for platforms without APIs

### 2. Smart Matching

* Analyzes job descriptions for requirement matching
* Calculates compatibility scores
* Filters jobs based on minimum match threshold

### 3. Application Customization

* Generates tailored cover letters per job
* Customizes resume emphasis based on job requirements
* Handles platform-specific application forms

### 核心能力

* **Dry Run Mode**: Test without submitting applications
* **Manual Confirmation**: Review each application before submission
* **Rate Limiting**: Prevents overwhelming platforms
* **Application Logging**: Tracks all submissions for reference

### 5. Form Automation

Automatically fills common application fields:

* Personal information
* Work authorization status
* Education and experience
* Skills and certifications
* Screening questions (using AI when needed)

## Advanced Usage

### Custom Cover Letter Templates

Create a template with placeholders:

```text
Dear Hiring Manager at {company},

I am excited to apply for the {position} role. With {years} years of
experience in {skills}, I believe I would be an excellent fit.

{custom_paragraph}

I look forward to discussing how I can contribute to {company}'s success.

Best regards,
{name}
```

### Application Tracking

Results are automatically saved in JSON format with details on each application submitted, including timestamps, match scores, and status.

## Bundled Resources

### Scripts

* `job_search_apply.py` - Main automation script with search, matching, and application logic

### References

* `platform_integration.md` - Technical documentation for API integration, web scraping, form automation, and platform-specific details

### Assets

* `profile_template.json` - Comprehensive profile template with all required and optional fields

## Safety and Ethics

### Important Guidelines

1. **Truthfulness**: Never misrepresent qualifications or experience
2. **Genuine Interest**: Only apply to jobs you're actually interested in
3. **Rate Limiting**: Respect platform limits and terms of service
4. **Manual Review**: Consider enabling confirmation mode for quality control
5. **Privacy**: Secure storage of personal information and credentials

### Best Practices

* Start with dry-run mode to verify behavior
* Set reasonable limits (5-10 applications per day)
* Use high match score thresholds (0.75+)
* Enable confirmation for important applications
* Track results to optimize strategy

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

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
### 1. Set Up User Profile

First, create a user profile using the template:

```bash
cp profile_template.json ~/job_profile.json

```

### 2. Run Job Search and Apply

```bash
python job_search_apply.py \
  --title "Software Engineer" \
  --location "San Francisco, CA" \
  --remote \
  --max-applications 10 \
  --dry-run

python job_search_apply.py \
  --profile ~/job_profile.json \
  --title "Backend Engineer" \
  --platforms linkedin,indeed \
  --auto-apply

python job_search_apply.py \
  --p
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Job Auto Apply？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Job Auto Apply有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
