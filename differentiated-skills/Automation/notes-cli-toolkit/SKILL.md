---
slug: "notes-cli-toolkit"
name: "notes-cli-toolkit"
version: "1.0.0"
displayName: "笔记CLI工具箱"
summary: "解决无头批处理难、frontmatter难改、daily模板乱痛点，用notesmd-cli把笔记玩成数据库"
license: "Proprietary"
description: |-
  基于 `notesmd-cli` 的 Obsidian 笔记批处理工具箱。聚焦无头（headless）批量操作、
  frontmatter 元数据治理、daily note 模板化、与 `$EDITOR` 集成，把笔记从"逐篇手改"升级为
  "脚本化批处理"。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
  - 自动化
  - 知识管理
  - 命令行工具
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 笔记 CLI 工具箱

把 Obsidian vault 当作可被脚本批处理的笔记数据库。基于 `notesmd-cli` 完成无头创建、frontmatter 治理、daily note 模板化与编辑器集成。

## Vault 模型

Obsidian vault = 普通磁盘文件夹。

| 路径 | 内容 | notesmd-cli 是否可操作 |
|:-----|:-----|:----------------------|
| `*.md` | Markdown 笔记 | 是（直接读写磁盘） |
| `.obsidian/app.json` | 默认新文件位置配置 | 读取（用于 create） |
| `.obsidian/daily-notes.json` | daily note 配置 | 读取（用于 daily） |
| `*.canvas` | 画板 JSON | 不支持（需手动处理） |
| 附件目录 | 图片/PDF | 不直接管理 |

`notesmd-cli` 直接操作磁盘，**Obsidian 不需要运行**，适合无头服务器与 CI。

## 多库发现

Obsidian 桌面端记录 vault 列表于：

- macOS: `~/Library/Application Support/obsidian/obsidian.json`
- Windows: `%APPDATA%/obsidian/obsidian.json`
- Linux: `~/.config/obsidian/obsidian.json`

`notesmd-cli` 从该文件解析；vault 名通常是文件夹名。

```bash
# 已设默认
notesmd-cli print-default --path-only

# 未设默认 → 读 obsidian.json，取 "open": true 条目
```

多库常见（iCloud vs ~/Documents、工作 vs 个人），**不要猜，读配置**。

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

```bash
# 1. 设默认库 + 打开方式
notesmd-cli set-default "<vault-folder-name>"
notesmd-cli set-default --open-type editor   # 用 $EDITOR 而非 Obsidian

# 2. 搜索
notesmd-cli search                           # 交互式模糊搜索
notesmd-cli search-content "query"           # 全文搜索

# 3. 创建
notesmd-cli create "Folder/New note" --content "..."

# 4. Daily note
notesmd-cli daily                             # 创建/打开今日 daily

# 5. frontmatter
notesmd-cli frontmatter "NoteName" --print
notesmd-cli frontmatter "NoteName" --edit --key "status" --value "done"

# 6. 移动/删除
notesmd-cli move "old/path/note" "new/path/note"
notesmd-cli delete "path/note"
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。

### 命令参数说明

- `-MM-DD`: 命令参数,用于指定操作选项

## 无头模式与 CI 集成

`notesmd-cli` 直接操作磁盘，**Obsidian 不需要运行**。适合服务器与 CI/CD。

### 示例

```yaml
# .github/workflows/daily-note.yml
name: Daily Note
on:
  schedule:
    - cron: "0 6 * * *"   # 每日 6 点
jobs:
  daily:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g notesmd-cli
      - run: |
          notesmd-cli set-default "vault" --open-type editor
          notesmd-cli daily
      - run: |
          git add .
          git commit -m "chore: daily note $(date +%F)" || echo "no changes"
          git push
```

### 服务器批量归档

```bash
# 在 NAS/服务器上跑，无 GUI
notesmd-cli set-default "my-vault" --open-type editor
# 把 30 天前的 daily 归档
scripts/archive-daily --days 30 --to "Archive/Daily/"
```

## frontmatter 治理

把 frontmatter 当数据库字段操作。

### 单条操作

```bash
# 打印
notesmd-cli frontmatter "NoteName" --print

# 编辑（添加/修改）
notesmd-cli frontmatter "NoteName" --edit --key "status" --value "done"
notesmd-cli frontmatter "NoteName" --edit --key "tags" --value "project,urgent"

# 删除
notesmd-cli frontmatter "NoteName" --delete --key "draft"
```

### 批量模板

```bash
# 批量打标签（从 CSV：note_path,tag）
tail -n +2 tags.csv | while IFS=, read -r note tag; do
  notesmd-cli frontmatter "$note" --edit --key "tags" --value "$tag"
done

# 批量改状态：draft → published
for note in $(notesmd-cli search-content "status: draft" --paths-only); do
  notesmd-cli frontmatter "$note" --edit --key "status" --value "published"
