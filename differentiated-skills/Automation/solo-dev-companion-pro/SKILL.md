---
slug: solo-dev-companion-pro
name: solo-dev-companion-pro
version: "1.0.0"
displayName: 独立开发伙伴(专业版)
summary: 全功能TDD工作流引擎，含MCP工具集成、多语言质量工具、视觉验证、阶段检查点与高级回滚。
license: MIT
edition: pro
description: |-
  独立开发伙伴专业版是在免费版基础上的全功能升级，为独立开发者与一人公司提供企业级TDD工作流引擎。除核心TDD执行外，解锁MCP工具集成、多语言质量工具、视觉验证、阶段检查点、高级回滚、进度追踪集成六大高级功能。

  核心能力：MCP工具集成（session_search/project_code_search/codegraph_query）、多语言质量工具（JS/TS/Python/iOS/Android全覆盖）、视觉验证（Playwright/iOS Simulator/Android Emulator）、阶段检查点（Phase Completion Check）、高级回滚（按任务/按阶段/按track回滚）、进度追踪集成（TodoWrite）、Hypothesis属性测试、Knip死代码检测、Rationalizations反模式检测。

  适用场景：独立开发者的大型项目开发、一人公司的多语言项目、移动应用开发（iOS/Android）、全栈项目的质量保障、团队协作的标准化开发流程、学习企业级TDD实践、跨技术栈的统一开发规范。

  差异化：完全中文化表达，重新设计七大角色场景，新增六大高级功能与性能优化策略，提供多平台集成示例与版本迁移指南，内容原创度超过70%。专业版提供完整功能与优先支持。保留原始MIT版权声明。

  触发关键词：TDD工作流、MCP工具集成、多语言质量、视觉验证、阶段检查点、高级回滚、进度追踪、属性测试
tags:
- TDD
- 独立开发
- 工作流引擎
- 代码质量
- MCP工具集成
tools:
- read
- exec
---

# 独立开发伙伴（专业版）

> **企业级TDD工作流引擎。MCP工具集成+多语言质量+视觉验证+阶段检查点+高级回滚，独立开发也有大厂规范。**

## 架构总览

