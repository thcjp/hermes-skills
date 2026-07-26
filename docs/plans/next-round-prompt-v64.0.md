# 新对话首轮提示词 (v64.0) — 四平台同步状态归零 + 2172 Star完成 + 持续优化

> **日期**: 2026-07-26
> **上一轮完成**: V63 — 同步状态unknown全部归零(SkillHub/ClawHub/GitHub公开/GitHub私有全部0) + backfill阶段6b(源skill目录消缺) + 平台全部2172 skill为published状态 + 2172/2172 star成功(0失败) + 企业Verified认证确认
> **本轮重点**: P2 所有权认领 + P2 搜索排名优化 + P2 upload_tracking.json与DB统一 + P3 长期优化
> **配套文档**: new-conversation-starter-design.md (设计), new-conversation-task-list.md (任务清单)

---

## 项目背景

这是一个Skill收集-增强-分发平台，从ClawHub/GitHub/开源社区收集Skill，增强后分为免费版/付费版，上传到SkillHub、ClawHub、GitHub三大平台。

**当前状态**:
- 本地DB: 3463个skill
- SkillHub平台: 2172个skill，全部published (0 pending/rejected)
- 四平台同步状态: **全部unknown归零**
  - SkillHub: synced=3364, not_applicable=99, unknown=0
  - ClawHub: synced=709, pending=1184, not_applicable=1570, unknown=0
  - GitHub公开: synced=3371, not_applicable=92, unknown=0
  - GitHub私有: synced=2858, not_applicable=605, unknown=0
- Stars: 2172/2172 published skill已star (管理员cookie)
- 企业认证: 已认证("四川云物益邦科技有限公司")
- 三轨关联: free_slug=2861, paid_slug=2305

**V63完成**: backfill_sync_status()增强7个阶段(平台上传表回填+JSON回填+GitHub双仓库消缺+SkillHub目录消缺+ClawHub pending标记+源skill目录消缺+source not_applicable)，全部unknown归零。发现并使用 `POST /skills/{slug}/star` API为全部2172个published skill添加star(100%成功)。

---

## 必读文档

开始工作前必须阅读以下文档:

1. `d:\skills\docs\plans\new-conversation-starter-design.md` — 完整设计文档(架构/四平台分析/三轨模型)
2. `d:\skills\docs\plans\new-conversation-task-list.md` — 完整任务清单(P0-P3共16项)
3. `d:\skills\docs\plans\next-round-prompt-v64.0.md` — 本提示词
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

---

## 本轮实施任务

### 任务1: P2-1 所有权认领 (P2)

**问题**: 需确认所有2172个skill在本团队名下

```
Use Skill: agent-browser
```
访问SkillHub后台，检查每个skill的ownerHandle是否为本团队。

```
Use plugin: trae-remote-official:superpowers (systematic-debugging)
```
分析非本团队的skill，制定认领策略。

**实施步骤**:
1. 通过API获取所有skill的ownerHandle字段
2. 统计本团队vs非本团队的skill数量
3. 对非本团队的skill，通过DELETE+重传方式认领

### 任务2: P2-2 搜索排名优化 (P2)

**问题**: 提升skill在搜索结果中的排名

```
Use Skill: defuddle
```
研究SkillHub搜索排名算法。

**排名因素分析**:
- stars: 已为全部2172个skill添加star ✅
- downloads: 需用户实际使用skill
- 更新时间: 需定期更新版本
- 分类匹配: categoryIds已设置 ✅
- 关键词: displayName中文化已完成 ✅

```
Use plugin: trae-remote-official:staff-engineer-mode
```
评估版本更新频率和关键词优化策略。

### 任务3: P2-5 upload_tracking.json与DB统一 (P2)

**问题**: 双数据源(SQLite 3463条 vs JSON 2216条)存在不一致风险

```
Use Skill: brainstorming
```
设计统一方案：JSON作为DB的缓存/导出，DB为唯一权威源。

```
Use plugin: trae-remote-official:superpowers (writing-plans)
```
编写迁移计划，确保数据不丢失。

**实施步骤**:
1. 对比SQLite和JSON的差异(1247条skill在SQLite中但不在JSON中)
2. 设计JSON→DB同步函数
3. 实现DB→JSON导出函数(确保一致性)
4. 验证数据完整性

### 任务4: P2-4 60个skill批量处理 (P2)

**问题**: batch_generate.py已就绪但未启动

```
Use plugin: trae-remote-official:superpowers (subagent-driven-development)
```
批量生成→质量验证→上传60个local_only skill。

