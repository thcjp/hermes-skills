# 第54轮提示词 (v54.0) — SkillHub重新发布触发审核 + ClawHub定时任务监控 + 源skill扩展 + 审计维护

> **日期**: 2026-07-25
> **上一轮完成**: V52/V53 — 830个license修复(Proprietary→MIT) + 53个source_missing修复 + L4-L9审计100%A级 + GitHub双仓库推送成功
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库
> **最高优先级**: 💰 SkillHub重新发布 — license已修复为MIT,需重新上传触发审核

## V52/V53完成总结

| 任务 | 状态 | 结果 |
|------|------|------|
| V51完成验证 | ✅ | commit 7d461d824 确认 |
| SkillHub审核拒绝根因分析 | ✅ | license:Proprietary触发Pay Skill审核要求 |
| 830个SKILL.md license修复 | ✅ | Proprietary→MIT (commit 611a1acc0) |
| DB pricing_on_platform清空 | ✅ | 1129条skillhub记录pricing_on_platform=NULL |
| 53个source_missing修复 | ✅ | local_path更新为packaged-skills/skillhub/[slug] |
| L4-L9审计 | ✅ | 100%A级 (2097/2097, 平均分100.0) |
| GitHub origin推送 | ✅ | b92d03f28..611a1acc0 main→main |
| GitHub hermes-skills推送 | ✅ | b92d03f28..611a1acc0 main→main |
| upload_tracking.json更新 | ✅ | 记录V52/V53执行结果 |
| SkillHub重新发布 | ❌ | 会话过期,API凭证失效,需用户登录 |
| ClawHub定时任务 | ⏳ | Active, 0次执行, 下次2026-07-24T20:00 UTC |

### SkillHub审核拒绝问题分析

| 维度 | 详情 |
|------|------|
| **用户收到的通知** | "您的Skill「xxxxx」版本xxxx审核未通过：该Skill缺少必要的支付服务" (40+个) |
| **根因** | SKILL.md中license:Proprietary触发SkillHub Pay Skill审核流程 |
| **SkillHub Pay Skill要求** | 企业认证 + 微信商户号 + 支付服务封装 + 价格设置 |
| **个人用户Pay Skill** | "即将上线，敬请期待" (未开放) |
| **修复方案** | license从Proprietary改为MIT (830个文件已修复) |
| **待办** | 需重新上传830个技能到SkillHub触发重新审核 |
| **阻塞原因** | SkillHub会话过期,API Key失效,CLI不支持publish |

### 三平台策略

| 平台 | 策略 | License | 说明 |
|------|------|---------|------|
| SkillHub | 仅免费(MIT) | MIT | 引流为主,Pay Skill上线后再升级 |
| ClawHub | 免费+付费 | MIT/Proprietary | 海外开源生态 |
| hermes-skills | 免费+付费 | MIT/Proprietary | 公开引流仓库 |

### 数据库状态

| 表 | 记录数 | 说明 |
|----|--------|------|
| skills | 2882 | free:1675, paid:599, source:600, tool:8 |
| platform_uploads | 3446 | skillhub:1129(全部MIT), clawhub:1155, github:1159 |
| source_missing | 0 | 53个已全部修复 |

### Git提交历史

```
611a1acc0 fix: V52 — 830个SkillHub技能license从Proprietary改为MIT
ac2d63ab2 docs: add v52.0 next-round prompt
7d461d824 fix: V51 — SkillHub平台状态同步 + retry_pending清零
b92d03f28 fix: V50收尾 — 三语README更新 + upload_tracking同步
```

## 实施任务

### 任务1: SkillHub重新发布触发审核 (最高优先级)

**问题**: 830个SKILL.md的license已从Proprietary改为MIT,但SkillHub平台上的版本仍然是旧的。用户收到40+个审核拒绝通知。需要重新上传触发审核。

**阻塞原因**: SkillHub会话过期,API Key失效,CLI不支持publish命令

**执行方案**:
1. **用户登录SkillHub**: 导航到 https://www.skillhub.cn,完成登录
2. **获取新Cookie**: 登录后从浏览器导出cookie到 `~/.skillhub_cookies.txt`
3. **使用浏览器API重新发布**:
   - 导航到 https://www.skillhub.cn/admin/skills
   - 使用browser_evaluate调用Admin API获取所有技能列表
   - 筛选status为rejected/pending_review的技能
   - 通过 `POST /api/v1/orgs/862/skills` 重新上传(license:MIT)
   - 每批10个,避免并发限制
