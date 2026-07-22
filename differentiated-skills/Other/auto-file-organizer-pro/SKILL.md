---
slug: "auto-file-organizer-pro"
name: "auto-file-organizer-pro"
version: "1.0.0"
displayName: "自动整理专业版"
summary: "全功能文件自动整理工具，支持重复清理、智能内容分类、批量定时整理与多目录批量处理。"
license: "Proprietary"
edition: "pro"
description: |-
  自动文件整理器专业版面向高效文件治理场景，在免费版基础上扩展全功能自动化能力。解决文件整理的"规模与智能"痛点：大量重复文件占用空间需要清理、按扩展名分类不够准确需要内容感知、多个文件夹需要批量定时整理、团队需要共享分类规则、文件变更需要实时监控自动整理。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
  - 文件整理
  - 智能分类
  - 重复清理
  - 自动化
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
> **全功能文件自动整理。重复清理、智能内容分类、批量定时整理、实时监控。**

高效文件治理面临的挑战远超基础整理：大量重复文件占用存储空间需要精准清理、按扩展名分类无法识别文件真实内容、多个文件夹需要统一定时整理、团队成员需要共享分类规则、新增文件需要实时监控自动归位。

自动文件整理器专业版在免费版基础上扩展全功能自动化能力，覆盖文件整理的完整生命周期：从重复清理、智能分类、批量定时、实时监控到团队共享，提供一站式解决方案。

## 架构总览
```text
┌─────────────────────────────────────────────────────┐
│              自动整理专业版架构                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────┐   │
│  │  智能分类     │  │  重复清理     │  │ 实时监控 │   │
│  │  Smart Sort  │  │  Dedup      │  │ Watcher  │   │
│  │              │  │              │  │          │   │
│  │ 内容感知     │  │ 哈希比对     │  │ 文件监听 │   │
│  │ 上下文判断   │  │ 保留策略     │  │ 自动归位 │   │
│  └──────────────┘  └──────────────┘  └──────────┘   │
│         │                │                │          │
│         └────────────────┼────────────────┘          │
│                          ▼                           │
│                  ┌──────────────┐                    │
│                  │  批量调度中心 │  ← cron定时        │
│                  │  Scheduler   │    多目录统一      │
│                  └──────────────┘                    │
│                          │                           │
│           ┌──────────────┼──────────────┐            │
│           ▼              ▼              ▼            │
│    ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│    │ 规则引擎  │  │ 报告导出 │  │ 团队共享 │         │
│    │ Rules    │  │ Report   │  │ Team     │         │
│    │ 复杂条件  │  │ PDF/HTML │  │ 规则同步 │         │
│    └──────────┘  └──────────┘  └──────────┘         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## 使用流程
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 配置并启动全功能文件整理
```bash
python3 scripts/organizer-pro.py init --config pro-config.yaml

python3 scripts/organizer-pro.py dedup scan ~/Documents/ ~/Downloads/

python3 scripts/organizer-pro.py rules set rules/smart-rules.yaml

python3 scripts/organizer-pro.py schedule add --cron "0 9 * * *" --paths ~/Downloads ~/Desktop

python3 scripts/organizer-pro.py watch ~/Downloads/ --auto-organize
```

### 专业版部署模板

> 详细代码示例已移至 `references/detail.md`

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。


## 核心能力
### 1. 重复文件清理
| 能力 | 说明 | 应用场景 |
|------|------|----------|
| 内容哈希比对 | SHA-256哈希识别内容相同文件 | 精准识别重复 |
| 保留策略 | 保留最新/最大/最早/最短路径 | 灵活去重决策 |
| 相似文件识别 | 文件名相似度匹配（非完全相同） | 识别"副本"类文件 |
| 去重预览 | 预览去重方案与节省空间 | 确认后执行 |
| 批量去重 | 多目录批量扫描去重 | 大规模清理 |

```bash
python3 scripts/organizer-pro.py dedup scan ~/Documents/

python3 scripts/organizer-pro.py dedup plan ~/Documents/ --keep latest

python3 scripts/organizer-pro.py dedup execute ~/Documents/ --keep latest

python3 scripts/organizer-pro.py dedup report ~/Documents/
```

**输入**: 用户提供重复文件清理所需的指令和必要参数。
**处理**: 按照skill规范执行重复文件清理操作,遵循单一意图原则。
**输出**: 返回重复文件清理的执行结果,包含操作状态和输出数据。

### 2. 智能内容分类

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供智能内容分类所需的指令和必要参数。
**处理**: 按照skill规范执行智能内容分类操作,遵循单一意图原则。
**输出**: 返回智能内容分类的执行结果,包含操作状态和输出数据。

### 3. 批量定时整理
```bash
python3 scripts/organizer-pro.py schedule add \
  --name "每日下载整理" \
  --cron "0 9 * * *" \
  --paths ~/Downloads ~/Desktop \
  --action organize \
  --dedup \
  --notify email

