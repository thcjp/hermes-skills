---
slug: auto-monitor
name: auto-monitor
version: "1.0.0"
displayName: Auto Monitor - System Monitoring
summary: 主动监控系统状态。定期检查服务器健康，主动汇报，无需等待指令。
license: MIT
description: |-
  主动监控系统状态。定期检查服务器健康，主动汇报，无需等待指令。

  核心能力:

  - 运维工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 系统运维、监控告警、资源管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 状态, system, monitor, 主动监控系统, auto, 定期检查服务, monitoring, 器健康
tags:
- Operations
tools:
- read
- exec
---

# Auto Monitor - System Monitoring

主动监控系统，主动发现问题。

## 能力轮廓

* **输入**：系统状态
* **输出**：健康报告 + 异常告警
* **核心**：主动检查 → 及时汇报

## 工作流

```text
1. 定期检查（每 N 分钟）
2. 检查项：
   - 磁盘使用率
   - 内存使用率
   - CPU 负载
   - 网络状态
   - 进程状态
3. 异常判断
   - 超过阈值？→ 主动告警
4. 汇报
   - 正常：简洁汇报
   - 异常：详细说明 + 建议
```

## 告警阈值

* 磁盘 > 80%
* 内存 > 85%
* CPU Load > 核数 × 0.8

## 主动性

* 不等用户问"服务器怎么样"
* 发现问题主动说
* 可以自动修复的立刻处理

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
