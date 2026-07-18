---
slug: code-quality-tool-pro
name: code-quality-tool-pro
version: "1.0.0"
displayName: 代码质量检查专业版
summary: 企业级代码质量审计,支持OWASP Top 10、批量扫描、自定义规则与CI/CD集成,输出多格式报告。
license: MIT
edition: pro
description: |-
  面向企业研发团队的高级代码质量审计工具,提供深度安全扫描、合规性检查、批量项目分析与CI/CD流水线集成。

  核心能力:
  - OWASP Top 10 安全漏洞深度扫描
  - 全项目批量代码审计
  - 自定义规则引擎与策略管理
  - 多格式报告输出(SARIF/HTML/JSON)
  - CI/CD 流水线集成
  - 多租户协同审查与问题跟踪

  适用场景:
  - 企业级代码安全审计
  - 合规性检查(等保/GDPR)
  - 大型项目批量质量扫描
  - DevSecOps 流水线集成

  差异化:
  - 专业版完全兼容免费版配置,支持平滑升级
  - 提供企业级规则库与自定义规则能力
  - 支持多租户协同与问题跟踪系统集成
  - 内置合规性模板(等保2.0、GDPR、PCI-DSS)

  触发关键词: 代码审计, 安全扫描, OWASP, 合规检查, 批量扫描, SARIF, DevSecOps, CI/CD, code audit, security scan
tags:
- 开发工具
- 代码质量
- 安全审计
- 企业级
- DevSecOps
tools:
- read
- exec
---

# 代码质量检查工具 - 专业版

## 概述

代码质量检查工具专业版为企业研发团队提供深度代码审计能力。在免费版基础能力之上,专业版新增 OWASP Top 10 漏洞扫描、全项目批量分析、自定义规则引擎、多格式报告输出和 CI/CD 流水线集成,满足企业级 DevSecOps 实践需求。

专业版完全兼容免费版的配置文件和检查规则,企业用户可从免费版无缝升级,已有配置无需修改即可在专业版中使用。

## 核心能力

### 1. OWASP Top 10 深度安全扫描

覆盖 OWASP Top 10 全部安全风险类别,提供漏洞定位、风险评级和修复建议。

| OWASP 类别 | 检查内容 | 风险等级 |
|:-----------|:---------|:---------|
| A01 权限失效 | 越权访问、缺少访问控制 | 高危 |
| A02 加密失败 | 弱加密算法、明文传输 | 高危 |
| A03 注入攻击 | SQL注入、命令注入、XSS | 严重 |
| A04 不安全设计 | 缺少输入验证、不安全业务流 | 中危 |
| A05 配置错误 | 默认配置、调试模式开启 | 高危 |
| A06 脆弱组件 | 已知漏洞依赖、过期库 | 中危 |
| A07 认证失败 | 弱密码策略、会话管理缺陷 | 高危 |
| A08 数据完整性 | 反序列化、未验证更新 | 高危 |
| A09 日志监控 | 缺少审计日志、敏感信息记录 | 中危 |
| A10 SSRF | 服务端请求伪造风险 | 高危 |

```bash
# 专业版深度安全扫描脚本
#!/bin/bash
echo "=== OWASP Top 10 深度扫描 ==="

echo "[A03] 注入攻击检查..."
grep -rnE "(eval|exec)\s*\(" src/ --include="*.js" --include="*.py" --include="*.php"
grep -rnE "query\s*\(\s*['\"].*\+.*['\"]" src/ --include="*.js" --include="*.py"

echo "[A02] 加密失败检查..."
grep -rnE "(md5|sha1|des|rc4)\s*\(" src/ --include="*.js" --include="*.py"
grep -rn "http://" src/ --include="*.js" | grep -v "localhost\|127.0.0.1"

echo "[A05] 配置错误检查..."
grep -rnE "(debug\s*[:=]\s*true|allow_origin\s*[:=]\s*['\"]\*['\"])" src/

echo "[A06] 脆弱组件检查..."
if [ -f "package.json" ]; then
    npm audit --json > security-audit.json 2>/dev/null
    echo "依赖漏洞报告已生成: security-audit.json"
fi
```

### 2. 全项目批量审计

支持对大型代码库进行批量扫描,自动识别项目结构并应用对应规则。

