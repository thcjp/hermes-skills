# 新对话启动包 — 详细设计文档 (v2.0)

> **日期**: 2026-07-26
> **版本**: v2.0 (方案C: 流程+质量门禁架构)
> **目的**: 为开启新对话提供完整的项目上下文、架构现状、质量门禁系统、自动化生命周期、差距分析和待办任务
> **生成依据**: V54-V64全部对话记忆 + round1-7-comprehensive-review-v2.md + 代码级探索 + 9项新增需求分析

---

## 一、项目概览

### 1.1 项目定位

Skill 收集-增强-分发平台。从 ClawHub、GitHub、开源社区收集优秀 Skill，二次包装增强后分为免费版/付费版，上传到 SkillHub、ClawHub、GitHub 三大平台。

### 1.2 核心数据 (截至V64)

| 指标 | 值 |
|------|-----|
| 本地数据库skill总数 | 3463 |
| SkillHub平台published | 2172 |
| 四平台同步状态 | 全部unknown归零 |
| Stars | 2172/2172 (100%) |
| 内容质量通过率 | 99.4% (2801/2818) |
| 三轨关联 | free_slug=2861, paid_slug=2305 |
| 企业认证 | 四川云物益邦科技有限公司 (Verified) |
| Git提交 | 4d68b6dbe (V64) + 5a8dfcb41 (V65提示词) |

### 1.3 项目目录结构

```
d:\skills\
├── config/                              # 统一配置中心
│   ├── project_config.py                # 路径/常量/阈值
│   ├── platform_config.py               # 平台URL/API/限流/GitHub双仓库
│   └── github_repo_strategy.py          # GitHub仓库策略(shim)
├── tools/                               # 工具脚本(60+)
│   ├── db.py                            # 数据库模块(10张表)
│   ├── enterprise_uploader.py           # SkillHub企业版上传
│   ├── version_sync_pipeline.py         # 版本同步流水线(含upgrade命令)
│   ├── orchestrator.py                  # 统一编排入口(8阶段)
│   ├── clawhub_batch_uploader.py        # ClawHub批量上传
│   ├── quality_gate.py                  # L1静态质量门禁(13项)
│   ├── llm_validator.py                 # L2 LLM验证(TRACE五维度)
│   ├── agent_trial.py                   # L3 Agent试用(100分制)
│   ├── deep_quality_audit.py            # L4-L9深度审计
│   ├── skill_batch_upgrader_v3.py       # 批量升级(v3.2: 内容质量+合规)
│   ├── auto_discover.py                 # 自动发现(多源头)
│   ├── multi_source_discover.py         # 多源发现扩展
│   ├── market_monitor.py                # 市场监控(评分/趋势)
│   ├── upgrade_checker.py              # 升级检测(版本/hash)
│   ├── update_mechanism.py             # 更新机制(L1-L3门禁集成)
│   ├── daily_sync.py                   # 日常同步
│   ├── trace_llm_scorer.py             # TRACE评分核心
│   ├── skill_core/                      # 核心模块(parser/checks/rules)
│   └── ...
├── data/                                # 数据存储
│   ├── upload_tracking.json             # 上传追踪(5.8MB, schema v4.0)
│   ├── category_mapping.json            # 分类映射
│   ├── reports/                         # 审计报告
│   └── health_reports/                  # 健康检查
├── docs/                                # 项目文档
│   ├── ARCHITECTURE.md                  # 唯一架构文档
│   ├── plans/                           # 计划文档
│   └── specs/                           # 设计文档
├── packaged-skills/skillhub/            # 免费版skill(SkillHub)
├── enterprise-upload/                   # 付费版skill
├── clawhub-skills/downloaded/           # 源skill(ClawHub下载)
├── opensource-skills/packaged/          # 开源版skill
├── differentiated-skills/               # 差异化日志
├── skill-registry.db                    # 唯一SQLite数据库
└── .credentials/                        # 平台认证凭证
```

---

## 二、三轨模型（源/免费/付费）

### 2.1 三轨定义

