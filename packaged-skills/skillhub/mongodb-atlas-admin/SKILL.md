---
slug: mongodb-atlas-admin
name: mongodb-atlas-admin
version: "2.0.0"
displayName: 文档数据库管理
summary: 通过API浏览和调用文档数据库云管理平台，支持目录浏览、端点详情和实时调用
license: MIT-0
description: |-
  通过API浏览和调用文档数据库云管理平台。支持API目录浏览、端点详情获取、
  Schema定义查询和实时API调用。覆盖50+分类的完整API端点，支持 dry-run
  预检和自动确认模式。适用于独立开发者、企业团队和自动化工作流场景。
  不适用于直接数据库查询操作。
tools:
  - read
  - exec
---

# 文档数据库云管理平台

通过API浏览和调用文档数据库云管理平台的管理接口。

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
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. API目录浏览
通过 `atlas-api.mjs catalog` 列出所有可用的API分类和端点，覆盖50+分类，包括集群管理、数据库用户、网络配置、备份恢复、监控告警等。

```bash
node scripts/atlas-api.mjs catalog
```

**处理**: 按照skill规范执行API目录浏览操作,遵循单一意图原则。
**输出**: 返回API目录浏览的执行结果,包含操作状态和输出数据。

### 2. 端点详情获取
通过 `atlas-api.mjs detail` 查看特定端点的详细信息，包括HTTP方法、路径参数、请求体Schema和响应格式。

```bash
node scripts/atlas-api.mjs detail --category "Clusters" --endpoint "Create Cluster"
```

- 执行`端点详情获取`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`端点详情获取`相关配置参数进行设置
### 3. Schema定义查询
查看API端点的请求和响应Schema定义，了解参数类型、是否必填和默认值。

```bash
node scripts/atlas-api.mjs detail --category "Database Users" --endpoint "Create Database User" --schema
```

- 执行`Schema定义查询`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`Schema定义查询`相关配置参数进行设置
### 4. 实时API调用
通过 `atlas-call.mjs` 直接调用API端点，支持 `--dry-run` 预检和 `--yes` 自动确认。

```bash
# 预检模式（不实际执行）
node scripts/atlas-call.mjs --category "Clusters" --endpoint "Create Cluster" --dry-run --data '{"name":"myCluster", "providerSettings": {"providerName": "AWS", "regionName": "US_EAST_1", "instanceSizeName": "M10"}}'

# 实际执行
node scripts/atlas-call.mjs --category "Clusters" --endpoint "Create Cluster" --yes --data '{"name":"myCluster", "providerSettings": {"providerName": "AWS", "regionName": "US_EAST_1", "instanceSizeName": "M10"}}'
```

**输入**: 用户提供实时API调用所需的指令和必要参数。
### 5. 分类搜索
按关键词搜索API分类，快速定位需要的端点。

```bash
node scripts/atlas-api.mjs catalog --search "backup"
```

**输入**: 用户提供分类搜索所需的指令和必要参数。
**输出**: 返回分类搜索的执行结果,包含操作状态和输出数据。

### 6. 凭证管理
通过环境变量管理API凭证，支持公私钥认证方式。

```bash
export ATLAS_CLIENT_ID="your_client_id"
export ATLAS_CLIENT_SECRET="your_client_secret"
```

**输入**: 用户提供凭证管理所需的指令和必要参数。
**处理**: 按照skill规范执行凭证管理操作,遵循单一意图原则。

### 能力覆盖范围

本skill还覆盖以下能力场景: 浏览和调用文档数、据库云管理平台、支持目录浏览、端点详情和实时调、定义查询和实时、分类的完整、预检和自动确认模、适用于独立开发者、企业团队和自动化、工作流场景、不适用于直接数据、库查询操作。这些能力在上述核心功能中均有对应处理逻辑。
### 源能力映射
本skill覆盖源skill的以下能力点:

| 源能力点 | 支持状态 | 实现方式 |
|:---------|:---------|:---------|
| Projects / Organizations | 支持 | 通过核心功能实现对应能力 |

**输入**: 用户提供源能力映射所需的指令和必要参数。
**处理**: 按照skill规范执行源能力映射操作,遵循单一意图原则。
**输出**: 返回源能力映射的执行结果,包含操作状态和输出数据。
### 领域术语
本skill涉及以下领域术语: `requires`, `safety`, `openapi`, `list`, `print`, `operation`, `skip`, `serverless`, `protocol`, `patch`, `require`, `environment`, `democluster`, `confirm`, `configurations`

**输入**: 用户提供领域术语所需的指令和必要参数。
**处理**: 按照skill规范执行领域术语操作,遵循单一意图原则。
**输出**: 返回领域术语的执行结果,包含操作状态和输出数据。

## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`mongodb-atlas-admin`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

### 命令参数说明

- `-Demand`: 命令参数,用于指定操作选项
- `--category`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Demand`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Demand`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Demand`: 命令参数,用于指定操作选项

## 真实示例

### 示例1：列出所有API分类

```bash
node scripts/atlas-api.mjs catalog
```

输出：
```
Available API Categories (52):
  - Alerts
  - Atlas Search
  - Auditing
  - Backup
  - Clusters
  - Database Users
  - Network Peering
  - Private Endpoints
  - ...
