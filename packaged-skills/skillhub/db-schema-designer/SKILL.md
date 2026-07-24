---
slug: "db-schema-designer"
name: "db-schema-designer"
version: 1.0.1
displayName: "数据库Schema设计器(专业版)"
summary: "全功能数据库建模工具,支持SQLite/`PostgreSQL`/MySQL多引擎,含性能诊断、版本管理、团队协作与自定义抽取器。"
license: "Proprietary"
edition: "pro"
description: |-
  数据库Schema设计器(专业版)是企业级数据库建模与演进管理工具,在免费版软Schema方法论基础上,扩展多数据库引擎适配、性能诊断、Schema版本管理、团队协作与自定义抽取器等高级能力。核心能力:
  - 支持SQLite、`PostgreSQL`、MySQL三大引擎的统一建模与差异化适配
  - 内置性能诊断引擎,自动识别慢查询、冗余索引、N+1问题
  - Schema版本管理与迁移脚本生成,支持灰度发布与回滚
  - 自定义抽取器模板,支持LLM驱动的结构化数据提取
  - 团队协作模式,支持Schema评审、变更审批、权限分级
  -...
tags:
  - 数据库
  - 建模
  - 性能优化
  - 企业版
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "设计,UI/UX,创意"
category: "Creative"
---
# 数据库Schema设计器(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 数据库Schema设计器(专业版)全功能数据库建模 | 不支持 | 支持 |
| 数据库Schema设计器(专业版)版本管理 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |

## 核心能力

### 多数据库引擎适配
| 引擎 | 软Schema支持 | JSON字段 | FTS方案 | 推荐场景 |
|:-----|:-----|:-----|:-----|:-----|
| SQLite | 完整支持 | JSON1扩展 | FTS5+LIKE回退 | 单机/嵌入式/原型 |
| `PostgreSQL` | 完整支持 | JSONB原生 | pg_trgm+tsvector | 中大型在线业务 |
| MySQL | 完整支持 | JSON类型 | ngram全文索引 | 已有MySQL技术栈 |

统一建模层通过方言适配器,自动生成对应引擎的DDL语句:

```text
┌─────────────────────────────────────────────────────────┐
│  统一建模层(逻辑Schema定义)                              │
│  - 主干字段 / 软字段 / 业务视图 / 索引策略               │
└─────────────────────────────────────────────────────────┘
              │                    │                │
              ▼                    ▼                ▼
     ┌──────────────┐    ┌────────────────┐  ┌──────────────┐
     │ SQLite方言    │    │ PostgreSQL方言  │  │ MySQL方言     │
     │ (JSON1+FTS5) │    │ (JSONB+pg_trgm)│  │ (JSON+ngram) │
     └──────────────┘    └────────────────┘  └──────────────┘
```

**输入**: 用户提供多数据库引擎适配所需的指令和必要参数.
**处理**: 解析多数据库引擎适配的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 性能诊断引擎

自动识别以下问题并给出优化建议:

| 诊断项 | 检测方式 | 优化建议 |
|---:|---:|---:|
| 慢查询 | EXPLAIN QUERY PLAN分析 | 添加索引、重写SQL、拆分查询 |
| 冗余索引 | 索引使用率统计 | 合并或删除低效索引 |
| N+1查询 | 查询日志模式识别 | 改用JOIN或批量预取 |
| JSON深扫 | 查询路径分析 | 提取高频字段到键值对表 |
| 全表扫描 | EXPLAIN输出 | 建立合适索引或分区 |

### Schema版本管理
```bash
# 初始化版本库
schema-designer init --db data/flexible.db
# ...
# 生成迁移脚本(基于差异)
schema-designer diff --from v1.2.0 --to v1.3.0 --output migrations/
# ...
# 应用迁移(支持灰度)
schema-designer migrate --target v1.3.0 --strategy rolling
# ...
# 回滚到指定版本
schema-designer rollback --to v1.2.0 --backup-dir data/backups/
```

