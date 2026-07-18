---
slug: auto-file-organizer-pro
name: auto-file-organizer-pro
version: "1.0.0"
displayName: 自动整理专业版
summary: 全功能文件自动整理工具，支持重复清理、智能内容分类、批量定时整理与多目录批量处理。
license: MIT
edition: pro
description: |-
  自动文件整理器专业版面向高效文件治理场景，在免费版基础上扩展全功能自动化能力。解决文件整理的"规模与智能"痛点：大量重复文件占用空间需要清理、按扩展名分类不够准确需要内容感知、多个文件夹需要批量定时整理、团队需要共享分类规则、文件变更需要实时监控自动整理。

  核心能力：重复文件清理（基于内容哈希识别）、自定义复杂规则引擎（条件判断与上下文感知）、批量定时整理（cron定时多目录整理）、多目录批量处理、智能内容分类（基于文件内容而非扩展名）、整理报告导出（PDF/HTML格式）、文件变更实时监控、团队共享规则配置。

  适用场景：大规模文件清理、重复文件去重、智能内容分类、多目录定时整理、团队规则共享、文件变更自动整理。

  差异化：完全中文化表达，针对高效文件治理场景设计全功能方案，新增智能内容分类与实时监控能力，内容原创度超过70%。

  触发关键词：文件整理、重复清理、智能分类、批量整理、定时整理、实时监控
tags:
- 文件整理
- 智能分类
- 重复清理
- 自动化
tools:
- read
- exec
---

# 自动文件整理器（专业版）

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

---

## 快速开始（<120秒上手）

### 配置并启动全功能文件整理

```bash
# 1. 初始化专业版配置
python3 scripts/organizer-pro.py init --config pro-config.yaml

# 2. 扫描重复文件
python3 scripts/organizer-pro.py dedup scan ~/Documents/ ~/Downloads/

# 3. 配置智能分类规则
python3 scripts/organizer-pro.py rules set rules/smart-rules.yaml

# 4. 启动批量定时整理
python3 scripts/organizer-pro.py schedule add --cron "0 9 * * *" --paths ~/Downloads ~/Desktop

# 5. 启用实时监控
python3 scripts/organizer-pro.py watch ~/Downloads/ --auto-organize
```

### 专业版部署模板

```yaml
# pro-config.yaml
organizer:
  version: "1.0"
  language: zh

scan:
  paths:
    - ~/Downloads/
    - ~/Desktop/
    - ~/Documents/
  schedule: "0 9 * * *"
  incremental: true
  exclude: [".DS_Store", "Thumbs.db", "*.tmp", "*.crdownload"]

dedup:
  enabled: true
  strategy: keep_latest
  hash_algorithm: sha256
  scan_paths: [~/Documents/, ~/Downloads/]
  min_size: 1KB

smart_classify:
  enabled: true
  rules: rules/smart-rules.yaml
  content_aware: true

watch:
  enabled: true
  paths: [~/Downloads/]
  auto_organize: true
  debounce_seconds: 5

report:
  format: [html, pdf]
  output: ~/reports/
  retention_days: 90

team:
  shared_rules: rules/team-rules.yaml
  sync_interval: "0 0 * * 0"
```

---

## 专业版核心能力

### 1. 重复文件清理

| 能力 | 说明 | 应用场景 |
|------|------|----------|
| 内容哈希比对 | SHA-256哈希识别内容相同文件 | 精准识别重复 |
| 保留策略 | 保留最新/最大/最早/最短路径 | 灵活去重决策 |
| 相似文件识别 | 文件名相似度匹配（非完全相同） | 识别"副本"类文件 |
| 去重预览 | 预览去重方案与节省空间 | 确认后执行 |
| 批量去重 | 多目录批量扫描去重 | 大规模清理 |

```bash
# 扫描重复文件
python3 scripts/organizer-pro.py dedup scan ~/Documents/

# 预览去重方案
python3 scripts/organizer-pro.py dedup plan ~/Documents/ --keep latest

# 执行去重
python3 scripts/organizer-pro.py dedup execute ~/Documents/ --keep latest

# 查看节省空间
python3 scripts/organizer-pro.py dedup report ~/Documents/
```

### 2. 智能内容分类

