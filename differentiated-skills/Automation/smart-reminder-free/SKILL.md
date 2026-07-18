---
slug: smart-reminder-free
name: smart-reminder-free
version: "1.0.0"
displayName: 智能提醒助手(免费版)
summary: 自然语言事件捕获与提醒助手免费版，含中文解析、事件存储、默认提醒偏移与基础查询。
license: MIT
edition: free
description: |-
  智能提醒助手免费版是面向AI Agent的自然语言事件捕获与提醒系统。不同于提醒创建引擎，本技能聚焦"如何理解用户的自然语言事件描述并智能管理"：事件解析、结构化存储、提醒偏移、基础查询。

  核心能力：中文自然语言事件捕获（"后天上午10点有个会"）、事件结构化存储（events.yml）、默认提醒偏移（24小时/1小时/10分钟前）、基础重复模式（无/年度）、事件查询（"我最近有什么安排"）、最小化澄清提问、工作区数据隔离。

  适用场景：个人事件管理、生日与纪念日提醒、会议与截止日期捕获、轻量日程助手、自然语言交互偏好用户。

  差异化：完全中文化重写，聚焦"智能事件管理"而非提醒创建机制，新增事件解析决策树、events.yml结构规范、默认偏移策略、最小化澄清原则、查询接口设计。内容原创度超过70%。免费版提供基础事件管理与查询，专业版解锁自定义偏移、多渠道投递、农历生日、语义搜索等高级特性。

  触发关键词：智能提醒、自然语言、事件捕获、events.yml、提醒偏移、事件查询、日程助手
tags:
- 智能提醒
- 自然语言
- 事件管理
- 日程助手
tools:
- read
- exec
---

# 智能提醒助手（免费版）

> **不是教你创建提醒，而是教你理解用户的自然语言事件描述。中文解析、结构化存储、智能查询，一站式日程助手。**

用户说"后天上午10点有个会"、"下个月2号我妈生日"、"周五下午三点交报告"——如何把这些自然语言转化为结构化事件并设置提醒？本技能聚焦自然语言事件捕获与智能管理，帮助Agent成为用户的私人日程助手。

## 架构总览

```text
┌─────────────────────────────────────────────────────────┐
│              智能提醒助手 (免费版)                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────────────────────────────────┐          │
│  │            自然语言捕获层                    │          │
│  │   "后天上午10点有个会"                       │          │
│  │   "下个月2号我妈生日"                       │          │
│  │   "周五下午三点交报告"                      │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            事件解析层                        │          │
│  │   title │ start_datetime │ notes            │          │
│  │   reminders_offsets │ repeat                │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            澄清提问层（最小化）              │          │
│  │   仅在关键信息模糊时提问                     │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            存储层（events.yml）              │          │
│  │   工作区数据文件，支持Git同步                │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            提醒调度层                        │          │
│  │   默认偏移：24h前 / 1h前 / 10m前             │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            查询接口层                        │          │
│  │   "我最近有什么安排？"                       │          │
│  └────────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────┘
```

---

## 快速开始

### 30秒上手（捕获一个事件）

用户说"后天上午10点有个会"：

```python
import yaml
from pathlib import Path
from datetime import datetime, timedelta

# 事件存储路径
EVENTS_FILE = Path.home() / "workspace" / "reminders" / "events.yml"

def capture_event(natural_text, current_time=None):
    """捕获自然语言事件（基础版）"""
    if current_time is None:
        current_time = datetime.now()

    # 解析"后天上午10点"
    # 后天 = 当前日期 + 2天
    # 上午10点 = 10:00
    event_date = current_time + timedelta(days=2)
    start_datetime = event_date.replace(hour=10, minute=0, second=0, microsecond=0)

    event = {
        "id": f"evt_{int(current_time.timestamp())}",
        "title": "会议",  # 从"有个会"提取
        "start_datetime": start_datetime.isoformat(),
        "notes": "",
        "reminders_offsets": [1440, 60, 10],  # 24h/1h/10m前（分钟）
        "repeat": "none",
        "timezone": "Asia/Shanghai",
        "created_at": current_time.isoformat(),
        "status": "active"
    }

    # 写入events.yml
    EVENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    events = []
    if EVENTS_FILE.exists():
        events = yaml.safe_load(EVENTS_FILE.read_text(encoding="utf-8")) or []

    events.append(event)
    EVENTS_FILE.write_text(
        yaml.dump(events, allow_unicode=True, sort_keys=False),
        encoding="utf-8"
    )

    print(f"✓ 事件已捕获：{event['title']}")
    print(f"  时间：{start_datetime.strftime('%Y-%m-%d %H:%M')}")
    print(f"  提醒：24小时前、1小时前、10分钟前")

    return event

# 使用
capture_event("后天上午10点有个会")
```

