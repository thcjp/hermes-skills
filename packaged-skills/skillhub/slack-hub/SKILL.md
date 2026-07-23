---
slug: "slack-hub"
name: "slack-hub"
version: "1.0.0"
displayName: "Slack Hub工具专业版"
summary: "企业级Slack集成工具，支持批量消息发送、高级搜索、限流处理、消息模板与工作区深度管理。"
license: "Proprietary"
edition: "pro"
description: |-
  Slack Hub工具（专业版）—— 面向团队和企业的全功能Slack集成工具。核心能力:
  - 批量消息发送与多频道分发
  - 高级搜索与结果过滤
  - 智能限流处理与重试机制
  - 消息模板库与变量替换
  - 工作区频道深度管理
  - 搜索结果导出与分析

  适用场景:
  - 企业级跨频道信息分发
  - 历史消息深度检索与归档
  - 高频消息推送的限流管理
  - 团队沟通模板标准化

  差异化: 在免费版基础上增加批量发送、高级搜索、限流处理、模板管理等企业级能力，完全兼容免费版操作格式
tags:
  - 沟通协作
  - 企业级
  - Slack
  - 搜索引擎
  - 批量处理
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# Slack Hub工具专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

### 1. 批量消息发送与多频道分发
支持向多个频道同时发送消息，按频道分组批量推送，并自动处理发送结果。

**输入**: 用户提供批量消息发送与多频道分发所需的指令和必要参数。- 验证执行结果，确认输出符合预期格式
- 参考`批量消息发送与多频道分发`相关配置参数进行设置
### 2. 高级搜索与结果过滤
支持按时间范围、频道、用户、文件类型等多维度过滤搜索结果，并提供搜索结果排序与分页。- 验证执行结果，确认输出符合预期格式
- 参考`高级搜索与结果过滤`相关配置参数进行设置
### 3. 智能限流处理
内置Slack API限流处理机制，自动识别`Retry-After`头部，智能调整请求频率，避免触发限流。

**输出**: 返回智能限流处理的执行结果,包含操作状态和输出数据。
### 4. 消息模板库
提供常用消息模板管理，支持变量替换、分类存储与团队共享。

**处理**: 按照skill规范执行消息模板库操作,遵循单一意图原则。
**输出**: 返回消息模板库的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`消息模板库`相关配置参数进行设置
### 5. 工作区频道深度管理
列出频道详情、成员列表、创建时间、主题等信息，支持频道分类与标签管理。

**输入**: 用户提供工作区频道深度管理所需的指令和必要参数。
**处理**: 按照skill规范执行工作区频道深度管理操作,遵循单一意图原则。- 验证执行结果，确认输出符合预期格式
- 参考`工作区频道深度管理`相关配置参数进行设置
### 6. 搜索结果导出
将搜索结果导出为CSV、JSON、Markdown等格式，便于归档与分析。

**输入**: 用户提供搜索结果导出所需的指令和必要参数。- 验证执行结果，确认输出符合预期格式
- 参考`搜索结果导出`相关配置参数进行设置
#
## 适用场景

### 场景一：企业公告批量分发
向多个团队频道同时发送重要公告，并自动处理限流。

```python
import time

class BatchDistributor:
    """批量消息分发器"""

    def __init__(self, slack_client):
        self.client = slack_client
        self.rate_limiter = RateLimiter()

    def distribute(self, message, channels, template_vars=None):
        """
        向多个频道分发消息
        :param message: 消息内容或模板
        :param channels: 频道ID或名称列表
        :param template_vars: 模板变量
        """
        if template_vars:
            message = self.apply_template(message, template_vars)

        results = []
        for channel in channels:
            self.rate_limiter.wait_if_needed()

            try:
                result = self.client.send_message(
                    channel=channel,
                    text=message
                )
                results.append({
                    'channel': channel,
                    'status': 'success',
                    'timestamp': result.get('ts')
                })
            except RateLimitError as e:
                wait_time = e.retry_after
                print(f"限流，等待{wait_time}秒后重试 [{channel}]")
                time.sleep(wait_time)
                result = self.client.send_message(channel=channel, text=message)
                results.append({
                    'channel': channel,
                    'status': 'success_after_retry',
                    'timestamp': result.get('ts')
                })
            except Exception as e:
                results.append({
                    'channel': channel,
                    'status': 'failed',
                    'error': str(e)
                })

        return self.generate_report(results)

class RateLimiter:
    """智能限流器"""

    def __init__(self, min_interval=1.0):
        self.min_interval = min_interval
        self.last_request = 0

    def wait_if_needed(self):
        """必要时等待"""
        elapsed = time.time() - self.last_request
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_request = time.time()

distributor = BatchDistributor(slack_client)
report = distributor.distribute(
    message="【系统维护通知】今晚22:00-24:00进行系统升级，届时服务暂停。",
    channels=["#engineering", "#product", "#support", "#general"],
)
```

