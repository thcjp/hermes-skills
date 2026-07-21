---
slug: pipedrive-toolkit
name: pipedrive-toolkit
version: "1.0.0"
displayName: Pipedrive工具(专业版)
summary: 全功能Pipedrive CRM管理工具，支持商机全生命周期、批量操作与多连接管理
license: Proprietary
edition: pro
description: |-
  Pipedrive工具专业版是面向销售团队的完整CRM管理命令行方案，在免费版基础上解锁商机创建/更新/删除全生命周期、联系人和组织管理、活动创建与完成标记、备注管理、批量操作、多连接管理和自定义字段操作等全部高级能力。核心能力：商机CRUD全生命周期、联系人/组织CRUD、活动创建与管理、备注创建与关联、批量数据导入导出、多Pipedrive账户连接管理、自定义字段读写、高级过滤器管理、OAuth连接全生命周期控制
tags:
- 销售管理
- CRM集成
- 批量操作
- 高级集成
tools:
  - - read
- exec
---
# Pipedrive工具(专业版)

## 核心能力

| 能力模块 | 专业版支持 | 说明 |
|:---------|:-----------|:-----|
| 商机管理 | 全量CRUD | 列表、详情、创建、更新、删除、搜索 |
| 联系人管理 | 全量CRUD | 列表、详情、创建、更新、删除、搜索 |
| 组织管理 | 全量CRUD | 列表、详情、创建、更新、删除 |
| 活动管理 | 全量CRUD | 列表、详情、创建、更新、删除 |
| 备注管理 | 创建+查询 | 列表、创建（关联到商机/联系人/组织） |
| 管道管理 | 全量查询 | 列表、详情 |
| 阶段管理 | 全量查询 | 列表、详情（按管道过滤） |
| 用户管理 | 查询 | 列表用户、当前用户信息 |
| 批量操作 | 支持 | 批量创建、更新和数据导入 |
| 连接管理 | 全量CRUD | 列表、创建、查看、删除OAuth连接 |
| 多账户支持 | 支持 | 通过连接ID指定操作目标账户 |
| 自定义字段 | 支持 | 通过字段API Key读写自定义字段 |
| 高级过滤 | 支持 | 创建和管理自定义过滤器 |
### 能力模块

执行能力模块操作,处理用户输入并返回结果。

**输入**: 用户提供能力模块所需的参数和指令。

**输出**: 返回能力模块的处理结果。

- 执行`能力模块`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`能力模块`相关配置参数进行设置
### 商机管理

执行商机管理操作,处理用户输入并返回结果。

**输入**: 用户提供商机管理所需的参数和指令。

**输出**: 返回商机管理的处理结果。

- 执行`商机管理`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`商机管理`相关配置参数进行设置
### 联系人管理

执行联系人管理操作,处理用户输入并返回结果。

**输入**: 用户提供联系人管理所需的参数和指令。

**输出**: 返回联系人管理的处理结果。

- 执行`联系人管理`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`联系人管理`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 全功能、Pipedrive、CRM、管理工具、支持商机全生命周、批量操作与多连接、工具专业版是面向、销售团队的完整、管理命令行方案、在免费版基础上解、锁商机创建、删除全生命周期、联系人和组织管理、活动创建与完成标、多连接管理和自定、义字段操作等全部、高级能力、核心能力、全生命周期、活动创建与管理、备注创建与关联、批量数据导入导出、账户连接管理、自定义字段读写、高级过滤器管理、连接全生命周期控。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 销售场景：客户录入与商机创建
新客户接触后，通过命令行快速录入联系人信息并创建关联商机：

```python
import urllib.request, os, json

headers = {'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}', 'Content-Type': 'application/json'}

# 1. 创建组织
org_data = json.dumps({'name': '新客户公司', 'address': '上海市浦东新区'}).encode()
org_req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/organizations', data=org_data, method='POST')
for k, v in headers.items(): org_req.add_header(k, v)
org_response = json.load(urllib.request.urlopen(org_req))
org_id = org_response['data']['id']

# 2. 创建联系人（关联到组织）
person_data = json.dumps({'name': '张三', 'email': ['zhangsan@example.com'], 'phone': ['13800138000'], 'org_id': org_id}).encode()
person_req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/persons', data=person_data, method='POST')
for k, v in headers.items(): person_req.add_header(k, v)
person_response = json.load(urllib.request.urlopen(person_req))
person_id = person_response['data']['id']

# 3. 创建商机（关联到联系人和组织）
deal_data = json.dumps({'title': '新客户合作', 'value': 50000, 'currency': 'CNY', 'person_id': person_id, 'org_id': org_id, 'stage_id': 1}).encode()
deal_req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/deals', data=deal_data, method='POST')
for k, v in headers.items(): deal_req.add_header(k, v)
deal_response = json.load(urllib.request.urlopen(deal_req))
print(f"商机已创建：{deal_response['data']['title']}")
```

