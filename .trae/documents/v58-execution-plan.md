# V58 实施计划：企业Cookie + 非破坏性分类 + 批量操作 + V59提示词

## 摘要

执行 `next-round-prompt-v58.0.md` 的7项任务。核心创新：**推翻V57"PUT API不可用"的未验证假设**，在执行任何DELETE操作前，先验证非破坏性分类修复方法（PATCH/PUT元数据更新）。用户明确要求：用agent-browser获取企业团队Cookie，且需调查已上传skill能否通过升级/修改方式归类而非DELETE重传。

## 当前状态分析

### V56/V57 复核结果（已验证完成，commit 26f460436）

| 修复项 | 文件 | 验证状态 |
|--------|------|---------|
| categoryIds字段 | `enterprise_uploader.py:448` | ✅ `'categoryIds': [team_category_id]` |
| TEAM_CATEGORY_IDS常量 | `enterprise_uploader.py:43-54` | ✅ 10个团队分类ID |
| get_team_category_id() | `enterprise_uploader.py:150-168` | ✅ platform→team→数字ID |
| update_mechanism.py categoryIds | `update_mechanism.py:539` | ✅ 从`[]`改为`[team_cat_id]` |
| batch_field_fix.py 6命令 | `batch_field_fix.py` | ✅ check-auth/reupload-all-batch等 |
| description优化 | 全部1144个skill | ✅ 1144/1144 >= 150字符 |
| 5个VPN skill转型 | 网络安全诊断工具 | ✅ body内容清洁，license=MIT |

### V58 阻断项

- `~/.skillhub_cookies.txt` 仅112字节（个人session），Admin API返回"enterprise authentication required"
- 7个未提交文件（3个新skill + 3个修改的工具 + 1个报告），与V58无直接关联

### 关键发现：V57核心假设存疑

V57计划中"因PUT API不可用，必须DELETE+重传"的结论**未经代码验证**。代码级证据表明PATCH/PUT已用于其他端点：

| 端点 | 方法 | 状态 | 证据 |
|------|------|------|------|
| `/orgs/{ORG_ID}/admin/skills/{slug}/visibility` | PATCH | ✅ 已验证可用 | `batch_field_fix.py:372-374` |
| `/orgs/{ORG_ID}/admin/skills/{slug}/rename-slug` | PUT | ✅ 已验证可用 | `community_publish.js:61-66` |
| `/orgs/{ORG_ID}/admin/skills/{slug}` | PATCH/PUT? | ❓ 未测试 | REST惯例推断极可能支持 |

**结论**：既然PATCH已用于visibility、PUT已用于rename-slug，对基础资源`/admin/skills/{slug}`执行PATCH/PUT更新categoryIds/tags/summary_zh/iconUrl**极大概率可行**。DELETE+重传应作为最后手段。

## 提议的变更

### Phase 1: Agent-browser 获取企业团队Cookie（P0阻断项）

**目标**：获取企业团队版Cookie，解除所有API操作阻断

**步骤**：
1. 使用 `agent-browser` skill 导航到 `https://www.skillhub.cn`
2. `browser_snapshot` 检测登录状态（登录按钮 vs 用户头像/企业标识）
3. 导航到 `https://www.skillhub.cn/enterprise/org-xxo535hs` 验证企业团队身份
4. 导航到 `https://www.skillhub.cn/admin/skills` 验证Admin权限
5. 使用 `browser_evaluate` 执行 `document.cookie` 提取完整cookie
6. 写入 `~/.skillhub_cookies.txt`
7. 验证：`python batch_field_fix.py check-auth` 返回 `✅ 认证成功`

**失败处理**：
- 个人账号登录 → 提示用户切换企业团队账号
- Cookie不完整 → 用browser DevTools Application→Cookies面板补充
- check-auth仍失败 → 用户需先访问企业管理后台激活企业session

### Phase 2: 非破坏性分类方法调研（核心 — 用户关键关切）

**目标**：在DELETE前验证是否存在非破坏性分类修复方法

**方法A：PATCH/PUT 元数据更新（最高优先级）**

依据：`PATCH /admin/skills/{slug}/visibility` 已验证可用。

