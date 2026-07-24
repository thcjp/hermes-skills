# 下一轮任务提示词 (Round 03)

> **生成时间**: 2026-07-20
> **基于**: `D:\skills\docs\plans\2026-07-20-skill-automation-v2-design.md` Phase 1 Step 1.5-1.6
> **前序**: Round 02 已完成 dependency_verifier.py 编写 + ai-artist-workstation 试跑通过
> **目标**: 编写 agent_trial.py（L3真实agent试运行）并对 sales-copy-writer 试跑

## 前序成果

### Round 01 完成内容
1. 编写 `llm_validator.py`（L2验证器, 4项检查+TRACE快评）
2. sales-copy-writer 试跑通过: TRACE 44/50 (A级), DB写入 total=46

### Round 02 完成内容
1. ai-artist-workstation L2验证通过: TRACE 42/50 (B级), 依赖可达性WARN
2. 编写 `dependency_verifier.py`（外部依赖验证器, 6类依赖识别）
3. ai-artist-workstation 依赖验证: 成功识别"鹧应AI写真"[付费]等3个特定外部API服务
4. 优化过滤: 通用描述和误识别已正确过滤
5. sales-copy-writer 依赖验证: 9个依赖(8个已知AI模型+1个LLM_API_KEY), PASS

### 关键发现
- L2验证能发现"格式合规但依赖未验证"的问题
- dependency_verifier.py 成功识别中文名称外部API服务(如"鹧应AI写真")
- 过滤优化后无误识别

## 本轮范围（严格限定）

1. **Step 1.5**: 编写 `d:\skills\skill-registry\agent_trial.py`（L3真实agent试运行）
2. **Step 1.6**: 对 sales-copy-writer 试跑 L3 验证

## 任务详情

### Step 1.5: 编写 agent_trial.py

L3验证是分层验证的最深层级，在定稿发布前执行。

功能要求:
1. 实际启动agent加载SKILL.md，用3个典型输入测试真实输出
2. 验证内容:
   - 真实加载: agent能否正确加载SKILL.md并理解指令
   - 真实执行: 3个典型输入能否产出预期结果
   - 异常处理: 边界输入(空/超长/非法)是否有合理反馈
   - 输出可用性: 输出结果是否可直接使用(非占位符/非模板)

设计理念:
  - 不硬编码调用外部agent框架
  - 生成试运行prompt，由AI(当前会话)充当agent执行
  - 复用 llm_validator.py 的触发测试用例
  - 试运行结果保存为JSON报告

CLI接口:
```
python agent_trial.py --help
python agent_trial.py trial <slug>                    # 生成试运行prompt
python agent_trial.py trial <slug> --json              # 输出JSON格式
python agent_trial.py import <slug> <result.json>      # 导入试运行结果
```

流程:
  Step 1: 读取SKILL.md内容
  Step 2: 生成3个典型输入(复用llm_validator的触发测试用例)
  Step 3: 生成试运行prompt(含SKILL.md内容+3个输入+评估标准)
  Step 4: AI执行试运行(当前会话,非脚本自动)
  Step 5: 导入试运行结果,输出L3验证结论

### Step 1.6: 对 sales-copy-writer 试跑 L3 验证

操作:
1. 运行 `python agent_trial.py trial sales-copy-writer`
2. 读取生成的试运行prompt
3. 作为AI agent执行3个典型输入的真实试运行
4. 评估输出可用性(非占位符/非模板)
5. 保存试运行结果JSON
6. 运行 `python agent_trial.py import sales-copy-writer <结果.json>`
7. 验证L3验证结论

预期: sales-copy-writer作为纯LLM驱动skill,应能通过L3验证(3/3输入PASS+异常处理PASS)。

## 不在本轮范围

- 三层验证集成到流水线（Round 04）
- ai-artist-workstation的L3验证（因其依赖"鹧应AI写真"未验证,L3可能失败,留待依赖确认后）
- 模板化生成器（Phase 2）

## 验收标准

- [ ] `python agent_trial.py --help` 正常显示帮助
- [ ] `python agent_trial.py trial sales-copy-writer` 输出试运行prompt
- [ ] prompt包含3个典型输入和评估标准
- [ ] AI执行试运行后,3/3输入产出预期结果
- [ ] 异常处理测试通过(空输入/超长输入/非法参数)
- [ ] 输出可用性评估: 非占位符/非模板
- [ ] 试运行结果保存为JSON报告
- [ ] `python agent_trial.py import` 输出L3验证最终结论

## 关键约束

1. **小规模**: 只用 sales-copy-writer 一个 skill 验证
2. **实事求是**: 试运行结果基于真实执行,不虚假实现
3. **不引入新 bug**: 修改前先读取原代码
4. **复用现有**: 复用 llm_validator.py 的触发测试用例和find_skill_md
5. **L3 vs L2区别**: L2是"模拟评估",L3是"真实执行"。L3要实际运行skill流程,产出真实输出