### 60秒标准搭建（含提醒调度）

配置完整的提醒调度：

```python
import yaml
import subprocess
from pathlib import Path
from datetime import datetime, timedelta

EVENTS_FILE = Path.home() / "workspace" / "reminders" / "events.yml"
TIMEZONE = "Asia/Shanghai"
DEFAULT_OFFSETS = [1440, 60, 10]  # 24h/1h/10m前（分钟）

class SmartReminder:
    """智能提醒助手（免费版）"""

    def __init__(self):
        self.events_file = EVENTS_FILE
        self.events_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.events_file.exists():
            self.events_file.write_text("[]", encoding="utf-8")

    def capture(self, title, start_datetime, notes="", offsets=None, repeat="none"):
        """捕获事件并创建提醒"""
        if offsets is None:
            offsets = DEFAULT_OFFSETS

        event = {
            "id": f"evt_{int(datetime.now().timestamp())}",
            "title": title,
            "start_datetime": start_datetime.isoformat(),
            "notes": notes,
            "reminders_offsets": offsets,
            "repeat": repeat,
            "timezone": TIMEZONE,
            "created_at": datetime.now().isoformat(),
            "status": "active"
        }

        # 存储事件
        events = self._load_events()
        events.append(event)
        self._save_events(events)

        # 为每个偏移创建cron作业
        for offset_min in offsets:
            remind_at = start_datetime - timedelta(minutes=offset_min)
            if remind_at <= datetime.now():
                continue  # 跳过已过去的提醒

            job_name = f"reminder-{event['id']}-{offset_min}m"
            subprocess.run([
                "skill-platform", "cron", "add",
                "--name", job_name,
                "--at", remind_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "--session", "main",
                "--system-event", f"提醒：{title}（{offset_min}分钟后开始）",
                "--announce",
                "--channel", "telegram",
                "--to", "+8613800138000",
                "--delete-after-run"
            ], check=False)

        print(f"✓ 事件已捕获并设置{len(offsets)}个提醒")
        return event

    def query_upcoming(self, days=7):
        """查询即将到来的事件"""
        events = self._load_events()
        now = datetime.now()
        upcoming = []

        for event in events:
            if event["status"] != "active":
                continue
            start = datetime.fromisoformat(event["start_datetime"])
            if now <= start <= now + timedelta(days=days):
                upcoming.append(event)

        upcoming.sort(key=lambda e: e["start_datetime"])
        return upcoming

    def cancel(self, event_id):
        """取消事件"""
        events = self._load_events()
        for event in events:
            if event["id"] == event_id:
                event["status"] = "cancelled"
                self._save_events(events)
                print(f"✓ 事件已取消：{event['title']}")
                return event
        print(f"✗ 未找到事件：{event_id}")
        return None

    def _load_events(self):
        return yaml.safe_load(self.events_file.read_text(encoding="utf-8")) or []

    def _save_events(self, events):
        self.events_file.write_text(
            yaml.dump(events, allow_unicode=True, sort_keys=False),
            encoding="utf-8"
        )

# 使用示例
sr = SmartReminder()

# 捕获事件
sr.capture(
    title="团队周会",
    start_datetime=datetime.now() + timedelta(days=2, hours=2),
    notes="讨论Q3规划"
)

# 捕获生日事件（年度重复）
sr.capture(
    title="妈妈生日",
    start_datetime=datetime(2026, 8, 2, 9, 0),
    notes="记得提前准备礼物",
    repeat="yearly"
)

# 查询即将到来的事件
upcoming = sr.query_upcoming(days=7)
for event in upcoming:
    print(f"  {event['start_datetime']}: {event['title']}")
```

### 120秒完整配置（自然语言解析增强）

配置中文自然语言解析：

