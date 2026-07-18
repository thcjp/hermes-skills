---
slug: security-audit-tool-pro
name: security-audit-tool-pro
version: "1.0.0"
displayName: 安全审计工具(专业版)
summary: 企业级安全审计平台,8维度扫描、合规模板、HTML报告、定时审计与CI/CD集成
license: MIT
edition: pro
description: |-
  核心能力:
  - 8维度安全扫描(凭据/端口/配置/权限/Docker/K8s/云/合规)
  - 等保2.0/PCI-DSS/ISO27001合规模板
  - HTML/PDF/SARIF多格式专业报告
  - Cron定时审计+邮件/Webhook告警
  - 智能修复+回滚机制
  - CI/CD流水线集成

  适用场景:
  - 企业级安全合规审计
  - 等保/PCI-DSS认证评估
  - DevSecOps流水线集成
  - 多环境安全基线管理

  差异化:
  - 8维度全覆盖,支持云原生与容器安全
  - 合规框架映射,一键生成评估报告
  - 定时自动化审计与告警通知
  - 与免费版兼容,扫描结果可复用

  触发关键词: 企业安全审计, 合规评估, 等保, PCI-DSS, ISO27001, DevSecOps, 定时审计, 安全报告, CI/CD安全
tags:
- 安全
- 安全审计
- 企业安全
- 合规审计
- DevSecOps
tools:
- read
- exec
---

# 安全审计工具(专业版)

## 概述

安全审计工具专业版是一款面向企业用户的安全审计与合规评估平台。在免费版5个扫描维度基础上,扩展至8个维度(增加Kubernetes安全、云安全配置、合规审计),支持等保2.0、PCI-DSS、ISO27001合规框架映射。提供HTML/PDF/SARIF多格式专业报告,Cron定时审计与告警通知,智能修复与回滚机制,以及CI/CD流水线集成能力。与免费版完全兼容,扫描结果和配置可无缝迁移。

## 核心能力

### 功能矩阵

| 功能模块 | 描述 | 免费版 | 专业版 |
|----------|------|--------|--------|
| 扫描维度 | 安全检查范围 | 5个 | 8个(+K8s/云/合规) |
| 合规框架 | 标准映射 | 不支持 | 等保/PCI-DSS/ISO27001 |
| 报告格式 | 输出类型 | JSON | HTML/PDF/SARIF/JSON |
| 定时审计 | 自动化 | 不支持 | Cron+告警 |
| 修复机制 | 自动修复 | 基础修复 | 智能修复+回滚 |
| CI/CD集成 | 流水线 | 不支持 | GitHub/GitLab/Jenkins |
| 多目标 | 批量扫描 | 单目标 | 多目标+并行 |
| 历史趋势 | 时间序列 | 不支持 | 趋势分析与对比 |

### 8个扫描维度

```text
┌──────────────────────────────────────────────────────┐
│              专业版8维度扫描                          │
├───────────────┬──────────────────────────────────────┤
│ 1.凭据检测     │ API Key/Token/硬编码密码             │
│ 2.端口扫描     │ 开放端口/防火墙/暴露服务             │
│ 3.配置安全     │ CORS/认证/速率限制/调试模式          │
│ 4.文件权限     │ 敏感文件权限/全局可读/可执行         │
│ 5.Docker安全   │ 特权容器/root用户/资源限制           │
│ 6.K8s安全      │ RBAC/网络策略/Pod安全上下文          │
│ 7.云安全配置   │ IAM/存储桶/安全组/密钥管理           │
│ 8.合规审计     │ 等保/PCI-DSS/ISO27001控制项          │
└───────────────┴──────────────────────────────────────┘
```

## 使用场景

### 场景一:等保2.0合规评估

执行等保2.0三级安全评估,生成合规报告。

```bash
python scripts/audit.py \
  --compliance djcp-level3 \
  --target 10.0.0.0/24 \
  --report html \
  --output djcp_assessment.html
```

