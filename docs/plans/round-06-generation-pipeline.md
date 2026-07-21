# Round 06: 生成流水线集成与端到端验证

> **阶段**: Phase 2 - 生成层补全 (Step 2.3 + 2.4)
> **前序**: Round 05 已完成 5 种设计模式模板创建 + 1 个 Generator 模式 skill 验证(L1 10/10, L2 47/50 A级)
> **目标**: 将模板选择+内容生成+L1检查+依赖验证+L2验证集成为统一流水线, 并用 2 个不同模式的 skill 端到端验证

---

## 背景与上下文

### Round 05 完成情况

| 任务 | 状态 | 结果 |
|------|------|------|
| 创建 templates/ 目录 + README.md | ✓ 完成 | 6 个文件 |
| 创建 5 种设计模式模板 | ✓ 完成 | 每个含 8 标准章节+写作指引+质量检查点 |
| 用 Generator 模板生成 daily-report-writer | ✓ 完成 | 201 行, L1 10/10, L2 47/50 A级 |
| 模板化效率验证 | ✓ 完成 | 效率提升 3 倍, 质量提升 22 分(D→A) |
| 模板修复(slug字段+占位符前缀) | ✓ 完成 | 5 个模板均已修复 |

### 当前生成流程（手动）

```
人工选模板 → AI填充占位符 → 人工运行L1 → 人工运行依赖验证 → 人工运行L2 → 人工导入结果
```

**问题**: 每步都需要人工介入, 无法批量自动化。

### 目标生成流程（自动化）

```
输入slug → 自动选模板 → AI填充 → 自动L1 → 自动依赖验证 → 自动L2 → 汇总报告
```

---

## Step 2.3: 创建生成流水线脚本

### 任务: 创建 `d:\skills\skill-registry\generate_skill.py`

**功能**: 将模板选择+内容生成+L1检查+依赖验证+L2验证集成为统一流水线。

**CLI 接口**:
```bash
# 从已有skill生成改进版(读取原始SKILL.md, 用模板重新生成)
python generate_skill.py from-existing <slug> [--template <template_name>] [--skip-l2] [--skip-dep-verify]

# 从发现候选创建全新skill
python generate_skill.py from-candidate <slug> --template <template_name> --description <desc>

# 批量生成(从DB中选取未上传的skill)
python generate_skill.py batch --category <category> --limit <n> [--template <template_name>]
```

**核心函数**:

```python
def select_template(skill_content: str, skill_category: str) -> str:
    """
    根据skill内容自动选择最匹配的模板。
    
    选择逻辑:
    - 内容含"审查/评估/检查/打分" → reviewer_template
    - 内容含"生成/创作/输出/模板" → generator_template  
    - 内容含"多步骤/流程/流水线/管道" → pipeline_template
    - 内容含"反推/还原/逆向/解密" → inversion_template
    - 默认 → tool_wrapper_template
    """

def generate_from_template(template_name: str, skill_data: dict) -> str:
    """
    读取模板, 用skill_data填充占位符, 生成完整SKILL.md内容。
    
    参数:
    - template_name: 模板名称(不含.md)
    - skill_data: 包含slug/displayName/summary/description等字段的dict
    
    返回: 完整的SKILL.md内容字符串
    """

def run_generation_pipeline(slug: str, template_name: str = None, 
                            skip_l2: bool = False, 
                            skip_dep_verify: bool = False) -> dict:
    """
    执行完整生成流水线:
    1. 读取原始skill(如果有)或创建新skill
    2. 选择模板(自动或手动指定)
    3. 生成SKILL.md内容
    4. 保存到 packaged-skills/skillhub/{slug}/SKILL.md
    5. 运行L1静态检查(quality_gate.py)
    6. 运行依赖验证(dependency_verifier.py) - 如不skip
    7. 运行L2 LLM验证(llm_validator.py) - 如不skip
    8. 汇总结果
    
    返回: {
        'slug': slug,
        'template_used': template_name,
        'l1_result': {...},
        'dep_verify_result': {...},
        'l2_result': {...},
        'overall_passed': True/False,
        'output_path': '...'
    }
    """
```

**实现要点**:

1. **模板选择逻辑** (select_template):
   - 读取原始SKILL.md内容
   - 按关键词匹配选择模板
   - 支持手动指定 `--template` 参数覆盖自动选择

2. **内容生成** (generate_from_template):
   - 读取模板文件
   - 识别 `{{占位符}}` 
   - AI填充占位符(调用LLM或使用规则填充)
   - 删除 `<!-- 写作指引 -->` 和 `<!-- 质量检查点 -->` 注释
   - 返回完整SKILL.md内容

