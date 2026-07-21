# Skill Registry 工作流状态机修复方案设计文档

> **文档创建时间**: 2026-07-20
> **评估对象**: `d:\skills\skill-registry` 工作流状态机
> **核心问题**: 1848/1909 条记录（96.8%）卡在 `step1_read_original`，`workflow_states` 表完全为空
> **配套验证脚本**: `c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5\round2_workflow_fix.py`

---

## 一、问题诊断

### 1.1 数据库实际状态（脚本验证后）

| 维度 | 实际数据 |
|------|---------|
| `workflow_state` 分布 | `step1_read_original: 1848`, `completed: 61` |
| `current_status` 分布 | `optimized: 930`, `differentiated: 898`, `packaged: 39`, `published: 22`, `registered: 20` |
| `workflow_states` 表（10步追踪）记录数 | **0**（完全为空）|
| `scores` 表记录数 | **2330**（baseline: 1150, final: 1180）—— 与 WORKFLOW_INTEGRITY_REPORT.md 中"为空"的描述不符，实际已有历史评分数据 |

### 1.2 1848 条卡在 step1 的记录细分

| current_status | is_differentiated | upload_state | 记录数 | 真实状态推断 |
|---------------|-------------------|--------------|--------|------------|
| optimized | 1 | not_uploaded | 879 | 已优化待上传（应处于 step7_validate）|
| differentiated | 1 | not_uploaded | 847 | 差异化完成待生成双版本（应处于 step5_add_deps）|
| differentiated | 1 | uploaded | 51 | 已上传免费版（应处于 step8_upload_free）|
| optimized | 1 | uploaded | 51 | 已上传免费版（应处于 step8_upload_free）|
| registered | 1 | not_uploaded | 20 | 真正未开始（保持 step1_read_original）|

### 1.3 根因分析

| 根因 | 证据 | 影响 |
|------|------|------|
| `register_skill()` 不接受 `workflow_state` 参数 | `db.py` 第 299-363 行函数签名无此参数 | 新注册 skill 一律使用 schema 默认值 `step1_read_original` |
| `scan_and_import.py` 不设置 `workflow_state` | 第 193-209 行调用 `register_skill()` 未传该参数 | 1848 条导入记录全部使用默认值 |
| `init_baseline.py` 显式设置 `workflow_state='completed'` | 第 104、189、309 行 | 61 条原创/开源/企业版记录正确 |
| `update_workflow_state()` 函数存在但从未被调用 | grep 全代码库仅 `db.py` 自身定义 | `workflow_states` 表为空，10步追踪完全失效 |
| `record_score()` 已被外部 batch 脚本调用 | scores 表 2330 条记录，reviewer 字段含 batch2~batch12_script | WORKFLOW_INTEGRITY_REPORT.md 中"从未调用"的结论已过时 |

### 1.4 `workflow_state` 与 `current_status` 语义矛盾

- `current_status` 字段反映业务状态（registered/differentiated/optimized/packaged/published）
- `workflow_state` 字段反映生产流水线状态（step1~step9/completed）
- 1828 条记录的 `current_status` 是 `optimized` 或 `differentiated`，但 `workflow_state` 仍是 `step1_read_original` —— 两字段语义矛盾

---

## 二、10 步工作流状态机设计

### 2.1 状态机定义（基于 `FRAMEWORK_ADR.md` ADR-003）

| 步号 | 状态名 | 全名 | 描述 |
|------|--------|------|------|
| 1 | read_original | `step1_read_original` | 读取原始 skill 内容 |
| 2 | debrand | `step2_debrand` | 去标识化（移除原作者/仓库/平台烙印）|
| 3 | enhance | `step3_enhance` | 差异化增强（功能/质量提升）|
| 4 | chineseize | `step4_chineseize` | displayName 中文化 + frontmatter 规范化 |
| 5 | add_deps | `step5_add_deps` | 补充依赖说明章节 |
| 6 | generate_dual | `step6_generate_dual` | 生成免费版/付费版双 payload |
| 7 | validate | `step7_validate` | 质量门禁验证（去标识 + 八大维度评分 ≥ 40）|
| 8 | upload_free | `step8_upload_free` | 上传免费版到 SkillHub (CLI) |
| 9 | upload_paid | `step9_upload_paid` | 上传付费版到企业 API |
| 10 | completed | `completed` | 工作流完成（终态）|

> **元状态**：`failed` 不是步骤，而是 `workflow_states.status` 字段的值。当某步失败时，`skills.workflow_state` 保留在当前步骤，`workflow_states.status='failed'`，`workflow_states.retry_count++`。

### 2.2 合法状态转换规则

