---
slug: cybersecurity-engine-tool-pro
name: cybersecurity-engine-tool-pro
version: 1.0.0
displayName: 网络安全评估引擎专业版
summary: 企业级安全评估与威胁建模平台,支持完整十二阶段评估、合规框架映射、多维安全评分与自动化漏洞管理,适合安全团队与企业用户.
license: Proprietary
edition: pro
description: '网络安全评估引擎专业版,为企业安全团队提供全方位安全评估与治理能力.
  核心能力:十二阶段深度评估、STRIDE+攻击树建模、合规框架映射、100分制多维评分、自动化漏洞SLA管理、安全程序设计.
  适用场景:企业安全架构评审、合规审计准备、安全程序建设、红蓝对抗准备.
  差异化:专业版兼容免费版评估方法,新增企业级合规映射、自动化治理与团队协作能力,满足规模化安全管理需求.
  适用关键词: 安全评估, 合规审计, 安全程序, 安全评分, enterprise, compliance, SOC2, ISO27001'
tags:
  - 安全
  - 威胁建模
  - 合规审计
  - 企业版
  - 安全治理
  - 加密
  - 工具
tools:
  - read
  - exec
homepage: ""
# 定价元数据
category: "Security"
---
# 网络安全评估引擎专业版
## 概述
专业版为企业安全团队提供完整的网络安全评估与治理平台,涵盖从安全态势评估到安全程序设计的全生命周期管理。在免费版基础评估能力之上,新增十二阶段深度评估、STRIDE+攻击树威胁建模、SOC 2/ISO 27001/GDPR/HIPAA合规框架映射、100分制多维安全评分、自动化漏洞SLA跟踪与企业级报告导出。专业版完全兼容免费版评估方法,已有评估流程可无缝升级.
### 专业版核心优势
| 优势 | 说明 |
|---|---|
| 十二阶段评估 | 从态势评估到供应链安全的完整覆盖 |
| 合规框架映射 | SOC 2/ISO 27001/GDPR/HIPAA/PCI DSS |
| 多维评分 | 100分制8维度加权评分体系 |
| 自动化SLA | 漏洞修复SLA自动跟踪与升级 |
| 安全程序设计 | 四季度分阶段安全程序建设方案 |
| 红蓝对抗 | 渗透测试方法论与红队演练准备 |
| 报告导出 | HTML/PDF/SARIF合规报告 |
| 团队协作 | 多租户协作与角色权限管理 |

## 核心能力
### 1. 十二阶段深度评估(专业版独有)
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 网络安全评估引擎专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```text
Phase 1:  安全态势评估      -> 三层健康检查 + 完整评估简报
Phase 2:  威胁建模(STRIDE+)  -> 系统分解 + STRIDE分析 + 威胁登记
Phase 3:  应用安全(OWASP+)   -> A01-A10深度检查 + 修复模式
Phase 4:  基础设施安全       -> 网络/容器/云安全基线
Phase 5:  漏洞管理程序       -> 生命周期 + SLA + 扫描计划
Phase 6:  事件响应           -> 严重级别 + 响应手册 + 事后复盘
Phase 7:  安全头与浏览器安全 -> HTTP头 + Cookie安全
Phase 8:  认证授权深度       -> 密码策略 + JWT + OAuth/OIDC
Phase 9:  安全程序设计       -> 四季度建设方案 + 指标看板
Phase 10: 渗透测试方法论     -> 侦察 + 测试阶段 + 报告模板
Phase 11: 供应链安全         -> 依赖安全 + 构建管道 + CI/CD
Phase 12: 安全评分体系       -> 8维度100分制评分
```

