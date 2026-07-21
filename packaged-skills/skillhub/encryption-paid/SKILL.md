---
slug: encryption-paid
name: encryption-paid
version: "1.0.0"
displayName: 加密工具专业版
summary: 企业级加密管理,支持KMS集成、密钥轮换、合规审计、批量加密与深度代码安全扫描。
license: Proprietary
edition: pro
description: |-
  面向企业安全团队的高级加密管理工具,提供KMS密钥管理集成、自动密钥轮换、合规性审计、批量加密与深度代码安全扫描。核心能力:
  - KMS/Vault密钥管理集成
  - 自动密钥轮换与版本管理
  - 合规性审计(等保/GDPR/PCI-DSS)
  - 批量文件加密与解密
  - 深度代码加密审计
  - 信封加密与密钥派生

  适用场景:
  - 企业级数据加密保护
  - 合规性安全审计
  - 密钥生命周期管理
  - DevSecOps安全集成

  差异化:
  - 专业版完全兼容免费版命令,支持平滑升级
  - 提供KMS/Va...
tags:
- 开发工具
- 安全
- 加密
- 企业级
- 合规审计
tools:
  - - read
- exec
# 加密工具 - 专业版
## 概述
---
# 加密工具专业版

## 核心能力

### 1. KMS/Vault密钥管理集成
集成主流密钥管理服务,实现企业级密钥生命周期管理。

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供KMS/Vault密钥管理集成所需的指令和必要参数。
**处理**: 按照skill规范执行KMS/Vault密钥管理集成操作,遵循单一意图原则。
**输出**: 返回KMS/Vault密钥管理集成的执行结果,包含操作状态和输出数据。

### 2. 自动密钥轮换
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供自动密钥轮换所需的指令和必要参数。
**处理**: 按照skill规范执行自动密钥轮换操作,遵循单一意图原则。
**输出**: 返回自动密钥轮换的执行结果,包含操作状态和输出数据。

### 3. 合规性审计
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供合规性审计所需的指令和必要参数。
**处理**: 按照skill规范执行合规性审计操作,遵循单一意图原则。
**输出**: 返回合规性审计的执行结果,包含操作状态和输出数据。

### 4. 批量文件加密
```bash
#!/bin/bash
echo "=== 批量文件加密 ==="

ENCRYPTION_KEY_ID="${ENCRYPTION_KEY_ID:-app-master-key}"
ENCRYPT_EXTENSIONS=("env" "key" "pem" "p12" "secret" "credentials")
EXCLUDE_DIRS=("node_modules" ".git" "dist" "build")

encrypt_file() {
    local file="$1"
    local output="${file}.encrypted"

    local data_key=$(openssl rand -hex 32)
    local iv=$(openssl rand -hex 12)

    openssl enc -aes-256-gcm \
        -K "$data_key" \
        -iv "$iv" \
        -in "$file" \
        -out "$output"

    local encrypted_key=$(echo -n "$data_key" | openssl enc -aes-256-gcm \
        -K "$MASTER_KEY" -iv "$(openssl rand -hex 12)" | base64)

    cat > "${output}.meta" << EOF
{
    "key_id": "$ENCRYPTION_KEY_ID",
    "algorithm": "aes-256-gcm",
    "iv": "$iv",
    "encrypted_data_key": "$encrypted_key",
    "encrypted_at": "$(date -Iseconds)",
    "original_size": $(stat -f%z "$file" 2>/dev/null || stat -c%s "$file")
}
EOF

    echo "已加密: $file -> $output"
}

echo "扫描需要加密的文件..."
for ext in "${ENCRYPT_EXTENSIONS[@]}"; do
    find . -name "*.$ext" $(printf "! -path */%s/* " "${EXCLUDE_DIRS[@]}") | while read f; do
        if [ ! -f "${f}.encrypted" ]; then
            encrypt_file "$f"
        fi
    done
done

echo -e "\n加密文件清单:"
find . -name "*.encrypted" | while read f; do
    echo "  $f"
done

echo -e "\n批量加密完成"
```

### 5. 深度代码安全扫描
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供深度代码安全扫描所需的指令和必要参数。
**处理**: 按照skill规范执行深度代码安全扫描操作,遵循单一意图原则。
**输出**: 返回深度代码安全扫描的执行结果,包含操作状态和输出数据。
## 适用场景

### 场景一:企业数据加密保护
使用信封加密保护企业敏感数据。

> 详细代码示例已移至 `references/detail.md`

### 场景二:合规性审计
对企业代码进行合规性安全审计。

