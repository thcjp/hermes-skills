# 详细参考 - weiyun-skills

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

### 工作流 1：查找并下载文件
当需要在微云中找到某个文件并下载到本地时，按以下步骤操作：

**第一步：查询根目录**

```text
调用 weiyun.list，参数：limit=50, get_type=0
```

* 响应中的 `file_list` 包含文件，`dir_list` 包含子目录
* **记住响应顶层的 `pdir_key`**（后续下载需要用到）
* 如果文件在根目录 → 进入第三步
* 如果文件不在根目录 → 需要遍历子目录（第二步）

**第二步：遍历子目录查找文件**

```text
调用 weiyun.list，参数：
  dir_key = <子目录的 dir_key>（从 dir_list 中获取）
  pdir_key = <子目录所在父目录的 pdir_key>（即上一次 list 响应顶层的 pdir_key，或子目录所在目录的 dir_key）
  limit = 50
```

**⚠️ 关键**：查询子目录时 `dir_key` 和 `pdir_key` 的含义：

* `dir_key`：要查询的目标子目录的 key（从 `dir_list` 中的 `dir_key` 字段获取）
* `pdir_key`：该子目录所在的父目录 key（从上一级 `weiyun.list` 响应顶层的 `pdir_key` 获取）

如果还有嵌套子目录，递归重复此步骤。

**第三步：获取下载链接**

```text
调用 weiyun.download，参数：
  items = [{"file_id": "<文件的 file_id>", "pdir_key": "<文件所在目录的 pdir_key>"}]
```

* `file_id`：从 `file_list` 中获取
* `pdir_key`：使用 `weiyun.list` 响应中**顶层的 `pdir_key`**（不是文件自身的 `pdir_key` 字段）

**第四步：下载文件到本地**

```bash
curl -s -L -o <本地文件名> -b "<cookie>" "<https_download_url>"
```

* `-L`：跟随重定向（必须）
* `-b`：携带 cookie（从 download 响应中获取，格式如 `FTN5K=08bfd4be`）
* 下载完成后验证文件大小与 `file_size` 一致



### 算法步骤（分块大小 = 512KB = 524288 字节）
1. 创建**一个**共享的 SHA1 哈希对象
2. 对于除最后一块之外的每个块：
   * 读取 524288 字节并 `update()` 到 SHA1 对象
   * 提取 SHA1 内部寄存器（h0, h1, h2, h3, h4）以**小端序**输出
   * 输出为 40 字符 hex 字符串 → 该块的 `sha` 值
3. 对于最后一块（可能不足 524288 字节）：
   * 继续用相同 SHA1 对象 update 剩余数据
   * `sha` 值为**整个文件的标准 SHA1 hexdigest**（大端序，含 finalization）



## 分块 SHA1 计算算法
这是上传功能最核心的部分。微云**不使用**标准的独立分块 SHA1，而是使用**流式 SHA1 内部状态**。




### 1. weiyun.list — 目录列表查询
查询微云网盘的目录内容，返回子目录和文件列表。

**请求参数**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| get_type | uint32 | 否 | 获取类型：0-所有，1-仅目录，2-仅文件 |
| offset | uint32 | 否 | 分页起始偏移量，从 0 开始 |
| limit | uint32 | **是** | 每页返回数量，最大 50 |
| order_by | uint32 | 否 | 排序字段：0-不排序，1-按名字，2-按修改时间 |
| asc | bool | 否 | true-升序，false-降序（默认） |
| dir_key | string | 否 | 要查询的目录 key（hex 编码），为空则使用 token 绑定的 dirkey |
| pdir_key | string | 否 | 要查询的父目录 key（hex 编码），为空则使用 token 绑定的 pdirkey |
| req_header | ReqHeader | 推荐 | 请求信息头，用于数据上报（含 `qua` 和 `version`） |

**响应**：返回 `pdir_key`（父目录 key）、`dir_list`（目录列表）、`file_list`（文件列表）、`finish_flag`（是否拉取完毕）。

**注意**：腾讯文档文件会被自动过滤，不出现在返回结果中。



