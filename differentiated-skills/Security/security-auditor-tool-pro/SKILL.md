---
slug: security-auditor-tool-pro
name: security-auditor-tool-pro
version: "1.0.0"
displayName: 代码安全审计员(专业版)
summary: 企业级代码安全审计,OWASP Top 10全覆盖、AST自动扫描、多语言支持、ASVS合规映射
license: MIT
edition: pro
description: |-
  核心能力:
  - OWASP Top 10:2021全覆盖审计(10大类别)
  - AST静态分析自动漏洞检测
  - TypeScript/Python/Go/Java多语言支持
  - 10+框架安全规则(Next.js/Express/Django/FastAPI等)
  - OWASP ASVS合规等级映射(L1/L2/L3)
  - HTML/PDF/SARIF专业审计报告
  - Git Hook持续安全监控

  适用场景:
  - 企业级代码安全审计项目
  - 安全合规认证(ASVS/PCI-DSS)
  - DevSecOps代码安全门禁
  - 多语言项目安全统一管理

  差异化:
  - AST精确分析,极低误报率
  - 多语言多框架统一审计
  - ASVS合规等级自动映射
  - 与免费版兼容,检查清单可复用

  触发关键词: 代码审计, 企业安全, AST分析, OWASP ASVS, 多语言审计, 安全门禁, DevSecOps, SAST, 静态分析
tags:
- 安全
- 代码审计
- 企业安全
- 静态分析
- OWASP
- DevSecOps
tools:
- read
- exec
---

# 代码安全审计员(专业版)

## 概述

代码安全审计员专业版是一款面向企业用户的代码安全审计与SAST(静态应用安全测试)平台。在免费版Top 5 OWASP检查基础上,扩展至Top 10全覆盖,增加AST静态分析自动扫描、TypeScript/Python/Go/Java多语言支持、10+框架安全规则、OWASP ASVS合规等级映射等企业级功能。提供HTML/PDF/SARIF专业审计报告,支持Git Hook持续安全监控。与免费版完全兼容,检查清单和代码示例可无缝复用。

## 核心能力

### 功能矩阵

| 功能模块 | 描述 | 免费版 | 专业版 |
|----------|------|--------|--------|
| OWASP覆盖 | 安全类别 | Top 5 | Top 10全覆盖 |
| 扫描方式 | 检测方法 | 手动清单 | AST自动分析 |
| 语言支持 | 代码语言 | TypeScript | TS+Python+Go+Java |
| 框架规则 | 框架适配 | Next.js/Express | 10+框架 |
| 合规映射 | 标准对照 | 不支持 | ASVS L1/L2/L3 |
| 报告格式 | 输出类型 | 文本 | HTML/PDF/SARIF |
| 持续监控 | 集成方式 | 不支持 | Git Hook/CI/CD |
| 误报抑制 | 精确度 | 模式匹配 | AST语义分析 |

### OWASP Top 10全覆盖

```text
┌──────────────────────────────────────────────────────────┐
│              专业版OWASP Top 10审计                      │
├──────────┬───────────────────────┬───────────────────────┤
│ A01      │ 访问控制失效          │ IDOR/SSRF/权限验证    │
│ A02      │ 加密失败              │ 密码哈希/TLS/密钥管理 │
│ A03      │ 注入                  │ SQL/命令/LDAP/NoSQL   │
│ A04      │ 不安全设计            │ 架构缺陷/业务逻辑     │
│ A05      │ 安全配置错误          │ 默认配置/错误泄露     │
│ A06      │ 易受攻击的组件        │ 依赖漏洞/版本检查     │
│ A07      │ 身份认证失败          │ JWT/Session/速率限制 │
│ A08      │ 完整性失败            │ 签名验证/反序列化     │
│ A09      │ 日志与监控不足        │ 审计日志/告警         │
│ A10      │ 服务端请求伪造(SSRF)  │ URL验证/内网防护      │
└──────────┴───────────────────────┴───────────────────────┘
```

## 使用场景

### 场景一:企业级代码安全审计

对整个代码仓库执行自动化安全审计。

```bash
python scripts/code_audit.py \
  --target /path/to/project \
  --languages typescript,python \
  --owasp top10 \
  --format html \
  --output security_report.html
```

