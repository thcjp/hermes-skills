---
slug: "gog"
name: "gog"
version: "1.0.0"
displayName: "Gog"
summary: "Google Workspace命令行工具,覆盖Gmail/日历/云盘/联系人/表格/文档六大服务。"
license: "MIT"
description: |-
  Google Workspace 命令行工具技能。通过 `gog` CLI 统一操作 Gmail、Calendar、Drive、
  Contacts、Sheets、Docs 六大服务,支持 OAuth 凭证管理、多账户切换、JSON 结构化输出与
  脚本化批处理。适用于独立开发者效率提升、自动化工作流编排与一人公司办公自动化场景。
  支持 Gmail 搜索发送、日历事件查询、云盘文件检索、联系人列表、表格读写清除、文档导出查看等。
tags:
  - 研发工具
  - Productivity
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
---
# gog

`gog` 是 Google Workspace 的命令行工具,统一封装 Gmail、Calendar、Drive、Contacts、Sheets、Docs 六大服务的 API 调用。所有操作通过 OAuth 凭证鉴权,支持多账户切换、JSON 结构化输出与 `--no-input` 脚本模式。

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
## 核心能力

- OAuth 凭证管理:导入 `client_secret.json`、添加多服务授权账户、列出已授权账户
- Gmail:按 Gmail 搜索语法检索邮件(`newer_than:`、`from:`、`has:attachment` 等)、发送邮件
- Calendar:按时间范围查询日历事件,支持 ISO8601 时间区间
- Drive:按查询语法检索文件,支持 `--max` 限制返回数量
- Contacts:列出联系人,支持分页
- Sheets:读取指定范围、更新单元格、追加行、清除范围、获取表格元数据
- Docs:导出为 txt/docx/markdown、直接 cat 输出文档内容
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`gog`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 一次性配置

```bash
gog auth credentials /path/to/client_secret.json
gog auth add you@gmail.com --services gmail,calendar,drive,contacts,sheets,docs
gog auth list
```

`client_secret.json` 从 Google Cloud Console 的 OAuth 客户端凭证页面下载,类型选择"桌面应用"。`--services` 按需勾选,首次 `auth add` 会触发浏览器授权流程。

## 常用命令

### Gmail

搜索近 7 天邮件:

```bash
gog gmail search 'newer_than:7d' --max 10
```

发送邮件:

```bash
gog gmail send --to a@b.com --subject "Hi" --body "Hello"
```

### Calendar

查询日历事件:

```bash
gog calendar events <calendarId> --from 2026-07-01T00:00:00Z --to 2026-07-31T23:59:59Z
```

### Drive

搜索云盘文件:

```bash
gog drive search "name='季度报告'" --max 10
```

### Contacts

列出联系人:

```bash
gog contacts list --max 20
```

### Sheets

读取范围:

```bash
gog sheets get <sheetId> "Tab!A1:D10" --json
```

更新范围:

```bash
gog sheets update <sheetId> "Tab!A1:B2" --values-json '[["A","B"],["1","2"]]' --input USER_ENTERED
```

追加行:

```bash
gog sheets append <sheetId> "Tab!A:C" --values-json '[["x","y","z"]]' --insert INSERT_ROWS
```

清除范围:

```bash
gog sheets clear <sheetId> "Tab!A2:Z"
```

获取元数据:

```bash
gog sheets metadata <sheetId> --json
```

### Docs

导出文档:

```bash
gog docs export <docId> --format txt --out /tmp/doc.txt
```

直接输出文档内容:

```bash
gog docs cat <docId>
```

## 使用约定

- 设置 `GOG_ACCOUNT=you@gmail.com` 可避免每次重复 `--account` 参数
- 脚本化场景优先使用 `--json` 加 `--no-input`,确保输出可解析且不阻塞
- Sheets 数据优先通过 `--values-json` 传递,避免内联行格式歧义
- Docs 仅支持 export/cat/copy;原位编辑需 Docs API 客户端,不在 gog 范围内
- 发送邮件或创建事件前需人工确认,避免误操作

## 适用场景

### 场景一:独立开发者邮件批处理

输入:近 7 天带附件的邮件列表、`--max 20`、JSON 输出
输出:结构化邮件列表,包含发件人、主题、附件名,可管道给下游脚本分类归档

### 场景二:自动化工作流表格读写

输入:Google Sheet ID、目标范围 `Tab!A:C`、追加数据 `[["x","y","z"]]`
输出:追加后的范围统计(更新行数、列数),可用于流水线断言

### 场景三:一人公司日历事件同步

输入:主日历 ID、ISO8601 时间区间 `--from` `--to`
输出:该区间内所有事件列表,含标题、开始时间、结束时间、参会人

### 场景四:文档批量导出归档

输入:多个 Doc ID、导出格式 `txt`、输出路径 `/tmp/`
输出:本地文本文件,可纳入版本控制或全文检索索引

## 案例展示

### 案例一:近 7 天邮件归档流水线

需求:每天凌晨归档近 7 天带附件的邮件到本地 JSON 文件。

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

下游脚本读取 JSON 分类归档,`--no-input` 确保不阻塞流水线。

### 案例二:Google Sheet 追加日志行

需求:CI 流水线每次构建完成后,向监控 Sheet 的 `Builds!A:C` 追加一行构建记录。

实现:

```bash
gog sheets append <sheetId> "Builds!A:C" \
  --values-json '[["2026-07-20","#1234","success"]]' \
  --insert INSERT_ROWS \
  --no-input
```

输出:`UpdatedRange: Builds!A5:C5, UpdatedRows: 1`,可用于断言追加成功。

### 案例三:日历事件导出为待办清单

需求:导出本周主日历事件,生成 Markdown 待办清单。

