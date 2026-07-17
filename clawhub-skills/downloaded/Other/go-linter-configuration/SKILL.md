---
slug: go-linter-configuration
name: go-linter-configuration
version: "1.0.0"
displayName: Go Linter Configuration
summary: Configure and troubleshoot golangci-lint for Go projects. Handle import resolution
  issues, type-c...
license: MIT
description: |-
  Configure and troubleshoot golangci-lint for Go projects. Handle import
  resolution issues, type-c...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: linter, lint, configure, configuration, projects, golangci, troubleshoot
tags:
- Other
tools:
- read
- exec
---

# Go Linter Configuration

Configure and troubleshoot golangci-lint for Go projects. This skill helps handle import resolution issues, type-checking problems, and optimize configurations for both local and CI environments.

## Installation

Install golangci-lint:

```bash
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
```

Or use the official installation script:

```bash
curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.59.1
```

## Basic Usage

Run linter on entire project:

```bash
golangci-lint run ./...
```

Run with specific configuration:

```bash
golangci-lint run --config .golangci.yml ./...
```

## Configuration File (.golangci.yml)

### Minimal Configuration (for CI environments with import issues)

```yaml
run:
  timeout: 5m
  tests: false
  build-tags: []

linters:
  disable-all: true
  enable:
    - gofmt          # Format checking only

linters-settings:
  gofmt:
    simplify: true

issues:
  exclude-use-default: false
  max-issues-per-linter: 50
  max-same-issues: 3

output:
  format: tab
```

### Standard Configuration (for local development)

```yaml
run:
  timeout: 5m
  tests: true
  build-tags: []

linters:
  enable:
    - gofmt
    - govet
    - errcheck
    - staticcheck
    - unused
    - gosimple
    - ineffassign

linters-settings:
  govet:
    enable:
      - shadow
  errcheck:
    check-type-assertions: true
  staticcheck:
    checks: ["all"]

issues:
  exclude-use-default: false
  max-issues-per-linter: 50
  max-same-issues: 3

output:
  format: tab
```

## Troubleshooting Common Issues

### "undefined: package" Errors

Problem: Linter reports undefined references to imported packages
Solution: Use minimal configuration with `disable-all: true` and only enable basic linters like `gofmt`

### Import Resolution Problems

Problem: CI environment cannot resolve dependencies properly
Solution:

1. Ensure go.mod and go.sum are up to date
2. Use `go mod download` before running linter in CI
3. Consider using simpler linters in CI environment

### Type-Checking Failures

Problem: Linter fails during type checking phase
Solution:

1. Temporarily disable complex linters that require type checking
2. Use `--fast` flag for quicker, less intensive checks
3. Verify all imports are properly declared

## CI/CD Optimization

For GitHub Actions workflow:

```yaml
name: Code Quality

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    - name: Set up Go
      uses: actions/setup-go@v4
      with:
        go-version: "1.21"
        cache: true

    - name: Download dependencies
      run: go mod download

    - name: Install golangci-lint
      run: |
        curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.59.1

    - name: Lint
      run: golangci-lint run --config .golangci.yml ./...
```

## Linter Selection Guidelines

* **gofmt**: For formatting consistency
* **govet**: For semantic errors
* **errcheck**: For unchecked errors
* **staticcheck**: For static analysis
* **unused**: For dead code detection
* **gosimple**: For simplification suggestions
* **ineffassign**: For ineffective assignments

Choose linters based on project needs and CI performance requirements.

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
