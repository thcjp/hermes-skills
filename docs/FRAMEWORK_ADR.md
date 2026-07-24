# 自动化框架架构决策记录 (ADR)

> **创建时间**: 2026-07-20
> **状态**: Accepted
> **评估方法**: staff-engineer-mode (architecture-decisions + production-readiness-review)

---

## 一、决策问题

当前自动化框架（发现/更新/治理）的架构是否存在阻碍长期运维的设计缺陷？如何规范化？

## 二、上下文与驱动力

### 2.1 系统现状
- 数据库: 1909条skill记录，640个唯一source_slug
- 三大触发机制: "更新"(update_mechanism.py), "发现"(auto_discover.py), "治理"(clean_naming.py)
- 预期660条(60 juejin + 600 clawhub)，实际1909条，膨胀~3倍

### 2.2 驱动力 (Forces)

| 驱动力 | 说明 | 影响 |
|--------|------|------|
| 数据模型混淆 | 原始下载记录和差异化产出记录混在同一张skills表 | 治理困难，更新检测重复，统计失真 |
| 来源类型不一致 | clawhub_download/clawhub_differentiated/clawhub三种source值 | update_mechanism.py需用集合判断，易遗漏 |
| 工作流追踪失效 | 1848/1909条记录卡在step1_read_original | 无法追踪skill生产进度 |
| 质量门禁缺失 | check_debranding.py存在但未集成，record_score()从未调用 | 差异化质量无自动化保证 |
| 治理文档缺失 | 缺少GOVERNANCE_TRIGGER.md | "治理"触发无标准化流程 |
| 上传重试缺失 | 11条失败上传无重试机制 | 发布成功率无法保障 |

## 三、架构决策

### ADR-001: 数据模型分离 — 源记录与产出记录解耦

**决策**: 将skills表中的"原始下载"记录(source_type=download)迁移到独立的`sources`表，skills表仅保留"产出"记录(differentiated/original)

**替代方案**:

| 方案 | 优点 | 缺点 | 结论 |
|------|------|------|------|
| A. 独立sources表 | 数据模型清晰，统计准确 | 需迁移数据，改代码 | **采纳** |
| B. skills表加record_type字段 | 改动最小 | 查询需过滤，治理复杂 | 拒绝(治标不治本) |
| C. 保持现状 | 零改动 | 660→1909问题持续恶化 | 拒绝 |

**后果**:
- 正面: 统计精确(640源→1280产出)，更新检测不重复，治理范围明确
- 负面: 需迁移671+298=969条源记录，update_mechanism.py需调整查询

**可逆性**: 中等 — 数据迁移有回滚成本，但schema变更可逆

### ADR-002: 来源类型统一 — 三值收敛为单值

**决策**: 将clawhub_download/clawhub_differentiated/clawhub统一为`clawhub`，通过edition字段区分free/paid

**替代方案**:

| 方案 | 优点 | 缺点 | 结论 |
|------|------|------|------|
| A. 统一为clawhub + edition | 简洁，查询简单 | 需迁移数据 | **采纳** |
| B. 保持三值 | 零改动 | SOURCE_*_TYPES集合易遗漏 | 拒绝 |
| C. 新增source_subtype字段 | 保留信息 | 过度设计 | 拒绝 |

### ADR-003: 工作流状态机 — 10步追踪自动化

**决策**: 启用workflow_states表(已存在但为空)，在update_mechanism.py/auto_discover.py的每个阶段调用update_workflow_state()

**状态机**:
```
step1_read_original → step2_debrand → step3_enhance → step4_chineseize
→ step5_add_deps → step6_generate_dual → step7_validate → step8_upload_free
→ step9_upload_paid → completed
```

### ADR-004: 质量门禁集成 — 上传前强制验证

**决策**: 在update_mechanism.py的upload阶段前插入质量门禁，调用check_debranding.py + record_score()，不达标则阻止上传

### ADR-005: 治理触发文档 — 完成三触发体系

**决策**: 创建GOVERNANCE_TRIGGER.md，定义"治理"触发时的标准化流程

## 四、系统地图

### 4.1 数据流

```
[ClawHub/GitHub/Hermes]
        ↓ (auto_discover.py scan)
[sources表] ← 原始下载记录
        ↓ (AI差异化改造)
[skills表] ← 产出记录 (free + paid 双版本)
        ↓ (update_mechanism.py generate)
[payloads/] ← JSON payload
        ↓ (update_mechanism.py upload)
[SkillHub/ClawHub平台]
```

### 4.2 信任边界

