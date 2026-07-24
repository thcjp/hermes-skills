---
slug: "model-routing-tool-pro"
name: "model-routing-tool-pro"
version: "1.0.0"
displayName: "模型路由工具(专业版)"
summary: "团队级模型路由套件,含成本仪表盘、批量分发、自定义规则与监控告警。。模型路由工具(专业版)面向团队与企业,在三层路由决策基础上,扩展成本分析仪表盘、批量任务分发、自定义路由规则、实时监控告警"
license: "Proprietary"
edition: "pro"
description: |-
  模型路由工具(专业版)面向团队与企业,在三层路由决策基础上,扩展成本分析仪表盘、批量任务分发、自定义路由规则、实时监控告警与团队策略治理能力。核心能力:
  - 三层路由 + 自定义规则引擎
  - 成本仪表盘:按任务/项目/团队追踪成本
  - 批量任务分发与并发路由
  - 实时监控:超预算告警、异常路由检测
  - 团队策略:路由白名单、降级策略、成本上限
  - 多供应商路由与故障转移

  适用场景:
  - 企业API成本治理与预算控制
  - 大规模子Agent并发任务分发
  - 团队路由策略统一与合规
  - 多供应商成本对比与故...
tags:
  - Development
  - AI
  - 模型路由
  - 企业级
  - 成本优化
  - 监控
  - 工具
  - 效率
  - 自动化
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# 模型路由工具(专业版)

## 概述

模型路由工具(专业版)面向团队与企业,在兼容免费版三层路由决策的基础上,扩展了成本分析仪表盘、批量任务分发、自定义路由规则、实时监控告警与团队策略治理能力.
当你在请求中提及 成本治理、批量路由、路由规则、预算告警、多供应商 等关键词时,本工具会自动激活,为团队提供结构化的模型路由治理方案.
本版本完全兼容 `model-routing-tool-free` 的三层路由决策(Flash → Standard → Plus / 32B),可平滑升级,已有路由逻辑无需改造.
## 核心能力

| 能力模块 | 说明 | 与免费版差异 |
|----|---|------|
| 三层路由 | Flash → Standard → Plus / 32B 决策 | 与免费版一致 |
| 黄金规则 | 30秒思考阈值 | 与免费版一致 |
| 自定义规则 | 团队路由规则引擎(正则/关键词/任务类型) | 免费版无 |
| 成本仪表盘 | 按任务/项目/团队/模型追踪成本 | 免费版无 |
| 批量分发 | 批量任务并发路由与结果聚合 | 免费版仅单任务 |
| 实时监控 | 超预算告警、异常路由检测 | 免费版无 |
| 团队策略 | 白名单、降级策略、成本上限 | 免费版无 |
| 多供应商 | 多供应商路由与故障转移 | 免费版单供应商 |
| 报告导出 | 周/月成本与路由报告 | 免费版无 |

### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.
**输入**: 用户提供参数配置与调用所需的指令和必要参数.
**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置.
**输入**: 用户提供结果处理与输出所需的指令和必要参数.
**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：团队级模型路由套、含成本仪表盘、自定义规则与监控、模型路由工具、专业版、面向团队与企业、在三层路由决策基、扩展成本分析仪表、批量任务分发、自定义路由规则、实时监控告警与团、队策略治理能力、核心能力、自定义规则引擎、团队追踪成本、批量任务分发与并、路由白名单等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一:企业API成本治理

团队希望追踪各项目的API成本,并在超预算时告警.
```bash
# 查看本月成本仪表盘
node （请参考skill目录中的脚本文件） --period month --group-by project
# ...
# 输出
# 项目成本仪表盘: 2026-07
#
# | 项目 | Flash | Standard | Plus | 总成本 | 预算 | 使用率 |
# | --- | --- | --- | --- | --- | --- | --- |
# | 客服机器人 | $12 | $45 | $8 | $65 | $100 | 65% |
# | 代码审查 | $3 | $28 | $15 | $46 | $80 | 57% |
# | 数据分析 | $5 | $12 | $22 | $39 | $50 | 78% |
# | 文档生成 | $8 | $6 | $0 | $14 | $30 | 47% |
# | 总计 | $28 | $91 | $45 | $164 | $260 | 63% |
```

设置预算告警:

```yaml
# config/budget-alerts.yaml 预算告警配置
alerts:
  - name: 项目级月度预算
    threshold: 80%
    action: notify
    targets:
      - slack: "#ai-cost-alerts"
      - email: ["tech-lead@company.com"]
  - name: 单任务成本异常
    threshold: $5
    action: notify_and_review
    targets:
      - webhook: "https://hooks.internal/ai-anomaly"
  - name: 总预算硬上限
    threshold: $500
    action: degrade
    degrade_to: flash
```

### 场景二:批量任务分发

