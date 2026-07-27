# SkillHub 发布流程 7 项修复验证报告

**验证日期**: 2026-07-27
**验证范围**: d:\skills\tools\ 目录下的 5 个文件
**验证方法**: 代码审查 + 逻辑分析 + 边界条件检查

---

## 总览

| 编号 | 修复项 | 文件 | 验证结果 |
|------|--------|------|----------|
| C1 | current_slug 追踪 | platform_ops.py:1214 | 需改进 |
| C2 | 清除已有 -sk 后缀 | platform_ops.py:1261 | 通过 |
| C1 | 使用 actual_slug 而非原始 slug | enterprise_uploader.py:383 | 需改进 |
| C3 | 基于 platform_uploads 记录标记 synced | db.py:1373 | 需改进 |
| H1 | admin API 交叉验证 | platform_ops.py:1424 | 需改进 |
| H2 | 客户端二次过滤 | platform_ops.py:968 | 通过 |
| H3 | 移除 3 个废弃命令 | auto_publish.py | 通过 |
| H4 | 标记废弃并重定向 | batch_approve_api.py | 通过 |

**统计**: 通过 4 项 / 需改进 4 项 / 失败 0 项

---

## 1. C1 修复: publish_to_community 中的 current_slug 追踪

**文件**: `d:\skills\tools\platform_ops.py` 第 1269-1290 行

### 修复逻辑

```python
current_slug = slug
for suffix in ['-sk', '-sk1', '-sk2', '-sk3']:
    if current_slug.endswith(suffix):
        continue
    new_slug = base_slug + suffix
    rename_url = f".../admin/skills/{current_slug}/rename-slug"  # 使用 current_slug
    ...
    if rename_success:
        current_slug = new_slug  # 关键: 更新 current_slug
        ...
        retry_url = f".../admin/skills/{new_slug}/publish-to-community"
```

### 验证结果: 需改进

**正确的部分**:
- `current_slug = new_slug` 确保重命名成功后，下一次 rename API 调用使用的是平台上的最新 slug，而非原始 slug
- `if current_slug.endswith(suffix): continue` 正确跳过当前 slug 已有的后缀
- rename 和 publish 的 URL 都正确使用了 `current_slug` / `new_slug`

**遗漏的 edge case**:
1. **多次 rename 成功但所有 publish 均失败时，返回值丢失最终 slug**:
   - 场景: rename `foo` -> `foo-sk` (成功), publish `foo-sk` (失败) -> rename `foo-sk` -> `foo-sk1` (成功), publish `foo-sk1` (失败) -> ... 全部失败
   - 此时平台上 skill 的 slug 已变为 `foo-sk3`，但函数返回 `{'success': False, 'slug': slug}` (原始 slug `foo`)
   - 调用方无法知道 skill 已被重命名，导致本地 DB 与平台 slug 不一致
   - **建议**: 失败返回中应包含 `current_slug` 字段:
     ```python
     return {'success': False, 'slug': slug, 'final_slug': current_slug,
             'error': f'slug冲突且所有后缀均被占用: {err_str}'}
     ```

2. **unpublish 后未重试原始 slug 的 publish**:
   - Step 2a 执行了 `unpublish-from-community`，但之后直接进入 rename 流程，未尝试用原始 slug 重新 publish
   - 如果 409 冲突是因为同一 skill 已有社区发布记录（而非其他 skill 占用 slug），unpublish 后原始 slug 应该可以重新 publish
   - 当前逻辑会不必要地触发 rename

**新 bug 风险**: 低。核心追踪逻辑正确，仅失败路径的信息不完整。

---

## 2. C2 修复: 清除已有 -sk 后缀

**文件**: `d:\skills\tools\platform_ops.py` 第 1261-1273 行

### 修复逻辑

```python
base_slug = slug
for existing_suffix in ['-sk3', '-sk2', '-sk1', '-sk']:
    if base_slug.endswith(existing_suffix) and len(base_slug) > len(existing_suffix):
        base_slug = base_slug[:-len(existing_suffix)]
        break

current_slug = slug
for suffix in ['-sk', '-sk1', '-sk2', '-sk3']:
    ...
    new_slug = base_slug + suffix  # 基于清理后的 base_slug 生成
```

### 验证结果: 通过

