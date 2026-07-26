# 新对话启动包 — 详细设计文档

> **日期**: 2026-07-26
> **版本**: v1.0
> **目的**: 为开启新对话提供完整的项目上下文、架构现状、四平台同步分析、待办任务和执行策略
> **生成依据**: 回顾v54.0-v61.0全部对话记忆 + round1-7-comprehensive-review-v2.md + 架构治理设计文档 + 代码级探索

---

## 一、项目概览

### 1.1 项目定位

Skill 收集-增强-分发平台。从 ClawHub、GitHub、开源社区收集优秀 Skill，二次包装增强后分为免费版/付费版，上传到 SkillHub、ClawHub、GitHub 三大平台。

### 1.2 核心数据

| 指标 | 值 |
|------|-----|
| 本地数据库skill总数 | 3463 |
| SkillHub平台skill总数 | 2182 |
| approved | 1889 |
| pending | 267 |
| admin_review | 2 |
| rejected | 4 |
| platform_review | 20 |
| 批量重传完成率 | 1920/1920 (100%) |
| DisplayName中文化 | 438/438 (100%) |
| Round 1-7任务完成率 | 28/30 (93.3%) |

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
│   ├── version_sync_pipeline.py         # 8阶段版本同步流水线
│   ├── orchestrator.py                  # 统一编排入口
│   ├── clawhub_batch_uploader.py        # ClawHub批量上传
│   ├── deep_quality_audit.py            # L4-L8深度审计
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
  - source_slug             — 源skill的slug (65%已填充)
  - edition                 — free/pro/paid
  - skill_type              — free/paid/source
  - is_paid                 — 0=免费, 1=付费, NULL=未设置(581个)
  - parent_slug             — 父skill的slug(部分实现)
  - pricing_tier            — L1-入门级/L2-标准级/L3-专业级/L4-企业级
```

### 2.3 三轨关联缺陷

| 缺陷 | 严重度 | 现状 |
|------|--------|------|
| `free_slug`字段未创建 | P1 | 设计文档提出但未实施 |
| `paid_slug`字段未创建 | P1 | 设计文档提出但未实施 |
| `parent_slug`关联不完整 | P1 | 部分填充 |
| `is_paid`有581个NULL | P2 | 未设置付费标志 |
| `skill_type`语义混乱 | P2 | NULL=584, tool=8, 多种旧值共存 |
| `v_skill_lifecycle`视图未创建 | P2 | 设计文档提出但未实施 |

### 2.4 三轨在四平台的分布

| 平台 | 源skill | 免费版 | 付费版 |
|------|---------|--------|--------|
| 本地DB | sources表(4598条) | skills表(free=3308) | skills表(pro=123,paid=31) |
| SkillHub | 不上传 | ✅ CLI上传 | ✅ API/浏览器上传 |
| ClawHub | 不上传 | ✅ 批量上传 | ✅ 10%引流(173条) |
| GitHub hermes-skills | 不上传 | ✅ git push | ✅ git push(与clawhub一致) |
| GitHub origin(私有) | 不上传 | ✅ git push | ✅ git push |

---

## 三、四平台同步机制现状分析

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

    ┌──────────────────────────────────────────────────┐
    │          upload_tracking.json (5.8MB)            │ ← 独立数据源
    │  skillhub / clawhub / hermes / coze 对象         │
    └──────────────────────────────────────────────────┘
```

### 3.2 各平台跟踪详情

#### 3.2.1 本地数据库 (skill-registry.db)

| 表 | 记录数 | 跟踪内容 |
|----|--------|---------|
| skills | 3463 | slug/版本/状态/定价/分类 |
| versions | 4690 | 版本历史/content_hash/file_size |
| platform_uploads | 3459 | 平台上传状态/HTTP状态/错误 |
| operations | 11470 | 操作日志/前后状态 |
| sources | 4598 | 来源信息/原始slug |
| scores | 4461(有效) | TRACE评分/8维度 |
| pricing | 1916 | 定价策略/价格模型 |
| workflow_states | 14413 | 工作流步骤状态 |
| dependencies | 0 | 依赖关系(空表) |
| skills_fts | 0 | 全文搜索(空表) |

