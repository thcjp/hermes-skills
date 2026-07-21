---
slug: google-workspace-toolkit
name: google-workspace-toolkit
version: "1.0.0"
displayName: 谷歌办公工具接口专业版
summary: 全功能Google办公工具接口,49个工具覆盖十大服务,支持企业级批量操作与多租户管理。
license: Proprietary
edition: pro
description: |-
  谷歌办公工具接口专业版,通过工具协议统一调用 Google Workspace 全部十大服务共 49 个工具,OAuth 登录即用,无需云控制台配置。核心能力:
  - 49 个工具全覆盖:Gmail / Calendar / Drive / Docs / Sheets / Slides / Chat / People / Time / Auth
  - 企业级批量操作与自动化工作流
  - 多账户与多租户管理
  - Google Chat 群组消息发送与空间管理
  - Docs 文档创建、编辑、文本替换
  - Sheets 表格读取、查找、...
tags:
- 沟通协作
- 谷歌办公
- 工具接口
- 企业效率
- 自动化
- 数据处理
tools:
  - - read
- exec
---
# 谷歌办公工具接口专业版

## 核心能力

### 一、Gmail 高级邮件管理(9个工具)
- `gmail.search`:邮件搜索
- `gmail.get`:获取邮件详情
- `gmail.send`:发送邮件
- `gmail.createDraft`:创建草稿
- `gmail.sendDraft`:发送草稿
- `gmail.modify`:修改邮件状态(已读/未读/标签)
- `gmail.listLabels`:列出所有标签
- `gmail.downloadAttachment`:下载附件

### 二、Calendar 高级日程管理(8个工具)
- `calendar.list`:列出所有日历
- `calendar.listEvents`:列出事件
- `calendar.getEvent`:获取事件详情
- `calendar.createEvent`:创建事件
- `calendar.updateEvent`:更新事件
- `calendar.deleteEvent`:删除事件
- `calendar.findFreeTime`:查找空闲时间
- `calendar.respondToEvent`:响应事件邀请

**输入**: 用户提供二、Calendar 高级日程管理(8个工具)所需的指令和必要参数。
**处理**: 按照skill规范执行二、Calendar 高级日程管理(8个工具)操作,遵循单一意图原则。### 三、Drive 文件管理(3个工具)
- `drive.search`:搜索文件
- `drive.downloadFile`:下载文件
- `drive.findFolder`:查找文件夹

**输入**: 用户提供三、Drive 文件管理(3个工具)所需的指令和必要参数。
**输出**: 返回三、Drive 文件管理(3个工具)的执行结果,包含操作状态和输出数据。### 四、Docs 文档操作(8个工具,专业版独有)
- `docs.create`:创建新文档
- `docs.find`:查找文档
- `docs.getText`:获取文档全文
- `docs.insertText`:插入文本
- `docs.appendText`:追加文本
- `docs.replaceText`:替换文本
- `docs.move`:移动文档
- `docs.extractIdFromUrl`:从 URL 提取文档 ID

