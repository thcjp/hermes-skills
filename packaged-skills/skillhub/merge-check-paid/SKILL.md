---
slug: "merge-check-paid"
name: "merge-check-paid"
version: "1.0.0"
displayName: "合并检查工具(专业版)"
summary: "批量PR合并性预测,含全维度分析、历史趋势、CI/CD门禁与自定义规则。"
license: "Proprietary"
edition: "pro"
description: |-
  合并检查工具(专业版)面向团队与维护者,提供批量PR合并性预测、全维度深度分析、历史趋势追踪、CI/CD门禁集成与自定义拒绝向量规则。核心能力:
  - 批量PR分析与团队级看板
  - 全6维度深度分析:技术信号、PR卫生、架构契合、评审状态、流程合规、社交元信号
  - 作者与仓库历史合并趋势追踪
  - CI/CD流水线门禁集成
  - 自定义拒绝向量与团队规则
  - 风险预警与周报生成

  适用场景:
  - 维护者批量评审待合并PR队列
  - 团队代码质量门禁与SRE治理
  - 贡献者健康度跟踪与导师分配
  - 大型开源项目PR...
tags:
  - Development
  - 代码审查
  - GitHub
  - 企业级
  - CI/CD
  - DevOps
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# 合并检查工具(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 能力模块 | 支持 | 支持 |
| 与免费版差异 | 不支持 | 支持 |
| 单PR分析 | 不支持 | 支持 |
| 与免费版一致,深度更深 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 说明 | 与免费版差异 |
| --- | --- | --- |
| 单PR分析 | 技术信号+PR卫生+架构契合+评审状态+流程合规+社交元信号 | 与免费版一致,深度更深 |
| 批量分析 | 一次分析多个PR,输出团队看板 | 免费版仅单PR |
| 历史趋势 | 作者/仓库历史合并率与趋势 | 免费版仅当前快照 |
| CI/CD门禁 | 流水线集成,PR不达标自动阻断 | 免费版无 |
| 自定义规则 | 团队专属拒绝向量与阈值 | 免费版无 |
| 周报导出 | 团队PR健康度周报 | 免费版无 |
| 风险预警 | 高风险PR实时提醒 | 免费版无 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项。

**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 单PR分析

针对单PR,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供单PR分析相关的配置参数、输入数据和处理选项。

**输出**: 返回单PR分析的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`单PR分析`的配置文档进行参数调优
### 批量分析

针对批量,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供批量分析相关的配置参数、输入数据和处理选项。

**输出**: 返回批量分析的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`批量分析`的配置文档进行参数调优
#
## 适用场景

### 场景一:维护者批量评审待合并队列

维护者面对一长串待评审PR,希望按合并概率排序处理。

```bash
# 批量分析仓库所有开放PR
bash （请参考skill目录中的脚本文件） owner/repo --state open --limit 20

# 输出团队看板
bash （请参考skill目录中的脚本文件） owner/repo --format dashboard > pr-dashboard.html
```

工具输出按合并概率排序的看板:

```text

## 使用流程

### 1. 团队配置初始化

```bash
# 初始化团队规则配置
cp config/team-rules.example.json config/team-rules.json

# 编辑团队阈值与规则
vi config/team-rules.json
```

### 2. 单PR深度分析(兼容免费版)

```bash
bash （请参考skill目录中的脚本文件） owner/repo#123 --full-dimensions
```

### 3. 批量分析

```bash
# 分析所有开放PR
bash （请参考skill目录中的脚本文件） owner/repo --state open

# 按标签筛选
bash （请参考skill目录中的脚本文件） owner/repo --label "needs-review"

# 按作者筛选
bash （请参考skill目录中的脚本文件） owner/repo --author "alice"

# 生成HTML看板
bash （请参考skill目录中的脚本文件） owner/repo --format dashboard --output pr-board.html
```

### 4. 历史趋势导出

```bash
# 导出仓库近6个月合并趋势
bash （请参考skill目录中的脚本文件） owner/repo --months 6 --format csv > trend.csv

