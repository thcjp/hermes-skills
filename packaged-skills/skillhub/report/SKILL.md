---
slug: "report"
name: "report"
version: 1.0.4
displayName: "定制报表生成"
summary: "配置自定义周期性报表,用户定义数据源,自动处理调度与格式化投递"
license: "Proprietary"
description: |-
  配置自定义周期性报表,用户定义数据源,自动处理调度与格式化投递。核心能力包括数据源用户驱动配置、YAML报表配置、Cron定时调度、多渠道投递(chat/telegram/file/email)、报表管理(列表/暂停/按需运行)与环境变量安全凭证管理.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
category: "Automation"
---
# 定制报表生成

配置自定义周期性报表,用户定义数据源,自动处理调度与格式化投递.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 定制报表生成处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 定制报表生成自动处理调度与格式化 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 数据存储结构

```text
~/report/
├── memory.md               # 索引 + 偏好设置
├── {name}/
│   ├── config.md           # 报表配置
│   ├── data.jsonl          # 历史数据
│   └── generated/          # 已生成的报表
```

首次使用前创建: `mkdir -p ~/report`

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

- **数据源用户驱动配置**: 用户指定追踪的数据内容,如需外部API则由用户提供凭证,凭证以环境变量引用存储而非明文值
- **YAML报表配置**: 在 `~/report/{name}/config.md` 中以YAML格式定义报表名称、调度计划、数据源、格式与投递渠道
- **Cron定时调度**: 支持每日 `0 9 * * *`、每周 `0 9 * * 1`、每月 `0 9 1 * *` 与按需触发四种调度频率
- **多渠道投递**: 支持 `chat`(对话回复)、`telegram`(Telegram消息)、`file`(本地文件)、`email`(邮件)四种投递渠道
- **报表管理**: 支持列表查看(读取 `~/report/memory.md`)、暂停报表(更新配置)、按需运行(立即生成)
- **环境变量安全凭证**: 配置中引用环境变量名而非值,凭证不存储在配置文件中,确保安全性
- **投递安全控制**: 外部投递(Telegram/webhook/email)将报表内容发送到设备外,用户需显式配置每个渠道并信任目标;`file` 投递保持本地存储
### 数据源用户驱动配置

针对数据源用户驱动,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供数据源用户驱动配置相关的配置参数、输入数据和处理选项.
**输出**: 返回数据源用户驱动配置的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`数据源用户驱动配置`的配置文档进行参数调优
### YAML报表配置

针对YAML报表,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供YAML报表配置相关的配置参数、输入数据和处理选项.
**输出**: 返回YAML报表配置的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`YAML报表配置`的配置文档进行参数调优
### Cron定时调度

针对Cron定时,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Cron定时调度相关的配置参数、输入数据和处理选项.
**输出**: 返回Cron定时调度的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Cron定时调度`的配置文档进行参数调优
#
## 适用范围

本技能:

* 在 `~/report/` 目录存储报表配置
* 按调度计划生成报表
* 通过用户配置的渠道投递报表

**用户驱动模型:**

* 用户定义包含哪些数据
* 用户授予对所需数据源的访问权限
* 用户在外部数据需要时提供API密钥
* 技能处理调度和格式化

本技能不会:

* 在未提供用户凭证的情况下访问API
* 从用户未指定的数据源拉取数据
* 存储凭证(用户通过环境变量提供)

## 环境变量

**无固定要求。** 用户按需提供API密钥:

```bash
export STRIPE_API_KEY="[REDACTED]"
export ANALYTICS_API_KEY="[REDACTED]"
```

配置中引用环境变量名,永不引用值.
## 投递安全

外部投递(Telegram/webhook/email)将报表内容发送到设备外.
* 用户显式配置每个渠道
* 用户负责信任投递目标
* `file` 投递保持在本地(`~/report/{name}/generated/`)

## 能力速查
### 1. 用户定义数据源

创建报表时:

1. 用户指定要追踪的数据
2. 如需外部API,用户提供凭证
3. 凭证存储为环境变量引用,而非值

示例:

```text
用户: "每周生成一次我的Stripe收入报表"
助手: "我需要Stripe API访问权限。请在你的环境中设置 STRIPE_API_KEY。"
用户: "已完成"
配置存储为 "source": {"type": "api", "env": "STRIPE_API_KEY"}
```

### 2. 报表配置

在 `~/report/{name}/config.md` 中:

```yaml
name: weekly-revenue
schedule: "0 9 * * 1"  # 每周一上午9点
sources:
  - type: api
    env: STRIPE_API_KEY  # 用户提供
