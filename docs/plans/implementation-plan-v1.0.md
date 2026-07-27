# 实施计划 v1.0

> 日期: 2026-07-27
> 关联: 2026-07-27-quality-governance-finance-skills-design.md, task-list-v1.0.md
> 原则: 严禁补丁式修复、碎片化功能、冗余化已有主线和功能模块

## 前置必读

执行任何步骤前，必须阅读以下文档：
1. `docs/specs/2026-07-27-quality-governance-finance-skills-design.md` — 设计方案
2. `docs/plans/task-list-v1.0.md` — 任务清单（51子任务）
3. `docs/deep-differentiation-methodology.md` — 深度差异化方法论
4. `docs/NAMING_CONVENTION.md` — 命名规范

## 执行顺序

```
第一批: T1-001~T1-004 (构建评分器) — 阻塞后续所有任务
第二批: T2-001~T2-004 ∥ T2-005~T2-007 (采集+定价) — 与T1-005~T1-007并行
第三批: T1-008~T1-012 ∥ T2-008~T2-011 (重做+生产) — 并行
第四批: T1-013~T1-015 ∥ T2-012~T2-014 ∥ T3-001~T3-002 (上传+质检+同步) — 并行
第五批: T1-016~T1-018 ∥ T2-015~T2-016 ∥ T3-003~T3-004 (治理+上传+识别) — 并行
第六批: T2-017~T2-018 ∥ T3-005~T3-007 (跟踪+升级) — 并行
第七批: T1-019~T1-021 ∥ T2-019~T2-020 ∥ T3-008~T3-010 (校准+验证+循环) — 并行
```

---

## 第一批：构建本地评分器（T1-001 ~ T1-004）

### T1-001: 编写 local_quality_scorer.py

**目标**: 创建5维度LLM质量评分器

**文件**: `tools/local_quality_scorer.py`（新增）

**核心结构**:
```python
#!/usr/bin/env python3
"""本地LLM质量评分器 — 5维度评测SKILL.md质量，产出0-5分"""

import json, os, sys, re
from pathlib import Path

# 配置加载
CONFIG_PATH = Path(__file__).parent.parent / "data" / "config" / "quality_scoring_config.json"

SCORE_DIMENSIONS = [
    {"key": "completeness", "name": "功能完整性", "weight": 1.0},
    {"key": "accuracy", "name": "准确性", "weight": 1.0},
    {"key": "usability", "name": "易用性", "weight": 1.0},
    {"key": "security", "name": "安全性", "weight": 1.0},
    {"key": "innovation", "name": "创新性", "weight": 1.0},
]

SCORE_THRESHOLD = 4.5  # 与quality_gate.py RATING_GATE_THRESHOLD一致

def score_skill(skill_md_path_or_content: str) -> dict:
    """对SKILL.md评分，返回{total_score, dimensions, feedback}"""
    # 1. 读取SKILL.md内容
    # 2. 构造评测prompt（5维度结构化评测）
    # 3. 调用LLM API（从config读取端点和key）
    # 4. 解析LLM返回的JSON结构{dimensions: {key: score, reason}, total, suggestions}
    # 5. 返回标准化结果
    pass

def _build_eval_prompt(skill_content: str) -> str:
    """构造5维度评测prompt"""
    pass

def _call_llm(prompt: str, config: dict) -> str:
    """调用LLM API"""
    pass

def _parse_llm_response(response: str) -> dict:
    """解析LLM返回为标准结构"""
    pass

if __name__ == "__main__":
    # CLI: python local_quality_scorer.py <skill_dir_or_md_path>
    # 输出JSON: {total_score, dimensions, feedback, passed}
    pass
```

