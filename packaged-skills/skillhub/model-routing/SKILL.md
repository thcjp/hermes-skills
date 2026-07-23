---
slug: "model-routing"
name: "model-routing"
version: "1.0.0"
displayName: "模型路由工具(专业版)"
summary: "团队级模型路由套件,含成本仪表盘、批量分发、自定义规则与监控告警。"
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
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# 模型路由工具(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 能力模块 | 支持 | 支持 |
| 与免费版差异 | 不支持 | 支持 |
| 三层路由 | 不支持 | 支持 |
| 与免费版一致 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 说明 | 与免费版差异 |
| --- | --- | --- |
| 三层路由 | Flash → Standard → Plus / 32B 决策 | 与免费版一致 |
| 黄金规则 | 30秒思考阈值 | 与免费版一致 |
| 自定义规则 | 团队路由规则引擎(正则/关键词/任务类型) | 免费版无 |
| 成本仪表盘 | 按任务/项目/团队/模型追踪成本 | 免费版无 |
| 批量分发 | 批量任务并发路由与结果聚合 | 免费版仅单任务 |
| 实时监控 | 超预算告警、异常路由检测 | 免费版无 |
| 团队策略 | 白名单、降级策略、成本上限 | 免费版无 |
| 多供应商 | 多供应商路由与故障转移 | 免费版单供应商 |
| 报告导出 | 周/月成本与路由报告 | 免费版无 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项。

**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 三层路由

针对三层路由,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供三层路由相关的配置参数、输入数据和处理选项。

**输出**: 返回三层路由的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`三层路由`的配置文档进行参数调优
### 黄金规则

针对黄金规则,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供黄金规则相关的配置参数、输入数据和处理选项。

**输出**: 返回黄金规则的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`黄金规则`的配置文档进行参数调优
#
## 适用场景

### 场景一:企业API成本治理

团队希望追踪各项目的API成本,并在超预算时告警。

```bash
# 查看本月成本仪表盘
node （请参考skill目录中的脚本文件） --period month --group-by project

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

团队需要并发处理大量任务,按复杂度自动路由并聚合结果。

```javascript
// batch-route.mjs 批量路由分发
import { routeBatch } from './lib/router.mjs';

const tasks = [
  { id: 't1', content: '翻译这段话', expectedComplexity: 'low' },
  { id: 't2', content: '实现用户认证模块', expectedComplexity: 'medium' },
  { id: 't3', content: '设计多区域部署架构', expectedComplexity: 'high' },
  // ... 100个任务
];

const results = await routeBatch(tasks, {
  concurrency: 10,
  costCap: 50,          // 单批成本上限$50
  fallbackModel: 'GLM-4.5-Flash',  // 超成本降级
  onProgress: (done, total) => console.log(`${done}/${total}`),
});

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

团队希望根据任务特征自定义路由,而非完全依赖默认决策。

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

  - name: 翻译任务用Flash
    match:
      allOf:
        - keyword: "翻译"
        - maxLength: 500
    route: flash
    reason: "短文本翻译用Flash足够"

  - name: 代码审查用Standard
    match:
      anyOf:
        - regex: "(审查|review|PR)"
        - filePattern: "*.py"
    route: standard
    reason: "代码审查是Standard主力场景"

  - name: 成本上限降级
    condition:
      monthlyBudgetUsed: ">80%"
    route: flash
    fallback: true
    reason: "月度预算超80%,降级到Flash"

default: standard  # 未匹配规则时的默认路由
```

## 使用流程

### 1. 团队配置初始化

```bash
# 初始化团队路由配置
mkdir -p config reports
cp config/routing-rules.example.yaml config/routing-rules.yaml
cp config/budget-alerts.example.yaml config/budget-alerts.yaml

# 编辑团队规则
vi config/routing-rules.yaml
```

### 2. 单任务路由(兼容免费版)

```javascript
import { route } from './lib/router.mjs';

// 自动决策
const result = await route({
  content: '设计多租户数据库schema',
});
// → { model: 'GLM-4-Plus', tier: 'plus', reason: '架构决策' }

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

# 输出成本与路由报告
node （请参考skill目录中的脚本文件） \
  --input tasks.json \
  --report reports/batch-$(date +%Y%m%d).html
```

### 4. 成本仪表盘

```bash
# 月度成本报告
node （请参考skill目录中的脚本文件） --period month --format html > reports/month.html

# 按团队分组
node （请参考skill目录中的脚本文件） --period month --group-by team

# 导出CSV
node （请参考skill目录中的脚本文件） --period month --format csv > reports/month.csv
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | model-routing处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js版本**: 建议 20 LTS 及以上(用于运行路由与监控脚本)
- **数据库**: 可选,用于持久化审计日志(建议使用时序数据库)

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 模型API供应商 | API | 必需 | 自行选择并申请API Key |
| Node.js | 运行时 | 必需 | nodejs.org 下载 |
| jq | JSON处理 | 推荐 | 系统包管理器安装 |
| 通知渠道 | webhook | 可选 | Slack/飞书/企业微信等 |

### API Key 配置

- 本Skill基于指令驱动,无需额外API Key。
- 各模型API供应商需配置独立Key,建议通过环境变量(如 `PROVIDER_A_KEY`、`PROVIDER_B_KEY`)注入,不入库。
- 通知渠道的webhook URL需配置为环境变量或密钥管理器。
- 审计日志若存数据库,数据库凭据按对应服务文档配置。

### 可用性分类

- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,。PRO版面向团队与企业,提供成本仪表盘、批量分发、自定义规则与监控告警能力,完全兼容免费版三层路由决策。

## 案例展示

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

  - name: provider-b
    enabled: true
    priority: 2
    models:
      flash: "model-b-flash"
      standard: "model-b-standard"
      plus: "model-b-plus"
    apiKey: "${PROVIDER_B_KEY}"
    costMultiplier: 0.85  # 便宜15%

  - name: provider-c
    enabled: false          # 备用,默认禁用
    priority: 3
    models: { ... }
    apiKey: "${PROVIDER_C_KEY}"
```

## 常见问题

### Q1:PRO版与免费版如何共存?

两者三层路由决策完全兼容,PRO版包含免费版全部能力。团队升级时直接替换Skill文件,已有路由逻辑无需改造。

### Q2:成本仪表盘数据从哪里来?

仪表盘数据来自路由决策审计日志。每次路由都会记录:任务ID、选择的模型、实际成本、时间戳、项目/团队标签。建议日志保留90天,定期归档。

### Q3:自定义规则会覆盖默认决策吗?

会。规则引擎优先级:自定义规则 > 强制指定 > 默认决策树。未匹配任何规则时回退到默认决策树(与免费版一致)。

### Q4:多供应商如何选择主供应商?

建议按成本与可用性选择:优先用costMultiplier低的(更便宜),健康检查异常的自动降级。可设置优先级,主供应商故障时自动切换到备用。

### Q5:批量分发会触发API限流吗?

可能。建议设置合理的 `concurrency`(默认10)与供应商的限流配置匹配。批量超过100个任务时建议分批并加间隔,避免突发流量触发限流。

### Q6:支持多租户隔离吗?

支持。通过不同项目/团队标签实现租户隔离,各租户的预算、规则、审计日志独立。租户间数据互不影响。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 
