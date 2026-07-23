---
slug: "firewall"
name: "firewall"
version: "1.0.0"
displayName: "Firewall"
summary: "按安全最佳实践配置服务器与云防火墙,封堵风险"
license: "Proprietary"
description: |-
  Configure firewalls on servers and cloud providers with security best
  practices。核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Security
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# Firewall

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Configure firewalls on servers and cloud providers with security best | 支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Configure firewalls on servers and cloud providers with security best
  practices
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 防火墙配置 | 服务器IP和规则集 | 防火墙规则和端口策略 |
| 云防火墙管理 | 云平台和安全组配置 | 安全组规则和网络ACL |
| 安全审计 | 防火墙规则和流量日志 | 规则审计报告和风险提示 |

**不适用于**：非网络防火墙的安全防护(如应用层WAF)

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| target_host | string | 是 | 目标服务器IP或主机名 |
| action | string | 否 | 操作类型, 可选: allow/deny/audit, 默认: audit |

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

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 工具依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。

## 常见问题

### Q1: 如何开始使用Firewall？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Firewall有什么限制？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖云服务，需要网络连接
