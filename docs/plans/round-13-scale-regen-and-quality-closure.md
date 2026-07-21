# Round 13: 规模化再生与三层质量闭环 (Phase 9)

> **前置条件**: Round 12 已完成三层质量保障体系建立（L2-Capability 12项检查 + 源保真度检查器 + 跨skill多样性分析器）
> **核心问题**: 如何在批量再生成491个剩余skill的过程中，保证每个skill的个体能力质量？
> **预估时间**: 180-240 分钟
> **验收标准**: 631/631 skill全量再生成 + L2-Capability 100% A级 + 源保真度≥75分 + 跨skill多样性≥90%

---

## 背景与核心问题

### 用户提出的根本性质疑（Round 11延续）

> "目前机制太多的批量化，虽然本项目的skill本来都是从其他项目中抽取出来的优秀功能的skill，但是本项目全部是批量处理，模板化、流水线，那么不同类型、不同业务的skill是如何保证每一个skill本身的能力、功能、质量的？"

### Round 12 已建立的回答：三层能力质量保障体系

Round 12 通过构建三层质量保障工具，从技术层面回答了这个问题：

| 层次 | 工具 | 检测目标 | 核心指标 |
|------|------|----------|----------|
| 第一层：个体内容质量 | `l2_capability_checker.py` (12项检查) | 检测同质化、截断、占位符、领域深度 | L2-Capability分数≥85(A级) |
| 第二层：源能力保真 | `source_fidelity_checker.py` (4项指标) | 验证生成版本保留源skill的核心能力 | 能力覆盖率=100%, 保真度≥75 |
| 第三层：跨skill多样性 | `cross_skill_diversity.py` (4维Jaccard) | 检测同类别内的skill同质化 | 多样性评分≥90% |

**三层体系的逻辑**：
- 第一层确保每个skill自身的内容质量（不空洞、不模板化）
- 第二层确保生成版本不丢失源skill的真实能力（领域知识保真）
- 第三层确保同类skill之间有足够差异（不互相雷同）

### Round 12 已验证的关键数据

| 指标 | LLM再生成skills | 旧模板skills | 质量差距 |
|------|----------------|-------------|----------|
| L2-Capability平均分 | 96.9 | 74.8 | +22.1 |
| L2 A级比例 | 100% (138/138) | 31.2% (238/764) | +68.8% |
| 跨skill多样性 | 100% (0/2278高风险) | 14.3% (1725/2415高风险) | +85.7% |
| 源能力覆盖率 | 89.9% (62/69=100%) | N/A | N/A |

**结论**: LLM再生成方法已在70个skill上验证成功，质量显著优于旧模板，需推广到全部631个skill。

### 当前完成进度

| 类别 | 已完成 | 总数 | 完成率 |
|------|--------|------|--------|
| Communication | 37 | 38 | 97.4% |
| Creative | 22 | 65 | 33.8% |
| Agents | 10 | 43 | 23.3% |
| Automation | 1 | 58 | 1.7% |
| Development | 0 | 50 | 0% |
| Finance | 0 | 11 | 0% |
| Integrations | 0 | 94 | 0% |
| Knowledge | 0 | 32 | 0% |
| Lifestyle | 0 | 18 | 0% |
| Operations | 0 | 14 | 0% |
| Other | 0 | 90 | 0% |
| Productivity | 0 | 38 | 0% |
| Research | 0 | 57 | 0% |
| Security | 0 | 23 | 0% |
| **合计** | **70** | **631** | **11.1%** |

**剩余491个skill待再生成**，分布在12个类别中。

---

## Round 13 核心策略：规模化再生 + 质量闭环

### 策略一：分类别批量再生成（优先大类别）

按类别从大到小处理，每批20个skill（40个文件），每批完成后立即运行三层质量验证：

