---
slug: java-development-manual
name: java-development-manual
version: "0.1.0"
displayName: Java Development Man
summary: Java开发手册规约集合，基于阿里巴巴Java开发手册（嵩山版）。 涵盖7大维度：编程规约、异常日志、单元测试、安全规约、MySQL数据库、工程结构、设计规约。
  当用户需要：(1) 编写或审查J...
license: MIT-0
description: |-
  Java开发手册规约集合，基于阿里巴巴Java开发手册（嵩山版）。涵盖7大维度：编程规约、异常日志、单元测试、安全规约、MySQL数据库、工程结构、设计规约。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Development
tools:
  - - read
- exec
---
# Java Development Man

## 核心能力

本手册基于阿里巴巴Java开发手册（嵩山版），将规约分为7个维度。规约按约束力强弱分为：

| 级别 | 含义 | 说明 |
| --- | --- | --- |
| **【强制】** | 必须遵守 | 违反可能导致严重问题 |
| **【推荐】** | 建议遵守 | 提升代码质量和可维护性 |
| **【参考】** | 可选择性采纳 | 根据实际情况判断 |

## 适用场景

1. **命名检查** → 查看 [coding-convention.md](/api/v1/skills/java-development-manual/file?path=references%2Fcoding-convention.md&ownerHandle=shinelon) 的"命名风格"章节
2. **并发问题** → 查看 [coding-convention.md](/api/v1/skills/java-development-manual/file?path=references%2Fcoding-convention.md&ownerHandle=shinelon) 的"并发处理"章节
3. **异常处理** → 查看 [exception-log.md](/api/v1/skills/java-development-manual/file?path=references%2Fexception-log.md&ownerHandle=shinelon)
4. **安全问题** → 查看 [security.md](/api/v1/skills/java-development-manual/file?path=references%2Fsecurity.md&ownerHandle=shinelon)

## 使用流程

### Step 1: 内容解析
按审查标准执行检查
解析待审查内容, 提取以下要素:
- 关键要素: 关键要素
- 关键要素: 关键要素

### Step 2: 逐项检查
按审查标准执行检查
按照 `references/checklist.md` 中的检查清单逐项审查:

| 检查项 | 检查方法 | 通过标准 |
|--------|---------|---------|
| 代码风格 | 多维度审查 | 符合标准 |
| 安全合规 | 多维度审查 | 符合标准 |
| 无障碍性 | 多维度审查 | 符合标准 |

### Step 3: 评级判定
按审查标准执行检查
根据检查结果评定等级:
- A级(优秀): 符合标准
- B级(良好): 符合标准
- C级(及格): 符合标准
- D级(不及格): 符合标准

### Step 4: 生成报告
按审查标准执行检查
输出审查报告, 包含: 总评/各项详情/改进建议/优先级排序。

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
| 待审查内容为空 | 用户未提供内容 | 提示用户提供待审查的代码 |
| 内容格式不识别 | 传入不支持的内容格式 | 列出支持的格式, 建议转换后重试 |
| 检查项超出范围 | 传入了不存在的检查维度 | 列出可用检查维度, 使用默认全部检查 |
| 审查超时 | 内容过长导致处理超时 | 建议分段审查, 每段不超过5000字 |
| 其他异常 | 内部处理异常 | 检查输入后重试 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
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
## 案例展示

### 示例1：基础用法

```
### 代码审查场景

1. **命名检查** → 查看 [coding-convention.md](/api/v1/skills/java-development-manual/file?path=references%2Fcoding-convention.md&ownerHandle=shinelon) 的"命名风格"章节
2. **并发问题** → 查看 [coding-convention.md](/api/v1/skills/java-development-manual/file?path=references%2Fcoding-convention.md&ownerHandle=shinelon) 的"并发处理"章节
3. **异常处理** → 查看 [exception-log.md](/api/v1/skills/java-development-manual/file?path=references%2Fexception-log.md&ownerHandle=shinelon)
4. **安全问题** → 查看 [security.md](/api/v1/sk
```

## 常见问题

### Q1: 如何开始使用Java Development Man？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Java Development Man有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
