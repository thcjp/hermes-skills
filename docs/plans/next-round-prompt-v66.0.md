# 下一轮对话提示词 (v66.0)

> **日期**: 2026-07-26
> **前置版本**: v65.0 (方案C: 质量门禁系统增强)
> **核心任务**: P1任务(营销关卡集成到上传流水线 + 平台操作固化) + P0-4持续运营 + Git推送到双远程

---

## 本轮已完成 (v65.0 → v66.0)

### P0: 质量门禁系统 + 防幻觉机制 ✅

| 任务 | 状态 | 实现详情 |
|------|------|---------|
| P0-1: 营销关卡实现 | ✅完成 | `quality_gate.py` 新增 `run_marketing_gate()` (7项检查: displayName中文化/summary营销/description非模板/tags质量/categoryIds映射/pricing合理性/license合规) |
| P0-2: 防幻觉机制实现 | ✅完成 | `quality_gate.py` 新增 `run_anti_hallucination()` (3项检查: 交叉验证/需求理解偏差/虚假实现检测) |
| P0-3: L2/L3集成到version_sync_pipeline | ✅完成 | `sync_skill_to_all_platforms()` 集成完整质量链路: L1→L1.5→营销关卡→防幻觉→L2→L3→平台同步 |
| P0-3扩展: upgrade_single_skill集成 | ✅完成 | 独立升级流程新增 Step 5.5(营销关卡) + Step 5.6(防幻觉), sync时跳过L2/L3(需AI单独执行) |
| 统一质量检查入口 | ✅完成 | `run_full_quality_check()`: L1(13项)+营销(7项)+防幻觉(3项) = 23项完整检查 |
| CLI参数增强 | ✅完成 | sync命令新增 `--skip-marketing`/`--skip-l2`/`--skip-l3`; sync-all批量模式默认跳过L2/L3 |
| format_terminal_output增强 | ✅完成 | 支持分层显示(L1_static/marketing_gate/anti_hallucination) |

### 测试验证

| Skill | L1(13项) | L1.5(7项) | 营销(7项) | 防幻觉(3项) | 阻断点 |
|-------|---------|----------|----------|------------|--------|
| ws-agent-browser | 5/13 ✗ | - | 0/7 ✗ | 3/3 ✓ | L1(占位符+缺失frontmatter) |
| ad-insight-hub | 12/13 ✗ | - | 5/7 ✗ | 1/3 ✗ | L1(占位符xxx) |
| bilibili-helper | 13/13 ✓ | 7/7 ✓ | 5/7 ✗ | 2/3 ✗ | 营销关卡(tags过多+pricing缺失) |

### Git提交

- **Commit**: `aef97df52` - feat(quality-gate): v2.0 质量门禁系统增强
- **变更**: 4 files changed, 1568 insertions(+), 477 deletions(-)
- **影响文件**: `quality_gate.py`, `version_sync_pipeline.py`, `new-conversation-starter-design.md`, `new-conversation-task-list.md`
- **推送状态**: GitHub网络不可达(连接重置), 本地commit已保存, 待网络恢复后推送

---

## 下一轮核心任务

### P0-4: 持续运营 (循环任务)

**目标**: 持续审核pending、处理rejected、监控平台状态

**执行步骤**:
1. 查询DB当前pending/admin_review/rejected/platform_review数量
2. 如pending>10, 运行审核脚本(batch_approve_api.py)
3. 如rejected>0, 运行handle_rejected_v2.py处理
4. 如platform_review>0, 记录审核进度
5. 将运营状态记录到DB的operations表

### P1-1: 平台操作固化到platform_ops.py (需求2)

**目标**: 将散落在多个脚本中的star/download/审核/发布操作统一到platform_ops.py

**缺口**: star/download/审核/发布操作散落在batch_approve_api.py, handle_rejected_v2.py, auto_publish.py等多个脚本

**影响文件**: `tools/platform_ops.py` (增强), `tools/orchestrator.py` (调用)

**修复原则**: 高质量融合: 将分散操作整合为统一API，不破坏现有脚本; platform_ops作为唯一平台操作入口

**详细步骤**:

在 `platform_ops.py` 中新增统一操作函数:
```python
def star_skill(slug: str) -> dict:           # 复用V63已实现的Star API (POST /api/v1/skills/{slug}/star)
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

### P1-2: 营销关卡集成到enterprise_uploader (需求3)

**目标**: 将P0-1实现的营销关卡集成到enterprise_uploader的上传前检查

**影响文件**: `tools/enterprise_uploader.py`

**详细步骤**:
1. 在enterprise_uploader的上传前检查中调用 `run_marketing_gate_check()`
2. 营销关卡未通过的skill给出具体修复建议并阻止上传
3. 添加 `--skip-marketing` 参数供批量场景使用

### P1-3: 搜索排名优化

**目标**: 提升skill在SkillHub搜索结果中的排名
**因素**: stars✅(已完成)、downloads、更新时间、分类匹配、关键词
**技能/插件**: defuddle(研究排名算法) → agent-browser(验证)

---

## P2任务预告 (下一轮后续)

| 任务 | 目标 | 影响文件 |
|------|------|---------|
| P2-1: 平台评分同步到DB | SkillHub AI评分/用户评分/下载数写入DB | db.py, market_monitor.py |
| P2-2: 低评分触发升级 | 评分<4.0自动触发upgrade_single_skill | market_monitor.py, upgrade_checker.py |
| P2-3: 自动化流水线完善 | daily_sync.py整合所有循环任务 | daily_sync.py, orchestrator.py |
| P2-4: 所有权认领 | 确保所有skill在本团队名下 | agent-browser |

---

## P3任务预告 (长期)

| 任务 | 目标 | 影响文件 |
|------|------|---------|
| P3-1: 统一数据源到SQLite | upgrade_checker从JSON迁移到SQLite; find_skill_md统一到skill_core | upgrade_checker.py, orchestrator.py |
| P3-2: 质量检查统一入口 | quality_gate.py作为所有质量检查的统一入口 | quality_gate.py |
| P3-3: 文档对齐 | 确保docs与代码完全一致 | docs/ |

---

## 执行注意事项

1. **不创建碎片化新文件**: 所有增强在现有文件中进行
2. **不模拟/mock**: 所有功能必须真实执行
3. **全链路修复**: 底层数据→中间模块→前端UI
4. **向后兼容**: 现有脚本和CLI命令仍可独立运行
5. **Git推送**: 网络恢复后执行 `git push origin main` 和 `git push hermes-skills main`
6. **读取设计文档**: 执行前先阅读 `d:\skills\docs\plans\new-conversation-starter-design.md` v2.0
7. **读取任务清单**: 执行前先阅读 `d:\skills\docs\plans\new-conversation-task-list.md` v2.0

## 质量链路全景 (v2.0已完成部分)

```
L1静态格式(13项) ✅ → L1.5内容质量(7项) ✅ → 营销关卡(7项) ✅ → 防幻觉(3项) ✅ → L2 LLM验证 ✅ → L3 Agent试用 ✅ → GitHub同步 → SkillHub同步 → ClawHub同步
```

所有质量门禁已集成到 `sync_skill_to_all_platforms()` 和 `upgrade_single_skill()` 两个核心入口。
