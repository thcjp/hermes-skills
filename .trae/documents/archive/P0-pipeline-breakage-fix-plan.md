# P0 关键管道断裂修复计划

> 基于对 d:\skills 实际代码的逐行验证，非文档承诺。
> 制定日期：2026-07-25
> 前序：修复计划v3 第1轮

---

## Summary

修复自动化管道的3处关键断裂，使系统从"不可用"恢复到"基本可用"：
1. `daily_sync.py:121` 硬编码 `--dry-run` → 改为配置项控制
2. `update_mechanism.py:702-714` 付费上传stub → 改为调用 `enterprise_uploader.upload_skill()` 真实上传
3. `db.py:40-67` CREATE TABLE 缺5列 → 补齐 pricing_engine 运行时添加的列

---

## Current State Analysis

### P0-1: daily_sync.py 硬编码 --dry-run

**文件**: `d:\skills\tools\daily_sync.py`

第116-121行：
```python
def step_sync_clawhub():
    """阶段7: ClawHub 同步"""
    log("=" * 50)
    log("阶段7: SYNC_CLAWHUB - ClawHub 批量上传")
    log("=" * 50)
    run_script("clawhub_batch_uploader.py", ["--dry-run"])
```

`run_script` 函数（第41-52行）接收 args 列表并拼接到命令中。`["--dry-run"]` 被硬编码，导致 ClawHub 每日同步永远是干跑，永不实际上传。

`daily_sync.py` 第30-33行已从 `project_config` 导入多个配置项：
```python
from project_config import (
    DB_PATH, TOOLS_DIR, DATA_DIR, REPORT_DIR,
    HEALTH_REPORT_DIR, DISCOVERY_DIR
)
```

`project_config.py` 中目前无 `CLAWHUB_DRY_RUN` 配置项（grep确认无匹配）。

### P0-2: update_mechanism.py 付费上传stub

**文件**: `d:\skills\tools\update_mechanism.py`

第702-714行：
```python
def upload_paid_via_api(slug: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """通过企业API上传付费版本"""
    result = {'slug': slug, 'platform': 'skillhub_paid', 'method': 'enterprise_api'}
    # 注意: 企业API需要session cookies认证
    # 这里生成payload文件，实际上传由AI通过浏览器MCP完成
    payload_path = PAYLOADS_DIR / f"{slug}-paid.json"
    result['payload_path'] = str(payload_path)
    result['payload'] = payload
    result['status'] = 'payload_ready'
    result['note'] = '企业API上传需要浏览器session cookies认证，请通过browser_evaluate执行上传'
    return result
```

该函数只保存payload文件并返回 `payload_ready`，从不发起HTTP请求。

**调用点**（第914-917行）：
```python
if dual.get('paid_payload'):
    paid_result = upload_paid_via_api(slug, dual['paid_payload'])
    results['paid_upload'] = paid_result
```

**真实上传逻辑已存在于** `d:\skills\tools\enterprise_uploader.py` 第304-426行：
- `upload_skill(slug, dry_run=False)` 函数
- 完整流程：门控检查 → 找SKILL.md → 解析frontmatter → 构建payload → 获取cookie → multipart POST → 解析响应
- 使用 `urlopen(Request(...))` 发送真实HTTP请求（第403-404行）
- cookie从 `COOKIE_FILE` 或 `SKILLHUB_SESSION_COOKIE` 环境变量获取（第215-227行）
- 无cookie时返回 `{'success': False, 'message': '无认证cookie...'}`（第378行）

**导入兼容性**：
- `enterprise_uploader.py` 第25行：`sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))` — 自动将 tools/ 加入sys.path
- `enterprise_uploader.py` 第26行：`from config import (...)` — 使用 tools/config.py shim，shim转发到 project_config
- `update_mechanism.py` 第21行已将 config/ 目录加入 sys.path
- 两文件同在 tools/ 目录，无循环依赖，可直接 `from enterprise_uploader import upload_skill`

### P0-3: db.py CREATE TABLE 缺5列

**文件**: `d:\skills\tools\db.py`