3. **流水线编排** (run_generation_pipeline):
   - 串联 L1 → dep_verify → L2
   - 每步失败时记录原因并决定是否继续
   - L1失败 → 阻塞, 不继续
   - dep_verify失败 → 警告但继续(标记manual_review)
   - L2失败 → 记录但不阻塞(返回结果供人工审阅)

4. **结果汇总**:
   - 输出JSON格式的完整报告
   - 保存到 `skill-registry/generation_report_{slug}.json`

### 文件依赖

| 文件 | 用途 | 状态 |
|------|------|------|
| `templates/*.md` | 5种设计模式模板 | Round 05 已创建 |
| `quality_gate.py` | L1静态检查 | 已有 |
| `dependency_verifier.py` | 依赖验证 | Round 02 已创建 |
| `llm_validator.py` | L2 LLM验证 | Round 01 已创建 |
| `skill-registry.db` | skill数据库 | 已有 |

---

## Step 2.4: 端到端验证

### 任务: 用 2 个不同模式的 skill 验证完整流水线

**测试用例 1: Reviewer 模式**
- 候选: 从 DB 中选 1 个审查/评估类 skill
- 模板: `reviewer_template.md`
- 预期: L1 10/10 + 依赖验证通过 + L2 TRACE≥35

**测试用例 2: Pipeline 模式**
- 候选: 从 DB 中选 1 个多步骤流程类 skill  
- 模板: `pipeline_template.md`
- 预期: L1 10/10 + 依赖验证通过 + L2 TRACE≥35

### 验证步骤(每个测试用例)

1. 运行 `python generate_skill.py from-existing <slug> --template <template>`
2. 检查生成报告:
   - L1 是否 10/10
   - 依赖验证是否通过(或标记为manual_review)
   - L2 TRACE 是否 ≥35
3. 如 L1 未通过, 修复后重试(最多 2 轮)
4. 如 L2 未通过, 分析原因并记录

### 成功标准

| 指标 | 目标 |
|------|------|
| 流水线脚本创建 | ✓ generate_skill.py 可运行 |
| Reviewer 模式测试 | L1 10/10 + L2 ≥35 |
| Pipeline 模式测试 | L1 10/10 + L2 ≥35 |
| 自动模板选择 | 正确匹配 2/2 |
| 结果汇总报告 | JSON格式, 含所有步骤结果 |
| 总耗时 | < 10 分钟/skill(含L2) |

---

## 实现顺序

### Phase A: 创建 generate_skill.py (Step 2.3)

1. 创建 `d:\skills\skill-registry\generate_skill.py`
2. 实现 `select_template()` - 模板自动选择
3. 实现 `generate_from_template()` - 模板填充(规则填充版, 非LLM调用)
4. 实现 `run_generation_pipeline()` - 流水线编排
5. 实现 CLI 接口(from-existing / from-candidate / batch)
6. 用 daily-report-writer 测试基本功能(应复现 Round 05 的结果)

### Phase B: 端到端验证 (Step 2.4)

7. 从 DB 选 1 个 Reviewer 模式 skill, 运行流水线
8. 检查结果, 如需修复则修复
9. 从 DB 选 1 个 Pipeline 模式 skill, 运行流水线
10. 检查结果, 如需修复则修复
11. 汇总 2 个测试用例的结果

### Phase C: 生成 Round 07 提示词

12. 生成 Round 07 提示词(Phase 3: 运维层补全 - health_check.py + 定时任务)

---

## 关键约束

1. **不调用LLM API**: generate_from_template() 使用规则填充(从原始SKILL.md提取信息), 不调用LLM API。LLM评估仅在L2步骤中由AI agent手动执行。
2. **不破坏现有**: 不修改已有的 skill 文件, 只生成新文件到 packaged-skills/skillhub/
3. **错误不中断**: 流水线中某步失败时, 记录错误并继续后续步骤(除非L1失败阻塞)
4. **报告完整**: 每次运行必须输出完整的JSON报告, 含所有步骤的结果和耗时
5. **模板选择可覆盖**: 自动选择模板时, 允许用户用 --template 参数手动覆盖

---

## 不在本轮范围

- 运维层补全(Phase 3: health_check.py, 定时任务, 告警)
- 3 skill 全链路验证(Phase 4)
- 批量生成60个skill(Phase 4)
- 文件清理(独立任务)

---

## 验收标准

- [ ] `generate_skill.py` 创建完成, CLI 可运行
- [ ] `select_template()` 能根据内容自动选择模板
- [ ] `generate_from_template()` 能填充模板占位符
- [ ] `run_generation_pipeline()` 串联 L1+dep_verify+L2
- [ ] daily-report-writer 测试通过(复现 Round 05 结果)
- [ ] Reviewer 模式 skill 测试通过(L1 10/10 + L2 ≥35)
- [ ] Pipeline 模式 skill 测试通过(L1 10/10 + L2 ≥35)
- [ ] 生成汇总报告 JSON 格式完整
