---
slug: zhuchenggong-doubao-image-gen
name: zhuchenggong-doubao-image-gen
version: "1.0.0"
displayName: "Doubao Image Gen è±\x86å\x8C\Nå\x9B¾ç\x89\x87ç\x94\x9Fæ\x88\x90"
summary: 豆包AI图片生成技能 - 视觉设计师专用
license: MIT-0
description: |-
  豆包AI图片生成技能 - 视觉设计师专用\n\n核心能力:\n- 创意设计领域的专业化AI辅助工具\n- 基于高人气开源Skill深度优化升级\n\
  - 移除风险代码,增强安全性和稳定性\n\n适用场景:\n- 内容创作、设计生成、多媒体制作\n- 独立开发者与一人公司效率提升\n- 自动化工作流与智能决策辅助\n\
  \n差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。\n\n触发关键词: doubao, 豆包,\
  \ zhuchenggong, 图片生成技能, å\x9B¾ç\x89\x87ç\x94\x9Fæ\x88\x90, è±\x86å\x8C, gen, 视觉设计师专
tags: '[''Creative'']'
tools: '[read, exec]'
---

# Doubao Image Gen è±åå¾ççæ

## ★★★ 调度时必读 ★★★

收到任务后，**第一步**必须是：问用户想要什么样的图片？有什么要求？
不要直接去生成图片！

---

## 完整流程

一、点开豆包AI创作页面
二、**问客户**想要什么样的图片/有什么要求 ← 第一步！
三、客户确认后，输入提示词
四、设置比例：默认3:4，**如果客户选了比例则按客户的**
五、点击发送按钮生成图片
六、等待图片生成完成
七、**★ 子Agent截大图** - 生成后立即截4张图，通过 message 工具发给用户选择
八、用户选好后，点开大图确认
九、用户确认后，点击下载原图保存
十、**★ 复制到 D 盘** - 下载后立即复制到 D:\Skill平台\downloads\images\

## 生成前确认要素（必须）

1. ★ 先问客户：想要什么样的图片？有什么提示词/要求？
2. 客户确认后，输入提示词
3. 设置比例：默认3:4，如果客户选了比例则按客户的
4. 点击发送按钮生成

## 关键规则

1. ★ 必须先问客户想要什么样的图片
2. 输入提示词后，点发送按钮（向上的箭头），不要按回车
3. 等待图片完全生成后再截图
4. 用户选好后要点开大图确认
5. 用户确认后才能保存
6. 每步必须拿到结果才能下一步
7. ★ **截图必须用 message 工具发图片给用户**，不要用虚拟路径
8. ★ 截图路径用实际路径：`/home/success/.skill-platform/media/browser/xxx.jpg`
9. ★ **下载后必须复制到 D 盘**：`cp xxx.jpg /mnt/d/Skill平台/downloads/images/`

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
