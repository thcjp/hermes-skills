---
slug: "feishu-file-sender"
name: "feishu-file-sender"
version: "1.0.0"
displayName: "飞书文件发送专业版"
summary: "企业级文件批量分发与稳定投递，支持审计与重试机制"
license: "Proprietary"
edition: "pro"
description: |-
  飞书文件发送专业版面向企业用户与高效能个人用户。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - 沟通协作
  - 飞书
  - 文件发送
  - 企业效率
  - 批量操作
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
---
# 飞书文件发送专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |
| 消息频控与智能排队 | 不支持 | 支持 |

## 核心能力

### 批量分发引擎
- **多接收者发送**: 一次性向多个用户与群组分发文件
- **收件人列表**: 支持 CSV/JSON 收件人列表
- **个性化文件名**: 每个接收者可指定不同文件名
- **速率控制**: 可配置发送速率与并发
- **失败重试**: 自动重试失败的发送

**输出**: 返回批量分发引擎的处理结果,包含执行状态码、结果数据和执行日志。
### 多文件管理
- **批量上传**: 一次上传多个文件
- **文件打包**: 多文件打包为 ZIP 发送
- **文件版本**: 文件版本管理与历史记录
- **文件过期**: 自动清理过期文件

**输入**: 用户提供多文件管理所需的指令和必要参数。
**输出**: 返回多文件管理的处理结果,包含执行状态码、结果数据和执行日志。### 发送队列
- **异步处理**: 非阻塞发送，提升吞吐量
- **优先级队列**: 支持文件发送优先级
- **队列监控**: 实时查看队列状态
- **暂停/恢复**: 队列暂停与恢复控制

**输入**: 用户提供发送队列所需的指令和必要参数。
**输出**: 返回发送队列的处理结果,包含执行状态码、结果数据和执行日志。### 重试与恢复
- **自动重试**: 可配置重试次数与间隔
- **断点续传**: 大文件分片上传支持断点续传
- **失败日志**: 完整记录失败原因
- **手动重发**: 一键重发失败文件

**输入**: 用户提供重试与恢复所需的指令和必要参数。
**处理**: 解析重试与恢复的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回重试与恢复的处理结果,包含执行状态码、结果数据和执行日志。### 审计与合规

- **操作审计**: 全部发送操作日志记录
- **接收追踪**: 文件接收状态追踪
- **合规导出**: 审计报告导出
- **敏感文件标记**: 敏感文件特殊标记

### 发送分析
- **发送统计**: 成功/失败/接收统计
- **趋势分析**: 发送量趋势图表
- **文件类型分析**: 各类型文件发送占比
- **导出报告**: CSV/JSON 格式导出

**输入**: 用户提供发送分析所需的指令和必要参数。
### 大文件支持
- **分片上传**: 大文件自动分片上传
- **进度追踪**: 上传进度实时显示
- **断点续传**: 网络中断后自动恢复

---

**输入**: 用户提供大文件支持所需的指令和必要参数。
**处理**: 解析大文件支持的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回大文件支持的处理结果,包含执行状态码、结果数据和执行日志。

#
## 适用场景

### 场景一：批量分发月度报表

财务部门需要向50名部门负责人分发各自的月度财务报表。

**准备收件人列表** `recipients.csv`:

```csv
open_id,name,department,file_path,file_name
ou_001,张三,技术部,reports/tech_july.pdf,技术部7月报表.pdf
ou_002,李四,市场部,reports/market_july.pdf,市场部7月报表.pdf
ou_003,王五,财务部,reports/finance_july.pdf,财务部7月报表.pdf
```

**执行批量分发**:

```bash
# 试运行（预览不实际发送）
python3 （请参考skill目录中的脚本文件） \
  --recipients recipients.csv \
  --rate-limit 10 \
  --dry-run
# ...
# 正式发送
python3 （请参考skill目录中的脚本文件） \
  --recipients recipients.csv \
  --rate-limit 10 \
  --retry 3 \
  --log batch_send.log
```

输出示例：

```text
📋 批量文件分发任务
   收件人: 50
   速率: 10 个/分钟
# ...
[1/50] ✅ ou_001 - 张三 - 技术部7月报表.pdf (2.3 MB)
[2/50] ✅ ou_002 - 李四 - 市场部7月报表.pdf (1.8 MB)
[3/50] ✅ ou_003 - 王五 - 财务部7月报表.pdf (3.1 MB)
...
📊 分发完成: 48 成功, 2 失败
   失败列表: failures.csv
   审计日志: batch_send_audit.log
```

### 场景二：多文件打包发送

向项目团队发送包含多个文件的项目交付包。

```bash
# 批量上传多个文件并打包发送
python3 （请参考skill目录中的脚本文件） \
  --target "oc_project_group" \
  --files "docs/design.pdf,docs/api.md,docs/test_report.xlsx,source/code.zip" \
  --package "project_delivery.zip" \
  --message "项目交付文档包，请查收。"
```

### 场景三：定时自动分发报表

设置每天早上自动生成并发送监控报表。

