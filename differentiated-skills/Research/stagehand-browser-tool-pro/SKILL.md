---
slug: stagehand-browser-tool-pro
name: stagehand-browser-tool-pro
version: "1.0.0"
displayName: 浏览器自动化工具专业版
summary: 企业级浏览器自动化平台,支持远程浏览器、批量任务调度、代理穿透与团队协作
license: MIT
edition: pro
description: |-
  浏览器自动化工具专业版,面向企业团队和高级用户提供完整的浏览器自动化解决方案。
  支持远程浏览器集群、批量任务调度、代理穿透、验证码处理、团队协作等高级能力。

  核心能力:
  - 远程浏览器集群(Browserbase),支持高并发和反爬虫场景
  - 批量任务调度与并行执行,提升大规模数据处理效率
  - 代理网络与验证码自动处理,应对复杂反爬环境
  - 会话持久化与团队协作,支持多用户共享浏览器配置
  - 完整兼容免费版所有功能,平滑升级无障碍

  适用场景:
  - 企业级数据采集与监控自动化
  - 电商竞品价格监控与情报收集
  - 跨境业务的多地区浏览器任务调度
  - QA 自动化测试与持续集成流程

  差异化:
  - 专业版提供远程浏览器集群,突破本地资源限制
  - 内置批量任务编排引擎,支持复杂工作流
  - 增强安全与合规能力,满足企业审计需求
  - 兼容免费版指令体系,迁移成本趋近于零

  触发关键词: 浏览器自动化, 远程浏览器, 批量任务, 代理穿透, 企业自动化, 数据采集, browser, stagehand, browserbase, enterprise
tags:
- 研究工具
- 浏览器自动化
- 企业级
- 批量处理
tools:
- read
- exec
---

# 浏览器自动化工具专业版

## 概述

浏览器自动化工具专业版是企业级的网页自动化解决方案。在完整兼容免费版所有本地浏览器能力的基础上,专业版引入了远程浏览器集群、批量任务调度、代理网络穿透、验证码自动处理等高级能力,适用于大规模数据采集、跨地区业务自动化、QA 测试集成等复杂企业场景。

专业版特别强化了团队协作和任务编排能力,支持多用户共享浏览器配置、任务优先级队列、执行日志审计等功能,满足企业级安全合规要求。

## 核心能力

### 1. 远程浏览器集群

通过远程浏览器服务(Browserbase)实现高并发、反爬虫场景下的稳定运行。

```bash
# 远程浏览器模式配置
# .env 文件配置
BROWSERBASE_API_KEY=your_api_key_here
BROWSERBASE_PROJECT_ID=your_project_id_here

# 启动远程浏览器会话
browser navigate https://target-site.com --mode remote

# 远程模式支持隐身模式
browser act "启用隐身模式浏览" --stealth

# 远程模式支持代理
browser navigate https://region-specific.com --proxy "us-east"
```

### 2. 批量任务调度

支持批量任务编排和并行执行,显著提升大规模数据处理效率。

```bash
# 批量任务配置文件 batch_tasks.json
{
  "tasks": [
    {"id": "task_001", "url": "https://site1.com", "action": "extract_titles"},
    {"id": "task_002", "url": "https://site2.com", "action": "extract_prices"},
    {"id": "task_003", "url": "https://site3.com", "action": "extract_reviews"}
  ],
  "concurrency": 5,
  "retry": 3,
  "timeout": 60000
}

# 执行批量任务
browser batch run batch_tasks.json

# 查看任务进度
browser batch status

# 导出任务结果
browser batch export --format csv --output results.csv
```

### 3. 代理网络与验证码处理

内置代理网络支持,自动应对验证码和反爬机制。

```bash
# 配置代理池
browser proxy configure proxies.json

# 自动验证码处理
browser act "填写表单并提交" --captcha auto

# 地理位置模拟
browser navigate https://region-site.com --geo "US,California"
```

### 4. 会话持久化与团队协作

支持浏览器会话持久化和团队配置共享。

```bash
# 保存当前浏览器会话
browser session save --name "project_a_session"

# 恢复之前的会话
browser session restore --name "project_a_session"

# 共享会话给团队成员
browser session share --name "project_a_session" --team "dev_team"
```

### 5. 完整兼容免费版

专业版完全兼容免费版的所有指令和配置,平滑升级。

```bash
# 免费版的所有命令在专业版中均可使用
browser navigate https://example.com
browser act "点击登录按钮"
browser extract "提取页面内容"
browser screenshot
browser close
```

## 使用场景

### 场景一:电商竞品价格监控

某电商平台运营团队需要每日监控 50 个竞品商品的价格变动,并生成对比报告。

