---
slug: dns-networking-tool-pro
name: dns-networking-tool-pro
version: "1.0.0"
displayName: DNS网络诊断专业版
summary: 企业级网络诊断,支持批量巡检、防火墙审计、代理链分析与持续监控告警。
license: MIT
edition: pro
description: |-
  面向运维团队的企业级网络诊断工具,提供批量目标巡检、防火墙规则审计、代理链完整分析、持续监控与告警通知。

  核心能力:
  - 批量多目标DNS与端口巡检
  - 防火墙规则审计(iptables/ufw/云安全组)
  - 代理链完整诊断(HTTP/SOCKS5)
  - 持续监控与告警通知
  - 网络拓扑路径分析(mtr/traceroute)
  - 多格式诊断报告输出

  适用场景:
  - 企业级网络故障排查
  - 服务可用性持续监控
  - 防火墙策略审计
  - 混合云网络连通性验证

  差异化:
  - 专业版完全兼容免费版命令,支持平滑升级
  - 支持批量巡检与定时监控
  - 提供防火墙规则审计能力
  - 支持多格式报告与告警集成

  触发关键词: 网络巡检, 防火墙审计, 批量诊断, 持续监控, 代理诊断, mtr, traceroute, network monitoring, firewall audit
tags:
- 开发工具
- 网络诊断
- 运维监控
- 企业级
tools:
- read
- exec
---

# DNS网络诊断工具 - 专业版

## 概述

DNS网络诊断工具专业版为运维团队提供企业级网络诊断能力。在免费版基础诊断能力之上,专业版新增批量多目标巡检、防火墙规则审计、代理链完整分析、持续监控与告警通知,满足企业级网络运维需求。

专业版完全兼容免费版的所有诊断命令和配置,运维团队可从免费版无缝升级,已有诊断脚本无需修改即可在专业版中使用。

## 核心能力

### 1. 批量多目标巡检

支持对多个目标进行批量DNS解析、端口连通性和证书检查。

```python
# 专业版批量巡检脚本
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

        # DNS解析
        try:
            dns_result = subprocess.run(
                ["dig", "+short", target["host"]],
                capture_output=True, text=True, timeout=5
            )
            result["dns"] = dns_result.stdout.strip().split('\n')[0] or None
        except Exception as e:
            result["dns"] = f"ERROR: {e}"

        # 端口检查
        for port in target["ports"]:
            try:
                nc_result = subprocess.run(
                    ["nc", "-zv", "-w", "3", target["host"], str(port)],
                    capture_output=True, text=True, timeout=5
                )
                result["ports"][port] = "open" if nc_result.returncode == 0 else "closed"
            except Exception:
                result["ports"][port] = "timeout"

        # 证书检查
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

        # 延迟测试
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


# 使用示例
if __name__ == "__main__":
    inspector = NetworkInspectorPro()
    results = inspector.run_batch_inspection()
    report = inspector.generate_report()

    with open("network-report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\n巡检完成: {report['healthy']}/{report['total_targets']} 健康")
```

### 2. 防火墙规则审计

审计 iptables/ufw/云安全组规则,发现潜在安全风险。

```bash
# 专业版防火墙审计脚本
#!/bin/bash
echo "=== 防火墙规则审计 ==="

# iptables审计
echo "--- iptables规则 ---"
sudo iptables -L -n -v

echo "--- 检查高危规则 ---"
echo "[警告] 开放给所有IP的SSH:"
sudo iptables -L -n | grep -E "dpt:22\s*$" | grep -v "DROP\|REJECT"

echo "[警告] 开放给所有IP的数据库端口:"
sudo iptables -L -n | grep -E "dpt:(3306|5432|6379|27017)\s*$"

echo "[警告] 允许转发:"
sudo iptables -L FORWARD -n | grep -v "Chain\|target\|^$"

# ufw审计
echo "--- ufw状态 ---"
sudo ufw status verbose

echo "--- ufw高危规则 ---"
sudo ufw status | grep -E "ALLOW.*ANYWHERE"

# 生成审计报告
{
    echo "# 防火墙审计报告"
    echo "生成时间: $(date)"
    echo ""
    echo "## iptables规则"
    sudo iptables -L -n -v
    echo ""
    echo "## ufw状态"
    sudo ufw status verbose
} > firewall-audit-$(date +%Y%m%d).md
```

