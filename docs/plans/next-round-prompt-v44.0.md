# 第44轮提示词 (v44.0) — SkillHub 可见性与评分优化

> **日期**: 2026-07-24
> **上一轮完成**: V43任务分析 + SkillHub可见性/评分专题诊断
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库

## 背景诊断

### 分析结论（已验证）

| 问题 | 诊断 | 数据验证 |
|------|------|----------|
| 2000+技能不可见 | 22个`org_only` + 29个`NULL`可见性 + 可能的平台侧隐藏 | DB确认: org_only=22, NULL=29, public+success=1075 |
| COS文件同步失败 | S3/MinIO(COS后端)上传失败→download_ready=FALSE | 40个报告失败，需平台侧确认 |
| 分类影响 | Label系统非传统category，无标签不影响显示但影响筛选 | DB确认: 957个NULL category |
| 评分下降 | 纯用户算术平均，无自动质量评分，复杂度↑→期望↑→满意度分散 | 源码确认 |
| 7个pending_review | 注入营销文本+重复YAML+slug不匹配+乱码+依赖矛盾 | review_analysis_v36.json确认 |

### 数据库实测状态

```
SkillHub platform_uploads:
  success=1120 (org_only=22, NULL=29, public=1075)
  retry_pending=8
  cancelled=1
  
NULL category技能: 957个 (无tags列，需从SKILL.md推断)
无效category值: '' (空字符串), 'packaged'
有效category值: Agents, Automation, Communication, Creative, Development, 
               Finance, Integrations, Knowledge, Lifestyle, Operations, 
               Other, Productivity, Research, Security
```

## 实施任务

### 任务1: 增强 `auto_publish.py` — 添加 `check-visibility` 命令

**目标**: 在现有 `auto_publish.py` 中新增一个命令，不创建新文件

**实现**:
1. 新增 `check_visibility()` 函数:
   - 查询数据库中所有 `platform='skillhub'` 的记录
   - 分类统计: org_only / NULL / public
   - 输出不可见技能清单（slug + category + status）
   - 生成可见性诊断报告 JSON 到 `data/reports/visibility_report.json`
2. 在 `main()` 中添加 `check-visibility` 命令路由
3. 增强 `generate_community_publish_js()`:
   - 在现有JS脚本中增加 `download_ready` 检查
   - 增加 `namespace.type` (TEAM/GLOBAL) 报告
   - 增加 `hidden` 状态检查
   - 输出完整的可见性诊断JSON

### 任务2: 增强 `fix_missing_fields.py` — 添加 category 推断

**目标**: 在现有 `fix_missing_fields.py` 中增加 category 推断功能

**实现**:
1. 新增 `TAG_TO_CATEGORY_MAP` 字典: 将 tags 关键词映射到16个有效 category
2. 新增 `infer_category(slug, path, body, tags)` 函数:
   - 优先从 tags 推断
   - 其次从 slug/path 关键词推断
   - 最后从 body 内容关键词推断
3. 增强 `fix_missing_fields.py` 主流程:
   - 检测 SKILL.md frontmatter 中缺失的 category 字段
   - 调用 `infer_category()` 填充
   - 同时更新数据库 `skills.category` 字段
4. 修复无效 category 值: `''` → 推断值, `'packaged'` → 推断值

### 任务3: 增强 `db.py` — 添加可见性追踪字段迁移

**目标**: 在现有 `db.py` 的 `init_db()` 中增加字段迁移

**实现**:
1. 在 `init_db()` 末尾添加迁移逻辑:
   - `ALTER TABLE platform_uploads ADD COLUMN community_published INTEGER DEFAULT 0`
   - `ALTER TABLE platform_uploads ADD COLUMN download_ready TEXT`
   - 使用 try/except 处理已存在字段（幂等迁移）
2. 更新 `record_upload()` 函数支持新字段
3. 添加 `update_visibility_status()` 函数: 批量更新可见性状态

### 任务4: 增强 `deep_quality_audit.py` — 添加 L9 可见性预检

**目标**: 在现有审计管道中增加 L9 层，不创建新文件

