---
slug: "security-audit"
name: "security-audit"
version: 1.0.1
displayName: "Security Audit"
summary: "SkillHub部署全面安全审计,扫暴露凭据与开放端口"
license: "Proprietary"
description: |-
  Comprehensive security auditing for SkillHub deployments。Scans for
  exposed credentials, open por。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标.
tags:
  - Security
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tools: ["read", "exec"]
tags: "安全,加密,工具"
category: "Security"
---
# Security Audit

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |
| 零日漏洞检测与防护规则下发 | 不支持 | 支持 |

## 核心能力

- Comprehensive security auditing for SkillHub deployments
- Scans for exposed credentials, open ports, misconfigured services
- CVE关联分析与漏洞优先级排序
- 安全基线合规审计（CIS Benchmarks / OWASP Top 10）
- 批量资产风险评分与威胁情报订阅
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 部署安全扫描 | SkillHub部署配置 | 暴露面和安全漏洞报告 |
| 配置审计 | 服务器和服务配置 | 安全配置基线和合规检查 |
| 漏洞修复建议 | 扫描结果和漏洞列表 | 修复优先级和操作指南 |

**不适用于**：非SkillHub部署的其他平台安全审计

## 使用流程

### 阶段一：信息收集与资产识别

1. 确认审计目标范围（部署目录、服务端口、配置文件路径）
2. 收集资产清单：运行中的进程、监听端口、环境变量、挂载卷
3. 扫描文件系统中的敏感文件（`.env`、`config.yml`、`credentials.json`、`*.pem`、`*.key`）

```bash
# 示例：快速识别暴露的凭据文件
find /app -type f \( -name ".env*" -o -name "*.pem" -o -name "*.key" -o -name "credentials*" \) 2>/dev/null
```

### 阶段二：漏洞扫描与凭据检测

4. 执行凭据泄露扫描，使用正则匹配常见密钥模式：
   - AWS Access Key: `AKIA[0-9A-Z]{16}`
   - AWS Secret Key: 40位Base64字符串
   - GitHub Token: `gh[pousr]_[A-Za-z0-9]{36}`
   - 私钥文件头: `-----BEGIN RSA PRIVATE KEY-----`
   - 数据库连接串: `mongodb://user:pass@host`
   - JWT Secret: 高熵字符串出现在 `SECRET_KEY`、`JWT_SECRET` 变量中
5. 执行端口扫描，识别非必要的开放端口（如 22/SSH、3306/MySQL、6379/Redis 对公网暴露）
6. 检查服务配置基线：TLS版本、密码套件、CORS策略、认证开关

### 阶段三：CVE关联与风险评分

7. 将扫描发现的组件版本与CVE数据库关联，匹配已知漏洞
8. 按CVSS v3.1评分对漏洞排序：Critical (9.0+)、High (7.0-8.9)、Medium (4.0-6.9)、Low (0.1-3.9)
9. 结合资产暴露面计算实际风险评分：`Risk = CVSS × Exposure Factor × Asset Value`

### 阶段四：报告生成与修复建议

10. 生成结构化审计报告，包含发现项、风险等级、修复建议、验证方法
11. 提供修复优先级矩阵：按"风险等级 × 修复成本"排序
12. 输出可执行的修复脚本或配置补丁

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| target | string | 是 | 审计目标URL或配置路径 |
| audit_type | string | 否 | 审计类型, 可选: deploy/config/vuln, 默认: deploy |
| scan_depth | string | 否 | 扫描深度, 可选: quick/standard/deep, 默认: standard |
| output_format | string | 否 | 报告格式, 可选: json/markdown/html, 默认: markdown |
| exclude_paths | string[] | 否 | 排除扫描的路径列表, 如 node_modules、.git |
| severity_threshold | string | 否 | 最低报告严重级别, 可选: critical/high/medium/low/info, 默认: medium |

## 输出格式

The audit produces a report with:

| Level | Description |
|:----:|:----:|
| 🔴 CRITICAL | Immediate action required (exposed credentials) |
| 🟠 HIGH | Significant risk, fix soon |
| 🟡 MEDIUM | Moderate concern |
| 🟢 INFO | FYI, no action needed |

### 报告结构示例

```json
{
  "audit_id": "audit-20260724-001",
  "target": "/app/skillhub-deploy",
  "scan_summary": {
    "total_findings": 12,
    "critical": 2,
    "high": 4,
    "medium": 5,
    "low": 1
  },
  "findings": [
    {
      "id": "FIND-001",
      "severity": "CRITICAL",
      "category": "credential_exposure",
      "title": "AWS Access Key detected in .env file",
      "description": "AKIAIOSFODNN7EXAMPLE found at line 3 of /app/.env",
      "evidence": "AKIA[0-9A-Z]{16}",
      "remediation": "Rotate the key immediately, move secrets to a vault (AWS Secrets Manager / HashiCorp Vault), add .env to .gitignore",
      "cvss_score": 9.1,
      "cve_refs": []
    }
  ],
  "compliance_status": {
    "cis_benchmark": "62% compliant (8/13 checks passed)",
    "owasp_top10": "A05:2021 - Security Misconfiguration detected"
  }
}
```

