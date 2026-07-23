# Round 36 执行提示词 v36.0

## 上下文
- **上一轮**: Round 35 (Git: b5ad269b, 1837 files, +64084/-40812)
- **当前日期**: 2026-07-24
- **数据库**: 1917 skills, 0 NULL pricing_tier, 0 'free' tier
- **平台状态**: SkillHub 2068 published/7 pending_review, ClawHub 432 published/300 pending, Hermes 1067 published

## Round 35 完成情况

### Task 1 (P0): L7b综合修复 - 完成 ✅
- **发现的关键问题**: 上一轮修复只覆盖了`packaged-skills/skillhub`目录,**遗漏了`differentiated-skills`和`opensource-skills/packaged`两个目录**
- **综合修复**: 扫描2137个SKILL.md文件,修改1182个文件
  - VAGUE_TASK: 9961处修复(13种模式),验证后=0 ✅
  - MISSING_INPUT: 733个输入格式节添加,验证后=0 ✅  
  - NO_OUTPUT: 772个输出格式节添加,验证后=0 ✅
- **L7a改善**: avg_score 91.8→100.0, template_blocks 276→0, 全部A级

### Task 2 (P0): ClawHub批量上传 - 部分完成 ⚠️
- 创建`clawhub_batch_uploader.py`(支持shell=True、断点续传、版本递增)
- 今日上传2个: podcast-toolkit-free, model-routing-tool-free
- **限流**: 200/24h窗口已满,剩余300个待续传
- **续传命令**: `python clawhub_batch_uploader.py --resume`

### Task 3 (P1): L7A去重 - 部分完成 ⚠️
- 99个标记skills的155个重复块对已消除(100%)
- **全量扫描发现**: 仍有1211个重复块对分布在788个文件中
- 73个文件存在重复章节标题(如`## 付费版专享能力`出现2次)

### Task 4 (P1): 定价异常修复 - 完成 ✅
- pdf-workflow-suite: free→L2/monthly/19.9
- 0个'free' pricing_tier, 0个NULL pricing_tier

### Task 5 (P2): 多源自动差异化 - 完成 ✅
- 创建`auto_differentiate.py`,7步流水线
- 函数: resolve_slug_conflict, generate_skill_md, evaluate_pricing_tier
- CLI: --limit, --source, --dry-run, 测试通过

### Task 6 (P2): 看板L7b可视化 - 完成 ✅
- dashboard_server.py添加get_l7b_stats()、/api/l7b-audit端点
- HTML块含4个指标卡+等级图表+检查项列表

## 交叉验证发现的遗留问题

### 1. Critical: MISSING_TOOLS/MISSING_TAGS (952+文件)
- 审计发现`differentiated-skills`目录下952+个文件缺少`tools`和`tags`字段
- 审计因critical issues提前退出,导致L7b报告未更新

### 2. Critical: autopilot-flow缺失核心字段
- MISSING_SLUG, MISSING_VERSION, MISSING_NAME
- 路径: `differentiated-skills/Automation/autopilot-flow/SKILL.md`

### 3. L7A全量去重未完成
- 1211个重复块对(788个文件)未处理
- 主要类型: 表格分隔符重复(788文件)、通用付费能力行重复(1423文件)、重复章节标题(73文件)

### 4. L7b报告未更新
- `reports/l7b_executability_report.json`仍显示旧数据(A=554/B=525/C=539/D=478/F=1)
- 原因: 审计因critical issues退出,未执行L7b报告生成
- 直接验证已确认: VAGUE_TASK=0, MISSING_INPUT=0, NO_OUTPUT=0

### 5. L3定价占比过高
- L3=1076/1917=56.1%, 需要基于display_name进行重新评估
- 上一轮使用中文关键词匹配英文slug导致0命中

### 6. ClawHub 300个待上传
- 限流200/24h,需在限流窗口重置后续传

### 7. SkillHub 7个pending_review
- 仍在平台审核队列中

## Round 36 任务清单