| 批次 | 类别 | 数量 | 预估批次 |
|------|------|------|----------|
| Batch 8-12 | Integrations | 94 | 5批 |
| Batch 13-17 | Other | 90 | 5批 |
| Batch 18-20 | Automation | 57 | 3批 |
| Batch 21-23 | Research | 57 | 3批 |
| Batch 24-26 | Development | 50 | 3批 |
| Batch 27-28 | Agents | 33 | 2批 |
| Batch 29-30 | Creative (剩余) | 43 | 2批 |
| Batch 31-32 | Productivity | 38 | 2批 |
| Batch 33 | Communication (剩余) | 1 | 1批 |
| Batch 34 | Knowledge | 32 | 2批 |
| Batch 35 | Security | 23 | 1批 |
| Batch 36 | Lifestyle | 18 | 1批 |
| Batch 37 | Operations | 14 | 1批 |
| Batch 38 | Finance | 11 | 1批 |
| **合计** | | **491** | **~25批** |

### 策略二：三层质量验证流水线

每个批次生成后，依次运行三层验证：

```
生成 → L1格式检查 → L2-Capability(12项) → 源保真度 → 跨skill多样性 → DB更新
```

**验证标准**：
- L1: 10/10 通过（格式规范）
- L2-Capability: ≥85分（A级），<85分则自动修复后重新验证
- 源保真度: 能力覆盖率=100%，保真度≥75分
- 跨skill多样性: 同类别内相似度≤60%

**自动修复策略**：
- L1失败：运行auto_fix()修复格式问题
- L2-Capability <85：识别失分项，针对性增强内容
- 源保真度 <75：检查missing_capabilities，补充缺失能力点
- 多样性高风险：重新生成，增加领域差异化要求

### 策略三：子Agent生成指令增强（v3）

基于Round 12的经验，增强子Agent指令：

```
你是一个skill内容生成专家。请基于源skill的内容，生成高质量的paid和free版本。

## 核心要求（优先级从高到低）
1. **能力保真（最重要）**: 保留源skill的所有核心能力点，不得遗漏
   - 读取源skill的"核心能力"/"核心功能"/"Core"章节
   - 提取每个能力点（###标题、编号列表、bullet列表）
   - 在生成版本中覆盖每个能力点（可用不同表述，但能力必须在）
2. **领域深度**: 包含领域专属的参数、API名、命令名、数值阈值
   - 至少5个领域专属的API/命令引用（反引号包裹）
   - 至少3个领域专属的数值参数（如分辨率、频率限制、字符限制）
   - 至少5个领域专属的错误场景（非通用3行错误表）
3. **内容独特**: 不得使用通用模板填充
   - 错误处理表: 至少5个领域专属场景，非"配置错误/运行时错误/网络错误"
   - FAQ: 至少5个领域专属问题，非"如何开始使用/遇到错误怎么办"
   - 使用流程: 领域专属步骤，非"确认环境→选择方式→执行操作→参考错误处理"
4. **真实示例**: 示例必须包含真实的参数值和输出
5. **章节命名灵活**: 可使用"核心原则"/"核心规则"/"核心工作流"等非标准命名
   - 检查器已支持fallback查找，不必强制统一章节名

## 生成步骤
1. 读取源skill: {source_path}
2. 提取核心能力点列表（必须完整，不得遗漏）
3. 为每个能力点编写具体描述（≥50字符，含参数/用法/输出）
4. 编写领域专属错误处理（≥5个场景）
5. 编写真实使用示例（≥2个完整案例）
6. 编写领域专属FAQ（≥5个问题）
7. 生成paid版（完整能力）和free版（基础能力+升级提示）

## 质量自检（生成后自检）
- [ ] 核心能力点数量 ≥ 源skill的能力点数量
- [ ] 错误处理有5+个领域专属场景
- [ ] 示例包含真实参数值
- [ ] FAQ有5+个领域专属问题
- [ ] 无通用模板填充（检查GENERIC_*常量）
- [ ] frontmatter 8字段齐全
- [ ] displayName ≤ 20字符
- [ ] 无GitHub链接、无开源项目名、无平台烙印词
```

---

