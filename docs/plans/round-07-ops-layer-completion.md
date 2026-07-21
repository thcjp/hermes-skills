# Round 07: 运维层补全 (Phase 3)

> **前置条件**: Round 06 已完成（生成流水线端到端验证通过）
> **设计文档**: `D:\skills\docs\plans\2026-07-20-skill-automation-v2-design.md` 第3.4节
> **预估时间**: 30-45 分钟
> **验收标准**: health_check.py 输出健康报告 + 定时任务创建 + 文档冲突解决

---

## 背景与目标

Phase 1（验证层）和 Phase 2（生成层）已全部完成：
- L1 静态检查、L2 LLM 验证、L3 Agent 试用三层验证体系就绪
- 5种设计模式模板 + generate_skill.py 生成流水线就绪
- 3个测试 skill 验证通过（daily-report-writer / code-quality / auto-workflow）

Phase 3 聚焦运维层补全，解决设计文档第3.4节识别的问题：
1. **健康检查缺失** — 无 DB 完整性检查、无文件有效性检查、无平台状态监控
2. **定时任务缺失** — 来源更新检测、治理扫描、健康检查均需手动执行
3. **文档冲突未解决** — `deep-differentiation-methodology.md` 与 `NAMING_CONVENTION.md` 的 -pro 后缀矛盾

---

## 任务清单

### Step 3.1: 编写 health_check.py

**目标**: 一键输出 DB + 文件 + 平台健康报告

**文件**: `D:\skills\skill-registry\health_check.py`

**检查项设计**:

#### 1. DB 完整性检查
- `workflow_state` 覆盖率: 统计 active/deprecated/null 分布
- 孤儿记录数: local_path 指向不存在的文件
- 重复 slug: 同一 slug 有多条 active 记录
- TRACE 评分覆盖率: 有 trace_llm 评分的 skill 占比
- L1/L2 验证状态: 各 workflow_state 的数量分布

#### 2. 文件完整性检查
- local_path 有效性: 抽样检查 50 条记录的文件是否存在
- SKILL.md 存在性: packaged-skills/skillhub/ 下的 SKILL.md 是否齐全
- 文件行数合规: 抽样检查是否 ≤500 行
- frontmatter 完整性: 抽样检查 8 必需字段

#### 3. 平台状态检查
- 上传成功率: 从 upload_records 统计
- pending 审核数: 从 DB 统计待审核 skill
- 发布分布: free vs paid 数量

**CLI 接口**:
```bash
python health_check.py                    # 完整健康报告（终端输出）
python health_check.py --json             # JSON 格式输出
python health_check.py --section db       # 仅检查 DB
python health_check.py --section files    # 仅检查文件
python health_check.py --section platform # 仅检查平台
python health_check.py -o report.json     # 保存报告到文件
```

**输出格式**:
```json
{
  "checked_at": "2026-07-21T...",
  "overall_status": "healthy|warning|critical",
  "db_health": {
    "total_skills": 1909,
    "active": 1858,
    "deprecated": 51,
    "workflow_state_coverage": "97.2%",
    "orphan_records": 0,
    "duplicate_slugs": 0,
    "trace_score_coverage": "12.5%",
    "issues": []
  },
  "file_health": {
    "checked_count": 50,
    "valid_paths": 50,
    "invalid_paths": 0,
    "skill_md_exists": 50,
    "line_count_compliant": 50,
    "issues": []
  },
  "platform_health": {
    "upload_success_rate": "100%",
    "pending_review": 12,
    "free_count": 6,
    "paid_count": 6,
    "issues": []
  },
  "recommendations": []
}
```

**验收标准**:
- [ ] `python health_check.py` 能正常运行，输出完整报告
- [ ] DB 检查覆盖 workflow_state/orphan/duplicate/trace_score 4 项
- [ ] 文件检查抽样 ≥50 条，检查 path 存在性 + SKILL.md 存在性
- [ ] 平台检查覆盖上传成功率 + pending 审核
- [ ] overall_status 正确反映健康状态（healthy/warning/critical）

---

### Step 3.2: 创建定时任务

**目标**: 使用 Schedule 工具创建 3 个 cron 定时任务

**定时任务设计**:

| 任务名 | 频率 | 执行内容 | cron 表达式 |
|--------|------|---------|-------------|
| skill-source-update | 每日 09:00 | 运行 `update_mechanism.py check` 检测来源更新 | `0 9 * * *` |
| skill-governance-scan | 每周一 10:00 | 运行 `clean_naming.py --dry-run` 治理扫描 | `0 10 * * 1` |
| skill-health-check | 每周一 11:00 | 运行 `health_check.py -o report.json` 健康检查 | `0 11 * * 1` |

**实现方式**: 使用 `Schedule` 工具的 `create` action

