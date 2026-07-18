---
slug: git-toolkit-pro
name: git-toolkit-pro
version: "1.0.0"
displayName: Git工具包专业版
summary: 企业级Git管理,支持批量分支操作、自动化审查、Git Hook管理与CI/CD流水线集成。
license: MIT
edition: pro
description: |-
  面向企业研发团队的高级Git管理工具,提供批量分支操作、自动化代码审查、Git Hook管理、历史分析与CI/CD流水线集成。

  核心能力:
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
  - 支持Git Hook统一管理
  - 内置团队协作工作流模板

  触发关键词: Git管理, 批量分支, 代码审查, Git Hook, 提交规范, 仓库分析, CI/CD, team workflow, git automation
tags:
- 开发工具
- Git
- 版本控制
- 企业级
- DevOps
tools:
- read
- exec
---

# Git工具包 - 专业版

## 概述

Git工具包专业版为企业研发团队提供高级Git管理能力。在免费版基础Git操作之上,专业版新增批量分支管理、自动化代码审查、Git Hook统一管理、提交规范强制执行和仓库历史深度分析,满足企业级团队协作需求。

专业版完全兼容免费版的所有Git命令和配置,研发团队可从免费版无缝升级,已有Git配置和别名无需修改。

## 核心能力

### 1. 批量分支管理

支持批量创建、清理和管理分支。

```python
# 专业版批量分支管理工具
import subprocess
import json
from datetime import datetime

class BranchManager:
    """批量分支管理器"""

    @staticmethod
    def list_branches(remote=False, merged=None):
        """列出分支"""
        cmd = ["git", "branch"]
        if remote:
            cmd.append("-r")
        if merged:
            cmd.extend(["--merged", merged])

        result = subprocess.run(cmd, capture_output=True, text=True)
        branches = []
        for line in result.stdout.strip().split('\n'):
            branch = line.strip().lstrip('* ').strip()
            if branch and 'HEAD' not in branch:
                branches.append(branch)
        return branches

    @staticmethod
    def batch_create(prefix, count, base_branch="main"):
        """批量创建分支"""
        created = []
        for i in range(1, count + 1):
            branch_name = f"{prefix}-{i:03d}"
            result = subprocess.run(
                ["git", "checkout", "-b", branch_name, base_branch],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                created.append(branch_name)
                print(f"[OK] 创建分支: {branch_name}")
            else:
                print(f"[FAIL] 创建失败: {branch_name} - {result.stderr}")
        return created

    @staticmethod
    def batch_delete(branches, force=False):
        """批量删除分支"""
        deleted = []
        flag = "-D" if force else "-d"
        for branch in branches:
            result = subprocess.run(
                ["git", "branch", flag, branch],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                deleted.append(branch)
                print(f"[OK] 删除分支: {branch}")
            else:
                print(f"[FAIL] 删除失败: {branch} - {result.stderr.strip()}")
        return deleted

    @staticmethod
    def cleanup_merged(base_branch="main"):
        """清理已合并的分支"""
        merged = BranchManager.list_branches(merged=base_branch)
        # 排除当前分支和基础分支
        current = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True
        ).stdout.strip()

        to_delete = [b for b in merged if b != base_branch and b != current]
        if to_delete:
            print(f"清理 {len(to_delete)} 个已合并分支:")
            BranchManager.batch_delete(to_delete)
        else:
            print("没有需要清理的分支")
        return to_delete

    @staticmethod
    def branch_report():
        """生成分支报告"""
        branches = BranchManager.list_branches()
        report = {
            "total_branches": len(branches),
            "branches": []
        }
        for branch in branches:
            # 获取最后提交信息
            result = subprocess.run(
                ["git", "log", "-1", "--format=%H|%an|%ar|%s", branch],
                capture_output=True, text=True
            )
            if result.stdout:
                parts = result.stdout.strip().split('|', 3)
                report["branches"].append({
                    "name": branch,
                    "last_commit": parts[0] if len(parts) > 0 else "",
                    "author": parts[1] if len(parts) > 1 else "",
                    "last_update": parts[2] if len(parts) > 2 else "",
                    "message": parts[3] if len(parts) > 3 else ""
                })
        return report


# 使用示例
manager = BranchManager()

# 清理已合并分支
# manager.cleanup_merged("main")

# 生成分支报告
report = manager.branch_report()
print(json.dumps(report, indent=2, ensure_ascii=False))
```

