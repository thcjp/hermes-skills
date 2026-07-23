---
slug: "slack-api-toolkit"
name: "slack-api-toolkit"
version: "1.0.0"
displayName: "Slack API工具箱Pro"
summary: "Slack全功能集成方案，含文件、搜索、反应、书签、批量操作与审计日志。"
license: "Proprietary"
edition: "pro"
description: |-
  Slack API工具箱（专业版）为团队与企业提供Slack API的全功能集成方案，覆盖消息、频道、文件、搜索、反应、书签等全部能力。核心能力：全API端点覆盖、文件管理与上传、消息与文件搜索、表情反应与书签管理、批量操作、定时消息、操作审计日志、多工作区管理、MCP工具集成适配。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API.
tags:
  - 集成工具
  - 团队协作
  - 企业级
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# Slack API工具箱Pro

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

| 能力 | 说明 | 专业版支持 |
|:-----|:-----|:-----|
| 托管OAuth连接 | 自动管理Token | 是 |
| 消息全操作 | 发送、回复、更新、删除、定时 | 是 |
| 频道全管理 | 创建、加入、离开、归档、重命名、设置主题 | 是 |
| 文件管理 | 上传、下载、删除、查询 | 是 |
| 消息与文件搜索 | 全工作区搜索 | 是 |
| 表情反应 | 添加、删除、查询反应 | 是 |
| 书签与置顶 | 书签增删改查、消息置顶 | 是 |
| 直接消息 | 打开DM、列出DM频道 | 是 |
| 批量操作 | 批量发消息、批量管理 | 是 |
| 定时消息 | 定时发送与取消 | 是 |
| 审计日志 | 操作全程留痕 | 是 |
| 多工作区管理 | 多连接切换 | 是 |
### 托管OAuth连接

针对托管OAuth连接,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供托管OAuth连接相关的配置参数、输入数据和处理选项.
**输出**: 返回托管OAuth连接的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`托管OAuth连接`的配置文档进行参数调优
### 消息全操作

针对消息全,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供消息全操作相关的配置参数、输入数据和处理选项.
**输出**: 返回消息全操作的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`消息全操作`的配置文档进行参数调优
### 频道全管理

针对频道全,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供频道全管理相关的配置参数、输入数据和处理选项.
**输出**: 返回频道全管理的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`频道全管理`的配置文档进行参数调优
#
## 适用场景

### 场景1：企业级Slack自动化

某公司需要在新员工入职时自动：创建欢迎频道、发送入职指南、邀请至相关频道、置顶重要文档。使用专业版工作流：批量创建频道 → 批量发送消息 → 批量邀请成员 → 置顶消息，全程自动化，操作留痕供审计.
### 场景2：跨工作区管理

集团有多个Slack工作区（按事业部划分）。管理员使用专业版多连接管理：建立多个工作区连接，通过`--connection`指定目标工作区，统一管理跨工作区的公告发布与频道治理.
### 场景3：合规审计场景

金融行业客户要求所有Slack操作可追溯。专业版审计日志记录每次消息发送、文件上传、频道变更的操作者、时间、目标与结果，支持导出供合规审计。敏感操作（如批量删除消息）实时告警.
### 场景4：消息搜索与归档

运营团队需要查找过去30天内所有提及"产品发布"的消息并归档。使用专业版搜索接口：`search messages "产品发布"`，结果导出为报告，无需逐频道翻阅.
### 场景5：Agent驱动的Slack工作流

Agent根据业务事件自动执行Slack操作：如CI构建失败时，Agent搜索相关频道、发送带文件附件的告警、添加表情反应标记优先级、置顶关键信息。专业版提供完整API支撑此类复杂工作流.
## 使用流程

### 依赖说明

### 运行环境
1. **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
2. **操作系统**：Windows / macOS / Linux
3. **网络**：可访问Slack网关与Slack API

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| Slack网关账户 | 在线服务 | 必需 | 在网关控制台注册 |
| Slack工作区 | 在线服务 | 必需 | 在Slack创建或加入 |
| Node.js | 运行时 | 可选 | CLI安装需要 |
| Python | 运行时 | 可选 | Python SDK需要 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
4. **网关API Key**：存储于环境变量`SGW_API_KEY`或通过`sgw login`保存
5. **Slack OAuth Token**：由网关托管，通过OAuth授权建立连接
6. **禁止**：在代码或脚本中硬编码API Key或Slack Token

