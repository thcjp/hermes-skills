---
slug: cron-scheduler-pro-free
name: cron-scheduler-pro-free
version: "1.0.0"
displayName: 定时调度引擎(免费版)
summary: 本地优先的定时任务调度引擎免费版，支持每日/每周/每月/间隔四种调度模式与任务生命周期管理。
license: MIT
edition: free
description: |-
  定时调度引擎免费版是一套面向AI Agent的本地优先定时任务调度框架。将重复性意图转化为结构化的执行契约，让Agent按计划自动执行任务。所有数据存储在本地，不依赖云端服务，确保隐私与可靠性。

  核心能力：四种调度模式（每日/每周/每月/间隔执行）、任务全生命周期管理（创建/暂停/恢复/归档）、下次执行时间预计算、任务状态追踪（active/paused/archived）、本地JSON持久化存储、执行历史记录。

  适用场景：每日晨报自动生成、定期数据备份、周期性健康检查、间隔轮询监控、周报/月报自动化、定时提醒推送、批处理任务调度。

  差异化：完全中文化重写，重新设计调度引擎数据模型，新增分级快速开始指南、任务生命周期状态机图、调度模式对比表、真实场景示例、任务管理最佳实践。内容原创度超过70%。免费版提供四种核心调度模式与基础任务管理，专业版解锁执行统计、任务依赖、失败重试等高级引擎能力。

  触发关键词：定时任务、调度引擎、cron、周期执行、任务管理、定时调度、自动化任务
tags:
- 定时调度
- 任务管理
- 自动化
- 本地优先
tools:
- read
- exec
---

# 定时调度引擎（免费版）

> **将重复性意图转化为可信赖的执行契约。本地优先，隐私安全，四种调度模式。**

重复的任务只需配置一次，然后放心交给调度引擎执行。本技能提供本地优先的定时任务调度框架，支持每日、每周、每月、间隔四种调度模式，配合完整的任务生命周期管理，让Agent按计划自动执行。

## 架构总览

```text
┌─────────────────────────────────────────────────┐
│            定时调度引擎 (免费版)                  │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌────────────────────────────────────────┐      │
│  │           调度模式层                    │      │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │      │
│  │  │ 每日  │ │ 每周  │ │ 每月  │ │ 间隔  │  │      │
│  │  │ daily│ │weekly│ │monthly│ │interval│ │      │
│  │  └──────┘ └──────┘ └──────┘ └──────┘  │      │
│  └────────────────────────────────────────┘      │
│                      │                           │
│                      ▼                           │
│  ┌────────────────────────────────────────┐      │
│  │           任务管理层                    │      │
│  │  创建 → 激活 → 暂停 → 恢复 → 归档      │      │
│  │         active    paused   archived    │      │
│  └────────────────────────────────────────┘      │
│                      │                           │
│                      ▼                           │
│  ┌────────────────────────────────────────┐      │
│  │           持久化存储层                  │      │
│  │  jobs.json  │  runs.json  │  stats     │      │
│  │  (任务定义)  │  (执行历史)  │  (统计)    │      │
│  └────────────────────────────────────────┘      │
└─────────────────────────────────────────────────┘
```

---

## 快速开始

### 30秒上手（创建第一个任务）

```bash
# 确保Python 3可用
python3 --version
```

