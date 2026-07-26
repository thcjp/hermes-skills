# 下一轮对话提示词 (v67.0)

> **日期**: 2026-07-26
> **前置版本**: v66.0 (安全预检增强 + ClawHub营销包装 + 平台操作固化)
> **核心任务**: P1-2(营销关卡集成到enterprise_uploader) + P1-3(搜索排名优化) + P2任务群(平台评分同步/低评分触发/自动化流水线) + SkillHub API令牌刷新后执行auto_publish

---

## 本轮已完成 (v66.0 → v67.0)

### 安全预检系统增强 ✅

| 任务 | 状态 | 实现详情 |
|------|------|---------|
| 21项安全预检 | ✅完成 | `quality_gate.py` 新增10项科恩实验室+云鼎实验室高风险模式检测(SSRF/数据外泄/混淆代码/反向Shell/权限提升/挖矿/Prompt注入/持久化/不安全反序列化/依赖混淆) |
| 源skill安全扫描 | ✅完成 | `source_security_scan.py` 新增scan_content()+auto_fix_risks(), 扫描源skill并自动修复 |
| 生产流水线集成 | ✅完成 | `auto_differentiate.py` + `upload_gate.py` 集成L1.5安全预检层 |
| version_sync_pipeline集成 | ✅完成 | `sync_skill_to_all_platforms()` 和 `upgrade_single_skill()` 均集成安全预检, critical阻断/high+medium警告 |

### ClawHub上传流程标准化 ✅

| 任务 | 状态 | 实现详情 |
|------|------|---------|
| 营销参数集成 | ✅完成 | `sync_to_clawhub()` 新增 --categories/--topics/--name/--slug/--json 参数, 复用clawhub_batch_uploader的提取函数 |
| 分类映射修复 | ✅完成 | `category_mapping.json` 新增 local_to_clawhub 直连映射(14项), 修复frontmatter category=Agents时映射断裂bug |
| get_clawhub_category增强 | ✅完成 | 优先使用local_to_clawhub直连, 其次中转映射, 最后slug/body推断 |

### 平台操作固化 ✅

| 任务 | 状态 | 实现详情 |
|------|------|---------|
| platform_ops.py统一入口 | ✅完成 | 新增 star_skill/batch_approve/handle_rejected/auto_publish/get_platform_status/publish_to_community 6个统一函数 |
| auto_publish完整流程 | ✅完成 | 查询状态→审核通过→社区发布→收藏→更新DB, 一键完成 |
| publish_to_community | ✅完成 | POST /orgs/{ORG_ID}/admin/skills/{slug}/publish-to-community, 含slug冲突重试 |

### 实测验证 ✅

| 验证项 | 结果 | 详情 |
|--------|------|------|
| 安全预检对真实skill | 21项检查: 20通过, 1失败 | API密钥明文处理(critical)被检测, 与科恩实验室"读取环境变量"风险标注一致 |
| ClawHub营销参数 | category=creative, topics=[audio,upload,aioz,stream], displayName=AIOZ音频上传免费版 | 营销参数全部正确提取 |
| 分类映射 | local_to_clawhub 14项, Agents→agents | 直连映射工作正常 |
| DB状态 | 0 pending, 0 rejected | 质量门禁有效阻断问题skill |
| 质量门禁阻断 | 1 marketing_gate/blocked, 2 quality_gate/blocked | 新门禁正在工作 |

### SkillHub平台状态分析

| 检查项 | 结果 | 说明 |
|--------|------|------|
| API令牌状态 | ⚠ 过期 | HTTP 401: "invalid or expired enterprise token" |
| 公开API | ✅ 可用 | GET /api/v1/skills/{slug} 返回完整skill数据(含安全报告) |
| 安全报告(科恩) | benign(安全) | 标注4项风险: 不安全网络传输/读取环境变量/调用外部API/HTTP请求 |
| 安全报告(云鼎) | suspicious(可疑) | 存在潜在风险, 需关注 |
| 企业页可见性 | 需登录 | 页面要求登录后才能查看 |
| DB pending/rejected | 0/0 | 质量门禁有效防止问题skill进入平台 |

### Git提交

- **Commit 1**: `28171808f` - feat(security): v2.2安全预检增强 — 科恩实验室+云鼎实验室21项检测
- **Commit 2**: `7bb873868` - feat(platform-ops): auto_publish社区发布 + 安全预检集成到version_sync_pipeline
- **Commit 3**: `3d9983af7` - feat(clawhub): v2.2 ClawHub营销包装增强 — 分类直连映射修复+topics/name参数集成
- **推送状态**: ✅ 已成功推送到 origin(私有) + hermes-skills(公开) 双远程仓库

