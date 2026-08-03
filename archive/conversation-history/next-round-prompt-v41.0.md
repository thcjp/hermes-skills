# Round 41 执行提示词 v41.0 (架构治理专项)

## 上下文
- **上一轮**: Round 40 (Git: cadc4889, 14 files, +646/-2082)
- **当前日期**: 2026-07-24
- **数据库**: 2882 total skills (1162 updated + 959 active + 759 stale + 1 not_found + 1 optimized)
- **平台状态**: SkillHub 1126 success, ClawHub 1152 success/855 published, GitHub 1159 success
- **审计状态**: L4-L8 全量通过, 2097/2097 A级
- **5轮交叉审核**: 发现31项问题, 3个致命SQL bug, 10个新遗漏, 用户核心要求实现度20%

## 治理背景

项目已出现严重碎片化和冗余迹象：
1. **配置散乱**: 17个脚本硬编码DB_PATH(非5个), DIFFERENTIATED_DIR在26个脚本中硬编码
2. **工具/产品混合**: skill-registry/包含69个.py脚本 + 957个JSON数据文件混在一起
3. **三轨模型错误**: 付费版映射到enterprise-upload/(仅2个), 实际260个paid在differentiated-skills/
4. **数据缺失**: hermes-skills(759个)完全未导入数据库, packaged-skills/skillhub(807个)未导入
5. **核心要求未实现**: 每日数据同步(0%), UI看板从数据库读取(10%)

## 执行原则
1. **每个Phase完成后必须git commit**, 创建回滚tag
2. **Phase 3前必须备份数据库**
3. **禁止任何mock/fallback/skip/todo/pass**
4. **所有SQL必须先用Python验证语法正确**
5. **任务必须定义到结束**, 防止半拉子工程

---

## Phase 1: 统一配置中心 (P0)

### Task 1.1: 创建config/目录和模块
- 创建 `d:\skills\config\__init__.py` - 导出所有配置
- 创建 `d:\skills\config\project_config.py` - 从skill-registry/config.py迁移并扩展:
  - 保留: PROJECT_ROOT, DB_PATH, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, EXPORT_DIR, BACKUP_DIR
  - 保留: TRACE阈值, 付费判断, 数据库表名常量, TRACE_FIELD_MAPPING
  - **新增**: TOOLS_DIR, DATA_DIR, REPORT_DIR(改为data/reports/)
  - **新增**: CLAWHUB_DOWNLOADED_DIR, HERMES_SKILLS_DIR, ENTERPRISE_UPLOAD_DIR, DIFFERENTIATED_DIR
  - **保留REGISTRY_DIR**: 暂时保留指向skill-registry/, Phase 2重命名后再改
  - 修改: MARKET_DATA_DIR, BACKUP_DIR 改为基于DATA_DIR而非REGISTRY_DIR
- 创建 `d:\skills\config\platform_config.py` - 平台配置:
  - SkillHub: CLI路径、API URL、WAF限制(5800字符)
  - ClawHub: 上传限制(200/24h)、Token路径
  - GitHub: 双仓库remote配置、分支
- 移动 `skill-registry/github_repo_strategy.py` → `config/github_repo_strategy.py`

### Task 1.2: 修改17个硬编码DB_PATH脚本
**完整清单(5轮审核确认)**:
1. `orchestrator.py` (DB_PATH + SKILLS_ROOT + SKILL_REGISTRY_DIR, 3个常量)
2. `version_sync_pipeline.py` (DB_PATH + SKILLS_ROOT + 5个路径常量, 7个常量)
3. `db.py` (DB_PATH)
4. `analyze_status.py` (DB_PATH)
5. `dashboard_server.py` (DB_PATH + REGISTRY_DIR)
6. `auto_discover.py` (DB_PATH + SKILLS_ROOT + CLAWHUB_DOWNLOADED_DIR)
7. `clean_naming.py` (DB_PATH)
8. `github_scanner.py` (DB_PATH + GITHUB_REPOS)
9. `init_baseline.py` (DB_PATH + SKILLS_ROOT)
10. `multi_source_discover.py` (DB_PATH)
11. `skill_batch_upgrader_v3.py` (DB_PATH)
12. `task3_pricing_calibration.py` (DB_PATH)
13. `update_mechanism.py` (DB_PATH + SKILLS_ROOT + 5个路径常量)
14. `update_v2_and_report.py` (DB_PATH)
15. `skill_core/db.py` (DB_PATH fallback)
16. `check_debranding.py` (直接sqlite3.connect硬编码)
17. `scan_and_import.py` (3处直接sqlite3.connect硬编码)

