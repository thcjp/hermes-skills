---
slug: dns-networking
name: dns-networking
version: "1.0.0"
displayName: DNS & Networking
summary: "调试DNS解析与网络连通,DNS故障/端口测试一键诊断(社区下载版)"
  failures, testing por...
license: MIT
description: |-
  Debug DNS resolution and network connectivity。Use when troubleshooting
  DNS failures, testing por。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# DNS & Networking

Debug DNS resolution, network connectivity, and HTTP issues. Covers dig/nslookup, port testing, firewall rules, curl diagnostics, /etc/hosts, proxy configuration, and certificate troubleshooting.

## When to Use

* DNS name not resolving or resolving to wrong IP
* Connection refused / connection timed out errors
* Diagnosing firewall or security group rules
* HTTP requests failing for unclear reasons
* Proxy configuration issues
* SSL/TLS certificate errors
* Testing connectivity between services

## DNS Debugging

### Query DNS records

```bash
dig example.com
dig +short example.com

dig example.com MX        # Mail servers
dig example.com CNAME     # Aliases
dig example.com TXT       # Text records (SPF, DKIM, etc.)
dig example.com NS        # Name servers
dig example.com AAAA      # IPv6 address
dig example.com SOA       # Start of Authority

dig @8.8.8.8 example.com
dig @1.1.1.1 example.com

dig +trace example.com

dig -x 93.184.216.34

nslookup example.com
nslookup example.com 8.8.8.8    # Query specific server
nslookup -type=MX example.com

host example.com
host -t MX example.com
```

### Check DNS propagation

```bash
for dns in 8.8.8.8 1.1.1.1 9.9.9.9 208.67.222.222; do
    echo -n "$dns: "
    dig +short @"$dns" example.com
done

dig example.com | grep -E '^\S+\s+\d+\s+IN\s+A'
```

### Local DNS issues

```bash
cat /etc/resolv.conf

cat /etc/hosts

sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
sudo systemd-resolve --flush-caches
ipconfig /flushdns

resolvectl status
```

### /etc/hosts patterns

```bash

127.0.0.1    myapp.local
127.0.0.1    api.myapp.local

0.0.0.0      ads.example.com

203.0.113.50    example.com
203.0.113.50    www.example.com

192.168.1.100   db.local redis.local cache.local
```

## Port and Connectivity Testing

### Test if a port is open

```bash
nc -zv example.com 443
nc -zv -w 5 example.com 80    # 5 second timeout

for port in 22 80 443 5432 6379; do
    nc -zv -w 2 example.com $port 2>&1
done

timeout 3 bash -c 'echo > /dev/tcp/example.com/443' && echo "Open" || echo "Closed"

curl -sI -o /dev/null -w "%{http_code}" https://example.com

docker exec my-container nc -zv db 5432
```

### Network path diagnostics

```bash
traceroute example.com

mtr example.com
mtr -r -c 20 example.com   # Report mode, 20 packets

ping -c 5 example.com

ip addr show          # Linux
ifconfig              # macOS / older Linux

ip route show         # Linux
netstat -rn           # macOS
route -n              # Linux (older)
```

### Check listening ports

```bash
ss -tlnp
ss -tlnp | grep :8080

lsof -i -P -n | grep LISTEN
lsof -i :8080

netstat -tlnp
netstat -tlnp | grep :8080

lsof -i :3000
fuser 3000/tcp   # Linux
```

## curl Diagnostics

### Verbose request inspection

```bash
curl -v https://api.example.com/endpoint

curl -o /dev/null -s -w "
    DNS:        %{time_namelookup}s
    Connect:    %{time_connect}s
    TLS:        %{time_appconnect}s
    TTFB:       %{time_starttransfer}s
    Total:      %{time_total}s
    Status:     %{http_code}
    Size:       %{size_download} bytes
" https://api.example.com/endpoint

curl -sI https://api.example.com/endpoint

curl -sIL https://example.com

curl --resolve example.com:443:203.0.113.50 https://example.com

curl --interface eth1 https://example.com
```

### Debug common HTTP issues

```bash
curl --http1.1 https://example.com
curl --http2 https://example.com

curl --tlsv1.2 https://example.com
curl --tlsv1.3 https://example.com

curl -k https://self-signed.example.com

curl -H "Host: example.com" https://203.0.113.50/

curl -X OPTIONS -H "Origin: http://localhost:3000" \
     -H "Access-Control-Request-Method: POST" \
     -v https://api.example.com/endpoint
```

## Firewall Basics

### iptables (Linux)

