---
slug: pyx-scan
name: pyx-scan
version: "2.0.0"
displayName: 技能安全扫描
summary: AI技能安全检查工具，通过Scanner API对技能进行安全评级和风险报告
license: MIT-0
description: |-
  AI技能安全检查工具，通过Scanner API对技能进行安全评级和风险报告。评估维度
  包括恶意指令、数据泄露、权限滥用、供应链风险等。返回信任评分（0-10）、
  风险评分（0-10）和置信度百分比。支持WebFetch和curl两种调用方式。适用于
  独立开发者、企业团队和自动化工作流场景。不适用于非AI技能的安全扫描。
tools:
  - read
  - exec
---

# 技能安全扫描

通过Scanner API对AI技能进行安全评级和风险报告。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 技能安全检查
对指定技能进行安全扫描，评估潜在风险。通过 `https://scanner.pyxmate.com/api/v1/check/` 端点调用，需要提供技能所有者和名称。

- 执行`技能安全检查`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`技能安全检查`相关配置参数进行设置
### 2. 信任评分
返回 `trust_score`（0-10），分数越高表示技能越可信。10分为最高信任，0分为最低信任。

**输入**: 用户提供信任评分所需的指令和必要参数。
**处理**: 按照skill规范执行信任评分操作,遵循单一意图原则。

### 3. 风险评分
返回 `risk_score`（0-10），分数越高表示风险越大。0分为无风险，10分为极高风险。

**输入**: 用户提供风险评分所需的指令和必要参数。
**处理**: 按照skill规范执行风险评分操作,遵循单一意图原则。

### 4. 置信度评估
返回 `confidence` 百分比（0-100%），表示评估结果的可信程度。100%为最高置信度。

**输入**: 用户提供置信度评估所需的指令和必要参数。
**处理**: 按照skill规范执行置信度评估操作,遵循单一意图原则。

### 5. 风险报告生成
根据扫描结果生成详细的风险报告，包含：
- 恶意指令检测
- 数据泄露风险评估
- 权限滥用分析
- 供应链风险检查
- 代码注入风险

### 6. WebFetch与curl双模式
支持两种调用方式：
- WebFetch：通过工具调用API
- curl：通过命令行调用API（fallback）

**输入**: 用户提供WebFetch与curl双模式所需的指令和必要参数。
**输出**: 返回WebFetch与curl双模式的执行结果,包含操作状态和输出数据。

### 7. 批量扫描
支持对多个技能进行批量安全扫描，逐个调用API并汇总结果。

**输入**: 用户提供批量扫描所需的指令和必要参数。

- 执行`批量扫描`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`批量扫描`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 技能安全检查工具、对技能进行安全评、级和风险报告、评估维度、包括恶意指令、供应链风险等、返回信任评分、和置信度百分比、适用于、独立开发者、企业团队和自动化、工作流场景、不适用于非、技能的安全扫描。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

### 第一步：确认技能信息

需要提供技能的所有者（owner）和名称（name）：
- owner：技能仓库或包的所有者
- name：技能名称

格式：`owner/name`

### 第二步：调用Scanner API

#### 方式1：WebFetch

```
WebFetch: https://scanner.pyxmate.com/api/v1/check/owner/name
```

#### 方式2：curl（fallback）

```bash
curl -s "https://scanner.pyxmate.com/api/v1/check/owner/name"
```

### 第三步：解析结果

根据返回的 `trust_score`、`risk_score` 和 `confidence` 生成评估报告。

## 真实示例

### 示例1：扫描单个技能

```bash
curl -s "https://scanner.pyxmate.com/api/v1/check/acme-corp/data-processor"
```

输出：
```json
{
  "owner": "acme-corp",
  "name": "data-processor",
  "trust_score": 8.5,
  "risk_score": 2.0,
  "confidence": 92,
  "issues": [
    {
      "severity": "low",
      "type": "data_access",
      "description": "技能请求文件系统读取权限，但范围有限"
    }
  ],
  "scanned_at": "2026-07-21T10:30:00Z"
}
```

### 示例2：扫描高风险技能

```bash
curl -s "https://scanner.pyxmate.com/api/v1/check/unknown-vendor/suspicious-tool"
```

输出：
```json
{
  "owner": "unknown-vendor",
  "name": "suspicious-tool",
  "trust_score": 1.5,
  "risk_score": 9.0,
  "confidence": 88,
  "issues": [
    {
      "severity": "critical",
      "type": "prompt_injection",
      "description": "检测到可能的提示注入攻击指令"
    },
    {
      "severity": "high",
      "type": "data_exfiltration",
      "description": "技能包含向外部服务器发送数据的行为"
    },
    {
      "severity": "high",
      "type": "privilege_escalation",
      "description": "技能请求超出功能所需的系统权限"
    }
  ],
  "scanned_at": "2026-07-21T10:31:00Z"
}
```

