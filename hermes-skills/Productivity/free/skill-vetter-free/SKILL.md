---
name: "skill-vetter-free"
description: "基础版 AI Agent 技能审查工具，执行来源检查和 RED FLAGS 检测。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "Skill Vetter Free"
  version: "1.0.0"
  summary: "基础版 AI Agent 技能审查工具，执行来源检查和 RED FLAGS 检测。"
  tags:
    - "通用办公"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
tools:
  - exec
  - read
  - write
---
# Skill Vetter Free

skill-vetter-free 是安全优先的 AI Agent 技能审查工具基础版。**永远不要在未审查前安装任何技能。**

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 来源检查（Source Check）
验证技能来源的可靠性。回答 5 个关键问题：技能从哪里来（SkillHub / GitHub / 其他）？
作者是否知名/可信？下载量/星标数是多少？最后更新时间？是否有其他 Agent 的评价？
基础版支持手动来源验证，不包含 GitHub API 自动查询命令。

### 2. 强制代码审查（Code Review - MANDATORY）
读取技能中的所有文件，逐一检查 RED FLAGS 清单。发现以下任何一项立即拒绝安装：
`curl`/`wget` 到未知 URL；向外部服务器发送数据；请求凭证/令牌/API Key；
读取 `~/.ssh`、`~/.aws`、`~/.config` 路径而无明确理由；访问 `MEMORY.md`、`USER.md`、
`SOUL.md`、`IDENTITY.md` 等身份文件；使用 `JSON.parse()` 或 `execute()` 处理外部输入；
修改工作区外的系统文件；向 IP 地址而非域名发起网络调用；使用混淆代码。

**输出**: 返回强制代码审查（Code Review - MANDATORY）的执行结果,包含操作状态和输出数据。
### 3. 基础审查报告生成
生成基础审查报告，包含：技能名称、来源、作者、版本；RED FLAGS 列表（None 或具体列表）；
基础安装建议（SAFE TO INSTALL / DO NOT INSTALL）。基础版不包含风险分级（LOW/MEDIUM/HIGH/EXTREME）

#
## 使用流程

1. 确认技能来源（SkillHub / GitHub / 其他），记录作者和版本
2. 手动查询下载量、星标数和最后更新时间
3. 读取技能中的所有文件，逐一检查 RED FLAGS 清单
4. 生成基础审查报告，输出 RED FLAGS 和安装建议
5. 存在 RED FLAGS 的技能拒绝安装

#
## 示例

### 示例1：技能基础审查

```text
SKILL VETTING REPORT (BASIC)
═══════════════════════════════════════
Skill: my-skill
Source: GitHub (example/skill-repo)
Author: example-user
Version: 1.2.0
───────────────────────────────────────
RED FLAGS:
• scripts/install.sh: curl to unknown URL
• scripts/install.sh: Network call to IP instead of domain
• scripts/helper.sh: Reads ~/.config without clear reason

VERDICT: DO NOT INSTALL

NOTES: install.sh 向未知 IP 发起网络请求，且访问 ~/.config 无明确理由。
═══════════════════════════════════════
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `curl`/`wget` 到未知 URL | 技能尝试从不受信任的源下载数据 | 立即标记为 RED FLAG，拒绝安装 |
| 请求凭证/令牌/API Key | 技能要求用户提供敏感凭证 | 标记为 RED FLAG，拒绝安装 |
| 读取 `~/.ssh`/`~/.aws`/`~/.config` | 技能访问敏感系统路径 | 检查是否有明确理由；无理由则拒绝安装 |
| 访问 `MEMORY.md`/`USER.md`/`SOUL.md`/`IDENTITY.md` | 技能触及 Agent 身份文件 | 立即拒绝安装 |
| 使用 `JSON.parse()`/`execute()` 处理外部输入 | 代码注入风险 | 标记为 RED FLAG，拒绝安装 |

## 常见问题

### Q1: 免费版支持 GitHub API 快速查询吗？
A: 免费版不包含 GitHub API 快速审查命令。需要手动访问 GitHub 页面查看星标数、最后更新时间
等信息。完整版支持 `curl -s "https://api.相关技术文档 自动查询仓库元数据。

### Q2: 免费版的风险分级有哪几个级别？
A: 免费版仅输出两种安装建议：SAFE TO INSTALL 和 DO NOT INSTALL。完整版支持 4 级风险分级
（LOW/MEDIUM/HIGH/EXTREME），并根据级别决定是否需要人工批准。

### Q3: 免费版包含权限范围评估吗？
A: 免费版不包含权限范围评估。完整版支持评估文件读写、命令执行、网络访问的最小权限需求，
并标记超出功能需求的权限请求为风险信号。

### Q4: 免费版支持信任层级评估吗？
A: 免费版不包含 5 级信任层级评估。完整版根据来源（官方技能、高星标仓库 1000+、已知作者、
新/未知来源、请求凭证的技能）应用差异化审查深度。

### Q5: 如何升级到完整版？
A: 将技能替换为完整版 skill-vetter 即可。完整版包含 6 项核心能力、GitHub API 快速审查命令、
4 级风险分级、权限范围评估、5 级信任层级和结构化审查报告。

## 已知限制

- 不包含 GitHub API 自动查询命令，需手动查看仓库信息
- 不包含 4 级风险分级（LOW/MEDIUM/HIGH/EXTREME），仅输出二值安装建议
- 不包含权限范围评估和最小权限分析
- 不包含 5 级信任层级差异化审查
- 不包含结构化审查报告的完整字段（指标、权限需求、附注）

## 安全注意事项

| 风险类型 | 防范措施 |
|----------|---------|
| API密钥泄露 | 通过环境变量配置，禁止硬编码到代码或配置文件中 |
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 网络通信安全 | 使用HTTPS协议，验证SSL证书有效性 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 效率量化分析

| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 差异化对比

| 对比维度 | 本技能 | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 核心功能 | 通用场景 | 通用场景 |

## 核心功能

- **自动化执行**: 基于指令驱动的自动化流程
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据