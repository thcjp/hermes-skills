---
slug: git-helper-tool-free
name: git-helper-tool-free
version: "1.0.0"
displayName: Git助手免费版
summary: 提供Git常见操作辅助、冲突解决指引、提交规范检查与安全操作清单,适合开发者日常使用。
license: MIT
edition: free
description: |-
  面向开发者的Git操作辅助工具,提供常见操作指引、冲突解决步骤、提交规范检查与安全操作清单。

  核心能力:
  - 常见Git操作辅助指引
  - 合并冲突解决步骤
  - 提交信息规范检查
  - 安全操作检查清单
  - 常用配置模板

  适用场景:
  - Git操作遇到问题时的辅助
  - 冲突解决指引
  - 提交规范自检
  - 新手Git操作指导

  差异化:
  - 免费版提供操作指引和检查清单,开箱即用
  - 安全优先,避免误操作
  - 与专业版命令兼容,可平滑升级

  触发关键词: Git助手, Git帮助, 冲突解决, 提交规范, 安全检查, git help, git操作, 冲突处理
tags:
- 开发工具
- Git
- 辅助工具
tools:
- read
- exec
---

# Git助手 - 免费版

## 概述

Git助手免费版为开发者提供Git操作辅助能力。工具提供常见操作指引、合并冲突解决步骤、提交信息规范检查和安全操作检查清单,帮助开发者安全高效地使用Git。

本版本适合Git操作遇到问题时的辅助、冲突解决指引和新手Git操作指导。所有指引以步骤化方式呈现,易于跟随。

## 核心能力

### 1. 常见操作辅助

提供常见Git操作的分步指引。

**提交代码:**

```bash
# 步骤1: 查看当前状态
git status

# 步骤2: 查看变更内容
git diff
git diff --staged

# 步骤3: 暂存文件
git add file1.txt file2.txt
# 或全部暂存
git add .

# 步骤4: 提交
git commit -m "feat(scope): 描述"

# 步骤5: 推送
git push
```

**创建功能分支:**

```bash
# 步骤1: 切换到基础分支
git switch main

# 步骤2: 拉取最新代码
git pull

# 步骤3: 创建并切换到功能分支
git switch -c feature/new-feature

# 步骤4: 推送到远程
git push -u origin feature/new-feature
```

**合并分支:**

```bash
# 步骤1: 切换到目标分支
git switch main

# 步骤2: 拉取最新
git pull

# 步骤3: 合并功能分支
git merge feature/new-feature

# 步骤4: 如有冲突,解决冲突
# 步骤5: 提交合并
git commit

# 步骤6: 推送
git push

# 步骤7: 删除功能分支
git branch -d feature/new-feature
```

### 2. 冲突解决指引

```bash
# 冲突解决完整流程

# 步骤1: 查看冲突文件
git diff --name-only --diff-filter=U

# 步骤2: 查看冲突内容
git diff

# 冲突标记说明:
# <<<<<<< HEAD
# 当前分支的代码
# =======
# 合并分支的代码
# >>>>>>> feature-branch

# 步骤3: 手动编辑冲突文件
# - 打开冲突文件
# - 找到 <<<<<<< ======= >>>>>>> 标记
# - 选择保留的代码
# - 删除冲突标记

# 步骤4: 验证无冲突标记
grep -rn "<<<\|>>>\|===" . --include="*.js" --include="*.py"

# 步骤5: 测试代码
npm test  # 或其他测试命令

# 步骤6: 标记已解决
git add resolved-file.txt

# 步骤7: 完成合并
git commit
# 或取消合并
git merge --abort
```

### 3. 提交规范检查

```bash
#!/bin/bash
# 提交信息规范检查
check_commit_message() {
    local msg="$1"
    local errors=()

    # 检查格式
    if ! echo "$msg" | grep -qE '^(feat|fix|docs|style|refactor|test|chore|perf|ci|build)(\(\w+\))?:\s+.+'; then
        errors+=("格式不符合Conventional Commits规范")
        errors+=("正确格式: type(scope): description")
        errors+=("类型: feat|fix|docs|style|refactor|test|chore|perf|ci|build")
    fi

    # 检查首行长度
    local first_line=$(echo "$msg" | head -1)
    if [ ${#first_line} -gt 72 ]; then
        errors+=("首行长度${#first_line}超过72字符")
    fi

    # 检查是否以句号结尾
    if echo "$first_line" | grep -qE '[。.]$'; then
        errors+=("首行不应以句号结尾")
    fi

    # 输出结果
    if [ ${#errors[@]} -eq 0 ]; then
        echo "[OK] 提交信息规范"
        return 0
    else
        echo "[FAIL] 提交信息不规范:"
        for err in "${errors[@]}"; do
            echo "  - $err"
        done
        return 1
    fi
}

# 使用示例
check_commit_message "feat(auth): 添加用户登录功能"
check_commit_message "修复了一个bug"
```

### 4. 安全操作检查