**输入**: 用户提供十二阶段深度评估(专业版独有)所需的指令和必要参数.
**处理**: 解析十二阶段深度评估(专业版独有)的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回十二阶段深度评估(专业版独有)的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 合规框架映射(专业版独有)
```yaml
# 示例
compliance_mapping:
  SOC_2:
    CC1:  "控制环境 -> 安全治理程序(Phase 9)"
    CC2:  "沟通与信息 -> 安全日志与告警(Phase 6)"
    CC6:  "逻辑与物理访问 -> 认证授权(Phase 8)"
    CC7:  "系统运行 -> 漏洞管理(Phase 5)"
    CC8:  "变更管理 -> CI/CD安全(Phase 11)"
# ...
  ISO_27001:
    A5:   "信息安全策略 -> 安全程序设计(Phase 9)"
    A6:   "组织安全 -> 角色与职责"
    A8:   "资产管理 -> 资产清单与分类"
    A9:   "人力资源安全 -> 安全意识培训"
    A12:  "运营安全 -> 漏洞管理(Phase 5)"
    A14:  "系统获取与维护 -> 供应链安全(Phase 11)"
# ...
  GDPR:
    Art5:  "数据原则 -> 数据分类(Phase 1)"
    Art25: "设计与默认隐私 -> 安全设计(Phase 3)"
    Art32: "安全处理 -> 加密与访问控制(Phase 4, 8)"
    Art33: "违规通知 -> 事件响应(Phase 6)"
# ...
  HIPAA:
    Admin:  "管理保障 -> 安全程序(Phase 9)"
    Phys:   "物理保障 -> 基础设施安全(Phase 4)"
    Tech:   "技术保障 -> 加密与认证(Phase 8)"
```

**输入**: 用户提供合规框架映射(专业版独有)所需的指令和必要参数.
**处理**: 解析合规框架映射(专业版独有)的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回合规框架映射(专业版独有)的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 100分制多维安全评分(专业版独有)
```python
#!/usr/bin/env python3
"""专业版安全评分引擎"""
# ...
class SecurityScoringEngine:
    """8维度100分制安全评分"""
# ...
    DIMENSIONS = {
        "authentication_access": {"weight": 0.20, "name": "认证与访问控制"},
        "data_protection": {"weight": 0.15, "name": "数据保护"},
        "vulnerability_mgmt": {"weight": 0.15, "name": "漏洞管理"},
        "infrastructure": {"weight": 0.15, "name": "基础设施安全"},
        "logging_monitoring": {"weight": 0.10, "name": "日志与监控"},
        "incident_response": {"weight": 0.10, "name": "事件响应"},
        "code_security": {"weight": 0.10, "name": "代码安全"},
        "supply_chain": {"weight": 0.05, "name": "供应链安全"},
    }
# ...
    def __init__(self):
        self.scores = {}
        self.findings = {}
# ...
    def score_dimension(self, dimension, score, findings=None):
        """设置维度得分(0-10)与发现项"""
        if dimension not in self.DIMENSIONS:
            raise ValueError(f"未知维度: {dimension}")
        self.scores[dimension] = min(max(score, 0), 10)
        self.findings[dimension] = findings or []
# ...
    def calculate_composite(self):
        """计算综合得分(0-100)"""
        if not self.scores:
            return 0
        total = 0
        for dim, config in self.DIMENSIONS.items():
            if dim in self.scores:
                total += self.scores[dim] * config["weight"] * 10
        return round(total)
# ...
    def get_tier(self, score):
        """获取安全等级"""
        if score >= 90: return ("S", "卓越 - 安全是竞争优势")
        elif score >= 70: return ("A", "良好 - 基础扎实,持续改进")
        elif score >= 50: return ("B", "待改进 - 存在显著差距")
        else: return ("F", "危险 - 暂停功能开发,修复安全问题")
# ...
    def generate_report(self):
        """生成评分报告"""
        composite = self.calculate_composite()
        tier, label = self.get_tier(composite)
# ...
        report = {
            "composite_score": composite,
            "tier": tier,
            "label": label,
            "dimensions": {}
        }
# ...
        for dim, config in self.DIMENSIONS.items():
            score = self.scores.get(dim, 0)
            report["dimensions"][dim] = {
                "name": config["name"],
                "score": score * 10,
                "weight": f"{config['weight']*100:.0f}%",
                "findings": self.findings.get(dim, [])
            }
# ...
        return report
# ...
# 使用示例
if __name__ == "__main__":
    import json
    engine = SecurityScoringEngine()
# ...
    # 评分各维度(0-10分)
    engine.score_dimension("authentication_access", 8, ["MFA覆盖率95%"])
    engine.score_dimension("data_protection", 7, ["静态加密已启用"])
    engine.score_dimension("vulnerability_mgmt", 6, ["3个高危漏洞待修复"])
    engine.score_dimension("infrastructure", 8, ["防火墙配置良好"])
    engine.score_dimension("logging_monitoring", 5, ["缺少SIEM集成"])
    engine.score_dimension("incident_response", 4, ["响应计划未测试"])
    engine.score_dimension("code_security", 9, ["SAST已集成CI"])
    engine.score_dimension("supply_chain", 6, ["缺少SBOM生成"])
# ...
    report = engine.generate_report()
    print(json.dumps(report, indent=2, ensure_ascii=False))
```

