---
slug: "dns-config"
name: "dns-config"
version: "1.0.0"
displayName: "DNS配置工具专业版"
summary: "企业级 DNS 配置工具,支持 CAA、Cloudflare 代理、通配符与批量迁移策略。"
license: "Proprietary"
edition: "pro"
description: |-
  面向企业运维与基础设施团队的 DNS 全功能配置与迁移工具。核心能力:
  - CAA 记录配置(限制证书授权 CA,防未授权签发)
  - Cloudflare 代理行为管理与 CNAME 扁平化
  - 通配符记录与通配符 SSL 证书(DNS challenge)
  - 企业级批量迁移策略与回滚方案
  - 高级调试(全链路追踪、权威对比、记录完整性校验)

  适用场景:
  - 企业多域名 DNS 架构治理
  - 安全合规要求下的 CAA 与证书管控
  - Cloudflare 架构下的代理与源站保护

  差异化: Pro 版在免...
tags:
  - DNS
  - 企业运维
  - Communication
  - 安全配置
  - 批量迁移
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# DNS配置工具专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 能力模块 | 支持 | 支持 |
| 免费版 | 不支持 | 支持 |
| :----- | 不支持 | 支持 |
| :------: | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 说明 | 免费版 | Pro 版 |
|:-------|:-----|:------:|:------:|
| TTL 管理 | 迁移前调整 | 支持 | 支持+批量 |
| 邮件认证 | SPF/DKIM/DMARC | 支持 | 支持+验证 |
| www 处理 | apex 与 www | 支持 | 支持+批量 |
| 基础调试 | dig 命令 | 支持 | 支持 |
| CAA 记录 | 证书授权限制 | 不支持 | 支持 |
| Cloudflare 代理 | 代理行为管理 | 不支持 | 支持 |
| 通配符记录 | 通配符与 SSL | 不支持 | 支持 |
| 批量迁移 | 多域名迁移 | 不支持 | 支持+回滚 |
| 高级调试 | 全链路追踪 | 基础 | 完整 |
| 记录完整性 | 全类型校验 | 部分 | 支持 |
### 能力模块

执行能力模块操作,处理用户输入并返回结果。

**输入**: 用户提供能力模块所需的参数和指令。

**输出**: 返回能力模块的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`能力模块`相关配置参数进行设置
### TTL 管理

执行TTL 管理操作,处理用户输入并返回结果。

**输入**: 用户提供TTL 管理所需的参数和指令。

**输出**: 返回TTL 管理的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`TTL 管理`相关配置参数进行设置
### 邮件认证

执行邮件认证操作,处理用户输入并返回结果。

**输入**: 用户提供邮件认证所需的参数和指令。

**输出**: 返回邮件认证的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`邮件认证`相关配置参数进行设置
#
## 适用场景

### 场景一:配置 CAA 记录防止未授权证书签发

企业安全合规要求限制仅指定 CA 可为域名签发 SSL 证书,防止未授权 CA 被滥用签发。

```bash
# 1. 基础 CAA:仅允许 Let's Encrypt 签发
example.com. CAA 0 issue "letsencrypt.org"

# 2. 通配符需单独条目
example.com. CAA 0 issuewild "letsencrypt.org"

# 3. 事件报告(发现异常签发时通知)
example.com. CAA 0 iodef "mailto:security@example.com"

# 4. 验证 CAA 配置
dig example.com CAA +short
```

未配置 CAA 时,任何 CA 都可为域名签发证书,存在安全风险。配置后仅指定 CA 可签发。

### 场景二:Cloudflare 代理行为管理

企业使用 Cloudflare 代理保护源站,需正确理解橙云/灰云行为并避免常见陷阱。

```bash
# 橙云(Proxied):隐藏源站 IP,但影响非 HTTP 服务
# - 适用于 Web 流量(HTTP/HTTPS)
# - 会中断 SSH、邮件、游戏服务器等非 HTTP 服务
# - Cloudflare 控制缓存,TTL 设置被忽略

# 灰云(DNS-only):仅 DNS 解析,不代理
# - 适用于 SSH、邮件、游戏服务器等非 HTTP 服务
# - 源站 IP 暴露,需自行防护
# - TTL 设置生效

# CNAME 扁平化(apex 使用 CNAME)
# - Cloudflare 支持 apex 的 CNAME 扁平化
# - 但迁移离开 Cloudflare 时会造成混乱
# - 建议记录架构决策,便于后续迁移

# Universal SSL 仅代理记录生效
# - 橙云记录自动获得 Universal SSL
# - 灰云(DNS-only)记录需源站证书
```

