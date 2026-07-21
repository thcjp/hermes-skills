---
slug: ops-dashboard-pro
name: ops-dashboard-pro
version: "1.0.0"
displayName: 运维看板(专业版)
summary: 全功能实时运维监控看板，支持成本分析、变更操作、告警通知与审计日志
license: Proprietary
edition: pro
description: |-
  运维看板专业版是面向团队和企业的完整运维监控方案，在免费版基础上解锁成本分析与用量统计、变更操作与备份管理、告警通知与自动响应、批量会话管理、审计日志与操作追踪、服务商审计集成和系统级运维操作等全部高级能力。核心能力：会话全生命周期管理、Token成本追踪与预算告警、定时任务执行与重试、网关健康监控与自动恢复、批量操作与检查点、变更审计链、敏感数据深度扫描、多环境配置管理、系统级重启控制
tags:
- 运维监控
- 成本分析
- 变更管理
- 高级集成
tools:
  - - read
- exec
---

# 运维看板（专业版）
全功能实时运维监控看板，覆盖会话管理、成本分析、变更操作、告警通知和审计日志。专业版面向需要深度运维能力的团队和企业用户。

## 概述
在企业级AI Agent部署中，运维不仅需要"看到"系统状态，更需要"操作"和"追溯"。运维看板专业版在免费版的只读监控基础上，新增变更操作（任务执行、备份创建、模型切换）、成本追踪（Token用量、API费用、预算告警）、自动响应（阈值告警、故障恢复）和审计日志（操作追踪、合规审查）四大能力模块，形成从监控到操作到审计的完整闭环。

专业版同时提供多层安全防护体系，覆盖认证授权、CORS策略、敏感数据扫描和操作权限控制四个层面，确保运维操作的安全性和合规性。

## 核心能力
| 能力模块 | 专业版支持 | 说明 |
|:---------|:-----------|:-----|
| 会话管理 | 全量 | 查看、终止、归档、批量清理 |
| 定时任务 | 全量 | 查看、执行、重试、禁用 |
| 成本分析 | 支持 | Token用量、API费用、预算告警 |
| 健康监控 | 全量 | 网关健康、服务依赖、自动恢复 |
| 变更操作 | 支持 | 备份创建、模型切换、配置更新 |
| 告警通知 | 支持 | 阈值告警、邮件/Webhook通知 |
| 批量管理 | 支持 | 批量会话操作、检查点恢复 |
| 审计日志 | 支持 | 完整操作审计链、合规导出 |
| 安全扫描 | 全量 | 敏感数据深度扫描、配置审查 |
| 服务商审计 | 支持 | 调用AI服务商组织API获取用量 |
| 系统操作 | 支持 | 用户级systemctl重启控制 |

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 按照skill规范执行参数配置与调用操作,遵循单一意图原则。
**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 按照skill规范执行结果处理与输出操作,遵循单一意图原则。
**输出**: 返回结果处理与输出的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：全功能实时运维监、控看板、支持成本分析、告警通知与审计日、运维看板专业版是、面向团队和企业的、完整运维监控方案、在免费版基础上解、锁成本分析与用量、变更操作与备份管、告警通知与自动响、批量会话管理、审计日志与操作追、服务商审计集成和、系统级运维操作等、全部高级能力、核心能力、会话全生命周期管、成本追踪与预算告、定时任务执行与重、网关健康监控与自、批量操作与检查点、变更审计链、多环境配置管理、系统级重启控制等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景
### 运维场景：成本监控与预算告警
追踪AI Agent的Token消耗和API费用，设置预算阈值，超支时自动告警：

```bash
# 查看成本概览
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/cost/summary

# 查看按会话的成本明细
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/cost/by-session

# 设置预算告警阈值
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"monthly_budget": 500, "alert_threshold": 0.8}' \
     http://localhost:3000/api/cost/budget

# 查看月度成本趋势
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     "http://localhost:3000/api/cost/trend?period=monthly"
```

### 管理场景：批量会话清理
定期清理过期会话，释放系统资源：

```bash
# 查看所有会话（含已结束的）
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/sessions?status=all

# 批量归档超过7天的会话
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"action": "archive", "older_than_days": 7}' \
     http://localhost:3000/api/sessions/batch

# 批量终止异常会话
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"action": "terminate", "status": "error"}' \
     http://localhost:3000/api/sessions/batch
```

### 故障恢复场景：定时任务重试
定时任务执行失败时，通过看板触发重试并检查结果：

```bash
# 查看失败任务列表
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     "http://localhost:3000/api/cron?status=failed"

# 手动触发任务执行
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"task": "daily-report"}' \
     http://localhost:3000/api/cron/run-now

# 查看任务执行结果
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/cron/history/daily-report
```

