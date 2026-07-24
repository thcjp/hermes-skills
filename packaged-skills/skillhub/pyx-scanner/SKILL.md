---
slug: "pyx-scanner"
name: "pyx-scanner"
version: 1.0.1
displayName: "Skill安全扫描(专业版)"
summary: "企业级Skill安全检测方案，支持批量扫描、持续监控、自定义策略与团队协作审计。。Skill安全扫描专业版是一套面向安全团队与企业级场景的 AI Agent Skill 安全检测解决方案，在"
license: "Proprietary"
edition: "pro"
description: |-
  Skill安全扫描专业版是一套面向安全团队与企业级场景的 AI Agent Skill 安全检测解决方案，在免费版基础上扩展出批量扫描与队列调度、持续监控与变更通知、自定义安全策略、详细漏洞分析与修复建议、团队协作与审计日志等能力。核心能力：提供批量扫描任务编排、Skill 变更持续监控与告警、组织级安全策略与白名单管理、漏洞详情分析与修复建议、扫描结果团队协作与审计存档
tags:
  - 安全
  - 集成工具
  - 扫描
  - 企业级
  - 专业版
  - 工具
  - 效率
  - 加密
  - 运维
  - api
  - 持续监控
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"
---
# Skill安全扫描(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Skill安全扫描(专业版)支持批量扫描 | 不支持 | 支持 |
| Skill安全扫描(专业版)持续监控 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |

## 核心能力

### 能力一：批量扫描与队列调度

支持一次性提交数百个 Skill 进行批量扫描，内置队列调度避免触发限流，支持断点续扫与结果汇总.
| 批量场景 | 配置要点 | 输出形式 |
|:-----|:-----|:-----|
| 仓库全量扫描 | 从仓库清单文件读取 | 汇总报告 + 风险清单 |
| 团队 Skill 清单 | 从团队配置读取 | 按团队分组报告 |
| 依赖链扫描 | 递归扫描依赖 Skill | 依赖树 + 风险传播分析 |
| 定期复查 | 按周期自动触发 | 趋势对比报告 |

### 能力二：持续监控与变更通知
监控已扫描 Skill 的状态变化（如版本更新、新漏洞披露），变更时自动告警并触发重新扫描.
**处理**: 解析能力二：持续监控与变更通知的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回能力二：持续监控与变更通知的处理结果,包含执行状态码、结果数据和执行日志。### 能力三：自定义安全策略与白名单
根据组织安全要求，自定义判定阈值、禁止权限、强制审查项。支持白名单机制豁免特定 Skill.
**输入**: 用户提供能力三：自定义安全策略与白名单所需的指令和必要参数.
**处理**: 解析能力三：自定义安全策略与白名单的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回能力三：自定义安全策略与白名单的处理结果,包含执行状态码、结果数据和执行日志。### 能力四：详细漏洞分析与修复建议

对 CAUTION 与 FAILED 判定的 Skill，提供漏洞详情分析、影响评估、修复建议、替代方案推荐。- 验证返回数据的完整性和格式正确性
- 参考`能力二：持续监控与变更通知`的配置文档进行参数调优
### 能力五：团队协作与审计日志
扫描结果支持团队协作处理（分配、评论、状态流转），所有操作留存审计日志，满足合规要求.
**输入**: 用户提供能力五：团队协作与审计日志所需的指令和必要参数。### 能力六：CI/CD 集成门禁
将安全扫描集成到 CI/CD 流水线，新增 Skill 自动触发扫描，未通过的构建会被拦截.
**处理**: 解析能力六：CI/CD 集成门禁的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回能力六：CI/CD 集成门禁的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`能力五：团队协作与审计日志`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：企业 Skill 仓库季度审计

每季度对仓库内 200+ Skill 进行全量扫描，生成风险清单与趋势报告，追踪历史风险项的修复进展.
### 场景二：关键 Skill 持续监控

对核心业务依赖的 10 个 Skill 开启持续监控，任何版本更新或新漏洞披露立即告警，触发重新扫描.
### 场景三：多团队安全准入流程

新 Skill 引入需经过"提交申请 → 自动扫描 → 安全团队审查 → 审批存档"的标准化流程，所有步骤留存审计日志.
### 场景四：合规审计报告生成

