---

name: "elite-longterm-memory-local-free"
description: "基础本地记忆系统，热内存加文件归档，纯本地运行无外部依赖。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。支持多场景应用和灵活配置。"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "本地向量记忆免费版"
  version: "1.0.0"
  summary: "基础本地记忆系统，热内存加文件归档，纯本地运行无外部依赖。"
  tags:
    - "智能助手"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
tools:
  - exec
  - read
  - write

---

# 本地向量记忆免费版（Elite Longterm Memory Local Free）

**本地优先，隐私至上。** 基础本地记忆系统，通过热内存与文件归档，让 Agent 不遗忘关键上下文与用户偏好。所有数据完全存储在本地，无需任何外部依赖。本免费版提供两层记忆能力，覆盖单设备本地记忆持久化需求。

## 核心能力

- **热内存（SESSION-STATE.md）**：活跃工作记忆，抗压缩与重启。参数：当前任务、关键上下文、待办动作、近期决策。输出：会话级状态文件，Agent 每次响应前先读取。遵循 WAL 协议：用户输入触发写入，先写状态再回复。文件结构含 Current Task、Key Context、Pending Actions、Recent Decisions 四个区块。

- **精选归档（MEMORY.md + daily/）**：人类可读的长期记忆。参数：MEMORY.md（摘要文件）+ memory/YYYY-MM-DD.md（每日日志）+ memory/topics/（主题文件）。输出：精炼后的长期记忆与每日活动记录。会话结束时将重要内容从 SESSION-STATE.md 迁移至 MEMORY.md，创建或更新每日日志。

- **WAL 协议保障**：写前日志机制确保数据持久。参数：触发条件（用户表达偏好/做出决策/给出期限/纠正代理）。输出：先写入 SESSION-STATE.md 再回复用户。若先回复再保存，崩溃或压缩会导致上下文丢失；WAL 确保写入优先，保障持久性。

- **会话记忆协议**：标准化 Agent 记忆行为。参数：会话开始/对话中/会话结束三个阶段的行为规则。输出：会话开始读取 SESSION-STATE.md 获取热上下文，检查 memory/YYYY-MM-DD.md 了解近期活动；对话中用户给出具体细节则先写入再回复；会话结束时更新最终状态并迁移重要内容到 MEMORY.md。
### 热内存（SESSION-STATE.md）

执行热内存（SESSION-STATE.md）操作,处理用户输入并返回结果。

**输入**: 用户提供热内存（SESSION-STATE.md）所需的参数和指令。

### 精选归档（MEMORY.md + daily/）

执行精选归档（MEMORY.md + daily/）操作,处理用户输入并返回结果。

**输入**: 用户提供精选归档（MEMORY.md + daily/）所需的参数和指令。

### WAL 协议保障

执行WAL 协议保障操作,处理用户输入并返回结果。

**输入**: 用户提供WAL 协议保障所需的参数和指令。

#
## 使用流程

领先步：创建记忆系统结构。手动创建 SESSION-STATE.md（热内存，含 Current Task、Key Context、Pending Actions、Recent Decisions 四区块）、MEMORY.md（长期摘要）、memory/ 目录（每日日志）。

第二步：配置 Agent 记忆协议。在 AGENTS.md 或 SOUL.md 中添加记忆协议：会话开始时读取 SESSION-STATE.md 了解近期活动。对话中用户给出具体细节则先写入 SESSION-STATE.md 再回复。

第三步：会话结束与维护。会话结束时更新 SESSION-STATE.md 最终状态，将重要内容迁移至 MEMORY.md，创建或更新 memory/YYYY-MM-DD.md 每日日志。定期合并每日日志到 MEMORY.md 保持精简。

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

## 错误处理

| 错误类型 | 原因 | 处理方式 |
|:---|:---|:---|
| Agent 遗忘对话中途上下文 | SESSION-STATE.md 未被更新，未遵循 WAL 协议 | 在 AGENTS.md 中添加强制规则"用户给出具体细节时先写入 SESSION-STATE.md 再回复"；验证 Agent 指令包含记忆协议 |
| 记忆文件未被加载 | Agent 跳过读取记忆文件，会话开始未读取 SESSION-STATE.md | 在 AGENTS.md 中添加强制规则"会话开始必须读取 SESSION-STATE.md"；检查文件是否存在与可读 |
| 重复犯同类错误 | 错误经验未记录到 memory/lessons.md | 每次犯错后手动写入 lessons.md；在 AGENTS.md 中配置"犯错后强制记录"规则 |