```bash
sudo iptables -L -n -v

sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT

sudo iptables -A INPUT -s 203.0.113.0/24 -p tcp --dport 22 -j ACCEPT

sudo iptables -A INPUT -p tcp --dport 3306 -j DROP

sudo iptables-save > /etc/iptables/rules.v4
```

### ufw (simpler, Ubuntu/Debian)

```bash
sudo ufw enable

sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow from 203.0.113.0/24 to any port 22
sudo ufw deny 3306

sudo ufw status verbose

sudo ufw reset
```

### macOS firewall

```bash
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate

sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on

sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/local/bin/myapp
```

## Proxy Configuration

### Environment variables

```bash
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
export NO_PROXY=localhost,127.0.0.1,.internal.example.com

export http_proxy=http://proxy.example.com:8080  # lowercase also works

export HTTPS_PROXY=http://user:password@proxy.example.com:8080
```

### Test through proxy

```bash
curl -x http://proxy.example.com:8080 https://httpbin.org/ip

curl --socks5 localhost:1080 https://httpbin.org/ip

curl -x http://proxy:8080 https://httpbin.org/ip
curl https://httpbin.org/ip  # Compare with direct

curl -v -x http://proxy:8080 https://example.com 2>&1 | grep -i "proxy\|connect"
```

### Common proxy issues

```bash

git config --global http.proxy http://proxy:8080
git config --global https.proxy http://proxy:8080
git config --global --unset http.proxy

npm config set proxy http://proxy:8080
npm config set https-proxy http://proxy:8080

pip install --proxy http://proxy:8080 package-name
```

## 错误处理

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | \
  openssl x509 -noout -subject -issuer -dates

echo | openssl s_client -connect example.com:443 2>/dev/null | \
  openssl x509 -noout -enddate

openssl s_client -showcerts -connect example.com:443 < /dev/null 2>/dev/null | \
  awk '/BEGIN CERT/,/END CERT/' > chain.pem

openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt server.pem

openssl s_client -connect cdn.example.com:443 -servername cdn.example.com

date
```

## Quick Diagnostics Script

```bash
#!/bin/bash
TARGET="${1:?Usage: net-check.sh <hostname> [port]}"
PORT="${2:-443}"

echo "=== Network Check: $TARGET:$PORT ==="

echo -n "DNS resolution: "
IP=$(dig +short "$TARGET" | head -1)
[[ -n "$IP" ]] && echo "$IP" || echo "FAILED"

echo -n "Ping: "
ping -c 1 -W 3 "$TARGET" > /dev/null 2>&1 && echo "OK" || echo "FAILED (may be blocked)"

echo -n "Port $PORT: "
nc -zv -w 5 "$TARGET" "$PORT" 2>&1 | grep -q "succeeded\|open" && echo "OPEN" || echo "CLOSED/FILTERED"

if [[ "$PORT" == "443" || "$PORT" == "8443" ]]; then
    echo -n "TLS: "
    echo | openssl s_client -connect "$TARGET:$PORT" -servername "$TARGET" 2>/dev/null | \
      grep -q "Verify return code: 0" && echo "VALID" || echo "INVALID/ERROR"

    echo -n "Certificate expiry: "
    echo | openssl s_client -connect "$TARGET:$PORT" 2>/dev/null | \
      openssl x509 -noout -enddate 2>/dev/null | sed 's/notAfter=//'
fi

echo "=== Done ==="
```

## Tips

* `dig +short` is the fastest way to check DNS from the command line. Use `@8.8.8.8` to bypass local caching.
* `nc -zv` is the simplest port connectivity test. If nc isn't available, use bash's `/dev/tcp`.
* curl's `-w` format string with timing variables is the fastest way to diagnose slow HTTP requests: DNS, connect, TLS, and TTFB are all visible.
* DNS changes propagate based on TTL. Check the current TTL with `dig` before expecting a DNS change to take effect.
* `/etc/hosts` changes take effect immediately (no TTL, no propagation delay). Use it to test domain migrations before changing DNS.
* When debugging "connection refused": first verify the port is open with `nc`, then check the service is actually listening with `ss -tlnp` or `lsof -i`.
* `mtr` is better than `traceroute` for diagnosing packet loss — it runs continuously and shows per-hop loss percentages.
* Node.js, Python `requests`, and many libraries do NOT automatically use `HTTP_PROXY` environment variables. Check each tool's proxy documentation.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Debug DNS resolution and network connectivity
- Use when troubleshooting
  DNS failures, testing por
- 触发关键词: network, dns, debug, connectivity, resolution, networking

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 常见问题

### Q1: 如何开始使用DNS & Networking？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: DNS & Networking有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
