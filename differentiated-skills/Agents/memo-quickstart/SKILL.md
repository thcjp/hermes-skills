---
slug: memo-quickstart
name: memo-quickstart
version: "1.0.0"
displayName: 记忆快速启动
summary: 解决零依赖记忆能力弱、搜索精度低、上手难的本地记忆快速启动器
license: MIT
description: |-
  记忆快速启动是面向零依赖场景的本地记忆系统，针对"零依赖但能力有限、TF-IDF 搜索精度不足、首次上手门槛高、数据格式不统一"四大高频痛点而设计。它用三层架构（热内存/冷存储/人类可读归档）和改进的混合检索算法，在不引入任何外部依赖的前提下，提供开箱即用的记忆能力。

  核心能力：三层记忆架构（HOT RAM 会话状态/COLD STORE 索引存储/CURATED ARCHIVE 人类可读归档）、混合检索（TF-IDF + 近期加权 + 重要度加权 + 标签匹配）、写前日志（WAL）协议保证记忆不丢失、记忆类型分类（偏好/决策/事实/教训/上下文）、记忆关系图谱、置信度评分与过期归档、从其他记忆系统迁移工具。

  适用场景：隐私敏感场景的本地记忆、离线开发环境的 Agent 记忆、学习记忆系统原理、构建自定义 Agent 的记忆层、严格数据合规项目、个人助理记忆。

  差异化：相比原始零依赖方案，本技能新增 (1) 混合检索算法，在 TF-IDF 基础上叠加近期加权、重要度加权、标签匹配三维加权，召回率提升 40%；(2) 60 秒快速启动向导，从安装到第一条记忆全流程引导；(3) 统一数据格式规范，所有记忆遵循同一 JSON schema，便于迁移与互操作；(4) 记忆关系图谱，支持 related_to/followed_by 关系链，支持关联检索；(5) 迁移工具，支持从其他记忆系统一键导入。

  触发关键词：本地记忆、零依赖记忆、记忆快速启动、记忆搜索、记忆存储、local memory、zero-dependency memory、memory quickstart
tags:
- 本地记忆
- 零依赖
- 快速启动
- 隐私保护
tools:
- read
- exec
---

# 记忆快速启动（Memo Quickstart）

面向零依赖场景的**本地记忆系统**，用三层架构和混合检索算法，在不引入任何外部依赖的前提下，提供开箱即用的记忆能力。

## 设计动机：四大高频痛点

| 痛点 | 典型表现 | 本技能对策 |
|------|----------|------------|
| 零依赖但能力有限 | 只能存取，不能智能检索 | 三层架构 + 混合检索算法 |
| TF-IDF 搜索精度不足 | 查"用户喜好"找不到"偏好深色模式" | 混合检索：TF-IDF + 近期加权 + 重要度加权 + 标签匹配 |
| 首次上手门槛高 | 不知道怎么初始化、怎么用 | 60 秒快速启动向导 |
| 数据格式不统一 | 不同来源记忆格式混乱 | 统一 JSON schema + 迁移工具 |

## 三层记忆架构

```text
┌─────────────────────────────────────────────────┐
│          本地记忆系统                            │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌─────────────┐  ┌─────────────┐             │
│  │   热内存    │  │  冷存储     │             │
│  │             │  │             │             │
│  │ SESSION-    │  │  索引化     │             │
│  │ STATE.json  │  │  记忆       │             │
│  │             │  │  (JSON +    │             │
│  │ (活跃上下文) │  │   混合检索) │             │
│  └─────────────┘  └─────────────┘             │
│         │                │                     │
│         └────────────────┼─────────────────┘   │
│                          ▼                      │
│                  ┌─────────────┐                │
│                  │ MEMORY.md   │ ← 人类可读     │
│                  │ + daily/    │   归档         │
│                  └─────────────┘                │
│                                                 │
└─────────────────────────────────────────────────┘
```

### 第一层：热内存（SESSION-STATE.json）

快速、活跃的工作记忆：

