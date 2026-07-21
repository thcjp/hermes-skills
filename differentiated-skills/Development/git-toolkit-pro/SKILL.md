---
slug: git-toolkit-pro
name: git-toolkit-pro
version: "1.0.0"
displayName: Git工具包专业版
summary: 企业级Git管理,支持批量分支操作、自动化审查、Git Hook管理与CI/CD流水线集成。
license: Proprietary
edition: pro
description: |-
  面向企业研发团队的高级Git管理工具,提供批量分支操作、自动化代码审查、Git Hook管理、历史分析与CI/CD流水线集成。核心能力:
  - 批量分支管理与清理
  - 自动化代码审查与PR检查
  - Git Hook统一管理
  - 提交规范强制执行
  - 仓库历史深度分析
  - CI/CD流水线集成

  适用场景:
  - 企业级团队协作开发
  - 大型仓库分支管理
  - 自动化代码审查流程
  - DevOps流水线集成

  差异化:
  - 专业版完全兼容免费版命令,支持平滑升级
  - 提供批量操作和自动化能力
  - ...
tags:
- 开发工具
- Git
- 版本控制
- 企业级
- DevOps
tools:
  - - read
- exec
# Git工具包 - 专业版
## 概述
---
Git工具包专业版为企业研发团队提供高级Git管理能力。在免费版基础Git操作之上,专业版新增批量分支管理、自动化代码审查、Git Hook统一管理、提交规范强制执行和仓库历史深度分析,满足企业级团队协作需求。

专业版完全兼容免费版的所有Git命令和配置,研发团队可从免费版无缝升级,已有Git配置和别名无需修改。

## 核心能力
### 1. 批量分支管理
支持批量创建、清理和管理分支。

> 详细代码示例已移至 `references/detail.md`

### 2. 自动化代码审查
自动检查提交规范和代码质量。

> 详细代码示例已移至 `references/detail.md`

### 3. Git Hook 统一管理

> 详细代码示例已移至 `references/detail.md`

### 4. 仓库历史分析

> 详细代码示例已移至 `references/detail.md`

## 使用场景
### 场景一:团队工作流自动化
配置团队标准Git工作流。

```bash
#!/bin/bash
echo "=== 团队Git工作流配置 ==="

bash git-hooks.sh install

git config alias.feature 'checkout -b feature'
git config alias.hotfix 'checkout -b hotfix'
git config alias.release 'checkout -b release'
git config alias.cleanup '!git branch --merged main | grep -v "main" | xargs git branch -d'
git config alias.sync '!git fetch --all --prune && git pull --rebase'

cat > .gitmessage << 'EOF
EOF
git config commit.template .gitmessage

echo "团队工作流配置完成"
```

### 场景二:批量分支清理
定期清理过期分支。

```bash
#!/bin/bash
echo "=== 分支清理 ==="

git fetch --all --prune

echo "清理已合并分支..."
git branch --merged main | grep -v "main\|master\|develop" | \
    xargs -r git branch -d

echo -e "\n查找过期分支..."
THRESHOLD=$(date -d "30 days ago" +%Y-%m-%d 2>/dev/null || date -v-30d +%Y-%m-%d)

for branch in $(git branch --format "%(refname:short)"); do
    LAST_COMMIT=$(git log -1 --format=%ai "$branch" 2>/dev/null)
    if [ -n "$LAST_COMMIT" ]; then
        COMMIT_DATE=$(echo "$LAST_COMMIT" | cut -d' ' -f1)
        if [[ "$COMMIT_DATE" < "$THRESHOLD" ]]; then
            echo "  [过期] $branch (最后提交: $COMMIT_DATE)"
        fi
    fi
done

python3 -c "
from repository_analyzer import RepositoryAnalyzer
import json
report = RepositoryAnalyzer.branch_analysis()
print(json.dumps(report, indent=2, ensure_ascii=False))
"
```

### 场景三:CI/CD流水线集成
将Git检查集成到CI/CD流水线。

```yaml
git_quality_check:
  stage: check
  script:
    - |
      echo "检查提交规范..."
      MSG=$(git log -1 --format=%s)
      PATTERN='^(feat|fix|docs|style|refactor|test|chore|perf|ci|build)(\(\w+\))?:\s+.+'
      if ! echo "$MSG" | grep -qE "$PATTERN"; then
        echo "提交信息不符合规范: $MSG"
        exit 1
      fi

    - |
      echo "自动化代码审查..."
      python3 code_review.py --diff "$(git diff origin/main...HEAD)" \
        --format json --output review-report.json

    - |
      BRANCH=$(git branch --show-current)
      echo "当前分支: $BRANCH"
      if echo "$BRANCH" | grep -qE "^(feature|hotfix|release)/"; then
        echo "[OK] 分支命名规范"
      else
        echo "[!] 分支命名不规范,应为 feature/*, hotfix/*, release/*"
        exit 1
      fi

    - python3 repository_analyzer.py --output repo-report.json
  artifacts:
    paths:
      - review-report.json
      - repo-report.json
    expire_in: 30 days
```

