---
slug: "linear-sync"
name: "linear-sync"
version: "1.0.0"
displayName: "Linear同步(专业版)"
summary: "全功能Linear管理工具，支持任务全生命周期、批量操作、GraphQL API与Git集成"
license: "Proprietary"
edition: "pro"
description: |-
  Linear同步工具专业版是面向研发团队的完整项目管理命令行方案，在免费版基础上解锁任务全生命周期管理、批量操作、文档管理、里程碑管理、GraphQL API直接调用和Git集成等全部高级能力。核心能力：任务创建/更新/删除/评论全生命周期、批量任务操作、Linear文档管理、项目里程碑管理、GraphQL原始查询、Git分支创建与PR关联、任务状态自动流转、团队与项目管理全量操作
tags:
  - 任务管理
  - 项目协作
  - Git集成
  - 高级集成
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# Linear同步(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 能力模块 | 支持 | 支持 |
| :--------- | 不支持 | 支持 |
| :----- | 不支持 | 支持 |
| 任务列表 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 专业版支持 | 说明 |
|:---------|:-----------|:-----|
| 任务列表 | 全量 | 按状态、团队、分配者过滤 |
| 任务详情 | 全量 | 查看完整信息和评论 |
| 任务创建 | 全量 | 标题、描述、状态、优先级、分配者 |
| 任务更新 | 支持 | 修改标题、状态、优先级等字段 |
| 任务删除 | 支持 | 安全删除（需确认） |
| 任务评论 | 支持 | 添加、查看和回复评论 |
| 任务流转 | 支持 | start开始、PR创建、状态切换 |
| 批量操作 | 支持 | 批量创建、更新和状态变更 |
| 文档管理 | 支持 | 创建、查看、更新和删除文档 |
| 里程碑管理 | 支持 | 创建和查看项目里程碑 |
| 项目管理 | 全量 | 创建、查看、更新项目 |
| 团队管理 | 全量 | 列出、创建、删除、成员管理 |
| GraphQL API | 支持 | 直接执行GraphQL查询和变更 |
| Git集成 | 支持 | 分支创建、PR关联 |
| 配置管理 | 全量 | 环境变量和TOML配置文件 |
### 能力模块

执行能力模块,自动处理参数解析、任务调度和结果格式化,返回结构化输出。

**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项。

**输出**: 返回能力模块的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`能力模块`相关配置参数进行设置
### 任务列表

执行任务列表,自动处理参数解析、任务调度和结果格式化,返回结构化输出。

**输入**: 用户提供任务列表相关的配置参数、输入数据和处理选项。

**输出**: 返回任务列表的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`任务列表`相关配置参数进行设置
### 任务详情

执行任务详情,自动处理参数解析、任务调度和结果格式化,返回结构化输出。

**输入**: 用户提供任务详情相关的配置参数、输入数据和处理选项。

**输出**: 返回任务详情的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`任务详情`相关配置参数进行设置
#
## 适用场景

### 开发者场景：任务开发全流程

从领取任务到创建PR的完整开发工作流自动化：

```bash
# 1. 查看分配给自己的任务
linear issue list -a self -s started

# 2. 开始开发任务（自动创建分支）
linear issue start ABC-123

# 3. 创建PR关联任务
linear issue pr

# 4. 添加评论记录进度
linear issue comment add ABC-123 -b "已完成核心逻辑，待代码审查"

# 5. 更新任务状态
linear issue update ABC-123 -s "In Review"
```

### 项目经理场景：批量任务管理

批量创建和管理项目任务，提升团队协作效率：

```bash
# 批量创建任务（通过脚本循环）
for task in "实现登录页" "实现注册页" "实现密码重置"; do
  linear issue create -t "$task" -d "需求描述" -s "Backlog" --priority 2
done

# 查看项目所有任务的状态分布
linear issue list -A | grep -oP 'Status: \K\S+' | sort | uniq -c

# 查看项目里程碑
linear milestone list --project <projectId>

# 创建新项目
linear project create -n "Q1迭代" -t ENG -s started --target-date 2026-03-31
```

### 技术负责人场景：GraphQL自定义查询

通过GraphQL API执行CLI未覆盖的高级查询：

```bash
# 导出GraphQL schema用于参考
linear schema -o /tmp/linear-schema.graphql

# 查询当前用户信息
linear api '{ viewer { id name email } }'

# 带变量查询
linear api 'query($teamId: String!) { team(id: $teamId) { name } }' \
  --variable teamId=abc123

# 复杂过滤查询
linear api 'query($filter: IssueFilter!) { issues(filter: $filter) { nodes { title } } }' \
  --variables-json '{"filter": {"state": {"name": {"eq": "In Progress"}}}}'

# 获取前5个任务的标题
linear api '{ issues(first: 5) { nodes { identifier title } } }' | jq '.data.issues.nodes[].title'
```

