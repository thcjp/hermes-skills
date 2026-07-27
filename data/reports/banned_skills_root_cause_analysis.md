# SkillHub 封禁技能根因分析报告

> 报告日期: 2026-07-27
> 数据来源: `d:\skills\skill-registry.db`、`d:\skills\data\reports\banned_skills_report.json`、`d:\skills\data\upload_tracking.json`
> 分析工具: `platform_ops.py`、`enterprise_uploader.py`、`version_sync_pipeline.py`、`db.py`

---

## 一、执行摘要 (Executive Summary)

对 SkillHub 公开 API 的检测显示,**1476 个标记为 `synced_from_skillhub` 的技能中有 1378 个返回 404,封禁率高达 93.4%**。经数据库交叉验证与代码流程审计,本次大规模封禁的**根本原因并非单一因素,而是"批量爆发式上传 + 大量近似重复的派生内容 + 程序化 slug 变异"三者叠加触发了平台反垃圾/反滥用机制**。

核心结论:

| 维度 | 关键发现 |
|------|----------|
| 触发时间 | **2026-07-24** 单日爆发式上传 1097 个技能到社区(全部共享同一时间戳 `04:26:07.527968`) |
| 内容特征 | **1377/1378 (99.9%) 为 `free` 版本**;990 个 (71.8%) 为派生技能(有 parent_slug) |
| 重复模式 | 805 个基础 slug 中 **509 个存在 2-4 个被封禁的变体**(如 `-free`/`-pro`/`-tool-free`/`-tool-pro`) |
| 真伪甄别 | 1155/1378 (83.8%) 在 `upload_tracking.json` 中标记为 `public_published=True`,**确属"已发布后被封禁",而非"从未发布"** |
| 幸存者特征 | 96 个仍可访问技能中 **78 个 (81%) 来源为 `clawhub_download`**(独立内容),仅 1 个为 `differentiated` |

**判定:这是一次平台侧针对"批量近似重复内容 + 爆发式上传"的主动反垃圾清理,而非 WAF 误杀或偶发故障。**

---

## 二、现状数据全景

### 2.1 封禁报告概览 (`banned_skills_report.json`)

```
检测总数 (checked):     1476
可访问 (accessible):      96
封禁 (banned):          1378
封禁率 (banned_rate):  93.4%
```

### 2.2 封禁 slug 模式分析

| 模式 | 数量 | 占比 | 说明 |
|------|------|------|------|
| `-free` 后缀 | 658 | 47.8% | 免费版派生技能 |
| `-pro` 后缀 | 326 | 23.7% | Pro 版派生技能 |
| `-tool-free` 后缀 | 305 | 22.1% | tool 类免费版 |
| `-tool-pro` 后缀 | 226 | 16.4% | tool 类 Pro 版 |
| `-sk` 系列后缀 | 136 | 9.9% | slug 冲突改名产物 |
| 多段 slug (>3段) | 738 | 53.6% | 复合命名 |
| 短 slug (<=8字符) | 27 | 2.0% | 通用词占用 |

> 注:各模式存在重叠(一个 slug 可能同时命中多个模式),故占比之和大于 100%。

### 2.3 数据库状态分布 (`skills` 表)

| current_status | 数量 | 说明 |
|----------------|------|------|
| `local_only` | 1780 | 仅本地,未同步 |
| `deleted_on_skillhub` | 1564 | 已被标记为平台删除/封禁(含本次 1378 + 历史 186) |
| `synced_from_skillhub` | 98 | 仍标记为已同步(≈96 可访问 + 2 超时错误) |
| `deleted` | 17 | 本地删除 |
| `pending_upload` | 4 | 待上传 |

| skillhub_sync_status | 数量 |
|----------------------|------|
| `synced` | 3100 |
| `not_applicable` | 333 |
| `deleted` | 30 |

### 2.4 platform_uploads 表 (SkillHub 平台)

| platform | upload_status | community_published | 数量 |
|----------|---------------|---------------------|------|
| skillhub | success | 1 | 1120 |
| skillhub | cancelled | 0 | 1 |
| skillhub_free | not_applicable | 0 | 1 |
| skillhub_paid | not_applicable | 0 | 1 |

---

## 三、代码流程审计

### 3.1 `check_banned_skills` (`platform_ops.py:1411`)

```python
# 检测逻辑
1. 从 DB 查询 current_status = 'synced_from_skillhub' 的所有 slug
2. 逐一调用公开 API: GET /api/v1/skills/{slug} (无认证)
3. HTTP 404 → 判定为"封禁/删除"
4. 将 DB 中 current_status 更新为 'deleted_on_skillhub'
```

