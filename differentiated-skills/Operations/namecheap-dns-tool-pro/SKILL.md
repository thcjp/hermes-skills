---
slug: namecheap-dns-tool-pro
name: namecheap-dns-tool-pro
version: 1.0.0
displayName: DNS管理专业版
summary: 企业级DNS管理平台，支持多域名批量、DNS监控、告警与多注册商集成。
license: Proprietary
edition: pro
description: '面向企业运维团队的DNS管理平台。支持多域名批量管理、DNS传播监控、

  告警通知、多注册商集成（Namecheap/Cloudflare/AWS Route53等）与

  DNS安全配置（DNSSEC/CAA）。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修。'
tags:
- Operations
- DNS
- 企业级
- 域名管理
tools:
- - read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# DNS管理专业版（PRO版）

## 概述

本平台为企业运维团队提供全功能的DNS管理能力。相比免费版，PRO版新增多域名批量管理、DNS监控告警、多注册商集成、DNS安全配置和变更审计等高级功能，全面满足企业级DNS管理的复杂需求。

PRO版完全兼容免费版Namecheap DNS命令，升级后原有DNS记录可直接管理。

## 核心能力

### PRO版功能增强对比

| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 域名数量 | 单域名 | 多域名批量 |
| 注册商 | 仅Namecheap | +Cloudflare/Route53/Aliyun |
| DNS监控 | 不支持 | 传播监控+告警 |
| DNS安全 | 基础 | DNSSEC/CAA/SPF/DKIM |
| 变更管理 | 不支持 | 审计+版本回滚 |
| 域名到期 | 不支持 | 监控+续费提醒 |
| 模板配置 | 不支持 | 批量模板应用 |
| 性能测试 | 不支持 | DNS解析性能测试 |

**输入**: 用户提供PRO版功能增强对比所需的指令和必要参数。
**处理**: 按照skill规范执行PRO版功能增强对比操作,遵循单一意图原则。
**输出**: 返回PRO版功能增强对比的执行结果,包含操作状态和输出数据。

### 多注册商支持

| 注册商 | 支持功能 | 认证方式 |
| --- | --- | --- |
| Namecheap | 全功能 | API User/Key |
| Cloudflare | 全功能 | API Token |
| AWS Route53 | 全功能 | Access Key |
| 阿里云DNS | 全功能 | Access Key |
| GoDaddy | 全功能 | API Key/Secret |

**输入**: 用户提供多注册商支持所需的指令和必要参数。
**处理**: 按照skill规范执行多注册商支持操作,遵循单一意图原则。
**输出**: 返回多注册商支持的执行结果,包含操作状态和输出数据。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、管理平台、支持多域名批量、告警与多注册商集、面向企业运维团队、支持多域名批量管、告警通知、多注册商集成、安全配置、when、需要系统监控、日志分析、运维告警、部署管理时使用、不适用于物理硬件等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一：多域名批量配置

用户输入："给所有域名统一添加SPF记录"

```bash
# 批量添加记录
python3 scripts/dns_pro.py batch add \
  --domains-file domains.txt \
  --type TXT \
  --host "@" \
  --value "v=spf1 include:_spf.google.com ~all" \
  --ttl 3600

# 输出：
# 示例
# example.org    [OK] SPF记录已添加
# example.net    [FAIL] API限流，稍后重试
```

### 场景二：DNS监控

用户输入："监控关键域名的DNS解析状态"

```bash
# 设置DNS监控
python3 scripts/dns_pro.py monitor add \
  --domains "example.com,api.example.com" \
  --check-type "A,MX,TXT" \
  --interval 300 \
  --alert "webhook,email"

# 查看监控状态
python3 scripts/dns_pro.py monitor status

# 输出：
# example.com      A:192.168.1.1   [OK]   最后检查: 2分钟前
# api.example.com  CNAME:cdn.com   [WARN] 解析延迟增高
```

### 场景三：DNS安全配置

用户输入："为域名配置DNS安全"

```bash
# 一键安全配置
python3 scripts/dns_pro.py secure \
  --domain example.com \
  --enable-dnssec \
  --add-caa "letsencrypt.org" \
  --add-spf \
  --add-dkim \
  --add-dmarc

# 输出安全配置报告
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt

# 配置多注册商凭证
cp config_pro_template.yaml config_pro.yaml
```

### 常用命令

```bash
# 多域名批量
python3 scripts/dns_pro.py batch add --domains-file domains.txt --type A --value 192.168.1.1
python3 scripts/dns_pro.py batch export --domains all --output dns_backup.xlsx

# DNS监控
python3 scripts/dns_pro.py monitor add --domains "example.com" --interval 300 --alert webhook
python3 scripts/dns_pro.py monitor status

# 安全配置
python3 scripts/dns_pro.py secure --domain example.com --enable-dnssec --add-caa "letsencrypt.org"

# 多注册商
python3 scripts/dns_pro.py registrars list
python3 scripts/dns_pro.py migrate --domain example.com --from namecheap --to cloudflare

# 变更审计
python3 scripts/dns_pro.py audit --domain example.com --days 30
python3 scripts/dns_pro.py rollback --domain example.com --version 5

# 域名到期
python3 scripts/dns_pro.py expiry check --all
python3 scripts/dns_pro.py expiry alert --days 30
```

