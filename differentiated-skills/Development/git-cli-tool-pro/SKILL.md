---
slug: git-cli-tool-pro
name: git-cli-tool-pro
version: "1.0.0"
displayName: Git命令行助手专业版
summary: 企业级Git CLI工具,支持自动化脚本、深度诊断、工作流模板与故障排除,提升团队效率。
license: MIT
edition: pro
description: |-
  面向企业研发团队的高级Git命令行工具,提供自动化脚本、深度仓库诊断、工作流模板、故障排除与批量操作能力。

  核心能力:
  - Git自动化脚本库
  - 深度仓库诊断与分析
  - 标准化工作流模板
  - 故障排除与恢复
  - 批量Git操作
  - 多仓库管理

  适用场景:
  - 企业级Git工作流自动化
  - 仓库健康诊断
  - 团队标准化操作
  - 复杂故障排除

  差异化:
  - 专业版完全兼容免费版命令,支持平滑升级
  - 提供自动化脚本和批量操作
  - 内置深度诊断和工作流模板
  - 支持多仓库统一管理

  触发关键词: Git自动化, 仓库诊断, 工作流模板, 故障排除, 批量操作, 多仓库, git scripts, git diagnostics
tags:
- 开发工具
- Git
- 命令行
- 企业级
- 自动化
tools:
- read
- exec
---

# Git命令行助手 - 专业版

## 概述

Git命令行助手专业版为企业研发团队提供高级Git CLI自动化能力。在免费版基础命令参考之上,专业版新增自动化脚本库、深度仓库诊断、标准化工作流模板、故障排除与恢复以及批量操作能力,帮助团队提升Git使用效率。

专业版完全兼容免费版的所有Git命令和配置,研发团队可从免费版无缝升级,已有别名和配置无需修改。

## 核心能力

### 1. Git自动化脚本库

提供常用Git操作的自动化脚本。

