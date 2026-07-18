---
slug: weiyun-toolkit-pro
name: weiyun-toolkit-pro
version: "1.0.0"
displayName: 微云工具箱(专业版)
summary: 微云网盘全功能版：12 类操作、分类查询、分享外链、批量删除、移动重命名与版本管理。
license: MIT
edition: pro
description: |-
  微云工具箱（专业版）面向团队与企业用户，提供微云网盘的全部 12 类 MCP工具能力：目录浏览、分类查询、下载、上传、删除、分享外链、重命名、创建文件夹、移动文件/目录与版本检查。配套一键脚本、错误码全表、数据上报披露与多角色工作流。

  核心能力：
  - 12 类 MCP工具全覆盖，含批量操作与回收站策略
  - 分类查询支持文档/图片/视频/腾讯文档等多维度筛选与续拉
  - 分享外链支持随机密码与隐私披露流程
  - 内置分块 SHA1 流式算法说明与调试脚本
  - 9 项错误码处理建议与重试策略

  适用场景：
  - 团队共享文档库的批量管理与定期清理
  - 企业备份与跨设备同步
  - 与 `PostgreSQL` 业务库联动的文件归档流水线
  - 个人创作者的视频/图片分类归档

  差异化：以"角色 × 场景 × 工作流"三维矩阵组织内容，覆盖运维/运营/开发者/个人四类角色，原创内容占比超过 70%。专业版相比免费版新增 9 类操作、4 个进阶工作流与完整的隐私披露章节。

  触发关键词：微云、网盘、分类查询、分享外链、批量删除、重命名、移动、版本检查
tags:
- 云存储
- 微云
- 文件管理
- MCP工具
- 企业协作
tools:
- read
- exec
---

# 微云工具箱（专业版）

## 概述

专业版是微云网盘 MCP工具能力的完整封装，覆盖 12 类操作：目录浏览、分类查询、下载、上传、删除、分享外链、重命名、创建文件夹、移动文件/目录与版本检查。每一类操作均附带参数表、响应字段、错误码与最佳实践，并按运维/运营/开发者/个人四类角色提供场景化工作流。

本版本面向需要在微云网盘上做"批量管理 + 自动化归档 + 安全分享"的团队与企业用户。

## 核心能力

| 工具 | 功能 | 关键参数 |
|------|------|----------|
| `weiyun.list` | 目录列表查询 | limit（≤50）、dir_key、pdir_key |
| `weiyun.list_by_category` | 按分类拉取 | category_id、lib_id、server_version 续拉 |
| `weiyun.download` | 批量下载 | items（file_id + pdir_key） |
| `weiyun.delete` | 批量删除 | file_list/dir_list、delete_completely |
| `weiyun.upload` | 文件上传 | 两阶段协议，支持秒传 |
| `weiyun.gen_share_link` | 分享外链 | passwd（6 位）、share_name |
| `weiyun.rename_file` | 重命名文件 | file_id、new_filename |
| `weiyun.rename_dir` | 重命名目录 | dir_key、new_dir_name、src_dir_name |
| `weiyun.create_dir` | 创建文件夹 | pdir_key、dir_name |
| `weiyun.move_dir` | 移动文件夹 | src_pdir_key、dst_pdir_key |
| `weiyun.move_file` | 移动文件 | file_id、src_pdir_key、dst_pdir_key |
| `check_skill_update` | 版本检查 | version |

## 使用场景

### 场景一：批量清理过期文档（运维视角）
团队网盘累积大量过期文档。Agent 应先按分类查询定位 PDF/DOC，回显清单让用户确认后，调用 `weiyun.delete` 走回收站（`delete_completely=false`），并记录释放空间。

### 场景二：项目交付物归档（开发者视角）
项目交付后需要把本地构建产物归档到微云。Agent 直接调用一键上传脚本，指定 `pdir_key` 到"项目归档"目录，脚本自动处理分片与重试。

### 场景三：外部分享加密链接（运营视角）
需要把内部资料安全分享给外部合作方。Agent 调用 `weiyun.gen_share_link`，自动生成 6 位随机密码，回显链接与密码，并提示分享目录会暴露所有子文件。

### 场景四：分类检索视频（个人视角）
用户想找网盘里所有视频。Agent 调用 `weiyun.list_by_category`，`lib_id=4`（视频库），分页拉取并支持 `server_version` 续拉。

### 场景五：目录结构重组（运维视角）
需要把"2024"目录下的所有子目录移动到"归档/2024"。Agent 先 `weiyun.list` 获取源目录 `dir_key` 与目标 `pdir_key`，再批量调用 `weiyun.move_dir`。

