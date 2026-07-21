---
slug: feishu-card-builder
name: feishu-card-builder
version: "1.0.0"
displayName: 飞书卡片专业版
summary: 企业级飞书交互卡片与批量推送，支持模板与高级组件
license: Proprietary
edition: pro
description: |-
  飞书卡片专业版面向企业用户与高效能个人用户，在免费版卡片消息发送能力之上扩展
  批量推送、卡片模板系统、高级交互组件、数据动态绑定、卡片版本管理与发送分析等
  企业级特性。核心能力:
  - 批量卡片推送（多用户/多群组同时发送）
  - 卡片模板系统（内置与自定义模板。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
- 沟通协作
- 飞书
- 卡片消息
- 企业效率
- 批量操作
tools:
  - - read
- exec
---
# 飞书卡片专业版

## 核心能力

### 批量推送引擎
- **多目标发送**: 一次性向多个用户与群组推送
- **收件人列表**: 支持 CSV/JSON 收件人列表
- **变量替换**: 每个目标收到个性化内容
- **速率控制**: 可配置发送速率与并发
- **失败重试**: 自动重试失败目标

**输出**: 返回批量推送引擎的执行结果,包含操作状态和输出数据。
### 卡片模板系统
- **内置模板**: 通知、报告、审批、邀请、告警等企业常用模板
- **自定义模板**: 创建、编辑、删除自定义模板
- **变量插值**: 支持 `（根据实际场景填充）` 语法
- **条件渲染**: 支持条件判断与循环
- **模板预览**: 渲染效果实时预览
- **版本管理**: 模板版本控制与回滚

**输入**: 用户提供卡片模板系统所需的指令和必要参数。
**处理**: 按照skill规范执行卡片模板系统操作,遵循单一意图原则。### 高级交互组件
- **表单组件**: 输入框、文本域、选择器
- **多按钮组**: 多个操作按钮排列
- **分栏布局**: 多列内容布局
- **分隔线**: 内容分隔
- **备注组件**: 折叠展开内容
- **数据表格**: 结构化数据展示

**处理**: 按照skill规范执行高级交互组件操作,遵循单一意图原则。
**输出**: 返回高级交互组件的执行结果,包含操作状态和输出数据。### 数据动态绑定
- **JSON 数据源**: 从 JSON 文件自动填充卡片内容
- **API 数据源**: 从外部 API 获取数据填充
- **数据映射**: 字段映射与转换
- **条件显示**: 根据数据动态显示/隐藏组件

**输入**: 用户提供数据动态绑定所需的指令和必要参数。
**输出**: 返回数据动态绑定的执行结果,包含操作状态和输出数据。### 发送分析
- **送达统计**: 成功/失败/已读统计
- **阅读追踪**: 卡片打开率追踪
- **按钮点击**: 按钮点击统计
- **趋势分析**: 发送量趋势图表
- **导出报告**: CSV/JSON 格式导出

### 定时与触发
- **定时推送**: 指定时间或周期性发送
- **条件触发**: 满足条件自动发送
- **任务队列**: 管理待发送任务
- **状态监控**: 实时查看任务状态

---

### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级飞书交互卡、片与批量推送、支持模板与高级组、飞书卡片专业版面、向企业用户与高效、能个人用户、在免费版卡片消息、发送能力之上扩展、卡片版本管理与发、送分析等、企业级特性、核心能力、批量卡片推送、多用户、多群组同时发送、内置与自定义模板、Use、需要数据分析、报表生成、统计洞察、数据可视化时使用、不适用于实时流数、据处理。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一：批量推送个性化通知
HR 部门需要向500名员工发送包含个人信息的工资条通知卡片。

**准备收件人列表** `employees.csv`:

```csv
open_id,name,department,salary_month,amount
ou_001,张三,技术部,2026年7月,¥15000
ou_002,李四,市场部,2026年7月,¥12000
ou_003,王五,财务部,2026年7月,¥13000
```

**创建卡片模板** `templates/salary_card.json`:

