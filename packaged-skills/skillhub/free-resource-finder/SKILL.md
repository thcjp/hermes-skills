---
slug: free-resource-finder
name: free-resource-finder
version: "1.0.0"
displayName: 免费资源发现器(专业版)
summary: 全功能免费AI资源管理工具,含自动fallback、后台守护、负载均衡、成本分析与质量监控,适合长期无人值守场景。
license: Proprietary
edition: pro
description: |-
  免费资源发现器(专业版)是企业级免费AI资源管理工具,在免费版基础上扩展自动fallback链、后台守护进程、多Key负载均衡、调用统计与成本分析、模型质量监控等高级能力。核心能力:
  - 自动fallback链: 主模型失败时自动切换备用模型,保障服务连续性
  - 后台守护进程: 实时探测模型可用性,限速中断时自动重建链路
  - 多API Key负载均衡: 聚合多账号额度,突破单账号限速
  - 调用统计与成本分析: 详细记录每次调用,生成用量报告
  - 模型质量监控: 持续评估模型表现,自动调整排序
  - 智能路由: 按任务类型自动选...
tags:
- AI模型
- 资源管理
- 自动化
- 企业版
tools:
  - - read
- exec
---
# 免费资源发现器(专业版)

## 核心能力

### 自动fallback链
主模型失败时自动切换备用模型,保障服务连续性:

```text
┌──────────────────────────────────────────────────────────┐
│  请求进入                                                │
└──────────────────────────────────────────────────────────┘
                    │
                    ▼
            ┌───────────────┐
            │  主模型请求    │
            └───────────────┘
                    │
          ┌─────────┴─────────┐
          │ 成功               │ 失败(429/500/超时)
          ▼                   ▼
    ┌──────────┐      ┌───────────────┐
    │  返回结果 │      │ 切换fallback1 │
    └──────────┘      └───────────────┘
                              │
                    ┌─────────┴─────────┐
                    │ 成功               │ 失败
                    ▼                   ▼
              ┌──────────┐      ┌───────────────┐
              │  返回结果 │      │ 切换fallback2 │
              └──────────┘      └───────────────┘
                                        │
                              ┌─────────┴─────────┐
                              │ ...                │ 全部失败
                              ▼                   ▼
                        ┌──────────┐      ┌───────────────┐
                        │  返回结果 │      │ 触发守护进程   │
                        └──────────┘      └───────────────┘
```

配置示例:

```json
{
  "fallback_chain": [
    {"model": "qwen/qwen3-coder:free", "priority": 1},
    {"model": "deepseek/deepseek-coder:free", "priority": 2},
    {"model": "meta-llama/llama-3.3-70b-instruct:free", "priority": 3},
    {"model": "openrouter/free", "priority": 4}
  ],
  "fallback_policy": {
    "trigger_on": ["429", "500", "502", "503", "timeout"],
    "timeout": 30,
    "max_retries": 2,
    "cooldown": 60
  }
}
```

### 后台守护进程
实时探测模型可用性,限速中断时自动重建链路:

```bash
# 启动守护进程(前台)
free-finder daemon

# 后台运行
nohup free-finder daemon > ~/.free-finder/daemon.log 2>&1 &

# 单次探测
free-finder daemon --once

# 查看守护状态
free-finder daemon --status

# 停止守护
free-finder daemon --stop
```

守护进程工作机制:
1. 每60秒探测主模型可用性
2. 连续3次失败则触发链路重建
3. 实时测试所有fallback模型,按可用性重新排序
4. 选出最优可用模型作为新主模型
5. 通知Agent应用新配置

### 多API Key负载均衡
聚合多账号额度,突破单账号限速:

```bash
# 添加多个API Key
free-finder keys add --provider openrouter --key "sk-or-v1-key1"
free-finder keys add --provider openrouter --key "sk-or-v1-key2"
free-finder keys add --provider openrouter --key "sk-or-v1-key3"

# 查看Key状态
free-finder keys list

# 查看各Key用量
free-finder keys stats
```

负载均衡策略:

| 策略 | 说明 | 适用场景 |
| --- | --- | --- |
| round_robin | 轮询分配 | 默认,均匀消耗 |
| least_used | 优先用量最少的Key | 最大化总额度 |
| lowest_latency | 优先延迟最低的Key | 追求响应速度 |
| weighted | 按权重分配 | 混合免费与付费Key |