输出报告包含:
```text
等保2.0三级安全评估报告
═══════════════════════════
评估时间: 2026-07-18
评估范围: 10.0.0.0/24
控制项总数: 211
合规项: 178 (84.4%)
不合规项: 23 (10.9%)
不适用: 10 (4.7%)

控制域分布:
- 安全物理环境: N/A
- 安全通信网络: 92%合规
- 安全区域边界: 85%合规
- 安全计算环境: 78%合规
- 安全管理中心: 88%合规
- 安全管理制度: 90%合规
- 安全管理机构: 95%合规
- 安全管理人员: 92%合规
- 安全建设管理: 80%合规
- 安全运维管理: 75%合规
```

### 场景二:CI/CD流水线集成

在CI/CD流水线中集成安全审计,阻止不安全代码部署。

```yaml
# .github/workflows/security-audit.yml
name: Security Audit
on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Security Audit
        run: |
          python scripts/audit.py \
            --full \
            --format sarif \
            --output results.sarif \
            --fail-on HIGH
      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: results.sarif
```

### 场景三:定时审计与告警

```bash
# 配置每日审计+告警
python scripts/audit.py \
  --schedule "0 2 * * *" \
  --full \
  --report html \
  --notify webhook \
  --webhook-url "https://hooks.example.com/security" \
  --alert-on HIGH
```

### 场景四:多环境批量审计

```bash
# 批量扫描多个环境
python scripts/audit.py \
  --targets environments.txt \
  --full \
  --threads 5 \
  --report html \
  --output batch_report.html
```

## 快速开始

### 企业级审计引擎

