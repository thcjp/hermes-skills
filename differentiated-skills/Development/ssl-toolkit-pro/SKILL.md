---
slug: ssl-toolkit-pro
name: ssl-toolkit-pro
version: "1.0.0"
displayName: SSL工具箱(专业版)
summary: 企业级TLS套件,含通配符/SAN、全服务器配置、安全审计、自动化监控与告警。
license: MIT
edition: pro
description: |-
  SSL工具箱(专业版)面向团队与企业,提供完整的TLS证书管理、全主流服务器配置、安全审计评分、自动化监控告警与多域名治理能力。

  核心能力:
  - 全证书类型:单域名/通配符/SAN/多域名/EV
  - 全主流服务器:Nginx/Apache/Node.js/Caddy/Traefik/HAProxy
  - 安全审计:TLS配置评分、漏洞扫描、Cipher套件优化
  - 自动化:全自动化申请/续期/部署/监控
  - 监控告警:证书过期预警、配置漂移检测
  - 多域名治理:证书资产清单与到期看板

  适用场景:
  - 企业多站点TLS统一管理
  - 通配符与SAN证书治理
  - 安全合规要求的TLS审计
  - 大规模证书过期监控

  差异化:
  - 完全兼容免费版证书申请与基础配置
  - 新增进阶证书、全服务器、审计、监控四大模块
  - 提供企业级TLS策略模板与治理流程
  - 中英双语审计报告

  触发关键词: ssl, https, tls, 证书, certificate, certbot, let's encrypt, 通配符, wildcard, san, 多域名, 审计, 监控, 告警, 企业, enterprise, mTLS
tags:
- Development
- 安全
- SSL
- 企业级
- 运维
- 监控
- TLS
tools:
- read
- exec
---

# SSL工具箱(专业版)

## 概述

SSL工具箱(专业版)面向团队与企业,在兼容免费版证书申请与基础配置的基础上,扩展了全证书类型(通配符/SAN/多域名/EV)、全主流服务器配置(Node.js/Caddy/Traefik/HAProxy)、安全审计评分、自动化监控告警与多域名治理能力。

当你在请求中提及 通配符证书、SAN、多域名管理、TLS审计、安全评分、证书监控、mTLS 等关键词时,本工具会自动激活,为企业提供结构化的TLS治理方案。

本版本完全兼容 `ssl-toolkit-free` 的证书申请命令与Nginx/Apache配置,可平滑升级,已有证书与配置无需改造。

## 核心能力

| 能力模块 | 说明 | 与免费版差异 |
| --- | --- | --- |
| 基础证书申请 | certbot/acme.sh/Caddy | 与免费版一致 |
| 证书类型 | 单域名 | 与免费版一致 |
| 进阶证书 | 通配符/SAN/多域名/EV | 免费版无 |
| 服务器配置 | Nginx/Apache | 与免费版一致 |
| 进阶服务器 | Node.js/Caddy/Traefik/HAProxy | 免费版无 |
| 错误诊断 | 5类常见错误 | 与免费版一致 |
| 安全审计 | TLS评分/Cipher优化/漏洞扫描 | 免费版无 |
| 自动化 | 全自动申请/续期/部署 | 免费版仅基础续期 |
| 监控告警 | 过期预警/配置漂移 | 免费版无 |
| 多域名治理 | 资产清单/到期看板 | 免费版无 |
| mTLS | 双向TLS配置 | 免费版无 |

## 使用场景

### 场景一:企业多站点通配符证书治理

企业有大量子域名,希望用通配符证书统一管理,降低证书数量。

```bash
# 申请通配符证书(需DNS-01验证)
certbot certonly --manual --preferred-challenges dns \
  -d "*.example.com" -d "example.com"

# 或使用acme.sh(支持更多DNS服务商)
acme.sh --issue --dns dns_cf \
  -d "*.example.com" -d "example.com"

# 查看企业所有证书资产
node scripts/cert-inventory.mjs --root /etc/letsencrypt/live/
```

证书资产清单输出:

