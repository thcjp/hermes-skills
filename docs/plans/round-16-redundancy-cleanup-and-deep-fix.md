# Round 16: 冗余清理 + 质量门禁整合 + 深度修复

## 背景与上两轮实际完成情况（代码层面验证，非文档）

### Round 14 实际完成情况

| 任务 | 计划 | 实际完成 | 验证方式 |
|------|------|---------|---------|
| SF检查器提取逻辑修复 | 5处 | ✅ 5处已完成 | source_fidelity_checker.py代码审查 |
| P0 skill修复 (SF<40) | 42个 | ✅ 42/42完成 | check_p0_current.py运行结果 |
| P1最差skill修复 (SF<35) | 12个 | ✅ 12/12完成 | recheck_p1.py运行结果 |
| P1剩余skill再生成 | 273个 | ❌ 未完成 | p1_recheck_results.json: 285个still_need_regen |
| L3功能验证机制 | 创建+批量修复 | ✅ 创建l3_function_checker.py + l3_batch_fix.py | 907/1017个skill已修改 |
| L4任务完成能力验证 | 创建关卡 | ✅ 创建l4_task_gate.py + l4_batch_fix.py | 959/1017个skill已修改 |
| SF V4全量检查 | 全量 | ❌ 未执行 | 无sf_batch_results_v4.json |

### Round 15 实际完成情况

| 任务 | 计划 | 实际完成 | 验证方式 |
|------|------|---------|---------|
| L3批量修复-模板套话 | ~520个 | ✅ 700个已清除 | l3_batch_fix.py执行结果 |
| L3批量修复-错误处理 | ~584个 | ✅ 759个已补全 | l3_batch_fix.py执行结果 |
| L3批量修复-依赖说明 | ~480个 | ✅ 271个已补全 | l3_batch_fix.py执行结果 |
| L3通过率 | ≥80% | ❌ 3% (3/100) | l3_function_checker.py --batch --limit 100 |
| L4批量修复 | 全量 | ✅ 959/1017已修改 | l4_batch_fix.py --batch执行结果 |
| L4通过率 | ≥70% | ❌ 0% (0/200) | l4_task_gate.py --batch --limit 200 |
| 冗余清理 | 未计划 | ✅ 本轮完成 | 见下方冗余清理记录 |

### 本轮冗余清理记录

**发现的问题**：上一轮创建了`l1_format_checker.py`和`skill_status_manager.py`，但项目中已有`quality_gate.py`（10项L1检查）和`skill_core/parser.py`（统一frontmatter解析）+ DB状态管理。

**已执行的清理**：
1. 删除 `l1_format_checker.py`（与`quality_gate.py` 100%冗余）
2. 删除 `skill_status_manager.py` + `skill_status.json`（与DB+`analyze_status.py`冗余）
3. 重构 `l4_task_gate.py` → 使用`skill_core/parser.py`
4. 重构 `l4_batch_fix.py` → 使用`skill_core/parser.py`
5. 重构 `l3_function_checker.py` → 使用`skill_core/parser.py`
6. 重构 `l3_batch_fix.py` → 使用`skill_core/parser.py`
7. 修复L4批量修复bug（###标题被拼接到同一行，182个skill受影响）

**待重构项**：
- `upload_gate.py` 重新实现了frontmatter/章节检查，应改为调用`quality_gate.py`和`l4_task_gate.py`
- `auto_discover.py`、`enterprise_uploader.py`、`github_scanner.py`、`init_baseline.py` 仍有自己的`parse_frontmatter`

---

## 当前质量门禁架构（清理后）

```
quality_gate.py (L1: 10项格式检查)
    ↓
source_fidelity_checker.py (L2-SF: 源保真度) + l2_capability_checker.py (L2-Cap: 能力质量)
    ↓
l3_function_checker.py (L3: 7维度功能验证) + l3_batch_fix.py (L3批量修复)
    ↓
l4_task_gate.py (L4: 6维度任务完成能力验证) + l4_batch_fix.py (L4批量修复)
    ↓
upload_gate.py (上传门控: 合规+定价+安全) → 应编排L1-L4
    ↓
上传平台
```

