# SkillHub 发布流程分析报告

## 分析范围

| 文件 | 关键函数 | 上传机制 | 数据库 |
|------|----------|----------|--------|
| `platform_ops.py` | `publish_to_community`, `auto_publish`, `batch_approve` | Admin API (HTTP) | JSON (`upload_tracking.json`) |
| `enterprise_uploader.py` | `upload_skill` | HTTP POST FormData | SQLite (`DB_PATH`) |
| `version_sync_pipeline.py` | `sync_to_skillhub`, `sync_skill_to_all_platforms` | `skillhub` CLI | SQLite (`DB_PATH`) |
| `auto_publish.py` (遗留) | `publish_to_skillhub`, `auto_flow`, `generate_community_publish_js` | CLI + 浏览器JS | JSON (`upload_tracking.json`) |
| `community_publish.js` (遗留) | 浏览器端发布脚本 | 浏览器fetch | 无 |
| `batch_approve_api.py` (遗留) | `batch_approve_all` | Admin API (HTTP) | 无 |

---

## 一、各文件发布流程问题列表

### 1. `platform_ops.py` — `publish_to_community` (第1208-1275行)

#### 问题 1.1 [严重] rename 循环中的 slug 陈旧 BUG

**位置**: 第1256-1274行

```python
for suffix in ['-sk', '-sk1', '-sk2', '-sk3']:
    if slug.endswith(suffix):
        continue
    new_slug = slug + suffix
    rename_url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills/{slug}/rename-slug"
    # ^^^ 始终使用原始 slug
    rename_body = json.dumps({'newSlug': new_slug}).encode('utf-8')
    rename_success, rename_result = _api_request('PUT', rename_url, headers, data=rename_body, timeout=15)

    if rename_success:
        time.sleep(0.2)
        retry_url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills/{new_slug}/publish-to-community"
        retry_success, retry_result = _api_request('POST', retry_url, headers, data=body, timeout=30)
        if retry_success:
            _update_db_community_published(slug, new_slug)
            return {'success': True, ...}
        # publish失败,继续尝试下一个后缀  <--- BUG在此
    # rename失败(409=已占用),继续尝试下一个后缀
```

**问题描述**: 当第一次 rename 成功 (slug -> slug-sk) 但 publish 失败时，循环继续尝试下一个后缀 `-sk1`。但此时平台上该 skill 的 slug 已经变成了 `slug-sk`，而 `rename_url` 仍然使用原始 `slug`。由于原始 slug 已不存在于平台，后续所有 rename 请求 (到 -sk1, -sk2, -sk3) 都会失败。

**影响**: rename 成功但 publish 失败的 skill 会处于一个"半改名"状态——平台上 slug 已变，但本地 DB 仍记录原始 slug，且社区发布未完成。后续重试也无法成功。

#### 问题 1.2 [中等] unpublish 结果未检查

**位置**: 第1251-1253行

```python
unpub_url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills/{slug}/unpublish-from-community"
_api_request('POST', unpub_url, headers, data=b'{}', timeout=15)
time.sleep(0.2)
```

**问题描述**: `unpublish-from-community` 的返回值被完全忽略。如果 unpublish 失败 (认证过期、skill 从未发布过、网络错误等)，rename + publish 流程仍会继续执行，可能导致不可预期的状态。

#### 问题 1.3 [中等] unpublish 的必要性未区分场景

**位置**: 第1245-1253行

**问题描述**: 409 slug_conflict 有两种可能:
- **场景A**: 自己之前已用该 slug 发布到社区 -> unpublish 有意义
- **场景B**: 另一个 org/skill 已占用该 slug -> unpublish 自己的 skill 无意义，反而可能取消已有的社区发布

代码没有区分这两种场景，统一执行 unpublish，在场景B中会造成误操作。

#### 问题 1.4 [低] 没有前置状态检查

**位置**: 第1237-1239行

**问题描述**: `publish_to_community` 直接尝试 publish-to-community API，没有先检查 skill 是否处于 `published` 状态 (已审核通过)。如果 skill 还在 `pending` 状态，publish-to-community 很可能失败，但错误信息可能不清晰。

---

### 2. `platform_ops.py` — `auto_publish` (第1295-1363行)

#### 问题 2.1 [严重] batch_approve 后立即 publish_to_community，未等待平台状态同步

**位置**: 第1330-1344行

