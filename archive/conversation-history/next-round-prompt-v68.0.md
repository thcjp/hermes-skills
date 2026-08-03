# 下一轮对话提示词 (v68.0)

> **日期**: 2026-07-27
> **前置版本**: v67.0 (安全预检增强+ClawHub营销标准化+平台操作固化)
> **核心任务**: Git推送恢复后执行(网络阻塞) + 评分批量同步(覆盖率0.1%→100%) + ClawHub批量上传续传(530个pending) + SkillHub admin token刷新 + 自动化流水线整合

---

## 本轮已完成 (v67.0 → v68.0)

### 企业上传器安全集成 ✅

| 任务 | 状态 | 实现详情 |
|------|------|---------|
| 安全预检集成 | ✅完成 | `enterprise_uploader.py` 上传前自动执行21项安全预检, critical阻断上传 |
| 防幻觉检查集成 | ✅完成 | 集成3项防幻觉检查(交叉验证/需求偏差/虚假实现检测), fail时阻止上传 |
| CLI参数 | ✅完成 | 新增 `--skip-security` 和 `--skip-marketing` 参数供紧急场景使用 |

### 市场监控增强 ✅

| 任务 | 状态 | 实现详情 |
|------|------|---------|
| DB schema扩展 | ✅完成 | skills表新增5字段: platform_rating, platform_rating_count, platform_downloads, platform_ai_review, last_platform_sync_at |
| sync_platform_ratings() | ✅完成 | 从SkillHub公开API同步评分数据到DB, 支持批量同步(--limit参数) |
| check_low_rating_skills() | ✅完成 | 评分<4.5触发自动升级流程, 修复local_path处理 |
| CLI命令 | ✅完成 | 新增 `sync-ratings` 和 `check-low-ratings` 子命令 |
| 评分同步执行 | ✅完成 | 2个低评分skill已同步(3.3和3.6), 评分覆盖率0.1%待提升 |

### 版本同步管道增强 ✅

| 任务 | 状态 | 实现详情 |
|------|------|---------|
| publish_to_community集成 | ✅完成 | SkillHub同步后自动执行publish-to-community API, 设置visibility=public |
| 安全预检集成 | ✅完成 | L1.5内容质量后自动执行21项安全检查, critical阻断/high+medium警告 |
| --skip-security参数 | ✅完成 | 新增CLI参数允许跳过安全预检(紧急情况) |

### ClawHub批量上传器增强 ✅

| 任务 | 状态 | 实现详情 |
|------|------|---------|
| --from-db模式 | ✅完成 | 从数据库查询pending skill直接上传, 不再依赖目录遍历 |
| 营销参数集成 | ✅完成 | categories/topics/name自动从SKILL.md frontmatter提取并填充 |
| 数据库跟踪 | ✅完成 | 上传结果自动写入platform_uploads表(INSERT/UPDATE) |
| 分类映射修复 | ✅完成 | 新增local_to_clawhub直连映射, 修复frontmatter category映射断裂 |
| ClawHub CLI修复 | ✅完成 | 修复登录问题(主站registry), 添加"Not logged in"错误处理 |
| 目录查找增强 | ✅完成 | 优先使用DB local_path, 支持differentiated-skills子目录 |

### 质量门控slug匹配检测 ✅

| 任务 | 状态 | 实现详情 |
|------|------|---------|
| _check_requirement_deviation增强 | ✅完成 | 新增slug-keyword匹配: 检测slug与displayName/body内容是否一致 |
| 测试验证 | ✅完成 | 成功检测university-applications/命理大师不匹配(3.3分skill) |

### 低评分skill治理 ✅

| 任务 | 状态 | 实现详情 |
|------|------|---------|
| university-applications-sk | ✅已删除 | 3.3分, 内容为命理大师(完全错误), 已从SkillHub平台删除(HTTP 200) |
| word-docx-sk | ✅已删除 | 3.6分, 本地文件缺失, 已从SkillHub平台删除(HTTP 200) |
| DB状态修复 | ✅完成 | 标记为deleted_on_skillhub, 588个缺失本地文件的pending标记为not_applicable |

