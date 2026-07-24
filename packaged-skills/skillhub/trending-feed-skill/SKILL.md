---
slug: "trending-feed-skill"
name: "trending-feed-skill"
version: 1.0.1
displayName: "热榜订阅(专业版)"
summary: "全功能 GitHub Trending 订阅，含批量抓取、多级缓存、定时推送、自定义模板。"
license: "Proprietary"
edition: "pro"
description: |-
  全功能 GitHub Trending 订阅，含批量抓取、多级缓存、定时推送、自定义模板。核心能力：
  - 批量抓取多语言、多时间窗（daily/weekly/monthly）热榜
  - 多级缓存（内存 + 文件）与命中率统计
  - GitHub Token 认证，速率限制提升至 5000 次/小时
  - 定时抓取并自动推送到飞书、Discord、Telegram
  - 自定义输出模板与字段映射...
tags:
  - 集成工具
  - 数据聚合
  - 企业效率
  - 自动化
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
category: "Automation"
---
# 热榜订阅(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 热榜订阅(专业版)含批量抓取 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

| 能力 | 说明 | 免费版 | 专业版 |
|:-----|:-----|:-----|:-----|
| 页面抓取 | 抓取 GitHub Trending 页面 | 是 | 是 |
| 语言过滤 | 按编程语言筛选 | 是 | 是 |
| 批量抓取 | 多语言、多时间窗并集 | 否 | 是 |
| 多级缓存 | 内存 + 文件 + 命中率 | 否 | 是 |
| Token 认证 | 5000 次/小时 | 否 | 是 |
| 定时推送 | cron 调度 + IM 推送 | 否 | 是 |
| 自定义模板 | 字段映射 + Webhook | 否 | 是 |
| 增量对比 | 与上次结果差异 | 否 | 是 |
| 成本预估 | Token 用量与请求预算 | 否 | 是 |
### 页面抓取

针对页面抓取,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供页面抓取相关的配置参数、输入数据和处理选项.
**输出**: 返回页面抓取的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`页面抓取`的配置文档进行参数调优
### 语言过滤

针对语言过滤,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供语言过滤相关的配置参数、输入数据和处理选项.
**输出**: 返回语言过滤的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`语言过滤`的配置文档进行参数调优
### 批量抓取

针对批量抓取,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供批量抓取相关的配置参数、输入数据和处理选项.
**输出**: 返回批量抓取的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`批量抓取`的配置文档进行参数调优
#
## 适用场景

### 场景 1：企业技术情报订阅
技术战略团队每日 9 点自动抓取 Python、Rust、Go、TypeScript 四门语言的热榜，去重后推送到飞书群，作为每日技术晨会素材。专业版的多语言并集模式避免重复抓取，命中率统计显示缓存复用率.
### 场景 2：内容创作素材自动采集
技术自媒体设置每日定时任务，将热榜项目按"星标增长 > 500"过滤后，自动生成选题清单推送到 Notion 或飞书文档。自定义模板支持输出"项目名 + 描述 + 星标 + 选题建议"四字段结构.
### 场景 3：多语言生态长期监测
开源项目负责人持续关注 Rust 生态，每周抓取 weekly 热榜，与上周结果做增量对比，识别"新晋热榜"与"持续上榜"两类项目，输出趋势报告.
### 场景 4：招聘团队技术栈热度追踪
招聘团队按月抓取多语言热榜，统计各语言项目的平均星标与新增项目数，校准岗位 JD 中的技术栈要求权重.
## 使用流程

> 上手时间：< 60 秒。专业版支持配置文件一键启用全部能力.
### 步骤 1：批量抓取多语言

```bash
python3 ~/.skill-platform/workspace/skills/trending-feed/（请参考skill目录中的脚本文件） \
  --languages python,rust,go,typescript \
  --since weekly \
  --limit 20
```

### 步骤 2：启用缓存

```bash
export TRENDING_CACHE_ENABLED=true
export TRENDING_CACHE_DIR=~/.trending-cache
export TRENDING_CACHE_TTL=3600
python3 ~/.skill-platform/workspace/skills/trending-feed/（请参考skill目录中的脚本文件） python
```

### 步骤 3：Token 认证提升速率

```bash
export GITHUB_TOKEN=ghp_详情见说明详情见说明详情见说明详情见说明详情见说明详情见说明xx
python3 ~/.skill-platform/workspace/skills/trending-feed/（请参考skill目录中的脚本文件） --languages python,go
```

### 步骤 4：定时推送

```bash
# 每日 9 点抓取并推送到飞书
0 9 * * * python3 fetch_trending.py --languages python,rust --push feishu --webhook $FEISHU_WEBHOOK
```

### 步骤 5：自定义模板