```python
if review_status == 'pending':
    approve_result = batch_approve([slug])
    if approve_result.get('success') and slug in approve_result.get('approved', []):
        review_status = 'published'  # 本地立即更新
    # ...

if review_status in ('published', 'approved', 'public_published'):
    if visibility != 'public' or not front_visible:
        pub_result = publish_to_community(slug)  # 立即调用，可能平台尚未同步
```

**问题描述**: `batch_approve` 成功后，本地立即将 `review_status` 设为 `published`，然后马上调用 `publish_to_community`。但 SkillHub 平台的审核状态更新可能是异步的——API 返回成功只表示请求已接受，不代表平台已完成状态转换。如果平台尚未完成 approve 处理，publish-to-community 会失败。

#### 问题 2.2 [严重] rename 后的 slug 未传播到后续操作

**位置**: 第1344-1356行

```python
pub_result = publish_to_community(slug)
result['steps']['publish_to_community'] = pub_result
if pub_result.get('success'):
    visibility = 'public'
    front_visible = True
# ...

# Step 4: 收藏
if not status.get('db_starred'):
    star_result = star_skill(slug)  # 仍使用原始 slug!
```

**问题描述**: 如果 `publish_to_community` 执行了 rename (slug -> slug-sk)，返回结果中 `pub_result['slug']` 是新 slug。但 `auto_publish` 没有读取这个新 slug，后续的 `star_skill(slug)` 仍使用原始 slug，而平台上该 skill 的 slug 已经改变，star 操作会失败。

#### 问题 2.3 [低] 已 public_published 的 skill 仍可能触发不必要的 publish

**位置**: 第1341行

```python
if review_status in ('published', 'approved', 'public_published'):
    if visibility != 'public' or not front_visible:
```

**问题描述**: 如果 skill 已经是 `public_published` 但 `visibility` 查询返回非 `public` (可能是 API 返回值不一致或缓存问题)，会触发不必要的 publish_to_community 调用。

---

### 3. `platform_ops.py` — `batch_approve` (第968-1037行)

#### 问题 3.1 [低] 自动获取 pending 列表时未二次过滤

**位置**: 第988-1001行

```python
slugs = []
pages = (total // 100) + 1
for page in range(1, pages + 1):
    url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills?reviewStatus=pending&page={page}&pageSize=100"
    success, data = _api_request('GET', url, headers)
    for sk in data.get('skills', []):
        slug = sk.get('slug', '')
        if slug:
            slugs.append(slug)
```

**问题描述**: 与 `batch_approve_api.py` 中的注释 ("API的reviewStatus过滤器不生效，需二次过滤") 对比，`platform_ops.py` 的 `batch_approve` 依赖 `reviewStatus=pending` 过滤器，没有做二次过滤。如果该过滤器确实不生效，会审核到非 pending 状态的 skill。

#### 问题 3.2 [低] 分页计算可能遗漏

**位置**: 第990行

```python
pages = (total // 100) + 1
```

**问题描述**: 当 `total` 正好是 100 的整数倍时 (如 total=200)，`pages = 200//100 + 1 = 3`，会多扫描一页 (空页)，虽然不会出错但效率略低。更严重的是，如果 total 在扫描过程中变化 (有新 skill 进入 pending)，可能遗漏部分 skill。

---

### 4. `enterprise_uploader.py` — `upload_skill` (第383-675行)

#### 问题 4.1 [严重] 完全没有调用 publish_to_community 和 batch_approve

**问题描述**: `enterprise_uploader.py` 的 `upload_skill` 函数仅执行 HTTP POST 上传到 `/orgs/{ORG_ID}/skills`。虽然 payload 中设置了 `visibility: 'public'` (第516行)，但根据 SkillHub 平台生命周期模型:

```
not_uploaded -> pending -> published -> public_published
```

上传后 skill 处于 `pending` 状态，需要:
1. `batch_approve` 审核通过 -> `published`
2. `publish_to_community` 设置 visibility=public -> `public_published`

`enterprise_uploader.py` 两个步骤都没有调用，上传的 skill 会停留在 pending 状态，无法在前台可见。payload 中的 `visibility: 'public'` 并不会自动触发社区发布。

**影响**: 通过 `enterprise_uploader.py` 上传的 skill 需要手动运行 `platform_ops.py batch-approve` 和 `platform_ops.py publish-community` 才能完成发布，流程不完整。

#### 问题 4.2 [中等] 质量门控逻辑与 version_sync_pipeline.py 重复且不一致

**位置**: 第411-452行

