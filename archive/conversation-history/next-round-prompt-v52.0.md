# 第52轮提示词 (v52.0) — SkillHub COS同步修复 + 53缺失付费skill生成 + 源skill扩展 + GitHub推送恢复

> **日期**: 2026-07-25
> **上一轮完成**: V51 — SkillHub平台状态API验证 + retry_pending清零 + 53缺失付费标记 + hermes-skills提交
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库
> **最高优先级**: 💰 SkillHub前台可见性 — COS同步问题阻断引流和赚钱

## V51完成总结

| 任务 | 状态 | 结果 |
|------|------|------|
| hermes-skills仓库提交 | ✅ | 14分类+759免费+459付费=1218, commit成功 |
| 数据库状态验证 | ✅ | skill-registry.db健康(2882 skills, 16表) |
| SkillHub API验证 | ✅ | 2035总技能: 1995 public, 40 org_only |
| SkillHub浏览器发布 | ⚠️ | 40个org_only技能因"COS文件同步失败"全部失败 |
| SkillHub前台搜索验证 | ❌ | 搜索memory-distiller/cron-guard/免费版均无结果 |
| retry_pending清零 | ✅ | 8个→0(全部更新为success, visibility=public) |
| 53缺失付费skill处理 | ✅ | 全部标记为source_missing(无-pro版本) |
| upload_tracking.json更新 | ✅ | sh_public_on_platform=1995, sh_org_only=40 |
| ClawHub定时任务确认 | ✅ | Active, 0次执行, 下次7/25 12:00北京 |
| Git推送 | ❌ | origin+hermes-skills均网络失败(Connection reset) |

### SkillHub平台状态(API验证)

| 指标 | 值 | 说明 |
|------|----|------|
| 平台总技能数 | 2035 | API返回total=2035 |
| visibility=public | 1995 | 管理后台标记为公开 |
| visibility=org_only | 40 | 需发布到社区 |
| visibility=null | 0 | 无空值 |
| hidden=true | 0 | 无隐藏技能 |
| download_ready=false | 0 | 无未就绪技能 |
| 前台搜索可见 | 0 | COS同步失败导致前台不可见 |

### SkillHub COS同步问题分析

| 根因 | 证据 | 影响 |
|------|------|------|
| COS文件同步失败 | 40个org_only技能发布全部返回"COS 文件同步失败，请稍后重试" | 无法发布到社区 |
| 前台搜索不可见 | 搜索memory-distiller/cron-guard/免费版均0结果 | 1995个public技能也不可见 |
| 平台侧基础设施问题 | 错误来自api.skillhub.cn服务端 | 非客户端可修复 |
| 全平台22,000技能 | 前台显示"共2.2万个技能" | 其他发布者的技能可搜索 |

### 数据库状态

| 表 | 记录数 | 说明 |
|----|--------|------|
| skills | 2882 | free:1675, paid:599, source:600, tool:8 |
| platform_uploads | 3446 | skillhub:1129, clawhub:1155, github:1159 |
| versions | — | 版本历史 |
| skills_fts | — | 全文搜索索引 |

### 平台状态 (upload_tracking.json)

| 平台 | 状态 | 详情 |
|------|------|------|
| SkillHub | 1995 public + 40 org_only | COS同步失败, 前台0可见 |
| ClawHub | 1153 success (DB) | 定时任务Active, 下次7/25 12:00 |
| Community | 4032 published | 本地标记 |
| Hermes | 1218 eligible (759+459) | 已提交,推送待网络恢复 |
| GitHub | origin+hermes-skills | 网络中断,待重试 |

### 定时任务

| 任务 | ID | 状态 | 频率 | 说明 |
|------|----|------|------|------|
| ClawHub每日批量上传 | 73efabe0 | Active | 每日04:00 UTC | 200条/天, 0次执行 |
| JueJin每日Bug扫描 | 0e578864 | Paused | 每日09:00 | 已暂停 |

## 实施任务

### 任务1: SkillHub COS同步问题修复与重试 (最高优先级)

**问题**: SkillHub平台COS(腾讯云对象存储)文件同步失败,导致:
- 40个org_only技能无法发布到社区
- 1995个public技能在前台搜索中不可见
- 全部2035个技能的文件可能未同步到公共CDN

**根因**: api.skillhub.cn服务端返回"COS 文件同步失败，请稍后重试"

**执行方案**:
1. 等待24小时后重试(平台侧可能已修复)
2. 重新登录 https://www.skillhub.cn/admin
3. 使用浏览器MCP工具:
   - 导航到 https://www.skillhub.cn/admin/skills
   - 执行 `browser_evaluate` 调用API检查COS状态
   - 重试发布40个org_only技能
   - 验证1995个public技能是否前台可见
4. 如果COS仍然失败:
   - 联系SkillHub客服反馈COS同步问题
   - 检查是否有技能文件过大或格式问题
   - 尝试单个技能重新上传触发COS同步
5. 如果COS已恢复:
   - 批量发布40个org_only技能
   - 验证至少10个技能在前台可搜索到
   - 更新upload_tracking.json

