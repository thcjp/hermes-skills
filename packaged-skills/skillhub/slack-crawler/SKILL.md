---
slug: "slack-crawler"
name: "slack-crawler"
version: "1.0.0"
displayName: "Slack爬虫工具Pro"
summary: "企业级Slack归档方案，含API同步、线程完整化、定时调度、增量更新与数据导出。"
license: "Proprietary"
edition: "pro"
description: |-
  Slack爬虫工具（专业版）为团队与企业提供完整的Slack归档与检索方案，支持API同步、线程/DM完整化、定时调度与增量更新。核心能力：Slack API双向同步、线程回复与私信完整化、定时调度自动同步、增量更新与版本对比、数据导出（CSV/JSON）、高级SQL分析、多工作区归档、数据回滚。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
  - 集成工具
  - 数据分析
  - 企业级
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# Slack爬虫工具Pro

## 核心能力

| 能力 | 说明 | 专业版支持 |
|------|------|-----------|
| 桌面端同步 | 从Slack桌面应用导出同步 | 是 |
| API同步 | 从Slack API同步最新数据 | 是 |
| 线程回复完整化 | 自动补全所有线程回复 | 是 |
| 私信完整化 | 归档私信与群聊 | 是 |
| 定时调度 | 定时自动同步 | 是 |
| 增量更新 | 仅同步变化数据 | 是 |
| 版本对比与回滚 | 数据版本管理与回滚 | 是 |
| 数据导出 | 导出为CSV/JSON | 是 |
| 高级SQL分析 | 复杂统计与趋势分析 | 是 |
| 多工作区归档 | 同时归档多个工作区 | 是 |
| 关键词检索 | 全文检索 | 是 |
| 只读SQL统计 | 精确统计与排名 | 是 |
### 桌面端同步

执行桌面端同步操作,处理用户输入并返回结果。

**输入**: 用户提供桌面端同步所需的参数和指令。

**输出**: 返回桌面端同步的处理结果。

- 执行`桌面端同步`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`桌面端同步`相关配置参数进行设置
### API同步

执行API同步操作,处理用户输入并返回结果。

**输入**: 用户提供API同步所需的参数和指令。

**输出**: 返回API同步的处理结果。

- 执行`API同步`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`API同步`相关配置参数进行设置
### 线程回复完整化

执行线程回复完整化操作,处理用户输入并返回结果。

**输入**: 用户提供线程回复完整化所需的参数和指令。

**输出**: 返回线程回复完整化的处理结果。

- 执行`线程回复完整化`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`线程回复完整化`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级、归档方案、线程完整化、增量更新与数据导、爬虫工具、为团队与企业提供、完整的、归档与检索方案、定时调度与增量更、核心能力、双向同步、线程回复与私信完、定时调度自动同步、增量更新与版本对、数据回滚、Use、需要数据分析、报表生成、统计洞察、数据可视化时使用、不适用于实时流数、据处理。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景1：企业级Slack合规归档

金融行业客户要求所有Slack消息（含线程回复与私信）长期留存供合规审计。使用专业版：定时调度每小时从API同步最新数据，自动完整化所有线程回复，归档数据每日导出至对象存储，满足留存要求。

### 场景2：跨工作区数据分析

集团有多个Slack工作区。管理员使用专业版多工作区归档：为每个工作区配置同步任务，统一归档到本地，通过SQL跨工作区统计活跃度、识别低活跃频道、优化工作区结构。

### 场景3：团队协作洞察

HR团队希望分析跨部门协作情况。使用专业版高级SQL：统计跨频道@提及次数、线程深度分布、响应时间分布，生成协作洞察报告，识别协作瓶颈与优秀实践。

### 场景4：长期消息留存与回滚

研发团队需要保留所有技术讨论以便回溯。专业版增量更新与版本对比功能记录每次同步的数据变化，当误删重要讨论时可通过版本回滚恢复。

