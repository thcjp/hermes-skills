# skill-registry.db 数据质量审计报告

| 项目 | 内容 |
|------|------|
| 数据库 | `d:\skills\skill-registry.db` |
| 审计时间 | 2026-07-27 21:45 |
| 访问模式 | 只读 (SQLite `mode=ro`,未对数据库做任何修改) |
| 审计范围 | skills 主表(3495 行)+ skills_fts 全文检索表 + 关联表 |
| 审计脚本 | `audit_skill_registry.py` |

---

## 审计结论速览(Executive Summary)

本次审计共扫描 **3495** 个 skill。整体数据结构完整,核心标识字段(slug / display_name / category / pricing_tier / is_paid)零空值,但存在 **多项可能导致平台封禁的高风险问题**:

| 风险等级 | 问题 | 影响范围 |
|----------|------|----------|
| 极高 | slug 含程序化后缀(`-sk`/`-v2` 等) | 677 个 (19.37%) |
| 极高 | is_paid 与 pricing_tier 定价矛盾 | 767 个 (21.95%) |
| 高 | slug 长度 < 8 字符(通用词抢占) | 140 个 (4.01%) |
| 高 | description 含模板套话(一键/帮助你等) | 33 个 (0.94%) |
| 高 | description 字段与 summary 完全重复且硬截断 100 字符 | 3349 个 (95.82%) |
| 中 | content_hash 为空 | 738 个 (21.12%) |
| 中 | description/summary 为空 | 146 个 (4.18%) |
| 中 | 重复 content_hash | 788 组 / 1576 行 (45.09%) |
| 中 | 重复 display_name(营销命名冲突) | 1098 组 / 2286 行 (65.41%) |
| 关注 | 处于 pending 上传状态且 100% 不合规 | 1439 个 |

**最关键发现**:`description` 字段在 FTS 表中是 `summary` 的逐字副本(100% 相同),最大长度被硬截断在 100 字符。若平台要求 150–280 字符的营销描述,则 **没有任何一个 skill 满足要求**,这是系统性字段缺失,而非个别质量问题。

---

## 0. FTS 关联验证

| 检查项 | 结果 |
|--------|------|
| skills 表总行数 | 3495 |
| skills_fts 总行数 | 3495 |
| 按 `s.id = f.rowid` 关联数 | 3495(完全匹配) |
| 按 `s.slug = f.slug` 关联数 | 3495(完全匹配) |

结论:FTS 表与主表一一对应,采用 `s.id = f.rowid` 关联获取 `description`/`tags` 字段,数据可靠。

---

## 1. 基本信息统计

### 1.1 总 skill 数
**3495**

### 1.2 按 current_status 分布

| current_status | 数量 | 占比 |
|----------------|-----:|-----:|
| local_only | 1691 | 48.38% |
| deleted_on_skillhub | 1655 | 47.35% |
| synced_from_skillhub | 96 | 2.75% |
| differentiated | 32 | 0.92% |
| deleted | 17 | 0.49% |
| pending_upload | 4 | 0.11% |

> 说明:近半数(47.35%)skill 已在 skillhub 上被删除,48.38% 仅本地存在。真正在线(synced)的占比很低(2.75%)。

### 1.3 按 source 分布

| source | 数量 | 占比 |
|--------|-----:|-----:|
| clawhub_differentiated | 949 | 27.15% |
| differentiated | 790 | 22.60% |
| clawhub_download | 597 | 17.08% |
| skillhub_sync | 580 | 16.60% |
| clawhub | 298 | 8.53% |
| packaged | 166 | 4.75% |
| opensource_modified | 39 | 1.12% |
| finance_differentiate | 32 | 0.92% |
| original_creation | 23 | 0.66% |
| clawhub_downloaded | 8 | 0.23% |
| manual | 8 | 0.23% |
| hermes | 3 | 0.09% |
| e2e_test | 1 | 0.03% |
| opensource | 1 | 0.03% |

### 1.4 按 category 分布

| category | 数量 | 占比 |
|----------|-----:|-----:|
| Development | 873 | 24.98% |
| Automation | 538 | 15.39% |
| Other | 507 | 14.51% |
| Security | 241 | 6.90% |
| Creative | 238 | 6.81% |
| Research | 225 | 6.44% |
| Productivity | 200 | 5.72% |
| Finance | 195 | 5.58% |
| Operations | 182 | 5.21% |
| Knowledge | 108 | 3.09% |
| Agents | 78 | 2.23% |
| Communication | 49 | 1.40% |
| Lifestyle | 31 | 0.89% |
| Integrations | 30 | 0.86% |

