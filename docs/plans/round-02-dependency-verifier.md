# 下一轮任务提示词 (Round 02)

> **生成时间**: 2026-07-20
> **基于**: `D:\skills\docs\plans\2026-07-20-skill-automation-v2-design.md` Phase 1 Step 1.3-1.4
> **前序**: Round 01 已完成 llm_validator.py 编写 + sales-copy-writer 试跑通过 (TRACE 44/50, A级)
> **目标**: 编写 dependency_verifier.py 并对 ai-artist-workstation 试跑 L2+依赖验证

## 前序成果

Round 01 完成内容:
1. 编写 `d:\skills\skill-registry\llm_validator.py` (L2验证器, 4项检查+TRACE快评)
2. 对 sales-copy-writer 试跑 L2 验证通过:
   - 静态检查: T=10/10, C=10/10
   - LLM评估: T=9, R=8, A=9, C=9, E=9 → 总分 44/50 (A级)
   - DB写入: total=46, grade=A, is_llm_evaluated=true
3. 修复格式适配 bug (L2扁平格式 → save_trace_score嵌套格式转换)

## 本轮范围（严格限定）

1. **Step 1.3**: 对 `ai-artist-workstation` 试跑 L2 验证（有外部依赖的skill）
2. **Step 1.4**: 编写 `d:\skills\skill-registry\dependency_verifier.py`（外部依赖验证器）

## 任务详情

### Step 1.3: L2验证试跑-有外部依赖

ai-artist-workstation 引用了"鹧应AI写真"等外部API/模型，与纯LLM驱动的 sales-copy-writer 不同。

操作:
1. 运行 `python llm_validator.py validate ai-artist-workstation`
2. 读取生成的 L2 验证报告
3. 作为 AI 评估器执行 R+A+E 维度评估
4. 重点检查: 外部依赖"鹧应AI写真"是否真实可达
5. 运行 `python llm_validator.py import ai-artist-workstation <评估结果.json>`
6. 验证 DB 写入正确

预期发现: ai-artist-workstation 的外部依赖可能无法验证（"鹧应AI写真"非已知模型），这将暴露依赖验证器的必要性。

### Step 1.4: 编写 dependency_verifier.py

基于 Step 1.3 的发现，编写独立的外部依赖验证器。

功能要求:
1. 从 SKILL.md 提取外部依赖（复用 llm_validator.py 的 extract_external_dependencies）
2. 自动验证:
   - npm包: `npm view <package>` 检查存在性
   - PyPI包: `pip index versions <package>` 检查存在性
   - HTTP API: HEAD请求检查可达性
   - 模型名: 与已知模型列表比对
3. 输出依赖验证报告（JSON格式）
4. CLI接口:
   ```
   python dependency_verifier.py --help
   python dependency_verifier.py verify <slug>
   python dependency_verifier.py verify <slug> --json
   ```

设计约束:
- 不硬编码API Key，不实际调用需要认证的API
- HTTP HEAD请求设置3秒超时，失败标记为warning而非error
- npm/pip检查通过subprocess执行，捕获超时
- 验证结果保存到 `d:\skills\skill-registry\dep_verification_report_<slug>.json`

## 不在本轮范围

- agent_trial.py（Round 03）
- 三层验证集成到流水线（Round 04）
- 模板化生成器（Phase 2）

## 验收标准

- [ ] ai-artist-workstation 的 L2 验证报告已生成
- [ ] 正确识别 ai-artist-workstation 的外部依赖
- [ ] dependency_verifier.py 的 --help 正常
- [ ] dependency_verifier.py verify ai-artist-workstation 输出依赖验证报告
- [ ] 报告区分"已知模型/npm包/pypi包/api_endpoint"四类依赖
- [ ] 不可达/不存在的依赖标记为 warning
- [ ] 验证结果保存为 JSON 报告

## 关键约束

1. **小规模**: 只用 ai-artist-workstation 一个 skill 验证
2. **实事求是**: 依赖验证结果基于实际检查，不虚假标记
3. **不引入新 bug**: 修改前先读取原代码
4. **复用现有**: 复用 llm_validator.py 的 extract_external_dependencies 函数
5. **超时保护**: 所有外部检查设3秒超时，避免长时间阻塞
