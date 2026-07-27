# SkillHub 发布流程代码审查报告

**审查范围**: `d:\skills\tools` 目录下 SkillHub 发布流程相关代码
**审查日期**: 2026-07-27
**审查重点**: 发布流程一致性、-sk 改名问题、封禁检测方法论、乐观回填、冗余文件

---

## 一、问题总览

| 编号 | 严重程度 | 问题 | 文件 |
|------|----------|------|------|
| C1 | Critical | star_skill 使用陈旧 slug（改名后未同步） | enterprise_uploader.py:416 |
| C2 | Critical | publish_to_community -sk 改名生成畸形 slug | platform_ops.py:1260 |
| C3 | Critical | db.py 乐观回填导致 false synced 状态 | db.py:1373-1405 |
| H1 | High | check_banned_skills 仅凭 404 判定封禁，方法论缺陷 | platform_ops.py:1411-1523 |
| H2 | High | platform_ops.batch_approve 依赖失效的 API 过滤器 | platform_ops.py:980 |
| H3 | High | auto_publish.py 废弃命令未清理，仍被推荐调用 | auto_publish.py:463-480 |
| H4 | High | batch_approve_api.py 与 platform_ops.batch_approve 重复 | batch_approve_api.py 全文件 |
| M1 | Medium | DB 更新逻辑不一致（slug 查询 vs skill_id 查询） | enterprise_uploader.py:428 vs version_sync_pipeline.py:1167 |
| M2 | Medium | community_slug（改名后新 slug）未写入 SQLite | platform_ops.py:1280, enterprise_uploader.py:423 |
| M3 | Medium | auto_publish.py public-publish 命令文档存在但未实现 | auto_publish.py:11 |
| L1 | Low | enterprise_uploader DB 更新异常被静默吞没 | enterprise_uploader.py:437-438 |

---

## 二、Critical 级问题详解

### C1: star_skill 使用陈旧 slug（改名后未同步）

**文件**: `d:\skills\tools\enterprise_uploader.py:413-420`

**问题代码**:
```python
# Step 3: 收藏 (提升搜索排名) + DB更新 — 仅在社区发布成功时执行
if ptc_result.get('success'):
    time.sleep(0.2)
    star_result = star_skill(slug)   # <-- BUG: 使用原始 slug
```

**根因分析**:
`publish_to_community(slug)` 在遇到 slug 冲突时会执行改名操作（如 `foo` → `foo-sk`），返回结果为：
```python
{'success': True, 'slug': 'foo-sk', 'original_slug': 'foo', ...}
```
但 `_post_upload_publish` 中的 `star_skill(slug)` 始终使用传入的原始 slug（`foo`），而非改名后的新 slug（`foo-sk`）。

`star_skill` 内部调用 `POST /api/v1/skills/{slug}/star`（platform_ops.py:954），如果 slug 已改名为 `foo-sk`，则对 `foo` 的 star 请求会返回 404，收藏操作静默失败。

**影响**:
- 所有触发 -sk 改名的 skill 都无法被收藏
- 搜索排名无 star 加分，降低了前台可见性
- 这与"看起来已发布但前台不可见"的根因问题直接相关

**修复方案**:
```python
if ptc_result.get('success'):
    time.sleep(0.2)
    # 使用社区发布后的实际 slug（可能已改名）
    actual_slug = ptc_result.get('slug', slug)
    star_result = star_skill(actual_slug)
```

---

### C2: publish_to_community -sk 改名生成畸形 slug

**文件**: `d:\skills\tools\platform_ops.py:1255-1277`

**问题代码**:
```python
current_slug = slug
for suffix in ['-sk', '-sk1', '-sk2', '-sk3']:
    if current_slug.endswith(suffix):
        continue
    new_slug = slug + suffix  # 始终基于原始slug生成new_slug  <-- BUG
    rename_url = f".../admin/skills/{current_slug}/rename-slug"
```

**根因分析**:
`new_slug = slug + suffix` 始终在**原始 slug** 后追加后缀。当输入 slug 本身已带 `-sk` 后缀时（即二次发布/重发布场景），会生成畸形 slug：

