---
slug: security-hardening-shield
name: security-hardening-shield
version: "1.1.0"
displayName: "安全加固之盾"
summary: "OWASP Top 10防护+三层边界系统,上线前安全加固不留死角"
license: Proprietary
description: |-
  安全加固之盾——系统化安全防护框架,基于OWASP Top 10预防+三层边界(信任/数据/网络)分层防护,提供从输入校验到密钥管理到依赖审计的全链路加固方案。适用于上线前安全审计、认证授权设计、密钥凭证管理、依赖漏洞扫描、输入输出防护场景。触发关键词:安全加固、安全审计、OWASP、漏洞扫描、密钥管理、认证授权、依赖审计、安全边界、输入校验、安全防护
tags: [安全加固, OWASP, 安全审计, 漏洞防护, 安全架构]
tools:
  - read
  - exec
suggested_price: "50.00"
pricing_tier: "enterprise"
pricing_rationale: "安全合规类, small市场, enterprise复杂度, rare频次, enterprise层 → 低频高价值,专业壁垒高"
---
# 安全加固之盾

系统化的安全防护框架。处理用户输入、认证、数据存储、外部集成时,强制执行安全检查与加固。核心理念:默认不信任、最小权限、纵深防御。

## 核心能力

1. **OWASP Top 10 防护**:注入/XSS/CSRF/SSRF/XXE/反序列化等十大漏洞识别与防护方案
2. **三层边界系统**:信任边界(内外数据流转)/数据边界(分级保护)/网络边界(暴露面控制)分层防护
3. **认证授权设计**:密码哈希(bcrypt/argon2)、OAuth 2.0、多因子认证、RBAC/ABAC 权限模型
4. **密钥凭证管理**:密钥分级存储、KMS/Vault 集成、定期轮换、零硬编码策略
5. **依赖漏洞审计**:npm audit/pip-audit/bandit/snyk 全链路扫描与许可证合规检查

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 上线前安全审计 | 项目源码目录、技术栈 | 安全审计报告 + 漏洞清单 + 修复建议 |
| 认证授权设计 | 业务角色矩阵、权限要求 | 认证方案 + 权限模型 + 会话管理策略 |
| 密钥凭证管理 | 现有密钥使用情况 | 密钥分级方案 + 轮换策略 + 存储规范 |
| 依赖漏洞扫描 | package.json/requirements.txt | 漏洞清单 + 升级建议 + 许可证合规报告 |
| 输入防护加固 | 用户输入处理代码路径 | 输入校验白名单 + 输出编码方案 + CSP 策略 |

**不适用于**:
- 渗透测试与红蓝对抗(本Skill为加固防护,非攻击模拟)
- 实时威胁检测与入侵响应(需专用 SIEM 系统)
- 移动端 App 加固(专注于 Web/后端安全)
- 物理安全与运维安全(仅覆盖应用层安全)
- 加密算法底层实现(使用标准库,不自行实现加密)

## 使用流程

### Step 1: 项目安全画像
1. 识别项目技术栈(语言/框架/数据库/云服务)
2. 扫描代码目录结构,识别入口点(Controllers/Routes/Handlers)
3. 识别数据流:外部输入 → 处理 → 存储 → 输出
4. 输出项目安全画像报告

### Step 2: 三层边界识别
1. **信任边界**:标记所有外部输入点(HTTP API/文件上传/第三方回调)
2. **数据边界**:按敏感度标记数据(公开/敏感/密钥级)
3. **网络边界**:标记网络分区(公网/内网/隔离区)

### Step 3: OWASP Top 10 检查
1. 按风险类别逐项检查(注入/XSS/CSRF/SSRF/XXE 等)
2. 对每个发现的漏洞评估严重程度(Critical/High/Medium/Low)
3. 给出具体防护代码示例与修复建议

### Step 4: 认证授权审计
1. 检查密码存储方案(是否使用 bcrypt/argon2)
2. 检查会话管理(ID 是否随机、Cookie 安全标志)
3. 检查权限校验(是否服务端强制、是否默认拒绝)

### Step 5: 密钥与依赖审计
1. 全代码库扫描硬编码密钥(gitleaks/truffleHog)
2. 检查密钥来源是否为 KMS/Vault/环境变量
3. 执行 `npm audit` / `pip-audit` 漏洞扫描
4. 检查许可证合规性

### Step 6: 输出加固报告
1. 生成 `security-audit.md` 总览报告
2. 生成 `vulnerabilities.md` 漏洞清单(按严重程度排序)
3. 生成 `remediation.md` 修复建议(含代码示例)
4. 生成 `dependency-audit.md` 依赖审计报告

## 三层边界系统

### 边界一:信任边界(Trust Boundary)
- **外部输入区**:所有来自用户/第三方/网络的数据
- **内部可信区**:经过验证的业务数据
- **规则**:跨边界必须校验,不信任任何外部输入

### 边界二:数据边界(Data Boundary)
- **公开数据**:可对外暴露
- **敏感数据**:需加密存储/传输
- **密钥数据**:仅内存中存在,不落盘
- **规则**:按数据敏感度分级保护

