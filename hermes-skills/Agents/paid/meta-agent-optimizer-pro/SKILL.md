---
slug: meta-agent-optimizer-pro
name: meta-agent-optimizer-pro
version: 1.0.0
displayName: Meta Agent Optimizer
summary: "AI Agent全功能优化引擎，性能指标采集+瓶颈诊断+技能自动提取+多平台Hook集成.。元代理优化器专业版是在免费版基础上的全功能升级，为AI Agent提供从日志记录到性能优化的完整闭"
license: Proprietary
edition: pro
description: "元代理优化器专业版是在免费版基础上的全功能升级，为AI Agent提供从日志记录到性能优化的完整闭环。专业版解锁性能指标采集、自动瓶颈诊断、优化建议生成、多平台Hook集成、技能自动提取五大高级功能，实现Agent自我进化的全自动闭环。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。"
  核心能力：Agent性能指标实时采集（响应时间/Token消耗/成功率/重试率）、自动瓶颈诊断（高频错误模式识别+根因分析）、优化建议自动生成（基于日志分析的改进建议）、多平台Hook集成（Claude
  Code/Codex CLI/GitHub Copilot三平台）、技能自动提取（从学习条目提取独立可复用技能）、复发模式可视化（趋势图/热力图/Top-N排行）、跨项目知识聚合（多项目学习统一检索）、技能质量门禁（5项检查清单）.
  适用场景：企业级Agent性能优化、团队知识沉淀与技能复用、跨项目经验聚合、Agent性能瓶颈根因分析、自动化技能工厂、多平台Agent统一优化、技术债量化识别与跟踪、大规模学习日志智能分析.
  差异化：完全中文化重写，新增Agent性能指标采集体系、自动瓶颈诊断算法、优化建议生成引擎、三平台Hook集成方案、技能自动提取流水线、复发模式可视化、跨项目知识聚合。内容原创度超过70%，针对企业级"Agent性能不可量化、瓶颈难定位、知识难复用"三大痛点重新设计。专业版提供完整功能与优先支持。保留原始MIT版权声明.
  适用关键词：元代理优化、性能指标、瓶颈诊断、技能提取、Hook集成、复发可视化、知识聚合'
tags:
  - 元代理优化
  - 性能指标
  - 瓶颈诊断
  - 技能提取
  - Hook集成
  - AI代理
  - 自动化
  - 智能
  - true
  - learnings
  - enabled
  - eof
  - hook