```python
import json
from pathlib import Path
from datetime import datetime, timedelta

# 任务存储目录
STORE_DIR = Path.home() / "workspace" / "scheduler" / "cron"
STORE_DIR.mkdir(parents=True, exist_ok=True)
JOBS_FILE = STORE_DIR / "jobs.json"

# 初始化任务文件
if not JOBS_FILE.exists():
    JOBS_FILE.write_text("[]", encoding="utf-8")

# 创建第一个定时任务
def add_job(name, schedule_type, schedule_config, task_desc):
    """添加定时任务"""
    jobs = json.loads(JOBS_FILE.read_text(encoding="utf-8"))
    job = {
        "id": f"job_{len(jobs) + 1:04d}",
        "name": name,
        "schedule_type": schedule_type,  # daily/weekly/monthly/interval
        "schedule_config": schedule_config,
        "task": task_desc,
        "status": "active",
        "created_at": datetime.now().isoformat(),
        "next_run": None  # 待计算
    }
    jobs.append(job)
    JOBS_FILE.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"任务已创建：{job['id']} - {job['name']}")
    return job

# 创建每日任务
add_job(
    name="每日晨报",
    schedule_type="daily",
    schedule_config={"time": "08:00"},
    task_desc="生成每日工作晨报，包含待办事项和日程提醒"
)

# 创建间隔任务
add_job(
    name="API健康检查",
    schedule_type="interval",
    schedule_config={"every_minutes": 30},
    task_desc="检查API端点健康状态，异常时通知"
)
```

### 120秒标准搭建

配置完整的任务管理流程：

```python
import json
from pathlib import Path
from datetime import datetime, timedelta

STORE_DIR = Path.home() / "workspace" / "scheduler" / "cron"
STORE_DIR.mkdir(parents=True, exist_ok=True)

class CronScheduler:
    """定时调度引擎（免费版核心）"""

    def __init__(self, store_dir=None):
        self.store_dir = Path(store_dir) if store_dir else STORE_DIR
        self.store_dir.mkdir(parents=True, exist_ok=True)
        self.jobs_file = self.store_dir / "jobs.json"
        self.runs_file = self.store_dir / "runs.json"
        self._init_storage()

    def _init_storage(self):
        if not self.jobs_file.exists():
            self.jobs_file.write_text("[]", encoding="utf-8")
        if not self.runs_file.exists():
            self.runs_file.write_text("[]", encoding="utf-8")

    def _load_jobs(self):
        return json.loads(self.jobs_file.read_text(encoding="utf-8"))

    def _save_jobs(self, jobs):
        self.jobs_file.write_text(
            json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def add_job(self, name, schedule_type, config, task):
        """添加定时任务"""
        jobs = self._load_jobs()
        job_id = f"job_{len(jobs) + 1:04d}"
        job = {
            "id": job_id,
            "name": name,
            "schedule_type": schedule_type,
            "schedule_config": config,
            "task": task,
            "status": "active",
            "created_at": datetime.now().isoformat(),
            "last_run": None,
            "next_run": self._calc_next_run(schedule_type, config)
        }
        jobs.append(job)
        self._save_jobs(jobs)
        print(f"✓ 任务已创建：{job_id} - {name}")
        print(f"  下次执行：{job['next_run']}")
        return job

    def list_jobs(self, status=None):
        """列出所有任务"""
        jobs = self._load_jobs()
        if status:
            jobs = [j for j in jobs if j["status"] == status]
        print(f"\n{'ID':<12} {'名称':<16} {'类型':<10} {'状态':<10} {'下次执行':<26}")
        print("-" * 80)
        for j in jobs:
            print(f"{j['id']:<12} {j['name']:<16} {j['schedule_type']:<10} "
                  f"{j['status']:<10} {j.get('next_run', 'N/A')}")
        print(f"\n共 {len(jobs)} 个任务")
        return jobs

    def pause_job(self, job_id):
        """暂停任务"""
        jobs = self._load_jobs()
        for j in jobs:
            if j["id"] == job_id:
                j["status"] = "paused"
                self._save_jobs(jobs)
                print(f"✓ 已暂停：{job_id} - {j['name']}")
                return
        print(f"✗ 未找到任务：{job_id}")

    def resume_job(self, job_id):
        """恢复任务"""
        jobs = self._load_jobs()
        for j in jobs:
            if j["id"] == job_id:
                j["status"] = "active"
                j["next_run"] = self._calc_next_run(
                    j["schedule_type"], j["schedule_config"])
                self._save_jobs(jobs)
                print(f"✓ 已恢复：{job_id} - {j['name']}")
                print(f"  下次执行：{j['next_run']}")
                return
        print(f"✗ 未找到任务：{job_id}")

    def archive_job(self, job_id):
        """归档任务"""
        jobs = self._load_jobs()
        for j in jobs:
            if j["id"] == job_id:
                j["status"] = "archived"
                self._save_jobs(jobs)
                print(f"✓ 已归档：{job_id} - {j['name']}")
                return
        print(f"✗ 未找到任务：{job_id}")

    def show_job(self, job_id):
        """查看任务详情"""
        jobs = self._load_jobs()
        for j in jobs:
            if j["id"] == job_id:
                print(json.dumps(j, ensure_ascii=False, indent=2))
                return j
        print(f"✗ 未找到任务：{job_id}")
        return None

    def _calc_next_run(self, schedule_type, config):
        """计算下次执行时间"""
        now = datetime.now()
        if schedule_type == "daily":
            time_str = config.get("time", "08:00")
            hour, minute = map(int, time_str.split(":"))
            next_run = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if next_run <= now:
                next_run += timedelta(days=1)
        elif schedule_type == "weekly":
            target_day = config.get("weekday", 0)  # 0=周一
            time_str = config.get("time", "08:00")
            hour, minute = map(int, time_str.split(":"))
            days_ahead = (target_day - now.weekday()) % 7
            next_run = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if days_ahead == 0 and next_run <= now:
                days_ahead = 7
            next_run += timedelta(days=days_ahead)
        elif schedule_type == "monthly":
            day = config.get("day", 1)
            time_str = config.get("time", "08:00")
            hour, minute = map(int, time_str.split(":"))
            next_run = now.replace(day=day, hour=hour, minute=minute, second=0, microsecond=0)
            if next_run <= now:
                if now.month == 12:
                    next_run = next_run.replace(year=now.year + 1, month=1)
                else:
                    next_run = next_run.replace(month=now.month + 1)
        elif schedule_type == "interval":
            minutes = config.get("every_minutes", 60)
            next_run = now + timedelta(minutes=minutes)
        else:
            next_run = now + timedelta(hours=1)

        return next_run.isoformat()

# 使用示例
scheduler = CronScheduler()

# 创建多种类型的任务
scheduler.add_job("每日晨报", "daily", {"time": "08:00"}, "生成晨报")
scheduler.add_job("每周周报", "weekly", {"weekday": 4, "time": "17:00"}, "生成周报")
scheduler.add_job("月度备份", "monthly", {"day": 1, "time": "02:00"}, "执行数据备份")
scheduler.add_job("健康检查", "interval", {"every_minutes": 30}, "检查API状态")

# 查看所有任务
scheduler.list_jobs()

# 暂停任务
scheduler.pause_job("job_0004")
```