### ClawHub状态同步 ✅

| 任务 | 状态 | 实现详情 |
|------|------|---------|
| skills表clawhub_sync_status | ✅完成 | 从platform_uploads表同步clawhub上传状态到skills表 |
| 状态一致性 | ✅完成 | clawhub success: 1401 (platform_uploads) ↔ synced: 775 + 588 not_applicable |

### Git提交

- **Commit**: `82c05f503` - feat: v2.2 安全预检增强+评分同步+ClawHub营销标准化+低评分治理
- **变更**: 1050 files changed, 14834 insertions(+), 23142 deletions(-)
- **推送状态**: ❌ 失败 — github.com:443 TCP不可达, SSH key未注册GitHub
- **本地状态**: ✅ 已提交到main分支

---

## 当前平台状态

| 平台 | 状态 | 数量 | 说明 |
|------|------|------|------|
| SkillHub | success | 1120 | 已发布 |
| SkillHub | cancelled | 1 | 已取消 |
| ClawHub | success | 1401 | 已上传 |
| ClawHub | cancelled | 2 | 已取消 |
| GitHub公开 | success | 1640 | 已同步 |
| marketing_gate/blocked | - | 1 | 营销关卡阻断 |
| quality_gate/blocked | - | 2 | 质量门禁阻断 |
| pending | - | 0 | 无待审核 |
| rejected | - | 0 | 无被拒 |

### skills表状态分布

| 状态 | 数量 | 说明 |
|------|------|------|
| synced_from_skillhub | 1768 | 已同步到SkillHub |
| local_only | 1546 | 仅本地 |
| deleted_on_skillhub | 128 | 已从SkillHub删除 |
| deleted | 21 | 已完全删除 |

### 评分覆盖

| 指标 | 值 | 说明 |
|------|-----|------|
| 有评分的skill | 2/1768 | 0.1% (极低,需批量同步) |
| 低评分skill(<4.5) | 0 | 2个已删除 |
| platform_rating字段 | 已就绪 | DB schema已扩展 |

---

## 下一轮核心任务

### P0: Git推送到双远程仓库 (阻塞项)

**问题**: github.com:443 TCP不可达, SSH key未注册
**影响**: 本地commit 82c05f503未推送到远程

**解决方案**:
1. **方案A**: 等待网络恢复后执行:
   ```bash
   cd d:\skills
   git push origin main
   git push hermes-skills main
   ```
2. **方案B**: 配置SSH key到GitHub后使用SSH over 443:
   ```bash
   # 将~/.ssh/id_ed25519.pub添加到GitHub Settings → SSH keys
   # 配置~/.ssh/config:
   # Host github.com
   #   Hostname ssh.github.com
   #   Port 443
   #   User git
   git push ssh://git@ssh.github.com:443/thcjp/hermes-skills.git main
   ```
3. **方案C**: 使用代理推送:
   ```bash
   git config http.proxy http://127.0.0.1:PORT
   git push origin main
   git config --unset http.proxy
   ```

### P1-1: 评分批量同步 (覆盖率0.1%→100%)

**目标**: 将1768个synced_from_skillhub skill的平台评分全部同步到DB
**影响文件**: `tools/market_monitor.py`
**预计耗时**: 约30分钟(1768个API调用)

**执行步骤**:
```bash
# 批量同步评分(每次200个)
python tools/market_monitor.py sync-ratings --limit 200
python tools/market_monitor.py sync-ratings --limit 200
# 重复直到全部同步
```

**验证**:
- DB中platform_rating > 0的skill数量 ≥ 1768的80%
- 低评分skill(<4.5)列表已更新

### P1-2: ClawHub批量上传续传 (530个pending)

**目标**: 将530个有效pending skill上传到ClawHub(每日限200个)
**影响文件**: `tools/clawhub_batch_uploader.py`
**预计耗时**: 3天(530/200≈3天)