> 风险提示:`Other` 占 14.51%(507 个),分类不够精细,可能影响平台检索与归类。

---

## 2. 字段完整性检查

### 2.1 skills 表字段空值统计

| 检查项 | 空值数量 | 占比 | 风险 |
|--------|---------:|-----:|------|
| slug 为空或NULL | 0 | 0.00% | 无 |
| current_display_name 为空或NULL | 0 | 0.00% | 无 |
| summary 为空或NULL | 146 | 4.18% | 中 |
| pricing_tier 为空或NULL | 0 | 0.00% | 无 |
| is_paid 为NULL | 0 | 0.00% | 无 |
| content_hash 为空或NULL | 738 | 21.12% | 中 |
| current_name 为空或NULL | 0 | 0.00% | 无 |
| category 为空或NULL | 0 | 0.00% | 无 |
| local_path 为空或NULL | 0 | 0.00% | 无 |

### 2.2 description 为空或NULL(来自 skills_fts)

| 指标 | 数量 | 占比 |
|------|-----:|-----:|
| description 为空或NULL | 146 | 4.18% |
| description 非空 | 3349 | 95.82% |

### 2.3 tags 为空或NULL(来自 skills_fts)

| 指标 | 数量 | 占比 |
|------|-----:|-----:|
| tags 为空或NULL | 0 | 0.00% |

> 标签字段 100% 填充,完整性良好。

---

## 3. 质量风险检查

### 3.1 description 包含模板套话的 skill

检测关键词:`本技能` / `本工具` / `帮助你` / `强大的` / `高效的` / `智能的` / `一键` / `轻松`

| 关键词 | 命中数 | 占比 |
|--------|-------:|-----:|
| 本技能 | 0 | 0.00% |
| 本工具 | 1 | 0.03% |
| 帮助你 | 2 | 0.06% |
| 强大的 | 0 | 0.00% |
| 高效的 | 0 | 0.00% |
| 智能的 | 0 | 0.00% |
| 一键 | 30 | 0.86% |
| 轻松 | 0 | 0.00% |
| **至少命中一个(去重)** | **33** | **0.94%** |

**风险评估:高**。`一键` 是主要违规词(30 个),这类营销套话易被平台判定为低质/刷量内容,存在封禁风险。命中示例:
- `ai-image-gen`: "...Gemini Flash Image一键生成4K商用图..."
- `bilibili-helper`: "...B站运营助手一键生成5个标题方案..."
- `bizauto-flow-free`: "...业务自动化师免费版帮助你将重复性业务流程..."

### 3.2 description 长度异常(长度 < 150 或 > 280)

| 区间 | 数量 | 占比 | 风险 |
|------|-----:|-----:|------|
| 长度 < 150 | 3349 | 95.82% | 高 |
| 长度 > 280 | 0 | 0.00% | 无 |
| 长度 150–280(合规) | 0 | 0.00% | — |
| 为空 | 146 | 4.18% | 中 |

**description 长度分布直方**:

| 区间 | 数量 | 占比示意 |
|------|-----:|:---|
| 空 | 146 | ## |
| 1–50 | 2169 | ############################### |
| 51–100 | 1180 | ################ |
| 101–149 | 0 | |
| 150–200 | 0 | |
| 201–280 | 0 | |
| 281–400 | 0 | |
| 401+ | 0 | |

**关键发现**:description 最大长度 = **100 字符**,平均 51.38 字符,在 100 字符处存在硬截断,101+ 完全为空。详见第 8 节根因分析。

### 3.3 summary 长度 > 100 字符的 skill

| 指标 | 数量 | 占比 |
|------|-----:|-----:|
| summary 长度 > 100 | 0 | 0.00% |
| summary 为空 | 146 | 4.18% |
| summary 长度合规(≤100) | 3349 | 95.82% |

> summary 在 100 字符处同样硬截断(与 description 一致),详见第 8 节。

### 3.4 slug 包含程序化后缀

检测后缀:`-v2` / `-v3` / `-plus` / `-max` / `-elite` / `-sk` / `-sk1` / `-sk2` / `-sk3`