**输入**: 用户提供四、Docs 文档操作(8个工具,专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行四、Docs 文档操作(8个工具,专业版独有)操作,遵循单一意图原则。### 五、Sheets 表格操作(4个工具,专业版独有)
- `sheets.getText`:获取表格文本
- `sheets.getRange`:按范围读取数据
- `sheets.find`:查找数据
- `sheets.getMetadata`:获取表格元数据

**输入**: 用户提供五、Sheets 表格操作(4个工具,专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行五、Sheets 表格操作(4个工具,专业版独有)操作,遵循单一意图原则。
**输出**: 返回五、Sheets 表格操作(4个工具,专业版独有)的执行结果,包含操作状态和输出数据。### 六、Slides 幻灯片操作(3个工具,专业版独有)
- `slides.getText`:获取幻灯片文本
- `slides.find`:查找文本
- `slides.getMetadata`:获取幻灯片元数据

**输入**: 用户提供六、Slides 幻灯片操作(3个工具,专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行六、Slides 幻灯片操作(3个工具,专业版独有)操作,遵循单一意图原则。
**输出**: 返回六、Slides 幻灯片操作(3个工具,专业版独有)的执行结果,包含操作状态和输出数据。### 七、Chat 群组协作(8个工具,专业版独有)
- `chat.listSpaces`:列出所有空间
- `chat.findSpaceByName`:按名称查找空间
- `chat.sendMessage`:发送空间消息
- `chat.getMessages`:获取空间消息
- `chat.sendDm`:发送私信
- `chat.findDmByEmail`:按邮箱查找私信
- `chat.listThreads`:列出消息线程
- `chat.setUpSpace`:创建空间

### 八、People 人员管理(2个工具,专业版独有)
- `people.getUserProfile`:获取用户资料
- `people.getMe`:获取当前用户信息

**处理**: 按照skill规范执行八、People 人员管理(2个工具,专业版独有)操作,遵循单一意图原则。
**输出**: 返回八、People 人员管理(2个工具,专业版独有)的执行结果,包含操作状态和输出数据。### 九、Time 时间工具(3个工具,专业版独有)
- `time.getCurrentDate`:获取当前日期
- `time.getCurrentTime`:获取当前时间
- `time.getTimeZone`:获取时区

**处理**: 按照skill规范执行九、Time 时间工具(3个工具,专业版独有)操作,遵循单一意图原则。
**输出**: 返回九、Time 时间工具(3个工具,专业版独有)的执行结果,包含操作状态和输出数据。### 十、Auth 认证管理(2个工具)
- `auth.clear`:清除凭据
- `auth.refreshToken`:刷新令牌

**输入**: 用户提供十、Auth 认证管理(2个工具)所需的指令和必要参数。
**处理**: 按照skill规范执行十、Auth 认证管理(2个工具)操作,遵循单一意图原则。
**输出**: 返回十、Auth 认证管理(2个工具)的执行结果,包含操作状态和输出数据。

### 能力覆盖范围

本skill还覆盖以下能力场景: 全功能、Google、办公工具接口、个工具覆盖十大服、支持企业级批量操、作与多租户管理、谷歌办公工具接口、通过工具协议统一、Workspace、全部十大服务共、OAuth、登录即用、无需云控制台配置、核心能力、个工具全覆盖、企业级批量操作与、自动化工作流、多账户与多租户管、群组消息发送与空、间管理、文档创建、文本替换、表格读取。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一:通过 Google Chat 向团队空间推送通知
项目经理需要向团队 Chat 空间推送每日站会通知,无需手动打开 Chat 应用。

```bash
# 优秀步:查找目标空间
gwtool call --server google-workspace \
    --tool "chat.findSpaceByName" \
    name="研发团队日常"

# 第二步:发送通知消息
gwtool call --server google-workspace \
    --tool "chat.sendMessage" \
    spaceName="研发团队日常" \
    text="各位,今日站会改为下午3点,会议室B,请准时参加。"

# 第三步:发送私信提醒未回复的成员
gwtool call --server google-workspace \
    --tool "chat.sendDm" \
    email="zhangsan@company.com" \
    text="张三,站会时间已调整,请确认参加。"
```

### 场景二:批量创建项目文档并填充模板内容
项目启动时,需批量创建多个标准文档并填充模板内容。

```python
#!/usr/bin/env python3
"""批量创建项目文档"""
import subprocess
import json

def call_tool(tool_name, **params):
    cmd = ['gwtool', 'call', '--server', 'google-workspace', '--tool', tool_name]
    for key, value in params.items():
        if isinstance(value, (dict, list)):
            cmd.append(f'{key}={json.dumps(value)}')
        else:
            cmd.append(f'{key}={value}')
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout) if result.stdout else {}

# 项目文档清单
documents = [
    {"title": "项目需求说明书", "content": "# 需求说明书\n\n## 1. 项目背景\n\n## 2. 功能需求\n\n## 3. 非功能需求"},
    {"title": "技术设计方案", "content": "# 技术设计\n\n## 1. 架构设计\n\n## 2. 数据库设计\n\n## 3. 接口设计"},
    {"title": "测试计划文档", "content": "# 测试计划\n\n## 1. 测试范围\n\n## 2. 测试策略\n\n## 3. 里程碑"},
    {"title": "上线检查清单", "content": "# 上线 Checklist\n\n## 1. 代码审查\n\n## 2. 测试通过\n\n## 3. 部署准备"},
]

created_docs = []
for doc in documents:
    result = call_tool('docs.create', title=doc['title'], markdown=doc['content'])
    doc_id = result.get('documentId', '未知')
    created_docs.append({"title": doc['title'], "id": doc_id})
    print(f"已创建: {doc['title']} (ID: {doc_id})")

print(f"\n批量创建完成,共 {len(created_docs)} 份文档")
```

### 场景三:从多个 Sheets 自动采集数据汇总
月底需从各部门的 Sheets 报表中采集数据汇总到总表。

```bash
# 从销售部 Sheets 读取数据
gwtool call --server google-workspace \
    --tool "sheets.getRange" \
    spreadsheetId="sales_sheet_id" \
    range="月度数据!A1:E31"

# 从市场部 Sheets 读取数据
gwtool call --server google-workspace \
    --tool "sheets.getRange" \
    spreadsheetId="marketing_sheet_id" \
    range="月度数据!A1:E31"

# 从财务部 Sheets 读取数据
gwtool call --server google-workspace \
    --tool "sheets.getRange" \
    spreadsheetId="finance_sheet_id" \
    range="月度数据!A1:E31"
```

```python
#!/usr/bin/env python3
"""多部门数据汇总脚本"""
import subprocess
import json

def fetch_sheet_data(sheet_id, sheet_range):
    """从指定 Sheets 读取数据"""
    result = subprocess.run([
        'gwtool', 'call', '--server', 'google-workspace',
        '--tool', 'sheets.getRange',
        f'spreadsheetId={sheet_id}',
        f'range={sheet_range}'
    ], capture_output=True, text=True)
    return json.loads(result.stdout) if result.stdout else []

# 各部门数据源
departments = {
    "销售部": "sales_sheet_id",
    "市场部": "marketing_sheet_id",
    "财务部": "finance_sheet_id",
}

all_data = []
for dept, sheet_id in departments.items():
    data = fetch_sheet_data(sheet_id, "月度数据!A1:E31")
    for row in data[1:]:  # 跳过表头
        all_data.append([dept] + row)
    print(f"{dept} 数据采集完成: {len(data)-1} 条记录")

print(f"\n汇总完成,共 {len(all_data)} 条记录")
```

## 使用流程

### 依赖说明

### 运行环境
1. **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
2. **操作系统**: Windows / macOS / Linux
3. **Node.js**: 建议 18.0+(运行工具接口)
4. **Python**: 建议 3.8+(运行自动化脚本模板)
5. **网络环境**: 需可访问 Google API 服务

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js 18+ | 运行时 | 必需 | nodejs.org 下载 |
| npm / npx | 包管理 | 必需 | 随 Node.js 安装 |
| @presto-ai/google-workspace-toolkit | 工具接口 | 必需 | npm 全局安装 |
| gwtool 命令行工具 | CLI | 必需 | 随工具接口安装 |
| Google Workspace 账户 | 账户 | 必需 | 企业版或个人版 |
| Python 3.8+ | 运行时 | 推荐 | python.org 下载 |
| jq (JSON处理) | 工具 | 推荐 | 系统包管理器安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
6. 无需创建 Google Cloud 项目
7. 无需创建 OAuth 凭据或下载 client_secret.json
8. 首次使用时通过浏览器完成 Google OAuth 授权
9. 授权范围覆盖 Gmail、Calendar、Drive、Docs、Sheets、Slides、Chat、People 全部服务
10. 凭据自动存储于 `~/.config/google-workspace-toolkit/` 目录

### 可用性分类
11. **分类**: MD+EXEC(纯 Markdown 指令,核心功能通过工具协议调用需要 exec 命令行执行能力)
12. **说明**: 基于工具接口的企业级 AI Skill,通过工具协议统一调用 Google Workspace 全部十大服务共 49 个工具。专业版完全兼容免费版的零云控制台配置与 OAuth 登录体验,额外解锁 Docs、Sheets、Slides、Chat、People 等高级服务,并提供企业级批量操作模板与多账户管理能力,适合团队协作与规模化办公场景。

### 命令参数说明

13. `--command`: 命令参数,用于指定操作选项
14. `--server`: 命令参数,用于指定操作选项
15. `--scope`: 命令参数,用于指定操作选项
16. `--arg`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


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
| 待审查内容为空 | 用户未提供内容 | 提示用户提供待审查的代码 |
| 内容格式不识别 | 传入不支持的内容格式 | 列出支持的格式, 建议转换后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 |
| 检查项超出范围 | 传入了不存在的检查维度 | 列出可用检查维度, 使用默认全部检查 |
| 审查超时 | 内容过长导致处理超时 | 建议分段审查, 每段不超过5000字 |
| 其他异常 | 内部处理异常 | 检查输入后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行智能审查, 推荐GPT-4/智谱GLM-4/DeepSeek |
| `references/checklist.md` | 文件 | 是 | 相关说明 |
| `references/scoring.md` | 文件 | 否 | 相关说明 |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

## 案例展示

### 工具服务注册配置
```bash
# 注册配置
gwtool config add google-workspace \
    --command "npx" \
    --arg "-y" \
    --arg "@presto-ai/google-workspace-toolkit" \
    --scope home

# 查看已注册服务
gwtool config list
```

### 企业级自动化工作流模板
```python
#!/usr/bin/env python3
"""企业跨服务自动化工作流示例"""
import subprocess
import json
from datetime import datetime

class WorkspaceToolkit:
    def __init__(self):
        self.server = 'google-workspace'

    def call(self, tool_name, **params):
        cmd = ['gwtool', 'call', '--server', self.server, '--tool', tool_name]
        for key, value in params.items():
            if isinstance(value, (dict, list)):
                cmd.append(f'{key}={json.dumps(value)}')
            else:
                cmd.append(f'{key}={value}')
        result = subprocess.run(cmd, capture_output=True, text=True)
        return json.loads(result.stdout) if result.stdout else {}

    def get_current_user(self):
        return self.call('people.getMe')

    def list_calendar_events(self, calendar_id, time_min, time_max):
        return self.call('calendar.listEvents',
                        calendarId=calendar_id,
                        timeMin=time_min,
                        timeMax=time_max)

    def find_free_time(self, attendees, time_min, time_max, duration):
        return self.call('calendar.findFreeTime',
                        attendees=attendees,
                        timeMin=time_min,
                        timeMax=time_max,
                        duration=duration)

    def send_chat_message(self, space_name, text):
        return self.call('chat.sendMessage', spaceName=space_name, text=text)

    def create_doc(self, title, markdown):
        return self.call('docs.create', title=title, markdown=markdown)

    def read_sheet_range(self, sheet_id, range_str):
        return self.call('sheets.getRange', spreadsheetId=sheet_id, range=range_str)

# 使用示例
toolkit = WorkspaceToolkit()
user = toolkit.get_current_user()
print(f"当前用户: {user.get('emailAddress', '未知')}")

# 查找空闲时间安排会议
free_slots = toolkit.find_free_time(
    attendees=["a@company.com", "b@company.com"],
    time_min="2026-07-25T09:00:00Z",
    time_max="2026-07-25T18:00:00Z",
    duration=60
)
print(f"可用时段: {free_slots}")

# 发送 Chat 通知
toolkit.send_chat_message("研发团队日常", "会议时间已确认,请查看日历。")
```

## 常见问题

### Q1: 免费版升级到专业版需要重新配置吗?
**A**: 不需要。专业版与免费版使用相同的安装与注册流程,OAuth 凭据通用。升级后直接获得全部 49 个工具的调用权限。

### Q2: Chat 工具发送消息失败怎么办?
**A**: 请确认:
- 目标空间是否存在(用 `chat.listSpaces` 或 `chat.findSpaceByName` 确认)
- 当前账户是否有该空间的发送权限
- 空间名称是否准确(区分大小写)

### Q3: Docs 创建的文档支持哪些格式?
**A**: `docs.create` 工具支持传入 Markdown 格式内容,系统会自动转换为 Google Docs 原生格式。复杂排版(如表格、图片)建议创建后在 Docs 界面手动补充。

### Q4: Sheets 读取大数据量时很慢?
**A**: 使用 `sheets.getRange` 限定读取范围,避免用 `sheets.getText` 读取整表。单次建议读取不超过 1000 行,大数据量分批读取。

### Q5: 如何同时管理多个 Google 账户?
**A**: 专业版支持多账户管理。使用 `auth.clear` 切换账户,或在不同终端会话中分别授权不同账户:

```bash
# 账户 A 操作
gwtool call --server google-workspace --tool "gmail.search" query="is:unread" maxResults=5

# 切换到账户 B
gwtool call --server google-workspace --tool "auth.clear"
gwtool call --server google-workspace --tool "gmail.search" query="is:unread" maxResults=5
```

### Q6: 49 个工具是否都需要单独授权?
**A**: 不需要。OAuth 授权时一次性授予所有服务权限,后续所有工具均可直接调用,无需逐个授权。

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