---

### 2. weiyun.list_by_category — 按分类拉取文件列表
按文件分类（文档、图片、视频等）分页拉取文件列表，支持通过 `server_version` 续拉。

**请求参数**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| category_id | uint64 | 否 | 分类 ID（位运算值），有值时优先于 lib_id 和 suffix_list。例如：1-doc、2-excel、4-ppt、8-pdf、64-image、512-腾讯文档、4095-全部 |
| lib_id | int32 | 否 | 库 ID：1-文档，2-图片，3-音乐，4-视频，5-其他。`category_id` 有值时会忽略此字段 |
| local_version | string | 否 | 上次返回的 `server_version`，用于增量续拉；首次请求传空字符串 |
| group_id | int32 | 否 | 分组 ID。文档库：0-全部，1-doc，2-xls，3-ppt，4-pdf，50-腾讯文档 Doc，51-腾讯文档 Sheet，52-腾讯文档表单；图片/视频库可传相册分组 ID |
| suffix_list | string[] | 否 | 指定后缀列表，仅文档库和其他库有效，例如 `["docx", "xlsx"]` |
| count | int32 | **是** | 本次拉取数量，最大 100 |
| sort_type | int32 | 否 | 排序类型：0-创建时间，1-修改时间，2-名称，3-拍摄时间，4-大小 |
| is_desc_order | bool | 否 | 是否降序排列：true-降序（默认），false-升序 |

**响应**：返回 `server_version`（服务端游标，续拉时回填到 `local_version`）、`file_list`（文件列表）、`finish_flag`（是否拉取完成）。

**注意**：该接口要求同时携带真实微云 cookie（如 `uid`、`uid_key`）和 `mcp_token`。



---

### 4. weiyun.delete — 批量删除
批量删除微云网盘中的文件或目录。

**请求参数**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file_list | McpDeleteFileItem[] | 否 | 待删除的文件列表（`file_id` + `pdir_key`） |
| dir_list | McpDeleteDirItem[] | 否 | 待删除的目录列表（`dir_key` + `pdir_key` + `dir_name`） |
| delete_completely | bool | 否 | false-移到回收站（默认），true-彻底删除 |

**McpDeleteFileItem 字段**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file_id | string | **是** | 文件唯一标识符 |
| pdir_key | string | **是** | 文件所在目录 key |

**McpDeleteDirItem 字段**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dir_key | string | **是** | 目录 key（hex 编码） |
| pdir_key | string | **是** | 父目录 key（hex 编码） |
| dir_name | string | **是** | 目录名称（**后端必填**，缺失会导致 `1192 参数错误，目录名无效`） |

**注意**：`file_list` 和 `dir_list` 至少要填一个。

**⚠️ 删除是危险操作，AI Agent 必须遵守以下规则**：

1. **任何 `weiyun.delete` 调用都必须先取得用户的明确确认**（哪怕只是删除单个文件），禁止仅凭模糊指令（如"清理一下"、"整理目录"）就直接调用。
2. **`delete_completely=true` 是不可恢复的彻底删除**：在调用前必须用一句独立的提示向用户说明"该操作不可恢复，将绕过回收站"，并取得用户对**该次具体调用**的二次确认。建议默认使用 `delete_completely=false` 走回收站。
3. **批量删除前**必须把目标列表（文件名 / 目录名 + 数量）回显给用户校对，避免因 `file_id` / `dir_key` 解析错误而误删非目标项。
4. **删除目录时还需用户再次确认**（目录可能包含大量子文件）。

**⚠️ 删除目录时 `dir_name` 必填**：

* `dir_name` 可通过 `weiyun.list` 获取目录信息时得到，删除目录时必须传入，否则后端返回 `1192 参数错误`。
* 删除**文件**不受影响，无需 `dir_name`。

**响应**：返回 `freed_space`（释放的空间字节数）和 `freed_index_cnt`（删除的文件/目录总数）。



---

### 5. weiyun.gen_share_link — 生成分享外链
为微云文件或目录生成分享短链接。