| 轨道 | skill_type | 目录 | 说明 |
|------|-----------|------|------|
| 源 | source | `clawhub-skills/downloaded/` | 从ClawHub/GitHub下载的原始skill |
| 免费版 | free | `packaged-skills/skillhub/` | 增强后的免费版，MIT许可证 |
| 付费版 | paid | `enterprise-upload/` | 增强后的付费版，Proprietary许可证 |

### 2.2 数据库三轨关联

```
skills表字段:
  - slug (UNIQUE)           — skill唯一标识
  - source_slug             — 源skill的slug
  - edition                 — free/pro/paid
  - skill_type              — free/paid/source
  - is_paid                 — 0=免费, 1=付费
  - parent_slug             — 父skill的slug
  - pricing_tier            — L1-入门级/L2-标准级/L3-专业级/L4-企业级
  - free_slug               — 免费版slug (V62已创建并回填: 2861)
  - paid_slug               — 付费版slug (V62已创建并回填: 2305)
```

### 2.3 三轨在四平台的分布

| 平台 | 源skill | 免费版 | 付费版 |
|------|---------|--------|--------|
| 本地DB | sources表 | skills表(free) | skills表(pro/paid) |
| SkillHub | 不上传 | CLI上传 | API/浏览器上传 |
| ClawHub | 不上传 | 批量上传 | 10%引流 |
| GitHub hermes-skills | 不上传 | git push | git push(与clawhub一致) |
| GitHub origin(私有) | 不上传 | git push | git push |

---

## 三、四平台同步机制现状 (V63已完成)

### 3.1 四平台架构

```
                    ┌─────────────────────┐
                    │   skill-registry.db  │ ← 唯一权威数据库
                    │   (SQLite, 10张表)   │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │  platform_uploads表  │ ← 平台上传状态
                    └──┬─────┬─────┬──────┘
                       │     │     │
            ┌──────────┘     │     └──────────┐
            ▼                ▼                ▼
    ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
    │   SkillHub   │ │   ClawHub    │ │   GitHub     │
    │   团队版     │ │  开源生态    │ │  hermes+origin│
    └──────────────┘ └──────────────┘ └──────────────┘
```

### 3.2 四平台同步状态 (V63完成后)

| 平台 | synced | pending | not_applicable | unknown |
|------|--------|---------|----------------|---------|
| SkillHub | 3364 | 0 | 99 | 0 |
| ClawHub | 709 | 1184 | 1570 | 0 |
| GitHub公开 | 3371 | 0 | 92 | 0 |
| GitHub私有 | 2858 | 0 | 605 | 0 |

### 3.3 同步流水线 (version_sync_pipeline.py)

10阶段端到端自动化:

```
1. DETECT      — 扫描本地SKILL.md，对比DB hash检测变更
2. INCREMENT   — 自动递增版本号(patch级)
3. VALIDATE_L1 — L1静态质量门禁(13项检查)
4. VALIDATE_L1.5 — L1.5内容质量门禁(7项检查+修复) [V64新增]
5. SYNC_GITHUB — git push到hermes-skills(公开)+origin(私有)
6. SYNC_SKILLHUB — 上传免费版(CLI) + 生成付费版payload
7. SYNC_CLAWHUB  — 上传到ClawHub(限流200/24h)
8. RECORD      — 记录所有平台同步结果到数据库
9. UPGRADE     — 独立skill升级流程(查找→检测→修复→验证→L1→同步) [V64新增]
10. STATUS     — 四平台同步状态查询
```

### 3.4 数据库表结构

| 表 | 记录数 | 跟踪内容 |
|----|--------|---------|
| skills | 3463 | slug/版本/状态/定价/分类/四平台sync_status |
| versions | 4690 | 版本历史/content_hash/file_size |
| platform_uploads | 3459 | 平台上传状态/HTTP状态/错误 |
| operations | 11470 | 操作日志/前后状态 |
| sources | 4598 | 来源信息/原始slug |
| scores | 4461 | TRACE评分/8维度 |
| pricing | 1916 | 定价策略/价格模型 |
| workflow_states | 14413 | 工作流步骤状态 |
| dependencies | 0 | 依赖关系(空表) |
| skills_fts | 0 | 全文搜索(空表) |

---

## 四、平台认证与配置

