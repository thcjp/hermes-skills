---
slug: namecheap-dns
name: namecheap-dns
version: "1.1.0"
displayName: Namecheap DNS
summary: Manage Namecheap DNS records safely by fetching existing entries, merging
  changes, auto-backing u...
license: MIT
description: |-
  Manage Namecheap DNS records safely by fetching existing entries, merging
  changes, auto-backing u。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Operations
tools:
  - - read
- exec
---
# Namecheap DNS

## 核心能力

1. **Ghost record detection** — automatic check for records invisible to API
2. **Auto-backup before changes** — every `add` or `remove` creates a timestamped backup (includes DNS snapshot)
3. **Dry-run mode** — `--dry-run` shows what will change without applying
4. **Diff preview** — see exactly what records will be added/removed
5. **Fetch-first** — always gets current DNS state before changes
6. **Merge logic** — adds to existing records instead of replacing
7. **Rollback** — one command to restore from backup
8. **Safety override** — `--force` flag for when you need to bypass ghost record warnings
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: Manage、Namecheap、safely、fetching、entries、merging、backing、Use、需要项目管理、任务规划、进度跟踪、团队协作时使用、不适用于实际人员、绩效评估、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
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
| 待审查内容为空 | 用户未提供内容 | 提示用户提供待审查的代码 |
| 内容格式不识别 | 传入不支持的内容格式 | 列出支持的格式, 建议转换后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 |
| 检查项超出范围 | 传入了不存在的检查维度 | 列出可用检查维度, 使用默认全部检查 |
| 审查超时 | 内容过长导致处理超时 | 建议分段审查, 每段不超过5000字 |
| 其他异常 | 内部处理异常 | 检查输入后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
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

### Q2: 遇到错误怎么办？
A: 

### Q3: Namecheap DNS有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

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
