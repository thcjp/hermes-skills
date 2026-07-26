# 新对话首轮提示词 (v62.0) — 四平台同步机制建设 + 持续审核闭环 + Verified认证

> **日期**: 2026-07-26
> **上一轮完成**: V61 — 批量重传1920/1920(100%) + 334个admin_review审核通过(0失败) + 43个rejected处理 + DisplayName中文化438/438(100%) + Round1-7复核93.3%
> **本轮重点**: P0-3 四平台同步机制建设 + P0-1/P0-2 持续审核闭环 + P1-1 Verified认证申请
> **配套文档**: new-conversation-starter-design.md (设计), new-conversation-task-list.md (任务清单)

---

## 项目背景

这是一个Skill收集-增强-分发平台，从ClawHub/GitHub/开源社区收集Skill，增强后分为免费版/付费版，上传到SkillHub、ClawHub、GitHub三大平台。

**当前状态**:
- 本地DB: 3463个skill
- SkillHub平台: 2182个skill (1889 approved, 267 pending, 2 admin_review, 4 rejected, 20 platform_review)
- 批量重传: 1920/1920完成(100%)
- DisplayName中文化: 438/438(100%)
- Round 1-7任务: 28/30完成(93.3%)

**四平台同步现状**: 部分实现但存在关键缺陷 — 无统一sync_status字段，两套数据源(SQLite+JSON)无同步，GitHub双仓库未区分，三轨关联字段未创建。

---

## 必读文档

开始工作前必须阅读以下文档:

1. `d:\skills\docs\plans\new-conversation-starter-design.md` — 完整设计文档(架构/四平台分析/三轨模型)
2. `d:\skills\docs\plans\new-conversation-task-list.md` — 完整任务清单(P0-P3共16项)
3. `d:\skills\docs\plans\next-round-prompt-v61.0.md` — 上一轮提示词
4. `d:\skills\.trae\documents\round1-7-comprehensive-review-v2.md` — Round1-7复核报告
5. `d:\skills\docs\specs\2026-07-24-architecture-governance-design.md` — 架构治理设计文档

---

## 技能/插件使用指南

### 按环节调用映射

| 环节 | 调用 | 用途 |
|------|------|------|
| 设计新功能/方案 | `Use Skill: brainstorming` | 探索需求，形成设计方案，产出spec文档 |
| 需求验证/HOTL合约 | `Use plugin: trae-remote-official:hotl` | 生成HOTL合约(intent/verification/governance) |
| 编写实施计划 | `Use plugin: trae-remote-official:superpowers` (writing-plans) | 创建bite-sized可执行计划 |
| 并行子代理执行 | `Use plugin: trae-remote-official:superpowers` (subagent-driven-development) | 独立任务并行执行 |
| TDD开发 | `Use plugin: trae-remote-official:superpowers` (test-driven-development) | RED-GREEN-REFACTOR循环 |
| 测试生成 | `Use plugin: trae-remote-official:tailtest` | 为Python文件生成R1-R15规则测试 |
| 系统调试 | `Use plugin: trae-remote-official:superpowers` (systematic-debugging) | 系统化调试任何bug/失败 |
| 代码审查 | `Use plugin: trae-remote-official:coderabbit` | AI代码审查，PR反馈 |
| HOTL代码审查 | `Use plugin: trae-remote-official:hotl` (code-review) | 对照HOTL合约审查 |
| 浏览器自动化 | `Use Skill: agent-browser` | SkillHub/ClawHub平台操作 |
| 浏览器调试 | `Use plugin: trae-remote-official:chrome-devtools` | 前端检查/网络请求/控制台 |
| 网页内容提取 | `Use Skill: defuddle` | 提取网页clean markdown内容 |
| UI/Dashboard设计 | `Use plugin: trae-remote-official:stark` | Web界面设计(如需dashboard) |
| AI产品构建 | `Use plugin: trae-remote-official:runtype-skills` | AI产品/Agent/Flow构建(如需) |
| 工程决策 | `Use plugin: trae-remote-official:staff-engineer-mode` | 跨生命周期工程决策 |
| 完成验证 | `Use plugin: trae-remote-official:superpowers` (verification-before-completion) | 声称完成前必须验证 |
| Git分支完成 | `Use plugin: trae-remote-official:superpowers` (finishing-a-development-branch) | 决定merge/PR/cleanup |
| TRAE反馈 | `Use Skill: feedback` | 提交TRAE产品反馈 |

### 典型工作流调用顺序

**工作流1: 四平台同步机制建设(本轮核心)**
```
Use Skill: brainstorming  →  设计sync_status字段方案
Use plugin: trae-remote-official:superpowers (writing-plans)  →  编写实施计划
Use plugin: trae-remote-official:superpowers (tdd)  →  TDD开发db.py增强
Use plugin: trae-remote-official:tailtest  →  生成测试用例
Use plugin: trae-remote-official:coderabbit  →  代码审查
Use plugin: trae-remote-official:superpowers (verification-before-completion)  →  验证完成
```