版本管理特性:
- 每次变更生成带语义化版本号的迁移脚本
- 支持前向迁移与回滚迁移双向脚本
- 灰度发布:按比例逐步应用变更,降低风险
- 变更审计:记录操作人、时间、影响范围

**处理**: 解析Schema版本管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 自定义抽取器

支持通过模板定义字段抽取逻辑,可集成LLM实现智能提取:

```python
# 示例
def extract_policy(raw_content: str) -> dict:
    """从政策原文抽取结构化字段"""
    return {
        "title": extract_title(raw_content),
        "release_date": extract_date(raw_content),
        "issuing_org": extract_org(raw_content),
        "policy_type": classify_policy(raw_content),
        "subsidy_amount": extract_amount(raw_content),
    }
# ...
# LLM驱动抽取器(通过Agent平台内置LLM)
def extract_with_llm(raw_content: str, schema: dict) -> dict:
    """使用LLM按schema抽取结构化数据"""
    prompt = f"按以下schema抽取信息: {schema}\n原文: {raw_content}"
    # 调用Agent平台LLM接口
    ...
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `自定义抽取器` 选项
- 处理流程: 接收输入 -> 执行自定义抽取器 -> 返回结果
- 输入: 用户提供自定义抽取器所需的参数和指令
- 输出: 返回自定义抽取器的处理结果,包含执行状态码、结果数据和执行日志

### 团队协作模式
| 角色 | 权限 | 典型操作 |
|:---:|:---:|:---:|
| Owner | 全部权限 | 审批变更、管理成员 |
| DBA | Schema管理 | 执行迁移、性能诊断 |
| Developer | 只读+提议 | 提交Schema变更提议 |
| Auditor | 只读 | 查看变更历史、合规审计 |

协作流程:
1. Developer提交Schema变更提议(含影响分析)
2. DBA评审技术方案,标记风险点
3. Owner审批通过后生成迁移脚本
4. 灰度发布,观察性能指标
5. 全量应用,记录审计日志

#
## 适用场景

### 场景1 -中大型项目从SQLite迁移到`PostgreSQL`

用户意图: "我们的知识库从SQLite迁到`PostgreSQL`,要保留软Schema能力。"

适配要点:
- `JSON`字段改为`JSONB`(支持GIN索引,查询性能更好)
- FTS5替换为`pg_trgm`+`tsvector`
- 键值对表结构不变,索引策略调整
- 通过`schema-designer diff`生成迁移脚本

### 场景2 -团队Schema治理

用户意图: "多人协作开发,Schema变更经常冲突,需要治理流程。"

实施方案:
- 启用团队协作模式,设置角色权限
- 所有变更走提议-评审-审批流程
- 启用版本管理,每次变更生成迁移脚本
- 性能诊断作为评审必检项

### 场景3 -数据中台性能优化

用户意图: "知识库查询变慢了,需要诊断优化。"

诊断步骤:
1. 运行`schema-designer diagnose --db data/flexible.db`
2. 查看慢查询报告与索引使用率
3. 根据建议提取高频JSON字段到键值对表
4. 重建索引,观察性能指标

### 场景4 -合规审计下的Schema追溯

用户意图: "审计要求能追溯任意时点的Schema结构。"

实施方案:
- 启用版本管理,每次变更留存快照
- 通过`schema-designer history`查看完整变更链
- 导出审计报告(含操作人、时间、影响范围)

## 使用流程

### 第1步:初始化项目

```bash
# 创建项目目录
mkdir -p my-knowledge-base/{data,scripts,migrations}
cd my-knowledge-base
# ...
# 初始化Schema版本库
schema-designer init --engine postgresql --db "postgresql://user:pass@localhost/kb"
```

### 第2步:Discovery需求澄清

Agent主动向用户确认数据来源、主干字段、软字段、查询需求、数据量级等(同免费版Discovery流程,但支持多引擎选项).
### 第3步:生成多引擎DDL

```bash
# 生成SQLite版本
schema-designer generate --template knowledge_base --engine sqlite --output ddl/sqlite.sql
# ...
# 生成PostgreSQL版本
schema-designer generate --template knowledge_base --engine postgresql --output ddl/postgres.sql
# ...
# 生成MySQL版本
schema-designer generate --template knowledge_base --engine mysql --output ddl/mysql.sql
```

### 第4步:应用并验证

```bash
# 应用Schema
schema-designer apply --engine postgresql --ddl ddl/postgres.sql
# ...
# 运行性能基线测试
schema-designer baseline --workload （请参考skill目录中的脚本文件）
# ...
# 归档测试数据
schema-designer archive --source manual --content "测试数据" --extractor extract_policy
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:------|------:|:------|:------|
| content | string | 否 | db-schema-designer处理的内容输入 |,  |
| content | string | 否 | db-schema-designer处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "designer 相关配置参数",
    result: "designer 相关配置参数",
    result: "designer 相关配置参数",
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
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+(运行schema-designer CLI)
- **数据库**: SQLite 3.35+ / `PostgreSQL` 12+ / MySQL 8.0+

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------:|--------|:-------|:------:|
| schema-designer | CLI工具 | 必需 | `pip install schema-designer` |
| psycopg2 | Python库 | `PostgreSQL`必需 | `pip install psycopg2-binary` |
| pymysql | Python库 | MySQL必需 | `pip install pymysql` |
| pypdf | Python库 | 可选 | `pip install pypdf`(PDF提取) |
| jieba | Python库 | 可选 | `pip install jieba`(中文分词) |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- **数据库连接**: 通过环境变量`DATABASE_URL`配置,禁止硬编码
- **LLM抽取器**: 使用Agent平台内置LLM,或配置`LLM_API_KEY`环境变量
- **Schema版本库**: 本地存储于`data/schema_versions/`,无需额外Key
- **禁止**: 在SKILL.md或脚本中硬编码任何凭证

