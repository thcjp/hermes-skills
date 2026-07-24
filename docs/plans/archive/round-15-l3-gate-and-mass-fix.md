# Round 15: L3功能验证关卡 + P1批量修复 + 质量闭环

## 背景与上轮结果

### Round 14 完成情况（代码层面验证，非文档）

#### 14.1 P0剩余42个skill（SF<40）— ✅ 全部完成
- 修复 `source_fidelity_checker.py` 的5处提取逻辑缺陷：
  1. h3_points正则 `r'^###\s+\d*\s*(.+)$'` → `r'^###\s+(.+)$'` + 编号剥离（修复`### 1. Title`被提取为`. Title`然后被过滤的问题）
  2. 扩展capability_keywords 17个新关键词（Engagement, Loop, Artboard, Creative Tips等）
  3. 多章节提取：从所有非垃圾匹配章节提取，而非只取第一个
  4. markdown链接误过滤修复：`[text](url)`不再被占位符过滤器过滤
  5. 终极fallback：过滤后0个能力点时，从所有非排除非垃圾章节重新提取
- 42/42 P0 skill全部修复完成，平均SF从32提升到83

#### 14.2-14.4 P1批量再生成 — 🔄 部分完成
- P1全量重检（318个SF 40-69的skill）：
  - 33个skill因SF检查器改进自动达标（SF≥70）
  - 12个最差skill（SF<35）已全部修复（SF平均32→83）
  - 剩余273个skill（SF 40-69）待批量再生成
- 部分skill分数下降原因：SF检查器改进后提取到更多源能力点，覆盖率更准确（之前被高估）

#### 14.7 L3功能验证机制 — ✅ 已建立并执行批量修复
- 创建 `l3_function_checker.py`，7个维度检查
- 创建 `l3_batch_fix.py`，批量修复3类系统性问题
- 批量修复结果（1017个skill）：
  - 700个清除了模板套话
  - 759个补全了错误处理章节
  - 271个补全了依赖说明
  - 共907个skill被修改
- L3通过率变化：0% → 1%（13/1017 PASS）
- **剩余主要瓶颈**：L3-2能力可执行性（核心能力0个###标题或描述过短）和L3-7内容实质性（核心能力<300字符、缺乏技术细节）—— 这两类问题无法批量修复，需要逐个skill读取源内容重写核心能力

---

## Round 15 目标

**核心原则：第一要务是skill高质量完成任务。不能通过的skill必须打回重做。**

### 质量门禁体系（四层 + 打回机制）

```
生成/修改/包装 → L1格式检查 → L2 SF保真度检查 → L3功能验证 → L4任务完成能力验证 → 上传平台
                                    ↑                    ↑                    ↓
                                    ←←← 不通过，打回 ←←←←←←←←←←←←←←←←←←←←←←←←←
```

- **L1格式检查**（`l1_format_checker.py`）：检查frontmatter、章节结构、slug一致性
- **L2 SF保真度检查**（`source_fidelity_checker.py`）：检查源能力覆盖率、术语保留率、错误场景质量
- **L3功能验证**（`l3_function_checker.py`）：检查skill文档质量（7维度：结构/可执行性/场景/指令/错误处理/依赖/实质性）
- **L4任务完成能力验证**（`l4_task_gate.py`）：检查skill能否实际完成任务（6维度：任务映射/命令执行/错误恢复/依赖闭环/输出标准/用户体验）
- **上传平台**：仅L1+L2+L3+L4全部PASS的skill才能上传

### 打回机制（`skill_status_manager.py`）

```
状态流转:
  pending → l1_passed → l2_passed → l3_passed → l4_passed → ready_for_upload
                                        ↓              ↓
                                   rejected_l3    rejected_l4
                                        ↓              ↓
                                   打回L3修复     打回生成/修改/包装
                                        ↓              ↓
                                   重做后重新验证  重做后重新验证

打回规则:
  - L4不通过 → 状态改为 rejected_l4 → 打回生成/修改/包装步骤
  - L3不通过 → 状态改为 rejected_l3 → 打回修改/增强步骤
  - 打回次数超过3次 → 状态改为 needs_manual → 需人工介入
  - 第一要务: skill高质量完成任务,不允许为通过验证而降低标准
```