**正确的部分**:
- 后缀检查顺序正确: `-sk3` -> `-sk2` -> `-sk1` -> `-sk`，长后缀优先匹配，避免 `-sk` 先于 `-sk3` 匹配
- `len(base_slug) > len(existing_suffix)` 防止 slug 本身就是后缀（如 slug="-sk"）导致空 base_slug
- `break` 确保只剥离一个后缀，不递归剥离
- `new_slug = base_slug + suffix` 基于清理后的 base 生成，避免了 `foo-sk` -> `foo-sk-sk1` 的畸形叠加

**边界条件验证**:
| 输入 slug | base_slug | 生成的 new_slug 候选 | 正确? |
|-----------|-----------|---------------------|-------|
| `foo` | `foo` | `foo-sk`, `foo-sk1`, `foo-sk2`, `foo-sk3` | 是 |
| `foo-sk` | `foo` | (跳过-sk), `foo-sk1`, `foo-sk2`, `foo-sk3` | 是 |
| `foo-sk2` | `foo` | `foo-sk`, `foo-sk1`, (跳过-sk2), `foo-sk3` | 是 |
| `a-sk` | `a` | (跳过-sk), `a-sk1`, `a-sk2`, `a-sk3` | 是 |
| `-sk` | `-sk` (不剥离) | (-sk-sk... 畸形但输入本身已畸形) | 可接受 |

**新 bug 风险**: 无。

---

## 3. C1 修复: _post_upload_publish 使用 actual_slug

**文件**: `d:\skills\tools\enterprise_uploader.py` 第 414-453 行

### 修复逻辑

```python
if ptc_result.get('success'):
    actual_slug = ptc_result.get('slug', slug)  # 改名后的新 slug
    was_renamed = ptc_result.get('original_slug') is not None
    star_result = star_skill(actual_slug)  # 使用实际 slug

    if was_renamed and actual_slug != slug:
        # 更新 skills 表 slug + platform_uploads
        conn.execute("UPDATE skills SET slug = ?, ... WHERE slug = ?", (actual_slug, slug))
        conn.execute("UPDATE platform_uploads SET ..., platform_slug = ? WHERE skill_id = (SELECT id FROM skills WHERE slug = ?)", (actual_slug, actual_slug))
```

### 验证结果: 需改进

**正确的部分**:
- `actual_slug = ptc_result.get('slug', slug)` 正确获取改名后的 slug
- `was_renamed = ptc_result.get('original_slug') is not None` 检测准确（publish_to_community 仅在改名时返回 `original_slug`）
- `star_skill(actual_slug)` 使用实际 slug 调用平台 API，正确
- 改名时更新 skills 表和 platform_uploads 表的 slug，正确

**遗漏的 edge case / 新 bug 风险**:

1. **slug UNIQUE 约束冲突被静默吞掉** (中风险):
   - skills 表定义了 `slug TEXT UNIQUE NOT NULL` (db.py 第 62 行)
   - 如果 `actual_slug` (如 `foo-sk`) 已存在于 skills 表中（例如之前某次操作的残留），`UPDATE skills SET slug = 'foo-sk' WHERE slug = 'foo'` 会抛出 `IntegrityError`
   - 整个 DB 更新块被 `except Exception: pass` 包裹（第 452 行），错误被完全静默
   - 调用方无法知道 DB 更新失败，star_skill 的平台调用已成功但本地记录未更新
   - **建议**: 至少记录 warning 日志，或在 result 中标记 DB 更新状态

2. **star_skill 的 JSON DB 更新对改名 slug 失效** (低风险):
   - `star_skill()` 内部调用 `load_db()` / `save_db()` 操作 JSON DB (upload_tracking.json)
   - JSON DB 中 skill 的 key 是原始 slug，但 `star_skill(actual_slug)` 用新 slug 查找: `if slug in db['skills']` 为 False
   - 结果: star API 平台调用成功，但 JSON DB 的 starred 状态未记录
   - SQLite DB 和 JSON DB 之间产生不一致
   - **建议**: star_skill 应接受 `original_slug` 参数用于 JSON DB 查找，或在调用方更新 JSON DB

3. **SQLite 和 JSON DB 双写不一致** (低风险):
   - `_post_upload_publish` 更新 SQLite DB (slug 字段、community_published)
   - `_update_db_community_published` (由 publish_to_community 调用) 更新 JSON DB (review_status、community_slug)
   - 改名后 SQLite 的 slug 已变，但 JSON DB 的 key 未变（仅记录 community_slug 字段）
   - 后续操作如果分别查不同 DB，可能得到不同的 slug