**输入**: 用户提供多API Key负载均衡所需的指令和必要参数。
**处理**: 按照skill规范执行多API Key负载均衡操作,遵循单一意图原则。
**输出**: 返回多API Key负载均衡的执行结果,包含操作状态和输出数据。### 调用统计与成本分析
```bash
# 查看今日统计
free-finder stats --today

# 查看本周报告
free-finder stats --week --format pdf --output report.pdf

# 按模型分组统计
free-finder stats --group-by model

# 按日期导出CSV
free-finder stats --from 2026-07-01 --to 2026-07-18 --format csv
```

统计维度:
- 调用次数(成功/失败/重试)
- Token用量(输入/输出)
- 响应延迟(P50/P90/P99)
- 错误分布(429/500/超时)
- 模型使用占比
- 节省成本估算(对比付费模型)

### 智能路由
按任务类型自动选择最优模型:

```json
{
  "routing_rules": [
    {"task": "code_completion", "model": "qwen3-coder", "reason": "速度最优"},
    {"task": "code_generation", "model": "deepseek-coder", "reason": "质量最优"},
    {"task": "long_context", "model": "llama3.3-70b", "reason": "上下文最长"},
    {"task": "function_call", "model": "qwen3-coder", "reason": "支持tool_use"}
  ]
}
```

**输入**: 用户提供智能路由所需的指令和必要参数。
**输出**: 返回智能路由的执行结果,包含操作状态和输出数据。### 模型质量监控
持续评估模型表现,自动调整排序:

```bash
# 启动质量监控
free-finder monitor start

# 查看质量趋势
free-finder monitor trend --days 30

# 查看模型评分变化
free-finder monitor scores

# 导出质量报告
free-finder monitor report --format html --output quality.html
```

监控指标:
- 可用率(成功率/总尝试)
- 平均延迟与P99延迟
- 输出质量评分(基于基准测试)
- 限速触发频率
- 错误类型分布

## 适用场景

### 场景1 -7x24小时无人值守AI服务
用户意图: "我搭了个自动化流程,需要AI模型7x24小时稳定运行,预算为零。"

实施方案:
1. 配置4-5个免费模型组成fallback链
2. 启动后台守护进程
3. 配置多API Key负载均衡(3个以上账号)
4. 设置智能路由(按任务类型选模型)
5. 启用质量监控,每周 review 一次

### 场景2 -团队共享免费模型资源池
用户意图: "团队5个人共用免费模型,经常撞限速,需要统一管理。"

实施方案:
1. 部署free-finder作为团队共享服务
2. 配置5-10个API Key(每人注册1-2个账号)
3. 启用least_used负载均衡策略
4. 设置调用配额(每人每日上限)
5. 每周生成用量报告,优化分配

### 场景3 -模型选型长期评估
用户意图: "我们准备付费选型,想先用免费版做3个月评估。"

实施方案:
1. 启用质量监控,持续记录各模型表现
2. 定义评估维度(质量、速度、稳定性、能力)
3. 每月导出质量报告对比
4. 3个月后基于数据决定付费模型

### 场景4 -高并发场景负载均衡
用户意图: "有个活动预计峰值100 QPS,免费模型撑不住,怎么优化?"

实施方案:
1. 聚合10+个API Key(多账号)
2. 启用round_robin负载均衡
3. 配置5+个模型的fallback链
4. 设置智能路由,分流不同任务
5. 监控实时用量,动态调整

## 使用流程

### 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+(运行free-finder CLI)
- **网络**: 可访问聚合平台API
- **可选**: systemd/supervisor(守护进程管理)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| free-finder[pro] | CLI工具 | 必需 | `pip install free-finder[pro]` |
| requests | Python库 | 必需 | `pip install requests` |
| aiohttp | Python库 | 必需 | `pip install aiohttp`(异步探测) |
| prometheus-client | Python库 | 可选 | `pip install prometheus-client`(监控导出) |
| OpenRouter API | API服务 | 必需 | 注册OpenRouter账号获取免费Key |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- **聚合平台Key**: 通过环境变量或加密配置文件存储,禁止硬编码
- **多Key管理**: 使用`free-finder keys add`命令添加,自动加密存储
- **Key存储位置**: `~/.free-finder/keys.enc`(AES-256加密)
- **Key轮换**: 建议每90天轮换,使用`free-finder keys rotate`命令
- **禁止**: 在SKILL.md或脚本中硬编码任何API Key

