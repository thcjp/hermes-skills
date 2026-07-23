# 版本同步流水线 (Version Sync Pipeline)

## 概述

版本同步流水线实现了从本地skill变更检测到多平台同步的端到端自动化流程。覆盖 GitHub开放库、SkillHub(免费+付费)、ClawHub三个平台，以SQLite数据库为唯一权威数据源。

## 架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                    orchestrator.py (统一编排)                     │
│                                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │ DISCOVER │→│ ENHANCE  │→│  AUDIT   │→│   SYNC   │→RECORD  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘        │
│       │              │              │              │              │
└───────┼──────────────┼──────────────┼──────────────┼──────────────┘
        │              │              │              │
        ▼              ▼              ▼              ▼
┌───────────────┐ ┌──────────┐ ┌──────────────┐ ┌─────────────────┐
│auto_discover   │ │审计报告   │ │deep_quality  │ │version_sync     │
│version_sync    │ │JSON读取  │ │_audit.py     │ │_pipeline.py     │
│_pipeline.py    │ │B级识别   │ │L1-L8全量审计  │ │sync_to_github   │
│scan            │ │          │ │              │ │sync_to_skillhub │
└───────────────┘ └──────────┘ └──────────────┘ │sync_to_clawhub  │
                                                  └─────────────────┘
                                                         │
                          ┌──────────────┬───────────────┼──────────────┐
                          ▼              ▼               ▼              ▼
                   ┌──────────┐  ┌─────────────┐  ┌──────────┐  ┌──────────┐
                   │ GitHub   │  │ SkillHub    │  │ ClawHub  │  │ Database │
                   │ git push │  │ CLI + API   │  │ npx CLI  │  │ SQLite   │
                   └──────────┘  └─────────────┘  └──────────┘  └──────────┘
```

## 8阶段流程

### 阶段1: DISCOVER (发现)
- **脚本**: `auto_discover.py scan` + `version_sync_pipeline.py scan`
- **功能**: 扫描新skill + 检测已有skill的SKILL.md变更(通过SHA-256 hash对比)
- **扫描目录**:
  - `packaged-skills/skillhub/` → source: packaged
  - `opensource-skills/packaged/` → source: opensource
  - `differentiated-skills/` → source: differentiated
- **输出**: `version_sync_scan_report.json` (变更skill列表)

### 阶段2: ENHANCE (增强)
- **脚本**: `orchestrator.py enhance`
- **功能**: 基于审计报告识别B级skill，生成增强建议
- **数据源**: `deep_quality_audit_report.json`
- **识别维度**: L5可销售性B级、L7b可执行性B级、L6内容真实性问题、L7a语义模板问题
- **状态**: 半自动(识别自动，内容增强需AI介入)

### 阶段3: INCREMENT (版本递增)
- **脚本**: `version_sync_pipeline.py increment_version()`
- **功能**: 自动递增patch版本号 (1.0.0 → 1.0.1)
- **规则**: 
  - 三段式版本号: 递增patch位
  - 两段式版本号: 递增minor位并补0
  - 无版本号: 默认1.0.1
- **文件更新**: 直接修改SKILL.md中的version字段

### 阶段4: VALIDATE (质量门禁)
- **脚本**: `deep_quality_audit.py` (L1-L8全量审计)
- **功能**: 对变更skill执行8层质量检查
- **层级**:
  | 层级 | 名称 | 检查内容 | 默认状态 |
  |------|------|----------|----------|
  | L1 | 静态格式 | frontmatter完整性、必填字段 | 默认启用 |
  | L2 | LLM验证 | 语义合理性、逻辑一致性 | 按需启用 |
  | L3 | Agent试用 | 实际执行验证 | 按需启用 |
  | L4 | 功能质量 | 完整性、准确性、可用性 | 默认启用 |
  | L5 | 可销售性 | 商业价值、差异化、定价合理性 | 默认启用 |
  | L6 | 内容真实性 | 已知限制、依赖说明真实性 | 默认启用 |
  | L7a | 语义模板 | TF-IDF重复块检测、模板化检测 | 默认启用(opt-out) |
  | L7b | 可执行性 | 任务定义清晰度、输入输出规范 | 默认启用(opt-out) |
  | L8 | 安全审计 | API密钥暴露、URL安全、注入检测 | 默认启用(opt-out) |
- **门禁规则**: L1未通过则阻塞同步

### 阶段5: SYNC_GITHUB (GitHub同步)
- **脚本**: `version_sync_pipeline.py sync_to_github()`
- **功能**: git add → git commit → git push
- **仓库**: `https://github.com/thcjp/-.git` (main分支)
- **超时**: 180秒(git push)
- **提交格式**: `feat({slug}): upgrade to v{version} - {changelog}`
- **记录**: platform_uploads表记录同步结果

### 阶段6: SYNC_SKILLHUB (SkillHub同步)
- **脚本**: `version_sync_pipeline.py sync_to_skillhub()`
- **免费版**: 通过`skillhub publish` CLI上传
  - WAF限制: 内容 ≤ 5800字符
  - 超长内容自动阻塞并记录
