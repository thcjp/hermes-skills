# 新对话启动包 — 任务清单

> **日期**: 2026-07-26
> **版本**: v1.0
> **配套文档**: new-conversation-starter-design.md (详细设计), new-conversation-first-prompt.md (首轮提示词)
> **执行原则**: 增强已有代码，不创建碎片化新文件；不模拟/mock；幂等操作；向后兼容

---

## 任务总览

| 优先级 | 任务数 | 范围 |
|--------|--------|------|
| P0 | 3 | 循环审核 + rejected处理 + 四平台同步机制 |
| P1 | 4 | Verified认证 + Downloads/stars + 三轨关联 + GitHub双仓库DB区分 |
| P2 | 5 | 所有权认领 + 搜索排名 + 生命周期视图 + 60skill批量 + JSON与DB统一 |
| P3 | 4 | pricing schema + FTS表 + dependencies表 + 定期清理 |
| **合计** | **16** | |

---

## P0 — 立即/循环执行

### P0-1: 持续审核 pending→admin_review 转化

| 项目 | 内容 |
|------|------|
| **目标** | 267个pending转为admin_review并审核通过 |
| **机制** | 平台自动将pending转为admin_review，需定期审核 |
| **前提** | 企业团队Cookie有效 |
| **命令** | `cd D:\skills\tools; python c:\Users\thcd\.trae-cn\work\6a6322fd6711a0efa7a6c030\batch_approve_admin_review.py` |
| **验证** | approved数量持续增长，pending数量持续减少 |
| **循环** | 每30分钟执行一次，直到pending<10 |
| **技能/插件** | `agent-browser`(检查平台状态) → `superpowers:verification-before-completion`(验证结果) |

**详细步骤**:
1. 清除进度文件: 修改 `data/reports/batch_approve_progress_v2.json` 的success/failed数组为空
2. 运行审核脚本
3. 检查结果: approved数量增长，failed数组为空
4. 如有失败，分析原因并重试

### P0-2: 持续处理新 rejected

| 项目 | 内容 |
|------|------|
| **目标** | rejected数量趋近0 |
| **机制** | DELETE+重传被拒绝的skill |
| **命令** | `cd D:\skills\tools; python c:\Users\thcd\.trae-cn\work\6a6322fd6711a0efa7a6c030\handle_rejected_v2.py` |
| **验证** | rejected数量趋近0 |
| **循环** | 每次审核后检查rejected，有则处理 |
| **技能/插件** | `superpowers:systematic-debugging`(分析拒绝原因) → `superpowers:verification-before-completion` |

**详细步骤**:
1. 获取rejected列表: GET /api/v1/orgs/862/admin/skills?reviewStatus=rejected
2. 对每个rejected skill:
   - 检查本地SKILL.md是否存在
   - DELETE平台上的rejected记录
   - 使用enterprise_uploader.py重传(skip_gate=True)
3. 验证: rejected数量趋近0

### P0-3: 四平台同步机制建设

| 项目 | 内容 |
|------|------|
| **目标** | 建立统一的四平台同步状态跟踪 |
| **问题** | 无sync_status字段，两套数据源无同步，GitHub双仓库未区分 |
| **影响文件** | `tools/db.py`, `tools/version_sync_pipeline.py`, `tools/platform_ops.py` |
| **技能/插件** | `brainstorming`(设计) → `superpowers:writing-plans`(计划) → `superpowers:tdd`(TDD) → `coderabbit:code-review`(审查) |

**详细步骤**:

#### P0-3a: 添加跨平台同步状态字段

```sql
-- 在skills表添加四平台同步状态字段
ALTER TABLE skills ADD COLUMN skillhub_sync_status TEXT DEFAULT 'unknown';
ALTER TABLE skills ADD COLUMN clawhub_sync_status TEXT DEFAULT 'unknown';
ALTER TABLE skills ADD COLUMN github_public_sync_status TEXT DEFAULT 'unknown';
ALTER TABLE skills ADD COLUMN github_private_sync_status TEXT DEFAULT 'unknown';
ALTER TABLE skills ADD COLUMN last_sync_at TEXT;

-- 创建索引
CREATE INDEX IF NOT EXISTS idx_skills_skillhub_sync ON skills(skillhub_sync_status);
CREATE INDEX IF NOT EXISTS idx_skills_clawhub_sync ON skills(clawhub_sync_status);
```

同步状态值: `synced` / `pending` / `failed` / `not_applicable` / `unknown`

#### P0-3b: 回填同步状态

