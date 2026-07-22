---
slug: "verify-claims"
name: "verify-claims"
version: "1.0.0"
displayName: "Verify Claims"
summary: "This fact-checking skill is mostly coherent, but it can automatically create"
license: "Proprietary"
description: |-
  This fact-checking skill is mostly coherent, but it can automatically
  create delayed follow-up ch。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
  - Research
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# Verify Claims

## 核心能力

- This fact-checking skill is mostly coherent, but it can automatically
  create delayed follow-up ch
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 默认值 |
| mode | string | 否 | 处理模式, 可选: json/text/markdown, 默认: 默认值 |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明"
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

中间产物模板参考: `assets/（根据实际场景填充）`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

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

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "mode": "示例数据"
}
```
**执行日志**:
```
Step 1 [按流程执行]: 示例数据 ✓ (1.2s)
  Gate: 示例数据 ✓
Step 2 [按流程执行]: 示例数据 ✓ (3.5s)
  Gate: 示例数据 ✓
Step 3 [按流程执行]: 示例数据 ✓ (2.1s)
  Gate: 示例数据 ✓
Step 4 [按流程执行]: 示例数据 ✓ (0.8s)
```
**最终输出**:
```
示例数据
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例数据",
  "mode": "示例数据"
}
```
**执行日志**:
```
Step 1 [按流程执行]: 示例数据 ✓ (0.9s)
  Gate: 示例数据 ✓
Step 2 [按流程执行]: 示例数据 ✓ (2.8s)
  Gate: 示例数据 ✗ → 重试
Step 2 [按流程执行]: 示例数据 ✓ (3.1s)
  Gate: 示例数据 ✓
Step 3 [按流程执行]: 示例数据 ✓ (1.5s)
  Gate: 示例数据 ✓
Step 4 [按流程执行]: 示例数据 ✓ (0.6s)
```
**最终输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据",
  "max_retries": 1
}
```
**执行日志**:
```
Step 1 [按流程执行]: 示例数据 ✓ (1.1s)
  Gate: 示例数据 ✓
Step 2 [按流程执行]: 示例数据 ✗ → 重试(1/1)
Step 2 [按流程执行]: 示例数据 ✗ → 超过最大重试次数
流程暂停, 断点: Step 2
```
**输出**(部分结果):
```json
{
  "success": false,
  "error": "Step 2 failed after 1 retries",
  "data": {
    "completed_steps": [1],
    "checkpoint": "step_2",
    "partial_result": "示例数据"
  }
}
```

## 常见问题

### Q1: 如何开始使用Verify Claims？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Verify Claims有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

### When Fact-Checkers Haven't Covered the Topic
If searches return no relevant results:

1. Try broader search terms
2. Try related claims that fact-checkers may have covered
3. If still no results, check if the content is recent (3 days or less)
4. **For fresh content (≤3 days old)**:
   * Acknowledge: "This is very recent content. Professional fact-checkers typically need a few days to verify claims."
   * If scheduling tools are available: Schedule a follow-up fact-check for 3 days later
   * If scheduling is not available: Suggest the user returns in 3 days for updated verification
   * Offer to do preliminary general web research in the meantime
5. **For older content**: Acknowledge "Professional fact-checkers haven't specifically addressed this claim"
6. Offer to do general web research instead
7. Consider if the claim is too obscure or too local for major fact-checkers

### Contradicting Fact-Checkers
If fact-checkers disagree:

1. Present all perspectives fairly
2. Note the disagreement explicitly
3. Consider if they're addressing slightly different aspects
4. Look for consensus on specific sub-points
5. Don't force a conclusion if the evidence is genuinely mixed

### Outdated Information
If fact-checks are old but the claim is current:

1. Note the publication dates
2. Search for more recent fact-checks
3. Consider if circumstances have changed
4. Acknowledge if using older sources due to lack of recent coverage

### Language Barriers
If key fact-checkers are in languages you don't fully understand:

1. Use web_fetch to retrieve the content
2. Focus on verdicts, ratings, and conclusion sections which are often clear
3. Use any English summaries or abstracts
4. Acknowledge limitations if language creates uncertainty

### Bias Concerns
Users may question fact-checker reliability:

1. Stick to well-established, internationally recognized services
2. Present findings from multiple fact-checkers to show consensus
3. Note if you're using fact-checkers from multiple countries/perspectives
4. Acknowledge that no source is perfect, but these are professional verification services