### 可用性分类
7. **分类**：MD+EXEC（）
8. **说明**：基于Markdown的AI Skill，

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | slack-api-toolkit处理的内容输入 |, 默认: 全部维度 |
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

| 现象 | 可能原因 | 解决方案 |
|:------|------:|:------|
| 400 Missing connection | 未建立Slack连接 | 运行`sgw connection create slack` |
| 401 Invalid API key | API Key无效或过期 | `sgw login`重新登录 |
| 429 Rate limited | 超过10请求/秒 | 降低频率或使用批量接口 |
| missing_scope | OAuth权限不足 | 在控制台为连接申请额外权限 |
| file_not_found | 文件ID错误 | 确认ID以F开头，从file list获取 |
| channel_not_found | 频道ID错误 | 确认ID格式（C/G/D开头） |

## 依赖说明(补充)

| 依赖项 | 类型 | 必需 | 说明 |
|---:|:---|---:|---:|
| LLM | 模型 | 是 | 需要LLM进行智能审查, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

## 案例展示

### 文件管理

```bash
# 列出文件（按频道、用户、类型过滤）
sgw slack file list --count 100
sgw slack file list --channel C0123456789 --user U0123456789 --types images,pdfs
# ...
# 上传文件
sgw slack file upload --file ./example.txt --channel C0123456789 --title '示例文件'
# ...
# 查看文件信息
sgw slack file view F0123456789
# ...
# 删除文件
sgw slack file delete F0123456789
```

### 定时消息

```bash
# 创建定时消息
sgw slack schedule create --channel C0123456789 --text '每日站会提醒' --post-at 1734567890
# ...
# 列出定时消息
sgw slack schedule list
# ...
# 删除定时消息
sgw slack schedule delete --channel C0123456789 --id Q1234567890
```

### 表情反应与书签

```bash
# 添加反应
sgw slack reaction add --channel C0123456789 --ts 1234567890.123456 --emoji thumbsup
# ...
# 查看消息上的反应
sgw slack reaction get --channel C0123456789 --ts 1234567890.123456
# ...
# 添加书签
sgw slack bookmark add --channel C0123456789 --title '团队手册' --type link --link https://example.com/handbook
# ...
# 编辑书签
sgw slack bookmark edit --channel C0123456789 --bookmark-id Bk0123456789 --title '更新标题'
# ...
# 置顶消息
sgw slack pin add --channel C0123456789 --ts 1234567890.123456
```

### Python 全功能调用

```python
import os
import requests
# ...
api_key = os.environ['SGW_API_KEY']
base = 'https://api.slack-gateway.com/slack/api'
# ...
# 搜索消息
resp = requests.get(f'{base}/search.messages',
    headers={'Authorization': f'Bearer {api_key}'},
    params={'query': '产品发布'})
print(resp.json())
# ...
# 上传文件
with open('./report.pdf', 'rb') as f:
    resp = requests.post(f'{base}/files.upload',
        headers={'Authorization': f'Bearer {api_key}'},
        data={'channels': 'C0123456789', 'title': '月度报告'},
        files={'file': f})
print(resp.json())
```

## 常见问题

### Q1：批量操作部分失败如何处理？
A：批量结果按项返回状态。失败项可单独重试。常见失败原因包括频道不存在、权限不足、速率限制.
### 错误恢复步骤
| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制
A：单文件最大1GB（v2接口）。大文件建议使用`files.getUploadURLExternal`分片上传.
### Q3：搜索结果不全怎么办？
A：新上传文件与消息有索引延迟（通常几分钟）。搜索支持Slack查询语法细化结果，如`in:#channel from:@user`.
### Q4：定时消息时区如何处理？
A：`post_at`使用Unix时间戳（UTC）。按本地时区计算后转换为UTC时间戳传入.
### Q5：多工作区如何避免发错？
A：始终指定`--connection`或`Maton-Connection`头。默认连接可能与预期不符，显式指定最安全.
### Q6：可以与现有Slack App共存吗？
A：可以。本工具通过托管OAuth建立独立连接，不影响现有Slack App。两者可并行使用同一工作区.
### Q7：如何对接MCP工具生态？
A：专业版提供MCP端点集成适配，MCP工具通过本工具调用Slack API。配置MCP server时指定网关地址与API Key，MCP端点即可操作Slack全部能力.
### Q8：审计日志保留多久？
A：默认保留90天，可配置延长至1年。日志支持导出为JSONL格式供长期归档.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 搜索结果依赖第三方搜索引擎的可用性
- 免费版有搜索次数限制，高频使用可能被限流