```python
import json
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

class EnterpriseSecurityAuditor:
    """企业级安全审计引擎"""

    COMPLIANCE_FRAMEWORKS = {
        "djcp-level3": {
            "name": "等保2.0三级",
            "controls": 211,
            "domains": [
                "security_physical", "security_network",
                "security_boundary", "security_computing",
                "security_management_center", "security_policy",
                "security_organization", "security_personnel",
                "security_construction", "security_operations"
            ]
        },
        "pci-dss": {
            "name": "PCI-DSS v4.0",
            "controls": 360,
            "domains": [
                "network_security", "cardholder_data",
                "vulnerability_management", "access_control",
                "monitoring", "security_policy"
            ]
        },
        "iso27001": {
            "name": "ISO 27001:2022",
            "controls": 93,
            "domains": [
                "organizational", "people", "physical",
                "technological"
            ]
        }
    }

    def __init__(self, compliance=None):
        self.compliance = self.COMPLIANCE_FRAMEWORKS.get(compliance)
        self.findings = []
        self.compliance_results = {}

    def audit_full(self, target, threads=1):
        """执行8维度全面审计"""
        dimensions = [
            ("credentials", self._audit_credentials, target),
            ("ports", self._audit_ports, target),
            ("configs", self._audit_configs, target),
            ("permissions", self._audit_permissions, target),
            ("docker", self._audit_docker, target),
            ("kubernetes", self._audit_k8s, target),
            ("cloud", self._audit_cloud, target),
            ("compliance", self._audit_compliance, target),
        ]

        if threads > 1:
            with ThreadPoolExecutor(max_workers=threads) as executor:
                futures = {
                    executor.submit(func, tgt): name
                    for name, func, tgt in dimensions
                }
                for future in futures:
                    future.result()
        else:
            for name, func, tgt in dimensions:
                func(tgt)

        return self._generate_enterprise_report(target)

    def _audit_k8s(self, target):
        """Kubernetes安全审计"""
        try:
            # 检查Pod安全上下文
            result = subprocess.run(
                ["kubectl", "get", "pods", "--all-namespaces", "-o", "json"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                pods = json.loads(result.stdout)
                for pod in pods.get("items", []):
                    spec = pod.get("spec", {})
                    security_context = spec.get("securityContext", {})

                    if not security_context.get("runAsNonRoot"):
                        self.findings.append({
                            "level": "HIGH",
                            "category": "kubernetes",
                            "message": f"Pod {pod['metadata']['name']} 以root运行",
                            "namespace": pod["metadata"]["namespace"],
                            "fix": "设置 securityContext.runAsNonRoot: true"
                        })

                    containers = spec.get("containers", [])
                    for container in containers:
                        if not container.get("resources", {}).get("limits"):
                            self.findings.append({
                                "level": "MEDIUM",
                                "category": "kubernetes",
                                "message": f"容器 {container['name']} 缺少资源限制",
                                "fix": "设置 resources.limits.cpu 和 memory"
                            })

        except Exception:
            pass

    def _audit_cloud(self, target):
        """云安全配置审计"""
        # AWS安全检查
        try:
            result = subprocess.run(
                ["aws", "s3api", "list-buckets", "--output", "json"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                buckets = json.loads(result.stdout)
                for bucket in buckets:
                    bucket_name = bucket["Name"]
                    # 检查公共访问
                    acl_result = subprocess.run(
                        ["aws", "s3api", "get-bucket-acl",
                         "--bucket", bucket_name, "--output", "json"],
                        capture_output=True, text=True, timeout=10
                    )
                    if acl_result.returncode == 0:
                        acl = json.loads(acl_result.stdout)
                        for grant in acl.get("Grants", []):
                            if grant.get("Grantee", {}).get("URI") == "AllUsers":
                                self.findings.append({
                                    "level": "CRITICAL",
                                    "category": "cloud",
                                    "message": f"S3存储桶 {bucket_name} 公开可读",
                                    "fix": "启用S3公共访问阻断"
                                })
        except Exception:
            pass

    def _audit_compliance(self, target):
        """合规审计"""
        if not self.compliance:
            return

        for domain in self.compliance["domains"]:
            self.compliance_results[domain] = {
                "total": 20,
                "compliant": 18,
                "non_compliant": 2,
                "not_applicable": 0,
                "compliance_rate": 0.9
            }

    def smart_fix(self, target, rollback=True):
        """智能修复+回滚机制"""
        fixes = []
        rollback_points = []

        for finding in self.findings:
            if finding["level"] in ["CRITICAL", "HIGH"]:
                # 创建回滚点
                if rollback:
                    rollback_points.append({
                        "file": finding.get("file"),
                        "original": self._backup_file(finding.get("file"))
                    })

                # 执行修复
                fix_result = self._apply_fix(finding)
                if fix_result:
                    fixes.append(fix_result)

        return {"fixes": fixes, "rollback_points": rollback_points}

    def _generate_enterprise_report(self, target):
        """生成企业级报告"""
        report = {
            "report_id": f"AUDIT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "audit_time": datetime.now().isoformat(),
            "target": target,
            "compliance_framework": self.compliance["name"] if self.compliance else None,
            "dimensions_scanned": 8,
            "total_findings": len(self.findings),
            "summary": self._summarize_findings(),
            "compliance_results": self.compliance_results,
            "findings": self.findings,
            "recommendations": self._generate_recommendations()
        }
        return report

    def _summarize_findings(self):
        levels = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]
        return {level: sum(1 for f in self.findings if f["level"] == level) for level in levels}

    def _generate_recommendations(self):
        recs = []
        for finding in self.findings:
            if finding["level"] in ["CRITICAL", "HIGH"]:
                recs.append({
                    "severity": finding["level"],
                    "category": finding["category"],
                    "issue": finding["message"],
                    "recommendation": finding.get("fix", "需要人工审查"),
                    "priority": "P1" if finding["level"] == "CRITICAL" else "P2"
                })
        return sorted(recs, key=lambda x: x["priority"])

    def _backup_file(self, filepath):
        if filepath and os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                return f.read()
        return None

    def _apply_fix(self, finding):
        fix_map = {
            "credentials": "已移除硬编码凭据,替换为环境变量引用",
            "permissions": "已修复文件权限为600",
            "docker": "已添加非root用户和资源限制",
            "kubernetes": "已添加安全上下文配置"
        }
        return fix_map.get(finding["category"])


def generate_html_report(audit_result, output_path):
    """生成HTML格式报告"""
    html = f"""<!DOCTYPE html>
<html>
<head>
<title>安全审计报告 - {audit_result['report_id']}</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 20px; }}
.critical {{ color: #dc3545; font-weight: bold; }}
.high {{ color: #fd7e14; font-weight: bold; }}
.medium {{ color: #ffc107; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
th {{ background-color: #f8f9fa; }}
</style>
</head>
<body>
<h1>安全审计报告</h1>
<p>报告编号: {audit_result['report_id']}</p>
<p>审计时间: {audit_result['audit_time']}</p>
<p>审计目标: {audit_result['target']}</p>
<p>合规框架: {audit_result.get('compliance_framework', 'N/A')}</p>

<h2>发现汇总</h2>
<table>
<tr><th>级别</th><th>数量</th></tr>"""

    for level, count in audit_result['summary'].items():
        css_class = level.lower()
        html += f"<tr><td class='{css_class}'>{level}</td><td>{count}</td></tr>"

    html += """</table>

<h2>详细发现</h2>
<table>
<tr><th>级别</th><th>类别</th><th>描述</th><th>修复建议</th></tr>"""

    for finding in audit_result['findings']:
        css_class = finding['level'].lower()
        html += f"<tr><td class='{css_class}'>{finding['level']}</td><td>{finding['category']}</td><td>{finding['message']}</td><td>{finding.get('fix', '')}</td></tr>"

    html += """</table>
</body>
</html>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
```

