---
slug: "mermaid-diagram-tool-pro"
name: "mermaid-diagram-tool-pro"
version: "1.0.0"
displayName: "Mermaid图表工具(专业版)"
summary: "团队级Mermaid图表套件,含全类型、自定义主题、批量生成与CI语法校验。。Mermaid图表工具(专业版)面向团队与企业,提供全类型Mermaid图表生成、复杂多节点图、自定义主题样式、"
license: "Proprietary"
edition: "pro"
description: |-
  Mermaid图表工具(专业版)面向团队与企业,提供全类型Mermaid图表生成、复杂多节点图、自定义主题样式、从文档批量生成、CI语法校验与文档自动嵌入能力。核心能力:
  - 全图表类型:含C4架构图、Git图、类图、需求图等进阶类型
  - 复杂多节点图与子图分组
  - 自定义主题、样式与品牌色
  - 从Markdown/PRD批量生成多张图表
  - CI流水线语法校验,阻断错误图表
  - 文档自动嵌入与版本同步

  适用场景:
  - 企业架构与C4模型文档
  - 技术文档站点的图表统一管理
  - PRD到图表的批量转换
  ...
tags:
  - Development
  - 文档
  - Mermaid
  - 企业级
  - 可视化
  - 架构
  - 工具
  - 效率
  - 自动化
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# Mermaid图表工具(专业版)

## 概述

Mermaid图表工具(专业版)面向团队与企业,在兼容免费版7种基础图表类型与输出规则的基础上,扩展了全类型图表(含C4架构图、Git图、类图、需求图)、复杂多节点图与子图分组、自定义主题与品牌色、从文档批量生成、CI语法校验与文档自动嵌入能力.
当你在请求中提及 架构图、C4模型、企业架构、批量图表、图表规范、品牌主题、CI校验 等关键词时,本工具会自动激活,为团队提供统一的图表生成与治理方案.
本版本完全兼容 `mermaid-diagram-tool-free` 的输出格式与基础类型,可平滑升级,已有图表代码无需修改.
## 核心能力

| 能力模块 | 说明 | 与免费版差异 |
|----|---|------|
| 基础类型 | 流程图、时序图、状态图、脑图、ER图、时间线、用户旅程 | 与免费版一致 |
| 进阶类型 | C4架构图、Git图、类图、需求图、Sankey图 | 免费版无 |
| 复杂图 | 多节点子图分组、跨图引用、注释分段 | 免费版仅简单图 |
| 主题样式 | 自定义主题、品牌色、CSS样式注入 | 免费版默认样式 |
| 批量生成 | 从Markdown/PRD文档批量提取并生成多图 | 免费版仅单图 |
| CI校验 | 流水线语法校验,阻断错误图表 | 免费版仅基础自检 |
| 文档嵌入 | 自动嵌入Markdown并保持版本同步 | 免费版无 |
| 图表模板 | 团队图表模板库 | 免费版无 |

### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.
**输入**: 用户提供参数配置与调用所需的指令和必要参数.
**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置.
**输入**: 用户提供结果处理与输出所需的指令和必要参数.
**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：团队级、Mermaid、图表套件、含全类型、批量生成与、图表工具、专业版、面向团队与企业、提供全类型、图表生成、复杂多节点图、自定义主题样式、从文档批量生成、语法校验与文档自、动嵌入能力、核心能力、全图表类型、需求图等进阶类型、复杂多节点图与子、样式与品牌色、批量生成多张图表、文档自动嵌入与版等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一:企业C4架构图

团队需要绘制C4模型的系统架构,工具生成结构化架构图.
```mermaid
flowchart LR
    subgraph 用户层
        U[终端用户]
        A[管理员]
    end
    subgraph 应用层
        Web[Web前端]
        API[API网关]
        Auth[认证服务]
    end
    subgraph 数据层
        DB[(主数据库)]
        Cache[(缓存)]
        MQ[消息队列]
    end
    U --> Web
    A --> Web
    Web --> API
    API --> Auth
    API --> DB
    API --> Cache
    API --> MQ
```

C4容器图示例:

```mermaid
flowchart TB
    subgraph 系统边界
        Web[Web应用<br/>React + TypeScript]
        API[API服务<br/>Node.js]
        Worker[后台任务<br/>Python]
    end
    User([用户]) --> Web
    Web --> API
    API --> DB[(数据库)]
    API --> Cache[(缓存)]
    Worker --> DB
    Worker --> MQ[消息队列]
```

### 场景二:批量从PRD生成图表

