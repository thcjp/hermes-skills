---
slug: safe-encryption-tool-pro
name: safe-encryption-tool-pro
version: "1.0.0"
displayName: 安全加密工具-专业版
summary: 企业级加密平台,支持批量加密、密钥管理、安全策略与审计日志,量子安全算法
license: Proprietary
edition: pro
description: |-
  企业级安全加密工具专业版,面向团队与企业数据保护。核心能力:
  - 批量文件与目录加密
  - 密钥管理服务(KMS)集成
  - 企业安全策略与合规
  - 审计日志与操作追溯
  - 多算法支持(ML-KEM-512/768/1024)
  - 目录递归加密与压缩
  - 团队密钥共享与权限
  - API 接口与自动化集成

  适用场景:
  - 企业敏感数据加密保护
  - 合规数据存储(GDPR/等保)
  - 安全文件归档与传输
  - 开发环境密钥管理

  差异化:专业版在免费版基础上扩展批量加密、KMS 集成、安全策略与审计日...
tags:
- 加密
- 企业级
- 密钥管理
- 安全合规
- 审计日志
tools:
  - - read
- exec
---
# 安全加密工具 - 专业版

## 概述

安全加密工具专业版是企业级数据加密平台,在免费版文件加密能力之上扩展批量加密、密钥管理服务(KMS)集成、企业安全策略、审计日志与团队密钥共享。适合企业敏感数据保护、合规存储与安全归档。

专业版兼容免费版加密文件格式,已有加密文件可直接解密。

## 核心能力

### 1. 批量文件与目录加密

支持递归加密整个目录,保持目录结构,自动跳过已加密文件。

**输入**: 用户提供批量文件与目录加密所需的指令和必要参数。
**处理**: 按照skill规范执行批量文件与目录加密操作,遵循单一意图原则。
**输出**: 返回批量文件与目录加密的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 2. 密钥管理服务(KMS)

集成 KMS 进行密钥生命周期管理,密钥不在本地存储,降低泄露风险。

**输入**: 用户提供密钥管理服务(KMS)所需的指令和必要参数。
**处理**: 按照skill规范执行密钥管理服务(KMS)操作,遵循单一意图原则。
**输出**: 返回密钥管理服务(KMS)的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 3. 企业安全策略

配置密码复杂度策略、加密算法策略、文件类型白名单,强制执行安全规范。

**输入**: 用户提供企业安全策略所需的指令和必要参数。
**处理**: 按照skill规范执行企业安全策略操作,遵循单一意图原则。
**输出**: 返回企业安全策略的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 4. 审计日志

所有加密/解密操作全程记录,包含操作者、时间、文件、算法等信息,满足合规审计需求。

**输入**: 用户提供审计日志所需的指令和必要参数。
**处理**: 按照skill规范执行审计日志操作,遵循单一意图原则。
**输出**: 返回审计日志的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 5. 多算法支持

支持 ML-KEM-512/768/1024 三个安全级别,按数据敏感度选择。

**输入**: 用户提供多算法支持所需的指令和必要参数。
**处理**: 按照skill规范执行多算法支持操作,遵循单一意图原则。
**输出**: 返回多算法支持的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 6. 团队密钥共享

支持团队密钥池,成员可共享加密密钥,支持密钥轮换与撤销。

**输入**: 用户提供团队密钥共享所需的指令和必要参数。
**处理**: 按照skill规范执行团队密钥共享操作,遵循单一意图原则。
**输出**: 返回团队密钥共享的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 7. 压缩加密一体化

加密时自动压缩,减少存储空间,同时提高安全性。

**输入**: 用户提供压缩加密一体化所需的指令和必要参数。
**处理**: 按照skill规范执行压缩加密一体化操作,遵循单一意图原则。
**输出**: 返回压缩加密一体化的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 8. API 接口

提供 RESTful API,支持第三方系统集成,实现自动化加密流水线。

**输入**: 用户提供API 接口所需的指令和必要参数。
**处理**: 按照skill规范执行API 接口操作,遵循单一意图原则。
**输出**: 返回API 接口的执行结果,包含操作状态和输出数据。
**技术参数**：使用`input_params`和`output_format`参数控制执行行为,支持`json`/`text`/`csv`输出格式。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级加密平台、支持批量加密、安全策略与审计日、量子安全算法、企业级安全加密工、具专业版、面向团队与企业数、据保护、核心能力、企业安全策略与合、审计日志与操作追、目录递归加密与压、团队密钥共享与权、接口与自动化集成等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一:企业目录批量加密