```bash
python3 fetch_trending.py python \
  --template ""skill_result". "skill_result" (⭐"skill_result" | "skill_result") - skill 相关配置参数"
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | trending-feed-skill处理的内容输入 |,  |
| content | string | 否 | trending-feed-skill处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "skill 相关配置参数",
    result: "skill 相关配置参数",
    result: "skill 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|:---:|:---:|:---:|:---:|
| 返回空列表 | 网络不通 / 代理未配置 | 
| 403 速率限制 | 未配置 Token / Token 过期 | 配置 `GITHUB_TOKEN` 或刷新 | P1 |
| 部分语言失败 | 语言名拼写错误 | 使用小写、标准语言名 | P2 |
| 推送失败 | Webhook URL 失效 | 重新生成 Webhook 并更新配置 | P1 |
| 缓存不命中 | TTL 过期 / 参数不一致 | 调大 TTL，统一参数组合 | P3 |
| 增量对比无输出 | 首次运行无历史数据 | 第二次运行后生效 | P3 |
| 模板渲染异常 | 字段名错误 | 检查模板变量名拼写 | P2 |

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（用于运行抓取与调度脚本）
- **cron / 任务计划**：用于定时推送（Linux 用 cron，Windows 用任务计划程序）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| Python 标准库 | 运行时 | 必需 | Python 自带（urllib / json / re / sched） |
| requests | Python 包 | 推荐 | `pip install requests`，用于更稳定的 HTTP 请求 |
| PyYAML | Python 包 | 推荐 | `pip install pyyaml`，用于解析配置文件 |
| GitHub REST API | 外部 API | 必需 | 公开 API，Token 认证后 5000 次/小时 |
| 飞书 / Discord Webhook | 外部 API | 可选 | 各平台机器人配置中获取 Webhook URL |

### API Key 配置
- **GitHub Token**：存储于环境变量 `GITHUB_TOKEN`，建议通过系统密钥管理工具注入，禁止硬编码
- **IM Webhook**：存储于环境变量 `FEISHU_WEBHOOK`、`DISCORD_WEBHOOK`，由配置文件引用
- **禁止**：在 SKILL.md 或脚本中硬编码 Token 与 Webhook URL

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务，支持定时调度与多渠道推送

## 案例展示

### 完整配置文件

```yaml
# trending_config.yaml
languages: [python, rust, go, typescript]
since: weekly          # daily / weekly / monthly
limit: 20
cache:
  enabled: true
  dir: ~/.trending-cache
  ttl: 3600
auth:
  github_token: ${GITHUB_TOKEN}
push:
  enabled: true
  channels:
    - type: feishu
      webhook: ${FEISHU_WEBHOOK}
    - type: discord
      webhook: ${DISCORD_WEBHOOK}
template: ""skill_metadata". "skill_metadata" (⭐"skill_metadata" | "skill_metadata") - skill 相关配置参数"
dedup: true
incremental: true
```

### 时间窗参数

| 参数值 | 含义 | 适用场景 |
|---:|:---|---:|
| `daily` | 今日热榜 | 每日技术动态 |
| `weekly` | 本周热榜 | 周报素材 |
| `monthly` | 本月热榜 | 月度趋势分析 |

### 缓存配置

| 配置项 | 默认值 | 说明 |
|:------:|--------|:-------|
| `TRENDING_CACHE_ENABLED` | false | 是否启用缓存 |
| `TRENDING_CACHE_DIR` | ~/.trending-cache | 缓存目录 |
| `TRENDING_CACHE_TTL` | 3600 | 缓存有效期（秒） |

## 常见问题

### Q1：批量抓取时部分语言失败如何处理？

A：专业版采用"部分成功"策略，单语言失败不影响其他语言，失败语言会在结果中标记 `error` 字段。建议检查 `GITHUB_TOKEN` 是否有效，并降低并发数.
### Q2：缓存命中率低怎么办？

A：(1) 检查 TTL 是否过短；(2) 确认缓存目录可写；(3) 同一查询使用相同的参数组合（语言、时间窗、条数）才能命中缓存.
### Q3：定时推送失败如何重试？

A：专业版内置重试机制，默认重试 3 次，间隔 60 秒。可在配置文件中调整 `push.retry_count` 与 `push.retry_interval`.
### Q4：Token 认证后仍报 403？

A：(1) 确认 Token 未过期；(2) 检查 Token 权限是否包含 `public_repo`；(3) GitHub 企业版 Token 需额外配置 `GH_ENTERPRISE_URL`.
### Q5：如何对接非飞书/Discord 平台？

A：专业版支持自定义 Webhook，配置 `push.channels` 中 `type: custom`，提供 `webhook` 与 `payload_template` 即可对接任意支持 HTTP 的平台.
### Q6：增量对比如何识别"新晋"与"持续"项目？

A：`--incremental` 输出会标注 `status` 字段：`new`（新晋）、`persist`（持续）、`dropped`（掉出）。建议周报只关注 `new` 与 `dropped` 两类.
### Q7：成本预估如何计算？

A：专业版根据语言数、时间窗数、条数估算请求数，结合 GitHub API 配额计算 Token 消耗。`--budget` 超限时自动熔断并返回已获取的部分结果.
### Q8：多平台推送时顺序如何保证？

A：专业版按配置文件中 `channels` 顺序串行推送，单平台失败不阻塞后续平台。如需严格顺序，配置 `push.sequential: true`.
### Q9：如何回滚到上次的缓存结果？

A：使用 `--rollback` 参数，专业版会读取上一次成功的缓存结果输出。适用于 GitHub API 临时不可用的降级场景.
### Q10：专业版是否支持私有仓库 Trending？

A：GitHub 官方不提供私有仓库 Trending。专业版支持配置 `--repo-list` 自定义仓库列表，结合 Token 抓取私有仓库的星标与活跃度作为替代指标.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

