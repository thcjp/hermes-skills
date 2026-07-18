---
slug: grain-crawler-pro
name: grain-crawler-pro
version: "1.0.0"
displayName: 归档检索(专业版)
summary: 全功能 Granola 归档检索，含同步、SQL、转录稿、面板、批量导出。
license: MIT
edition: pro
description: |-
  全功能 Granola 归档检索，含同步、SQL、转录稿、面板、批量导出。

  核心能力：
  - 云端同步（private-api 与 desktop-cache 双来源）
  - 跨笔记只读 SQL 统计查询
  - 会议转录稿与侧边面板读取
  - 批量导出与增量更新
  - 加密源调试前的显式解锁与密钥检查
  - 结构化 JSON 输出与源缺口报告

  适用场景：
  - 企业会议知识库集中检索与分析
  - 跨团队会议决策追踪
  - 研究访谈转录稿深度分析
  - 合规审计与会议纪要归档

  差异化：相比免费版新增同步、SQL、转录稿、面板四大能力，覆盖企业级知识库管理需求，配套源缺口报告与加密源安全调试流程。

  触发关键词：归档检索、会议转录、SQL 查询、同步、granola、批量导出
tags:
- 集成工具
- 知识管理
- 企业效率
- 数据分析
tools:
- read
- exec
---

# 归档检索（专业版）

## 概述

专业版在免费版本地检索能力之上，扩展了云端同步、SQL 统计、转录稿读取、面板数据四大能力，覆盖企业级会议知识库的集中检索与分析场景。配套源缺口报告、加密源安全调试流程与增量更新机制，让团队"同步一次、全员可查"，将分散的会议纪要转化为可查询、可统计的结构化资产。

## 核心能力

| 能力 | 说明 | 免费版 | 专业版 |
|------|------|--------|--------|
| 本地优先检索 | 先用本地归档响应 | 是 | 是 |
| 笔记搜索 | 关键词检索 | 是 | 是 |
| 笔记详情 | 读取单条笔记 | 是 | 是 |
| 新鲜度检查 | 检测归档过期 | 是 | 是 |
| 云端同步 | 双来源拉取最新归档 | 否 | 是 |
| SQL 查询 | 跨笔记只读统计 | 否 | 是 |
| 转录稿读取 | 读取会议转录稿 | 否 | 是 |
| 面板数据 | 读取侧边面板内容 | 否 | 是 |
| 批量导出 | 批量导出笔记 | 否 | 是 |
| 增量更新 | 仅同步变化部分 | 否 | 是 |
| 源缺口报告 | 标注缺失数据来源 | 否 | 是 |
| 加密源安全调试 | 显式解锁与密钥检查 | 否 | 是 |

## 使用场景

### 场景 1：企业会议知识库集中检索
知识管理团队每周从 private-api 同步全公司会议纪要，用 SQL 统计"本周提及'合规'的会议次数与参会人"，生成合规审计周报。专业版的双来源同步确保数据完整，源缺口报告标注未同步的团队。

### 场景 2：跨团队决策追踪
项目经理检索"跨团队""季度规划"关键词，定位涉及多个团队的决策记录，读取转录稿还原讨论过程，明确责任人。SQL 查询统计各团队决策数量与平均决策时长。

### 场景 3：研究访谈深度分析
研究员批量导出访谈转录稿，用 SQL 按"受访者角色"分组统计高频话题，识别共性诉求。面板数据用于交叉验证访谈中提及的数据图表。

### 场景 4：合规审计与纪要归档
审计团队按月批量导出会议纪要归档，SQL 查询"涉及金额 > 100 万"的决策记录，配合转录稿还原决策依据。增量更新确保只同步当月变化，降低存储与时间成本。

## 快速开始

> 上手时间：< 120 秒。专业版支持双来源同步与 SQL 查询，建议先完成一次完整同步。

### 步骤 1：环境与新鲜度检查

```bash
grain-crawler doctor --json
grain-crawler status --json
```

### 步骤 2：按需同步

仅在数据过期或用户明确要求时同步：

