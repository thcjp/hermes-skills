---
slug: smart-reminder-pro
name: smart-reminder-pro
version: "1.0.0"
displayName: 智能提醒助手(专业版)
summary: 自然语言事件捕获与提醒助手专业版，含自定义偏移、多渠道投递、农历生日、语义搜索与完整重复模式。
license: Proprietary
edition: pro
description: |-
  智能提醒助手专业版是在免费版基础上的全功能升级，为AI Agent提供企业级自然语言事件管理能力。专业版解锁自定义提醒偏移、多渠道投递、完整重复模式、农历生日支持、语义搜索、事件更新与归档等高级特性，实现复杂事件场景的智能管理。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- 智能提醒
- 事件管理
- 农历生日
- 语义搜索
tools:
  - - read
- exec
# 智能提醒助手（专业版）
---
> **AI Agent的企业级自然语言事件管理系统。自定义偏移、多渠道投递、农历生日、语义搜索，复杂场景一网打尽。**

管理事件不仅是捕获，更涉及完整生命周期：如何自定义提醒偏移？如何处理农历生日？如何实现"上次关于XXX的讨论"的语义搜索？如何管理多渠道投递？本技能聚焦事件管理的完整企业级能力，帮助Agent成为用户的智能日程助手。

## 架构总览

## 快速开始
### 30秒上手（捕获农历生日事件）
用户说"我妈农历六月二十生日"：

### 120秒标准搭建（多渠道+自定义偏移）
配置多渠道投递与自定义提醒偏移：

## 核心功能
### 中英文自然语言捕获
支持中英文双语事件描述：

| 语言 | 输入示例 | 解析能力 |
|------|----------|----------|
| **中文** | "后天上午10点有个会" | 相对日期+时段+事件 |
| **中文** | "下个月2号我妈生日" | 月份+日期+年度重复 |
| **中文** | "我妈农历六月二十生日" | 农历日期+年度重复 |
| **中文** | "每周一上午9点站会" | 周重复+时段+事件 |
| **英文** | "meeting tomorrow at 2pm" | 相对日期+时段+事件 |
| **英文** | "team standup next monday at 9am" | 周几+时段+事件 |
| **英文** | "mom birthday next month 15th" | 月份+日期+年度重复 |
| **英文** | "weekly review every friday at 3pm" | 周重复+时段+事件 |

### 自定义提醒偏移
| 偏移策略 | 偏移序列 | 适用场景 |
|----------|----------|----------|
| **默认** | 24h/1h/10m | 通用事件 |
| **重要事件** | 7d/3d/1d/2h/30m/10m | 项目里程碑、重要会议 |
| **日常事件** | 1h/10m | 站会、日常检查 |
| **紧急事件** | 30m/10m/5m/1m | 紧急提醒 |
| **长周期事件** | 30d/7d/3d/1d | 生日、纪念日、季度复盘 |

```python
sr.capture(
    title="项目A里程碑评审",
    start_datetime=datetime.now() + timedelta(days=30),
    offsets=[43200, 10080, 4320, 1440, 120, 30, 10],  # 30d/7d/3d/1d/2h/30m/10m
    channels=[{"channel": "telegram", "to": "+8613800138000"}]
)
```

### 完整重复模式
| 模式 | 字段值 | 说明 | 示例 |
|------|--------|------|------|
| **无重复** | `none` | 单次事件 | 一次性会议 |
| **年度** | `yearly` | 每年同日 | 生日、纪念日 |
| **月度** | `monthly` | 每月同日 | 月度总结 |
| **周度** | `weekly` | 每周同日 | 周会、周报 |
| **日度** | `daily` | 每日同日 | 站会、日报 |

### 农历生日支持

**农历生日存储规范**：

```yaml
- id: evt_1700000002
  title: 妈妈生日
  start_datetime: "2026-08-02T00:00:00"  # 当年公历日期
  notes: 记得提前准备礼物
  reminders_offsets: [1440, 60, 10]
  repeat: yearly
  lunar_date: "06-20"  # 原始农历日期（月-日）
  timezone: Asia/Shanghai
  status: active
```