### Task 1 (P0): 修复MISSING_TOOLS/MISSING_TAGS/MISSING_SLUG critical issues
**目标**: 消除全部critical级审计问题,使审计能够完整运行并生成L7b报告

1. 扫描全部3个目录,找出所有缺失`tools`字段的SKILL.md文件
2. 为每个文件添加合适的`tools`字段(基于skill内容推断: read/write/exec/glob/grep等)
3. 扫描缺失`tags`字段的文件,添加合适的tags(基于skill类别和功能)
4. 修复autopilot-flow的MISSING_SLUG/MISSING_VERSION/MISSING_NAME
5. 重新运行`python deep_quality_audit.py --layer7b`确认0个critical issues
6. 确认L7b报告已更新且反映修复后的等级分布

**验证标准**:
- 审计exit code = 0
- 0个MISSING_TOOLS, 0个MISSING_TAGS, 0个MISSING_SLUG
- L7b报告grade_distribution中C+D < 100

### Task 2 (P0): ClawHub 300个剩余skill批量上传
**目标**: 在限流窗口重置后上传剩余300个skill

1. 检查ClawHub限流是否已重置(距上次上传>24h)
2. 运行`python clawhub_batch_uploader.py --resume --limit 200`
3. 如果仍有剩余,记录并在下一轮继续
4. 上传完成后同步`clawhub_published_slugs.json`和数据库

**验证标准**:
- ClawHub published count >= 730 (432+300-2重复)
- `clawhub_upload_results.json`中success列表更新

### Task 3 (P1): L7A全量去重
**目标**: 消除剩余1211个重复块对(788个文件)

1. 扩展`deduplicate_blocks.py`覆盖全部3个目录
2. 修复73个文件的重复章节标题(合并或重命名)
3. 处理表格分隔符重复(规范化分隔符格式)
4. 处理通用付费能力行重复(差异化描述)
5. 生成全量去重报告

**验证标准**:
- 全量扫描重复块对 < 100
- 重复章节标题文件数 = 0

### Task 4 (P1): L3定价再平衡
**目标**: 将L3占比从56.1%降到40%以下

1. 使用英文关键词或display_name字段进行LOW_VALUE检测
2. 对简单工具类skill(格式化、计数、排序等)降级为L1/L2
3. 对复杂AI类skill保持L3或升级为L4
4. 同步更新SKILL.md frontmatter和数据库

**验证标准**:
- L3占比 < 40%
- L1+L2占比 > 30%
- 0个'free' pricing_tier

### Task 5 (P2): 重新生成L7b报告并更新看板
**目标**: 获得修复后的准确L7b等级分布

1. 在Task 1修复critical issues后运行`python deep_quality_audit.py --layer7b`
2. 确认L7b报告反映修复后的状态
3. 验证看板L7b可视化正确显示新数据
4. 对比before/after等级分布

**验证标准**:
- L7b报告generated_at为当前时间
- A+B级占比 > 70%
- C+D级占比 < 30%

### Task 6 (P2): SkillHub pending_review跟踪 + 安全审核失败分析
**目标**: 跟踪7个pending_review状态,分析29个安全审核失败原因

1. 查询SkillHub API获取7个pending_review的最新状态
2. 如有approved的skill,执行对外发布流程
3. 分析29个安全审核失败的skill,提取失败原因
4. 制定避免安全审核失败的规则清单
5. 对可修复的失败skill进行内容修正后重新提交

**验证标准**:
- 7个pending_review状态已更新
- 29个安全审核失败原因已分析
- 可修复的失败skill已重新提交

## 执行规则
1. 遵循`修复提示词.md`的R1-R78规则
2. 每个任务完成后进行代码级验证(非文档声明)
3. 禁止任何形式的mock/fallback/todo/pass
4. 修复必须覆盖全部3个目录(packaged-skills/skillhub, opensource-skills/packaged, differentiated-skills)
5. 完成后生成下一轮提示词v37.0
