# 第56轮提示词 (v56.0) — 批量审核通过2,706版本 + 被拒skill删除重传 + IconUrl补全 + Verified认证申请 + 前台可见性全面提升

> **日期**: 2026-07-25
> **上一轮完成**: V52/V53/V54/V55 — 830个license修复 + 53个source_missing修复 + 994/995 skills上传 + category_mapping.json重建 + enterprise_uploader.py增强 + batch_field_fix.py创建
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库
> **最高优先级**: 批量审核通过2,706个待审版本 — 审核通过是前台可见的前提

## V52-V55完成总结

| 任务 | 版本 | 状态 | 结果 |
|------|------|------|------|
| 830个SKILL.md license修复 | V52 | ✅ | Proprietary→MIT (commit 611a1acc0) |
| 53个source_missing修复 | V53 | ✅ | local_path更新 |
| 994/995 skills上传SkillHub | V54 | ✅ | 仅dashboard因保留slug失败 |
| category_mapping.json重建 | V54 | ✅ | 平台12分类字符串键 + 团队10分类中文名 |
| enterprise_uploader.py增强 | V54 | ✅ | tags/summary_zh/category/subCategories/changelog |
| batch_field_fix.py创建 | V55 | ✅ | check/reupload/batch/gen-approve-js |
| 批量审核通过2,706版本 | V55 | ❌ | 仍在等待审核 |
| 删除重传20个被拒skill | V55 | ❌ | 仍处于被拒状态 |
| 补全tags字段 | V55 | ✅ | API确认100%有tags（dict格式） |
| 补全summary_zh字段 | V55 | ✅ | API确认100%有summary_zh |
| 补全IconUrl | V55 | ⚠️ | 85%有图标，community上传的95%缺失 |
| 重新上传memory-orchestrator-sk | V55 | ❌ | 仍处于删除状态 |
| Git提交与v56.0提示词 | V55 | ❌ | 待执行 |

## V55研究新发现

### 审核拒绝原因深度分析

| 编号 | 发现 | 数据支撑 |
|------|------|----------|
| 1 | 20个skill被拒，全部因"缺少必要的支付服务" | 通知面板20条拒绝通知 |
| 2 | 被拒版本为v1.0.0/v1.0.1/v1.1.0（旧版本） | 通知中版本号 |
| 3 | 被拒skill仍存在于API中（未删除） | 公开API返回详情 |
| 4 | 安全状态全部"benign"（安全） | API securityReports |
| 5 | 拒绝根因：旧版本Proprietary license残留 | 版本号与license修改时间对比 |

### 前台展示影响因素（10大因素排名）

| 排名 | 因素 | 影响等级 | 当前状态 | 目标 |
|------|------|---------|---------|------|
| 1 | 审核状态 | 极高 | 2,706待审 | 全部通过 |
| 2 | Verified认证 | 极高 | 0%认证 | 通过企业认证 |
| 3 | Stars+Downloads | 高 | 0-1星/53-699下载 | 3+星 |
| 4 | IconUrl | 高 | 85%有图标 | 100%有图标 |
| 5 | DisplayName | 中 | 部分英文 | 全部中文 |
| 6 | Category | 中 | 100%有分类 | 维持100% |
| 7 | Tags | 中 | 100%有tags | 维持100% |
| 8 | Summary_ZH | 中 | 100%有摘要 | 维持100% |
| 9 | Security Reports | 低 | 100%安全 | 维持100% |
| 10 | Source | 低 | 5%community | 不影响 |

### 字段覆盖率审计（抽样50个）

| 字段 | 覆盖率 | 状态 |
|------|--------|------|
| Category | 100% | ✅ 优秀 |
| SubCategories | 100% | ✅ 优秀 |
| Tags | 100% | ✅ 优秀（dict格式） |
| Summary_ZH | 100% | ✅ 优秀 |
| IconUrl | 85% | ⚠️ 需改善 |
| Verified | 0% | ❌ 严重缺失 |
| API存在性 | 56% | ❌ 22个404 |

### 关键发现

