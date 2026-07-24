# 第53轮提示词 (v53.0) — SkillHub审核拒绝修复 + 重新发布 + COS同步重试 + 53缺失付费生成 + GitHub推送恢复

> **日期**: 2026-07-25
> **上一轮完成**: V52 — 830个SkillHub技能license从Proprietary改为MIT + DB pricing清空
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库
> **最高优先级**: 💰 SkillHub重新发布 — license修复后需重新上传触发审核

## V52完成总结

| 任务 | 状态 | 结果 |
|------|------|------|
| V51完成验证 | ✅ | commits 7d461d824 + ac2d63ab2 确认 |
| SkillHub Pay Skill调研 | ✅ | 企业认证+微信商户号+支付服务封装,个人用户未上线 |
| 根因分析 | ✅ | license:Proprietary触发Pay Skill审核要求 |
| 830个SKILL.md license修复 | ✅ | Proprietary→MIT, 806+24个文件 |
| 定价元数据清理 | ✅ | 删除#定价元数据注释和pricing字段 |
| DB pricing_on_platform清空 | ✅ | 1129条skillhub记录pricing_on_platform=NULL |
| upload_tracking.json更新 | ✅ | 记录license修复策略 |
| Git提交 | ✅ | commit 611a1acc0 (831文件, +836/-1546) |
| Git推送 | ❌ | 网络中断(Connection reset) |

### SkillHub Pay Skill要求分析

| 要求 | 状态 | 说明 |
|------|------|------|
| 企业认证 | ❌ | 需在腾讯统一身份平台完成 |
| 微信商户号绑定 | ❌ | 需绑定微信支付商户号 |
| 付费服务封装 | ❌ | 需将服务封装为可调用Skill |
| 价格与计费说明 | ❌ | 需设置单次调用价格 |
| 个人用户Pay Skill | ❌ | "即将上线，敬请期待" |

### 三平台策略调整

| 平台 | 策略 | 说明 |
|------|------|------|
| SkillHub | 仅免费(MIT) | 引流为主,个人Pay Skill上线后再升级 |
| ClawHub | 免费+付费 | 海外开源生态,付费版保留Proprietary |
| hermes-skills | 免费+付费 | 公开引流仓库,付费版保留Proprietary |

### 数据库状态

| 表 | 记录数 | 说明 |
|----|--------|------|
| skills | 2882 | free:1675, paid:599, source:600, tool:8 |
| platform_uploads | 3446 | skillhub:1129(全部pricing=NULL), clawhub:1155, github:1159 |
| pricing | 1916 | 146个付费skill有定价(per_use, 19.9/29.9 CNY) |

### Git提交历史

```
611a1acc0 fix: V52 — 830个SkillHub技能license从Proprietary改为MIT
ac2d63ab2 docs: add v52.0 next-round prompt
7d461d824 fix: V51 — SkillHub平台状态同步 + retry_pending清零 + 53缺失付费标记
b92d03f28 fix: V50收尾 — 三语README更新 + upload_tracking hermes_eligible同步
```

## 实施任务

### 任务1: SkillHub重新发布触发审核 (最高优先级)

**问题**: 830个SKILL.md的license已从Proprietary改为MIT,但SkillHub平台上的版本仍然是旧的。需要重新上传触发审核。

**执行方案**:
1. 确认用户已登录 https://www.skillhub.cn
2. 使用浏览器MCP工具打开 https://www.skillhub.cn/admin/skills
3. 通过Admin API批量重新上传修改过的技能
4. API: `POST /api/v1/orgs/862/admin/skills/{slug}/reupload` 或类似端点
5. 如果无重新上传API,需要:
   - 先删除旧版本
   - 重新上传新版本(license:MIT)
6. 批量处理(每批10个,避免并发限制)
7. **验证**: 审核状态从rejected变为pending_review或approved

**优先处理**: 40+个被审核拒绝的技能(用户收到的通知)

**验证标准**: 至少10个技能审核通过,在SkillHub前台可搜索到

### 任务2: SkillHub COS同步重试

**问题**: 40个org_only技能因"COS文件同步失败"无法发布

