---
slug: "obsidian-cli"
name: "obsidian-cli"
version: 1.0.1
displayName: "Obsidian CLI(专业版)"
summary: "全功能Obsidian命令行管理工具，支持模板、插件、同步、历史、开发工具与TUI交互模式。Obsidian CLI工具专业版是面向团队和高级用户的完整命令行知识管理方案，在免费版基础上解锁"
license: "Proprietary"
edition: "pro"
description: |-
  Obsidian CLI工具专业版是面向团队和高级用户的完整命令行知识管理方案，在免费版基础上解锁模板管理、插件与主题控制、Obsidian Sync同步、文件版本历史、开发者调试工具、工作区布局管理和TUI交互模式等全部高级能力。核心能力：全量文件操作（移动/删除/覆盖）、模板读取与批量插入、插件安装与重载、主题切换与CSS片段管理、Sync同步状态与历史恢复、文件版本对比与回滚、开发者工具（控制台/错误/DOM/截图）、工作区保存加载、TUI交互终端
tags:
  - 笔记管理
  - 命令行工具
  - 知识库运维
  - 高级集成
  - 工具
  - 效率
  - 自动化
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"
---
# Obsidian CLI(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Obsidian CLI(专业版)idian命令行管理 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 专业版支持 | 说明 |
|:-----|:-----|:-----|
| 全量文件操作 | 支持 | 创建、读取、追加、移动、删除、覆盖 |
| 全文搜索 | 支持 | 关键词搜索、路径过滤、JSON输出、打开结果 |
| 标签与属性 | 支持 | 标签统计、属性读写、列表类型支持 |
| 链接结构分析 | 支持 | 反向链接、外向链接、孤立笔记、断链检测 |
| Daily Notes | 支持 | 打开、读取、追加、前置插入、分屏模式 |
| 任务管理 | 支持 | 全库任务列表、状态切换、自定义状态标记 |
| 模板管理 | 支持 | 列出模板、读取内容、变量解析、插入到文件 |
| 书签管理 | 支持 | 文件/文件夹/搜索/URL书签的增删查 |
| 插件管理 | 支持 | 安装、启用、禁用、卸载、开发重载 |
| 主题与CSS | 支持 | 主题切换、安装、CSS片段启用禁用 |
| Obsidian Sync | 支持 | 同步状态、暂停恢复、历史恢复、已删除文件 |
| 文件历史 | 支持 | 版本列表、读取历史版本、恢复、diff对比 |
| 开发者工具 | 支持 | 控制台、JS错误、eval执行、截图、DOM检查 |
| 工作区管理 | 支持 | 当前布局查看、保存、加载工作区 |
| TUI交互模式 | 支持 | 带自动补全和历史记录的终端交互界面 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 全量文件操作

针对全量文件,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供全量文件操作相关的配置参数、输入数据和处理选项.
**输出**: 返回全量文件操作的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`全量文件操作`的配置文档进行参数调优
### 全文搜索

针对全文搜索,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供全文搜索相关的配置参数、输入数据和处理选项.
**输出**: 返回全文搜索的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`全文搜索`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 开发者场景：插件开发与调试
在开发Obsidian插件时，频繁需要重载插件、查看控制台日志和截图调试。通过命令行将整个调试流程自动化：

```bash
obsidian plugin:reload id=my-plugin
# ...
obsidian dev:errors
# ...
obsidian dev:screenshot path=bug-report.png
# ...
obsidian eval code="app.vault.getFiles().length"
```

### 运维场景：知识库健康审计
定期对大型知识库执行结构审计，识别需要处理的孤立笔记和断链：

```bash
obsidian orphans
# ...
obsidian deadends
# ...
obsidian unresolved verbose counts
```

### 团队场景：多设备同步管理
管理团队共享知识库的同步状态，确保多设备数据一致性：

```bash
obsidian sync:status
# ...
obsidian sync:deleted
obsidian sync:restore file="重要文档" version=2
# ...
obsidian sync off
obsidian sync on
```

### 内容场景：模板化批量创建
使用模板批量创建结构化笔记，保持团队文档格式统一：

```bash
obsidian templates
# ...
obsidian template:read name=会议纪要 resolve title="周会202601"
# ...
obsidian create name="周会纪要-第10周" template=会议纪要
# ...
obsidian template:insert name=任务清单
```

## 使用流程

### 前置条件
1. Obsidian 1.12及以上版本，需Catalyst许可证
2. 在Obsidian中开启命令行接口：设置 → 通用 → 命令行接口 → 启用
3. 注册`obsidian`命令后重启终端
4. Obsidian应用必须处于运行状态