**关键实现要点**:
- LLM调用使用 `data/config/quality_scoring_config.json` 中的端点配置
- 评测prompt要求LLM返回严格JSON格式，每维度0.0-1.0分+文字理由+改进建议
- 总分 = 5个维度分数之和（0.0-5.0）
- `passed = total_score >= 4.5`
- 支持单文件路径和目录路径输入（目录时自动查找SKILL.md）
- 错误处理：LLM调用失败时返回 `{total_score: 0.0, error: "..."}`，不阻断流程（由上层判断）

**验证**: 对3个已知skill评分
- 已知好skill（如平台评分≥4.5的）→ 本地评分应≥4.0
- 已知坏skill（如已删除的university-applications-sk 3.3分）→ 本地评分应≤3.5
- 中等skill → 本地评分在3.5-4.5之间

### T1-002: 编写评分器配置

**文件**: `data/config/quality_scoring_config.json`（新增）

```json
{
  "llm": {
    "api_endpoint": "",
    "api_key": "",
    "model": "",
    "max_tokens": 2000,
    "temperature": 0.3
  },
  "dimensions": [
    {"key": "completeness", "name": "功能完整性", "weight": 1.0, "description": "核心功能描述完整性、输入输出格式清晰度、使用场景充分性"},
    {"key": "accuracy", "name": "准确性", "weight": 1.0, "description": "技术描述正确性、依赖说明准确性、无错误/误导信息"},
    {"key": "usability", "name": "易用性", "weight": 1.0, "description": "结构清晰度、示例充分性、frontmatter规范性、用户上手难度"},
    {"key": "security", "name": "安全性", "weight": 1.0, "description": "无安全风险模式、依赖说明透明、无敏感信息泄露"},
    {"key": "innovation", "name": "创新性", "weight": 1.0, "description": "差异化亮点、独特价值、非简单复制"}
  ],
  "threshold": 4.5,
  "prompt_template": "你是一个SKILL质量评测专家..."
}
```

**验证**: `python tools/local_quality_scorer.py --config data/config/quality_scoring_config.json --test` 输出配置加载成功

### T1-003: 扩展 quality_gate.py

**文件**: `tools/quality_gate.py`（修改）

**修改点**:

1. `run_full_quality_check()` 函数签名扩展:
```python
# 现有签名
def run_full_quality_check(skill_md, include_l2l3=False):
# 扩展为
def run_full_quality_check(skill_md, include_l2l3=False, include_local_score=True):
```

2. 在函数体内，5层检查之后新增本地评分:
```python
# 在防幻觉检查之后，汇总之前
if include_local_score:
    local_result = run_local_scoring(skill_md)
    result['local_score'] = local_result.get('total_score', 0.0)
    result['local_score_feedback'] = local_result.get('feedback', '')
    result['local_score_dimensions'] = local_result.get('dimensions', {})
    if result['local_score'] < 4.5:
        result['overall_passed'] = False
        # 添加到失败检查项
        result['checks'].append({
            'layer': 'local_score',
            'name': '本地LLM质量评分',
            'passed': False,
            'severity': 'high',
            'message': f"本地评分 {result['local_score']:.1f} < 4.5, 需改进: {result['local_score_feedback']}"
        })
```

3. 新增子函数:
```python
def run_local_scoring(skill_md):
    """调用local_quality_scorer对SKILL.md评分"""
    try:
        from local_quality_scorer import score_skill
        return score_skill(skill_md)
    except ImportError:
        return {'total_score': 0.0, 'feedback': 'local_quality_scorer未安装', 'dimensions': {}}
    except Exception as e:
        return {'total_score': 0.0, 'feedback': f'评分异常: {e}', 'dimensions': {}}
```

**约束**: 不改动现有5层46项检查的任何逻辑，仅在汇总阶段追加local_score

**验证**: 
```python
from quality_gate import run_full_quality_check
result = run_full_quality_check(skill_md_content, include_local_score=True)
assert 'local_score' in result
assert 'local_score_feedback' in result
```

### T1-004: DB schema更新 + 评分器验证