### 4.1 SkillHub 团队版

| 配置项 | 值 |
|--------|-----|
| ORG_ID | 862 |
| API_BASE | https://api.skillhub.cn/api/v1 |
| WAF限制 | 5800字符 |
| 认证 | 企业团队Cookie (skh_ent_token) |
| 企业认证 | 已认证("四川云物益邦科技有限公司") |
| Star API | POST /api/v1/skills/{slug}/star |
| 审核工作流 | pending → admin_review → approved(published) |
| 非破坏性更新 | 不可用(categoryIds/tags/summary_zh修改只能DELETE+重传) |

### 4.2 ClawHub

| 配置项 | 值 |
|--------|-----|
| API_URL | https://clawhub.ai/api |
| 每日限制 | 200/24h |

### 4.3 GitHub 双仓库

| 仓库 | Remote | 可见性 | 推送内容 |
|------|--------|--------|---------|
| 公开引流 | hermes-skills | public | 免费+付费skill |
| 私有备份 | origin | private | 全部skill+项目代码 |

### 4.4 团队分类ID映射

| 平台分类键 | 中文名 | 数字ID |
|------------|--------|--------|
| office-efficiency | 通用办公 | 11039 |
| content-creation | 内容创作 | 11040 |
| dev-programming | 研发工具 | 11041 |
| data-analysis | 数据分析 | 11042 |
| design-media | 需求设计 | 11043 |
| ai-agent | 信息检索 | 11044 |
| knowledge-management | 项目管理 | 11045 |
| business-ops | 数据分析 | 11046 |
| education | 安全合规 | 11047 |
| professional | 其他 | 11048 |

---

## 五、已完成的里程碑 (V54-V64)

| 轮次 | 主要任务 | 结果 |
|------|---------|------|
| V54 | SkillHub重新发布(企业认证) | 830个MIT skill批量上传 |
| V55-V57 | 可见性修复+分类+元数据 | categoryIds/visibility:public/tags修复 |
| V58-V59 | 批量重传+审核自动化 | 1920/1920重传完成(100%) |
| V60 | admin_review批量审核 | 334个审核通过(0失败) |
| V61 | rejected处理+DisplayName中文化 | 43个rejected处理+438个中文化(100%) |
| V62 | 四平台同步机制+三轨关联字段 | sync_status字段+free_slug/paid_slug回填 |
| V63 | 四平台unknown归零+Star+Verified | unknown全部归零+2172 star+企业认证 |
| V64 | 内容质量全面升级+独立升级流程 | 11%→99.4%通过率+upgrade命令+L1.5门禁 |

---

## 六、质量门禁系统架构 (v2.0新增)

### 6.1 质量门禁全景图