### 2. 自动化代码审查

自动检查提交规范和代码质量。

```python
# 专业版自动化代码审查
import re
from datetime import datetime

class CodeReviewAutomation:
    """自动化代码审查"""

    COMMIT_PATTERN = re.compile(
        r'^(feat|fix|docs|style|refactor|test|chore|perf|ci|build)'
        r'(\(\w+\))?'
        r':\s+.+'
    )

    @staticmethod
    def check_commit_message(message):
        """检查提交信息规范"""
        issues = []

        # 检查格式
        if not CodeReviewAutomation.COMMIT_PATTERN.match(message):
            issues.append({
                "severity": "error",
                "message": "提交信息不符合Conventional Commits规范",
                "expected": "type(scope): description",
                "actual": message[:100]
            })

        # 检查长度
        first_line = message.split('\n')[0]
        if len(first_line) > 72:
            issues.append({
                "severity": "warning",
                "message": f"首行长度{len(first_line)}超过72字符"
            })

        # 检查类型
        types = ['feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore', 'perf', 'ci', 'build']
        msg_type = message.split('(')[0].split(':')[0]
        if msg_type not in types:
            issues.append({
                "severity": "error",
                "message": f"未知的提交类型: {msg_type}",
                "valid_types": types
            })

        return issues

    @staticmethod
    def review_diff(diff_content):
        """审查代码差异"""
        issues = []

        # 检查调试代码
        debug_patterns = [
            (r'console\.log', "发现console.log调试代码"),
            (r'debugger;', "发现debugger语句"),
            (r'print\(', "发现print调试代码"),
        ]

        for pattern, message in debug_patterns:
            if re.search(pattern, diff_content):
                issues.append({
                    "severity": "warning",
                    "message": message
                })

        # 检查敏感信息
        secret_patterns = [
            (r'password\s*=\s*["\']', "发现硬编码密码"),
            (r'api_key\s*=\s*["\']', "发现硬编码API密钥"),
            (r'secret\s*=\s*["\']', "发现硬编码密钥"),
        ]

        for pattern, message in secret_patterns:
            if re.search(pattern, diff_content, re.IGNORECASE):
                issues.append({
                    "severity": "error",
                    "message": message
                })

        # 检查TODO/FIXME
        if re.search(r'\b(TODO|FIXME|HACK)\b', diff_content):
            issues.append({
                "severity": "info",
                "message": "发现TODO/FIXME标记"
            })

        return issues

    @staticmethod
    def generate_review_report(commit_info, diff_content):
        """生成审查报告"""
        message_issues = CodeReviewAutomation.check_commit_message(
            commit_info.get("message", "")
        )
        code_issues = CodeReviewAutomation.review_diff(diff_content)

        return {
            "review_time": datetime.now().isoformat(),
            "commit": commit_info.get("hash", ""),
            "author": commit_info.get("author", ""),
            "message_issues": message_issues,
            "code_issues": code_issues,
            "summary": {
                "errors": sum(1 for i in message_issues + code_issues if i["severity"] == "error"),
                "warnings": sum(1 for i in message_issues + code_issues if i["severity"] == "warning"),
                "infos": sum(1 for i in message_issues + code_issues if i["severity"] == "info"),
            },
            "recommendation": "阻断合并" if any(i["severity"] == "error" for i in message_issues + code_issues) else "允许合并"
        }
```

### 3. Git Hook 统一管理