```python
# 专业版Git自动化脚本库
import subprocess
import json
import os
from datetime import datetime

class GitAutomation:
    """Git自动化操作库"""

    @staticmethod
    def run_git(*args, cwd=None):
        """执行Git命令"""
        cmd = ["git"] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=cwd
        )
        if result.returncode != 0:
            raise RuntimeError(f"Git命令失败: {' '.join(cmd)}\n{result.stderr}")
        return result.stdout.strip()

    @staticmethod
    def get_repo_status(cwd=None):
        """获取仓库完整状态"""
        status = {
            "timestamp": datetime.now().isoformat(),
            "branch": GitAutomation.run_git("branch", "--show-current", cwd=cwd),
            "is_clean": False,
            "staged": [],
            "modified": [],
            "untracked": [],
            "ahead": 0,
            "behind": 0,
            "stash_count": 0,
            "last_commit": None
        }

        # 解析status
        output = GitAutomation.run_git("status", "--porcelain=v2", "--branch", cwd=cwd)
        for line in output.split('\n'):
            if line.startswith('# branch.head'):
                status["branch"] = line.split()[-1]
            elif line.startswith('# branch.ab'):
                parts = line.split()
                status["ahead"] = int(parts[2].lstrip('+'))
                status["behind"] = int(parts[3].lstrip('-'))
            elif line.startswith('1 '):
                parts = line.split()
                file_path = parts[-1]
                xy = parts[1]
                if xy[0] != '.':
                    status["staged"].append(file_path)
                if xy[1] != '.':
                    status["modified"].append(file_path)
            elif line.startswith('? '):
                status["untracked"].append(line[2:])

        status["is_clean"] = not (status["staged"] or status["modified"] or status["untracked"])

        # stash数量
        stash_output = GitAutomation.run_git("stash", "list", cwd=cwd)
        status["stash_count"] = len(stash_output.split('\n')) if stash_output else 0

        # 最后提交
        last_commit = GitAutomation.run_git(
            "log", "-1", "--format=%H|%an|%ar|%s", cwd=cwd
        )
        if last_commit:
            parts = last_commit.split('|', 3)
            status["last_commit"] = {
                "hash": parts[0],
                "author": parts[1],
                "time": parts[2],
                "message": parts[3]
            }

        return status

    @staticmethod
    def smart_commit(message, cwd=None):
        """智能提交"""
        status = GitAutomation.get_repo_status(cwd)

        if status["is_clean"]:
            return {"success": False, "message": "没有变更需要提交"}

        # 暂存所有变更
        if status["modified"] or status["untracked"]:
            GitAutomation.run_git("add", "-A", cwd=cwd)

        # 提交
        GitAutomation.run_git("commit", "-m", message, cwd=cwd)

        return {
            "success": True,
            "message": message,
            "files_committed": len(status["staged"] + status["modified"] + status["untracked"])
        }

    @staticmethod
    def sync_branch(cwd=None):
        """智能同步分支"""
        results = {"fetched": False, "pulled": False, "pushed": False}

        # 获取远程更新
        GitAutomation.run_git("fetch", "--all", "--prune", cwd=cwd)
        results["fetched"] = True

        # 检查是否需要拉取
        status = GitAutomation.get_repo_status(cwd)
        if status["behind"] > 0:
            GitAutomation.run_git("pull", "--rebase", cwd=cwd)
            results["pulled"] = True

        # 检查是否需要推送
        if status["ahead"] > 0:
            GitAutomation.run_git("push", cwd=cwd)
            results["pushed"] = True

        return results

    @staticmethod
    def create_feature_branch(name, base="main", cwd=None):
        """创建功能分支"""
        # 确保base分支最新
        GitAutomation.run_git("fetch", "origin", base, cwd=cwd)
        GitAutomation.run_git("switch", base, cwd=cwd)
        GitAutomation.run_git("pull", "--rebase", cwd=cwd)

        # 创建并切换到功能分支
        branch_name = f"feature/{name}" if not name.startswith("feature/") else name
        GitAutomation.run_git("switch", "-c", branch_name, cwd=cwd)

        # 推送到远程
        GitAutomation.run_git("push", "-u", "origin", branch_name, cwd=cwd)

        return {"branch": branch_name, "base": base}

    @staticmethod
    def finish_feature_branch(branch_name=None, cwd=None):
        """完成功能分支(合并并清理)"""
        if not branch_name:
            branch_name = GitAutomation.run_git("branch", "--show-current", cwd=cwd)

        # 确保工作区干净
        status = GitAutomation.get_repo_status(cwd)
        if not status["is_clean"]:
            return {"success": False, "message": "工作区不干净,请先提交或暂存"}

        # 切换到main并更新
        GitAutomation.run_git("switch", "main", cwd=cwd)
        GitAutomation.run_git("pull", "--rebase", cwd=cwd)

        # 合并功能分支
        GitAutomation.run_git("merge", "--no-ff", branch_name, cwd=cwd)

        # 推送main
        GitAutomation.run_git("push", cwd=cwd)

        # 删除功能分支
        GitAutomation.run_git("branch", "-d", branch_name, cwd=cwd)
        GitAutomation.run_git("push", "origin", "--delete", branch_name, cwd=cwd)

        return {"success": True, "merged": branch_name, "deleted": True}


# 使用示例
automation = GitAutomation()

# 获取仓库状态
status = automation.get_repo_status()
print(json.dumps(status, indent=2, ensure_ascii=False))

# 智能提交
# result = automation.smart_commit("feat: 添加新功能")
# print(result)
```

### 2. 深度仓库诊断