**问题描述**: `enterprise_uploader.py` 独立实现了质量门控检查 (评分门控 + 营销关卡 + 安全预检 + 防幻觉)，与 `version_sync_pipeline.py` 的 `sync_skill_to_all_platforms` 中的检查 (第969-1102行) 高度重叠。两处实现存在差异:
- `enterprise_uploader.py`: 评分门控失败返回详细 `rating_gate` 对象
- `version_sync_pipeline.py`: 评分门控失败返回 `failed_checks` 字符串列表
- 安全预检的严重级别判断逻辑不同 (enterprise_uploader 只阻断 critical，version_sync_pipeline 也只阻断 critical，但 warning 输出不同)

#### 问题 4.3 [低] WAF 重试逻辑仅存在于此文件

**位置**: 第598-664行

**问题描述**: `enterprise_uploader.py` 有完整的两级 WAF 重试策略 (截断 content -> base64 编码)，但 `version_sync_pipeline.py` 使用 CLI 上传时没有类似处理。如果 CLI 遇到 WAF 拦截，没有重试机制。

---

### 5. `version_sync_pipeline.py` — `sync_to_skillhub` + `sync_skill_to_all_platforms`

#### 问题 5.1 [严重] 缺少 batch_approve 步骤

**位置**: 第1122-1167行

```python
# 8. SkillHub同步
if not skip_skillhub:
    sh_result = sync_to_skillhub(slug, skill_md, new_version, skill_id, is_paid)
    free_upload = sh_result.get('free_upload') or {}
    free_status = free_upload.get('status', 'unknown')
    if free_status == 'success':
        # 8.5 发布到社区 (publish-to-community)
        # ^^^ 直接调用 publish_to_community，跳过了 batch_approve!
        from platform_ops import publish_to_community
        ptc_result = publish_to_community(slug)
```

**问题描述**: `sync_to_skillhub` 使用 `skillhub publish` CLI 上传后，skill 在平台上处于 `pending` 状态。`sync_skill_to_all_platforms` 直接调用 `publish_to_community`，但跳过了 `batch_approve` 步骤。在 pending 状态下调用 publish-to-community 很可能失败，因为 skill 尚未通过审核。

**正确流程应为**: CLI上传 -> batch_approve -> publish_to_community

#### 问题 5.2 [严重] publish_to_community 仅在 free_upload 成功时调用

**位置**: 第1130行

```python
if free_status == 'success':
    # 才调用 publish_to_community
```

**问题描述**: 当 CLI 上传返回 `version_exists` (版本已存在) 时，skill 可能已经在平台上且处于 `published` 状态，但仍未发布到社区。此时跳过 `publish_to_community` 会导致 skill 永远无法获得社区可见性。

#### 问题 5.3 [严重] rename 后的 slug 未更新到本地 DB

**位置**: 第1138-1156行

```python
ptc_result = publish_to_community(slug)
result['phases']['publish_to_community'] = ptc_result
if ptc_result.get('success'):
    # 更新DB的community_published状态
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("UPDATE platform_uploads SET community_published = 1 ...")
    conn.execute("UPDATE skills SET skillhub_sync_status = 'synced' ...")
```

**问题描述**: 如果 `publish_to_community` 执行了 rename (slug -> slug-sk)，`ptc_result` 中包含新 slug，但 `version_sync_pipeline.py` 没有将新 slug 更新到 SQLite DB 的 `skills` 表。后续同步操作 (如 ClawHub 同步、版本检测) 仍会使用原始 slug，而 SkillHub 上的 slug 已改变，导致无法正确匹配。

#### 问题 5.4 [中等] 直接操作 SQLite 而非通过统一接口

**位置**: 第1144-1156行

**问题描述**: 直接执行 SQL UPDATE 语句更新 `community_published` 和 `skillhub_sync_status`，绕过了 `platform_ops.py` 中的 `_update_db_community_published` 函数。这导致:
- SQLite DB (`platform_uploads` 表) 被更新
- JSON DB (`upload_tracking.json`) 未被更新
- 两个数据库的社区发布状态不一致

#### 问题 5.5 [中等] 使用 CLI 而非 API 上传，与 enterprise_uploader.py 不一致

**位置**: 第717行

```python
cli_cmd = f'skillhub publish "{skill_dir}" --changelog "Auto-sync v{new_version}"'
```

**问题描述**: `version_sync_pipeline.py` 使用 `skillhub publish` CLI 命令上传，而 `enterprise_uploader.py` 使用 HTTP POST FormData 直接调用 API。两种方式的行为差异:
- CLI: 无法设置 categoryIds、iconUrl、subCategories 等营销参数
- CLI: 无法设置 visibility、billingType 等字段
- CLI: WAF 拦截无重试机制
- API: 可以完整控制 payload，有 WAF 重试