```
┌─────────────────────────────────────────────────────────────────┐
│                     质量门禁系统 (7层)                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  L1 静态格式合规 ─── quality_gate.py (13项)                     │
│  ├── 去标识化 / slug一致性 / kebab-case                        │
│  ├── 行数≤500 / frontmatter 8字段 / displayName≤20             │
│  ├── summary≤100 / description 150-280c / version x.y.z        │
│  ├── tools YAML数组 / 无XML尖括号 / 无占位符 / 无夸大词         │
│  ↓                                                              │
│  L1.5 内容质量 ──── skill_batch_upgrader_v3.py (7项检查+修复)  │
│  ├── summary去重 / description去重                              │
│  ├── 无模板套话 / 无占位符 / body无重复句子                     │
│  ├── 章节无错误合并 / 输入格式表非空                            │
│  ↓                                                              │
│  L2 LLM验证 ─────── llm_validator.py (TRACE五维度)             │
│  ├── T(Trust) / R(Reliability) / A(Adaptability)              │
│  ├── C(Convention) / E(Effectiveness)                          │
│  └── 总分≥35/50 通过, 输出A/B/C/D等级                          │
│  ↓                                                              │
│  L3 Agent试用 ───── agent_trial.py (100分制)                   │
│  ├── 典型输入40分 + 异常输入30分 + 可用性30分                  │
│  └── ≥70分通过, 输出A/B/C/D等级                                │
│  ↓                                                              │
│  L4-L9 深度审计 ── deep_quality_audit.py (6层评分)             │
│  ├── L4 功能质量(100): 内容深度+指令性+代码示例+任务定义+错误  │
│  ├── L5 可销售性(100): 内容深度+功能完整+技术深度+UX+专业性    │
│  ├── L6 内容真实性: 模板填充/空段落/截断/占位检测              │
│  ├── L7a 语义质量: 嵌入模型语义块相似度(去重/矛盾)            │
│  ├── L7b 可执行性: LLM模拟执行评估                             │
│  ├── L8 安全审计: 营销注入/API密钥/slug不匹配/标签不匹配等    │
│  └── L9 可见性: 分类/摘要/价值命题/快速开始/标签               │
│  ↓                                                              │
│  营销关卡 ────────── (新增, 需实现)                             │
│  ├── displayName 中文化且≤20字符                               │
│  ├── summary 营销优化且≤100字符                                │
│  ├── description 150-280字符, 非模板化                          │
│  ├── tags 5-10个, 与功能匹配                                   │
│  ├── categoryIds 正确映射                                       │
│  ├── pricing 合理(pricing_tier匹配skill复杂度)                │
│  └── license 合规(free=MIT, paid=Proprietary)                  │
│  ↓                                                              │
│  防幻觉机制 ─────── (新增, 需实现)                             │
│  ├── 交叉验证: L2 TRACE评分 vs L3 Agent试用 vs L4-L9审计       │
│  ├── 需求理解偏差检测: 实际内容 vs description声明              │
│  └── 虚假实现检测: 无占位符/无模板/无空函数体                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 各层职责与实现状态

| 层级 | 模块 | 检查项数 | 评分机制 | 自动修复 | 状态 |
|------|------|---------|---------|---------|------|
| L1 | quality_gate.py | 13 | pass/fail | 无 | 完整 |
| L1.5 | skill_batch_upgrader_v3.py | 7 | pass/fail | 7项修复函数 | 完整(V64) |
| L2 | llm_validator.py | 4 | TRACE 0-50 | 无 | 完整(需AI执行) |
| L3 | agent_trial.py | 3 | 0-100分 | 无 | 完整(需AI执行) |
| L4 | deep_quality_audit.py | 5 | 0-100分 A/B/C/D/F | --fix | 完整 |
| L5 | deep_quality_audit.py | 5 | 0-100分 A/B/C/D | --fix | 完整 |
| L6 | deep_quality_audit.py | 4 | 检测列表 | --fix | 完整 |
| L7a | deep_quality_audit.py | 语义 | 相似度分 | 无 | 完整 |
| L7b | deep_quality_audit.py | LLM | 评估分 | 无 | 完整(需AI) |
| L8 | deep_quality_audit.py | 8类 | 检测列表 | 无 | 完整 |
| L9 | deep_quality_audit.py | 5 | 检测列表 | --fix | 完整 |
| 营销关卡 | (新增) | 7 | pass/fail | (需实现) | 缺失 |
| 防幻觉 | (新增) | 3 | 交叉验证 | (需实现) | 缺失 |

### 6.3 质量门禁集成点

```
上传流水线:
  version_sync_pipeline.sync_skill_to_all_platforms()
    → L1: run_quality_check()
    → L1.5: run_content_quality_gate() [V64]
    → (L2/L3: 需update_mechanism集成,当前version_sync_pipeline未集成L2/L3)
    → GitHub + SkillHub + ClawHub 同步

独立升级:
  version_sync_pipeline.upgrade_single_skill()
    → L1.5: run_content_quality_check() + auto_fix_content()
    → L1: run_quality_check()
    → (L2/L3: 未集成)
    → 多平台同步

更新机制:
  update_mechanism.sync_skill_to_platform()
    → L1: quality_gate.run_quality_gate()
    → L2: 检查l2_final_report是否存在且TRACE≥35
    → L3: 检查l3_final_report是否存在且评分≥70
    → 三层全过才上传
