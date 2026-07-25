# SkillHub 12大因素深度复核 + v57.0实施 + v58.0提示词生成方案

## 摘要

用户要求复核 `skillhub-visibility-analysis-v6.html` 中提到的12大可见性因素是否都已处理，并指出两个严重问题：分类页全为0、企业页skill数(1637)与后台(2600+)不一致。经代码级验证确认：

1. **分类全为0的根因**：`enterprise_uploader.py` 第409行使用 `'category': platform_category`（字符串），缺少 API 必需的 `'categoryIds'`（数字ID数组）。994个skill通过浏览器批量脚本上传时完全缺失 `categoryIds` 字段。
2. **skill数量差异原因**：企业页1637=已审核通过且对外可见的skill；后台2600+=包含已审核(1637)+待审核(~994)+被拒绝(38)。差额是审核流程的中间状态，非冗余或重复。
3. **12因素中8个未真正完成**：因素1/2/3/7/8/9/11/12均处于阻断或平台数据缺失状态。v6报告中因素8(Category)被误判为"达标"是最严重的误判。

本方案分三轮执行：第一轮本地修复（categoryIds字段+description优化+VPN转型+脚本增强），第二轮API操作（需企业Cookie），第三轮收尾（v58提示词+Git提交）。

## 当前状态分析

### 12大因素真实状态对照表

| # | 因素 | v6报告评估 | 真实状态 | 证据 | 需要行动 |
|---|------|-----------|---------|------|---------|
| 1 | 审核状态 | 2706待审 | ❌ 未处理 | Admin API需企业Cookie | 获取Cookie→批量审核 |
| 2 | 对外发布 | 4个org_only | ❌ 未处理 | 同上 | Cookie→publish |
| 3 | 搜索索引 | 0可搜索 | ❌ 未处理 | 依赖因素1 | 审核通过后自动索引 |
| 4 | Downloads | 0 | ⚠️ 4.3万总量 | 企业页面显示4.3万下载 | 原有skill有，新增无 |
| 5 | Stars | 0 | ⚠️ 1星 | 企业页面显示1收藏 | 长期积累 |
| 6 | Score | 0 | ❌ 0 | 依赖4+5 | 长期积累 |
| 7 | IconUrl | 0%覆盖 | ❌ 994个未上传 | batch_000.json无iconUrl字段 | DELETE+重传 |
| **8** | **Category** | **达标(100%)** | **❌ 全部0!** | admin/skills/categories全0；enterprise_uploader.py无categoryIds字段 | **修复categoryIds+重传** |
| 9 | Summary_ZH | 0%覆盖 | ❌ 994个未上传 | batch_000.json无summary_zh | DELETE+重传 |
| 10 | Description | 0.5%合格 | ⚠️ 119个本地优化 | 平台未更新 | DELETE+重传 |
| 11 | DisplayName | 29.3%中文 | ❌ 40%英文 | 企业页面显示英文标题 | 中文化+重传 |
| 12 | Tags | 89.2%合格 | ❌ 994个未上传 | batch_000.json有tags但格式可能不对 | DELETE+重传 |

### 根因验证（代码级确认）

**证据1 — enterprise_uploader.py 第398-415行**：
```python
payload = {
    ...
    'category': platform_category,  # 字符串 "office-efficiency"，API不识别
    'iconUrl': ...,
    # 缺少 'categoryIds' 字段
}
```

**证据2 — update_mechanism.py 第533行**：
```python
'categoryIds': [],  # 空数组
```

**证据3 — batch_000.json（994个skill批量上传数据）**：
- Grep搜索 `categoryIds` → 0匹配（完全缺失）
- Grep搜索 `iconUrl`/`summary_zh`/`subCategories`/`changelog` → 0匹配（全部缺失）

**证据4 — enterprise_upload_report.json 第13行（原始60个skill）**：
- `"misc (其他)": "所有技能暂归此类(categoryIds: [11048])"` — 确认正确格式为数字ID数组

### skill数量差异分析