**platform_uploads表平台分布**:

| platform值 | 记录数 | 成功数 | 问题 |
|------------|--------|--------|------|
| github | 1159 | 1159 | 未区分hermes-skills(公开)和origin(私有) |
| clawhub | 1155 | 1153 | 正常 |
| skillhub | 1129 | 1128 | 正常 |
| skillhub_free | 1 | 0 | 仅1条(version_sync_pipeline产生) |
| skillhub_paid | 1 | 0 | 仅1条(payload_ready状态) |

#### 3.2.2 upload_tracking.json (独立数据源)

```json
{
  "slug": "example-skill",
  "lifecycle": {"stage": "public_published"},
  "is_free": false,
  "pricing_model": "paid",
  "pair_slug": "example-skill-free",
  "skillhub": {
    "uploaded": true,
    "review_status": "published",
    "public_published": true,
    "org_prefix": "@org-xxo535hs/",
    "full_slug": "@org-xxo535hs/example-skill"
  },
  "clawhub": {
    "uploaded": true,
    "status": "published"
  },
  "hermes": {
    "evaluated": true,
    "eligible": false,
    "github_published": true,
    "github_repo": "https://github.com/thcjp/hermes-skills"
  },
  "is_source": false,
  "source_origin": {"type": "clawhub", "original_slug": "..."},
  "upgrade_tracking": {"source_version": "1.0.0", "needs_upgrade": false}
}
```

#### 3.2.3 同步流水线 (version_sync_pipeline.py)

8阶段端到端自动化:

```
1. DISCOVER    — 扫描本地SKILL.md，对比DB hash检测变更
2. ENHANCE     — 内容增强(去品牌化/差异化)
3. INCREMENT   — 自动递增版本号(patch级)
4. VALIDATE    — L1-L8质量门禁检查
5. SYNC_GITHUB — git push到hermes-skills(公开)+origin(私有)
6. SYNC_SKILLHUB — 上传免费版(CLI) + 生成付费版payload
7. SYNC_CLAWHUB  — 上传到ClawHub(限流200/24h)
8. RECORD      — 记录所有平台同步结果到数据库
```

### 3.3 同步机制缺陷总结

| # | 缺陷 | 严重度 | 影响 |
|---|------|--------|------|
| 1 | 无统一sync_status字段 | P0 | 无法从DB直接查询四平台同步状态 |
| 2 | 两套数据源无同步 | P0 | SQLite与JSON数据冗余/不一致 |
| 3 | GitHub双仓库未区分 | P1 | DB中只有"github"值，不区分公开/私有 |
| 4 | hermes状态未入DB | P1 | hermes-skills状态仅在JSON中 |
| 5 | free_slug/paid_slug未创建 | P1 | 三轨关联不完整 |
| 6 | v_skill_lifecycle视图未创建 | P2 | 无法直接查询生命周期看板 |
| 7 | is_paid有581个NULL | P2 | 付费标志未设置 |
| 8 | skill_type语义混乱 | P2 | 多种旧值共存 |
| 9 | FTS表为空 | P2 | 搜索功能不可用 |
| 10 | dependencies表为空 | P3 | 依赖关系未维护 |

### 3.4 四平台同步状态评估结论

**结论: 部分实现，存在关键缺陷**

- ✅ **版本同步流水线**已实现端到端自动化，覆盖三平台
- ✅ **platform_uploads表**记录了github/clawhub/skillhub上传状态
- ✅ **upload_tracking.json**提供了细粒度生命周期跟踪
- ❌ **无统一同步状态**：无法从数据库一条SQL查询某skill在四平台的完整状态
- ❌ **两套数据源未统一**：SQLite和JSON各自为政，存在不一致风险
- ❌ **GitHub双仓库未区分**：DB记录不区分hermes-skills(公开)和origin(私有)
- ❌ **hermes平台状态未入DB**：仅在JSON中跟踪
- ❌ **三轨关联字段未创建**：free_slug/paid_slug设计但未实施