```

### 6.4 质量门禁缺陷分析

| 缺陷 | 严重度 | 现状 | 修复方向 |
|------|--------|------|---------|
| version_sync_pipeline未集成L2/L3 | P0 | 仅L1+L1.5 | 集成L2/L3检查或调用update_mechanism |
| L2/L3依赖人工AI执行prompt | P0 | 非自动化 | 集成LLM API自动执行 |
| 营销关卡缺失 | P1 | 无统一前置检查 | 新增marketing_gate函数 |
| 防幻觉机制缺失 | P1 | 无交叉验证 | 新增cross_validation函数 |
| upgrade_checker用JSON非SQLite | P2 | 数据源割裂 | 迁移到SQLite |
| orchestrator.py有SKILL_DATA_DIR bug | P3 | 配置导入不完整 | 修复import |

---

## 七、自动化生命周期 (v2.0新增)

### 7.1 完整生命周期架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Skill 自动化生命周期                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐         │
│  │  发现    │──→│  增强    │──→│ 质量门禁 │──→│  上传    │         │
│  │ Discover │   │ Enhance  │   │ Gate     │   │ Upload   │         │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬────┘         │
│       │              │              │              │                │
│  auto_discover  batch_upgrader  L1-L9+营销    enterprise_uploader  │
│  multi_source   generate_skill  +防幻觉       clawhub_uploader     │
│  market_monitor                防幻觉        git push               │
│       │              │              │              │                │
│       ▼              ▼              ▼              ▼                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐         │
│  │  审核    │──→│  发布    │──→│  收藏    │──→│  反馈    │         │
│  │ Review   │   │ Publish  │   │ Star     │   │ Feedback │         │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬────┘         │
│       │              │              │              │                │
│  batch_approve  auto_publish   Star API     market_monitor         │
│  handle_rejected               (V63已实现)   获取rating/reviewCount │
│       │              │              │              │                │
│       └──────────────┴──────────────┴──────────────┘                │
│                              │                                      │
│                              ▼                                      │
│                    ┌────────────────┐                                │
│                    │  升级触发      │                                │
│                    │ Upgrade Trigger│                                │
│                    └───────┬────────┘                                │
│                            │                                       │
│                    ┌───────┴────────┐                              │
│                    │a. 源版本变更    │                              │
│                    │   upgrade_check │                              │
│                    │   er.py         │                              │
│                    ├────────────────┤                              │
│                    │b. 平台低评分    │                              │
│                    │   rating<4.0    │                              │
│                    │   (需实现)      │                              │
│                    └───────┬────────┘                              │
│                            │                                       │
│                            ▼                                       │
│                    upgrade_single_skill()                           │
│                    (查找→检测→修复→验证→L1→同步)                   │
│                            │                                       │
│                            ▼                                       │
│                    回到"增强"阶段                                  │
│                    (闭环)                                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 7.2 各阶段实现状态

| 阶段 | 模块 | 自动化程度 | 缺口 |
|------|------|-----------|------|
| 发现 | auto_discover.py / multi_source_discover.py / market_monitor.py | 全自动 | 无 |
| 增强 | skill_batch_upgrader_v3.py / generate_skill.py | 半自动 | 内容增强需AI执行 |
| 质量门禁 | L1+L1.5自动 / L2-L9需AI | 半自动 | L2/L3需人工AI |
| 上传 | enterprise_uploader.py / clawhub_batch_uploader.py / git | 全自动 | 无 |
| 审核 | batch_approve / handle_rejected | 全自动 | 需循环执行 |
| 发布 | auto_publish.py | 全自动 | 无 |
| 收藏 | Star API (V63实现) | 全自动 | 无 |
| 反馈 | market_monitor.py获取rating | 半自动 | 评分未写入DB触发升级 |
| 升级触发a | upgrade_checker.py版本/hash对比 | 全自动 | 用JSON非SQLite |
| 升级触发b | 平台低评分触发 | 缺失 | 需实现 |

### 7.3 升级触发机制设计 (需求8)

**触发事件A: 源版本变更**
```
upgrade_checker.py
  → 扫描源skill目录 (clawhub-skills/downloaded/)
  → 对比 content_hash + version
  → 标记 needs_upgrade
  → 触发 upgrade_single_skill()