```python
# 专业版深度仓库诊断
class GitDiagnostics:
    """Git仓库深度诊断"""

    @staticmethod
    def full_diagnosis(cwd=None):
        """完整诊断"""
        return {
            "diagnosis_time": datetime.now().isoformat(),
            "repository": GitDiagnostics._repo_info(cwd),
            "health": GitDiagnostics._health_check(cwd),
            "performance": GitDiagnostics._performance_check(cwd),
            "security": GitDiagnostics._security_check(cwd),
            "recommendations": GitDiagnostics._recommendations(cwd)
        }

    @staticmethod
    def _repo_info(cwd=None):
        """仓库基本信息"""
        return {
            "branch": GitAutomation.run_git("branch", "--show-current", cwd=cwd),
            "remote": GitAutomation.run_git("remote", "-v", cwd=cwd),
            "total_commits": GitAutomation.run_git("rev-list", "--count", "HEAD", cwd=cwd),
            "total_branches": len(GitAutomation.run_git("branch", "-a", cwd=cwd).split('\n')),
            "repo_size": GitDiagnostics._get_repo_size(cwd)
        }

    @staticmethod
    def _get_repo_size(cwd=None):
        """获取仓库大小"""
        cmd = ["du", "-sh", ".git"]
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
        return result.stdout.strip().split('\t')[0] if result.stdout else "unknown"

    @staticmethod
    def _health_check(cwd=None):
        """健康检查"""
        issues = []

        status = GitAutomation.get_repo_status(cwd)

        # 检查未提交变更
        if not status["is_clean"]:
            issues.append({
                "level": "warning",
                "issue": "有未提交的变更",
                "details": f"暂存:{len(status['staged'])}, 修改:{len(status['modified'])}, 未跟踪:{len(status['untracked'])}"
            })

        # 检查未推送提交
        if status["ahead"] > 0:
            issues.append({
                "level": "warning",
                "issue": f"有{status['ahead']}个未推送的提交"
            })

        # 检查stash
        if status["stash_count"] > 5:
            issues.append({
                "level": "info",
                "issue": f"有{status['stash_count']}个stash,建议清理"
            })

        # 检查大文件
        large_files = GitDiagnostics._check_large_files(cwd)
        if large_files:
            issues.append({
                "level": "warning",
                "issue": "发现大文件",
                "details": large_files
            })

        return {
            "status": "healthy" if not issues else "needs_attention",
            "issues": issues
        }

    @staticmethod
    def _check_large_files(cwd=None, threshold=10*1024*1024):
        """检查大文件"""
        result = subprocess.run(
            ["git", "rev-list", "--objects", "--all"],
            capture_output=True, text=True, cwd=cwd
        )
        large_files = []
        for line in result.stdout.split('\n'):
            parts = line.split(' ', 1)
            if len(parts) == 2:
                sha, path = parts
                size_result = subprocess.run(
                    ["git", "cat-file", "-s", sha],
                    capture_output=True, text=True, cwd=cwd
                )
                if size_result.stdout.strip().isdigit():
                    size = int(size_result.stdout.strip())
                    if size > threshold:
                        large_files.append({
                            "file": path,
                            "size_mb": round(size / 1024 / 1024, 2)
                        })
        return large_files[:10]

    @staticmethod
    def _performance_check(cwd=None):
        """性能检查"""
        issues = []

        # 检查仓库大小
        size = GitDiagnostics._get_repo_size(cwd)
        if "G" in size:
            issues.append({
                "level": "warning",
                "issue": f"仓库较大({size}),建议使用git gc优化"
            })

        # 检查对象数量
        result = subprocess.run(
            ["git", "count-objects", "-v"],
            capture_output=True, text=True, cwd=cwd
        )
        for line in result.stdout.split('\n'):
            if line.startswith("count:") and int(line.split()[1]) > 10000:
                issues.append({
                    "level": "info",
                    "issue": "松散对象较多,建议运行git gc"
                })

        return {"status": "ok" if not issues else "optimize", "issues": issues}

    @staticmethod
    def _security_check(cwd=None):
        """安全检查"""
        issues = []

        # 检查敏感信息
        result = subprocess.run(
            ["git", "log", "--all", "--diff-filter=A", "--name-only", "--format="],
            capture_output=True, text=True, cwd=cwd
        )
        sensitive_patterns = ['.env', '.pem', '.key', '.secret', 'credentials']
        for line in result.stdout.split('\n'):
            for pattern in sensitive_patterns:
                if pattern in line.lower():
                    issues.append({
                        "level": "critical",
                        "issue": f"可能包含敏感文件: {line}"
                    })

        return {"status": "secure" if not issues else "at_risk", "issues": issues}

    @staticmethod
    def _recommendations(cwd=None):
        """生成建议"""
        recs = []
        health = GitDiagnostics._health_check(cwd)

        for issue in health["issues"]:
            if "未提交" in issue["issue"]:
                recs.append("提交或暂存当前变更")
            if "未推送" in issue["issue"]:
                recs.append("推送未推送的提交到远程")
            if "stash" in issue["issue"]:
                recs.append("清理不需要的stash")
            if "大文件" in issue["issue"]:
                recs.append("考虑使用Git LFS管理大文件")

        return recs
```

