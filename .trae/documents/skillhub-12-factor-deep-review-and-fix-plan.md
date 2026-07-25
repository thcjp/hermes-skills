# SkillHub 12大因素深度复核与修复方案

## 摘要

通过深度复核 v6 可见性分析报告中的 12 大因素，发现 **2 个严重误判** 和 **1 个关键遗漏**：

1. **因素8（Category）被误判为"达标"** — 实际上平台分类全部显示 0。根因：994 个 skill 上传时使用了错误的字段名 `category`（字符串），而 API 要求 `categoryIds`（数字 ID 数组）。
2. **因素7/9/10/12 的"已完成"仅限本地** — iconUrl、summary_zh、description、tags 的修复都只改了本地 SKILL.md 文件，从未实际上传到平台。994 个 skill 的平台数据仍然缺失这些字段。
3. **994 个 skill 通过浏览器脚本上传时缺少关键字段** — batch_000.json 证实上传数据只有 `slug, name, displayName, version, summary, license, homepage, tags, tools, category, content`，缺失 `categoryIds, iconUrl, summary_zh, subCategories, changelog`。

技能数量差异已查明：企业页面 1637 = 已审核通过的 skill；后台 2600+ = 包含待审版本；差额 ~1000 = V54 上传的 994 个待审 skill。

## 当前状态分析

### 12 大因素真实状态对照表

| # | 因素 | v6报告评估 | 真实状态 | 证据 | 需要行动 |
|---|------|-----------|---------|------|---------|
| 1 | 审核状态 | 2,706待审 | ❌ 未处理 | Admin API 需企业Cookie | 获取企业Cookie→批量审核 |
| 2 | 对外发布 | 4个org_only | ❌ 未处理 | 同上 | 企业Cookie→publish |
| 3 | 搜索索引 | 0可搜索 | ❌ 未处理 | 依赖因素1 | 审核通过后自动索引 |
| 4 | Downloads | 0 | ⚠️ 4.3万总量 | 企业页面显示4.3万下载 | 原有skill有，新增无 |
| 5 | Stars | 0 | ⚠️ 1星 | 企业页面显示1收藏 | 几乎没有 |
| 6 | Score | 0 | ❌ 0 | 依赖4+5 | 长期积累 |
| 7 | IconUrl | 0%覆盖 | ❌ **994个未上传** | batch_000.json无iconUrl字段 | DELETE+重传 |
| 8 | Category | 达标(100%) | ❌ **全部0!** | admin/skills/categories全0 | **修复categoryIds+重传** |
| 9 | Summary_ZH | 0%覆盖 | ❌ **994个未上传** | batch_000.json无summary_zh | DELETE+重传 |
| 10 | Description | 0.5%合格 | ⚠️ 119个已优化(本地) | 本地已改，平台未更新 | DELETE+重传 |
| 11 | DisplayName | 29.3%中文 | ❌ 40%英文 | 企业页面显示英文标题 | 中文化+重传 |
| 12 | Tags | 89.2%合格 | ❌ **994个未上传** | batch_000.json有tags但格式可能不对 | DELETE+重传 |

### 问题1：分类全部为0的根因分析

**证据链：**

1. `enterprise_upload_report.json` 第13行：原始60个skill使用 `categoryIds: [11048]`（数字ID）
2. `batch_000.json`（994个skill的批量上传数据）：只有 `category: "Finance"`（字符串），**无 `categoryIds` 字段**
3. `enterprise_uploader.py` 第409行：`'category': platform_category`（字符串 "office-efficiency"），**非 `categoryIds`**
4. `update_mechanism.py` 第533行：`'categoryIds': []`（空数组）
5. SkillHub 企业页面：所有1637个skill都归为"科创少年"一个分类

**结论：** SkillHub API 的分类字段是 `categoryIds`（数字ID数组），不是 `category`（字符串）。994个skill上传时完全没有发送 `categoryIds`，所以平台分类全为0。

### 问题2：技能数量差异分析