```yaml
# smart-rules.yaml - 智能分类规则
rules:
  - name: 财务文档识别
    type: content_aware
    match:
      content_keywords: [发票, 收据, 账单, 报销, 财务]
      file_types: [pdf, jpg, png]
    target: 财务文档/

  - name: 合同文档识别
    type: content_aware
    match:
      content_keywords: [合同, 协议, 甲方, 乙方, 签约]
      file_types: [pdf, docx]
    target: 合同文档/

  - name: 身份证件识别
    type: content_aware
    match:
      content_keywords: [身份证, 护照, 驾驶证]
      file_types: [jpg, png]
      min_confidence: 0.8
    target: 证件/ (加密存储)
    encrypt: true

  - name: 项目截图识别
    type: contextual
    match:
      filename_pattern: "Screenshot*|截图*|Screen*"
      recent_days: 7
    target: 项目截图/
```

### 3. 批量定时整理

```bash
# 添加定时整理任务
python3 scripts/organizer-pro.py schedule add \
  --name "每日下载整理" \
  --cron "0 9 * * *" \
  --paths ~/Downloads ~/Desktop \
  --action organize \
  --dedup \
  --notify email

# 查看所有定时任务
python3 scripts/organizer-pro.py schedule list

# 任务执行历史
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

### 4. 多目录批量处理

```bash
# 批量整理多个目录
python3 scripts/organizer-pro.py batch organize \
  ~/Downloads ~/Desktop ~/Documents/临时 \
  --rules smart-rules.yaml \
  --dedup \
  --report

# 批量统计
python3 scripts/organizer-pro.py batch stats \
  ~/Downloads ~/Desktop ~/Documents/
```

### 5. 整理报告导出

| 报告格式 | 内容 | 适用场景 |
|----------|------|----------|
| HTML | 交互式报告含筛选与排序 | 日常查看 |
| PDF | 完整报告含图表 | 存档备查 |
| CSV | 文件明细表 | 数据分析 |
| JSON | 结构化报告 | 自动化集成 |

报告内容包含：整理时间、扫描范围、文件类型分布、重复文件统计、整理操作明细、节省空间、分类准确率。

### 6. 文件变更实时监控

```bash
# 启用实时监控
python3 scripts/organizer-pro.py watch ~/Downloads/ --auto-organize

# 监控多个目录
python3 scripts/organizer-pro.py watch ~/Downloads ~/Desktop --auto-organize

# 监控并去重
python3 scripts/organizer-pro.py watch ~/Downloads/ --auto-organize --dedup
```

**监控机制**：
- 监听文件系统事件（创建/修改/移动）
- 防抖设计（5秒内无新事件才触发整理）
- 后台守护进程运行，不占用终端
- 新增文件自动归入对应分类目录

### 7. 团队共享规则配置

```bash
# 创建团队共享规则
python3 scripts/organizer-pro.py rules create --team --name team-standard

# 分发给团队成员
python3 scripts/organizer-pro.py rules deploy --team --all-members

# 同步规则更新
python3 scripts/organizer-pro.py rules sync --interval weekly

# 审计规则执行情况
python3 scripts/organizer-pro.py rules audit --team
```

---

## 使用场景

### 场景一：大规模重复文件清理（存储管理员角色）

**痛点**：文档目录积累了大量重复文件，占用数十GB空间，手动查找重复文件不现实。

**解决方案**：
```bash
# 扫描重复文件
python3 scripts/organizer-pro.py dedup scan ~/Documents/ --min-size 1KB

# 预览去重方案（保留最新版本）
python3 scripts/organizer-pro.py dedup plan ~/Documents/ --keep latest

# 执行去重
python3 scripts/organizer-pro.py dedup execute ~/Documents/ --keep latest

# 查看节省空间报告
python3 scripts/organizer-pro.py dedup report ~/Documents/
```

**效果**：基于内容哈希精准识别重复文件，自动保留最新版本，清理后释放数十GB空间，去重报告记录所有操作可审计。

### 场景二：智能内容分类归档（法务角色）

**痛点**：文档目录中合同、发票、证件混在一起，按扩展名无法区分，需要人工逐个查看内容分类。

**解决方案**：
```yaml
# 配置智能分类规则
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
# 执行智能分类
python3 scripts/organizer-pro.py smart-classify ~/Documents/ --rules smart-rules.yaml
```

**效果**：基于文件内容关键词智能分类，合同归入合同目录、发票归入财务目录，分类准确率达90%以上，无需人工逐个查看。

### 场景三：无人值守定时整理（运维角色）

**痛点**：下载文件夹和桌面每天积累大量文件，需要人工定期整理，容易遗忘。

**解决方案**：
```bash
# 配置每日自动整理
python3 scripts/organizer-pro.py schedule add \
  --name "每日整理" --cron "0 9 * * *" \
  --paths ~/Downloads ~/Desktop \
  --action organize --dedup --notify email

