---
slug: weiyun-toolkit
name: weiyun-toolkit
version: "1.0.0"
displayName: 微云工具箱(专业版)
summary: 微云网盘全功能版：12 类操作、分类查询、分享外链、批量删除、移动重命名与版本管理。
license: Proprietary
edition: pro
description: |-
  微云工具箱（专业版）面向团队与企业用户，提供微云网盘的全部 12 类 MCP工具能力：目录浏览、分类查询、下载、上传、删除、分享外链、重命名、创建文件夹、移动文件/目录与版本检查。配套一键脚本、错误码全表、数据上报披露与多角色工作流。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
- 云存储
- 微云
- 文件管理
- MCP工具
- 企业协作
tools:
  - - read
- exec
---
# 微云工具箱(专业版)

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

## 适用场景

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

## 使用流程

### 120 秒上手
1. 设置环境变量 `WEIYUN_MCP_TOKEN` 与 `WEIYUN_ENV_ID`
2. 浏览目录：`weiyun.list`
3. 选择目标工作流（下载/上传/分享/删除/移动）
4. 按工作流模板调用对应工具

### 示例

```text
调用 weiyun.list_by_category，参数：
  category_id = 8    # 8 = PDF
  count = 50
  local_version = "<上次响应的 server_version>"  # 续拉
```

分类位运算值：1-doc、2-excel、4-ppt、8-pdf、64-image、512-腾讯文档、4095-全部。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（运行上传与参数计算脚本）
- **网络**：可访问 `https://www.weiyun.com` 域名

### 依赖说明
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
- **端点白名单**：脚本仅接受 `https://*.weiyun.com` / `*.qq.com` 的 协议 server 端点

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **模型路由建议**：专业版推荐使用 GPT-4o / Claude Sonnet 以处理复杂的批量操作编排
- **业务联动**：可与企业 `关系型数据库` 业务库联动，将网盘文件元数据同步到数据库做归档流水线

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

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