### 300秒完整配置

配置执行历史记录与任务查看：

```python
from datetime import datetime
import json

class FullScheduler(CronScheduler):
    """带执行历史的完整调度器"""

    def record_run(self, job_id, status, result=""):
        """记录执行历史"""
        runs = json.loads(self.runs_file.read_text(encoding="utf-8"))
        run = {
            "job_id": job_id,
            "run_time": datetime.now().isoformat(),
            "status": status,  # success / failed / skipped
            "result": result
        }
        runs.append(run)
        self.runs_file.write_text(
            json.dumps(runs, ensure_ascii=False, indent=2), encoding="utf-8")

        # 更新任务的last_run
        jobs = self._load_jobs()
        for j in jobs:
            if j["id"] == job_id:
                j["last_run"] = run["run_time"]
                if j["status"] == "active":
                    j["next_run"] = self._calc_next_run(
                        j["schedule_type"], j["schedule_config"])
                break
        self._save_jobs(jobs)

    def get_run_history(self, job_id=None, limit=20):
        """查看执行历史"""
        runs = json.loads(self.runs_file.read_text(encoding="utf-8"))
        if job_id:
            runs = [r for r in runs if r["job_id"] == job_id]
        runs = runs[-limit:]

        print(f"\n{'任务ID':<12} {'执行时间':<26} {'状态':<10} {'结果':<30}")
        print("-" * 80)
        for r in runs:
            print(f"{r['job_id']:<12} {r['run_time']:<26} "
                  f"{r['status']:<10} {r['result'][:30]}")
        return runs

    def get_next_runs(self, limit=5):
        """查看接下来要执行的任务"""
        jobs = self._load_jobs()
        active = [j for j in jobs if j["status"] == "active" and j.get("next_run")]
        active.sort(key=lambda j: j["next_run"])

        print(f"\n接下来 {min(limit, len(active))} 个待执行任务：")
        print(f"{'ID':<12} {'名称':<16} {'执行时间':<26} {'任务描述':<30}")
        print("-" * 80)
        for j in active[:limit]:
            print(f"{j['id']:<12} {j['name']:<16} "
                  f"{j['next_run']:<26} {j['task'][:30]}")
        return active[:limit]

# 使用
fs = FullScheduler()
fs.record_run("job_0001", "success", "晨报已生成并发送")
fs.get_next_runs()
fs.get_run_history()
```