**修改方式**: 每个脚本删除硬编码, 改为:
```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'config'))
from project_config import DB_PATH, SKILLS_ROOT, ...
```
**注意**: 此阶段**不修改REGISTRY_DIR引用**, 仅修改DB_PATH和相关路径常量

### Task 1.3: 统一GITHUB_REPOS定义
- 将auto_discover.py和github_scanner.py中的GITHUB_REPOS统一到config/platform_config.py
- 两个脚本都改为从config导入

### Task 1.4: 修复阈值不一致
- 使用UPDATE而非ALTER: `UPDATE scores SET pass_threshold = 42 WHERE pass_threshold = 40 OR pass_threshold IS NULL`
- 所有脚本使用config.TRACE_PASS_THRESHOLD

### Task 1.5: 修改26个引用differentiated-skills的脚本
- 所有脚本中的`Path(r"D:\skills\differentiated-skills")`改为从config导入DIFFERENTIATED_DIR
- 完整脚本清单(通过grep确认): auto_publish.py, capability_pipeline.py, deep_quality_audit.py, diff_batch_fix.py, diff_batch_fix2.py, diff_batch_fix3.py, diff_l4_batch_fix.py, hermes_batch_convert.py, hermes_converter.py, template_cleanup.py等

**验证标准**:
- `grep -rn "d:\\\\skills\\\\skill-registry.db" skill-registry/*.py skill-registry/**/*.py` 返回0结果
- `grep -rn "d:\\\\skills\\\\differentiated-skills" skill-registry/*.py` 返回0结果
- `python -c "from config import DB_PATH; print(DB_PATH)"` 正常输出
- 所有17个脚本可正常import config

**Git检查点**: `git add -A && git commit -m "Phase 1: unified configuration center - fixed 17+26 hardcoded scripts"`
**回滚tag**: `git tag pre-phase-1` (在Phase开始前创建)

---

## Phase 2: 工具/产品物理分离 (P0)

### Task 2.1: 创建data/目录结构
```
d:\skills\data\
├── reports/           # 审计报告JSON
├── health_reports/    # 健康检查报告
├── market-data/       # 市场数据
├── backups/           # 数据库备份
└── discovery/         # 发现候选数据
```

### Task 2.2: 移动数据文件到data/
- `skill-registry/*.json` (957个) → `data/reports/` (报告类) 或 `data/` (状态文件类)
- 状态文件移到data/根目录: upload_tracking.json, clawhub_published_slugs.json, clawhub_upload_checkpoint.json, clawhub_upload_batches.json, clawhub_upload_results.json, clawhub_remaining.json, category_mapping.json
- `skill-registry/health_reports/` → `data/health_reports/`
- `skill-registry/market-data/` → `data/market-data/`
- `skill-registry/backups/` → `data/backups/`
- `skill-registry/discovery/` → `data/discovery/`

### Task 2.3: 重命名skill-registry/ → tools/
- `skill-registry/*.py` → `tools/*.py` (使用git mv保留历史)
- `skill-registry/skill_core/` → `tools/core/`
- `skill-registry/templates/` → `tools/templates/`
- 删除空的skill-registry/目录

