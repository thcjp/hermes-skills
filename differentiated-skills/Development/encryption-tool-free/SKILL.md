---
slug: encryption-tool-free
name: encryption-tool-free
version: "1.0.0"
displayName: 加密工具基础版
summary: 提供文件加密、密码哈希、算法选择指南与基础安全审计,适合个人开发者保护数据。
license: MIT
edition: free
description: |-
  面向开发者的数据加密辅助工具,涵盖文件加密、密码哈希、加密算法选择与基础代码安全审计。

  核心能力:
  - 文件加密与解密(age/gpg)
  - 密码哈希(bcrypt/argon2)
  - 加密算法选择指南
  - 基础代码安全审计
  - TLS证书检查

  适用场景:
  - 敏感文件加密保护
  - 用户密码安全存储
  - 加密算法选择参考
  - 基础安全代码审查

  差异化:
  - 免费版聚焦常用加密操作,开箱即用
  - 提供算法选择速查表
  - 与专业版命令兼容,可平滑升级

  触发关键词: 加密, 解密, 密码哈希, bcrypt, argon2, AES, TLS, 证书, 文件加密, encrypt, decrypt, hash
tags:
- 开发工具
- 安全
- 加密
tools:
- read
- exec
---

# 加密工具 - 免费版

## 概述

加密工具免费版为开发者提供日常数据加密保护能力。工具涵盖文件加密解密、密码哈希存储、加密算法选择指南和基础代码安全审计,帮助开发者在开发阶段正确使用加密技术保护敏感数据。

本版本适合敏感文件加密保护、用户密码安全存储和基础安全代码审查。所有操作通过命令行工具和代码示例完成。

## 核心能力

### 1. 加密算法选择指南

根据使用场景推荐合适的加密算法。

| 用途 | 推荐算法 | 应避免 |
|:-----|:---------|:-------|
| 密码存储 | argon2id, bcrypt (cost>=12) | MD5, SHA1, 明文SHA256 |
| 对称加密 | AES-256-GCM, ChaCha20-Poly1305 | AES-ECB, DES, RC4 |
| 非对称加密 | RSA-4096+OAEP, Ed25519, P-256 | RSA-1024, PKCS#1 v1.5 |
| 密钥派生 | PBKDF2 (>=600k), scrypt, argon2 | 单次哈希 |
| JWT签名 | RS256, ES256 | HS256(弱密钥) |
| TLS | 1.2+ | TLS 1.0/1.1, SSLv3 |

### 2. 文件加密与解密

使用 age 或 gpg 加密敏感文件。

```bash
# 使用age加密(推荐)
age -p -o file.age file.txt          # 密码加密
age -d -o file.txt file.age          # 解密

# 使用age密钥加密
age-keygen -o key.txt                # 生成密钥
age -r <recipient> -o file.age file.txt  # 公钥加密
age -d -i key.txt -o file.txt file.age   # 私钥解密

# 使用gpg加密
gpg -c --cipher-algo AES256 file.txt   # 对称加密
gpg -d file.txt.gpg > file.txt         # 解密

# 批量加密
for f in *.secret; do
    age -p -o "${f}.age" "$f"
    shred -u "$f"    # 安全删除原文件
done
```

### 3. 密码哈希

安全地存储用户密码。

```python
# Python密码哈希示例
import hashlib
import os
import hmac

# 方法1:使用bcrypt(推荐)
import bcrypt

def hash_password_bcrypt(password: str) -> str:
    """使用bcrypt哈希密码"""
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password_bcrypt(password: str, hashed: str) -> bool:
    """验证bcrypt密码"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# 方法2:使用PBKDF2
def hash_password_pbkdf2(password: str) -> str:
    """使用PBKDF2哈希密码"""
    salt = os.urandom(32)
    iterations = 600000
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)
    return f"pbkdf2${iterations}${salt.hex()}${hashed.hex()}"

def verify_password_pbkdf2(password: str, stored: str) -> bool:
    """验证PBKDF2密码"""
    parts = stored.split('$')
    iterations = int(parts[1])
    salt = bytes.fromhex(parts[2])
    stored_hash = parts[3]
    computed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)
    return hmac.compare_digest(computed.hex(), stored_hash)

# 使用示例
password = "mySecurePassword123"
hashed = hash_password_bcrypt(password)
print(f"哈希值: {hashed}")
print(f"验证: {verify_password_bcrypt(password, hashed)}")
```