| 数据源 | 数量 | 含义 |
|--------|------|------|
| 企业页面 `/enterprise/org-xxo535hs` | 1637 | 已审核通过且对外可见的skill |
| 后台技能列表+审核列表 | 2600+ | 已审核(1637) + 待审核(~994) + 被拒绝(38) |
| 差额 | ~1000 | V54上传的994个skill处于"待审核"状态 |
| 1639→1637 | -2 | 可能有2个skill被拒绝或下架 |

**结论**：差额是正常的审核流程中间状态。待审核skill不出现在企业公开页面，只出现在后台管理列表。这不是冗余或重复。需通过批量审核通过消除差额。

## 提议的变更

### 第一轮：本地修复（无需API，可立即执行）

---

#### 变更1：修复 enterprise_uploader.py — 添加 categoryIds 字段

**文件**：`D:\skills\tools\enterprise_uploader.py`

**变更内容**：

1. 在第37行附近（`CATEGORY_MAP_FILE` 定义后）添加团队分类ID常量：
```python
TEAM_CATEGORY_IDS = {
    "通用办公": 11039, "研发工具": 11040, "系统运维": 11041,
    "质量测试": 11042, "需求设计": 11043, "信息检索": 11044,
    "项目管理": 11045, "数据分析": 11046, "安全合规": 11047, "其他": 11048,
}
```

2. 在 `get_platform_category()` 函数后（约第133行后）添加：
```python
def get_team_category_id(platform_category: str) -> int:
    """从平台分类键获取团队分类数字ID
    映射链: platform_category → platform_to_team → TEAM_CATEGORY_IDS
    """
    global _CATEGORY_MAP_CACHE
    if _CATEGORY_MAP_CACHE is None:
        _CATEGORY_MAP_CACHE = _load_category_map()
    platform_to_team = _CATEGORY_MAP_CACHE.get('platform_to_team', {})
    team_name = platform_to_team.get(platform_category, '其他')
    return TEAM_CATEGORY_IDS.get(team_name, 11048)
```

3. 在 `upload_skill()` 的 payload 构建处（第398-415行），添加 `categoryIds`：
```python
team_category_id = get_team_category_id(platform_category)
payload = {
    ...
    'categoryIds': [team_category_id],  # API必需: 团队分类数字ID数组
    'category': platform_category,       # 保留作为备份
    ...
}
```

**原因**：API要求 `categoryIds`（数字ID数组），当前代码只发送 `category`（字符串），导致994个skill分类全为0。

**验证**：
```bash
python -m py_compile tools/enterprise_uploader.py
python -c "from enterprise_uploader import get_team_category_id; print(get_team_category_id('office-efficiency'))"  # 应输出11039
python -c "from enterprise_uploader import get_team_category_id; print(get_team_category_id('dev-programming'))"  # 应输出11040
```

---

#### 变更2：修复 update_mechanism.py — 填充 categoryIds

**文件**：`D:\skills\tools\update_mechanism.py`

**变更内容**：

1. 在文件顶部导入区域添加：
```python
from enterprise_uploader import get_team_category_id, get_platform_category
```

2. 在 `generate_payload()` 函数（第524-534行）中，修复空 `categoryIds`：
```python
# 从SKILL.md内容推断平台分类，再获取团队分类ID
platform_cat = get_platform_category(slug, metadata, body)
team_cat_id = get_team_category_id(platform_cat)

payload = {
    ...
    'categoryIds': [team_cat_id],  # 填充团队分类数字ID，不再为空
}
```

**原因**：第533行 `'categoryIds': []` 导致更新机制生成的payload分类为空。

**验证**：
```bash
python -m py_compile tools/update_mechanism.py
python -c "from update_mechanism import generate_payload; r = generate_payload('test-slug'); print(r.get('categoryIds', 'MISSING'))"
```

---

#### 变更3：优化剩余 description 长度（1010个skill）

**文件**：`D:\skills\tools\batch_optimize_description.py`（已存在）