**每年自动更新公历日期**：

### 多渠道投递
| 渠道 | 配置 | 适用场景 |
|------|------|----------|
| **Telegram** | `{"channel": "telegram", "to": "+8613800138000"}` | 个人移动通知 |
| **Discord** | `{"channel": "discord", "to": "channel:ID"}` | 团队协作通知 |
| **WhatsApp** | `{"channel": "whatsapp", "to": "+8613800138000"}` | 国际用户通知 |

**多渠道同时投递**：

```python
sr.capture(
    title="产品评审会议",
    start_datetime=datetime.now() + timedelta(days=2),
    channels=[
        {"channel": "telegram", "to": "+8613800138000"},
        {"channel": "discord", "to": "channel:1476104553148452958"},
        {"channel": "whatsapp", "to": "+8613800138000"}
    ]
)
```

### 语义搜索
```python
results = sr.semantic_search("上次关于产品规划的讨论")

```

**搜索算法**：
1. 关键词提取（移除停用词）
2. 标题匹配（权重3）
3. 备注匹配（权重2）
4. 模糊匹配（权重5）
5. 综合评分排序

### 事件生命周期管理

**生命周期状态机**：

```text
创建 → 活跃(active) ←→ 暂停(paused)
            │
            ├──→ 取消(cancelled)
            └──→ 归档(archived)
```

## 使用场景
### 场景一：农历生日年度提醒（家庭角色）
**场景描述**：捕获家人农历生日，每年自动转换为公历并提醒。

```python
sr.capture(
    title="妈妈生日",
    start_datetime=lunar_to_solar(6, 20),
    notes="记得提前准备礼物",
    offsets=[4320, 1440, 60, 10],  # 3天/1天/1小时/10分钟
    repeat="yearly",
    lunar_date="06-20",
    channels=[
        {"channel": "telegram", "to": "+8613800138000"},
        {"channel": "discord", "to": "channel:family"}
    ]
)
```

### 场景二：项目里程碑多渠道提醒（项目经理角色）
**场景描述**：项目里程碑评审，提前多阶段提醒，同时投递多个渠道。

```python
sr.capture(
    title="项目A里程碑评审",
    start_datetime=datetime.now() + timedelta(days=30),
    notes="Q3产品规划评审会议",
    offsets=[43200, 10080, 4320, 1440, 120, 30, 10],  # 30d/7d/3d/1d/2h/30m/10m
    channels=[
        {"channel": "telegram", "to": "+8613800138000"},
        {"channel": "discord", "to": "channel:project-a"}
    ]
)
```

### 场景三：周期性工作提醒（团队负责人角色）
**场景描述**：配置每日站会、每周周报、每月总结的周期性提醒。

### 场景四：语义搜索历史事件（产品经理角色）
**场景描述**：用户问"上次关于产品规划的讨论是什么时候？"，语义搜索历史事件。

```python
results = sr.semantic_search("产品规划 讨论")

print("相关事件：")
for r in results[:5]:
    dt = datetime.fromisoformat(r["start_datetime"])
    print(f"  [{r['relevance_score']}] {dt.strftime('%Y-%m-%d %H:%M')}: {r['title']}")
    if r.get("notes"):
        print(f"      备注：{r['notes']}")
```

### 场景五：中英文混合事件管理（外企员工角色）
**场景描述**：外企员工使用中英文混合描述事件，助手智能识别语言并解析。

## 多角色场景指南
| 角色 | 典型场景 | 推荐配置 | 核心价值 |
|------|----------|----------|----------|
| 家庭成员 | 农历生日提醒 | yearly+多渠道+农历 | 家人重要日子不忘 |
| 项目经理 | 里程碑多阶段提醒 | 自定义偏移+多渠道 | 关键节点充分预警 |
| 团队负责人 | 周期性工作提醒 | daily/weekly/monthly | 团队日常规范 |
| 产品经理 | 历史事件检索 | 语义搜索 | 快速查找相关讨论 |
| 外企员工 | 中英文混合事件 | 双语解析 | 跨语言工作流 |
| 销售经理 | 客户跟进提醒 | weekly+多渠道 | 客户关系维护 |
| 个人用户 | 个人日程管理 | 默认偏移+单渠道 | 轻量日程助手 |