### 运营场景：批量活动创建
为多个商机批量创建跟进活动，确保销售跟进不遗漏：

```python
import urllib.request, os, json

headers = {'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}', 'Content-Type': 'application/json'}

# 获取所有open商机
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/deals?status=open&limit=100')
req.add_header('Authorization', headers['Authorization'])
deals = json.load(urllib.request.urlopen(req))['data']

# 为每个商机创建跟进电话活动
for deal in deals:
    activity_data = json.dumps({
        'subject': f'跟进电话 - {deal["title"]}',
        'type': 'call',
        'due_date': '2026-07-20',
        'due_time': '10:00',
        'deal_id': deal['id']
    }).encode()
    req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/activities', data=activity_data, method='POST')
    for k, v in headers.items(): req.add_header(k, v)
    urllib.request.urlopen(req)
    print(f"已创建活动：跟进 {deal['title']}")
```

### 管理场景：多账户数据查询
管理多个Pipedrive账户，通过连接ID指定查询目标：

```bash
# 列出所有连接
python -c "
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections?app=pipedrive&status=ACTIVE')
req.add_header('Authorization', f'Bearer {os.environ[\"MATON_API_KEY\"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
"

# 查询指定账户的商机（通过Maton-Connection头指定）
python -c "
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/deals?status=open')
req.add_header('Authorization', f'Bearer {os.environ[\"MATON_API_KEY\"]}')
req.add_header('Maton-Connection', '{connection_id}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
"
```

## 使用流程

### 前置条件
1. 已注册API代理服务账户并获取API Key
2. 已创建Pipedrive OAuth连接
3. 已设置API Key环境变量

### 配置环境变量
```bash
export MATON_API_KEY="your_api_key_here"
```

### 使用流程
```bash
# 1. 列出open商机
python -c "
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/deals?status=open')
req.add_header('Authorization', f'Bearer {os.environ[\"MATON_API_KEY\"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
"

# 2. 创建新商机
python -c "
import urllib.request, os, json
data = json.dumps({'title': '测试商机', 'value': 10000, 'currency': 'CNY'}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/deals', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ[\"MATON_API_KEY\"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
"

# 3. 创建联系人
python -c "
import urllib.request, os, json
data = json.dumps({'name': '李四', 'email': ['lisi@example.com']}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/persons', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ[\"MATON_API_KEY\"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
"

# 4. 创建跟进活动
python -c "
import urllib.request, os, json
data = json.dumps({'subject': '跟进电话', 'type': 'call', 'due_date': '2026-07-20'}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/activities', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ[\"MATON_API_KEY\"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
"
```

### 命令参数说明

4. `-Connection`: 命令参数,用于指定操作选项
5. `-Type`: 命令参数,用于指定操作选项
6. `-Connection头指定`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Connection`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-Connection头指定`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Connection`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-Connection头指定`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Connection头指定`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-Connection`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-Connection`: 命令参数,用于指定操作选项
- `-Connection头指定`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Connection`: 命令参数,用于指定操作选项
- `-Connection头指定`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-Connection头指定`: 命令参数,用于指定操作选项
- `-Connection`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Connection头指定`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-Connection`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-Connection头指定`: 命令参数,用于指定操作选项
- `-Connection`: 命令参数,用于指定操作选项

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

