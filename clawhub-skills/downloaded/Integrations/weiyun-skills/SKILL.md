---
slug: weiyun-skills
name: weiyun-skills
version: "1.0.10"
displayName: Weiyun Skills
summary: 微云网盘MCP接口完整技能。
license: MIT
description: |-
  微云网盘MCP接口完整技能。

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 微云网盘, weiyun, 接口完整技能, skills
tags:
- Integrations
tools:
  - - read
- exec
# Weiyun Skills
---
首次安装使用时，需要先完成本地安装和注册，详见 `references/auth.md`。

> **Windows 用户**：所有 `bash ./setup.sh` 命令请替换为 `powershell -ExecutionPolicy Bypass -File setup.ps1`，详见 `references/auth.md`。

## 版本更新检查（每天首次使用前必须执行）
每天使用本 SKILL 前进行一次更新检查，按照如下步骤执行：

### 1. 查看当前版本 version
读取本文件顶部 frontmatter 中的 `version` 字段；格式为 `MAJOR.MINOR.PATCH`。

### 2. 查看最新版本 latest
通过命令获取最新版本信息 `latest`，输入参数 `version` 为上一步获取的当前版本：

```bash
mcporter call "https://www.weiyun.com/api/v3/mcpserver" "check_skill_update" --args '{"version": "当前版本"}'
```

JSON 格式数据返回，返回参数示例：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `latest` | string | 最新版本号，格式为 MAJOR.MINOR.PATCH |
| `release_note` | string | 最新版本发布说明 |
| `instruction` | string | 更新指令 |

### 3. 更新版本
如果当前版本 `version` 低于最新版本 `latest`，则遵循 `instruction` 指令进行更新，或提示用户更新。

## 功能概述
提供微云（Weiyun）网盘通过 MCP 协议进行文件管理的完整能力，包含 **12 个 MCP Tool**：

| Tool 名称 | 功能 | 说明 |
| --- | --- | --- |
| `weiyun.list` | 目录列表查询 | 按目录查看文件和子目录，支持分页和排序 |
| `weiyun.list_by_category` | 按分类拉取文件列表 | 按文档、图片、视频等分类分页拉取文件，支持续拉 |
| `weiyun.download` | 批量下载 | 批量获取文件的 HTTPS 下载链接 |
| `weiyun.delete` | 批量删除 | 批量删除文件或目录，支持回收站或彻底删除 |
| `weiyun.upload` | 文件上传 | 两阶段协议：预上传 + 分片上传，支持秒传 |
| `weiyun.gen_share_link` | 生成分享外链 | 为文件或目录生成分享短链接，支持设置分享密码 |
| `weiyun.rename_file` | 重命名文件 | 重命名微云网盘中的文件 |
| `weiyun.rename_dir` | 重命名目录 | 重命名微云网盘中的目录 |
| `weiyun.create_dir` | 创建文件夹 | 在微云网盘中创建文件夹 |
| `weiyun.move_dir` | 移动文件夹 | 移动微云网盘中的文件夹到目标目录 |
| `weiyun.move_file` | 移动文件 | 移动微云网盘中的文件到目标目录 |
| `check_skill_update` | 技能版本检查更新 | 检查当前 Skill 版本是否为最新，获取更新指令 |

**核心架构原则**：文件哈希计算和 `block_sha_list` 生成**必须在客户端/本地完成**。服务端只接收预计算好的哈希值，不会接收原始文件数据来计算哈希。这种设计是为了防止海量请求打爆服务器的存储和 CPU。

