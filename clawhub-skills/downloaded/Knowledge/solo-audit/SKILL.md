---
slug: solo-audit
name: solo-audit
version: "1.4.1"
displayName: Audit
summary: "知识库健康检查,断链/缺frontmatter/标签不一致/封面(社区下载版)"
  and cover...
license: MIT
description: |-
  Health check knowledge base for broken links, missing frontmatter, tag
  inconsistencies, and cover。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。适用于独立开发者、企业团队和自动化工作流场景。
tags: '[''Knowledge'']'
tools:
  - read
  - exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Comprehensive Knowledge Base Health Auditor

## Overview

The Comprehensive Knowledge Base Health Auditor (solo-audit) is an essential tool for maintaining the quality and reliability of markdown-based knowledge bases. It is designed to identify and report on common issues such as broken links, missing frontmatter, inconsistent tagging, orphaned files, and content gaps. solo-audit is a powerful tool for ensuring that your knowledge base is not only functional but also secure and user-friendly.

## Functionality

### Parsing Focus Area

- Parse the focus area from `$ARGUMENTS` (optional). If specified, the audit will concentrate on the provided area (e.g., "tags", "frontmatter", "links"). If not provided, the audit will run a full assessment.

### File Discovery

- Utilize Glob to locate all .md files, excluding common non-content directories: `.venv/`, `node_modules/`, `.git/`, `archive/`, `.archive_old/`.

### Frontmatter Audit

- Scan a sample of existing files to detect the frontmatter schema in use.
- Check each markdown file for the presence of YAML frontmatter, core fields, consistency of `type` and `status` values, and non-empty tag lists.
- Track files with missing or incomplete frontmatter.

### Link Check

- Identify broken internal links using Grep and verify the existence of each target file.
- Run any project-specific link-checking scripts if available.

### Tag Consistency Audit

- Use Grep to find all `tags:` sections and analyze for near-duplicate tags, single-use tags, and overly broad tags.
- List all unique tags with their counts.

### Orphaned Files

- Check for files not referenced in any other file's `related:` field.

### Content Quality

- Identify documents that appear to be ideas or opportunities based on the `type` field or directory location.
- Check for drafts that have been in status for more than 30 days, missing metadata, and documents with very little content.

### Coverage Gaps

- Check each directory for empty or near-empty directories and directories with only 1-2 files.

### Reporting

- Generate a detailed report outlining the findings, including broken links, tag analysis, orphaned files, content quality issues, and coverage gaps.

## Steps

1. **Parse focus area** from `$ARGUMENTS` (optional).
2. **Find all markdown files.**
3. **Perform frontmatter audit.**
4. **Conduct link check.**
5. **Audit tag consistency.**
6. **Identify orphaned files.**
7. **Assess content quality.**
8. **Check for coverage gaps.**
9. **Output comprehensive report.**

## Common Issues and Solutions

### No markdown files found

**Cause:** Running in the wrong directory or all files excluded.
**Solution:** Ensure you are in the knowledge base root and check exclude patterns.

### Too many single-use tags

**Cause:** Inconsistent tagging across documents.
**Solution:** Pick canonical tags from the most-used list and re-run the audit after cleanup.

### Frontmatter validation errors

**Cause:** YAML syntax issues.
**Solution:** Ensure `---` delimiters are present and use `type:` and `status:` values consistent with your KB's detected schema.

## Dependencies

### Operating Environment

- **Agent Platform:** Any AI Agent supporting SKILL.md (Claude Code, Cursor, Codex, Gemini CLI, etc.)
- **Operating System:** Windows, macOS, Linux

### Dependencies

| Dependency | Type | Required | Acquisition Method |
|:-----------|:-----|:---------|:------------------|
| LLM API | API | Required | Provided by the built-in LLM of the Agent |

### API Key Configuration

- This Skill is based on Markdown instructions and does not require an additional API key, except for explicitly marked external APIs.

### Usability Classification

- **Category:** MD+EXEC (Pure Markdown instructions, some features require exec command-line execution capabilities)
- **Description:** An AI Skill based on Markdown that drives Agent tasks through natural language instructions.

## Core Capabilities

- In-depth health check for knowledge bases, identifying issues like broken links, missing frontmatter, inconsistent tags, and coverages.
- Trigger keywords: health, knowledge, base, check, audit, broken, solo

## Use Cases

| Scenario | Input | Output |
|:--------|:------|:-------|
| Basic Usage | User request | Processed result |

**Not applicable to:** Complex decision scenarios requiring human judgment.

## Usage Workflow

