# 项目架构治理设计文档

> **日期**: 2026-07-24
> **方案**: 方案A - 渐进式彻底治理
> **原则**: 不移动2000+个产品skill目录,重构配置/工具/数据/文档层,确保彻底完成

## 一、问题诊断

### 1.1 配置散乱(严重)
- `DB_PATH` 在5处脚本中硬编码绕过config.py(实际扫描: orchestrator.py, version_sync_pipeline.py, db.py, analyze_status.py, dashboard_server.py)
- `TRACE_PASS_THRESHOLD=42` vs 数据库`scores`表默认值40,阈值不一致
- `GITHUB_REPOS`在auto_discover.py和github_scanner.py两处定义且结构不同
- `CLAWHUB_DOWNLOADED_DIR`在2处重复硬编码
- config.py缺少HERMES_SKILLS_DIR、ENTERPRISE_UPLOAD_DIR、DIFFERENTIATED_DIR等路径
- `pricing_tier`格式不统一: "L3" vs "L3-专业级" 两种格式共存(实际: L3=801, L3-专业级=160)

### 1.2 工具/产品物理混合(严重)
- `skill-registry/`包含69个工具脚本 + 957个JSON数据文件 + 模板 + 报告
- 顶层散落5个.ps1脚本、1个.sh脚本、8个审核报告.md文件
- 工具脚本与数据文件混在同一目录,无法区分

### 1.3 数据库冗余(严重)
- 7个数据库文件分布在3个位置(5个为空文件或备份,仅1个活跃)
- `dependencies`表完全空置(0行)
- `operations.skill_id`的NOT NULL约束在实际DB中未生效
- FTS全文搜索表(skills_fts*)全部为空,搜索功能不可用
- 0个视图存在,无法直接从数据库读取skill生命周期看板数据

### 1.4 文档矛盾(严重)
- 版本同步流水线在3处描述为不同阶段数(8/10/5)
- 质量审计层数在6处描述为不同数字(8层/6层/5维度)
- 上传命令名称不一致(`clawhub` vs `npx clawhub publish` vs `skillhub publish`)
- 10个审核报告v1/v2双版本共存,43+个Round计划文档未归档
- 无ARCHITECTURE.md,README.md几乎为空

### 1.5 源/免费/付费不清晰
- 源skill在`clawhub-skills/downloaded/`(600个SKILL.md)
- 免费版在`packaged-skills/skillhub/`(995个) + `hermes-skills/`(759个) + `opensource-skills/packaged/`(40个)
- 付费版在`enterprise-upload/`(仅2个)
- 数据库skills表已有`skill_type`字段但语义不符(现有值: None=1841, differentiated=71, md_exec=300, opensource_modified=39, original_creation=23, original_download=600, tool=8)
- 已有`source_slug`字段且65%已填充(1886/2882),但缺少`free_slug`和`paid_slug`关联字段
- `is_paid`字段有573个NULL值,`edition`字段分布: free=2124, pro=454, paid=262
- 无法从数据库直接查询某个skill的三轨状态和各平台上传状态

## 二、目标架构

### 2.1 治理后的目录结构

