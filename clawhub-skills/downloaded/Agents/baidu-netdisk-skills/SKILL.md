---
slug: baidu-netdisk-skills
name: baidu-netdisk-skills
version: "1.1.5"
displayName: 百度网盘
summary: 百度网盘(Baidu Drive)文件管理。
license: MIT
description: |-
  百度网盘(Baidu Drive)文件管理。核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Agents
tools:
  - - read
- exec
---

# 百度网盘

百度网盘文件管理工具，所有操作限制在 `/apps/bdpan/` 目录内。适配 Claude Code、DuClaw、Skill平台 等。

> 使用注意事项详见 [reference/notes.md](/api/v1/skills/baidu-netdisk-skills/file?path=reference%2Fnotes.md&ownerHandle=wscats)

## 触发规则

### 网盘文件操作触发

同时满足以下条件才执行：

1. 用户消息中包含**明确指向百度网盘**的关键词，至少匹配以下之一：
   * `百度网盘`、`百度云盘`、`bdpan`、`baidu netdisk`、`baidu pan`、`baidu drive`、`pan.baidu.com`
2. 操作意图明确（上传/下载/转存/分享/查看/搜索/移动/复制/重命名/创建文件夹/删除/登录/注销）
3. 对于**写操作**（上传、删除、移动、覆盖式下载、公开分享），即使触发词命中，也必须先列出"将要执行的操作 + 影响范围"并取得用户显式确认（`y`）后再执行

**不要触发的情况：**

* 用户仅说"网盘""云盘""云存储""百度云"等泛指或可能指向其他百度产品的词，未明确指向百度网盘 → 应反问"您指的是百度网盘（pan.baidu.com）吗？"再决定
* 用户在讨论其他云盘服务（OneDrive、Google Drive、阿里云盘、夸克网盘等）
* 仅复述、引用或摘要历史聊天记录中的网盘内容，而无新的操作意图

未通过触发规则时，禁止执行任何 bdpan 命令。

> **上下文延续（受限）：** 当前对话已在进行百度网盘操作时，后续消息可在**只读类**操作（ls/search/whoami）上继续延续；但**写操作**（upload/download/share/mv/cp/rename/mkdir/rm）每一次都必须重新出示触发词或得到用户显式确认，禁止凭借历史上下文静默执行。

### 记忆备份/恢复触发

**以下表达即使未提及"网盘"也应触发（仅限 kimiclaw/maxclaw/qclaw/skill-platform 环境）：**

| 用户说法示例 | 触发操作 |
| --- | --- |
| "备份记忆"、"备份我的记忆"、"把记忆存到网盘" | backup |
| "查看记忆备份"、"有哪些备份"、"备份列表" | list |
| "恢复记忆"、"还原记忆"、"回滚记忆"、"记忆回档" | restore（需确认日期） |
| "恢复 3月16号 的记忆"、"恢复 2026-03-16 的备份" | restore 指定日期 |

**以下情况不触发记忆备份/恢复：**

* "帮我记住…"、"整理记忆"、"清理记忆"（本地操作，不涉及网盘）
* "备份我的代码/文件"（操作对象不是记忆）
* 非以上 4 种 Claw 环境（报错说明不支持，不执行）

