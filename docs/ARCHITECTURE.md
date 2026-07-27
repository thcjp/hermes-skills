# 项目架构文档

> **唯一权威文档** — 所有架构、流程、配置描述以此为准

## 一、项目定位

本项目是一个 **Skill 收集-增强-分发平台**：

1. **收集** — 每日从 ClawHub、GitHub、开源社区发现并下载已被广泛使用的优秀 Skill
2. **增强** — 对下载的 Skill 进行二次包装、差异化改造、质量优化
3. **定价** — 为增强后的 Skill 设置单一 slug + edition/pricing_model 元数据（v3.0: 不再创建-free/-pro派生副本）
4. **分发** — 上传到固定平台（ClawHub、GitHub 双仓库；SkillHub 账号当前已封禁，待申诉解封）

## 二、目录结构

```
d:\skills\
├── config/                     # 统一配置中心（唯一配置真相源）
│   ├── __init__.py             # 导出所有配置
│   ├── project_config.py       # 路径、常量、阈值
│   ├── platform_config.py      # 平台 URL、API、限流、GitHub 双仓库
│   └── github_repo_strategy.py # GitHub 仓库策略
│
├── tools/                      # 工具脚本（生产工具，非产品）
│   ├── orchestrator.py         # 统一编排入口
│   ├── version_sync_pipeline.py# 版本同步流水线
│   ├── deep_quality_audit.py   # L4-L8 深度质量审计
│   ├── auto_discover.py        # Skill 发现与变更检测
│   ├── clawhub_batch_uploader.py # ClawHub 批量上传
│   ├── dashboard_server.py     # 看板服务
│   ├── config.py               # 向后兼容 shim（转发到 config/）
│   └── ...                     # 其余工具脚本
│
├── data/                       # 数据存储（非代码）
│   ├── reports/                # 审计报告 JSON
│   ├── health_reports/         # 健康检查报告
│   ├── market-data/            # 市场数据
│   ├── backups/                # 数据库备份（.gitignored）
│   └── discovery/              # 发现候选数据
│
├── docs/                       # 项目文档
│   ├── ARCHITECTURE.md         # 本文件（唯一架构文档）
│   ├── README.md               # 项目入口
│   ├── version-sync-pipeline.md# 8 阶段流水线详细文档
│   ├── plans/                  # 计划文档
│   │   ├── archive/            # 历史计划归档
│   │   └── next-round-prompt-v*.md
│   └── reports/                # 审查报告
│
├── clawhub-skills/downloaded/  # 源 Skill（ClawHub 下载）
├── packaged-skills/skillhub/   # 产品 Skill — 免费版（SkillHub）
├── hermes-skills/              # 产品 Skill — 免费版（GitHub 公开引流）
├── opensource-skills/          # 产品 Skill — 开源版
├── enterprise-upload/          # 产品 Skill — 付费版
├── differentiated-skills/      # 差异化日志
│
├── .credentials/               # 凭证存储（.gitignored）
├── skill-registry.db           # 唯一数据库
├── .gitignore
└── README.md                   # 项目入口
```

## 三、单一Slug + Edition模型 (v3.0重构)

v3.0安全增强后，每个产品 Skill 使用**单一 slug + edition/pricing_model 元数据**区分版本，不再创建-free/-pro独立slug。

> **根因**: 2026-07-24批量上传中，990+个-free/-pro派生skill被平台内容指纹系统识别为"近似重复内容"并批量封禁（封禁率93.4%）。详见 `data/reports/banned_skills_root_cause_analysis.md`。

| 字段 | 说明 | 示例 |
|------|------|------|
| `slug` | 唯一标识符（kebab-case） | `crypto-portfolio` |
| `edition` | 版本类型 | `paid` / `free_merged`（历史遗留） |
| `pricing_model` | 定价模式 | `per_call` / `monthly` / `free` / `freemium` |
| `parent_slug` | 父Skill的slug（差异化派生时） | `crypto-portfolio` |

历史遗留的-free/-pro slug通过 `clean_naming.py` 合并治理：
- 免费版记录标记为 `current_status='deleted'`，`edition='free_merged'`
- 付费版记录继承为唯一slug，`edition='paid'`

## 四、8 阶段流水线（唯一权威描述）

```
1. DISCOVER      — 发现新 Skill + 检测已有 Skill 变更
2. ENHANCE       — 内容增强（基于审计报告识别 B 级 Skill）
3. INCREMENT     — 版本号递增（patch 级）
4. VALIDATE      — L1-L8 全量质量审计
5. SYNC_GITHUB   — GitHub 双仓库同步（免费→hermes-skills，全部→origin）
6. SYNC_SKILLHUB — SkillHub 免费+付费同步
7. SYNC_CLAWHUB  — ClawHub 同步（定时任务自动）
8. RECORD        — 数据库记录（versions + platform_uploads + operations）
```

