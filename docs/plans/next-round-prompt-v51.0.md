# 第51轮提示词 (v51.0) — SkillHub前台发布执行 + 平台状态对齐 + 缺失skill补全 + 源skill扩展

> **日期**: 2026-07-25
> **上一轮完成**: V50 — hermes-skills仓库重构(14分类+759免费+459付费) + GitHub双仓库推送成功 + 全层级100%A级维持
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库
> **最高优先级**: 💰 SkillHub前台可见性 — 做出来是为了引流和赚钱的

## V50完成总结

| 任务 | 状态 | 结果 |
|------|------|------|
| hermes-skills仓库重构 | ✅ | 14分类目录 + free/paid子目录 + 三语README |
| 付费skill添加到hermes-skills | ✅ | 459个付费skill复制到hermes-skills/[category]/paid/ |
| platform_config付费策略 | ✅ | push_paid=True, paid_strategy=clawhub_aligned |
| version_sync_pipeline多平台同步 | ✅ | 支持免费+付费推送到hermes-skills |
| 数据库重建 | ✅ | 2882 skills (free:1675, paid:599, source:600, tool:8) |
| 14标准分类统一 | ✅ | 所有skill使用14个标准category |
| GitHub双仓库推送 | ✅ | origin: 159f8276f..564d0938a, hermes-skills: 7b0a18c56..564d0938a |
| 全层级审计 | ✅ | L4-L9 全部100%A级 (2097 skills) |

### hermes-skills仓库最终状态

| 分类 | 免费skill | 付费skill | 合计 |
|------|----------|----------|------|
| Agents | 20 | 27 | 47 |
| Automation | 20 | 238 | 258 |
| Communication | 56 | 12 | 68 |
| Creative | 124 | 47 | 171 |
| Development | 194 | 35 | 229 |
| Finance | 34 | 10 | 44 |
| Integrations | 5 | 0 | 5 |
| Knowledge | 50 | 49 | 99 |
| Lifestyle | 12 | 0 | 12 |
| Operations | 41 | 17 | 58 |
| Other | 0 | 0 | 0 |
| Productivity | 69 | 2 | 71 |
| Research | 87 | 3 | 90 |
| Security | 47 | 19 | 66 |
| **合计** | **759** | **459** | **1218** |

### 审计最终结果 — 全部100%A级

| 审计层 | A级 | B级 | C级 | 平均分 | 通过率 |
|--------|-----|-----|-----|--------|--------|
| L4 功能质量 | 2097 | 0 | 0 | 93.7 | 100% |
| L5 可销售性 | 2097 | 0 | 0 | 90.4 | 100% |
| L6 内容真实性 | 2097 | 0 | 0 | 100.0 | 100% |
| L7a 语义模板 | 2097 | 0 | 0 | 100.0 | 100% |
| L7b 可执行性 | 2097 | 0 | 0 | 100.0 | 100% |
| L8 安全审计 | 2097 | 0 | 0 | 100.0 | 100% |
| L9 可见性质量 | 2097 | 0 | 0 | 100.0 | 100% |

### 平台状态 (upload_tracking.json)

| 平台 | 成功 | 待处理 | 失败/拒绝 |
|------|------|--------|----------|
| SkillHub | 2036 (本地标记) | 2 pending + 17 platform_review | 20 rejected + 9 deleted |
| ClawHub | 228 published | 704 not_uploaded | 1153 not_eligible |
| Community | 4032 published | — | 40 failed |
| Hermes | 759 eligible (仅免费) → 现含459付费 | 1326 not_eligible (待更新) | — |

### 定时任务

| 任务 | ID | 状态 | 频率 | 说明 |
|------|----|------|------|------|
| ClawHub每日批量上传 | 73efabe0 | Active | 每日04:00 UTC (12:00北京) | 200条/天 |
| JueJin每日Bug扫描 | 0e578864 | Paused | 每日09:00 | 已暂停 |