### L3 vs L4 的区别

| 维度 | L3功能验证 | L4任务完成能力验证 |
|------|-----------|-------------------|
| 检查对象 | 文档质量 | 功能可用性 |
| 核心问题 | 文档写得好不好？ | skill能否实际完成任务？ |
| L3-1/L4-1 | 结构完整性（章节齐全） | 任务可映射性（能力→任务） |
| L3-2/L4-2 | 能力可执行性（描述够详细） | 命令可执行性（命令有获取说明） |
| L3-3/L4-3 | 场景覆盖率 | 错误恢复可操作性（非空话） |
| L3-4/L4-4 | 指令清晰度 | 依赖闭环性（用户能配置环境） |
| L3-5/L4-5 | 错误处理完整性 | 输出标准明确性 |
| L3-6/L4-6 | 依赖准确性 | 用户体验完整性 |
| L3-7 | 内容实质性 | - |

---

## 执行步骤

### Step 15.1: L3批量修复——模板套话清除（~520个skill）

**问题**：65%的skill包含模板套话，L3-7检查失败

**执行方式**：
1. 批量扫描所有skill，识别包含以下模板套话的skill：
   - "本Skill基于Markdown指令"
   - "通过自然语言指令驱动Agent执行任务"
   - "纯Markdown指令,部分功能需要exec命令行执行能力"
   - "需要LLM支持，无LLM环境无法使用"
   - "复杂场景可能需要人工辅助判断"
   - "性能取决于底层模型能力"
   - "请先阅读使用流程章节"
   - "请参考错误处理章节"
   - "请参考已知限制章节了解具体限制"
2. 删除这些套话，替换为skill具体的技术描述
3. 同时清除所有"触发关键词"字样（38%的skill）

**验证**：`python l3_function_checker.py --batch` 确认L3-7通过率提升

### Step 15.2: L3批量修复——错误处理章节补全（~584个skill）

**问题**：73%的skill缺少 `## 错误处理` 章节

**执行方式**：
1. 对每个缺少 `## 错误处理` 的skill，根据其核心能力生成对应的错误处理表格
2. 每个错误处理表格至少3行，包含：错误场景、原因、处理方式
3. 错误场景应与skill的具体能力相关，不是通用错误

**验证**：`python l3_function_checker.py --batch` 确认L3-5通过率提升

### Step 15.3: L3批量修复——依赖说明补全（~480个skill）

**问题**：58%的skill依赖说明不完整

**执行方式**：
1. 确保每个skill的 `## 依赖说明` 包含：
   - LLM/AI依赖声明
   - 运行环境（操作系统/Agent平台）
   - API Key配置说明（或明确声明无需）
   - 可用性分类（MD/MD+EXEC）
2. 检查tools字段与可用性分类是否一致

**验证**：`python l3_function_checker.py --batch` 确认L3-6通过率提升

### Step 15.4: L3批量修复——核心能力技术细节补全（~416个skill）

**问题**：52%的skill核心能力章节缺乏技术细节

**执行方式**：
1. 对每个L3-2或L3-7失败的skill：
   - 确保 `## 核心能力` 有≥3个###标题
   - 每个###标题下有≥50字符描述
   - 每个能力点有≥2个操作指令指示符（代码引用/表格/代码块/编号列表/bullet/动作动词）
2. 可能需要读取源skill内容，提取真实技术细节

**验证**：`python l3_function_checker.py --batch` 确认L3-2通过率提升

### Step 15.5: P1剩余273个skill批量再生成

**目标**：将273个SF 40-69的skill提升到SF≥70