同一项目的两个上传入口使用不同机制，容易导致上传的 skill 元数据不一致。

---

## 二、需要修复的具体位置

| 编号 | 文件 | 行号 | 问题 | 优先级 |
|------|------|------|------|--------|
| F1 | `platform_ops.py` | 1256-1274 | rename 循环中 slug 陈旧，需追踪当前 slug | P0 |
| F2 | `platform_ops.py` | 1251-1253 | unpublish 结果未检查 | P1 |
| F3 | `platform_ops.py` | 1330-1344 | batch_approve 后未等待平台同步就调用 publish | P0 |
| F4 | `platform_ops.py` | 1344-1356 | rename 后 star_skill 仍用原始 slug | P0 |
| F5 | `enterprise_uploader.py` | 383-675 | upload_skill 未调用 batch_approve 和 publish_to_community | P0 |
| F6 | `version_sync_pipeline.py` | 1130-1139 | 缺少 batch_approve 步骤 | P0 |
| F7 | `version_sync_pipeline.py` | 1130 | publish_to_community 仅在 free_upload 成功时调用 | P1 |
| F8 | `version_sync_pipeline.py` | 1138-1156 | rename 后 slug 未更新到 DB | P0 |
| F9 | `version_sync_pipeline.py` | 1144-1156 | 直接操作 SQLite，未同步 JSON DB | P1 |
| F10 | `version_sync_pipeline.py` | 717 | CLI 上传无营销参数，与 enterprise_uploader 不一致 | P2 |
| F11 | `platform_ops.py` | 988-1001 | batch_approve 未二次过滤 pending 列表 | P2 |

---

## 三、冗余/碎片化功能列表

### 3.1 publish-to-community 逻辑存在 3 份实现

| 实现 | 文件 | 机制 | 状态 |
|------|------|------|------|
| `publish_to_community()` | `platform_ops.py:1208` | Python API 调用 | 活跃 (统一入口) |
| `generate_community_publish_js()` | `auto_publish.py:348` | 生成浏览器 JS 脚本 | 遗留 (注释说已收口但文件仍在) |
| 浏览器脚本 | `community_publish.js` | 直接浏览器 fetch | 遗留 (独立文件) |

**冲突点**: 三份实现的 rename 后缀策略不同:
- `platform_ops.py`: 尝试 `-sk`, `-sk1`, `-sk2`, `-sk3` (4个后缀)
- `community_publish.js`: 只尝试 `-sk` (1个后缀)
- `auto_publish.py` 生成的 JS: 尝试 `-sk`, `-sk1`, `-sk2` (3个后缀)

### 3.2 batch_approve 逻辑存在 2 份实现

| 实现 | 文件 | 状态 |
|------|------|------|
| `batch_approve()` | `platform_ops.py:968` | 活跃 (统一入口) |
| `batch_approve_all()` | `batch_approve_api.py:87` | 遗留 (独立脚本，含断点续传功能) |

**冲突点**: `batch_approve_api.py` 有断点续传 (progress_file) 和二次过滤逻辑，`platform_ops.py` 的 `batch_approve` 没有这些功能。

### 3.3 SkillHub 上传逻辑存在 3 份实现

| 实现 | 文件 | 机制 | 营销参数 | WAF 重试 |
|------|------|------|----------|----------|
| `upload_skill()` | `enterprise_uploader.py:383` | HTTP POST FormData | 完整 (categoryIds, iconUrl, subCategories) | 两级重试 |
| `sync_to_skillhub()` | `version_sync_pipeline.py:687` | `skillhub publish` CLI | 无 | 无 |
| `publish_to_skillhub()` | `auto_publish.py:101` | `skillhub publish` CLI (另一套) | 无 | 无 |

### 3.4 auto_flow / auto_publish 逻辑存在 2 份实现

| 实现 | 文件 | 机制 |
|------|------|------|
| `auto_publish()` | `platform_ops.py:1295` | API 直调 (approve + publish + star) |
| `auto_flow()` | `auto_publish.py:206` | CLI 上传 + JS 脚本生成 (浏览器端发布) |

### 3.5 常量定义分散在 4 个文件中