详细说明见 [version-sync-pipeline.md](version-sync-pipeline.md)。

## 五、L1-L8 审计体系（唯一权威描述）

| 层级 | 名称 | 脚本 | 说明 |
|------|------|------|------|
| L1 | 格式合规 | `quality_gate.py` | frontmatter 格式检查 |
| L2 | 能力评估 | `l2_capability_checker.py` | 基础能力检查 |
| L3 | 功能验证 | `l3_function_checker.py` | 功能完整性检查 |
| L4 | 功能质量 | `deep_quality_audit.py` | 八大维度评分 |
| L5 | 可销售性 | `deep_quality_audit.py` | 商业化评估 |
| L6 | 内容真实性 | `deep_quality_audit.py` | 内容真实性检查 |
| L7a | 语义模板 | `deep_quality_audit.py` | 语义模板审计（默认启用） |
| L7b | 可执行性 | `deep_quality_audit.py` | 可执行性审计 |
| L8 | 安全审计 | `deep_quality_audit.py` | 安全合规审计 |

## 六、平台策略（唯一权威描述）

| 平台 | 状态 | 上传方式 | 限流 | 备注 |
|------|------|----------|------|------|
| SkillHub | **已封禁** | CLI `skillhub publish` | WAF 5800 字符 | 账号org-xxo535hs已被封禁(404/401)，待申诉解封 |
| ClawHub | 活跃 | `clawhub publish` | 30/hour, 100/day, 2min间隔 | v3.0速率限制已集成到clawhub_batch_uploader |
| GitHub hermes-skills | 活跃 | `git push` | 无 | 公开引流仓库 |
| GitHub origin | 活跃 | `git push` | 无 | 私有备份仓库（URL已修正为hermes-skills.git） |

### GitHub 双仓库策略

- **公开引流仓库** (`hermes-skills`)：`https://github.com/thcjp/hermes-skills`，推送全部 Skill + 项目代码
- **私有备份仓库** (`origin`)：与hermes-skills同URL（v3.0修正，原`-.git`URL已废弃）

### SkillHub账号封禁状态

- **组织**: 科创少年 (org-xxo535hs, orgId: 862)
- **封禁时间**: 2026-07-24之后
- **根因**: 单日爆发式上传1098个Skill + 990+个近似重复派生内容 + 136个-sk系列slug变异
- **影响**: 1378/1476 (93.4%) Skill被封禁，组织公开API返回404，管理员API返回401
- **申诉策略**: 详见 `data/reports/skillhub_account_ban_analysis_and_unban_strategy.md`

## 七、配置系统

所有配置统一从 `config/` 目录导入，消除硬编码：

```python
# 使用方式
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
from project_config import DB_PATH, TOOLS_DIR, DATA_DIR, TRACE_PASS_THRESHOLD
from platform_config import GITHUB_REPOS, is_free_skill
```

关键配置项：
- `DB_PATH` — 唯一数据库路径 `d:\skills\skill-registry.db`
- `TRACE_PASS_THRESHOLD` — 评分通过阈值 42
- `TOOLS_DIR` — 工具脚本目录 `d:\skills\tools`
- `DATA_DIR` — 数据存储目录 `d:\skills\data`

## 八、数据库 Schema

### 核心表

| 表名 | 记录数 | 说明 |
|------|--------|------|
| `skills` | ~2882 | Skill 主表，含三轨模型字段 |
| `versions` | ~4690 | 版本记录 |
| `platform_uploads` | ~3459 | 平台上传记录 |
| `scores` | ~4295 | 评分记录 |
| `pricing` | ~1916 | 定价记录 |
| `sources` | ~656 | 源信息 |
| `operations` | ~11470 | 操作日志 |
| `workflow_states` | ~14413 | 工作流状态 |
| `skills_fts` | FTS5 | 全文搜索（触发器自动同步） |

### 看板视图

| 视图名 | 说明 |
|--------|------|
| `v_skill_lifecycle` | Skill 生命周期看板（含三平台上传状态） |
| `v_platform_summary` | 平台上传汇总 |
| `v_three_track_overview` | 三轨模型概览 |

## 九、触发机制

### 自动发现
- **触发条件**：每日定时执行
- **脚本**：`tools/auto_discover.py`
- **输出**：`data/discovery/candidates.json`

### 版本同步
- **触发条件**：检测到变更后
- **脚本**：`tools/version_sync_pipeline.py`
- **8 阶段**：DISCOVER → ENHANCE → INCREMENT → VALIDATE → SYNC_GITHUB → SYNC_SKILLHUB → SYNC_CLAWHUB → RECORD

### ClawHub 定时上传
- **触发条件**：每日 12:00（北京时间）
- **脚本**：`tools/clawhub_batch_uploader.py`
- **限制**：200 条/24 小时
