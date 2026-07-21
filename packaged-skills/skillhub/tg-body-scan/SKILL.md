---
slug: tg-body-scan
name: tg-body-scan
version: "1.0.0"
displayName: 体测扫描工具专业版
summary: 企业级 Telegram 体测测量平台，支持批量扫描、历史趋势、团队管理与高级分析报表。
license: Proprietary
edition: pro
description: |-
  面向健身工作室、运动队与健康管理团队的批量体测测量平台。
  核心能力: 批量视频扫描、历史趋势对比、团队数据管理、高级分析报表、数据导出、API 集成。
  适用场景: 健身工作室会员管理、运动队体测跟踪、企业健康项目、医疗康复监测。
  差异化: 专业版在免费版基础上新增批量处理与团队治理，兼容免费版提交接口与返回格式。
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
---
# 体测扫描工具专业版

## 核心能力

| 能力 | 免费版 | 专业版 |
| --- | :---: | :---: |
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
### 单次视频扫描

执行单次视频扫描操作,处理用户输入并返回结果。

**输入**: 用户提供单次视频扫描所需的参数和指令。

**输出**: 返回单次视频扫描的处理结果。
### 基础围度测量

执行基础围度测量操作,处理用户输入并返回结果。

**输入**: 用户提供基础围度测量所需的参数和指令。

**输出**: 返回基础围度测量的处理结果。
### 腰臀比汇总

执行腰臀比汇总操作,处理用户输入并返回结果。

**输入**: 用户提供腰臀比汇总所需的参数和指令。

**输出**: 返回腰臀比汇总的处理结果。


## 适用场景

### 场景一：健身工作室会员月度批量体测

工作室每月为全部会员集中进行体测，批量提交视频并统一生成报告。

```python
# batch_body_scan.py
import json
import time

members = [
    {"id": "M001", "name": "张三", "gender": "male",   "height": 178, "video": "https://cdn.example.com/m001.mp4", "phone": "iPhone 15 Pro"},
    {"id": "M002", "name": "李四", "gender": "female", "height": 165, "video": "https://cdn.example.com/m002.mp4", "phone": "iPhone 14"},
    {"id": "M003", "name": "王五", "gender": "male",   "height": 182, "video": "https://cdn.example.com/m003.mp4", "phone": "Pixel 8"},
]

scan_ids = []

# 第1步: 批量提交扫描
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

# 第2步: 批量轮询（并行轮询多个任务）
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

# 第3步: 汇总输出
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

print(f"📊 张三 历史趋势 ({len(history['scans'])} 次扫描)")
print(f"{'日期':<12} {'腰围':>8} {'臀围':>8} {'腰臀比':>8} {'变化':>8}")
print("-" * 50)

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

# 获取团队当月全部扫描结果
report = anthrovision_bridge_get_team_report(
    team_id="STUDIO_01",
    month="2026-07",
    include_trends=True
)

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

print(f"✅ 已导出 {len(report['members'])} 位会员数据至 studio_report_202607.csv")

# 生成摘要
summary = report["summary"]
print(f"\n📋 团队月度摘要:")
print(f"  总扫描次数: {summary['total_scans']}")
print(f"  平均腰臀比: {summary['avg_whr']:.2f}")
print(f"  腰围平均变化: {summary['avg_waist_delta']:+.1f} cm")
print(f"  达标率: {summary['healthy_ratio']:.0%}")
```

## 使用流程

1. 创建团队并添加成员。

```python
# 创建团队
team = anthrovision_bridge_create_team(name="星耀健身工作室", admin_id="admin_001")

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

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **通信渠道**：Telegram（需可访问 Telegram 服务）

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
| :------- | :----- | :--------- | :--------- |
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

## 案例展示

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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
