---
slug: "dns-networking-paid"
name: "dns-networking-paid"
version: 1.0.1
displayName: "DNS网络诊断专业版"
summary: "企业级网络诊断,支持批量巡检、防火墙审计、代理链分析与持续监控告警。。面向运维团队的企业级网络诊断工具,提供批量目标巡检、防火墙规则审计、代理链完整分析、持续监控与告警通知。核心能力: -"
license: "Proprietary"
edition: "pro"
description: |-
  面向运维团队的企业级网络诊断工具,提供批量目标巡检、防火墙规则审计、代理链完整分析、持续监控与告警通知。核心能力:
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
  - 专业版完全兼容免费版命令...
tags:
  - 开发工具
  - 网络诊断
  - 运维监控
  - 企业级
  - 网络
  - DNS
  - 工具
  - echo
  - grep
  - sudo
  - iptables
  - bash
tools:
  - read
  - exec
homepage: ""
# 定价元数据
category: "Operations"
---
# DNS网络诊断专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| DNS网络诊断专业版代理链分析与持续监控 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 核心能力

### 1. 批量多目标巡检
支持对多个目标进行批量DNS解析、端口连通性和证书检查.
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供批量多目标巡检所需的指令和必要参数.
**输出**: 返回批量多目标巡检的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 防火墙规则审计
审计 iptables/ufw/云安全组规则,发现潜在安全风险.
```bash
#!/bin/bash
echo "=== 防火墙规则审计 ==="
# ...
echo "--- iptables规则 ---"
sudo iptables -L -n -v
# ...
echo "--- 检查高危规则 ---"
echo "[警告] 开放给所有IP的SSH:"
sudo iptables -L -n | grep -E "dpt:22\s*$" | grep -v "DROP\|REJECT"
# ...
echo "[警告] 开放给所有IP的数据库端口:"
sudo iptables -L -n | grep -E "dpt:(3306|5432|6379|27017)\s*$"
# ...
echo "[警告] 允许转发:"
sudo iptables -L FORWARD -n | grep -v "Chain\|target\|^$"
# ...
echo "--- ufw状态 ---"
sudo ufw status verbose
# ...
echo "--- ufw高危规则 ---"
sudo ufw status | grep -E "ALLOW.*ANYWHERE"
# ...
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

**输入**: 用户提供防火墙规则审计所需的指令和必要参数。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `防火墙规则审计` 选项

### 3. 代理链完整诊断
完整诊断 HTTP/HTTPS/SOCKS5 代理链路.
```bash
#!/bin/bash
echo "=== 代理链诊断 ==="
# ...
echo "--- 代理环境变量 ---"
echo "HTTP_PROXY:  ${HTTP_PROXY:-未设置}"
echo "HTTPS_PROXY: ${HTTPS_PROXY:-未设置}"
echo "NO_PROXY:    ${NO_PROXY:-未设置}"
# ...
echo -e "\n--- 直连测试 ---"
curl -o /dev/null -s -w "直连耗时: %{time_total}s, 状态码: %{http_code}\n" \
  https://httpbin.org/ip
# ...
if [ -n "$HTTP_PROXY" ]; then
    echo -e "\n--- HTTP代理测试 ---"
    curl -x "$HTTP_PROXY" -o /dev/null -s -w \
      "代理耗时: %{time_total}s, 状态码: %{http_code}\n" \
      https://httpbin.org/ip
# ...
    echo -e "\n--- 代理详细信息 ---"
    curl -v -x "$HTTP_PROXY" https://httpbin.org/ip 2>&1 | \
      grep -i "proxy\|connect"
fi
# ...
echo -e "\n--- SOCKS5代理测试 ---"
curl --socks5 localhost:1080 -o /dev/null -s -w \
  "SOCKS5耗时: %{time_total}s, 状态码: %{http_code}\n" \
  https://httpbin.org/ip 2>/dev/null || echo "SOCKS5代理不可用"
# ...
echo -e "\n--- 工具代理配置 ---"
echo "Git代理:    $(git config --global http.proxy 2>/dev/null || echo '未设置')"
echo "npm代理:    $(npm config get proxy 2>/dev/null || echo '未设置')"
echo "pip代理:    $(pip config list 2>/dev/null | grep proxy || echo '未设置')"
```

**处理**: 解析代理链完整诊断的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回代理链完整诊断的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `代理链完整诊断` 选项

### 4. 持续监控与告警
定时监控目标可用性,异常时发送告警.
**输入**: 用户提供持续监控与告警所需的指令和必要参数.
**输出**: 返回持续监控与告警的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 网络路径分析
使用 mtr 进行持续路径分析,发现网络抖动和丢包.
```bash
echo "=== 网络路径分析 ==="
# ...
mtr -r -c 100 example.com
# ...
mtr --report --report-cycles 20 --json example.com > path-analysis.json
# ...
traceroute -n example.com
# ...
for target in api.example.com cdn.example.com db.example.com; do
    echo "--- $target ---"
    mtr -r -c 20 "$target"
    echo ""