## 触发场景
* 使用微云 MCP 工具进行文件管理（查询、下载、删除、上传、分享、重命名、创建文件夹、移动文件/目录）
* **上传文件到微云**：优先使用 `scripts/upload_to_weiyun.py` 一键完成，无需手动计算参数或调用 MCP
* 按分类（文档、图片、视频等）查找微云文件（`weiyun.list_by_category` Tool）
* 重命名微云文件或目录（`weiyun.rename_file`、`weiyun.rename_dir` Tool）
* 在微云中创建文件夹（`weiyun.create_dir` Tool）
* 移动微云文件或目录到其他位置（`weiyun.move_file`、`weiyun.move_dir` Tool）
* 实现或调试微云 MCP 文件上传（`weiyun.upload` Tool）
* 计算 `block_sha_list`、`check_sha`、`check_data` 等上传参数
* 理解微云两阶段上传协议（预上传 → 分片上传）
* 检查技能版本更新（`check_skill_update`）
* 调试 FTN 上传错误或 SHA1 校验不匹配问题

## 接口一览
**注意** : 所有接口请求时都**务必**要在 `req_header` 字段中携带上报数据，详见下方「数据上报」章节

### 1. weiyun.list — 目录列表查询
> 详细内容已移至 `references/detail.md`

### 2. weiyun.list_by_category — 按分类拉取文件列表
> 详细内容已移至 `references/detail.md`

### 3. weiyun.download — 批量下载
批量获取微云文件的 HTTPS 下载链接。

**注意事项**：

本功能无法下载微云分享的链接里面的文件，只能下载用户微云网盘中的文件。

**请求参数**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | McpDownloadFileItem[] | **是** | 需要下载的文件列表 |

每个 `McpDownloadFileItem` 包含 `file_id`（文件 ID）和 `pdir_key`（所在目录 key），均为必填。

**响应**：每个文件返回 `file_id`、`https_download_url`（下载链接）、`file_size`（文件大小）、`cookie`（下载时需携带的 cookie）。

**权限校验**：只能下载当前用户拥有的文件（通过 `pdir_key` 判断目录所有权）。

### 4. weiyun.delete — 批量删除
> 详细内容已移至 `references/detail.md`

### 5. weiyun.gen_share_link — 生成分享外链
> 详细内容已移至 `references/detail.md`

### 6. weiyun.upload — 文件上传
> 详细内容已移至 `references/detail.md`

### 7. weiyun.rename_file — 重命名文件
重命名微云网盘中的文件，需要提供文件所在目录 key 和文件 ID。

**请求参数**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file_id | string | **是** | 文件唯一标识符 |
| pdir_key | string | **是** | 文件所在目录 key（hex 编码） |
| new_filename | string | **是** | 修改后的文件名 |

**响应**：返回 `error`（错误信息，成功时为空）。

### 8. weiyun.rename_dir — 重命名目录
重命名微云网盘中的目录，需要提供目录 key、父目录 key 和修改前的目录名。

**请求参数**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dir_key | string | **是** | 目录 key（hex 编码） |
| pdir_key | string | **是** | 父目录 key（hex 编码） |
| new_dir_name | string | **是** | 修改后的目录名 |
| src_dir_name | string | **是** | 修改前的目录名 |

**响应**：返回 `error`（错误信息，成功时为空）。

### 9. weiyun.create_dir — 创建文件夹
在微云网盘中创建文件夹，需要提供父目录 key 和文件夹名称。

**请求参数**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pdir_key | string | 否 | 父目录 key（hex 编码），在此目录下创建新文件夹。为空则使用 token 绑定的目录 |
| dir_name | string | **是** | 新文件夹名称 |

**响应**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| dir_key | string | 新创建的目录 key（hex 编码） |
| dir_name | string | 创建后的目录名（可能被自动改名，如存在同名目录） |
| error | string | 错误信息，成功时为空 |

### 10. weiyun.move_dir — 移动文件夹
移动微云网盘中的文件夹到目标目录，需要提供源目录 key 和目标目录 key。

**请求参数**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dir_key | string | **是** | 待移动的目录 key（hex 编码） |
| src_pdir_key | string | **是** | 源父目录 key（hex 编码），即当前所在的目录 |
| dst_pdir_key | string | **是** | 目标父目录 key（hex 编码），即要移动到的目录 |
| dir_name | string | 否 | 目录名称，移动时可选填用于冲突处理 |

**响应**：返回 `error`（错误信息，成功时为空）。