```bash
# 创建定时分发任务
python3 （请参考skill目录中的脚本文件） create \
  --name "daily-monitor-report" \
  --cron "0 9 * * 1-5" \
  --recipients monitor_team.csv \
  --file-generator "generate_report.py" \
  --timezone "Asia/Shanghai"
# ...
# 查看定时任务
python3 （请参考skill目录中的脚本文件） list
# ...
# 查看任务历史
python3 （请参考skill目录中的脚本文件） history --name "daily-monitor-report"
```

---

## 使用流程

### 从免费版升级

专业版完全兼容免费版，现有脚本无需修改：

```bash
# 免费版命令依然有效
python3 （请参考skill目录中的脚本文件） file.pdf ou_详情见说明 app_id app_secret
python3 （请参考skill目录中的脚本文件） image.png ou_详情见说明 app_id app_secret
# ...
# 专业版新增命令
python3 （请参考skill目录中的脚本文件） --recipients list.csv
python3 （请参考skill目录中的脚本文件） --target oc_详情见说明 --files f1.pdf,f2.pdf
```

### 配置批量分发

```json
{
  "batch": {
    "rate_limit": 10,
    "max_recipients": 500,
    "retry_count": 3,
    "retry_delay": 30,
    "concurrency": 5,
    "on_failure": "log",
    "failure_log": "~/.config/feishu-file-sender/failures.log"
  }
}
```

### 配置审计日志

```json
{
  "audit": {
    "enabled": true,
    "log_file": "~/.config/feishu-file-sender/audit.log",
    "actions": ["send", "upload", "delete"],
    "retention_days": 365,
    "auto_archive": true
  }
}
```

---

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | feishu-file-sender处理的内容输入 |,  |
| content | string | 否 | feishu-file-sender处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "sender 相关配置参数",
    result: "sender 相关配置参数",
    result: "sender 相关配置参数",
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

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8 及以上
- **网络环境**: 需可访问飞书开放平台 API（国内: open.feishu.cn / 国际: open.larksuite.com）
- **磁盘空间**: 队列与日志建议预留 1GB 以上

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 官方网站下载安装 |
| Python 标准库 | 运行库 | 必需 | Python 自带（requests, json, csv） |
| 飞书应用 | 应用 | 必需 | 飞书开放平台创建应用 |
| app_id/app_secret | 凭证 | 必需 | 飞书应用配置页获取 |
| cron 服务 | 系统服务 | 可选 | 系统自带（定时任务需要） |
| 数据库 | 存储引擎 | 可选 | 用于队列与审计日志（可选 SQLite 文件存储） |

### API Key 配置

- 本工具通过飞书应用凭证（app_id 与 app_secret）获取 `tenant_access_token` 进行认证
- 凭证通过配置文件或命令行参数传入
- 企业用户建议使用密钥管理服务统一管理凭证
- 应用需在飞书开放平台开通文件上传、消息发送与文件管理权限

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，部分功能需要 exec 命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行 Python 脚本，支持批量分发、队列管理、分片上传与审计合规等企业级功能

## 案例展示

### 发送队列配置

```json
{
  "queue": {
    "enabled": true,
    "queue_dir": "~/.config/feishu-file-sender/queue",
    "max_concurrency": 5,
    "priority_levels": 3,
    "auto_retry": true,
    "retry_count": 3,
    "retry_delay": 60
  }
}
```

### 大文件分片配置

```json
{
  "large_file": {
    "threshold_mb": 10,
    "chunk_size_mb": 5,
    "resume_enabled": true,
    "progress_tracking": true,
    "temp_dir": "~/.config/feishu-file-sender/temp"
  }
}
```

### 定时任务配置

```json
{
  "schedules": [
    {
      "name": "weekly-report",
      "cron": "0 10 * * 1",
      "timezone": "Asia/Shanghai",
      "recipients": "recipients.csv",
      "file_generator": "generate_report.py",
      "file_name": "周报_"sender_result".pdf"
    }
  ]
}
```

---

## 常见问题

### 错误恢复步骤
| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

**解决**: 降低发送速率，飞书 API 有频率限制：

```bash
python3 （请参考skill目录中的脚本文件） --recipients list.csv --rate-limit 5
```

### 问题2：大文件上传超时

**解决**: 启用分片上传与断点续传：

```bash
# 使用分片上传
python3 （请参考skill目录中的脚本文件） \
  --file large_video.mp4 \
  --target ou_详情见说明 \
  --chunk-size 5 \
  --resume
```

### 问题3：发送队列堆积

**解决**: 检查队列状态并调整并发：

```bash
# 查看队列状态
python3 （请参考skill目录中的脚本文件） status
# ...
# 增加并发数
python3 （请参考skill目录中的脚本文件） config --concurrency 10
```

### 问题4：审计日志占用空间过大

**解决**: 配置日志轮转与压缩：

```bash
# 压缩旧日志
python3 （请参考skill目录中的脚本文件） compress --older-than 30
# ...
# 清理过期日志
python3 （请参考skill目录中的脚本文件） clean --older-than 365
```

### 问题5：部分接收者未收到文件

**解决**: 检查失败列表并重发：

```bash
# 查看失败列表
cat failures.csv
# ...
# 重发失败文件
python3 （请参考skill目录中的脚本文件） --recipients failures.csv --retry 3
```

---

## 错误处理

| 错误场景(续)(续)| 原因 | 处理方式 |
|-------:|:-------|-------:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持

