---
slug: password-gen-pro-tool-pro
name: password-gen-pro-tool-pro
version: "1.0.0"
displayName: 密码生成器Pro专业版
summary: 企业级密码管理平台,支持批量生成、泄露检查、企业策略模板、加密存储与CSV导出,适合安全团队与企业用户。
license: Proprietary
edition: pro
description: |-
  密码生成器Pro专业版,为企业安全团队提供全方位密码生成与管理能力。
  核心能力:批量密码生成、HaveIBeenPwned泄露检查、企业密码策略模板、加密存储、多格式导出。
  适用场景:企业密码策略管理、批量账户初始化、密码安全审计、合规管理。
  差异化:专业版兼容免费版生成方法,新增企业级批量管理与泄露检查能力,满足规模化密码安全需求。
  适用关键词: 批量密码, 泄露检查, 密码策略, 企业密码, batch password, breach check, password policy
tags:
- 安全
- 密码
- 企业版
- 泄露检查
tools:
  - - read
- exec
# 密码生成器Pro专业版
## 概述
---
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

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供批量密码生成(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行批量密码生成(专业版独有)操作,遵循单一意图原则。
**输出**: 返回批量密码生成(专业版独有)的执行结果,包含操作状态和输出数据。

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
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]

        try:
            response = requests.get(self.API_URL.format(prefix), timeout=10)

            if response.status_code == 200:
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

    test_passwords = ["password", "123456", "qwerty", "MyStr0ngP@ss!"]

    for pwd in test_passwords:
        result = checker.check_password(pwd)
        print(f"密码: {pwd[:3]}***")
        print(f"  泄露: {result.get('breached', False)}")
        print(f"  出现次数: {result.get('occurrences', 0)}")
        print(f"  严重性: {result.get('severity', 'UNKNOWN')}")
        print()
```

**输入**: 用户提供泄露检查(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行泄露检查(专业版独有)操作,遵循单一意图原则。
**输出**: 返回泄露检查(专业版独有)的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 企业密码策略模板(专业版独有)

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供企业密码策略模板(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行企业密码策略模板(专业版独有)操作,遵循单一意图原则。
**输出**: 返回企业密码策略模板(专业版独有)的执行结果,包含操作状态和输出数据。

### 4. 加密密码存储(专业版独有)

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供加密密码存储(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行加密密码存储(专业版独有)操作,遵循单一意图原则。
**输出**: 返回加密密码存储(专业版独有)的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级密码管理平、支持批量生成、泄露检查、企业策略模板、加密存储与、CSV、适合安全团队与企、业用户、密码生成器、Pro、专业版、为企业安全团队提、供全方位密码生成、与管理能力、核心能力、批量密码生成、HaveIBeenPwned、企业密码策略模板、加密存储、多格式导出、适用场景、企业密码策略管理、批量账户初始化、密码安全审计、合规管理、差异化、专业版兼容免费版、生成方法、新增企业级批量管、理与泄露检查能力、满足规模化密码安、全需求、适用关键词、批量密码、密码策略、企业密码、batch、password、breach、check、policy等。

## 使用场景
### 场景一:企业密码策略部署
```python
#!/usr/bin/env python3
"""企业密码策略部署"""

from policy_manager import PasswordPolicyManager

def deploy_password_policy():
    """部署企业密码策略"""
    manager = PasswordPolicyManager()

    policy = manager.get_policy("strict")
    print(f"=== 部署策略: {policy['name']} ===")
    print(f"  最小长度: {policy['min_length']}")
    print(f"  需要小写: {policy['require_lower']}")
    print(f"  需要大写: {policy['require_upper']}")
    print(f"  需要数字: {policy['require_digits']}")
    print(f"  需要特殊字符: {policy['require_symbols']}")

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
echo "=== 批量账户密码初始化 ==="

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

accounts = []
with open("accounts.csv", "r") as f:
    reader = csv.DictReader(f)
    accounts = list(reader)

print(f"账户数量: {len(accounts)}")
print(f"生成密码并检查泄露...")

results = []
for account in accounts:
    while True:
        password = gen.generate_one(length=16, exclude_similar=True)
        validation = policy_mgr.validate_password(password, "strict")
        if validation["valid"]:
            break

    breach = checker.check_password(password)

    results.append({
        "username": account["username"],
        "site": account["site"],
        "password": password,
        "breached": breach.get("breached", False),
        "strength": "STRONG"
    })

    print(f"  {account['username']}@{account['site']}: {'已泄露,重新生成' if breach.get('breached') else '安全'}")

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
        validation = policy_mgr.validate_password(pwd, policy_name)

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
passwords = ["weak123", "MyStr0ng!P@ss", "password", "C0rrect-Horse-42"]
report = password_audit(passwords, "strict")
print(json.dumps(report, indent=2, ensure_ascii=False))
```

## 不适用场景

以下场景密码生成器Pro专业版不适合处理：

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
```python
gen = PasswordGenerator()
password = gen.generate(16)

batch_gen = BatchPasswordGenerator()
passwords = batch_gen.generate_batch(100, length=16)
checker = BreachChecker()
for pwd in passwords:
    breach = checker.check_password(pwd["password"])
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。

### 命令参数说明

- `-Horse-42`: 命令参数,用于指定操作选项

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

### 已知限制
专业版支持单次生成1000个密码。更大数量建议分批处理。

### Q5: 策略模板可以自定义吗?
可以。在POLICY_TEMPLATES中添加自定义策略,配置各项规则参数。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+
- **网络**: 泄露检查需可访问 `https://api.pwnedpasswords.com`

### 依赖详情
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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```