```

**触发事件B: 平台低评分** (需实现)
```
market_monitor.py
  → 定期扫描SkillHub平台评分
  → 获取每个skill的 avgRating / reviewCount
  → 写入DB: skills表新增 platform_rating / platform_rating_count 字段
  → 如果 avgRating < 4.0 (阈值可配置)
  → 触发 upgrade_single_skill()
```

**升级流程** (已实现: upgrade_single_skill)
```
1. 查找SKILL.md (find_skill_md, 搜索4个目录)
2. 内容质量检测 (7项检查)
3. 自动修复 (7项内容修复 + 合规修复)
4. 验证修复 (重新检测)
5. L1合规检查 (13项格式检查)
6. 多平台同步 (GitHub + SkillHub + ClawHub)
7. 记录升级结果到DB
```

### 7.4 多平台状态同步 (需求7)

**当前状态**:
- 四平台sync_status已建立(V63), unknown全部归零
- market_monitor.py能获取SkillHub的avgRating/reviewCount
- 平台AI评价/用户评价**未同步回本地DB**

**需要实现的同步闭环**:
```
定时任务 (cron / daily_sync.py)
  → SkillHub: GET /api/v1/skills/{slug} 获取 rating, reviewCount, downloads
  → ClawHub: API获取评分和下载数
  → GitHub: API获取 star数, fork数
  → 写入DB: skills表新增字段
    - platform_rating (平台平均评分)
    - platform_rating_count (评分数)
    - platform_downloads (下载数)
    - platform_ai_review (平台AI测评结果, JSON)
  → 如果 platform_rating < 阈值 → 触发升级