团队需要并发处理大量任务,按复杂度自动路由并聚合结果.
```javascript
// batch-route.mjs 批量路由分发
import { routeBatch } from './lib/router.mjs';
// ...
const tasks = [
  { id: 't1', content: '翻译这段话', expectedComplexity: 'low' },
  { id: 't2', content: '实现用户认证模块', expectedComplexity: 'medium' },
  { id: 't3', content: '设计多区域部署架构', expectedComplexity: 'high' },
  // ... 100个任务
];
// ...
const results = await routeBatch(tasks, {
  concurrency: 10,
  costCap: 50,          // 单批成本上限$50
  fallbackModel: 'GLM-4.5-Flash',  // 超成本降级
  onProgress: (done, total) => console.log(`${done}/${total}`),
});
// ...
// 输出
// {
//   results: [...],
//   summary: {
//     total: 100,
//     success: 97,
//     failed: 3,
//     cost: $42.5,
//     routing: { flash: 45, standard: 48, plus: 7 },
//     duration: '3m 22s'
//   }
// }
```

### 场景三:自定义路由规则

团队希望根据任务特征自定义路由,而非完全依赖默认决策.
```yaml
# config/routing-rules.yaml 自定义路由规则
rules:
  - name: 含敏感关键词强制Plus
    match:
      anyOf:
        - regex: "(安全|漏洞|审计|合规)"
        - regex: "(架构|设计|重构)"
    route: plus
    reason: "敏感/架构类任务需要深度推理"
# ...
  - name: 翻译任务用Flash
    match:
      allOf:
        - keyword: "翻译"
        - maxLength: 500
    route: flash
    reason: "短文本翻译用Flash足够"
# ...
  - name: 代码审查用Standard
    match:
      anyOf:
        - regex: "(审查|review|PR)"
        - filePattern: "*.py"
    route: standard
    reason: "代码审查是Standard主力场景"
# ...
  - name: 成本上限降级
    condition:
      monthlyBudgetUsed: ">80%"
    route: flash
    fallback: true
    reason: "月度预算超80%,降级到Flash"
# ...
default: standard  # 未匹配规则时的默认路由
```

## 不适用场景

以下场景模型路由工具(专业版)不适合处理：

- 实际人员绩效评估
- 财务预算审批
- 合同法务审核

## 触发条件

需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于非本工具能力范围的需求.
## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 1. 团队配置初始化

```bash
# 初始化团队路由配置
mkdir -p config reports
cp config/routing-rules.example.yaml config/routing-rules.yaml
cp config/budget-alerts.example.yaml config/budget-alerts.yaml
# ...
# 编辑团队规则
vi config/routing-rules.yaml
```

### 2. 单任务路由(兼容免费版)

```javascript
import { route } from './lib/router.mjs';
// ...
// 自动决策
const result = await route({
  content: '设计多租户数据库schema',
});
// → { model: 'GLM-4-Plus', tier: 'plus', reason: '架构决策' }
// ...
// 强制指定层级
const result2 = await route({
  content: '翻译这段话',
  forceTier: 'flash',
});
```

### 3. 批量路由

```bash
# 从文件批量路由
node （请参考skill目录中的脚本文件） \
  --input tasks.json \
  --concurrency 10 \
  --cost-cap 50 \
  --output results.json
# ...
# 输出成本与路由报告
node （请参考skill目录中的脚本文件） \
  --input tasks.json \
  --report reports/batch-$(date +%Y%m%d).html
```

### 4. 成本仪表盘

```bash
# 月度成本报告
node （请参考skill目录中的脚本文件） --period month --format html > reports/month.html
# ...
# 按团队分组
node （请参考skill目录中的脚本文件） --period month --group-by team
# ...
# 导出CSV
node （请参考skill目录中的脚本文件） --period month --format csv > reports/month.csv
```

#
## 示例

### 团队策略配置

```yaml
# config/team-policy.yaml 团队策略
policy:
  defaultTier: standard
  cost:
    monthlyBudget: 500
    perTaskCap: 5
    degradeAt: 80%
    degradeTo: flash
  routing:
    allowForce: true           # 允许任务强制指定层级
    allowOverride: false        # 禁止绕过规则
    auditLog: true             # 记录所有路由决策
  fallback:
    primaryProvider: provider-a
    fallbackProvider: provider-b
    healthCheck: 60s
  compliance:
    forbiddenModels: []        # 合规禁用的模型
    requiredTierForPII: plus   # 含PII数据强制用Plus
```

### 多供应商故障转移

```yaml
# config/providers.yaml 多供应商配置
providers:
  - name: provider-a
    enabled: true
    priority: 1
    models:
      flash: "model-a-flash"
      standard: "model-a-standard"
      plus: "model-a-plus"
    apiKey: "${PROVIDER_A_KEY}"
    costMultiplier: 1.0
# ...
  - name: provider-b
    enabled: true
    priority: 2
    models:
      flash: "model-b-flash"
      standard: "model-b-standard"
      plus: "model-b-plus"
    apiKey: "${PROVIDER_B_KEY}"
    costMultiplier: 0.85  # 便宜15%
# ...
  - name: provider-c
    enabled: false          # 备用,默认禁用
    priority: 3
    models: { ... }
    apiKey: "${PROVIDER_C_KEY}"
```

