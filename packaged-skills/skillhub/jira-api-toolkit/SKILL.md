---
slug: jira-api-toolkit
name: jira-api-toolkit
version: "1.0.0"
displayName: Jira工具箱(专业版)
summary: 全功能 Jira Cloud 集成，含创建/更新/流转/批量/自动化与多连接管理。
license: Proprietary
edition: pro
description: |-
  全功能 Jira Cloud 集成，含创建/更新/流转/批量/自动化与多连接管理。核心能力：
  - 全部只读能力 + 创建/更新/删除议题
  - 流转议题状态与评论管理
  - 用户搜索与分配
  - 批量操作与自动化工作流
  - 多连接高级管理与优先支持

  适用场景：
  - 团队自动化议题创建与状态同步
  - 项目经理批量流转与分配
  - DevOps 流水线议题状态驱动
  - 企业多团队多 Jira 实例管理

  差异化：相比免费版新增写操作、批量、自动化三大能力，覆盖团队与企业级 Jira 自动化需求，配套多连接管理与优先支持
tags:
- 集成工具
- 项目管理
- 企业效率
- 自动化
tools:
  - - read
- exec
---
# Jira工具箱(专业版)

## 核心能力

| 能力 | 说明 | 免费版 | 专业版 |
|------|------|--------|--------|
| 托管 OAuth 认证 | 自动注入令牌 | 是 | 是 |
| JQL 搜索 | 字段过滤与分页 | 是 | 是 |
| 查看议题详情 | 读取全部字段 | 是 | 是 |
| 项目/类型/状态元数据 | 只读元数据 | 是 | 是 |
| 创建议题 | 新建议题 | 否 | 是 |
| 更新/删除议题 | 修改与删除 | 否 | 是 |
| 流转议题 | 改变状态 | 否 | 是 |
| 评论管理 | 添加/查看评论 | 否 | 是 |
| 用户搜索 | 查找用户 | 否 | 是 |
| 议题分配 | 指派负责人 | 否 | 是 |
| 批量操作 | 批量创建/更新 | 否 | 是 |
| 多连接高级管理 | 多账号切换 | 基础 | 高级 |
| 优先支持 | 优先响应 | 否 | 是 |
### 托管 OAuth 认证

执行托管 OAuth 认证操作,处理用户输入并返回结果。

**输入**: 用户提供托管 OAuth 认证所需的参数和指令。

**输出**: 返回托管 OAuth 认证的处理结果。

- 执行`托管 OAuth 认证`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`托管 OAuth 认证`相关配置参数进行设置
### JQL 搜索

执行JQL 搜索操作,处理用户输入并返回结果。

**输入**: 用户提供JQL 搜索所需的参数和指令。

**输出**: 返回JQL 搜索的处理结果。

- 执行`JQL 搜索`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`JQL 搜索`相关配置参数进行设置
### 查看议题详情

执行查看议题详情操作,处理用户输入并返回结果。

**输入**: 用户提供查看议题详情所需的参数和指令。

**输出**: 返回查看议题详情的处理结果。

- 执行`查看议题详情`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`查看议题详情`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 全功能、Jira、Cloud、含创建、自动化与多连接管、核心能力、全部只读能力、流转议题状态与评、用户搜索与分配、批量操作与自动化、工作流、多连接高级管理与。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景 1：团队自动化议题创建与状态同步
Scrum Master 每周从需求文档批量创建议题，自动分配到对应负责人与冲刺。专业版的批量创建避免逐条手动录入，状态流转配合 CI/CD 实现"代码合并即议题关闭"。

### 场景 2：项目经理批量流转与分配
版本发布后，项目经理批量流转"待发布"议题为"已发布"，批量分配回归测试议题给 QA 团队。专业版的批量操作一次完成，避免逐条点击。

### 场景 3：DevOps 流水线议题状态驱动
CI/CD 流水线在部署成功后自动流转关联议题为"已上线"，部署失败自动添加评论记录失败原因与日志链接。评论管理能力让流水线状态可追溯。

### 场景 4：企业多团队多 Jira 实例管理
企业有多个 Jira 实例（如研发、运维、客服各一套），专业版的多连接高级管理支持按团队切换连接，批量同步跨实例的关联议题。

## 使用流程

> 上手时间：< 120 秒。专业版在免费版只读基础上新增写操作，建议先熟悉只读命令再启用写操作。

### 依赖说明

### 运行环境
1. **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
2. **操作系统**：Windows / macOS / Linux
3. **Node.js**：16+（用于运行 CLI）
4. **cron / 任务计划**：用于自动化触发（Linux 用 cron，Windows 用任务计划程序）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| maton CLI | 命令行工具 | 必需 | `npm install -g @maton/cli` 或 `brew install maton-ai/cli/maton` |
| Jira Cloud 账号 | SaaS 账号 | 必需 | Atlassian 账号，用于 OAuth 授权 |
| Node.js | 运行时 | 必需 | Node.js 官方渠道下载 |
| jq（可选） | 命令行工具 | 可选 | 用于 JSON 结果处理与管道 |

### API Key 配置
5. **maton API Key**：通过 `maton login` 获取，存储于环境变量 `MATON_API_KEY`，禁止硬编码
6. **Jira OAuth 连接**：通过 `maton connection create jira` 在浏览器完成授权
7. **默认连接**：可选设置环境变量 `MATON_DEFAULT_CONNECTION` 指定默认连接
8. **禁止**：在 SKILL.md 或脚本中硬编码 API Key 与 OAuth 令牌

### 可用性分类
9. **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
10. **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务，支持读写操作与自动化工作流

