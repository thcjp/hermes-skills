---

slug: "doc-guard"
name: "doc-guard"
version: 1.0.1
displayName: "文档护盾专业版"
summary: "团队级端到端加密文档协作平台，支持批量操作、版本回滚、权限管理与自定义加密策略。。文档护盾专业版在免费版基础上扩展团队协作、版本管理、自定义加密与批量操作能力。Use when 需要提升效率"
license: "Proprietary"
edition: "pro"
description: |-，可自动提升工作效率
  文档护盾专业版在免费版基础上扩展团队协作、版本管理、自定义加密与批量操作能力。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务.
tags:
  - 集成工具
  - 安全
  - 企业级
  - 团队协作
  - 工具
  - 效率
  - 自动化
  - 知识
  - 文档
  - 加密
  - 写作
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"

---

# 文档护盾专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 文档护盾专业版权限管理 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

## 核心能力

### 错误恢复步骤
| 错误场景 | 原因 | 处理方式 |
|:-----|:-----|:-----|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
### 错误场景

针对错误场景,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供错误场景相关的配置参数、输入数据和处理选项.
**输出**: 返回错误场景的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`错误场景`的配置文档进行参数调优
### LLM响应超时或无响应

针对LLM响应超时或无响应,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供LLM响应超时或无响应相关的配置参数、输入数据和处理选项.
**输出**: 返回LLM响应超时或无响应的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`LLM响应超时或无响应`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 已知限制
- 端到端加密文档创建、读取、更新
- 文档列表与基础搜索
- 单文档删除
- MCP工具协议接入
- 客户端加密、去中心化存储

### 专业版新增能力
| 能力模块 | 输入 | 输出 | 适用场景 |
|---:|---:|---:|---:|
| 批量创建 | 文档数组 | 创建结果列表 | 大规模导入 |
| 批量更新 | 更新数组 | 更新结果列表 | 批量修订 |
| 版本历史 | docId | 版本列表 | 审计与回滚 |
| 版本回滚 | docId + 版本号 | 回滚后文档 | 误操作恢复 |
| 权限管理 | docId + 用户列表 | 权限矩阵 | 团队协作 |
| 共享空间 | 空间名 + 成员 | 空间 docId | 项目级协作 |
| 自定义加密 | 加密策略 | 策略 ID | 合规定制 |
| 密钥轮换 | docId | 新密钥版本 | 安全运维 |
| 模板系统 | 模板定义 | 模板 ID | 重复任务 |
| 审计日志 | 时间范围 | 操作记录 | 合规检查 |

## 适用场景

### 场景一：团队知识库加密管理（团队负责人角色）
团队需要建立内部知识库但担心数据泄露。使用共享空间把文档按项目分组，成员按角色获得读 / 写 / 管理权限，所有内容在客户端加密后才同步到服务端.
### 场景二：合规审计文档归档（合规角色）
法规要求保留 5 年内的所有文档操作记录。专业版提供完整审计日志导出，包括谁在何时对哪个文档做了什么操作，可导出为 CSV 或 JSON 用于合规检查.
### 场景三：跨组织协作的隐私保护（BD 角色与外部合作伙伴）
与外部合作伙伴共享项目文档但又不希望对方看到内部版本。通过权限矩阵设置只读权限，并启用密钥轮换——即使密钥泄露历史版本仍可保护.
### 场景四：大规模文档迁移（运维角色）
从其他笔记平台迁移 10 万份文档到加密存储。专业版提供批量创建 API 与进度跟踪，支持断点续传与失败重试.
### 场景五：密钥轮换与安全运维（安全角色）
安全策略要求每 90 天轮换一次密钥。专业版提供密钥轮换接口，旧密钥加密的历史版本自动迁移，无需用户介入.
### 场景六：文档模板自动化（运营角色）
周报、月报、会议纪要等重复性文档可通过模板自动生成。模板支持变量插值与流水线编排，降低重复劳动.
## 使用流程

### 批量创建文档

```json
{
  "tool": "batch_create_documents",
  "params": {
    "documents": [
      { "title": "周报 W28", "content": "# 周报\n\n## 完成\n..." },
      { "title": "周报 W29", "content": "# 周报\n\n## 完成\n..." },
      { "title": "周报 W30", "content": "# 周报\n\n## 完成\n..." }
    ]
  }
}
```