| 数据源 | 数量 | 含义 |
|--------|------|------|
| 企业页面 `/enterprise/org-xxo535hs` | 1637 | 已审核通过且对外可见的skill |
| 后台技能列表+审核列表 | 2600+ | 包含已审核(1637) + 待审核(~994) + 被拒绝(38) |
| 差额 | ~1000 | V54上传的994个skill处于"待审核"状态 |
| 1639→1637 | -2 | 可能有2个skill被拒绝或删除 |

**结论：** 差额是正常的——待审核的skill不出现在企业公开页面，只出现在后台管理列表。这不是冗余或重复，而是审核流程的中间状态。

## 修复方案

### 核心修复1：修复 `enterprise_uploader.py` 的 categoryIds 字段

**文件：** `D:\skills\tools\enterprise_uploader.py`

**当前代码（第398-415行）：**
```python
payload = {
    ...
    'category': platform_category,  # 错误：API不识别此字段
    'iconUrl': CATEGORY_ICONS.get(platform_category, DEFAULT_ICON),
    'subCategories': subcategories,
    ...
}
```

**修复为：**
```python
# 从category_mapping.json获取团队分类数字ID
team_category_name = get_team_category_name(platform_category)  # 如 "通用办公"
team_category_id = TEAM_CATEGORY_IDS.get(team_category_name, 11048)  # 如 11039

payload = {
    ...
    'categoryIds': [team_category_id],  # 正确：API要求的字段名和格式
    'category': platform_category,      # 保留作为备份(不影响)
    'iconUrl': CATEGORY_ICONS.get(platform_category, DEFAULT_ICON),
    'subCategories': subcategories,
    ...
}
```

**需要添加的常量：**
```python
TEAM_CATEGORY_IDS = {
    "通用办公": 11039,
    "研发工具": 11040,
    "系统运维": 11041,
    "质量测试": 11042,
    "需求设计": 11043,
    "信息检索": 11044,
    "项目管理": 11045,
    "数据分析": 11046,
    "安全合规": 11047,
    "其他": 11048,
}
```

**需要添加的函数：**
```python
def get_team_category_id(platform_category: str) -> int:
    """从平台分类键获取团队分类数字ID"""
    global _CATEGORY_MAP_CACHE
    if _CATEGORY_MAP_CACHE is None:
        _CATEGORY_MAP_CACHE = _load_category_map()
    platform_to_team = _CATEGORY_MAP_CACHE.get('platform_to_team', {})
    team_name = platform_to_team.get(platform_category, '其他')
    return TEAM_CATEGORY_IDS.get(team_name, 11048)
```

### 核心修复2：修复 `update_mechanism.py` 的空 categoryIds

**文件：** `D:\skills\tools\update_mechanism.py` 第533行

**当前：** `'categoryIds': [],`

**修复为：** 从 SKILL.md 的 category 字段推断 team category ID 并填充。

### 核心修复3：全量 DELETE + 重传策略

由于 PUT API 不可用，所有字段修复必须通过 DELETE + POST 重传实现。

**重传范围：** 全部 994 个 V54 上传的 skill（它们都缺失 categoryIds, iconUrl, summary_zh, subCategories, changelog）

**重传统一使用 `enterprise_uploader.py`**（而非浏览器批量脚本），确保所有字段正确发送。

**执行步骤：**
1. 修复 `enterprise_uploader.py` 添加 `categoryIds` 字段
2. 获取企业账号 Cookie
3. 批量 DELETE 994 个 skill
4. 批量 POST 重传 994 个 skill（使用修复后的 enterprise_uploader.py）
5. 批量审核通过重传的版本
6. 验证分类、图标、摘要等字段在平台上正确显示

### 核心修复4：更新 v6 分析报告的误判

**因素8（Category）从"达标"改为"阻断"** — 这是之前最严重的误判，导致分类问题一直未被处理。

### 核心修复5：生成 v58.0 提示词

基于真实状态生成下一轮提示词，包含：
- categoryIds 修复任务
- 全量重传任务
- 企业Cookie获取任务
- 审核通过任务
- 验证任务

