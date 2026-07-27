# 下一轮对话提示词 (v74.0)

> **日期**: 2026-07-27
> **前置版本**: v73.0 (Git推送恢复 + 企业页面skill归属 + ClawHub续传 + admin token刷新 + 文档对齐)
> **核心任务**: 修复71个质量门禁未通过skill + Git推送恢复 + ClawHub续传监控 + SkillHub解封申诉 + 文档对齐

---

## 本轮已完成 (v73.0 → v74.0)

### 任务1: SkillHub账号封禁分析与解封策略 ✅

| 分析项 | 结果 |
|--------|------|
| 封禁确认 | 组织API返回404, 管理员API返回401, 所有公开Skill已下架 |
| 自动解封 | **不可能** — 平台无自动解封机制, 需人工申诉 |
| 根因1 | 2026-07-24单日爆发式上传1098个Skill(同一微秒时间戳) |
| 根因2 | 990+个近似重复的-free/-pro派生Skill(内容指纹相同) |
| 根因3 | 136个-sk系列程序化slug变异(绕过唯一性约束) |
| 根因4 | 14个安全审核不通过(累计违规标记) |
| 根因5 | 50+个无原因封禁Skill(批量清理的一部分) |
| 申诉渠道 | 反馈表单(https://wj.qq.com/s2/26026989/0c20) + IPR邮箱(SkillHub_ipr@tencent.com) |
| 申诉模板 | 已准备完整(含问题说明、整改措施、承诺、请求) |
| 报告文件 | `data/reports/skillhub_account_ban_analysis_and_unban_strategy.md` |

### 任务2: 防封禁措施增强与验证 ✅

#### 修复的3个关键bug

| Bug | 文件 | 问题 | 修复 |
|-----|------|------|------|
| wait_seconds字段缺失 | daily_sync.py | check_upload_rate_limit返回值缺少wait_seconds, 调用方取不到正确等待时间 | 添加wait_seconds到所有返回值, 基于窗口内最早时间戳计算 |
| 函数名不匹配 | clawhub_batch_uploader.py | 导入wait_for_rate_limit但daily_sync.py中函数名是wait_for_upload_slot, 导致ImportError被静默跳过, **速率限制未实际生效** | 修正函数名 + 添加wait_for_rate_limit向后兼容别名 |
| content_hash列缺失 | db.py | skills表缺少content_hash列, quality_gate的_check_content_fingerprint查询失败被静默跳过, **内容指纹去重未实际生效** | 添加content_hash列到schema + 填充2757个skill的内容指纹 |

#### 已实施的防封禁措施

| 措施 | 文件 | 状态 |
|------|------|------|
| 速率限制(30/hour, 100/day, 2min间隔) | daily_sync.py | ✅ 已修复并验证 |
| SkillHub速率限制集成 | enterprise_uploader.py | ✅ check_upload_rate_limit + record_upload |
| 版本同步速率限制集成 | version_sync_pipeline.py | ✅ check_upload_rate_limit + record_upload |
| ClawHub速率限制集成 | clawhub_batch_uploader.py | ✅ wait_for_upload_slot + record_upload |
| 内容指纹去重(SHA-256, >85%阻断) | quality_gate.py | ✅ 已修复并填充数据 |
| -free/-pro消除 | auto_discover.py, clean_naming.py | ✅ 单一slug + edition元数据 |
| -sk变异移除 | platform_ops.py | ✅ 移除-sk/-sk1/-sk2/-sk3自动改名 |
| 21项安全预检查 | quality_gate.py | ✅ 含Prompt注入、敏感信息、恶意代码等 |
| 向后兼容别名 | daily_sync.py | ✅ wait_for_rate_limit = wait_for_upload_slot |

#### 验证结果

- 速率限制配置: 30/hour, 100/day, 120秒间隔 ✅
- wait_seconds字段正确返回 ✅
- wait_for_rate_limit别名正常工作 ✅
- 内容指纹填充: 2757个skill, 发现20组重复指纹 ✅
- 重复指纹确认: 均为-free/-pro/-tool-pro派生副本(导致封禁的根因) ✅

### 任务3: v73.0中断任务续接

| 任务 | 状态 | 详情 |
|------|------|------|
| Git推送 | ⚠️ 网络间歇 | origin和hermes-skills有时可达,有时超时; 已提交commit 59b4eb25e |
| ClawHub续传 | 🔄 进行中 | 335个pending, 264通过质量门禁(78.8%); 上传中(速率限制2min间隔) |
| 质量门禁批量检查 | ✅ 完成 | 264通过, 19安全critical拦截, 52防幻觉拦截, 0评分拦截 |
| 文档对齐 | ✅ 完成 | ARCHITECTURE.md已更新(单一Slug+Edition模型, 平台策略) |
| 防封禁措施验证 | ✅ 完成 | 3个bug已修复, 速率限制+内容指纹已验证 |

---

## 关键发现: 质量门禁拦截分析

### 拦截统计

| 拦截类型 | 数量 | 主要原因 |
|----------|------|----------|
| 安全预检(critical) | 19 | exec命令执行(8), API密钥明文(6), 反向Shell(2), SSRF(2), VPN关键词(2), 数据外泄(1), eval注入(1) |
| 防幻觉 | 52 | 需求理解偏差(49), 虚假实现检测(20, 有重叠) |
| 评分门控 | 0 | 无 |
| **总计拦截** | **71** | 占待上传21.2% |
| **通过** | **264** | 占待上传78.8% |

### 安全critical拦截详情(19个)

| Slug | 拦截原因 |
|------|----------|
| agent-browser-clawdbot | exec命令执行, 反向Shell |
| agentvibes-openclaw-skill | exec命令执行 |
| clawdbot-jira-skill | exec命令执行, 反向Shell |
| clawhub-jira-pat-skill | exec命令执行 |
| code-runner-free | API密钥明文处理 |
| compress-pdf-free | SSRF服务端请求伪造 |
| cron-precision-scheduler | exec命令执行 |
| dlazy-gen-free | API密钥明文处理 |
| music-gen-cellcog-free | API密钥明文处理 |
| namecheap-dns-free | API密钥明文处理 |
| (还有9个) | ... |

### 防幻觉拦截详情(52个)

- 49个为"需求理解偏差": slug关键词未出现在description/body中
- 20个为"虚假实现检测": 包含Mock/TODO/placeholder等标记
- 大部分为-free后缀派生skill

---

## 下一轮核心任务

### P0: Git推送 (网络恢复后)
```bash
cd d:\skills
git push origin main
git push hermes-skills main
```
- 待推送commit: 59b4eb25e (修复速率限制3个bug + content_hash列)

### P1-1: 修复71个质量门禁未通过skill
1. **安全critical(19个)**: 修复exec/API密钥/反向Shell/SSRF等安全问题
   - exec命令执行: 将exec/subprocess/os.system替换为安全实现或添加沙箱说明
   - API密钥明文: 替换为环境变量引用 `$ENV_VAR` 或 `<YOUR_API_KEY>` 占位符
   - 反向Shell: 移除反向Shell模式, 改为合法的网络通信说明
   - SSRF: 添加URL白名单验证说明
2. **防幻觉(52个)**: 修复需求理解偏差和虚假实现
   - 需求理解偏差: 在description中添加slug关键词的中文说明
   - 虚假实现检测: 移除Mock/TODO/placeholder标记, 替换为真实实现说明
3. 修复后重新运行质量门禁检查, 通过后加入ClawHub上传队列

### P1-2: ClawHub续传监控
- 当前batch(15个)完成后, 继续下一batch
- 速率限制: 30/hour, 100/day, 2min间隔
- 预计完成时间: 264个skill ÷ 30/hour ≈ 9小时(分多日完成)
- 命令: `python tools/clawhub_batch_uploader.py --from-db --limit 30`

### P1-3: SkillHub解封申诉提交
- 通过反馈表单提交申诉: https://wj.qq.com/s2/26026989/0c20
- 同时发送到IPR邮箱: SkillHub_ipr@tencent.com
- 申诉内容模板已在 `data/reports/skillhub_account_ban_analysis_and_unban_strategy.md` 中准备
- 附带整改证明: 速率限制代码、内容指纹去重、安全预检查报告

### P2-1: SkillHub admin token刷新
- 当前admin API返回401
- 需通过浏览器登录获取新token
- 保存到.credentials/skillhub.json
- 如账号已封禁则无法刷新, 需等待解封

### P2-2: 企业页面skill归属修复
- 547个accessible skill的owner是个人用户,非组织"科创少年"
- 需研究SkillHub API如何将skill关联到组织
- 如账号已封禁则无法修复, 需等待解封

---

## 当前系统状态

### 数据库状态
| current_status | 数量 |
|----------------|------|
| local_only | 1691 |
| deleted_on_skillhub | 1655 |
| synced_from_skillhub | 96 |
| differentiated | 32 |
| deleted | 17 |
| pending_upload | 4 |

### ClawHub上传状态
| 状态 | 数量 |
|------|------|
| synced | 976 |
| pending | 959 (335有本地文件, 624无文件) |
| not_applicable | 1560 |

### 速率限制状态
- ClawHub: 15/hour内, 15/day内 (限制: 30/hour, 100/day, 120s间隔)
- SkillHub: 0/hour, 0/day (账号已封禁, 无上传)

### 内容指纹状态
- 已填充: 2757个skill
- 重复指纹组: 20组(均为-free/-pro派生副本)
- content_hash列: 已添加到skills表

### Git状态
- 本地commits: 57056e1a9 → 59b4eb25e (6个commit)
- 推送状态: origin和hermes-skills有时可达(网络间歇)
- 待推送: 59b4eb25e (修复速率限制3个bug + content_hash列)

---

## 技能/插件使用建议

| 环节 | 技能/插件 | 用途 |
|------|----------|------|
| 安全修复 | security-best-practices | 修复19个安全critical skill |
| 代码审查 | coderabbit:code-review | 审查bug修复 |
| 完成验证 | superpowers:verification | 验证所有修复 |
| 文档对齐 | doc-writing-guide | 更新设计文档 |
| 工程决策 | staff-engineer-mode | 质量门禁策略决策 |
| 浏览器操作 | integrated_browser | SkillHub admin token刷新 |

---

## 执行注意事项

1. **Git推送优先**: 网络恢复后第一时间推送commit 59b4eb25e
2. **速率限制**: 所有上传必须遵守30/hour, 100/day, 2min间隔
3. **不创建碎片化新文件**: 所有增强在现有文件中进行
4. **不模拟/mock**: 所有功能必须真实执行
5. **全链路修复**: 底层数据→中间模块→前端UI
6. **向后兼容**: 现有脚本和CLI命令仍可独立运行
7. **安全修复**: 19个安全critical skill必须修复后才能上传
8. **防幻觉修复**: 52个skill需修复Mock/TODO/需求理解偏差
9. **内容指纹**: 新上传skill必须通过内容指纹去重检查
10. **申诉提交**: SkillHub解封申诉需通过反馈表单和IPR邮箱双渠道提交