### 边界三:网络边界(Network Boundary)
- **公网区**:直接暴露,需最强防护
- **内网区**:受限访问
- **隔离区**:数据库/密钥存储
- **规则**:最小暴露面,默认拒绝

## OWASP Top 10 检查表

| 风险 | 检查项 | 防护措施 |
|:-----|:-------|:---------|
| 注入 | SQL/NoSQL/命令注入 | 参数化查询、输入白名单 |
| 失效认证 | 弱密码、会话固定 | 多因子、会话过期、密码哈希 |
| 敏感数据泄露 | 明文传输/存储 | TLS、加密存储、密钥管理 |
| XML 外部实体 | XXE 注入 | 禁用外部实体解析 |
| 失效访问控制 | 越权访问 | 服务端权限校验、默认拒绝 |
| 安全配置错误 | 默认配置/错误信息泄露 | 安全基线、自定义错误页 |
| XSS | 反射/存储型 XSS | 输出编码、CSP 策略 |
| 不安全反序列化 | 远程代码执行 | 输入校验、白名单类 |
| 已知漏洞组件 | 依赖漏洞 | 依赖审计、及时升级 |
| 日志监控不足 | 攻击无感知 | 安全日志、异常告警 |

## 安全检查清单

- [ ] 所有外部输入经过校验
- [ ] 密码使用 bcrypt/argon2 哈希
- [ ] 所有传输使用 HTTPS
- [ ] 敏感数据加密存储
- [ ] 密钥不在源码中(零硬编码)
- [ ] 依赖无已知漏洞
- [ ] 错误信息不泄露内部细节
- [ ] 日志记录安全事件
- [ ] 权限服务端校验
- [ ] CORS 配置正确

## 示例

### 示例1: 上线前安全审计(输入→输出)

**输入**:
```
项目: Node.js + Express + MongoDB 电商后端
目录: /home/user/shop-backend
关注点: 用户认证、支付接口、订单数据
```

**输出**(security-audit.md 片段):
```markdown
## 安全审计报告

### 严重漏洞
1. [Critical] 登录接口 SQL 注入
   - 位置: src/auth/login.js:23
   - 代码: `db.query("SELECT * FROM users WHERE email='" + email + "'")`
   - 修复: 使用参数化查询 `db.query("SELECT * FROM users WHERE email = ?", [email])`

2. [High] 密码使用 MD5 哈希
   - 位置: src/auth/register.js:45
   - 修复: 替换为 bcrypt,`const hash = await bcrypt.hash(password, 12)`

### 中等问题
3. [Medium] CORS 配置为 `*`
   - 位置: src/app.js:15
   - 修复: `cors({ origin: ['https://shop.com'], credentials: true })`

### 通过项
- [x] 使用 HTTPS
- [x] 依赖无已知漏洞(npm audit clean)
```

### 示例2: 密钥管理加固(输入→输出)

**输入**:
```
现状: API Key 硬编码在 config.js
密钥类型: 第三方支付 API Key、数据库密码、JWT 签名密钥
目标: 实现密钥零暴露
```

**输出**(remediation.md 片段):
```markdown
## 密钥加固方案

### 1. 立即移除硬编码
- 将 config.js 中的所有密钥移除
- 替换为环境变量读取:`process.env.PAYMENT_API_KEY`

### 2. 密钥分级管理
| 等级 | 类型 | 存储方式 | 轮换周期 |
|:-----|:-----|:---------|:---------|
| 主密钥 | KMS Master Key | AWS KMS / 阿里云 KMS | 180天 |
| 数据密钥 | 业务数据加密密钥 | KMS 解密后内存使用 | 90天 |
| 会话密钥 | JWT 签名密钥 | 环境变量 + Vault | 30天 |

### 3. 国内替代方案
- AWS KMS → 阿里云 KMS / 腾讯云 KMS
- HashiCorp Vault → 阿里云密钥管理服务 / 自建 Vault
- AWS Secrets Manager → 阿里云凭据管家

### 4. 检测机制
- 提交前 hook: `gitleaks protect --staged`
- CI/CD 集成: `trufflehog filesystem --path=./src`
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| 静态扫描工具未安装 | 环境缺少 bandit/eslint-plugin-security | 提示安装命令并跳过该工具检查,继续其他维度审计 |
| 源码目录无 package.json/requirements.txt | 非标准项目结构 | 询问用户技术栈,手动指定依赖文件路径 |
| 硬编码密钥误报 | 测试用 Mock 数据被识别 | 用户确认后加入白名单,记录到审计日志 |
| 漏洞修复影响业务 | 修复方案与现有代码冲突 | 提供 2 个备选方案(短期缓解 + 长期修复) |
| 国内无法访问海外漏洞库 | NVD/OSV 网络超时 | 切换国内镜像或使用离线漏洞数据库 |
| 密钥扫描耗时过长 | 大型代码库 | 限制扫描文件类型(.js/.py/.go),排除 node_modules |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代 |
|:-------|:-----|:---------|:---------|:---------|
| LLM API | API | 必需 | Agent 内置 LLM 提供分析能力 | 国内 LLM(通义/文心/智谱) |
| npm audit | 工具 | 可选 | Node.js 自带 | cnpm audit |
| pip-audit | 工具 | 可选 | `pip install pip-audit` | 国内 PyPI 镜像安装 |
| bandit | 工具 | 可选 | `pip install bandit` | 国内 PyPI 镜像安装 |
| gitleaks | 工具 | 可选 | GitHub Releases | TruffleHog / 国内 GitLab 内置扫描 |
| snyk | 工具 | 可选 | `npm install -g snyk` | 阿里云依赖审计服务 |

### API Key 配置
- **本Skill无需额外API Key配置**
- **安全要求**: 扫描过程中如发现硬编码密钥,立即提示用户轮换并从代码库历史中清除

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,需 exec 能力调用静态分析工具

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: Node.js电商后端上线前安全审计

**输入**:
```
项目: Node.js + Express + MongoDB 电商后端
目录: /home/user/shop-backend
关注点: 用户认证、支付接口、订单数据
入口文件: src/app.js
API路由: src/routes/auth.js, src/routes/payment.js, src/routes/orders.js
```

**LLM生成输出** (`output/shop-backend/security-audit.md`):
```markdown
# 安全审计报告 - shop-backend

