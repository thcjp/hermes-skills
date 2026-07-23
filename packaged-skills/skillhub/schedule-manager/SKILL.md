---
slug: "schedule-manager"
name: "schedule-manager"
version: "1.0.0"
displayName: "任务调度管家(专业版)"
summary: "全功能任务调度系统，含依赖链、失败重试、多通道告警、日历集成、团队时区协调与监控仪表盘，支撑企业级调度场景。"
license: "Proprietary"
edition: "pro"
description: |-
  任务调度管家专业版是面向团队与企业的全功能任务调度系统。在免费版基础上解锁任务依赖链（DAG编排）、失败自动重试与指数退避、多通道告警（邮件/Telegram/钉钉/飞书）、日历集成（Google Calendar/Outlook）、团队时区协调视图、监控仪表盘、任务优先级与资源调度七大高级能力。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。
tags:
  - 任务调度
  - 自动化
  - 依赖编排
  - 企业调度
  - 监控告警
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# 任务调度管家(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

### 功能一：DAG任务依赖编排
专业版支持有向无环图（DAG）任务编排，定义任务间依赖关系：

> 详细代码示例已移至 `references/detail.md`

**DAG执行规则**：
- 仅当所有`depends_on`任务成功后，下游任务才触发
- 任一节点失败，下游节点全部跳过（避免无效执行）
- 支持条件分支（`condition`字段，基于上游输出判断）
- 支持并行节点（无依赖关系的节点自动并行）

### 功能二：失败自动重试与指数退避
```json
{
  "fetch": {
    "task": "从API抓取数据",
    "retry": {
      "max_retries": 3,
      "backoff_strategy": "exponential",
      "base_delay_seconds": 60,
      "retry_on": ["timeout", "5xx_error", "network_error"]
    }
  }
}
```

**退避策略**：
- `exponential`（指数退避）：60s → 240s → 540s（base × retry²）
- `linear`（线性退避）：60s → 120s → 180s
- `fixed`（固定间隔）：60s → 60s → 60s
- `custom`（自定义）：指定每次重试的精确延迟

**重试触发条件**：
- 超时（timeout）
- 网络错误（network_error）
- 5xx服务端错误（5xx_error）
- 默认不重试4xx客户端错误与业务逻辑错误

**处理**: 解析功能二：失败自动重试与指数退避的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回功能二：失败自动重试与指数退避的处理结果,包含执行状态码、结果数据和执行日志。### 功能三：多通道失败告警
> 详细代码示例已移至 `references/detail.md`

**告警类型**：
- `on_failure`：任务失败时立即告警
- `on_retry`：任务重试时告警（默认关闭，避免噪音）
- `on_recovery`：任务恢复成功时告警（让运维知道已恢复）
- `on_dead_letter`：任务进入死信队列时告警（重试耗尽）

**告警内容模板**：
```text
🚨 调度告警
任务："manager_result"
链："manager_metadata"
失败原因："manager_status"
已重试："manager_summary"/"manager_summary"
下次重试："manager_details"
建议操作：执行流程
```

**输入**: 用户提供功能三：多通道失败告警所需的指令和必要参数。
**输出**: 返回功能三：多通道失败告警的处理结果,包含执行状态码、结果数据和执行日志。### 功能四：日历集成
```bash
export GOOGLE_CALENDAR_ID="your-calendar@gmail.com"
export GOOGLE_CREDENTIALS_PATH="~/.credentials/google.json"

export OUTLOOK_CALENDAR_ID="your-calendar@outlook.com"
export OUTLOOK_TOKEN_PATH="~/.credentials/outlook.json"
```

**双向同步**：
- 任务创建时自动在日历创建事件
- 日历事件修改时自动更新任务时间
- 任务完成时自动标记日历事件为已完成