测试方案（选1个已上传skill作样本）：
1. GET `/api/v1/skills/{slug}` 获取当前字段（基线）
2. PATCH `/orgs/{ORG_ID}/admin/skills/{slug}` 发送 `{categoryIds, tags, summary_zh, iconUrl}`
3. 若PATCH失败(405)，尝试PUT同端点
4. 重新GET验证字段是否更新

判定：HTTP 200 + 字段更新 → **Path A可行**

**方法B：版本升级方式（POST新版本携带categoryIds）**

测试 `POST /orgs/{ORG_ID}/admin/skills/{slug}/versions`（不DELETE旧版本，直接POST新版本携带categoryIds）。

判定：HTTP 200/201 + 新版本创建 → **Path A可行**

**方法C：Admin UI API观察（使用agent-browser）**

1. agent-browser导航到 `https://www.skillhub.cn/admin/skills`
2. 点击编辑某skill的分类
3. `browser_network_requests` 捕获前端发出的API请求
4. 分析请求方法/URL/body，直接揭示前端使用的元数据更新API

判定：发现可用端点 → **Path A可行**

**路径选择**：
```
方法A(PATCH/PUT) → 成功 → Path A
     │失败
方法B(POST版本) → 成功 → Path A
     │失败
方法C(观察UI) → 发现 → Path A
     │未发现
Path B: DELETE+重传（最后手段）
```

### Phase 3: 执行分类修复

**Path A（优先）：非破坏性批量更新**

在 `batch_field_fix.py` 中新增命令（遵循"增强已有代码"原则）：
- `test-metadata-patch <slug>`：单skill测试PATCH
- `update-metadata-batch`：批量PATCH/PUT更新994个skill的categoryIds/tags/summary_zh/iconUrl

复用 `enterprise_uploader.py` 的函数生成payload：
- `get_platform_category()` → `get_team_category_id()` → categoryIds
- `parse_tags()` → tags
- `generate_summary_zh()` → summary_zh
- `CATEGORY_ICONS` → iconUrl

每个skill间隔1秒（PATCH比POST轻量），支持断点续传，**不触发新审核，不丢失downloads/stars**。

**Path B（兜底）：DELETE + 重传**

仅当Phase 2三种方法全部失败时执行：
- `python batch_field_fix.py reupload-all-batch`
- DELETE → POST重传，间隔2秒，断点续传
- 接受downloads/stars数据损失（记录为已知限制）
- 重传后触发新审核

### Phase 4: 批量操作

**4.1 批量审核2,706个待审版本**
```bash
python batch_field_fix.py gen-approve-js
```
在浏览器 `/admin/skill-reviews` 控制台执行生成的JS脚本。若已有 `batch_approve_v3.js`（支持自动翻页+进度持久化），优先使用v3。

验证：剩余待审核 < 50，抽样10个skill前台可搜索。

**4.2 DELETE+重传38个被拒skill**
```bash
python batch_field_fix.py reupload-rejected
```
38个被拒slug列表在 `batch_field_fix.py:49-62`，使用修复后的enterprise_uploader.py。

**4.3 发布4个org_only skill**
```bash
python batch_field_fix.py publish-org-only
```
使用已验证的 `PATCH /admin/skills/{slug}/visibility` 端点。4个slug：`ai-artist-workstation-pro`, `clickhouse-olap-expert`, `requirement-explorer-pro`, `lead-research-hunter`。

**4.4 重传memory-orchestrator-sk**
```bash
python batch_field_fix.py reupload-deleted
```

**执行顺序**：
```
Phase 1 (Cookie) → Phase 2 (调研) → Phase 3 (Path A/B分类修复)
                                    ↓
Phase 4.1 (审核2706) ── 需Phase 1 ──┐
Phase 4.2 (重传38被拒) ── 需Phase 1 ─┤
Phase 4.3 (发布4 org_only) ── 需Phase 1 ├→ Phase 5 (Git+V59)
Phase 4.4 (重传memory) ── 需Phase 1 ─┘
```

注意：若Path B执行（重传触发新审核），建议先完成4.1审核现有2706个，再执行Path B。

### Phase 5: Git提交与V59提示词