## 实施步骤

### 步骤1：修复 enterprise_uploader.py（本地，无需API）

1. 添加 `TEAM_CATEGORY_IDS` 常量映射
2. 添加 `get_team_category_id()` 函数
3. 在 payload 中添加 `'categoryIds': [team_category_id]`
4. 保留 `'category': platform_category` 作为备份
5. 验证语法正确

### 步骤2：修复 update_mechanism.py（本地，无需API）

1. 在 `build_upload_payload()` 函数中填充 `categoryIds`
2. 从 SKILL.md 的 category 字段推断 team category ID

### 步骤3：生成 v58.0 提示词（本地，无需API）

1. 基于 12 大因素真实状态编写
2. 明确 categoryIds 修复为最高优先级
3. 包含全量重传策略
4. 包含验证检查清单

### 步骤4：获取企业账号 Cookie（需用户操作）

1. 用户在浏览器登录企业团队账号
2. 导出完整 cookie
3. 保存到 `~/.skillhub_cookies.txt`
4. 运行 `check-auth` 验证

### 步骤5：全量 DELETE + 重传（需企业Cookie）

1. 批量 DELETE 994 个 skill
2. 批量 POST 重传（使用修复后的 enterprise_uploader.py）
3. 确保每个 skill 携带完整字段

### 步骤6：批量审核通过（需企业Cookie）

1. 生成审核 JS 脚本
2. 在浏览器执行批量审核
3. 验证审核结果

### 步骤7：验证修复效果（需企业Cookie）

1. 访问 `/admin/skills/categories` 确认分类不再为0
2. 访问企业页面确认 skill 数量增加
3. 抽样检查 iconUrl, summary_zh, tags 字段
4. 前台搜索测试

### 步骤8：Git 提交

1. 提交所有修复
2. 推送到 GitHub
3. 更新跟踪文件

## 假设与决策

1. **API字段名确认：** 基于 `enterprise_upload_report.json` 中 `categoryIds: [11048]` 的历史成功记录，确认 API 字段名为 `categoryIds`（复数，数字ID数组）
2. **重传策略：** 因 PUT API 不可用，必须 DELETE + POST。但这意味着已有的 downloads/stars 数据会丢失。决策：接受损失，因为分类为0导致的前台不可见问题更严重
3. **浏览器脚本 vs Python脚本：** V54使用浏览器脚本上传导致字段缺失。决策：后续统一使用修复后的 `enterprise_uploader.py`，确保字段完整性
4. **审核流程：** 重传后需要重新审核。决策：先批量审核通过现有2706个待审版本，再重传994个新版本触发新审核
5. **1637 vs 2600差异：** 确认为正常审核流程差异，无需特殊处理

## 验证步骤

1. `enterprise_uploader.py` 语法检查：`python -m py_compile tools/enterprise_uploader.py`
2. `update_mechanism.py` 语法检查：`python -m py_compile tools/update_mechanism.py`
3. categoryIds 字段验证：`python -c "from enterprise_uploader import upload_skill; r = upload_skill('test-slug', dry_run=True); print(r)"`
4. 企业Cookie验证：`python batch_operations_v2.py check-auth`
5. 分类页面验证：访问 `https://www.skillhub.cn/admin/skills/categories` 确认分类不再为0
6. 企业页面验证：访问 `https://www.skillhub.cn/enterprise/org-xxo535hs` 确认skill数量增加
7. 字段抽样验证：通过 API GET 检查 10 个 skill 的 categoryIds, iconUrl, summary_zh 字段
8. 前台搜索验证：在 skillhub.cn 搜索 10 个 skill 确认可搜索到

## 下一轮提示词生成

完成以上修复后，生成 `next-round-prompt-v58.0.md`，包含：
- P0: categoryIds 修复 + 全量重传 + 审核通过
- P1: DisplayName 中文化 + Verified 认证申请
- P2: downloads/stars 积累策略 + 所有权认领
