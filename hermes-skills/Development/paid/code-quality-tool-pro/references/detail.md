# 详细参考 - code-quality-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import os
import json
from datetime import datetime

class CodeAuditPro:
    """企业级代码审计引擎"""

    def __init__(self, project_root, rules_config=None):
        self.project_root = project_root
        self.results = []
        self.rules = self._load_rules(rules_config)

    def _load_rules(self, config):
        """加载规则配置,兼容免费版格式"""
        default_rules = {
            "security": ["hardcoded_secrets", "sql_injection", "xss",
                         "weak_crypto", "path_traversal"],
            "style": ["naming", "formatting", "comments"],
            "compliance": ["owasp_top10", "pci_dss", "gdpr"],
        }
        if config and os.path.exists(config):
            with open(config, 'r', encoding='utf-8') as f:
                user_rules = json.load(f)
                default_rules.update(user_rules)
        return default_rules

    def scan_project(self):
        """扫描整个项目"""
        supported_extensions = ('.js', '.ts', '.py', '.java', '.go',
                                '.php', '.rb', '.cs')

        for root, dirs, files in os.walk(self.project_root):
            dirs[:] = [d for d in dirs if d not in
                       ('node_modules', '.git', 'dist', 'build', '__pycache__')]

            for file in files:
                if file.endswith(supported_extensions):
                    filepath = os.path.join(root, file)
                    self._scan_file(filepath)

        return self._generate_report()

    def _scan_file(self, filepath):
        """扫描单个文件"""
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
                for i, line in enumerate(lines, 1):
                    issues.extend(self._check_line(line, i, filepath))
        except Exception as e:
            issues.append({
                "file": filepath,
                "line": 0,
                "severity": "error",
                "category": "scan_error",
                "message": str(e)
            })
        self.results.extend(issues)

    def _check_line(self, line, lineno, filepath):
        """检查单行代码"""
        issues = []
        checks = [
            (r"password\s*=\s*['\"]", "hardcoded_secret", "critical"),
            (r"eval\s*\(", "code_injection", "critical"),
            (r"SELECT.*\+.*FROM", "sql_injection", "high"),
            (r"innerHTML\s*=", "xss_risk", "medium"),
            (r"\b(md5|sha1)\b\s*\(", "weak_crypto", "high"),
        ]
        for pattern, category, severity in checks:
            import re
            if re.search(pattern, line, re.IGNORECASE):
                issues.append({
                    "file": filepath,
                    "line": lineno,
                    "severity": severity,
                    "category": category,
                    "message": f"检测到 {category} 风险",
                    "code": line.strip()
                })
        return issues

    def _generate_report(self):
        """生成审计报告"""
        report = {
            "scan_time": datetime.now().isoformat(),
            "project": self.project_root,
            "total_files": len(set(r["file"] for r in self.results)),
            "total_issues": len(self.results),
            "severity_count": {},
            "issues": self.results
        }
        for r in self.results:
            sev = r["severity"]
            report["severity_count"][sev] = \
                report["severity_count"].get(sev, 0) + 1
        return report

if __name__ == "__main__":
    auditor = CodeAuditPro("./src", ".codequality.yml")
    report = auditor.scan_project()

    with open("audit-report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"扫描完成: {report['total_files']} 个文件")
    print(f"发现问题: {report['total_issues']} 个")
    for sev, count in report["severity_count"].items():
        print(f"  {sev}: {count}")
```

## 代码示例 (yaml)

```yaml
version: "2.0"
edition: pro

settings:
  parallel_workers: 4
  max_file_size: 10MB
  exclude_dirs: [node_modules, .git, dist, build, vendor]
  encoding: utf-8

security:
  owasp_top10: true
  hardcoded_secrets: true
  sql_injection: true
  xss_detection: true
  weak_crypto: true
  path_traversal: true
  ssrf_detection: true
  deserialization: true

compliance:
  - template: owasp_top10
    severity_threshold: high
  - template: pci_dss
    enabled: true
  - template: gdpr
    enabled: true

custom_rules:
  - id: ENT-001
    name: 企业内部安全规范
    pattern: "internal_api_key"
    severity: critical

ci_cd:
  fail_on: [critical, high]
  report_format: [sarif, html, json]
  output_dir: ./reports/
  artifact_retention: 30
  issue_tracker_integration: true

multi_tenant:
  enabled: true
  default_tenant: default
  role_based_access: true
```