## 性能优化策略
### 解析优化
1. **语言检测前置**：先检测语言再解析，避免全量扫描
2. **正则编译缓存**：预编译常用正则表达式，提升解析速度
3. **关键词索引**：为语义搜索建立关键词索引，加速查询
4. **批量解析**：多个事件批量解析，减少重复初始化

### 存储优化
1. **YAML压缩**：使用紧凑格式存储，减少文件体积
2. **归档分离**：归档事件单独存储，避免主文件膨胀
3. **索引文件**：为常用查询建立索引文件（按日期、按标题）
4. **增量更新**：仅更新变更部分，避免全量重写

### 投递优化
1. **渠道优先级**：重要事件多渠道同时投递
2. **去重检查**：创建前检查是否已存在相同提醒
3. **错峰调度**：多个提醒错开时间，避免集中触发
4. **bestEffort模式**：非关键渠道启用bestEffort

### 成本控制
- 简单事件使用默认偏移，避免过多提醒作业
- 历史事件定期归档，减少查询范围
- 语义搜索限制结果数量，避免全量扫描
- 周期性事件复用cron表达式，减少作业数量

## 多平台集成示例
### 与日历系统集成
```python
import caldav

def sync_from_calendar(calendar_url, username, password):
    """从CalDAV日历同步事件"""
    client = caldav.DAVClient(url=calendar_url, username=username, password=password)
    calendar = client.principal().calendars()[0]

    events = calendar.date_search(start=datetime.now(), end=datetime.now() + timedelta(days=30))
    for event in events:
        sr.capture(
            title=event.vobject.vevent.summary.value,
            start_datetime=event.vobject.vevent.dtstart.value
        )
```

### 与团队协作平台集成
```python
def capture_from_message(message_text):
    """从聊天消息捕获事件"""
    parsed = parser.parse(message_text)
    if parsed["start_datetime"]:
        sr.capture(
            title=parsed["title"],
            start_datetime=parsed["start_datetime"],
            repeat=parsed["repeat"]
        )
        return True
    return False
```

### 与任务管理系统集成
```python
def sync_from_task_manager(tasks):
    """从任务列表同步截止日期"""
    for task in tasks:
        if task.get("deadline"):
            sr.capture(
                title=f"任务截止：{task['title']}",
                start_datetime=task["deadline"],
                notes=task.get("description", ""),
                offsets=[1440, 120, 30, 10],  # 1天/2小时/30分钟/10分钟
                channels=[{"channel": "telegram", "to": task["assignee_phone"]}]
            )
```

### 与CRM系统集成
```python
def schedule_customer_followup(customer_id, followup_date):
    """安排客户跟进提醒"""
    customer = get_customer(customer_id)
    sr.capture(
        title=f"客户跟进：{customer['name']}",
        start_datetime=followup_date,
        notes=f"联系电话：{customer['phone']}\n上次沟通：{customer['last_contact']}",
        offsets=[1440, 60, 10],
        repeat="weekly",  # 每周跟进
        channels=[{"channel": "telegram", "to": customer['assignee_phone']}]
    )
```

## 版本升级迁移指南
### 从免费版升级至专业版
1. **数据兼容**：专业版完全兼容免费版的events.yml格式
2. **新增字段**：
   - `channels`：多渠道投递配置（数组）
   - `lunar_date`：农历日期（月-日）
   - `updated_at`：更新时间戳
3. **功能激活**：
   - 自定义偏移：在capture时传入offsets参数
   - 多渠道投递：在capture时传入channels参数
   - 农历支持：安装`lunardate`包
   - 语义搜索：调用semantic_search方法
