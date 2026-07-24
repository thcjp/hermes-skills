# Round 18: 残留失败修复 + 首批上传

## 背景与上下文

Round 17 完成了 SF提升 + L4闭环 + L3收尾,全量验证结果如下:

| 指标 | Round 16 | Round 17 | 目标 | 状态 |
|------|----------|----------|------|------|
| L3 PASS | 77% | 84% | ≥50% | ✅ |
| L4 PASS | 34% | 69% | ≥50% | ✅ |
| L4 PASS+WARN | 68% | 92% | ≥70% | ✅ |
| SF平均分 | 70.0 | 82.5 | ≥72 | ✅ |
| SF≥70占比 | 49.1% | 94% | ≥80% | ✅ |
| 三关全通过 | - | 75% | ≥60% | ✅ |

**770/1017 skills已通过L3+L4+SF三关验证,可进入上传流程。**

### 残留失败分布 (247 skills, 24%)

| 失败类型 | 数量 | 主要维度 |
|----------|------|----------|
| 仅L3失败 | 141 | L3-2(87), L3-7(59), L3-1(21), L3-5(10) |
| 仅L4失败 | 54 | L4-3(77), L4-4(65), L4-2(57) |
| 仅SF失败 | 31 | SF<70 |
| 多关失败 | 21 | 组合失败 |

### 关键代码文件

- `D:\skills\skill-registry\l3_function_checker.py` - L3检查器(7维度)
- `D:\skills\skill-registry\l3_batch_fix.py` - L3批量修复
- `D:\skills\skill-registry\l4_task_gate.py` - L4检查器(6维度)
- `D:\skills\skill-registry\l4_batch_fix.py` - L4批量修复
- `D:\skills\skill-registry\source_fidelity_checker.py` - SF检查器
- `D:\skills\skill-registry\sf_batch_boost.py` - SF批量提升
- `D:\skills\skill-registry\quality_gate.py` - L1格式检查器(13维度)
- `D:\skills\skill-registry\upload_gate.py` - 上传关卡
- `D:\skills\skill-registry\original_skills_registry.json` - 460个原创skill注册表
- `D:\skills\skill-registry\full_verification_results.json` - 全量验证结果

### 已建立的架构原则

1. **NON_CAPABILITY_HEADINGS**: 元信息标题(能力覆盖范围/技术细节/处理流程/输出格式/脚本获取/命令参数说明/源能力映射/领域术语等),在L3-2/L4-1/L4-5检查器和修复脚本中统一过滤
2. **原创skill注册表**: 460个无clawhub源的skill自动获得SF=100
3. **章节名变体匹配**: `extract_section`支持核心能力/核心功能/核心规则/核心概念/核心原则/核心工作流/核心操作等变体
4. **4层质量门**: L1(格式) → L2(SF+Cap) → L3(功能) → L4(任务) → 上传

## Round 18 目标

1. 将三关全通过率从75%提升到≥90%
2. 770个已通过skill开始上传到SkillHub
3. 247个未通过skill完成残留修复

## 执行步骤

### Step 18.1: L3-2能力可执行性深度修复 (87 skills, 8%)

**问题**: 能力点###标题下内容缺乏具体操作指令(代码/表格/列表/动词),仅有1个指示符

**根因**: `fix_l3_2_actionability`仅在内容完全无指示符时触发补充,但当仅有1个指示符(刚好低于阈值2)时不触发

**修复方案**:
1. 在`l3_batch_fix.py`的`fix_l3_2_actionability`中,将触发条件从"无指示符"改为"指示符<2"
2. 为仅有1个指示符的能力点补充操作指令(添加bullet list + action verb)
3. 运行L3批量修复,验证L3-2通过率

### Step 18.2: L3-7内容实质性深度修复 (59 skills, 5%)

**问题**: 核心能力章节内容过短(<300字符)或过于通用,缺乏具体技术细节

**根因**: `fix_l3_7_substance`扩展核心能力到300+字符,但部分skill的核心能力章节被L4修复覆盖后变短

**修复方案**:
1. 在`l3_batch_fix.py`的`fix_l3_7_substance`中,增加对L4修复后产生的简短核心能力章节的检测
2. 为通用描述补充具体技术参数(如输入格式/输出格式/处理步骤)
3. 运行L3批量修复,验证L3-7通过率

### Step 18.3: L4-3错误恢复可操作性修复 (77 skills, 7%)