```bash
# 步骤1:准备监控任务清单
cat > price_monitor.json << 'EOF'
{
  "tasks": [
    {"id": "p001", "url": "https://competitor-a.com/product/123", "extract": "price"},
    {"id": "p002", "url": "https://competitor-b.com/item/456", "extract": "price"},
    {"id": "p003", "url": "https://competitor-c.com/detail/789", "extract": "price"}
  ],
  "concurrency": 10,
  "schedule": "0 9 * * *"
}
EOF

# 步骤2:执行批量监控(远程浏览器,避开反爬)
browser batch run price_monitor.json --mode remote --stealth

# 步骤3:导出结果并生成报告
browser batch export --format json --output prices_$(date +%Y%m%d).json
browser report generate --input prices_*.json --template price_comparison
```

### 场景二:跨境业务多地区任务调度

一家跨境电商企业需要同时在美国、欧洲、东南亚三个地区执行本地化浏览器任务。

```bash
# 配置多地区任务
cat > global_tasks.json << 'EOF'
{
  "regions": [
    {"name": "US", "geo": "US,California", "tasks": [{"url": "https://us-site.com", "action": "extract_inventory"}]},
    {"name": "EU", "geo": "DE,Frankfurt", "tasks": [{"url": "https://eu-site.com", "action": "extract_inventory"}]},
    {"name": "SEA", "geo": "SG,Singapore", "tasks": [{"url": "https://sea-site.com", "action": "extract_inventory"}]}
  ],
  "concurrency": 3,
  "parallel_regions": true
}
EOF

# 执行多地区并行任务
browser batch run global_tasks.json --mode remote

# 汇总各地区数据
browser batch merge --output global_inventory.json
```

### 场景三:QA 自动化测试集成

QA 团队需要将浏览器自动化集成到持续集成流程中,每日执行回归测试。

```bash
# 测试用例配置
cat > regression_tests.json << 'EOF'
{
  "tests": [
    {"name": "login_flow", "url": "https://app.example.com/login", "steps": ["fill_form", "submit", "verify_dashboard"]},
    {"name": "checkout_flow", "url": "https://app.example.com/cart", "steps": ["add_item", "checkout", "verify_payment"]}
  ],
  "headless": true,
  "screenshot_on_failure": true
}
EOF

# 集成到 CI 流程(无头模式)
browser batch run regression_tests.json --headless --mode remote

# 生成测试报告
browser report generate --input test_results.json --template qa_report --output qa_report.html

# 失败用例自动重试
browser batch retry --failed-only --max-retries 3
```

## 快速开始

### 第一步:升级安装

如果已安装免费版,可直接升级到专业版:

```bash
# 进入工具目录
cd ~/.skill-platform/workspace/skills/stagehand-browser-tool-pro

# 安装专业版依赖(包含远程浏览器支持)
npm install

# 升级全局命令
npm link

# 验证专业版功能
browser --version --edition
```

### 第二步:配置远程浏览器

```bash
# 配置 Browserbase 远程浏览器服务
cat > .env << 'EOF'
BROWSERBASE_API_KEY=your_api_key_here
BROWSERBASE_PROJECT_ID=your_project_id_here

# 代理配置(可选)
PROXY_ENABLED=true
PROXY_POOL=premium

# 高级配置
MAX_CONCURRENT_SESSIONS=20
SESSION_TIMEOUT=300000
RETRY_ATTEMPTS=3
EOF

# 验证远程连接
browser navigate https://example.com --mode remote
```

### 第三步:运行首个批量任务

```bash
# 创建批量任务配置
cat > first_batch.json << 'EOF'
{
  "tasks": [
    {"id": "t1", "url": "https://example.com/page1", "action": "extract_content"},
    {"id": "t2", "url": "https://example.com/page2", "action": "extract_content"},
    {"id": "t3", "url": "https://example.com/page3", "action": "extract_content"}
  ],
  "concurrency": 3,
  "mode": "remote"
}
EOF

# 执行批量任务
browser batch run first_batch.json

# 查看执行结果
browser batch status
```

## 配置示例

### 企业级配置文件

```bash
# enterprise_config.json - 企业级完整配置
{
  "edition": "pro",
  "browser": {
    "default_mode": "remote",
    "fallback_to_local": true,
    "headless": true,
    "stealth": true,
    "timeout": 60000
  },
  "batch": {
    "max_concurrency": 20,
    "retry_attempts": 3,
    "retry_delay": 5000,
    "priority_queue": true
  },
  "proxy": {
    "enabled": true,
    "pool": "premium",
    "rotation": "per_session",
    "geo_targeting": true
  },
  "security": {
    "session_encryption": true,
    "audit_log": true,
    "data_retention_days": 30
  },
  "team": {
    "shared_sessions": true,
    "role_based_access": true,
    "collaboration": true
  }
}
```

### 团队协作配置

```bash
# team_config.json - 团队协作配置
{
  "team": {
    "name": "automation_team",
    "members": ["alice", "bob", "charlie"],
    "shared_configs": true,
    "session_sharing": true
  },
  "permissions": {
    "admin": ["batch_run", "session_manage", "config_edit"],
    "operator": ["batch_run", "session_use"],
    "viewer": ["batch_status", "report_view"]
  }
}
```