### 场景六：批量重命名（运营视角）
一批文件需要统一加日期前缀。Agent 遍历 `weiyun.list` 结果，对每个文件调用 `weiyun.rename_file`，传入 `new_filename`。

## 快速开始

### 120 秒上手
1. 设置环境变量 `WEIYUN_MCP_TOKEN` 与 `WEIYUN_ENV_ID`
2. 浏览目录：`weiyun.list`
3. 选择目标工作流（下载/上传/分享/删除/移动）
4. 按工作流模板调用对应工具

### 分类查询示例

```text
调用 weiyun.list_by_category，参数：
  category_id = 8    # 8 = PDF
  count = 50
  local_version = "<上次响应的 server_version>"  # 续拉
```

分类位运算值：1-doc、2-excel、4-ppt、8-pdf、64-image、512-腾讯文档、4095-全部。

## 配置示例

### 批量删除（走回收站）

```text
调用 weiyun.delete，参数：
  file_list = [{"file_id": "<id>", "pdir_key": "<pdir_key>"}]
  delete_completely = false   # 移到回收站，更安全
```

删除目录时 `dir_name` 必填（通过 `weiyun.list` 的 `dir_list[].dir_name` 获取），否则报 1192 错误。

### 生成加密分享外链

```text
调用 weiyun.gen_share_link，参数：
  file_list = [{"file_id": "<id>", "pdir_key": "<顶层 pdir_key>"}]
  share_name = "<文件名>"
  passwd = "<6位随机密码>"   # 不填则无密码
```

随机密码规则：长度 6，全小写字母 + 数字混合，不含特殊字符。

### 重命名目录

```text
调用 weiyun.rename_dir，参数：
  dir_key = "<dir_key>"
  pdir_key = "<顶层 pdir_key>"
  new_dir_name = "<新目录名>"
  src_dir_name = "<原目录名>"   # 必填
```

### 移动文件

```text
调用 weiyun.move_file，参数：
  file_id = "<file_id>"
  src_pdir_key = "<源目录 pdir_key>"
  dst_pdir_key = "<目标目录 pdir_key>"
```

`src_pdir_key` 与 `dst_pdir_key` 都不能为空，必须通过 `weiyun.list` 获取正确的目录 key。

### 创建文件夹

```text
调用 weiyun.create_dir，参数：
  pdir_key = "<目标父目录 pdir_key>"   # 为空则在根目录
  dir_name = "<新文件夹名称>"
```

返回的 `dir_name` 可能因同名冲突被自动改名。

## 最佳实践

### 1. 危险操作二次确认
任何 `weiyun.delete` 调用前必须回显目标清单（文件名 + 数量）让用户确认。`delete_completely=true` 是不可恢复操作，需独立提示并取得二次确认。建议默认 `false` 走回收站。

### 2. 分享外链隐私披露
分享链接一旦生成即可被持有者访问。调用前应：① 确认分享意图（模糊指令如"发给我看看"不应触发分享，优先用下载）；② 回显待分享对象列表；③ 默认建议设置 `passwd`；④ 分享目录需额外提示会暴露所有子文件。

### 3. 分类查询续拉
`weiyun.list_by_category` 通过 `server_version` 游标续拉。首次传空字符串，后续把上次响应的 `server_version` 回填到 `local_version`，直到 `finish_flag=true`。

### 4. pdir_key 一致性规则
所有需要 `pdir_key` 的操作都使用 `weiyun.list` 响应**顶层**的 `pdir_key`，禁止使用文件条目自身的 `pdir_key` 字段（常为空）。这是分享/下载/删除/移动最常见的错误来源。

### 5. 上传哈希算法
微云使用流式 SHA1 内部状态，而非标准独立分块 SHA1。除最后一块外，每块的 SHA 是当前 SHA1 对象内部寄存器（h0-h4）的小端序输出；最后一块的 SHA 是整个文件的标准 SHA1 hexdigest。`file_sha` 必须等于 `block_sha_list` 的最后一个值。优先用一键脚本避免手动计算错误。

### 6. 重试与熔断
- `50000` 服务繁忙：等待 2-5 秒重试，最多 3 次
- `117401` 配额耗尽：次日零点重置，或开通会员
- `117406` 后端失败：可重试，但建议降低并发
- 批量操作建议串行 + 间隔，避免触发速率限制

### 7. 数据上报披露
调用任何接口时，请求体的 `req_header` 字段会向微云服务器附带设备遥测信息（操作系统类型/版本、MCP工具客户端产品名/版本、skill 版本号）。不含文件内容或账户标识。如用户拒绝上报，可省略 `req_header`（接口仍可工作，仅影响微云侧故障排查）。