### Task 2.4: 移动顶层脚本到tools/scripts/
- `retry-skillhub.ps1`, `retry-skillhub-v2.ps1` → `tools/scripts/`
- `run-skillhub.sh`, `skillhub.ps1` → `tools/scripts/`
- `upload-differentiated.ps1`, `upload-to-skillhub.ps1` → `tools/scripts/`

### Task 2.5: 更新所有路径引用
**关键更新清单**:
1. `config/project_config.py`: REGISTRY_DIR → TOOLS_DIR, REPORT_DIR → DATA_DIR/reports/
2. `tools/orchestrator.py`: 15处SKILL_REGISTRY_DIR引用 → TOOLS_DIR
3. `tools/version_sync_pipeline.py`: SKILL_REGISTRY_DIR → TOOLS_DIR
4. `tools/clawhub_batch_uploader.py`: 7个数据文件路径更新为data/目录
5. `tools/dashboard_server.py`: REGISTRY_DIR → TOOLS_DIR, 报告路径更新
6. `tools/deep_quality_audit.py`: REGISTRY_DIR → TOOLS_DIR
7. 所有脚本中的`skill-registry`路径引用 → `tools`
8. `.gitignore`: 更新路径规则
9. 所有引用`.skillhub-credentials`的脚本 → `.credentials`

### Task 2.6: 更新定时任务路径
- ClawHub定时任务(Schedule ID: 5f5e0baf)中的脚本路径需更新
- 检查定时任务message中的路径引用

**验证标准**:
- `skill-registry/`目录不存在
- `tools/`目录包含所有69个.py脚本
- `data/`目录包含所有957个JSON数据文件
- `python tools/orchestrator.py status` 正常输出
- `python tools/version_sync_pipeline.py scan` 正常输出
- `python tools/clawhub_batch_uploader.py --dry-run` 正常运行

**Git检查点**: `git add -A && git commit -m "Phase 2: physical separation - tools/ + data/ + path updates"`
**回滚tag**: `git tag pre-phase-2` (在Phase开始前创建)

---

## Phase 3: 数据库清理和增强 (P0)

### Task 3.0: 数据库备份
```bash
cp d:\skills\skill-registry.db d:\skills\data\backups\skill-registry.db.pre-phase-3
```

### Task 3.1: 删除冗余数据库文件
- 删除前验证每个文件确认为空或备份
- 删除: skills.db(0字节), skill-registry.db.backup_20260720_092727, skill-registry.db.bak_pricing_fix, skill-registry/skill-registry.db(0字节), skill-registry/skills.db(0字节), skill-registry/skill_registry.db(0字节)
- 保留: d:\skills\skill-registry.db (唯一数据库)

### Task 3.2: 数据库schema增强
```sql
-- 仅新增free_slug和paid_slug(skill_type和source_slug已存在)
-- 使用Python try/except包裹实现幂等
ALTER TABLE skills ADD COLUMN free_slug TEXT;
ALTER TABLE skills ADD COLUMN paid_slug TEXT;
-- 索引名使用idx_skills_source_slug避免与已有idx_skills_source冲突
CREATE INDEX IF NOT EXISTS idx_skills_source_slug ON skills(source_slug);
CREATE INDEX IF NOT EXISTS idx_skills_free ON skills(free_slug);
CREATE INDEX IF NOT EXISTS idx_skills_paid ON skills(paid_slug);
```

