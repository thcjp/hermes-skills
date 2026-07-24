# 下一轮任务提示词 (Round 05)

> **生成时间**: 2026-07-20
> **基于**: `D:\skills\docs\plans\2026-07-20-skill-automation-v2-design.md` Phase 2 Step 2.1-2.2
> **前序**: Round 04 已完成三层验证集成到上传流水线, Phase 1(验证层补全)全部完成
> **目标**: 进入Phase 2生成层补全, 创建5种设计模式模板并用模板生成1个新skill验证

## 前序成果

### Phase 1 验证层补全完成清单 (Round 01-04)

| 轮次 | 完成内容 | 验证结果 |
|------|---------|---------|
| Round 01 | llm_validator.py (L2验证器) | sales-copy-writer TRACE 44/50 A级 |
| Round 02 | dependency_verifier.py (依赖验证器) | ai-artist-workstation 识别"鹧应AI写真"[付费] |
| Round 03 | agent_trial.py (L3试运行器) | sales-copy-writer 100/100 A级, 6用例全通过 |
| Round 04 | 三层验证集成到sync_skill_to_platform() | 4场景测试全通过 |

### 三层验证体系架构

```
L1 静态检查 (quality_gate.py, <1秒)
  ↓ PASS
L2 LLM模拟验证 (llm_validator.py, ~30秒) + 依赖验证 (dependency_verifier.py)
  ↓ PASS (TRACE≥35)
L3 真实agent试运行 (agent_trial.py, ~2分钟)
  ↓ PASS (3/3典型+异常处理+输出可用)
正式上传到平台
```

### Round 04 集成测试发现
- sales-copy-writer 当前515行, 超过L1的500行上限(9/10通过) - 真实问题被L1正确检测
- L2/L3最终报告不存在时, 正确阻止上传并给出AI执行指引
- --skip-l2/--skip-l3 参数正常工作, 支持批量场景

## 本轮范围（严格限定）

1. **Step 2.1**: 创建5种设计模式模板
2. **Step 2.2**: 用模板生成1个新skill并验证

## 任务详情

### Step 2.1: 创建5种设计模式模板

基于SKILL_QUALITY_STANDARD.md的8标准章节, 创建5种设计模式的生成模板。

5种设计模式(参考deep-differentiation-methodology.md):
1. **Tool Wrapper模式**: 包装外部工具/API为skill
2. **Generator模式**: 生成内容(文案/代码/设计等)
3. **Reviewer模式**: 审核/评估/打分
4. **Inversion模式**: 反向操作(如解密/还原/反推)
5. **Pipeline模式**: 多步骤流水线(如数据处理全流程)

模板要求:
- 每个模板包含8标准章节骨架(核心能力/适用场景/使用流程/输入格式/输出格式/异常处理/依赖说明/案例展示)
- 每个章节有写作指引(说明该章节应写什么)
- 每个章节有质量检查点(验证该章节是否达标)
- 模板用Jinja2-like占位符({{topic}}/{{feature}}等)标记AI需填充的位置
- 保存到 `d:\skills\skill-registry\templates\` 目录

文件结构:
```
skill-registry/templates/
  ├── README.md                          # 模板使用说明
  ├── tool_wrapper_template.md           # Tool Wrapper模式模板
  ├── generator_template.md              # Generator模式模板
  ├── reviewer_template.md               # Reviewer模式模板
  ├── inversion_template.md              # Inversion模式模板
  └── pipeline_template.md               # Pipeline模式模板
```

### Step 2.2: 用模板生成1个新skill验证

选择1个简单的候选skill(纯LLM驱动, 无外部依赖), 用Generator模板生成。

操作:
1. 从DB或clawhub-skills中选1个简单的候选
2. 读取Generator模板
3. AI填充模板占位符, 生成完整SKILL.md
4. 保存到 `d:\skills\packaged-skills\skillhub\{slug}\SKILL.md`
5. 运行L1静态检查验证格式
6. 运行L2验证验证内容质量
7. (可选)运行L3验证真实可运行性

预期: 模板生成的skill应通过L1+L2验证, 证明模板化生成有效。

## 不在本轮范围

- 外部依赖验证器集成到生成流水线（Step 2.3, 下一轮）
- 生成流水线端到端验证（Step 2.4, 下一轮）
- 运维层补全（Phase 3）
- 文件清理（独立任务）

## 验收标准

- [ ] 5种设计模式模板创建完成, 每个包含8标准章节
- [ ] 每个模板有写作指引和质量检查点
  - [ ] 模板用占位符标记AI填充位置
- [ ] 用Generator模板生成1个新skill
- [ ] 新skill通过L1静态检查(10/10)
- [ ] 新skill通过L2验证(TRACE≥35)
- [ ] 模板化生成比从零设计效率更高

## 关键约束

1. **小规模**: 只用1个候选skill验证模板
2. **模板不是死板套用**: 模板提供骨架和指引, AI填充具体内容
3. **8标准章节必须完整**: 每个模板的8章节不能缺失
4. **质量检查点实用**: 检查点应能实际验证章节质量, 非形式化
5. **不破坏现有**: 不修改已有的skill, 只生成新skill
