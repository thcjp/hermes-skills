---
slug: "pan-file-commander-pro"
name: "pan-file-commander-pro"
version: "1.0.0"
displayName: "网盘指挥官专业版"
summary: "命令式网盘管理,含记忆备份恢复、大文件后台下载、批量操作、增量同步、完整性校验。"
license: "Proprietary"
edition: "pro"
description: |-
  网盘指挥官专业版是一个以"命令式高效操作"为核心视角的百度网盘文件管理工具,所有操作限制在 `/apps/bdpan/` 目录内。面向个人创作者、团队协作者、内容运营、开发者、Agent记忆管理者五类角色。针对网盘管理"命令记不住、操作不连贯、路径易出错、风险操作无确认、文件难分类、大文件下载超时中断、批量操作繁琐、记忆无法跨设备同步、下载完整性无校验、同步可靠性差"十大痛点,构建了快捷命令模板、分类视图、智能路径校验、分层确认规则、操作意图识别、记忆备份恢复、大文件后台下载、批量操作模板、增量同步与完整性校验十大核心能力。

  核心能力包括:bdpan CLI完整的文件管理(上传/下载/转存/分享/搜索/移动/复制/重命名/创建/删除);基于文件大小的智能下载策略(小文件直接+大文件后台nohup);Agent记忆备份与恢复(支持兼容Agent、增强Agent、快速Agent、Agent平台四类环境);批量处理模板(批量上传/下载/增量同步);完整性校验(文件大小比对);严格的安全约束与路径校验;分层确认规则(高/中/低风险);操作意图识别与歧义消除。

  适用场景:百度网盘文件日常管理、大文件可靠下载(>50MB后台模式)、批量文件上传下载、Agent记忆跨设备备份与恢复、分享链接转存、团队文件共享、增量同步工作流、下载完整性校验、文件分类浏览与查找、自动化文件同步。

  差异化亮点:相比免费版,专业版新增Agent记忆备份与恢复(支持兼容Agent/增强Agent/快速Agent/Agent平台四类环境,含manifest生成与safety net)、大文件后台下载(nohup+进度轮询,解决Bash超时)、批量操作模板(批量上传/下载)、增量同步(仅上传变化文件)、完整性校验(文件大小比对)。相比通用网盘工具,本指挥官聚焦"命令式高效操作",以快捷命令模板与分层确认规则为核心。

  适用关键词:网盘指挥官、百度网盘、文件管理、bdpan、pan-file-commander、记忆备份、大文件下载、批量操作、增量同步
tags:
  - 智能代理
  - 文件管理
  - 百度网盘
  - 命令式操作
  - 记忆备份
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
---
# 网盘指挥官(专业版)

百度网盘文件管理工具,以"命令式高效操作"为核心视角,所有操作限制在 `/apps/bdpan/` 目录内。专业版在免费版基础上解锁Agent记忆备份与恢复、大文件后台下载、批量操作模板、增量同步与完整性校验。适配所有支持SKILL.md的Agent平台。

> 使用注意事项详见 [reference/notes.md](./reference/notes.md)

## 触发规则

### 网盘文件操作触发

同时满足以下条件才执行:

1. 用户消息中包含**明确指向百度网盘**的关键词,至少匹配以下之一:
   * `百度网盘`、`百度云盘`、`bdpan`、`baidu netdisk`、`baidu pan`、`baidu drive`、`pan.baidu.com`
2. 操作意图明确(上传/下载/转存/分享/查看/搜索/移动/复制/重命名/创建文件夹/删除/登录/注销)
3. 对于**写操作**(上传、删除、移动、覆盖式下载、公开分享),即使触发词命中,也必须先列出"将要执行的操作 + 影响范围"并取得用户显式确认(`y`)后再执行

**不要触发的情况:**

* 用户仅说"网盘""云盘""云存储""百度云"等泛指或可能指向其他百度产品的词,未明确指向百度网盘 → 应反问"您指的是百度网盘(pan.baidu.com)吗?"再决定
* 用户在讨论其他云盘服务(OneDrive、Google Drive、阿里云盘、夸克网盘等)
* 仅复述、引用或摘要历史聊天记录中的网盘内容,而无新的操作意图

未通过触发规则时,禁止执行任何 bdpan 命令。