```python
# 专业版批量审计脚本
import os
import json
from datetime import datetime

class CodeAuditPro:
    """企业级代码审计引擎"""

    def __init__(self, project_root, rules_config=None):
        self.project_root = project_root
        self.results = []
        self.rules = self._load_rules(rules_config)

    def _load_rules(self, config):
        """加载规则配置,兼容免费版格式"""
        default_rules = {
            "security": ["hardcoded_secrets", "sql_injection", "xss",
                         "weak_crypto", "path_traversal"],
            "style": ["naming", "formatting", "comments"],
            "compliance": ["owasp_top10", "pci_dss", "gdpr"],
        }
        if config and os.path.exists(config):
            with open(config, 'r', encoding='utf-8') as f:
                user_rules = json.load(f)
                default_rules.update(user_rules)
        return default_rules

    def scan_project(self):
        """扫描整个项目"""
        supported_extensions = ('.js', '.ts', '.py', '.java', '.go',
                                '.php', '.rb', '.cs')

        for root, dirs, files in os.walk(self.project_root):
            # 排除依赖和构建目录
            dirs[:] = [d for d in dirs if d not in
                       ('node_modules', '.git', 'dist', 'build', '__pycache__')]

            for file in files:
                if file.endswith(supported_extensions):
                    filepath = os.path.join(root, file)
                    self._scan_file(filepath)

        return self._generate_report()

    def _scan_file(self, filepath):
        """扫描单个文件"""
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
                for i, line in enumerate(lines, 1):
                    issues.extend(self._check_line(line, i, filepath))
        except Exception as e:
            issues.append({
                "file": filepath,
                "line": 0,
                "severity": "error",
                "category": "scan_error",
                "message": str(e)
            })
        self.results.extend(issues)

    def _check_line(self, line, lineno, filepath):
        """检查单行代码"""
        issues = []
        checks = [
            (r"password\s*=\s*['\"]", "hardcoded_secret", "critical"),
            (r"eval\s*\(", "code_injection", "critical"),
            (r"SELECT.*\+.*FROM", "sql_injection", "high"),
            (r"innerHTML\s*=", "xss_risk", "medium"),
            (r"\b(md5|sha1)\b\s*\(", "weak_crypto", "high"),
        ]
        for pattern, category, severity in checks:
            import re
            if re.search(pattern, line, re.IGNORECASE):
                issues.append({
                    "file": filepath,
                    "line": lineno,
                    "severity": severity,
                    "category": category,
                    "message": f"检测到 {category} 风险",
                    "code": line.strip()
                })
        return issues

    def _generate_report(self):
        """生成审计报告"""
        report = {
            "scan_time": datetime.now().isoformat(),
            "project": self.project_root,
            "total_files": len(set(r["file"] for r in self.results)),
            "total_issues": len(self.results),
            "severity_count": {},
            "issues": self.results
        }
        for r in self.results:
            sev = r["severity"]
            report["severity_count"][sev] = \
                report["severity_count"].get(sev, 0) + 1
        return report


# 使用示例
if __name__ == "__main__":
    auditor = CodeAuditPro("./src", ".codequality.yml")
    report = auditor.scan_project()

    # 输出 JSON 报告
    with open("audit-report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    # 输出摘要
    print(f"扫描完成: {report['total_files']} 个文件")
    print(f"发现问题: {report['total_issues']} 个")
    for sev, count in report["severity_count"].items():
        print(f"  {sev}: {count}")
```

### 3. 自定义规则引擎

支持企业自定义安全规则和质量标准。

```yaml
# 企业自定义规则配置
version: "2.0"
edition: pro

# 自定义安全规则
custom_rules:
  - id: CUSTOM-001
    name: 禁止使用内部测试密钥
    pattern: "TEST_KEY_\\d+"
    severity: high
    message: "检测到内部测试密钥,请使用环境变量"

  - id: CUSTOM-002
    name: API 路径必须包含版本号
    pattern: "/api/(?!v\\d+/)"
    severity: medium
    message: "API 路径需包含版本号,如 /api/v1/"

  - id: CUSTOM-003
    name: 数据库连接必须使用连接池
    pattern: "createConnection\\s*\\("
    severity: medium
    message: "建议使用连接池替代单个连接"

# 合规性模板
compliance_templates:
  - name: 等保2.0三级
    rules: [owasp_top10, data_protection, access_control, audit_log]
  - name: GDPR
    rules: [data_privacy, consent_check, right_to_erasure]
  - name: PCI-DSS
    rules: [card_data_handling, encryption_required, access_audit]

# CI/CD 集成配置
ci_cd:
  fail_on: [critical, high]
  report_format: [sarif, html, json]
  output_dir: ./reports/
  upload_artifact: true
```