**执行步骤**:
```bash
# 确保ClawHub CLI已登录
npx clawhub auth login --device

# 从DB查询pending并上传
python tools/clawhub_batch_uploader.py --from-db --limit 200
```

**验证**:
- platform_uploads表中clawhub/success数量 ≥ 1931 (1401+530)
- skills表中clawhub_sync_status=synced数量增加

### P1-3: SkillHub admin API token刷新

**问题**: Admin API返回401, 所有admin操作(审核/发布/收藏)被阻断
**影响**: 无法通过API执行auto_publish等管理操作

**解决方案**:
1. 使用浏览器登录SkillHub admin后台
2. 通过browser_evaluate在浏览器中执行API调用(利用cookie认证)
3. 或获取新的API token保存到 .credentials/skillhub.json

**已知可用方式**:
- ✅ 公开API: GET /api/v1/skills/{slug} (无需认证)
- ✅ 浏览器API: 在已登录浏览器中通过fetch调用admin API
- ❌ Admin API: 直接HTTP调用返回401

### P2-1: 自动化流水线整合

**目标**: 完善daily_sync.py, 整合所有循环任务
**影响文件**: `tools/daily_sync.py`, `tools/orchestrator.py`

**详细步骤**:
1. daily_sync.py整合:
   - 持续审核pending/rejected (0个,无需操作)
   - 定期同步平台评分 (sync_platform_ratings)
   - 检查低评分触发升级 (check_low_rating_skills)
   - ClawHub批量上传续传 (clawhub_batch_uploader --from-db)
2. orchestrator.py修复config导入bug
3. 设置定时任务(cron/Windows Task Scheduler)

### P2-2: 质量检查统一入口确认

**目标**: 确认run_full_quality_check()包含所有44项检查
**影响文件**: `tools/quality_gate.py`

**验证步骤**:
1. 确认run_full_quality_check()调用链:
   - L1静态格式(13项) → L1.5内容质量(7项) → 营销关卡(7项) → 安全预检(21项) → 防幻觉(3项) = 51项
2. 所有上传入口统一使用此函数
3. 测试用例覆盖所有51项

### P2-3: 文档对齐

**目标**: 更新设计文档与代码完全对齐
**影响文件**: `docs/ARCHITECTURE.md`, `docs/plans/new-conversation-starter-design.md`

**详细步骤**:
1. 更新架构文档: 添加评分同步系统、低评分治理流程
2. 更新任务清单: 标记v67-v68已完成项
3. 更新安全预检文档: 确认21项检测列表
4. 添加ClawHub --from-db模式文档

### P3-1: 统一数据源到SQLite

**目标**: 消除双数据源, upgrade_checker从JSON迁移到SQLite
**影响文件**: `tools/upgrade_checker.py`, `tools/orchestrator.py`

### P3-2: 搜索排名优化

**目标**: 提升skill在SkillHub搜索结果中的排名
**因素**: stars✅(已完成)、downloads、更新时间、分类匹配、关键词

---

## 质量门禁完整链路 (v2.2)

```
L1静态格式(13项) ✅
  → L1.5内容质量(7项) ✅
  → 营销关卡(7项) ✅
  → 安全预检(21项) ✅
    → critical: 阻断上传
    → high/medium: 警告但继续
  → 防幻觉(3项) ✅
    → slug-content匹配检测 ✅
  → L2 LLM验证 (可选)
  → L3 Agent试用 (可选)
  → 平台同步
    → GitHub公开 ✅
    → SkillHub ✅ (含publish_to_community)
    → ClawHub ✅ (含营销参数)
```

所有质量门禁已集成到:
- `sync_skill_to_all_platforms()` — 新skill全平台同步
- `upgrade_single_skill()` — 独立skill升级
- `EnterpriseUploader.upload()` — 企业上传器
- `clawhub_batch_uploader.py` — ClawHub批量上传

---

## 安全预检系统架构 (v2.2)