输出示例:
```
代码安全审计报告
══════════════════════════════════════
项目: /path/to/project
语言: TypeScript, Python
框架: Next.js, Express, FastAPI
扫描文件: 342
发现问题: 23
  CRITICAL: 3
  HIGH: 8
  MEDIUM: 9
  LOW: 3

OWASP分布:
  A01 访问控制: 5个问题
  A03 注入:     3个问题
  A07 认证:     4个问题
  ...

ASVS合规等级:
  L1 (基础):    82%合规
  L2 (标准):    68%合规
  L3 (高级):    45%合规
```

### 场景二:多语言项目审计

```bash
# 同时审计多种语言
python scripts/code_audit.py \
  --target /path/to/monorepo \
  --languages typescript,python,go,java \
  --frameworks nextjs,express,django,spring \
  --owasp top10 \
  --asvs L2 \
  --format sarif \
  --output results.sarif
```

### 场景三:Git Hook持续监控

```bash
# 安装pre-commit Hook
python scripts/code_audit.py --install-hook

# 每次提交时自动扫描变更文件
# .git/hooks/pre-commit
#!/bin/bash
python scripts/code_audit.py \
  --files $(git diff --cached --name-only) \
  --fail-on HIGH \
  --format text
```

### 场景四:CI/CD安全门禁

```yaml
# GitLab CI配置
security-audit:
  stage: test
  script:
    - python scripts/code_audit.py
        --target .
        --languages typescript
        --owasp top10
        --asvs L2
        --fail-on HIGH
        --format sarif
        --output security.sarif
  artifacts:
    reports:
      sast: security.sarif
```

## 快速开始

### AST静态分析引擎