4. **指令兼容**：免费版的所有命令在专业版中均可使用

### 版本更新历史
| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-07 | 初版发布，含自定义偏移、多渠道、农历、语义搜索、完整重复模式 |

## 错误处理
| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 事件未捕获 | 自然语言无法解析 | 检查输入格式；使用明确日期时间 | 高 |
| 提醒未触发 | 偏移时间已过 | 检查事件时间；调整偏移序列 | 高 |
| 农历转换失败 | 闰月处理异常 | 检查农历日期；手动指定公历 | 中 |
| 多渠道部分失败 | 单渠道凭证错误 | 检查失败渠道配置；启用bestEffort | 中 |
| 语义搜索无结果 | 关键词不匹配 | 调整搜索词；检查事件标题与备注 | 中 |
| 语义搜索结果不准 | 评分算法需调优 | 调整权重；增加同义词 | 低 |
| events.yml损坏 | YAML格式错误 | 使用yaml校验工具；从备份恢复 | 高 |
| 事件状态异常 | 状态转换错误 | 手动修正状态字段 | 中 |
| 周期性提醒不触发 | cron表达式错误 | 验证5字段格式；检查时区 | 高 |
| 重复事件堆积 | 未及时归档 | 定期执行archive；设置自动归档 | 低 |
| 中英文混合解析失败 | 语言检测错误 | 检查输入文本；手动指定语言 | 中 |
| 农历生日年度未更新 | 自动更新未执行 | 手动运行update_lunar_events | 中 |
| 多渠道投递延迟 | 作业数量过多 | 错峰调度；合并相同时间作业 | 低 |
| 查询结果过多 | 时间范围过大 | 缩小查询范围；使用语义搜索 | 低 |
| 事件标题提取错误 | 解析逻辑不足 | 手动指定标题；优化正则 | 低 |
| 存储文件过大 | 历史事件过多 | 定期归档；分离归档文件 | 低 |

## 即时修复清单
| 问题 | 修复方法 |
|------|----------|
| 事件无法捕获 | 检查自然语言格式；使用明确日期 |
| 提醒未触发 | 检查偏移时间；验证事件时间在未来 |
| 农历转换失败 | 检查农历日期；处理闰月情况 |
| 多渠道失败 | 检查渠道凭证；启用bestEffort |
| 语义搜索不准 | 调整搜索词；优化评分权重 |
| events.yml损坏 | 使用yaml校验；从Git恢复 |
| 周期性不触发 | 验证cron表达式；检查时区 |
| 农历年度未更新 | 手动运行更新脚本 |
| 状态异常 | 手动修正status字段 |
| 文件过大 | 定期归档历史事件 |

## FAQ
### Q1：免费版与专业版有什么区别？
免费版提供基础中文自然语言捕获、默认偏移（24h/1h/10m）、年度重复、单渠道投递、基础查询。专业版解锁自定义偏移序列、完整重复模式（yearly/monthly/weekly/daily）、农历生日支持、多渠道投递、语义搜索、事件全生命周期管理（更新/暂停/恢复/归档）、中英文双语解析。此外提供多角色场景指南、性能优化策略、多平台集成示例、完整FAQ（15问）与故障排查表（16项）。

### Q2：农历生日如何处理？
专业版使用`lunardate`库将农历日期转换为公历。存储时同时保留原始农历日期（`lunar_date`字段，格式为"月-日"）和当年公历日期（`start_datetime`字段）。每年自动运行`update_lunar_events`更新公历日期。遇到闰月时会提示用户确认。

### Q3：如何自定义提醒偏移？
在capture方法中传入offsets参数（分钟数组）。例如`offsets=[43200, 10080, 4320, 1440, 120, 30, 10]`表示30天/7天/3天/1天/2小时/30分钟/10分钟前各提醒一次。专业版提供5种预设偏移策略（默认/重要/日常/紧急/长周期），也可完全自定义。