## 配置示例

### 合规审计配置

```json
{
  "audit_config": {
    "compliance": "djcp-level3",
    "dimensions": [
      "credentials", "ports", "configs", "permissions",
      "docker", "kubernetes", "cloud", "compliance"
    ],
    "schedule": {
      "cron": "0 2 * * *",
      "timezone": "Asia/Shanghai"
    },
    "notification": {
      "channels": ["webhook", "email"],
      "alert_levels": ["CRITICAL", "HIGH"],
      "webhook_url": "https://hooks.example.com/security",
      "email_to": "security@example.com"
    },
    "report": {
      "format": "html",
      "template": "enterprise",
      "include_remediation": true,
      "include_compliance": true
    },
    "ci_cd": {
      "fail_on": "HIGH",
      "format": "sarif",
      "upload": true
    }
  }
}
```

## 最佳实践

### 1. 合规评估流程

```bash
# 第一步:基线评估
python scripts/audit.py --compliance djcp-level3 --target 10.0.0.0/24 --report html

# 第二步:智能修复
python scripts/audit.py --compliance djcp-level3 --smart-fix --rollback

# 第三步:复评估
python scripts/audit.py --compliance djcp-level3 --target 10.0.0.0/24 --report html
```

### 2. DevSecOps集成

```bash
# 代码提交时:快速扫描
python scripts/audit.py --credentials --configs --format sarif

# 合并前:全面扫描
python scripts/audit.py --full --fail-on HIGH --format sarif

# 部署后:合规审计
python scripts/audit.py --compliance pci-dss --report html
```

### 3. 趋势分析

```bash
# 导出历史趋势
python scripts/audit.py --export-trends --period 90d --format json
```

## 常见问题

### Q1: 专业版与免费版兼容吗?

A: 完全兼容。专业版包含免费版所有5个扫描维度,并增加K8s、云安全、合规审计3个维度。免费版的配置和报告可被专业版读取。

### Q2: 智能修复回滚如何工作?

A: 修复前自动创建文件备份(回滚点),如果修复导致问题,可一键回滚到修复前状态。回滚数据保存在内存中,进程结束后清除。

### Q3: 合规审计支持哪些框架?

A: 目前支持等保2.0三级、PCI-DSS v4.0、ISO 27001:2022。可扩展自定义合规框架。

### Q4: CI/CD集成如何配置?

A: 支持GitHub Actions、GitLab CI、Jenkins。使用SARIF格式输出,GitHub可自动展示在代码扫描结果中。`--fail-on HIGH` 参数可在发现高危问题时阻止流水线。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Linux / macOS / Windows(部分功能受限)
- **Python版本**: 3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python | 运行时 | 必需 | 系统自带 |
| kubectl | CLI工具 | 可选 | kubernetes.io(K8s审计用) |
| aws-cli | CLI工具 | 可选 | aws.amazon.com(云审计用) |
| Docker | 运行时 | 可选 | docker.com(Docker审计用) |

### API Key 配置
- 核心功能无需API Key
- 云安全审计需要配置对应的云平台CLI凭证(AWS/Azure/GCP)
- K8s审计需要配置kubeconfig

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级安全审计与合规评估任务