### 版本回滚

```json
{
  "tool": "rollback_document",
  "params": {
    "docId": "abc123",
    "targetVersion": 3
  }
}
```

### 权限管理

```json
{
  "tool": "set_permissions",
  "params": {
    "docId": "abc123",
    "permissions": [
      { "user": "alice@team.com", "role": "editor" },
      { "user": "bob@team.com", "role": "viewer" }
    ]
  }
}
```

### 密钥轮换

```json
{
  "tool": "rotate_key",
  "params": { "docId": "abc123" }
}
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | doc-guard处理的内容输入 |,  |
| content | string | 否 | doc-guard处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "guard 相关配置参数",
    result: "guard 相关配置参数",
    result: "guard 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|:------|------:|:------|:------|
| 同步长期失败 | 去中心化存储限流 | 调用工具，间隔 60 秒 | 高 |
| 批量创建部分失败 | 单条超过 10MB | 拆分大文档或精简内容 | 高 |
| 权限变更未生效 | 本地缓存未刷新 | 等待 5 分钟或清空本地缓存 | 中 |
| 密钥轮换卡住 | 网络中断 | 查看轮换状态，必要时手动重启 | 中 |
| 审计日志缺失 | 服务未启用日志 | 检查策略 `audit_log: True` | 中 |
| 搜索结果不全 | 索引未同步 | 触发索引重建 | 中 |
| 模板变量未替换 | 语法错误 | 检查 `Doc Guard 核心处理` 拼写与定义 | 低 |
| 批量迁移内存高 | 一次性载入全部 | 改为分批加载 | 低 |

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 与 MCP工具协议的 AI Agent（Claude Code / Cursor / Windsurf / ChatGPT 等）
- **操作系统**：Windows / macOS / Linux
- **浏览器**：现代浏览器（用于查看分享链接与管理后台）
- **Python**：3.9+（批量迁移脚本与自定义加密策略示例需要）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本兼容性 |
|---:|:---|---:|---:|:---|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 | 不限 |
| MCP工具客户端 | 协议适配 | 必需 | Agent 客户端自带 | 协议 2025-03+ |
| 加密文档服务端 | 后端服务 | 必需 | 自建或托管，需提供 `<SERVER_URL>` | v2.0+ |
| 去中心化存储 | 存储层 | 必需 | 内置于服务端，对外透明 | 不限 |
| 企业 KMS（可选） | 密钥管理 | 推荐 | AWS KMS / 阿里云 KMS / 自建 Vault | 兼容 PKCS#11 |
| SIEM（可选） | 审计集成 | 可选 | Splunk / ELK / Datadog | 支持 CEF 或 JSON |
| Python3 | 运行时 | 可选 | 官网下载，迁移脚本依赖 | 3.9+ |

### API Key 配置
- 本 Skill 通过 MCP工具协议接入，无需单独 API Key
- 服务端 `<SERVER_URL>` 由用户自行部署或选择托管方案
- 用户密钥片段由客户端本地生成与保管，不上传服务端
- 企业 KMS 凭据存储于 `d:\skills\.skillhub-credentials\` 目录（已 gitignore）
- 禁止在 SKILL.md 或脚本中硬编码任何密钥或 Token

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过 MCP工具协议与加密文档服务端通信；专业版涉及批量操作与脚本化迁移，建议在支持 Python 执行的环境下使用

## 案例展示

### 自定义加密策略

```python
import os
from pathlib import Path
# ...
# 自定义加密策略配置示例
ENCRYPTION_POLICY = {
    'algorithm': 'AES-256-GCM',          # 加密算法
    'key_derivation': 'PBKDF2-HMAC-SHA512',  # 密钥派生
    'iterations': 210000,                  # 派生迭代次数（建议 >= 210000）
    'key_rotation_days': 90,               # 密钥轮换周期
    'dual_factor': True,                   # 双因素加密
    'audit_log': True,                     # 启用审计日志
}
# ...
# 密钥存储位置（必须本地，不上传）
KEY_STORE_PATH = Path.home() / '.doc-guard' / 'keys'
KEY_STORE_PATH.mkdir(parents=True, exist_ok=True)
# ...
# 审计日志归档目录
AUDIT_LOG_PATH = Path.home() / '.doc-guard' / 'audit'
AUDIT_LOG_PATH.mkdir(parents=True, exist_ok=True)
# ...
print(f"加密策略：{ENCRYPTION_POLICY['algorithm']}")
print(f"密钥轮换周期：{ENCRYPTION_POLICY['key_rotation_days']} 天")
```

### 批量迁移脚本

```python
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
# ...
def migrate_documents(source_docs: list, batch_size: int = 50) -> dict:
    """批量迁移文档到加密存储，支持断点续传。"""
    checkpoint = load_checkpoint()  # 从检查点加载已完成项
    results = {'success': 0, 'failed': [], 'skipped': 0}