**工作流2: SkillHub批量审核**
```
Use Skill: agent-browser  →  检查平台审核状态
执行batch_approve_admin_review.py  →  批量审核
Use plugin: trae-remote-official:superpowers (verification-before-completion)  →  验证结果
```

**工作流3: Verified认证申请**
```
Use Skill: agent-browser  →  访问SkillHub后台
Use Skill: defuddle  →  提取认证申请要求
准备材料并提交
```

**工作流4: 问题调试**
```
Use plugin: trae-remote-official:superpowers (systematic-debugging)  →  系统化调试
Use plugin: trae-remote-official:chrome-devtools  →  浏览器调试(前端问题)
Use plugin: trae-remote-official:coderabbit  →  代码审查
```

---

## 本轮实施任务

### 任务1: P0-1 持续审核 pending→admin_review 转化 (P0 — 循环执行)

**机制**: 平台会自动将pending转为admin_review，需定期审核

```bash
# 清除进度文件
cd D:\skills; python -c "
import json
f = 'data/reports/batch_approve_progress_v2.json'
d = json.load(open(f, 'r', encoding='utf-8'))
d['success'] = []; d['failed'] = []; d['total'] = 0; d['completed'] = 0
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
"

# 运行审核
cd D:\skills\tools; python c:\Users\thcd\.trae-cn\work\6a6322fd6711a0efa7a6c030\batch_approve_admin_review.py
```

**验证**: approved数量持续增长，pending数量持续减少
**技能调用**: 先 `Use Skill: agent-browser` 检查平台当前状态

### 任务2: P0-2 持续处理新 rejected (P0 — 循环执行)

```bash
cd D:\skills\tools; python c:\Users\thcd\.trae-cn\work\6a6322fd6711a0efa7a6c030\handle_rejected_v2.py
```

**验证**: rejected数量趋近0
**技能调用**: 如有复杂拒绝原因，`Use plugin: trae-remote-official:superpowers` (systematic-debugging)

### 任务3: P0-3 四平台同步机制建设 (P0 — 本轮核心)

这是本轮最重要的任务。使用以下技能/插件顺序执行:

#### 步骤3a: 设计方案
```
Use Skill: brainstorming
```
设计sync_status字段方案，覆盖:
- skills表添加4个同步状态字段(skillhub_sync_status, clawhub_sync_status, github_public_sync_status, github_private_sync_status)
- 同步状态值定义: synced/pending/failed/not_applicable/unknown
- 回填策略(从platform_uploads和upload_tracking.json)
- GitHub双仓库DB区分(github → github_public + github_private)

#### 步骤3b: 编写实施计划
```
Use plugin: trae-remote-official:superpowers (writing-plans)
```
创建bite-sized实施计划，每个任务有明确的文件路径和验证命令。

#### 步骤3c: TDD开发
```
Use plugin: trae-remote-official:superpowers (test-driven-development)
```
对db.py的增强使用TDD: 先写测试(ALTER TABLE/回填/查询)，再实现。

#### 步骤3d: 生成测试用例
```
Use plugin: trae-remote-official:tailtest
```
为db.py生成R1-R15规则层测试。

#### 步骤3e: 代码审查
```
Use plugin: trae-remote-official:coderabbit
```
审查所有修改，确保:
- 向后兼容(不破坏enterprise_uploader.py)
- 幂等操作(可重复执行)
- 使用db.py业务函数(禁止裸SQL)
- PRAGMA foreign_keys = ON

#### 步骤3f: 验证完成
```
Use plugin: trae-remote-official:superpowers (verification-before-completion)
```
验证:
- 一条SQL可查询任意skill的四平台同步状态
- platform_uploads表中github_public和github_private分开记录
- upload_tracking.json中的hermes状态已同步到DB

**影响文件**:
- `tools/db.py` — 添加字段定义、回填函数、查询函数
- `tools/version_sync_pipeline.py` — 修改SYNC_GITHUB阶段record调用
- `tools/platform_ops.py` — 统一数据源逻辑

### 任务4: P1-1 Verified 认证申请 (P1)

```
Use Skill: agent-browser
```
访问 https://www.skillhub.cn/enterprise/org-xxo535hs 检查Verified认证入口。

```
Use Skill: defuddle
```
提取认证申请要求文档。

**前提条件已满足**:
- 企业团队已通过认证 ✅
- 已绑定微信商户号 ✅
- skill数量充足 ✅ (2182个)
- skill质量合格 ✅ (displayName中文化100%, description≥150字符)

### 任务5: P1-3 三轨关联字段实施 (P1)

```sql
ALTER TABLE skills ADD COLUMN free_slug TEXT;
ALTER TABLE skills ADD COLUMN paid_slug TEXT;
CREATE INDEX IF NOT EXISTS idx_skills_free ON skills(free_slug);
CREATE INDEX IF NOT EXISTS idx_skills_paid ON skills(paid_slug);
```