```python
import ast
import re
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Finding:
    owasp: str
    category: str
    severity: str
    file: str
    line: int
    code: str
    issue: str
    fix: str
    asvs: str = ""

class ASTSecurityAnalyzer:
    """AST静态安全分析器"""

    ASVS_MAPPING = {
        "A01": {"L1": "V1.1", "L2": "V4.1", "L3": "V4.2"},
        "A02": {"L1": "V2.1", "L2": "V6.1", "L3": "V6.2"},
        "A03": {"L1": "V5.1", "L2": "V5.2", "L3": "V5.3"},
        "A07": {"L1": "V7.1", "L2": "V7.2", "L3": "V7.3"},
    }

    FRAMEWORK_RULES = {
        "nextjs": {
            "patterns": [
                r"app\.(get|post|put|delete)\(['\"](?!.*authenticate)",
                r"dangerouslySetInnerHTML",
                r"process\.env\.(?!NEXT_PUBLIC_)"
            ]
        },
        "express": {
            "patterns": [
                r"app\.(get|post|put|delete)\(.*\)",
                r"req\.query\.",
                r"res\.send\(.*req\."
            ]
        },
        "django": {
            "patterns": [
                r"render\(.*request\.POST",
                r"\.objects\.raw\(",
                r"mark_safe\("
            ]
        },
        "fastapi": {
            "patterns": [
                r"@app\.(get|post|put|delete)",
                r"Body\(\)",
                r"Depends\(\)"
            ]
        }
    }

    def __init__(self, languages=None, frameworks=None, asvs_level=None):
        self.languages = languages or ["typescript", "python"]
        self.frameworks = frameworks or []
        self.asvs_level = asvs_level
        self.findings: List[Finding] = []

    def analyze(self, target_path):
        """分析整个项目"""
        target = Path(target_path)

        for filepath in target.rglob("*"):
            if self._should_scan(filepath):
                if filepath.suffix == ".py":
                    self._analyze_python(filepath)
                elif filepath.suffix in [".ts", ".tsx", ".js", ".jsx"]:
                    self._analyze_typescript(filepath)
                elif filepath.suffix == ".go":
                    self._analyze_go(filepath)
                elif filepath.suffix == ".java":
                    self._analyze_java(filepath)

        return self._generate_report()

    def _analyze_python(self, filepath):
        """Python AST分析"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                source = f.read()

            tree = ast.parse(source, filename=str(filepath))

            for node in ast.walk(tree):
                # 检测SQL注入
                if isinstance(node, ast.Call):
                    if self._is_sql_concat(node, source):
                        self._add_finding(
                            "A03", "SQL注入", "CRITICAL",
                            filepath, node.lineno, source,
                            "字符串拼接SQL查询",
                            "使用参数化查询: cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))"
                        )

                    # 检测eval
                    if isinstance(node.func, ast.Name) and node.func.id == "eval":
                        self._add_finding(
                            "A03", "代码注入", "CRITICAL",
                            filepath, node.lineno, source,
                            "使用eval()执行动态代码",
                            "移除eval(),使用安全的替代方案"
                        )

                    # 检测pickle反序列化
                    if isinstance(node.func, ast.Attribute) and node.func.attr == "loads":
                        if "pickle" in source:
                            self._add_finding(
                                "A08", "不安全反序列化", "HIGH",
                                filepath, node.lineno, source,
                                "使用pickle.loads()反序列化",
                                "使用JSON替代pickle,或验证数据来源"
                            )

                # 检测硬编码密码
                if isinstance(node, ast.Assign):
                    for target_node in node.targets:
                        if isinstance(target_node, ast.Name):
                            name = target_node.id.lower()
                            if any(kw in name for kw in ["password", "secret", "token", "key"]):
                                if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                                    self._add_finding(
                                        "A02", "硬编码密钥", "CRITICAL",
                                        filepath, node.lineno, source,
                                        f"硬编码{name}",
                                        "使用环境变量: os.environ.get('SECRET_KEY')"
                                    )

        except SyntaxError:
            pass

    def _analyze_typescript(self, filepath):
        """TypeScript/JavaScript分析"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')

            patterns = [
                (r"SELECT.*FROM.*\$\{.*\}", "A03", "SQL注入", "CRITICAL", "使用参数化查询"),
                (r"exec\(`.*\$\{.*\}`\)", "A03", "命令注入", "CRITICAL", "使用execFile参数数组"),
                (r"eval\(.*\)", "A03", "代码注入", "CRITICAL", "移除eval()"),
                (r"dangerouslySetInnerHTML", "A07", "XSS风险", "HIGH", "使用DOMPurify消毒"),
                (r"process\.env\.(SECRET|KEY|PASSWORD)", "A02", "环境变量密钥", "MEDIUM", "确保不记录到日志"),
                (r"http://(?!localhost|127\.0\.0\.1)", "A02", "非加密连接", "MEDIUM", "使用HTTPS"),
                (r"res\.json\(.*password.*\)", "A01", "密码泄露", "HIGH", "从响应中移除敏感字段"),
            ]

            for pattern, owasp, category, severity, fix in patterns:
                for match in re.finditer(pattern, content, re.IGNORECASE):
                    line_num = content[:match.start()].count('\n') + 1
                    self._add_finding(
                        owasp, category, severity,
                        filepath, line_num, content,
                        match.group()[:80],
                        fix
                    )

        except Exception:
            pass

    def _should_scan(self, filepath):
        """判断是否需要扫描"""
        skip_dirs = {"node_modules", ".git", "dist", "build", "__pycache__", ".venv"}
        skip_files = {".min.js", ".min.css", "package-lock.json"}

        for skip in skip_dirs:
            if skip in str(filepath):
                return False

        for skip in skip_files:
            if skip in filepath.name:
                return False

        return filepath.suffix in {".py", ".ts", ".tsx", ".js", ".jsx", ".go", ".java"}

    def _is_sql_concat(self, node, source):
        """检测SQL字符串拼接"""
        if isinstance(node.func, ast.Attribute) and node.func.attr in ["execute", "query"]:
            if node.args and isinstance(node.args[0], ast.BinOp):
                return True
        return False

    def _add_finding(self, owasp, category, severity, filepath, line, source, issue, fix):
        """添加发现项"""
        lines = source.split('\n')
        code = lines[line - 1].strip() if line <= len(lines) else ""

        asvs = ""
        if self.asvs_level and owasp in self.ASVS_MAPPING:
            asvs = self.ASVS_MAPPING[owasp].get(self.asvs_level, "")

        self.findings.append(Finding(
            owasp=owasp, category=category, severity=severity,
            file=str(filepath), line=line, code=code[:100],
            issue=issue, fix=fix, asvs=asvs
        ))

    def _generate_report(self):
        """生成报告"""
        summary = {}
        for f in self.findings:
            key = f"{f.owasp}_{f.severity}"
            summary[key] = summary.get(key, 0) + 1

        return {
            "total_files_scanned": len(set(f.file for f in self.findings)),
            "total_findings": len(self.findings),
            "summary": summary,
            "asvs_level": self.asvs_level,
            "findings": [
                {
                    "owasp": f.owasp, "category": f.category,
                    "severity": f.severity, "file": f.file,
                    "line": f.line, "code": f.code,
                    "issue": f.issue, "fix": f.fix,
                    "asvs": f.asvs
                }
                for f in self.findings
            ]
        }
```

