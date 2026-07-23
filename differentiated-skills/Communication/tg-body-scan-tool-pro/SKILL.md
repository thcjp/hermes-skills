---
slug: "tg-body-scan-tool-pro"
name: "tg-body-scan-tool-pro"
version: "1.0.0"
displayName: "体测扫描工具专业版"
summary: "企业级 Telegram 体测测量平台，支持批量扫描、历史趋势、团队管理与高级分析报表。"
license: "Proprietary"
edition: "pro"
description: |-
  面向健身工作室、运动队与健康管理团队的批量体测测量平台。
  核心能力: 批量视频扫描、历史趋势对比、团队数据管理、高级分析报表、数据导出、API 集成。
  适用场景: 健身工作室会员管理、运动队体测跟踪、企业健康项目、医疗康复监测。
  差异化: 专业版在免费版基础上新增批量处理与团队治理，兼容免费版提交接口与返回格式。
  适用关键词: 体测, 批量扫描, 趋势分析, 团队管理, telegram, 健康报表, body-scan, 专业
tags:
  - 体测扫描
  - 批量测量
  - 趋势分析
  - 团队管理
  - 健康报表
  - 企业级
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
---
# 体测扫描工具 专业版

## 概述

专业版体测扫描工具为健身工作室、运动队与企业健康项目提供批量体测测量与团队数据管理能力。在免费版单次扫描基础上，专业版新增批量视频提交、历史趋势对比、团队成员管理、高级分析报表与数据导出等功能，满足持续跟踪与团队治理需求。

专业版完全兼容免费版：相同的提交接口与返回格式，免费版用户升级后历史扫描记录可自动导入团队数据库，无需重新测量。

## 核心能力

| 能力 | 免费版 | 专业版 |
|---|---|---|
| 单次视频扫描 | 支持 | 支持 |
| 基础围度测量 | 支持 | 支持 |
| 腰臀比汇总 | 支持 | 支持 |
| 批量视频扫描 | - | 支持 |
| 历史趋势对比 | - | 支持 |
| 团队成员管理 | - | 支持 |
| 高级分析报表 | - | 支持 |
| 数据导出（CSV/JSON） | - | 支持 |
| API 集成 | - | 支持 |
| 优先处理队列 | - | 支持 |
| 自定义测量项 | - | 支持 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、Telegram、体测测量平台、支持批量扫描、历史趋势、团队管理与高级分、析报表、面向健身工作室、运动队与健康管理、团队的批量体测测、量平台、核心能力、批量视频扫描、历史趋势对比、团队数据管理、高级分析报表、数据导出、API、适用场景、健身工作室会员管、运动队体测跟踪、企业健康项目、医疗康复监测、差异化、专业版在免费版基、础上新增批量处理、与团队治理、兼容免费版提交接、口与返回格式、适用关键词、批量扫描、趋势分析、团队管理、健康报表、body、scan等。

## 使用场景

### 场景一：健身工作室会员月度批量体测

工作室每月为全部会员集中进行体测，批量提交视频并统一生成报告。

```python
# batch_body_scan.py
import json
import time
# ...
members = [
    {"id": "M001", "name": "张三", "gender": "male",   "height": 178, "video": "https://cdn.example.com/m001.mp4", "phone": "iPhone 15 Pro"},
    {"id": "M002", "name": "李四", "gender": "female", "height": 165, "video": "https://cdn.example.com/m002.mp4", "phone": "iPhone 14"},
    {"id": "M003", "name": "王五", "gender": "male",   "height": 182, "video": "https://cdn.example.com/m003.mp4", "phone": "Pixel 8"},
]
# ...
scan_ids = []
# ...
# 步骤1: 批量提交扫描
for m in members:
    result = anthrovision_bridge_submit_scan(
        gender=m["gender"],
        height_cm=m["height"],
        video_url=m["video"],
        phone_model=m["phone"],
        member_id=m["id"],          # 专业版独有: 关联会员ID
        team_id="STUDIO_01"          # 专业版独有: 关联团队
    )
    scan_ids.append({"member": m["name"], "scan_id": result["scan_id"]})
    print(f"已提交: {m['name']} -> {result['scan_id']}")
# ...
# 步骤2: 批量轮询（并行轮询多个任务）
pending = set(item["scan_id"] for item in scan_ids)
results = {}
while pending:
    for item in scan_ids:
        sid = item["scan_id"]
        if sid in results:
            continue
        r = anthrovision_bridge_check_scan(scan_id=sid)
        if r["status"] != "processing":
            results[sid] = r
            pending.discard(sid)
            print(f"完成: {item['member']} -> {r['status']}")
    if pending:
        time.sleep(12)
# ...
# 步骤3: 汇总输出
for item in scan_ids:
    r = results[item["scan_id"]]
    print(f"\n📊 {item['member']} 测量结果:")
    for k, v in r.get("measurements", {}).items():
        print(f"  {k}: {v} cm")
    print(f"  腰臀比: {r.get('waist_hip_ratio', 'N/A')}")
```

