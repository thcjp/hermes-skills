---
slug: "typescript-toolkit"
name: "typescript-toolkit"
version: "1.0.0"
displayName: "TypeScript工具集(专业版)"
summary: "面向团队与企业的TypeScript类型安全平台,含批量迁移、CI集成、规范审查与高级泛型工程。"
license: "Proprietary"
edition: "pro"
description: |-
  TypeScript工具集专业版为团队与企业提供端到端类型安全工程能力,涵盖批量JS→TS迁移、CI流水线集成、企业级规范审查与高级泛型设计。核心能力:
  - 批量代码迁移与渐进式类型化策略
  - 企业级tsconfig与ESLint规则集
  - 高级泛型、条件类型、映射类型工程化设计
  - CI/CD流水线类型检查与质量门禁
  - 团队规范文档自动生成与代码审查

  适用场景:
  - 中大型团队TypeScript规范统一与落地
  - 遗留JavaScript代码库渐进式迁移
  - 企业CI流水线类型安全门禁
  - 跨团队代码...
tags:
  - TypeScript
  - 类型系统
  - 企业开发
  - 工程规范
  - CI/CD
  - 代码审查
  - 团队协作
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
tools: ["read", "exec", "glob", "grep"]
tags: "工具,效率,自动化"
---
# TypeScript工具集(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |
| 零日漏洞检测与防护规则下发 | 不支持 | 支持 |

## 核心能力

| 能力 | 说明 | 是否兼容免费版 |
|:-----|:-----|:-----|
| 类型收窄与字面量陷阱 | 免费版全部能力 | 完全兼容 |
| 批量 JS→TS 迁移 | 渐进式类型化、JSDoc 类型、`allowJs` 策略 | Pro 新增 |
| 企业 tsconfig 模板 | 多包仓库、路径别名、项目引用、增量编译 | Pro 新增 |
| 高级泛型工程 | 条件类型、映射类型、模板字面量类型、类型递归 | Pro 新增 |
| CI/CD 集成 | GitHub Actions、GitLab CI 类型检查与质量门禁 | Pro 新增 |
| 规范文档自动生成 | 从代码注释生成 API 文档与团队规范 | Pro 新增 |
| 团队代码审查 | PR 级别类型安全审查与规则一致性检查 | Pro 新增 |
### 类型收窄与字面量陷阱

针对类型收窄与字面量陷阱,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供类型收窄与字面量陷阱相关的配置参数、输入数据和处理选项。

**输出**: 返回类型收窄与字面量陷阱的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`类型收窄与字面量陷阱`的配置文档进行参数调优
### 批量 JS→TS 迁移

针对批量 JS→TS ,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供批量 JS→TS 迁移相关的配置参数、输入数据和处理选项。

**输出**: 返回批量 JS→TS 迁移的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`批量 JS→TS 迁移`的配置文档进行参数调优
### 企业 tsconfig 模板

针对企业 tsconfig 模板,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供企业 tsconfig 模板相关的配置参数、输入数据和处理选项。

**输出**: 返回企业 tsconfig 模板的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`企业 tsconfig 模板`的配置文档进行参数调优
#
## 适用场景

### 场景 1:批量 JavaScript → TypeScript 渐进式迁移

企业遗留 JS 代码库需要分阶段迁移到 TS,本工具生成迁移路线图与每阶段配置。

```bash
# 优秀阶段:允许 JS 文件,启用 JSDoc 类型检查
npx tsc --init --allowJs --checkJs --noEmit
# ...
# 第二阶段:为高优先级模块添加 .d.ts 声明
npx tsc --declaration --emitDeclarationOnly --outDir types
# ...
# 第三阶段:逐模块重命名为 .ts 并启用严格模式
npx tsc --strict --noImplicitAny --strictNullChecks
```

迁移路线图示例:

| 阶段 | 目标 | 配置关键项 | 验证方式 |
|---:|---:|---:|---:|
| 1 | 启用 JS 类型检查 | `allowJs`、`checkJs` | `tsc --noEmit` 无错误 |
| 2 | 添加声明文件 | `declaration`、`emitDeclarationOnly` | 类型声明可被其他模块导入 |
| 3 | 重命名为 `.ts` | `strict`、`noImplicitAny` | 单模块 `tsc --noEmit` 通过 |
| 4 | 启用全量严格 | `strict`、`noUncheckedIndexedAccess` | 全仓库 `tsc --noEmit` 通过 |

### 场景 2:企业级 `tsconfig.json` 多包仓库配置

```jsonc
// 根 tsconfig.json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022"],
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noFallthroughCasesInSwitch": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "composite": true,
    "incremental": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "paths": {
      "@shared/*": ["./packages/shared/src/*"],
      "@core/*": ["./packages/core/src/*"]
    }
  },
  "references": [
    { "path": "./packages/shared" },
    { "path": "./packages/core" },
    { "path": "./packages/api" }
  ]
}
```

### 场景 3:CI/CD 类型安全门禁

在 GitHub Actions 中集成类型检查与 ESLint,作为 PR 合并的前置门禁。

```yaml
# .github/workflows/typecheck.yml
name: TypeScript Quality Gate
on:
  pull_request:
    branches: [main, release/*]
jobs:
  typecheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - name: 类型检查
        run: npx tsc --noEmit --pretty
      - name: ESLint 检查
        run: npx eslint . --max-warnings=0
      - name: 类型覆盖率
        run: npx type-coverage --detail --strict --at-least 95
```

## 使用流程

### 优秀步:声明企业规范

在对话中说明团队规模、项目类型与质量要求,例如:

```
我们是 30 人的前端团队,正在把一个有 5 年历史的 JS 代码库迁移到 TS,
需要分 6 个月完成的迁移路线图,以及每个阶段的 CI 门禁配置。
```

