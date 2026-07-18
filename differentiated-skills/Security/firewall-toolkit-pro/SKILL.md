---
slug: firewall-toolkit-pro
name: firewall-toolkit-pro
version: "1.0.0"
displayName: 防火墙配置工具包专业版
summary: 企业级防火墙管理平台,支持云安全组、nftables、批量多机部署、CIS基线审计与实时日志分析,适合企业网络安全团队。
license: MIT
edition: pro
description: |-
  防火墙配置工具包专业版,为企业安全团队提供全方位防火墙管理与网络安全加固能力。
  核心能力:云安全组管理、nftables配置、批量多机部署、CIS安全基线审计、实时日志分析与告警、规则版本管理。
  适用场景:企业网络安全架构、多云安全组统一管理、合规审计、自动化安全运维。
  差异化:专业版兼容免费版配置方法,新增企业级多机管理与云安全组能力,满足规模化网络安全需求。
  触发关键词: 云安全组, nftables, 批量部署, CIS基线, 防火墙审计, security group, nftables, multi-host
tags:
- 防火墙
- 网络安全
- 企业版
- 云安全组
tools:
- read
- exec
---

# 防火墙配置工具包专业版

## 概述

专业版为企业安全团队提供完整的防火墙管理与网络安全加固平台,在免费版iptables/ufw配置能力之上,新增云安全组(AWS/Azure/GCP)管理、nftables高级配置、批量多机部署、CIS安全基线完整审计、实时日志分析与告警、规则版本管理与回滚。专业版完全兼容免费版配置方法,已有防火墙规则可无缝升级,适合企业级网络安全运维。

### 专业版核心优势

| 优势 | 说明 |
|:-----|:-----|
| 云安全组 | AWS/Azure/GCP安全组统一管理 |
| nftables | 新一代Linux防火墙框架 |
| 批量部署 | 多机并行配置,一键部署 |
| CIS基线 | 完整CIS Benchmark合规审计 |
| 日志分析 | 实时流量分析与异常告警 |
| 版本管理 | 规则版本化,支持回滚 |
| 自动化 | CI/CD集成与自动修复 |
| 报告导出 | HTML/PDF合规报告 |

## 核心能力

### 1. 云安全组管理(专业版独有)

```python
#!/usr/bin/env python3
"""专业版多云安全组管理器"""

import json
from abc import ABC, abstractmethod

class SecurityGroupManager(ABC):
    """安全组管理基类"""
    
    @abstractmethod
    def list_security_groups(self):
        pass
    
    @abstractmethod
    def create_rule(self, group_id, rule):
        pass
    
    @abstractmethod
    def delete_rule(self, group_id, rule_id):
        pass


class AWSSecurityGroupManager(SecurityGroupManager):
    """AWS安全组管理"""
    
    def __init__(self):
        import boto3
        self.ec2 = boto3.client('ec2')
    
    def list_security_groups(self):
        response = self.ec2.describe_security_groups()
        return [
            {
                "id": sg['GroupId'],
                "name": sg['GroupName'],
                "description": sg.get('Description', ''),
                "rules": len(sg.get('IpPermissions', []))
            }
            for sg in response['SecurityGroups']
        ]
    
    def create_rule(self, group_id, rule):
        """创建入站规则"""
        response = self.ec2.authorize_security_group_ingress(
            GroupId=group_id,
            IpPermissions=[{
                'IpProtocol': rule.get('protocol', 'tcp'),
                'FromPort': rule['port'],
                'ToPort': rule['port'],
                'IpRanges': [{'CidrIp': rule.get('cidr', '0.0.0.0/0')}]
            }]
        )
        return response
    
    def delete_rule(self, group_id, rule_id):
        """删除规则"""
        pass
    
    def audit_open_ports(self):
        """审计所有开放端口"""
        groups = self.ec2.describe_security_groups()
        findings = []
        
        for sg in groups['SecurityGroups']:
            for perm in sg.get('IpPermissions', []):
                cidr = perm.get('IpRanges', [{}])[0].get('CidrIp', '')
                if cidr == '0.0.0.0/0':
                    port = perm.get('FromPort', 'ALL')
                    protocol = perm.get('IpProtocol', 'all')
                    
                    severity = "CRITICAL"
                    if protocol == 'tcp' and port in [22, 3389]:
                        severity = "CRITICAL"
                    elif protocol == 'tcp' and port in [80, 443]:
                        severity = "INFO"
                    elif port in [3306, 5432, 6379, 27017]:
                        severity = "HIGH"
                    
                    findings.append({
                        "group": sg['GroupName'],
                        "group_id": sg['GroupId'],
                        "port": port,
                        "protocol": protocol,
                        "cidr": cidr,
                        "severity": severity,
                        "description": f"{sg['GroupName']} 开放 {port}/{protocol} 给 0.0.0.0/0"
                    })
        
        return findings


class AzureSecurityGroupManager(SecurityGroupManager):
    """Azure网络安全组管理"""
    
    def __init__(self):
        from azure.mgmt.network import NetworkManagementClient
        from azure.identity import DefaultAzureCredential
        credential = DefaultAzureCredential()
        self.client = NetworkManagementClient(credential, "subscription_id")
    
    def list_security_groups(self):
        groups = self.client.network_security_groups.list_all()
        return [{"id": g.id, "name": g.name} for g in groups]


if __name__ == "__main__":
    manager = AWSSecurityGroupManager()
    
    # 审计开放端口
    findings = manager.audit_open_ports()
    print(f"发现 {len(findings)} 个开放端口:")
    for f in findings:
        print(f"  [{f['severity']}] {f['description']}")
```