**请求参数**：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file_list | McpShareFileItem[] | 否 | 待分享的文件列表（`file_id` + `pdir_key`） |
| dir_list | McpShareDirItem[] | 否 | 待分享的目录列表（`dir_key` + `pdir_key`） |
| share_name | string | 否 | 分享名称，不填则使用第一个文件或目录名 |
| passwd | string | 否 | 分享密码，不填则创建无密码分享，长度一定是 6 个字符。支持随机密码，也支持用户指定密码 |

**注意**：

`file_list` 和 `dir_list` 至少要填一个。

随机分享密码生成规则：长度6，全小写字母+数字混合，不包含特殊字符

分享外链无法使用本 skill 进行下载，需要提示用户打开网页进行下载

**⚠️ 分享外链是隐私扩散操作，AI Agent 必须遵守以下规则**：

1. **调用前向用户确认分享意图**：分享链接一旦生成即可被链接持有者访问（在密码有效期内），可能将原本仅当前账号可见的内容暴露给链接接收方。模糊指令（如"发给我看看"）不应触发分享外链生成 —— 优先使用 `weiyun.download` 取得本地副本。
2. **回显将被分享的对象列表**：在调用前把待分享的文件 / 目录名以及预计的有效期、是否设置密码这些信息向用户复述并取得确认。
3. **默认建议设置 `passwd`**：未设置密码意味着任何拿到短链的人都能访问。除非用户明确表示"不要密码"，否则应使用随机密码并在结果中告知用户密码值。
4. **分享目录尤其要谨慎**：目录分享会同时暴露其下所有子文件 / 子目录。

**⚠️ 关键：pdir_key 不能为空！**

* `pdir_key` 必须使用 `weiyun.list` 响应中**顶层的 `pdir_key`**，而不是文件自身的 `pdir_key` 字段（该字段可能为空字符串）
* 如果传空的 `pdir_key`，可能导致分享链接异常，**强烈建议**调用方显式传入正确的 `pdir_key`
* 错误示例：直接用 `file_list[i].pdir_key`（可能为空）
* 正确示例：使用 `weiyun.list` 响应顶层的 `pdir_key` 字段值

**响应**：返回 `short_url`（分享短链接）和 `share_name`（分享名称）。



---

### 6. weiyun.upload — 文件上传
微云文件上传采用**两阶段协议**：

#### 阶段一：预上传
发送文件元数据和分块 SHA1 列表，检查是否可以秒传，或获取上传通道。

**必填字段**：`filename`、`file_size`、`file_sha`、`block_sha_list`、`check_sha`
**可选字段**：`file_md5`、`check_data`、`pdir_key`

**关键行为**：`file_sha` **必须等于** `block_sha_list` 的最后一个值，否则校验会失败。

**响应判断**：

* `file_exist=true` → 秒传成功，上传完毕
* `file_exist=false` → 使用返回的 `upload_key`、`channel_list`、`ex` 进行分片上传

**⚠️ 重试策略**：

* 预上传或分片上传时，服务端可能返回 `retcode=50000, msg=服务繁忙`（瞬时不可用），这**不是 MCP 工具自身缺陷**。
* **推荐重试方式**：遇到 `50000` 错误时，等待 2~5 秒后重试，最多重试 3 次。
* 一键上传脚本 `upload_to_weiyun.py` 已内置重试逻辑，优先使用脚本上传。
* 手动调用 MCP 上传时，调用方应自行实现重试。

#### 阶段二：分片上传
根据预上传返回的通道列表，逐片上传文件数据。

**必填字段**：`upload_key`、`channel_list`、`channel_id`、`ex`、`file_data`、`filename`

**上传状态**：

* `1` = 继续上传下一分片
* `2` = 上传完成
* `3` = 等待其他通道完成



---

### 使用脚本
#### 一键上传脚本（推荐）
直接上传本地文件到微云，整合了参数计算 + 预上传 + 分片上传的完整流程：

