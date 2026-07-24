# Round 24 - SkillHub Platform Review 应对策略

## 现状分析

### 61个卡在 platform_review 的 skill

| 类型 | 数量 | 描述 |
|------|------|------|
| 测试技能 | 1 | `test-paid-skill` - 需删除 |
| 企业版技能 | 60 | changelog 为"企业版发布"的企业版上传技能 |

### API 限制
- `POST /api/v1/orgs/862/admin/skills/{slug}/approve` → 400: "skill is not in admin_review status"
- `POST /api/v1/orgs/862/admin/skills/{slug}/reject` → 400: "skill is not in admin_review status"
- platform_review 是平台侧二次审核，组织管理员无法通过API干预

## 应对策略

### 策略1：联系平台支持（推荐）
- 联系邮箱：skillhub_ipr@tencent.com（页面底部显示）
- 说明情况：61个技能长时间卡在平台审核状态，请求平台侧处理
- 附上技能列表和slug
- 预期结果：平台支持团队手动审核或批量通过

### 策略2：删除重新上传
- 对于确实需要的技能，可以先从SkillHub删除，然后重新上传
- 重新上传后会进入 admin_review 流程，可以正常审核
- 风险：可能再次进入 platform_review

### 策略3：等待平台审核完成
- platform_review 是平台侧的正常审核流程
- 可能因为技能数量多（2200+）导致审核积压
- 无需操作，等待平台处理

## 建议执行顺序

1. **立即执行**：删除 `test-paid-skill` 测试技能
2. **并行执行**：联系平台支持（邮件），附上60个企业版技能slug列表
3. **后续观察**：如果1周内无进展，考虑策略2删除重传

## 本次本地治理的影响

### 本地删除的158个skill
这些skill在SkillHub上可能仍有发布记录。需要：
1. 从SkillHub技能列表中查找已删除的skill
2. 对找到的执行下架/删除操作
3. 确保三端一致

### 本地修改的166个skill
这些skill的SKILL.md内容已更新（frontmatter修复、tags修复、版本对齐）。
需要：
1. 重新上传到SkillHub（版本号+1）
2. 同步到ClawHub（sync已在进行中）
3. 同步到个人版