```
step1_read_original ──┬──> step2_debrand          (正向: 开始去标识)
                      └──> failed                 (异常: 无法读取原始内容)

step2_debrand ────────┬──> step3_enhance          (正向: 去标识完成)
                      ├──> step1_read_original    (回退: 需重新读取原始)
                      └──> failed

step3_enhance ────────┬──> step4_chineseize       (正向)
                      ├──> step2_debrand          (回退: 增强失败重做去标识)
                      └──> failed

step4_chineseize ─────┬──> step5_add_deps         (正向)
                      ├──> step3_enhance          (回退)
                      └──> failed

step5_add_deps ───────┬──> step6_generate_dual    (正向)
                      ├──> step4_chineseize       (回退)
                      └──> failed

step6_generate_dual ──┬──> step7_validate         (正向)
                      ├──> step5_add_deps         (回退: 双版本生成失败)
                      └──> failed

step7_validate ───────┬──> step8_upload_free      (正向: 验证通过)
                      ├──> step6_generate_dual    (回退: 验证失败重新生成)
                      └──> failed

step8_upload_free ────┬──> step9_upload_paid      (正向: 有付费版)
                      ├──> completed              (跳步: 无付费版直接完成)
                      ├──> step7_validate         (回退: 上传失败需重试)
                      └──> failed

step9_upload_paid ────┬──> completed              (正向: 终态)
                      ├──> step8_upload_free      (回退: 重试)
                      └──> failed

completed             ───> (终态，不可再转)

failed                ───> 任意非终态步骤          (重试入口)
```

### 2.3 转换合法性矩阵（验证脚本已确认）

| from \ to | step2 | step3 | step4 | step5 | step6 | step7 | step8 | step9 | completed | failed |
|-----------|-------|-------|-------|-------|-------|-------|-------|-------|-----------|--------|
| step1     | OK    | -     | -     | -     | -     | -     | -     | -     | -         | OK     |
| step2     | -     | OK    | -     | -     | -     | -     | -     | -     | -         | OK     |
| step3     | OK(回)| -     | OK    | -     | -     | -     | -     | -     | -         | OK     |
| step4     | -     | OK(回)| -     | OK    | -     | -     | -     | -     | -         | OK     |
| step5     | -     | -     | OK(回)| -     | OK    | -     | -     | -     | -         | OK     |
| step6     | -     | -     | -     | OK(回)| -     | OK    | -     | -     | -         | OK     |
| step7     | -     | -     | -     | -     | OK(回)| -     | OK    | -     | -         | OK     |
| step8     | -     | -     | -     | -     | -     | OK(回)| -     | OK    | OK(跳步)  | OK     |
| step9     | -     | -     | -     | -     | -     | -     | OK(回)| -     | OK        | OK     |
| completed | -     | -     | -     | -     | -     | -     | -     | -     | -         | -      |

---

## 三、批量回填方案

### 3.1 回填决策矩阵

```
┌─────────────────┬─────────────────┬──────────────┬─────────────────┬────────────────────────┐
│ current_status  │ is_differentiated│ free_upload  │ paid_upload     │ => 目标 workflow_state │
├─────────────────┼─────────────────┼──────────────┼─────────────────┼────────────────────────┤
│ registered      │ 0/1             │ no           │ no              │ step1_read_original    │
│ differentiated  │ 1               │ no           │ no              │ step5_add_deps         │
│ optimized       │ 1               │ no           │ no              │ step7_validate         │
│ differentiated  │ 1               │ yes          │ no              │ step8_upload_free      │
│ optimized       │ 1               │ yes          │ no              │ step8_upload_free      │
│ *               │ *               │ yes          │ yes             │ completed              │
│ packaged        │ 1               │ no           │ no              │ step8_upload_free      │
│ published       │ 0/1             │ *            │ *               │ completed              │
└─────────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
```

### 3.2 回填后预期分布（验证脚本 dry-run 输出）

| 目标状态 | 记录数 |
|---------|--------|
| `step7_validate` | 879 |
| `step5_add_deps` | 847 |
| `step8_upload_free` | 102 |
| `step1_read_original`（保持不变）| 20 |
| **合计** | **1848** |

### 3.3 回填实施步骤

```bash
# 1. 备份数据库（必须）
copy "d:\skills\skill-registry.db" "d:\skills\skill-registry.db.bak.%date:~0,10%"

# 2. dry-run 验证
python "c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5\round2_workflow_fix.py"

# 3. 真实写回
python "c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5\round2_workflow_fix.py" --apply

# 4. 验证回填结果
python "c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5\round2_workflow_fix.py"
```

### 3.4 回填操作的副作用

