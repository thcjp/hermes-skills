# 质量治理与金融技能生产设计方案

> 日期: 2026-07-27
> 版本: v1.0
> 状态: 已确认
> 关联: next-round-prompt-v70.0.md, task-list-v1.0.md, implementation-plan-v1.0.md

## 一、背景与问题

### 1.1 当前系统断点

项目已有完整的生产管线（8阶段orchestrator）和质量门禁（46项检查），但存在一个核心断点：

- **本地质量检测**是通过/失败式检查，不产生数值评分
- **4.5分阈值**仅适用于SkillHub平台AI评分，是上传后从平台抓取的后置数据
- **评分覆盖率仅0.1%**（2/1768），大量已上传技能的平台评分未同步
- **无本地AI评分机制**，无法在上传前预判平台评分

这导致：低质量技能上传后才发现评分不达标，需要反复上传-评分-升级-重传，浪费平台资源和时间。

### 1.2 本次设计目标

1. **任务1**: 构建本地LLM质量评分器，对全部存量技能执行三层质量检测，≤4.5打回重做，>4.5后上传SkillHub并跟踪平台评分，最终校准本地评分体系
2. **任务2**: 从多源采集20个金融领域技能，差异化生产10免费+20收费，用30个技能跑通完整管线（含平台评分跟踪和打回重做闭环）
3. **任务3**: 对SkillHub平台上所有≤4.5分的技能（免费和收费）用最新管线升级，直至全部>4.5

## 二、三层质量评分架构

### 2.1 架构总览

```
第1层：本地LLM预评分（快速粗筛，前置门控）
  ↓ local_score ≥ 4.5 通过
第2层：现有L2/L3/L4深度检查（精确验证）
  ↓ 全部通过
第3层：平台AI评分（最终闭环，上传后跟踪）
  ↓ platform_rating ≥ 4.5
完成
```

### 2.2 第1层：本地LLM预评分

**模块**: `tools/local_quality_scorer.py`（新增）

**评测5维度**（对齐SkillHub平台AI评测维度）:

| 维度 | 权重 | 评测内容 |
|------|------|---------|
| 功能完整性 | 1.0 | 核心功能描述是否完整、输入输出格式是否清晰、使用场景是否充分 |
| 准确性 | 1.0 | 技术描述是否正确、依赖说明是否准确、无错误/误导信息 |
| 易用性 | 1.0 | 结构是否清晰、示例是否充分、frontmatter是否规范、用户能否快速上手 |
| 安全性 | 1.0 | 无安全风险模式、依赖说明透明、无敏感信息泄露 |
| 创新性 | 1.0 | 差异化亮点是否突出、独特价值是否明确、非简单复制 |

**评分产出**: 每维度0.0-1.0分，总分0.0-5.0分，附文字改进建议

**阈值**: `local_score < 4.5` → 阻断上传，返回改进建议

**实现**: 调用LLM API对SKILL.md全文做结构化评测，评测prompt模板存于 `data/config/quality_scoring_config.json`

### 2.3 第2层：现有深度检查（复用）

| 检查器 | 现有分制 | 换算5分制 | 阈值 |
|--------|---------|----------|------|
| L2 TRACE评分 | 50分 | ÷10 | ≥3.5 (即35/50) |
| L3 功能验证 | 100分 | ÷20 | ≥3.5 (即70/100) |
| L4 任务完成 | 100分 | ÷20 | ≥3.0 (即60/100) |
| 46项合规检查 | 通过/失败 | 不换算 | 全部通过 |

此层为现有能力，不新增代码，仅通过 `run_full_quality_check(include_l2l3=True)` 启用。

### 2.4 第3层：平台AI评分（复用+强化）

复用现有 `market_monitor.py` 的 `sync_platform_ratings()` 和 `check_low_rating_skills()`，强化批量抓取效率。

### 2.5 统一入口集成

`run_full_quality_check()` 扩展:
- 新增参数 `include_local_score=True`（默认True）
- 新增子函数 `run_local_scoring()` 调用 `local_quality_scorer.score_skill()`
- 返回结果新增 `local_score` 字段（0.0-5.0）和 `local_score_feedback` 字段（改进建议）
- `local_score < 4.5` → `overall_passed = False`，阻断上传

## 三、任务1：存量技能质量治理

### 3.1 扫描范围

| 目录 | 数量 | 说明 |
|------|------|------|
| packaged-skills/skillhub/ | ~1003 | 含免费版+付费版对 |
| opensource-skills/packaged/ | ~40 | 开源改造版 |
| enterprise-upload/ | ~3 | 企业付费版 |
| **合计** | ~1046 | |

### 3.2 执行阶段

**阶段1-1: 构建本地评分器**
- 新增 `tools/local_quality_scorer.py`
- 扩展 `tools/quality_gate.py` 的 `run_full_quality_check()`
- 新增 `data/config/quality_scoring_config.json`
- DB skills表新增 `local_quality_score` 字段（REAL, 0-5）
- 用已知好skill（平台评分≥4.5）和坏skill（平台评分<4.5）验证评分器准确性

**阶段1-2: 全量存量扫描**
- 对1046个skill执行 `run_full_quality_check(include_local_score=True)`
- 结果写入DB `local_quality_score` 字段
- 产出全量质量评分报告

**阶段1-3: 低分打回重做**
- 筛选 `local_score ≤ 4.5` 的skill
- 根据5维度评测反馈逐个升级SKILL.md（整体性内容提升，非补丁式修改）
- 升级后重新评分，循环直到 > 4.5

**阶段1-4: 上传SkillHub并跟踪**
- 通过三层检测的skill批量上传SkillHub
- 执行 `sync-ratings` 批量同步平台AI评分