**新 bug 风险**: 中。UNIQUE 约束冲突的静默处理可能导致数据不一致且难以排查。

---

## 4. C3 修复: 基于 platform_uploads 记录标记 synced

**文件**: `d:\skills\tools\db.py` 第 1373-1402 行

### 修复逻辑

```python
# 仅当 platform_uploads 表中存在 success 记录时才标记为 synced
c.execute("""
    UPDATE skills SET skillhub_sync_status = 'synced'
    WHERE skillhub_sync_status = 'unknown'
    AND EXISTS (
        SELECT 1 FROM platform_uploads
        WHERE skill_id = skills.id
        AND platform = 'skillhub'
        AND upload_status = 'success'
    )
""")

# 未有上传记录但本地文件存在的, 标记为 pending_upload
c.execute("""
    UPDATE skills SET skillhub_sync_status = 'pending_upload'
    WHERE skillhub_sync_status = 'unknown'
    AND local_path IS NOT NULL AND local_path != ''
    AND (skill_type != 'source' OR skill_type IS NULL)
    AND NOT EXISTS (...)
""")
```

### 验证结果: 需改进

**正确的部分**:
- 从基于目录路径 (`local_path LIKE '%packaged-skills%skillhub%'`) 改为基于 `platform_uploads` 实际记录，根因修复准确
- `EXISTS` 子查询正确关联 `skill_id = skills.id` 和 `platform = 'skillhub'` 和 `upload_status = 'success'`
- 补充了 `pending_upload` 标记，让无上传记录但有本地文件的 skill 有明确状态
- `skill_type != 'source'` 排除源 skill，正确

**遗漏的 edge case**:

1. **历史误标数据未清理** (中风险):
   - 修复仅影响 `WHERE skillhub_sync_status = 'unknown'` 的记录
   - 之前被错误标记为 `synced` 的 912 个 skill（因目录路径匹配而误标）不会被自动纠正
   - 这些 skill 仍会被 `check_banned_skills` 纳入检查范围，可能产生误判
   - **建议**: 增加一个清理脚本，将无 platform_uploads success 记录但被标记为 synced 的 skill 重置为 `unknown` 或 `pending_upload`:
     ```sql
     UPDATE skills SET skillhub_sync_status = 'pending_upload'
     WHERE skillhub_sync_status = 'synced'
     AND NOT EXISTS (
         SELECT 1 FROM platform_uploads
         WHERE skill_id = skills.id AND platform = 'skillhub' AND upload_status = 'success'
     )
     AND local_path IS NOT NULL
     ```

2. **上传成功但 platform_uploads 记录缺失的 skill 会被误标为 pending_upload** (低风险):
   - 场景: 上传 API 调用成功，但写入 platform_uploads 表失败（网络错误、DB 锁等）
   - 这类 skill 会被标记为 `pending_upload`，可能导致重复上传
   - 但相比之前 912 个误标为 synced，这个方向的误判危害更小（重复上传 vs 误判封禁）

3. **upload_status 值的一致性** (低风险):
   - 修复依赖 `upload_status = 'success'` 的精确匹配
   - 如果存在其他表示成功的值（如 `'success_partial'`, `'completed'`），这些 skill 不会被标记为 synced
   - 需确认 platform_uploads.upload_status 的值域是否统一

**新 bug 风险**: 低。修复逻辑本身正确，主要问题是历史数据未清理。

---

## 5. H1 修复: check_banned_skills 中的 admin API 交叉验证

**文件**: `d:\skills\tools\platform_ops.py` 第 1424-1616 行

### 修复逻辑

对公开 API 返回 404 的 skill，使用 admin API 交叉验证:
- admin API 也失败 -> 确认 `banned`
- admin API 成功 + visibility != 'public' -> `never_published` (非封禁)
- admin API 成功 + visibility == 'public' + reviewStatus == 'pending' -> `pending_review` (非封禁)
- admin API 成功 + visibility == 'public' + 其他 -> `inconsistent` (异常)

### 验证结果: 需改进

**正确的部分**:
- 核心思路正确: 404 不等于封禁，需要交叉验证区分四种情况
- `admin_data.get('reviewStatus', admin_data.get('review_status', ''))` 同时兼容驼峰和下划线命名，防御性好
- DB 更新逻辑正确: 仅 `banned_slugs` 标记为 `deleted_on_skillhub`，`never_published_slugs` 仅标记 `community_published = 0`
- `never_published` 不改变 `current_status`，保持 `synced_from_skillhub`，正确

