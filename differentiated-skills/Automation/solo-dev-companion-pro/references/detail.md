# 详细参考 - solo-dev-companion-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (json)

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

## 代码示例 (text)

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



### 场景七：跨技术栈的统一规范（架构师角色）
**痛点**：不同技术栈的lint/format/type-check命令各异，难以统一管理。

**对策**：用Makefile封装统一接口。

```makefile
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



### 5. 高级回滚（专业版）
```bash
solo-dev rollback task 1.3
solo-dev rollback phase 1
solo-dev rollback track auth-feature
solo-dev rollback preview --phase 1
```

**关键规则**：永不使用`git reset --hard`，始终用`git revert`保留历史。



### Q6：Hypothesis属性测试如何工作？
通过`@given(st.from_type(Model))`自动生成符合类型约束的测试用例，包括边缘情况（空值、极值、边界）。相比手写测试，覆盖更全面。



## 性能优化策略


## 版本升级迁移指南



### 1. MCP工具集成（专业版）
```bash
session_search "如何实现JWT认证"

project_code_search "auth middleware" --project "my-app"

codegraph_query "MATCH (f:File)-[:IMPORTS]->(dep) WHERE f.path CONTAINS 'auth' RETURN dep.path"

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



---

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



---

### 3. 视觉验证（专业版）
**Web项目（Playwright）**：
```bash
pnpm dev

playwright screenshot --url "http://localhost:3000/auth" --output "auth-page.png"
playwright console-check --url "http://localhost:3000"  # 检查console错误
playwright screenshot --url "..." --viewport 375  # 移动端
playwright screenshot --url "..." --viewport 768  # 平板
```

**iOS项目（Simulator）**：
```bash
xcodebuild -scheme {Name} -sdk iphonesimulator build
xcrun simctl install booted {app-path}

xcrun simctl launch booted {bundle-id}
xcrun simctl io booted screenshot /tmp/sim-screenshot.png

xcrun simctl spawn booted log stream --style compact --timeout 10
```

**Android项目（Emulator）**：
```bash
./gradlew assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk

adb shell am start -n {package}/{activity}
adb exec-out screencap -p > /tmp/emu-screenshot.png

adb logcat '*:E' --format=time -d 2>&1 | tail -20
```

**优雅降级**：无工具时自动跳过视觉验证，不阻塞完成。



---

### 4. 阶段检查点（专业版）
```bash
solo-dev audit-shas --phase 1

solo-dev verify --phase 1

make test

make lint

solo-dev mark-verification --phase 1

git commit -m "chore(plan): complete phase 1"

solo-dev checkpoint --phase 1
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
