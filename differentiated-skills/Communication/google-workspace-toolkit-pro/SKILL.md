---
slug: google-workspace-toolkit-pro
name: google-workspace-toolkit-pro
version: "1.0.0"
displayName: 谷歌办公工具接口专业版
summary: 全功能Google办公工具接口,49个工具覆盖十大服务,支持企业级批量操作与多租户管理。
license: MIT
edition: pro
description: |-
  谷歌办公工具接口专业版,通过工具协议统一调用 Google Workspace 全部十大服务共 49 个工具,OAuth 登录即用,无需云控制台配置。

  核心能力:
  - 49 个工具全覆盖:Gmail / Calendar / Drive / Docs / Sheets / Slides / Chat / People / Time / Auth
  - 企业级批量操作与自动化工作流
  - 多账户与多租户管理
  - Google Chat 群组消息发送与空间管理
  - Docs 文档创建、编辑、文本替换
  - Sheets 表格读取、查找、元数据管理
  - Slides 幻灯片文本提取与查找

  适用场景:
  - 企业跨部门协作与消息通知
  - 团队文档批量创建与内容更新
  - 数据报表自动化采集与汇总
  - 会议安排与参会人空闲时间协调

  差异化:专业版完全兼容免费版工具调用方式,额外解锁 Docs、Sheets、Slides、Chat、People 等高级服务共 39 个工具,并提供企业级批量操作模板与多账户管理能力,适合团队协作与规模化办公场景。

  触发关键词: gmail, google, workspace, docs, sheets, slides, chat, 邮件, 日历, drive, 工具接口, 工具协议, 批量, 企业, 自动化
tags:
- 沟通协作
- 谷歌办公
- 工具接口
- 企业效率
- 自动化
- 数据处理
tools:
- read
- exec
---

# 谷歌办公工具接口 - 专业版

## 概述

谷歌办公工具接口专业版是一款全功能 Google Workspace 工具协议调用方案。在完全兼容免费版零配置 OAuth 登录体验的基础上,专业版解锁了全部 49 个工具,覆盖 Gmail、Calendar、Drive、Docs、Sheets、Slides、Chat、People、Time、Auth 十大服务。

无论是通过 Google Chat 向团队群组推送通知、批量创建与编辑 Docs 文档、从 Sheets 自动采集数据报表,还是协调多位参会人的会议时间,专业版都能通过统一的工具协议高效完成。

### 免费版与专业版能力对比

| 服务模块 | 免费版工具数 | 专业版工具数 | 新增能力 |
|:---------|:-------------|:-------------|:---------|
| Auth 认证 | 0 | 2 | 凭据清除、令牌刷新 |
| Gmail 邮件 | 4 | 9 | 草稿发送、标签管理、附件下载 |
| Calendar 日历 | 4 | 8 | 事件更新/删除、响应事件 |
| Drive 文件 | 2 | 3 | 文件夹查找 |
| Docs 文档 | 0 | 8 | 创建、查找、插入、追加、替换文本 |
| Sheets 表格 | 0 | 4 | 文本获取、范围读取、查找、元数据 |
| Slides 幻灯片 | 0 | 3 | 文本获取、查找、元数据 |
| Chat 群组 | 0 | 8 | 空间列表、消息发送、私信、线程 |
| People 人员 | 0 | 2 | 用户资料、当前用户 |
| Time 时间 | 0 | 3 | 当前日期、时间、时区 |
| **合计** | **10** | **49** | 新增 39 个工具 |

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

### 三、Drive 文件管理(3个工具)

- `drive.search`:搜索文件
- `drive.downloadFile`:下载文件
- `drive.findFolder`:查找文件夹

### 四、Docs 文档操作(8个工具,专业版独有)

- `docs.create`:创建新文档
- `docs.find`:查找文档
- `docs.getText`:获取文档全文
- `docs.insertText`:插入文本
- `docs.appendText`:追加文本
- `docs.replaceText`:替换文本
- `docs.move`:移动文档
- `docs.extractIdFromUrl`:从 URL 提取文档 ID

### 五、Sheets 表格操作(4个工具,专业版独有)

- `sheets.getText`:获取表格文本
- `sheets.getRange`:按范围读取数据
- `sheets.find`:查找数据
- `sheets.getMetadata`:获取表格元数据

### 六、Slides 幻灯片操作(3个工具,专业版独有)

- `slides.getText`:获取幻灯片文本
- `slides.find`:查找文本
- `slides.getMetadata`:获取幻灯片元数据

### 七、Chat 群组协作(8个工具,专业版独有)

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

### 九、Time 时间工具(3个工具,专业版独有)

- `time.getCurrentDate`:获取当前日期
- `time.getCurrentTime`:获取当前时间
- `time.getTimeZone`:获取时区

### 十、Auth 认证管理(2个工具)