### 文档管理场景：项目文档协同

创建和管理Linear中的项目文档：

```bash
# 列出所有文档
linear document list

# 从文件创建文档
linear document create --title "设计规格" --content-file ./spec.md --project <projectId>

# 查看文档
linear document view <slug>

# 更新文档内容
linear document update <slug> --content-file ./updated-spec.md

# 删除文档
linear document delete <slug> -y
```

## 使用流程

### 前置条件

1. 已安装`linear`命令行工具
2. 已在Linear设置中创建API Key
3. 已完成认证和项目配置

### 依赖说明

### 运行环境

4. **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
5. **操作系统**：Windows / macOS / Linux
6. **linear CLI**：已安装并通过认证
7. **Git**：已配置（Git集成功能需要）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| linear CLI | 命令行工具 | 必需 | 通过包管理器安装 |
| Linear账户 | 在线账户 | 必需 | 在Linear官网注册 |
| Linear API Key | 认证凭据 | 必需 | 在Linear设置中创建 |
| Git | 版本控制 | 可选 | Git集成功能需要 |
| jq | 命令行工具 | 可选 | GraphQL结果处理时使用 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置

8. **Linear API Key**：在Linear网页端设置 → 账户 → 安全中创建
9. **存储方式**：通过`linear auth login`命令安全存储，或通过环境变量`LINEAR_API_KEY`配置
10. **Token获取**：通过`linear auth token`命令获取当前认证Token（用于curl直接调用）
11. **禁止**：在代码或配置文件中明文写入API Key或Token
12. **权限管理**：API Key的权限范围在Linear设置中控制，建议遵循最小权限原则

### 可用性分类

13. **分类**：MD+EXEC（纯Markdown指令，需要exec命令行执行能力）
14. **说明**：基于Markdown的AI Skill，通过自然语言指令驱动Agent执行Linear全量命令行操作

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | linear-sync处理的内容输入 |, 默认: 全部维度 |
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

| 症状 | 可能原因 | 解决方案 | 优先级 |
|:-----|:---------|:---------|:-------|
| 认证失败 | API Key过期或权限不足 | 重新创建API Key，检查权限范围 | 高 |
| 查询返回空 | 团队ID配置错误 | 检查`.linear.toml`的`team_id` | 高 |
| 创建任务报错 | 必填字段缺失 | 确保提供标题(-t)和描述(-d) | 中 |
| GraphQL报错 | 查询语法错误 | 对照Schema检查字段名和类型 | 中 |
| issue start失败 | Git未配置或仓库问题 | 检查Git远程配置和VCS设置 | 中 |
| issue pr创建失败 | 仓库未关联Linear | 在Linear设置中配置Git集成 | 中 |
| 批量操作触发429 | API速率限制 | 添加请求间隔，降低并发 | 中 |
| 文档创建失败 | 项目ID错误 | 通过`project list`确认项目ID | 低 |
| 里程碑创建失败 | 日期格式错误 | 使用YYYY-MM-DD格式 | 低 |
| 配置不生效 | 文件路径错误 | 确认配置文件在查找路径中 | 低 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行智能审查, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

## 案例展示

### 任务全生命周期管理

```bash
# 创建任务（完整参数）
linear issue create \
  -t "修复支付bug" \
  -d "用户支付时出现500错误" \
  -s "In Progress" \
  -a self \
  --priority 1

# 更新任务字段
linear issue update ABC-123 -s "Done" -t "已修复支付bug"
linear issue update ABC-123 --priority 2

# 开始开发任务
linear issue start ABC-123

# 创建PR关联任务
linear issue pr

# 添加评论
linear issue comment add ABC-123 -b "修复方案：添加异常处理和重试机制"

# 删除任务（需确认）
linear issue delete ABC-123 -y
```

### 批量操作

```bash
# 批量创建任务
for task in "登录页" "注册页" "首页" "个人中心"; do
  linear issue create -t "实现${task}" -d "开发${task}前端页面" -s "Backlog" --priority 2
done

# 批量更新状态（使用GraphQL）
linear api 'mutation {
  issueUpdate(id: "ABC-123", input: {stateId: "done-state-id"}) { success }
}'

# 批量查询任务状态
linear issue list -A --format json | jq '.[] | {id: .id, title: .title, state: .state.name}'
```

### 文档管理

```bash
# 列出文档
linear document list

# 创建文档（从文件）
linear document create \
  --title "技术设计文档" \
  --content-file ./design.md \
  --project <projectId>

# 创建文档（直接内容）
linear document create \
  --title "会议纪要" \
  --content "# 周会纪要\n\n## 议题\n1. 进度同步\n2. 风险评估" \
  --project <projectId>

# 查看文档
linear document view <slug>

# 更新文档
linear document update <slug> --content-file ./updated.md

# 删除文档
linear document delete <slug> -y
```