```bash
#!/bin/bash
# Git安全操作检查清单
echo "=== Git安全检查清单 ==="

# 1. 检查当前分支
BRANCH=$(git branch --show-current)
echo "1. 当前分支: $BRANCH"
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
    echo "   [!] 在主分支上,请确认是否要直接操作"
fi

# 2. 检查未提交变更
if [ -n "$(git status --porcelain)" ]; then
    echo "2. [!] 有未提交的变更"
    git status -s
fi

# 3. 检查未推送提交
AHEAD=$(git rev-list --count @{upstream}..HEAD 2>/dev/null)
if [ -n "$AHEAD" ] && [ "$AHEAD" -gt 0 ]; then
    echo "3. [!] 有 $AHEAD 个未推送的提交"
fi

# 4. 检查stash
STASH_COUNT=$(git stash list | wc -l)
if [ "$STASH_COUNT" -gt 0 ]; then
    echo "4. 有 $STASH_COUNT 个stash"
fi

# 5. 检查是否落后远程
BEHIND=$(git rev-list --count HEAD..@{upstream} 2>/dev/null)
if [ -n "$BEHIND" ] && [ "$BEHIND" -gt 0 ]; then
    echo "5. [!] 落后远程 $BEHIND 个提交"
fi

echo ""
echo "=== 安全建议 ==="
echo "- 不要在main分支直接提交"
echo "- 推送前先pull"
echo "- 使用--force-with-lease替代--force"
echo "- 定期清理已合并分支"
```

### 5. 常用配置模板

```bash
# Git全局配置模板
setup_git_config() {
    echo "=== Git配置向导 ==="

    # 用户信息
    read -p "姓名: " name
    read -p "邮箱: " email
    git config --global user.name "$name"
    git config --global user.email "$email"

    # 默认分支
    git config --global init.defaultBranch main

    # 推荐配置
    git config --global pull.rebase true
    git config --global push.default current
    git config --global push.autoSetupRemote true

    # 别名
    git config --global alias.st "status -sb"
    git config --global alias.co checkout
    git config --global alias.sw switch
    git config --global alias.br branch
    git config --global alias.ci commit
    git config --global alias.lg "log --graph --oneline --all -20"

    echo "Git配置完成"
    git config --list --global
}

# .gitignore模板生成
generate_gitignore() {
    local type="${1:-node}"
    echo "=== 生成 .gitignore ($type) ==="

    case "$type" in
        node)
            cat > .gitignore << 'EOF'
node_modules/
dist/
.env
.env.local
*.log
.vscode/
.DS_Store
coverage/
.nyc_output/
EOF
            ;;
        python)
            cat > .gitignore << 'EOF'
__pycache__/
*.pyc
venv/
.venv/
*.egg-info/
dist/
build/
.env
.pytest_cache/
.mypy_cache/
EOF
            ;;
        java)
            cat > .gitignore << 'EOF'
target/
*.class
*.jar
*.war
.idea/
*.iml
.gradle/
build/
EOF
            ;;
        *)
            cat > .gitignore << 'EOF'
*.log
*.tmp
*.bak
.DS_Store
Thumbs.db
.vscode/
.idea/
EOF
            ;;
    esac
    echo ".gitignore 已生成"
}
```

## 使用场景

### 场景一:解决合并冲突

遇到合并冲突时获取解决指引。

```bash
#!/bin/bash
# 冲突解决助手
echo "=== 合并冲突解决助手 ==="

# 1. 检查是否有冲突
CONFLICTS=$(git diff --name-only --diff-filter=U 2>/dev/null)
if [ -z "$CONFLICTS" ]; then
    echo "没有冲突文件"
    exit 0
fi

echo "发现冲突文件:"
echo "$CONFLICTS" | while read f; do
    echo "  - $f"
done

# 2. 显示冲突详情
echo -e "\n冲突详情:"
for f in $CONFLICTS; do
    echo "--- $f ---"
    grep -n "<<<<<<<\|=======\|>>>>>>>" "$f" 2>/dev/null
done

# 3. 解决指引
echo -e "\n解决步骤:"
echo "1. 打开冲突文件"
echo "2. 找到 <<<<<<< ======= >>>>>>> 标记"
echo "3. 选择保留的代码,删除标记"
echo "4. git add <file>"
echo "5. git commit"

# 4. 检查是否还有冲突标记
echo -e "\n冲突标记检查:"
for f in $CONFLICTS; do
    if grep -q "<<<<<<<\|>>>>>>>" "$f" 2>/dev/null; then
        echo "  [!] $f 仍有冲突标记"
    fi
done
```

### 场景二:提交前检查

提交前进行安全检查。