**5.1 Git提交**
```bash
cd D:\skills
git add -A
git commit -m "fix: V58 — 企业Cookie + 非破坏性分类修复 + 批量审核2706 + 重传38被拒 + 发布4 org_only + V59提示词"
git push origin master
git push hermes-skills master
```

**5.2 生成 next-round-prompt-v59.0.md**

聚焦剩余12大因素问题：
- **P1: DisplayName中文化**（因素11，40%英文→100%中文）— 若Path A可行，用PATCH批量更新
- **P1: Verified认证申请**（因素6，Score=0）— 调研SkillHub企业认证申请流程
- **P2: downloads/stars积累策略**（因素4/5）— Path A保留数据则制定增长策略；Path B则重新积累
- **P2: 所有权认领** — 调研SkillHub skill所有权认领机制

## 插件使用计划

| 插件 | 用途 | 使用阶段 |
|------|------|---------|
| staff-engineer-mode | API调研策略决策、数据损失权衡 | Phase 2/3 |
| superpowers:systematic-debugging | API端点测试排查 | Phase 2 |
| superpowers:verification-before-completion | 验证分类修复生效、数据未丢失 | Phase 3/4 |
| hotl:executing-plans | 结构化执行带检查点 | 全流程 |
| hotl:verification-before-completion | 每Phase完成前验证门禁 | 各Phase |
| tailtest | 为新增update-metadata-batch命令生成测试 | Phase 3 |
| frontend-design / stark | 理解Admin UI前端结构发现API端点 | Phase 2方法C |

## 假设与决策

1. **PATCH/PUT可用性假设**：基于visibility端点PATCH已验证、rename-slug端点PUT已验证，推断基础资源PATCH/PUT极可能可用。若不可用，Path B兜底。
2. **非破坏性优先原则**：DELETE+重传会导致downloads/stars数据损失，必须先验证非破坏性方法。这是用户明确要求。
3. **增强已有代码**：所有新功能（test-metadata-patch, update-metadata-batch）集成到batch_field_fix.py，不创建碎片化新文件。
4. **Cookie获取方式**：优先用agent-browser自动检测，失败时提供手动导出指南。
5. **断点续传**：所有批量操作支持从报告文件恢复进度。
6. **不模拟/mock**：所有操作真实执行，API测试用真实skill样本。

## 验证步骤

### Phase 1 验证
- `python batch_field_fix.py check-auth` 返回 `✅ 认证成功! Skill总数: XXXX`
- Cookie文件 > 200字节

### Phase 2 验证
- 方法A/B/C测试结果记录
- Path A/B决策明确记录

### Phase 3 验证
- **Path A**：抽样10个skill GET检查 categoryIds/iconUrl/summary_zh/tags 正确
- **Path A**：downloads/stars数据未丢失
- **Path B**：994个skill重传成功（断点续传）
- `/admin/skills/categories` 分类不再为0

### Phase 4 验证
- 2,706个待审版本批量审核通过（剩余<50）
- 38个被拒skill DELETE并重新上传成功
- 4个org_only skill切换为public
- memory-orchestrator-sk重新上传成功
- 抽样10个skill在前台可搜索

### Phase 5 验证
- Git提交并推送（origin + hermes-skills）
- `next-round-prompt-v59.0.md` 生成
- V59包含DisplayName中文化、Verified认证、downloads/stars策略

## 任务执行顺序

```
Phase 1 (Cookie获取) ─────────────────────────────┐
                                                   │
Phase 2 (非破坏性调研) ── 需Phase 1 ───────────────┤
                                                   │
Phase 3 (分类修复 Path A/B) ── 需Phase 2结论 ──────┤
   Path A: 无需重新审核                             │
   Path B: 触发新审核 ─────────────────────────────┤
                                                   │
Phase 4.1 (审核2706) ── 需Phase 1 ─────────────────┤
Phase 4.2 (重传38被拒) ── 需Phase 1 ───────────────┼──→ Phase 5 (Git+V59)
Phase 4.3 (发布4 org_only) ── 需Phase 1 ───────────┤
Phase 4.4 (重传memory) ── 需Phase 1 ───────────────┘
```