**验证标准**: 
- 40个org_only技能发布成功
- 至少10个技能在skillhub.cn/skills前台可搜索到
- sh_frontend_visible > 0

### 任务2: 53个缺失付费skill生成

**问题**: 599个付费skill中,53个无-pro版本(源文件不存在),已标记为source_missing

**缺失skill示例**:
- telegram-agent-comm (Agents) — free版本存在,pro版本缺失
- discord-toolkit (Communication) — free版本存在,pro版本缺失
- email-toolkit (Communication) — free版本存在,pro版本缺失

**执行方案**:
1. 从数据库查询53个source_missing的slug和对应free版本路径
2. 对每个skill:
   - 读取free版本SKILL.md
   - 生成pro版本(增强功能描述,添加付费特性)
   - 修改license为Proprietary
   - 添加付费功能说明
   - 保存到 differentiated-skills/[category]/[slug]-pro/
3. 更新数据库local_path指向新路径
4. 复制到hermes-skills/[category]/paid/
5. 运行审计确保100%A级

**验证标准**: 53个source_missing全部生成-pro版本,审计通过

### 任务3: GitHub推送恢复

**问题**: origin和hermes-skills仓库推送均失败(Connection reset)

**执行方案**:
1. 检查网络连接
2. 配置Git:
   ```
   git config http.postBuffer 524288000
   git config http.lowSpeedLimit 0
   git config http.lowSpeedTime 999999
   ```
3. 推送origin (私有备份)
4. 推送hermes-skills (公开引流) — 包含759免费+459付费=1218
5. 如果持续失败,尝试SSH协议或分批推送

**验证标准**: 两个仓库均推送成功

### 任务4: ClawHub定时任务监控

**问题**: ClawHub定时任务(73efabe0)已创建但0次执行,下次运行7/25 12:00北京

**执行方案**:
1. 等待定时任务首次执行(7/25 12:00)
2. 执行后检查:
   - Schedule get 73efabe0 查看执行记录
   - 检查upload_tracking.json中ch_published数量变化
   - 验证VERSION_EXISTS和protected namespace错误处理
3. 如果定时任务执行失败:
   - 诊断失败原因
   - 修复clawhub_batch_uploader.py
   - 手动触发一次(trigger)测试

**验证标准**: ClawHub published数量从228增长

### 任务5: 源skill发现与扩展 — 从多平台获取新skill

**问题**: 当前110个源skill全部来自clawhub,需扩展来源

**执行方案**:
1. 检查GitHub高星项目中的skill定义:
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

### 任务6: hermes-skills前端可见性优化

**问题**: hermes-skills仓库已提交但未推送成功,且README需优化引流效果

**执行方案**:
1. 推送hermes-skills到GitHub(任务3完成后)
2. 检查README.md的三语版本数据是否准确
3. 添加SkillHub和ClawHub的引流链接
4. 添加付费skill的购买引导(SkillPay链接)
5. 优化SEO(关键词、描述)
6. 添加Star引导和Issue模板

**验证标准**: hermes-skills推送成功,README含引流链接

### 任务7: 审计维护 — 确保L4-L9持续100%A级

**执行方案**:
1. 运行 `python tools/deep_quality_audit.py`
2. 检查L4-L9各层级结果
3. 如有非A级,立即修复
4. 生成审计报告

**验证标准**: L4-L9全部100%A级

### 任务8: Git提交与下一轮提示词生成

**执行方案**:
1. 提交所有变更到本地git
2. 推送到origin和hermes-skills
3. 生成 next-round-prompt-v53.0.md
4. 更新ARCHITECTURE.md中的平台策略表

## 验证检查清单

- [ ] SkillHub COS同步修复,40个org_only技能发布成功
- [ ] SkillHub前台至少10个技能可搜索到
- [ ] 53个缺失付费skill生成-pro版本
- [ ] GitHub origin推送成功
- [ ] GitHub hermes-skills推送成功
- [ ] ClawHub定时任务首次执行成功
- [ ] 源skill新增50+(从GitHub/dify/n8n)
- [ ] hermes-skills README含引流链接
- [ ] L4-L9审计100%A级
- [ ] 下一轮提示词v53.0生成

## 约束

1. **增强已有代码** — 所有修复功能集成到现有工具脚本，不创建碎片化新文件
2. **不模拟/mock** — 所有文件修改和数据库操作必须真实执行
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏现有命令功能
5. **内容保真** — tags增强和value proposition增强不得改变技能原有语义和功能
6. **网络容错** — GitHub推送失败不应阻塞其他任务的执行
7. **质量底线** — 不得引入任何会降低L4-L9审计等级的修改(当前100%A级)
8. **付费skill保护** — hermes-skills中的付费skill应与clawhub付费版一致，不得将全部付费skill开源
9. **分类统一** — 本地分类目录=skillhub分类=clawhub分类=hermes-skills分类
10. **版本同步** — 本地skill版本升级后，必须同步到全部3个平台的对应skill
11. **SkillHub优先** — SkillHub前台可见性是最高优先级，COS同步问题阻断引流和赚钱
12. **COS重试策略** — 如COS持续失败,每日重试一次,并记录重试日志