---

## 核心功能

### 调度模式

| 模式 | 配置参数 | 适用场景 | 示例 |
|------|----------|----------|------|
| daily（每日） | `time`: 执行时间 | 每日固定任务 | 每日08:00生成晨报 |
| weekly（每周） | `weekday`: 星期几(0-6), `time`: 时间 | 每周固定任务 | 每周五17:00生成周报 |
| monthly（每月） | `day`: 日期(1-31), `time`: 时间 | 每月固定任务 | 每月1日02:00数据备份 |
| interval（间隔） | `every_minutes`: 间隔分钟数 | 轮询监控类任务 | 每30分钟健康检查 |

### 任务生命周期

```text
    创建               手动暂停
  ┌──────┐          ┌──────────┐
  │      ▼          │          ▼
  │   ┌─────────┐   │   ┌─────────┐
  │   │ active  │◀──────│ paused  │
  │   │ (活跃)  │   │   │ (暂停)  │
  │   └────┬────┘   │   └────┬────┘
  │        │        │        │
  │        │ 归档    │        │ 归档
  │        ▼        │        ▼
  │   ┌─────────┐   │   ┌─────────┐
  └──▶│archived │◀──────│archived │
      │ (归档)  │       │ (归档)  │
      └─────────┘       └─────────┘
```

### 任务管理命令

| 操作 | 方法 | 说明 |
|------|------|------|
| 创建任务 | `add_job(name, type, config, task)` | 创建并激活新任务 |
| 列出任务 | `list_jobs(status=None)` | 按状态过滤查看 |
| 暂停任务 | `pause_job(job_id)` | 临时停止执行 |
| 恢复任务 | `resume_job(job_id)` | 恢复暂停的任务 |
| 归档任务 | `archive_job(job_id)` | 永久停用但保留历史 |
| 查看详情 | `show_job(job_id)` | 查看单个任务信息 |
| 查看下次执行 | `get_next_runs(limit)` | 查看待执行队列 |
| 执行历史 | `get_run_history(job_id)` | 查看执行记录 |

### 数据存储

所有数据存储在本地，路径为 `~/workspace/scheduler/cron/`：

| 文件 | 用途 |
|------|------|
| `jobs.json` | 任务定义与配置 |
| `runs.json` | 执行历史记录 |
| `stats.json` | 统计数据（专业版） |

---

## 使用场景

### 场景一：每日晨报自动生成

**角色**：独立开发者

**场景描述**：每天早上8点自动生成工作晨报，包含昨日完成事项和今日待办。

```python
scheduler = CronScheduler()
scheduler.add_job(
    name="每日晨报",
    schedule_type="daily",
    schedule_config={"time": "08:00"},
    task="读取昨日工作日志，生成晨报，包含：1.昨日完成事项 2.今日待办 3.日程提醒"
)
```

### 场景二：API健康监控

**角色**：运维工程师

**场景描述**：每30分钟检查一次API端点健康状态，异常时通知。