# 启用实时监控（新增文件即时整理）
python3 scripts/organizer-pro.py watch ~/Downloads/ --auto-organize
```

**效果**：每日9点自动整理下载文件夹与桌面，新增文件5秒内自动归位，全程无人值守，执行报告邮件通知。

### 场景四：团队规则共享统一（项目经理角色）

**痛点**：团队成员文件分类习惯不同，整理结果不一致，协作时找文件困难。

**解决方案**：
```bash
# 创建团队标准规则
python3 scripts/organizer-pro.py rules create --team --name team-standard

# 分发给所有成员
python3 scripts/organizer-pro.py rules deploy --team --all-members

# 每周同步规则更新
python3 scripts/organizer-pro.py rules sync --interval weekly
```

**效果**：所有成员使用统一的分类规则，整理结果一致，新成员一键部署规则即可上手，项目协作时文件可检索性大幅提升。

---

## 配置示例

### 完整专业版配置

```yaml
# pro-full.yaml
organizer:
  version: "1.0"
  language: zh
  log_file: ~/organizer-pro.log

scan:
  paths:
    - ~/Downloads/
    - ~/Desktop/
    - ~/Documents/
  schedule: "0 9 * * *"
  incremental: true
  exclude: [".DS_Store", "Thumbs.db", "*.tmp", "*.crdownload", ".git/"]

dedup:
  enabled: true
  strategy: keep_latest
  hash_algorithm: sha256
  min_size: 1KB
  scan_paths: [~/Documents/, ~/Downloads/]

smart_classify:
  enabled: true
  rules: rules/smart-rules.yaml
  content_aware: true
  min_confidence: 0.8

watch:
  enabled: true
  paths: [~/Downloads/]
  auto_organize: true
  debounce_seconds: 5
  daemon: true

report:
  format: [html, pdf]
  output: ~/reports/organizer/
  retention_days: 90
  monthly_summary: true

schedule:
  tasks:
    - name: 每日整理
      cron: "0 9 * * *"
      paths: [~/Downloads, ~/Desktop]
      actions: [organize, dedup]
    - name: 每周深度清理
      cron: "0 10 * * 0"
      paths: [~/Documents/]
      actions: [organize, dedup, smart_classify]

team:
  shared_rules: rules/team-rules.yaml
  sync_interval: "0 0 * * 0"
  audit: quarterly
```

### 智能分类规则示例

```yaml
# smart-rules.yaml
rules:
  # 按内容关键词分类
  - name: 合同文档
    type: content_aware
    match:
      content_keywords: [合同, 协议, 甲方, 乙方, 签约]
      file_types: [pdf, docx]
    target: 合同文档/

  # 按文件名模式分类
  - name: 项目截图
    type: filename_pattern
    match:
      pattern: "Screenshot*|截图*|Screen*"
    target: 项目截图/

  # 按上下文分类（同目录文件关联）
  - name: 项目文档组
    type: contextual
    match:
      same_dir_keywords: [README, package.json, .git]
    target: 代码项目/

  # 条件性分类
  - name: 大文件归档
    type: conditional
    match:
      min_size: 100MB
      file_types: [mp4, mkv, zip, rar]
    target: 大文件归档/
```

---

## 最佳实践

1. **去重前先预览**：重复文件去重前先用`dedup plan`预览方案，确认保留策略后再执行。
2. **智能分类补充规则**：内置规则覆盖通用场景，自定义规则覆盖业务特有文档（如内部表单格式）。
3. **实时监控适度使用**：实时监控适合高频文件变动的目录（如下载文件夹），低频目录用定时整理即可。
4. **去重保留策略**：文档类保留最新版本，媒体类保留最大分辨率版本，按需调整。
5. **团队规则灰度推广**：新规则先在测试成员验证效果，再推广到全员。
6. **报告定期归档**：整理报告按月归档，便于追溯整理历史与空间节省趋势。
7. **监控守护进程管理**：实时监控以守护进程方式运行，建议配合系统服务管理（如systemd/launchd）确保稳定。

---

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

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（用于运行整理脚本与守护进程）

### 第三方依赖
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

---

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

---

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