**问题**: 错误处理章节缺失或条目仅有空话(如"重试")无具体可执行操作

**根因**: `fix_l4_3_error_recovery`仅在错误处理章节存在时替换空话,不会创建新章节

**修复方案**:
1. 在`l4_batch_fix.py`的`fix_l4_3_error_recovery`中,当错误处理章节缺失时,从`l3_batch_fix.py`的`generate_error_section`生成标准错误处理表
2. 确保每个错误处理条目包含场景+原因+具体处理方式(动作动词)
3. 运行L4批量修复,验证L4-3通过率

### Step 18.4: L4-4依赖闭环性修复 (65 skills, 6%)

**问题**: 声明需要API Key但未给出获取步骤或配置方式

**根因**: `fix_l4_4_dependency_closure`未补充API Key获取步骤和配置方式

**修复方案**:
1. 在`l4_batch_fix.py`中改进`fix_l4_4_dependency_closure`(如不存在则新建)
2. 为声明API Key的skill补充获取步骤(官网链接/注册流程)和配置方式(环境变量/配置文件)
3. 运行L4批量修复,验证L4-4通过率

### Step 18.5: L4-2命令可执行性修复 (57 skills, 5%)

**问题**: 脚本引用无获取方式,命令参数未解释

**根因**: `fix_l4_2_command_executability`已实现但对部分脚本引用场景覆盖不足

**修复方案**:
1. 在`l4_batch_fix.py`的`fix_l4_2_command_executability`中,扩大脚本引用检测范围
2. 为所有未在代码块中的脚本引用补充"脚本获取"说明
3. 运行L4批量修复,验证L4-2通过率

### Step 18.6: SF<70的31个skill深度提升

**问题**: 31个skill的SF分数仍低于70

**修复方案**:
1. 分析31个skill的SF失败维度(能力覆盖率/术语保留/描述深度/差异化)
2. 针对性补充缺失的源能力映射和领域术语
3. 运行SF批量提升,验证SF≥70占比

### Step 18.7: L3-1结构完整性 + L3-5错误处理修复 (31 skills, 3%)

**问题**: L3-1(21 skills)结构不完整,L3-5(10 skills)错误处理不完整

**修复方案**:
1. 运行L3批量修复(已包含L3-1和L3-5修复逻辑)
2. 验证通过率

### Step 18.8: 全量L3+L4+SF验证

**执行**:
1. 对全部1017个skill运行L3+L4+SF检查
2. 确认三关全通过率≥90%
3. 生成最终验证报告

### Step 18.9: 770个已通过skill批量上传SkillHub

**执行**:
1. 使用`upload_gate.py`筛选已通过L1+L2+L3+L4的skill
2. 按P0→P1→P2→P3→P4+P5优先级顺序上传
3. 命令: `skillhub publish /d/skills/packaged-skills/skillhub/[skill-folder] --changelog "[description]"`
4. 记录上传结果,标记已上传skill

### Step 18.10: 生成Round 19提示词

**执行**:
1. 分析Round 18完成情况
2. 生成Round 19提示词文档

## 验证命令

```bash
# L3检查
python l3_function_checker.py --batch

# L4检查
python l4_task_gate.py --batch

# SF检查
python source_fidelity_checker.py --batch

# 全量验证
python c:\Users\thcd\.trae-cn\work\6a5e1d47ef5f370fd441a912\full_verification.py

# L3批量修复
python l3_batch_fix.py --limit 0

# L4批量修复
python l4_batch_fix.py --batch

# SF批量提升
python sf_batch_boost.py --batch
```

## 注意事项

1. **不要降低标准**: 修复的目的是让skill真正能高质量完成任务,不是降低检查标准让其通过
2. **不要引入冗余**: 所有新增功能必须检查是否与已有功能重复
3. **NON_CAPABILITY_HEADINGS一致性**: 任何新增的###元信息标题必须同步添加到所有检查器和修复脚本的NON_CAPABILITY_HEADINGS列表
4. **章节名变体匹配**: 修改`extract_section`时确保所有调用方使用统一的变体匹配规则
5. **上传前验证**: 每个skill上传前必须确认已通过L1+L2+L3+L4全部门
6. **使用brainstorming skill**: 在开始实施前,先用brainstorming skill确认每个步骤的修复策略
7. **使用dogfood skill**: 修复完成后,用dogfood skill对样本skill进行实际任务测试
8. **使用git-commit skill**: 每完成一个步骤后提交代码