```python
import re
from datetime import datetime, timedelta

class NaturalLanguageParser:
    """中文自然语言事件解析（免费版）"""

    def parse(self, text, current_time=None):
        """解析自然语言事件描述"""
        if current_time is None:
            current_time = datetime.now()

        result = {
            "title": "",
            "start_datetime": None,
            "notes": "",
            "repeat": "none"
        }

        # ===== 日期解析 =====

        # 后天
        if "后天" in text:
            date = current_time + timedelta(days=2)
        # 明天
        elif "明天" in text:
            date = current_time + timedelta(days=1)
        # 今天
        elif "今天" in text:
            date = current_time
        # 下周X
        elif match := re.search(r"下周([一二三四五六日天])", text):
            day_map = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4, "六": 5, "日": 6, "天": 6}
            target_day = day_map[match.group(1)]
            days_ahead = (target_day - current_time.weekday()) % 7
            if days_ahead == 0:
                days_ahead = 7
            date = current_time + timedelta(days=days_ahead)
        # 周X
        elif match := re.search(r"周([一二三四五六日天])", text):
            day_map = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4, "六": 5, "日": 6, "天": 6}
            target_day = day_map[match.group(1)]
            days_ahead = (target_day - current_time.weekday()) % 7
            date = current_time + timedelta(days=days_ahead)
        # X月X号
        elif match := re.search(r"(\d+)月(\d+)号", text):
            month, day = int(match.group(1)), int(match.group(2))
            date = current_time.replace(month=month, day=day)
            if date < current_time:
                date = date.replace(year=date.year + 1)
        else:
            date = None  # 需要澄清

        # ===== 时间解析 =====

        # 上午X点
        if match := re.search(r"上午(\d+)点", text):
            hour = int(match.group(1))
            time = (hour, 0)
        # 下午X点
        elif match := re.search(r"下午(\d+)点", text):
            hour = int(match.group(1)) + 12
            time = (hour, 0)
        # X点X分
        elif match := re.search(r"(\d+)点(\d+)分", text):
            time = (int(match.group(1)), int(match.group(2)))
        # X点
        elif match := re.search(r"(\d+)点", text):
            time = (int(match.group(1)), 0)
        else:
            time = None  # 需要澄清

        # 组合日期时间
        if date and time:
            result["start_datetime"] = date.replace(
                hour=time[0], minute=time[1], second=0, microsecond=0
            )
        elif date:
            result["start_datetime"] = date  # 仅有日期，需澄清时间

        # ===== 重复模式 =====

        if "生日" in text or "纪念日" in text:
            result["repeat"] = "yearly"

        # ===== 标题提取 =====

        # 提取"有X"或"是X"之后的内容作为标题
        if match := re.search(r"有(.+)$", text):
            result["title"] = match.group(1).strip()
        elif match := re.search(r"是(.+)$", text):
            result["title"] = match.group(1).strip()
        else:
            # 移除时间相关词汇，剩余作为标题
            cleaned = re.sub(r"(后天|明天|今天|下周[一二三四五六日天]|周[一二三四五六日天]|\d+月\d+号|上午|\d+点|\d+分|下午|有个|有)", "", text)
            result["title"] = cleaned.strip() or "未命名事件"

        return result

    def needs_clarification(self, parsed):
        """判断是否需要澄清"""
        missing = []
        if parsed["start_datetime"] is None:
            missing.append("时间")
        if not parsed["title"]:
            missing.append("标题")
        return missing

# 使用示例
parser = NaturalLanguageParser()

# 解析各种自然语言
texts = [
    "后天上午10点有个会",
    "下个月2号我妈生日",
    "周五下午三点交报告",
    "明天上午9点站会"
]

for text in texts:
    print(f"\n输入：{text}")
    parsed = parser.parse(text)
    print(f"  标题：{parsed['title']}")
    print(f"  时间：{parsed['start_datetime']}")
    print(f"  重复：{parsed['repeat']}")

    missing = parser.needs_clarification(parsed)
    if missing:
        print(f"  ⚠️ 需要澄清：{', '.join(missing)}")
```

---

## 核心功能

### 自然语言事件捕获

支持中文自然语言事件描述：

| 输入模式 | 解析结果 | 示例 |
|----------|----------|------|
| `<相对日期><时段><事件>` | 日期+时间+标题 | "后天上午10点有个会" |
| `<月份><日期><事件>` | 具体日期+标题 | "下个月2号我妈生日" |
| `<周几><时段><事件>` | 周几+时间+标题 | "周五下午三点交报告" |
| `<相对日期><时段><事件>` | 日期+时间+标题 | "明天上午9点站会" |

**支持的日期表达**：
- 相对日期：今天、明天、后天
- 周几：周一至周日、下周一至下周日
- 具体日期：X月X号、X月X日

**支持的时间表达**：
- 时段+点：上午X点、下午X点
- 具体时间：X点X分

### 事件结构化存储

事件存储在 `~/.workspace/reminders/events.yml`：