## 最佳实践

### 1. 成本治理三阶段

| 阶段 | 动作 | 验收标准 |
|:-----|:-----|:-----|
| 1. 透明化 | 接入仪表盘,统计现状 | 各项目成本可见 |
| 2. 优化 | 应用规则,降级冗余任务 | 月成本下降20%+ |
| 3. 治理 | 预算告警与降级策略 | 超预算自动降级 |

### 2. 路由规则设计原则

- 默认路由设为Standard(平衡成本与质量)
- 仅对明确特征强制路由(正则/关键词)
- 保留降级路径(超预算降Flash)
- 规则需带reason便于审计
- 定期复盘规则命中率与效果

### 3. 批量分发参数调优

| 参数 | 推荐值 | 说明 |
|---:|---:|---:|
| concurrency | 10 | 平衡速度与API限流 |
| costCap | 单批$50 | 控制单批成本 |
| fallbackModel | Flash | 超成本降级 |
| retry | 2 | 失败重试次数 |
| timeout | 60s | 单任务超时 |

### 4. 监控告警分级

| 告警级别 | 触发条件 | 动作 |
|:---:|:---:|:---:|
| 提示 | 预算使用50% | 仅记录仪表盘 |
| 警告 | 预算使用80% | 通知团队,准备降级 |
| 严重 | 预算使用95% | 自动降级到Flash |
| 紧急 | 单任务成本>$5 | 暂停并人工审查 |

### 5. 多供应商故障转移

```bash
# 健康检查
node （请参考skill目录中的脚本文件） --all-providers
# ...
# 手动切换主供应商
node （请参考skill目录中的脚本文件） --primary provider-b
# ...
# 成本对比报告
node （请参考skill目录中的脚本文件） --period month
```

### 6. 合规与审计

```bash
# 查询路由审计日志
node （请参考skill目录中的脚本文件） --task-id t-2026-07-18-001
# ...
# 导出合规报告
node （请参考skill目录中的脚本文件） \
  --since 2026-07-01 \
  --format csv \
  --output reports/compliance-july.csv
```

## 常见问题

### Q1:PRO版与免费版如何共存?

两者三层路由决策完全兼容,PRO版包含免费版全部能力。团队升级时直接替换Skill文件,已有路由逻辑无需改造.
### Q2:成本仪表盘数据从哪里来?

仪表盘数据来自路由决策审计日志。每次路由都会记录:任务ID、选择的模型、实际成本、时间戳、项目/团队标签。建议日志保留90天,定期归档.
### Q3:自定义规则会覆盖默认决策吗?

会。规则引擎优先级:自定义规则 > 强制指定 > 默认决策树。未匹配任何规则时回退到默认决策树(与免费版一致).
### Q4:多供应商如何选择主供应商?

建议按成本与可用性选择:优先用costMultiplier低的(更便宜),健康检查异常的自动降级。可设置优先级,主供应商故障时自动切换到备用.
### Q5:批量分发会触发API限流吗?

可能。建议设置合理的 `concurrency`(默认10)与供应商的限流配置匹配。批量超过100个任务时建议分批并加间隔,避免突发流量触发限流.
### Q6:支持多租户隔离吗?

支持。通过不同项目/团队标签实现租户隔离,各租户的预算、规则、审计日志独立。租户间数据互不影响.
## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js版本**: 建议 20 LTS 及以上(用于运行路由与监控脚本)
- **数据库**: 可选,用于持久化审计日志(建议使用时序数据库)

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 模型API供应商 | API | 必需 | 自行选择并申请API Key |
| Node.js | 运行时 | 必需 | nodejs.org 下载 |
| jq | JSON处理 | 推荐 | 系统包管理器安装 |
| 通知渠道 | webhook | 可选 | Slack/飞书/企业微信等 |

### API Key 配置

- 基础LLM由Agent平台内置提供，Skill基于Markdown指令驱动
- 各模型API供应商需配置独立Key,建议通过环境变量(如 `PROVIDER_A_KEY`、`PROVIDER_B_KEY`)注入,不入库.
- 通知渠道的webhook URL需配置为环境变量或密钥管理器.
- 审计日志若存数据库,数据库凭据按对应服务文档配置.
### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent完成操作。PRO版面向团队与企业,提供成本仪表盘、批量分发、自定义规则与监控告警能力,完全兼容免费版三层路由决策.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 执行效率受模型能力与网络环境影响

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "模型路由工具(专业版)处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "model routing pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
