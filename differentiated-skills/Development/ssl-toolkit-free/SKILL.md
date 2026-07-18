---
slug: ssl-toolkit-free
name: ssl-toolkit-free
version: "1.0.0"
displayName: SSL工具箱(免费版)
summary: 个人用户的HTTPS配置、TLS证书管理与基础连接排障工具。
license: MIT
edition: free
description: |-
  SSL工具箱(免费版)为个人用户提供HTTPS配置、TLS证书管理与基础连接排障能力。

  核心能力:
  - Let's Encrypt免费证书申请与续期
  - 证书状态检查与详情查看
  - 常见错误诊断与修复
  - Nginx/Apache基础HTTPS配置
  - 证书类型选择指引

  适用场景:
  - 个人站点启用HTTPS
  - 证书过期排查与续期
  - 常见SSL错误诊断

  差异化:
  - 免费版聚焦个人站点的基础SSL管理
  - 移除原始平台与作者引用,纯净适配SkillHub
  - 提供中文友好的错误诊断表

  触发关键词: ssl, https, tls, 证书, certificate, certbot, let's encrypt, 加密, 安全连接, nginx, apache
tags:
- Development
- 安全
- SSL
- 运维
tools:
- read
- exec
---

# SSL工具箱(免费版)

## 概述

SSL工具箱(免费版)为个人用户提供HTTPS配置、TLS证书管理与基础连接排障能力。当你在请求中提及 SSL证书、HTTPS配置、Let's Encrypt、certbot、TLS配置、证书过期、混合内容、证书链错误 等关键词时,本工具会自动激活,根据任务推荐合适的工具与方法,并输出可执行的命令与配置。

本版本聚焦个人站点的基础SSL管理,适合个人博客、小型站点与本地开发环境。如需通配符证书、多域名SAN、高级排障、自动化审计与多服务器配置,请升级至 PRO 版本。

## 核心能力

| 能力 | 说明 |
| --- | --- |
| 免费证书申请 | certbot / acme.sh / Caddy自动获取 |
| 证书状态检查 | openssl查看远程证书状态 |
| 证书详情查看 | 解析证书字段(有效期、域名、签发者) |
| 常见错误诊断 | 5类常见错误的根因与修复 |
| 基础服务器配置 | Nginx / Apache HTTPS配置模板 |
| 证书续期 | 自动化续期与dry-run验证 |
| 证书类型选择 | 单域名/通配符/SAN/自签名指引 |

## 使用场景

### 场景一:为个人站点启用HTTPS

用户希望为个人博客启用HTTPS,工具推荐Let's Encrypt免费证书。

```bash
# 使用certbot为Nginx申请证书
certbot certonly --nginx -d example.com -d www.example.com

# 验证证书已签发
ls /etc/letsencrypt/live/example.com/
# fullchain.pem  privkey.pem  chain.pem  cert.pem
```

配置Nginx使用证书:

```nginx
server {
    listen 443 ssl http2;
    server_name example.com www.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    # 基础安全配置
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
}
```

### 场景二:检查证书状态与有效期

用户希望检查某域名证书是否快过期。

```bash
# 查看远程证书有效期
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates

# 输出示例
# notBefore=Jun 19 00:00:00 2026 GMT
# notAfter=Sep 17 00:00:00 2026 GMT

# 查看证书完整详情
openssl s_client -connect example.com:443 -servername example.com
```

### 场景三:诊断证书错误

用户报告浏览器显示证书错误,工具诊断根因并给出修复。

| 错误 | 根因 | 修复 |
| --- | --- | --- |
| `certificate has expired` | 证书已过期 | 用 `certbot renew` 续期 |
| `unable to verify` / `self signed` | 缺少中间证书 | 配置中包含完整证书链 |
| `hostname mismatch` | 证书不覆盖该域名 | 为正确域名申请证书或加SAN |
| `mixed content` | HTTPS页面引用HTTP资源 | 把所有URL改为HTTPS或用 `//` |
| `ERR_CERT_AUTHORITY_INVALID` | 自签名或不受信任的CA | 使用Let's Encrypt或安装CA证书 |

## 快速开始

### 1. 申请免费证书

```bash
# 方式一:certbot(最常用)
certbot certonly --nginx -d example.com -d www.example.com

# 方式二:certbot standalone(无Web服务器时)
certbot certonly --standalone -d example.com

# 方式三:acme.sh(轻量)
acme.sh --issue -d example.com --nginx
```

### 2. 检查证书状态

```bash
# 查看远程证书有效期
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates

# 查看证书详情
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -text

# 查看本地证书文件
openssl x509 -in cert.pem -text -noout
```

### 3. 配置服务器

Nginx配置:

```nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
}

# HTTP跳转HTTPS
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}
```

Apache配置:

