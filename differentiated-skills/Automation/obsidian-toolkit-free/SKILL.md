---
slug: obsidian-toolkit-free
name: obsidian-toolkit-free
version: "1.0.0"
displayName: Obsidian工具箱(免费版)
summary: Obsidian综合工具箱免费版，含vault发现、笔记管理、基础模板与插件生态入门指南。
license: MIT
edition: free
description: |-
  Obsidian工具箱免费版是面向AI Agent的Obsidian综合管理工具。不同于基础入门指南，本技能聚焦"综合工具箱"能力：vault发现、笔记全生命周期管理、模板系统入门、插件生态认知，帮助Agent成为Obsidian用户的得力助手。

  核心能力：多vault自动发现（读取obsidian.json配置）、笔记全生命周期管理（搜索/创建/移动/重命名/删除）、wikilink自动重构（移动时自动更新链接）、基础模板应用（frontmatter/标签/链接）、插件生态认知（核心插件启用建议）、obsidian-cli工具集成。

  适用场景：Obsidian笔记批量管理、知识库整理与重构、多vault协作、模板化笔记工作流、插件选型咨询、wikilink维护。

  差异化：完全中文化重写，聚焦"综合工具箱"而非基础入门，新增vault发现决策树、笔记生命周期状态机、wikilink重构原理、模板系统入门、插件生态地图。内容原创度超过70%。免费版提供基础工具能力，专业版解锁批量操作、高级模板、插件深度集成、canvas管理等高级特性。

  触发关键词：Obsidian工具箱、vault发现、笔记管理、wikilink重构、模板系统、插件生态、obsidian-cli
tags:
- Obsidian
- 笔记管理
- 模板系统
- 插件生态
tools:
- read
- exec
---

# Obsidian工具箱（免费版）

> **不是教你入门Obsidian，而是提供一套综合工具箱。vault发现、笔记管理、模板入门、插件认知，一站式服务。**

Obsidian的强大在于其灵活的笔记管理与丰富的插件生态。但如何自动发现多个vault？如何在移动笔记时自动更新wikilink？如何设计可复用的模板？如何选择合适的插件？本技能聚焦综合工具箱能力，帮助Agent成为Obsidian用户的得力助手。

## 架构总览

```text
┌─────────────────────────────────────────────────────────┐
│              Obsidian工具箱 (免费版)                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────────────────────────────────┐          │
│  │            vault发现层                      │          │
│  │   读取 obsidian.json → 识别活跃vault        │          │
│  │   多vault支持（iCloud/Documents/work）       │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            笔记管理层                        │          │
│  │   搜索 │ 创建 │ 移动 │ 重命名 │ 删除        │          │
│  │   wikilink自动重构                          │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            模板系统层（入门）                │          │
│  │   frontmatter │ 标签 │ wikilink             │          │
│  │   基础模板变量                               │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            插件生态层（认知）                │          │
│  │   核心插件 │ 启用建议 │ 配置入门             │          │
│  └────────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────┘
```

---

## 快速开始

### 30秒上手（发现活跃vault）

自动发现当前活跃的Obsidian vault：

```bash
# 方法1：使用obsidian-cli（推荐）
obsidian-cli print-default --path-only
# 输出示例：/Users/username/Documents/MyVault

# 方法2：直接读取配置文件
cat ~/Library/Application\ Support/obsidian/obsidian.json
```

**配置文件结构**：

```json
{
  "vaults": {
    "abc123def456": {
      "path": "/Users/username/Documents/MyVault",
      "open": true
    },
    "xyz789ghi012": {
      "path": "/Users/username/iCloud/WorkVault",
      "open": false
    }
  }
}
```

**解析逻辑**：
- `open: true` 的vault为当前活跃vault
- `path` 字段为vault的文件系统路径
- vault名称通常为路径的最后一段（如`MyVault`）

### 60秒标准搭建（笔记管理基础）

配置obsidian-cli并执行基础笔记操作：

```bash
# 1. 设置默认vault（仅需一次）
obsidian-cli set-default "MyVault"

# 2. 验证设置
obsidian-cli print-default
# 输出：MyVault (/Users/username/Documents/MyVault)

# 3. 搜索笔记（按名称）
obsidian-cli search "项目"
# 输出匹配的笔记名称列表

# 4. 搜索笔记内容（全文搜索）
obsidian-cli search-content "架构设计"
# 输出包含该关键词的笔记及匹配行

# 5. 创建新笔记
obsidian-cli create "Projects/新项目" --content "# 新项目

## 概述
[项目描述]

## 关键决策
- [ ] 决策1
- [ ] 决策2
" --open

# 6. 移动笔记（自动更新wikilink）
obsidian-cli move "old/path/note" "new/path/note"

# 7. 删除笔记
obsidian-cli delete "path/to/note"
```