**输入**: 用户提供功能四：日历集成所需的指令和必要参数。
**处理**: 解析功能四：日历集成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 功能五：团队时区协调视图
```text
团队时区协调视图
┌────────────┬──────────┬──────────┬──────────┬──────────┐
│ 任务        │ 上海时间 │ 纽约时间 │ 伦敦时间 │ 东京时间 │
├────────────┼──────────┼──────────┼──────────┼──────────┤
│ 每日站会    │ 09:00    │ 21:00-1  │ 02:00    │ 10:00    │
│ 周报同步    │ Fri 16:00│ Fri 04:00│ Fri 09:00│ Fri 17:00│
│ 数据备份    │ 02:00    │ 14:00-1  │ 19:00-1  │ 03:00    │
└────────────┴──────────┴──────────┴──────────┴──────────┘
⚠️ 标记：纽约与伦敦时间可能在非工作时间，建议调整
```

**输入**: 用户提供功能五：团队时区协调视图所需的指令和必要参数。
**处理**: 解析功能五：团队时区协调视图的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回功能五：团队时区协调视图的处理结果,包含执行状态码、结果数据和执行日志。### 功能六：监控仪表盘
```bash
python3 ~/workspace/schedule/dashboard.py --port 19196

```

**仪表盘指标**：
- 执行成功率（近7天/30天/90天）
- 平均执行耗时与P95耗时
- 失败任务Top 10
- 任务执行趋势图
- 死信队列状态
- 资源并发使用率

**输入**: 用户提供功能六：监控仪表盘所需的指令和必要参数。
**输出**: 返回功能六：监控仪表盘的处理结果,包含执行状态码、结果数据和执行日志。### 功能七：优先级与资源调度
```json
{
  "critical_report": {
    "task": "生成老板要看的关键报表",
    "priority": "critical",
    "resource_pool": "high_memory",
    "max_concurrent_in_pool": 2
  },
  "daily_cleanup": {
    "task": "清理临时文件",
    "priority": "low",
    "resource_pool": "default"
  }
}
```

**优先级规则**：
- `critical`：抢占低优先级任务的资源，立即执行
- `high`：优先于normal与low执行
- `normal`：默认优先级
- `low`：仅在资源空闲时执行
#
## 适用场景

**痛点**：CI/CD流水线涉及构建、测试、扫描、部署多步骤，步骤间有严格依赖，任一失败需立即告警。

**配置**：

> 详细代码示例已移至 `references/detail.md`

**效果**：流水线全自动化，unit_test与security_scan并行执行缩短30%耗时，任一失败立即钉钉告警并暂停下游，避免错误代码进入生产环境。

## 使用流程

### 60秒上手（升级激活）
专业版完全兼容免费版的目录结构与数据格式，无需迁移：

```bash
ls ~/workspace/schedule/

cat ~/workspace/schedule/preferences.json | grep edition
```

### 依赖说明

### 运行环境
1. **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
2. **操作系统**: Windows / macOS / Linux
3. **Python**: 3.8+（用于监控仪表盘与日历同步脚本）
4. **Node.js**: 14+（用于webhook告警脚本，可选）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| cron解析库 | 库 | 必需 | Python `croniter` |
| Express | npm包 | 仪表盘必需 | `npm install express` |
| Google API客户端 | 库 | 日历集成必需 | `pip install google-api-python-client` |
| Requests | 库 | 告警必需 | `pip install requests` |

### API Key 配置
5. 钉钉/飞书webhook：通过环境变量`DINGTALK_WEBHOOK`/`FEISHU_WEBHOOK`配置
6. Telegram bot：通过环境变量`TELEGRAM_BOT_TOKEN`配置
7. Google Calendar：OAuth凭证存储在`~/.credentials/google.json`
8. Outlook Calendar：OAuth凭证存储在`~/.credentials/outlook.json`
9. 仪表盘token：每次启动自动生成，或通过`DASHBOARD_TOKEN`环境变量指定
10. 所有敏感信息通过环境变量传入，禁止硬编码在配置文件中