- **付费版**: 生成payload JSON文件
  - 路径: `enterprise-upload/payloads/{slug}-paid-v{version}.json`
  - 需浏览器session认证手动上传
- **状态**: 免费版自动，付费版半自动

### 阶段7: SYNC_CLAWHUB (ClawHub同步)
- **脚本**: `version_sync_pipeline.py sync_to_clawhub()`
- **功能**: 通过`npx clawhub publish`直接上传
- **限流**: 200个/24小时
- **重试**: 通过checkpoint文件支持断点续传
- **批量上传**: `clawhub_batch_uploader.py --resume --limit 200`

### 阶段8: RECORD (记录)
- **数据库**: SQLite (`d:\skills\skill-registry.db`)
- **表结构**:
  | 表名 | 用途 |
  |------|------|
  | skills | skill主表(slug, version, status, pricing等) |
  | versions | 版本历史(hash, changelog, file_size) |
  | platform_uploads | 平台上传记录(platform, status, error) |
  | operations | 操作日志(operation_type, details) |
- **原则**: 所有操作均记录到operations表，平台同步结果记录到platform_uploads表

## 脚本依赖关系

```
orchestrator.py
  ├── auto_discover.py          (阶段1: 扫描新skill)
  ├── version_sync_pipeline.py   (阶段1-8: 变更检测→同步)
  │   ├── quality_gate.py        (阶段4: L1质量门禁)
  │   └── skill_core/parser.py   (frontmatter解析)
  ├── deep_quality_audit.py      (阶段4: L1-L8全量审计)
  └── clawhub_batch_uploader.py  (阶段7: ClawHub批量上传)
```

## 数据流

```
SKILL.md文件 → SHA-256 hash → 数据库versions表对比
                                    ↓ (hash不匹配)
                              版本递增 + SKILL.md更新
                                    ↓
                              质量门禁检查 (L1-L8)
                                    ↓ (通过)
                    ┌───────────────┼───────────────┐
                    ↓               ↓               ↓
              GitHub push      SkillHub upload   ClawHub upload
                    ↓               ↓               ↓
              platform_uploads表记录(每平台独立)
                    ↓
              operations表记录(操作日志)
```

## 使用方式

### 单个skill同步
```bash
python version_sync_pipeline.py sync <slug>
# 跳过特定平台:
python version_sync_pipeline.py sync <slug> --skip-github --skip-clawhub
```

### 批量同步所有变更
```bash
python version_sync_pipeline.py scan          # 检测变更
python version_sync_pipeline.py sync-all       # 同步所有变更skill
```

### 统一编排
```bash
python orchestrator.py status                 # 状态概览
python orchestrator.py discover               # 仅执行发现阶段
python orchestrator.py enhance                # 仅执行增强阶段
python orchestrator.py audit                  # 仅执行审计阶段
python orchestrator.py sync-all               # 同步所有变更skill
python orchestrator.py sync <slug>            # 同步单个skill
python orchestrator.py full-run               # 完整流程
python orchestrator.py pipeline-report        # 流水线报告
```

### ClawHub批量上传
```bash
python clawhub_batch_uploader.py --resume --limit 200
```

## 已知限制

1. **SkillHub WAF限制**: 内容超过5800字符的skill无法通过CLI上传，需手动通过浏览器提交
2. **SkillHub付费版**: 需浏览器session认证，无法完全自动化
3. **ClawHub限流**: 每日200个新skill上限，大批量上传需多天完成
4. **GitHub网络**: push操作受网络状况影响，已设置180秒超时
5. **L2/L3审计**: 需要LLM API Key，默认不启用
6. **ENHANCE阶段**: B级skill识别自动，但内容增强需AI介入

## 灾难恢复和回滚

### 版本回滚
```bash
# 查看历史版本
sqlite3 skill-registry.db "SELECT version, created_at, changelog FROM versions WHERE skill_id=? ORDER BY created_at DESC"

# Git回滚到上一版本
git revert HEAD~1 --no-edit
git push origin main
```

### 数据库恢复
```bash
# 数据库备份(执行前建议)
cp skill-registry.db skill-registry.db.bak

# 恢复
cp skill-registry.db.bak skill-registry.db
```

### 平台同步失败处理
1. **GitHub失败**: 检查网络和认证，重试`git push origin main`
2. **SkillHub失败**: 检查CLI是否安装(`skillhub --version`)，内容是否超长
3. **ClawHub限流**: 等待24小时后重试，使用`--resume`从断点继续

### Checkpoint恢复
- ClawHub上传checkpoint: `clawhub_upload_checkpoint.json`
- 版本同步报告: `version_sync_{slug}_{timestamp}.json`
- 审计报告: `deep_quality_audit_report.json`

## 后续优化方向

1. SkillHub API直传(绕过CLI和WAF限制)
2. ClawHub限流自适应调度(自动检测限流窗口)
3. L2/L3审计自动化(LLM API集成)
4. 增强阶段AI自动化(基于审计报告自动生成增强建议)
5. 多仓库GitHub同步(支持多个开放库)
6. 同步结果通知(飞书/邮件告警)
