# 新对话启动包 — 任务清单 (v2.0)

> **日期**: 2026-07-26
> **版本**: v2.0 (方案C: 流程+质量门禁架构)
> **配套文档**: new-conversation-starter-design.md v2.0 (详细设计)
> **执行原则**: 增强已有代码，不创建碎片化新文件；不模拟/mock；幂等操作；向后兼容；全链路修复(底层数据→中间模块→前端)；高质量碎片融合
> **重组依据**: 9项需求差距分析矩阵 (design.md 第八章)

---

## 任务总览

| 优先级 | 需求覆盖 | 任务数 | 核心目标 |
|--------|---------|--------|---------|
| P0 | 需求1(质量检测) + 需求4(防幻觉) | 4 | 质量门禁系统增强 + L2/L3集成 + 防幻觉机制 + 持续运营 |
| P1 | 需求2(平台经验) + 需求3(营销关卡) | 3 | 营销数据质量门禁 + 平台操作固化 |
| P2 | 需求5(自动化) + 需求7(多平台同步) + 需求8(升级触发) | 4 | 自动生命周期 + 反馈闭环 + 平台评分同步 |
| P3 | 需求6(反碎片化) + 需求9(流程体系化) | 3 | 数据源统一 + 代码碎片融合 + 文档对齐 |
| **合计** | **9项需求全覆盖** | **14** | |

### v1.0已完成任务 (V62-V64)

| v1.0任务 | 状态 | 完成轮次 |
|---------|------|---------|
| P0-1 循环审核 pending→admin_review | ✅完成 | V60-V63 |
| P0-2 持续处理rejected | ✅完成 | V61-V63 |
| P0-3 四平台同步机制建设 | ✅完成 | V62-V63 |
| P1-1 Verified认证 | ✅完成 | V63 |
| P1-2 Downloads/stars | ✅完成 | V63 |
| P1-3 三轨关联字段 | ✅完成 | V62 |
| P1-4 GitHub双仓库DB区分 | ✅完成 | V62 |
| P2-3 v_skill_lifecycle视图 | ✅完成 | V62 |
| P2-5 JSON与DB统一 | ✅完成 | V62-V63 |

---

## P0 — 质量门禁系统 + 防幻觉机制 (需求1, 4)

### P0-1: 营销关卡实现 (需求3前置, 但属P0质量基础设施)

| 项目 | 内容 |
|------|------|
| **目标** | 在quality_gate.py中新增营销数据质量门禁，作为上传前置关卡 |
| **需求映射** | 需求3(营销数据质量关卡) — 但作为质量门禁基础设施，提升至P0 |
| **缺口** | tags/category/name/pricing未作为统一上传前置关卡 |
| **影响文件** | `tools/quality_gate.py`, `tools/version_sync_pipeline.py` |
| **修复原则** | 全链路: quality_gate.py(检查函数) → version_sync_pipeline.py(集成到流水线) → enterprise_uploader.py(上传前调用) |

**详细步骤**:

在 `quality_gate.py` 中新增 `run_marketing_gate()` 函数，包含7项检查:

```python
def run_marketing_gate(skill_md_path: Path) -> dict:
    """营销数据质量门禁检查
    
    在L1静态格式检查通过后，检查营销关键数据:
    1. displayName中文化且≤20字符
    2. summary营销优化且≤100字符  
    3. description 150-280字符, 非模板化
    4. tags 5-10个, 与功能匹配
    5. categoryIds正确映射(非空, 匹配10个分类之一)
    6. pricing合理性(pricing_tier匹配skill复杂度)
    7. license合规(free=MIT, paid=Proprietary)
    """
```

**验证**:
- `python quality_gate.py <path> --marketing` 输出营销关卡结果
- version_sync_pipeline中L1通过后自动执行营销关卡
- 营销关卡未通过的skill被阻止上传

### P0-2: 防幻觉机制实现 (需求4)

