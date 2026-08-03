---
slug: web
name: web
version: "1.0.0"
displayName: Web Development
summary: "用HTML/CSS/JS与现代框架建调部署网站(社区下载版)"
  frameworks following pr...
license: MIT
description: |-
  Build, debug, and deploy websites using HTML, CSS, JavaScript, and modern
  frameworks following pr。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

# Advanced Web Development Toolkit

## Overview

Welcome to the Advanced Web Development Toolkit, a cornerstone for modern web development. This toolkit is designed to empower developers with the knowledge and tools to create, optimize, and deploy high-quality web applications using the latest technologies and best practices.

## Quick Reference

| Need | Resource |
| --- | --- |
| HTML/CSS troubleshooting | [HTML/CSS Guide](html-css.md) |
| JavaScript debugging | [JavaScript Patterns](javascript.md) |
| Framework selection | [Frameworks Guide](frameworks.md) |
| Deployment strategies | [Deployment Guide](deploy.md) |
| Performance optimization | [Performance Guide](performance.md) |
| SEO best practices | [SEO Guide](seo.md) |
| Accessibility compliance | [Accessibility Guide](accessibility.md) |
| Security considerations | [Security Guide](security.md) |

## Key Concepts

### Doctype and Quirks Mode
The `<!DOCTYPE html>` declaration is crucial for standard mode rendering in browsers, avoiding quirks mode which can lead to inconsistent behavior.

### CSS Specificity and Cascade
Master the CSS cascade and specificity to ensure styles are applied correctly across your website.

### Type Coercion
Prevent unexpected behavior by using strict equality (`===`) over loose equality (`==`).

### Async/Await and Loops
Use `for...of` loops or `Promise.all` for managing asynchronous operations in JavaScript.

### CORS Configuration
Server-side CORS configuration is essential for cross-origin resource sharing and must be carefully managed.

### Responsive Design
Implement responsive design with viewport meta tags and media queries to ensure compatibility across devices.

### Form Handling
Prevent form submissions from reloading the page by calling `e.preventDefault()` in your submit handlers.

### Image Dimensions
Specify image dimensions to optimize page load times and improve the user experience.

### HTTPS and Mixed Content
Secure your site with HTTPS and avoid mixed content issues to enhance security and trust.

### Environment Variables
Use environment variables to manage configuration and secrets, separating them from client-side code.

## Common Queries

**"Make it responsive"** → Implement responsive design using media queries and test across various device widths.

**"Deploy to production"** → Follow the [Deployment Guide](deploy.md) for step-by-step instructions on deploying to various platforms.

**"Fix CORS error"** → Configure server headers or use a proxy to resolve CORS issues when server configuration is out of your control.

**"Improve performance"** → Use Lighthouse for performance audits and focus on critical metrics like LCP, CLS, and FID.

**"Add SEO"** → Optimize your site for search engines by following best practices for titles, descriptions, and structured data.

## Framework Decision Tree

| Project Type | Framework Recommendation |
| --- | --- |
| Static site | Gatsby, Next.js with static generation |
| Blog or documentation | Next.js, Nuxt.js |
| E-commerce | Vue.js with Nuxt.js, Angular with Angular Universal |
| Content management | WordPress, Drupal, Joomla |
| Real-time application | Socket.IO, WebSockets with Next.js |

## Dependency Requirements

### Runtime Environment
- **Agent Platform**: Compatible with any AI Agent supporting SKILL.md (Claude Code, Cursor, Codex, Gemini CLI, etc.)
- **Operating System**: Windows, macOS, Linux

### Dependencies
| Dependency | Type | Required | Acquisition Method |
|:-------|:-----|:---------|:---------|
| LLM API | API | Required | Provided by the AI Agent's built-in LLM |
| Webpack | Build Tool | Optional | Install via npm or yarn |
| Babel | Transpiler | Optional | Install via npm or yarn |

### API Key Configuration
- This skill uses Markdown instructions and does not require an additional API key unless specified for external APIs.

### Usability Classification
- **Category**: MD+EXEC (Markdown instructions with some features requiring exec command-line execution)
- **Description**: An AI-driven Markdown skill that executes tasks based on natural language commands.

## Core Capabilities

- Build, debug, and deploy websites using HTML, CSS, JavaScript, and modern web frameworks
- Trigger Keywords: web development, HTML, CSS, JavaScript, frameworks, deployment, optimization, SEO, accessibility

## Applicability Scenarios

| Scenario | Input | Output |
|------|------|------|
| Basic Usage | User request | Processed result |
| Advanced Usage | Complex development tasks | Automated solutions |

**Not Applicable**: Complex decision-making scenarios requiring human judgment

## Usage Workflow