```bash
#!/bin/bash
# 专业版Git Hook管理工具
echo "=== Git Hook 管理 ==="

HOOKS_DIR=".git/hooks"
TEAM_HOOKS_DIR=".githooks"

# 安装团队Hook
install_hooks() {
    echo "安装团队Git Hook..."
    
    # 创建团队Hook目录
    mkdir -p "$TEAM_HOOKS_DIR"
    
    # 配置Git使用团队Hook目录
    git config core.hooksPath "$TEAM_HOOKS_DIR"
    
    # pre-commit hook
    cat > "$TEAM_HOOKS_DIR/pre-commit" << 'EOF'
#!/bin/bash
echo "=== Pre-commit 检查 ==="

# 1. 检查提交规范
BRANCH=$(git branch --show-current)
echo "当前分支: $BRANCH"

# 2. 检查调试代码
STAGED=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(js|ts|py)$')
if [ -n "$STAGED" ]; then
    echo "检查调试代码..."
    DEBUG=$(echo "$STAGED" | xargs grep -l "console.log\|debugger\|print(" 2>/dev/null)
    if [ -n "$DEBUG" ]; then
        echo "[!] 发现调试代码:"
        echo "$DEBUG"
        exit 1
    fi
fi

# 3. 检查敏感信息
echo "检查敏感信息..."
SECRET=$(echo "$STAGED" | xargs grep -lE "(password|secret|api_key)\s*=\s*['\"]" 2>/dev/null)
if [ -n "$SECRET" ]; then
    echo "[!] 发现敏感信息:"
    echo "$SECRET"
    exit 1
fi

# 4. 检查文件大小
LARGE_FILES=$(git diff --cached --name-only | xargs -I{} sh -c 'test -f "{}" && wc -c "{}" | awk "{if(\$1>1048576) print \$2}"' 2>/dev/null)
if [ -n "$LARGE_FILES" ]; then
    echo "[!] 发现大文件(>1MB):"
    echo "$LARGE_FILES"
    exit 1
fi

echo "[OK] Pre-commit 检查通过"
EOF
    chmod +x "$TEAM_HOOKS_DIR/pre-commit"
    
    # commit-msg hook
    cat > "$TEAM_HOOKS_DIR/commit-msg" << 'EOF'
#!/bin/bash
echo "=== Commit-msg 检查 ==="

MSG=$(cat "$1")
PATTERN='^(feat|fix|docs|style|refactor|test|chore|perf|ci|build)(\(\w+\))?:\s+.+'

if ! echo "$MSG" | grep -qE "$PATTERN"; then
    echo "[!] 提交信息不符合规范!"
    echo "格式: type(scope): description"
    echo "类型: feat|fix|docs|style|refactor|test|chore|perf|ci|build"
    echo "示例: feat(auth): 添加用户登录功能"
    exit 1
fi

# 检查首行长度
FIRST_LINE=$(echo "$MSG" | head -1)
if [ ${#FIRST_LINE} -gt 72 ]; then
    echo "[!] 首行长度超过72字符"
    exit 1
fi

echo "[OK] 提交信息规范"
EOF
    chmod +x "$TEAM_HOOKS_DIR/commit-msg"
    
    # pre-push hook
    cat > "$TEAM_HOOKS_DIR/pre-push" << 'EOF'
#!/bin/bash
echo "=== Pre-push 检查 ==="

BRANCH=$(git branch --show-current)

# 禁止直接推送到main/master
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
    echo "[!] 禁止直接推送到 $BRANCH 分支"
    echo "请通过Pull Request合并代码"
    exit 1
fi

echo "[OK] Pre-push 检查通过"
EOF
    chmod +x "$TEAM_HOOKS_DIR/pre-push"
    
    echo "Hook安装完成:"
    ls -la "$TEAM_HOOKS_DIR/"
}

# 卸载Hook
uninstall_hooks() {
    git config --unset core.hooksPath
    echo "Hook已卸载"
}

# 主逻辑
case "$1" in
    install) install_hooks ;;
    uninstall) uninstall_hooks ;;
    *) echo "用法: $0 {install|uninstall}" ;;
esac
```

### 4. 仓库历史分析