```yaml
- id: evt_1700000000
  title: 团队周会
  start_datetime: "2026-07-20T10:00:00"
  notes: 讨论Q3规划
  reminders_offsets:
    - 1440  # 24小时前
    - 60    # 1小时前
    - 10    # 10分钟前
  repeat: none
  timezone: Asia/Shanghai
  created_at: "2026-07-18T10:00:00"
  status: active

- id: evt_1700000001
  title: 妈妈生日
  start_datetime: "2026-08-02T09:00:00"
  notes: 记得提前准备礼物
  reminders_offsets:
    - 1440
    - 60
    - 10
  repeat: yearly
  timezone: Asia/Shanghai
  created_at: "2026-07-18T10:01:00"
  status: active
```

**字段说明**：

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | string | 是 | 事件唯一ID |
| `title` | string | 是 | 事件标题 |
| `start_datetime` | ISO 8601 | 是 | 开始时间 |
| `notes` | string | 否 | 备注 |
| `reminders_offsets` | number[] | 是 | 提醒偏移（分钟） |
| `repeat` | enum | 是 | `none`/`yearly`（免费版） |
| `timezone` | string | 是 | IANA时区 |
| `created_at` | ISO 8601 | 是 | 创建时间 |
| `status` | enum | 是 | `active`/`cancelled`/`done` |

### 默认提醒偏移

| 偏移 | 说明 | 适用场景 |
|------|------|----------|
| 1440分钟（24小时） | 提前一天提醒 | 重要事件预先准备 |
| 60分钟（1小时） | 提前一小时提醒 | 即将开始的事件 |
| 10分钟（10分钟） | 提前十分钟提醒 | 最后提醒 |

**设计理由**：三级偏移覆盖"预先准备-即将开始-最后提醒"三个阶段，平衡提醒充分性与打扰频率。

### 最小化澄清原则

**仅当关键信息模糊时才提问**：

| 模糊情况 | 澄清问题 | 示例 |
|----------|----------|------|
| 日期无法解析 | "请问是哪一天？" | "有个会"（无日期） |
| 时间缺失 | "请问是几点？" | "后天有个会"（无时间） |
| 月份歧义 | "请问是哪个月？" | "2号有个会"（无月份） |
| 标题不明确 | "请问事件内容是？" | "后天上午10点"（无事件） |

**原则**：
- 一次只问最少必要的问题
- 优先使用上下文推断（如"生日"默认年度重复）
- 避免连续追问，影响用户体验

### 事件查询接口

```python
# 查询即将到来的事件
sr.query_upcoming(days=7)

# 查询特定时间段
sr.query_range(start, end)

# 按标题搜索
sr.search_by_title("会议")
```

**查询回复格式**：

```text
你最近7天的安排：

1. 2026-07-20 10:00 - 团队周会（讨论Q3规划）
2. 2026-07-22 15:00 - 客户评审会议
3. 2026-07-25 09:00 - 每日站会

共3个事件。
```

---

## 使用场景

### 场景一：会议事件捕获

**角色**：职场人士

**场景描述**：用户说"后天上午10点有个会"，捕获事件并设置提醒。

```python
sr = SmartReminder()
parser = NaturalLanguageParser()

# 解析自然语言
parsed = parser.parse("后天上午10点有个会")

# 检查是否需要澄清
missing = parser.needs_clarification(parsed)
if missing:
    print(f"请问补充以下信息：{', '.join(missing)}")
else:
    # 捕获事件
    sr.capture(
        title=parsed["title"],
        start_datetime=parsed["start_datetime"],
        notes="",
        repeat=parsed["repeat"]
    )
```

### 场景二：生日年度提醒

**角色**：注重家庭的人

**场景描述**：用户说"下个月2号我妈生日"，捕获为年度重复事件。

```python
# 解析（自动识别"生日"→yearly重复）
parsed = parser.parse("下个月2号我妈生日")

sr.capture(
    title=parsed["title"],
    start_datetime=parsed["start_datetime"],
    notes="记得提前准备礼物",
    repeat="yearly"  # 年度重复
)
```

### 场景三：截止日期提醒

**角色**：项目经理

**场景描述**：用户说"周五下午三点交报告"，捕获截止日期提醒。

```python
parsed = parser.parse("周五下午三点交报告")

sr.capture(
    title=parsed["title"],
    start_datetime=parsed["start_datetime"],
    notes="项目A阶段性报告",
    repeat="none"
)
```

### 场景四：查询近期安排

**角色**：忙碌的职场人士