1. Confirm that the runtime environment meets the requirements specified in the Dependency Requirements section.
2. Choose the appropriate usage method based on the Applicability Scenarios.
3. Execute the operation and check the output result.
4. If an error occurs, refer to the Error Handling section.

## Examples

### Example 1: Basic Usage

```
Input: User request
Processing: Execute the workflow based on the Usage Workflow
Output: Processed result
```

### Example 2: Advanced Usage

```
Input: "I need to optimize my website's performance"
Processing: Analyze the website using Lighthouse and provide optimization suggestions
Output: Detailed performance optimization report
```

## Error Handling

| Error Scenario | Cause | Resolution |
|---------|------|---------|
| Configuration Error | Missing or incorrectly formatted parameters | Check the Dependency Requirements for configuration requirements |
| Runtime Error | Inadequate runtime environment | Confirm that the runtime environment meets the requirements |
| Network Error | Connection timeout or unreachability | Check network connection and retry; refer to domestic alternatives if necessary |

## Frequently Asked Questions

### Q1: How do I start using the Advanced Web Development Toolkit?
A: Please read the Usage Workflow section and confirm that the environment meets the requirements specified in the Dependency Requirements.

### Q2: What should I do if I encounter an error?
A: Please refer to the Error Handling section for instructions on how to handle errors.

### Q3: What are the limitations of the Advanced Web Development Toolkit?
A: Please refer to the Known Limitations section for details on the skill's limitations.

## Known Limitations

- Requires LLM support; cannot be used without an LLM environment
- May require human judgment for complex scenarios
- Performance depends on the underlying model capabilities

## Boundary Conditions and Limitations

### Input Restrictions
- **Input Format**: The skill only accepts specific formats, such as Markdown code examples or problem descriptions. Non-standard formats or binary data cannot be processed correctly.
- **Length Limit**: There is a limit to the length of input content, and overly long content may cause the skill to fail to parse or respond correctly.
- **Complexity Limit**: For overly complex scenarios, the skill may not be able to provide an accurate solution, and human intervention may be required for decision-making.

### Performance Boundaries
- **Processing Speed**: The speed of processing requests is limited by the capabilities of the underlying model, and processing time may be longer for complex or large data scenarios.
- **Concurrency Handling**: The skill has limited concurrency handling capabilities, and a large number of concurrent requests may cause response delays.

### Compatibility Constraints
- **Browser Compatibility**: The output of the skill may be inconsistent across different browsers, and it is recommended to test in mainstream browsers.
- **Framework Compatibility**: The skill supports a limited set of frameworks and libraries, and may not provide expected functionality for unsupported frameworks or libraries.

### Data Security and Privacy
- **Data Leak Risk**: The skill may involve sensitive data in the processing process, and data security must be ensured to avoid data leaks.
- **Privacy Protection**: The skill should comply with relevant privacy protection regulations to ensure that user privacy is not violated.

### Environment Dependencies
- **Operating System**: The skill runs on specific operating systems and does not support cross-platform usage.
- **Hardware Requirements**: The skill has certain requirements for hardware resources, such as CPU and memory, and may not meet the requirements of low-end configurations.

### Human Assistance
- **Complex Scenarios**: For complex or vague requirements, the skill may not be able to provide an accurate solution, and human assistance may be required for decision-making.
- **Decision-Making Scenarios**: The skill is not suitable for complex decision-making scenarios requiring human judgment, such as risk assessment and business decision-making.

## Differentiation Advantages

### Comparison with Similar Solutions

1. **Manual Operation**: Compared to manual coding and debugging, this skill significantly improves development efficiency through automated tools and predefined rules.
2. **Other Tools**: Compared to other code editors or IDEs, this skill focuses on the automation of the web development process.
3. **Universal Methods**: Compared to universal programming methods, this skill is optimized for the web development field.

### Unique Features

1. **Framework Decision Tree**: This skill provides a framework decision tree to help developers choose the appropriate framework based on project requirements.
2. **Fast Deployment**: This skill supports fast deployment to the production environment through platforms such as Vercel, Netlify, and VPS.
3. **Performance Optimization**: This skill provides a series of performance optimization suggestions.
4. **SEO Optimization**: This skill includes SEO optimization suggestions.
5. **Security Protection**: This skill provides a series of security protection suggestions.

### Efficiency Improvement

Using this skill, developers can save at least 50% of the time spent on code writing and debugging. By automating tools and predefined rules, manual intervention is reduced, reducing the probability of errors and improving development efficiency.

### Innovation in Application Scenarios

1. **Rapid Prototype Design**: This skill can help developers quickly build prototypes, verify design ideas, and save time and costs in the design phase.
2. **Team Collaboration**: This skill supports team collaboration in development, and improves team collaboration efficiency through code generation and automated deployment.
3. **Education Field**: This skill can be used as a web development teaching tool to help students quickly master web development skills and improve teaching effectiveness.