```bash
#!/bin/bash
echo "=== 企业加密合规审计 ==="

echo "阶段1: 深度代码扫描..."
python3 deep_crypto_auditor.py ./ > crypto-audit.json
echo "代码审计报告: crypto-audit.json"

echo -e "\n阶段2: 合规性检查..."
python3 compliance_auditor.py --template "等保2.0" --output compliance-report.json
python3 compliance_auditor.py --template "GDPR" --output gdpr-report.json
python3 compliance_auditor.py --template "PCI-DSS" --output pci-report.json

echo -e "\n阶段3: 密钥管理审计..."
python3 key_rotation_check.py --kms-config .kms/keys.json

echo -e "\n阶段4: 生成综合报告..."
python3 generate_compliance_report.py \
    --crypto-audit crypto-audit.json \
    --compliance compliance-report.json \
    --gdpr gdpr-report.json \
    --pci pci-report.json \
    --output final-compliance-report.html

echo -e "\n合规审计完成"
echo "报告: final-compliance-report.html"
```

### 场景三:DevSecOps安全集成
将加密检查集成到开发流水线。

```yaml
crypto_security_check:
  stage: security
  image: python:3.11
  script:
    - python3 deep_crypto_auditor.py . --format sarif --output crypto-audit.sarif

    - python3 compliance_auditor.py --template "等保2.0" --fail-on high

    - |
      CRITICAL=$(python3 -c "import json; r=json.load(open('crypto-audit.json')); print(sum(1 for f in r['findings'] if f['severity']=='critical'))")
      if [ "$CRITICAL" -gt 0 ]; then
        echo "发现 $CRITICAL 个严重加密安全问题"
        exit 1
      fi

    - python3 key_rotation_check.py --max-age 90 --fail
  artifacts:
    reports:
      sast: crypto-audit.sarif
    paths:
      - crypto-audit.json
      - compliance-report.json
  only:
    - merge_requests
    - main
```

## 使用流程

### 步骤一:配置KMS
```yaml
version: "2.0"
edition: pro

kms:
  provider: local  # local | aws | vault | aliyun
  key_id: app-master-key
  auto_rotate: true
  rotation_interval_days: 90

compliance:
  templates: [等保2.0, GDPR, PCI-DSS]
  fail_on: [critical, high]

audit:
  deep_scan: true
  report_format: [sarif, html, json]
```

### 步骤二:运行审计
```
请对当前项目进行深度加密安全审计,检查合规性并生成报告。
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Linux / macOS / Windows
- **运行时**:Python 3.8+ / Node.js 16+

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| cryptography | Python库 | 必需 | pip install cryptography |
| bcrypt | Python库 | 推荐 | pip install bcrypt |
| age | 加密工具 | 推荐 | 系统包管理器安装 |
| openssl | TLS工具 | 必需 | 系统自带 |
| HashiCorp Vault | KMS服务 | 可选 | vaultproject.io |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- KMS服务需要配置认证:

```bash
export VAULT_ADDR="https://vault.company.com"
export VAULT_TOKEN="${VAULT_TOKEN}"

export ALIYUN_KMS_ACCESS_KEY_ID="${KMS_ACCESS_KEY}"
export ALIYUN_KMS_ACCESS_KEY_SECRET="${KMS_SECRET}"
```

### 可用性分类
- **分类**:MD+EXEC+PRO(专业版支持KMS集成、自动轮换和深度审计)
- **说明**:企业级加密管理工具,支持密钥生命周期管理和合规审计
- **适用规模**:中小型到大型项目
- **兼容性**:完全兼容免费版命令和配置,支持平滑升级

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100

检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100

检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100

检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过

改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1:专业版如何兼容免费版?
专业版完全兼容免费版的所有加密命令和配置。免费版的 `.encryption.yml` 可直接在专业版使用,专业版会自动启用KMS和深度审计功能。

### Q2:支持哪些KMS服务?
| KMS服务 | 支持状态 | 配置方式 |
|:---------|:---------|:---------|
| 本地KMS | 完全支持 | 内置实现 |
| HashiCorp Vault | 完全支持 | VAULT_ADDR/VAULT_TOKEN |
| 阿里云KMS | 完全支持 | ALIYUN_KMS_CONFIG |
| 腾讯云KMS | 完全支持 | TENCENT_KMS_CONFIG |

### Q3:密钥轮换会影响已有数据吗?
不会。轮换后旧版本密钥保留用于解密旧数据,新数据使用新版本密钥加密。系统自动处理版本兼容。

### Q4:如何生成合规报告?
```bash
python3 compliance_auditor.py --all-templates --format html --output reports/

python3 compliance_auditor.py --template "等保2.0" --format pdf
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
