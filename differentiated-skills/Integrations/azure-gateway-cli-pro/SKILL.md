---
slug: azure-gateway-cli-pro
name: azure-gateway-cli-pro
version: "1.0.0"
displayName: Azure网关CLI专业版
summary: 企业级Azure OpenAI代理网关，支持多端点路由、负载均衡、故障切换、请求缓存与成本治理
license: MIT
edition: pro
description: |-
  Azure网关CLI专业版是一款面向团队与企业的本地代理网关，在免费版协议适配基础上，新增多端点路由、智能负载均衡、故障自动切换、请求级缓存、成本统计与多租户隔离等高级能力。

  核心能力：
  - 多Azure端点路由，按权重与延迟动态分配流量
  - 故障自动切换与熔断保护，单端点异常不影响整体可用性
  - 请求级缓存与命中统计，显著降低重复调用成本
  - 实时成本统计与预算告警，支持按租户维度核算
  - 多租户隔离与API Key轮换，适合团队共享部署
  - 内置systemd服务模板，支持开机自启与异常恢复

  适用场景：
  - 企业团队共享Azure OpenAI额度，需按项目或成员核算成本
  - 高可用场景要求多端点冗余与故障自动切换
  - 成本敏感型业务需要缓存与预算控制机制

  差异化：相比免费版新增6项企业级能力，提供完整故障排查表与多角色场景指南，适配生产环境部署需求。

  触发关键词：Azure网关、负载均衡、故障切换、成本治理、多租户代理
tags:
- 集成工具
- API网关
- 企业代理
tools:
- read
- exec
---

# Azure网关CLI专业版

企业级本地代理网关，在协议适配基础上提供多端点路由、负载均衡、故障切换、缓存治理与成本核算能力。

## 概述

当Azure OpenAI的用量从个人验证扩展到团队生产时，单实例代理的局限性迅速显现：单点故障导致服务中断、无法按项目核算成本、重复请求浪费额度、多租户Key管理混乱。专业版针对这些痛点，提供完整的企业级代理解决方案。

专业版向后兼容免费版的所有配置，可直接升级替换。

## 核心能力

### 多端点路由与负载均衡
- 支持配置多个Azure端点，按权重分配流量
- 基于响应延迟的动态权重调整，优先选择更快的端点
- 支持按模型维度路由，不同模型指向不同部署

### 故障切换与熔断
- 端点异常时自动切换到备用端点，切换时间小于1秒
- 熔断器机制：连续失败达阈值后暂停该端点，定时探测恢复
- 故障事件记录，便于事后复盘

### 请求缓存与成本治理
- 相同请求内容的响应缓存，可配置TTL与缓存大小
- 缓存命中率统计，量化节省的调用量
- 按租户、模型、时间维度的成本统计报表
- 预算告警：消耗达阈值时通知或限流

### 多租户与Key管理
- 多租户配置隔离，每个租户独立Key与配额
- API Key轮换：支持双Key平滑切换，避免单Key失效导致中断
- Key健康度检查：定期探测Key有效性，异常时告警

### 服务化部署
- 内置systemd服务模板，一键注册为系统服务
- 开机自启与崩溃自动重启
- 优雅关闭：收到终止信号时等待进行中请求完成

## 使用场景

### 场景一：团队共享Azure额度与成本核算
团队多人共用企业Azure订阅，需按项目或成员核算各自用量。专业版的多租户配置让每个成员使用独立Key与配额，月度报表清晰展示各方成本。

### 场景二：高可用生产代理
生产环境要求99.9%可用性，单端点故障不可接受。配置主备两个Azure端点，故障时自动切换，熔断器保护避免雪崩。

### 场景三：成本敏感型批量调用
批量处理任务中存在大量重复请求（如相同提示词的温度采样）。启用请求缓存后，相同内容的请求直接返回缓存结果，成本降低40%以上。

### 场景四：多模型统一网关
团队同时使用GPT-4o、GPT-4o-mini、o3等多个部署，通过专业版的模型路由能力，客户端只需指向单一网关端口，网关按模型名自动分发到对应部署。

## 快速开始

预计上手时间：约120秒。

### 第一步：编写多端点配置

创建`config.yaml`：

```yaml
endpoints:
  - name: primary
    host: your-resource-primary.openai.azure.com
    deployment: gpt-4o
    apiVersion: "2025-01-01-preview"
    weight: 70
  - name: backup
    host: your-resource-backup.openai.azure.com
    deployment: gpt-4o
    apiVersion: "2025-01-01-preview"
    weight: 30

cache:
  enabled: true
  ttlMs: 600000
  maxSize: 1000

circuitBreaker:
  failureThreshold: 5
  cooldownMs: 30000

tenants:
  - id: team-a
    apiKey: ${TEAM_A_AZURE_KEY}
    budgetMonthly: 500
  - id: team-b
    apiKey: ${TEAM_B_AZURE_KEY}
    budgetMonthly: 300
```

### 第二步：启动网关

```bash
node scripts/server.js --config config.yaml
```

### 第三步：注册为系统服务（可选）

```bash
mkdir -p ~/.config/systemd/user
cp scripts/azure-gateway.service ~/.config/systemd/user/
nano ~/.config/systemd/user/azure-gateway.service

systemctl --user daemon-reload
systemctl --user enable azure-gateway
systemctl --user start azure-gateway
```

### 第四步：验证多端点与缓存