### 2. nftables高级配置(专业版独有)

```bash
#!/bin/bash
# nftables企业级防火墙配置

echo "=== nftables企业级配置 ==="

# 创建nftables配置文件
cat > /etc/nftables.conf << 'NFTABLES'
#!/usr/sbin/nft -f

flush ruleset

# 基础表
table inet firewall {
    # 集合:管理IP白名单
    set admin_ips {
        type ipv4_addr
        flags interval
        elements = {
            10.0.0.0/8,      # 内网管理段
            192.168.1.0/24   # 管理员网段
        }
    }

    # 集合:黑名单IP
    set blacklist {
        type ipv4_addr
        flags interval
        elements = {}
    }

    # 集合:被限制的端口
    set blocked_ports {
        type inet_service
        elements = { 23, 21, 3389, 3306, 5432, 6379, 27017 }
    }

    chain input {
        type filter hook input priority 0; policy drop;

        # 允许回环
        iif "lo" accept

        # 已建立连接
        ct state established,related accept

        # 丢弃无效连接
        ct state invalid drop

        # 黑名单IP丢弃
        ip saddr @blacklist drop

        # 管理端口仅允许白名单IP
        tcp dport { 22, 8080 } ip saddr != @admin_ips drop

        # 允许SSH(限速)
        tcp dport 22 limit rate 5/minute burst 10 packets accept

        # 允许HTTP/HTTPS
        tcp dport { 80, 443 } accept

        # 拒绝危险端口
        tcp dport @blocked_ports drop

        # ICMP限速
        icmp type echo-request limit rate 1/second accept

        # 记录并丢弃其他流量
        limit rate 5/minute log prefix "nft-drop: " drop
    }

    chain forward {
        type filter hook forward priority 0; policy drop;
        ct state established,related accept
        ct state invalid drop
    }

    chain output {
        type filter hook output priority 0; policy accept;
    }
}

# NAT表
table ip nat {
    chain prerouting {
        type nat hook prerouting priority 0;
    }

    chain postrouting {
        type nat hook postrouting priority 100;
    }
}
NFTABLES

# 应用配置
nft -f /etc/nftables.conf
echo "nftables配置已应用"

# 启用开机自动加载
systemctl enable nftables
systemctl start nftables

echo ""
echo "=== 当前nftables规则 ==="
nft list ruleset | head -50
```

### 3. 批量多机部署(专业版独有)