### 场景三:通配符记录与通配符 SSL 证书

企业有大量子域名,需用通配符记录简化管理,并用 DNS challenge 签发通配符证书。

```bash
# 1. 通配符记录
*.example.com. A 1.2.3.4

# 注意:通配符不匹配 apex
# 示例
# 但不匹配 example.com 本身,需单独配置:
example.com. A 1.2.3.4

# 2. 显式子域名优先于通配符
# 若同时存在 *.example.com 和 api.example.com 的记录
# api.example.com 的显式记录优先生效

# 3. 通配符 SSL 证书(DNS challenge 签发)
# 使用 Let's Encrypt + DNS challenge 获取 *.example.com 证书
certbot certonly --manual --preferred-challenges dns \
  -d "*.example.com" -d "example.com"
```

### 场景四:企业级批量迁移

企业需将 50 个域名从旧 DNS 服务商批量迁移到新服务商,要求零停机和可回滚。

```bash
# 1. 迁移前 7 天:批量降低所有域名 TTL 至 300 秒
for domain in $(cat domains.txt); do
  echo "降低 $domain 的 TTL..."
  # 在旧服务商后台批量修改 TTL
done

# 2. 导出所有域名当前记录
for domain in $(cat domains.txt); do
  dig +nocmd +noall +answer $domain ANY > "records-$domain.txt"
  dig +nocmd +noall +answer _dmarc.$domain TXT >> "records-$domain.txt"
done

# 3. 在新服务商预配置所有记录(不切换 NS)

# 4. 迁移当日:切换 NS 记录
for domain in $(cat domains.txt); do
  # 在域名注册商处更新 NS 为新服务商
  echo "切换 $domain 的 NS 记录..."
done

# 5. 多解析器验证
for domain in $(cat domains.txt); do
  echo "验证 $domain:"
  dig @8.8.8.8 $domain +short
  dig @1.1.1.1 $domain +short
done

# 6. 回滚预案:若新服务商异常,将 NS 切回旧服务商
# (TTL 已降至 300 秒,回滚后 5 分钟内生效)
```

## 使用流程

### 优秀步:评估当前架构

```bash
# 检查现有 CAA 配置
dig example.com CAA +short

# 检查 Cloudflare 代理状态(若使用)
dig example.com +short  # 返回 Cloudflare IP 说明已代理

# 导出完整记录清单
dig +nocmd +noall +answer example.com ANY
```

### 第二步:按需求配置

根据你的安全合规需求和企业架构,参考上方使用场景中的配置示例。

### 第三步:完整验证

