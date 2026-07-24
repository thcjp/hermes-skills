# 第50轮提示词 (v50.0修订版) — SkillHub可见性优先 + hermes-skills仓库重构 + 多平台版本同步 + 分类统一

> **日期**: 2026-07-24
> **上一轮完成**: V49 — 全层级100%A级达成, GitHub双仓库推送成功 (commit 6795a1655 + 7b0a18c56)
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库
> **里程碑**: 🎯 全层级审计100%A级达成 — 历史最佳
> **最高优先级**: 💰 SkillHub前台可见性 — 做出来是为了引流和赚钱的

## V49完成总结

| 任务 | 状态 | 结果 |
|------|------|------|
| L9 MISSING_VALUE_PROPOSITION收敛 | ✅ | 120→0 |
| L9 MISSING_OR_IRRELEVANT_TAGS收敛 | ✅ | 77→0 |
| L8 TAG_MISMATCH修复 | ✅ | 3→0 |
| fix_missing_fields.py根因修复 | ✅ | VP关键词与审计对齐 |
| Dashboard API端点验证 | ✅ | /api/stats, /api/l9-visibility, /api/l7-audit 全部正常 |
| Git提交 | ✅ | commit 6795a1655 (279文件) |
| GitHub推送 | ✅ | origin + hermes-skills 均推送成功 (caba75978..7b0a18c56) |

## V49审计最终结果 — 🏆 全部100%A级

| 审计层 | A级 | B级 | C级 | 平均分 | 通过率 |
|--------|-----|-----|-----|--------|--------|
| L4 功能质量 | 2097 | 0 | 0 | 93.7 | 100% |
| L5 可销售性 | 2097 | 0 | 0 | 90.4 | 100% |
| L6 内容真实性 | 2097 | 0 | 0 | 100.0 | 100% |
| L7a 语义模板 | 2097 | 0 | 0 | 100.0 | 100% |
| L7b 可执行性 | 2097 | 0 | 0 | 100.0 | 100% |
| L8 安全审计 | 2097 | 0 | 0 | 100.0 | 100% |
| L9 可见性质量 | 2097 | 0 | 0 | 100.0 | 100% |

### 平台状态 (upload_tracking.json)

| 平台 | 成功 | 待处理 | 失败/拒绝 |
|------|------|--------|----------|
| SkillHub | 2036 published (本地标记) | 2 pending + 1 admin + 17 platform_review | 20 rejected + 9 deleted |
| ClawHub | 228 published | 704 not_uploaded | 1153 not_eligible |
| Community | 4032 published | — | 40 failed |
| Hermes | 759 eligible (仅免费) | 1326 not_eligible (付费未推送) | — |

### SkillHub可见性根因

| 根因 | 证据 | 影响 |
|------|------|------|
| CLI无publish命令 | v0.4.1仅支持install/search/list/config | 无法通过CLI上传skill |
| 数据库标记≠平台状态 | 1120条success记录是V45本地DB设置 | DB状态不代表平台状态 |
| download_ready全NULL | 1120条记录download_ready均为NULL | 从未验证平台是否处理了版本 |
| 实际搜索验证失败 | `npx skillhub search`找不到我们的skill | 确认前台不可见 |

### 当前hermes-skills仓库问题

| 问题 | 现状 | 期望 |
|------|------|------|
| 仅含免费skill | 759个-free后缀目录 | 应含付费版（与clawhub付费版一致） |
| 无分类目录结构 | 扁平目录，所有skill在同一层 | 按category分类（Agents/Automation/...） |
| 无多语言目录 | 仅README.md + README.en.md | 需zh-CN/zh-TW/en三语分类索引 |
| 付费skill全部闭源 | push_paid=False | 部分付费skill应开源引流 |

## 实施任务

### 任务1: SkillHub前台可见性修复 — 浏览器发布 (最高优先级)

**问题**: SkillHub前台完全看不到我们的skill，无法引流和赚钱。CLI无publish命令，1120个"success"仅为本地DB标记。

**根因**: 从未真正上传到SkillHub平台，仅在本地DB设置了community_published=1和visibility=public。

**修复方案**:
1. 确认用户已登录 https://www.skillhub.cn
2. 在浏览器控制台执行 `tools/community_publish.js`
3. 脚本自动:
   - 获取所有skill列表（含visibility/download_ready/namespace信息）
   - 生成可见性诊断报告
   - 筛选 org_only + NULL visibility 的skill
   - 批量调用 `POST /admin/skills/{slug}/publish-to-community` API
   - 处理slug冲突（自动追加-sk后缀）