---

## 下一轮核心任务

### P0: SkillHub API令牌刷新 + auto_publish执行 (阻塞项)

**问题**: SkillHub企业API令牌已过期, 所有admin操作(审核/发布/收藏)被阻断
**影响**: 企业页可见性无法修复(2068个published skill中部分visibility非public)

**执行步骤**:
1. 用户刷新SkillHub认证(登录skillhub.cn, 获取新的企业token)
2. 保存token到 .credentials/skillhub.json
3. 执行批量auto_publish:
   ```bash
   python tools/platform_ops.py auto-publish-all
   ```
4. 验证企业页可见skill数量是否增加

**替代方案**: 使用agent-browser登录后批量操作
```bash
agent-browser --session skillhub open "https://www.skillhub.cn/login"
# 登录后执行JS批量发布
```

### P1-2: 营销关卡集成到enterprise_uploader (需求3)

**目标**: 将P0-1实现的营销关卡集成到enterprise_uploader的上传前检查

**影响文件**: `tools/enterprise_uploader.py`

**详细步骤**:
1. 在enterprise_uploader的上传前检查中调用 `run_marketing_gate()`
2. 营销关卡未通过的skill给出具体修复建议并阻止上传
3. 添加 `--skip-marketing` 参数供批量场景使用

**验证**:
- enterprise_uploader上传前自动执行营销关卡检查
- 营销关卡未通过的skill被阻止并给出修复建议

### P1-3: 搜索排名优化 (延续v1.0)

**目标**: 提升skill在SkillHub搜索结果中的排名
**因素**: stars✅(已完成)、downloads、更新时间、分类匹配、关键词
**技能/插件**: defuddle(研究排名算法) → agent-browser(验证)

**执行步骤**:
1. 安装defuddle: `npm install -g defuddle`
2. 研究SkillHub搜索排名算法
3. 优化skill的tags/summary/description以匹配搜索关键词
4. 验证搜索排名提升

### P2-1: 平台评分同步到DB (需求7)

**目标**: 将SkillHub平台AI评分、用户评分、下载数同步到本地DB

**影响文件**: `tools/db.py` (新增字段), `tools/market_monitor.py` (增强)

**详细步骤**:
1. DB新增字段:
   ```sql
   ALTER TABLE skills ADD COLUMN platform_rating REAL DEFAULT 0;
   ALTER TABLE skills ADD COLUMN platform_rating_count INTEGER DEFAULT 0;
   ALTER TABLE skills ADD COLUMN platform_downloads INTEGER DEFAULT 0;
   ALTER TABLE skills ADD COLUMN platform_ai_review TEXT;
   ALTER TABLE skills ADD COLUMN last_platform_sync_at TEXT;
   ```
2. market_monitor.py新增 `sync_platform_ratings()`:
   - GET /api/v1/skills/{slug} 获取 avgRating, reviewCount, downloads
   - 写入DB: platform_rating, platform_rating_count, platform_downloads
3. 同时同步安全报告状态(keen/sanbu)到DB

**验证**:
- DB有platform_rating等字段且已回填
- market_monitor能定时同步平台评分

### P2-2: 平台低评分触发升级 (需求8)

**目标**: 当平台评分低于阈值时自动触发skill升级

**影响文件**: `tools/market_monitor.py`, `tools/upgrade_checker.py`
**依赖**: P2-1完成

**详细步骤**:
```python
RATING_THRESHOLD = 4.0  # 可配置

def check_low_rating_skills():
    """检查评分低于阈值的skill，触发升级"""
    # SELECT slug FROM skills WHERE platform_rating < RATING_THRESHOLD AND platform_rating > 0
    # 对每个低评分skill:
    #   1. 分析低评分原因(从platform_ai_review提取)
    #   2. 触发 upgrade_single_skill(slug)
    #   3. 记录升级触发原因到DB
```

### P2-3: 自动化流水线完善 (需求5)

**目标**: 完善daily_sync.py，实现定时自动化

**影响文件**: `tools/daily_sync.py` (增强), `tools/orchestrator.py`

**详细步骤**:
1. daily_sync.py整合所有循环任务:
   - 持续审核pending/rejected
   - 定期同步平台评分
   - 检查低评分触发升级
   - 检查源版本变更触发升级
2. orchestrator.py修复config导入bug

### P3-1: 统一数据源到SQLite (需求6)

**目标**: 消除双数据源, upgrade_checker从JSON迁移到SQLite

**影响文件**: `tools/upgrade_checker.py`, `tools/orchestrator.py`, `tools/skill_core/`

