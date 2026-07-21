---
slug: format-converter
name: format-converter
version: "1.0.0"
displayName: 数据格式转换(专业版)
summary: 全功能数据格式转换平台,支持批量、流式、自定义映射、定时任务与企业数据库导入导出。
license: Proprietary
edition: pro
description: |-
  数据格式转换专业版面向需要在大规模数据与多源系统间进行格式转换的专业开发者与数据工程师,提供完整的批量、流式、自动化转换能力。核心能力:
  - 涵盖免费版全部能力,无文件大小与数量限制
  - 批量转换:目录级批量处理,支持通配符与递归
  - 流式转换:大文件分块读取与流式输出,支持 GB 级
  - 自定义字段映射:重命名、过滤、合并、拆分字段
  - 转换模板保存与复用:常见场景一键复用
  - 定时转换任务:cron 调度,自动监听与转换
  - 企业数据库导入导出:`PostgreSQL`/MySQL/ClickHouse 数据 ↔ 任...
tags:
  - 格式转换
  - 批量处理
  - 企业集成
  - 集成工具
tools:
  - read
  - exec
---
# 数据格式转换(专业版)

## 核心能力

### 2.1 全格式支持(免费版基础 + 扩展)
| 主流格式 | 扩展格式 |
|----------|----------|
| CSV / JSON / YAML / XML / TOML | Parquet / Avro / MessagePack / Protobuf / Excel(xlsx) |

**输入**: 用户提供1 全格式支持(免费版基础 + 扩展)所需的指令和必要参数。
**处理**: 按照skill规范执行1 全格式支持(免费版基础 + 扩展)操作,遵循单一意图原则。
**输出**: 返回1 全格式支持(免费版基础 + 扩展)的执行结果,包含操作状态和输出数据。

### 2.2 批量转换
- **目录级处理**:对整个目录的所有匹配文件批量转换
- **通配符支持**:`*.json` / `config_*.yaml` 等
- **递归处理**:可选是否递归子目录
- **并行执行**:多文件并行转换,默认 4 线程
- **失败隔离**:单文件失败不影响其他文件,记录到错误日志
- **进度监控**:实时显示转换进度与预估剩余时间

**输入**: 用户提供2 批量转换所需的指令和必要参数。
**输出**: 返回2 批量转换的执行结果,包含操作状态和输出数据。

### 2.3 流式转换

- **分块读取**:大文件按 chunk 读取,避免内存溢出
- **流式输出**:边读边写,支持 GB 级文件
- **内存监控**:实时监控内存,超阈值自动溢写磁盘
- **断点续转**:转换中断后可从断点继续
- **格式适配**:JSON Lines(NDJSON)、CSV 流式、XML SAX 等

### 2.4 自定义字段映射

```yaml
mapping:
  rename:
    user_name: username       # 重命名
    created_at: created_time
  filter:                      # 过滤字段
    - internal_id
    - debug_flag
  merge:                       # 合并字段
    full_name:
      from: [first_name, last_name]
      sep: " "
  split:                       # 拆分字段
    name_parts:
      from: full_name
      sep: " "
      to: [first, last]
  transform:                   # 类型转换
    age: int
    price: float
    is_active: bool
```

### 2.5 转换模板保存与复用

- **模板库**:常见场景保存为模板(如"YAML 配置迁移到 TOML")
- **参数化**:模板支持参数,如输入目录、输出目录、字段映射
- **版本管理**:模板版本化,支持回滚
- **团队共享**:模板可在团队内共享

### 2.6 定时转换任务

- **cron 调度**:标准 5 段式 cron 表达式
- **文件监听**:监听目录变化,新文件自动转换
- **任务依赖**:多任务编排,前序任务完成触发后序
- **失败重试**:指数退避,最多 3 次
- **审计日志**:任务执行历史完整留痕

### 2.7 企业数据库导入导出
- **`PostgreSQL`**:支持 COPY 命令高速导入导出
- **MySQL**:支持 LOAD DATA INFILE
- **ClickHouse**:支持高性能批量插入
- **表 ↔ 文件**:数据库表直接导出为 CSV/JSON/Parquet
- **文件 ↔ 表**:文件直接导入到指定表
- **类型映射**:数据库类型与目标格式类型自动映射

**输入**: 用户提供7 企业数据库导入导出所需的指令和必要参数。
**处理**: 按照skill规范执行7 企业数据库导入导出操作,遵循单一意图原则。

### 2.8 验证与对账

- **行数校验**:转换前后行数必须一致(除非显式过滤)
- **字段校验**:字段数量与名称一致性检查
- **哈希校验**:可选字段值哈希对比
- **抽样校验**:大数据集抽样对比
- **差异报告**:不匹配项生成详细差异报告

## 适用场景

### 3.1 按角色场景矩阵

| 角色 | 场景 | 关键能力 | 输出形态 |
|------|------|----------|----------|
| 数据工程师 | ETL 流程格式适配 | 流式转换 + 字段映射 | 目标格式文件 |
| 后端开发者 | 多系统数据同步 | 定时任务 + 数据库导入导出 | 数据库表 + 文件 |
| 运维工程师 | 配置文件批量迁移 | 批量转换 + 模板复用 | 转换后配置目录 |
| BI 工程师 | 数据仓库导出分析 | `PostgreSQL` → Parquet | Parquet 数据集 |

### 示例