| 常量 | enterprise_uploader.py | platform_ops.py | auto_publish.py | version_sync_pipeline.py |
|------|----------------------|-----------------|-----------------|------------------------|
| ORG_ID (862) | `ORG_ID = 862` (行43) | `_ADMIN_ORG_ID = 862` (行99) | `ADMIN_ORG_ID = 862` (行66) | 无 (从 platform_ops 获取) |
| API_BASE | `API_BASE` (行44) | `_API_BASE` (行98) | `ADMIN_API_HOST` (行65) | 无 |
| PUBLISHER_ID (742) | 无 | `_ADMIN_PUBLISHER_ID` (行1206) | `ADMIN_PUBLISHER_ID` (行67) | 无 |
| WAF 限制 (5800) | 无 (用不同方式处理) | 无 | `MAX_CONTENT_LENGTH = 5800` (行60) | `SKILLHUB_MAX_CONTENT = 5800` (行88) |

### 3.6 质量门控检查重复实现

| 检查项 | enterprise_uploader.py | version_sync_pipeline.py |
|--------|----------------------|------------------------|
| 评分门控 | `run_rating_gate()` (行413) | `run_rating_gate_check()` (行1025) |
| 营销关卡 | `run_marketing_gate()` (行422) | `run_marketing_gate_check()` (行1038) |
| 安全预检 | `run_security_precheck()` (行437) | `run_security_precheck()` (行1001) |
| 防幻觉 | `run_anti_hallucination()` (行447) | `run_anti_hallucination_check()` (行1052) |

注意: 函数名不同 (`run_rating_gate` vs `run_rating_gate_check`)，但功能重叠。

### 3.7 两个数据库追踪同一发布状态

| 数据库 | 使用文件 | 追踪内容 |
|--------|----------|----------|
| SQLite (`DB_PATH`) | `enterprise_uploader.py`, `version_sync_pipeline.py` | `platform_uploads.community_published`, `skills.skillhub_sync_status` |
| JSON (`upload_tracking.json`) | `platform_ops.py`, `auto_publish.py` | `skills[slug].skillhub.review_status`, `skills[slug].skillhub.public_published` |

两个数据库独立更新，互不同步。`publish_to_community` 更新 JSON DB，`version_sync_pipeline.py` 更新 SQLite DB，导致状态不一致。

---

## 四、建议的修复方案

### 方案 1: 修复 `publish_to_community` 的 rename 循环 BUG (F1)

```python
# platform_ops.py 第1256-1274行 修改为:
current_slug = slug  # 追踪当前 slug
for suffix in ['-sk', '-sk1', '-sk2', '-sk3']:
    if current_slug.endswith(suffix):
        continue
    new_slug = slug + suffix  # 新 slug 基于原始 slug，避免叠加
    rename_url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills/{current_slug}/rename-slug"
    # ^^^ 使用 current_slug 而非 slug
    rename_body = json.dumps({'newSlug': new_slug}).encode('utf-8')
    rename_success, rename_result = _api_request('PUT', rename_url, headers, data=rename_body, timeout=15)

    if rename_success:
        current_slug = new_slug  # 更新当前 slug
        time.sleep(0.2)
        retry_url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills/{new_slug}/publish-to-community"
        retry_success, retry_result = _api_request('POST', retry_url, headers, data=body, timeout=30)
        if retry_success:
            _update_db_community_published(slug, new_slug)
            return {'success': True, 'slug': new_slug, 'original_slug': slug, ...}
    # rename失败,继续尝试下一个后缀
```

### 方案 2: 修复 `auto_publish` 的 slug 传播问题 (F3, F4)

```python
# platform_ops.py auto_publish 函数中, Step 3 修改为:
if review_status in ('published', 'approved', 'public_published'):
    if visibility != 'public' or not front_visible:
        pub_result = publish_to_community(slug)
        result['steps']['publish_to_community'] = pub_result
        if pub_result.get('success'):
            # 使用返回的新 slug (如果有 rename)
            actual_slug = pub_result.get('slug', slug)
            visibility = 'public'
            front_visible = True
        # ...

    # Step 4: 收藏 — 使用 actual_slug
    actual_slug = pub_result.get('slug', slug) if pub_result else slug
    if not status.get('db_starred'):
        star_result = star_skill(actual_slug)  # 使用可能改名后的 slug
```

### 方案 3: 修复 `version_sync_pipeline.py` 缺少 batch_approve (F6)

