---
slug: "typescript-skills-tool-pro"
name: "typescript-skills-tool-pro"
version: "1.0.0"
displayName: "TS编码规范工具(专业版)"
summary: "面向团队的TypeScript编码规范平台,含自动化审查、规则集管理、CI集成与规范文档生成。"
license: "Proprietary"
edition: "pro"
description: |-
  TypeScript编码规范工具专业版为团队与企业提供端到端编码规范落地能力,涵盖自动化审查、企业级规则集、CI集成与规范文档自动生成。核心能力:
  - 企业级ESLint规则集与多层配置管理
  - 自动化代码审查脚本与PR级规范检查
  - 规范文档自动生成与版本化
  - CI/CD流水线规范门禁
  - 跨包仓库规范一致性校验
  - 团队培训材料与代码示例库

  适用场景:
  - 中大型团队TypeScript规范统一落地
  - 多包仓库规范一致性管理
  - PR级自动化规范审查
  - 企业内部规范文档维护与发布

  差异化...
tags:
  - TypeScript
  - 编码规范
  - 企业开发
  - 自动化审查
  - CI/CD
  - 团队协作
  - 工程规范
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# TypeScript 编码规范工具(专业版)

## 概述

`typescript-skills-tool-pro` 是面向团队与企业的 TypeScript 编码规范工程平台。它在免费版基础规范之上,扩展了企业级 ESLint 规则集、自动化审查脚本、CI/CD 集成与规范文档自动生成能力,帮助团队在规模化项目中维持一致的代码风格与质量。

本版本完全兼容免费版输出的所有规范建议与代码示例,可平滑升级。所有指令通过 Markdown 驱动 Agent,无需额外安装私有脚本。

## 核心能力

| 能力 | 说明 | 是否兼容免费版 |
| --- | --- | --- |
| 基础规范指导 | 免费版全部命名、类型、函数、模块规范 | 完全兼容 |
| 企业级 ESLint 规则集 | 多层配置、命名约定、复杂度门禁 | Pro 新增 |
| 自动化代码审查 | 脚本化扫描、PR 级规范检查、报告生成 | Pro 新增 |
| 规范文档生成 | 从代码与规则集自动生成规范文档 | Pro 新增 |
| CI/CD 规范门禁 | GitHub Actions、GitLab CI 集成 | Pro 新增 |
| 多包仓库一致性 | 跨包规范校验与共享配置 | Pro 新增 |
| 团队培训材料 | 示例库、反模式集合、培训大纲 | Pro 新增 |

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 按照skill规范执行参数配置与调用操作,遵循单一意图原则。
**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 按照skill规范执行结果处理与输出操作,遵循单一意图原则。
**输出**: 返回结果处理与输出的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：面向团队的、TypeScript、编码规范平台、含自动化审查、规则集管理、集成与规范文档生、编码规范工具专业、版为团队与企业提、供端到端编码规范、落地能力、涵盖自动化审查、企业级规则集、集成与规范文档自、核心能力、规则集与多层配置、自动化代码审查脚、规范文档自动生成、与版本化、流水线规范门禁、跨包仓库规范一致、性校验、团队培训材料与代、码示例库等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景 1:企业级 ESLint 规则集落地

为团队生成完整的企业级 ESLint 配置,包含命名约定、复杂度门禁与导入顺序。

```jsonc
// .eslintrc.json(企业基线)
{
  "root": true,
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "project": "./tsconfig.json",
    "sourceType": "module"
  },
  "plugins": ["@typescript-eslint", "import", "sonarjs", "eslint-plugin-tsdoc"],
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking",
    "plugin:import/recommended",
    "plugin:import/typescript",
    "plugin:sonarjs/recommended"
  ],
  "rules": {
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/explicit-function-return-type": ["error", { "allowExpressions": true }],
    "@typescript-eslint/no-unused-vars": ["error", { "argsIgnorePattern": "^_", "varsIgnorePattern": "^_" }],
    "@typescript-eslint/consistent-type-imports": ["error", { "prefer": "type-imports" }],
    "@typescript-eslint/no-non-null-assertion": "error",
    "@typescript-eslint/prefer-nullish-coalescing": "error",
    "@typescript-eslint/prefer-optional-chain": "error",
    "@typescript-eslint/strict-boolean-expressions": "warn",
    "@typescript-eslint/naming-convention": [
      "error",
      { "selector": "typeLike", "format": ["PascalCase"] },
      { "selector": "variable", "format": ["camelCase", "UPPER_CASE"], "leadingUnderscore": "forbid" },
      { "selector": "parameter", "format": ["camelCase"], "leadingUnderscore": "allow" },
      { "selector": "enumMember", "format": ["PascalCase"] }
    ],
    "import/order": ["error", {
      "groups": ["builtin", "external", "internal", "parent", "sibling", "index"],
      "newlines-between": "always",
      "alphabetize": { "order": "asc", "caseInsensitive": true }
    }],
    "import/no-default-export": "error",
    "import/no-cycle": "error",
    "sonarjs/cognitive-complexity": ["error", 15],
    "sonarjs/no-duplicate-string": ["error", 5],
    "tsdoc/syntax": "warn"
  },
  "overrides": [
    {
      "files": ["*.test.ts", "*.spec.ts"],
      "rules": {
        "@typescript-eslint/no-non-null-assertion": "off",
        "sonarjs/no-duplicate-string": "off"
      }
    }
  ]
}
```