实现:

```bash
gog calendar events primary \
  --from 2026-07-20T00:00:00Z \
  --to 2026-07-26T23:59:59Z \
  --json --no-input \
  | python3 -c "
import json,sys
events = json.load(sys.stdin)
for e in events:
    print(f'- [ ] {e[\"summary\"]} @ {e[\"start\"]}')
"
```

输出本周所有会议标题与开始时间,管道给 Python 生成 Markdown 清单。

## 异常处理

### 1. OAuth 凭证未导入

现象:`gog auth list` 为空,或调用任何命令返回 "no credentials"
原因:未执行 `gog auth credentials` 导入 `client_secret.json`
处理:从 Google Cloud Console 下载 OAuth 桌面应用凭证,执行 `gog auth credentials /path/to/client_secret.json` 后重新 `gog auth add`

### 2. 账户未授权目标服务

现象:调用 `gog gmail search` 返回 "service not authorized for account"
原因:`auth add` 时 `--services` 未包含 gmail
处理:重新执行 `gog auth add you@gmail.com --services gmail,calendar,drive,contacts,sheets,docs`,补全所需服务

### 3. Sheets 范围格式错误

现象:`gog sheets get` 返回 400,提示 "Unable to parse range"
原因:范围未带工作表名(如 `A1:D10`)或工作表名含特殊字符未加引号
处理:范围必须为 `工作表名!A1:D10` 格式;含空格或特殊字符的工作表名需用单引号包裹,如 `'My Sheet'!A1:D10`

### 4. Sheets 值矩阵维度不匹配

现象:`gog sheets update` 返回 400,提示 "values length does not match range"
原因:`--values-json` 的列数与范围的列数不一致
处理:核对范围列数与每行 values 的元素数;范围 `A1:B2` 对应 2 行 2 列,values 必须为 `[["A","B"],["1","2"]]`

### 5. Gmail 搜索语法错误

现象:`gog gmail search` 返回 400,提示 "Invalid query"
原因:搜索语法使用了 Gmail 不支持的运算符,或引号未闭合
处理:使用 Gmail 官方支持的运算符(`from:`、`to:`、`subject:`、`has:attachment`、`newer_than:`、`older_than:` 等);含空格的关键词用双引号包裹,如 `subject:"周报 评审"`

### 6. Calendar 时间格式不合法

现象:`gog calendar events` 返回 400,提示 "Invalid time"
原因:`--from` 或 `--to` 未使用 ISO8601 格式,或缺少时区标识
处理:时间必须为 ISO8601 带时区,如 `2026-07-20T00:00:00Z` 或 `2026-07-20T00:00:00+08:00`;不要用 `2026-07-20` 这种纯日期

### 7. Drive 查询语法错误

现象:`gog drive search` 返回 400,提示 "Invalid query"
原因:使用了 Drive API 不支持的查询运算符,或运算符拼写错误
处理:使用 Drive 官方查询语法,如 `name='报告'`、`mimeType='application/pdf'`、`modifiedTime > '2026-07-01T00:00:00'`;等号后值用单引号包裹

### 8. Docs 原位编辑不被支持

现象:尝试用 `gog docs` 修改文档内容但找不到对应子命令
原因:gog 的 docs 模块仅支持 export/cat/copy,不支持原位编辑
处理:原位编辑需使用 Google Docs API 客户端直接调用 `documents:batchUpdate`;gog 流程下可先 `export` 为 txt,本地编辑后重新上传为新文档

## FAQ

### Q1:如何避免每次都传 `--account`?

设置环境变量 `GOG_ACCOUNT=you@gmail.com`,gog 会自动使用该账户作为默认账户,无需每次命令重复传入。

### Q2:`--values-json` 和内联行参数有什么区别?

`--values-json` 接收标准 JSON 二维数组(如 `[["A","B"],["1","2"]]`),推荐用于脚本化场景,可避免 shell 转义问题。内联行参数适合简单交互式调用,但含特殊字符时易出错。

### Q3:Docs 能否直接修改文档内容?

不能。gog 的 docs 模块仅支持 export(导出)、cat(输出内容)、copy(复制文档)。原位编辑需要 Google Docs API 的 `documents:batchUpdate` 接口,不在 gog 范围内。常见替代流程是 export 为 txt 本地编辑后重新上传。

### Q4:多账户如何切换?

通过 `--account` 参数指定,或设置 `GOG_ACCOUNT` 环境变量切换默认账户。`gog auth list` 可查看所有已授权账户。不同账户的 OAuth token 相互隔离。

### Q5:Gmail 发送邮件是否需要确认?

是的。发送邮件是不可逆操作,gog 默认在发送前会要求确认。脚本化场景可加 `--no-input`,但需自行承担误发风险。建议先 `gog gmail send --dry-run` 预览内容。

### Q6:Sheets 的 `--input USER_ENTERED` 与 `RAW` 有何区别?

`USER_ENTERED` 表示值按用户在 UI 中输入的方式解析(如 `=SUM(A1:A10)` 会被识别为公式),`RAW` 表示值作为字面量原样写入(公式不会被计算)。默认为 `USER_ENTERED`,写入纯数据时建议显式指定以避免歧义。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- Docs 不支持原位编辑,仅支持 export/cat/copy
- Calendar 仅支持事件查询,不支持事件创建与修改(需人工确认或调用 Calendar API)
- Sheets 单次请求的单元格数量受 Google API 配额限制,大批量写入需分批
- Gmail 发送邮件的附件大小上限 25MB,超过需使用 Drive 链接
- OAuth token 有有效期,过期后需重新 `gog auth add` 刷新
- `gog` 不封装 Google Workspace 的权限管理与组织管理能力,仅处理个人账户维度操作
