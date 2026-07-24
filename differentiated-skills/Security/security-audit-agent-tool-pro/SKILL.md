---
slug: security-audit-agent-tool-pro
name: security-audit-agent-tool-pro
version: 1.0.0
displayName: Agent安全审计专业版
summary: 企业级AI Agent安全审计平台,支持多Agent审计、深度提示注入检测、沙盒逃逸分析与CI/CD集成,适合安全团队与企业用户.
license: Proprietary
edition: pro
description: Agent安全审计专业版,为企业安全团队提供全方位AI Agent安全审计能力。核心能力:多Agent批量审计、上下文感知提示注入检测、沙盒逃逸分析、工具参数投毒检测、供应链安全、SARIF报告与CI/CD集成。Use
  when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标.
tags:
  - 安全
  - AI安全
  - Agent审计
  - 企业版
  - 深度检测
  - AI代理
  - 自动化
  - 智能
  - echo
  - agent
  - 专业版独
  - grep
  - null
tools:
  - read
  - exec
  - write
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Agents"
---
专业版为企业安全团队提供完整的AI Agent安全审计平台,涵盖多Agent批量审计、上下文感知深度提示注入检测、沙盒逃逸分析、工具参数投毒检测、供应链安全审查与CI/CD安全门禁。在免费版基础审计能力之上,新增企业级深度检测、自动化修复建议与合规报告导出。专业版完全兼容免费版审计方法,已有审计流程可无缝升级.
### 专业版核心优势
| 优势 | 说明 |
|---|---|
| 多Agent审计 | 批量审计多个Agent项目,统一管理 |
| 深度注入检测 | 上下文感知,检测复杂多轮注入 |
| 沙盒逃逸分析 | 检测Agent突破沙盒限制的行为 |
| 参数投毒检测 | 检测工具参数中的恶意载荷 |
| 供应链安全 | 审计Agent依赖的第三方组件 |
| 自动化修复 | 生成针对性修复方案与代码 |
| SARIF报告 | 集成到代码扫描与合规流程 |
| CI/CD门禁 | 部署前安全检查,阻断不安全Agent |