```
d:\skills\
├── config/                              # 【新建】统一配置中心
│   ├── __init__.py                      # 导出所有配置
│   ├── project_config.py                # 路径、常量、阈值
│   ├── platform_config.py               # 平台URL、API、限流
│   └── github_repo_strategy.py          # GitHub双仓库策略(从skill-registry移入)
│
├── tools/                               # 【重命名】工具脚本(原skill-registry/)
│   ├── core/                            # 核心模块(原skill_core/)
│   │   ├── db.py                        # 数据库连接
│   │   ├── parser.py                    # SKILL.md解析器
│   │   └── checks.py                    # 检查规则
│   ├── discovery/                       # 发现工具脚本
│   ├── audit/                           # 审计工具脚本
│   ├── upload/                          # 上传工具脚本
│   ├── templates/                       # 生成模板(原templates/)
│   ├── scripts/                         # 辅助脚本(原顶层.ps1/.sh)
│   ├── orchestrator.py                  # 统一编排
│   ├── version_sync_pipeline.py         # 版本同步流水线
│   ├── deep_quality_audit.py            # 深度质量审计
│   ├── clawhub_batch_uploader.py        # ClawHub批量上传
│   └── ... (其余69个.py文件)
│
├── data/                                # 【新建】数据存储
│   ├── reports/                         # 审计报告JSON(原skill-registry/*.json)
│   ├── health_reports/                  # 健康检查报告
│   ├── market-data/                     # 市场数据
│   ├── backups/                         # 数据库备份
│   ├── discovery/                       # 发现候选数据
│   ├── upload_tracking.json             # 上传追踪(5.8MB)
│   ├── clawhub_published_slugs.json     # ClawHub已发布列表
│   ├── clawhub_upload_checkpoint.json   # 上传断点续传
│   └── category_mapping.json            # 分类映射
│
├── docs/                                # 【重组】项目文档
│   ├── ARCHITECTURE.md                  # 【新建】唯一架构文档
│   ├── README.md                        # 【重写】项目入口
│   ├── version-sync-pipeline.md         # 流水线文档(保留,更新路径)
│   ├── plans/                           # 计划文档
│   │   ├── next-round-prompt-v41.0.md   # 当前轮次
│   │   └── archive/                     # 【新建】历史计划归档
│   └── reports/                         # 【新建】报告文档
│       ├── quality-analysis.md          # 质量分析(从顶层移入)
│       └── security-analysis.md         # 安全分析(从顶层移入)
│
├── packaged-skills/skillhub/            # 产品skill-免费版(SkillHub) - 保持不动
├── hermes-skills/                       # 产品skill-免费版(Hermes) - 保持不动
├── opensource-skills/packaged/          # 产品skill-开源版 - 保持不动
├── enterprise-upload/                   # 产品skill-付费版 - 保持不动
├── clawhub-skills/downloaded/           # 源skill(ClawHub下载) - 保持不动
├── differentiated-skills/               # 差异化日志 - 保持不动
│
├── .credentials/                        # 凭证存储(原.skillhub-credentials)
├── skill-registry.db                    # 唯一数据库
├── .gitignore
├── PROJECT_MEMORY.md                    # 项目记忆(gitignored)
└── README.md                            # 项目入口(重写)
```

### 2.2 关键设计决策

| 决策 | 理由 |
|------|------|
| 产品skill目录不移动 | 996+759+40个skill目录移动风险过高,且目录命名已与平台对应 |
| skill-registry/重命名为tools/ | 明确标识为工具脚本,与产品物理隔离 |
| 新建config/目录 | 配置独立于工具脚本,所有脚本统一导入 |
| 新建data/目录 | 数据文件与工具脚本分离,957个JSON不再混在脚本目录 |
| 新建docs/reports/ | 顶层报告文件归入docs统一管理 |
| 历史计划归档到docs/plans/archive/ | 43+个Round计划不再淹没当前文档 |

## 三、详细任务清单

### Phase 1: 统一配置中心 (P0)

**目标**: 消除8处DB_PATH冗余,所有脚本统一从config/导入

#### Task 1.1: 创建config/目录和模块
- 创建 `config/__init__.py` - 导出所有配置
- 创建 `config/project_config.py` - 扩展现有config.py,添加缺失路径:
  - `TOOLS_DIR` = PROJECT_ROOT / "tools"
  - `DATA_DIR` = PROJECT_ROOT / "data"
  - `CLAWHUB_DOWNLOADED_DIR` = PROJECT_ROOT / "clawhub-skills" / "downloaded"
  - `HERMES_SKILLS_DIR` = PROJECT_ROOT / "hermes-skills"
  - `ENTERPRISE_UPLOAD_DIR` = PROJECT_ROOT / "enterprise-upload"
  - `DIFFERENTIATED_DIR` = PROJECT_ROOT / "differentiated-skills"