**输入**: 用户提供100分制多维安全评分(专业版独有)所需的指令和必要参数.
**处理**: 解析100分制多维安全评分(专业版独有)的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回100分制多维安全评分(专业版独有)的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 自动化漏洞SLA管理(专业版独有)
```yaml
# 漏洞SLA配置
vulnerability_sla:
  critical:
    cvss_range: "9.0-10.0"
    remediation_sla: "24小时"
    escalation: "立即通知CTO/CISO"
    auto_ticket: true
    sla_breach_action: "阻断部署"
# ...
  high:
    cvss_range: "7.0-8.9"
    remediation_sla: "7天"
    escalation: "通知团队负责人"
    auto_ticket: true
    sla_breach_action: "标记逾期"
# ...
  medium:
    cvss_range: "4.0-6.9"
    remediation_sla: "30天"
    escalation: "加入迭代待办"
    auto_ticket: false
# ...
  low:
    cvss_range: "0.1-3.9"
    remediation_sla: "90天"
    escalation: "记录跟踪"
    auto_ticket: false
```

**输入**: 用户提供自动化漏洞SLA管理(专业版独有)所需的指令和必要参数.
**处理**: 解析自动化漏洞SLA管理(专业版独有)的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回自动化漏洞SLA管理(专业版独有)的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级安全评估与、威胁建模平台、支持完整十二阶段、合规框架映射、多维安全评分与自、动化漏洞管理、适合安全团队与企、业用户、网络安全评估引擎、专业版、为企业安全团队提、供全方位安全评估、与治理能力、核心能力、十二阶段深度评估、STRIDE、攻击树建模、分制多维评分、自动化漏洞、SLA、安全程序设计、适用场景、企业安全架构评审、合规审计准备、安全程序建设、红蓝对抗准备、差异化、专业版兼容免费版、评估方法、新增企业级合规映、自动化治理与团队、协作能力、满足规模化安全管、理需求、适用关键词、安全评估、合规审计、安全程序、安全评分、enterprise、compliance、SOC、ISO等.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景一:企业安全架构评审
对企业整体安全架构进行十二阶段深度评估,生成合规报告.
```bash
#!/bin/bash
# 企业安全架构评审脚本(专业版)
echo "============================================"
echo "企业安全架构评审"
echo "评审时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================"
# ...
# Phase 1: 安全态势评估
echo ""
echo "=== Phase 1: 安全态势评估 ==="
echo "执行三层健康检查..."
# 关键风险检查
CRITICAL=0
for pattern in 'AKIA[0-9A-Z]\{16\}' 'BEGIN.*PRIVATE KEY'; do
    count=$(grep -rn "$pattern" --include='*.{js,ts,py,go}' . 2>/dev/null | wc -l)
    [ "$count" -gt 0 ] && CRITICAL=$((CRITICAL + count))
done
echo "关键风险: ${CRITICAL} 项"
# ...
# Phase 4: 基础设施安全
echo ""
echo "=== Phase 4: 基础设施安全 ==="
echo "检查网络暴露..."
if command -v ss &> /dev/null; then
    DANGEROUS_PORTS=$(ss -tlnp 2>/dev/null | grep -E '6379|2375|3306|27017' | wc -l)
    echo "危险端口暴露: ${DANGEROUS_PORTS} 个"
fi
# ...
# Phase 8: 认证授权
echo ""
echo "=== Phase 8: 认证授权检查 ==="
JWT_ISSUES=$(grep -rn "alg.*none\|HS256.*shared" --include='*.{js,ts,py}' . 2>/dev/null | wc -l)
echo "JWT配置问题: ${JWT_ISSUES} 处"
# ...
echo ""
echo "============================================"
echo "评审完成,详细报告请查看专业版HTML输出"
echo "============================================"
```