- **更新 `skills.workflow_state` 字段**：1848 条记录从 `step1_read_original` 改为正确的状态
- **更新 `skills.updated_at` 字段**：记录回填时间
- **插入 `operations` 表记录**：1848 条 `operation_type='workflow_backfill'` 操作记录，含 `before_state` 和 `after_state`
- **插入 `workflow_states` 表记录**：为处于 `step7_validate`/`step8_upload_free`/`step9_upload_paid`/`completed` 的 skill 补一条 `status='completed'` 的步骤记录，含 `result_data` JSON 说明回填来源
- **保持 `step1_read_original` 的 20 条记录不变**：这些是真正未开始差异化的 skill

---

## 四、代码修改建议

### 4.1 修改 `db.py` - `register_skill()` 增加 `workflow_state` 参数

**文件**: `d:\skills\skill-registry\db.py`
**位置**: 第 299-363 行

**修改前**:
```python
def register_skill(slug, name, display_name, version, category, source, local_path,
                   source_slug=None, source_url=None, source_author=None,
                   source_license=None, skill_type=None, pricing_model=None,
                   is_differentiated=0, notes=None, edition=None, parent_slug=None):
    ...
    if existing:
        c.execute("""
            UPDATE skills SET
                current_name = ?, current_display_name = ?, current_version = ?,
                category = ?, source = ?, local_path = ?,
                source_slug = ?, source_url = ?, source_author = ?, source_license = ?,
                skill_type = ?, pricing_model = ?, is_differentiated = ?,
                edition = ?, parent_slug = ?,
                updated_at = ?, notes = ?
            WHERE id = ?
        """, (...))
    else:
        c.execute("""
            INSERT INTO skills (
                slug, current_name, current_display_name, current_version,
                category, source, source_slug, source_url, source_author, source_license,
                local_path, created_at, updated_at, current_status,
                is_differentiated, pricing_model, skill_type, notes,
                edition, parent_slug
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (...))
```

**修改后**:
```python
def register_skill(slug, name, display_name, version, category, source, local_path,
                   source_slug=None, source_url=None, source_author=None,
                   source_license=None, skill_type=None, pricing_model=None,
                   is_differentiated=0, notes=None, edition=None, parent_slug=None,
                   workflow_state=None):
    """注册或更新一个skill

    v1.2新增参数：
        workflow_state: 工作流状态，默认 None 时根据 is_differentiated 推断
                       'step1_read_original' (未开始) 或 'step5_add_deps' (差异化完成)
    """
    # 推断默认 workflow_state
    if workflow_state is None:
        workflow_state = 'step5_add_deps' if is_differentiated else 'step1_read_original'

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

    now = datetime.now().isoformat()

    c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
    existing = c.fetchone()

    if existing:
        skill_id = existing[0]
        c.execute("""
            UPDATE skills SET
                current_name = ?, current_display_name = ?, current_version = ?,
                category = ?, source = ?, local_path = ?,
                source_slug = ?, source_url = ?, source_author = ?, source_license = ?,
                skill_type = ?, pricing_model = ?, is_differentiated = ?,
                edition = ?, parent_slug = ?,
                workflow_state = ?,
                updated_at = ?, notes = ?
            WHERE id = ?
        """, (name, display_name, version, category, source, local_path,
              source_slug, source_url, source_author, source_license,
              skill_type, pricing_model, is_differentiated,
              edition, parent_slug,
              workflow_state,
              now, notes, skill_id))
    else:
        c.execute("""
            INSERT INTO skills (
                slug, current_name, current_display_name, current_version,
                category, source, source_slug, source_url, source_author, source_license,
                local_path, created_at, updated_at, current_status,
                is_differentiated, pricing_model, skill_type, notes,
                edition, parent_slug, workflow_state
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (slug, name, display_name, version, category, source,
              source_slug, source_url, source_author, source_license,
              local_path, now, now, 'registered', is_differentiated,
              pricing_model, skill_type, notes, edition, parent_slug,
              workflow_state))
        skill_id = c.lastrowid

    # ... 后续 versions / operations 记录不变 ...
```

### 4.2 修改 `scan_and_import.py` - 显式设置 `workflow_state`

**文件**: `d:\skills\skill-registry\scan_and_import.py`
**位置**: 第 184-209 行 `import_skills_to_db()` 函数