```

### 示例2：创建集群（dry-run预检）

```bash
node scripts/atlas-call.mjs \
  --category "Clusters" \
  --endpoint "Create Cluster" \
  --dry-run \
  --data '{
    "name": "prod-cluster",
    "clusterType": "REPLICASET",
    "providerSettings": {
      "providerName": "AWS",
      "regionName": "US_EAST_1",
      "instanceSizeName": "M10"
    },
    "replicationSpecs": [{
      "numShards": 1,
      "regionsConfig": {"US_EAST_1": {"electableNodes": 3, "priority": 7, "readOnlyNodes": 0}}
    }]
  }'
```

输出：
```
[dry-run] Request would be:
  POST /api/atlas/v2.0/groups/{groupId}/clusters
  Body: {"name": "prod-cluster", "clusterType": "REPLICASET", ...}
No changes applied. Remove --dry-run to execute.
```

### 示例3：创建数据库用户

```bash
node scripts/atlas-call.mjs \
  --category "Database Users" \
  --endpoint "Create Database User" \
  --yes \
  --data '{
    "username": "app-user",
    "password": "SecurePass123!",
    "roles": [{"roleName": "readWrite", "databaseName": "myApp"}]
  }'
```

输出：
```json
{
  "id": "60d5ec9b1234567890abcdef",
  "username": "app-user",
  "roles": [{"roleName": "readWrite", "databaseName": "myApp"}],
  "links": [{"href": "https://cloud.mongodb.com/api/atlas/v2.0/groups/.../databaseUsers/app-user"}]
}
```

### 示例4：搜索备份相关API

```bash
node scripts/atlas-api.mjs catalog --search "backup"
```

输出：
```
Matching categories:
  - Backup (12 endpoints)
    - Create Backup Schedule
    - Get Backup Schedule
    - Update Backup Schedule
    - Delete Backup Schedule
    - Take Snapshot On-Demand
    - ...
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `ATLAS_CLIENT_ID`未配置 | 凭证缺失 | 通过 `export ATLAS_CLIENT_ID="your_id"` 设置 |
| `ATLAS_CLIENT_SECRET`未配置 | 凭证缺失 | 通过 `export ATLAS_CLIENT_SECRET="your_secret"` 设置 |
| JSON数据格式错误 | `--data`参数无效JSON | 使用 `jq` 验证JSON格式，确保引号和括号正确 |
| dry-run与实际执行不匹配 | 预检参数与执行参数不一致 | 先用 `--dry-run` 预检，确认后去掉 `--dry-run` 加 `--yes` 执行 |
| API返回401 Unauthorized | 凭证过期或权限不足 | 检查凭证是否正确，确认API Key具有所需权限 |
| API返回429 Too Many Requests | 速率限制 | 等待60秒后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，或降低调用频率 |
| API返回404 Not Found | 分类或端点名拼写错误 | 用 `catalog` 命令确认正确的分类和端点名称 |

## 常见问题

### Q1: 支持哪些API分类？
A: 覆盖50+分类，包括 Alerts、Atlas Search、Auditing、Backup、Clusters、Database Users、Network Peering、Private Endpoints、Monitoring、Logs 等。用 `atlas-api.mjs catalog` 查看完整列表。

### Q2: `--dry-run`和`--yes`有什么区别？
A: `--dry-run` 只预检请求不实际执行，显示将要发送的HTTP方法和请求体。`--yes` 跳过交互确认直接执行。建议先用 `--dry-run` 预检再实际执行。

### Q3: 如何配置API凭证？
A: 设置环境变量 `ATLAS_CLIENT_ID` 和 `ATLAS_CLIENT_SECRET`。这是公私钥认证方式，在云管理平台的API Keys页面创建。

### Q4: 支持直接查询数据库吗？
A: 不支持。本工具仅管理云平台配置（集群、用户、网络、备份等），不执行数据库查询操作。查询请使用 `mongosh` 或应用程序驱动。

### Q5: 如何查找特定功能的API？
A: 使用 `atlas-api.mjs catalog --search "keyword"` 按关键词搜索。例如搜索 "backup" 会列出所有备份相关的分类和端点。

### Q6: API调用有速率限制吗？
A: 有。返回429状态码时表示触发速率限制，需等待60秒后重试。建议批量操作时控制调用频率。

### Q7: `--data`参数的JSON格式有什么要求？
A: 必须是有效的JSON字符串。建议先用 `jq` 验证格式。命令行中JSON建议用单引号包裹，内部字符串用双引号。

## 已知限制

- 仅管理云平台配置，不执行数据库查询
- 需要预先配置 `ATLAS_CLIENT_ID` 和 `ATLAS_CLIENT_SECRET`
- API调用有速率限制，429时需等待重试
- `--dry-run` 不会实际执行，需去掉后加 `--yes` 才执行
- 覆盖50+分类的API端点，但部分高级功能可能需要直接调用原始API
- 环境变量在当前会话生效，新会话需重新设置
