# Round 37 执行提示词 v37.0

## 上下文
- **上一轮**: Round 36 (Git: 58542b46, 63 files, +1705/-24084)
- **当前日期**: 2026-07-24
- **数据库**: 1917 skills, 0 NULL pricing_tier, 0 'free' tier
- **平台状态**: SkillHub 2068 published/7 pending_review, ClawHub 773 published/144 pending, Hermes 1067 published

## Round 36 完成情况

### Task 1 (P0): 修复MISSING_TOOLS/MISSING_TAGS/MISSING_SLUG - 完成 ✅
- 扫描全部3个目录,修复2137个SKILL.md文件
- MISSING_TOOLS: 2137→0, MISSING_TAGS: 2092→0, MISSING_SLUG/VERSION/NAME: 1→0
- 审计critical issues: 0 ✅

### Task 2 (P0): ClawHub批量上传 - 部分完成 ⚠️
- 本轮上传117个成功,22个VERSION_EXISTS失败
- 今日总上传158个(41+117),ClawHub已发布773个
- **剩余**: 144个待上传 + 22个VERSION_EXISTS需版本递增修复
- 限流窗口: 200/24h,下次重置约2026-07-24T21:01:18

### Task 3 (P1): L7A全量去重 - 完成 ✅
- 消除1211个重复块对(788个文件)
- 73个重复章节标题文件修复为0
- 表格分隔符重复规范化,通用付费能力行差异化

### Task 4 (P1): L3定价再平衡 - 完成 ✅
- L3从56.1%(1076/1917)降至27.5%(527/1917)
- L1+L2从30.3%升至58.9%(1129/1917)
- 549个L3降级: 321→L1, 228→L2
- 0个'free' pricing_tier, 0个NULL pricing_tier

### Task 5 (P2): L7b报告更新 - 完成 ✅
- 审计结果: A=2097, B=0, C=0, D=0, F=0
- avg_score=100.0, pass_rate=100%, executable=2097/2097
- 全部6项检查: VAGUE_TASK=0, MISSING_INPUT=0, NO_OUTPUT=0, BROKEN_REF=0, NO_CODE=0, CONTRADICTION=0
- 3个B级矛盾skill已修复(solo-workflow-engine-pro, agentvibes-skill-free, weather-toolkit-free)
- 修复后重新审计: A=2097, B=0 (100% A级)

### Task 6 (P2): SkillHub审核分析 - 完成 ✅
- 7个pending_review skills已修复(移除外部URL/营销文本/重复YAML字段/乱码修复)
- 分析8类安全审核失败原因: EXTERNAL_URL, INJECTED_MARKETING_TEXT, API_KEY_EXPOSURE, SLUG_CONTENT_MISMATCH, DUPLICATE_YAML_FIELDS, TAG_MISMATCH, GARBLED_TEXT, DEPENDENCY_CONTRADICTION
- 21个deleted skills中13个已成功republished,7个仍pending

## 交叉验证发现的遗留问题

### 1. ClawHub 144个待上传 + 22个VERSION_EXISTS失败
- 144个skill尚未上传到ClawHub
- 22个skill因版本号已存在(VERSION_EXISTS)导致上传失败
- 需要在SKILL.md中递增version字段后重新上传
- 失败列表: github-api-toolkit-free, grain-crawler-free, graph-query-tool-free, jira-flow-skill-free, json-lint-tool-free, json-validator-free, key-vault-manager-free, linear-api-toolkit-free, linear-sync-tool-free, linear-workflow-skill-free, mongo-manager-free, notion-api-toolkit-free, ops-dashboard-free, pg-mcp-skills-free, remix-auth-tool-free, tg-bot-builder-free, figma-toolkit-free, nano-pdf-tool-free, popeye-prod-tool-free, personal-health-tool-free, auto-monitor-tool-free, k8s-devops-tool-free

### 2. SkillHub 7个pending_review需重新提交
- 7个skills已修复安全审核问题,但仍处于pending状态
- 需要通过skillhub publish命令重新提交
- 版本控制工作流, 数据分析工具包, 交易策略指南, XML解析工具, 文字RPG街机v3, 视频上传流工具, PDF压缩工具

### 3. L6内容真实性: 15个skill有轻微问题
- 7个EMPTY_LIMITATIONS (已知限制段落为空): daily-news-brief, figma, juejin-skills, namecheap-dns, okx-dex-token, ui-ux, pdf-compressor-tool
- 2个EMPTY_SECTIONS (3个段落为空或过短): cron-assist, cron-scheduler-pro
- 5个PLACEHOLDER_CASE (案例展示为占位符内容): cron-master-pro, cron-scheduler-pro, 等
- 1个EMPTY_LIMITATIONS: 另有1个skill

### 4. 数据库platform_uploads表未同步
- platform_uploads表仅记录161条clawhub上传,实际已发布773个
- 需要批量同步上传记录到数据库

### 5. L7a审计显示"enabled: false"
- 最新审计运行时L7a标记为disabled
- 所有skill显示"L7A_DISABLED: Layer 7a 未启用"
- 但avg_score=100.0, template_blocks=0, 可能是审计脚本逻辑问题
- 需要检查deep_quality_audit.py的L7a启用条件

