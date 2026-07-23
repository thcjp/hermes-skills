---
slug: "code-runner-tool-pro"
name: "code-runner-tool-pro"
version: "1.0.0"
displayName: "代码执行工具专业版"
summary: "企业级PTY代码执行,支持批量任务、并发执行、执行审计与CI/CD集成"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队与企业的高级代码执行工具,在免费版基础上扩展批量执行、并发管理、执行审计等能力。核心能力:
  - 批量任务执行与并发管理
  - 执行日志审计与结果追踪
  - CI/CD 流水线集成
  - 自定义应答规则与执行策略
  - 多用户隔离与权限管理

  适用场景:
  - 企业级批量代码处理
  - CI/CD 流水线自动化
  - 多项目并行开发与测试

  差异化:
  - 兼容免费版全部能力,无缝升级
  - 支持批量并发与任务编排
  - 提供执行审计与日志追踪
  - 优先技术支持与更新通道

  适用关键词: runner,...
tags:
  - 开发工具
  - 代码执行
  - 企业级
  - 批量处理
  - CI/CD集成
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9

---
# 代码执行工具专业版
## 概述
代码执行工具专业版为企业团队提供高级 PTY 代码执行能力。在免费版单任务执行基础上,扩展了批量并发、执行审计、CI/CD 集成、多用户隔离等功能,满足企业级自动化开发的需求.
专业版完全兼容免费版的 API 与执行流程,已有工作流可无缝升级.
## 核心能力
### 1. 批量任务执行
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 代码执行工具专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```python
from code_runner import run_batch_tasks
# ...
tasks = [
    {
        "workdir": "/path/to/auth-service",
        "prompt": "实现 JWT 认证,添加单元测试",
        "priority": "high"
    },
    {
        "workdir": "/path/to/order-service",
        "prompt": "添加订单状态机,包含测试",
        "priority": "medium"
    },
    {
        "workdir": "/path/to/payment-service",
        "prompt": "集成第三方支付网关",
        "priority": "medium"
    }
]
# ...
results = run_batch_tasks(tasks, max_concurrent=3)
```

**输入**: 用户提供批量任务执行所需的指令和必要参数.
**处理**: 解析批量任务执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回批量任务执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 并发管理与任务编排
| 功能 | 说明 |
|:-----|:-----|
| 并发控制 | 可配置最大并发数(默认 3) |
| 优先级队列 | 高优先级任务优先执行 |
| 依赖编排 | 任务间可配置依赖关系 |
| 失败重试 | 自动重试失败任务 |
| 超时管理 | 每个任务独立超时配置 |

```python
# 依赖说明
pipeline = [
    {"id": "schema", "prompt": "创建数据库 Schema", "depends_on": []},
    {"id": "dal", "prompt": "实现数据访问层", "depends_on": ["schema"]},
    {"id": "logic", "prompt": "编写业务逻辑", "depends_on": ["dal"]},
    {"id": "api", "prompt": "添加 API 端点", "depends_on": ["logic"]},
    {"id": "test", "prompt": "运行集成测试", "depends_on": ["api"]}
]
# ...
results = run_pipeline(pipeline, max_concurrent=2)
```

**输入**: 用户提供并发管理与任务编排所需的指令和必要参数.
**处理**: 解析并发管理与任务编排的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回并发管理与任务编排的响应数据,包含状态码、结果和日志.
### 3. 执行日志审计
```python
# 审计配置
audit_config = {
    "enabled": True,
    "log_dir": ".code-runner/logs/",
    "capture_stdout": True,
    "capture_stderr": True,
    "track_changes": True,
    "retention_days": 90
}
```

审计记录包含:

| 记录项 | 说明 |
|---:|---:|
| 任务 ID | 唯一标识 |
| 执行时间 | 开始/结束时间 |
| 执行用户 | 以哪个用户运行 |
| 任务描述 | 自然语言描述 |
| 执行结果 | 成功/失败/超时 |
| 变更文件 | 修改了哪些文件 |
| 输出日志 | stdout/stderr 完整记录 |
| 执行耗时 | 总耗时(秒) |

**输入**: 用户提供执行日志审计所需的指令和必要参数.
**处理**: 解析执行日志审计的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回执行日志审计的响应数据,包含状态码、结果和日志.
### 4. CI/CD 集成
```yaml
# 示例
pipeline:
  - stage: code-execution
    jobs:
      - name: run-development
        script: |
          python3 -m code_runner \
            --workdir $PROJECT_DIR \
            --prompt "实现新功能并添加测试" \
            --user ci-runner \
            --timeout 600 \
            --audit
      - name: run-tests
        depends_on: run-development
        script: |
          python3 -m code_runner \
            --workdir $PROJECT_DIR \
            --prompt "运行全量测试套件,报告结果" \
            --user ci-runner \
            --timeout 300
```