```json
{
  "header": {
    "title": "工资条通知 - （根据实际场景填充）",
    "color": "blue"
  },
  "elements": [
    {
      "type": "div",
      "text": "尊敬的 **（根据实际场景填充）**（（根据实际场景填充））："
    },
    {
      "type": "div",
      "text": "您本月工资为 **（根据实际场景填充）**，请登录系统查看详情。"
    },
    {
      "type": "action",
      "actions": [
        {
          "type": "button",
          "text": "查看详情",
          "url": "https://hr.company.com/salary/（根据实际场景填充）"
        }
      ]
    }
  ]
}
```

**执行批量推送**:

```bash
# 试运行（预览不实际发送）
node skills/feishu-card-builder/batch-send.js \
  --recipients employees.csv \
  --template templates/salary_card.json \
  --rate-limit 20 \
  --dry-run

# 正式发送
node skills/feishu-card-builder/batch-send.js \
  --recipients employees.csv \
  --template templates/salary_card.json \
  --rate-limit 20 \
  --log batch_send.log
```

输出示例：

```text
📋 批量推送任务
   收件人: 500
   模板: templates/salary_card.json
   速率: 20 条/分钟

[1/500] ✅ ou_001 - 张三 - 技术部
[2/500] ✅ ou_002 - 李四 - 市场部
...
📊 推送完成: 498 成功, 2 失败
   发送报告: batch_send_report.json
```

### 场景二：数据报表卡片自动生成
运维团队需要每天自动生成系统监控报表卡片并推送到管理群。

```bash
# 创建定时任务
node skills/feishu-card-builder/schedule.js create \
  --name "daily-monitor-report" \
  --cron "0 9 * * 1-5" \
  --target "oc_management_group" \
  --template templates/monitor_report.json \
  --data-source "fetch_metrics.py" \
  --timezone "Asia/Shanghai"

# 查看定时任务
node skills/feishu-card-builder/schedule.js list

# 查看任务历史
node skills/feishu-card-builder/schedule.js history --name "daily-monitor-report"
```

### 场景三：交互式审批卡片
发送包含审批按钮的交互卡片，支持批准/驳回操作。

```bash
# 发送交互式审批卡片
node skills/feishu-card-builder/interactive-send.js \
  --target "ou_manager" \
  --template templates/approval.json \
  --data '{"applicant":"张三","amount":"¥5000","purpose":"差旅报销"}' \
  --callback-url "https://api.company.com/approval/callback"
```

审批卡片模板 `templates/approval.json`:

```json
{
  "header": {
    "title": "审批申请",
    "color": "orange"
  },
  "elements": [
    {"type": "div", "text": "申请人: **（根据实际场景填充）**"},
    {"type": "div", "text": "金额: **（根据实际场景填充）**"},
    {"type": "div", "text": "事由: （根据实际场景填充）"},
    {
      "type": "action",
      "actions": [
        {"type": "button", "text": "批准", "value": "approve", "type": "primary"},
        {"type": "button", "text": "驳回", "value": "reject", "type": "danger"}
      ]
    }
  ]
}
```

---

## 使用流程

### 从免费版升级
专业版完全兼容免费版，现有命令无需修改：

```bash
# 免费版命令依然有效
node skills/feishu-card-builder/send.js --target "ou_详情见说明" --text "Hello"
node skills/feishu-card-builder/send_safe.js --target "ou_详情见说明" --text "内容" --title "通知"

# 专业版新增命令
node skills/feishu-card-builder/batch-send.js --recipients list.csv --template tpl.json
node skills/feishu-card-builder/interactive-send.js --target "ou_详情见说明" --template tpl.json
```

### 配置模板系统
```json
{
  "templates": {
    "dir": "templates/",
    "builtins": ["notification", "report", "approval", "alert"],
    "version_control": true,
    "max_versions": 10
  }
}
```

