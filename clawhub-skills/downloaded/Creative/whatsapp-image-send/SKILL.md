---
slug: whatsapp-image-send
name: whatsapp-image-send
version: "1.0.1"
displayName: WhatsApp Image Send
summary: Send images, videos, audio, or documents via WhatsApp by downloading, copying
  to workspace, sendi...
license: MIT
description: |-
  Send images, videos, audio, or documents via WhatsApp by downloading,
  copying to workspace, sendi...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: whatsapp, images, audio, send, documents, videos, image
tags:
- Creative
tools:
- read
- exec
---

# WhatsApp Image Send

## Workflow

1. **Download**: Save file to `/tmp/<filename>`

   bash

   ```
   curl -o /tmp/<filename> <url>
   ```
2. **Copy to workspace**: WhatsApp requires workspace path

   bash

   ```
   cp /tmp/<filename> ~/.skill-platform/workspace/
   ```
3. **Send to WhatsApp**

   bash

   ```
   message --channel whatsapp --target <phone> --filePath /home/seekey/.skill-platform/workspace/<filename> --message "<caption>"
   ```
4. **Cleanup**: Delete temp file

   bash

   ```
   rm /tmp/<filename>
   ```

## Notes

* Phone format: +country + number (e.g., +14843124960)
* Supported: jpg, png, gif, video, audio, document

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
