---
intent: 全面评估Skill自动化体系的完整性与正确性, 设计分层验证机制与四层架构升级方案
success_criteria: 自动化体系能持续产出"审核必过+内容质量达标+真实可运行"的skill, 小规模试点验证通过后再全面推广
risk_level: medium
auto_approve: false
created_at: 2026-07-20
based_on: P0 workflow完成结果 + WORKFLOW_INTEGRITY_REPORT + 3个skill抽样验证 + 用户选择(分层验证+深度清理)
---

# Skill自动化体系 v2 设计方案

> **前序**: P0 workflow已完成4项基础修复(质量门禁/import写DB/上传重试/门禁集成), P1-1完成skill_core共享层。
> 本文档针对P0遗留问题和新发现的缺失项, 设计v2升级方案。

## 一、现状评估（实事求是）

### 1.1 已完成的能力（P0+P1-1）

| 环节 | 已有能力 | 证据 |
|------|---------|------|
| 发现-扫描 | auto_discover.py scan/dedup | clawhub+github双来源扫描 |
| 发现-导入 | cmd_import()写DB | P0-2修复, 测试skill_id=1918/1919 |
| 包装-格式检查 | quality_gate.py 10项检查 | ai-video-director被挡住 |
| 包装-共享层 | skill_core/ 4模块 | P1-1完成, 规则单一来源 |
| 发布-重试 | upload_free_via_cli()指数退避 | 1s/2s/4s, 不可重试错误分类 |
| 发布-门禁集成 | sync_skill_to_platform()上传前检查 | blocked_by_quality_gate记录 |
| 治理 | GOVERNANCE_TRIGGER.md 7阶段 | 三触发体系补全 |

### 1.2 抽样验证结果（3个skill）

| Skill | 格式合规 | 内容结构 | 可运行性验证 | 外部依赖真实性 |
|-------|---------|---------|-------------|--------------|
| ai-artist-workstation | ✓ 10/10 | ✓ 8章节齐全 | ✗ 未测试 | ⚠ 引用"鹧应AI写真"未验证 |
| seo-doctor | ✓ | ✓ 8章节齐全 | ✗ 未测试 | ⚠ 引用"BERT模型"未验证 |
| sales-copy-writer | ✓ | ✓ 8章节齐全 | ✗ 未测试 | ✓ 纯LLM驱动, 无外部依赖 |

**关键发现**: 格式检查通过 ≠ 可运行。3个skill中2个引用了外部API/模型, 但没有任何机制验证这些依赖是否真实可用。

### 1.3 P0 workflow的不完善之处

P0解决了"审核必拒"的格式问题, 但未解决以下核心问题:

| # | P0未覆盖的问题 | 影响 |
|---|--------------|------|
| 1 | **无"生成"自动化** | 差异化改造完全依赖AI手动, 无法批量产出 |
| 2 | **无"可运行性"验证** | 质量门禁只查格式, 不验证skill能否真正运行 |
| 3 | **TRACE评分未集成** | trace_llm_scorer.py存在但未集成到流水线 |
| 4 | **无端到端测试** | 生成后没有实际调用skill验证输出质量 |
| 5 | **外部依赖未验证** | skill引用的API/包/模型未验证真实性 |
| 6 | **workflow_states 10步表未启用** | workflow_state字段已回填, 但10步详细追踪表仍为空 |
| 7 | **文档冲突未解决** | deep-differentiation-methodology.md与NAMING_CONVENTION.md的-pro后缀矛盾 |
| 8 | **运维监控缺失** | 无健康检查、无告警、无定时任务 |
| 9 | **付费版上传半人工** | 依赖浏览器session cookies, 无法全自动 |

## 二、完整性与正确性评估

### 2.1 四层架构完整度评分

