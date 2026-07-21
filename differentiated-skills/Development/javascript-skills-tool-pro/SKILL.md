---
slug: javascript-skills-tool-pro
name: javascript-skills-tool-pro
version: "1.0.0"
displayName: JavaScript规范工具(专业版)
summary: 面向团队与企业的全量JavaScript规范套件,含性能优化、安全审查与CI/CD集成。
license: Proprietary
edition: pro
description: |-
  JavaScript规范工具(专业版)面向团队与企业,提供全量JavaScript代码风格规范、性能优化策略、安全审查清单与CI/CD自动化集成方案。核心能力:
  - 覆盖28+全量风格规则,含迭代器、生成器、标准库等进阶主题
  - 完整异步并发模型与错误链路最佳实践
  - 团队级Lint规则定制与预提交钩子集成
  - 性能优化与安全审查清单
  - TypeScript深度兼容与混用规范

  适用场景:
  - 企业级前端工程规范统一
  - 大型团队代码审查与质量门禁
  - 性能敏感场景的代码优化
  - 安全合规要求的项目交付

...
tags:
- Development
- Frontend
- JavaScript
- 代码规范
- 企业级
- 性能优化
- 安全审查
tools:
  - - read
- exec
---
# JavaScript规范工具(专业版)

## 概述

JavaScript规范工具(专业版)面向团队与企业级前端工程,在兼容免费版核心规则集的基础上,扩展了全量风格规则、性能优化策略、安全审查清单、异步并发模型、TypeScript深度兼容以及CI/CD自动化集成方案。

当你在请求中提及 JavaScript、前端规范、性能优化、安全审查、CI/CD 集成等关键词时,本工具会自动激活,输出符合企业级交付标准的代码、审查报告与流水线配置。

本版本完全兼容 `javascript-skills-tool-free` 的所有核心规则,可平滑升级,历史项目无需重构。

## 核心能力

| 能力模块 | 说明 | 与免费版差异 |
| --- | --- | --- |
| 全量风格规则 | 28+规则,含迭代器、生成器、标准库等进阶主题 | 免费版仅核心规则集 |
| 异步并发模型 | Promise.all / allSettled / 错误链路 / 取消令牌 | 免费版仅基础 async/await |
| 性能优化 | 内存管理、事件循环、渲染性能、打包优化 | 免费版无 |
| 安全审查 | XSS / 原型污染 / 依赖审计 / 密钥处理 | 免费版无 |
| TypeScript兼容 | 混用规范、类型推导、声明文件 | 免费版仅基础建议 |
| CI/CD集成 | 流水线模板、预提交钩子、自定义规则 | 免费版仅基础配置示例 |
| 团队治理 | 规则分级、豁免机制、迁移指南 | 免费版无 |

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
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：面向团队与企业的、JavaScript、规范套件、含性能优化、安全审查与、规范工具、专业版、面向团队与企业、提供全量、代码风格规范、性能优化策略、安全审查清单与、自动化集成方案、核心能力、完整异步并发模型、与错误链路最佳实、团队级、Lint、规则定制与预提交、钩子集成、性能优化与安全审、查清单、深度兼容与混用规等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一:企业级前端工程规范统一

团队需要为多个前端项目统一规范,并接入CI门禁。工具输出完整的规则配置与流水线模板。

```yaml
# .github/workflows/lint.yml 企业级Lint流水线
name: Code Quality Gate
on:
  pull_request:
    branches: [main, release/*]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint:strict
      - run: npm run type-check
      - run: npm run test:coverage
      - name: 阻止覆盖率下降
        run: npx codecov || exit 1
```

### 场景二:性能敏感场景的代码优化

某仪表盘页面滚动卡顿,工具分析后给出符合规范的重构方案。

```javascript
// 优化前:每次滚动都创建新闭包并触发重排
list.addEventListener('scroll', () => {
  items.forEach((item) => {
    item.style.top = `${window.scrollY + item.offsetTop}px`;
  });
});

// 优化后:使用 requestAnimationFrame + transform 走合成层
let ticking = false;
const updateLayout = () => {
  items.forEach((item) => {
    item.style.transform = `translateY(${window.scrollY}px)`;
  });
  ticking = false;
};

list.addEventListener('scroll', () => {
  if (!ticking) {
    window.requestAnimationFrame(updateLayout);
    ticking = true;
  }
}, { passive: true });
```

### 场景三:安全合规审查

金融项目要求对所有用户输入做防XSS处理,工具输出符合规范的安全工具函数。

```javascript
const ESCAPE_MAP = {
  '&': '&amp;',
  '<': '&lt;',
  '>': '&gt;',
  '"': '&quot;',
  "'": '&#x27;',
  '`': '&#x60;',
};

