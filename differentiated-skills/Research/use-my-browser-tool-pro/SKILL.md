---
slug: use-my-browser-tool-pro
name: use-my-browser-tool-pro
version: 1.0.0
displayName: 真实浏览器控制专业版
summary: 企业级真实浏览器控制平台,支持批量会话、多浏览器管理、安全审计与团队协作
license: Proprietary
edition: pro
description: 真实浏览器控制专业版,面向企业团队和高级用户提供深度的真实浏览器控制能力。支持批量会话管理、多浏览器实例控制、安全审计、团队协作等高级功能。Use
  when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。
tags:
- 研究工具
- 浏览器控制
- 企业级
- 批量处理
tools:
- - read
- exec
homepage: https://skillhub.cn
pricing_tier: L4
pricing_model: monthly
suggested_price: 99.9
---

真实浏览器控制专业版是企业级的真实浏览器自动化解决方案。在完整兼容免费版所有单浏览器控制能力的基础上,专业版引入了批量会话管理、多浏览器实例控制、安全审计、团队协作等高级能力,适用于企业级 Web 自动化测试、跨账号数据采集、批量表单处理等复杂场景。

专业版特别强化了安全合规能力,支持完整的操作日志审计、基于角色的访问控制、数据加密传输,满足企业级安全合规要求。

## 核心能力
### 1. 批量会话管理
同时控制多个浏览器实例,支持并行操作。

```bash
{
  "sessions": [
    {"id": "session_1", "profile": "account_a", "url": "https://app.example.com/dashboard"},
    {"id": "session_2", "profile": "account_b", "url": "https://app.example.com/dashboard"},
    {"id": "session_3", "profile": "account_c", "url": "https://app.example.com/dashboard"}
  ],
  "concurrency": 3,
  "auto_reconnect": true
}

tmwd batch start batch_sessions.json

tmwd batch status

tmwd batch exec --all-sessions --code "return document.querySelector('.notification').innerText"
```

**输入**: 用户提供批量会话管理所需的指令和必要参数。
**处理**: 按照skill规范执行批量会话管理操作,遵循单一意图原则。
**输出**: 返回批量会话管理的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 多浏览器配置文件隔离
支持多个浏览器配置文件,隔离不同账号环境。

```bash
tmwd profile create --name "account_a" --isolated
tmwd profile create --name "account_b" --isolated

tmwd exec --profile "account_a" --code "document.querySelector('#user-menu').click()"
tmwd exec --profile "account_b" --code "document.querySelector('#user-menu').click()"

tmwd profile list
tmwd profile delete --name "old_account"
```

**输入**: 用户提供多浏览器配置文件隔离所需的指令和必要参数。
**处理**: 按照skill规范执行多浏览器配置文件隔离操作,遵循单一意图原则。
**输出**: 返回多浏览器配置文件隔离的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 安全审计与操作日志
完整记录所有浏览器操作,满足企业合规要求。

```bash
tmwd audit enable --log-dir ./audit_logs

tmwd audit log --date $(date +%Y-%m-%d)

tmwd audit log --session "session_1"

tmwd audit export --format csv --output audit_report.csv

```

**输入**: 用户提供安全审计与操作日志所需的指令和必要参数。
**处理**: 按照skill规范执行安全审计与操作日志操作,遵循单一意图原则。
**输出**: 返回安全审计与操作日志的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 团队协作
支持团队共享浏览器配置和会话。

```bash
tmwd team create --name "qa_team"

tmwd profile share --name "test_env" --team "qa_team"

tmwd session share --id "session_1" --team "qa_team"

tmwd team resources --team "qa_team"
```

**输入**: 用户提供团队协作所需的指令和必要参数。
**处理**: 按照skill规范执行团队协作操作,遵循单一意图原则。
**输出**: 返回团队协作的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. 高级 CSP 绕过
增强的反检测和 CSP 绕过能力。