**⚠️ 关键**：`src_pdir_key` 和 `dst_pdir_key` 都需要使用 `weiyun.list` 响应中**顶层的 `pdir_key`** 或对应目录的 `dir_key`，不能传空字符串。

### 11. weiyun.move_file — 移动文件
移动微云网盘中的文件到目标目录，需要提供文件 ID、源目录 key 和目标目录 key。

**请求参数**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file_id | string | **是** | 待移动的文件唯一标识符 |
| src_pdir_key | string | **是** | 源父目录 key（hex 编码），即文件当前所在的目录 |
| dst_pdir_key | string | **是** | 目标父目录 key（hex 编码），即要移动到的目录 |
| filename | string | 否 | 文件名称，移动时可选填用于冲突处理 |

**响应**：返回 `error`（错误信息，成功时为空）。

**⚠️ 关键**：`src_pdir_key` 和 `dst_pdir_key` 都需要使用 `weiyun.list` 响应中**顶层的 `pdir_key`** 或对应目录的 `dir_key`，不能传空字符串。

### 12. check_skill_update — 技能版本检查更新
检查当前 Skill 版本是否为最新，如有新版本则返回更新指令。

**请求参数**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | string | **是** | 当前 Skill 版本号，格式 MAJOR.MINOR.PATCH |

**响应**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| latest | string | 最新版本号，格式 MAJOR.MINOR.PATCH |
| release_note | string | 最新版本发布说明 |
| instruction | string | 更新指令（需要更新时遵循此指令执行） |

**注意**：每天首次使用本 Skill 前必须执行一次版本检查（详见文档顶部「版本更新检查」章节）。

### check_sha 和 check_data 计算
用于服务端防篡改验证：

```text
lastBlockSize = file_size % 524288（若为 0 则取 524288）
checkBlockSize = lastBlockSize % 128（若为 0 则取 128）

check_sha：处理完所有非最后块后，继续 update 最后块中前 (lastBlockSize - checkBlockSize) 字节，
           然后取 SHA1 内部寄存器 h0-h4 小端序输出为 hex
check_data：文件末尾 checkBlockSize 字节的 Base64 编码
```

### 使用脚本
> 详细内容已移至 `references/detail.md`

## 错误处理
MCP 接口在出现异常时会返回以下错误码，调用方可根据错误码进行相应处理：

| 错误码 | 名称 | 说明 |
| --- | --- | --- |
| 1192 | 参数错误，目录名无效 | 删除目录时缺少 `dir_name` 字段，需通过 `weiyun.list` 获取后传入 |
| 50000 | 服务繁忙 | 服务端瞬时不可用，等待 2~5 秒后重试，最多重试 3 次 |
| 117401 | ERR_RATE_LIMIT | 每日调用配额已耗尽，请明天再试 |
| 117402 | ERR_MCP_TOKEN_INVALID | MCP token 无效或已过期，请重新生成 token |
| 117403 | ERR_MCP_PARAM_EMPTY | 请求必填参数为空（如删除接口 file_list 和 dir_list 都为空） |
| 117404 | ERR_MCP_PARAM_INVALID | 请求参数不合法（如 file_id 或 pdir_key 格式错误） |
| 117405 | ERR_MCP_PERMISSION_DENIED | 无权操作非本人目录的文件 |
| 117406 | ERR_MCP_BACKEND_FAIL | 后端服务调用失败，请稍后重试 |
| 117407 | ERR_MCP_TOKEN_DISABLED | MCP token 已被禁用（取消授权/手动拉黑/安全打击） |

**处理建议**：

* **1192**：删除目录时 `dir_name` 缺失导致，请先通过 `weiyun.list` 获取目录名再传入 `weiyun.delete`
* **50000**：服务端临时异常，等待 2~5 秒后重试，最多 3 次。上传场景建议优先使用 `upload_to_weiyun.py`（已内置重试）
* **117401**：等待次日零点配额自动重置，或开通微云会员提升配额
* **117402**：重新生成 token
* **117403/117404**：检查请求参数是否完整且格式正确
* **117405**：确认操作的文件/目录属于当前用户
* **117406**：属于服务端临时异常，可重试
* **117407**：错误是取消授权则需要重新授权，被安全误打击则需要联系微云客服人员做解封处理