```bash
# 验证 CAA
dig example.com CAA +short

# 验证通配符
dig anything.example.com +short

# 验证所有记录类型
for type in A AAAA MX TXT CAA NS SOA; do
  echo "=== $type ==="
  dig example.com $type +short
done
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 全部维度 |
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent 平台**: 支持解析 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **命令行工具**: `dig`(DNS 查询)、`certbot`/`acme.sh`(证书签发,可选)
- **DNS 服务商后台**: 支持高级功能(CAA/通配符)的 DNS 服务商
- **Cloudflare 账号**: 若使用 Cloudflare 代理与 DNS API(可选)

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM 能力 | API | 必需 | 由 Agent 内置大模型提供 |
| dig 命令 | 工具 | 推荐 | 系统自带或安装 bind-utils/dnsutils |
| DNS 服务商后台 | 平台 | 必需 | 支持 CAA 的 DNS 服务商 |
| Cloudflare | 平台 | 可选 | Cloudflare 账号(代理架构时) |
| certbot / acme.sh | 工具 | 可选 | 通配符证书签发 |
| mail-tester.com | 验证服务 | 推荐 | 免费在线服务 |

### API Key 配置

- **本 Skill 核心无需 API Key**: 基于 Markdown 指令和命令行工具,不调用外部 API。
- **Cloudflare API Token**: 若使用 Cloudflare DNS API 自动化签发通配符证书,需在 Cloudflare 后台创建 API Token(权限:Zone DNS 编辑),通过环境变量注入。
- **DNS 服务商凭证**: 修改 DNS 记录需登录服务商后台,凭证由用户自行管理。
- **ACME 账户**: certbot/acme.sh 首次使用会自动创建 Let's Encrypt ACME 账户,无需手动配置 Key。

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令 + 部分功能需 `exec` 执行 dig/certbot 等命令)
- **说明**: 以自然语言指令驱动 Agent 指导 DNS 高级配置、证书签发与批量迁移
- **适用规模**: 企业级、多域名架构、安全合规场景
- **兼容性**: 与 `dns-config-tool-free` 配置原则完全兼容,可平滑升级
- **支持级别**: 优先支持(Pro 版享有问题优先响应与功能迭代建议通道)

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

检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过

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

检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过

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

检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过

改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1: CAA 记录配置后证书签发失败?

检查 CAA 是否过于严格。若 CAA 仅允许 `letsencrypt.org`,但实际使用 ZeroSSL 签发,会被拒绝。确认 CAA 中 `issue` 字段包含所有实际使用的 CA。通配符证书需额外配置 `issuewild`。紧急情况下可用 `issue ";"` 完全禁止签发。

### Q2: Cloudflare 橙云后 SSH/邮件连不上?

橙云(代理)仅支持 HTTP/HTTPS 流量,会中断 SSH、邮件(SMTP/IMAP)、游戏服务器等非 HTTP 服务。这些服务必须用灰云(DNS-only)。检查记录的代理状态,将非 HTTP 服务记录切换为灰云。

### Q3: 通配符证书续期失败?

通配符证书必须用 DNS challenge 续期。若使用 HTTP challenge 会失败。建议配置 DNS API 自动化(如 acme.sh + Cloudflare DNS API),实现自动续期。确认 DNS API Token 权限包含 Zone DNS 编辑权限。

### Q4: apex 用 CNAME 扁平化后迁移出 Cloudflare 报错?

其他 DNS 服务商通常不支持 apex 的 CNAME(RFC 限制)。Cloudflare 的 CNAME 扁平化是其特有功能。迁移离开 Cloudflare 时需将 apex 的 CNAME 改回 A 记录。建议迁移前在架构文档记录此决策,迁移时优先处理 apex 记录。

### Q5: 批量迁移如何保证零停机?

关键:迁移前 7 天将所有域名 TTL 降至 300 秒并等待生效;在新服务商完整预配置所有记录(包括 TXT/CAA/MX 等所有类型)并验证一致;迁移日仅切换 NS 记录(不改记录值);切换后多解析器验证;保留旧服务商 7 天回滚窗口。TTL 300 秒确保回滚 5 分钟生效。

### Q6: Universal SSL 没生效?

Universal SSL 仅对橙云(代理)记录生效。若记录为灰云(DNS-only),不获得 Universal SSL,需在源站自行配置证书。检查记录代理状态,Web 流量记录应设为橙云。新启用代理后 Universal SSL 可能需要几分钟到几小时激活。

### Q7: 迁移后邮件认证失效?

迁移时容易遗漏 TXT 记录(SPF/DKIM/DMARC)。迁移后务必逐一验证:SPF(`dig TXT example.com`)、DKIM(`dig TXT default._domainkey.example.com`)、DMARC(`dig TXT _dmarc.example.com`)。DKIM 记录由邮件服务商提供,确保完整复制(含公钥)。

### Q8: Pro 版和免费版能同时用吗?

可以。两者配置原则兼容。Pro 版包含免费版全部能力,额外提供 CAA、Cloudflare、通配符与批量迁移。建议企业环境统一使用 Pro 版,免费版用于个人轻量场景。

### Q9: 如何监控 CAA 异常签发?

配置 CAA 的 `iodef` 字段(`CAA 0 iodef "mailto:security@example.com"`),当有 CA 尝试为域名签发证书但被 CAA 拒绝时,指定邮箱会收到通知。定期检查通知,发现异常签发尝试及时排查。

### Q10: 大规模迁移用什么工具辅助?

Pro 版提供迁移检查清单和脚本模板。批量操作可编写脚本循环处理(如 bash 遍历域名列表执行 dig 验证)。记录导出用 `dig +nocmd +noall +answer domain ANY` 批量保存。迁移进度跟踪建议用表格记录每个域名的阶段状态。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖云服务，需要网络连接
