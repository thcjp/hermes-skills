---
slug: "productivity-improving"
name: "productivity-improving"
version: 1.1.1
displayName: "Productivity Tracker"
summary: "生产力追踪与每日复盘助手,输入活动日志/目标/日报"
license: "Proprietary"
description: |-
  Productivity tracker and daily review assistant。Input activity logs,
  time notes, goals, or a dai。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策.
tags:
  - Productivity
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "exec", "glob", "grep"]
tags: "工具,效率,自动化"
category: "Automation"
---
# Productivity Tracker

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

### 1. Activity Recording
* Real-time activity tracking with start/end timestamps
* Automatic duration calculation
* Support for interruptions and resumption
* Voice and text input support

**处理**: 解析Activity Recording的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Activity Recording的处理结果,包含执行状态码、结果数据和执行日志.
### 2. Smart Categorization
Auto-categorize activities into:

* **Work**: coding, meetings, emails, planning
* **Learning**: reading, courses, research
* **Health**: exercise, meditation, sleep
* **Life**: cooking, cleaning, family time
* **Rest**: entertainment, social media, breaks

**处理**: 解析Smart Categorization的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Smart Categorization的处理结果,包含执行状态码、结果数据和执行日志.
### 3. Time Analysis
* Daily/weekly/monthly time distribution
* Focus time vs. fragmented time analysis
* Peak productivity hours identification
* Work-life balance metrics

**处理**: 解析Time Analysis的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Time Analysis的处理结果,包含执行状态码、结果数据和执行日志.
### 4. Daily Report Generation
```markdown
# ...
**输入**: 用户提供Daily Report Generation所需的指令和必要参数.
**处理**: 解析Daily Report Generation的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Daily Report Generation的处理结果,包含执行状态码、结果数据和执行日志.
# ...
#
## 适用场景
# ...
| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 日报撰写 | 工作内容与日期 | Markdown日报文件 |
| 生产力追踪与每日复盘 | 目标数据与配置参数 | 处理结果与执行状态 |
| 输入活动日志 | 目标数据与配置参数 | 处理结果与执行状态 |
# ...
**不适用于**：需要人工判断的复杂决策场景
# ...
## 使用流程
# ...
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节
# ...
## 输入格式
# ...
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | productivity-improving处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |
# ...
## 输出格式
# ...
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
# ...
## 异常处理
# ...
# ...
| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 
# ...
## 依赖说明
# ...
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
# ...
### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
# ...
### API Key 配置
- 
# ...
### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,
# ...
# ...
**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示
# ...
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
# ...
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
# ...
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
# ...
## 常见问题
# ...
### Q1: 如何开始使用Productivity Tracker？
A: 
# ...
### Q2: 遇到错误怎么办？
A: 
# ...
### Q3: Productivity Tracker有什么限制？
A: 
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
# ...