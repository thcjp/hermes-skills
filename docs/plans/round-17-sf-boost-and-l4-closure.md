# Round 17: SF提升 + L3/L4收尾 + 无源skill处理

## 背景与Round 16实际完成情况（代码层面验证）

### Round 16 实际完成情况

| 任务 | 计划 | 实际完成 | 验证方式 |
|------|------|---------|---------|
| upload_gate.py重构 | 编排L1-L4 | ✅ v2.0完成,13项L1检查 | upload_gate.py代码审查+测试 |
| L4-1/L4-3深度修复 | 批量修复 | ✅ 833个skill已修复 | L4 PASS 0%→34%, L4-1 79%→12%, L4-3 92%→8% |
| L3深度修复 | L3-2/L3-3/L3-4/L3-7 | ✅ 1006个skill已修复 | L3 PASS 0%→72%, L3-3 86%→0%, L3-7 59%→3% |
| SF V4全量检查 | 全量 | ✅ 完成 | sf_batch_results_v4.json |
| 其余parse_frontmatter冗余清理 | 4个文件 | ✅ 完成 | auto_discover/github_scanner/init_baseline/enterprise_uploader |
| P1剩余273个skill再生成 | 273个 | ❌ 未完成 | 280个SF 40-69的skill仍需重新生成 |
| L3+L4全量验证 | 全量 | ✅ 100样本验证 | L3 72% PASS, L4 34% PASS + 34% WARN |

### 当前质量指标（100样本）

| 指标 | Round 15 | Round 16 | 目标 | 状态 |
|------|---------|---------|------|------|
| L3 PASS | 3% | 72% | ≥50% | ✅ 达标 |
| L4 PASS | 0% | 34% | ≥30% | ✅ 达标 |
| L4 PASS+WARN | 0% | 68% | ≥50% | ✅ 达标 |
| SF平均分 | 65.3 | 70.0 | ≥65 | ✅ 达标 |
| SF≥70占比 | 35.3% | 49.1% | ≥60% | ❌ 未达标 |
| 无源skill | 244 | 244 | 0 | ❌ 未处理 |

### 当前L3各维度失败率（100样本）

| 维度 | 失败率 | 主要原因 |
|------|--------|---------|
| L3-1 结构完整性 | 3% | 少数skill缺少必需章节 |
| L3-2 能力可执行性 | 16% | 部分###标题仍缺操作指令 |
| L3-3 场景覆盖率 | 0% | 已完全修复 |
| L3-4 指令清晰度 | 0% | 已完全修复 |
| L3-5 错误处理完整性 | 0% | 已完全修复 |
| L3-6 依赖准确性 | 11% | 部分依赖说明缺少可用性分类 |
| L3-7 内容实质性 | 3% | 少数skill核心能力<300字符 |

### 当前L4各维度失败率（50样本）

| 维度 | 失败率 | 主要原因 |
|------|--------|---------|
| L4-1 任务可映射性 | 12% | 少数skill核心能力<3个###标题 |
| L4-2 命令可执行性 | 26% | 脚本引用无获取说明,命令参数未解释 |
| L4-3 错误恢复可操作性 | 8% | 基本修复完成 |
| L4-4 依赖闭环性 | 0% | 已完全修复 |
| L4-5 输出标准明确性 | 38% | 核心能力缺少输出格式说明 |
| L4-6 用户体验完整性 | 22% | 使用流程非线性,缺少FAQ |

### SF V4分布（556个有源skill）

| 范围 | 数量 | 占比 |
|------|------|------|
| 0-39 | 3 | 0.5% |
| 40-49 | 32 | 5.8% |
| 50-59 | 113 | 20.3% |
| 60-69 | 135 | 24.3% |
| 70-79 | 103 | 18.5% |
| 80-89 | 120 | 21.6% |
| 90-100 | 50 | 9.0% |

---

## Round 17 目标

**核心原则：第一要务是skill高质量完成任务。不通过的skill必须打回重做。**

### Step 17.1: 无源skill处理（244个）

**问题**：244个skill没有源skill，无法进行SF检查。这些skill是原创的或来源不明的。

**执行**：
1. 扫描244个无源skill，分类：
   - 原创skill（无源）：标记为"原创"，跳过SF检查
   - 源skill路径错误：修正路径，重新检查SF
   - 源skill被删除：从备份恢复或标记为"无源"
2. 对原创skill，建立替代验证：L1+L3+L4全通过即可上传
3. 对源skill路径错误的，修正`source_fidelity_checker.py`的源skill查找逻辑

**验证**：`python source_fidelity_checker.py --batch` 确认无源skill数量减少

### Step 17.2: SF 40-69的280个skill批量提升（核心任务）

**问题**：280个skill的SF分数在40-69之间，未达到SF≥70的目标

**执行**：
1. 从`sf_batch_results_v4.json`提取SF 40-69的280个skill列表
2. 分析每个skill的SF失败原因：
   - 能力覆盖率低（cov<100%）：补充缺失能力点
   - 领域术语保留低（term<30%）：补充领域术语
   - 错误场景不足（err<5）：补充错误处理