```bash
python3 scripts/upload_to_weiyun.py /path/to/file --token <mcp_token> --env_id <env_id>

python3 scripts/upload_to_weiyun.py /path/to/file --token <mcp_token> --pdir_key <dir_key>

export WEIYUN_MCP_TOKEN=<mcp_token>
export WEIYUN_ENV_ID=<env_id>
python3 scripts/upload_to_weiyun.py /path/to/file
```

脚本参数：

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `file_path` | **是** | 本地文件路径（位置参数） |
| `--token` | **是** | MCP token（或设 `WEIYUN_MCP_TOKEN` 环境变量） |
| `--env_id` | 否 | 环境标识（如 `sit-0cd15bb3`，或设 `WEIYUN_ENV_ID`） |
| `--pdir_key` | 否 | 上传目标目录 key（不填使用 token 绑定目录） |
| `--mcp_url` | 否 | MCP 服务地址（默认 `https://www.weiyun.com/api/v3/mcpserver`） |
| `--max_rounds` | 否 | 最大上传轮数（默认 50） |

上传策略：循环「预上传获取通道 → 上传一片 → 重新预上传」直到完成。每次预上传会自动跳过已成功的分片（offset 随进度递增），支持秒传。

**AI Agent 使用时**：只需要 `execute_command` 运行此脚本即可，无需手动计算 block_sha_list 或调用 MCP。

**⚠️ 能力披露（execute_command 的影响范围）**：该脚本会读取本地文件、读取 `WEIYUN_MCP_TOKEN` / `WEIYUN_MCP_URL` / `WEIYUN_ENV_ID` 等环境变量，并向受信任的微云 MCP 端点发起 HTTPS 网络请求上传文件内容。AI Agent 在调用前应：

1. 向用户确认**待上传文件的具体路径**，禁止用通配符或泛指词（如"我电脑里的文档"）触发上传，避免无意中上传敏感文件；
2. 不要把 `--token` 明文写入会被持久化的脚本或 shell history（推荐用 `WEIYUN_MCP_TOKEN` 环境变量）；
3. `--mcp_url` 与 `WEIYUN_MCP_URL` 仅接受 `https://*.weiyun.com` / `*.qq.com` 的端点，脚本内置白名单校验；如确需指向 mock / 本地调试地址，须显式设置 `WEIYUN_MCP_URL_ALLOW_INSECURE=1` 才能放行。

#### 参数计算脚本
仅计算上传参数（不执行上传），用于调试或手动调用 MCP：

```bash
python3 scripts/gen_block_info_list.py /path/to/file
```

输出包括：`block_sha_list`、`file_sha`、`file_md5`、`check_sha`、`check_data`、`block_size`、`block_count`。

两个脚本均包含纯 Python 的 SHA1 实现，支持提取未经 finalization 的内部状态 — 这是 Python 标准库 `hashlib.sha1` 无法做到的。



---