## 常见操作工作流
### 工作流 2：上传文件到微云
**推荐方式**（一键脚本）：

```bash

python3 scripts/upload_to_weiyun.py /path/to/file --pdir_key <pdir_key>
```

**手动方式**：参见上方「5. weiyun.upload — 文件上传」章节。

### 工作流 3：生成分享链接
```text
调用 weiyun.list → 找到目标文件的 file_id，记住响应**顶层** pdir_key

调用 weiyun.gen_share_link，参数：
  file_list = [{"file_id": "<file_id>", "pdir_key": "<响应顶层的 pdir_key>"}]
  share_name = "<文件名>"
```

**⚠️ 关键**：`pdir_key` 必须使用 `weiyun.list` 响应中**顶层的 `pdir_key`**，绝对不能传空字符串！文件项中的 `pdir_key` 字段可能为空，不可使用。

### 工作流 4：删除文件或目录
```text
调用 weiyun.list → 找到目标文件的 file_id 或目录的 dir_key 和 dir_name，记住响应顶层 pdir_key

调用 weiyun.delete，参数：
  file_list = [{"file_id": "<file_id>", "pdir_key": "<pdir_key>"}]
  delete_completely = false  （移到回收站，更安全）

调用 weiyun.delete，参数：
  dir_list = [{"dir_key": "<dir_key>", "pdir_key": "<pdir_key>", "dir_name": "<目录名>"}]
  delete_completely = false
```

**注意**：删除目录时 `dir_name` 必填，可通过 `weiyun.list` 返回的 `dir_list[].dir_name` 获取。

### 工作流 5：重命名文件或目录
```text
调用 weiyun.list → 找到目标文件的 file_id 或目录的 dir_key，记住响应顶层 pdir_key

调用 weiyun.rename_file，参数：
  file_id = "<file_id>"
  pdir_key = "<响应顶层的 pdir_key>"
  new_filename = "<新文件名>"

调用 weiyun.rename_dir，参数：
  dir_key = "<dir_key>"
  pdir_key = "<响应顶层的 pdir_key>"
  new_dir_name = "<新目录名>"
  src_dir_name = "<原目录名>"
```

### 工作流 6：按分类查找文件
```text
调用 weiyun.list_by_category，参数：
  category_id = 8    （8 = PDF）
  count = 50

调用 weiyun.list_by_category，参数：
  category_id = 8
  count = 50
  local_version = "<上次响应的 server_version>"

调用 weiyun.list_by_category，参数：
  lib_id = 1         （1 = 文档库）
  suffix_list = ["docx", "xlsx"]
  count = 50
```

### 工作流 7：创建文件夹
```text
调用 weiyun.list → 记住响应顶层 pdir_key 或目标子目录的 dir_key

调用 weiyun.create_dir，参数：
  pdir_key = "<目标父目录的 pdir_key>"（为空则在 token 绑定的根目录下创建）
  dir_name = "<新文件夹名称>"
```

**响应**：返回新创建目录的 `dir_key` 和 `dir_name`（可能因同名被自动改名）。

### 工作流 8：移动文件或目录
```text
调用 weiyun.list，查询源目录 → 找到目标文件的 file_id 或目录的 dir_key，记住响应顶层 pdir_key 作为 src_pdir_key

调用 weiyun.list，查询目标目录 → 记住响应顶层的 pdir_key 作为 dst_pdir_key

调用 weiyun.move_file，参数：
  file_id = "<file_id>"
  src_pdir_key = "<源目录的 pdir_key>"
  dst_pdir_key = "<目标目录的 pdir_key>"

调用 weiyun.move_dir，参数：
  dir_key = "<要移动的目录 dir_key>"
  src_pdir_key = "<源父目录的 pdir_key>"
  dst_pdir_key = "<目标父目录的 pdir_key>"
```

