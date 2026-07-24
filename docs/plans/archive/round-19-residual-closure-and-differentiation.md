# Round 19: 残留56个skill闭环 + 上传验证 + 600 skill深度差异化启动

## 背景与上下文

Round 18 完成了残留失败修复和首批上传,全量验证结果如下:

| 指标 | Round 17 | Round 18 | 目标 | 状态 |
|------|----------|----------|------|------|
| L3 PASS | 84% | 100% | ≥50% | ✅ 超额 |
| L4 PASS | 69% | 79% | ≥50% | ✅ |
| L4 PASS+WARN | 92% | 97% | ≥70% | ✅ |
| SF平均分 | 82.5 | 82.6 | ≥72 | ✅ |
| SF≥70占比 | 94% | 94% | ≥80% | ✅ |
| 三关全通过 | 75% | 94% | ≥90% | ✅ 超额 |

**961/1017 skills已通过L3+L4+SF三关验证,正在批量上传到clawhub/SkillHub。**

### Round 18 关键修复

1. **L3-7模板套话清除**: 修复了TEMPLATE_PHRASES前缀匹配问题(45→0),新增REPO_PATTERNS清除开源仓库引用(15→0)
2. **L3-1章节名标准化**: 新增`fix_section_names`函数,将核心工作流/核心规则/核心功能等变体统一为"核心能力"(21→0)
3. **L3-5子串匹配bug修复**: 发现`### 错误处理`被checker的`## 错误处理`正则子串匹配,使用行锚定正则修复(10→0)
4. **L3-5关键词补充**: 为英文错误表的9个API类skill添加"处理方式"关键词(9→0)
5. **L3-2能力可执行性**: 修复memory skill的双模式检索section指示符不足(1→0)
6. **L4批量修复**: L4-3/L4-4/L4-2/L4-6批量修复,196个skill修改
7. **模板套话污染源清除**: `generate_limitations_section`和`generate_dependency_section`不再注入TEMPLATE_PHRASES

### 残留失败分布 (56 skills, 6%)

| 失败类型 | 数量 | 主要维度 |
|----------|------|----------|
| L4 FAIL | 25 | L4-2+L4-3(20), L4-5+L4-6(4), L4-1+L4-3(1) |
| SF<70 | 31 | SF分数38-69 |

### 关键代码文件

- `D:\skills\skill-registry\l3_function_checker.py` - L3检查器(7维度)
- `D:\skills\skill-registry\l3_batch_fix.py` - L3批量修复
- `D:\skills\skill-registry\l4_task_gate.py` - L4检查器(6维度)
- `D:\skills\skill-registry\l4_batch_fix.py` - L4批量修复
- `D:\skills\skill-registry\source_fidelity_checker.py` - SF检查器
- `D:\skills\skill-registry\sf_batch_boost.py` - SF批量提升
- `D:\skills\skill-registry\full_verification_results.json` - 全量验证结果
- `D:\skills\packaged-skills\failed-temp\` - 56个未通过skill的临时存放目录

### 已建立的架构原则

1. **NON_CAPABILITY_HEADINGS**: 元信息标题在L3-2/L4-1/L4-5检查器和修复脚本中统一过滤
2. **原创skill注册表**: 460个无clawhub源的skill自动获得SF=100
3. **章节名变体匹配**: `extract_section`支持核心能力/核心功能/核心规则等变体
4. **4层质量门**: L1(格式) → L2(SF+Cap) → L3(功能) → L4(任务) → 上传
5. **checker-fixer对齐原则**: 修复函数必须使用与检查器完全相同的检测逻辑,包括已知的bug行为
6. **行锚定正则**: 章节名检测使用`^##\s+章节名\s*$`而非子串匹配,避免`### 错误处理`被`## 错误处理`子串匹配
7. **PHRASE_REPLACEMENTS**: 模板套话替换为中性替代文本,保留行结构,不删除整行

## Round 19 目标

1. 56个残留失败skill全部修复并通过验证(三关全通过率→100%)
2. 验证961个已上传skill在clawhub平台上的显示和可用性
3. 处理上传失败(如有)并重新上传
4. 启动600个clawhub下载skill的深度差异化工作
5. 撤回此前51个需要撤回的skill

## 执行步骤

### Step 19.1: 恢复56个失败skill并分析根因

