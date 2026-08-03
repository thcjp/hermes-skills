# GitHub 平台规则文档

> 同步函数: `version_sync_pipeline.sync_to_github` | 注册表: `platform_registry['github']`

## 平台概述

GitHub 作为代码托管平台，用于管理 skill 的版本控制和开源发布。本项目采用双仓库策略：公开仓库(开放库)存放可公开的 skill，私有仓库存放内部工具和配置。

**关键属性**:
- 可变现: 否(代码托管平台)
- 同步函数: `version_sync_pipeline.sync_to_github`
- 适配器模块: 无(GitHub 无独立 adapter)
- 仓库策略: 双仓库(公开 + 私有)
- 分支: 主分支

## 认证要求

### Git 认证
- **SSH Key**: 推荐使用 SSH key 进行 Git 推送
- **HTTPS + Token**: 使用 GitHub Personal Access Token
- **配置文件**: `~/.gitconfig` 或项目 `.git/config`

### 仓库配置
```
来源: config/github_repo_strategy.py
  PUBLIC_REMOTE: 公开仓库远程地址
  PRIVATE_REMOTE: 私有仓库远程地址
  GITHUB_BRANCH: 主分支名
```

## 速率限制

| 参数 | 值 | 说明 |
|------|-----|------|
| cooldown | 3s | Git 操作最小间隔 |
| max_per_hour | 60 | 每小时最大提交数 |
| max_per_day | 无限制 | GitHub API 限制为 5000 req/h |

**注意**: GitHub 速率限制主要针对 API 调用，Git push 操作受 GitHub 服务端限制。

## 预上传检查项

| 检查项 | 阻断级别 | 说明 |
|--------|---------|------|
| dedup | 阻断(fail-safe) | 内容指纹去重 |

**来源**: `pre_upload_checks.run_pre_checks()` + `platform_registry['github'].pre_checks`

**注意**: GitHub 仅检查去重(避免重复内容推送到仓库)，不检查质量门控和安全扫描(代码托管平台无内容审核)。

## 发布流程

```
sync_to_github(slug, skill_md, new_version, changelog, source, skill_id)
  ├─ 1. 确定 skill 目录路径
  ├─ 2. Git add → git add <skill_dir>
  ├─ 3. Git commit → git commit -m "changelog"
  ├─ 4. Git push → git push <remote> <branch>
  │    ├─ 公开仓库: PUBLIC_REMOTE
  │    └─ 私有仓库: PRIVATE_REMOTE(如需)
  ├─ 5. 记录 platform_upload 结果
  └─ 6. 返回同步结果
```

### 同步结果状态
| 状态 | 说明 |
|------|------|
| success | Git push 成功 |
| no_changes | 无需提交的变更(内容未变) |
| failed | Git 操作失败 |
| error | 异常错误 |

### 版本递增规则
版本号采用语义化版本(SemVer)，自动递增 patch 级：
- `1.0.0` → `1.0.1`(patch 级递增)
- 由 `increment_version()` 函数处理
- 每次检测到 SKILL.md 内容变更时自动递增

### 变更检测机制
```
1. 计算 SKILL.md 的 MD5 哈希
2. 与数据库中存储的 hash 对比
3. hash 不同 → 检测到变更 → 触发版本同步
4. hash 相同 → 无变更 → 跳过同步
```

**来源**: `upgrade_checker.compute_content_hash()` + `version_sync_pipeline.scan_changes()`

## 双仓库策略

```
公开仓库(PUBLIC_REMOTE)
  └─ 存放: 可公开的 skill(packaged + opensource + differentiated)
  └─ License: MIT

私有仓库(PRIVATE_REMOTE)
  └─ 存放: 内部工具、配置、数据库
  └─ 不对外公开
```

**来源**: `config/github_repo_strategy.py`

## 常见问题

### Q: Git push 失败(权限拒绝)
A: 检查 SSH key 或 Personal Access Token 是否有效。确保有目标仓库的 push 权限。

### Q: Git push 返回 no_changes
A: SKILL.md 内容未变化，git diff 为空。这是正常行为，表示无需提交的变更。

### Q: 公开仓库和私有仓库有什么区别
A:
- 公开仓库: 存放可公开的 skill，MIT license，面向社区
- 私有仓库: 存放内部工具和配置，不对外公开

### Q: GitHub 同步是否需要速率限制
A: GitHub API 有速率限制(5000 req/h)，但 Git push 操作通常不受影响。本项目仍设置 cooldown=3s 以避免短时间内大量 push。

## 封禁风险点

| 风险 | 严重度 | 描述 | 缓解措施 |
|------|--------|------|---------|
| 重复内容推送 | 低 | 相同内容以不同路径推送 | dedup 预检查 |
| 大文件推送 | 低 | SKILL.md 超过 GitHub 文件大小限制(100MB) | 内容长度检查 |
| 频繁 push | 低 | 短时间大量 push 触发 GitHub 反滥用 | cooldown=3s |

## 与其他平台的差异

| 维度 | SkillHub | ClawHub | Coze | GitHub |
|------|---------|---------|------|--------|
| 变现 | SkillPay | 无 | 70% 分成 | 无 |
| 用途 | Skill 分发 | 开源 Skill 分发 | Plugin 分发 | 版本控制 |
| 速率限制 | 严格(60s/20日) | 宽松(5s/100日) | 预期(10s/50日) | 最宽松(3s/无日限) |
| 内容审核 | WAF + 审核 | 无 | 6类标准 | 无 |
| 发布后流程 | approve→publish→star | 无 | 资格检查 | 无 |
| License | MIT~Proprietary | 仅开源 | 灵活 | MIT(公开仓库) |