## 最佳实践

### 1. 免费版到专业版的平滑迁移

专业版完全兼容免费版指令,迁移时只需更新依赖和配置:

```bash
# 1. 备份免费版配置
cp ~/.skill-platform/workspace/skills/stagehand-browser-tool-free/.env .env.backup

# 2. 安装专业版
cd ~/.skill-platform/workspace/skills/stagehand-browser-tool-pro
npm install && npm link

# 3. 恢复配置(免费版配置在专业版中完全有效)
cp .env.backup .env

# 4. 验证原有脚本仍可运行
browser navigate https://example.com
browser extract "页面标题"
```

### 2. 批量任务的容错与重试

```bash
# 配置自动重试和容错
{
  "tasks": [...],
  "retry": {
    "attempts": 3,
    "delay": 5000,
    "backoff": "exponential"
  },
  "fallback": {
    "enabled": true,
    "mode": "local",
    "on_error": "continue"
  }
}
```

### 3. 资源利用优化

```bash
# 根据任务复杂度调整并发数
# 简单任务:高并发
browser batch run simple_tasks.json --concurrency 20

# 复杂任务:适中并发,避免超时
browser batch run complex_tasks.json --concurrency 5 --timeout 120000
```

### 4. 安全与审计

```bash
# 启用审计日志
browser config set audit_log true

# 查看操作日志
browser audit log --date $(date +%Y-%m-%d)

# 导出审计报告
browser audit export --format csv --output audit_report.csv
```

## 免费版与专业版对比

| 功能特性 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 本地浏览器操作 | 支持 | 支持 |
| 自然语言指令 | 支持 | 支持 |
| 页面导航与提取 | 支持 | 支持 |
| 远程浏览器集群 | 不支持 | 支持 |
| 批量任务调度 | 不支持 | 支持 |
| 代理网络穿透 | 不支持 | 支持 |
| 验证码自动处理 | 不支持 | 支持 |
| 会话持久化 | 不支持 | 支持 |
| 团队协作 | 不支持 | 支持 |
| 审计日志 | 不支持 | 支持 |
| 并发执行 | 单实例 | 多实例并行 |
| 适用场景 | 个人使用 | 企业级应用 |
| 技术支持 | 社区支持 | 优先支持 |

## 常见问题

### Q1: 专业版是否兼容免费版的脚本?

**A:** 完全兼容。专业版是免费版的超集,所有免费版指令和配置在专业版中均可直接使用,无需修改。

### Q2: 远程浏览器服务如何计费?

**A:** 远程浏览器服务(Browserbase)按使用量计费,具体费用请参考服务提供商的定价方案。专业版本身不额外收费,您只需为远程浏览器服务的实际使用量付费。

### Q3: 批量任务失败后如何排查?

**A:** 专业版提供详细的任务执行日志:

```bash
# 查看失败任务详情
browser batch status --failed

# 查看特定任务的执行日志
browser batch log --task-id task_001

# 查看失败任务的截图
browser batch screenshots --task-id task_001
```

### Q4: 如何限制团队成员的权限?

**A:** 通过团队权限配置实现细粒度访问控制:

```bash
# 配置角色权限
browser team config set --role operator --permissions "batch_run,session_use"
browser team config set --role viewer --permissions "batch_status,report_view"
```

### Q5: 数据安全如何保障?

**A:** 专业版提供多重安全保障:

- 会话加密存储,敏感数据不落地
- 完整审计日志,所有操作可追溯
- 基于角色的访问控制(RBAC)
- 数据保留策略可配置,自动清理过期数据

## 依赖说明

### 运行环境

- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18.0.0 及以上版本
- **Chrome 浏览器**: 100 及以上版本(本地模式需要)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | 官方网站下载安装 |
| Chrome 浏览器 | 浏览器 | 本地模式必需 | 官方网站下载安装 |
| Browserbase API | 远程服务 | 远程模式必需 | 官方网站注册获取 |
| 代理服务 | 网络 | 代理模式必需 | 代理服务提供商 |
| npm 依赖包 | 库 | 必需 | 通过 `npm install` 自动安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

专业版需要以下 API Key 配置:

```bash
# .env 文件配置
# 远程浏览器服务
BROWSERBASE_API_KEY=your_browserbase_api_key
BROWSERBASE_PROJECT_ID=your_project_id

# 代理服务(可选)
PROXY_API_KEY=your_proxy_api_key

# 团队协作服务(可选)
TEAM_API_TOKEN=your_team_api_token
```

### 可用性分类

- **分类**: MD+EXEC+API(综合型,支持本地执行、远程 API 调用和批量任务编排)
- **说明**: 企业级浏览器自动化平台,支持本地和远程浏览器、批量任务调度、团队协作等高级功能
- **适用规模**: 多用户、多浏览器实例、本地与远程混合部署
- **兼容性**: 完全兼容免费版,支持平滑升级
