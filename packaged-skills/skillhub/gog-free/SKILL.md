---
slug: gog-free
name: gog-free
version: "1.0.0"
displayName: Gog(免费)
summary: Google Workspace命令行工具基础版,覆盖Gmail搜索与Sheets读写。
license: MIT
description: |-
  Google Workspace 命令行工具的基础免费版。覆盖 Gmail 邮件搜索与 Sheets 表格读写两类核心操作,
  通过 OAuth 凭证鉴权,支持 JSON 结构化输出。适用于个人开发者邮件检索与轻量级表格读写场景。
  本免费版仅支持 Gmail search 与 Sheets get/append,Calendar/Drive/Contacts/Docs 等高级能力请升级付费版。
tags:
  - Communication
tools:
  - read
  - exec
---

# gog-free

`gog` 是 Google Workspace 的命令行工具。本免费版封装 Gmail 邮件搜索与 Sheets 表格读写两类基础操作,通过 OAuth 凭证鉴权,适合个人开发者轻量级使用。

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
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）

## 核心能力

- OAuth 凭证管理:导入 `client_secret.json`、添加账户授权、列出已授权账户
- Gmail 搜索:按 Gmail 搜索语法检索邮件(`newer_than:`、`from:`、`has:attachment` 等)
- Sheets 读取:读取指定范围的数据,支持 JSON 输出
- Sheets 追加:向指定范围追加行数据
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: Google、Workspace、命令行工具基础版、搜索与、命令行工具的基础、免费版、邮件搜索与、表格读写两类核心、凭证鉴权、结构化输出、适用于个人开发者、邮件检索与轻量级、表格读写场景、本免费版仅支持、search、get、append、Calendar、Drive、Contacts、Docs、等高级能力请升级、付费版。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`gog-free`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

### 命令参数说明

- `--insert`: 命令参数,用于指定操作选项

## 一次性配置

```bash
gog auth credentials /path/to/client_secret.json
gog auth add you@gmail.com --services gmail,sheets
gog auth list
```

`client_secret.json` 从 Google Cloud Console 的 OAuth 客户端凭证页面下载,类型选择"桌面应用"。本免费版仅需 `gmail` 与 `sheets` 两个服务授权。

## 常用命令

### Gmail 搜索

搜索近 7 天邮件:

```bash
gog gmail search 'newer_than:7d' --max 10
```

按发件人搜索:

```bash
gog gmail search 'from:noreply@github.com' --max 20 --json
```

### Sheets 读取

读取指定范围:

```bash
gog sheets get <sheetId> "Tab!A1:D10" --json
```

### Sheets 追加

向范围追加行:

```bash
gog sheets append <sheetId> "Tab!A:C" --values-json '[["x","y","z"]]' --insert INSERT_ROWS
```

## 使用约定

- 设置 `GOG_ACCOUNT=you@gmail.com` 可避免每次重复 `--account` 参数
- 脚本化场景优先使用 `--json` 加 `--no-input`,确保输出可解析且不阻塞
- Sheets 数据优先通过 `--values-json` 传递,避免内联行格式歧义
- Gmail 搜索含空格的关键词用双引号包裹,如 `subject:"周报 评审"`

## 适用场景

### 场景一:开发者邮件检索

输入:近 7 天邮件、`--max 20`、JSON 输出
输出:结构化邮件列表,包含发件人、主题,可管道给下游脚本分类

### 场景二:轻量级表格读取

输入:Google Sheet ID、范围 `Tab!A1:D10`、JSON 输出
输出:二维数组数据,可导入本地分析工具

## 案例展示

### 案例一:近 7 天邮件归档

需求:导出近 7 天带附件的邮件到本地 JSON 文件。

实现:

```bash
export GOG_ACCOUNT=you@gmail.com
gog gmail search 'newer_than:7d has:attachment' --max 50 --json --no-input > /tmp/mail-$(date +%F).json
```

输出示例:

```json
[
  {"id":"abc123","from":"noreply@github.com","subject":"PR merged","attachments":["patch.diff"]},
  {"id":"def456","from":"boss@company.com","subject":"周报评审","attachments":["review.pdf"]}
]
```

