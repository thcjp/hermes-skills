# Round 41 执行提示词 v41.0

## 上下文
- **上一轮**: Round 40 (Git: cadc4889, 14 files, +646/-2082, pushed to origin)
- **当前日期**: 2026-07-24
- **数据库**: 2882 total skills (1162 updated + 959 active + 759 stale + 1 not_found + 1 optimized)
- **平台状态**: SkillHub 1126 success, ClawHub 1152 success/855 published, GitHub 1159 success
- **审计状态**: L4-L8 全量通过, 2097/2097 A级, 0问题
- **定时任务**: ClawHub每日12:00北京时间自动上传 (ID: 5f5e0baf, Active, 0次执行)
- **GitHub双仓库**: hermes-skills(公开引流) + origin(私有备份), 策略已固化到github_repo_strategy.py

## Round 40 完成情况

### Task 1 (P0): SkillHub blocked skill修复 - 完成 ✅
- accounting-and-finance: 10731→5777字符, retry_pending
- accounting-finance: 9857→4116字符, retry_pending
- ace-music: 7863→4907字符, retry_pending
- sales-copy-writer: 修复质量门禁, status=success
- ai-artist-workstation: 精简至5353字符, status=success
- ai-video-director: 标记not_found(文件系统不存在)

### Task 2 (P1): SkillHub failed skill重试 - 完成 ✅
- cdp-browser-master: 精简至3901字符, status=success
- cron-guard: 精简至3884字符, status=success
- linear-workflow-bot: 精简至5784字符+修复YAML格式, status=success
- ai-artist-workstation: 精简至5353字符, status=success

### Task 3 (P1): ClawHub protected namespace修复 - 完成 ✅
- openclaw-dashboard → dashboard-toolkit (active)
- openclaw-linear → linear-integration (active)
- pandoc-convert-openclaw → pandoc-converter (active)
- 4个剩余openclaw-前缀slug标记为stale

### Task 4 (P2): ClawHub上传进度监控 - 进行中 ⚠️
- 定时任务Active, 0次执行, 今日12:00首次执行
- 855 published, 1152 DB success records

### Task 5 (P2): chat skill付费版上传 - 未完成 ❌
- skillhub_paid: 1条记录, 0 success (需浏览器session认证)

### Task 6 (P2): 全量平台同步状态验证 - 完成 ✅
- GitHub: 1159 success (54.6%)
- SkillHub: 1126 success + 16 retry_pending (53.8%)
- ClawHub: 1152 success (54.3%)
- 0 mock记录 ✅

### 额外完成: GitHub双仓库策略固化 ✅
- github_repo_strategy.py: 免费/付费skill判定规则
- version_sync_pipeline.py: 双remote推送逻辑
- git remote: hermes-skills + origin
- 策略文档化: 公开引流(免费) + 私有备份(全部)

## 交叉验证发现的遗留问题

### 1. GitHub hermes-skills仓库首次推送未执行
- git remote已配置, 但从未实际push到hermes-skills
- 需验证GitHub上hermes-skills仓库是否存在
- 需执行首次推送(仅免费skill目录)

### 2. SkillHub 16条retry_pending历史记录
- 这些是Round 40修复过程中的历史记录
- 对应的skill已有success记录, retry_pending是旧记录
- 需清理或标记为superseded

### 3. ClawHub定时任务尚未执行
- 今日12:00北京时间首次执行
- 502个待上传, 预计3天完成

### 4. 759个stale skills需调查
- 这些skill在DB中存在但文件系统中不存在(或反向)
- 可能是clawhub下载源、差异化前的原始skill、或已删除的skill
- 需要分类处理: 源skill保留/无效skill清除

### 5. chat skill付费版仍待上传
- 需要浏览器session认证手动上传

