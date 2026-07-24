---
slug: "google-workspace-mcp"
name: "google-workspace-mcp"
version: 1.0.1
displayName: "Google Workspace MCP"
summary: "免Google Cloud Console配置,OAuth登录即用Gmail/Calendar/Drive/Docs/Sheets/Chat等49项工具,覆盖邮件、日历、文档、表格与联系人管理。"
license: "Proprietary"
description: |-
  通过 @presto-ai/google-workspace-mcp 以纯OAuth登录方式访问Google Workspace全家桶,跳过Cloud Console建项目、启用API、下载client_secret.json等繁琐步骤。支持Gmail邮件搜索收发、Calendar日程管理与空闲时段查找、Drive文件检索下载、Docs文档增改查、Sheets与Slides读取、Chat空间消息、People个人资料及Time时区查询共49个工具。适用于独立开发者日常办公自动化、企业团队协同排程、以及跨Google服务的自动化工作流编排.
tags:
  - 通用办公
  - Productivity
  - Google
  - 工具
  - 效率
  - 自动化
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"
---
# Google Workspace MCP

通过 `@presto-ai/google-workspace-mcp` 以OAuth登录访问Google Workspace,无需在Google Cloud Console创建项目、启用API或下载client_secret.json。首次使用时弹出浏览器完成Google授权,凭证保存在 `~/.config/google-workspace-mcp/`,后续调用直接复用.
传统接入Google API需建项目、逐个启用API、创建OAuth凭据、下载client_secret.json、配置重定向URI;本技能将上述步骤全部托管,登录Google账号即可开始调用49个工具.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Google Workspace MCP处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| Google Workspace MCPConsole配置 | 不支持 | 支持 |
| Google Workspace MCP表格与联系人管理 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

涵盖10类共49个工具,均通过 `mcporter call --server google-workspace --tool "<tool>"` 调用.
**Gmail 邮件(8项)**: `gmail.search` 按Gmail查询语法检索邮件; `gmail.get` 读取单封正文; `gmail.send` 直接发送; `gmail.createDraft` 与 `gmail.sendDraft` 草稿流转; `gmail.modify` 标记已读/加星/归档; `gmail.listLabels` 列出标签; `gmail.downloadAttachment` 下载附件.
**Calendar 日历(8项)**: `calendar.list` 列出所有日历; `calendar.listEvents` 按时间区间拉取事件; `calendar.getEvent` 查单事件; `calendar.createEvent`/`calendar.updateEvent`/`calendar.deleteEvent` 增删改; `calendar.findFreeTime` 按参会者与时长查找共同空闲; `calendar.respondToEvent` 回复邀请.
**Drive 云盘(3项)**: `drive.search` 按文件名/内容检索; `drive.downloadFile` 下载到本地路径; `drive.findFolder` 查找文件夹.
**Docs 文档(8项)**: `docs.create` 由Markdown新建文档; `docs.find` 检索; `docs.getText` 提取纯文本; `docs.insertText`/`docs.appendText`/`docs.replaceText` 插入/追加/替换; `docs.move` 移动; `docs.extractIdFromUrl` 从URL解析文档ID.
**Sheets 表格(4项)**: `sheets.getText` 读取整表文本; `sheets.getRange` 读取指定区域; `sheets.find` 检索; `sheets.getMetadata` 取元数据.
**Slides 幻灯片(3项)**: `slides.getText`/`slides.find`/`slides.getMetadata` 读取文本与元数据(仅读取,不可编辑).
**Chat 聊天(8项)**: `chat.listSpaces`/`chat.findSpaceByName` 空间检索; `chat.sendMessage`/`chat.sendDm` 发消息; `chat.getMessages`/`chat.listThreads` 拉取历史; `chat.findDmByEmail` 按邮箱找私信; `chat.setUpSpace` 创建空间.
**People 联系人(2项)**: `people.getUserProfile`/`people.getMe` 获取用户资料.
**Time 时间(3项)**: `time.getCurrentDate`/`time.getCurrentTime`/`time.getTimeZone` 获取当前日期、时间与时区.
**Auth 鉴权(2项)**: `auth.clear` 清除凭证触发重新授权; `auth.refreshToken` 刷新令牌.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`google-workspace-mcp`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 安装与授权

```bash
npm install -g @presto-ai/google-workspace-mcp
mcporter config add google-workspace --command "npx" --arg "-y" --arg "@presto-ai/google-workspace-mcp" --scope home
```

首次调用任意工具会打开浏览器请求Google授权,完成后凭证写入 `~/.config/google-workspace-mcp/`.
## 常用命令

### Gmail