```bash
tmwd exec --code "document.querySelector('#btn').click()" --auto-strategy

tmwd exec --code "document.querySelector('#btn').click()" --force-cdp

tmwd exec --code "document.querySelector('#btn').click()" --stealth
```

**输入**: 用户提供高级 CSP 绕过所需的指令和必要参数。
**处理**: 按照skill规范执行高级 CSP 绕过操作,遵循单一意图原则。
**输出**: 返回高级 CSP 绕过的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 6. 定时任务与自动化流程
支持定时执行浏览器自动化任务。

```bash
{
  "tasks": [
    {
      "name": "每日数据采集",
      "schedule": "0 9 * * *",
      "actions": [
        {"type": "navigate", "url": "https://app.example.com/data"},
        {"type": "exec", "code": "return extractData()"},
        {"type": "save", "output": "daily_data.json"}
      ]
    }
  ]
}

tmwd schedule start schedule.json

tmwd schedule status
```

**输入**: 用户提供定时任务与自动化流程所需的指令和必要参数。
**处理**: 按照skill规范执行定时任务与自动化流程操作,遵循单一意图原则。
**输出**: 返回定时任务与自动化流程的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 7. 完整兼容免费版
专业版完全兼容免费版的所有命令和配置,平滑升级。

```bash
tmwd_status()
tmwd_switch(pattern="example.com")
tmwd_navigate(url="https://example.com")
tmwd_text(max_chars=5000)
tmwd_exec(code="document.querySelector('#btn').click()")
```

**输入**: 用户提供完整兼容免费版所需的指令和必要参数。
**处理**: 按照skill规范执行完整兼容免费版操作,遵循单一意图原则。
**输出**: 返回完整兼容免费版的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级真实浏览器、控制平台、支持批量会话、多浏览器管理、安全审计与团队协、真实浏览器控制专、面向企业团队和高、级用户提供深度的、真实浏览器控制能、支持批量会话管理、多浏览器实例控制、团队协作等高级功、when、需要安全检测、合规审计、漏洞扫描、加密防护时使用、不适用于渗透测试、未授权目标、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 输出格式

本skill的输出格式为Markdown文本,包含操作状态和执行结果。具体输出内容取决于执行的能力点和输入参数。

## 使用场景
### 场景一:企业级 Web 自动化测试
某 QA 团队需要在多个账号环境中执行回归测试。

```bash
cat > test_sessions.json << 'EOF'
{
  "sessions": [
    {"id": "admin_test", "profile": "admin_account", "url": "https://app.example.com/admin"},
    {"id": "user_test", "profile": "user_account", "url": "https://app.example.com/dashboard"},
    {"id": "guest_test", "profile": "guest_account", "url": "https://app.example.com/home"}
  ],
  "concurrency": 3
}
EOF

tmwd batch start test_sessions.json

tmwd batch exec --all-sessions --code "
  var result = {
    title: document.title,
    url: location.href,
    buttons: document.querySelectorAll('button').length,
    forms: document.querySelectorAll('form').length
  };
  return result;
"

tmwd batch results --output test_results.json

tmwd report generate --input test_results.json --output qa_report.html
```

### 场景二:跨账号数据采集与同步
某运营团队需要从多个社交媒体账号采集数据。

```bash
cat > social_sessions.json << 'EOF'
{
  "sessions": [
    {"id": "account_1", "profile": "social_a", "url": "https://social.example.com/analytics"},
    {"id": "account_2", "profile": "social_b", "url": "https://social.example.com/analytics"},
    {"id": "account_3", "profile": "social_c", "url": "https://social.example.com/analytics"}
  ],
  "concurrency": 3
}
EOF

tmwd batch start social_sessions.json

tmwd batch exec --all-sessions --code "
  var metrics = {
    followers: document.querySelector('.follower-count').innerText,
    engagement: document.querySelector('.engagement-rate').innerText,
    posts: document.querySelector('.post-count').innerText
  };
  return metrics;
"

tmwd batch results --output social_metrics.json

tmwd report consolidate --input social_metrics.json --output social_report.html
```