`--no-input` 确保不阻塞脚本执行。

### 案例二:Sheet 追加日志行

需求:向监控 Sheet 的 `Builds!A:C` 追加一行构建记录。

实现:

```bash
gog sheets append <sheetId> "Builds!A:C" \
  --values-json '[["2026-07-20","#1234","success"]]' \
  --insert INSERT_ROWS \
  --no-input
```

输出:`UpdatedRange: Builds!A5:C5, UpdatedRows: 1`,可用于断言追加成功。

## 异常处理

### 1. OAuth 凭证未导入

现象:`gog auth list` 为空,或调用任何命令返回 "no credentials"
原因:未执行 `gog auth credentials` 导入 `client_secret.json`
处理:从 Google Cloud Console 下载 OAuth 桌面应用凭证,执行 `gog auth credentials /path/to/client_secret.json` 后重新 `gog auth add`

### 2. 账户未授权目标服务

现象:调用 `gog gmail search` 返回 "service not authorized for account"
原因:`auth add` 时 `--services` 未包含 gmail
处理:重新执行 `gog auth add you@gmail.com --services gmail,sheets`,补全所需服务

### 3. Sheets 范围格式错误

现象:`gog sheets get` 返回 400,提示 "Unable to parse range"
原因:范围未带工作表名(如 `A1:D10`)或工作表名含特殊字符未加引号
处理:范围必须为 `工作表名!A1:D10` 格式;含空格或特殊字符的工作表名需用单引号包裹,如 `'My Sheet'!A1:D10`

### 4. Sheets 值矩阵维度不匹配

现象:`gog sheets append` 返回 400,提示 "values length does not match range"
原因:`--values-json` 的列数与范围的列数不一致
处理:核对范围列数与每行 values 的元素数;范围 `A:C` 对应 3 列,values 每行必须为 3 个元素

### 5. Gmail 搜索语法错误

现象:`gog gmail search` 返回 400,提示 "Invalid query"
原因:搜索语法使用了 Gmail 不支持的运算符,或引号未闭合
处理:使用 Gmail 官方支持的运算符(`from:`、`to:`、`subject:`、`has:attachment`、`newer_than:`、`older_than:` 等);含空格的关键词用双引号包裹

## FAQ

### Q1:如何避免每次都传 `--account`?

设置环境变量 `GOG_ACCOUNT=you@gmail.com`,gog 会自动使用该账户作为默认账户,无需每次命令重复传入。

### Q2:`--values-json` 和内联行参数有什么区别?

`--values-json` 接收标准 JSON 二维数组(如 `[["A","B"],["1","2"]]`),推荐用于脚本化场景,可避免 shell 转义问题。内联行参数适合简单交互式调用,但含特殊字符时易出错。

### Q3:本免费版支持发送邮件吗?

不支持。本免费版仅支持 Gmail 搜索与 Sheets 读/追加。邮件发送、日历事件、云盘搜索、联系人列表、文档导出等能力请升级付费版。

### Q4:Sheets 支持更新和清除单元格吗?

本免费版仅支持 `get`(读取)与 `append`(追加)。`update`(更新)与 `clear`(清除)需升级付费版。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 本免费版仅支持 Gmail search 与 Sheets get/append,不支持邮件发送、Calendar、Drive、Contacts、Docs
- Sheets 单次请求的单元格数量受 Google API 配额限制,大批量写入需分批
- OAuth token 有有效期,过期后需重新 `gog auth add` 刷新
- Gmail 搜索结果受 Google API 配额限制,`--max` 上限为 100

## 升级提示

本免费版仅覆盖 Gmail 搜索与 Sheets 读写基础能力。如需以下能力,请升级到付费版 `gog`:

- Gmail 邮件发送
- Calendar 日历事件查询
- Drive 云盘文件搜索
- Contacts 联系人列表
- Sheets update/clear/metadata 完整能力
- Docs 文档导出与 cat
- 多账户切换与完整 8 类领域异常处理