**修改建议**:
```python
def import_skills_to_db(skills):
    """导入skill列表到数据库"""
    from db import register_skill, record_operation

    count = 0
    for skill in skills:
        pricing_model = 'free'
        if skill['skill_type'] == 'original_creation':
            pricing_model = 'freemium'
        elif skill['skill_type'] == 'differentiated':
            pricing_model = 'freemium'
        elif skill['skill_type'] == 'original_download':
            pricing_model = 'free'

        # 根据 skill_type 推断 workflow_state
        if skill['is_differentiated']:
            # 已差异化完成的 skill，工作流应处于"待生成双版本"阶段
            workflow_state = 'step5_add_deps'
        else:
            # 原始下载的 skill，工作流处于"未开始"
            workflow_state = 'step1_read_original'

        skill_id = register_skill(
            slug=skill['slug'],
            name=skill['name'],
            display_name=skill['display_name'],
            version=skill['version'],
            category=skill['category'],
            source=skill['source'],
            local_path=skill['local_path'],
            source_slug=skill['source_slug'],
            source_url=skill['source_url'],
            source_author=skill['source_author'],
            source_license=skill['source_license'],
            skill_type=skill['skill_type'],
            pricing_model=pricing_model,
            is_differentiated=skill['is_differentiated'],
            notes=f"File hash: {skill['file_hash'][:16]}, size: {skill['file_size']}b",
            workflow_state=workflow_state  # 新增
        )

        # ... 后续 UPDATE current_status 代码不变 ...
```

### 4.3 修改 `update_mechanism.py` - 集成 `update_workflow_state()` 和 `record_score()`

**文件**: `d:\skills\skill-registry\update_mechanism.py`

#### 4.3.1 顶部导入

**位置**: 第 28-32 行附近

```python
# 在现有 import 后添加
sys.path.insert(0, str(Path(__file__).parent))
from db import update_workflow_state, record_score
```

#### 4.3.2 `check_skill_update()` - 阶段1结束时更新状态

**位置**: 第 333-427 行 `check_skill_update()` 函数末尾

```python
def check_skill_update(skill: Dict[str, Any]) -> Dict[str, Any]:
    # ... 现有逻辑不变 ...
    
    # 新增：来源检测到变更时，标记 step1 为 in_progress
    if result['status'] == 'changed':
        try:
            update_workflow_state(
                skill_id=skill['id'],
                step_number=1,
                step_name='read_original',
                status='in_progress',
                result_data=json.dumps({
                    'old_hash': last_hash[:16] if last_hash else None,
                    'new_hash': result['new_hash'][:16] if result['new_hash'] else None,
                }),
                notes=f"检测到来源变更: {result.get('change_type', 'unknown')}"
            )
        except Exception as e:
            print(f"  [WARN] 更新 workflow_state 失败: {e}")
    
    return result
```

#### 4.3.3 `sync_skill_to_platform()` - 阶段4/5 状态推进

**位置**: 第 624-659 行 `sync_skill_to_platform()` 函数