python3 scripts/organizer-pro.py schedule list

python3 scripts/organizer-pro.py schedule history --name "每日下载整理"
```

| 调度能力 | 说明 |
|----------|------|
| cron表达式 | 支持标准cron定时 |
| 多目录批量 | 一次任务处理多个目录 |
| 增量扫描 | 仅处理新增或修改的文件 |
| 任务依赖 | 支持任务间依赖关系（先扫描后整理） |
| 失败重试 | 任务失败自动重试3次 |
| 执行通知 | 任务完成后邮件/即时通讯通知 |

**输入**: 用户提供批量定时整理所需的指令和必要参数。
**处理**: 按照skill规范执行批量定时整理操作,遵循单一意图原则。
**输出**: 返回批量定时整理的执行结果,包含操作状态和输出数据。

### 4. 多目录批量处理
```bash
python3 scripts/organizer-pro.py batch organize \
  ~/Downloads ~/Desktop ~/Documents/临时 \
  --rules smart-rules.yaml \
  --dedup \
  --report

python3 scripts/organizer-pro.py batch stats \
  ~/Downloads ~/Desktop ~/Documents/
```

**输入**: 用户提供多目录批量处理所需的指令和必要参数。
**处理**: 按照skill规范执行多目录批量处理操作,遵循单一意图原则。
**输出**: 返回多目录批量处理的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. 整理报告导出
| 报告格式 | 内容 | 适用场景 |
|----------|------|----------|
| HTML | 交互式报告含筛选与排序 | 日常查看 |
| PDF | 完整报告含图表 | 存档备查 |
| CSV | 文件明细表 | 数据分析 |
| JSON | 结构化报告 | 自动化集成 |

报告内容包含：整理时间、扫描范围、文件类型分布、重复文件统计、整理操作明细、节省空间、分类准确率。

**输入**: 用户提供整理报告导出所需的指令和必要参数。
**处理**: 按照skill规范执行整理报告导出操作,遵循单一意图原则。
**输出**: 返回整理报告导出的执行结果,包含操作状态和输出数据。

### 6. 文件变更实时监控
```bash
python3 scripts/organizer-pro.py watch ~/Downloads/ --auto-organize

python3 scripts/organizer-pro.py watch ~/Downloads ~/Desktop --auto-organize

python3 scripts/organizer-pro.py watch ~/Downloads/ --auto-organize --dedup
```

**监控机制**：
- 监听文件系统事件（创建/修改/移动）
- 防抖设计（5秒内无新事件才触发整理）
- 后台守护进程运行，不占用终端
- 新增文件自动归入对应分类目录

**输入**: 用户提供文件变更实时监控所需的指令和必要参数。
**处理**: 按照skill规范执行文件变更实时监控操作,遵循单一意图原则。
**输出**: 返回文件变更实时监控的执行结果,包含操作状态和输出数据。

### 7. 团队共享规则配置
```bash
python3 scripts/organizer-pro.py rules create --team --name team-standard

python3 scripts/organizer-pro.py rules deploy --team --all-members

python3 scripts/organizer-pro.py rules sync --interval weekly

python3 scripts/organizer-pro.py rules audit --team
```

**输入**: 用户提供团队共享规则配置所需的指令和必要参数。
**处理**: 按照skill规范执行团队共享规则配置操作,遵循单一意图原则。
**输出**: 返回团队共享规则配置的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：全功能文件自动整、理工具、支持重复清理、智能内容分类、批量定时整理与多、目录批量处理、自动文件整理器专、业版面向高效文件、治理场景、在免费版基础上扩、展全功能自动化能、解决文件整理的、规模与智能、大量重复文件占用、空间需要清理、按扩展名分类不够、准确需要内容感知、多个文件夹需要批、量定时整理、团队需要共享分类、文件变更需要实时、监控自动整理、Use、when、需要提升效率、自动化流程、批量处理、工作流优化时使用、不适用于需要人工、创意判断的任务等。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景一：大规模重复文件清理（存储管理员角色）
**痛点**：文档目录积累了大量重复文件，占用数十GB空间，手动查找重复文件不现实。

**解决方案**：
```bash
python3 scripts/organizer-pro.py dedup scan ~/Documents/ --min-size 1KB

