# V144执行提示词 — 真实问题修复(基于多Agent交叉审核)

> **方法论**: 代码驱动 + grep验证 + 关联验证
> **规则**: 禁mock/pass/todo;每任务附grep验证
> **来源**: V142-V143声称"已完成"经3组独立审核发现9处严重问题

---

## 背景: V142-V143声明被审核推翻

### 审核9项核心发现

| # | 声明 | 实际 | 严重度 |
|---|------|------|--------|
| 1 | 零pass残留 | 21处裸pass(2处掩盖错误) | 严重 |
| 2 | 效率提升3倍消除 | _QUANT_POOL仍含;3文件共享固定文案 | 高 |
| 3 | E13断点修复 | optimize_marketing_copy仍只生成prompt | 严重 |
| 4 | plug_orchestrator集成 | orchestrator.py零引用 | 严重 |
| 5 | skillhub_adapter收口 | enterprise_uploader零引用 | 高 |
| 6 | pre_upload_checks消除复制 | 两个上传器未接入 | 高 |
| 7 | 版本追踪闭环 | 半闭环(无自动触发升级) | 中 |
| 8 | "5处其他pass"修复 | V143原始prompt无此声明(可能虚构) | 高 |
| 9 | 架构图准确性 | download_tracking/top_earning不存在 | 高 |

---

## 任务清单

### G1: 修复2处掩盖错误的pass (P0, 20min)

| 文件 | 行号 | 当前 | 修复 |
|------|------|------|------|
| skillhub_adapter.py | ~171 | `except Exception: pass` | `except Exception as e: print(f"[WARN] ...: {e}")` |
| skill_core/parser.py | ~310 | `except Exception: pass` | `except Exception as e: print(f"[WARN] ...: {e}")` |

### G2: 消除3文件共享固定文案 (P0, 30min)

| 文件 | 行号 | 硬编码文案 |
|------|------|-----------|
| auto_differentiate.py | ~1527 | "适用于独立开发者与一人公司效率提升" |
| generate_skill.py | ~1153,1156 | "支持多种输入格式,输出结构化结果,适用于独立开发者与一人公司效率提升" |
| skill_batch_upgrader_v2.py | ~244 | 同上完全相同文案 |

修复: 提取为共享函数+差异化文案池

### G3: 修复optimize_marketing_copy的E13断点 (P0, 1h)

orchestrator.py调用的optimize_marketing_copy在use_agent=True时仍只生成prompt不执行LLM。

修复: 在optimize_marketing_copy中调用llm_bridge.execute()

### G4: plug_orchestrator接入orchestrator (P0, 30min)

orchestrator.py phase_package中应调用PlugOrchestrator

### G5: skillhub_adapter接入enterprise_uploader (P1, 1h)

enterprise_uploader应从skillhub_adapter读取配置

### G6: pre_upload_checks接入两个上传器 (P1, 1h)

### G7: 修复v94.md文档不准确声明 (P0, 30min)

---

## 防漂移检查清单

- [ ] G1: 2处掩盖错误pass修复
- [ ] G2: 3文件共享文案消除
- [ ] G3: optimize_marketing_copy调用llm_bridge.execute
- [ ] G4: plug_orchestrator在orchestrator.py中被调用
- [ ] G5: enterprise_uploader引用skillhub_adapter
- [ ] G6: 两个上传器调用pre_upload_checks
- [ ] G7: v94.md修正虚假声明
