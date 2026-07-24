# Skill 自动发现触发机制

> **触发词**: "发现"
> **创建时间**: 2026-07-20
> **位置**: `d:\skills\skill-registry\DISCOVER_TRIGGER.md`

---

## 触发规则

当用户输入 **"发现"** 时，立即启动本文件定义的自动发现流水线。
扫描多平台来源，找出本地没有的新skill，差异化改造后发布。

---

## 执行流程（5阶段）

### 阶段1: 来源扫描 (Source Scan)

**命令**:
```bash
cd d:\skills\skill-registry
# 扫描所有来源（clawhub本地 + github仓库）
python auto_discover.py scan --source all
# 或仅扫描clawhub本地
python auto_discover.py scan --source clawhub
# 或扫描clawhub远程API
python auto_discover.py scan --source clawhub --remote --limit 30
```

**输出**: `d:\skills\skill-registry\discovery\candidates.json`

**来源平台**:
| 平台 | skill数量 | 扫描方式 |
|------|----------|---------|
| ClawHub | 59,900+ | 本地下载目录 + 远程API |
| GitHub | 10+仓库 | git clone + raw文件拉取 |
| Hermes | 未公开 | Publisher Portal API (待接入) |

---

### 阶段2: 去重比对 (Dedup)

**命令**:
```bash
python auto_discover.py dedup
```

**比对逻辑**:
1. 精确匹配 `source_slug` — 如果本地DB已有相同source_slug，跳过
2. 模糊匹配 `display_name` — 如果displayName已存在（不区分大小写），跳过
3. 匹配 `slug` — 如果生成的slug冲突，跳过

**输出**: 候选新skill列表

---

### 阶段3: 差异化改造 (Differentiation)

**AI操作**（此阶段由AI执行）:

对每个候选新skill:

1. **读取原始SKILL.md**:
   ```bash
   python auto_discover.py candidates  # 查看候选列表
   ```

2. **执行差异化改造**（遵循 `deep-differentiation-methodology.md`）:
   - 去标识化: 移除原始仓库名、作者名、开源项目烙印
   - 质量增强: 补充三层介绍(displayName/summary/SKILL.md)
   - 中文化: displayName和summary中文化
   - 添加依赖说明: `## 依赖说明` 章节
   - 优化prompt结构

3. **按命名规范生成双版本**:

   | 版本 | slug | displayName | 定价 |
   |------|------|------------|------|
   | 付费版 | `{base-slug}` | `{中文名}` | 9.90 CNY/次 |
   | 免费版 | `{base-slug}-free` | `{中文名}免费版` | 无 |

4. **保存到本地目录**:
   - 付费版: `d:\skills\packaged-skills\skillhub\{base-slug}\SKILL.md`
   - 免费版: `d:\skills\packaged-skills\skillhub\{base-slug}-free\SKILL.md`

5. **录入数据库**:
   ```bash
   python update_mechanism.py status  # 确认录入
   ```

---

### 阶段3.5: 质量验证 (Quality Gate) — P0-4新增

**目的**: 在上传前强制执行质量门禁, 挡住审核必拒问题(slug不一致/超长/缺字段/烙印残留)

**命令**:
```bash
# 单独检查1个skill
python quality_gate.py d:\skills\packaged-skills\skillhub\{slug}\SKILL.md

# 批量检查(目录)
python quality_gate.py d:\skills\packaged-skills\skillhub --json -o report.json

# 上传时自动触发(无需手动调用)
python update_mechanism.py upload {slug}
# → sync_skill_to_platform()会自动调用quality_gate, 不通过则阻止上传
```

**10项检查**:
1. 去标识化检测 (复用check_debranding.py, high级残留则fail)
2. slug==name==folder一致性 (SkillHub审核必拒点)
3. SKILL.md行数 ≤ 500 (SkillHub审核必拒点)
4. frontmatter 8必需字段齐全 (slug/name/version/displayName/summary/license/description/tools)
5. displayName ≤ 20字符
6. summary ≤ 100字符
7. tools为YAML数组格式 (非字符串)
8. frontmatter无XML尖括号
9. 无占位符 (待补充/TODO/FIXME等)
10. 无夸大词 (万能/超级/最强等)

**行为**:
- 任一high级检查fail → 阻止上传, 返回`blocked_by_quality_gate`, 记录到DB
- 全部pass → 进入阶段4上传流程
- `skip_quality_gate=True`可跳过(仅调试用, 生产环境禁止)

**集成点**: `sync_skill_to_platform()`在上传前自动调用, 无需手动运行

---

### 阶段4: 双版本生成与上传 (Dual Edition + Upload)

**命令**:
```bash
# 生成双版本payload
python update_mechanism.py generate {base-slug} --version 1.0.0 --changelog "初始版本"
python update_mechanism.py generate {base-slug}-free --version 1.0.0 --changelog "初始版本"

# 上传到平台
python update_mechanism.py upload {base-slug}       # 付费版
python update_mechanism.py upload {base-slug}-free  # 免费版
```

**上传机制**:
| 版本 | 上传方式 | 认证 | 定价 |
|------|---------|------|------|
| 付费版 | 企业API | session cookies | billingType=per_call, pricePerCall=9.90 |
| 免费版 | CLI publish | skh_ token | 无定价 |

---

### 阶段5: 结果汇报 (Report)

**AI操作**:

1. 汇总发现结果:
   - 扫描来源数
   - 发现新skill数
   - 差异化完成数
   - 上传成功数

2. 生成可视化报告（PureShowWidget）

3. 更新数据库状态

---

## 命名规范要点

### slug规则
```
付费版: {base-slug}           例: sales-copy-artisan
免费版: {base-slug}-free      例: sales-copy-artisan-free
```

### displayName规则
```
付费版: {中文名}              例: 卖货文案匠
免费版: {中文名}免费版         例: 卖货文案匠免费版
```

### 版本号
- 版本号通过 `current_version` 字段管理
- **不写入slug**
- 版本递增规则:
  - Bug修复: patch+1 (1.0.0 → 1.0.1)
  - 功能新增: minor+1 (1.0.0 → 1.1.0)
  - 破坏性变更: major+1 (1.0.0 → 2.0.0)

### 数据库关联
```sql
-- 付费版
slug: {base-slug}
edition: paid
parent_slug: NULL

-- 免费版
slug: {base-slug}-free
edition: free
parent_slug: {base-slug}  -- 指向付费版
```

---

## 与"更新"机制的协作

| 触发词 | 系统 | 作用 |
|--------|------|------|
| **"更新"** | update_mechanism.py | 检查已有skill的来源更新，升级版本 |
| **"发现"** | auto_discover.py | 扫描平台发现新skill，差异化后发布 |
| **"治理"** | clean_naming.py | 清理DB中的命名规范问题 |

---

## 完整一键执行

```bash
# 步骤1: 扫描来源
cd d:\skills\skill-registry
python auto_discover.py scan --source all

# 步骤2: 查看候选
python auto_discover.py candidates

# 步骤3: AI执行差异化改造（对每个候选skill）
# (AI读取原始SKILL.md，执行去标识化+质量增强+中文化)

# 步骤4: 生成双版本并上传
python update_mechanism.py generate {base-slug} --version 1.0.0
python update_mechanism.py upload {base-slug}
python update_mechanism.py generate {base-slug}-free --version 1.0.0
python update_mechanism.py upload {base-slug}-free

# 步骤5: 状态确认
python update_mechanism.py status
```
