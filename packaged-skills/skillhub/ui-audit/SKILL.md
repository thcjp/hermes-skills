---
slug: "ui-audit"
name: "ui-audit"
version: "1.0.1"
displayName: "UI Audit"
summary: "自动化 UI 审计工具，基于 UX 原则评估界面的视觉层级、样式和无障碍性。"
license: "Proprietary"
description: |-
  ui-audit 是一个自动化 UI 审计技能，基于 Warp-Speed Decisioning 框架评估界面设计质量。
  支持 3 大支柱（Scaffolding、Decisioning、Crafting）、12 类 UI 模式库、4 级创新光谱和
  结构化审计报告生成。输出包含视觉层级、视觉样式、无障碍性等必检项，以及导航、可用性、
  入门引导等上下文检查项。适用于设计师、前端工程师和产品团队的设计评审场景。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tags:
  - 安全合规
---
# UI Audit

ui-audit 基于 Warp-Speed Decisioning 框架，对界面进行结构化 UX 审计。核心理念是
"Speed ≠ Recklessness"——快速设计不等于鲁莽设计，关键在于意图性。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

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
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 基础框架引用与决策流程
加载 `00-core-framework.md` 获取 3 支柱决策工作流，加载 `01-anchors.md` 获取 7 个设计韧性思维模型，
加载 `02-information-scaffold.md` 获取心理学、经济学、无障碍性和默认值理论。决策流程为三步权衡：
institutional knowledge → user familiarity → research，通过 JTBD（Jobs-to-be-done）支持度选择方案。

**处理**: 按照skill规范执行基础框架引用与决策流程操作,遵循单一意图原则。
**输出**: 返回基础框架引用与决策流程的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`基础框架引用与决策流程`相关配置参数进行设置
### 2. 新界面设计检查清单（6 步流程）
参照 `10-checklist-new-interfaces.md` 执行 6 步新界面设计流程。每步包含明确的输入、输出和验证标准。
同时参照 `11-checklist-fidelity.md` 检查组件状态（hover/focus/disabled/loading）、交互逻辑、
可扩展性和反馈机制。参照 `13-checklist-innovation.md` 评估 5 级原创性光谱（Level 0-4）。- 验证执行结果，确认输出符合预期格式
- 参考`新界面设计检查清单（6 步流程）`相关配置参数进行设置
### 3. 视觉样式审计（Spacing/Color/Elevation/Typography/Motion）
参照 `12-checklist-visual-style.md` 审计视觉样式。检查间距一致性（8px 基线网格）、
色彩调色板遵循度、阴影/elevation 层级、字体系统（display/body/mono 配对）、
圆角/边框一致性、图标风格统一性和动效原则。每项检查标注 pass/warn/fail/na 状态。

**输入**: 用户提供视觉样式审计（Spacing/Color/Elevation/Typography/Motion）所需的指令和必要参数。
**输出**: 返回视觉样式审计（Spacing/Color/Elevation/Typography/Motion）的执行结果,包含操作状态和输出数据。

- 执行`视觉样式审计（Spacing/Color/Elevation/Typography/Motion）`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`视觉样式审计（Spacing/Color/Elevation/Typography/Motion）`相关配置参数进行设置
### 4. UI 模式库匹配（12 类模式）
根据核心问题匹配模式库：`20-patterns-chunking.md`（卡片/标签页/手风琴/分页/轮播）、
`21-patterns-progressive-disclosure.md`（tooltip/popover/drawer/modal）、
`22-patterns-cognitive-load.md`（stepper/wizard/极简导航/简化表单）、
`23-patterns-visual-hierarchy.md`（字体/颜色/留白/尺寸/邻近性）、
`24-patterns-social-proof.md`（推荐语/UGC/徽章/社交集成）、
`25-patterns-feedback.md`（进度条/通知/验证/上下文帮助）、
`26-patterns-error-handling.md`（表单验证/撤销重做/对话框/自动保存）、
`27-patterns-accessibility.md`（键盘导航/ARIA/alt 文本/对比度/缩放）、
`28-patterns-personalization.md`（仪表盘/自适应内容/偏好设置/l10n）、
`29-patterns-onboarding.md`（引导教程/上下文提示/清单）、
`30-patterns-information.md`（面包屑/站点地图/标签/分面搜索）、
`31-patterns-navigation.md`（优先导航/离屏导航/粘性导航/底部导航）。- 验证执行结果，确认输出符合预期格式
- 参考`UI 模式库匹配（12 类模式）`相关配置参数进行设置
### 5. 结构化审计报告生成（JSON 格式）
生成包含必检项和上下文检查项的 JSON 审计报告。必检项：Visual Hierarchy、Visual Style、
Accessibility。上下文检查项：Navigation（多页应用）、Usability（交互流程）、Onboarding（新用户体验）、
Social Proof（落地页/营销页）、Forms（数据录入）。每项包含 6-10 个检查点，
标注 pass/warn/fail/na 状态。报告包含 macro_bets 对齐分析和 priority_fixes 优先修复列表。- 验证执行结果，确认输出符合预期格式
- 参考`结构化审计报告生成（JSON 格式）`相关配置参数进行设置
### 6. Macro Bet 对齐分析
分析设计与公司宏观押注的对齐度。4 类 macro bets：Velocity（功能快速上市）、
Efficiency（减少浪费）、Accuracy（更高准确率）、Innovation（发现未开发潜力）。
每类标注 strong/moderate/weak 对齐度，确保微观设计决策与公司宏观战略一致。