### 可用性分类
- **分类**: MD+EXEC+CLI(Markdown指令+命令行工具+数据库操作)
- **说明**: 基于Markdown的AI Skill，部分高级功能需要schema-designer CLI

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

### Q1: 从免费版升级到专业版,现有数据需要迁移吗?

A: 不需要。专业版兼容免费版的Schema结构,直接安装专业版即可使用高级功能,现有数据无损升级.
### Q2: 多引擎适配时,JSON字段类型怎么选?

A: SQLite用JSON1扩展(文本存储), `PostgreSQL`用JSONB(二进制存储,支持GIN索引,查询更快), MySQL用JSON类型。统一逻辑层会自动映射.
### Q3: 性能诊断会拖慢生产数据库吗?

A: 不会。诊断默认走只读副本或采样模式,EXPLAIN QUERY PLAN不执行实际查询。建议在低峰期运行完整诊断.
### Q4: 灰度发布时如何处理新旧Schema共存?

A: 通过视图层屏蔽差异,新字段允许NULL,旧版本写入时忽略新字段。全量应用后再添加NOT NULL约束.
### Q5: Schema回滚会丢失数据吗?

A: 不会。回滚前自动备份受影响数据到`data/backups/`,回滚仅恢复Schema结构,数据保留。如需恢复数据,从备份目录还原.
### Q6: 自定义抽取器如何调试?

A: 使用`schema-designer test-extractor --extractor my_extractor --input sample.txt`单独测试抽取器,查看输出与预期差异,支持逐步断点调试.
### Q7: 团队协作模式下,如何处理冲突的Schema变更?

A: 通过PR评审流程合并冲突变更,版本管理工具会检测冲突并提示合并方案。无法自动合并时,由DBA人工裁决.
### Q8: 如何导出Schema审计报告?

A: 运行`schema-designer audit --from 2026-01-01 --to 2026-06-30 --format pdf --output audit.pdf`,支持PDF、HTML、CSV三种格式.
### Q9: 增量同步如何保证多环境一致性?

A: 通过校验和(checksum)比对各环境Schema快照,差异项生成同步脚本,应用后再次校验,确保一致.
### Q10: 专业版支持哪些LLM抽取器?

A: 支持Agent平台内置LLM,以及OpenAI兼容接口的自定义LLM。配置时填写API endpoint和key即可.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