## 项目安全画像
- 技术栈: Node.js 18 + Express 4 + MongoDB 5
- 入口点: 3个路由模块(auth/payment/orders),共18个API端点
- 数据流: HTTP请求 → Express中间件 → Controller → MongoDB
- 三层边界:
  - 信任边界: 18个API端点均为外部输入点
  - 数据边界: 用户密码(密钥级)/订单数据(敏感)/商品信息(公开)
  - 网络边界: API服务(公网)/MongoDB(内网隔离)

## 审计结果概览
| 严重程度 | 数量 | OWASP类别 |
|:---------|:-----|:----------|
| Critical | 2 | 注入、失效认证 |
| High | 3 | 敏感数据泄露、失效访问控制、XSS |
| Medium | 4 | 安全配置错误、已知漏洞组件等 |
| Low | 2 | 日志监控、CORS |
| 通过项 | 8 | HTTPS、参数化查询(部分)等 |
```

**LLM生成输出** (`output/shop-backend/vulnerabilities.md`):
```markdown
# 漏洞清单(按严重程度排序)

## Critical级别

### VULN-001: 登录接口NoSQL注入
- **OWASP类别**: A03:2021 - Injection
- **严重程度**: Critical
- **位置**: `src/routes/auth.js:23`
- **漏洞代码**:
```javascript
router.post("/login", async (req, res) => {
  const { email, password } = req.body;
  // 危险:直接将用户输入传入查询
  const user = await User.findOne({ email, password: hashPassword(password) });
  // 攻击者可发送 {"email":{"$ne":""},"password":{"$ne":""}} 绕过认证
});
```
- **影响**: 攻击者可通过NoSQL注入绕过认证,以任意用户身份登录
- **修复方案**:
```javascript
const { email, password } = req.body;
// 输入校验:确保email和password是字符串
if (typeof email !== "string" || typeof password !== "string") {
  return res.status(400).json({ error: "无效的输入" });
}
// 使用参数化查询
const user = await User.findOne({ email: email });
if (!user || !await bcrypt.compare(password, user.passwordHash)) {
  return res.status(401).json({ error: "邮箱或密码错误" });
}
```

### VULN-002: 密码使用MD5哈希
- **OWASP类别**: A02:2021 - Cryptographic Failures
- **严重程度**: Critical
- **位置**: `src/routes/auth.js:45`
- **漏洞代码**:
```javascript
const crypto = require("crypto");
const hash = crypto.createHash("md5").update(password).digest("hex");
// MD5已被证明不安全,彩虹表攻击可在秒级破解
```
- **影响**: 数据库泄露后,所有用户密码可在数小时内被破解
- **修复方案**:
```javascript
const bcrypt = require("bcrypt");
// 使用bcrypt,cost factor=12
const saltRounds = 12;
const hash = await bcrypt.hash(password, saltRounds);
// 或使用argon2(更安全)
const argon2 = require("argon2");
const hash = await argon2.hash(password, {
  type: argon2.argon2id,
  memoryCost: 65536,
  timeCost: 3,
  parallelism: 1,
});
```

## High级别

### VULN-003: 支付接口缺少服务端权限校验
- **OWASP类别**: A01:2021 - Broken Access Control
- **严重程度**: High
- **位置**: `src/routes/payment.js:34`
- **漏洞代码**:
```javascript
router.post("/pay", async (req, res) => {
  const { orderId, amount } = req.body;
  // 危险:未校验当前用户是否拥有该订单
  const result = await processPayment(orderId, amount);
  res.json(result);
});
```
- **影响**: 用户A可支付用户B的订单,或篡改订单金额
- **修复方案**:
```javascript
router.post("/pay", authenticate, async (req, res) => {
  const { orderId, amount } = req.body;
  const userId = req.user.id;

  // 服务端权限校验:确认订单属于当前用户
  const order = await Order.findById(orderId);
  if (!order || order.userId !== userId) {
    return res.status(403).json({ error: "无权操作此订单" });
  }

  // 服务端金额校验:不信任客户端传入的金额
  if (amount !== order.totalAmount) {
    return res.status(400).json({ error: "金额不匹配" });
  }

  const result = await processPayment(orderId, order.totalAmount);
  res.json(result);
});
```

