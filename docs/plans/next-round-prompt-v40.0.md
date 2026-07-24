# Round 40 执行提示词 v40.0

## 上下文
- **上一轮**: Round 39 (Git: 73214748, 8 files, +12328/-15)
- **当前日期**: 2026-07-24
- **数据库**: 2874 skills total (2122 active + 752 stale), 文件系统2122 SKILL.md
- **平台状态**: SkillHub 1126 success, ClawHub 530 success/~827 pending, GitHub 2 records
- **审计状态**: L4-L8 全量通过, 2097/2097 A级, 0问题

## Round 39 完成情况

### Task 1 (P0): ClawHub剩余skill上传 - 阻塞 ⚠️
- 限流窗口: 200/24h, 上次上传2026-07-24T03:27:59
- 限流重置: 约2026-07-25 03:28 (北京时间)
- 当前已发布: 530 (DB) / 855 (checkpoint)
- 剩余约502个待上传, 需至少3轮(502/200≈3)
- 上传命令: `python clawhub_batch_uploader.py --resume --limit 200`

### Task 2 (P1): 数据库skill数量对齐 - 完成 ✅
- 扫描文件系统: 2122个唯一slug (2137个SKILL.md文件)
- 导入缺失skill: 957个新skill录入数据库
- 标记stale记录: 752个过期skill标记为stale
- 最终状态: 2874 total = 2122 active + 752 stale
- active(2122) = 文件系统(2122) ✅

### Task 3 (P1): 版本同步流水线首次实跑验证 - 完成 ✅
- 扫描变更: 1177个skill检测到hash变更(之前审计轮次修改未同步版本)
- 端到端测试: `chat` skill v1.1.0→v1.1.1
  - ✅ 变更检测: hash 00d5bcd1→1f877016
  - ✅ 版本递增: 1.1.0→1.1.1
  - ✅ 质量门禁: 13/13通过
  - ✅ GitHub push: commit 22be3975 成功
  - ⚠️ SkillHub: CLI返回failed(需检查CLI可用性)
  - ✅ SkillHub付费版: payload生成成功
  - ⚠️ ClawHub: 跳过(限流中)
  - ✅ 数据库记录: versions + operations + platform_uploads
- 修复3个bug:
  - sync_to_skillhub: None空值处理(free_upload初始化为None导致.get()失败)
  - sync_to_clawhub: 从batch_uploader(参数错误)改为npx clawhub直接上传
  - sync_to_github: 增加platform_uploads记录(之前遗漏) + push超时60s→180s

### Task 4 (P1): orchestrator.py验证 - 完成 ✅
- `orchestrator.py status` 运行正常
- 显示: 2874 skills, ClawHub 530 success, SkillHub 1126 success
- 审计状态: L4-L8全A级, 2097/2097
- ClawHub限流: 剩余19.8h重置
- full-run未执行(1177个变更skill批量同步不实际,需分批处理)

### Task 5 (P2): 版本同步流水线文档化 - 完成 ✅
- 创建 `docs/version-sync-pipeline.md`
- 包含: 架构图、8阶段说明、脚本依赖、数据流、使用方式
- 包含: 已知限制(6项)、灾难恢复(版本回滚/数据库恢复/平台失败处理)
- 包含: 后续优化方向(6项)

### Task 6 (P2): ClawHub定时上传自动化 - 待创建 ⏳
- 计划: 每日12:00(北京时间)执行ClawHub上传200个
- 上传命令: `python clawhub_batch_uploader.py --resume --limit 200`
- 完成条件: published >= 1357时删除定时任务
- 状态: 定时任务创建超时,需重试

## 版本同步流水线状态

| 阶段 | 脚本 | 状态 | 验证结果 |
|------|------|------|----------|
| 1. DISCOVER | auto_discover.py + scan | ✅ | 1177个变更检测正确 |
| 2. ENHANCE | orchestrator.py enhance | ⚠️ | 半自动(识别自动,增强需AI) |
| 3. INCREMENT | increment_version() | ✅ | 1.1.0→1.1.1 正确 |
| 4. VALIDATE | deep_quality_audit.py | ✅ | 13/13门禁通过 |
| 5. SYNC_GITHUB | sync_to_github() | ✅ | push成功+记录完整 |
| 6. SYNC_SKILLHUB | sync_to_skillhub() | ⚠️ | CLI失败,付费payload正常 |
| 7. SYNC_CLAWHUB | sync_to_clawhub() | ⚠️ | 限流中,代码已修复 |
| 8. RECORD | SQLite | ✅ | versions+operations+platform_uploads |

