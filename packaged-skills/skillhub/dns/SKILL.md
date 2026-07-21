---
slug: dns
name: dns
version: "1.0.0"
displayName: DNS配置专家
summary: DNS记录配置、TTL迁移、邮件认证三件套、CAA证书锁定与Cloudflare代理排障
license: MIT
description: |-
  DNS领域专业配置与排障Skill,覆盖记录生命周期、邮件认证链、证书授权限制与CDN代理行为。

  核心能力:
  - 迁移前的TTL预降策略与多resolver缓存探测
  - SPF/DKIM/DMARC三位一体邮件认证配置
  - CAA记录锁定证书签发机构,配合iodef实现安全事件上报
  - Cloudflare橙云/灰云代理行为与CNAME扁平化分析
  - dig +trace链路诊断与权威/缓存响应比对
  - www规范化、通配符记录、子域优先级规则

  适用场景:
  - 域名迁移前的TTL预热与缓存验证
  - 邮件投递率治理(SPF/DKIM/DMARC全链路)
  - 证书安全加固(CAA锁定+iodef告警)
  - Cloudflare代理导致的非HTTP服务故障排查
tags:
  - Communication
  - Networking
  - DevOps
tools:
  - read
  - exec
---

# DNS配置专家

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD（纯Markdown指令，无需exec命令行能力）

## 核心能力

本Skill围绕DNS记录的正确配置、迁移策略与故障排查构建,重点解决以下领域问题:

- **TTL迁移策略**: 迁移前48小时将TTL降至300秒,确保旧缓存过期后再切换;迁移稳定24小时后恢复至3600-86400秒
- **邮件认证三件套**: SPF(单TXT记录)、DKIM(签名)、DMARC(策略聚合)必须同时配置,缺一不可;SPF单独配置不足以保证投递率
- **CAA证书锁定**: 限制可签发证书的CA,配合iodef实现安全事件上报;未配置CAA时任何CA均可签发证书
- **www规范化**: apex与www必须同时配置或互转,HTTPS重定向需双域名证书;未配置www会导致链接失效
- **Cloudflare代理行为**: 橙云隐藏源站IP但破坏非HTTP服务(SSH/邮件/游戏);代理模式忽略用户TTL设置;Universal SSL仅对代理记录生效
- **通配符规则**: *.example.com不匹配apex,显式子域优先于通配符;多级子域(a.b.example.com)也不被通配符匹配
- **dig链路诊断**: +trace展示完整解析链,@ns直接查询权威服务器绕过缓存;对比权威与缓存响应可判断传播进度
- **通配符SSL证书**: HTTP-01验证不支持通配符,需使用DNS-01挑战方式签发

## 适用场景

### 场景一： 域名迁移前的TTL预热
- **输入**: 待迁移域名 example.com,当前TTL=86400s,计划48小时后切换DNS商
- **处理**: 先用 `dig +nocmd +noall +answer example.com` 探测当前缓存TTL;将TTL降至300s;等待原TTL完全过期;切换后用Google(8.8.8.8)、Cloudflare(1.1.1.1)、本地ISP多resolver验证
- **输出**: TTL降级确认 + 多resolver缓存状态报告 + 切换时机建议

### 场景二： 邮件投递率治理
- **输入**: 业务邮件频繁进入收件人垃圾箱,域名 example.com,使用Google Workspace与Mailgun双通道发送
- **处理**: 检查SPF是否为单TXT记录、结尾是否为 `-all`/`~all`;检查DKIM签名是否生效;配置DMARC `_dmarc.example.com TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com"`;使用 mail-tester.com 验证完整链路
- **输出**: 三件套配置状态表 + 修复建议清单 + 验证步骤

### 场景三： CAA证书安全加固
- **输入**: 安全合规要求限制证书签发机构,仅允许 Let's Encrypt,通配符证书同样受限
- **处理**: 配置 `example.com. CAA 0 issue "letsencrypt.org"`;通配符单独配置 `CAA 0 issuewild "letsencrypt.org"`;配置 `CAA 0 iodef "mailto:security@example.com"` 接收未授权签发事件报告
- **输出**: CAA记录清单 + 未授权签发告警通道 + dig验证命令

### 场景四： Cloudflare代理导致SSH/邮件故障
- **输入**: 开启Cloudflare橙云后,SSH(22)、SMTP(25/465)、游戏服务器无法连接,但Web服务正常
- **处理**: 识别橙云仅代理HTTP/HTTPS;将非HTTP记录改为灰云(DNS-only);检查CNAME扁平化在迁移时的副作用;确认Universal SSL仅对代理记录生效,DNS-only需源站证书
- **输出**: 代理模式分类表 + 灰云切换记录清单 + 源站证书补充建议

## 案例展示