- 创建 `config/platform_config.py` - 平台配置:
  - SkillHub: CLI路径、API URL、WAF限制(5800字符)
  - ClawHub: 上传限制(200/24h)、Token路径
  - GitHub: 双仓库remote配置、分支
- 移动 `github_repo_strategy.py` → `config/github_repo_strategy.py`

#### Task 1.2: 修改7个硬编码脚本
- `db.py`: 删除硬编码DB_PATH,改为`from config import DB_PATH`
- `analyze_status.py`: 同上
- `auto_discover.py`: 删除DB_PATH、SKILLS_ROOT、CLAWHUB_DOWNLOADED_DIR硬编码
- `dashboard_server.py`: 删除DB_PATH、REGISTRY_DIR硬编码
- `clean_naming.py`: 删除DB_PATH硬编码
- `github_scanner.py`: 删除DB_PATH、GITHUB_REPOS硬编码
- `init_baseline.py`: 删除DB_PATH、SKILLS_ROOT硬编码

#### Task 1.3: 修复阈值不一致
- 数据库`scores`表`pass_threshold`默认值: 40 → 42
- 确保所有脚本使用`config.TRACE_PASS_THRESHOLD`

#### Task 1.4: 更新所有脚本的import路径
- 全部从`from config import ...`改为`from config import ...`(新模块)
- 添加`sys.path.insert(0, str(Path(__file__).parent.parent / "config"))`确保跨目录导入

**验证标准**:
- `grep -r "d:\\\\skills\\\\skill-registry.db" tools/` 返回0结果(无硬编码)
- 所有脚本可正常import config
- 数据库阈值统一为42

### Phase 2: 工具/产品物理分离 (P0)

**目标**: skill-registry/ → tools/, 数据文件 → data/

#### Task 2.1: 创建data/目录结构
- `data/reports/` - 审计报告JSON
- `data/health_reports/` - 健康检查报告
- `data/market-data/` - 市场数据
- `data/backups/` - 数据库备份
- `data/discovery/` - 发现候选数据

#### Task 2.2: 移动数据文件到data/
- `skill-registry/*.json` → `data/reports/` (报告类JSON)
- `skill-registry/health_reports/` → `data/health_reports/`
- `skill-registry/market-data/` → `data/market-data/`
- `skill-registry/backups/` → `data/backups/`
- `skill-registry/discovery/` → `data/discovery/`
- 保留状态文件在data/根: `upload_tracking.json`, `clawhub_published_slugs.json`, `clawhub_upload_checkpoint.json`, `category_mapping.json`

#### Task 2.3: 重命名skill-registry/ → tools/
- `skill-registry/*.py` → `tools/*.py`
- `skill-registry/skill_core/` → `tools/core/`
- `skill-registry/templates/` → `tools/templates/`
- 删除空的skill-registry/目录

#### Task 2.4: 移动顶层脚本到tools/scripts/
- `retry-skillhub.ps1` → `tools/scripts/`
- `retry-skillhub-v2.ps1` → `tools/scripts/`
- `run-skillhub.sh` → `tools/scripts/`
- `skillhub.ps1` → `tools/scripts/`
- `upload-differentiated.ps1` → `tools/scripts/`
- `upload-to-skillhub.ps1` → `tools/scripts/`

#### Task 2.5: 更新所有路径引用
- config.py中REGISTRY_DIR改为TOOLS_DIR
- 所有脚本中的`skill-registry`路径引用改为`tools`
- orchestrator.py中的脚本路径更新
- version_sync_pipeline.py中的路径更新
- .gitignore更新

**验证标准**:
- `skill-registry/`目录不存在
- `tools/`目录包含所有.py脚本
- `data/`目录包含所有数据文件
- 所有脚本可正常运行