```bash
mcporter call --server google-workspace --tool "gmail.search" query="is:unread" maxResults=10
mcporter call --server google-workspace --tool "gmail.get" messageId="18c1f3a2b5d4e6f7"
mcporter call --server google-workspace --tool "gmail.send" to="team@corp.com" subject="周报" body="本周进展如下"
mcporter call --server google-workspace --tool "gmail.createDraft" to="review@corp.com" subject="审阅请求" body="请确认附件"
```

### Calendar

```bash
mcporter call --server google-workspace --tool "calendar.list"
mcporter call --server google-workspace --tool "calendar.listEvents" calendarId="primary" timeMin="2026-07-20T00:00:00Z" timeMax="2026-07-20T23:59:59Z"
mcporter call --server google-workspace --tool "calendar.createEvent" calendarId="primary" summary="评审会" start='{"dateTime":"2026-07-21T10:00:00+08:00"}' end='{"dateTime":"2026-07-21T11:00:00+08:00"}'
mcporter call --server google-workspace --tool "calendar.findFreeTime" attendees='["a@corp.com","b@corp.com"]' timeMin="2026-07-21T09:00:00+08:00" timeMax="2026-07-21T18:00:00+08:00" duration=60
```

### Drive / Docs / Sheets

```bash
mcporter call --server google-workspace --tool "drive.search" query="季度财报"
mcporter call --server google-workspace --tool "drive.downloadFile" fileId="1A2B3C4D5E6F" localPath="/tmp/report.pdf"
mcporter call --server google-workspace --tool "docs.find" query="会议纪要"
mcporter call --server google-workspace --tool "docs.getText" documentId="1A2B3C4D5E6F"
mcporter call --server google-workspace --tool "docs.create" title="需求文档" markdown="# 背景\n本次需求..."
mcporter call --server google-workspace --tool "sheets.getRange" spreadsheetId="1A2B3C4D5E6F" range="Sheet1!A1:D20"
```

### Chat

```bash
mcporter call --server google-workspace --tool "chat.listSpaces"
mcporter call --server google-workspace --tool "chat.findSpaceByName" name="项目协调"
mcporter call --server google-workspace --tool "chat.sendMessage" spaceName="spaces/AAAA123" text="部署已完成"
mcporter call --server google-workspace --tool "chat.sendDm" email="colleague@corp.com" text="请查看最新方案"
mcporter call --server google-workspace --tool "chat.getMessages" spaceName="spaces/AAAA123" maxResults=20
mcporter call --server google-workspace --tool "chat.setUpSpace" name="新项目空间" users='["a@corp.com","b@corp.com"]'
```

### People / Time / Slides

```bash
mcporter call --server google-workspace --tool "people.getMe"
mcporter call --server google-workspace --tool "people.getUserProfile" email="manager@corp.com"
mcporter call --server google-workspace --tool "time.getCurrentDate"
mcporter call --server google-workspace --tool "time.getTimeZone"
mcporter call --server google-workspace --tool "slides.getText" presentationId="1A2B3C4D5E6F"
mcporter call --server google-workspace --tool "slides.find" presentationId="1A2B3C4D5E6F" query="季度目标"
mcporter call --server google-workspace --tool "slides.getMetadata" presentationId="1A2B3C4D5E6F"
```

### 鉴权与维护

```bash
mcporter call --server google-workspace --tool "auth.refreshToken"
mcporter call --server google-workspace --tool "auth.clear"
rm -rf ~/.config/google-workspace-mcp
```

`auth.refreshToken` 用于令牌临近过期时主动续期; `auth.clear` 清除凭证后下一次调用会重新弹出浏览器授权; 彻底重置可删除凭证目录.
## 适用场景

- **邮件批处理**: 检索未读或特定标签邮件,按主题分类后批量回复或归档,适合每日清空收件箱的自动化与按规则过滤后统一处理.
- **日程协同排期**: 查找多位参会者的共同空闲时段并一键创建会议邀请,适合跨时区团队约会与外部客户拜访安排.
- **文档知识检索**: 跨Drive与Docs搜索会议纪要、方案文档,提取要点汇总结论,适合会前快速准备与项目资料归档.
- **表格数据读取**: 读取Sheets指定区域数据用于下游分析或报表生成,适合财务与运营数据流转到本地处理流程.
## 使用案例

### 案例一: 晨会简报自动生成

每日晨会前汇总当日日程、重要未读邮件与昨日会议纪要,合并为简报文本.
操作:
- `calendar.listEvents` 拉取 `calendarId="primary"` 当日 09:00-18:00 事件
- `gmail.search` 查询 `is:unread label:important maxResults=10`
- `docs.find` 搜索 `query="会议纪要"` 后 `docs.getText` 提取正文要点
- 将日程列表、邮件摘要、纪要结论合并输出