```python
# 专业版仓库历史分析
import subprocess
import json
from collections import Counter
from datetime import datetime, timedelta

class RepositoryAnalyzer:
    """仓库历史分析器"""

    @staticmethod
    def contributor_stats():
        """贡献者统计"""
        result = subprocess.run(
            ["git", "shortlog", "-sn", "--all"],
            capture_output=True, text=True
        )
        contributors = []
        for line in result.stdout.strip().split('\n'):
            if line:
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    contributors.append({
                        "commits": int(parts[0]),
                        "author": parts[1]
                    })
        return contributors

    @staticmethod
    def commit_frequency(days=30):
        """提交频率分析"""
        since = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        result = subprocess.run(
            ["git", "log", "--since", since, "--format", "%ad", "--date", "short"],
            capture_output=True, text=True
        )
        dates = result.stdout.strip().split('\n')
        frequency = Counter(dates)
        return {
            "period_days": days,
            "total_commits": len(dates),
            "daily_average": round(len(dates) / days, 2),
            "most_active_day": frequency.most_common(1)[0] if frequency else None,
            "frequency": dict(sorted(frequency.items()))
        }

    @staticmethod
    def file_change_stats():
        """文件变更统计"""
        result = subprocess.run(
            ["git", "log", "--name-only", "--format", "COMMIT:%H"],
            capture_output=True, text=True
        )
        file_changes = Counter()
        for line in result.stdout.split('\n'):
            if line and not line.startswith('COMMIT:'):
                file_changes[line] += 1
        return {
            "most_changed": file_changes.most_common(20),
            "total_unique_files": len(file_changes)
        }

    @staticmethod
    def branch_analysis():
        """分支分析"""
        # 获取所有分支
        result = subprocess.run(
            ["git", "branch", "-a", "--format", "%(refname:short)"],
            capture_output=True, text=True
        )
        branches = [b.strip() for b in result.stdout.split('\n') if b.strip()]

        analysis = {
            "total_branches": len(branches),
            "active_branches": [],
            "stale_branches": []
        }

        threshold = datetime.now() - timedelta(days=30)
        for branch in branches:
            # 获取最后提交时间
            log_result = subprocess.run(
                ["git", "log", "-1", "--format=%ai", branch],
                capture_output=True, text=True
            )
            if log_result.stdout:
                last_commit = datetime.fromisoformat(
                    log_result.stdout.strip().split('+')[0]
                )
                if last_commit > threshold:
                    analysis["active_branches"].append({
                        "branch": branch,
                        "last_commit": last_commit.isoformat()
                    })
                else:
                    analysis["stale_branches"].append({
                        "branch": branch,
                        "last_commit": last_commit.isoformat(),
                        "days_since": (datetime.now() - last_commit).days
                    })

        return analysis

    @staticmethod
    def generate_report():
        """生成完整分析报告"""
        return {
            "analysis_time": datetime.now().isoformat(),
            "contributors": RepositoryAnalyzer.contributor_stats(),
            "commit_frequency": RepositoryAnalyzer.commit_frequency(),
            "file_changes": RepositoryAnalyzer.file_change_stats(),
            "branch_analysis": RepositoryAnalyzer.branch_analysis()
        }
```

## 使用场景

### 场景一:团队工作流自动化

配置团队标准Git工作流。

```bash
#!/bin/bash
# 团队工作流自动化
echo "=== 团队Git工作流配置 ==="

# 1. 安装团队Hook
bash git-hooks.sh install

# 2. 配置标准别名
git config alias.feature 'checkout -b feature'
git config alias.hotfix 'checkout -b hotfix'
git config alias.release 'checkout -b release'
git config alias.cleanup '!git branch --merged main | grep -v "main" | xargs git branch -d'
git config alias.sync '!git fetch --all --prune && git pull --rebase'

# 3. 配置提交模板
cat > .gitmessage << 'EOF
# 提交信息格式: type(scope): description
# 类型: feat|fix|docs|style|refactor|test|chore|perf|ci|build
# 示例: feat(auth): 添加用户登录功能
#
# 首行不超过72字符
# 空行后写详细说明
EOF
git config commit.template .gitmessage

echo "团队工作流配置完成"
```

### 场景二:批量分支清理

定期清理过期分支。