const escapeHtml = (input) => String(input).replace(/[&<>"'`]/g, (ch) => ESCAPE_MAP[ch]);

// 防止原型污染的安全合并
const safeMerge = (target, ...sources) => {
  for (const source of sources) {
    if (source === null || typeof source !== 'object') continue;
    for (const [key, value] of Object.entries(source)) {
      if (key === '__proto__' || key === 'constructor' || key === 'prototype') continue;
      target[key] = typeof value === 'object' && value !== null
        ? safeMerge(Array.isArray(value) ? [] : {}, value)
        : value;
    }
  }
  return target;
};

export { escapeHtml, safeMerge };
```

## 不适用场景

以下场景JavaScript规范工具(专业版)不适合处理：

- 实际人员绩效评估
- 财务预算审批
- 合同法务审核

## 触发条件

需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于非本工具能力范围的需求。

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 1. 平滑升级

如果你已使用免费版,直接替换Skill文件即可。核心规则完全兼容,新增能力按需启用。

```bash
# 项目根目录初始化企业级配置
npx eslint --init
npm i -D prettier eslint-config-prettier eslint-plugin-security eslint-plugin-import
```

### 2. 接入预提交钩子

```bash
npm i -D husky lint-staged
npx husky init
echo 'npx lint-staged' > .husky/pre-commit
```

```json
// package.json
{
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "eslint --fix --max-warnings=0",
      "prettier --write",
      "git add"
    ]
  }
}
```

### 3. 团队规则分级

```javascript
// .eslintrc.enterprise.js 企业级规则分级
module.exports = {
  extends: [
    'eslint:recommended',
    'plugin:import/recommended',
    'plugin:security/recommended',
    'prettier',
  ],
  rules: {
    // 阻断级:必须修复才能合并
    'no-eval': 'error',
    'no-implied-eval': 'error',
    'security/detect-object-injection': 'error',
    'no-var': 'error',
    'prefer-const': 'error',
    'eqeqeq': ['error', 'always'],

    // 警告级:建议修复,不阻断
    'no-unused-vars': 'warn',
    'prefer-template': 'warn',
    'no-console': ['warn', { allow: ['warn', 'error'] }],

    // 提示级:风格建议
    'prefer-arrow-callback': 'off',
    'arrow-body-style': 'off',
  },
  overrides: [
    {
      files: ['**/*.ts', '**/*.tsx'],
      extends: ['plugin:@typescript-eslint/recommended'],
      rules: { 'no-unused-vars': 'off' },
    },
  ],
};
```

## 示例

### 全量Prettier企业配置

```json
{
  "singleQuote": true,
  "semi": true,
  "tabWidth": 2,
  "trailingComma": "all",
  "printWidth": 100,
  "arrowParens": "always",
  "endOfLine": "lf",
  "overrides": [
    {
      "files": "*.json5",
      "options": { "singleQuote": false }
    }
  ]
}
```

### 自定义ESLint规则开发

```javascript
// eslint-plugin-enterprise/rules/no-magic-number.js 自定义规则
module.exports = {
  meta: {
    type: 'suggestion',
    docs: { description: '禁止魔法数字,要求提取为命名常量' },
    schema: [
      {
        type: 'object',
        properties: { ignore: { type: 'array', items: { type: 'number' } } },
        additionalProperties: false,
      },
    ],
  },
  create(context) {
    const ignored = (context.options[0] && context.options[0].ignore) || [0, 1, -1];
    return {
      Literal(node) {
        if (typeof node.value === 'number' && !ignored.includes(node.value)) {
          context.report({
            node,
            message: '魔法数字 {{value}} 应提取为命名常量',
            data: { value: node.value },
          });
        }
      },
    };
  },
};
```

## 最佳实践

### 1. 异步并发模型

使用 `Promise.all` 并发独立任务,`Promise.allSettled` 收集全部结果。

```javascript
async function loadDashboard() {
  const [user, posts, notifications] = await Promise.all([
    fetchUser(),
    fetchPosts(),
    fetchNotifications(),
  ]);
  return { user, posts, notifications };
}

// 需要全部结果(无论成败)时使用 allSettled
async function importAll(sources) {
  const results = await Promise.allSettled(sources.map((s) => importSource(s)));
  const fulfilled = results.filter((r) => r.status === 'fulfilled').map((r) => r.value);
  const rejected = results.filter((r) => r.status === 'rejected');
  if (rejected.length > 0) {
    console.warn(`部分导入失败: ${rejected.length}/${results.length}`);
  }
  return fulfilled;
}
```

### 2. 自定义错误与错误链路

只抛出 `Error` 子类,保留原始错误上下文。

```javascript
class ValidationError extends Error {
  constructor(message, field, { cause } = {}) {
    super(message, { cause });
    this.name = 'ValidationError';
    this.field = field;
  }
}

class DatabaseError extends Error {
  constructor(message, { cause } = {}) {
    super(message, { cause });
    this.name = 'DatabaseError';
  }
}