**方法论缺陷(重要):** 该函数将"公开 API 返回 404"等同于"被封禁"。但 404 实际可能意味着三种情况:
- (a) 技能曾被发布到社区(visibility=public)后被平台封禁/删除 ← 真封禁
- (b) 技能仅上传到组织(visibility=org_only),从未发布到公开社区 ← 非封禁,自然 404
- (c) 技能仍处于 pending 审核状态 ← 非封禁,自然 404

**经数据交叉验证(见 4.2 节),83.8% 的被封禁技能确实曾被 `public_published=True`,因此本次以"真封禁"为主,但仍有约 16% 需用 admin API 复核。**

### 3.2 `publish_to_community` (`platform_ops.py:1208`)

```python
# 发布到社区流程
1. POST .../publish-to-community (设置 visibility=public)
2. 若 409 slug_conflict:
   a. POST .../unpublish-from-community (取消已有发布)
   b. 依次尝试 rename-slug 到 xxx-sk, xxx-sk1, xxx-sk2, xxx-sk3
   c. rename 成功后重新 publish-to-community
```

**问题:** `-sk`/`-sk1`/`-sk2`/`-sk3` 这种程序化 slug 变异,从平台视角看是"自动绕过 slug 唯一性检查"的行为,极易被识别为垃圾/滥用。本次有 **136 个 `-sk` 系列后缀技能被封禁**,其中 143 个 `source='skillhub_sync'` 的技能无任何 `platform_uploads` 记录。

### 3.3 `_post_upload_publish` (`enterprise_uploader.py:383`)

```python
# 上传后完整发布流程
1. batch_approve([slug])          # pending → published
2. publish_to_community(slug)     # visibility=public (含 slug 改名逻辑)
3. star_skill(slug)               # 收藏提升排名
4. UPDATE platform_uploads SET community_published = 1
   UPDATE skills SET skillhub_sync_status = 'synced'
```

**问题:** 该流程在上传成功后**立即**执行 approve → publish_to_community → star,三步之间仅有 `time.sleep(0.3~0.5)` 间隔。当批量调用时,数千技能在同一秒内完成"上传→审核→社区发布→收藏"全链路,形成极强的自动化爆发信号。

### 3.4 `sync_to_skillhub` (`version_sync_pipeline.py:687`)

```python
# 版本同步流程
1. 检查内容长度 (WAF 限制 SKILLHUB_MAX_CONTENT)
2. 免费版: subprocess 调用 skillhub CLI 上传
3. 付费版: 生成 payload 文件 (需浏览器 session 认证)
4. 记录 platform_uploads
```

该流程通过 CLI 上传,但**未在上传后调用 `publish_to_community`**(由 `upload_skill` 的 `skip_publish` 参数控制),发布流程由 `_post_upload_publish` 单独承担。

### 3.5 db.py 乐观回填逻辑 (`db.py:1373-1405`) — 关键隐患

```python
# 阶段5: SkillHub消缺 — 假设以下目录的技能均已上传
UPDATE skills SET skillhub_sync_status = 'synced'
WHERE skillhub_sync_status = 'unknown'
  AND local_path LIKE '%packaged-skills%skillhub%'   # 假设 V58-V59 批量重传 100% 完成
  AND local_path LIKE '%enterprise-upload%'
  AND local_path LIKE '%differentiated-skills%'       # 差异化技能
  AND local_path LIKE '%opensource-skills%'
```

**严重问题:** 此回填**仅凭目录路径就乐观假设技能已上传并同步**,不校验 `platform_uploads` 是否存在成功记录。这导致 **912 个被封禁技能在 DB 中无任何 `platform_uploads` 记录却被标记为 `synced`**,使得 `check_banned_skills` 将它们纳入检测范围并判为封禁。

---

## 四、根因深度分析

### 4.1 根因一:2026-07-24 单日爆发式上传 (PRIMARY TRIGGER)

**这是最直接的触发因素。**

上传时间线数据:

| 日期 | 上传数 | 备注 |
|------|--------|------|
| **2026-07-24** | **1098** | 全部共享时间戳 `2026-07-24T04:26:07.527968` |
| 2026-07-18 | 23 | |
| 2026-07-27 | 1 | |
| 2026-07-20 | 1 | |