```bash
grain-crawler sync --source private-api
grain-crawler sync --source desktop-cache
```

### 步骤 3：有界查询

```bash
grain-crawler search "季度规划"
grain-crawler notes --json
grain-crawler note get <id>
grain-crawler transcripts get <id>
grain-crawler panels get <id>
```

### 步骤 4：只读 SQL 统计

```bash
grain-crawler --json sql "select count(*) as notes from notes;"
grain-crawler --json sql "select title, updated_at from notes where title like '%合规%' order by updated_at desc limit 20;"
```

## 配置示例

### 同步来源参数

| 参数值 | 含义 | 适用场景 |
|--------|------|----------|
| `private-api` | 云端私有 API | 跨设备同步、团队共享 |
| `desktop-cache` | 桌面端缓存 | 本地快速刷新、离线兜底 |

### SQL 查询能力

| 查询类型 | 示例 | 说明 |
|----------|------|------|
| 计数 | `select count(*) as notes from notes;` | 统计笔记总数 |
| 排序 | `select title, updated_at from notes order by updated_at desc limit 20;` | 按时间倒序取最新 |
| 分组 | `select source, count(*) from notes group by source;` | 按来源分组统计 |
| 模糊匹配 | `select title from notes where title like '%合规%';` | 标题模糊检索 |
| 范围 | `select * from notes where updated_at > '2026-07-01';` | 按时间范围筛选 |

> 专业版 SQL 仅支持只读查询（SELECT），禁止 DDL 与 DML，避免误操作归档数据。

### 输出字段扩展

| 字段 | 类型 | 来源 | 说明 |
|------|------|------|------|
| `note_id` | string | notes | 笔记唯一标识 |
| `title` | string | notes | 笔记标题 |
| `updated_at` | string | notes | 最后更新时间 |
| `summary` | string | notes | 内容摘要 |
| `transcript` | string | transcripts | 转录稿全文 |
| `panel_content` | string | panels | 面板内容 |
| `source` | string | notes | 数据来源 |
| `source_gaps` | array | status | 缺失的数据来源列表 |

## 最佳实践

1. **本地优先，按需同步**：所有查询默认走本地归档，仅在 `status` 显示过期或用户明确要求时触发 `sync`，降低云端 API 负载。
2. **双来源互补**：private-api 用于跨设备同步，desktop-cache 用于本地兜底。建议先 private-api 同步，失败时回退 desktop-cache。
3. **有界读取**：单次读取笔记数控制在 50 条以内，转录稿按需读取单条，避免一次性加载过多数据。
4. **SQL 只读**：专业版 SQL 仅支持 SELECT，用于精确计数与排名。复杂统计建议先 `notes --json` 导出再用外部工具分析。
5. **报告绝对日期**：输出时间一律使用绝对日期范围，避免相对表述。源缺口需明确标注缺失的来源与时间段。
6. **加密源安全调试**：在调试加密源前，必须运行显式 unlock / secrets 检查，禁止意外触发 Keychain 弹窗。
7. **增量更新降本**：使用 `sync --incremental` 仅同步变化部分，降低同步时间与存储成本，适合高频同步场景。

## 常见问题

### Q1：同步失败如何处理？

A：(1) 检查网络与 private-api 凭证；(2) 回退 desktop-cache 来源；(3) 查看源缺口报告定位失败来源。专业版会在结果中标注 `source_gaps` 字段。

### Q2：SQL 查询报错"只读模式"？

A：专业版 SQL 仅支持 SELECT。如需更新归档数据，请在 Granola 桌面端操作后重新同步。

### Q3：转录稿读取返回空？

A：(1) 确认该会议已开启转录；(2) 检查转录稿是否已完成处理；(3) 部分旧会议可能无转录稿，`source_gaps` 会标注。

### Q4：面板数据与笔记内容不一致？

A：面板数据可能滞后于笔记正文，建议以 `note get` 的正文为准，面板仅作辅助参考。

### Q5：增量更新如何判断变化？