## 交叉验证发现的遗留问题

### 1. ClawHub 502个待上传 (最高优先级)
- 限流: 200/24h, 重置约2026-07-25 03:28
- 需3轮上传, 预计3天完成
- 需创建定时任务自动化

### 2. 1177个skill版本待同步
- 原因: 之前审计轮次修改了SKILL.md但未递增版本号
- 影响: version_sync_pipeline.py scan检测到大量变更
- 解决: 分批执行sync-all或设置定时同步

### 3. SkillHub CLI不可用
- skillhub publish命令返回failed
- 需检查CLI是否安装和认证状态
- 付费版payload生成正常

### 4. GitHub网络不稳定
- push操作偶尔失败(Connection reset/timeout)
- 已设置180秒超时
- 建议网络稳定时批量push

### 5. 数据库stale记录处理
- 752个stale记录(在DB但不在文件系统)
- 可能是重命名/删除的旧skill
- 需确认是否物理删除或保留历史

## Round 40 任务清单

### Task 1 (P0): ClawHub剩余skill上传 + 定时任务
**目标**: 创建定时任务并完成首批上传

1. 检查ClawHub限流是否已重置(距上次上传>24h)
2. 创建定时任务: 每日12:00(北京时间)执行 `python clawhub_batch_uploader.py --resume --limit 200`
3. 如限流已重置,立即执行首批200个上传
4. 上传完成后同步clawhub_published_slugs.json和数据库platform_uploads表
5. 验证ClawHub published count增长

**验证标准**:
- 定时任务已创建(cron: 0 12 * * *, timezone: Asia/Shanghai)
- ClawHub published count >= 730 (530+200)
- platform_uploads表clawhub success记录数增长

### Task 2 (P0): 1177个变更skill批量版本同步
**目标**: 将1177个变更skill的版本同步到所有平台

1. 运行 `python version_sync_pipeline.py scan` 确认变更列表
2. 分批执行同步(每批50个,避免网络超时):
   - `python version_sync_pipeline.py sync <slug> --skip-clawhub` (跳过ClawHub限流)
   - 优先同步packaged目录(39个,影响面最大)
   - 其次opensource目录
   - 最后differentiated目录
3. 每批完成后检查git log确认push成功
4. 验证数据库versions表新增1177条版本记录
5. 验证platform_uploads表github记录增长

**验证标准**:
- version_sync_pipeline.py scan 变更数减少至<100
- git log 新增1177个feat({slug})提交
- versions表新增1177条记录
- platform_uploads表github success记录>100

### Task 3 (P1): SkillHub CLI问题排查
**目标**: 修复SkillHub CLI上传失败问题

1. 检查 `skillhub --version` 是否可用
2. 检查 `skillhub whoami` 认证状态
3. 如CLI不可用,尝试 `npm install -g skillhub` 或 `npx skillhub`
4. 如认证过期,执行 `skillhub login`
5. 测试单个skill上传: `skillhub publish "d:\skills\packaged-skills\skillhub\chat" --changelog "test"`
6. 验证platform_uploads表skillhub_free success记录增长

**验证标准**:
- skillhub CLI可用且认证有效
- 至少1个skill通过CLI成功上传到SkillHub
- platform_uploads表skillhub_free新增success记录

### Task 4 (P1): 数据库stale记录处理
**目标**: 处理752个stale记录

1. 分析stale记录: 确认是否为重命名/删除/迁移
2. 对于重命名的skill: 更新slug映射关系
3. 对于已删除的skill: 标记为deleted(不物理删除,保留历史)
4. 生成stale处理报告
5. 验证数据库一致性

**验证标准**:
- stale记录处理报告生成
- 每条stale记录有明确的处理决策(重命名/删除/保留)
- 数据库skills表status字段准确反映实际状态

