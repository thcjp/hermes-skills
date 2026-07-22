---
slug: "grain-crawler"
name: "grain-crawler"
version: "1.0.0"
displayName: "归档检索(专业版)"
summary: "全功能 Granola 归档检索，含同步、SQL、转录稿、面板、批量导出。"
license: "Proprietary"
edition: "pro"
description: |-
  全功能 Granola 归档检索。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - 集成工具
  - 知识管理
  - 企业效率
  - 数据分析
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 归档检索(专业版)

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
### 本地优先检索

执行本地优先检索操作,处理用户输入并返回结果。

**输入**: 用户提供本地优先检索所需的参数和指令。

**输出**: 返回本地优先检索的处理结果。

- 执行`本地优先检索`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`本地优先检索`相关配置参数进行设置
### 笔记搜索

执行笔记搜索操作,处理用户输入并返回结果。

**输入**: 用户提供笔记搜索所需的参数和指令。

**输出**: 返回笔记搜索的处理结果。

- 执行`笔记搜索`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`笔记搜索`相关配置参数进行设置
### 笔记详情

执行笔记详情操作,处理用户输入并返回结果。

**输入**: 用户提供笔记详情所需的参数和指令。

**输出**: 返回笔记详情的处理结果。

- 执行`笔记详情`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`笔记详情`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 全功能、Granola、归档检索、含同步、Use、需要提升效率、自动化流程、批量处理、工作流优化时使用、不适用于需要人工、创意判断的任务、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景 1：企业会议知识库集中检索
知识管理团队每周从 private-api 同步全公司会议纪要，用 SQL 统计"本周提及'合规'的会议次数与参会人"，生成合规审计周报。专业版的双来源同步确保数据完整，源缺口报告标注未同步的团队。

### 场景 2：跨团队决策追踪
项目经理检索"跨团队""季度规划"关键词，定位涉及多个团队的决策记录，读取转录稿还原讨论过程，明确责任人。SQL 查询统计各团队决策数量与平均决策时长。

### 场景 3：研究访谈深度分析
研究员批量导出访谈转录稿，用 SQL 按"受访者角色"分组统计高频话题，识别共性诉求。面板数据用于交叉验证访谈中提及的数据图表。

### 场景 4：合规审计与纪要归档
审计团队按月批量导出会议纪要归档，SQL 查询"涉及金额 > 100 万"的决策记录，配合转录稿还原决策依据。增量更新确保只同步当月变化，降低存储与时间成本。

## 使用流程

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

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态


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


| 现象 | 可能原因 | 解决步骤 | 优先级 |
|------|----------|----------|--------|
| 归档为空 | 未登录 / 未同步 | 桌面端登录后运行 `sync` | P1 |
| 同步失败 | 网络不通 / 凭证失效 | 执行ping命令测试网络连通性,检查防火墙和代理设置与 private-api 凭证，回退 desktop-cache | P1 |
| SQL 报错只读 | 执行了非 SELECT 语句 | 改用 SELECT 查询 | P2 |
| 转录稿为空 | 未开启转录 / 处理中 | 确认转录已开启并完成处理 | P2 |
| 面板数据滞后 | 同步时序问题 | 重新同步或以正文为准 | P3 |
| 加密源弹窗 | 未显式解锁 | 按提示完成 unlock / secrets 检查 | P1 |
| 增量更新无效 | 首次为全量同步 | 第二次运行后增量生效 | P3 |
| 批量导出失败 | 磁盘空间不足 | 清理磁盘或分批导出 | P2 |

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux（macOS 与 Granola 桌面端兼容性优秀）
- **Python**：3.8+（用于运行命令行工具与 SQL 查询）

### 依赖说明
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

## 案例展示

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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
