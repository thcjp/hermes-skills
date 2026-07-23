---
slug: "typescript-skills-paid"
name: "typescript-skills-paid"
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
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# TS编码规范工具(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| TS编码规范工具(专业版)规则集管理 | 不支持 | 支持 |
| TS编码规范工具(专业版)I集成与规范文档生成 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |

## 核心能力

| 能力 | 说明 | 是否兼容免费版 |
|:-----|:-----|:-----|
| 基础规范指导 | 免费版全部命名、类型、函数、模块规范 | 完全兼容 |
| 企业级 ESLint 规则集 | 多层配置、命名约定、复杂度门禁 | Pro 新增 |
| 自动化代码审查 | 脚本化扫描、PR 级规范检查、报告生成 | Pro 新增 |
| 规范文档生成 | 从代码与规则集自动生成规范文档 | Pro 新增 |
| CI/CD 规范门禁 | GitHub Actions、GitLab CI 集成 | Pro 新增 |
| 多包仓库一致性 | 跨包规范校验与共享配置 | Pro 新增 |
| 团队培训材料 | 示例库、反模式集合、培训大纲 | Pro 新增 |
### 基础规范指导

针对基础规范指导,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供基础规范指导相关的配置参数、输入数据和处理选项.
**输出**: 返回基础规范指导的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`基础规范指导`的配置文档进行参数调优
### 企业级 ESLint 规则集

针对企业级 ESLint 规则集,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供企业级 ESLint 规则集相关的配置参数、输入数据和处理选项.
**输出**: 返回企业级 ESLint 规则集的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`企业级 ESLint 规则集`的配置文档进行参数调优
### 自动化代码审查

针对自动化代码审查,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供自动化代码审查相关的配置参数、输入数据和处理选项.
**输出**: 返回自动化代码审查的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`自动化代码审查`的配置文档进行参数调优
#
## 适用场景

### 场景 1:企业级 ESLint 规则集落地

为团队生成完整的企业级 ESLint 配置,包含命名约定、复杂度门禁与导入顺序.
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

生成一个本地脚本,扫描仓库并输出规范违规报告.
```bash
#!/usr/bin/env bash
# （请参考skill目录中的脚本文件） — 生成团队规范违规报告
set -euo pipefail
# ...
REPORT_DIR="reports/lint"
mkdir -p "$REPORT_DIR"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
# ...
# 1. ESLint 检查输出 JSON
npx eslint . --ext .ts,.tsx \
  --format json \
  --output-file "$REPORT_DIR/eslint-$TIMESTAMP.json" || true
# ...
# 2. 统计违规分布
npx eslint . --ext .ts,.tsx --format compact \
  | awk -F: '{print $1}' \
  | sort | uniq -c | sort -rn \
  | head -20 > "$REPORT_DIR/top-files-$TIMESTAMP.txt"
# ...
# 3. 类型覆盖率
npx type-coverage --detail --strict > "$REPORT_DIR/type-coverage-$TIMESTAMP.txt"
# ...
echo "报告已生成于 $REPORT_DIR/"
echo "  - eslint-$TIMESTAMP.json:完整 ESLint 结果"
echo "  - top-files-$TIMESTAMP.txt:违规最多的文件 Top 20"
echo "  - type-coverage-$TIMESTAMP.txt:类型覆盖率详情"
```

### 场景 3:CI/CD 规范门禁

在 GitHub Actions 中集成规范检查,作为 PR 合并的前置门禁.
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

## 使用流程

### 优秀步:声明团队上下文

在对话中说明团队规模、项目结构与规范现状,例如:

```
我们是 20 人的 Node.js 后端团队,仓库是 monorepo 结构,有 5 个子包.
需要一套统一的 ESLint 规则集,以及 CI 门禁配置,目标类型覆盖率 95%.
```

### 第二步:获取工程方案

工具会输出分层 ESLint 配置、CI 门禁 YAML、审查脚本与规范文档草稿.
### 第三步:落地与监控

```bash
# 应用配置后,本地验证
npx eslint . --max-warnings=0
npx tsc --noEmit
npx type-coverage --strict --at-least 95
# ...
# 生成首份基线报告
bash （请参考skill目录中的脚本文件）
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | typescript-skills处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "skills_result": "skills_result_value",
      "skills_metadata": "skills_metadata_value",
      "skills_status": "skills_status_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/typescript-skills_template`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **Node.js**:建议 20 LTS+
- **TypeScript**:建议 5.0+
- **CI 平台**:GitHub Actions / GitLab CI / Jenkins / Azure Pipelines

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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

## 案例展示

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
# （请参考skill目录中的脚本文件） — 从 ESLint 规则生成规范文档
set -euo pipefail
# ...
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
# ...
echo "规范文档已生成:$OUTPUT"
```

## 常见问题

### Q1: 团队已有大量历史代码不符合新规则,如何落地?

采用渐进式策略:1) 新规则设为 `warn` 而非 `error`,先生成报告;2) 在 CI 中仅对新增/修改文件强制 `error`;3) 设置治理里程碑,逐步清理存量违规.
### Q2: 多包仓库如何保证规范一致性?

共享 ESLint 基线配置包,子包通过 `extends` 继承。配合 `eslint --print-config` 校验最终配置,确保无意外覆盖.
### Q3: `import/no-cycle` 报错很多,如何处理?

循环依赖通常反映架构问题。短期可在 `overrides` 中对特定目录关闭规则,长期通过分层重构(提取共享模块)消除循环.
### Q4: 规范文档如何与代码保持同步?

使用 `（请参考skill目录中的脚本文件）` 在 CI 中自动重新生成规范文档,若文档与规则集不一致则阻断 PR。规范变更通过修改规则集 PR 一次性完成.
### Q5: Pro 版与免费版如何协同?

Pro 版完全兼容免费版的所有规范建议。个人开发者可继续使用免费版,团队场景启用 Pro 版获得自动化审查与企业级能力。两个版本可在同一仓库并存.
### Q6: 如何度量团队规范成熟度?

跟踪三个指标:ESLint 违规密度(违规数 / 千行)、类型覆盖率、CI 规范门禁通过率。三者共同反映规范成熟度.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

