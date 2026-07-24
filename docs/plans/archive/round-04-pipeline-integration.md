# 下一轮任务提示词 (Round 04)

> **生成时间**: 2026-07-20
> **基于**: `D:\skills\docs\plans\2026-07-20-skill-automation-v2-design.md` Phase 1 Step 1.7
> **前序**: Round 03 已完成 agent_trial.py 编写 + sales-copy-writer L3验证通过
> **目标**: 将L1/L2/L3三层验证集成到skill上传流水线

## 前序成果

### 三层验证体系已完成

| 层级 | 脚本 | 验证内容 | sales-copy-writer结果 |
|------|------|---------|----------------------|
| L1 静态检查 | quality_gate.py | 10项格式检查 | 10/10 PASS |
| L2 LLM模拟验证 | llm_validator.py | 触发精准度+输出完整性+依赖可达性+TRACE快评 | 44/50 A级 PASS |
| L3 真实agent试运行 | agent_trial.py | 3典型输入+3异常输入+输出可用性 | 100/100 A级 PASS |

### Round 01-03 完成清单
1. ✅ llm_validator.py (L2验证器, 含格式适配bug修复)
2. ✅ dependency_verifier.py (依赖验证器, 含中文API服务识别+双重过滤)
3. ✅ agent_trial.py (L3试运行器, 含6用例+输出可用性评估)
4. ✅ sales-copy-writer 三层验证全链路通过
5. ✅ ai-artist-workstation L2验证通过(42/50 B级), 依赖验证识别出"鹧应AI写真"[付费]

## 本轮范围（严格限定）

1. **Step 1.7**: 将三层验证集成到 `sync_skill_to_platform()` 上传流水线

## 任务详情

### Step 1.7: 三层验证集成到上传流水线

当前 `sync_skill_to_platform()` 在上传前只调用 `quality_gate.py` (L1静态检查)。
需要扩展为: L1通过后 → 执行L2验证 → L2通过后 → 提示执行L3 → 全部通过才允许上传。

具体修改:
1. 读取 `update_mechanism.py` 中的 `sync_skill_to_platform()` 函数
2. 在L1检查通过后, 添加L2验证调用
3. 在L2验证通过后, 添加L3验证状态检查
4. 添加 `--skip-l2` 和 `--skip-l3` 参数, 允许批量场景跳过耗时验证
5. 验证结果记录到DB的 workflow_state 字段

设计约束:
- 不破坏现有L1集成(P0-4成果)
- L2/L3为可选执行, 默认开启, 可通过参数跳过
- L3需要AI执行, 流水线只检查"L3是否已通过", 不自动执行
- 集成后用 sales-copy-writer 验证全链路

### 验证要求

1. 修改前: 读取并理解现有 `sync_skill_to_platform()` 的完整实现
2. 修改后: 用 sales-copy-writer 试跑集成后的流水线
3. 验证: L1→L2→L3 顺序执行, 每层通过才进入下一层
4. 验证: --skip-l2 和 --skip-l3 参数正常工作
5. 验证: 未通过验证的skill被正确阻止上传

## 不在本轮范围

- 模板化生成器（Phase 2）
- 运维层补全（Phase 3）
- 文件清理（独立任务）

## 验收标准

- [ ] `sync_skill_to_platform()` 集成三层验证
- [ ] L1通过后自动执行L2
- [ ] L2通过后检查L3状态
- [ ] 未通过验证的skill被阻止上传, 记录blocked_reason
- [ ] --skip-l2 和 --skip-l3 参数正常工作
- [ ] sales-copy-writer 集成验证通过(L1+L2+L3全部PASS)
- [ ] 现有L1集成(P0-4)未被破坏
- [ ] 修改后 `sync_skill_to_platform()` 的 --help 或相关文档更新

## 关键约束

1. **小规模**: 只用 sales-copy-writer 验证集成
2. **不破坏现有**: P0-4的L1集成必须保持正常
3. **渐进式**: 先读取理解, 再修改, 后验证
4. **可跳过**: L2/L3必须支持跳过, 避免批量场景耗时过长
5. **状态可追溯**: 验证结果记录到DB, 可查询