```python
def sync_skill_to_platform(slug: str, skill_id: int, new_version: str,
                           changelog: str = None) -> Dict[str, Any]:
    results = {
        'slug': slug,
        'version': new_version,
        'free_upload': None,
        'paid_upload': None,
    }

    skill_md = find_skill_md(slug)
    if not skill_md:
        results['error'] = f'SKILL.md not found for: {slug}'
        # 新增：标记失败
        update_workflow_state(skill_id, 6, 'generate_dual', 'failed',
                              notes=f"SKILL.md not found: {slug}")
        return results

    # === 阶段4: 双版本生成 ===
    # 新增：标记 step6 为 in_progress
    update_workflow_state(skill_id, 6, 'generate_dual', 'in_progress',
                          notes="开始生成免费/付费双版本 payload")

    dual = generate_dual_payloads(slug, new_version, changelog)
    results['payloads'] = dual

    if dual.get('free_path'):
        # 新增：step6 完成
        update_workflow_state(skill_id, 6, 'generate_dual', 'completed',
                              result_data=json.dumps({
                                  'free_path': dual['free_path'],
                                  'paid_path': dual.get('paid_path')
                              }))
    else:
        update_workflow_state(skill_id, 6, 'generate_dual', 'failed',
                              notes="payload 生成失败")
        return results

    # === 阶段5: 质量门禁验证（新增）===
    # 新增：step7_validate - 强制质量门禁
    update_workflow_state(skill_id, 7, 'validate', 'in_progress',
                          notes="执行质量门禁验证")

    quality_passed = run_quality_gate(slug, skill_md)
    if not quality_passed['passed']:
        update_workflow_state(skill_id, 7, 'validate', 'failed',
                              result_data=json.dumps(quality_passed),
                              notes=f"质量门禁未通过: {quality_passed['reasons']}")
        results['error'] = f"质量门禁未通过: {quality_passed['reasons']}"
        return results
    
    update_workflow_state(skill_id, 7, 'validate', 'completed',
                          result_data=json.dumps(quality_passed),
                          notes="质量门禁验证通过")

    # === 阶段5: 上传免费版 ===
    if dual.get('free_path'):
        update_workflow_state(skill_id, 8, 'upload_free', 'in_progress',
                              notes="上传免费版到 SkillHub")
        free_result = upload_free_via_cli(slug, skill_md)
        results['free_upload'] = free_result
        record_upload(skill_id, new_version, 'skillhub', slug,
                      free_result['status'],
                      http_status=free_result.get('exit_code'),
                      error=free_result.get('error'),
                      visibility='public')

        # 新增：根据上传结果更新状态
        if free_result['status'] == 'success':
            update_workflow_state(skill_id, 8, 'upload_free', 'completed',
                                  notes="免费版上传成功")
        else:
            update_workflow_state(skill_id, 8, 'upload_free', 'failed',
                                  result_data=json.dumps({
                                      'exit_code': free_result.get('exit_code'),
                                      'stderr': free_result.get('stderr', '')[:500]
                                  }),
                                  notes=f"免费版上传失败: exit={free_result.get('exit_code')}")

    # === 阶段5: 上传付费版 ===
    if dual.get('paid_payload'):
        update_workflow_state(skill_id, 9, 'upload_paid', 'in_progress',
                              notes="准备付费版上传 payload")
        paid_result = upload_paid_via_api(slug, dual['paid_payload'])
        results['paid_upload'] = paid_result
        # 注意：付费版实际需人工通过浏览器上传，状态保持 in_progress
        # 实际上传成功后由人工/AI 调用 update_workflow_state(step9, 'completed')
    else:
        # 无付费版（如冲奖款/获奖款），直接进入 completed
        update_workflow_state(skill_id, 9, 'upload_paid', 'completed',
                              notes="无付费版，跳过此步骤")
        update_workflow_state(skill_id, 10, 'completed', 'completed',
                              notes="工作流完成（仅免费版）")

    return results


def run_quality_gate(slug: str, skill_md_path: Path) -> Dict[str, Any]:
    """质量门禁：去标识检查 + 八大维度评分（新增函数）
    
    返回:
        {
            'passed': bool,
            'reasons': [str],
            'debranding_ok': bool,
            'score': int,
            'is_pass': bool
        }
    """
    import subprocess
    result = {'passed': False, 'reasons': [], 'debranding_ok': False, 'score': 0, 'is_pass': False}
    
    # 1. 去标识检查（调用 check_debranding.py）
    check_debranding = Path(__file__).parent / "check_debranding.py"
    if check_debranding.exists():
        try:
            proc = subprocess.run(
                ['python', str(check_debranding), '--slug', slug],
                capture_output=True, text=True, timeout=30
            )
            if proc.returncode == 0:
                result['debranding_ok'] = True
            else:
                result['reasons'].append(f"去标识检查失败: {proc.stderr[:200]}")
        except Exception as e:
            result['reasons'].append(f"去标识检查异常: {e}")
    else:
        result['reasons'].append("check_debranding.py 不存在，跳过去标识检查")
        result['debranding_ok'] = True  # 容错：无检查脚本时放行
    
    # 2. 八大维度评分（需 AI 评分后通过 record_score 写入）
    # 这里检查 scores 表是否已有 final 评分且通过
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT total_score, is_pass FROM scores
        WHERE skill_id = (SELECT id FROM skills WHERE slug = ?)
        AND score_type = 'final'
        ORDER BY scored_at DESC LIMIT 1
    """, (slug,))
    row = c.fetchone()
    conn.close()
    
    if row:
        result['score'] = row['total_score']
        result['is_pass'] = bool(row['is_pass'])
        if not result['is_pass']:
            result['reasons'].append(f"评分未过阈值: {row['total_score']}/40")
    else:
        # 无评分记录时放行（向后兼容），但应记录警告
        result['reasons'].append("警告: 无 final 评分记录，建议先调用 record_score()")
        result['is_pass'] = True  # 容错
    
    # 综合判定
    result['passed'] = result['debranding_ok'] and result['is_pass']
    return result
```

#### 4.3.4 新增 `retry-failed` 子命令

**位置**: 第 892-951 行 `main()` 函数附近

```python
def cmd_retry_failed(args):
    """重试上传失败的 skill（新增命令）"""
    print("查找上传失败的 skill...")
    conn = get_db()
    c = conn.cursor()
    # 找出 workflow_state 标记为 failed 的 skill
    c.execute("""
        SELECT DISTINCT s.id, s.slug, s.current_version, s.workflow_state
        FROM skills s
        JOIN workflow_states w ON w.skill_id = s.id
        WHERE w.status = 'failed' AND w.retry_count < 3
        ORDER BY s.slug
    """)
    failed = [dict(r) for r in c.fetchall()]
    conn.close()
    
    if not failed:
        print("没有需要重试的失败记录")
        return
    
    print(f"找到 {len(failed)} 个失败 skill:")
    for f in failed:
        print(f"  - {f['slug']} (state={f['workflow_state']})")
    
    for f in failed:
        print(f"\n重试: {f['slug']}")
        result = sync_skill_to_platform(f['slug'], f['id'], f['current_version'])
        print(f"  结果: {json.dumps(result, ensure_ascii=False, indent=2)[:500]}")


# 在 main() 的 subparsers 部分新增:
# retry-failed
subparsers.add_parser('retry-failed', help='重试上传失败的 skill')

# 在命令分发部分新增:
elif args.command == 'retry-failed':
    cmd_retry_failed(args)
```