done
```

**输入**: 用户提供网络路径分析所需的指令和必要参数.
**输出**: 返回网络路径分析的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `网络路径分析` 选项

#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一:生产环境网络巡检
对生产环境所有服务进行批量网络巡检.
```bash
#!/bin/bash
echo "=== 生产环境网络巡检 ==="
echo "时间: $(date)"
echo ""
# ...
TARGETS=$(cat << 'EOF'
api.example.com:443
app.example.com:443
db.internal:5432
cache.internal:6379
mq.internal:5672
EOF
)
# ...
while IFS=':' read -r host port; do
    echo -n "$host:$port -> "
    if nc -zv -w 3 "$host" "$port" 2>&1 | grep -q "succeeded\|open"; then
        latency=$(curl -o /dev/null -s -w "%{time_total}" "https://$host" 2>/dev/null || echo "N/A")
        echo "OK (延迟: ${latency}s)"
    else
        echo "FAIL"
    fi
done <<< "$TARGETS"
# ...
echo ""
echo "=== 巡检报告已生成: network-inspection-$(date +%Y%m%d).json ==="
```

### 场景二:防火墙策略变更审计
变更防火墙规则后进行审计验证.
```bash
#!/bin/bash
echo "=== 防火墙变更审计 ==="
# ...
sudo iptables-save > "iptables-backup-$(date +%Y%m%d).rules"
echo "规则已备份"
# ...
echo "--- 安全审计 ---"
# ...
echo "1. 检查开放端口:"
sudo iptables -L INPUT -n --line-numbers | grep ACCEPT
# ...
echo -e "\n2. 检查来源限制:"
sudo iptables -L INPUT -n -v | grep -v "0.0.0.0/0" | grep ACCEPT
# ...
echo -e "\n3. 检查高危端口:"
for port in 22 3306 5432 6379 27017; do
    matches=$(sudo iptables -L INPUT -n | grep "dpt:$port" | grep ACCEPT)
    if [ -n "$matches" ]; then
        echo "[!] 端口 $port 开放: $matches"
    fi
done
```

### 场景三:混合云连通性验证
验证混合云环境各节点间连通性.
```bash
#!/bin/bash
echo "=== 混合云连通性验证 ==="
# ...
declare -A NODES
NODES["公有云API"]="api.cloud.com:443"
NODES["私有云DB"]="db.private.cloud:5432"
NODES["边缘节点1"]="edge1.region1:443"
NODES["边缘节点2"]="edge2.region2:443"
# ...
for name in "${!NODES[@]}"; do
    IFS=':' read -r host port <<< "${NODES[$name]}"
    echo -n "$name ($host:$port): "
# ...
    ip=$(dig +short "$host" | head -1)
    if [ -z "$ip" ]; then
        echo "DNS解析失败"
        continue
    fi
# ...
    if nc -zv -w 3 "$host" "$port" 2>&1 | grep -q "open\|succeeded"; then
        latency=$(ping -c 3 -W 3 "$host" 2>/dev/null | tail -1 | awk -F'/' '{print $5}')
        echo "OK (IP: $ip, 延迟: ${latency}ms)"
    else
        echo "FAIL (IP: $ip)"
    fi
done
```

## 使用流程

### 步骤一:配置巡检目标
创建 `.network-inspector.yml` 配置文件:

```yaml
version: "2.0"
edition: pro
# ...
targets:
  - host: api.example.com
    ports: [80, 443]
    check_cert: true
  - host: db.internal.com
    ports: [5432, 6379]
    check_cert: false
# ...
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
请对配置文件中的所有目标执行网络巡检,生成JSON格式报告.
```

### 步骤三:查看报告
报告输出到 `./reports/` 目录,包含:
1. `inspection.json`:结构化巡检结果
2. `inspection.html`:可视化巡检报告
3. `firewall-audit.md`:防火墙审计报告

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | dns-networking处理的内容输入 |, 默认: 全部维度 |
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

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Linux(推荐) / macOS / Windows(WSL)
- **运行时**:Python 3.8+ / Bash
- **权限**:部分审计命令需要 root/sudo 权限

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
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

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100
# ...
检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100
# ...
检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100
# ...
检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过
# ...
改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1:专业版如何兼容免费版?
专业版完全兼容免费版的所有诊断命令。免费版的 `.network-diag.yml` 配置可被专业版识别,专业版会自动启用额外的高级诊断功能.
### Q2:批量巡检性能如何?
| 目标数量 | 并发数 | 耗时 | 资源占用 |
|:------|------:|:------|:------|
| 10 | 5 | <30s | 低 |
| 50 | 10 | 1-2min | 中 |
| 100 | 20 | 2-5min | 中 |
| 500+ | 50 | 5-15min | 高 |

### Q3:如何集成到运维平台?
```bash
echo "# HELP network_target_up Target availability (1=up, 0=down)"
echo "# TYPE network_target_up gauge"
for target in api.example.com db.internal.com; do
    status=$(nc -zv -w 3 "$target" 443 2>&1 && echo 1 || echo 0)
    echo "network_target_up{target=\"$target\"} $status"
done
```

### Q4:告警如何去重?
```python
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

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