**DB修改**:
```sql
ALTER TABLE skills ADD COLUMN local_quality_score REAL DEFAULT 0.0;
ALTER TABLE skills ADD COLUMN local_score_feedback TEXT DEFAULT '';
ALTER TABLE skills ADD COLUMN local_score_at TEXT DEFAULT '';
```

通过 `tools/db.py` 的 `_ensure_columns()` 幂等添加（现有模式）。

**验证步骤**:
1. 从DB查询已知平台评分的2个skill（university-applications-sk 3.3分、word-docx-sk 3.6分）
2. 对它们的SKILL.md执行本地评分
3. 对比偏差：`abs(local_score - platform_rating) <= 0.5`
4. 选取3个已知高质量skill（平台synced且无低分标记的）验证评分≥4.0

**产出**: `data/reports/local_scorer_validation.json` — 含验证结果

---

## 第二批：全量扫描 + 多源采集 + 定价升级（并行）

### T1-005~T1-007: 全量存量扫描

**T1-005: 批量扫描脚本**

不新建文件，在 `tools/quality_gate.py` 中新增 `batch_scan_all_skills()` 函数:
```python
def batch_scan_all_skills(directories=None, include_local_score=True):
    """批量扫描所有存量skill，执行run_full_quality_check"""
    if directories is None:
        directories = [
            'packaged-skills/skillhub',
            'opensource-skills/packaged',
            'enterprise-upload'
        ]
    # 遍历每个目录下的子目录，对每个SKILL.md执行完整质检
    # 结果写入DB local_quality_score字段
    # 返回汇总统计
```

CLI入口: `python tools/quality_gate.py --batch-scan`

**T1-006: 执行全量扫描**
```bash
cd d:\skills
python tools/quality_gate.py --batch-scan 2>&1 | tee data/reports/batch_scan_log.txt
```
预计耗时：1046个skill × ~3秒/个 ≈ 52分钟（LLM调用为主要瓶颈）

**T1-007: 生成评分报告**
```bash
python -c "
import sqlite3, json
conn = sqlite3.connect('skill-registry.db')
rows = conn.execute('SELECT slug, local_quality_score, local_score_feedback FROM skills WHERE local_quality_score > 0').fetchall()
report = {'total': len(rows), 'skills': [{'slug': r[0], 'score': r[1], 'feedback': r[2]} for r in rows]}
json.dump(report, open('data/reports/local_quality_scan.json', 'w'), ensure_ascii=False, indent=2)
print(f'报告生成: {len(rows)}个skill已评分')
"
```

### T2-001~T2-004: 多源采集20个金融技能

**T2-001: ClawHub Finance筛选**

读取 `clawhub-skills/downloaded/Finance/` 下12个技能的SKILL.md，评估质量，筛选8-10个:
```bash
# 列出Finance目录下所有技能
ls clawhub-skills/downloaded/Finance/
# 对每个技能读取SKILL.md，评估功能完整性和差异化潜力
```

**T2-002: GitHub扫描**
```bash
cd d:\skills
python tools/github_scanner.py --keywords "quant,trading,stock,futures,crypto,a-stock,bitcoin,ethereum,technical-analysis,backtest" --min-stars 50 --limit 20
```

**T2-003: Web搜索补充**

使用WebSearch搜索:
- "AI agent stock trading skill 2026"
- "quantitative trading MCP tool"
- "crypto trading automation agent"
- "A股量化分析工具 AI"
- "期货交易策略自动化 skill"

使用defuddle提取页面内容，评估是否适合转化为skill。

**T2-004: 去重+初筛**

合并三个来源候选，去重（按功能相似度），筛选最终20个，输出:
```bash
python -c "
import json
candidates = {
    'clawhub': [...],  # T2-001结果
    'github': [...],   # T2-002结果
    'web': [...]       # T2-003结果
}
# 去重逻辑：按功能描述相似度聚类
# 筛选标准：功能独特性、技术可行性、差异化潜力
final = select_top_20(candidates)
json.dump(final, open('data/discovery/finance_candidates.json', 'w'), ensure_ascii=False, indent=2)
"
```