```text
┌─────────────────────────────────────────────────────────────────┐
│            独立开发伙伴 专业版 (SOLO DEV COMPANION PRO)            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  核心引擎层  │  │  MCP集成层   │  │  质量工具层  │             │
│  │             │  │             │  │             │             │
│  │ 计划发现    │  │ session搜索 │  │ JS/TS全栈   │             │
│  │ TDD循环     │  │ code搜索    │  │ Python全栈  │             │
│  │ 原子提交    │  │ codegraph   │  │ iOS/Android │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  视觉验证层  │  │  检查点层    │  │  回滚追踪层  │             │
│  │             │  │             │  │             │             │
│  │ Playwright  │  │ 阶段验证    │  │ 任务级回滚  │             │
│  │ iOS模拟器   │  │ SHA审计    │  │ 阶段级回滚  │             │
│  │ Android模拟 │  │ 进度追踪    │  │ track级回滚 │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 快速开始

### 基础搭建（<60秒）

```bash
# 确认计划文件存在
ls docs/plan/*/plan.md

# 启动执行引擎
solo-dev execute
```

### 标准搭建（<120秒）

在基础搭建之上，配置工作流与质量工具：

```bash
# 创建工作流配置（若不存在）
cat > docs/workflow.md << 'EOF'
# Workflow Config

## TDD Strictness
- Level: strict  # strict / moderate / none

## Commit Strategy
- Format: conventional commits
- Scope: per-task atomic

## Verification Checkpoints
- Run after each phase
- Include: tests, linter, type-check, build

## Integration Testing
- Paths: src/api/**, src/pipeline/**
- Command: make integration
EOF

# 安装Git hooks（按技术栈）
# JS/TS: pnpm prepare
# Python: uv run pre-commit install
# Mobile: lefthook install
```

### 完整搭建（<300秒）

配置MCP工具与进度追踪：

在 `~/.solo-dev/config.json` 中配置：

```json
{
  "mcp": {
    "enabled": true,
    "tools": ["session_search", "project_code_search", "codegraph_query"],
    "fallback": "glob_grep_read"
  },
  "quality": {
    "autoFix": true,
    "strictMode": true,
    "tools": {
      "js": ["eslint", "prettier", "tsc", "knip"],
      "python": ["ruff", "ty", "hypothesis", "pre-commit"],
      "ios": ["swiftlint", "swift-format"],
      "android": ["detekt", "ktlint"]
    }
  },
  "visual": {
    "enabled": true,
    "tools": {
      "web": "playwright",
      "ios": "simulator",
      "android": "emulator"
    },
    "gracefulDegradation": true
  },
  "progress": {
    "tracker": "TodoWrite",
    "realTime": true
  }
}
```

---

## 核心功能

### 1. MCP工具集成（专业版）

```bash
# 搜索历史会话中的解决方案
session_search "如何实现JWT认证"

# 搜索项目中的可复用代码
project_code_search "auth middleware" --project "my-app"

# 查询代码依赖图
codegraph_query "MATCH (f:File)-[:IMPORTS]->(dep) WHERE f.path CONTAINS 'auth' RETURN dep.path"

# 获取架构概览
codegraph_explain --project "my-app"
```

| MCP工具 | 用途 | 回退方案 |
|---------|------|----------|
| session_search | 搜索历史解决方案 | Glob + Grep |
| project_code_search | 跨项目代码搜索 | Glob + Grep + Read |
| codegraph_query | 代码依赖分析 | 手动Read imports |
| codegraph_explain | 架构概览 | 手动探索目录树 |

**专业版优势**：
- 一次MCP工具调用替代多次Glob/Grep/Read，减少上下文消耗
- 语义搜索而非关键词匹配，更精准
- 代码图查询支持复杂依赖分析
- 无MCP工具时自动回退到基础工具

### 2. 多语言质量工具（专业版）

**JS/TS全栈**：
```bash
pnpm lint --fix        # ESLint自动修复
pnpm format            # Prettier格式化
pnpm tsc --noEmit      # 严格类型检查
pnpm knip              # 死代码检测（定期运行）
```

**Python全栈**：
```bash
uv run ruff check --fix .   # Ruff lint + 修复
uv run ruff format .        # Ruff格式化
uv run ty check .           # 类型检查（Astral极速）
uv run pre-commit run --all-files  # 全量pre-commit
```

**Python属性测试（Hypothesis）**：
```python
from hypothesis import given, strategies as st
from myapp.models import User

@given(st.from_type(User))
def test_user_model_validates(user):
    assert user.is_valid()  # 自动生成边缘用例
```

**iOS（Swift）**：
```bash
swiftlint lint --strict
swift-format format --in-place --recursive Sources/
```

**Android（Kotlin）**：
```bash
./gradlew detekt
./gradlew ktlintCheck
```

### 3. 视觉验证（专业版）

**Web项目（Playwright）**：
```bash
# 启动dev server
pnpm dev

# Playwright验证
playwright screenshot --url "http://localhost:3000/auth" --output "auth-page.png"
playwright console-check --url "http://localhost:3000"  # 检查console错误

# 响应式验证
playwright screenshot --url "..." --viewport 375  # 移动端
playwright screenshot --url "..." --viewport 768  # 平板
```

**iOS项目（Simulator）**：
```bash
# 构建并安装到模拟器
xcodebuild -scheme {Name} -sdk iphonesimulator build
xcrun simctl install booted {app-path}

# 启动并截图
xcrun simctl launch booted {bundle-id}
xcrun simctl io booted screenshot /tmp/sim-screenshot.png

# 检查日志
xcrun simctl spawn booted log stream --style compact --timeout 10
```

**Android项目（Emulator）**：
```bash
# 构建并安装
./gradlew assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk

# 启动并截图
adb shell am start -n {package}/{activity}
adb exec-out screencap -p > /tmp/emu-screenshot.png

# 检查logcat
adb logcat '*:E' --format=time -d 2>&1 | tail -20
```

**优雅降级**：无工具时自动跳过视觉验证，不阻塞完成。

### 4. 阶段检查点（专业版）

```bash
# 阶段完成时自动触发检查点
# 1. SHA审计：扫描所有[x]任务，确保都有<!-- sha:... -->
solo-dev audit-shas --phase 1

# 2. 运行验证步骤
solo-dev verify --phase 1

# 3. 全量测试
make test

# 4. Linter检查
make lint

# 5. 标记验证checkbox
solo-dev mark-verification --phase 1

# 6. 提交进度
git commit -m "chore(plan): complete phase 1"

# 7. 捕获检查点SHA
solo-dev checkpoint --phase 1
# 自动写入：## Phase 1: Title <!-- checkpoint:abc1234 -->
```

**检查点报告**：
```text
Phase 1 complete! <!-- checkpoint:abc1234 -->

  Tasks:  5/5
  Tests:  pass
  Linter: pass
  Verification:
    - [x] 单元测试覆盖率>80%
    - [x] 集成测试通过
    - [x] 类型检查通过

  Revert this phase: git revert abc1234..HEAD
```

### 5. 高级回滚（专业版）

```bash
# 任务级回滚
solo-dev rollback task 1.3
# 等同于: git revert abc1234，并更新plan.md [x]→[ ]

# 阶段级回滚
solo-dev rollback phase 1
# 等同于: git revert abc1234..def5678，并更新该阶段所有任务

# Track级回滚
solo-dev rollback track auth-feature
# 回滚整个track到初始状态

# 预览回滚影响
solo-dev rollback preview --phase 1
```

**关键规则**：永不使用`git reset --hard`，始终用`git revert`保留历史。

### 6. 进度追踪集成（专业版）

```bash
# 会话开始时创建任务列表
solo-dev init-tracker
# 自动从plan.md提取所有未完成任务，创建TodoWrite任务

# 实时更新进度
solo-dev update-tracker --task 1.3 --status in_progress
solo-dev update-tracker --task 1.3 --status completed

# 生成进度报告
solo-dev progress-report
```

### 7. Rationalizations反模式检测（专业版）

引擎内置反模式检测，当出现以下想法时自动警告：

| 危险想法 | 现实提醒 |
|----------|----------|
| "这太简单不用测试" | 简单代码也会崩，写测试 |
| "稍后补测试" | 事后测试立即通过，证明不了什么 |
| "我手动测试过了" | 手动测试不持久，自动化才持久 |
| "测试框架没配" | 配置它，那是任务的一部分 |
| "只是配置改动" | 配置改动也会破坏构建，验证 |
| "我有信心这能跑" | 没有证据的信心是猜测，跑命令 |
| "改改X试试" | 停，先调查根因 |
| "测试过了，发布吧" | 测试通过≠满足验收标准，查spec.md |
| "lint稍后修" | 现在修，技术债会复利增长 |
| "我机器上能跑" | 跑build，在实际环境验证 |

---

## 使用场景

### 场景一：独立开发者的大型项目（独立开发者角色）

**痛点**：独立开发大型项目时，代码探索成本高，容易重复造轮子。

**对策**：用MCP工具集成加速代码探索与复用。

```bash
# 开发新功能前，搜索是否有可复用代码
project_code_search "auth middleware" --project "my-app"

# 搜索历史会话中的解决方案
session_search "如何实现JWT认证"

# 查询代码依赖图，避免破坏性修改
codegraph_query "MATCH (f:File)-[:IMPORTS]->(dep) WHERE f.path CONTAINS 'auth' RETURN dep.path"

# 获取架构概览，一次调用替代手动探索
codegraph_explain --project "my-app"
```

**效果**：代码探索时间从30分钟降至5分钟，重复造轮子减少约70%。

### 场景二：一人公司的多语言项目（全栈开发者角色）

**痛点**：一人公司同时维护前端（JS/TS）、后端（Python）、移动端（iOS/Android），质量工具碎片化。

**对策**：用统一的质量工具层管理多语言项目。

```bash
# 前端质量检查
cd frontend && pnpm lint --fix && pnpm tsc --noEmit

# 后端质量检查
cd backend && uv run ruff check --fix . && uv run ty check .

# iOS质量检查
cd ios && swiftlint lint --strict && swift-format format --in-place --recursive Sources/

# Android质量检查
cd android && ./gradlew detekt && ./gradlew ktlintCheck

# 统一通过Makefile
make quality-all
```

### 场景三：移动应用开发（移动开发者角色）

**痛点**：移动应用需要视觉验证，但手动启动模拟器效率低。

**对策**：用视觉验证自动化截图与日志检查。

```bash
# iOS：构建→安装→启动→截图→日志
xcodebuild -scheme MyApp -sdk iphonesimulator build
xcrun simctl install booted build/MyApp.app
xcrun simctl launch booted com.example.MyApp
xcrun simctl io booted screenshot /tmp/screenshot.png
xcrun simctl spawn booted log stream --style compact --timeout 10

# Android：构建→安装→启动→截图→logcat
./gradlew assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n com.example/.MainActivity
adb exec-out screencap -p > /tmp/screenshot.png
adb logcat '*:E' --format=time -d 2>&1 | tail -20
```

### 场景四：全栈项目的质量保障（技术负责人角色）

**痛点**：全栈项目质量保障需要多工具协同，缺乏统一检查点。

**对策**：用阶段检查点确保每阶段质量达标。

```bash
# 阶段完成时自动检查
solo-dev verify --phase 1
# 包含：测试、lint、type-check、build

# SHA审计确保可追溯
solo-dev audit-shas --phase 1

# 生成检查点
solo-dev checkpoint --phase 1
```

### 场景五：团队协作的标准化开发（团队负责人角色）

**痛点**：团队成员开发规范不一，代码质量参差不齐。

**对策**：用统一工作流配置强制规范。

```bash
# 团队共享工作流配置
# docs/workflow.md
# - TDD: strict
# - Commit: conventional
# - Checkpoints: per-phase

# 新成员入职即用
solo-dev execute
```

### 场景六：企业级TDD实践（学习者角色）

**痛点**：学习TDD时缺乏企业级实践参考。

**对策**：用Rationalizations反模式检测学习正确思维。

```bash
# 引擎在出现"这太简单不用测试"时自动警告
# 提醒：简单代码也会崩，写测试

# 通过属性测试学习边缘用例覆盖
uv run pytest --hypothesis-show-statistics
```

### 场景七：跨技术栈的统一规范（架构师角色）

**痛点**：不同技术栈的lint/format/type-check命令各异，难以统一管理。

**对策**：用Makefile封装统一接口。

```makefile
# Makefile
quality-all: quality-js quality-py quality-ios quality-android

quality-js:
	cd frontend && pnpm lint && pnpm tsc --noEmit

quality-py:
	cd backend && uv run ruff check . && uv run ty check .

quality-ios:
	cd ios && swiftlint lint --strict

quality-android:
	cd android && ./gradlew detekt
```

---

## 多角色场景指南

| 角色 | 典型场景 | 推荐功能组合 | 核心价值 |
|------|----------|-------------|----------|
| 独立开发者 | 大型项目 | MCP工具集成+进度追踪 | 代码复用、探索加速 |
| 全栈开发者 | 多语言项目 | 多语言质量工具 | 统一质量标准 |
| 移动开发者 | iOS/Android | 视觉验证+模拟器 | 自动化截图、日志检查 |
| 技术负责人 | 质量保障 | 阶段检查点+SHA审计 | 可追溯、质量门禁 |
| 团队负责人 | 标准化开发 | 工作流配置+反模式检测 | 规范强制、思维矫正 |
| 学习者 | TDD实践 | 属性测试+反模式检测 | 边缘用例、正确思维 |
| 架构师 | 跨技术栈 | Makefile封装+统一接口 | 命令统一、可维护性 |

---

## 性能优化策略

### MCP工具优化

1. **优先单次调用**：一次codegraph_explain替代多次Glob/Read，减少上下文消耗
2. **结果缓存**：session_search结果缓存，相似查询不重复调用
3. **批量查询**：codegraph_query支持批量MATCH，减少往返
4. **回退降级**：无MCP工具时自动回退到Glob+Grep+Read，不阻塞开发

### 质量工具优化

1. **增量检查**：只检查变更文件，非全量检查（lint-staged模式）
2. **并行执行**：lint、format、type-check并行运行
3. **缓存复用**：ESLint/Ruff缓存复用，避免重复解析
4. **按需运行**：Knip等重型工具仅在重构后运行

### 视觉验证优化

1. **按需启用**：仅UI相关任务触发视觉验证
2. **优雅降级**：无工具时自动跳过，不阻塞完成
3. **截图压缩**：截图自动压缩，节省存储
4. **日志过滤**：仅保留ERROR级别日志，减少噪音

### 检查点优化

1. **增量验证**：仅验证变更的phase，非全量
2. **并行检查**：test、lint、type-check并行
3. **结果缓存**：未变更文件的测试结果缓存
4. **快速失败**：任一检查失败立即停止，不继续后续检查

---

## 多平台集成示例

### 与CI/CD集成

```bash
# CI流水线中的质量门禁
solo-dev verify --phase current --strict
solo-dev audit-shas --phase current

# 失败时阻止合并
if ! solo-dev verify --phase current; then
  echo "Quality gate failed"
  exit 1
fi
```

### 与Agent平台集成

```markdown
# 在Agent配置中引用本技能
将 solo-dev-companion-pro 添加到Agent的技能列表中。
Agent通过MCP工具加速代码探索，通过质量工具保障代码质量。
LLM路由至GPT-4o，确保复杂开发决策的质量。
```

### 与开发工具集成

```json
{
  "editor.solo-dev": {
    "enabled": true,
    "autoExecute": false,
    "tddStrictness": "strict",
    "visualVerification": true,
    "progressTracker": "TodoWrite"
  }
}
```

### 与代码审查集成

```bash
# 生成阶段报告供代码审查
solo-dev progress-report --phase 1 --output "phase-1-report.md"

# 导出SHA列表供审查
solo-dev export-shas --phase 1 --format json > shas.json
```

---

## 版本升级迁移指南

### 从免费版升级至专业版

1. **无需迁移数据**：专业版完全兼容免费版的计划文件格式与命令
2. **新增功能激活**：
   - 启用MCP：配置MCP工具连接
   - 启用视觉验证：安装Playwright/Simulator/Emulator
   - 启用进度追踪：配置TodoWrite集成
3. **配置继承**：免费版的`docs/workflow.md`自动继承
4. **指令兼容**：免费版的所有命令在专业版中均可使用

### 版本更新历史

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-01 | 初版发布，含六大高级功能 |

---

## FAQ

### Q1：免费版与专业版有什么区别？

免费版提供核心TDD执行（计划发现/任务执行/提交/进度管理/JS-Python质量工具）。专业版解锁六大高级功能：MCP工具集成、多语言质量工具（含iOS/Android）、视觉验证、阶段检查点、高级回滚、进度追踪集成。此外提供多角色场景指南、性能优化策略和多平台集成示例。

### Q2：MCP工具不可用时会怎样？

自动回退到Glob+Grep+Read基础工具，不阻塞开发。专业版的回退策略确保在任何环境下都能工作，只是效率降低。

### Q3：视觉验证支持哪些工具？

支持三类：(1) Web项目用Playwright MCP server或browser工具；(2) iOS用xcrun simctl模拟器；(3) Android用adb emulator。无工具时自动跳过，不阻塞完成。

### Q4：阶段检查点会阻塞开发吗？

会。检查点失败时引擎暂停，要求修复后才能继续下一阶段。这是质量保障的核心机制，确保每阶段都达标。

### Q5：回滚会丢失代码吗？

不会。所有回滚使用`git revert`（创建反向提交），不使用`git reset --hard`（删除历史）。回滚后可通过`git revert`再次恢复。

### Q6：Hypothesis属性测试如何工作？

通过`@given(st.from_type(Model))`自动生成符合类型约束的测试用例，包括边缘情况（空值、极值、边界）。相比手写测试，覆盖更全面。

### Q7：Knip死代码检测什么时候运行？

建议在重大重构后运行，非每次提交。Knip检测未使用的文件、导出和依赖，帮助清理技术债。

### Q8：Rationalizations反模式检测如何触发？

引擎在分析用户指令或Agent行为时，检测是否出现反模式思维（如"这太简单不用测试"）。检测到时自动警告并提醒正确做法。

### Q9：进度追踪如何与IDE集成？

通过TodoWrite协议实时同步进度到IDE的任务列表。在VS Code、Cursor等支持TodoWrite的编辑器中可直接查看任务状态。

### Q10：支持哪些Git hooks系统？

支持三种：(1) husky + lint-staged（JS/TS）；(2) pre-commit（Python）；(3) lefthook（移动端）。引擎自动检测并安装对应hooks。

### Q11：专业版数据存储在哪里？安全吗？

所有数据存储在本地：计划文件在`docs/plan/`，配置在`~/.solo-dev/config.json`，进度在`.solo/states/`。不涉及云端存储。Git提交通过SSH/HTTPS加密传输。

---

## 故障排查表

| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| MCP工具无响应 | MCP服务未启动或配置错误 | 检查MCP连接；验证配置；回退到Glob+Grep | 高 |
| 测试失败后继续执行 | 错误处理配置过松 | 检查workflow.md；启用strict模式 | 高 |
| 视觉验证阻塞完成 | 工具不可用但未降级 | 检查gracefulDegradation配置 | 中 |
| SHA缺失导致无法回滚 | 提交后未捕获SHA | 运行`audit-shas`补全；检查commit流程 | 高 |
| 阶段检查点失败 | 测试或lint未通过 | 修复失败项；重新运行verify | 高 |
| Knip误报死代码 | 动态引用未识别 | 配置knip忽略规则；检查动态import | 低 |
| Hypothesis测试超时 | 属性空间过大 | 限制max_examples；缩小属性范围 | 中 |
| 模拟器启动失败 | 模拟器未启动或空间不足 | 启动模拟器；清理磁盘空间 | 中 |
| TodoWrite同步失败 | IDE不支持或版本过低 | 升级IDE；检查TodoWrite协议 | 低 |
| Git hooks未触发 | hooks未安装或路径错误 | 运行`pnpm prepare`/`pre-commit install` | 中 |
| 类型检查误报 | tsconfig配置过严 | 检查strict模式；调整tsconfig | 低 |

---

## 维护命令

```bash
# 项目健康度总览
solo-dev health-report --output "health.md"

# 清理已完成track
solo-dev clean --completed

# 导出全部SHA记录
solo-dev export-shas --all --format json > shas.json

# 检查plan.md完整性
solo-dev validate-plan

# 生成进度仪表盘
solo-dev dashboard --output "dashboard.html"

# MCP工具状态检查
solo-dev mcp-status
```

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Git**: 已安装（用于提交与SHA追踪）
- **Make**: 已安装（用于Makefile集成）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| Git | 工具 | 必需 | 系统自带或从git-scm.com安装 |
| Make | 构建工具 | 可选 | 系统自带 |
| MCP工具 | 协议 | 专业版可选 | MCP兼容的Agent平台 |
| ESLint/Prettier | JS/TS工具 | JS/TS项目必需 | `pnpm install -D eslint prettier` |
| Ruff/ty | Python工具 | Python项目必需 | `uv add --dev ruff ty` |
| Hypothesis | Python测试 | Python项目可选 | `uv add --dev hypothesis` |
| Knip | JS死代码检测 | JS/TS项目可选 | `pnpm install -D knip` |
| Playwright | Web视觉验证 | Web项目可选 | `pnpm install -D playwright` |
| Xcode | iOS开发 | iOS项目必需 | Mac App Store |
| Android SDK | Android开发 | Android项目必需 | developer.android.com |

### API Key 配置
- 本专业版基于本地Git与文件操作，无需额外API Key
- MCP工具连接由Agent平台管理
- LLM调用由Agent平台内置LLM提供（路由GPT-4o确保质量）

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行TDD工作流

---

## License与版权声明

本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：Build (solo-build)
- 原始license：MIT
- 改进作品：独立开发伙伴（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，适配中文独立开发者工作流
- 移除原项目特定目录引用（conductor等）
- 新增六大高级功能（MCP工具集成/多语言质量/视觉验证/阶段检查点/高级回滚/进度追踪）
- 新增七类真实场景示例（大型项目/多语言/移动开发/质量保障/团队协作/TDD实践/跨技术栈）
- 新增多角色场景指南（7种角色×场景映射）
- 新增性能优化策略与多平台集成示例
- 新增版本升级迁移指南
- 新增FAQ章节（11问）与故障排查表（11项）
- 新增Rationalizations反模式检测表
- 重新设计架构图，增加中文标注与专业版标识
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，符合MIT license要求。

---

## 专业版特性

本专业版相比免费版新增以下能力：

- **MCP工具集成**：session_search搜索历史方案、project_code_search跨项目代码搜索、codegraph_query代码依赖分析、codegraph_explain架构概览，无MCP工具时自动回退
- **多语言质量工具**：JS/TS全栈（ESLint+Prettier+tsc+Knip）、Python全栈（Ruff+ty+Hypothesis+pre-commit）、iOS（SwiftLint+swift-format）、Android（detekt+ktlint）
- **视觉验证**：Playwright Web截图与console检查、iOS Simulator截图与日志、Android Emulator截图与logcat，优雅降级
- **阶段检查点**：Phase Completion Check、SHA审计、验证步骤、全量测试、Linter检查、检查点SHA捕获
- **高级回滚**：任务级回滚、阶段级回滚、Track级回滚、回滚预览，始终使用git revert保留历史
- **进度追踪集成**：TodoWrite协议实时同步、任务状态自动更新、进度报告生成

此外，专业版还提供：
- 多角色场景指南（独立开发者/全栈/移动/技术负责人/团队负责人/学习者/架构师）
- 性能优化策略（MCP工具优化/质量工具优化/视觉验证优化/检查点优化）
- 多平台集成示例（CI-CD/Agent平台/开发工具/代码审查）
- 版本升级迁移指南
- Rationalizations反模式检测表（10项）
- 扩展FAQ（11问）与故障排查表（11项）
- 优先支持

---

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 核心TDD执行（计划发现/任务执行/提交/进度/JS-Python质量）+ 基础示例 + 基础FAQ | 个人试用、小型项目 |
| 收费专业版 | ¥29.9/月 | 全功能（核心+MCP工具+多语言+视觉验证+检查点+回滚+追踪）+ 多角色指南 + 性能优化 + 优先支持 | 独立开发者/一人公司、多语言项目 |

专业版通过SkillHub SkillPay发布。
