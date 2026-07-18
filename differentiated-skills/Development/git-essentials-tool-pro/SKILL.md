---
slug: git-essentials-tool-pro
name: git-essentials-tool-pro
version: "1.0.0"
displayName: Git基础工具专业版
summary: 企业级Git版本控制,支持高级变基、历史重写、子模块批量管理、性能优化与团队协作。
license: MIT
edition: pro
description: |-
  面向研发团队的高级Git版本控制工具,提供交互式变基、历史重写、子模块批量管理、仓库性能优化与团队协作工作流。

  核心能力:
  - 高级交互式变基与历史重写
  - 子模块批量管理
  - 仓库性能优化(gc/fsck)
  - 二分查找(bisect)调试
  - 批量标签与版本管理
  - 团队协作工作流模板

  适用场景:
  - 企业级版本控制管理
  - 复杂历史整理与重写
  - 大型项目子模块管理
  - 版本发布与标签管理

  差异化:
  - 专业版完全兼容免费版命令,支持平滑升级
  - 提供高级历史管理能力
  - 支持子模块批量操作
  - 内置性能优化工具

  触发关键词: Git高级, 交互式变基, 历史重写, 子模块, bisect, git gc, 版本管理, git rebase -i, git filter-branch
tags:
- 开发工具
- Git
- 版本控制
- 企业级
tools:
- read
- exec
---

# Git基础工具 - 专业版

## 概述

Git基础工具专业版为研发团队提供高级版本控制能力。在免费版核心Git命令之上,专业版新增交互式变基、历史重写、子模块批量管理、仓库性能优化和二分查找调试,满足企业级版本控制需求。

专业版完全兼容免费版的所有Git命令和配置,研发团队可从免费版无缝升级,已有配置和别名无需修改。

## 核心能力

### 1. 高级交互式变基

使用交互式变基整理提交历史。

```bash
# 交互式变基最近N个提交
git rebase -i HEAD~5

# 变基操作选项:
# pick   - 保留提交
# reword - 修改提交信息
# edit   - 暂停修改提交内容
# squash - 合并到上一个提交
# fixup  - 合并并丢弃信息
# exec   - 执行命令
# drop   - 删除提交
# reword - 修改提交信息

# 变基过程中
git rebase --continue    # 解决冲突后继续
git rebase --skip        # 跳过当前提交
git rebase --abort       # 取消变基

# 自动变基(合并提交)
git rebase -i --autosquash HEAD~10

# 修改历史提交信息
git rebase -i HEAD~3
# 将要修改的提交从pick改为reword
```

```python
# 专业版变基辅助脚本
import subprocess

class RebaseHelper:
    """交互式变基辅助工具"""

    @staticmethod
    def squash_commits(count, message=None):
        """压缩最近N个提交"""
        if message:
            # 使用fixup自动合并
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

        # 创建备份分支
        backup = f"backup/{current}-{subprocess.run(['date', '+%Y%m%d%H%M%S'], capture_output=True, text=True).stdout.strip()}"
        subprocess.run(["git", "branch", backup])
        print(f"备份分支已创建: {backup}")

        # 执行变基
        result = subprocess.run(["git", "rebase", target_branch])
        if result.returncode != 0:
            print("变基失败,可回滚:")
            print(f"  git rebase --abort")
            print(f"  git reset --hard {backup}")
        else:
            print(f"变基成功,备份在 {backup}")
```

### 2. 历史重写

安全地重写Git历史。

```bash
# 修改全局作者信息
git filter-branch --env-filter '
    OLD_EMAIL="old@email.com"
    NEW_NAME="新名字"
    NEW_EMAIL="new@email.com"
    if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]; then
        export GIT_COMMITTER_NAME="$NEW_NAME"
        export GIT_COMMITTER_EMAIL="$NEW_EMAIL"
    fi
    if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]; then
        export GIT_AUTHOR_NAME="$NEW_NAME"
        export GIT_AUTHOR_EMAIL="$NEW_EMAIL"
    fi
' --tag-name-filter cat -- --branches --tags

# 从历史中删除文件
git filter-branch --tree-filter 'rm -f sensitive.txt' --prune-empty HEAD

# 使用git-filter-repo(推荐替代filter-branch)
# pip install git-filter-repo
git filter-repo --path sensitive.txt --invert-paths
git filter-repo --replace-text replacements.txt

# 从历史中删除大文件
git filter-branch --tree-filter 'rm -f large-file.bin' HEAD
git filter-repo --path large-file.bin --invert-paths

# 清理引用
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

```python
# 专业版历史重写工具
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

### 3. 子模块批量管理

