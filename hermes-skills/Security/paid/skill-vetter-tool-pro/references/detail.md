# 详细参考 - skill-vetter-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

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
        "network_unknown": (r"(curl|wget|fetch)\s+['\"]https?://(?!api\.|cdn\.)", "HIGH"),
        "data_exfil": (r"(POST|upload|send).*(password|secret|token|key)", "CRITICAL"),
        "ip_connection": (r"https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", "HIGH"),
        "webhook_exfil": (r"(discord\.com/api/webhooks|hooks\.slack\.com)", "CRITICAL"),
        "suspicious_paste": (r"(pastebin\.com|glot\.io|hastebin\.com)", "HIGH"),
        "net_exfil_unrestricted": (r"(fetch|axios|requests)\.(post|put).*body", "HIGH"),

        "credential_request": (r"(request|ask|input).*(password|token|api.?key)", "HIGH"),
        "read_ssh": (r"~?/\.ssh/|~?/\.aws/|~?/\.gnupg/", "CRITICAL"),
        "read_keychain": (r"(keychain|credential.?manager|browser.?profile)", "CRITICAL"),
        "hardcoded_secret": (r"(password|secret|token|key)\s*[:=]\s*['\"][^'\"]{16,}['\"]", "CRITICAL"),

        "eval_exec": (r"(eval\s*\(|exec\s*\(|Function\s*\().*input", "CRITICAL"),
        "command_injection": (r"exec\(`.*\$\{.*\}`\)", "CRITICAL"),
        "remote_loader": (r"(require|import)\(['\"]https?://", "CRITICAL"),
        "auto_update": (r"(curl|wget).*\|\s*(bash|sh|python|node)", "CRITICAL"),
        "base64_decode": (r"(atob|base64decode|b64decode)\(", "MEDIUM"),

        "prompt_injection": (r"(ignore.*(previous|all|above).*instruction|<\|im_start\|>)", "CRITICAL"),
        "system_prompt_leak": (r"(system.?prompt|instructions.*extract|reveal.*prompt)", "HIGH"),
        "model_manipulation": (r"(jailbreak|DAN|override.*safety|bypass.*filter)", "CRITICAL"),

        "system_modify": (r"(/etc/|/usr/|C:\\Windows\\|C:\\System32)", "CRITICAL"),
        "privilege_escalation": (r"(sudo|runas|setuid|chmod.*777)", "HIGH"),
        "cookie_access": (r"(browser.?cookies|session.?storage|local.?storage)", "HIGH"),

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

        scan_results = self._scan_code(path)

        ai_analysis = self._ai_risk_analysis(scan_results)

        sandbox_results = None
        if sandbox:
            sandbox_results = self._sandbox_test(path)

        risk_score = self._calculate_risk_score(scan_results, sandbox_results)

        trust_recommendation = self._recommend_trust(risk_score)

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

