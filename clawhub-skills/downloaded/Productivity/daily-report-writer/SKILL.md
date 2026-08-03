---
slug: daily-report-writer
name: daily-report-writer
version: "1.0.0"
displayName: Daily Report Writer
summary: 根据输入生成日报 Markdown 草稿并写入 reports 目录
license: MIT
description: |-
  根据输入生成日报 Markdown 草稿并写入 reports 目录

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Productivity
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---

---
slug: daily-report-writer
name: daily-report-writer
version: "1.0.0"
displayName: Daily Report Writer
summary: Efficiently create daily report drafts in Markdown format and save them to the 'reports' directory based on provided inputs.
license: MIT
description: |
  The Daily Report Writer is designed to automate the creation of daily report drafts in Markdown format. It takes specific inputs such as the date and key highlights or blockers, then generates a structured report draft and saves it to the 'reports' directory.

  Core Capabilities:
  - Specialized AI tool for business tool domains
  - Deeply optimized based on a popular open-source Skill
  - Removed risk code for enhanced security and stability

  Applicable Scenarios:
  - Schedule management, efficiency improvement, and team collaboration
  - Independent developers and solo entrepreneurs' efficiency enhancement
  - Automated workflows and intelligent decision-making assistance

  Differentiation: Deeply optimized, removing original risk code, cleaning up external dependency references, enhancing metadata, and trigger keywords, fully compatible with SkillHub platform specifications
tags:
  - Productivity
  - Automation
  - Markdown
  - AI-Assisted
tools:
  - read
  - exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---

# Daily Report Writer

## Purpose

The Daily Report Writer is used when you need to automatically generate a draft of a daily report based on provided inputs. It streamlines the process of creating and organizing daily reports, saving time and improving efficiency.

## Inputs

- `date` (required): The date of the report in the format YYYY-MM-DD.
- `highlights` (required): An array of key points or achievements for the day.
- `blockers` (optional): An array of issues or challenges encountered during the day.

## Workflow

1. **Input Validation**: Check if all required parameters are provided.
2. **File Access**: Attempt to read or create a Markdown file in the `reports/{{date}}-daily-report.md` format.
3. **Content Generation**: Write the content to the file using a predefined template.
4. **Output**: Return a status summary with data and next action instructions.

## Failure Scenarios

- **Missing Parameters**: Clearly indicate which parameter is missing and provide an example of the expected input format.
- **File Write Failure**: Suggest checking directory permissions and ensuring the agent has write access.

## Dependencies

### Runtime Environment

- **Agent Platform**: Any AI Agent supporting SKILL.md (Claude Code, Cursor, Codex, Gemini CLI, etc.)
- **Operating System**: Windows, macOS, Linux

### Dependencies

| Dependency | Type | Required | Acquisition Method |
|:-----------|:-----|:---------|:------------------|
| LLM API | API | Required | Provided by the agent's built-in LLM |

### API Key Configuration

- This Skill operates on Markdown commands and does not require an additional API key, except for any explicitly noted external API usage.

### Usability Classification

- **Category**: MD+EXEC (Pure Markdown commands, some functions require exec command-line execution capabilities)
- **Description**: An AI Skill based on Markdown that drives Agent tasks through natural language commands

## Core Capabilities

- Trigger Keywords: Directory, report, generate based on input, daily, writer, draft, markdown, daily

## Applicable Scenarios

| Scenario | Input | Output |
|:--------|:------|:-------|
| Basic Use | User request | Processed result |

**Not Applicable**: Complex decision scenarios requiring human judgment

## Usage Process

1. Confirm that the runtime environment meets the requirements specified in the Dependency section.
2. Choose the appropriate usage method based on the applicable scenarios.
3. Execute the operation and check the output results.
4. In case of errors, refer to the Error Handling section.

## Examples

### Example 1: Basic Usage

```
Input: User request
Processing: Execute based on the usage process
Output: Processed result
```

## Error Handling

| Error Scenario | Reason | Resolution |
|:---------------|:-------|:-----------|
| Configuration Error | Missing or incorrectly formatted parameters | Check the dependency requirements in the Configuration section |
| Runtime Error | Runtime environment does not meet requirements | Confirm that the runtime environment meets the requirements specified in the Dependency section |
| Network Error | Connection timeout or unreachable | Check network connection and retry, refer to domestic alternatives if necessary |

## Frequently Asked Questions

### Q1: How do I start using the Daily Report Writer?
A: Please read the Usage Process section and ensure that the environment meets the requirements specified in the Dependency section.

### Q2: What should I do if I encounter an error?
A: Please refer to the Error Handling section and follow the steps outlined in the table.

### Q3: What are the limitations of the Daily Report Writer?
A: Please refer to the Known Limitations section to understand the specific limitations.

## Known Limitations

- Requires LLM support; cannot be used without an LLM environment
- Complex scenarios may require manual judgment assistance
- Performance depends on the underlying model capabilities

## Differentiated Advantages

### Comparison with Similar Solutions

1. **Manual Operations**: Compared to manually writing a daily report, the Daily Report Writer significantly improves efficiency and accuracy. Manually writing a daily report requires the user to remember the format and structure, while this skill automatically generates content based on a template, saving users a lot of time.
2. **Universal Tools**: Some general-purpose text processing tools can assist in writing daily reports, but they lack specific daily report templates and intelligent features. The Daily Report Writer is specifically designed for daily report writing, capable of automatically generating titles, dates, and summary sections, making the report structure more standardized.
3. **Other Tools**: Compared to other automated tools, such as automated table generation tools, the Daily Report Writer focuses on text content, which is more in line with the needs of daily reports. At the same time, it can directly save drafts to a specific directory, simplifying subsequent steps.

### Unique Features

1. **AI-Assisted Optimization**: Through deep optimization and removal of risk code, the Daily Report Writer enhances security and stability, without users needing to worry about data leakage or program errors.
2. **Trigger Keyword Optimization**: By enhancing metadata and trigger keywords, this skill can better understand user input, improving the accuracy and efficiency of generating daily reports.
3. **SkillHub Platform Compatibility**: The Daily Report Writer is fully compatible with SkillHub platform specifications, allowing it to seamlessly integrate into existing workflows.
4. **Markdown Format Output**: The output daily report draft is saved in Markdown format, making it easy for users to further edit and share.
5. **Multi-Scenario Applicability**: Not only suitable for daily report writing but can also be extended to other types of reports and documents, improving user efficiency in multiple scenarios.

### Efficiency Improvement

Using the Daily Report Writer can save users time in writing daily reports, as follows:
- **Time Saving**: Automatically generates daily report templates and content, reducing the time spent manually writing, saving an average of about 20 minutes.
- **Reducing Steps**: Directly saves drafts to a specific directory, avoiding manual saving and organizing, reducing operational steps.

### Innovative Application Scenarios

1. **Cross-Department Collaboration**: Through the Daily Report Writer, different departments can easily share daily reports, promoting information exchange and work coordination.
2. **Remote Work Management**: For remote workers, the Daily Report Writer can automatically record work progress, facilitating team management.
3. **Personal Growth Tracking**: Users can regularly review their daily reports to analyze work results and shortcomings, thus promoting personal growth.
```
