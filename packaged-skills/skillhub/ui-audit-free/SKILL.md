---
slug: "ui-audit-free"
name: "ui-audit-free"
version: 1.0.1
displayName: "UI Audit Free"
summary: "基础版 UI 审计工具，评估界面的视觉层级、视觉样式和无障碍性。"
license: "MIT"
description: |-
  ui-audit-free 是自动化 UI 审计技能的基础版本，基于 Warp-Speed Decisioning 框架评估界面设计.
  支持 3 大支柱决策流程和视觉层级、视觉样式、无障碍性三项必检项审计。不包含 12 类 UI 模式库
  匹配、Macro Bet 对齐分析和上下文检查项。适合快速设计评审，升级完整版获取全量审计能力.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 安全合规
pricing_tier: "L1-入门级"
suggested_price: "9.9 CNY/per_use"

---
# UI Audit Free

ui-audit-free 基于 Warp-Speed Decisioning 框架，对界面进行基础 UX 审计。核心理念是
"Speed ≠ Recklessness"——快速设计不等于鲁莽设计，关键在于意图性.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | UI Audit Free处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 核心理念：3 Pillars of Warp-Speed Decisioning

1. **Scaffolding** — 用于自动化重复决策的规则体系
2. **Decisioning** — 用于做出新决策的流程
3. **Crafting** — 用于执行决策的检查清单

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
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

### 1. 基础框架引用与决策流程
加载 `00-core-framework.md` 获取 3 支柱决策工作流。决策流程为三步权衡：
institutional knowledge → user familiarity → research，通过 JTBD 支持度选择方案.
基础版支持核心决策框架，不包含 `01-anchors.md` 和 `02-information-scaffold.md` 的完整内容.
**处理**: 解析基础框架引用与决策流程的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回基础框架引用与决策流程的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`基础框架引用与决策流程`的配置文档进行参数调优
### 2. 视觉样式审计（Spacing/Color/Elevation/Typography/Motion）
参照 `12-checklist-visual-style.md` 审计视觉样式。检查间距一致性（8px 基线网格）、
色彩调色板遵循度、阴影/elevation 层级、字体系统配对、圆角/边框一致性和图标风格统一性.
每项检查标注 pass/warn/fail/na 状态.
**输入**: 用户提供视觉样式审计（Spacing/Color/Elevation/Typography/Motion）所需的指令和必要参数.
**输出**: 返回视觉样式审计（Spacing/Color/Elevation/Typography/Motion）的处理结果,包含执行状态码、结果数据和执行日志.
- 针对`视觉样式审计（Spacing/Color/Elevation/Typography/Motion）`,解析输入数据并返回响应
- 验证返回数据的完整性和格式正确性
- 参考`视觉样式审计（Spacing/Color/Elevation/Typography/Motion）`的配置文档进行参数调优
### 3. 基础审计报告生成（JSON 格式）
生成包含三项必检项的 JSON 审计报告：Visual Hierarchy、Visual Style、Accessibility.
每项包含 6-10 个检查点，标注 pass/warn/fail/na 状态。基础版不包含 Navigation、Usability、
Onboarding 等上下文检查项，也不包含 macro_bets 对齐分析。- 验证返回数据的完整性和格式正确性
- 参考`基础审计报告生成（JSON 格式）`的配置文档进行参数调优
#
## 使用流程

1. 确定审计目标界面，收集截图或设计稿
2. 执行三步权衡：institutional knowledge → user familiarity → research
3. 参照 `12-checklist-visual-style.md` 执行视觉样式审计
4. 生成 JSON 格式审计报告，包含三项必检项
5. 输出基础修复建议列表

## 示例

### 示例1：电商落地页基础审计

```json
{
  "title": "Product Landing Page — Checkout Flow",
  "project": "ShopFast",
  "date": "2026-07-21",
  "visual_hierarchy": {
    "title": "Visual Hierarchy",
    "checks": [
      { "label": "标题区分度", "status": "pass", "notes": "H1 32px/H2 24px，层级清晰" },
      { "label": "主操作按钮清晰度", "status": "warn", "notes": "CTA 与背景对比度 3.2:1，低于 4.5:1 标准" },
      { "label": "分组与邻近性", "status": "pass", "notes": "商品信息卡片间距 16px 一致" },
      { "label": "字体层级", "status": "fail", "notes": "正文使用 14px，低于 16px 推荐值" }
    ]
  },
  "accessibility": {
    "title": "Accessibility",
    "checks": [
      { "label": "键盘可操作性", "status": "pass", "notes": "Tab 顺序符合视觉顺序" },
      { "label": "可见焦点", "status": "fail", "notes": "CTA 按钮无 focus 样式" },
      { "label": "色彩对比度", "status": "warn", "notes": "链接 #007bff = 3.2:1 未通过 4.5:1" },
      { "label": "触摸目标", "status": "fail", "notes": "移动端 CTA 高度 38px，低于 44px 标准" }
    ]
  }
}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 色彩对比度低于 4.5:1 | 正文或链接颜色与背景对比不足 | 在 `27-patterns-accessibility.md` 中查找 WCAG 标准色值 |
| 触摸目标小于 44px | 移动端按钮/链接尺寸不足 | 将最小尺寸调整为 44x44px |
| 缺少 focus 可见状态 | 交互元素未定义 :focus 样式 | 添加 focus outline 样式 |
| 间距系统不一致 | 未使用统一的 8px 基线网格 | 建立 4/8/16/24/32px 间距 token |
| 缺少 alt 文本 | 图片未提供无障碍描述 | 为信息性图片添加描述 |

## 常见问题

### Q1: 免费版支持哪些检查项？
A: 免费版支持三项必检项：Visual Hierarchy、Visual Style、Accessibility。不包含 Navigation、
Usability、Onboarding、Social Proof、Forms 等上下文检查项。如需完整审计，请升级到完整版 ui-audit.
### Q2: 免费版可以使用 12 类 UI 模式库吗？
A: 免费版不包含 UI 模式库匹配功能。完整版支持 12 类模式匹配，包括 `20-patterns-chunking.md`、
`21-patterns-progressive-disclosure.md`、`22-patterns-cognitive-load.md` 等模式文件的完整引用.
### Q3: Macro Bet 分析在免费版中可用吗？
A: 免费版不包含 Macro Bet 对齐分析。完整版支持 Velocity、Efficiency、Accuracy、Innovation
四类宏观押注的对齐度分析，帮助确保微观设计决策与公司战略一致.
### Q4: 免费版的审计报告包含 priority_fixes 吗？
A: 免费版生成基础修复建议，但不包含引用 framework_reference 的结构化 priority_fixes 列表.
完整版输出带优先级排序和框架引用的完整修复列表.
### Q5: 如何升级到完整版？
A: 将技能替换为完整版 ui-audit 即可。完整版包含 6 项核心能力、12 类 UI 模式库、
Macro Bet 分析、上下文检查项和结构化优先修复列表.
## 已知限制

- 仅支持三项必检项，不包含 Navigation、Usability、Onboarding 等上下文检查项
- 不包含 12 类 UI 模式库匹配功能
- 不包含 Macro Bet 对齐分析
- 不包含 5 级原创性光谱（Level 0-4）评估
- 不包含 `01-anchors.md` 和 `02-information-scaffold.md` 的完整内容

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "UI Audit Free处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "ui-audit"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