```bash
#!/bin/bash
# 批量分支清理
echo "=== 分支清理 ==="

# 1. 获取远程更新
git fetch --all --prune

# 2. 清理本地已合并分支
echo "清理已合并分支..."
git branch --merged main | grep -v "main\|master\|develop" | \
    xargs -r git branch -d

# 3. 查找过期分支(30天无提交)
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

# 4. 生成分支报告
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
# GitLab CI配置
git_quality_check:
  stage: check
  script:
    # 1. 提交规范检查
    - |
      echo "检查提交规范..."
      MSG=$(git log -1 --format=%s)
      PATTERN='^(feat|fix|docs|style|refactor|test|chore|perf|ci|build)(\(\w+\))?:\s+.+'
      if ! echo "$MSG" | grep -qE "$PATTERN"; then
        echo "提交信息不符合规范: $MSG"
        exit 1
      fi
    
    # 2. 代码审查
    - |
      echo "自动化代码审查..."
      python3 code_review.py --diff "$(git diff origin/main...HEAD)" \
        --format json --output review-report.json
    
    # 3. 分支命名检查
    - |
      BRANCH=$(git branch --show-current)
      echo "当前分支: $BRANCH"
      if echo "$BRANCH" | grep -qE "^(feature|hotfix|release)/"; then
        echo "[OK] 分支命名规范"
      else
        echo "[!] 分支命名不规范,应为 feature/*, hotfix/*, release/*"
        exit 1
      fi
    
    # 4. 生成仓库报告
    - python3 repository_analyzer.py --output repo-report.json
  artifacts:
    paths:
      - review-report.json
      - repo-report.json
    expire_in: 30 days
```

## 快速开始

### 步骤一:配置团队环境

```yaml
# .git-team.yml
version: "2.0"
edition: pro

# 团队配置
team:
  default_branch: main
  branch_prefix:
    feature: "feature/"
    hotfix: "hotfix/"
    release: "release/"

# 提交规范
commit:
  conventional: true
  max_subject_length: 72
  require_scope: false

# Hook管理
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

# 分支管理
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

# 团队配置
team:
  name: "研发团队"
  default_branch: main
  protected_branches: [main, develop, release/*]

# 分支策略
branching:
  strategy: gitflow
  prefixes:
    feature: "feature/"
    hotfix: "hotfix/"
    release: "release/"
    bugfix: "bugfix/"
  auto_cleanup: true
  stale_days: 30

# 提交规范
commit:
  conventional: true
  types: [feat, fix, docs, style, refactor, test, chore, perf, ci, build]
  max_subject: 72
  require_scope: false
  template: .gitmessage

# Hook管理
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

# 代码审查
review:
  auto_review: true
  check_patterns:
    debug_code: true
    secrets: true
    todo_fixme: true
  block_on_error: true

# 仓库分析
analysis:
  contributor_stats: true
  commit_frequency: true
  branch_analysis: true
  file_change_stats: true
  report_schedule: weekly

# CI/CD集成
ci_cd:
  commit_check: true
  branch_check: true
  auto_review: true
  report_artifacts: true
```

## 最佳实践

1. **统一Hook**:团队共享Git Hook,确保规范一致

```bash
# 将Hook纳入版本控制
git add .githooks/
git commit -m "chore: 添加团队Git Hook"
```

2. **定期清理**:设置定期分支清理任务

```bash
# 每周清理
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
# 1. 将Hook放在项目目录
mkdir -p .githooks
cp hooks/* .githooks/

# 2. 配置Git使用共享Hook目录
git config core.hooksPath .githooks

# 3. 纳入版本控制
git add .githooks
git commit -m "chore: 共享Git Hook"

# 4. 团队成员克隆后配置
git config core.hooksPath .githooks
```

### Q3:如何绕过Hook(紧急情况)?

```bash
# 跳过pre-commit和commit-msg(仅紧急情况)
git commit --no-verify -m "hotfix: 紧急修复"

# 不建议常规使用
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
# SSH认证
git config --global credential.helper store

# 或使用Token认证
git remote set-url origin https://<token>@git.example.com/repo.git
```

### 可用性分类

- **分类**:MD+EXEC+PRO(专业版支持批量操作、Hook管理和仓库分析)
- **说明**:企业级Git管理工具,支持团队协作和自动化审查
- **适用规模**:中小型到大型团队项目
- **兼容性**:完全兼容免费版命令和配置,支持平滑升级