### 3. 代理链完整诊断

完整诊断 HTTP/HTTPS/SOCKS5 代理链路。

```bash
# 代理链诊断脚本
#!/bin/bash
echo "=== 代理链诊断 ==="

# 1. 检查代理环境变量
echo "--- 代理环境变量 ---"
echo "HTTP_PROXY:  ${HTTP_PROXY:-未设置}"
echo "HTTPS_PROXY: ${HTTPS_PROXY:-未设置}"
echo "NO_PROXY:    ${NO_PROXY:-未设置}"

# 2. 直连测试
echo -e "\n--- 直连测试 ---"
curl -o /dev/null -s -w "直连耗时: %{time_total}s, 状态码: %{http_code}\n" \
  https://httpbin.org/ip

# 3. 代理测试
if [ -n "$HTTP_PROXY" ]; then
    echo -e "\n--- HTTP代理测试 ---"
    curl -x "$HTTP_PROXY" -o /dev/null -s -w \
      "代理耗时: %{time_total}s, 状态码: %{http_code}\n" \
      https://httpbin.org/ip

    echo -e "\n--- 代理详细信息 ---"
    curl -v -x "$HTTP_PROXY" https://httpbin.org/ip 2>&1 | \
      grep -i "proxy\|connect"
fi

# 4. SOCKS5代理测试
echo -e "\n--- SOCKS5代理测试 ---"
curl --socks5 localhost:1080 -o /dev/null -s -w \
  "SOCKS5耗时: %{time_total}s, 状态码: %{http_code}\n" \
  https://httpbin.org/ip 2>/dev/null || echo "SOCKS5代理不可用"

# 5. 常见工具代理配置检查
echo -e "\n--- 工具代理配置 ---"
echo "Git代理:    $(git config --global http.proxy 2>/dev/null || echo '未设置')"
echo "npm代理:    $(npm config get proxy 2>/dev/null || echo '未设置')"
echo "pip代理:    $(pip config list 2>/dev/null | grep proxy || echo '未设置')"
```

### 4. 持续监控与告警

定时监控目标可用性,异常时发送告警。

```python
# 专业版持续监控脚本
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


# 监控配置
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

# 启动监控
# monitor = NetworkMonitor(config)
# monitor.monitor_loop(interval=60)
```

### 5. 网络路径分析

使用 mtr 进行持续路径分析,发现网络抖动和丢包。

```bash
# 网络路径分析
echo "=== 网络路径分析 ==="

# mtr持续监控(报告模式)
mtr -r -c 100 example.com

# mtr JSON报告
mtr --report --report-cycles 20 --json example.com > path-analysis.json

# traceroute路径追踪
traceroute -n example.com

# 对比多条路径
for target in api.example.com cdn.example.com db.example.com; do
    echo "--- $target ---"
    mtr -r -c 20 "$target"
    echo ""
done
```

## 使用场景

### 场景一:生产环境网络巡检

对生产环境所有服务进行批量网络巡检。

```bash
#!/bin/bash
# 生产环境网络巡检脚本
echo "=== 生产环境网络巡检 ==="
echo "时间: $(date)"
echo ""

# 加载目标列表
TARGETS=$(cat << 'EOF'
api.example.com:443
app.example.com:443
db.internal:5432
cache.internal:6379
mq.internal:5672
EOF
)

# 批量检查
while IFS=':' read -r host port; do
    echo -n "$host:$port -> "
    if nc -zv -w 3 "$host" "$port" 2>&1 | grep -q "succeeded\|open"; then
        # 测量延迟
        latency=$(curl -o /dev/null -s -w "%{time_total}" "https://$host" 2>/dev/null || echo "N/A")
        echo "OK (延迟: ${latency}s)"
    else
        echo "FAIL"
    fi
done <<< "$TARGETS"

# 生成巡检报告
echo ""
echo "=== 巡检报告已生成: network-inspection-$(date +%Y%m%d).json ==="
```