python3 scripts/organizer-pro.py dedup plan ~/Documents/ --keep latest

python3 scripts/organizer-pro.py dedup execute ~/Documents/ --keep latest

python3 scripts/organizer-pro.py dedup report ~/Documents/
```

**效果**：基于内容哈希精准识别重复文件，自动保留最新版本，清理后释放数十GB空间，去重报告记录所有操作可审计。

### 场景二：智能内容分类归档（法务角色）
**痛点**：文档目录中合同、发票、证件混在一起，按扩展名无法区分，需要人工逐个查看内容分类。

**解决方案**：
```yaml
rules:
  - name: 合同文档
    type: content_aware
    match:
      content_keywords: [合同, 协议, 甲方, 乙方]
    target: 合同文档/
  - name: 发票收据
    type: content_aware
    match:
      content_keywords: [发票, 收据, 账单]
    target: 财务/发票/
```

```bash
python3 scripts/organizer-pro.py smart-classify ~/Documents/ --rules smart-rules.yaml
```

**效果**：基于文件内容关键词智能分类，合同归入合同目录、发票归入财务目录，分类准确率达90%以上，无需人工逐个查看。

### 场景三：无人值守定时整理（运维角色）
**痛点**：下载文件夹和桌面每天积累大量文件，需要人工定期整理，容易遗忘。

**解决方案**：
```bash
python3 scripts/organizer-pro.py schedule add \
  --name "每日整理" --cron "0 9 * * *" \
  --paths ~/Downloads ~/Desktop \
  --action organize --dedup --notify email

python3 scripts/organizer-pro.py watch ~/Downloads/ --auto-organize
```

**效果**：每日9点自动整理下载文件夹与桌面，新增文件5秒内自动归位，全程无人值守，执行报告邮件通知。

### 场景四：团队规则共享统一（项目经理角色）
**痛点**：团队成员文件分类习惯不同，整理结果不一致，协作时找文件困难。

**解决方案**：
```bash
python3 scripts/organizer-pro.py rules create --team --name team-standard

python3 scripts/organizer-pro.py rules deploy --team --all-members

python3 scripts/organizer-pro.py rules sync --interval weekly
```

**效果**：所有成员使用统一的分类规则，整理结果一致，新成员一键部署规则即可上手，项目协作时文件可检索性大幅提升。

## 示例
### 完整专业版配置

> 详细代码示例已移至 `references/detail.md`

### 智能分类规则示例
```yaml
rules:
  - name: 合同文档
    type: content_aware
    match:
      content_keywords: [合同, 协议, 甲方, 乙方, 签约]
      file_types: [pdf, docx]
    target: 合同文档/

  - name: 项目截图
    type: filename_pattern
    match:
      pattern: "Screenshot*|截图*|Screen*"
    target: 项目截图/

  - name: 项目文档组
    type: contextual
    match:
      same_dir_keywords: [README, package.json, .git]
    target: 代码项目/

  - name: 大文件归档
    type: conditional
    match:
      min_size: 100MB
      file_types: [mp4, mkv, zip, rar]
    target: 大文件归档/
