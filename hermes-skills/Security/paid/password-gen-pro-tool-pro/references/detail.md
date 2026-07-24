# 详细参考 - password-gen-pro-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

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

        if len(password) < policy["min_length"]:
            violations.append(f"长度不足,最少{policy['min_length']}位")
        if len(password) > policy["max_length"]:
            violations.append(f"长度超限,最多{policy['max_length']}位")

        if policy["require_lower"] and not any(c.islower() for c in password):
            violations.append("缺少小写字母")
        if policy["require_upper"] and not any(c.isupper() for c in password):
            violations.append("缺少大写字母")
        if policy["require_digits"] and not any(c.isdigit() for c in password):
            violations.append("缺少数字")
        if policy["require_symbols"] and not any(c in '!@#$%^&*()-_=+' for c in password):
            violations.append("缺少特殊字符")

        unique = len(set(password))
        if unique < policy["min_unique_chars"]:
            violations.append(f"唯一字符不足,最少{policy['min_unique_chars']}个")

        import re
        if re.search(r'(.)\1{' + str(policy["max_repeats"]) + ',}', password):
            violations.append(f"连续重复字符超过{policy['max_repeats']}个")

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

    print("=== 可用策略 ===")
    for p in manager.list_policies():
        print(f"  {p['id']}: {p['name']} (最少{p['min_length']}位)")

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

## 代码示例 (python)

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

    passwords = gen.generate_batch(100, length=16, exclude_similar=True)

    gen.export_csv(passwords, "batch_passwords.csv")
    gen.export_json(passwords, "batch_passwords.json")

    print(f"生成 {len(passwords)} 个密码")
    print(f"CSV导出: batch_passwords.csv")
    print(f"JSON导出: batch_passwords.json")
    print(f"\n前5个密码:")
    for p in passwords[:5]:
        print(f"  {p['id']:3d}. {p['password']}")
```

## 代码示例 (python)

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

    store.store("example.com", "user1", "MyStr0ngP@ss!", "个人账户")

    entries = store.retrieve("example.com")
    for e in entries:
        print(f"站点: {e['site']}")
        print(f"用户: {e['username']}")
        print(f"密码: {e['password']}")
```

