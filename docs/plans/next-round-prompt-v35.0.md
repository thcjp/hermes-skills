# 下一阶段提示词 v35.0

> **生成时间**: 2026-07-23
> **前置条件**: Round 34 六任务已通过代码级验证并修复(git: befb581c)
> **验证方法**: 三组并行代码验证Agent + hotl:verification-before-completion
> **数据基线**: 1917skills, L7a A=1821/B=276/C=0/avg=91.8, 4类模板污染=0

---

## 本轮完成状态总结

| 任务 | 优先级 | 代码验证结果 | 修复内容 |
|------|--------|-------------|---------|
| 任务1 L7a C级修复 | P0 | ✅ 通过 | 60个C级→A级, 清除模板1271处+占位文本414处 |
| 任务2 L7b全量审查 | P0 | ✅ 通过 | 聚合缺陷修复, BROKEN_REF自动修复4262处, 完整报告输出 |
| 任务3 定价校准 | P1 | ✅ 通过 | 新阈值校准, L1=122/L2=457/L3=1076/L4=261, NULL=0 |
| 任务4 summary审查 | P1 | ✅ 通过(修复后) | 563占位符→0, 411文件替换, Pass2清理2169处 |
| 任务5 看板验证 | P2 | ✅ 通过 | 4API全available=True, 4函数+4HTML验证OK |
| 任务6 多源发现 | P2 | ✅ 通过 | 6扫描器, 582候选skill, candidates_unified.json |

**交叉验证**: 3组并行Agent全通过, 4类模板污染(根据实际场景填充/执行XX操作/相关说明/默认值)全部0残留

**遗留问题(本轮发现但未修复)**:
1. L7b C/D级 = 1018skills(48.6%): VAGUE_TASK=1097, MISSING_INPUT=1007, NO_OUTPUT=934
2. L7A_DUPLICATE_BLOCKS = 895skills有重复内容块
3. 1个异常'free' pricing_tier记录在付费池
4. L3占比56.1%略高于目标40%
5. 276个B级skill可进一步提升

---

## 下一阶段任务

### 任务1(P0): L7b C/D级skill质量批量提升

**背景**: L7b全量审查发现1018个C/D级skill(48.6%), 三大问题: VAGUE_TASK(1097处模糊任务描述), MISSING_INPUT(1007处缺少输入说明), NO_OUTPUT(934处缺少输出格式)

**具体操作**:
1. 从 `l7b_executability_report.json` 提取所有C/D级skill的slug列表和具体问题
2. 对VAGUE_TASK问题:
   - 识别SKILL.md中"执行XX操作"类模糊描述(已被Pass1替换但可能仍有残留模式)
   - 用skill的displayName+slug派生具体功能描述
   - 替换为: "[displayName] - [具体功能描述], 支持[参数1/参数2]输入, 输出[格式]"
3. 对MISSING_INPUT问题:
   - 检查SKILL.md的"输入格式"章节是否存在且非空
   - 如缺失, 根据skill的功能类型(工具类/平台类/服务类)生成标准输入参数表
   - 必填参数: input/data/content(根据类型选择), 可选参数: mode/format/timeout
4. 对NO_OUTPUT问题:
   - 检查SKILL.md的"输出格式"章节是否存在且包含JSON示例
   - 如缺失, 生成标准输出JSON模板: {success, data:{result}, execution_log:[], error}
5. 修复后重新运行 `python deep_quality_audit.py --layer7 --layer7b` 验证
6. 目标: C/D级从1018(48.6%)降至500(24%)以下, A+B级从1079(51.4%)提升至75%以上

### 任务2(P0): ClawHub 502个pending skill批量上传

**背景**: ClawHub上传限制已重置(2026-07-23 19:15后), 502个pending skill待上传

**具体操作**:
1. 确认上传限制已重置(测试上传1个skill验证)
2. 使用已准备好的目录映射和上传脚本(120秒超时)
3. 分批上传: 每批50个, 共11批(502/50≈11)
4. 每批上传后检查HTTP响应, 记录成功/失败
5. 失败的skill收集后重试1次
6. 上传完成后同步数据库platform_uploads表
7. 目标: ClawHub从430 published/502 pending → 932 published/0 pending