**⚠️ 关键**：`src_pdir_key` 和 `dst_pdir_key` 不能为空，必须通过 `weiyun.list` 获取正确的目录 key。

## 认证机制
所有 MCP 工具需要通过 `WyHeader` HTTP 头传递 `mcp_token`：

```text
WyHeader: mcp_token=<token>
```

## 数据上报
**ℹ️ 用户隐私披露**：调用本 skill 的任何 MCP 接口时，请求体的 `req_header` 字段会向微云服务器附带以下遥测信息，便于官方做问题定位：

* 操作系统类型与版本号（如 `MAC_15.4.1`、`WINDOWS_10.0.19045`）；
* MCP 客户端产品名称与版本号（如 `CODEBUDDY_4.8.1`）；
* 当前 skill 版本号（如 `1.0.8`）。

这些字段不包含文件内容、文件名或账户标识，但仍属于设备级遥测。AI Agent 在首次为用户调用本 skill 前，建议**告知用户上述上报内容**；如用户明确拒绝上报，可在调用 MCP 接口时**省略 `req_header` 字段**（接口仍可正常工作，仅会影响微云侧的故障排查能力）。

为了方便微云官方进行问题故障定位，MCP 客户端在调用每个接口时，**应在请求体的 `req_header` 字段中携带上报数据**。

### ReqHeader 字段说明
| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `qua` | string | 推荐 | 用户设备信息，格式：`{平台}_{平台版本}_{渠道}_{渠道方版本}`，如 `MAC_15.4.1_CODEBUDDY_4.8.1` |
| `version` | string | 推荐 | skill 的版本号，如 `1.0.4`，取自本文件顶部 frontmatter 的 `version` 字段 |

### qua 规则（客户端实时采集）
QUA 是一个字符串，由设备信息拼接而成：

```text
{平台}_{平台版本}_{渠道}_{渠道方版本}
```

* **平台**：检测当前操作系统类型（`MAC` / `WINDOWS` / `LINUX`）
* **平台版本**：获取操作系统版本号（如 macOS `15.4.1`，Windows `10.0.19045`）
* **渠道**：MCP 客户端的产品名称（如 `CODEBUDDY`、`WORKBUDDY`）
* **渠道方版本**：MCP 客户端（IDE 插件）的版本号

| 平台 | QUA 示例 |
| --- | --- |
| macOS | `MAC_15.4.1_CODEBUDDY_4.8.1` |
| Windows | `WINDOWS_10.0.19045_WORKBUDDY_4.8.1` |
| Linux | `LINUX_6.1.0_CODEBUDDY_4.8.1` |

### 示例
```json
{
  "limit": 50,
  "req_header": {
    "qua": "MAC_15.4.1_CODEBUDDY_4.8.1",
    "version": "1.0.9"
  }
}
```

## 常见问题
> 详细内容已移至 `references/detail.md`

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

## 适用场景
* 使用微云 MCP 工具进行文件管理（查询、下载、删除、上传、分享、重命名、创建文件夹、移动文件/目录）
* **上传文件到微云**：优先使用 `scripts/upload_to_weiyun.py` 一键完成，无需手动计算参数或调用 MCP
* 按分类（文档、图片、视频等）查找微云文件（`weiyun.list_by_category` Tool）
* 重命名微云文件或目录（`weiyun.rename_file`、`weiyun.rename_dir` Tool）
* 在微云中创建文件夹（`weiyun.create_dir` Tool）
* 移动微云文件或目录到其他位置（`weiyun.move_file`、`weiyun.move_dir` Tool）
* 实现或调试微云 MCP 文件上传（`weiyun.upload` Tool）
* 计算 `block_sha_list`、`check_sha`、`check_data` 等上传参数
* 理解微云两阶段上传协议（预上传 → 分片上传）
* 检查技能版本更新（`check_skill_update`）
* 调试 FTN 上传错误或 SHA1 校验不匹配问题

## 使用流程
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 已知限制
- 需要API Key，无Key环境无法使用