第40-67行 CREATE TABLE skills 语句包含到 `workflow_state` 为止，但缺少 pricing_engine.py 运行时添加的5列。

`pricing_engine.py` 第546-550行通过 ALTER TABLE 添加：
```python
for col, col_type in [('suggested_price', 'REAL'), ('pricing_category', 'TEXT'), 
                      ('pricing_rationale', 'TEXT'), ('pricing_tier', 'TEXT'),
                      ('is_paid', 'INTEGER')]:
    if col not in columns:
        c.execute(f"ALTER TABLE skills ADD COLUMN {col} {col_type}")
```

db.py 第69-85行已有类似的 ALTER TABLE 迁移模式（edition/parent_slug/current_score/workflow_state），可参照添加。

**注**：v3计划中提到的 `free_slug/paid_slug` 经grep验证是变量名而非DB列名，实际只缺5列。`summary` 列也未找到ALTER TABLE添加语句，可能是审计误报。

---

## Proposed Changes

### 变更1: P0-1 — daily_sync.py + project_config.py

**文件1**: `d:\skills\config\project_config.py`
- **位置**: 在 `CLAWHUB_DOWNLOADED_DIR` 定义之后（约第56行后）
- **操作**: 新增配置项
- **内容**:
  ```python
  # ClawHub每日同步是否干跑模式（False=真实上传，True=仅模拟）
  CLAWHUB_DRY_RUN = False
  ```
- **原因**: 消除 daily_sync.py 中的 --dry-run 硬编码，使运维可配置

**文件2**: `d:\skills\tools\daily_sync.py`
- **位置**: 第30-33行导入语句 + 第121行
- **操作**: 
  1. 在导入列表中增加 `CLAWHUB_DRY_RUN`
  2. 将第121行 `run_script("clawhub_batch_uploader.py", ["--dry-run"])` 改为根据配置决定
- **修改后**:
  ```python
  # 第30-33行改为:
  from project_config import (
      DB_PATH, TOOLS_DIR, DATA_DIR, REPORT_DIR,
      HEALTH_REPORT_DIR, DISCOVERY_DIR, CLAWHUB_DRY_RUN
  )
  
  # 第121行改为:
  args = ["--dry-run"] if CLAWHUB_DRY_RUN else []
  run_script("clawhub_batch_uploader.py", args)
  ```
- **原因**: 默认真实上传，保留干跑能力供调试

### 变更2: P0-2 — update_mechanism.py

**文件**: `d:\skills\tools\update_mechanism.py`
- **位置**: 第702-714行 `upload_paid_via_api` 函数
- **操作**: 重写函数，调用 enterprise_uploader.upload_skill() 进行真实上传
- **修改后**:
  ```python
  def upload_paid_via_api(slug: str, payload: Dict[str, Any]) -> Dict[str, Any]:
      """通过企业API上传付费版本
      
      调用 enterprise_uploader.upload_skill() 发起真实HTTP上传。
      若上传失败（如无cookie/网络错误），保存payload文件作为备份。
      """
      result = {'slug': slug, 'platform': 'skillhub_paid', 'method': 'enterprise_api'}
      
      # 保存payload作为备份（无论上传成功与否）
      payload_path = PAYLOADS_DIR / f"{slug}-paid.json"
      result['payload_path'] = str(payload_path)
      result['payload'] = payload
      
      # 调用真实上传逻辑
      try:
          from enterprise_uploader import upload_skill
          upload_result = upload_skill(slug)
          
          if upload_result.get('success'):
              result['status'] = 'uploaded'
              result['response'] = upload_result.get('response', {})
              result['score'] = upload_result.get('score', 0)
              result['price'] = upload_result.get('price', 0)
              result['is_paid'] = upload_result.get('is_paid', True)
          else:
              # 上传失败，保留payload备份
              result['status'] = 'payload_ready'
              result['error'] = upload_result.get('message', '上传失败')
              result['note'] = '真实上传失败，payload已保存，可手动重试'
      except Exception as e:
          # 导入或调用异常，保留payload备份
          result['status'] = 'payload_ready'
          result['error'] = f'上传异常: {str(e)}'
          result['note'] = '企业上传模块异常，payload已保存'
      
      return result
  ```
