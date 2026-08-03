# 新对话首轮提示词 (v65.0) — 内容质量99.4%达标 + 独立升级流程 + L1.5门禁 + 批量重传待执行

> **日期**: 2026-07-26
> **上一轮完成**: V64 — 内容质量全面升级(v3.2) + 独立skill升级流程 + L1.5内容质量门禁
> **本轮重点**: P0 批量重传已修复skill到SkillHub + P0 Git推送(网络重试) + P1 L1合规修复 + P2 延续任务
> **配套文档**: new-conversation-starter-design.md (设计), new-conversation-task-list.md (任务清单)

---

## 项目背景

这是一个Skill收集-增强-分发平台，从ClawHub/GitHub/开源社区收集Skill，增强后分为免费版/付费版，上传到SkillHub、ClawHub、GitHub三大平台。

**当前状态**:
- 本地DB: 3463个skill
- SkillHub平台: 2172个skill published
- 四平台同步状态: 全部unknown归零
  - SkillHub: synced=3364, not_applicable=99, unknown=0
  - ClawHub: synced=709, pending=1184, not_applicable=1570, unknown=0
  - GitHub公开: synced=3371, not_applicable=92, unknown=0
  - GitHub私有: synced=2858, not_applicable=605, unknown=0
- 三轨关联: free_slug=2861, paid_slug=2305
- 企业认证: 已认证("四川云物益邦科技有限公司")
- Stars: 2172/2172 published skill已star

**V64完成**: 内容质量检测修复系统(v3.2) + 独立skill升级流程 + L1.5内容质量门禁

---

## V64完成总结

| 验证项 | 状态 | 关键数据 |
|--------|------|---------|
| 内容质量检测系统 | PASS | 7项检查: summary/description去重,模板套话,占位符,body重复句子,章节合并,空输入表 |
| 内容质量自动修复 | PASS | 7项修复函数: 含新增fix_duplicate_sentences_body |
| 内容质量通过率 | PASS | 11.0% → 99.4% (310→2801/2818) |
| 批量修复skill数 | PASS | 2764个skill内容质量已修复 |
| 独立升级流程 | PASS | upgrade_single_skill() + CLI upgrade命令 |
| 升级流程测试 | PASS | ws-agent-browser: 内容7/7通过, L1合规正确阻止 |
| L1.5质量门禁 | PASS | run_content_quality_gate()集成到version_sync_pipeline |
| 检查逻辑修复 | PASS | summary/description不存在时返回True(无需检查) |
| fix_empty_input_table增强 | PASS | 正则支持空行和可变列数 |
| py_compile | PASS | skill_batch_upgrader_v3.py + version_sync_pipeline.py |
| Git提交 | PASS | 4d68b6dbe (1901 files, +157363/-53627) |
| Git推送 | FAIL | GitHub网络不可达(origin + hermes-skills均超时) |

---

## 质量根因分析

