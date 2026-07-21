---
slug: security
name: security
version: "1.0.0"
displayName: GoPlus安全扫描
summary: GoPlus AgentGuard安全扫描，支持定时巡逻、漏洞发现、Webhook通知与结果检查。
license: Proprietary
description: |-
  GoPlus AgentGuard驱动的安全扫描工具，提供代码与依赖安全检查。
  支持定时巡逻（Schedule Patrol）、一次性扫描、漏洞发现详情管理。
  通过Chat ID/Webhook发送安全通知，支持按文件路径定位漏洞。
  适用于项目安全审计、持续安全监控与漏洞管理流程。
tools:
  - read
  - exec
---

# GoPlus安全扫描

GoPlus AgentGuard安全扫描，支持定时巡逻、漏洞发现、Webhook通知与结果检查。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Go环境**: Go 1.19+（如扫描Go项目）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| GoPlus CLI | CLI工具 | 必需 | `go install github.com/Qianjiachang/goplus@latest` |
| Go | 运行时 | 可选 | https://go.dev/dl/ |
| Webhook URL | API | 可选 | Slack/飞书/钉钉等平台配置 |

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，需要exec命令行执行能力运行GoPlus CLI）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行安全扫描任务

## 核心能力

### 安全扫描（Security Scan）

执行一次性安全扫描，检测代码中的安全漏洞：

- **代码扫描**：扫描Go源代码中的安全问题（SQL注入、命令注入、路径遍历等）
- **依赖检查**：检查项目依赖中的已知漏洞（CVE）
- **配置审计**：检查安全配置项（硬编码密钥、不安全默认值等）
- **扫描范围**：支持指定目录、文件或整个项目
- **扫描结果**：按严重程度分类（Critical / High / Medium / Low / Info）

### 定时巡逻（Schedule Patrol）
配置定时安全巡逻，实现持续安全监控：

- **定时执行**：按cron表达式定期执行安全扫描
- **巡逻模式**：持续监控代码变更，发现新漏洞立即告警
- **增量扫描**：仅扫描变更的文件，提高效率
- **巡逻状态**：启动、停止、查看巡逻状态
- **巡逻间隔**：支持每日、每周、自定义间隔

**输入**: 用户提供定时巡逻（Schedule Patrol）所需的指令和必要参数。
**输出**: 返回定时巡逻（Schedule Patrol）的执行结果,包含操作状态和输出数据。### 漏洞发现详情（Findings Detail）

查看每个安全发现（finding）的详细信息：

- **漏洞描述**：漏洞类型、描述与影响范围
- **文件路径**：漏洞所在的文件路径与行号
- **代码片段**：展示存在问题的代码片段
- **修复建议**：提供具体的修复方案与代码示例
- **严重程度**：Critical / High / Medium / Low / Info 分级
- **状态管理**：Open（未处理）、Fixed（已修复）、Ignored（已忽略）

### Chat ID / Webhook通知

通过Chat ID或Webhook发送安全通知：

- **Chat ID通知**：将扫描结果发送到指定聊天会话
- **Webhook通知**：通过Webhook推送到Slack、飞书、钉钉等平台
- **通知内容**：漏洞摘要、严重程度统计、详细报告链接
- **通知时机**：扫描完成、发现Critical/High漏洞、巡逻告警
- **通知配置**：可配置通知阈值（如仅通知High以上漏洞）

### 按文件路径定位漏洞（Finding with File Path）
根据文件路径快速定位相关漏洞：

- **路径过滤**：按文件路径筛选安全发现
- **文件级视图**：查看指定文件中的所有安全问题
- **目录级视图**：查看指定目录下的所有安全问题
- **快速跳转**：从通知直接跳转到漏洞代码位置
- **批量处理**：按文件路径批量修复或忽略漏洞

**输入**: 用户提供按文件路径定位漏洞（Finding with File Path）所需的指令和必要参数。
**输出**: 返回按文件路径定位漏洞（Finding with File Path）的执行结果,包含操作状态和输出数据。### 检查结果（Check Results）

查看与管理安全扫描结果：

- **结果摘要**：漏洞总数、按严重程度分布、修复进度
- **历史趋势**：漏洞数量随时间的变化趋势
- **修复追踪**：跟踪漏洞从发现到修复的全过程
- **报告导出**：导出为JSON、Markdown、HTML格式报告
- **对比分析**：对比两次扫描结果，识别新增与已修复的漏洞

### 健康检查（Health Check）
检查GoPlus AgentGuard服务健康状态：

- **服务状态**：检查GoPlus CLI是否正常运行
- **配置验证**：验证Webhook URL、Chat ID等配置是否有效
- **连接测试**：测试与通知平台的连接是否正常
- **版本检查**：检查GoPlus CLI版本是否为最新

**输入**: 用户提供健康检查（Health Check）所需的指令和必要参数。
**输出**: 返回健康检查（Health Check）的执行结果,包含操作状态和输出数据。
## 使用流程

