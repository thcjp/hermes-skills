# 详细参考 - workflow-splitter-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (json)

```json
{
  "smart": {
    "enabled": true,
    "historyBased": true,
    "autoRebalance": true,
    "learningRate": 0.1
  },
  "models": {
    "routing": {
      "reasoning": ["gpt-4o", "claude-opus"],
      "coding": ["claude-sonnet", "gpt-4o"],
      "creative": ["claude-opus", "gpt-4o"],
      "analysis": ["gpt-4o", "claude-sonnet"]
    },
    "parallel": {
      "enabled": true,
      "maxConcurrent": 3,
      "strategy": "vote"
    },
    "preferences": {
      "preferredProvider": "auto",
      "fallback": true
    }
  },
  "execution": {
    "parallel": true,
    "maxWorkers": 8,
    "dependencyAware": true
  },
  "collaboration": {
    "enabled": true,
    "team": ["alice", "bob", "charlie"],
    "taskAssignment": "balanced"
  },
  "versioning": {
    "enabled": true,
    "retention": 30
  }
}
```

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────┐
│            工作流分解器 专业版 (WORKFLOW SPLITTER PRO)             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  核心引擎层  │  │  智能算法层  │  │  模型编排层  │             │
│  │             │  │             │  │             │             │
│  │ 任务分析    │  │ 历史数据    │  │ 多模型协作  │             │
│  │ 步骤拆解    │  │ 拆解优化    │  │ 路由规则    │             │
│  │ 进度跟踪    │  │ 自动平衡    │  │ 自定义偏好  │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  并行执行层  │  │  性能分析层  │  │  协作管理层  │             │
│  │             │  │             │  │             │             │
│  │ 依赖图分析  │  │ 瓶颈识别    │  │ 多人协作    │             │
│  │ 自动并行化  │  │ 优化建议    │  │ 任务分发    │             │
│  │ 重平衡      │  │ 效率报告    │  │ 进度同步    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 完整搭建（<300秒）
配置多模型编排与团队协作：

在 `~/.workflow-splitter/config.json` 中配置：

```json
{
  "smart": {
    "enabled": true,
    "historyBased": true,
    "autoRebalance": true,
    "learningRate": 0.1
  },
  "models": {
    "routing": {
      "reasoning": ["gpt-4o", "claude-opus"],
      "coding": ["claude-sonnet", "gpt-4o"],
      "creative": ["claude-opus", "gpt-4o"],
      "analysis": ["gpt-4o", "claude-sonnet"]
    },
    "parallel": {
      "enabled": true,
      "maxConcurrent": 3,
      "strategy": "vote"
    },
    "preferences": {
      "preferredProvider": "auto",
      "fallback": true
    }
  },
  "execution": {
    "parallel": true,
    "maxWorkers": 8,
    "dependencyAware": true
  },
  "collaboration": {
    "enabled": true,
    "team": ["alice", "bob", "charlie"],
    "taskAssignment": "balanced"
  },
  "versioning": {
    "enabled": true,
    "retention": 30
  }
}
```



## 架构总览
```text
┌─────────────────────────────────────────────────────────────────┐
│            工作流分解器 专业版 (WORKFLOW SPLITTER PRO)             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  核心引擎层  │  │  智能算法层  │  │  模型编排层  │             │
│  │             │  │             │  │             │             │
│  │ 任务分析    │  │ 历史数据    │  │ 多模型协作  │             │
│  │ 步骤拆解    │  │ 拆解优化    │  │ 路由规则    │             │
│  │ 进度跟踪    │  │ 自动平衡    │  │ 自定义偏好  │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  并行执行层  │  │  性能分析层  │  │  协作管理层  │             │
│  │             │  │             │  │             │             │
│  │ 依赖图分析  │  │ 瓶颈识别    │  │ 多人协作    │             │
│  │ 自动并行化  │  │ 优化建议    │  │ 任务分发    │             │
│  │ 重平衡      │  │ 效率报告    │  │ 进度同步    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```



### 4. 性能分析（专业版）
```bash
workflow-splitter analyze --task-id "task-001" --metric duration

workflow-splitter report --task-id "task-001" --type efficiency

workflow-splitter suggest --task-id "task-001"

workflow-splitter compare --task-id "task-001" --history 10
```

**性能指标**：

| 指标 | 说明 | 优化方向 |
|------|------|----------|
| 步骤耗时 | 每步实际vs预估 | 调整粒度 |
| 模型效率 | 各模型执行效率 | 优化路由 |
| 并行收益 | 并行vs串行耗时 | 增加并行度 |
| 瓶颈步骤 | 耗时最长的步骤 | 拆分或优化 |
| 重试次数 | 失败重试统计 | 优化输入 |



### 1. 智能拆解算法（专业版）
```bash
workflow-splitter smart enable

workflow-splitter split "开发用户认证系统" --smart

workflow-splitter explain --task-id "task-001"
workflow-splitter rebalance --task-id "task-001"

workflow-splitter feedback --task-id "task-001" --rating 5 --comment "拆解合理"
```

**智能算法优势**：
- 基于历史拆解数据，持续优化拆解策略
- 自动识别任务模式，应用最佳拆解模板
- 根据执行反馈动态调整后续步骤
- 学习用户偏好，个性化拆解



### 场景七：大型重构的步骤规划（架构师角色）
**痛点**：大型重构涉及数百文件修改，需要精细的步骤规划以降低风险。

**对策**：用智能拆解+依赖分析+并行执行。

```bash
workflow-splitter split "单体应用拆分为微服务" --smart --granularity fine

workflow-splitter analyze-deps --task-id "task-001"

workflow-splitter report --task-id "task-001" --type risk

workflow-splitter execute-parallel --task-id "task-001" --max-workers 3
```



### Q2：智能拆解算法如何学习？
通过历史拆解数据与执行反馈持续学习。每次拆解后用户可提供评分与反馈，算法据此优化拆解策略。学习率可配置（默认0.1）。



### Q8：性能分析能识别哪些瓶颈？
五类瓶颈：(1) 耗时最长的步骤；(2) 重试次数最多的步骤；(3) 并行收益不足的步骤；(4) 模型效率低的步骤；(5) 依赖等待长的步骤。



## 性能优化策略


## 版本升级迁移指南