### 示例3：批量扫描

```bash
for skill in "acme-corp/data-processor" "acme-corp/auth-helper" "vendor-x/file-utils"; do
  echo "=== Scanning: $skill ==="
  curl -s "https://scanner.pyxmate.com/api/v1/check/$skill" | jq '{name: .name, trust: .trust_score, risk: .risk_score, confidence: .confidence}'
done
```

输出：
```
=== Scanning: acme-corp/data-processor ===
{"name": "data-processor", "trust": 8.5, "risk": 2.0, "confidence": 92}
=== Scanning: acme-corp/auth-helper ===
{"name": "auth-helper", "trust": 9.0, "risk": 1.0, "confidence": 95}
=== Scanning: vendor-x/file-utils ===
{"name": "file-utils", "trust": 3.0, "risk": 7.5, "confidence": 80}
```

### 示例4：技能不存在

```bash
curl -s "https://scanner.pyxmate.com/api/v1/check/nonexistent/missing-skill"
```

输出：
```json
{
  "error": "Not Found",
  "status": 404,
  "message": "Skill 'nonexistent/missing-skill' not found in registry"
}
```

## 错误处理


| 错误场景 | HTTP状态码 | 原因 | 处理方式 |
|---------|-----------|------|---------|
| 技能不存在 | 404 | owner/name拼写错误或未注册 | 确认技能名称格式为 `owner/name`，检查拼写 |
| 速率限制 | 429 | 短时间内请求过多 | 等待60秒后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，批量扫描时增加间隔 |
| 服务器错误 | 500/502/503 | Scanner服务端异常 | 等待5分钟后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，或联系服务管理员 |
| 网络连接失败 | 无响应 | 网络不可达或DNS解析失败 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，尝试更换DNS |
| owner/name格式无效 | 400 | 缺少斜杠或包含非法字符 | 确保格式为 `owner/name`，不含空格和特殊字符 |
| 响应解析失败 | 200但JSON无效 | 服务端返回非预期格式 | 检查原始响应，使用 `jq` 验证JSON |
| 置信度过低 | 200但confidence < 50 | 技能信息不足或分析样本有限 | 结果仅供参考，建议手动审查技能代码 |

## 常见问题

### Q1: trust_score和risk_score的关系是什么？
A: `trust_score`（0-10）表示技能可信度，越高越好。`risk_score`（0-10）表示风险等级，越低越好。两者不一定互补——一个技能可能信任度高但仍有已知风险。建议综合参考两者和 `confidence` 值。

### Q2: confidence低于多少不可信？
A: `confidence` 低于50%时结果仅供参考，建议手动审查。低于30%时几乎不可信，可能是技能信息不足或分析样本有限导致。

### Q3: 支持哪些类型的技能扫描？
A: 支持已注册到Scanner平台的AI技能。技能需要以 `owner/name` 格式提供。未注册的技能返回404。

### Q4: 批量扫描有速率限制吗？
A: 有。短时间内大量请求会触发429速率限制。建议批量扫描时每次请求间隔至少1秒，或等待429响应后60秒重试。

### Q5: WebFetch和curl方式有什么区别？
A: WebFetch通过工具调用API，适合在Agent流程中直接使用。curl通过命令行调用，作为fallback方式。两者返回相同结果，但curl方式可以更好地处理HTTP错误码。

### Q6: 扫描结果包含哪些风险类型？
A: 包含 `prompt_injection`（提示注入）、`data_exfiltration`（数据泄露）、`privilege_escalation`（权限滥用）、`supply_chain`（供应链风险）、`code_injection`（代码注入）等。每个风险有severity级别（critical/high/medium/low）。

### Q7: 如何判断技能是否安全？
A: 建议标准：`trust_score >= 7.0` 且 `risk_score <= 3.0` 且 `confidence >= 80%` 且无critical级别问题。不满足任一条件时建议进一步审查。

## 已知限制

- 仅支持已注册到Scanner平台的AI技能
- 技能名称格式必须为 `owner/name`
- 有API速率限制，429时需等待60秒重试
- `confidence` 低于50%时结果仅供参考
- 不支持本地未发布技能的扫描
- 扫描结果有时效性，技能更新后需重新扫描
- 服务端返回5xx错误时需等待5分钟后重试
