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


tags:
- Integrations
tools:
  - - read
- exec
# Weiyun Skills
---
# Weiyun Skills

## 核心能力

- （根据实际场景填充） - 生成生成内容
- （根据实际场景填充） - 遵循专业风格规范
- （根据实际场景填充） - 支持多种变体等多种变体
- （根据实际场景填充） - 自动适配多种场景

## 适用场景

* 使用微云 协议 工具进行文件管理（查询、下载、删除、上传、分享、重命名、创建文件夹、移动文件/目录）
* **上传文件到微云**：优先使用 `scripts/upload_to_weiyun.py` 一键完成，无需手动计算参数或调用 协议
* 按分类（文档、图片、视频等）查找微云文件（`weiyun.list_by_category` Tool）
* 重命名微云文件或目录（`weiyun.rename_file`、`weiyun.rename_dir` Tool）
* 在微云中创建文件夹（`weiyun.create_dir` Tool）
* 移动微云文件或目录到其他位置（`weiyun.move_file`、`weiyun.move_dir` Tool）
* 实现或调试微云 协议 文件上传（`weiyun.upload` Tool）
* 计算 `block_sha_list`、`check_sha`、`check_data` 等上传参数
* 理解微云两阶段上传协议（预上传 → 分片上传）
* 检查技能版本更新（`check_skill_update`）
* 调试 FTN 上传错误或 SHA1 校验不匹配问题

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

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

协议 接口在出现异常时会返回以下错误码，调用方可根据错误码进行相应处理：

| 错误码 | 名称 | 说明 |
| --- | --- | --- |
| 1192 | 参数错误，目录名无效 | 删除目录时缺少 `dir_name` 字段，需通过 `weiyun.list` 获取后传入 |
| 50000 | 服务繁忙 | 服务端瞬时不可用，等待 2~5 秒后重试，最多重试 3 次 |
| 117401 | ERR_RATE_LIMIT | 每日调用配额已耗尽，请明天再试 |
| 117402 | ERR_MCP_TOKEN_INVALID | 协议 token 无效或已过期，请重新生成 token |
| 117403 | ERR_MCP_PARAM_EMPTY | 请求必填参数为空（如删除接口 file_list 和 dir_list 都为空） |
| 117404 | ERR_MCP_PARAM_INVALID | 请求参数不合法（如 file_id 或 pdir_key 格式错误） |
| 117405 | ERR_MCP_PERMISSION_DENIED | 无权操作非本人目录的文件 |
| 117406 | ERR_MCP_BACKEND_FAIL | 后端服务调用失败，请稍后重试 |
| 117407 | ERR_MCP_TOKEN_DISABLED | 协议 token 已被禁用（取消授权/手动拉黑/安全打击） |

**处理建议**：

* **1192**：删除目录时 `dir_name` 缺失导致，请先通过 `weiyun.list` 获取目录名再传入 `weiyun.delete`
* **50000**：服务端临时异常，等待 2~5 秒后重试，最多 3 次。上传场景建议优先使用 `upload_to_weiyun.py`（已内置重试）
* **117401**：等待次日零点配额自动重置，或开通微云会员提升配额
* **117402**：重新生成 token
* **117403/117404**：检查请求参数是否完整且格式正确
* **117405**：确认操作的文件/目录属于当前用户
* **117406**：属于服务端临时异常，可重试
* **117407**：错误是取消授权则需要重新授权，被安全误打击则需要联系微云客服人员做解封处理

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
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

> 详细内容已移至 `references/detail.md`

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