```bash
#!/bin/bash
# 专业版子模块管理工具
echo "=== 子模块管理 ==="

# 添加子模块
git submodule add https://example.com/lib.git libs/lib
git submodule add -b main https://example.com/lib.git libs/lib

# 初始化和更新
git submodule init
git submodule update
git submodule update --init --recursive

# 克隆含子模块的仓库
git clone --recursive https://example.com/repo.git

# 批量更新所有子模块
git submodule foreach 'git pull origin main'
git submodule update --remote --merge

# 批量执行命令
git submodule foreach 'git status'
git submodule foreach 'git checkout main'

# 删除子模块
git submodule deinit -f libs/lib
git rm -f libs/lib
rm -rf .git/modules/libs/lib

# 查看子模块状态
git submodule status
git submodule summary
```

```python
# 专业版子模块批量管理
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

### 4. 二分查找调试

使用bisect定位问题引入的提交。

```bash
# 二分查找流程
git bisect start                    # 开始二分
git bisect bad                      # 标记当前版本有问题
git bisect good v1.0.0             # 标记v1.0.0是好的

# Git会自动切换到中间提交,测试后:
git bisect good                     # 标记当前提交是好的
git bisect bad                      # 标记当前提交是坏的
# 重复直到找到问题提交

# 自动二分(用脚本测试)
git bisect start HEAD v1.0.0 --
git bisect run ./test-script.sh     # 返回0=good, 1=bad

# 查看bisect日志
git bisect log

# 结束bisect
git bisect reset                    # 结束并回到原来分支

# 可视化bisect
git bisect visualize                # 查看剩余范围
```

```bash
#!/bin/bash
# 自动二分查找脚本示例
cat > bisect-test.sh << 'EOF'
#!/bin/bash
# 测试脚本:返回0=正常,1=有问题

# 运行测试
npm test > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "正常"
    exit 0
else
    echo "有问题"
    exit 1
fi
EOF
chmod +x bisect-test.sh

# 执行自动二分
git bisect start
git bisect bad HEAD
git bisect good v1.0.0
git bisect run ./bisect-test.sh
```

### 5. 仓库性能优化

```bash
# 仓库优化
git gc                              # 垃圾回收
git gc --aggressive                 # 深度回收
git gc --prune=now                  # 立即清理

# 仓库检查
git fsck                            # 检查完整性
git fsck --full                     # 完整检查

# 对象统计
git count-objects -v                # 对象统计
git count-objects -vH               # 人性化显示

# 压缩
git repack -a -d --depth=250 --window=250

# 优化前检查
echo "=== 优化前 ==="
git count-objects -vH
du -sh .git/

# 执行优化
git gc --aggressive --prune=now

# 优化后检查
echo -e "\n=== 优化后 ==="
git count-objects -vH
du -sh .git/
```

### 6. 批量标签与版本管理

```python
# 专业版标签管理
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

## 使用场景

### 场景一:整理提交历史

合并和整理功能分支的提交历史。

```bash
#!/bin/bash
# 整理提交历史
echo "=== 整理提交历史 ==="

# 1. 创建备份
BACKUP_BRANCH="backup/$(date +%Y%m%d%H%M%S)"
git branch "$BACKUP_BRANCH"
echo "备份分支: $BACKUP_BRANCH"

# 2. 交互式变基合并提交
echo "开始交互式变基..."
git rebase -i HEAD~5

# 在编辑器中:
# pick   abc1234 feat: 添加功能A
# fixup  def5678 fix: 修复A的问题
# squash ghi9012 feat: 完善功能A
# pick   jkl3456 feat: 添加功能B

# 3. 如果出问题,回滚
# git rebase --abort
# git reset --hard $BACKUP_BRANCH

echo "历史整理完成"
```

### 场景二:清除历史中的敏感信息

```bash
#!/bin/bash
# 清除敏感信息
echo "=== 清除历史敏感信息 ==="

# 1. 创建备份
BACKUP_BRANCH="backup/$(date +%Y%m%d%H%M%S)"
git branch "$BACKUP_BRANCH"
echo "备份分支: $BACKUP_BRANCH"

# 2. 查找敏感文件
echo "查找历史中的敏感文件..."
git log --all --diff-filter=A --name-only --format="" -- \
    "*.env" "*.pem" "*.key" "*.secret" "credentials*"

# 3. 使用filter-repo清除
# pip install git-filter-repo
git filter-repo --path .env --invert-paths
git filter-repo --path credentials.json --invert-paths

# 4. 强制推送(通知所有协作者)
echo "需要强制推送,请确认:"
echo "  git push --force-with-lease origin --all"
echo "  git push --force-with-lease origin --tags"

# 5. 清理
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

### 场景三:大型项目子模块管理

```bash
#!/bin/bash
# 大型项目子模块管理
echo "=== 子模块批量管理 ==="

# 1. 查看子模块状态
echo "当前子模块:"
git submodule status