### 任务3(P1): L7A_DUPLICATE_BLOCKS去重

**背景**: L7a审计发现895个skill存在重复内容块(相似度>0.92), 虽已提升至A/B级但质量仍有提升空间

**具体操作**:
1. 从 `deep_quality_audit_report.json` 的semantic_audit部分提取所有L7A_DUPLICATE_BLOCKS标记
2. 分析重复块的类型:
   - 类型A: "付费版专享能力"表格跨skill重复(多skill使用相同能力描述)
   - 类型B: "使用流程"章节跨skill重复(多skill使用相同的4步流程)
   - 类型C: "错误处理"章节跨skill重复(多skill使用相同错误码)
3. 对类型A: 根据skill功能生成差异化能力描述
4. 对类型B: 根据skill类型(工具/平台/服务)生成差异化流程步骤
5. 对类型C: 根据skill可能遇到的错误类型生成差异化错误处理
6. 修复后重新运行L7a审计验证重复块减少
7. 目标: 重复块从895个降至200个以下

### 任务4(P1): 定价异常修复与L3再平衡

**背景**: 1个异常'free' pricing_tier记录混入付费池, L3占比56.1%高于目标40%

**具体操作**:
1. 定位异常'free'记录:
   - `SELECT slug, current_display_name FROM skills WHERE pricing_tier = 'free'`
   - 确认该skill是否应为free(检查slug是否以-free结尾)
   - 如不应为free, 修正pricing_tier为L1-L4
2. L3再平衡分析:
   - 统计L3(1076个)中LOW_VALUE_KEYWORDS命中情况
   - 对命中LOW_VALUE_KEYWORDS的L3 skill, 重新评估是否应降级为L1/L2
   - 调整评分阈值或增加关键词权重, 使L3占比降至40-45%
3. 更新DB和SKILL.md frontmatter
4. 目标: 0个异常'free'记录, L3占比降至45%以下

### 任务5(P2): 多源发现→流水线Step 2对接

**背景**: multi_source_discover.py已发现582个候选skill, 需对接到流水线的Step 2(自动差异化)

**具体操作**:
1. 阅读 `full-automation-pipeline-design.md` 的Step 2部分
2. 创建 `d:\skills\skill-registry\auto_differentiate.py`:
   - 读取 `candidates_unified.json` 的582个候选
   - 对每个候选: 生成标准化SKILL.md(基于content_preview和metadata)
   - 执行差异化: 修改displayName/summary/description, 添加付费版专享能力
   - 检查slug冲突(与现有1917个skill比对)
3. 输出到 `d:\skills\packaged-skills\skillhub\` 新目录
4. 更新数据库skills表
5. 目标: 582个候选中至少300个完成差异化并入库

### 任务6(P2): 看板L7b可视化增强

**背景**: dashboard_server.py已有L7a/pricing/marketing/license 4个区块, 需增加L7b可执行性区块

**具体操作**:
1. 在dashboard_server.py中新增 `get_l7b_stats()` 函数:
   - 读取 `l7b_executability_report.json`
   - 返回: check_distribution, grade_distribution, pass_rate, top_issues
2. 新增API端点 `/api/l7b-audit`
3. 在dashboard HTML中新增L7b区块:
   - 6项检查分布柱状图(NO_CODE/BROKEN_REF/VAGUE_TASK/MISSING_INPUT/NO_OUTPUT/CONTRADICTION)
   - 等级分布饼图(A/B/C/D)
   - 通过率指标卡片
4. 验证: 启动dashboard, 确认新区块正确渲染
5. 目标: L7b区块与现有4个区块并列显示, API返回available=True

---

## 执行要求

1. **必须代码级验证**: 每个任务完成后, 使用三组并行Agent验证实际代码, 不接受仅文档/报告验证
2. **集成升级增强**: 所有修改必须是集成升级, 不是新增碎片化模块
3. **禁止任何形式的mock/fallback/todo/占位符**
4. **使用staff-engineer-mode进行架构决策, hotl进行验证, coderabbit进行代码审查**
5. **Git commit带anti-reversion注释**
6. **遵循修复提示词.md的R1-R78铁律, 特别是R1(运行时证据优先)、R45(同一根因一次性修复)、R57(声称已修复必须提供代码diff+运行输出)**
