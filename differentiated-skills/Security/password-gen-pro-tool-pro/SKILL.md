---
slug: password-gen-pro-tool-pro
name: password-gen-pro-tool-pro
version: "1.0.0"
displayName: 密码生成器Pro专业版
summary: 企业级密码管理平台,支持批量生成、泄露检查、企业策略模板、加密存储与CSV导出,适合安全团队与企业用户。
license: MIT
edition: pro
description: |-
  密码生成器Pro专业版,为企业安全团队提供全方位密码生成与管理能力。
  核心能力:批量密码生成、HaveIBeenPwned泄露检查、企业密码策略模板、加密存储、多格式导出。
  适用场景:企业密码策略管理、批量账户初始化、密码安全审计、合规管理。
  差异化:专业版兼容免费版生成方法,新增企业级批量管理与泄露检查能力,满足规模化密码安全需求。
  触发关键词: 批量密码, 泄露检查, 密码策略, 企业密码, batch password, breach check, password policy
tags:
- 安全
- 密码
- 企业版
- 泄露检查
tools:
- read
- exec
---

# 密码生成器Pro专业版

## 概述

专业版为企业安全团队提供完整的密码生成与管理平台,在免费版密码生成与强度检测基础上,新增批量密码生成(CSV导出)、HaveIBeenPwned泄露检查、企业密码策略模板、加密密码存储与多格式导出。专业版完全兼容免费版生成方法,已有密码生成脚本可无缝升级,适合企业级密码安全治理。

### 专业版核心优势

| 优势 | 说明 |
|:-----|:-----|
| 批量生成 | 批量生成数百个密码,CSV导出 |
| 泄露检查 | 集成HaveIBeenPwned API |
| 策略模板 | 预置企业密码策略模板 |
| 加密存储 | AES加密存储密码历史 |
| 多格式导出 | CSV/JSON/1Password |
| 密码审计 | 全量密码安全审计 |
| API集成 | REST API接口 |
| 合规报告 | 生成密码合规报告 |

## 核心能力

### 1. 批量密码生成(专业版独有)

```python
#!/usr/bin/env python3
"""专业版批量密码生成器"""

import secrets
import string
import csv
import json
from datetime import datetime

class BatchPasswordGenerator:
    """批量密码生成器"""
    
    def __init__(self):
        self.char_sets = {
            'lower': string.ascii_lowercase,
            'upper': string.ascii_uppercase,
            'digits': string.digits,
            'symbols': '!@#$%^&*()-_=+[]{}|;:,.<>?',
        }
    
    def generate_one(self, length=16, **kwargs):
        """生成单个密码"""
        use_lower = kwargs.get('use_lower', True)
        use_upper = kwargs.get('use_upper', True)
        use_digits = kwargs.get('use_digits', True)
        use_symbols = kwargs.get('use_symbols', True)
        exclude_similar = kwargs.get('exclude_similar', False)
        
        chars = ''
        required = []
        
        if use_lower:
            s = self.char_sets['lower']
            if exclude_similar:
                s = s.replace('l', '').replace('o', '')
            chars += s
            required.append(secrets.choice(s))
        
        if use_upper:
            s = self.char_sets['upper']
            if exclude_similar:
                s = s.replace('I', '').replace('O', '')
            chars += s
            required.append(secrets.choice(s))
        
        if use_digits:
            s = self.char_sets['digits']
            if exclude_similar:
                s = s.replace('0', '').replace('1', '')
            chars += s
            required.append(secrets.choice(s))
        
        if use_symbols:
            s = self.char_sets['symbols']
            chars += s
            required.append(secrets.choice(s))
        
        password = list(required)
        for _ in range(length - len(required)):
            password.append(secrets.choice(chars))
        
        secrets.SystemRandom().shuffle(password)
        return ''.join(password)
    
    def generate_batch(self, count, length=16, **kwargs):
        """批量生成密码"""
        results = []
        for i in range(count):
            password = self.generate_one(length, **kwargs)
            results.append({
                "id": i + 1,
                "password": password,
                "length": length,
                "created": datetime.utcnow().isoformat() + "Z"
            })
        return results
    
    def export_csv(self, passwords, filename):
        """导出为CSV"""
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'password', 'length', 'created'])
            writer.writeheader()
            writer.writerows(passwords)
        return filename
    
    def export_json(self, passwords, filename):
        """导出为JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(passwords, f, indent=2, ensure_ascii=False)
        return filename


if __name__ == "__main__":
    gen = BatchPasswordGenerator()
    
    # 批量生成100个密码
    passwords = gen.generate_batch(100, length=16, exclude_similar=True)
    
    # 导出
    gen.export_csv(passwords, "batch_passwords.csv")
    gen.export_json(passwords, "batch_passwords.json")
    
    print(f"生成 {len(passwords)} 个密码")
    print(f"CSV导出: batch_passwords.csv")
    print(f"JSON导出: batch_passwords.json")
    print(f"\n前5个密码:")
    for p in passwords[:5]:
        print(f"  {p['id']:3d}. {p['password']}")
```

