# 前4轮复核报告 + 第5轮提示词

> 基于实际代码逐行验证，非文档承诺
> 复核日期：2026-07-25

---

## 一、前4轮真实完成情况复核

### 第1轮 P0-1~P0-3 关键管道断裂修复 — ✅ 全部已验证

| 编号 | 验证方法 | 代码事实 | 结论 |
|------|---------|---------|------|
| P0-1 | 读取 `daily_sync.py:121` | `run_script("clawhub_batch_uploader.py", ["--dry-run"] if CLAWHUB_DRY_RUN else [])`，`CLAWHUB_DRY_RUN=False` 在 `project_config.py:59` | ✅ 已修复 |
| P0-2 | 读取 `update_mechanism.py:683-719` | `upload_paid_via_api` 调用 `from enterprise_uploader import upload_skill`，`payload_path.write_text()` 落盘备份，失败时才返回 `payload_ready` | ✅ 已修复 |
| P0-3 | 读取 `db.py:66-70` | skills表CREATE TABLE含 `suggested_price REAL, pricing_category TEXT, pricing_rationale TEXT, pricing_tier TEXT, is_paid INTEGER DEFAULT 0` | ✅ 已修复 |

### 第2轮 Q1-Q5 质量门控有效性修复 — ✅ 全部已验证

| 编号 | 验证方法 | 代码事实 | 结论 |
|------|---------|---------|------|
| Q1 | 读取 `rules.py:11-13` | `from project_config import MIN_DESCRIPTION_LEN, MAX_DESCRIPTION_LEN`，值为150-280 | ✅ 已修复 |
| Q2 | 读取 `rules.py:32-49` | PLACEHOLDER_PATTERNS含16条模式，含 `待填充/TBD/xxx/HACK/[PLACEHOLDER]` | ✅ 已修复 |
| Q3 | 读取 `rules.py:45-47` | 模板占位符正则为 `能力\d+[::]` / `场景\d+[::]` / `步骤\d+[::]`，支持任意数字 | ✅ 已修复 |
| Q4 | 读取 `rules.py:54-59` | EXAGGERATION_WORDS含16个词，含 `终极/完美/第一/顶级/极致/最好` | ✅ 已修复 |
| Q5 | 读取 `quality_gate.py:76` | `passed = len(issues) == 0`（HIGH+medium都判fail） | ✅ 已修复 |

### 第3轮 D1-D3 数据库追踪链路修复 — ✅ 全部已验证

| 编号 | 验证方法 | 代码事实/DB实测 | 结论 |
|------|---------|----------------|------|
| D1 | 读取 `multi_source_discover.py:217-231` + DB查询 | record_source_to_db查询skills表4层匹配(source_slug→slug→-free→-pro)写入skill_id | ✅ 已修复 |
| D2 | 读取 `project_config.py:166` + 全文件扫描 | `get_db_connection()` 含 `PRAGMA foreign_keys = ON`；20个额外文件也已补全，共52/52连接 | ✅ 已修复 |
| D3 | 读取 `db.py:203-215` + DB查询 | sources表有 `skill_id INTEGER` + FK约束 + ALTER迁移 + 索引；DB实测: JOIN=469, sources总4587, 已关联469 | ✅ 已修复 |

### 第4轮 D4-D6 DB写入收口与历史保护 — ✅ 全部已验证

| 编号 | 验证方法 | 代码事实/DB实测 | 结论 |
|------|---------|----------------|------|
| D4 | grep统计 | 59处裸SQL(14处在db.py业务函数层，45处在其他18个文件)；D5+D6已修复3个文件 | ⚠️ 部分完成（剩余15个文件待分批处理） |
| D5 | 读取3个文件 + DB查询 | `agent_trial.py:389` DELETE→`UPDATE scores SET is_current=0`；INSERT含`is_current=1`；`batch_l2_eval.py:148` DELETE→UPDATE；`trace_llm_scorer.py:371-381` UPDATE-in-place→UPDATE is_current=0+INSERT is_current=1；DB实测: scores表有is_current列, 3个skill有多条评分记录(如skill_id=1有3条trace_llm) | ✅ 已修复 |
| D6 | 读取 `update_mechanism.py:30,226-229,771-913` | `from db import record_upload as db_record_upload`；原record_upload函数已删除；7处调用改为`db_record_upload`+`error_message=` | ✅ 已修复 |

