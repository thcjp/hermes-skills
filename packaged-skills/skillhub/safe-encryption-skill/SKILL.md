---
slug: "safe-encryption-skill"
name: "safe-encryption-skill"
version: "0.1.0"
displayName: "Safe Encryption"
summary: "Encrypt, decrypt, and manage keys with the SAFE CLI — a modern GPG alternative"
license: "Proprietary"
description: |-
  Encrypt, decrypt, and manage keys with the SAFE CLI — a modern GPG alternative
  with post-quantum 。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Other
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# Safe Encryption

## 核心能力

- Encrypt, decrypt, and manage keys with the SAFE CLI — a modern GPG alternative
  with post-quantum
#
## 适用场景

### Protect API Keys / .env Files
> 已移至 `references/detail.md`

### Share Secrets with a Teammate
> 已移至 `references/detail.md`

### Encrypt Backup Before Cloud Upload
> 已移至 `references/detail.md`

### Encrypt Entire Directories
> 已移至 `references/detail.md`

### Git-Friendly Encrypted Secrets
> 已移至 `references/detail.md`

### Separation of Duties (Two People Required)
> 已移至 `references/detail.md`

### Two-Factor Encryption (Password + Key)
> 已移至 `references/detail.md`

### Team Encryption + Emergency Backup
> 已移至 `references/detail.md`

### Post-Quantum Hybrid Protection
> 已移至 `references/detail.md`

### Temporary Decryption (No File on Disk)
> 已移至 `references/detail.md`

### Password Rotation
> 已移至 `references/detail.md`

### Key Rotation (Compromised Key)
> 已移至 `references/detail.md`

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
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
| 待审查内容为空 | 用户未提供内容 | 提示用户提供待审查的代码 |
| 内容格式不识别 | 传入不支持的内容格式 | 列出支持的格式, 建议转换后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 |
| 检查项超出范围 | 传入了不存在的检查维度 | 列出可用检查维度, 使用默认全部检查 |
| 审查超时 | 内容过长导致处理超时 | 建议分段审查, 每段不超过5000字 |
| 其他异常 | 内部处理异常 | 检查输入后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 |

## 依赖说明

### 运行环境
> 已移至 `references/detail.md`

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
> 已移至 `references/detail.md`

### 可用性分类
> 已移至 `references/detail.md`


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

> 已移至 `references/detail.md`

### 示例1：基础用法
> 已移至 `references/detail.md`

## 常见问题

> 已移至 `references/detail.md`

### Q1: 如何开始使用Safe Encryption？
> 已移至 `references/detail.md`

### Q2: 遇到错误怎么办？
> 已移至 `references/detail.md`

### Q3: Safe Encryption有什么限制？
> 已移至 `references/detail.md`

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