```

---

## 八、差距分析矩阵 (v2.0新增)

### 8.1 需求vs代码差距矩阵

| # | 需求 | 现有代码 | 缺口 | 修复方案 | 影响文件 | 优先级 |
|---|------|---------|------|---------|---------|--------|
| 1 | 真正有效的质量检测 | L1(13项)+L1.5(7项)自动; L2-L9完整但需AI执行 | L2/L3未自动化; version_sync_pipeline未集成L2/L3 | 集成L2/L3到version_sync_pipeline; L2/L3结果文件检查 | version_sync_pipeline.py, update_mechanism.py | P0 |
| 2 | 平台经验固化 | Star API已实现; 审核脚本已就绪; auto_publish已实现 | star/download/审核/发布操作散落在多个脚本 | 统一到platform_ops.py; 固化为pipeline前置步骤 | platform_ops.py, orchestrator.py | P1 |
| 3 | 营销数据质量关卡 | L1有夸大词检查; L5有可销售性; L8有营销注入检测 | tags/category/name/pricing未作为统一上传前置关卡 | 新增marketing_gate函数到quality_gate.py | quality_gate.py, version_sync_pipeline.py | P1 |
| 4 | AI自动化防幻觉 | 无 | 无交叉验证; 无需求理解偏差检测; 无虚假实现检测 | 新增cross_validate函数; 对比description vs body; 检测空函数体 | 新增anti_hallucination.py或集成到quality_gate | P0 |
| 5 | 自动化流水线 | orchestrator.py(8阶段); auto_discover(多源); daily_sync | L2/L3需人工; 无持续监控; 无自动升级触发b | 集成L2/L3自动化; 实现定时升级触发; 完善daily_sync | orchestrator.py, daily_sync.py, market_monitor.py | P2 |
| 6 | 反碎片化 | 多个独立工具(60+) | upgrade_checker用JSON vs orchestrator用SQLite; config导入有bug; 重复实现find_skill_md | 统一数据源到SQLite; 修复config导入; 合并重复函数 | upgrade_checker.py, orchestrator.py, config/ | P3 |
| 7 | 多平台状态同步 | 四平台sync_status已建立; market_monitor获取rating | 平台AI评价未写入DB; 用户评论未获取; 无定时同步 | DB新增platform_rating字段; 定时同步任务; market_monitor增强 | db.py, market_monitor.py, daily_sync.py | P2 |
| 8 | 升级触发机制 | upgrade_checker检测版本/hash变更(触发a) | 无平台低评分触发(触发b); 无持续监控循环 | 实现rating监控; DB新增评分字段; 升级触发b逻辑 | market_monitor.py, db.py, upgrade_checker.py | P2 |
| 9 | 全业务流程体系化 | ARCHITECTURE.md+starter-design.md(v1.0) | 无完整业务流程文档; 无代码vs需求差距分析 | 本文档(v2.0)即为此交付物; 后续按差距矩阵逐项修复 | 本文档 | P3 |

### 8.2 碎片化/冗余实现清单

| 问题 | 涉及文件 | 修复方向 | 优先级 |
|------|---------|---------|--------|
| find_skill_md重复实现 | version_sync_pipeline.py + skill_batch_upgrader_v3.py | 统一到skill_core/ | P2 |
| 数据源割裂 | upgrade_checker.py(JSON) vs orchestrator.py(SQLite) | upgrade_checker迁移到SQLite | P2 |
| config导入不完整 | orchestrator.py(缺SKILL_DATA_DIR) + upgrade_checker.py(缺DATA_DIR) | 修复import | P3 |
| 质量检查分散 | quality_gate(L1) + batch_upgrader(L1.5) + deep_audit(L4-L9) | 统一入口: orchestrator.audit() | P3 |
| 营销检查分散 | quality_gate(夸大词) + deep_audit(L5/L8/L9) + batch_upgrader(摘要描述) | 新增marketing_gate统一 | P1 |

### 8.3 修复原则 (用户强调)

1. **全链路修复**: 从底层数据(DB schema) → 中间模块(tools/) → 前端UI(如有), 禁止只修当前环节
2. **高质量融合**: 碎片化代码统合必须以更高质量为前提, 禁止简单合并
3. **幂等操作**: 所有修复函数必须可重复执行不产生副作用
4. **向后兼容**: 增强不能破坏现有功能
5. **禁止mock**: 所有操作必须真实执行
6. **增强已有代码**: 不创建碎片化新文件, 功能集成到现有工具脚本

---

## 九、技能/插件使用策略

### 9.1 各环节技能/插件调用映射

| 环节 | 技能/插件 | 用途 |
|------|----------|------|
| 设计/规划 | brainstorming | 探索需求，形成设计方案 |
| 需求验证 | hotl:brainstorming | HOTL合约设计 |
| 代码实现 | superpowers:subagent-driven-development | 并行子代理执行 |
| 测试驱动 | superpowers:tdd / tailtest | TDD循环/测试生成 |
| 系统调试 | superpowers:systematic-debugging | 系统化调试 |
| 代码审查 | coderabbit:code-review / hotl:code-review | AI代码审查 |
| 浏览器自动化 | agent-browser / chrome-devtools | SkillHub/ClawHub操作 |
| 网页内容提取 | defuddle | 研究文档提取 |
| UI设计 | stark:web-design | Dashboard设计(如需) |
| AI产品构建 | runtype:runtype-build-product | AI产品(如需) |
| 工程决策 | staff-engineer-mode | 跨生命周期工程决策 |
| 完成验证 | superpowers:verification-before-completion | 完成前验证 |
| 计划编写 | superpowers:writing-plans / hotl:writing-plans | 实施计划编写 |
| TRAE反馈 | feedback | 提交TRAE反馈 |

### 9.2 典型工作流中的调用顺序

**工作流1: 质量门禁系统建设**
```
brainstorming → writing-plans → subagent-driven-development → tdd → code-review → verification-before-completion
```

**工作流2: 自动化生命周期建设**
```
brainstorming → systematic-debugging(分析现有流程) → writing-plans → subagent-driven-development → verification
```

**工作流3: 独立skill升级**
```
version_sync_pipeline.py upgrade <slug> → (自动: 检测→修复→验证→L1→同步) → verification-before-completion
```

---

## 十、约束条件

### 10.1 硬约束（来自project_memory.md）

1. Skill名称/简介/触发词必须移除开源项目和原项目烙印引用
2. 所有Skill必须有三层介绍: displayName(≤20字符)、summary(≤100字符)、SKILL.md主内容
3. SKILL.md必须包含`## 依赖说明` section
4. Frontmatter必须含: slug(全局唯一kebab-case)、displayName、version、summary、license、description、tools
5. homepage字段不得指向原开源仓库
6. SKILL.md中无源仓库引用
7. 内部参考文件(如catalog.md)不上传到SkillHub
8. Slug冲突通过修改名称解决
9. SkillHub有SkillPay变现机制(企业认证+微信商户)
10. 个人用户不可用Proprietary license
11. 公开引流git仓库: https://github.com/thcjp/hermes-skills
12. 必须建立私有仓库备份

