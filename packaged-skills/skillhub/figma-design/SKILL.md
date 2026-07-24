---
slug: "figma-design"
name: "figma-design"
version: 1.0.7
displayName: "Figma"
summary: "读文件/管评论/提设计令牌/下图片/建Webhook,Figma全管"
license: "Proprietary"
description: |-
  Read files, manage comments, extract design tokens, download images,
  and create webhooks in Figma。
tags:
  - Integrations
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# Figma

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 核心能力

- Read files, manage comments, extract design tokens, download images,
  and create webhooks in Figma
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 文件读取 | Figma文件URL或file_key | 文件JSON结构与节点数据 |
| 设计令牌提取 | file_key与目标令牌类型 | Tailwind/CSS设计令牌配置 |
| 图片下载 | file_key与node_id列表 | PNG/SVG格式图片文件 |
| 评论管理 | file_key与评论文本 | 评论发布/删除操作结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

```bash
clawlink_call_tool --tool "figma_get_current_user" --params '{}'
# .
clawlink_call_tool --tool "figma_discover_figma_resources" --params '{"figma_url": "https://www.figma.com/file/ABC123xyz/MyFile"}'
# .
clawlink_call_tool --tool "figma_get_file_json" --params '{"file_key": "ABC123xyz"}'
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | figma-design处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "design_result": "design_result_value",
      "design_metadata": "design_metadata_value",
      "design_status": "design_status_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/figma-design_template`

## 错误处理
| Status / Error | Meaning |
|:-------------:|:-------------:|
| Tool not found | The tool name does not exist in the current catalog. Verify with `clawlink_list_tools --integration figma`. |
| Missing connection | Figma is not connected. Direct the user to <https://claw-link.dev/dashboard?add=figma>. |
| `400 File type not supported` | File is a FigJam board or Slides file, not a Design file. Only Design files work with `get_file_json`. |
| `404 Not Found` | File key, node ID, or webhook does not exist or is not accessible to the authenticated user. |
| `403 Forbidden` | Insufficient permissions for the requested operation (e.g., team admin required for team webhooks). |
| Write rejected | User did not confirm a write action. Always confirm before executing writes. |

### 错误恢复步骤
1. Check that the ClawLink plugin is installed:

   bash

   ```
   skill-platform plugins list
   ```
2. If the plugin is installed but tools are missing, tell the user to send `/new` as a standalone message to reload the catalog.
3. If a fresh chat does not help, run:

   bash

   ```
   skill-platform config set tools.alsoAllow '["clawlink-plugin"]' --strict-json
   skill-platform gateway restart
   ```
4. After restart, tell the user to send `/new` again and retry.

### Troubleshooting: Invalid Tool Call

1. Ensure the integration slug is exactly `figma`.
2. Use `clawlink_describe_tool` to verify parameter names and types before calling.
3. For write operations, always call `clawlink_preview_tool` first.
> **处理方式**: 参考上表中的错误场景说明,按照对应建议进行处理和恢复。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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

### Discover resources from a Figma URL

```bash
clawlink_call_tool --tool "figma_discover_figma_resources" \
  --params '{
    "figma_url": "https://www.figma.com/file/ABC123xyz/MyDesign"
  }'
```

### Get file JSON and extract a specific node

```bash
clawlink_call_tool --tool "figma_get_file_json" \
  --params '{
    "file_key": "ABC123xyz"
  }'
```

### Download an image from a file node

```bash
clawlink_call_tool --tool "figma_download_figma_images" \
  --params '{
    "file_key": "ABC123xyz",
    "images": [
      {
        "node_id": "1:2",
        "file_name": "logo.png",
        "format": "png"
      }
    ]
  }'
```

### Post a comment on a file

```bash
clawlink_call_tool --tool "figma_add_a_comment_to_a_file" \
  --params '{
    "file_key": "ABC123xyz",
    "comment": {
      "text": "Please review the updated hero section"
    }
  }'
```

### Extract design tokens and convert to Tailwind

```bash
clawlink_call_tool --tool "figma_extract_design_tokens" \
  --params '{
    "file_key": "ABC123xyz"
  }'
# .
clawlink_call_tool --tool "figma_design_tokens_to_tailwind" \
  --params '{
    "tokens": { "$schema": ".", "colors": {.} }
  }'
```

## 常见问题

### Q1: 如何开始使用Figma？
A: 

## 已知限制

- **API速率限制**：Figma REST API对每个访问令牌的速率限制约为每分钟100次请求（具体阈值随账户类型变化），批量下载图片或提取大量节点时容易触发 `429 Too Many Requests` 错误。触发速率限制后需等待约60秒冷却窗口才能重试，且当前工具不支持自动指数退避重试，需手动间隔调用。高频评论发布操作（如批量添加评论）也受此限制约束，建议每批不超过20条评论。
- **文件大小与节点数量限制**：单个Figma文件的JSON结构在节点数超过5000时，`figma_get_file_json` 接口响应时间显著增加（可能超过30秒），且返回的JSON体积可能超过50MB导致内存压力。对超大型设计系统文件（如包含上千个组件的库文件），建议按 `node_id` 分批获取子树而非整文件拉取；整文件拉取超过20000个节点时，API可能返回不完整数据或直接超时。
- **组件变体（Variants）提取约束**：提取设计令牌时，组件变体的属性组合不会自动展开为独立令牌，需要手动遍历每个变体实例逐个提取。嵌套组件（Component内嵌Component）的令牌提取可能丢失内层组件被覆盖的样式属性（overrides），导致生成的Tailwind配置与实际渲染效果存在差异。此外，使用Figma Variables（变量系统）定义的颜色/间距令牌，无法通过 `get_file_json` 直接获取，需调用独立的Variables API端点。
- **插件兼容性与文件类型限制**：本技能依赖ClawLink插件桥接Figma API，当Figma平台发布新的API版本字段时，ClawLink插件未及时更新可能出现字段解析失败或返回空值。文件类型方面，仅支持Design文件（`.fig`），FigJam画板文件和Figma Slides幻灯片文件调用 `get_file_json` 会返回 `400 File type not supported` 错误；无法读取已归档（archived）或对当前用户未共享（无查看权限）的文件。
- **图片导出分辨率与格式限制**：`figma_download_figma_images` 支持PNG/SVG/JPG/PDF四种导出格式，但单次导出的图片分辨率上限为4096×4096像素（Figma API硬性限制），超出该尺寸的设计稿会被等比缩小，导致高清设计稿导出后清晰度下降。SVG导出对含位图填充（bitmap fill）或复杂混合模式（blend mode）的节点会退化为PNG嵌入而非矢量路径，失去无损缩放能力；批量下载超过100张图片时单次请求易超时，需分批调用。