```javascript
// Node.js密码哈希示例
const crypto = require('crypto');

// 使用PBKDF2
function hashPassword(password) {
    const salt = crypto.randomBytes(32);
    const iterations = 600000;
    const hashed = crypto.pbkdf2Sync(password, salt, iterations, 64, 'sha512');
    return `pbkdf2$${iterations}$${salt.toString('hex')}$${hashed.toString('hex')}`;
}

function verifyPassword(password, stored) {
    const parts = stored.split('$');
    const iterations = parseInt(parts[1]);
    const salt = Buffer.from(parts[2], 'hex');
    const storedHash = parts[3];
    const computed = crypto.pbkdf2Sync(password, salt, iterations, 64, 'sha512');
    return crypto.timingSafeEqual(
        Buffer.from(storedHash, 'hex'),
        computed
    );
}

// 安全随机数生成
function generateSecureToken(length = 32) {
    return crypto.randomBytes(length).toString('hex');
}
```

### 4. 基础代码安全审计

检查代码中的加密相关安全问题。

```bash
#!/bin/bash
# 基础加密安全审计
echo "=== 加密安全审计 ==="

# 1. 检查弱哈希算法
echo "--- 弱哈希算法检查 ---"
grep -rnE "\b(md5|sha1)\s*\(" . --include="*.js" --include="*.py" --include="*.java" | \
    grep -v "node_modules\|test\|\.min\."

# 2. 检查硬编码密钥
echo -e "\n--- 硬编码密钥检查 ---"
grep -rnE "(secret|key|password|token)\s*=\s*['\"][^'\"]{8,}['\"]" . \
    --include="*.js" --include="*.py" | grep -v "node_modules\|test"

# 3. 检查不安全的随机数
echo -e "\n--- 不安全随机数检查 ---"
grep -rn "Math.random" . --include="*.js" | grep -v "node_modules\|\.min\."
grep -rn "random.random" . --include="*.py" | grep -v "secrets\|test"

# 4. 检查禁用的证书验证
echo -e "\n--- 证书验证检查 ---"
grep -rnE "rejectUnauthorized\s*:\s*false" . --include="*.js"
grep -rn "verify\s*=\s*False" . --include="*.py"

# 5. 检查ECB模式
echo -e "\n--- ECB模式检查 ---"
grep -rn "ECB\|ecb" . --include="*.js" --include="*.py" | grep -v "node_modules"

echo -e "\n=== 审计完成 ==="
```

### 5. TLS证书检查

检查TLS证书配置和有效期。

```bash
# 检查证书信息
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | \
  openssl x509 -noout -subject -issuer -dates

# 检查证书链
openssl s_client -showcerts -connect example.com:443 < /dev/null 2>/dev/null | \
  awk '/BEGIN CERT/,/END CERT/' > chain.pem

# 验证证书
openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt server.pem

# 检查支持的TLS版本
for version in tls1 tls1_1 tls1_2 tls1_3; do
    echo -n "$version: "
    echo | openssl s_client -connect example.com:443 -$version 2>/dev/null | \
      grep -q "Cipher" && echo "支持" || echo "不支持"
done
```

## 使用场景

### 场景一:敏感配置文件加密

加密项目中的敏感配置文件。

```bash
#!/bin/bash
# 敏感配置文件加密
echo "=== 配置文件加密 ==="

# 生成加密密钥
age-keygen -o ~/.config/age/key.txt
RECIPIENT=$(grep -oP 'age1\w+' ~/.config/age/key.txt)
echo "公钥: $RECIPIENT"

# 加密配置文件
for f in .env.production database.yml secrets.json; do
    if [ -f "$f" ]; then
        age -r "$RECIPIENT" -o "${f}.age" "$f"
        echo "已加密: $f -> ${f}.age"
        shred -u "$f"
    fi
done

# 解密配置文件(部署时)
# age -d -i ~/.config/age/key.txt -o .env.production .env.production.age
```

