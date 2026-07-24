# 版本同步流水线 (Version Sync Pipeline)

## 概述

版本同步流水线是一个端到端自动化系统，负责将本地Skill的版本变更同步到GitHub开放库、SkillHub（免费+付费）和ClawHub三个平台。系统以SQLite数据库为唯一权威数据源，通过8个阶段完成从变更检测到多平台同步的全流程。

## 架构图

```
┌─────────────────────────────────────────────────────────────┐
│                    orchestrator.py                           │
│                   (统一编排入口)                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ DISCOVER │→│ ENHANCE  │→│ INCREMENT│→│ VALIDATE │    │
│  │ 变更检测  │  │ 内容增强  │  │ 版本递增  │  │ 质量门禁  │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
│       │                                          │           │
│       ▼                                          ▼           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │  GITHUB  │→│ SKILLHUB │→│ CLAWHUB  │→│  RECORD  │    │
│  │ 开放库同步 │  │ 免费+付费 │  │ 免费同步  │  │ 数据记录  │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
         │              │              │
         ▼              ▼              ▼
   ┌──────────┐  ┌──────────┐  ┌──────────┐
   │  GitHub  │  │ SkillHub │  │ ClawHub  │
   │  仓库    │  │ CLI/API  │  │   CLI    │
   └──────────┘  └──────────┘  └──────────┘
         │              │              │
         └──────────────┼──────────────┘
                        ▼
              ┌──────────────────┐
              │  SQLite 数据库    │
              │ skill-registry.db │
              ├──────────────────┤
              │ skills 表        │
              │ versions 表      │
              │ platform_uploads │
              │ operations 表    │
              └──────────────────┘
```

## 8阶段详细说明

### 阶段1: DISCOVER - 变更检测

**脚本**: `auto_discover.py` + `version_sync_pipeline.py scan`

**功能**:
- 扫描本地SKILL.md文件，计算SHA-256哈希
- 对比数据库`versions`表中记录的最后哈希值
- 检测内容变更，输出变更skill列表

**使用方式**:
```bash
python version_sync_pipeline.py scan
```

**输出**: `version_sync_scan_report.json` - 包含所有变更skill的slug、旧/新哈希、当前版本

### 阶段2: ENHANCE - 内容增强

**脚本**: `orchestrator.py enhance`

**功能**:
- 读取`deep_quality_audit_report.json`审计报告
- 识别L5/L6/L7a/L7b各层级B级skill
- 生成增强建议列表

**状态**: 半自动（识别自动，增强内容需AI执行）

### 阶段3: INCREMENT - 版本递增

**脚本**: `version_sync_pipeline.py` 内的 `increment_version()` 函数

**功能**:
- 自动递增patch版本号（如1.0.0 → 1.0.1）
- 更新SKILL.md文件中的version字段
- 重新计算文件哈希

**规则**:
- 三段式版本号（X.Y.Z）：递增Z
- 两段式版本号（X.Y）：递增Y，补Z为0
- 非标准版本号：追加.1

### 阶段4: VALIDATE - 质量门禁

**脚本**: `deep_quality_audit.py`

**功能**:
- L1 静态格式检查（frontmatter合规性）
- L2 LLM语义验证
- L3 Agent试用测试
- L4 功能质量审计
- L5 可销售性评估
- L6 内容真实性验证
- L7a 语义模板审计（TF-IDF重复检测）
- L7b 可执行性审计
- L8 安全审计

**默认状态**: L7a/L7b/L8均默认启用（opt-out模式）

**使用方式**:
```bash
python deep_quality_audit.py                    # 全量审计
python deep_quality_audit.py --no-layer7b       # 跳过L7b
```

### 阶段5: SYNC_GITHUB - GitHub同步

**脚本**: `version_sync_pipeline.py` 内的 `sync_to_github()` 函数

**功能**:
- `git add <SKILL.md路径>`
- `git commit -m "feat(<slug>): upgrade to v<version> - <changelog>"`
- `git push origin main`

**验证**: commit哈希记录到`platform_uploads`表

### 阶段6: SYNC_SKILLHUB - SkillHub同步

**脚本**: `version_sync_pipeline.py` 内的 `sync_to_skillhub()` 函数

**免费版**: 通过`skillhub publish` CLI上传
- WAF限制：内容长度 ≤ 5800字符
- 超长内容自动标记为`blocked_content_too_long`

**付费版**: 生成payload JSON文件
- 输出到 `enterprise-upload/payloads/<slug>-paid-v<version>.json`
- 包含定价信息（按次计费，9.90 CNY/次）
- 实际上传需浏览器session认证

### 阶段7: SYNC_CLAWHUB - ClawHub同步

**脚本**: `version_sync_pipeline.py` 内的 `sync_to_clawhub()` 函数 + `clawhub_batch_uploader.py`