### 10.2 执行约束

13. 增强已有代码，不创建碎片化新文件
14. 不模拟/mock/fallback/todo/pass
15. 幂等操作，可重复执行无副作用
16. 向后兼容，不破坏enterprise_uploader.py现有功能
17. 所有API操作使用企业团队账号Cookie
18. 所有上传必须包含categoryIds数字ID数组和visibility:public
19. 断点续传支持
20. 内容保真，DisplayName翻译不改语义
21. 分类统一: 本地分类=skillhub分类=clawhub分类
22. 审核工作流: admin_review状态才能approve
23. 非破坏性更新不可用: categoryIds/tags/summary_zh修改只能DELETE+重传
24. 搜索路径完整: find_skill_md搜索四个目录

### 10.3 技术约束

25. 所有数据库连接必须 PRAGMA foreign_keys = ON
26. 使用db.py业务函数，禁止裸SQL
27. 每个修改后立即py_compile验证
28. 仅使用SkillHub团队号(不用个人号)
29. ClawHub只有一个号
30. SkillHub WAF限制5800字符
31. ClawHub限流200/24h
32. Star API每用户限一次

### 10.4 质量约束 (v2.0新增)

33. **全链路修复**: 从DB→模块→UI, 禁止只修当前环节
34. **高质量融合**: 碎片化统合必须以更高质量为前提
35. **L1.5门禁**: 内容质量检查必须在L1合规后、L2前执行
36. **营销关卡**: 上传前必须通过营销数据检查
37. **防幻觉**: 关键环节必须交叉验证
38. **升级优先**: 尽量升级版本而非DELETE+重传(除非营销展示需要)

---

## 十一、关键文件索引

| 类别 | 文件路径 |
|------|---------|
| 数据库定义 | `d:\skills\tools\db.py` |
| 配置中心 | `d:\skills\config\project_config.py` |
| 平台配置 | `d:\skills\config\platform_config.py` |
| 版本同步流水线 | `d:\skills\tools\version_sync_pipeline.py` |
| SkillHub企业上传 | `d:\skills\tools\enterprise_uploader.py` |
| ClawHub批量上传 | `d:\skills\tools\clawhub_batch_uploader.py` |
| 统一编排 | `d:\skills\tools\orchestrator.py` |
| L1质量门禁 | `d:\skills\tools\quality_gate.py` |
| L2 LLM验证 | `d:\skills\tools\llm_validator.py` |
| L3 Agent试用 | `d:\skills\tools\agent_trial.py` |
| L4-L9深度审计 | `d:\skills\tools\deep_quality_audit.py` |
| 批量升级(v3.2) | `d:\skills\tools\skill_batch_upgrader_v3.py` |
| 自动发现 | `d:\skills\tools\auto_discover.py` |
| 多源发现 | `d:\skills\tools\multi_source_discover.py` |
| 市场监控 | `d:\skills\tools\market_monitor.py` |
| 升级检测 | `d:\skills\tools\upgrade_checker.py` |
| 更新机制 | `d:\skills\tools\update_mechanism.py` |
| 日常同步 | `d:\skills\tools\daily_sync.py` |
| TRACE评分 | `d:\skills\tools\trace_llm_scorer.py` |
| 数据库文件 | `d:\skills\skill-registry.db` |
| JSON数据源 | `d:\skills\data\upload_tracking.json` |
| 内容质量报告 | `d:\skills\data\reports\content_quality_report.json` |
| 架构设计文档 | `d:\skills\docs\specs\2026-07-24-architecture-governance-design.md` |
| 综合评审报告 | `d:\skills\.trae\documents\round1-7-comprehensive-review-v2.md` |
| 架构文档 | `d:\skills\docs\ARCHITECTURE.md` |