### VULN-004: 商品评论存在存储型XSS
- **OWASP类别**: A03:2021 - Injection (XSS)
- **严重程度**: High
- **位置**: `src/routes/products.js:67`
- **漏洞代码**:
```javascript
router.post("/:id/review", async (req, res) => {
  const { content } = req.body;
  // 危险:评论内容未转义直接存储和返回
  await Review.create({ productId: req.params.id, content });
  res.json({ success: true });
});
// 前端渲染: <div>{review.content}</div>  ← XSS!
```
- **影响**: 攻击者可注入恶意脚本,窃取其他用户的session token
- **修复方案**:
```javascript
// 方案1: 服务端输出编码(推荐使用DOMPurify)
const DOMPurify = require("isomorphic-dompurify");
const cleanContent = DOMPurify.sanitize(content);
await Review.create({ productId: req.params.id, content: cleanContent });

// 方案2: 前端使用安全的渲染方式
// React默认转义: <div>{review.content}</div> ← 安全
// 避免使用: dangerouslySetInnerHTML
```

### VULN-005: 错误信息泄露堆栈跟踪
- **OWASP类别**: A05:2021 - Security Misconfiguration
- **严重程度**: High
- **位置**: `src/app.js:85`
- **漏洞代码**:
```javascript
app.use((err, req, res, next) => {
  res.status(500).json({
    error: err.message,
    stack: err.stack,  // 危险:泄露服务器文件路径和依赖版本
  });
});
```
- **修复方案**:
```javascript
app.use((err, req, res, next) => {
  // 生产环境不泄露内部错误
  if (process.env.NODE_ENV === "production") {
    res.status(500).json({ error: "服务器内部错误" });
  } else {
    res.status(500).json({ error: err.message, stack: err.stack });
  }
  // 安全日志记录完整错误(不返回给客户端)
  logger.error("Unhandled error", { error: err.stack, path: req.path });
});
```

## 通过项
- [x] 使用HTTPS(SSL证书有效)
- [x] 订单查询使用参数化查询(Mongoose)
- [x] JWT签名密钥来自环境变量
- [x] npm audit无已知漏洞
- [x] 文件上传限制类型和大小
- [x] 速率限制已启用(express-rate-limit)
- [x] Helmet中间件已配置
- [x] CORS配置为指定域名(非通配符)
```

**LLM生成输出** (`output/shop-backend/remediation.md`):
```markdown
# 修复建议与优先级

## 修复优先级矩阵
| 优先级 | 漏洞 | 预估工时 | 风险 | 建议时间 |
|:-------|:-----|:---------|:-----|:---------|
| P0 | VULN-001 NoSQL注入 | 2h | 认证绕过 | 立即 |
| P0 | VULN-002 MD5哈希 | 4h | 密码泄露 | 立即 |
| P1 | VULN-003 越权支付 | 3h | 资金损失 | 24h内 |
| P1 | VULN-004 存储型XSS | 2h | 会话劫持 | 24h内 |
| P1 | VULN-005 错误泄露 | 1h | 信息泄露 | 48h内 |

## 密码哈希迁移方案
```javascript
// 迁移脚本:将MD5密码逐步迁移到bcrypt
async function migratePasswords() {
  const users = await User.find({ passwordHash: { $regex: /^[a-f0-9]{32}$/ } });
  for (const user of users) {
    // 用户下次登录时,用MD5验证后立即升级为bcrypt
    // 详见: src/auth/migrate-hash.js
  }
}
```

## 验证命令
```bash
# 重新扫描
npx eslint src/ --ext .js --rulesdir ./eslint-rules

# 依赖审计
npm audit

# 密钥扫描
gitleaks detect --source . --report-path ./gitleaks-report.json

# 启动应用验证
NODE_ENV=production npm start
```
```

**效果验证**: ✓OWASP Top 10分类标注(A01-A05) ✓每个漏洞含位置+代码+影响+修复 ✓严重程度四级(Critical/High/Medium/Low) ✓修复优先级矩阵含工时估算 ✓密码哈希迁移方案(渐进式升级)

### 案例2: 认证授权系统设计(OAuth 2.0 + RBAC)

**输入**:
```
需求: 设计SaaS平台的认证授权系统
角色: 超级管理员/企业管理员/普通用户/访客
功能: 账密登录、OAuth第三方登录、API Key访问、多因子认证
技术栈: Node.js + PostgreSQL + Redis
```

**LLM生成输出** (`output/auth-design/auth-system.md`):
```markdown
# 认证授权系统设计方案

## 1. 认证方案

### 1.1 密码认证(核心)
```javascript
const bcrypt = require("bcrypt");
const argon2 = require("argon2");

// 密码存储:使用argon2id(推荐)或bcrypt
async function hashPassword(plainPassword) {
  return argon2.hash(plainPassword, {
    type: argon2.argon2id,
    memoryCost: 65536,  // 64MB
    timeCost: 3,        // 3次迭代
    parallelism: 1,
  });
}

// 密码验证:使用恒定时间比较防时序攻击
async function verifyPassword(plainPassword, hash) {
  return argon2.verify(hash, plainPassword);
}

// 密码策略
const passwordPolicy = {
  minLength: 12,
  requireUppercase: true,
  requireLowercase: true,
  requireNumbers: true,
  requireSpecialChars: true,
  breachCheck: true,  // 检查是否在已知泄露密码库中
};
```

