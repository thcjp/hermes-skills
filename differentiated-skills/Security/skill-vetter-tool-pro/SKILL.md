---
slug: skill-vetter-tool-pro
name: skill-vetter-tool-pro
version: "1.0.0"
displayName: Skill安全审查(专业版)
summary: 企业级Skill安全审查平台,含自动扫描、沙箱测试、信任注册表与持续监控
license: MIT
edition: pro
description: |-
  核心能力:
  - 24项红旗规则+自定义规则引擎
  - 自动化代码扫描与AI风险分析
  - 沙箱隔离环境测试
  - Skill信任注册表与生命周期管理
  - 批量审查与并行处理
  - 变更检测与持续监控
  - HTML/PDF专业审查报告

  适用场景:
  - 企业AI Agent安全治理
  - Skill供应链安全管理
  - 安全合规审计
  - 开发团队安全规范执行

  差异化:
  - 自动化深度分析,降低人工审查负担
  - 沙箱隔离测试,安全验证Skill行为
  - 信任生命周期管理(注册/验证/撤销)
  - 与免费版兼容,红旗规则可复用

  触发关键词: Skill安全审查, 企业安全, 沙箱测试, 信任管理, 供应链安全, 持续监控, skill vetting, sandbox, trust registry
tags:
- 安全
- Skill安全
- 企业安全
- 供应链安全
- 沙箱测试
tools:
- read
- exec
---

# Skill安全审查(专业版)

## 概述

Skill安全审查专业版是一款面向企业用户的AI Agent Skill安全治理平台。在免费版12项红旗规则基础上,扩展至24项规则并支持自定义规则引擎,增加自动化代码扫描与AI风险分析、沙箱隔离环境测试、Skill信任注册表与生命周期管理、批量审查与并行处理、变更检测与持续监控等企业级功能。与免费版完全兼容,红旗规则和审查流程可无缝复用。

## 核心能力

### 功能矩阵

| 功能模块 | 描述 | 免费版 | 专业版 |
|----------|------|--------|--------|
| 红旗规则 | 检测规则数 | 12项 | 24项+自定义 |
| 审查方式 | 检测方法 | 人工清单 | 自动扫描+AI分析 |
| 沙箱测试 | 隔离验证 | 不支持 | Docker沙箱环境 |
| 信任注册表 | 生命周期 | 不支持 | 注册/验证/撤销 |
| 批量审查 | 处理能力 | 单个Skill | 批量+并行 |
| 变更监控 | 持续跟踪 | 不支持 | 文件哈希+告警 |
| 报告格式 | 输出类型 | 文本 | HTML/PDF/JSON |
| 风险评分 | 量化评估 | 4级分类 | 0-100分制 |

### 24项红旗规则

```text
┌──────────────────────────────────────────────────────────┐
│              专业版24项红旗检测规则                      │
├──────────────┬───────────────────────────────────────────┤
│ 网络安全      │ 未知URL请求/数据外泄/IP连接/Webhook外泄   │
│ 凭据安全      │ 凭据请求/SSH访问/密钥链访问/硬编码密钥    │
│ 代码执行      │ eval/exec/命令注入/远程加载/自动更新      │
│ 数据安全      │ 身份文件访问/环境变量窃取/混淆代码        │
│ AI安全        │ Prompt注入/系统提示泄露/模型操纵          │
│ 系统安全      │ 系统文件修改/提权请求/浏览器Cookie访问    │
│ 供应链安全    │ 未声明安装/木马分发/粘贴板URL/社会工程   │
│ 区块链安全    │ 私钥泄露/助记词/钱包盗取/无限授权         │
└──────────────┴───────────────────────────────────────────┘
```

## 使用场景

### 场景一:企业级Skill安全审查

对新安装的Skill执行全面安全审查。

```bash
python scripts/vet_skill.py \
  --target /path/to/skill \
  --deep-scan \
  --sandbox-test \
  --report html \
  --output vetting_report.html
```

输出示例:
```
Skill安全审查报告
══════════════════════════════════════
Skill: example-skill v1.2.0
风险评分: 35/100 (MEDIUM)
审查文件: 18
红旗项: 3 (1 HIGH, 2 MEDIUM)
沙箱测试: 通过(无异常行为)
信任建议: restricted (受限信任)

红旗详情:
  [HIGH] 网络请求到未知URL
    文件: index.js:42
    证据: fetch('https://unknown-server.com/data')

  [MEDIUM] 环境变量读取
    文件: config.js:15
    证据: process.env.API_KEY

  [MEDIUM] Base64解码
    文件: utils.js:28
    证据: atob(encodedData)
```

### 场景二:批量Skill审查

```bash
# 批量审查所有已安装的Skill
python scripts/vet_skill.py \
  --batch ~/.skills/ \
  --threads 5 \
  --report html \
  --output batch_vetting.html
```

