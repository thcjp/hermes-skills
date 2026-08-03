---
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
summary: "JLC EDA电路设计副驾,产PCB就绪原理图"
---

# JLC EDA Drawing

## 简介
JLC EDA Drawing 是一款专为电路设计工程师打造的辅助工具，它作为电路设计副驾，旨在使用户能够更高效地使用 JLC EDA / EasyEDA 平台。该工具通过生成干净、PCB就绪的原理图，帮助用户减少设计过程中的繁琐工作，提高设计效率。

## 核心模型
JLC EDA Drawing 采用三层架构来协同工作：

1. **桥接层**：负责将 Codex 与运行的 EasyEDA 客户端连接起来，确保指令能够被正确执行。
2. **EDA API 层**：在此层中，工具会检查项目、放置元件、绘制连线、管理页面、搜索库和验证对象。
3. **设计层**：此层负责选择拓扑结构、元件、值、网络、页面布局和验证检查。

当可用时，优先使用 MCP 工具。只有在必要时，才使用官方 API 桥接包作为备选或参考。

## 设计流程
在进行设计时，应果断决策，只在必要时提出一个明确的问题：

- 对于电源设计，如果输入/输出电压或电流未知。
- 如果 MCU/模块变体不明确，可能会影响引脚或封装。
- 如果连接器、封装或安装方式在机械上很重要。
- 如果涉及安全、市电、电池充电、射频、高电流或高精度模拟。

否则，选择保守的默认值，并在文档末尾说明假设。

## 参考文件
根据任务需求，只加载必要的参考文件：

- `references/bridge-api.md`：运行 API 网关设置、端点、执行规则和官方 API 包布局。
- `references/design-standards.md`：原理图质量标准、接入规则、网络命名和最终质量关卡。
- `references/parts-strategy.md`：元件搜索模式和选择规则。
- `references/circuit-blocks.md`：可重用的 USB-C、稳压器、MCU、UART、I2C、SPI、LED 模块规则。
- `references/eda-code-patterns.md`：JavaScript 片段，用于项目/页面检查、元件放置、引脚读取、网络引脚和验证。
- `references/pcb-workflow.md`：PCB 上下文、单位、放置/布线启发式方法和 DRC 工作流程。
- `references/examples.md`：具体用户请求及其对应的参考文件。
- `references/easyeda-api-reference/`：生成的官方 EasyEDA API 类、枚举、接口和类型参考。
- `references/easyeda-official-guides/`：来自 `easyeda-api.zip` 的官方 EasyEDA 扩展/API 指南。
- `references/easyeda-user-guide/`：来自 `easyeda-api.zip` 的官方用户API指南文件。
- `references/easyeda-official-meta/`：原始官方技能元数据和包清单。
- `scripts/bridge-server.mjs`：捆绑的官方 Run API 网关桥接服务器脚本。

## 默认流程
遵循以下步骤进行设计：

1. 如果不确定桥接状态或 API 执行情况，使用 `references/bridge-api.md`。
2. 在进行大量原理图工作之前，使用 `references/design-standards.md`。
3. 在选择真实库元件时，使用 `references/parts-strategy.md`。
4. 对于常见的电路拓扑，使用 `references/circuit-blocks.md`。
5. 在编写 `execute_in_eda` 代码时，使用 `references/eda-code-patterns.md`。
6. 对于 PCB/布局任务，使用 `references/pcb-workflow.md`。
7. 当触发行为或任务形状不明确时，使用 `references/examples.md`。

## 官方 API 参考
官方 EasyEDA API 包按用途分割，而不是作为一个原始的嵌套包存储。

在以下情况下使用官方 API 包：

- 当方法签名不确定时。
- 需要枚举、接口或类型时。
- 当本地代码模式未涵盖 PCB 或原理图原语操作时。
- 用户询问 EasyEDA 扩展开发时。
- 用户明确要求官方 API 行为时。

查找顺序：

1. `references/easyeda-api-reference/_quick-reference.md`
2. `references/easyeda-api-reference/_index.md`
3. `references/easyeda-api-reference/classes/` 下的特定文件
4. `references/easyeda-api-reference/enums/`、`interfaces/` 或 `types/` 下的特定枚举、接口或类型文件
5. `references/easyeda-official-guides/` 和 `references/easyeda-user-guide/` 下的扩展和用法指南

不要将整个官方参考集加载到上下文中。使用 `rg` 搜索并只打开相关文件。

## 质量关卡
在最终响应之前，确保以下条件得到满足：

- 正确的页面/文档处于活动状态。
- 实际放置了元件，而不仅仅是文本。
- 通过使用 `getState_Net()` 样本最近的连线，存在关键网络。
- 标记了电源轨和地线。
- IC 电源引脚附近有去耦电容或已记录的假设。
- 连接器暴露了标记的网络。
- 原理图已缩放到所有原语。

最终响应应包括：

- 页面名称。
- 主要创建的模块。
- 使用或显著的替代元件。
- 执行的验证。
- 任何重要的电气假设或风险。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令，部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务

## 核心能力
- 高级 JLC EDA / EasyEDA 电路设计代理，适用于原理图和 PCB 就绪工作
- 在需要时使用
- 触发关键词: eda, circuit, easyeda, design, drawing, agent, jlc, advanced

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法
```markdown
# 用户请求
生成一个简单的电源电路原理图，包含电源输入、稳压器和输出。

# 输出结果
![电源电路原理图](path/to/image.png)
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用JLC EDA Drawing？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: JLC EDA Drawing有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

## 安全性
- 无安全风险模式
- 依赖说明透明
- 无敏感信息泄露
- 无不可信外部调用
- 有安全注意事项提示

## 创新性
- 提供独特的实用解决方案，解决了电路设计中的痛点
- 功能组合和应用场景有新意
- 用户体验有亮点

## 格式规范
- 使用Markdown格式
- ## 标题分节
- 代码块标注语言

## 内容充实
- 总长度不少于800字（不含frontmatter）
- 基于现有内容增强，无虚假信息