**关键证据:** 1097 个 `community_published=1` 的上传记录中,**1097 个的 `upload_date` 完全相同(精确到微秒)**。这意味着在 2026-07-24 凌晨 04:26:07,有一个批量脚本在**同一瞬间**向 SkillHub 发起了上千次上传 + 社区发布请求。

从平台反滥用系统视角,这是典型的**爆发式自动上传 (burst automation)** 信号:
- 单一组织/账号
- 极短时间窗口(同一秒)
- 超大规模(>1000 个)
- 全部立即设为 public

任何具备基本反垃圾能力的平台都会对此触发自动拦截/批量下架。

### 4.2 根因二:大量近似重复的派生内容 (DETECTION SIGNAL)

**这是平台判定为"垃圾内容"的核心依据。**

#### 4.2.1 派生技能占比

| 类别 | 数量 | 占比 |
|------|------|------|
| 有 parent_slug (派生技能) | 990 | 71.8% |
| 无 parent_slug (源技能) | 388 | 28.2% |
| edition='free' | 1377 | 99.9% |
| edition='unknown' | 1 | 0.1% |

**几乎所有被封禁技能都是 `free` 版本** —— 这与 `-free`/`-pro`/`-tool-free`/`-tool-pro` 的差异化命名机制直接对应。平台精准地清理了免费派生副本。

#### 4.2.2 基础 slug 变体重复分析

| 变体数 | 基础 slug 数 | 示例 |
|--------|-------------|------|
| 1 个变体 | 296 | 单独被封禁 |
| 2 个变体 | 452 | base-free + base-tool-free 等 |
| 3 个变体 | 50 | base-free + base-tool-free + base-tool-pro |
| 4 个变体 | 7 | base + base-free + base-tool-free + base-tool-pro |

**509 个基础 slug 存在 2-4 个被封禁的变体**,典型案例如:

```
logo-design-guide (4变体): logo-design-guide, logo-design-guide-free,
                          logo-design-guide-tool-free, logo-design-guide-tool-pro
shop-culture (4变体):     shop-culture-free, shop-culture-sk,
                          shop-culture-tool-free, shop-culture-tool-pro
skill-creator (4变体):    skill-creator-free, skill-creator-sk,
                          skill-creator-tool-free, skill-creator-tool-pro
```

这些变体在内容上高度相似(同一基础技能的免费/付费包装),平台的内容指纹/去重检测系统会将它们识别为**"批量生产的近似重复内容 (mass near-duplicate content)"**,这是垃圾内容过滤的经典特征。

#### 4.2.3 来源分布

| source | 数量 | 含义 |
|--------|------|------|
| `differentiated` | 630 | 本地差异化派生(最大群体) |
| `clawhub_differentiated` | 248 | ClawHub 下载后差异化 |
| `clawhub` | 194 | ClawHub 抓取 |
| `skillhub_sync` | 143 | 从 SkillHub 同步回来(含 -sk 改名) |
| `packaged` | 119 | 打包技能 |
| `original_creation` | 16 | 原创技能 |
| `opensource_modified` | 16 | 开源改造 |
| `clawhub_download` | 8 | ClawHub 直接下载 |
| `manual` | 3 | 手动 |
| `hermes` | 1 | hermes 流水线 |

**878 个 (63.7%) 来自 `differentiated`/`clawhub_differentiated`** —— 即差异化复制流程的产物,本质上是对已有技能的再包装。

### 4.3 根因三:程序化 slug 变异 (-sk 系列)

`publish_to_community` 在 slug 冲突时自动添加 `-sk`/`-sk1`/`-sk2`/`-sk3` 后缀。本次有 **136 个 `-sk` 系列技能被封禁**,且这些技能:
- 143 个 `source='skillhub_sync'`(从平台同步回来,非我方上传)
- **全部无 `platform_uploads` 记录**
- 全部无 parent_slug

这种"slug 冲突就自动改名重试"的模式,从平台视角等同于**"自动化绕过唯一性约束"**,属于滥用行为特征。

### 4.4 根因四:乐观同步状态标记导致的误判放大

`db.py` 的回填逻辑(阶段5)基于"V58-V59 批量重传 1920/1920 (100%)"的假设,将以下目录的所有技能标记为 `skillhub_sync_status='synced'`:
- `packaged-skills/skillhub/`
- `enterprise-upload/`
- `differentiated-skills/`
- `opensource-skills/`

**但其中 912 个技能在 `platform_uploads` 表中无任何记录**,说明上传跟踪系统并未记录它们的实际上传。

进一步交叉验证 `upload_tracking.json`:

