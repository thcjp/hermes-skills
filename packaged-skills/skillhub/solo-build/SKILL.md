---
slug: "solo-build"
name: "solo-build"
version: 2.2.2
displayName: "构建执行引擎"
summary: "执行实现计划任务,TDD工作流,自动提交,阶段门检查,进度跟踪。。执行实现计划任务的引擎:轨道选择、上下文加载、任务恢复、 TDD工作流、集成测试、视觉验证、阶段门检查、错误处理与进度 跟踪"
license: "MIT"
description: |-
  执行实现计划任务的引擎:轨道选择、上下文加载、任务恢复、
  TDD工作流、集成测试、视觉验证、阶段门检查、错误处理与进度
  跟踪。覆盖Python/JS-TS/iOS/Android多栈质量工具与理性化
  防护.
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 创意设计
  - UI设计
  - 前端
  - 设计
  - 包含执行
  - 状态码
  - 结果数据
  - 和执行日
  - plan
category: "Creative"
---
# 构建执行引擎

执行实现计划中的任务,采用TDD工作流、自动提交与阶段门检查。从 `plan.md` 选取下一个未完成任务,实现、提交、更新进度,直至全部完成.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 构建执行引擎处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 轨道选择
- 通过参数指定轨道ID:验证 `{plan_root}/{argument}/plan.md` 存在
- 通过 `--task X.Y` 跳转到指定任务
- 无参数时:搜索 `docs/plan/` 下所有 `plan.md`,列出有未完成任务的轨道,多个时询问用户

**输出**: 返回轨道选择的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 上下文加载
并行读取必要文档,不读源码:
- `docs/plan/{trackId}/plan.md` — 任务列表(必需)
- `docs/plan/{trackId}/spec.md` — 验收标准(必需)
- `docs/workflow.md` — TDD策略、提交策略(若存在)
- 项目配置文档 — 架构、Do/Don't
- `.solo/pipelines/progress.md` — 前次迭代记录(若存在)

**输入**: 用户提供上下文加载所需的指令和必要参数.
**处理**: 解析上下文加载的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回上下文加载的处理结果,包含执行状态码、结果数据和执行日志.
### 3. 架构概览(若MCP工具可用)
- `codegraph_explain(project="{project name}")` 一次调用返回技术栈、语言、目录层级、关键模式、主要依赖、枢纽文件
- 避免手动遍历目录树

- 参考`架构概览(若MCP工具可用)`的配置文档进行参数调优
### 4. 任务恢复
检测 `plan.md` 中 `[~]` 标记的中断任务:
- 显示:上次任务、当前进度
- 选项:从断点继续 / 重启当前任务 / 先看进度摘要
- 通过询问用户后继续

**处理**: 解析任务恢复的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回任务恢复的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 任务执行循环
扫描 `plan.md` 中所有 `- [ ]` 或 `- [~]` 任务,若全部 `[x]` 则跳到完成流程。否则逐个执行:
1. 查找下一个任务:解析 `- [ ] Task X.Y:` 行
2. 启动任务:`[ ]` → `[~]`,宣布 "Starting Task X.Y"
3. 研究:用 `project_code_search` 找相关代码,只读top 2-3结果
4. TDD或直接实现
5. 集成测试
6. 完成任务:`[~]` → `[x]`,提交
7. 阶段完成检查

**输入**: 用户提供任务执行循环所需的指令和必要参数.
### 6. 智能研究
- MCP可用:`project_code_search(query="{task keywords}")` 找相关代码
- MCP可用:`session_search("{task keywords}")` 查历史解决方案
- MCP可用:`codegraph_query` 检查文件依赖与导入
- MCP不可用:只读任务描述中明确提到的文件路径;Glob特定模块目录;Grep窄模式只搜 `src/` 或 `app/`
- 禁止:`Grep "keyword" .` 全项目搜索

**输入**: 用户提供智能研究所需的指令和必要参数.
**输出**: 返回智能研究的处理结果,包含执行状态码、结果数据和执行日志.
### 7. TDD工作流
- Red:写失败测试,运行确认失败
- Green:写最小代码使测试通过,运行确认通过
- Refactor:在测试保持green下清理代码,最后再运行一次

**输入**: 用户提供TDD工作流所需的指令和必要参数.
**输出**: 返回TDD工作流的处理结果,包含执行状态码、结果数据和执行日志.
### 8. 非TDD工作流
- TDD为"none":直接实现,运行现有测试确认无破坏
- TDD为"moderate":业务逻辑与API路由写测试,UI/配置跳过

**输入**: 用户提供非TDD工作流所需的指令和必要参数.
**输出**: 返回非TDD工作流的处理结果,包含执行状态码、结果数据和执行日志.
### 9. 集成测试(CLI优先)
- 任务触及核心业务逻辑(流水线、算法、代理工具)时,运行 `make integration`
- CLI执行与UI相同代码路径,无需浏览器
- `make integration` 失败则修复后再提交