**功能**:
- 通过`npx clawhub publish`上传
- 限流：200个新skill/24小时
- 版本冲突自动递增重试
- 断点续传支持

**批量上传**:
```bash
python clawhub_batch_uploader.py --resume --limit 200
```

### 阶段8: RECORD - 数据记录

**数据库表**:
- `skills`: 更新`current_version`和`updated_at`
- `versions`: 插入新版本记录（版本号、哈希、文件大小、行数、changelog）
- `platform_uploads`: 插入平台上传记录（平台、状态、HTTP状态码、错误信息）
- `operations`: 插入操作日志（操作类型、时间、操作者、详情、结果状态）

## 脚本依赖关系

```
orchestrator.py (统一入口)
  ├── auto_discover.py (发现新skill, API扫描)
  ├── version_sync_pipeline.py (变更检测+版本递增+多平台同步)
  │   ├── skill_core/parser.py (frontmatter解析, 单一来源)
  │   ├── quality_gate.py (L1静态检查)
  │   ├── clawhub_batch_uploader.py (ClawHub批量上传)
  │   └── git (GitHub同步: add/commit/push)
  └── deep_quality_audit.py (L1-L8全量质量审计)
      ├── skill_core/parser.py (frontmatter解析)
      └── sklearn (TF-IDF语义分析)
```

## 数据流

```
SKILL.md文件 → 哈希计算 → DB对比 → 变更检测
                                    ↓
                              版本递增 → 质量门禁
                                    ↓
                    ┌───────────────┼───────────────┐
                    ↓               ↓               ↓
              GitHub push     SkillHub上传    ClawHub上传
                    ↓               ↓               ↓
                    └───────────────┼───────────────┘
                                    ↓
                            SQLite DB记录
                            (versions + platform_uploads + operations)
```

## 使用方式

### 日常运维命令

```bash
# 查看全流程状态
python orchestrator.py status

# 查看流水线完整性报告
python orchestrator.py pipeline-report

# 执行完整流程
python orchestrator.py full-run
```

### 单skill同步

```bash
# 同步单个skill到所有平台
python version_sync_pipeline.py sync <slug>

# 仅同步到GitHub
python version_sync_pipeline.py sync-github <slug>

# 强制同步（即使无变更）
python version_sync_pipeline.py sync <slug> --force

# 跳过特定平台
python version_sync_pipeline.py sync <slug> --skip-clawhub --skip-skillhub
```

### 批量同步

```bash
# 扫描所有变更
python version_sync_pipeline.py scan

# 同步所有变更skill
python version_sync_pipeline.py sync-all

# 生成同步报告
python version_sync_pipeline.py report
```

### ClawHub批量上传

```bash
# 上传200个（每日限流）
python clawhub_batch_uploader.py --resume --limit 200

# 干跑模式（不实际上传）
python clawhub_batch_uploader.py --dry-run
```

## 已知限制

1. **无文件监听**: 使用cron调度而非watchdog实时监听，需手动运行或设置定时任务
2. **内容增强半自动**: B级→A级增强需AI执行，无法全自动
3. **SkillHub付费版**: 上传需浏览器session认证，仅payload自动生成
4. **ClawHub限流**: 200个新skill/24小时，大批量上传需多轮
5. **SkillHub WAF限制**: 内容超过5800字符无法通过CLI上传

## 灾难恢复和回滚

### 版本回滚

```bash
# 查看历史版本
sqlite3 d:\skills\skill-registry.db "SELECT version, created_at, changelog FROM versions WHERE skill_id = (SELECT id FROM skills WHERE slug = '<slug>') ORDER BY created_at DESC"

# Git回滚到指定commit
cd d:\skills
git log --oneline --grep="<slug>"
git revert <commit_hash>
```

### 平台同步失败处理

1. **GitHub push失败**: 检查网络和权限，重新运行`sync-github <slug>`
2. **SkillHub上传失败**: 检查内容长度，缩短SKILL.md或使用浏览器手动上传
3. **ClawHub限流**: 等待24小时后运行`clawhub_batch_uploader.py --resume`
4. **ClawHub版本冲突**: 自动递增版本号重试，或手动修改版本号

### 数据库备份

```bash
# 备份数据库
copy d:\skills\skill-registry.db d:\skills\skill-registry.db.bak

# 恢复数据库
copy d:\skills\skill-registry.db.bak d:\skills\skill-registry.db
```

## 后续优化方向

1. **文件监听**: 集成watchdog实现SKILL.md变更实时检测
2. **SkillHub API**: 研究API方式替代CLI上传，突破WAF限制
3. **并行上传**: 多平台并行同步，减少总同步时间
4. **增量审计**: 仅审计变更的skill而非全量审计
5. **自动回滚**: 同步失败时自动回滚版本号和文件变更