**执行方式**：
1. 使用5个并行子代理，每个处理~55个skill
2. 每个子代理任务：
   - 读取源skill，提取真实能力点
   - 读取当前生成版本，识别覆盖率不足的能力
   - 重写生成版本，确保所有源能力点被覆盖
   - 确保L1+L2+L3全部通过
3. 子代理v4指令模板（见Round 14）

**验证**：`python source_fidelity_checker.py --batch --limit 800` 全量SF检查

### Step 15.6: 源能力点空skill改进（197个）

**问题**：197个skill的源skill提取出0个能力点（source_caps_empty=True）

**分类处理**：
1. **源skill有内容但提取失败**（~80个）：改进extract_capability_points提取逻辑
2. **源skill本身就是模板/空壳**（~60个）：使用alternative quality standard
   - 检查生成版本是否有≥5个实质性bullet point（每个>20字符）
   - 检查是否有足够的代码示例和技术术语
3. **源skill内容为非标准格式**（~57个）：手动分析源内容，定制提取规则

### Step 15.7: 无源skill替代质量标准（244个）

**问题**：244个skill没有找到源skill文件

**替代质量标准**：
1. L3功能验证必须PASS（7维度全部通过）
2. 核心能力≥5个###标题，每个≥80字符描述
3. 错误处理≥5个场景
4. 必须包含代码示例或使用示例
5. SF检查跳过（无源可对比），但L3必须通过

### Step 15.8: 全量L3功能验证

**执行**：`python l3_function_checker.py --batch` 检查全部1017个skill

**目标**：L3通过率≥80%（814/1017）

**不通过处理**：
- 使用 `python skill_status_manager.py reject <slug> --stage l3 --reason "..."` 标记不通过
- 打回Step 15.1-15.4对应的修复步骤
- 直到L3通过为止

### Step 15.9: L4任务完成能力验证（上传前最终关卡）

**这是上传平台前的最后一道关卡。L3检查文档质量，L4检查skill能否实际完成任务。**

**执行**：
1. `python skill_status_manager.py init` 初始化状态
2. `python l4_task_gate.py --batch --output l4_results.json` 全量L4验证
3. 对不通过的skill执行打回：`python skill_status_manager.py reject <slug> --stage l4 --reason "..."`

**L4验证6个维度**：
- L4-1 任务可映射性：每个核心能力###标题对应一个明确用户任务，有输入→处理→输出描述
- L4-2 命令可执行性：引用的命令/脚本有完整获取和使用说明，参数有解释
- L4-3 错误恢复可操作性：错误处理有具体可执行恢复步骤，不是"重试"空话
- L4-4 依赖闭环性：用户按说明能完整配置环境（LLM能力要求/API Key获取步骤/运行环境）
- L4-5 输出标准明确性：每个能力有明确成功输出描述，Agent能判断任务是否完成
- L4-6 用户体验完整性：使用流程线性、有FAQ、free版有升级提示、有已知限制

**前50个skill L4验证结果**（已完成）：
- 通过: 0%（0/50）
- 警告: 6%（3/50）
- 不通过: 94%（47/50）
- 主要瓶颈:
  - L4-1 任务可映射性: 96%失败（核心能力缺少输入/输出/处理描述）
  - L4-3 错误恢复可操作性: 90%失败（错误处理只有空话如"重试"）
  - L4-5 输出标准明确性: 40%失败（缺少输出描述）
  - L4-2 命令可执行性: 30%失败（命令参数未解释）
  - L4-4 依赖闭环性: 28%失败（API Key缺少配置方式）
  - L4-6 用户体验完整性: 18%失败（缺少FAQ或使用流程非线性）

**目标**：L4通过率≥70%（712/1017）

**不通过处理**：
1. 使用 `python skill_status_manager.py reject <slug> --stage l4 --reason "..."` 标记状态为 rejected_l4
2. 打回生成/修改/包装步骤（Step 15.5或对应的生成步骤）
3. 重新生成/修改/包装后重新验证L4
4. 打回次数超过3次 → 状态改为 needs_manual，需人工介入
5. **第一要务：skill高质量完成任务。不允许为通过验证而降低标准。**