### 场景二：个人历史趋势对比

专业版自动存档每次扫描，支持按时间线查看围度变化趋势。

```python
# trend_analysis.py
# 查询某会员过去6个月的所有扫描记录
history = anthrovision_bridge_get_history(
    member_id="M001",
    start_date="2026-01-01",
    end_date="2026-07-18"
)
# ...
print(f"📊 张三 历史趋势 ({len(history['scans'])} 次扫描)")
print(f"{'日期':<12} {'腰围':>8} {'臀围':>8} {'腰臀比':>8} {'变化':>8}")
print("-" * 50)
# ...
prev_waist = None
for scan in history["scans"]:
    waist = scan["measurements"].get("waist", "N/A")
    hip = scan["measurements"].get("hip", "N/A")
    ratio = scan.get("waist_hip_ratio", "N/A")
    delta = f"{waist - prev_waist:+.1f}" if prev_waist and isinstance(waist, (int, float)) else "-"
    print(f"{scan['date']:<12} {waist:>8} {hip:>8} {ratio:>8} {delta:>8}")
    prev_waist = waist if isinstance(waist, (int, float)) else None
```

**趋势输出示例**

```text
📊 张三 历史趋势 (6 次扫描)
日期          腰围     臀围    腰臀比     变化
------------------------------------------------
2026-01-15     85.2     98.1     0.87        -
2026-02-15     83.8     97.5     0.86     -1.4
2026-03-15     82.1     96.8     0.85     -1.7
2026-04-15     81.0     96.3     0.84     -1.1
2026-05-15     79.8     95.9     0.83     -1.2
2026-06-15     78.9     95.5     0.83     -0.9
📈 腰围累计减少 6.3 cm，趋势良好
```

### 场景三：团队健康报表导出

为工作室生成月度团队健康报表，导出 CSV 供进一步分析。

```python
# export_report.py
import csv
# ...
# 获取团队当月全部扫描结果
report = anthrovision_bridge_get_team_report(
    team_id="STUDIO_01",
    month="2026-07",
    include_trends=True
)
# ...
# 导出 CSV
with open("studio_report_202607.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["会员ID", "姓名", "性别", "身高", "肩宽", "胸围", "腰围", "臀围", "腰臀比", "腰围月变化"])
    for row in report["members"]:
        m = row["latest_scan"]["measurements"]
        writer.writerow([
            row["member_id"], row["name"], row["gender"], row["height"],
            m.get("shoulder", ""), m.get("chest", ""), m.get("waist", ""), m.get("hip", ""),
            row["latest_scan"].get("waist_hip_ratio", ""),
            row.get("monthly_delta", {}).get("waist", "")
        ])
# ...
print(f"✅ 已导出 {len(report['members'])} 位会员数据至 studio_report_202607.csv")
# ...
# 生成摘要
summary = report["summary"]
print(f"\n📋 团队月度摘要:")
print(f"  总扫描次数: {summary['total_scans']}")
print(f"  平均腰臀比: {summary['avg_whr']:.2f}")
print(f"  腰围平均变化: {summary['avg_waist_delta']:+.1f} cm")
print(f"  达标率: {summary['healthy_ratio']:.0%}")
```

## 不适用场景

以下场景体测扫描工具专业版不适合处理：

- 实时流数据处理
- 小规模数据手动分析
- 非结构化文本情感分析

## 触发条件

需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于非本工具能力范围的需求。

## 快速开始

1. 创建团队并添加成员。

```python
# 创建团队
team = anthrovision_bridge_create_team(name="星耀健身工作室", admin_id="admin_001")
# ...
# 添加成员
anthrovision_bridge_add_member(team_id=team["team_id"], member_id="M001", name="张三")
anthrovision_bridge_add_member(team_id=team["team_id"], member_id="M002", name="李四")
```

2. 批量提交会员体测视频。

```python
anthrovision_bridge_submit_scan(
    gender="male", height_cm=178,
    video_url="https://cdn.example.com/m001.mp4",
    phone_model="iPhone 15 Pro",
    member_id="M001", team_id=team["team_id"]
)
```

