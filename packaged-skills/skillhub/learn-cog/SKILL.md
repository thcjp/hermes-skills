---
slug: "learn-cog"
name: "learn-cog"
version: "1.0.0"
displayName: "个性化学习助手"
summary: "AI驱动的个性化学习助手，支持项目教程、语言学习、写作反馈、视觉学习与学习指南。"
license: "Proprietary"
description: |-
  个性化学习助手，基于CellCog提供多模式AI辅导。
  支持项目教程、语言学习、写作反馈、视觉学习与学习指南生成。
  覆盖STEM、人文、技术与职业技能等多学科领域。
  适用于学生、开发者与终身学习者的知识获取与技能提升。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
---
# 个性化学习助手

AI驱动的个性化学习助手，支持项目教程、语言学习、写作反馈、视觉学习与学习指南。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 个性化学习助手处理的输入数据或指令 |
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

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python环境**: Python 3.8+（如使用CellCog SDK）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| CellCog SDK | Python库 | 可选 | `pip install -U cellcog` |
| CELLCOG_API_KEY | API密钥 | 可选 | CellCog平台获取 |
| 终端/Shell | CLI | 可选 | 操作系统自带 |

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行学习辅导任务

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 项目教程（Project Tutorials）
通过实战项目驱动学习，从零到一构建完整应用：

- **逐步引导**：将复杂项目拆解为可执行的步骤，每步附带代码示例
- **项目类型**：REST API搭建、Web应用开发、CLI工具构建、数据处理管道等
- **可运行代码**：提供可直接运行的代码示例，边学边做
- **深度概念讲解**：在项目实践中讲解Docker容器、React Hooks等技术原理
- **能力评估**：通过mini-project综合检验学习成果

示例请求：

> "Walk me through building a REST API step by step"
> "Teach me React hooks: My level is I know basic JavaScript, never used React"

**输出**: 返回项目教程（Project Tutorials）的处理结果,包含执行状态码、结果数据和执行日志。
### 语言学习（Language Learning）
系统化掌握新语言，覆盖听说读写全方位训练：

- **语法讲解（Grammar Explanations）**：如"Explain Japanese particles with examples"
- **对话练习（Conversation Practice）**：如"Practice ordering food in French"场景对话
- **词汇构建（Vocabulary Building）**：如"Teach me 20 essential business Chinese phrases"
- **多语言支持**：日语（JLPT N4-N1）、法语、西班牙语、中文等
- **文化背景**：附带语言使用的文化语境与注意事项

**输入**: 用户提供语言学习（Language Learning）所需的指令和必要参数。
**处理**: 解析语言学习（Language Learning）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回语言学习（Language Learning）的处理结果,包含执行状态码、结果数据和执行日志。### 写作反馈（Writing Feedback）

对文章、论文、邮件等写作内容提供专业反馈：

- **语法与拼写检查**：识别并修正语法错误与拼写问题
- **结构优化**：评估文章结构，建议段落重组与逻辑改进
- **语言润色**：优化用词、句式与语气，提升表达力
- **写作风格指导**：学术写作、商务写作、创意写作的风格调整
- **语言学习写作**：如"Check my Spanish essay and explain my mistakes"

### 视觉学习（Visual Learning）
通过图表、图示、信息图等视觉化方式辅助理解：

- **概念图示**：如"Create a diagram explaining the water cycle"
- **流程图**：将复杂流程可视化为步骤图
- **信息图**：将数据与概念组织为易理解的视觉格式
- **对比图**：通过视觉对比帮助理解差异
- **学习风格适配**：支持Visual（图表）、Examples（示例）、Analogies（类比）、Step-by-Step（步骤）、Big Picture（全局）、Hands-On（实践）等多种学习风格

**输入**: 用户提供视觉学习（Visual Learning）所需的指令和必要参数。
**处理**: 解析视觉学习（Visual Learning）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 学习指南（Study Guides）
生成系统化的学习材料与备考资源：

- **学习指南（Study Guides）**：如"Create a study guide for AP Chemistry exam"
- **闪卡（Flashcards）**：如"Generate 50 flashcards for Spanish vocabulary"
- **模拟测试（Practice Tests）**：如"Create a practice quiz on US History 1900-1950"
- **摘要笔记（Summary Notes）**：如"Summarize Chapter 5 of my biology textbook"
- **速查表（Cheat Sheets）**：如"Create a one-page reference for Python syntax"

**输入**: 用户提供学习指南（Study Guides）所需的指令和必要参数。
**处理**: 解析学习指南（Study Guides）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 概念解释与作业辅导（Concept Explanations & Homework）
多角度解释概念与作业问题解答：

- **概念拆解**：如"Explain quantum entanglement like I'm 10 years old"
- **多角度解释**：如"Explain recursion using 3 different analogies"
- **数学解题**：逐步解答微积分、物理等问题并解释每步
- **代码调试**：解释代码为何不工作并帮助修复
- **作文结构**：帮助构建论文框架与论点

