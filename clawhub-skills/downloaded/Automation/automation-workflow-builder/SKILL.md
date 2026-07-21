---
slug: automation-workflow-builder
name: automation-workflow-builder
version: "1.0.0"
displayName: Automation Workflow 
  æ\x9E\x84å»ºå\x99¨ï¼\x8Cè®¾è®¡å¹¶æ\x89§è¡\x8Cè·¨å¹³å\x8F°è\x87ªå\x8A¨å\x8C\x96æµ\x81\
  ç¨\x8Bï¼\x8Cæ\x94¯æ\x8C\x81å®\x9Aæ\x97¶è§¦å\x8F\x91ã\x80\x81æ\x96\x87ä»¶ç\x9B\x91\
  æ\x8E§ã\x80\x81å¤\x9Aæ­¥éª¤æ\x93\x8Dä½\x9Cã\x80\x82é\x80\x82ç\x94¨äº\x8Eæ\x95°æ\x8D\
  ®å\x90\x8Cæ­¥ã\x80\x81å\x86\Nå®¹å\x8F\x91å¸\x83ã\x80\x81æ\x8A¥å\x91\x8Aç\x94\x9F\
  æ\x88\x90ã\x80\x82ï¼\x89"
summary: 自动化工作流构建器，设计并执行跨平台自动化流程，支持触发器、条件判断、多步骤操作。
license: MIT-0
description: |-
  自动化工作流构建器，设计并执行跨平台自动化流程，支持触发器、条件判断、多步骤操作。\n\n核心能力:\n- 效率工具领域的专业化AI辅助工具\n\
  - 基于高人气开源Skill深度优化升级\n- 移除风险代码,增强安全性和稳定性\n\n适用场景:\n- 工作流自动化、任务调度、批处理\n- 独立开发者与一人公司效率提升\n\
  - 自动化工作流与智能决策辅助\n\n差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags: '[''Automation'']'
tools:
  - read
  - exec
---
# automation-workflow-builderï¼èªå¨åå·¥ä½æµæå»ºå¨ï¼è®¾è®¡å¹¶æ§è¡è·¨å¹³å°èªå¨åæµç¨ï¼æ¯æå®æ¶è§¦åãæä»¶çæ§ãå¤æ­¥éª¤æä½ãéç¨äºæ°æ®åæ­¥ãåå®¹åå¸ãæ¥åçæãï¼

设计并执行自动化工作流，替代重复性人工操作。

## 功能特性

### 1. 触发器系统

* 定时触发（Cron）
* 文件变化触发
* API webhook 触发
* 手动触发

### 2. 条件判断

* IF/ELSE 逻辑
* 多条件组合
* 数据过滤

### 3. 操作节点

* 文件操作（读/写/移动/复制）
* 网络请求（GET/POST）
* 数据处理（转换/格式化）
* 命令执行
* 通知发送

### 4. 工作流模板

* 数据同步
* 内容发布
* 报告生成
* 监控告警

## 示例

```javascript
// 示例 1：定时抓取 + 处理 + 保存
const workflow = {
  trigger: { type: "cron", schedule: "0 */6 * * *" },
  steps: [
    { action: "fetch", url: "https://api.example.com/data" },
    { action: "transform", script: "process(data)" },
    { action: "save", path: "./output/data.json" }
  ]
}

// 示例 2：文件监控 + 自动处理
const workflow = {
  trigger: { type: "watch", path: "./inbox" },
  steps: [
    { action: "read", file: "${trigger.file}" },
    { action: "process", type: "convert" },
    { action: "move", to: "./processed" }
  ]
}

// 示例 3：多步骤数据同步
const workflow = {
  trigger: { type: "manual" },
  steps: [
    { action: "fetch", url: "source-api", output: "data1" },
    { action: "fetch", url: "another-api", output: "data2" },
    { action: "merge", inputs: ["data1", "data2"] },
    { action: "upload", destination: "cloud-storage" }
  ]
}
```

## 预置工作流模板

### 模板 1：竞品价格监控

```text
触发：每天 9:00
步骤：
1. 抓取竞品网站价格
2. 与本地数据对比
3. 如有变化，发送通知
4. 保存历史记录
```

### 模板 2：内容自动发布

```text
触发：新文件添加到./drafts
步骤：
1. 读取草稿内容
2. 格式化/优化
3. 发布到目标平台
4. 记录发布日志
```

### 模板 3：数据报告生成

```text
触发：每周一 8:00
步骤：
1. 从多个 API 拉取数据
2. 合并、计算指标
3. 生成图表/表格
4. 导出 PDF/Excel
5. 发送邮件/消息
```

## 使用场景

1. **电商运营** - 价格监控、库存同步、订单处理
2. **内容创作** - 素材收集、格式转换、多平台发布
3. **数据分析** - 数据抓取、清洗、报告生成
4. **客户服务** - 自动回复、工单处理、反馈收集
5. **项目管理** - 进度跟踪、状态同步、提醒通知

## 不适用场景

以下场景Automation Workflow不适合处理：

- 需要人工创意判断的任务
- 非结构化头脑风暴
- 人际沟通协调


## 触发条件

需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于非本工具能力范围的需求。


## 定制开发

需要定制化自动化工作流、企业级集成方案？

📧 联系：careytian-ai@github

---

## 许可证

MIT-0

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Automation Workflow？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Automation Workflow有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