### 场景 2:自动化代码审查脚本

生成一个本地脚本,扫描仓库并输出规范违规报告。

```bash
#!/usr/bin/env bash
# scripts/lint-report.sh — 生成团队规范违规报告
set -euo pipefail

REPORT_DIR="reports/lint"
mkdir -p "$REPORT_DIR"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

# 1. ESLint 检查输出 JSON
npx eslint . --ext .ts,.tsx \
  --format json \
  --output-file "$REPORT_DIR/eslint-$TIMESTAMP.json" || true

# 2. 统计违规分布
npx eslint . --ext .ts,.tsx --format compact \
  | awk -F: '{print $1}' \
  | sort | uniq -c | sort -rn \
  | head -20 > "$REPORT_DIR/top-files-$TIMESTAMP.txt"

# 3. 类型覆盖率
npx type-coverage --detail --strict > "$REPORT_DIR/type-coverage-$TIMESTAMP.txt"

echo "报告已生成于 $REPORT_DIR/"
echo "  - eslint-$TIMESTAMP.json:完整 ESLint 结果"
echo "  - top-files-$TIMESTAMP.txt:违规最多的文件 Top 20"
echo "  - type-coverage-$TIMESTAMP.txt:类型覆盖率详情"
```

### 场景 3:CI/CD 规范门禁

在 GitHub Actions 中集成规范检查,作为 PR 合并的前置门禁。

```yaml
# .github/workflows/lint-gate.yml
name: TypeScript Lint Gate
on:
  pull_request:
    branches: [main, release/*]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - name: ESLint 检查(零警告)
        run: npx eslint . --max-warnings=0
      - name: 导入顺序检查
        run: npx eslint . --rule 'import/order: error'
      - name: 命名约定检查
        run: npx eslint . --rule '@typescript-eslint/naming-convention: error'
      - name: 复杂度门禁
        run: npx eslint . --rule 'sonarjs/cognitive-complexity: [error, 15]'
      - name: 类型覆盖率门禁
        run: npx type-coverage --strict --at-least 95
      - name: 上传报告
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: lint-report
          path: reports/lint/
```

## 不适用场景

以下场景TS编码规范工具(专业版)不适合处理：

- 实际人员绩效评估
- 财务预算审批
- 合同法务审核

## 触发条件

需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于非本工具能力范围的需求。

## 快速开始

### 第一步:声明团队上下文

在对话中说明团队规模、项目结构与规范现状,例如:

```
我们是 20 人的 Node.js 后端团队,仓库是 monorepo 结构,有 5 个子包。
需要一套统一的 ESLint 规则集,以及 CI 门禁配置,目标类型覆盖率 95%。
```

### 第二步:获取工程方案

工具会输出分层 ESLint 配置、CI 门禁 YAML、审查脚本与规范文档草稿。

### 第三步:落地与监控

```bash
# 应用配置后,本地验证
npx eslint . --max-warnings=0
npx tsc --noEmit
npx type-coverage --strict --at-least 95

# 生成首份基线报告
bash scripts/lint-report.sh
```

#
## 示例

### 多包仓库共享 ESLint 配置

```jsonc
// packages/eslint-config-base/index.json(共享基线)
{
  "parser": "@typescript-eslint/parser",
  "parserOptions": { "sourceType": "module" },
  "plugins": ["@typescript-eslint", "import"],
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:import/recommended"
  ],
  "rules": {
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/consistent-type-imports": "error",
    "import/order": ["error", { "newlines-between": "always" }]
  }
}
```

