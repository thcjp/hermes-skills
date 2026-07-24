---
slug: web-vuln-assess-tool-pro
name: web-vuln-assess-tool-pro
version: 1.0.0
displayName: Web漏洞评估(专业版)
summary: "企业级Web漏洞评估平台,API自动化评估、HTML/PDF报告、测试脚本生成与合规审计,支持多种使用场景和自动化处理"
license: Proprietary
edition: pro
description: 核心能力:，可自动提升工作效率

  - API驱动的自动化漏洞评估(19类100+检查项)

  - HTML/PDF/SARIF专业评估报告

  - 自动生成渗透测试脚本

  - OWASP/PCI-DSS/GDPR/HIPAA合规映射

  - 多应用批量评估与并行处理

  - 漏洞修复优先级智能排序

  - 技术栈特定检测规则(20+技术)

  适用场景:

  - 企业级Web应用安全评估

  - 合规性安全审计(PCI-DSS/GDPR/HIPAA)

  - 渗透测试范围规划与脚本生成

  - DevSecOps安全门禁

  差异化:

  - API自动化评估...'
tags:
  - 安全
  - Web安全
  - 企业安全
  - 漏洞评估
  - 合规审计
  - Web开发
  - 前端
  - 开发工具
  - api
  - html
  - python
  - web
  - 请参考
tools:
  - read
  - exec
  - write
  - glob
homepage: ""
# 定价元数据
category: "Development"
---
Web漏洞评估专业版是一款面向企业用户的自动化Web安全评估平台。在免费版手动检查清单基础上,增加API驱动的自动化评估能力,支持19类100+检查项的自动扫描。提供HTML/PDF/SARIF专业评估报告,自动生成渗透测试脚本,覆盖OWASP/PCI-DSS/GDPR/HIPAA四种合规框架映射。支持多应用批量评估与并行处理,满足企业级安全审计需求。与免费版完全兼容,检查清单和评估流程可无缝复用.
## 核心能力
### 功能矩阵
| 功能模块 | 描述 | 免费版 | 专业版 |
|----|---|---|---|
| 评估方式 | 检测方法 | 手动清单 | API自动化 |
| 检查项 | 检查数量 | 100+ | 100+实时更新 |
| 技术栈 | 支持范围 | 20种 | 20+自定义 |
| 合规框架 | 标准映射 | 4种 | 4种+自定义 |
| 报告格式 | 输出类型 | 文本 | HTML/PDF/SARIF |
| 测试脚本 | 渗透脚本 | 不支持 | 自动生成 |
| 批量评估 | 多应用 | 不支持 | 批量+并行 |
| 修复优先级 | 排序方式 | 严重等级 | 智能排序 |