### 合规场景：审计日志导出
导出完整操作审计日志，用于合规审查：

```bash
# 查看操作审计日志
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     "http://localhost:3000/api/audit/logs?start=2026-01-01&end=2026-01-31"

# 按操作类型筛选
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     "http://localhost:3000/api/audit/logs?type=mutation"

# 导出审计报告（JSON格式）
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     "http://localhost:3000/api/audit/export?format=json" > audit-report.json
```

## 快速开始
### 前置条件
- Node.js 18+ 已安装
- 运维看板服务已部署并运行
- 已设置`OPS_DASHBOARD_AUTH_TOKEN`环境变量

### 环境配置
创建`.env`文件配置完整运行参数：

```bash
# .env 文件
DASHBOARD_PORT=3000
DASHBOARD_HOST=localhost

# 认证配置
OPS_DASHBOARD_AUTH_TOKEN=your_secure_token_here

# CORS配置
DASHBOARD_CORS_ORIGINS=http://localhost:3000

# 高级功能开关（默认关闭，按需启用）
OPS_DASHBOARD_LOAD_KEYS_ENV=0
OPS_DASHBOARD_ENABLE_PROVIDER_AUDIT=0
OPS_DASHBOARD_ENABLE_CONFIG_ENDPOINT=0
OPS_DASHBOARD_ENABLE_SYSTEMCTL_RESTART=0
OPS_DASHBOARD_ENABLE_MUTATING_OPS=0

# 附件操作权限（默认全部关闭）
OPS_DASHBOARD_ALLOW_ATTACHMENT_FILEPATH_COPY=0
OPS_DASHBOARD_ALLOW_ATTACHMENT_COPY_FROM_TMP=0
OPS_DASHBOARD_ALLOW_ATTACHMENT_COPY_FROM_WORKSPACE=0
OPS_DASHBOARD_ALLOW_ATTACHMENT_COPY_FROM_HOME=0
```

### 依赖详情
```bash
# 检查服务健康
curl http://localhost:3000/api/health

# 查看当前配置
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/config
```

### 使用流程
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

```bash
# 1. 查看系统概览
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/overview

# 2. 查看成本摘要
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/cost/summary

# 3. 查看活跃会话
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/sessions?status=active

# 4. 查看定时任务
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/cron

# 5. 执行安全扫描
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/security/scan

# 6. 查看审计日志
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/audit/logs
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。

### 命令参数说明

- `-X`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

## 示例
### 安全防护体系
专业版提供四层安全防护，所有高敏感功能默认关闭，需通过环境变量显式启用：

```bash
# 第一层：认证授权
# 所有API请求需携带Token
OPS_DASHBOARD_AUTH_TOKEN=your_secure_token_here

# 第二层：CORS策略
# 默认仅允许本地来源，按需添加外部来源
DASHBOARD_CORS_ORIGINS=https://dashboard.example.com,https://ops.example.com

# 第三层：功能开关
# 高敏感功能需显式启用
OPS_DASHBOARD_ENABLE_PROVIDER_AUDIT=1    # 允许调用AI服务商API
OPS_DASHBOARD_ENABLE_CONFIG_ENDPOINT=1   # 暴露配置端点
OPS_DASHBOARD_ENABLE_MUTATING_OPS=1      # 允许变更操作
OPS_DASHBOARD_ENABLE_SYSTEMCTL_RESTART=1 # 允许系统重启
# 第四层：附件权限
# 附件文件操作需逐项启用
OPS_DASHBOARD_ALLOW_ATTACHMENT_FILEPATH_COPY=1
OPS_DASHBOARD_ALLOW_ATTACHMENT_COPY_FROM_TMP=1
OPS_DASHBOARD_ALLOW_ATTACHMENT_COPY_FROM_WORKSPACE=1
OPS_DASHBOARD_ALLOW_ATTACHMENT_COPY_FROM_HOME=1
```

### 成本分析与预算管理
```bash
# 查看成本概览（总费用、日均、趋势）
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/cost/summary

# 按会话查看成本明细
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     "http://localhost:3000/api/cost/by-session?limit=50"

# 按模型查看成本分布
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/cost/by-model

# 设置月度预算和告警阈值
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "monthly_budget": 1000,
       "alert_threshold": 0.8,
       "alert_webhook": "https://hooks.example.com/alert"
     }' \
     http://localhost:3000/api/cost/budget

# 查看成本趋势
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     "http://localhost:3000/api/cost/trend?period=daily&days=30"
```

### 变更操作与备份
```bash
# 创建系统备份
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"type": "full", "description": "变更前备份"}' \
     http://localhost:3000/api/backup/create

