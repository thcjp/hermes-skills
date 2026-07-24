# 第43轮提示词 (v43.0)

> **日期**: 2026-07-24
> **上一轮完成**: V42全部7项任务完成 + 4项Phase 1-2回归修复 + 三轨模型数据质量修复
> **Git 提交**: e87e9132 (6 files, +220/-7273)
> **V41状态**: 已废弃（Phase 1-7全部集成到V42并完成）

## 上一轮完成情况

### V42 任务1: GitHub 推送重试 ✅
- `git push origin main` 首次成功 (cadc4889..11564336)
- 后续推送 (含e87e9132) 因 github.com 网络超时失败
- `git push hermes-skills main` 持续失败 (port 443 连接超时)

### V42 任务2: ClawHub 定时上传监控 ✅
- 定时任务(ID: 5f5e0baf)路径已从 `skill-registry/` 更新为 `tools/` + `data/`（Phase 2回归修复）
- 已发布: 855，剩余: 502
- 下次运行: 2026-07-25 12:00 (北京时间)
- 预计3天内完成全部上传

### V42 任务3: SkillHub 待审 skill 处理 ✅
- 清理14条重复记录 (16→8 retry_pending)
- 取消1个 blocked_by_quality_gate (ai-video-director, skill已not_found)
- 8个有效 retry_pending skills（SKILL.md均存在，状态=updated）
- 1个 failed (chat, skillhub CLI不可用)
- 1个 payload_ready (chat, skillhub_paid, 需浏览器手动上传)

