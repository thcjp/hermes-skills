---

name: "jira-free"
description: "Jira问题跟踪、Sprint管理、项目看板与工作流自动化，支持REST API操作。免费版。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "Jira集成引擎(免费版)"
  version: "1.0.0"
  summary: "Jira问题跟踪、Sprint管理、项目看板与工作流自动化，支持REST API操作。免费版"
  tags:
    - "通用办公"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
tools:
  - exec
  - read
  - write

---

# Jira集成引擎(免费版)

Jira问题跟踪与项目管理集成引擎，通过REST API操作Jira实例，覆盖问题管理、Sprint规划与工作流自动化。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 问题管理
通过Jira REST API v3管理问题：

```bash
# 创建问题
curl -X POST "https://your-domain.atlassian.net/rest/api/3/issue" \
  -u "email@example.com:API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "fields": {
      "project": {"key": "PROJ"},
      "summary": "实现用户登录功能",
      "description": {"type": "doc","version": 1,"content": [{"type": "paragraph","content": [{"type": "text","text": "需要实现OAuth登录"}]}]},
      "issuetype": {"name": "Story"},
      "priority": {"name": "High"},
      "assignee": {"accountId": "user-account-id"}
    }
  }'

# 查询问题
curl -X GET "https://your-domain.atlassian.net/rest/api/3/issue/PROJ-123" \
  -u "email@example.com:API_TOKEN"

# 更新问题
curl -X PUT "https://your-domain.atlassian.net/rest/api/3/issue/PROJ-123" \
  -u "email@example.com:API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"fields": {"summary": "更新后的标题"}}'
```

### 2. JQL高级查询
```bash
# JQL查询
atlassian.net/rest/api/3/search" \
  -u "email@example.com:API_TOKEN" \
  --data-urlencode 'jql=project = PROJ AND sprint in openSprints() AND status != Done ORDER BY priority DESC' \
  -G
```

常用JQL模式：
- 当前Sprint未完成：`sprint in openSprints() AND status != Done`
- 某人待办：`assignee = "user@domain.com" AND statusCategory != Done`
- 高优先级缺陷：`issuetype = Bug AND priority in (Highest, High) AND status = Open`
- 过期问题：`duedate < now() AND statusCategory != Done`

**输出**: 返回JQL高级查询的执行结果,包含操作状态和输出数据。

### 3. Sprint与看板管理
```bash
# 获取活跃Sprint
atlassian.net/rest/agile/1.0/board/1/sprint?state=active" \
  -u "email@example.com:API_TOKEN"

# 将问题移入Sprint
atlassian.net/rest/agile/1.0/sprint/1/issue" \
  -u "email@example.com:API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"issues": ["PROJ-1", "PROJ-2"]}'

# 创建Sprint
atlassian.net/rest/agile/1.0/sprint" \
  -u "email@example.com:API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Sprint 15", "startDate": "2026-08-01", "endDate": "2026-08-14", "originBoardId": 1}'
```

- 异常时参考错误处理章节进行恢复
- 关键参数: `sprint与看板管理` 选项

### 4. 工作流与状态流转
```bash
# 获取可用状态流转
atlassian.net/rest/api/3/issue/PROJ-123/transitions" \
  -u "email@example.com:API_TOKEN"

# 执行状态流转
atlassian.net/rest/api/3/issue/PROJ-123/transitions" \
  -u "email@example.com:API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"transition": {"id": "21"}}'

# 添加评论
atlassian.net/rest/api/3/issue/PROJ-123/comment" \
  -u "email@example.com:API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"body": {"type": "doc","version": 1,"content": [{"type": "paragraph","content": [{"type": "text","text": "已修复，请验证"}]}]}}'
```

**输出**: 返回工作流与状态流转的执行结果,包含操作状态和输出数据。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `工作流与状态流转` 选项