```
发现层  ████████████░░░░  75%  (扫描+去重+导入OK, 差异化仍手动)
生成层  ██████░░░░░░░░░░  40%  (格式检查OK, 内容生成+可运行性验证缺失)
验证层  ████░░░░░░░░░░░░  25%  (仅静态格式检查, 无LLM模拟+真实试运行)
运维层  ████████░░░░░░░░  50%  (重试OK, 监控+告警+定时缺失)
```

### 2.2 "能否持续产出高质量可运行skill"的判断

**结论: 当前体系不能保证持续产出"真正可运行"的skill。**

| 维度 | 能否保证 | 原因 |
|------|---------|------|
| 审核必过(格式) | ✓ 能 | quality_gate.py 10项检查已集成 |
| 内容质量达标 | △ 部分 | 结构完整, 但无TRACE评分把关 |
| 真实可运行 | ✗ 不能 | 无任何运行验证机制 |
| 外部依赖真实 | ✗ 不能 | 引用的API/包未验证 |
| 持续批量产出 | ✗ 不能 | 差异化改造依赖AI手动, 无模板化 |

## 三、设计方案：四层架构 + 分层验证

### 3.1 架构总览

```
┌─────────────────────────────────────────────────────────┐
│                    运维监控层 (Layer 4)                    │
│  健康检查 · 告警 · 定时任务 · 看板                          │
├─────────────────────────────────────────────────────────┤
│                    发布层 (Layer 3)                       │
│  双版本生成 · 质量门禁 · 上传重试 · 状态追踪                │
├─────────────────────────────────────────────────────────┤
│                    验证层 (Layer 2) ← 核心新增             │
│  L1静态检查 · L2 LLM模拟 · L3 真实agent试运行             │
├─────────────────────────────────────────────────────────┤
│                    生成层 (Layer 1) ← 核心补全             │
│  差异化模板 · 生成器 · 外部依赖验证                         │
├─────────────────────────────────────────────────────────┤
│                    发现层 (Layer 0)                       │
│  多源扫描 · 去重 · 导入DB                                  │
└─────────────────────────────────────────────────────────┘
```

### 3.2 验证层设计（核心新增 - 分层验证）

用户选择: **分层验证**

#### L1: 静态检查（已有, 日常生成时执行）
- 现有 quality_gate.py 的10项检查
- 执行时机: 每次生成/修改skill后立即执行
- 通过标准: 10/10 PASS
- 耗时: <1秒/skill

#### L2: LLM模拟验证（新增, 进入上传队列前执行）
- 用LLM模拟"用户输入典型请求 → skill响应 → 评估输出质量"
- 执行时机: skill通过L1后, 进入上传队列前
- 验证内容:
  1. 触发精准度: 给定3个典型用户输入, skill是否被正确触发
  2. 输出完整性: 模拟skill执行, 输出是否包含承诺的核心能力
  3. 依赖可达性: 检查skill引用的API endpoint/包名是否真实存在
  4. TRACE快评: T/R/A/C/E五维度快速评分(每维度0-10, 总分≥35才通过)
- 通过标准: 4项全部PASS, TRACE总分≥35/50
- 耗时: ~30秒/skill(3次LLM调用)
- 实现: 新建 `skill-registry/llm_validator.py`

#### L3: 真实agent试运行（新增, 定稿发布前执行）
- 实际启动agent加载SKILL.md, 用3个典型输入测试真实输出
- 执行时机: skill定稿后, 正式上传到平台前
- 验证内容:
  1. 真实加载: agent能否正确加载SKILL.md并理解指令
  2. 真实执行: 3个典型输入能否产出预期结果
  3. 异常处理: 边界输入(空/超长/非法)是否有合理反馈
  4. 输出可用性: 输出结果是否可直接使用(非占位符/非模板)
- 通过标准: 3/3典型输入PASS + 异常处理PASS
- 耗时: ~2分钟/skill
- 实现: 新建 `skill-registry/agent_trial.py`

#### 分层验证流程图

