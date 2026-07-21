---
slug: go-linter-configuration
name: go-linter-configuration
version: "1.0.0"
displayName: Go Linter Configurat
summary: Configure and troubleshoot golangci-lint for Go projects. Handle import resolution
  issues, type-c...
license: MIT
description: |-
  Configure and troubleshoot golangci-lint for Go projects。Handle import
  resolution issues, type-c。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
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

## 错误处理

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

- Configure and troubleshoot golangci-lint for Go projects
- Handle import
  resolution issues, type-c
- 触发关键词: linter, lint, configure, configuration, projects, golangci, troubleshoot

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 常见问题

### Q1: 如何开始使用Go Linter Configurat？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Go Linter Configurat有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
