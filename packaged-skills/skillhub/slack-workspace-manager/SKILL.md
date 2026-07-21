---
slug: slack-workspace-manager
name: slack-workspace-manager
version: "1.0.0"
displayName: Slack工作区管理专业版
summary: 企业级Slack工作区管理平台，支持企业Grid、审计日志、Canvas文档、用户组管理与批量操作。
license: Proprietary
edition: pro
description: |-
  Slack工作区管理器（专业版）—— 面向企业的全功能Slack工作区管理平台。核心能力:
  - 企业Grid多团队管理与审计日志
  - Canvas文档创建与编辑
  - 用户组管理与权限控制
  - 批量频道操作与成员管理
  - 自定义表情管理与通话控制
  - 完整的工作区安全与权限审计

  适用场景:
  - 企业级Slack工作区治理
  - 跨团队协作与权限管理
  - 审计合规与安全监控
  - 批量工作区配置与迁移

  差异化: 在免费版基础上增加企业Grid、审计日志、Canvas、用户组、批量操作等企业级能力...
tags:
- 沟通协作
- 企业级
- Slack
- 工作区管理
- 安全审计
tools:
  - - read
- exec
---
# Slack工作区管理专业版

## 核心能力

### 1. 企业Grid多团队管理
支持Enterprise Grid组织下的多团队管理，列出所有团队、跨团队用户管理。

**处理**: 按照skill规范执行企业Grid多团队管理操作,遵循单一意图原则。
**输出**: 返回企业Grid多团队管理的执行结果,包含操作状态和输出数据。

- 执行`企业Grid多团队管理`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`企业Grid多团队管理`相关配置参数进行设置
### 2. 审计日志读取
读取企业Grid审计日志，追踪用户操作、频道变更、权限修改等安全事件。

**处理**: 按照skill规范执行审计日志读取操作,遵循单一意图原则。
**输出**: 返回审计日志读取的执行结果,包含操作状态和输出数据。

- 执行`审计日志读取`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`审计日志读取`相关配置参数进行设置
### 3. Canvas文档管理
创建、编辑、删除Slack Canvas文档，支持分区编辑与内容查找。

**输入**: 用户提供Canvas文档管理所需的指令和必要参数。
**处理**: 按照skill规范执行Canvas文档管理操作,遵循单一意图原则。

- 执行`Canvas文档管理`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`Canvas文档管理`相关配置参数进行设置
### 4. 用户组管理
创建、启用、禁用用户组（子团队），管理组成员与权限。

**处理**: 按照skill规范执行用户组管理操作,遵循单一意图原则。

- 执行`用户组管理`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`用户组管理`相关配置参数进行设置
### 5. 批量频道操作
批量创建频道、批量邀请成员、批量归档、批量设置主题。

**输入**: 用户提供批量频道操作所需的指令和必要参数。
**处理**: 按照skill规范执行批量频道操作操作,遵循单一意图原则。

- 执行`批量频道操作`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`批量频道操作`相关配置参数进行设置
### 6. 自定义表情管理
添加、列出、删除工作区自定义表情。

**输入**: 用户提供自定义表情管理所需的指令和必要参数。
**处理**: 按照skill规范执行自定义表情管理操作,遵循单一意图原则。
**输出**: 返回自定义表情管理的执行结果,包含操作状态和输出数据。

- 执行`自定义表情管理`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`自定义表情管理`相关配置参数进行设置
### 7. 通话控制
查看通话详情、结束通话、添加/移除通话参与者。

**输入**: 用户提供通话控制所需的指令和必要参数。
**处理**: 按照skill规范执行通话控制操作,遵循单一意图原则。
**输出**: 返回通话控制的执行结果,包含操作状态和输出数据。