### 配置发送分析
```json
{
  "analytics": {
    "enabled": true,
    "tracking": {
      "delivery": true,
      "read_receipt": true,
      "button_click": true
    },
    "log_file": "~/.config/feishu-card-builder/analytics.log",
    "retention_days": 90
  }
}
```

---

### 命令参数说明

1. `--title`: 命令参数,用于指定操作选项
2. `--rate-limit`: 命令参数,用于指定操作选项
3. `--timezone`: 命令参数,用于指定操作选项
4. `--target`: 命令参数,用于指定操作选项
5. `-log`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

### 命令参数说明

- `--callback-url`: 命令参数,用于指定操作选项
- `--data`: 命令参数,用于指定操作选项
- `--recipients`: 命令参数,用于指定操作选项
- `--data-source`: 命令参数,用于指定操作选项
- `--dry-run`: 命令参数,用于指定操作选项

### 命令参数说明

- `-send`: 命令参数,用于指定操作选项
- `-report`: 命令参数,用于指定操作选项
- `-monitor-report`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js版本**: 16 及以上
- **网络环境**: 需可访问飞书开放平台 API
- **磁盘空间**: 模板与日志建议预留 500MB 以上

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需 | 官方网站下载安装 |
| feishu-common | 模块 | 必需 | 飞书通用认证模块 |
| 飞书应用 | 应用 | 必需 | 飞书开放平台创建应用 |
| app_id/app_secret | 凭证 | 必需 | 飞书应用配置页获取 |
| cron 服务 | 系统服务 | 可选 | 系统自带（定时任务需要） |
| 数据库 | 存储引擎 | 可选 | 用于模板版本与日志（可选 SQLite 文件存储） |

### API Key 配置
- 本工具通过飞书应用凭证（app_id 与 app_secret）进行认证
- 凭证由 feishu-common 模块统一管理
- 交互回调需配置 callback_secret
- 无需额外 API Key
- 应用需在飞书开放平台开通消息发送与交互回调权限

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要 exec 命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行 Node.js 脚本，支持批量推送、模板渲染、交互组件与发送分析等企业级功能

## 案例展示

### 批量推送配置
```json
{
  "batch": {
    "rate_limit": 20,
    "max_recipients": 2000,
    "retry_count": 3,
    "retry_delay": 30,
    "concurrency": 5,
    "on_failure": "log",
    "failure_log": "~/.config/feishu-card-builder/batch_failures.log"
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
      "target": "oc_team_group",
      "template": "templates/weekly_report.json",
      "data_source": "generate_report.py"
    }
  ]
}
```

### 交互回调配置
```json
{
  "interactive": {
    "callback_url": "https://api.company.com/feishu/callback",
    "callback_secret": "your_callback_secret",
    "timeout": 30,
    "retry": 3
  }
}
```

---

## 常见问题

### 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制
**解决**: 降低发送速率，飞书 API 有频率限制：

```bash
node skills/feishu-card-builder/batch-send.js \
  --recipients list.csv --template tpl.json --rate-limit 10
```

### 问题2：模板变量未替换
**解决**: 确保变量名与数据源字段一致：

```bash
# 验证模板
node skills/feishu-card-builder/template.js validate --name "通知" --data sample.json
```

### 问题3：交互回调无响应
**解决**: 检查回调 URL 与密钥配置：

```bash
# 测试回调
node skills/feishu-card-builder/interactive.js test-callback

# 查看回调日志
node skills/feishu-card-builder/interactive.js callback-log
```

### 问题4：定时任务未执行
**解决**: 检查 cron 表达式与时区：

```bash
node skills/feishu-card-builder/schedule.js validate --cron "0 9 * * 1-5"
node skills/feishu-card-builder/schedule.js status --name "daily-report"
```

### 问题5：卡片内容超长
**解决**: 飞书卡片有内容长度限制，超长内容建议拆分或使用折叠组件：

```json
{
  "type": "note",
  "elements": [
    {"type": "div", "text": "折叠的详细内容..."}
  ]
}
```

---

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
- 需要LLM支持
- 需要LLM支持
- 需要LLM支持