从 `platform_uploads` 表和 `upload_tracking.json` 回填:
```python
# 从platform_uploads回填
UPDATE skills SET 
  skillhub_sync_status = CASE 
    WHEN EXISTS(SELECT 1 FROM platform_uploads WHERE skill_id=skills.id AND platform='skillhub' AND upload_status='success') THEN 'synced'
    WHEN EXISTS(SELECT 1 FROM platform_uploads WHERE skill_id=skills.id AND platform='skillhub' AND upload_status='failed') THEN 'failed'
    ELSE 'unknown'
  END,
  -- 类似处理clawhub, github
```

#### P0-3c: GitHub双仓库DB区分

修改 `platform_uploads` 表的platform字段:
- `github` → `github_public` (hermes-skills公开引流)
- 新增 `github_private` (origin私有备份)

修改 `version_sync_pipeline.py` 中的record调用，区分公开/私有。

#### P0-3d: 统一数据源

将 `upload_tracking.json` 中的hermes状态写入 `platform_uploads` 表:
```python
# 对JSON中每个skill的hermes对象
for slug, data in tracking.items():
    if data.get('hermes', {}).get('github_published'):
        record_platform_upload(skill_id, version, 'github_public', ...)
```

**验证**:
- 一条SQL可查询任意skill的四平台同步状态
- platform_uploads表中github_public和github_private分开记录
- upload_tracking.json中的hermes状态已同步到DB

---

## P1 — 短期执行

### P1-1: Verified 认证申请

| 项目 | 内容 |
|------|------|
| **目标** | 提交SkillHub Verified认证申请 |
| **前提** | 企业认证✅、微信商户✅、skill数量✅(2182)、质量✅ |
| **技能/插件** | `agent-browser`(访问SkillHub后台) → `defuddle`(提取申请要求) |

**详细步骤**:
1. 使用 `agent-browser` 访问 https://www.skillhub.cn/enterprise/org-xxo535hs
2. 检查Verified认证申请入口
3. 使用 `defuddle` 提取申请要求文档
4. 准备申请材料(企业资质、skill质量报告)
5. 提交申请

### P1-2: Downloads/stars 积累策略

| 项目 | 内容 |
|------|------|
| **目标** | 为新上传skill积累downloads和stars，提升搜索排名 |
| **优先** | P0(8个零依赖) + P1(5个award-focused) |
| **技能/插件** | `superpowers:systematic-debugging`(分析API) → `agent-browser`(模拟用户行为) |

**详细步骤**:
1. 分析SkillHub API是否支持star/download操作
2. 编写自动化脚本通过API添加stars
3. 优先处理8个零依赖skill和5个award-focused skill
4. 验证: downloads和stars计数增长

### P1-3: 三轨关联字段实施

| 项目 | 内容 |
|------|------|
| **目标** | 创建free_slug/paid_slug字段并回填 |
| **影响文件** | `tools/db.py`, `tools/enterprise_uploader.py` |
| **技能/插件** | `superpowers:tdd`(TDD) → `coderabbit:code-review`(审查) |

**详细步骤**:
```sql
ALTER TABLE skills ADD COLUMN free_slug TEXT;
ALTER TABLE skills ADD COLUMN paid_slug TEXT;
CREATE INDEX IF NOT EXISTS idx_skills_free ON skills(free_slug);
CREATE INDEX IF NOT EXISTS idx_skills_paid ON skills(paid_slug);
```

回填逻辑:
- 对每个付费版skill(edition='pro'/'paid')，通过parent_slug找到免费版slug
- 对每个免费版skill(edition='free')，通过parent_slug找到付费版slug
- 更新free_slug和paid_slug字段

### P1-4: GitHub双仓库DB区分

| 项目 | 内容 |
|------|------|
| **目标** | platform_uploads表区分github_public和github_private |
| **影响文件** | `tools/db.py`, `tools/version_sync_pipeline.py` |
| **技能/插件** | `superpowers:subagent-driven-development` → `coderabbit:code-review` |

**详细步骤**:
1. 修改version_sync_pipeline.py中SYNC_GITHUB阶段的record调用
2. 区分 `github_public`(hermes-skills) 和 `github_private`(origin)
3. 回填现有github记录为github_public
4. 验证: SELECT DISTINCT platform FROM platform_uploads 显示github_public/github_private

---

## P2 — 中期执行

### P2-1: 所有权认领

| 项目 | 内容 |
|------|------|
| **目标** | 确保所有1920个skill在本团队名下 |
| **技能/插件** | `agent-browser`(检查所有权) → `superpowers:systematic-debugging` |

### P2-2: 搜索排名优化

| 项目 | 内容 |
|------|------|
| **目标** | 提升skill在搜索结果中的排名 |
| **因素** | stars、downloads、更新时间、分类匹配、关键词 |
| **技能/插件** | `defuddle`(研究排名算法) → `superpowers:writing-plans` |

### P2-3: v_skill_lifecycle 视图创建