**实现**:
1. 新增 `check_visibility_quality()` 函数:
   - 检查 category 是否为 NULL 或无效值
   - 检查 summary 是否存在且 ≥ 50字符（影响搜索排名权重）
   - 检查 description 是否包含明确价值主张
   - 检查是否存在"快速开始"/"Quick Start"区块（评分优化）
   - 检查 tags 是否存在且与内容相关
   - 评级: A(90+) / B(70+) / C(50+) / D(<50)
2. 在主审计流程中集成 L9 检查
3. 在审计报告中增加 L9 统计

### 任务5: 生成增强版 community publish JS

**目标**: 使用增强后的 `generate_community_publish_js()` 生成浏览器脚本

**实现**:
1. 执行 `python tools/auto_publish.py gen-community-publish-js`
2. 生成的JS脚本将:
   - 获取所有技能列表（含 visibility, download_ready, namespace 信息）
   - 筛选 org_only + NULL visibility 技能
   - 批量调用 `publish-to-community` API
   - 报告所有不可见原因
   - 输出 JSON 结果供数据库同步
3. 同时生成 COS 重试脚本: `python tools/auto_publish.py retry-cos-failures`

### 任务6: 修复 7 个 pending_review 技能内容

**目标**: 直接修复 SKILL.md 文件内容问题

**需修复的技能**:
1. `version-control-workflows` — 删除注入的营销文本，修复重复YAML
2. `data-analysis-toolkit` — 删除外部URL，删除营销文本，修复依赖矛盾
3. `trading-strategy-guide` — 删除外部URL，删除API密钥模式，修复slug不匹配
4. `xml-parser-tool` — 修复slug不匹配，修复重复YAML
5. `text-rpg-arcade-v3` — 修复tags不匹配，修复重复YAML
6. `video-upload-stream-tool` — 删除外部URL，删除API密钥模式，修复依赖矛盾
7. `pdf-compressor-tool` — 修复乱码文本，修复重复YAML

**修复规则**:
- 删除所有 "Use when 需要营销推广、广告投放..." 注入文本
- 删除所有外部商业URL (lemonsqueezy.com, kairyuu.net, attoaioz.cyou等)
- 删除API密钥格式展示 (Authorization: Bearer, stream-public-key等)
- 修复重复YAML字段 (保留YAML列表格式，删除字符串格式)
- 修复乱码文本为正确中文
- 修复依赖矛盾（统一"需要API Key"或"无需API Key"）

### 任务7: 数据库 category 批量修复

**目标**: 修复 957 个 NULL/无效 category 技能

**实现**:
1. 对每个 NULL category 技能:
   - 读取对应 SKILL.md 的 frontmatter tags
   - 调用 `infer_category()` 推断 category
   - 更新 SKILL.md frontmatter 添加 category 字段
   - 更新数据库 `skills.category` 字段
2. 修复 `'packaged'` category → 推断为正确值
3. 修复 `''` (空字符串) category → 推断为正确值
4. 生成修复报告: `data/reports/category_fix_report.json`

## 验证检查清单

- [ ] `auto_publish.py check-visibility` 命令可用且输出正确
- [ ] `fix_missing_fields.py` 能推断并填充 category
- [ ] `db.py` 迁移成功（community_published + download_ready 字段存在）
- [ ] `deep_quality_audit.py` L9 检查正常运行
- [ ] 增强版 community publish JS 已生成
- [ ] 7个 pending_review 技能内容已修复
- [ ] 957个 NULL category 已修复至 ≤ 50
- [ ] Git 提交完成

## 约束

1. **不创建新文件**（除计划文件和报告文件外）
2. **不新增独立脚本** — 所有功能必须集成到现有 `auto_publish.py`, `fix_missing_fields.py`, `db.py`, `deep_quality_audit.py`
3. **不模拟/mock** — 所有数据库操作必须真实执行
4. **幂等迁移** — 数据库 ALTER TABLE 必须幂等（字段已存在时不报错）
5. **向后兼容** — 增强不能破坏现有命令的功能