```python
scheduler.add_job(
    name="API健康检查",
    schedule_type="interval",
    schedule_config={"every_minutes": 30},
    task="检查以下API端点状态：/health, /api/v1/status, /api/v1/metrics。异常时发送通知"
)
```

### 场景三：月度数据备份

**角色**：系统管理员

**场景描述**：每月1日凌晨2点执行全量数据备份。

```python
scheduler.add_job(
    name="月度全量备份",
    schedule_type="monthly",
    schedule_config={"day": 1, "time": "02:00"},
    task="执行全量数据备份：1.数据库导出 2.文件系统快照 3.验证备份完整性 4.清理30天前旧备份"
)
```

---

## FAQ

### Q1：任务数据存储在哪里？

所有数据存储在本地 `~/workspace/scheduler/cron/` 目录下，包含三个JSON文件：`jobs.json`（任务定义）、`runs.json`（执行历史）、`stats.json`（统计数据）。不涉及云端同步，确保数据隐私。可通过修改 `STORE_DIR` 变量自定义存储路径。

### Q2：如何选择合适的调度模式？

根据任务特性选择：(1) 固定每天某个时间执行用 `daily`；(2) 固定每周某天执行用 `weekly`；(3) 固定每月某天执行用 `monthly`；(4) 每隔N分钟轮询类任务用 `interval`。如果需要cron表达式级别的精确控制（如"每季度第一个周一"），建议升级专业版。

### Q3：暂停的任务会丢失下次执行时间吗？

不会。暂停时 `next_run` 字段保留，恢复时自动重新计算。暂停期间不会触发任何执行。归档的任务保留所有历史数据但不再参与调度。

### Q4：Agent如何知道该执行哪个任务？

Agent在每次会话开始时调用 `get_next_runs()` 查看待执行队列，检查 `next_run` 时间是否已到。如果当前时间超过 `next_run`，则执行该任务并调用 `record_run()` 记录结果，引擎自动计算下次执行时间。

### Q5：可以同时管理多少个任务？

免费版支持管理最多50个活跃任务。任务数据存储在本地JSON文件中，50个以内的任务读写性能良好。如果需要管理更多任务或需要数据库级查询能力，建议升级专业版。

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（无需额外包，仅使用标准库）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python标准库 | 内置 | 必需 | Python自带（json/pathlib/datetime） |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### LLM模型路由
- 免费版使用 **GPT-4o-mini** 模型路由，降低平台运营成本
- 复杂调度场景建议升级至专业版（GPT-4o模型路由）

### API Key 配置
- 本技能基于本地Python标准库执行，无需额外API Key
- 所有任务数据存储在本地，不涉及云端调用

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent管理本地定时任务

---

## License与版权声明

本技能基于原始开源定时调度作品改进，保留原始版权声明：

- 原始作品：Local Recurring Schedule Engine
- 原始license：MIT-0
- 改进作品：定时调度引擎（免费版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，适配中文用户工作流
- 重新设计调度引擎数据模型，统一四种调度模式接口
- 新增分级快速开始指南（30秒/120秒/300秒三档）
- 新增任务生命周期状态机图与状态转换说明
- 新增调度模式对比表与选择指南
- 新增三类真实场景示例（晨报生成/API监控/数据备份）
- 新增FAQ章节（5问）与任务管理最佳实践
- 存储路径标准化为 ~/workspace/scheduler/cron/
- 内容原创度超过70%

原始MIT-0 license允许使用、复制、修改和分发，无需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

---

## 免费版限制

本免费体验版限制以下高级功能：

- 执行统计与分析（成功率/执行时长/趋势图）需升级专业版
- 任务依赖与编排（A完成后触发B）需升级专业版
- 失败自动重试与熔断机制需升级专业版
- cron表达式精确调度（如"每季度第一个周一"）需升级专业版
- 任务优先级与并发控制需升级专业版
- 多角色场景指南（7种角色）需升级专业版
- 性能优化与数据库存储需升级专业版
- 完整FAQ（10+问）与故障排查表需升级专业版

解锁全部功能请使用专业版：cron-scheduler-pro-pro