- `auth.clear`:清除凭据
- `auth.refreshToken`:刷新令牌

## 使用场景

### 场景一:通过 Google Chat 向团队空间推送通知

项目经理需要向团队 Chat 空间推送每日站会通知,无需手动打开 Chat 应用。

```bash
# 第一步:查找目标空间
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

## 快速开始

### 第一步:安装与注册(与免费版一致)

```bash
# 安装工具接口
npm install -g @presto-ai/google-workspace-toolkit

# 注册 Google Workspace 服务
gwtool config add google-workspace \
    --command "npx" \
    --arg "-y" \
    --arg "@presto-ai/google-workspace-toolkit" \
    --scope home
```

### 第二步:完成 OAuth 登录

```bash
# 首次调用触发 OAuth 登录
gwtool call --server google-workspace --tool "people.getMe"
```

### 第三步:验证高级服务可用性

```bash
# 验证 Docs
gwtool call --server google-workspace --tool "docs.find" query="测试"

# 验证 Sheets
gwtool call --server google-workspace --tool "sheets.getMetadata" spreadsheetId="<sheetId>"

# 验证 Chat
gwtool call --server google-workspace --tool "chat.listSpaces"

# 验证 Slides
gwtool call --server google-workspace --tool "slides.getMetadata" presentationId="<presentationId>"
```

## 配置示例

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

## 最佳实践

### 1. 批量操作加入重试与错误处理

企业级操作涉及多个工具调用,务必对每次调用做错误捕获:

```python
def safe_call(toolkit, tool_name, max_retries=3, **params):
    """带重试机制的工具调用"""
    for attempt in range(max_retries):
        try:
            result = toolkit.call(tool_name, **params)
            if result:
                return result
        except Exception as e:
            print(f"[重试 {attempt+1}/{max_retries}] {tool_name} 调用失败: {e}")
    print(f"[失败] {tool_name} 已达最大重试次数")
    return None
```

### 2. Chat 消息发送前确认空间名称

避免发错群组,发送前先查找确认空间:

```bash
# 先查找空间确认
gwtool call --server google-workspace --tool "chat.findSpaceByName" name="研发团队日常"

# 确认后再发送
gwtool call --server google-workspace --tool "chat.sendMessage" spaceName="研发团队日常" text="通知内容"
```

### 3. Docs 文档操作善用 URL 提取

从文档 URL 直接提取 ID,避免手动复制长 ID:

```bash
# 从 URL 提取文档 ID
gwtool call --server google-workspace \
    --tool "docs.extractIdFromUrl" \
    url="https://docs.google.com/document/d/1abc123/edit"

# 用提取的 ID 获取文档内容
gwtool call --server google-workspace --tool "docs.getText" documentId="1abc123"
```

### 4. Sheets 数据读取优先使用范围限定

避免一次性读取整表导致性能问题,优先用范围限定:

```bash
# 推荐:限定范围
gwtool call --server google-workspace \
    --tool "sheets.getRange" \
    spreadsheetId="<id>" \
    range="Sheet1!A1:E100"

# 不推荐:读取整表(数据量大时缓慢)
gwtool call --server google-workspace \
    --tool "sheets.getText" \
    spreadsheetId="<id>"
```

### 5. 多服务联动提升效率

结合 Time 工具实现动态时间查询:

```bash
# 获取当前日期
CURRENT_DATE=$(gwtool call --server google-workspace --tool "time.getCurrentDate" | jq -r '.date')

# 用当前日期查询日历
gwtool call --server google-workspace \
    --tool "calendar.listEvents" \
    calendarId="your@gmail.com" \
    timeMin="${CURRENT_DATE}T00:00:00Z" \
    timeMax="${CURRENT_DATE}T23:59:59Z"
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

## 依赖说明

### 运行环境

- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 建议 18.0+(运行工具接口)
- **Python**: 建议 3.8+(运行自动化脚本模板)
- **网络环境**: 需可访问 Google API 服务

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

- 无需创建 Google Cloud 项目
- 无需创建 OAuth 凭据或下载 client_secret.json
- 首次使用时通过浏览器完成 Google OAuth 授权
- 授权范围覆盖 Gmail、Calendar、Drive、Docs、Sheets、Slides、Chat、People 全部服务
- 凭据自动存储于 `~/.config/google-workspace-toolkit/` 目录

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,核心功能通过工具协议调用需要 exec 命令行执行能力)
- **说明**: 基于工具接口的企业级 AI Skill,通过工具协议统一调用 Google Workspace 全部十大服务共 49 个工具。专业版完全兼容免费版的零云控制台配置与 OAuth 登录体验,额外解锁 Docs、Sheets、Slides、Chat、People 等高级服务,并提供企业级批量操作模板与多账户管理能力,适合团队协作与规模化办公场景。