### 场景二:用户密码安全存储

实现安全的用户密码存储方案。

```python
# 用户密码安全存储示例
import bcrypt
import secrets
import hmac

class PasswordManager:
    """安全的密码管理器"""

    @staticmethod
    def hash_password(password: str) -> str:
        """哈希用户密码"""
        # 验证密码强度
        if len(password) < 8:
            raise ValueError("密码长度至少8位")
        
        # 使用bcrypt哈希(cost=12)
        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """验证密码(常量时间比较)"""
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
        except Exception:
            return False

    @staticmethod
    def generate_token(length: int = 32) -> str:
        """生成安全随机令牌"""
        return secrets.token_urlsafe(length)

    @staticmethod
    def generate_api_key() -> str:
        """生成API密钥"""
        return f"sk_{secrets.token_hex(32)}"


# 使用示例
pm = PasswordManager()

# 用户注册
password = "UserSecurePass123!"
hashed = pm.hash_password(password)
print(f"存储哈希: {hashed}")

# 用户登录
input_password = "UserSecurePass123!"
is_valid = pm.verify_password(input_password, hashed)
print(f"密码验证: {'成功' if is_valid else '失败'}")

# 生成API密钥
api_key = pm.generate_api_key()
print(f"API密钥: {api_key}")
```

### 场景三:API数据加密传输

对API传输的敏感数据进行加密。

```javascript
// Node.js API数据加密
const crypto = require('crypto');

class DataEncryptor {
    constructor(key) {
        this.key = Buffer.from(key, 'hex');  // 32字节密钥
        this.algorithm = 'aes-256-gcm';
    }

    encrypt(plaintext) {
        const iv = crypto.randomBytes(12);  // GCM推荐12字节IV
        const cipher = crypto.createCipheriv(this.algorithm, this.key, iv);
        
        let encrypted = cipher.update(plaintext, 'utf8', 'hex');
        encrypted += cipher.final('hex');
        const authTag = cipher.getAuthTag();
        
        return {
            iv: iv.toString('hex'),
            encrypted: encrypted,
            authTag: authTag.toString('hex')
        };
    }

    decrypt(encryptedData) {
        const decipher = crypto.createDecipheriv(
            this.algorithm,
            this.key,
            Buffer.from(encryptedData.iv, 'hex')
        );
        decipher.setAuthTag(Buffer.from(encryptedData.authTag, 'hex'));
        
        let decrypted = decipher.update(encryptedData.encrypted, 'hex', 'utf8');
        decrypted += decipher.final('utf8');
        return decrypted;
    }
}

// 使用示例
const key = crypto.randomBytes(32).toString('hex');
const encryptor = new DataEncryptor(key);

const sensitiveData = '{"ssn":"123-45-6789","credit_card":"4532-1234-5678-9010"}';
const encrypted = encryptor.encrypt(sensitiveData);
console.log('加密数据:', encrypted);

const decrypted = encryptor.decrypt(encrypted);
console.log('解密数据:', decrypted);
```

## 快速开始

### 步骤一:安装工具

```bash
# 安装age(推荐)
# macOS
brew install age
# Linux
sudo apt install age  # Debian/Ubuntu

# 安装gpg(通常已预装)
gpg --version
```

### 步骤二:触发加密操作

在 AI Agent 中输入:

```
请帮我加密 .env.production 文件,并生成加密密钥。
```

### 步骤三:安全存储密钥

Agent 会生成加密密钥并提供安全存储建议。

## 配置示例

### 加密工具配置

