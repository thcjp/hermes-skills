---
slug: "solo-build-free"
name: "solo-build-free"
version: "1.0.0"
displayName: "构建执行引擎(免费版)"
summary: "执行实现计划任务,TDD工作流,自动提交,阶段门检查,进度跟踪。(免费版)"
license: "MIT"
description: |-
  执行实现计划任务的引擎:轨道选择、上下文加载、任务恢复、
  TDD工作流、集成测试、阶段门检查、错误处理与进度跟踪。覆盖
  Python/JS-TS/iOS/Android多栈质量工具与理性化防护。适用于
  独立开发者、企业团队和自动化工作流场景。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 创意设计
---
# 构建执行引擎(免费版)

执行实现计划中的任务,采用TDD工作流、自动提交与阶段门检查。从 `plan.md` 选取下一个未完成任务,实现、提交、更新进度,直至全部完成。

## 核心能力

### 1. 轨道选择
- 通过参数指定轨道ID:验证 `{plan_root}/{argument}/plan.md` 存在
- 通过 `--task X.Y` 跳转到指定任务
- 无参数时:搜索 `docs/plan/` 下所有 `plan.md`,列出有未完成任务的轨道,多个时询问用户

**输出**: 返回轨道选择的执行结果,包含操作状态和输出数据。
### 2. 上下文加载
并行读取必要文档,不读源码:
- `docs/plan/{trackId}/plan.md` — 任务列表(必需)
- `docs/plan/{trackId}/spec.md` — 验收标准(必需)
- `docs/workflow.md` — TDD策略、提交策略(若存在)
- 项目配置文档 — 架构、Do/Don't
- `.solo/pipelines/progress.md` — 前次迭代记录(若存在)

**输入**: 用户提供上下文加载所需的指令和必要参数。
**处理**: 按照skill规范执行上下文加载操作,遵循单一意图原则。
**输出**: 返回上下文加载的执行结果,包含操作状态和输出数据。

### 3. 任务恢复
检测 `plan.md` 中 `[~]` 标记的中断任务:
- 显示:上次任务、当前进度
- 选项:从断点继续 / 重启当前任务 / 先看进度摘要
- 通过询问用户后继续

**处理**: 按照skill规范执行任务恢复操作,遵循单一意图原则。
**输出**: 返回任务恢复的执行结果,包含操作状态和输出数据。

### 4. 任务执行循环
扫描 `plan.md` 中所有 `- [ ]` 或 `- [~]` 任务,若全部 `[x]` 则跳到完成流程。否则逐个执行:
1. 查找下一个任务:解析 `- [ ] Task X.Y:` 行
2. 启动任务:`[ ]` → `[~]`,宣布 "Starting Task X.Y"
3. 研究:用 `project_code_search` 找相关代码,只读top 2-3结果
4. TDD或直接实现
5. 集成测试
6. 完成任务:`[~]` → `[x]`,提交
7. 阶段完成检查


### 输出格式

执行结果以Markdown格式返回,包含操作状态(成功/失败)、处理摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。- 验证执行结果，确认输出符合预期格式
- 参考`输出格式`相关配置参数进行设置
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 执行计划 | plan.md + spec.md | 全部任务完成 + 提交记录 |
| 恢复中断 | [~]标记的任务 | 从断点继续 |
| 单任务执行 | --task X.Y | 该任务实现+测试+提交 |

不适用于:计划创建(用 `/plan`)、部署(用 `/deploy`)、代码审查(用 `/review`)、无plan.md的项目。

## 使用流程

1. 确认 `docs/plan/{trackId}/plan.md` 与 `spec.md` 存在
2. 用MCP工具或并行读取加载上下文(不读源码)
3. 扫描未完成任务,若全部完成跳到完成流程
4. 逐个执行任务:研究 → TDD/直接实现 → 集成测试 → 提交
5. 每阶段结束运行检查点
6. 全部完成后:最终验证 + 更新状态 + 输出 `<solo:done/>`

## 示例

### 示例:任务执行循环
```
Starting Task 2.1: 实现用户登录接口

1. 研究: project_code_search(query="login auth", project="myapp")
   找到 src/auth/login.ts,读取
2. TDD Red: 写 tests/login.test.ts,运行 `make test` 确认失败
3. TDD Green: 实现 src/auth/login.ts,运行 `make test` 确认通过
4. TDD Refactor: 提取重复代码,运行 `make test` 确认仍通过
5. 集成测试: `make integration` 通过
6. 完成: plan.md [~] → [x],git commit -m "feat(auth): implement login API"
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 无plan.md | 未运行 `/plan` 创建轨道 | 提示 "No plans found. Run /plan first." |
| 测试失败 | 实现破坏现有功能 | 尝试修复 → 失败则 `git checkout` 回滚 → 暂停等用户输入 |
| 阶段检查点失败 | 阶段边界测试或linter失败 | 修复后重跑该阶段验证,不跳过 |
| MCP工具不可用 | 未配置MCP或服务不可达 | 降级为Glob+Grep+Read,只读任务明确提到的文件 |

## 常见问题

### Q1: `plan.md` 中的任务状态标记 `[ ]`、`[~]`、`[x]` 有何区别?
A: `[ ]` 表示未开始;`[~]` 表示进行中(可恢复);`[x]` 表示完成。开始任务时 `[ ]` → `[~]`,完成时 `[~]` → `[x]`。恢复时检测 `[~]` 标记,询问用户从断点继续还是重启。

### Q2: 为何禁止 `Grep "keyword" .` 全项目搜索?
A: 全项目搜索会dump数百行无关内容到上下文,浪费token且稀释关键信息。应只读任务明确提到的文件路径,或Glob特定模块目录(`src/auth/**/*.ts`),或Grep窄模式只搜 `src/`。研究要surgical。

### Q3: TDD的Red-Green-Refactor如何执行?
A: Red — 写失败测试,运行 `make test` 确认失败;Green — 写最小代码使测试通过,运行确认通过;Refactor — 在测试保持green下清理代码,最后再运行一次。TDD为"none"时直接实现;"moderate"时只对业务逻辑与API写测试。

## 已知限制

- 需要LLM支持,无LLM环境无法执行
- 依赖 `plan.md` 与 `spec.md` 存在,无计划无法执行
- MCP工具不可用时降级为文件搜索,效率降低

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 升级提示

本免费版提供基础功能。升级到完整版 solo-build 获取全部能力和高级特性。
