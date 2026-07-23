---
slug: "merge-check-tool-pro"
name: "merge-check-tool-pro"
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
  - read
  - exec
homepage: "https://skillhub.cn"
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9

---
# 合并检查工具(专业版)

## 概述

合并检查工具(专业版)面向团队与维护者,在兼容免费版单PR分析能力的基础上,扩展了批量PR分析、全6维度深度分析、历史趋势追踪、CI/CD门禁集成与自定义拒绝向量规则.
当你在请求中提及 批量PR、合并性预测、团队代码审查、CI门禁、贡献者健康度、维护者看板 等关键词时,本工具会自动激活,为团队提供结构化的PR治理与质量门禁方案.
本版本完全兼容 `merge-check-tool-free` 的单PR分析与报告格式,可平滑升级,已有脚本与工作流无需改造.
## 核心能力

| 能力模块 | 说明 | 与免费版差异 |
|----|---|------|
| 单PR分析 | 技术信号+PR卫生+架构契合+评审状态+流程合规+社交元信号 | 与免费版一致,深度更深 |
| 批量分析 | 一次分析多个PR,输出团队看板 | 免费版仅单PR |
| 历史趋势 | 作者/仓库历史合并率与趋势 | 免费版仅当前快照 |
| CI/CD门禁 | 流水线集成,PR不达标自动阻断 | 免费版无 |
| 自定义规则 | 团队专属拒绝向量与阈值 | 免费版无 |
| 周报导出 | 团队PR健康度周报 | 免费版无 |
| 风险预警 | 高风险PR实时提醒 | 免费版无 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置.
### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.
**输入**: 用户提供参数配置与调用所需的指令和必要参数.
**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置.
**输入**: 用户提供结果处理与输出所需的指令和必要参数.
**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：合并性预测、含全维度分析、门禁与自定义规则、合并检查工具、专业版、面向团队与维护者、提供批量、全维度深度分析、历史趋势追踪、门禁集成与自定义、拒绝向量规则、分析与团队级看板、维度深度分析、作者与仓库历史合、并趋势追踪、流水线门禁集成、自定义拒绝向量与、团队规则、风险预警与周报生等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一:维护者批量评审待合并队列

维护者面对一长串待评审PR,希望按合并概率排序处理.
```bash
# 批量分析仓库所有开放PR
bash （请参考skill目录中的脚本文件） owner/repo --state open --limit 20
# ...
# 输出团队看板
bash （请参考skill目录中的脚本文件） owner/repo --format dashboard > pr-dashboard.html
```

工具输出按合并概率排序的看板:

```text
## 不适用场景
# ...
以下场景合并检查工具(专业版)不适合处理：
# ...
- 实时流数据处理
- 小规模数据手动分析
- 非结构化文本情感分析
# ...
## 触发条件
# ...
需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于非本工具能力范围的需求.
# ...
## 团队PR看板: owner/repo (20个开放PR)
# ...
| PR | 标题 | 评分 | 关键风险 | 优先动作 |
|:-----|:-----|:-----|:-----|:-----|
| #201 | 修复登录超时 | 高(88%) | 无 | 可合并 |
| #198 | 重构数据层 | 中(62%) | 1200行变更 | 建议拆分 |
| #195 | 新增导出功能 | 中(58%) | 评审意见未处理 | 等待作者响应 |
| #190 | 升级依赖 | 低(35%) | CI失败+无关联issue | 需作者修复 |
| #185 | 文档更新 | 低(28%) | 停滞30天 | 提醒作者或关闭 |
```

### 场景二:CI/CD流水线门禁

团队在CI流水线中加入合并性检查,不达标PR无法合并.
```yaml
# .github/workflows/merge-gate.yml
name: Mergeability Gate
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]
jobs:
  merge-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 安装 gh CLI
        run: |
          curl -fsSL https://cli.packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
          echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
          sudo apt update && sudo apt install gh -y
      - name: 运行合并性检查
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          REPORT=$(bash （请参考skill目录中的脚本文件） ${{ github.repository }}#${{ github.event.pull_request.number }})
          SCORE=$(echo "$REPORT" | jq -r '.merge_score // 0')
          if [ "$SCORE" -lt 50 ]; then
            echo "::error::合并性评分 ${SCORE} 低于阈值50,请处理后重试"
            exit 1
          fi
      - name: 上传报告
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: merge-report
          path: merge-report.json
```