```yaml
# .encryption.yml - 加密配置
version: "1.0"

# 文件加密
file_encryption:
  tool: age                    # age 或 gpg
  key_path: ~/.config/age/key.txt
  encrypt_extensions: [.env, .yml, .json, .key]

# 密码哈希
password_hashing:
  algorithm: bcrypt
  cost: 12
  
# 安全审计
audit:
  check_weak_hashes: true
  check_hardcoded_secrets: true
  check_insecure_random: true
  check_cert_validation: true

# TLS检查
tls:
  min_version: "1.2"
  check_cert_expiry: true
  warning_days: 30
```

## 最佳实践

1. **密码只哈希不加密**:密码应该使用单向哈希,不可逆

```python
# 正确:哈希密码
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(12))

# 错误:加密密码(可逆)
# encrypted = cipher.encrypt(password)
```

2. **永远不要重用IV/Nonce**:AES-GCM重复使用Nonce会导致灾难性安全问题

```javascript
// 正确:每次加密生成新IV
const iv = crypto.randomBytes(12);
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);

// 错误:固定IV
// const iv = Buffer.from('fixed-iv-12byt');
```

3. **使用CSPRNG**:安全场景必须使用密码学安全随机数

```python
# 正确
import secrets
token = secrets.token_hex(32)

# 错误
import random
token = ''.join(random.choices('0123456789abcdef', k=64))
```

4. **常量时间比较**:比较敏感数据时使用常量时间比较

```python
import hmac
# 正确
hmac.compare_digest(stored_hash, computed_hash)

# 错误(有时序泄露)
# stored_hash == computed_hash
```

5. **密钥分离**:不同用途使用不同密钥

```yaml
keys:
  encryption: "用于数据加密的密钥"
  signing: "用于签名的密钥"
  backup: "用于备份的密钥"
```

## 常见问题

### Q1:bcrypt和argon2应该选哪个?

| 特性 | bcrypt | argon2 |
|:-----|:-------|:-------|
| 成熟度 | 非常成熟 | 较新 |
| 抗GPU | 一般 | 强 |
| 抗ASIC | 一般 | 强 |
| 内存消耗 | 低 | 可调 |
| 推荐场景 | 通用 | 高安全要求 |

### Q2:如何安全存储加密密钥?

```bash
# 1. 使用环境变量(基础)
export ENCRYPTION_KEY="your-key-here"

# 2. 使用密钥管理服务(推荐)
# AWS KMS / 阿里云KMS / HashiCorp Vault

# 3. 使用age密钥文件
age-keygen -o ~/.config/age/key.txt
chmod 600 ~/.config/age/key.txt
```

### Q3:免费版与专业版有何区别?

| 能力维度 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 密钥管理 | 手动 | KMS/Vault集成 |
| 代码审计 | 基础规则 | 深度审计 |
| 合规检查 | 不支持 | 合规模板 |
| 批量加密 | 单文件 | 批量处理 |
| 密钥轮换 | 手动 | 自动轮换 |
| 报告输出 | 文本 | HTML/JSON |

### Q4:如何检查TLS配置是否安全?

```bash
# 检查TLS版本和密码套件
nmap --script ssl-enum-ciphers -p 443 example.com

# 使用openssl检查
echo | openssl s_client -connect example.com:443 2>/dev/null | \
  grep -E "Protocol|Cipher|Verify"
```

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Bash / Python 3.8+ / Node.js 16+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| age | 加密工具 | 推荐 | github.com/FiloSottile/age |
| gpg | 加密工具 | 可选 | 系统自带或安装 gnupg |
| openssl | TLS工具 | 必需 | 系统自带 |
| Python bcrypt | 库 | 推荐 | pip install bcrypt |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 加密密钥应通过环境变量或密钥管理服务配置:

```bash
# 通过环境变量
export ENCRYPTION_KEY="${ENCRYPTION_KEY}"

# 通过密钥文件
export AGE_KEY_FILE="~/.config/age/key.txt"
```

### 可用性分类

- **分类**:MD+EXEC(纯 Markdown 指令,需要 exec 命令行执行能力)
- **说明**:基于 Markdown 的 AI Skill,通过自然语言指令驱动 Agent 执行加密相关任务
- **适用规模**:单文件到中小型项目