## 安全基线合规检查清单

### CIS Benchmark 关键检查项

| 检查项 | 检查方法 | 合规标准 |
|:------|:------|:------|
| 禁止root容器运行 | 检查 Dockerfile USER 指令 | USER 指令设置为非root用户 |
| 最小权限文件系统 | 检查文件权限 | 配置文件权限 ≤ 640，密钥文件 ≤ 600 |
| 网络端口最小化 | 扫描监听端口 | 仅暴露业务必需端口（80/443） |
| 环境变量无敏感信息 | 扫描 env 与 config | 敏感凭据不在明文环境变量中 |
| TLS 配置合规 | 检查 TLS 版本与密码套件 | TLS ≥ 1.2，禁用 RC4/DES/3DES |
| 依赖版本无已知CVE | 比对 CVE 数据库 | 无 Critical/High 级别未修复CVE |

### OWASP Top 10 映射

| OWASP 类别 | 审计检测点 |
|:------|:------|
| A01 - 权限控制失效 | API端点鉴权检查、垂直/水平越权测试 |
| A02 - 加密机制失效 | 传输加密（TLS）、存储加密（at-rest）、密钥管理 |
| A03 - 注入 | 输入验证、参数化查询、ORM使用检查 |
| A05 - 安全配置错误 | 默认凭据、错误信息泄露、目录列表 |
| A07 - 身份认证失效 | 密码策略、会话管理、MFA支持 |

## CI/CD 集成指南

将安全审计集成到CI/CD流水线中，实现每次部署前的自动安全门禁：

```yaml
# GitHub Actions 示例
- name: Security Audit
  run: |
    # 触发安全审计技能
    echo '{"target":"./deploy","audit_type":"deploy","scan_depth":"standard"}' | skill exec security-audit
  env:
    SEVERITY_THRESHOLD: high  # CI中仅阻断High及以上
    
- name: Security Gate
  run: |
    # 检查审计结果，存在Critical则中止部署
    if [ $(jq '.scan_summary.critical' audit-report.json) -gt 0 ]; then
      echo "Deployment blocked: Critical security findings detected"
      exit 1
    fi
```

### CI/CD 集成最佳实践

- **Pre-commit Hook**: 在代码提交前执行快速凭据扫描（scan_depth=quick），阻断密钥泄露
- **PR 阶段**: 执行标准扫描（scan_depth=standard），在PR评论中展示发现项
- **Release 阶段**: 执行深度扫描（scan_depth=deep），生成完整合规报告
- **定时巡检**: 每日定时对新发现的CVE执行增量扫描，订阅威胁情报更新

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 工具依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 常见问题

### Q1: 如何开始使用Security Audit？
A: 首先确定审计目标的路径或URL，然后指定审计类型（deploy/config/vuln）。例如：对 `/app/deploy` 目录执行部署安全扫描，命令为 `audit --target /app/deploy --audit_type deploy`。首次使用建议先用 `scan_depth=quick` 进行快速扫描以了解整体安全状况，再逐步深入。

### Q2: 扫描发现大量误报怎么办？
A: 可以通过以下方式减少误报：（1）使用 `exclude_paths` 排除测试目录和依赖目录（如 `node_modules`、`test`、`__tests__`）；（2）提高 `severity_threshold` 到 `high` 过滤低优先级发现；（3）在配置文件中添加已知安全的凭据白名单（如示例密钥 `AKIAIOSFODNN7EXAMPLE`）。

### Q3: 审计报告中的CVE信息如何更新？
A: CVE数据库通过威胁情报订阅实时更新。付费版支持自动订阅NVD（National Vulnerability Database）和厂商安全公告，每日增量同步新发现的漏洞。免费版使用内置CVE快照，建议每月手动更新一次。

### Q4: 如何验证修复是否有效？
A: 修复后重新执行相同参数的审计扫描，对比两次报告的 `scan_summary` 字段。确认对应 `findings` 条目状态变为 `resolved`。对于凭据泄露类发现，还需在外部服务（如AWS IAM控制台）确认密钥已轮换且旧密钥已禁用。

### Q5: 审计过程中是否会影响线上服务？
A: 安全审计采用只读扫描模式，不修改任何文件或配置。端口扫描使用非侵入式SYN扫描，不会建立完整TCP连接。对于生产环境，建议在低峰期执行 `scan_depth=deep` 的深度扫描以避免潜在的负载影响。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