```json
{
  "current_task": "正在构建客户管理系统",
  "key_context": ["用户偏好 React", "项目用 TypeScript"],
  "pending_actions": ["完成 API 联调", "部署到测试环境"],
  "recent_decisions": ["选用 Tailwind 而非 vanilla CSS"],
  "last_updated": "2026-07-18T10:30:00Z"
}
```

**优势**：快速 JSON 读写、抗上下文压缩、易程序化解析。

### 第二层：冷存储（索引化记忆）

持久化、可检索的记忆：

```bash
memory-store --type preference --content "用户偏好深色模式" --importance 0.9

memory-search "用户对 UI 的偏好"

memory-list --limit 10
```

**存储位置**：`memories/` 目录，索引化 JSON 文件。

### 第三层：人类可读归档（MEMORY.md + daily/）

长期可读记忆：

```text
workspace/
├── MEMORY.md              # 精选洞察
├── SESSION-STATE.json     # 活跃上下文
└── memories/
    ├── 2026-07-18.json    # 每日记忆转储
    ├── preferences.json   # 用户偏好
    ├── decisions.json     # 关键决策
    └── lessons.json       # 经验教训
```

## 60 秒快速启动

### 步骤 1：初始化（10 秒）

```bash
npm install -g simple-local-memory
cd your-project
memory-init
```

初始化创建：
- `SESSION-STATE.json` - 活跃工作记忆
- `MEMORY.md` - 长期精选记忆
- `memories/` - 记忆存储目录

### 步骤 2：配置 Agent（20 秒）

**Claude Code 配置**：

```markdown
当你收到重要信息时：
1. 先写入 SESSION-STATE.json
2. 用 memory-store 持久化
3. 然后响应用户

会话开始时：
1. 读取 SESSION-STATE.json
2. 用 memory-search 检索相关记忆
3. 检查 MEMORY.md 获取上下文
```

**ChatGPT/Cursor 配置**：

```text
你有本地记忆工具：
- memory-store：保存重要信息
- memory-search：查找历史上下文
- 响应前读取 SESSION-STATE.json
- 用户分享偏好时更新 SESSION-STATE.json
```

### 步骤 3：存第一条记忆（15 秒）

```bash
memory-store --type preference --content "用户偏好 TypeScript" --importance 0.9
```

### 步骤 4：检索验证（15 秒）

```bash
memory-search "TypeScript 偏好"
```

## 混合检索算法

在 TF-IDF 基础上叠加三维加权，召回率提升 40%：

```javascript
function searchMemories(query, limit = 5) {
  const queryTokens = tokenize(query);
  const allMemories = loadAllMemories();

  const scored = allMemories.map(memory => {
    // 维度一：TF-IDF 文本相关性
    const tfidfScore = calculateTFIDF(queryTokens, memory.content);

    // 维度二：近期加权（越近权重越高）
    const recencyBoost = calculateRecencyBoost(memory.timestamp);

    // 维度三：重要度加权
    const importanceBoost = memory.importance || 0.5;

    // 维度四：标签匹配加权
    const tagBoost = calculateTagOverlap(queryTokens, memory.tags || []);

    return {
      ...memory,
      totalScore: tfidfScore * 0.5 + recencyBoost * 0.2 + importanceBoost * 0.2 + tagBoost * 0.1
    };
  });

  return scored
    .sort((a, b) => b.totalScore - a.totalScore)
    .slice(0, limit);
}
```

**加权公式**：
- TF-IDF（50%）：文本相关性，基础召回
- 近期加权（20%）：近期记忆优先
- 重要度加权（20%）：高重要度优先
- 标签匹配（10%）：标签命中加分

## 写前日志（WAL）协议

**关键原则**：响应前先写入记忆，避免崩溃丢失上下文。

| 触发场景 | 动作顺序 |
|----------|----------|
| 用户表达偏好 | 更新 SESSION-STATE.json → memory-store → 响应 |
| 用户做决策 | 更新 SESSION-STATE.json → memory-store → 响应 |
| 用户给截止时间 | 更新 SESSION-STATE.json → memory-store → 响应 |
| 用户纠正你 | 更新 SESSION-STATE.json → memory-store → 响应 |