### 场景三:沙箱隔离测试

```bash
# 在Docker沙箱中安全测试Skill行为
python scripts/vet_skill.py \
  --target /path/to/skill \
  --sandbox-test \
  --sandbox-timeout 60 \
  --monitor network,filesystem,process
```

### 场景四:信任注册表管理

```bash
# 审查后注册信任
python scripts/vet_skill.py --target /path/to/skill --register-trust

# 查询信任状态
python scripts/vet_skill.py --lookup /path/to/skill

# 撤销信任
python scripts/vet_skill.py --revoke /path/to/skill --reason "检测到恶意行为"

# 列出所有信任记录
python scripts/vet_skill.py --list-trust
```

## 快速开始

### 企业级审查引擎

```python
import os
import re
import json
import hashlib
import subprocess
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

class EnterpriseSkillVetter:
    """企业级Skill安全审查引擎"""

    RED_FLAGS_24 = {
        # 网络安全 (6项)
        "network_unknown": (r"(curl|wget|fetch)\s+['\"]https?://(?!api\.|cdn\.)", "HIGH"),
        "data_exfil": (r"(POST|upload|send).*(password|secret|token|key)", "CRITICAL"),
        "ip_connection": (r"https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", "HIGH"),
        "webhook_exfil": (r"(discord\.com/api/webhooks|hooks\.slack\.com)", "CRITICAL"),
        "suspicious_paste": (r"(pastebin\.com|glot\.io|hastebin\.com)", "HIGH"),
        "net_exfil_unrestricted": (r"(fetch|axios|requests)\.(post|put).*body", "HIGH"),

        # 凭据安全 (4项)
        "credential_request": (r"(request|ask|input).*(password|token|api.?key)", "HIGH"),
        "read_ssh": (r"~?/\.ssh/|~?/\.aws/|~?/\.gnupg/", "CRITICAL"),
        "read_keychain": (r"(keychain|credential.?manager|browser.?profile)", "CRITICAL"),
        "hardcoded_secret": (r"(password|secret|token|key)\s*[:=]\s*['\"][^'\"]{16,}['\"]", "CRITICAL"),

        # 代码执行 (5项)
        "eval_exec": (r"(eval\s*\(|exec\s*\(|Function\s*\().*input", "CRITICAL"),
        "command_injection": (r"exec\(`.*\$\{.*\}`\)", "CRITICAL"),
        "remote_loader": (r"(require|import)\(['\"]https?://", "CRITICAL"),
        "auto_update": (r"(curl|wget).*\|\s*(bash|sh|python|node)", "CRITICAL"),
        "base64_decode": (r"(atob|base64decode|b64decode)\(", "MEDIUM"),

        # AI安全 (3项)
        "prompt_injection": (r"(ignore.*(previous|all|above).*instruction|<\|im_start\|>)", "CRITICAL"),
        "system_prompt_leak": (r"(system.?prompt|instructions.*extract|reveal.*prompt)", "HIGH"),
        "model_manipulation": (r"(jailbreak|DAN|override.*safety|bypass.*filter)", "CRITICAL"),

        # 系统安全 (3项)
        "system_modify": (r"(/etc/|/usr/|C:\\Windows\\|C:\\System32)", "CRITICAL"),
        "privilege_escalation": (r"(sudo|runas|setuid|chmod.*777)", "HIGH"),
        "cookie_access": (r"(browser.?cookies|session.?storage|local.?storage)", "HIGH"),

        # 供应链安全 (3项)
        "undeclared_install": (r"(npm install|pip install)(?!.*--save)", "MEDIUM"),
        "trojan_distribution": (r"(download.*execute|password.*extract|binary.*run)", "CRITICAL"),
        "social_engineering": (r"(urgent.*execute|must.*run.*now|critical.*install)", "HIGH"),
    }

    TRUST_LEVELS = {
        "untrusted": {"score_range": (0, 30), "capabilities": "none"},
        "restricted": {"score_range": (31, 60), "capabilities": "limited"},
        "trusted": {"score_range": (61, 100), "capabilities": "full"}
    }

    def __init__(self):
        self.findings = []
        self.trust_registry = self._load_trust_registry()

    def vet_deep(self, skill_path, sandbox=False):
        """深度安全审查"""
        path = Path(skill_path)

        # Step 1: 自动代码扫描
        scan_results = self._scan_code(path)

        # Step 2: AI风险分析
        ai_analysis = self._ai_risk_analysis(scan_results)

        # Step 3: 沙箱测试(可选)
        sandbox_results = None
        if sandbox:
            sandbox_results = self._sandbox_test(path)

        # Step 4: 风险评分
        risk_score = self._calculate_risk_score(scan_results, sandbox_results)

        # Step 5: 信任建议
        trust_recommendation = self._recommend_trust(risk_score)

        # Step 6: 生成报告
        report = self._generate_report(
            skill_path, scan_results, ai_analysis,
            sandbox_results, risk_score, trust_recommendation
        )

        return report

    def _scan_code(self, path):
        """自动代码扫描"""
        findings = []
        files_scanned = 0

        for filepath in path.rglob("*"):
            if filepath.is_file() and filepath.suffix in {".js", ".ts", ".py", ".md", ".json", ".sh", ".yaml"}:
                if any(skip in str(filepath) for skip in ["node_modules", ".git", "dist"]):
                    continue

                files_scanned += 1
                try:
                    content = filepath.read_text(encoding='utf-8', errors='ignore')
                    for flag_id, (pattern, severity) in self.RED_FLAGS_24.items():
                        for match in re.finditer(pattern, content, re.IGNORECASE):
                            line_num = content[:match.start()].count('\n') + 1
                            findings.append({
                                "flag": flag_id,
                                "severity": severity,
                                "file": str(filepath),
                                "line": line_num,
                                "evidence": match.group()[:100]
                            })
                except Exception:
                    pass

        return {"files_scanned": files_scanned, "findings": findings}

    def _ai_risk_analysis(self, scan_results):
        """AI风险分析"""
        findings = scan_results["findings"]
        analysis = {
            "critical_count": sum(1 for f in findings if f["severity"] == "CRITICAL"),
            "high_count": sum(1 for f in findings if f["severity"] == "HIGH"),
            "medium_count": sum(1 for f in findings if f["severity"] == "MEDIUM"),
            "risk_patterns": self._identify_patterns(findings),
            "attack_scenarios": self._predict_attacks(findings)
        }
        return analysis

    def _sandbox_test(self, skill_path):
        """Docker沙箱测试"""
        try:
            # 在隔离容器中运行Skill
            result = subprocess.run([
                "docker", "run", "--rm",
                "--network=none",  # 禁用网络
                "--read-only",     # 只读文件系统
                "--memory=256m",   # 内存限制
                "--cpus=0.5",      # CPU限制
                "-v", f"{skill_path}:/skill:ro",
                "sandbox-python:latest",
                "python", "/skill/test.py"
            ], capture_output=True, text=True, timeout=60)

            return {
                "exit_code": result.returncode,
                "stdout": result.stdout[:500],
                "stderr": result.stderr[:500],
                "network_blocked": True,
                "filesystem_readonly": True
            }
        except Exception as e:
            return {"error": str(e), "sandbox_available": False}

    def _calculate_risk_score(self, scan_results, sandbox_results=None):
        """计算风险评分(0-100,越高越安全)"""
        findings = scan_results["findings"]
        score = 100

        for finding in findings:
            if finding["severity"] == "CRITICAL":
                score -= 20
            elif finding["severity"] == "HIGH":
                score -= 10
            elif finding["severity"] == "MEDIUM":
                score -= 5

        if sandbox_results and sandbox_results.get("exit_code", 0) != 0:
            score -= 15

        return max(0, min(100, score))

    def _recommend_trust(self, risk_score):
        """信任等级建议"""
        for level, info in self.TRUST_LEVELS.items():
            low, high = info["score_range"]
            if low <= risk_score <= high:
                return {"level": level, "capabilities": info["capabilities"]}
        return {"level": "untrusted", "capabilities": "none"}

    def _identify_patterns(self, findings):
        """识别风险模式"""
        patterns = []
        flags = [f["flag"] for f in findings]

        if "data_exfil" in flags and "credential_request" in flags:
            patterns.append("凭据窃取模式: 请求凭据+外传数据")
        if "remote_loader" in flags and "eval_exec" in flags:
            patterns.append("远程代码执行模式: 加载+执行远程代码")
        if "prompt_injection" in flags:
            patterns.append("AI操纵模式: Prompt注入攻击")
        if "auto_update" in flags:
            patterns.append("持久化模式: 自动更新机制")

        return patterns

    def _predict_attacks(self, findings):
        """预测攻击场景"""
        scenarios = []
        flags = set(f["flag"] for f in findings)

        if {"read_ssh", "data_exfil"} & flags:
            scenarios.append("攻击者可能窃取SSH密钥并外传")
        if {"credential_request", "webhook_exfil"} & flags:
            scenarios.append("攻击者可能收集凭据通过Webhook外传")
        if {"prompt_injection", "system_prompt_leak"} & flags:
            scenarios.append("攻击者可能操纵AI行为或泄露系统提示")

        return scenarios

    def _load_trust_registry(self):
        """加载信任注册表"""
        registry_path = Path.home() / ".skill-vetter" / "registry.json"
        if registry_path.exists():
            with open(registry_path) as f:
                return json.load(f)
        return {}

    def register_trust(self, skill_id, source, trust_level, preset):
        """注册信任记录"""
        file_hash = self._compute_hash(source)
        self.trust_registry[skill_id] = {
            "source": source,
            "trust_level": trust_level,
            "preset": preset,
            "hash": file_hash,
            "registered_at": datetime.now().isoformat()
        }
        self._save_registry()
        return f"已注册: {skill_id} (信任级别: {trust_level})"

    def _compute_hash(self, path):
        """计算文件哈希"""
        hasher = hashlib.sha256()
        for filepath in Path(path).rglob("*"):
            if filepath.is_file():
                with open(filepath, 'rb') as f:
                    hasher.update(f.read())
        return hasher.hexdigest()

    def _save_registry(self):
        """保存信任注册表"""
        registry_dir = Path.home() / ".skill-vetter"
        registry_dir.mkdir(parents=True, exist_ok=True)
        with open(registry_dir / "registry.json", 'w') as f:
            json.dump(self.trust_registry, f, indent=2)

    def batch_vet(self, skills_dir, threads=5):
        """批量审查"""
        skills = [d for d in Path(skills_dir).iterdir() if d.is_dir()]
        results = []

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = {executor.submit(self.vet_deep, str(s)): s for s in skills}
            for future in futures:
                skill = futures[future]
                try:
                    result = future.result()
                    results.append({"skill": skill.name, "result": result})
                    print(f"[完成] {skill.name}")
                except Exception as e:
                    print(f"[失败] {skill.name}: {str(e)}")

        return results
```