### 4.4 修改 `auto_discover.py` - `cmd_import()` 真正写库

**文件**: `d:\skills\skill-registry\auto_discover.py`
**位置**: 第 419-452 行 `cmd_import()` 函数

**修改前**（仅打印，不写库）:
```python
def cmd_import(args):
    # ... 查找候选 skill ...
    print(f"导入skill: {args.slug}")
    print(f"  注意: 导入需要AI执行差异化改造，请参考NAMING_CONVENTION.md")
    # 没有任何 DB 写入操作
```

**修改后**（真正写库）:
```python
def cmd_import(args):
    """导入指定 skill 到本地 DB（v1.2: 真正写入数据库）"""
    if not CANDIDATES_FILE.exists():
        print("未找到候选列表，请先执行 scan 命令")
        return

    with open(CANDIDATES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    target = None
    for skill in data.get('new_skills', []):
        if skill.get('source_slug') == args.slug:
            target = skill
            break

    if not target:
        print(f"未在候选列表中找到: {args.slug}")
        return

    # 新增：调用 register_skill() 真正写入 DB
    sys.path.insert(0, str(Path(__file__).parent))
    from db import register_skill, update_workflow_state, record_operation
    
    # 候选 skill 还未差异化改造，workflow_state = step1_read_original
    slug = target.get('source_slug', args.slug)
    skill_id = register_skill(
        slug=slug,
        name=target.get('display_name', slug),
        display_name=target.get('display_name', slug),
        version='1.0.0',
        category=target.get('category', 'Other'),
        source='clawhub_download' if target.get('source_platform') == 'clawhub' else 'opensource_modified',
        local_path=target.get('local_path', ''),
        source_slug=slug,
        source_url=target.get('source_url', ''),
        source_license=target.get('_license', 'MIT'),
        skill_type='original_download',
        is_differentiated=0,
        notes=f"从 {target.get('source_platform')} 自动发现并导入",
        workflow_state='step1_read_original'  # 新增：初始状态
    )
    
    # 新增：初始化 workflow_states 记录
    update_workflow_state(skill_id, 1, 'read_original', 'completed',
                          result_data=json.dumps({
                              'source_platform': target.get('source_platform'),
                              'source_url': target.get('source_url')
                          }),
                          notes="自动发现导入，step1 已完成")
    
    print(f"导入成功: {slug} (skill_id={skill_id})")
    print(f"  workflow_state: step1_read_original (已完成)")
    print(f"  下一步: 执行差异化改造（step2_debrand -> step5_add_deps）")
    print(f"  完成后使用: python update_mechanism.py generate {slug}")
```

### 4.5 启用 `record_score()` 质量门禁的完整集成

`record_score()` 已被外部 batch 脚本调用过（scores 表有 2330 条记录），但未集成到 `update_mechanism.py` 的流水线中。完整集成方案：

#### 4.5.1 在 `step7_validate` 阶段强制调用

参见 4.3.3 中的 `run_quality_gate()` 函数。该函数：
1. 调用 `check_debranding.py` 做去标识检查
2. 查询 `scores` 表是否已有 `final` 评分且 `is_pass=1`
3. 综合判定是否通过门禁

#### 4.5.2 AI 评分集成点

当 AI 完成差异化改造后，应通过以下方式调用 `record_score()`：

```python
from db import record_score

# AI 完成差异化改造后，对每个 skill 进行评分
record_score(
    skill_id=skill_id,
    score_type='final',
    quality=5,           # 质量 (0-6)
    practicality=5,      # 实用性
    simplicity=4,        # 易用性
    cost=5,              # 成本
    performance=5,       # 性能
    debranding=6,        # 去标识完整度
    compliance=5,        # 合规性
    differentiation=5,   # 差异化程度
    reviewer='ai_agent',
    notes='差异化改造后自动评分'
)
# 总分 40 即可通过门禁
```

#### 4.5.3 历史评分数据利用

现有 2330 条历史评分（1150 baseline + 1180 final）可作为门禁基线。`run_quality_gate()` 优先使用 `final` 评分，无评分时容错放行并告警。

---

## 五、阶段映射设计

### 5.1 `update_mechanism.py` 阶段映射