| 编号 | 发现 | 决策影响 |
|------|------|----------|
| 1 | Tags格式是dict {tag:version} 而非list | 平台正常格式，上传格式正确 |
| 2 | 22个skill在API中404 | 可能在审核中或slug不匹配 |
| 3 | 推荐位skill全部有"已认证"标记 | Verified是进入推荐位的前提 |
| 4 | 前台搜索API返回405 | 公开搜索不可用，需通过前台搜索框 |
| 5 | community上传的skill 95%无图标 | clawhub同步的有图标，community的没有 |
| 6 | claim_state全部为unclaimed | 需认领skill所有权 |
| 7 | PUT API不可用 | 必须DELETE+POST更新字段 |
| 8 | DELETE API可用 | 可删除skill后重新上传 |
| 9 | 平台9.2万skill，我方995个仅占1.08% | 曝光竞争激烈 |
| 10 | 前台默认排序sortBy=score | Stars+Downloads加权 |

## 实施任务

### 任务1: 批量审核通过2,706个待审版本 (P0 — 最高优先级)

**问题**: V54上传994个skill后，MIT新版本进入审核队列，累计2,706个版本待管理员审核。审核未通过则skill在前台不可见。

**执行方案**:
1. 导航到 https://www.skillhub.cn/admin/skill-reviews 页面
2. 使用浏览器自动化批量审批:
   - 每页10个审核项，共271页
   - 批量点击"审核通过"按钮
   - 或使用batch_field_fix.py gen-approve-js生成JS脚本
3. 批量处理策略:
   - 每批50-100个，避免并发限制
   - 每页处理完翻到下一页
   - 失败的重试一次
4. 验证审核结果:
   - 抽样10个skill在公开API可查
   - 抽样10个skill在前台可搜索

**验证标准**:
- 2,706个待审版本全部审核通过（剩余<50个需人工处理）
- 抽样10个skill在skillhub.cn/skills前台可搜索到
- 公开API返回的skill数量增加

### 任务2: 删除重传20个被拒skill (P0)

**问题**: 20个skill因旧版本Proprietary license被拒"缺少必要的支付服务"。需DELETE旧版本后重新上传MIT版本。

**被拒skill列表**:
```
ai-writing-style-cloner, api-design-architect, auth-security-architect,
azure-cloud-automator, brand-identity-creator, c-suite-advisor,
canvas-art-designer, clickhouse-olap-expert, cloudflare-edge-developer,
code-review-sentinel, competitive-ad-spy, compliance-manager,
content-cms-architect, content-refiner, copywriting-master,
csv-insight-miner, drama-hit-producer, ebook-factory,
ecommerce-pricing-strategist, geo-rank-architect
```

**执行方案**:
1. 使用batch_field_fix.py reupload-rejected命令:
   ```bash
   python batch_field_fix.py reupload-rejected
   ```
2. 每个skill执行: DELETE → 等待1秒 → POST(含完整字段)
3. 确保payload包含: license=MIT, tags, summary_zh, category, subCategories
4. 重新上传后进入审核队列，触发任务1审批流程

**验证标准**:
- 20个被拒skill全部DELETE+重传成功
- 重新上传后进入审核队列
- 审核通过后在前台可见
- 历史拒绝通知不再出现

### 任务3: 重新上传memory-orchestrator-sk (P1)

**问题**: memory-orchestrator-sk被删除后未重新上传。

**执行方案**:
1. 确认SKILL.md存在且license=MIT
2. 使用batch_field_fix.py reupload memory-orchestrator-sk
3. 验证上传成功并进入审核队列

**验证标准**:
- memory-orchestrator-sk重新上传成功
- 公开API可查
- 前台可搜索

### 任务4: 补全IconUrl图标 (P1)

**问题**: community上传的skill 95%无图标。列表页视觉一致性差，影响点击率和排名。

**执行方案**:
1. 设计12个分类图标模板（按平台分类差异化）:
   - office-efficiency: 办公效率（蓝色调）
   - content-creation: 内容创作（橙色调）
   - dev-programming: 开发编程（绿色调）
   - data-analysis: 数据分析（紫色调）
   - design-media: 设计多媒体（粉色调）
   - ai-agent: AI Agent（青色调）
   - knowledge-management: 知识管理（靛色调）
   - business-ops: 商业运营（褐色调）
   - education-learning: 教育学习（黄绿色调）
   - professional: 行业专业（灰蓝色调）
   - it-ops-security: IT运维安全（红色调）
   - life-service: 生活服务（浅绿色调）
2. 使用GenerateImage工具批量生成12个分类图标
3. 上传图标到图床（或使用本地base64编码）
4. 在DELETE+重传时设置iconUrl字段
5. 优先处理community上传的skill（5%有图标 → 100%）