| 项目 | 内容 |
|------|------|
| **目标** | 在quality_gate.py中新增防幻觉检查，防止AI虚假实现和需求理解偏差 |
| **需求映射** | 需求4(AI自动化防幻觉) |
| **缺口** | 无交叉验证; 无需求理解偏差检测; 无虚假实现检测 |
| **影响文件** | `tools/quality_gate.py`, `tools/version_sync_pipeline.py` |
| **修复原则** | 全链路: quality_gate.py(检测函数) → version_sync_pipeline.py(集成) → upgrade_single_skill(独立升级时调用) |

**详细步骤**:

在 `quality_gate.py` 中新增 `run_anti_hallucination()` 函数，包含3项检查:

```python
def run_anti_hallucination(skill_md_path: Path, l2_report: dict = None, 
                           l3_report: dict = None, l4_report: dict = None) -> dict:
    """防幻觉机制检查
    
    1. 交叉验证: L2 TRACE评分 vs L3 Agent试用 vs L4-L9审计
       - 如果三层评分差异>20分，标记为"评分分歧"，需人工复核
       - 如果三层中有任意一层未通过，总体未通过
    
    2. 需求理解偏差检测: 实际内容 vs description声明
       - 提取description中的关键功能声明
       - 检查body中是否包含对应实现
       - 如果声明了某功能但body中无对应内容，标记为"需求理解偏差"
    
    3. 虚假实现检测: 无占位符/无模板/无空函数体
       - 检查代码块是否为空或仅含注释
       - 检查是否有 TODO/FIXME/placeholder 标记
       - 检查函数体是否为 pass/.../NotImplemented
    """
```

**验证**:
- `python quality_gate.py <path> --anti-hallucination` 输出防幻觉检查结果
- 有虚假实现的skill被阻止上传
- 交叉验证发现评分分歧时标记警告

### P0-3: L2/L3集成到version_sync_pipeline (需求1)

| 项目 | 内容 |
|------|------|
| **目标** | 将L2 LLM验证和L3 Agent试用集成到version_sync_pipeline，复用update_mechanism的成熟模式 |
| **需求映射** | 需求1(真正有效的质量检测) |
| **缺口** | version_sync_pipeline仅集成L1+L1.5, 未集成L2/L3; update_mechanism已集成但两套流水线割裂 |
| **影响文件** | `tools/version_sync_pipeline.py` |
| **修复原则** | 复用update_mechanism.py的L2/L3检查模式(check report exists)，不重新实现; 统一到同一检查逻辑 |

**详细步骤**:

1. 在 `version_sync_pipeline.py` 的 `sync_skill_to_all_platforms()` 中，L1.5通过后:
   - 检查 `l2_final_report_{slug}.json` 是否存在
   - 如果存在，验证TRACE总分≥35
   - 如果不存在，标记为`blocked_by_l2_pending`，生成L2验证报告供AI执行

2. L2通过后:
   - 检查 `l3_final_report_{slug}.json` 是否存在
   - 如果存在，验证评分≥70
   - 如果不存在，标记为`blocked_by_l3_pending`，生成L3试用提示供AI执行

3. 添加 `--skip-l2` 和 `--skip-l3` 参数，仅用于批量场景(与update_mechanism一致)

**验证**:
- version_sync_pipeline sync <slug> 现在执行L1→L1.5→L2→L3完整链路
- 无L2/L3报告的skill被正确阻止，并给出AI执行指引
- update_mechanism和version_sync_pipeline使用相同的L2/L3检查逻辑

### P0-4: 持续运营 (循环任务)

| 项目 | 内容 |
|------|------|
| **目标** | 持续审核pending、处理rejected、监控平台状态 |
| **命令** | 循环执行审核和rejected处理脚本 |
| **循环** | 每30分钟执行一次 |

**详细步骤**:
1. 检查pending数量，如>10则运行审核脚本
2. 检查rejected数量，如>0则处理
3. 检查platform_review数量，跟踪平台审核进度
4. 记录运营状态到DB

---

## P1 — 营销关卡 + 平台经验固化 (需求2, 3)