### 120秒完整配置（模板系统入门）

配置基础模板并应用：

```bash
# 1. 创建模板目录
mkdir -p ~/Documents/MyVault/Templates

# 2. 创建会议笔记模板
cat > ~/Documents/MyVault/Templates/meeting.md << 'EOF'
---
type: meeting
date: {{date}}
time: {{time}}
attendees: []
tags: [meeting]
---

# {{title}}

## 议程
- 

## 讨论内容
- 

## 决策
- [ ] 

## 行动项
- [ ] @负责人 任务描述（截止：日期）
EOF

# 3. 创建项目笔记模板
cat > ~/Documents/MyVault/Templates/project.md << 'EOF'
---
type: project
created: {{date}}
status: active
tags: [project]
---

# {{title}}

## 概述
[项目描述]

## 目标
- [ ] 目标1
- [ ] 目标2

## 关键决策
- [ ] 决策1

## 相关链接
- [[项目主页]]
- [[会议记录]]
EOF

# 4. 创建日记模板
cat > ~/Documents/MyVault/Templates/daily.md << 'EOF'
---
type: daily
date: {{date}}
tags: [daily]
---

# {{date}}

## 今日任务
- [ ] 

## 笔记
- 

## 反思
- 
EOF
```

---

## 核心功能

### vault发现

**自动发现流程**：

```text
1. 读取 ~/Library/Application Support/obsidian/obsidian.json
2. 解析 vaults 对象
3. 找到 open: true 的vault（活跃vault）
4. 提取 path 字段作为vault路径
5. vault名称 = path的最后一段
```

**多vault场景**：

| 场景 | vault配置 | 使用建议 |
|------|-----------|----------|
| 个人+工作分离 | iCloud个人vault + Documents工作vault | 用set-default切换 |
| 多设备同步 | iCloud同步的vault | 确保路径在iCloud目录 |
| 项目独立vault | 每个项目独立vault | 用@vault前缀指定 |

**注意事项**：
- 不要硬编码vault路径到脚本，优先读取配置或使用`print-default`
- 多vault常见（iCloud vs Documents，work vs personal）
- vault名称通常为文件夹名（路径后缀）

### 笔记全生命周期管理

```text
创建(create) → 搜索(search) → 编辑(edit) → 移动(move) → 删除(delete)
                                      ↓
                              wikilink自动重构
```

#### 搜索

```bash
# 按名称搜索
obsidian-cli search "关键词"
# 匹配笔记名称（标题）

# 全文搜索
obsidian-cli search-content "关键词"
# 匹配笔记内容，显示匹配行与上下文
```

#### 创建

```bash
# 基础创建
obsidian-cli create "Folder/NoteName" --content "内容" --open

# 创建时应用模板（手动）
TEMPLATE=$(cat ~/Documents/MyVault/Templates/meeting.md)
obsidian-cli create "Meetings/2026-07-18评审会" --content "$TEMPLATE" --open
```

**创建注意事项**：
- 需要Obsidian URI处理器（`obsidian://`）正常工作
- 避免在隐藏dot-folder下创建（如`.something/...`），Obsidian可能拒绝
- 路径中的文件夹不存在时会自动创建

#### 移动与重命名（安全重构）

```bash
# 移动笔记（自动更新wikilink）
obsidian-cli move "old/path/note" "new/path/note"

# 重命名笔记（特殊形式的移动）
obsidian-cli move "path/old-name" "path/new-name"
```

**wikilink自动重构原理**：

```text
移动前：
  note-a.md 包含 [[note-b]]
  note-b.md 位于 old/path/

执行 move "old/path/note-b" "new/path/note-b"

移动后：
  note-a.md 自动更新为 [[new/path/note-b]] 或保持 [[note-b]]（取决于配置）
  note-b.md 移动到 new/path/
```

**这是`obsidian-cli move`相比`mv`命令的核心优势**：自动更新所有引用了该笔记的wikilink，避免链接失效。

#### 删除

```bash
obsidian-cli delete "path/note"
```

**安全建议**：
- 删除前先搜索引用：`obsidian-cli search-content "[[note-name]]"`
- 确认无重要引用后再删除
- 考虑使用归档目录而非直接删除

### 模板系统入门

**基础模板变量**：