### Task 3.2b: 迁移skill_type值到三轨模型
```sql
-- 迁移前备份原始值
ALTER TABLE skills ADD COLUMN skill_type_original TEXT;
UPDATE skills SET skill_type_original = skill_type;

-- 源skill
UPDATE skills SET skill_type = 'source' WHERE skill_type IN ('original_download', 'clawhub_download');
-- 免费版(根据edition判断,不一律映射)
UPDATE skills SET skill_type = 'free' WHERE skill_type IN ('md_exec', 'opensource_modified', 'original_creation');
UPDATE skills SET skill_type = 'free' WHERE skill_type = 'differentiated' AND (is_paid = 0 OR is_paid IS NULL);
-- 付费版(differentiated中is_paid=1的)
UPDATE skills SET skill_type = 'paid' WHERE skill_type = 'differentiated' AND is_paid = 1;
-- NULL值根据local_path + edition综合判断
UPDATE skills SET skill_type = 'source' WHERE skill_type IS NULL AND local_path LIKE '%clawhub-skills/downloaded%';
UPDATE skills SET skill_type = 'paid' WHERE skill_type IS NULL AND edition IN ('paid', 'pro');
UPDATE skills SET skill_type = 'free' WHERE skill_type IS NULL AND (local_path LIKE '%packaged-skills%' OR local_path LIKE '%hermes-skills%' OR local_path LIKE '%opensource-skills%' OR local_path LIKE '%differentiated-skills%');
-- tool保持不变
```

### Task 3.2c: 规范化pricing_tier格式 (已修正运算符优先级)
```sql
-- 统一为带中文后缀的格式
UPDATE skills SET pricing_tier = 'L1-入门级' WHERE pricing_tier = 'L1';
UPDATE skills SET pricing_tier = 'L2-标准级' WHERE pricing_tier = 'L2';
UPDATE skills SET pricing_tier = 'L3-专业级' WHERE pricing_tier = 'L3';
UPDATE skills SET pricing_tier = 'L4-企业级' WHERE pricing_tier = 'L4';
-- 填充NULL和空值(必须加括号!)
UPDATE skills SET pricing_tier = 'L1-入门级' WHERE (pricing_tier IS NULL OR pricing_tier = '') AND (edition IS NULL OR edition = '' OR edition = 'free');
UPDATE skills SET pricing_tier = 'L3-专业级' WHERE (pricing_tier IS NULL OR pricing_tier = '') AND edition IN ('pro', 'paid');
-- 填充is_paid NULL值
UPDATE skills SET is_paid = 1 WHERE edition IN ('paid', 'pro') AND is_paid IS NULL;
UPDATE skills SET is_paid = 0 WHERE edition = 'free' AND is_paid IS NULL;
```

### Task 3.3: 填充三轨关联字段
```sql
-- source类型自引用
UPDATE skills SET source_slug = slug WHERE skill_type = 'source' AND (source_slug IS NULL OR source_slug = '');
-- free类型自引用
UPDATE skills SET free_slug = slug WHERE skill_type = 'free' AND free_slug IS NULL;
-- paid类型自引用
UPDATE skills SET paid_slug = slug WHERE skill_type = 'paid' AND paid_slug IS NULL;
-- 关联free和paid(同parent_slug,加排序保证确定性)
UPDATE skills SET paid_slug = (
    SELECT s2.slug FROM skills s2
    WHERE s2.parent_slug = skills.parent_slug AND s2.skill_type = 'paid'
    ORDER BY s2.updated_at DESC LIMIT 1
) WHERE skill_type = 'free' AND paid_slug IS NULL AND parent_slug IS NOT NULL;
-- 根据local_path推断剩余NULL的source_slug
UPDATE skills SET source_slug = slug WHERE source_slug IS NULL AND local_path LIKE '%clawhub-skills/downloaded%';
```

### Task 3.4: 重建FTS (已修正列名)
```sql
-- FTS表实际列: slug, name, display_name, description, tags, category
-- skills表对应: slug, current_name, current_display_name, notes(作为description), ''(tags), category
BEGIN TRANSACTION;
DELETE FROM skills_fts;
INSERT INTO skills_fts(rowid, slug, name, display_name, description, tags, category)
SELECT id, slug, current_name, current_display_name, COALESCE(notes, ''), '', category
FROM skills WHERE current_status IN ('active', 'updated');
COMMIT;
```