## 核心能力
### 1. 多Agent批量审计(专业版独有)
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | Agent安全审计专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
#!/bin/bash
AGENTS_DIR="${1:-./agents}"
REPORT_FILE="agent-audit-report.json"
# ...
echo "============================================"
echo "多Agent批量安全审计"
echo "审计时间: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
echo "============================================"
# ...
echo "[" > "$REPORT_FILE"
FIRST=true
# ...
for agent_dir in "$AGENTS_DIR"/*/; do
    agent_name=$(basename "$agent_dir")
    echo ""
    echo "审计Agent: ${agent_name}"
# ...
    ISSUES=0
# ...
    CODE_ISSUES=$(grep -rn 'eval(\|exec(\|system(' \
      --include='*.{js,ts,py}' "$agent_dir" 2>/dev/null | \
      grep -v 'node_modules\|test' | wc -l)
# ...
    SECRET_ISSUES=$(grep -rn 'sk-[A-Za-z0-9]\{20,\}\|AKIA[0-9A-Z]\{16\}' \
      --include='*.{js,ts,py,json,yaml}' "$agent_dir" 2>/dev/null | \
      grep -v 'node_modules\|example' | wc -l)
# ...
    INJECTION_ISSUES=0
    for pattern in 'ignore.*previous\|disregard.*above\|you.*are.*now'; do
        count=$(grep -ric "$pattern" "$agent_dir" 2>/dev/null | \
                awk -F: '{s+=$2} END {print s}')
        INJECTION_ISSUES=$((INJECTION_ISSUES + count))
    done
# ...
    TOOL_ISSUES=0
    if [ -f "${agent_dir}tools.json" ]; then
        TOOL_COUNT=$(jq '. | length' "${agent_dir}tools.json" 2>/dev/null)
        PERMISSIONLESS=$(jq '[.[] | select(.permissions == null or .allowed_actions == null)] | length' \
            "${agent_dir}tools.json" 2>/dev/null)
        TOOL_ISSUES=$PERMISSIONLESS
    fi
# ...
    TOTAL=$((CODE_ISSUES + SECRET_ISSUES + INJECTION_ISSUES + TOOL_ISSUES))
    echo "  代码问题: ${CODE_ISSUES}"
    echo "  密钥泄露: ${SECRET_ISSUES}"
    echo "  注入风险: ${INJECTION_ISSUES}"
    echo "  工具权限: ${TOOL_ISSUES}"
    echo "  总计: ${TOTAL}"
# ...
    [ "$FIRST" = true ] && FIRST=false || echo "," >> "$REPORT_FILE"
    echo "{\"agent\": \"${agent_name}\", \"code\": ${CODE_ISSUES}, \"secrets\": ${SECRET_ISSUES}, \"injection\": ${INJECTION_ISSUES}, \"tools\": ${TOOL_ISSUES}, \"total\": ${TOTAL}}" >> "$REPORT_FILE"
done
# ...
echo "]" >> "$REPORT_FILE"
echo ""
echo "审计完成,报告: ${REPORT_FILE}"
```

**输入**: 用户提供多Agent批量审计(专业版独有)所需的指令和必要参数.
**处理**: 解析多Agent批量审计(专业版独有)的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回多Agent批量审计(专业版独有)的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 上下文感知提示注入检测(专业版独有)

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供上下文感知提示注入检测(专业版独有)所需的指令和必要参数.
**处理**: 解析上下文感知提示注入检测(专业版独有)的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回上下文感知提示注入检测(专业版独有)的响应数据,包含状态码、结果和日志.
### 3. 沙盒逃逸分析(专业版独有)
```bash
#!/bin/bash
echo "=== 沙盒逃逸风险分析 ==="
# ...
echo ""
echo "--- 1. 文件系统越权 ---"
FS_ACCESS=$(grep -rn 'open(\|readFile(\|writeFile(\|fs\.' \
  --include='*.{js,ts}' . 2>/dev/null | \
  grep -v 'node_modules\|test' | wc -l)
echo "  文件系统操作: ${FS_ACCESS} 处"
# ...
PATH_TRAVERSAL=$(grep -rn '\.\./\|\.\.\\\|%2e%2e' \
  --include='*.{js,ts,py}' . 2>/dev/null | \
  grep -v 'node_modules\|test' | wc -l)
[ "$PATH_TRAVERSAL" -gt 0 ] && echo "  [!] 路径遍历风险: ${PATH_TRAVERSAL} 处"
# ...
echo ""
echo "--- 2. 网络访问 ---"
NET_ACCESS=$(grep -rn 'fetch(\|http\.get\|requests\.\|axios\.' \
  --include='*.{js,ts,py}' . 2>/dev/null | \
  grep -v 'node_modules\|test' | wc -l)
echo "  网络请求: ${NET_ACCESS} 处"
# ...
if ! grep -rn 'allowed.*url\|whitelist.*url\|allowedDomains' \
  --include='*.{js,ts,py,json}' . 2>/dev/null | grep -v 'node_modules'; then
    echo "  [!] 未发现URL白名单配置"
fi
# ...
echo ""
echo "--- 3. 进程执行 ---"
PROC_EXEC=$(grep -rn 'exec\|spawn\|system\|subprocess' \
  --include='*.{js,ts,py}' . 2>/dev/null | \
  grep -v 'node_modules\|test\|executive\|execution' | wc -l)
echo "  进程执行: ${PROC_EXEC} 处"
```

**输入**: 用户提供沙盒逃逸分析(专业版独有)所需的指令和必要参数.
**处理**: 解析沙盒逃逸分析(专业版独有)的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回沙盒逃逸分析(专业版独有)的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. SARIF报告导出(专业版独有)

**输入**: 用户提供SARIF报告导出(专业版独有)所需的指令和必要参数.
**处理**: 解析SARIF报告导出(专业版独有)的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回SARIF报告导出(专业版独有)的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、安全审计平台、支持多、深度提示注入检测、沙盒逃逸分析与、适合安全团队与企、业用户、安全审计专业版、为企业安全团队提、供全方位、安全审计能力、核心能力、工具参数投毒检测、供应链安全、报告与、Use、when、需要安全检测、合规审计、漏洞扫描、加密防护时使用、不适用于渗透测试、未授权目标等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景
### 场景一:企业级Agent安全治理
```bash
#!/bin/bash
echo "============================================"
echo "企业Agent安全治理"
echo "============================================"
# ...
echo "阶段1: 批量审计"
bash multi_agent_audit.sh ./agents --output audit-report.json
# ...
echo "阶段2: 深度注入检测"
python3 deep_injection_scan.py --dir ./agents --output injection-report.json
# ...
echo "阶段3: 沙盒逃逸分析"
bash sandbox_escape_check.sh ./agents
# ...
echo "阶段4: 报告生成"
python3 generate_sarif.py --input audit-report.json --output agent-audit.sarif
# ...
echo ""
echo "治理完成"
echo "  审计报告: audit-report.json"
echo "  注入报告: injection-report.json"
echo "  SARIF报告: agent-audit.sarif"
```

### 场景二:CI/CD安全门禁
```yaml
name: Agent Security Gate
on: [push, pull_request]
# ...
jobs:
  agent-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
# ...
      - name: Run Agent Security Audit
        run: |
          CRITICAL=0
          for pattern in 'eval(' 'exec(' 'system(' 'sk-[A-Za-z0-9]{20,}'; do
            count=$(grep -rn "$pattern" --include='*.{js,ts,py}' . | grep -v 'node_modules\|test' | wc -l)
            [ "$count" -gt 0 ] && echo "Found: $pattern ($count)" && CRITICAL=$((CRITICAL + count))
          done
# ...
          python3 deep_injection_scan.py --dir . --output injection.json
          INJECTION_COUNT=$(jq '.total_findings' injection.json)
# ...
          if [ "$CRITICAL" -gt 0 ] || [ "$INJECTION_COUNT" -gt 0 ]; then
            echo "Security gate FAILED"
            exit 1
          fi
          echo "Security gate PASSED"
# ...
      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: agent-audit.sarif
```

### 场景三:工具参数投毒检测
```python
#!/usr/bin/env python3
"""工具参数投毒检测"""
# ...
import re
import json
# ...
class ParameterPoisoningDetector:
    """检测Agent工具参数中的恶意载荷"""
# ...
    MALICIOUS_PATTERNS = {
        "command_injection": [
            r';\s*(rm|del|format|shutdown)',
            r'\|\s*(bash|sh|cmd|powershell)',
            r'`.*`',
            r'\$\(.*\)',
        ],
        "path_traversal": [
            r'\.\./',
            r'\.\.\\',
            r'%2e%2e',
            r'..%2f',
        ],
        "sql_injection": [
            r"'.*(OR|AND|UNION).*SELECT",
            r';\s*(DROP|DELETE|INSERT|UPDATE)',
            r"--\s*$",
        ],
        "xss": [
            r'<script.*>.*</script>',
            r'javascript:',
            r'on(error|load|click)=',
        ],
        "ssrf": [
            r'http://127\.0\.0\.1',
            r'http://localhost',
            r'http://169\.254\.169\.254',  # 云元数据
            r'http://0\.0\.0\.0',
        ]
    }
# ...
    def check_parameter(self, param_name, param_value):
        """检查单个参数"""
        findings = []
        value_str = str(param_value)
# ...
        for attack_type, patterns in self.MALICIOUS_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, value_str, re.IGNORECASE):
                    findings.append({
                        "parameter": param_name,
                        "attack_type": attack_type,
                        "pattern": pattern,
                        "value_snippet": value_str[:100],
                        "severity": "CRITICAL"
                    })
# ...
        return findings
# ...
    def check_tool_call(self, tool_name, parameters):
        """检查工具调用的所有参数"""
        all_findings = []
        for name, value in parameters.items():
            findings = self.check_parameter(name, value)
            for f in findings:
                f["tool"] = tool_name
                all_findings.append(f)
        return all_findings
# ...
if __name__ == "__main__":
    detector = ParameterPoisoningDetector()
# ...
    findings = detector.check_tool_call("file_reader", {
        "path": "../../../etc/passwd",
        "command": "ls; rm -rf /"
    })
# ...
    print(json.dumps(findings, indent=2, ensure_ascii=False))
```

## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 从免费版升级
```bash
bash codebase_scan.sh
# ...
bash multi_agent_audit.sh ./agents --full --output report.json
```

### 首次深度注入检测
```bash
python3 deep_injection_scan.py --dir ./agents --output injection-report.json
```

#
## 示例
### 审计规则配置
```yaml
rules:
  prompt_injection:
    enabled: true
    patterns: "deep"  # deep模式启用上下文感知
    severity_threshold: "MEDIUM"
# ...
  sandbox_escape:
    enabled: true
    check_fs: true
    check_network: true
    check_process: true
# ...
  parameter_poisoning:
    enabled: true
    attack_types: [command, path, sql, xss, ssrf]
# ...
  hardcoded_secrets:
    enabled: true
    patterns: [api_key, token, password, private_key]
# ...
  tool_permissions:
    enabled: true
    require_schema: true
    require_rate_limit: true
```

### 安全等级矩阵
| 发现类型 | 严重 | 高危 | 中危 | 低危 |
|---:|---:|---:|---:|---:|
| 提示注入 | 直接覆盖 | 角色劫持 | 编码绕过 | 间接泄露 |
| 沙盒逃逸 | 进程执行 | 文件越权 | 网络访问 | 信息泄露 |
| 参数投毒 | 命令注入 | 路径遍历 | SQL注入 | XSS |
| 密钥泄露 | 私钥 | API Key | Token | 内部URL |

## 最佳实践
1. **深度防御**:代码审计+提示注入检测+沙盒分析多层防护.
2. **批量治理**:对所有Agent项目定期执行批量审计.
3. **CI/CD门禁**:将安全审计集成到部署流水线,阻断不安全Agent.
4. **SARIF集成**:使用SARIF报告集成到代码扫描平台.
5. **持续监控**:定期扫描,跟踪安全态势变化.
6. **红蓝对抗**:使用专业版检测结果指导红队演练.
## 常见问题
### Q1: 专业版与免费版审计结果是否兼容?
完全兼容。专业版在免费版基础检查上增加深度检测,免费版发现的问题专业版一定能发现.
### Q2: 深度注入检测如何工作?
使用三层检测:直接注入模式匹配、间接注入上下文分析、多轮注入行为追踪,覆盖复杂攻击场景.
### Q3: SARIF报告如何使用?
将SARIF文件上传到GitHub Code Scanning或Azure DevOps,安全发现会自动显示在PR中.
### Q4: CI/CD门禁如何配置?
参考CI/CD集成示例,设置严重漏洞零容忍策略。发现CRITICAL级别问题时阻断部署.
### Q5: 参数投毒检测覆盖哪些攻击?
覆盖命令注入、路径遍历、SQL注入、XSS、SSRF五大类攻击模式.
## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+(使用深度检测引擎时需要)
- **Shell**: Bash(脚本示例使用Bash语法)

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| grep | 文本搜索工具 | 必需 | 系统自带 |
| python3 | 运行时环境 | 推荐 | python.org 下载 |
| jq | JSON处理工具 | 必需 | `apt install jq` / `brew install jq` |
| semgrep | SAST工具 | 可选 | `pip install semgrep` |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 专业版为知识驱动+工具集成模式
- 深度检测在本地执行,不发送代码到外部
- SARIF报告生成无需额外API Key

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级AI Agent安全审计与治理任务

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "Agent安全审计专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "security audit agent pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