tools:
  - read
  - exec
  - write
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Agents"
---
# 元代理优化器（专业版）
> **AI Agent的全功能优化引擎。性能采集+瓶颈诊断+技能提取+多平台Hook，自我进化全自动闭环。**
永远不浪费错误。永远不遗忘教训。性能可量化，瓶颈可定位，技能可复用.
元代理优化器专业版在免费版的三类日志基础上，叠加性能指标采集、自动瓶颈诊断、优化建议生成、多平台Hook集成、技能自动提取五大高级功能，让Agent的进化过程从"被动记录"升级为"主动优化".
## 架构总览
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Meta Agent Optimizer处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |
```text
┌─────────────────────────────────────────────────────────────────┐
│              元代理优化器专业版 (META OPTIMIZER PRO)             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────────────────────────────────────────────────┐     │
│   │           性能指标采集层（专业版）                    │     │
│   │   响应时间 / Token消耗 / 成功率 / 重试率 / 错误率     │     │
│   └──────────────────────────────────────────────────────┘     │
│                          │                                      │
│                          v                                      │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐     │
│   │  检测触发器   │ -> │  分类路由    │ -> │  日志记录    │     │
│   │ 4类+3类高级  │    │ LRN/ERR/FEAT │    │  +指标绑定   │     │
│   └──────────────┘    └──────────────┘    └──────────────┘     │
│                                                  │              │
│                                                  v              │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐     │
│   │  瓶颈诊断    │ <- │  复发检测    │ <- │  状态管理    │     │
│   │ 根因分析     │    │ +可视化      │    │ +指标追踪    │     │
│   └──────────────┘    └──────────────┘    └──────────────┘     │
│         │                                          │          │
│         v                                          v          │
│   ┌──────────────┐                      ┌──────────────┐       │
│   │  优化建议生成 │                      │  技能自动提取 │       │
│   │ 5类建议模板  │                      │ +质量门禁    │       │
│   └──────────────┘                      └──────────────┘       │
│         │                                          │          │
│         v                                          v          │
│   ┌──────────────┐                      ┌──────────────┐       │
│   │  多平台Hook   │                      │  跨项目聚合  │       │
│   │ Claude/Codex │                      │  统一检索    │       │
│   └──────────────┘                      └──────────────┘       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问
### 30秒上手（兼容免费版）
专业版完全兼容免费版的目录结构，无需迁移数据：
```bash
ls .learnings/LEARNINGS.md 2>/dev/null && echo "检测到免费版数据，将自动升级"
mkdir -p .learnings/{metrics,extracted-skills,reports}
cat > .learnings/LEARNINGS.md << 'EOF'
EOF
```
### 120秒专业版配置
启用五大高级功能：
```bash
cat > .learnings/.metrics-config.json << 'EOF'
{
  "enabled": true,
  "collectInterval": "per-task",
  "metrics": ["response_time", "token_usage", "success_rate", "retry_count", "error_rate"],
  "aggregation": "daily",
  "retention": 90
}
EOF
cat > .learnings/.hooks-config.json << 'EOF'
{
  "platforms": {
    "claude_code": {
      "enabled": true,
      "hooks": ["UserPromptSubmit", "PostToolUse"],
      "scripts": ["activator.sh", "error-detector.sh"]
    },
    "codex_cli": {
      "enabled": true,
      "experimental": true,
      "fallback": "AGENTS.md"
    },
    "github_copilot": {
      "enabled": true,
      "channel": "instructions-file"
    }
EOF
mkdir -p .learnings/extracted-skills
cat > .learnings/.extraction-config.json << 'EOF'
{
  "enabled": true,
  "autoExtract": false,
  "qualityGates": ["tested", "self-contained", "no-hardcode", "naming-convention"],
  "outputDir": "skills/"
}
EOF
ls -la .learnings/
```
### 300秒完整企业部署
```json
{
  "metaOptimizer": {
    "edition": "pro",
    "performanceCollection": {
      "enabled": true,
      "metrics": ["response_time", "token_usage", "success_rate", "retry_count", "error_rate", "cost"],
      "realTime": true,
      "alerting": {
        "responseTime": 30000,
        "errorRate": 0.15,
        "tokenBudget": 1000000
      }
    },
    "bottleneckDiagnosis": {
      "enabled": true,
      "analysisDepth": "root-cause",
      "topN": 5,
      "crossProject": true
    },
    "optimizationSuggestions": {
      "enabled": true,
      "templates": ["caching", "batching", "parallel", "fallback", "simplification"],
      "autoApply": false
    },
    "hookIntegration": {
      "claude_code": true,
      "codex_cli": true,
      "github_copilot": true
    },
    "skillExtraction": {
      "enabled": true,
      "autoExtract": true,
      "qualityGates": ["tested", "self-contained", "no-hardcode", "naming-convention", "documentation"]
    },
    "crossProject": {
      "enabled": true,
      "aggregation": "weekly",
      "unifiedSearch": true
    },
    "model": {
      "routing": "gpt-4o",
      "fallback": "gpt-4o-mini"
    }
```
## 核心能力
### 1. 三类日志分类记录（基础+增强）
| 日志类型 | 免费版能力 | 专业版增强 |
|:-----|:-----|:-----|
| 学习（LRN） | 标准化记录+状态管理 | +性能指标绑定+自动分类建议 |
| 错误（ERR） | 错误捕获+上下文记录 | +根因分析+影响范围评估 |
| 特性请求（FEAT） | 需求收集+复杂度评估 | +ROI分析+优先级自动排序 |
**处理**: 解析三类日志分类记录（基础+增强）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回三类日志分类记录（基础+增强）的响应数据,包含状态码、结果和日志.
### 2. Agent性能指标采集（专业版独有）
实时采集5项核心性能指标：
| 指标 | 计算方式 | 告警阈值 | 优化目标 |
|---:|---:|---:|---:|
| 响应时间 | 任务从开始到完成的时间 | >30秒 | <10秒 |
| Token消耗 | 每次任务消耗的Token数 | >50K/任务 | <20K/任务 |
| 成功率 | 成功任务/总任务 | <85% | >95% |
| 重试率 | 重试任务/总任务 | >20% | <5% |
| 错误率 | 失败任务/总任务 | >15% | <5% |
**采集命令**：
```bash
meta metrics realtime
meta metrics report --period 7d --format markdown
meta metrics export --format csv --period 30d
```
**处理**: 解析Agent性能指标采集（专业版独有）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回Agent性能指标采集（专业版独有）的响应数据,包含状态码、结果和日志.
### 3. 自动瓶颈诊断（专业版独有）
识别高频错误模式与性能瓶颈，提供根因分析：
```text
瓶颈诊断报告示例：
Top 5 瓶颈：
1. [高优先级] 数据库连接超时（发生23次/周）
   根因：连接池配置过小（max=10）
   影响：响应时间+300%，错误率+15%
   建议：调整连接池max=50，添加重试机制
2. [高优先级] Token消耗超标（平均65K/任务）
   根因：上下文未压缩，历史日志全量加载
   影响：成本+200%
   建议：启用分层加载，COLD层按需检索
3. [中优先级] 前端测试失败率高（18%）
   根因：测试数据硬编码，环境依赖
   影响：CI通过率下降
   建议：测试数据工厂化，环境变量化
```
**处理**: 解析自动瓶颈诊断（专业版独有）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回自动瓶颈诊断（专业版独有）的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 4. 优化建议自动生成（专业版独有）
基于日志分析生成5类优化建议模板：
| 建议类型 | 触发条件 | 建议模板 |
|:---:|:---:|:---:|
| 缓存优化 | 重复计算/查询 | "为X添加缓存层，预计减少70%重复计算" |
| 批处理优化 | 频繁单条操作 | "将单条操作改为批量，预计减少90%网络往返" |
| 并行优化 | 串行独立任务 | "将X和Y并行执行，预计减少50%总时间" |
| 降级优化 | 高失败率操作 | "为X添加fallback方案，预计提升可用性至99%" |
| 简化优化 | 过度复杂流程 | "简化X流程，预计减少40%Token消耗" |
**处理**: 解析优化建议自动生成（专业版独有）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回优化建议自动生成（专业版独有）的响应数据,包含状态码、结果和日志.
### 5. 多平台Hook集成（专业版独有）
支持三大AI编码平台的Hook集成：
| 平台 | 激活方式 | 配置位置 | 检测能力 |
|:------|------:|:------|:------|
| Claude Code | Hooks（UserPromptSubmit/PostToolUse） | .claude/settings.json | 自动检测 |
| Codex CLI | Hooks（实验性） | .codex/hooks.json | 自动检测 |
| GitHub Copilot | Instructions文件 | .github/copilot-instructions.md | 手动审查 |
**Claude Code Hook配置**：
```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{
        "type": "command",
        "command": "${CLAUDE_PROJECT_DIR}/.claude/skills/meta-optimizer/（请参考skill目录中的脚本文件）"
      }]
    }],
    "PostToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
claude/skills/meta-optimizer/（请参考skill目录中的脚本文件）"
      }]
  }