### 1.2 多因子认证(MFA)
```javascript
const speakeasy = require("speakeasy");
const QRCode = require("qrcode");

// 生成TOTP密钥
async function setupMFA(userId) {
  const secret = speakeasy.generateSecret({
    name: `SaaS Platform:${userId}`,
  });
  // 存储密钥(加密后存数据库)
  await storeEncrypted(userId, secret.base32);
  // 返回QR码供用户扫描
  const qrUrl = await QRCode.toDataURL(secret.otpauth_url);
  return { qrUrl, secret: secret.base32 };
}

// 验证TOTP
function verifyMFA(userId, token) {
  const secret = getDecryptedSecret(userId);
  return speakeasy.totp.verify({
    secret,
    encoding: "base32",
    token,
    window: 1,  // 允许前后1个时间窗口(30秒)
  });
}
```

### 1.3 OAuth 2.0第三方登录
```javascript
// OAuth 2.0授权码流程(以Google为例)
const { google } = require("googleapis");

const oauth2Client = new google.auth.OAuth2(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  process.env.GOOGLE_REDIRECT_URI
);

// Step 1: 重定向到Google授权页
app.get("/auth/google", (req, res) => {
  const url = oauth2Client.generateAuthUrl({
    access_type: "offline",
    scope: ["profile", "email"],
    state: req.session.oauthState,  // CSRF防护
  });
  res.redirect(url);
});

// Step 2: 回调处理
app.get("/auth/google/callback", async (req, res) => {
  // 验证state防止CSRF
  if (req.query.state !== req.session.oauthState) {
    return res.status(403).json({ error: "Invalid state" });
  }
  const { tokens } = await oauth2Client.getToken(req.query.code);
  // 用tokens获取用户信息,创建/更新本地用户
  const userInfo = await oauth2Client.getTokenInfo(tokens.access_token);
  await upsertUser({
    email: userInfo.email,
    oauthProvider: "google",
    oauthId: userInfo.sub,
  });
  // 生成本地JWT
  const jwt = generateJWT(userInfo.email);
  res.redirect(`/auth/success?token=${jwt}`);
});
```

### 1.4 会话管理
```javascript
// JWT + Redis黑名单(支持主动登出)
const jwt = require("jsonwebtoken");

function generateJWT(userId) {
  return jwt.sign(
    { sub: userId, iat: Date.now() },
    process.env.JWT_SECRET,
    { expiresIn: "15m" }  // 短期access token
  );
}

// Refresh Token(长期,存储在Redis)
async function generateRefreshToken(userId) {
  const refreshToken = crypto.randomBytes(32).toString("hex");
  const hashed = await bcrypt.hash(refreshToken, 10);
  await redis.set(`refresh:${userId}`, hashed, "EX", 7 * 24 * 3600);
  return refreshToken;
}

// 登出:将JWT加入Redis黑名单
async function logout(token) {
  const decoded = jwt.decode(token);
  const ttl = decoded.exp - Math.floor(Date.now() / 1000);
  await redis.set(`blacklist:${token}`, "1", "EX", ttl);
}

// 中间件:验证JWT
async function authenticate(req, res, next) {
  const token = req.headers.authorization?.replace("Bearer ", "");
  if (!token) return res.status(401).json({ error: "未提供token" });

  // 检查黑名单
  const blacklisted = await redis.get(`blacklist:${token}`);
  if (blacklisted) return res.status(401).json({ error: "token已失效" });

  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch {
    return res.status(401).json({ error: "token无效或已过期" });
  }
}
```

## 2. 授权方案(RBAC)

### 2.1 权限模型
```sql
-- 角色表
CREATE TABLE roles (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) UNIQUE NOT NULL,
  description TEXT
);

-- 权限表
CREATE TABLE permissions (
  id SERIAL PRIMARY KEY,
  resource VARCHAR(50) NOT NULL,  -- 资源:order/user/payment
  action VARCHAR(20) NOT NULL,    -- 动作:create/read/update/delete
  description TEXT
);

-- 角色-权限映射(多对多)
CREATE TABLE role_permissions (
  role_id INT REFERENCES roles(id),
  permission_id INT REFERENCES permissions(id),
  PRIMARY KEY (role_id, permission_id)
);

-- 用户-角色映射
CREATE TABLE user_roles (
  user_id INT REFERENCES users(id),
  role_id INT REFERENCES roles(id),
  scope_id INT,  -- 作用域(企业ID),支持ABAC
  PRIMARY KEY (user_id, role_id, scope_id)
);
```

### 2.2 权限矩阵
| 角色 | order:create | order:read | order:update | user:read | user:delete |
|:-----|:-------------|:-----------|:-------------|:----------|:------------|
| 超级管理员 | ✓ | ✓ | ✓ | ✓ | ✓ |
| 企业管理员 | ✓ | ✓(本企业) | ✓(本企业) | ✓(本企业) | ✗ |
| 普通用户 | ✓(本人) | ✓(本人) | ✗ | ✗ | ✗ |
| 访客 | ✗ | ✗ | ✗ | ✗ | ✗ |