### 复核结论

- 前4轮共14项修复（P0×3 + Q×5 + D×6），13项已完全验证，1项部分完成（D4剩余15个文件裸SQL待后续分批处理）
- 所有修改均基于实际代码确认，无虚假实现
- 3个验证skill(ad-creative-intel-free/agentvibes-skill-free/agent-assistant-free)质量门结果跨轮一致，无回归

---

## 二、第5轮提示词（A1-A3 生成质量与运维闭环）

```
任务: 修复3处架构与运维闭环问题（A1-A3）

背景: 生成模块名不副实(llm_generated标记无LLM调用)，运维闭环实为报告生成器(检测不修复)，
trace_llm_scorer完全独立于skill_core(第三套检查实现)。

前序复核确认:
- 第1-4轮14项修复已全部验证通过（D4裸SQL部分完成不影响本轮）
- skill_core已包含parser.py(parse_frontmatter返回dict含raw/fields/body)和rules.py(EXAGGERATION_WORDS含16词)
- generate_skill.py第1051行llm_generated初始为False，第1103行设为True(实际无LLM调用)
- ops闭环.py第173-255行generate_ops_report()收集issues后只写report，不触发修复
- trace_llm_scorer.py第186-244行static_check()自行解析frontmatter+硬编码夸大词列表(10个，与rules.py的16个不一致)

执行步骤(小规模, 3个skill验证):

【A1】修复 generate_skill.py llm_generated标记名不副实
1. 读取 generate_skill.py 第1051行，确认: 'llm_generated': False
2. 读取 generate_skill.py 第1102-1103行，确认:
   - 第1102行: else: (所有placeholder已填充的分支)
   - 第1103行: result['llm_generated'] = True
   问题: generate_from_template是纯模板规则填充，未调用任何LLM API，但llm_generated=True名不副实
3. 修改 generate_skill.py:
   a. 第1103行: 删除 result['llm_generated'] = True
   b. 在删除位置增加: result['all_placeholders_filled'] = True
      （诚实标记: 所有placeholder已通过模板规则填充完成，但非LLM生成）
   c. 在第1052行(result初始化)增加: 'all_placeholders_filled': False,
   d. 搜索所有引用 result['llm_generated'] 的位置(grep "llm_generated" generate_skill.py)
      确认无其他地方设为True，如有则一并删除
4. 验证:
   a. python -m py_compile generate_skill.py
   b. grep "llm_generated" generate_skill.py → 应仅在初始化处为False，无设为True的地方
   c. grep "all_placeholders_filled" generate_skill.py → 应有初始化(False)和设为True两处

【A2】修复 ops闭环.py 检测不修复的开环问题
1. 读取 ops闭环.py 第234-255行，确认 generate_ops_report() 函数:
   - 第234行: report = { ... }
   - 第237行: 'issues': issues,
   - 第255行: return report
   问题: 检测到issues后只写入report，不触发任何修复动作
2. 读取 ops闭环.py 第258-321行，确认:
   - print_terminal_report(report): 输出报告到终端
   - main(): 调用generate_ops_report()后输出
3. 修改 ops闭环.py generate_ops_report()函数:
   a. 在第253行(return report之前)增加修复建议逻辑:
      ```python
      # A2修复: 检测到问题后生成修复建议，闭合运维环
      fix_actions = []
      for issue in issues:
          if 'L1覆盖率不足' in issue:
              fix_actions.append({
                  'action': 'run_l1_quality_gate',
                  'script': 'python quality_gate.py --batch',
                  'reason': issue
              })
          elif 'L2 A级比例不足' in issue:
              fix_actions.append({
                  'action': 'run_l2_evaluation',
                  'script': 'python batch_l2_eval.py --only-unevaluated',
                  'reason': issue
              })
          elif '低分skill' in issue:
              fix_actions.append({
                  'action': 'annotate_low_scores',
                  'script': 'python trace_llm_scorer.py annotate',
                  'reason': issue
              })
          elif 'L3覆盖率不足' in issue:
              fix_actions.append({
                  'action': 'run_l3_trial',
                  'script': 'python agent_trial.py batch --limit 5',
                  'reason': issue
              })
          elif '健康检查' in issue:
              fix_actions.append({
                  'action': 'run_health_check_detail',
                  'script': 'python health_check.py --json',
                  'reason': issue
              })

      report['fix_actions'] = fix_actions
      report['has_fix_actions'] = len(fix_actions) > 0
      ```
   b. 修改 print_terminal_report()函数(在第297行 print(f"\n{'='*70}") 之前)增加:
      ```python
      # A2修复: 输出修复建议
      fix_actions = report.get('fix_actions', [])
      if fix_actions:
          print(f"\n--- 修复建议 ({len(fix_actions)}个) ---")
          for i, fa in enumerate(fix_actions, 1):
              print(f"  [{i}] {fa['action']}")
              print(f"      原因: {fa['reason']}")
              print(f"      命令: {fa['script']}")
      ```
   c. 修改 main()函数(在第312行 print_terminal_report(report) 之后)增加:
      ```python
      # A2修复: 如果有修复建议，输出执行提示
      if report.get('has_fix_actions'):
          print(f"\n⚠ 检测到{len(report['fix_actions'])}个问题，建议执行上述修复脚本")
          print(f"  复制命令执行后，重新运行 python ops闭环.py 验证修复效果")
      ```
4. 验证:
   a. python -m py_compile ops闭环.py
   b. python ops闭环.py --json 2>&1 | python -c "import sys,json; r=json.load(sys.stdin); print('fix_actions数:', len(r.get('fix_actions',[]))); print('has_fix_actions:', r.get('has_fix_actions'))"
   c. 确认输出包含fix_actions列表和has_fix_actions=True（如果有问题）

【A3】修复 trace_llm_scorer.py 独立于skill_core的第三套检查实现
1. 读取 trace_llm_scorer.py 第186-244行，确认static_check()中重复实现:
   - 第186-193行: 自行解析frontmatter (re.split方式，与skill_core/parser.py重复)
   - 第212-223行: 自行检查硬编码凭证 (3个pattern)
   - 第225-234行: 自行检查保留词 (硬编码4个词: claude/anthropic/openai/chatgpt)
   - 第236-244行: 自行检查夸大词 (硬编码10个词，与rules.py的16个不一致)
2. 读取 skill_core/parser.py 第12-50行，确认:
   - parse_frontmatter(content)返回 dict: {'raw': str, 'fields': dict, 'body': str}
   - 注意: 返回值是dict不是tuple，与trace_llm_scorer当前解析方式不同
3. 读取 skill_core/rules.py 第54-59行，确认:
   - EXAGGERATION_WORDS含16个词(比trace_llm_scorer的10个多6个: 最完美/最专业/全球首发/业界第一/独一无二/绝无仅有)
4. 修改 trace_llm_scorer.py:
   a. 在文件头部导入区(第40行 from config import... 之后)增加:
      ```python
      # A3修复: 从skill_core导入共享解析和规则，消除第三套检查实现
      from skill_core.parser import parse_frontmatter
      from skill_core.rules import EXAGGERATION_WORDS
      ```
   b. 修改 static_check() 函数第186-193行(frontmatter解析):
      原:
      ```python
      if skill_content.startswith('---'):
          parts = re.split(r'^---\s*$', skill_content, maxsplit=2, flags=re.MULTILINE)
          if len(parts) >= 3:
              fm = parts[1]
              body = parts[2]
              checks['has_frontmatter'] = True
              checks['frontmatter_valid'] = True
      ```
      改:
      ```python
      # A3修复: 使用skill_core.parse_frontmatter替代自行解析
      parsed = parse_frontmatter(skill_content)
      if parsed['raw']:
          fm = parsed['raw']
          body = parsed['body']
          checks['has_frontmatter'] = True
          checks['frontmatter_valid'] = True
      ```
   c. 修改第225-234行(保留词检查)和第236-244行(夸大词检查):
      将第240行硬编码的夸大词列表:
      ```python
      for word in ['万能', '超级', '最强', '最好', '最佳', '终极', '完美', '第一', '顶级', '极致']:
      ```
      改为使用skill_core的统一列表:
      ```python
      # A3修复: 使用skill_core.rules.EXAGGERATION_WORDS替代硬编码(消除16词vs10词不一致)
      for word in EXAGGERATION_WORDS:
      ```
   d. 保留static_check中TRACE特有的检查项(has_core_capability/has_use_cases等第251-261行)，
      这些是TRACE评分特有逻辑，不需要迁移
   e. 注意: parse_frontmatter返回的fm是原始frontmatter文本(str)，与原代码parts[1]类型一致，
      后续的re.search检查逻辑无需修改
5. 验证:
   a. python -m py_compile trace_llm_scorer.py
   b. python -c "import sys; sys.path.insert(0,'.'); sys.path.insert(0,'../config'); from trace_llm_scorer import static_check; r=static_check('---\ndisplayName: test\nsummary: 最强工具\n---\n# test\n核心能力'); print('has_frontmatter:', r['has_frontmatter']); print('has_exaggeration:', r['has_exaggeration']); print('issues:', r['issues'])"
      确认: has_frontmatter=True, has_exaggeration=True(因"最强"在EXAGGERATION_WORDS中)
   c. python batch_l2_eval.py --limit 1 --dry-run 2>&1 确认无报错

验收标准:
- generate_skill.py的llm_generated标记不再被设为True(因无LLM调用)
- 新增all_placeholders_filled标记诚实反映模板填充状态
- ops闭环.py检测到问题后输出fix_actions修复建议列表(含action/reason/script)
- ops闭环.py终端输出包含"修复建议"区块
- trace_llm_scorer.py的static_check使用skill_core.parse_frontmatter替代自行解析
- trace_llm_scorer.py的夸大词检查使用skill_core.rules.EXAGGERATION_WORDS(16词)替代硬编码(10词)
- 3个skill(ad-creative-intel-free/agentvibes-skill-free/agent-assistant-free)质量门验证无回归
- batch_l2_eval.py --limit 1 --dry-run无报错
- 不引入新bug，不改变现有行为（除修复的3处外）

约束:
- 禁止 mock/TODO/pass/fallback
- 每步修改后立即语法检查 python -m py_compile
- A1不删除llm_generated字段(保持兼容)，只改变其语义(不再设为True)
- A2不自动执行修复脚本(只输出建议命令)，由用户/AI决定执行
- A3保留TRACE特有的检查项(has_core_capability/has_use_cases等)，仅迁移重复的通用检查
- A3注意parse_frontmatter返回dict{'raw','fields','body'}，不是tuple，需用parsed['raw']和parsed['body']
- 完成第5轮后，输出第6轮提示词（L1-L8 冗余文件清理）
```

---

## 三、第5轮涉及文件清单

| 任务 | 文件 | 修改类型 | 预计改动行数 |
|------|------|---------|------------|
| A1 | `generate_skill.py` | 标记修正 | ~5行 |
| A2 | `ops闭环.py` | 增加修复建议 | ~40行 |
| A3 | `trace_llm_scorer.py` | 导入skill_core | ~15行 |
| 验证 | 3个skill质量门回归 | 无修改 | 0 |

总计修改3个文件，预计~60行改动。