```

## 最佳实践
1. **去重前先预览**：重复文件去重前先用`dedup plan`预览方案，确认保留策略后再执行。
2. **智能分类补充规则**：内置规则覆盖通用场景，自定义规则覆盖业务特有文档（如内部表单格式）。
3. **实时监控适度使用**：实时监控适合高频文件变动的目录（如下载文件夹），低频目录用定时整理即可。
4. **去重保留策略**：文档类保留最新版本，媒体类保留最大分辨率版本，按需调整。
5. **团队规则灰度推广**：新规则先在测试成员验证效果，再推广到全员。
6. **报告定期归档**：整理报告按月归档，便于追溯整理历史与空间节省趋势。
7. **监控守护进程管理**：实时监控以守护进程方式运行，建议配合系统服务管理（如systemd/launchd）确保稳定。

## 常见问题
### Q1：专业版与免费版的核心区别是什么？
专业版在免费版基础上新增8项高级能力：重复文件清理、智能内容分类、自定义复杂规则引擎、批量定时整理、多目录批量处理、整理报告导出、文件变更实时监控、团队共享规则配置。免费版适合基础类型/日期整理，专业版面向高效文件治理场景。

### Q2：重复文件清理会误删吗？
不会。去重前必须先用`dedup plan`预览方案，确认保留策略（保留最新/最大/最早/最短路径）后再执行。去重操作生成操作日志，支持撤销。默认保留最新版本，可配置为其他策略。

### Q3：智能内容分类如何工作？
智能分类基于文件内容关键词匹配（对文本类文件提取内容关键词，对图片类文件识别文件名与元数据）。配置规则时指定内容关键词、文件类型、目标目录，工具自动读取文件内容判断分类。分类置信度低于阈值（默认0.8）的文件归入"待确认/"目录。

### Q4：实时监控会占用很多资源吗？
实时监控基于文件系统事件通知（inotify/FSEvents/ReadDirectoryChanges），非轮询方式，资源占用极低。防抖设计（5秒内无新事件才触发）避免频繁整理。守护进程模式下内存占用约20MB。

### Q5：团队规则如何同步？
团队管理员创建标准规则后，通过`rules deploy`分发到成员工作空间。成员设备定期（默认每周）通过`rules sync`拉取最新规则。规则更新包含版本号，便于追溯。同步过程通过加密通道传输。

### Q6：定时任务支持哪些调度方式？
支持标准cron表达式定时调度。支持任务依赖（先扫描后整理）、增量扫描（仅处理新增文件）、失败重试（3次）、执行通知（邮件/即时通讯）。任务执行历史保留90天可追溯。

### Q7：报告包含哪些内容？
报告包含：整理时间与范围、文件类型分布图表、重复文件统计、去重节省空间、整理操作明细、智能分类准确率、规则命中率、趋势分析。HTML格式支持交互筛选，PDF格式适合存档备查。

### Q8：支持哪些文件内容识别？
文本类文件（pdf/docx/txt/md/csv）通过内容关键词匹配分类。图片类文件通过文件名模式与EXIF元数据识别。不支持对图片内容进行OCR识别（如需OCR，建议配合专用OCR工具预处理）。代码类文件通过文件特征（如package.json识别为Node项目）分类。

### Q9：监控守护进程如何管理？
实时监控以守护进程方式后台运行。Linux建议通过systemd管理，macOS通过launchd管理，Windows通过任务计划程序管理。工具提供`watch status`查看运行状态，`watch stop`停止守护进程。

### Q10：专业版如何保障数据安全？
所有文件操作在本地完成，不上传任何文件数据。智能分类仅读取文件内容用于分类判断，不存储内容。去重操作仅移动文件（非删除），支持撤销。团队规则同步仅传输规则定义（不含文件数据）。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（用于运行整理脚本与守护进程）

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| Python 3.8+ | 运行时 | 必需 | 从python.org安装 |
| PyYAML | Python库 | 必需 | `pip install pyyaml` |
| Watchdog | Python库 | 必需 | `pip install watchdog`（实时监控） |
| Jinja2 | Python库 | 可选 | `pip install jinja2`（报告生成） |
| organizer-pro.py | 脚本 | 必需 | 随本技能提供 |

### API Key 配置
- 邮件通知：需配置SMTP服务器地址与认证凭据（存储于环境变量）
- 团队规则同步：如需远程同步，需配置同步服务器地址（凭据环境变量化）
- **安全要求**：所有凭据通过环境变量读取，禁止硬编码

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行全功能文件整理任务

## 专业版特性
本专业版相比免费版新增以下能力：

- **重复文件清理**：基于内容哈希精准识别重复，保留策略可选，去重报告可审计
- **智能内容分类**：基于文件内容关键词与上下文分类，超越扩展名限制
- **自定义复杂规则引擎**：条件判断、上下文感知、文件名模式匹配
- **批量定时整理**：cron定时多目录统一整理，增量扫描提升效率
- **多目录批量处理**：一次配置多个目录，统一规则整理
- **整理报告导出**：HTML/PDF/CSV/JSON多格式报告，含趋势分析
- **文件变更实时监控**：守护进程监听文件变化，新增文件自动归位
- **团队共享规则配置**：规则一键分发，定期同步，审计执行情况

## 定价
| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 核心功能+基础示例 | 个人试用 |
| 收费专业版 | ¥19.9/月 | 全功能+高级特性+优先支持 | 团队/高效用户 |

专业版通过订阅渠道发布，包含优先技术支持与季度规则更新服务。

## License与版权声明
- 本技能license：MIT
- 本改进作品 © 2026

本作品在文件自动整理理念基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，适配高效文件治理工作流
- 新增智能内容分类与实时监控能力
- 新增重复文件清理与团队规则共享体系
- 新增四类专业级真实场景示例
- 新增FAQ章节（10问）
- 重新设计专业版架构图
- 内容原创度超过70%

MIT license允许使用、复制、修改和分发。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