### 2.3 权限校验中间件
```javascript
function requirePermission(resource, action) {
  return async (req, res, next) => {
    const userId = req.user.id;
    const scopeId = req.user.enterpriseId;  // 企业作用域

    // 查询用户是否有该权限
    const hasPermission = await checkPermission(userId, resource, action, scopeId);
    if (!hasPermission) {
      return res.status(403).json({ error: "权限不足" });
    }
    next();
  };
}

// 使用示例
router.post("/orders",
  authenticate,
  requirePermission("order", "create"),
  createOrder
);

router.get("/users/:id",
  authenticate,
  requirePermission("user", "read"),
  getUser
);
```

## 3. API Key认证(机器间访问)
```javascript
// API Key格式: sak_{32位随机字符}_{校验码}
function generateAPIKey() {
  const key = crypto.randomBytes(32).toString("hex");
  const checksum = crypto.createHash("sha256").update(key).digest("hex").substring(0, 8);
  return `sak_${key}_${checksum}`;
}

// API Key存储:仅存储哈希值
async function storeAPIKey(userId, key) {
  const hashed = await bcrypt.hash(key, 12);
  await db.query(
    "INSERT INTO api_keys (user_id, key_hash, scopes, expires_at) VALUES (?, ?, ?, ?)",
    [userId, hashed, ["read:orders"], new Date(Date.now() + 365 * 24 * 3600 * 1000)]
  );
}

// API Key验证
async function verifyAPIKey(req, res, next) {
  const apiKey = req.headers["x-api-key"];
  if (!apiKey || !apiKey.startsWith("sak_")) {
    return res.status(401).json({ error: "无效的API Key" });
  }
  // 查询并验证(恒定时间比较)
  const keys = await db.query("SELECT * FROM api_keys WHERE expires_at > NOW()");
  for (const row of keys.rows) {
    if (await bcrypt.compare(apiKey, row.key_hash)) {
      req.apiKey = { userId: row.user_id, scopes: row.scopes };
      return next();
    }
  }
  return res.status(401).json({ error: "API Key无效或已过期" });
}
```

## 4. 安全检查清单
- [x] 密码使用argon2id哈希(cost=64MB/3迭代)
- [x] 支持TOTP多因子认证
- [x] OAuth 2.0含state参数(CSRF防护)
- [x] JWT短有效期(15min)+Refresh Token(7天)
- [x] Redis黑名单支持主动登出
- [x] RBAC含作用域(企业隔离)
- [x] API Key仅存储哈希值
- [x] 权限默认拒绝(白名单模式)
- [x] 恒定时间比较防时序攻击
- [x] 密码策略(12位+复杂度+泄露检查)
```

**效果验证**: ✓密码认证(argon2id+密码策略) ✓MFA(TOTP+QR码) ✓OAuth 2.0完整流程(state+CSRF防护) ✓JWT+Refresh Token+黑名单 ✓RBAC含作用域(企业隔离) ✓API Key仅存哈希 ✓恒定时间比较防时序攻击

### 案例3: 密钥管理加固(从硬编码到KMS)

**输入**:
```
现状审计发现:
1. config.js中硬编码3个API Key和2个数据库密码
2. JWT密钥写在docker-compose.yml中
3. 第三方支付密钥直接写在前端配置中
目标: 实现密钥零暴露,使用KMS管理
```

**LLM生成输出** (`output/key-management/hardening.md`):
```markdown
# 密钥管理加固方案

## 1. 当前密钥暴露清单(脱敏)
| 密钥 | 位置 | 类型 | 暴露风险 |
|:-----|:-----|:-----|:---------|
| PAYMENT_KEY: sk_live_****1234 | config.js:12 | 支付API | Critical |
| DB_PASSWORD: p@ss****w0rd | config.js:15 | 数据库密码 | Critical |
| JWT_SECRET: jwt_****secret | docker-compose.yml:8 | 签名密钥 | High |
| AWS_KEY: AKIA****XXXX | config.js:18 | 云服务凭证 | Critical |
| STRIPE_KEY: sk_live_****5678 | frontend/.env | 支付密钥 | Critical(前端暴露) |

## 2. 密钥分级方案
| 等级 | 密钥类型 | 存储方式 | 轮换周期 | 访问控制 |
|:-----|:---------|:---------|:---------|:---------|
| L1-主密钥 | KMS Master Key | 阿里云KMS | 180天 | 仅运维团队 |
| L2-数据密钥 | 数据库加密密钥 | KMS解密后内存使用 | 90天 | 应用服务账号 |
| L3-会话密钥 | JWT签名密钥 | 环境变量+Vault | 30天 | 应用服务账号 |
| L4-API密钥 | 第三方API Key | 凭据管家(阿里云) | 按需 | 按最小权限 |

## 3. 加固实施步骤