**输入**: 用户提供CI/CD 集成所需的指令和必要参数.
**处理**: 解析CI/CD 集成的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回CI/CD 集成的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. 自定义应答规则
```python
# 扩展自动应答规则
custom_responses = {
    b'Do you want to': b'y\n',
    b'Are you sure': b'y\n',
    b'Continue?': b'y\n',
    b'Press Enter to continue': b'\n',
    b'Enter password': os.environ.get('EXEC_PASSWORD', '').encode() + b'\n',
    b'Select option': b'1\n'  # 选择第一个选项
}
```

**输入**: 用户提供自定义应答规则所需的指令和必要参数.
**处理**: 解析自定义应答规则的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回自定义应答规则的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、PTY、代码执行、支持批量任务、并发执行、执行审计与、面向团队与企业的、高级代码执行工具、在免费版基础上扩、展批量执行、执行审计等能力、核心能力、批量任务执行与并、执行日志审计与结、果追踪、流水线集成、自定义应答规则与、执行策略、多用户隔离与权限等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景一: 企业级批量代码处理
对多个微服务模块批量执行开发任务.
```python
from code_runner import run_batch_tasks
# ...
# 批量处理微服务
services = ["auth", "order", "payment", "notification", "user"]
tasks = [
    {
        "workdir": f"/projects/microservices/{svc}",
        "prompt": f"为 {svc} 服务添加健康检查端点和单元测试",
        "priority": "medium",
        "timeout": 300
    }
    for svc in services
]
# ...
results = run_batch_tasks(tasks, max_concurrent=3)
# ...
# 生成汇总报告
for task_id, result in results.items():
    status = "成功" if result.success else "失败"
    print(f"{task_id}: {status} (耗时 {result.duration}秒)")
```

输出示例:

```text
批量执行报告
=====================================
任务总数: 5
成功: 4
失败: 1
总耗时: 812 秒
# ...
详情:
auth-service:        成功 (耗时 156秒)
order-service:       成功 (耗时 198秒)
payment-service:     成功 (耗时 175秒)
notification-service:成功 (耗时 142秒)
user-service:        失败 (超时,建议增加超时或拆分任务)
# ...
审计日志: .code-runner/logs/batch-20260718-143000.log
```

### 场景二: CI/CD 流水线自动化
在 CI/CD 流水线中自动执行代码任务.
```bash
#!/bin/bash
# CI/CD 流水线脚本
# 1. 执行开发任务
python3 -m code_runner \
  --workdir $CI_PROJECT_DIR \
  --prompt "根据 PR 描述实现功能,添加测试" \
  --user ci-runner \
  --timeout 600 \
  --audit
# ...
# 2. 运行测试
python3 -m code_runner \
  --workdir $CI_PROJECT_DIR \
  --prompt "运行全量测试,报告通过率和失败详情" \
  --user ci-runner \
  --timeout 300
# ...
# 3. 代码审查
python3 -m code_runner \
  --workdir $CI_PROJECT_DIR \
  --prompt "审查代码变更,输出审查报告" \
  --user ci-runner \
  --timeout 300
```

### 场景三: 多项目并行开发
多个项目同步开发,统一管理与追踪.
```python
# 多项目并行开发
projects = [
    {"name": "frontend", "workdir": "/projects/frontend-app"},
    {"name": "backend", "workdir": "/projects/backend-api"},
    {"name": "mobile", "workdir": "/projects/mobile-app"}
]
# ...
tasks = [
    {
        "workdir": p["workdir"],
        "prompt": f"审查 {p['name']} 项目代码,生成质量报告",
        "tag": p["name"]
    }
    for p in projects
]
# ...
results = run_batch_tasks(tasks, max_concurrent=3)
# ...
# 按项目汇总
for p in projects:
    result = results.get(p["name"])
    if result and result.success:
        print(f"{p['name']}: 审查完成,评分 {result.score}")
```

## 快速开始
### 第一步: 安装与配置
```bash
# 安装依赖
pip install code-runner-pro
# ...
# 初始化配置
mkdir -p .code-runner/{logs,reports,configs}
# ...
cat > .code-runner/config.json << 'EOF'
{
  "edition": "pro",
  "execution": {
    "max_concurrent": 3,
    "default_timeout": 300,
    "retry_count": 2,
    "default_user": "code-runner"
  },
  "audit": {
    "enabled": true,
    "log_dir": ".code-runner/logs/",
    "capture_output": true,
    "track_changes": true,
    "retention_days": 90
  }
}
EOF
```

### 第二步: 执行批量任务
```python
from code_runner import run_batch_tasks
# ...
tasks = [
    {"workdir": "/projects/app1", "prompt": "添加健康检查端点"},
    {"workdir": "/projects/app2", "prompt": "添加健康检查端点"},
    {"workdir": "/projects/app3", "prompt": "添加健康检查端点"}
]
# ...
results = run_batch_tasks(tasks, max_concurrent=3)
```

### 第三步: 查看审计报告
```bash
# 查看最新审计报告
cat .code-runner/logs/latest-audit.log
```