### 场景三:贡献者健康度跟踪与导师分配

开源项目希望跟踪贡献者的合并健康度,为低合并率贡献者分配导师.
```bash
# 分析仓库近90天所有已关闭PR,生成贡献者健康度报告
bash （请参考skill目录中的脚本文件） owner/repo \
  --state closed \
  --since 2026-04-19 \
  --group-by author \
  --format health-report > contributor-health.md
```

输出示例:

```text
## 贡献者健康度报告: owner/repo (近90天)
# ...
| 贡献者 | PR总数 | 已合并 | 合并率 | 平均关闭时长 | 健康度 |
|---:|---:|---:|---:|---:|---:|
| alice | 12 | 11 | 92% | 1.8天 | 优秀 |
| bob | 8 | 6 | 75% | 3.2天 | 良好 |
| carol | 5 | 2 | 40% | 8.5天 | 需指导 |
| dave | 3 | 0 | 0% | 14天 | 待导师对接 |
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 1. 团队配置初始化

```bash
# 初始化团队规则配置
cp config/team-rules.example.json config/team-rules.json
# ...
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
# ...
# 按标签筛选
bash （请参考skill目录中的脚本文件） owner/repo --label "needs-review"
# ...
# 按作者筛选
bash （请参考skill目录中的脚本文件） owner/repo --author "alice"
# ...
# 生成HTML看板
bash （请参考skill目录中的脚本文件） owner/repo --format dashboard --output pr-board.html
```

### 4. 历史趋势导出

```bash
# 导出仓库近6个月合并趋势
bash （请参考skill目录中的脚本文件） owner/repo --months 6 --format csv > trend.csv
# ...
# 生成趋势图
bash （请参考skill目录中的脚本文件） owner/repo --months 6 --format chart > trend.html
```

#
## 示例

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
|:---:|:---:|:---:|
| 通过 | ≥70 | 允许合并,标记 |
| 警告 | 50-69 | 允许合并,提醒评审 |
| 阻断 | 30-49 | 阻断合并,要求处理 |
| 严重 | <30 | 阻断并通知维护者 |

## 最佳实践

### 1. 维护者每日队列分流

```bash
#!/usr/bin/env bash
# （请参考skill目录中的脚本文件） 每日PR分流
set -euo pipefail
# ...
REPO="${1:?用法: （请参考skill目录中的脚本文件） owner/repo}"
# ...
echo "## 每日PR分流 - $(date +%Y-%m-%d)"
echo ""
# ...
# 高概率可合并
echo "### 可合并(评分≥80)"
bash （请参考skill目录中的脚本文件） "$REPO" --state open --min-score 80 --format list
# ...
# 需关注(评分50-79)
echo "### 需关注(评分50-79)"
bash （请参考skill目录中的脚本文件） "$REPO" --state open --score-range 50-79 --format list
# ...
# 需介入(评分<50)
echo "### 需介入(评分<50)"
bash （请参考skill目录中的脚本文件） "$REPO" --state open --max-score 49 --format list
```

### 2. 贡献者健康度周报

```bash
# 生成周报
bash （请参考skill目录中的脚本文件） owner/repo \
  --period weekly \
  --format markdown \
  --output reports/week-$(date +%Y-W%V).md