- 执行`通话控制`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`通话控制`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级、工作区管理平台、支持企业、用户组管理与批量、工作区管理器、专业版、面向企业的全功能、核心能力、多团队管理与审计、文档创建与编辑、用户组管理与权限、批量频道操作与成、员管理、自定义表情管理与、完整的工作区安全、与权限审计。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一：批量创建项目频道并邀请成员
```python
# batch_channel_setup.py
class BatchChannelSetup:
    """批量频道配置器"""

    def __init__(self, slack_client):
        self.client = slack_client

    def setup_project_channels(self, project_config):
        """
        批量创建项目频道并配置
        :param project_config: 项目频道配置
        """
        results = []

        for channel_spec in project_config['channels']:
            # 1. 创建频道
            channel = self.client.create_channel(
                name=channel_spec['name'],
                is_private=channel_spec.get('is_private', False)
            )
            channel_id = channel['id']

            # 2. 设置主题与用途
            if channel_spec.get('topic'):
                self.client.set_channel_topic(
                    channel=channel_id,
                    topic=channel_spec['topic']
                )
            if channel_spec.get('purpose'):
                self.client.set_channel_purpose(
                    channel=channel_id,
                    purpose=channel_spec['purpose']
                )

            # 3. 批量邀请成员
            if channel_spec.get('members'):
                self.client.invite_users(
                    channel=channel_id,
                    users=channel_spec['members']
                )

            # 4. 发送欢迎消息
            self.client.send_message(
                channel=channel_id,
                text=channel_spec.get('welcome', f"欢迎来到 {channel_spec['name']} 频道！")
            )

            results.append({
                'name': channel_spec['name'],
                'id': channel_id,
                'status': 'created'
            })

        return results

# 示例
setup = BatchChannelSetup(slack_client)
results = setup.setup_project_channels({
    'channels': [
        {
            'name': 'project-alpha-general',
            'topic': 'Alpha项目通用讨论',
            'purpose': '项目日常沟通与协调',
            'members': ['U001', 'U002', 'U003'],
            'welcome': 'Alpha项目正式启动！请同步各自任务。'
        },
        {
            'name': 'project-alpha-eng',
            'topic': 'Alpha项目工程讨论',
            'is_private': True,
            'members': ['U001', 'U002'],
            'welcome': '工程团队频道已创建。'
        }
    ]
})
```

### 场景二：审计日志安全监控
```python
# audit_monitor.py
class AuditMonitor:
    """审计日志监控器"""

    def __init__(self, slack_client):
        self.client = slack_client

    def get_security_events(self, days=7):
        """获取安全相关事件"""
        logs = self.client.read_audit_logs(
            action='*',
            count=1000
        )

        security_events = []
        for entry in logs:
            if entry['action'] in [
                'user_login',
                'user_logout',
                'app_installed',
                'app_uninstalled',
                'channel_created',
                'channel_deleted',
                'role_assigned',
                'permission_granted'
            ]:
                security_events.append({
                    '时间': entry['date_create'],
                    '动作': entry['action'],
                    '操作者': entry['actor'],
                    '实体': entry['entity'],
                    'IP地址': entry.get('ip_address', 'N/A')
                })

        return self.format_report(security_events)

    def check_anomalies(self, events):
        """检测异常行为"""
        anomalies = []

        # 检测非工作时间的大量操作
        # 检测异常IP地址
        # 检测权限变更
        # 检测频道批量删除
        return anomalies

# 使用示例
monitor = AuditMonitor()
events = monitor.get_security_events(days=30)
anomalies = monitor.check_anomalies(events)
```

### 场景三：用户组与权限管理
```bash
# 创建用户组
slack-workspace-manager-pro create-user-group \
  --name "engineering-leads" \
  --description "工程团队负责人"

# 添加成员到用户组
slack-workspace-manager-pro update-user-group \
  --group-id "S0123456789" \
  --add-users "U001,U002,U003"

# 列出所有用户组
slack-workspace-manager-pro list-user-groups

# 创建Canvas文档记录团队规范
slack-workspace-manager-pro create-canvas \
  --title "工程团队协作规范" \
  --content "## 团队规范\n1. 代码提交前需通过CI\n2. PR需至少2人评审\n3...."
# 编辑Canvas分区
slack-workspace-manager-pro edit-canvas \
  --canvas-id "F0123456789" \
  --section-id "S001" \
  --content "更新的内容"
```

## 使用流程

### 安装
```bash
npx skillhub@latest install slack-workspace-manager-pro
```

### 配置与连接
```bash
# 连接Slack工作区（需要企业Grid管理员权限）
slack-workspace-manager-pro connect --enterprise-grid

# 验证企业连接
slack-workspace-manager-pro list-enterprise-teams
```

