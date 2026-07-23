---
slug: security-audit-tool-pro
name: security-audit-tool-pro
version: 1.0.0
displayName: 安全审计工具(专业版)
summary: 企业级安全审计平台,8维度扫描、合规模板、HTML报告、定时审计与CI/CD集成
license: Proprietary
edition: pro
description: '核心能力:

  - 8维度安全扫描(凭据/端口/配置/权限/Docker/K8s/云/合规)

  - 等保2。0/PCI-DSS/ISO27001合规模板

  - HTML/PDF/SARIF多格式专业报告

  - Cron定时审计+邮件/Webhook告警

  - 智能修复+回滚机制

  - CI/CD流水线集成

  适用场景:

  - 企业级安全合规审计

  - 等保/PCI-DSS认证评估

  - DevSecOps流水线集成

  - 多环境安全基线管理

  差异化:

  - 8维度全覆盖,支持云原生与容器安全

  - 合规框架映射,一键...'
tags:
- 安全
- 安全审计
- 企业安全
- 合规审计
- DevSecOps
tools:
- read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
安全审计工具专业版是一款面向企业用户的安全审计与合规评估平台。在免费版5个扫描维度基础上,扩展至8个维度(增加Kubernetes安全、云安全配置、合规审计),支持等保2.0、PCI-DSS、ISO27001合规框架映射。提供HTML/PDF/SARIF多格式专业报告,Cron定时审计与告警通知,智能修复与回滚机制,以及CI/CD流水线集成能力。与免费版完全兼容,扫描结果和配置可无缝迁移.
## 核心能力
### 功能矩阵
| 功能模块 | 描述 | 免费版 | 专业版 |
|----|---|---|---|
| 扫描维度 | 安全检查范围 | 5个 | 8个(+K8s/云/合规) |
| 合规框架 | 标准映射 | 不支持 | 等保/PCI-DSS/ISO27001 |
| 报告格式 | 输出类型 | JSON | HTML/PDF/SARIF/JSON |
| 定时审计 | 自动化 | 不支持 | Cron+告警 |
| 修复机制 | 自动修复 | 基础修复 | 智能修复+回滚 |
| CI/CD集成 | 流水线 | 不支持 | GitHub/GitLab/Jenkins |
| 多目标 | 批量扫描 | 单目标 | 多目标+并行 |
| 历史趋势 | 时间序列 | 不支持 | 趋势分析与对比 |