## 任务清单

### Step 9.1: 批量再生成 - Integrations类别 (30分钟)

**目标**: 完成94个Integrations类别skill的LLM再生成

**方法**:
1. 从capability_scan_result.json读取Integrations类别的94个skill
2. 分5批，每批20个skill（40个文件）
3. 每批派发10个并行子agent
4. 生成后运行validate_batch.py（L1+L2-Capability+auto_fix）
5. 运行source_fidelity_checker.py --batch
6. 记录验证结果

**验证**: 每批40/40通过L1+L2-Capability，源保真度能力覆盖率=100%

### Step 9.2: 批量再生成 - Other类别 (30分钟)

**目标**: 完成90个Other类别skill的LLM再生成

**方法**: 同Step 9.1，分5批处理

### Step 9.3: 批量再生成 - Automation + Research类别 (30分钟)

**目标**: 完成57+57=114个skill的LLM再生成

**方法**: 同Step 9.1，分6批处理

### Step 9.4: 批量再生成 - Development + Agents类别 (25分钟)

**目标**: 完成50+33=83个skill的LLM再生成

**方法**: 同Step 9.1，分5批处理

### Step 9.5: 批量再生成 - 剩余类别 (25分钟)

**目标**: 完成43+38+1+32+23+18+14+11=180个skill的LLM再生成

**类别**: Creative(剩余)、Productivity、Communication(剩余)、Knowledge、Security、Lifestyle、Operations、Finance

**方法**: 同Step 9.1，分9批处理

### Step 9.6: 全量三层质量验证 (20分钟)

**目标**: 对全部631个再生成skill运行三层质量验证

**方法**:
1. 运行batch_l2_enhanced.py → L2-Capability 12项检查
2. 运行source_fidelity_checker.py --batch → 源保真度检查
3. 运行cross_skill_diversity.py → 跨skill多样性分析
4. 生成综合质量报告

**验证标准**:
- L2-Capability: 100% A级（≥85分）
- 源保真度: ≥75分，能力覆盖率≥95%
- 跨skill多样性: ≥90%

### Step 9.7: DB全量更新与-free版本注册 (15分钟)

**目标**: 将全部1320个skill的评分记录到DB，注册缺失的-free版本

**方法**:
1. 为每个-paid版本的-free版本在skills表中创建记录
2. 更新所有skill的scores表记录（L2-Capability + Source Fidelity）
3. 更新workflow_states表状态
4. 生成完成度报告

### Step 9.8: 质量趋势分析与报告 (10分钟)

**目标**: 分析全量再生成前后的质量变化趋势

**方法**:
1. 对比Round 11（70 skills）→ Round 13（631 skills）的质量趋势
2. 按类别分析质量分布
3. 识别质量薄弱类别，制定优化计划
4. 生成最终质量报告

---

## 三层质量保障工具说明

### 工具1: l2_capability_checker.py (12项检查)

**位置**: `D:\skills\skill-registry\l2_capability_checker.py`

**12项检查**:
| 检查项 | 检测目标 | 满分 |
|--------|----------|------|
| C1: description_completeness | 描述截断检测 | 10 |
| C2: core_capability_specificity | 核心能力具体性 | 10 |
| C3: workflow_concreteness | 流程具体性 | 10 |
| C4: error_handling_specificity | 异常处理具体性 | 10 |
| C5: example_authenticity | 示例真实性 | 10 |
| C6: faq_relevance | FAQ相关性 | 10 |
| C7: domain_keyword_coverage | 领域关键词覆盖 | 10 |
| C8: content_uniqueness | 内容独特性 | 10 |
| C9: chapter_depth | 章节深度 | 10 |
| C10: information_density | 信息密度 | 10 |
| C11: functional_completeness | 功能完整性(能力点数量+描述深度) | 10 |
| C12: domain_depth | 领域深度(数值/API/错误/概念) | 10 |

**总分**: 120分(缩放至100)，A级≥85，B级≥70，C级≥50