### Task 3.5: 创建看板视图 (已修正字段名和平台匹配)
```sql
CREATE VIEW IF NOT EXISTS v_skill_lifecycle AS
WITH latest_uploads AS (
    SELECT
        skill_id,
        CASE
            WHEN platform IN ('skillhub', 'skillhub_free', 'skillhub_paid') THEN 'skillhub'
            WHEN platform IN ('github', 'github_private', 'github_public') THEN 'github'
            ELSE platform
        END as platform_group,
        platform, upload_status,
        ROW_NUMBER() OVER (
            PARTITION BY skill_id,
            CASE
                WHEN platform IN ('skillhub', 'skillhub_free', 'skillhub_paid') THEN 'skillhub'
                WHEN platform IN ('github', 'github_private', 'github_public') THEN 'github'
                ELSE platform
            END,
            ORDER BY upload_date DESC
        ) as rn
    FROM platform_uploads
    WHERE platform != 'quality_gate'
)
SELECT
    s.slug, s.current_display_name, s.skill_type,
    s.source_slug, s.free_slug, s.paid_slug,
    s.current_version, s.current_status,
    s.pricing_tier, s.edition, s.is_paid,
    s.category, s.source,
    sh.upload_status as skillhub_status,
    ch.upload_status as clawhub_status,
    gh.upload_status as github_status,
    s.updated_at as last_updated
FROM skills s
LEFT JOIN latest_uploads sh ON sh.skill_id = s.id AND sh.platform_group = 'skillhub' AND sh.rn = 1
LEFT JOIN latest_uploads ch ON ch.skill_id = s.id AND ch.platform_group = 'clawhub' AND ch.rn = 1
LEFT JOIN latest_uploads gh ON gh.skill_id = s.id AND gh.platform_group = 'github' AND gh.rn = 1
WHERE s.current_status IN ('active', 'updated', 'stale');
```

### Task 3.6: 清理空表
- 删除空表dependencies或添加注释标记为预留
- 记录operations表约束不一致问题

### Task 3.7: 导入hermes-skills到数据库
- 扫描hermes-skills/目录759个SKILL.md
- 解析frontmatter获取slug, displayName, version等
- 插入skills表, skill_type='free', source='hermes'

### Task 3.8: 数据库与文件系统对齐
- 扫描所有6个产品目录的SKILL.md文件
- 对比数据库记录, 识别差异
- 缺失的导入, 多余的标记stale

**验证标准**:
- 仅1个数据库文件存在
- `SELECT skill_type, COUNT(*) FROM skills GROUP BY skill_type` 显示source/free/paid/tool分布
- `SELECT * FROM v_skill_lifecycle LIMIT 10` 正常返回
- `SELECT COUNT(*) FROM skills_fts` > 0 (FTS不为空)
- `SELECT COUNT(*) FROM skills WHERE pricing_tier IS NULL OR pricing_tier = ''` 返回0
- `SELECT COUNT(*) FROM skills WHERE is_paid IS NULL` 返回0
- pro/paid edition的skill没有被错误标记为L1-入门级

**Git检查点**: `git add -A && git commit -m "Phase 3: database enhancement - three-track model + views + FTS rebuild"`

---

## Phase 4: 文档统一 (P1)

### Task 4.1: 创建ARCHITECTURE.md
唯一架构文档, 包含:
- 项目概述和特色(收集→增强→拆分→上传)
- 目录结构说明(config/, tools/, data/, docs/, 产品skill目录)
- 8阶段流水线(以orchestrator.py为准, version_sync_pipeline.py实现其中7个Phase)
- L1-L8审计体系
- 平台策略(SkillHub/ClawHub/GitHub双仓库)
- 数据库schema和三轨模型
- 配置系统说明

### Task 4.2: 重写README.md
- 项目简介
- 快速开始
- 目录结构导航
- 文档索引

### Task 4.3: 统一流程描述
- 删除/合并其他文档中的流水线描述
- 统一为8阶段(orchestrator.py为准)
- 统一审计层数为L1-L8