---

## 四、平台认证与配置

### 4.1 SkillHub 团队版

| 配置项 | 值 |
|--------|-----|
| ORG_ID | 862 |
| API_BASE | https://api.skillhub.cn/api/v1 |
| CLI路径 | ~/.skillhub/skills_store_cli.py |
| WAF限制 | 5800字符 |
| 认证 | 企业团队Cookie (skh_ent_token) |
| 发布命令 | `skillhub publish /d/skills/packaged-skills/skillhub/[folder] --changelog "[desc]"` |
| 审核工作流 | pending → admin_review → approved |
| 审核API | POST /api/v1/orgs/862/admin/skills/{slug}/approve {"versionId": vid} |

### 4.2 ClawHub

| 配置项 | 值 |
|--------|-----|
| API_URL | https://clawhub.ai/api |
| CLI | npx clawhub publish |
| 每日限制 | 200/24h |
| Token文件 | .credentials/clawhub_token.json |

### 4.3 GitHub 双仓库

| 仓库 | Remote | URL | 可见性 | 推送内容 |
|------|--------|-----|--------|---------|
| 公开引流 | hermes-skills | https://github.com/thcjp/hermes-skills | public | 免费+付费skill |
| 私有备份 | origin | https://github.com/thcjp/-.git | private | 全部skill+项目代码 |

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

## 五、关键API工作流

### 5.1 SkillHub审核工作流

```
上传skill(POST) → 创建版本 → reviewStatus=pending
    ↓ (平台自动处理，不可API控制)
reviewStatus=admin_review ← 可被管理员审核
    ↓ POST /api/v1/orgs/862/admin/skills/{slug}/approve {"versionId": vid}
reviewStatus=approved ← 审核通过，skill变为published
```

**核心约束**:
- pending → admin_review 转换不可API控制，需等待平台
- visibility修改只能DELETE+重传
- categoryIds/tags/summary_zh修改只能DELETE+重传
- 无PATCH/PUT非破坏性更新API

### 5.2 版本同步流水线命令

```bash
python version_sync_pipeline.py scan              # 扫描变更
python version_sync_pipeline.py sync <slug>       # 同步单个skill
python version_sync_pipeline.py sync-all          # 同步所有变更skill
python version_sync_pipeline.py status            # 查看同步状态
python version_sync_pipeline.py report            # 生成同步报告
```

### 5.3 批量审核命令

```bash
# 审核admin_review状态的skill
cd D:\skills\tools; python c:\Users\thcd\.trae-cn\work\6a6322fd6711a0efa7a6c030\batch_approve_admin_review.py

# 处理rejected skill
cd D:\skills\tools; python c:\Users\thcd\.trae-cn\work\6a6322fd6711a0efa7a6c030\handle_rejected_v2.py
```

---

## 六、已完成的里程碑

### 6.1 V54-V61 完成

| 轮次 | 主要任务 | 结果 |
|------|---------|------|
| V54 | SkillHub重新发布(企业认证) | 830个MIT skill批量上传 |
| V55-V57 | 可见性修复+分类+元数据 | categoryIds/visibility:public/tags修复 |
| V58-V59 | 批量重传+审核自动化 | 1920/1920重传完成(100%) |
| V60 | admin_review批量审核 | 334个审核通过(0失败) |
| V61 | rejected处理+DisplayName中文化 | 43个rejected处理+438个中文化(100%) |

### 6.2 Round 1-7 复核

| 轮次 | 范围 | 完成率 |
|------|------|--------|
| Round 1 | P0-1~P0-3 关键管道断裂 | 100% |
| Round 2 | Q1-Q5 质量门修复 | 100% |
| Round 3 | D1-D3 数据库追踪链接 | 100% |
| Round 4 | D4-D6 DB写入收口 | 100% |
| Round 5 | A1-A3 架构与运营闭环 | 100% |
| Round 6 | L1-L8 冗余文件清理 | 100% |
| Round 7 | R7-1~R7-5 SQL收口+DNS+审核 | 80% |
| **合计** | **30项** | **93.3%** |