| 边界 | 信任方向 | 控制措施 |
|------|---------|---------|
| 外部来源 → sources表 | 不信任 | SHA256校验 + 去重检查 |
| sources表 → skills表 | 半信任 | 质量门禁 + 去标识检查 |
| skills表 → 平台 | 信任 | 上传前最终验证 |

### 4.3 有界上下文映射

| 上下文 | 职责 | 上游 | 下游 | 关系 |
|--------|------|------|------|------|
| 来源扫描 | 发现新skill | 外部平台 | 去重比对 | 反腐层 |
| 去重比对 | 过滤已存在 | 来源扫描 | 差异化改造 | 一致性 |
| 差异化改造 | 去标识+增强 | 去重比对 | 双版本生成 | 核心域 |
| 双版本生成 | free+paid | 差异化改造 | 平台同步 | 供应商 |
| 平台同步 | 上传发布 | 双版本生成 | SkillHub/ClawHub | 客户/供应商 |
| 命名治理 | 规范清理 | 全部上下文 | - | 共享内核 |
| 版本更新 | 来源变更检测 | 外部平台 | 差异化改造 | 合作伙伴 |

## 五、适应度函数 (Fitness Functions)

| 属性 | 指标 | 阈值 | 测量源 | 频率 | 失败响应 | 检查路径 |
|------|------|------|--------|------|---------|---------|
| 依赖方向 | source→skill单向 | 0反向依赖 | DB查询 | 每次治理 | 阻止操作 | `SELECT * FROM skills WHERE source_slug IN (SELECT slug FROM skills)` |
| 来源唯一性 | 同source_slug最多1条源记录 | ≤1 | DB查询 | 每次导入 | 拒绝导入 | `SELECT source_slug, COUNT(*) FROM sources GROUP BY source_slug HAVING COUNT(*)>1` |
| 命名规范 | slug不含版本号 | 0违规 | DB查询 | 每次治理 | 自动修复 | `SELECT * FROM skills WHERE slug GLOB '*-[0-9]*'` |
| 烙印清除 | 0个禁止关键词 | 0 | check_debranding.py | 每次上传前 | 阻止上传 | `python check_debranding.py --slug <slug>` |
| 工作流完整性 | workflow_states表记录数 | =skills表记录数 | DB查询 | 每日 | 告警 | `SELECT COUNT(*) FROM workflow_states vs SELECT COUNT(*) FROM skills` |
| 上传成功率 | 失败重试≤3次 | ≥95% | platform_uploads | 每次上传 | 自动重试 | `SELECT upload_status, COUNT(*) FROM platform_uploads GROUP BY upload_status` |

## 六、风险登记册

| 风险 | 可能性 | 影响 | 缓解措施 | 负责人 |
|------|--------|------|---------|--------|
| 数据迁移丢失记录 | 中 | 高 | 迁移前完整备份DB | update_mechanism.py |
| 源记录迁移后更新检测断裂 | 中 | 高 | 保留source_slug关联 | auto_discover.py |
| 质量门禁过严阻塞发布 | 低 | 中 | 设置告警而非硬阻断 | check_debranding.py |
| workflow_state迁移不完整 | 中 | 中 | 批量回填+增量更新 | clean_naming.py |
| description格式批量修复引入错误 | 低 | 低 | 先dry-run再执行 | 批量脚本 |

## 七、后续检查

1. `testing-and-quality-gates`: 为质量门禁定义自动化测试用例
2. `configuration-and-automation-safety`: 为批量数据迁移定义安全操作规程

---

## 八、Round 1 质量分析发现汇总

### 8.1 差异化改造质量 (Agent 1)
- 平均分: 8.8/10
- 烙印移除: 10/10 (0残留)
- 质量增强: 9/10 (100%有依赖说明)
- 直接复制: 0%
- 问题: 部分frontmatter缺description字段

### 8.2 SKILL.md结构规范 (Agent 2)
- 整体合规率: 76.4%
- 系统级问题1: description字段格式100%不合规(字符串而非数组)
- 系统级问题2: 80%缺少版本历史表格
- 个别异常: key-guard displayName 371字符(导入错误)

### 8.3 工作流完整性 (Agent 3)
- 整体完整度: 60%
- 缺失: GOVERNANCE_TRIGGER.md
- 断点: 5处(import不写DB, status代替import等)
- 质量门禁: check_debranding.py未集成, record_score()从未调用
- 重试机制: 完全缺失(11条失败)
- 工作流追踪: 1848/1909卡在step1, workflow_states表为空