1. 安装GoPlus CLI：`go install github.com/Qianjiachang/goplus@latest`
2. 执行健康检查，确认服务正常运行
3. 执行一次性安全扫描或配置定时巡逻
4. 查看漏洞发现详情，按文件路径定位问题
5. 配置Chat ID或Webhook接收安全通知
6. 修复漏洞后再次扫描验证
7. 检查扫描结果，导出报告

## 示例

### 示例1：执行安全扫描

```
用户: 扫描我的Go项目安全漏洞

Agent: 安全扫描完成：
- 扫描文件: 156个
- 发现漏洞: 7个
  - Critical: 1 (SQL注入)
  - High: 2 (硬编码密钥、命令注入)
  - Medium: 3 (不安全配置)
  - Low: 1 (信息泄露)

Critical漏洞详情:
- 文件: cmd/handler/user.go:45
- 类型: SQL Injection
- 代码: db.Query("SELECT * FROM users WHERE name='" + name + "'")
- 修复: 使用参数化查询 db.Query("SELECT * FROM users WHERE name=?", name)
```

### 示例2：配置定时巡逻与通知

```
用户: 配置每天定时巡逻，发现High以上漏洞通知我的飞书群

Agent: 定时巡逻已配置：
- 巡逻间隔: 每日 09:00
- 扫描范围: 整个项目
- 通知方式: 飞书Webhook
- 通知阈值: High及以上
- Webhook URL: https://open.feishu.cn/open-apis/bot/v2/hook/xxx

巡逻状态: 已启动
下次执行: 2026-02-17 09:00
```

### 示例3：按文件路径查看漏洞

```
用户: 查看 cmd/handler/ 目录下的所有安全漏洞

Agent: cmd/handler/ 目录安全发现：
1. user.go:45 - Critical - SQL Injection
2. user.go:78 - High - Hardcoded Secret
3. admin.go:23 - High - Command Injection
4. admin.go:56 - Medium - Insecure Config
5. auth.go:12 - Medium - Weak Crypto

建议优先修复Critical和High级别漏洞。
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| GoPlus CLI未安装 | 未执行go install | 运行 `go install github.com/Qianjiachang/goplus@latest` 安装 |
| 健康检查失败 | GoPlus服务未运行 | 重启GoPlus服务；对照依赖说明章节逐项验证配置项,确认环境变量已正确设置文件 |
| 扫描超时 | 项目过大或网络问题 | 缩小扫描范围；增加超时时间；执行ping命令测试网络连通性,检查防火墙和代理设置连接 |
| Webhook推送失败 | URL无效或网络问题 | 验证Webhook URL；执行ping命令测试网络连通性,检查防火墙和代理设置；执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令推送 |
| Chat ID无效 | 会话ID错误 | 确认Chat ID正确；检查会话权限 |
| 扫描结果为空 | 无Go源代码或路径错误 | 确认扫描路径包含Go文件；检查路径拼写 |

## 常见问题

### Q1: 安全扫描覆盖哪些类型的漏洞？
A: 覆盖SQL注入、命令注入、路径遍历、硬编码密钥、不安全加密、不安全配置、依赖CVE等多种安全漏洞类型，按Critical/High/Medium/Low/Info五级分类。

### Q2: 定时巡逻和一次性扫描有什么区别？
A: 一次性扫描是手动触发的单次扫描。定时巡逻（Schedule Patrol）按cron表达式定期自动扫描，支持增量扫描（仅扫描变更文件），适合持续安全监控。

### Q3: 如何配置Webhook通知？
A: 在Slack/飞书/钉钉等平台创建Bot，获取Webhook URL。配置到GoPlus中，设置通知阈值（如仅通知High以上）。扫描完成或发现高危漏洞时自动推送通知。

### Q4: 如何按文件路径查看漏洞？
A: 使用按文件路径定位功能，指定文件或目录路径，系统会筛选出该路径下的所有安全发现，包括文件名、行号、漏洞类型与修复建议。

### Q5: 漏洞状态如何管理？
A: 每个漏洞有三种状态：Open（未处理）、Fixed（已修复）、Ignored（已忽略）。修复代码后再次扫描会自动更新状态，也可手动标记为Ignored。

### Q6: 如何导出安全报告？
A: 支持导出为JSON、Markdown、HTML三种格式。报告包含漏洞摘要、严重程度分布、详细发现列表与修复建议，适用于安全审计与团队协作。

## 已知限制

- 需要安装GoPlus CLI，无CLI环境无法执行扫描
- 主要针对Go语言项目，对其他语言支持有限
- 依赖漏洞检查需要网络访问CVE数据库
- 定时巡逻需要GoPlus服务持续运行
- 误报率取决于代码复杂度，需人工复核
- Webhook通知受目标平台API频率限制