**输入**: 用户提供Macro Bet 对齐分析所需的指令和必要参数。
**输出**: 返回Macro Bet 对齐分析的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`Macro Bet 对齐分析`相关配置参数进行设置
#
## 使用流程

1. 确定审计类型：设计决策（加载 `00-core-framework.md`）、新界面（加载 `10-checklist-new-interfaces.md`）、
   模式选择（识别核心问题后加载对应 `20-31-patterns-*.md`）
2. 执行三步权衡：institutional knowledge → user familiarity → research
3. 消除与约束冲突的方案，优先与 macro bets 对齐的方案，基于 JTBD 支持度选择
4. 应用相关检查清单和模式参考执行审计
5. 生成 JSON 格式审计报告，包含必检项和上下文检查项
6. 输出 priority_fixes 优先修复列表，每项引用对应的 framework_reference

#
## 示例

### 示例1：电商落地页审计

```json
{
  "title": "Product Landing Page — Checkout Flow",
  "project": "ShopFast",
  "date": "2026-07-21",
  "macro_bets": [
    { "category": "velocity", "description": "复用现有卡片模式加速上线", "alignment": "strong" },
    { "category": "efficiency", "description": "减少结账步骤从 5 步到 3 步", "alignment": "strong" }
  ],
  "jtbd": [
    { "user": "首次购买用户", "situation": "浏览商品详情页", "motivation": "快速完成购买", "outcome": "减少决策疲劳" }
  ],
  "visual_hierarchy": {
    "title": "Visual Hierarchy",
    "checks": [
      { "label": "标题区分度", "status": "pass", "notes": "H1 32px/H2 24px，层级清晰" },
      { "label": "主操作按钮清晰度", "status": "warn", "notes": "CTA 与背景对比度 3.2:1，低于 4.5:1 标准" },
      { "label": "分组与邻近性", "status": "pass", "notes": "商品信息卡片间距 16px 一致" },
      { "label": "阅读流", "status": "pass", "notes": "Z 型阅读路径符合预期" },
      { "label": "字体层级", "status": "fail", "notes": "正文使用 14px，低于 16px 推荐值" },
      { "label": "色彩层级", "status": "warn", "notes": "次要信息与背景对比不足" }
    ]
  },
  "accessibility": {
    "title": "Accessibility",
    "checks": [
      { "label": "键盘可操作性", "status": "pass", "notes": "Tab 顺序符合视觉顺序" },
      { "label": "可见焦点", "status": "fail", "notes": "CTA 按钮无 focus 样式" },
      { "label": "色彩对比度", "status": "warn", "notes": "正文 #666 on #fff = 5.7:1 通过，链接 #007bff = 3.2:1 未通过" },
      { "label": "触摸目标", "status": "fail", "notes": "移动端 CTA 高度 38px，低于 44px 标准" }
    ]
  },
  "priority_fixes": [
    { "rank": 1, "title": "增大移动端 CTA 触摸目标", "description": "高度从 38px 提升到 44px", "framework_reference": "27-patterns-accessibility.md → Touch Targets" },
    { "rank": 2, "title": "添加 CTA focus 样式", "description": "添加 2px solid #0056b3 focus outline", "framework_reference": "27-patterns-accessibility.md → Keyboard Nav" },
    { "rank": 3, "title": "提升正文字号到 16px", "description": "从 14px 调整为 16px", "framework_reference": "12-checklist-visual-style.md → Typography" }
  ]
}
```

### 示例2：表单交互流程审计