**输入**: 用户提供集成测试(CLI优先)所需的指令和必要参数.
**输出**: 返回集成测试(CLI优先)的处理结果,包含执行状态码、结果数据和执行日志.
### 10. 视觉验证
- Web:启动dev server,导航主页,检查console,截图
- iOS:构建+安装模拟器,启动,截图,检查日志
- Android:构建APK+安装模拟器,启动,截图,检查logcat
- 工具不可用时跳过,非完成阻塞项

**输入**: 用户提供视觉验证所需的指令和必要参数.
**输出**: 返回视觉验证的处理结果,包含执行状态码、结果数据和执行日志.
### 11. 多栈质量工具
- Python:`ruff check --fix`、`mypy`、`pytest -q`
- JS/TS:`pnpm lint`、`pnpm typecheck`、`pnpm test --reporter=dot`
- iOS(Swift):`swiftlint lint --strict`、`swift-format format --in-place --recursive Sources/`
- Android(Kotlin):`./gradlew detekt`、`./gradlew ktlintCheck`
- Makefile约定:优先 `make test`/`make lint`/`make build` 而非原始命令

**处理**: 解析多栈质量工具的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回多栈质量工具的处理结果,包含执行状态码、结果数据和执行日志.
### 12. 阶段完成检查
- 每阶段结束:运行测试 + linter,通过后进入下一阶段
- 失败则修复,不跳过

**输入**: 用户提供阶段完成检查所需的指令和必要参数.
**输出**: 返回阶段完成检查的处理结果,包含执行状态码、结果数据和执行日志.
### 13. 错误处理
测试失败处理:
- 显示失败详情
- 选项:尝试修复 / 回滚任务(git checkout) / 暂停人工介入
- 不自动跳过失败

**输入**: 用户提供错误处理所需的指令和必要参数.
**输出**: 返回错误处理的处理结果,包含执行状态码、结果数据和执行日志.
### 14. 轨道完成
全部任务 `[x]` 后:
- 最终验证:本地构建(`pnpm build`/`uv build`/`xcodebuild`/`./gradlew assembleDebug`)+ 全套测试 + linter + 视觉smoke test
- 更新 `plan.md`: `**Status:** [ ] Not Started` → `**Status:** [x] Complete`
- 输出完成信号 `<solo:done/>`(仅当 `.solo/states/` 存在时)
- 汇总:任务数、提交数、测试通过率、耗时

**处理**: 解析轨道完成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 15. 进度跟踪
- 会话开始:读 `plan.md`,为每个阶段创建任务列表
- 工作中:`in_progress` 开始任务,`completed` 完成
- 实时可见进度

**输入**: 用户提供进度跟踪所需的指令和必要参数.
**处理**: 解析进度跟踪的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 16. 理性化防护目录
| 想法 | 现实 |
|:---:|:---:|
| "太简单不用测试" | 简单代码也会坏,写测试 |
| "以后加测试" | 后写的测试立即通过,证明不了什么 |
| "我手动测过了" | 手动测试不持久,自动化才持久 |
| "只是配置改动" | 配置改动破坏构建,验证 |
| "我有信心能用" | 无证据的信心是猜测,运行命令 |
| "测试过了,发布" | 测试通过 ≠ 满足验收标准,检查 spec.md |

**输入**: 用户提供理性化防护目录所需的指令和必要参数.
**输出**: 返回理性化防护目录的处理结果,包含执行状态码、结果数据和执行日志.
### 17. 关键规则
1. 运行阶段检查点:测试+linter通过才进下一阶段
2. 失败即停:不跳过测试失败
3. 保持 `plan.md` 更新:任务状态反映实际进度
4. 每任务提交:原子提交,conventional格式
5. 编码前研究:30秒搜索省30分钟重写
6. 一次一任务:完成当前再开始下一个
7. 测试输出精简:`head -50` 或 `--reporter=dot`/`-q`,只显示失败详情
8. 验证后再说完成:运行命令、读完整输出、确认成功后再标记完成

### 输出格式

完成响应以Markdown格式返回,包含任务状态(成功/失败)、解析摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。- 验证返回数据的完整性和格式正确性
- 参考`输出格式`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:------|------:|:------|
| 执行计划 | plan.md + spec.md | 全部任务完成 + 提交记录 |
| 恢复中断 | [~]标记的任务 | 从断点继续 |
| 单任务执行 | --task X.Y | 该任务实现+测试+提交 |
| 阶段验证 | 阶段结束 | 测试+linter检查通过 |
| 最终验证 | 全部任务[x] | 构建+测试+视觉验证+完成信号 |

不适用于:计划创建(用 `/plan`)、部署(用 `/deploy`)、代码审查(用 `/review`)、无plan.md的项目.
## 使用流程

