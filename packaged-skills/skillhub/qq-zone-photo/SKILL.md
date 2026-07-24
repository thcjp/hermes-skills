---
slug: "qq-zone-photo"
name: "qq-zone-photo"
version: 1.0.4
displayName: "社交空间相册"
summary: "管理社交空间相册，支持扫码登录、浏览照片、上传下载"
license: "Proprietary"
description: |-
  社交空间相册自动化管理工具。支持扫码登录、相册浏览、照片上传/下载、
  相册创建等功能。通过Cookie认证访问社交空间非官方API，适用于相册备份、
  照片迁移和批量管理等场景.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# 社交空间相册

社交空间相册的自动化管理工具，支持扫码登录、相册浏览、照片上传/下载、相册创建等功能。通过 `qzone_photos.py` 脚本调用社交空间非官方API实现自动化操作.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 社交空间相册处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 安全与隐私

- Cookie文件包含社交空间完整访问权限，请勿泄露或分享
- 凭证仅存储在本地，不会上传到任何服务器
- 会话Cookie有时效性，过期后需重新登录
- 本工具使用社交空间非官方API，平台更新接口后可能需要适配

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

### 1. 扫码登录

通过 `python3 （请参考skill目录中的脚本文件） --action login --cookies cookies.json` 执行扫码登录。生成二维码供用户扫描，登录成功后自动将Cookie保存到指定的cookies文件中。Cookie包含 `qq_number`、`p_skey`、`skey` 和 `uin` 字段。适用于首次使用或Cookie过期后的重新认证.
### 2. 列出相册

通过 `python3 （请参考skill目录中的脚本文件） --action list --cookies cookies.json` 列出当前账号的所有相册。返回相册列表，包含相册ID（`album-id`）、相册标题、照片数量等信息。可选参数 `--qq` 指定目标账号。适用于浏览相册结构和获取相册ID。- 验证返回数据的完整性和格式正确性
### 3. 浏览相册照片

通过 `python3 （请参考skill目录中的脚本文件） --action photos --album-id "ALBUM_ID" --cookies cookies.json` 浏览指定相册中的照片。必填参数 `--album-id` 指定目标相册，可选参数 `--qq` 指定账号。返回照片列表，包含照片URL、缩略图、上传时间等信息。适用于查看相册内容和获取照片下载URL。- 验证返回数据的完整性和格式正确性
- 参考`浏览相册照片`的配置文档进行参数调优
### 4. 上传照片
通过 `python3 （请参考skill目录中的脚本文件） --action upload --photo "/path/to/image.jpg" --album-id "ALBUM_ID" --cookies cookies.json` 上传照片到指定相册。必填参数 `--photo` 指定本地图片路径，`--album-id` 指定目标相册。可选参数 `--qq` 指定账号。适用于照片备份和迁移场景.
**处理**: 解析上传照片的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回上传照片的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`上传照片`的配置文档进行参数调优
### 5. 下载单张照片
通过 `python3 （请参考skill目录中的脚本文件） --action download --url "PHOTO_URL" --cookies cookies.json` 下载单张照片。必填参数 `--url` 指定照片URL（从 `photos` action获取），可选参数 `--output` 指定下载目录。适用于选择性下载特定照片.
**处理**: 解析下载单张照片的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 6. 下载整个相册

通过 `python3 （请参考skill目录中的脚本文件） --action download-album --album-id "ALBUM_ID" --output ./downloads --cookies cookies.json` 下载整个相册的所有照片。必填参数 `--album-id` 指定目标相册，可选参数 `--output` 指定下载目录（默认当前目录）。适用于相册全量备份场景。- 验证返回数据的完整性和格式正确性
- 参考`下载整个相册`的配置文档进行参数调优
### 7. 创建相册

通过 `python3 （请参考skill目录中的脚本文件） --action create --title "我的新相册" --cookies cookies.json` 创建新相册。必填参数 `--title` 指定相册标题，可选参数 `--desc` 指定相册描述，`--qq` 指定账号。创建成功后返回新相册的 `album-id`。适用于批量上传前的相册准备.
#
## 使用流程

1. 首次使用执行扫码登录：`python3 （请参考skill目录中的脚本文件） --action login --cookies cookies.json`
2. 列出所有相册获取目标 `album-id`：`python3 （请参考skill目录中的脚本文件） --action list --cookies cookies.json`
3. 根据需求选择操作：浏览照片（`photos`）、上传照片（`upload`）、下载照片（`download`/`download-album`）、创建相册（`create`）
4. 上传照片时指定本地图片路径和目标相册ID
5. 下载照片时先通过 `photos` action获取照片URL，再执行下载
6. 如遇Cookie过期，重新执行 `login` action获取新Cookie

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 示例

### 示例1：扫码登录并备份整个相册