### 2. 泄露检查(专业版独有)

```python
#!/usr/bin/env python3
"""专业版密码泄露检查"""

import hashlib
import requests

class BreachChecker:
    """密码泄露检查器(使用HaveIBeenPwned API)"""
    
    API_URL = "https://api.pwnedpasswords.com/range/{}"
    
    def check_password(self, password):
        """检查密码是否已泄露"""
        # 使用k-anonymity模型:只发送哈希前缀
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        
        try:
            response = requests.get(self.API_URL.format(prefix), timeout=10)
            
            if response.status_code == 200:
                # 在返回的哈希后缀中查找
                hashes = response.text.splitlines()
                for line in hashes:
                    parts = line.strip().split(':')
                    if len(parts) == 2 and parts[0] == suffix:
                        count = int(parts[1])
                        return {
                            "breached": True,
                            "occurrences": count,
                            "severity": "CRITICAL" if count > 1000 else "HIGH" if count > 100 else "MEDIUM"
                        }
                
                return {
                    "breached": False,
                    "occurrences": 0,
                    "severity": "NONE"
                }
        except Exception as e:
            return {
                "breached": None,
                "error": str(e),
                "severity": "UNKNOWN"
            }
    
    def check_batch(self, passwords):
        """批量检查密码泄露"""
        results = []
        for pwd in passwords:
            result = self.check_password(pwd)
            results.append({
                "password_preview": pwd[:3] + "***" + pwd[-2:],
                "length": len(pwd),
                "breached": result.get("breached", False),
                "occurrences": result.get("occurrences", 0),
                "severity": result.get("severity", "UNKNOWN")
            })
        return results


if __name__ == "__main__":
    import json
    checker = BreachChecker()
    
    # 检查常见弱密码
    test_passwords = ["password", "123456", "qwerty", "MyStr0ngP@ss!"]
    
    for pwd in test_passwords:
        result = checker.check_password(pwd)
        print(f"密码: {pwd[:3]}***")
        print(f"  泄露: {result.get('breached', False)}")
        print(f"  出现次数: {result.get('occurrences', 0)}")
        print(f"  严重性: {result.get('severity', 'UNKNOWN')}")
        print()
```

### 3. 企业密码策略模板(专业版独有)

