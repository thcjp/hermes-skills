---
slug: "namecheap-dns"
name: "namecheap-dns"
version: 1.1.1
displayName: "Namecheap DNS"
summary: "安全管理Namecheap DNS,拉取/合并/自动备份/原子更新。Manage Namecheap DNS records safely by fetching existing entr"
license: "Proprietary"
description: |-
  Manage Namecheap DNS records safely by fetching existing entries, merging
  changes, auto-backing u。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估.
tags:
  - Operations
  - 工具
  - 效率
  - 自动化
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# Namecheap DNS

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Namecheap DNS安全管理 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

## 核心能力

1. **Ghost record detection** — automatic check for records invisible to API
2. **Auto-backup before changes** — every `add` or `remove` creates a timestamped backup (includes DNS snapshot)
3. **Dry-run mode** — `--dry-run` shows what will change without applying
4. **Diff preview** — see exactly what records will be added/removed
5. **Fetch-first** — always gets current DNS state before changes
6. **Merge logic** — adds to existing records instead of replacing
7. **Rollback** — one command to restore from backup
8. **Safety override** — `--force` flag for when you need to bypass ghost record warnings
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| DNS记录管理 | 域名和记录类型 | DNS记录列表和变更确认 |
| 记录合并 | 现有记录和新记录 | 合并后的DNS配置和差异 |
| 安全更新 | 域名和API凭据 | DNS更新结果和验证状态 |

**不适用于**：非Namecheap域名注册商的DNS管理

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| domain | string | 是 | Namecheap域名 |
| record_type | string | 否 | 记录类型, 可选: A/CNAME/MX/TXT, 默认: 全部 |

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

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### Mailgun Setup

```bash
./namecheap-dns.js add menuhq.ai \
  --txt "mail.menuhq.ai=v=spf1 include:mailgun.org ~all" \
  --txt "smtp._domainkey.mail.menuhq.ai=k=rsa; p=MIGfMA0..." \
  --txt "_dmarc.mail.menuhq.ai=v=DMARC1; p=quarantine;" \
  --cname "email.mail.menuhq.ai=mailgun.org" \
  --mx "mail.menuhq.ai=10 mxa.mailgun.org" \
  --mx "mail.menuhq.ai=20 mxb.mailgun.org" \
  --dry-run
```

Review the diff, then run without `--dry-run` to apply.

## 常见问题

### Q1: 如何开始使用Namecheap DNS？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

This skill has critical limitations due to the Namecheap API's destructive nature. Please review carefully before use:

### ⚠️ The Namecheap API is Destructive

The Namecheap `domains.dns.setHosts` API method **replaces ALL DNS records** for a domain. There is no "add one record" or "update one record" endpoint. Every change requires:

1. Fetch all existing records (`getHosts`)
2. Modify the list
3. Upload the entire list (`setHosts`)

**This skill handles this for you** by always fetching first and merging changes.

### 🔍 Ghost Records: The Hidden Danger

**Problem:** `domains.dns.getHosts` does NOT return all DNS records. Records managed by Namecheap subsystems are invisible to the API:

* **Email Forwarding** — MX, SPF, and DKIM records
* **URL Redirect** — A/CNAME records for domain parking/redirects
* **Third-party integrations** — Records added through Namecheap's dashboard for services

Since `setHosts` **replaces all records**, using the API can silently delete these hidden records.

### 🛡️ How This Skill Protects You

1. **`verify` command** — Compares API records with actual live DNS (via `dig`) and warns about ghost records
2. **Automatic safety check** — Before any `add`, `remove`, or `restore`, the skill checks for ghost records
3. **Refuses to proceed** — If ghost records are detected, the operation is blocked (unless `--force` is used)
4. **Clear warnings** — Shows exactly which records will be lost if you proceed
5. **DNS snapshots in backups** — Captures actual DNS state via `dig`, not just API state

### When to Use `--force`

Only use the `--force` flag when:

* You've manually verified the ghost records are no longer needed
* You're intentionally removing email forwarding or URL redirects
* You understand and accept that those records will be deleted

**Never use `--force` blindly.** Always run `verify` first to see what will be lost.

### Example: The Production Incident

This skill was created after adding Mailgun DNS records via the API wiped out Namecheap's email forwarding records. The email forwarding MX/SPF/TXT records were invisible to `getHosts`, so the fetch-merge-write pattern deleted them.

Now, the skill would have:

1. Detected the ghost records during `verify`
2. Refused to proceed without `--force`
3. Shown exactly which email forwarding records would be deleted
4. Created a backup including the DNS snapshot