### 案例1: 迁移后部分用户仍访问旧服务器
**背景**: 将 example.com 从旧DNS商迁移到新DNS商,A记录已更新,但约30%用户48小时后仍命中旧IP。

**诊断过程**:
1. 用 `dig +trace example.com` 查看完整解析链,定位缓存层级
2. 用 `dig @8.8.8.8 example.com` 与 `dig @1.1.1.1 example.com` 对比,发现Google解析器仍返回旧IP
3. 用 `dig @ns1.oldprovider.com example.com` 直接查询旧权威服务器,确认旧DNS商记录未删除
4. 检查原TTL,发现迁移前未降TTL(仍为86400s),旧缓存需24小时才过期

**修复**:
- 在旧DNS商保留记录同步至新IP,直到新DNS全球生效
- 下次迁移前48小时将TTL降至300s
- 迁移稳定24小时后再将TTL恢复至3600s以上

### 案例2: SPF+DMARC配置后邮件仍被拒收
**背景**: 已配置SPF和DMARC,但向Gmail发送业务邮件仍被拒收。

**诊断过程**:
1. 检查SPF记录: `dig TXT example.com` 发现存在两条SPF TXT记录,这是无效配置
2. 合并为单条: `"v=spf1 include:_spf.google.com include:mailgun.org -all"`
3. 检查SPF结尾: 原为 `+all`(允许所有),改为 `-all`(拒绝)
4. 检查DKIM: 发现未配置DKIM签名,仅SPF+DMARC不足以保证投递率
5. 配置DMARC的rua报告,分析聚合数据定位失败来源

**修复**:
- 合并多条SPF为单条TXT,使用 `include:` 串联多来源
- SPF结尾强制为 `-all` 或 `~all`,禁止 `+all`/`?all`
- 补充DKIM签名配置
- 使用 mail-tester.com 验证完整三件套

### 案例3: 通配符证书签发失败
**背景**: 为 `*.example.com` 申请通配符SSL证书,使用HTTP验证方式失败。

**诊断过程**:
1. 检查DNS: `dig example.com` 与 `dig www.example.com` 发现apex无A记录,通配符不匹配apex
2. 检查CAA: 发现配置了 `CAA 0 issue "letsencrypt.org"` 但未配置 `issuewild`,导致通配符签发被拒
3. 确认验证方式: HTTP-01验证不支持通配符,必须改用DNS-01挑战

**修复**:
- 为apex单独配置A记录
- 补充 `CAA 0 issuewild "letsencrypt.org"`
- 切换至DNS-01挑战方式签发通配符证书

## 调试命令参考

### dig核心命令
- `dig +trace example.com`: 从根服务器逐级解析,展示完整解析链,定位问题发生的层级
- `dig @ns1.provider.com example.com`: 直接查询权威服务器,绕过所有缓存层,验证权威记录是否已更新
- `dig +nocmd +noall +answer example.com`: 精简输出,仅显示答案段,快速查看当前TTL与记录值
- `dig @8.8.8.8 example.com`: 指定Google公共解析器查询,用于对比不同resolver的缓存状态
- `dig @1.1.1.1 example.com`: 指定Cloudflare公共解析器查询,与Google解析器对比可判断缓存传播进度
- `dig TXT example.com`: 查询TXT记录,验证SPF/DMARC配置
- `dig MX example.com`: 查询MX记录,验证邮件路由
- `dig AAAA example.com`: 查询IPv6记录,A记录正常不代表AAAA正确
- `dig CAA example.com`: 查询CAA记录,验证证书签发机构限制
- `dig +dnssec example.com`: 查看DNSSEC签名状态,诊断SERVFAIL类错误
- `dig +short example.com`: 仅输出IP地址,适合脚本中快速获取解析结果

### 诊断策略
1. **权威与缓存对比**: 用 `dig @ns1.provider.com` 查权威,用 `dig @8.8.8.8` 查缓存,两者不一致说明传播未完成
2. **多resolver验证**: 至少对比Google(8.8.8.8)、Cloudflare(1.1.1.1)、本地ISP三个resolver,它们缓存独立
3. **全记录类型检查**: A记录正常不代表AAAA、MX、TXT都正确,需逐项检查所有相关记录类型
4. **TTL探测**: 修改记录前先探测当前缓存TTL,估算旧缓存过期时间,避免在旧TTL未过期时切换
5. **邮件认证完整验证**: SPF/DMARC配置后,使用 mail-tester.com 发送测试邮件,验证完整三件套链路是否生效

## 异常处理

### 1. dig返回SERVFAIL
**原因**: 权威服务器返回错误,常见于DNSSEC签名失败或权威服务器故障
**处理**: 用 `dig +dnssec example.com` 查看DNSSEC状态;检查DS记录是否正确发布;联系DNS托管商确认权威服务器健康度