### P1-1: 平台操作固化到platform_ops.py (需求2)

| 项目 | 内容 |
|------|------|
| **目标** | 将散落在多个脚本中的star/download/审核/发布操作统一到platform_ops.py |
| **需求映射** | 需求2(平台经验固化) |
| **缺口** | star/download/审核/发布操作散落在batch_approve_api.py, handle_rejected_v2.py, auto_publish.py等多个脚本 |
| **影响文件** | `tools/platform_ops.py` (增强), `tools/orchestrator.py` (调用) |
| **修复原则** | 高质量融合: 将分散操作整合为统一API，不破坏现有脚本; platform_ops作为唯一平台操作入口 |

**详细步骤**:

在 `platform_ops.py` 中新增统一操作函数:
```python
def star_skill(slug: str) -> dict:           # 复用V63已实现的Star API
def batch_approve(slugs: list) -> dict:       # 复用batch_approve_api逻辑
def handle_rejected(slug: str) -> dict:       # 复用handle_rejected_v2逻辑
def auto_publish(slug: str) -> dict:          # 复用auto_publish逻辑
def get_platform_status(slug: str) -> dict:   # 统一状态查询
def run_platform_pipeline(slug: str) -> dict: # 一键执行: star→approve→publish
```

**验证**:
- platform_ops.py成为平台操作的唯一入口
- orchestrator.py调用platform_ops而非直接调用散落脚本
- 现有脚本仍可独立运行(向后兼容)

### P1-2: 营销关卡集成到上传流水线 (需求3)

| 项目 | 内容 |
|------|------|
| **目标** | 将P0-1实现的营销关卡集成到version_sync_pipeline和enterprise_uploader |
| **需求映射** | 需求3(营销数据质量关卡) |
| **影响文件** | `tools/version_sync_pipeline.py`, `tools/enterprise_uploader.py` |
| **依赖** | P0-1完成 |

**详细步骤**:
1. 在version_sync_pipeline的sync流程中，L1.5之后、L2之前插入营销关卡检查
2. 在enterprise_uploader的上传前检查中调用营销关卡
3. 营销关卡未通过的skill给出具体修复建议

### P1-3: 搜索排名优化 (延续v1.0 P2-2)

| 项目 | 内容 |
|------|------|
| **目标** | 提升skill在SkillHub搜索结果中的排名 |
| **因素** | stars✅、downloads、更新时间、分类匹配、关键词 |
| **技能/插件** | `defuddle`(研究排名算法) → `agent-browser`(验证) |

---

## P2 — 自动生命周期 + 反馈闭环 + 多平台同步 (需求5, 7, 8)

### P2-1: 平台评分同步到DB (需求7)

| 项目 | 内容 |
|------|------|
| **目标** | 将SkillHub平台AI评分、用户评分、下载数同步到本地DB |
| **需求映射** | 需求7(多平台状态同步) |
| **缺口** | 平台AI评价未写入DB; 用户评论未获取; 无定时同步 |
| **影响文件** | `tools/db.py` (新增字段), `tools/market_monitor.py` (增强) |

**详细步骤**:

1. DB新增字段:
```sql
ALTER TABLE skills ADD COLUMN platform_rating REAL DEFAULT 0;
ALTER TABLE skills ADD COLUMN platform_rating_count INTEGER DEFAULT 0;
ALTER TABLE skills ADD COLUMN platform_downloads INTEGER DEFAULT 0;
ALTER TABLE skills ADD COLUMN platform_ai_review TEXT;  -- JSON格式存储AI测评结果
ALTER TABLE skills ADD COLUMN last_platform_sync_at TEXT;
```

2. market_monitor.py增强:
```python
def sync_platform_ratings():
    """定期从SkillHub获取评分并写入DB"""
    # GET /api/v1/skills/{slug} 获取 avgRating, reviewCount, downloads
    # 写入DB: platform_rating, platform_rating_count, platform_downloads
```

**验证**:
- DB有platform_rating等字段且已回填
- market_monitor能定时同步平台评分