**详细步骤**:
1. upgrade_checker.py迁移: 从DB `platform_uploads`表读取, 不再依赖JSON
2. find_skill_md统一到 `skill_core/parser.py`
3. orchestrator.py修复SKILL_DATA_DIR等未定义变量

### P3-2: 质量检查统一入口 (需求6)

**目标**: 统一质量检查入口

**影响文件**: `tools/quality_gate.py`

**详细步骤**:
1. 确认 `run_full_quality_check()` 包含: L1(13项)+营销(7项)+防幻觉(3项)+安全(21项) = 44项
2. 所有调用方统一使用此入口

### P3-3: 文档对齐 (需求9)

**目标**: 确保ARCHITECTURE.md和starter-design.md v2.0与代码完全对齐

**影响文件**: `docs/ARCHITECTURE.md`, `docs/plans/new-conversation-starter-design.md`

**详细步骤**:
1. 更新设计文档, 添加安全预检系统(21项)和源skill安全扫描
2. 更新任务清单, 标记已完成项
3. 更新架构文档, 添加安全预检层

---

## 安全预检系统架构 (v2.2已完成)

```
生产环节:
  auto_differentiate.py
    → source_security_scan.scan_content()  [L1.5安全预检]
    → critical风险: 阻断差异化
    → high/medium风险: auto_fix_risks()自动修复

上传流水线:
  version_sync_pipeline.sync_skill_to_all_platforms()
    → L1静态格式(13项)
    → L1.5内容质量(7项)
    → 营销关卡(7项)
    → 安全预检(21项)  [v2.2新增]
      → critical: 阻断上传
      → high/medium: 警告但继续
    → 防幻觉(3项)
    → L2/L3 (可选, 需AI执行)
    → 平台同步

独立升级:
  version_sync_pipeline.upgrade_single_skill()
    → 同上完整质量链路

上传门控:
  upload_gate.py
    → L1.5安全预检层  [v2.2新增]
    → 检查源skill安全风险
```

## 质量门禁完整链路 (v2.2)

```
L1静态格式(13项) ✅ → L1.5内容质量(7项) ✅ → 营销关卡(7项) ✅ → 安全预检(21项) ✅ → 防幻觉(3项) ✅ → L2 LLM验证 ✅ → L3 Agent试用 ✅ → GitHub同步 → SkillHub同步 → ClawHub同步
```

所有质量门禁已集成到 `sync_skill_to_all_platforms()` 和 `upgrade_single_skill()` 两个核心入口。

---

## 执行注意事项

1. **不创建碎片化新文件**: 所有增强在现有文件中进行
2. **不模拟/mock**: 所有功能必须真实执行
3. **全链路修复**: 底层数据→中间模块→前端UI
4. **向后兼容**: 现有脚本和CLI命令仍可独立运行
5. **API令牌**: 需用户刷新SkillHub企业token后才能执行admin操作
6. **读取设计文档**: 执行前先阅读 `d:\skills\docs\plans\new-conversation-starter-design.md` v2.0
7. **读取任务清单**: 执行前先阅读 `d:\skills\docs\plans\new-conversation-task-list.md` v2.0
8. **安全预检优先**: 所有新skill必须通过21项安全预检才能上传

## 技能/插件使用建议

| 环节 | 技能/插件 | 用途 |
|------|----------|------|
| API令牌刷新 | agent-browser | 登录SkillHub获取新token |
| 搜索排名研究 | defuddle + WebSearch | 研究SkillHub搜索算法 |
| 排名验证 | agent-browser | 验证搜索排名提升 |
| 平台评分同步 | platform_ops + market_monitor | API获取评分写入DB |
| 自动化流水线 | daily_sync + orchestrator | 定时任务整合 |
| 代码审查 | coderabbit:code-review | 审查新增代码 |
| 完成验证 | superpowers:verification-before-completion | 完成前验证 |

## 当前Git状态

```
最新commit: 3d9983af7
推送状态: ✅ 已推送到 origin + hermes-skills
分支: main
领先origin: 0 (已同步)
```

## 当前平台状态

| 平台 | 状态 | 数量 |
|------|------|------|
| SkillHub | success | 1128 |
| SkillHub | cancelled | 1 |
| ClawHub | success | 1161 |
| ClawHub | cancelled | 2 |
| GitHub公开 | success | 1640 |
| marketing_gate/blocked | - | 1 |
| quality_gate/blocked | - | 2 |
| security_precheck/blocked | - | 0 (未触发上传) |
| pending | - | 0 |
| rejected | - | 0 |