### 场景二:合规审计准备
```python
#!/usr/bin/env python3
"""专业版合规审计准备工具"""
# ...
class CompliancePrep:
    """合规框架检查清单生成器"""
# ...
    FRAMEWORKS = {
        "SOC2": {
            "name": "SOC 2 Type II",
            "categories": {
                "CC1": "控制环境 - 安全治理程序是否建立",
                "CC2": "沟通与信息 - 安全事件是否被记录和沟通",
                "CC6": "逻辑访问 - 认证授权机制是否健全",
                "CC7": "系统运行 - 漏洞管理流程是否完善",
                "CC8": "变更管理 - CI/CD是否有安全控制",
            },
            "evidence_required": [
                "安全策略文档",
                "访问控制矩阵",
                "漏洞扫描报告",
                "事件响应记录",
                "变更审批记录",
            ]
        },
        "ISO27001": {
            "name": "ISO 27001",
            "categories": {
                "A5": "信息安全策略",
                "A6": "组织信息安全",
                "A8": "资产管理",
                "A12": "运营安全",
                "A14": "系统获取与维护",
            },
            "evidence_required": [
                "信息安全政策",
                "风险评估报告",
                "资产清单",
                "运营程序文档",
                "系统维护记录",
            ]
        }
    }
# ...
    def generate_checklist(self, framework):
        """生成合规检查清单"""
        fw = self.FRAMEWORKS.get(framework)
        if not fw:
            return f"未知框架: {framework}"
# ...
        print(f"\n{'='*50}")
        print(f"合规检查清单: {fw['name']}")
        print(f"{'='*50}")
# ...
        print(f"\n控制类别:")
        for code, desc in fw["categories"].items():
            print(f"  [{code}] {desc}")
            print(f"       状态: [ ] 已实施  [ ] 部分实施  [ ] 未实施")
# ...
        print(f"\n所需证据材料:")
        for i, evidence in enumerate(fw["evidence_required"], 1):
            print(f"  {i}. {evidence}")
            print(f"     状态: [ ] 已准备  [ ] 准备中  [ ] 未准备")
# ...
        return f"\n检查清单已生成,共 {len(fw['categories'])} 个控制类别, {len(fw['evidence_required'])} 项证据材料"
# ...
if __name__ == "__main__":
    prep = CompliancePrep()
    print(prep.generate_checklist("SOC2"))
    print(prep.generate_checklist("ISO27001"))
```

### 场景三:安全程序建设方案
```yaml
# 四季度安全程序建设方案
security_program:
  Q1_foundation:
    name: "基础建设"
    weeks:
      - "1-2: 资产清单(我们有什么?)"
      - "3-4: 风险评估(什么最重要?)"
      - "5-6: 关键控制(认证、密钥、备份)"
      - "7-8: 基础扫描(依赖、代码密钥)"
      - "9-10: 事件响应计划"
      - "11-12: 安全意识基础"
# ...
  Q2_automation:
    name: "自动化"
    items:
      - "CI/CD安全扫描(SAST、依赖审计)"
      - "自动化密钥检测(pre-commit钩子)"
      - "集中化日志与基础告警"
      - "季度访问审查"
      - "漏洞管理流程"
# ...
  Q3_maturity:
    name: "成熟度提升"
    items:
      - "渗透测试(首次外部评估)"
      - "安全架构评审"
      - "数据分类与处理策略"
      - "供应商安全评估"
      - "漏洞赏金计划(小规模启动)"
# ...
  Q4_optimization:
    name: "优化"
    items:
      - "合规框架对齐(SOC 2, ISO 27001)"
      - "红队演练"
      - "安全指标看板"
      - "安全冠军计划"
      - "供应链安全(SBOM、签名制品)"
```