```text
## 证书资产清单: example.com 集群

| 域名 | 类型 | 签发者 | 到期日 | 剩余天数 | 状态 |
| --- | --- | --- | --- | --- | --- |
| *.example.com | 通配符 | Let's Encrypt | 2026-09-17 | 61 | 正常 |
| api.example.com | 单域名 | Let's Encrypt | 2026-08-05 | 18 | 即将到期 |
| *.staging.example.com | 通配符 | Let's Encrypt | 2026-10-01 | 75 | 正常 |
| internal.example.com | 自签名 | - | 2027-01-01 | 167 | 内部使用 |
```

### 场景二:TLS安全审计与评分

企业需要通过安全合规审计,工具对TLS配置评分并给出优化建议。

```bash
# 扫描TLS配置并评分
node scripts/tls-audit.mjs --host example.com --port 443 --format html > audit-report.html

# 输出
# TLS安全审计报告: example.com
#
# 总分: B (75/100)
#
# | 检查项 | 结果 | 得分 | 建议 |
# | --- | --- | --- | --- |
# | TLS协议版本 | TLS 1.2/1.3 | 20/20 | - |
# | Cipher套件 | 部分弱算法 | 12/20 | 移除CBC套件 |
# | 证书链 | 完整 | 15/15 | - |
# | HSTS | 未启用 | 0/10 | 启用HSTS |
# | OCSP装订 | 未启用 | 8/10 | 启用OCSP |
# | 前向保密 | 支持 | 10/10 | - |
# | 证书强度 | RSA 2048 | 10/15 | 升级到ECDSA |
```

应用优化后的Nginx配置:

```nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    # 仅启用TLS 1.2与1.3
    ssl_protocols TLSv1.2 TLSv1.3;

    # 优化Cipher套件(前向保密优先)
    ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:!aNULL:!MD5:!CBC';
    ssl_prefer_server_ciphers off;

    # 启用HSTS
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

    # 启用OCSP装订
    ssl_stapling on;
    ssl_stapling_verify on;
    ssl_trusted_certificate /etc/letsencrypt/live/example.com/chain.pem;

    # 会话复用
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;
    ssl_session_tickets off;
}
```

### 场景三:证书过期监控与告警

企业有上百个证书,需要提前预警避免过期事故。

```bash
# 配置监控
node scripts/cert-monitor.mjs --config config/cert-watch.yaml

# 证书监控配置
```

```yaml
# config/cert-watch.yaml 证书监控配置
monitors:
  - host: example.com
    port: 443
    alertDays: 30      # 30天前预警
    criticalDays: 7    # 7天前严重

  - host: api.example.com
    port: 443
    alertDays: 30
    criticalDays: 7

  - file: /etc/letsencrypt/live/staging.example.com/cert.pem
    alertDays: 30
    criticalDays: 7

alerts:
  - level: warning
    threshold: 30
    targets:
      - slack: "#devops-alerts"
  - level: critical
    threshold: 7
    targets:
      - slack: "#devops-alerts"
      - pagerduty: "cert-expiry"

schedule:
  cron: "0 8 * * *"   # 每天8点检查
```

## 快速开始

### 1. 全主流服务器配置

#### Caddy(自动HTTPS)

```caddy
example.com {
    reverse_proxy localhost:3000
    # Caddy自动申请并续期Let's Encrypt证书
}
```

#### Traefik(自动HTTPS)

```yaml
# traefik.yml
entryPoints:
  web:
    address: ":80"
    http:
      redirections:
        entryPoint:
          to: websecure
          scheme: https
  websecure:
    address: ":443"

certificatesResolvers:
  letsencrypt:
    acme:
      email: admin@example.com
      storage: acme.json
      httpChallenge:
        entryPoint: web
```

#### HAProxy

```haproxy
frontend https
    bind *:443 ssl crt /etc/ssl/certs/example.com.pem alpn h2
    http-request redirect scheme https code 301 if { hdr(host) -i example.com }
    default_backend app

# 证书文件需合并:cat fullchain.pem privkey.pem > example.com.pem
```

#### Node.js