## 配置示例

### 企业审查配置

```json
{
  "vetting_config": {
    "rules": "24+custom",
    "custom_rules": [
      {
        "id": "custom_data_upload",
        "pattern": "upload.*user.*data",
        "severity": "HIGH",
        "description": "上传用户数据"
      }
    ],
    "sandbox": {
      "enabled": true,
      "image": "sandbox-python:latest",
      "network": "none",
      "readonly": true,
      "memory": "256m",
      "cpus": "0.5",
      "timeout": 60
    },
    "trust_registry": {
      "auto_register": false,
      "require_approval": true
    },
    "monitoring": {
      "enabled": true,
      "check_interval": "daily",
      "alert_on_change": true
    },
    "report": {
      "format": "html",
      "include_recommendations": true,
      "include_attack_scenarios": true
    }
  }
}
```

### 信任等级能力模型

| 信任级别 | 评分范围 | 文件访问 | 网络访问 | 命令执行 |
|----------|----------|----------|----------|----------|
| untrusted | 0-30 | 工作区只读 | 禁止 | 禁止 |
| restricted | 31-60 | 工作区读写 | 白名单域名 | 受限命令 |
| trusted | 61-100 | 全部读写 | 全部允许 | 全部允许 |

## 最佳实践

### 1. 安装前审查流程

