---
slug: "workflow-splitter"
name: "workflow-splitter"
version: 1.0.1
displayName: "工作流分解器(专业版)"
summary: "全功能任务拆解引擎，含智能算法、多模型并行编排、并行执行、性能分析与模板库。"
license: "Proprietary"
edition: "pro"
description: |-
  工作流分解器专业版是在免费版基础上的全功能升级，为复杂项目团队提供企业级任务拆解与子任务分配能力。除基础拆解外，解锁智能拆解算法、多模型并行编排、并行执行、性能分析、模板库、自定义路由、团队协作、版本管理八大高级功能。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估.
tags:
  - 任务拆解
  - 工作流分解
  - 多模型编排
  - 并行执行
  - 项目管理
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# 工作流分解器(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 工作流分解器(专业版)多模型并行编排 | 不支持 | 支持 |
| 工作流分解器(专业版)性能分析 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |

## 核心能力

> 详细内容已移至 `references/detail.md` - 

### 1. 智能拆解算法（专业版）

**输入**: 用户提供智能拆解算法（专业版）所需的指令和必要参数.
**处理**: 解析智能拆解算法（专业版）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回智能拆解算法（专业版）的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`智能拆解算法（专业版）`的配置文档进行参数调优
### 2. 多模型并行编排（专业版）
```bash
workflow-splitter execute --step 3 --multi-model --strategy vote
workflow-splitter route config \
  --reasoning "gpt-4o,claude-opus" \
  --coding "claude-sonnet,gpt-4o" \
  --creative "claude-opus"
# ...
workflow-splitter route prefer --provider "anthropic" --task-type "coding"
# ...
workflow-splitter route fallback --primary "gpt-4o" --secondary "claude-sonnet"
```

**编排策略**：

| 策略 | 说明 | 适用场景 |
|:-----|:-----|:-----|
| vote | 多模型投票选最优 | 关键决策步骤 |
| cascade | 主模型失败切换备选 | 高可用要求 |
| parallel | 多模型并行取最快 | 时间敏感 |
| consensus | 多模型达成共识 | 高准确度要求 |
| specialize | 按专长分配子任务 | 复杂多领域 |

**输入**: 用户提供多模型并行编排（专业版）所需的指令和必要参数.
**输出**: 返回多模型并行编排（专业版）的处理结果,包含执行状态码、结果数据和执行日志.
### 3. 并行执行（专业版）
```bash
workflow-splitter analyze-deps --task-id "task-001"
# ...
workflow-splitter execute-parallel --task-id "task-001" --max-workers 8
# ...
workflow-splitter plan --task-id "task-001" --visualize
# ...
workflow-splitter dag --task-id "task-001" --output "deps.png"
```

**并行执行示例**：

```text
第1步: 需求分析 ──┐
                  ├──> 第4步: 集成（依赖1,2,3）
第2步: UI设计   ──┤
                  ├──> 第5步: 测试（依赖4）
第3步: API设计  ──┘
# ...
并行执行：
T0: 步骤1, 2, 3 并行
T1: 步骤4（等待1,2,3完成）
T2: 步骤5（等待4完成）
```

**输入**: 用户提供并行执行（专业版）所需的指令和必要参数.
### 4. 性能分析（专业版）

**输入**: 用户提供性能分析（专业版）所需的指令和必要参数.
**处理**: 解析性能分析（专业版）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回性能分析（专业版）的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`性能分析（专业版）`的配置文档进行参数调优
### 5. 模板库（专业版）
```bash
workflow-splitter template list
# ...
workflow-splitter template install --pack software-dev
workflow-splitter template install --pack data-analysis
workflow-splitter template install --pack consulting
workflow-splitter template install --pack research
# ...
workflow-splitter split "开发电商平台" --template "software-dev"
# ...
workflow-splitter template create "my-template" --from-task "task-001"
# ...
workflow-splitter template export "software-dev" --output "sd.json"
workflow-splitter template import "custom.json"
```

**模板分类**：