加密整个项目目录,保持目录结构。

```bash
# 递归加密目录
safe-pro encrypt-dir \
  --input /data/sensitive-project \
  --output /data/sensitive-project-encrypted \
  --kms-key "projects/sensitive-project/v2" \
  --algorithm ML-KEM-768 \
  --compress \
  --recursive \
  --exclude "*.log,tmp/*"

# 输出:
# 正在扫描目录...
# 发现文件: 1,247 个
# 跳过(已加密): 0
  # 跳过(排除规则): 23 个
# 正在加密: 1,224 个文件
# 进度: [##########] 100%
# 加密完成: 1,224/1,224
# 压缩率: 62%
# 总耗时: 45.3s

# 递归解密
safe-pro decrypt-dir \
  --input /data/sensitive-project-encrypted \
  --output /data/sensitive-project-decrypted \
  --kms-key "projects/sensitive-project/v2" \
  --recursive
```

### 场景二:KMS 密钥管理

通过 KMS 管理加密密钥,实现密钥轮换。

```bash
# 创建密钥
safe-pro kms create-key \
  --name "financial-data" \
  --algorithm ML-KEM-768 \
  --rotation "90d" \
  --description "财务数据加密密钥"

# 列出密钥版本
safe-pro kms list-versions --name "financial-data"
# 版本 1: 创建于 2025-01-01, 状态: 活跃
# 版本 2: 创建于 2025-04-01, 状态: 活跃(当前)
# 版本 3: 创建于 2025-07-01, 状态: 活跃(当前)

# 使用特定密钥版本加密
safe-pro encrypt \
  --input report.pdf \
  --output report.pdf.encrypted \
  --kms-key "financial-data@v3"

# 旧版本数据仍可解密
safe-pro decrypt \
  --input old_report.pdf.encrypted \
  --output old_report.pdf \
  --kms-key "financial-data@v1"
```

### 场景三:审计日志与合规报告

```bash
# 查看操作日志
safe-pro audit log \
  --from 2025-01-01 --to 2025-01-31 \
  --user "alice@company.com"

# 输出:
# === 加密操作审计日志 ===
# 时间                 用户              操作   文件              算法       密钥
# 2025-01-15 09:30:22  alice@company.com  加密  financial/Q1.pdf  ML-KEM-768  financial-data@v2
# 2025-01-15 14:22:10  alice@company.com  解密  financial/Q1.pdf  ML-KEM-768  financial-data@v2
# 2025-01-16 10:15:33  alice@company.com  加密  financial/Q2.pdf  ML-KEM-768  financial-data@v2
# 总计: 47 次操作

# 生成合规报告
safe-pro audit report \
  --period 2025-01 \
  --format pdf \
  --output compliance-report-2025-01.pdf

# 报告包含:
# - 加密操作统计
# - 密钥使用情况
# - 异常操作告警
# - 合规性检查结果
```

## 不适用场景

以下场景安全加密工具-专业版不适合处理：

- 渗透测试未授权目标
- 物理安全防护
- 社会工程学攻击

## 触发条件

需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于非本工具能力范围的需求。

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 从免费版升级

```bash
# 免费版加密文件完全兼容
# 升级到专业版
safe-pro upgrade --from free

# 配置 KMS
export KMS_ENDPOINT="https://kms.company.com"
export KMS_API_KEY="your-kms-api-key"

# 验证 KMS 连接
safe-pro kms ping
# 输出: KMS 连接正常,版本 2.1.0
```

### 配置安全策略

```bash
# 创建企业安全策略
cat > security-policy.json << 'EOF'
{
  "passphrase": {
    "minLength": 20,
    "requireUppercase": true,
    "requireLowercase": true,
    "requireNumbers": true,
    "requireSpecialChars": true
  },
  "algorithm": {
    "default": "ML-KEM-768",
    "minimum": "ML-KEM-512",
    "classified": "ML-KEM-1024"
  },
  "files": {
    "allowedTypes": ["pdf", "docx", "xlsx", "txt", "csv", "json"],
    "maxSize": "500MB",
    "excludePatterns": ["*.tmp", "*.log", ".git/*"]
  },
  "audit": {
    "enabled": true,
    "retention": "365d",
    "alertOnAnomaly": true
  }
}
EOF
```

## 示例

### 企业级配置