**注意事项**:
- cron 任务的最小间隔为 10 分钟
- 每个任务的 `message` 字段需包含完整的执行指令（路径、参数、输出位置）
- 时区设置为 `Asia/Shanghai`
- 输出报告保存到 `D:\skills\skill-registry\health_reports\` 目录

**验收标准**:
- [ ] 3 个定时任务创建成功
- [ ] 每个任务的 message 包含完整执行指令
- [ ] cron 表达式正确（每日/每周）
- [ ] 时区设置为 Asia/Shanghai

---

### Step 3.3: 解决文档冲突

**目标**: 修正 `deep-differentiation-methodology.md` 的 -pro 后缀矛盾

**当前冲突**:
- `D:\skills\deep-differentiation-methodology.md` 第 57 行: "新slug命名：`[原意]-pro` 或 `[新概念]`"（建议用 -pro）
- `D:\skills\deep-differentiation-methodology.md` 第 67 行: "使用功能化命名，不使用`-pro`后缀的简单变体"（不建议用 -pro）
- `D:\skills\skill-registry\NAMING_CONVENTION.md` 第 108 行: "slug含`-free`/`-pro`后缀 | 1216条(64%) | 严重"（标记为严重问题）

**修复方案**:
1. 将 `D:\skills\deep-differentiation-methodology.md` 移动到 `D:\skills\skill-registry\deep-differentiation-methodology.md`
2. 修正第 57 行: 删除 "`[原意]-pro` 或" 部分，改为 "新slug命名：`[功能化新概念]`，不使用 -pro/-free 后缀"
3. 确保与 NAMING_CONVENTION.md 一致: -pro/-free 后缀是严重问题，应合并为逻辑 skill

**验收标准**:
- [ ] deep-differentiation-methodology.md 移入 skill-registry/ 目录
- [ ] 第 57 行 -pro 建议已删除
- [ ] 与 NAMING_CONVENTION.md 无矛盾
- [ ] 文档内容其余部分不受影响

---

## 执行顺序

1. **Step 3.1** → 编写 health_check.py（15-20 分钟）
2. **Step 3.2** → 创建 3 个定时任务（5-10 分钟）
3. **Step 3.3** → 解决文档冲突（5 分钟）
4. **汇总** → 运行 health_check.py 验证，确认 Phase 3 验收标准
5. **生成 Round 08 提示词** → Phase 4（定稿与全面升级）

---

## Round 06 完成总结

### 已完成成果

| 项目 | 状态 | 详情 |
|------|------|------|
| generate_skill.py | ✅ 完成 | ~700行，模板选择+内容生成+L1+dep+L2 集成 |
| daily-report-writer 测试 | ✅ 通过 | L1 10/10, L2 47/50 (A级) |
| code-quality 测试 | ✅ 通过 | L1 10/10, L2 38/50 (B级, ≥35) |
| auto-workflow 测试 | ✅ 通过 | L1 10/10, L2 35/50 (B级, ≥35) |

### 修复的 Bug

| Bug | 根因 | 修复方案 |
|-----|------|---------|
| L1 未检测 `{{占位符}}` | rules.py PLACEHOLDER_PATTERNS 缺少 `{{...}}` 正则 | 添加 `(r'\{\{[a-zA-Z_][a-zA-Z0-9_]*\}\}', '占位符-未填充模板变量')` |
| 章节替换不完整 | HTML 注释在章节替换之后删除，正则被 `<!-- ` 截断 | 调整顺序: 先删 HTML 注释，再做章节替换；正则改为 `\n## \|\Z` |
| 占位符未填充 | generate_from_template 只替换整章节，不填充单个 `{{占位符}}` | 新增 `fill_common_placeholders()` + `fill_remaining_placeholders()` 两层填充 |

### 遗留问题

1. **TRACE_PASS_THRESHOLD 不一致**: 计划文档要求 L2 ≥35，但 config.py 中 `TRACE_PASS_THRESHOLD=42`。rule-based 生成质量为 B 级（35-44），达不到 42 阈值。建议: Phase 4 定稿时统一阈值，或调整生成策略加入 LLM 辅助填充
2. **生成内容偏通用**: `fill_remaining_placeholders()` 使用智能默认值填充，但部分默认值（如 "按流程执行"、"建议优化"）仍偏通用。后续可考虑: 在 L2 评估后，由 AI agent 手动优化低分章节
3. **依赖验证误报**: "无需额外API" 和 "除内容中明确标注的外部API" 被 dependency_verifier 误识别为中文 API 服务名。建议: 在 GENERIC_DESCRIPTIONS 列表中添加这些短语

---

## Phase 2 验收清单

- [x] 5种设计模式模板创建完成（Round 05）
- [x] 用模板生成的skill通过L1+L2验证（Round 05-06，3个skill）
- [x] 生成流水线端到端跑通（Round 06，generate_skill.py）
- [x] L1 占位符检测修复（Round 06，rules.py）
- [x] 模板填充增强（Round 06，fill_common + fill_remaining）

## Phase 3 验收清单（待完成）

- [ ] health_check.py输出健康报告
- [ ] 定时任务创建并触发
- [ ] 文档冲突解决