### 场景5：定时同步避免人工干预

运维团队希望归档自动保持新鲜，无需人工触发同步。使用专业版定时调度：配置每小时增量同步，仅同步变化数据（增量更新），带宽与API配额消耗最小化。

## 使用流程

### 步骤1：配置Slack API Token

```bash
export SLACK_TOKEN="xoxb-your-token-here"
```

Token需具有`channels:history`、`groups:history`、`im:history`、`mpim:history`等读取权限。

### 步骤2：初始化归档并首次全量同步

```bash
slack-crawler init
slack-crawler sync --source api --full
```

全量同步会拉取所有可访问频道的历史消息，首次同步耗时取决于工作区规模。

### 步骤3：完整化线程与私信

```bash
slack-crawler hydrate --threads
slack-crawler hydrate --dms
slack-crawler hydrate --mpims
```

`hydrate`命令补全所有线程回复、私信与群聊消息。

### 步骤4：配置定时调度

```yaml
schedule:
  sync:
    cron: "0 * * * *"    # 每小时同步
    mode: incremental     # 增量更新
    hydrate: true         # 自动完整化新线程
  export:
    cron: "0 2 * * *"    # 每日凌晨2点导出
    format: json
    destination: s3://company-slack-archive/
```

### 步骤5：增量同步与版本管理

```bash
# 增量同步（仅变化数据）
slack-crawler sync --source api --incremental

# 查看版本历史
slack-crawler versions --channel "#general" --limit 10

# 回滚到指定版本
slack-crawler rollback --version v20260715
```

### 命令参数说明

1. `--split-by`: 命令参数,用于指定操作选项
2. `--dms`: 命令参数,用于指定操作选项
3. `--format`: 命令参数,用于指定操作选项
4. `--mpims`: 命令参数,用于指定操作选项
5. `--output`: 命令参数,用于指定操作选项

### 命令参数说明

- `--until`: 命令参数,用于指定操作选项
- `--full`: 命令参数,用于指定操作选项
- `-slack-archive`: 命令参数,用于指定操作选项
- `--incremental`: 命令参数,用于指定操作选项
- `-your-token-here`: 命令参数,用于指定操作选项

### 命令参数说明

- `--since`: 命令参数,用于指定操作选项
- `--source`: 命令参数,用于指定操作选项
- `-alerts`: 命令参数,用于指定操作选项

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

| 现象 | 可能原因 | 解决方案 |
|------|---------|---------|
| 同步429 Rate limited | 超过Slack速率限制 | 降低rate_limit配置或增加同步间隔 |
| 线程完整化不完整 | Token缺少threads:read权限 | 在Slack App配置中添加权限 |
| 增量同步遗漏消息 | 游标检查点损坏 | 删除checkpoint.json后全量同步 |
| 定时任务未执行 | 调度服务未启动 | 检查cron服务与调度配置 |
| SQL查询慢 | 数据量大无索引 | 迁移至`PostgreSQL`或添加索引 |
| 导出文件过大 | 未压缩 | 启用gzip压缩或按频道分文件 |

## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux
- **本地存储**：归档数据库默认存储于`~/.slack-crawler/archive.db`
- **数据库**：SQLite（默认，内置）或`PostgreSQL`（大型工作区推荐）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Slack API Token | 凭据 | 必需 | 在Slack App配置中创建 |
| Slack桌面应用 | 桌面软件 | 可选 | Slack官网下载（桌面端同步） |
| SQLite | 数据库 | 必需 | 系统内置或随工具安装 |
| `PostgreSQL` | 数据库 | 可选 | postgresql.org下载（大型工作区） |
| 对象存储 | 基础设施 | 可选 | AWS S3/阿里云OSS（导出归档） |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- **Slack API Token**：存储于环境变量`SLACK_TOKEN`，需具有history读取权限
- **多工作区Token**：每个工作区独立Token，通过`--workspace`切换
- **禁止**：在脚本或配置文件中硬编码Token