| 模板包 | 适用场景 | 步骤数 |
|---:|---:|---:|
| software-dev | 软件开发 | 6-10步 |
| data-analysis | 数据分析 | 4-6步 |
| consulting | 咨询项目 | 8-12步 |
| research | 研究项目 | 5-8步 |
| migration | 系统迁移 | 10-15步 |
| refactor | 代码重构 | 6-8步 |

**输入**: 用户提供模板库（专业版）所需的指令和必要参数.
### 6. 自定义路由（专业版）
```bash
workflow-splitter route add \
  --condition "task_type=coding AND complexity=high" \
  --model "claude-sonnet" \
  --priority 1
# ...
workflow-splitter route list
# ...
workflow-splitter route test --task "开发登录API"
# ...
workflow-splitter route priority --rule-id "rule-001" --priority 1
```

**输入**: 用户提供自定义路由（专业版）所需的指令和必要参数.
**处理**: 解析自定义路由（专业版）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回自定义路由（专业版）的处理结果,包含执行状态码、结果数据和执行日志.
### 7. 团队协作（专业版）
```bash
workflow-splitter team add --member "alice" --skills "frontend"
workflow-splitter team add --member "bob" --skills "backend"
workflow-splitter team add --member "charlie" --skills "devops"
# ...
workflow-splitter assign --task-id "task-001" --strategy balanced
# ...
workflow-splitter team status
# ...
workflow-splitter sync --task-id "task-001"
# ...
workflow-splitter team report --task-id "task-001"
```

**分配策略**：

| 策略(续)| 说明 | 适用场景 |
|:----:|:----:|:----:|
| balanced | 按负载均衡分配 | 通用 |
| skill-based | 按技能匹配 | 专业要求高 |
| round-robin | 轮询分配 | 任务均匀 |
| availability | 按可用性 | 紧急任务 |

**输入**: 用户提供团队协作（专业版）所需的指令和必要参数.
**输出**: 返回团队协作（专业版）的处理结果,包含执行状态码、结果数据和执行日志.
### 8. 版本管理（专业版）
```bash
workflow-splitter version log --task-id "task-001"
# ...
workflow-splitter version diff --task-id "task-001" --from "v1" --to "v2"
# ...
workflow-splitter version rollback --task-id "task-001" --to "v1"
# ...
workflow-splitter version tag --task-id "task-001" --tag "approved"
```

**处理**: 解析版本管理（专业版）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回版本管理（专业版）的处理结果,包含执行状态码、结果数据和执行日志.
#
## 适用场景

### 场景一：企业级项目的WBS分解（项目经理角色）
**痛点**：大型项目需要WBS（工作分解结构），手动分解耗时且易遗漏.
**对策**：用智能算法+模板库快速生成WBS.
```bash
workflow-splitter split "企业ERP系统实施" --template "consulting" --smart
# ...
workflow-splitter report --task-id "task-001" --format wbs --output "wbs.md"
# ...
workflow-splitter assign --task-id "task-001" --strategy skill-based
```

**效果**：WBS生成时间从2天降至2小时，遗漏率降低约80%.
### 场景二：研发团队的任务分配（技术负责人角色）
**痛点**：研发任务需要按成员技能合理分配，手动分配效率低.
**对策**：用团队协作+技能匹配自动分发.
```bash
workflow-splitter split "开发支付模块" --smart
# ...
workflow-splitter assign --task-id "task-001" --strategy skill-based
# ...
workflow-splitter team status
```

### 场景三：多模型协作的复杂任务（AI工程师角色）
**痛点**：复杂任务需要多个模型协作，缺乏统一的编排工具.
**对策**：用多模型并行编排+投票策略.
```bash
workflow-splitter execute --step 1 --multi-model --strategy vote
# ...
workflow-splitter execute --step 3 --multi-model --strategy specialize
```