### Step 1: 立即移除硬编码密钥
```bash
# 1. 在密钥服务商控制台立即轮换所有暴露的密钥
# 2. 从代码中移除硬编码

# 修复前(config.js):
module.exports = {
  PAYMENT_KEY: "sk_live_abc123def456",  // ← 删除
  DB_PASSWORD: "p@ssw0rd123",           // ← 删除
};

# 修复后(config.js):
module.exports = {
  PAYMENT_KEY: process.env.PAYMENT_KEY,  // 从环境变量读取
  DB_PASSWORD: process.env.DB_PASSWORD,
};
```

### Step 2: 清除Git历史中的密钥
```bash
# 使用BFG Repo-Cleaner清除历史
bfg --replace-text passwords.txt
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 或使用git filter-repo
git filter-repo --invert-paths --path config.js
```

### Step 3: 集成KMS(阿里云)
```javascript
// KMS集成示例(阿里云)
const KMS = require("@alicloud/kms20160120");

const client = new KMS({
  accessKeyId: process.env.KMS_ACCESS_KEY,
  accessKeySecret: process.env.KMS_SECRET,
  endpoint: "https://kms.cn-hangzhou.aliyuncs.com",
});

// 从KMS获取数据密钥(信封加密)
async function getDataKey() {
  const result = await client.generateDataKey({
    KeyId: process.env.KMS_KEY_ID,    // 主密钥ID
    KeySpec: "AES_256",                // 256位AES密钥
  });
  return {
    ciphertextBlob: result.body.ciphertextBlob,  // 加密的密钥(可落盘)
    plaintext: result.body.plaintext,            // 明文密钥(仅内存)
  };
}

// 数据库字段加密
async function encryptField(plaintext) {
  const { ciphertextBlob, plaintext: dataKey } = await getDataKey();
  const cipher = crypto.createCipheriv("aes-256-gcm", Buffer.from(dataKey, "base64"), iv);
  const encrypted = Buffer.concat([cipher.update(plaintext, "utf8"), cipher.final()]);
  return { ciphertextBlob, encrypted: encrypted.toString("base64"), iv: iv.toString("base64"), authTag: cipher.getAuthTag().toString("base64") };
}
```

### Step 4: 添加pre-commit hook防止再次提交密钥
```bash
# .git/hooks/pre-commit
#!/bin/bash
gitleaks protect --staged --redact --report-path ./gitleaks-report.json
if [ $? -eq 1 ]; then
  echo "⚠️ 检测到硬编码密钥!请移除后重新提交。"
  echo "报告: ./gitleaks-report.json"
  exit 1
fi
```

### Step 5: CI/CD集成密钥扫描
```yaml
# .github/workflows/security.yml
name: Security Scan
on: [push, pull_request]
jobs:
  gitleaks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 4. 前端密钥处理
```javascript
// 错误:支付密钥不能出现在前端
// frontend/.env: REACT_APP_STRIPE_KEY=sk_live_xxx  ← 绝对禁止

// 正确:使用后端代理调用第三方API
// frontend/api.js
async function createPayment(orderId) {
  // 前端仅调用自己的后端
  const response = await fetch("/api/payment/create", {
    method: "POST",
    body: JSON.stringify({ orderId }),
  });
  return response.json();
  // 后端(使用KMS中的密钥)调用Stripe API
}
```

## 5. 验证检查
- [ ] Git历史中无密钥(gitleaks扫描通过)
- [ ] 代码中无硬编码密钥(grep扫描)
- [ ] 所有密钥通过环境变量/KMS获取
- [ ] pre-commit hook已启用
- [ ] CI/CD含密钥扫描步骤
- [ ] 所有暴露密钥已在服务商处轮换
```

**效果验证**: ✓密钥暴露清单脱敏显示 ✓密钥四级分类(L1-L4+轮换周期) ✓KMS信封加密方案(主密钥+数据密钥) ✓Git历史清除步骤(BFG/git filter-repo) ✓pre-commit hook + CI/CD双重防护

### 案例4: 依赖漏洞审计(Node.js项目)

**输入**:
```
项目: Node.js电商后端
package.json依赖: express, mongoose, jwt, bcrypt, axios, lodash等32个包
要求: 全链路漏洞扫描+许可证合规检查+修复建议
```

**LLM生成输出** (`output/dep-audit/dependency-audit.md`):
```markdown
# 依赖漏洞审计报告

## 审计概览
- 依赖总数: 32个直接依赖 + 287个间接依赖
- 已知漏洞: 8个(1 Critical + 2 High + 3 Medium + 2 Low)
- 许可证合规: 1个不合规(GPL-3.0)
- 审计工具: npm audit + snyk + license-checker

## 漏洞清单

### Critical
| 包名 | 当前版本 | 漏洞编号 | 影响 | 修复版本 |
|:-----|:---------|:---------|:-----|:---------|
| lodash | 4.17.20 | CVE-2021-23337 | 命令注入 | ≥4.17.21 |

### High
| 包名 | 当前版本 | 漏洞编号 | 影响 | 修复版本 |
|:-----|:---------|:---------|:-----|:---------|
| axios | 0.21.0 | CVE-2021-3749 | ReDoS正则拒绝服务 | ≥0.21.2 |
| jsonwebtoken | 8.5.1 | CVE-2022-23529 | 认证绕过 | ≥9.0.0 |

### Medium
| 包名 | 当前版本 | 漏洞编号 | 影响 | 修复版本 |
|:-----|:---------|:---------|:-----|:---------|
| minimist | 1.2.5 | CVE-2021-44906 | 原型污染 | ≥1.2.6 |
| ansi-regex | 5.0.0 | CVE-2021-3807 | ReDoS | ≥5.0.1 |
| tmpl | 1.0.4 | CVE-2021-3749 | ReDoS | ≥1.0.5 |

## 修复方案

### 立即修复(Critical + High)
```bash
# 1. 更新lodash(直接依赖)
npm install lodash@4.17.21