### Task 5 (P2): 版本同步流水线增强
**目标**: 提升流水线自动化程度

1. sync-all批量同步优化: 添加批次大小参数(--batch-size 50)
2. 失败重试机制: GitHub push失败自动重试3次
3. 进度报告: 每批完成后输出进度百分比
4. 断点续传: sync-all支持从指定slug继续
5. 同步结果汇总: sync-all完成后生成汇总报告

**验证标准**:
- `python version_sync_pipeline.py sync-all --batch-size 50` 正确分批执行
- GitHub push失败后自动重试
- 进度报告显示已完成/总数/百分比
- 断点续传从指定slug正确恢复

### Task 6 (P2): 定时自动化任务配置
**目标**: 配置完整的运维自动化定时任务

1. ClawHub每日上传: 12:00执行 `python clawhub_batch_uploader.py --resume --limit 200`
2. 版本同步每周扫描: 周一06:00执行 `python version_sync_pipeline.py scan`
3. 质量审计每周执行: 周日03:00执行 `python deep_quality_audit.py`
4. 数据库备份每日: 00:00执行 `cp skill-registry.db skill-registry.db.bak`
5. 每个任务设置完成条件(如ClawHub上传完成后删除定时任务)

**验证标准**:
- 4个定时任务已创建
- 每个任务有明确的完成条件
- 任务描述包含完整的执行指令

## 执行规则
1. 遵循`修复提示词.md`的R1-R78规则
2. 每个任务完成后进行代码级验证(非文档声明)
3. 禁止任何形式的mock/fallback/todo/pass
4. 修复必须覆盖全部3个目录(packaged-skills/skillhub, opensource-skills/packaged, differentiated-skills)
5. 完成后生成下一轮提示词v41.0

## 平台统计速览
| 平台 | 已发布 | 待审核/待上传 | 总计 |
|------|--------|---------------|------|
| SkillHub | 1126 | 0 | 1126 |
| ClawHub | 530 | ~827 | 1357 |
| GitHub | 2 | ~1175 | 1177 |

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

## 数据库统计速览
| 指标 | 数值 |
|------|------|
| 总记录 | 2874 |
| 活跃(active) | 2122 |
| 过期(stale) | 752 |
| 文件系统SKILL.md | 2122 |
| versions表 | 3520+ |
| operations表 | 9327+ |
| platform_uploads(clawhub) | 530 success |
| platform_uploads(skillhub) | 1126 success |
| platform_uploads(github) | 2 success |

## 版本同步流水线速览
| 阶段 | 脚本 | 状态 | Round 39验证 |
|------|------|------|-------------|
| 1. DISCOVER | auto_discover.py + scan | ✅ | 1177变更检测正确 |
| 2. ENHANCE | orchestrator.py enhance | ⚠️ | 半自动 |
| 3. INCREMENT | increment_version() | ✅ | 1.1.0→1.1.1正确 |
| 4. VALIDATE | deep_quality_audit.py | ✅ | 13/13门禁通过 |
| 5. SYNC_GITHUB | sync_to_github() | ✅ | push成功+记录完整 |
| 6. SYNC_SKILLHUB | sync_to_skillhub() | ⚠️ | CLI失败,付费payload正常 |
| 7. SYNC_CLAWHUB | sync_to_clawhub() | ⚠️ | 限流中,代码已修复 |
| 8. RECORD | SQLite | ✅ | 全表记录完整 |

## Git提交记录
| 轮次 | Commit | 文件数 | 变更行数 |
|------|--------|--------|----------|
| Round 36 | 58542b46 | 63 | +1705/-24084 |
| Round 36 | d8e61e8d | 1 | +192 |
| Round 37 | 081cf7f0 | 2105 | +60051/-89044 |
| Round 38 | d8412748 | 35 | +7216/-435 |
| Round 38 | 5f390079 | 1 | +1/-1 (auto-sync: accounting-and-finance v1.0.1) |
| Round 38 | 22be3975 | 1 | +1/-1 (auto-sync: chat v1.1.1) |
| Round 39 | 73214748 | 8 | +12328/-15 |
