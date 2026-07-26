# 新对话首轮提示词 (v63.0) — 同步状态消缺 + 持续审核闭环 + Verified认证 + Downloads/Stars策略

> **日期**: 2026-07-26
> **上一轮完成**: V62 — 四平台同步机制建设(sync_status字段+回填+GitHub双仓库DB区分+Hermes JSON→DB同步) + 三轨关联字段(free_slug=2861/paid_slug=2305) + v_skill_lifecycle视图增强 + find_skill_md搜索路径完善 + Git推送双远程(c0e62a2b3)
> **本轮重点**: P0-4 同步状态unknown消缺 + P0-1/P0-2 持续审核闭环 + P1-1 Verified认证 + P1-2 Downloads/Stars策略
> **配套文档**: new-conversation-starter-design.md (设计), new-conversation-task-list.md (任务清单)

---

## 项目背景

这是一个Skill收集-增强-分发平台，从ClawHub/GitHub/开源社区收集Skill，增强后分为免费版/付费版，上传到SkillHub、ClawHub、GitHub三大平台。

**当前状态**:
- 本地DB: 3463个skill
- v_skill_lifecycle视图: 3444条记录
- SkillHub平台(JSON): 2068 published, 31 deleted, 7 pending
- 四平台同步状态:
  - SkillHub: synced=1120, unknown=2257, not_applicable=86
  - ClawHub: synced=708, unknown=1208, not_applicable=1547
  - GitHub公开: synced=1640, unknown=1739, not_applicable=84
  - GitHub私有: not_applicable=597, unknown=2866
- 三轨关联: free_slug=2861, paid_slug=2305
- platform_uploads: github_public=1640, clawhub=1155, skillhub=1129

**V62完成**: 四平台同步机制已建立并验证通过(10/10)，但存在大量unknown状态记录需消缺。

---

## 必读文档

开始工作前必须阅读以下文档:

1. `d:\skills\docs\plans\new-conversation-starter-design.md` — 完整设计文档(架构/四平台分析/三轨模型)
2. `d:\skills\docs\plans\new-conversation-task-list.md` — 完整任务清单(P0-P3共16项)
3. `d:\skills\docs\plans\next-round-prompt-v63.0.md` — 本提示词
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