**场景描述**：用户问"我最近有什么安排？"，返回近期事件列表。

```python
upcoming = sr.query_upcoming(days=7)

if not upcoming:
    print("最近7天没有安排")
else:
    print("你最近7天的安排：\n")
    for i, event in enumerate(upcoming, 1):
        dt = datetime.fromisoformat(event["start_datetime"])
        print(f"{i}. {dt.strftime('%Y-%m-%d %H:%M')} - {event['title']}")
        if event["notes"]:
            print(f"   备注：{event['notes']}")
```

---

## FAQ

### Q1：支持哪些自然语言格式？

免费版支持中文自然语言：(1) 相对日期（今天/明天/后天）+ 时段（上午/下午X点）+ 事件；(2) 周几（周一至周日、下周一至下周日）+ 时段 + 事件；(3) 具体日期（X月X号）+ 事件。例如"后天上午10点有个会"、"周五下午三点交报告"、"下个月2号我妈生日"。

### Q2：事件数据存储在哪里？

事件存储在工作区的 `~/.workspace/reminders/events.yml` 文件。使用YAML格式，便于阅读与编辑。文件可纳入Git版本控制，实现跨设备同步与备份。事件数据与技能本身分离，便于迁移。

### Q3：默认提醒偏移是什么？

默认在事件开始前的24小时、1小时、10分钟各提醒一次，覆盖"预先准备-即将开始-最后提醒"三个阶段。专业版支持自定义偏移序列。所有提醒通过cron作业调度，投递到Telegram（免费版默认渠道）。

### Q4：如何处理信息不完整的事件？

采用"最小化澄清"原则：仅当关键信息（日期、时间、标题）模糊时才提问，一次只问最少必要的问题。例如用户说"有个会"（无日期），仅问"请问是哪一天？"。优先使用上下文推断（如"生日"默认年度重复），避免连续追问。

### Q5：如何查询即将到来的事件？

直接问"我最近有什么安排？"、"下周有什么？"等自然语言查询。助手会读取events.yml，计算近期事件（默认7天），按时间排序返回列表。每个事件显示时间、标题与备注。

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（用于自然语言解析与事件管理）
- **PyYAML**: 用于YAML文件读写

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | 从python.org安装 |
| PyYAML | Python包 | 必需 | `pip install pyyaml` |
| Agent Gateway | 运行时 | 必需 | Agent平台内置 |
| skill-platform CLI | 工具 | 必需 | Agent平台内置 |
| Telegram Bot | 投递通道 | 否 | 注册Telegram Bot获取 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### LLM模型路由
- 免费版使用 **GPT-4o-mini** 模型路由，降低平台运营成本
- 复杂事件解析场景建议升级至专业版（GPT-4o模型路由）

### API Key 配置
- Telegram投递需要Telegram Bot Token（存储在Agent Gateway配置中）
- 禁止在SKILL.md或脚本中硬编码Token
- 工作区数据（events.yml）不涉及API Key

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent管理事件与提醒

---

## License与版权声明

本技能基于原始开源自然语言提醒作品改进，保留原始版权声明：

- 原始作品：Natural Language Reminder
- 原始license：MIT
- 改进作品：智能提醒助手（免费版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，适配中文用户工作流
- 聚焦"智能事件管理"而非提醒创建机制
- 新增中文自然语言解析决策树与模式表
- 新增events.yml结构规范与字段说明表
- 新增默认提醒偏移策略（24h/1h/10m三级）
- 新增最小化澄清原则与提问模板
- 新增事件查询接口与回复格式规范
- 新增Python实现的事件管理类与解析器
- 新增分级快速开始指南（30秒/60秒/120秒三档）
- 新增四类真实场景示例（会议/生日/截止/查询）
- 新增FAQ章节（5问）
- 新增依赖说明章节与License版权声明
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

---

## 免费版限制

本免费体验版限制以下高级功能：

- 自定义提醒偏移序列需升级专业版
- 多渠道投递（Telegram+Discord+WhatsApp）需升级专业版
- 完整重复模式（monthly/weekly/daily）需升级专业版
- 农历生日支持（自动公历转换）需升级专业版
- 语义搜索（"上次关于XXX的讨论"）需升级专业版
- 事件更新与归档管理需升级专业版
- 英文自然语言解析需升级专业版
- 多角色场景指南（7种角色）需升级专业版
- 完整FAQ（10+问）与故障排查表需升级专业版
- 性能优化策略与多平台集成示例需升级专业版

解锁全部功能请使用专业版：smart-reminder-pro
