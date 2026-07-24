# 详细参考 - git-essentials-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
class TagManager:
    """标签与版本管理器"""

    @staticmethod
    def list_tags(pattern=None):
        """列出标签"""
        cmd = ["git", "tag", "-l"]
        if pattern:
            cmd.append(pattern)
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip().split('\n') if result.stdout else []

    @staticmethod
    def create_version_tag(version, message=None, commit=None):
        """创建版本标签"""
        cmd = ["git", "tag", "-a", f"v{version}", "-m", message or f"版本 {version}"]
        if commit:
            cmd.append(commit)
        subprocess.run(cmd)
        print(f"标签 v{version} 已创建")

    @staticmethod
    def batch_tag_commits(prefix, start, end, base="v"):
        """批量创建标签"""
        for i in range(start, end + 1):
            version = f"{base}{prefix}.{i}"
            TagManager.create_version_tag(version, f"自动标签 {version}")

    @staticmethod
    def push_tags(remote="origin"):
        """推送所有标签"""
        subprocess.run(["git", "push", remote, "--tags"])
        print("标签已推送到远程")

    @staticmethod
    def delete_tag(version, remote=False):
        """删除标签"""
        subprocess.run(["git", "tag", "-d", f"v{version}"])
        if remote:
            subprocess.run(["git", "push", "origin", "--delete", f"v{version}"])
        print(f"标签 v{version} 已删除")

    @staticmethod
    def tag_report():
        """生成标签报告"""
        tags = TagManager.list_tags()
        report = {"total_tags": len(tags), "tags": []}
        for tag in tags:
            result = subprocess.run(
                ["git", "log", "-1", "--format=%H|%ai|%an|%s", tag],
                capture_output=True, text=True
            )
            if result.stdout:
                parts = result.stdout.strip().split('|', 3)
                report["tags"].append({
                    "tag": tag,
                    "commit": parts[0],
                    "date": parts[1],
                    "author": parts[2],
                    "message": parts[3]
                })
        return report
```

## 代码示例 (python)

```python
import subprocess

class RebaseHelper:
    """交互式变基辅助工具"""

    @staticmethod
    def squash_commits(count, message=None):
        """压缩最近N个提交"""
        if message:
            cmd = f"git rebase -i --autosquash HEAD~{count}"
        else:
            cmd = f"git rebase -i HEAD~{count}"
        print(f"执行: {cmd}")
        print("在编辑器中将除第一个外的pick改为squash或fixup")

    @staticmethod
    def reword_last_message(new_message):
        """修改最近的提交信息"""
        subprocess.run([
            "git", "commit", "--amend", "-m", new_message
        ])

    @staticmethod
    def split_commit(commit_hash):
        """拆分提交"""
        print(f"拆分提交: {commit_hash}")
        subprocess.run(["git", "rebase", "-i", f"{commit_hash}~1"])
        print("在编辑器中将该提交改为edit")
        print("然后运行: git reset HEAD~")
        print("分别暂存和提交拆分后的内容")
        print("最后运行: git rebase --continue")

    @staticmethod
    def reorder_commits(count):
        """重排提交顺序"""
        print(f"重排最近{count}个提交")
        subprocess.run(["git", "rebase", "-i", f"HEAD~{count}"])
        print("在编辑器中调整提交顺序")

    @staticmethod
    def safe_rebase(target_branch):
        """安全变基(创建备份分支)"""
        current = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True
        ).stdout.strip()

        backup = f"backup/{current}-{subprocess.run(['date', '+%Y%m%d%H%M%S'], capture_output=True, text=True).stdout.strip()}"
        subprocess.run(["git", "branch", backup])
        print(f"备份分支已创建: {backup}")

        result = subprocess.run(["git", "rebase", target_branch])
        if result.returncode != 0:
            print("变基失败,可回滚:")
            print(f"  git rebase --abort")
            print(f"  git reset --hard {backup}")
        else:
            print(f"变基成功,备份在 {backup}")
```

## 代码示例 (python)

```python
class HistoryRewriter:
    """安全的历史重写工具"""

    @staticmethod
    def find_sensitive_files():
        """查找历史中的敏感文件"""
        result = subprocess.run(
            ["git", "log", "--all", "--diff-filter=A", "--name-only",
             "--format=", "--", "*.env", "*.pem", "*.key", "*.secret"],
            capture_output=True, text=True
        )
        return list(set(result.stdout.strip().split('\n')))

    @staticmethod
    def find_large_files(threshold_mb=10):
        """查找历史中的大文件"""
        result = subprocess.run(
            ["git", "rev-list", "--objects", "--all"],
            capture_output=True, text=True
        )
        large_files = []
        for line in result.stdout.split('\n'):
            parts = line.split(' ', 1)
            if len(parts) == 2:
                sha, path = parts
                size_result = subprocess.run(
                    ["git", "cat-file", "-s", sha],
                    capture_output=True, text=True
                )
                if size_result.stdout.strip().isdigit():
                    size = int(size_result.stdout.strip())
                    if size > threshold_mb * 1024 * 1024:
                        large_files.append({
                            "path": path,
                            "size_mb": round(size / 1024 / 1024, 2),
                            "sha": sha
                        })
        return sorted(large_files, key=lambda x: x["size_mb"], reverse=True)

    @staticmethod
    def create_backup_branch():
        """创建备份分支"""
        import time
        timestamp = time.strftime("%Y%m%d%H%M%S")
        branch_name = f"backup/before-rewrite-{timestamp}"
        subprocess.run(["git", "branch", branch_name])
        print(f"备份分支已创建: {branch_name}")
        return branch_name
```

## 代码示例 (python)

```python
class SubmoduleManager:
    """子模块批量管理器"""

    @staticmethod
    def list_submodules():
        """列出所有子模块"""
        result = subprocess.run(
            ["git", "submodule", "status"],
            capture_output=True, text=True
        )
        submodules = []
        for line in result.stdout.strip().split('\n'):
            parts = line.strip().split()
            if len(parts) >= 2:
                submodules.append({
                    "sha": parts[0].lstrip('-+U'),
                    "path": parts[1],
                    "status": "normal" if parts[0][0] != '-' else "uninitialized"
                })
        return submodules

    @staticmethod
    def batch_update():
        """批量更新所有子模块"""
        result = subprocess.run(
            ["git", "submodule", "update", "--remote", "--merge"],
            capture_output=True, text=True
        )
        return result.stdout

    @staticmethod
    def batch_command(command):
        """在所有子模块中执行命令"""
        result = subprocess.run(
            ["git", "submodule", "foreach", command],
            capture_output=True, text=True
        )
        return result.stdout

    @staticmethod
    def batch_checkout(branch):
        """批量切换子模块分支"""
        return SubmoduleManager.batch_command(f"git checkout {branch}")
```

## 代码示例 (yaml)

```yaml
version: "2.0"
edition: pro

history:
  safe_rewrite: true
  create_backup: true
  backup_prefix: "backup/"

submodules:
  auto_update: false
  default_branch: main
  recursive: true

optimization:
  auto_gc: false
  gc_threshold: 500MB
  aggressive_gc: false

tags:
  format: "v{major}.{minor}.{patch}"
  annotated: true
  auto_push: true

rebase:
  autosquash: true
  autostash: true
  safe_mode: true

bisect:
  auto_test: true
  test_script: ./bisect-test.sh
```