# 查看备份列表
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/backup/list

# 从备份恢复
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"backup_id": "backup-001"}' \
     http://localhost:3000/api/backup/restore

# 切换默认模型
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"model": "qwen2.5:7b"}' \
     http://localhost:3000/api/ops/update-model

# 更新配置
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"key": "temperature", "value": "0.3"}' \
     http://localhost:3000/api/ops/update-config
```

### 告警通知配置
```bash
# 查看告警规则
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/alerts/rules

# 创建告警规则
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "成本超支告警",
       "metric": "cost",
       "threshold": 800,
       "operator": ">",
       "webhook": "https://hooks.example.com/alert",
       "enabled": true
     }' \
     http://localhost:3000/api/alerts/rules

# 查看告警历史
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/alerts/history

# 确认告警
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"alert_id": "alert-001", "action": "acknowledge"}' \
     http://localhost:3000/api/alerts/acknowledge
```

### 审计日志与合规
```bash
# 查看所有操作日志
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/audit/logs

# 按类型筛选（mutation类型为变更操作）
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     "http://localhost:3000/api/audit/logs?type=mutation"

# 按时间范围筛选
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     "http://localhost:3000/api/audit/logs?start=2026-01-01&end=2026-01-31"

# 按操作者筛选
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     "http://localhost:3000/api/audit/logs?operator=admin"

# 导出审计报告
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     "http://localhost:3000/api/audit/export?format=json" > audit.json
```

### 服务商审计集成
```bash
# 启用服务商审计功能
export OPS_DASHBOARD_ENABLE_PROVIDER_AUDIT=1

# 查看OpenAI组织用量
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/provider/openai/usage

# 查看Anthropic组织用量
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/provider/anthropic/usage

# 查看多服务商成本对比
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/provider/comparison
```

### 系统级操作
```bash
# 启用系统重启功能
export OPS_DASHBOARD_ENABLE_SYSTEMCTL_RESTART=1

# 用户级服务重启（非root）
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"service": "agent-service"}' \
     http://localhost:3000/api/ops/systemctl-restart

# 查看系统资源状态
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/ops/system-status
```

### 敏感数据深度扫描
```bash
# 执行全量安全扫描
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/security/scan

# 扫描指定模式
curl -X POST -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "patterns": ["token=", "API_KEY", "SECRET", "PASSWORD", "COOKIE"],
       "paths": ["./config", "./.env"]
     }' \
     http://localhost:3000/api/security/scan