### 依赖说明

### 运行环境
5. **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
6. **操作系统**：Windows / macOS / Linux
7. **Obsidian版本**：1.12及以上，需Catalyst许可证
8. **Obsidian Sync**：同步功能需要Obsidian Sync订阅

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| Obsidian应用 | 桌面应用 | 必需 | 从Obsidian官网下载安装 |
| obsidian CLI | 命令行工具 | 必需 | 在Obsidian设置中启用命令行接口 |
| Obsidian Sync | 订阅服务 | 可选 | 同步功能需要，按需订阅 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
9. 本Skill基于Obsidian本地命令行接口，无需额外API Key
10. Obsidian Sync功能需要Obsidian账户登录，在应用内配置
11. 开发者工具中的eval执行无需额外认证

### 可用性分类
12. **分类**：MD+EXEC（纯Markdown指令，需要exec命令行执行能力）
13. **说明**：基于Markdown的AI Skill，通过自然语言指令驱动Agent执行Obsidian全量命令行操作

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | obsidian-cli处理的内容输入 |,  |
| content | string | 否 | obsidian-cli处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "cli 相关配置参数",
    result: "cli 相关配置参数",
    result: "cli 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 症状 | 可能原因 | 解决方案 | 优先级 |
|:------|------:|:------|:------|
| 命令执行无响应 | Obsidian未运行 | 启动Obsidian应用后 | 高 |
| command not found | CLI未注册或PATH未更新 | 在设置中启用CLI，重启终端 | 高 |
| 插件安装失败 | 插件ID错误或网络问题 | 确认插件ID，
| Sync状态显示错误 | Sync订阅过期 | 检查Obsidian Sync订阅状态 | 高 |
| eval执行报错 | JS语法错误或API不存在 | 在开发者控制台先测试代码 | 中 |
| 截图文件为空 | 路径权限问题 | 使用有写入权限的目录 | 低 |
| TUI补全不工作 | 终端不兼容 | 使用现代终端模拟器 | 低 |
| 工作区加载失败 | 引用的文件已删除 | 重建工作区或恢复文件 | 中 |
| diff无输出 | 版本号超出范围 | 先用history查看有效版本 | 低 |
| 主题切换无效 | 主题文件损坏 | 卸载后重新安装主题 | 中 |

## 依赖说明(补充)

| 依赖项 | 类型 | 必需 | 说明 |
|---:|:---|---:|---:|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 文件高级操作
```bash
obsidian move file="草稿" to="归档/"
# ...
obsidian move path="收件箱/旧笔记.md" to="项目/新笔记.md"
# ...
obsidian delete file="废弃笔记"
# ...
obsidian delete file="废弃笔记" permanent
# ...
obsidian create name="自动生成" content="# 自动内容" silent overwrite
obsidian create path="收件箱/想法.md" template=Daily
```

### 搜索高级用法
```bash
obsidian search:open query="项目计划"
# ...
obsidian search query="待办" matches
# ...
obsidian search query="报告" path="项目/" limit=10
```

### 链接结构分析
```bash
obsidian backlinks file="核心概念"
# ...
obsidian links file="核心概念"
# ...
obsidian orphans
# ...
obsidian deadends
# ...
obsidian unresolved
obsidian unresolved verbose counts
```

### 模板管理
```bash
obsidian templates
# ...
obsidian template:read name=Daily
# ...
obsidian template:read name=Daily resolve title="今日笔记"
# ...
obsidian template:insert name=任务清单
```

### 书签管理
```bash
obsidian bookmarks
# ...
obsidian bookmark file="重要文档.md"
# ...
obsidian bookmark file=笔记 subpath="#章节标题"
# ...
obsidian bookmark folder="项目/"
# ...
obsidian bookmark search="详情见说明"
# ...
obsidian bookmark url="https://example.com" title="参考资料"
```

### 插件与主题管理
```bash
obsidian plugins
# ...
obsidian plugins:enabled
# ...
obsidian plugin id=dataview
# ...
obsidian plugin:enable id=dataview
obsidian plugin:disable id=dataview
# ...
obsidian plugin:install id=dataview enable
# ...
obsidian plugin:uninstall id=dataview
# ...
obsidian plugin:reload id=my-plugin
# ...
obsidian themes
obsidian theme
obsidian theme:set name=Minimal
obsidian theme:install name="主题名称" enable
# ...
obsidian snippets
obsidian snippet:enable name=my-snippet
obsidian snippet:disable name=my-snippet
```