**区分原则：** 操作对象是否为 Agent 记忆文件（AGENTS.md、SOUL.md、MEMORY.md、memory/*.md 等）。

---

## 已知限制

1. **登录**：必须使用 `bash ${CLAUDE_SKILL_DIR}/scripts/login.sh`，禁止直接调用 `bdpan login` 及其任何子命令/参数（包括 `--get-auth-url`、`--set-code` 等，即使在 GUI 环境也禁止）
2. **Token/配置**：禁止读取或输出 `~/.config/bdpan/config.json` 内容（含 access_token 等敏感凭据）
3. **更新/登录**：更新必须由用户明确指令触发，禁止自动或静默执行；Agent 禁止使用 `--yes` 参数执行 update.sh 或 login.sh
4. **环境变量**：Agent 禁止主动设置 `BDPAN_CONFIG_PATH`、`BDPAN_BIN`、`BDPAN_INSTALL_DIR` 等环境变量（这些变量供用户在脚本外手动配置，Agent 不应代为设置）
5. **路径安全**：禁止路径穿越（`..`、`~`）、禁止访问 `/apps/bdpan/` 范围外的绝对路径
6. **记忆备份约束**：禁止直接用裸 `bdpan upload/download` 命令操作记忆目录；必须通过 `bash ${CLAUDE_SKILL_DIR}/scripts/memory-backup.sh` 脚本执行，以确保 manifest 生成、路径安全检查、safety net 备份等机制正常运行

---

## 前置检查

每次触发时按顺序执行：

1. **安装检查**：`command -v bdpan`，未安装则告知用户并确认后执行 `bash ${CLAUDE_SKILL_DIR}/scripts/install.sh`（用户确认后可加 `--yes` 跳过安装器内部确认）
2. **登录检查**：`bdpan whoami`，未登录则引导执行 `bash ${CLAUDE_SKILL_DIR}/scripts/login.sh`
3. **路径校验**：验证远端路径在 `/apps/bdpan/` 范围内

---

## 确认规则

| 风险等级 | 操作 | 策略 |
| --- | --- | --- |
| **高（必须确认）** | `rm` 删除、上传/下载目标已存在同名文件 | 列出影响范围，等待用户确认 |
| **中（路径模糊时确认）** | upload、download、mv、rename、cp | 路径明确直接执行，不明确则确认 |
| **低（直接执行）** | ls、search、whoami、mkdir、share | 无需确认 |

**额外规则：**

* 操作意图模糊（"处理文件"→确认上传还是下载）→ 必须确认
* 序数/代词引用有歧义（"第N个"、"它"、"上面那个"）→ 必须确认
* 用户取消意图（"算了"、"不要了"、"取消"）→ 立即中止，不执行任何命令

---

## 核心操作

### 查看状态

```bash
bdpan whoami
```

### 列表查询

```bash
bdpan ls [目录路径] [--json] [--order name|time|size] [--desc] [--folder]
```

### 上传

```bash
bdpan upload <本地路径> <远端路径>
```

**关键约束：** 单文件上传远端路径必须是文件名，禁止以 `/` 结尾。文件夹上传：`bdpan upload ./project/ project/`。

步骤：确认本地路径存在 → 确认远端路径 → `bdpan ls` 检查远端是否已存在 → 执行。

### 下载

**直接下载：**

```bash
bdpan download <远端路径> <本地路径>
```

步骤：`bdpan ls` 确认云端存在 → 确认本地路径 → 检查本地是否已存在 → **检查文件大小决定下载策略** → 执行。若 ls 未找到，建议 `bdpan search <文件名>`。

**大文件下载策略（重要）：**

Agent 的 Bash 工具有执行超时限制，大文件下载可能因超时而中断。必须根据文件大小选择下载策略：

1. **获取文件大小**：用 `bdpan ls --json <远端路径>` 获取 `size` 字段（字节）
2. **按大小分策略执行**：

| 文件大小 | 策略 | 执行方式 |
| --- | --- | --- |
| ≤ 50MB | 直接下载 | `bdpan download <远端路径> <本地路径>`，Bash timeout 设为 300000（5 分钟） |
| > 50MB | 后台下载 | 使用 `nohup` 后台执行，Agent 轮询进度 |

**小文件（≤ 50MB）直接下载：**

正常执行 `bdpan download`，Bash 工具 timeout 参数设为 `300000`（5 分钟）。

**大文件（> 50MB）后台下载流程：**

```bash
nohup bdpan download <远端路径> <本地路径> > /tmp/bdpan-dl-$$.log 2>&1 & echo $!
```

```bash
kill -0 <PID> 2>/dev/null && echo "running" || echo "done"; ls -l <本地路径> 2>/dev/null; tail -5 /tmp/bdpan-dl-<PID>.log 2>/dev/null
```

```bash
rm -f /tmp/bdpan-dl-<PID>.log
```

Agent 执行大文件后台下载时的行为规范：

* 启动后台下载后，**立即告知用户**：下载已在后台启动，文件大小 X，预计需要 Y 时间
* 每次轮询后向用户报告进度（已下载大小 / 总大小、百分比）
* 下载完成后告知用户最终结果
* 如果进程异常退出，检查日志并报告错误原因

**分享链接下载（先转存再下载到本地）：**

```bash
bdpan download "https://pan.baidu.com/s/1xxxxx?pwd=abcd" ./downloaded/
bdpan download "https://pan.baidu.com/s/1xxxxx" ./downloaded/ -p abcd    # 提取码单独传入
bdpan download "https://pan.baidu.com/s/1xxxxx?pwd=abcd" ./downloaded/ -t my-folder  # 指定转存目录
```

> 分享链接下载同样适用大文件策略：转存完成后，用 `bdpan ls --json` 获取文件大小，再按上述策略执行下载。

### 转存

将分享文件转存到网盘，**不下载到本地**（与 download 分享链接模式的区别）。

```bash
bdpan transfer "https://pan.baidu.com/s/1xxxxx" -p <提取码> [-d 目标目录] [--json]
```

步骤：确认分享链接格式有效 → 确认有提取码（链接中含 `?pwd=` 或反问用户）→ 确认目标目录 → 执行。转存成功后只展示本次转存的文件（非整个目录），显示数量和目标目录。

### 分享

```bash
bdpan share <路径> [路径...] [--period <天数>] [--json]
```

**--period / -d 参数：** 分享有效期（天），取值：0=永久, 1, 7, 30（默认：7）

**智能选择规则：**

Agent 必须根据用户的语义意图判断有效期，而非仅匹配固定关键词。

* 用户表达了"希望长期有效/永久/不过期/一直能用"等语义 → 使用 `--period 0`，并提示用户：永久链接无法自动过期，请注意文件安全
* 用户指定了具体天数或时间范围 → 选择最接近的枚举值（1、7、30）
* 用户未表达任何有效期偏好 → 默认 `--period 7`

步骤：`bdpan ls` 确认文件存在 → 根据用户意图选择有效期 → 执行分享 → 展示链接+提取码+有效期。

> 付费接口，需在百度网盘开放平台购买服务。

### 搜索

```bash
bdpan search <关键词> [--category 0-7] [--no-dir|--dir-only] [--page-size N] [--page N] [--json]
```

category：0=全部 1=视频 2=音频 3=图片 4=文档 5=应用 6=其他 7=种子。`--no-dir` 和 `--dir-only` 互斥。

### 移动 / 复制 / 重命名 / 创建文件夹

```bash
bdpan mv <源路径> <目标目录>
bdpan cp <源路径> <目标目录>
bdpan rename <路径> <新名称>       # 第二参数是文件名，非完整路径
bdpan mkdir <路径>
```

---

## 路径规则

| 场景 | 格式 | 示例 |
| --- | --- | --- |
| **命令参数** | 相对路径（相对于 `/apps/bdpan/`） | `bdpan upload ./f.txt docs/f.txt` |
| **展示给用户** | 中文名 | "已上传到：我的应用数据/bdpan/docs/f.txt" |

映射关系：`我的应用数据` ↔ `/apps`

**禁止：** 命令中使用中文路径（`我的应用数据/...`）、展示时暴露 API 路径（`/apps/bdpan/...`）。

---

## 授权码处理

用户发送 32 位十六进制字符串时，先确认："这是百度网盘授权码吗？确认后将执行登录流程。" 确认后执行 `bash ${CLAUDE_SKILL_DIR}/scripts/login.sh`（不使用 `--yes`，保留安全确认环节）。

---

## 管理功能

### 安装

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/install.sh [--yes]
```

安装器从百度 CDN（`issuecdn.baidupcs.com`）下载并执行。注意：install.sh 不执行本地 SHA256 校验，完整性依赖 HTTPS 传输保护。安全敏感场景建议先手动审查安装器内容或在沙箱中执行。

### 登录 / 注销 / 卸载

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/login.sh              # 登录（内置安全免责声明）
bdpan logout                                            # 注销
bash ${CLAUDE_SKILL_DIR}/scripts/uninstall.sh [--yes]   # 卸载
```

### 更新（必须用户明确指令触发）

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/update.sh              # 检查并更新（需用户确认）
bash ${CLAUDE_SKILL_DIR}/scripts/update.sh --check       # 仅检查更新
```

---

## 记忆备份与恢复

仅支持 4 种 Claw 产品（kimiclaw、maxclaw、qclaw、skill-platform），自动检测当前环境。

**网盘存储路径：** `/apps/bdpan/agent-memory/<agent>/<device>/manual/<timestamp>/`

**备份内容：** 7 个 Workspace 文件（AGENTS.md、SOUL.md、USER.md、IDENTITY.md、TOOLS.md、MEMORY.md、HEARTBEAT.md）+ `memory/*.md` + `manifest.json`

### 备份记忆

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/memory-backup.sh backup
```

### 查看备份列表

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/memory-backup.sh list
```

### 恢复备份

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/memory-backup.sh restore 2026-03-16

bash ${CLAUDE_SKILL_DIR}/scripts/memory-backup.sh restore 2026-03-16 --force

bash ${CLAUDE_SKILL_DIR}/scripts/memory-backup.sh restore 2026-03-16 --yes
```

**恢复安全机制：**

1. **影响预览**：恢复前会列出所有将被覆盖/新增的本地文件清单
2. **显式确认**：默认必须用户输入 `y` 才会执行覆盖（非交互式环境下若未加 `--yes` 直接拒绝执行）
3. **Safety net**：恢复前自动将当前本地记忆备份到 `<workspace>/.backup-before-restore/<timestamp>/`，防止误操作数据丢失

### 操作流程

1. 执行前自动检查：bdpan 是否安装 → 是否已登录（未满足则引导处理）
2. 检测当前 Agent 类型 → 不支持的环境报错退出
3. 执行对应操作（backup/list/restore）

---

## 参考文档

遇到对应问题时按需查阅，无需预加载：

| 文档 | 何时查阅 |
| --- | --- |
| [bdpan-commands.md](/api/v1/skills/baidu-netdisk-skills/file?path=reference%2Fbdpan-commands.md&ownerHandle=wscats) | 需要完整命令参数、选项、JSON 输出格式 |
| [authentication.md](/api/v1/skills/baidu-netdisk-skills/file?path=reference%2Fauthentication.md&ownerHandle=wscats) | 认证流程细节、Token 管理 |
| [examples.md](/api/v1/skills/baidu-netdisk-skills/file?path=reference%2Fexamples.md&ownerHandle=wscats) | 更多使用示例（批量上传、自动备份等） |
| [troubleshooting.md](/api/v1/skills/baidu-netdisk-skills/file?path=reference%2Ftroubleshooting.md&ownerHandle=wscats) | 遇到错误需要排查 |

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

## 核心能力

### 安装

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/install.sh [--yes]
```

安装器从百度 CDN（`issuecdn.baidupcs.com`）下载并执行。注意：install.sh 不执行本地 SHA256 校验，完整性依赖 HTTPS 传输保护。安全敏感场景建议先手动审查安装器内容或在沙箱中执行。

### 登录 / 注销 / 卸载

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/login.sh              # 登录（内置安全免责声明）
bdpan logout                                            # 注销
bash ${CLAUDE_SKILL_DIR}/scripts/uninstall.sh [--yes]   # 卸载
```

### 更新（必须用户明确指令触发）

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/update.sh              # 检查并更新（需用户确认）
bash ${CLAUDE_SKILL_DIR}/scripts/update.sh --check       # 仅检查更新
```

---

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
1. 执行前自动检查：bdpan 是否安装 → 是否已登录（未满足则引导处理）
2. 检测当前 Agent 类型 → 不支持的环境报错退出
3. 执行对应操作（backup/list/restore）

---
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用百度网盘？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: 百度网盘有什么限制？
A: 请参考已知限制章节了解具体限制。