### V42 任务4: 看板服务更新验证 ✅
- `dashboard_server.py` 正常启动 (http://localhost:8765)
- API `/api/stats` 返回正确的三轨模型数据
- 三轨分布: free=1675, source=600, paid=599, tool=8
- 平台状态、分类、定价分层均正确显示

### V42 任务5: daily_sync.py 集成测试 ✅
- `python tools/daily_sync.py --report` 正常运行
- 报告已生成: `data/health_reports/daily_sync_20260724.json`
- 报告数据与数据库一致

### V42 任务6: 源 skill 多源发现与增强 ✅
- **修复Phase 1回归**: GITHUB_REPOS错误统一为Git远程配置，拆分为:
  - `GITHUB_REPOS` (Git推送: hermes-skills + origin)
  - `GITHUB_SCAN_REPOS` (发现扫描: anthropics/skills, obra/superpowers, addyosmani/agent-skills, ComposioHQ/awesome-claude-skills, VoltAgent/awesome-openclaw-skills)
- **修复Phase 1回归**: `auto_discover.py` DISCOVERY_DIR 使用旧路径 `SKILLS_ROOT/tools/discovery`，改为从config导入 `DATA_DIR/discovery`
- **修复Phase 1回归**: `multi_source_discover.py` 缺少 `DATA_DIR` 导入
- 多源发现运行结果:
  - GitHub扫描: 111个候选 (5个配置仓库 + 关键词搜索50个仓库)
  - AwesomeList: 76个候选 (e2b-dev/awesome-ai-agents + Shubhamsaboo/awesome-llm-apps)
  - Hermes: 0个新发现 (759个已全部入库)
  - N8N: 0个 (API未返回数据，需调查)
  - Dify: 0个 (API未返回数据，需调查)
  - Coze: 0个 (API返回0个bot)
- 统一候选列表: `data/discovery/candidates_unified.json` (119个候选)
- sources表累计: hermes=469, github-search=111, awesome-list=76

### V42 任务7: 三轨模型完整性检查 ✅
- 发现并修复6类数据质量问题 (共1289条记录):
  1. source类型 is_paid=1 → 0 (修复600条)
  2. paid类型 is_paid!=1 → 1 (修复238条)
  3. free类型 edition=paid/pro → free (修复117条)
  4. source类型 source_slug!=slug (修复11条)
  5. L1-入门级 + edition=paid/pro → L3-专业级 (修复43条)
  6. L4-企业级 + edition=free → L2-标准级 (修复280条)
- 定价分层重新平衡:
  - 修复前: L1=597, L2=807, L3=967, L4=511
  - 修复后: L1=554, L2=1087, L3=1010, L4=231
- 三轨关联字段: 0个缺失 (source_slug, free_slug, paid_slug)
- 数据库备份: `data/backups/skill-registry.db.pre-v42-fix-20260724130053`

### V42 额外修复
- ClawHub定时任务路径更新 (Phase 2回归: skill-registry/ → tools/ + data/)
- SkillHub重复platform_uploads记录清理 (14条删除)
- 过时platform_uploads记录取消 (ai-video-director not_found)

## 当前项目状态

| 维度 | 数据 |
|------|------|
| 总 Skill 数 | 2882 |
| 三轨分布 | source=600, free=1675, paid=599, tool=8 |
| 定价分层 | L1-入门级=554, L2-标准级=1087, L3-专业级=1010, L4-企业级=231 |
| SkillHub | success=1120, retry_pending=8, cancelled=1, failed=1, payload_ready=1 |
| ClawHub | success=1152, fail=2, retry_pending=1, published=855, remaining=502 |
| GitHub | success=1159 |
| FTS 记录 | 2330 |
| 看板视图 | 3个 (v_skill_lifecycle, v_platform_summary, v_three_track_overview) |
| 多源发现 | hermes=469, github-search=111, awesome-list=76 |
| 数据质量 | 0个NULL (pricing_tier, is_paid, edition, source_slug, free_slug, paid_slug) |

## V41/V42 集成确认

| V41 Phase | V42状态 | Git Commit |
|-----------|---------|------------|
| Phase 1: 统一配置中心 | ✅ 已完成 | 4a7e4e01 |
| Phase 2: 工具/产品物理分离 | ✅ 已完成 | b8beccc4 |
| Phase 3: 数据库清理和增强 | ✅ 已完成 | 2e604e81 |
| Phase 4: 文档统一 | ✅ 已完成 | 2e604e81 |
| Phase 5: 顶层文件清理 | ✅ 已完成 | 2e604e81 |
| Phase 6: 每日同步实现 | ✅ 已完成 | 2e604e81 |
| Phase 7: 全量验证 | ✅ 已完成 | 2e604e81 |

**结论**: V41的全部7个Phase已集成到V42并完成，V41可以废弃。

## 第43轮任务清单

### 任务1: GitHub 推送重试（持续网络问题）
- `git push origin main`（私有备份仓库，含e87e9132提交）
- `git push hermes-skills main`（公开引流仓库）
- 如果网络持续不通，考虑:
  - 检查DNS解析: `nslookup github.com`
  - 使用代理: `git config --global http.proxy http://127.0.0.1:port`
  - 使用SSH协议: `git remote set-url origin git@github.com:thcjp/-.git`

### 任务2: ClawHub 定时上传持续监控
- 检查定时任务(ID: 5f5e0baf)运行结果
- 855已发布 + 每日200 = 预计3天内完成全部1357个
- 检查 `data/clawhub_published_slugs.json` 总数
- 如果总数 >= 1357，通知用户可以删除定时任务

### 任务3: SkillHub retry_pending 处理
- 8个有效retry_pending skills (均已有SKILL.md):
  1. cdp-browser-master (differentiated-skills/Automation/)
  2. cron-guard (differentiated-skills/Automation/)
  3. linear-workflow-bot (differentiated-skills/Automation/)
  4. ai-artist-workstation (packaged-skills/skillhub/)
  5. sales-copy-writer (packaged-skills/skillhub/)
  6. accounting-and-finance (clawhub-skills/downloaded/Finance/)
  7. accounting-finance (differentiated-skills/Finance/)
  8. ace-music (clawhub-skills/downloaded/Creative/)
- 检查skillhub CLI是否可用: `where skillhub` 或 `npm list -g`
- 如果CLI可用，逐个执行: `skillhub publish [path]`
- 如果CLI不可用，通过Trae Work对话命令上传
- 1个failed (chat): skillhub CLI未识别，需安装或使用Trae Work
- 1个payload_ready (chat, paid): 需浏览器手动上传

### 任务4: N8N/Dify/Coze API 调查与修复
- N8N: `https://api.n8n.io/api/templates/workflows` 返回0个候选
  - 调查API是否需要认证或已变更
  - 尝试: `https://api.n8n.io/api/templates/workflows?limit=50&category=ai`
- Dify: `https://cloud.dify.ai/api/explore/apps` 返回0个候选
  - 调查API是否需要认证
  - 尝试爬取HTML页面提取嵌入数据
- Coze: `https://www.coze.cn/api/store/bot/list` 返回0个bot
  - 调查API是否需要认证或已变更
  - 尝试: `https://api.coze.cn/api/store/bot/list?page=1&size=50`

### 任务5: 多源候选下载与入库
- 从 `data/discovery/candidates_unified.json` (119个候选)中选择高质量项目
- 下载GitHub仓库中的SKILL.md或README.md
- 转化为标准SKILL.md格式 (frontmatter + 内容)
- 入库为 skill_type='source'
- 执行差异化增强流程 (→ free版 → paid版)

### 任务6: Free→Paid 增强计划
- 1675个free skill缺少paid版 (正常，非所有free都需要paid)
- 优先为以下类别创建paid版:
  - L3-专业级和L4-企业级的free skill (高价值)
  - Agents类别 (市场需求大)
  - Finance类别 (付费意愿高)
- 13个source skill缺少free版，需创建免费版
- 生成增强计划文档: `docs/enhancement-plan.md`

### 任务7: daily_sync.py 定时任务配置
- 将 `python tools/daily_sync.py --full` 配置为每日定时任务
- 建议时间: 每日 06:00 (ClawHub任务之前)
- 与ClawHub定时任务(12:00)协调
- 验证完整同步流程: 发现→审计→GitHub同步→SkillHub同步→ClawHub同步→报告

### 任务8: FTS 触发器验证
- FTS记录从2121增加到2330 (三轨修复后)
- 验证INSERT/UPDATE/DELETE触发器是否正常工作
- 执行测试: 更新一条skill记录，检查FTS是否同步
- 如果触发器失效，重建FTS并重新创建触发器

## 验证检查清单

- [ ] GitHub origin 推送成功 (含e87e9132)
- [ ] GitHub hermes-skills 推送成功
- [ ] ClawHub 定时任务正常运行 (published >= 1055)
- [ ] SkillHub 8个 retry_pending 已处理
- [ ] N8N/Dify/Coze API 调查完成
- [ ] 新候选 skill 已下载并入库
- [ ] Free→Paid 增强计划已生成
- [ ] daily_sync.py 定时任务已配置
- [ ] FTS 触发器验证通过

## 多源发现系统架构

```
多源头发现系统 (multi_source_discover.py)
├── ClawHub扫描器 (auto_discover.py)
│   └── API: https://clawhub.ai/api + mirror-cn.clawhub.com/api
├── N8N扫描器 ⚠️ API未返回数据
│   └── API: https://api.n8n.io/api/templates/workflows
├── Dify扫描器 ⚠️ API未返回数据
│   └── API: https://cloud.dify.ai/api/explore/apps
├── Coze扫描器 ⚠️ API未返回数据
│   └── API: https://www.coze.cn/api/store/bot/list
├── Hermes扫描器 ✅ 759个已入库
│   └── GitHub: thcjp/hermes-skills
├── AwesomeList扫描器 ✅ 76个候选
│   └── GitHub: e2b-dev/awesome-ai-agents, Shubhamsaboo/awesome-llm-apps
├── GitHub扫描器 ✅ 111个候选
│   ├── 配置仓库: anthropics/skills, obra/superpowers, addyosmani/agent-skills,
│   │            ComposioHQ/awesome-claude-skills, VoltAgent/awesome-openclaw-skills
│   └── 关键词搜索: ai agent, llm tool, ai workflow, claude skill, gpt skill
└── 统一输出: data/discovery/candidates_unified.json
    └── 数据库: sources表 (source_type, source_name, source_url, ...)
```

## Git提交记录

| 轮次 | Commit | 文件数 | 变更行数 | 说明 |
|------|--------|--------|----------|------|
| Round 41 Phase 1 | 4a7e4e01 | - | - | 统一配置中心 |
| Round 41 Phase 2 | b8beccc4 | - | - | 工具/产品物理分离 |
| Round 41 Phase 3-7 | 2e604e81 | 94 | +5410/-1960 | 数据库增强+文档统一+每日同步+全量验证 |
| Round 41 | cdae7300 | - | - | 凭证安全修复 |
| Round 41 | 11564336 | 1 | +192 | V42.0提示词 |
| Round 42 | e87e9132 | 6 | +220/-7273 | GITHUB_SCAN_REPOS拆分+DATA_DIR修复+三轨数据质量 |