```text
1. 监听 `input/` 目录新增 JSON 文件
2. 自动触发转换任务
3. 流式读取 JSON,按字段映射重命名/过滤/合并
4. 流式输出 CSV 到 `output/` 目录
5. 校验行数与字段一致性
6. 生成差异报告(如有)
7. 任务执行日志写入审计表
```

## 使用流程

预计上手时间:**< 120 秒**(批量与数据库任务需配置)。

### 4.1 批量转换

```text
请批量转换 ./configs 目录下所有 YAML 文件为 TOML:
- 递归子目录
- 输出到 ./configs_toml/
- 保留目录结构
- 并行 4 线程
- 失败的文件记录到 errors.log
```

### 4.2 大文件流式转换

```text
请流式转换 large.json(约 5GB)为 CSV:
- 分块读取,每块 100000 行
- 嵌套字段以点号展开
- 流式输出到 large.csv
- 内存监控,超 4GB 自动溢写磁盘
- 支持断点续转
```

### 4.3 数据库导出

```text
请把 PostgreSQL 的 sales 表导出为 Parquet:
- 数据源: 凭证从环境变量读取
- 表: sales(2024 年全量)
- 输出: sales_2024.parquet
- 分区: 按月分区(partition=YYYY-MM)
- 压缩: snappy
```

### 4.4 自定义字段映射

```text
请转换 users.json 为 csv,应用以下映射:
- 重命名: user_name → username
- 过滤: 排除 internal_id、debug_flag
- 合并: first_name + last_name → full_name
- 类型: age 转 int,price 转 float
```

### 4.5 定时任务

```text
请配置定时转换任务:
- 监听 ./input/ 目录
- 触发: 新增 *.json 文件
- 转换: JSON → CSV(应用模板 yaml_config)
- 输出: ./output/{原文件名}.csv
- 校验: 行数一致性
- 失败: 重试 3 次,仍失败则告警
```

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
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 依赖说明

### 运行环境

- **Agent 平台**: 任意支持 SKILL.md 的 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.11+(tomllib 内置)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| pyyaml | Python 库 | 必需 | `pip install pyyaml`(YAML) |
| xmltodict | Python 库 | 必需 | `pip install xmltodict`(XML) |
| tomli_w | Python 库 | 必需 | `pip install tomli_w`(TOML 写入) |
| tomllib | Python 库 | 必需 | Python 3.11+ 内置(TOML 读取) |
| chardet | Python 库 | 可选 | `pip install chardet`(编码检测) |
| pyarrow | Python 库 | 可选 | `pip install pyarrow`(Parquet) |
| openpyxl | Python 库 | 可选 | `pip install openpyxl`(Excel) |
| msgpack | Python 库 | 可选 | `pip install msgpack`(MessagePack) |
| sqlalchemy | Python 库 | 可选 | `pip install sqlalchemy`(数据库) |
| psycopg2 | Python 库 | 可选 | `pip install psycopg2-binary`(`PostgreSQL`) |
| clickhouse-driver | Python 库 | 可选 | `pip install clickhouse-driver`(ClickHouse) |
| watchdog | Python 库 | 可选 | `pip install watchdog`(文件监听) |
| redis | Python 库 | 可选 | `pip install redis`(任务队列) |
| apscheduler | Python 库 | 可选 | `pip install apscheduler`(定时任务) |

### API Key 配置

- **数据库凭证**: 通过 `DB_HOST`/`DB_USER`/`DB_PASSWORD` 等环境变量传入
- **对象存储**: 通过 `OSS_ACCESS_KEY`/`OSS_SECRET_KEY` 等环境变量传入
- **任务队列**: 通过 `REDIS_URL` 环境变量传入
- **禁止**: 在 SKILL.md、脚本、配置文件中硬编码任何凭证
- **推荐路径**: 凭证统一存放在 `d:\skills\.skill-credentials\` 目录(已 gitignore)

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言驱动的 AI Skill,集成批量、流式、自动化与企业集成的完整转换生产线

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1: 专业版支持多大的文件?

A: 流式转换支持 GB 级文件。批量转换无文件数量上限,受限于磁盘空间。

### Q2: 批量转换失败如何排查?

A: 查看 `errors.log`,包含失败文件路径与错误原因。失败文件不影响其他文件转换。

### Q3: 流式转换是否支持断点续传?

A: 支持。转换中断后可从断点继续,已转换部分不重复处理。

### Q4: 字段映射支持哪些操作?

A: 支持重命名、过滤、合并、拆分、类型转换。详见配置示例。

### Q5: 数据库导出是否支持分区?

A: 支持。可按日期、类别等字段分区输出,便于后续分析。

### Q6: 转换前后数据如何校验?

A: 自动校验行数一致性与字段名称一致性,可选字段值哈希对比,生成差异报告。

### Q7: 模板是否支持参数?

A: 支持。模板可参数化,如输入目录、输出目录、字段映射等。

### Q8: 是否支持 MCP工具扩展?

A: 专业版支持通过 MCP工具协议接入外部存储与计算后端,可在 `mcp_servers` 配置块中注册 MCP server 与 MCP端点,融入 MCP生态共享转换能力。

### Q9: 多源数据如何同步?

A: 通过定时任务监听源目录或源表变化,自动触发转换与同步。

### Q10: 凭证如何安全存储?

A: 凭证统一通过环境变量传入,**禁止**硬编码;推荐存放于 `d:\skills\.skill-credentials\` 目录(已 gitignore)。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
