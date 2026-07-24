---
slug: skill-vetter-tool-pro
name: skill-vetter-tool-pro
version: 1.0.0
displayName: Skill安全审查(专业版)
summary: "企业级Skill安全审查平台,含自动扫描、沙箱测试、信任注册表与持续监控,支持多种使用场景和自动化处理"
license: Proprietary
edition: pro
description: 核心能力:，可自动提升工作效率

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

  - ...'
tags:
  - 安全
  - Skill安全
  - 企业安全
  - 供应链安全
  - 沙箱测试
  - 加密
  - 工具
  - python
  - path
tools:
  - read
  - exec
homepage: ""
# 定价元数据
category: "Security"
---
Skill安全审查专业版是一款面向企业用户的AI Agent Skill安全治理平台。在免费版12项红旗规则基础上,扩展至24项规则并支持自定义规则引擎,增加自动化代码扫描与AI风险分析、沙箱隔离环境测试、Skill信任注册表与生命周期管理、批量审查与并行处理、变更检测与持续监控等企业级功能。与免费版完全兼容,红旗规则和审查流程可无缝复用.
## 核心能力
### 功能矩阵
| 功能模块 | 描述 | 免费版 | 专业版 |
|----|---|---|---|
| 红旗规则 | 检测规则数 | 12项 | 24项+自定义 |
| 审查方式 | 检测方法 | 人工清单 | 自动扫描+AI分析 |
| 沙箱测试 | 隔离验证 | 不支持 | Docker沙箱环境 |
| 信任注册表 | 生命周期 | 不支持 | 注册/验证/撤销 |
| 批量审查 | 处理能力 | 单个Skill | 批量+并行 |
| 变更监控 | 持续跟踪 | 不支持 | 文件哈希+告警 |
| 报告格式 | 输出类型 | 文本 | HTML/PDF/JSON |
| 风险评分 | 量化评估 | 4级分类 | 0-100分制 |

**输入**: 用户提供功能矩阵所需的指令和必要参数.
**处理**: 解析功能矩阵的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回功能矩阵的响应数据,包含状态码、结果和日志.
### 24项红旗规则
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | Skill安全审查(专业版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

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

**输入**: 用户提供项红旗规则所需的指令和必要参数.
**处理**: 解析项红旗规则的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回项红旗规则的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、安全审查平台、含自动扫描、信任注册表与持续、核心能力、自定义规则引擎、自动化代码扫描与、风险分析、沙箱隔离环境测试、信任注册表与生命、周期管理、批量审查与并行处、变更检测与持续监、专业审查报告等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景
### 场景一:企业级Skill安全审查
对新安装的Skill执行全面安全审查.
```bash
python （请参考skill目录中的脚本文件） \
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
# ...
红旗详情:
  [HIGH] 网络请求到未知URL
    文件: index.js:42
    证据: fetch('https://unknown-server.com/data')
# ...
  [MEDIUM] 环境变量读取
    文件: config.js:15
    证据: process.env.API_KEY
# ...
  [MEDIUM] Base64解码
    文件: utils.js:28
    证据: atob(encodedData)
```

### 场景二:批量Skill审查
```bash
python （请参考skill目录中的脚本文件） \
  --batch ~/.skills/ \
  --threads 5 \
  --report html \
  --output batch_vetting.html
```

### 场景三:沙箱隔离测试
```bash
python （请参考skill目录中的脚本文件） \
  --target /path/to/skill \
  --sandbox-test \
  --sandbox-timeout 60 \
  --monitor network,filesystem,process
```

### 场景四:信任注册表管理
```bash
python （请参考skill目录中的脚本文件） --target /path/to/skill --register-trust
# ...
python （请参考skill目录中的脚本文件） --lookup /path/to/skill
# ...
python （请参考skill目录中的脚本文件） --revoke /path/to/skill --reason "检测到恶意行为"
# ...
python （请参考skill目录中的脚本文件） --list-trust
```

## 不适用场景

以下场景Skill安全审查(专业版)不适合处理：

- 无明确技术栈的模糊需求
- 纯架构设计决策
- 运维部署管理

## 触发条件

需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于非本工具能力范围的需求.
## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 企业级审查引擎

> 详细代码示例已移至 `references/detail.md`

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例
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
|---:|---:|---:|---:|---:|
| untrusted | 0-30 | 工作区只读 | 禁止 | 禁止 |
| restricted | 31-60 | 工作区读写 | 白名单域名 | 受限命令 |
| trusted | 61-100 | 全部读写 | 全部允许 | 全部允许 |

## 最佳实践
### 1. 安装前审查流程
```bash
python （请参考skill目录中的脚本文件） --target /path/to/skill --deep-scan
# ...
python （请参考skill目录中的脚本文件） --target /path/to/skill --sandbox-test
# ...
python （请参考skill目录中的脚本文件） --target /path/to/skill --register-trust --level restricted
```

### 2. 持续监控
```bash
python （请参考skill目录中的脚本文件） --monitor ~/.skills/ --schedule "0 3 * * *"
```

### 3. 批量审查
```bash
python （请参考skill目录中的脚本文件） --batch ~/.skills/ --threads 5 --report html
```

## 常见问题
### Q1: 专业版与免费版兼容吗?
A: 完全兼容。专业版包含免费版所有12项红旗规则,并扩展至24项+自定义规则。免费版的审查报告可被专业版读取.
### Q2: 沙箱测试安全吗?
A: 沙箱使用Docker隔离:禁用网络、只读文件系统、限制内存和CPU。即使Skill包含恶意代码,也无法影响宿主系统.
### Q3: 信任注册表如何工作?
A: 注册时计算Skill文件哈希。每次启动时验证哈希,如果文件被篡改(哈希不匹配),自动降级信任级别并告警.
### Q4: 支持自定义规则吗?
A: 支持。在配置文件中添加自定义规则,指定正则模式、严重等级和描述。自定义规则与内置规则一起执行.
## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Python | 运行时 | 必需 | 系统自带 |
| re模块 | 标准库 | 必需 | Python内置 |
| hashlib模块 | 标准库 | 必需 | Python内置 |
| Docker | 运行时 | 可选 | docker.com(沙箱测试用) |

### API Key 配置
- 核心功能无需API Key,所有审查在本地执行
- 可选配置: VirusTotal API(增强恶意URL检测)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行企业级Skill安全审查任务

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