### T2-005~T2-007: 定价策略升级

**T2-005: 升级 pricing_engine.py**

修改 `tools/pricing_engine.py`:

1. `CATEGORY_BASE_PRICE` 新增金融类别:
```python
'finance': {
    'min': 19.9, 'max': 199.0, 'base': 29.9,
    'rationale': '金融领域高专业门槛、高风险、高价值，基础价高于数据分析类'
},
'quantitative_trading': {
    'min': 39.0, 'max': 199.0, 'base': 69.0,
    'rationale': '量化交易工具专业度极高，实盘信号/策略回测等具有直接经济价值'
},
'crypto': {
    'min': 19.9, 'max': 149.0, 'base': 29.9,
    'rationale': '加密货币工具市场大但竞争激烈，中档定价'
},
```

2. `PRICE_ANCHOR_POINTS` 扩展:
```python
# 现有
PRICE_ANCHOR_POINTS = [0.99, 1.9, 2.9, ..., 49.0, 69.0, 99.0]
# 扩展为
PRICE_ANCHOR_POINTS = [0.99, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9, 7.9, 8.9, 9.9, 12.0, 15.0, 19.0, 19.9, 25.0, 29.0, 39.0, 49.0, 59.0, 69.0, 79.0, 89.0, 99.0, 129.0, 149.0, 169.0, 199.0]
```

3. `MAX_PRICE` 更新:
```python
MAX_PRICE = 199.0  # 从99.0提升，支持企业级金融工具
```

4. `COMPLEXITY_FACTOR` 金融领域加成:
```python
# 在evaluate_complexity()中新增
if any(kw in description.lower() for kw in ['backtest', 'strategy', 'portfolio', 'risk', 'signal']):
    complexity_score += 1  # 金融复杂度额外加分
```

**T2-006: 升级 task3_pricing_calibration.py**

修改 `tools/task3_pricing_calibration.py`:

1. `score_value()` 新增金融高价值关键词:
```python
HIGH_VALUE_KEYWORDS.extend([
    'backtest', 'strategy', 'portfolio', 'risk_management', 'signal',
    'alpha', 'beta', 'sharpe', 'drawdown', 'position',
    'futures', 'options', 'margin', 'leverage',
    'blockchain', 'defi', 'liquidity', 'yield',
    'real_time', 'live_trading', 'execution',
])
```

2. L4价格映射提升:
```python
# 现有
L4_PRICE = {'price': 99.9, 'model': 'monthly'}
# 扩展为（金融L4）
L4_PRICE_FINANCE = {'price': 149.9, 'model': 'monthly'}
```

3. `simple_tool_penalty()` 排除金融类:
```python
# 金融类skill不适用简单工具惩罚
if category in ('finance', 'quantitative_trading', 'crypto'):
    return 0
```

**T2-007: 验证定价**

对5个金融skill示例执行定价:
```bash
python tools/pricing_engine.py price clawhub-skills/downloaded/Finance/stock-filter-skills
python tools/pricing_engine.py price clawhub-skills/downloaded/Finance/t-trading
python tools/pricing_engine.py price clawhub-skills/downloaded/Finance/finance-radar
python tools/pricing_engine.py price clawhub-skills/downloaded/Finance/okx-dex-token
python tools/pricing_engine.py price clawhub-skills/downloaded/Finance/finance-report-analyzer
```
验证: 定价在19.9-199元区间，L4级金融工具定价≥99元。

---

## 第三批：低分重做 + 差异化生产（并行）

### T1-008~T1-012: 低分打回重做