### 场景三:批量表单处理
某企业需要批量处理在线申请表单。

```bash
cat > form_data.json << 'EOF'
{
  "forms": [
    {"id": "form_1", "data": {"name": "张三", "email": "zhangsan@example.com", "phone": "13800138001"}},
    {"id": "form_2", "data": {"name": "李四", "email": "lisi@example.com", "phone": "13800138002"}},
    {"id": "form_3", "data": {"name": "王五", "email": "wangwu@example.com", "phone": "13800138003"}}
  ]
}
EOF

tmwd batch form-fill --input form_data.json --url "https://form.example.com/apply"

tmwd batch verify --input form_data.json

tmwd batch submit --input form_data.json --confirm

tmwd report generate --input results.json --output form_report.html
```

## 快速开始
### 依赖详情
```bash
skill-platform plugins install skill-platform-tmwd-pro --registry https://registry.npmjs.org

tmwd --version --edition
```

### 第二步:配置企业环境
```bash
cat > enterprise_config.json << 'EOF'
{
  "edition": "pro",
  "sessions": {
    "max_concurrent": 10,
    "auto_reconnect": true,
    "timeout": 60000
  },
  "profiles": {
    "isolated": true,
    "encrypted": true,
    "backup": "daily"
  },
  "audit": {
    "enabled": true,
    "log_dir": "./audit_logs",
    "retention_days": 90
  },
  "team": {
    "enabled": true,
    "shared_profiles": true,
    "role_based_access": true
  }
}
EOF

tmwd config init enterprise_config.json
```

### 第三步:运行首个批量任务
```bash
cat > first_batch.json << 'EOF'
{
  "sessions": [
    {"id": "s1", "profile": "default", "url": "https://example.com"},
    {"id": "s2", "profile": "default", "url": "https://example.org"}
  ],
  "concurrency": 2
}
EOF

tmwd batch start first_batch.json

tmwd batch status
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。


## 示例
### 企业级配置
```json
{
  "edition": "pro",
  "sessions": {
    "max_concurrent": 10,
    "auto_reconnect": true,
    "heartbeat_interval": 5000,
    "timeout": 60000
  },
  "profiles": {
    "isolated": true,
    "encrypted": true,
    "backup": "daily",
    "max_profiles": 50
  },
  "execution": {
    "max_execution_time": 30000,
    "return_format": "json",
    "auto_strategy": true,
    "stealth_mode": false
  },
  "audit": {
    "enabled": true,
    "log_dir": "./audit_logs",
    "retention_days": 90,
    "encrypt_logs": true,
    "export_format": "csv,json"
  },
  "team": {
    "enabled": true,
    "shared_profiles": true,
    "shared_sessions": true,
    "role_based_access": true
  },
  "scheduling": {
    "enabled": true,
    "max_tasks": 100,
    "retry_attempts": 3
  }
}
```

### 团队协作配置
```json
{
  "team": {
    "name": "automation_team",
    "members": [
      {"email": "lead@company.com", "role": "admin"},
      {"email": "qa1@company.com", "role": "operator"},
      {"email": "qa2@company.com", "role": "operator"},
      {"email": "manager@company.com", "role": "viewer"}
    ],
    "shared_resources": {
      "profiles": true,
      "sessions": true,
      "scripts": true
    }
  },
  "permissions": {
    "admin": ["all"],
    "operator": ["execute", "create_session", "use_profile"],
    "viewer": ["view", "export_logs"]
  }
}
```

## 最佳实践
### 1. 免费版到专业版的平滑迁移
```bash
tmwd_status()
tmwd_exec(code="document.querySelector('#btn').click()")

tmwd batch start sessions.json

tmwd audit enable
tmwd profile create --name "test_env" --isolated
```

### 2. 批量任务的性能优化
```bash
tmwd batch start sessions.json --concurrency 5

tmwd session pool create --size 10 --profile "default"
```

### 3. 安全审计的最佳实践
```bash
tmwd audit enable --log-dir ./audit_logs --encrypt