### 2. SPF记录被截断或解析异常
**原因**: 单条TXT记录超过255字节,或使用多个TXT分别存放SPF
**处理**: 使用 `include:` 引用减少长度;SPF必须为单条TXT记录,多条SPF TXT会导致解析器只取第一条或全部拒绝

### 3. DMARC的rua报告未收到
**原因**: rua邮箱配置错误、目标域未授权接收、或报告过大被拒收
**处理**: 确认 `rua=mailto:` 邮箱可接收外部邮件;若报告域与发件域不同,需在目标域配置 `example.com._report._dmarc.reportdomain.com TXT "v=DMARC1"` 授权

### 4. Cloudflare橙云后MX记录失效
**原因**: 橙云仅代理HTTP/HTTPS,MX记录被代理后邮件路由异常
**处理**: 将MX记录及邮件相关A记录改为灰云(DNS-only);橙云仅保留在Web服务记录上

### 5. CNAME扁平化迁移后解析异常
**原因**: Cloudflare的CNAME flattening在迁移到其他DNS商时不被支持,导致apex解析失败
**处理**: 迁移前将apex的CNAME flattening改为A记录;确认新DNS商支持类似功能或改用ALIAS/ANAME记录

### 6. 通配符记录未命中子域
**原因**: `*.example.com` 不匹配apex `example.com`,且多级子域(`a.b.example.com`)也不被匹配
**处理**: 为apex单独配置记录;为多级子域单独配置或使用 `*.b.example.com` 覆盖

### 7. TTL修改后立即生效但随后回退
**原因**: 修改的是权威记录,但缓存层TTL未过期;或存在中间缓存层(企业DNS、ISP DNS)独立缓存
**处理**: 用 `dig @ns1.provider.com example.com` 确认权威记录已更新;等待各缓存层TTL自然过期;避免反复修改TTL

### 8. AAAA记录存在但IPv6访问失败
**原因**: A记录正常不代表AAAA正确;或双栈配置下IPv6路由问题
**处理**: 单独检查 `dig AAAA example.com`;确认IPv6地址可达;临时删除AAAA记录强制IPv4以隔离问题

## FAQ

### Q1: 迁移前TTL应该提前多久降低?
A: 至少提前48小时将TTL降至300秒。必须确保当前TTL(如86400s)完全过期后,新的300s TTL才会在全球解析器生效。降TTL前先用 `dig +nocmd +noall +answer example.com` 探测当前缓存TTL,避免在旧TTL未过期时切换。

### Q2: SPF可以配置多条TXT记录吗?
A: 不可以。SPF必须为单条TXT记录,多条SPF TXT记录无效。如果需要包含多个发送源,使用 `include:` 串联,如 `"v=spf1 include:_spf.google.com include:mailgun.org -all"`。SPF结尾应为 `-all`(拒绝)或 `~all`(软失败),禁止使用 `+all` 或 `?all`。

### Q3: DMARC的p=none/quarantine/reject有什么区别?
A: `p=none` 仅监控不处理,用于初始观察阶段;`p=quarantine` 将未通过认证的邮件隔离至垃圾箱;`p=reject` 直接拒绝。建议从none开始观察rua报告,逐步升级到quarantine再到reject,避免误伤合法邮件。

### Q4: Cloudflare橙云和灰云该如何选择?
A: 橙云(代理)适合HTTP/HTTPS服务,隐藏源站IP并提供CDN/WAF/Universal SSL;灰云(DNS-only)适合非HTTP服务,如SSH、SMTP、游戏服务器、MX记录。橙云会忽略用户TTL设置并破坏非HTTP服务,迁移时CNAME扁平化也易产生混淆。

### Q5: CAA记录配置后会影响现有证书续期吗?
A: 会。配置CAA后,未列入CAA的CA无法签发或续期证书。配置CAA前需确认当前所有证书签发机构都已包含在issue记录中,否则续期会失败。通配符证书需单独配置issuewild条目。

### Q6: dig +trace和dig @ns有什么区别?
A: `dig +trace` 从根服务器开始逐级解析,展示完整解析链,适合定位解析链路问题;`dig @ns1.provider.com` 直接查询指定权威服务器,绕过所有缓存,适合验证权威记录是否已更新。两者配合使用可定位缓存与权威不一致问题。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 无法直接修改DNS托管商的记录,需配合API或控制台操作执行
- DNSSEC配置因托管商差异较大,仅提供诊断思路而非自动配置
- DMARC的rua报告解析需额外工具(如parsedmarc),本Skill不内置报告解析
- Cloudflare行为基于公开文档,具体功能可能随平台更新而变化
- TTL传播时间受全球ISP缓存策略影响,无法精确预测完全生效时间
- 邮件投递率受收件方策略影响,完整三件套配置不保证100%送达
- CAA记录配置不影响已签发的现有证书,仅影响后续签发与续期
- 通配符SSL证书签发需DNS托管商支持DNS-01挑战的API自动化