1. 确认 `docs/plan/{trackId}/plan.md` 与 `spec.md` 存在
2. 用MCP工具或并行读取加载上下文(不读源码)
3. 扫描未完成任务,若全部完成跳到完成流程
4. 逐个执行任务:研究 → TDD/直接实现 → 集成测试 → 提交
5. 每阶段结束运行检查点
6. 全部完成后:最终验证 + 更新状态 + 输出 `<solo:done/>`

## 示例

### 示例1:任务执行循环
```
Starting Task 2.1: 实现用户登录接口
# ...
1. 研究: project_code_search(query="login auth", project="myapp")
   找到 src/auth/login.ts,读取
2. TDD Red: 写 tests/login.test.ts,运行 `make test` 确认失败
3. TDD Green: 实现 src/auth/login.ts,运行 `make test` 确认通过
4. TDD Refactor: 提取重复代码,运行 `make test` 确认仍通过
5. 集成测试: `make integration` 通过
6. 完成: plan.md [~] → [x],git commit -m "feat(auth): implement login API"
```

### 示例2:错误处理
```
Tests failing after Task 3.2:
  FAIL  tests/payment.test.js
  ● payment processor › should reject invalid card
# ...
  Expected: rejected
  Received: accepted
# ...
1. Attempt to fix
2. Rollback task changes (git checkout)
3. Pause for manual intervention
```

### 示例3:阶段检查点
```
Phase 2 Complete. Running checkpoint:
  $ make test
  Tests: 45 passed, 0 failed
  $ make lint
  No issues found
Checkpoint passed. Proceeding to Phase 3.
```

### 示例4:轨道完成信号
```
All tasks complete. Final verification:
  $ pnpm build
  ✓ Build successful
  $ make test
  Tests: 120 passed, 0 failed
# ...
**Status:** [x] Complete
# ...
<solo:done/>
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 无plan.md | 未运行 `/plan` 创建轨道 | 提示 "No plans found. Run /plan first." |
| 测试失败 | 实现破坏现有功能 | 尝试修复 → 失败则 `git checkout` 回滚 → 暂停等用户输入 |
| 阶段检查点失败 | 阶段边界测试或linter失败 | 修复后重跑该阶段验证,不跳过 |
| MCP工具不可用 | 未配置MCP或服务不可达 | 降级为Glob+Grep+Read,只读任务明确提到的文件 |
| Makefile不存在 | 项目无Makefile | 降级为原始命令:`pnpm test`/`pytest -q`/`xcodebuild` |
| 视觉工具不可用 | 无浏览器/模拟器 | 跳过视觉验证,非完成阻塞项;记录跳过原因 |
| 理性化偷工减料 | "太简单不用测试"等想法 | 查理性化目录,停止偷工,按规则执行 |

## 常见问题

### Q1: `plan.md` 中的任务状态标记 `[ ]`、`[~]`、`[x]` 有何区别?
A: `[ ]` 表示未开始;`[~]` 表示进行中(可恢复);`[x]` 表示完成。开始任务时 `[ ]` → `[~]`,完成时 `[~]` → `[x]`。恢复时检测 `[~]` 标记,询问用户从断点继续还是重启.
### Q2: 为何禁止 `Grep "keyword" .` 全项目搜索?
A: 全项目搜索会dump数百行无关内容到上下文,浪费token且稀释关键信息。应只读任务明确提到的文件路径,或Glob特定模块目录(`src/auth/**/*.ts`),或Grep窄模式只搜 `src/`。研究要surgical.
### Q3: TDD的Red-Green-Refactor如何执行?
A: Red — 写失败测试,运行 `make test` 确认失败;Green — 写最小代码使测试通过,运行确认通过;Refactor — 在测试保持green下清理代码,最后再运行一次。TDD为"none"时直接实现;"moderate"时只对业务逻辑与API写测试.
### Q4: `make integration` 与 `make test` 有何区别?
A: `make test` 运行单元测试,快速反馈;`make integration` 运行集成测试,验证核心业务逻辑(流水线、算法、代理工具)的端到端行为。任务触及核心逻辑时两者都要运行,集成测试失败必须修复后再提交.
### Q5: `<solo:done/>` 信号何时输出?
A: 仅当 `.solo/states/` 目录存在(管道模式)且全部任务完成、最终验证通过时输出一次。不要在响应其他位置重复该标签。非管道模式不输出.
### Q6: 每任务提交的conventional格式是什么?
A: `type(scope): description`,如 `feat(auth): implement login API`、`fix(payment): reject invalid card`、`refactor(ui): extract common button`。type用feat/fix/refactor/test/docs/chore,scope为模块名,description为动词开头的小写陈述.
## 已知限制

- 需要LLM支持,无LLM环境无法执行
- 依赖 `plan.md` 与 `spec.md` 存在,无计划无法执行
- MCP工具不可用时降级为文件搜索,效率降低
- 视觉验证依赖浏览器/模拟器,无环境时跳过
- 不覆盖计划创建、部署、代码审查阶段