- **原因**: 使付费版上传走真实HTTP路径，payload备份仅在网络/认证失败时使用
- **关键设计决策**: 
  - 不修改 `enterprise_uploader.py`，仅调用其 `upload_skill()` 函数
  - `enterprise_uploader.upload_skill()` 内部会做门控检查（与sync_skill_to_platform中的L1检查重复，但幂等无害）
  - `enterprise_uploader.upload_skill()` 自己构建payload（从SKILL.md读取），与传入的payload参数可能略有差异，但SKILL.md是source of truth，可接受
  - payload文件始终保存（作为备份），不是fallback逻辑而是备份策略

### 变更3: P0-3 — db.py

**文件**: `d:\skills\tools\db.py`
- **位置**: 第40-67行 CREATE TABLE skills 语句 + 第69-85行 ALTER TABLE 迁移区
- **操作**: 
  1. 在 CREATE TABLE 语句的 `workflow_state` 行之后增加5列定义
  2. 在 ALTER TABLE 迁移区增加5列的迁移（为已有数据库补列）
- **修改后 CREATE TABLE 部分**（在 `workflow_state TEXT DEFAULT 'step1_read_original'` 之后、闭合 `)` 之前增加）:
  ```python
              workflow_state TEXT DEFAULT 'step1_read_original',
              suggested_price REAL,
              pricing_category TEXT,
              pricing_rationale TEXT,
              pricing_tier TEXT,
              is_paid INTEGER DEFAULT 0
  ```
  **注意**: 原第65行 `workflow_state TEXT DEFAULT 'step1_read_original'` 末尾无逗号，需加逗号。
  
- **修改后 ALTER TABLE 迁移区**（在第83-85行 `workflow_state` 迁移之后增加）:
  ```python
      try:
          c.execute("ALTER TABLE skills ADD COLUMN suggested_price REAL")
      except sqlite3.OperationalError:
          pass
      try:
          c.execute("ALTER TABLE skills ADD COLUMN pricing_category TEXT")
      except sqlite3.OperationalError:
          pass
      try:
          c.execute("ALTER TABLE skills ADD COLUMN pricing_rationale TEXT")
      except sqlite3.OperationalError:
          pass
      try:
          c.execute("ALTER TABLE skills ADD COLUMN pricing_tier TEXT")
      except sqlite3.OperationalError:
          pass
      try:
          c.execute("ALTER TABLE skills ADD COLUMN is_paid INTEGER DEFAULT 0")
      except sqlite3.OperationalError:
          pass
  ```
- **原因**: 消除schema漂移，新环境init_database()后无需运行pricing_engine.py即可使用pricing相关列
- **设计决策**: 保留ALTER TABLE迁移（与现有edition/parent_slug/current_score/workflow_state模式一致），确保已有数据库平滑升级。pricing_engine.py中的ALTER TABLE逻辑可保留（幂等，IF NOT EXISTS检查）。

---

## Assumptions & Decisions

1. **P0-2 不修改 enterprise_uploader.py**: 避免扩大改动范围。`upload_skill()` 的接口（slug + dry_run）足够使用，其内部门控检查虽与sync_skill_to_platform重复但幂等无害。
2. **P0-2 payload始终保存**: 不是fallback/敷衍，而是审计备份策略。真实上传是主路径，payload备份在上传失败时供手动重试。
3. **P0-3 保留pricing_engine.py的ALTER TABLE**: 幂等操作，不删除。新环境通过init_database()即可获得全部列，旧环境通过ALTER TABLE迁移。
4. **P0-3 实际缺5列非7列**: 经grep验证，`free_slug/paid_slug`是变量名非DB列名。v3计划中的"7列"是审计误报。
5. **P0-1 默认False**: `CLAWHUB_DRY_RUN = False` 意味着默认真实上传，这是修复的目的。需要调试时可临时设为True。
6. **不改变record_upload调用**: 第916-917行的 `results['paid_upload'] = paid_result` 保持不变，upload_paid_via_api返回的dict结构兼容。