**批量修复策略**（针对L4主要瓶颈）：
- L4-1批量修复：为每个核心能力###标题补充"输入→处理→输出"描述
- L4-3批量修复：将错误处理中的空话替换为具体可执行操作
- L4-5批量修复：为每个核心能力补充成功输出描述
- L4-2批量修复：为代码块中的命令参数添加解释
- L4-4批量修复：为API Key依赖补充配置方式说明

### Step 15.10: 全量SF V4检查

**执行**：`python source_fidelity_checker.py --batch --limit 800`

**目标**：
- SF≥50: ≥90%（720/800）
- SF≥70: ≥60%（480/800）
- 平均SF: ≥65

### Step 15.11: 生成Round 16提示词

---

## 关键约束

1. **禁止mock/simulate/fallback/pass/todo**：所有修复必须实质性
2. **第一要务是skill高质量完成任务**：L4任务完成能力验证是最终硬关卡
3. **四层门禁不可跳过**：L1→L2→L3→L4，任何一层不通过都不能上传
4. **打回机制**：L4不通过的skill，标记 rejected_l4，打回生成/修改/包装步骤
5. **打回次数限制**：超过3次打回 → needs_manual，需人工介入
6. **不引用开源仓库**：SKILL.md中不包含github.com等链接
7. **slug==name==文件夹名**：三者必须一致
8. **frontmatter完整**：slug, name, version, displayName(≤20字符), summary(≤100字符), license, description, tools
9. **三个必需章节**：## 依赖说明、## 核心能力(≥3个###)、## 错误处理
10. **无模板残留**：不包含"触发关键词"、模板套话、占位符
11. **L4核心要求**：每个核心能力必须有输入→处理→输出描述，错误处理必须有具体可执行操作

## 文件路径

- SF检查器：`D:\skills\skill-registry\source_fidelity_checker.py`
- L1检查器：`D:\skills\skill-registry\l1_format_checker.py`
- L3检查器：`D:\skills\skill-registry\l3_function_checker.py`
- L4检查器：`D:\skills\skill-registry\l4_task_gate.py`
- 状态管理器：`D:\skills\skill-registry\skill_status_manager.py`
- 状态文件：`D:\skills\skill-registry\skill_status.json`
- L3批量修复器：`D:\skills\skill-registry\l3_batch_fix.py`
- 生成skill目录：`D:\skills\packaged-skills\skillhub\`
- 源skill目录：`D:\skills\clawhub-skills\downloaded\`
- 差异化skill目录：`D:\skills\differentiated-skills\`
- SF V3结果：`D:\skills\skill-registry\sf_batch_results_v3.json`
- P1重检结果：`c:\Users\thcd\.trae-cn\work\6a5e1d47ef5f370fd441a912\p1_recheck_results.json`
- P1再生成列表：`c:\Users\thcd\.trae-cn\work\6a5e1d47ef5f370fd441a912\p1_regen_list.json`

## 执行优先级

1. **P0（最高）**：Step 15.1-15.4 L3批量修复（解决L3通过率0%的系统性问题）
2. **P1（高）**：Step 15.5 P1剩余273个skill再生成
3. **P2（中）**：Step 15.6-15.7 特殊skill处理（197+244个）
4. **P3（高）**：Step 15.8-15.9 L3+L4全量验证（上传前最终关卡）
5. **P4（低）**：Step 15.10 全量SF V4检查
6. **P5（最后）**：Step 15.11 生成下一轮提示词

## 预期结果

| 指标 | 当前值 | 目标值 |
|------|--------|--------|
| L3通过率 | 1%（13/1017） | ≥80%（814/1017） |
| L4通过率 | 0%（0/50样本） | ≥70%（712/1017） |
| SF≥50 | ~60% | ≥90% |
| SF≥70 | ~15% | ≥60% |
| 平均SF | ~50 | ≥65 |
| 可上传skill数 | 0 | ≥712 |
| 需人工介入 | 0 | <50 |