4. 执行后复制结果: `JSON.stringify(window.__publishResults)`
5. 更新数据库状态和upload_tracking.json
6. **验证**: `npx skillhub search "关键词"` 能找到我们的skill

**优先发布顺序**: P0(8零依赖) → P1(5获奖) → P2(3已获奖) → P3(12变现) → P4+P5(32开源改造)

**验证标准**: 至少10个skill在SkillHub前台可搜索到

### 任务2: hermes-skills仓库重构 — 分类目录 + 付费版 + 多语言索引

**问题**: hermes-skills仓库目前仅含免费skill（扁平目录），缺少付费版和分类结构。用户要求：
- 传收费的版本（和clawhub收费版本一致），不要把收费的全部开源
- 做一个分类目录，中文（繁体简体）英文，按分类排序
- 分类汇总skillhub、clawhub的，在本地就建立好分类，上传平台也同样分类

**修复方案**:

#### 2.1 修改platform_config.py推送策略
```python
# 修改前: hermes-skills仅推免费
GITHUB_REPOS = [
    {"name": "hermes-skills", "push_free": True, "push_paid": False},
    {"name": "origin", "push_free": True, "push_paid": True},
]

# 修改后: hermes-skills推免费+部分付费（与clawhub付费版一致）
GITHUB_REPOS = [
    {"name": "hermes-skills", "push_free": True, "push_paid": True, "paid_strategy": "clawhub_aligned"},
    {"name": "origin", "push_free": True, "push_paid": True},
]
```

#### 2.2 创建分类目录结构
```
hermes-skills/
├── README.md                    # 中文简体索引
├── README.zh-CN.md              # 中文简体
├── README.zh-TW.md              # 中文繁体
├── README.en.md                 # 英文索引
├── Agents/                      # AI代理
│   ├── README.md                # 分类说明（三语）
│   ├── free/                     # 免费版
│   │   ├── ai-agent-helper-free/SKILL.md
│   │   └── ...
│   └── paid/                     # 付费版（与clawhub一致）
│       ├── ai-agent-helper-pro/SKILL.md
│       └── ...
├── Automation/                  # 自动化
│   ├── README.md
│   ├── free/
│   └── paid/
├── Communication/               # 通信
├── Creative/                    # 创意
├── Development/                 # 开发
├── Finance/                     # 金融
├── Integrations/                # 集成
├── Knowledge/                   # 知识
├── Lifestyle/                   # 生活
├── Operations/                  # 运维
├── Other/                       # 其他
├── Productivity/                # 效率
├── Research/                    # 研究
└── Security/                    # 安全
```

#### 2.3 实现步骤
1. 从`differentiated-skills/`读取所有skill的category字段
2. 从`packaged-skills/skillhub/`读取所有免费skill
3. 从`packaged-skills/clawhub/`或`enterprise-upload/`读取付费skill
4. 按category创建分类目录，移动skill到对应`free/`或`paid/`子目录
5. 为每个category目录创建README.md（三语分类说明）
6. 创建顶层README.md/README.zh-CN.md/README.zh-TW.md/README.en.md（三语总索引）
7. 提交并推送到hermes-skills仓库

**验证**: hermes-skills仓库含14个分类目录，每个含free/paid子目录，三语README

### 任务3: 多平台版本同步机制 — 本地升级自动同步到全部平台

**问题**: 后续凡是本地skill（产品型）升级版本了，都必须同步升级发布出去的全部收费免费的对应skill。

**修复方案**: 增强`tools/version_sync_pipeline.py`的`sync_skill_to_all_platforms()`函数:

1. **版本升级检测**: 当本地SKILL.md的version字段变更时
2. **自动同步触发**:
   - **SkillHub**: 浏览器API重新发布（如已实现community_publish.js）
   - **ClawHub**: `npx clawhub publish [path] --version [new_version]`
   - **GitHub hermes-skills**: `git add → git commit → git push hermes-skills main`
   - **GitHub origin**: `git push origin main`
3. **同步日志**: 记录到upload_tracking.json和数据库platform_uploads表
4. **验证**: 确认所有平台版本号一致

