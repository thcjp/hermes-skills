# 第47轮提示词 (v47.0) — L9深度质量提升 + 阻塞任务恢复 + 审计报告结构修复

> **日期**: 2026-07-24
> **上一轮完成**: V46 — L8/L9批量修复2137个skill, L8 100%通过, L9 96% A+B合格率 (commit 1034ee20)
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库

## V46完成总结

| 任务 | 状态 | 结果 |
|------|------|------|
| L8 DUPLICATE_YAML_FIELDS修复 | ✅ | 2090→0 |
| L8 TAG_MISMATCH修复 | ✅ | 1421→0 |
| L9 INSUFFICIENT_SUMMARY修复 | ✅ | 1800→0 |
| L9 MISSING_QUICK_START修复 | ✅ | 1091→0 |
| L9 A+B合格率 | ✅ | 38%→96% (91.6分) |
| fix_missing_fields.py增强 | ✅ | 新增fix_frontmatter_separators/segment-based duplicate YAML/expand_summary/add_quick_start |
| auto_publish.py增强 | ✅ | npx skillhub集成 + CLI_NO_PUBLISH错误检测 |
| Git提交 | ✅ | commit 1034ee20 (2145文件, +114280/-125475) |
| 8个retry_pending技能重试 | ⚠️ 阻塞 | skillhub CLI v0.4.1无publish命令, 用户未登录SkillHub |
| hermes-skills推送 | ⚠️ 阻塞 | GitHub不可达(TCP 443连接失败) |
| origin推送 | ⚠️ 阻塞 | GitHub不可达 |

## V46审计最终结果

### L7b 可执行性审计 (2097 skills)
| 指标 | 值 |
|------|-----|
| 平均分 | 99.9/100 |
| A级 | 2094 |
| B级 | 2 |
| C级 | 0 |
| D级 | 0 |
| F级 | 1 (cron-guard: L7B_NO_CODE) |

### L8 安全审计 (2097 skills)
| 指标 | 值 |
|------|-----|
| 平均分 | 100.0/100 |
| A级 | 2097 (100%) |
| 安全问题总数 | 0 |

### L9 可见性质量预检 (2097 skills)
| 指标 | 值 |
|------|-----|
| 平均分 | 91.6/100 |
| A级 | 1098 (52%) |
| B级 | 918 (44%) |
| C级 | 81 (4%) |
| D级 | 0 |
| A+B级合格率 | 96% (2016/2097) |

| 剩余问题类型 | 触发数 | 修复方向 |
|----------|--------|----------|
| MISSING_OR_IRRELEVANT_TAGS | 788 | tags与内容相关性不足,需基于slug/category/body重新推断 |
| MISSING_VALUE_PROPOSITION | 292 | description缺少价值命题关键词(如"提升/节省/自动化/分析/生成") |
| INSUFFICIENT_SUMMARY | 0 | 已修复 |
| MISSING_QUICK_START | 0 | 已修复 |
| INVALID_CATEGORY | 0 | 已修复 |

### 平台状态
| 平台 | 成功 | 待重试 | 失败/取消 |
|------|------|--------|----------|
| SkillHub | 1120 | 8 (retry_pending) | 1 (cancelled) |
| ClawHub | 1152 | 1 (retry_pending) | 2 (fail) |

### 三轨模型
| 轨道 | 数量 |
|------|------|
| 免费增强版 | 1519 |
| 付费增强版 | 1158 |
| 总计 | 2677 |

## 实施任务

### 任务1: GitHub推送恢复 (阻塞任务)

**问题**: V46提交(commit 1034ee20)因GitHub不可达未能推送到origin和hermes-skills

**实现**:
1. 检测GitHub连通性: `Test-NetConnection github.com -Port 443`
2. 连通后执行: `git push origin main` (私有备份,全量)
3. 连通后执行: `git push hermes-skills main` (公开引流,全量)
4. 如持续不可达,设置定时重试(每30分钟检测一次)

### 任务2: 8个retry_pending技能浏览器上传 (阻塞任务)

**问题**: skillhub CLI v0.4.1无publish命令, Admin API需浏览器cookie认证