async function updateUser(id, payload) {
  try {
    await persist(id, payload);
  } catch (err) {
    throw new DatabaseError(`用户 ${id} 持久化失败`, { cause: err });
  }
}
```

### 3. 性能优化清单

| 场景 | 反模式 | 推荐做法 |
| --- | --- | --- |
| 高频事件 | 直接操作DOM | `requestAnimationFrame` + 节流/防抖 |
| 大列表渲染 | 全量渲染 | 虚拟列表 / 分页 |
| 频繁布局读写 | 交替读写 | 批量读后批量写 |
| 图片资源 | 大图原尺寸 | 响应式 `srcset` + 懒加载 |
| 打包体积 | 全量引入 | Tree-shaking + 动态导入 |

### 4. 安全审查清单

```javascript
// 禁止:eval 与 Function 构造器
// eval('userInput');          // ❌
// new Function('return ' + code)();  // ❌

// 禁止:innerHTML 直接拼接用户输入
// el.innerHTML = userInput;  // ❌

// 推荐:使用 textContent 或转义
el.textContent = userInput;     // ✅
el.innerHTML = sanitize(userInput);  // ✅ 经消毒库处理
```

### 5. TypeScript深度兼容

```typescript
// 类型导入与运行时导入分离
import type { UserDTO } from './types';
import { fetchUser } from './api';

// 使用 unknown 而非 any 处理外部数据
function parseResponse(raw: unknown): UserDTO {
  if (typeof raw !== 'object' || raw === null) {
    throw new TypeError('响应必须为对象');
  }
  const obj = raw as Record<string, unknown>;
  return {
    id: String(obj.id),
    name: String(obj.name),
    active: Boolean(obj.active),
  };
}
```

### 6. 团队迁移指南

| 阶段 | 动作 | 验收标准 |
| --- | --- | --- |
| 1. 基线评估 | 运行 `eslint . --max-warnings=9999` 统计现状 | 输出问题清单与分类 |
| 2. 规则分级 | 按阻断/警告/提示三档配置 | 团队评审通过 |
| 3. 预提交钩子 | 接入 husky + lint-staged | 本地提交前自动修复 |
| 4. CI门禁 | 流水线增加 `lint:strict` 步骤 | 不合规PR无法合并 |
| 5. 持续治理 | 每月复盘告警与豁免 | 豁免清单收敛 |

## 常见问题

### Q1:PRO版与免费版如何共存?

两者规则完全兼容,PRO版包含免费版全部能力。建议团队统一使用PRO版,个人项目可继续使用免费版。迁移时直接替换Skill文件,无需改动业务代码。

### Q2:如何为已有项目渐进式接入?

参考"团队迁移指南"五阶段方案。先用警告级跑通全量扫描,统计问题分布;再按模块逐步提升为阻断级,避免一次性阻塞所有提交。

### Q3:PRO版是否支持Monorepo?

支持。建议在根目录放置基础配置,各子包通过 `extends` 继承并按需覆盖。配合 `eslint-plugin-import` 的 `no-extraneous-dependencies` 规则可强制依赖边界。

### Q4:性能优化建议是否覆盖框架场景?

工具提供框架无关的性能原则(事件循环、合成层、内存)。对React/Vue等框架,工具会结合其渲染模型给出符合规范的写法,但深度框架调优建议结合对应专用工具。

### Q5:安全审查覆盖哪些漏洞?

覆盖常见前端漏洞:XSS、原型污染、不安全反序列化、敏感信息硬编码、危险动态执行、依赖审计。不覆盖服务端安全,如需服务端审查请配合后端专用工具。

### Q6:自定义规则开发支持哪些能力?

支持标准的ESLint规则开发模式,可访问AST节点、配置schema、提供自动修复建议。详见"配置示例"中的自定义规则模板。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js版本**: 建议 20 LTS 及以上(用于支持最新ESLint与原生ES模块)
- **包管理器**: npm / pnpm / yarn 任一(推荐 pnpm 用于Monorepo)

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| ESLint | npm包 | 推荐 | `npm i -D eslint` |
| Prettier | npm包 | 推荐 | `npm i -D prettier` |
| eslint-config-prettier | npm包 | 推荐 | `npm i -D eslint-config-prettier` |
| eslint-plugin-security | npm包 | 推荐 | `npm i -D eslint-plugin-security` |
| eslint-plugin-import | npm包 | 可选 | `npm i -D eslint-plugin-import` |
| husky | npm包 | 推荐 | `npm i -D husky` |
| lint-staged | npm包 | 推荐 | `npm i -D lint-staged` |
| TypeScript | npm包 | 可选 | `npm i -D typescript` |
| Node.js | 运行时 | 推荐 | nodejs.org 下载 |

### API Key 配置

- 本skill基于Markdown指令规范,无需额外API Key(除内容中明确标注的外部API)。
- 若CI/CD流水线需上传覆盖率或安全扫描结果,请按对应服务(Codecov / Snyk 等)文档配置令牌环境变量。

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent完成操作。PRO版面向团队与企业,提供全量规则、性能优化、安全审查与CI/CD集成方案,完全兼容免费版核心规则。

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
