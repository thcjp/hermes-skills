# 第46轮提示词 (v46.0) — L8/L9质量问题批量修复 + 平台侧可见性验证

> **日期**: 2026-07-24
> **上一轮完成**: V45 — DB迁移+可见性修复+L9集成+7个pending_review修复 (commit 96124b0a)
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库

## V45完成总结

| 任务 | 状态 | 结果 |
|------|------|------|
| DB迁移 | ✅ | community_published/download_ready字段已添加 |
| L9集成 | ✅ | run_audit()+main()已完全集成，--no-layer9 CLI参数可用 |
| 可见性修复 | ✅ | 45个不可见技能(23 NULL+22 org_only)→public，1120个success技能community_published=1 |
| Community JS | ✅ | 增强版community_publish.js已生成 |
| 7个pending_review修复 | ✅ | 删除重复YAML/定价元数据/外部URL/API密钥/营销注入/乱码 |
| 审计验证 | ✅ | L9正常工作，2097技能分析完成，审计通过 |
| Git提交 | ✅ | commit 96124b0a，已推送到GitHub |

## V45审计关键发现

### L8安全审计 (2097 skills)
| 问题类型 | 触发数 | 说明 |
|----------|--------|------|
| DUPLICATE_YAML_FIELDS | 2090 | tools/tags字段在frontmatter中出现两次（列表格式+字符串格式） |
| TAG_MISMATCH | 1421 | frontmatter中tags值与内容不匹配 |
| EXTERNAL_URL | 0 | 已清除 |
| INJECTED_MARKETING_TEXT | 0 | 已清除 |
| API_KEY_EXPOSURE | 0 | 已清除 |
| GARBLED_TEXT | 0 | 已清除 |

### L9可见性质量预检 (2097 skills)
| 指标 | 值 |
|------|-----|
| 平均分 | 62.2/100 |
| A级 | 110 (5%) |
| B级 | 688 (33%) |
| C级 | 984 (47%) |
| D级 | 315 (15%) |
| A+B级合格率 | 38% (798/2097) |

| 问题类型 | 触发数 | 修复方向 |
|----------|--------|----------|
| INSUFFICIENT_SUMMARY | 1800 | summary < 50字符，需扩充描述 |
| MISSING_QUICK_START | 1091 | 缺少"快速开始"/"Quick Start"章节 |
| MISSING_OR_IRRELEVANT_TAGS | 447 | tags缺失或与内容不相关 |
| MISSING_VALUE_PROPOSITION | 292 | description缺少价值命题关键词 |
| INVALID_CATEGORY | 0 | 已全部修复 |

## 实施任务

### 任务1: 批量修复L8 DUPLICATE_YAML_FIELDS (2090个skill)

**问题**: frontmatter中 `tools` 和 `tags` 字段出现两次：
- 第一次: YAML列表格式 (`tools:\n  - read\n  - exec`)
- 第二次: 字符串/数组格式 (`tools: ["read", "write", "exec"]` 或 `tags: "工作流,自动化,效率"`)

**修复方案**: 增强 `fix_missing_fields.py` 添加 `fix_duplicate_yaml_fields()` 函数：
1. 解析frontmatter，检测重复字段
2. 保留第一次出现的格式（YAML列表），合并第二次的缺失值
3. 删除第二次出现的重复字段
4. 同时修复 TAG_MISMATCH：确保tags与slug/category/content一致

### 任务2: 批量修复L9 INSUFFICIENT_SUMMARY (1800个skill)

**问题**: summary字段不足50字符

**修复方案**: 增强 `fix_missing_fields.py` 添加 `expand_summary()` 函数：
1. 读取当前summary和description
2. 如果summary < 50字符，从description/body中提取关键信息扩充
3. 确保扩充后的summary >= 50字符且 <= 100字符
4. 保留原有核心信息，不改变语义

### 任务3: 批量修复L9 MISSING_QUICK_START (1091个skill)

**问题**: 缺少"快速开始"/"Quick Start"章节

**修复方案**: 增强 `fix_missing_fields.py` 添加 `add_quick_start_section()` 函数：
1. 检测body中是否已有"## 快速开始"/"## Quick Start"章节
2. 如果没有，在"## 使用流程"或"## 核心能力"后插入标准化的快速开始章节
3. 内容模板: 简明步骤 + 基本用法示例

### 任务4: 平台侧可见性验证

**目标**: 在SkillHub平台侧实际验证技能可见性

**实现**:
1. 使用生成的 `community_publish.js` 在浏览器中执行
2. 验证1120个success技能在平台前台是否可见
3. 如有不可见技能，使用JS脚本调用 `publish-to-community` API
4. 同步结果到数据库

### 任务5: 重试8个retry_pending技能

**目标**: 重新上传8个retry_pending技能到SkillHub

**技能列表**:
- cdp-browser-master, cron-guard, linear-workflow-bot
- ai-artist-workstation, sales-copy-writer
- accounting-and-finance, accounting-finance, ace-music

**实现**: `python tools/auto_publish.py publish-skillhub <slug>` 逐个重试

### 任务6: hermes-skills仓库推送

**目标**: 将技能同步到公共引流仓库 `https://github.com/thcjp/hermes-skills`

**实现**:
1. 确认hermes-skills仓库的remote配置
2. 推送精选免费技能到公共仓库
3. 验证推送结果

## 验证检查清单

- [ ] L8 DUPLICATE_YAML_FIELDS 从2090降至0
- [ ] L8 TAG_MISMATCH 从1421降至<100
- [ ] L9 INSUFFICIENT_SUMMARY 从1800降至<200
- [ ] L9 MISSING_QUICK_START 从1091降至<100
- [ ] L9 A+B级合格率从38%提升至70%+
- [ ] 8个retry_pending技能重试上传
- [ ] hermes-skills仓库推送完成
- [ ] Git提交完成

## 约束

1. **不创建新文件** — 所有修复功能集成到现有 `fix_missing_fields.py`
2. **不模拟/mock** — 所有文件修改和数据库操作必须真实执行
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏现有命令功能
5. **内容保真** — 扩充summary和添加Quick Start不得改变技能原有语义和功能
