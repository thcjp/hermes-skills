# Round 28 完成报告 & Round 29 计划

## Round 28 完成报告

### 核心成果：本地主数据库架构升级

**问题诊断**: 旧版 `upload_tracking.json` 仅记录 `uploaded: true/false`，完全不跟踪平台审核状态，导致每轮都需反复查询平台。这违背了"本地数据为唯一权威源"的原则。

**解决方案**: 重建为 Schema v2.0，覆盖全生命周期 + 双平台状态：

```
生命周期: discovered → produced → tested → uploaded → published → deprecated → deleted
                    ↑ 生产环节 ↑                    ↑ 上传运营环节 ↑
```

每个skill记录包含:
- **lifecycle**: 生命周期阶段
- **is_free / pricing_model / pair_slug**: 商业属性（免费/付费/配对关系）
- **skillhub**: uploaded, review_status (approved/rejected/platform_review/admin_review/not_uploaded/deleted), reviewed_at, last_sync
- **clawhub**: upload_eligible, uploaded, status (published/not_uploaded/not_eligible/withdrawn), last_sync
- **quality**: last_audit, status, issues
- **source_path / category**: 本地源路径和分类

### 1. SkillHub后台清理 ✓

| 操作 | 数量 | 说明 |
|------|------|------|
| 批量审核通过 | 147 | admin_review → approved |
| 批量删除 | 105 | 重复(-2后缀)和测试skill (test-*, trunc-*, waf-test-*) |
| 剩余admin_review | 1 | jira-pat-toolkit (API返回400，状态异常) |

**操作方式**: 通过 `POST /api/v1/orgs/862/admin/skills/{slug}/approve` 和 `DELETE /api/v1/orgs/862/admin/skills/{slug}` API

### 2. 本地数据库重建 ✓

| 维度 | 数量 |
|------|------|
| 总skill数 | 2083 |
| 本地packaged | 983 |
| 本地differentiated | 1100 |
| 免费版 | 759 |
| 付费版 | 1324 |

**SkillHub状态分布**:
| 状态 | 数量 |
|------|------|
| approved | 2032 |
| platform_review | 17 (本地) + 41 (非本地) |
| rejected | 29 |
| admin_review | 1 |
| not_uploaded | 4 |

**ClawHub状态分布**:
| 状态 | 数量 |
|------|------|
| published | 227 |
| not_uploaded (免费版待传) | 704 |
| not_eligible (付费版不可传) | 1152 |
| withdrawn | 0 |
| ⚠ 付费版已在ClawHub | 172 (需撤回) |

### 3. 平台运维工具创建 ✓

`platform_ops.py` 支持以下命令:
- `status` - 查看数据库状态概览
- `pending` - 列出所有待处理操作
- `skillhub-actions` - 生成SkillHub操作清单
- `clawhub-actions` - 生成ClawHub操作清单
- `mark-approved <slug>` - 标记SkillHub已审核
- `mark-deleted <slug>` - 标记SkillHub已删除
- `mark-clawhub-published <slug>` - 标记ClawHub已发布
- `mark-clawhub-withdrawn <slug>` - 标记ClawHub已撤回
- `find-paid-on-clawhub` - 查找需撤回的付费版
- `find-free-for-clawhub` - 查找待上传的免费版
- `find-rejected` / `find-platform-review` - 查找特定状态skill

### 4. ClawHub付费版策略 ✓

- **新策略**: 付费版不上传ClawHub（ClawHub为免费开源平台）
- **实施**: `clawhub.upload_eligible = false` for all paid versions
- **历史问题**: 172个付费版已在ClawHub发布，需逐步撤回
- **后续**: 只上传免费版到ClawHub，付费版仅在SkillHub销售

### 5. 关键发现

1. **41个孤儿platform_review skill**: 在SkillHub上有58个platform_review状态的skill，但只有17个在本地数据库中。其余41个可能是通过Web UI直接上传的企业版，不在本地管理范围内
2. **29个rejected skill**: 需逐个检查拒绝原因，修改后重新上传
3. **4个not_uploaded skill**: 本地存在但未上传到SkillHub
4. **版本不一致**: 部分skill本地版本与平台版本可能不一致（需后续核对）

### 文件变更
- `D:\skills\skill-registry\upload_tracking.json` - 重建为Schema v2.0 (723KB → ~1.2MB)
- `D:\skills\skill-registry\upload_tracking_v1_backup.json` - 旧版备份
- `D:\skills\skill-registry\platform_ops.py` - 新建平台运维工具
- `D:\skills\skill-registry\skillhub_review_status_raw.json` - (临时文件，在temp目录)

---

## Round 29 计划

### 1. SkillHub收尾操作
- 审核jira-pat-toolkit (最后1个admin_review)
- 逐个检查29个rejected skill的拒绝原因
- 修改被拒绝的skill后重新上传
- 跟进17个platform_review skill (联系skillhub_ipr@tencent.com)
- 调查41个非本地platform_review skill的来源

### 2. ClawHub付费版撤回 (172个)
- 使用 `python platform_ops.py find-paid-on-clawhub` 获取清单
- 通过ClawHub后台批量撤回付费版
- 撤回后运行 `python platform_ops.py mark-clawhub-withdrawn <slug> ...` 更新本地状态
- 优先撤回有免费版配对的付费skill

### 3. ClawHub免费版续传 (704个)
- 使用 `python platform_ops.py find-free-for-clawhub` 获取清单
- 每日200个限流，预计4天完成
- 上传后运行 `python platform_ops.py mark-clawhub-published <slug> ...` 更新本地状态

### 4. 4个未上传SkillHub的skill
- 检查本地数据库中 `skillhub.review_status = not_uploaded` 的4个skill
- 确认原因后上传

### 5. 三端数据一致性验证
- 本地2083 vs SkillHub 2032+17+29+1+4=2083 vs ClawHub 227+704=931 (目标)
- 生成最终对齐报告
- 确保本地数据库为唯一权威源

### 6. 个人版同步
- 团队版(org 862)的修改同步到个人版
- 无API访问，需通过UI操作

### 7. 版本一致性核对
- 对比本地版本与平台版本
- 发现不一致的更新到最新版本

## 提示词

复核Round 28的完成情况。Round 28的核心成果是重建了本地主数据库为唯一权威源（Schema v2.0），覆盖全生命周期+双平台状态，并创建了platform_ops.py运维工具。开始实施round-29计划：SkillHub收尾（审核jira-pat-toolkit、修复29个rejected、跟进17个platform_review）、ClawHub付费版撤回（172个）、ClawHub免费版续传（704个）、三端数据一致性验证。所有操作基于本地数据库驱动，不再反复查询平台。完成后生成下一轮的提示词。