**执行方案**:
1. 等待24小时后(COS可能已恢复)重试
2. 使用浏览器Admin API重新发布40个org_only技能
3. 如果仍然失败,联系SkillHub客服
4. 验证1995个public技能是否前台可见

**验证标准**: 40个org_only技能发布成功,前台搜索可见

### 任务3: 53个缺失付费skill生成

**问题**: 599个付费skill中,53个无-pro版本(源文件不存在)

**执行方案**:
1. 从数据库查询53个source_missing的slug
2. 读取对应free版本SKILL.md
3. 生成pro版本:
   - 增强功能描述
   - 添加付费特性说明
   - 修改license为Proprietary(仅ClawHub/hermes-skills)
4. 保存到 differentiated-skills/[category]/[slug]-pro/
5. 复制到 hermes-skills/[category]/paid/
6. 运行审计确保100%A级

**验证标准**: 53个source_missing全部生成-pro版本

### 任务4: GitHub推送恢复

**问题**: origin和hermes-skills推送均失败(Connection reset)

**执行方案**:
1. 检查网络连接
2. 配置Git: http.postBuffer, lowSpeedLimit, lowSpeedTime
3. 推送origin (私有备份): https://github.com/thcjp/-.git
4. 推送hermes-skills (公开引流): https://github.com/thcjp/hermes-skills.git
5. 如果持续失败,尝试SSH协议或分批推送

**验证标准**: 两个仓库均推送成功

### 任务5: ClawHub定时任务监控

**问题**: ClawHub定时任务(73efabe0)已创建,首次运行7/25 12:00北京

**执行方案**:
1. 检查定时任务执行状态(Schedule get 73efabe0)
2. 验证upload_tracking.json中ch_published数量变化
3. 如果执行失败,诊断并修复clawhub_batch_uploader.py

**验证标准**: ClawHub published数量增长

### 任务6: 源skill发现与扩展

**问题**: 当前110个源skill全部来自clawhub,需扩展来源

**执行方案**:
1. 从GitHub高星项目提取skill(anthropics/skills, obra/superpowers等)
2. 从dify项目提取可复用skill
3. 从n8n workflow提取可转化skill
4. 新skill添加到clawhub-skills/downloaded/
5. 运行差异化流程生成free+paid版本

**验证标准**: 数据库source skills从600增长至650+

### 任务7: 审计维护

**执行方案**:
1. 运行 `python tools/deep_quality_audit.py`
2. 检查L4-L9各层级结果
3. 如有非A级,立即修复

**验证标准**: L4-L9全部100%A级

### 任务8: Git提交与下一轮提示词生成

**执行方案**:
1. 提交所有变更
2. 推送到origin和hermes-skills
3. 生成 next-round-prompt-v54.0.md

## 验证检查清单

- [ ] SkillHub重新发布,40+被拒绝技能审核通过
- [ ] SkillHub前台至少10个技能可搜索到
- [ ] COS同步重试,40个org_only技能发布成功
- [ ] 53个缺失付费skill生成-pro版本
- [ ] GitHub origin推送成功
- [ ] GitHub hermes-skills推送成功
- [ ] ClawHub定时任务执行成功
- [ ] 源skill新增50+
- [ ] L4-L9审计100%A级
- [ ] 下一轮提示词v54.0生成

## 约束

1. **增强已有代码** — 所有修复功能集成到现有工具脚本，不创建碎片化新文件
2. **不模拟/mock** — 所有文件修改和数据库操作必须真实执行
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏现有命令功能
5. **内容保真** — tags增强和value proposition增强不得改变技能原有语义和功能
6. **网络容错** — GitHub推送失败不应阻塞其他任务的执行
7. **质量底线** — 不得引入任何会降低L4-L9审计等级的修改(当前100%A级)
8. **三平台策略** — SkillHub=免费引流, ClawHub=免费+付费, hermes-skills=免费+付费
9. **分类统一** — 本地分类目录=skillhub分类=clawhub分类=hermes-skills分类
10. **版本同步** — 本地skill版本升级后,必须同步到全部3个平台
11. **SkillHub优先** — SkillHub前台可见性是最高优先级,license已修复需重新发布
12. **Pay Skill规划** — 个人用户Pay Skill上线后,再升级付费技能到Pay Skill