### 命令参数说明

11. `-f44ec481e5e7`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| mode | string | 否 | 处理模式, 可选: json/text/markdown, 默认: 默认值 |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/（根据实际场景填充）`

## 异常处理


| 现象 | 可能原因 | 解决步骤 | 优先级 |
|------|----------|----------|--------|
| 401 Invalid API key | 未登录 / Key 过期 | `maton login` 重新登录 | P1 |
| 400 Missing connection | 未创建 Jira 连接 | `maton connection create jira` | P1 |
| 400 Invalid transition id | 工作流不可达 | `transition list` 获取可用流转 | P2 |
| 400 Invalid accountId | 用户不存在 / 无权限 | `user search` 重新获取 accountId | P2 |
| 429 Rate limited | 超过 10 请求/秒 | 降速、分批、执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 | P2 |
| 204 误判失败 | 204 为成功 | 确认 204 即成功 | P3 |
| Agile API scope 错误 | 缺少 OAuth scope | 联系支持申请扩展 scope | P2 |
| 管道 Invalid API key | 环境变量未展开 | 直接用 CLI 或显式 export | P3 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM执行各步骤的智能处理, 推荐GPT-4/智谱GLM-4/DeepSeek |
| `references/pipeline配置` | 文件 | 是 | 相关说明 |
| `assets/（根据实际场景填充）` | 文件 | 是 | 相关说明 |
| `references/checklist.md` | 文件 | 否 | 相关说明 |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 写操作命令速查

| 命令 | 用途 | 示例 |
|------|------|------|
| `issue create` | 创建议题 | `maton jira issue create --cloud-id abc-123 --project PROJ --summary '标题' --type Task` |
| `issue update` | 更新议题 | `maton jira issue update PROJ-123 --cloud-id abc-123 --summary '新标题'` |
| `issue delete` | 删除议题 | `maton jira issue delete PROJ-123 --cloud-id abc-123` |
| `issue update --assignee` | 分配议题 | `maton jira issue update PROJ-123 --cloud-id abc-123 --assignee <accountId>` |
| `transition list` | 查看可用流转 | `maton jira transition list PROJ-123 --cloud-id abc-123` |
| `transition apply` | 流转状态 | `maton jira transition apply PROJ-123 --cloud-id abc-123 --id 31` |
| `comment add` | 添加评论 | `maton jira comment add PROJ-123 --cloud-id abc-123 --body '评论内容'` |
| `comment list` | 查看评论 | `maton jira comment list PROJ-123 --cloud-id abc-123` |
| `user search` | 搜索用户 | `maton jira user search john --cloud-id abc-123` |

### 创建议题请求体

```json
{
  "fields": {
    "project": {"key": "PROJ"},
    "summary": "修复登录失败",
    "issuetype": {"name": "Task"},
    "priority": {"name": "High"},
    "assignee": {"accountId": "712020:5aff718e-6fe0-4548-82f4-f44ec481e5e7"}
  }
}
```

### 流转议题请求体

```json
{
  "transition": {"id": "31"}
}
```

### 多连接管理

| 命令 | 用途 |
|------|------|
| `maton connection list jira --status ACTIVE` | 列出活跃 Jira 连接 |
| `maton connection create jira` | 创建新连接 |
| `maton connection view {id}` | 查看连接详情 |
| `maton connection delete {id}` | 删除连接 |
| `--connection {id}` | 操作时指定连接 |

## 常见问题

### Q1：创建议题报 400 字段校验错误？

A：(1) `project.key` 必须存在且大写；(2) `issuetype.name` 必须是该项目可用的类型；(3) 必填字段（如 priority）未传。建议先 `issuetype list` 确认可用类型。

### Q2：流转报 400 无效 transition id？

A：transition id 因工作流而异。先 `transition list PROJ-123` 获取该议题可用流转与对应 id，再用返回的 id 流转。

### Q3：分配议题报 400 无效 accountId？

A：(1) `user search` 获取目标用户的 accountId；(2) accountId 格式为 `712020:uuid`；(3) 确保用户在该项目有可分配权限。

### Q4：批量操作触发 429？

A：Jira Cloud 限制 10 请求/秒/账号。建议：(1) 每批 20-50 条，批次间间隔 1 秒；(2) 使用重试机制处理 429；(3) 大批量任务在非高峰时段执行。

### Q5：删除议题后能否恢复？

A：Jira 删除议题默认不可恢复（除非启用回收站）。专业版建议删除前先 `comment add` 记录删除原因，或使用"关闭"替代"删除"。

### Q6：评论支持富文本吗？

A：支持。评论 body 使用 Atlassian Document Format（ADF），可包含段落、列表、代码块等。CLI 的 `--body` 字符串会自动包装为段落。

### Q7：多连接如何默认指定？

A：通过环境变量 `MATON_DEFAULT_CONNECTION` 设置默认连接 id，未指定 `--connection` 时使用默认。适合单人多账号场景。

### Q8：Agile API 报 scope 错误？

A：敏捷 API（看板、冲刺、epic）需额外 OAuth scope。报错时联系 maton 支持并提供所需操作与用例，申请扩展 scope。

### Q9：更新议题返回 204 算成功吗？

A：是。更新、删除、流转成功返回 HTTP 204 No Content，表示操作成功且无返回体。误判为失败是常见错误。

### Q10：专业版支持自动化触发吗？

A：支持。配合 CI/CD 与 cron 可实现自动化：代码合并触发议题流转、定时批量创建周期议题、部署失败自动添加评论等。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖云服务，需要网络连接