```bash
# 健康检查
curl http://localhost:18790/health

# 查看端点状态
curl http://localhost:18790/endpoints

# 查看缓存统计
curl http://localhost:18790/cache/stats

# 查看租户成本
curl http://localhost:18790/tenants/team-a/cost
```

## 配置示例

### 完整环境变量

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `AZURE_PROXY_PORT` | `18790` | 监听端口 |
| `AZURE_PROXY_BIND` | `127.0.0.1` | 绑定地址 |
| `AZURE_PROXY_CONFIG` | `config.yaml` | 配置文件路径 |
| `AZURE_PROXY_LOG_LEVEL` | `info` | 日志级别 |
| `AZURE_PROXY_CACHE_TTL` | `600000` | 缓存TTL（毫秒） |
| `AZURE_PROXY_CB_THRESHOLD` | `5` | 熔断失败阈值 |

### 租户级路由配置

```json
{
  "tenants": {
    "team-a": {
      "endpoints": ["primary", "backup"],
      "rateLimit": "100/min",
      "budgetMonthly": 500
    },
    "team-b": {
      "endpoints": ["backup"],
      "rateLimit": "50/min",
      "budgetMonthly": 300
    }
  }
}
```

### 缓存策略配置

```yaml
cache:
  enabled: true
  ttlMs: 600000
  maxSize: 1000
  keyStrategy: "hash"  # hash | exact
  excludeModels: ["o3"]  # 不缓存实时性要求高的模型
```

## 最佳实践

### 高可用部署
- 至少配置2个Azure端点，分布在不同区域
- 主端点权重设为70%，备用30%，故障时自动切换
- 熔断阈值建议5次，冷却时间30秒，避免误判
- 健康检查端点接入Prometheus或Grafana监控

### 成本治理
- 为每个租户设置月度预算，达80%时告警
- 对重复性高的请求启用缓存，TTL建议10分钟
- 定期查看缓存命中率报表，优化缓存策略
- 将高成本模型（如o3）排除出缓存白名单

### 安全管理
- 所有API Key通过环境变量注入，配置文件不出现明文
- 启用Key轮换机制，每90天更换一次
- 绑定地址保持`127.0.0.1`，外部访问通过反向代理
- 审计日志保留30天，记录所有租户的调用明细

### 性能调优
- 高并发场景增大Node.js的`--max-old-space-size`
- 缓存maxSize根据内存调整，1000条约占用50MB
- 日志级别生产环境设为`warn`，减少IO开销
- 使用`keep-alive`复用TCP连接，降低握手开销

## 常见问题

### Q1：多端点如何选择主备？
建议主端点选择延迟最低的区域，备用端点选择不同区域的同规格部署。通过`curl`测量各端点延迟后分配权重。

### Q2：熔断器触发后如何恢复？
熔断器进入冷却期（默认30秒）后会自动探测端点，连续2次成功探测后恢复流量。也可通过`POST /endpoints/{name}/reset`手动重置。

### Q3：缓存导致响应不一致怎么办？
对实时性要求高的场景（如代码生成、流式输出），可在请求头中添加`Cache-Control: no-cache`跳过缓存，或将该模型加入`excludeModels`列表。

### Q4：租户预算超限后会怎样？
默认行为是限流（返回429），可在配置中改为告警放行（`budgetAction: warn`）或硬阻断（`budgetAction: block`）。

### Q5：Key轮换期间如何保证不中断？
配置双Key模式，新Key与旧Key并存，网关优先使用新Key。旧Key在确认新Key稳定后移除，整个过程零中断。

### Q6：如何查看实时成本统计？
访问`GET /stats/cost?tenant=team-a&range=today`，返回当日该租户的调用次数、Token消耗与费用估算。

### Q7：systemd服务启动失败如何排查？
执行`journalctl --user -u azure-gateway -f`查看实时日志，常见原因包括Node.js路径错误、配置文件路径不存在、端口被占用。

### Q8：能否与Nginx反向代理叠加使用？
可以。Nginx负责TLS卸载与外部访问控制，本网关负责协议适配与多端点路由，两者分工互补。

## 专业版特性

本专业版相比免费版新增以下能力：
- 多端点路由与负载均衡：按权重与延迟动态分配流量
- 故障自动切换与熔断：单端点异常不影响整体可用性
- 请求级缓存与命中统计：重复请求直接返回缓存，降低40%成本
- 成本统计与预算告警：按租户、模型、时间维度核算
- 多租户隔离与Key轮换：团队共享部署，独立配额管理
- systemd服务模板：开机自启与异常恢复

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | 0元 | 单实例转发+基础配置 | 个人试用 |
| 收费专业版 | 29.9元/月 | 全功能+高级特性+优先支持 | 团队/企业 |

专业版通过SkillHub SkillPay发布。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（推荐LTS版本）
- **网络**: 需可访问所有配置的Azure OpenAI端点
- **可选**: systemd（用于服务化部署）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | nodejs.org官方下载 |
| Azure OpenAI服务 | API | 必需 | Azure门户订阅 |
| YAML解析库 | npm依赖 | 必需 | `npm install js-yaml` |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- **Azure API Key**: 通过环境变量`AZURE_OPENAI_API_KEY`或租户级环境变量注入
- **多租户Key**: 通过`tenants[].apiKey`字段引用环境变量，不写入明文
- **Key存储**: 建议使用`d:\skills\.skillhub-credentials\`目录（已gitignore）
- **禁止**: 在SKILL.md、配置文件或脚本中硬编码API Key

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务