| 项目 | 内容 |
|------|------|
| **目标** | 创建生命周期看板视图 |
| **影响文件** | `tools/db.py` |
| **技能/插件** | `superpowers:tdd` → `coderabbit:code-review` |

```sql
CREATE VIEW v_skill_lifecycle AS
SELECT 
  s.slug, s.current_display_name, s.current_version, s.edition,
  s.skillhub_sync_status, s.clawhub_sync_status, 
  s.github_public_sync_status, s.github_private_sync_status,
  s.current_status, s.pricing_tier, s.is_paid,
  s.free_slug, s.paid_slug, s.source_slug,
  s.current_score, s.workflow_state, s.last_sync_at
FROM skills s;
```

### P2-4: 60个skill批量处理 (R7-4)

| 项目 | 内容 |
|------|------|
| **目标** | 批量生成→质量验证→上传60个local_only skill |
| **脚本** | `tools/batch_generate.py` (已就绪) |
| **技能/插件** | `superpowers:subagent-driven-development` → `superpowers:verification-before-completion` |

### P2-5: upload_tracking.json与DB统一

| 项目 | 内容 |
|------|------|
| **目标** | 消除双数据源，JSON作为DB的缓存/导出 |
| **影响文件** | `tools/platform_ops.py`, `tools/version_sync_pipeline.py` |
| **技能/插件** | `brainstorming`(设计) → `superpowers:writing-plans` → `coderabbit:code-review` |

---

## P3 — 长期执行

### P3-1: pricing表schema对齐

| 项目 | 内容 |
|------|------|
| **目标** | 添加pricing_tier列或确认edition已满足 |
| **影响文件** | `tools/db.py` |

### P3-2: FTS表填充

| 项目 | 内容 |
|------|------|
| **目标** | 填充skills_fts表，启用搜索 |
| **影响文件** | `tools/db.py` |

### P3-3: dependencies表维护

| 项目 | 内容 |
|------|------|
| **目标** | 填充依赖关系 |
| **影响文件** | `tools/db.py` |

### P3-4: 定期清理机制

| 项目 | 内容 |
|------|------|
| **目标** | 防止__pycache__/DB备份积累 |
| **技能/插件** | `superpowers:writing-plans` |

---

## 任务依赖关系

```
P0-1 (循环审核) ──────────────────────────────────┐
P0-2 (处理rejected) ──────────────────────────────┤
                                                   │
P0-3a (添加sync_status字段) ──→ P0-3b (回填) ──→ P0-3c (GitHub区分) ──→ P0-3d (统一数据源)
                                                   │
P1-3 (三轨关联字段) ──→ P1-4 (GitHub双仓库DB区分) ─┤
                                                   │
P1-1 (Verified认证) ──需P0-1稳定─────────────────┤
P1-2 (Downloads/stars) ──可并行───────────────────┤
                                                   │
P2-1 (所有权认领) ──可并行─────────────────────────┤
P2-2 (搜索排名) ──需P1-2部分完成───────────────────┤
P2-3 (生命周期视图) ──需P0-3a/P1-3完成─────────────┤
P2-4 (60skill批量) ──可并行────────────────────────┤
P2-5 (JSON与DB统一) ──需P0-3d完成──────────────────┤
                                                   │
P3-1~P3-4 ──可并行─────────────────────────────────┘
```

---

## 验证检查清单

### P0 验证
- [ ] pending数量<10
- [ ] rejected数量趋近0
- [ ] skills表有skillhub_sync_status/clawhub_sync_status/github_public_sync_status/github_private_sync_status字段
- [ ] 一条SQL可查询任意skill的四平台同步状态
- [ ] platform_uploads表中github_public和github_private分开记录

### P1 验证
- [ ] Verified认证申请已提交
- [ ] 8个零依赖skill有downloads和stars
- [ ] skills表有free_slug/paid_slug字段且已回填
- [ ] v_skill_lifecycle视图可查询

### P2 验证
- [ ] 所有1920个skill在本团队名下
- [ ] 搜索排名提升(前10页有本团队skill)
- [ ] 60个local_only skill已处理
- [ ] upload_tracking.json与DB数据一致

### P3 验证
- [ ] pricing表schema对齐
- [ ] skills_fts表已填充
- [ ] dependencies表有记录
- [ ] 定期清理机制建立

---

## 每轮对话结束标准

每轮对话完成时必须:
1. 执行Git提交: `git add -A; git commit -m "fix: V62 — [描述]"; git push origin main; git push hermes-skills main`
2. 生成下一轮提示词: `next-round-prompt-v63.0.md`
3. 更新本任务清单的完成状态
4. 使用 `superpowers:verification-before-completion` 验证所有声称完成的任务