**T1-008: 筛选低分skill**
```bash
python -c "
import sqlite3, json
conn = sqlite3.connect('skill-registry.db')
rows = conn.execute('''
    SELECT slug, local_quality_score, local_score_feedback, local_path
    FROM skills
    WHERE local_quality_score > 0 AND local_quality_score <= 4.5
    ORDER BY local_quality_score ASC
''').fetchall()
print(f'低分skill数: {len(rows)}')
for r in rows:
    print(f'  {r[0]}: {r[1]}分 — {r[2][:80]}...')
"
```

**T1-009~T1-012: 批量升级**

对每个低分skill，根据5维度反馈执行整体性内容提升:
- 读取 `local_score_feedback` 和 `local_score_dimensions`
- 针对最弱维度（分数最低的1-2个维度）做实质性内容增强
- **严禁补丁式修改**: 不是简单改几个字，而是根据反馈重写相关章节
- 升级后重新执行 `run_full_quality_check(include_local_score=True)`
- 循环直到 `local_score > 4.5` 或达到3轮上限

升级原则:
- 功能完整性不足 → 补充核心功能描述、输入输出示例、使用场景
- 准确性不足 → 修正技术描述、补充依赖说明、核实信息准确性
- 易用性不足 → 优化文档结构、补充使用示例、改善frontmatter
- 安全性不足 → 修复安全风险、补充安全说明、清理敏感信息
- 创新性不足 → 增强差异化描述、突出独特价值、补充创新点

### T2-008~T2-011: 深度差异化生产

**T2-008: 执行auto_differentiate.py**
```bash
cd d:\skills
# 对finance_candidates.json中的20个源技能执行差异化
python tools/auto_differentiate.py --source-file data/discovery/finance_candidates.json --limit 20
```

**T2-009: 免费/收费分配**

分配决策标准:
- **仅付费版**（10个）: 量化策略/实盘信号/专业数据API/高频交易/回测引擎
  - 判定: 含"strategy/backtest/signal/execution/live"关键词
  - 判定: 技术方式简单（用户看prompt即可复现）
  - 判定: 直接经济价值（实盘交易信号）
- **免费版+付费版**（10个）: 基础概念/教育/新闻/入门分析/数据展示
  - 判定: 普及型功能（财经新闻/基础知识/概念解释）
  - 判定: 用户需要先体验才能判断价值

**T2-010: 生产免费版**

对10个普及型技能，基于付费版SKILL.md精简生产免费版:
- 移除高级功能（保留核心功能）
- license改为MIT
- 移除suggested_price
- slug添加 `-free` 后缀
- displayName添加"免费版"后缀

**T2-011: 应用定价**
```bash
# 对20个付费版执行定价
python tools/task3_pricing_calibration.py --filter finance --update-db --update-skill-md
```

---

## 第四批：上传 + 质检 + 评分同步（并行）

### T1-013~T1-015: 上传SkillHub并跟踪

**T1-013: 批量上传**
```bash
# 上传通过质检的skill到SkillHub
# 使用现有 upload-packaged.ps1 或逐个 skillhub publish
cd d:\skills
.\tools\scripts\upload-packaged.ps1 --skillhub-only
```

**T1-014: 评分同步**
```bash
python tools/market_monitor.py sync-ratings --limit 200
# 重复执行直到覆盖率≥80%
```

**T1-015: 生成报告**
```bash
python tools/market_monitor.py report --output data/reports/upload_tracking_report.json
```

### T2-012~T2-014: 三层质检+打回重做

**T2-012: 执行质检**
```bash
cd d:\skills
# 对30个新技能逐个执行完整质检
for /d %d in (packaged-skills\skillhub\*-finance-*) do python tools/quality_gate.py --check "%d\SKILL.md" --include-local-score
```

**T2-013: 低分重做**

对local_score ≤ 4.5的skill根据反馈重做，循环直到 > 4.5。

**T2-014: DB更新**
```bash
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
# 更新30个金融skill的workflow_state为quality_passed
conn.execute(\"UPDATE skills SET workflow_state='quality_passed' WHERE slug LIKE '%-finance-%' AND local_quality_score > 4.5\")
conn.commit()
"
```