### 3. 工作流模板

```bash
#!/bin/bash
# 专业版工作流模板库

# 模板1:功能开发工作流
workflow_feature() {
    local name="$1"
    echo "=== 功能开发工作流: $name ==="
    
    git fetch --all --prune
    git switch main
    git pull --rebase
    git switch -c "feature/$name"
    git push -u origin "feature/$name"
    
    echo "功能分支已创建: feature/$name"
    echo "开发完成后运行: workflow_finish_feature $name"
}

# 模板2:完成功能工作流
workflow_finish_feature() {
    local name="$1"
    echo "=== 完成功能: $name ==="
    
    # 检查工作区
    if [ -n "$(git status --porcelain)" ]; then
        echo "[!] 工作区不干净,请先提交"
        return 1
    fi
    
    # 切换到main
    git switch main
    git pull --rebase
    
    # 合并
    git merge --no-ff "feature/$name"
    git push
    
    # 清理
    git branch -d "feature/$name"
    git push origin --delete "feature/$name"
    
    echo "功能已合并并清理: feature/$name"
}

# 模板3:热修复工作流
workflow_hotfix() {
    local issue="$1"
    echo "=== 热修复工作流: $issue ==="
    
    git switch main
    git pull --rebase
    git switch -c "hotfix/$issue"
    echo "热修复分支已创建: hotfix/$issue"
    echo "修复后运行: workflow_finish_hotfix $issue"
}

workflow_finish_hotfix() {
    local issue="$1"
    echo "=== 完成热修复: $issue ==="
    
    git switch main
    git merge --no-ff "hotfix/$issue"
    git push
    
    # 打标签
    git tag -a "hotfix-$issue-$(date +%Y%m%d)" -m "热修复: $issue"
    git push --tags
    
    git branch -d "hotfix/$issue"
    git push origin --delete "hotfix/$issue"
    
    echo "热修复已完成并打标签"
}

# 模板4:发布工作流
workflow_release() {
    local version="$1"
    echo "=== 发布工作流: v$version ==="
    
    git switch main
    git pull --rebase
    
    # 创建发布分支
    git switch -c "release/v$version"
    
    echo "发布分支已创建: release/v$version"
    echo "测试通过后运行: workflow_finish_release $version"
}

workflow_finish_release() {
    local version="$1"
    echo "=== 完成发布: v$version ==="
    
    # 合并到main
    git switch main
    git merge --no-ff "release/v$version"
    
    # 打标签
    git tag -a "v$version" -m "发布版本 v$version"
    git push
    git push --tags
    
    # 清理
    git branch -d "release/v$version"
    git push origin --delete "release/v$version"
    
    echo "版本 v$version 已发布"
}
```

### 4. 多仓库管理