**8个技能列表**:
- cdp-browser-master, cron-guard, linear-workflow-bot
- ai-artist-workstation, sales-copy-writer
- accounting-and-finance, accounting-finance, ace-music

**实现**:
1. 用户登录 https://www.skillhub.cn (微信/手机登录)
2. 导航到"发布Skill"页面
3. 逐个上传8个技能的SKILL.md文件
4. 上传成功后更新数据库: `UPDATE platform_uploads SET upload_status='success' WHERE slug IN (...)`

**替代方案**: 增强auto_publish.py的generate_community_publish_js(),生成包含SKILL.md内容的上传JS脚本

### 任务3: L9 MISSING_OR_IRRELEVANT_TAGS修复 (788个skill)

**问题**: tags字段与skill内容相关性不足(匹配率<50%)

**修复方案**: 增强 `fix_missing_fields.py` 的 `infer_tags()` 函数:
1. 读取skill的slug、category、body前2000字符
2. 基于TAG_TO_CATEGORY_MAP反向映射,从内容关键词推断tags
3. 确保至少3个tags与body内容有直接匹配
4. 保留原有有效tags,补充缺失的相关tags

**验证**: 运行deep_quality_audit.py, 确认MISSING_OR_IRRELEVANT_TAGS从788降至<100

### 任务4: L9 MISSING_VALUE_PROPOSITION修复 (292个skill)

**问题**: description缺少价值命题关键词

**价值命题关键词库**:
- 效率类: 提升/节省/加速/自动化/优化/简化
- 能力类: 分析/生成/转换/处理/监控/管理
- 专业类: 企业级/专业/智能/深度/全面
- 场景类: 适用/支持/覆盖/内置

**修复方案**: 增强 `fix_missing_fields.py` 添加 `enhance_value_proposition()` 函数:
1. 读取description字段
2. 检测是否包含至少1个价值命题关键词
3. 如缺失,从body的核心能力章节提取关键动词,补充到description末尾
4. 保持description语义不变,仅增强价值表述

### 任务5: L7b cron-guard F级修复

**问题**: cron-guard声明有脚本但正文中无代码块(L7B_NO_CODE)

**修复方案**:
1. 读取cron-guard的SKILL.md
2. 检查是否确实需要代码块(如描述中提到脚本/cron/命令)
3. 如需要,添加标准化的cron配置代码块示例
4. 如不需要(纯指令型skill),修改描述去除"脚本"相关表述

### 任务6: 审计报告JSON结构修复

**问题**: deep_quality_audit_report.json的layer9/layer8/layer7b字段返回None

**修复方案**:
1. 检查deep_quality_audit.py的报告生成逻辑
2. 确保report字典使用正确的key名(layer9_summary而非layer9)
3. 验证JSON结构可被外部脚本正确解析

### 任务7: ClawHub剩余3个问题技能处理

**问题**: 1个retry_pending + 2个fail

**实现**:
1. 查询3个技能的slug和错误信息
2. 修复错误内容(如VERSION_EXISTS需递增版本号)
3. 执行: `npx clawhub publish <skill_dir> --changelog "Retry after fix"`
4. 更新数据库状态

## 验证检查清单

- [ ] GitHub推送成功(origin + hermes-skills)
- [ ] 8个retry_pending技能上传到SkillHub(或生成可执行的浏览器上传脚本)
- [ ] L9 MISSING_OR_IRRELEVANT_TAGS从788降至<100
- [ ] L9 MISSING_VALUE_PROPOSITION从292降至<50
- [ ] L9 A+B级合格率从96%提升至98%+
- [ ] L7b cron-guard从F级修复为A级或B级
- [ ] 审计报告JSON结构正确可解析
- [ ] ClawHub 3个问题技能处理完成
- [ ] Git提交完成

## 约束

1. **不创建新文件** — 所有修复功能集成到现有 `fix_missing_fields.py` 和 `deep_quality_audit.py`
2. **不模拟/mock** — 所有文件修改和数据库操作必须真实执行
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏现有命令功能
5. **内容保真** — tags增强和value proposition增强不得改变技能原有语义和功能
6. **网络容错** — GitHub推送失败不应阻塞其他任务的执行