### P2-2: 平台低评分触发升级 (需求8)

| 项目 | 内容 |
|------|------|
| **目标** | 当平台评分低于阈值时自动触发skill升级 |
| **需求映射** | 需求8(升级触发机制) |
| **缺口** | 无平台低评分触发(触发b); 无持续监控循环 |
| **影响文件** | `tools/market_monitor.py`, `tools/upgrade_checker.py` |
| **依赖** | P2-1完成 |

**详细步骤**:

```python
# market_monitor.py新增
RATING_THRESHOLD = 4.0  # 可配置

def check_low_rating_skills():
    """检查评分低于阈值的skill，触发升级"""
    # SELECT slug FROM skills WHERE platform_rating < RATING_THRESHOLD AND platform_rating > 0
    # 对每个低评分skill:
    #   1. 分析低评分原因(从platform_ai_review提取)
    #   2. 触发 upgrade_single_skill(slug)
    #   3. 记录升级触发原因到DB
```

**验证**:
- 评分<4.0的skill自动触发升级流程
- 升级触发原因记录到DB

### P2-3: 自动化流水线完善 (需求5)

| 项目 | 内容 |
|------|------|
| **目标** | 完善daily_sync.py，实现定时自动化: 发现→增强→质量门禁→上传→审核→发布→收藏→反馈→升级 |
| **需求映射** | 需求5(自动化流水线) |
| **缺口** | L2/L3需人工; 无持续监控; 无自动升级触发b |
| **影响文件** | `tools/daily_sync.py` (增强), `tools/orchestrator.py` |

**详细步骤**:
1. daily_sync.py整合所有循环任务:
   - 持续审核pending/rejected
   - 定期同步平台评分
   - 检查低评分触发升级
   - 检查源版本变更触发升级
2. orchestrator.py修复config导入bug，作为手动触发入口

### P2-4: 所有权认领 (延续v1.0 P2-1)

| 项目 | 内容 |
|------|------|
| **目标** | 确保所有skill在本团队名下 |
| **技能/插件** | `agent-browser` |

---

## P3 — 流程统一 + 碎片化代码统合 (需求6, 9)

### P3-1: 统一数据源到SQLite (需求6)

| 项目 | 内容 |
|------|------|
| **目标** | 消除双数据源，upgrade_checker从JSON迁移到SQLite |
| **需求映射** | 需求6(反碎片化) |
| **缺口** | upgrade_checker用JSON vs orchestrator用SQLite; config导入有bug; 重复实现find_skill_md |
| **影响文件** | `tools/upgrade_checker.py`, `tools/orchestrator.py`, `tools/skill_core/` |
| **修复原则** | 高质量融合: 以SQLite为唯一数据源，JSON降级为导出/缓存; 统一find_skill_md到skill_core |

**详细步骤**:

1. upgrade_checker.py迁移:
   - 将`upload_tracking.json`的数据读取改为从DB `platform_uploads`表读取
   - 保留JSON导出功能(DB → JSON导出)

2. find_skill_md统一:
   - 将version_sync_pipeline.py、update_mechanism.py、skill_batch_upgrader_v3.py中的find_skill_md统一到`skill_core/parser.py`
   - 统一搜索4个目录: packaged-skills, opensource-skills, differentiated-skills, enterprise-upload

3. orchestrator.py修复:
   - 修复SKILL_DATA_DIR等未定义变量
   - 从project_config导入所有需要的常量

**验证**:
- upgrade_checker从DB读取数据，不再依赖JSON
- find_skill_md在skill_core/中有唯一实现
- orchestrator.py无import错误

### P3-2: 质量检查统一入口 (需求6)

| 项目 | 内容 |
|------|------|
| **目标** | 统一质量检查入口: L1+L1.5+营销+防幻觉 → quality_gate.py统一调用 |
| **需求映射** | 需求6(反碎片化) |
| **缺口** | 质量检查分散在quality_gate(L1) + batch_upgrader(L1.5) + deep_audit(L4-L9) |
| **影响文件** | `tools/quality_gate.py` (增强为统一入口) |