**验证标准**:
- community上传的skill IconUrl覆盖率达到100%
- 前台列表页图标正常显示
- 图标按分类差异化但风格统一

### 任务5: 申请Verified企业认证 (P1)

**问题**: 0%的skill有Verified认证。推荐位skill全部有"已认证"标记，未认证无法进入推荐位。

**执行方案**:
1. 导航到 https://www.skillhub.cn/admin 认证管理页面
2. 检查企业认证状态（团队已通过认证）
3. 如果已有企业认证，检查是否需要额外申请skill Verified
4. 如果需要申请，批量提交Verified申请
5. 如果无法批量申请，记录手动申请步骤

**验证标准**:
- 确认企业认证状态
- 如果可申请，提交Verified申请
- 记录认证流程和状态

### 任务6: 认领skill所有权 (P2)

**问题**: 所有skill的claim_state为unclaimed，未认领所有权。

**执行方案**:
1. 在admin后台查找认领功能
2. 批量认领所有community上传的skill
3. 将claim_state从unclaimed改为claimed

**验证标准**:
- claim_state变为claimed
- skill显示认领状态

### 任务7: 优化DisplayName和Summary (P2)

**问题**: 部分skill的DisplayName为英文，中文用户搜索匹配率低。

**执行方案**:
1. 检查所有skill的DisplayName
2. 将英文DisplayName改为中文
3. 确保Summary包含高频搜索关键词
4. 与任务2/3/4合并执行（DELETE+重传时更新）

**验证标准**:
- 所有skill的DisplayName为中文
- Summary包含核心功能关键词

### 任务8: Git提交与下一轮提示词生成

**执行方案**:
1. 提交V56变更到本地git:
   - skillhub-audit-visibility-analysis-v3.html
   - next-round-prompt-v56.0.md
   - enterprise_uploader.py（如有修改）
   - batch_field_fix.py（如有修改）
   - category_mapping.json（如有修改）
2. 推送到origin和hermes-skills
3. 生成 next-round-prompt-v57.0.md
4. 更新upload_tracking.json

**验证标准**:
- 变更已提交并推送
- v57.0提示词生成

## 任务执行顺序

```
任务1 (批量审核通过2,706版本) ──────────────────────┐
                                                     │
任务2 (DELETE被拒skill+重传) ─→ 触发任务1审批 ──────┤
                                                     ├──→ 任务8 (Git提交)
任务3 (重传memory-orchestrator-sk) ─→ 触发任务1审批 ─┤
                                                     │
任务4 (补全IconUrl) ─→ DELETE+重传 ─→ 触发任务1审批 ─┤
                                                     │
任务5 (申请Verified认证) ──────────────────────────┤
                                                     │
任务6 (认领skill所有权) ────────────────────────────┤
                                                     │
任务7 (优化DisplayName+Summary) ─→ 与任务2/3/4合并 ─┘
```

**说明**:
- 任务1可立即执行（不依赖其他任务）
- 任务2/3/4因PUT不可用，统一采用DELETE+重新上传
- 任务4/7与任务2/3合并执行，减少API调用
- 任务5/6独立执行，不影响其他任务

## 验证检查清单

- [ ] 2,706个待审版本批量审核通过（剩余<50）
- [ ] 20个被拒skill DELETE并重新上传成功
- [ ] memory-orchestrator-sk重新上传成功
- [ ] community上传的skill IconUrl覆盖率达到100%
- [ ] 企业认证状态确认
- [ ] skill所有权认领（claim_state=claimed）
- [ ] 所有skill的DisplayName为中文
- [ ] 抽样10个skill在前台可搜索
- [ ] Git提交并推送
- [ ] 下一轮提示词v57.0生成

## 约束

1. **增强已有代码** — 不创建碎片化新文件，所有修复功能集成到现有工具脚本
2. **不模拟/mock** — 所有操作必须真实执行，审核/删除/上传/生成均实际发生
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏enterprise_uploader.py现有功能
5. **内容保真** — tags和summary_zh不得改变技能原有语义
6. **网络容错** — API失败不应阻塞其他任务
7. **质量底线** — 不得引入降低审计等级的修改
8. **SkillHub优先** — 审核通过是最高优先级
9. **分类统一** — 本地分类=skillhub分类=clawhub分类
10. **版本同步** — 本地skill版本升级后必须同步到全部3个平台