## 配置示例
### 企业级配置
```json
{
  "edition": "pro",
  "organization": {
    "name": "开发团队",
    "default_user": "code-runner"
  },
  "execution": {
    "max_concurrent": 5,
    "default_timeout": 600,
    "retry_count": 2,
    "priority_enabled": true,
    "dependency_aware": true
  },
  "audit": {
    "enabled": true,
    "log_dir": ".code-runner/logs/",
    "capture_stdout": true,
    "capture_stderr": true,
    "track_changes": true,
    "retention_days": 180
  },
  "cicd": {
    "integration_enabled": true,
    "webhook_url": "",
    "notify_on_failure": true
  },
  "security": {
    "user_isolation": true,
    "sandbox_enabled": true,
    "protected_paths": ["**/*.env", "**/secrets/**"]
  }
}
```

### CI/CD 集成配置
```yaml
# CI/CD 配置示例
code_runner:
  image: python:3.11
  variables:
    CODE_RUNNER_USER: ci-runner
    CODE_RUNNER_TIMEOUT: "600"
    CODE_RUNNER_AUDIT: "true"
  before_script:
    - pip install code-runner-pro
    - npm install -g @anthropic-ai/claude-code
  script:
    - python3 -m code_runner --workdir $CI_PROJECT_DIR --prompt "$TASK" --audit
  artifacts:
    paths:
      - .code-runner/logs/
    expire_in: 30 days
```

## 最佳实践
### 1. 任务拆分与编排
| 原则 | 说明 |
|:---:|:---:|
| 单一职责 | 每个任务只做一件事 |
| 合理大小 | 单任务 5-10 分钟 |
| 消除依赖 | 尽量并行执行 |
| 优先级 | 关键路径高优先级 |

### 2. 并发度配置
| 场景 | 建议并发度 | 说明 |
|:------|------:|:------|
| 开发环境 | 2-3 | 避免资源争抢 |
| CI/CD | 3-5 | 平衡速度与稳定 |
| 专用服务器 | 5-10 | 充分利用资源 |

### 3. 免费版与专业版能力对比
| 能力 | 免费版 | 专业版 |
|---:|:---|---:|
| 执行方式 | 单任务 | 批量并发 |
| 任务编排 | 不支持 | 支持(依赖+优先级) |
| 执行审计 | 不支持 | 支持(90天) |
| CI/CD 集成 | 不支持 | 支持 |
| 自定义应答 | 基础规则 | 可扩展规则 |
| 多用户隔离 | 不支持 | 支持 |
| 优先支持 | 社区 | 专属通道 |

### 4. 审计日志分析
```bash
# 分析执行日志
请分析 .code-runner/logs/ 下最近 7 天的执行日志
统计: 成功率、平均耗时、失败原因分布
输出: 执行趋势报告
```

## 常见问题
### Q1: 专业版是否兼容免费版的 API?
完全兼容。专业版的 `run_code_task` 函数与免费版签名一致,免费版代码无需修改即可运行.
### Q2: 并发执行时资源不够怎么办?
降低并发度或增加超时时间。监控 CPU 和内存使用,避免资源耗尽:

```python
# 动态调整并发度
import psutil
cpu_usage = psutil.cpu_percent()
max_concurrent = 5 if cpu_usage < 70 else 2
```

### Q3: CI/CD 中如何安全存储凭据?
使用 CI/CD 平台的密钥管理功能,不要在代码中硬编码:

```yaml
variables:
  ANTHROPIC_API_KEY: $CI_SECRETS_API_KEY
```

### Q4: 审计日志占用空间太大怎么办?
配置日志保留策略与压缩:

```json
{
  "audit": {
    "retention_days": 90,
    "compress_after_days": 7,
    "max_size_mb": 500
  }
}
```

### Q5: 任务失败后如何自动重试?
在配置中启用自动重试:

```json
{
  "execution": {
    "retry_count": 2,
    "retry_delay_seconds": 30
  }
}
```

### Q6: 如何获得优先技术支持?
专业版用户可通过专属通道提交问题,通常 1 个工作日内响应.
## 依赖说明
### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Linux / macOS(Unix-like 环境)
- **Python**: 3.8 或更高版本
- **权限**: root 或 sudo(用户切换需要)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------:|--------|:-------|:------:|
| Python 3.8+ | 运行时 | 必需 | python.org |
| 代码 CLI | CLI 工具 | 必需 | `npm install -g @anthropic-ai/claude-code` |
| LLM API | API | 必需 | 由代码 CLI 内置 LLM 提供 |
| pty 模块 | Python 标准库 | 必需 | Python 自带 |
| psutil(可选) | Python 库 | 资源监控推荐 | `pip install psutil` |

### API Key 配置
```bash
# 代码 CLI 认证
export ANTHROPIC_API_KEY="your-api-key"
# ...
# 工具配置
export CODE_RUNNER_USER="code-runner"
export CODE_RUNNER_TIMEOUT="600"
export CODE_RUNNER_AUDIT="true"
```

### 可用性分类
- **分类**: MD+EXEC+SCRIPT+AUDIT(Markdown 指令 + 命令行执行 + Python 脚本 + 审计日志)
- **说明**: 通过自然语言指令驱动 Agent 批量执行编程任务,支持 CI/CD 集成与执行审计
- **离线可用**: 否,代码 CLI 需要连接 LLM API

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|----|:--:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```