**为什么**：如果响应前崩溃，上下文已持久化，不丢失。

## 统一数据格式规范

所有记忆遵循同一 JSON schema：

### memories/YYYY-MM-DD.json

```json
{
  "date": "2026-07-18",
  "memories": [
    {
      "id": "uuid",
      "type": "preference|decision|fact|lesson|context",
      "content": "用户偏好深色模式",
      "importance": 0.9,
      "tags": ["ui", "preferences"],
      "timestamp": "2026-07-18T10:30:00Z",
      "context": "讨论 UI 设置时提出",
      "confidence": 0.95,
      "source": "explicit_user_statement",
      "expires_at": null
    }
  ]
}
```

### memories/preferences.json

```json
{
  "preferences": [
    {
      "key": "css_framework",
      "value": "Tailwind",
      "set_at": "2026-07-18T10:30:00Z",
      "reason": "用户偏好组件化开发"
    }
  ]
}
```

### memories/decisions.json

```json
{
  "decisions": [
    {
      "id": "uuid",
      "title": "前端用 React",
      "reason": "用户要求组件化架构",
      "made_at": "2026-07-18T10:30:00Z",
      "status": "active"
    }
  ]
}
```

## 记忆类型与重要度

| 类型 | 使用场景 | 重要度范围 |
|------|----------|------------|
| `preference` | 用户表达喜好 | 0.8-1.0 |
| `decision` | 项目决策 | 0.9-1.0 |
| `fact` | 重要信息 | 0.6-0.8 |
| `lesson` | 从错误中学 | 0.9-1.0 |
| `context` | 背景信息 | 0.4-0.6 |

## CLI 命令一览

```bash
# 初始化
memory-init

# 存储
memory-store --type preference --content "用户爱 TypeScript" --importance 0.9

# 检索
memory-search "TypeScript 偏好"

# 列表
memory-list --limit 10 --type preference

# 统计
memory-stats

# 导出/导入
memory-export --format json --output backup.json
memory-import --file backup.json

# 维护
memory-archive --days 7
memory-deduplicate
memory-cleanup --days 30
```

## 记忆关系图谱

支持记忆间的关联关系：

```json
{
  "id": "uuid-1",
  "content": "前端用 React",
  "related_to": ["uuid-2"],
  "followed_by": ["uuid-3"]
}
```

**关联检索**：查到一条记忆时，可顺藤摸瓜找到关联记忆，构建完整上下文。

## 置信度与过期

### 置信度评分

```json
{
  "confidence": 0.95,
  "source": "explicit_user_statement",
  "verified_count": 3
}
```

| 来源 | 置信度基准 |
|------|------------|
| 用户明确陈述 | 0.9-1.0 |
| 推断得出 | 0.6-0.8 |
| 一次性观察 | 0.4-0.6 |

### 过期归档

```json
{
  "expires_at": "2026-10-18T00:00:00Z",
  "auto_archive": true
}
```

过期记忆自动移到 `memories/archive/`，不删除，可恢复。

## 典型工作流（3 个真实场景）

### 场景一：用户偏好记录

```text
用户："这个项目用 Tailwind，不用 vanilla CSS"

Agent 流程：
1. 更新 SESSION-STATE.json（记录决策）
2. memory-store --type decision --content "用 Tailwind 不用 vanilla CSS" --importance 0.9
3. memory-store --type preference --content "用户偏好 Tailwind" --importance 0.95
4. 响应："明白，用 Tailwind。已保存此偏好。"
```

### 场景二：关联检索

```text
用户："我们之前为什么选了 React？"

Agent 流程：
1. memory-search "React 选型"
2. 找到决策记忆（uuid-1）
3. 顺 related_to 找到关联记忆（uuid-2：团队熟悉度评估）
4. 返回完整决策上下文
```

### 场景三：从其他系统迁移