**遗漏的 edge case**:

1. **条件分支顺序导致 pending_review 分支近乎死代码** (中风险):
   ```python
   if visibility != 'public':        # 第一优先级
       never_published += 1
   elif review_status == 'pending':  # 第二优先级
       pending_review += 1
   ```
   - pending 状态的 skill 通常 visibility 不是 'public'（尚未发布到社区）
   - 因此 `visibility != 'public'` 先命中，pending skill 被归入 `never_published`
   - `elif review_status == 'pending'` 分支仅在 visibility == 'public' 且 reviewStatus == 'pending' 时触发（异常状态）
   - **影响**: `pending_review` 计数器几乎永远为 0，pending skill 被错误归类为 never_published
   - **DB 影响**: never_published_slugs 会执行 `community_published = 0`，对 pending skill 来说 community_published 本就不应为 1，所以无害但冗余
   - **建议**: 调整分支顺序:
     ```python
     if review_status == 'pending':
         pending_review += 1
     elif visibility != 'public':
         never_published += 1
     else:
         inconsistent += 1
     ```

2. **无 API 限流保护** (低风险):
   - 对每个 404 skill 发起 2 次 API 调用（公开 + admin）
   - 若有大量 404 skill（如 912 个），共 1824 次调用，无 sleep/限流
   - 可能触发 API 限流（429），导致 admin 验证失败，误判为 banned
   - 当前仅每 200 个打印进度，无延迟
   - **建议**: 每 50-100 个 404 skill 加入 `time.sleep(1)` 限流

3. **admin API 返回 403/401 时的处理** (低风险):
   - 如果 admin 认证过期，`_api_request` 返回 `(False, {...})`
   - 当前逻辑将 admin 失败等同于 "admin API 也返回错误 -> 确认封禁"
   - 但 403/401 是认证问题，不是 skill 不存在
   - 可能将所有 404 skill 误判为 banned
   - **建议**: 区分 admin API 的 404（确认封禁）和 403/401（认证失败，跳过判定）

**新 bug 风险**: 中。条件分支顺序问题和认证失败误判可能导致 banned 数量虚高。

---

## 6. H2 修复: batch_approve 中的客户端二次过滤

**文件**: `d:\skills\tools\platform_ops.py` 第 988-1007 行

### 修复逻辑

```python
# H2修复: reviewStatus=pending API过滤器可能不生效, 需客户端二次过滤
for sk in data.get('skills', []):
    slug = sk.get('slug', '')
    rs = sk.get('reviewStatus', sk.get('review_status', ''))
    if slug and rs == 'pending':
        slugs.append(slug)
    elif slug and rs != 'pending':
        pass  # API过滤器未生效, 跳过非pending
```

### 验证结果: 通过

**正确的部分**:
- 客户端二次过滤确保仅审核 `reviewStatus == 'pending'` 的 skill，即使 API 过滤器失效
- `sk.get('reviewStatus', sk.get('review_status', ''))` 兼容驼峰和下划线命名
- `slug and rs == 'pending'` 同时检查 slug 非空和状态匹配
- `elif` 分支虽为 `pass`（空操作），但注释清晰说明意图

**边界条件验证**:
| API 返回的 reviewStatus | 客户端过滤结果 | 正确? |
|------------------------|---------------|-------|
| 'pending' | 加入审核列表 | 是 |
| 'approved' | 跳过 | 是 |
| 'rejected' | 跳过 | 是 |
| '' (空) | 跳过 | 是 |
| None | 跳过 (get 返回 '') | 是 |
| 'Pending' (大写) | 跳过 (大小写敏感) | 可接受 |

**轻微注意**:
- 分页计算 `pages = (total // 100) + 1` 在 total 为 100 的整数倍时会多请求一页（如 total=100 时请求 2 页，第 2 页为空），但无害
- 大小写敏感: 如果 API 返回 'Pending' 而非 'pending'，会被跳过。但 API 通常返回小写，风险极低

**新 bug 风险**: 无。

---

## 7. H3 修复: auto_publish.py 移除 3 个废弃命令

**文件**: `d:\skills\tools\auto_publish.py`

### 修复逻辑

移除的 3 个命令:
1. `batch-public-publish` -> 重定向到 `platform_ops.py batch-republish`
2. `gen-community-publish-js` -> 重定向到 `platform_ops.py batch-republish`
3. `sync-platform-status` -> `batch_republish_to_community` 已自动同步 DB