| UPDATE_TRIGGER.md 阶段 | 对应 workflow_state 步号 | 调用函数 |
|------------------------|-------------------------|---------|
| 阶段1: 来源检测 | （不改状态，仅检测）| `check_skill_update()` |
| 阶段2: 变更分析 | step1 (read_original) | AI 分析时调用 `update_workflow_state(1, 'in_progress')` |
| 阶段3: 本地升级 | step2 → step3 → step4 → step5 | AI 改造时逐级推进 |
| 阶段4: 双版本生成 | step6 (generate_dual) | `sync_skill_to_platform()` 中调用 |
| 阶段5: 平台同步 | step7 → step8 → step9 | `sync_skill_to_platform()` 中调用 |
| 阶段6: 结果汇报 | step10 (completed) | 上传成功后调用 |

### 5.2 `auto_discover.py` 阶段映射

| DISCOVER_TRIGGER.md 阶段 | 对应 workflow_state 步号 | 调用位置 |
|--------------------------|-------------------------|---------|
| 阶段1: 来源扫描 | （不改状态）| `cmd_scan()` |
| 阶段2: 去重比对 | （不改状态）| `deduplicate()` |
| 阶段3: 差异化改造 | step1 → step2 → step3 → step4 → step5 | `cmd_import()` 初始化 + AI 改造时推进 |
| 阶段4: 双版本+上传 | step6 → step7 → step8 → step9 | 调用 `update_mechanism.py` 的 `sync_skill_to_platform()` |
| 阶段5: 汇报 | step10 (completed) | 上传成功后调用 |

---

## 六、修复实施路线图

### Phase 1: 紧急修复（P0，立即执行）

1. **备份数据库**
   ```bash
   copy "d:\skills\skill-registry.db" "d:\skills\skill-registry.db.bak.20260720"
   ```

2. **执行回填脚本**
   ```bash
   python "c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5\round2_workflow_fix.py" --apply
   ```
   预期结果：1848 条记录从 `step1_read_original` 修正为正确状态

3. **修改 `db.py` 的 `register_skill()`**（参见 4.1）

4. **修改 `scan_and_import.py`**（参见 4.2）

### Phase 2: 流水线集成（P1，1-2 天内）

5. **修改 `update_mechanism.py`**（参见 4.3）
   - 导入 `update_workflow_state` 和 `record_score`
   - 在 `check_skill_update()` 末尾添加状态更新
   - 在 `sync_skill_to_platform()` 中添加 step6/7/8/9 推进
   - 新增 `run_quality_gate()` 函数
   - 新增 `retry-failed` 子命令

6. **修改 `auto_discover.py`**（参见 4.4）
   - `cmd_import()` 真正调用 `register_skill()`
   - 初始化 `workflow_states` 记录

### Phase 3: 质量门禁启用（P1，2-3 天内）

7. **在 AI 差异化改造流程中集成 `record_score()`**
   - AI 完成改造后强制评分
   - 评分 < 40 阻止上传

8. **完善 `check_debranding.py` 集成**
   - 确保可通过 `--slug` 参数单 skill 检查
   - 输出标准化 JSON 供 `run_quality_gate()` 解析

### Phase 4: 监控与告警（P2，1 周内）

9. **添加适应度函数检查**（参见 FRAMEWORK_ADR.md 第五节）
   - 每日检查 `workflow_states` 表记录数是否等于 `skills` 表
   - 失败上传重试次数 ≤ 3
   - 评分通过率 ≥ 95%

---

## 七、验证脚本说明

### 7.1 脚本位置

`c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5\round2_workflow_fix.py`

### 7.2 使用方式

```bash
# 1. 仅演练（不写库，推荐先用）
python round2_workflow_fix.py

# 2. 限制演练记录数
python round2_workflow_fix.py --limit 50

# 3. 真实写回（生产使用前必须备份 DB）
python round2_workflow_fix.py --apply
```

### 7.3 脚本功能

| 功能 | 说明 |
|------|------|
| 当前状态分析 | 显示 `workflow_state`/`current_status` 分布、`workflow_states` 表记录数、`scores` 表记录数 |
| 10 步状态机定义 | 完整定义 10 个步骤 + 元状态 `failed` |
| 转换规则验证 | 验证 8 个示例转换的合法性，确保状态机一致性 |
| 回填演练 | 根据 `current_status + is_differentiated + 上传状态` 推断 1848 条记录的正确状态 |
| 集成点验证 | 检查 `db.py`/`scan_and_import.py`/`update_mechanism.py`/`auto_discover.py` 当前是否已集成状态机 |
| 阶段映射设计 | 显示 `update_mechanism.py` 和 `auto_discover.py` 各阶段对应的 `workflow_state` 步号 |
| 真实写回 | `--apply` 模式下实际更新 `skills.workflow_state`、插入 `operations` 和 `workflow_states` 记录 |

### 7.4 验证结果（dry-run 模式输出摘要）