| 症状 | 可能原因 | 解决方案 | 优先级 |
|:-----|:---------|:---------|:-------|
| 401未授权 | API Key无效或未设置 | 检查MATON_API_KEY环境变量 | 高 |
| 400缺少连接 | Pipedrive OAuth连接未创建 | 创建连接并完成授权 | 高 |
| 404资源不存在 | ID错误或资源已删除 | 确认ID正确，检查资源状态 | 中 |
| 429速率限制 | 请求过于频繁 | 降低请求频率，添加间隔 | 中 |
| 创建失败 | 必填字段缺失 | 检查请求体，确保必填字段完整 | 中 |
| 更新不生效 | 方法或ID错误 | 确认PUT方法和正确ID | 中 |
| 多账户数据错乱 | 未指定连接ID | 添加Maton-Connection头 | 中 |
| 自定义字段无效 | 字段API Key错误 | 在后台确认字段Key | 低 |
| 连接授权失败 | URL已过期 | 重新创建连接获取新URL | 中 |
| 删除后仍可见 | 软删除标记 | 在回收站中永久删除 | 低 |

## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.6+（使用urllib标准库，无需额外安装）
- **Node.js**：可选（使用JavaScript集成示例时需要）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| API代理服务 | 在线服务 | 必需 | 注册账户并获取API Key |
| Pipedrive账户 | 在线账户 | 必需 | 在Pipedrive官网注册 |
| Pipedrive OAuth连接 | 认证连接 | 必需 | 在代理服务中创建 |
| Python | 运行时 | 必需 | 系统通常自带或从官网安装 |
| Node.js | 运行时 | 可选 | JavaScript集成时需要 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- **API代理Key**：通过`MATON_API_KEY`环境变量配置
- **获取方式**：在代理服务设置页面创建账户并复制API Key
- **Pipedrive OAuth**：通过代理服务管理页面创建连接并完成授权
- **多账户管理**：每个Pipedrive账户对应一个连接ID，通过`Maton-Connection`头指定
- **禁止**：在代码或配置文件中明文写入API Key
- **安全建议**：将API Key存储在`.env`文件中（已加入.gitignore），写操作需用户显式确认

### 可用性分类
- **分类**：MD+EXEC（纯Markdown指令，需要exec命令行执行能力）
- **说明**：基于Markdown的AI Skill，通过自然语言指令驱动Agent执行Pipedrive全量API操作

## 案例展示

### 连接管理
```python
import urllib.request, os, json

headers = {'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}', 'Content-Type': 'application/json'}

# 列出所有Pipedrive连接
req = urllib.request.Request('https://api.maton.ai/connections?app=pipedrive&status=ACTIVE')
req.add_header('Authorization', headers['Authorization'])
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

# 创建新连接
data = json.dumps({'app': 'pipedrive'}).encode()
req = urllib.request.Request('https://api.maton.ai/connections', data=data, method='POST')
for k, v in headers.items(): req.add_header(k, v)
response = json.load(urllib.request.urlopen(req))
# 打开返回的url完成OAuth授权
print(f"请在浏览器中打开此URL完成授权：{response['connection']['url']}")

# 查看指定连接详情
req = urllib.request.Request('https://api.maton.ai/connections/{connection_id}')
req.add_header('Authorization', headers['Authorization'])
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

# 删除连接
req = urllib.request.Request('https://api.maton.ai/connections/{connection_id}', method='DELETE')
req.add_header('Authorization', headers['Authorization'])
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
```

### 商机全生命周期
```python
import urllib.request, os, json

headers = {'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}', 'Content-Type': 'application/json'}

# 创建商机
data = json.dumps({
    'title': '企业版合作',
    'value': 50000,
    'currency': 'CNY',
    'person_id': 123,
    'org_id': 456,
    'stage_id': 1,
    'expected_close_date': '2026-06-30'
}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/deals', data=data, method='POST')
for k, v in headers.items(): req.add_header(k, v)
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

# 更新商机
data = json.dumps({'title': '更新后的标题', 'value': 75000, 'status': 'won'}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/deals/123', data=data, method='PUT')
for k, v in headers.items(): req.add_header(k, v)
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

# 删除商机
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/deals/123', method='DELETE')
req.add_header('Authorization', headers['Authorization'])
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
```