### Task 4.4: 修正三轨模型描述
- 付费版: differentiated-skills/中edition=paid/pro的(713个) + enterprise-upload/(2个)
- 免费版: packaged-skills/skillhub/(995个) + hermes-skills/(759个) + opensource-skills/(40个) + differentiated-skills/中edition=free的
- 源: clawhub-skills/downloaded/(600个)

### Task 4.5: 清理冗余文档
- 删除v1审核报告, 保留v2
- 归档历史Round计划到docs/plans/archive/
- 合并UPLOAD-GUIDE.md → docs/ARCHITECTURE.md
- 移动顶层报告到docs/reports/

**验证标准**:
- ARCHITECTURE.md存在且包含完整架构描述
- README.md有实质内容
- 0个v1审核报告
- 流水线描述仅1处(8阶段)

**Git检查点**: `git add -A && git commit -m "Phase 4: documentation unification - ARCHITECTURE.md + README + cleanup"`

---

## Phase 5: 顶层文件清理 (P2)

### Task 5.1: 移动顶层文件
- 13个.md报告文件 → docs/reports/
- clawhub-config.json → config/
- skill_verification_report.html → 删除(临时文件)

### Task 5.2: 清理空目录
- 检查并删除packaged-skills/下的空目录

### Task 5.3: 重命名凭证目录
- `.skillhub-credentials/` → `.credentials/`
- 更新所有脚本和.gitignore中的引用

### Task 5.4: 更新.gitignore
- 添加: data/backups/, .credentials/, config/secrets.py
- 移除: 过时的路径规则

**验证标准**:
- 顶层仅保留: config/, tools/, data/, docs/, 产品skill目录, .credentials/, skill-registry.db, .gitignore, README.md
- 0个空目录

**Git检查点**: `git add -A && git commit -m "Phase 5: top-level cleanup - moved files + renamed credentials"`

---

## Phase 6: 每日同步与看板 (P0 - 用户核心要求)

### Task 6.1: 修改dashboard_server.py使用视图
- 将直接查表改为`SELECT * FROM v_skill_lifecycle`
- 看板UI增加三轨状态列(source/free/paid)
- 看板UI增加各平台上传状态列(skillhub/clawhub/github)
- 看板UI增加pricing_tier和edition显示

### Task 6.2: 创建每日同步脚本
- 创建 `tools/daily_sync.py`:
  - 扫描变更(version_sync_pipeline.py scan)
  - 同步GitHub(免费→hermes-skills, 全部→origin)
  - 同步SkillHub(免费CLI + 付费payload)
  - 同步ClawHub(定时任务已有)
  - 记录到数据库
  - 生成每日同步报告

### Task 6.3: 配置每日定时任务
- 创建Windows定时任务或使用Schedule工具
- 每日固定时间执行daily_sync.py
- 与现有ClawHub定时任务(5f5e0baf)协调

**验证标准**:
- `python tools/dashboard_server.py` 启动后看板显示三轨状态
- `python tools/daily_sync.py --dry-run` 正常输出同步计划
- 看板数据来自v_skill_lifecycle视图(非直接查表)

**Git检查点**: `git add -A && git commit -m "Phase 6: daily sync + dashboard view integration"`

---

## Phase 7: 全量验证 (P0)

### Task 7.1: 脚本运行验证
- `python tools/orchestrator.py status` 正常输出
- `python tools/version_sync_pipeline.py scan` 正常输出
- `python tools/deep_quality_audit.py` 正常运行
- `python tools/clawhub_batch_uploader.py --dry-run` 正常运行
- `python tools/dashboard_server.py` 正常启动

### Task 7.2: 配置一致性验证
- `grep -rn "d:\\\\skills\\\\skill-registry.db" tools/ config/` 返回0结果
- `grep -rn "d:\\\\skills\\\\differentiated-skills" tools/` 返回0结果
- `grep -rn "skill-registry" tools/*.py` 仅出现在注释中
- 所有脚本的DB_PATH来自config

