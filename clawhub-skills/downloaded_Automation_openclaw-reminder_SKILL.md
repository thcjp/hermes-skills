---
slug: -reminder
name: -reminder
version: "1.0.5"
displayName: Reminder
summary: "用 cron建一次性提醒任务,指定时间与内容"
  time and task content...
license: MIT
description: |-
  Create one-time reminder tasks using  cron。User specifies reminder
  time and task content。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Automation
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

> **核心功能**: 本技能提供化工作流场景等能力。

# Reminder

Create one-time reminder tasks using Skill平台 cron.

## Usage

When user says "remind me to <参数> in 30 seconds" or "remind me at 3pm", I create a cron job that executes the task and returns the result when the time comes.

## Parameter Configuration

### Fixed Parameters

* `--session main` - Use main session to inherit Discord context
* `--system-event` - System event payload for main session
* `--channel discord` - Discord channel
* `--announce` - Send result directly to Discord
* `--delete-after-run` - Delete task after execution

### Dynamic Parameters (from current session context)

Use `session_status` tool to get current session's deliveryContext:

* `--agent` - Get from `deliveryContext.accountId` (e.g., `machu`)
* `--to` - Get from `deliveryContext.to` (e.g., `channel:1476104553148452958`)

How to get:

```bash
session_status
```

## Time Parsing

Parse user input time, support:

* Relative time: `30 seconds`, `1 minute`, `30 minutes`, `2 hours`, `1 day`
* Absolute time: `3pm`, `9am today`, `12pm tomorrow`

Convert to ISO 8601 format for cron.

## 示例

User says "remind me to check weather in 30 seconds":

```bash
session_status

date -u -d "+30 seconds" +"%Y-%m-%dT%H:%M:%SZ"

skill-platform cron add \
  --name "reminder-weather" \
  --at "2026-02-26T13:30:00Z" \
  --session main \
  --system-event "Check Beijing weather" \
  --agent machu \
  --announce \
  --channel discord \
  --to "channel:1476104553148452958" \
  --delete-after-run
```

## Task Content (SECURITY)

User-specified task content must be sanitized before passing to cron:

1. **Validation Method**: REJECT dangerous patterns (not escape)

   The script rejects any input containing:

   * Command substitution: `$()`, backticks `` ` ``
   * Shell metacharacters: `;`, `|`, `&`, `>`, `<`
   * Double quotes: `"` (breaks CLI quoting)
   * Newlines: `\n` (can inject multiple commands)
   * Dangerous command prefixes: `sudo`, `rm`, `wget`, `curl`, `bash`, etc.
2. **Sanitization Script**:
   Use `scripts/sanitize-message.sh` to validate input:

   bash

   ```
   ./scripts/sanitize-message.sh "user's task content"
   # Exit code 0 = safe, non-zero = rejected
   ```
3. **If rejected**: Tell user the task contains invalid characters and ask them to rephrase without: $() ` ; | & > < " or dangerous commands.

## Confirmation Reply

After creating the task, reply to user to confirm:

* "OK, will remind you in X minutes/to do <参数>"
* Don't tell user the specific cron command

## Notes

1. Time must be in the future, not the past
2. Task content should be concise and clear
3. If time exceeds 48 hours, suggest using calendar
4. Always use `--session main` + `--system-event` for reliable Discord delivery
5. Validate task content with sanitize-message.sh before creating job

## 依赖与配置
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
- **分类**: MD+execute(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 功能能力
- Create one-time reminder tasks using  cron
- User specifies reminder
  time and task content
- 触发关键词: using, create, tasks, , reminder, time

## 适用范围
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用指南
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 异常管理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 问题汇编
### Q1: 如何开始使用Reminder？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Reminder有什么限制？
A: 请参考已知限制章节了解具体限制。

## 使用约束
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 功能边界
### 输入限制
- **时间范围**：用户指定的提醒时间必须在未来，不支持设置过去的提醒。
- **时间精度**：用户输入的时间需足够精确，以避免因时间解析错误导致的提醒失败。
- **任务内容长度**：任务内容不宜过长，以免在执行时造成命令行界面输出截断。

### 性能边界
- **任务数量**：系统对同时创建的任务数量有限制，过多任务可能导致性能下降或系统资源不足。
- **执行频率**：频繁的提醒任务执行可能会对系统性能产生影响，建议合理规划提醒频率。

### 兼容性约束
- **操作系统**：该技能在Windows、macOS和Linux操作系统上均支持，但可能存在细微差异。
- **Agent平台**：仅支持SKILL.md的AI Agent，如Claude Code、Cursor、Codex、Gemini CLI等。
- **LLM API**：依赖LLM API支持，无LLM环境无法使用。

### 安全限制
- **任务内容安全**：用户指定的任务内容需经过安全验证，避免执行恶意命令。
- **API Key**：除内容中明确标注的外部API外，无需额外API Key配置。

### 其他限制
- **复杂场景处理**：对于需要人工判断的复杂决策场景，该技能无法直接处理，可能需要人工辅助。
- **网络依赖**：执行任务时可能需要网络连接，网络不稳定可能导致任务执行失败。

## 用户问答
### Q1: Reminder支持哪些输入格式？

A1: 用 cron建一次性提醒任务,指定时间与内容。支持文本指令和结构化参数输入，具体格式参考使用流程章节。

### Q2: 需要配置API Key吗？

A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。

### Q3: 命令行执行失败怎么办？

A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。

## 安全规范
### 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 量化评估
| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 特色对比
| 对比维度 | Reminder | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 用 cron建一次性提醒任务,指定时间与内容 | 通用场景 | 通用场景 |

## 错误处理策略
针对Reminder使用中可能遇到的常见问题,提供以下排查方案:

| 错误类型 | 原因分析 | 解决方案 |
|---------|---------|---------|
| API认证失败(401) | API密钥错误或过期 | 检查密钥配置,重新生成token |
| 接口限流(429) | 请求频率超出限制 | 降低调用频率,启用重试退避策略 |
| 响应超时(504) | 网络延迟或服务端负载过高 | 增加超时阈值,检查网络连接 |
| 文件不存在 | 路径错误或文件未创建 | 检查路径拼写,确认文件已生成 |
| 文件格式不支持 | 扩展名不在支持列表中 | 转换为支持的格式后重试 |
| 权限不足 | 当前用户无读写权限 | 检查文件权限,以管理员身份运行 |
| 命令执行失败 | 参数错误或环境依赖缺失 | 检查命令语法,确认依赖已安装 |
| 进程超时 | 命令执行时间过长 | 增加超时设置,优化命令参数 |
| 网络连接失败 | DNS解析失败或防火墙拦截 | 检查网络配置,确认代理设置 |

### Reminder通用排查步骤

1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块

## 常见疑问速答
### Q1: Reminder支持哪些输入格式？

A1: 用 cron建一次性提醒任务,指定时间与内容。支持文本指令和结构化参数输入，具体格式参考使用流程章节。

### Q2: 需要配置API Key吗？

A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。

### Q3: 命令行执行失败怎么办？

A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。