### 联系人管理
```python
import urllib.request, os, json

headers = {'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}', 'Content-Type': 'application/json'}

# 创建联系人
data = json.dumps({
    'name': '王五',
    'email': ['wangwu@example.com'],
    'phone': ['+8613800138000'],
    'org_id': 456,
    'visible_to': 3
}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/persons', data=data, method='POST')
for k, v in headers.items(): req.add_header(k, v)
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

# 更新联系人
data = json.dumps({'name': '王五（已更新）', 'email': ['new@example.com']}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/persons/123', data=data, method='PUT')
for k, v in headers.items(): req.add_header(k, v)
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

# 删除联系人
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/persons/123', method='DELETE')
req.add_header('Authorization', headers['Authorization'])
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
```

### 组织管理
```python
import urllib.request, os, json

headers = {'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}', 'Content-Type': 'application/json'}

# 创建组织
data = json.dumps({'name': '新公司', 'address': '北京市海淀区', 'visible_to': 3}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/organizations', data=data, method='POST')
for k, v in headers.items(): req.add_header(k, v)
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

# 更新组织
data = json.dumps({'name': '新公司国际'}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/organizations/456', data=data, method='PUT')
for k, v in headers.items(): req.add_header(k, v)
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

# 删除组织
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/organizations/456', method='DELETE')
req.add_header('Authorization', headers['Authorization'])
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
```

### 活动管理
```python
import urllib.request, os, json

headers = {'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}', 'Content-Type': 'application/json'}

# 创建活动
data = json.dumps({
    'subject': '跟进电话',
    'type': 'call',
    'due_date': '2026-03-15',
    'due_time': '14:00',
    'duration': '00:30',
    'deal_id': 789,
    'person_id': 123,
    'note': '讨论合同条款'
}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/activities', data=data, method='POST')
for k, v in headers.items(): req.add_header(k, v)
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

# 标记活动为已完成
data = json.dumps({'done': 1, 'note': '已完成 - 客户同意条款'}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/activities/123', data=data, method='PUT')
for k, v in headers.items(): req.add_header(k, v)
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

# 删除活动
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/activities/123', method='DELETE')
req.add_header('Authorization', headers['Authorization'])
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
```

### 备注管理
```python
import urllib.request, os, json

headers = {'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}', 'Content-Type': 'application/json'}

# 创建备注（关联到商机）
data = json.dumps({
    'content': '会议纪要：讨论了定价和时间表',
    'deal_id': 789,
    'pinned_to_deal_flag': 1
}).encode()
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/notes', data=data, method='POST')
for k, v in headers.items(): req.add_header(k, v)
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

# 列出备注（按商机过滤）
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/notes?deal_id=789')
req.add_header('Authorization', headers['Authorization'])
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
```

### JavaScript集成示例
```javascript
const headers = {
  'Authorization': `Bearer ${process.env.MATON_API_KEY}`,
  'Content-Type': 'application/json'
};

// 创建商机
await fetch('https://api.maton.ai/pipedrive/api/v1/deals', {
  method: 'POST',
  headers,
  body: JSON.stringify({title: '新商机', value: 10000, currency: 'CNY'})
}).then(r => r.json());

// 更新商机状态为成交
await fetch('https://api.maton.ai/pipedrive/api/v1/deals/123', {
  method: 'PUT',
  headers,
  body: JSON.stringify({status: 'won'})
}).then(r => r.json());

// 多账户查询（指定连接ID）
await fetch('https://api.maton.ai/pipedrive/api/v1/deals', {
  headers: {
    ...headers,
    'Maton-Connection': '{connection_id}'
  }
}).then(r => r.json());
```

### 数据字段说明
| 字段 | 类型 | 说明 |
|:-----|:-----|:-----|
| ID | 整数 | 资源唯一标识 |
| email | 数组 | 支持多个邮箱地址 |
| phone | 数组 | 支持多个电话号码 |
| visible_to | 整数 | 可见性：1(仅创建者)/3(全公司)/5(可见性组)/7(全公司+可见性组) |
| status | 字符串 | 商机状态：open/won/lost/deleted |
| 自定义字段 | 混合 | 通过字段API Key访问（如`abc123_custom_field`） |

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 常见问题

### Q1: 创建操作返回400错误？
检查请求体JSON格式是否正确，必填字段是否完整。商机创建至少需要`title`字段，联系人至少需要`name`字段，组织至少需要`name`字段。

### Q2: 更新操作未生效？


## 已知限制

- 每次请求仅处理单一任务,不支持批量并发
- 
- 和网络环境