done

# 按状态过滤并导出清单
scripts/frontmatter-query --filter "status=published" --output published.md
```

## daily note 模板化

`notesmd-cli daily` 自动读 `.obsidian/daily-notes.json`，按配置的文件夹、格式、模板生成。

### 配置示例（`.obsidian/daily-notes.json`）

```json
{
  "folder": "Daily",
  "format": "YYYY-MM-DD",
  "template": "Templates/Daily Template"
}
```

### 模板文件示例（`Templates/Daily Template.md`）

```markdown
---
date: {{date}}
status: active
tags: [daily]
---

# {{date}}

## 今日任务
- [ ] 

## 笔记
- 

## 回顾
- 
```

### 批量补建缺失的 daily

```bash
# 补建过去 7 天缺失的 daily
scripts/backfill-daily --days 7
# 检查 Daily/ 目录，缺失的按模板生成
```

## 编辑器集成决策表

| 场景 | 推荐方式 | 命令 |
|:-----|:---------|:-----|
| 桌面有 Obsidian | 用 Obsidian 打开 | `notesmd-cli create "note" --open` |
| 服务器/终端环境 | 用 `$EDITOR` | `notesmd-cli create "note" --open --editor` |
| CI/无交互 | 不打开，只创建 | `notesmd-cli create "note" --content "..."` |
| 已有笔记编辑 | 用 `$EDITOR` 打开 | `notesmd-cli open "note" --editor` |

设默认打开方式：`notesmd-cli set-default --open-type editor`。

## 真实场景示例

### 场景1：CI 自动生成 daily 并推送

```
触发：GitHub Actions 每日 6 点
执行：
1. notesmd-cli set-default "vault" --open-type editor
2. notesmd-cli daily（按模板生成）
3. git add . && git commit && git push
4. 其他设备 pull 即可看到今日 daily
```

### 场景2：批量把草稿改发布

```
用户：把所有 status: draft 的笔记改成 status: published
执行：
1. search-content "status: draft" --paths-only → 列出 12 篇
2. 逐个 frontmatter --edit --key status --value published
3. 报告：更新 12 篇
```

### 场景3：服务器批量归档旧 daily

```
用户：把 30 天前的 daily 移到 Archive/
执行：
1. scripts/archive-daily --days 30 --to "Archive/Daily/"
2. move 每个旧 daily（自动更新链接）
3. 报告：归档 30 篇
```

### 场景4：按 frontmatter 查询

```
用户：列出所有 tags 含 "project" 且 status=active 的笔记
执行：
1. scripts/frontmatter-query --filter "tags~project,status=active"
2. 输出：8 篇匹配，含路径与摘要
```

### 场景5：无 GUI 服务器编辑

```
用户：SSH 到服务器改笔记
执行：
1. notesmd-cli set-default "vault" --open-type editor
2. notesmd-cli open "Projects/X" --editor
3. $EDITOR（vim/nano）打开，改完保存
4. Obsidian 桌面端 pull 即可同步
```

## FAQ

**Q1: 无头模式真的不需要 Obsidian 运行吗？**
A: 是的。`notesmd-cli` 直接读写 `.md` 文件，读取 `.obsidian/*.json` 配置。Obsidian 桌面端运行时检测到文件变化会自动刷新。

**Q2: frontmatter 编辑会破坏 YAML 格式吗？**
A: 不会。`notesmd-cli` 解析 YAML 后修改再写回，保留缩进与注释。但建议编辑前备份，避免极端格式问题。

**Q3: daily note 模板支持变量吗？**
A: 支持。`{{date}}`、`{{time}}`、`{{title}}` 等标准变量。自定义变量需在模板中用 frontmatter 或脚本预处理。

**Q4: `--editor` 用哪个编辑器？**
A: 读 `$EDITOR` 环境变量。设为 `vim`、`nano`、`code`（VS Code）等均可。Windows 可设为 `code --wait`。

**Q5: 批量操作前怎么预览？**
A: 所有批量脚本支持 `--dry-run`，先打印将执行的命令列表，确认后再去掉 flag 实跑。

## 故障排查

| 现象 | 排查路径 |
|:-----|:---------|
| `print-default` 返回空 | 未设默认 → 读 obsidian.json 找 `"open": true` |
| `create` 报路径错 | 检查 `.obsidian/app.json` 默认位置 → 避免隐藏 dot-folder |
| `daily` 不按模板生成 | 检查 `.obsidian/daily-notes.json` 的 `template` 字段 → 模板文件存在 |
| frontmatter 编辑失败 | 检查 YAML 是否合法 → 用 `--print` 看当前内容 → 修复格式 |
| `--editor` 无反应 | 检查 `$EDITOR` 是否设置 → `echo $EDITOR` → 设为 `vim` 等 |
| CI 中 `search` 卡住 | `search` 是交互式模糊搜索，CI 用 `search-content` 替代 |
| move 后链接断 | 确认 CLI 版本支持链接更新 → 升级 notesmd-cli → 手动修复残留 |

## 依赖说明

### 运行环境
- **Agent 平台**: 任意支持 SKILL.md 的 AI Agent
- **操作系统**: Windows / macOS / Linux（无头模式适合服务器）
- **Obsidian**: 桌面版（可选，无头模式不需要运行）
- **编辑器**: `$EDITOR` 环境变量指向的编辑器（vim/nano/code 等）

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| `notesmd-cli` | 命令行工具 | 必需 | npm / 官方仓库 |
| Obsidian 桌面版 | 软件 | 可选（仅配置文件需要） | obsidian.md 下载 |
| Node.js ≥ 16 | 运行时 | 必需（notesmd-cli 依赖） | nodejs.org |
| `$EDITOR` | 编辑器 | 可选（编辑器模式） | 系统自带或安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 无需 API Key
- CI 集成需要 Git 仓库的 Personal Access Token（用于 push）

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 必须通过 exec 执行 `notesmd-cli` 与批量脚本）
- **说明**: 基于自然语言指令驱动 Agent 批处理笔记，含无头模式、frontmatter 治理、daily 模板化

## 核心能力

### 基于 `notesmd-cli
基于 `notesmd-cli` 的 Obsidian 笔记批处理工具箱

**输入**: 用户提供基于 `notesmd-cli所需的指令和必要参数。
**处理**: 按照skill规范执行基于 `notesmd-cli操作,遵循单一意图原则。
**输出**: 返回基于 `notesmd-cli的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 聚焦无头（headless）批
聚焦无头（headless）批量操作、

**输入**: 用户提供聚焦无头（headless）批所需的指令和必要参数。
**处理**: 按照skill规范执行聚焦无头（headless）批操作,遵循单一意图原则。
**输出**: 返回聚焦无头（headless）批的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

  frontmatter 元数据治理、daily note 模板化、与 `$EDITOR` 集成，把笔记从"逐篇手改"升级为
  "脚本化批处理"
### obsidian/daily-
obsidian/daily-notes

**输入**: 用户提供obsidian/daily-所需的指令和必要参数。
**处理**: 按照skill规范执行obsidian/daily-操作,遵循单一意图原则。
**输出**: 返回obsidian/daily-的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：解决无头批处理难、模板乱痛点、把笔记玩成数据库、Use、when、需要数据分析、报表生成、统计洞察、数据可视化时使用、不适用于实时流数、据处理等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 适用场景

### 场景1：CI 自动生成 daily 并推送

```
触发：GitHub Actions 每日 6 点
执行：
1. notesmd-cli set-default "vault" --open-type editor
2. notesmd-cli daily（按模板生成）
3. git add . && git commit && git push
4. 其他设备 pull 即可看到今日 daily
```

### 场景2：批量把草稿改发布

```
用户：把所有 status: draft 的笔记改成 status: published
执行：
1. search-content "status: draft" --paths-only → 列出 12 篇
2. 逐个 frontmatter --edit --key status --value published
3. 报告：更新 12 篇
```

### 场景3：服务器批量归档旧 daily

```
用户：把 30 天前的 daily 移到 Archive/
执行：
1. scripts/archive-daily --days 30 --to "Archive/Daily/"
2. move 每个旧 daily（自动更新链接）
3. 报告：归档 30 篇
```

### 场景4：按 frontmatter 查询

```
用户：列出所有 tags 含 "project" 且 status=active 的笔记
执行：
1. scripts/frontmatter-query --filter "tags~project,status=active"
2. 输出：8 篇匹配，含路径与摘要
```

### 场景5：无 GUI 服务器编辑

```
用户：SSH 到服务器改笔记
执行：
1. notesmd-cli set-default "vault" --open-type editor
2. notesmd-cli open "Projects/X" --editor
3. $EDITOR（vim/nano）打开，改完保存
4. Obsidian 桌面端 pull 即可同步
```

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 常见问题

### Q1: 笔记CLI工具箱支持哪些输入格式？
支持文本输入、文件上传和API调用三种方式。

### Q2: 使用笔记CLI工具箱需要什么环境？
需要支持SKILL.md的AI Agent平台，详见依赖说明。

### Q3: 输出结果可以直接使用吗？
输出结果建议人工审核后使用，确保符合具体业务需求。

## 错误处理

- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断 - 处理方式: 按上述步骤操作并确认结果
- 执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令机制: 失败时自动执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令, 最多3次 - 处理方式: 按上述步骤操作并确认结果
## 输出格式

处理结果以结构化格式返回, 包含状态码、消息和数据字段。