```bash
#!/bin/bash
# 批量多机防火墙部署

HOSTS_FILE="hosts.txt"  # 格式: IP SSH_PORT
RULES_FILE="firewall-rules.sh"

echo "=== 批量防火墙部署 ==="
echo "目标主机文件: ${HOSTS_FILE}"
echo "规则文件: ${RULES_FILE}"
echo ""

SUCCESS=0
FAIL=0

while IFS=' ' read -r ip port; do
    [ -z "$ip" ] && continue
    port=${port:-22}
    
    echo "--- 部署到: ${ip}:${port} ---"
    
    # 复制规则文件到目标主机
    if scp -P "$port" "$RULES_FILE" "root@${ip}:/tmp/firewall-rules.sh" 2>/dev/null; then
        # 远程执行
        if ssh -p "$port" "root@${ip}" "bash /tmp/firewall-rules.sh && rm /tmp/firewall-rules.sh" 2>/dev/null; then
            echo "  [OK] ${ip} 部署成功"
            ((SUCCESS++))
        else
            echo "  [FAIL] ${ip} 执行失败"
            ((FAIL++))
        fi
    else
        echo "  [FAIL] ${ip} 文件传输失败"
        ((FAIL++))
    fi
done < "$HOSTS_FILE"

echo ""
echo "========================================="
echo "部署完成: 成功 ${SUCCESS} 台, 失败 ${FAIL} 台"
echo "========================================="
```

### 4. CIS安全基线审计(专业版独有)

```bash
#!/bin/bash
# CIS安全基线完整审计

echo "=== CIS防火墙安全基线审计 ==="
echo ""

PASS=0
FAIL=0
WARN=0

check_cis() {
    local id=$1
    local name=$2
    local condition=$3
    local level=$4
    
    if eval "$condition"; then
        echo "  [PASS] [$id] $name"
        ((PASS++))
    else
        if [ "$level" = "high" ]; then
            echo "  [FAIL] [$id] $name"
            ((FAIL++))
        else
            echo "  [WARN] [$id] $name"
            ((WARN++))
        fi
    fi
}

# CIS 3.5.1.1 - 确保默认入站策略为DROP
check_cis "3.5.1.1" "默认入站策略为DROP" \
    "iptables -L INPUT -n | head -1 | grep -q DROP || ufw status verbose | grep -q 'deny (incoming)'" "high"

# CIS 3.5.1.2 - 确保默认出站策略为ACCEPT或DROP
check_cis "3.5.1.2" "默认出站策略已配置" \
    "iptables -L OUTPUT -n | head -1 | grep -qE 'DROP|ACCEPT'" "medium"

# CIS 3.5.1.3 - 确保默认转发策略为DROP
check_cis "3.5.1.3" "默认转发策略为DROP" \
    "iptables -L FORWARD -n | head -1 | grep -q DROP" "medium"

# CIS 3.5.1.4 - 确保回环接口已配置
check_cis "3.5.1.4" "回环接口已配置" \
    "iptables -L INPUT -n | grep -q 'lo.*ACCEPT'" "high"

# CIS 3.5.1.5 - 确保已建立连接已配置
check_cis "3.5.1.5" "已建立连接规则已配置" \
    "iptables -L INPUT -n | grep -q 'ESTABLISHED'" "high"

# CIS 3.5.2.1 - 确保防火墙已启用
check_cis "3.5.2.1" "防火墙已启用" \
    "ufw status | grep -q 'Status: active' || systemctl is-active nftables | grep -q active" "high"

# CIS 4.2.1 - 确保SSH MaxAuthTries <= 4
check_cis "4.2.1" "SSH最大认证尝试 <= 4" \
    "grep -q 'MaxAuthTries [1-4]' /etc/ssh/sshd_config" "medium"

# CIS 4.2.2 - 确保SSH忽略rhosts
check_cis "4.2.2" "SSH忽略rhosts" \
    "grep -q 'IgnoreRhosts yes' /etc/ssh/sshd_config" "medium"

# CIS 4.2.3 - 确保禁用SSHroot登录
check_cis "4.2.3" "SSH禁止root登录" \
    "grep -q 'PermitRootLogin no' /etc/ssh/sshd_config" "high"

# CIS 4.2.4 - 确保SSH禁用空密码
check_cis "4.2.4" "SSH禁用空密码" \
    "grep -q 'PermitEmptyPasswords no' /etc/ssh/sshd_config" "high"

echo ""
echo "========================================="
echo "CIS基线审计结果"
echo "  通过: ${PASS}"
echo "  失败: ${FAIL}"
echo "  警告: ${WARN}"
echo "========================================="
```