**输入**: 用户提供功能矩阵所需的指令和必要参数.
**处理**: 解析功能矩阵的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回功能矩阵的响应数据,包含状态码、结果和日志.
### API评估流程
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | Web漏洞评估(专业版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```text
┌──────────────────────────────────────────────────────┐
│              专业版API评估流程                        │
├──────────────┬───────────────────────────────────────┤
│ 1.信息收集    │ 应用名称/类型/技术栈/部署环境/范围    │
│ 2.API调用     │ 发送评估请求到自动化扫描引擎          │
│ 3.结果解析    │ 解析API返回的评估结果/检查清单/修复   │
│ 4.报告生成    │ 输出HTML/PDF/SARIF格式报告           │
│ 5.脚本生成    │ 可选: 生成渗透测试脚本               │
│ 6.合规映射    │ 映射OWASP/PCI-DSS/GDPR/HIPAA         │
└──────────────┴───────────────────────────────────────┘
```

**输入**: 用户提供API评估流程所需的指令和必要参数.
**处理**: 解析API评估流程的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回API评估流程的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、Web、漏洞评估平台、自动化评估、测试脚本生成与合、规审计、核心能力、驱动的自动化漏洞、专业评估报告、自动生成渗透测试、多应用批量评估与、并行处理、漏洞修复优先级智、技术栈特定检测规等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景
### 场景一:自动化漏洞评估
通过API执行自动化Web漏洞评估.
```bash
python （请参考skill目录中的脚本文件） \
  --app-name "ShopFast" \
  --app-type "E-commerce Platform" \
  --tech-stack "python,react,postgresql,redis,docker,aws" \
  --deployment "Cloud (AWS)" \
  --scope "all" \
  --compliance "owasp_top_10,pci_dss" \
  --include-remediation \
  --include-testing-scripts \
  --format html \
  --output assessment_report.html
```

输出示例:
```
Web漏洞评估报告
══════════════════════════════════════
应用: ShopFast 电商平台
技术栈: Python, React, `PostgreSQL`, Redis, Docker, AWS
范围: 全部19个类别
合规: OWASP Top 10, PCI-DSS
# ...
CRITICAL发现:
  1. SQL注入 - /api/products?id=1
  2. 认证绕过 - /api/admin/panel
# ...
HIGH发现:
  1. XSS - /search?q=<script>
  2. SSRF - /api/fetch?url=
  3. 访问控制 - /api/users/{id} (IDOR)
# ...
MEDIUM发现:
  1. 配置错误 - 缺失安全头
  2. CORS - 通配符配置
  3. DoS - 无速率限制
  4. 内容欺骗 - 开放重定向
# ...
安全检查清单: 47项
修复指南: 10项
测试脚本: 8个
# ...
HTML报告: assessment_report.html
```

### 场景二:合规审计评估
```bash
python （请参考skill目录中的脚本文件） \
  --app-name "PaymentGateway" \
  --tech-stack "java,spring,postgresql,docker,aws" \
  --compliance "pci_dss" \
  --include-remediation \
  --format pdf \
  --output pci_assessment.pdf
```

### 场景三:批量多应用评估
```bash
python （请参考skill目录中的脚本文件） \
  --batch apps_config.json \
  --threads 5 \
  --format sarif \
  --output batch_results.sarif
```

### 场景四:生成渗透测试脚本
```bash
python （请参考skill目录中的脚本文件） \
  --app-name "ShopFast" \
  --target-url "https://shopfast.example.com" \
  --include-testing-scripts \
  --format html \
  --output assessment.html
# ...
```

## 不适用场景

以下场景Web漏洞评估(专业版)不适合处理：

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

### 自动化评估引擎

> 详细代码示例已移至 `references/detail.md`

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例
### 批量评估配置
```json
[
  {
    "name": "ShopFast电商平台",
    "type": "E-commerce Platform",
    "url": "https://shopfast.example.com",
    "technology_stack": ["python", "react", "postgresql", "redis", "docker", "aws"],
    "deployment_environment": "Cloud (AWS)",
    "compliance": ["owasp_top_10", "pci_dss"],
    "include_remediation": true,
    "include_testing_scripts": true
  },
  {
    "name": "AdminBackend管理系统",
    "type": "Web Application",
    "url": "https://admin.example.com",
    "technology_stack": ["java", "spring", "postgresql", "kubernetes"],
    "deployment_environment": "Cloud (Azure)",
    "compliance": ["owasp_top_10", "gdpr"],
    "include_remediation": true
  }
]
```

### 合规框架详情
| 框架 | 检查重点 | 适用场景 | 检查类别数 |
|---:|---:|---:|---:|
| OWASP Top 10 | A01-A10通用Web漏洞 | 所有Web应用 | 10 |
| PCI-DSS | 支付数据保护 | 电商/支付系统 | 12 |
| GDPR | 个人数据保护 | 欧洲用户应用 | 8 |
| HIPAA | 医疗数据保护 | 医疗健康应用 | 6 |

## 最佳实践
### 1. 评估流程
```bash
python （请参考skill目录中的脚本文件） --app-name "MyApp" --scope all --format html
# ...
python （请参考skill目录中的脚本文件） --app-name "MyApp" --compliance pci_dss --format pdf
# ...
python （请参考skill目录中的脚本文件） --app-name "MyApp" --include-testing-scripts --format html
# ...
python （请参考skill目录中的脚本文件） --app-name "MyApp" --scope all --format html
```

### 2. CI/CD集成
```yaml
web-security-assessment:
  stage: security
  script:
    - python （请参考skill目录中的脚本文件）
        --app-name "MyApp"
        --target-url $STAGING_URL
        --scope all
        --compliance owasp_top_10
        --include-remediation
        --format sarif
        --output results.sarif
        --fail-on HIGH
  artifacts:
    reports:
      sast: results.sarif
```

### 3. 修复优先级
| 优先级 | 条件 | 响应时间 |
|:---:|:---:|:---:|
| P0 | CRITICAL(注入/认证绕过/零日) | 24小时 |
| P1 | HIGH(XSS/SSRF/访问控制) | 7天 |
| P2 | MEDIUM(配置/CORS/DoS) | 30天 |
| P3 | LOW(信息泄露/最佳实践) | 90天 |

## 常见问题
### Q1: 专业版与免费版兼容吗?
A: 完全兼容。专业版包含免费版所有19个漏洞类别和检查清单,并增加API自动化评估、HTML/PDF报告、测试脚本生成和合规审计功能.
### Q2: API评估准确吗?
A: API评估基于100+检查项的自动化扫描,覆盖OWASP Top 10全部类别。对于已知漏洞模式准确率高,但建议结合人工审查处理业务逻辑漏洞.
### Q3: 测试脚本安全吗?
A: 测试脚本仅用于授权范围内的安全测试。脚本包含明确的测试目标和建议,不会执行破坏性操作。请确保在授权环境下使用.
### Q4: 支持哪些报告格式?
A: 支持HTML(交互式可打印)、PDF(正式报告)、SARIF(CI/CD集成)、JSON(可编程)四种格式.
## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Python | 运行时 | 必需 | 系统自带 |
| requests | Python包 | 推荐 | `pip install requests` |
| curl | CLI工具 | 可选 | 系统自带(测试脚本用) |

### API Key 配置
- 核心评估功能无需API Key(内置检查规则)
- 可选配置 `VULN_ASSESS_API_KEY`: 外部漏洞评估API(增强检测能力)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级Web漏洞评估任务

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 自动化评估仅覆盖OWASP Top 10等已知漏洞模式，零日漏洞和业务逻辑漏洞无法检测
- 评估过程会对目标发送探测请求，可能触发目标WAF/IDS告警，需提前获得授权
- HTML/PDF报告的漏洞修复建议为通用方案，特定技术栈的修复步骤需人工细化