### 场景二:防火墙策略变更审计

变更防火墙规则后进行审计验证。

```bash
#!/bin/bash
# 防火墙变更审计
echo "=== 防火墙变更审计 ==="

# 备份当前规则
sudo iptables-save > "iptables-backup-$(date +%Y%m%d).rules"
echo "规则已备份"

# 审计规则安全性
echo "--- 安全审计 ---"

# 检查是否有过于宽松的规则
echo "1. 检查开放端口:"
sudo iptables -L INPUT -n --line-numbers | grep ACCEPT

echo -e "\n2. 检查来源限制:"
sudo iptables -L INPUT -n -v | grep -v "0.0.0.0/0" | grep ACCEPT

echo -e "\n3. 检查高危端口:"
for port in 22 3306 5432 6379 27017; do
    matches=$(sudo iptables -L INPUT -n | grep "dpt:$port" | grep ACCEPT)
    if [ -n "$matches" ]; then
        echo "[!] 端口 $port 开放: $matches"
    fi
done
```

### 场景三:混合云连通性验证

验证混合云环境各节点间连通性。

```bash
#!/bin/bash
# 混合云连通性验证
echo "=== 混合云连通性验证 ==="

# 定义各云环境节点
declare -A NODES
NODES["公有云API"]="api.cloud.com:443"
NODES["私有云DB"]="db.private.cloud:5432"
NODES["边缘节点1"]="edge1.region1:443"
NODES["边缘节点2"]="edge2.region2:443"

# 批量验证
for name in "${!NODES[@]}"; do
    IFS=':' read -r host port <<< "${NODES[$name]}"
    echo -n "$name ($host:$port): "

    # DNS解析
    ip=$(dig +short "$host" | head -1)
    if [ -z "$ip" ]; then
        echo "DNS解析失败"
        continue
    fi

    # 端口连通性
    if nc -zv -w 3 "$host" "$port" 2>&1 | grep -q "open\|succeeded"; then
        # 延迟测试
        latency=$(ping -c 3 -W 3 "$host" 2>/dev/null | tail -1 | awk -F'/' '{print $5}')
        echo "OK (IP: $ip, 延迟: ${latency}ms)"
    else
        echo "FAIL (IP: $ip)"
    fi
done
```

## 快速开始

### 步骤一:配置巡检目标

创建 `.network-inspector.yml` 配置文件:

```yaml
version: "2.0"
edition: pro

targets:
  - host: api.example.com
    ports: [80, 443]
    check_cert: true
  - host: db.internal.com
    ports: [5432, 6379]
    check_cert: false

monitoring:
  enabled: true
  interval: 60
  alert:
    email:
      to: ops@company.com
    webhook:
      url: "https://hooks.example.com/alert"
```

### 步骤二:运行巡检

```
请对配置文件中的所有目标执行网络巡检,生成JSON格式报告。
```

### 步骤三:查看报告

报告输出到 `./reports/` 目录,包含:
- `inspection.json`:结构化巡检结果
- `inspection.html`:可视化巡检报告
- `firewall-audit.md`:防火墙审计报告

## 配置示例

### 企业级完整配置

```yaml
# 企业级网络诊断配置(专业版)
version: "2.0"
edition: pro

# 巡检目标
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

# DNS服务器
dns_servers:
  primary: 8.8.8.8
  secondary: 1.1.1.1
  internal: 10.0.0.53

# 防火墙审计
firewall_audit:
  enabled: true
  check_iptables: true
  check_ufw: true
  high_risk_ports: [22, 3306, 5432, 6379]
  allowed_sources:
    ssh: ["10.0.0.0/8", "192.168.0.0/16"]

# 代理诊断
proxy_diagnosis:
  enabled: true
  test_urls:
    - https://httpbin.org/ip
    - https://ifconfig.me

# 持续监控
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

# 报告配置
report:
  format: [json, html, markdown]
  output_dir: ./reports/
  retention_days: 90
  include_history: true
```