```
生成/修改skill
    │
    ▼
L1静态检查 (quality_gate.py, <1s)
    │ PASS
    ▼
[日常: 可继续修改]
    │ 准备上传
    ▼
L2 LLM模拟验证 (llm_validator.py, ~30s)
    │ PASS (TRACE≥35)
    ▼
[进入上传队列]
    │ 定稿发布前
    ▼
L3 真实agent试运行 (agent_trial.py, ~2min)
    │ PASS (3/3 + 异常处理)
    ▼
正式上传到平台
```

### 3.3 生成层设计（核心补全）

#### 问题: 差异化改造完全依赖AI手动

#### 方案: 模板化生成器 + 外部依赖验证

**3.3.1 差异化模板系统**
- 基于SKILL_QUALITY_STANDARD.md的8标准章节, 创建生成模板
- 5种设计模式各一套模板(Tool Wrapper/Generator/Reviewer/Inversion/Pipeline)
- 模板包含: 章节骨架 + 写作指引 + 质量检查点
- AI只需填充具体内容, 不需从零设计结构
- 实现: 新建 `skill-registry/templates/` 目录, 5个模板文件

**3.3.2 外部依赖验证器**
- 扫描SKILL.md中引用的外部依赖(API endpoint/npm包/PyPI包/模型名)
- 自动验证:
  - npm包: `npm view <package>` 检查存在性
  - PyPI包: `pip index versions <package>` 检查存在性
  - HTTP API: HEAD请求检查可达性
  - 模型名: 与已知模型列表比对
- 输出: 依赖验证报告, 标记不可达/不存在的依赖
- 实现: 新建 `skill-registry/dependency_verifier.py`

**3.3.3 生成流水线**
```
原始SKILL.md → 读取 → 选择模板 → AI填充内容 → L1静态检查 → 外部依赖验证
                                                              │
                                                    PASS ←─────┴─────→ FAIL
                                                      │                    │
                                                 进入L2验证          返回修改
```

### 3.4 运维层设计（补全缺失）

**3.4.1 健康检查脚本**
- 检查DB完整性: workflow_state覆盖率、孤儿记录数、重复记录数
- 检查文件完整性: local_path有效性、SKILL.md存在性
- 检查平台状态: 上传成功率、pending审核数
- 实现: 新建 `skill-registry/health_check.py`

**3.4.2 定时任务**
- 每日: 来源更新检测(update_mechanism.py check)
- 每周: 全面治理扫描(clean_naming.py dry-run)
- 每周: 健康检查(health_check.py)
- 实现: 使用Schedule工具创建cron任务

## 四、实施路线（小规模试点→定稿→全面升级）

### 4.1 核心原则

1. **每次只改1个环节, 用1-2个skill验证**
2. **验证通过后再进入下一环节**
3. **所有环节都通过小规模验证后, 才全面推广**
4. **不破坏P0/P1-1已完成的成果**

### 4.2 实施阶段

#### Phase 1: 验证层补全（最高优先级）

| 步骤 | 任务 | 验证skill | 验证标准 | 状态 |
|------|------|----------|---------|------|
| 1.1 | 编写llm_validator.py | sales-copy-writer(纯LLM) | TRACE评分≥35, 4项PASS | 待实施 |
| 1.2 | L2验证试跑-纯LLM skill | sales-copy-writer | 通过L2验证 | 待实施 |
| 1.3 | L2验证试跑-有外部依赖 | ai-artist-workstation | 识别"鹧应AI写真"未验证 | 待实施 |
| 1.4 | 编写dependency_verifier.py | ai-artist-workstation | 正确识别外部依赖 | 待实施 |
| 1.5 | 编写agent_trial.py | sales-copy-writer | 3/3输入PASS | 待实施 |
| 1.6 | L3验证试跑 | sales-copy-writer | 真实agent能执行 | 待实施 |
| 1.7 | 三层验证集成到流水线 | sales-copy-writer | L1→L2→L3全链路通 | 待实施 |

#### Phase 2: 生成层补全