**阶段1-5: 平台低分二次治理**
- 平台AI评分 < 4.5 的skill → `upgrade_single_skill()` → 重传
- 循环直到平台评分 ≥ 4.5

**阶段1-6: 评分体系校准**
- 对比本地评分与平台评分的一致性
- 分析偏差模式，校准评分器权重
- 产出质量检测体系升级建议报告

## 四、任务2：金融技能生产全流程

### 4.1 采集源与目标

| 源 | 预期数量 | 工具 |
|----|---------|------|
| ClawHub Finance分类 | 8-10 | 现有clawhub-skills/downloaded/Finance/ |
| GitHub高星仓库 | 5-8 | github_scanner.py |
| Web搜索补充 | 3-5 | WebSearch + defuddle |
| **合计** | **20** | |

### 4.2 免费/收费分配原则

| 类型 | 判定条件 | 分配 |
|------|---------|------|
| 仅付费版 | 高价值（量化策略/实盘信号/专业数据）或易逆向（简单公式/通用指标） | 10个 |
| 免费版+付费版 | 普及型（基础概念/教育/新闻/入门工具） | 10个（各产免费+付费） |
| **总计** | | 10免费 + 20付费 = 30个 |

### 4.3 定价策略升级

**升级方向**:
- 金融类别基础价高于现有数据分析类（9.9元→19.9元起）
- 价格上限提升至199元（企业级金融量化工具）
- 新增金融高价值关键词到 `task3_pricing_calibration.py` 的 `score_value()`
- `pricing_engine.py` 的 `PRICE_ANCHOR_POINTS` 新增 69.0/99.0/129.0/169.0/199.0 价格点
- 高频交易工具适用月付，低频分析工具适用按次

**升级先于生产**，确保20个付费版直接使用新策略定价。

### 4.4 执行阶段

**阶段2-1: 多源采集20个金融技能** → finance_candidates.json
**阶段2-2: 定价策略升级** → pricing_engine.py + task3_pricing_calibration.py 更新
**阶段2-3: 深度差异化生产30个** → auto_differentiate.py + 免费/收费分配 + 定价
**阶段2-4: 三层质检+打回重做** → run_full_quality_check，循环直到>4.5
**阶段2-5: 全平台上传** → SkillHub + ClawHub + GitHub
**阶段2-6: 平台评分跟踪+二次治理** → sync-ratings + 低分重做闭环
**阶段2-7: 流程验证总结** → 全流程验证报告

## 五、任务3：平台低分技能全量治理

### 5.1 目标

对SkillHub平台上所有AI评分≤4.5的技能（免费和收费），用最新管线（含local_quality_scorer）升级，直至全部>4.5。

### 5.2 执行阶段

**阶段3-1: 全量评分同步**
- 执行 `python tools/market_monitor.py sync-ratings --limit 200`
- 重复执行直到1768个synced skill全部同步
- 目标: DB中 `platform_rating > 0` 的skill ≥ 1768的80%

**阶段3-2: 低分技能识别**
- 查询DB `platform_rating > 0 AND platform_rating < 4.5` 的全部skill
- 分类: 本地有文件 / 本地无文件

**阶段3-3: 批量升级**
- 本地有文件: `upgrade_single_skill(slug)` + `run_full_quality_check(include_local_score=True)`
  - local_score < 4.5 → 根据反馈升级 → 重新评分 → 循环
  - local_score ≥ 4.5 → 允许重传
- 本地无文件: 标记 `needs_rebuild`，从平台下载或重新差异化

**阶段3-4: 重传+跟踪+循环**
- 升级后重传SkillHub
- 等待平台AI评测（24-48小时）
- 重新sync-ratings获取新评分
- 仍 < 4.5 → 再次升级 → 循环直到 ≥ 4.5

## 六、文件组织与集成方案

### 6.1 新增文件（仅2个）

| 文件 | 用途 |
|------|------|
| `tools/local_quality_scorer.py` | 本地LLM质量评分器 |
| `data/config/quality_scoring_config.json` | 评分器配置（LLM端点/维度权重/prompt模板） |

### 6.2 修改现有文件（4个，均为扩展）

| 文件 | 修改 |
|------|------|
| `tools/quality_gate.py` | `run_full_quality_check()` 新增 `include_local_score` 参数和 `local_score` 返回字段 |
| `tools/pricing_engine.py` | 新增金融类别基础价、更高价格点、金融领域系数 |
| `tools/task3_pricing_calibration.py` | 新增金融高价值关键词、L4价格上限提升 |
| `tools/market_monitor.py` | `sync_platform_ratings()` 优化批量抓取并发效率 |

### 6.3 约束

- 不创建新的上传脚本、差异化脚本、编排脚本、数据库
- 复用现有 `orchestrator.py` 8阶段管线、`auto_differentiate.py`、`clawhub_batch_uploader.py`
- DB仅新增 `local_quality_score` 字段，不改表结构
- 所有新能力通过扩展现有主线集成，不创建平行系统

## 七、设计原则

1. **严禁补丁式修复**: 每个低分skill根据5维度反馈做整体性内容提升，不逐条打补丁
2. **严禁碎片化功能**: 仅2个新文件+4个扩展修改，不创建平行系统
3. **严禁冗余化已有模块**: 复用现有46项检查、L2/L3/L4检查器、上传脚本、编排器
4. **三层递进**: 第1层不过不进入第2层，第2层不过不上传，上传后第3层跟踪
5. **闭环校准**: 本地评分与平台评分对比，持续校准本地评分器准确性
6. **单向依赖**: local_quality_scorer → quality_gate → upload_gate → orchestrator，不反向依赖