### 验证结果: 通过

**正确的部分**:
- `main()` 函数的命令分发中已完全移除这 3 个命令的 `elif` 分支
- 文件中无对应的函数定义（`batch_public_publish`、`gen_community_publish_js`、`sync_platform_status`）
- docstring 中保留了废弃说明和重定向指引（第 18-21 行），用户友好
- 未知命令会进入 `else` 分支打印帮助信息

**当前 main() 支持的命令**:
- `publish-skillhub` - 上传到 SkillHub
- `auto-flow` - 完整自动化流程
- `check-status` - 检查状态
- `retry-rejected` - 重试被拒绝的 skill
- `retry-cos-failures` - 生成 COS 失败重试脚本
- `check-visibility` - 检查可见性状态

**新 bug 风险**: 无。向后兼容性通过 docstring 中的重定向指引处理。

---

## 8. H4 修复: batch_approve_api.py 标记废弃并重定向

**文件**: `d:\skills\tools\batch_approve_api.py`

### 修复逻辑

```python
warnings.warn(
    "batch_approve_api.py 已废弃,请使用 platform_ops.py batch-approve",
    DeprecationWarning,
    stacklevel=2
)

def _redirect():
    from platform_ops import batch_approve
    # 支持 --check, --slug <slug>, 无参数(批量) 三种模式
    ...
```

### 验证结果: 通过

**正确的部分**:
- 文件头部有完整的废弃说明（docstring），包含重定向命令和废弃原因
- `warnings.warn(DeprecationWarning)` 在模块导入时即发出警告
- `_redirect()` 函数将所有调用转发到 `platform_ops.batch_approve`
- 支持三种调用模式:
  - `--check`: 检查待审核数量（调用 `batch_approve(slugs=[], delay=0)`）
  - `--slug <slug>`: 审核单个 skill
  - 无参数: 批量审核所有 pending
- `if __name__ == '__main__'` 入口先打印废弃提示再执行重定向

**轻微注意**:
- `--check` 模式调用 `batch_approve(slugs=[], delay=0)`，传入空列表。batch_approve 中 `if not slugs: return {'success': True, 'approved': 0, ...}`，会直接返回。但 `total_pending` 字段不在返回值中（batch_approve 返回 `approved` 和 `failed`），所以 `result.get('total_pending', 0)` 总是返回 0。这是一个小 bug -- `--check` 功能实际上无法获取待审核数量。
  - **建议**: `--check` 应直接调用 admin API 查询 pending 数量，或调用 batch_approve 中获取 pending 列表的逻辑

**新 bug 风险**: 低。`--check` 功能不完善但不影响主流程。

---

## 综合风险评估

### 高优先级改进项 (建议尽快处理)

1. **C1 (enterprise_uploader.py)**: slug UNIQUE 约束冲突被 `except Exception: pass` 静默吞掉。建议至少添加日志记录，以便排查 DB 更新失败的情况。

2. **H1 (platform_ops.py)**: 条件分支顺序导致 `pending_review` 分支近乎死代码。建议将 `review_status == 'pending'` 检查提前到 `visibility != 'public'` 之前。

3. **C3 (db.py)**: 历史误标为 synced 的 912 个 skill 未被清理。建议增加清理脚本重置无实际上传记录的 synced 状态。

### 中优先级改进项

4. **C1 (platform_ops.py)**: 多次 rename 成功但 publish 全部失败时，返回值丢失最终 slug。建议在失败返回中包含 `final_slug`。

5. **H1 (platform_ops.py)**: admin API 认证失败（403/401）被误判为 "确认封禁"。建议区分 404 和认证错误。

6. **H4 (batch_approve_api.py)**: `--check` 模式无法获取待审核数量（`total_pending` 字段不存在）。建议直接查询 admin API。

### 低优先级改进项

7. **C1 (enterprise_uploader.py)**: star_skill 的 JSON DB 更新对改名 slug 失效。建议 star_skill 接受 original_slug 参数。

8. **H1 (platform_ops.py)**: 无 API 限流保护，大量 404 skill 时可能触发 429。

---

## 结论

7 项修复（含 C1 在两个文件中的两处修复，共 8 处验证点）整体质量良好，核心修复逻辑均正确无误。4 项通过，4 项需改进，0 项失败。需改进项的问题集中在 edge case 处理和错误信息完整性上，不影响主流程的正确性，但可能在特定场景下导致数据不一致或误判。建议优先处理 3 个高优先级改进项。