### 6. ClawHub已发布数与数据库不匹配
- ClawHub实际已发布: 773个(published_slugs.json)
- 数据库platform_uploads记录: 161条
- 需要全量同步

## Round 37 任务清单

### Task 1 (P0): ClawHub剩余144+22个skill上传
**目标**: 完成ClawHub全量上传

1. 修复22个VERSION_EXISTS失败skill: 在SKILL.md中递增version字段(1.0.0→1.0.1)
2. 检查ClawHub限流是否已重置(距上次上传>24h)
3. 运行`python clawhub_batch_uploader.py --resume --limit 200`上传剩余166个(144+22)
4. 如果仍有剩余,记录并在下一轮继续
5. 上传完成后同步clawhub_published_slugs.json和数据库platform_uploads表

**验证标准**:
- ClawHub published count >= 939 (773+166)
- 0个VERSION_EXISTS失败
- platform_uploads表clawhub记录数 >= 939

### Task 2 (P0): SkillHub 7个pending_review重新提交
**目标**: 将修复后的7个skill重新提交到SkillHub

1. 对7个已修复skill执行`skillhub publish`命令
2. 检查提交后状态是否从pending变为reviewing
3. 如果仍被拒绝,分析新的失败原因并修复
4. 记录每个skill的提交结果

**验证标准**:
- 7个skill已重新提交
- 提交结果已记录

### Task 3 (P1): 数据库platform_uploads全量同步
**目标**: 使数据库上传记录与实际平台状态一致

1. 读取clawhub_published_slugs.json获取全部773个已发布slug
2. 对比数据库platform_uploads表,找出缺失记录
3. 批量插入缺失的上传记录
4. 同步skillhub的2068条published记录
5. 验证数据库记录数与平台实际一致

**验证标准**:
- platform_uploads表clawhub记录数 = 773
- platform_uploads表skillhub记录数 = 2068
- 0条不一致记录

### Task 4 (P1): L6内容真实性修复(15个skill)
**目标**: 消除L6审计中的15个轻微问题

1. 修复7个EMPTY_LIMITATIONS: 为每个skill添加具体的已知限制内容
2. 修复2个EMPTY_SECTIONS: 填充空段落或过短段落
3. 修复5个PLACEHOLDER_CASE: 用具体案例替换占位符内容
4. 重新运行审计验证L6 avg_score=100.0

**验证标准**:
- L6 total_with_issues = 0
- L6 avg_score = 100.0
- 0个EMPTY_LIMITATIONS, 0个EMPTY_SECTIONS, 0个PLACEHOLDER_CASE

### Task 5 (P2): L7a审计启用状态修复
**目标**: 确保L7a审计正确启用并运行

1. 检查deep_quality_audit.py中L7a的启用条件
2. 修复导致L7a标记为disabled的逻辑问题
3. 重新运行完整审计(不带--layer7b参数)
4. 验证L7a正确运行并显示enabled: true

**验证标准**:
- L7a enabled = true
- L7a avg_score = 100.0
- L7a total_template_blocks = 0
- 0个L7A_DISABLED问题

### Task 6 (P2): 安全审核失败预防规则文档
**目标**: 将8类安全审核失败原因转化为可执行的预防规则

1. 基于skillhub_review_analysis_v36.json的8类失败原因
2. 编写安全审核预防检查清单(可集成到deep_quality_audit.py)
3. 新增L8安全审计层: 检查外部URL、营销文本注入、API密钥模式、slug内容匹配等
4. 对全部2097个skill运行L8审计
5. 修复发现的任何安全问题

**验证标准**:
- L8审计层已实现并集成
- 安全审核预防规则文档已创建
- 全量L8审计通过率 > 99%

## 执行规则
1. 遵循`修复提示词.md`的R1-R78规则
2. 每个任务完成后进行代码级验证(非文档声明)
3. 禁止任何形式的mock/fallback/todo/pass
4. 修复必须覆盖全部3个目录(packaged-skills/skillhub, opensource-skills/packaged, differentiated-skills)
5. 完成后生成下一轮提示词v38.0

## 平台统计速览
| 平台 | 已发布 | 待审核/待上传 | 总计 |
|------|--------|---------------|------|
| SkillHub | 2068 | 7 pending | 2075 |
| ClawHub | 773 | 144+22 pending | 939 |
| Hermes | 1067 | 0 | 1067 |

## 审计质量速览
| 层级 | 状态 | A级 | B级 | C+D+F级 | avg_score |
|------|------|-----|-----|---------|-----------|
| L6 内容真实性 | ✅ | 2097 | 0 | 0 | 99.5 |
| L7a 语义模板 | ⚠️ disabled | 2097 | 0 | 0 | 100.0 |
| L7b 可执行性 | ✅ | 2097 | 0 | 0 | 100.0 |
| Critical | ✅ | 0 critical, 0 warning, 2097 OK | | | |

## 定价分布速览
| 定价层级 | 数量 | 占比 | 目标 |
|----------|------|------|------|
| L1-入门级 | 443 | 23.1% | - |
| L2-标准级 | 686 | 35.8% | - |
| L3-专业级 | 527 | 27.5% | <40% ✅ |
| L4-企业级 | 261 | 13.6% | - |
| L1+L2合计 | 1129 | 58.9% | >30% ✅ |
| NULL/free | 0 | 0% | 0 ✅ |