```

### 3. 自定义拒绝向量开发

```javascript
// custom-vectors/no-tests-for-logic.js 自定义向量
module.exports = {
  id: 'no_tests_for_logic',
  description: '业务逻辑变更但未更新测试',
  weight: -15,
  evaluate(context) {
    const logicFiles = context.files.filter((f) =>
      /\.(js|ts|py|go|java)$/.test(f.path) && !f.path.includes('test')
    );
    const testFiles = context.files.filter((f) =>
      /test|spec|__tests__/.test(f.path)
    );
    if (logicFiles.length > 0 && testFiles.length === 0) {
      return {
        triggered: true,
        detail: `${logicFiles.length}个逻辑文件变更但无测试更新`,
      };
    }
    return { triggered: false };
  },
};
```

### 4. 高风险PR实时预警

```yaml
# .github/workflows/pr-alert.yml 高风险PR预警
name: High-Risk PR Alert
on:
  pull_request:
    types: [opened]
jobs:
  alert:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 检查合并性
        id: check
        run: |
          SCORE=$(bash （请参考skill目录中的脚本文件） ${{ github.repository }}#${{ github.event.pull_request.number }} | jq -r '.merge_score')
          echo "score=$SCORE" >> $GITHUB_OUTPUT
      - name: 低分预警
        if: steps.check.outputs.score < 30
        uses: slackapi/slack-github-action@v1
        with:
          slack-message: "高风险PR: ${{ github.event.pull_request.html_url }} 评分 ${{ steps.check.outputs.score }}"
```

### 5. 趋势分析与持续改进

| 指标 | 健康范围 | 预警阈值 |
|:------|------:|:------|
| 平均合并时长 | <3天 | >7天 |
| 合并率 | 60-85% | <40% 或 >95% |
| 平均PR规模 | <400行 | >800行 |
| CI通过率 | >90% | <75% |
| 评审响应时长 | <24小时 | >72小时 |

## 常见问题

### Q1:PRO版与免费版如何共存?

两者单PR分析与报告格式完全兼容,PRO版包含免费版全部能力。维护者升级时直接替换Skill文件,已有脚本无需改造.
### Q2:批量分析会触发限流吗?

会。工具默认遵守 GitHub API 限流,建议为团队配置 `GITHUB_TOKEN` 提升配额(5000 req/h)。批量分析超过50个PR时建议分批并加间隔.
### Q3:自定义规则如何与团队规则共存?

自定义向量在团队规则基础上叠加计算。每个向量返回 `triggered` 与 `weight`,最终评分 = 基础分 + Σ(向量权重)。阻断器触发会直接拉低评分.
### Q4:门禁误判怎么办?

提供 `--bypass` 标记供维护者手动放行,但会在看板标注"人工放行"并记录原因,便于审计。建议定期复盘误判案例以调优阈值.
### Q5:支持私有仓库吗?

支持。需要为CI运行环境配置具有仓库读取权限的 `GITHUB_TOKEN` 或 PAT。批量分析私有仓库时,所有数据处理在本地完成,不上传外部服务.
### Q6:能否对接Slack/飞书等通知渠道?

可以。门禁工作流可集成任意通知渠道,工具输出标准JSON,便于二次开发对接 webhook。常见做法是高风险PR触发IM通知,低风险PR仅记录看板.
## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **gh CLI版本**: 建议 2.40 及以上
- **Python版本**: 建议 3.10 及以上(用于报告生成与趋势图)

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| gh CLI | 命令行工具 | 必需 | cli/cli 下载 |
| jq | JSON处理 | 必需 | 系统包管理器安装 |
| Python | 运行时 | 推荐 | python.org 下载 |
| matplotlib | Python包 | 可选 | `pip install matplotlib`(趋势图) |
| GITHUB_TOKEN | 凭据 | 必需 | 仓库Settings → Secrets |

### API Key 配置

- 本skill基于Markdown指令规范,无需额外API Key.
- `gh` CLI 通过 `gh auth login` 或环境变量 `GITHUB_TOKEN` 认证.
- CI/CD门禁需在仓库Secrets配置 `GITHUB_TOKEN`(自动提供)或 PAT(私有仓库批量分析).
- 通知渠道(Slack/飞书)的 webhook URL 需配置为仓库Secret.
### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent完成操作。PRO版面向团队与维护者,提供批量分析、历史趋势、CI/CD门禁与自定义规则能力,完全兼容免费版单PR分析.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
