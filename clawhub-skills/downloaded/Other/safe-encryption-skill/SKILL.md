---
slug: safe-encryption-skill
name: safe-encryption-skill
version: "0.1.0"
displayName: Safe Encryption
summary: "使用SAFE CLI加密解密管理密钥,后量子密码学,现代GPG替代方案,提升加密安全性"
  with post-quantum ...
license: MIT
description: |-
  Encrypt, decrypt, and manage keys with the SAFE CLI — a modern GPG alternative
  with post-quantum 。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
# Safe Encryption
pricing_tier: "L1-入门级"
pricing_model: "per_use"
suggested_price: 9.9
---

SAFE is a modern encryption CLI with post-quantum support, multi-recipient encryption, and composable authentication.

## Behavior Guidelines
> 已移至 `references/detail.md`

### Installation Debugging
> 已移至 `references/detail.md`

## Quick Reference
> 已移至 `references/detail.md`

### Key Storage Convention
> 已移至 `references/detail.md`

### Generate Keys
> 已移至 `references/detail.md`

### Manage Keys
> 已移至 `references/detail.md`

### Encrypt
> 已移至 `references/detail.md`

### Decrypt
> 已移至 `references/detail.md`

### Info
> 已移至 `references/detail.md`

### Piping (stdin/stdout)
> 已移至 `references/detail.md`

## 适用场景

### Protect API Keys / .env Files
> 已移至 `references/detail.md`

### Share Secrets with a Teammate
> 已移至 `references/detail.md`

### Encrypt Backup Before Cloud Upload
> 已移至 `references/detail.md`

### Encrypt Entire Directories
> 已移至 `references/detail.md`

### Git-Friendly Encrypted Secrets
> 已移至 `references/detail.md`

### Separation of Duties (Two People Required)
> 已移至 `references/detail.md`

### Two-Factor Encryption (Password + Key)
> 已移至 `references/detail.md`

### Team Encryption + Emergency Backup
> 已移至 `references/detail.md`

### Post-Quantum Hybrid Protection
> 已移至 `references/detail.md`

### Temporary Decryption (No File on Disk)
> 已移至 `references/detail.md`

### Password Rotation
> 已移至 `references/detail.md`

### Key Rotation (Compromised Key)
> 已移至 `references/detail.md`

## Composable Paths (AND vs OR Logic)
> 已移至 `references/detail.md`

## Editing Encrypted Files
> 已移至 `references/detail.md`

### Data Input Options
> 已移至 `references/detail.md`

### Read Bytes at Offset
> 已移至 `references/detail.md`

### Write Bytes at Offset (In-Place Edit)
> 已移至 `references/detail.md`

### Append Data
> 已移至 `references/detail.md`

### In-Place Editing Workflow
> 已移至 `references/detail.md`

## Managing Recipients (UNLOCK Blocks)
> 已移至 `references/detail.md`

## Algorithm Options
> 已移至 `references/detail.md`

### AEAD (Content Encryption)
> 已移至 `references/detail.md`

### Key Types
> 已移至 `references/detail.md`

### Key ID Modes
> 已移至 `references/detail.md`

### Password KDF
> 已移至 `references/detail.md`

### Key Hash Algorithm
> 已移至 `references/detail.md`

## Migration from GPG/PGP
> 已移至 `references/detail.md`

## Edge Cases & Tips
> 已移至 `references/detail.md`

## Troubleshooting
> 已移至 `references/detail.md`

## Security Notes
> 已移至 `references/detail.md`

### Password Security
> 已移至 `references/detail.md`

## Agent-to-Agent Encrypted Communication
> 已移至 `references/detail.md`

### First-Run Setup
> 已移至 `references/detail.md`

### Exchanging Keys Between Agents
> 已移至 `references/detail.md`

### Convention: Reply-To Keys
> 已移至 `references/detail.md`

### Workflow: Send a Message
> 已移至 `references/detail.md`

### Checking if a Message is For You
> 已移至 `references/detail.md`