```javascript
import https from 'node:https';
import fs from 'node:fs';

const server = https.createServer({
  cert: fs.readFileSync('/etc/letsencrypt/live/example.com/fullchain.pem'),
  key: fs.readFileSync('/etc/letsencrypt/live/example.com/privkey.pem'),
  minVersion: 'TLSv1.2',
  ciphers: [
    'ECDHE-ECDSA-AES128-GCM-SHA256',
    'ECDHE-RSA-AES128-GCM-SHA256',
    '!aNULL', '!MD5', '!CBC',
  ].join(':'),
}, (req, res) => {
  res.writeHead(200);
  res.end('Hello over HTTPS');
});

server.listen(443);
```

### 2. mTLS双向TLS配置

```nginx
server {
    listen 443 ssl http2;
    server_name api.internal.example.com;

    ssl_certificate /etc/ssl/certs/server.pem;
    ssl_certificate_key /etc/ssl/private/server-key.pem;

    # 启用客户端证书验证
    ssl_client_certificate /etc/ssl/certs/ca.pem;
    ssl_verify_client on;
    ssl_verify_depth 2;

    location / {
        # 仅允许持有有效客户端证书的请求
        if ($ssl_client_verify != SUCCESS) {
            return 403;
        }
        proxy_pass http://backend;
    }
}
```

### 3. 自动化部署流水线

```yaml
# .github/workflows/cert-renew.yml 证书自动续期与部署
name: Certificate Renewal
on:
  schedule:
    - cron: '0 0 * * 1'  # 每周一执行
jobs:
  renew:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 安装certbot
        run: sudo apt-get install -y certbot
      - name: 续期证书
        env:
          CF_API_TOKEN: ${{ secrets.CF_API_TOKEN }}
        run: |
          certbot certonly --dns-cloudflare \
            --dns-cloudflare-credentials ~/.secrets/certbot.ini \
            -d "*.example.com" -d "example.com" \
            --non-interactive --agree-tos
      - name: 部署到服务器
        run: |
          scp -r /etc/letsencrypt/live/ deploy@prod:/tmp/new-certs/
          ssh deploy@prod 'sudo systemctl reload nginx'
      - name: 通知
        if: always()
        uses: slackapi/slack-github-action@v1
        with:
          slack-message: "证书续期${{ job.status == 'success' && '成功' || '失败' }}"
```

## 配置示例

### 企业TLS策略基线

| 检查项 | 基线要求 | 说明 |
| --- | --- | --- |
| TLS协议 | 仅TLS 1.2/1.3 | 禁用1.0/1.1 |
| Cipher套件 | 仅GCM/ChaCha20 | 禁用CBC/RC4/3DES |
| 密钥长度 | RSA≥2048或ECDSA | 推荐ECDSA |
| HSTS | max-age≥63072000 | 含includeSubDomains |
| OCSP装订 | 启用 | 提升握手速度 |
| 前向保密 | 强制 | ECDHE套件 |
| 证书链 | 完整 | fullchain.pem |

### 证书类型决策矩阵

| 场景 | 推荐类型 | 验证方式 | 说明 |
| --- | --- | --- | --- |
| 单站点 | 单域名 | HTTP-01 | 最简单 |
| 多子域名 | 通配符 | DNS-01 | 一证覆盖所有子域 |
| 多个不同域名 | SAN | HTTP-01/DNS-01 | 一证多域 |
| 内部服务 | 自签名/私有CA | - | 仅内部信任 |
| 金融/政府 | EV | 增强 | 浏览器显示组织名 |

## 最佳实践

### 1. 证书资产清单治理

```bash
# 定期生成资产清单
node scripts/cert-inventory.mjs --root /etc/letsencrypt/live/ --format html > reports/certs-$(date +%Y%m%d).html

# 30天内到期证书
node scripts/cert-inventory.mjs --expiring-within 30
```

### 2. 监控告警分级

| 级别 | 剩余天数 | 动作 |
| --- | --- | --- |
| 提示 | 30天 | 记录清单 |
| 警告 | 14天 | 通知运维 |
| 严重 | 7天 | 立即续期 |
| 紧急 | 1天 | 电话升级 |