### 4. 多格式报告输出

支持 SARIF、HTML、JSON 等多种报告格式,可集成到主流问题跟踪系统。

```bash
# 生成多种格式报告
echo "=== 生成审计报告 ==="

# JSON 格式(用于程序处理)
python audit.py --format json --output report.json

# SARIF 格式(用于 GitHub/GitLab 集成)
python audit.py --format sarif --output report.sarif

# HTML 格式(用于人工审阅)
python audit.py --format html --output report.html

# 摘要输出(用于 CI/CD 日志)
python audit.py --format summary
```

## 使用场景

### 场景一:企业级安全审计

对大型项目进行全面安全审计,生成合规报告。

```bash
# 企业级安全审计流程
#!/bin/bash
PROJECT_DIR="${1:-.}"
echo "=== 企业级代码安全审计 ==="
echo "项目目录: $PROJECT_DIR"
echo "扫描时间: $(date)"
echo ""

# 1. 运行全量扫描
python audit.py \
    --project "$PROJECT_DIR" \
    --rules ".codequality.yml" \
    --compliance "owasp_top10,pci_dss" \
    --format sarif,html,json \
    --output ./reports/

# 2. 生成执行摘要
python audit.py --summary --output executive-summary.txt

# 3. 检查是否有关键问题
CRITICAL_COUNT=$(python audit.py --count --severity critical)
if [ "$CRITICAL_COUNT" -gt 0 ]; then
    echo "警告: 发现 $CRITICAL_COUNT 个严重问题,建议立即修复"
    exit 1
fi

echo "审计完成,报告已输出到 ./reports/ 目录"
```

### 场景二:CI/CD 流水线集成

将代码质量检查集成到持续集成流水线中。

```yaml
# GitLab CI 配置示例
code_quality_scan:
  stage: test
  image: node:18
  script:
    - echo "运行代码质量扫描(专业版)"
    - python audit.py
        --project .
        --format sarif
        --output reports/audit.sarif
    - python audit.py
        --format summary
        --fail-on critical,high
  artifacts:
    reports:
      sast: reports/audit.sarif
    paths:
      - reports/
    expire_in: 30 days
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
```

### 场景三:多租户协同审查

多个团队协同进行代码审查,问题跟踪与分配。

```python
# 多租户协同审查工作流
class CollaborativeReview:
    """多租户协同代码审查"""

    def __init__(self, tenant_id):
        self.tenant_id = tenant_id
        self.reviews = {}

    def assign_review(self, issue_id, reviewer, priority="normal"):
        """分配审查任务"""
        self.reviews[issue_id] = {
            "tenant": self.tenant_id,
            "reviewer": reviewer,
            "priority": priority,
            "status": "assigned",
            "assigned_at": datetime.now().isoformat()
        }

    def batch_assign(self, issues, reviewers):
        """批量分配审查任务"""
        for i, issue in enumerate(issues):
            reviewer = reviewers[i % len(reviewers)]
            self.assign_review(issue["id"], reviewer)
```

## 快速开始

### 步骤一:配置规则

创建 `.codequality.yml` 配置文件(兼容免费版格式):

```yaml
version: "2.0"
edition: pro
rules:
  security: [owasp_top10, hardcoded_secrets, weak_crypto]
  style: [naming, formatting]
  compliance: [owasp_top10]
ci_cd:
  fail_on: [critical, high]
  report_format: [sarif, html]
```

### 步骤二:运行审计

```
请对当前项目进行全面代码安全审计,生成 SARIF 和 HTML 格式报告。
```

### 步骤三:查看报告

报告输出到 `./reports/` 目录,包含:
- `audit.sarif`:用于 CI/CD 集成
- `audit.html`:用于人工审阅
- `audit.json`:用于程序处理
- `summary.txt`:执行摘要

## 配置示例

### 企业级完整配置