## 不适用场景

以下场景网络安全评估引擎专业版不适合处理：

- 渗透测试未授权目标
- 物理安全防护
- 社会工程学攻击

## 触发条件

需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于非本工具能力范围的需求.
## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 从免费版升级
专业版完全兼容免费版评估方法,新增企业级能力:

```bash
# 免费版:基础三层检查
bash security-check.sh
# ...
# 专业版:十二阶段深度评估
bash security-check.sh --full --compliance SOC2 --report html
```

### 首次安全评分
```bash
# 运行100分制安全评分
python3 security_score.py --dimensions all --output report.html
```

#
## 配置示例
### 安全指标看板
```yaml
security_dashboard:
  vulnerability_management:
    - open_critical: 0       # 目标:始终为0
    - open_high: 0           # 目标:少于5
    - mttr_critical: "24h"   # 平均修复时间
    - scan_coverage: "100%"  # 扫描覆盖率
  incident_management:
    - incidents_this_quarter: 0
    - mttd: "< 1h"           # 平均检测时间
    - mttr: "< 24h"          # 平均恢复时间
  access_control:
    - mfa_adoption: "100%"
    - stale_accounts: 0       # 超过90天未使用
    - access_reviews: "按时完成"
```

### 扫描计划配置
| 扫描类型 | 频率 | 工具示例 |
|---:|---:|---:|
| 依赖扫描 | 每次CI构建 | npm audit, pip-audit, trivy |
| SAST(代码) | 每次PR | Semgrep, CodeQL, Bandit |
| 密钥扫描 | 每次提交 | GitLeaks, truffleHog |
| 容器扫描 | 每次镜像构建 | Trivy, Grype, Snyk |
| DAST(运行时) | 每周 | OWASP ZAP, Nuclei |
| 渗透测试 | 每季度 | 人工+自动化 |
| 红队演练 | 每年 | 外部安全公司 |

## 最佳实践
1. **假设已被入侵**:设计时假设攻击者已在内部,验证一切.
2. **零信任架构**:从不信任,始终验证,最小权限.
3. **深度防御**:多层安全控制,无单点故障.
4. **安全左移**:在开发早期集成安全,而非上线前检查.
5. **持续监控**:安全是持续过程,不是一次性检查.
6. **合规不等同安全**:SOC 2通过不等于安全,合规是起点而非终点.
## 常见问题
### Q1: 专业版评估需要多长时间?
基础评估(Phase 1-4)约1-2天,完整十二阶段评估约1-2周,具体取决于系统复杂度.
### Q2: 安全评分多久更新一次?
建议每月执行一次完整评分,每次重大发布后追加评分。关键指标(如开放漏洞数)应实时监控.
### Q3: 合规映射支持哪些框架?
支持SOC 2、ISO 27001、GDPR、HIPAA、PCI DSS、SOX等主流框架。可自定义映射规则.
### Q4: 漏洞SLA如何自动化?
通过CI/CD集成,在部署前检查漏洞SLA状态。超过SLA的严重/高危漏洞将阻断部署.
### Q5: 如何与免费版评估结果对接?
专业版使用相同的评估方法论,免费版发现的问题可直接导入专业版威胁登记表进行SLA跟踪.
## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+(使用评分引擎时需要)
- **Shell**: Bash(脚本示例使用Bash语法)

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| grep | 文本搜索工具 | 必需 | 系统自带 |
| python3 | 运行时环境 | 推荐 | python.org 下载 |
| npm | 包管理器 | 按需 | nodejs.org 下载 |
| trivy | 漏洞扫描器 | 推荐 | 官方安装指南 |
| semgrep | SAST工具 | 推荐 | `pip install semgrep` |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 专业版为知识驱动+工具集成模式
- 集成的扫描工具(Semgrep, Trivy等)使用各自的配置
- 无需额外API Key即可使用核心评估能力

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级安全评估、合规审计与安全治理任务

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

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "网络安全评估引擎专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "cybersecurity engine pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