# ...
    pending = [d for d in source_docs if d['id'] not in checkpoint]
# ...
    def migrate_one(doc):
        try:
            # 调用 MCP工具的 batch_create_documents
            result = call_mcp_tool('create_document', {
                'title': doc['title'],
                'content': doc['content']
            })
            return {'id': doc['id'], 'status': 'ok', 'docId': result['docId']}
        except Exception as e:
            return {'id': doc['id'], 'status': 'failed', 'error': str(e)}
# ...
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures = {ex.submit(migrate_one, d): d for d in pending}
        for i, fut in enumerate(as_completed(futures), 1):
            r = fut.result()
            if r['status'] == 'ok':
                results['success'] += 1
                checkpoint.add(r['id'])
            else:
                results['failed'].append(r)
            # 每 100 条落盘一次检查点
            if i % 100 == 0:
                save_checkpoint(checkpoint)
    save_checkpoint(checkpoint)
    return results
# ...
def load_checkpoint():
    from pathlib import Path
    p = Path.home() / '.doc-guard' / 'migration.checkpoint'
    if p.exists():
        return set(json.loads(p.read_text()))
    return set()
# ...
def save_checkpoint(checkpoint):
    from pathlib import Path
    p = Path.home() / '.doc-guard' / 'migration.checkpoint'
    p.write_text(json.dumps(list(checkpoint)))
```

## 常见问题

### Q1：团队场景下密钥如何管理？
A：推荐使用密钥托管服务（如 KMS），团队成员通过 SSO 鉴权后从 KMS 获取文档密钥。专业版支持对接企业 KMS，密钥永不离开 KMS 边界.
### Q2：批量迁移中途失败如何续传？
A：检查点文件记录已完成 docId，重启脚本时自动跳过。失败列表会写入 `migration_failed.json`，可针对性重试.
### Q3：版本回滚会丢失当前修改吗？
A：不会。回滚本质是创建一个新版本，内容为目标版本副本。当前最新版本仍保留在历史中，可随时恢复.
### Q4：权限变更后多久生效？
A：实时生效。被收回权限的用户下次访问会返回 403，已建立的本地缓存会在 5 分钟内失效.
### Q5：密钥轮换期间能否访问文档？
A：可以。轮换是后台任务，期间所有访问仍走旧密钥；轮换完成后切换到新密钥，旧密钥保留用于解密历史版本.
### Q6：自定义加密策略与默认有什么区别？
A：默认使用 AES-256-GCM 与 PBKDF2-HMAC-SHA256（10 万次迭代）。专业版可自定义算法、迭代次数（建议 >= 21 万次）、双因素加密、密钥轮换周期等.
### Q7：审计日志能实时流式订阅吗？
A：可以。专业版提供 Webhook 订阅机制，所有操作实时推送到指定端点，适合 SIEM 集成.
### Q8：模板支持哪些变量？
A：支持 `doc-guard_template`、`doc-guard_template`、`doc-guard_template` 等内置变量，也支持自定义变量与条件逻辑（if/else）.
### Q9：共享空间与个人文档有什么区别？
A：个人文档只有所有者可访问；共享空间由空间管理员管理，成员按角色获得不同权限。空间内的文档继承空间权限.
### Q10：如何导出审计日志到 SIEM？
A：调用 `export_audit_log` 工具，参数为时间范围与格式（CSV/JSON/CEF），结果可推送到 Splunk、ELK、Datadog 等主流 SIEM.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 不能替代专业安全审计，仅提供辅助检查能力
- 加密强度依赖正确配置的密钥与算法参数
