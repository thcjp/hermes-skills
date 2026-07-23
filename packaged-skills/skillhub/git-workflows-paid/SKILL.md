---
slug: "git-workflows-paid"
name: "git-workflows-paid"
version: "1.0.0"
displayName: "Git高级操作专业版"
summary: "企业级 Git 进阶方案，支持子树子模块、稀疏检出、大型单体仓库与冲突自动记忆。"
license: "Proprietary"
edition: "pro"
description: |-
  面向企业级研发团队的 Git 进阶操作专业工具。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务.
tags:
  - 开发工具
  - 版本控制
  - Git进阶
  - 企业架构
  - Monorepo
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Git高级操作专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 免费版 | 专业版新增 |
|:-----|:-----|:-----|
| 交互式变基 | 完整支持 | 自动化变基策略 + 团队规范 |
| 二分查找 | 手动 + 脚本 | 批量缺陷定位 + 构建跳过策略 |
| 工作树 | 基础创建/删除 | 工作树批量管理与代码审查工作流 |
| 冲突解决 | 手动解决 | rerere 自动记忆 + 三方对比 |
| 仓库管理 | - | 子树/子模块完整方案 |
| 大仓库优化 | - | 稀疏检出 + 部分克隆 |
| 批量操作 | - | 批量樱桃挑选 + 跨仓库迁移 |
| 代码考古 | 基础 log/blame | 深度 blame 分析 + pickaxe 搜索 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 交互式变基

针对交互式变基,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供交互式变基相关的配置参数、输入数据和处理选项.
**输出**: 返回交互式变基的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`交互式变基`的配置文档进行参数调优
### 二分查找

针对二分查找,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供二分查找相关的配置参数、输入数据和处理选项.
**输出**: 返回二分查找的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`二分查找`的配置文档进行参数调优
#
## 适用场景

### 场景一：大型单体仓库稀疏检出

团队维护一个大型单体仓库，开发者只需要关注自己负责的模块.
```text
用户：我们的 monorepo 太大了，每次克隆都很慢，怎么优化
# ...
助手：使用稀疏检出 + 部分克隆
# ...
1. 部分克隆（不下载完整历史）
   git clone --filter=blob:none --sparse https://repo.example.com/monorepo.git
   cd monorepo
# ...
2. 设置需要检出的目录
   git sparse-checkout set packages/my-service packages/shared-lib
# ...
3. 添加额外需要的目录
   git sparse-checkout add packages/another-lib
# ...
4. 查看当前稀疏检出配置
   git sparse-checkout list
# ...
5. 如需检出全部
   git sparse-checkout disable
# ...
6. 另一种方式：无检出克隆
   git clone --no-checkout https://repo.example.com/monorepo.git
   cd monorepo
   git sparse-checkout set packages/my-service
   git checkout main
```

### 场景二：子树与子模块管理共享代码

团队有多个项目需要共享一个公共库，需要选择合适的管理策略.
```bash
# ============ 子树方案（推荐：代码直接嵌入）============
# ...
# 添加子树
git subtree add --prefix=lib/shared https://repo.example.com/shared-lib.git main --squash
# ...
# 拉取子树更新
git subtree pull --prefix=lib/shared https://repo.example.com/shared-lib.git main --squash
# ...
# 推送子树修改
git subtree push --prefix=lib/shared https://repo.example.com/shared-lib.git main
# ...
# 拆分子树为独立分支
git subtree split --prefix=lib/shared -b shared-lib-standalone
# ...
# ============ 子模块方案（指针引用）============
# ...
# 添加子模块
git submodule add https://repo.example.com/shared-lib.git lib/shared
# ...
# 克隆含子模块的仓库
git clone --recurse-submodules https://repo.example.com/main-repo.git
# ...
# 初始化已有仓库的子模块
git submodule update --init --recursive
# ...
# 更新子模块到最新
git submodule update --remote
# ...
# 删除子模块
git rm lib/shared
rm -rf .git/modules/lib/shared
```

**子树 vs 子模块选择策略**：

| 特性 | 子树（subtree） | 子模块（submodule） |
|---:|---:|---:|
| 代码存储 | 直接嵌入仓库 | 指针引用外部仓库 |
| 克隆体验 | 开箱即用 | 需额外初始化命令 |
| 仓库体积 | 较大 | 较小 |
| 独立性 | 弱 | 强 |
| 适用场景 | 共享库、第三方代码 | 大依赖、独立发布周期 |
| 协作复杂度 | 低 | 高 |

### 场景三：冲突自动记忆与批量解决