---

## 七、待完成任务（按优先级）

### P0 — 立即/循环执行

1. **持续审核pending→admin_review转化** — 267个pending等待平台转换
2. **持续处理新rejected** — rejected趋近0
3. **四平台同步机制建设** — 统一sync_status字段，消除双数据源

### P1 — 短期执行

4. **Verified认证申请** — 前提条件已满足(企业认证/微信商户/skill数量/质量)
5. **Downloads/stars积累策略** — 优先P0(8个零依赖)和P1(5个award-focused)
6. **三轨关联字段实施** — 创建free_slug/paid_slug字段+回填
7. **GitHub双仓库DB区分** — platform_uploads区分github_public/github_private

### P2 — 中期执行

8. **所有权认领** — 检查slug所有权，认领非本团队占用的
9. **搜索排名优化** — 关键词/categoryIds/版本更新频率
10. **v_skill_lifecycle视图创建** — 生命周期看板
11. **R7-4: 60个skill批量处理** — batch_generate.py就绪但未启动
12. **upload_tracking.json与DB统一** — 消除双数据源

### P3 — 长期执行

13. **pricing表schema对齐** — pricing_tier列
14. **FTS表填充** — 搜索功能
15. **dependencies表维护** — 依赖关系
16. **定期清理机制** — 防止__pycache__/DB备份积累

---

## 八、技能/插件使用策略

### 8.1 各环节技能/插件调用映射

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

### 8.2 典型工作流中的调用顺序

**工作流1: 四平台同步机制建设**
```
brainstorming → writing-plans → subagent-driven-development → tdd → code-review → verification-before-completion
```

**工作流2: SkillHub批量审核**
```
agent-browser(检查状态) → 执行batch_approve脚本 → verification-before-completion
```

**工作流3: 新skill生成与上传**
```
defuddle(研究源) → generate_skill → quality_gate → enterprise_uploader → clawhub_batch_uploader → git push → DB record
```

**工作流4: 问题调试**
```
systematic-debugging → chrome-devtools(前端) → code-review → verification
```

---

## 九、约束条件

### 9.1 硬约束（来自project_memory.md）

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

### 9.2 执行约束

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

### 9.3 技术约束

25. 所有数据库连接必须 PRAGMA foreign_keys = ON
26. 使用db.py业务函数，禁止裸SQL
27. 每个修改后立即py_compile验证
28. 仅使用SkillHub团队号(不用个人号)
29. ClawHub只有一个号
30. SkillHub WAF限制5800字符

---

## 十、关键文件索引

| 类别 | 文件路径 |
|------|---------|
| 数据库定义 | `d:\skills\tools\db.py` |
| 配置中心 | `d:\skills\config\project_config.py` |
| 平台配置 | `d:\skills\config\platform_config.py` |
| GitHub策略 | `d:\skills\config\github_repo_strategy.py` |
| 版本同步流水线 | `d:\skills\tools\version_sync_pipeline.py` |
| SkillHub企业上传 | `d:\skills\tools\enterprise_uploader.py` |
| ClawHub批量上传 | `d:\skills\tools\clawhub_batch_uploader.py` |
| 每日同步 | `d:\skills\tools\daily_sync.py` |
| 平台运维 | `d:\skills\tools\platform_ops.py` |
| 深度审计 | `d:\skills\tools\deep_quality_audit.py` |
| 数据库文件 | `d:\skills\skill-registry.db` |
| JSON数据源 | `d:\skills\data\upload_tracking.json` |
| 架构设计文档 | `d:\skills\docs\specs\2026-07-24-architecture-governance-design.md` |
| 综合评审报告 | `d:\skills\.trae\documents\round1-7-comprehensive-review-v2.md` |
| 最新提示词 | `d:\skills\docs\plans\next-round-prompt-v61.0.md` |
| 架构文档 | `d:\skills\docs\ARCHITECTURE.md` |