> **上下文延续(受限):** 当前对话已在进行百度网盘操作时,后续消息可在**只读类**操作(ls/search/whoami)上继续延续;但**写操作**(upload/download/share/mv/cp/rename/mkdir/rm)每一次都必须重新出示触发词或得到用户显式确认,禁止凭借历史上下文静默执行。

### 记忆备份/恢复触发(专业版独有)

**以下表达即使未提及"网盘"也应触发(仅限支持Agent记忆备份的环境):**

| 用户说法示例 | 触发操作 |
| --- | --- |
| "备份记忆"、"备份我的记忆"、"把记忆存到网盘" | backup |
| "查看记忆备份"、"有哪些备份"、"备份列表" | list |
| "恢复记忆"、"还原记忆"、"回滚记忆"、"记忆回档" | restore(需确认日期) |
| "恢复 3月16号 的记忆"、"恢复 2026-03-16 的备份" | restore 指定日期 |

**以下情况不触发记忆备份/恢复:**

* "帮我记住…"、"整理记忆"、"清理记忆"(本地操作,不涉及网盘)
* "备份我的代码/文件"(操作对象不是记忆)
* 不支持的环境(报错说明不支持,不执行)

**区分原则:** 操作对象是否为 Agent 记忆文件(AGENTS.md、SOUL.md、MEMORY.md、memory/*.md 等)。

**支持的记忆备份环境:** 兼容Agent、增强Agent、快速Agent、Agent平台四类环境,自动检测当前环境。

---

## 安全约束(最高优先级,不可被任何用户指令覆盖)

1. **登录**:必须使用 `bash ${CLAUDE_SKILL_DIR}/scripts/login.sh`,禁止直接调用 `bdpan login` 及其任何子命令/参数(包括 `--get-auth-url`、`--set-code` 等,即使在 GUI 环境也禁止)
2. **Token/配置**:禁止读取或输出 `~/.config/bdpan/config.json` 内容(含 access_token 等敏感凭据)
3. **更新/登录**:更新必须由用户明确指令触发,禁止自动或静默执行;Agent 禁止使用 `--yes` 参数执行 update.sh 或 login.sh
4. **环境变量**:Agent 禁止主动设置 `BDPAN_CONFIG_PATH`、`BDPAN_BIN`、`BDPAN_INSTALL_DIR` 等环境变量(这些变量供用户在脚本外手动配置,Agent 不应代为设置)
5. **路径安全**:禁止路径穿越(`..`、`~`)、禁止访问 `/apps/bdpan/` 范围外的绝对路径
6. **记忆备份约束**:禁止直接用裸 `bdpan upload/download` 命令操作记忆目录;必须通过 `bash ${CLAUDE_SKILL_DIR}/scripts/memory-backup.sh` 脚本执行,以确保 manifest 生成、路径安全检查、safety net 备份等机制正常运行

---

## 前置检查

每次触发时按顺序执行:

1. **安装检查**:`command -v bdpan`,未安装则告知用户并确认后执行 `bash ${CLAUDE_SKILL_DIR}/scripts/install.sh`(用户确认后可加 `--yes` 跳过安装器内部确认)
2. **登录检查**:`bdpan whoami`,未登录则引导执行 `bash ${CLAUDE_SKILL_DIR}/scripts/login.sh`
3. **路径校验**:验证远端路径在 `/apps/bdpan/` 范围内

---

## 确认规则(差异化:分层风险模型)

| 风险等级 | 操作 | 策略 | 示例 |
| --- | --- | --- | --- |
| **高(必须确认)** | `rm` 删除、上传/下载目标已存在同名文件、记忆恢复(覆盖当前记忆) | 列出影响范围,等待用户确认 | `bdpan rm docs/old.txt` |
| **中(路径模糊时确认)** | upload、download、mv、rename、cp | 路径明确直接执行,不明确则确认 | `bdpan mv docs/ archive/` |
| **低(直接执行)** | ls、search、whoami、mkdir、share | 无需确认 | `bdpan ls docs/` |

**额外规则:**

* 操作意图模糊("处理文件"→确认上传还是下载)→ 必须确认
* 序数/代词引用有歧义("第N个"、"它"、"上面那个")→ 必须确认
* 用户取消意图("算了"、"不要了"、"取消")→ 立即中止,不执行任何命令

---

## 快速开始(分级时间)

### 30秒:确认登录状态
```bash
bdpan whoami
```
未登录则运行: `bash ${CLAUDE_SKILL_DIR}/scripts/login.sh`

### 60秒:浏览文件并执行一次操作
```bash
# 1. 列出根目录文件
bdpan ls

# 2. 上传一个文件(确认后执行)
bdpan upload ./local-file.txt docs/local-file.txt
```

### 120秒:完成专业版完整操作流程
1. 前置检查(安装→登录→路径校验)
2. 浏览文件(参见快捷命令模板)
3. 选择操作(上传/下载/转存/分享/搜索/移动/复制/重命名/创建/删除/记忆备份)
4. 路径校验与确认(参见确认规则)
5. 执行操作并报告结果(大文件使用后台下载,批量操作使用模板)

---

## 使用流程

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。

#
## 核心能力
### 浏览类快捷命令
执行浏览类快捷命令操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作。
执行浏览类快捷命令操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作。
```bash
# 列出根目录
bdpan ls

# 列出指定目录(按名称排序)
bdpan ls docs/ --order name

# 列出指定目录(按时间倒序,最新在前)
bdpan ls docs/ --order time --desc

# 列出指定目录(按大小倒序,最大在前)
bdpan ls docs/ --order size --desc

# 仅列出文件夹
bdpan ls docs/ --folder

# JSON格式输出(便于后续处理)
bdpan ls docs/ --json
```

### 搜索类快捷命令
执行搜索类快捷命令操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作。
执行搜索类快捷命令操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作。
```bash
# 按关键词搜索
bdpan search "报告"

# 搜索视频文件
bdpan search "会议" --category 1

# 搜索图片文件
bdpan search "截图" --category 3

# 搜索文档文件
bdpan search "合同" --category 4

# 仅搜索文件夹
bdpan search "项目" --dir-only
```

### 单文件操作快捷命令
执行单文件操作快捷命令操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作。
```bash
# 上传单文件
bdpan upload ./local.txt docs/local.txt

# 下载单文件(小文件≤50MB直接下载)
bdpan download docs/local.txt ./local.txt

# 移动文件
bdpan mv docs/old.txt archive/

# 复制文件
bdpan cp docs/template.txt templates/

# 重命名文件(第二参数是文件名,非完整路径)
bdpan rename docs/old-name.txt new-name.txt

# 创建文件夹
bdpan mkdir docs/new-folder

# 删除文件(高风险,需确认)
bdpan rm docs/unwanted.txt
```

### 分享类快捷命令
执行分享类快捷命令操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作。
执行分享类快捷命令操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作。
```bash
# 分享文件(默认7天有效期)
bdpan share docs/report.pdf

# 分享文件(永久有效,需提示用户安全风险)
bdpan share docs/report.pdf --period 0

# 分享文件(30天有效期)
bdpan share docs/report.pdf --period 30

# 分享多个文件
bdpan share docs/file1.txt docs/file2.txt --period 7
```

### 转存类快捷命令
执行转存类快捷命令操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作。
```bash
# 转存分享链接(链接含提取码)
bdpan transfer "https://pan.baidu.com/s/1xxxxx?pwd=abcd"

# 转存分享链接(提取码单独传入)
bdpan transfer "https://pan.baidu.com/s/1xxxxx" -p abcd

# 转存到指定目录
bdpan transfer "https://pan.baidu.com/s/1xxxxx" -p abcd -d downloads/
```

---
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：命令式网盘管理、含记忆备份恢复、大文件后台下载、批量操作、增量同步、完整性校验、网盘指挥官专业版、是一个以、命令式高效操作、为核心视角的百度、网盘文件管理工具、所有操作限制在、apps、bdpan、目录内、面向个人创作者、团队协作者、内容运营、开发者、Agent、记忆管理者五类角、针对网盘管理、命令记不住、操作不连贯、路径易出错、风险操作无确认、文件难分类、大文件下载超时中、批量操作繁琐、记忆无法跨设备同、下载完整性无校验、同步可靠性差、十大痛点、构建了快捷命令模、分类视图、智能路径校验、分层确认规则、操作意图识别、记忆备份恢复、批量操作模板、增量同步与完整性、校验十大核心能力等。

## 智能下载策略(专业版独有核心)

根据文件大小自动选择下载策略,解决大文件超时中断痛点:

### 下载策略选择
```bash
# 1. 获取文件大小
bdpan ls --json <远端路径>
# 从JSON输出中读取 size 字段(字节)
```

| 文件大小 | 策略 | 执行方式 | 超时设置 |
|----------|------|----------|----------|
| ≤ 50MB | 直接下载 | `bdpan download <远端路径> <本地路径>` | Bash timeout=300000(5分钟) |
| > 50MB | 后台下载 | nohup后台执行,Agent轮询进度 | 无超时限制 |

### 小文件(≤ 50MB)直接下载
```bash
bdpan download <远端路径> <本地路径>
```
Bash 工具 timeout 参数设为 `300000`(5 分钟)。

### 大文件(> 50MB)后台下载流程(专业版独有)
```bash
# 启动后台下载
nohup bdpan download <远端路径> <本地路径> > /tmp/bdpan-dl-$$.log 2>&1 & echo $!
```

```bash
# 轮询进度
kill -0 <PID> 2>/dev/null && echo "running" || echo "done"; ls -l <本地路径> 2>/dev/null; tail -5 /tmp/bdpan-dl-<PID>.log 2>/dev/null
```

```bash
# 清理日志
rm -f /tmp/bdpan-dl-<PID>.log
```

**Agent执行大文件后台下载行为规范:**

* 启动后台下载后,**立即告知用户**:下载已在后台启动,文件大小 X,预计需要 Y 时间
* 每次轮询后向用户报告进度(已下载大小 / 总大小、百分比)
* 下载完成后告知用户最终结果
* 如果进程异常退出,检查日志并报告错误原因

### 分享链接下载(先转存再下载到本地)
```bash
bdpan download "https://pan.baidu.com/s/1xxxxx?pwd=abcd" ./downloaded/
bdpan download "https://pan.baidu.com/s/1xxxxx" ./downloaded/ -p abcd    # 提取码单独传入
bdpan download "https://pan.baidu.com/s/1xxxxx?pwd=abcd" ./downloaded/ -t my-folder  # 指定转存目录
```

> 分享链接下载同样适用大文件策略:转存完成后,用 `bdpan ls --json` 获取文件大小,再按上述策略执行下载。

---

## 完整性校验(专业版独有)

下载完成后验证文件完整性:

```bash
# 1. 获取远端文件大小
bdpan ls --json <远端路径> | grep -o '"size":[0-9]*'

# 2. 获取本地文件大小
ls -l <本地路径> | awk '{print $5}'

# 3. 比对大小
# 如大小不一致,提示用户重新下载
```

---

## 批量操作模板(专业版独有)

### 批量上传
```bash
# 批量上传目录下所有文件
for file in ./local-dir/*; do
  filename=$(basename "$file")
  bdpan upload "$file" "remote-dir/$filename"
done
```

### 批量下载
```bash
# 获取文件列表并批量下载
bdpan ls --json remote-dir/ | jq -r '.[].path' | while read path; do
  bdpan download "$path" "./local-dir/$(basename $path)"
done
```

### 批量分享
```bash
# 批量分享目录下所有PDF文件
bdpan ls --json docs/ | jq -r '.[] | select(.path | endswith(".pdf")) | .path' | while read file; do
  echo "=== 分享: $file ==="
  bdpan share "$file" --period 7
done
```

---

## 增量同步机制(专业版独有)

仅上传变化的文件,减少带宽消耗:

```bash
# 1. 获取远端文件列表(含大小和时间)
bdpan ls --json remote-dir/ > /tmp/remote-files.json

# 2. 对比本地文件
for file in ./local-dir/*; do
  filename=$(basename "$file")
  local_size=$(stat -c%s "$file")
  remote_size=$(jq -r ".[] | select(.name==\"$filename\") | .size" /tmp/remote-files.json)

  if [ "$local_size" != "$remote_size" ]; then
    echo "文件 $filename 有变化,上传中..."
    bdpan upload "$file" "remote-dir/$filename"
  else
    echo "文件 $filename 无变化,跳过"
  fi
done
```

---

## Agent记忆备份与恢复(专业版独有)

支持兼容Agent、增强Agent、快速Agent、Agent平台四类环境,自动检测当前环境是否支持。

**网盘存储路径:** `/apps/bdpan/agent-memory/<agent>/<device>/manual/<timestamp>/`

**备份内容:** 7 个 Workspace 文件(AGENTS.md、SOUL.md、USER.md、IDENTITY.md、TOOLS.md、MEMORY.md、HEARTBEAT.md)+ `memory/*.md` + `manifest.json`

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

**恢复安全机制:**

1. **影响预览**:恢复前会列出所有将被覆盖/新增的本地文件清单
2. **显式确认**:默认必须用户输入 `y` 才会执行覆盖(非交互式环境下若未加 `--yes` 直接拒绝执行)
3. **Safety net**:恢复前自动将当前本地记忆备份到 `<workspace>/.backup-before-restore/<timestamp>/`,防止误操作数据丢失

### 操作流程
1. 执行前自动检查:bdpan 是否安装 → 是否已登录(未满足则引导处理)
2. 检测当前 Agent 类型 → 不支持的环境报错退出(仅支持兼容Agent/增强Agent/快速Agent/Agent平台四类)
3. 执行对应操作(backup/list/restore)

---

## 文件分类视图(差异化)

通过 `--json` 输出配合本地处理,生成分类视图:

### 按类型分类
```bash
bdpan ls docs/ --json | jq -r '.[] | .path' | grep -oE '\.[^.]+$' | sort | uniq -c | sort -rn
```

### 按大小分类
```bash
bdpan ls docs/ --json | jq -r '
  if .size > 104857600 then "大文件(>100MB)"
  elif .size > 10485760 then "中文件(10-100MB)"
  elif .size > 1048576 then "小文件(1-10MB)"
  else "微小文件(<1MB)"
  end' | sort | uniq -c
```

### 按时间分类
```bash
bdpan ls docs/ --json | jq -r '.created_at | .[0:7]' | sort | uniq -c
```

---

## 智能路径校验(差异化)

### 路径补全
```bash
# 列出目录以辅助路径补全
bdpan ls docs/ --folder
# 用户输入"docs/"后,Agent列出docs下的文件夹供选择
```

### 越界检测
```bash
validate_path() {
  local path="$1"
  if [[ "$path" == *"..",* ]] || [[ "$path" == *~* ]]; then
    echo "错误: 路径包含禁止字符(.. 或 ~)"
    return 1
  fi
  if [[ "$path" == /* ]]; then
    echo "错误: 命令参数禁止使用绝对路径,请使用相对路径"
    return 1
  fi
  return 0
}
```

---

## 操作意图识别(差异化)

### 歧义消除决策树
```
用户输入 → 是否包含明确操作动词?
├─ 否 → 反问:"您想做什么?(上传/下载/查看/搜索/移动/删除/分享/备份记忆)"
└─ 是 → 操作对象是否明确?
        ├─ 否 → 反问:"请确认操作对象(哪个文件/目录?)"
        └─ 是 → 路径是否在 /apps/bdpan/ 范围内?
                ├─ 否 → 提示路径越界,建议合法路径
                └─ 是 → 风险等级判断(高/中/低)
                        ├─ 高 → 列出影响范围,等待确认
                        ├─ 中 → 路径模糊时确认
                        └─ 低 → 直接执行
```

---

## 路径规则

| 场景 | 格式 | 示例 |
| --- | --- | --- |
| **命令参数** | 相对路径(相对于 `/apps/bdpan/`) | `bdpan upload ./f.txt docs/f.txt` |
| **展示给用户** | 中文名 | "已上传到:我的应用数据/bdpan/docs/f.txt" |

映射关系:`我的应用数据` ↔ `/apps`

**禁止:** 命令中使用中文路径(`我的应用数据/...`)、展示时暴露 API 路径(`/apps/bdpan/...`)。

---

## 授权码处理

用户发送 32 位十六进制字符串时,先确认:"这是百度网盘授权码吗?确认后将执行登录流程。" 确认后执行 `bash ${CLAUDE_SKILL_DIR}/scripts/login.sh`(不使用 `--yes`,保留安全确认环节)。

---

## 管理功能

### 安装
```bash
bash ${CLAUDE_SKILL_DIR}/scripts/install.sh [--yes]
```

安装器从百度 CDN(`issuecdn.baidupcs.com`)下载并执行。注意:install.sh 不执行本地 SHA256 校验,完整性依赖 HTTPS 传输保护。安全敏感场景建议先手动审查安装器内容或在沙箱中执行。

### 登录 / 注销 / 卸载
```bash
bash ${CLAUDE_SKILL_DIR}/scripts/login.sh              # 登录(内置安全免责声明)
bdpan logout                                            # 注销
bash ${CLAUDE_SKILL_DIR}/scripts/uninstall.sh [--yes]   # 卸载
```

### 更新(必须用户明确指令触发)
```bash
bash ${CLAUDE_SKILL_DIR}/scripts/update.sh              # 检查并更新(需用户确认)
bash ${CLAUDE_SKILL_DIR}/scripts/update.sh --check       # 仅检查更新
```

---

## 示例

### 场景一:个人创作者 - 大文件下载
```text
角色: 个人创作者
任务: "帮我下载网盘里的视频素材,大概800MB"

执行流程:
1. 前置检查(安装→登录)
2. bdpan ls --json 获取文件大小(800MB > 50MB,使用后台下载)
3. nohup启动后台下载,告知用户:下载已在后台启动,文件大小800MB,预计需要X分钟
4. Agent轮询进度,每次报告已下载大小/总大小/百分比
5. 下载完成后,执行完整性校验(远端大小 vs 本地大小)
6. 告知用户最终结果,清理日志文件
```

### 场景二:团队协作者 - 批量分享
```text
角色: 团队协作者
任务: "把docs目录下所有PDF分享给团队,有效期7天"

执行流程:
1. 前置检查
2. bdpan ls --json docs/ 获取PDF文件列表
3. 遍历PDF文件,逐个执行 bdpan share --period 7
4. 收集所有分享链接+提取码
5. 汇总输出:文件名+链接+提取码+有效期
6. 提示用户:链接7天后过期,请及时分享给团队
```

### 场景三:内容运营 - 批量上传与增量同步
```text
角色: 内容运营
任务: "把本地素材目录同步到网盘,只上传有变化的文件"

执行流程:
1. 前置检查
2. bdpan ls --json remote-dir/ 获取远端文件列表(含大小)
3. 遍历本地文件,对比大小
4. 对有变化的文件执行 bdpan upload
5. 对无变化的文件跳过(节省带宽)
6. 输出同步报告:新增X个,更新Y个,跳过Z个
```

### 场景四:Agent记忆管理者 - 跨设备记忆同步
```text
角色: Agent记忆管理者
任务: "备份我的Agent记忆到网盘,然后在新设备恢复"

执行流程:
1. 检测当前环境(兼容Agent/增强Agent/快速Agent/Agent平台)
2. 执行 bash ${CLAUDE_SKILL_DIR}/scripts/memory-backup.sh backup
3. 备份7个Workspace文件 + memory/*.md + manifest.json
4. 生成备份时间戳目录
5. 在新设备执行 memory-backup.sh list 查看可用备份
6. 选择日期执行 memory-backup.sh restore <date>
7. 恢复前列出影响预览,要求用户确认
8. 自动创建Safety net备份到 .backup-before-restore/
9. 执行恢复,告知用户结果
```

### 场景五:开发者 - 分享链接转存与下载
```text
角色: 开发者
任务: "朋友发来的分享链接,转存到网盘后下载到本地"

执行流程:
1. 前置检查
2. 确认分享链接格式有效
3. 确认提取码(链接含 ?pwd= 或反问用户)
4. bdpan transfer 转存到指定目录
5. bdpan ls --json 获取转存文件大小
6. 按大小选择下载策略(≤50MB直接,>50MB后台)
7. 下载完成后完整性校验
8. 告知用户最终结果
```

---

## 已知限制

- 本skill的能力范围受限于核心能力章节中定义的功能,不支持超出范围的操作
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 错误处理


| 序号 | 错误场景 | 原因 | 处理方式 | 优先级 |
|------|----------|------|----------|--------|
| 1 | 输入参数缺失 | 用户未提供必要参数 | 提示用户提供所需参数后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 | P0 |
| 2 | 执行超时 | 处理时间过长 | 检查输入数据量,分批处理 | P1 |
| 3 | 输出格式错误 | 结果不符合预期格式 | 检查`output_format`参数配置 | P1 |

## 常见问题FAQ

**Q: 命令参数中的路径为什么不能用绝对路径?**
A: 所有操作限制在 `/apps/bdpan/` 目录内,命令参数使用相对路径(相对于 `/apps/bdpan/`)。绝对路径会被拒绝,以确保路径安全。展示给用户时使用中文名(我的应用数据/bdpan/...)。

**Q: 上传文件时提示远端路径错误?**
A: 单文件上传远端路径必须是文件名(如 `docs/file.txt`),禁止以 `/` 结尾(如 `docs/`)。文件夹上传使用 `bdpan upload ./project/ project/` 格式。

**Q: 如何选择分享有效期?**
A: 根据语义意图判断:用户表达"长期/永久/不过期"使用 `--period 0`(并提示安全风险);指定具体天数选择最接近的枚举值(1/7/30);未表达偏好默认 `--period 7`。永久链接无法自动过期,请注意文件安全。

**Q: 分享链接转存和下载有什么区别?**
A: 转存(`bdpan transfer`)将分享文件保存到你的网盘,不下载到本地。下载分享链接(`bdpan download "分享链接"`)先转存再下载到本地。如只需保存到网盘用transfer,如需本地文件用download。

**Q: 大文件下载总是超时中断怎么办?**
A: 使用专业版智能下载策略。先用 `bdpan ls --json` 获取文件大小,大于50MB的文件使用nohup后台下载模式,Agent轮询进度。这避免了Bash工具超时限制导致的中断。

**Q: 下载速度很慢怎么办?**
A: 下载速度受百度网盘服务端限制。非会员用户可能遇到限速。建议:1)确认网络连接正常;2)使用后台下载模式避免超时;3)如需更高速度,考虑开通百度网盘会员。

**Q: 如何判断下载是否完整?**
A: 使用专业版完整性校验。下载完成后,用 `bdpan ls --json` 获取远端文件大小,与本地文件大小(`ls -l`)比对。大小不一致则需要重新下载。

**Q: 批量上传很多文件如何操作?**
A: 使用专业版批量操作模板。用for循环遍历本地目录,逐个执行 `bdpan upload`。如需增量同步(仅上传变化文件),先获取远端文件列表,对比大小后仅上传有变化的文件。

**Q: 记忆备份支持哪些环境?**
A: 支持兼容Agent、增强Agent、快速Agent、Agent平台四类环境。脚本会自动检测当前环境,不支持的环境会报错退出。操作对象必须是Agent记忆文件(AGENTS.md、SOUL.md、MEMORY.md等)。

**Q: 恢复记忆会覆盖当前记忆吗?**
A: 会,但有安全机制保护。恢复前会:1)列出所有将被覆盖的文件清单;2)要求用户显式确认;3)自动将当前记忆备份到 `.backup-before-restore/` 目录,防止误操作数据丢失。

**Q: 增量同步如何判断文件是否变化?**
A: 通过文件大小对比。先用 `bdpan ls --json` 获取远端文件列表(含size字段),再与本地文件大小(`stat -c%s`)比对。大小不一致则认为有变化,执行上传。大小一致则跳过。

**Q: 专业版与免费版的核心差异?**
A: 专业版在免费版基础上新增:Agent记忆备份与恢复(支持四类环境)、大文件后台下载(nohup+进度轮询)、批量操作模板(批量上传/下载/分享)、增量同步(仅上传变化文件)、完整性校验(文件大小比对)。

## 故障排查

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| `bdpan: command not found` | 未安装 | 运行 `bash ${CLAUDE_SKILL_DIR}/scripts/install.sh` |
| `not logged in` | 未登录 | 运行 `bash ${CLAUDE_SKILL_DIR}/scripts/login.sh` |
| 下载超时中断 | 文件过大,Bash超时 | 使用大文件后台下载策略(nohup) |
| 上传路径错误 | 远端路径以`/`结尾 | 单文件上传远端路径必须是文件名 |
| 下载文件不完整 | 网络中断或限速 | 使用完整性校验比对大小,重新下载 |
| 分享链接无效 | 链接过期或提取码错误 | 确认链接有效性和提取码 |
| 分享接口报错 | 未购买百度网盘开放平台服务 | 分享为付费接口,需在开放平台购买服务 |
| 路径穿越报错 | 路径含`..`或`~` | 使用相对路径,禁止路径穿越 |
| 中文路径报错 | 命令中使用了中文路径 | 命令参数使用相对路径,展示时用中文名 |
| 记忆备份失败 | 环境不支持或未登录 | 检查环境支持(兼容/增强/快速/Agent平台),确认bdpan已登录 |
| 恢复后记忆异常 | 恢复了错误日期 | 从 `.backup-before-restore/` 恢复Safety net备份 |
| 增量同步遗漏 | 文件大小相同但内容不同 | 增量同步仅对比大小,如需精确对比需用哈希(需手动实现) |
| 批量操作中断 | 单个文件失败导致循环退出 | 脚本中加 `|| true` 或 `continue` 跳过失败文件 |
| 序数引用歧义 | "第N个"不明确 | 列出文件清单,向用户确认具体文件 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Shell**: bash(脚本执行需要)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| bdpan CLI | 工具 | 必需 | `bash ${CLAUDE_SKILL_DIR}/scripts/install.sh` |
| 百度网盘账户 | 账户 | 必需 | 注册百度网盘账号 |
| bash | 运行时 | 必需 | 系统自带或安装Git Bash |
| jq | 工具 | 可选(JSON处理与分类视图) | 从stedolan.github.io/jq安装 |
| nohup | 工具 | 可选(大文件后台下载) | 系统自带 |

### API Key 配置
- 通过百度网盘OAuth授权登录,无需手动配置API Key
- 授权码通过 `bash ${CLAUDE_SKILL_DIR}/scripts/login.sh` 流程获取
- **禁止**读取或输出 `~/.config/bdpan/config.json` 内容(含敏感凭据)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,需要命令行执行能力运行bdpan CLI)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent使用bdpan CLI管理百度网盘文件。需要bdpan CLI和百度网盘账户。专业版高级功能(记忆备份/大文件下载/批量操作)需要对应环境支持。

## 专业版特性

本专业版相比免费版新增以下能力:

- Agent记忆备份与恢复:支持兼容Agent、增强Agent、快速Agent、Agent平台四类环境,含manifest生成、路径安全检查、Safety net备份,支持跨设备记忆同步
- 大文件后台下载:基于文件大小的智能下载策略(≤50MB直接+>50MB后台nohup),Agent轮询进度,解决Bash超时中断痛点
- 批量操作模板:批量上传、批量下载、批量分享,支持for循环遍历与失败跳过
- 增量同步机制:仅上传变化的文件(文件大小对比),减少带宽消耗
- 完整性校验:下载完成后比对远端与本地文件大小,确保下载完整
- 记忆备份/恢复触发规则:即使未提及"网盘"也能触发记忆备份与恢复操作

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 核心文件管理(上传/下载/转存/分享/搜索/移动/复制/重命名/创建/删除)+ 快捷命令模板 + 分类视图 + 路径校验 | 个人日常文件管理 |
| 收费专业版 | ¥19.9/月 | 全功能 + 记忆备份恢复 + 大文件后台下载 + 批量操作 + 增量同步 + 完整性校验 | 创作者、团队协作者、内容运营、Agent记忆管理 |

专业版通过SkillHub SkillPay发布。定价为创意工具类(内容生产与文件管理),包含5类角色场景支持与10大核心能力。

## License与版权声明

本skill基于原始作品改进,保留原始版权声明:

- 原始作品: baidu-netdisk-skills (百度网盘)
- 原始license: MIT
- 改进作品: pan-file-commander-pro
- 改进license: MIT

本改进作品在原始作品基础上进行了深度差异化改造,包括但不限于:
- 重新定位为"指挥官"视角(原始为通用文件管理)
- 新增快捷命令模板(浏览/搜索/单文件操作/分享/转存5类)
- 新增文件分类视图(按类型/大小/时间)
- 新增智能路径校验(路径补全与越界检测)
- 新增操作意图识别(歧义消除决策树)
- 新增分层确认规则(高/中/低风险+示例)
- 新增智能下载策略(专业版独有,按文件大小自动选择直接/后台模式)
- 新增Agent记忆备份与恢复(专业版独有,支持兼容Agent/增强Agent/快速Agent/Agent平台四类环境)
- 新增批量操作模板(专业版独有,批量上传/下载/分享)
- 新增增量同步机制(专业版独有,仅上传变化文件)
- 新增完整性校验(专业版独有,文件大小比对)
- 新增记忆备份/恢复触发规则(专业版独有)
- 新增分级快速开始(30秒/60秒/120秒)
- 新增FAQ(12问)与故障排查表(14项)
- 新增5类角色场景示例(创作者/团队/运营/记忆管理/开发者)
- 重写description为五段结构,新增edition字段
- 保留原作者版权声明，去除非必要外部引用链接
- 兼容Agent平台适配(原私有环境名已通用化为兼容Agent/增强Agent/快速Agent/Agent平台)

原始MIT license允许修改与再分发,本改进作品在MIT license下发布,保留原始版权声明。