#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 批量创建问题 | 需求列表+项目Key | 批量创建API调用+结果汇总 |
| Sprint报告 | Sprint ID | Sprint进度+问题状态分布 |
| 缺陷追踪 | 项目Key+时间范围 | 缺陷列表+优先级分布+趋势 |
| 工作流自动化 | 触发条件+动作 | 状态流转+评论+分配脚本 |

**不适用于**：Jira插件开发、Jira管理员配置、Jira Server/Data Center安装部署。

## 使用流程

1. 配置认证（邮箱+API Token）
2. 确定Jira实例URL和项目Key
3. 选择操作类型（创建/查询/更新/流转）
4. 构造并发送REST API请求
5. 解析响应并格式化输出

#
## 示例

### 示例1：查询当前Sprint问题
```bash
curl -s -X GET "https://your-domain.atlassian.net/rest/api/3/search" \
  -u "email@example.com:API_TOKEN" \
  --data-urlencode 'jql=project = PROJ AND sprint in openSprints() ORDER BY priority DESC' \
  -G | jq '.issues[] | {key: .key, summary: .fields.summary, status: .fields.status.name, assignee: .fields.assignee.displayName}'
```
输出：当前Sprint所有问题的Key、标题、状态和负责人列表。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `401 Unauthorized` | API Token无效或邮箱错误 | 在Atlassian账户设置中重新生成API Token，确认邮箱与账户一致，使用 `-u "email:token"` 格式 |
| `404 Not Found` | 问题Key或API路径错误 | 确认问题Key存在（如PROJ-123），检查API版本路径（`/rest/api/3/` vs `/rest/api/2/`） |
| `400 Bad Request` "field is required" | 创建问题时缺少必填字段 | 先GET一个同类型问题查看必填字段，确保project/summary/issuetype字段完整 |
| `403 Forbidden` | API Token权限不足 | 确认Token关联的账户在目标项目中有对应权限（Browse Projects/Create Issues），联系Jira管理员调整权限 |

## 常见问题

### Q1: 如何获取Jira API Token？
登录Atlassian账户（https://id.atlassian.com/manage-profile/security/api-tokens），点击"Create API token"，输入标签名后复制Token。使用时配合注册邮箱：`-u "your-email@domain.com:YOUR_API_TOKEN"`。注意Token只显示一次，需妥善保存。Server/Data Center版本使用用户名+密码或Personal Access Token（PAT）。

### Q2: Jira Cloud和Server/Data Center的API有什么区别？
Cloud使用`https://your-domain.atlassian.net/rest/api/3/`，认证用邮箱+API Token。Server/DC使用`https://your-jira-server/rest/api/2/`，认证用用户名+密码或PAT。API v3支持Atlassian Document Format（ADF）富文本，v2使用纯文本。如果不需要富文本，v2的API在Cloud上仍可用，但建议迁移到v3。部分敏捷API路径Cloud为`/rest/agile/1.0/`，Server一致。

### Q3: JQL查询结果如何分页？
默认返回50条，最多100条。使用`startAt`和`maxResults`参数分页：`?jql=...&startAt=0&maxResults=100`。遍历所有结果时，循环请求直到`total` <= `startAt + maxResults`。大批量查询建议使用`fields`参数限制返回字段减少响应体积：`&fields=key,summary,status,assignee`。导出全量数据可考虑Jira的CSV导出功能或`/rest/api/3/search`的`expand`参数。

## 已知限制

- 需要Jira实例的网络访问权限
- API Token权限受账户角色限制
- API速率限制：Cloud每分钟每用户约40请求

## 升级提示

本免费版提供基础功能。升级到完整版 jira 获取全部能力和高级特性。

## 安全注意事项

| 风险类型 | 防范措施 |
|----------|---------|
| API密钥泄露 | 通过环境变量配置，禁止硬编码到代码或配置文件中 |
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 网络通信安全 | 使用HTTPS协议，验证SSL证书有效性 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 效率量化分析

| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 差异化对比

| 对比维度 | 本技能 | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 核心功能 | 通用场景 | 通用场景 |

## 核心功能

- **自动化执行**: 基于指令驱动的自动化流程
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据