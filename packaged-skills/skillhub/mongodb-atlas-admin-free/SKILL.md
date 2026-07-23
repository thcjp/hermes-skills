---
slug: "mongodb-atlas-admin-free"
name: "mongodb-atlas-admin-free"
version: "1.0.0"
displayName: "文档数据库管理(免费版)"
summary: "通过API浏览和调用文档数据库云管理平台，支持目录浏览、端点详情和实时调用(免费版)"
license: "MIT"
description: |-
  通过API浏览和调用文档数据库云管理平台。支持API目录浏览、端点详情获取、
  Schema定义查询和实时API调用。覆盖50+分类的完整API端点，支持 dry-run
  预检和自动确认模式。适用于独立开发者、企业团队和自动化工作流场景。
  不适用于直接数据库查询操作。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 数据存储
---
# 文档数据库云管理平台(免费版)

通过API浏览和调用文档数据库云管理平台的管理接口。

## 核心能力

### 1. API目录浏览
通过 `atlas-api.mjs catalog` 列出所有可用的API分类和端点，覆盖50+分类，包括集群管理、数据库用户、网络配置、备份恢复、监控告警等。

```bash
node （请参考skill目录中的脚本文件） catalog
```

**处理**: 按照skill规范执行API目录浏览操作,遵循单一意图原则。
**输出**: 返回API目录浏览的执行结果,包含操作状态和输出数据。

### 2. 端点详情获取
通过 `atlas-api.mjs detail` 查看特定端点的详细信息，包括HTTP方法、路径参数、请求体Schema和响应格式。

```bash
node （请参考skill目录中的脚本文件） detail --category "Clusters" --endpoint "Create Cluster"
```- 验证执行结果，确认输出符合预期格式
- 参考`端点详情获取`相关配置参数进行设置
### 3. Schema定义查询
查看API端点的请求和响应Schema定义，了解参数类型、是否必填和默认值。

```bash
node （请参考skill目录中的脚本文件） detail --category "Database Users" --endpoint "Create Database User" --schema
```- 验证执行结果，确认输出符合预期格式
- 参考`Schema定义查询`相关配置参数进行设置
### 4. 实时API调用
通过 `atlas-call.mjs` 直接调用API端点，支持 `--dry-run` 预检和 `--yes` 自动确认。

```bash
# 预检模式（不实际执行）
node （请参考skill目录中的脚本文件） --category "Clusters" --endpoint "Create Cluster" --dry-run --data '{"name":"myCluster", "providerSettings": {"providerName": "AWS", "regionName": "US_EAST_1", "instanceSizeName": "M10"}}'

# 实际执行
node （请参考skill目录中的脚本文件） --category "Clusters" --endpoint "Create Cluster" --yes --data '{"name":"myCluster", "providerSettings": {"providerName": "AWS", "regionName": "US_EAST_1", "instanceSizeName": "M10"}}'
```

#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| API目录浏览 | 无 | 50+分类的API端点列表 |
| 端点详情查询 | 分类+端点名 | HTTP方法/参数/Schema |
| 实时API调用 | 分类+端点+数据 | API调用结果 |

## 使用流程

1. 设置环境变量 `ATLAS_CLIENT_ID` 和 `ATLAS_CLIENT_SECRET`
2. 用 `catalog` 浏览API分类,或用 `--search` 搜索
3. 用 `detail` 查看端点详情和Schema
4. 用 `--dry-run` 预检请求
5. 确认后用 `--yes` 实际执行

#
## 示例

### 示例:创建集群（dry-run预检）

```bash
node （请参考skill目录中的脚本文件） \
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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `ATLAS_CLIENT_ID`未配置 | 凭证缺失 | 通过 `export ATLAS_CLIENT_ID="your_id"` 设置 |
| `ATLAS_CLIENT_SECRET`未配置 | 凭证缺失 | 通过 `export ATLAS_CLIENT_SECRET="your_secret"` 设置 |
| JSON数据格式错误 | `--data`参数无效JSON | 使用 `jq` 验证JSON格式，确保引号和括号正确 |
| API返回401 Unauthorized | 凭证过期或权限不足 | 检查凭证是否正确，确认API Key具有所需权限 |

## 常见问题

### Q1: 支持哪些API分类？
A: 覆盖50+分类，包括 Alerts、Atlas Search、Auditing、Backup、Clusters、Database Users、Network Peering、Private Endpoints、Monitoring、Logs 等。用 `atlas-api.mjs catalog` 查看完整列表。

### Q2: `--dry-run`和`--yes`有什么区别？
A: `--dry-run` 只预检请求不实际执行，显示将要发送的HTTP方法和请求体。`--yes` 跳过交互确认直接执行。建议先用 `--dry-run` 预检再实际执行。

### Q3: 如何配置API凭证？
A: 设置环境变量 `ATLAS_CLIENT_ID` 和 `ATLAS_CLIENT_SECRET`。这是公私钥认证方式，在云管理平台的API Keys页面创建。

## 已知限制

- 仅管理云平台配置，不执行数据库查询
- 需要预先配置 `ATLAS_CLIENT_ID` 和 `ATLAS_CLIENT_SECRET`
- API调用有速率限制，429时需等待重试

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
## 升级提示

本免费版提供基础功能。升级到完整版 mongodb-atlas-admin 获取全部能力和高级特性。
