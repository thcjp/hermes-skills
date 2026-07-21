# 详细参考 - web-vuln-assess-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import json
import os
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

class WebVulnAssessmentPro:
    """企业级Web漏洞评估引擎"""

    VULN_CATEGORIES = {
        "injection": {"name": "注入漏洞", "severity": "CRITICAL", "owasp": "A03:2021"},
        "authentication": {"name": "认证与会话管理", "severity": "HIGH", "owasp": "A07:2021"},
        "data_exposure": {"name": "敏感数据暴露", "severity": "HIGH", "owasp": "A02:2021"},
        "misconfiguration": {"name": "安全配置错误", "severity": "MEDIUM", "owasp": "A05:2021"},
        "xml_vulnerabilities": {"name": "XML漏洞", "severity": "HIGH", "owasp": "-"},
        "access_control": {"name": "访问控制失效", "severity": "HIGH", "owasp": "A01:2021"},
        "deserialization": {"name": "不安全反序列化", "severity": "HIGH", "owasp": "A08:2021"},
        "api_security": {"name": "API安全", "severity": "HIGH", "owasp": "-"},
        "communication": {"name": "不安全通信", "severity": "MEDIUM", "owasp": "-"},
        "client_side": {"name": "客户端漏洞", "severity": "MEDIUM", "owasp": "-"},
        "dos": {"name": "拒绝服务", "severity": "MEDIUM", "owasp": "-"},
        "ssrf": {"name": "SSRF", "severity": "HIGH", "owasp": "A10:2021"},
        "auth_bypass": {"name": "认证绕过", "severity": "CRITICAL", "owasp": "-"},
        "content_spoofing": {"name": "内容欺骗", "severity": "MEDIUM", "owasp": "-"},
        "business_logic": {"name": "业务逻辑缺陷", "severity": "HIGH", "owasp": "-"},
        "zero_day": {"name": "零日模式", "severity": "CRITICAL", "owasp": "-"},
        "mobile": {"name": "移动应用漏洞", "severity": "HIGH", "owasp": "-"},
        "iot": {"name": "IoT漏洞", "severity": "HIGH", "owasp": "-"},
        "other": {"name": "其他漏洞", "severity": "MEDIUM", "owasp": "-"}
    }

    COMPLIANCE_FRAMEWORKS = {
        "owasp_top_10": {"name": "OWASP Top 10:2021", "categories": 10},
        "pci_dss": {"name": "PCI-DSS v4.0", "categories": 12, "focus": "支付数据保护"},
        "gdpr": {"name": "GDPR", "categories": 8, "focus": "个人数据保护"},
        "hipaa": {"name": "HIPAA", "categories": 6, "focus": "医疗数据保护"}
    }

    SUPPORTED_TECH = [
        "php", "nodejs", "python", "java", "dotnet", "ruby",
        "react", "angular", "vue", "wordpress",
        "mysql", "postgresql", "mongodb", "redis",
        "docker", "kubernetes", "aws", "azure", "nginx", "apache"
    ]

    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("VULN_ASSESS_API_KEY")
        self.assessment_results = {}

    def assess(self, app_info, scope="all", compliance=None,
               include_remediation=True, include_scripts=False):
        """执行自动化漏洞评估"""
        categories = self._get_scope(scope)

        findings = self._run_assessment(app_info, categories)

        compliance_results = {}
        if compliance:
            for framework in compliance:
                compliance_results[framework] = self._map_compliance(findings, framework)

        remediation = {}
        if include_remediation:
            remediation = self._generate_remediation(findings)

        test_scripts = {}
        if include_scripts:
            test_scripts = self._generate_test_scripts(findings, app_info)

        report = self._generate_report(
            app_info, findings, compliance_results,
            remediation, test_scripts
        )

        return report

    def _run_assessment(self, app_info, categories):
        """执行评估(模拟API调用)"""
        findings = []

        for cat_id in categories:
            cat = self.VULN_CATEGORIES[cat_id]
            finding = {
                "category": cat_id,
                "name": cat["name"],
                "severity": cat["severity"],
                "owasp": cat["owasp"],
                "findings": self._check_category(cat_id, app_info)
            }
            findings.append(finding)

        return findings

    def _check_category(self, category, app_info):
        """检查单个类别(模拟)"""
        checks = {
            "injection": [
                {"check": "SQL注入检测", "status": "FAIL", "endpoint": "/api/products?id=1", "detail": "字符串拼接查询"},
                {"check": "命令注入检测", "status": "PASS", "detail": "使用参数数组"}
            ],
            "authentication": [
                {"check": "JWT安全配置", "status": "WARN", "detail": "过期时间过长(24h)"},
                {"check": "Session Cookie安全", "status": "PASS", "detail": "httpOnly+secure+sameSite"}
            ],
            "access_control": [
                {"check": "IDOR检测", "status": "FAIL", "endpoint": "/api/users/{id}", "detail": "无授权检查"},
                {"check": "管理接口保护", "status": "PASS", "detail": "IP白名单"}
            ]
        }
        return checks.get(category, [{"check": f"{category}检查", "status": "PASS", "detail": "未发现问题"}])

    def _map_compliance(self, findings, framework):
        """合规框架映射"""
        framework_info = self.COMPLIANCE_FRAMEWORKS.get(framework, {})
        mapped = {
            "framework": framework_info.get("name", framework),
            "focus": framework_info.get("focus", "通用"),
            "total_checks": framework_info.get("categories", 0),
            "compliant": 0,
            "non_compliant": 0,
            "categories": []
        }

        for finding in findings:
            if finding.get("findings"):
                fails = sum(1 for f in finding["findings"] if f["status"] == "FAIL")
                if fails > 0:
                    mapped["non_compliant"] += 1
                else:
                    mapped["compliant"] += 1

                mapped["categories"].append({
                    "category": finding["name"],
                    "status": "FAIL" if fails > 0 else "PASS",
                    "fail_count": fails
                })

        mapped["compliance_rate"] = round(
            mapped["compliant"] / max(mapped["total_checks"], 1) * 100, 1
        )

        return mapped

    def _generate_remediation(self, findings):
        """生成修复指南"""
        remediation_guide = {
            "injection": {
                "priority": "P0",
                "fix": "使用参数化查询: cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))",
                "reference": "OWASP SQL Injection Prevention Cheat Sheet"
            },
            "access_control": {
                "priority": "P0",
                "fix": "添加授权检查: if post.author_id != current_user.id: return 403",
                "reference": "OWASP Access Control Cheat Sheet"
            },
            "authentication": {
                "priority": "P1",
                "fix": "设置JWT过期时间为15分钟,使用刷新令牌",
                "reference": "OWASP Authentication Cheat Sheet"
            }
        }

        guide = {}
        for finding in findings:
            cat = finding["category"]
            if any(f["status"] == "FAIL" for f in finding["findings"]):
                guide[cat] = remediation_guide.get(cat, {
                    "priority": "P2",
                    "fix": "参考OWASP修复指南",
                    "reference": "OWASP Top 10"
                })

        return guide

    def _generate_test_scripts(self, findings, app_info):
        """生成渗透测试脚本"""
        scripts = {}
        target_url = app_info.get("url", "http://localhost:3000")

        for finding in findings:
            cat = finding["category"]
            fails = [f for f in finding["findings"] if f["status"] == "FAIL"]

            if fails:
                if cat == "injection":
                    scripts["sqli_test"] = self._gen_sqli_script(target_url)
                elif cat == "access_control":
                    scripts["idor_test"] = self._gen_idor_script(target_url)
                elif cat == "authentication":
                    scripts["auth_test"] = self._gen_auth_script(target_url)
                elif cat == "ssrf":
                    scripts["ssrf_test"] = self._gen_ssrf_script(target_url)

        return scripts

    def _gen_sqli_script(self, target_url):
        return f"""#!/bin/bash
TARGET="{target_url}"
PAYLOADS=("'" "1' OR '1'='1" "1; DROP TABLE--" "1 UNION SELECT NULL--")

for payload in "${{PAYLOADS[@]}}"; do
    echo "[*] 测试: $payload"
    RESPONSE=$(curl -s "{target_url}/api/products?id=$payload")
    if echo "$RESPONSE" | grep -qi "error\|sql\|syntax"; then
        echo "[!] 发现SQL注入: $payload"
    fi
done
"""

    def _gen_idor_script(self, target_url):
        return f"""#!/bin/bash
TARGET="{target_url}"

for i in $(seq 1 100); do
    RESPONSE=$(curl -s -o /dev/null -w "%{{http_code}}" "{target_url}/api/users/$i")
    if [ "$RESPONSE" = "200" ]; then
        echo "[!] IDOR可能: /api/users/$i 返回200"
    fi
done
"""

    def _gen_auth_script(self, target_url):
        return f"""#!/bin/bash
TARGET="{target_url}"

RESPONSE=$(curl -s -o /dev/null -w "%{{http_code}}" "{target_url}/api/admin/panel")
if [ "$RESPONSE" != "401" ] && [ "$RESPONSE" != "403" ]; then
    echo "[!] 管理接口无认证保护"
fi

curl -s -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ1c2VyIjoiYWRtaW4ifQ." "{target_url}/api/admin"
"""

    def _gen_ssrf_script(self, target_url):
        return f"""#!/bin/bash
TARGET="{target_url}"
PAYLOADS=("http://127.0.0.1" "http://169.254.169.254/latest/meta-data/" "http://localhost:6379")

for payload in "${{PAYLOADS[@]}}"; do
    echo "[*] 测试SSRF: $payload"
    RESPONSE=$(curl -s "{target_url}/api/fetch?url=$payload")
    if [ -n "$RESPONSE" ]; then
        echo "[!] 可能存在SSRF: $payload"
    fi
done
"""

    def _generate_report(self, app_info, findings, compliance, remediation, scripts):
        """生成综合评估报告"""
        total_fails = sum(
            sum(1 for f in finding["findings"] if f["status"] == "FAIL")
            for finding in findings
        )
        critical = sum(1 for f in findings if f["severity"] == "CRITICAL" and any(x["status"] == "FAIL" for x in f["findings"]))
        high = sum(1 for f in findings if f["severity"] == "HIGH" and any(x["status"] == "FAIL" for x in f["findings"]))

        return {
            "report_id": f"ASSESS-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "generated_at": datetime.now().isoformat(),
            "app_info": app_info,
            "summary": {
                "total_findings": total_fails,
                "critical": critical,
                "high": high,
                "risk_level": "CRITICAL" if critical > 0 else "HIGH" if high > 0 else "MEDIUM"
            },
            "findings": findings,
            "compliance": compliance,
            "remediation": remediation,
            "test_scripts": scripts
        }

    def batch_assess(self, apps_config_path, threads=5):
        """批量评估多个应用"""
        with open(apps_config_path) as f:
            apps = json.load(f)

        results = []
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = {
                executor.submit(self.assess, app): app["name"]
                for app in apps
            }
            for future in as_completed(futures):
                app_name = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                    print(f"[完成] {app_name}: {result['summary']['total_findings']} 个问题")
                except Exception as e:
                    print(f"[失败] {app_name}: {str(e)}")

        return results

    def generate_html_report(self, report, output_path):
        """生成HTML报告"""
        html = f"""<!DOCTYPE html>
<html>
<head><title>Web漏洞评估报告 - {report['app_info']['name']}</title>
<style>
body {{ font-family: Arial; margin: 20px; }}
.critical {{ color: #dc3545; font-weight: bold; }}
.high {{ color: #fd7e14; font-weight: bold; }}
.medium {{ color: #ffc107; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ border: 1px solid #ddd; padding: 8px; }}
th {{ background: #f8f9fa; }}
</style>
</head>
<body>
<h1>Web漏洞评估报告</h1>
<p>报告编号: {report['report_id']}</p>
<p>生成时间: {report['generated_at']}</p>
<p>应用名称: {report['app_info']['name']}</p>
<p>风险等级: <span class="{report['summary']['risk_level'].lower()}">{report['summary']['risk_level']}</span></p>
<p>发现问题: {report['summary']['total_findings']} (CRITICAL: {report['summary']['critical']}, HIGH: {report['summary']['high']})</p>

<h2>漏洞详情</h2>
<table>
<tr><th>类别</th><th>严重程度</th><th>OWASP</th><th>检查项</th><th>状态</th></tr>"""

        for finding in report['findings']:
            for item in finding['findings']:
                css = finding['severity'].lower()
                status_css = "critical" if item['status'] == 'FAIL' else ""
                html += f"""<tr>
<td class="{css}">{finding['name']}</td>
<td class="{css}">{finding['severity']}</td>
<td>{finding['owasp']}</td>
<td>{item['check']}</td>
<td class="{status_css}">{item['status']}</td>
</tr>"""

        html += """</table>"""

        if report.get('compliance'):
            html += "<h2>合规映射</h2><table><tr><th>框架</th><th>合规率</th><th>通过</th><th>未通过</th></tr>"
            for framework, result in report['compliance'].items():
                html += f"""<tr><td>{result['framework']}</td>
<td>{result['compliance_rate']}%</td>
<td>{result['compliant']}</td>
<td>{result['non_compliant']}</td></tr>"""
            html += "</table>"

        if report.get('remediation'):
            html += "<h2>修复指南</h2><table><tr><th>类别</th><th>优先级</th><th>修复方案</th></tr>"
            for cat, guide in report['remediation'].items():
                html += f"""<tr><td>{cat}</td><td>{guide['priority']}</td><td>{guide['fix']}</td></tr>"""
            html += "</table>"

        html += "</body></html>"

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        return output_path
```

