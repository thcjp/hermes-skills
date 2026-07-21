---
slug: feishu-send-file
name: feishu-send-file
version: "1.2.1"
displayName: feishu-send-file
summary: 飞书发送文件技能。用于通过飞书向用户发送普通文件附件（HTML、ZIP、PDF、代码文件等）以及处理“本地图片路径被发成路径文本”的可靠补救场景。普通文件必须先上传获取
  `file_key` 再...
license: MIT-0
description: |-
  飞书发送文件技能。用于通过飞书向用户发送普通文件附件（HTML、ZIP、PDF、代码文件等）以及处理“本地图片路径被发成路径文本”的可靠补救场景。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。
tags:
- Communication
- Creative
tools:
  - - read
- exec
---

# feishu-send-file

飞书机器人发送普通文件（非图片/视频）需要两步：先上传文件获取 file_key，再用 file_key 发消息。

如果本地图片通过常规 `message` / `media` 路径发送后，用户在飞书里看到的是 `/root/...png` 路径文本而不是图片本体，不要继续重试同一种方式；直接改走本技能的**稳定图片上传脚本**。

## 快速流程

### 方式一：用脚本（推荐）

```bash
python3 scripts/send_file.py <file_path> <open_id> <app_id> <app_secret> [file_name]
```

**参数说明：**

* `file_path`: 要发送的文件路径（HTML/PDF/ZIP/代码文件等）
* `open_id`: 接收者的 open_id（从 inbound_meta 的 chat_id 字段获取，格式为 `user:ou_xxx`，取 `ou_xxx` 部分）
* `app_id`: 飞书应用 ID（从 `skill-platform.json` 的 `channels.feishu.appId` 读取）
* `app_secret`: 飞书应用密钥（从 `skill-platform.json` 的 `channels.feishu.appSecret` 读取）
* `file_name`: 可选，自定义文件名（不填则用原文件名）

**快速获取配置：**

```bash
grep -A 2 '"feishu"' /root/.skill-platform/skill-platform.json | grep -E '(appId|appSecret)'
```

**完整示例：**

```bash
python3 /root/.skill-platform/workspace/skills/feishu-send-file/scripts/send_file.py \
  /root/myfiles/report.html \
  <USER_OPEN_ID> \
  <YOUR_APP_ID> \
  <YOUR_APP_SECRET> \
  report.html
```

**AI 助手使用示例：**

```python
exec(f"""
python3 /root/.skill-platform/workspace/skills/feishu-send-file/scripts/send_file.py \\
  {file_path} \\
  {user_open_id} \\
  {app_id} \\
  {app_secret} \\
  {custom_filename}
""")
```

### 方式二：手动两步

**Step 1 - 上传文件：**

```bash
TOKEN=$(curl -s -X POST "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal" \
  -H "Content-Type: application/json" \
  -d '{"app_id":"<APP_ID>","app_secret":"<APP_SECRET>"}' | python3 -c "import json,sys; print(json.load(sys.stdin)['tenant_access_token'])")

FILE_KEY=$(curl -s -X POST "https://open.feishu.cn/open-apis/im/v1/files" \
  -H "Authorization: Bearer $TOKEN" \
  -F "file_type=stream" \
  -F "file_name=<文件名>" \
  -F "file=@<文件路径>" | python3 -c "import json,sys; print(json.load(sys.stdin)['data']['file_key'])")
```

**Step 2 - 发送消息：**

```bash
curl -s -X POST "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"receive_id\":\"<OPEN_ID>\",\"msg_type\":\"file\",\"content\":\"{\\\"file_key\\\":\\\"$FILE_KEY\\\"}\"}"
```

## 稳定发送图片（2026-03-15 补充）

### 什么时候不要再硬用 `message` + `media`

如果你把本地图片路径（尤其是 `/root/myfiles/...`）传给飞书消息链路后，用户在飞书里看到的是：

* `📎 /root/myfiles/xxx.png`
* 或纯本地路径文本

那就说明这次**没有真正发成图片**。不要继续重试同一种参数组合。

### 原因（真实世界版）

* 飞书真正的图片消息不是“把本地路径塞给消息发送器”
* 正路是：**先上传到 `im/v1/images`，拿到 `image_key`，再发送 `msg_type=image`**
* Skill平台 / Feishu 插件在某些本地路径场景下（特别是 `/root/myfiles/...`）可能无法走通本地媒体上传链路，随后自动降级成把路径文本发出去
* 所以：`messageId` 返回成功 **不等于** 用户真的看到了图片

### 成功标准

**只有一个成功标准：用户在飞书里实际看到图片本体。**

如果回显的是路径文本，就视为失败。

### 推荐脚本（稳定版）

```bash
python3 scripts/send_image.py <image_path> <open_id> <app_id> <app_secret> [domain]
```

示例：

```bash
python3 /root/.skill-platform/workspace/skills/feishu-send-file/scripts/send_image.py \
  /root/myfiles/generated-images/demo.png \
  <USER_OPEN_ID> \
  <YOUR_APP_ID> \
  <YOUR_APP_SECRET>
```

如果是国际版 Lark：

```bash
python3 scripts/send_image.py <image_path> <open_id> <app_id> <app_secret> lark
```

### 这和普通文件的区别

* **普通文件**：`im/v1/files` -> `file_key` -> `msg_type=file`
* **图片**：`im/v1/images` -> `image_key` -> `msg_type=image`

这两条链路不要混用。

## 注意事项

* **普通文件**：必须走本技能的两步流程，直接用 `filePath` 参数只会显示路径
* **图片**：理论上 `message` tool 的 `media` 参数可以工作；但如果用户看到的是路径文本而不是图片本体，立刻改用 `scripts/send_image.py`
* **不要把 `/root/myfiles/...` 本地路径回显误判为发送成功**
* `receive_id_type=open_id` 对应个人用户；群聊用 `chat_id` 并替换类型
* 飞书 file_type 用 `stream` 适用于所有普通文件类型

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 用于通过飞书向用户发送普通文件附件（HTML、ZIP、PDF、代码文件等）以及处理“本地图片路径被发成路径文本”的可靠补救场景
- 普通文件必须先上传获取
  `file_key` 再
- 触发关键词: 技能, feishu-send-file, feishu, file, 通文件附件, 用于通过飞书, send, html

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用feishu-send-file？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: feishu-send-file有什么限制？
A: 请参考已知限制章节了解具体限制。
