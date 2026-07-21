# 详细参考 - smart-reminder-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import re
from datetime import datetime, timedelta

class AdvancedNaturalLanguageParser:
    """高级自然语言解析器（中英文，专业版）"""

    CN_NUM = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
              "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
              "十一": 11, "十二": 12}

    def parse(self, text, current_time=None):
        """解析中英文自然语言事件描述"""
        if current_time is None:
            current_time = datetime.now()

        text = text.strip()

        if re.search(r"[\u4e00-\u9fa5]", text):
            return self._parse_chinese(text, current_time)
        else:
            return self._parse_english(text, current_time)

    def _parse_chinese(self, text, current_time):
        """解析中文"""
        result = {"title": "", "start_datetime": None, "notes": "", "repeat": "none", "lunar": None}

        if "农历" in text or "阴历" in text:
            if match := re.search(r"农历(\d+)月(\d+)", text):
                result["lunar"] = (int(match.group(1)), int(match.group(2)))
                result["repeat"] = "yearly"

        date = None

        if "后天" in text:
            date = current_time + timedelta(days=2)
        elif "明天" in text:
            date = current_time + timedelta(days=1)
        elif "今天" in text:
            date = current_time
        elif match := re.search(r"下周([一二三四五六日天])", text):
            day_map = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4, "六": 5, "日": 6, "天": 6}
            target_day = day_map[match.group(1)]
            days_ahead = (target_day - current_time.weekday()) % 7
            if days_ahead == 0:
                days_ahead = 7
            date = current_time + timedelta(days=days_ahead)
        elif match := re.search(r"周([一二三四五六日天])", text):
            day_map = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4, "六": 5, "日": 6, "天": 6}
            target_day = day_map[match.group(1)]
            days_ahead = (target_day - current_time.weekday()) % 7
            date = current_time + timedelta(days=days_ahead)
        elif match := re.search(r"(\d+)月(\d+)号", text):
            month, day = int(match.group(1)), int(match.group(2))
            date = current_time.replace(month=month, day=day)
            if date < current_time:
                date = date.replace(year=date.year + 1)
        elif match := re.search(r"下个月(\d+)号", text):
            day = int(match.group(1))
            next_month = current_time.month + 1 if current_time.month < 12 else 1
            next_year = current_time.year if current_time.month < 12 else current_time.year + 1
            date = current_time.replace(year=next_year, month=next_month, day=day)

        time = None

        if match := re.search(r"上午(\d+)点", text):
            time = (int(match.group(1)), 0)
        elif match := re.search(r"下午(\d+)点", text):
            time = (int(match.group(1)) + 12, 0)
        elif match := re.search(r"(\d+)点(\d+)分", text):
            time = (int(match.group(1)), int(match.group(2)))
        elif match := re.search(r"(\d+)点", text):
            time = (int(match.group(1)), 0)

        if date and time:
            result["start_datetime"] = date.replace(
                hour=time[0], minute=time[1], second=0, microsecond=0
            )
        elif date:
            result["start_datetime"] = date

        if "生日" in text or "纪念日" in text:
            result["repeat"] = "yearly"
        elif "每周" in text:
            result["repeat"] = "weekly"
        elif "每月" in text:
            result["repeat"] = "monthly"
        elif "每天" in text or "每日" in text:
            result["repeat"] = "daily"

        if match := re.search(r"有(.+)$", text):
            result["title"] = match.group(1).strip()
        elif match := re.search(r"是(.+)$", text):
            result["title"] = match.group(1).strip()
        else:
            cleaned = re.sub(
                r"(后天|明天|今天|下周[一二三四五六日天]|周[一二三四五六日天]|\d+月\d+号|下个月\d+号|上午|\d+点|\d+分|下午|农历|阴历|有个|有|是|生日|每周|每月|每天|每日)",
                "", text
            )
            result["title"] = cleaned.strip() or "未命名事件"

        return result

    def _parse_english(self, text, current_time):
        """解析英文"""
        result = {"title": "", "start_datetime": None, "notes": "", "repeat": "none", "lunar": None}

        text_lower = text.lower()

        date = None

        if "tomorrow" in text_lower:
            date = current_time + timedelta(days=1)
        elif "today" in text_lower:
            date = current_time
        elif "next monday" in text_lower:
            date = self._next_weekday(current_time, 0)
        elif "next tuesday" in text_lower:
            date = self._next_weekday(current_time, 1)
        elif "next wednesday" in text_lower:
            date = self._next_weekday(current_time, 2)
        elif "next thursday" in text_lower:
            date = self._next_weekday(current_time, 3)
        elif "next friday" in text_lower:
            date = self._next_weekday(current_time, 4)
        elif "next saturday" in text_lower:
            date = self._next_weekday(current_time, 5)
        elif "next sunday" in text_lower:
            date = self._next_weekday(current_time, 6)
        elif match := re.search(r"(\d+)/(\d+)", text):
            month, day = int(match.group(1)), int(match.group(2))
            date = current_time.replace(month=month, day=day)
            if date < current_time:
                date = date.replace(year=date.year + 1)

        time = None

        if match := re.search(r"(\d+)\s*(?:am|a\.m\.)", text_lower):
            time = (int(match.group(1)), 0)
        elif match := re.search(r"(\d+)\s*(?:pm|p\.m\.)", text_lower):
            time = (int(match.group(1)) + 12, 0)
        elif match := re.search(r"(\d+):(\d+)", text):
            time = (int(match.group(1)), int(match.group(2)))
        elif match := re.search(r"at\s+(\d+)", text_lower):
            time = (int(match.group(1)), 0)

        if date and time:
            result["start_datetime"] = date.replace(
                hour=time[0], minute=time[1], second=0, microsecond=0
            )
        elif date:
            result["start_datetime"] = date

        if "birthday" in text_lower or "anniversary" in text_lower:
            result["repeat"] = "yearly"
        elif "weekly" in text_lower or "every week" in text_lower:
            result["repeat"] = "weekly"
        elif "monthly" in text_lower or "every month" in text_lower:
            result["repeat"] = "monthly"
        elif "daily" in text_lower or "every day" in text_lower:
            result["repeat"] = "daily"

        cleaned = re.sub(
            r"(tomorrow|today|next\s+\w+|\d+/\d+|at\s+\d+|am|pm|a\.m\.|p\.m\.|:\d+|birthday|anniversary|weekly|monthly|daily|every\s+\w+)",
            "", text, flags=re.IGNORECASE
        )
        result["title"] = cleaned.strip() or "Untitled Event"

        return result

    def _next_weekday(self, current_time, target_day):
        """计算下一个目标星期几"""
        days_ahead = (target_day - current_time.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return current_time + timedelta(days=days_ahead)

parser = AdvancedNaturalLanguageParser()

zh_texts = [
    "后天上午10点有个会",
    "下个月2号我妈生日",
    "周五下午三点交报告",
    "我妈农历六月二十生日",
    "每周一上午9点站会"
]

print("=== 中文解析 ===")
for text in zh_texts:
    parsed = parser.parse(text)
    print(f"\n输入：{text}")
    print(f"  标题：{parsed['title']}")
    print(f"  时间：{parsed['start_datetime']}")
    print(f"  重复：{parsed['repeat']}")
    if parsed['lunar']:
        print(f"  农历：{parsed['lunar']}")

en_texts = [
    "meeting tomorrow at 2pm",
    "team standup next monday at 9am",
    "mom birthday next month 15th",
    "weekly review every friday at 3pm"
]

print("\n=== 英文解析 ===")
for text in en_texts:
    parsed = parser.parse(text)
    print(f"\nInput: {text}")
    print(f"  Title: {parsed['title']}")
    print(f"  Time: {parsed['start_datetime']}")
    print(f"  Repeat: {parsed['repeat']}")
```

## 代码示例 (python)

```python
import yaml
import subprocess
from pathlib import Path
from datetime import datetime, timedelta

EVENTS_FILE = Path.home() / "workspace" / "reminders" / "events.yml"
TIMEZONE = "Asia/Shanghai"

class SmartReminderPro:
    """智能提醒助手（专业版）"""

    def __init__(self):
        self.events_file = EVENTS_FILE
        self.events_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.events_file.exists():
            self.events_file.write_text("[]", encoding="utf-8")

    def capture(self, title, start_datetime, notes="", offsets=None,
                repeat="none", channels=None, lunar_date=None):
        """捕获事件并创建多渠道提醒"""
        if offsets is None:
            offsets = [1440, 60, 10]  # 默认24h/1h/10m
        if channels is None:
            channels = [{"channel": "telegram", "to": "+8613800138000"}]

        event = {
            "id": f"evt_{int(datetime.now().timestamp())}",
            "title": title,
            "start_datetime": start_datetime.isoformat() if isinstance(start_datetime, datetime) else start_datetime,
            "notes": notes,
            "reminders_offsets": offsets,
            "repeat": repeat,
            "channels": channels,
            "timezone": TIMEZONE,
            "created_at": datetime.now().isoformat(),
            "status": "active"
        }

        if lunar_date:
            event["lunar_date"] = lunar_date

        events = self._load_events()
        events.append(event)
        self._save_events(events)

        for offset_min in offsets:
            if isinstance(start_datetime, str):
                remind_at = datetime.fromisoformat(start_datetime) - timedelta(minutes=offset_min)
            else:
                remind_at = start_datetime - timedelta(minutes=offset_min)

            if remind_at <= datetime.now():
                continue

            for ch in channels:
                job_name = f"reminder-{event['id']}-{offset_min}m-{ch['channel']}"
                cmd = [
                    "skill-platform", "cron", "add",
                    "--name", job_name,
                    "--at", remind_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "--session", "main",
                    "--system-event", f"提醒：{title}（{offset_min}分钟后开始）",
                    "--announce",
                    "--channel", ch["channel"],
                    "--to", ch["to"],
                    "--delete-after-run"
                ]
                subprocess.run(cmd, check=False)

        print(f"✓ 事件已捕获：{len(offsets)}个偏移 × {len(channels)}个渠道")
        return event

    def update(self, event_id, **kwargs):
        """更新事件"""
        events = self._load_events()
        for event in events:
            if event["id"] == event_id:
                for key, value in kwargs.items():
                    if key in event:
                        event[key] = value
                event["updated_at"] = datetime.now().isoformat()
                self._save_events(events)
                print(f"✓ 事件已更新：{event_id}")
                return event
        print(f"✗ 未找到事件：{event_id}")
        return None

    def cancel(self, event_id):
        """取消事件"""
        return self.update(event_id, status="cancelled")

    def pause(self, event_id):
        """暂停事件提醒"""
        return self.update(event_id, status="paused")

    def resume(self, event_id):
        """恢复事件提醒"""
        return self.update(event_id, status="active")

    def archive(self, event_id):
        """归档事件"""
        return self.update(event_id, status="archived")

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

    def semantic_search(self, query):
        """语义搜索事件（专业版）"""
        events = self._load_events()
        results = []

        query_lower = query.lower()
        keywords = self._extract_keywords(query)

        for event in events:
            score = 0
            title = event["title"].lower()
            notes = event.get("notes", "").lower()

            for kw in keywords:
                if kw in title:
                    score += 3
                if kw in notes:
                    score += 2

            if query_lower in title or query_lower in notes:
                score += 5

            if score > 0:
                event_copy = event.copy()
                event_copy["relevance_score"] = score
                results.append(event_copy)

        results.sort(key=lambda e: e["relevance_score"], reverse=True)
        return results

    def _extract_keywords(self, query):
        """提取搜索关键词"""
        import re
        stop_words = {"的", "了", "是", "在", "有", "和", "与", "或", "上", "下", "中"}
        words = re.findall(r"[\u4e00-\u9fa5]+|[a-zA-Z]+", query)
        return [w for w in words if w not in stop_words and len(w) > 1]

    def _load_events(self):
        return yaml.safe_load(self.events_file.read_text(encoding="utf-8")) or []

    def _save_events(self, events):
        self.events_file.write_text(
            yaml.dump(events, allow_unicode=True, sort_keys=False),
            encoding="utf-8"
        )

sr = SmartReminderPro()

sr.capture(
    title="产品评审会议",
    start_datetime=datetime.now() + timedelta(days=2, hours=2),
    notes="讨论Q3产品规划",
    offsets=[2880, 1440, 60, 10],  # 2天/1天/1小时/10分钟
    channels=[
        {"channel": "telegram", "to": "+8613800138000"},
        {"channel": "discord", "to": "channel:1476104553148452958"}
    ]
)

results = sr.semantic_search("上次关于产品规划的讨论")
for r in results:
    print(f"  [{r['relevance_score']}] {r['start_datetime']}: {r['title']}")
```

## 代码示例 (python)

```python
from lunardate import LunarDate
from datetime import datetime, timedelta
import yaml
from pathlib import Path

EVENTS_FILE = Path.home() / "workspace" / "reminders" / "events.yml"

def capture_lunar_birthday(lunar_month, lunar_day, title, notes=""):
    """捕获农历生日事件（专业版）"""
    current_year = datetime.now().year

    lunar_date = LunarDate(current_year, lunar_month, lunar_day)
    solar_date = lunar_date.toSolarDate()

    if solar_date < datetime.now().date():
        lunar_date = LunarDate(current_year + 1, lunar_month, lunar_day)
        solar_date = lunar_date.toSolarDate()

    event = {
        "id": f"evt_{int(datetime.now().timestamp())}",
        "title": title,
        "start_datetime": datetime.combine(solar_date, datetime.min.time()).isoformat(),
        "notes": notes,
        "reminders_offsets": [1440, 60, 10],  # 24h/1h/10m
        "repeat": "yearly",
        "lunar_date": f"{lunar_month:02d}-{lunar_day:02d}",  # 存储原始农历
        "timezone": "Asia/Shanghai",
        "created_at": datetime.now().isoformat(),
        "status": "active"
    }

    EVENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    events = []
    if EVENTS_FILE.exists():
        events = yaml.safe_load(EVENTS_FILE.read_text(encoding="utf-8")) or []
    events.append(event)
    EVENTS_FILE.write_text(
        yaml.dump(events, allow_unicode=True, sort_keys=False),
        encoding="utf-8"
    )

    print(f"✓ 农历生日已捕获：{title}")
    print(f"  农历：{lunar_month}月{lunar_day}日")
    print(f"  公历：{solar_date.strftime('%Y-%m-%d')}")
    print(f"  重复：每年")

    return event

capture_lunar_birthday(6, 20, "妈妈生日", "记得提前准备礼物")
```

## 代码示例 (text)

```text
┌──────────────────────────────────────────────────────────────┐
│                 智能提醒助手 (专业版)                           │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────┐          │
│  │            自然语言捕获层（中英文）              │          │
│  │   中文：后天上午10点有个会                        │          │
│  │   英文：meeting next Monday at 2pm               │          │
│  └─────────────────────────────────────────────────┘          │
│                              │                                │
│                              ▼                                │
│  ┌─────────────────────────────────────────────────┐          │
│  │            事件解析层（增强版）                  │          │
│  │   title │ start_datetime │ notes                │          │
│  │   reminders_offsets │ repeat │ lunar_date        │          │
│  └─────────────────────────────────────────────────┘          │
│                              │                                │
│                              ▼                                │
│  ┌─────────────────────────────────────────────────┐          │
│  │            农历转换层（专业版）                  │          │
│  │   农历日期 → 公历日期（自动处理闰月）            │          │
│  └─────────────────────────────────────────────────┘          │
│                              │                                │
│                              ▼                                │
│  ┌─────────────────────────────────────────────────┐          │
│  │            存储层（events.yml）                  │          │
│  │   工作区数据文件，支持Git同步                    │          │
│  └─────────────────────────────────────────────────┘          │
│                              │                                │
│                              ▼                                │
│  ┌─────────────────────────────────────────────────┐          │
│  │            多渠道投递层（专业版）                │          │
│  │   Telegram │ Discord │ WhatsApp │ 同时投递       │          │
│  └─────────────────────────────────────────────────┘          │
│                              │                                │
│                              ▼                                │
│  ┌─────────────────────────────────────────────────┐          │
│  │            生命周期管理层（专业版）              │          │
│  │   创建/更新/取消/暂停/恢复/归档/查询             │          │
│  └─────────────────────────────────────────────────┘          │
│                              │                                │
│                              ▼                                │
│  ┌─────────────────────────────────────────────────┐          │
│  │            语义搜索层（专业版）                  │          │
│  │   "上次关于XXX的讨论" → 关键词+语义匹配          │          │
│  └─────────────────────────────────────────────────┘          │
└──────────────────────────────────────────────────────────────┘
```

## 代码示例 (python)

```python
sr.capture(
    title="每日站会",
    start_datetime=next_weekday(datetime.now(), 0).replace(hour=9, minute=30),
    offsets=[10],
    repeat="daily",
    channels=[{"channel": "discord", "to": "channel:team"}]
)

sr.capture(
    title="周报提交",
    start_datetime=next_weekday(datetime.now(), 4).replace(hour=17, minute=0),
    offsets=[60, 10],
    repeat="weekly",
    channels=[{"channel": "discord", "to": "channel:team"}]
)

sr.capture(
    title="月度总结",
    start_datetime=datetime.now().replace(day=1, hour=10, minute=0),
    offsets=[1440, 60],
    repeat="monthly",
    channels=[{"channel": "discord", "to": "channel:team"}]
)
```

## 代码示例 (python)

```python
parser.parse("后天上午10点有个会")
parser.parse("meeting next Monday at 2pm")
texts = [
    "明天上午9点站会",
    "team lunch tomorrow at 12pm",
    "下个月2号我妈生日",
    "project review next friday at 3pm"
]

for text in texts:
    parsed = parser.parse(text)
    sr.capture(
        title=parsed["title"],
        start_datetime=parsed["start_datetime"],
        repeat=parsed["repeat"],
        lunar_date=f"{parsed['lunar'][0]:02d}-{parsed['lunar'][1]:02d}" if parsed.get("lunar") else None
    )
```

## 代码示例 (python)

```python
from lunardate import LunarDate

def lunar_to_solar(lunar_month, lunar_day, year=None):
    """农历转公历（自动处理闰月）"""
    if year is None:
        year = datetime.now().year

    try:
        lunar_date = LunarDate(year, lunar_month, lunar_day)
        solar_date = lunar_date.toSolarDate()
        return solar_date
    except ValueError:
        print(f"警告：{year}年农历{lunar_month}月{lunar_day}日不存在（可能涉及闰月）")
        return None
```

## 代码示例 (python)

```python
def update_lunar_events():
    """每年更新农历事件的公历日期"""
    events = sr._load_events()
    current_year = datetime.now().year

    for event in events:
        if event.get("lunar_date") and event["repeat"] == "yearly":
            month, day = map(int, event["lunar_date"].split("-"))
            solar_date = lunar_to_solar(month, day, current_year)
            if solar_date:
                event["start_datetime"] = solar_date.isoformat()
                event["updated_at"] = datetime.now().isoformat()

    sr._save_events(events)
```

## 代码示例 (python)

```python
sr.capture(title="会议", start_datetime=...)

sr.update(event_id, title="新标题", notes="新备注")

sr.pause(event_id)
sr.resume(event_id)

sr.cancel(event_id)

sr.archive(event_id)

sr.query_upcoming(days=7)

sr.semantic_search("关键词")
```

### 300秒完整配置（中英文自然语言解析）
配置完整的中英文自然语言解析器：

```python
import re
from datetime import datetime, timedelta

class AdvancedNaturalLanguageParser:
    """高级自然语言解析器（中英文，专业版）"""

    CN_NUM = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
              "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
              "十一": 11, "十二": 12}

    def parse(self, text, current_time=None):
        """解析中英文自然语言事件描述"""
        if current_time is None:
            current_time = datetime.now()

        text = text.strip()

        if re.search(r"[\u4e00-\u9fa5]", text):
            return self._parse_chinese(text, current_time)
        else:
            return self._parse_english(text, current_time)

    def _parse_chinese(self, text, current_time):
        """解析中文"""
        result = {"title": "", "start_datetime": None, "notes": "", "repeat": "none", "lunar": None}

        if "农历" in text or "阴历" in text:
            if match := re.search(r"农历(\d+)月(\d+)", text):
                result["lunar"] = (int(match.group(1)), int(match.group(2)))
                result["repeat"] = "yearly"

        date = None

        if "后天" in text:
            date = current_time + timedelta(days=2)
        elif "明天" in text:
            date = current_time + timedelta(days=1)
        elif "今天" in text:
            date = current_time
        elif match := re.search(r"下周([一二三四五六日天])", text):
            day_map = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4, "六": 5, "日": 6, "天": 6}
            target_day = day_map[match.group(1)]
            days_ahead = (target_day - current_time.weekday()) % 7
            if days_ahead == 0:
                days_ahead = 7
            date = current_time + timedelta(days=days_ahead)
        elif match := re.search(r"周([一二三四五六日天])", text):
            day_map = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4, "六": 5, "日": 6, "天": 6}
            target_day = day_map[match.group(1)]
            days_ahead = (target_day - current_time.weekday()) % 7
            date = current_time + timedelta(days=days_ahead)
        elif match := re.search(r"(\d+)月(\d+)号", text):
            month, day = int(match.group(1)), int(match.group(2))
            date = current_time.replace(month=month, day=day)
            if date < current_time:
                date = date.replace(year=date.year + 1)
        elif match := re.search(r"下个月(\d+)号", text):
            day = int(match.group(1))
            next_month = current_time.month + 1 if current_time.month < 12 else 1
            next_year = current_time.year if current_time.month < 12 else current_time.year + 1
            date = current_time.replace(year=next_year, month=next_month, day=day)

        time = None

        if match := re.search(r"上午(\d+)点", text):
            time = (int(match.group(1)), 0)
        elif match := re.search(r"下午(\d+)点", text):
            time = (int(match.group(1)) + 12, 0)
        elif match := re.search(r"(\d+)点(\d+)分", text):
            time = (int(match.group(1)), int(match.group(2)))
        elif match := re.search(r"(\d+)点", text):
            time = (int(match.group(1)), 0)

        if date and time:
            result["start_datetime"] = date.replace(
                hour=time[0], minute=time[1], second=0, microsecond=0
            )
        elif date:
            result["start_datetime"] = date

        if "生日" in text or "纪念日" in text:
            result["repeat"] = "yearly"
        elif "每周" in text:
            result["repeat"] = "weekly"
        elif "每月" in text:
            result["repeat"] = "monthly"
        elif "每天" in text or "每日" in text:
            result["repeat"] = "daily"

        if match := re.search(r"有(.+)$", text):
            result["title"] = match.group(1).strip()
        elif match := re.search(r"是(.+)$", text):
            result["title"] = match.group(1).strip()
        else:
            cleaned = re.sub(
                r"(后天|明天|今天|下周[一二三四五六日天]|周[一二三四五六日天]|\d+月\d+号|下个月\d+号|上午|\d+点|\d+分|下午|农历|阴历|有个|有|是|生日|每周|每月|每天|每日)",
                "", text
            )
            result["title"] = cleaned.strip() or "未命名事件"

        return result

    def _parse_english(self, text, current_time):
        """解析英文"""
        result = {"title": "", "start_datetime": None, "notes": "", "repeat": "none", "lunar": None}

        text_lower = text.lower()

        date = None

        if "tomorrow" in text_lower:
            date = current_time + timedelta(days=1)
        elif "today" in text_lower:
            date = current_time
        elif "next monday" in text_lower:
            date = self._next_weekday(current_time, 0)
        elif "next tuesday" in text_lower:
            date = self._next_weekday(current_time, 1)
        elif "next wednesday" in text_lower:
            date = self._next_weekday(current_time, 2)
        elif "next thursday" in text_lower:
            date = self._next_weekday(current_time, 3)
        elif "next friday" in text_lower:
            date = self._next_weekday(current_time, 4)
        elif "next saturday" in text_lower:
            date = self._next_weekday(current_time, 5)
        elif "next sunday" in text_lower:
            date = self._next_weekday(current_time, 6)
        elif match := re.search(r"(\d+)/(\d+)", text):
            month, day = int(match.group(1)), int(match.group(2))
            date = current_time.replace(month=month, day=day)
            if date < current_time:
                date = date.replace(year=date.year + 1)

        time = None

        if match := re.search(r"(\d+)\s*(?:am|a\.m\.)", text_lower):
            time = (int(match.group(1)), 0)
        elif match := re.search(r"(\d+)\s*(?:pm|p\.m\.)", text_lower):
            time = (int(match.group(1)) + 12, 0)
        elif match := re.search(r"(\d+):(\d+)", text):
            time = (int(match.group(1)), int(match.group(2)))
        elif match := re.search(r"at\s+(\d+)", text_lower):
            time = (int(match.group(1)), 0)

        if date and time:
            result["start_datetime"] = date.replace(
                hour=time[0], minute=time[1], second=0, microsecond=0
            )
        elif date:
            result["start_datetime"] = date

        if "birthday" in text_lower or "anniversary" in text_lower:
            result["repeat"] = "yearly"
        elif "weekly" in text_lower or "every week" in text_lower:
            result["repeat"] = "weekly"
        elif "monthly" in text_lower or "every month" in text_lower:
            result["repeat"] = "monthly"
        elif "daily" in text_lower or "every day" in text_lower:
            result["repeat"] = "daily"

        cleaned = re.sub(
            r"(tomorrow|today|next\s+\w+|\d+/\d+|at\s+\d+|am|pm|a\.m\.|p\.m\.|:\d+|birthday|anniversary|weekly|monthly|daily|every\s+\w+)",
            "", text, flags=re.IGNORECASE
        )
        result["title"] = cleaned.strip() or "Untitled Event"

        return result

    def _next_weekday(self, current_time, target_day):
        """计算下一个目标星期几"""
        days_ahead = (target_day - current_time.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return current_time + timedelta(days=days_ahead)

parser = AdvancedNaturalLanguageParser()

zh_texts = [
    "后天上午10点有个会",
    "下个月2号我妈生日",
    "周五下午三点交报告",
    "我妈农历六月二十生日",
    "每周一上午9点站会"
]

print("=== 中文解析 ===")
for text in zh_texts:
    parsed = parser.parse(text)
    print(f"\n输入：{text}")
    print(f"  标题：{parsed['title']}")
    print(f"  时间：{parsed['start_datetime']}")
    print(f"  重复：{parsed['repeat']}")
    if parsed['lunar']:
        print(f"  农历：{parsed['lunar']}")

en_texts = [
    "meeting tomorrow at 2pm",
    "team standup next monday at 9am",
    "mom birthday next month 15th",
    "weekly review every friday at 3pm"
]

print("\n=== 英文解析 ===")
for text in en_texts:
    parsed = parser.parse(text)
    print(f"\nInput: {text}")
    print(f"  Title: {parsed['title']}")
    print(f"  Time: {parsed['start_datetime']}")
    print(f"  Repeat: {parsed['repeat']}")
```



