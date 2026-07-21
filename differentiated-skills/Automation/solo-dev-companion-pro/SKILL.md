---
slug: solo-dev-companion-pro
name: solo-dev-companion-pro
version: "1.0.0"
displayName: 独立开发伙伴(专业版)
summary: 全功能TDD工作流引擎，含MCP工具集成、多语言质量工具、视觉验证、阶段检查点与高级回滚。
license: Proprietary
edition: pro
description: |-
  独立开发伙伴专业版是在免费版基础上的全功能升级，为独立开发者与一人公司提供企业级TDD工作流引擎。除核心TDD执行外，解锁MCP工具集成、多语言质量工具、视觉验证、阶段检查点、高级回滚、进度追踪集成六大高级功能。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- TDD
- 独立开发
- 工作流引擎
- 代码质量
- MCP工具集成
tools:
  - - read
- exec
# 独立开发伙伴（专业版）
---
> **企业级TDD工作流引擎。MCP工具集成+多语言质量+视觉验证+阶段检查点+高级回滚，独立开发也有大厂规范。**

## 快速开始
### 基础搭建（<60秒）
```bash
ls docs/plan/*/plan.md

solo-dev execute
```

### 标准搭建（<120秒）
在基础搭建之上，配置工作流与质量工具：

```bash
cat > docs/workflow.md << 'EOF'
- Level: strict  # strict / moderate / none
- Format: conventional commits
- Scope: per-task atomic

- Run after each phase
- Include: tests, linter, type-check, build

- Paths: src/api/**, src/pipeline/**
- Command: make integration
EOF

```

## 核心功能

### 1. MCP工具集成（专业版）
> 详细内容已移至 `references/detail.md`

### 2. 多语言质量工具（专业版）
> 详细内容已移至 `references/detail.md`

### 3. 视觉验证（专业版）
> 详细内容已移至 `references/detail.md`

### 4. 阶段检查点（专业版）
> 详细内容已移至 `references/detail.md`

### 6. 进度追踪集成（专业版）
```bash
solo-dev init-tracker
solo-dev update-tracker --task 1.3 --status in_progress
solo-dev update-tracker --task 1.3 --status completed

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

## 使用场景
### 场景一：独立开发者的大型项目（独立开发者角色）
**痛点**：独立开发大型项目时，代码探索成本高，容易重复造轮子。

**对策**：用MCP工具集成加速代码探索与复用。

```bash
project_code_search "auth middleware" --project "my-app"

session_search "如何实现JWT认证"

codegraph_query "MATCH (f:File)-[:IMPORTS]->(dep) WHERE f.path CONTAINS 'auth' RETURN dep.path"

codegraph_explain --project "my-app"
```

**效果**：代码探索时间从30分钟降至5分钟，重复造轮子减少约70%。

### 场景二：一人公司的多语言项目（全栈开发者角色）
**痛点**：一人公司同时维护前端（JS/TS）、后端（Python）、移动端（iOS/Android），质量工具碎片化。

**对策**：用统一的质量工具层管理多语言项目。

```bash
cd frontend && pnpm lint --fix && pnpm tsc --noEmit

cd backend && uv run ruff check --fix . && uv run ty check .

cd ios && swiftlint lint --strict && swift-format format --in-place --recursive Sources/

cd android && ./gradlew detekt && ./gradlew ktlintCheck

make quality-all
```

### 场景三：移动应用开发（移动开发者角色）
**痛点**：移动应用需要视觉验证，但手动启动模拟器效率低。

**对策**：用视觉验证自动化截图与日志检查。

```bash
xcodebuild -scheme MyApp -sdk iphonesimulator build
xcrun simctl install booted build/MyApp.app
xcrun simctl launch booted com.example.MyApp
xcrun simctl io booted screenshot /tmp/screenshot.png
xcrun simctl spawn booted log stream --style compact --timeout 10

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
solo-dev verify --phase 1
solo-dev audit-shas --phase 1

solo-dev checkpoint --phase 1
```

### 场景五：团队协作的标准化开发（团队负责人角色）
**痛点**：团队成员开发规范不一，代码质量参差不齐。

**对策**：用统一工作流配置强制规范。

```bash
solo-dev execute
```

### 场景六：企业级TDD实践（学习者角色）
**痛点**：学习TDD时缺乏企业级实践参考。

**对策**：用Rationalizations反模式检测学习正确思维。

```bash
uv run pytest --hypothesis-show-statistics
```

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

## 示例
### 与CI/CD集成
```bash
solo-dev verify --phase current --strict
solo-dev audit-shas --phase current

if ! solo-dev verify --phase current; then
  echo "Quality gate failed"
  exit 1
fi
```

### 与Agent平台集成
```markdown
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
solo-dev progress-report --phase 1 --output "phase-1-report.md"

solo-dev export-shas --phase 1 --format json > shas.json
```

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

## 错误处理
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

## 维护命令
```bash
solo-dev health-report --output "health.md"

solo-dev clean --completed

solo-dev export-shas --all --format json > shas.json

solo-dev validate-plan

solo-dev dashboard --output "dashboard.html"

solo-dev mcp-status
```

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

## License与版权声明
> 详细内容已移至 `references/detail.md`

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

## 定价
| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 核心TDD执行（计划发现/任务执行/提交/进度/JS-Python质量）+ 基础示例 + 基础FAQ | 个人试用、小型项目 |
| 收费专业版 | ¥29.9/月 | 全功能（核心+MCP工具+多语言+视觉验证+检查点+回滚+追踪）+ 多角色指南 + 性能优化 + 优先支持 | 独立开发者/一人公司、多语言项目 |

专业版通过SkillHub SkillPay发布。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