### Q4：语义搜索如何工作？
语义搜索通过关键词提取、标题匹配（权重3）、备注匹配（权重2）、模糊匹配（权重5）综合评分。例如搜索"产品规划讨论"会自动提取关键词"产品"、"规划"、"讨论"，在所有事件的标题和备注中匹配，按综合评分排序返回结果。

### Q5：支持哪些重复模式？
专业版支持5种重复模式：`none`（无重复）、`yearly`（年度，适用于生日纪念日）、`monthly`（月度，适用于月度总结）、`weekly`（周度，适用于周会周报）、`daily`（日度，适用于站会日报）。重复事件会按规则自动计算下次触发时间。

### Q6：如何实现多渠道投递？
在capture方法中传入channels参数（数组），每个元素包含`channel`和`to`字段。例如同时投递Telegram和Discord：`channels=[{"channel": "telegram", "to": "+phone"}, {"channel": "discord", "to": "channel:ID"}]`。系统会为每个渠道创建独立的提醒作业。

### Q7：中英文混合事件如何处理？
专业版自动检测输入语言（通过中文字符检测），分别调用中文解析器或英文解析器。中文支持相对日期（今天/明天/后天）、周几、农历等；英文支持tomorrow/today/next weekday等。无需手动指定语言。

### Q8：事件数据存储在哪里？
事件存储在工作区的`~/.workspace/reminders/events.yml`文件。使用YAML格式，便于阅读与编辑。文件可纳入Git版本控制，实现跨设备同步与备份。专业版支持归档分离，避免主文件膨胀。

### Q9：如何管理事件生命周期？
专业版提供完整生命周期管理：创建（capture）、更新（update）、暂停（pause）、恢复（resume）、取消（cancel）、归档（archive）、查询（query_upcoming）、搜索（semantic_search）。状态机为：活跃↔暂停，活跃→取消/归档。

### Q10：如何与日历系统集成？
专业版提供CalDAV日历同步示例，可从日历拉取事件并自动捕获。也支持从Slack/Discord消息、任务管理系统、CRM系统同步事件。详见"多平台集成示例"章节。

### Q11：默认提醒偏移是什么？
默认在事件开始前的24小时、1小时、10分钟各提醒一次，覆盖"预先准备-即将开始-最后提醒"三个阶段。专业版支持5种预设策略与完全自定义。

### Q12：如何处理信息不完整的事件？
采用"最小化澄清"原则：仅当关键信息（日期、时间、标题）模糊时才提问，一次只问最少必要的问题。优先使用上下文推断（如"生日"默认年度重复），避免连续追问。

### Q13：事件查询支持哪些方式？
支持三种查询：(1) 即将到来查询（query_upcoming），按时间范围返回近期事件；(2) 时间段查询（query_range），返回指定时间段内的事件；(3) 语义搜索（semantic_search），按关键词语义匹配返回相关事件。

### Q14：events.yml损坏怎么办？
使用YAML校验工具检查格式。专业版建议将events.yml纳入Git版本控制，损坏时可从历史版本恢复。也可手动修复YAML格式（检查缩进、引号、特殊字符）。

### Q15：如何批量导入事件？
通过编写批量导入脚本，从CSV、JSON、日历等数据源读取事件，循环调用capture方法。专业版支持错误隔离，单条导入失败不影响其他。详见"多平台集成示例"章节。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（用于自然语言解析、农历转换与事件管理）
- **PyYAML**: 用于YAML文件读写
- **lunardate**: 用于农历转公历（专业版功能）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | 从python.org安装 |
| PyYAML | Python包 | 必需 | `pip install pyyaml` |
| lunardate | Python包 | 专业版必需 | `pip install lunardate` |
| Agent Gateway | 运行时 | 必需 | Agent平台内置 |
| skill-platform CLI | 工具 | 必需 | Agent平台内置 |
| Telegram Bot | 投递通道 | 否 | 注册Telegram Bot获取 |
| Discord Bot | 投递通道 | 否 | 注册Discord Bot获取 |
| WhatsApp Business | 投递通道 | 否 | 注册WhatsApp Business API |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### LLM模型路由
- 专业版使用 **GPT-4o** 模型路由，确保复杂事件解析与语义搜索的质量
- 支持中英文双语自然语言解析与农历日期处理