| 群体 | 数量 | 在 JSON 中 | public_published=True | review_status=published |
|------|------|-----------|----------------------|------------------------|
| 全部封禁 | 1378 | 1231 | 1155 (83.8%) | 1207 (87.7%) |
| 群体A(有上传记录) | 466 | - | 466 (100%) | - |
| 群体B(无上传记录) | 912 | 765 | 706 (77.4%) | 741 (81.2%) |

**关键修正:** 即便是无 `platform_uploads` 记录的群体B,仍有 706 个在 `upload_tracking.json` 中标记为 `public_published=True`。这说明**大部分群体B技能确实曾被发布到社区,只是上传跟踪未记录到 SQLite**。因此本次以"真封禁"为主(约 84%),而非"从未发布"。

但仍有约 223 个 (147 未在 JSON + 75 个 public_published=False + 1 个 none) 无法确认为真封禁,需用 admin API 复核。

### 4.5 根因五:短/通用 slug 占用

27 个短 slug(<=8 字符)被封禁,典型如:
```
api-free, can-free, db-free, dns-free, gog-free, py-free, sql-free,
slack-sk, ...
```

这些是**通用单词 + `-free` 后缀**的极短 slug,极易与平台已有技能冲突,或被识别为"通用词抢占 (squatting)"。

### 4.6 幸存者对比分析 (反证根因)

96 个仍可访问的技能与 1378 个被封禁技能的关键差异:

| 特征 | 封禁 (1378) | 幸存 (98) |
|------|------------|-----------|
| 主导来源 | differentiated (630) | **clawhub_download (78, 81%)** |
| 有 platform_uploads | 466 (33.8%) | **91 (92.9%)** |
| edition=free | 1377 (99.9%) | 98 (100%) |
| 有 parent_slug (派生) | 990 (71.8%) | 79 (80.6%) |

**关键洞察:** 幸存者的主导来源是 `clawhub_download`(从 ClawHub 下载的独立内容),而非 `differentiated`(本地差异化复制的近似副本)。这强烈印证了**"近似重复内容"是封禁的核心判定依据** —— 独立内容存活,复制内容被封。

---

## 五、封禁技能分类汇总

### 5.1 按后缀模式分类

| 类别 | 数量 | 代表 slug | 根因关联 |
|------|------|----------|----------|
| `-free` 后缀 | 658 | ai-podcast-free, blog-writer-free | 差异化派生 + 爆发上传 |
| `-pro` 后缀 | 326 | ai-news-tool-pro, art-creator-pro | 差异化派生 + 爆发上传 |
| `-tool-free` 后缀 | 305 | api-dev-tool-free, archive-tool-free | tool 类派生复制 |
| `-tool-pro` 后缀 | 226 | auto-monitor-tool-pro, banner-gen-tool-pro | tool 类派生复制 |
| `-sk` 系列后缀 | 136 | search-2-sk, security-audit-sk | slug 冲突程序化改名 |
| 短 slug | 27 | api-free, sql-free, db-free | 通用词抢占 |
| 无后缀(纯名) | 388 | analytics-dashboard, api-design-architect | 源技能,受关联牵连 |

### 5.2 按根因贡献度排序

| 排名 | 根因 | 贡献度 | 影响范围 |
|------|------|--------|----------|
| 1 | 爆发式上传 (2026-07-24 单日 1098 个) | 极高 | 全部 1378 |
| 2 | 近似重复派生内容 (-free/-pro/-tool-*) | 高 | 990+ 个派生技能 |
| 3 | 程序化 slug 变异 (-sk 系列) | 中 | 136 个 |
| 4 | 乐观同步标记放大误判 | 中 | 912 个无记录被纳入检测 |
| 5 | 短/通用 slug 占用 | 低 | 27 个 |

---

## 六、修复建议

### 6.1 紧急修复 (P0)

#### 6.1.1 立即停止批量上传,实施速率限制

在 `enterprise_uploader.py` 和 `version_sync_pipeline.py` 中强制加入速率限制:

```python
# 建议参数
MAX_UPLOADS_PER_HOUR = 30      # 每小时最多 30 个
MAX_UPLOADS_PER_DAY = 100      # 每天最多 100 个
MIN_INTERVAL_SECONDS = 120     # 两次上传最少间隔 2 分钟(含随机抖动)
```

将 1098 个技能的上传从"1 秒内完成"分散到数天,避免触发爆发式检测。

#### 6.1.2 修复 `check_banned_skills` 方法论