3. 查看团队报表与趋势。

```python
report = anthrovision_bridge_get_team_report(team_id=team["team_id"], month="2026-07")
print(report["summary"])
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤。

## 示例

专业版配置支持团队管理与批量调度。

```json
{
  "team": {
    "team_id": "STUDIO_01",
    "name": "星耀健身工作室",
    "max_members": 200,
    "auto_archive": true,
    "archive_interval_days": 30
  },
  "scan": {
    "batch_concurrency": 5,
    "priority_queue": true,
    "custom_measurements": ["neck", "thigh", "calf"],
    "retention_months": 24
  },
  "export": {
    "formats": ["csv", "json", "xlsx"],
    "include_trends": true,
    "auto_export_day": 1
  },
  "notification": {
    "on_complete": true,
    "channel": "telegram",
    "target": "<管理员TelegramID>"
  }
}
```

## 最佳实践

- **批量限流**：批量提交时控制并发数（建议 5 个并行），避免后端服务过载。
- **优先级队列**：VIP 会员扫描设置高优先级，系统优先处理。
- **定期存档**：开启 `auto_archive`，每月自动归档历史数据，保持查询性能。
- **趋势基线**：每位会员首次扫描作为基线，后续测量自动与基线对比。
- **自定义测量项**：根据业务需求启用额外测量项（如颈围、大腿围、小腿围）。
- **数据导出**：每月初自动导出报表，便于经营分析与会员汇报。
- **隐私合规**：团队成员数据仅对授权管理员可见，遵守当地数据保护法规。
- **兼容免费版**：免费版用户升级后，将其手动记录的历史数据录入即可建立趋势基线。

## 常见问题

### Q1：专业版如何兼容免费版？

专业版与免费版使用相同的提交接口与返回格式。免费版用户升级后，手动记录的历史数据可批量录入团队数据库，后续扫描自动归档。

### Q2：批量扫描时如何管理并发？

通过 `scan.batch_concurrency` 配置并行任务数（默认 5）。专业版优先级队列确保高优先级任务先处理，低优先级任务排队等待。

### Q3：历史数据保留多久？

默认保留 24 个月（`scan.retention_months`）。可在配置中调整，建议至少保留 12 个月以支持年度趋势分析。

### Q4：支持哪些导出格式？

支持 CSV、JSON、XLSX 三种格式。可配置 `export.auto_export_day` 在每月指定日期自动导出。

### Q5：如何为不同会员设置不同测量项？

在 `scan.custom_measurements` 中配置全局自定义测量项。若需按会员个性化配置，在提交扫描时通过 `custom_measurements` 参数覆盖。

### Q6：团队成员数据安全如何保障？

- 数据传输全程加密（TLS）。
- 团队数据仅对授权管理员与对应会员可见。
- 支持数据脱敏导出（隐藏会员真实姓名，使用 ID 替代）。
- 满足 GDPR 等数据保护法规要求，支持数据删除请求。

### Q7：专业版扫描速度比免费版快吗？

专业版享有优先处理队列，在服务繁忙时段扫描任务优先调度，平均等待时间更短。

### Q8：可以集成到现有健身管理系统吗？

可以。专业版提供完整 API 接口，支持通过 HTTP 调用提交扫描、查询结果与导出报表，便于集成到现有会员管理或健康管理系统中。

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **通信渠道**：Telegram（需可访问 Telegram 服务）

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| AnthroVision 扫描服务（专业版） | API | 必需 | 体测扫描后端服务（专业版接入凭证） |
| Telegram Bot | 通信渠道 | 必需 | 通过 `@BotFather` 创建机器人 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Python | 运行时 | 推荐 | 批量脚本与报表导出需要，v3.9+ |
| 数据库 | 存储 | 推荐 | 团队数据持久化（可选，默认文件存储） |
| pandas | Python 库 | 可选 | `pip install pandas`，高级报表分析 |

### API Key 配置

- 在 Agent 配置中填入 AnthroVision 专业版扫描服务的接入凭证（与免费版凭证不同，需单独申请）。
- 团队管理员凭证配置在 `team.admin_id` 中。
- 建议使用环境变量管理敏感凭证。

```bash
# 环境变量示例
export BODYSCAN_PRO_API_KEY="your_pro_api_key"
export BODYSCAN_TEAM_ID="STUDIO_01"
export TG_BOT_TOKEN="your_telegram_bot_token"
```

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务。专业版在免费版基础上新增批量处理、团队管理与趋势分析，提交接口与返回格式向后兼容免费版。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "体测扫描工具专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "tg body scan pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