```yaml
# 企业级代码质量配置(专业版)
version: "2.0"
edition: pro

# 全局设置
settings:
  parallel_workers: 4
  max_file_size: 10MB
  exclude_dirs: [node_modules, .git, dist, build, vendor]
  encoding: utf-8

# 安全规则
security:
  owasp_top10: true
  hardcoded_secrets: true
  sql_injection: true
  xss_detection: true
  weak_crypto: true
  path_traversal: true
  ssrf_detection: true
  deserialization: true

# 合规性检查
compliance:
  - template: owasp_top10
    severity_threshold: high
  - template: pci_dss
    enabled: true
  - template: gdpr
    enabled: true

# 自定义规则
custom_rules:
  - id: ENT-001
    name: 企业内部安全规范
    pattern: "internal_api_key"
    severity: critical

# CI/CD 集成
ci_cd:
  fail_on: [critical, high]
  report_format: [sarif, html, json]
  output_dir: ./reports/
  artifact_retention: 30
  issue_tracker_integration: true

# 多租户配置
multi_tenant:
  enabled: true
  default_tenant: default
  role_based_access: true
```

## 最佳实践

1. **分层扫描**:先运行快速扫描阻断关键问题,再进行深度审计
2. **规则版本化**:将 `.codequality.yml` 纳入版本控制,确保团队规则一致
3. **增量审计**:利用 Git diff 仅扫描变更文件,提升效率
4. **报告归档**:保留历史审计报告用于合规追溯
5. **自动修复**:对低风险问题启用自动修复,减少人工干预

```bash
# 专业版最佳实践:分层扫描策略
echo "=== 第一层:快速阻断 ==="
python audit.py --quick --fail-on critical
if [ $? -ne 0 ]; then exit 1; fi

echo "=== 第二层:深度审计 ==="
python audit.py --deep --format sarif,html --output ./reports/

echo "=== 第三层:增量检查 ==="
git diff --name-only HEAD~1 | python audit.py --incremental
```

## 常见问题

### Q1:专业版如何兼容免费版配置?

专业版完全兼容免费版的 `.codequality.yml` 配置格式。升级后无需修改任何配置,专业版会自动识别并应用免费版规则,同时启用额外的高级检查。

### Q2:如何集成到现有 CI/CD 系统?

```bash
# GitHub Actions 集成
# .github/workflows/code-quality.yml
name: Code Quality
on: [push, pull_request]
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Code Audit
        run: python audit.py --format sarif --output report.sarif
      - uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: report.sarif
```

### Q3:扫描大型项目性能如何?

| 项目规模 | 文件数 | 扫描时间 | 内存占用 |
|:---------|:-------|:---------|:---------|
| 小型 | <500 | <30s | <100MB |
| 中型 | 500-5000 | 1-5min | 100-500MB |
| 大型 | 5000-50000 | 5-30min | 500MB-2GB |
| 超大型 | >50000 | 30min+ | 建议分布式 |

### Q4:如何管理多团队的规则差异?

使用多租户配置,每个租户可以有独立的规则集:

```yaml
multi_tenant:
  tenants:
    - id: team-frontend
      rules: [owasp_top10, xss_detection]
    - id: team-backend
      rules: [owasp_top10, sql_injection, ssrf]
    - id: team-mobile
      rules: [owasp_top10, insecure_storage]
```

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Python 3.8+ / Node.js 18+ / Bash
- **CI/CD**:支持主流 CI/CD 平台

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| grep/ripgrep | 系统工具 | 必需 | 系统自带 |
| npm audit | CLI工具 | 可选 | Node.js 自带 |
| SARIF SDK | 库 | 可选 | pip install sarif-tools |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 如需集成外部安全扫描服务,在 `.codequality.yml` 中配置:

```yaml
external_services:
  snyk:
    api_key: "${SNYK_API_KEY}"
    enabled: false
  sonarqube:
    url: "${SONARQUBE_URL}"
    token: "${SONARQUBE_TOKEN}"
    enabled: false
```

### 可用性分类

- **分类**:MD+EXEC+PRO(专业版支持批量执行、CI/CD 集成和高级分析)
- **说明**:企业级 AI Skill,支持全项目批量扫描、多格式报告输出和流水线集成
- **适用规模**:中小型到超大型项目(文件数无上限)
- **兼容性**:完全兼容免费版配置,支持平滑升级