**复现路径**（输入 slug = `"foo-sk"`，即之前已改名过一次的 skill）:
| 迭代 | suffix | current_slug.endswith(suffix) | new_slug = slug + suffix | 结果 |
|------|--------|-------------------------------|--------------------------|------|
| 1 | `-sk` | `"foo-sk".endswith("-sk")` → True | 跳过 | continue |
| 2 | `-sk1` | `"foo-sk".endswith("-sk1")` → False | `"foo-sk" + "-sk1"` = **`"foo-sk-sk1"`** | 畸形 slug |
| 3 | `-sk2` | `"foo-sk-sk1".endswith("-sk2")` → False | `"foo-sk" + "-sk2"` = **`"foo-sk-sk2"`** | 畸形 slug |

生成的 `"foo-sk-sk1"` 既不符合命名规范，也加剧了封禁风险（根因分析报告指出 `-sk` 系列改名是封禁原因之一，畸形的多段后缀会进一步触发平台风控）。

**影响**:
- 生成畸形 slug（如 `foo-sk-sk1`、`foo-sk-sk2`），加剧封禁风险
- `current_slug.endswith(suffix)` 检查无法拦截此情况（`"foo-sk"` 不以 `"-sk1"` 结尾）
- 改名后的 skill 二次发布时必然触发此 bug

**修复方案**:
```python
# 先剥离已有的 -sk 系列后缀，得到 base slug
base_slug = slug
for existing_suffix in ['-sk3', '-sk2', '-sk1', '-sk']:
    if base_slug.endswith(existing_suffix):
        base_slug = base_slug[:-len(existing_suffix)]
        break

current_slug = slug
for suffix in ['-sk', '-sk1', '-sk2', '-sk3']:
    if current_slug.endswith(suffix):
        continue
    new_slug = base_slug + suffix  # 基于剥离后的 base slug 生成
    # ... 后续逻辑不变
```

---

### C3: db.py 乐观回填导致 false synced 状态

**文件**: `d:\skills\tools\db.py:1373-1405`

**问题代码**:
```python
# ====== 阶段5: SkillHub消缺 — packaged-skills/skillhub/目录的skill已上传 ======
# V58-V59完成1920/1920批量重传(100%)，packaged-skills/skillhub/目录的skill
# 都已通过enterprise_uploader上传到SkillHub
c.execute("""
    UPDATE skills SET skillhub_sync_status = 'synced'
    WHERE skillhub_sync_status = 'unknown'
    AND local_path LIKE '%packaged-skills%skillhub%'
""")
# ... 类似的还有 enterprise-upload / differentiated-skills / opensource-skills
```

**根因分析**:
这段代码基于**目录路径假设**批量标记 `skillhub_sync_status = 'synced'`，而非基于实际的上传成功记录（`platform_uploads` 表）。

该逻辑存在以下问题：
1. **假设不可靠**: 文件在 `packaged-skills/skillhub/` 目录下，不代表已成功上传。上传可能失败、被 WAF 拦截、被拒绝、或上传后又被封禁。
2. **覆盖了阶段1的结果**: 阶段1（db.py:1232-1245）已经基于 `platform_uploads` 表做了精确回填，但阶段5用路径假设覆盖了阶段1未能确定的 `unknown` 记录，将未上传的 skill 也标记为 `synced`。
3. **与 C2 改名 bug 联动放大**: 如果 skill 被改名（`foo` → `foo-sk`），SQLite 中 `skills.slug` 仍为 `foo`，被标记为 `synced`，但平台上实际 slug 是 `foo-sk`。后续 `check_banned_skills` 用 `foo` 查公开 API 得到 404，误判为封禁。

**误判放大链路**:
```
db.py 阶段5: local_path LIKE '%packaged-skills%' → skillhub_sync_status='synced' (乐观假设)
    ↓
check_banned_skills: 查询 current_status='synced_from_skillhub' 的 slug
    ↓
公开 API GET /skills/{原始slug} → 404 (因为已改名为 -sk)
    ↓
误判为封禁: current_status = 'deleted_on_skillhub' (错误)
    ↓
后续运维基于错误状态做决策: 可能删除本地文件或放弃修复
```

