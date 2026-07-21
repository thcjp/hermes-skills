---
slug: free-resource-finder-pro
name: free-resource-finder-pro
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
全功能免费AI资源管理工具,在免费版发现与切换能力基础上,扩展自动fallback、后台守护、负载均衡、成本分析与质量监控,适合长期无人值守场景。

## 概述
在生产环境中使用免费AI模型,最大的挑战不是"能不能用",而是"能不能稳定用"。免费模型普遍存在限速、不稳定、随时下线等问题,直接用于业务会导致服务中断。专业版围绕"稳定性"构建完整能力矩阵,通过自动fallback、后台守护、负载均衡三大机制,让免费模型也能支撑7x24小时服务。

专业版兼容免费版的配置与数据,可直接升级,无需重新配置。

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

### 调用统计与成本分析
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

### 模型质量监控
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

## 使用场景
### 场景1:7x24小时无人值守AI服务
用户意图: "我搭了个自动化流程,需要AI模型7x24小时稳定运行,预算为零。"

实施方案:
1. 配置4-5个免费模型组成fallback链
2. 启动后台守护进程
3. 配置多API Key负载均衡(3个以上账号)
4. 设置智能路由(按任务类型选模型)
5. 启用质量监控,每周 review 一次

### 场景2:团队共享免费模型资源池
用户意图: "团队5个人共用免费模型,经常撞限速,需要统一管理。"

实施方案:
1. 部署free-finder作为团队共享服务
2. 配置5-10个API Key(每人注册1-2个账号)
3. 启用least_used负载均衡策略
4. 设置调用配额(每人每日上限)
5. 每周生成用量报告,优化分配

### 场景3:模型选型长期评估
用户意图: "我们准备付费选型,想先用免费版做3个月评估。"

实施方案:
1. 启用质量监控,持续记录各模型表现
2. 定义评估维度(质量、速度、稳定性、能力)
3. 每月导出质量报告对比
4. 3个月后基于数据决定付费模型

### 场景4:高并发场景负载均衡
用户意图: "有个活动预计峰值100 QPS,免费模型撑不住,怎么优化?"

实施方案:
1. 聚合10+个API Key(多账号)
2. 启用round_robin负载均衡
3. 配置5+个模型的fallback链
4. 设置智能路由,分流不同任务
5. 监控实时用量,动态调整

## 快速开始
### 依赖说明
```bash
# 安装专业版
pip install free-finder[pro]

# 初始化配置
free-finder init --edition pro

# 配置主API Key
free-finder config set api.key "$OPENROUTER_API_KEY"
```

### 步骤2:配置fallback链
```bash
# 自动生成fallback链(基于质量排序)
free-finder chain auto-generate --top 5

# 手动添加fallback
free-finder chain add --model deepseek-coder --priority 2

# 查看当前链路
free-finder chain list
```

### 步骤3:启动守护进程
```bash
# 后台启动守护
nohup free-finder daemon > ~/.free-finder/daemon.log 2>&1 &

# 验证守护运行
free-finder daemon --status
```

### 步骤4:配置负载均衡
```bash
# 添加多个Key
free-finder keys add --provider openrouter --key "$KEY1"
free-finder keys add --provider openrouter --key "$KEY2"
free-finder keys add --provider openrouter --key "$KEY3"

# 设置负载均衡策略
free-finder config set loadbalancer.strategy least_used
```

### 步骤5:启用监控
```bash
# 启动质量监控
free-finder monitor start

# 验证监控运行
free-finder monitor status
```

## 示例
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

## 最佳实践
### fallback链设计
| 链路位置 | 模型特征 | 说明 |
| --- | --- | --- |
| 主模型 | 质量最高,速度 acceptable | 日常首选 |
| fallback 1 | 质量接近主模型 | 主模型限速时顶上 |
| fallback 2 | 上下文更长 | 长文本场景备用 |
| fallback 3 | 稳定性最高 | 极端情况兜底 |
| 末位 | 聚合平台自动路由 | 最后保障 |

### 守护进程调优
- 探测间隔: 60秒(平衡灵敏度与API消耗)
- 失败阈值: 连续3次(避免误判)
- 重建策略: live_test(实测可用性,非依赖缓存)
- 冷却时间: 60秒(避免频繁切换)
- 通知机制: 邮件/ webhook(专业版支持)

### 多Key管理要点
- Key来源: 不同账号注册(避免同一IP批量注册被风控)
- Key轮换: 每90天更换一次
- Key监控: 监控各Key用量,避免单Key耗尽
- Key安全: 存储于加密配置文件,禁止明文
- 备用Key: 预留2-3个未启用Key,应急使用

### 成本分析维度
| 维度 | 计算方式 | 价值 |
| --- | --- | --- |
| 节省金额 | 免费调用次数 × 付费模型单价 | 量化免费价值 |
| 有效调用率 | 成功调用 / 总调用 | 评估稳定性 |
| 平均延迟 | 总延迟 / 成功调用 | 评估用户体验 |
| 重试开销 | 重试次数 × 单次成本 | 评估浪费 |
| 模型分布 | 各模型调用占比 | 优化路由策略 |

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

## 专业版特性
本专业版相比免费版新增以下能力:
- 自动fallback链: 主模型失败自动切换,保障服务连续性
- 后台守护进程: 实时探测可用性,自动重建链路
- 多API Key负载均衡: 聚合多账号额度,突破单账号限速
- 调用统计与成本分析: 详细用量报告与节省金额估算
- 模型质量监控: 持续评估表现,自动调整排序
- 智能路由: 按任务类型自动选择最优模型
- 团队共享模式: 统一管理团队资源池
- 优先支持: 专属技术支持通道,SLA响应

## 定价
| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 发现+切换+基础排查 | 个人试用 |
| 收费专业版 | ¥29.9/月 | 全功能+自动化+监控+优先支持 | 团队/企业 |

专业版通过SkillHub SkillPay发布。

## 依赖说明
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
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务,高级功能需要free-finder CLI与守护进程

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制
- 需要API Key，无Key环境无法使用