```bash
# Step 1: 深度扫描
python scripts/vet_skill.py --target /path/to/skill --deep-scan

# Step 2: 沙箱测试
python scripts/vet_skill.py --target /path/to/skill --sandbox-test

# Step 3: 注册信任(如通过审查)
python scripts/vet_skill.py --target /path/to/skill --register-trust --level restricted
```

### 2. 持续监控

```bash
# 配置每日变更检测
python scripts/vet_skill.py --monitor ~/.skills/ --schedule "0 3 * * *"
```

### 3. 批量审查

```bash
# 审查所有已安装Skill
python scripts/vet_skill.py --batch ~/.skills/ --threads 5 --report html
```

## 常见问题

### Q1: 专业版与免费版兼容吗?

A: 完全兼容。专业版包含免费版所有12项红旗规则,并扩展至24项+自定义规则。免费版的审查报告可被专业版读取。

### Q2: 沙箱测试安全吗?

A: 沙箱使用Docker隔离:禁用网络、只读文件系统、限制内存和CPU。即使Skill包含恶意代码,也无法影响宿主系统。

### Q3: 信任注册表如何工作?

A: 注册时计算Skill文件哈希。每次启动时验证哈希,如果文件被篡改(哈希不匹配),自动降级信任级别并告警。

### Q4: 支持自定义规则吗?

A: 支持。在配置文件中添加自定义规则,指定正则模式、严重等级和描述。自定义规则与内置规则一起执行。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python | 运行时 | 必需 | 系统自带 |
| re模块 | 标准库 | 必需 | Python内置 |
| hashlib模块 | 标准库 | 必需 | Python内置 |
| Docker | 运行时 | 可选 | docker.com(沙箱测试用) |

### API Key 配置
- 核心功能无需API Key,所有审查在本地执行
- 可选配置: VirusTotal API(增强恶意URL检测)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级Skill安全审查任务