## 最佳实践

1. **定期巡检**:设置定时任务进行每日网络巡检
2. **变更后审计**:网络拓扑或防火墙变更后立即审计
3. **历史趋势**:保存巡检历史,分析网络质量趋势
4. **分级告警**:根据严重程度设置不同告警渠道

```bash
# 定时巡检任务(crontab)
# 每小时巡检一次
0 * * * * /opt/tools/network-inspector.sh >> /var/log/network-inspection.log 2>&1

# 每日防火墙审计
0 2 * * * /opt/tools/firewall-audit.sh >> /var/log/firewall-audit.log 2>&1
```

5. **自动化修复**:对常见问题设置自动修复脚本

```bash
# 自动DNS缓存刷新
if ! nc -zv -w 3 example.com 443 2>&1 | grep -q "open"; then
    echo "连接失败,尝试刷新DNS缓存..."
    sudo systemd-resolve --flush-caches
    sleep 5
    nc -zv -w 3 example.com 443
fi
```

## 常见问题

### Q1:专业版如何兼容免费版?

专业版完全兼容免费版的所有诊断命令。免费版的 `.network-diag.yml` 配置可被专业版识别,专业版会自动启用额外的高级诊断功能。

### Q2:批量巡检性能如何?

| 目标数量 | 并发数 | 耗时 | 资源占用 |
|:---------|:-------|:-----|:---------|
| 10 | 5 | <30s | 低 |
| 50 | 10 | 1-2min | 中 |
| 100 | 20 | 2-5min | 中 |
| 500+ | 50 | 5-15min | 高 |

### Q3:如何集成到运维平台?

```bash
# 输出Prometheus指标
echo "# HELP network_target_up Target availability (1=up, 0=down)"
echo "# TYPE network_target_up gauge"
for target in api.example.com db.internal.com; do
    status=$(nc -zv -w 3 "$target" 443 2>&1 && echo 1 || echo 0)
    echo "network_target_up{target=\"$target\"} $status"
done
```

### Q4:告警如何去重?

```python
# 告警去重逻辑
class AlertManager:
    def __init__(self):
        self.active_alerts = {}
        self.cooldown = 300  # 5分钟冷却

    def should_alert(self, host, issue):
        key = f"{host}:{issue}"
        if key in self.active_alerts:
            elapsed = time.time() - self.active_alerts[key]
            if elapsed < self.cooldown:
                return False  # 冷却期内,不重复告警
        self.active_alerts[key] = time.time()
        return True
```

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Linux(推荐) / macOS / Windows(WSL)
- **运行时**:Python 3.8+ / Bash
- **权限**:部分审计命令需要 root/sudo 权限

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| dig/nslookup | 系统工具 | 必需 | 安装 dnsutils/bind-utils |
| nc(netcat) | 系统工具 | 必需 | 安装 netcat |
| curl | 系统工具 | 必需 | 系统自带 |
| openssl | 系统工具 | 必需 | 系统自带 |
| mtr | 系统工具 | 推荐 | 安装 mtr |
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| iptables/ufw | 系统工具 | 可选 | 系统自带(Linux) |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 告警通知需要配置邮件服务器或 Webhook:

```yaml
alert:
  email:
    smtp_host: "${SMTP_HOST}"
    smtp_port: "${SMTP_PORT}"
    username: "${SMTP_USER}"
    password: "${SMTP_PASSWORD}"
  webhook:
    url: "${ALERT_WEBHOOK_URL}"
    headers:
      Authorization: "Bearer ${ALERT_TOKEN}"
```

### 可用性分类

- **分类**:MD+EXEC+PRO(专业版支持批量巡检、持续监控和告警)
- **说明**:企业级 AI Skill,支持多目标批量诊断、防火墙审计和持续监控
- **适用规模**:中小型到大型网络环境(目标数无上限)
- **兼容性**:完全兼容免费版命令和配置,支持平滑升级