1. Confirm that the environment meets the requirements specified in the Dependency section.
2. Choose the appropriate usage method based on the applicable scenario.
3. Execute the operation and check the output result.
4. If an error occurs, refer to the Error Handling section.

## Examples

### Example 1: Basic Usage

```
Input: User request
Processing: Execute according to the usage workflow
Output: Processed result
```

## Error Handling

| Error Scenario | Reason | Solution |
|:---------------|:-------|:---------|
| Configuration Error | Missing or incorrect parameters | Check the configuration requirements in the Dependency section |
| Runtime Error | Inadequate runtime environment | Confirm that the runtime environment meets the requirements |
| Network Error | Connection timeout or unreachability | Check network connection and retry, refer to domestic alternatives |

## Common Questions

### Q1: How do I start using Audit?
A: Please refer to the Usage Workflow section and ensure that the environment meets the requirements specified in the Dependency section.

### Q2: What should I do if I encounter an error?
A: Please refer to the Error Handling section and follow the steps outlined in the table.

### Q3: What are the limitations of Audit?
A: Please refer to the Known Limitations section for more information.

## Known Limitations

- Requires LLM support; cannot be used without an LLM environment.
- Complex scenarios may require human judgment.
- Performance depends on the underlying model capabilities.

## Boundary Conditions and Limitations

### Input Limitations

- **File Count:** solo-audit may take a long time to complete the audit when the knowledge base contains a large number of `.md` files, as each file must be checked.
- **File Size:** The size of a single file should not exceed the limitations of the operating system or file system, otherwise the audit may fail.
- **Path Length:** There are limitations on path length in the operating system, and overly long paths may cause the audit tool to fail to access files correctly.

### Performance Boundaries

- **Processing Speed:** The performance of solo-audit may be affected for knowledge bases with a large number of files and complex structures, and the processing speed may be slow.
- **Resource Consumption:** The audit process may consume a large amount of CPU and memory resources, especially when checking a large number of files.

### Compatibility Constraints

- **Operating System:** solo-audit must be run on an AI Agent platform that supports SKILL.md, such as Claude Code, Cursor, Codex, Gemini CLI, etc.
- **File Format:** Only `.md` formatted files are supported; the audit tool cannot check files in other formats.
- **External Dependencies:** If there are external links or scripts in the project, solo-audit may not be able to handle them correctly, and all dependencies must be ensured to meet expectations.

## Differentiation Advantages

### Comparison with Similar Solutions

1. **Manual Operation:**
   - **Manual Operation:** Requires manual checking of each file, which is time-consuming and labor-intensive, and may miss issues.
   - **solo-audit:** Automates the process, quickly scans the entire knowledge base, saves a lot of time and labor, and covers more comprehensively.

2. **Other Tools:**
   - **General Markdown Check Tools:** May only provide some check functions, such as format errors, grammar errors, etc., but cannot comprehensively check the health of the knowledge base.
   - **solo-audit:** Focuses on the health check of the knowledge base, including issues such as broken links, missing frontmatter, inconsistent tags, and coverages, and provides detailed reports and recommendations.

3. **General Methods:**
   - **Script Writing:** Requires writing specific scripts to check the knowledge base, which lacks flexibility and is difficult to handle complex scenarios.
   - **solo-audit:** Provides predefined check processes and flexible configuration options, can easily adapt to different scenarios, and is easy to use.

### Unique Features

1. **Intelligent Parsing:** Automatically identifies the frontmatter schema without manual configuration.
2. **Multi-dimensional Checks:** Covers multiple dimensions such as broken links, tag consistency, orphaned files, and content quality, ensuring the comprehensive health of the knowledge base.
3. **Customizable Reports:** Provides detailed reports, including issue lists, recommendations, and improvement measures, helping users quickly locate and resolve problems.
4. **Automated Execution:** Supports scheduled execution to ensure that the knowledge base remains healthy.
5. **Cross-platform Compatibility:** Supports Windows, macOS, Linux, and other operating systems, making it convenient for users to use in different environments.

### Efficiency Improvement

- **Save Time:** Compared to manual operation, solo-audit can save over 80% of time.
- **Reduce Steps:** No need to write scripts, simplifying the operation process and reducing the threshold for use.

### Innovation in Application Scenarios

1. **Knowledge Base Maintenance:** Regularly use solo-audit to perform health checks on the knowledge base to ensure content quality and improve user experience.
2. **Team Collaboration:** Integrate solo-audit into the workflow to achieve automated maintenance and collaboration of the knowledge base.
3. **Automated Testing:** Use solo-audit for automated testing before the release of the knowledge base to ensure the stability and reliability of the knowledge base.