**影响**:
- 大量未上传/上传失败/已改名的 skill 被错误标记为 `synced`
- 为 `check_banned_skills` 的误判提供了错误的数据源
- 1920 个 skill 的批量乐观标记，误判数量可能很大

**修复方案**:
```python
# 删除阶段5的乐观回填，仅保留阶段1基于 platform_uploads 的精确回填
# 如果需要处理 unknown 状态，应调用 check_banned_skills + admin API 逐一验证
# 而非基于目录路径假设批量标记

# 替代方案: 标记为 'pending_verification' 而非 'synced'
c.execute("""
    UPDATE skills SET skillhub_sync_status = 'pending_verification'
    WHERE skillhub_sync_status = 'unknown'
    AND local_path LIKE '%packaged-skills%skillhub%'
""")
```

---

## 三、High 级问题详解

### H1: check_banned_skills 仅凭 404 判定封禁，方法论缺陷

**文件**: `d:\skills\tools\platform_ops.py:1411-1523`

**问题代码**:
```python
def check_banned_skills(limit: int = 0) -> dict:
    # ...
    for i, slug in enumerate(all_slugs, 1):
        url = f"{_API_BASE}/skills/{slug}"
        try:
            req = Request(url, headers=pub_headers)
            with urlopen(req, timeout=10) as resp:
                accessible += 1
        except HTTPError as e:
            if e.code == 404:
                banned += 1
                banned_slugs.append(slug)
                # ... 直接标记为 deleted_on_skillhub
```

**根因分析**:
仅凭公开 API 404 判定封禁，但 404 实际上可能意味着以下**四种**情况，函数无法区分：

| 情况 | 实际状态 | 404? | 判定结果 | 正确? |
|------|----------|------|----------|-------|
| a. 曾发布后被封禁 | 真封禁 | 是 | banned | 正确 |
| b. 仅上传到组织，从未发布到社区 | visibility=org_only | 是 | banned | **误判** |
| c. 仍处于 pending/admin_review 审核状态 | 未上架 | 是 | banned | **误判** |
| d. slug 已改名为 -sk 后缀 | 平台 slug 变了 | 是（原始 slug） | banned | **误判** |

该函数**未使用 admin API 交叉验证**。同文件中的 `get_platform_status`（platform_ops.py:1103-1151）已经同时查询 admin API 和公开 API，但 `check_banned_skills` 只用了公开 API。

**影响**:
- 大量 `org_only`、`pending`、已改名的 skill 被误判为封禁
- 误判后直接修改 SQLite `current_status = 'deleted_on_skillhub'`，造成数据污染
- 与 C3 的乐观回填联动，误判被放大

**修复方案**:
```python
def check_banned_skills(limit: int = 0) -> dict:
    # ...
    cookies, admin_headers = _load_api_auth()
    
    for i, slug in enumerate(all_slugs, 1):
        # Step 1: 先查 admin API 获取实际状态
        admin_url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills?slug={slug}&pageSize=1"
        success, admin_data = _api_request('GET', admin_url, admin_headers)
        
        if success and admin_data.get('skills'):
            skill = admin_data['skills'][0]
            vis = skill.get('visibility', '')
            rs = skill.get('reviewStatus', '')
            # 只有 admin API 也找不到，或明确标记为 deleted/banned 的才是真封禁
            if vis == 'public' and rs in ('published', 'approved'):
                # admin API 确认存在且公开，但公开 API 404 → 真封禁
                # 再查公开 API 确认
                pub_url = f"{_API_BASE}/skills/{slug}"
                pub_success, _ = _api_request('GET', pub_url, pub_headers)
                if not pub_success:
                    banned_slugs.append(slug)
            elif vis == 'org_only' or rs in ('pending', 'admin_review'):
                # 非封禁，跳过
                pass
        else:
            # admin API 也找不到 → 可能真删除
            banned_slugs.append(slug)
```

---