| 后缀 | 命中数 |
|------|-------:|
| -v2 | 22 |
| -v3 | 4 |
| -plus | 4 |
| -max | 3 |
| -elite | 3 |
| -sk | 649 |
| -sk1 / -sk2 / -sk3 | 0 |
| **至少含一个后缀(去重)** | **677 (19.37%)** |

**风险评估:极高(封禁风险)**。`-sk` 后缀占 649 个,是程序化批量生成的典型特征,极易被平台识别为机器刷量/抢占命名空间而封禁。建议全部重命名为语义化 slug。

### 3.5 slug 长度 < 8 字符(通用词抢占风险)

| 指标 | 数量 | 占比 |
|------|-----:|-----:|
| slug 长度 < 8 | 140 | 4.01% |

**风险评估:高**。抢占通用短词(如 `ui`/`ux`/`go`/`api`/`pdf`/`aws`/`git`/`sql`/`css`/`json` 等)易被判定为恶意抢占命名空间。示例(节选):
`ui`, `ux`, `go`, `db`, `py`, `dns`, `git`, `ssl`, `web`, `api`, `csv`, `sql`, `vue`, `pdf`, `aws`, `k8s`, `css`, `xml`, `vpn`, `cron`, `logo`, `code`, `test`, `json`, `game` ...

---

## 4. 定价一致性检查

### 4.1 is_paid=1 但 pricing_tier=L1(矛盾)

| 指标 | 数量 | 占比 |
|------|-----:|-----:|
| is_paid=1 且 pricing_tier=L1 | 108 | 3.09% |

**风险评估:中**。付费 skill 却标注最低档 L1,定价逻辑自相矛盾。示例:
`evolution-engine-v2`, `memory-distiller-v2`, `netdisk-sync-pro`, `neurocache-pro`, `redis-cache-master`, `cron-scheduler-pro`, `aws-cloud-inspector`, `excel-ninja`, `cron-scheduler-pro-paid` ...

### 4.2 is_paid=0 但 pricing_tier=L3/L4(矛盾)

| 指标 | 数量 | 占比 |
|------|-----:|-----:|
| is_paid=0 且 pricing_tier=L3/L4 | 659 | 18.86% |

**风险评估:高**。免费 skill 却标注中高付费档(L3/L4),占比近两成,定价体系严重不一致。示例:
`admapix`, `ai-agent-helper`, `aws-agentcore-langgraph`, `azure-infra`, `neosoul-decision-agent`, `browser-automation-cdp`, `cloud-infra-automation`, `email-gmail-outlook`, `feishu-card` ...

### 4.3 pricing_tier 分布统计

| pricing_tier | 数量 | 占比 |
|--------------|-----:|-----:|
| L1 | 1147 | 32.82% |
| L2 | 1089 | 31.16% |
| L3 | 1018 | 29.13% |
| L4 | 237 | 6.78% |
| L5 | 4 | 0.11% |

### 4.4 is_paid 分布统计

| is_paid | 数量 | 占比 |
|---------|-----:|-----:|
| 0(免费) | 2270 | 64.95% |
| 1(付费) | 1225 | 35.05% |

### 4.5 is_paid × pricing_tier 交叉表

| is_paid | pricing_tier | 数量 | 占比 | 备注 |
|---------|--------------|-----:|-----:|------|
| 0 | L1 | 1039 | 29.73% | 一致 |
| 0 | L2 | 572 | 16.37% | 待确认 |
| 0 | L3 | 659 | 18.86% | **矛盾** |
| 1 | L1 | 108 | 3.09% | **矛盾** |
| 1 | L2 | 517 | 14.79% | 一致 |
| 1 | L3 | 359 | 10.27% | 一致 |
| 1 | L4 | 237 | 6.78% | 一致 |
| 1 | L5 | 4 | 0.11% | 一致 |

> 合计矛盾 skill = 108 + 659 = **767 个 (21.95%)**。另有 `is_paid=0 且 L2`(572 个)的语义也需复核(L2 是否代表付费档)。

---

## 5. 重复内容检查

### 5.1 相同 content_hash 的 skill 组数

| 指标 | 数值 |
|------|-----:|
| 重复 content_hash 组数(去重) | 788 |
| 涉及重复 content_hash 的 skill 行数 | 1576 (45.09%) |

**风险评估:中**。近半数 skill 内容哈希与他人重复。但抽样显示重复多发生在 `local_only` 与 `deleted_on_skillhub` 之间(即同一 skill 的本地副本与已删除线上副本),属于历史版本残留而非恶意克隆。重复组示例:
- `ff744902...`: local_only + deleted_on_skillhub
- `fedd272c...`: local_only + local_only
- `fec18d4b...`: deleted_on_skillhub + deleted_on_skillhub