### 可用性分类
- **分类**：MD+EXEC（）
- **说明**：基于Markdown的AI Skill，

## 案例展示

### 定时调度配置

```yaml
schedule:
  sync:
    cron: "0 * * * *"
    mode: incremental
    channels: ["#general", "#engineering", "#ops"]  # 可选：指定频道
    hydrate_threads: true
    hydrate_dms: false  # 私信按需开启
  export:
    cron: "0 2 * * *"
    format: json
    destination: s3://company-slack-archive/
    compress: true
  alert:
    on_sync_failure: true
    channel: "#ops-alerts"
```

### 增量更新配置

```yaml
incremental:
  strategy: cursor       # 基于游标的增量
  checkpoint: ~/.slack-crawler/checkpoint.json
  on_conflict: skip      # 冲突时跳过（已存在的不覆盖）
  batch_size: 1000       # 每批拉取1000条
  rate_limit: 1          # 每秒1请求（遵守Slack限制）
```

### 高级SQL分析

```bash
# 跨频道协作分析：@提及网络
slack-crawler sql "
  select mentioned_user, count(*) as mention_count
  from mentions
  group by mentioned_user
  order by mention_count desc
  limit 20;
"

# 线程深度分布
slack-crawler sql "
  select thread_depth, count(*) as cnt
  from threads
  group by thread_depth
  order by thread_depth;
"

# 响应时间分析（中位数）
slack-crawler sql "
  select channel,
         avg(response_time_minutes) as avg_resp,
         max(response_time_minutes) as max_resp
  from response_times
  group by channel
  order by avg_resp desc;
"

# 活跃时段热力图数据
slack-crawler sql "
  select strftime('%w', timestamp) as weekday,
         strftime('%H', timestamp) as hour,
         count(*) as cnt
  from messages
  group by weekday, hour
  order by cnt desc;
"
```

### 数据导出

```bash
# 导出为JSON
slack-crawler export --format json --output ./archive-2026-07.json

# 导出为CSV（按频道分文件）
slack-crawler export --format csv --output ./archive/ --split-by channel

# 导出指定时间范围
slack-crawler export --format json --since 2026-01-01 --until 2026-06-30 --output ./h1-2026.json
```

## 常见问题

### Q1：首次全量同步需要多长时间？
A：取决于工作区规模与历史长度。1万消息约5分钟，10万消息约30分钟，百万级消息需数小时。受Slack API速率限制影响（约1请求/秒）。

### Q2：增量同步如何判断"变化"？
A：基于Slack的`latest`游标，仅拉取上次同步后新增的消息。已存在的消息不重复拉取，最小化API消耗。

### Q3：线程完整化会拉取多少额外数据？
A：取决于线程活跃度。通常线程回复量为顶层消息的2-5倍。完整化是确保归档完整的关键步骤，不可跳过。

### Q4：可以同时归档多个工作区吗？
A：可以。专业版支持多工作区归档，每个工作区使用独立Token与归档数据库，通过`--workspace`参数切换。

### Q5：归档数据可以迁移到`PostgreSQL`吗？
A：可以。工作区超过100万消息时建议迁移至`PostgreSQL`以获得更好性能。专业版提供迁移工具，一键将SQLite数据导入`PostgreSQL`。

### Q6：定时同步失败如何排查？
A：查看调度日志与告警频道。常见原因包括Token过期（需刷新）、速率限制（降低频率）、网络中断（自动重试3次）。

### Q7：版本回滚会影响新增数据吗？
A：回滚会恢复到指定版本的状态，回滚后新增的数据需要重新同步。建议回滚前先创建当前版本快照。

### Q8：如何对接MCP工具生态？
A：专业版提供MCP端点查询适配，MCP工具通过本工具检索Slack归档。配置MCP server时指定归档数据库路径，MCP端点即可执行只读SQL与检索。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