# 生成趋势图
bash （请参考skill目录中的脚本文件） owner/repo --months 6 --format chart > trend.html
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | merge-check处理的内容输入 |, 默认: 全部维度 |
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
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **gh CLI版本**: 建议 2.40 及以上
- **Python版本**: 建议 3.10 及以上(用于报告生成与趋势图)

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| gh CLI | 命令行工具 | 必需 | 相关技术文档 下载 |
| jq | JSON处理 | 必需 | 系统包管理器安装 |
| Python | 运行时 | 推荐 | python.org 下载 |
| matplotlib | Python包 | 可选 | `pip install matplotlib`(趋势图) |
| GITHUB_TOKEN | 凭据 | 必需 | 仓库Settings → Secrets |

### API Key 配置

- 本Skill基于指令驱动,无需额外API Key。
- `gh` CLI 通过 `gh auth login` 或环境变量 `GITHUB_TOKEN` 认证。
- CI/CD门禁需在仓库Secrets配置 `GITHUB_TOKEN`(自动提供)或 PAT(私有仓库批量分析)。
- 通知渠道(Slack/飞书)的 webhook URL 需配置为仓库Secret。

### 可用性分类

- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,。PRO版面向团队与维护者,提供批量分析、历史趋势、CI/CD门禁与自定义规则能力,完全兼容免费版单PR分析。

## 案例展示

### 团队规则配置

```json
{
  "thresholds": {
    "min_merge_score": 50,
    "max_changed_lines": 1000,
    "max_changed_files": 15,
    "max_open_days": 14
  },
  "blockers": [
    { "id": "ci_failing", "weight": -30, "description": "CI检查未通过" },
    { "id": "changes_requested", "weight": -25, "description": "存在未处理的修改意见" },
    { "id": "no_linked_issue", "weight": -10, "description": "未关联issue" },
    { "id": "draft_state", "weight": -100, "description": "草稿状态" }
  ],
  "boosters": [
    { "id": "all_ci_green", "weight": 20, "description": "所有CI通过" },
    { "id": "has_approvals", "weight": 15, "description": "已获得批准" },
    { "id": "single_concern", "weight": 10, "description": "单一职责" }
  ],
  "custom_vectors": [
    {
      "id": "no_tests",
      "check": "files_changed_without_tests",
      "weight": -15,
      "description": "逻辑变更但未更新测试"
    }
  ]
}
```

### CI/CD门禁阈值分级

| 阈值 | 评分范围 | 流水线动作 |
| --- | --- | --- |
| 通过 | ≥70 | 允许合并,标记 |
| 警告 | 50-69 | 允许合并,提醒评审 |
| 阻断 | 30-49 | 阻断合并,要求处理 |
| 严重 | <30 | 阻断并通知维护者 |

## 常见问题

### Q1:PRO版与免费版如何共存?

两者单PR分析与报告格式完全兼容,PRO版包含免费版全部能力。维护者升级时直接替换Skill文件,已有脚本无需改造。

### Q2:批量分析会触发限流吗?

会。工具默认遵守 GitHub API 限流,建议为团队配置 `GITHUB_TOKEN` 提升配额(5000 req/h)。批量分析超过50个PR时建议分批并加间隔。

### Q3:自定义规则如何与团队规则共存?

自定义向量在团队规则基础上叠加计算。每个向量返回 `triggered` 与 `weight`,最终评分 = 基础分 + Σ(向量权重)。阻断器触发会直接拉低评分。

### Q4:门禁误判怎么办?

提供 `--bypass` 标记供维护者手动放行,但会在看板标注"人工放行"并记录原因,便于审计。建议定期复盘误判案例以调优阈值。

### Q5:支持私有仓库吗?

支持。需要为CI运行环境配置具有仓库读取权限的 `GITHUB_TOKEN` 或 PAT。批量分析私有仓库时,所有数据处理在本地完成,不上传外部服务。

### Q6:能否对接Slack/飞书等通知渠道?

可以。门禁工作流可集成任意通知渠道,工具输出标准JSON,便于二次开发对接 webhook。常见做法是高风险PR触发IM通知,低风险PR仅记录看板。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