年度合规审计需要提供 Skill 安全报告，包含扫描覆盖率、风险分布、修复及时率等指标，自动生成 PDF 报告.
### 场景五：CI/CD 自动化门禁

开发团队在 PR 中新增 Skill 依赖时，CI 自动触发扫描，FAILED 判定阻止合并，CAUTION 判定需安全团队审批.
## 使用流程

本助手需要配合扫描服务 API 与团队配置使用。请确保已配置专业版授权与 API Key.
**典型提问模板**：

```
帮我扫描仓库内所有 Skill，生成风险清单
```

```
为团队配置安全策略：禁止任何 Skill 申请文件系统写权限
```

```
监控这 10 个核心 Skill，变更时告警
```

Agent 会根据需求匹配对应的能力模块，输出"策略配置 → 扫描执行 → 结果分析 → 报告生成 → 审计存档"五段式方案.
**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | pyx-scanner处理的内容输入 |, 默认: 全部维度 |
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

| 症状 | 可能原因 | 排查方法 | 对策 |
|:---:|:---:|:---:|:---:|
| 批量扫描中断 | 限流或网络异常 | 查看扫描日志 | 启用断点续扫 |
| 监控告警未触发 | 配置错误或服务故障 | 检查监控配置 | 修复配置并测试 |
| 策略未生效 | 规则语法错误 | 查看策略加载日志 | 修正规则语法 |
| CI 门禁误拦 | 策略过严或白名单缺失 | 查看扫描详情 | 调整策略或加白名单 |
| 审计日志缺失 | 日志服务故障 | 检查日志存储 | 修复日志服务并补录 |
| 漏洞修复建议不准 | 漏洞库过时 | 更新漏洞库 | 联系扫描服务更新 |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 需能访问 scanner.pyxmate.com
- **CI/CD**: GitHub Actions / GitLab CI / Jenkins（可选）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| WebFetch 工具 | Agent工具 | 推荐 | Agent 内置工具 |
| curl | 命令行工具 | 必需 | 系统自带或安装 |
| jq | JSON处理工具 | 推荐 | 系统包管理器安装 |
| 扫描服务 API Key | 凭据 | 必需 | 联系扫描服务提供方获取 |
| 对象存储 | 存储 | 推荐 | AWS S3 / 阿里云 OSS（审计日志） |

### API Key 配置
- 本专业版需配置扫描服务 API Key，存储于环境变量 `PYX_SCANNER_API_KEY`
- CI/CD 集成的 Webhook URL 等敏感配置应存储于密钥管理服务或 CI Secrets
- 审计日志存储的访问凭据同样需要密钥管理
- 禁止在 SKILL.md 或脚本中硬编码 API Token 或 Webhook URL

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，需要exec命令行执行扫描、配置与CI/CD集成）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行企业级安全检测流程

## 案例展示

### 批量扫描配置

```yaml
# batch-scan-config.yaml
scan_targets:
  - source: repository
    path: ./skills-inventory.yaml
    recursive: true
# ...
  - source: team_config
    teams:
      - backend
      - frontend
      - data
# ...
schedule:
  type: quarterly
  retry_on_failure: true
  max_retries: 3
  retry_interval: 60s
# ...
output:
  format: [markdown, pdf]
  distribution:
    - email: security-team@company.com
    - webhook: https://hooks.slack.com/详情见说明
```

### 安全策略配置

```yaml
# security-policy.yaml
policies:
  - name: block_filesystem_write
    description: 禁止任何 Skill 申请文件系统写权限
    rule: permissions contains "filesystem.write"
    action: deny
# ...
  - name: block_network_access
    description: 网络 Skill 需安全团队审批
    rule: permissions contains "network.*"
    action: require_approval
    approver: security-team
# ...
  - name: trust_score_threshold
    description: 信任分低于 6 的 Skill 需人工审查
    rule: trust_score < 6
    action: require_review
# ...
  - name: max_risk_score
    description: 风险分超过 3 的 Skill 禁止使用
    rule: risk_score > 3
    action: deny
# ...
whitelist:
  - owner: internal-team
    reason: 内部团队开发，已通过代码审查
    expires: 2026-12-31
```