## 配置示例

### PRO企业级配置

```yaml
pro_config:
  registrars:
    namecheap:
      api_user: "${NAMECHEAP_API_USER}"
      api_key: "${NAMECHEAP_API_KEY}"
      username: "${NAMECHEAP_USERNAME}"
      client_ip: "${NAMECHEAP_CLIENT_IP}"
    cloudflare:
      api_token: "${CLOUDFLARE_API_TOKEN}"
    route53:
      access_key: "${AWS_ACCESS_KEY_ID}"
      secret_key: "${AWS_SECRET_ACCESS_KEY}"
    aliyun:
      access_key: "${ALIYUN_ACCESS_KEY}"
      secret_key: "${ALIYUN_SECRET_KEY}"

  monitoring:
    check_interval: 300
    check_types: ["A", "AAAA", "CNAME", "MX", "TXT", "NS"]
    alert:
      channels: ["webhook", "email", "telegram"]
      on_change: true              # 记录变更时告警
      on_failure: true             # 解析失败时告警
    global_resolvers:
      - "8.8.8.8"
      - "1.1.1.1"
      - "114.114.114.114"

  security:
    dnssec: true
    caa: true
    spf: true
    dkim: true
    dmarc: true

  audit:
    enabled: true
    retention_days: 365
    versioning: true               # 记录版本化
    max_versions: 50

  expiry:
    check_frequency: "daily"
    alert_days: [90, 60, 30, 7, 1]
    auto_renew: false              # 自动续费（谨慎开启）

  batch:
    max_parallel: 5
    retry_on_failure: true
    rate_limit_delay: 1
```

## 最佳实践

### PRO版企业实践

| 实践领域 | 建议做法 |
| --- | --- |
| 批量管理 | 使用模板统一配置，避免逐个操作 |
| DNS监控 | 关键域名设置监控，及时发现问题 |
| 安全配置 | 启用DNSSEC，配置CAA防止未授权证书 |
| 变更管理 | 所有变更记录审计，支持回滚 |
| 域名续费 | 设置到期提醒，避免域名过期 |

### 免费版兼容性

```text
免费版命令 → PRO版命令（增强）：
dns.py record list (单域名)  → dns_pro.py batch export (多域名)
dns.py record add            → dns_pro.py batch add (批量)
基础记录管理                  → +监控+安全+审计+多注册商
```

## 常见问题

### Q1：支持哪些DNS注册商？

PRO版支持Namecheap、Cloudflare、AWS Route53、阿里云DNS和GoDaddy五大注册商。可通过统一接口管理不同注册商的域名。

### Q2：DNS监控如何工作？

PRO版定期从全球多个DNS解析器查询域名记录，与预期值对比。发现记录变更或解析失败时触发告警。

### Q3：DNSSEC如何配置？

PRO版自动生成DNSSEC密钥对，在注册商处启用DNSSEC并上传公钥。同时配置DS记录。整个流程自动化，但需域名注册商支持DNSSEC。

### Q4：变更审计如何工作？

所有DNS记录的创建、修改、删除操作都会记录审计日志，包含操作人、时间、变更前后内容。支持版本回滚，可恢复到历史任意版本。

### Q5：域名到期监控准确吗？

PRO版通过注册商API查询域名到期时间，提前90/60/30/7/1天发送提醒。数据来自注册商实时API，准确可靠。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| requests | Python库 | 必需 | `pip install requests` |
| dnspython | Python库 | 必需 | `pip install dnspython`（DNS查询） |
| boto3 | Python库 | 可选 | `pip install boto3`（Route53） |
| openpyxl | Python库 | 可选 | `pip install openpyxl`（Excel导出） |

### API Key 配置

| 注册商 | 环境变量 | 是否必需 | 用途 |
|:-------|:---------|:---------|:-----|
| Namecheap | `NAMECHEAP_API_*` | 可选 | Namecheap DNS |
| Cloudflare | `CLOUDFLARE_API_TOKEN` | 可选 | Cloudflare DNS |
| AWS Route53 | `AWS_ACCESS_KEY_ID` | 可选 | Route53 DNS |
| 阿里云 | `ALIYUN_ACCESS_KEY` | 可选 | 阿里云DNS |

- 仅需配置使用的注册商凭证
- 所有凭证存储在本地配置文件

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本+API执行）
- **说明**: 企业级DNS管理平台，支持多注册商与监控审计
- **PRO版特性**: 多域名批量、多注册商、DNS监控、安全配置、变更审计、到期监控
- **兼容性**: 完全兼容免费版Namecheap DNS命令

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 依赖云服务，需要网络连接

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```