### Workflow: Receive and Reply
> 已移至 `references/detail.md`

### Publishing Your Public Key
> 已移至 `references/detail.md`

### Handling Multiple Identities
> 已移至 `references/detail.md`

### Error Handling
> 已移至 `references/detail.md`

### Checking All Identities
> 已移至 `references/detail.md`

### Sharing via Pastebin
> 已移至 `references/detail.md`

### Posting a Public Message (Forum/Mailing List)
> 已移至 `references/detail.md`

## 依赖说明

### 运行环境
> 已移至 `references/detail.md`

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
> 已移至 `references/detail.md`

### 可用性分类
> 已移至 `references/detail.md`

## 核心能力
- Encrypt, decrypt, and manage keys with the SAFE CLI — a modern GPG alternative
  with post-quantum
- 触发关键词: safe, decrypt, encrypt, manage, keys, encryption, skill

## 使用流程
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例
> 已移至 `references/detail.md`

### 示例1：基础用法
> 已移至 `references/detail.md`

## 常见问题
> 已移至 `references/detail.md`

### Q1: 如何开始使用Safe Encryption？
> 已移至 `references/detail.md`

### Q2: 遇到错误怎么办？
> 已移至 `references/detail.md`

### Q3: Safe Encryption有什么限制？
> 已移至 `references/detail.md`

## 已知限制
- 需要API Key，无Key环境无法使用

## 常见问题与故障排查

### FAQ

**Q1: 如何为Safe Encryption生成一个新的密钥对？**
A1: 使用以下命令生成新的密钥对：
```bash
safe generate-key
```
这将创建一个公钥和私钥文件，通常分别存储在`~/.safe/keys/public.key`和`~/.safe/keys/private.key`。

**Q2: 我如何加密一个文件，以便只有特定的团队成员可以解密？**
A2: 使用以下命令加密文件，并指定团队成员的公钥：
```bash
safe encrypt --recipient user@example.com file.txt
```
确保你有团队成员的公钥，否则他们无法解密文件。

**Q3: 如何在加密和解密过程中使用密码？**
A3: 使用以下命令加密文件，并要求输入密码：
```bash
safe encrypt --password prompt file.txt
```
解密时，系统会提示你输入相同的密码。

**Q4: 如果我丢失了私钥，怎么办？**
A4: 如果你丢失了私钥，将无法解密任何使用该私钥加密的数据。确保定期备份你的私钥。如果真的丢失，你可能需要重新生成密钥对并通知所有相关团队成员。

**Q5: 如何在Safe Encryption中使用后量子密码学算法？**
A5: Safe Encryption默认使用后量子密码学算法。要查看可用算法，使用以下命令：
```bash
safe list-algorithms
```
选择合适的后量子算法，然后在加密或解密时指定它。

### 故障排查指南

**故障1: 加密文件时出现错误 "Recipient key is not valid"**
- 步骤1: 检查是否有团队成员的公钥，并确保它是正确的。
- 步骤2: 使用`safe list-recipient-keys`验证公钥列表。

**故障2: 解密文件时提示 "Password is incorrect"**
- 步骤1: 确认你输入的密码与加密时使用的密码完全一致。
- 步骤2: 如果仍然无法解密，尝试重新加密文件，并确保在提示时输入正确的密码。

**故障3: 加密或解密操作非常慢**
- 步骤1: 检查你的系统资源，如CPU和内存，确保它们没有被其他应用程序过度占用。
- 步骤2: 尝试使用不同的后量子密码学算法，有些算法可能比其他算法更快。

### 最佳实践

1. 定期备份你的密钥对，以防丢失。
2. 使用强密码保护你的密钥，并定期更换密码。
3. 使用安全的存储方法来存储你的私钥，如硬件安全模块(HSM)。
4. 在共享敏感信息时，始终使用加密，即使信息看起来不敏感。
5. 确保所有团队成员都了解如何安全地使用Safe Encryption。