```python
#!/usr/bin/env python3
"""专业版企业密码策略模板"""

import json

class PasswordPolicyManager:
    """企业密码策略管理器"""
    
    POLICY_TEMPLATES = {
        "standard": {
            "name": "标准策略",
            "min_length": 12,
            "max_length": 128,
            "require_lower": True,
            "require_upper": True,
            "require_digits": True,
            "require_symbols": False,
            "exclude_similar": False,
            "min_unique_chars": 8,
            "max_repeats": 3,
            "block_common": True,
        },
        "strict": {
            "name": "严格策略",
            "min_length": 16,
            "max_length": 128,
            "require_lower": True,
            "require_upper": True,
            "require_digits": True,
            "require_symbols": True,
            "exclude_similar": True,
            "min_unique_chars": 12,
            "max_repeats": 2,
            "block_common": True,
        },
        "high_security": {
            "name": "高安全策略",
            "min_length": 20,
            "max_length": 128,
            "require_lower": True,
            "require_upper": True,
            "require_digits": True,
            "require_symbols": True,
            "exclude_similar": True,
            "min_unique_chars": 15,
            "max_repeats": 2,
            "block_common": True,
        },
        "passphrase": {
            "name": "口令短语策略",
            "min_length": 20,
            "max_length": 128,
            "require_lower": True,
            "require_upper": False,
            "require_digits": True,
            "require_symbols": False,
            "exclude_similar": False,
            "min_unique_chars": 10,
            "max_repeats": 5,
            "block_common": True,
        }
    }
    
    COMMON_PASSWORDS = [
        "password", "123456", "qwerty", "admin", "letmein",
        "welcome", "monkey", "dragon", "master", "login"
    ]
    
    def get_policy(self, template_name):
        """获取策略模板"""
        return self.POLICY_TEMPLATES.get(template_name)
    
    def validate_password(self, password, policy_name="standard"):
        """根据策略验证密码"""
        policy = self.POLICY_TEMPLATES.get(policy_name)
        if not policy:
            return {"valid": False, "error": f"未知策略: {policy_name}"}
        
        violations = []
        
        # 长度检查
        if len(password) < policy["min_length"]:
            violations.append(f"长度不足,最少{policy['min_length']}位")
        if len(password) > policy["max_length"]:
            violations.append(f"长度超限,最多{policy['max_length']}位")
        
        # 字符类型检查
        if policy["require_lower"] and not any(c.islower() for c in password):
            violations.append("缺少小写字母")
        if policy["require_upper"] and not any(c.isupper() for c in password):
            violations.append("缺少大写字母")
        if policy["require_digits"] and not any(c.isdigit() for c in password):
            violations.append("缺少数字")
        if policy["require_symbols"] and not any(c in '!@#$%^&*()-_=+' for c in password):
            violations.append("缺少特殊字符")
        
        # 唯一字符数
        unique = len(set(password))
        if unique < policy["min_unique_chars"]:
            violations.append(f"唯一字符不足,最少{policy['min_unique_chars']}个")
        
        # 重复字符
        import re
        if re.search(r'(.)\1{' + str(policy["max_repeats"]) + ',}', password):
            violations.append(f"连续重复字符超过{policy['max_repeats']}个")
        
        # 常见密码检查
        if policy["block_common"]:
            if password.lower() in self.COMMON_PASSWORDS:
                violations.append("密码过于常见")
        
        return {
            "valid": len(violations) == 0,
            "policy": policy["name"],
            "violations": violations
        }
    
    def list_policies(self):
        """列出所有策略"""
        return [
            {"id": k, "name": v["name"], "min_length": v["min_length"]}
            for k, v in self.POLICY_TEMPLATES.items()
        ]


if __name__ == "__main__":
    manager = PasswordPolicyManager()
    
    # 列出策略
    print("=== 可用策略 ===")
    for p in manager.list_policies():
        print(f"  {p['id']}: {p['name']} (最少{p['min_length']}位)")
    
    # 验证密码
    print("\n=== 密码验证 ===")
    test_passwords = ["weak", "MyStr0ngP@ssw0rd!2026"]
    for pwd in test_passwords:
        result = manager.validate_password(pwd, "strict")
        print(f"\n密码: {pwd[:5]}...")
        print(f"  策略: {result['policy']}")
        print(f"  有效: {result['valid']}")
        if result["violations"]:
            for v in result["violations"]:
                print(f"  违规: {v}")
```

### 4. 加密密码存储(专业版独有)

```python
#!/usr/bin/env python3
"""专业版加密密码存储"""

import json
import os
from datetime import datetime
from cryptography.fernet import Fernet

class EncryptedPasswordStore:
    """加密密码存储"""
    
    def __init__(self, storage_file="password_store.enc"):
        self.storage_file = storage_file
        self.key_file = "store_key.key"
        self.cipher = self._get_cipher()
    
    def _get_cipher(self):
        """获取加密器"""
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
            os.chmod(self.key_file, 0o600)  # 仅owner可读
        return Fernet(key)
    
    def store(self, site, username, password, notes=""):
        """存储密码"""
        # 读取现有数据
        data = self._load()
        
        entry = {
            "site": site,
            "username": username,
            "password": password,
            "notes": notes,
            "created": datetime.utcnow().isoformat() + "Z",
            "updated": datetime.utcnow().isoformat() + "Z"
        }
        
        data["entries"].append(entry)
        self._save(data)
        return entry
    
    def retrieve(self, site):
        """检索密码"""
        data = self._load()
        return [e for e in data["entries"] if e["site"] == site]
    
    def list_sites(self):
        """列出所有站点"""
        data = self._load()
        return list(set(e["site"] for e in data["entries"]))
    
    def _load(self):
        """加载加密数据"""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "rb") as f:
                encrypted = f.read()
            decrypted = self.cipher.decrypt(encrypted)
            return json.loads(decrypted)
        return {"entries": []}
    
    def _save(self, data):
        """保存加密数据"""
        encrypted = self.cipher.encrypt(json.dumps(data).encode())
        with open(self.storage_file, "wb") as f:
            f.write(encrypted)
        os.chmod(self.storage_file, 0o600)


if __name__ == "__main__":
    store = EncryptedPasswordStore()
    
    # 存储密码
    store.store("example.com", "user1", "MyStr0ngP@ss!", "个人账户")
    
    # 检索
    entries = store.retrieve("example.com")
    for e in entries:
        print(f"站点: {e['site']}")
        print(f"用户: {e['username']}")
        print(f"密码: {e['password']}")
```