### 场景二：高级历史消息搜索
```python
class AdvancedSearch:
    """高级搜索器"""

    def search(self, query, filters=None):
        """
        高级搜索
        :param query: 搜索关键词
        :param filters: 过滤条件
        """
        filters = filters or {}

        search_query = self.build_query(query, filters)

        results = self.client.search_messages(
            query=search_query,
            count=filters.get('max_results', 50),
            page=filters.get('page', 1)
        )

        filtered = self.apply_filters(results, filters)

        if filters.get('sort_by'):
            filtered = self.sort_results(filtered, filters['sort_by'])

        return filtered

    def build_query(self, query, filters):
        """构建高级查询"""
        parts = [query]

        if filters.get('channel'):
            parts.append(f"in:#{filters['channel']}")
        if filters.get('from_user'):
            parts.append(f"from:{filters['from_user']}")
        if filters.get('after'):
            parts.append(f"after:{filters['after']}")
        if filters.get('before'):
            parts.append(f"before:{filters['before']}")
        if filters.get('has_file'):
            parts.append("has:file")
        if filters.get('has_link'):
            parts.append("has:link")

        return " ".join(parts)

    def export_results(self, results, format='csv'):
        """导出搜索结果"""
        if format == 'csv':
            return self.export_csv(results)
        elif format == 'json':
            return self.export_json(results)
        elif format == 'markdown':
            return self.export_markdown(results)

searcher = AdvancedSearch()
results = searcher.search(
    query="部署文档",
    filters={
        'channel': 'engineering',
        'from_user': 'alice',
        'after': '2026-06-01',
        'before': '2026-07-01',
        'has_file': True,
        'sort_by': 'timestamp',
        'max_results': 100
    }
)
searcher.export_results(results, format='csv')
```

### 场景三：消息模板管理与发送
```bash
slack-hub-tool-pro template create \
  --name "上线通知" \
  --category "release" \
  --content "【上线通知】{project} v{version} 已部署到{environment}环境。变更内容：{changes}"

slack-hub-tool-pro template send \
  --name "上线通知" \
  --target "#engineering" \
  --vars '{"project":"Alpha","version":"2.1.0","environment":"生产","changes":"新增用户认证模块"}'

slack-hub-tool-pro template broadcast \
  --name "上线通知" \
  --targets "#engineering,#product,#support" \
  --vars '{"project":"Alpha","version":"2.1.0","environment":"生产","changes":"新增用户认证模块"}'
```

## 使用流程

### 安装
```bash
npx skillhub@latest install slack-hub-tool-pro
```

### 配置
```bash
SLACK_BOT_TOKEN=xoxb-your-bot-token-here
SLACK_APP_TOKEN=xapp-your-app-token-here
```

### 基本使用
```bash
slack-hub-tool-pro batch-send \
  --targets "#eng,#product,#support" \
  --message "重要通知：系统将于今晚维护"

slack-hub-tool-pro search \
  --query "部署文档" \
  --channel "engineering" \
  --after "2026-06-01" \
  --has-file \
  --sort-by timestamp

slack-hub-tool-pro search \
  --query "bug报告" \
  --export csv \
  --output bug_reports.csv

slack-hub-tool-pro channel-info --channel "C0123456789"
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | slack-hub处理的内容输入 |,  |
| content | string | 否 | slack-hub处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "hub 相关配置参数",
    result: "hub 相关配置参数",
    result: "hub 相关配置参数",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.8+
- **网络环境**: 需能访问Slack API端点

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Slack Bot Token | API凭证 | 必需 | Slack App管理页面创建 |
| Slack App Token | API凭证 | 必需 | 启用Socket Mode时需要 |
| Python 3.8+ | 运行时 | 必需 | python.org 官方下载 |
| slack-sdk | Python库 | 必需 | `pip install slack-sdk` |
| requests | Python库 | 必需 | `pip install requests` |
| jinja2 | Python库 | 推荐 | `pip install jinja2`（模板引擎） |
| sqlite3 | 标准库 | 推荐 | Python内置（模板存储） |

### API Key 配置
```bash
export SLACK_BOT_TOKEN="xoxb-your-bot-token-here"
export SLACK_APP_TOKEN="xapp-your-app-token-here"

```

### API 端点说明
本工具调用以下Slack Web API端点：
- `https://slack.com/api/chat.postMessage` - 发送消息
- `https://slack.com/api/search.messages` - 搜索消息
- `https://slack.com/api/search.files` - 搜索文件
- `https://slack.com/api/conversations.list` - 列出频道
- `https://slack.com/api/conversations.info` - 频道详情
- `https://slack.com/api/conversations.members` - 频道成员

所有端点均实现了限流处理与自动重试机制。

### 可用性分类
- **分类**: MD+EXEC+SCRIPT+API（Markdown指令 + 命令行执行 + Python脚本 + Slack API）
- **说明**: 基于Markdown的AI Skill，专业版支持批量操作、高级搜索与限流处理
- **适用人群**: 企业团队、项目经理、运营团队、Slack管理员
- **兼容性**: 完全兼容免费版操作格式与配置，支持无缝升级
- **支持级别**: 优先技术支持，工作日24小时内响应

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

### 示例2: 进阶用法
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

### Q: 专业版与免费版如何兼容？
专业版完全兼容免费版的所有操作格式与配置。免费版的命令行参数可直接在专业版中使用，升级无需修改现有配置。

### Q: 批量发送时如何避免触发限流？
专业版内置智能限流器，默认每秒发送1条消息。当收到Slack API的`Retry-After`响应时，会自动等待指定时间后重试。你也可以通过配置调整发送间隔。

### Q: 高级搜索支持哪些过滤条件？
| 过滤条件 | 参数 | 示例 |
|:---------|:-----|:-----|
| 频道 | `--channel` | `engineering` |
| 用户 | `--from` | `alice` |
| 时间起点 | `--after` | `2026-06-01` |
| 时间终点 | `--before` | `2026-07-01` |
| 包含文件 | `--has-file` | - |
| 包含链接 | `--has-link` | - |
| 排除词 | 查询中使用`-` | `部署 -测试` |

### Q: 搜索结果导出支持哪些格式？
支持CSV、JSON、Markdown三种格式。CSV适合Excel分析，JSON适合程序处理，Markdown适合文档归档。

### Q: 模板变量支持嵌套吗？
```python
template = "{project} v{version} 部署到 {environment}"

template = "{user}在{date}提交了{count}个变更"
```

### Q: 频道详情包含哪些信息？
```bash
slack-hub-tool-pro channel-info --channel "C0123456789"

```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