**工作流1: 同步状态unknown消缺(本轮核心)**
```
Use plugin: trae-remote-official:superpowers (systematic-debugging)  →  分析unknown原因
Use Skill: brainstorming  →  设计消缺方案
Use plugin: trae-remote-official:superpowers (writing-plans)  →  编写实施计划
Use plugin: trae-remote-official:superpowers (tdd)  →  TDD开发消缺逻辑
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

**工作流4: Downloads/Stars策略**
```
Use Skill: agent-browser  →  检查API能力
Use plugin: trae-remote-official:superpowers (systematic-debugging)  →  分析API
Use plugin: trae-remote-official:staff-engineer-mode  →  工程决策
```

---

## 本轮实施任务

### 任务1: P0-4 同步状态unknown消缺 (P0 — 本轮核心)

**问题**: V62建立的sync_status字段有大量unknown记录:
- SkillHub: 2257条unknown (65%)
- ClawHub: 1208条unknown (35%)
- GitHub公开: 1739条unknown (50%)
- GitHub私有: 2866条unknown (83%)

**根因分析**:
1. SkillHub unknown=2257: 大量skill已上传到平台(JSON中published=2068)，但platform_uploads表中无记录
2. ClawHub unknown=1208: 类似原因，JSON中有clawhub状态但DB未回填
3. GitHub公开 unknown=1739: 部分skill推送到GitHub但未记录到platform_uploads
4. GitHub私有 unknown=2866: 私有仓库推送记录缺失

**消缺策略**:
```
Use plugin: trae-remote-official:superpowers (systematic-debugging)
```
分析每个unknown记录的来源：
- 从upload_tracking.json的skillhub/clawhub/hermes对象回填
- 从git log回填GitHub推送记录
- 从本地文件存在性判断not_applicable
- 对确实未上传的标记为pending

**实施步骤**:
```
Use Skill: brainstorming
```
设计增强backfill_sync_status()函数，增加JSON→DB回填逻辑。

```
Use plugin: trae-remote-official:superpowers (tdd)
```
增强db.py中的backfill_sync_status()，从upload_tracking.json补充回填。

```
Use plugin: trae-remote-official:coderabbit
```
审查回填逻辑，确保幂等和向后兼容。

**验证**: unknown数量减少50%以上，synced数量持续增长

**影响文件**:
- `tools/db.py` — 增强backfill_sync_status()函数
- `tools/platform_ops.py` — 统一数据源逻辑(如需)

### 任务2: P0-1 持续审核 pending→admin_review 转化 (P0 — 循环执行)

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

### 任务3: P0-2 持续处理新 rejected (P0 — 循环执行)

```bash
cd D:\skills\tools; python c:\Users\thcd\.trae-cn\work\6a6322fd6711a0efa7a6c030\handle_rejected_v2.py
```

**验证**: rejected数量趋近0
**技能调用**: 如有复杂拒绝原因，`Use plugin: trae-remote-official:superpowers` (systematic-debugging)

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
- skill数量充足 ✅ (2068个published)
- skill质量合格 ✅ (displayName中文化100%, description≥150字符)

### 任务5: P1-2 Downloads/Stars积累策略 (P1)

```
Use plugin: trae-remote-official:staff-engineer-mode
```
评估Downloads/Stars积累的工程可行性和策略。

```
Use Skill: agent-browser
```
检查SkillHub API是否支持star/download操作。

**优先处理**:
- P0: 8个零依赖skill
- P1: 5个award-focused skill

### 任务6: P2-5 upload_tracking.json与DB统一 (P2 — 可提前)

**问题**: 双数据源(SQLite+JSON)存在不一致风险
- SQLite skills表: 3463条
- JSON skills对象: 2216条
- 差异: 1247条skill在SQLite中但不在JSON中

```
Use Skill: brainstorming
```
设计统一方案：JSON作为DB的缓存/导出，DB为唯一权威源。

```
Use plugin: trae-remote-official:superpowers (writing-plans)
```
编写迁移计划，确保数据不丢失。

### 任务7: Git提交与下一轮提示词生成

```bash
cd D:\skills
git add -A
git commit -m "feat: V63 — 同步状态unknown消缺 + 持续审核闭环 + Verified认证 + Downloads/Stars策略"
git push origin main
git push hermes-skills main
```

生成 `next-round-prompt-v64.0.md`

---

## 任务执行顺序

```
任务1 (同步状态unknown消缺) ── 本轮核心 ────────────────┐
  systematic-debugging(分析)                              │
  brainstorming(设计)                                     │
  writing-plans(计划)                                     │
  tdd(开发)                                              ├──→ 任务7 (Git提交)
  code-review(审查)                                       │
  verification(验证)                                      │
                                                          │
任务2 (持续审核admin_review) ── 循环执行 ──────────────────┤
任务3 (持续处理rejected) ── 循环执行 ──────────────────────┤
任务4 (Verified认证) ── 可并行 ──────────────────────────┤
任务5 (Downloads/Stars) ── 可并行 ────────────────────────┤
任务6 (JSON与DB统一) ── 可并行 ────────────────────────────┘
```

---

## V62验证结果(已完成)

| 验证项 | 状态 | 关键数据 |
|--------|------|---------|
| Schema字段 | PASS | 8个新字段全部存在 |
| 索引 | PASS | 6个索引全部创建 |
| 同步状态回填 | PASS | SH:1206, CH:2255, GH_pub:1724 |
| GitHub双仓库区分 | PASS | github→github_public迁移完成(1640条) |
| Hermes状态同步 | PASS | 1640条synced |
| 三轨关联字段 | PASS | free:2861, paid:2305 |
| v_skill_lifecycle视图 | PASS | 包含所有sync_status列(3444条) |
| 一条SQL查询 | PASS | 四平台状态可查 |
| py_compile | PASS | 3个文件编译通过 |
| find_skill_md | PASS | 包含enterprise搜索路径 |

---

## 验证检查清单

- [ ] SkillHub unknown从2257减少到<1000
- [ ] ClawHub unknown从1208减少到<500
- [ ] GitHub公开unknown从1739减少到<800
- [ ] GitHub私有unknown从2866减少到<1500
- [ ] 7个pending有部分转为admin_review并审核通过
- [ ] rejected数量趋近0
- [ ] Verified认证申请已提交(或确认无入口)
- [ ] Downloads/Stars策略已制定并开始执行
- [ ] JSON与DB统一方案已设计
- [ ] Git提交并推送到双远程仓库
- [ ] 下一轮提示词v64.0生成
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
d:\skills\config\project_config.py             — 平台配置
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

完成本轮任务后，生成 `next-round-prompt-v64.0.md`，格式参考本文档，包含:
1. 本轮完成总结(表格)
2. 平台当前状态
3. 实施任务(按优先级)
4. 技能/插件使用指南
5. 验证检查清单
6. 约束条件
