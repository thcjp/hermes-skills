# Skill 收集-增强-分发平台

全网收集优秀 Skill，二次包装增强后分为免费版和付费版，上传到 SkillHub、ClawHub、GitHub 三大平台。

## 快速开始

```bash
# 查看项目状态
python tools/orchestrator.py status

# 执行版本同步流水线
python tools/version_sync_pipeline.py scan

# 运行深度质量审计
python tools/deep_quality_audit.py

# ClawHub 批量上传（每日 200 条限制）
python tools/clawhub_batch_uploader.py --dry-run
```

## 目录导航

| 目录 | 说明 |
|------|------|
| `config/` | 统一配置中心（路径、阈值、平台配置） |
| `tools/` | 工具脚本（发现、审计、上传、编排） |
| `data/` | 数据存储（报告、备份、市场数据） |
| `docs/` | 项目文档 |
| `clawhub-skills/downloaded/` | 源 Skill（ClawHub 下载） |
| `packaged-skills/skillhub/` | 产品 Skill — 免费版 |
| `hermes-skills/` | 产品 Skill — GitHub 公开引流 |
| `enterprise-upload/` | 产品 Skill — 付费版 |

## 核心文档

- [架构文档](docs/ARCHITECTURE.md) — 唯一权威架构描述
- [版本同步流水线](docs/version-sync-pipeline.md) — 8 阶段流水线详细说明
- [当前轮次计划](docs/plans/) — 执行计划文档

## 技术栈

- **数据库**：SQLite（`skill-registry.db`）
- **配置**：Python（`config/` 目录统一管理）
- **平台**：SkillHub CLI、ClawHub CLI、Git
- **语言**：Python 3.x