### T3-001~T3-002: 全量评分同步

**T3-001: 首批同步**
```bash
cd d:\skills
python tools/market_monitor.py sync-ratings --limit 200 2>&1 | tee data/reports/sync_ratings_batch1.txt
```

**T3-002: 循环同步**
```bash
# 重复执行直到覆盖率达80%
# 每次同步200个，预计需要9次（1768/200≈9）
for /L %i in (1,1,9) do python tools/market_monitor.py sync-ratings --limit 200
```
预计总耗时: 9 × ~30分钟 ≈ 4.5小时（可分多次执行）

---

## 第五批：平台治理 + 上传 + 识别（并行）

### T1-016~T1-018: 平台低分二次治理

**T1-016: 查询低分skill**
```bash
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
rows = conn.execute('''
    SELECT slug, platform_rating, local_quality_score
    FROM skills
    WHERE platform_rating > 0 AND platform_rating < 4.5
''').fetchall()
print(f'平台低分skill数: {len(rows)}')
for r in rows: print(f'  {r[0]}: platform={r[1]}, local={r[2]}')
"
```

**T1-017: 升级+重传**
```bash
# 对每个低分skill执行升级
python -c "
from tools.version_sync_pipeline import upgrade_single_skill
# 逐个升级低分skill
for slug in low_rating_slugs:
    upgrade_single_skill(slug)
"
```

**T1-018: 循环直到≥4.5**

### T2-015~T2-016: 全平台上传

**T2-015: SkillHub上传**
```bash
cd d:\skills
# 对30个金融skill逐个上传SkillHub
for %d in (finance_skill_dirs) do python tools/scripts/skillhub.ps1 publish "%d" --changelog "金融领域技能首发"
```

**T2-016: ClawHub + GitHub上传**
```bash
# ClawHub上传
python tools/clawhub_batch_uploader.py --from-db --limit 30 --filter finance
# GitHub同步
cd hermes-skills
git add . && git commit -m "feat: add 30 finance skills" && git push
```

### T3-003~T3-004: 低分识别

**T3-003: 查询全量低分**
```bash
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
rows = conn.execute('''
    SELECT slug, platform_rating, local_path
    FROM skills
    WHERE platform_rating > 0 AND platform_rating < 4.5
    ORDER BY platform_rating ASC
''').fetchall()
print(f'全量低分skill数: {len(rows)}')
"
```

**T3-004: 分类**
```bash
python -c "
import sqlite3, os
conn = sqlite3.connect('skill-registry.db')
rows = conn.execute('SELECT slug, local_path FROM skills WHERE platform_rating > 0 AND platform_rating < 4.5').fetchall()
has_local = [r for r in rows if r[1] and os.path.exists(r[1])]
no_local = [r for r in rows if not r[1] or not os.path.exists(r[1])]
print(f'本地有文件: {len(has_local)}, 本地无文件: {len(no_local)}')
"
```

---

## 第六批：评分跟踪 + 批量升级（并行）

### T2-017~T2-018: 平台评分跟踪

**T2-017: 等待+同步**
```bash
# 上传后等待24-48小时，然后同步评分
python tools/market_monitor.py sync-ratings --limit 30 --filter finance
```

**T2-018: 低分重做循环**

对平台评分<4.5的金融skill执行升级+重传，循环直到≥4.5。

### T3-005~T3-007: 批量升级

**T3-005: 本地有文件的升级**
```bash
# 对每个有本地文件的低分skill执行升级
python -c "
from tools.quality_gate import run_full_quality_check
from tools.version_sync_pipeline import upgrade_single_skill
# 逐个升级，使用include_local_score
"
```

**T3-006: 循环重做**

local_score ≤ 4.5的根据反馈重做，循环直到 > 4.5。