回填: 通过parent_slug关联免费版和付费版。

**技能调用**: `Use plugin: trae-remote-official:superpowers` (tdd) + `Use plugin: trae-remote-official:coderabbit`

### 任务6: Git提交与下一轮提示词生成

```bash
cd D:\skills
git add -A
git commit -m "feat: V62 — 四平台同步机制建设 + 持续审核闭环 + Verified认证申请 + 三轨关联字段"
git push origin main
git push hermes-skills main
```

生成 `next-round-prompt-v63.0.md`

---

## 任务执行顺序

```
任务1 (持续审核admin_review) ── 循环执行 ──────────────┐
                                                       │
任务2 (持续处理rejected) ── 循环执行 ──────────────────┤
                                                       │
任务3 (四平台同步机制) ── 本轮核心 ────────────────────┤
  3a: brainstorming(设计)                              │
  3b: writing-plans(计划)                              │
  3c: tdd(开发)                                        ├──→ 任务6 (Git提交)
  3d: tailtest(测试)                                   │
  3e: code-review(审查)                                │
  3f: verification(验证)                               │
                                                       │
任务4 (Verified认证) ── 可并行 ────────────────────────┤
                                                       │
任务5 (三轨关联字段) ── 可并行 ────────────────────────┘
```

---

## 验证检查清单

- [ ] 267个pending有部分转为admin_review并审核通过
- [ ] rejected数量趋近0
- [ ] skills表有skillhub_sync_status/clawhub_sync_status/github_public_sync_status/github_private_sync_status字段
- [ ] 一条SQL可查询任意skill的四平台同步状态
- [ ] platform_uploads表中github_public和github_private分开记录
- [ ] upload_tracking.json中的hermes状态已同步到DB
- [ ] Verified认证申请已提交(或确认无入口)
- [ ] skills表有free_slug/paid_slug字段且已回填
- [ ] Git提交并推送到双远程仓库
- [ ] 下一轮提示词v63.0生成
- [ ] 使用verification-before-completion验证所有声称完成的任务

---

## 约束条件

1. **增强已有代码** — 不创建碎片化新文件，所有修复功能集成到现有工具脚本
2. **不模拟/mock** — 所有操作必须真实执行
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏enterprise_uploader.py现有功能
5. **企业账号** — 所有API操作必须使用企业团队账号Cookie
6. **categoryIds** — 所有上传必须包含categoryIds数字ID数组
7. **visibility:public** — 所有上传必须包含visibility:public
8. **断点续传** — 全量重传支持从报告文件恢复进度
9. **内容保真** — DisplayName翻译不得改变技能原有语义
10. **分类统一** — 本地分类=skillhub分类=clawhub分类
11. **审核工作流** — admin_review状态才能approve，pending需等待平台
12. **非破坏性更新不可用** — categoryIds/tags/summary_zh修改只能DELETE+重传
13. **搜索路径完整** — find_skill_md搜索PACKAGED+OPENSOURCE+ENTERPRISE_UPLOAD+DIFFERENTIATED四个目录
14. **PRAGMA** — 所有数据库连接必须 PRAGMA foreign_keys = ON
15. **禁止裸SQL** — 使用db.py业务函数
16. **py_compile** — 每个修改后立即py_compile验证
17. **仅团队号** — 仅使用SkillHub团队号(不用个人号)
18. **WAF限制** — SkillHub WAF限制5800字符
19. **ClawHub限流** — 每日200/24h

---

## 关键API参考

### SkillHub 审核API
```
POST /api/v1/orgs/862/admin/skills/{slug}/approve
Body: {"versionId": vid}
```
仅对admin_review状态的skill有效。

### SkillHub 状态查询
```
GET /api/v1/orgs/862/admin/skills?reviewStatus=pending
GET /api/v1/orgs/862/admin/skills?reviewStatus=admin_review
GET /api/v1/orgs/862/admin/skills?reviewStatus=rejected
GET /api/v1/orgs/862/admin/skills?reviewStatus=approved
```

### 数据库路径
```
d:\skills\skill-registry.db
```

### 关键脚本路径
```
d:\skills\tools\enterprise_uploader.py          — SkillHub企业版上传
d:\skills\tools\version_sync_pipeline.py        — 版本同步流水线
d:\skills\tools\db.py                           — 数据库模块
d:\skills\tools\clawhub_batch_uploader.py       — ClawHub批量上传
d:\skills\config\platform_config.py             — 平台配置
d:\skills\data\upload_tracking.json             — 上传追踪JSON
d:\skills\data\category_mapping.json            — 分类映射
```

---

## 团队分类ID映射

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

## 下一轮提示词生成要求

完成本轮任务后，生成 `next-round-prompt-v63.0.md`，格式参考本文档，包含:
1. 本轮完成总结(表格)
2. 平台当前状态
3. 实施任务(按优先级)
4. 技能/插件使用指南
5. 验证检查清单
6. 约束条件