| 步骤 | 任务 | 验证skill | 验证标准 | 状态 |
|------|------|----------|---------|------|
| 2.1 | 创建5种设计模式模板 | - | 模板覆盖8标准章节 | 待实施 |
| 2.2 | 用模板生成1个新skill | 选1个候选 | L1+L2通过 | 待实施 |
| 2.3 | 外部依赖验证器集成 | 上一步skill | 依赖全部验证 | 待实施 |
| 2.4 | 生成流水线端到端验证 | 上一步skill | 发现→生成→验证全通 | 待实施 |

#### Phase 3: 运维层补全

| 步骤 | 任务 | 验证标准 | 状态 |
|------|------|---------|------|
| 3.1 | 编写health_check.py | 输出DB+文件+平台健康报告 | 待实施 |
| 3.2 | 创建定时任务 | cron任务正确触发 | 待实施 |
| 3.3 | 解决文档冲突 | deep-differentiation-methodology.md移入skill-registry/并修正-pro矛盾 | 待实施 |

#### Phase 4: 定稿与全面升级

| 步骤 | 任务 | 前提 | 状态 |
|------|------|------|------|
| 4.1 | 3个skill全链路定稿验证 | Phase 1-3全部通过 | 待实施 |
| 4.2 | 定稿后批量推广 | 3个skill验证无问题 | 待实施 |
| 4.3 | 启用workflow_states 10步表 | 推广时同步启用 | 待实施 |

### 4.3 每个步骤的验证要求

- **代码验证**: 新代码必须有--help输出或dry-run模式
- **试跑验证**: 用1个真实skill运行, 记录实际输出
- **对比验证**: 修改前后行为对比, 确保无回退
- **证据保存**: 每次验证结果保存为JSON报告

## 五、文件清理计划（深度清理）

### 5.1 清理分类

#### A. 明确删除（临时文件, 零价值）

| 文件模式 | 数量 | 说明 |
|---------|------|------|
| `.api-probe*.sh/.txt` | 12 | API探测临时脚本和输出 |
| `.inspect*.sh` | 2 | 检查脚本 |
| `.dryrun*.txt` | 1 | 干跑结果 |
| `.cli-src.py`, `.cli-info.txt` | 2 | CLI信息和源码 |
| `.auth-help.txt`, `.config-help.txt`, `.login-help.txt`, `.pub-help.txt` | 4 | 帮助文本 |
| `.publish-free.sh/.txt` | 2 | 发布临时文件 |
| `retry-results.txt`, `upload-results.txt` | 2 | 结果临时文件 |
| `.inspect2.sh` | 1 | 检查脚本 |

**小计: 26个文件**

#### B. 归档后删除（过期报告, 有历史价值）

| 文件 | 说明 | 归档到 |
|------|------|--------|
| `round2_displayname_anomalies.csv` | 第2轮分析 | archive/round2/ |
| `round2_duplicate_analysis_report.md` | 第2轮分析 | archive/round2/ |
| `round2_duplicate_groups.csv` | 第2轮分析 | archive/round2/ |
| `round3_cross_validation_report.md` | 第3轮分析 | archive/round3/ |
| `round4_verify_cleanup_report.md` | 第4轮分析 | archive/round4/ |
| `round5_final_validation_report.md` | 第5轮分析 | archive/round5/ |
| `LLM类Skill案例展示审核报告.md` | 早期审核 | archive/ |
| `SKILL-规范性分析报告.md` | 早期分析 | archive/ |
| `SKILLHUB_质量差距分析报告.md` | 早期分析 | archive/ |
| `TRACE评估与增强报告.md` | 早期分析 | archive/ |
| `skill_case_test_report.md` | 早期测试 | archive/ |
| `skill_test_report.md` | 早期测试 | archive/ |
| `差异化改造质量分析报告.md` | 早期分析 | archive/ |
| `WORKFLOW_STATE_MACHINE_FIX.md` | 已完成修复 | archive/ |

**小计: 14个文件归档**

#### C. 评估后删除（冗余脚本/备份）

