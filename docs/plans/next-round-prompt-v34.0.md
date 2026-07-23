# 下一阶段提示词 v34.0

> **生成时间**: 2026-07-23
> **前置条件**: Round 33 六任务已通过代码级验证并修复(git: 969c6bfc)
> **验证方法**: 三组并行代码验证Agent + hotl:verification-before-completion

---

## 本轮完成状态总结

| 任务 | 优先级 | 代码验证结果 | 修复内容 |
|------|--------|-------------|---------|
| 任务1 License同步 | P0 | ✅ 通过 | 1832 Proprietary + 53 MIT + 31 MIT-0(免费) |
| 任务2 营销话术 | P0 | ❌→✅ 修复 | 92个文件169处: ping污染156+自毁话术5+summary超长8 |
| 任务3 定价元数据 | P1 | ⚠️→✅ 修复 | 1081个NULL修复+39个非标准映射, DB 806→1916 |
| 任务4 L7全量审计 | P1 | ✅ 通过 | 2097个skill, L7a A=1761/B=276/C=60, avg=90.8 |
| 任务5 L7b原型 | P2 | ⚠️→✅ 修复 | L7B_BROKEN_REF空壳→实际检查文件存在性 |
| 任务6 看板增强 | P2 | ✅ 通过 | 4函数+4API+4HTML+4JS, 语法验证OK |

**最终验证**: ping残留=0, 自毁话术=0, NULL pricing_tier=0, 语法检查全通过

---

## 下一阶段任务

### 任务1(P0): L7a C级skill内容修复

**背景**: L7a审计发现60个C级skill(评分50),存在模板块填充和内容重复问题

**具体操作**:
1. 从 `deep_quality_audit_report.json` 中提取所有L7a C级skill的slug列表
2. 对每个C级skill:
   - 识别L7A_TEMPLATE_DETECTED标记的模板块(相似度=1.000的填充内容)
   - 识别L7A_DUPLICATE_BLOCKS标记的重复内容块(相似度>0.92)
   - 自动清理: 用差异化内容替换模板块,删除重复段落
   - 或标记为需要人工审查,生成修复建议
3. 清理后重新运行 `python deep_quality_audit.py --layer7` 验证等级提升
4. 目标: C级skill数量从60降至0(全部提升至B级或以上)

### 任务2(P0): L7b全量可执行性审查

**背景**: L7B_BROKEN_REF已修复为实际检查,需要对全部skill运行

**具体操作**:
1. 运行 `python deep_quality_audit.py --layer7 --layer7b` 对全部2097个skill
2. 收集L7b检测结果,统计6项检查的触发分布:
   - L7B_NO_CODE: 声称有脚本但无代码块
   - L7B_BROKEN_REF: 引用了不存在的脚本/文件
   - L7B_VAGUE_TASK: 模糊任务描述
   - L7B_MISSING_INPUT: 缺少输入参数说明
   - L7B_NO_OUTPUT: 缺少输出格式说明
   - L7B_CONTRADICTION: 免费/付费矛盾声明
3. 对L7B_BROKEN_REF检测到的问题,自动修复(删除不存在的脚本引用或创建占位文件)
4. 对其他L7b问题,生成修复清单和建议
5. 输出"可执行性验证报告"

### 任务3(P1): 定价模型校准

**背景**: 当前分布L3=937(48.8%)+L4=796(41.6%)过于集中,L1=4(0.2%)+L2=179(9.3%)占比过低

**具体操作**:
1. 分析当前评分模型的问题:
   - 评分阈值是否合理(>=15→L4, >=10→L3, >=6→L2, <6→L1)
   - 关键词权重是否需要调整
   - 是否需要增加新的评分维度
2. 调整评分模型参数:
   - 提高L1/L2的门槛(降低阈值或增加维度)
   - 或增加更多基础工具类关键词到LOW_VALUE_KEYWORDS
   - 考虑skill的实际市场定位(工具类vs平台类vs服务类)
3. 重新评估全部skill的定价等级
4. 更新DB和SKILL.md frontmatter
5. 目标分布: L1≈10%, L2≈30%, L3≈40%, L4≈20%

### 任务4(P1): 全量summary质量审查

**背景**: 已发现2个summary含"（根据实际场景填充）"占位符,可能还有更多

**具体操作**:
1. 扫描全部skill的summary字段,检测:
   - 占位符文本("根据实际场景填充"、"TODO"、"待补充"等)
   - 模板化文本("提供X - 生成Y - 支持Z"格式重复)
   - 长度超标(>100字符)
   - 长度过短(<10字符)
   - 含英文(应全部中文化)
2. 对有问题的summary,用"痛点+方案+量化+差异"公式重写
3. 每个summary控制在20字/100字内
4. 更新DB和SKILL.md frontmatter
5. 输出summary质量报告

### 任务5(P2): 看板实际运行验证

**背景**: dashboard_server.py代码验证通过,但未实际启动验证页面渲染

**具体操作**:
1. 启动 `python dashboard_server.py` 在后台运行
2. 使用browser工具访问 http://localhost:8765
3. 截图验证以下区块正确渲染:
   - Layer 7 语义审计区块(显示A/B/C等级分布柱状图)
   - 定价分布区块(显示L1-L4分布柱状图)
   - 营销话术质量卡片(显示已清理743/已优化8/专享表826)
   - License一致性卡片(显示100%一致性)
4. 验证API端点返回正确数据:
   - /api/l7-audit
   - /api/pricing
   - /api/marketing
   - /api/license
5. 如有渲染问题,修复HTML/CSS/JS代码

### 任务6(P2): 全自动流水线Step 1启动

**背景**: 根据 full-automation-pipeline-design.md,开始实施多源头发现系统

**具体操作**:
1. 阅读 `D:\skills\docs\plans\full-automation-pipeline-design.md` 的Step 1部分
2. 创建 `d:\skills\skill-registry\multi_source_discover.py`
3. 实现以下扫描器(复用auto_discover.py的fetch_url等函数):
   - GitHub AI项目扫描器(扩展搜索关键词)
   - N8N社区扫描器
   - Dify社区扫描器
   - Coze社区扫描器
   - Hermes社区扫描器
   - awesome-lists扫描器
4. 统一输出到 `d:\skills\skill-registry\discovery\candidates_unified.json`
5. 扫描结果记录到数据库sources表

---

## 执行要求

1. **必须代码级验证**: 每个任务完成后,使用三组并行Agent验证实际代码,不接受仅文档/报告验证
2. **集成升级增强**: 所有修改必须是集成升级,不是新增碎片化模块
3. **每完成一个任务生成下一个任务的提示词**
4. **禁止任何形式的mock/fallback/todo/占位符**
5. **使用staff-engineer-mode进行架构决策,hotl进行验证,coderabbit进行代码审查**
6. **Git commit带anti-reversion注释**