**T3-007: 无文件标记**
```bash
python -c "
import sqlite3
conn = sqlite3.connect('skill-registry.db')
conn.execute(\"UPDATE skills SET current_status='needs_rebuild' WHERE platform_rating > 0 AND platform_rating < 4.5 AND (local_path IS NULL OR local_path = '')\")
conn.commit()
"
```

---

## 第七批：校准 + 验证 + 循环（并行）

### T1-019~T1-021: 评分体系校准

**T1-019: 偏差分析**
```bash
python -c "
import sqlite3, json
conn = sqlite3.connect('skill-registry.db')
rows = conn.execute('''
    SELECT slug, local_quality_score, platform_rating
    FROM skills
    WHERE local_quality_score > 0 AND platform_rating > 0
''').fetchall()
# 计算偏差
diffs = [(r[0], r[1], r[2], abs(r[1]-r[2])) for r in rows]
avg_diff = sum(d[3] for d in diffs) / len(diffs)
consistent = sum(1 for d in diffs if d[3] <= 0.5)
print(f'对比skill数: {len(diffs)}')
print(f'平均偏差: {avg_diff:.2f}')
print(f'一致率(偏差≤0.5): {consistent}/{len(diffs)} ({consistent/len(diffs)*100:.1f}%)')
# 分析偏差模式
local_high = sum(1 for d in diffs if d[1] > d[2] + 0.5)  # 本地高平台低
local_low = sum(1 for d in diffs if d[1] < d[2] - 0.5)   # 本地低平台高
print(f'本地偏高: {local_high}, 本地偏低: {local_low}')
"
```

**T1-020: 校准评分器**

根据偏差分析调整:
- 如果本地偏高 → 收紧评分标准（prompt中提高要求）
- 如果本地偏低 → 放宽评分标准
- 调整维度权重（偏差大的维度降低权重或修改评测标准）

**T1-021: 升级建议报告**

产出 `data/reports/quality_system_upgrade_report.md`

### T2-019~T2-020: 流程验证总结

**T2-019: 全流程验证**

记录每阶段指标:
| 阶段 | 耗时 | 成功率 | 问题 |
|------|------|--------|------|
| 采集 | | | |
| 定价 | | | |
| 差异化 | | | |
| 质检 | | | |
| 上传 | | | |
| 跟踪 | | | |
| 重做 | | | |

**T2-020: 优化建议**

产出 `docs/plans/finance-pipeline-optimization.md`

### T3-008~T3-010: 重传+循环

**T3-008: 重传**
```bash
# 升级后的skill重传SkillHub
python -c "
from tools.version_sync_pipeline import sync_skill_to_all_platforms
# 逐个重传升级后的skill
"
```

**T3-009: 循环跟踪**

等待24-48小时 → sync-ratings → 仍<4.5的再次升级 → 循环。

**T3-010: 治理总结报告**

产出 `data/reports/platform_low_score_governance_report.md`

---

## 执行约束（适用于所有批次）

1. **严禁补丁式修复**: 每个低分skill根据5维度反馈做整体性内容提升
2. **严禁碎片化功能**: 仅新增 `local_quality_scorer.py` 和 `quality_scoring_config.json`，不创建其他新文件
3. **严禁冗余化**: 复用现有 `auto_differentiate.py`、`clawhub_batch_uploader.py`、`orchestrator.py`、`market_monitor.py`
4. **严禁mock/fallback/todo**: 所有功能必须真实实现，不使用模拟数据
5. **单向依赖**: `local_quality_scorer` → `quality_gate` → `upload_gate` → `orchestrator`
6. **DB一致性**: 所有评分数据写入 `skill-registry.db`，不创建新数据库
7. **向后兼容**: `run_full_quality_check(include_local_score=False)` 行为与现有完全一致
8. **Git提交**: 每完成一个阶段提交一次，commit message格式: `feat(stage-X-Y): 描述`