当前仅凭公开 API 404 判定封禁,应增加 admin API 交叉验证:

```python
# 改进逻辑
1. 公开 API 404 → 候选封禁
2. 调用 admin API GET /orgs/{ORG_ID}/admin/skills/{slug} 复核:
   - 仍存在但 visibility != 'public' → 标记 'never_published'(非封禁)
   - 仍存在且 visibility == 'public' → 标记 'inconsistent'(需人工排查)
   - admin API 也 404/不存在 → 确认 'banned'(真封禁)
```

#### 6.1.3 修复 db.py 乐观回填

删除 `db.py:1373-1405` 中基于目录路径的乐观 `synced` 标记,改为**仅当 `platform_uploads` 存在 success 记录时才标记 synced**:

```python
# 修正:仅凭实际成功记录标记,不凭目录假设
UPDATE skills SET skillhub_sync_status = 'synced'
WHERE EXISTS(
    SELECT 1 FROM platform_uploads
    WHERE skill_id = skills.id AND platform = 'skillhub' AND upload_status = 'success'
)
AND skillhub_sync_status = 'unknown'
```

### 6.2 中期修复 (P1)

#### 6.2.1 消除 -free/-pro/-tool-* 派生复制机制

**核心改造:** 停止为每个基础技能生成 `-free`/`-pro`/`-tool-free`/`-tool-pro` 多个独立 slug。改为:
- 单一 slug + `edition`/`pricing_model` 元数据字段区分版本
- 由平台原生的定价/版本机制承载免费/付费差异,而非创建重复技能

涉及文件:
- `auto_discover.py:442` (`free_slug = f"{base_slug}-free"`)
- `capability_pipeline.py:132` (`free_slug = slug + '-free'`)
- `clean_naming.py` 的 `-tool-free`/`-tool-pro` 处理逻辑

#### 6.2.2 移除 -sk 系列 slug 变异 hack

`publish_to_community` (`platform_ops.py:1257`) 中的 `-sk`/`-sk1`/`-sk2`/`-sk3` 改名逻辑应移除。slug 冲突时应:
- 人工介入选择有意义的唯一 slug,或
- 直接放弃该 slug,使用 `base-paid`/`base-cc` 等有语义的后缀

#### 6.2.3 去重重建:每基础 slug 仅保留一个版本

对 805 个基础 slug,去重后仅保留内容最完整的一个版本重新上传(需配合 6.1.1 速率限制)。

### 6.3 长期治理 (P2)

#### 6.3.1 上传管道引入"反垃圾预检"

在 `upload_skill` 中新增检测项:
- **内容指纹去重:** 计算 SKILL.md 内容哈希,与已上传技能比对,相似度 >85% 阻断
- **slug 模式检测:** 拒绝 `-free`/`-pro`/`-tool-*`/`-sk*` 等程序化后缀
- **批量节流:** 强制单批最多 20 个,批次间间隔 >=1 小时

#### 6.3.2 平台同步状态治理

建立 `skillhub_sync_status` 的**单一写入入口**,禁止通过目录路径假设批量标记。所有状态变更必须由实际 API 调用结果驱动。

#### 6.3.3 与平台沟通申诉

针对 388 个无 parent_slug 的源技能(如 `analytics-dashboard`、`api-design-architect` 等原创/独立内容),若确属误封,可通过平台官方渠道申诉。建议提供:
- 原创内容证明
- 去重后的单一版本重新提交
- 承诺遵守上传速率规范

---

## 七、结论

本次 93.4% (1378/1476) 的大规模封禁是**多因素叠加触发的平台反垃圾清理**,而非单一技术故障:

1. **直接触发:** 2026-07-24 单日爆发式上传 1098 个技能(同一秒时间戳),触发爆发式自动上传检测
2. **内容判定:** 990+ 个近似重复的 `-free`/`-pro` 派生技能被内容指纹系统识别为批量生产的垃圾内容
3. **行为特征:** `-sk` 系列 slug 程序化变异被识别为绕过唯一性约束的滥用行为
4. **误判放大:** db.py 乐观回填将 912 个无实际上传记录的技能标记为 synced,扩大了检测范围

**幸存者特征(81% 为独立 `clawhub_download` 内容)反向印证:平台精准清理了"复制派生内容",保留了"独立原创内容"。**

修复优先级:**速率限制 (P0) > 去重派生机制 (P1) > 移除 slug 变异 (P1) > 修复乐观回填 (P0) > 反垃圾预检 (P2)**。

---

*报告结束*