### 里程碑与项目管理

```bash
# 列出项目
linear project list

# 创建项目
linear project create \
  -n "Q1产品迭代" \
  -t ENG \
  -s started \
  --target-date 2026-03-31

# 查看项目里程碑
linear milestone list --project <projectId>

# 创建里程碑
linear milestone create -n "MVP发布" --project <projectId> --target-date 2026-02-15

# 查看项目更新
linear project-update list --project <projectId>
```

### 团队管理

```bash
# 列出团队
linear team list

# 查看团队成员
linear team members

# 查看团队信息
linear team view ENG

# 查看团队标签
linear label list
```

### GraphQL API直接调用

```bash
# 导出Schema用于参考
linear schema -o /tmp/linear-schema.graphql

# 搜索Schema中的特定类型
grep -i "cycle" /tmp/linear-schema.graphql
grep -A 30 "^type Issue " /tmp/linear-schema.graphql

# 执行查询
linear api '{ viewer { id name email } }'

# 带变量的查询
linear api 'query($teamId: String!) { team(id: $teamId) { name } }' \
  --variable teamId=abc123

# 带JSON变量的复杂查询
linear api 'query($filter: IssueFilter!) { issues(filter: $filter) { nodes { title } } }' \
  --variables-json '{"filter": {"state": {"name": {"eq": "In Progress"}}}}'

# 使用curl直接调用
curl -s -X POST https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: $(linear auth token)" \
  -d '{"query": "{ viewer { id } }"}'
```

### Git集成配置

```bash
# 配置版本控制系统
# 在 .linear.toml 中设置
# vcs = "git"  或  vcs = "jj"

# 任务开始时自动创建分支
linear issue start ABC-123
# 自动创建分支：eng/ABC-123-fix-login-bug

# 创建PR关联任务
linear issue pr
# 自动创建PR并关联到任务
```

### 配置文件完整示例

```toml
# .linear.toml
team_id = "ENG"
workspace = "mycompany"
issue_sort = "priority"
vcs = "git"
```

| 配置项 | 环境变量 | TOML键 | 示例值 |
|:-------|:---------|:-------|:-------|
| 团队ID | `LINEAR_TEAM_ID` | `team_id` | `"ENG"` |
| 工作区 | `LINEAR_WORKSPACE` | `workspace` | `"mycompany"` |
| 任务排序 | `LINEAR_ISSUE_SORT` | `issue_sort` | `"priority"` 或 `"manual"` |
| 版本控制 | `LINEAR_VCS` | `vcs` | `"git"` 或 `"jj"` |

配置文件查找顺序：
1. 当前目录的`linear.toml`或`.linear.toml`
2. 项目根目录的`linear.toml`或`.linear.toml`
3. 项目根目录的`.config/linear.toml`
4. 用户目录的`~/.config/linear/linear.toml`

## 常见问题

### Q1: 任务更新时状态ID怎么获取？

通过`linear issue list --format json`查看任务的状态信息，或通过GraphQL查询`{ workflowStates { id name } }`获取所有状态ID。

### Q2: 批量创建任务时如何控制速率？

Linear API有速率限制。批量操作时在循环中添加`sleep 1`控制请求间隔，避免触发429错误。

### Q3: Git集成的分支命名规则是什么？

默认格式为`<团队前缀>/<任务ID>-<任务标题slug>`。具体格式可在`.linear.toml`中通过相关配置项自定义。

### Q4: GraphQL查询返回字段不全？

Linear的GraphQL API按需返回字段，必须在查询中明确指定需要的字段。使用`linear schema`导出Schema查看可用字段。

### Q5: 文档创建支持Markdown吗？

支持。通过`--content-file`上传的Markdown文件会被Linear解析并渲染。直接使用`--content`参数时也可传入Markdown格式文本。

### Q6: issue pr命令如何关联代码仓库？

需在项目根目录执行，CLI会自动检测Git远程仓库并创建PR。确保仓库已关联到Linear团队设置的Git集成中。

### Q7: 多团队环境下如何切换操作的团队？

通过`LINEAR_TEAM_ID`环境变量临时指定，或在`.linear.toml`中设置`team_id`。也可在GraphQL查询中通过`teamId`参数指定。

### Q8: 任务删除是否可恢复？

Linear的任务删除是软删除，可在网页端的回收站中恢复。建议删除前先添加评论记录删除原因。

### Q9: 如何查看任务的完整评论历史？

通过`linear issue view ABC-123`查看任务详情时会包含评论。或通过GraphQL查询`{ issue(id: "ABC-123-id") { comments { body user { name } } } }`。

### Q10: 配置文件修改后不生效？

配置文件在命令执行时读取。确保修改的是正确查找路径下的文件。使用`linear config`交互式重新生成配置确保生效。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
