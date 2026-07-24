# Skill 命名规范与自动发现系统设计

> **创建时间**: 2026-07-20
> **目标**: 建立长期、持续、自动化的 Skill 生产与维护体系

---

## 一、多平台来源生态

### 1.1 可用来源平台

| 平台 | Skill数量 | 接入方式 | 许可证 | 与SkillHub兼容 | 优先级 |
|------|----------|---------|--------|---------------|--------|
| **ClawHub** | 59,900+ | CLI API + 向量搜索 | 免费公开 | 原生兼容(同源OpenClaw) | P0 |
| **Hermes Marketplace** | 未公开 | Publisher Portal + SDK | Skill自声明 | 需适配(MCP桥接) | P2 |
| **GitHub: anthropics/skills** | 17个官方 | git clone | Apache-2.0/MIT | SKILL.md格式兼容 | P1 |
| **GitHub: obra/superpowers** | 10+框架级 | 插件市场命令 | MIT | SKILL.md格式兼容 | P1 |
| **GitHub: addyosmani/agent-skills** | 多个工程类 | git clone | MIT | SKILL.md格式兼容 | P1 |
| **GitHub: ComposioHQ/awesome-claude-skills** | 1000+ | git clone | 各skill不一 | Claude Code格式兼容 | P1 |
| **GitHub: VoltAgent/awesome-openclaw-skills** | 大量 | git clone | 各skill不一 | OpenClaw格式兼容 | P1 |
| **腾讯SkillHub** | 13,000+ | 已接入 | 含SkillPay | 已在用 | P0(当前) |

### 1.2 来源优先级策略

```
P0: ClawHub (59,900+技能，最大来源池，API成熟)
P1: GitHub高星仓库 (质量高，许可证明确)
P2: Hermes Marketplace (生态独立，需适配)
P3: 其他平台 (Codex Plugins, Composio等)
```

---

## 二、命名规范

### 2.1 核心规则

**一个逻辑Skill = 两个版本 = 两个独立slug**

| 版本 | slug格式 | displayName格式 | 定价 |
|------|---------|----------------|------|
| 付费版 | `{base-slug}` | `{中文名}` | 9.90 CNY/次 |
| 免费版 | `{base-slug}-free` | `{中文名}免费版` | 无定价 |

### 2.2 版本号规则

版本号通过 `current_version` 字段管理，**不写入slug**：

| 场景 | 付费版slug | 免费版slug | version |
|------|-----------|-----------|---------|
| 初版 | `sales-copy-artisan` | `sales-copy-artisan-free` | 1.0.0 |
| Bug修复 | `sales-copy-artisan` | `sales-copy-artisan-free` | 1.0.1 |
| 功能新增 | `sales-copy-artisan` | `sales-copy-artisan-free` | 1.1.0 |
| 破坏性变更 | `sales-copy-artisan` | `sales-copy-artisan-free` | 2.0.0 |

### 2.3 slug生成规则

```
{base-slug} = kebab-case(核心功能名)
{base-slug}-free = 免费版

示例:
- 付费: geo-rank-architect     displayName: GEO占位架构师
- 免费: geo-rank-architect-free displayName: GEO占位架构师免费版

- 付费: viral-prophet           displayName: 爆款预言机
- 免费: viral-prophet-free      displayName: 爆款预言机免费版
```

### 2.4 关联机制

通过数据库字段建立付费版与免费版的关联：

```sql
-- 付费版记录
slug: sales-copy-artisan
edition: paid
parent_slug: NULL

-- 免费版记录
slug: sales-copy-artisan-free
edition: free
parent_slug: sales-copy-artisan  -- 指向付费版
```

### 2.5 数据库字段规范

| 字段 | 付费版取值 | 免费版取值 | 说明 |
|------|-----------|-----------|------|
| `slug` | `{base-slug}` | `{base-slug}-free` | 稳定标识，不含版本号 |
| `current_display_name` | `{中文名}` | `{中文名}免费版` | 用户可见名称 |
| `edition` | `paid` | `free` | 版本类型 |
| `pricing_model` | `per_call` | `free` | 定价模式 |
| `parent_slug` | NULL | `{base-slug}` | 免费版指向付费版 |
| `current_version` | `1.0.0` | `1.0.0` | 版本号同步 |
| `source_slug` | 原始skill的slug | 同付费版 | 来源溯源 |

---

## 三、本地数据治理方案

### 3.1 当前问题诊断

对本地1909个skill的扫描发现：

| 问题 | 影响范围 | 严重度 |
|------|---------|--------|
| slug含`-free`/`-pro`后缀 | 1216条(64%) | 严重 |
| 版本号写入slug | 24条 | 中等 |
| 同一skill拆成多条记录 | 大量(如xxx-free + xxx-pro) | 严重 |
| pricing_model与edition语义混乱 | 876条pricing_model为空 | 严重 |
| category被source污染 | 59条(opensource/original) | 轻微 |
| display_name绑定定价词 | 1087条 | 中等 |
| platform_uploads缺唯一约束 | 重复记录 | 轻微 |

### 3.2 治理策略

**原则: 不破坏已上传到平台的slug，新skill严格执行新规范**

#### 策略A: 已上传skill保持不变
- 已上传到SkillHub/clawhub的103个skill保持现有slug
- 在DB中添加 `legacy_slug` 字段标记旧命名
- 后续版本更新时保持原slug不变

#### 策略B: 未上传skill执行迁移
- 将 `xxx-tool-free` 和 `xxx-tool-pro` 合并为一个逻辑skill
- 付费版slug = 去除后缀的base slug
- 免费版slug = base slug + `-free`
- 用 `parent_slug` 建立关联