### SkillHub可见性根因 (仍未解决)

| 根因 | 证据 | 影响 |
|------|------|------|
| CLI无publish命令 | v0.4.1仅支持install/search/list/config | 无法通过CLI上传skill |
| 数据库标记≠平台状态 | 1120条success记录是V45本地DB设置 | DB状态不代表平台状态 |
| download_ready全NULL | 1120条记录download_ready均为NULL | 从未验证平台是否处理了版本 |
| 实际搜索验证失败 | `npx skillhub search`找不到我们的skill | 确认前台不可见 |

## 实施任务

### 任务1: SkillHub前台发布执行 (最高优先级 — 引流和赚钱的关键)

**问题**: SkillHub前台完全看不到我们的skill。1120条"success"和2036条"published"均为本地DB标记，从未真正上传到SkillHub平台。

**根因**: CLI无publish命令，需要通过浏览器Admin API发布。

**执行方案**:
1. 确认用户已登录 https://www.skillhub.cn
2. 使用浏览器MCP工具打开 https://www.skillhub.cn/admin
3. 在浏览器控制台执行 `tools/community_publish.js`
4. 脚本自动:
   - 获取所有skill列表（含visibility/download_ready/namespace信息）
   - 生成可见性诊断报告
   - 筛选 org_only + NULL visibility 的skill
   - 批量调用 `POST /admin/skills/{slug}/publish-to-community` API
   - 处理slug冲突（自动追加-sk后缀）
5. 执行后复制结果: `JSON.stringify(window.__publishResults)`
6. 更新数据库 platform_uploads 表和 upload_tracking.json
7. **验证**: 在 SkillHub 前台搜索关键词，确认skill可见

**优先发布顺序**: P0(8零依赖) → P1(5获奖) → P2(3已获奖) → P3(12变现) → P4+P5(32开源改造)

**验证标准**: 至少10个skill在SkillHub前台可搜索到

### 任务2: SkillHub 8个retry_pending技能重试

**技能列表**:
1. cdp-browser-master
2. cron-guard
3. linear-workflow-bot
4. ai-artist-workstation
5. sales-copy-writer
6. accounting-and-finance
7. accounting-finance
8. ace-music

**执行方案**:
1. 检查每个skill的SKILL.md是否通过L1-L9审计（已100%A级）
2. 通过浏览器Admin API重新上传这些skill
3. 更新 platform_uploads 表状态从 retry_pending → success/rejected
4. 更新 upload_tracking.json

**验证**: retry_pending从8降至0（或记录新的失败原因）

### 任务3: 平台上传状态同步 — upload_tracking.json与DB对齐

**问题**: upload_tracking.json中的状态可能与平台实际状态不一致，hermes_eligible仍为759（未包含新增的459付费skill）。

**执行方案**:
1. 更新 upload_tracking.json 中 hermes 相关统计:
   - hermes_eligible: 759 → 1218 (759免费 + 459付费)
   - hermes_not_eligible: 1326 → 867 (1326 - 459已添加)
2. 从SkillHub API获取实际skill状态（如可通过浏览器访问）
3. 从ClawHub API获取实际skill状态
4. 更新 upload_tracking.json 中的 status 和 visibility 字段
5. 更新数据库 platform_uploads 表

**验证**: upload_tracking.json hermes_eligible=1218, hermes_not_eligible=867

### 任务4: 53个缺失付费skill调查与补全

**问题**: 599个付费skill中，53个因源目录不存在被跳过，未添加到hermes-skills。

**执行方案**:
1. 从数据库查询53个缺失skill的slug和local_path
2. 检查local_path是否存在（可能目录名不同或已移动）
3. 在 differentiated-skills/ 中搜索 -pro 后缀的变体
4. 对于找到的skill，复制到 hermes-skills/[category]/paid/
5. 对于确实找不到的，在数据库中标记为 source_missing

**验证**: 53个缺失skill要么补全到hermes-skills，要么标记为source_missing