### 可用性分类
11. **分类**: MD+EXEC（）
12. **说明**: 基于Markdown的AI Skill，

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | schedule-manager处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "manager_count": "manager_count_value",
      "manager_timestamp": "manager_timestamp_value",
      "manager_version": "manager_version_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/schedule-manager_template`

## 异常处理


| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 任务链不触发 | trigger配置错误或时区不匹配 | 检查cron表达式与timezone字段；用`schedule dry-run <chain>`验证 | 高 |
| 依赖节点不执行 | 上游节点失败或被跳过 | 检查上游节点状态；查看是否触发`on_failure`策略 | 高 |
| 不生效 | retry配置缺失或触发条件不匹配 | 检查`retry_on`是否包含实际错误类型；查看日志中的error分类 | 高 |
| 告警未发送 | webhook配置错误或token过期 | 验证webhook URL可达性；检查环境变量是否正确加载 | 高 |
| 仪表盘无法访问 | 端口被占用或token错误 | 检查端口占用；确认URL中的token与启动日志一致 | 中 |
| 日历同步失败 | OAuth凭证过期或权限不足 | 重新生成凭证；确认日历API权限已授予 | 中 |
| 任务链执行缓慢 | 并发度不足或资源竞争 | 调整`max_concurrent`；为高优先级任务设置独立资源池 | 中 |
| 检查点恢复失败 | 检查点文件损坏或版本不兼容 | 从最近的有效检查点恢复；检查存储目录权限 | 高 |
| 死信队列堆积 | 任务持续失败未处理 | 排查失败根因；修复后手动或discard | 高 |
| 时区显示错误 | preferences中timezone配置错误 | 显式设置timezone；检查系统时区是否正确 | 低 |
| 优先级抢占失效 | priority字段未配置或资源池未隔离 | 检查priority与resource_pool配置；确认并发限制 | 中 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM执行各步骤的智能处理, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 场景一：企业级CI/CD流水线编排（DevOps工程师角色）
**痛点**：CI/CD流水线涉及构建、测试、扫描、部署多步骤，步骤间有严格依赖，任一失败需立即告警。

**配置**：

> 详细代码示例已移至 `references/detail.md`

**效果**：流水线全自动化，unit_test与security_scan并行执行缩短30%耗时，任一失败立即钉钉告警并暂停下游，避免错误代码进入生产环境。

### 场景二：跨时区分布式团队协作（技术负责人角色）
**痛点**：团队分布在3个时区，定期同步会议时间难以协调，数据备份任务需在所有人下班后执行。

**配置**：
```text
1. 用团队时区协调视图找出所有人都在工作时间的窗口
2. 将站会调度到上海9:00（纽约21:00前一天，伦敦2:00，东京10:00）
   - 伦敦2:00不合理，调整为上海20:00（伦敦12:00，纽约8:00，东京21:00）
3. 数据备份调度到上海凌晨2:00（所有时区都在非工作时间）
```

**效果**：通过时区协调视图一眼看清优秀会议时间，避免用 calculators 反复换算。备份任务选择对所有人影响最小的窗口。

### 场景三：关键业务任务监控（运维工程师角色）
**痛点**：关键业务任务（如每日结算）失败后无人知晓，影响次日业务，缺乏全局监控视角。

**配置**：

> 详细代码示例已移至 `references/detail.md`

**效果**：结算任务失败立即多通道告警（含电话呼叫），3次重试后进入死信队列触发紧急告警。监控仪表盘实时展示成功率与P95耗时，SLA超时自动升级告警级别。

### 场景四：复杂数据ETL调度（数据工程师角色）
**痛点**：ETL流程涉及多数据源抽取、转换、加载，步骤间有依赖，需要断点恢复与幂等保障。