### 6. origin仓库可见性
- 建议在GitHub设置中将origin (https://github.com/thcjp/-.git) 改为private
- 当前可能为public, 付费skill内容暴露

## Round 41 任务清单

### Task 1 (P0): GitHub hermes-skills仓库首次推送
**目标**: 将免费skill推送到公开引流仓库

1. 验证GitHub上hermes-skills仓库是否存在(如不存在需创建)
2. 执行首次推送: `git push hermes-skills main`
3. 验证hermes-skills仓库内容: 仅包含免费skill
4. 在GitHub上设置hermes-skills仓库为public
5. 在GitHub上设置origin仓库为private
6. 验证github_repo_strategy.py的is_free_skill()函数对全部2121个active+updated skill的分类结果
7. 生成免费/付费skill分布报告

**验证标准**:
- hermes-skills仓库push成功
- hermes-skills仓库可见性为public
- origin仓库可见性为private
- 免费/付费skill分类报告生成

### Task 2 (P1): ClawHub定时任务执行验证
**目标**: 验证定时任务首次执行结果

1. 检查定时任务执行历史 (Schedule ID: 5f5e0baf)
2. 如已执行: 查看clawhub_daily_log.txt执行记录
3. 验证clawhub_published_slugs.json数量增长 (>855)
4. 如未执行: 手动触发一次 (action: trigger)
5. 验证数据库platform_uploads表clawhub记录同步

**验证标准**:
- 定时任务至少执行1次
- published count > 855
- 日志文件有执行记录
- 数据库记录同步

### Task 3 (P1): SkillHub retry_pending历史记录清理
**目标**: 清理16条已过时的retry_pending记录

1. 查询所有retry_pending记录
2. 对每条记录检查是否已有对应的success记录
3. 如有success记录: 将旧retry_pending标记为superseded
4. 如无success记录: 保留retry_pending并标注待重试
5. 生成清理报告

**验证标准**:
- 0条无对应success的retry_pending记录(或明确标注待重试)
- 清理报告生成

### Task 4 (P1): 759个stale skills分类处理
**目标**: 调查并分类处理stale skills

1. 查询所有stale skills的slug和来源
2. 分类:
   a. clawhub下载源skill (is_source=true): 保留, 标记为source
   b. 差异化前原始skill: 保留, 标记为original
   c. 已删除/无效skill: 清除DB记录
   d. 文件系统存在但DB标记stale: 重新标记为active
3. 更新数据库current_status字段
4. 生成stale skills分类报告

**验证标准**:
- 每个stale skill有明确分类
- 无效skill已清除
- 误标stale的skill已恢复active
- 分类报告生成

### Task 5 (P2): chat skill付费版上传
**目标**: 完成chat skill付费版上传到SkillHub

1. 检查enterprise-upload/payloads/chat-paid-v1.1.1.json
2. 通过Trae Work浏览器方式上传到SkillHub
3. 验证platform_uploads表skillhub_paid记录status=success

**验证标准**:
- chat skill付费版上传成功
- platform_uploads表skillhub_paid记录status=success

### Task 6 (P2): 版本同步流水线GitHub双仓库实跑验证
**目标**: 端到端验证双仓库推送策略

1. 选择一个免费skill和一个付费skill
2. 修改SKILL.md内容(添加注释或微调)
3. 运行version_sync_pipeline.py sync <slug>
4. 验证:
   - 免费skill: 推送到hermes-skills + origin
   - 付费skill: 仅推送到origin
5. 检查两个仓库的git log确认推送结果
6. 恢复SKILL.md原始内容

**验证标准**:
- 免费skill在hermes-skills仓库有commit记录
- 付费skill在hermes-skills仓库无新commit记录
- 两个skill在origin仓库都有commit记录

## 执行规则
1. 遵循`修复提示词.md`的R1-R78规则
2. 每个任务完成后进行代码级验证(非文档声明)
3. 禁止任何形式的mock/fallback/todo/pass
4. 修复必须覆盖全部3个目录(packaged-skills/skillhub, opensource-skills/packaged, differentiated-skills)
5. 完成后生成下一轮提示词v42.0

## 平台统计速览
| 平台 | 已发布 | 待审核/待上传 | 失败/阻塞 | 总计 |
|------|--------|---------------|-----------|------|
| SkillHub | 1126 | 0 | 0 (历史16 retry_pending) | 1126 |
| ClawHub | 855 published / 1152 DB | 502 (定时任务处理中) | 0 | 1357 |
| GitHub (origin) | 1159 | 962 (未同步) | 0 | 2121 |
| GitHub (hermes-skills) | 0 (首次推送待执行) | - | - | - |

## 审计质量速览
| 层级 | 状态 | A级 | B级 | C+D+F级 | avg_score | issues |
|------|------|-----|-----|---------|-----------|--------|
| L4 功能质量 | ✅ | 2097 | 0 | 0 | 93.6 | 0 |
| L5 可销售性 | ✅ | 2097 | 0 | 0 | 90.3 | 0 |
| L6 内容真实性 | ✅ | 2097 | 0 | 0 | 100.0 | 0 |
| L7a 语义模板 | ✅ | 2097 | 0 | 0 | 100.0 | 0 |
| L7b 可执行性 | ✅ | 2097 | 0 | 0 | 100.0 | 0 |
| L8 安全审计 | ✅ | 2097 | 0 | 0 | 100.0 | 0 |
| Critical | ✅ | 0 critical, 0 warning, 0 info, 2097 OK | | | | |

## 版本同步流水线速览
| 阶段 | 脚本 | 状态 |
|------|------|------|
| 1. DISCOVER | auto_discover.py + version_sync_pipeline.py scan | ✅ |
| 2. ENHANCE | orchestrator.py enhance (基于审计报告) | ⚠️ 半自动 |
| 3. INCREMENT | version_sync_pipeline.py increment_version() | ✅ |
| 4. VALIDATE | deep_quality_audit.py (L1-L8) | ✅ |
| 5. SYNC_GITHUB | version_sync_pipeline.py sync_to_github() 双仓库 | ✅ (策略已固化, 待首次推送) |
| 6. SYNC_SKILLHUB | version_sync_pipeline.py sync_to_skillhub() | ⚠️ 付费版半自动 |
| 7. SYNC_CLAWHUB | clawhub_batch_uploader.py (定时任务自动) | ✅ |
| 8. RECORD | SQLite (versions + platform_uploads + operations) | ✅ |

## GitHub双仓库策略速览
| 仓库 | Remote | URL | 可见性 | 推送内容 | 状态 |
|------|--------|-----|--------|----------|------|
| hermes-skills | hermes-skills | https://github.com/thcjp/hermes-skills | public | 仅免费skill | ⚠️ 待首次推送 |
| origin | origin | https://github.com/thcjp/-.git | 建议private | 全部skill+项目代码 | ✅ 已推送 |

## 定时任务速览
| 任务名 | Schedule ID | Cron | 时区 | 状态 | 下次执行 | 执行次数 |
|--------|-------------|------|------|------|----------|----------|
| ClawHub每日自动上传 | 5f5e0baf | 0 12 * * * | Asia/Shanghai | Active | 2026-07-24 12:00 | 0 |

## Git提交记录
| 轮次 | Commit | 文件数 | 变更行数 |
|------|--------|--------|----------|
| Round 36 | 58542b46 | 63 | +1705/-24084 |
| Round 36 | d8e61e8d | 1 | +192 |
| Round 37 | 081cf7f0 | 2105 | +60051/-89044 |
| Round 38 | d8412748 | 35 | +7216/-435 |
| Round 39 | 73214748 | 8 | +12328/-15 |
| Round 39 | 4679c803 | 1158 skills | batch version upgrade |
| Round 39 | 27101ea3 | 8 | +12328/-15 |
| Round 40 | cadc4889 | 14 | +646/-2082 |