**统一解析层**：`skill_core/parser.py`（所有检查器共用，消除9处重复实现中的5处）

---

## 当前L4各维度失败率（200个样本，批量修复后）

| 维度 | 修复前失败率 | 修复后失败率 | 改善 | 主要原因 |
|------|------------|------------|------|---------|
| L4-1 任务可映射性 | 96% | 84% | 12% | 核心能力<3个###标题 |
| L4-2 命令可执行性 | 30% | 19% | 11% | 命令参数未解释 |
| L4-3 错误恢复可操作性 | 90% | 87% | 3% | 仍有"重试"等空话 |
| L4-4 依赖闭环性 | 28% | 4% | 24% | 已大幅改善 |
| L4-5 输出标准明确性 | 40% | 30% | 10% | 部分已补充 |
| L4-6 用户体验完整性 | 18% | 14% | 4% | 使用流程非线性 |

---

## Round 16 目标

**核心原则：第一要务是skill高质量完成任务。不通过的skill必须打回重做。**

### Step 16.1: upload_gate.py重构——编排L1-L4检查

**问题**：`upload_gate.py`重新实现了frontmatter/章节检查，与`quality_gate.py`冗余

**执行**：
1. `upload_gate.py`导入并调用`quality_gate.py`（L1）、`source_fidelity_checker.py`（L2-SF）、`l3_function_checker.py`（L3）、`l4_task_gate.py`（L4）
2. 删除`upload_gate.py`中重复的frontmatter/章节检查代码
3. 保留`upload_gate.py`独有的合规检查、定价检查、安全检查
4. 上传门控流程：L1→L2→L3→L4→合规→定价→安全→上传

**验证**：`python upload_gate.py check-all` 确认编排正确

### Step 16.2: L4-1深度修复——核心能力结构补全（~850个skill）

**问题**：84%的skill核心能力<3个###标题，L4-1任务可映射性失败

**执行**：
1. 扫描所有L4-1失败的skill
2. 对每个skill：
   - 读取源skill提取真实能力点
   - 确保核心能力有≥3个###标题
   - 每个###标题下有输入→处理→输出描述
3. 使用5个并行子代理，每个处理~170个skill

**验证**：`python l4_task_gate.py --batch --limit 200` 确认L4-1失败率<30%

### Step 16.3: L4-3深度修复——错误处理可操作性（~870个skill）

**问题**：87%的skill错误处理仍有空话（"重试"、"检查网络"等）

**执行**：
1. 扩展`VAGUE_TO_ACTION`字典，覆盖更多空话模式
2. 对每个错误处理条目：
   - 识别空话短语
   - 替换为具体可执行操作（包含动作动词）
   - 确保每个错误场景有对应的恢复步骤
3. 批量执行修复

**验证**：`python l4_task_gate.py --batch --limit 200` 确认L4-3失败率<20%

### Step 16.4: L3-2/L3-7深度修复——核心能力技术细节（~700个skill）

**问题**：L3通过率仅3%，主要瓶颈是L3-2（能力可执行性）和L3-7（内容实质性）

**执行**：
1. 对每个L3-2/L3-7失败的skill：
   - 确保每个###标题下有≥50字符描述
   - 确保有≥2个操作指令指示符（代码引用/表格/代码块/编号列表/bullet/动作动词）
   - 补充具体技术细节，去除通用描述
2. 可能需要读取源skill内容提取真实技术细节

**验证**：`python l3_function_checker.py --batch --limit 200` 确认L3通过率≥30%

### Step 16.5: P1剩余273个skill批量再生成

**目标**：将273个SF 40-69的skill提升到SF≥70

**执行**：
1. 从`p1_recheck_results.json`提取SF<70的skill列表
2. 使用5个并行子代理，每个处理~55个skill
3. 每个子代理：读取源skill→提取能力点→重写生成版本→确保L1+L2+L3+L4通过

**验证**：`python source_fidelity_checker.py --batch --limit 800` 全量SF检查

### Step 16.6: SF V4全量检查

