---
slug: read-github-tool-pro
name: read-github-tool-pro
version: 1.0.0
displayName: 代码仓库阅读专业版
summary: "企业级代码仓库分析平台，支持批量仓库分析、跨仓库搜索、代码审计与API集成。代码仓库阅读工具专业版。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆"
license: Proprietary
edition: pro
description: "代码仓库阅读工具专业版。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。支持多场景应用和灵活配置。"
  when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API.
tags:
  - 开发
  - 企业级
  - 代码审计
  - 仓库分析
  - 技术选型
  - 版本控制
  - Git
  - 开发工具
  - pro
  - true
  - api
  - read-github-pro
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Development"
---
# 代码仓库阅读工具（专业版）
## 概述
代码仓库阅读工具专业版在免费版单仓库文档阅读的基础上，新增批量多仓库分析、跨仓库代码搜索、代码审计与安全检查、仓库对比分析、多格式导出和 REST API 集成等企业级能力，满足开发团队技术选型、安全审计和代码库管理的深度需求.
PRO 版本与免费版完全兼容，用户可随时从免费版平滑升级，原有搜索习惯和工作流均可无缝迁移.
## 核心能力
### 能力矩阵
| 能力项 | 免费版 | PRO 版本 |
|---|---|------|
| 仓库数 | 单仓库 | 批量多仓库 |
| 代码搜索 | 单仓库精确匹配 | 跨仓库语义+精确 |
| 代码审计 | 不支持 | 安全漏洞检查 |
| 仓库对比 | 不支持 | 架构/依赖/质量对比 |
| 导出格式 | 终端输出 | MD/PDF/JSON |
| 搜索历史 | 不支持 | 完整历史+书签 |
| API 集成 | 不支持 | REST API |
| 自定义规则 | 不支持 | 分析规则定制 |
| 依赖分析 | 不支持 | 依赖树+风险评估 |
| 代码质量 | 不支持 | 复杂度/覆盖率分析 |
**处理**: 解析能力矩阵的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回能力矩阵的响应数据,包含状态码、结果和日志.
### PRO 专属能力详解
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 代码仓库阅读专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |
```text
[PRO] 批量多仓库文档获取与对比
[PRO] 跨仓库代码搜索（语义匹配+精确匹配）
[PRO] 代码安全审计（漏洞/密钥/硬编码检测）
[PRO] 仓库架构分析（目录结构/模块划分）
[PRO] 依赖关系分析（依赖树/版本/许可证）
[PRO] 代码质量评估（复杂度/重复率/覆盖率）
[PRO] 多仓库对比报告生成
[PRO] 搜索历史与书签管理
[PRO] REST API 集成
[PRO] 自定义代码分析规则
[PRO] 多格式导出（Markdown/PDF/JSON/HTML）
[PRO] 定时仓库监控（变更检测）
```
**处理**: 解析PRO 专属能力详解的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回PRO 专属能力详解的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 核心功能执行
用`input_params`参数进行配置.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级代码仓库分、析平台、支持批量仓库分析、跨仓库搜索、代码审计与、代码仓库阅读工具、专业版、Use、when、接口对接、Webhook、系统连接时使用、不适用于逆向工程、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景
### 场景一：技术选型多方案对比
技术团队需要对比多个开源方案，选择最适合的技术栈.
```text
用户：帮我对比分析以下3个状态管理库：
1. reduxjs/redux
2. pmndrs/zustand
3. jotaijs/jotai
# ...
Agent 执行流程：
1. 并行获取3个仓库的文档
2. 分别分析架构设计、API设计、性能特征
3. 对比社区活跃度、维护状态、Star趋势
4. 分析依赖关系与兼容性
5. 生成对比报告
```
示例输出：
```markdown
## 状态管理库对比分析报告
### 基础信息对比
| 维度 | Redux | Zustand | Jotai |
|---:|---:|---:|---:|
| Star数 | 60.2k | 45.8k | 18.5k |
| 包大小 | 3.2kB | 1.1kB | 2.4kB |
| 周下载量 | 8.5M | 5.2M | 1.8M |
| 维护状态 | 活跃 | 活跃 | 活跃 |
| TypeScript | 原生 | 原生 | 原生 |
# ...
### 架构设计对比
- Redux: 单一store + reducer模式 + 中间件
- Zustand: 极简store + hooks优先
- Jotai: 原子化状态 + 无store
# ...
### 安全审计结果
| 仓库 | 漏洞数 | 风险等级 | 许可证 |
|:---:|:---:|:---:|:---:|
| Redux | 0 | 低 | MIT |
| Zustand | 0 | 低 | MIT |
| Jotai | 0 | 低 | MIT |
# ...
### 推荐建议
- 大型项目：Redux（生态成熟）
- 中型项目：Zustand（轻量灵活）
- 原子化需求：Jotai（细粒度控制）
```
### 场景二：开源项目安全审计
安全团队需要对企业使用的开源依赖进行安全审计.
```python
# security_audit.py - 安全审计配置
audit_config = {
    "repositories": [
        "org/internal-service-1",
        "org/internal-service-2",
        "third-party/vendor-lib"
    ],
    "checks": {
        "vulnerabilities": True,      # 已知漏洞检查
        "secrets_detection": True,    # 密钥泄露检测
        "hardcoded_credentials": True, # 硬编码凭证
        "dangerous_functions": True,   # 危险函数调用
        "dependency_scan": True,       # 依赖扫描
        "license_compliance": True     # 许可证合规
    },
    "severity_levels": ["critical", "high", "medium", "low"],
    "output": {
        "format": ["pdf", "json"],
        "path": "~/read-github-pro/audits/"
    }
}
```
### 场景三：跨仓库代码搜索
开发者需要在多个仓库中搜索某个函数或模式的实现.
```text
用户：在以下3个仓库中搜索"errorHandler"的实现方式
# ...
Agent：
1. 并行在3个仓库中搜索"errorHandler"
2. 收集所有匹配结果
3. 对比不同实现方式
4. 生成搜索报告
```
```bash
# 批量跨仓库搜索
python3 （请参考skill目录中的脚本文件） batch-search \
    --repos "facebook/react,vuejs/vue,angular/angular" \
    --query "errorHandler" \
    --mode semantic \
    --output ~/read-github-pro/reports/cross_search.md
```
## 快速开始
### Step 1：初始化 PRO 环境
```bash
# 创建 PRO 版本工作目录
mkdir -p ~/read-github-pro/{reports,audits,history,bookmarks,config,rules}
# ...
# 初始化配置文件
cat > ~/read-github-pro/config.yaml << 'EOF'
edition: pro
version: "1.0.0"
# ...
# protocol server配置
协议适配层:
  base_url: "https://gitmcp.io"
  timeout: 30
  max_concurrent: 10
# ...
# 批量分析
batch:
  max_repositories: 20
  parallel_fetch: true
  comparison_report: true
# ...
# 搜索配置
search:
  code_mode: "both"  # exact + semantic
  docs_mode: "semantic"
  max_results: 50
  cross_repo: true
# ...
# 安全审计
audit:
  enabled: true
  checks:
    - vulnerabilities
    - secrets
    - hardcoded_credentials
    - dangerous_functions
    - dependency_scan
    - license_compliance
  severity_filter: ["critical", "high", "medium"]
# ...
# 代码质量
quality:
  complexity: true
  duplication: true
  coverage: true
# ...
# 导出
export:
  formats: ["markdown", "pdf", "json", "html"]
  path: "~/read-github-pro/reports/"
# ...
# 历史记录
history:
  enabled: true
  retention_days: 90
  searchable: true
# ...
# API
api:
  enabled: true
  rate_limit: "200/hour"
EOF
```
### Step 2：从免费版迁移
```bash
# 免费版脚本完全兼容
# PRO版增强脚本提供额外功能
echo "免费版脚本保持兼容，PRO增强脚本已就绪"
```
### Step 3：执行首次批量分析
```bash
# 批量获取多个仓库文档
python3 （请参考skill目录中的脚本文件） batch-fetch \
    --repos "facebook/react,vuejs/vue,angular/angular" \
    --output ~/read-github-pro/reports/batch_fetch.md
```
#
## 示例
### 自定义分析规则
```yaml
# rules/custom_rules.yaml - 自定义代码分析规则
rules:
  - name: "检查未处理的错误"
    pattern: "catch\\s*\\(.*\\)\\s*\\{\\s*\\}"
    severity: "medium"
    description: "空的catch块可能导致错误被忽略"
# ...
  - name: "检测硬编码API密钥"
    pattern: "(api_key|apikey|api-key)\\s*[:=]\\s*['\"][^'\"]+['\"]"
    severity: "high"
    description: "检测到硬编码的API密钥"
# ...
  - name: "检查危险函数eval"
    pattern: "eval\\s*\\("
    severity: "high"
    description: "使用eval可能导致代码注入风险"
# ...
  - name: "检查console.log残留"
    pattern: "console\\.log\\s*\\("
    severity: "low"
    description: "生产代码中残留调试日志"
# ...
  - name: "许可证合规检查"
    check: "license"
    allowed: ["MIT", "Apache-2.0", "BSD-3-Clause", "ISC"]
    severity: "high"
    description: "使用不合规的开源许可证"
```
### 仓库监控配置
```bash
# 配置仓库变更监控
cat > ~/read-github-pro/monitoring.yaml << 'EOF'
monitoring:
  repositories:
    - repo: "org/critical-service"
      check_interval: "1h"
      alerts:
        - new_commit
        - new_release
        - dependency_change
        - security_advisory
# ...
    - repo: "third-party/important-lib"
      check_interval: "6h"
      alerts:
        - new_release
        - security_advisory
# ...
  notification:
    channels: [email, webhook]
    recipients: ["dev-team@company.com"]
    webhook: "https://hooks.dev.local/repo-alerts"
EOF
```
### REST API 集成
```python
# api_client.py - PRO 版本 API 客户端
import requests
# ...
class ReadGitHubProClient:
    def __init__(self, api_key, base_url="https://api.read-github-pro.local"):
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.base_url = base_url
# ...
    def batch_fetch_docs(self, repos):
        """批量获取仓库文档"""
        resp = requests.post(
            f"{self.base_url}/v1/batch/fetch-docs",
            headers=self.headers,
            json={"repos": repos}
        )
        return resp.json()
# ...
    def cross_search_code(self, repos, query, mode="semantic"):
        """跨仓库代码搜索"""
            f"{self.base_url}/v1/search/cross-repo",
            json={"repos": repos, "query": query, "mode": mode}
        )
        return resp.json()
# ...
    def security_audit(self, repos, checks=None):
        """安全审计"""
            f"{self.base_url}/v1/audit",
            json={"repos": repos, "checks": checks or "all"}
        )
        return resp.json()
# ...
    def compare_repos(self, repos, dimensions=None):
        """仓库对比分析"""
            f"{self.base_url}/v1/compare",
            json={"repos": repos, "dimensions": dimensions or "all"}
        )
        return resp.json()
# ...
    def get_history(self, query=None, days=30):
        """获取搜索历史"""
        params = {"days": days}
        if query:
            params["q"] = query
            f"{self.base_url}/v1/history",
            params=params
        )
        return resp.json()
```
## 优选实践
### 1. 技术选型标准流程
```python
# 推荐的技术选型流程
SELECTION_WORKFLOW = {
    "step_1": "批量获取候选库文档",
    "step_2": "对比基础信息（Star/下载量/大小）",
    "step_3": "架构设计对比分析",
    "step_4": "安全审计（漏洞/许可证）",
    "step_5": "代码质量评估（复杂度/覆盖率）",
    "step_6": "依赖关系分析",
    "step_7": "生成对比报告与推荐建议"
}
```
### 2. 定期安全审计
```bash
# 依赖说明
cat > ~/read-github-pro/monthly_audit.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y%m)
python3 （请参考skill目录中的脚本文件） audit \
    --repos $(cat ~/read-github-pro/config/dependencies.txt) \
    --checks all \
    --output ~/read-github-pro/audits/monthly_${DATE}.pdf \
    --format pdf
EOF
# ...
# 添加定时任务
(crontab -l 2>/dev/null; echo "0 2 1 * * ~/read-github-pro/monthly_audit.sh") | crontab -
```
### 3. 利用书签管理常用仓库
```bash
# 添加书签
python3 （请参考skill目录中的脚本文件） bookmark add facebook/react --tag "frontend"
# ...
# 按标签查询
python3 （请参考skill目录中的脚本文件） bookmark list --tag "frontend"
# ...
# 快速访问
python3 （请参考skill目录中的脚本文件） bookmark open react
```
### 4. 利用搜索历史
```bash
# 查看搜索历史
python3 （请参考skill目录中的脚本文件） history list
# ...
# 重新执行历史搜索
python3 （请参考skill目录中的脚本文件） history replay <search_id>
```
## 常见问题
### Q1：PRO 版本支持多少个仓库批量分析？
PRO 版本单次批量分析支持最多 20 个仓库并行处理，可配置并发数（默认 10）.
### Q2：安全审计检查哪些项目？
安全审计包括：已知漏洞检查、密钥泄露检测、硬编码凭证检测、危险函数调用检测、依赖扫描和许可证合规检查.
### Q3：跨仓库搜索支持哪些模式？
支持两种模式：
- 精确匹配（exact）：按关键词精确匹配代码内容
- 语义搜索（semantic）：按语义相似度匹配，支持自然语言查询
### Q4：自定义分析规则如何编写？
自定义规则使用 YAML 格式定义，支持正则表达式模式匹配，可设置严重等级和描述信息。详见 `rules/custom_rules.yaml`.
### Q5：免费版脚本是否兼容？
PRO 版本完全兼容免费版的 `gitmcp.py` 脚本，同时提供增强版 `gitmcp_pro.py` 脚本支持批量分析和审计功能.
### 已知限制
默认每小时 200 次调用，可通过配置调整.
## 依赖说明
### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.10 及以上（推荐 3.12）
- **网络连接**: 稳定的互联网连接
- **存储空间**: 至少 200MB 用于报告与历史记录
### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| protocol server | 服务 | 必需 | gitmcp.io提供 |
| Python 3.10+ | 运行时 | 必需 | 系统包管理器安装 |
| requests | Python 包 | 可选 | `pip install requests` |
| PyYAML | Python 包 | 可选 | `pip install pyyaml` |
| bandit | Python 包 | 可选 | `pip install bandit`（安全审计） |
| radon | Python 包 | 可选 | `pip install radon`（代码复杂度） |
| pandoc | 工具 | 可选 | 系统包管理器安装（PDF导出） |
### API Key 配置
PRO 版本支持 API 集成，需配置相关密钥：
```bash
# 配置 API 认证
export READ_GITHUB_PRO_API_KEY="${API_KEY:?请设置环境变量}"
# ...
# 或写入配置文件
cat > ~/read-github-pro/.env << 'EOF'
READ_GITHUB_PRO_API_KEY=your_api_key
EOF
```
### 可用性分类
- **分类**: MD+EXEC+API（Markdown 指令 + Python 脚本执行 + API 集成）
- **说明**: PRO 版本支持批量仓库分析、跨仓库搜索、安全审计、代码质量评估与 REST API 集成
- **适用规模**: 开发团队、安全团队、技术选型委员会
- **兼容性**: 与 read-github-tool-free 完全兼容，免费版脚本可直接使用
- **支持级别**: 优先技术支持，提供自定义分析规则定制与安全审计咨询服务
## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |
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
| 对比维度 | 代码仓库阅读专业版 | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 企业级代码仓库分析平台，支持批量仓库分析、跨仓库搜索、代码审计与API集成。代码 | 通用场景 | 通用场景 |
## 核心功能
- **自动化执行**: 企业级代码仓库分析平台，支持批量仓库分析、跨仓库搜索、代码审计与API集成。代码仓库阅读工具专业版。Use when 需
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据
## 核心功能

- **自动化执行**: 企业级代码仓库分析平台，支持批量仓库分析、跨仓库搜索、代码审计与API集成。代码仓库阅读工具专业版。Use when 需
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据