## 不适用场景

以下场景Git工具包专业版不适合处理：

- 需要人工创意判断的任务
- 非结构化头脑风暴
- 人际沟通协调


## 触发条件

需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于非本工具能力范围的需求。


## 快速开始
### 步骤一:配置团队环境
```yaml
version: "2.0"
edition: pro

team:
  default_branch: main
  branch_prefix:
    feature: "feature/"
    hotfix: "hotfix/"
    release: "release/"

commit:
  conventional: true
  max_subject_length: 72
  require_scope: false

hooks:
  pre_commit:
    check_debug: true
    check_secrets: true
    check_large_files: true
    max_file_size: 1MB
  commit_msg:
    check_format: true
  pre_push:
    block_direct_push_main: true

branch:
  auto_cleanup: true
  stale_threshold_days: 30
  protect_branches: [main, master, develop]
```

### 步骤二:安装团队Hook
```
请安装团队Git Hook并配置标准工作流。
```

## 配置示例
### 企业级完整配置
```yaml
version: "2.0"
edition: pro

team:
  name: "研发团队"
  default_branch: main
  protected_branches: [main, develop, release/*]

branching:
  strategy: gitflow
  prefixes:
    feature: "feature/"
    hotfix: "hotfix/"
    release: "release/"
    bugfix: "bugfix/"
  auto_cleanup: true
  stale_days: 30

commit:
  conventional: true
  types: [feat, fix, docs, style, refactor, test, chore, perf, ci, build]
  max_subject: 72
  require_scope: false
  template: .gitmessage

hooks:
  enabled: true
  shared_dir: .githooks
  pre_commit:
    check_debug_code: true
    check_secrets: true
    check_large_files: true
    max_file_size: 1048576
    run_linter: true
  commit_msg:
    check_format: true
    check_length: true
  pre_push:
    block_direct_push_main: true
    require_tests: true

review:
  auto_review: true
  check_patterns:
    debug_code: true
    secrets: true
    todo_fixme: true
  block_on_error: true

analysis:
  contributor_stats: true
  commit_frequency: true
  branch_analysis: true
  file_change_stats: true
  report_schedule: weekly

ci_cd:
  commit_check: true
  branch_check: true
  auto_review: true
  report_artifacts: true
```

## 最佳实践
1. **统一Hook**:团队共享Git Hook,确保规范一致

```bash
git add .githooks/
git commit -m "chore: 添加团队Git Hook"
```

2. **定期清理**:设置定期分支清理任务

```bash
0 2 * * 0 cd /project && git fetch --prune && git branch --merged main | xargs git branch -d
```

3. **提交模板**:使用提交模板引导规范提交

4. **分支保护**:在Git平台上保护关键分支

5. **自动化审查**:将代码审查集成到提交流程

## 常见问题
### Q1:专业版如何兼容免费版?
专业版完全兼容免费版的所有Git命令和配置。免费版的别名和配置可直接使用,专业版会自动启用Hook管理和批量操作功能。

### Q2:Hook如何团队共享?
```bash
mkdir -p .githooks
cp hooks/* .githooks/

git config core.hooksPath .githooks

git add .githooks
git commit -m "chore: 共享Git Hook"

git config core.hooksPath .githooks
```

### Q3:如何绕过Hook(紧急情况)?
```bash
git commit --no-verify -m "hotfix: 紧急修复"

```

### Q4:仓库分析支持哪些指标?
| 指标 | 说明 |
|:-----|:-----|
| 贡献者统计 | 按提交数排名 |
| 提交频率 | 每日提交趋势 |
| 文件热度 | 最常修改的文件 |
| 分支分析 | 活跃/过期分支 |
| 代码行数 | 历史代码量变化 |

## 依赖说明
### 运行环境
- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Git 2.20+ / Python 3.8+ / Bash

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Git 2.20+ | 运行时 | 必需 | git-scm.com 下载 |
| Python 3.8+ | 运行时 | 推荐 | python.org 下载 |
| Bash | 运行时 | 推荐 | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 远程仓库认证配置:

```bash
git config --global credential.helper store

git remote set-url origin https://<token>@git.example.com/repo.git
```

### 可用性分类
- **分类**:MD+EXEC+PRO(专业版支持批量操作、Hook管理和仓库分析)
- **说明**:企业级Git管理工具,支持团队协作和自动化审查
- **适用规模**:中小型到大型团队项目
- **兼容性**:完全兼容免费版命令和配置,支持平滑升级

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