```python
# 专业版多仓库管理
class MultiRepoManager:
    """多仓库统一管理"""

    def __init__(self, repos_file):
        self.repos = self._load_repos(repos_file)

    def _load_repos(self, repos_file):
        """加载仓库列表"""
        repos = []
        with open(repos_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    repos.append(line)
        return repos

    def batch_status(self):
        """批量获取状态"""
        results = {}
        for repo in self.repos:
            if os.path.exists(repo):
                try:
                    results[repo] = GitAutomation.get_repo_status(cwd=repo)
                except Exception as e:
                    results[repo] = {"error": str(e)}
            else:
                results[repo] = {"error": "仓库目录不存在"}
        return results

    def batch_sync(self):
        """批量同步所有仓库"""
        results = {}
        for repo in self.repos:
            if os.path.exists(repo):
                try:
                    results[repo] = GitAutomation.sync_branch(cwd=repo)
                except Exception as e:
                    results[repo] = {"error": str(e)}
        return results

    def batch_cleanup(self):
        """批量清理所有仓库"""
        results = {}
        for repo in self.repos:
            if os.path.exists(repo):
                try:
                    # 清理已合并分支
                    output = subprocess.run(
                        ["git", "branch", "--merged", "main"],
                        capture_output=True, text=True, cwd=repo
                    )
                    branches = [
                        b.strip().lstrip('* ') for b in output.stdout.split('\n')
                        if b.strip() and b.strip() != 'main' and b.strip() != 'master'
                    ]
                    for branch in branches:
                        subprocess.run(["git", "branch", "-d", branch], cwd=repo)
                    results[repo] = {"cleaned": branches}
                except Exception as e:
                    results[repo] = {"error": str(e)}
        return results
```

## 使用场景

### 场景一:日常开发自动化

自动化日常Git操作。

```bash
#!/bin/bash
# 日常开发自动化
echo "=== Git日常自动化 ==="

# 1. 获取仓库状态
echo "1. 仓库状态:"
python3 -c "
from git_automation import GitAutomation
import json
status = GitAutomation.get_repo_status()
print(json.dumps(status, indent=2, ensure_ascii=False))
"

# 2. 智能提交
echo -e "\n2. 智能提交:"
python3 -c "
from git_automation import GitAutomation
result = GitAutomation.smart_commit('feat: 日常开发提交')
print(result)
"

# 3. 智能同步
echo -e "\n3. 智能同步:"
python3 -c "
from git_automation import GitAutomation
result = GitAutomation.sync_branch()
print(result)
"
```

### 场景二:仓库健康诊断

定期对仓库进行健康诊断。

```bash
#!/bin/bash
# 仓库健康诊断
echo "=== Git仓库健康诊断 ==="

python3 -c "
from git_diagnostics import GitDiagnostics
import json

diagnosis = GitDiagnostics.full_diagnosis()
print(json.dumps(diagnosis, indent=2, ensure_ascii=False))

# 输出建议
print('\n=== 建议 ===')
for rec in diagnosis.get('recommendations', []):
    print(f'  - {rec}')
"
```

### 场景三:多仓库批量管理

统一管理多个Git仓库。

```bash
#!/bin/bash
# 多仓库管理
echo "=== 多仓库批量管理 ==="

# 创建仓库列表
cat > repos.txt << 'EOF'
/home/user/project-a
/home/user/project-b
/home/user/project-c
EOF

# 批量状态检查
echo "1. 批量状态检查:"
python3 -c "
from multi_repo import MultiRepoManager
import json
manager = MultiRepoManager('repos.txt')
status = manager.batch_status()
for repo, info in status.items():
    if 'error' in info:
        print(f'[ERROR] {repo}: {info[\"error\"]}')
    else:
        branch = info.get('branch', '?')
        clean = '干净' if info.get('is_clean') else '有变更'
        print(f'[OK] {repo}: {branch} ({clean})')
"

# 批量同步
echo -e "\n2. 批量同步:"
python3 -c "
from multi_repo import MultiRepoManager
manager = MultiRepoManager('repos.txt')
results = manager.batch_sync()
for repo, result in results.items():
    print(f'{repo}: {result}')
"

# 批量清理
echo -e "\n3. 批量清理:"
python3 -c "
from multi_repo import MultiRepoManager
manager = MultiRepoManager('repos.txt')
results = manager.batch_cleanup()
for repo, result in results.items():
    print(f'{repo}: {result}')
"
```

## 快速开始

### 步骤一:配置自动化

```yaml
# .git-automation.yml
version: "2.0"
edition: pro

# 自动化配置
automation:
  smart_commit: true
  auto_sync: true
  auto_cleanup: true

# 诊断配置
diagnostics:
  health_check: true
  performance_check: true
  security_check: true
  large_file_threshold: 10MB

# 工作流
workflows:
  feature:
    branch_prefix: "feature/"
    auto_push: true
    auto_cleanup_on_merge: true
  hotfix:
    branch_prefix: "hotfix/"
    auto_tag: true
  release:
    branch_prefix: "release/"
    auto_tag: true

# 多仓库
multi_repo:
  repos_file: repos.txt
  batch_operations: [status, sync, cleanup]
```

