---
slug: "who-is-actor"
name: "who-is-actor"
version: 1.0.1
displayName: "Who Is Actor"
summary: "Git仓库参与者识别技能。Git repository actor identification skill。核心能力: - 开发工具领域的专业化AI辅助工具 - 基于高人气开源Skil"
license: "Proprietary"
description: |-
  Git repository actor identification skill。核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Development
  - 工具
  - 效率
  - path
  - my-project
  - churn
  - bus-factor
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# Who Is Actor

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Who Is ActorGit仓库参与者识别 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

- Git repository actor identification skill
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

- When users need an aggregate, repository-level view of commit cadence, churn, and rework signals to surface collaboration-process improvement areas
- When users want to compare team-wide patterns (not individuals) such as commit-message conventionality, weekend/late-night ratios, and bus-factor risk
- When users want to understand the visible-engagement distribution across the repository as a starting point for conversation, **not** as a verdict on individuals
- When users need a structured, data-driven artifact to facilitate retrospective discussions about workflow

### 适用场景(补充)
- Performance reviews, calibration, ranking, hiring, firing, layoffs, compensation, or any HR action
- Producing rankings or judgments of individuals' worth, intelligence, or commitment
- Surveillance of specific employees without their knowledge or consent
- Analyzing repositories the user has not confirmed they have authority to inspect

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | who-is-actor处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "actor_result": "actor_result_value",
      "actor_metadata": "actor_metadata_value",
      "actor_status": "actor_status_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/who-is-actor_template`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
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

You don't need to memorize any commands or parameters — simply describe what you need in any language (please supply an absolute repository path along with the request):

### English
```
💬 "Analyze the repository at /path/to/my-project"
💬 "Generate a repository-level collaboration-pattern report for /path/to/my-project"
💬 "Show aggregate commit-cadence and churn signals for /path/to/my-project since 2024-01-01"
💬 "What does the commit-time distribution look like on branch main in /path/to/my-project?"
💬 "Is there a bus-factor risk in /path/to/my-project?"
# ...
```

### 中文
```
💬 "分析一下 /path/to/my-project 这个仓库的协作模式"
💬 "生成 /path/to/my-project 的仓库级提交节奏与流失率报告"
💬 "从 2024 年 1 月开始，分析 main 分支的提交节奏分布"
💬 "看看这个仓库有没有巴士因子风险"
💬 "统计 /path/to/my-project 中提交消息的约定式合规率"
# ...
```

### 日本語
```
💬 "このリポジトリの協作パターンを分析してください /path/to/my-project"
💬 "このリポジトリのコミット時間分布とチャーン率レポートを作成してください"
💬 "このリポジトリの bus-factor リスクを確認してください"
```

### 한국어
```
💬 "이 저장소의 협업 패턴을 분석해 주세요 /path/to/my-project"
💬 "이 저장소의 커밋 케이던스와 churn 지표 보고서를 만들어 주세요"
💬 "이 저장소의 bus-factor 리스크를 확인해 주세요"
```

### Español
```
💬 "Analiza los patrones de colaboración del repositorio en /path/to/my-project"
💬 "Genera un informe a nivel de repositorio sobre cadencia de commits y churn"
💬 "¿Existe riesgo de bus-factor en /path/to/my-project?"
```

### Français
```
💬 "Analyse les motifs de collaboration du dépôt à /path/to/my-project"
💬 "Génère un rapport au niveau du dépôt sur la cadence des commits et le churn"
💬 "Y a-t-il un risque de bus-factor dans /path/to/my-project ?"
```

### Deutsch
```
💬 "Analysiere die Kollaborationsmuster des Repositories unter /path/to/my-project"
💬 "Erstelle einen Repository-Level-Bericht zu Commit-Kadenz und Churn"
💬 "Gibt es ein Bus-Factor-Risiko in /path/to/my-project?"
```

## 常见问题

### Q1: 如何开始使用Who Is Actor？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