### Task 7.3: 数据库完整性验证
- skills表记录数与文件系统对齐
- v_skill_lifecycle视图可查询且数据正确
- FTS搜索功能可用
- 三轨字段(skill_type/source_slug/free_slug/paid_slug)正确填充

### Task 7.4: 三轨模型验证
- `SELECT skill_type, COUNT(*) FROM skills GROUP BY skill_type` 分布合理
- `SELECT COUNT(*) FROM skills WHERE skill_type = 'paid' AND edition NOT IN ('paid', 'pro')` 返回0
- `SELECT COUNT(*) FROM skills WHERE pricing_tier = 'L1-入门级' AND edition IN ('pro', 'paid')` 返回0

### Task 7.5: Git提交和推送
- 提交所有变更
- 推送到origin(私有备份)
- 验证hermes-skills仓库状态

**验证标准**:
- 所有脚本正常运行
- 0个硬编码路径
- 数据库完整且正确
- 三轨模型数据准确

**Git检查点**: `git add -A && git commit -m "Phase 7: full validation passed"`
**最终推送**: `git push origin main`

---

## 修正后的三轨模型(唯一权威)

| 轨道 | skill_type | 主要目录 | 实际数量 | 判定依据 |
|------|-----------|----------|----------|----------|
| 源 | source | clawhub-skills/downloaded/ | 600 | 从外部下载的原始skill |
| 免费版 | free | packaged-skills/skillhub/ + hermes-skills/ + opensource-skills/packaged/ + differentiated-skills/(edition=free) | ~2121 | edition=free或is_paid=0 |
| 付费版 | paid | differentiated-skills/(edition=paid/pro) + enterprise-upload/ | ~715 | edition=paid/pro或is_paid=1 |
| 工具 | tool | tools/ | 8 | 项目工具脚本 |

## 修正后的8阶段流水线(唯一权威)

```
1. DISCOVER     - 发现新skill + 检测已有skill变更 (orchestrator.py phase_discover)
2. ENHANCE      - 内容增强建议 (orchestrator.py phase_enhance)
3. AUDIT        - L1-L8全量质量审计 (orchestrator.py phase_audit)
4. SYNC_GITHUB  - GitHub双仓库同步 (version_sync_pipeline.py sync_to_github)
5. SYNC_SKILLHUB - SkillHub免费+付费同步 (version_sync_pipeline.py sync_to_skillhub)
6. SYNC_CLAWHUB  - ClawHub同步 (clawhub_batch_uploader.py)
7. RECORD       - 数据库记录 (version_sync_pipeline.py record_platform_upload)
8. REPORT       - 生成报告 (orchestrator.py phase_report)
```
注: version_sync_pipeline.py实现其中Phase 4-7的子流程(DETECT→INCREMENT→VALIDATE→SYNC→RECORD)

## 修正后的平台策略(唯一权威)

| 平台 | 免费版 | 付费版 | 上传方式 | 限流 |
|------|--------|--------|----------|------|
| SkillHub | CLI publish | 浏览器session | skillhub publish | WAF 5800字符 |
| ClawHub | 全部免费 | 10%引流 | clawhub_batch_uploader.py | 200/24h |
| GitHub hermes-skills | 仅免费 | 不推送 | git push hermes-skills | 无 |
| GitHub origin | 全部 | 全部 | git push origin | 无 |

## Git提交记录
| 轮次 | Commit | 文件数 | 变更行数 |
|------|--------|--------|----------|
| Round 40 | cadc4889 | 14 | +646/-2082 |
| Round 41 Phase 1 | (待提交) | - | - |
| Round 41 Phase 2 | (待提交) | - | - |
| Round 41 Phase 3 | (待提交) | - | - |
| Round 41 Phase 4 | (待提交) | - | - |
| Round 41 Phase 5 | (待提交) | - | - |
| Round 41 Phase 6 | (待提交) | - | - |
| Round 41 Phase 7 | (待提交) | - | - |