**执行方式**：
```bash
cd D:\skills\tools
python batch_optimize_description.py --dry-run  # 预览
python batch_optimize_description.py            # 执行
```

**原因**：v57提示词记录1010/1035个skill的description长度<150字符，影响详情页质量和搜索权重。

**验证**：检查最新报告，确认1010个skill的description达到150-280字符。

---

#### 变更4：处理5个VPN被封禁skill（本地内容修改）

**被封禁skill**：v2ray-proxy-tool-free, v2ray-proxy-tool-pro, universal-proxy-pro, vpn-toolkit-free, vpn-toolkit-pro

**转型方向**：VPN/翻墙工具 → 网络安全诊断/隐私保护工具（合规方向）

| Slug | 原主题 | 转型方向 |
|------|--------|----------|
| v2ray-proxy-tool-free | V2Ray代理管理 | 网络连通性诊断工具 |
| v2ray-proxy-tool-pro | V2Ray代理管理Pro | 网络安全审计工具 |
| universal-proxy-pro | 通用代理Pro | 网络配置管理工具 |
| vpn-toolkit-free | VPN工具包免费版 | 隐私保护检查工具 |
| vpn-toolkit-pro | VPN工具包Pro版 | 网络安全加固工具 |

**修改要点**：
- frontmatter: displayName/summary/description/tags/category/license 全部更新
- body: V2Ray/proxy启动命令 → 网络诊断命令(ping/traceroute/netstat)
- 移除所有V2Ray/VPN/代理/翻墙关键词
- license改为MIT
- 双目录同步：differentiated-skills 和 hermes-skills

**验证**：Grep搜索5个skill的SKILL.md，确认不再包含v2ray/vpn/代理/翻墙/proxy关键词。

---

#### 变更5：增强 batch_operations_v2.py — 添加全量重传命令

**文件**：`D:\skills\tools\batch_operations_v2.py`

**变更内容**：在 `main()` 函数中添加 `reupload-all-batch` 命令，用于批量DELETE+重传994个V54上传的skill。支持断点续传：从已有报告中读取已完成的slug。

**原因**：因PUT API不可用，所有字段修复必须通过DELETE+POST重传实现。需要一个专门的批量命令来处理994个skill的重传。

**验证**：
```bash
python -m py_compile tools/batch_operations_v2.py
python batch_operations_v2.py  # 查看帮助，确认新命令存在
```

---

### 第二轮：API任务（需企业Cookie，用户操作后执行）

---

#### 变更6：获取企业账号Cookie（用户操作 — 阻断项）

用户需在浏览器登录企业团队账号，导出完整cookie到 `~/.skillhub_cookies.txt`。

验证：`python batch_operations_v2.py check-auth` 返回 `✅ 认证成功`。

---

#### 变更7：批量审核通过2706个待审版本

```bash
python batch_operations_v2.py approve-all
```
在浏览器执行生成的JS脚本，自动遍历审核队列。

验证：2706个待审版本全部审核通过，抽样10个skill在前台可搜索。

---

#### 变更8：DELETE+重传38个被拒skill

```bash
python batch_operations_v2.py reupload-rejected
```

验证：38个被拒skill全部DELETE+重传成功，重新进入审核队列。

---

#### 变更9：全量DELETE+重传994个V54上传的skill

```bash
python batch_operations_v2.py reupload-all-batch
```

**关键说明**：
- 此操作会DELETE旧版本（丢失已有downloads/stars数据）→ POST重传（携带完整字段）
- 因PUT API不可用，这是修复categoryIds/iconUrl/summary_zh/tags的唯一方式
- 脚本支持断点续传
- 每个skill间隔2秒，避免API限流

验证：
- 访问 `/admin/skills/categories` 确认分类不再为0
- 抽样10个skill通过API GET检查 categoryIds, iconUrl, summary_zh, tags 字段

---

#### 变更10：4个org_only skill对外发布 + 重传memory-orchestrator-sk

```bash
python batch_operations_v2.py publish-org-only
python batch_operations_v2.py reupload-deleted
```