#### 策略C: 新增skill严格执行新规范
- 自动发现的新skill一律按2.1规则命名
- 不允许版本号写入slug
- 不允许edition后缀以外的定价词出现在slug中

---

## 四、自动发现系统设计

### 4.1 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                    自动发现系统                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │ ClawHub  │  │ GitHub   │  │ Hermes   │  → 来源层   │
│  │ Scanner  │  │ Watcher  │  │ Monitor  │             │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘             │
│       │              │              │                    │
│       └──────────────┼──────────────┘                    │
│                      ▼                                   │
│              ┌──────────────┐                            │
│              │  去重比对器   │  → 过滤层                 │
│              │  (vs DB)     │                            │
│              └──────┬───────┘                            │
│                     ▼                                    │
│              ┌──────────────┐                            │
│              │  差异化引擎   │  → 加工层                 │
│              │  (AI驱动)    │                            │
│              └──────┬───────┘                            │
│                     ▼                                    │
│              ┌──────────────┐                            │
│              │ 双版本生成器  │  → 产出层                 │
│              │ (paid+free)  │                            │
│              └──────┬───────┘                            │
│                     ▼                                    │
│              ┌──────────────┐                            │
│              │  平台同步器   │  → 发布层                 │
│              │ (CLI+API)    │                            │
│              └──────────────┘                            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 4.2 来源扫描器

#### ClawHub扫描器
```python
# 扫描clawhub最新skill列表
clawhub search --category {category} --sort newest --limit 100
# 下载skill
clawhub install {slug}
# 批量更新
clawhub update --all
```

#### GitHub仓库监控器
```python
# 监控指定仓库的release
repos = [
    "anthropics/skills",
    "obra/superpowers",
    "addyosmani/agent-skills",
    "ComposioHQ/awesome-claude-skills",
    "VoltAgent/awesome-openclaw-skills",
]
# 定时拉取最新commit/release
git fetch && git log --oneline -10
```

#### Hermes监控器
```python
# Hermes Publisher Portal API
GET https://hermes.nousresearch.com/api/skills?sort=newest
```

### 4.3 去重比对逻辑

```python
def is_new_skill(source_slug, source_platform):
    """检查是否为本地不存在的新skill"""
    # 1. 精确匹配source_slug
    existing = db.query("""
        SELECT id FROM skills 
        WHERE source_slug = ? AND source = ?
    """, (source_slug, source_platform))
    if existing:
        return False
    
    # 2. 模糊匹配displayName (防止同名不同slug)
    existing = db.query("""
        SELECT id FROM skills 
        WHERE current_display_name LIKE ?
    """, (f"%{display_name}%",))
    if existing:
        return False
    
    return True
```

### 4.4 差异化改造流程

对每个新发现的skill执行：

1. **去标识化**: 移除原始仓库名、作者名、开源项目烙印
2. **质量增强**: 
   - 补充三层介绍(displayName/summary/SKILL.md)
   - 添加依赖说明
   - 优化prompt结构
3. **中文化**: displayName和summary中文化
4. **定价评估**: 根据功能复杂度确定定价档位
5. **生成双版本**: 付费版 + 免费版

### 4.5 触发机制

| 触发方式 | 说明 |
|---------|------|
| 用户输入"发现" | 手动触发全量扫描 |
| 用户输入"更新" | 触发更新机制(已有skill的版本检查) |
| 定时任务 | 每日/每周自动扫描新skill |
| 增量触发 | 用户指定来源平台后扫描 |

---

## 五、实施计划

### Phase 1: 数据治理 (当前)
- [ ] 清理DB中pricing_model/edition字段不一致问题
- [ ] 为已上传的103个skill添加legacy_slug标记
- [ ] 建立slug迁移映射表

### Phase 2: 自动发现脚本
- [ ] 创建 `auto_discover.py` 主控脚本
- [ ] 实现ClawHub扫描器
- [ ] 实现GitHub仓库监控器
- [ ] 实现去重比对器

### Phase 3: 差异化自动化
- [ ] 创建差异化模板库
- [ ] 实现AI驱动的差异化改造流程
- [ ] 实现双版本自动生成

### Phase 4: 持续运营
- [ ] 定时任务配置
- [ ] 监控仪表盘
- [ ] 质量评分系统

---

## 六、文件清单

| 文件 | 路径 | 作用 |
|------|------|------|
| 本设计文档 | `d:\skills\skill-registry\NAMING_CONVENTION.md` | 命名规范与系统设计 |
| 自动发现脚本 | `d:\skills\skill-registry\auto_discover.py` | 来源扫描+去重+差异化 |
| 数据治理脚本 | `d:\skills\skill-registry\clean_naming.py` | 清理现有命名问题 |
| 来源配置 | `d:\skills\skill-registry\sources.yaml` | 来源平台配置 |
| 更新机制 | `d:\skills\skill-registry\update_mechanism.py` | 已有skill的版本更新 |
| 触发指令 | `d:\skills\skill-registry\UPDATE_TRIGGER.md` | 更新流程AI手册 |
| 发现指令 | `d:\skills\skill-registry\DISCOVER_TRIGGER.md` | 发现流程AI手册 |

---

## 七、与更新机制的协作

| 触发词 | 执行的系统 | 作用 |
|--------|----------|------|
| "更新" | update_mechanism.py | 检查已有skill的来源更新，升级版本 |
| "发现" | auto_discover.py | 扫描平台发现新skill，差异化后发布 |
| "治理" | clean_naming.py | 清理DB中的命名规范问题 |

三个系统共享 `skill-registry.db`，通过 `source_slug` 和 `parent_slug` 建立完整的溯源链路。
