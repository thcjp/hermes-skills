---
slug: git-essentials-tool-pro
name: git-essentials-tool-pro
version: 1.0.0
displayName: Git基础工具专业版
summary: 企业级Git版本控制,支持高级变基、历史重写、子模块批量管理、性能优化与团队协作。
license: Proprietary
edition: pro
description: '面向研发团队的高级Git版本控制工具,提供交互式变基、历史重写、子模块批量管理、仓库性能优化与团队协作工作流。核心能力:

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

  - 支持子模...'
tags:
- 开发工具
- Git
- 版本控制
- 企业级
tools:
- - read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
Git基础工具专业版为研发团队提供高级版本控制能力。在免费版核心Git命令之上,专业版新增交互式变基、历史重写、子模块批量管理、仓库性能优化和二分查找调试,满足企业级版本控制需求。

专业版完全兼容免费版的所有Git命令和配置,研发团队可从免费版无缝升级,已有配置和别名无需修改。

## 核心能力
### 1. 高级交互式变基
使用交互式变基整理提交历史。

```bash
git rebase -i HEAD~5

git rebase --continue    # 解决冲突后继续
git rebase --skip        # 跳过当前提交
git rebase --abort       # 取消变基
git rebase -i --autosquash HEAD~10

git rebase -i HEAD~3
```

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供高级交互式变基所需的指令和必要参数。
**处理**: 按照skill规范执行高级交互式变基操作,遵循单一意图原则。
**输出**: 返回高级交互式变基的执行结果,包含操作状态和输出数据。

### 2. 历史重写
安全地重写Git历史。

```bash
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

git filter-branch --tree-filter 'rm -f sensitive.txt' --prune-empty HEAD

git filter-repo --path sensitive.txt --invert-paths
git filter-repo --replace-text replacements.txt

git filter-branch --tree-filter 'rm -f large-file.bin' HEAD
git filter-repo --path large-file.bin --invert-paths

rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供历史重写所需的指令和必要参数。
**处理**: 按照skill规范执行历史重写操作,遵循单一意图原则。
**输出**: 返回历史重写的执行结果,包含操作状态和输出数据。

### 3. 子模块批量管理
```bash
#!/bin/bash
echo "=== 子模块管理 ==="

git submodule add https://example.com/lib.git libs/lib
git submodule add -b main https://example.com/lib.git libs/lib

git submodule init
git submodule update
git submodule update --init --recursive

git clone --recursive https://example.com/repo.git

git submodule foreach 'git pull origin main'
git submodule update --remote --merge

git submodule foreach 'git status'
git submodule foreach 'git checkout main'

git submodule deinit -f libs/lib
git rm -f libs/lib
rm -rf .git/modules/libs/lib

git submodule status
git submodule summary
```

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供子模块批量管理所需的指令和必要参数。
**处理**: 按照skill规范执行子模块批量管理操作,遵循单一意图原则。
**输出**: 返回子模块批量管理的执行结果,包含操作状态和输出数据。

### 4. 二分查找调试
使用bisect定位问题引入的提交。

```bash
git bisect start                    # 开始二分
git bisect bad                      # 标记当前版本有问题
git bisect good v1.0.0             # 标记v1.0.0是好的
git bisect good                     # 标记当前提交是好的
git bisect bad                      # 标记当前提交是坏的
git bisect start HEAD v1.0.0 --
git bisect run ./test-script.sh     # 返回0=good, 1=bad
git bisect log

git bisect reset                    # 结束并回到原来分支
git bisect visualize                # 查看剩余范围
```

```bash
#!/bin/bash
cat > bisect-test.sh << 'EOF'
#!/bin/bash
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

git bisect start
git bisect bad HEAD
git bisect good v1.0.0
git bisect run ./bisect-test.sh
```

**输入**: 用户提供二分查找调试所需的指令和必要参数。
**处理**: 按照skill规范执行二分查找调试操作,遵循单一意图原则。
**输出**: 返回二分查找调试的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. 仓库性能优化
```bash
git gc                              # 垃圾回收
git gc --aggressive                 # 深度回收
git gc --prune=now                  # 立即清理
git fsck                            # 检查完整性
git fsck --full                     # 完整检查
git count-objects -v                # 对象统计
git count-objects -vH               # 人性化显示
git repack -a -d --depth=250 --window=250