### Phase 3: 数据库清理和增强 (P1)

**目标**: 删除冗余DB,增强三轨模型

#### Task 3.1: 删除冗余数据库文件
- 删除 `d:\skills\skills.db`
- 删除 `d:\skills\skill-registry.db.backup_20260720_092727`
- 删除 `d:\skills\skill-registry.db.bak_pricing_fix`
- 删除 `d:\skills\skill-registry\skill-registry.db`
- 删除 `d:\skills\skill-registry\skills.db`
- 删除 `d:\skills\skill-registry\skill_registry.db`
- 保留 `d:\skills\skill-registry.db` (唯一数据库)

#### Task 3.2: 数据库schema增强
```sql
-- skill_type字段已存在(语义不符,需迁移值),source_slug已存在(65%已填充)
-- 仅需新增free_slug和paid_slug字段
ALTER TABLE skills ADD COLUMN free_slug TEXT;
ALTER TABLE skills ADD COLUMN paid_slug TEXT;
CREATE INDEX IF NOT EXISTS idx_skills_type ON skills(skill_type);
CREATE INDEX IF NOT EXISTS idx_skills_source ON skills(source_slug);
CREATE INDEX IF NOT EXISTS idx_skills_free ON skills(free_slug);
CREATE INDEX IF NOT EXISTS idx_skills_paid ON skills(paid_slug);
```

#### Task 3.2b: 迁移现有skill_type值到三轨模型
现有skill_type值需映射到source|free|paid:
```sql
-- 迁移映射:
-- original_download → source (从外部下载的原始skill)
-- clawhub_download → source
-- differentiated → free (差异化后的免费版)
-- md_exec → free (markdown可执行版)
-- opensource_modified → free (开源修改版)
-- original_creation → free (原创免费版)
-- tool → tool (项目工具,不属于产品skill)
-- NULL → 根据目录位置自动判断

UPDATE skills SET skill_type = 'source' WHERE skill_type IN ('original_download', 'clawhub_download');
UPDATE skills SET skill_type = 'free' WHERE skill_type IN ('differentiated', 'md_exec', 'opensource_modified', 'original_creation');
-- NULL值根据local_path判断
UPDATE skills SET skill_type = 'source' WHERE skill_type IS NULL AND local_path LIKE '%clawhub-skills/downloaded%';
UPDATE skills SET skill_type = 'free' WHERE skill_type IS NULL AND (local_path LIKE '%packaged-skills%' OR local_path LIKE '%hermes-skills%' OR local_path LIKE '%opensource-skills%');
UPDATE skills SET skill_type = 'paid' WHERE skill_type IS NULL AND local_path LIKE '%enterprise-upload%';
```

#### Task 3.2c: 规范化pricing_tier格式
```sql
-- 统一为带中文后缀的格式
UPDATE skills SET pricing_tier = 'L1-入门级' WHERE pricing_tier = 'L1';
UPDATE skills SET pricing_tier = 'L2-标准级' WHERE pricing_tier = 'L2';
UPDATE skills SET pricing_tier = 'L3-专业级' WHERE pricing_tier = 'L3';
UPDATE skills SET pricing_tier = 'L4-企业级' WHERE pricing_tier = 'L4';
-- 填充NULL和空值
UPDATE skills SET pricing_tier = 'L1-入门级' WHERE pricing_tier IS NULL OR pricing_tier = '' AND edition = 'free';
UPDATE skills SET pricing_tier = 'L3-专业级' WHERE pricing_tier IS NULL OR pricing_tier = '' AND edition IN ('pro', 'paid');
```