```bash
# 扫码登录，Cookie自动保存到cookies.json
python3 （请参考skill目录中的脚本文件） --action login --cookies cookies.json
# 输出: 二维码已生成，请使用社交平台App扫描登录...
# 登录成功后: Cookie已保存到 cookies.json
# ...
# 列出所有相册
python3 （请参考skill目录中的脚本文件） --action list --cookies cookies.json
# 输出示例:
# 相册ID: V0003 | 标题: 旅行 | 照片数: 45
# 相册ID: V0005 | 标题: 2024毕业季 | 照片数: 28
# ...
# 下载整个旅行相册
python3 （请参考skill目录中的脚本文件） --action download-album --album-id "V0003" --output ./downloads --cookies cookies.json
```

### 示例2：创建相册并上传多张照片

```bash
# 创建新相册
python3 （请参考skill目录中的脚本文件） --action create --title "2024毕业季" --desc "毕业旅行照片" --cookies cookies.json
# 输出: 相册创建成功，album-id: V0007
# ...
# 上传照片到新相册
python3 （请参考skill目录中的脚本文件） --action upload --photo "/path/to/graduation1.jpg" --album-id "V0007" --cookies cookies.json
python3 （请参考skill目录中的脚本文件） --action upload --photo "/path/to/graduation2.jpg" --album-id "V0007" --cookies cookies.json
# ...
# 浏览相册确认上传结果
python3 （请参考skill目录中的脚本文件） --action photos --album-id "V0007" --cookies cookies.json
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| Cookie过期 | `p_skey` 或 `skey` 失效 | 重新执行 `--action login` 扫码登录获取新Cookie |
| 相册ID无效 | `--album-id` 指向不存在的相册 | 先执行 `--action list` 获取有效的 `album-id` |
| 上传照片路径不存在 | `--photo` 指向的文件不存在或路径错误 | 检查图片文件路径，使用绝对路径确保可访问 |
| 下载照片URL无效 | `--url` 已过期或格式错误 | 重新执行 `--action photos` 获取最新的照片URL |
| 创建相册标题为空 | `--title` 参数缺失或为空 | 提供有效的相册标题字符串 |
| Cookie文件格式错误 | `cookies.json` JSON格式不正确 | 确认文件包含 `qq_number`、`p_skey`、`skey`、`uin` 四个字段且JSON格式有效 |
| 虚拟环境未激活 | 未执行 `source .venv/（请参考skill目录中的脚本文件）` | 先激活虚拟环境再执行脚本命令 |
| API接口变更 | 社交平台更新了非官方API | 等待工具更新适配新接口，或手动提取Cookie |

## 常见问题

### Q1: 如何扫码登录？

执行 `python3 （请参考skill目录中的脚本文件） --action login --cookies cookies.json` 命令。脚本会生成二维码，使用社交平台App扫描二维码完成登录。登录成功后Cookie自动保存到指定的cookies文件中，包含 `qq_number`、`p_skey`、`skey` 和 `uin` 字段.
### Q2: Cookie过期怎么办？

Cookie包含的 `p_skey` 和 `skey` 有时效性，过期后所有操作会返回认证失败。重新执行 `--action login` 扫码登录即可获取新的Cookie。建议在脚本中添加Cookie有效性检查，过期时自动触发重新登录.
### Q3: 如何获取相册ID？

执行 `python3 （请参考skill目录中的脚本文件） --action list --cookies cookies.json` 列出所有相册。返回结果包含每个相册的ID（`album-id`）、标题和照片数量。使用返回的 `album-id` 进行后续的照片浏览、上传或下载操作.
### Q4: 支持哪些图片格式上传？

上传功能支持常见的图片格式，包括JPG、JPEG、PNG、GIF、BMP等。通过 `--photo` 参数指定本地图片文件路径。建议使用绝对路径（如 `/path/to/image.jpg`）确保文件可访问。单次上传一张照片，批量上传需多次执行命令.
### Q5: 如何批量下载整个相册？

使用 `--action download-album` 命令下载整个相册的所有照片。指定 `--album-id` 和 `--output`（下载目录）参数。例如：`python3 （请参考skill目录中的脚本文件） --action download-album --album-id "V0003" --output ./downloads --cookies cookies.json`。脚本会自动遍历相册中所有照片并逐一下载.
### Q6: Cookie文件包含哪些字段？

Cookie文件（`cookies.json`）为JSON格式，包含4个字段：`qq_number`（社交平台账号）、`p_skey`（认证密钥）、`skey`（会话密钥）和 `uin`（用户标识，格式如 `o0123456789`）。也可手动从浏览器开发者工具（F12 -> Application -> Cookies）提取，但推荐使用扫码登录自动获取.
## 已知限制

- 依赖社交空间非官方API，平台接口变更后可能需要适配
- Cookie有时效性，过期后需重新扫码登录
- 上传操作为单张上传，暂不支持批量上传
- Cookie文件包含完整访问权限，需妥善保管
- 需要Python虚拟环境（`.venv`）已激活