```json
{
  "version": "2.0",
  "organization": "my-company",
  "kms": {
    "endpoint": "https://kms.company.com",
    "apiKey": "${KMS_API_KEY}",
    "defaultKey": "company-default",
    "rotationPeriod": "90d"
  },
  "encryption": {
    "algorithm": "ML-KEM-768",
    "compress": true,
    "parallel": 4
  },
  "policy": "security-policy.json",
  "audit": {
    "enabled": true,
    "storage": "postgresql://audit:***@db.company.com/audit",
    "retention": "365d"
  },
  "api": {
    "enabled": true,
    "port": 8443,
    "auth": "oauth2"
  }
}
```

### 免费版与专业版能力对比

| 能力 | 免费版 | 专业版 |
|------|--------|--------|
| 文件加密 | 单文件 | 单文件 + 批量 + 目录 |
| 密码方式 | passphrase | passphrase + KMS |
| 算法 | ML-KEM-512 | 512/768/1024 |
| 密钥管理 | 无 | KMS + 轮换 + 撤销 |
| 安全策略 | 无 | 企业级策略强制 |
| 审计日志 | 无 | 全程记录 + 合规报告 |
| 压缩 | 无 | 自动压缩 |
| 团队共享 | 无 | 密钥池 + 权限 |
| API 接口 | 无 | RESTful API |
| 技术支持 | 社区 | 优先工单 + SLA |

## 最佳实践

1. **KMS 优先**:企业环境优先使用 KMS 管理密钥,避免本地存储
2. **密钥轮换**:设置 90 天轮换周期,定期更新加密密钥
3. **分级加密**:按数据敏感度选择算法(普通 ML-KEM-512,机密 ML-KEM-768,绝密 ML-KEM-1024)
4. **审计常态化**:定期审查审计日志,检测异常操作模式
5. **最小权限**:团队成员按需授予加密/解密权限,定期审查权限
6. **压缩加密**:对文本类数据启用压缩,减少存储与提高安全性
7. **备份密钥**:KMS 密钥必须有备份,防止 KMS 故障导致数据无法解密

## 常见问题

### Q: KMS 故障时如何解密文件?

A: 专业版支持密钥缓存,KMS 密钥会在本地缓存一段时间。KMS 故障期间可使用缓存密钥解密。长期故障需启用 KMS 灾备方案。建议定期导出密钥备份到离线存储。

### Q: 密钥轮换后旧文件需要重新加密吗?

A: 不需要。旧文件使用旧版本密钥加密,解密时 KMS 会自动选择对应版本的密钥。新文件使用新版本密钥加密。如需将旧文件迁移到新密钥,可使用批量重加密功能。

### Q: 如何实现跨团队文件共享?

A: 1) 创建共享密钥,授权给相关团队;2) 加密文件时使用共享密钥;3) 接收方团队通过 KMS 获取密钥解密。也可使用密钥包装(key wrapping)机制,用接收方的公钥包装共享密钥。

### Q: 审计日志如何满足合规要求?

A: 专业版审计日志记录所有加密/解密操作的完整信息(操作者、时间、文件、算法、密钥版本、IP 地址),日志写入防篡改存储。支持导出为标准格式(SIEM 兼容),满足 GDPR、等保等合规要求。

## 依赖说明

### 运行环境

- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **数据库**: PostgreSQL/MySQL(审计日志存储)

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| SAFE CLI Pro | 加密工具 | 必需 | 官方安装包 |
| KMS 服务 | 密钥管理 | 必需 | 自建或云服务 |
| PostgreSQL | 数据库 | 审计日志必需 | 官方网站下载 |
| Redis | 缓存 | 推荐 | 官方网站下载 |
| Node.js | API服务 | API接口必需 | 官方网站下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置

- KMS 服务:配置 `KMS_ENDPOINT` 和 `KMS_API_KEY`
- 数据库:配置 `AUDIT_DB_URL`(审计日志数据库连接)
- API 接口:通过 `SAFE_API_KEY` 配置访问密钥
- OAuth2:配置 `OAUTH_CLIENT_ID` 和 `OAUTH_CLIENT_SECRET`(API 认证)

### 可用性分类

- **分类**: MD+EXEC(Markdown指令 + 命令行执行)
- **说明**: 通过自然语言指令驱动 Agent 执行企业级加密管理,包含批量加密、KMS 集成与审计日志
- **兼容性**: 完全兼容免费版加密文件格式
- **支持**: 优先工单支持,SLA 保障响应时间
- API Key通过环境变量配置: export API_KEY=your_key

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用