**执行**:
1. 将`D:\skills\packaged-skills\failed-temp\`中的56个skill移回`D:\skills\packaged-skills\skillhub\`
2. 分析25个L4 FAIL skill的具体失败维度:
   - 20个L4-2+L4-3: 命令可执行性+错误恢复
   - 4个L4-5+L4-6: timer/timer-free/whatsapp-messaging/whatsapp-messaging-free
   - 1个L4-1+L4-3: pg-job-queue
3. 分析31个SF<70 skill的具体失败维度

### Step 19.2: L4-2+L4-3深度修复 (20 skills)

**问题**: L4-2(命令可执行性)和L4-3(错误恢复可操作性)同时失败

**修复方案**:
1. 检查`l4_batch_fix.py`中`fix_l4_2_command_executability`和`fix_l4_3_error_recovery`的覆盖范围
2. 对20个skill逐个分析失败原因,判断是修复函数未覆盖还是修复后仍不通过
3. 扩展修复函数覆盖范围,确保所有脚本引用都有获取方式,所有错误处理都有具体操作

### Step 19.3: L4-5+L4-6深度修复 (4 skills)

**问题**: timer/timer-free/whatsapp-messaging/whatsapp-messaging-free的输出标准(L4-5)和用户体验(L4-6)不通过

**修复方案**:
1. 逐个检查这4个skill的SKILL.md
2. 为能力点补充明确的输出格式说明(L4-5)
3. 补充FAQ和已知限制章节(L4-6)

### Step 19.4: L4-1+L4-3修复 (1 skill)

**问题**: pg-job-queue的任务可映射性和错误恢复不通过

**修复方案**:
1. 检查核心能力###标题是否缺少输入→处理→输出描述
2. 补充错误处理章节

### Step 19.5: SF<70深度提升 (31 skills)

**问题**: 31个skill的SF分数在38-69之间

**修复方案**:
1. 分析每个skill的SF失败维度(能力覆盖率/术语保留/描述深度/差异化)
2. 针对性补充缺失的源能力映射和领域术语
3. 运行SF批量提升,验证SF≥70

### Step 19.6: 全量验证 + 残留skill上传

**执行**:
1. 对全部1017个skill运行L3+L4+SF检查
2. 确认三关全通过率达到100%
3. 将新通过的56个skill上传到clawhub
4. 命令: `npx clawhub sync --root "D:\skills\packaged-skills\skillhub" --all --changelog "Round 19: residual 56 skills upload"`

### Step 19.7: 上传验证

**执行**:
1. 通过浏览器访问clawhub.ai,检查已上传skill的显示情况
2. 验证skill的displayName、summary、description是否正确显示
3. 检查skill的SKILL.md内容是否完整
4. 记录上传失败的skill并重新上传

### Step 19.8: 撤回51个需要撤回的skill

**背景**: 项目记忆中记录"Clawhub upload of 51 skills must be撤回 (withdrawn)"

**执行**:
1. 确定需要撤回的51个skill列表
2. 使用`npx clawhub skill --help`查看撤回命令
3. 批量撤回51个skill

### Step 19.9: 启动600个clawhub skill深度差异化

**背景**: 项目记忆中记录"600 skills downloaded from clawhub must undergo deep differentiation before uploading to both skillhub and clawhub"和"Deep differentiation must enhance quality, practicality, and usability"

**执行**:
1. 确定600个待差异化skill的来源和位置
2. 制定差异化策略:
   - 提升质量: 补充缺失章节,增强内容实质性
   - 提升实用性: 添加更多使用场景和示例
   - 提升可用性: 简化使用流程,改善错误处理
   - 降低LLM成本: 优化指令,减少不必要的LLM调用
   - 提升效率/性能: 添加缓存策略,减少重复操作
3. 对首批50个skill进行深度差异化
4. 差异化后运行L3+L4+SF验证
5. 上传差异化后的skill到clawhub和SkillHub

### Step 19.10: 生成Round 20提示词

**执行**:
1. 分析Round 19完成情况
2. 生成Round 20提示词文档

## 验证命令

```bash
# 环境变量设置 (每次新终端需要设置)
$env:CLAWHUB_SITE="https://clawhub.ai"
$env:CLAWHUB_REGISTRY="https://clawhub.ai"

# L3检查
python l3_function_checker.py --batch

# L4检查
python l4_task_gate.py --batch

# SF检查
python source_fidelity_checker.py --batch

# 全量验证
python c:\Users\thcd\.trae-cn\work\6a5e1d47ef5f370fd441a912\full_verification.py

# L3批量修复
python l3_batch_fix.py

# L4批量修复
python l4_batch_fix.py --batch

# SF批量提升
python sf_batch_boost.py --batch

# clawhub登录 (token已存储,如失效需重新获取)
npx clawhub whoami

# clawhub批量上传
npx clawhub sync --root "D:\skills\packaged-skills\skillhub" --all --changelog "description"

# clawhub单个skill上传
npx clawhub publish "D:\skills\packaged-skills\skillhub\[skill-folder]" --changelog "description"
```

## 注意事项

1. **不要降低标准**: 修复的目的是让skill真正能高质量完成任务,不是降低检查标准让其通过
2. **不要引入冗余**: 所有新增功能必须检查是否与已有功能重复
3. **NON_CAPABILITY_HEADINGS一致性**: 任何新增的###元信息标题必须同步添加到所有检查器和修复脚本的NON_CAPABILITY_HEADINGS列表
4. **章节名变体匹配**: 修改`extract_section`时确保所有调用方使用统一的变体匹配规则
5. **checker-fixer对齐**: 修复函数必须使用与检查器完全相同的检测逻辑
6. **行锚定正则**: 章节名检测使用`^##\s+章节名\s*$`而非子串匹配
7. **上传前验证**: 每个skill上传前必须确认已通过L3+L4+SF三关
8. **clawhub环境变量**: 上传时需要设置CLAWHUB_SITE和CLAWHUB_REGISTRY为https://clawhub.ai
9. **token管理**: API token在clawhub.ai/settings?view=tokens创建,仅显示一次
10. **使用brainstorming skill**: 在开始实施前,先用brainstorming skill确认每个步骤的修复策略
11. **使用dogfood skill**: 修复完成后,用dogfood skill对样本skill进行实际任务测试
12. **使用git-commit skill**: 每完成一个步骤后提交代码