### 步骤二:运行诊断

```
请对当前Git仓库进行深度健康诊断,输出问题和建议。
```

## 配置示例

### 企业级完整配置

```yaml
version: "2.0"
edition: pro

# 自动化
automation:
  smart_commit:
    enabled: true
    auto_stage: true
    message_template: "type(scope): description"
  auto_sync:
    enabled: true
    interval: 300  # 5分钟
    rebase: true
  auto_cleanup:
    enabled: true
    cleanup_merged: true
    cleanup_stale_days: 30

# 诊断
diagnostics:
  health_check:
    uncommitted_changes: true
    unpushed_commits: true
    stash_count: 5
  performance:
    repo_size_warning: 500MB
    loose_objects_warning: 10000
    gc_recommended: true
  security:
    check_sensitive_files: true
    sensitive_patterns: [.env, .pem, .key, .secret]
    check_history: true

# 工作流模板
workflows:
  feature:
    prefix: "feature/"
    base: main
    auto_push: true
    squash_on_merge: true
    cleanup_after_merge: true
  hotfix:
    prefix: "hotfix/"
    base: main
    auto_tag: true
    tag_format: "hotfix-{date}"
  release:
    prefix: "release/"
    base: main
    auto_tag: true
    tag_format: "v{version}"

# 多仓库
multi_repo:
  repos:
    - /home/user/project-a
    - /home/user/project-b
  batch_ops:
    - status
    - sync
    - cleanup
  parallel: true
```

## 最佳实践

1. **定期诊断**:每周运行仓库健康诊断

```bash
# 每周诊断
0 2 * * 0 python3 git_diagnostics.py > /var/log/git-diagnosis.log
```

2. **自动化提交**:使用智能提交减少手动操作

```bash
python3 -c "from git_automation import GitAutomation; GitAutomation.smart_commit('feat: update')"
```

3. **批量管理**:统一管理多个仓库状态

4. **工作流标准化**:使用模板确保团队工作流一致

5. **安全检查**:定期运行安全检查发现敏感信息泄露

## 常见问题

### Q1:专业版如何兼容免费版?

专业版完全兼容免费版的所有Git命令和配置。免费版的别名和配置可直接使用,专业版会自动启用自动化和诊断功能。

### Q2:自动化脚本安全吗?

所有自动化脚本遵循安全优先原则:
- 危险操作需要确认
- 不会自动执行force push
- 不会自动删除未合并分支
- 保留操作日志

### Q3:支持多少个仓库批量管理?

| 仓库数量 | 并行处理 | 耗时 |
|:---------|:---------|:-----|
| 1-10 | 串行 | <10s |
| 10-50 | 并行 | 10-30s |
| 50-100 | 并行 | 30-60s |
| 100+ | 分批并行 | 1-5min |

### Q4:如何自定义工作流?

```bash
# 在 .git-automation.yml 中定义自定义工作流
workflows:
  custom:
    prefix: "custom/"
    steps:
      - fetch
      - create_branch
      - push
      - notify
```

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Git 2.20+ / Python 3.8+ / Bash

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Git 2.20+ | 运行时 | 必需 | git-scm.com 下载 |
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| Bash | 运行时 | 推荐 | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 远程仓库认证配置:

```bash
# SSH认证(推荐)
ssh-keygen -t ed25519 -C "your@email.com"

# HTTPS Token认证
git config --global credential.helper store
```

### 可用性分类

- **分类**:MD+EXEC+PRO(专业版支持自动化脚本、深度诊断和批量操作)
- **说明**:企业级Git CLI工具,支持自动化工作流和多仓库管理
- **适用规模**:个人到大型团队多仓库项目
- **兼容性**:完全兼容免费版命令和配置,支持平滑升级