### 场景四：并行开发的项目管理（敏捷教练角色）
**痛点**：敏捷开发需要并行执行多个用户故事，依赖管理复杂.
**对策**：用依赖图分析+并行执行.
```bash
workflow-splitter analyze-deps --task-id "sprint-1"
# ...
workflow-splitter execute-parallel --task-id "sprint-1" --max-workers 5
# ...
workflow-splitter dag --task-id "sprint-1" --output "sprint-deps.png"
```

### 场景五：咨询项目的结构化拆解（咨询顾问角色）
**痛点**：咨询项目涉及多阶段交付，需要结构化拆解与进度追踪.
**对策**：用咨询模板+版本管理.
```bash
workflow-splitter split "数字化转型咨询" --template "consulting"
# ...
workflow-splitter version tag --task-id "task-001" --tag "client-approved"
# ...
workflow-splitter rebalance --task-id "task-001"
# ...
workflow-splitter report --task-id "task-001" --format gantt --output "gantt.html"
```

### 场景六：产品发布的checklist生成（产品经理角色）
**痛点**：产品发布涉及多部门协作，checklist容易遗漏关键步骤.
**对策**：用模板库生成完整checklist.
```bash
workflow-splitter split "产品v2.0发布" --template "release-checklist"
# ...
workflow-splitter assign --task-id "task-001" --team "marketing,dev,ops"
# ...
workflow-splitter progress --task-id "task-001"
```

> 详细内容已移至 `references/detail.md` - ### 场景七：大型重构的步骤规划（架构师角色）

## 使用流程

### 基础搭建（<60秒）
```bash
workflow-splitter split "重构微服务架构"
# ...
workflow-splitter report
```

### 标准搭建（<120秒）
在基础搭建之上，启用智能算法与模板库：

```bash
workflow-splitter smart enable
# ...
workflow-splitter template install --pack software-dev
workflow-splitter template install --pack data-analysis
workflow-splitter template install --pack consulting
# ...
workflow-splitter split "开发电商平台" --template "software-dev"
# ...
workflow-splitter template list
```

> 详细内容已移至 `references/detail.md` - ### 完整搭建（<300秒）

以下是工作流分解器(专业版)的快速搭建流程，从初始化到完整配置的步骤说明.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:------|------:|:------|:------|
| content | string | 否 | workflow-splitter处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "splitter_result": "splitter_result_value",
      "splitter_metadata": "splitter_metadata_value",
      "splitter_status": "splitter_status_value"
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

中间产物模板参考: `assets/workflow-splitter_template`

## 异常处理

| 问题 | 可能原因 | 解决方案 | 优先级 |
|---:|:---|---:|---:|
| 拆解步骤过粗/过细 | granularity设置不当 | 调整`--granularity`参数 | 中 |
| 智能算法建议不准 | 历史数据不足 | 提供更多反馈；禁用smart用模板 | 中 |
| 多模型结果冲突 | 模型差异大 | 切换策略（vote→consensus） | 中 |
| 并行执行死锁 | 依赖图有环 | 检查依赖；`analyze-deps`检测环 | 高 |
| 团队成员进度不同步 | 同步延迟 | `sync`手动同步；
| 模板不匹配任务 | 模板适用范围窄 | 创建自定义模板；用smart模式 | 低 |
| 路由规则冲突 | 优先级设置错误 | `route list`检查；调整priority | 中 |
| 版本回滚丢失数据 | 回滚到旧版本覆盖新 | 回滚前先export当前版本 | 高 |
| 性能分析无数据 | 执行历史不足 | 执行更多任务积累数据 | 低 |
| 模型API超时 | 网络或服务问题 | 
| 任务分配不均 | 策略不当或技能不匹配 | 切换分配策略；检查成员技能配置 | 中 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（用于智能算法与性能分析，专业版功能）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------:|--------|:-------|:------:|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| workflow-splitter CLI | 命令行工具 | 必需 | 随本技能提供 |
| Python 3.8+ | 运行时 | 专业版必需 | 从python.org安装 |
| Graphviz | 图形可视化 | 专业版可选 | 系统包管理器安装 |