**实现**: 在`sync_skill_to_all_platforms()`中增加：
```python
# 版本变更检测
old_version = get_platform_version(slug, platform)
if old_version and version.parse(new_version) > version.parse(old_version):
    # 触发平台重新发布
    for platform in ['skillhub', 'clawhub', 'github_public', 'github_private']:
        sync_to_platform(slug, skill_md, new_version, platform)
```

**验证**: 手动修改一个skill的version，运行pipeline，确认4个平台同步更新

### 任务4: 多平台分类统一 — 本地分类=平台分类

**问题**: 用户要求"在本地就建立好分类，上传平台也同样分类"。当前各平台分类可能不一致。

**修复方案**:
1. 确认14个标准category（与skillhub/clawhub对齐）:
   Agents, Automation, Communication, Creative, Development, Finance,
   Integrations, Knowledge, Lifestyle, Operations, Other, Productivity,
   Research, Security
2. 检查所有SKILL.md的frontmatter category字段
3. 确保category值在14个标准值范围内
4. 在hermes-skills仓库的目录结构中使用相同分类
5. 在SkillHub/ClawHub上传时使用相同category

**验证**: 所有2097个skill的category字段均为14个标准值之一

### 任务5: 数据库重建

**问题**: skills.db无表，需重建

**实现**:
1. 运行: `python tools/daily_sync.py`
2. 验证表结构和数据
3. 验证Dashboard API端点

**验证**: `SELECT COUNT(*) FROM skills` 返回2882+

### 任务6: ClawHub 704个待上传技能

**问题**: ClawHub有704个未上传技能，原定时任务已丢失

**实现**:
1. 从upload_tracking.json获取704个not_uploaded技能列表
2. 使用`npx clawhub publish`批量上传（每日200限制）
3. 创建新的定时任务: 每日12:00(Beijing time)上传200个
4. 处理VERSION_EXISTS错误（递增版本号）
5. 处理protected namespace错误（重命名）

**验证**: ClawHub published从228提升至500+

### 任务7: SkillHub 8个retry_pending技能重试

**问题**: 8个技能处于retry_pending状态

**技能列表**: cdp-browser-master, cron-guard, linear-workflow-bot, ai-artist-workstation, sales-copy-writer, accounting-and-finance, accounting-finance, ace-music

**实现**:
1. 检查每个skill的SKILL.md是否通过L1-L9审计（已100%A级）
2. 通过浏览器Admin API重新上传
3. 更新upload_tracking.json状态

**验证**: retry_pending从8降至0

### 任务8: 平台上传状态同步

**问题**: upload_tracking.json中的状态可能与平台实际状态不一致

**实现**:
1. 从SkillHub API获取实际skill状态
2. 从ClawHub API获取实际skill状态
3. 更新upload_tracking.json中的status和visibility字段
4. 更新数据库platform_uploads表

**验证**: upload_tracking.json与平台API状态一致

## 验证检查清单

- [ ] SkillHub浏览器发布验证(至少10个skill前台可搜索)
- [ ] hermes-skills仓库含14个分类目录，每个含free/paid子目录
- [ ] hermes-skills仓库含三语README（zh-CN/zh-TW/en）
- [ ] hermes-skills仓库含付费skill（与clawhub付费版一致）
- [ ] version_sync_pipeline.py支持多平台版本同步
- [ ] 所有2097个skill的category为14个标准值之一
- [ ] 数据库skills.db重建完成
- [ ] ClawHub 704个not_uploaded技能至少上传200+
- [ ] SkillHub 8个retry_pending技能全部重试
- [ ] 平台上传状态同步完成
- [ ] Git提交完成

## 约束

1. **增强已有代码** — 所有修复功能集成到现有工具脚本，不创建碎片化新文件（分类目录README除外）
2. **不模拟/mock** — 所有文件修改和数据库操作必须真实执行
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏现有命令功能
5. **内容保真** — tags增强和value proposition增强不得改变技能原有语义和功能
6. **网络容错** — GitHub推送失败不应阻塞其他任务的执行
7. **质量底线** — 不得引入任何会降低L4-L9审计等级的修改(当前100%A级)
8. **付费skill保护** — hermes-skills中的付费skill应与clawhub付费版一致，不得将全部付费skill开源
9. **分类统一** — 本地分类目录=skillhub分类=clawhub分类=hermes-skills分类
10. **版本同步** — 本地skill版本升级后，必须同步到全部3个平台的对应skill
