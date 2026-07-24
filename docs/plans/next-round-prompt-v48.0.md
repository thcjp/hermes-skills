# 第48轮提示词 (v48.0) — L9剩余质量问题修复 + 平台阻塞任务恢复 + 数据库重建

> **日期**: 2026-07-24
> **上一轮完成**: V47 — L9质量大幅提升(tags+value proposition), description损坏修复(1127文件), L7a重复块修复, 根因修复fix_missing_fields.py (commit 4d1ad4536)
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库

## V47完成总结

| 任务 | 状态 | 结果 |
|------|------|------|
| L9 MISSING_OR_IRRELEVANT_TAGS修复 | ✅ | 788→161 (80%减少) |
| L9 MISSING_VALUE_PROPOSITION修复 | ✅ | 292→133 (54%减少) |
| L9 A+B合格率提升 | ✅ | 96%→99% (2087/2097) |
| L9平均分提升 | ✅ | 91.6→97.6 |
| L7a write-a-skill-free重复块修复 | ✅ | L7a 100%A, 0重复块 |
| L7b cron-guard F级修复 | ✅ | 已修复为A级 |
| description字段损坏修复 | ✅ | 1127个文件修复(\|-，可XXX提升工作效率) |
| fix_missing_fields.py根因修复 | ✅ | _replace_frontmatter_field支持block scalar |
| extract_frontmatter增强 | ✅ | 正确解析YAML列表和block scalar |
| fix_irrelevant_tags阈值对齐 | ✅ | 使用与审计相同的max(1, n//2) |
| Git提交 | ✅ | commit 4d1ad4536 (2144文件, +15080/-39718) |
| GitHub推送 | ⚠️ 阻塞 | 网络不可达,待重试 |

## V47审计最终结果

### 全层级审计概览 (2097 skills)

| 审计层 | 名称 | A级 | B级 | C级 | D/F级 | 通过率 |
|--------|------|-----|-----|-----|-------|--------|
| L4 | 功能质量 | 2097 | 0 | 0 | 0 | 100% |
| L5 | 可销售性 | 2092 | 5 | 0 | 0 | 100% |
| L6 | 内容真实性 | 2097 | 0 | 0 | 0 | 100% |
| L7a | 语义模板 | 2097 | 0 | 0 | 0 | 100% |
| L7b | 可执行性 | 2095 | 1 | 1 | 0 | 100% |
| L8 | 安全审计 | 2097 | 0 | 0 | 0 | 100% |
| L9 | 可见性质量 | 1813 | 274 | 10 | 0 | 99% A+B |

### L9 可见性质量详情 (2097 skills)
| 指标 | V46 | V47 | 变化 |
|------|-----|-----|------|
| 平均分 | 91.6 | 97.6 | +6.0 |
| A级 | 1098 (52%) | 1813 (86%) | +715 |
| B级 | 918 (44%) | 274 (13%) | -644 |
| C级 | 81 (4%) | 10 (0.5%) | -71 |
| A+B合格率 | 96% | 99% | +3% |

| 剩余问题类型 | V46数量 | V47数量 | 减少量 |
|----------|--------|---------|--------|
| MISSING_OR_IRRELEVANT_TAGS | 788 | 161 | -627 (80%) |
| MISSING_VALUE_PROPOSITION | 292 | 133 | -159 (54%) |
| INSUFFICIENT_SUMMARY | 0 | 0 | — |
| MISSING_QUICK_START | 0 | 0 | — |
| INVALID_CATEGORY | 0 | 0 | — |

### 10个C级skill (需重点修复)
| slug | 分数 | 问题 |
|------|------|------|
| dns-free | 65 | description缺价值命题 + tags相关性不足(6/15) |
| excel-formula | 65 | description缺价值命题 + tags相关性不足(0/1) |
| kai-tw-figma | 65 | description缺价值命题 + tags相关性不足(5/12) |
| knowledge-graph | 65 | description缺价值命题 + tags相关性不足(5/13) |
| note-app-cli | 65 | description缺价值命题 + tags相关性不足(0/1) |
| ocean-chat-assistant | 65 | description缺价值命题 + tags相关性不足(5/13) |
| repo-reader-tool | 65 | description缺价值命题 + tags相关性不足(6/14) |
| text-rpg-arcade-v3 | 65 | description缺价值命题 + tags相关性不足(5/13) |
| prompt-architect-pro | 65 | description缺价值命题 + tags相关性不足(0/1) |
| content-filter-tool-pro | 65 | description缺价值命题 + tags相关性不足(0/1) |

### 平台状态
| 平台 | 成功 | 待处理 | 失败/拒绝 |
|------|------|--------|----------|
| SkillHub | 2036 | 2 pending + 1 admin + 17 platform_review | 20 rejected |
| ClawHub | 430 | 505 not_uploaded | 1171 not_eligible |
| Community | 4032 | — | 40 failed |
| Hermes | 759 eligible | 1326 not_eligible | — |

### 三轨模型
| 轨道 | 数量 |
|------|------|
| 源技能 | 110 (71 clawhub + 39 opensource) |
| 免费增强版 | 759 |
| 付费增强版 | 1326 |
| 生产总计 | 2085 (985 packaged + 1100 differentiated) |
| 配对率 | 1516/2085 (73%) |

## 实施任务

### 任务1: GitHub推送恢复 (阻塞任务)

**问题**: V47提交(commit 4d1ad4536)因GitHub网络不可达未能推送

**实现**:
1. 检测GitHub连通性: `Test-NetConnection github.com -Port 443`
2. 连通后执行: `git push origin main` (私有备份)
3. 连通后执行: `git push hermes-skills main` (公开引流)
4. 如持续不可达,跳过不阻塞后续任务

### 任务2: L9 10个C级skill重点修复

**问题**: 10个C级skill同时缺少价值命题和tags相关性

**修复方案**: 逐个手动修复(自动化修复对这些skill效果不佳):
1. 读取每个skill的SKILL.md和body内容
2. 基于body核心能力章节,重写description添加价值命题关键词
3. 基于body关键词频率分析,重新推断tags(确保tags在body中有直接匹配)
4. 特别关注tags为单个逗号分隔字符串的格式问题(如`tags: - "tag1,tag2,tag3"`)

**10个skill列表**: dns-free, excel-formula, kai-tw-figma, knowledge-graph, note-app-cli, ocean-chat-assistant, repo-reader-tool, text-rpg-arcade-v3, prompt-architect-pro, content-filter-tool-pro

**验证**: 运行deep_quality_audit.py, 确认C级skill从10降至0

### 任务3: L9 MISSING_VALUE_PROPOSITION批量修复 (133个)

**问题**: description缺少价值命题关键词(提升/节省/加速/自动化/优化/简化/分析/生成/转换/处理/监控/管理)

**修复方案**: 增强 `fix_missing_fields.py` 的 `fix_missing_value_proposition()` 函数:
1. 读取description字段(支持block scalar格式)
2. 检测是否包含至少1个价值命题关键词
3. 如缺失,从body的`## 核心能力`章节提取关键动词
4. 将价值命题补充到description的block scalar内容末尾(而非追加到`|-`行)
5. **关键修复**: 确保_replace_frontmatter_field正确处理block scalar,不会破坏`|-`格式

**验证**: 运行deep_quality_audit.py, 确认MISSING_VALUE_PROPOSITION从133降至<30

### 任务4: L9 MISSING_OR_IRRELEVANT_TAGS批量修复 (161个)

**问题**: tags字段与skill内容相关性不足(匹配率<50%)

**修复方案**: 
1. 修复tags格式问题: 检测`tags: - "tag1,tag2,tag3"`(单个列表项包含逗号)并转换为`tags: tag1,tag2,tag3`(字符串格式)
2. 对相关性不足的tags,使用_extract_body_keywords()从body提取高频关键词替换
3. 确保新tags在body前3000字符中有直接匹配
4. **注意**: 不要运行fix_missing_fields.py的fix_irrelevant_tags()后再运行其他修复,因为可能回退tags格式

**验证**: 运行deep_quality_audit.py, 确认MISSING_OR_IRRELEVANT_TAGS从161降至<50

### 任务5: L7b 2个非A级skill修复

**问题**: 
- accounting-and-finance (B级): 有代码但缺少输出格式说明
- cdp-browser-master (C级): 有代码但缺少输入参数和输出格式说明

**修复方案**:
1. 读取两个skill的SKILL.md
2. 在代码块附近添加`## 输入格式`和`## 输出格式`章节(含JSON代码块)
3. 确保输入格式包含参数名、类型、必填、说明表格
4. 确保输出格式包含success/result/metadata的JSON结构

### 任务6: L5 5个B级skill内容增强

**问题**: 5个B级skill因内容偏少(<2K字符)评为B级
- automation-recipe-pack (60分)
- data-analysis-toolkit (65分)
- pdf-compressor-tool (65分)
- trading-strategy-guide (55分)
- (第5个需确认)

**修复方案**: 为每个skill补充:
1. 更详细的核心能力描述
2. 额外的使用场景
3. 完整的示例
4. 错误处理表格
5. 目标: 内容超过2K字符,达到A级(80+分)

### 任务7: 数据库重建

**问题**: skills.db为空(无表),upload_tracking.json是唯一数据源

**修复方案**:
1. 运行daily_sync.py重建数据库表结构
2. 从upload_tracking.json导入skills和platform_uploads数据
3. 从文件系统扫描补充文件路径和frontmatter信息
4. 重建FTS全文搜索索引
5. 验证dashboard可正常查询

### 任务8: ClawHub 505个待上传skill监控

**问题**: ClawHub有505个not_uploaded技能,定时任务每日12:00上传200个

**实现**:
1. 检查定时任务状态(ID: 5f5e0baf)
2. 查看最近运行日志
3. 确认上传进度(430→目标935+)
4. 如有失败技能,分析原因并修复

## 验证检查清单

- [ ] GitHub推送成功(origin + hermes-skills),或确认网络仍不可达
- [ ] L9 10个C级skill全部修复为B级以上
- [ ] L9 MISSING_VALUE_PROPOSITION从133降至<30
- [ ] L9 MISSING_OR_IRRELEVANT_TAGS从161降至<50
- [ ] L9 A+B级合格率从99%提升至99.5%+
- [ ] L9 C级skill从10降至0
- [ ] L7b 2个非A级skill修复为A级
- [ ] L5 5个B级skill增强为A级
- [ ] 数据库skills.db重建完成(含表结构和数据)
- [ ] ClawHub定时任务正常运行
- [ ] Git提交完成

## 约束

1. **不创建新文件** — 所有修复功能集成到现有工具脚本
2. **不模拟/mock** — 所有文件修改和数据库操作必须真实执行
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏现有命令功能
5. **内容保真** — tags增强和value proposition增强不得改变技能原有语义和功能
6. **网络容错** — GitHub推送失败不应阻塞其他任务的执行
7. **block scalar安全** — 修复description时必须正确处理`|-`格式,不得产生`|-，XXX`损坏
8. **tags格式一致** — tags必须使用字符串格式(`tags: tag1,tag2,tag3`),不得使用单个列表项包含逗号的格式