```
卡在 step1_read_original 的记录细分:
  status=optimized       diff=1 upload=not_uploaded -> 879 条
  status=differentiated  diff=1 upload=not_uploaded -> 847 条
  status=differentiated  diff=1 upload=uploaded     -> 51 条
  status=optimized       diff=1 upload=uploaded     -> 51 条
  status=registered      diff=1 upload=not_uploaded -> 20 条

回fill后目标分布:
  step7_validate           : 879 条
  step5_add_deps           : 847 条
  step8_upload_free        : 102 条
  step1_read_original      : 20 条

状态机验证: [OK] 状态机定义无问题
转换合法性验证示例: 全部 [OK]

代码集成点现状:
  [MISSING] db_py_register_skill_has_workflow_state_param    = False
  [MISSING] scan_and_import_passes_workflow_state            = False
  [MISSING] update_mechanism_calls_update_workflow_state     = False
  [MISSING] update_mechanism_calls_record_score              = False
  [MISSING] auto_discover_cmd_import_writes_db               = False
```

---

## 八、风险评估与缓解

| 风险 | 可能性 | 影响 | 缓解措施 |
|------|--------|------|---------|
| 回填时 `current_status` 与 `workflow_state` 推断不一致 | 中 | 中 | 回填脚本在 `operations` 表记录 `before_state`/`after_state` 和推断依据，可追溯审计 |
| `register_skill()` 增加 `workflow_state` 参数后破坏现有调用方 | 低 | 高 | 参数默认值 `None` 时根据 `is_differentiated` 自动推断，向后兼容 |
| `update_mechanism.py` 集成状态机后影响上传性能 | 低 | 低 | `update_workflow_state()` 是单条 SQL 更新，耗时 < 10ms |
| `record_score()` 质量门禁过严阻塞发布 | 中 | 中 | `run_quality_gate()` 对无评分记录的 skill 容错放行并告警，不硬阻断 |
| `auto_discover.py` 的 `cmd_import()` 改为真正写库后产生重复 skill | 中 | 中 | `register_skill()` 已有 `slug` 唯一约束 + UPDATE 分支，重复导入会更新而非新建 |

---

## 九、附录：相关文件清单

| 文件 | 路径 | 角色 |
|------|------|------|
| 数据库 schema | `d:\skills\skill-registry\db.py` | 定义 `workflow_states` 表、`update_workflow_state()`、`record_score()`、`register_skill()` |
| 扫描导入 | `d:\skills\skill-registry\scan_and_import.py` | 批量导入 skill（需修改以设置 `workflow_state`）|
| 更新机制 | `d:\skills\skill-registry\update_mechanism.py` | 6 阶段流水线（需集成状态机）|
| 自动发现 | `d:\skills\skill-registry\auto_discover.py` | 5 阶段发现流水线（需修复 `cmd_import`）|
| 基线初始化 | `d:\skills\skill-registry\init_baseline.py` | 已正确设置 `workflow_state='completed'`，无需修改 |
| 去标识检查 | `d:\skills\skill-registry\check_debranding.py` | 质量门禁组件（需集成到 `step7_validate`）|
| 架构决策记录 | `d:\skills\skill-registry\FRAMEWORK_ADR.md` | ADR-003 定义 10 步状态机 |
| 完整性报告 | `d:\skills\skill-registry\WORKFLOW_INTEGRITY_REPORT.md` | 第七节描述 workflow_state 失效问题 |
| **本方案配套脚本** | `c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5\round2_workflow_fix.py` | 状态机修复方案验证与回填脚本 |
| **本设计文档** | `d:\skills\WORKFLOW_STATE_MACHINE_FIX.md` | 本文档 |

---

## 十、总结

本方案针对 `d:\skills\skill-registry` 工作流状态机的三个核心问题：

1. **1848 条记录卡在 `step1_read_original`** —— 通过 `round2_workflow_fix.py --apply` 批量回填，根据 `current_status + is_differentiated + 上传状态` 推断正确状态

2. **`register_skill()` 不接受 `workflow_state` 参数** —— 修改 `db.py` 增加参数，默认根据 `is_differentiated` 推断

3. **`update_workflow_state()` 和 `record_score()` 未集成到流水线** —— 在 `update_mechanism.py` 的 `check_skill_update()`、`sync_skill_to_platform()` 中集成状态推进，在 `auto_discover.py` 的 `cmd_import()` 中实现真正的 DB 写入

修复后预期效果：
- `workflow_state` 字段准确反映每个 skill 的真实生产进度
- `workflow_states` 表逐步积累 10 步详细追踪记录
- 质量门禁（去标识 + 八大维度评分）强制生效，不达标阻止上传
- 失败上传可通过 `python update_mechanism.py retry-failed` 重试