**配置**：
```json
{
  "etl_pipeline": {
    "trigger": { "cron": "0 1 * * *" },
    "nodes": {
      "extract_mysql": { "task": "抽取MySQL数据", "checkpoint": true },
      "extract_mongo": { "task": "抽取MongoDB数据", "checkpoint": true },
      "transform": { "task": "数据转换与清洗", "depends_on": ["extract_mysql", "extract_mongo"] },
      "load_warehouse": { "task": "加载到数据仓库", "depends_on": ["transform"] },
      "verify": { "task": "数据校验", "depends_on": ["load_warehouse"] }
    },
    "checkpoint": { "enabled": true, "storage": "~/workspace/schedule/checkpoints/" }
  }
}
```

**效果**：每步执行后保存检查点，失败后从最后成功的检查点恢复，避免全量重跑。校验步骤确保数据质量，校验失败自动告警。

## 常见问题

### Q1：免费版与专业版有什么区别？
免费版提供基础调度（一次性任务、周期任务、时区感知、执行日志）。专业版新增7大高级功能：DAG任务依赖编排、失败自动重试与指数退避、多通道告警、日历集成、团队时区协调视图、监控仪表盘、优先级与资源调度。此外提供多角色场景指南、性能优化策略和多平台集成示例。

### Q2：DAG编排支持哪些依赖模式？
支持串行依赖（A→B→C）、并行无依赖（A与B并行）、合并依赖（A与B都成功后触发C）、条件分支（根据A的输出决定执行B或C）。不支持循环依赖（DAG是有向无环图）。复杂条件可通过`condition`字段基于上游输出判断。

### Q3：重试策略如何选择？
- **网络波动型任务**（如API调用）：指数退避，重试3-5次
- **资源竞争型任务**（如数据库写入）：线性退避，重试2-3次
- **幂等性任务**：可多次重试，退避可短
- **非幂等任务**：谨慎重试，避免重复执行副作用

### Q4：告警通道如何配置？
在`preferences.json`的`alerts.channels`中配置各通道的webhook或token。所有敏感信息（webhook URL、bot token）通过环境变量传入，不硬编码在配置文件中。支持钉钉、飞书、邮件、Telegram、企业微信。

### Q5：监控仪表盘会泄露任务数据吗？
仪表盘默认绑定`127.0.0.1`，仅本地可访问。token在每次启动时随机生成。仪表盘仅展示任务元数据（名称、状态、耗时）与错误信息，不展示任务执行的具体业务数据。

### Q6：日历集成支持哪些日历？
支持Google Calendar与Microsoft Outlook Calendar。双向同步需要配置OAuth凭证。单向同步（任务→日历事件）仅需只读权限。不支持Apple Calendar原生集成（可通过Google Calendar间接同步）。

### Q7：死信队列是什么？如何处理？
死信队列存储重试耗尽仍失败的任务。进入死信队列的任务不会自动重试，需要人工介入排查。处理方式：修复问题后手动重试（`schedule retry <task_id>`）、放弃任务（`schedule discard <task_id>`）、调整重试策略后重新入队。

### Q8：优先级调度如何工作？
高优先级任务会抢占低优先级任务的资源。被抢占的任务会保存检查点并暂停，待高优先级任务完成后恢复执行。critical级别任务可抢占所有其他任务。同优先级任务按FIFO顺序执行。

### Q9：检查点恢复如何保障幂等性？
检查点记录每步的执行状态与输出。恢复时从最后成功的检查点继续，跳过已完成的步骤。对于非幂等操作（如发送邮件），检查点会记录"已发送"标记，恢复时不会重复发送。建议关键任务设计为幂等。

### Q10：专业版能管理多少个任务？
专业版设计支持单实例管理1000+任务、100+任务链。实际性能取决于任务执行频率与资源占用。建议高频任务（每分钟级）单独部署实例，避免相互影响。监控仪表盘支持按任务链分组查看，避免信息过载。

### Q11：团队多用户如何共享调度配置？
将`~/workspace/schedule/`目录纳入git版本控制，团队成员通过git共享配置。告警通道的token通过环境变量各自配置，不提交到git。监控仪表盘支持多用户访问（基于token鉴权）。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