### 可用性分类
- **分类**: MD+EXEC+CLI+DAEMON(Markdown指令+命令行工具+后台守护进程)
- **说明**: 基于Markdown的AI Skill,,高级功能需要free-finder CLI与守护进程

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| `references/style.md` | 文件 | 是 | 相关说明 |
| `assets/output.json` | 文件 | 是 | 相关说明 |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 完整专业版配置
```json
{
  "edition": "pro",
  "api": {
    "base_url": "https://openrouter.ai/api/v1",
    "timeout": 30,
    "retry": 2
  },
  "fallback_chain": [
    {"model": "qwen/qwen3-coder:free", "priority": 1},
    {"model": "deepseek/deepseek-coder:free", "priority": 2},
    {"model": "meta-llama/llama-3.3-70b-instruct:free", "priority": 3}
  ],
  "fallback_policy": {
    "trigger_on": ["429", "500", "502", "503", "timeout"],
    "max_retries": 2,
    "cooldown": 60
  },
  "daemon": {
    "enabled": true,
    "probe_interval": 60,
    "failure_threshold": 3,
    "rebuild_strategy": "live_test"
  },
  "loadbalancer": {
    "strategy": "least_used",
    "keys": [
      {"id": "key1", "weight": 1},
      {"id": "key2", "weight": 1},
      {"id": "key3", "weight": 1}
    ]
  },
  "monitor": {
    "enabled": true,
    "metrics": ["availability", "latency", "quality"],
    "benchmark_interval": 3600
  },
  "routing": {
    "enabled": true,
    "rules": [
      {"task": "code_completion", "model": "qwen3-coder"},
      {"task": "code_generation", "model": "deepseek-coder"}
    ]
  }
}
```

### 守护进程日志示例
```text
[2026-07-18 10:00:00] [INFO] 探测主模型 qwen3-coder... OK (320ms)
[2026-07-18 10:01:00] [INFO] 探测主模型 qwen3-coder... OK (310ms)
[2026-07-18 10:02:00] [WARN] 探测主模型 qwen3-coder... FAIL (429)
[2026-07-18 10:03:00] [WARN] 探测主模型 qwen3-coder... FAIL (429)
[2026-07-18 10:04:00] [WARN] 探测主模型 qwen3-coder... FAIL (429) (3/3)
[2026-07-18 10:04:01] [INFO] 触发链路重建...
[2026-07-18 10:04:05] [INFO] 测试 deepseek-coder... OK (450ms)
[2026-07-18 10:04:08] [INFO] 测试 llama3.3-70b... OK (580ms)
[2026-07-18 10:04:10] [INFO] 新主模型: deepseek-coder
[2026-07-18 10:04:11] [INFO] 配置已更新,通知Agent应用
```

## 常见问题

### Q1: 守护进程会消耗多少API额度?
A: 守护进程每60秒探测一次,单次探测消耗约10 token。24小时约消耗14400 token,对免费额度影响可忽略(<1%)。

### Q2: 多Key负载均衡是否违反平台ToS?
A: 大多数聚合平台(如OpenRouter)允许个人使用多账号,但禁止商业转售。建议阅读平台ToS,合理使用。团队场景推荐使用平台提供的团队版。

### Q3: 智能路由如何识别任务类型?
A: 通过请求特征识别: (1)system prompt关键词(如"补全代码"→code_completion); (2)输入长度(>8K→long_context); (3)是否含function定义(→function_call); (4)可自定义规则。

### Q4: 质量监控的基准测试是什么?
A: 内置100个编程任务(涵盖Python/JS/Java等多语言),每小时运行一次,记录通过率与质量评分。支持自定义基准测试集。

### Q5: fallback切换时会丢失上下文吗?
A: 不会。切换时自动重放最近N轮对话(默认10轮),新模型接续上下文。但注意: 若新模型上下文长度<原模型,可能截断早期对话。

### Q6: 如何导出统计报告给团队?
A: 运行`free-finder stats --week --format pdf --email team@example.com`,支持PDF/HTML/CSV三种格式,可直接发送邮件。

### Q7: 守护进程意外退出怎么办?
A: 推荐使用systemd或supervisor管理守护进程,实现自动重启。配置示例见`docs/systemd.service`。

### Q8: 专业版支持哪些聚合平台?
A: 支持OpenRouter、SiliconFlow、Together AI等OpenAI兼容协议的平台。配置时填写对应base_url即可。

### Q9: 如何在Kubernetes中部署?
A: 提供Helm Chart,一行命令部署: `helm install free-finder ./charts/free-finder`。支持HPA自动扩缩容。

### Q10: 专业版有SLA保障吗?
A: 专业版提供99.5%可用性SLA(基于守护进程+多Key+fallback机制)。如未达标,按比例退还月费。详细SLA条款见服务协议。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