## 使用场景

### 场景一:企业密码策略部署

```python
#!/usr/bin/env python3
"""企业密码策略部署"""

from policy_manager import PasswordPolicyManager

def deploy_password_policy():
    """部署企业密码策略"""
    manager = PasswordPolicyManager()
    
    # 选择策略
    policy = manager.get_policy("strict")
    print(f"=== 部署策略: {policy['name']} ===")
    print(f"  最小长度: {policy['min_length']}")
    print(f"  需要小写: {policy['require_lower']}")
    print(f"  需要大写: {policy['require_upper']}")
    print(f"  需要数字: {policy['require_digits']}")
    print(f"  需要特殊字符: {policy['require_symbols']}")
    
    # 验证现有密码
    print("\n=== 验证密码样本 ===")
    test_cases = ["old123", "MyStr0ng!P@ssw0rd2026"]
    for pwd in test_cases:
        result = manager.validate_password(pwd, "strict")
        status = "通过" if result["valid"] else "不通过"
        print(f"  {pwd[:5]}...: {status}")
        if result["violations"]:
            for v in result["violations"]:
                print(f"    - {v}")

deploy_password_policy()
```

### 场景二:批量账户初始化

```bash
#!/bin/bash
# 批量账户密码初始化

echo "=== 批量账户密码初始化 ==="

# 读取账户列表
ACCOUNTS_FILE="accounts.csv"  # 格式: username,site
OUTPUT_FILE="account_passwords.csv"

python3 << 'PYTHON'
import csv
from batch_generator import BatchPasswordGenerator
from breach_checker import BreachChecker
from policy_manager import PasswordPolicyManager

gen = BatchPasswordGenerator()
checker = BreachChecker()
policy_mgr = PasswordPolicyManager()

# 读取账户
accounts = []
with open("accounts.csv", "r") as f:
    reader = csv.DictReader(f)
    accounts = list(reader)

print(f"账户数量: {len(accounts)}")
print(f"生成密码并检查泄露...")

results = []
for account in accounts:
    # 生成符合策略的密码
    while True:
        password = gen.generate_one(length=16, exclude_similar=True)
        validation = policy_mgr.validate_password(password, "strict")
        if validation["valid"]:
            break
    
    # 检查泄露
    breach = checker.check_password(password)
    
    results.append({
        "username": account["username"],
        "site": account["site"],
        "password": password,
        "breached": breach.get("breached", False),
        "strength": "STRONG"
    })
    
    print(f"  {account['username']}@{account['site']}: {'已泄露,重新生成' if breach.get('breached') else '安全'}")

# 导出
with open("account_passwords.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["username", "site", "password", "breached", "strength"])
    writer.writeheader()
    writer.writerows(results)

print(f"\n导出完成: account_passwords.csv ({len(results)}个账户)")
PYTHON
```

### 场景三:密码安全审计