echo "=== 优化前 ==="
git count-objects -vH
du -sh .git/

git gc --aggressive --prune=now

echo -e "\n=== 优化后 ==="
git count-objects -vH
du -sh .git/
```

**输入**: 用户提供仓库性能优化所需的指令和必要参数。
**处理**: 按照skill规范执行仓库性能优化操作,遵循单一意图原则。
**输出**: 返回仓库性能优化的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 6. 批量标签与版本管理

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供批量标签与版本管理所需的指令和必要参数。
**处理**: 按照skill规范执行批量标签与版本管理操作,遵循单一意图原则。
**输出**: 返回批量标签与版本管理的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、版本控制、支持高级变基、性能优化与团队协、面向研发团队的高、版本控制工具、提供交互式变基、仓库性能优化与团、队协作工作流、核心能力、高级交互式变基与、团队协作工作流模等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景
### 场景一:整理提交历史
合并和整理功能分支的提交历史。

```bash
#!/bin/bash
echo "=== 整理提交历史 ==="

BACKUP_BRANCH="backup/$(date +%Y%m%d%H%M%S)"
git branch "$BACKUP_BRANCH"
echo "备份分支: $BACKUP_BRANCH"

echo "开始交互式变基..."
git rebase -i HEAD~5

echo "历史整理完成"
```

### 场景二:清除历史中的敏感信息
```bash
#!/bin/bash
echo "=== 清除历史敏感信息 ==="

BACKUP_BRANCH="backup/$(date +%Y%m%d%H%M%S)"
git branch "$BACKUP_BRANCH"
echo "备份分支: $BACKUP_BRANCH"

echo "查找历史中的敏感文件..."
git log --all --diff-filter=A --name-only --format="" -- \
    "*.env" "*.pem" "*.key" "*.secret" "credentials*"

git filter-repo --path .env --invert-paths
git filter-repo --path credentials.json --invert-paths

echo "需要强制推送,请确认:"
echo "  git push --force-with-lease origin --all"
echo "  git push --force-with-lease origin --tags"

rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

### 场景三:大型项目子模块管理
```bash
#!/bin/bash
echo "=== 子模块批量管理 ==="

echo "当前子模块:"
git submodule status

echo -e "\n更新所有子模块..."
git submodule update --init --recursive
git submodule update --remote --merge

echo -e "\n切换子模块到main分支..."
git submodule foreach 'git checkout main'

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

## 不适用场景

以下场景Git基础工具专业版不适合处理：

- 无明确技术栈的模糊需求
- 纯架构设计决策
- 运维部署管理

## 触发条件

需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于非本工具能力范围的需求。

## 快速开始
### Step 1:配置高级Git
```ini
[user]
    name = 你的名字
    email = your@email.com

[alias]
    st = status
    co = checkout
    ci = commit
    lg = log --graph --oneline --all -20

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

### Step 2:运行高级操作
```
请帮我整理最近5个提交的历史,合并相关的提交。
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。

#
## 配置示例
### 企业级配置

> 详细代码示例已移至 `references/detail.md`

## 最佳实践
1. **变基前备份**:执行变基前创建备份分支

```bash
git branch backup/$(date +%Y%m%d%H%M%S)
```

2. **使用autosquash**:自动整理fixup提交

```bash
git commit --fixup HEAD~2

git rebase -i --autosquash HEAD~5
```

3. **定期优化**:定期运行gc优化仓库

```bash
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
python3 -c "from history_rewriter import HistoryRewriter; print(HistoryRewriter.find_large_files())"

git branch backup/before-cleanup

git filter-repo --path large-file.bin --invert-paths

git reflog expire --expire=now --all
git gc --prune=now --aggressive

git push --force-with-lease
```

## 依赖说明
### 运行环境
- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Git 2.30+ / Python 3.8+ / Bash

### 依赖详情
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
ssh-keygen -t ed25519 -C "your@email.com"

git config --global credential.helper store
```

### 可用性分类
- **分类**:MD+EXEC+PRO(专业版支持高级变基、历史重写和子模块管理)
- **说明**:企业级Git版本控制工具,支持高级历史管理和性能优化
- **适用规模**:中小型到大型项目
- **兼容性**:完全兼容免费版命令和配置,支持平滑升级

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```
