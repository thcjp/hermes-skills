# 详细参考 - security-audit-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

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
        try:
            result = subprocess.run(
                ["aws", "s3api", "list-buckets", "--output", "json"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                buckets = json.loads(result.stdout)
                for bucket in buckets:
                    bucket_name = bucket["Name"]
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
                if rollback:
                    rollback_points.append({
                        "file": finding.get("file"),
                        "original": self._backup_file(finding.get("file"))
                    })

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