```apache
SSLEngine on
SSLCertificateFile /path/to/cert.pem
SSLCertificateKeyFile /path/to/privkey.pem
SSLCertificateChainFile /path/to/chain.pem
```

## 配置示例

### 核心任务速查表

| 任务 | 工具/方法 |
| --- | --- |
| 获取免费证书 | `certbot`, acme.sh, Caddy(自动) |
| 检查证书状态 | `openssl s_client -connect host:443` |
| 查看证书详情 | `openssl x509 -in cert.pem -text -noout` |
| 测试配置 | ssllabs.com/ssltest 或 `testssl.sh` |
| 转换格式 | PEM / DER / PKCS12 互转 |

### 常用证书命令

```bash
# 申请证书
certbot certonly --nginx -d example.com -d www.example.com

# 查看远程证书有效期
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates

# 查看远程证书完整信息
openssl s_client -connect example.com:443 -servername example.com
```

### 证书类型选择

| 类型 | 适用场景 |
| --- | --- |
| 单域名 | 一个站点(example.com) |
| 通配符(*.domain.com) | 所有子域名 |
| 多域名(SAN) | 多个不同域名共用一个证书 |
| 自签名 | 仅本地开发 — 浏览器会警告 |

## 最佳实践

### 1. 始终自动化续期

Let's Encrypt证书90天过期,务必自动化:

```bash
# 测试续期(不实际执行)
certbot renew --dry-run

# 添加cron定时续期
crontab -e
# 每天凌晨检查并续期
0 0 * * * certbot renew --quiet
```

### 2. 配置HTTP跳转HTTPS

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    return 301 https://$host$request_uri;
}
```

### 3. 使用完整证书链

```nginx
# 正确:使用fullchain.pem(包含中间证书)
ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;

# 错误:仅用cert.pem(缺少中间证书,部分客户端无法验证)
ssl_certificate /etc/letsencrypt/live/example.com/cert.pem;
```

### 4. 启用现代TLS协议

```nginx
# 推荐:仅启用TLS 1.2与1.3
ssl_protocols TLSv1.2 TLSv1.3;

# 禁用:TLS 1.0与1.1(已不安全)
# ssl_protocols TLSv1 TLSv1.1;  # ❌
```

### 5. 解决混合内容

HTTPS页面引用HTTP资源会触发混合内容警告:

```html
<!-- 错误:HTTP资源 -->
<img src="http://cdn.example.com/image.png">

<!-- 正确:HTTPS或协议相对 -->
<img src="https://cdn.example.com/image.png">
<img src="//cdn.example.com/image.png">
```

## 常见问题

### Q1:免费版支持哪些服务器?

免费版提供Nginx与Apache基础配置模板。如需Node.js、Caddy、Traefik、HAProxy等,请使用PRO版。

### Q2:Let's Encrypt证书有效期多久?

90天。务必配置自动续期,建议每天检查一次。`certbot renew` 只在证书剩余有效期<30天时实际续期,所以频繁检查是安全的。

### Q3:免费版能否申请通配符证书?

免费版提供通配符证书的说明,但通配符证书需要DNS-01验证,配置较复杂。深度通配符与多域名管理请使用PRO版。

### Q4:免费版与PRO版差异?

| 维度 | 免费版 | PRO版 |
| --- | --- | --- |
| 证书类型 | 单域名为主 | 全类型(含通配符/SAN) |
| 服务器配置 | Nginx/Apache | 全主流(Node/Caddy/Traefik/HAProxy) |
| 排障深度 | 5类常见错误 | 全错误+性能+安全审计 |
| 自动化 | 基础续期 | 全自动+监控+告警 |
| 安全审计 | 不支持 | TLS配置评分+漏洞扫描 |
| 支持 | 社区支持 | 优先支持 |

### Q5:自签名证书能用吗?

仅适合本地开发,浏览器会警告。生产环境务必使用受信任CA签发的证书(如Let's Encrypt)。

### Q6:本工具能做什么、不能做什么?

能做:HTTPS配置、证书申请与续期、常见错误诊断、基础服务器配置。
不能做:应用层鉴权(JWT/OAuth)、SSH密钥、VPN/隧道、防火墙配置 — 这些请用对应专用工具。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Web服务器**: Nginx / Apache(配置HTTPS需要)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| openssl | 命令行工具 | 必需 | 系统自带 |
| certbot | 命令行工具 | 推荐 | `pip install certbot` 或 eff.org 下载 |
| acme.sh | 命令行工具 | 可选 | acme.sh 安装脚本 |
| Nginx/Apache | Web服务器 | 视场景 | 系统包管理器安装 |

### API Key 配置

- 本Skill基于Markdown指令,无需额外API Key。
- Let's Encrypt 通过ACME协议自动签发证书,无需API Key。
- 域名DNS解析需提前配置好,指向你的服务器IP。

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务。免费版聚焦个人站点的HTTPS配置、证书管理与基础连接排障。