```python
# version_sync_pipeline.py 第1130行后添加:
if free_status == 'success':
    print(f"  ✓ SkillHub同步成功")

    # 8.4 审核通过 (新增步骤)
    print(f"  [5.4/7] 审核通过...")
    try:
        from platform_ops import batch_approve
        approve_result = batch_approve([slug])
        result['phases']['batch_approve'] = approve_result
        if not approve_result.get('success'):
            print(f"  ⚠ 审核未通过,跳过社区发布")
            # 审核失败不阻断后续流程,但跳过 publish_to_community
        else:
            time.sleep(1)  # 等待平台状态同步
    except ImportError:
        print(f"  ⚠ platform_ops模块不可用,跳过审核")

    # 8.5 发布到社区
    if result['phases'].get('batch_approve', {}).get('success'):
        from platform_ops import publish_to_community
        ptc_result = publish_to_community(slug)
        # ...
```

### 方案 4: 修复 `enterprise_uploader.py` 缺少发布步骤 (F5)

在 `enterprise_uploader.py` 的 `upload_skill` 函数成功返回前，添加可选的审核+社区发布步骤:

```python
# enterprise_uploader.py upload_skill 函数末尾, return 成功结果前添加:
if response_data and not dry_run:
    # 可选: 自动审核+社区发布
    auto_publish_to_community = os.environ.get('SKILLHUB_AUTO_PUBLISH', '0') == '1'
    if auto_publish_to_community:
        try:
            from platform_ops import batch_approve, publish_to_community
            batch_approve([slug])
            time.sleep(1)
            pub_result = publish_to_community(slug)
            # 更新返回结果
            response_data['community_published'] = pub_result.get('success', False)
        except ImportError:
            pass
```

### 方案 5: 统一 slug 传播到 DB (F8)

```python
# version_sync_pipeline.py 第1138行后添加:
ptc_result = publish_to_community(slug)
result['phases']['publish_to_community'] = ptc_result
if ptc_result.get('success'):
    actual_slug = ptc_result.get('slug', slug)  # 可能为改名后的 slug
    original_slug = ptc_result.get('original_slug', slug)

    # 如果 slug 被改名,更新 SQLite DB
    if actual_slug != slug:
        try:
            conn = sqlite3.connect(str(DB_PATH))
            conn.execute("UPDATE skills SET slug = ? WHERE slug = ?", (actual_slug, slug))
            conn.execute("UPDATE platform_uploads SET slug = ? WHERE slug = ?", (actual_slug, slug))
            conn.commit()
            conn.close()
        except Exception:
            pass

    # 更新 community_published 状态
    # ...
```

### 方案 6: 长期架构重构 — 消除碎片化

1. **统一上传入口**: 所有 SkillHub 上传统一通过 `enterprise_uploader.py` 的 HTTP API 方式 (支持完整营销参数 + WAF 重试)，废弃 `version_sync_pipeline.py` 中的 CLI 方式和 `auto_publish.py` 中的 `publish_to_skillhub`。

2. **统一发布流程**: 所有社区发布统一通过 `platform_ops.py:publish_to_community`，废弃 `auto_publish.py:generate_community_publish_js` 和 `community_publish.js`。

3. **统一数据库**: 合并 SQLite 和 JSON 数据库为单一数据源，或建立明确的同步机制。建议以 SQLite 为权威源，JSON DB 作为缓存层。

4. **统一常量**: 创建 `config/skillhub_config.py`，集中定义 ORG_ID、API_BASE、PUBLISHER_ID、WAF 限制等常量，所有文件从该模块导入。

5. **统一质量门控**: 创建 `quality_gate_pipeline.py`，封装完整的门控流程 (评分+营销+安全+防幻觉)，所有上传入口调用同一函数。

6. **删除遗留文件**: `auto_publish.py`、`community_publish.js`、`batch_approve_api.py` 的功能已被 `platform_ops.py` 收口，应删除或标记为 deprecated。

---

## 五、发布流程正确性总结

### 当前状态: 流程碎片化，存在多个 BUG

```
enterprise_uploader.py:    上传 -> [结束]  (缺少 approve + publish_to_community)
version_sync_pipeline.py:  上传 -> publish_to_community  (缺少 approve, slug 未传播)
platform_ops.py auto_publish: approve -> publish_to_community  (slug 未传播, 未等待同步)
platform_ops.py publish_to_community: publish -> [409] -> unpublish -> rename -> publish  (rename 循环 BUG)
```

### 期望状态: 统一的完整发布流程

```
上传 (HTTP API) -> batch_approve -> 等待同步 -> publish_to_community -> slug 传播到 DB -> star
                                              (含 unpublish -> rename -> publish 冲突处理)
```
