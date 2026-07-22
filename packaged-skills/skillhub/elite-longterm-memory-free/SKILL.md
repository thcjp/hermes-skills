---
slug: "elite-longterm-memory-free"
name: "elite-longterm-memory-free"
version: "1.0.0"
displayName: "精英长期记忆免费版"
summary: "基础 AI Agent 记忆系统，热内存加文件归档，抗压缩不丢上下文。"
license: "MIT"
description: |-
  面向 AI Agent 的基础长期记忆系统，提供热内存与文件归档两层记忆能力。
  热内存（SESSION-STATE.md）抗压缩与重启，通过 WAL 协议确保先写状态再回复。
  精选归档（MEMORY.md + daily/）提供人类可读的长期记忆与每日日志。
  适用于 AI 编程助手、智能对话等需要跨会话记忆的基础场景。
  本免费版覆盖单设备记忆持久化需求，帮助 Agent 不遗忘关键上下文与用户偏好。
  不适用于需要向量语义搜索、跨设备同步或自动事实抽取的高级场景。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 智能助手
---
# 精英长期记忆免费版（Elite Longterm Memory Free）

**AI Agent 的基础记忆系统。** 通过热内存与文件归档，让 Agent 不遗忘关键上下文与用户偏好。本免费版提供两层记忆能力，覆盖单设备记忆持久化需求。

## 核心能力

### 1. 热内存（SESSION-STATE.md）

活跃工作记忆，抗压缩与重启。参数：当前任务、关键上下文、待办动作、近期决策。输出：会话级状态文件，Agent 每次响应前先读取。遵循 WAL 协议：用户输入触发写入，先写状态再回复。文件结构含 Current Task、Key Context、Pending Actions、Recent Decisions 四个区块。- 验证执行结果，确认输出符合预期格式
- 参考`热内存（SESSION-STATE.md）`相关配置参数进行设置
### 2. 精选归档（MEMORY.md + daily/）

人类可读的长期记忆。参数：workspace 目录结构，MEMORY.md（摘要文件）+ memory/YYYY-MM-DD.md（每日日志）。输出：精炼后的长期记忆与每日活动记录。会话结束时将重要内容从 SESSION-STATE.md 迁移至 MEMORY.md，创建或更新每日日志。- 验证执行结果，确认输出符合预期格式
- 参考`精选归档（MEMORY.md + daily/）`相关配置参数进行设置
### 3. WAL 协议保障

写前日志机制确保数据持久。参数：触发条件（用户表达偏好/做出决策/给出期限/纠正代理）。输出：先写入 SESSION-STATE.md 再回复用户。若先回复再保存，崩溃或压缩会导致上下文丢失；WAL 确保写入优先，保障持久性。- 验证执行结果，确认输出符合预期格式
- 参考`WAL 协议保障`相关配置参数进行设置
### 4. 记忆检索与关联
通过语义搜索检索历史记忆,支持时间范围、关键词和关联实体过滤。自动建立记忆间的关联关系,形成知识网络。

**输入**: 用户提供记忆检索与关联所需的指令和必要参数。
**输出**: 返回记忆检索与关联的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`记忆检索与关联`相关配置参数进行设置
#
## 使用流程

第一步：创建热内存文件。执行 `cat > SESSION-STATE.md` 创建包含 Current Task、Key Context、Pending Actions、Recent Decisions 四区块的状态文件。这是 Agent 的"RAM"，抗压缩、抗重启。

第二步：配置 Agent 指令。在 AGENTS.md 中添加记忆协议：会话开始时读取 SESSION-STATE.md 获取热上下文，检查 memory/YYYY-MM-DD.md 了解近期活动。对话中用户给出具体细节则先写入 SESSION-STATE.md 再回复。

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
不支持。免费版仅提供热内存（SESSION-STATE.md）与文件归档（MEMORY.md + daily/）两层记忆，无 LanceDB 向量搜索能力。记忆召回依赖文件读取与关键词匹配。向量语义搜索在付费版提供。

**Q2：免费版能跨设备同步记忆吗？**
不能。免费版仅支持单设备本地记忆，无云备份与跨设备同步能力。所有记忆存储在本地文件系统中。跨设备同步在付费版通过云备份层提供。

**Q3：免费版如何处理记忆膨胀？**
通过定期维护：SESSION-STATE.md 保持精简（仅当前任务上下文）；MEMORY.md 控制在合理大小，详细内容链接到 memory/topics/ 下的主题文件；每日日志定期合并到 MEMORY.md。付费版提供向量数据库 compact 压缩与自动记忆卫生。

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

2. **无跨设备同步**：仅支持单设备本地记忆，无云备份能力，多设备协作场景无法使用。

3. **无自动事实抽取**：不集成 Mem0 自动抽取，所有记忆需 Agent 手动存储，无法从对话中自动提取偏好与决策。

## 升级提示

本免费版提供基础热内存与文件归档两层记忆。升级到付费版可获得以下完整能力：

- **六层完整记忆架构**：新增 LanceDB 向量语义搜索（温存储）、Git-Notes 知识图谱（冷存储）、云备份（跨设备同步）、Mem0 自动事实抽取
- **向量语义搜索**：memory_recall 与 memory_store 工具，按相关度排序召回记忆，支持 autoRecall 自动注入
- **知识图谱冷存储**：结构化决策与学习记录，分支隔离，永久保存
- **云备份与跨设备同步**：SuperMemory API 支持跨设备记忆同步与知识库对话
- **自动事实抽取**：Mem0 集成，从对话中自动提取偏好、决策、事实，节省 80% token
- **完整 WAL 协议**：写前日志保障数据持久，避免崩溃或压缩导致上下文丢失

付费版适合需要语义搜索、跨设备同步、自动事实抽取的高级 AI Agent 应用场景。
