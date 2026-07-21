# 详细参考 - git-toolkit-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
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

## 代码示例 (bash)

```bash
#!/bin/bash
echo "=== Git Hook 管理 ==="

HOOKS_DIR=".git/hooks"
TEAM_HOOKS_DIR=".githooks"

install_hooks() {
    echo "安装团队Git Hook..."

    mkdir -p "$TEAM_HOOKS_DIR"

    git config core.hooksPath "$TEAM_HOOKS_DIR"

    cat > "$TEAM_HOOKS_DIR/pre-commit" << 'EOF'
#!/bin/bash
echo "=== Pre-commit 检查 ==="

BRANCH=$(git branch --show-current)
echo "当前分支: $BRANCH"

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

echo "检查敏感信息..."
SECRET=$(echo "$STAGED" | xargs grep -lE "(password|secret|api_key)\s*=\s*['\"]" 2>/dev/null)
if [ -n "$SECRET" ]; then
    echo "[!] 发现敏感信息:"
    echo "$SECRET"
    exit 1
fi

LARGE_FILES=$(git diff --cached --name-only | xargs -I{} sh -c 'test -f "{}" && wc -c "{}" | awk "{if(\$1>1048576) print \$2}"' 2>/dev/null)
if [ -n "$LARGE_FILES" ]; then
    echo "[!] 发现大文件(>1MB):"
    echo "$LARGE_FILES"
    exit 1
fi

echo "[OK] Pre-commit 检查通过"
EOF
    chmod +x "$TEAM_HOOKS_DIR/pre-commit"

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

FIRST_LINE=$(echo "$MSG" | head -1)
if [ ${#FIRST_LINE} -gt 72 ]; then
    echo "[!] 首行长度超过72字符"
    exit 1
fi

echo "[OK] 提交信息规范"
EOF
    chmod +x "$TEAM_HOOKS_DIR/commit-msg"

    cat > "$TEAM_HOOKS_DIR/pre-push" << 'EOF'
#!/bin/bash
echo "=== Pre-push 检查 ==="

BRANCH=$(git branch --show-current)

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

uninstall_hooks() {
    git config --unset core.hooksPath
    echo "Hook已卸载"
}

case "$1" in
    install) install_hooks ;;
    uninstall) uninstall_hooks ;;
    *) echo "用法: $0 {install|uninstall}" ;;
esac
```

## 代码示例 (python)

```python
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

manager = BranchManager()

report = manager.branch_report()
print(json.dumps(report, indent=2, ensure_ascii=False))
```

## 代码示例 (python)

```python
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

        if not CodeReviewAutomation.COMMIT_PATTERN.match(message):
            issues.append({
                "severity": "error",
                "message": "提交信息不符合Conventional Commits规范",
                "expected": "type(scope): description",
                "actual": message[:100]
            })

        first_line = message.split('\n')[0]
        if len(first_line) > 72:
            issues.append({
                "severity": "warning",
                "message": f"首行长度{len(first_line)}超过72字符"
            })

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