### 案例二: 财报审阅与回复

审阅云盘中的季度财报并起草回复邮件.
操作:
- `drive.search` 检索 `query="季度财报 PDF"`
- `drive.downloadFile` 下载到 `/tmp/report.pdf`
- `sheets.getRange` 读取配套财务表 `Sheet1!A1:D20` 区域
- `gmail.createDraft` 起草回复邮件附上数据要点,人工确认后 `gmail.sendDraft` 发送

### 案例三: 跨团队会议排期

为多部门协作会议寻找共同空闲时段并发邀请.
操作:
- `chat.findDmByEmail` 确认参会者邮箱对应的Chat身份
- `calendar.findFreeTime` 传入 `attendees=["a@corp.com","b@corp.com"]`、`duration=60` 与时间区间
- `calendar.createEvent` 在返回的空闲时段创建事件并自动发送邀请

## 异常处理

- **OAuth令牌过期**: 工具返回401或未授权时,调用 `auth.refreshToken` 刷新; 仍失败则 `auth.clear` 后重新触发浏览器授权.
- **首次授权浏览器未弹出**: 确认系统默认浏览器已设置且非headless环境; 远程SSH场景需配置浏览器重定向或本地授权后复制凭证目录.
- **gmail.search 返回空**: 校验查询语法(如 `is:unread`、`from:`、`after:`),放宽时间或标签条件; Gmail查询不支持正则,仅支持其原生搜索运算符.
- **calendar.findFreeTime 无结果**: 参会者需已共享日历或同域; 否则只能基于主日历推断,建议改用 `calendar.listEvents` 逐人比对.
- **drive.downloadFile 写入失败**: `localPath` 所在目录无写权限时更换到 `/tmp` 或用户目录; 文件过大受Google导出配额限制需分批下载.
- **docs.insertText 索引越界**: 插入位置需基于当前文档长度,先 `docs.getText` 校验边界; `documentId` 须为Docs ID而非Drive文件ID.
- **sheets.getRange 范围超界**: 工作表名需与实际一致(默认 `Sheet1`),区域引用如 `Sheet1!A1:B10`; 超出已用区域返回空值而非报错.
- **chat.sendMessage 权限不足**: 仅可向已加入的Space发消息,未加入时先 `chat.setUpSpace` 或由空间管理员添加; 应用需具备Chat OAuth scope.
| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ;确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 对照使用流程章节检查输入格式;参考示例章节修正输入 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述,补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 对照依赖说明章节确认环境配置;检查命令权限设置 |

## 常见问题

**是否必须创建Google Cloud项目?**
不需要。本技能通过托管OAuth绕过Cloud Console建项目、启用API、配置凭据等步骤,只需浏览器登录Google账号即可.
**凭证存储在哪里? 如何多账号切换?**
凭证保存在 `~/.config/google-workspace-mcp/`。切换账号时执行 `auth.clear` 清除当前凭证,再次调用工具会触发新账号的浏览器授权流程.
**支持Google Workspace企业账号吗?**
支持,前提是企业管理员未在第三方应用访问策略中禁用相应API scope; 受限scope可能需管理员单独审批.
**调用频率受限怎么办?**
受Google API配额约束,批量操作(如循环发邮件)建议每次间隔并做错误重试; 高频场景可考虑申请Google配额提升.
**能否编辑Sheets与Slides?**
当前Sheets仅支持读取(getText/getRange/find/getMetadata),Slides同样仅读取; 写入需求可结合Docs的Markdown转换间接实现.
**Chat消息支持富文本与卡片吗?**
`chat.sendMessage` 支持简单文本; 卡片消息需自行构造Chat API的卡片JSON,本技能未提供高层封装.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖网络与Google服务可用性,离线不可用.
- OAuth令牌有有效期,长时间未使用可能需重新授权.
- 企业Workspace账号的管理员策略可能限制第三方应用与部分scope.
- Slides与Sheets当前仅支持读取,无法直接写入或格式化.
- Chat仅覆盖Google Chat空间与私信,不包含外部IM平台.
- `calendar.findFreeTime` 对未共享日历的参会者只能基于主日历推断,准确度有限.
- 凭证以本地文件形式存储,迁移设备时需手动复制 `~/.config/google-workspace-mcp/` 目录.
- Gmail单次搜索maxResults受API上限约束,大批量拉取需分页或缩小查询条件.
- Docs的 `docs.replaceText` 为全量替换,不支持正则; 复杂改写需先读取全文再构造新内容.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Google Workspace MCP处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "google-workspace-mcp"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
