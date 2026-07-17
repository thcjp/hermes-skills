---
slug: live-stream-script
name: live-stream-script
version: "2.0.0"
displayName: Live Stream Script
summary: 直播脚本生成器。带货直播、娱乐直播、知识直播话术、互动设计、开场预热、逼单话术、互动话术库。Live stream script generator
  for e-commerce, entert...
license: MIT-0
description: |-
  直播脚本生成器。带货直播、娱乐直播、知识直播话术、互动设计、开场预热、逼单话术、互动话术库。Live stream script generator
  for e-commerce, entert...

  核心能力:

  - 生活工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 个人健康、生活管理、习惯养成

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: generator, live, stream, 娱乐直播, commerce, 知识直播话术, 带货直播, 直播脚本生成
tags:
- Lifestyle
- Knowledge
tools:
- read
- exec
---

# Live Stream Script

直播话术和带货口播脚本生成器。开场预热、产品介绍、逼单促单、互动话术。

## Usage

```bash
live.sh warmup "产品"

live.sh open "主题"

live.sh product "产品名" "卖点1,卖点2"

live.sh close "产品名" "价格"

live.sh interact

live.sh help
```

## When to Use

* 用户要做直播带货，需要话术脚本
* 需要前5分钟留人预热话术
* 需要产品介绍、逼单促单话术
* 需要直播互动话术模板
* 需要直播开场白

脚本使用 Python 生成直播话术模板，涵盖预热、开场、产品讲解、促单、互动等环节。

## Commands

| Command | Description |
| --- | --- |
| `warmup` | 开场预热话术（前5分钟留人策略） |
| `open` | 直播开场话术 |
| `product` | 产品介绍话术（FABE法则） |
| `close` | 逼单/促单话术（限时+限量+赠品） |
| `interact` | 互动话术模板（关注/扣1/抽奖/挽留/下播） |
| `help` | 显示帮助信息 |

查看 `tips.md` 获取直播带货实战技巧（留人策略、逼单技巧、数据复盘等）。

## Output

## 所有输出为纯文本，可直接用于直播脚本。

💬 Feedback & Feature Requests: <https://bytesagain.com/feedback>
Powered by BytesAgain | bytesagain.com

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
