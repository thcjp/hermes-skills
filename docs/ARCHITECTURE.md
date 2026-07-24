# 项目架构文档

> **唯一权威文档** — 所有架构、流程、配置描述以此为准

## 一、项目定位

本项目是一个 **Skill 收集-增强-分发平台**：

1. **收集** — 每日从 ClawHub、GitHub、开源社区发现并下载已被广泛使用的优秀 Skill
2. **增强** — 对下载的 Skill 进行二次包装、差异化改造、质量优化
3. **拆分** — 将增强后的 Skill 分为免费版和付费版
4. **分发** — 上传到固定平台（SkillHub、ClawHub、GitHub 双仓库）

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

## 三、三轨模型

每个产品 Skill 应该有三轨，数据库通过 `skills` 表的 `skill_type`、`source_slug`、`free_slug`、`paid_slug` 字段关联：

| 轨道 | skill_type | 目录 | 说明 |
|------|-----------|------|------|
| 源 | `source` | `clawhub-skills/downloaded/` | 从外部下载的原始 Skill |
| 免费版 | `free` | `packaged-skills/skillhub/` | 增强后的免费版 |
| 付费版 | `paid` | `enterprise-upload/` | 增强后的付费版 |

数据库关联字段：
- `skills.source_slug` → 源 Skill 的 slug
- `skills.free_slug` → 免费版的 slug
- `skills.paid_slug` → 付费版的 slug
- `skills.parent_slug` → 父 Skill 的 slug（免费版指向源，付费版指向免费版）

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

| 平台 | 免费版 | 付费版 | 上传方式 | 限流 |
|------|--------|--------|----------|------|
| SkillHub | CLI `skillhub publish` | 浏览器 | `skillhub publish` | WAF 5800 字符 |
| ClawHub | 全部 | 10% 引流 | `npx clawhub publish` | 200/24h |
| GitHub hermes-skills | 仅免费 | 不推送 | `git push` | 无 |
| GitHub origin | 全部 | 全部 | `git push` | 无 |

### GitHub 双仓库策略

- **公开引流仓库** (`hermes-skills`)：`https://github.com/thcjp/hermes-skills`，仅推送免费 Skill
- **私有备份仓库** (`origin`)：`https://github.com/thcjp/-.git`，推送全部 Skill + 项目代码

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