### H2: platform_ops.batch_approve 依赖失效的 API 过滤器

**文件**: `d:\skills\tools\platform_ops.py:980` 对比 `d:\skills\tools\batch_approve_api.py:55-59`

**问题代码** (platform_ops.py):
```python
def batch_approve(slugs: list = None, delay: float = 0.3) -> dict:
    # ...
    if slugs is None:
        url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills?reviewStatus=pending&page=1&pageSize=1"
        #                                                     ^^^^^^^^^^^^^^^^^^^^^^^^
        #                                                     依赖 API 过滤器
```

**对比** (batch_approve_api.py:55-59):
```python
def get_pending_skills(page=1, pageSize=100):
    """获取待审核skill列表
    
    注意: API的reviewStatus过滤器可能不生效，返回所有skill。
    调用方需通过skill对象中的reviewStatus字段做二次过滤。
    """
```

**根因分析**:
`batch_approve_api.py` 已经明确注释"API 的 reviewStatus 过滤器可能不生效"，并实现了客户端二次过滤逻辑（batch_approve_api.py:132-147，检查 `rs == 'admin_review'` 和 `rs == 'pending'`）。

但 `platform_ops.py` 的 `batch_approve` 直接信任 `reviewStatus=pending` 过滤器，**未做客户端二次过滤**。如果过滤器失效，会返回所有 skill，然后对所有 skill 调用 approve API。

**影响**:
- 可能对已 published 的 skill 调用 approve，产生无意义请求
- 可能遗漏 `admin_review` 状态的 skill（因为只过滤了 `pending`，未包含 `admin_review`）
- 与 `batch_approve_api.py` 的过滤逻辑不一致

**修复方案**:
```python
def batch_approve(slugs: list = None, delay: float = 0.3) -> dict:
    # ...
    if slugs is None:
        # 不依赖 API 过滤器，获取全部后客户端二次过滤
        slugs = []
        page = 1
        while True:
            url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills?page={page}&pageSize=100"
            success, data = _api_request('GET', url, headers)
            if not success:
                break
            for sk in data.get('skills', []):
                rs = sk.get('reviewStatus', '')
                if rs in ('pending', 'admin_review'):  # 客户端二次过滤
                    slugs.append(sk.get('slug', ''))
            if len(slugs) >= data.get('total', 0) or not data.get('skills'):
                break
            page += 1
```

---

### H3: auto_publish.py 废弃命令未清理，仍被推荐调用

**文件**: `d:\skills\tools\auto_publish.py`

**问题1**: `check_visibility()` 函数推荐调用已废弃命令

```python
# auto_publish.py:462-468
"recommendations": [
    "对 org_only 技能执行 gen-community-publish-js 生成发布脚本",     # 废弃命令
    "对 NULL visibility 技能执行 gen-community-publish-js (含诊断模式)", # 废弃命令
    "对 retry_pending 技能执行 publish-skillhub 重新上传",
    "对 NULL/无效 category 技能执行 fix_missing_fields.py 推断category",
    "在浏览器执行生成的JS脚本后执行 sync-platform-status 同步结果",     # 废弃命令
],

# auto_publish.py:480
print(f"  1. 执行: python tools/auto_publish.py gen-community-publish-js")  # 废弃命令
```

**问题2**: 文档头声明了废弃命令，但 `check_visibility()` 的推荐项未同步更新

```python
# auto_publish.py:18-21 (文档头声明废弃)
已废弃(请使用 platform_ops.py):
  - batch-public-publish    → python platform_ops.py batch-republish
  - gen-community-publish-js → python platform_ops.py batch-republish
  - sync-platform-status    → batch_republish_to_community已自动同步DB
```

**问题3**: `public-publish` 命令在文档中列为活跃命令，但未实现

```python
# auto_publish.py:11 (文档)
  4. public-publish <slug>...          — 批量对外发布(已上架→公开)

# auto_publish.py:492-529 (main 函数) — 未实现 public-publish 分支
```

**影响**:
- 用户按 `check_visibility()` 的推荐执行 `gen-community-publish-js`，会得到"未知命令"错误
- 文档与实现不一致，增加维护混乱