#### Task 3.3: 数据迁移-填充三轨关联字段
- Task 3.2b已将skill_type迁移为source|free|paid|tool
- 填充free_slug: 对free类型skill, free_slug = slug自身
- 填充paid_slug: 对paid类型skill, paid_slug = slug自身; 对free类型skill, 查找同parent_slug的paid版
- 填充source_slug: 对已有source_slug的保留, 对NULL的根据local_path推断
- 差异化日志(differentiated-skills/1102个)需导入数据库并标记skill_type
```sql
-- 填充free_slug
UPDATE skills SET free_slug = slug WHERE skill_type = 'free' AND free_slug IS NULL;
-- 填充paid_slug
UPDATE skills SET paid_slug = slug WHERE skill_type = 'paid' AND paid_slug IS NULL;
-- 关联free和paid (同parent_slug)
UPDATE skills SET paid_slug = (
    SELECT s2.slug FROM skills s2
    WHERE s2.parent_slug = skills.parent_slug AND s2.skill_type = 'paid'
    LIMIT 1
) WHERE skill_type = 'free' AND paid_slug IS NULL AND parent_slug IS NOT NULL;
```

#### Task 3.4: 清理空表和修复约束
- 删除空表dependencies或添加注释标记为预留
- 记录operations表约束不一致问题
- 重建FTS全文搜索表(当前全部为空):
```sql
-- 重建FTS索引
DELETE FROM skills_fts;
INSERT INTO skills_fts(skill_id, slug, display_name, summary, category)
SELECT id, slug, current_display_name, summary, category FROM skills WHERE current_status IN ('active', 'updated');
```

#### Task 3.5: 创建看板视图
```sql
-- 使用窗口函数替代关联子查询,提高查询性能
CREATE VIEW v_skill_lifecycle AS
WITH latest_uploads AS (
    SELECT
        skill_id, platform, upload_status,
        ROW_NUMBER() OVER (PARTITION BY skill_id, platform ORDER BY upload_date DESC) as rn
    FROM platform_uploads
)
SELECT
    s.slug, s.display_name, s.skill_type,
    s.source_slug, s.free_slug, s.paid_slug,
    s.current_version, s.current_status,
    s.pricing_tier, s.edition, s.is_paid,
    s.category, s.source,
    sh.upload_status as skillhub_status,
    ch.upload_status as clawhub_status,
    gh.upload_status as github_status,
    s.updated_at as last_updated
FROM skills s
LEFT JOIN latest_uploads sh ON sh.skill_id = s.id AND sh.platform = 'skillhub' AND sh.rn = 1
LEFT JOIN latest_uploads ch ON ch.skill_id = s.id AND ch.platform = 'clawhub' AND ch.rn = 1
LEFT JOIN latest_uploads gh ON gh.skill_id = s.id AND gh.platform = 'github' AND gh.rn = 1
WHERE s.current_status IN ('active', 'updated');
```

**验证标准**:
- 仅1个数据库文件存在
- skills表有skill_type/source_slug/free_slug/paid_slug字段
- v_skill_lifecycle视图可查询
- 0个冗余DB文件

### Phase 4: 文档统一 (P1)

**目标**: 消除文档矛盾,创建唯一权威文档

#### Task 4.1: 创建ARCHITECTURE.md
唯一架构文档,包含:
- 项目概述和特色(收集→增强→拆分→上传)
- 目录结构说明
- 数据流图: 发现→下载→增强→审计→拆分免费/付费→上传→记录
- 8阶段流水线(唯一权威描述)
- L1-L8审计体系(唯一权威描述)
- 平台策略(SkillHub/ClawHub/GitHub双仓库)
- 数据库schema
- 配置系统说明

#### Task 4.2: 重写README.md
- 项目简介
- 快速开始
- 目录结构导航
- 文档索引

#### Task 4.3: 统一流程描述
- 删除/合并 `docs/plans/full-automation-pipeline-design.md` 中的10步描述
- 删除/合并 `skill-registry/WORKFLOW_INTEGRITY_REPORT.md` 中的5阶段描述
- 统一为8阶段(以version_sync_pipeline.py为准)
- 统一审计层数为L1-L8