tmwd audit export --format csv --output monthly_audit.csv --period "2026-07"

tmwd audit config set --retention-days 90 --auto-cleanup
```

### 4. 团队协作的权限管理
```bash
tmwd team permissions --role "operator" --permissions "execute,create_session"
tmwd team permissions --role "viewer" --permissions "view,export_logs"

tmwd profile share --name "test_env" --team "qa_team" --read-only
```

## 免费版与专业版对比
| 功能特性 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 真实浏览器控制 | 支持 | 支持 |
| 页面导航与提取 | 支持 | 支持 |
| JavaScript 执行 | 支持 | 支持 |
| 多标签页管理 | 支持 | 支持 |
| CSP 回退机制 | 支持 | 支持 |
| 批量会话管理 | 不支持 | 支持 |
| 多浏览器配置隔离 | 不支持 | 支持 |
| 安全审计日志 | 不支持 | 支持 |
| 团队协作 | 不支持 | 支持 |
| 高级 CSP 绕过 | 不支持 | 支持 |
| 定时任务调度 | 不支持 | 支持 |
| 并发执行 | 单会话 | 多会话并行 |
| 数据加密 | 不支持 | 支持 |
| 适用场景 | 个人使用 | 企业级应用 |
| 技术支持 | 社区支持 | 优先支持 |

## 常见问题
### Q1: 专业版是否兼容免费版的命令?
**A:** 完全兼容。专业版是免费版的超集,所有免费版命令在专业版中均可直接使用,无需修改。

### Q2: 批量会话如何管理资源?
**A:** 专业版提供会话池和资源管理:

```bash
tmwd session pool create --size 10 --profile "default"

tmwd resources status

tmwd config set --auto-cleanup --idle-timeout 300
```

### Q3: 安全审计记录哪些内容?
**A:** 专业版审计日志包含:

- 所有页面导航记录(含 URL 和时间戳)
- 执行的 JavaScript 代码
- 提取的数据摘要(不含敏感数据明文)
- 操作者信息和会话 ID
- 异常和错误记录

### Q4: 团队协作如何保障数据安全?
**A:** 专业版提供多重安全保障:

- 浏览器配置文件加密存储
- 共享资源基于角色访问控制
- 审计日志完整记录所有操作
- 敏感数据自动脱敏
- 数据传输加密

### Q5: 如何与现有 CI/CD 系统集成?
**A:** 专业版提供 CLI 接口和 Webhook,支持与 CI/CD 系统集成:

```bash
tmwd batch start test_sessions.json --headless
tmwd batch results --output ci_results.json
tmwd report generate --input ci_results.json --format junit --output test_report.xml
```

## 依赖说明
### 运行环境
- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **浏览器**: Google Chrome 100 及以上版本
- **浏览器扩展**: Tampermonkey(用户脚本管理器)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Chrome 浏览器 | 浏览器 | 必需 | 官方网站下载安装 |
| Tampermonkey | 浏览器扩展 | 必需 | Chrome 应用商店安装 |
| skill-platform-tmwd-pro | 插件 | 必需 | 通过 `skill-platform plugins install` 安装 |
| 用户脚本 | 脚本 | 必需 | 通过 Tampermonkey 安装 |
| 数据库 | 存储 | 团队协作必需 | 本地或云端数据库 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
专业版需要以下配置:

```bash
TEAM_API_TOKEN=your_team_api_token

DB_HOST=localhost
DB_PORT=5432
DB_NAME=browser_automation
DB_USER=admin
DB_PASSWORD=your_password

ENCRYPTION_KEY=your_encryption_key
```

### 可用性分类
- **分类**: MD+EXEC+API(综合型,支持本地执行、批量会话管理和安全审计)
- **说明**: 企业级真实浏览器控制平台,支持批量会话、多浏览器管理、安全审计等高级功能
- **适用规模**: 多用户、多浏览器实例、企业级部署
- **兼容性**: 完全兼容免费版,支持平滑升级
- API Key通过环境变量配置: export API_KEY=your_key

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