3. 使用LLM重新生成这些skill的核心能力章节
4. 或者：基于源skill内容，手动补充缺失的能力点和术语

**策略**：
- 优先处理SF 40-49的32个skill（最差）
- 然后处理SF 50-59的113个skill
- 最后处理SF 60-69的135个skill

**验证**：`python source_fidelity_checker.py --batch --output sf_batch_results_v5.json` 确认SF≥70占比≥60%

### Step 17.3: L4-5输出标准明确性深度修复（38%失败率）

**问题**：38%的skill核心能力缺少输出格式说明

**执行**：
1. 扫描所有L4-5失败的skill
2. 对每个skill的核心能力###标题：
   - 补充输出格式说明（JSON/CSV/Markdown/文本/表格）
   - 补充输出内容描述（返回什么数据）
   - 补充成功/失败判断标准
3. 更新`l4_batch_fix.py`的`fix_l4_5_output_clarity`函数

**验证**：`python l4_task_gate.py --batch --limit 100` 确认L4-5失败率<15%

### Step 17.4: L4-2命令可执行性修复（26%失败率）

**问题**：26%的skill脚本引用无获取说明，命令参数未解释

**执行**：
1. 扫描所有L4-2失败的skill
2. 对每个引用的脚本/命令：
   - 补充scripts目录说明或安装说明
   - 补充命令参数解释
   - 或在代码块中给出完整调用示例
3. 更新`l4_batch_fix.py`添加`fix_l4_2_command_executability`函数

**验证**：`python l4_task_gate.py --batch --limit 100` 确认L4-2失败率<15%

### Step 17.5: L4-6用户体验完整性修复（22%失败率）

**问题**：22%的skill使用流程非线性，缺少FAQ

**执行**：
1. 扫描所有L4-6失败的skill
2. 对每个skill：
   - 确保使用流程是线性步骤（1→2→3→4）
   - 补充FAQ章节（≥3个常见问题）
   - free版补充升级提示
3. 更新`l4_batch_fix.py`添加`fix_l4_6_user_experience`函数

**验证**：`python l4_task_gate.py --batch --limit 100` 确认L4-6失败率<10%

### Step 17.6: L3-2/L3-6收尾修复

**问题**：L3-2仍有16%失败率，L3-6仍有11%失败率

**执行**：
1. L3-2：对剩余失败的skill，确保每个###标题有≥2个细节指示符
2. L3-6：对剩余失败的skill，补充依赖说明的可用性分类（MD/EXEC）

**验证**：`python l3_function_checker.py --batch --limit 100` 确认L3通过率≥80%

### Step 17.7: 全量L3+L4+SF验证

**执行**：
1. `python l3_function_checker.py --batch --output l3_results_v2.json`
2. `python l4_task_gate.py --batch --output l4_results_v2.json`
3. `python source_fidelity_checker.py --batch --output sf_batch_results_v5.json`

**目标**：
- L3通过率: ≥80%
- L4通过率: ≥50%（PASS+WARN ≥70%）
- SF≥70占比: ≥60%
- SF平均分: ≥72

### Step 17.8: 生成Round 18提示词

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
9. **非能力点标题过滤**：检查器和批量修复都需跳过"能力覆盖范围"、"技术细节"等元信息标题

## 文件路径

- **L1检查器**：`quality_gate.py`（13项格式检查）
- **L2-SF检查器**：`source_fidelity_checker.py`（源保真度）
- **L2-Cap检查器**：`l2_capability_checker.py`（能力质量）
- **L3检查器**：`l3_function_checker.py`（7维度功能验证）
- **L3批量修复**：`l3_batch_fix.py`
- **L4检查器**：`l4_task_gate.py`（6维度任务完成能力验证）
- **L4批量修复**：`l4_batch_fix.py`
- **上传门控**：`upload_gate.py` v2.0（编排L1-L4+合规+定价+安全）
- **统一解析层**：`skill_core/parser.py`（frontmatter解析单一来源）
- **规则定义**：`skill_core/rules.py`（格式规则常量）
- **检查函数**：`skill_core/checks.py`（L1检查函数库）
- **DB管理**：`skill_core/db.py` + `config.py`
- 生成skill目录：`D:\skills\packaged-skills\skillhub\`
- 源skill目录：`D:\skills\clawhub-skills\downloaded\`
- SF V4结果：`D:\skills\skill-registry\sf_batch_results_v4.json`

## 执行优先级

1. **P0（最高）**：Step 17.2 SF 40-69的280个skill批量提升（核心质量瓶颈）
2. **P1（高）**：Step 17.1 无源skill处理（消除244个验证盲区）
3. **P2（高）**：Step 17.3-17.5 L4-5/L4-2/L4-6深度修复（L4收尾）
4. **P3（中）**：Step 17.6 L3-2/L3-6收尾修复
5. **P4（中）**：Step 17.7 全量验证
6. **P5（最后）**：Step 17.8 生成下一轮提示词