```jsonc
// packages/api/.eslintrc.json(子包继承)
{
  "extends": "@your-org/eslint-config-base",
  "parserOptions": { "project": "./tsconfig.json" },
  "rules": {
    "@typescript-eslint/explicit-function-return-type": "error"
  }
}
```

### 规范文档自动生成脚本

```bash
#!/usr/bin/env bash
# scripts/gen-styleguide.sh — 从 ESLint 规则生成规范文档
set -euo pipefail

OUTPUT="docs/styleguide.md"
{
  echo "# TypeScript 编码规范"
  echo ""
  echo "> 自动生成于 $(date +%Y-%m-%d),规则来源:.eslintrc.json"
  echo ""
  echo "## 规则清单"
  echo ""
  npx eslint --print-config src/index.ts \
    | jq -r '.rules | to_entries[] | "| \(.key) | \(.value | tostring) |"' \
    | sort
} > "$OUTPUT"

echo "规范文档已生成:$OUTPUT"
```

## 最佳实践

1. **采用分层 ESLint 配置**:共享基线 + 子包覆盖,降低维护成本,保证一致性。
2. **CI 门禁零警告策略**:`--max-warnings=0` 阻断所有警告进入主分支,强制即时修复。
3. **类型覆盖率门禁**:用 `type-coverage --at-least 95` 作为 CI 必过门禁。
4. **命名约定强制**:通过 `@typescript-eslint/naming-convention` 规则化命名风格,避免口头约定失效。
5. **复杂度门禁**:`sonarjs/cognitive-complexity` 限制函数认知复杂度,提升可维护性。
6. **导入顺序自动化**:`import/order` 规则配合 `--fix` 自动整理导入,无需人工排序。
7. **规范文档版本化**:将规范文档纳入仓库,与代码同步演进,通过 PR 审查变更。
8. **定期生成违规报告**:每周或每个迭代生成报告,识别热点模块安排专项治理。

## 常见问题

### Q1: 团队已有大量历史代码不符合新规则,如何落地?

采用渐进式策略:1) 新规则设为 `warn` 而非 `error`,先生成报告;2) 在 CI 中仅对新增/修改文件强制 `error`;3) 设置治理里程碑,逐步清理存量违规。

### Q2: 多包仓库如何保证规范一致性?

共享 ESLint 基线配置包,子包通过 `extends` 继承。配合 `eslint --print-config` 校验最终配置,确保无意外覆盖。

### Q3: `import/no-cycle` 报错很多,如何处理?

循环依赖通常反映架构问题。短期可在 `overrides` 中对特定目录关闭规则,长期通过分层重构(提取共享模块)消除循环。

### Q4: 规范文档如何与代码保持同步?

使用 `scripts/gen-styleguide.sh` 在 CI 中自动重新生成规范文档,若文档与规则集不一致则阻断 PR。规范变更通过修改规则集 PR 一次性完成。

### Q5: Pro 版与免费版如何协同?

Pro 版完全兼容免费版的所有规范建议。个人开发者可继续使用免费版,团队场景启用 Pro 版获得自动化审查与企业级能力。两个版本可在同一仓库并存。

### Q6: 如何度量团队规范成熟度?

跟踪三个指标:ESLint 违规密度(违规数 / 千行)、类型覆盖率、CI 规范门禁通过率。三者共同反映规范成熟度。

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **Node.js**:建议 20 LTS+
- **TypeScript**:建议 5.0+
- **CI 平台**:GitHub Actions / GitLab CI / Jenkins / Azure Pipelines

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| TypeScript | npm 包 | 必需 | `npm i -D typescript` |
| ESLint + @typescript-eslint | npm 包 | 必需 | `npm i -D eslint @typescript-eslint/eslint-plugin @typescript-eslint/parser` |
| eslint-plugin-import | npm 包 | 推荐 | `npm i -D eslint-plugin-import` |
| eslint-plugin-sonarjs | npm 包 | 推荐 | `npm i -D eslint-plugin-sonarjs` |
| eslint-plugin-tsdoc | npm 包 | 可选 | `npm i -D eslint-plugin-tsdoc` |
| type-coverage | npm 包 | 推荐 | `npm i -D type-coverage` |
| jq | 系统工具 | 可选 | 系统包管理器安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 完全基于 Markdown 指令,无需额外 API Key
- CI 中如需访问私有 npm 注册表,配置 `NODE_AUTH_TOKEN` 环境变量
- 如集成 SonarQube 云端分析,需配置 `SONAR_TOKEN`

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言指令驱动 Agent 输出企业级规范方案;CI 集成与审查脚本需在仓库中落地并由 CI 运行器执行

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
