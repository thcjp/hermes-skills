# 详细参考 - dns-networking-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import subprocess
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

class NetworkInspectorPro:
    """企业级网络巡检引擎"""

    def __init__(self, config_file=None):
        self.targets = []
        self.results = []
        self._load_config(config_file)

    def _load_config(self, config_file):
        """加载巡检配置"""
        self.targets = [
            {"host": "api.example.com", "ports": [80, 443], "check_cert": True},
            {"host": "db.internal.com", "ports": [5432, 6379], "check_cert": False},
            {"host": "cdn.example.com", "ports": [80, 443], "check_cert": True},
        ]

    def inspect_target(self, target):
        """检查单个目标"""
        result = {
            "host": target["host"],
            "timestamp": datetime.now().isoformat(),
            "dns": None,
            "ports": {},
            "certificate": None,
            "latency": None
        }

        try:
            dns_result = subprocess.run(
                ["dig", "+short", target["host"]],
                capture_output=True, text=True, timeout=5
            )
            result["dns"] = dns_result.stdout.strip().split('\n')[0] or None
        except Exception as e:
            result["dns"] = f"ERROR: {e}"

        for port in target["ports"]:
            try:
                nc_result = subprocess.run(
                    ["nc", "-zv", "-w", "3", target["host"], str(port)],
                    capture_output=True, text=True, timeout=5
                )
                result["ports"][port] = "open" if nc_result.returncode == 0 else "closed"
            except Exception:
                result["ports"][port] = "timeout"

        if target.get("check_cert") and 443 in target["ports"]:
            try:
                cert_result = subprocess.run(
                    f"echo | openssl s_client -connect {target['host']}:443 "
                    f"-servername {target['host']} 2>/dev/null | "
                    f"openssl x509 -noout -enddate 2>/dev/null",
                    shell=True, capture_output=True, text=True, timeout=10
                )
                result["certificate"] = cert_result.stdout.strip() or None
            except Exception:
                result["certificate"] = "ERROR"

        try:
            curl_result = subprocess.run(
                ["curl", "-o", "/dev/null", "-s", "-w", "%{time_total}",
                 f"https://{target['host']}"],
                capture_output=True, text=True, timeout=10
            )
            result["latency"] = curl_result.stdout.strip()
        except Exception:
            result["latency"] = None

        return result

    def run_batch_inspection(self, max_workers=10):
        """批量巡检"""
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self.inspect_target, t): t for t in self.targets
            }
            for future in as_completed(futures):
                result = future.result()
                self.results.append(result)
                status = "OK" if result["dns"] else "FAIL"
                print(f"[{status}] {result['host']}")
        return self.results

    def generate_report(self, format="json"):
        """生成报告"""
        report = {
            "scan_time": datetime.now().isoformat(),
            "total_targets": len(self.results),
            "healthy": sum(1 for r in self.results if r["dns"]),
            "unhealthy": sum(1 for r in self.results if not r["dns"]),
            "results": self.results
        }
        return report

if __name__ == "__main__":
    inspector = NetworkInspectorPro()
    results = inspector.run_batch_inspection()
    report = inspector.generate_report()

    with open("network-report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\n巡检完成: {report['healthy']}/{report['total_targets']} 健康")
```

## 代码示例 (python)

```python
import subprocess
import json
import time
import smtplib
from datetime import datetime
from email.mime.text import MIMEText

class NetworkMonitor:
    """网络持续监控与告警"""

    def __init__(self, config):
        self.targets = config.get("targets", [])
        self.alert_config = config.get("alert", {})
        self.history = []

    def check_target(self, host, port=443):
        """检查目标可用性"""
        try:
            result = subprocess.run(
                ["nc", "-zv", "-w", "5", host, str(port)],
                capture_output=True, text=True, timeout=10
            )
            return result.returncode == 0
        except Exception:
            return False

    def monitor_loop(self, interval=60):
        """监控循环"""
        while True:
            for target in self.targets:
                is_ok = self.check_target(target["host"], target.get("port", 443))
                record = {
                    "host": target["host"],
                    "port": target.get("port", 443),
                    "status": "up" if is_ok else "down",
                    "timestamp": datetime.now().isoformat()
                }
                self.history.append(record)

                if not is_ok:
                    self.send_alert(target["host"], "服务不可达")

            time.sleep(interval)

    def send_alert(self, host, message):
        """发送告警"""
        subject = f"[网络告警] {host} - {message}"
        body = f"""
告警时间: {datetime.now()}
目标主机: {host}
告警信息: {message}

请及时检查服务状态。
"""
        print(f"[ALERT] {subject}")

        if self.alert_config.get("email"):
            try:
                msg = MIMEText(body)
                msg["Subject"] = subject
                msg["From"] = self.alert_config["email"]["from"]
                msg["To"] = self.alert_config["email"]["to"]

                with smtplib.SMTP(
                    self.alert_config["email"]["smtp_host"],
                    self.alert_config["email"]["smtp_port"]
                ) as server:
                    server.send_message(msg)
            except Exception as e:
                print(f"邮件发送失败: {e}")

config = {
    "targets": [
        {"host": "api.example.com", "port": 443},
        {"host": "db.internal.com", "port": 5432},
    ],
    "alert": {
        "email": {
            "from": "monitor@company.com",
            "to": "ops@company.com",
            "smtp_host": "smtp.company.com",
            "smtp_port": 25
        }
    }
}

```

## 代码示例 (yaml)

```yaml
version: "2.0"
edition: pro

targets:
  - host: api.example.com
    ports: [80, 443, 8080]
    check_cert: true
    expected_latency: 0.5
  - host: db.internal.com
    ports: [5432, 6379]
    check_cert: false
  - host: cdn.example.com
    ports: [80, 443]
    check_cert: true

dns_servers:
  primary: 8.8.8.8
  secondary: 1.1.1.1
  internal: 10.0.0.53

firewall_audit:
  enabled: true
  check_iptables: true
  check_ufw: true
  high_risk_ports: [22, 3306, 5432, 6379]
  allowed_sources:
    ssh: ["10.0.0.0/8", "192.168.0.0/16"]

proxy_diagnosis:
  enabled: true
  test_urls:
    - https://httpbin.org/ip
    - https://ifconfig.me

monitoring:
  enabled: true
  interval: 60
  alert:
    email:
      from: monitor@company.com
      to: ops@company.com
      smtp_host: smtp.company.com
      smtp_port: 587
    webhook:
      url: "https://hooks.example.com/network-alert"
    slack:
      webhook: "https://hooks.slack.com/services/xxx"

report:
  format: [json, html, markdown]
  output_dir: ./reports/
  retention_days: 90
  include_history: true
```