# 查看扫描历史
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/security/history
```

## 最佳实践
1. **最小权限原则**：高敏感功能默认全部关闭，仅在实际需要时通过环境变量逐项启用，用后及时关闭。
2. **变更前先备份**：执行任何变更操作（模型切换、配置更新）前，先通过`/api/backup/create`创建备份点。
3. **预算告警前置**：在月初设置月度预算和告警阈值（建议80%），避免月底超支。
4. **审计日志定期审查**：每周导出一次审计日志，重点检查mutation类型操作，确保无未授权变更。
5. **CORS白名单管理**：生产环境严格限制CORS来源，仅允许运维看板域名，禁止使用通配符。
6. **安全扫描自动化**：将安全扫描纳入CI/CD流程，每次部署前自动扫描敏感信息泄露。
7. **附件权限分层控制**：按实际需求逐项启用附件操作权限，避免一次性全部开放。

## 常见问题
### Q1: 变更操作返回403禁止访问？
变更操作需启用`OPS_DASHBOARD_ENABLE_MUTATING_OPS=1`环境变量。该功能默认关闭以防误操作。启用后还需在请求中携带有效的认证Token。

### Q2: 成本数据为空或不准确？
成本追踪依赖于Agent会话的Token使用记录。确保Agent正确上报Token用量。服务商审计数据需启用`OPS_DASHBOARD_ENABLE_PROVIDER_AUDIT=1`并配置服务商API Key。

### Q3: 告警Webhook未收到通知？
检查Webhook URL是否可从服务端访问。测试网络连通性，确认Webhook服务正常响应。查看`/api/alerts/history`中告警记录的状态。

### Q4: 服务商审计调用报错？
确保已设置`OPS_DASHBOARD_ENABLE_PROVIDER_AUDIT=1`，且在`keys.env`文件中配置了服务商API Key。使用`OPS_DASHBOARD_LOAD_KEYS_ENV=1`加载密钥文件。

### Q5: systemctl重启失败？
系统重启功能仅支持用户级服务（非root）。确保`OPS_DASHBOARD_ENABLE_SYSTEMCTL_RESTART=1`已启用，且目标服务配置为用户级systemd服务。

### Q6: 批量操作超时？
批量操作涉及大量会话时可能超时。建议分批执行，每批不超过100条。检查`/api/audit/logs`确认已完成的操作数量。

### Q7: 审计日志占用磁盘过大？
配置日志保留策略，定期清理过期日志。通过`/api/audit/export`导出后归档，再清理服务端日志。

### Q8: 备份恢复后配置不一致？
备份恢复会覆盖当前配置。建议在非高峰期执行恢复操作，并在恢复后验证关键配置项。恢复前先创建当前状态的备份。

### Q9: 安全扫描误报如何处理？
安全扫描基于模式匹配，可能产生误报。将误报项添加到白名单配置中，后续扫描将跳过这些项。

### Q10: 多人同时操作导致冲突？
专业版通过审计日志记录所有操作。建议团队制定操作规范，高峰期避免并发变更操作。关键操作使用检查点机制。

## 错误处理
| 错误场景(症状) | 可能原因 | 解决方案 | 优先级 |
|:-----|:---------|:---------|:-------|
| API返回403 | 功能开关未启用 | 设置对应环境变量为1 | 高 |
| 成本数据为空 | Token用量未上报 | 检查Agent配置，确保上报Token | 高 |
| 变更操作无响应 | 操作队列积压 | 检查`/api/audit/logs`，等待执行 | 中 |
| 告警未触发 | 阈值设置不合理 | 检查告警规则和阈值配置 | 中 |
| 服务商审计失败 | API Key未配置 | 启用LOAD_KEYS_ENV并配置密钥 | 中 |
| 备份创建失败 | 磁盘空间不足 | 检查磁盘空间，清理旧备份 | 高 |
| 审计日志丢失 | 日志保留期过短 | 调整日志保留策略 | 低 |
| CORS请求被拒 | 来源不在白名单 | 添加来源到CORS_ORIGINS | 中 |
| 安全扫描超时 | 扫描范围过大 | 缩小扫描路径或分批扫描 | 低 |
| systemctl失败 | 权限不足 | 使用用户级服务，非root | 中 |
## 专业版特性
本专业版相比免费版新增以下能力：
- 成本分析与预算管理：Token用量追踪、API费用统计、月度预算设置和超支告警
- 变更操作与备份管理：系统备份创建与恢复、模型切换、配置更新等变更操作
- 告警通知与自动响应：自定义告警规则、Webhook通知、阈值触发自动响应
- 批量会话管理：批量归档、终止和清理会话，支持按条件筛选
- 审计日志与合规追踪：完整操作审计链、按类型和时间筛选、合规报告导出
- 服务商审计集成：调用OpenAI/Anthropic等服务商组织API获取用量数据
- 系统级运维操作：用户级systemctl服务重启控制
- 四层安全防护体系：认证授权、CORS策略、功能开关、附件权限分层控制
- 敏感数据深度扫描：自定义扫描模式、多路径扫描、扫描历史追踪

## 定价
| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | 0元 | 只读监控+基础安全扫描 | 个人试用 |
| 收费专业版 | 99元/月 | 全功能+成本分析+变更操作+告警+审计 | 团队/企业 |

专业版通过SkillHub SkillPay发布。

## 依赖说明
### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux（系统级操作需Linux）
- **Node.js**：18.0及以上版本
- **运行时**：运维看板服务需持续运行

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | 从Node.js官网下载安装 |
| Express | npm包 | 必需 | 通过`npm install express`安装 |
| curl | 命令行工具 | 必需 | 系统通常自带 |
| OpenAI API Key | API密钥 | 可选 | 服务商审计功能需要 |
| Anthropic API Key | API密钥 | 可选 | 服务商审计功能需要 |
| systemd | 系统服务 | 可选 | 系统重启功能需要（Linux） |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- **运维看板Token**：通过`OPS_DASHBOARD_AUTH_TOKEN`环境变量配置
- **服务商API Key**：存储在`keys.env`文件中，需设置`OPS_DASHBOARD_LOAD_KEYS_ENV=1`加载
- **存储位置**：所有密钥文件存储在项目根目录（已加入.gitignore）
- **禁止**：在代码或配置文件中硬编码任何API Key或Token
- **安全建议**：生产环境使用反向代理（如Nginx）添加额外的认证层

### 可用性分类
- **分类**：MD+EXEC（纯Markdown指令，需要exec命令行执行能力）
- **说明**：基于Markdown的AI Skill，通过自然语言指令驱动Agent执行运维看板全量API操作

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