### 问题发现
用户随机抽查SkillHub上的`ws-agent-browser-sk`技能，AI测评出大量质量问题：
- summary/description重复文本
- 模板化套话("按照skill规范执行"等)
- 占位符内容("根据实际场景填充"等)
- body中重复句子
- 章节错误合并(### 标题跟在上一行末尾)
- 空输入格式表(只有表头没有数据行)

### 根因定位
| 根因类型 | 具体原因 | 影响范围 |
|----------|---------|---------|
| **生产流程问题** | 批量生成脚本(batch_generate.py)产出模板化内容 | 89%的skill受影响(初始2508/2818) |
| **质量阀门问题** | 批量上传时L2(LLM验证)/L3(Agent试用)检查被跳过 | 低质量skill直接上传到平台 |
| **检查逻辑缺陷** | summary/description不存在时返回False(误报) | 虚增259+333个失败计数 |

### 解决方案
| 方案 | 实现 | 效果 |
|------|------|------|
| L1.5内容质量门禁 | version_sync_pipeline新增run_content_quality_gate() | 阻止低质量skill上传 |
| 自动检测+修复 | skill_batch_upgrader_v3.py content-check/content-fix | 通过率11%→99.4% |
| 独立升级流程 | upgrade_single_skill() + CLI upgrade命令 | 单skill完整升级链路 |
| 检查逻辑修复 | 不存在字段返回True而非False | 消除误报 |

---

## 本轮实施任务

### 任务1: P0 Git推送(网络重试) (P0)

**问题**: V64提交(4d68b6dbe)因GitHub网络不可达未能推送

```bash
cd D:\skills
git push origin main
git push hermes-skills main
```

### 任务2: P0 批量重传已修复skill到SkillHub (P0)

**问题**: 2764个skill内容已修复但平台版本未更新

```
Use Skill: agent-browser
```

需要将修复后的skill重新上传到SkillHub平台。

**约束**:
- SkillHub非破坏性更新不可用(categoryIds/tags/summary_zh修改只能DELETE+重传)
- WAF限制5800字符
- 需要先通过L1.5内容质量门禁
- 使用version_sync_pipeline.py sync-all批量同步

**实施步骤**:
1. 运行`python tools/version_sync_pipeline.py scan`检测变更
2. 运行`python tools/version_sync_pipeline.py sync-all`批量同步
3. 验证SkillHub平台版本已更新

### 任务3: P1 L1合规修复 (P1)

**问题**: ws-agent-browser等skill内容质量通过(7/7)但L1格式合规未通过

```
Use plugin: trae-remote-official:superpowers (systematic-debugging)
```

L1合规失败项:
- slug==name==folder一致性
- slug为kebab-case
- frontmatter 8必需字段
- displayName≤20字符
- summary≤100字符
- description长度(150-280字符)
- version格式
- tools为YAML数组

**实施步骤**:
1. 扫描所有skill的L1合规状态
2. 使用skill_batch_upgrader_v3.py fix命令批量修复
3. 验证修复结果

### 任务4: P2 延续V64任务

#### P2-1 所有权认领
```
Use Skill: agent-browser
```
检查所有2172个skill的ownerHandle是否为本团队。

#### P2-2 搜索排名优化
```
Use Skill: defuddle
```
研究SkillHub搜索排名算法，优化stars/downloads/更新频率。

#### P2-3 upload_tracking.json与DB统一
```
Use Skill: brainstorming
```
设计JSON→DB同步方案，DB为唯一权威源。

#### P2-4 ClawHub pending上传
1184个free skill标记为pending(待上传到ClawHub)。
```
Use Skill: agent-browser
```
使用clawhub_batch_uploader.py批量上传。约束: 每日200/24h。

### 任务5: P3 长期优化

- P3-1: 处理剩余17个空输入表skill
- P3-2: pricing表schema对齐
- P3-3: FTS表填充(搜索功能)
- P3-4: dependencies表维护
- P3-5: 内容质量监控(新skill入库时自动检查)
- P3-6: 定期清理机制(防止__pycache__/DB备份积累)

### 任务6: Git提交与下一轮提示词生成

```bash
cd D:\skills
git add -A
git commit -m "feat: V65 — 批量重传+L1合规修复+所有权认领+JSON-DB统一+ClawHub上传"
git push origin main
git push hermes-skills main
```

生成 `next-round-prompt-v66.0.md`

---

## 必读文档

开始工作前必须阅读以下文档:

1. `d:\skills\docs\plans\new-conversation-starter-design.md` — 完整设计文档
2. `d:\skills\docs\plans\new-conversation-task-list.md` — 完整任务清单
3. `d:\skills\docs\plans\next-round-prompt-v65.0.md` — 本提示词
4. `d:\skills\.trae\documents\round1-7-comprehensive-review-v2.md` — Round1-7复核报告

---

## 技能/插件使用指南

| 环节 | 调用 | 用途 |
|------|------|------|
| 设计新功能/方案 | `Use Skill: brainstorming` | 探索需求，形成设计方案 |
| 需求验证/HOTL合约 | `Use plugin: trae-remote-official:hotl` | 生成HOTL合约 |
| 编写实施计划 | `Use plugin: trae-remote-official:superpowers` (writing-plans) | 创建可执行计划 |
| 并行子代理执行 | `Use plugin: trae-remote-official:superpowers` (subagent-driven-development) | 独立任务并行执行 |
| TDD开发 | `Use plugin: trae-remote-official:superpowers` (test-driven-development) | RED-GREEN-REFACTOR |
| 测试生成 | `Use plugin: trae-remote-official:tailtest` | 为Python文件生成测试 |
| 系统调试 | `Use plugin: trae-remote-official:superpowers` (systematic-debugging) | 系统化调试 |
| 代码审查 | `Use plugin: trae-remote-official:coderabbit` | AI代码审查 |
| HOTL代码审查 | `Use plugin: trae-remote-official:hotl` (code-review) | 对照HOTL合约审查 |
| 浏览器自动化 | `Use Skill: agent-browser` | SkillHub/ClawHub平台操作 |
| 浏览器调试 | `Use plugin: trae-remote-official:chrome-devtools` | 前端检查/网络请求 |
| 网页内容提取 | `Use Skill: defuddle` | 提取网页clean markdown |
| UI/Dashboard设计 | `Use plugin: trae-remote-official:stark` | Web界面设计 |
| AI产品构建 | `Use plugin: trae-remote-official:runtype-skills` | AI产品构建 |
| 工程决策 | `Use plugin: trae-remote-official:staff-engineer-mode` | 跨生命周期工程决策 |
| 完成验证 | `Use plugin: trae-remote-official:superpowers` (verification-before-completion) | 声称完成前必须验证 |
| Git分支完成 | `Use plugin: trae-remote-official:superpowers` (finishing-a-development-branch) | 决定merge/PR/cleanup |
| TRAE反馈 | `Use Skill: feedback` | 提交TRAE产品反馈 |

---

## 内容质量检测与修复系统(v3.2)使用指南

### 检查所有skill内容质量
```bash
python tools/skill_batch_upgrader_v3.py content-check
```
输出报告到 `data/reports/content_quality_report.json`

### 批量修复内容质量
```bash
python tools/skill_batch_upgrader_v3.py content-fix
```
自动修复: summary去重, description去重, body去重, 模板清理, 占位符清理, 章节换行, 输入表补充

### 修复指定skill
```bash
python tools/skill_batch_upgrader_v3.py content-fix --slug <slug>
```

### 修复问题最多的N个skill
```bash
python tools/skill_batch_upgrader_v3.py content-fix --top 50
```

### 独立skill升级完整流程
```bash
# 仅检测+修复(不上传平台)
python tools/version_sync_pipeline.py upgrade <slug> --skip-platforms

# 完整升级(检测+修复+多平台同步)
python tools/version_sync_pipeline.py upgrade <slug>

# 强制同步(即使内容质量未完全通过)
python tools/version_sync_pipeline.py upgrade <slug> --force
```

### 7项内容质量检查
| 检查项 | 检查ID | 说明 |
|--------|--------|------|
| summary无重复 | dup_summary | 前后半段重复或连续重复短语 |
| description无重复 | dup_description | 重复句子或前后重复 |
| 无模板化套话 | template_content | "按照skill规范执行"等批量生成套话 |
| 无占位符内容 | placeholder_content | "根据实际场景填充"等占位符 |
| body无重复句子 | dup_sentences | body中20字符以上的重复句子 |
| 章节无错误合并 | section_merging | ### 标题直接跟在上一行末尾 |
| 输入格式表非空 | empty_input_table | 只有表头没有数据行 |

---

## 验证检查清单

- [ ] Git推送成功(origin + hermes-skills)
- [ ] 批量重传已修复skill到SkillHub
- [ ] L1合规修复(至少ws-agent-browser通过)
- [ ] 所有权认领: 确认2172个skill在本团队名下
- [ ] 搜索排名: 分析排名算法，制定优化策略
- [ ] JSON与DB统一: 设计并实施统一方案
- [ ] ClawHub pending(1184个)开始上传
- [ ] 剩余17个空输入表skill已处理
- [ ] pricing表schema对齐
- [ ] FTS表已填充
- [ ] dependencies表有记录
- [ ] 内容质量监控机制建立(新skill入库时自动检查)
- [ ] 定期清理机制建立
- [ ] Git提交并推送到双远程仓库
- [ ] 下一轮提示词v66.0生成
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
21. **L1.5门禁** — 内容质量检查必须在L1合规通过后、L2 LLM验证前执行
22. **升级流程** — upgrade_single_skill必须按6步流程执行:查找→检测→修复→验证→L1→同步

---

## 关键API参考

### SkillHub Star API
```
POST /api/v1/skills/{slug}/star
Body: {}
Response: {"alreadyStarred": false, "ok": true, "starred": true}
```

### SkillHub 状态查询
```
GET /api/v1/orgs/862/admin/skills?status=published&page=1&pageSize=100
```

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
d:\skills\tools\db.py                           — 数据库模块
d:\skills\tools\enterprise_uploader.py           — SkillHub企业版上传
d:\skills\tools\version_sync_pipeline.py         — 版本同步流水线(含upgrade命令)
d:\skills\tools\skill_batch_upgrader_v3.py       — 批量升级工具(含content-check/content-fix)
d:\skills\tools\clawhub_batch_uploader.py       — ClawHub批量上传
d:\skills\config\project_config.py             — 平台配置
d:\skills\data\upload_tracking.json             — 上传追踪JSON
d:\skills\data\category_mapping.json            — 分类映射
d:\skills\data\reports\content_quality_report.json — 内容质量报告
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

完成本轮任务后，生成 `next-round-prompt-v66.0.md`，格式参考本文档，包含:
1. 本轮完成总结(表格)
2. 平台当前状态
3. 实施任务(按优先级)
4. 技能/插件使用指南
5. 验证检查清单
6. 约束条件