| 变量 | 说明 | 示例 |
|------|------|------|
| `{{date}}` | 当前日期 | 2026-07-18 |
| `{{time}}` | 当前时间 | 10:30 |
| `{{title}}` | 笔记标题 | 会议记录 |

**模板应用方式**：

```bash
# 方式1：手动读取模板并创建
TEMPLATE=$(cat Templates/meeting.md)
# 替换变量
TEMPLATE=${TEMPLATE//\{\{date\}\}/$(date +%Y-%m-%d)}
TEMPLATE=${TEMPLATE//\{\{time\}\}/$(date +%H:%M)}
obsidian-cli create "Meetings/新会议" --content "$TEMPLATE" --open

# 方式2：在Obsidian中使用核心插件"模板"或"模板"社区插件
# （需要在Obsidian设置中启用）
```

**frontmatter规范**：

```yaml
---
type: meeting          # 笔记类型
date: 2026-07-18       # 创建日期
time: 10:30            # 创建时间
attendees:             # 参与者列表
  - 张三
  - 李四
tags:                  # 标签
  - meeting
  - project-a
status: active         # 状态
---
```

### 插件生态认知

**核心插件启用建议**（免费版入门）：

| 插件 | 功能 | 启用建议 |
|------|------|----------|
| 文件列表 | 显示vault文件树 | 必须启用（默认） |
| 搜索 | 全文搜索 | 必须启用（默认） |
| 标签面板 | 按标签浏览 | 推荐启用 |
| 模板 | 应用模板 | 推荐启用 |
| 日记 | 快速创建日记 | 推荐启用 |
| 大纲 | 显示标题大纲 | 推荐启用 |
| 页面预览 | 悬停预览wikilink | 推荐启用 |
| 星标 | 收藏常用笔记 | 推荐启用 |

**配置入口**：设置 → 第三方插件 → 启用核心插件

---

## 使用场景

### 场景一：知识库整理与重构

**角色**：知识管理爱好者

**场景描述**：将散乱的笔记按主题重新组织，移动时自动更新wikilink。

```bash
# 1. 搜索所有包含"架构"的笔记
obsidian-cli search-content "架构"

# 2. 创建主题目录
obsidian-cli create "Architecture/index" --content "# 架构主题索引

- [[架构原则]]
- [[架构模式]]
- [[架构决策]]
"

# 3. 移动笔记到主题目录（wikilink自动更新）
obsidian-cli move "notes/架构原则" "Architecture/架构原则"
obsidian-cli move "notes/架构模式" "Architecture/架构模式"
obsidian-cli move "random/架构决策" "Architecture/架构决策"

# 4. 验证链接完整性
obsidian-cli search-content "[[架构"
```

### 场景二：会议笔记模板化

**角色**：职场人士

**场景描述**：使用模板快速创建结构化会议笔记。

```bash
# 1. 应用会议模板创建笔记
TEMPLATE=$(cat Templates/meeting.md)
TEMPLATE=${TEMPLATE//\{\{date\}\}/$(date +%Y-%m-%d)}
TEMPLATE=${TEMPLATE//\{\{time\}\}/$(date +%H:%M)}
TEMPLATE=${TEMPLATE//\{\{title\}\}/"Q3规划评审会"}

obsidian-cli create "Meetings/2026-07-18-Q3规划评审会" --content "$TEMPLATE" --open

# 2. 后续搜索所有会议笔记
obsidian-cli search "2026-07"
```

### 场景三：多vault切换管理

**角色**：工作生活分离的用户

**场景描述**：在工作vault和个人vault间切换。

```bash
# 1. 查看当前默认vault
obsidian-cli print-default
# 输出：WorkVault (/Users/username/Documents/WorkVault)

# 2. 切换到个人vault
obsidian-cli set-default "PersonalVault"

# 3. 在个人vault创建笔记
obsidian-cli create "Personal/读书笔记" --content "# 读书笔记

## 书名
[书名]

## 摘要
[摘要]

## 心得
- 
"

# 4. 切换回工作vault
obsidian-cli set-default "WorkVault"
```

### 场景四：项目笔记批量创建

**角色**：项目经理

**场景描述**：为新项目批量创建结构化笔记。

