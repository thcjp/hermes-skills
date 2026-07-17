---
slug: multi-search-engine-simple
name: multi-search-engine-simple
version: "1.0.0"
displayName: "Multi Search Engine æ\x9E\x81ç®\x80å\x9B½å\x86\Nç\x89\x88"
summary: 【国内精简版】多种免费搜索方式在互联网上搜索最新信息，10个国内网站（精简7个国内不能访问的海外网站）
license: MIT-0
description: |-
  【国内精简版】多种免费搜索方式在互联网上搜索最新信息，10个国内网站（精简7个国内不能访问的海外网站）\n\n核心能力:\n- 研究工具领域的专业化AI辅助工具\n\
  - 基于高人气开源Skill深度优化升级\n- 移除风险代码,增强安全性和稳定性\n\n适用场景:\n- 数据研究、文献分析、信息收集\n- 独立开发者与一人公司效率提升\n\
  - 自动化工作流与智能决策辅助\n\n差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。\n\n\
  触发关键词: 上搜索最新信, æ\x9E\x81ç®\x80å\x9B½å\x86, 国内精简版, engine, 方式在互联网, 多种免费搜索, multi,\
  \ 个国内网站
tags: '[''Research'']'
tools: '[read, exec]'
---

# Multi Search Engine æç®å½åç

集成 10 个免费搜索引擎。

## Search Engines

* **Baidu**: `https://www.baidu.com/s?wd={keyword}`
* **Bing CN**: `https://cn.bing.com/search?q={keyword}&ensearch=0`
* **Bing INT**: `https://cn.bing.com/search?q={keyword}&ensearch=1`
* **360**: `https://www.so.com/s?q={keyword}`
* **Sogou**: `https://sogou.com/web?query={keyword}`
* **WeChat**: `https://wx.sogou.com/weixin?type=2&query={keyword}`
* **Toutiao**: `https://so.toutiao.com/search?keyword={keyword}`
* **Jisilu**: `https://www.jisilu.cn/explore/?keyword={keyword}`
* **Ecosia**: `https://www.ecosia.org/search?q={keyword}`
* **WolframAlpha**: `https://www.wolframalpha.com/input?i={keyword}`

## License

MIT

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