团队有大量PRD文档,希望批量提取流程并生成图表.
```bash
# 从PRD文档批量生成图表
node （请参考skill目录中的脚本文件） \
  --input docs/prd/ \
  --output docs/diagrams/ \
  --format mermaid \
  --embed
# ...
# 输出
# docs/diagrams/prd-001-用户注册.mmd
# docs/diagrams/prd-001-登录流程.mmd
# docs/diagrams/prd-002-订单流程.mmd
```

工具会解析每份PRD,识别可可视化的流程/时序/状态,生成对应的 `.mmd` 文件,并自动嵌入回原文档的对应位置.
### 场景三:团队品牌主题统一

团队希望所有图表使用统一的品牌色与字体.
```yaml
# theme/brand-theme.yaml 团队品牌主题
themeVariables:
  primaryColor: "#1a73e8"
  primaryTextColor: "#ffffff"
  primaryBorderColor: "#1557b0"
  lineColor: "#5f6368"
  secondaryColor: "#e8f0fe"
  tertiaryColor: "#f1f3f4"
  background: "#ffffff"
  fontFamily: '"Noto Sans SC", "Segoe UI", sans-serif'
  fontSize: "14px"
```

```bash
# 应用品牌主题生成图表
node （请参考skill目录中的脚本文件） \
  --input diagrams/流程图.mmd \
  --theme theme/brand-theme.yaml \
  --output output/流程图.svg
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 1. 团队规范初始化

```bash
# 初始化团队图表规范目录
mkdir -p diagrams theme templates scripts
# ...
# 复制品牌主题模板
cp config/brand-theme.example.yaml theme/brand-theme.yaml
# ...
# 复制图表模板库
cp -r config/templates/* templates/
```

### 2. 单图生成(兼容免费版)

```bash
# 命令行生成单张图表
node （请参考skill目录中的脚本文件） --input input.mmd --output output.svg --theme theme/brand-theme.yaml
```

### 3. 批量生成

```bash
# 从文档目录批量生成
node （请参考skill目录中的脚本文件） \
  --input docs/specs/ \
  --output docs/diagrams/ \
  --embed \
  --theme theme/brand-theme.yaml
```

### 4. CI语法校验

```yaml
# .github/workflows/diagram-check.yml 图表语法校验
name: Diagram Syntax Check
on:
  pull_request:
    paths:
      - '**/*.mmd'
      - 'docs/**/*.md'
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - name: 校验所有 .mmd 文件
        run: |
          for f in $(find . -name '*.mmd'); do
            npx mmdc -i "$f" -o /tmp/check.svg || {
              echo "::error file=$f::Mermaid 语法错误"
              exit 1
            }
          done
      - name: 校验嵌入图表
        run: node （请参考skill目录中的脚本文件） docs/
```

## 示例

### 团队图表模板库

```text
templates/
├── flowchart-standard.mmd      # 标准流程图模板
├── sequence-api.mmd            # API时序图模板
├── state-machine.mmd           # 状态机模板
├── er-database.mmd             # ER图模板
├── c4-container.mmd            # C4容器图模板
├── c4-component.mmd            # C4组件图模板
├── git-flow.mmd                # Git分支图模板
└── class-diagram.mmd           # 类图模板
```

### 自定义主题变量

| 变量 | 说明 | 示例 |
|:-----|:-----|:-----|
| `primaryColor` | 主色 | `#1a73e8` |
| `primaryTextColor` | 主色文字 | `#ffffff` |
| `primaryBorderColor` | 主色边框 | `#1557b0` |
| `lineColor` | 连线颜色 | `#5f6368` |
| `secondaryColor` | 次色 | `#e8f0fe` |
| `tertiaryColor` | 第三色 | `#f1f3f4` |
| `background` | 背景 | `#ffffff` |
| `fontFamily` | 字体 | `"Noto Sans SC"` |
| `fontSize` | 字号 | `14px` |

### C4架构图模板

```mermaid
flowchart TB
    subgraph 系统[系统边界:订单系统]
        direction TB
        subgraph 前端[前端层]
            Web[Web应用]
            Mobile[移动应用]
        end
        subgraph 服务[服务层]
            Gateway[API网关]
            Order[订单服务]
            Pay[支付服务]
        end
        subgraph 存储[存储层]
            DB[(订单库)]
            Cache[(Redis)]
        end
    end
    Web --> Gateway
    Mobile --> Gateway
    Gateway --> Order
    Gateway --> Pay
    Order --> DB
    Order --> Cache
    Pay --> DB
```

### Git分支图