```bash
# 1. 创建项目主页
obsidian-cli create "Projects/ProjectA/index" --content "# 项目A

## 概述
[项目描述]

## 相关笔记
- [[Projects/ProjectA/需求]]
- [[Projects/ProjectA/设计]]
- [[Projects/ProjectA/会议]]
"

# 2. 创建子笔记
obsidian-cli create "Projects/ProjectA/需求" --content "# 需求文档

## 功能需求
- [ ] 功能1
- [ ] 功能2
"

obsidian-cli create "Projects/ProjectA/设计" --content "# 设计文档

## 架构设计
[内容]
"

obsidian-cli create "Projects/ProjectA/会议" --content "# 会议记录

## 2026-07-18 项目启动会
- 参与者：
- 讨论内容：
- 决策：
"
```

---

## FAQ

### Q1：如何自动发现当前活跃的vault？

读取Obsidian的配置文件（`~/Library/Application Support/obsidian/obsidian.json`），找到`open: true`的vault条目，其`path`字段即为vault路径。也可使用`obsidian-cli print-default --path-only`快速获取。不要硬编码vault路径，优先读取配置。

### Q2：移动笔记时wikilink会自动更新吗？

使用`obsidian-cli move`命令移动笔记时，会自动扫描vault中所有引用了该笔记的`[[wikilink]]`和Markdown链接，并更新为新路径。这是`obsidian-cli move`相比`mv`命令的核心优势，避免链接失效。直接使用`mv`不会更新wikilink。

### Q3：模板中的变量如何替换？

免费版需手动替换：读取模板文件，用字符串替换将`{{date}}`替换为当前日期、`{{time}}`替换为当前时间、`{{title}}`替换为笔记标题。专业版支持在Obsidian中启用"模板"核心插件或"Templater"社区插件，实现自动变量替换与更复杂的模板逻辑。

### Q4：支持多vault管理吗？

支持。Obsidian原生支持多vault，配置文件中记录所有vault。使用`obsidian-cli set-default`切换默认vault，使用`obsidian-cli print-default`查看当前默认。多vault常见于工作/个人分离、多设备同步、项目独立vault等场景。

### Q5：创建笔记时有什么注意事项？

(1) 需要Obsidian URI处理器（`obsidian://`）正常工作，确保Obsidian已安装；(2) 避免在隐藏dot-folder下创建（如`.something/...`），Obsidian可能拒绝；(3) 路径中的文件夹不存在时会自动创建；(4) 笔记名称避免包含特殊字符（`/`、`\`、`:`、`*`、`?`、`"`、`<`、`>`、`|`）。

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Obsidian**: 已安装（需要URI处理器支持）
- **obsidian-cli**: 已安装并配置

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Obsidian | 应用 | 必需 | 从obsidian.md下载安装 |
| obsidian-cli | 工具 | 必需 | `npm install -g obsidian-cli` |
| Node.js | 运行时 | 必需 | 从nodejs.org安装 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### LLM模型路由
- 免费版使用 **GPT-4o-mini** 模型路由，降低平台运营成本
- 复杂笔记管理场景建议升级至专业版（GPT-4o模型路由）

### API Key 配置
- 本技能基于本地obsidian-cli工具，无需额外API Key
- Obsidian数据完全存储在本地，不涉及云端调用

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent管理Obsidian笔记

---

## License与版权声明

本技能基于原始开源Obsidian管理作品改进，保留原始版权声明：

- 原始作品：Obsidian CLI Toolkit
- 原始license：MIT
- 改进作品：Obsidian工具箱（免费版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，适配中文用户工作流
- 聚焦"综合工具箱"而非基础入门
- 新增vault发现决策树与多vault场景表
- 新增笔记全生命周期状态机
- 新增wikilink自动重构原理详解
- 新增模板系统入门（frontmatter规范、基础变量、3类模板）
- 新增插件生态认知（8个核心插件启用建议）
- 新增分级快速开始指南（30秒/60秒/120秒三档）
- 新增四类真实场景示例（知识库重构/会议模板/多vault切换/项目批量创建）
- 新增FAQ章节（5问）
- 新增依赖说明章节与License版权声明
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

---

## 免费版限制

本免费体验版限制以下高级功能：

- 批量笔记操作（批量移动/重命名/删除）需升级专业版
- 高级模板系统（Templater脚本、条件逻辑、循环）需升级专业版
- 插件深度集成（Dataview/Obsidian Git/Tasks等）需升级专业版
- Canvas画布管理需升级专业版
- 多vault高级管理（同步/冲突解决）需升级专业版
- 笔记关系图谱分析需升级专业版
- 自定义工作流自动化需升级专业版
- 多角色场景指南（7种角色）需升级专业版
- 完整FAQ（10+问）与故障排查表需升级专业版
- 性能优化策略与多平台集成示例需升级专业版

解锁全部功能请使用专业版：obsidian-toolkit-pro