### Obsidian Sync同步
```bash
obsidian sync:status
# ...
obsidian sync off
obsidian sync on
# ...
obsidian sync:history file="项目计划"
# ...
obsidian sync:restore file="项目计划" version=2
# ...
obsidian sync:deleted
```

### 文件历史与版本对比
```bash
obsidian history file="项目计划"
# ...
obsidian history:read file="项目计划" version=1
# ...
obsidian history:restore file="项目计划" version=2
# ...
obsidian diff file="项目计划" from=2 to=1
```

### 开发者工具
```bash
obsidian devtools
# ...
obsidian dev:console
# ...
obsidian dev:errors
# ...
obsidian eval code="app.vault.getFiles().length"
# ...
obsidian dev:screenshot path=screenshot.png
# ...
obsidian dev:dom selector=".workspace-leaf"
# ...
obsidian dev:css selector=".mod-active" prop=background
# ...
obsidian dev:mobile on/off
# ...
obsidian dev:debug on/off
```

### 工作区与导航
```bash
obsidian workspace
# ...
obsidian workspace:save name="编码模式"
# ...
obsidian workspace:load name="编码模式"
# ...
obsidian tabs
# ...
obsidian tab:open file=笔记
# ...
obsidian random
obsidian random folder=收件箱 newtab
# ...
obsidian unique
# ...
obsidian wordcount file=笔记
```

### 命令面板与快捷键
```bash
obsidian commands
# ...
obsidian commands filter=editor
# ...
obsidian command id=editor:toggle-bold
# ...
obsidian hotkeys
```

### TUI交互模式
```bash
obsidian
```

TUI快捷键一览：

| 类别 | 快捷键 | 功能 |
|:------:|--------|:-------|
| 导航 | Ctrl+B/F | 光标左移/右移 |
| 导航 | Ctrl+A/E | 行首/行尾 |
| 编辑 | Ctrl+U | 删除至行首 |
| 编辑 | Ctrl+K | 删除至行尾 |
| 补全 | Tab/↓ | 确认补全 |
| 补全 | Shift+Tab/Esc | 退出补全 |
| 历史 | Ctrl+P/N | 上一条/下一条 |
| 历史 | Ctrl+R | 反向搜索历史 |
| 其他 | Enter | 执行命令 |
| 其他 | Ctrl+L | 清屏 |
| 其他 | Ctrl+C/D | 退出TUI |

## 常见问题

### Q1: 插件安装后未生效？
安装时添加`enable`标志：`obsidian plugin:install id=插件名 enable`。若已安装但未启用，使用`plugin:enable id=插件名`单独启用.
### Q2: Sync恢复文件时选择哪个版本？
先执行`sync:history file=文件名`查看版本列表和时间戳，确认目标版本后执行`sync:restore file=文件名 version=版本号`.
### Q3: eval命令执行报错？
`eval`执行的是Obsidian内部JavaScript API，需确保代码语法正确。常见用法：`app.vault.getFiles()`获取文件列表，`app.workspace.getActiveFile()`获取当前文件。复杂表达式建议先在开发者控制台测试.
### Q4: TUI模式中文输入异常？
TUI模式依赖终端的输入处理。若中文输入异常，尝试使用支持IME的现代终端（如iTerm2、Windows Terminal），或在非TUI模式下使用带引号的参数传递中文内容.
### Q5: 主题安装后界面未更新？
安装时添加`enable`标志：`theme:install name=主题名 enable`。若已安装，使用`theme:set name=主题名`切换激活主题.
### Q6: diff命令显示的版本号含义？
`diff file=文件 from=2 to=1`表示对比版本2和版本1的差异。版本号越大表示越新，通过`history file=文件`可查看完整版本列表.
### Q7: 工作区保存后加载时布局错乱？
工作区保存的是标签页和面板布局的快照。若加载时出现错乱，可能是因为相关文件已被移动或删除。确保引用的文件路径有效后再加载工作区.
### Q8: 截图命令保存的文件在哪里？
`dev:screenshot path=路径`中指定的路径为保存位置。建议使用绝对路径确保文件可找到，如`path=/tmp/screenshot.png`.
### Q9: commands列表太长如何筛选？
使用`commands filter=关键词`过滤命令，如`commands filter=editor`只显示编辑器相关命令.
### Q10: 多Vault环境下如何切换操作的库？
通过`vault`参数指定：`obsidian vault="库名" <命令>`。也可以在TUI模式中通过环境变量设置默认库.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
- 数据本地存储，不支持多设备自动同步
- 免费版有存储容量限制，大量笔记可能影响检索性能
- 依赖Agent平台的LLM能力进行内容理解与组织