#### Task 4.4: 清理冗余文档
- 删除v1审核报告(5个),保留v2
- 归档历史Round计划到 `docs/plans/archive/`
- 合并 `UPLOAD-GUIDE.md` → `docs/ARCHITECTURE.md`
- 合并 `DISCOVER_TRIGGER.md`, `UPDATE_TRIGGER.md`, `GOVERNANCE_TRIGGER.md` → `docs/ARCHITECTURE.md`
- 删除 `skill-registry/WORKFLOW_INTEGRITY_REPORT.md` (合并到ARCHITECTURE.md)
- 移动顶层报告到 `docs/reports/`

**验证标准**:
- ARCHITECTURE.md存在且包含完整架构描述
- README.md有实质内容
- 0个v1审核报告
- 历史Round计划在archive/目录
- 流水线描述仅1处(8阶段)

### Phase 5: 顶层文件清理 (P2)

**目标**: 顶层目录干净整洁

#### Task 5.1: 移动顶层文件
- 6个脚本 → `tools/scripts/`
- 5个v1审核报告 → 删除
- 3个报告.md → `docs/reports/`
- `skill_verification_report.html` → 删除(临时文件)
- `clawhub-config.json` → `config/`

#### Task 5.2: 清理空目录
- 删除 `packaged-skills/coze/` (空)
- 删除 `packaged-skills/promptbase/` (空)
- 删除 `packaged-skills/agent-ai/` (空)
- 删除 `packaged-skills/failed-temp/` (空)

#### Task 5.3: 清理日志版本冗余
- 删除 `clawhub-skills/download-log.csv` (保留v2)
- 删除 `packaged-skills/upload-log.csv` (保留v2)
- 删除 `retry-skillhub.ps1` (保留v2)

#### Task 5.4: 重命名凭证目录
- `.skillhub-credentials/` → `.credentials/`
- 更新所有脚本中的引用

**验证标准**:
- 顶层仅保留: config/, tools/, data/, docs/, 产品skill目录, .credentials/, skill-registry.db, .gitignore, README.md, PROJECT_MEMORY.md
- 0个空目录
- 0个v1/v2冗余

### Phase 6: 全量验证 (P0)

**目标**: 确保重构后系统功能正常

#### Task 6.1: 脚本运行验证
- `python tools/orchestrator.py status` 正常输出
- `python tools/version_sync_pipeline.py scan` 正常输出
- `python tools/deep_quality_audit.py` 正常运行
- `python tools/clawhub_batch_uploader.py --dry-run` 正常运行

#### Task 6.2: 配置一致性验证
- `grep -r "skill-registry" tools/*.py` 仅出现在注释中
- `grep -r "d:\\\\skills\\\\skill-registry.db" tools/` 返回0结果
- 所有脚本的DB_PATH来自config

#### Task 6.3: 数据库完整性验证
- skills表记录数 = 2882
- v_skill_lifecycle视图可查询
- platform_uploads表记录完整

#### Task 6.4: Git提交
- 提交所有变更
- 推送到origin(私有备份)

## 四、项目特色流程(唯一权威描述)

### 4.1 项目定位

本项目是一个**Skill收集-增强-分发平台**:
1. **收集**: 每日从ClawHub、GitHub、开源社区发现并下载优秀skill
2. **增强**: 对下载的skill进行二次包装、差异化、质量优化
3. **拆分**: 将增强后的skill分为免费版和付费版
4. **分发**: 上传到固定平台(SkillHub、ClawHub、GitHub)

### 4.2 8阶段流水线(唯一权威)