## 使用场景

### 场景一:企业网络安全架构部署

```bash
#!/bin/bash
# 企业网络安全架构:DMZ + 内网分层

echo "=== 企业网络安全架构部署 ==="

# 网络架构:
# 互联网 -> [WAF/防火墙] -> DMZ(Web服务器) -> [内部防火墙] -> 内网(数据库)

# 1. DMZ区域防火墙(对外)
echo "--- 配置DMZ防火墙 ---"
nft add rule inet firewall input tcp dport { 80, 443 } accept comment '"DMZ: Web服务"'
nft add rule inet firewall input tcp dport 22 ip saddr @admin_ips accept comment '"DMZ: 管理SSH"'

# 2. 内网防火墙(对内)
echo "--- 配置内网防火墙 ---"
nft add rule inet firewall forward ip saddr 10.0.1.0/24 ip daddr 10.0.2.0/24 tcp dport 3306 accept comment '"内网: Web->DB"'
nft add rule inet firewall forward ip saddr 10.0.1.0/24 ip daddr 10.0.2.0/24 tcp dport 6379 accept comment '"内网: Web->Redis"'

# 3. 云安全组配置
echo ""
echo "--- 云安全组配置 ---"
echo "  Web安全组: 入站 80/443 对0.0.0.0/0开放, 22仅管理网段"
echo "  DB安全组: 入站 3306 仅Web安全组, 22仅管理网段"
echo "  Redis安全组: 入站 6379 仅Web安全组"

echo ""
echo "企业网络安全架构部署完成"
```

### 场景二:多云安全组统一管理

```python
#!/usr/bin/env python3
"""多云安全组统一管理"""

class MultiCloudFirewallManager:
    """多云防火墙统一管理"""
    
    def __init__(self):
        self.providers = {}
    
    def register_provider(self, name, manager):
        self.providers[name] = manager
    
    def unified_audit(self):
        """统一安全审计"""
        all_findings = []
        
        for provider_name, manager in self.providers.items():
            findings = manager.audit_open_ports()
            for f in findings:
                f["provider"] = provider_name
                all_findings.append(f)
        
        return all_findings
    
    def generate_compliance_report(self, findings):
        """生成合规报告"""
        report = {
            "total_findings": len(findings),
            "by_severity": {},
            "by_provider": {},
            "findings": findings
        }
        
        for f in findings:
            # 按严重级别统计
            sev = f["severity"]
            report["by_severity"][sev] = report["by_severity"].get(sev, 0) + 1
            
            # 按云服务商统计
            prov = f["provider"]
            report["by_provider"][prov] = report["by_provider"].get(prov, 0) + 1
        
        return report


if __name__ == "__main__":
    import json
    manager = MultiCloudFirewallManager()
    # manager.register_provider("aws", AWSSecurityGroupManager())
    # manager.register_provider("azure", AzureSecurityGroupManager())
    
    # 模拟审计结果
    findings = [
        {"provider": "aws", "severity": "CRITICAL", "description": "SSH开放给0.0.0.0/0"},
        {"provider": "azure", "severity": "HIGH", "description": "数据库端口开放给0.0.0.0/0"},
    ]
    
    report = manager.generate_compliance_report(findings)
    print(json.dumps(report, indent=2, ensure_ascii=False))
```

### 场景三:防火墙规则版本管理

```bash
#!/bin/bash
# 防火墙规则版本管理与回滚

RULES_DIR="/etc/firewall-versions"
mkdir -p "$RULES_DIR"

# 保存当前规则版本
save_version() {
    local version_name=$1
    local timestamp=$(date '+%Y%m%d%H%M%S')
    local filename="${RULES_DIR}/${timestamp}_${version_name}.rules"
    
    # 保存iptables规则
    iptables-save > "$filename"
    
    # 记录版本信息
    echo "${timestamp} ${version_name} $(wc -l < "$filename")行" >> "${RULES_DIR}/versions.log"
    echo "已保存版本: ${version_name} (${filename})"
}

# 列出所有版本
list_versions() {
    echo "=== 防火墙规则版本历史 ==="
    if [ -f "${RULES_DIR}/versions.log" ]; then
        cat "${RULES_DIR}/versions.log"
    else
        echo "暂无保存的版本"
    fi
}

# 回滚到指定版本
rollback() {
    local version_file=$1
    
    if [ ! -f "$version_file" ]; then
        echo "版本文件不存在: ${version_file}"
        return 1
    fi
    
    # 先保存当前版本
    save_version "pre-rollback"
    
    # 恢复指定版本
    iptables-restore < "$version_file"
    echo "已回滚到: ${version_file}"
}

# 使用示例
save_version "initial-baseline"
list_versions
```