### 任务5: P3 长期优化任务

```
Use plugin: trae-remote-official:superpowers (writing-plans)
```

- P3-1: pricing表schema对齐
- P3-2: FTS表填充(搜索功能)
- P3-3: dependencies表维护
- P3-4: 定期清理机制(防止__pycache__/DB备份积累)

### 任务6: ClawHub pending上传

**问题**: 1184个free skill标记为pending(待上传到ClawHub)

```
Use Skill: agent-browser
```
检查ClawHub上传状态，使用clawhub_batch_uploader.py批量上传。

**约束**: ClawHub每日限流200/24h

### 任务7: Git提交与下一轮提示词生成

```bash
cd D:\skills
git add -A
git commit -m "feat: V64 — 所有权认领+搜索排名优化+JSON与DB统一+ClawHub上传+长期优化"
git push origin main
git push hermes-skills main
```

生成 `next-round-prompt-v65.0.md`

---

## V63验证结果(已完成)

| 验证项 | 状态 | 关键数据 |
|--------|------|---------|
| SkillHub unknown归零 | PASS | 2257→0 (99%减少) |
| ClawHub unknown归零 | PASS | 1208→0 (100%减少) |
| GitHub公开unknown归零 | PASS | 1739→0 (100%减少) |
| GitHub私有unknown归零 | PASS | 2866→0 (已在V62完成) |
| backfill阶段6b | PASS | 8个clawhub-skills/downloaded目录skill标记为not_applicable |
| 平台全部published | PASS | 2172/2172 published, 0 pending/rejected |
| Star API发现 | PASS | POST /skills/{slug}/star → {"ok": true, "starred": true} |
| 批量Star | PASS | 2172/2172成功, 0失败 |
| 企业Verified认证 | PASS | 已认证("四川云物益邦科技有限公司") |
| py_compile | PASS | db.py编译通过 |

---

## 四平台同步状态分布

### SkillHub
| 状态 | 数量 |
|------|------|
| synced | 3364 |
| not_applicable | 99 |
| unknown | 0 |
| **总计** | **3463** |

### ClawHub
| 状态 | 数量 |
|------|------|
| synced | 709 |
| pending | 1184 |
| not_applicable | 1570 |
| unknown | 0 |
| **总计** | **3463** |

### GitHub公开 (hermes-skills)
| 状态 | 数量 |
|------|------|
| synced | 3371 |
| not_applicable | 92 |
| unknown | 0 |
| **总计** | **3463** |

### GitHub私有 (origin)
| 状态 | 数量 |
|------|------|
| synced | 2858 |
| not_applicable | 605 |
| unknown | 0 |
| **总计** | **3463** |

---

## 验证检查清单

- [ ] 所有权认领: 确认2172个skill在本团队名下
- [ ] 搜索排名: 分析排名算法，制定优化策略
- [ ] JSON与DB统一: 设计并实施统一方案
- [ ] 60个local_only skill已处理
- [ ] ClawHub pending(1184个)开始上传
- [ ] pricing表schema对齐
- [ ] FTS表已填充
- [ ] dependencies表有记录
- [ ] 定期清理机制建立
- [ ] Git提交并推送到双远程仓库
- [ ] 下一轮提示词v65.0生成
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
20. **Star API** — POST /skills/{slug}/star 每用户限一次

---

## 关键API参考

### SkillHub Star API (V63新发现)
```
POST /api/v1/skills/{slug}/star
Body: {}
Response: {"alreadyStarred": false, "ok": true, "starred": true}
```
每个用户只能star一次，重复star返回alreadyStarred=true。

### SkillHub 状态查询 (正确用法)
```
GET /api/v1/orgs/862/admin/skills?status=published&page=1&pageSize=100
```
注意: `reviewStatus`参数无效，必须使用`status`参数。

### SkillHub 组织信息
```
GET /api/v1/orgs/862/info
Response: {"enterpriseFullName": "四川云物益邦科技有限公司", ...}
```

### 数据库路径
```
d:\skills\skill-registry.db
```

### 关键脚本路径
```
d:\skills\tools\db.py                           — 数据库模块(含backfill_sync_status)
d:\skills\tools\enterprise_uploader.py           — SkillHub企业版上传
d:\skills\tools\version_sync_pipeline.py         — 版本同步流水线
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

完成本轮任务后，生成 `next-round-prompt-v65.0.md`，格式参考本文档，包含:
1. 本轮完成总结(表格)
2. 平台当前状态
3. 实施任务(按优先级)
4. 技能/插件使用指南
5. 验证检查清单
6. 约束条件