### 5.1b pending 状态的 content_hash 重复(不应有)

| 指标 | 数值 |
|------|-----:|
| pending/draft 状态下重复 content_hash 组数 | 0 |

**风险评估:无**。待发布流程中无内容重复,符合要求。

### 5.2 相同 slug 的 skill 数量

| 指标 | 数值 |
|------|-----:|
| 重复 slug 组数 | 0 |

结论:符合 UNIQUE 约束,无重复 slug。

### 5.3 相同 current_display_name 重复检查(营销命名冲突)

| 指标 | 数值 |
|------|-----:|
| 重复 display_name 组数 | 1098 |
| 涉及重复 display_name 的 skill 行数 | 2286 (65.41%) |

**风险评估:中**。65% 的 skill 与他人共用展示名,营销命名严重冲突。高频重复示例:
`Notion`(9), `Calendar`(8), `Figma`(7), `Skill`(6), `Kubernetes`(6), `Linear`(5), `进化引擎`(4), `图表工具专业版`(4), `Frontend Design`(4), `Discord`(4) ...

> 大量 skill 使用通用产品名(Notion/Figma/Linear 等)作为展示名,可能涉及商标/命名冲突,影响用户识别与平台合规。

---

## 6. 上传状态风险检查

### 6.1 skillhub_sync_status 分布

| 状态 | 数量 | 占比 |
|------|-----:|-----:|
| pending_upload | 1352 | 38.68% |
| synced | 1121 | 32.07% |
| not_applicable | 878 | 25.12% |
| deleted | 144 | 4.12% |

**skillhub_sync_status = pending_upload 的 skill 数:1352 (38.68%)**

### 6.2 clawhub_sync_status 分布

| 状态 | 数量 | 占比 |
|------|-----:|-----:|
| not_applicable | 2507 | 71.73% |
| synced | 781 | 22.35% |
| pending | 207 | 5.92% |

**clawhub_sync_status = pending 的 skill 数:207 (5.92%)**

### 6.3 其它平台同步状态分布

| 平台 | synced | not_applicable |
|------|-------:|---------------:|
| github_public_sync_status | 3411 (97.60%) | 84 (2.40%) |
| github_private_sync_status | 2898 (82.92%) | 597 (17.08%) |

### 6.4 pending skill 质量信息完整性检查

合并 `skillhub_sync_status='pending_upload'` 或 `clawhub_sync_status='pending'` 的 skill,共 **1439 个**:

| 检查项 | 数量 | 占比 | 风险 |
|--------|-----:|-----:|------|
| description 为空 | 54 | 3.75% | 中 |
| summary 为空 | 54 | 3.75% | 中 |
| pricing_tier 为空 | 0 | 0.00% | 无 |
| is_paid 为NULL | 0 | 0.00% | 无 |
| content_hash 为空 | 634 | 44.06% | 中 |
| tags 为空 | 0 | 0.00% | 无 |
| description 含模板套话 | 11 | 0.76% | 高(封禁) |
| 定价矛盾(is_paid/tier不一致) | 224 | 15.57% | 中 |
| **完全合规**(字段齐全+长度合规+无套话+无矛盾) | **0** | **0.00%** | — |
| **待修复后再上传** | **1439** | **100.00%** | 需处理 |

**风险评估:极高**。所有 1439 个待上传 skill **无一完全合规**,主要受 description 长度系统性不达标(详见第 8 节)拖累;其中 11 个含模板套话、224 个定价矛盾,若直接上传存在封禁风险。`content_hash` 缺失 634 个(44.06%)也会影响去重校验。

---

## 7. 封禁风险综合汇总

| 编号 | 风险项 | 数量 | 占比 | 等级 |
|------|--------|-----:|-----:|------|
| 风险1 | description 含模板套话 | 33 | 0.94% | 高 |
| 风险2 | slug 含程序化后缀(`-sk`/`-v2` 等) | 677 | 19.37% | 极高 |
| 风险3 | slug 长度 < 8(通用词抢占) | 140 | 4.01% | 高 |
| 风险4 | description 长度 < 150 | 3349 | 95.82% | 系统性 |
| 风险5 | description 长度 > 280 | 0 | 0.00% | 无 |
| 风险6 | summary 长度 > 100 | 0 | 0.00% | 无 |
| 风险7 | is_paid/tier 定价矛盾 | 767 | 21.95% | 极高 |
| 风险8 | 重复 content_hash 组数 | 788 | — | 中 |
| 风险9 | pending 状态 content_hash 重复 | 0 | — | 无 |
| 风险10 | description 为空 | 146 | 4.18% | 中 |
| 风险11 | pending skill 中含模板套话 | 11 | — | 高 |