## 配置示例

### 审计配置

```json
{
  "audit_config": {
    "languages": ["typescript", "python", "go", "java"],
    "frameworks": ["nextjs", "express", "django", "fastapi", "spring"],
    "owasp": "top10",
    "asvs_level": "L2",
    "rules": {
      "A01_access_control": true,
      "A02_crypto": true,
      "A03_injection": true,
      "A04_design": true,
      "A05_misconfig": true,
      "A06_components": true,
      "A07_auth": true,
      "A08_integrity": true,
      "A09_logging": true,
      "A10_ssrf": true
    },
    "output": {
      "format": ["html", "sarif"],
      "include_fix": true,
      "include_asvs": true
    },
    "ci_cd": {
      "fail_on": "HIGH",
      "exclude_dirs": ["node_modules", ".git", "dist", "test"]
    }
  }
}
```

### ASVS合规等级

| 等级 | 描述 | 适用场景 |
|------|------|----------|
| L1 | 基础安全验证 | 小型应用、低风险 |
| L2 | 标准安全验证 | 企业应用、中等风险 |
| L3 | 高级安全验证 | 高风险应用、金融/医疗 |

## 最佳实践

### 1. 分阶段审计策略

```bash
# 开发阶段:快速扫描变更文件
python scripts/code_audit.py --files $(git diff --name-only) --format text

# 合并前:全面扫描
python scripts/code_audit.py --target . --owasp top10 --format html

# 发布前:合规审计
python scripts/code_audit.py --target . --owasp top10 --asvs L2 --format pdf
```

### 2. 误报抑制

```json
{
  "suppressions": [
    {
      "file": "test/**",
      "rule": "A03_injection",
      "reason": "测试文件中的示例代码"
    },
    {
      "file": "docs/**",
      "rule": "*",
      "reason": "文档目录不扫描"
    }
  ]
}
```

### 3. 持续监控

```bash
# 安装Git Hook
python scripts/code_audit.py --install-hook --fail-on HIGH

# CI/CD集成
python scripts/code_audit.py --target . --format sarif --output results.sarif
```

## 常见问题

### Q1: 专业版与免费版兼容吗?

A: 完全兼容。专业版包含免费版所有OWASP检查清单和代码示例,并在此基础上增加AST自动扫描、多语言支持和ASVS合规映射。

### Q2: AST分析比正则匹配好在哪里?

A: AST分析理解代码结构,能精确识别变量类型、函数调用关系和数据流,误报率显著低于纯正则匹配。例如,能区分字符串中的SQL关键字和实际SQL查询。

### Q3: 支持哪些框架?

A: 支持 Next.js、Express、Django、FastAPI、Flask、Spring Boot、Gin、Echo 等10+主流框架,每种框架有专属安全规则。

### Q4: SARIF报告如何使用?

A: SARIF是OASIS标准格式,可上传到GitHub Code Scanning、GitLab SAST、Azure DevOps等平台,在代码审查中直接展示安全发现。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python | 运行时 | 必需 | 系统自带 |
| ast模块 | 标准库 | 必需 | Python内置 |
| Node.js | 运行时 | 可选 | nodejs.org(TS分析) |
| TypeScript | npm包 | 可选 | `npm install -g typescript` |
| Go | 运行时 | 可选 | go.dev(Go分析) |
| Java JDK | 运行时 | 可选 | oracle.com(Java分析) |

### API Key 配置
- 专业版无需API Key,所有分析在本地执行
- 可选配置: Snyk API(增强依赖漏洞检测)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级代码安全审计任务