**修复方案**:
1. 将 `check_visibility()` 中的推荐命令改为 `python platform_ops.py batch-republish`
2. 删除文档中 `public-publish` 的活跃命令声明，或实现该命令
3. 清理 `check_visibility()` 中所有对废弃命令的引用

---

### H4: batch_approve_api.py 与 platform_ops.batch_approve 重复

**文件**: `d:\skills\tools\batch_approve_api.py`（全文件，256 行）

**重复对比**:

| 维度 | batch_approve_api.py | platform_ops.py batch_approve |
|------|----------------------|-------------------------------|
| 函数名 | `batch_approve_all()` | `batch_approve()` |
| 认证 | 自有 `init_auth()` | 复用 `_load_api_auth()` |
| API 调用 | `approve_skill(slug)` | 内联 `_api_request` |
| 过滤逻辑 | 客户端二次过滤（正确） | 依赖 API 过滤器（有 bug，见 H2） |
| 进度文件 | 有（`batch_approve_progress.json`） | 无 |
| DB 更新 | 无 | 更新 JSON DB |
| 返回值 | 无（直接 print） | dict |

**根因分析**:
`batch_approve_api.py` 是早期独立脚本，`platform_ops.py` 的 `batch_approve` 是后续集成的版本。两者功能高度重复，但 `batch_approve_api.py` 的客户端过滤逻辑更正确（见 H2），而 `platform_ops.py` 的集成度更高（更新 DB、返回 dict）。

**影响**:
- 维护两份代码，修复需同步两处
- 两者过滤逻辑不一致，可能导致行为差异
- 调用方可能混用两个入口，产生不一致的结果

**修复方案**:
1. 将 `batch_approve_api.py` 的客户端过滤逻辑合并到 `platform_ops.py batch_approve`
2. 在 `batch_approve_api.py` 中添加 deprecation warning，指向 `platform_ops.py batch-approve`
3. 最终删除 `batch_approve_api.py`

---

## 四、Medium 级问题详解

### M1: DB 更新逻辑不一致（slug 查询 vs skill_id 查询）

**文件对比**:

`enterprise_uploader.py:423-434`（slug 子查询）:
```python
conn.execute("""
    UPDATE platform_uploads SET community_published = 1
    WHERE skill_id = (SELECT id FROM skills WHERE slug = ?)
    AND platform = 'skillhub'
""", (slug,))
conn.execute("""
    UPDATE skills SET skillhub_sync_status = 'synced'
    WHERE slug = ?
""", (slug,))
```

`version_sync_pipeline.py:1163-1172`（skill_id 直接查询）:
```python
conn.execute("""
    UPDATE platform_uploads SET community_published = 1
    WHERE skill_id = ? AND platform = 'skillhub'
""", (skill_id,))
conn.execute("""
    UPDATE skills SET skillhub_sync_status = 'synced'
    WHERE id = ?
""", (skill_id,))
```

**问题**:
- `enterprise_uploader` 通过 slug 子查询定位 skill_id，如果 slug 在 skills 表中不存在（如新上传未注册），UPDATE 静默失败（影响 0 行）
- `version_sync_pipeline` 直接使用 skill_id，更健壮
- 两者的更新逻辑应统一

**修复方案**:
`enterprise_uploader._post_upload_publish` 应在 `upload_skill` 调用前就获取 skill_id，传入 `_post_upload_publish`，使用 skill_id 更新 DB。

---

### M2: community_slug（改名后新 slug）未写入 SQLite

**文件**: `d:\skills\tools\platform_ops.py:1280-1295`

**问题代码**:
```python
def _update_db_community_published(original_slug: str, community_slug: str):
    """更新本地DB中的社区发布状态"""
    try:
        db = load_db()  # <-- JSON DB
        if original_slug in db['skills']:
            sh = db['skills'][original_slug].setdefault('skillhub', {})
            # ...
            if community_slug != original_slug:
                sh['community_slug'] = community_slug  # <-- 只写 JSON DB
            # ...
            save_db(db)
    except Exception:
        pass
```