### API Key 配置
- 多模型编排需要各模型提供商的API Key
- API Key通过环境变量配置，禁止硬编码
- 建议将API Key存储在`~/.workflow-splitter/credentials/`目录（已gitignore）
- LLM调用由Agent平台内置LLM提供（专业版路由GPT-4o确保质量）

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，拆解

## 案例展示

### 与项目管理工具集成
```bash
workflow-splitter export --task-id "task-001" --format jira --output "jira.json"
# ...
workflow-splitter export --task-id "task-001" --format asana --output "asana.csv"
# ...
workflow-splitter import --from jira --project "PROJ-001"
```

### 与Agent平台集成
```markdown
将 workflow-splitter-pro 添加到Agent的技能列表中.
Agent通过自然语言指令驱动任务拆解与模型编排.
LLM路由至GPT-4o，确保复杂拆解决策的质量.
```

### 与开发工具集成
```json
{
  "editor.workflow-splitter": {
    "enabled": true,
    "smartSplit": true,
    "parallelExecution": true,
    "teamSync": true
  }
}
```

### 与CI/CD集成
```bash
workflow-splitter split "实现PR #$PR_NUMBER" --smart
# ...
workflow-splitter assign --task-id "task-001" --team "reviewers"
```

> 详细内容已移至 `references/detail.md` - ## 版本升级迁移指南
### 从免费版升级至专业版
1. **无需迁移数据**：专业版完全兼容免费版的任务格式与命令
2. **新增功能激活**：
   - 启用智能算法：`workflow-splitter smart enable`
   - 启用并行执行：`workflow-splitter execute-parallel`
   - 启用团队协作：`workflow-splitter team add`
3. **模板安装**：`workflow-splitter template install --pack software-dev`
4. **指令兼容**：免费版的所有命令在专业版中均可使用

### 版本更新历史
| 版本 | 日期 | 变更内容 |
|----|:--:|---:|
| 1.0.0 | 2026-01 | 初版发布，含八大高级功能 |

## 常见问题

### Q1：免费版与专业版有什么区别？
免费版提供基础拆解能力（任务分析/步骤拆解/模型匹配/进度跟踪/问题诊断）。专业版解锁八大高级功能：智能拆解算法、多模型并行编排、并行执行、性能分析、模板库、自定义路由、团队协作、版本管理。此外提供多角色场景指南、性能优化策略和多平台集成示例.
> 详细内容已移至 `references/detail.md` - ### Q2：智能拆解算法如何学习？
### Q3：多模型并行编排会增加成本吗？
会。多模型并行意味着多次API调用。专业版通过四种方式控制成本：(1) 仅关键步骤用多模型；(2) 简单步骤用低成本模型；(3) 结果缓存复用；(4) 投票策略取最优而非全用.
### Q4：并行执行支持多少个步骤？
受maxWorkers配置限制（默认8）。无依赖的步骤自动并行，有依赖的按拓扑顺序串行.
### Q5：模板库支持自定义吗？
支持。可通过`template create`从已有任务生成模板，也可手动编写模板文件。支持模板的导出与导入，便于团队共享.
### Q6：团队协作如何同步进度？
通过共享任务状态文件同步。每个成员执行完一步后更新状态，其他成员可实时查看。支持冲突检测与解决.
### Q7：版本管理支持分支吗？
支持。每个版本是拆解方案的快照，可通过tag标记。支持任意版本间的对比与回滚。适用于客户确认场景.
> 详细内容已移至 `references/detail.md` - ### Q8：性能分析能识别哪些瓶颈？
### Q9：可以与Jira/Asana集成吗？
可以。专业版支持导出为Jira、Asana、Trello等项目管理工具的格式。也支持从这些工具导入现有项目.
### Q10：自定义路由的规则优先级如何工作？
按priority数值排序（1最高）。优秀个匹配的规则生效。可通过`route priority`调整优先级.
### Q11：专业版数据存储在哪里？安全吗？
所有数据存储在本地`~/.workflow-splitter/`目录。团队协作数据通过加密通道同步。模型API Key通过环境变量配置，不硬编码.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|----|----|----|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