### 持续监控配置

```yaml
# monitoring-config.yaml
monitored_skills:
  - owner: anthropic
    name: web-search
    alert_on: [version_update, new_vulnerability]
# ...
  - owner: internal-team
    name: core-processor
    alert_on: [version_update, new_vulnerability, config_change]
# ...
alerts:
  channels:
    - type: slack
      webhook: ${SLACK_WEBHOOK_URL}
    - type: email
      recipients: [security-team@company.com]
# ...
  rules:
    - condition: new_vulnerability
      severity: critical
      action: immediate_scan
    - condition: version_update
      severity: info
      action: schedule_scan
```

### CI/CD 门禁配置

```yaml
# .github/workflows/skill-security.yml
name: Skill Security Gate
on:
  pull_request:
    paths:
      - 'skills/**'
# ...
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Detect new skills
        id: detect
        run: |
          NEW_SKILLS=$(git diff --name-only origin/main...HEAD | grep "^skills/" || true)
          echo "skills=$NEW_SKILLS" >> $GITHUB_OUTPUT
# ...
      - name: Run security scan
        if: steps.detect.outputs.skills != ''
        run: |
          for skill in $按流程执行; do
            owner=$(echo $skill | cut -d'/' -f2)
            name=$(echo $skill | cut -d'/' -f3)
            result=$(curl -s "https://scanner.pyxmate.com/api/v1/check/$owner/$name")
# ...
            verdict=$(echo $result | jq -r '.recommendation')
            if [ "$verdict" == "danger" ]; then
              echo "::error::Skill $owner/$name failed security scan"
              exit 1
            fi
          done
```

### 漏洞分析报告模板

```text
# ...

具体详情请参考下方内容.
## 常见问题
# ...
### Q1：批量扫描如何避免限流？
# ...
专业版内置队列调度器，默认每秒 1 个请求，遇到 429 自动退避 60 秒。可通过配置调整并发数，但建议不超过 2 并发.
# ...
### Q2：持续监控如何感知 Skill 更新？
# ...
通过定期轮询 Skill 仓库的版本信息（如 git tag、package version），与上次扫描时的版本对比，发现变化即触发重新扫描.
# ...
### Q3：自定义策略支持哪些规则？
# ...
支持基于权限、信任分、风险分、漏洞数量、依赖关系等多维度的规则。规则语法类似 CEL（Common Expression Language），支持 AND/OR/NOT 逻辑组合.
# ...
### Q4：白名单有效期多长合适？
# ...
建议最长不超过 1 年。到期后需重新评估风险并续期。内部团队开发的 Skill 可适当延长，但每年至少 review 一次.
# ...
### Q5：CI/CD 门禁失败后如何处理？
# ...
FAILED 判定阻止合并，需移除该 Skill 依赖或联系作者修复。CAUTION 判定需安全团队审批后才能合并，审批记录留存审计日志.
# ...
### Q6：审计日志保留多久？
# ...
合规要求通常为 3 年，金融行业可能要求 7 年。建议存储于低成本对象存储（如 S3 Glacier），按需检索.
# ...
### Q7：如何评估安全策略有效性？
# ...
关键指标：策略命中率（被拦截的 Skill 占比）、误报率（被拦截但实际安全的占比）、修复及时率（漏洞在 SLA 内修复的占比）。季度 review 这些指标.
# ...
### Q8：漏洞修复建议如何生成？
# ...
基于漏洞类型、Skill 用途、依赖关系等上下文，结合内置修复知识库生成。对于复杂漏洞，建议联系专业安全顾问人工分析.
# ...
### Q9：团队协作如何分工？
# ...
建议角色分工：提交者（开发者）、初审（安全工程师）、终审（安全负责人）、审计（合规团队）。每个角色有明确权限与职责.
# ...
### Q10：如何与现有安全工具集成？
# ...
本助手提供 Webhook 与 API 接口，可与 SIEM（如 Splunk）、工单系统（如 Jira）、通知系统（如 Slack）集成。具体集成方案参考各工具的对接文档.
# ...
## 错误处理
# ...
# ...
| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
# ...