团队频繁遇到相同冲突，需要自动化冲突解决流程.
```bash
# 1. 全局启用 rerere（冲突自动记忆）
git config --global rerere.enabled true
# ...
# 2. 首次解决冲突时 Git 自动记录方案
git merge feature/complex
# 出现冲突...
# 手动解决...
git add .
git commit
# Git 输出: Recorded resolution for 'path/to/file.ts'
# ...
# 3. 再次遇到相同冲突时自动应用
git merge another-feature
# Git 输出: Resolved 'path/to/file.ts' using previous resolution
# ...
# 4. 查看 rerere 状态
git rerere diff
ls .git/rr-cache/
# ...
# 5. 忘记指定文件的方案
git rerere forget path/to/file.ts
# ...
# 6. 三方对比解决复杂冲突
git show :1:path/to/file.ts   # 共同祖先版本
git show :2:path/to/file.ts   # 当前分支版本（ours）
git show :3:path/to/file.ts   # 合并分支版本（theirs）
# ...
# 7. 批量采用某一方的版本
git checkout --ours path/to/file.ts    # 采用当前版本
git checkout --theirs path/to/file.ts  # 采用合并版本
git add path/to/file.ts
```

## 使用流程

### 企业级 Git 配置

```bash
# 启用冲突自动记忆
git config --global rerere.enabled true
# ...
# 启用部分克隆支持
git config --global feature.experimental true
# ...
# 配置合并工具
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'
# ...
# 配置 fetch 时自动清理
git config --global fetch.prune true
# ...
# 配置 diff 算法
git config --global diff.algorithm patience
# ...
# 配置合并策略
git config --global merge.conflictstyle diff3
```

### 子模块批量管理脚本

```bash
# 批量更新所有子模块
git submodule foreach 'git pull origin main'
# ...
# 批量查看子模块状态
git submodule status
# ...
# 批量初始化并更新
git submodule update --init --recursive
# ...
# 批量切换子模块分支
git submodule foreach 'git checkout main'
# ...
# 批量拉取子模块最新代码
git submodule update --remote --merge
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | git-workflows处理的内容输入 |, 默认: 全部维度 |
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
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Git 版本**: 建议 2.25 及以上（需支持 sparse-checkout cone 模式、partial clone）

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| Git | 命令行工具 | 必需 | 系统包管理器安装 |
| git-subtree | 内置工具 | 可选 | Git 2.7+ 内置 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令驱动，无需额外 API Key
- 子模块和子树操作需要对应仓库的访问权限（SSH Key 或令牌）

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 执行 Git 高级操作，专业版功能依赖较新版本的 Git 和命令行执行能力

## 案例展示

### 稀疏检出配置文件

```bash
# 锥形模式（推荐：按目录匹配）
git sparse-checkout init --cone
git sparse-checkout set packages/web packages/api packages/shared
# ...
# 非锥形模式（按模式匹配）
# .git/info/sparse-checkout 文件内容：
# packages/web/*
# packages/api/*
# docs/*.md
```

### 暂存高级模式

```bash
# 部分文件暂存
git stash push -m "WIP: 重构认证流程" -- src/auth.ts src/login.ts
# ...
# 包含未追踪文件
git stash push -u -m "包含新文件"
# ...
# 查看暂存内容
git stash show -p stash@{0}
# ...
# 从暂存创建分支
git stash branch new-feature stash@{0}
# ...
# 交互式暂存
git stash push -p
```

### blame 与代码考古

```bash
# 查看文件每行最后修改者
git blame src/auth.ts
# ...
# 指定行范围
git blame -L 50,70 src/auth.ts
# ...
# 忽略空白差异
git blame -w src/auth.ts
# ...
# 检测代码移动
git blame -M src/auth.ts
# ...
# 检测跨文件移动
git blame -C src/auth.ts
# ...
# 查找字符串添加/删除的提交
git log -S "function oldName" --oneline
git log -G "详情见说明.*hack" --oneline
# ...
# 查看文件完整历史（含重命名）
git log --follow --oneline -- src/auth.ts
# ...
# 查看提交的文件变更统计
git log --stat --oneline -20
```

## 常见问题

### Q1：稀疏检出后如何添加新目录？

```bash
git sparse-checkout add packages/new-module
```

### Q2：子模块更新后其他成员如何同步？

```bash
# 拉取子模块指针变更
git pull origin main
# ...
# 同步子模块到指针指向的提交
git submodule update --init --recursive
```

### Q3：rerere 记录了错误的解决方案怎么办？

```bash
# 忘记指定文件的方案
git rerere forget path/to/file.ts
# ...
# 清除所有记忆
rm -rf .git/rr-cache/
```

### Q4：如何将一个目录拆分为独立仓库？

```bash
# 使用子树拆分
git subtree split --prefix=lib/shared -b shared-standalone
# ...
# 推送到新仓库
git push https://repo.example.com/new-repo.git shared-standalone:main
```

### Q5：部分克隆后如何获取完整历史？

```bash
# 获取指定文件的历史
git fetch --filter=blob:none origin
# ...
# 或完全取消过滤
git config --unset remote.origin.partialclonefilter
git fetch --unshallow
```

### Q6：如何批量樱桃挑选一系列提交？

```bash
# 挑选连续范围
git cherry-pick abc123..ghi789
# ...
# 挑选多个不连续提交
git cherry-pick abc123 def456 ghi789
# ...
# 跨仓库挑选
git remote add upstream https://repo.example.com/other.git
git fetch upstream
git cherry-pick upstream/main~3
```

### Q7：如何查看子模块的具体提交？

```bash
# 查看子模块指针
git ls-tree HEAD lib/shared
# ...
# 查看子模块差异
git diff --submodule
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