format: chat
delivery: telegram
```

### 3. 调度计划

| 频率 | Cron表达式 | 示例 |
|:---:|:---:|:---:|
| 每日 | `0 9 * * *` | 每天上午9点 |
| 每周 | `0 9 * * 1` | 每周一上午9点 |
| 每月 | `0 9 1 * *` | 每月1日上午9点 |
| 按需 | - | 用户请求时 |

### 4. 投递渠道

用户在 `config.md` 中配置:

* `chat` — 在对话中回复
* `telegram` — 发送到Telegram(用户提供chat ID)
* `file` — 保存到 `~/report/{name}/generated/`
* `email` — 通过用户配置的邮件发送

### 5. 报表管理

```text
"列出我的报表" → 读取 ~/report/memory.md
"暂停X报表"    → 更新配置
"立即运行X"    → 按需生成
```

## 使用流程

1. 执行 `mkdir -p ~/report` 创建数据存储目录
2. 用户定义报表名称、数据源和所需凭证
3. 用户在环境中设置所需的环境变量(如 `STRIPE_API_KEY`)
4. 在 `~/report/{name}/config.md` 中创建YAML配置,指定 `schedule`、`sources`、`format` 和 `delivery`
5. 根据调度计划自动生成报表,或用户请求按需运行
6. 通过配置的投递渠道发送报表内容
7. 使用"列出我的报表"查看所有报表,"暂停X报表"暂停,"立即运行X"按需生成

#
## 示例

### 示例1:创建每周收入报表

```yaml
# ~/report/weekly-revenue/config.md
name: weekly-revenue
schedule: "0 9 * * 1"
sources:
  - type: api
    env: STRIPE_API_KEY
    endpoint: "https://api.stripe.com/v1/charges"
    params:
      created.gte: "last_week_start"
      created.lt: "today"
format: chat
delivery: telegram
```

输出:
```text
报表 weekly-revenue 已创建.
调度: 每周一上午9点
数据源: Stripe API (环境变量 STRIPE_API_KEY)
投递: Telegram
请在环境中设置 STRIPE_API_KEY 后生效.
```

### 示例2:每日站会摘要报表

```yaml
# ~/report/daily-standup/config.md
name: daily-standup
schedule: "0 8 * * 1-5"
sources:
  - type: api
    env: PROJECT_API_TOKEN
    endpoint: "https://api.projectmgmt.com/v2/tasks"
    params:
      assignee: "current_user"
      status: "in_progress"
format: chat
delivery: chat
```

### 示例3:月度文件报表

```yaml
# ~/report/monthly-summary/config.md
name: monthly-summary
schedule: "0 9 1 * *"
sources:
  - type: file
    path: "~/projects/logs/"
    pattern: "*.jsonl"
format: markdown
delivery: file
```

输出:
```text
报表 monthly-summary 已生成.
保存位置: ~/report/monthly-summary/generated/2024-01-01-summary.md
包含 3 个数据源的汇总分析.
```

### 示例4:管理报表

```text
用户: "列出我的报表"
助手: "当前报表:
  1. weekly-revenue (每周一 9:00, Telegram投递, 活跃)
  2. daily-standup (工作日 8:00, 对话投递, 活跃)
  3. monthly-summary (每月1日 9:00, 文件投递, 已暂停)"