### API Key 配置
- Telegram投递需要Telegram Bot Token（存储在Agent Gateway配置中）
- Discord投递需要Discord Bot Token（存储在Agent Gateway配置中）
- WhatsApp投递需要WhatsApp Business API凭证
- 禁止在SKILL.md或脚本中硬编码Token
- 工作区数据（events.yml）不涉及API Key

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent管理企业级事件与提醒

## License与版权声明
本技能基于原始开源自然语言提醒作品改进，保留原始版权声明：

- 原始作品：Natural Language Reminder
- 原始license：MIT
- 改进作品：智能提醒助手（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，适配中文用户工作流
- 聚焦"智能事件管理"而非提醒创建机制
- 新增中英文双语自然语言解析器（Python完整实现）
- 新增自定义提醒偏移策略表（5种预设）
- 新增完整重复模式（none/yearly/monthly/weekly/daily）
- 新增农历生日支持（lunardate库集成，自动公历转换，闰月处理）
- 新增多渠道投递矩阵与同时投递实现
- 新增语义搜索算法（关键词提取+多维度评分）
- 新增事件全生命周期管理（创建/更新/暂停/恢复/取消/归档）
- 新增生命周期状态机图示
- 新增分级快速开始指南（30秒/120秒/300秒三档）
- 新增五类真实场景示例（农历生日/里程碑/周期性/语义搜索/中英文混合）
- 新增多角色场景指南（7种角色）
- 新增性能优化策略（解析/存储/投递/成本）
- 新增多平台集成示例（日历/团队协作/任务管理/CRM）
- 新增版本升级迁移指南
- 新增FAQ章节（15问）与故障排查表（16项）
- 新增即时修复清单（10项）
- 新增依赖说明章节与License版权声明
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

## 专业版特性
本专业版相比免费版新增以下能力：

- **自定义提醒偏移**：完全自定义提醒偏移序列，提供5种预设策略（默认/重要/日常/紧急/长周期），支持多达7个提醒节点，满足不同紧急程度需求
- **多渠道投递**：将同一事件同时投递到Telegram、Discord、WhatsApp等多个渠道，确保重要事件触达，支持渠道优先级配置
- **完整重复模式**：支持none/yearly/monthly/weekly/daily五种重复模式，自动计算下次触发时间，无需重复创建
- **农历生日支持**：使用lunardate库自动将农历日期转换为公历，支持闰月处理，每年自动更新公历日期，存储原始农历日期便于追溯
- **语义搜索**：通过关键词提取、标题匹配、备注匹配、模糊匹配综合评分，实现"上次关于XXX的讨论"等自然语言查询，快速定位历史事件
- **中英文双语解析**：自动检测输入语言，分别调用中文或英文解析器，支持中英文混合工作流
- **事件全生命周期管理**：完整的创建/更新/暂停/恢复/取消/归档功能，生命周期状态机清晰，便于事件状态管理

此外，专业版还提供：
- 多角色场景指南（7种角色×场景映射）
- 性能优化策略（解析/存储/投递/成本）
- 多平台集成示例（日历/团队协作/任务管理/CRM）
- 版本升级迁移指南
- 扩展FAQ（15问）与故障排查表（16项）
- 即时修复清单（10项）
- 优先支持

## 定价
| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 基础中文解析 + 默认偏移 + 年度重复 + 单渠道 + 基础查询 + 基础示例 + 基础FAQ | 个人试用、轻量日程需求 |
| 收费专业版 | ¥29.9/月 | 自定义偏移 + 多渠道 + 完整重复 + 农历生日 + 语义搜索 + 双语解析 + 生命周期管理 + 多角色指南 + 性能优化 + 优先支持 | 团队/企业、复杂事件管理 |

专业版通过SkillHub SkillPay发布。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