## 常见问题
1. **上传文件应该怎么做**：直接用 `python3 scripts/upload_to_weiyun.py <文件路径> --pdir_key <目录key>`，无需手动计算参数或调用 MCP
2. **下载时 pdir_key 应该填什么**：使用 `weiyun.list` 响应中**顶层的 `pdir_key`**，而不是文件自身的 `pdir_key` 字段（该字段可能为空字符串）
3. **生成分享链接时 pdir_key 不能为空**：必须先调用 `weiyun.list`，使用响应**顶层的 `pdir_key`**（不是 `file_list[i].pdir_key`，该字段通常为空）。`pdir_key` 为空会导致分享链接打开异常
4. **查询子目录时 pdir_key 怎么填**：填入子目录所在父目录的 key。对于根目录下的子目录，就是根目录 `weiyun.list` 响应顶层的 `pdir_key`
5. **下载时需要携带 cookie**：`weiyun.download` 返回的下载链接需要用 `curl -b "<cookie>"` 携带 cookie 值，同时 `-L` 跟随重定向
6. **上传报 "Cannot upload to a directory that you do not own"**：必须指定 `--pdir_key` 参数。先调用 `weiyun.list` 获取响应中顶层的 `pdir_key`
7. **分片上传通道 len=0**：每轮上传完一片后，返回的通道列表可能全部 len=0，需要重新预上传获取下一批通道。`upload_to_weiyun.py` 已自动处理此问题
8. **SHA1 不匹配**：确保分块 SHA 值使用流式 SHA1 内部状态（小端序），而非独立分块 SHA1
9. **file_sha 被覆盖**：服务端用最后一个 block 的 SHA 覆盖 file_sha — 两者必须相等
10. **Base64 双重编码**：MCP 框架自动将 base64 字符串转为 bytes 传给 `file_data` 字段，服务端会再次进行 Base64 解码
11. **通道 ID 不匹配**：上传分片时 `channel_id` 必须与 `channel_list` 中某个条目匹配
12. **环境标识**：SIT 环境需在 Cookie 中携带 `env_id=sit-xxxxx`
13. **权限校验**：下载、删除、分享操作会校验目录所有权，非本人目录的文件会被跳过
14. **腾讯文档过滤**：列表查询会自动过滤腾讯文档类型的文件
15. **pip install requests**：上传脚本依赖 `requests` 库，如提示缺少请先安装：`pip install requests`
16. **所有需要 pdir_key 的操作**（下载、删除、分享、上传、重命名），都应使用 `weiyun.list` 响应**顶层**的 `pdir_key`，而不是文件/目录条目自身的 `pdir_key` 字段
17. **Windows 编码要求（防止中文乱码）**：Windows 下执行 Python 脚本或 mcporter 命令前**必须**先切换控制台代码页为 UTF-8，格式为 `chcp 65001 >nul && python ...`。Python 脚本已内置 `_encoding_fix.py` 模块自动修复 stdout/stderr 编码，但 `chcp 65001` 仍然是必要的（确保 cmd/PowerShell 控制台本身使用 UTF-8 解码输出）
18. **Windows 下使用 `python` 而非 `python3`**：Windows 系统通常使用 `python` 命令，macOS/Linux 使用 `python3`。请根据用户操作系统自动选择正确的命令
19. **重命名文件/目录**：先调用 `weiyun.list` 获取 `file_id`/`dir_key`、`dir_name` 和顶层 `pdir_key`，再调用 `weiyun.rename_file` 或 `weiyun.rename_dir`（重命名目录时需额外传 `src_dir_name` 即原目录名）
20. **按分类查找文件**：使用 `weiyun.list_by_category`，通过 `category_id` 或 `lib_id` 指定分类，支持 `server_version` 续拉。该接口需要同时携带真实微云 cookie 和 `mcp_token`
21. **生成带密码的分享链接**：在调用 `weiyun.gen_share_link` 时设置 `passwd` 参数即可创建加密分享
22. **创建文件夹**：调用 `weiyun.create_dir`，传入 `pdir_key`（父目录 key）和 `dir_name`（文件夹名称）。`pdir_key` 为空时在 token 绑定的根目录下创建。返回的 `dir_name` 可能因同名冲突被自动改名
23. **移动文件/目录**：使用 `weiyun.move_file` 或 `weiyun.move_dir`。需要先通过 `weiyun.list` 分别获取源目录和目标目录的 `pdir_key`，填入 `src_pdir_key` 和 `dst_pdir_key`。两个 key 都不能为空
24. **移动操作的目录 key 获取**：`src_pdir_key` 来自文件/目录当前所在位置的 `weiyun.list` 响应顶层 `pdir_key`；`dst_pdir_key` 来自目标位置的 `weiyun.list` 响应顶层 `pdir_key` 或目标目录的 `dir_key`
25. **删除目录返回 1192 错误**：`dir_name` 是删除目录时的必填字段，需通过 `weiyun.list` 获取目录的 `dir_name` 后传入 `weiyun.delete`。删除文件不需要此字段
26. **上传时报 50000 服务繁忙**：这是服务端瞬时不可用，非 MCP 工具缺陷。等待 2~5 秒后重试，最多 3 次。推荐使用 `upload_to_weiyun.py` 一键上传脚本（已内置重试逻辑）



---