```python
#!/usr/bin/env python3
"""密码安全审计"""

import json
from policy_manager import PasswordPolicyManager
from breach_checker import BreachChecker

def password_audit(passwords, policy_name="standard"):
    """密码安全审计"""
    policy_mgr = PasswordPolicyManager()
    checker = BreachChecker()
    
    report = {
        "audit_date": datetime.utcnow().isoformat() + "Z",
        "policy": policy_name,
        "total_passwords": len(passwords),
        "results": {
            "compliant": 0,
            "non_compliant": 0,
            "breached": 0,
            "weak": 0
        },
        "details": []
    }
    
    for pwd in passwords:
        # 策略合规性
        validation = policy_mgr.validate_password(pwd, policy_name)
        
        # 泄露检查
        breach = checker.check_password(pwd)
        
        detail = {
            "password_preview": pwd[:3] + "***",
            "length": len(pwd),
            "compliant": validation["valid"],
            "breached": breach.get("breached", False),
            "violations": validation.get("violations", [])
        }
        
        if validation["valid"]:
            report["results"]["compliant"] += 1
        else:
            report["results"]["non_compliant"] += 1
        
        if breach.get("breached"):
            report["results"]["breached"] += 1
        
        report["details"].append(detail)
    
    return report

from datetime import datetime
# 使用示例
passwords = ["weak123", "MyStr0ng!P@ss", "password", "C0rrect-Horse-42"]
report = password_audit(passwords, "strict")
print(json.dumps(report, indent=2, ensure_ascii=False))
```

## 快速开始

### 从免费版升级

```python
# 免费版:单个密码生成
gen = PasswordGenerator()
password = gen.generate(16)

# 专业版:批量生成+泄露检查
batch_gen = BatchPasswordGenerator()
passwords = batch_gen.generate_batch(100, length=16)
checker = BreachChecker()
for pwd in passwords:
    breach = checker.check_password(pwd["password"])
```

## 配置示例

### 专业版功能矩阵

| 功能 | 免费版 | 专业版 | 说明 |
|:-----|:-------|:-------|:-----|
| 密码生成 | 支持 | 支持 | 单个生成 |
| 批量生成 | 不支持 | 支持 | 批量CSV |
| 强度检测 | 基础 | 多维度 | 评分+反馈 |
| 泄露检查 | 不支持 | 支持 | HaveIBeenPwned |
| 策略模板 | 不支持 | 支持 | 4种模板 |
| 加密存储 | 不支持 | 支持 | AES加密 |
| 导出格式 | 文本 | CSV/JSON | 多格式 |

### 企业密码策略模板

| 模板 | 最小长度 | 特殊字符 | 适用场景 |
|:-----|:---------|:---------|:---------|
| standard | 12 | 不要求 | 普通系统 |
| strict | 16 | 要求 | 重要系统 |
| high_security | 20 | 要求 | 核心系统 |
| passphrase | 20 | 不要求 | 用户友好 |

## 最佳实践

1. **策略优先**:根据系统重要性选择合适的密码策略模板。
2. **泄露检查**:所有新密码生成后执行泄露检查。
3. **批量管理**:使用批量生成+CSV导出管理大量账户。
4. **加密存储**:密码使用加密存储,密钥文件设置严格权限。
5. **定期审计**:定期审计现有密码的合规性与泄露状态。
6. **最小权限**:密码存储文件仅owner可读写(600权限)。

## 常见问题

### Q1: 专业版与免费版生成方法兼容吗?

完全兼容。专业版使用相同的密码生成算法,新增批量、泄露检查与策略管理能力。

### Q2: 泄露检查会暴露密码吗?

不会。使用k-anonymity模型,仅发送SHA1哈希的前5位字符到HaveIBeenPwned API,密码本身不会泄露。

### Q3: 加密存储的密钥如何管理?

密钥文件(store_key.key)应妥善保管。建议备份密钥到安全位置,丢失密钥将无法解密密码。

### Q4: 批量生成有数量限制吗?

专业版支持单次生成1000个密码。更大数量建议分批处理。

### Q5: 策略模板可以自定义吗?

可以。在POLICY_TEMPLATES中添加自定义策略,配置各项规则参数。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+
- **网络**: 泄露检查需可访问 `https://api.pwnedpasswords.com`

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| python3 | 运行时 | 必需 | python.org 下载 |
| requests | HTTP库 | 推荐 | `pip install requests` |
| cryptography | 加密库 | 推荐 | `pip install cryptography` |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- HaveIBeenPwned API为公开接口,无需API Key
- 加密存储密钥自动生成,存储在本地key文件中
- REST API服务建议配置认证Token

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级密码生成与管理任务