---

### 第三轮：收尾任务

---

#### 变更11：生成 next-round-prompt-v58.0.md

**文件**：`D:\skills\docs\plans\next-round-prompt-v58.0.md`

**内容要点**：
- 基于真实12因素状态编写（修正v57中因素8"达标"的误判）
- P0: categoryIds修复已完成 → 全量重传 + 审核通过
- P1: DisplayName中文化 + Verified认证申请
- P2: downloads/stars积累策略 + 所有权认领
- 包含验证检查清单

---

#### 变更12：Git提交所有变更

```bash
cd D:\skills
git add -A
git commit -m "fix: V58 — categoryIds修复 + description优化 + VPN转型 + batch增强 + v58提示词"
git push origin master
git push hermes-skills master
```

## 假设与决策

1. **API字段名确认**：基于 `enterprise_upload_report.json` 中 `categoryIds: [11048]` 的历史成功记录，确认API字段名为 `categoryIds`（复数，数字ID数组）。

2. **重传策略决策**：因PUT API不可用，必须DELETE+POST。接受downloads/stars数据损失，因为分类为0导致的前台不可见问题更严重。

3. **浏览器脚本 vs Python脚本**：V54使用浏览器脚本上传导致字段缺失。后续统一使用修复后的 `enterprise_uploader.py`，确保字段完整性。

4. **1637 vs 2600差异**：确认为正常审核流程差异（已审核 vs 待审核），无需特殊处理。通过批量审核通过消除差额。

5. **VPN skill转型原则**：不删除skill，保留slug和目录结构，仅修改内容为合规的网络安全工具。

6. **保留category字段**：在payload中同时发送 `categoryIds`（API必需）和 `category`（备份），不影响功能。

## 任务执行顺序

```
第一轮（本地，可立即并行执行）:
  变更1 (修复enterprise_uploader.py) ──────────┐
  变更2 (修复update_mechanism.py) ─────────────┤
  变更3 (优化1010个description) ────────────────┤
  变更4 (5个VPN skill转型) ─────────────────────┤
  变更5 (增强batch_operations_v2.py) ───────────┤
                                                │
第二轮（API，需Cookie）:                        │
  变更6 (获取企业Cookie — 用户操作) ────────────┤
  变更7 (批量审核2706版本) ── 需要变更6 ────────┤
  变更8 (DELETE+重传38被拒) ── 需要变更1,6 ─────┤
  变更9 (全量重传994个) ── 需要变更1,5,6 ───────┤
  变更10 (发布org_only+重传memory) ── 需要变更6 ┤
                                                │
第三轮（收尾）:                                 │
  变更11 (生成v58.0提示词) ── 需要全部完成 ─────┤
  变更12 (Git提交) ── 需要全部完成 ─────────────┘
```

## 验证步骤

### 第一轮验证（本地）
- `enterprise_uploader.py` 语法检查通过
- `get_team_category_id('office-efficiency')` 返回 11039
- `get_team_category_id('dev-programming')` 返回 11040
- `update_mechanism.py` 语法检查通过
- `generate_payload()` 返回的 `categoryIds` 不再为空
- `batch_operations_v2.py` 语法检查通过
- 1010个skill的description长度达到150-280字符
- 5个VPN skill不再包含V2Ray/VPN/代理/翻墙关键词
- 5个VPN skill的license改为MIT

### 第二轮验证（API）
- `check-auth` 返回 `✅ 认证成功`
- 2706个待审版本批量审核通过（剩余<50）
- 38个被拒skill DELETE并重新上传成功
- 994个skill全量重传成功
- `/admin/skills/categories` 分类不再为0
- 抽样10个skill的 categoryIds, iconUrl, summary_zh, tags 字段正确
- 4个org_only skill切换为public
- memory-orchestrator-sk重新上传成功
- 前台搜索10个skill确认可搜索

### 第三轮验证
- `next-round-prompt-v58.0.md` 生成
- Git提交成功
- 推送到origin和hermes-skills