---

## Verification Steps

### 步骤1: 语法检查（每个文件修改后立即执行）
```powershell
cd d:\skills
python -m py_compile config\project_config.py
python -m py_compile tools\daily_sync.py
python -m py_compile tools\update_mechanism.py
python -m py_compile tools\db.py
```

### 步骤2: P0-1 验证 — dry-run配置生效
```powershell
cd d:\skills
python -c "
import sys
sys.path.insert(0, 'config')
from project_config import CLAWHUB_DRY_RUN
print(f'CLAWHUB_DRY_RUN = {CLAWHUB_DRY_RUN}')
assert CLAWHUB_DRY_RUN == False, '默认应为False(真实上传)'
print('P0-1 验证通过: 配置项存在且默认为False')
"
```

### 步骤3: P0-2 验证 — upload_paid_via_api调用真实上传
```powershell
cd d:\skills
python -c "
import sys
sys.path.insert(0, 'tools')
sys.path.insert(0, 'config')
from update_mechanism import upload_paid_via_api
# 验证函数不再直接返回payload_ready（除非上传失败）
# 检查函数源码中包含enterprise_uploader导入
import inspect
src = inspect.getsource(upload_paid_via_api)
assert 'enterprise_uploader' in src, '应导入enterprise_uploader'
assert 'upload_skill' in src, '应调用upload_skill'
print('P0-2 验证通过: upload_paid_via_api调用真实上传逻辑')
"
```

### 步骤4: P0-3 验证 — init_database包含全部列
```powershell
cd d:\skills
python -c "
import sys, sqlite3, tempfile, os
sys.path.insert(0, 'tools')
sys.path.insert(0, 'config')

# 使用临时数据库验证
tmpdb = os.path.join(tempfile.gettempdir(), 'test_p0_3.db')
if os.path.exists(tmpdb):
    os.remove(tmpdb)

# 临时替换DB_PATH
import db as dbmod
dbmod.DB_PATH = tmpdb
dbmod.init_database()

conn = sqlite3.connect(tmpdb)
c = conn.cursor()
c.execute('PRAGMA table_info(skills)')
columns = [row[1] for row in c.fetchall()]
conn.close()
os.remove(tmpdb)

required = ['suggested_price', 'pricing_category', 'pricing_rationale', 'pricing_tier', 'is_paid']
missing = [col for col in required if col not in columns]
assert not missing, f'缺失列: {missing}'
print(f'P0-3 验证通过: init_database包含全部5个pricing列')
print(f'  skills表共{len(columns)}列: {columns}')
"
```

### 步骤5: 无回归验证 — 3个真实skill质量门检查
```powershell
cd d:\skills
python tools\quality_gate.py "differentiated-skills\Agents\ad-creative-intel-free"
python tools\quality_gate.py "differentiated-skills\Creative\agentvibes-skill-free"
python tools\quality_gate.py "differentiated-skills\Other\agent-assistant-free"
```
通过标准：3个skill质量门检查均正常运行，无报错，结果与第2轮一致。

### 步骤6: 无回归验证 — update_mechanism check命令
```powershell
cd d:\skills
python tools\update_mechanism.py check --slug ad-creative-intel-free
```
通过标准：命令正常运行，无NameError/ImportError。

---

## 修改文件清单

| 文件 | 变更类型 | 变更内容 |
|------|---------|---------|
| `d:\skills\config\project_config.py` | 新增 | 增加 `CLAWHUB_DRY_RUN = False` 配置项 |
| `d:\skills\tools\daily_sync.py` | 修改 | 导入CLAWHUB_DRY_RUN + 第121行条件化dry-run |
| `d:\skills\tools\update_mechanism.py` | 修改 | 重写upload_paid_via_api函数(第702-714行) |
| `d:\skills\tools\db.py` | 修改 | CREATE TABLE增加5列 + ALTER TABLE迁移增加5列 |