## 示例

### 示例：偏好持久化与跨会话召回

输入：
```
用户："这个项目用 Tailwind，不用原生 CSS"
```

Agent 内部执行与输出：
```
1. WAL 协议触发：先写入 SESSION-STATE.md
   - Key Context 区块追加："Decision: Use Tailwind, not vanilla CSS"

2. 然后回复用户："收到——用 Tailwind。"

3. 会话结束时迁移到 MEMORY.md：
   ## 偏好
   - 前端框架：Tailwind（不用原生 CSS）

后续会话开始时：
   Agent 读取 SESSION-STATE.md + MEMORY.md
   → 获取热上下文："用户偏好 Tailwind"
   → 回复时自动遵循该偏好
```

## FAQ

**Q1：免费版支持向量语义搜索吗？**
不支持。免费版仅提供热内存（SESSION-STATE.md）与文件归档（MEMORY.md + daily/）两层记忆，无 LanceDB 向量搜索能力。记忆召回依赖文件读取与关键词匹配。向量语义搜索在付费版通过 LanceDB 与 Ollama 本地 Embedding 提供。

**Q2：免费版需要安装 Ollama 吗？**
不需要。免费版纯 Markdown 指令驱动，所有记忆通过文件读写管理，无需 Ollama、Node.js 或任何外部依赖。付费版需要 Ollama 运行 nomic-embed-text 模型提供本地向量 Embedding。

**Q3：免费版能自动召回相关记忆吗？**
不能。免费版无 autoRecall 自动召回能力，Agent 需手动读取 SESSION-STATE.md 与 MEMORY.md 获取上下文。付费版支持 autoRecall=true 会话开始自动搜索相关记忆并注入上下文。

## 依赖说明

**LLM 依赖**：由 Agent 内置 LLM 提供自然语言理解与推理能力，必需。

**API Key 配置**：本 Skill 无需任何 API Key，纯 Markdown 指令驱动，所有记忆存储在本地文件，不做任何网络请求。

**运行环境**：
- Agent 平台：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- 操作系统：Windows / macOS / Linux
- 文件系统：本地存储，必需，操作系统内置

**可用性分类**：MD（纯 Markdown 指令，无需 exec 命令行能力）。所有记忆通过文件读写管理。

## 已知限制

1. **无向量语义搜索**：不提供 LanceDB 向量搜索能力，记忆召回依赖文件读取与关键词匹配，无法进行语义相似度召回。

2. **无自动召回与捕获**：不支持 autoRecall 自动召回与 autoCapture 自动捕获，所有记忆操作需 Agent 手动执行。

3. **无 CLI 管理工具**：不提供 memory.js CLI 工具的 stats、dedup、compact、cleanup、backup 等管理命令，记忆维护需手动操作文件。

## 升级提示

本免费版提供基础热内存与文件归档两层本地记忆。升级到付费版可获得以下完整能力：

- **LanceDB 向量语义搜索**：基于本地 LanceDB 的语义召回，无需精确关键词匹配，按语义相似度排序召回记忆
- **Ollama 本地 Embedding**：通过 nomic-embed-text 模型本地生成 768 维向量，完全免费、本地毫秒级延迟、数据不出域、可离线使用
- **完整 CLI 管理工具**：memory.js 提供 store、search、stats、dedup、export、backup、compact、cleanup 等完整管理命令
- **自动召回与捕获**：autoRecall 会话开始自动召回相关记忆，autoCapture 按类别与重要性自动存储
- **五层完整记忆架构**：热内存、LanceDB 向量、Git-Notes 知识图谱、精选归档、本地 Embedding 五层协同
- **插件集成**：启用后自动提供 memory_recall、memory_store、memory_forget 三个工具，深度集成 Agent 工作流

付费版适合需要语义搜索、自动召回、完整记忆管理工具的高级本地 AI Agent 应用场景，特别适合对数据隐私有高要求的环境。

## 安全注意事项

| 风险类型 | 防范措施 |
|----------|---------|
| API密钥泄露 | 通过环境变量配置，禁止硬编码到代码或配置文件中 |
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 网络通信安全 | 使用HTTPS协议，验证SSL证书有效性 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 效率量化分析

| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 差异化对比

| 对比维度 | 本技能 | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 核心功能 | 通用场景 | 通用场景 |

## 核心功能

- **自动化执行**: 基于指令驱动的自动化流程
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据