### 3. 安全审计周期

| 审计项 | 频率 | 工具 |
| --- | --- | --- |
| 证书到期 | 每天 | cert-monitor |
| TLS配置评分 | 每月 | tls-audit |
| 漏洞扫描 | 每月 | testssl.sh |
| 配置漂移 | 每周 | config-diff |

### 4. 配置漂移检测

```bash
# 检测Nginx配置是否与基线一致
node scripts/config-diff.mjs \
  --baseline config/nginx-ssl-baseline.conf \
  --actual /etc/nginx/conf.d/ssl.conf

# 输出差异并告警
```

### 5. 多域名到期看板

```bash
# 生成到期看板HTML
node scripts/cert-dashboard.mjs \
  --hosts example.com,api.example.com,staging.example.com \
  --format html > dashboard.html

# 输出CSV供运维系统消费
node scripts/cert-dashboard.mjs --hosts ... --format csv > dashboard.csv
```

### 6. 灾备与回滚

```bash
# 续期前备份当前证书
cp -r /etc/letsencrypt/live/ /backup/certs-$(date +%Y%m%d)/

# 续期失败时回滚
cp -r /backup/certs-20260718/* /etc/letsencrypt/live/
sudo systemctl reload nginx
```

## 常见问题

### Q1:PRO版与免费版如何共存?

两者证书申请命令与Nginx/Apache配置完全兼容,PRO版包含免费版全部能力。团队升级时直接替换Skill文件,已有证书与配置无需改造。

### Q2:通配符证书如何申请?

通配符证书需要DNS-01验证,要求你的DNS服务商支持API。certbot需安装对应DNS插件(如 `certbot-dns-cloudflare`),acme.sh原生支持多种DNS服务商。

### Q3:TLS审计评分标准是什么?

参考Mozilla TLS配置与现代最佳实践,从协议版本、Cipher套件、证书链、HSTS、OCSP、前向保密、证书强度等维度评分,A+为最高。建议目标A及以上。

### Q4:证书监控如何部署?

建议独立部署监控服务,通过cron定期检查所有证书的远程状态与本地文件,提前预警。生产环境建议接入PagerDuty等值班系统,确保严重告警有人响应。

### Q5:mTLS与单向TLS有何区别?

- 单向TLS:仅服务器出示证书,客户端验证服务器身份(常见HTTPS)
- mTLS:服务器与客户端互相出示证书,双向验证(适合内部服务间通信、零信任架构)

mTLS需要为每个客户端签发证书,通常配合私有CA管理。

### Q6:支持多租户隔离吗?

支持。通过不同证书目录与配置文件实现租户隔离,各租户的证书、监控、审计日志独立。租户间配置互不影响。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Web服务器**: Nginx / Apache / Caddy / Traefik / HAProxy / Node.js 任一
- **DNS服务商**: 通配符证书需要支持API的DNS服务商

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| openssl | 命令行工具 | 必需 | 系统自带 |
| certbot | 命令行工具 | 推荐 | `pip install certbot` |
| acme.sh | 命令行工具 | 可选 | acme.sh 安装脚本 |
| testssl.sh | 安全扫描 | 推荐 | testssl.sh 下载 |
| Node.js | 运行时 | 推荐 | nodejs.org 下载(审计脚本) |
| DNS插件 | certbot插件 | 通配符必需 | `pip install certbot-dns-cloudflare` 等 |
| 通知渠道 | webhook | 可选 | Slack/PagerDuty/飞书等 |

### API Key 配置

- 本Skill基于Markdown指令,无需额外API Key。
- Let's Encrypt 通过ACME协议自动签发,无需API Key。
- 通配符证书的DNS-01验证需要DNS服务商的API令牌(如Cloudflare API Token),配置为环境变量,不入库。
- 监控告警的webhook URL需配置为环境变量或密钥管理器。

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务。PRO版面向团队与企业,提供全证书类型、全主流服务器配置、安全审计、自动化监控与多域名治理能力,完全兼容免费版证书申请与基础配置。