4. **验证**: 至少10个技能审核通过,在SkillHub前台可搜索到
5. **优先处理**: 40+个被审核拒绝的技能

**验证标准**: 
- 40+个被拒绝技能重新提交审核
- 至少10个技能在skillhub.cn/skills前台可搜索到
- sh_frontend_visible > 0

### 任务2: ClawHub定时任务监控

**问题**: ClawHub定时任务(73efabe0)Active但0次执行,下次运行2026-07-24T20:00 UTC

**执行方案**:
1. 等待定时任务首次执行
2. 执行后检查:
   - Schedule get 73efabe0 查看执行记录
   - 检查upload_tracking.json中ch_published数量变化
   - 验证VERSION_EXISTS和protected namespace错误处理
3. 如果定时任务执行失败:
   - 诊断失败原因
   - 修复clawhub_batch_uploader.py
   - 手动触发一次(trigger)测试

**验证标准**: ClawHub published数量从1153增长

### 任务3: 源skill发现与扩展

**问题**: 当前600个源skill全部来自clawhub,需扩展来源

**执行方案**:
1. 从GitHub高星项目提取skill:
   - anthropics/skills
   - obra/superpowers  
   - 12-factor-agents
   - langgraph
   - crewAI
   - autogen
2. 从dify项目提取可复用skill
3. 从n8n workflow提取可转化为skill的工作流
4. 将新skill添加到clawhub-skills/downloaded/
5. 录入数据库(source=github/dify/n8n)
6. 运行差异化流程生成free+paid版本

**验证标准**: 数据库source skills从600增长至650+

### 任务4: hermes-skills前端可见性优化

**问题**: hermes-skills仓库已推送成功,但需优化引流效果

**执行方案**:
1. 检查README.md的三语版本数据是否准确
2. 添加SkillHub和ClawHub的引流链接
3. 添加付费skill的购买引导
4. 优化SEO(关键词、描述)
5. 添加Star引导和Issue模板

**验证标准**: hermes-skills README含引流链接,数据准确

### 任务5: 审计维护

**执行方案**:
1. 运行 `python tools/deep_quality_audit.py`
2. 检查L4-L9各层级结果
3. 如有非A级,立即修复

**验证标准**: L4-L9全部100%A级

### 任务6: Git提交与下一轮提示词生成

**执行方案**:
1. 提交所有变更到本地git
2. 推送到origin和hermes-skills
3. 生成 next-round-prompt-v55.0.md
4. 更新ARCHITECTURE.md中的平台策略表

## 验证检查清单

- [ ] SkillHub重新发布,40+被拒绝技能重新提交审核
- [ ] SkillHub前台至少10个技能可搜索到
- [ ] ClawHub定时任务首次执行成功
- [ ] 源skill新增50+(从GitHub/dify/n8n)
- [ ] hermes-skills README含引流链接
- [ ] L4-L9审计100%A级
- [ ] 下一轮提示词v55.0生成

## 约束

1. **增强已有代码** — 所有修复功能集成到现有工具脚本，不创建碎片化新文件
2. **不模拟/mock** — 所有文件修改和数据库操作必须真实执行
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏现有命令功能
5. **内容保真** — tags增强和value proposition增强不得改变技能原有语义和功能
6. **网络容错** — GitHub推送失败不应阻塞其他任务的执行
7. **质量底线** — 不得引入任何会降低L4-L9审计等级的修改(当前100%A级)
8. **三平台策略** — SkillHub=免费引流(MIT), ClawHub=免费+付费, hermes-skills=免费+付费
9. **分类统一** — 本地分类目录=skillhub分类=clawhub分类=hermes-skills分类
10. **版本同步** — 本地skill版本升级后,必须同步到全部3个平台
11. **SkillHub优先** — SkillHub重新发布是最高优先级,license已修复需重新上传
12. **Pay Skill规划** — 个人用户Pay Skill上线后,再升级付费技能到Pay Skill
13. **用户登录** — SkillHub重新发布需要用户先登录skillhub.cn,获取有效session