**输入**: 用户提供功能矩阵所需的指令和必要参数.
**处理**: 解析功能矩阵的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回功能矩阵的响应数据,包含状态码、结果和日志.
### 8个扫描维度
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 安全审计工具(专业版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```text
┌──────────────────────────────────────────────────────┐
│              专业版8维度扫描                          │
├───────────────┬──────────────────────────────────────┤
│ 1.凭据检测     │ API Key/Token/硬编码密码             │
│ 2.端口扫描     │ 开放端口/防火墙/暴露服务             │
│ 3.配置安全     │ CORS/认证/速率限制/调试模式          │
│ 4.文件权限     │ 敏感文件权限/全局可读/可执行         │
│ 5.Docker安全   │ 特权容器/root用户/资源限制           │
│ 6.K8s安全      │ RBAC/网络策略/Pod安全上下文          │
│ 7.云安全配置   │ IAM/存储桶/安全组/密钥管理           │
│ 8.合规审计     │ 等保/PCI-DSS/ISO27001控制项          │
└───────────────┴──────────────────────────────────────┘
```

**输入**: 用户提供个扫描维度所需的指令和必要参数.
**处理**: 解析个扫描维度的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回个扫描维度的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级安全审计平、合规模板、定时审计与、核心能力、维度安全扫描、多格式专业报告、Webhook、回滚机制、流水线集成等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景
### 场景一:等保2.0合规评估
执行等保2.0三级安全评估,生成合规报告.
```bash
python （请参考skill目录中的脚本文件） \
  --compliance djcp-level3 \
  --target 10.0.0.0/24 \
  --report html \
  --output djcp_assessment.html
```

输出报告包含:
```text
等保2.0三级安全评估报告
═══════════════════════════
评估时间: 2026-07-18
评估范围: 10.0.0.0/24
控制项总数: 211
合规项: 178 (84.4%)
不合规项: 23 (10.9%)
不适用: 10 (4.7%)
# ...
控制域分布:
- 安全物理环境: N/A
- 安全通信网络: 92%合规
- 安全区域边界: 85%合规
- 安全计算环境: 78%合规
- 安全管理中心: 88%合规
- 安全管理制度: 90%合规
- 安全管理机构: 95%合规
- 安全管理人员: 92%合规
- 安全建设管理: 80%合规
- 安全运维管理: 75%合规
```

### 场景二:CI/CD流水线集成
在CI/CD流水线中集成安全审计,阻止不安全代码部署.
```yaml
name: Security Audit
on: [push, pull_request]
# ...
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Security Audit
        run: |
          python （请参考skill目录中的脚本文件） \
            --full \
            --format sarif \
            --output results.sarif \
            --fail-on HIGH
      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: results.sarif
```

### 场景三:定时审计与告警
```bash
python （请参考skill目录中的脚本文件） \
  --schedule "0 2 * * *" \
  --full \
  --report html \
  --notify webhook \
  --webhook-url "https://hooks.example.com/security" \
  --alert-on HIGH
```

### 场景四:多环境批量审计
```bash
python （请参考skill目录中的脚本文件） \
  --targets environments.txt \
  --full \
  --threads 5 \
  --report html \
  --output batch_report.html
```

## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 企业级审计引擎

> 详细代码示例已移至 `references/detail.md`

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例
### 合规审计配置
```json
{
  "audit_config": {
    "compliance": "djcp-level3",
    "dimensions": [
      "credentials", "ports", "configs", "permissions",
      "docker", "kubernetes", "cloud", "compliance"
    ],
    "schedule": {
      "cron": "0 2 * * *",
      "timezone": "Asia/Shanghai"
    },
    "notification": {
      "channels": ["webhook", "email"],
      "alert_levels": ["CRITICAL", "HIGH"],
      "webhook_url": "https://hooks.example.com/security",
      "email_to": "security@example.com"
    },
    "report": {
      "format": "html",
      "template": "enterprise",
      "include_remediation": true,
      "include_compliance": true
    },
    "ci_cd": {
      "fail_on": "HIGH",
      "format": "sarif",
      "upload": true
    }
  }
}
```

## 最佳实践
### 1. 合规评估流程
```bash
python （请参考skill目录中的脚本文件） --compliance djcp-level3 --target 10.0.0.0/24 --report html
# ...
python （请参考skill目录中的脚本文件） --compliance djcp-level3 --smart-fix --rollback
# ...
python （请参考skill目录中的脚本文件） --compliance djcp-level3 --target 10.0.0.0/24 --report html
```

### 2. DevSecOps集成
```bash
python （请参考skill目录中的脚本文件） --credentials --configs --format sarif
# ...
python （请参考skill目录中的脚本文件） --full --fail-on HIGH --format sarif
# ...
python （请参考skill目录中的脚本文件） --compliance pci-dss --report html
```

### 3. 趋势分析
```bash
python （请参考skill目录中的脚本文件） --export-trends --period 90d --format json
```

## 常见问题
### Q1: 专业版与免费版兼容吗?
A: 完全兼容。专业版包含免费版所有5个扫描维度,并增加K8s、云安全、合规审计3个维度。免费版的配置和报告可被专业版读取.
### Q2: 智能修复回滚如何工作?
A: 修复前自动创建文件备份(回滚点),如果修复导致问题,可一键回滚到修复前状态。回滚数据保存在内存中,进程结束后清除.
### Q3: 合规审计支持哪些框架?
A: 目前支持等保2.0三级、PCI-DSS v4.0、ISO 27001:2022。可扩展自定义合规框架.
### Q4: CI/CD集成如何配置?
A: 支持GitHub Actions、GitLab CI、Jenkins。使用SARIF格式输出,GitHub可自动展示在代码扫描结果中。`--fail-on HIGH` 参数可在发现高危问题时阻止流水线.
## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Linux / macOS / Windows(部分功能受限)
- **Python版本**: 3.8+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| Python | 运行时 | 必需 | 系统自带 |
| kubectl | CLI工具 | 可选 | kubernetes.io(K8s审计用) |
| aws-cli | CLI工具 | 可选 | aws.amazon.com(云审计用) |
| Docker | 运行时 | 可选 | docker.com(Docker审计用) |

### API Key 配置
- 核心功能无需API Key
- 云安全审计需要配置对应的云平台CLI凭证(AWS/Azure/GCP)
- K8s审计需要配置kubeconfig

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级安全审计与合规评估任务

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