| 文件 | 说明 | 处理 |
|------|------|------|
| `skill-registry.db.backup_20260720_092727` | DB备份 | 保留(最新备份) |
| `skill_batch_upgrader_v2.py` | 旧版批量升级器 | 删除(v3已取代) |
| `batch12_mapping.txt` | 批处理映射 | 评估后删除 |
| `batch12_mapping_full.txt` | 批处理映射 | 评估后删除 |
| `batch12_pending_list.txt` | 批处理待处理 | 评估后删除 |
| `skill-registry/__pycache__/` | Python缓存 | 删除(自动重建) |
| `skill-registry/skill_core/__pycache__/` | Python缓存 | 删除(自动重建) |
| `skillhub-*-analysis.html` (4个) | HTML分析报告 | 归档到archive/ |

#### D. 保留（核心文件, 不动）

- skill-registry/ 下所有.py脚本(除v2废弃的)
- skill-registry/ 下所有.md文档(触发器/规范/ADR)
- packaged-skills/ 全部
- clawhub-skills/, differentiated-skills/, opensource-skills/ 目录
- skill-registry.db (主数据库)
- .gitignore, README.md, UPLOAD-GUIDE.md

### 5.2 清理执行顺序

1. 创建 `d:\skills\archive\` 目录
2. 归档B类文件到archive/
3. 删除A类临时文件
4. 评估C类文件, 确认后删除
5. 清理__pycache__
6. 验证清理后项目仍能正常运行(quality_gate.py --help)

### 5.3 清理验证

- 清理后运行: `python quality_gate.py --help` 确认脚本正常
- 清理后运行: `python auto_discover.py scan --source clawhub --limit 1` 确认发现正常
- 清理后检查: DB查询确认数据完整

## 六、风险与缓解

| 风险 | 可能性 | 影响 | 缓解措施 |
|------|--------|------|---------|
| L2验证LLM成本高 | 中 | 中 | 仅在上传队列前执行, 非每次修改 |
| L3试运行耗时 | 高 | 中 | 仅定稿前执行, 非日常 |
| 外部依赖验证误报 | 中 | 低 | 标记为warning而非fail, 人工确认 |
| 清理误删文件 | 低 | 高 | 归档而非直接删除, 保留7天观察期 |
| 模板化导致同质化 | 中 | 中 | 5种模式+AI填充内容, 非机械套用 |

## 七、验收标准

### 7.1 Phase 1验收（验证层）
- [ ] llm_validator.py对sales-copy-writer输出TRACE评分
- [ ] dependency_verifier.py正确识别ai-artist-workstation的外部依赖
- [ ] agent_trial.py对sales-copy-writer执行3个试运行输入
- [ ] 三层验证集成到sync_skill_to_platform()

### 7.2 Phase 2验收（生成层）
- [ ] 5种设计模式模板创建完成
- [ ] 用模板生成的skill通过L1+L2验证
- [ ] 生成流水线端到端跑通

### 7.3 Phase 3验收（运维层）
- [ ] health_check.py输出健康报告
- [ ] 定时任务创建并触发
- [ ] 文档冲突解决

### 7.4 Phase 4验收（全面升级）
- [ ] 3个skill全链路定稿验证通过
- [ ] 定稿后才能批量推广
- [ ] workflow_states 10步表启用

### 7.5 文件清理验收
- [ ] 26个临时文件删除
- [ ] 14个报告归档
- [ ] __pycache__清理
- [ ] 清理后项目功能正常

## 八、与P0 workflow的关系

| P0任务 | v2方案关系 |
|--------|-----------|
| P0-1 质量门禁 | v2的L1静态检查, 保留不变 |
| P0-2 import写DB | v2发现层的基础, 保留不变 |
| P0-3 上传重试 | v2发布层的基础, 保留不变 |
| P0-4 门禁集成 | v2验证层的起点, 扩展为三层 |
| P1-1 skill_core | v2共享层, 扩展支持新模块 |

**v2是P0的增量升级, 不推翻P0成果。**