# 2. 更新axios
npm install axios@1.6.0

# 3. 更新jsonwebtoken(注意:9.0.0有Breaking Change)
npm install jsonwebtoken@9.0.0
# 需要同步修改代码:
# - algorithm默认从HS256变为RS256
# - 需显式指定: jwt.sign(payload, secret, { algorithm: "HS256" })
```

### 计划修复(Medium + Low)
```bash
# 批量更新间接依赖
npm audit fix

# 无法自动修复的手动处理
npm install minimist@1.2.8
```

## 许可证合规报告
| 许可证类型 | 数量 | 合规状态 |
|:-----------|:-----|:---------|
| MIT | 268 | ✓ 合规 |
| Apache-2.0 | 12 | ✓ 合规 |
| BSD-3-Clause | 8 | ✓ 合规 |
| ISC | 5 | ✓ 合规 |
| GPL-3.0 | 1 | ✗ 不合规(需替换) |

### GPL-3.0依赖处理
```bash
# 定位GPL-3.0依赖
npx license-checker --summary | grep GPL
# 发现: react-sortable-tree 使用 GPL-3.0

# 替换为MIT许可的替代品
npm uninstall react-sortable-tree
npm install react-dnd  # MIT许可,功能类似
```

## CI/CD自动化审计
```yaml
# .github/workflows/dependency-audit.yml
name: Dependency Audit
on: [pull_request, schedule]
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - name: npm audit
        run: npm audit --audit-level=high
      - name: Snyk scan
        uses: snyk/actions/node@master
        with:
          command: monitor
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      - name: License check
        run: npx license-checker --production --onlyAllow "MIT;Apache-2.0;BSD-3-Clause;ISC"
```

## 审计验证
```bash
# 修复后重新审计
npm audit
# 预期: 0 vulnerabilities

# 许可证检查
npx license-checker --summary
# 预期: 无GPL依赖
```
```

**效果验证**: ✓漏洞分级清晰(Critical/High/Medium/Low) ✓每个漏洞含CVE编号+影响+修复版本 ✓jsonwebtoken升级Breaking Change提醒 ✓GPL-3.0许可证不合规处理 ✓CI/CD自动化审计配置

## 常见问题

### Q1: 这个Skill能完全替代渗透测试吗?
A: 不能。本Skill是**安全加固方法论**,聚焦于代码层面的预防与修复。渗透测试需要专业工具(Burp Suite/Nessus)和攻击视角的模拟,建议上线前结合使用:本Skill做白盒加固,渗透测试做黑盒验证。

### Q2: 扫描结果显示无漏洞,是否就安全了?
A: 不一定。静态扫描只能发现已知模式的漏洞,无法覆盖业务逻辑漏洞、零日漏洞、配置错误等问题。建议结合:依赖扫描 + 静态分析 + 代码审计 + 渗透测试 + 运行时监控,形成纵深防御。

### Q3: 国内项目使用哪些安全扫描工具?
A: 推荐:
- Python: `bandit`(代码扫描)+ `pip-audit`(依赖扫描)+ `safety`(漏洞库)
- Node.js: `npm audit` + `eslint-plugin-security` + `snyk`
- Go: `gosec` + `govulncheck`
- 通用密钥扫描: `gitleaks`(开源) / 阿里云代码安全扫描 / 腾讯云代码分析

### Q4: 如何处理历史提交中的硬编码密钥?
A: 1) 立即在服务方控制台轮换该密钥;2) 使用 `git filter-repo` 或 BFG Repo-Cleaner 清除历史;3) 强制推送并通知协作者重新克隆;4) 添加 pre-commit hook 防止再次提交。

## 已知限制

- 仅覆盖 Web/后端应用层安全,不涉及网络层防火墙与 WAF 配置
- 静态扫描无法发现运行时漏洞与业务逻辑漏洞(如越权、并发竞争)
- 不提供加密算法实现,仅推荐使用标准库(bcrypt/argon2/AES-GCM)
- 国内环境访问 NVD/OSV 等海外漏洞库可能超时,需切换国内镜像
- 不替代专业安全审计团队的人工代码审查
- 不覆盖移动端 App、IoT 设备、智能合约等特定领域安全

## 安全声明

- 本Skill执行过程中产生的所有密钥信息仅在内存中处理,不写入日志或输出文件
- 扫描结果中的密钥样本会自动脱敏(只显示前后 4 位)
- 建议用户在 CI/CD 中将本Skill的输出标记为敏感产物,限制访问权限