A：专业版基于 `updated_at` 字段与内容哈希判断变化，仅同步 `updated_at` 更新或哈希不同的笔记。首次同步为全量，后续为增量。

### Q6：加密源调试时为何提示需要解锁？

A：专业版在调试加密源前会显式运行 unlock / secrets 检查，避免意外触发 Keychain 弹窗。请按提示在终端完成解锁后重试。

### Q7：批量导出支持哪些格式？

A：专业版支持 JSON 与 Markdown 两种格式。JSON 适合程序化处理，Markdown 适合人工阅读与归档。

### Q8：源缺口报告如何解读？

A：`source_gaps` 数组列出缺失的数据来源（如 `transcripts`、`panels`）与对应笔记 ID，帮助定位需要补充同步的部分。

### Q9：SQL 查询性能如何优化？

A：(1) 加 `limit` 限制返回行数；(2) 用 `where` 缩小范围；(3) 避免 `select *`，只取需要的字段；(4) 复杂统计先导出再外部分析。

### Q10：专业版是否支持多账号同步？

A：支持。通过 `sync --account <account-id>` 指定账号，适合一人管理多个 Granola 账号的场景。

## 故障排查表

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|------|----------|----------|--------|
| 归档为空 | 未登录 / 未同步 | 桌面端登录后运行 `sync` | P1 |
| 同步失败 | 网络不通 / 凭证失效 | 检查网络与 private-api 凭证，回退 desktop-cache | P1 |
| SQL 报错只读 | 执行了非 SELECT 语句 | 改用 SELECT 查询 | P2 |
| 转录稿为空 | 未开启转录 / 处理中 | 确认转录已开启并完成处理 | P2 |
| 面板数据滞后 | 同步时序问题 | 重新同步或以正文为准 | P3 |
| 加密源弹窗 | 未显式解锁 | 按提示完成 unlock / secrets 检查 | P1 |
| 增量更新无效 | 首次为全量同步 | 第二次运行后增量生效 | P3 |
| 批量导出失败 | 磁盘空间不足 | 清理磁盘或分批导出 | P2 |

## 专业版特性

本专业版相比免费版新增以下能力：
- 云端双来源同步：private-api 与 desktop-cache 互补，确保数据完整
- 跨笔记只读 SQL：精确计数、排名、分组统计，支持复杂查询
- 会议转录稿读取：还原讨论过程，明确决策依据
- 侧边面板数据读取：交叉验证图表与数据
- 批量导出与增量更新：JSON / Markdown 双格式，仅同步变化部分
- 源缺口报告：标注缺失数据来源，定位同步缺口
- 加密源安全调试：显式解锁与密钥检查，避免意外弹窗

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 本地检索 + 笔记搜索 + 详情 + 新鲜度 | 个人试用 |
| 收费专业版 | ¥29.9/月 | 全功能 + 同步 + SQL + 转录稿 + 面板 + 批量 + 优先支持 | 团队 / 企业 |

专业版通过 SkillHub SkillPay 发布。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux（macOS 与 Granola 桌面端兼容性最佳）
- **Python**：3.8+（用于运行命令行工具与 SQL 查询）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| Granola 桌面端 | 应用 | 必需 | 官方渠道下载安装 |
| grain-crawler CLI | 命令行工具 | 必需 | 随 Skill 附带或按文档安装 |
| Python 标准库 | 运行时 | 必需 | Python 自带（json / sqlite3 / subprocess） |
| private-api 凭证 | 凭证 | 推荐 | Granola 账号设置中获取，用于云端同步 |
| SQLite | 数据库 | 必需 | Python 内置 sqlite3 模块，用于 SQL 查询 |

### API Key 配置
- **Granola 账号**：桌面端登录即可
- **private-api 凭证**：存储于环境变量 `GRANOLA_PRIVATE_API_KEY`，建议通过系统密钥管理工具注入，禁止硬编码
- **加密源密钥**：由系统 Keychain 管理，调试前需显式解锁
- **禁止**：在 SKILL.md 或脚本中硬编码凭证与密钥

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务，支持云端同步与 SQL 查询