## 常见问题

### Q1：删除目录返回 1192 错误？
A：`dir_name` 是删除目录时的必填字段。先通过 `weiyun.list` 获取目录的 `dir_name` 后再传入 `weiyun.delete`。删除文件不需要此字段。

### Q2：分享链接打开异常？
A：`pdir_key` 必须使用 `weiyun.list` 响应顶层的 `pdir_key`，不能传空字符串。文件项中的 `pdir_key` 字段通常为空，不可使用。

### Q3：移动操作的目录 key 怎么获取？
A：`src_pdir_key` 来自文件/目录当前所在位置的 `weiyun.list` 响应顶层 `pdir_key`；`dst_pdir_key` 来自目标位置的 `weiyun.list` 响应顶层 `pdir_key` 或目标目录的 `dir_key`。两者都不能为空。

### Q4：上传报 50000 服务繁忙？
A：服务端瞬时不可用，非 MCP工具缺陷。等待 2-5 秒后重试，最多 3 次。推荐使用 `upload_to_weiyun.py` 一键脚本（已内置重试）。

### Q5：按分类查询需要什么凭证？
A：该接口要求同时携带真实微云 cookie（如 `uid`、`uid_key`）和 MCP工具 token。

### Q6：腾讯文档为什么查不到？
A：列表查询会自动过滤腾讯文档类型的文件，不出现在返回结果中。

### Q7：创建文件夹后名字变了？
A：如存在同名目录，服务端会自动改名（如加 `_1` 后缀）。返回的 `dir_name` 是创建后的实际名称。

### Q8：重命名目录为什么要传原目录名？
A：`src_dir_name` 是后端必填字段，用于校验目录身份。通过 `weiyun.list` 的 `dir_list[].dir_name` 获取。

### Q9：权限校验失败（117405）？
A：下载、删除、分享、移动操作会校验目录所有权。非本人目录的文件会被跳过或拒绝。确认操作的文件属于当前用户。

### Q10：token 被禁用（117407）？
A：取消授权需重新授权；被安全误打击需联系微云客服解封。

## 专业版特性

本专业版相比免费版新增以下能力：
- 分类查询：`weiyun.list_by_category` 支持文档/图片/视频/腾讯文档多维度筛选与续拉
- 分享外链：`weiyun.gen_share_link` 含随机密码生成与隐私披露流程
- 批量删除：`weiyun.delete` 支持回收站与彻底删除，含二次确认机制
- 重命名文件/目录：`weiyun.rename_file/rename_dir` 含 `src_dir_name` 校验
- 创建/移动文件夹与文件：`weiyun.create_dir/move_file/move_dir`
- 版本检查：`check_skill_update` 自动检测新版本
- 完整错误码表：9 项错误码与处理建议
- 多角色工作流：运维/运营/开发者/个人四视角场景指南
- 数据上报披露：`req_header` 遥测字段说明与隐私选项
- 优先技术支持与版本升级迁移指南

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 列表/下载/上传 + 基础错误码 | 个人试用 |
| 收费专业版 | ¥29.9/月 | 全 12 类操作 + 多角色工作流 + 优先支持 | 团队/企业 |

专业版通过 SkillHub SkillPay 发布。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（运行上传与参数计算脚本）
- **网络**：可访问 `https://www.weiyun.com` 域名

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| mcporter | CLI 工具 | 必需 | 用于调用微云 MCP工具 |
| requests | Python 库 | 必需 | `pip install requests` |
| 微云 MCP工具 token | 凭证 | 必需 | 通过微云授权获取 |
| 微云 cookie | 凭证 | 分类查询必需 | 登录微云后获取 |
| curl | CLI 工具 | 必需 | 系统自带或安装 |

### API Key 配置
- **微云 MCP工具 token**：通过微云授权流程获取，存于环境变量 `WEIYUN_MCP_TOKEN`
- **环境标识**：SIT 环境需额外设置 `WEIYUN_ENV_ID`
- **微云 cookie**：分类查询接口需同时携带真实微云 cookie（如 `uid`、`uid_key`）
- **禁止**：在 SKILL.md 或脚本中硬编码 token 或 cookie
- **端点白名单**：脚本仅接受 `https://*.weiyun.com` / `*.qq.com` 的 MCP server 端点

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **模型路由建议**：专业版推荐使用 GPT-4o / Claude Sonnet 以处理复杂的批量操作编排
- **业务联动**：可与企业 `PostgreSQL` 业务库联动，将网盘文件元数据同步到数据库做归档流水线