**关键设计**:
- `find_chapter()`: 三轮查找（精确→包含→被包含），支持非标准章节名
- C2/C3 fallback: 查找###标题最多或编号步骤最多的章节
- C11: 支持表格格式能力点，三轮fallback查找能力章节
- C12: 弹性评分，5类信号（数值/API/错误/配置/概念）互补，适配创意类skill

### 工具2: source_fidelity_checker.py (4项指标)

**位置**: `D:\skills\skill-registry\source_fidelity_checker.py`

**4项指标**:
| 指标 | 权重 | 检测目标 |
|------|------|----------|
| 能力覆盖率 | 40% | 生成版本覆盖源skill能力点的比例 |
| 领域术语保留 | 25% | 源skill的API/命令/术语保留率 |
| 错误场景质量 | 15% | 生成版本的错误场景数量(≥5满分) |
| 差异化与增强度 | 20% | 保留核心+有新增术语的增强程度 |

**关键设计**:
- 中文关键词2-3字滑窗提取（解决"分层权限模型"被当作一个词的问题）
- 错误场景不检查重合度（源skill的错误通常是通用的，生成版本应该更好）
- 差异化评分改为增强度（覆盖率≥30% + 新增术语≥20% = 满分）

### 工具3: cross_skill_diversity.py (4维Jaccard)

**位置**: `D:\skills\skill-registry\cross_skill_diversity.py`

**4个维度**:
| 维度 | 权重 | 检测目标 |
|------|------|----------|
| 章节结构相似度 | 25% | ## 标题的Jaccard相似系数 |
| 错误处理重合度 | 25% | 错误场景的Jaccard相似系数 |
| FAQ问题重合度 | 20% | FAQ问题的Jaccard相似系数 |
| 领域关键词差异度 | 30% | 领域术语的Jaccard相似系数 |

**阈值**: 综合相似度>60% = 高风险同质化

---

## 验收标准

| 验收项 | 标准 | 验证方法 |
|--------|------|----------|
| 全量再生成 | 631/631 skill完成 | capability_scan_result.json计数 |
| L2-Capability | 100% A级(≥85) | batch_l2_enhanced.py |
| L2平均分 | ≥90 | DB scores表统计 |
| 源保真度 | ≥75分 | source_fidelity_checker.py --batch |
| 源能力覆盖率 | ≥95% | source_fidelity_checker.py |
| 跨skill多样性 | ≥90% | cross_skill_diversity.py |
| DB记录完整 | 1320条scores | DB查询 |
| -free版本注册 | 全量注册 | DB查询 |
| 质量报告 | 生成 | 综合质量报告 |

---

## 完成后生成Round 14提示词

Round 14预期方向：
1. **上传流水线恢复**: 1320个高质量skill批量上传到SkillHub
2. **定价策略执行**: 按Round 11定价分析结果分层定价
3. **L3功能验证**: 从0扩展到100+个skill的功能验证
4. **运营闭环**: 健康检查 + 质量监控 + 用户反馈收集

---

## 注意事项

1. **不得修改660个源skill**: 源skill仅作为生成参考，不得直接修改
2. **必须LLM生成**: 不得使用模板硬编码，每个skill必须由LLM基于源内容生成
3. **小测试迭代**: 每批20个skill生成后立即验证，发现问题立即修复再继续
4. **优先功能质量**: 功能、流程、产出质量优先于格式规范
5. **-paid文件夹清理**: 子agent可能创建多余的-paid文件夹，需自动检测并删除
6. **MCP上下文白名单**: check_debranding.py已更新中文MCP变体白名单
7. **不迎合不敷衍**: 如发现系统性质量问题，宁可重来也不放行
8. **三层验证不可省略**: 每批必须运行L2-Capability + Source Fidelity + Diversity
9. **源保真度B级可接受**: 术语保留率因LLM重述自然降低，B级(65-79)是正常的
10. **章节命名灵活**: 检查器已支持非标准章节名，不必强制统一