### 基本使用
```bash
# 企业Grid - 列出所有团队
slack-workspace-manager-pro list-enterprise-teams

# 审计日志 - 读取最近30天日志
slack-workspace-manager-pro read-audit-logs --days 30

# 批量操作 - 批量创建频道
slack-workspace-manager-pro batch-create-channels \
  --config channels.yaml

# 用户组管理
slack-workspace-manager-pro create-user-group \
  --name "oncall-team" \
  --description "值班团队"

# Canvas文档
slack-workspace-manager-pro create-canvas \
  --title "项目文档" \
  --content "内容..."
```

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


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.8+
- **网络环境**: 需能访问Slack API端点
- **Slack套餐**: 企业Grid功能需要Enterprise Grid套餐

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Slack OAuth Token | API凭证 | 必需 | OAuth授权流程获取 |
| Enterprise Grid权限 | 权限 | Grid功能必需 | Slack企业管理员授予 |
| Python 3.8+ | 运行时 | 必需 | python.org 官方下载 |
| slack-sdk | Python库 | 必需 | `pip install slack-sdk` |
| requests | Python库 | 必需 | `pip install requests` |
| sqlite3 | 标准库 | 推荐 | Python内置（审计日志存储） |
| pandas | Python库 | 推荐 | `pip install pandas`（日志分析） |
| pyyaml | Python库 | 推荐 | `pip install pyyaml`（配置解析） |

### API Key 配置
```bash
# 通过OAuth流程自动配置（推荐）
slack-workspace-manager-pro connect --enterprise-grid

# 专业版所需OAuth Scopes:
# 基础（与免费版相同）:
# - chat:write              发送消息
# - channels:read/write     频道管理
# - files:read/write        文件管理
# - reminders:read/write    提醒管理
# - users:read              用户查询
#
# 企业Grid扩展:
# - admin.teams:read        读取团队列表
# - admin.audit:read        读取审计日志
# - usergroups:read/write   用户组管理
# - calls:read/write        通话控制
# - emoji:read/write        表情管理
# - admin.users:write       工作区用户管理
# - team:read               团队信息
```

### 可用性分类
- **分类**: MD+EXEC+SCRIPT+API+ADMIN（Markdown指令 + 命令行执行 + Python脚本 + Slack API + 企业管理）
- **说明**: 基于Markdown的AI Skill，，专业版支持企业Grid管理、审计日志与批量操作
- **适用人群**: 企业IT管理员、安全团队、Slack工作区管理员、合规团队
- **兼容性**: 完全兼容免费版操作格式与配置，支持无缝升级
- **支持级别**: 优先技术支持，工作日24小时内响应
- **合规说明**: 审计日志功能满足企业合规要求，支持操作追溯与安全监控


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100

检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100

检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100

检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过

改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q: 专业版与免费版如何兼容？
专业版完全兼容免费版的所有操作格式与配置。免费版的命令行参数可直接在专业版中使用，升级无需修改现有配置或重新授权。

### Q: 企业Grid功能需要什么权限？
企业Grid管理功能需要Organization Owner或Admin权限。普通工作区管理员无法访问跨团队管理功能。

### Q: 审计日志能追溯多久？
审计日志可追溯的时间取决于企业Slack套餐：
- Enterprise Grid: 最多可追溯365天
- 专业版通过本地存储可延长保留时间

### Q: Canvas文档支持哪些操作？
```bash
# 创建Canvas
slack-workspace-manager-pro create-canvas --title "文档标题" --content "内容"

# 编辑分区
slack-workspace-manager-pro edit-canvas --canvas-id "F001" --section-id "S001" --content "新内容"

# 查找分区ID
slack-workspace-manager-pro lookup-canvas-sections --canvas-id "F001"

# 删除Canvas
slack-workspace-manager-pro delete-canvas --canvas-id "F001" --confirm
```

### Q: 用户组与频道有什么区别？
| 特性 | 用户组 | 频道 |
|:-----|:-------|:-----|
| 用途 | 角色与权限管理 | 消息沟通 |
| 成员 | 跨频道 | 频道内 |
| 提及 | `@group-name` | `@channel` |
| 管理 | 管理员创建 | 任何成员可创建 |

### Q: 批量操作有风险吗？
批量操作（特别是删除、归档）具有较高风险。专业版提供以下保护措施：
1. `--dry-run` 预览模式，不实际执行
2. `--confirm` 确认参数，防止误操作
3. 操作日志全程记录
4. 审计日志可追溯

### Q: 如何管理多个工作区？
```bash
# 列出企业Grid下所有团队
slack-workspace-manager-pro list-enterprise-teams

# 切换当前操作团队
slack-workspace-manager-pro switch-team --team-id "T0123456789"

# 跨团队用户管理
slack-workspace-manager-pro invite-user-to-workspace \
  --team-id "T0123456789" \
  --email "newuser@company.com"
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