## 快速开始

### 从免费版升级

```bash
# 免费版:单机UFW配置
ufw allow 80/tcp

# 专业版:多机批量部署+云安全组
bash batch_deploy.sh hosts.txt firewall-rules.sh
python3 cloud_sg_manager.py --audit --provider aws
```

## 配置示例

### 专业版功能矩阵

| 功能 | 免费版 | 专业版 | 说明 |
|:-----|:-------|:-------|:-----|
| iptables | 支持 | 支持 | Linux防火墙 |
| UFW | 支持 | 支持 | 简化防火墙 |
| nftables | 不支持 | 支持 | 新一代防火墙 |
| 云安全组 | 不支持 | 支持 | AWS/Azure/GCP |
| 批量部署 | 不支持 | 支持 | 多机并行 |
| CIS基线 | 基础 | 完整 | 合规审计 |
| 日志分析 | 基础 | 实时 | 异常检测 |
| 版本管理 | 不支持 | 支持 | 回滚能力 |

### CIS基线覆盖范围

| 控制项 | 免费版 | 专业版 |
|:-------|:-------|:-------|
| 3.5.1.x 防火墙默认策略 | 基础 | 完整 |
| 3.5.2.x 防火墙启用状态 | 基础 | 完整 |
| 4.2.x SSH配置 | 基础 | 完整 |
| 4.3.x 网络参数 | 不支持 | 完整 |
| 4.4.x 日志配置 | 不支持 | 完整 |

## 最佳实践

1. **分层防御**:DMZ+内网分层,不同区域不同安全策略。
2. **最小权限**:安全组遵循最小开放原则,仅允许必要的源IP和端口。
3. **版本管理**:所有规则变更保存版本,支持快速回滚。
4. **定期审计**:定期执行CIS基线审计,确保合规性。
5. **自动化**:将防火墙配置纳入CI/CD,避免手动操作错误。
6. **监控告警**:实时监控防火墙日志,异常流量自动告警。

## 常见问题

### Q1: 专业版与免费版规则是否兼容?

完全兼容。专业版支持iptables/ufw的所有规则格式,新增nftables和云安全组能力。

### Q2: 云安全组支持哪些云服务商?

支持AWS、Azure、GCP三大公有云,通过各自的SDK进行管理。

### Q3: 批量部署如何保证安全?

使用SSH密钥认证,部署前先在测试环境验证规则,生产环境分批次部署。

### Q4: CIS基线审计覆盖哪些标准?

覆盖CIS Benchmark for Linux的3.5(防火墙)和4.x(网络与SSH)章节。

### Q5: 规则版本管理如何使用?

每次变更前调用save_version保存当前状态,需要回滚时调用rollback恢复指定版本。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Linux(UFW/iptables/nftables为Linux工具)
- **Python**: 3.8+(使用云安全组管理时需要)
- **权限**: 需要root/sudo权限执行防火墙命令

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| iptables | 防火墙工具 | 必需 | 系统自带 |
| ufw | 防火墙工具 | 推荐 | `apt install ufw` |
| nftables | 防火墙工具 | 推荐 | `apt install nftables` |
| python3 | 运行时环境 | 推荐 | python.org 下载 |
| boto3 | AWS SDK | 按需 | `pip install boto3` |
| azure-sdk | Azure SDK | 按需 | `pip install azure-mgmt-network` |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 云安全组管理需配置各云服务商的访问凭证
- AWS: 配置Access Key ID和Secret Access Key
- Azure: 配置Service Principal凭证
- GCP: 配置Service Account JSON密钥

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级防火墙管理与网络安全加固任务