**问题**:
- 改名后的新 slug（`community_slug`）只写入 JSON DB（`upload_tracking.json`），未写入 SQLite
- `enterprise_uploader._post_upload_publish` 和 `version_sync_pipeline` 的 SQLite 更新都**不记录** community_slug
- 后续 `check_banned_skills` 从 SQLite 查询 slug，用的是原始 slug，导致 404 误判（与 C3、H1 联动）

**修复方案**:
在 SQLite 的 `platform_uploads` 表中增加 `platform_slug` 字段（或复用已有字段），记录改名后的实际平台 slug。

---

### M3: auto_publish.py public-publish 命令文档存在但未实现

**文件**: `d:\skills\tools\auto_publish.py:11`

```python
# 文档声明
  4. public-publish <slug>...          — 批量对外发布(已上架→公开)

# main() 函数（492-529行）未实现该分支
```

**修复方案**: 删除文档中的 `public-publish` 声明，或将其路由到 `platform_ops.publish_to_community`。

---

## 五、Low 级问题

### L1: enterprise_uploader DB 更新异常被静默吞没

**文件**: `d:\skills\tools\enterprise_uploader.py:437-438`

```python
try:
    conn = sqlite3.connect(str(DB_PATH))
    # ... UPDATE 操作
    conn.commit()
    conn.close()
except Exception:
    pass  # <-- 异常被完全吞没，无日志
```

**影响**: DB 更新失败时无任何告警，问题无法被发现。

**修复方案**: 至少记录 warning 日志：
```python
except Exception as e:
    print(f"  [WARNING] DB更新失败: {e}")
```

---

## 六、冗余文件列表

| 文件 | 状态 | 重复对象 | 建议 |
|------|------|----------|------|
| `batch_approve_api.py` | 完全冗余 | `platform_ops.py:batch_approve` | 合并过滤逻辑后删除 |
| `auto_publish.py` | 部分废弃 | `platform_ops.py` 多个函数 | 保留 `check_visibility`/`retry_cos_failures`，废弃部分清理引用 |
| `auto_publish.py` 的 `public-publish` 命令 | 文档残留 | 无实现 | 删除文档声明 |

### 碎片化文件清理建议

以下文件功能可考虑收口到 `platform_ops.py` 统一入口：
- `batch_approve_api.py` → `platform_ops.py batch-approve`（合并客户端过滤逻辑）
- `auto_publish.py` 的 `check-visibility` → `platform_ops.py check-visibility`
- `auto_publish.py` 的 `retry-cos-failures` → `platform_ops.py retry-cos-failures`

---

## 七、问题联动关系图

```
C3 (db.py 乐观回填)
  └─→ 将未上传/已改名的 skill 标记为 synced
       └─→ H1 (check_banned_skills 404 判定)
            └─→ 404 的真实原因可能是 C2 (改名后原始 slug 失效)
                 └─→ 误判为 banned，标记 deleted_on_skillhub
                      └─→ 后续运维基于错误状态决策（可能删除本地文件）

C2 (改名 bug)
  └─→ 改名后的 skill 的 star 操作失败 (C1)
       └─→ 搜索排名无加分，前台不可见
            └─→ 触发 batch_republish_to_community 再次改名
                 └─→ 生成畸形 slug (foo-sk-sk1)，加剧封禁风险
```

**核心结论**: C1、C2、C3 三个 Critical 问题相互联动，构成了"改名 → star 失败 → 不可见 → 重试改名 → 畸形 slug → 封禁 → 误判 → 错误决策"的恶性循环。修复时需同步处理三个问题。

---

## 八、修复优先级建议

1. **P0（立即修复）**: C1 + C2 + C3 — 阻断误判放大链路
2. **P1（本周修复）**: H1 + H2 — 修正封禁检测方法论和审核过滤逻辑
3. **P2（下周修复）**: H3 + H4 + M1 + M2 — 清理冗余、统一 DB 更新逻辑
4. **P3（择机修复）**: M3 + L1 — 文档清理和异常处理