**详细步骤**:
1. quality_gate.py新增 `run_full_quality_check()` 函数:
   ```python
   def run_full_quality_check(skill_md_path: Path, 
                               include_l2l3: bool = False) -> dict:
       """统一质量检查入口
       L1(13项) → L1.5(7项) → 营销关卡(7项) → 防幻觉(3项)
       可选: L2/L3报告检查
       """
   ```
2. 所有调用方统一使用此入口

### P3-3: 文档与代码对齐 (需求9)

| 项目 | 内容 |
|------|------|
| **目标** | 确保ARCHITECTURE.md和starter-design.md v2.0与代码完全对齐 |
| **需求映射** | 需求9(全业务流程体系化) |
| **影响文件** | `docs/ARCHITECTURE.md`, `docs/plans/new-conversation-starter-design.md` |

---

## 任务依赖关系

```
P0-1 (营销关卡) ──→ P1-2 (营销关卡集成) ─────────────────┐
                                                          │
P0-2 (防幻觉机制) ────────────────────────────────────────┤
                                                          │
P0-3 (L2/L3集成) ──→ P2-3 (自动化流水线) ────────────────┤
                                                          │
P0-4 (持续运营) ────循环执行─────────────────────────────┤
                                                          │
P1-1 (平台操作固化) ──→ P2-3 (自动化流水线) ─────────────┤
P1-3 (搜索排名) ────可并行──────────────────────────────┤
                                                          │
P2-1 (平台评分同步) ──→ P2-2 (低评分触发升级) ──────────┤
P2-4 (所有权认领) ────可并行─────────────────────────────┤
                                                          │
P3-1 (数据源统一) ──→ P3-2 (质量检查统一) ──→ P3-3 (文档对齐) │
```

---

## 验证检查清单

### P0 验证
- [ ] quality_gate.py包含run_marketing_gate()函数，7项检查全部可执行
- [ ] quality_gate.py包含run_anti_hallucination()函数，3项检查全部可执行
- [ ] version_sync_pipeline sync <slug> 执行L1→L1.5→营销→防幻觉→L2→L3完整链路
- [ ] 无L2/L3报告的skill被阻止上传并给出AI执行指引
- [ ] 有虚假实现的skill被营销关卡或防幻觉机制阻止
- [ ] pending<10, rejected趋近0

### P1 验证
- [ ] platform_ops.py包含star/approve/handle_rejected/publish/status/pipeline统一函数
- [ ] orchestrator.py通过platform_ops调用平台操作
- [ ] version_sync_pipeline中L1.5后自动执行营销关卡
- [ ] enterprise_uploader上传前调用营销关卡
- [ ] 搜索排名提升

### P2 验证
- [ ] DB有platform_rating/platform_rating_count/platform_downloads/platform_ai_review字段
- [ ] market_monitor能定时同步平台评分到DB
- [ ] 评分<4.0的skill自动触发upgrade_single_skill
- [ ] daily_sync.py整合所有循环任务

### P3 验证
- [ ] upgrade_checker从DB读取数据，不依赖JSON
- [ ] find_skill_md在skill_core/中有唯一实现，所有脚本从此导入
- [ ] orchestrator.py无import错误
- [ ] quality_gate.py包含run_full_quality_check()统一入口
- [ ] ARCHITECTURE.md与代码完全对齐

---

## 每轮对话结束标准

每轮对话完成时必须:
1. 执行Git提交: `git add -A; git commit -m "feat: V66 — [描述]"; git push origin main; git push hermes-skills main`
2. 生成下一轮提示词: `next-round-prompt-v67.0.md`
3. 更新本任务清单的完成状态
4. 使用 `superpowers:verification-before-completion` 验证所有声称完成的任务
5. 运行 `python -c "import py_compile; py_compile.compile('tools/quality_gate.py')"` 验证语法
6. 运行 `python -c "import py_compile; py_compile.compile('tools/version_sync_pipeline.py')"` 验证语法