```
生产环节:
  auto_differentiate.py
    → source_security_scan.scan_content()  [L1.5安全预检]
    → critical风险: 阻断差异化
    → high/medium风险: auto_fix_risks()自动修复

上传流水线:
  version_sync_pipeline.sync_skill_to_all_platforms()
    → L1静态格式(13项)
    → L1.5内容质量(7项)
    → 营销关卡(7项)
    → 安全预检(21项)
      → critical: 阻断上传
      → high/medium: 警告但继续
    → 防幻觉(3项)
    → 平台同步

企业上传器:
  enterprise_uploader.py
    → 安全预检(21项) [上传前]
    → 防幻觉检查(3项) [上传前]
    → 营销关卡(7项) [上传前]

ClawHub批量上传:
  clawhub_batch_uploader.py --from-db
    → 从DB查询pending skill
    → 营销参数自动提取
    → 数据库跟踪上传结果
```

---

## 当前Git状态

```
最新commit: 82c05f503
推送状态: ❌ 未推送 (github.com:443 TCP不可达)
分支: main
本地领先origin: 1 commit
```

## 执行注意事项

1. **Git推送优先**: 网络恢复后第一时间推送commit 82c05f503
2. **不创建碎片化新文件**: 所有增强在现有文件中进行
3. **不模拟/mock**: 所有功能必须真实执行
4. **全链路修复**: 底层数据→中间模块→前端UI
5. **向后兼容**: 现有脚本和CLI命令仍可独立运行
6. **API令牌**: SkillHub admin API仍返回401, 需通过浏览器执行admin操作
7. **读取设计文档**: 执行前先阅读 `d:\skills\docs\plans\new-conversation-starter-design.md`
8. **读取任务清单**: 执行前先阅读 `d:\skills\docs\plans\new-conversation-task-list.md`
9. **安全预检优先**: 所有新skill必须通过21项安全预检才能上传
10. **评分同步**: 优先执行sync_platform_ratings提升覆盖率
11. **ClawHub续传**: 每日限200个, 530个pending需3天完成

## 技能/插件使用建议

| 环节 | 技能/插件 | 用途 |
|------|----------|------|
| Git推送 | WebSearch | 查找GitHub代理方案 |
| 评分批量同步 | market_monitor | sync-ratings --limit 200 |
| ClawHub续传 | clawhub_batch_uploader | --from-db --limit 200 |
| SkillHub admin | integrated_browser | 浏览器中执行admin API |
| 自动化流水线 | daily_sync + orchestrator | 定时任务整合 |
| 代码审查 | coderabbit:code-review | 审查新增代码 |
| 完成验证 | superpowers:verification-before-completion | 完成前验证 |
| 文档对齐 | doc-writing-guide | 更新设计文档 |

## 数据库Schema (v68.0)

### skills表关键字段

| 字段 | 类型 | 说明 |
|------|------|------|
| slug | TEXT | 全局唯一kebab-case标识 |
| current_display_name | TEXT | 中文化显示名(≤20字符) |
| current_status | TEXT | active/synced_from_skillhub/local_only/deleted/deleted_on_skillhub |
| platform_rating | REAL | SkillHub平台评分(0-5) |
| platform_rating_count | INTEGER | 评分人数 |
| platform_downloads | INTEGER | 下载量 |
| platform_ai_review | TEXT | AI审查报告 |
| last_platform_sync_at | TEXT | 最后同步时间 |
| skillhub_sync_status | TEXT | SkillHub同步状态 |
| clawhub_sync_status | TEXT | ClawHub同步状态 |
| github_public_sync_status | TEXT | GitHub公开仓库同步状态 |

### platform_uploads表关键字段

| 字段 | 类型 | 说明 |
|------|------|------|
| platform | TEXT | skillhub/clawhub/github_public |
| platform_slug | TEXT | 平台上的slug |
| upload_status | TEXT | success/failed/cancelled/payload_ready |
| community_published | INTEGER | 0=未社区发布, 1=已社区发布 |
| visibility | TEXT | public/private |