**处理**: 解析概念解释与作业辅导（Concept Explanations & Homework）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回概念解释与作业辅导（Concept Explanations & Homework）的处理结果,包含执行状态码、结果数据和执行日志。

---

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 明确学习目标：概念理解、项目实践、语言学习、写作反馈或备考
3. 说明当前水平：如"Complete beginner"或"I understand the basics"
4. 选择学习风格：Visual、Examples、Analogies、Step-by-Step、Big Picture或Hands-On
5. 使用自然语言描述学习需求，Agent生成个性化学习内容
6. 通过主动回忆（Active Recall）与练习巩固学习成果

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤。

## 示例

### 示例1：学习React Hooks

```
用户: Teach me React hooks, I know basic JavaScript, never used React
# ...
Agent: React Hooks学习计划：
1. What problem do hooks solve? - 状态逻辑复用与组件简化
2. useState with simple examples - 计数器示例
3. useEffect with practical use cases - 数据获取与副作用
4. When to use which hook - 决策树
5. A mini-project putting it together - Todo App
# ...
[附带可运行的代码示例]
```

### 示例2：生成AWS认证学习指南

```
用户: Create a study guide for the AWS Solutions Architect exam
# ...
Agent: AWS Solutions Architect学习指南：
- Key services and when to use them (EC2, S3, RDS, Lambda...)
- Networking concepts (VPC, Subnets, Route53...)
- Security best practices (IAM, KMS, Security Groups...)
- Cost optimization strategies (Reserved Instances, Spot Fleet...)
[每节附练习题]
```

### 示例3：日语对话练习

```
用户: Help me practice Japanese, Level: JLPT N4, Focus: Conversational
# ...
Agent: 日语对话练习 - 在东京问路：
- Scenario: Asking for directions in Tokyo
- Vocabulary list: 駅、交差点、右、左...
- Grammar points used: 〜はどこですか、〜てください
- Cultural notes: 礼貌用语与鞠躬礼仪
- Variations to practice: 正式场合与日常场景
[Romaji + 汉字 + ひらがな标注]
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| CellCog SDK未安装 | 未执行pip install | 运行 `pip install -U cellcog` 安装SDK |
| CELLCOG_API_KEY缺失 | 环境变量未设置 | 设置 `CELLCOG_API_KEY` 环境变量；或使用Agent内置LLM |
| 学习内容过浅/过深 | 未说明当前水平 | 明确说明水平：Complete beginner / Intermediate / Advanced |
| 概念解释不清楚 | 学习风格不匹配 | 尝试不同学习风格：Visual / Analogies / Step-by-Step |
| 代码示例无法运行 | 环境依赖缺失 | 检查Python/Node版本；安装所需依赖包 |
| 请求超时 | 内容生成耗时较长 | 使用agent模式而非agent team模式；缩小请求范围 |

## 常见问题

### Q1: 如何获得最佳学习效果？
A: 1）说明当前水平；2）多问"为什么"而非只要答案；3）请求练习题；4）承认困惑点；5）基于已理解的内容构建新知识；6）使用主动回忆（要求测验而非仅解释）。

### Q2: agent模式和agent team模式有什么区别？
A: `agent`模式适合大多数学习场景：快速解释、作业辅导、学习材料生成。`agent team`模式适合综合学习：完整课程大纲、研究论文、多源综合分析。

### Q3: 支持哪些学科领域？
A: STEM（数学、物理、化学、生物、计算机、统计）、人文（历史、文学、哲学、语言、心理）、职业（商业、金融、营销、项目管理、设计、法律）、技术技能（编程语言、云平台、DevOps、数据工程、AI/ML）。

### Q4: 如何进行语言学习写作反馈？
A: 将你的写作内容发送给Agent，说明语言（如西班牙语），Agent会检查语法错误、解释错误原因、提供修改建议并优化表达。

### Q5: CellCog未安装怎么办？
A: 运行 `/cellcog-setup` 安装认证，或手动执行 `pip install -U cellcog` 并设置 `CELLCOG_API_KEY`。也可直接使用Agent内置LLM进行学习辅导。

### Q6: 如何生成备考学习计划？
A: 提供考试名称、时间线、目标分数、薄弱环节，Agent会生成包含每周计划、资源推荐、练习测试策略与考前清单的完整学习计划。

## 已知限制

- 单次会话仅覆盖一个学习意图，跨学科综合问题需拆分为多次交互
- CellCog SDK为可选依赖，未安装时部分高级功能受限
- 视觉学习生成的图表为文本描述格式，非真实图片
- 语言学习口语练习需配合TTS工具实现语音输出
- 复杂学科（如高级医学、法学）的准确性需人工验证
- 学习进度跟踪需要用户手动维护

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "个性化学习助手处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "learn-cog"
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