---

## 8. 关键根因分析:description 字段与 summary 完全冗余

针对第 3.2 节"description 长度 100% 不达标"的异常,补充查询揭示根因:

| 检查项 | 结果 |
|--------|------|
| description 非空总数 | 3349 |
| description == summary 的数量 | **3349 (100.00%)** |
| description 最大长度 | **100 字符** |
| description 最小长度 | 4 字符 |
| description 平均长度 | 51.38 字符 |
| summary 最大长度 | 100 字符 |

**结论**:数据库 FTS 表中的 `description` 字段并非独立的营销长描述,而是 `summary` 字段的逐字副本,且两者都被硬截断在 100 字符。因此:

1. **不存在 150–280 字符的营销描述**:任务要求的"description 长度 150–280"在该数据模型下无法满足,因为根本没有长描述字段。第 3.2 节的 95.82% 不达标是 **系统性字段缺失**,而非个别 skill 质量问题。
2. **字段冗余**:`description` 与 `summary` 100% 重复,FTS 的 description 列未承载额外信息,浪费索引空间且无意义。
3. **summary 检查(3.3)通过是"假阳性"**:summary ≤100 全部合规,仅因硬截断,而非内容质量过硬。

**对封禁风险的影响**:若目标平台要求提交 150–280 字符的独立营销描述,当前 3495 个 skill **全部缺失该字段**,批量上传将因描述过短/缺失被批量拒审。这是最高优先级的结构性问题。

抽样实际内容(最长 100 字符示例):
- `news-sentiment-scan`: "舆情监控与情绪分析技能。扫描港股、美股、A股等公司公告、新闻报道、券商研报、社交媒体(微博、雪球等),去噪后进行情绪打分(-10至+10)..."
- `podcast-downloader-tool`: "小宇宙播客下载工具。从小宇宙(xiaoyuzhoufm.com)下载播客音频和Show Notes。自动转换为MP3格式..."

---

## 9. 修复建议(按优先级)

### P0 — 上传前必须修复(否则封禁)
1. **重命名 677 个含程序化后缀的 slug**:优先处理 649 个 `-sk` 后缀,改为语义化命名(如 `meeting-note-sk` → `meeting-notes-zettelkasten`)。
2. **重命名 140 个 < 8 字符的通用词 slug**:避免抢占 `api`/`pdf`/`git` 等通用词,加业务前缀。
3. **清理 33 个含模板套话的 description**:去除"一键/帮助你/本工具"等套话,改写为客观功能描述。
4. **修正 767 个定价矛盾**:统一 is_paid 与 pricing_tier 语义(明确 L1=免费档、L2+ = 付费档),逐条校正。

### P1 — 结构性缺失
5. **新增独立营销长描述字段**(150–280 字符):当前 description=summary(100 字符硬截断)无法满足平台要求,需在 skills 表新增 `marketing_description` 列并补充内容,或扩展 summary 上限。这是导致 1439 个 pending skill 100% 不合规的根因。
6. **补充 738 个空 content_hash**:用于内容去重与版本追踪。
7. **补充 146 个空 description/summary**。

### P2 — 数据治理
8. **清理 788 组重复 content_hash**:确认是历史版本残留后归档/删除冗余 `local_only`/`deleted` 副本。
9. **治理 1098 组重复 display_name**:避免共用 Notion/Figma 等商标名,改为差异化命名。
10. **细化 507 个 `Other` 分类**:归入具体 category。
11. **复核 572 个 `is_paid=0 且 L2`** 的定价语义。

### P3 — 流程管控
12. pending_upload(1352)+ clawhub pending(207)共 1439 个 skill,**100% 不合规**,上传前必须先跑质量门禁(字段齐全 + 长度合规 + 无套话 + 无矛盾),目前通过率为 0。

---

*本报告由只读 SQL 查询生成,未对 `skill-registry.db` 做任何修改。原始查询日志见 `audit_report.txt`。*