# 2. 批量更新子模块
echo -e "\n更新所有子模块..."
git submodule update --init --recursive
git submodule update --remote --merge

# 3. 批量切换子模块分支
echo -e "\n切换子模块到main分支..."
git submodule foreach 'git checkout main'

# 4. 批量提交子模块更新
echo -e "\n检查子模块更新..."
CHANGED=$(git diff --submodule=log | grep "Submodule" | wc -l)
if [ "$CHANGED" -gt 0 ]; then
    echo "有 $CHANGED 个子模块更新"
    git add .
    git commit -m "chore: 更新子模块引用"
else
    echo "无子模块更新"
fi
```

## 快速开始

### 步骤一:配置高级Git

```ini
# ~/.gitconfig - 专业版配置
[user]
    name = 你的名字
    email = your@email.com

[alias]
    # 基础别名
    st = status
    co = checkout
    ci = commit
    lg = log --graph --oneline --all -20

    # 高级别名
    squash = "!f() { git rebase -i HEAD~$1; }; f"
    undo = reset --soft HEAD~1
    redo = reset --hard HEAD@{1}
    amend = commit --amend --no-edit
    cleanup = "!git branch --merged main | grep -v 'main' | xargs git branch -d"
    prune-remote = fetch --prune --all

[rebase]
    autosquash = true
    autoStash = true

[rerere]
    enabled = true
```

### 步骤二:运行高级操作

```
请帮我整理最近5个提交的历史,合并相关的提交。
```

## 配置示例

### 企业级配置

```yaml
# .git-essentials-pro.yml
version: "2.0"
edition: pro

# 历史管理
history:
  safe_rewrite: true
  create_backup: true
  backup_prefix: "backup/"

# 子模块
submodules:
  auto_update: false
  default_branch: main
  recursive: true

# 性能优化
optimization:
  auto_gc: false
  gc_threshold: 500MB
  aggressive_gc: false

# 标签管理
tags:
  format: "v{major}.{minor}.{patch}"
  annotated: true
  auto_push: true

# 变基
rebase:
  autosquash: true
  autostash: true
  safe_mode: true

# bisect
bisect:
  auto_test: true
  test_script: ./bisect-test.sh
```

## 最佳实践

1. **变基前备份**:执行变基前创建备份分支

```bash
git branch backup/$(date +%Y%m%d%H%M%S)
```

2. **使用autosquash**:自动整理fixup提交

```bash
# 创建fixup提交
git commit --fixup HEAD~2

# 自动变基合并
git rebase -i --autosquash HEAD~5
```

3. **定期优化**:定期运行gc优化仓库

```bash
# 每月优化
git gc --aggressive --prune=now
```

4. **安全重写**:重写历史前通知所有协作者

5. **子模块版本固定**:子模块使用特定提交而非分支

## 常见问题

### Q1:专业版如何兼容免费版?

专业版完全兼容免费版的所有Git命令和配置。免费版的别名和配置可直接使用。

### Q2:历史重写有什么风险?

历史重写会改变提交哈希,影响所有协作者。重写后需要:
1. 通知所有协作者
2. 强制推送
3. 协作者重新克隆或reset

### Q3:子模块和 subtree 有什么区别?

| 特性 | 子模块 | subtree |
|:-----|:-------|:--------|
| 独立仓库 | 是 | 否 |
| 克隆复杂度 | 需--recursive | 简单 |
| 更新方式 | submodule update | subtree pull |
| 历史独立性 | 独立 | 合并 |
| 适合场景 | 独立组件 | 紧密集成 |

### Q4:如何安全地清理大文件?

```bash
# 1. 查找大文件
python3 -c "from history_rewriter import HistoryRewriter; print(HistoryRewriter.find_large_files())"

# 2. 创建备份
git branch backup/before-cleanup

# 3. 使用filter-repo清理
git filter-repo --path large-file.bin --invert-paths

# 4. 清理引用
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 5. 强制推送
git push --force-with-lease
```

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Git 2.30+ / Python 3.8+ / Bash

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Git 2.30+ | 运行时 | 必需 | git-scm.com 下载 |
| Python 3.8+ | 运行时 | 推荐 | python.org 下载 |
| git-filter-repo | 工具 | 推荐 | pip install git-filter-repo |
| Bash | 运行时 | 推荐 | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 远程仓库认证配置:

```bash
# SSH认证(推荐)
ssh-keygen -t ed25519 -C "your@email.com"

# HTTPS Token
git config --global credential.helper store
```

### 可用性分类

- **分类**:MD+EXEC+PRO(专业版支持高级变基、历史重写和子模块管理)
- **说明**:企业级Git版本控制工具,支持高级历史管理和性能优化
- **适用规模**:中小型到大型项目
- **兼容性**:完全兼容免费版命令和配置,支持平滑升级