**执行**：`python source_fidelity_checker.py --batch --output sf_batch_results_v4.json`

**目标**：
- SF≥50: ≥90%
- SF≥70: ≥60%
- 平均SF: ≥65

### Step 16.7: 全量L3+L4验证

**执行**：
1. `python l3_function_checker.py --batch --output l3_results.json`
2. `python l4_task_gate.py --batch --output l4_results.json`

**目标**：
- L3通过率: ≥50%（从3%提升）
- L4通过率: ≥30%（从0%提升）

### Step 16.8: 其余parse_frontmatter冗余清理

**执行**：
1. 重构`auto_discover.py`、`enterprise_uploader.py`、`github_scanner.py`、`init_baseline.py`使用`skill_core/parser.py`
2. 确认全项目只有`skill_core/parser.py`一处`parse_frontmatter`实现

### Step 16.9: 生成Round 17提示词

---

## 关键约束

1. **禁止mock/simulate/fallback/pass/todo**：所有修复必须实质性
2. **第一要务是skill高质量完成任务**：L4任务完成能力验证是最终硬关卡
3. **四层门禁不可跳过**：L1→L2→L3→L4，任何一层不通过都不能上传
4. **不创建冗余功能**：新增功能前先检查已有功能，统一使用`skill_core/`模块
5. **打回机制**：L4不通过的skill打回重做，不允许为通过验证而降低标准
6. **不引用开源仓库**：SKILL.md中不包含github.com等链接
7. **slug==name==文件夹名**：三者必须一致
8. **无模板残留**：不包含"触发关键词"、模板套话、占位符

## 文件路径

- **L1检查器**：`quality_gate.py`（10项格式检查）
- **L2-SF检查器**：`source_fidelity_checker.py`（源保真度）
- **L2-Cap检查器**：`l2_capability_checker.py`（能力质量）
- **L3检查器**：`l3_function_checker.py`（7维度功能验证）
- **L3批量修复**：`l3_batch_fix.py`
- **L4检查器**：`l4_task_gate.py`（6维度任务完成能力验证）
- **L4批量修复**：`l4_batch_fix.py`
- **上传门控**：`upload_gate.py`（合规+定价+安全，待重构为编排L1-L4）
- **统一解析层**：`skill_core/parser.py`（frontmatter解析单一来源）
- **DB管理**：`skill_core/db.py` + `config.py`
- **状态分析**：`analyze_status.py`（基于DB的只读分析）
- **健康检查**：`health_check.py`（DB+文件+平台健康报告）
- **质量看板**：`quality_dashboard.py`（5维度质量可视化）
- 生成skill目录：`D:\skills\packaged-skills\skillhub\`
- 源skill目录：`D:\skills\clawhub-skills\downloaded\`
- SF V3结果：`D:\skills\skill-registry\sf_batch_results_v3.json`
- P1重检结果：`c:\Users\thcd\.trae-cn\work\6a5e1d47ef5f370fd441a912\p1_recheck_results.json`

## 执行优先级

1. **P0（最高）**：Step 16.1 upload_gate.py重构（消除最大冗余源头）
2. **P1（高）**：Step 16.2-16.3 L4深度修复（解决84%和87%失败率）
3. **P2（高）**：Step 16.4 L3深度修复（解决3%通过率）
4. **P3（中）**：Step 16.5 P1剩余273个skill再生成
5. **P4（中）**：Step 16.8 其余parse_frontmatter冗余清理
6. **P5（低）**：Step 16.6-16.7 全量验证
7. **P6（最后）**：Step 16.9 生成下一轮提示词

## 预期结果

| 指标 | 当前值 | 目标值 |
|------|--------|--------|
| L1通过率 | 未全量检查 | ≥90% |
| L3通过率 | 3% | ≥50% |
| L4通过率 | 0% | ≥30% |
| SF≥50 | ~60% | ≥90% |
| SF≥70 | ~15% | ≥60% |
| 平均SF | ~50 | ≥65 |
| 冗余parse_frontmatter | 9处 | 1处（skill_core/parser.py） |
| upload_gate冗余检查 | 有 | 0（编排L1-L4） |