### 第二步:获取工程方案

工具会输出迁移路线图、`tsconfig` 分层配置、CI 流水线 YAML 与团队规范文档草稿。

### 第三步:落地与监控

将配置应用到仓库,通过 CI 门禁监控类型覆盖率与错误数,定期复盘。

```bash
# 监控类型覆盖率趋势
npx type-coverage --detail --strict --at-least 95 --ignore-catch
# ...
# 输出未类型化代码热点
npx type-coverage --detail --strict | grep -E "^[^|]+\\| +[0-9]+%" | sort -t'|' -k2 -n
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | typescript-toolkit处理的内容输入 |,  |
| content | string | 否 | typescript-toolkit处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **Node.js**:建议 20 LTS+(支持 `--experimental-vm-modules` 等 CI 特性)
- **TypeScript**:建议 5.0+
- **CI 平台**:GitHub Actions / GitLab CI / Jenkins / Azure Pipelines

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| TypeScript | npm 包 | 必需 | `npm i -D typescript` |
| ESLint + @typescript-eslint | npm 包 | 必需 | `npm i -D eslint @typescript-eslint/eslint-plugin @typescript-eslint/parser` |
| type-coverage | npm 包 | 推荐 | `npm i -D type-coverage` |
| Prettier | npm 包 | 推荐 | `npm i -D prettier` |
| sonarjs 插件 | npm 包 | 可选 | `npm i -D eslint-plugin-sonarjs` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 完全基于 Markdown 指令,无需额外 API Key
- CI 中如需访问私有 npm 注册表,配置 `NODE_AUTH_TOKEN` 环境变量
- 如集成 SonarQube 云端分析,需配置 `SONAR_TOKEN`

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言指令驱动 Agent 输出企业级类型工程方案;CI 集成需要在仓库中落地 YAML 与 npm 脚本,由 CI 运行器执行

## 案例展示

### 企业级 ESLint 规则集

```jsonc
{
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "project": "./tsconfig.json",
    "sourceType": "module"
  },
  "plugins": ["@typescript-eslint", "import", "sonarjs"],
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking",
    "plugin:sonarjs/recommended"
  ],
  "rules": {
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/explicit-function-return-type": "error",
    "@typescript-eslint/no-unused-vars": ["error", { "argsIgnorePattern": "^_" }],
    "@typescript-eslint/consistent-type-imports": "error",
    "@typescript-eslint/no-non-null-assertion": "error",
    "@typescript-eslint/prefer-nullish-coalescing": "error",
    "@typescript-eslint/prefer-optional-chain": "error",
    "@typescript-eslint/strict-boolean-expressions": "warn",
    "@typescript-eslint/naming-convention": [
      "error",
      { "selector": "typeLike", "format": ["PascalCase"] },
      { "selector": "variable", "format": ["camelCase", "UPPER_CASE"] }
    ],
    "import/order": ["error", { "groups": ["builtin", "external", "internal", "parent", "sibling"] }],
    "sonarjs/cognitive-complexity": ["error", 15]
  }
}
```

### 高级泛型示例:类型安全的事件总线

```typescript
// 利用条件类型与映射类型实现类型安全的事件总线
type EventHandler<T> = (payload: T) => void;
// ...
type EventMap = {
  'user:created': { id: string; name: string };
  'user:deleted': { id: string };
  'order:paid': { orderId: string; amount: number };
};
// ...
class TypedEventBus<TMap extends Record<string, unknown>> {
  private handlers: { [K in keyof TMap]?: EventHandler<TMap[K]>[] } = {};
// ...
  on<K extends keyof TMap>(event: K, handler: EventHandler<TMap[K]>): void {
    (this.handlers[event] ??= []).push(handler);
  }
// ...
  emit<K extends keyof TMap>(event: K, payload: TMap[K]): void {
    this.handlers[event]?.forEach((h) => h(payload));
  }
}
// ...
const bus = new TypedEventBus<EventMap>();
bus.on('user:created', (p) => console.log(p.name));  // p.name 类型安全
bus.emit('user:created', { id: '1', name: 'Alice' }); // OK
// bus.emit('user:created', { id: '1' });              // 编译错误:缺少 name
```

## 常见问题

### 依赖说明(补充)

启用 `allowJs` 与 `checkJs`,优先为公共入口编写 `.d.ts` 声明;对无类型的第三方库使用 `// @ts-expect-error` 临时抑制,并登记技术债务跟踪。

### Q2: 多包仓库的 `tsconfig` 应该集中还是分散?

推荐根配置集中定义通用项,子包用 `extends` 继承并仅覆盖差异。配合 `composite: true` 与项目引用,可获得增量编译加速。

### Q3: CI 中 `tsc --noEmit` 太慢,如何优化?

1) 启用 `incremental: true` 与 `composite`,利用 `.tsbuildinfo` 缓存;2) 使用项目引用,只检查受影响的包;3) 在 CI 中并行执行多个 `tsc` 实例分片检查。

### Q4: `exactOptionalPropertyTypes` 启用后大量报错怎么办?

该选项语义严格,建议分阶段启用:先在新建模块中开启,存量模块通过 `// @ts-ignore` 临时抑制,逐步清理。

### Q5: Pro 版与免费版如何协同?

Pro 版完全兼容免费版的所有建议输出。个人开发者可继续使用免费版,团队场景启用 Pro 版获得企业级能力。两个版本可在同一仓库并存,无冲突。

### Q6: 如何度量团队的类型安全成熟度?

建议跟踪三个指标:类型覆盖率(`type-coverage`)、`any` 使用密度(`grep -r ": any" src | wc -l` 除以文件数)、CI 类型检查通过率。三者共同反映类型安全成熟度。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