```text
审计目标：用户注册表单（3 步 wizard）
核心问题：cognitive load（认知负荷）

模式匹配：22-patterns-cognitive-load.md
  → 推荐模式：Stepper + 简化表单 + 渐进式披露

检查结果：
  ├─ Visual Hierarchy: 6/8 pass, 2 warn
  │   ├─ 步骤指示器清晰度: pass（当前步骤高亮 #007bff）
  │   ├─ 表单标签关联: pass（label[for] 正确绑定）
  │   └─ 错误提示可见性: warn（错误文字 #ff0000 on #fff 对比度 3.9:1）
  ├─ Visual Style: 7/10 pass, 2 warn, 1 fail
  │   ├─ 间距一致性: pass（8px 基线网格）
  │   ├─ 输入框圆角: fail（4px 与按钮 8px 不一致）
  │   └─ 动效原则: warn（无 step 切换过渡动画）
  └─ Accessibility: 5/7 pass, 2 fail
      ├─ 键盘导航: pass（Tab 可达所有输入框）
      ├─ ARIA 标签: fail（step indicator 缺少 aria-current="step"）
      └─ 对比度 4.5:1: fail（placeholder #999 = 2.8:1 未通过）

Macro Bet 对齐: efficiency (strong) — 3 步 wizard 减少单页认知负荷
JTBD 支持: moderate — 注册流程与"快速开始使用"目标对齐
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 色彩对比度低于 4.5:1 | 正文或链接颜色与背景对比不足 | 在 `27-patterns-accessibility.md` 中查找 WCAG 标准色值，使用 contrast checker 验证后调整 |
| 触摸目标小于 44px | 移动端按钮/链接尺寸不足 | 参照 `27-patterns-accessibility.md` Touch Targets 章节，将最小尺寸调整为 44x44px |
| 缺少 focus 可见状态 | 交互元素未定义 :focus 样式 | 参照 `11-checklist-fidelity.md` Component States 章节，添加 focus outline |
| 间距系统不一致 | 未使用统一的 8px 基线网格 | 参照 `12-checklist-visual-style.md` Spacing 章节，建立 4/8/16/24/32px 间距 token |
| 缺少 alt 文本 | 图片未提供无障碍描述 | 参照 `27-patterns-accessibility.md` Alt Text 章节，为信息性图片添加描述，装饰性图片用 alt="" |
| 表单验证反馈缺失 | 用户提交后无即时错误提示 | 参照 `26-patterns-error-handling.md` Form Validation 章节，实现 inline 验证和错误消息 |
| 导航层级混乱 | 多页应用缺少面包屑或当前位置标识 | 参照 `31-patterns-navigation.md` 和 `30-patterns-information.md`，添加 breadcrumb 和 active state |

## 常见问题

### Q1: 审计报告中 pass/warn/fail/na 状态如何判定？
A: pass 表示完全符合 UX 原则和 WCAG 标准；warn 表示基本可用但有改进空间（如对比度 3.5:1 接近
4.5:1 阈值）；fail 表示违反关键原则（如触摸目标 < 44px）；na 表示不适用于当前界面类型
（如单页应用中的 navigation 检查项）。

### Q2: 12 类 UI 模式库如何选择匹配？
A: 首先识别核心问题类型：信息密度过高 → `20-patterns-chunking.md`；渐进式信息展示 →
`21-patterns-progressive-disclosure.md`；认知负荷过重 → `22-patterns-cognitive-load.md`；
视觉层级不清 → `23-patterns-visual-hierarchy.md`。加载对应模式文件后评估 benefits、
use cases、psychological principles 和 implementation guidelines。

### Q3: Macro Bet 分析如何与审计结果关联？
A: 每条 priority_fix 都应关联到公司 macro bets。例如 Velocity 押注的公司优先推荐复用现有模式
而非创新设计；Efficiency 押注的公司优先修复导致用户流失的可用性问题；Innovation 押注的公司
可以容忍更高风险的创新模式。对齐度标注为 strong/moderate/weak。

### Q4: 新界面设计的 6 步检查清单包含哪些步骤？
A: 参照 `10-checklist-new-interfaces.md`，6 步流程涵盖：1) 理解用户任务上下文 2) 识别核心
information architecture 3) 选择匹配的 UI 模式 4) 定义组件状态和交互 5) 应用视觉样式系统
6) 执行无障碍性验证。每步有明确的输入输出和验证标准。

### Q5: 5 级原创性光谱（Level 0-4）如何判定？
A: 参照 `13-checklist-innovation.md`：Level 0 = 直接复用现有模式（如标准表单）；Level 1 =
微调现有模式（如自定义表单样式）；Level 2 = 组合多个模式（如表单+wizard+渐进披露）；
Level 3 = 跨领域模式迁移（如将电商的购物车模式迁移到 SaaS）；Level 4 = 全新模式创造。
根据公司 Innovation macro bet 决定允许的原创性级别。

### Q6: 审计报告中每项检查点数量有何要求？
A: 每个检查项（Visual Hierarchy、Visual Style、Accessibility 等）应包含 6-10 个检查点。
Visual Hierarchy 检查标题区分度、主操作清晰度、分组邻近性、阅读流、字体层级、色彩层级、
留白使用、视觉重量平衡。Accessibility 检查键盘可操作性、可见焦点、色彩对比度（4.5:1）、
触摸目标（44px）、alt 文本、语义标记、reduced motion 支持。

## 已知限制

- 审计结果基于 UX 原则和 WCAG 标准，不替代真实用户测试
- 无法自动检测动态交互的时序问题（如动画延迟、加载状态切换）
- 对比度检查需要明确的色值输入，无法从截图自动提取
- 模式库匹配基于问题描述的准确性，模糊描述可能导致匹配偏差
- Innovation Level 判定具有主观性，建议团队讨论后确定