```
1. DISCOVER     - 发现新skill + 检测已有skill变更
2. ENHANCE      - 内容增强建议(基于审计报告识别B级skill)
3. INCREMENT    - 版本号递增(patch级)
4. VALIDATE     - L1-L8全量质量审计
5. SYNC_GITHUB  - GitHub双仓库同步(免费→hermes-skills, 全部→origin)
6. SYNC_SKILLHUB - SkillHub免费+付费同步
7. SYNC_CLAWHUB  - ClawHub同步(定时任务自动)
8. RECORD       - 数据库记录(versions + platform_uploads + operations)
```

### 4.3 L1-L8审计体系(唯一权威)

| 层级 | 名称 | 脚本 | 说明 |
|------|------|------|------|
| L1 | 格式合规 | quality_gate.py | frontmatter格式检查 |
| L2 | 能力评估 | l2_capability_checker.py | 基础能力检查 |
| L3 | 功能验证 | l3_function_checker.py | 功能完整性检查 |
| L4 | 功能质量 | deep_quality_audit.py | 八大维度评分 |
| L5 | 可销售性 | deep_quality_audit.py | 商业化评估 |
| L6 | 内容真实性 | deep_quality_audit.py | 内容真实性检查 |
| L7a | 语义模板 | deep_quality_audit.py | 语义模板审计 |
| L7b | 可执行性 | deep_quality_audit.py | 可执行性审计 |
| L8 | 安全审计 | deep_quality_audit.py | 安全合规审计 |

### 4.4 平台策略(唯一权威)

| 平台 | 免费版 | 付费版 | 上传方式 | 限流 |
|------|--------|--------|----------|------|
| SkillHub | ✅ CLI | ✅ 浏览器 | skillhub publish | WAF 5800字符 |
| ClawHub | ✅ 全部 | ✅ 10%引流 | npx clawhub publish | 200/24h |
| GitHub hermes-skills | ✅ 仅免费 | ❌ | git push | 无 |
| GitHub origin | ✅ 全部 | ✅ 全部 | git push | 无 |

### 4.5 三轨模型

每个产品skill应该有三轨:

| 轨道 | skill_type | 目录 | 说明 |
|------|-----------|------|------|
| 源 | source | clawhub-skills/downloaded/ | 从外部下载的原始skill |
| 免费版 | free | packaged-skills/skillhub/ | 增强后的免费版 |
| 付费版 | paid | enterprise-upload/ | 增强后的付费版 |

数据库关联:
- `skills.source_slug` → 源skill的slug
- `skills.free_slug` → 免费版的slug
- `skills.paid_slug` → 付费版的slug

## 五、风险和缓解

| 风险 | 缓解措施 |
|------|----------|
| 脚本import路径断裂 | 先创建config/,再逐步修改脚本,每个脚本修改后立即验证 |
| 数据库迁移数据丢失 | 迁移前备份,仅添加列不删除列 |
| 定时任务路径失效 | 更新定时任务中的脚本路径 |
| Git历史丢失 | 使用git mv保留历史 |

## 六、验证检查清单

- [ ] config/目录存在,包含project_config.py, platform_config.py, github_repo_strategy.py
- [ ] 0个脚本硬编码DB_PATH
- [ ] tools/目录存在,包含所有.py脚本
- [ ] data/目录存在,包含所有数据文件
- [ ] skill-registry/目录不存在
- [ ] 顶层仅有: config/, tools/, data/, docs/, 产品skill目录, .credentials/, skill-registry.db, .gitignore, README.md
- [ ] 仅1个数据库文件
- [ ] skills表有skill_type/source_slug/free_slug/paid_slug字段
- [ ] v_skill_lifecycle视图存在
- [ ] ARCHITECTURE.md存在且完整
- [ ] README.md有实质内容
- [ ] 0个v1审核报告
- [ ] 历史Round计划在docs/plans/archive/
- [ ] 流水线描述仅1处(8阶段)
- [ ] 审计层数描述仅1处(L1-L8)
- [ ] orchestrator.py status正常运行
- [ ] version_sync_pipeline.py scan正常运行
- [ ] deep_quality_audit.py正常运行
