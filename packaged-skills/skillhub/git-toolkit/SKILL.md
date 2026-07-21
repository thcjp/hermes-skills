---
slug: git-toolkit
name: git-toolkit
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
# Git工具包专业版

## 核心能力

### 1. 批量分支管理
支持批量创建、清理和管理分支。

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供批量分支管理所需的指令和必要参数。
**处理**: 按照skill规范执行批量分支管理操作,遵循单一意图原则。

### 2. 自动化代码审查
自动检查提交规范和代码质量。

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供自动化代码审查所需的指令和必要参数。
**输出**: 返回自动化代码审查的执行结果,包含操作状态和输出数据。

### 3. Git Hook 统一管理
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供Git Hook 统一管理所需的指令和必要参数。
**处理**: 按照skill规范执行Git Hook 统一管理操作,遵循单一意图原则。
**输出**: 返回Git Hook 统一管理的执行结果,包含操作状态和输出数据。

### 4. 仓库历史分析
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供仓库历史分析所需的指令和必要参数。
**处理**: 按照skill规范执行仓库历史分析操作,遵循单一意图原则。
**输出**: 返回仓库历史分析的执行结果,包含操作状态和输出数据。
## 适用场景

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

## 使用流程

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

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

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

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100

检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100

检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100

检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过

改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
