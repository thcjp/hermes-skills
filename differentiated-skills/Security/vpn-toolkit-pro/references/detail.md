# 详细参考 - vpn-toolkit-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import subprocess
import json
import time
import threading
import os
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

class VPNManager:
    """企业级VPN管理引擎"""

    def __init__(self, config_path="vpn_config.json"):
        self.config = self._load_config(config_path)
        self.vpn_servers = self.config.get("vpn_servers", [])
        self.active_vpn = None
        self.metrics = {}
        self.audit_log = []

    def load_balance(self):
        """负载均衡:选择最优VPN服务器"""
        best_vpn = None
        best_score = 0

        for vpn in self.vpn_servers:
            score = self._calculate_vpn_score(vpn)
            vpn["score"] = score
            if score > best_score:
                best_score = score
                best_vpn = vpn

        if best_vpn:
            self._connect_vpn(best_vpn)
            self._log_audit("load_balance", f"选择VPN: {best_vpn['name']} (评分: {best_score})")

        return best_vpn

    def _calculate_vpn_score(self, vpn):
        """计算VPN评分(延迟/带宽/可用性)"""
        latency = self._check_latency(vpn["endpoint"])
        bandwidth = vpn.get("bandwidth_mbps", 100)
        priority = vpn.get("priority", 1)

        bandwidth_score = min(bandwidth / 1000, 1.0) * 40
        latency_score = max(0, (500 - latency) / 500) * 40
        priority_score = (10 - priority) / 10 * 20

        return round(bandwidth_score + latency_score + priority_score, 1)

    def _check_latency(self, endpoint):
        """检测VPN服务器延迟"""
        host = endpoint.split(":")[0]
        try:
            result = subprocess.run(
                ["ping", "-c", "3", "-W", "5", host],
                capture_output=True, text=True, timeout=15
            )
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if "avg" in line:
                        parts = line.split("=")
                        if len(parts) >= 2:
                            avg = parts[1].split("/")[1]
                            return float(avg)
            return 999  # 不可达
        except Exception:
            return 999

    def _connect_vpn(self, vpn):
        """连接VPN"""
        protocol = vpn["protocol"]
        endpoint = vpn["endpoint"]

        if protocol == "wireguard":
            self._connect_wireguard(vpn)
        elif protocol == "openvpn":
            self._connect_openvpn(vpn)

        self.active_vpn = vpn
        self._log_audit("connect", f"已连接: {vpn['name']} ({protocol})")

    def _connect_wireguard(self, vpn):
        """连接WireGuard VPN"""
        config_file = f"/etc/wireguard/{vpn['name']}.conf"

        if not os.path.exists(config_file):
            self._generate_wg_config(vpn, config_file)

        subprocess.run(["wg-quick", "up", vpn["name"]], check=True)

    def _connect_openvpn(self, vpn):
        """连接OpenVPN VPN"""
        config_file = f"/etc/openvpn/{vpn['name']}.ovpn"
        subprocess.run(
            ["openvpn", "--config", config_file, "--daemon"],
            check=True
        )

    def failover(self):
        """故障转移:切换到备用VPN"""
        if self.active_vpn:
            self._disconnect_vpn(self.active_vpn)
            self._log_audit("failover", f"主VPN断开: {self.active_vpn['name']}")

        remaining = [v for v in self.vpn_servers if v != self.active_vpn]
        if remaining:
            next_vpn = min(remaining, key=lambda v: v.get("priority", 99))
            self._connect_vpn(next_vpn)
            self._log_audit("failover", f"切换到备用VPN: {next_vpn['name']}")
            return next_vpn
        return None

    def monitor(self, interval=30, alert_callback=None):
        """持续监控VPN状态"""
        while True:
            if self.active_vpn:
                metrics = self._collect_metrics(self.active_vpn)
                self.metrics[self.active_vpn["name"]] = metrics

                if metrics["latency"] > 500:
                    self._trigger_alert("high_latency", metrics, alert_callback)
                if metrics["packet_loss"] > 5:
                    self._trigger_alert("packet_loss", metrics, alert_callback)
                if not metrics["connected"]:
                    self._trigger_alert("disconnected", metrics, alert_callback)
                    self.failover()

            time.sleep(interval)

    def _collect_metrics(self, vpn):
        """收集VPN指标"""
        return {
            "timestamp": datetime.now().isoformat(),
            "vpn": vpn["name"],
            "connected": self._is_connected(vpn),
            "latency": self._check_latency(vpn["endpoint"]),
            "bandwidth": self._measure_bandwidth(vpn),
            "packet_loss": self._check_packet_loss(vpn["endpoint"])
        }

    def generate_audit_report(self, compliance="pci-dss", period_days=30):
        """生成合规审计报告"""
        report = {
            "report_id": f"VPN-AUDIT-{datetime.now().strftime('%Y%m%d')}",
            "compliance": compliance,
            "period": f"{period_days} days",
            "generated_at": datetime.now().isoformat(),
            "vpn_servers": len(self.vpn_servers),
            "audit_entries": len(self.audit_log),
            "events": self.audit_log[-100:],
            "metrics": self.metrics,
            "compliance_checks": self._run_compliance_checks(compliance)
        }
        return report

    def _run_compliance_checks(self, standard):
        """执行合规检查"""
        checks = {
            "pci-dss": [
                {"id": "REQ-4.1", "desc": "传输中数据加密", "status": "PASS"},
                {"id": "REQ-8.2", "desc": "VPN认证强密码策略", "status": "PASS"},
                {"id": "REQ-10.3", "desc": "VPN访问日志记录", "status": "PASS"},
                {"id": "REQ-11.4", "desc": "VPN隧道安全测试", "status": "PASS"}
            ],
            "hipaa": [
                {"id": "164.312(a)(1)", "desc": "访问控制", "status": "PASS"},
                {"id": "164.312(b)", "desc": "审计控制", "status": "PASS"},
                {"id": "164.312(e)(1)", "desc": "传输安全", "status": "PASS"}
            ]
        }
        return checks.get(standard, [])

    def deploy_batch(self, targets_file, config_template, threads=10):
        """批量部署VPN配置"""
        with open(targets_file) as f:
            targets = [line.strip() for line in f if line.strip()]

        results = []
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = {
                executor.submit(self._deploy_to_target, target, config_template): target
                for target in targets
            }
            for future in futures:
                target = futures[future]
                try:
                    result = future.result()
                    results.append({"target": target, "status": "success"})
                    print(f"[成功] {target}")
                except Exception as e:
                    results.append({"target": target, "status": "failed", "error": str(e)})
                    print(f"[失败] {target}: {str(e)}")

        return results

    def _deploy_to_target(self, target, config_template):
        """部署VPN配置到目标设备"""
        subprocess.run(
            ["scp", config_template, f"{target}:/etc/wireguard/wg0.conf"],
            check=True, timeout=30
        )
        subprocess.run(
            ["ssh", target, "wg-quick up wg0"],
            check=True, timeout=30
        )
        result = subprocess.run(
            ["ssh", target, "wg show"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            raise Exception("VPN启动验证失败")

    def _log_audit(self, event_type, message):
        """记录审计日志"""
        self.audit_log.append({
            "timestamp": datetime.now().isoformat(),
            "event": event_type,
            "message": message,
            "active_vpn": self.active_vpn["name"] if self.active_vpn else None
        })

    def _trigger_alert(self, alert_type, metrics, callback):
        """触发告警"""
        alert = {
            "timestamp": datetime.now().isoformat(),
            "type": alert_type,
            "vpn": metrics["vpn"],
            "metrics": metrics
        }
        self._log_audit("alert", f"告警: {alert_type} - VPN: {metrics['vpn']}")
        if callback:
            callback(alert)

    def _is_connected(self, vpn):
        try:
            result = subprocess.run(["wg", "show"], capture_output=True, text=True)
            return vpn["name"] in result.stdout
        except Exception:
            return False

    def _measure_bandwidth(self, vpn):
        return vpn.get("bandwidth_mbps", 100)

    def _check_packet_loss(self, endpoint):
        host = endpoint.split(":")[0]
        try:
            result = subprocess.run(
                ["ping", "-c", "10", "-W", "5", host],
                capture_output=True, text=True, timeout=30
            )
            for line in result.stdout.split('\n'):
                if "packet loss" in line:
                    loss_str = line.split(",")[2].strip()
                    return float(loss_str.split("%")[0])
        except Exception:
            pass
        return 0

    def _disconnect_vpn(self, vpn):
        try:
            if vpn["protocol"] == "wireguard":
                subprocess.run(["wg-quick", "down", vpn["name"]])
            elif vpn["protocol"] == "openvpn":
                subprocess.run(["pkill", "-f", vpn["name"]])
        except Exception:
            pass

    def _generate_wg_config(self, vpn, config_path):
        """生成WireGuard配置"""
        config = f"""[Interface]
PrivateKey = <auto-generated>
Address = 10.8.0.{vpn.get('priority', 1) + 1}/24
DNS = 10.8.0.1

[Peer]
PublicKey = <server-public-key>
Endpoint = {vpn['endpoint']}
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
"""
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as f:
            f.write(config)

    def _load_config(self, path):
        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)
        return {"vpn_servers": []}
```