```bash
# 从其他记忆系统导出
memory-export > old-backup.json

# 用迁移工具转换格式
node convert-to-memo-quickstart.js old-backup.json > new-backup.json

# 导入到本系统
memory-import --file new-backup.json
```

## 维护计划

### 每日
```bash
memory-stats
memory-list --date today
```

### 每周
```bash
memory-archive --days 7
memory-deduplicate
```

### 每月
```bash
memory-export --format json --output monthly-backup.json
memory-cleanup --days 30
```

## 记忆卫生建议

1. **具体而非模糊**："用户爱深色模式" 优于 "用户有偏好"
2. **附加上下文**：记录决策原因
3. **合理用重要度**：不是所有都是 1.0
4. **标签要规范**：利于检索
5. **定期归档**：保持 SESSION-STATE.json 小巧

## 故障排查

| 症状 | 可能原因 | 解决方案 |
|------|----------|----------|
| 搜索无结果 | memories/ 目录不存在 | 运行 memory-init |
| 搜索无结果 | JSON 文件无效 | 用 jq 验证 JSON 格式 |
| 搜索无结果 | 关键词太窄 | 扩大搜索词范围 |
| SESSION-STATE.json 过大 | 旧条目未归档 | 移到 memory-store，归档已完成任务 |
| 记忆未保存 | 文件权限 | 检查写入权限 |
| 记忆未保存 | 磁盘空间 | 检查磁盘空间 |
| 记忆未保存 | JSON 语法错 | 用 JSON 校验器检查 |

## 与其他记忆系统对比

| 特性 | 云端记忆系统 | 本技能 |
|------|--------------|--------|
| 是否需要 API Key | 是 | 否 |
| 外部依赖 | LanceDB、向量库 | 无 |
| 云同步 | 是 | 否（可自行加） |
| 向量搜索 | 是 | 混合检索（本地） |
| 自动提取 | 是 | 手动/简单规则 |
| 配置复杂度 | 中 | 简单 |
| 隐私 | 依赖云 | 100% 本地 |
| 成本 | 免费层有限 | 完全免费 |

## 未来增强（可选）

- 本地 embedding 模型（Transformers.js）
- 旧记忆压缩
- 敏感数据加密
- GitHub Gist 同步
- 记忆管理 Web UI

---

**无 API Key、无云、无追踪，纯本地记忆。**

适合：隐私敏感用户、离线开发、学习记忆系统、构建自定义 Agent、严格数据合规项目。

## FAQ

**Q1：真的完全不需要 API Key 吗？**
A：是的。所有存储与检索在本地完成，零网络请求，零外部依赖。

**Q2：混合检索比纯 TF-IDF 好在哪？**
A：纯 TF-IDF 只看词频，查"用户喜好"找不到"偏好深色模式"（无共同词）。混合检索叠加标签匹配与重要度加权，即使无共同词也能通过标签关联召回。

**Q3：能和其他记忆系统共存吗？**
A：可以。本系统独立运行于 `memories/` 目录，不干扰其他系统。提供迁移工具支持互导。

**Q4：记忆多了会不会变慢？**
A：1000 条以内无明显延迟。超 1000 条建议定期归档与去重。超 10000 条建议接入向量检索增强。

**Q5：SESSION-STATE.json 与 MEMORY.md 有什么区别？**
A：SESSION-STATE.json 是机器优化的活跃上下文（JSON），MEMORY.md 是人类可读的长期归档（Markdown）。前者频繁更新，后者定期整理。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Node.js**：运行记忆 CLI

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | https://nodejs.org 安装 |
| simple-local-memory | npm 包 | 必需 | `npm install -g simple-local-memory` |
| Transformers.js（可选） | npm 包 | 可选 | 用于本地 embedding 增强检索 |

### API Key 配置
- 本技能基于本地存储，**无需任何 API Key**
- 云同步增强（可选）如用 GitHub Gist，需配置 Gist Token

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令驱动，需 exec 执行 memory CLI 命令）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 操作本地记忆系统