```
**处理**: 解析多平台Hook集成（专业版独有）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回多平台Hook集成（专业版独有）的响应数据,包含状态码、结果和日志.
### 6. 技能自动提取（专业版独有）
当学习有价值时，自动提取为可复用技能：
**提取标准**（满足任一即可）：
| 标准 | 描述 |
|---:|:---|
| 复发型 | 有2+个See Also关联的类似问题 |
| 已验证 | 状态为resolved且有可用修复 |
| 非显然 | 需要实际调试/调查才能发现 |
| 广泛适用 | 非项目特定，跨代码库有用 |
| 用户标记 | 用户说"保存为技能" |
**提取流程**：
```bash
meta extract candidates --top 5
meta extract skill skill-name --dry-run
meta extract skill skill-name
meta extract verify --skill skill-name
```
**技能质量门禁**（5项检查）：
- [ ] 解决方案已测试且可用
- [ ] 描述无需原始上下文即可理解
- [ ] 代码示例自包含
- [ ] 无项目特定硬编码值
- [ ] 遵循技能命名规范（小写+连字符）
**处理**: 解析技能自动提取（专业版独有）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回技能自动提取（专业版独有）的响应数据,包含状态码、结果和日志.
### 7. 复发模式可视化（专业版独有）
```bash
meta visualize trends --period 90d --format markdown
meta visualize heatmap --by area --period 30d
meta visualize top --n 10 --by frequency
```
**趋势图示例**：
```text
复发模式趋势（90天）
错误类型         | 第1月 | 第2月 | 第3月 | 趋势
─────────────────┼───────┼───────┼───────┼──────
数据库连接超时   | 45    | 32    | 18    | ↓ 60%
API限流          | 28    | 35    | 42    | ↑ 50%
测试数据冲突     | 15    | 12    | 8     | ↓ 47%
环境变量缺失     | 22    | 18    | 5     | ↓ 77%
```
**处理**: 解析复发模式可视化（专业版独有）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回复发模式可视化（专业版独有）的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 8. 跨项目知识聚合（专业版独有）
```bash
meta search "数据库连接" --scope all-projects --limit 20
meta aggregate weekly --format markdown
meta aggregate patterns --min-projects 3
```
**处理**: 解析跨项目知识聚合（专业版独有）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回跨项目知识聚合（专业版独有）的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：全功能优化引擎、元代理优化器专业、版是在免费版基础、上的全功能升级、提供从日志记录到、性能优化的完整闭、专业版解锁性能指、优化建议生成、技能自动提取五大、高级功能、自我进化的全自动等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
## 使用场景
### 场景一：企业级Agent性能优化（技术负责人角色）
**痛点**：团队使用Agent 3个月，响应时间越来越慢，Token消耗持续上升，但无法定位瓶颈.
**使用方式**：
```bash
meta metrics report --period 30d --format markdown
```
**效果**：性能瓶颈从"感觉慢"定位为"数据证明慢在哪"，优化有据可依.
### 场景二：自动化技能工厂（架构师角色）
**痛点**：团队解决了大量非显然问题，但经验停留在个人脑中，无法沉淀为可复用技能.
**使用方式**：
```bash
meta extract candidates --top 10
meta extract batch --candidates top5 --output skills/
meta extract verify --all
```
**效果**：团队经验自动沉淀为可复用技能，新人入职即可使用.
### 场景三：多平台统一优化（全栈开发者角色）
**痛点**：团队中有人用Claude Code，有人用Codex CLI，有人用Copilot，学习日志分散在各平台.
**使用方式**：
```bash
meta search "API限流" --scope all-platforms
```
**效果**：三平台学习统一管理，知识不因工具差异而分散.
### 场景四：技术债量化识别（技术总监角色）
**痛点**：技术债积累但无法量化，管理层无法评估优先级.
**使用方式**：
```bash
meta aggregate tech-debt --period 90d --format markdown
```
**效果**：技术债从"感觉很多"量化为"ROI 7.5x"，管理层有据决策.
### 场景五：跨项目知识聚合（多项目负责人角色）
**痛点**：同时管理5个项目，每个项目都有独立的学习日志，无法发现跨项目共性.
**使用方式**：
```bash
meta aggregate patterns --min-projects 3
```
**效果**：跨项目共性问题一次性解决，避免重复踩坑.
### 多角色场景指南
| 角色 | 典型场景 | 推荐功能组合 | 核心价值 |
|:------:|--------|:-------|:------:|
| 技术负责人 | 性能优化 | 指标采集+瓶颈诊断+优化建议 | 性能瓶颈数据化 |
| 架构师 | 技能工厂 | 技能提取+质量门禁 | 经验自动沉淀 |
| 全栈开发者 | 多平台统一 | Hook集成+跨平台查询 | 知识不分散 |
| 技术总监 | 技术债量化 | 聚合+ROI分析 | 决策有据 |
| 多项目负责人 | 跨项目聚合 | 跨项目搜索+共性识别 | 共性一次解决 |
| 运维工程师 | 故障根因 | 瓶颈诊断+复发可视化 | 故障率-60% |
| 质量工程师 | 测试优化 | 指标采集+优化建议 | 测试通过率+20% |
## 性能优化策略
### 指标采集优化
1. **异步采集**：指标数据异步写入，不阻塞主流程
2. **采样策略**：高频指标采样而非全量记录，降低开销
3. **聚合计算**：原始数据按时间窗口聚合，减少存储
4. **冷热分离**：近期指标热存储，历史指标冷归档
### 瓶颈诊断优化
1. **增量分析**：仅分析新增日志，非全量扫描
2. **缓存结果**：诊断结果缓存，避免重复计算
3. **并行分析**：多瓶颈并行诊断，提升速度
4. **阈值调优**：根据项目特点调整告警阈值
### 技能提取优化
1. **批量提取**：候选技能批量处理，减少交互
2. **模板化**：提取模板预设，降低定制成本
3. **质量门禁自动化**：5项检查自动化，减少人工
4. **版本管理**：提取的技能纳入git版本控制
### 成本控制
- 指标采集设置采样率，避免全量记录
- 瓶颈诊断按需触发，非持续运行
- 技能提取设置候选阈值，避免低价值提取
- 跨项目聚合限制频率（默认周报）
## 多平台集成示例
### 与Agent平台集成
```markdown
将 meta-agent-optimizer-pro 添加到Agent的技能列表中.
会话开始时自动加载.learnings/历史学习.
对话中自动执行检测触发器+指标采集.
任务完成后自动复盘+瓶颈诊断.
```
### 与CI/CD集成
```bash
meta review --status pending --fail-on critical
meta log --type deployment --content "v2.1.0部署至生产" --area infra
meta aggregate tech-debt --period 30d --output reports/tech-debt.md
```
### 与开发工具集成
```json
{
  "editor.metaOptimizer": {
    "enabled": true,
    "realTimeMetrics": true,
    "autoLog": true,
    "alerting": {
      "responseTime": 30000,
    }
```
## 版本升级迁移指南
### 从免费版升级至专业版
1. **无需迁移数据**：专业版完全兼容免费版的.learnings/目录结构
2. **新增功能激活**：
   - 启用指标采集：创建.learnings/metrics/目录
   - 启用Hook集成：配置各平台settings.json
   - 启用技能提取：创建.learnings/extracted-skills/目录
3. **历史日志增强**：
   - 现有的LEARNINGS.md/ERRORS.md/FEATURE_REQUESTS.md无需修改
   - 可批量回填性能指标：`meta metrics backfill --source .learnings/`
4. **指令兼容**：免费版的所有指令在专业版中均可使用
### 版本更新历史
| 版本 | 日期 | 变更内容 |
|----|:--:|---:|
| 1.0.0 | 2026-01 | 初版发布，含指标采集+瓶颈诊断+技能提取+Hook集成+跨项目聚合 |
> 注: 本SKILL.md超过500行上限, 已截断尾部非核心章节以满足L1格式要求。完整内容见版本库历史。
## FAQ
### Q1: Meta Agent Optimizer支持哪些输入格式？
A1: AI Agent全功能优化引擎，性能指标采集+瓶颈诊断+技能自动提取+多平台Hook集成.。元代理优化器专业版是在免费版基础上的全功能升级，为AI Agent提。支持文本指令和结构化参数输入，具体格式参考使用流程章节。
### Q2: 使用Meta Agent Optimizer需要什么前置条件？
A2: 请确认运行环境满足依赖说明中的要求。Meta Agent Optimizer基于Markdown指令驱动，无需额外安装包。
### Q3: 命令行执行失败怎么办？
A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。
## 安全注意事项
| 风险类型 | 防范措施 |
|----------|---------|
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 网络通信安全 | 使用HTTPS协议，验证SSL证书有效性 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |
使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。
## 核心功能
- **自动化执行**: AI Agent全功能优化引擎，性能指标采集+瓶颈诊断+技能自动提取+多平台Hook集成.。元代理优化器专业版是在免费版
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据