```bash
#!/bin/bash
# 提交前检查
echo "=== 提交前检查 ==="

# 1. 检查分支
BRANCH=$(git branch --show-current)
echo "当前分支: $BRANCH"

if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
    echo "[!] 警告: 在 $BRANCH 分支上"
    read -p "确认在 $BRANCH 上提交? (y/N) " confirm
    [ "$confirm" != "y" ] && exit 1
fi

# 2. 检查调试代码
echo -e "\n检查调试代码..."
DEBUG=$(git diff --cached --name-only | xargs grep -l "console.log\|debugger\|print(" 2>/dev/null)
if [ -n "$DEBUG" ]; then
    echo "[!] 发现调试代码:"
    echo "$DEBUG"
fi

# 3. 检查敏感信息
echo -e "\n检查敏感信息..."
SECRET=$(git diff --cached | grep -iE "(password|secret|api_key)\s*=\s*['\"]" 2>/dev/null)
if [ -n "$SECRET" ]; then
    echo "[!] 发现敏感信息"
    exit 1
fi

# 4. 检查大文件
echo -e "\n检查大文件..."
LARGE=$(git diff --cached --name-only | xargs -I{} sh -c 'test -f "{}" && wc -c "{}"' 2>/dev/null | awk '$1>1048576{print $2}')
if [ -n "$LARGE" ]; then
    echo "[!] 发现大文件(>1MB):"
    echo "$LARGE"
fi

echo -e "\n[OK] 检查通过"
```

### 场景三:误操作恢复

```bash
#!/bin/bash
# 误操作恢复助手
echo "=== Git误操作恢复 ==="

echo "选择恢复场景:"
echo "1. 撤销最近的提交(保留变更)"
echo "2. 撤销最近的提交(丢弃变更)"
echo "3. 恢复误删除的分支"
echo "4. 恢复误reset的提交"
echo "5. 撤销已推送的提交"
read -p "选择(1-5): " choice

case $choice in
    1)
        echo "撤销提交,保留变更..."
        git reset --soft HEAD~1
        echo "变更已保留在工作区"
        ;;
    2)
        echo "撤销提交,丢弃变更..."
        read -p "确认丢弃所有变更? (y/N) " confirm
        [ "$confirm" = "y" ] && git reset --hard HEAD~1
        ;;
    3)
        echo "查找误删除的分支..."
        git reflog | grep "checkout\|branch"
        echo "找到SHA后: git checkout -b branch-name <sha>"
        ;;
    4)
        echo "查找误reset的提交..."
        git reflog | grep "reset"
        echo "找到SHA后: git reset --hard <sha>"
        ;;
    5)
        echo "撤销已推送的提交(安全方式)..."
        echo "1. git revert <commit-sha>"
        echo "2. git push origin <branch>"
        ;;
esac
```

## 快速开始

### 步骤一:获取帮助

在 AI Agent 中输入:

```
我遇到了Git合并冲突,请帮我解决。
```

### 步骤二:按照指引操作

Agent 会提供步骤化的解决指引。

### 步骤三:安全检查

操作完成后进行安全检查确认。

## 配置示例

### Git助手配置

```yaml
# .git-helper.yml
version: "1.0"

# 安全检查
safety:
  block_main_push: true
  check_debug_code: true
  check_secrets: true
  check_large_files: true
  max_file_size: 1MB

# 提交规范
commit:
  conventional: true
  max_subject: 72
  types: [feat, fix, docs, style, refactor, test, chore]

# 冲突解决
conflict:
  auto_detect: true
  check_markers: true
  suggest_resolution: true

# 恢复操作
recovery:
  show_reflog: true
  safe_mode: true
```

## 最佳实践

1. **操作前检查**:每次Git操作前运行安全检查

2. **规范提交**:遵循Conventional Commits规范

```bash
# 正确
git commit -m "feat(auth): 添加用户登录功能"

# 错误
git commit -m "update"
```

3. **安全推送**:使用 `--force-with-lease`

4. **及时清理**:定期清理已合并分支和stash

5. **保留reflog**:不要清理reflog,它是恢复的保障

## 常见问题

### Q1:如何查看Git命令帮助?

```bash
# 查看命令帮助
git help <command>
git <command> --help
git <command> -h    # 简短帮助

# 示例
git help commit
git merge --help
```

### Q2:如何配置Git补全?

```bash
# Bash补全
# 下载git-completion.bash
source ~/.git-completion.bash

# Zsh补全
# 在~/.zshrc中添加
autoload -Uz compinit && compinit
```

### Q3:免费版与专业版有何区别?

| 能力维度 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 操作指引 | 基础指引 | 智能向导 |
| 冲突解决 | 手动指引 | 自动分析 |
| 安全检查 | 基础检查 | 深度审计 |
| 恢复操作 | 手动恢复 | 自动恢复 |
| 批量操作 | 不支持 | 批量处理 |
| 诊断 | 基础 | 深度诊断 |

### Q4:如何查看Git配置?

```bash
# 查看所有配置
git config --list

# 查看全局配置
git config --list --global

# 查看特定配置
git config user.name
git config user.email
```

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Git 2.20+ / Bash

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Git | 运行时 | 必需 | git-scm.com 下载 |
| Bash | 运行时 | 推荐 | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 远程仓库认证:

```bash
git config --global credential.helper store
```

### 可用性分类

- **分类**:MD+EXEC(纯 Markdown 指令,需要 exec 命令行执行能力)
- **说明**:基于 Markdown 的 AI Skill,通过自然语言指令驱动 Agent 提供Git辅助
- **适用规模**:个人开发者日常使用