# ...
用户: "暂停daily-standup"
助手: "已暂停 daily-standup 报表。下次调度将跳过执行。"
# ...
用户: "立即运行weekly-revenue"
助手: "正在生成 weekly-revenue 报表...
  已通过Telegram投递。本周收入总计 $12,450,较上周增长8.3%。"
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 环境变量未设置 | 用户未在环境中配置 `STRIPE_API_KEY` 等凭证 | 提示用户执行 `export STRIPE_API_KEY="..."` 设置环境变量,配置中仅引用变量名 |
| Cron表达式无效 | `schedule` 字段格式错误(如 `0 9 *` 少字段) | 使用标准5字段Cron格式 `分 时 日 月 周`,参考调度计划表 |
| 外部API认证失败 | API密钥过期或无效 | 检查环境变量值是否正确,确认API密钥未过期,重新生成密钥后更新环境变量 |
| Telegram投递失败 | chat ID错误或Bot Token无效 | 确认Telegram Bot Token已配置,chat ID正确(负数表示群组),Bot已加入目标群组 |
| 数据源不可达 | API端点宕机或网络超时 | 检查API端点URL是否正确,确认网络连通性,设置机制或切换备用端点 |
| 配置文件格式错误 | `config.md` 中YAML缩进或语法错误 | 使用标准YAML缩进(空格而非Tab),验证 `name`、`schedule`、`sources`、`format`、`delivery` 字段完整性 |
| 文件权限错误 | `~/report/` 目录无写入权限 | 执行 `chmod 755 ~/report` 修改权限,确认用户对目录有读写权限 |
| 报表生成超时 | 数据源返回大量数据导致处理超时 | 在配置中添加分页参数限制单次拉取量,或缩小查询时间范围 |
| 投递内容过大 | 报表内容超过投递渠道限制(如Telegram消息4096字符) | 切换为 `file` 投递生成本地文件,或启用摘要模式精简内容 |

## 常见问题

### Q1: 如何添加新的数据源?
A: 在 `config.md` 的 `sources` 数组中添加新条目。每个数据源需指定 `type`(api/file)、`env`(环境变量名,仅API类型)和 `endpoint`(API端点URL)。如需外部API访问,需先在环境中设置对应的环境变量,配置中仅引用变量名而非值.
### Q2: Cron表达式的5个字段分别代表什么?
A: 标准Cron格式为 `分 时 日 月 周`。例如 `0 9 * * 1` 表示每周一上午9点: 分(0)、时(9)、日(*任意)、月(*任意)、周(1=周一)。`0 9 1 * *` 表示每月1日9点。`0 8 * * 1-5` 表示工作日(周一至周五)8点.
### Q3: 投递渠道有什么区别,如何选择?
A: `chat` 在对话中直接回复,适合即时查看;`telegram` 发送到Telegram群组或用户,适合团队共享;`file` 保存到 `~/report/{name}/generated/` 本地目录,适合归档和审计;`email` 通过邮件发送,适合正式分发。外部投递(telegram/email)会将内容发送到设备外,需确保信任目标.
### Q4: 凭证如何安全管理?
A: 凭证以环境变量形式存储,配置文件中仅引用变量名(如 `STRIPE_API_KEY`),永不存储明文值。使用 `export VAR_NAME="value"` 在环境中设置。技能不会存储凭证值,也不会在日志或报表中暴露凭证。每次运行时从环境中读取.
### Q5: 如何暂停或恢复报表?
A: 使用"暂停X报表"命令,技能会更新 `config.md` 将报表标记为暂停状态,下次调度将跳过执行。恢复时使用"恢复X报表"命令。按需运行不受暂停状态影响,使用"立即运行X"可随时强制生成.
### Q6: 报表历史数据存储在哪里?
A: 历史数据存储在 `~/report/{name}/data.jsonl` 中,每次生成的报表保存在 `~/report/{name}/generated/` 目录。所有报表的索引和用户偏好存储在 `~/report/memory.md` 中。使用 `file` 投递渠道的报表会持久保存,其他渠道投递后也会在本地保留副本.
### Q7: 如何修改已有报表的配置?
A: 直接编辑 `~/report/{name}/config.md` 文件,修改 `schedule`、`sources`、`format` 或 `delivery` 字段。修改后下一次调度将使用新配置。也可通过对话指令如"将weekly-revenue改为每日9点"让技能自动更新配置文件.
## 已知限制

- 不支持实时流数据处理,仅支持定时或按需批量生成
- 外部API访问依赖用户提供有效凭证,无凭证无法获取数据
- Telegram投递受消息长度限制(4096字符),超长内容需切换file投递
- Cron调度精度为分钟级,不支持秒级调度
- 报表格式固定为chat/markdown,不支持自定义模板引擎