### 任务5: ClawHub上传监控与状态验证

**问题**: ClawHub有704个not_uploaded技能，定时任务（ID: 73efabe0）应每日上传200条。

**执行方案**:
1. 检查定时任务最近执行状态（通过Schedule get）
2. 从数据库查询ClawHub最新上传记录
3. 计算704个not_uploaded中已上传的数量
4. 验证VERSION_EXISTS和protected namespace错误处理
5. 如果定时任务未正常运行，诊断并修复

**验证**: ClawHub published数量从228逐步增长

### 任务6: 源skill发现与扩展 — 从多平台获取新skill

**问题**: 用户要求skill来源不仅限于clawhub，还应从hermes、dify、n8n、GitHub高星项目提取。

**执行方案**:
1. 检查 `config/platform_config.py` 中的 GITHUB_SCAN_REPOS 列表
2. 运行 `tools/auto_discover.py` 或 `tools/multi_source_discover.py` 发现新skill
3. 从以下来源获取:
   - GitHub: anthropics/skills, obra/superpowers, 12-factor-agents, langgraph, crewAI, autogen等
   - Dify: 检查dify项目中的skill定义
   - n8n: 检查n8n workflow中的可提取skill
   - Hermes: 检查hermes-skills生态
4. 将新发现的skill添加到 clawhub-skills/downloaded/ 并录入数据库
5. 运行差异化流程生成免费版和付费版

**验证**: 数据库source skills从600增长至650+

### 任务7: hermes-skills README更新 — 反映实际付费skill数量

**问题**: hermes-skills的三语README可能未反映新增的459个付费skill。

**执行方案**:
1. 读取 hermes-skills/README.md, README.zh-CN.md, README.zh-TW.md, README.en.md
2. 更新统计数据:
   - 总skill数: 759 → 1218
   - 免费skill: 759
   - 付费skill: 459 (新增)
3. 更新各分类的skill数量表
4. 添加付费skill说明（保持proprietary license，与clawhub付费版一致）
5. 提交并推送到hermes-skills仓库

**验证**: 三语README统计数据与实际目录内容一致

### 任务8: Git提交与下一轮提示词生成

**执行方案**:
1. 提交所有变更到本地git
2. 推送到origin (私有备份) 和 hermes-skills (公开引流)
3. 生成 next-round-prompt-v52.0.md
4. 更新 ARCHITECTURE.md 中的平台策略表（hermes-skills现在含付费skill）

## 验证检查清单

- [ ] SkillHub浏览器发布验证(至少10个skill前台可搜索)
- [ ] SkillHub 8个retry_pending技能全部重试
- [ ] upload_tracking.json hermes_eligible更新为1218
- [ ] 53个缺失付费skill调查完成
- [ ] ClawHub定时任务正常运行验证
- [ ] 源skill发现扩展（新增50+）
- [ ] hermes-skills三语README更新
- [ ] Git提交并推送到双仓库
- [ ] 下一轮提示词v52.0生成

## 约束

1. **增强已有代码** — 所有修复功能集成到现有工具脚本，不创建碎片化新文件
2. **不模拟/mock** — 所有文件修改和数据库操作必须真实执行
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏现有命令功能
5. **内容保真** — tags增强和value proposition增强不得改变技能原有语义和功能
6. **网络容错** — GitHub推送失败不应阻塞其他任务的执行
7. **质量底线** — 不得引入任何会降低L4-L9审计等级的修改(当前100%A级)
8. **付费skill保护** — hermes-skills中的付费skill应与clawhub付费版一致，不得将全部付费skill开源
9. **分类统一** — 本地分类目录=skillhub分类=clawhub分类=hermes-skills分类
10. **版本同步** — 本地skill版本升级后，必须同步到全部3个平台的对应skill
11. **SkillHub优先** — SkillHub前台可见性是最高优先级，因为做出来是为了引流和赚钱的