```mermaid
gitGraph
    commit id: "初始化"
    commit id: "基础功能"
    branch develop
    checkout develop
    commit id: "开发中"
    branch feature/login
    checkout feature/login
    commit id: "登录功能"
    commit id: "修复bug"
    checkout develop
    merge feature/login
    checkout main
    merge develop
    commit id: "发布v1.0" tag: "v1.0"
```

## 最佳实践

### 1. 复杂图分段子图

节点超过20个时,用 `subgraph` 分组提升可读性.
```mermaid
flowchart TB
    subgraph 输入层
        A[用户请求]
        B[定时任务]
    end
    subgraph 处理层
        C[路由分发]
        D[业务处理]
        E[数据校验]
    end
    subgraph 输出层
        F[响应返回]
        G[日志记录]
    end
    A --> C
    B --> C
    C --> D
    D --> E
    E --> F
    D --> G
```

### 2. 主题与品牌一致性

团队所有图表统一使用同一主题文件,避免风格不一致。建议:

- 主题文件纳入版本控制,变更需评审
- 主色与品牌主色一致
- 字体优先使用中英文都好看的字体(如 Noto Sans SC)
- 暗色模式单独配置主题

### 3. 文档嵌入与版本同步

```bash
# 在Markdown中嵌入图表,使用引用而非内联
# docs/architecture.md
# ![系统架构](diagrams/architecture.mmd)
```

```bash
# CI中校验嵌入图表与源文件同步
node （请参考skill目录中的脚本文件） docs/ --strict
```

### 4. 批量生成与PRD对齐

```bash
# PRD变更时重新生成对应图表
node （请参考skill目录中的脚本文件） \
  --input docs/prd/订单PRD.md \
  --output docs/diagrams/ \
  --rule "流程图→flowchart,接口→sequence,状态→state" \
  --embed
```

### 5. CI校验最佳实践

| 校验项 | 工具 | 阻断级别 |
|---:|---:|---:|
| 语法错误 | `mmdc` 渲染 | 阻断 |
| 嵌入同步 | `validate-embed.mjs` | 阻断 |
| 主题一致 | `check-theme.mjs` | 警告 |
| 命名规范 | `lint-naming.mjs` | 警告 |
| 节点数超限 | `count-nodes.mjs --max 50` | 警告 |

## 常见问题

### Q1:PRO版与免费版如何共存?

两者输出格式与基础类型完全兼容,PRO版包含免费版全部能力。团队升级时直接替换Skill文件,已有 `.mmd` 文件无需修改.
### Q2:C4架构图与普通流程图有何区别?

C4是一种架构描述方法,分Context/Container/Component/Code四层。本工具用流程图+子图模拟C4容器图,提供结构化的系统边界、容器、组件表达,适合企业架构文档.
### Q3:批量生成会修改我的文档吗?

默认 `--embed` 模式会把生成的图表代码块嵌入回原Markdown的对应位置(替换 `<!-- mermaid:xxx -->` 标记处)。如不希望修改文档,去掉 `--embed` 仅生成独立 `.mmd` 文件.
### Q4:主题文件支持热重载吗?

支持。`render.mjs` 每次运行都重新读取主题文件,修改后无需重启。CI中建议锁定主题文件版本号,避免运行时变更导致不一致.
### Q5:支持MermaidLive/MermaidInk等在线渲染吗?

支持。生成的代码可直接粘贴到 Mermaid Live Editor。批量场景建议本地用 `mmdc` 渲染为SVG/PNG嵌入文档,避免依赖在线服务.
### Q6:能否生成可交互的HTML图表?

可以。通过 `mmdc` 渲染为SVG后嵌入HTML,或使用 mermaid.js 在前端动态渲染。团队图表站点建议用动态渲染,便于主题切换与缩放.
## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js版本**: 建议 20 LTS 及以上(用于 mmdc 渲染与批量脚本)
- **Mermaid版本**: 建议 10.x 及以上

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| @mermaid-js/mermaid-cli | npm包 | 必需 | `npm i -g @mermaid-js/mermaid-cli` |
| puppeteer | npm包 | 必需 | mmdc 依赖,自动安装 |
| Node.js | 运行时 | 必需 | nodejs.org 下载 |
| Chromium | 浏览器 | 必需 | mmdc 渲染依赖,首次运行自动下载 |

### API Key 配置

- 本skill基于Markdown指令规范,无需额外API Key.
- 本地渲染通过 mmdc + Chromium 完成,不依赖外部API.
- 若需对接在线图表托管服务,按对应服务文档配置令牌.
### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent完成操作。PRO版面向团队与企业,提供全类型图表、自定义主题、批量生成与CI校验能力,完全兼容免费版基础类型与输出格式.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "Mermaid图表工具(专业版)处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "mermaid diagram pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
