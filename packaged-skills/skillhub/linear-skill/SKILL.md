---
slug: "linear-skill"
name: "linear-skill"
version: "1.0.0"
displayName: "Linear"
summary: "经内置Node CLI与Linear API管项目/issue/任务"
license: "Proprietary"
description: |-
  Manage Linear projects, issues, and tasks via the bundled Node CLI and
  the official Linear API。U。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估.
tags:
  - Integrations
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# Linear

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |
| 数据质量检测与清洗规则 | 不支持 | 支持 |

## 核心能力

- Manage Linear projects, issues, and tasks via the bundled Node CLI and
  the official Linear API
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 项目与Issue管理 | 项目名称和操作类型 | Issue创建/更新/查询结果 |
| 工作流自动化 | 触发条件和动作定义 | 自动化规则和执行日志 |
| CLI操作 | Linear CLI命令和参数 | 命令执行结果和数据输出 |

**不适用于**：非Linear API的第三方集成开发

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| project_name | string | 是 | Linear项目名称 |
| cli_command | string | 否 | CLI命令, 可选: list/create/update/close, 默认: list |

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
|:---:|:---:|:---:|:---:|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

```bash
node {baseDir}/（请参考skill目录中的脚本文件） teams
node {baseDir}/（请参考skill目录中的脚本文件） projects
node {baseDir}/（请参考skill目录中的脚本文件） issues
node {baseDir}/（请参考skill目录中的脚本文件） issue ENG-123
node {baseDir}/（请参考skill目录中的脚本文件） createIssue "Title" "Description" "team-id" '{"priority":2}'
node {baseDir}/（请参考skill目录中的脚本文件） updateIssue "issue-id" '{"stateId":"state-id"}'
```

## 常见问题

### Q1: 如何开始使用Linear？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
